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
DatadiagramMLTextFormat_CellType = Class(name="DatadiagramMLTextFormat_CellType")
DatadiagramMLTextFormat_VisioDocument = Class(name="DatadiagramMLTextFormat_VisioDocument")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
DocumentSettingsElt = Class(name="DocumentSettingsElt")
DatadiagramMLTextFormat_DateTimeType = Class(name="DatadiagramMLTextFormat_DateTimeType")
DocumentSheet = Class(name="DocumentSheet")
MastersCollection = Class(name="MastersCollection")
PagesCollection = Class(name="PagesCollection")
WindowsInfo = Class(name="WindowsInfo")
EventList = Class(name="EventList")
HeaderFooter = Class(name="HeaderFooter")
VBProjectData = Class(name="VBProjectData")
EmailRoutingData = Class(name="EmailRoutingData")
SolutionXML = Class(name="SolutionXML")
DatadiagramMLTextFormat_DocumentPropertiesCollection = Class(name="DatadiagramMLTextFormat_DocumentPropertiesCollection")
VisioDocument = Class(name="VisioDocument")
ColorsTable = Class(name="ColorsTable")
PrintSetup = Class(name="PrintSetup")
FontsTable = Class(name="FontsTable")
FaceNamesTable = Class(name="FaceNamesTable")
StyleSheetsCollection = Class(name="StyleSheetsCollection")
CustomPropertiesCollection = Class(name="CustomPropertiesCollection")
DateTimeType = Class(name="DateTimeType")
DatadiagramMLTextFormat_CustomProperty = Class(name="DatadiagramMLTextFormat_CustomProperty")
DatadiagramMLTextFormat_ColorsTable = Class(name="DatadiagramMLTextFormat_ColorsTable")
ColorEntry = Class(name="ColorEntry")
DatadiagramMLTextFormat_ColorEntry = Class(name="DatadiagramMLTextFormat_ColorEntry")
IXrequiredElt = Class(name="IXrequiredElt")
DatadiagramMLTextFormat_CustomPropertiesCollection = Class(name="DatadiagramMLTextFormat_CustomPropertiesCollection")
DatadiagramMLTextFormat_FontEntry = Class(name="DatadiagramMLTextFormat_FontEntry")
CustomProperty = Class(name="CustomProperty")
IdentifiedElt = Class(name="IdentifiedElt")
DatadiagramMLTextFormat_FaceNamesTable = Class(name="DatadiagramMLTextFormat_FaceNamesTable")
FaceName = Class(name="FaceName")
DatadiagramMLTextFormat_FaceName = Class(name="DatadiagramMLTextFormat_FaceName")
DatadiagramMLTextFormat_FontsTable = Class(name="DatadiagramMLTextFormat_FontsTable")
FontEntry = Class(name="FontEntry")
DatadiagramMLTextFormat_EmailRoutingData = Class(name="DatadiagramMLTextFormat_EmailRoutingData")
DatadiagramMLTextFormat_StyleSheetsCollection = Class(name="DatadiagramMLTextFormat_StyleSheetsCollection")
StyleSheet = Class(name="StyleSheet")
DatadiagramMLTextFormat_StyleSheet = Class(name="DatadiagramMLTextFormat_StyleSheet")
Shape = Class(name="Shape")
NamedElt = Class(name="NamedElt")
DatadiagramMLTextFormat_DocumentSheet = Class(name="DatadiagramMLTextFormat_DocumentSheet")
PageSheet = Class(name="PageSheet")
DatadiagramMLTextFormat_VBProjectData = Class(name="DatadiagramMLTextFormat_VBProjectData")
DatadiagramMLTextFormat_IdentifiedElt = Class(name="DatadiagramMLTextFormat_IdentifiedElt", is_abstract=True)
DatadiagramMLTextFormat_UniqueIdElt = Class(name="DatadiagramMLTextFormat_UniqueIdElt", is_abstract=True)
DatadiagramMLTextFormat_Shape = Class(name="DatadiagramMLTextFormat_Shape")
ShapesCollection = Class(name="ShapesCollection")
ShapeElt = Class(name="ShapeElt")
DatadiagramMLTextFormat_ShapeElt = Class(name="DatadiagramMLTextFormat_ShapeElt", is_abstract=True)
DatadiagramMLTextFormat_PageSheet = Class(name="DatadiagramMLTextFormat_PageSheet")
UniqueIdElt = Class(name="UniqueIdElt")
MasterElt = Class(name="MasterElt")
PageElt = Class(name="PageElt")
DatadiagramMLTextFormat_NamedElt = Class(name="DatadiagramMLTextFormat_NamedElt", is_abstract=True)
DatadiagramMLTextFormat_Geom = Class(name="DatadiagramMLTextFormat_Geom")
IXElt = Class(name="IXElt")
DelElt = Class(name="DelElt")
CellType = Class(name="CellType")
LineTo = Class(name="LineTo")
MoveTo = Class(name="MoveTo")
DatadiagramMLTextFormat_IXElt = Class(name="DatadiagramMLTextFormat_IXElt", is_abstract=True)
DatadiagramMLTextFormat_DelElt = Class(name="DatadiagramMLTextFormat_DelElt", is_abstract=True)
PolylineTo = Class(name="PolylineTo")
InfiniteLine = Class(name="InfiniteLine")
Ellipse = Class(name="Ellipse")
EllipticalArcTo = Class(name="EllipticalArcTo")
SplineStart = Class(name="SplineStart")
NURBSTo = Class(name="NURBSTo")
ArcTo = Class(name="ArcTo")
SplineKnot = Class(name="SplineKnot")
DatadiagramMLTextFormat_LineTo = Class(name="DatadiagramMLTextFormat_LineTo")
XYElt = Class(name="XYElt")
Geom = Class(name="Geom")
DatadiagramMLTextFormat_MoveTo = Class(name="DatadiagramMLTextFormat_MoveTo")
DatadiagramMLTextFormat_XYAElt = Class(name="DatadiagramMLTextFormat_XYAElt", is_abstract=True)
DatadiagramMLTextFormat_ArcTo = Class(name="DatadiagramMLTextFormat_ArcTo")
XYAElt = Class(name="XYAElt")
DatadiagramMLTextFormat_XYElt = Class(name="DatadiagramMLTextFormat_XYElt", is_abstract=True)
DatadiagramMLTextFormat_XYABElt = Class(name="DatadiagramMLTextFormat_XYABElt", is_abstract=True)
DatadiagramMLTextFormat_InfiniteLine = Class(name="DatadiagramMLTextFormat_InfiniteLine")
XYABElt = Class(name="XYABElt")
DatadiagramMLTextFormat_XYABCDElt = Class(name="DatadiagramMLTextFormat_XYABCDElt", is_abstract=True)
DatadiagramMLTextFormat_SplineKnot = Class(name="DatadiagramMLTextFormat_SplineKnot")
DatadiagramMLTextFormat_PolylineTo = Class(name="DatadiagramMLTextFormat_PolylineTo")
DatadiagramMLTextFormat_SplineStart = Class(name="DatadiagramMLTextFormat_SplineStart")
DatadiagramMLTextFormat_XYABCDEElt = Class(name="DatadiagramMLTextFormat_XYABCDEElt", is_abstract=True)
DatadiagramMLTextFormat_NURBSTo = Class(name="DatadiagramMLTextFormat_NURBSTo")
XYABCDEElt = Class(name="XYABCDEElt")
DatadiagramMLTextFormat_Text = Class(name="DatadiagramMLTextFormat_Text")
TextElt = Class(name="TextElt")
DatadiagramMLTextFormat_Ellipse = Class(name="DatadiagramMLTextFormat_Ellipse")
XYABCDElt = Class(name="XYABCDElt")
DatadiagramMLTextFormat_EllipticalArcTo = Class(name="DatadiagramMLTextFormat_EllipticalArcTo")
DatadiagramMLTextFormat_Cp = Class(name="DatadiagramMLTextFormat_Cp")
DatadiagramMLTextFormat_Pp = Class(name="DatadiagramMLTextFormat_Pp")
DatadiagramMLTextFormat_Tp = Class(name="DatadiagramMLTextFormat_Tp")
DatadiagramMLTextFormat_Fld = Class(name="DatadiagramMLTextFormat_Fld")
DatadiagramMLTextFormat_StringElt = Class(name="DatadiagramMLTextFormat_StringElt")
DatadiagramMLTextFormat_Char = Class(name="DatadiagramMLTextFormat_Char")
DatadiagramMLTextFormat_TextElt = Class(name="DatadiagramMLTextFormat_TextElt", is_abstract=True)
Text = Class(name="Text")
DatadiagramMLTextFormat_IXrequiredElt = Class(name="DatadiagramMLTextFormat_IXrequiredElt", is_abstract=True)
DatadiagramMLTextFormat_Para = Class(name="DatadiagramMLTextFormat_Para")
DatadiagramMLTextFormat_TabsCollection = Class(name="DatadiagramMLTextFormat_TabsCollection")
Tab = Class(name="Tab")
DatadiagramMLTextFormat_Tab = Class(name="DatadiagramMLTextFormat_Tab")
TabsCollection = Class(name="TabsCollection")
DatadiagramMLTextFormat_Field = Class(name="DatadiagramMLTextFormat_Field")
DatadiagramMLTextFormat_MastersCollection = Class(name="DatadiagramMLTextFormat_MastersCollection")
Master = Class(name="Master")
MasterShortCut = Class(name="MasterShortCut")
DatadiagramMLTextFormat_MasterShortCut = Class(name="DatadiagramMLTextFormat_MasterShortCut")
Icon = Class(name="Icon")
DatadiagramMLTextFormat_Icon = Class(name="DatadiagramMLTextFormat_Icon")
DatadiagramMLTextFormat_Master = Class(name="DatadiagramMLTextFormat_Master")
DatadiagramMLTextFormat_ShapesCollection = Class(name="DatadiagramMLTextFormat_ShapesCollection")
Page = Class(name="Page")
DatadiagramMLTextFormat_ConnectsCollection = Class(name="DatadiagramMLTextFormat_ConnectsCollection")
Connect = Class(name="Connect")
DatadiagramMLTextFormat_Connect = Class(name="DatadiagramMLTextFormat_Connect")
ConnectsCollection = Class(name="ConnectsCollection")
DatadiagramMLTextFormat_MasterElt = Class(name="DatadiagramMLTextFormat_MasterElt", is_abstract=True)
DatadiagramMLTextFormat_PagesCollection = Class(name="DatadiagramMLTextFormat_PagesCollection")
DatadiagramMLTextFormat_PrintSetup = Class(name="DatadiagramMLTextFormat_PrintSetup")
DatadiagramMLTextFormat_Page = Class(name="DatadiagramMLTextFormat_Page")
DatadiagramMLTextFormat_PageElt = Class(name="DatadiagramMLTextFormat_PageElt", is_abstract=True)
DatadiagramMLTextFormat_DocumentSettingsElt = Class(name="DatadiagramMLTextFormat_DocumentSettingsElt")
DatadiagramMLTextFormat_WindowsInfo = Class(name="DatadiagramMLTextFormat_WindowsInfo")
DatadiagramMLTextFormat_EventList = Class(name="DatadiagramMLTextFormat_EventList")
DatadiagramMLTextFormat_HeaderFooter = Class(name="DatadiagramMLTextFormat_HeaderFooter")
DatadiagramMLTextFormat_SolutionXML = Class(name="DatadiagramMLTextFormat_SolutionXML")

