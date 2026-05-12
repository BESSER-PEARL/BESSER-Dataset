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
DatadiagramMLBasicDef_CellType = Class(name="DatadiagramMLBasicDef_CellType")
DatadiagramMLBasicDef_VisioDocument = Class(name="DatadiagramMLBasicDef_VisioDocument")
DatadiagramMLBasicDef_DateTimeType = Class(name="DatadiagramMLBasicDef_DateTimeType")
PagesCollection = Class(name="PagesCollection")
WindowsInfo = Class(name="WindowsInfo")
EventList = Class(name="EventList")
HeaderFooter = Class(name="HeaderFooter")
VBProjectData = Class(name="VBProjectData")
EmailRoutingData = Class(name="EmailRoutingData")
SolutionXML = Class(name="SolutionXML")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
DocumentSettingsElt = Class(name="DocumentSettingsElt")
ColorsTable = Class(name="ColorsTable")
PrintSetup = Class(name="PrintSetup")
FontsTable = Class(name="FontsTable")
FaceNamesTable = Class(name="FaceNamesTable")
StyleSheetsCollection = Class(name="StyleSheetsCollection")
DocumentSheet = Class(name="DocumentSheet")
MastersCollection = Class(name="MastersCollection")
CustomPropertiesCollection = Class(name="CustomPropertiesCollection")
DateTimeType = Class(name="DateTimeType")
DatadiagramMLBasicDef_DocumentPropertiesCollection = Class(name="DatadiagramMLBasicDef_DocumentPropertiesCollection")
VisioDocument = Class(name="VisioDocument")
DatadiagramMLBasicDef_StyleSheetsCollection = Class(name="DatadiagramMLBasicDef_StyleSheetsCollection")
StyleSheet = Class(name="StyleSheet")
DatadiagramMLBasicDef_StyleSheet = Class(name="DatadiagramMLBasicDef_StyleSheet")
Shape = Class(name="Shape")
IdentifiedElt = Class(name="IdentifiedElt")
DatadiagramMLBasicDef_CustomPropertiesCollection = Class(name="DatadiagramMLBasicDef_CustomPropertiesCollection")
CustomProperty = Class(name="CustomProperty")
DatadiagramMLBasicDef_CustomProperty = Class(name="DatadiagramMLBasicDef_CustomProperty")
DatadiagramMLBasicDef_VBProjectData = Class(name="DatadiagramMLBasicDef_VBProjectData")
DatadiagramMLBasicDef_EmailRoutingData = Class(name="DatadiagramMLBasicDef_EmailRoutingData")
DatadiagramMLBasicDef_Shape = Class(name="DatadiagramMLBasicDef_Shape")
ShapesCollection = Class(name="ShapesCollection")
ShapeElt = Class(name="ShapeElt")
DatadiagramMLBasicDef_ShapeElt = Class(name="DatadiagramMLBasicDef_ShapeElt", is_abstract=True)
NamedElt = Class(name="NamedElt")
DatadiagramMLBasicDef_DocumentSheet = Class(name="DatadiagramMLBasicDef_DocumentSheet")
PageSheet = Class(name="PageSheet")
DatadiagramMLBasicDef_PageSheet = Class(name="DatadiagramMLBasicDef_PageSheet")
UniqueIdElt = Class(name="UniqueIdElt")
MasterElt = Class(name="MasterElt")
PageElt = Class(name="PageElt")
DatadiagramMLBasicDef_NamedElt = Class(name="DatadiagramMLBasicDef_NamedElt", is_abstract=True)
DatadiagramMLBasicDef_IdentifiedElt = Class(name="DatadiagramMLBasicDef_IdentifiedElt", is_abstract=True)
DatadiagramMLBasicDef_UniqueIdElt = Class(name="DatadiagramMLBasicDef_UniqueIdElt", is_abstract=True)
MoveTo = Class(name="MoveTo")
ArcTo = Class(name="ArcTo")
SplineKnot = Class(name="SplineKnot")
PolylineTo = Class(name="PolylineTo")
InfiniteLine = Class(name="InfiniteLine")
DatadiagramMLBasicDef_IXElt = Class(name="DatadiagramMLBasicDef_IXElt", is_abstract=True)
DatadiagramMLBasicDef_DelElt = Class(name="DatadiagramMLBasicDef_DelElt", is_abstract=True)
DatadiagramMLBasicDef_Geom = Class(name="DatadiagramMLBasicDef_Geom")
IXElt = Class(name="IXElt")
DelElt = Class(name="DelElt")
CellType = Class(name="CellType")
LineTo = Class(name="LineTo")
DatadiagramMLBasicDef_LineTo = Class(name="DatadiagramMLBasicDef_LineTo")
XYElt = Class(name="XYElt")
Geom = Class(name="Geom")
DatadiagramMLBasicDef_MoveTo = Class(name="DatadiagramMLBasicDef_MoveTo")
Ellipse = Class(name="Ellipse")
EllipticalArcTo = Class(name="EllipticalArcTo")
SplineStart = Class(name="SplineStart")
NURBSTo = Class(name="NURBSTo")
DatadiagramMLBasicDef_XYElt = Class(name="DatadiagramMLBasicDef_XYElt", is_abstract=True)
DatadiagramMLBasicDef_XYABElt = Class(name="DatadiagramMLBasicDef_XYABElt", is_abstract=True)
DatadiagramMLBasicDef_InfiniteLine = Class(name="DatadiagramMLBasicDef_InfiniteLine")
XYABElt = Class(name="XYABElt")
DatadiagramMLBasicDef_XYAElt = Class(name="DatadiagramMLBasicDef_XYAElt", is_abstract=True)
DatadiagramMLBasicDef_ArcTo = Class(name="DatadiagramMLBasicDef_ArcTo")
XYAElt = Class(name="XYAElt")
DatadiagramMLBasicDef_SplineKnot = Class(name="DatadiagramMLBasicDef_SplineKnot")
DatadiagramMLBasicDef_PolylineTo = Class(name="DatadiagramMLBasicDef_PolylineTo")
DatadiagramMLBasicDef_XYABCDEElt = Class(name="DatadiagramMLBasicDef_XYABCDEElt", is_abstract=True)
DatadiagramMLBasicDef_NURBSTo = Class(name="DatadiagramMLBasicDef_NURBSTo")
XYABCDEElt = Class(name="XYABCDEElt")
DatadiagramMLBasicDef_Text = Class(name="DatadiagramMLBasicDef_Text")
TextElt = Class(name="TextElt")
DatadiagramMLBasicDef_XYABCDElt = Class(name="DatadiagramMLBasicDef_XYABCDElt", is_abstract=True)
DatadiagramMLBasicDef_Ellipse = Class(name="DatadiagramMLBasicDef_Ellipse")
XYABCDElt = Class(name="XYABCDElt")
DatadiagramMLBasicDef_EllipticalArcTo = Class(name="DatadiagramMLBasicDef_EllipticalArcTo")
DatadiagramMLBasicDef_SplineStart = Class(name="DatadiagramMLBasicDef_SplineStart")
Master = Class(name="Master")
MasterShortCut = Class(name="MasterShortCut")
DatadiagramMLBasicDef_MasterShortCut = Class(name="DatadiagramMLBasicDef_MasterShortCut")
DatadiagramMLBasicDef_TextElt = Class(name="DatadiagramMLBasicDef_TextElt", is_abstract=True)
Text = Class(name="Text")
DatadiagramMLBasicDef_StringElt = Class(name="DatadiagramMLBasicDef_StringElt")
DatadiagramMLBasicDef_MastersCollection = Class(name="DatadiagramMLBasicDef_MastersCollection")
Icon = Class(name="Icon")
DatadiagramMLBasicDef_Icon = Class(name="DatadiagramMLBasicDef_Icon")
DatadiagramMLBasicDef_Master = Class(name="DatadiagramMLBasicDef_Master")
DatadiagramMLBasicDef_MasterElt = Class(name="DatadiagramMLBasicDef_MasterElt", is_abstract=True)
DatadiagramMLBasicDef_PagesCollection = Class(name="DatadiagramMLBasicDef_PagesCollection")
DatadiagramMLBasicDef_ShapesCollection = Class(name="DatadiagramMLBasicDef_ShapesCollection")
DatadiagramMLBasicDef_ConnectsCollection = Class(name="DatadiagramMLBasicDef_ConnectsCollection")
Connect = Class(name="Connect")
DatadiagramMLBasicDef_Connect = Class(name="DatadiagramMLBasicDef_Connect")
ConnectsCollection = Class(name="ConnectsCollection")
DatadiagramMLBasicDef_PageElt = Class(name="DatadiagramMLBasicDef_PageElt", is_abstract=True)
DatadiagramMLBasicDef_DocumentSettingsElt = Class(name="DatadiagramMLBasicDef_DocumentSettingsElt")
DatadiagramMLBasicDef_ColorsTable = Class(name="DatadiagramMLBasicDef_ColorsTable")
Page = Class(name="Page")
DatadiagramMLBasicDef_Page = Class(name="DatadiagramMLBasicDef_Page")
DatadiagramMLBasicDef_SolutionXML = Class(name="DatadiagramMLBasicDef_SolutionXML")
DatadiagramMLBasicDef_PrintSetup = Class(name="DatadiagramMLBasicDef_PrintSetup")
DatadiagramMLBasicDef_FontsTable = Class(name="DatadiagramMLBasicDef_FontsTable")
DatadiagramMLBasicDef_FaceNamesTable = Class(name="DatadiagramMLBasicDef_FaceNamesTable")
DatadiagramMLBasicDef_WindowsInfo = Class(name="DatadiagramMLBasicDef_WindowsInfo")
DatadiagramMLBasicDef_EventList = Class(name="DatadiagramMLBasicDef_EventList")
DatadiagramMLBasicDef_HeaderFooter = Class(name="DatadiagramMLBasicDef_HeaderFooter")

