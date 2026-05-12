####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
DatadiagramMLSimplified_CellType = Class(name="DatadiagramMLSimplified_CellType")
DatadiagramMLSimplified_VisioDocument = Class(name="DatadiagramMLSimplified_VisioDocument")
MastersCollection = Class(name="MastersCollection")
PagesCollection = Class(name="PagesCollection")
DatadiagramMLSimplified_UniqueIdElt = Class(name="DatadiagramMLSimplified_UniqueIdElt", is_abstract=True)
DatadiagramMLSimplified_Shape = Class(name="DatadiagramMLSimplified_Shape")
ShapesCollection = Class(name="ShapesCollection")
DatadiagramMLSimplified_PageSheet = Class(name="DatadiagramMLSimplified_PageSheet")
Shape = Class(name="Shape")
UniqueIdElt = Class(name="UniqueIdElt")
MasterElt = Class(name="MasterElt")
PageElt = Class(name="PageElt")
DatadiagramMLSimplified_NamedElt = Class(name="DatadiagramMLSimplified_NamedElt", is_abstract=True)
DatadiagramMLSimplified_IdentifiedElt = Class(name="DatadiagramMLSimplified_IdentifiedElt", is_abstract=True)
DatadiagramMLSimplified_IXElt = Class(name="DatadiagramMLSimplified_IXElt", is_abstract=True)
DatadiagramMLSimplified_DelElt = Class(name="DatadiagramMLSimplified_DelElt", is_abstract=True)
DatadiagramMLSimplified_Geom = Class(name="DatadiagramMLSimplified_Geom")
IXElt = Class(name="IXElt")
DelElt = Class(name="DelElt")
CellType = Class(name="CellType")
ShapeElt = Class(name="ShapeElt")
DatadiagramMLSimplified_ShapeElt = Class(name="DatadiagramMLSimplified_ShapeElt", is_abstract=True)
InfiniteLine = Class(name="InfiniteLine")
Ellipse = Class(name="Ellipse")
EllipticalArcTo = Class(name="EllipticalArcTo")
SplineStart = Class(name="SplineStart")
NURBSTo = Class(name="NURBSTo")
DatadiagramMLSimplified_XYElt = Class(name="DatadiagramMLSimplified_XYElt", is_abstract=True)
LineTo = Class(name="LineTo")
MoveTo = Class(name="MoveTo")
ArcTo = Class(name="ArcTo")
SplineKnot = Class(name="SplineKnot")
PolylineTo = Class(name="PolylineTo")
DatadiagramMLSimplified_ArcTo = Class(name="DatadiagramMLSimplified_ArcTo")
XYAElt = Class(name="XYAElt")
DatadiagramMLSimplified_SplineKnot = Class(name="DatadiagramMLSimplified_SplineKnot")
DatadiagramMLSimplified_PolylineTo = Class(name="DatadiagramMLSimplified_PolylineTo")
DatadiagramMLSimplified_XYABElt = Class(name="DatadiagramMLSimplified_XYABElt", is_abstract=True)
DatadiagramMLSimplified_LineTo = Class(name="DatadiagramMLSimplified_LineTo")
XYElt = Class(name="XYElt")
Geom = Class(name="Geom")
DatadiagramMLSimplified_MoveTo = Class(name="DatadiagramMLSimplified_MoveTo")
DatadiagramMLSimplified_XYAElt = Class(name="DatadiagramMLSimplified_XYAElt", is_abstract=True)
DatadiagramMLSimplified_EllipticalArcTo = Class(name="DatadiagramMLSimplified_EllipticalArcTo")
DatadiagramMLSimplified_SplineStart = Class(name="DatadiagramMLSimplified_SplineStart")
DatadiagramMLSimplified_XYABCDEElt = Class(name="DatadiagramMLSimplified_XYABCDEElt", is_abstract=True)
DatadiagramMLSimplified_NURBSTo = Class(name="DatadiagramMLSimplified_NURBSTo")
XYABCDEElt = Class(name="XYABCDEElt")
DatadiagramMLSimplified_Text = Class(name="DatadiagramMLSimplified_Text")
TextElt = Class(name="TextElt")
DatadiagramMLSimplified_InfiniteLine = Class(name="DatadiagramMLSimplified_InfiniteLine")
XYABElt = Class(name="XYABElt")
DatadiagramMLSimplified_XYABCDElt = Class(name="DatadiagramMLSimplified_XYABCDElt", is_abstract=True)
DatadiagramMLSimplified_Ellipse = Class(name="DatadiagramMLSimplified_Ellipse")
XYABCDElt = Class(name="XYABCDElt")
Icon = Class(name="Icon")
DatadiagramMLSimplified_Icon = Class(name="DatadiagramMLSimplified_Icon")
DatadiagramMLSimplified_Master = Class(name="DatadiagramMLSimplified_Master")
DatadiagramMLSimplified_TextElt = Class(name="DatadiagramMLSimplified_TextElt", is_abstract=True)
Text = Class(name="Text")
DatadiagramMLSimplified_StringElt = Class(name="DatadiagramMLSimplified_StringElt")
DatadiagramMLSimplified_MastersCollection = Class(name="DatadiagramMLSimplified_MastersCollection")
VisioDocument = Class(name="VisioDocument")
Master = Class(name="Master")
MasterShortCut = Class(name="MasterShortCut")
DatadiagramMLSimplified_MasterShortCut = Class(name="DatadiagramMLSimplified_MasterShortCut")
IdentifiedElt = Class(name="IdentifiedElt")
NamedElt = Class(name="NamedElt")
Connect = Class(name="Connect")
DatadiagramMLSimplified_Connect = Class(name="DatadiagramMLSimplified_Connect")
ConnectsCollection = Class(name="ConnectsCollection")
DatadiagramMLSimplified_MasterElt = Class(name="DatadiagramMLSimplified_MasterElt", is_abstract=True)
DatadiagramMLSimplified_PagesCollection = Class(name="DatadiagramMLSimplified_PagesCollection")
Page = Class(name="Page")
DatadiagramMLSimplified_Page = Class(name="DatadiagramMLSimplified_Page")
DatadiagramMLSimplified_ShapesCollection = Class(name="DatadiagramMLSimplified_ShapesCollection")
DatadiagramMLSimplified_ConnectsCollection = Class(name="DatadiagramMLSimplified_ConnectsCollection")
DatadiagramMLSimplified_PageElt = Class(name="DatadiagramMLSimplified_PageElt", is_abstract=True)