# DatadiagramMLTextFormat_CellType class attributes and methods
DatadiagramMLTextFormat_CellType_unit: Property = Property(name="unit", type=StringType)
DatadiagramMLTextFormat_CellType_formula: Property = Property(name="formula", type=StringType)
DatadiagramMLTextFormat_CellType_err: Property = Property(name="err", type=StringType)
DatadiagramMLTextFormat_CellType_value: Property = Property(name="value", type=StringType)
DatadiagramMLTextFormat_CellType.attributes={DatadiagramMLTextFormat_CellType_formula, DatadiagramMLTextFormat_CellType_unit, DatadiagramMLTextFormat_CellType_err, DatadiagramMLTextFormat_CellType_value}

# DatadiagramMLTextFormat_VisioDocument class attributes and methods
DatadiagramMLTextFormat_VisioDocument_start: Property = Property(name="start", type=StringType)
DatadiagramMLTextFormat_VisioDocument_key: Property = Property(name="key", type=StringType)
DatadiagramMLTextFormat_VisioDocument_metric: Property = Property(name="metric", type=StringType)
DatadiagramMLTextFormat_VisioDocument_buildnum: Property = Property(name="buildnum", type=StringType)
DatadiagramMLTextFormat_VisioDocument_version: Property = Property(name="version", type=StringType)
DatadiagramMLTextFormat_VisioDocument_docLangId: Property = Property(name="docLangId", type=StringType)
DatadiagramMLTextFormat_VisioDocument.attributes={DatadiagramMLTextFormat_VisioDocument_docLangId, DatadiagramMLTextFormat_VisioDocument_version, DatadiagramMLTextFormat_VisioDocument_metric, DatadiagramMLTextFormat_VisioDocument_start, DatadiagramMLTextFormat_VisioDocument_buildnum, DatadiagramMLTextFormat_VisioDocument_key}

# DocumentPropertiesCollection class attributes and methods

# DocumentSettingsElt class attributes and methods

# DatadiagramMLTextFormat_DateTimeType class attributes and methods
DatadiagramMLTextFormat_DateTimeType_day: Property = Property(name="day", type=StringType)
DatadiagramMLTextFormat_DateTimeType_hour: Property = Property(name="hour", type=StringType)
DatadiagramMLTextFormat_DateTimeType_minute: Property = Property(name="minute", type=StringType)
DatadiagramMLTextFormat_DateTimeType_second: Property = Property(name="second", type=StringType)
DatadiagramMLTextFormat_DateTimeType_year: Property = Property(name="year", type=StringType)
DatadiagramMLTextFormat_DateTimeType_month: Property = Property(name="month", type=StringType)
DatadiagramMLTextFormat_DateTimeType.attributes={DatadiagramMLTextFormat_DateTimeType_month, DatadiagramMLTextFormat_DateTimeType_second, DatadiagramMLTextFormat_DateTimeType_hour, DatadiagramMLTextFormat_DateTimeType_year, DatadiagramMLTextFormat_DateTimeType_minute, DatadiagramMLTextFormat_DateTimeType_day}

# DocumentSheet class attributes and methods

# MastersCollection class attributes and methods

# PagesCollection class attributes and methods

# WindowsInfo class attributes and methods

# EventList class attributes and methods

# HeaderFooter class attributes and methods

# VBProjectData class attributes and methods

# EmailRoutingData class attributes and methods

# SolutionXML class attributes and methods

