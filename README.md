[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/albandechasteigner/GeniusLociForDynamo/issues)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)
[![Current version](https://img.shields.io/badge/current%20version-2020.9.17-brightgreen.svg)](http://dynamopackages.com/)
[![Follow me on Twitter for updates](https://img.shields.io/twitter/follow/geniusloci_bim.svg?label=Follow&style=social)](https://twitter.com/geniusloci_bim) 

![Logo Genius Loci](https://github.com/albandechasteigner/GeniusLociForDynamo/blob/master/Logo%20Genius%20Loci.png)

***Genius Loci*** is a compilation of 300+ custom nodes for the [Dynamo](http://www.dynamobim.com/) environment.
The vast majority of nodes are written in Python and related to Revit.
Particular emphasis is placed on interoperability and many nodes can handle with DWG, DWF, NWC and IFC files.
Another goal is to interact easily with linked files and Revit documents. 
Other categories of nodes focus on automating dimensions and managing materials and graphics.

Genius Loci is compatible with Dynamo 2.x. Revit 2017 to Revit 2023.
Be sure to have the DynamoIronPython2.7 package installed for Dynamo 2.13.

Feedbacks, [issues](https://github.com/albandechasteigner/GeniusLociForDynamo/issues), [pull request](https://github.com/albandechasteigner/GeniusLociForDynamo/pulls) and suggestions for improvement are welcome and can be reported in the repository.

Some custom nodes were inspired by the brilliant authors of the packages like archi-lab.net, Clockwork and Springs and adapted to meet my needs.
Thanks to the original authors for their great Python scripts and for everything they taught me by analyzing them..

### INSTALLATION
Installation is simple - just use Dynamo's built-in package manager and search for `Genius Loci`.

### UPDATES

###### 21.05.18 Update nodes for Revit 2022 and add Export PDF. 
###### 21.01.12 Added CAD Block Location from DWG link, Closest Level, TextNote AddLeader, Family Properties, Documents Properties, All Elements of Family, Document Units nodes. 
###### 20.11.08 Fixed the Print PDF(multiple formats) node which only worked for Dynamo 2.6 in previous update "20.10.15".
###### 20.06.18 Added Delete Compound Layer, Material Add Image and Duct Surfaces References nodes
###### 20.05.14 Added Link DWF, Copy DWFMarkup and Print Settings Properties nodes.
###### 20.04.29 Added Group Lines by Orthogonality and Element Filter By Name (equals, contains, doesn't contain) nodes
###### 20.04.23 Added Parse and Export PAT File nodes, Purge using API. Improvement for the creation of tags on linked elements.
###### 20.04.16 Added nodes to batch create fill patterns, Element Inner Centroid and FamilyInstance.ByReference nodes.
###### 20.04.04 Added CAD Layer Overrides, Create Family Parameter and All Elements at Phase nodes. Updated Material Change Texture Path, CAD Layer Visibility and Set SubCategory Properties nodes.
###### 20.03.24 Added All Elements at Level+, Element Change Level, Element Origin Reference, Family Document, Reset Materials Properties, Material Find Texture Path and Dimension Properties nodes. Updated Create Material, Get Project Locations and Dimension ByReferences nodes.
###### 19.09.03 Revised custom node inputs for Dynamo 2.2
###### 19.08.23 Added AppearanceAsset Get Properties, Get and Set Material Properties, Link IFC nodes.
###### 19.05.27 Added Manage Worksets of RevitLinkInstance and Family Get SubCategory nodes.
###### 2019.5.6 Added FamilyInstance Reference Line, 3DView Toggle To Isometric, updated Export IFC.
###### 2019.2.22 Added Convert Linked Reference node
###### 2019.02.06 Updated Compound Surfaces References node. Added Compound Edges References, Create 3DView and Create Note Block Schedule nodes.
###### 2019.1.28 Updated Set SubCategory Properties. Added FamilyInstance Symbolic Lines, Set Wall JoinType, Wall Edges References, Element Points References and Set SystemType Properties nodes.
###### 2019.1.20 Added Get Elements at Ends and Get Joined Elements nodes.
###### 2019.1.14 Added Create Compound System FamilyType, Get SystemType Properties, Set SketchPlane By Line, Compound Surfaces References and Element Pattern Reference nodes.
###### 2019.01.01 Added FamilyInstance Reference, FamilyInstance ReferenceType, Wall Layer References, Element Reference, and Dimension ByReferences nodes.
###### 2018.12.17 Added Wall CompoundStructureLayersLocation and Tag Set Location nodes. Updated Create Line Pattern.
###### 2018.12.09 Updated Tag Get tagged Element node (it now works with tags on linked elements and linked rooms). Added View Range and Create Line Pattern nodes.
###### 2018.11.29 Added support for Foreground and Background Patterns in various nodes. New nodes : View SetElementOverrides, Material Create and Add AppearanceAssetElement, Material Set Render Appearance Color and FilledRegion Color Change nodes.
###### 2018.11.22 Added 3DView Lock or Unlock, 3DView Restore Orientation, Create Sheet List Schedule, Create View List Schedule, Get Pinned Element and Get Hidden Element nodes.
###### 2018.11.02 Added View Properties, Collector of UserWorksets, Collector of Detail Items Types, and Tag Get tagged Element nodes. Updated SelectByCategoryAnd3DView node.
###### 2018.10.20 Added Display Units, ReportRevitLinks and Reload Revit Links nodes.
###### 2018.10.16 New nodes to create Material, to set Rendering Color and Tint Color, to change Texture Path and to Get and Set Appearance Asset.
###### 2018.10.09 New nodes : Railing SetPath, Get/ Set and Create DWG Export Setup nodes, Purge Unused
###### 2018.10.02  Added Get Elements Overrides
###### 2018.09.16  Added Reload CADLinks. Updated Print PDF in document node.
###### 2018.09.05 New nodes : Get Phase Map, Collector of FillPatternElement, FilledRegion Pattern Change, Enumerate Datum Extent Type, Switch between 2D or 3D extent
###### 2018.08.27 Added the ability to tag linked elements to the node Create Independent Tag. New nodes : Tag Is Orphaned, Get Phase Filter Presentation, Get Phase Filter

#### SOURCE OF PACKAGE NAME
Genius Loci usually refers to a location's distinctive atmosphere or the spirit of the place. It's a familiar notion for architects. Automation should free up time to create a better architecture.