# DatadiagramMLBasicDef_CellType class attributes and methods
DatadiagramMLBasicDef_CellType_unit: Property = Property(name="unit", type=StringType)
DatadiagramMLBasicDef_CellType_formula: Property = Property(name="formula", type=StringType)
DatadiagramMLBasicDef_CellType_err: Property = Property(name="err", type=StringType)
DatadiagramMLBasicDef_CellType_value: Property = Property(name="value", type=StringType)
DatadiagramMLBasicDef_CellType.attributes={DatadiagramMLBasicDef_CellType_formula, DatadiagramMLBasicDef_CellType_err, DatadiagramMLBasicDef_CellType_unit, DatadiagramMLBasicDef_CellType_value}

# DatadiagramMLBasicDef_VisioDocument class attributes and methods
DatadiagramMLBasicDef_VisioDocument_start: Property = Property(name="start", type=StringType)
DatadiagramMLBasicDef_VisioDocument_key: Property = Property(name="key", type=StringType)
DatadiagramMLBasicDef_VisioDocument_metric: Property = Property(name="metric", type=StringType)
DatadiagramMLBasicDef_VisioDocument_buildnum: Property = Property(name="buildnum", type=StringType)
DatadiagramMLBasicDef_VisioDocument_version: Property = Property(name="version", type=StringType)
DatadiagramMLBasicDef_VisioDocument_docLangId: Property = Property(name="docLangId", type=StringType)
DatadiagramMLBasicDef_VisioDocument.attributes={DatadiagramMLBasicDef_VisioDocument_start, DatadiagramMLBasicDef_VisioDocument_docLangId, DatadiagramMLBasicDef_VisioDocument_key, DatadiagramMLBasicDef_VisioDocument_metric, DatadiagramMLBasicDef_VisioDocument_buildnum, DatadiagramMLBasicDef_VisioDocument_version}

# DatadiagramMLBasicDef_DateTimeType class attributes and methods
DatadiagramMLBasicDef_DateTimeType_month: Property = Property(name="month", type=StringType)
DatadiagramMLBasicDef_DateTimeType_day: Property = Property(name="day", type=StringType)
DatadiagramMLBasicDef_DateTimeType_hour: Property = Property(name="hour", type=StringType)
DatadiagramMLBasicDef_DateTimeType_minute: Property = Property(name="minute", type=StringType)
DatadiagramMLBasicDef_DateTimeType_second: Property = Property(name="second", type=StringType)
DatadiagramMLBasicDef_DateTimeType_year: Property = Property(name="year", type=StringType)
DatadiagramMLBasicDef_DateTimeType.attributes={DatadiagramMLBasicDef_DateTimeType_second, DatadiagramMLBasicDef_DateTimeType_year, DatadiagramMLBasicDef_DateTimeType_hour, DatadiagramMLBasicDef_DateTimeType_day, DatadiagramMLBasicDef_DateTimeType_minute, DatadiagramMLBasicDef_DateTimeType_month}

# PagesCollection class attributes and methods

# WindowsInfo class attributes and methods

# EventList class attributes and methods

# HeaderFooter class attributes and methods

# VBProjectData class attributes and methods

# EmailRoutingData class attributes and methods

# SolutionXML class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# DocumentSettingsElt class attributes and methods

# ColorsTable class attributes and methods

# PrintSetup class attributes and methods

# FontsTable class attributes and methods

# FaceNamesTable class attributes and methods

# StyleSheetsCollection class attributes and methods

# DocumentSheet class attributes and methods

# MastersCollection class attributes and methods

# CustomPropertiesCollection class attributes and methods

# DateTimeType class attributes and methods