# DatadiagramMLTextFormat_DocumentPropertiesCollection class attributes and methods
DatadiagramMLTextFormat_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_hyperlinkBase_href: Property = Property(name="hyperlinkBase_href", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_alternateNames: Property = Property(name="alternateNames", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_template: Property = Property(name="template", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_buildNumberCreated: Property = Property(name="buildNumberCreated", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_buildNumberEdited: Property = Property(name="buildNumberEdited", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_creator: Property = Property(name="creator", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
DatadiagramMLTextFormat_DocumentPropertiesCollection.attributes={DatadiagramMLTextFormat_DocumentPropertiesCollection_manager, DatadiagramMLTextFormat_DocumentPropertiesCollection_category, DatadiagramMLTextFormat_DocumentPropertiesCollection_subject, DatadiagramMLTextFormat_DocumentPropertiesCollection_hyperlinkBase_href, DatadiagramMLTextFormat_DocumentPropertiesCollection_template, DatadiagramMLTextFormat_DocumentPropertiesCollection_company, DatadiagramMLTextFormat_DocumentPropertiesCollection_title, DatadiagramMLTextFormat_DocumentPropertiesCollection_description, DatadiagramMLTextFormat_DocumentPropertiesCollection_alternateNames, DatadiagramMLTextFormat_DocumentPropertiesCollection_buildNumberEdited, DatadiagramMLTextFormat_DocumentPropertiesCollection_keywords, DatadiagramMLTextFormat_DocumentPropertiesCollection_creator, DatadiagramMLTextFormat_DocumentPropertiesCollection_buildNumberCreated}

# VisioDocument class attributes and methods

# ColorsTable class attributes and methods

# PrintSetup class attributes and methods

# FontsTable class attributes and methods

# FaceNamesTable class attributes and methods

# StyleSheetsCollection class attributes and methods

# CustomPropertiesCollection class attributes and methods

# DateTimeType class attributes and methods

# DatadiagramMLTextFormat_CustomProperty class attributes and methods
DatadiagramMLTextFormat_CustomProperty_name: Property = Property(name="name", type=StringType)
DatadiagramMLTextFormat_CustomProperty_dataType: Property = Property(name="dataType", type=StringType)
DatadiagramMLTextFormat_CustomProperty.attributes={DatadiagramMLTextFormat_CustomProperty_name, DatadiagramMLTextFormat_CustomProperty_dataType}

# DatadiagramMLTextFormat_ColorsTable class attributes and methods

# ColorEntry class attributes and methods

# DatadiagramMLTextFormat_ColorEntry class attributes and methods
DatadiagramMLTextFormat_ColorEntry_rgb: Property = Property(name="rgb", type=StringType)
DatadiagramMLTextFormat_ColorEntry.attributes={DatadiagramMLTextFormat_ColorEntry_rgb}

# IXrequiredElt class attributes and methods

# DatadiagramMLTextFormat_CustomPropertiesCollection class attributes and methods

# DatadiagramMLTextFormat_FontEntry class attributes and methods
DatadiagramMLTextFormat_FontEntry_name: Property = Property(name="name", type=StringType)
DatadiagramMLTextFormat_FontEntry_charSet: Property = Property(name="charSet", type=StringType)
DatadiagramMLTextFormat_FontEntry_pitchAndFamily: Property = Property(name="pitchAndFamily", type=StringType)
DatadiagramMLTextFormat_FontEntry_attributes: Property = Property(name="attributes", type=StringType)
DatadiagramMLTextFormat_FontEntry_weight: Property = Property(name="weight", type=StringType)
DatadiagramMLTextFormat_FontEntry_unicode: Property = Property(name="unicode", type=StringType)
DatadiagramMLTextFormat_FontEntry.attributes={DatadiagramMLTextFormat_FontEntry_charSet, DatadiagramMLTextFormat_FontEntry_unicode, DatadiagramMLTextFormat_FontEntry_pitchAndFamily, DatadiagramMLTextFormat_FontEntry_name, DatadiagramMLTextFormat_FontEntry_attributes, DatadiagramMLTextFormat_FontEntry_weight}

# CustomProperty class attributes and methods

# IdentifiedElt class attributes and methods

# DatadiagramMLTextFormat_FaceNamesTable class attributes and methods

# FaceName class attributes and methods

# DatadiagramMLTextFormat_FaceName class attributes and methods
DatadiagramMLTextFormat_FaceName_name: Property = Property(name="name", type=StringType)
DatadiagramMLTextFormat_FaceName_unicodeRanges: Property = Property(name="unicodeRanges", type=StringType)
DatadiagramMLTextFormat_FaceName_charSet: Property = Property(name="charSet", type=StringType)
DatadiagramMLTextFormat_FaceName_panos: Property = Property(name="panos", type=StringType)
DatadiagramMLTextFormat_FaceName_flags: Property = Property(name="flags", type=StringType)
DatadiagramMLTextFormat_FaceName.attributes={DatadiagramMLTextFormat_FaceName_panos, DatadiagramMLTextFormat_FaceName_charSet, DatadiagramMLTextFormat_FaceName_name, DatadiagramMLTextFormat_FaceName_flags, DatadiagramMLTextFormat_FaceName_unicodeRanges}

# DatadiagramMLTextFormat_FontsTable class attributes and methods

# FontEntry class attributes and methods

# DatadiagramMLTextFormat_EmailRoutingData class attributes and methods
DatadiagramMLTextFormat_EmailRoutingData_data: Property = Property(name="data", type=StringType)
DatadiagramMLTextFormat_EmailRoutingData_size: Property = Property(name="size", type=StringType)
DatadiagramMLTextFormat_EmailRoutingData.attributes={DatadiagramMLTextFormat_EmailRoutingData_size, DatadiagramMLTextFormat_EmailRoutingData_data}

# DatadiagramMLTextFormat_StyleSheetsCollection class attributes and methods

# StyleSheet class attributes and methods

# DatadiagramMLTextFormat_StyleSheet class attributes and methods

# Shape class attributes and methods

# NamedElt class attributes and methods

# DatadiagramMLTextFormat_DocumentSheet class attributes and methods

# PageSheet class attributes and methods

# DatadiagramMLTextFormat_VBProjectData class attributes and methods
DatadiagramMLTextFormat_VBProjectData_data: Property = Property(name="data", type=StringType)
DatadiagramMLTextFormat_VBProjectData.attributes={DatadiagramMLTextFormat_VBProjectData_data}

# DatadiagramMLTextFormat_IdentifiedElt class attributes and methods
DatadiagramMLTextFormat_IdentifiedElt_ID: Property = Property(name="ID", type=StringType)
DatadiagramMLTextFormat_IdentifiedElt.attributes={DatadiagramMLTextFormat_IdentifiedElt_ID}

# DatadiagramMLTextFormat_UniqueIdElt class attributes and methods
DatadiagramMLTextFormat_UniqueIdElt_UniqueID: Property = Property(name="UniqueID", type=StringType)
DatadiagramMLTextFormat_UniqueIdElt.attributes={DatadiagramMLTextFormat_UniqueIdElt_UniqueID}

# DatadiagramMLTextFormat_Shape class attributes and methods
DatadiagramMLTextFormat_Shape_lineStyle: Property = Property(name="lineStyle", type=StringType)
DatadiagramMLTextFormat_Shape_fillStyle: Property = Property(name="fillStyle", type=StringType)
DatadiagramMLTextFormat_Shape_textStyle: Property = Property(name="textStyle", type=StringType)
DatadiagramMLTextFormat_Shape.attributes={DatadiagramMLTextFormat_Shape_textStyle, DatadiagramMLTextFormat_Shape_lineStyle, DatadiagramMLTextFormat_Shape_fillStyle}

# ShapesCollection class attributes and methods

# ShapeElt class attributes and methods

# DatadiagramMLTextFormat_ShapeElt class attributes and methods

# DatadiagramMLTextFormat_PageSheet class attributes and methods

# UniqueIdElt class attributes and methods

# MasterElt class attributes and methods

# PageElt class attributes and methods

# DatadiagramMLTextFormat_NamedElt class attributes and methods
DatadiagramMLTextFormat_NamedElt_name: Property = Property(name="name", type=StringType)
DatadiagramMLTextFormat_NamedElt_nameU: Property = Property(name="nameU", type=StringType)
DatadiagramMLTextFormat_NamedElt.attributes={DatadiagramMLTextFormat_NamedElt_name, DatadiagramMLTextFormat_NamedElt_nameU}

# DatadiagramMLTextFormat_Geom class attributes and methods

# IXElt class attributes and methods

# DelElt class attributes and methods

# CellType class attributes and methods

# LineTo class attributes and methods

# MoveTo class attributes and methods

# DatadiagramMLTextFormat_IXElt class attributes and methods
DatadiagramMLTextFormat_IXElt_iX: Property = Property(name="iX", type=StringType)
DatadiagramMLTextFormat_IXElt.attributes={DatadiagramMLTextFormat_IXElt_iX}

# DatadiagramMLTextFormat_DelElt class attributes and methods
DatadiagramMLTextFormat_DelElt_del_: Property = Property(name="del_", type=StringType)
DatadiagramMLTextFormat_DelElt.attributes={DatadiagramMLTextFormat_DelElt_del_}

# PolylineTo class attributes and methods

# InfiniteLine class attributes and methods

# Ellipse class attributes and methods

# EllipticalArcTo class attributes and methods

# SplineStart class attributes and methods

# NURBSTo class attributes and methods

# ArcTo class attributes and methods

# SplineKnot class attributes and methods

# DatadiagramMLTextFormat_LineTo class attributes and methods

# XYElt class attributes and methods

# Geom class attributes and methods

# DatadiagramMLTextFormat_MoveTo class attributes and methods

# DatadiagramMLTextFormat_XYAElt class attributes and methods

# DatadiagramMLTextFormat_ArcTo class attributes and methods

# XYAElt class attributes and methods

# DatadiagramMLTextFormat_XYElt class attributes and methods

# DatadiagramMLTextFormat_XYABElt class attributes and methods

# DatadiagramMLTextFormat_InfiniteLine class attributes and methods

# XYABElt class attributes and methods

# DatadiagramMLTextFormat_XYABCDElt class attributes and methods

# DatadiagramMLTextFormat_SplineKnot class attributes and methods

# DatadiagramMLTextFormat_PolylineTo class attributes and methods

# DatadiagramMLTextFormat_SplineStart class attributes and methods

# DatadiagramMLTextFormat_XYABCDEElt class attributes and methods

# DatadiagramMLTextFormat_NURBSTo class attributes and methods

# XYABCDEElt class attributes and methods

# DatadiagramMLTextFormat_Text class attributes and methods

# TextElt class attributes and methods

# DatadiagramMLTextFormat_Ellipse class attributes and methods

# XYABCDElt class attributes and methods

# DatadiagramMLTextFormat_EllipticalArcTo class attributes and methods

# DatadiagramMLTextFormat_Cp class attributes and methods

# DatadiagramMLTextFormat_Pp class attributes and methods

# DatadiagramMLTextFormat_Tp class attributes and methods

# DatadiagramMLTextFormat_Fld class attributes and methods

# DatadiagramMLTextFormat_StringElt class attributes and methods
DatadiagramMLTextFormat_StringElt_value: Property = Property(name="value", type=StringType)
DatadiagramMLTextFormat_StringElt.attributes={DatadiagramMLTextFormat_StringElt_value}

# DatadiagramMLTextFormat_Char class attributes and methods

# DatadiagramMLTextFormat_TextElt class attributes and methods

# Text class attributes and methods

# DatadiagramMLTextFormat_IXrequiredElt class attributes and methods
DatadiagramMLTextFormat_IXrequiredElt_iX: Property = Property(name="iX", type=StringType)
DatadiagramMLTextFormat_IXrequiredElt.attributes={DatadiagramMLTextFormat_IXrequiredElt_iX}

# DatadiagramMLTextFormat_Para class attributes and methods

# DatadiagramMLTextFormat_TabsCollection class attributes and methods

# Tab class attributes and methods

# DatadiagramMLTextFormat_Tab class attributes and methods

# TabsCollection class attributes and methods

# DatadiagramMLTextFormat_Field class attributes and methods

# DatadiagramMLTextFormat_MastersCollection class attributes and methods

# Master class attributes and methods

# MasterShortCut class attributes and methods

# DatadiagramMLTextFormat_MasterShortCut class attributes and methods
DatadiagramMLTextFormat_MasterShortCut_shortcutHelp: Property = Property(name="shortcutHelp", type=StringType)
DatadiagramMLTextFormat_MasterShortCut_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLTextFormat_MasterShortCut_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLTextFormat_MasterShortCut_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLTextFormat_MasterShortCut_shortcutURL: Property = Property(name="shortcutURL", type=StringType)
DatadiagramMLTextFormat_MasterShortCut_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLTextFormat_MasterShortCut.attributes={DatadiagramMLTextFormat_MasterShortCut_patternFlags, DatadiagramMLTextFormat_MasterShortCut_iconSize, DatadiagramMLTextFormat_MasterShortCut_alignName, DatadiagramMLTextFormat_MasterShortCut_shortcutHelp, DatadiagramMLTextFormat_MasterShortCut_shortcutURL, DatadiagramMLTextFormat_MasterShortCut_prompt}

# Icon class attributes and methods

# DatadiagramMLTextFormat_Icon class attributes and methods
DatadiagramMLTextFormat_Icon_value: Property = Property(name="value", type=StringType)
DatadiagramMLTextFormat_Icon.attributes={DatadiagramMLTextFormat_Icon_value}

# DatadiagramMLTextFormat_Master class attributes and methods
DatadiagramMLTextFormat_Master_baseID: Property = Property(name="baseID", type=StringType)
DatadiagramMLTextFormat_Master_matchByName: Property = Property(name="matchByName", type=StringType)
DatadiagramMLTextFormat_Master_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLTextFormat_Master_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLTextFormat_Master_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLTextFormat_Master_hidden: Property = Property(name="hidden", type=StringType)
DatadiagramMLTextFormat_Master_iconUpdate: Property = Property(name="iconUpdate", type=StringType)
DatadiagramMLTextFormat_Master_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLTextFormat_Master.attributes={DatadiagramMLTextFormat_Master_prompt, DatadiagramMLTextFormat_Master_baseID, DatadiagramMLTextFormat_Master_alignName, DatadiagramMLTextFormat_Master_iconSize, DatadiagramMLTextFormat_Master_iconUpdate, DatadiagramMLTextFormat_Master_patternFlags, DatadiagramMLTextFormat_Master_matchByName, DatadiagramMLTextFormat_Master_hidden}

# DatadiagramMLTextFormat_ShapesCollection class attributes and methods

# Page class attributes and methods

# DatadiagramMLTextFormat_ConnectsCollection class attributes and methods

# Connect class attributes and methods

# DatadiagramMLTextFormat_Connect class attributes and methods
DatadiagramMLTextFormat_Connect_fromSheet: Property = Property(name="fromSheet", type=StringType)
DatadiagramMLTextFormat_Connect_toSheet: Property = Property(name="toSheet", type=StringType)
DatadiagramMLTextFormat_Connect_fromCell: Property = Property(name="fromCell", type=StringType)
DatadiagramMLTextFormat_Connect_toCell: Property = Property(name="toCell", type=StringType)
DatadiagramMLTextFormat_Connect_fromPart: Property = Property(name="fromPart", type=StringType)
DatadiagramMLTextFormat_Connect_toPart: Property = Property(name="toPart", type=StringType)
DatadiagramMLTextFormat_Connect.attributes={DatadiagramMLTextFormat_Connect_fromSheet, DatadiagramMLTextFormat_Connect_toCell, DatadiagramMLTextFormat_Connect_fromCell, DatadiagramMLTextFormat_Connect_toSheet, DatadiagramMLTextFormat_Connect_fromPart, DatadiagramMLTextFormat_Connect_toPart}

# ConnectsCollection class attributes and methods

# DatadiagramMLTextFormat_MasterElt class attributes and methods

# DatadiagramMLTextFormat_PagesCollection class attributes and methods

# DatadiagramMLTextFormat_PrintSetup class attributes and methods

# DatadiagramMLTextFormat_Page class attributes and methods
DatadiagramMLTextFormat_Page_background: Property = Property(name="background", type=StringType)
DatadiagramMLTextFormat_Page_backPage: Property = Property(name="backPage", type=StringType)
DatadiagramMLTextFormat_Page_viewScale: Property = Property(name="viewScale", type=StringType)
DatadiagramMLTextFormat_Page_viewCenterX: Property = Property(name="viewCenterX", type=StringType)
DatadiagramMLTextFormat_Page_ViewCenterY: Property = Property(name="ViewCenterY", type=StringType)
DatadiagramMLTextFormat_Page_reviewerID: Property = Property(name="reviewerID", type=StringType)
DatadiagramMLTextFormat_Page_associatedPage: Property = Property(name="associatedPage", type=StringType)
DatadiagramMLTextFormat_Page.attributes={DatadiagramMLTextFormat_Page_viewCenterX, DatadiagramMLTextFormat_Page_backPage, DatadiagramMLTextFormat_Page_viewScale, DatadiagramMLTextFormat_Page_ViewCenterY, DatadiagramMLTextFormat_Page_associatedPage, DatadiagramMLTextFormat_Page_reviewerID, DatadiagramMLTextFormat_Page_background}

# DatadiagramMLTextFormat_PageElt class attributes and methods

# DatadiagramMLTextFormat_DocumentSettingsElt class attributes and methods

# DatadiagramMLTextFormat_WindowsInfo class attributes and methods

# DatadiagramMLTextFormat_EventList class attributes and methods

# DatadiagramMLTextFormat_HeaderFooter class attributes and methods

# DatadiagramMLTextFormat_SolutionXML class attributes and methods

# Relationships
docProps0: BinaryAssociation = BinaryAssociation(
    name="docProps0",
    ends={
        Property(name="DocumentPropertiesCollection", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dps_visioDocument", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docSettings1: BinaryAssociation = BinaryAssociation(
    name="docSettings1",
    ends={
        Property(name="DocumentSettingsElt", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dss_visioDocument", type=DocumentSettingsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docStyleSheets6: BinaryAssociation = BinaryAssociation(
    name="docStyleSheets6",
    ends={
        Property(name="sss_visioDocument", type=StyleSheetsCollection, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="StyleSheetsCollection", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
docDocumentSheet7: BinaryAssociation = BinaryAssociation(
    name="docDocumentSheet7",
    ends={
        Property(name="DocumentSheet", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ds_visioDocument", type=DocumentSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docMasters8: BinaryAssociation = BinaryAssociation(
    name="docMasters8",
    ends={
        Property(name="MastersCollection", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ms_visioDocument", type=MastersCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPages9: BinaryAssociation = BinaryAssociation(
    name="docPages9",
    ends={
        Property(name="PagesCollection", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument10", type=PagesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docWindows11: BinaryAssociation = BinaryAssociation(
    name="docWindows11",
    ends={
        Property(name="WindowsInfo", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_visioDocument", type=WindowsInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docEventList12: BinaryAssociation = BinaryAssociation(
    name="docEventList12",
    ends={
        Property(name="EventList", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="el_visioDocument", type=EventList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docHeaderFooter13: BinaryAssociation = BinaryAssociation(
    name="docHeaderFooter13",
    ends={
        Property(name="HeaderFooter", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ef_visioDocument", type=HeaderFooter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docVBProjectData14: BinaryAssociation = BinaryAssociation(
    name="docVBProjectData14",
    ends={
        Property(name="VBProjectData", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="vpd_visioDocument", type=VBProjectData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docEmailRoutingData15: BinaryAssociation = BinaryAssociation(
    name="docEmailRoutingData15",
    ends={
        Property(name="EmailRoutingData", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="erd_visioDocument", type=EmailRoutingData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docSolutionXML16: BinaryAssociation = BinaryAssociation(
    name="docSolutionXML16",
    ends={
        Property(name="SolutionXML", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sx_visioDocument", type=SolutionXML, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dps_visioDocument17: BinaryAssociation = BinaryAssociation(
    name="dps_visioDocument17",
    ends={
        Property(name="VisioDocument", type=DatadiagramMLTextFormat_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docProps", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
docColors2: BinaryAssociation = BinaryAssociation(
    name="docColors2",
    ends={
        Property(name="ColorsTable", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_visioDocument", type=ColorsTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPrintSetup3: BinaryAssociation = BinaryAssociation(
    name="docPrintSetup3",
    ends={
        Property(name="PrintSetup", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument", type=PrintSetup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docFonts4: BinaryAssociation = BinaryAssociation(
    name="docFonts4",
    ends={
        Property(name="FontsTable", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fs_visioDocument", type=FontsTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docFaceNames5: BinaryAssociation = BinaryAssociation(
    name="docFaceNames5",
    ends={
        Property(name="FaceNamesTable", type=DatadiagramMLTextFormat_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fns_visioDocument", type=FaceNamesTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customProps18: BinaryAssociation = BinaryAssociation(
    name="customProps18",
    ends={
        Property(name="CustomPropertiesCollection", type=DatadiagramMLTextFormat_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cps_docProp", type=CustomPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCreated19: BinaryAssociation = BinaryAssociation(
    name="timeCreated19",
    ends={
        Property(name="DateTimeType", type=DatadiagramMLTextFormat_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_DocumentPropertiesCollection", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cps_customProps31: BinaryAssociation = BinaryAssociation(
    name="cps_customProps31",
    ends={
        Property(name="CustomProperty", type=DatadiagramMLTextFormat_CustomPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cp_customProps", type=CustomProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cp_customProps32: BinaryAssociation = BinaryAssociation(
    name="cp_customProps32",
    ends={
        Property(name="CustomPropertiesCollection33", type=DatadiagramMLTextFormat_CustomProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="cps_customProps", type=CustomPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
cs_visioDocument34: BinaryAssociation = BinaryAssociation(
    name="cs_visioDocument34",
    ends={
        Property(name="VisioDocument35", type=DatadiagramMLTextFormat_ColorsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docColors", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
colorEntries36: BinaryAssociation = BinaryAssociation(
    name="colorEntries36",
    ends={
        Property(name="ColorEntry", type=DatadiagramMLTextFormat_ColorsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ce_colors", type=ColorEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce_colors37: BinaryAssociation = BinaryAssociation(
    name="ce_colors37",
    ends={
        Property(name="ColorsTable38", type=DatadiagramMLTextFormat_ColorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="colorEntries", type=ColorsTable, multiplicity=Multiplicity(1, 1))
    }
)
timeSaved20: BinaryAssociation = BinaryAssociation(
    name="timeSaved20",
    ends={
        Property(name="DateTimeType22", type=DatadiagramMLTextFormat_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_DocumentPropertiesCollection21", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeEdited23: BinaryAssociation = BinaryAssociation(
    name="timeEdited23",
    ends={
        Property(name="DateTimeType25", type=DatadiagramMLTextFormat_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_DocumentPropertiesCollection24", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timePrinted26: BinaryAssociation = BinaryAssociation(
    name="timePrinted26",
    ends={
        Property(name="DateTimeType28", type=DatadiagramMLTextFormat_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_DocumentPropertiesCollection27", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cps_docProp29: BinaryAssociation = BinaryAssociation(
    name="cps_docProp29",
    ends={
        Property(name="DocumentPropertiesCollection30", type=DatadiagramMLTextFormat_CustomPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customProps", type=DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
fe_fonts42: BinaryAssociation = BinaryAssociation(
    name="fe_fonts42",
    ends={
        Property(name="FontsTable43", type=DatadiagramMLTextFormat_FontEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="fontEntries", type=FontsTable, multiplicity=Multiplicity(1, 1))
    }
)
fns_visioDocument44: BinaryAssociation = BinaryAssociation(
    name="fns_visioDocument44",
    ends={
        Property(name="VisioDocument45", type=DatadiagramMLTextFormat_FaceNamesTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docFaceNames", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
faceNameEntries46: BinaryAssociation = BinaryAssociation(
    name="faceNameEntries46",
    ends={
        Property(name="FaceName", type=DatadiagramMLTextFormat_FaceNamesTable, multiplicity=Multiplicity(1, 1)),
        Property(name="fn_faceNames", type=FaceName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fn_faceNames47: BinaryAssociation = BinaryAssociation(
    name="fn_faceNames47",
    ends={
        Property(name="FaceNamesTable48", type=DatadiagramMLTextFormat_FaceName, multiplicity=Multiplicity(1, 1)),
        Property(name="faceNameEntries", type=FaceNamesTable, multiplicity=Multiplicity(1, 1))
    }
)
fs_visioDocument39: BinaryAssociation = BinaryAssociation(
    name="fs_visioDocument39",
    ends={
        Property(name="VisioDocument40", type=DatadiagramMLTextFormat_FontsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docFonts", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
fontEntries41: BinaryAssociation = BinaryAssociation(
    name="fontEntries41",
    ends={
        Property(name="FontEntry", type=DatadiagramMLTextFormat_FontsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="fe_fonts", type=FontEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vpd_visioDocument49: BinaryAssociation = BinaryAssociation(
    name="vpd_visioDocument49",
    ends={
        Property(name="VisioDocument50", type=DatadiagramMLTextFormat_VBProjectData, multiplicity=Multiplicity(1, 1)),
        Property(name="docVBProjectData", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
erd_visioDocument51: BinaryAssociation = BinaryAssociation(
    name="erd_visioDocument51",
    ends={
        Property(name="VisioDocument52", type=DatadiagramMLTextFormat_EmailRoutingData, multiplicity=Multiplicity(1, 1)),
        Property(name="docEmailRoutingData", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
sss_visioDocument53: BinaryAssociation = BinaryAssociation(
    name="sss_visioDocument53",
    ends={
        Property(name="VisioDocument54", type=DatadiagramMLTextFormat_StyleSheetsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docStyleSheets", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
stylesSheets55: BinaryAssociation = BinaryAssociation(
    name="stylesSheets55",
    ends={
        Property(name="StyleSheet", type=DatadiagramMLTextFormat_StyleSheetsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_stylesSheets", type=StyleSheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ss_stylesSheets56: BinaryAssociation = BinaryAssociation(
    name="ss_stylesSheets56",
    ends={
        Property(name="StyleSheetsCollection57", type=DatadiagramMLTextFormat_StyleSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesSheets", type=StyleSheetsCollection, multiplicity=Multiplicity(1, 1))
    }
)
ss_shapes60: BinaryAssociation = BinaryAssociation(
    name="ss_shapes60",
    ends={
        Property(name="ShapesCollection", type=DatadiagramMLTextFormat_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="shapes", type=ShapesCollection, multiplicity=Multiplicity(1, 1))
    }
)
shapeElts61: BinaryAssociation = BinaryAssociation(
    name="shapeElts61",
    ends={
        Property(name="ShapeElt", type=DatadiagramMLTextFormat_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="sse_shapeSheet", type=ShapeElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds_visioDocument58: BinaryAssociation = BinaryAssociation(
    name="ds_visioDocument58",
    ends={
        Property(name="VisioDocument59", type=DatadiagramMLTextFormat_DocumentSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="docDocumentSheet", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
noFill63: BinaryAssociation = BinaryAssociation(
    name="noFill63",
    ends={
        Property(name="CellType", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Geom", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noLine64: BinaryAssociation = BinaryAssociation(
    name="noLine64",
    ends={
        Property(name="CellType66", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Geom65", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noShow67: BinaryAssociation = BinaryAssociation(
    name="noShow67",
    ends={
        Property(name="CellType69", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Geom68", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noSnap70: BinaryAssociation = BinaryAssociation(
    name="noSnap70",
    ends={
        Property(name="CellType72", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Geom71", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linesTo73: BinaryAssociation = BinaryAssociation(
    name="linesTo73",
    ends={
        Property(name="LineTo", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="lt_geom", type=LineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sse_shapeSheet62: BinaryAssociation = BinaryAssociation(
    name="sse_shapeSheet62",
    ends={
        Property(name="Shape", type=DatadiagramMLTextFormat_ShapeElt, multiplicity=Multiplicity(1, 1)),
        Property(name="shapeElts", type=Shape, multiplicity=Multiplicity(1, 1))
    }
)
polylinesTo77: BinaryAssociation = BinaryAssociation(
    name="polylinesTo77",
    ends={
        Property(name="PolylineTo", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="pt_geom", type=PolylineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infiniteLines78: BinaryAssociation = BinaryAssociation(
    name="infiniteLines78",
    ends={
        Property(name="InfiniteLine", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="il_geom", type=InfiniteLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipses79: BinaryAssociation = BinaryAssociation(
    name="ellipses79",
    ends={
        Property(name="Ellipse", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="e_geom", type=Ellipse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipticalArcsTo80: BinaryAssociation = BinaryAssociation(
    name="ellipticalArcsTo80",
    ends={
        Property(name="EllipticalArcTo", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="eat_geom", type=EllipticalArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineStarts81: BinaryAssociation = BinaryAssociation(
    name="splineStarts81",
    ends={
        Property(name="SplineStart", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_geom", type=SplineStart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movesTo74: BinaryAssociation = BinaryAssociation(
    name="movesTo74",
    ends={
        Property(name="MoveTo", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_geom", type=MoveTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcsTo75: BinaryAssociation = BinaryAssociation(
    name="arcsTo75",
    ends={
        Property(name="ArcTo", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ac_geom", type=ArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineKnots76: BinaryAssociation = BinaryAssociation(
    name="splineKnots76",
    ends={
        Property(name="SplineKnot", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="sk_geom", type=SplineKnot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y85: BinaryAssociation = BinaryAssociation(
    name="y85",
    ends={
        Property(name="CellType87", type=DatadiagramMLTextFormat_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYElt86", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lt_geom88: BinaryAssociation = BinaryAssociation(
    name="lt_geom88",
    ends={
        Property(name="Geom", type=DatadiagramMLTextFormat_LineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="linesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
mt_geom89: BinaryAssociation = BinaryAssociation(
    name="mt_geom89",
    ends={
        Property(name="Geom90", type=DatadiagramMLTextFormat_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="movesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
a91: BinaryAssociation = BinaryAssociation(
    name="a91",
    ends={
        Property(name="CellType92", type=DatadiagramMLTextFormat_XYAElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYAElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nurbsTo82: BinaryAssociation = BinaryAssociation(
    name="nurbsTo82",
    ends={
        Property(name="NURBSTo", type=DatadiagramMLTextFormat_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="nt_geom", type=NURBSTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
x83: BinaryAssociation = BinaryAssociation(
    name="x83",
    ends={
        Property(name="CellType84", type=DatadiagramMLTextFormat_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pt_geom97: BinaryAssociation = BinaryAssociation(
    name="pt_geom97",
    ends={
        Property(name="Geom98", type=DatadiagramMLTextFormat_PolylineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="polylinesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
b99: BinaryAssociation = BinaryAssociation(
    name="b99",
    ends={
        Property(name="CellType100", type=DatadiagramMLTextFormat_XYABElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYABElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_geom101: BinaryAssociation = BinaryAssociation(
    name="il_geom101",
    ends={
        Property(name="Geom102", type=DatadiagramMLTextFormat_InfiniteLine, multiplicity=Multiplicity(1, 1)),
        Property(name="infiniteLines", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
c103: BinaryAssociation = BinaryAssociation(
    name="c103",
    ends={
        Property(name="CellType104", type=DatadiagramMLTextFormat_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYABCDElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d105: BinaryAssociation = BinaryAssociation(
    name="d105",
    ends={
        Property(name="CellType107", type=DatadiagramMLTextFormat_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYABCDElt106", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ac_geom93: BinaryAssociation = BinaryAssociation(
    name="ac_geom93",
    ends={
        Property(name="Geom94", type=DatadiagramMLTextFormat_ArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="arcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
sk_geom95: BinaryAssociation = BinaryAssociation(
    name="sk_geom95",
    ends={
        Property(name="Geom96", type=DatadiagramMLTextFormat_SplineKnot, multiplicity=Multiplicity(1, 1)),
        Property(name="splineKnots", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
eat_geom110: BinaryAssociation = BinaryAssociation(
    name="eat_geom110",
    ends={
        Property(name="Geom111", type=DatadiagramMLTextFormat_EllipticalArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipticalArcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
ss_geom112: BinaryAssociation = BinaryAssociation(
    name="ss_geom112",
    ends={
        Property(name="Geom113", type=DatadiagramMLTextFormat_SplineStart, multiplicity=Multiplicity(1, 1)),
        Property(name="splineStarts", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
e114: BinaryAssociation = BinaryAssociation(
    name="e114",
    ends={
        Property(name="CellType115", type=DatadiagramMLTextFormat_XYABCDEElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_XYABCDEElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nt_geom116: BinaryAssociation = BinaryAssociation(
    name="nt_geom116",
    ends={
        Property(name="Geom117", type=DatadiagramMLTextFormat_NURBSTo, multiplicity=Multiplicity(1, 1)),
        Property(name="nurbsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
e_geom108: BinaryAssociation = BinaryAssociation(
    name="e_geom108",
    ends={
        Property(name="Geom109", type=DatadiagramMLTextFormat_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipses", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
font120: BinaryAssociation = BinaryAssociation(
    name="font120",
    ends={
        Property(name="CellType121", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textElts118: BinaryAssociation = BinaryAssociation(
    name="textElts118",
    ends={
        Property(name="TextElt", type=DatadiagramMLTextFormat_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="te_text", type=TextElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
te_text119: BinaryAssociation = BinaryAssociation(
    name="te_text119",
    ends={
        Property(name="Text", type=DatadiagramMLTextFormat_TextElt, multiplicity=Multiplicity(1, 1)),
        Property(name="textElts", type=Text, multiplicity=Multiplicity(1, 1))
    }
)
case128: BinaryAssociation = BinaryAssociation(
    name="case128",
    ends={
        Property(name="DatadiagramMLTextFormat_Char129", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="CellType130", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1))
    }
)
pos131: BinaryAssociation = BinaryAssociation(
    name="pos131",
    ends={
        Property(name="CellType133", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char132", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fontScale134: BinaryAssociation = BinaryAssociation(
    name="fontScale134",
    ends={
        Property(name="CellType136", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char135", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size137: BinaryAssociation = BinaryAssociation(
    name="size137",
    ends={
        Property(name="CellType139", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char138", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dblUnderline140: BinaryAssociation = BinaryAssociation(
    name="dblUnderline140",
    ends={
        Property(name="CellType142", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char141", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overline143: BinaryAssociation = BinaryAssociation(
    name="overline143",
    ends={
        Property(name="CellType145", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char144", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color122: BinaryAssociation = BinaryAssociation(
    name="color122",
    ends={
        Property(name="CellType124", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char123", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style125: BinaryAssociation = BinaryAssociation(
    name="style125",
    ends={
        Property(name="CellType127", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char126", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rtlText152: BinaryAssociation = BinaryAssociation(
    name="rtlText152",
    ends={
        Property(name="CellType154", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char153", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
runVertical155: BinaryAssociation = BinaryAssociation(
    name="runVertical155",
    ends={
        Property(name="CellType157", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char156", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letterspace158: BinaryAssociation = BinaryAssociation(
    name="letterspace158",
    ends={
        Property(name="CellType160", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char159", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorTrans161: BinaryAssociation = BinaryAssociation(
    name="colorTrans161",
    ends={
        Property(name="CellType163", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char162", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localizeFont164: BinaryAssociation = BinaryAssociation(
    name="localizeFont164",
    ends={
        Property(name="CellType166", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char165", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
langID167: BinaryAssociation = BinaryAssociation(
    name="langID167",
    ends={
        Property(name="CellType169", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char168", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
strikethru146: BinaryAssociation = BinaryAssociation(
    name="strikethru146",
    ends={
        Property(name="CellType148", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char147", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doubleStrikethrough149: BinaryAssociation = BinaryAssociation(
    name="doubleStrikethrough149",
    ends={
        Property(name="CellType151", type=DatadiagramMLTextFormat_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Char150", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indLeft172: BinaryAssociation = BinaryAssociation(
    name="indLeft172",
    ends={
        Property(name="CellType174", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para173", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indRight175: BinaryAssociation = BinaryAssociation(
    name="indRight175",
    ends={
        Property(name="CellType177", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para176", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spLine178: BinaryAssociation = BinaryAssociation(
    name="spLine178",
    ends={
        Property(name="CellType180", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para179", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spBefore181: BinaryAssociation = BinaryAssociation(
    name="spBefore181",
    ends={
        Property(name="CellType183", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para182", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spAfter184: BinaryAssociation = BinaryAssociation(
    name="spAfter184",
    ends={
        Property(name="CellType186", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para185", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
horzAlign187: BinaryAssociation = BinaryAssociation(
    name="horzAlign187",
    ends={
        Property(name="CellType189", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para188", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indFirst170: BinaryAssociation = BinaryAssociation(
    name="indFirst170",
    ends={
        Property(name="CellType171", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bulletFont196: BinaryAssociation = BinaryAssociation(
    name="bulletFont196",
    ends={
        Property(name="CellType198", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para197", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localizeBulletFont199: BinaryAssociation = BinaryAssociation(
    name="localizeBulletFont199",
    ends={
        Property(name="CellType201", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para200", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bulletFontSize202: BinaryAssociation = BinaryAssociation(
    name="bulletFontSize202",
    ends={
        Property(name="CellType204", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para203", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textPosAfterBullet205: BinaryAssociation = BinaryAssociation(
    name="textPosAfterBullet205",
    ends={
        Property(name="CellType207", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para206", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flags208: BinaryAssociation = BinaryAssociation(
    name="flags208",
    ends={
        Property(name="CellType210", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para209", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bullet190: BinaryAssociation = BinaryAssociation(
    name="bullet190",
    ends={
        Property(name="CellType192", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para191", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bulletStr193: BinaryAssociation = BinaryAssociation(
    name="bulletStr193",
    ends={
        Property(name="CellType195", type=DatadiagramMLTextFormat_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Para194", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabs211: BinaryAssociation = BinaryAssociation(
    name="tabs211",
    ends={
        Property(name="Tab", type=DatadiagramMLTextFormat_TabsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="t_tabs", type=Tab, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_tabs212: BinaryAssociation = BinaryAssociation(
    name="t_tabs212",
    ends={
        Property(name="TabsCollection", type=DatadiagramMLTextFormat_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="tabs", type=TabsCollection, multiplicity=Multiplicity(1, 1))
    }
)
position213: BinaryAssociation = BinaryAssociation(
    name="position213",
    ends={
        Property(name="CellType214", type=DatadiagramMLTextFormat_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Tab", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alignment215: BinaryAssociation = BinaryAssociation(
    name="alignment215",
    ends={
        Property(name="CellType217", type=DatadiagramMLTextFormat_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Tab216", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiFmt235: BinaryAssociation = BinaryAssociation(
    name="uiFmt235",
    ends={
        Property(name="CellType237", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field236", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value218: BinaryAssociation = BinaryAssociation(
    name="value218",
    ends={
        Property(name="CellType219", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editMode220: BinaryAssociation = BinaryAssociation(
    name="editMode220",
    ends={
        Property(name="CellType222", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field221", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
format223: BinaryAssociation = BinaryAssociation(
    name="format223",
    ends={
        Property(name="CellType225", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field224", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type226: BinaryAssociation = BinaryAssociation(
    name="type226",
    ends={
        Property(name="CellType228", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field227", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiCat229: BinaryAssociation = BinaryAssociation(
    name="uiCat229",
    ends={
        Property(name="CellType231", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field230", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiCode232: BinaryAssociation = BinaryAssociation(
    name="uiCode232",
    ends={
        Property(name="CellType234", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field233", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calendar238: BinaryAssociation = BinaryAssociation(
    name="calendar238",
    ends={
        Property(name="CellType240", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field239", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectKind241: BinaryAssociation = BinaryAssociation(
    name="objectKind241",
    ends={
        Property(name="CellType243", type=DatadiagramMLTextFormat_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLTextFormat_Field242", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ms_visioDocument244: BinaryAssociation = BinaryAssociation(
    name="ms_visioDocument244",
    ends={
        Property(name="VisioDocument245", type=DatadiagramMLTextFormat_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docMasters", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
masters246: BinaryAssociation = BinaryAssociation(
    name="masters246",
    ends={
        Property(name="Master", type=DatadiagramMLTextFormat_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masters", type=Master, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
masterShortCuts247: BinaryAssociation = BinaryAssociation(
    name="masterShortCuts247",
    ends={
        Property(name="MasterShortCut", type=DatadiagramMLTextFormat_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masterShortCuts", type=MasterShortCut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
m_masterShortCuts248: BinaryAssociation = BinaryAssociation(
    name="m_masterShortCuts248",
    ends={
        Property(name="MastersCollection249", type=DatadiagramMLTextFormat_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="masterShortCuts", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
icons250: BinaryAssociation = BinaryAssociation(
    name="icons250",
    ends={
        Property(name="Icon", type=DatadiagramMLTextFormat_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="i_masterShortCut", type=Icon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i_masterShortCut251: BinaryAssociation = BinaryAssociation(
    name="i_masterShortCut251",
    ends={
        Property(name="MasterShortCut252", type=DatadiagramMLTextFormat_Icon, multiplicity=Multiplicity(1, 1)),
        Property(name="icons", type=MasterShortCut, multiplicity=Multiplicity(1, 1))
    }
)
m_masters253: BinaryAssociation = BinaryAssociation(
    name="m_masters253",
    ends={
        Property(name="MastersCollection254", type=DatadiagramMLTextFormat_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="masters", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
masterElts255: BinaryAssociation = BinaryAssociation(
    name="masterElts255",
    ends={
        Property(name="MasterElt", type=DatadiagramMLTextFormat_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="me_master", type=MasterElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shapes256: BinaryAssociation = BinaryAssociation(
    name="shapes256",
    ends={
        Property(name="Shape257", type=DatadiagramMLTextFormat_ShapesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_shapes", type=Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections258: BinaryAssociation = BinaryAssociation(
    name="connections258",
    ends={
        Property(name="Connect", type=DatadiagramMLTextFormat_ConnectsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_connects", type=Connect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_connects259: BinaryAssociation = BinaryAssociation(
    name="c_connects259",
    ends={
        Property(name="ConnectsCollection", type=DatadiagramMLTextFormat_Connect, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=ConnectsCollection, multiplicity=Multiplicity(1, 1))
    }
)
me_master260: BinaryAssociation = BinaryAssociation(
    name="me_master260",
    ends={
        Property(name="Master261", type=DatadiagramMLTextFormat_MasterElt, multiplicity=Multiplicity(1, 1)),
        Property(name="masterElts", type=Master, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument262: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument262",
    ends={
        Property(name="VisioDocument263", type=DatadiagramMLTextFormat_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docPages", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
pages264: BinaryAssociation = BinaryAssociation(
    name="pages264",
    ends={
        Property(name="Page", type=DatadiagramMLTextFormat_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="p_pages", type=Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p_pages265: BinaryAssociation = BinaryAssociation(
    name="p_pages265",
    ends={
        Property(name="PagesCollection266", type=DatadiagramMLTextFormat_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=PagesCollection, multiplicity=Multiplicity(1, 1))
    }
)
pageElts267: BinaryAssociation = BinaryAssociation(
    name="pageElts267",
    ends={
        Property(name="PageElt", type=DatadiagramMLTextFormat_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pe_page", type=PageElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pe_page268: BinaryAssociation = BinaryAssociation(
    name="pe_page268",
    ends={
        Property(name="Page269", type=DatadiagramMLTextFormat_PageElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pageElts", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
dss_visioDocument270: BinaryAssociation = BinaryAssociation(
    name="dss_visioDocument270",
    ends={
        Property(name="VisioDocument271", type=DatadiagramMLTextFormat_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="docSettings", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument272: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument272",
    ends={
        Property(name="VisioDocument273", type=DatadiagramMLTextFormat_PrintSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="docPrintSetup", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ws_visioDocument274: BinaryAssociation = BinaryAssociation(
    name="ws_visioDocument274",
    ends={
        Property(name="VisioDocument275", type=DatadiagramMLTextFormat_WindowsInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="docWindows", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
el_visioDocument276: BinaryAssociation = BinaryAssociation(
    name="el_visioDocument276",
    ends={
        Property(name="VisioDocument277", type=DatadiagramMLTextFormat_EventList, multiplicity=Multiplicity(1, 1)),
        Property(name="docEventList", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ef_visioDocument278: BinaryAssociation = BinaryAssociation(
    name="ef_visioDocument278",
    ends={
        Property(name="VisioDocument279", type=DatadiagramMLTextFormat_HeaderFooter, multiplicity=Multiplicity(1, 1)),
        Property(name="docHeaderFooter", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
sx_visioDocument280: BinaryAssociation = BinaryAssociation(
    name="sx_visioDocument280",
    ends={
        Property(name="VisioDocument281", type=DatadiagramMLTextFormat_SolutionXML, multiplicity=Multiplicity(1, 1)),
        Property(name="docSolutionXML", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_DatadiagramMLTextFormat_ColorEntry_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLTextFormat_ColorEntry)
gen_DatadiagramMLTextFormat_FontEntry_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLTextFormat_FontEntry)
gen_DatadiagramMLTextFormat_FaceName_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLTextFormat_FaceName)
gen_DatadiagramMLTextFormat_StyleSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLTextFormat_StyleSheet)
gen_DatadiagramMLTextFormat_StyleSheet_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLTextFormat_StyleSheet)
gen_DatadiagramMLTextFormat_StyleSheet_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLTextFormat_StyleSheet)
gen_DatadiagramMLTextFormat_DocumentSheet_PageSheet = Generalization(general=PageSheet, specific=DatadiagramMLTextFormat_DocumentSheet)
gen_DatadiagramMLTextFormat_DocumentSheet_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLTextFormat_DocumentSheet)
gen_DatadiagramMLTextFormat_PageSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLTextFormat_PageSheet)
gen_DatadiagramMLTextFormat_PageSheet_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLTextFormat_PageSheet)
gen_DatadiagramMLTextFormat_PageSheet_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLTextFormat_PageSheet)
gen_DatadiagramMLTextFormat_PageSheet_PageElt = Generalization(general=PageElt, specific=DatadiagramMLTextFormat_PageSheet)
gen_DatadiagramMLTextFormat_Geom_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLTextFormat_Geom)
gen_DatadiagramMLTextFormat_Geom_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_Geom)
gen_DatadiagramMLTextFormat_Geom_DelElt = Generalization(general=DelElt, specific=DatadiagramMLTextFormat_Geom)
gen_DatadiagramMLTextFormat_LineTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLTextFormat_LineTo)
gen_DatadiagramMLTextFormat_MoveTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLTextFormat_MoveTo)
gen_DatadiagramMLTextFormat_XYAElt_XYElt = Generalization(general=XYElt, specific=DatadiagramMLTextFormat_XYAElt)
gen_DatadiagramMLTextFormat_ArcTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLTextFormat_ArcTo)
gen_DatadiagramMLTextFormat_XYElt_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_XYElt)
gen_DatadiagramMLTextFormat_XYElt_DelElt = Generalization(general=DelElt, specific=DatadiagramMLTextFormat_XYElt)
gen_DatadiagramMLTextFormat_XYABElt_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLTextFormat_XYABElt)
gen_DatadiagramMLTextFormat_InfiniteLine_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLTextFormat_InfiniteLine)
gen_DatadiagramMLTextFormat_XYABCDElt_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLTextFormat_XYABCDElt)
gen_DatadiagramMLTextFormat_SplineKnot_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLTextFormat_SplineKnot)
gen_DatadiagramMLTextFormat_PolylineTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLTextFormat_PolylineTo)
gen_DatadiagramMLTextFormat_SplineStart_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLTextFormat_SplineStart)
gen_DatadiagramMLTextFormat_XYABCDEElt_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLTextFormat_XYABCDEElt)
gen_DatadiagramMLTextFormat_NURBSTo_XYABCDEElt = Generalization(general=XYABCDEElt, specific=DatadiagramMLTextFormat_NURBSTo)
gen_DatadiagramMLTextFormat_Text_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLTextFormat_Text)
gen_DatadiagramMLTextFormat_Ellipse_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLTextFormat_Ellipse)
gen_DatadiagramMLTextFormat_EllipticalArcTo_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLTextFormat_EllipticalArcTo)
gen_DatadiagramMLTextFormat_Cp_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLTextFormat_Cp)
gen_DatadiagramMLTextFormat_Cp_TextElt = Generalization(general=TextElt, specific=DatadiagramMLTextFormat_Cp)
gen_DatadiagramMLTextFormat_Pp_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLTextFormat_Pp)
gen_DatadiagramMLTextFormat_Pp_TextElt = Generalization(general=TextElt, specific=DatadiagramMLTextFormat_Pp)
gen_DatadiagramMLTextFormat_Tp_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLTextFormat_Tp)
gen_DatadiagramMLTextFormat_Tp_TextElt = Generalization(general=TextElt, specific=DatadiagramMLTextFormat_Tp)
gen_DatadiagramMLTextFormat_Fld_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLTextFormat_Fld)
gen_DatadiagramMLTextFormat_Fld_TextElt = Generalization(general=TextElt, specific=DatadiagramMLTextFormat_Fld)
gen_DatadiagramMLTextFormat_StringElt_TextElt = Generalization(general=TextElt, specific=DatadiagramMLTextFormat_StringElt)
gen_DatadiagramMLTextFormat_Char_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLTextFormat_Char)
gen_DatadiagramMLTextFormat_Char_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_Char)
gen_DatadiagramMLTextFormat_Char_DelElt = Generalization(general=DelElt, specific=DatadiagramMLTextFormat_Char)
gen_DatadiagramMLTextFormat_Para_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLTextFormat_Para)
gen_DatadiagramMLTextFormat_Para_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_Para)
gen_DatadiagramMLTextFormat_Para_DelElt = Generalization(general=DelElt, specific=DatadiagramMLTextFormat_Para)
gen_DatadiagramMLTextFormat_TabsCollection_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLTextFormat_TabsCollection)
gen_DatadiagramMLTextFormat_TabsCollection_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_TabsCollection)
gen_DatadiagramMLTextFormat_TabsCollection_DelElt = Generalization(general=DelElt, specific=DatadiagramMLTextFormat_TabsCollection)
gen_DatadiagramMLTextFormat_Tab_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_Tab)
gen_DatadiagramMLTextFormat_Field_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLTextFormat_Field)
gen_DatadiagramMLTextFormat_Field_IXElt = Generalization(general=IXElt, specific=DatadiagramMLTextFormat_Field)
gen_DatadiagramMLTextFormat_Field_DelElt = Generalization(general=DelElt, specific=DatadiagramMLTextFormat_Field)
gen_DatadiagramMLTextFormat_MasterShortCut_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLTextFormat_MasterShortCut)
gen_DatadiagramMLTextFormat_MasterShortCut_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLTextFormat_MasterShortCut)
gen_DatadiagramMLTextFormat_Icon_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLTextFormat_Icon)
gen_DatadiagramMLTextFormat_Master_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLTextFormat_Master)
gen_DatadiagramMLTextFormat_Master_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLTextFormat_Master)
gen_DatadiagramMLTextFormat_Master_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLTextFormat_Master)
gen_DatadiagramMLTextFormat_ShapesCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLTextFormat_ShapesCollection)
gen_DatadiagramMLTextFormat_ShapesCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLTextFormat_ShapesCollection)
gen_DatadiagramMLTextFormat_ConnectsCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLTextFormat_ConnectsCollection)
gen_DatadiagramMLTextFormat_ConnectsCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLTextFormat_ConnectsCollection)
gen_DatadiagramMLTextFormat_Page_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLTextFormat_Page)
gen_DatadiagramMLTextFormat_Page_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLTextFormat_Page)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={DatadiagramMLTextFormat_CellType, DatadiagramMLTextFormat_VisioDocument, DocumentPropertiesCollection, DocumentSettingsElt, DatadiagramMLTextFormat_DateTimeType, DocumentSheet, MastersCollection, PagesCollection, WindowsInfo, EventList, HeaderFooter, VBProjectData, EmailRoutingData, SolutionXML, DatadiagramMLTextFormat_DocumentPropertiesCollection, VisioDocument, ColorsTable, PrintSetup, FontsTable, FaceNamesTable, StyleSheetsCollection, CustomPropertiesCollection, DateTimeType, DatadiagramMLTextFormat_CustomProperty, DatadiagramMLTextFormat_ColorsTable, ColorEntry, DatadiagramMLTextFormat_ColorEntry, IXrequiredElt, DatadiagramMLTextFormat_CustomPropertiesCollection, DatadiagramMLTextFormat_FontEntry, CustomProperty, IdentifiedElt, DatadiagramMLTextFormat_FaceNamesTable, FaceName, DatadiagramMLTextFormat_FaceName, DatadiagramMLTextFormat_FontsTable, FontEntry, DatadiagramMLTextFormat_EmailRoutingData, DatadiagramMLTextFormat_StyleSheetsCollection, StyleSheet, DatadiagramMLTextFormat_StyleSheet, Shape, NamedElt, DatadiagramMLTextFormat_DocumentSheet, PageSheet, DatadiagramMLTextFormat_VBProjectData, DatadiagramMLTextFormat_IdentifiedElt, DatadiagramMLTextFormat_UniqueIdElt, DatadiagramMLTextFormat_Shape, ShapesCollection, ShapeElt, DatadiagramMLTextFormat_ShapeElt, DatadiagramMLTextFormat_PageSheet, UniqueIdElt, MasterElt, PageElt, DatadiagramMLTextFormat_NamedElt, DatadiagramMLTextFormat_Geom, IXElt, DelElt, CellType, LineTo, MoveTo, DatadiagramMLTextFormat_IXElt, DatadiagramMLTextFormat_DelElt, PolylineTo, InfiniteLine, Ellipse, EllipticalArcTo, SplineStart, NURBSTo, ArcTo, SplineKnot, DatadiagramMLTextFormat_LineTo, XYElt, Geom, DatadiagramMLTextFormat_MoveTo, DatadiagramMLTextFormat_XYAElt, DatadiagramMLTextFormat_ArcTo, XYAElt, DatadiagramMLTextFormat_XYElt, DatadiagramMLTextFormat_XYABElt, DatadiagramMLTextFormat_InfiniteLine, XYABElt, DatadiagramMLTextFormat_XYABCDElt, DatadiagramMLTextFormat_SplineKnot, DatadiagramMLTextFormat_PolylineTo, DatadiagramMLTextFormat_SplineStart, DatadiagramMLTextFormat_XYABCDEElt, DatadiagramMLTextFormat_NURBSTo, XYABCDEElt, DatadiagramMLTextFormat_Text, TextElt, DatadiagramMLTextFormat_Ellipse, XYABCDElt, DatadiagramMLTextFormat_EllipticalArcTo, DatadiagramMLTextFormat_Cp, DatadiagramMLTextFormat_Pp, DatadiagramMLTextFormat_Tp, DatadiagramMLTextFormat_Fld, DatadiagramMLTextFormat_StringElt, DatadiagramMLTextFormat_Char, DatadiagramMLTextFormat_TextElt, Text, DatadiagramMLTextFormat_IXrequiredElt, DatadiagramMLTextFormat_Para, DatadiagramMLTextFormat_TabsCollection, Tab, DatadiagramMLTextFormat_Tab, TabsCollection, DatadiagramMLTextFormat_Field, DatadiagramMLTextFormat_MastersCollection, Master, MasterShortCut, DatadiagramMLTextFormat_MasterShortCut, Icon, DatadiagramMLTextFormat_Icon, DatadiagramMLTextFormat_Master, DatadiagramMLTextFormat_ShapesCollection, Page, DatadiagramMLTextFormat_ConnectsCollection, Connect, DatadiagramMLTextFormat_Connect, ConnectsCollection, DatadiagramMLTextFormat_MasterElt, DatadiagramMLTextFormat_PagesCollection, DatadiagramMLTextFormat_PrintSetup, DatadiagramMLTextFormat_Page, DatadiagramMLTextFormat_PageElt, DatadiagramMLTextFormat_DocumentSettingsElt, DatadiagramMLTextFormat_WindowsInfo, DatadiagramMLTextFormat_EventList, DatadiagramMLTextFormat_HeaderFooter, DatadiagramMLTextFormat_SolutionXML},
    associations={docProps0, docSettings1, docStyleSheets6, docDocumentSheet7, docMasters8, docPages9, docWindows11, docEventList12, docHeaderFooter13, docVBProjectData14, docEmailRoutingData15, docSolutionXML16, dps_visioDocument17, docColors2, docPrintSetup3, docFonts4, docFaceNames5, customProps18, timeCreated19, cps_customProps31, cp_customProps32, cs_visioDocument34, colorEntries36, ce_colors37, timeSaved20, timeEdited23, timePrinted26, cps_docProp29, fe_fonts42, fns_visioDocument44, faceNameEntries46, fn_faceNames47, fs_visioDocument39, fontEntries41, vpd_visioDocument49, erd_visioDocument51, sss_visioDocument53, stylesSheets55, ss_stylesSheets56, ss_shapes60, shapeElts61, ds_visioDocument58, noFill63, noLine64, noShow67, noSnap70, linesTo73, sse_shapeSheet62, polylinesTo77, infiniteLines78, ellipses79, ellipticalArcsTo80, splineStarts81, movesTo74, arcsTo75, splineKnots76, y85, lt_geom88, mt_geom89, a91, nurbsTo82, x83, pt_geom97, b99, il_geom101, c103, d105, ac_geom93, sk_geom95, eat_geom110, ss_geom112, e114, nt_geom116, e_geom108, font120, textElts118, te_text119, case128, pos131, fontScale134, size137, dblUnderline140, overline143, color122, style125, rtlText152, runVertical155, letterspace158, colorTrans161, localizeFont164, langID167, strikethru146, doubleStrikethrough149, indLeft172, indRight175, spLine178, spBefore181, spAfter184, horzAlign187, indFirst170, bulletFont196, localizeBulletFont199, bulletFontSize202, textPosAfterBullet205, flags208, bullet190, bulletStr193, tabs211, t_tabs212, position213, alignment215, uiFmt235, value218, editMode220, format223, type226, uiCat229, uiCode232, calendar238, objectKind241, ms_visioDocument244, masters246, masterShortCuts247, m_masterShortCuts248, icons250, i_masterShortCut251, m_masters253, masterElts255, shapes256, connections258, c_connects259, me_master260, ps_visioDocument262, pages264, p_pages265, pageElts267, pe_page268, dss_visioDocument270, ps_visioDocument272, ws_visioDocument274, el_visioDocument276, ef_visioDocument278, sx_visioDocument280},
    generalizations={gen_DatadiagramMLTextFormat_ColorEntry_IXrequiredElt, gen_DatadiagramMLTextFormat_FontEntry_IdentifiedElt, gen_DatadiagramMLTextFormat_FaceName_IdentifiedElt, gen_DatadiagramMLTextFormat_StyleSheet_Shape, gen_DatadiagramMLTextFormat_StyleSheet_IdentifiedElt, gen_DatadiagramMLTextFormat_StyleSheet_NamedElt, gen_DatadiagramMLTextFormat_DocumentSheet_PageSheet, gen_DatadiagramMLTextFormat_DocumentSheet_NamedElt, gen_DatadiagramMLTextFormat_PageSheet_Shape, gen_DatadiagramMLTextFormat_PageSheet_UniqueIdElt, gen_DatadiagramMLTextFormat_PageSheet_MasterElt, gen_DatadiagramMLTextFormat_PageSheet_PageElt, gen_DatadiagramMLTextFormat_Geom_ShapeElt, gen_DatadiagramMLTextFormat_Geom_IXElt, gen_DatadiagramMLTextFormat_Geom_DelElt, gen_DatadiagramMLTextFormat_LineTo_XYElt, gen_DatadiagramMLTextFormat_MoveTo_XYElt, gen_DatadiagramMLTextFormat_XYAElt_XYElt, gen_DatadiagramMLTextFormat_ArcTo_XYAElt, gen_DatadiagramMLTextFormat_XYElt_IXElt, gen_DatadiagramMLTextFormat_XYElt_DelElt, gen_DatadiagramMLTextFormat_XYABElt_XYAElt, gen_DatadiagramMLTextFormat_InfiniteLine_XYABElt, gen_DatadiagramMLTextFormat_XYABCDElt_XYABElt, gen_DatadiagramMLTextFormat_SplineKnot_XYAElt, gen_DatadiagramMLTextFormat_PolylineTo_XYAElt, gen_DatadiagramMLTextFormat_SplineStart_XYABCDElt, gen_DatadiagramMLTextFormat_XYABCDEElt_XYABCDElt, gen_DatadiagramMLTextFormat_NURBSTo_XYABCDEElt, gen_DatadiagramMLTextFormat_Text_ShapeElt, gen_DatadiagramMLTextFormat_Ellipse_XYABCDElt, gen_DatadiagramMLTextFormat_EllipticalArcTo_XYABCDElt, gen_DatadiagramMLTextFormat_Cp_IXrequiredElt, gen_DatadiagramMLTextFormat_Cp_TextElt, gen_DatadiagramMLTextFormat_Pp_IXrequiredElt, gen_DatadiagramMLTextFormat_Pp_TextElt, gen_DatadiagramMLTextFormat_Tp_IXrequiredElt, gen_DatadiagramMLTextFormat_Tp_TextElt, gen_DatadiagramMLTextFormat_Fld_IXrequiredElt, gen_DatadiagramMLTextFormat_Fld_TextElt, gen_DatadiagramMLTextFormat_StringElt_TextElt, gen_DatadiagramMLTextFormat_Char_ShapeElt, gen_DatadiagramMLTextFormat_Char_IXElt, gen_DatadiagramMLTextFormat_Char_DelElt, gen_DatadiagramMLTextFormat_Para_ShapeElt, gen_DatadiagramMLTextFormat_Para_IXElt, gen_DatadiagramMLTextFormat_Para_DelElt, gen_DatadiagramMLTextFormat_TabsCollection_ShapeElt, gen_DatadiagramMLTextFormat_TabsCollection_IXElt, gen_DatadiagramMLTextFormat_TabsCollection_DelElt, gen_DatadiagramMLTextFormat_Tab_IXElt, gen_DatadiagramMLTextFormat_Field_ShapeElt, gen_DatadiagramMLTextFormat_Field_IXElt, gen_DatadiagramMLTextFormat_Field_DelElt, gen_DatadiagramMLTextFormat_MasterShortCut_IdentifiedElt, gen_DatadiagramMLTextFormat_MasterShortCut_NamedElt, gen_DatadiagramMLTextFormat_Icon_MasterElt, gen_DatadiagramMLTextFormat_Master_IdentifiedElt, gen_DatadiagramMLTextFormat_Master_UniqueIdElt, gen_DatadiagramMLTextFormat_Master_NamedElt, gen_DatadiagramMLTextFormat_ShapesCollection_MasterElt, gen_DatadiagramMLTextFormat_ShapesCollection_PageElt, gen_DatadiagramMLTextFormat_ConnectsCollection_MasterElt, gen_DatadiagramMLTextFormat_ConnectsCollection_PageElt, gen_DatadiagramMLTextFormat_Page_IdentifiedElt, gen_DatadiagramMLTextFormat_Page_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)