# DatadiagramMLSimplified_CellType class attributes and methods
DatadiagramMLSimplified_CellType_unit: Property = Property(name="unit", type=StringType)
DatadiagramMLSimplified_CellType_formula: Property = Property(name="formula", type=StringType)
DatadiagramMLSimplified_CellType_err: Property = Property(name="err", type=StringType)
DatadiagramMLSimplified_CellType_value: Property = Property(name="value", type=StringType)
DatadiagramMLSimplified_CellType.attributes={DatadiagramMLSimplified_CellType_formula, DatadiagramMLSimplified_CellType_unit, DatadiagramMLSimplified_CellType_value, DatadiagramMLSimplified_CellType_err}

# DatadiagramMLSimplified_VisioDocument class attributes and methods

# MastersCollection class attributes and methods

# PagesCollection class attributes and methods

# DatadiagramMLSimplified_UniqueIdElt class attributes and methods
DatadiagramMLSimplified_UniqueIdElt_UniqueID: Property = Property(name="UniqueID", type=StringType)
DatadiagramMLSimplified_UniqueIdElt.attributes={DatadiagramMLSimplified_UniqueIdElt_UniqueID}

# DatadiagramMLSimplified_Shape class attributes and methods
DatadiagramMLSimplified_Shape_lineStyle: Property = Property(name="lineStyle", type=StringType)
DatadiagramMLSimplified_Shape_fillStyle: Property = Property(name="fillStyle", type=StringType)
DatadiagramMLSimplified_Shape_textStyle: Property = Property(name="textStyle", type=StringType)
DatadiagramMLSimplified_Shape.attributes={DatadiagramMLSimplified_Shape_textStyle, DatadiagramMLSimplified_Shape_fillStyle, DatadiagramMLSimplified_Shape_lineStyle}

# ShapesCollection class attributes and methods

# DatadiagramMLSimplified_PageSheet class attributes and methods

# Shape class attributes and methods

# UniqueIdElt class attributes and methods

# MasterElt class attributes and methods

# PageElt class attributes and methods

# DatadiagramMLSimplified_NamedElt class attributes and methods
DatadiagramMLSimplified_NamedElt_name: Property = Property(name="name", type=StringType)
DatadiagramMLSimplified_NamedElt_nameU: Property = Property(name="nameU", type=StringType)
DatadiagramMLSimplified_NamedElt.attributes={DatadiagramMLSimplified_NamedElt_nameU, DatadiagramMLSimplified_NamedElt_name}

# DatadiagramMLSimplified_IdentifiedElt class attributes and methods
DatadiagramMLSimplified_IdentifiedElt_ID: Property = Property(name="ID", type=StringType)
DatadiagramMLSimplified_IdentifiedElt.attributes={DatadiagramMLSimplified_IdentifiedElt_ID}

# DatadiagramMLSimplified_IXElt class attributes and methods
DatadiagramMLSimplified_IXElt_iX: Property = Property(name="iX", type=StringType)
DatadiagramMLSimplified_IXElt.attributes={DatadiagramMLSimplified_IXElt_iX}