# DatadiagramMLBasicDef_DocumentPropertiesCollection class attributes and methods
DatadiagramMLBasicDef_DocumentPropertiesCollection_buildNumberEdited: Property = Property(name="buildNumberEdited", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_creator: Property = Property(name="creator", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_hyperlinkBase_href: Property = Property(name="hyperlinkBase_href", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_alternateNames: Property = Property(name="alternateNames", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_template: Property = Property(name="template", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection_buildNumberCreated: Property = Property(name="buildNumberCreated", type=StringType)
DatadiagramMLBasicDef_DocumentPropertiesCollection.attributes={DatadiagramMLBasicDef_DocumentPropertiesCollection_alternateNames, DatadiagramMLBasicDef_DocumentPropertiesCollection_manager, DatadiagramMLBasicDef_DocumentPropertiesCollection_creator, DatadiagramMLBasicDef_DocumentPropertiesCollection_hyperlinkBase_href, DatadiagramMLBasicDef_DocumentPropertiesCollection_title, DatadiagramMLBasicDef_DocumentPropertiesCollection_subject, DatadiagramMLBasicDef_DocumentPropertiesCollection_buildNumberEdited, DatadiagramMLBasicDef_DocumentPropertiesCollection_template, DatadiagramMLBasicDef_DocumentPropertiesCollection_category, DatadiagramMLBasicDef_DocumentPropertiesCollection_keywords, DatadiagramMLBasicDef_DocumentPropertiesCollection_description, DatadiagramMLBasicDef_DocumentPropertiesCollection_company, DatadiagramMLBasicDef_DocumentPropertiesCollection_buildNumberCreated}

# VisioDocument class attributes and methods

# DatadiagramMLBasicDef_StyleSheetsCollection class attributes and methods

# StyleSheet class attributes and methods

# DatadiagramMLBasicDef_StyleSheet class attributes and methods

# Shape class attributes and methods

# IdentifiedElt class attributes and methods

# DatadiagramMLBasicDef_CustomPropertiesCollection class attributes and methods

# CustomProperty class attributes and methods

# DatadiagramMLBasicDef_CustomProperty class attributes and methods
DatadiagramMLBasicDef_CustomProperty_name: Property = Property(name="name", type=StringType)
DatadiagramMLBasicDef_CustomProperty_dataType: Property = Property(name="dataType", type=StringType)
DatadiagramMLBasicDef_CustomProperty.attributes={DatadiagramMLBasicDef_CustomProperty_name, DatadiagramMLBasicDef_CustomProperty_dataType}

# DatadiagramMLBasicDef_VBProjectData class attributes and methods
DatadiagramMLBasicDef_VBProjectData_data: Property = Property(name="data", type=StringType)
DatadiagramMLBasicDef_VBProjectData.attributes={DatadiagramMLBasicDef_VBProjectData_data}

# DatadiagramMLBasicDef_EmailRoutingData class attributes and methods
DatadiagramMLBasicDef_EmailRoutingData_data: Property = Property(name="data", type=StringType)
DatadiagramMLBasicDef_EmailRoutingData_size: Property = Property(name="size", type=StringType)
DatadiagramMLBasicDef_EmailRoutingData.attributes={DatadiagramMLBasicDef_EmailRoutingData_size, DatadiagramMLBasicDef_EmailRoutingData_data}

# DatadiagramMLBasicDef_Shape class attributes and methods
DatadiagramMLBasicDef_Shape_lineStyle: Property = Property(name="lineStyle", type=StringType)
DatadiagramMLBasicDef_Shape_fillStyle: Property = Property(name="fillStyle", type=StringType)
DatadiagramMLBasicDef_Shape_textStyle: Property = Property(name="textStyle", type=StringType)
DatadiagramMLBasicDef_Shape.attributes={DatadiagramMLBasicDef_Shape_fillStyle, DatadiagramMLBasicDef_Shape_textStyle, DatadiagramMLBasicDef_Shape_lineStyle}

# ShapesCollection class attributes and methods

# ShapeElt class attributes and methods

# DatadiagramMLBasicDef_ShapeElt class attributes and methods

# NamedElt class attributes and methods

# DatadiagramMLBasicDef_DocumentSheet class attributes and methods

# PageSheet class attributes and methods

# DatadiagramMLBasicDef_PageSheet class attributes and methods

# UniqueIdElt class attributes and methods

# MasterElt class attributes and methods

# PageElt class attributes and methods

# DatadiagramMLBasicDef_NamedElt class attributes and methods
DatadiagramMLBasicDef_NamedElt_name: Property = Property(name="name", type=StringType)
DatadiagramMLBasicDef_NamedElt_nameU: Property = Property(name="nameU", type=StringType)
DatadiagramMLBasicDef_NamedElt.attributes={DatadiagramMLBasicDef_NamedElt_nameU, DatadiagramMLBasicDef_NamedElt_name}

# DatadiagramMLBasicDef_IdentifiedElt class attributes and methods
DatadiagramMLBasicDef_IdentifiedElt_ID: Property = Property(name="ID", type=StringType)
DatadiagramMLBasicDef_IdentifiedElt.attributes={DatadiagramMLBasicDef_IdentifiedElt_ID}

# DatadiagramMLBasicDef_UniqueIdElt class attributes and methods
DatadiagramMLBasicDef_UniqueIdElt_UniqueID: Property = Property(name="UniqueID", type=StringType)
DatadiagramMLBasicDef_UniqueIdElt.attributes={DatadiagramMLBasicDef_UniqueIdElt_UniqueID}

# MoveTo class attributes and methods

# ArcTo class attributes and methods

# SplineKnot class attributes and methods

# PolylineTo class attributes and methods

# InfiniteLine class attributes and methods

# DatadiagramMLBasicDef_IXElt class attributes and methods
DatadiagramMLBasicDef_IXElt_iX: Property = Property(name="iX", type=StringType)
DatadiagramMLBasicDef_IXElt.attributes={DatadiagramMLBasicDef_IXElt_iX}

# DatadiagramMLBasicDef_DelElt class attributes and methods
DatadiagramMLBasicDef_DelElt_del_: Property = Property(name="del_", type=StringType)
DatadiagramMLBasicDef_DelElt.attributes={DatadiagramMLBasicDef_DelElt_del_}

# DatadiagramMLBasicDef_Geom class attributes and methods

# IXElt class attributes and methods

# DelElt class attributes and methods

# CellType class attributes and methods

# LineTo class attributes and methods

# DatadiagramMLBasicDef_LineTo class attributes and methods

# XYElt class attributes and methods

# Geom class attributes and methods

# DatadiagramMLBasicDef_MoveTo class attributes and methods

# Ellipse class attributes and methods

# EllipticalArcTo class attributes and methods

# SplineStart class attributes and methods

# NURBSTo class attributes and methods

# DatadiagramMLBasicDef_XYElt class attributes and methods

# DatadiagramMLBasicDef_XYABElt class attributes and methods

# DatadiagramMLBasicDef_InfiniteLine class attributes and methods

# XYABElt class attributes and methods

# DatadiagramMLBasicDef_XYAElt class attributes and methods

# DatadiagramMLBasicDef_ArcTo class attributes and methods

# XYAElt class attributes and methods

# DatadiagramMLBasicDef_SplineKnot class attributes and methods

# DatadiagramMLBasicDef_PolylineTo class attributes and methods

# DatadiagramMLBasicDef_XYABCDEElt class attributes and methods

# DatadiagramMLBasicDef_NURBSTo class attributes and methods

# XYABCDEElt class attributes and methods

# DatadiagramMLBasicDef_Text class attributes and methods

# TextElt class attributes and methods

# DatadiagramMLBasicDef_XYABCDElt class attributes and methods

# DatadiagramMLBasicDef_Ellipse class attributes and methods

# XYABCDElt class attributes and methods

# DatadiagramMLBasicDef_EllipticalArcTo class attributes and methods

# DatadiagramMLBasicDef_SplineStart class attributes and methods

# Master class attributes and methods

# MasterShortCut class attributes and methods

# DatadiagramMLBasicDef_MasterShortCut class attributes and methods
DatadiagramMLBasicDef_MasterShortCut_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLBasicDef_MasterShortCut_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLBasicDef_MasterShortCut_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLBasicDef_MasterShortCut_shortcutURL: Property = Property(name="shortcutURL", type=StringType)
DatadiagramMLBasicDef_MasterShortCut_shortcutHelp: Property = Property(name="shortcutHelp", type=StringType)
DatadiagramMLBasicDef_MasterShortCut_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLBasicDef_MasterShortCut.attributes={DatadiagramMLBasicDef_MasterShortCut_iconSize, DatadiagramMLBasicDef_MasterShortCut_shortcutURL, DatadiagramMLBasicDef_MasterShortCut_shortcutHelp, DatadiagramMLBasicDef_MasterShortCut_patternFlags, DatadiagramMLBasicDef_MasterShortCut_alignName, DatadiagramMLBasicDef_MasterShortCut_prompt}

# DatadiagramMLBasicDef_TextElt class attributes and methods

# Text class attributes and methods

# DatadiagramMLBasicDef_StringElt class attributes and methods
DatadiagramMLBasicDef_StringElt_value: Property = Property(name="value", type=StringType)
DatadiagramMLBasicDef_StringElt.attributes={DatadiagramMLBasicDef_StringElt_value}

# DatadiagramMLBasicDef_MastersCollection class attributes and methods

# Icon class attributes and methods

# DatadiagramMLBasicDef_Icon class attributes and methods
DatadiagramMLBasicDef_Icon_value: Property = Property(name="value", type=StringType)
DatadiagramMLBasicDef_Icon.attributes={DatadiagramMLBasicDef_Icon_value}

# DatadiagramMLBasicDef_Master class attributes and methods
DatadiagramMLBasicDef_Master_baseID: Property = Property(name="baseID", type=StringType)
DatadiagramMLBasicDef_Master_matchByName: Property = Property(name="matchByName", type=StringType)
DatadiagramMLBasicDef_Master_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLBasicDef_Master_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLBasicDef_Master_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLBasicDef_Master_hidden: Property = Property(name="hidden", type=StringType)
DatadiagramMLBasicDef_Master_iconUpdate: Property = Property(name="iconUpdate", type=StringType)
DatadiagramMLBasicDef_Master_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLBasicDef_Master.attributes={DatadiagramMLBasicDef_Master_iconSize, DatadiagramMLBasicDef_Master_alignName, DatadiagramMLBasicDef_Master_patternFlags, DatadiagramMLBasicDef_Master_prompt, DatadiagramMLBasicDef_Master_baseID, DatadiagramMLBasicDef_Master_iconUpdate, DatadiagramMLBasicDef_Master_matchByName, DatadiagramMLBasicDef_Master_hidden}

# DatadiagramMLBasicDef_MasterElt class attributes and methods

# DatadiagramMLBasicDef_PagesCollection class attributes and methods

# DatadiagramMLBasicDef_ShapesCollection class attributes and methods

# DatadiagramMLBasicDef_ConnectsCollection class attributes and methods

# Connect class attributes and methods

# DatadiagramMLBasicDef_Connect class attributes and methods
DatadiagramMLBasicDef_Connect_fromCell: Property = Property(name="fromCell", type=StringType)
DatadiagramMLBasicDef_Connect_toCell: Property = Property(name="toCell", type=StringType)
DatadiagramMLBasicDef_Connect_fromPart: Property = Property(name="fromPart", type=StringType)
DatadiagramMLBasicDef_Connect_toPart: Property = Property(name="toPart", type=StringType)
DatadiagramMLBasicDef_Connect_fromSheet: Property = Property(name="fromSheet", type=StringType)
DatadiagramMLBasicDef_Connect_toSheet: Property = Property(name="toSheet", type=StringType)
DatadiagramMLBasicDef_Connect.attributes={DatadiagramMLBasicDef_Connect_toCell, DatadiagramMLBasicDef_Connect_toSheet, DatadiagramMLBasicDef_Connect_fromPart, DatadiagramMLBasicDef_Connect_toPart, DatadiagramMLBasicDef_Connect_fromSheet, DatadiagramMLBasicDef_Connect_fromCell}

# ConnectsCollection class attributes and methods

# DatadiagramMLBasicDef_PageElt class attributes and methods

# DatadiagramMLBasicDef_DocumentSettingsElt class attributes and methods

# DatadiagramMLBasicDef_ColorsTable class attributes and methods

# Page class attributes and methods

# DatadiagramMLBasicDef_Page class attributes and methods
DatadiagramMLBasicDef_Page_background: Property = Property(name="background", type=StringType)
DatadiagramMLBasicDef_Page_backPage: Property = Property(name="backPage", type=StringType)
DatadiagramMLBasicDef_Page_viewScale: Property = Property(name="viewScale", type=StringType)
DatadiagramMLBasicDef_Page_viewCenterX: Property = Property(name="viewCenterX", type=StringType)
DatadiagramMLBasicDef_Page_ViewCenterY: Property = Property(name="ViewCenterY", type=StringType)
DatadiagramMLBasicDef_Page_reviewerID: Property = Property(name="reviewerID", type=StringType)
DatadiagramMLBasicDef_Page_associatedPage: Property = Property(name="associatedPage", type=StringType)
DatadiagramMLBasicDef_Page.attributes={DatadiagramMLBasicDef_Page_background, DatadiagramMLBasicDef_Page_viewScale, DatadiagramMLBasicDef_Page_backPage, DatadiagramMLBasicDef_Page_associatedPage, DatadiagramMLBasicDef_Page_reviewerID, DatadiagramMLBasicDef_Page_ViewCenterY, DatadiagramMLBasicDef_Page_viewCenterX}

# DatadiagramMLBasicDef_SolutionXML class attributes and methods

# DatadiagramMLBasicDef_PrintSetup class attributes and methods

# DatadiagramMLBasicDef_FontsTable class attributes and methods

# DatadiagramMLBasicDef_FaceNamesTable class attributes and methods

# DatadiagramMLBasicDef_WindowsInfo class attributes and methods

# DatadiagramMLBasicDef_EventList class attributes and methods

# DatadiagramMLBasicDef_HeaderFooter class attributes and methods

# Relationships
docPages9: BinaryAssociation = BinaryAssociation(
    name="docPages9",
    ends={
        Property(name="PagesCollection", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument10", type=PagesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docWindows11: BinaryAssociation = BinaryAssociation(
    name="docWindows11",
    ends={
        Property(name="WindowsInfo", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_visioDocument", type=WindowsInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docEventList12: BinaryAssociation = BinaryAssociation(
    name="docEventList12",
    ends={
        Property(name="EventList", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="el_visioDocument", type=EventList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docHeaderFooter13: BinaryAssociation = BinaryAssociation(
    name="docHeaderFooter13",
    ends={
        Property(name="HeaderFooter", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ef_visioDocument", type=HeaderFooter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docVBProjectData14: BinaryAssociation = BinaryAssociation(
    name="docVBProjectData14",
    ends={
        Property(name="VBProjectData", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="vpd_visioDocument", type=VBProjectData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docEmailRoutingData15: BinaryAssociation = BinaryAssociation(
    name="docEmailRoutingData15",
    ends={
        Property(name="EmailRoutingData", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="erd_visioDocument", type=EmailRoutingData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docSolutionXML16: BinaryAssociation = BinaryAssociation(
    name="docSolutionXML16",
    ends={
        Property(name="SolutionXML", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sx_visioDocument", type=SolutionXML, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docProps0: BinaryAssociation = BinaryAssociation(
    name="docProps0",
    ends={
        Property(name="DocumentPropertiesCollection", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dps_visioDocument", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docSettings1: BinaryAssociation = BinaryAssociation(
    name="docSettings1",
    ends={
        Property(name="DocumentSettingsElt", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dss_visioDocument", type=DocumentSettingsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docColors2: BinaryAssociation = BinaryAssociation(
    name="docColors2",
    ends={
        Property(name="ColorsTable", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_visioDocument", type=ColorsTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPrintSetup3: BinaryAssociation = BinaryAssociation(
    name="docPrintSetup3",
    ends={
        Property(name="PrintSetup", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument", type=PrintSetup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docFonts4: BinaryAssociation = BinaryAssociation(
    name="docFonts4",
    ends={
        Property(name="FontsTable", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fs_visioDocument", type=FontsTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docFaceNames5: BinaryAssociation = BinaryAssociation(
    name="docFaceNames5",
    ends={
        Property(name="FaceNamesTable", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fns_visioDocument", type=FaceNamesTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docStyleSheets6: BinaryAssociation = BinaryAssociation(
    name="docStyleSheets6",
    ends={
        Property(name="StyleSheetsCollection", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sss_visioDocument", type=StyleSheetsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docDocumentSheet7: BinaryAssociation = BinaryAssociation(
    name="docDocumentSheet7",
    ends={
        Property(name="DocumentSheet", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ds_visioDocument", type=DocumentSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docMasters8: BinaryAssociation = BinaryAssociation(
    name="docMasters8",
    ends={
        Property(name="MastersCollection", type=DatadiagramMLBasicDef_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ms_visioDocument", type=MastersCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customProps18: BinaryAssociation = BinaryAssociation(
    name="customProps18",
    ends={
        Property(name="CustomPropertiesCollection", type=DatadiagramMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cps_docProp", type=CustomPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCreated19: BinaryAssociation = BinaryAssociation(
    name="timeCreated19",
    ends={
        Property(name="DateTimeType", type=DatadiagramMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_DocumentPropertiesCollection", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSaved20: BinaryAssociation = BinaryAssociation(
    name="timeSaved20",
    ends={
        Property(name="DateTimeType22", type=DatadiagramMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_DocumentPropertiesCollection21", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeEdited23: BinaryAssociation = BinaryAssociation(
    name="timeEdited23",
    ends={
        Property(name="DateTimeType25", type=DatadiagramMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_DocumentPropertiesCollection24", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dps_visioDocument17: BinaryAssociation = BinaryAssociation(
    name="dps_visioDocument17",
    ends={
        Property(name="VisioDocument", type=DatadiagramMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docProps", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
erd_visioDocument36: BinaryAssociation = BinaryAssociation(
    name="erd_visioDocument36",
    ends={
        Property(name="VisioDocument37", type=DatadiagramMLBasicDef_EmailRoutingData, multiplicity=Multiplicity(1, 1)),
        Property(name="docEmailRoutingData", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
sss_visioDocument38: BinaryAssociation = BinaryAssociation(
    name="sss_visioDocument38",
    ends={
        Property(name="VisioDocument39", type=DatadiagramMLBasicDef_StyleSheetsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docStyleSheets", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
stylesSheets40: BinaryAssociation = BinaryAssociation(
    name="stylesSheets40",
    ends={
        Property(name="StyleSheet", type=DatadiagramMLBasicDef_StyleSheetsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_stylesSheets", type=StyleSheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timePrinted26: BinaryAssociation = BinaryAssociation(
    name="timePrinted26",
    ends={
        Property(name="DateTimeType28", type=DatadiagramMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_DocumentPropertiesCollection27", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cps_docProp29: BinaryAssociation = BinaryAssociation(
    name="cps_docProp29",
    ends={
        Property(name="DocumentPropertiesCollection30", type=DatadiagramMLBasicDef_CustomPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customProps", type=DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
cps_customProps31: BinaryAssociation = BinaryAssociation(
    name="cps_customProps31",
    ends={
        Property(name="CustomProperty", type=DatadiagramMLBasicDef_CustomPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cp_customProps", type=CustomProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cp_customProps32: BinaryAssociation = BinaryAssociation(
    name="cp_customProps32",
    ends={
        Property(name="CustomPropertiesCollection33", type=DatadiagramMLBasicDef_CustomProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="cps_customProps", type=CustomPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
vpd_visioDocument34: BinaryAssociation = BinaryAssociation(
    name="vpd_visioDocument34",
    ends={
        Property(name="VisioDocument35", type=DatadiagramMLBasicDef_VBProjectData, multiplicity=Multiplicity(1, 1)),
        Property(name="docVBProjectData", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ss_shapes45: BinaryAssociation = BinaryAssociation(
    name="ss_shapes45",
    ends={
        Property(name="ShapesCollection", type=DatadiagramMLBasicDef_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="shapes", type=ShapesCollection, multiplicity=Multiplicity(1, 1))
    }
)
shapeElts46: BinaryAssociation = BinaryAssociation(
    name="shapeElts46",
    ends={
        Property(name="ShapeElt", type=DatadiagramMLBasicDef_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="sse_shapeSheet", type=ShapeElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sse_shapeSheet47: BinaryAssociation = BinaryAssociation(
    name="sse_shapeSheet47",
    ends={
        Property(name="Shape", type=DatadiagramMLBasicDef_ShapeElt, multiplicity=Multiplicity(1, 1)),
        Property(name="shapeElts", type=Shape, multiplicity=Multiplicity(1, 1))
    }
)
ss_stylesSheets41: BinaryAssociation = BinaryAssociation(
    name="ss_stylesSheets41",
    ends={
        Property(name="StyleSheetsCollection42", type=DatadiagramMLBasicDef_StyleSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesSheets", type=StyleSheetsCollection, multiplicity=Multiplicity(1, 1))
    }
)
ds_visioDocument43: BinaryAssociation = BinaryAssociation(
    name="ds_visioDocument43",
    ends={
        Property(name="VisioDocument44", type=DatadiagramMLBasicDef_DocumentSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="docDocumentSheet", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
movesTo59: BinaryAssociation = BinaryAssociation(
    name="movesTo59",
    ends={
        Property(name="MoveTo", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_geom", type=MoveTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcsTo60: BinaryAssociation = BinaryAssociation(
    name="arcsTo60",
    ends={
        Property(name="ArcTo", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ac_geom", type=ArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineKnots61: BinaryAssociation = BinaryAssociation(
    name="splineKnots61",
    ends={
        Property(name="SplineKnot", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="sk_geom", type=SplineKnot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
polylinesTo62: BinaryAssociation = BinaryAssociation(
    name="polylinesTo62",
    ends={
        Property(name="PolylineTo", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="pt_geom", type=PolylineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
noFill48: BinaryAssociation = BinaryAssociation(
    name="noFill48",
    ends={
        Property(name="CellType", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_Geom", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noLine49: BinaryAssociation = BinaryAssociation(
    name="noLine49",
    ends={
        Property(name="CellType51", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_Geom50", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noShow52: BinaryAssociation = BinaryAssociation(
    name="noShow52",
    ends={
        Property(name="CellType54", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_Geom53", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noSnap55: BinaryAssociation = BinaryAssociation(
    name="noSnap55",
    ends={
        Property(name="CellType57", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_Geom56", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linesTo58: BinaryAssociation = BinaryAssociation(
    name="linesTo58",
    ends={
        Property(name="LineTo", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="lt_geom", type=LineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
x68: BinaryAssociation = BinaryAssociation(
    name="x68",
    ends={
        Property(name="CellType69", type=DatadiagramMLBasicDef_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
y70: BinaryAssociation = BinaryAssociation(
    name="y70",
    ends={
        Property(name="CellType72", type=DatadiagramMLBasicDef_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYElt71", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lt_geom73: BinaryAssociation = BinaryAssociation(
    name="lt_geom73",
    ends={
        Property(name="Geom", type=DatadiagramMLBasicDef_LineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="linesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
infiniteLines63: BinaryAssociation = BinaryAssociation(
    name="infiniteLines63",
    ends={
        Property(name="InfiniteLine", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="il_geom", type=InfiniteLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipses64: BinaryAssociation = BinaryAssociation(
    name="ellipses64",
    ends={
        Property(name="Ellipse", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="e_geom", type=Ellipse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipticalArcsTo65: BinaryAssociation = BinaryAssociation(
    name="ellipticalArcsTo65",
    ends={
        Property(name="EllipticalArcTo", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="eat_geom", type=EllipticalArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineStarts66: BinaryAssociation = BinaryAssociation(
    name="splineStarts66",
    ends={
        Property(name="SplineStart", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_geom", type=SplineStart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nurbsTo67: BinaryAssociation = BinaryAssociation(
    name="nurbsTo67",
    ends={
        Property(name="NURBSTo", type=DatadiagramMLBasicDef_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="nt_geom", type=NURBSTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pt_geom82: BinaryAssociation = BinaryAssociation(
    name="pt_geom82",
    ends={
        Property(name="Geom83", type=DatadiagramMLBasicDef_PolylineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="polylinesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
b84: BinaryAssociation = BinaryAssociation(
    name="b84",
    ends={
        Property(name="CellType85", type=DatadiagramMLBasicDef_XYABElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYABElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_geom86: BinaryAssociation = BinaryAssociation(
    name="il_geom86",
    ends={
        Property(name="Geom87", type=DatadiagramMLBasicDef_InfiniteLine, multiplicity=Multiplicity(1, 1)),
        Property(name="infiniteLines", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
mt_geom74: BinaryAssociation = BinaryAssociation(
    name="mt_geom74",
    ends={
        Property(name="Geom75", type=DatadiagramMLBasicDef_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="movesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
a76: BinaryAssociation = BinaryAssociation(
    name="a76",
    ends={
        Property(name="CellType77", type=DatadiagramMLBasicDef_XYAElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYAElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ac_geom78: BinaryAssociation = BinaryAssociation(
    name="ac_geom78",
    ends={
        Property(name="Geom79", type=DatadiagramMLBasicDef_ArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="arcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
sk_geom80: BinaryAssociation = BinaryAssociation(
    name="sk_geom80",
    ends={
        Property(name="Geom81", type=DatadiagramMLBasicDef_SplineKnot, multiplicity=Multiplicity(1, 1)),
        Property(name="splineKnots", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
e99: BinaryAssociation = BinaryAssociation(
    name="e99",
    ends={
        Property(name="CellType100", type=DatadiagramMLBasicDef_XYABCDEElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYABCDEElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nt_geom101: BinaryAssociation = BinaryAssociation(
    name="nt_geom101",
    ends={
        Property(name="Geom102", type=DatadiagramMLBasicDef_NURBSTo, multiplicity=Multiplicity(1, 1)),
        Property(name="nurbsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
textElts103: BinaryAssociation = BinaryAssociation(
    name="textElts103",
    ends={
        Property(name="TextElt", type=DatadiagramMLBasicDef_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="te_text", type=TextElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c88: BinaryAssociation = BinaryAssociation(
    name="c88",
    ends={
        Property(name="CellType89", type=DatadiagramMLBasicDef_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYABCDElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d90: BinaryAssociation = BinaryAssociation(
    name="d90",
    ends={
        Property(name="CellType92", type=DatadiagramMLBasicDef_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLBasicDef_XYABCDElt91", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e_geom93: BinaryAssociation = BinaryAssociation(
    name="e_geom93",
    ends={
        Property(name="Geom94", type=DatadiagramMLBasicDef_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipses", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
eat_geom95: BinaryAssociation = BinaryAssociation(
    name="eat_geom95",
    ends={
        Property(name="Geom96", type=DatadiagramMLBasicDef_EllipticalArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipticalArcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
ss_geom97: BinaryAssociation = BinaryAssociation(
    name="ss_geom97",
    ends={
        Property(name="Geom98", type=DatadiagramMLBasicDef_SplineStart, multiplicity=Multiplicity(1, 1)),
        Property(name="splineStarts", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
masters107: BinaryAssociation = BinaryAssociation(
    name="masters107",
    ends={
        Property(name="Master", type=DatadiagramMLBasicDef_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masters", type=Master, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
masterShortCuts108: BinaryAssociation = BinaryAssociation(
    name="masterShortCuts108",
    ends={
        Property(name="MasterShortCut", type=DatadiagramMLBasicDef_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masterShortCuts", type=MasterShortCut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
m_masterShortCuts109: BinaryAssociation = BinaryAssociation(
    name="m_masterShortCuts109",
    ends={
        Property(name="MastersCollection110", type=DatadiagramMLBasicDef_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="masterShortCuts", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
te_text104: BinaryAssociation = BinaryAssociation(
    name="te_text104",
    ends={
        Property(name="Text", type=DatadiagramMLBasicDef_TextElt, multiplicity=Multiplicity(1, 1)),
        Property(name="textElts", type=Text, multiplicity=Multiplicity(1, 1))
    }
)
m_masters114: BinaryAssociation = BinaryAssociation(
    name="m_masters114",
    ends={
        Property(name="masters", type=MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="MastersCollection115", type=DatadiagramMLBasicDef_Master, multiplicity=Multiplicity(1, 1))
    }
)
ms_visioDocument105: BinaryAssociation = BinaryAssociation(
    name="ms_visioDocument105",
    ends={
        Property(name="VisioDocument106", type=DatadiagramMLBasicDef_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docMasters", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
icons111: BinaryAssociation = BinaryAssociation(
    name="icons111",
    ends={
        Property(name="Icon", type=DatadiagramMLBasicDef_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="i_masterShortCut", type=Icon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i_masterShortCut112: BinaryAssociation = BinaryAssociation(
    name="i_masterShortCut112",
    ends={
        Property(name="MasterShortCut113", type=DatadiagramMLBasicDef_Icon, multiplicity=Multiplicity(1, 1)),
        Property(name="icons", type=MasterShortCut, multiplicity=Multiplicity(1, 1))
    }
)
me_master121: BinaryAssociation = BinaryAssociation(
    name="me_master121",
    ends={
        Property(name="Master122", type=DatadiagramMLBasicDef_MasterElt, multiplicity=Multiplicity(1, 1)),
        Property(name="masterElts", type=Master, multiplicity=Multiplicity(1, 1))
    }
)
masterElts116: BinaryAssociation = BinaryAssociation(
    name="masterElts116",
    ends={
        Property(name="MasterElt", type=DatadiagramMLBasicDef_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="me_master", type=MasterElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shapes117: BinaryAssociation = BinaryAssociation(
    name="shapes117",
    ends={
        Property(name="Shape118", type=DatadiagramMLBasicDef_ShapesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_shapes", type=Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections119: BinaryAssociation = BinaryAssociation(
    name="connections119",
    ends={
        Property(name="Connect", type=DatadiagramMLBasicDef_ConnectsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_connects", type=Connect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_connects120: BinaryAssociation = BinaryAssociation(
    name="c_connects120",
    ends={
        Property(name="ConnectsCollection", type=DatadiagramMLBasicDef_Connect, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=ConnectsCollection, multiplicity=Multiplicity(1, 1))
    }
)
pageElts128: BinaryAssociation = BinaryAssociation(
    name="pageElts128",
    ends={
        Property(name="pe_page", type=PageElt, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PageElt", type=DatadiagramMLBasicDef_Page, multiplicity=Multiplicity(1, 1))
    }
)
pe_page129: BinaryAssociation = BinaryAssociation(
    name="pe_page129",
    ends={
        Property(name="Page130", type=DatadiagramMLBasicDef_PageElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pageElts", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
dss_visioDocument131: BinaryAssociation = BinaryAssociation(
    name="dss_visioDocument131",
    ends={
        Property(name="VisioDocument132", type=DatadiagramMLBasicDef_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="docSettings", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
cs_visioDocument133: BinaryAssociation = BinaryAssociation(
    name="cs_visioDocument133",
    ends={
        Property(name="VisioDocument134", type=DatadiagramMLBasicDef_ColorsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docColors", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument123: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument123",
    ends={
        Property(name="VisioDocument124", type=DatadiagramMLBasicDef_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docPages", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
pages125: BinaryAssociation = BinaryAssociation(
    name="pages125",
    ends={
        Property(name="Page", type=DatadiagramMLBasicDef_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="p_pages", type=Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p_pages126: BinaryAssociation = BinaryAssociation(
    name="p_pages126",
    ends={
        Property(name="PagesCollection127", type=DatadiagramMLBasicDef_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=PagesCollection, multiplicity=Multiplicity(1, 1))
    }
)
ef_visioDocument145: BinaryAssociation = BinaryAssociation(
    name="ef_visioDocument145",
    ends={
        Property(name="VisioDocument146", type=DatadiagramMLBasicDef_HeaderFooter, multiplicity=Multiplicity(1, 1)),
        Property(name="docHeaderFooter", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
sx_visioDocument147: BinaryAssociation = BinaryAssociation(
    name="sx_visioDocument147",
    ends={
        Property(name="VisioDocument148", type=DatadiagramMLBasicDef_SolutionXML, multiplicity=Multiplicity(1, 1)),
        Property(name="docSolutionXML", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument135: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument135",
    ends={
        Property(name="VisioDocument136", type=DatadiagramMLBasicDef_PrintSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="docPrintSetup", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
fs_visioDocument137: BinaryAssociation = BinaryAssociation(
    name="fs_visioDocument137",
    ends={
        Property(name="VisioDocument138", type=DatadiagramMLBasicDef_FontsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docFonts", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
fns_visioDocument139: BinaryAssociation = BinaryAssociation(
    name="fns_visioDocument139",
    ends={
        Property(name="VisioDocument140", type=DatadiagramMLBasicDef_FaceNamesTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docFaceNames", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ws_visioDocument141: BinaryAssociation = BinaryAssociation(
    name="ws_visioDocument141",
    ends={
        Property(name="VisioDocument142", type=DatadiagramMLBasicDef_WindowsInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="docWindows", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
el_visioDocument143: BinaryAssociation = BinaryAssociation(
    name="el_visioDocument143",
    ends={
        Property(name="VisioDocument144", type=DatadiagramMLBasicDef_EventList, multiplicity=Multiplicity(1, 1)),
        Property(name="docEventList", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_DatadiagramMLBasicDef_StyleSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLBasicDef_StyleSheet)
gen_DatadiagramMLBasicDef_StyleSheet_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLBasicDef_StyleSheet)
gen_DatadiagramMLBasicDef_StyleSheet_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLBasicDef_StyleSheet)
gen_DatadiagramMLBasicDef_DocumentSheet_PageSheet = Generalization(general=PageSheet, specific=DatadiagramMLBasicDef_DocumentSheet)
gen_DatadiagramMLBasicDef_DocumentSheet_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLBasicDef_DocumentSheet)
gen_DatadiagramMLBasicDef_PageSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLBasicDef_PageSheet)
gen_DatadiagramMLBasicDef_PageSheet_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLBasicDef_PageSheet)
gen_DatadiagramMLBasicDef_PageSheet_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLBasicDef_PageSheet)
gen_DatadiagramMLBasicDef_PageSheet_PageElt = Generalization(general=PageElt, specific=DatadiagramMLBasicDef_PageSheet)
gen_DatadiagramMLBasicDef_Geom_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLBasicDef_Geom)
gen_DatadiagramMLBasicDef_Geom_IXElt = Generalization(general=IXElt, specific=DatadiagramMLBasicDef_Geom)
gen_DatadiagramMLBasicDef_Geom_DelElt = Generalization(general=DelElt, specific=DatadiagramMLBasicDef_Geom)
gen_DatadiagramMLBasicDef_LineTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLBasicDef_LineTo)
gen_DatadiagramMLBasicDef_MoveTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLBasicDef_MoveTo)
gen_DatadiagramMLBasicDef_XYElt_IXElt = Generalization(general=IXElt, specific=DatadiagramMLBasicDef_XYElt)
gen_DatadiagramMLBasicDef_XYElt_DelElt = Generalization(general=DelElt, specific=DatadiagramMLBasicDef_XYElt)
gen_DatadiagramMLBasicDef_XYABElt_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLBasicDef_XYABElt)
gen_DatadiagramMLBasicDef_InfiniteLine_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLBasicDef_InfiniteLine)
gen_DatadiagramMLBasicDef_XYAElt_XYElt = Generalization(general=XYElt, specific=DatadiagramMLBasicDef_XYAElt)
gen_DatadiagramMLBasicDef_ArcTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLBasicDef_ArcTo)
gen_DatadiagramMLBasicDef_SplineKnot_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLBasicDef_SplineKnot)
gen_DatadiagramMLBasicDef_PolylineTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLBasicDef_PolylineTo)
gen_DatadiagramMLBasicDef_XYABCDEElt_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLBasicDef_XYABCDEElt)
gen_DatadiagramMLBasicDef_NURBSTo_XYABCDEElt = Generalization(general=XYABCDEElt, specific=DatadiagramMLBasicDef_NURBSTo)
gen_DatadiagramMLBasicDef_Text_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLBasicDef_Text)
gen_DatadiagramMLBasicDef_XYABCDElt_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLBasicDef_XYABCDElt)
gen_DatadiagramMLBasicDef_Ellipse_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLBasicDef_Ellipse)
gen_DatadiagramMLBasicDef_EllipticalArcTo_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLBasicDef_EllipticalArcTo)
gen_DatadiagramMLBasicDef_SplineStart_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLBasicDef_SplineStart)
gen_DatadiagramMLBasicDef_MasterShortCut_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLBasicDef_MasterShortCut)
gen_DatadiagramMLBasicDef_MasterShortCut_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLBasicDef_MasterShortCut)
gen_DatadiagramMLBasicDef_StringElt_TextElt = Generalization(general=TextElt, specific=DatadiagramMLBasicDef_StringElt)
gen_DatadiagramMLBasicDef_Icon_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLBasicDef_Icon)
gen_DatadiagramMLBasicDef_Master_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLBasicDef_Master)
gen_DatadiagramMLBasicDef_Master_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLBasicDef_Master)
gen_DatadiagramMLBasicDef_Master_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLBasicDef_Master)
gen_DatadiagramMLBasicDef_ShapesCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLBasicDef_ShapesCollection)
gen_DatadiagramMLBasicDef_ShapesCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLBasicDef_ShapesCollection)
gen_DatadiagramMLBasicDef_ConnectsCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLBasicDef_ConnectsCollection)
gen_DatadiagramMLBasicDef_ConnectsCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLBasicDef_ConnectsCollection)
gen_DatadiagramMLBasicDef_Page_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLBasicDef_Page)
gen_DatadiagramMLBasicDef_Page_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLBasicDef_Page)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={DatadiagramMLBasicDef_CellType, DatadiagramMLBasicDef_VisioDocument, DatadiagramMLBasicDef_DateTimeType, PagesCollection, WindowsInfo, EventList, HeaderFooter, VBProjectData, EmailRoutingData, SolutionXML, DocumentPropertiesCollection, DocumentSettingsElt, ColorsTable, PrintSetup, FontsTable, FaceNamesTable, StyleSheetsCollection, DocumentSheet, MastersCollection, CustomPropertiesCollection, DateTimeType, DatadiagramMLBasicDef_DocumentPropertiesCollection, VisioDocument, DatadiagramMLBasicDef_StyleSheetsCollection, StyleSheet, DatadiagramMLBasicDef_StyleSheet, Shape, IdentifiedElt, DatadiagramMLBasicDef_CustomPropertiesCollection, CustomProperty, DatadiagramMLBasicDef_CustomProperty, DatadiagramMLBasicDef_VBProjectData, DatadiagramMLBasicDef_EmailRoutingData, DatadiagramMLBasicDef_Shape, ShapesCollection, ShapeElt, DatadiagramMLBasicDef_ShapeElt, NamedElt, DatadiagramMLBasicDef_DocumentSheet, PageSheet, DatadiagramMLBasicDef_PageSheet, UniqueIdElt, MasterElt, PageElt, DatadiagramMLBasicDef_NamedElt, DatadiagramMLBasicDef_IdentifiedElt, DatadiagramMLBasicDef_UniqueIdElt, MoveTo, ArcTo, SplineKnot, PolylineTo, InfiniteLine, DatadiagramMLBasicDef_IXElt, DatadiagramMLBasicDef_DelElt, DatadiagramMLBasicDef_Geom, IXElt, DelElt, CellType, LineTo, DatadiagramMLBasicDef_LineTo, XYElt, Geom, DatadiagramMLBasicDef_MoveTo, Ellipse, EllipticalArcTo, SplineStart, NURBSTo, DatadiagramMLBasicDef_XYElt, DatadiagramMLBasicDef_XYABElt, DatadiagramMLBasicDef_InfiniteLine, XYABElt, DatadiagramMLBasicDef_XYAElt, DatadiagramMLBasicDef_ArcTo, XYAElt, DatadiagramMLBasicDef_SplineKnot, DatadiagramMLBasicDef_PolylineTo, DatadiagramMLBasicDef_XYABCDEElt, DatadiagramMLBasicDef_NURBSTo, XYABCDEElt, DatadiagramMLBasicDef_Text, TextElt, DatadiagramMLBasicDef_XYABCDElt, DatadiagramMLBasicDef_Ellipse, XYABCDElt, DatadiagramMLBasicDef_EllipticalArcTo, DatadiagramMLBasicDef_SplineStart, Master, MasterShortCut, DatadiagramMLBasicDef_MasterShortCut, DatadiagramMLBasicDef_TextElt, Text, DatadiagramMLBasicDef_StringElt, DatadiagramMLBasicDef_MastersCollection, Icon, DatadiagramMLBasicDef_Icon, DatadiagramMLBasicDef_Master, DatadiagramMLBasicDef_MasterElt, DatadiagramMLBasicDef_PagesCollection, DatadiagramMLBasicDef_ShapesCollection, DatadiagramMLBasicDef_ConnectsCollection, Connect, DatadiagramMLBasicDef_Connect, ConnectsCollection, DatadiagramMLBasicDef_PageElt, DatadiagramMLBasicDef_DocumentSettingsElt, DatadiagramMLBasicDef_ColorsTable, Page, DatadiagramMLBasicDef_Page, DatadiagramMLBasicDef_SolutionXML, DatadiagramMLBasicDef_PrintSetup, DatadiagramMLBasicDef_FontsTable, DatadiagramMLBasicDef_FaceNamesTable, DatadiagramMLBasicDef_WindowsInfo, DatadiagramMLBasicDef_EventList, DatadiagramMLBasicDef_HeaderFooter},
    associations={docPages9, docWindows11, docEventList12, docHeaderFooter13, docVBProjectData14, docEmailRoutingData15, docSolutionXML16, docProps0, docSettings1, docColors2, docPrintSetup3, docFonts4, docFaceNames5, docStyleSheets6, docDocumentSheet7, docMasters8, customProps18, timeCreated19, timeSaved20, timeEdited23, dps_visioDocument17, erd_visioDocument36, sss_visioDocument38, stylesSheets40, timePrinted26, cps_docProp29, cps_customProps31, cp_customProps32, vpd_visioDocument34, ss_shapes45, shapeElts46, sse_shapeSheet47, ss_stylesSheets41, ds_visioDocument43, movesTo59, arcsTo60, splineKnots61, polylinesTo62, noFill48, noLine49, noShow52, noSnap55, linesTo58, x68, y70, lt_geom73, infiniteLines63, ellipses64, ellipticalArcsTo65, splineStarts66, nurbsTo67, pt_geom82, b84, il_geom86, mt_geom74, a76, ac_geom78, sk_geom80, e99, nt_geom101, textElts103, c88, d90, e_geom93, eat_geom95, ss_geom97, masters107, masterShortCuts108, m_masterShortCuts109, te_text104, m_masters114, ms_visioDocument105, icons111, i_masterShortCut112, me_master121, masterElts116, shapes117, connections119, c_connects120, pageElts128, pe_page129, dss_visioDocument131, cs_visioDocument133, ps_visioDocument123, pages125, p_pages126, ef_visioDocument145, sx_visioDocument147, ps_visioDocument135, fs_visioDocument137, fns_visioDocument139, ws_visioDocument141, el_visioDocument143},
    generalizations={gen_DatadiagramMLBasicDef_StyleSheet_Shape, gen_DatadiagramMLBasicDef_StyleSheet_IdentifiedElt, gen_DatadiagramMLBasicDef_StyleSheet_NamedElt, gen_DatadiagramMLBasicDef_DocumentSheet_PageSheet, gen_DatadiagramMLBasicDef_DocumentSheet_NamedElt, gen_DatadiagramMLBasicDef_PageSheet_Shape, gen_DatadiagramMLBasicDef_PageSheet_UniqueIdElt, gen_DatadiagramMLBasicDef_PageSheet_MasterElt, gen_DatadiagramMLBasicDef_PageSheet_PageElt, gen_DatadiagramMLBasicDef_Geom_ShapeElt, gen_DatadiagramMLBasicDef_Geom_IXElt, gen_DatadiagramMLBasicDef_Geom_DelElt, gen_DatadiagramMLBasicDef_LineTo_XYElt, gen_DatadiagramMLBasicDef_MoveTo_XYElt, gen_DatadiagramMLBasicDef_XYElt_IXElt, gen_DatadiagramMLBasicDef_XYElt_DelElt, gen_DatadiagramMLBasicDef_XYABElt_XYAElt, gen_DatadiagramMLBasicDef_InfiniteLine_XYABElt, gen_DatadiagramMLBasicDef_XYAElt_XYElt, gen_DatadiagramMLBasicDef_ArcTo_XYAElt, gen_DatadiagramMLBasicDef_SplineKnot_XYAElt, gen_DatadiagramMLBasicDef_PolylineTo_XYAElt, gen_DatadiagramMLBasicDef_XYABCDEElt_XYABCDElt, gen_DatadiagramMLBasicDef_NURBSTo_XYABCDEElt, gen_DatadiagramMLBasicDef_Text_ShapeElt, gen_DatadiagramMLBasicDef_XYABCDElt_XYABElt, gen_DatadiagramMLBasicDef_Ellipse_XYABCDElt, gen_DatadiagramMLBasicDef_EllipticalArcTo_XYABCDElt, gen_DatadiagramMLBasicDef_SplineStart_XYABCDElt, gen_DatadiagramMLBasicDef_MasterShortCut_IdentifiedElt, gen_DatadiagramMLBasicDef_MasterShortCut_NamedElt, gen_DatadiagramMLBasicDef_StringElt_TextElt, gen_DatadiagramMLBasicDef_Icon_MasterElt, gen_DatadiagramMLBasicDef_Master_IdentifiedElt, gen_DatadiagramMLBasicDef_Master_UniqueIdElt, gen_DatadiagramMLBasicDef_Master_NamedElt, gen_DatadiagramMLBasicDef_ShapesCollection_MasterElt, gen_DatadiagramMLBasicDef_ShapesCollection_PageElt, gen_DatadiagramMLBasicDef_ConnectsCollection_MasterElt, gen_DatadiagramMLBasicDef_ConnectsCollection_PageElt, gen_DatadiagramMLBasicDef_Page_IdentifiedElt, gen_DatadiagramMLBasicDef_Page_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)