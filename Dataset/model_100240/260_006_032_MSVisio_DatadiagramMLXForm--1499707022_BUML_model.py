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
DatadiagramMLXForm_DateTimeType = Class(name="DatadiagramMLXForm_DateTimeType")
DocumentSettingsElt = Class(name="DocumentSettingsElt")
ColorsTable = Class(name="ColorsTable")
DatadiagramMLXForm_CellType = Class(name="DatadiagramMLXForm_CellType")
PrintSetup = Class(name="PrintSetup")
FontsTable = Class(name="FontsTable")
FaceNamesTable = Class(name="FaceNamesTable")
DatadiagramMLXForm_VisioDocument = Class(name="DatadiagramMLXForm_VisioDocument")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
EmailRoutingData = Class(name="EmailRoutingData")
SolutionXML = Class(name="SolutionXML")
DatadiagramMLXForm_DocumentPropertiesCollection = Class(name="DatadiagramMLXForm_DocumentPropertiesCollection")
VisioDocument = Class(name="VisioDocument")
StyleSheetsCollection = Class(name="StyleSheetsCollection")
DocumentSheet = Class(name="DocumentSheet")
MastersCollection = Class(name="MastersCollection")
PagesCollection = Class(name="PagesCollection")
WindowsInfo = Class(name="WindowsInfo")
EventList = Class(name="EventList")
HeaderFooter = Class(name="HeaderFooter")
VBProjectData = Class(name="VBProjectData")
DatadiagramMLXForm_CustomPropertiesCollection = Class(name="DatadiagramMLXForm_CustomPropertiesCollection")
CustomProperty = Class(name="CustomProperty")
DatadiagramMLXForm_CustomProperty = Class(name="DatadiagramMLXForm_CustomProperty")
DatadiagramMLXForm_DocumentSettingsElt = Class(name="DatadiagramMLXForm_DocumentSettingsElt")
CustomPropertiesCollection = Class(name="CustomPropertiesCollection")
DateTimeType = Class(name="DateTimeType")
DatadiagramMLXForm_SnapAnglesCollection = Class(name="DatadiagramMLXForm_SnapAnglesCollection")
SnapAngle = Class(name="SnapAngle")
DatadiagramMLXForm_SnapAngle = Class(name="DatadiagramMLXForm_SnapAngle")
Page = Class(name="Page")
DatadiagramMLXForm_ColorsTable = Class(name="DatadiagramMLXForm_ColorsTable")
StyleSheet = Class(name="StyleSheet")
ColorEntry = Class(name="ColorEntry")
DatadiagramMLXForm_ColorEntry = Class(name="DatadiagramMLXForm_ColorEntry")
IXrequiredElt = Class(name="IXrequiredElt")
SnapAnglesCollection = Class(name="SnapAnglesCollection")
DatadiagramMLXForm_PrintSetup = Class(name="DatadiagramMLXForm_PrintSetup")
DatadiagramMLXForm_FontsTable = Class(name="DatadiagramMLXForm_FontsTable")
FontEntry = Class(name="FontEntry")
DatadiagramMLXForm_FontEntry = Class(name="DatadiagramMLXForm_FontEntry")
IdentifiedElt = Class(name="IdentifiedElt")
DatadiagramMLXForm_FaceName = Class(name="DatadiagramMLXForm_FaceName")
DatadiagramMLXForm_VBProjectData = Class(name="DatadiagramMLXForm_VBProjectData")
DatadiagramMLXForm_EmailRoutingData = Class(name="DatadiagramMLXForm_EmailRoutingData")
DatadiagramMLXForm_StyleSheetsCollection = Class(name="DatadiagramMLXForm_StyleSheetsCollection")
DatadiagramMLXForm_FaceNamesTable = Class(name="DatadiagramMLXForm_FaceNamesTable")
FaceName = Class(name="FaceName")
DatadiagramMLXForm_StyleSheet = Class(name="DatadiagramMLXForm_StyleSheet")
Shape = Class(name="Shape")
NamedElt = Class(name="NamedElt")
DatadiagramMLXForm_DocumentSheet = Class(name="DatadiagramMLXForm_DocumentSheet")
PageSheet = Class(name="PageSheet")
DatadiagramMLXForm_UniqueIdElt = Class(name="DatadiagramMLXForm_UniqueIdElt", is_abstract=True)
DatadiagramMLXForm_Shape = Class(name="DatadiagramMLXForm_Shape")
ShapesCollection = Class(name="ShapesCollection")
ShapeElt = Class(name="ShapeElt")
DatadiagramMLXForm_ShapeElt = Class(name="DatadiagramMLXForm_ShapeElt", is_abstract=True)
DatadiagramMLXForm_IXElt = Class(name="DatadiagramMLXForm_IXElt", is_abstract=True)
DatadiagramMLXForm_DelElt = Class(name="DatadiagramMLXForm_DelElt", is_abstract=True)
DatadiagramMLXForm_Geom = Class(name="DatadiagramMLXForm_Geom")
IXElt = Class(name="IXElt")
DelElt = Class(name="DelElt")
DatadiagramMLXForm_PageSheet = Class(name="DatadiagramMLXForm_PageSheet")
UniqueIdElt = Class(name="UniqueIdElt")
MasterElt = Class(name="MasterElt")
PageElt = Class(name="PageElt")
DatadiagramMLXForm_NamedElt = Class(name="DatadiagramMLXForm_NamedElt", is_abstract=True)
DatadiagramMLXForm_IdentifiedElt = Class(name="DatadiagramMLXForm_IdentifiedElt", is_abstract=True)
LineTo = Class(name="LineTo")
MoveTo = Class(name="MoveTo")
ArcTo = Class(name="ArcTo")
SplineKnot = Class(name="SplineKnot")
PolylineTo = Class(name="PolylineTo")
InfiniteLine = Class(name="InfiniteLine")
Ellipse = Class(name="Ellipse")
EllipticalArcTo = Class(name="EllipticalArcTo")
SplineStart = Class(name="SplineStart")
NURBSTo = Class(name="NURBSTo")
CellType = Class(name="CellType")
DatadiagramMLXForm_MoveTo = Class(name="DatadiagramMLXForm_MoveTo")
DatadiagramMLXForm_XYAElt = Class(name="DatadiagramMLXForm_XYAElt", is_abstract=True)
DatadiagramMLXForm_ArcTo = Class(name="DatadiagramMLXForm_ArcTo")
XYAElt = Class(name="XYAElt")
DatadiagramMLXForm_SplineKnot = Class(name="DatadiagramMLXForm_SplineKnot")
DatadiagramMLXForm_PolylineTo = Class(name="DatadiagramMLXForm_PolylineTo")
DatadiagramMLXForm_XYABElt = Class(name="DatadiagramMLXForm_XYABElt", is_abstract=True)
DatadiagramMLXForm_InfiniteLine = Class(name="DatadiagramMLXForm_InfiniteLine")
XYABElt = Class(name="XYABElt")
DatadiagramMLXForm_XYElt = Class(name="DatadiagramMLXForm_XYElt", is_abstract=True)
DatadiagramMLXForm_LineTo = Class(name="DatadiagramMLXForm_LineTo")
XYElt = Class(name="XYElt")
Geom = Class(name="Geom")
DatadiagramMLXForm_TextElt = Class(name="DatadiagramMLXForm_TextElt", is_abstract=True)
Text = Class(name="Text")
DatadiagramMLXForm_IXrequiredElt = Class(name="DatadiagramMLXForm_IXrequiredElt", is_abstract=True)
DatadiagramMLXForm_Cp = Class(name="DatadiagramMLXForm_Cp")
DatadiagramMLXForm_Pp = Class(name="DatadiagramMLXForm_Pp")
DatadiagramMLXForm_XYABCDElt = Class(name="DatadiagramMLXForm_XYABCDElt", is_abstract=True)
DatadiagramMLXForm_Ellipse = Class(name="DatadiagramMLXForm_Ellipse")
XYABCDElt = Class(name="XYABCDElt")
DatadiagramMLXForm_EllipticalArcTo = Class(name="DatadiagramMLXForm_EllipticalArcTo")
DatadiagramMLXForm_SplineStart = Class(name="DatadiagramMLXForm_SplineStart")
DatadiagramMLXForm_XYABCDEElt = Class(name="DatadiagramMLXForm_XYABCDEElt", is_abstract=True)
DatadiagramMLXForm_NURBSTo = Class(name="DatadiagramMLXForm_NURBSTo")
XYABCDEElt = Class(name="XYABCDEElt")
DatadiagramMLXForm_Text = Class(name="DatadiagramMLXForm_Text")
TextElt = Class(name="TextElt")
DatadiagramMLXForm_Tp = Class(name="DatadiagramMLXForm_Tp")
DatadiagramMLXForm_Fld = Class(name="DatadiagramMLXForm_Fld")
DatadiagramMLXForm_StringElt = Class(name="DatadiagramMLXForm_StringElt")
DatadiagramMLXForm_Char = Class(name="DatadiagramMLXForm_Char")
DatadiagramMLXForm_Para = Class(name="DatadiagramMLXForm_Para")
DatadiagramMLXForm_TabsCollection = Class(name="DatadiagramMLXForm_TabsCollection")
Tab = Class(name="Tab")
DatadiagramMLXForm_Tab = Class(name="DatadiagramMLXForm_Tab")
TabsCollection = Class(name="TabsCollection")
DatadiagramMLXForm_Field = Class(name="DatadiagramMLXForm_Field")
DatadiagramMLXForm_MastersCollection = Class(name="DatadiagramMLXForm_MastersCollection")
DatadiagramMLXForm_XForm = Class(name="DatadiagramMLXForm_XForm")
Icon = Class(name="Icon")
DatadiagramMLXForm_Icon = Class(name="DatadiagramMLXForm_Icon")
Master = Class(name="Master")
DatadiagramMLXForm_Master = Class(name="DatadiagramMLXForm_Master")
MasterShortCut = Class(name="MasterShortCut")
DatadiagramMLXForm_MasterShortCut = Class(name="DatadiagramMLXForm_MasterShortCut")
DatadiagramMLXForm_Connect = Class(name="DatadiagramMLXForm_Connect")
ConnectsCollection = Class(name="ConnectsCollection")
DatadiagramMLXForm_ShapesCollection = Class(name="DatadiagramMLXForm_ShapesCollection")
DatadiagramMLXForm_ConnectsCollection = Class(name="DatadiagramMLXForm_ConnectsCollection")
Connect = Class(name="Connect")
DatadiagramMLXForm_MasterElt = Class(name="DatadiagramMLXForm_MasterElt", is_abstract=True)
DatadiagramMLXForm_PagesCollection = Class(name="DatadiagramMLXForm_PagesCollection")
DatadiagramMLXForm_Page = Class(name="DatadiagramMLXForm_Page")
DatadiagramMLXForm_PageElt = Class(name="DatadiagramMLXForm_PageElt", is_abstract=True)
DatadiagramMLXForm_WindowsInfo = Class(name="DatadiagramMLXForm_WindowsInfo")
DatadiagramMLXForm_EventList = Class(name="DatadiagramMLXForm_EventList")
DatadiagramMLXForm_HeaderFooter = Class(name="DatadiagramMLXForm_HeaderFooter")
DatadiagramMLXForm_SolutionXML = Class(name="DatadiagramMLXForm_SolutionXML")