# DatadiagramMLSimplified_DelElt class attributes and methods
DatadiagramMLSimplified_DelElt_del_: Property = Property(name="del_", type=StringType)
DatadiagramMLSimplified_DelElt.attributes={DatadiagramMLSimplified_DelElt_del_}

# DatadiagramMLSimplified_Geom class attributes and methods

# IXElt class attributes and methods

# DelElt class attributes and methods

# CellType class attributes and methods

# ShapeElt class attributes and methods

# DatadiagramMLSimplified_ShapeElt class attributes and methods

# InfiniteLine class attributes and methods

# Ellipse class attributes and methods

# EllipticalArcTo class attributes and methods

# SplineStart class attributes and methods

# NURBSTo class attributes and methods

# DatadiagramMLSimplified_XYElt class attributes and methods

# LineTo class attributes and methods

# MoveTo class attributes and methods

# ArcTo class attributes and methods

# SplineKnot class attributes and methods

# PolylineTo class attributes and methods

# DatadiagramMLSimplified_ArcTo class attributes and methods

# XYAElt class attributes and methods

# DatadiagramMLSimplified_SplineKnot class attributes and methods

# DatadiagramMLSimplified_PolylineTo class attributes and methods

# DatadiagramMLSimplified_XYABElt class attributes and methods

# DatadiagramMLSimplified_LineTo class attributes and methods

# XYElt class attributes and methods

# Geom class attributes and methods

# DatadiagramMLSimplified_MoveTo class attributes and methods

# DatadiagramMLSimplified_XYAElt class attributes and methods

# DatadiagramMLSimplified_EllipticalArcTo class attributes and methods

# DatadiagramMLSimplified_SplineStart class attributes and methods

# DatadiagramMLSimplified_XYABCDEElt class attributes and methods

# DatadiagramMLSimplified_NURBSTo class attributes and methods

# XYABCDEElt class attributes and methods

# DatadiagramMLSimplified_Text class attributes and methods

# TextElt class attributes and methods

# DatadiagramMLSimplified_InfiniteLine class attributes and methods

# XYABElt class attributes and methods

# DatadiagramMLSimplified_XYABCDElt class attributes and methods

# DatadiagramMLSimplified_Ellipse class attributes and methods

# XYABCDElt class attributes and methods

# Icon class attributes and methods

# DatadiagramMLSimplified_Icon class attributes and methods
DatadiagramMLSimplified_Icon_value: Property = Property(name="value", type=StringType)
DatadiagramMLSimplified_Icon.attributes={DatadiagramMLSimplified_Icon_value}

# DatadiagramMLSimplified_Master class attributes and methods
DatadiagramMLSimplified_Master_baseID: Property = Property(name="baseID", type=StringType)
DatadiagramMLSimplified_Master_matchByName: Property = Property(name="matchByName", type=StringType)
DatadiagramMLSimplified_Master_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLSimplified_Master_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLSimplified_Master_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLSimplified_Master_hidden: Property = Property(name="hidden", type=StringType)
DatadiagramMLSimplified_Master_iconUpdate: Property = Property(name="iconUpdate", type=StringType)
DatadiagramMLSimplified_Master_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLSimplified_Master.attributes={DatadiagramMLSimplified_Master_matchByName, DatadiagramMLSimplified_Master_prompt, DatadiagramMLSimplified_Master_patternFlags, DatadiagramMLSimplified_Master_hidden, DatadiagramMLSimplified_Master_alignName, DatadiagramMLSimplified_Master_iconSize, DatadiagramMLSimplified_Master_baseID, DatadiagramMLSimplified_Master_iconUpdate}

# DatadiagramMLSimplified_TextElt class attributes and methods

# Text class attributes and methods

# DatadiagramMLSimplified_StringElt class attributes and methods
DatadiagramMLSimplified_StringElt_value: Property = Property(name="value", type=StringType)
DatadiagramMLSimplified_StringElt.attributes={DatadiagramMLSimplified_StringElt_value}

# DatadiagramMLSimplified_MastersCollection class attributes and methods

# VisioDocument class attributes and methods

# Master class attributes and methods

# MasterShortCut class attributes and methods

# DatadiagramMLSimplified_MasterShortCut class attributes and methods
DatadiagramMLSimplified_MasterShortCut_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLSimplified_MasterShortCut_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLSimplified_MasterShortCut_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLSimplified_MasterShortCut_shortcutURL: Property = Property(name="shortcutURL", type=StringType)
DatadiagramMLSimplified_MasterShortCut_shortcutHelp: Property = Property(name="shortcutHelp", type=StringType)
DatadiagramMLSimplified_MasterShortCut_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLSimplified_MasterShortCut.attributes={DatadiagramMLSimplified_MasterShortCut_iconSize, DatadiagramMLSimplified_MasterShortCut_shortcutHelp, DatadiagramMLSimplified_MasterShortCut_alignName, DatadiagramMLSimplified_MasterShortCut_patternFlags, DatadiagramMLSimplified_MasterShortCut_shortcutURL, DatadiagramMLSimplified_MasterShortCut_prompt}

