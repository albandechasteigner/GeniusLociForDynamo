"""Finds pole of inaccessibility for a given polygon. Based on Vladimir Agafonkin's https://github.com/mapbox/polylabel"""
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

from math import sqrt
import time

import sys
sys.path.append(r"C:\Program Files (x86)\IronPython 2.7\Lib")
from Queue import PriorityQueue
inf = float("inf")

UIUnit = doc.GetUnits().GetFormatOptions(UnitType.UT_Length).DisplayUnits
mess=[]

def _point_to_polygon_distance(x, y, polygon):
    inside = False
    min_dist_sq = inf

    for ring in polygon:
        b = ring[-1]
        for a in ring:

            if ((a[1] &gt; y) != (b[1] &gt; y) and
                    (x &lt; (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0])):
                inside = not inside

            min_dist_sq = min(min_dist_sq, _get_seg_dist_sq(x, y, a, b))
            b = a

    result = sqrt(min_dist_sq)
    if not inside:
        return -result
    return result


def _get_seg_dist_sq(px, py, a, b):
    x = a[0]
    y = a[1]
    dx = b[0] - x
    dy = b[1] - y

    if dx != 0 or dy != 0:
        t = ((px - x) * dx + (py - y) * dy) / (dx * dx + dy * dy)

        if t &gt; 1:
            x = b[0]
            y = b[1]

        elif t &gt; 0:
            x += dx * t
            y += dy * t

    dx = px - x
    dy = py - y

    return dx * dx + dy * dy


class Cell(object):
    def __init__(self, x, y, h, polygon):
        self.h = h
        self.y = y
        self.x = x
        self.d = _point_to_polygon_distance(x, y, polygon)
        self.max = self.d + self.h * sqrt(2)

    def __lt__(self, other):
        return self.max &lt; other.max

    def __lte__(self, other):
        return self.max &lt;= other.max

    def __gt__(self, other):
        return self.max &gt; other.max

    def __gte__(self, other):
        return self.max &gt;= other.max

    def __eq__(self, other):
        return self.max == other.max


def _get_centroid_cell(polygon):
    area = 0
    x = 0
    y = 0
    points = polygon[0]
    b = points[-1]  # prev
    for a in points:
        f = a[0] * b[1] - b[0] * a[1]
        x += (a[0] + b[0]) * f
        y += (a[1] + b[1]) * f
        area += f * 3
        b = a
    if area == 0:
        return Cell(points[0][0], points[0][1], 0, polygon)
    return Cell(x / area, y / area, 0, polygon)
    pass


def polylabel(polygon, precision=1.0, debug=IN[1], with_distance=IN[2]):
    # find bounding box
    first_item = polygon[0][0]
    min_x = first_item[0]
    min_y = first_item[1]
    max_x = first_item[0]
    max_y = first_item[1]
    for p in polygon[0]:
        if p[0] &lt; min_x:
            min_x = p[0]
        if p[1] &lt; min_y:
            min_y = p[1]
        if p[0] &gt; max_x:
            max_x = p[0]
        if p[1] &gt; max_y:
            max_y = p[1]

    width = max_x - min_x
    height = max_y - min_y
    cell_size = min(width, height)
    h = cell_size / 2.0

    cell_queue = PriorityQueue()

    if cell_size == 0:
        if with_distance:
            return [min_x, min_y], None
        else:
            return [min_x, min_y]

    # cover polygon with initial cells
    x = min_x
    while x &lt; max_x:
        y = min_y
        while y &lt; max_y:
            c = Cell(x + h, y + h, h, polygon)
            y += cell_size
            cell_queue.put((-c.max, time.time(), c))
        x += cell_size

    best_cell = _get_centroid_cell(polygon)

    bbox_cell = Cell(min_x + width / 2, min_y + height / 2, 0, polygon)
    if bbox_cell.d &gt; best_cell.d:
        best_cell = bbox_cell

    num_of_probes = cell_queue.qsize()
    while not cell_queue.empty():
        _, __, cell = cell_queue.get()

        if cell.d &gt; best_cell.d:
            best_cell = cell

            if debug:
                mess.append('found best {} after {} probes'.format(
                    round(1e4 * UnitUtils.ConvertToInternalUnits(best_cell.d,UIUnit)) / 1e4, num_of_probes))

        if cell.max - best_cell.d &lt;= precision:
            continue

        h = cell.h / 2
        c = Cell(cell.x - h, cell.y - h, h, polygon)
        cell_queue.put((-c.max, time.time(), c))
        c = Cell(cell.x + h, cell.y - h, h, polygon)
        cell_queue.put((-c.max, time.time(), c))
        c = Cell(cell.x - h, cell.y + h, h, polygon)
        cell_queue.put((-c.max, time.time(), c))
        c = Cell(cell.x + h, cell.y + h, h, polygon)
        cell_queue.put((-c.max, time.time(), c))
        num_of_probes += 4

    if debug:
        mess.append('num probes: {}'.format(num_of_probes))
        mess.append('best distance: {}'.format(UnitUtils.ConvertToInternalUnits(best_cell.d,UIUnit)))
    if with_distance:
        return XYZ(best_cell.x, best_cell.y,z).ToPoint(),mess, UnitUtils.ConvertToInternalUnits(best_cell.d,UIUnit)
    else:
        return XYZ(best_cell.x, best_cell.y,z).ToPoint(), mess

items = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
curves,points=[],[]

#opt = Options()
#opt.IncludeNonVisibleObjects = True
#opt.View = doc.ActiveView
for item in items:
	geoEle=item.get_Geometry(Options())
	for geo in geoEle:
		if isinstance(geo, Autodesk.Revit.DB.Solid):
			sorted_faces=[sorted(geo.Faces,key=lambda face:face.Area, reverse=True) for face in geo.Faces][0]
			surface=sorted_faces[0].ToProtoType()
			for edges in sorted_faces[0].EdgeLoops:
				for edg in edges:
					curves.append(edg.AsCurve().ToProtoType())
					points.append([edg.AsCurve().GetEndPoint(0).X,edg.AsCurve().GetEndPoint(0).Y])
					z=edg.AsCurve().GetEndPoint(0).Z

OUT = surface,curves,polylabel([points])