# DatadiagramMLXForm_DateTimeType class attributes and methods
DatadiagramMLXForm_DateTimeType_hour: Property = Property(name="hour", type=StringType)
DatadiagramMLXForm_DateTimeType_minute: Property = Property(name="minute", type=StringType)
DatadiagramMLXForm_DateTimeType_year: Property = Property(name="year", type=StringType)
DatadiagramMLXForm_DateTimeType_month: Property = Property(name="month", type=StringType)
DatadiagramMLXForm_DateTimeType_day: Property = Property(name="day", type=StringType)
DatadiagramMLXForm_DateTimeType_second: Property = Property(name="second", type=StringType)
DatadiagramMLXForm_DateTimeType.attributes={DatadiagramMLXForm_DateTimeType_second, DatadiagramMLXForm_DateTimeType_minute, DatadiagramMLXForm_DateTimeType_year, DatadiagramMLXForm_DateTimeType_day, DatadiagramMLXForm_DateTimeType_month, DatadiagramMLXForm_DateTimeType_hour}

# DocumentSettingsElt class attributes and methods

# ColorsTable class attributes and methods

# DatadiagramMLXForm_CellType class attributes and methods
DatadiagramMLXForm_CellType_unit: Property = Property(name="unit", type=StringType)
DatadiagramMLXForm_CellType_formula: Property = Property(name="formula", type=StringType)
DatadiagramMLXForm_CellType_err: Property = Property(name="err", type=StringType)
DatadiagramMLXForm_CellType_value: Property = Property(name="value", type=StringType)
DatadiagramMLXForm_CellType.attributes={DatadiagramMLXForm_CellType_value, DatadiagramMLXForm_CellType_err, DatadiagramMLXForm_CellType_formula, DatadiagramMLXForm_CellType_unit}

# PrintSetup class attributes and methods

# FontsTable class attributes and methods

# FaceNamesTable class attributes and methods

# DatadiagramMLXForm_VisioDocument class attributes and methods
DatadiagramMLXForm_VisioDocument_start: Property = Property(name="start", type=StringType)
DatadiagramMLXForm_VisioDocument_key: Property = Property(name="key", type=StringType)
DatadiagramMLXForm_VisioDocument_metric: Property = Property(name="metric", type=StringType)
DatadiagramMLXForm_VisioDocument_buildnum: Property = Property(name="buildnum", type=StringType)
DatadiagramMLXForm_VisioDocument_version: Property = Property(name="version", type=StringType)
DatadiagramMLXForm_VisioDocument_docLangId: Property = Property(name="docLangId", type=StringType)
DatadiagramMLXForm_VisioDocument.attributes={DatadiagramMLXForm_VisioDocument_docLangId, DatadiagramMLXForm_VisioDocument_metric, DatadiagramMLXForm_VisioDocument_start, DatadiagramMLXForm_VisioDocument_version, DatadiagramMLXForm_VisioDocument_key, DatadiagramMLXForm_VisioDocument_buildnum}

# DocumentPropertiesCollection class attributes and methods

# EmailRoutingData class attributes and methods

# SolutionXML class attributes and methods