# IdentifiedElt class attributes and methods

# NamedElt class attributes and methods

# Connect class attributes and methods

# DatadiagramMLSimplified_Connect class attributes and methods
DatadiagramMLSimplified_Connect_fromSheet: Property = Property(name="fromSheet", type=StringType)
DatadiagramMLSimplified_Connect_toSheet: Property = Property(name="toSheet", type=StringType)
DatadiagramMLSimplified_Connect_fromCell: Property = Property(name="fromCell", type=StringType)
DatadiagramMLSimplified_Connect_toCell: Property = Property(name="toCell", type=StringType)
DatadiagramMLSimplified_Connect_fromPart: Property = Property(name="fromPart", type=StringType)
DatadiagramMLSimplified_Connect_toPart: Property = Property(name="toPart", type=StringType)
DatadiagramMLSimplified_Connect.attributes={DatadiagramMLSimplified_Connect_toSheet, DatadiagramMLSimplified_Connect_toPart, DatadiagramMLSimplified_Connect_toCell, DatadiagramMLSimplified_Connect_fromCell, DatadiagramMLSimplified_Connect_fromSheet, DatadiagramMLSimplified_Connect_fromPart}

# ConnectsCollection class attributes and methods

# DatadiagramMLSimplified_MasterElt class attributes and methods

# DatadiagramMLSimplified_PagesCollection class attributes and methods

# Page class attributes and methods

# DatadiagramMLSimplified_Page class attributes and methods
DatadiagramMLSimplified_Page_background: Property = Property(name="background", type=StringType)
DatadiagramMLSimplified_Page_backPage: Property = Property(name="backPage", type=StringType)
DatadiagramMLSimplified_Page_viewScale: Property = Property(name="viewScale", type=StringType)
DatadiagramMLSimplified_Page_viewCenterX: Property = Property(name="viewCenterX", type=StringType)
DatadiagramMLSimplified_Page_ViewCenterY: Property = Property(name="ViewCenterY", type=StringType)
DatadiagramMLSimplified_Page_reviewerID: Property = Property(name="reviewerID", type=StringType)
DatadiagramMLSimplified_Page_associatedPage: Property = Property(name="associatedPage", type=StringType)
DatadiagramMLSimplified_Page.attributes={DatadiagramMLSimplified_Page_backPage, DatadiagramMLSimplified_Page_viewCenterX, DatadiagramMLSimplified_Page_viewScale, DatadiagramMLSimplified_Page_reviewerID, DatadiagramMLSimplified_Page_associatedPage, DatadiagramMLSimplified_Page_background, DatadiagramMLSimplified_Page_ViewCenterY}

# DatadiagramMLSimplified_ShapesCollection class attributes and methods

# DatadiagramMLSimplified_ConnectsCollection class attributes and methods

# DatadiagramMLSimplified_PageElt class attributes and methods

# Relationships
docMasters0: BinaryAssociation = BinaryAssociation(
    name="docMasters0",
    ends={
        Property(name="MastersCollection", type=DatadiagramMLSimplified_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ms_visioDocument", type=MastersCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPages1: BinaryAssociation = BinaryAssociation(
    name="docPages1",
    ends={
        Property(name="PagesCollection", type=DatadiagramMLSimplified_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument", type=PagesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noFill5: BinaryAssociation = BinaryAssociation(
    name="noFill5",
    ends={
        Property(name="CellType", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_Geom", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noLine6: BinaryAssociation = BinaryAssociation(
    name="noLine6",
    ends={
        Property(name="CellType8", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_Geom7", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ss_shapes2: BinaryAssociation = BinaryAssociation(
    name="ss_shapes2",
    ends={
        Property(name="ShapesCollection", type=DatadiagramMLSimplified_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="shapes", type=ShapesCollection, multiplicity=Multiplicity(1, 1))
    }
)
shapeElts3: BinaryAssociation = BinaryAssociation(
    name="shapeElts3",
    ends={
        Property(name="ShapeElt", type=DatadiagramMLSimplified_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="sse_shapeSheet", type=ShapeElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sse_shapeSheet4: BinaryAssociation = BinaryAssociation(
    name="sse_shapeSheet4",
    ends={
        Property(name="Shape", type=DatadiagramMLSimplified_ShapeElt, multiplicity=Multiplicity(1, 1)),
        Property(name="shapeElts", type=Shape, multiplicity=Multiplicity(1, 1))
    }
)
polylinesTo19: BinaryAssociation = BinaryAssociation(
    name="polylinesTo19",
    ends={
        Property(name="PolylineTo", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="pt_geom", type=PolylineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infiniteLines20: BinaryAssociation = BinaryAssociation(
    name="infiniteLines20",
    ends={
        Property(name="InfiniteLine", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="il_geom", type=InfiniteLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipses21: BinaryAssociation = BinaryAssociation(
    name="ellipses21",
    ends={
        Property(name="Ellipse", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="e_geom", type=Ellipse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipticalArcsTo22: BinaryAssociation = BinaryAssociation(
    name="ellipticalArcsTo22",
    ends={
        Property(name="EllipticalArcTo", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="eat_geom", type=EllipticalArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineStarts23: BinaryAssociation = BinaryAssociation(
    name="splineStarts23",
    ends={
        Property(name="SplineStart", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_geom", type=SplineStart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nurbsTo24: BinaryAssociation = BinaryAssociation(
    name="nurbsTo24",
    ends={
        Property(name="NURBSTo", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="nt_geom", type=NURBSTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
x25: BinaryAssociation = BinaryAssociation(
    name="x25",
    ends={
        Property(name="CellType26", type=DatadiagramMLSimplified_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
y27: BinaryAssociation = BinaryAssociation(
    name="y27",
    ends={
        Property(name="CellType29", type=DatadiagramMLSimplified_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYElt28", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noShow9: BinaryAssociation = BinaryAssociation(
    name="noShow9",
    ends={
        Property(name="CellType11", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_Geom10", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noSnap12: BinaryAssociation = BinaryAssociation(
    name="noSnap12",
    ends={
        Property(name="CellType14", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_Geom13", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linesTo15: BinaryAssociation = BinaryAssociation(
    name="linesTo15",
    ends={
        Property(name="LineTo", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="lt_geom", type=LineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movesTo16: BinaryAssociation = BinaryAssociation(
    name="movesTo16",
    ends={
        Property(name="MoveTo", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_geom", type=MoveTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcsTo17: BinaryAssociation = BinaryAssociation(
    name="arcsTo17",
    ends={
        Property(name="ArcTo", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ac_geom", type=ArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineKnots18: BinaryAssociation = BinaryAssociation(
    name="splineKnots18",
    ends={
        Property(name="SplineKnot", type=DatadiagramMLSimplified_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="sk_geom", type=SplineKnot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a33: BinaryAssociation = BinaryAssociation(
    name="a33",
    ends={
        Property(name="CellType34", type=DatadiagramMLSimplified_XYAElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYAElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ac_geom35: BinaryAssociation = BinaryAssociation(
    name="ac_geom35",
    ends={
        Property(name="Geom36", type=DatadiagramMLSimplified_ArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="arcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
sk_geom37: BinaryAssociation = BinaryAssociation(
    name="sk_geom37",
    ends={
        Property(name="Geom38", type=DatadiagramMLSimplified_SplineKnot, multiplicity=Multiplicity(1, 1)),
        Property(name="splineKnots", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
pt_geom39: BinaryAssociation = BinaryAssociation(
    name="pt_geom39",
    ends={
        Property(name="Geom40", type=DatadiagramMLSimplified_PolylineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="polylinesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
lt_geom30: BinaryAssociation = BinaryAssociation(
    name="lt_geom30",
    ends={
        Property(name="Geom", type=DatadiagramMLSimplified_LineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="linesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
mt_geom31: BinaryAssociation = BinaryAssociation(
    name="mt_geom31",
    ends={
        Property(name="Geom32", type=DatadiagramMLSimplified_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="movesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
e_geom50: BinaryAssociation = BinaryAssociation(
    name="e_geom50",
    ends={
        Property(name="ellipses", type=Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="Geom51", type=DatadiagramMLSimplified_Ellipse, multiplicity=Multiplicity(1, 1))
    }
)
eat_geom52: BinaryAssociation = BinaryAssociation(
    name="eat_geom52",
    ends={
        Property(name="Geom53", type=DatadiagramMLSimplified_EllipticalArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipticalArcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
ss_geom54: BinaryAssociation = BinaryAssociation(
    name="ss_geom54",
    ends={
        Property(name="Geom55", type=DatadiagramMLSimplified_SplineStart, multiplicity=Multiplicity(1, 1)),
        Property(name="splineStarts", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
e56: BinaryAssociation = BinaryAssociation(
    name="e56",
    ends={
        Property(name="CellType57", type=DatadiagramMLSimplified_XYABCDEElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYABCDEElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nt_geom58: BinaryAssociation = BinaryAssociation(
    name="nt_geom58",
    ends={
        Property(name="Geom59", type=DatadiagramMLSimplified_NURBSTo, multiplicity=Multiplicity(1, 1)),
        Property(name="nurbsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
b41: BinaryAssociation = BinaryAssociation(
    name="b41",
    ends={
        Property(name="CellType42", type=DatadiagramMLSimplified_XYABElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYABElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_geom43: BinaryAssociation = BinaryAssociation(
    name="il_geom43",
    ends={
        Property(name="Geom44", type=DatadiagramMLSimplified_InfiniteLine, multiplicity=Multiplicity(1, 1)),
        Property(name="infiniteLines", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
c45: BinaryAssociation = BinaryAssociation(
    name="c45",
    ends={
        Property(name="CellType46", type=DatadiagramMLSimplified_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYABCDElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d47: BinaryAssociation = BinaryAssociation(
    name="d47",
    ends={
        Property(name="CellType49", type=DatadiagramMLSimplified_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLSimplified_XYABCDElt48", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
icons67: BinaryAssociation = BinaryAssociation(
    name="icons67",
    ends={
        Property(name="Icon", type=DatadiagramMLSimplified_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="i_masterShortCut", type=Icon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i_masterShortCut68: BinaryAssociation = BinaryAssociation(
    name="i_masterShortCut68",
    ends={
        Property(name="MasterShortCut69", type=DatadiagramMLSimplified_Icon, multiplicity=Multiplicity(1, 1)),
        Property(name="icons", type=MasterShortCut, multiplicity=Multiplicity(1, 1))
    }
)
m_masters70: BinaryAssociation = BinaryAssociation(
    name="m_masters70",
    ends={
        Property(name="MastersCollection71", type=DatadiagramMLSimplified_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="masters", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
textElts60: BinaryAssociation = BinaryAssociation(
    name="textElts60",
    ends={
        Property(name="TextElt", type=DatadiagramMLSimplified_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="te_text", type=TextElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
te_text61: BinaryAssociation = BinaryAssociation(
    name="te_text61",
    ends={
        Property(name="Text", type=DatadiagramMLSimplified_TextElt, multiplicity=Multiplicity(1, 1)),
        Property(name="textElts", type=Text, multiplicity=Multiplicity(1, 1))
    }
)
ms_visioDocument62: BinaryAssociation = BinaryAssociation(
    name="ms_visioDocument62",
    ends={
        Property(name="VisioDocument", type=DatadiagramMLSimplified_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docMasters", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
masters63: BinaryAssociation = BinaryAssociation(
    name="masters63",
    ends={
        Property(name="Master", type=DatadiagramMLSimplified_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masters", type=Master, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
masterShortCuts64: BinaryAssociation = BinaryAssociation(
    name="masterShortCuts64",
    ends={
        Property(name="MasterShortCut", type=DatadiagramMLSimplified_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masterShortCuts", type=MasterShortCut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
m_masterShortCuts65: BinaryAssociation = BinaryAssociation(
    name="m_masterShortCuts65",
    ends={
        Property(name="MastersCollection66", type=DatadiagramMLSimplified_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="masterShortCuts", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
connections75: BinaryAssociation = BinaryAssociation(
    name="connections75",
    ends={
        Property(name="Connect", type=DatadiagramMLSimplified_ConnectsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_connects", type=Connect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_connects76: BinaryAssociation = BinaryAssociation(
    name="c_connects76",
    ends={
        Property(name="ConnectsCollection", type=DatadiagramMLSimplified_Connect, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=ConnectsCollection, multiplicity=Multiplicity(1, 1))
    }
)
me_master77: BinaryAssociation = BinaryAssociation(
    name="me_master77",
    ends={
        Property(name="Master78", type=DatadiagramMLSimplified_MasterElt, multiplicity=Multiplicity(1, 1)),
        Property(name="masterElts", type=Master, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument79: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument79",
    ends={
        Property(name="VisioDocument80", type=DatadiagramMLSimplified_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docPages", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
pages81: BinaryAssociation = BinaryAssociation(
    name="pages81",
    ends={
        Property(name="Page", type=DatadiagramMLSimplified_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="p_pages", type=Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
masterElts72: BinaryAssociation = BinaryAssociation(
    name="masterElts72",
    ends={
        Property(name="MasterElt", type=DatadiagramMLSimplified_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="me_master", type=MasterElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shapes73: BinaryAssociation = BinaryAssociation(
    name="shapes73",
    ends={
        Property(name="Shape74", type=DatadiagramMLSimplified_ShapesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_shapes", type=Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p_pages82: BinaryAssociation = BinaryAssociation(
    name="p_pages82",
    ends={
        Property(name="PagesCollection83", type=DatadiagramMLSimplified_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=PagesCollection, multiplicity=Multiplicity(1, 1))
    }
)
pageElts84: BinaryAssociation = BinaryAssociation(
    name="pageElts84",
    ends={
        Property(name="PageElt", type=DatadiagramMLSimplified_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pe_page", type=PageElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pe_page85: BinaryAssociation = BinaryAssociation(
    name="pe_page85",
    ends={
        Property(name="Page86", type=DatadiagramMLSimplified_PageElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pageElts", type=Page, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_DatadiagramMLSimplified_PageSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLSimplified_PageSheet)
gen_DatadiagramMLSimplified_PageSheet_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLSimplified_PageSheet)
gen_DatadiagramMLSimplified_PageSheet_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLSimplified_PageSheet)
gen_DatadiagramMLSimplified_PageSheet_PageElt = Generalization(general=PageElt, specific=DatadiagramMLSimplified_PageSheet)
gen_DatadiagramMLSimplified_Geom_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLSimplified_Geom)
gen_DatadiagramMLSimplified_Geom_IXElt = Generalization(general=IXElt, specific=DatadiagramMLSimplified_Geom)
gen_DatadiagramMLSimplified_Geom_DelElt = Generalization(general=DelElt, specific=DatadiagramMLSimplified_Geom)
gen_DatadiagramMLSimplified_XYElt_IXElt = Generalization(general=IXElt, specific=DatadiagramMLSimplified_XYElt)
gen_DatadiagramMLSimplified_XYElt_DelElt = Generalization(general=DelElt, specific=DatadiagramMLSimplified_XYElt)
gen_DatadiagramMLSimplified_ArcTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLSimplified_ArcTo)
gen_DatadiagramMLSimplified_SplineKnot_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLSimplified_SplineKnot)
gen_DatadiagramMLSimplified_PolylineTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLSimplified_PolylineTo)
gen_DatadiagramMLSimplified_XYABElt_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLSimplified_XYABElt)
gen_DatadiagramMLSimplified_LineTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLSimplified_LineTo)
gen_DatadiagramMLSimplified_MoveTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLSimplified_MoveTo)
gen_DatadiagramMLSimplified_XYAElt_XYElt = Generalization(general=XYElt, specific=DatadiagramMLSimplified_XYAElt)
gen_DatadiagramMLSimplified_EllipticalArcTo_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLSimplified_EllipticalArcTo)
gen_DatadiagramMLSimplified_SplineStart_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLSimplified_SplineStart)
gen_DatadiagramMLSimplified_XYABCDEElt_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLSimplified_XYABCDEElt)
gen_DatadiagramMLSimplified_NURBSTo_XYABCDEElt = Generalization(general=XYABCDEElt, specific=DatadiagramMLSimplified_NURBSTo)
gen_DatadiagramMLSimplified_Text_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLSimplified_Text)
gen_DatadiagramMLSimplified_InfiniteLine_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLSimplified_InfiniteLine)
gen_DatadiagramMLSimplified_XYABCDElt_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLSimplified_XYABCDElt)
gen_DatadiagramMLSimplified_Ellipse_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLSimplified_Ellipse)
gen_DatadiagramMLSimplified_Icon_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLSimplified_Icon)
gen_DatadiagramMLSimplified_Master_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLSimplified_Master)
gen_DatadiagramMLSimplified_Master_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLSimplified_Master)
gen_DatadiagramMLSimplified_Master_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLSimplified_Master)
gen_DatadiagramMLSimplified_StringElt_TextElt = Generalization(general=TextElt, specific=DatadiagramMLSimplified_StringElt)
gen_DatadiagramMLSimplified_MasterShortCut_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLSimplified_MasterShortCut)
gen_DatadiagramMLSimplified_MasterShortCut_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLSimplified_MasterShortCut)
gen_DatadiagramMLSimplified_Page_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLSimplified_Page)
gen_DatadiagramMLSimplified_ShapesCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLSimplified_ShapesCollection)
gen_DatadiagramMLSimplified_ShapesCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLSimplified_ShapesCollection)
gen_DatadiagramMLSimplified_ConnectsCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLSimplified_ConnectsCollection)
gen_DatadiagramMLSimplified_ConnectsCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLSimplified_ConnectsCollection)
gen_DatadiagramMLSimplified_Page_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLSimplified_Page)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={DatadiagramMLSimplified_CellType, DatadiagramMLSimplified_VisioDocument, MastersCollection, PagesCollection, DatadiagramMLSimplified_UniqueIdElt, DatadiagramMLSimplified_Shape, ShapesCollection, DatadiagramMLSimplified_PageSheet, Shape, UniqueIdElt, MasterElt, PageElt, DatadiagramMLSimplified_NamedElt, DatadiagramMLSimplified_IdentifiedElt, DatadiagramMLSimplified_IXElt, DatadiagramMLSimplified_DelElt, DatadiagramMLSimplified_Geom, IXElt, DelElt, CellType, ShapeElt, DatadiagramMLSimplified_ShapeElt, InfiniteLine, Ellipse, EllipticalArcTo, SplineStart, NURBSTo, DatadiagramMLSimplified_XYElt, LineTo, MoveTo, ArcTo, SplineKnot, PolylineTo, DatadiagramMLSimplified_ArcTo, XYAElt, DatadiagramMLSimplified_SplineKnot, DatadiagramMLSimplified_PolylineTo, DatadiagramMLSimplified_XYABElt, DatadiagramMLSimplified_LineTo, XYElt, Geom, DatadiagramMLSimplified_MoveTo, DatadiagramMLSimplified_XYAElt, DatadiagramMLSimplified_EllipticalArcTo, DatadiagramMLSimplified_SplineStart, DatadiagramMLSimplified_XYABCDEElt, DatadiagramMLSimplified_NURBSTo, XYABCDEElt, DatadiagramMLSimplified_Text, TextElt, DatadiagramMLSimplified_InfiniteLine, XYABElt, DatadiagramMLSimplified_XYABCDElt, DatadiagramMLSimplified_Ellipse, XYABCDElt, Icon, DatadiagramMLSimplified_Icon, DatadiagramMLSimplified_Master, DatadiagramMLSimplified_TextElt, Text, DatadiagramMLSimplified_StringElt, DatadiagramMLSimplified_MastersCollection, VisioDocument, Master, MasterShortCut, DatadiagramMLSimplified_MasterShortCut, IdentifiedElt, NamedElt, Connect, DatadiagramMLSimplified_Connect, ConnectsCollection, DatadiagramMLSimplified_MasterElt, DatadiagramMLSimplified_PagesCollection, Page, DatadiagramMLSimplified_Page, DatadiagramMLSimplified_ShapesCollection, DatadiagramMLSimplified_ConnectsCollection, DatadiagramMLSimplified_PageElt},
    associations={docMasters0, docPages1, noFill5, noLine6, ss_shapes2, shapeElts3, sse_shapeSheet4, polylinesTo19, infiniteLines20, ellipses21, ellipticalArcsTo22, splineStarts23, nurbsTo24, x25, y27, noShow9, noSnap12, linesTo15, movesTo16, arcsTo17, splineKnots18, a33, ac_geom35, sk_geom37, pt_geom39, lt_geom30, mt_geom31, e_geom50, eat_geom52, ss_geom54, e56, nt_geom58, b41, il_geom43, c45, d47, icons67, i_masterShortCut68, m_masters70, textElts60, te_text61, ms_visioDocument62, masters63, masterShortCuts64, m_masterShortCuts65, connections75, c_connects76, me_master77, ps_visioDocument79, pages81, masterElts72, shapes73, p_pages82, pageElts84, pe_page85},
    generalizations={gen_DatadiagramMLSimplified_PageSheet_Shape, gen_DatadiagramMLSimplified_PageSheet_UniqueIdElt, gen_DatadiagramMLSimplified_PageSheet_MasterElt, gen_DatadiagramMLSimplified_PageSheet_PageElt, gen_DatadiagramMLSimplified_Geom_ShapeElt, gen_DatadiagramMLSimplified_Geom_IXElt, gen_DatadiagramMLSimplified_Geom_DelElt, gen_DatadiagramMLSimplified_XYElt_IXElt, gen_DatadiagramMLSimplified_XYElt_DelElt, gen_DatadiagramMLSimplified_ArcTo_XYAElt, gen_DatadiagramMLSimplified_SplineKnot_XYAElt, gen_DatadiagramMLSimplified_PolylineTo_XYAElt, gen_DatadiagramMLSimplified_XYABElt_XYAElt, gen_DatadiagramMLSimplified_LineTo_XYElt, gen_DatadiagramMLSimplified_MoveTo_XYElt, gen_DatadiagramMLSimplified_XYAElt_XYElt, gen_DatadiagramMLSimplified_EllipticalArcTo_XYABCDElt, gen_DatadiagramMLSimplified_SplineStart_XYABCDElt, gen_DatadiagramMLSimplified_XYABCDEElt_XYABCDElt, gen_DatadiagramMLSimplified_NURBSTo_XYABCDEElt, gen_DatadiagramMLSimplified_Text_ShapeElt, gen_DatadiagramMLSimplified_InfiniteLine_XYABElt, gen_DatadiagramMLSimplified_XYABCDElt_XYABElt, gen_DatadiagramMLSimplified_Ellipse_XYABCDElt, gen_DatadiagramMLSimplified_Icon_MasterElt, gen_DatadiagramMLSimplified_Master_IdentifiedElt, gen_DatadiagramMLSimplified_Master_UniqueIdElt, gen_DatadiagramMLSimplified_Master_NamedElt, gen_DatadiagramMLSimplified_StringElt_TextElt, gen_DatadiagramMLSimplified_MasterShortCut_IdentifiedElt, gen_DatadiagramMLSimplified_MasterShortCut_NamedElt, gen_DatadiagramMLSimplified_Page_IdentifiedElt, gen_DatadiagramMLSimplified_ShapesCollection_MasterElt, gen_DatadiagramMLSimplified_ShapesCollection_PageElt, gen_DatadiagramMLSimplified_ConnectsCollection_MasterElt, gen_DatadiagramMLSimplified_ConnectsCollection_PageElt, gen_DatadiagramMLSimplified_Page_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)