# DatadiagramMLXForm_DocumentPropertiesCollection class attributes and methods
DatadiagramMLXForm_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_creator: Property = Property(name="creator", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_hyperlinkBase_href: Property = Property(name="hyperlinkBase_href", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_alternateNames: Property = Property(name="alternateNames", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_template: Property = Property(name="template", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_buildNumberCreated: Property = Property(name="buildNumberCreated", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection_buildNumberEdited: Property = Property(name="buildNumberEdited", type=StringType)
DatadiagramMLXForm_DocumentPropertiesCollection.attributes={DatadiagramMLXForm_DocumentPropertiesCollection_title, DatadiagramMLXForm_DocumentPropertiesCollection_hyperlinkBase_href, DatadiagramMLXForm_DocumentPropertiesCollection_alternateNames, DatadiagramMLXForm_DocumentPropertiesCollection_buildNumberCreated, DatadiagramMLXForm_DocumentPropertiesCollection_company, DatadiagramMLXForm_DocumentPropertiesCollection_manager, DatadiagramMLXForm_DocumentPropertiesCollection_buildNumberEdited, DatadiagramMLXForm_DocumentPropertiesCollection_creator, DatadiagramMLXForm_DocumentPropertiesCollection_subject, DatadiagramMLXForm_DocumentPropertiesCollection_category, DatadiagramMLXForm_DocumentPropertiesCollection_description, DatadiagramMLXForm_DocumentPropertiesCollection_template, DatadiagramMLXForm_DocumentPropertiesCollection_keywords}

# VisioDocument class attributes and methods

# StyleSheetsCollection class attributes and methods

# DocumentSheet class attributes and methods

# MastersCollection class attributes and methods

# PagesCollection class attributes and methods

# WindowsInfo class attributes and methods

# EventList class attributes and methods

# HeaderFooter class attributes and methods

# VBProjectData class attributes and methods

# DatadiagramMLXForm_CustomPropertiesCollection class attributes and methods

# CustomProperty class attributes and methods

# DatadiagramMLXForm_CustomProperty class attributes and methods
DatadiagramMLXForm_CustomProperty_name: Property = Property(name="name", type=StringType)
DatadiagramMLXForm_CustomProperty_dataType: Property = Property(name="dataType", type=StringType)
DatadiagramMLXForm_CustomProperty.attributes={DatadiagramMLXForm_CustomProperty_dataType, DatadiagramMLXForm_CustomProperty_name}

# DatadiagramMLXForm_DocumentSettingsElt class attributes and methods
DatadiagramMLXForm_DocumentSettingsElt_dynamicGridEnabled: Property = Property(name="dynamicGridEnabled", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_protectStyles: Property = Property(name="protectStyles", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_protectShapes: Property = Property(name="protectShapes", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_protectMasters: Property = Property(name="protectMasters", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_protectBkgnds: Property = Property(name="protectBkgnds", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_customMenusFile: Property = Property(name="customMenusFile", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_customToolbarsFile: Property = Property(name="customToolbarsFile", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_attachedToolbars: Property = Property(name="attachedToolbars", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_glueSettings: Property = Property(name="glueSettings", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_snapSettings: Property = Property(name="snapSettings", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt_snapExtensions: Property = Property(name="snapExtensions", type=StringType)
DatadiagramMLXForm_DocumentSettingsElt.attributes={DatadiagramMLXForm_DocumentSettingsElt_protectShapes, DatadiagramMLXForm_DocumentSettingsElt_protectStyles, DatadiagramMLXForm_DocumentSettingsElt_attachedToolbars, DatadiagramMLXForm_DocumentSettingsElt_snapExtensions, DatadiagramMLXForm_DocumentSettingsElt_glueSettings, DatadiagramMLXForm_DocumentSettingsElt_dynamicGridEnabled, DatadiagramMLXForm_DocumentSettingsElt_customToolbarsFile, DatadiagramMLXForm_DocumentSettingsElt_customMenusFile, DatadiagramMLXForm_DocumentSettingsElt_protectBkgnds, DatadiagramMLXForm_DocumentSettingsElt_protectMasters, DatadiagramMLXForm_DocumentSettingsElt_snapSettings}

# CustomPropertiesCollection class attributes and methods

# DateTimeType class attributes and methods

# DatadiagramMLXForm_SnapAnglesCollection class attributes and methods

# SnapAngle class attributes and methods

# DatadiagramMLXForm_SnapAngle class attributes and methods
DatadiagramMLXForm_SnapAngle_angleValue: Property = Property(name="angleValue", type=StringType)
DatadiagramMLXForm_SnapAngle.attributes={DatadiagramMLXForm_SnapAngle_angleValue}

# Page class attributes and methods

# DatadiagramMLXForm_ColorsTable class attributes and methods

# StyleSheet class attributes and methods

# ColorEntry class attributes and methods

# DatadiagramMLXForm_ColorEntry class attributes and methods
DatadiagramMLXForm_ColorEntry_rgb: Property = Property(name="rgb", type=StringType)
DatadiagramMLXForm_ColorEntry.attributes={DatadiagramMLXForm_ColorEntry_rgb}

# IXrequiredElt class attributes and methods

# SnapAnglesCollection class attributes and methods

# DatadiagramMLXForm_PrintSetup class attributes and methods

# DatadiagramMLXForm_FontsTable class attributes and methods

# FontEntry class attributes and methods

# DatadiagramMLXForm_FontEntry class attributes and methods
DatadiagramMLXForm_FontEntry_name: Property = Property(name="name", type=StringType)
DatadiagramMLXForm_FontEntry_charSet: Property = Property(name="charSet", type=StringType)
DatadiagramMLXForm_FontEntry_pitchAndFamily: Property = Property(name="pitchAndFamily", type=StringType)
DatadiagramMLXForm_FontEntry_attributes: Property = Property(name="attributes", type=StringType)
DatadiagramMLXForm_FontEntry_weight: Property = Property(name="weight", type=StringType)
DatadiagramMLXForm_FontEntry_unicode: Property = Property(name="unicode", type=StringType)
DatadiagramMLXForm_FontEntry.attributes={DatadiagramMLXForm_FontEntry_pitchAndFamily, DatadiagramMLXForm_FontEntry_charSet, DatadiagramMLXForm_FontEntry_unicode, DatadiagramMLXForm_FontEntry_name, DatadiagramMLXForm_FontEntry_weight, DatadiagramMLXForm_FontEntry_attributes}

# IdentifiedElt class attributes and methods

# DatadiagramMLXForm_FaceName class attributes and methods
DatadiagramMLXForm_FaceName_name: Property = Property(name="name", type=StringType)
DatadiagramMLXForm_FaceName_unicodeRanges: Property = Property(name="unicodeRanges", type=StringType)
DatadiagramMLXForm_FaceName_charSet: Property = Property(name="charSet", type=StringType)
DatadiagramMLXForm_FaceName_panos: Property = Property(name="panos", type=StringType)
DatadiagramMLXForm_FaceName_flags: Property = Property(name="flags", type=StringType)
DatadiagramMLXForm_FaceName.attributes={DatadiagramMLXForm_FaceName_name, DatadiagramMLXForm_FaceName_flags, DatadiagramMLXForm_FaceName_unicodeRanges, DatadiagramMLXForm_FaceName_panos, DatadiagramMLXForm_FaceName_charSet}

# DatadiagramMLXForm_VBProjectData class attributes and methods
DatadiagramMLXForm_VBProjectData_data: Property = Property(name="data", type=StringType)
DatadiagramMLXForm_VBProjectData.attributes={DatadiagramMLXForm_VBProjectData_data}

# DatadiagramMLXForm_EmailRoutingData class attributes and methods
DatadiagramMLXForm_EmailRoutingData_data: Property = Property(name="data", type=StringType)
DatadiagramMLXForm_EmailRoutingData_size: Property = Property(name="size", type=StringType)
DatadiagramMLXForm_EmailRoutingData.attributes={DatadiagramMLXForm_EmailRoutingData_data, DatadiagramMLXForm_EmailRoutingData_size}

# DatadiagramMLXForm_StyleSheetsCollection class attributes and methods

# DatadiagramMLXForm_FaceNamesTable class attributes and methods

# FaceName class attributes and methods

# DatadiagramMLXForm_StyleSheet class attributes and methods

# Shape class attributes and methods

# NamedElt class attributes and methods

# DatadiagramMLXForm_DocumentSheet class attributes and methods

# PageSheet class attributes and methods

# DatadiagramMLXForm_UniqueIdElt class attributes and methods
DatadiagramMLXForm_UniqueIdElt_UniqueID: Property = Property(name="UniqueID", type=StringType)
DatadiagramMLXForm_UniqueIdElt.attributes={DatadiagramMLXForm_UniqueIdElt_UniqueID}

# DatadiagramMLXForm_Shape class attributes and methods
DatadiagramMLXForm_Shape_lineStyle: Property = Property(name="lineStyle", type=StringType)
DatadiagramMLXForm_Shape_fillStyle: Property = Property(name="fillStyle", type=StringType)
DatadiagramMLXForm_Shape_textStyle: Property = Property(name="textStyle", type=StringType)
DatadiagramMLXForm_Shape.attributes={DatadiagramMLXForm_Shape_textStyle, DatadiagramMLXForm_Shape_lineStyle, DatadiagramMLXForm_Shape_fillStyle}

# ShapesCollection class attributes and methods

# ShapeElt class attributes and methods

# DatadiagramMLXForm_ShapeElt class attributes and methods

# DatadiagramMLXForm_IXElt class attributes and methods
DatadiagramMLXForm_IXElt_iX: Property = Property(name="iX", type=StringType)
DatadiagramMLXForm_IXElt.attributes={DatadiagramMLXForm_IXElt_iX}

# DatadiagramMLXForm_DelElt class attributes and methods
DatadiagramMLXForm_DelElt_del_: Property = Property(name="del_", type=StringType)
DatadiagramMLXForm_DelElt.attributes={DatadiagramMLXForm_DelElt_del_}

# DatadiagramMLXForm_Geom class attributes and methods

# IXElt class attributes and methods

# DelElt class attributes and methods

# DatadiagramMLXForm_PageSheet class attributes and methods

# UniqueIdElt class attributes and methods

# MasterElt class attributes and methods

# PageElt class attributes and methods

# DatadiagramMLXForm_NamedElt class attributes and methods
DatadiagramMLXForm_NamedElt_name: Property = Property(name="name", type=StringType)
DatadiagramMLXForm_NamedElt_nameU: Property = Property(name="nameU", type=StringType)
DatadiagramMLXForm_NamedElt.attributes={DatadiagramMLXForm_NamedElt_nameU, DatadiagramMLXForm_NamedElt_name}

# DatadiagramMLXForm_IdentifiedElt class attributes and methods
DatadiagramMLXForm_IdentifiedElt_ID: Property = Property(name="ID", type=StringType)
DatadiagramMLXForm_IdentifiedElt.attributes={DatadiagramMLXForm_IdentifiedElt_ID}

# LineTo class attributes and methods

# MoveTo class attributes and methods

# ArcTo class attributes and methods

# SplineKnot class attributes and methods

# PolylineTo class attributes and methods

# InfiniteLine class attributes and methods

# Ellipse class attributes and methods

# EllipticalArcTo class attributes and methods

# SplineStart class attributes and methods

# NURBSTo class attributes and methods

# CellType class attributes and methods

# DatadiagramMLXForm_MoveTo class attributes and methods

# DatadiagramMLXForm_XYAElt class attributes and methods

# DatadiagramMLXForm_ArcTo class attributes and methods

# XYAElt class attributes and methods

# DatadiagramMLXForm_SplineKnot class attributes and methods

# DatadiagramMLXForm_PolylineTo class attributes and methods

# DatadiagramMLXForm_XYABElt class attributes and methods

# DatadiagramMLXForm_InfiniteLine class attributes and methods

# XYABElt class attributes and methods

# DatadiagramMLXForm_XYElt class attributes and methods

# DatadiagramMLXForm_LineTo class attributes and methods

# XYElt class attributes and methods

# Geom class attributes and methods

# DatadiagramMLXForm_TextElt class attributes and methods

# Text class attributes and methods

# DatadiagramMLXForm_IXrequiredElt class attributes and methods
DatadiagramMLXForm_IXrequiredElt_iX: Property = Property(name="iX", type=StringType)
DatadiagramMLXForm_IXrequiredElt.attributes={DatadiagramMLXForm_IXrequiredElt_iX}

# DatadiagramMLXForm_Cp class attributes and methods

# DatadiagramMLXForm_Pp class attributes and methods

# DatadiagramMLXForm_XYABCDElt class attributes and methods

# DatadiagramMLXForm_Ellipse class attributes and methods

# XYABCDElt class attributes and methods

# DatadiagramMLXForm_EllipticalArcTo class attributes and methods

# DatadiagramMLXForm_SplineStart class attributes and methods

# DatadiagramMLXForm_XYABCDEElt class attributes and methods

# DatadiagramMLXForm_NURBSTo class attributes and methods

# XYABCDEElt class attributes and methods

# DatadiagramMLXForm_Text class attributes and methods

# TextElt class attributes and methods

# DatadiagramMLXForm_Tp class attributes and methods

# DatadiagramMLXForm_Fld class attributes and methods

# DatadiagramMLXForm_StringElt class attributes and methods
DatadiagramMLXForm_StringElt_value: Property = Property(name="value", type=StringType)
DatadiagramMLXForm_StringElt.attributes={DatadiagramMLXForm_StringElt_value}

# DatadiagramMLXForm_Char class attributes and methods

# DatadiagramMLXForm_Para class attributes and methods

# DatadiagramMLXForm_TabsCollection class attributes and methods

# Tab class attributes and methods

# DatadiagramMLXForm_Tab class attributes and methods

# TabsCollection class attributes and methods

# DatadiagramMLXForm_Field class attributes and methods

# DatadiagramMLXForm_MastersCollection class attributes and methods

# DatadiagramMLXForm_XForm class attributes and methods

# Icon class attributes and methods

# DatadiagramMLXForm_Icon class attributes and methods
DatadiagramMLXForm_Icon_value: Property = Property(name="value", type=StringType)
DatadiagramMLXForm_Icon.attributes={DatadiagramMLXForm_Icon_value}

# Master class attributes and methods

# DatadiagramMLXForm_Master class attributes and methods
DatadiagramMLXForm_Master_baseID: Property = Property(name="baseID", type=StringType)
DatadiagramMLXForm_Master_matchByName: Property = Property(name="matchByName", type=StringType)
DatadiagramMLXForm_Master_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLXForm_Master_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLXForm_Master_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLXForm_Master_hidden: Property = Property(name="hidden", type=StringType)
DatadiagramMLXForm_Master_iconUpdate: Property = Property(name="iconUpdate", type=StringType)
DatadiagramMLXForm_Master_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLXForm_Master.attributes={DatadiagramMLXForm_Master_patternFlags, DatadiagramMLXForm_Master_matchByName, DatadiagramMLXForm_Master_baseID, DatadiagramMLXForm_Master_iconUpdate, DatadiagramMLXForm_Master_iconSize, DatadiagramMLXForm_Master_alignName, DatadiagramMLXForm_Master_hidden, DatadiagramMLXForm_Master_prompt}

# MasterShortCut class attributes and methods

# DatadiagramMLXForm_MasterShortCut class attributes and methods
DatadiagramMLXForm_MasterShortCut_iconSize: Property = Property(name="iconSize", type=StringType)
DatadiagramMLXForm_MasterShortCut_patternFlags: Property = Property(name="patternFlags", type=StringType)
DatadiagramMLXForm_MasterShortCut_prompt: Property = Property(name="prompt", type=StringType)
DatadiagramMLXForm_MasterShortCut_shortcutURL: Property = Property(name="shortcutURL", type=StringType)
DatadiagramMLXForm_MasterShortCut_shortcutHelp: Property = Property(name="shortcutHelp", type=StringType)
DatadiagramMLXForm_MasterShortCut_alignName: Property = Property(name="alignName", type=StringType)
DatadiagramMLXForm_MasterShortCut.attributes={DatadiagramMLXForm_MasterShortCut_shortcutHelp, DatadiagramMLXForm_MasterShortCut_patternFlags, DatadiagramMLXForm_MasterShortCut_alignName, DatadiagramMLXForm_MasterShortCut_prompt, DatadiagramMLXForm_MasterShortCut_iconSize, DatadiagramMLXForm_MasterShortCut_shortcutURL}

# DatadiagramMLXForm_Connect class attributes and methods
DatadiagramMLXForm_Connect_fromSheet: Property = Property(name="fromSheet", type=StringType)
DatadiagramMLXForm_Connect_toSheet: Property = Property(name="toSheet", type=StringType)
DatadiagramMLXForm_Connect_fromCell: Property = Property(name="fromCell", type=StringType)
DatadiagramMLXForm_Connect_toCell: Property = Property(name="toCell", type=StringType)
DatadiagramMLXForm_Connect_fromPart: Property = Property(name="fromPart", type=StringType)
DatadiagramMLXForm_Connect_toPart: Property = Property(name="toPart", type=StringType)
DatadiagramMLXForm_Connect.attributes={DatadiagramMLXForm_Connect_fromPart, DatadiagramMLXForm_Connect_toPart, DatadiagramMLXForm_Connect_fromSheet, DatadiagramMLXForm_Connect_toSheet, DatadiagramMLXForm_Connect_fromCell, DatadiagramMLXForm_Connect_toCell}

# ConnectsCollection class attributes and methods

# DatadiagramMLXForm_ShapesCollection class attributes and methods

# DatadiagramMLXForm_ConnectsCollection class attributes and methods

# Connect class attributes and methods

# DatadiagramMLXForm_MasterElt class attributes and methods

# DatadiagramMLXForm_PagesCollection class attributes and methods

# DatadiagramMLXForm_Page class attributes and methods
DatadiagramMLXForm_Page_background: Property = Property(name="background", type=StringType)
DatadiagramMLXForm_Page_backPage: Property = Property(name="backPage", type=StringType)
DatadiagramMLXForm_Page_viewScale: Property = Property(name="viewScale", type=StringType)
DatadiagramMLXForm_Page_viewCenterX: Property = Property(name="viewCenterX", type=StringType)
DatadiagramMLXForm_Page_ViewCenterY: Property = Property(name="ViewCenterY", type=StringType)
DatadiagramMLXForm_Page_reviewerID: Property = Property(name="reviewerID", type=StringType)
DatadiagramMLXForm_Page_associatedPage: Property = Property(name="associatedPage", type=StringType)
DatadiagramMLXForm_Page.attributes={DatadiagramMLXForm_Page_associatedPage, DatadiagramMLXForm_Page_reviewerID, DatadiagramMLXForm_Page_viewCenterX, DatadiagramMLXForm_Page_backPage, DatadiagramMLXForm_Page_ViewCenterY, DatadiagramMLXForm_Page_viewScale, DatadiagramMLXForm_Page_background}

# DatadiagramMLXForm_PageElt class attributes and methods

# DatadiagramMLXForm_WindowsInfo class attributes and methods

# DatadiagramMLXForm_EventList class attributes and methods

# DatadiagramMLXForm_HeaderFooter class attributes and methods

# DatadiagramMLXForm_SolutionXML class attributes and methods

# Relationships
docSettings1: BinaryAssociation = BinaryAssociation(
    name="docSettings1",
    ends={
        Property(name="DocumentSettingsElt", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dss_visioDocument", type=DocumentSettingsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docColors2: BinaryAssociation = BinaryAssociation(
    name="docColors2",
    ends={
        Property(name="ColorsTable", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_visioDocument", type=ColorsTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPrintSetup3: BinaryAssociation = BinaryAssociation(
    name="docPrintSetup3",
    ends={
        Property(name="PrintSetup", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument", type=PrintSetup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docFonts4: BinaryAssociation = BinaryAssociation(
    name="docFonts4",
    ends={
        Property(name="FontsTable", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fs_visioDocument", type=FontsTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docFaceNames5: BinaryAssociation = BinaryAssociation(
    name="docFaceNames5",
    ends={
        Property(name="FaceNamesTable", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fns_visioDocument", type=FaceNamesTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docProps0: BinaryAssociation = BinaryAssociation(
    name="docProps0",
    ends={
        Property(name="DocumentPropertiesCollection", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dps_visioDocument", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docEmailRoutingData15: BinaryAssociation = BinaryAssociation(
    name="docEmailRoutingData15",
    ends={
        Property(name="EmailRoutingData", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="erd_visioDocument", type=EmailRoutingData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docSolutionXML16: BinaryAssociation = BinaryAssociation(
    name="docSolutionXML16",
    ends={
        Property(name="SolutionXML", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sx_visioDocument", type=SolutionXML, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dps_visioDocument17: BinaryAssociation = BinaryAssociation(
    name="dps_visioDocument17",
    ends={
        Property(name="VisioDocument", type=DatadiagramMLXForm_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docProps", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
docStyleSheets6: BinaryAssociation = BinaryAssociation(
    name="docStyleSheets6",
    ends={
        Property(name="StyleSheetsCollection", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sss_visioDocument", type=StyleSheetsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docDocumentSheet7: BinaryAssociation = BinaryAssociation(
    name="docDocumentSheet7",
    ends={
        Property(name="DocumentSheet", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ds_visioDocument", type=DocumentSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docMasters8: BinaryAssociation = BinaryAssociation(
    name="docMasters8",
    ends={
        Property(name="MastersCollection", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ms_visioDocument", type=MastersCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPages9: BinaryAssociation = BinaryAssociation(
    name="docPages9",
    ends={
        Property(name="PagesCollection", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_visioDocument10", type=PagesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docWindows11: BinaryAssociation = BinaryAssociation(
    name="docWindows11",
    ends={
        Property(name="WindowsInfo", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_visioDocument", type=WindowsInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docEventList12: BinaryAssociation = BinaryAssociation(
    name="docEventList12",
    ends={
        Property(name="EventList", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="el_visioDocument", type=EventList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docHeaderFooter13: BinaryAssociation = BinaryAssociation(
    name="docHeaderFooter13",
    ends={
        Property(name="HeaderFooter", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="ef_visioDocument", type=HeaderFooter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docVBProjectData14: BinaryAssociation = BinaryAssociation(
    name="docVBProjectData14",
    ends={
        Property(name="VBProjectData", type=DatadiagramMLXForm_VisioDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="vpd_visioDocument", type=VBProjectData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timePrinted26: BinaryAssociation = BinaryAssociation(
    name="timePrinted26",
    ends={
        Property(name="DateTimeType28", type=DatadiagramMLXForm_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentPropertiesCollection27", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cps_docProp29: BinaryAssociation = BinaryAssociation(
    name="cps_docProp29",
    ends={
        Property(name="DocumentPropertiesCollection30", type=DatadiagramMLXForm_CustomPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customProps", type=DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
cps_customProps31: BinaryAssociation = BinaryAssociation(
    name="cps_customProps31",
    ends={
        Property(name="CustomProperty", type=DatadiagramMLXForm_CustomPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cp_customProps", type=CustomProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cp_customProps32: BinaryAssociation = BinaryAssociation(
    name="cp_customProps32",
    ends={
        Property(name="CustomPropertiesCollection33", type=DatadiagramMLXForm_CustomProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="cps_customProps", type=CustomPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
customProps18: BinaryAssociation = BinaryAssociation(
    name="customProps18",
    ends={
        Property(name="CustomPropertiesCollection", type=DatadiagramMLXForm_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cps_docProp", type=CustomPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeCreated19: BinaryAssociation = BinaryAssociation(
    name="timeCreated19",
    ends={
        Property(name="DateTimeType", type=DatadiagramMLXForm_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentPropertiesCollection", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSaved20: BinaryAssociation = BinaryAssociation(
    name="timeSaved20",
    ends={
        Property(name="DateTimeType22", type=DatadiagramMLXForm_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentPropertiesCollection21", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeEdited23: BinaryAssociation = BinaryAssociation(
    name="timeEdited23",
    ends={
        Property(name="DateTimeType25", type=DatadiagramMLXForm_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentPropertiesCollection24", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ds_snapAngles48: BinaryAssociation = BinaryAssociation(
    name="ds_snapAngles48",
    ends={
        Property(name="sa_docSettings", type=SnapAnglesCollection, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="SnapAnglesCollection", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1))
    }
)
sa_docSettings49: BinaryAssociation = BinaryAssociation(
    name="sa_docSettings49",
    ends={
        Property(name="DocumentSettingsElt50", type=DatadiagramMLXForm_SnapAnglesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ds_snapAngles", type=DocumentSettingsElt, multiplicity=Multiplicity(1, 1))
    }
)
snapAngles51: BinaryAssociation = BinaryAssociation(
    name="snapAngles51",
    ends={
        Property(name="SnapAngle", type=DatadiagramMLXForm_SnapAnglesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="sa_snapAngles", type=SnapAngle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sa_snapAngles52: BinaryAssociation = BinaryAssociation(
    name="sa_snapAngles52",
    ends={
        Property(name="SnapAnglesCollection53", type=DatadiagramMLXForm_SnapAngle, multiplicity=Multiplicity(1, 1)),
        Property(name="snapAngles", type=SnapAnglesCollection, multiplicity=Multiplicity(1, 1))
    }
)
dss_visioDocument34: BinaryAssociation = BinaryAssociation(
    name="dss_visioDocument34",
    ends={
        Property(name="VisioDocument35", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="docSettings", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
topPage36: BinaryAssociation = BinaryAssociation(
    name="topPage36",
    ends={
        Property(name="Page", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentSettingsElt", type=Page, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultTextStyle37: BinaryAssociation = BinaryAssociation(
    name="defaultTextStyle37",
    ends={
        Property(name="StyleSheet", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentSettingsElt38", type=StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultLineStyle39: BinaryAssociation = BinaryAssociation(
    name="defaultLineStyle39",
    ends={
        Property(name="StyleSheet41", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentSettingsElt40", type=StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cs_visioDocument54: BinaryAssociation = BinaryAssociation(
    name="cs_visioDocument54",
    ends={
        Property(name="VisioDocument55", type=DatadiagramMLXForm_ColorsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docColors", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
defaultFillStyle42: BinaryAssociation = BinaryAssociation(
    name="defaultFillStyle42",
    ends={
        Property(name="StyleSheet44", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentSettingsElt43", type=StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultGuideStyle45: BinaryAssociation = BinaryAssociation(
    name="defaultGuideStyle45",
    ends={
        Property(name="StyleSheet47", type=DatadiagramMLXForm_DocumentSettingsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_DocumentSettingsElt46", type=StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorEntries56: BinaryAssociation = BinaryAssociation(
    name="colorEntries56",
    ends={
        Property(name="ColorEntry", type=DatadiagramMLXForm_ColorsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ce_colors", type=ColorEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce_colors57: BinaryAssociation = BinaryAssociation(
    name="ce_colors57",
    ends={
        Property(name="ColorsTable58", type=DatadiagramMLXForm_ColorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="colorEntries", type=ColorsTable, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument59: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument59",
    ends={
        Property(name="VisioDocument60", type=DatadiagramMLXForm_PrintSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="docPrintSetup", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
fs_visioDocument61: BinaryAssociation = BinaryAssociation(
    name="fs_visioDocument61",
    ends={
        Property(name="VisioDocument62", type=DatadiagramMLXForm_FontsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docFonts", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
fontEntries63: BinaryAssociation = BinaryAssociation(
    name="fontEntries63",
    ends={
        Property(name="FontEntry", type=DatadiagramMLXForm_FontsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="fe_fonts", type=FontEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fe_fonts64: BinaryAssociation = BinaryAssociation(
    name="fe_fonts64",
    ends={
        Property(name="FontsTable65", type=DatadiagramMLXForm_FontEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="fontEntries", type=FontsTable, multiplicity=Multiplicity(1, 1))
    }
)
fn_faceNames69: BinaryAssociation = BinaryAssociation(
    name="fn_faceNames69",
    ends={
        Property(name="FaceNamesTable70", type=DatadiagramMLXForm_FaceName, multiplicity=Multiplicity(1, 1)),
        Property(name="faceNameEntries", type=FaceNamesTable, multiplicity=Multiplicity(1, 1))
    }
)
vpd_visioDocument71: BinaryAssociation = BinaryAssociation(
    name="vpd_visioDocument71",
    ends={
        Property(name="VisioDocument72", type=DatadiagramMLXForm_VBProjectData, multiplicity=Multiplicity(1, 1)),
        Property(name="docVBProjectData", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
erd_visioDocument73: BinaryAssociation = BinaryAssociation(
    name="erd_visioDocument73",
    ends={
        Property(name="VisioDocument74", type=DatadiagramMLXForm_EmailRoutingData, multiplicity=Multiplicity(1, 1)),
        Property(name="docEmailRoutingData", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
sss_visioDocument75: BinaryAssociation = BinaryAssociation(
    name="sss_visioDocument75",
    ends={
        Property(name="VisioDocument76", type=DatadiagramMLXForm_StyleSheetsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docStyleSheets", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
fns_visioDocument66: BinaryAssociation = BinaryAssociation(
    name="fns_visioDocument66",
    ends={
        Property(name="VisioDocument67", type=DatadiagramMLXForm_FaceNamesTable, multiplicity=Multiplicity(1, 1)),
        Property(name="docFaceNames", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
faceNameEntries68: BinaryAssociation = BinaryAssociation(
    name="faceNameEntries68",
    ends={
        Property(name="FaceName", type=DatadiagramMLXForm_FaceNamesTable, multiplicity=Multiplicity(1, 1)),
        Property(name="fn_faceNames", type=FaceName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds_visioDocument81: BinaryAssociation = BinaryAssociation(
    name="ds_visioDocument81",
    ends={
        Property(name="VisioDocument82", type=DatadiagramMLXForm_DocumentSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="docDocumentSheet", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
stylesSheets77: BinaryAssociation = BinaryAssociation(
    name="stylesSheets77",
    ends={
        Property(name="StyleSheet78", type=DatadiagramMLXForm_StyleSheetsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_stylesSheets", type=StyleSheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ss_stylesSheets79: BinaryAssociation = BinaryAssociation(
    name="ss_stylesSheets79",
    ends={
        Property(name="StyleSheetsCollection80", type=DatadiagramMLXForm_StyleSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesSheets", type=StyleSheetsCollection, multiplicity=Multiplicity(1, 1))
    }
)
ss_shapes83: BinaryAssociation = BinaryAssociation(
    name="ss_shapes83",
    ends={
        Property(name="ShapesCollection", type=DatadiagramMLXForm_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="shapes", type=ShapesCollection, multiplicity=Multiplicity(1, 1))
    }
)
shapeElts84: BinaryAssociation = BinaryAssociation(
    name="shapeElts84",
    ends={
        Property(name="ShapeElt", type=DatadiagramMLXForm_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="sse_shapeSheet", type=ShapeElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sse_shapeSheet85: BinaryAssociation = BinaryAssociation(
    name="sse_shapeSheet85",
    ends={
        Property(name="Shape", type=DatadiagramMLXForm_ShapeElt, multiplicity=Multiplicity(1, 1)),
        Property(name="shapeElts", type=Shape, multiplicity=Multiplicity(1, 1))
    }
)
noSnap93: BinaryAssociation = BinaryAssociation(
    name="noSnap93",
    ends={
        Property(name="DatadiagramMLXForm_Geom94", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="CellType95", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1))
    }
)
linesTo96: BinaryAssociation = BinaryAssociation(
    name="linesTo96",
    ends={
        Property(name="LineTo", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="lt_geom", type=LineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movesTo97: BinaryAssociation = BinaryAssociation(
    name="movesTo97",
    ends={
        Property(name="MoveTo", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_geom", type=MoveTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcsTo98: BinaryAssociation = BinaryAssociation(
    name="arcsTo98",
    ends={
        Property(name="ArcTo", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ac_geom", type=ArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineKnots99: BinaryAssociation = BinaryAssociation(
    name="splineKnots99",
    ends={
        Property(name="SplineKnot", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="sk_geom", type=SplineKnot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
polylinesTo100: BinaryAssociation = BinaryAssociation(
    name="polylinesTo100",
    ends={
        Property(name="PolylineTo", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="pt_geom", type=PolylineTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infiniteLines101: BinaryAssociation = BinaryAssociation(
    name="infiniteLines101",
    ends={
        Property(name="InfiniteLine", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="il_geom", type=InfiniteLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipses102: BinaryAssociation = BinaryAssociation(
    name="ellipses102",
    ends={
        Property(name="Ellipse", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="e_geom", type=Ellipse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ellipticalArcsTo103: BinaryAssociation = BinaryAssociation(
    name="ellipticalArcsTo103",
    ends={
        Property(name="EllipticalArcTo", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="eat_geom", type=EllipticalArcTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
splineStarts104: BinaryAssociation = BinaryAssociation(
    name="splineStarts104",
    ends={
        Property(name="SplineStart", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_geom", type=SplineStart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nurbsTo105: BinaryAssociation = BinaryAssociation(
    name="nurbsTo105",
    ends={
        Property(name="NURBSTo", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="nt_geom", type=NURBSTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
noFill86: BinaryAssociation = BinaryAssociation(
    name="noFill86",
    ends={
        Property(name="CellType", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Geom", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noLine87: BinaryAssociation = BinaryAssociation(
    name="noLine87",
    ends={
        Property(name="CellType89", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Geom88", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noShow90: BinaryAssociation = BinaryAssociation(
    name="noShow90",
    ends={
        Property(name="CellType92", type=DatadiagramMLXForm_Geom, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Geom91", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mt_geom112: BinaryAssociation = BinaryAssociation(
    name="mt_geom112",
    ends={
        Property(name="Geom113", type=DatadiagramMLXForm_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="movesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
a114: BinaryAssociation = BinaryAssociation(
    name="a114",
    ends={
        Property(name="CellType115", type=DatadiagramMLXForm_XYAElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYAElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ac_geom116: BinaryAssociation = BinaryAssociation(
    name="ac_geom116",
    ends={
        Property(name="Geom117", type=DatadiagramMLXForm_ArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="arcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
sk_geom118: BinaryAssociation = BinaryAssociation(
    name="sk_geom118",
    ends={
        Property(name="Geom119", type=DatadiagramMLXForm_SplineKnot, multiplicity=Multiplicity(1, 1)),
        Property(name="splineKnots", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
pt_geom120: BinaryAssociation = BinaryAssociation(
    name="pt_geom120",
    ends={
        Property(name="Geom121", type=DatadiagramMLXForm_PolylineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="polylinesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
b122: BinaryAssociation = BinaryAssociation(
    name="b122",
    ends={
        Property(name="CellType123", type=DatadiagramMLXForm_XYABElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYABElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
x106: BinaryAssociation = BinaryAssociation(
    name="x106",
    ends={
        Property(name="CellType107", type=DatadiagramMLXForm_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
y108: BinaryAssociation = BinaryAssociation(
    name="y108",
    ends={
        Property(name="CellType110", type=DatadiagramMLXForm_XYElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYElt109", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lt_geom111: BinaryAssociation = BinaryAssociation(
    name="lt_geom111",
    ends={
        Property(name="Geom", type=DatadiagramMLXForm_LineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="linesTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
te_text142: BinaryAssociation = BinaryAssociation(
    name="te_text142",
    ends={
        Property(name="Text", type=DatadiagramMLXForm_TextElt, multiplicity=Multiplicity(1, 1)),
        Property(name="textElts", type=Text, multiplicity=Multiplicity(1, 1))
    }
)
il_geom124: BinaryAssociation = BinaryAssociation(
    name="il_geom124",
    ends={
        Property(name="Geom125", type=DatadiagramMLXForm_InfiniteLine, multiplicity=Multiplicity(1, 1)),
        Property(name="infiniteLines", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
c126: BinaryAssociation = BinaryAssociation(
    name="c126",
    ends={
        Property(name="CellType127", type=DatadiagramMLXForm_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYABCDElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d128: BinaryAssociation = BinaryAssociation(
    name="d128",
    ends={
        Property(name="CellType130", type=DatadiagramMLXForm_XYABCDElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYABCDElt129", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e_geom131: BinaryAssociation = BinaryAssociation(
    name="e_geom131",
    ends={
        Property(name="Geom132", type=DatadiagramMLXForm_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipses", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
eat_geom133: BinaryAssociation = BinaryAssociation(
    name="eat_geom133",
    ends={
        Property(name="Geom134", type=DatadiagramMLXForm_EllipticalArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ellipticalArcsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
ss_geom135: BinaryAssociation = BinaryAssociation(
    name="ss_geom135",
    ends={
        Property(name="Geom136", type=DatadiagramMLXForm_SplineStart, multiplicity=Multiplicity(1, 1)),
        Property(name="splineStarts", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
e137: BinaryAssociation = BinaryAssociation(
    name="e137",
    ends={
        Property(name="CellType138", type=DatadiagramMLXForm_XYABCDEElt, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XYABCDEElt", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nt_geom139: BinaryAssociation = BinaryAssociation(
    name="nt_geom139",
    ends={
        Property(name="Geom140", type=DatadiagramMLXForm_NURBSTo, multiplicity=Multiplicity(1, 1)),
        Property(name="nurbsTo", type=Geom, multiplicity=Multiplicity(1, 1))
    }
)
textElts141: BinaryAssociation = BinaryAssociation(
    name="textElts141",
    ends={
        Property(name="TextElt", type=DatadiagramMLXForm_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="te_text", type=TextElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strikethru169: BinaryAssociation = BinaryAssociation(
    name="strikethru169",
    ends={
        Property(name="CellType171", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char170", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doubleStrikethrough172: BinaryAssociation = BinaryAssociation(
    name="doubleStrikethrough172",
    ends={
        Property(name="CellType174", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char173", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rtlText175: BinaryAssociation = BinaryAssociation(
    name="rtlText175",
    ends={
        Property(name="CellType177", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char176", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
runVertical178: BinaryAssociation = BinaryAssociation(
    name="runVertical178",
    ends={
        Property(name="CellType180", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char179", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font143: BinaryAssociation = BinaryAssociation(
    name="font143",
    ends={
        Property(name="CellType144", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color145: BinaryAssociation = BinaryAssociation(
    name="color145",
    ends={
        Property(name="CellType147", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char146", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style148: BinaryAssociation = BinaryAssociation(
    name="style148",
    ends={
        Property(name="CellType150", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char149", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case151: BinaryAssociation = BinaryAssociation(
    name="case151",
    ends={
        Property(name="CellType153", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char152", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pos154: BinaryAssociation = BinaryAssociation(
    name="pos154",
    ends={
        Property(name="CellType156", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char155", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fontScale157: BinaryAssociation = BinaryAssociation(
    name="fontScale157",
    ends={
        Property(name="CellType159", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char158", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size160: BinaryAssociation = BinaryAssociation(
    name="size160",
    ends={
        Property(name="CellType162", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char161", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dblUnderline163: BinaryAssociation = BinaryAssociation(
    name="dblUnderline163",
    ends={
        Property(name="CellType165", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char164", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overline166: BinaryAssociation = BinaryAssociation(
    name="overline166",
    ends={
        Property(name="CellType168", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char167", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indRight198: BinaryAssociation = BinaryAssociation(
    name="indRight198",
    ends={
        Property(name="CellType200", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para199", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spLine201: BinaryAssociation = BinaryAssociation(
    name="spLine201",
    ends={
        Property(name="CellType203", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para202", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letterspace181: BinaryAssociation = BinaryAssociation(
    name="letterspace181",
    ends={
        Property(name="CellType183", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char182", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorTrans184: BinaryAssociation = BinaryAssociation(
    name="colorTrans184",
    ends={
        Property(name="CellType186", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char185", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localizeFont187: BinaryAssociation = BinaryAssociation(
    name="localizeFont187",
    ends={
        Property(name="CellType189", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char188", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
langID190: BinaryAssociation = BinaryAssociation(
    name="langID190",
    ends={
        Property(name="CellType192", type=DatadiagramMLXForm_Char, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Char191", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indFirst193: BinaryAssociation = BinaryAssociation(
    name="indFirst193",
    ends={
        Property(name="CellType194", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indLeft195: BinaryAssociation = BinaryAssociation(
    name="indLeft195",
    ends={
        Property(name="CellType197", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para196", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bulletFontSize225: BinaryAssociation = BinaryAssociation(
    name="bulletFontSize225",
    ends={
        Property(name="CellType227", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para226", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textPosAfterBullet228: BinaryAssociation = BinaryAssociation(
    name="textPosAfterBullet228",
    ends={
        Property(name="CellType230", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para229", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spBefore204: BinaryAssociation = BinaryAssociation(
    name="spBefore204",
    ends={
        Property(name="CellType206", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para205", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spAfter207: BinaryAssociation = BinaryAssociation(
    name="spAfter207",
    ends={
        Property(name="CellType209", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para208", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
horzAlign210: BinaryAssociation = BinaryAssociation(
    name="horzAlign210",
    ends={
        Property(name="CellType212", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para211", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bullet213: BinaryAssociation = BinaryAssociation(
    name="bullet213",
    ends={
        Property(name="CellType215", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para214", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bulletStr216: BinaryAssociation = BinaryAssociation(
    name="bulletStr216",
    ends={
        Property(name="CellType218", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para217", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bulletFont219: BinaryAssociation = BinaryAssociation(
    name="bulletFont219",
    ends={
        Property(name="CellType221", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para220", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localizeBulletFont222: BinaryAssociation = BinaryAssociation(
    name="localizeBulletFont222",
    ends={
        Property(name="CellType224", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para223", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
format246: BinaryAssociation = BinaryAssociation(
    name="format246",
    ends={
        Property(name="CellType248", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field247", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type249: BinaryAssociation = BinaryAssociation(
    name="type249",
    ends={
        Property(name="CellType251", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field250", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiCat252: BinaryAssociation = BinaryAssociation(
    name="uiCat252",
    ends={
        Property(name="CellType254", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field253", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flags231: BinaryAssociation = BinaryAssociation(
    name="flags231",
    ends={
        Property(name="CellType233", type=DatadiagramMLXForm_Para, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Para232", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiCode255: BinaryAssociation = BinaryAssociation(
    name="uiCode255",
    ends={
        Property(name="CellType257", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field256", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiFmt258: BinaryAssociation = BinaryAssociation(
    name="uiFmt258",
    ends={
        Property(name="CellType260", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field259", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabs234: BinaryAssociation = BinaryAssociation(
    name="tabs234",
    ends={
        Property(name="Tab", type=DatadiagramMLXForm_TabsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="t_tabs", type=Tab, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calendar261: BinaryAssociation = BinaryAssociation(
    name="calendar261",
    ends={
        Property(name="CellType263", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field262", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_tabs235: BinaryAssociation = BinaryAssociation(
    name="t_tabs235",
    ends={
        Property(name="TabsCollection", type=DatadiagramMLXForm_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="tabs", type=TabsCollection, multiplicity=Multiplicity(1, 1))
    }
)
objectKind264: BinaryAssociation = BinaryAssociation(
    name="objectKind264",
    ends={
        Property(name="CellType266", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field265", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position236: BinaryAssociation = BinaryAssociation(
    name="position236",
    ends={
        Property(name="CellType237", type=DatadiagramMLXForm_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Tab", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alignment238: BinaryAssociation = BinaryAssociation(
    name="alignment238",
    ends={
        Property(name="CellType240", type=DatadiagramMLXForm_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Tab239", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value241: BinaryAssociation = BinaryAssociation(
    name="value241",
    ends={
        Property(name="CellType242", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editMode243: BinaryAssociation = BinaryAssociation(
    name="editMode243",
    ends={
        Property(name="CellType245", type=DatadiagramMLXForm_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_Field244", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locPinY281: BinaryAssociation = BinaryAssociation(
    name="locPinY281",
    ends={
        Property(name="CellType283", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm282", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle284: BinaryAssociation = BinaryAssociation(
    name="angle284",
    ends={
        Property(name="CellType286", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm285", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flipX287: BinaryAssociation = BinaryAssociation(
    name="flipX287",
    ends={
        Property(name="CellType289", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm288", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flipY290: BinaryAssociation = BinaryAssociation(
    name="flipY290",
    ends={
        Property(name="CellType292", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm291", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resizeMode293: BinaryAssociation = BinaryAssociation(
    name="resizeMode293",
    ends={
        Property(name="CellType295", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm294", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ms_visioDocument296: BinaryAssociation = BinaryAssociation(
    name="ms_visioDocument296",
    ends={
        Property(name="VisioDocument297", type=DatadiagramMLXForm_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docMasters", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
pinX267: BinaryAssociation = BinaryAssociation(
    name="pinX267",
    ends={
        Property(name="CellType268", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pinY269: BinaryAssociation = BinaryAssociation(
    name="pinY269",
    ends={
        Property(name="CellType271", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm270", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
width272: BinaryAssociation = BinaryAssociation(
    name="width272",
    ends={
        Property(name="CellType274", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm273", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
height275: BinaryAssociation = BinaryAssociation(
    name="height275",
    ends={
        Property(name="CellType277", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm276", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locPinX278: BinaryAssociation = BinaryAssociation(
    name="locPinX278",
    ends={
        Property(name="CellType280", type=DatadiagramMLXForm_XForm, multiplicity=Multiplicity(1, 1)),
        Property(name="DatadiagramMLXForm_XForm279", type=CellType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
icons302: BinaryAssociation = BinaryAssociation(
    name="icons302",
    ends={
        Property(name="Icon", type=DatadiagramMLXForm_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="i_masterShortCut", type=Icon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
masters298: BinaryAssociation = BinaryAssociation(
    name="masters298",
    ends={
        Property(name="Master", type=DatadiagramMLXForm_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masters", type=Master, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i_masterShortCut303: BinaryAssociation = BinaryAssociation(
    name="i_masterShortCut303",
    ends={
        Property(name="MasterShortCut304", type=DatadiagramMLXForm_Icon, multiplicity=Multiplicity(1, 1)),
        Property(name="icons", type=MasterShortCut, multiplicity=Multiplicity(1, 1))
    }
)
masterShortCuts299: BinaryAssociation = BinaryAssociation(
    name="masterShortCuts299",
    ends={
        Property(name="MasterShortCut", type=DatadiagramMLXForm_MastersCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="m_masterShortCuts", type=MasterShortCut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
m_masterShortCuts300: BinaryAssociation = BinaryAssociation(
    name="m_masterShortCuts300",
    ends={
        Property(name="MastersCollection301", type=DatadiagramMLXForm_MasterShortCut, multiplicity=Multiplicity(1, 1)),
        Property(name="masterShortCuts", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
m_masters305: BinaryAssociation = BinaryAssociation(
    name="m_masters305",
    ends={
        Property(name="MastersCollection306", type=DatadiagramMLXForm_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="masters", type=MastersCollection, multiplicity=Multiplicity(1, 1))
    }
)
connections310: BinaryAssociation = BinaryAssociation(
    name="connections310",
    ends={
        Property(name="Connect", type=DatadiagramMLXForm_ConnectsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_connects", type=Connect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_connects311: BinaryAssociation = BinaryAssociation(
    name="c_connects311",
    ends={
        Property(name="ConnectsCollection", type=DatadiagramMLXForm_Connect, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=ConnectsCollection, multiplicity=Multiplicity(1, 1))
    }
)
masterElts307: BinaryAssociation = BinaryAssociation(
    name="masterElts307",
    ends={
        Property(name="MasterElt", type=DatadiagramMLXForm_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="me_master", type=MasterElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shapes308: BinaryAssociation = BinaryAssociation(
    name="shapes308",
    ends={
        Property(name="Shape309", type=DatadiagramMLXForm_ShapesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ss_shapes", type=Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
me_master312: BinaryAssociation = BinaryAssociation(
    name="me_master312",
    ends={
        Property(name="Master313", type=DatadiagramMLXForm_MasterElt, multiplicity=Multiplicity(1, 1)),
        Property(name="masterElts", type=Master, multiplicity=Multiplicity(1, 1))
    }
)
ps_visioDocument314: BinaryAssociation = BinaryAssociation(
    name="ps_visioDocument314",
    ends={
        Property(name="VisioDocument315", type=DatadiagramMLXForm_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="docPages", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
pages316: BinaryAssociation = BinaryAssociation(
    name="pages316",
    ends={
        Property(name="Page317", type=DatadiagramMLXForm_PagesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="p_pages", type=Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p_pages318: BinaryAssociation = BinaryAssociation(
    name="p_pages318",
    ends={
        Property(name="PagesCollection319", type=DatadiagramMLXForm_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=PagesCollection, multiplicity=Multiplicity(1, 1))
    }
)
sx_visioDocument329: BinaryAssociation = BinaryAssociation(
    name="sx_visioDocument329",
    ends={
        Property(name="VisioDocument330", type=DatadiagramMLXForm_SolutionXML, multiplicity=Multiplicity(1, 1)),
        Property(name="docSolutionXML", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
pageElts320: BinaryAssociation = BinaryAssociation(
    name="pageElts320",
    ends={
        Property(name="PageElt", type=DatadiagramMLXForm_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pe_page", type=PageElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pe_page321: BinaryAssociation = BinaryAssociation(
    name="pe_page321",
    ends={
        Property(name="Page322", type=DatadiagramMLXForm_PageElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pageElts", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
ws_visioDocument323: BinaryAssociation = BinaryAssociation(
    name="ws_visioDocument323",
    ends={
        Property(name="VisioDocument324", type=DatadiagramMLXForm_WindowsInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="docWindows", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
el_visioDocument325: BinaryAssociation = BinaryAssociation(
    name="el_visioDocument325",
    ends={
        Property(name="VisioDocument326", type=DatadiagramMLXForm_EventList, multiplicity=Multiplicity(1, 1)),
        Property(name="docEventList", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)
ef_visioDocument327: BinaryAssociation = BinaryAssociation(
    name="ef_visioDocument327",
    ends={
        Property(name="VisioDocument328", type=DatadiagramMLXForm_HeaderFooter, multiplicity=Multiplicity(1, 1)),
        Property(name="docHeaderFooter", type=VisioDocument, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_DatadiagramMLXForm_ColorEntry_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLXForm_ColorEntry)
gen_DatadiagramMLXForm_FontEntry_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLXForm_FontEntry)
gen_DatadiagramMLXForm_FaceName_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLXForm_FaceName)
gen_DatadiagramMLXForm_DocumentSheet_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLXForm_DocumentSheet)
gen_DatadiagramMLXForm_StyleSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLXForm_StyleSheet)
gen_DatadiagramMLXForm_StyleSheet_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLXForm_StyleSheet)
gen_DatadiagramMLXForm_StyleSheet_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLXForm_StyleSheet)
gen_DatadiagramMLXForm_DocumentSheet_PageSheet = Generalization(general=PageSheet, specific=DatadiagramMLXForm_DocumentSheet)
gen_DatadiagramMLXForm_Geom_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_Geom)
gen_DatadiagramMLXForm_Geom_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_Geom)
gen_DatadiagramMLXForm_PageSheet_Shape = Generalization(general=Shape, specific=DatadiagramMLXForm_PageSheet)
gen_DatadiagramMLXForm_PageSheet_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLXForm_PageSheet)
gen_DatadiagramMLXForm_PageSheet_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLXForm_PageSheet)
gen_DatadiagramMLXForm_PageSheet_PageElt = Generalization(general=PageElt, specific=DatadiagramMLXForm_PageSheet)
gen_DatadiagramMLXForm_Geom_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_Geom)
gen_DatadiagramMLXForm_MoveTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLXForm_MoveTo)
gen_DatadiagramMLXForm_XYAElt_XYElt = Generalization(general=XYElt, specific=DatadiagramMLXForm_XYAElt)
gen_DatadiagramMLXForm_InfiniteLine_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLXForm_InfiniteLine)
gen_DatadiagramMLXForm_ArcTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLXForm_ArcTo)
gen_DatadiagramMLXForm_SplineKnot_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLXForm_SplineKnot)
gen_DatadiagramMLXForm_PolylineTo_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLXForm_PolylineTo)
gen_DatadiagramMLXForm_XYABElt_XYAElt = Generalization(general=XYAElt, specific=DatadiagramMLXForm_XYABElt)
gen_DatadiagramMLXForm_XYElt_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_XYElt)
gen_DatadiagramMLXForm_XYElt_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_XYElt)
gen_DatadiagramMLXForm_LineTo_XYElt = Generalization(general=XYElt, specific=DatadiagramMLXForm_LineTo)
gen_DatadiagramMLXForm_Cp_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLXForm_Cp)
gen_DatadiagramMLXForm_Cp_TextElt = Generalization(general=TextElt, specific=DatadiagramMLXForm_Cp)
gen_DatadiagramMLXForm_Pp_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLXForm_Pp)
gen_DatadiagramMLXForm_XYABCDElt_XYABElt = Generalization(general=XYABElt, specific=DatadiagramMLXForm_XYABCDElt)
gen_DatadiagramMLXForm_Ellipse_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLXForm_Ellipse)
gen_DatadiagramMLXForm_EllipticalArcTo_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLXForm_EllipticalArcTo)
gen_DatadiagramMLXForm_SplineStart_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLXForm_SplineStart)
gen_DatadiagramMLXForm_XYABCDEElt_XYABCDElt = Generalization(general=XYABCDElt, specific=DatadiagramMLXForm_XYABCDEElt)
gen_DatadiagramMLXForm_NURBSTo_XYABCDEElt = Generalization(general=XYABCDEElt, specific=DatadiagramMLXForm_NURBSTo)
gen_DatadiagramMLXForm_Text_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_Text)
gen_DatadiagramMLXForm_Pp_TextElt = Generalization(general=TextElt, specific=DatadiagramMLXForm_Pp)
gen_DatadiagramMLXForm_Tp_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLXForm_Tp)
gen_DatadiagramMLXForm_Tp_TextElt = Generalization(general=TextElt, specific=DatadiagramMLXForm_Tp)
gen_DatadiagramMLXForm_Fld_IXrequiredElt = Generalization(general=IXrequiredElt, specific=DatadiagramMLXForm_Fld)
gen_DatadiagramMLXForm_Fld_TextElt = Generalization(general=TextElt, specific=DatadiagramMLXForm_Fld)
gen_DatadiagramMLXForm_StringElt_TextElt = Generalization(general=TextElt, specific=DatadiagramMLXForm_StringElt)
gen_DatadiagramMLXForm_Char_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_Char)
gen_DatadiagramMLXForm_Char_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_Char)
gen_DatadiagramMLXForm_Char_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_Char)
gen_DatadiagramMLXForm_Para_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_Para)
gen_DatadiagramMLXForm_Para_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_Para)
gen_DatadiagramMLXForm_Para_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_Para)
gen_DatadiagramMLXForm_TabsCollection_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_TabsCollection)
gen_DatadiagramMLXForm_TabsCollection_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_TabsCollection)
gen_DatadiagramMLXForm_TabsCollection_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_TabsCollection)
gen_DatadiagramMLXForm_Tab_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_Tab)
gen_DatadiagramMLXForm_Field_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_Field)
gen_DatadiagramMLXForm_Field_IXElt = Generalization(general=IXElt, specific=DatadiagramMLXForm_Field)
gen_DatadiagramMLXForm_Field_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_Field)
gen_DatadiagramMLXForm_XForm_ShapeElt = Generalization(general=ShapeElt, specific=DatadiagramMLXForm_XForm)
gen_DatadiagramMLXForm_XForm_DelElt = Generalization(general=DelElt, specific=DatadiagramMLXForm_XForm)
gen_DatadiagramMLXForm_Icon_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLXForm_Icon)
gen_DatadiagramMLXForm_Master_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLXForm_Master)
gen_DatadiagramMLXForm_Master_UniqueIdElt = Generalization(general=UniqueIdElt, specific=DatadiagramMLXForm_Master)
gen_DatadiagramMLXForm_Master_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLXForm_Master)
gen_DatadiagramMLXForm_MasterShortCut_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLXForm_MasterShortCut)
gen_DatadiagramMLXForm_MasterShortCut_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLXForm_MasterShortCut)
gen_DatadiagramMLXForm_ShapesCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLXForm_ShapesCollection)
gen_DatadiagramMLXForm_ShapesCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLXForm_ShapesCollection)
gen_DatadiagramMLXForm_ConnectsCollection_MasterElt = Generalization(general=MasterElt, specific=DatadiagramMLXForm_ConnectsCollection)
gen_DatadiagramMLXForm_ConnectsCollection_PageElt = Generalization(general=PageElt, specific=DatadiagramMLXForm_ConnectsCollection)
gen_DatadiagramMLXForm_Page_IdentifiedElt = Generalization(general=IdentifiedElt, specific=DatadiagramMLXForm_Page)
gen_DatadiagramMLXForm_Page_NamedElt = Generalization(general=NamedElt, specific=DatadiagramMLXForm_Page)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={DatadiagramMLXForm_DateTimeType, DocumentSettingsElt, ColorsTable, DatadiagramMLXForm_CellType, PrintSetup, FontsTable, FaceNamesTable, DatadiagramMLXForm_VisioDocument, DocumentPropertiesCollection, EmailRoutingData, SolutionXML, DatadiagramMLXForm_DocumentPropertiesCollection, VisioDocument, StyleSheetsCollection, DocumentSheet, MastersCollection, PagesCollection, WindowsInfo, EventList, HeaderFooter, VBProjectData, DatadiagramMLXForm_CustomPropertiesCollection, CustomProperty, DatadiagramMLXForm_CustomProperty, DatadiagramMLXForm_DocumentSettingsElt, CustomPropertiesCollection, DateTimeType, DatadiagramMLXForm_SnapAnglesCollection, SnapAngle, DatadiagramMLXForm_SnapAngle, Page, DatadiagramMLXForm_ColorsTable, StyleSheet, ColorEntry, DatadiagramMLXForm_ColorEntry, IXrequiredElt, SnapAnglesCollection, DatadiagramMLXForm_PrintSetup, DatadiagramMLXForm_FontsTable, FontEntry, DatadiagramMLXForm_FontEntry, IdentifiedElt, DatadiagramMLXForm_FaceName, DatadiagramMLXForm_VBProjectData, DatadiagramMLXForm_EmailRoutingData, DatadiagramMLXForm_StyleSheetsCollection, DatadiagramMLXForm_FaceNamesTable, FaceName, DatadiagramMLXForm_StyleSheet, Shape, NamedElt, DatadiagramMLXForm_DocumentSheet, PageSheet, DatadiagramMLXForm_UniqueIdElt, DatadiagramMLXForm_Shape, ShapesCollection, ShapeElt, DatadiagramMLXForm_ShapeElt, DatadiagramMLXForm_IXElt, DatadiagramMLXForm_DelElt, DatadiagramMLXForm_Geom, IXElt, DelElt, DatadiagramMLXForm_PageSheet, UniqueIdElt, MasterElt, PageElt, DatadiagramMLXForm_NamedElt, DatadiagramMLXForm_IdentifiedElt, LineTo, MoveTo, ArcTo, SplineKnot, PolylineTo, InfiniteLine, Ellipse, EllipticalArcTo, SplineStart, NURBSTo, CellType, DatadiagramMLXForm_MoveTo, DatadiagramMLXForm_XYAElt, DatadiagramMLXForm_ArcTo, XYAElt, DatadiagramMLXForm_SplineKnot, DatadiagramMLXForm_PolylineTo, DatadiagramMLXForm_XYABElt, DatadiagramMLXForm_InfiniteLine, XYABElt, DatadiagramMLXForm_XYElt, DatadiagramMLXForm_LineTo, XYElt, Geom, DatadiagramMLXForm_TextElt, Text, DatadiagramMLXForm_IXrequiredElt, DatadiagramMLXForm_Cp, DatadiagramMLXForm_Pp, DatadiagramMLXForm_XYABCDElt, DatadiagramMLXForm_Ellipse, XYABCDElt, DatadiagramMLXForm_EllipticalArcTo, DatadiagramMLXForm_SplineStart, DatadiagramMLXForm_XYABCDEElt, DatadiagramMLXForm_NURBSTo, XYABCDEElt, DatadiagramMLXForm_Text, TextElt, DatadiagramMLXForm_Tp, DatadiagramMLXForm_Fld, DatadiagramMLXForm_StringElt, DatadiagramMLXForm_Char, DatadiagramMLXForm_Para, DatadiagramMLXForm_TabsCollection, Tab, DatadiagramMLXForm_Tab, TabsCollection, DatadiagramMLXForm_Field, DatadiagramMLXForm_MastersCollection, DatadiagramMLXForm_XForm, Icon, DatadiagramMLXForm_Icon, Master, DatadiagramMLXForm_Master, MasterShortCut, DatadiagramMLXForm_MasterShortCut, DatadiagramMLXForm_Connect, ConnectsCollection, DatadiagramMLXForm_ShapesCollection, DatadiagramMLXForm_ConnectsCollection, Connect, DatadiagramMLXForm_MasterElt, DatadiagramMLXForm_PagesCollection, DatadiagramMLXForm_Page, DatadiagramMLXForm_PageElt, DatadiagramMLXForm_WindowsInfo, DatadiagramMLXForm_EventList, DatadiagramMLXForm_HeaderFooter, DatadiagramMLXForm_SolutionXML},
    associations={docSettings1, docColors2, docPrintSetup3, docFonts4, docFaceNames5, docProps0, docEmailRoutingData15, docSolutionXML16, dps_visioDocument17, docStyleSheets6, docDocumentSheet7, docMasters8, docPages9, docWindows11, docEventList12, docHeaderFooter13, docVBProjectData14, timePrinted26, cps_docProp29, cps_customProps31, cp_customProps32, customProps18, timeCreated19, timeSaved20, timeEdited23, ds_snapAngles48, sa_docSettings49, snapAngles51, sa_snapAngles52, dss_visioDocument34, topPage36, defaultTextStyle37, defaultLineStyle39, cs_visioDocument54, defaultFillStyle42, defaultGuideStyle45, colorEntries56, ce_colors57, ps_visioDocument59, fs_visioDocument61, fontEntries63, fe_fonts64, fn_faceNames69, vpd_visioDocument71, erd_visioDocument73, sss_visioDocument75, fns_visioDocument66, faceNameEntries68, ds_visioDocument81, stylesSheets77, ss_stylesSheets79, ss_shapes83, shapeElts84, sse_shapeSheet85, noSnap93, linesTo96, movesTo97, arcsTo98, splineKnots99, polylinesTo100, infiniteLines101, ellipses102, ellipticalArcsTo103, splineStarts104, nurbsTo105, noFill86, noLine87, noShow90, mt_geom112, a114, ac_geom116, sk_geom118, pt_geom120, b122, x106, y108, lt_geom111, te_text142, il_geom124, c126, d128, e_geom131, eat_geom133, ss_geom135, e137, nt_geom139, textElts141, strikethru169, doubleStrikethrough172, rtlText175, runVertical178, font143, color145, style148, case151, pos154, fontScale157, size160, dblUnderline163, overline166, indRight198, spLine201, letterspace181, colorTrans184, localizeFont187, langID190, indFirst193, indLeft195, bulletFontSize225, textPosAfterBullet228, spBefore204, spAfter207, horzAlign210, bullet213, bulletStr216, bulletFont219, localizeBulletFont222, format246, type249, uiCat252, flags231, uiCode255, uiFmt258, tabs234, calendar261, t_tabs235, objectKind264, position236, alignment238, value241, editMode243, locPinY281, angle284, flipX287, flipY290, resizeMode293, ms_visioDocument296, pinX267, pinY269, width272, height275, locPinX278, icons302, masters298, i_masterShortCut303, masterShortCuts299, m_masterShortCuts300, m_masters305, connections310, c_connects311, masterElts307, shapes308, me_master312, ps_visioDocument314, pages316, p_pages318, sx_visioDocument329, pageElts320, pe_page321, ws_visioDocument323, el_visioDocument325, ef_visioDocument327},
    generalizations={gen_DatadiagramMLXForm_ColorEntry_IXrequiredElt, gen_DatadiagramMLXForm_FontEntry_IdentifiedElt, gen_DatadiagramMLXForm_FaceName_IdentifiedElt, gen_DatadiagramMLXForm_DocumentSheet_NamedElt, gen_DatadiagramMLXForm_StyleSheet_Shape, gen_DatadiagramMLXForm_StyleSheet_IdentifiedElt, gen_DatadiagramMLXForm_StyleSheet_NamedElt, gen_DatadiagramMLXForm_DocumentSheet_PageSheet, gen_DatadiagramMLXForm_Geom_ShapeElt, gen_DatadiagramMLXForm_Geom_IXElt, gen_DatadiagramMLXForm_PageSheet_Shape, gen_DatadiagramMLXForm_PageSheet_UniqueIdElt, gen_DatadiagramMLXForm_PageSheet_MasterElt, gen_DatadiagramMLXForm_PageSheet_PageElt, gen_DatadiagramMLXForm_Geom_DelElt, gen_DatadiagramMLXForm_MoveTo_XYElt, gen_DatadiagramMLXForm_XYAElt_XYElt, gen_DatadiagramMLXForm_InfiniteLine_XYABElt, gen_DatadiagramMLXForm_ArcTo_XYAElt, gen_DatadiagramMLXForm_SplineKnot_XYAElt, gen_DatadiagramMLXForm_PolylineTo_XYAElt, gen_DatadiagramMLXForm_XYABElt_XYAElt, gen_DatadiagramMLXForm_XYElt_IXElt, gen_DatadiagramMLXForm_XYElt_DelElt, gen_DatadiagramMLXForm_LineTo_XYElt, gen_DatadiagramMLXForm_Cp_IXrequiredElt, gen_DatadiagramMLXForm_Cp_TextElt, gen_DatadiagramMLXForm_Pp_IXrequiredElt, gen_DatadiagramMLXForm_XYABCDElt_XYABElt, gen_DatadiagramMLXForm_Ellipse_XYABCDElt, gen_DatadiagramMLXForm_EllipticalArcTo_XYABCDElt, gen_DatadiagramMLXForm_SplineStart_XYABCDElt, gen_DatadiagramMLXForm_XYABCDEElt_XYABCDElt, gen_DatadiagramMLXForm_NURBSTo_XYABCDEElt, gen_DatadiagramMLXForm_Text_ShapeElt, gen_DatadiagramMLXForm_Pp_TextElt, gen_DatadiagramMLXForm_Tp_IXrequiredElt, gen_DatadiagramMLXForm_Tp_TextElt, gen_DatadiagramMLXForm_Fld_IXrequiredElt, gen_DatadiagramMLXForm_Fld_TextElt, gen_DatadiagramMLXForm_StringElt_TextElt, gen_DatadiagramMLXForm_Char_ShapeElt, gen_DatadiagramMLXForm_Char_IXElt, gen_DatadiagramMLXForm_Char_DelElt, gen_DatadiagramMLXForm_Para_ShapeElt, gen_DatadiagramMLXForm_Para_IXElt, gen_DatadiagramMLXForm_Para_DelElt, gen_DatadiagramMLXForm_TabsCollection_ShapeElt, gen_DatadiagramMLXForm_TabsCollection_IXElt, gen_DatadiagramMLXForm_TabsCollection_DelElt, gen_DatadiagramMLXForm_Tab_IXElt, gen_DatadiagramMLXForm_Field_ShapeElt, gen_DatadiagramMLXForm_Field_IXElt, gen_DatadiagramMLXForm_Field_DelElt, gen_DatadiagramMLXForm_XForm_ShapeElt, gen_DatadiagramMLXForm_XForm_DelElt, gen_DatadiagramMLXForm_Icon_MasterElt, gen_DatadiagramMLXForm_Master_IdentifiedElt, gen_DatadiagramMLXForm_Master_UniqueIdElt, gen_DatadiagramMLXForm_Master_NamedElt, gen_DatadiagramMLXForm_MasterShortCut_IdentifiedElt, gen_DatadiagramMLXForm_MasterShortCut_NamedElt, gen_DatadiagramMLXForm_ShapesCollection_MasterElt, gen_DatadiagramMLXForm_ShapesCollection_PageElt, gen_DatadiagramMLXForm_ConnectsCollection_MasterElt, gen_DatadiagramMLXForm_ConnectsCollection_PageElt, gen_DatadiagramMLXForm_Page_IdentifiedElt, gen_DatadiagramMLXForm_Page_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)