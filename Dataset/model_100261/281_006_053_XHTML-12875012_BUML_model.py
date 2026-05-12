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

# Enumerations
Shape: Enumeration = Enumeration(
    name="Shape",
    literals={
            EnumerationLiteral(name="rect"),
			EnumerationLiteral(name="circle"),
			EnumerationLiteral(name="poly"),
			EnumerationLiteral(name="default")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="ltr"),
			EnumerationLiteral(name="rtl")
    }
)

ValueType: Enumeration = Enumeration(
    name="ValueType",
    literals={
            EnumerationLiteral(name="data"),
			EnumerationLiteral(name="ref"),
			EnumerationLiteral(name="object")
    }
)

FomeMethod: Enumeration = Enumeration(
    name="FomeMethod",
    literals={
            EnumerationLiteral(name="get"),
			EnumerationLiteral(name="post")
    }
)

InputType: Enumeration = Enumeration(
    name="InputType",
    literals={
            EnumerationLiteral(name="text"),
			EnumerationLiteral(name="password"),
			EnumerationLiteral(name="checkbox"),
			EnumerationLiteral(name="radio"),
			EnumerationLiteral(name="submit"),
			EnumerationLiteral(name="reset"),
			EnumerationLiteral(name="file"),
			EnumerationLiteral(name="hidden"),
			EnumerationLiteral(name="image"),
			EnumerationLiteral(name="button")
    }
)

ButtonType: Enumeration = Enumeration(
    name="ButtonType",
    literals={
            EnumerationLiteral(name="button"),
			EnumerationLiteral(name="submit"),
			EnumerationLiteral(name="reset")
    }
)

TFrame: Enumeration = Enumeration(
    name="TFrame",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="above"),
			EnumerationLiteral(name="below"),
			EnumerationLiteral(name="hsides"),
			EnumerationLiteral(name="lhs"),
			EnumerationLiteral(name="rhs"),
			EnumerationLiteral(name="vsides"),
			EnumerationLiteral(name="box"),
			EnumerationLiteral(name="border")
    }
)

TRules: Enumeration = Enumeration(
    name="TRules",
    literals={
            EnumerationLiteral(name="rows"),
			EnumerationLiteral(name="cols"),
			EnumerationLiteral(name="all"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="groups")
    }
)

CellHAlign: Enumeration = Enumeration(
    name="CellHAlign",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="justify"),
			EnumerationLiteral(name="char")
    }
)

CellVAlign: Enumeration = Enumeration(
    name="CellVAlign",
    literals={
            EnumerationLiteral(name="top"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="baseline"),
			EnumerationLiteral(name="bottom")
    }
)

Scope: Enumeration = Enumeration(
    name="Scope",
    literals={
            EnumerationLiteral(name="row"),
			EnumerationLiteral(name="col"),
			EnumerationLiteral(name="rowgroup"),
			EnumerationLiteral(name="colgroup")
    }
)

# Classes
XHTML_ValuedElement = Class(name="XHTML_ValuedElement", is_abstract=True)
XHTML_CDATA = Class(name="XHTML_CDATA")
ValuedElement = Class(name="ValuedElement")
XHTML_PCDATA = Class(name="XHTML_PCDATA")
XHTML_NMTOKEN = Class(name="XHTML_NMTOKEN")
XHTML_IDREF = Class(name="XHTML_IDREF")
XHTML_IDREFS = Class(name="XHTML_IDREFS")
IDREF = Class(name="IDREF")
XHTML_ID = Class(name="XHTML_ID")
XHTML_EMPTY = Class(name="XHTML_EMPTY")
XHTML_ContentType = Class(name="XHTML_ContentType")
CDATA = Class(name="CDATA")
XHTML_ContentTypes = Class(name="XHTML_ContentTypes")
ContentType = Class(name="ContentType")
XHTML_Charset = Class(name="XHTML_Charset")
XHTML_Charsets = Class(name="XHTML_Charsets")
Charset = Class(name="Charset")
XHTML_Character = Class(name="XHTML_Character")
XHTML_Number = Class(name="XHTML_Number")
XHTML_LinkTypes = Class(name="XHTML_LinkTypes")
XHTML_MediaDesc = Class(name="XHTML_MediaDesc")
XHTML_URI = Class(name="XHTML_URI")
XHTML_UriList = Class(name="XHTML_UriList")
URI = Class(name="URI")
XHTML_Datetime = Class(name="XHTML_Datetime")
XHTML_ScriptExpression = Class(name="XHTML_ScriptExpression")
XHTML_StyleSheet = Class(name="XHTML_StyleSheet")
XHTML_Text = Class(name="XHTML_Text")
XHTML_Length = Class(name="XHTML_Length")
XHTML_MultiLength = Class(name="XHTML_MultiLength")
XHTML_Pixels = Class(name="XHTML_Pixels")
XHTML_LanguageCode = Class(name="XHTML_LanguageCode")
NMTOKEN = Class(name="NMTOKEN")
XHTML_Coords = Class(name="XHTML_Coords")
Length = Class(name="Length")
XHTML_CoreAttrs = Class(name="XHTML_CoreAttrs", is_abstract=True)
ID = Class(name="ID")
StyleSheet = Class(name="StyleSheet")
Text = Class(name="Text")
XHTML_I18n = Class(name="XHTML_I18n", is_abstract=True)
LanguageCode = Class(name="LanguageCode")
XHTML_Events = Class(name="XHTML_Events", is_abstract=True)
ScriptExpression = Class(name="ScriptExpression")
XHTML_Attrs = Class(name="XHTML_Attrs", is_abstract=True)
CoreAttrs = Class(name="CoreAttrs")
I18n = Class(name="I18n")
Events = Class(name="Events")
XHTML_Focus = Class(name="XHTML_Focus", is_abstract=True)
Character = Class(name="Character")
Number = Class(name="Number")
XHTML_Specialpre = Class(name="XHTML_Specialpre", is_abstract=True)
Special = Class(name="Special")
PreContent = Class(name="PreContent")
XHTML_Special = Class(name="XHTML_Special", is_abstract=True)
inline = Class(name="inline")
ButtonContent = Class(name="ButtonContent")
XHTML_Fontstyle = Class(name="XHTML_Fontstyle", is_abstract=True)
AContent = Class(name="AContent")
XHTML_Phrase = Class(name="XHTML_Phrase", is_abstract=True)
XHTML_Inlineforms = Class(name="XHTML_Inlineforms", is_abstract=True)
XHTML_Miscinline = Class(name="XHTML_Miscinline", is_abstract=True)
Misc = Class(name="Misc")
Inline = Class(name="Inline")
XHTML_Misc = Class(name="XHTML_Misc", is_abstract=True)
Block = Class(name="Block")
Flow = Class(name="Flow")
FormContent = Class(name="FormContent")
ObjectElement = Class(name="ObjectElement")
MapElementContent = Class(name="MapElementContent")
FieldsetElement = Class(name="FieldsetElement")
XHTML_inline = Class(name="XHTML_inline", is_abstract=True)
XHTML_Inline = Class(name="XHTML_Inline", is_abstract=True)
PCDATA = Class(name="PCDATA")
XHTML_Heading = Class(name="XHTML_Heading", is_abstract=True)
block = Class(name="block")
XHTML_Lists = Class(name="XHTML_Lists", is_abstract=True)
XHTML_Blocktext = Class(name="XHTML_Blocktext", is_abstract=True)
XHTML_Block = Class(name="XHTML_Block", is_abstract=True)
XHTML_Flow = Class(name="XHTML_Flow", is_abstract=True)
XHTML_AContent = Class(name="XHTML_AContent", is_abstract=True)
XHTML_PreContent = Class(name="XHTML_PreContent", is_abstract=True)
XHTML_FormContent = Class(name="XHTML_FormContent", is_abstract=True)
XHTML_ButtonContent = Class(name="XHTML_ButtonContent", is_abstract=True)
XHTML_Html = Class(name="XHTML_Html")
Head = Class(name="Head")
Body = Class(name="Body")
XHTML_HeadMisc = Class(name="XHTML_HeadMisc", is_abstract=True)
XHTML_Head = Class(name="XHTML_Head")
HeadMisc = Class(name="HeadMisc")
HeadElement = Class(name="HeadElement")
Html = Class(name="Html")
XHTML_block = Class(name="XHTML_block", is_abstract=True)
XHTML_HeadElement = Class(name="XHTML_HeadElement", is_abstract=True)
XHTML_TitleHeadElement = Class(name="XHTML_TitleHeadElement")
Title = Class(name="Title")
BaseTitleHeadElement = Class(name="BaseTitleHeadElement")
XHTML_BaseTitleHeadElement = Class(name="XHTML_BaseTitleHeadElement")
Base = Class(name="Base")
XHTML_BaseHeadElement = Class(name="XHTML_BaseHeadElement")
TitleBaseHeadElement = Class(name="TitleBaseHeadElement")
XHTML_TitleBaseHeadElement = Class(name="XHTML_TitleBaseHeadElement")
XHTML_Title = Class(name="XHTML_Title")
XHTML_Base = Class(name="XHTML_Base")
EMPTY = Class(name="EMPTY")
XHTML_Link = Class(name="XHTML_Link")
Attrs = Class(name="Attrs")
LinkTypes = Class(name="LinkTypes")
MediaDesc = Class(name="MediaDesc")
XHTML_Meta = Class(name="XHTML_Meta")
XHTML_Script = Class(name="XHTML_Script")
Miscinline = Class(name="Miscinline")
XHTML_Noscript = Class(name="XHTML_Noscript")
XHTML_Style = Class(name="XHTML_Style")
XHTML_Div = Class(name="XHTML_Div")
XHTML_P = Class(name="XHTML_P")
XHTML_H1 = Class(name="XHTML_H1")
Heading = Class(name="Heading")
XHTML_H2 = Class(name="XHTML_H2")
XHTML_H3 = Class(name="XHTML_H3")
XHTML_H4 = Class(name="XHTML_H4")
XHTML_H5 = Class(name="XHTML_H5")
XHTML_H6 = Class(name="XHTML_H6")
XHTML_Body = Class(name="XHTML_Body")
XHTML_Ol = Class(name="XHTML_Ol")
XHTML_Li = Class(name="XHTML_Li")
XHTML_Dl = Class(name="XHTML_Dl")
DlElement = Class(name="DlElement")
XHTML_DlElement = Class(name="XHTML_DlElement", is_abstract=True)
XHTML_Dt = Class(name="XHTML_Dt")
XHTML_Dd = Class(name="XHTML_Dd")
XHTML_Address = Class(name="XHTML_Address")
Blocktext = Class(name="Blocktext")
XHTML_Hr = Class(name="XHTML_Hr")
XHTML_Pre = Class(name="XHTML_Pre")
XHTML_Ul = Class(name="XHTML_Ul")
Lists = Class(name="Lists")
Li = Class(name="Li")
XHTML_Blockquote = Class(name="XHTML_Blockquote")
XHTML_Ins = Class(name="XHTML_Ins")
Datetime = Class(name="Datetime")
XHTML_Del = Class(name="XHTML_Del")
XHTML_A = Class(name="XHTML_A")
Focus = Class(name="Focus")
Coords = Class(name="Coords")
XHTML_Span = Class(name="XHTML_Span")
Specialpre = Class(name="Specialpre")
XHTML_Bdo = Class(name="XHTML_Bdo")
XHTML_Br = Class(name="XHTML_Br")
XHTML_Em = Class(name="XHTML_Em")
Phrase = Class(name="Phrase")
XHTML_Strong = Class(name="XHTML_Strong")
XHTML_Dfn = Class(name="XHTML_Dfn")
XHTML_Code = Class(name="XHTML_Code")
XHTML_Samp = Class(name="XHTML_Samp")
XHTML_Kbd = Class(name="XHTML_Kbd")
XHTML_Var = Class(name="XHTML_Var")
XHTML_Cite = Class(name="XHTML_Cite")
XHTML_Abbr = Class(name="XHTML_Abbr")
XHTML_Acronym = Class(name="XHTML_Acronym")
XHTML_Q = Class(name="XHTML_Q")
XHTML_Sub = Class(name="XHTML_Sub")
XHTML_Sup = Class(name="XHTML_Sup")
XHTML_Tt = Class(name="XHTML_Tt")
Fontstyle = Class(name="Fontstyle")
XHTML_I = Class(name="XHTML_I")
XHTML_B = Class(name="XHTML_B")
XHTML_Big = Class(name="XHTML_Big")
XHTML_Small = Class(name="XHTML_Small")
XHTML_ObjectElement = Class(name="XHTML_ObjectElement", is_abstract=True)
XHTML_Object = Class(name="XHTML_Object")
UriList = Class(name="UriList")
XHTML_Param = Class(name="XHTML_Param")
XHTML_Img = Class(name="XHTML_Img")
XHTML_MapContent = Class(name="XHTML_MapContent")
MapElement = Class(name="MapElement")
XHTML_MapElement = Class(name="XHTML_MapElement", is_abstract=True)
XHTML_MapElementContent = Class(name="XHTML_MapElementContent", is_abstract=True)
XHTML_Map = Class(name="XHTML_Map")
MapContent = Class(name="MapContent")
XHTML_Area = Class(name="XHTML_Area")
XHTML_Form = Class(name="XHTML_Form")
ContentTypes = Class(name="ContentTypes")
Charsets = Class(name="Charsets")
XHTML_Label = Class(name="XHTML_Label")
XHTML_Input = Class(name="XHTML_Input")
Inlineforms = Class(name="Inlineforms")
XHTML_Select = Class(name="XHTML_Select")
SelectElement = Class(name="SelectElement")
XHTML_SelectElement = Class(name="XHTML_SelectElement", is_abstract=True)
XHTML_Optgroup = Class(name="XHTML_Optgroup")
XHTML_Option = Class(name="XHTML_Option")
XHTML_Textarea = Class(name="XHTML_Textarea")
Option = Class(name="Option")
XHTML_FieldsetElement = Class(name="XHTML_FieldsetElement", is_abstract=True)
XHTML_Fieldset = Class(name="XHTML_Fieldset")
XHTML_Legend = Class(name="XHTML_Legend")
XHTML_Button = Class(name="XHTML_Button")
XHTML_Cellhalign = Class(name="XHTML_Cellhalign", is_abstract=True)
XHTML_Cellvalign = Class(name="XHTML_Cellvalign", is_abstract=True)
XHTML_Table = Class(name="XHTML_Table")
Caption = Class(name="Caption")
Thead = Class(name="Thead")
Tfoot = Class(name="Tfoot")
TableElement = Class(name="TableElement")
ColElement = Class(name="ColElement")
XHTML_ColElement = Class(name="XHTML_ColElement")
Col = Class(name="Col")
Colgroup = Class(name="Colgroup")
XHTML_TableElement = Class(name="XHTML_TableElement")
Tbody = Class(name="Tbody")
Tr = Class(name="Tr")
Pixels = Class(name="Pixels")
XHTML_Thead = Class(name="XHTML_Thead")
Cellhalign = Class(name="Cellhalign")
Cellvalign = Class(name="Cellvalign")
XHTML_Tfoot = Class(name="XHTML_Tfoot")
XHTML_Tbody = Class(name="XHTML_Tbody")
XHTML_Colgroup = Class(name="XHTML_Colgroup")
XHTML_Caption = Class(name="XHTML_Caption")
MultiLength = Class(name="MultiLength")
XHTML_Col = Class(name="XHTML_Col")
XHTML_Tr = Class(name="XHTML_Tr")
TrElement = Class(name="TrElement")
IDREFS = Class(name="IDREFS")
XHTML_TrElement = Class(name="XHTML_TrElement", is_abstract=True)
XHTML_Th = Class(name="XHTML_Th")
XHTML_Td = Class(name="XHTML_Td")

# XHTML_ValuedElement class attributes and methods
XHTML_ValuedElement_value: Property = Property(name="value", type=StringType)
XHTML_ValuedElement.attributes={XHTML_ValuedElement_value}

# XHTML_CDATA class attributes and methods

# ValuedElement class attributes and methods

# XHTML_PCDATA class attributes and methods

# XHTML_NMTOKEN class attributes and methods

# XHTML_IDREF class attributes and methods

# XHTML_IDREFS class attributes and methods

# IDREF class attributes and methods

# XHTML_ID class attributes and methods

# XHTML_EMPTY class attributes and methods

# XHTML_ContentType class attributes and methods

# CDATA class attributes and methods

# XHTML_ContentTypes class attributes and methods

# ContentType class attributes and methods

# XHTML_Charset class attributes and methods

# XHTML_Charsets class attributes and methods

# Charset class attributes and methods

# XHTML_Character class attributes and methods

# XHTML_Number class attributes and methods

# XHTML_LinkTypes class attributes and methods

# XHTML_MediaDesc class attributes and methods

# XHTML_URI class attributes and methods

# XHTML_UriList class attributes and methods

# URI class attributes and methods

# XHTML_Datetime class attributes and methods

# XHTML_ScriptExpression class attributes and methods

# XHTML_StyleSheet class attributes and methods

# XHTML_Text class attributes and methods

# XHTML_Length class attributes and methods

# XHTML_MultiLength class attributes and methods

# XHTML_Pixels class attributes and methods

# XHTML_LanguageCode class attributes and methods

# NMTOKEN class attributes and methods

# XHTML_Coords class attributes and methods

# Length class attributes and methods

# XHTML_CoreAttrs class attributes and methods

# ID class attributes and methods

# StyleSheet class attributes and methods

# Text class attributes and methods

# XHTML_I18n class attributes and methods
XHTML_I18n_dir: Property = Property(name="dir", type=StringType)
XHTML_I18n.attributes={XHTML_I18n_dir}

# LanguageCode class attributes and methods

# XHTML_Events class attributes and methods

# ScriptExpression class attributes and methods

# XHTML_Attrs class attributes and methods

# CoreAttrs class attributes and methods

# I18n class attributes and methods

# Events class attributes and methods

# XHTML_Focus class attributes and methods

# Character class attributes and methods

# Number class attributes and methods

# XHTML_Specialpre class attributes and methods

# Special class attributes and methods

# PreContent class attributes and methods

# XHTML_Special class attributes and methods

# inline class attributes and methods

# ButtonContent class attributes and methods

# XHTML_Fontstyle class attributes and methods

# AContent class attributes and methods

# XHTML_Phrase class attributes and methods

# XHTML_Inlineforms class attributes and methods

# XHTML_Miscinline class attributes and methods

# Misc class attributes and methods

# Inline class attributes and methods

# XHTML_Misc class attributes and methods

# Block class attributes and methods

# Flow class attributes and methods

# FormContent class attributes and methods

# ObjectElement class attributes and methods

# MapElementContent class attributes and methods

# FieldsetElement class attributes and methods

# XHTML_inline class attributes and methods

# XHTML_Inline class attributes and methods

# PCDATA class attributes and methods

# XHTML_Heading class attributes and methods

# block class attributes and methods

# XHTML_Lists class attributes and methods

# XHTML_Blocktext class attributes and methods

# XHTML_Block class attributes and methods

# XHTML_Flow class attributes and methods

# XHTML_AContent class attributes and methods

# XHTML_PreContent class attributes and methods

# XHTML_FormContent class attributes and methods

# XHTML_ButtonContent class attributes and methods

# XHTML_Html class attributes and methods

# Head class attributes and methods

# Body class attributes and methods

# XHTML_HeadMisc class attributes and methods

# XHTML_Head class attributes and methods

# HeadMisc class attributes and methods

# HeadElement class attributes and methods

# Html class attributes and methods

# XHTML_block class attributes and methods

# XHTML_HeadElement class attributes and methods

# XHTML_TitleHeadElement class attributes and methods

# Title class attributes and methods

# BaseTitleHeadElement class attributes and methods

# XHTML_BaseTitleHeadElement class attributes and methods

# Base class attributes and methods

# XHTML_BaseHeadElement class attributes and methods

# TitleBaseHeadElement class attributes and methods

# XHTML_TitleBaseHeadElement class attributes and methods

# XHTML_Title class attributes and methods

# XHTML_Base class attributes and methods

# EMPTY class attributes and methods

# XHTML_Link class attributes and methods

# Attrs class attributes and methods

# LinkTypes class attributes and methods

# MediaDesc class attributes and methods

# XHTML_Meta class attributes and methods

# XHTML_Script class attributes and methods
XHTML_Script_defer: Property = Property(name="defer", type=StringType)
XHTML_Script_xml_space: Property = Property(name="xml_space", type=StringType)
XHTML_Script.attributes={XHTML_Script_defer, XHTML_Script_xml_space}

# Miscinline class attributes and methods

# XHTML_Noscript class attributes and methods

# XHTML_Style class attributes and methods
XHTML_Style_xml_space: Property = Property(name="xml_space", type=StringType)
XHTML_Style.attributes={XHTML_Style_xml_space}

# XHTML_Div class attributes and methods

# XHTML_P class attributes and methods

# XHTML_H1 class attributes and methods

# Heading class attributes and methods

# XHTML_H2 class attributes and methods

# XHTML_H3 class attributes and methods

# XHTML_H4 class attributes and methods

# XHTML_H5 class attributes and methods

# XHTML_H6 class attributes and methods

# XHTML_Body class attributes and methods

# XHTML_Ol class attributes and methods

# XHTML_Li class attributes and methods

# XHTML_Dl class attributes and methods

# DlElement class attributes and methods

# XHTML_DlElement class attributes and methods

# XHTML_Dt class attributes and methods

# XHTML_Dd class attributes and methods

# XHTML_Address class attributes and methods

# Blocktext class attributes and methods

# XHTML_Hr class attributes and methods

# XHTML_Pre class attributes and methods
XHTML_Pre_xml_space: Property = Property(name="xml_space", type=StringType)
XHTML_Pre.attributes={XHTML_Pre_xml_space}

# XHTML_Ul class attributes and methods

# Lists class attributes and methods

# Li class attributes and methods

# XHTML_Blockquote class attributes and methods

# XHTML_Ins class attributes and methods

# Datetime class attributes and methods

# XHTML_Del class attributes and methods

# XHTML_A class attributes and methods
XHTML_A_shape: Property = Property(name="shape", type=StringType)
XHTML_A.attributes={XHTML_A_shape}

# Focus class attributes and methods

# Coords class attributes and methods

# XHTML_Span class attributes and methods

# Specialpre class attributes and methods

# XHTML_Bdo class attributes and methods
XHTML_Bdo_dir: Property = Property(name="dir", type=StringType)
XHTML_Bdo.attributes={XHTML_Bdo_dir}

# XHTML_Br class attributes and methods

# XHTML_Em class attributes and methods

# Phrase class attributes and methods

# XHTML_Strong class attributes and methods

# XHTML_Dfn class attributes and methods

# XHTML_Code class attributes and methods

# XHTML_Samp class attributes and methods

# XHTML_Kbd class attributes and methods

# XHTML_Var class attributes and methods

# XHTML_Cite class attributes and methods

# XHTML_Abbr class attributes and methods

# XHTML_Acronym class attributes and methods

# XHTML_Q class attributes and methods

# XHTML_Sub class attributes and methods

# XHTML_Sup class attributes and methods

# XHTML_Tt class attributes and methods

# Fontstyle class attributes and methods

# XHTML_I class attributes and methods

# XHTML_B class attributes and methods

# XHTML_Big class attributes and methods

# XHTML_Small class attributes and methods

# XHTML_ObjectElement class attributes and methods

# XHTML_Object class attributes and methods
XHTML_Object_declare: Property = Property(name="declare", type=StringType)
XHTML_Object.attributes={XHTML_Object_declare}

# UriList class attributes and methods

# XHTML_Param class attributes and methods
XHTML_Param_valuetype: Property = Property(name="valuetype", type=StringType)
XHTML_Param.attributes={XHTML_Param_valuetype}

# XHTML_Img class attributes and methods
XHTML_Img_ismap: Property = Property(name="ismap", type=StringType)
XHTML_Img.attributes={XHTML_Img_ismap}

# XHTML_MapContent class attributes and methods

# MapElement class attributes and methods

# XHTML_MapElement class attributes and methods

# XHTML_MapElementContent class attributes and methods

# XHTML_Map class attributes and methods

# MapContent class attributes and methods

# XHTML_Area class attributes and methods
XHTML_Area_shape: Property = Property(name="shape", type=StringType)
XHTML_Area_nohref: Property = Property(name="nohref", type=StringType)
XHTML_Area.attributes={XHTML_Area_nohref, XHTML_Area_shape}

# XHTML_Form class attributes and methods
XHTML_Form_method: Property = Property(name="method", type=StringType)
XHTML_Form.attributes={XHTML_Form_method}

# ContentTypes class attributes and methods

# Charsets class attributes and methods

# XHTML_Label class attributes and methods

# XHTML_Input class attributes and methods
XHTML_Input_type: Property = Property(name="type", type=StringType)
XHTML_Input_checked: Property = Property(name="checked", type=StringType)
XHTML_Input_disabled: Property = Property(name="disabled", type=StringType)
XHTML_Input_readonly: Property = Property(name="readonly", type=StringType)
XHTML_Input.attributes={XHTML_Input_checked, XHTML_Input_type, XHTML_Input_disabled, XHTML_Input_readonly}

# Inlineforms class attributes and methods

# XHTML_Select class attributes and methods
XHTML_Select_multiple: Property = Property(name="multiple", type=StringType)
XHTML_Select_disabled: Property = Property(name="disabled", type=StringType)
XHTML_Select.attributes={XHTML_Select_disabled, XHTML_Select_multiple}

# SelectElement class attributes and methods

# XHTML_SelectElement class attributes and methods

# XHTML_Optgroup class attributes and methods
XHTML_Optgroup_disabled: Property = Property(name="disabled", type=StringType)
XHTML_Optgroup.attributes={XHTML_Optgroup_disabled}

# XHTML_Option class attributes and methods
XHTML_Option_selected: Property = Property(name="selected", type=StringType)
XHTML_Option_disabled: Property = Property(name="disabled", type=StringType)
XHTML_Option.attributes={XHTML_Option_disabled, XHTML_Option_selected}

# XHTML_Textarea class attributes and methods
XHTML_Textarea_disabled: Property = Property(name="disabled", type=StringType)
XHTML_Textarea_readonly: Property = Property(name="readonly", type=StringType)
XHTML_Textarea.attributes={XHTML_Textarea_disabled, XHTML_Textarea_readonly}

# Option class attributes and methods

# XHTML_FieldsetElement class attributes and methods

# XHTML_Fieldset class attributes and methods

# XHTML_Legend class attributes and methods

# XHTML_Button class attributes and methods
XHTML_Button_type: Property = Property(name="type", type=StringType)
XHTML_Button_disabled: Property = Property(name="disabled", type=StringType)
XHTML_Button.attributes={XHTML_Button_type, XHTML_Button_disabled}

# XHTML_Cellhalign class attributes and methods
XHTML_Cellhalign_align: Property = Property(name="align", type=StringType)
XHTML_Cellhalign.attributes={XHTML_Cellhalign_align}

# XHTML_Cellvalign class attributes and methods
XHTML_Cellvalign_valign: Property = Property(name="valign", type=StringType)
XHTML_Cellvalign.attributes={XHTML_Cellvalign_valign}

# XHTML_Table class attributes and methods
XHTML_Table_frame: Property = Property(name="frame", type=StringType)
XHTML_Table_rules: Property = Property(name="rules", type=StringType)
XHTML_Table.attributes={XHTML_Table_rules, XHTML_Table_frame}

# Caption class attributes and methods

# Thead class attributes and methods

# Tfoot class attributes and methods

# TableElement class attributes and methods

# ColElement class attributes and methods

# XHTML_ColElement class attributes and methods

# Col class attributes and methods

# Colgroup class attributes and methods

# XHTML_TableElement class attributes and methods

# Tbody class attributes and methods

# Tr class attributes and methods

# Pixels class attributes and methods

# XHTML_Thead class attributes and methods

# Cellhalign class attributes and methods

# Cellvalign class attributes and methods

# XHTML_Tfoot class attributes and methods

# XHTML_Tbody class attributes and methods

# XHTML_Colgroup class attributes and methods

# XHTML_Caption class attributes and methods

# MultiLength class attributes and methods

# XHTML_Col class attributes and methods

# XHTML_Tr class attributes and methods

# TrElement class attributes and methods

# IDREFS class attributes and methods

# XHTML_TrElement class attributes and methods

# XHTML_Th class attributes and methods
XHTML_Th_scope: Property = Property(name="scope", type=StringType)
XHTML_Th.attributes={XHTML_Th_scope}

# XHTML_Td class attributes and methods
XHTML_Td_scope: Property = Property(name="scope", type=StringType)
XHTML_Td.attributes={XHTML_Td_scope}

# Relationships
idrefs0: BinaryAssociation = BinaryAssociation(
    name="idrefs0",
    ends={
        Property(name="IDREF", type=XHTML_IDREFS, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_IDREFS", type=IDREF, multiplicity=Multiplicity(0, 9999))
    }
)
contentTypes1: BinaryAssociation = BinaryAssociation(
    name="contentTypes1",
    ends={
        Property(name="ContentType", type=XHTML_ContentTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_ContentTypes", type=ContentType, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
charsets2: BinaryAssociation = BinaryAssociation(
    name="charsets2",
    ends={
        Property(name="Charset", type=XHTML_Charsets, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Charsets", type=Charset, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
uris3: BinaryAssociation = BinaryAssociation(
    name="uris3",
    ends={
        Property(name="URI", type=XHTML_UriList, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_UriList", type=URI, multiplicity=Multiplicity(2, 9999))
    }
)
lengths4: BinaryAssociation = BinaryAssociation(
    name="lengths4",
    ends={
        Property(name="Length", type=XHTML_Coords, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Coords", type=Length, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
id5: BinaryAssociation = BinaryAssociation(
    name="id5",
    ends={
        Property(name="ID", type=XHTML_CoreAttrs, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_CoreAttrs", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class_6: BinaryAssociation = BinaryAssociation(
    name="class_6",
    ends={
        Property(name="CDATA", type=XHTML_CoreAttrs, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_CoreAttrs7", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style8: BinaryAssociation = BinaryAssociation(
    name="style8",
    ends={
        Property(name="StyleSheet", type=XHTML_CoreAttrs, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_CoreAttrs9", type=StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title10: BinaryAssociation = BinaryAssociation(
    name="title10",
    ends={
        Property(name="Text", type=XHTML_CoreAttrs, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_CoreAttrs11", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lang12: BinaryAssociation = BinaryAssociation(
    name="lang12",
    ends={
        Property(name="LanguageCode", type=XHTML_I18n, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_I18n", type=LanguageCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xml_lang13: BinaryAssociation = BinaryAssociation(
    name="xml_lang13",
    ends={
        Property(name="LanguageCode15", type=XHTML_I18n, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_I18n14", type=LanguageCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onclick16: BinaryAssociation = BinaryAssociation(
    name="onclick16",
    ends={
        Property(name="ScriptExpression", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ondblclick17: BinaryAssociation = BinaryAssociation(
    name="ondblclick17",
    ends={
        Property(name="ScriptExpression19", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events18", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onmouseup23: BinaryAssociation = BinaryAssociation(
    name="onmouseup23",
    ends={
        Property(name="ScriptExpression25", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events24", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onmouseover26: BinaryAssociation = BinaryAssociation(
    name="onmouseover26",
    ends={
        Property(name="ScriptExpression28", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events27", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onmousemove29: BinaryAssociation = BinaryAssociation(
    name="onmousemove29",
    ends={
        Property(name="ScriptExpression31", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events30", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onmouseout32: BinaryAssociation = BinaryAssociation(
    name="onmouseout32",
    ends={
        Property(name="ScriptExpression34", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events33", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onkeypress35: BinaryAssociation = BinaryAssociation(
    name="onkeypress35",
    ends={
        Property(name="ScriptExpression37", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events36", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onkeydown38: BinaryAssociation = BinaryAssociation(
    name="onkeydown38",
    ends={
        Property(name="ScriptExpression40", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events39", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onkeyup41: BinaryAssociation = BinaryAssociation(
    name="onkeyup41",
    ends={
        Property(name="ScriptExpression43", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events42", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accesskey44: BinaryAssociation = BinaryAssociation(
    name="accesskey44",
    ends={
        Property(name="Character", type=XHTML_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Focus", type=Character, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabindex45: BinaryAssociation = BinaryAssociation(
    name="tabindex45",
    ends={
        Property(name="Number", type=XHTML_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Focus46", type=Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onfocus47: BinaryAssociation = BinaryAssociation(
    name="onfocus47",
    ends={
        Property(name="ScriptExpression49", type=XHTML_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Focus48", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onblur50: BinaryAssociation = BinaryAssociation(
    name="onblur50",
    ends={
        Property(name="ScriptExpression52", type=XHTML_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Focus51", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onmousedown20: BinaryAssociation = BinaryAssociation(
    name="onmousedown20",
    ends={
        Property(name="ScriptExpression22", type=XHTML_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Events21", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcdataInline53: BinaryAssociation = BinaryAssociation(
    name="pcdataInline53",
    ends={
        Property(name="PCDATA", type=XHTML_Inline, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Inline", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pcdataFlow54: BinaryAssociation = BinaryAssociation(
    name="pcdataFlow54",
    ends={
        Property(name="PCDATA55", type=XHTML_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Flow", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pcdataAContent56: BinaryAssociation = BinaryAssociation(
    name="pcdataAContent56",
    ends={
        Property(name="PCDATA57", type=XHTML_AContent, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_AContent", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pcdataPreContent58: BinaryAssociation = BinaryAssociation(
    name="pcdataPreContent58",
    ends={
        Property(name="PCDATA59", type=XHTML_PreContent, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_PreContent", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pcdataButtonContent60: BinaryAssociation = BinaryAssociation(
    name="pcdataButtonContent60",
    ends={
        Property(name="PCDATA61", type=XHTML_ButtonContent, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_ButtonContent", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i18n62: BinaryAssociation = BinaryAssociation(
    name="i18n62",
    ends={
        Property(name="I18n", type=XHTML_Html, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Html", type=I18n, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id63: BinaryAssociation = BinaryAssociation(
    name="id63",
    ends={
        Property(name="ID65", type=XHTML_Html, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Html64", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xmlns66: BinaryAssociation = BinaryAssociation(
    name="xmlns66",
    ends={
        Property(name="URI68", type=XHTML_Html, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Html67", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
head69: BinaryAssociation = BinaryAssociation(
    name="head69",
    ends={
        Property(name="Head", type=XHTML_Html, multiplicity=Multiplicity(1, 1)),
        Property(name="html", type=Head, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body70: BinaryAssociation = BinaryAssociation(
    name="body70",
    ends={
        Property(name="Body", type=XHTML_Html, multiplicity=Multiplicity(1, 1)),
        Property(name="html71", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
i18n72: BinaryAssociation = BinaryAssociation(
    name="i18n72",
    ends={
        Property(name="I18n73", type=XHTML_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Head", type=I18n, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id74: BinaryAssociation = BinaryAssociation(
    name="id74",
    ends={
        Property(name="ID76", type=XHTML_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Head75", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
profile77: BinaryAssociation = BinaryAssociation(
    name="profile77",
    ends={
        Property(name="URI79", type=XHTML_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Head78", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headmisc80: BinaryAssociation = BinaryAssociation(
    name="headmisc80",
    ends={
        Property(name="HeadMisc", type=XHTML_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Head81", type=HeadMisc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headelement82: BinaryAssociation = BinaryAssociation(
    name="headelement82",
    ends={
        Property(name="HeadElement", type=XHTML_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Head83", type=HeadElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
html84: BinaryAssociation = BinaryAssociation(
    name="html84",
    ends={
        Property(name="Html", type=XHTML_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=Html, multiplicity=Multiplicity(1, 1))
    }
)
title85: BinaryAssociation = BinaryAssociation(
    name="title85",
    ends={
        Property(name="Title", type=XHTML_TitleHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TitleHeadElement", type=Title, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
headmisc86: BinaryAssociation = BinaryAssociation(
    name="headmisc86",
    ends={
        Property(name="HeadMisc88", type=XHTML_TitleHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TitleHeadElement87", type=HeadMisc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTitleHeadElement89: BinaryAssociation = BinaryAssociation(
    name="baseTitleHeadElement89",
    ends={
        Property(name="BaseTitleHeadElement", type=XHTML_TitleHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TitleHeadElement90", type=BaseTitleHeadElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
base91: BinaryAssociation = BinaryAssociation(
    name="base91",
    ends={
        Property(name="Base", type=XHTML_BaseTitleHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_BaseTitleHeadElement", type=Base, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
headmisc92: BinaryAssociation = BinaryAssociation(
    name="headmisc92",
    ends={
        Property(name="HeadMisc94", type=XHTML_BaseTitleHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_BaseTitleHeadElement93", type=HeadMisc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base95: BinaryAssociation = BinaryAssociation(
    name="base95",
    ends={
        Property(name="Base96", type=XHTML_BaseHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_BaseHeadElement", type=Base, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
headmisc97: BinaryAssociation = BinaryAssociation(
    name="headmisc97",
    ends={
        Property(name="HeadMisc99", type=XHTML_BaseHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_BaseHeadElement98", type=HeadMisc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
titleBaseHeadElement100: BinaryAssociation = BinaryAssociation(
    name="titleBaseHeadElement100",
    ends={
        Property(name="TitleBaseHeadElement", type=XHTML_BaseHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_BaseHeadElement101", type=TitleBaseHeadElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
title102: BinaryAssociation = BinaryAssociation(
    name="title102",
    ends={
        Property(name="Title103", type=XHTML_TitleBaseHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TitleBaseHeadElement", type=Title, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
headmisc104: BinaryAssociation = BinaryAssociation(
    name="headmisc104",
    ends={
        Property(name="HeadMisc106", type=XHTML_TitleBaseHeadElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TitleBaseHeadElement105", type=HeadMisc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
i18n107: BinaryAssociation = BinaryAssociation(
    name="i18n107",
    ends={
        Property(name="I18n108", type=XHTML_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Title", type=I18n, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id109: BinaryAssociation = BinaryAssociation(
    name="id109",
    ends={
        Property(name="ID111", type=XHTML_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Title110", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
href112: BinaryAssociation = BinaryAssociation(
    name="href112",
    ends={
        Property(name="URI113", type=XHTML_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Base", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
i18n117: BinaryAssociation = BinaryAssociation(
    name="i18n117",
    ends={
        Property(name="I18n118", type=XHTML_Meta, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Meta", type=I18n, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id119: BinaryAssociation = BinaryAssociation(
    name="id119",
    ends={
        Property(name="ID121", type=XHTML_Meta, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Meta120", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
httpequiv122: BinaryAssociation = BinaryAssociation(
    name="httpequiv122",
    ends={
        Property(name="CDATA124", type=XHTML_Meta, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Meta123", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name125: BinaryAssociation = BinaryAssociation(
    name="name125",
    ends={
        Property(name="CDATA127", type=XHTML_Meta, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Meta126", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content128: BinaryAssociation = BinaryAssociation(
    name="content128",
    ends={
        Property(name="CDATA130", type=XHTML_Meta, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Meta129", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scheme131: BinaryAssociation = BinaryAssociation(
    name="scheme131",
    ends={
        Property(name="CDATA133", type=XHTML_Meta, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Meta132", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
charset134: BinaryAssociation = BinaryAssociation(
    name="charset134",
    ends={
        Property(name="Charset135", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link", type=Charset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
href136: BinaryAssociation = BinaryAssociation(
    name="href136",
    ends={
        Property(name="URI138", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link137", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hreflang139: BinaryAssociation = BinaryAssociation(
    name="hreflang139",
    ends={
        Property(name="LanguageCode141", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link140", type=LanguageCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="ContentType144", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link143", type=ContentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rel145: BinaryAssociation = BinaryAssociation(
    name="rel145",
    ends={
        Property(name="LinkTypes", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link146", type=LinkTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rev147: BinaryAssociation = BinaryAssociation(
    name="rev147",
    ends={
        Property(name="LinkTypes149", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link148", type=LinkTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id114: BinaryAssociation = BinaryAssociation(
    name="id114",
    ends={
        Property(name="ID116", type=XHTML_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Base115", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
i18n152: BinaryAssociation = BinaryAssociation(
    name="i18n152",
    ends={
        Property(name="I18n153", type=XHTML_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Style", type=I18n, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id154: BinaryAssociation = BinaryAssociation(
    name="id154",
    ends={
        Property(name="ID156", type=XHTML_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Style155", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type157: BinaryAssociation = BinaryAssociation(
    name="type157",
    ends={
        Property(name="ContentType159", type=XHTML_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Style158", type=ContentType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
media160: BinaryAssociation = BinaryAssociation(
    name="media160",
    ends={
        Property(name="MediaDesc162", type=XHTML_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Style161", type=MediaDesc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title163: BinaryAssociation = BinaryAssociation(
    name="title163",
    ends={
        Property(name="Text165", type=XHTML_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Style164", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id166: BinaryAssociation = BinaryAssociation(
    name="id166",
    ends={
        Property(name="ID167", type=XHTML_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Script", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
charset168: BinaryAssociation = BinaryAssociation(
    name="charset168",
    ends={
        Property(name="Charset170", type=XHTML_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Script169", type=Charset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type171: BinaryAssociation = BinaryAssociation(
    name="type171",
    ends={
        Property(name="ContentType173", type=XHTML_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Script172", type=ContentType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
src174: BinaryAssociation = BinaryAssociation(
    name="src174",
    ends={
        Property(name="URI176", type=XHTML_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Script175", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block177: BinaryAssociation = BinaryAssociation(
    name="block177",
    ends={
        Property(name="Block", type=XHTML_Noscript, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Noscript", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
media150: BinaryAssociation = BinaryAssociation(
    name="media150",
    ends={
        Property(name="MediaDesc", type=XHTML_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Link151", type=MediaDesc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onload180: BinaryAssociation = BinaryAssociation(
    name="onload180",
    ends={
        Property(name="ScriptExpression182", type=XHTML_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Body181", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onunload183: BinaryAssociation = BinaryAssociation(
    name="onunload183",
    ends={
        Property(name="ScriptExpression185", type=XHTML_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Body184", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
html186: BinaryAssociation = BinaryAssociation(
    name="html186",
    ends={
        Property(name="Html187", type=XHTML_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=Html, multiplicity=Multiplicity(1, 1))
    }
)
divElements188: BinaryAssociation = BinaryAssociation(
    name="divElements188",
    ends={
        Property(name="Flow", type=XHTML_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Div", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pElements189: BinaryAssociation = BinaryAssociation(
    name="pElements189",
    ends={
        Property(name="Inline", type=XHTML_P, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_P", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h1Elements190: BinaryAssociation = BinaryAssociation(
    name="h1Elements190",
    ends={
        Property(name="Inline191", type=XHTML_H1, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_H1", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h2Elements192: BinaryAssociation = BinaryAssociation(
    name="h2Elements192",
    ends={
        Property(name="Inline193", type=XHTML_H2, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_H2", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h3Elements194: BinaryAssociation = BinaryAssociation(
    name="h3Elements194",
    ends={
        Property(name="Inline195", type=XHTML_H3, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_H3", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h4Elements196: BinaryAssociation = BinaryAssociation(
    name="h4Elements196",
    ends={
        Property(name="Inline197", type=XHTML_H4, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_H4", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h5Elements198: BinaryAssociation = BinaryAssociation(
    name="h5Elements198",
    ends={
        Property(name="Inline199", type=XHTML_H5, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_H5", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h6Elements200: BinaryAssociation = BinaryAssociation(
    name="h6Elements200",
    ends={
        Property(name="Inline201", type=XHTML_H6, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_H6", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyElements178: BinaryAssociation = BinaryAssociation(
    name="bodyElements178",
    ends={
        Property(name="Block179", type=XHTML_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Body", type=Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li203: BinaryAssociation = BinaryAssociation(
    name="li203",
    ends={
        Property(name="Li204", type=XHTML_Ol, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Ol", type=Li, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
liElements205: BinaryAssociation = BinaryAssociation(
    name="liElements205",
    ends={
        Property(name="Flow206", type=XHTML_Li, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Li", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dlElements207: BinaryAssociation = BinaryAssociation(
    name="dlElements207",
    ends={
        Property(name="DlElement", type=XHTML_Dl, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Dl", type=DlElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dtElements208: BinaryAssociation = BinaryAssociation(
    name="dtElements208",
    ends={
        Property(name="Inline209", type=XHTML_Dt, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Dt", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ddElements210: BinaryAssociation = BinaryAssociation(
    name="ddElements210",
    ends={
        Property(name="Flow211", type=XHTML_Dd, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Dd", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressElements212: BinaryAssociation = BinaryAssociation(
    name="addressElements212",
    ends={
        Property(name="Inline213", type=XHTML_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Address", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
li202: BinaryAssociation = BinaryAssociation(
    name="li202",
    ends={
        Property(name="Li", type=XHTML_Ul, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Ul", type=Li, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
blockquoteElements215: BinaryAssociation = BinaryAssociation(
    name="blockquoteElements215",
    ends={
        Property(name="Block216", type=XHTML_Blockquote, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Blockquote", type=Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite217: BinaryAssociation = BinaryAssociation(
    name="cite217",
    ends={
        Property(name="URI219", type=XHTML_Blockquote, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Blockquote218", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flowelement220: BinaryAssociation = BinaryAssociation(
    name="flowelement220",
    ends={
        Property(name="Flow221", type=XHTML_Ins, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Ins", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite222: BinaryAssociation = BinaryAssociation(
    name="cite222",
    ends={
        Property(name="URI224", type=XHTML_Ins, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Ins223", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datetime225: BinaryAssociation = BinaryAssociation(
    name="datetime225",
    ends={
        Property(name="Datetime", type=XHTML_Ins, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Ins226", type=Datetime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flowelement227: BinaryAssociation = BinaryAssociation(
    name="flowelement227",
    ends={
        Property(name="Flow228", type=XHTML_Del, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Del", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite229: BinaryAssociation = BinaryAssociation(
    name="cite229",
    ends={
        Property(name="URI231", type=XHTML_Del, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Del230", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datetime232: BinaryAssociation = BinaryAssociation(
    name="datetime232",
    ends={
        Property(name="Datetime234", type=XHTML_Del, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Del233", type=Datetime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preElements214: BinaryAssociation = BinaryAssociation(
    name="preElements214",
    ends={
        Property(name="PreContent", type=XHTML_Pre, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Pre", type=PreContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acontent235: BinaryAssociation = BinaryAssociation(
    name="acontent235",
    ends={
        Property(name="AContent", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A", type=AContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
charset236: BinaryAssociation = BinaryAssociation(
    name="charset236",
    ends={
        Property(name="Charset238", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A237", type=Charset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type239: BinaryAssociation = BinaryAssociation(
    name="type239",
    ends={
        Property(name="ContentType241", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A240", type=ContentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name242: BinaryAssociation = BinaryAssociation(
    name="name242",
    ends={
        Property(name="NMTOKEN", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A243", type=NMTOKEN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
href244: BinaryAssociation = BinaryAssociation(
    name="href244",
    ends={
        Property(name="URI246", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A245", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hreflang247: BinaryAssociation = BinaryAssociation(
    name="hreflang247",
    ends={
        Property(name="LanguageCode249", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A248", type=LanguageCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rel250: BinaryAssociation = BinaryAssociation(
    name="rel250",
    ends={
        Property(name="LinkTypes252", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A251", type=LinkTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rev253: BinaryAssociation = BinaryAssociation(
    name="rev253",
    ends={
        Property(name="LinkTypes255", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A254", type=LinkTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
coords256: BinaryAssociation = BinaryAssociation(
    name="coords256",
    ends={
        Property(name="Coords", type=XHTML_A, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_A257", type=Coords, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spanElements258: BinaryAssociation = BinaryAssociation(
    name="spanElements258",
    ends={
        Property(name="Inline259", type=XHTML_Span, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Span", type=Inline, multiplicity=Multiplicity(0, 9999))
    }
)
bdoElements260: BinaryAssociation = BinaryAssociation(
    name="bdoElements260",
    ends={
        Property(name="Inline261", type=XHTML_Bdo, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Bdo", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lang262: BinaryAssociation = BinaryAssociation(
    name="lang262",
    ends={
        Property(name="LanguageCode264", type=XHTML_Bdo, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Bdo263", type=LanguageCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xml_lang265: BinaryAssociation = BinaryAssociation(
    name="xml_lang265",
    ends={
        Property(name="LanguageCode267", type=XHTML_Bdo, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Bdo266", type=LanguageCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emElements268: BinaryAssociation = BinaryAssociation(
    name="emElements268",
    ends={
        Property(name="Inline269", type=XHTML_Em, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Em", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strongElements270: BinaryAssociation = BinaryAssociation(
    name="strongElements270",
    ends={
        Property(name="Inline271", type=XHTML_Strong, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Strong", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dfnElements272: BinaryAssociation = BinaryAssociation(
    name="dfnElements272",
    ends={
        Property(name="Inline273", type=XHTML_Dfn, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Dfn", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sampElements276: BinaryAssociation = BinaryAssociation(
    name="sampElements276",
    ends={
        Property(name="Inline277", type=XHTML_Samp, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Samp", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kbdElements278: BinaryAssociation = BinaryAssociation(
    name="kbdElements278",
    ends={
        Property(name="Inline279", type=XHTML_Kbd, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Kbd", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varElements280: BinaryAssociation = BinaryAssociation(
    name="varElements280",
    ends={
        Property(name="Inline281", type=XHTML_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Var", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citeElements282: BinaryAssociation = BinaryAssociation(
    name="citeElements282",
    ends={
        Property(name="Inline283", type=XHTML_Cite, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Cite", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbrElements284: BinaryAssociation = BinaryAssociation(
    name="abbrElements284",
    ends={
        Property(name="Inline285", type=XHTML_Abbr, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Abbr", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acronymElements286: BinaryAssociation = BinaryAssociation(
    name="acronymElements286",
    ends={
        Property(name="Inline287", type=XHTML_Acronym, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Acronym", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qElements288: BinaryAssociation = BinaryAssociation(
    name="qElements288",
    ends={
        Property(name="Inline289", type=XHTML_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Q", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cite290: BinaryAssociation = BinaryAssociation(
    name="cite290",
    ends={
        Property(name="URI292", type=XHTML_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Q291", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subElements293: BinaryAssociation = BinaryAssociation(
    name="subElements293",
    ends={
        Property(name="Inline294", type=XHTML_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Sub", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
codeElements274: BinaryAssociation = BinaryAssociation(
    name="codeElements274",
    ends={
        Property(name="Inline275", type=XHTML_Code, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Code", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ttElements297: BinaryAssociation = BinaryAssociation(
    name="ttElements297",
    ends={
        Property(name="Inline298", type=XHTML_Tt, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Tt", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iElements299: BinaryAssociation = BinaryAssociation(
    name="iElements299",
    ends={
        Property(name="Inline300", type=XHTML_I, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_I", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bElements301: BinaryAssociation = BinaryAssociation(
    name="bElements301",
    ends={
        Property(name="Inline302", type=XHTML_B, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_B", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bigElements303: BinaryAssociation = BinaryAssociation(
    name="bigElements303",
    ends={
        Property(name="Inline304", type=XHTML_Big, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Big", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
smallElements305: BinaryAssociation = BinaryAssociation(
    name="smallElements305",
    ends={
        Property(name="Inline306", type=XHTML_Small, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Small", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectpcdata307: BinaryAssociation = BinaryAssociation(
    name="objectpcdata307",
    ends={
        Property(name="PCDATA308", type=XHTML_ObjectElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_ObjectElement", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectelement309: BinaryAssociation = BinaryAssociation(
    name="objectelement309",
    ends={
        Property(name="ObjectElement", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object", type=ObjectElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supElements295: BinaryAssociation = BinaryAssociation(
    name="supElements295",
    ends={
        Property(name="Inline296", type=XHTML_Sup, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Sup", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classid310: BinaryAssociation = BinaryAssociation(
    name="classid310",
    ends={
        Property(name="URI312", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object311", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codebase313: BinaryAssociation = BinaryAssociation(
    name="codebase313",
    ends={
        Property(name="URI315", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object314", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data316: BinaryAssociation = BinaryAssociation(
    name="data316",
    ends={
        Property(name="URI318", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object317", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type319: BinaryAssociation = BinaryAssociation(
    name="type319",
    ends={
        Property(name="ContentType321", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object320", type=ContentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codetype322: BinaryAssociation = BinaryAssociation(
    name="codetype322",
    ends={
        Property(name="ContentType324", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object323", type=ContentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
archive325: BinaryAssociation = BinaryAssociation(
    name="archive325",
    ends={
        Property(name="UriList", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object326", type=UriList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
standby327: BinaryAssociation = BinaryAssociation(
    name="standby327",
    ends={
        Property(name="Text329", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object328", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
height330: BinaryAssociation = BinaryAssociation(
    name="height330",
    ends={
        Property(name="Length332", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object331", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
width333: BinaryAssociation = BinaryAssociation(
    name="width333",
    ends={
        Property(name="Length335", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object334", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usemap336: BinaryAssociation = BinaryAssociation(
    name="usemap336",
    ends={
        Property(name="URI338", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object337", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name339: BinaryAssociation = BinaryAssociation(
    name="name339",
    ends={
        Property(name="NMTOKEN341", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object340", type=NMTOKEN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabindex342: BinaryAssociation = BinaryAssociation(
    name="tabindex342",
    ends={
        Property(name="Number344", type=XHTML_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Object343", type=Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id345: BinaryAssociation = BinaryAssociation(
    name="id345",
    ends={
        Property(name="ID346", type=XHTML_Param, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Param", type=ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value350: BinaryAssociation = BinaryAssociation(
    name="value350",
    ends={
        Property(name="CDATA352", type=XHTML_Param, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Param351", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type353: BinaryAssociation = BinaryAssociation(
    name="type353",
    ends={
        Property(name="ContentType355", type=XHTML_Param, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Param354", type=ContentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src356: BinaryAssociation = BinaryAssociation(
    name="src356",
    ends={
        Property(name="URI357", type=XHTML_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Img", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alt358: BinaryAssociation = BinaryAssociation(
    name="alt358",
    ends={
        Property(name="Text360", type=XHTML_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Img359", type=Text, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
longdesc361: BinaryAssociation = BinaryAssociation(
    name="longdesc361",
    ends={
        Property(name="URI363", type=XHTML_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Img362", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
height364: BinaryAssociation = BinaryAssociation(
    name="height364",
    ends={
        Property(name="Length366", type=XHTML_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Img365", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
width367: BinaryAssociation = BinaryAssociation(
    name="width367",
    ends={
        Property(name="Length369", type=XHTML_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Img368", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name347: BinaryAssociation = BinaryAssociation(
    name="name347",
    ends={
        Property(name="CDATA349", type=XHTML_Param, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Param348", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapElements373: BinaryAssociation = BinaryAssociation(
    name="mapElements373",
    ends={
        Property(name="MapElement", type=XHTML_MapContent, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_MapContent", type=MapElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mapelement374: BinaryAssociation = BinaryAssociation(
    name="mapelement374",
    ends={
        Property(name="MapContent", type=XHTML_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Map", type=MapContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usemap370: BinaryAssociation = BinaryAssociation(
    name="usemap370",
    ends={
        Property(name="URI372", type=XHTML_Img, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Img371", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style381: BinaryAssociation = BinaryAssociation(
    name="style381",
    ends={
        Property(name="StyleSheet383", type=XHTML_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Map382", type=StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title384: BinaryAssociation = BinaryAssociation(
    name="title384",
    ends={
        Property(name="Text386", type=XHTML_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Map385", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name387: BinaryAssociation = BinaryAssociation(
    name="name387",
    ends={
        Property(name="NMTOKEN389", type=XHTML_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Map388", type=NMTOKEN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
coords390: BinaryAssociation = BinaryAssociation(
    name="coords390",
    ends={
        Property(name="Coords391", type=XHTML_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Area", type=Coords, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
href392: BinaryAssociation = BinaryAssociation(
    name="href392",
    ends={
        Property(name="URI394", type=XHTML_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Area393", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alt395: BinaryAssociation = BinaryAssociation(
    name="alt395",
    ends={
        Property(name="Text397", type=XHTML_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Area396", type=Text, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id375: BinaryAssociation = BinaryAssociation(
    name="id375",
    ends={
        Property(name="ID377", type=XHTML_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Map376", type=ID, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
class_378: BinaryAssociation = BinaryAssociation(
    name="class_378",
    ends={
        Property(name="CDATA380", type=XHTML_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Map379", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formelement398: BinaryAssociation = BinaryAssociation(
    name="formelement398",
    ends={
        Property(name="FormContent", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form", type=FormContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action399: BinaryAssociation = BinaryAssociation(
    name="action399",
    ends={
        Property(name="URI401", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form400", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enctype402: BinaryAssociation = BinaryAssociation(
    name="enctype402",
    ends={
        Property(name="ContentType404", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form403", type=ContentType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
onsubmit405: BinaryAssociation = BinaryAssociation(
    name="onsubmit405",
    ends={
        Property(name="ScriptExpression407", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form406", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onreset408: BinaryAssociation = BinaryAssociation(
    name="onreset408",
    ends={
        Property(name="ScriptExpression410", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form409", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accept411: BinaryAssociation = BinaryAssociation(
    name="accept411",
    ends={
        Property(name="ContentTypes", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form412", type=ContentTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accept_charset413: BinaryAssociation = BinaryAssociation(
    name="accept_charset413",
    ends={
        Property(name="Charsets", type=XHTML_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Form414", type=Charsets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
for_417: BinaryAssociation = BinaryAssociation(
    name="for_417",
    ends={
        Property(name="IDREF419", type=XHTML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Label418", type=IDREF, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accesskey420: BinaryAssociation = BinaryAssociation(
    name="accesskey420",
    ends={
        Property(name="Character422", type=XHTML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Label421", type=Character, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onfocus423: BinaryAssociation = BinaryAssociation(
    name="onfocus423",
    ends={
        Property(name="ScriptExpression425", type=XHTML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Label424", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onblur426: BinaryAssociation = BinaryAssociation(
    name="onblur426",
    ends={
        Property(name="ScriptExpression428", type=XHTML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Label427", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelelements415: BinaryAssociation = BinaryAssociation(
    name="labelelements415",
    ends={
        Property(name="Inline416", type=XHTML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Label", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name429: BinaryAssociation = BinaryAssociation(
    name="name429",
    ends={
        Property(name="CDATA430", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value431: BinaryAssociation = BinaryAssociation(
    name="value431",
    ends={
        Property(name="CDATA433", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input432", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size434: BinaryAssociation = BinaryAssociation(
    name="size434",
    ends={
        Property(name="CDATA436", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input435", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxlength437: BinaryAssociation = BinaryAssociation(
    name="maxlength437",
    ends={
        Property(name="Number439", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input438", type=Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src440: BinaryAssociation = BinaryAssociation(
    name="src440",
    ends={
        Property(name="URI442", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input441", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alt443: BinaryAssociation = BinaryAssociation(
    name="alt443",
    ends={
        Property(name="CDATA445", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input444", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usemap446: BinaryAssociation = BinaryAssociation(
    name="usemap446",
    ends={
        Property(name="URI448", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input447", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onselect449: BinaryAssociation = BinaryAssociation(
    name="onselect449",
    ends={
        Property(name="ScriptExpression451", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input450", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onchange452: BinaryAssociation = BinaryAssociation(
    name="onchange452",
    ends={
        Property(name="ScriptExpression454", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input453", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accept455: BinaryAssociation = BinaryAssociation(
    name="accept455",
    ends={
        Property(name="ContentTypes457", type=XHTML_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Input456", type=ContentTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectelement458: BinaryAssociation = BinaryAssociation(
    name="selectelement458",
    ends={
        Property(name="SelectElement", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select", type=SelectElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
size462: BinaryAssociation = BinaryAssociation(
    name="size462",
    ends={
        Property(name="Number464", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select463", type=Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabindex465: BinaryAssociation = BinaryAssociation(
    name="tabindex465",
    ends={
        Property(name="Number467", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select466", type=Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onfocus468: BinaryAssociation = BinaryAssociation(
    name="onfocus468",
    ends={
        Property(name="ScriptExpression470", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select469", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onblur471: BinaryAssociation = BinaryAssociation(
    name="onblur471",
    ends={
        Property(name="ScriptExpression473", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select472", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onchange474: BinaryAssociation = BinaryAssociation(
    name="onchange474",
    ends={
        Property(name="ScriptExpression476", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select475", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name459: BinaryAssociation = BinaryAssociation(
    name="name459",
    ends={
        Property(name="CDATA461", type=XHTML_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Select460", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
options477: BinaryAssociation = BinaryAssociation(
    name="options477",
    ends={
        Property(name="Option", type=XHTML_Optgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Optgroup", type=Option, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
label478: BinaryAssociation = BinaryAssociation(
    name="label478",
    ends={
        Property(name="Text480", type=XHTML_Optgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Optgroup479", type=Text, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label481: BinaryAssociation = BinaryAssociation(
    name="label481",
    ends={
        Property(name="Text482", type=XHTML_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Option", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionvalue483: BinaryAssociation = BinaryAssociation(
    name="optionvalue483",
    ends={
        Property(name="CDATA485", type=XHTML_Option, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Option484", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows488: BinaryAssociation = BinaryAssociation(
    name="rows488",
    ends={
        Property(name="Number490", type=XHTML_Textarea, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Textarea489", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cols491: BinaryAssociation = BinaryAssociation(
    name="cols491",
    ends={
        Property(name="Number493", type=XHTML_Textarea, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Textarea492", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
onselect494: BinaryAssociation = BinaryAssociation(
    name="onselect494",
    ends={
        Property(name="ScriptExpression496", type=XHTML_Textarea, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Textarea495", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onchange497: BinaryAssociation = BinaryAssociation(
    name="onchange497",
    ends={
        Property(name="ScriptExpression499", type=XHTML_Textarea, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Textarea498", type=ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldsetpcdata500: BinaryAssociation = BinaryAssociation(
    name="fieldsetpcdata500",
    ends={
        Property(name="PCDATA501", type=XHTML_FieldsetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_FieldsetElement", type=PCDATA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name486: BinaryAssociation = BinaryAssociation(
    name="name486",
    ends={
        Property(name="CDATA487", type=XHTML_Textarea, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Textarea", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldsetelements502: BinaryAssociation = BinaryAssociation(
    name="fieldsetelements502",
    ends={
        Property(name="FieldsetElement", type=XHTML_Fieldset, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Fieldset", type=FieldsetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
legendelement503: BinaryAssociation = BinaryAssociation(
    name="legendelement503",
    ends={
        Property(name="Inline504", type=XHTML_Legend, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Legend", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accesskey505: BinaryAssociation = BinaryAssociation(
    name="accesskey505",
    ends={
        Property(name="Character507", type=XHTML_Legend, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Legend506", type=Character, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttoncontent508: BinaryAssociation = BinaryAssociation(
    name="buttoncontent508",
    ends={
        Property(name="ButtonContent", type=XHTML_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Button", type=ButtonContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value512: BinaryAssociation = BinaryAssociation(
    name="value512",
    ends={
        Property(name="CDATA514", type=XHTML_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Button513", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name509: BinaryAssociation = BinaryAssociation(
    name="name509",
    ends={
        Property(name="CDATA511", type=XHTML_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Button510", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
char515: BinaryAssociation = BinaryAssociation(
    name="char515",
    ends={
        Property(name="Character516", type=XHTML_Cellhalign, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Cellhalign", type=Character, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
charoff517: BinaryAssociation = BinaryAssociation(
    name="charoff517",
    ends={
        Property(name="Length519", type=XHTML_Cellhalign, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Cellhalign518", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caption520: BinaryAssociation = BinaryAssociation(
    name="caption520",
    ends={
        Property(name="Caption", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table", type=Caption, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
colelement521: BinaryAssociation = BinaryAssociation(
    name="colelement521",
    ends={
        Property(name="ColElement", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table522", type=ColElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thead523: BinaryAssociation = BinaryAssociation(
    name="thead523",
    ends={
        Property(name="Thead", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table524", type=Thead, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tfoot525: BinaryAssociation = BinaryAssociation(
    name="tfoot525",
    ends={
        Property(name="Tfoot", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table526", type=Tfoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableelement527: BinaryAssociation = BinaryAssociation(
    name="tableelement527",
    ends={
        Property(name="TableElement", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table528", type=TableElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
summary529: BinaryAssociation = BinaryAssociation(
    name="summary529",
    ends={
        Property(name="Text531", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table530", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
width532: BinaryAssociation = BinaryAssociation(
    name="width532",
    ends={
        Property(name="Length534", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table533", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cellspacing537: BinaryAssociation = BinaryAssociation(
    name="cellspacing537",
    ends={
        Property(name="Length539", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table538", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cellpadding540: BinaryAssociation = BinaryAssociation(
    name="cellpadding540",
    ends={
        Property(name="Length542", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table541", type=Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cols543: BinaryAssociation = BinaryAssociation(
    name="cols543",
    ends={
        Property(name="Col", type=XHTML_ColElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_ColElement", type=Col, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colgroup544: BinaryAssociation = BinaryAssociation(
    name="colgroup544",
    ends={
        Property(name="Colgroup", type=XHTML_ColElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_ColElement545", type=Colgroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tbody546: BinaryAssociation = BinaryAssociation(
    name="tbody546",
    ends={
        Property(name="Tbody", type=XHTML_TableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TableElement", type=Tbody, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr547: BinaryAssociation = BinaryAssociation(
    name="tr547",
    ends={
        Property(name="Tr", type=XHTML_TableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_TableElement548", type=Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
border535: BinaryAssociation = BinaryAssociation(
    name="border535",
    ends={
        Property(name="Pixels", type=XHTML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Table536", type=Pixels, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
captionelement549: BinaryAssociation = BinaryAssociation(
    name="captionelement549",
    ends={
        Property(name="Inline550", type=XHTML_Caption, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Caption", type=Inline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr551: BinaryAssociation = BinaryAssociation(
    name="tr551",
    ends={
        Property(name="Tr552", type=XHTML_Thead, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Thead", type=Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr553: BinaryAssociation = BinaryAssociation(
    name="tr553",
    ends={
        Property(name="Tr554", type=XHTML_Tfoot, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Tfoot", type=Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tr555: BinaryAssociation = BinaryAssociation(
    name="tr555",
    ends={
        Property(name="Tr556", type=XHTML_Tbody, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Tbody", type=Tr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cols557: BinaryAssociation = BinaryAssociation(
    name="cols557",
    ends={
        Property(name="Col558", type=XHTML_Colgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Colgroup", type=Col, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
span559: BinaryAssociation = BinaryAssociation(
    name="span559",
    ends={
        Property(name="Number561", type=XHTML_Colgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Colgroup560", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
width562: BinaryAssociation = BinaryAssociation(
    name="width562",
    ends={
        Property(name="MultiLength", type=XHTML_Colgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Colgroup563", type=MultiLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
span564: BinaryAssociation = BinaryAssociation(
    name="span564",
    ends={
        Property(name="Number565", type=XHTML_Col, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Col", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
width566: BinaryAssociation = BinaryAssociation(
    name="width566",
    ends={
        Property(name="MultiLength568", type=XHTML_Col, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Col567", type=MultiLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headers578: BinaryAssociation = BinaryAssociation(
    name="headers578",
    ends={
        Property(name="IDREFS", type=XHTML_Th, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Th579", type=IDREFS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rowspan580: BinaryAssociation = BinaryAssociation(
    name="rowspan580",
    ends={
        Property(name="Number582", type=XHTML_Th, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Th581", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thelement570: BinaryAssociation = BinaryAssociation(
    name="thelement570",
    ends={
        Property(name="Flow571", type=XHTML_Th, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Th", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abbr572: BinaryAssociation = BinaryAssociation(
    name="abbr572",
    ends={
        Property(name="Text574", type=XHTML_Th, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Th573", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
axis575: BinaryAssociation = BinaryAssociation(
    name="axis575",
    ends={
        Property(name="CDATA577", type=XHTML_Th, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Th576", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trelements569: BinaryAssociation = BinaryAssociation(
    name="trelements569",
    ends={
        Property(name="TrElement", type=XHTML_Tr, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Tr", type=TrElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
colspan583: BinaryAssociation = BinaryAssociation(
    name="colspan583",
    ends={
        Property(name="Number585", type=XHTML_Th, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Th584", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tdelement586: BinaryAssociation = BinaryAssociation(
    name="tdelement586",
    ends={
        Property(name="Flow587", type=XHTML_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Td", type=Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headers594: BinaryAssociation = BinaryAssociation(
    name="headers594",
    ends={
        Property(name="IDREFS596", type=XHTML_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Td595", type=IDREFS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abbr588: BinaryAssociation = BinaryAssociation(
    name="abbr588",
    ends={
        Property(name="Text590", type=XHTML_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Td589", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rowspan597: BinaryAssociation = BinaryAssociation(
    name="rowspan597",
    ends={
        Property(name="Number599", type=XHTML_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Td598", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
axis591: BinaryAssociation = BinaryAssociation(
    name="axis591",
    ends={
        Property(name="CDATA593", type=XHTML_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Td592", type=CDATA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colspan600: BinaryAssociation = BinaryAssociation(
    name="colspan600",
    ends={
        Property(name="Number602", type=XHTML_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="XHTML_Td601", type=Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_XHTML_CDATA_ValuedElement = Generalization(general=ValuedElement, specific=XHTML_CDATA)
gen_XHTML_PCDATA_ValuedElement = Generalization(general=ValuedElement, specific=XHTML_PCDATA)
gen_XHTML_NMTOKEN_ValuedElement = Generalization(general=ValuedElement, specific=XHTML_NMTOKEN)
gen_XHTML_IDREF_ValuedElement = Generalization(general=ValuedElement, specific=XHTML_IDREF)
gen_XHTML_ID_ValuedElement = Generalization(general=ValuedElement, specific=XHTML_ID)
gen_XHTML_ContentType_CDATA = Generalization(general=CDATA, specific=XHTML_ContentType)
gen_XHTML_Charset_CDATA = Generalization(general=CDATA, specific=XHTML_Charset)
gen_XHTML_Character_CDATA = Generalization(general=CDATA, specific=XHTML_Character)
gen_XHTML_Number_CDATA = Generalization(general=CDATA, specific=XHTML_Number)
gen_XHTML_LinkTypes_CDATA = Generalization(general=CDATA, specific=XHTML_LinkTypes)
gen_XHTML_MediaDesc_CDATA = Generalization(general=CDATA, specific=XHTML_MediaDesc)
gen_XHTML_URI_CDATA = Generalization(general=CDATA, specific=XHTML_URI)
gen_XHTML_Datetime_CDATA = Generalization(general=CDATA, specific=XHTML_Datetime)
gen_XHTML_ScriptExpression_CDATA = Generalization(general=CDATA, specific=XHTML_ScriptExpression)
gen_XHTML_StyleSheet_CDATA = Generalization(general=CDATA, specific=XHTML_StyleSheet)
gen_XHTML_Text_CDATA = Generalization(general=CDATA, specific=XHTML_Text)
gen_XHTML_Length_CDATA = Generalization(general=CDATA, specific=XHTML_Length)
gen_XHTML_MultiLength_CDATA = Generalization(general=CDATA, specific=XHTML_MultiLength)
gen_XHTML_Pixels_CDATA = Generalization(general=CDATA, specific=XHTML_Pixels)
gen_XHTML_LanguageCode_NMTOKEN = Generalization(general=NMTOKEN, specific=XHTML_LanguageCode)
gen_XHTML_Attrs_CoreAttrs = Generalization(general=CoreAttrs, specific=XHTML_Attrs)
gen_XHTML_Attrs_I18n = Generalization(general=I18n, specific=XHTML_Attrs)
gen_XHTML_Attrs_Events = Generalization(general=Events, specific=XHTML_Attrs)
gen_XHTML_Specialpre_Special = Generalization(general=Special, specific=XHTML_Specialpre)
gen_XHTML_Specialpre_PreContent = Generalization(general=PreContent, specific=XHTML_Specialpre)
gen_XHTML_Special_inline = Generalization(general=inline, specific=XHTML_Special)
gen_XHTML_Special_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Special)
gen_XHTML_Fontstyle_inline = Generalization(general=inline, specific=XHTML_Fontstyle)
gen_XHTML_Fontstyle_AContent = Generalization(general=AContent, specific=XHTML_Fontstyle)
gen_XHTML_Fontstyle_PreContent = Generalization(general=PreContent, specific=XHTML_Fontstyle)
gen_XHTML_Fontstyle_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Fontstyle)
gen_XHTML_Phrase_inline = Generalization(general=inline, specific=XHTML_Phrase)
gen_XHTML_Phrase_AContent = Generalization(general=AContent, specific=XHTML_Phrase)
gen_XHTML_Phrase_PreContent = Generalization(general=PreContent, specific=XHTML_Phrase)
gen_XHTML_Phrase_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Phrase)
gen_XHTML_Inlineforms_inline = Generalization(general=inline, specific=XHTML_Inlineforms)
gen_XHTML_Inlineforms_AContent = Generalization(general=AContent, specific=XHTML_Inlineforms)
gen_XHTML_Inlineforms_PreContent = Generalization(general=PreContent, specific=XHTML_Inlineforms)
gen_XHTML_Miscinline_Misc = Generalization(general=Misc, specific=XHTML_Miscinline)
gen_XHTML_Miscinline_Inline = Generalization(general=Inline, specific=XHTML_Miscinline)
gen_XHTML_Miscinline_AContent = Generalization(general=AContent, specific=XHTML_Miscinline)
gen_XHTML_Miscinline_PreContent = Generalization(general=PreContent, specific=XHTML_Miscinline)
gen_XHTML_Misc_Block = Generalization(general=Block, specific=XHTML_Misc)
gen_XHTML_Misc_Flow = Generalization(general=Flow, specific=XHTML_Misc)
gen_XHTML_Misc_FormContent = Generalization(general=FormContent, specific=XHTML_Misc)
gen_XHTML_Misc_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Misc)
gen_XHTML_Misc_ObjectElement = Generalization(general=ObjectElement, specific=XHTML_Misc)
gen_XHTML_Misc_MapElementContent = Generalization(general=MapElementContent, specific=XHTML_Misc)
gen_XHTML_Misc_FieldsetElement = Generalization(general=FieldsetElement, specific=XHTML_Misc)
gen_XHTML_inline_Inline = Generalization(general=Inline, specific=XHTML_inline)
gen_XHTML_Inline_Flow = Generalization(general=Flow, specific=XHTML_Inline)
gen_XHTML_Inline_ObjectElement = Generalization(general=ObjectElement, specific=XHTML_Inline)
gen_XHTML_Inline_FieldsetElement = Generalization(general=FieldsetElement, specific=XHTML_Inline)
gen_XHTML_Heading_block = Generalization(general=block, specific=XHTML_Heading)
gen_XHTML_Heading_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Heading)
gen_XHTML_Lists_block = Generalization(general=block, specific=XHTML_Lists)
gen_XHTML_Lists_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Lists)
gen_XHTML_Blocktext_block = Generalization(general=block, specific=XHTML_Blocktext)
gen_XHTML_Blocktext_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Blocktext)
gen_XHTML_block_Block = Generalization(general=Block, specific=XHTML_block)
gen_XHTML_block_Flow = Generalization(general=Flow, specific=XHTML_block)
gen_XHTML_block_FormContent = Generalization(general=FormContent, specific=XHTML_block)
gen_XHTML_block_ObjectElement = Generalization(general=ObjectElement, specific=XHTML_block)
gen_XHTML_block_MapElementContent = Generalization(general=MapElementContent, specific=XHTML_block)
gen_XHTML_block_FieldsetElement = Generalization(general=FieldsetElement, specific=XHTML_block)
gen_XHTML_TitleHeadElement_HeadElement = Generalization(general=HeadElement, specific=XHTML_TitleHeadElement)
gen_XHTML_BaseHeadElement_HeadElement = Generalization(general=HeadElement, specific=XHTML_BaseHeadElement)
gen_XHTML_Title_PCDATA = Generalization(general=PCDATA, specific=XHTML_Title)
gen_XHTML_Base_EMPTY = Generalization(general=EMPTY, specific=XHTML_Base)
gen_XHTML_Link_EMPTY = Generalization(general=EMPTY, specific=XHTML_Link)
gen_XHTML_Link_Attrs = Generalization(general=Attrs, specific=XHTML_Link)
gen_XHTML_Link_HeadMisc = Generalization(general=HeadMisc, specific=XHTML_Link)
gen_XHTML_Meta_EMPTY = Generalization(general=EMPTY, specific=XHTML_Meta)
gen_XHTML_Meta_HeadMisc = Generalization(general=HeadMisc, specific=XHTML_Meta)
gen_XHTML_Script_PCDATA = Generalization(general=PCDATA, specific=XHTML_Script)
gen_XHTML_Script_Miscinline = Generalization(general=Miscinline, specific=XHTML_Script)
gen_XHTML_Script_HeadMisc = Generalization(general=HeadMisc, specific=XHTML_Script)
gen_XHTML_Noscript_Attrs = Generalization(general=Attrs, specific=XHTML_Noscript)
gen_XHTML_Noscript_Misc = Generalization(general=Misc, specific=XHTML_Noscript)
gen_XHTML_Style_PCDATA = Generalization(general=PCDATA, specific=XHTML_Style)
gen_XHTML_Style_HeadMisc = Generalization(general=HeadMisc, specific=XHTML_Style)
gen_XHTML_Div_Attrs = Generalization(general=Attrs, specific=XHTML_Div)
gen_XHTML_Div_block = Generalization(general=block, specific=XHTML_Div)
gen_XHTML_Div_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Div)
gen_XHTML_P_Attrs = Generalization(general=Attrs, specific=XHTML_P)
gen_XHTML_P_block = Generalization(general=block, specific=XHTML_P)
gen_XHTML_P_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_P)
gen_XHTML_H1_Attrs = Generalization(general=Attrs, specific=XHTML_H1)
gen_XHTML_H1_Heading = Generalization(general=Heading, specific=XHTML_H1)
gen_XHTML_H2_Attrs = Generalization(general=Attrs, specific=XHTML_H2)
gen_XHTML_H2_Heading = Generalization(general=Heading, specific=XHTML_H2)
gen_XHTML_H3_Attrs = Generalization(general=Attrs, specific=XHTML_H3)
gen_XHTML_H3_Heading = Generalization(general=Heading, specific=XHTML_H3)
gen_XHTML_H4_Attrs = Generalization(general=Attrs, specific=XHTML_H4)
gen_XHTML_H4_Heading = Generalization(general=Heading, specific=XHTML_H4)
gen_XHTML_H5_Attrs = Generalization(general=Attrs, specific=XHTML_H5)
gen_XHTML_H5_Heading = Generalization(general=Heading, specific=XHTML_H5)
gen_XHTML_H6_Attrs = Generalization(general=Attrs, specific=XHTML_H6)
gen_XHTML_H6_Heading = Generalization(general=Heading, specific=XHTML_H6)
gen_XHTML_Body_Attrs = Generalization(general=Attrs, specific=XHTML_Body)
gen_XHTML_Ol_Attrs = Generalization(general=Attrs, specific=XHTML_Ol)
gen_XHTML_Ol_Lists = Generalization(general=Lists, specific=XHTML_Ol)
gen_XHTML_Li_Attrs = Generalization(general=Attrs, specific=XHTML_Li)
gen_XHTML_Dl_Attrs = Generalization(general=Attrs, specific=XHTML_Dl)
gen_XHTML_Dl_Lists = Generalization(general=Lists, specific=XHTML_Dl)
gen_XHTML_DlElement_Attrs = Generalization(general=Attrs, specific=XHTML_DlElement)
gen_XHTML_Dt_DlElement = Generalization(general=DlElement, specific=XHTML_Dt)
gen_XHTML_Dd_DlElement = Generalization(general=DlElement, specific=XHTML_Dd)
gen_XHTML_Address_Attrs = Generalization(general=Attrs, specific=XHTML_Address)
gen_XHTML_Address_Blocktext = Generalization(general=Blocktext, specific=XHTML_Address)
gen_XHTML_Hr_EMPTY = Generalization(general=EMPTY, specific=XHTML_Hr)
gen_XHTML_Hr_Attrs = Generalization(general=Attrs, specific=XHTML_Hr)
gen_XHTML_Hr_Blocktext = Generalization(general=Blocktext, specific=XHTML_Hr)
gen_XHTML_Pre_Attrs = Generalization(general=Attrs, specific=XHTML_Pre)
gen_XHTML_Pre_Blocktext = Generalization(general=Blocktext, specific=XHTML_Pre)
gen_XHTML_Ul_Attrs = Generalization(general=Attrs, specific=XHTML_Ul)
gen_XHTML_Ul_Lists = Generalization(general=Lists, specific=XHTML_Ul)
gen_XHTML_Blockquote_Attrs = Generalization(general=Attrs, specific=XHTML_Blockquote)
gen_XHTML_Blockquote_Blocktext = Generalization(general=Blocktext, specific=XHTML_Blockquote)
gen_XHTML_Ins_Attrs = Generalization(general=Attrs, specific=XHTML_Ins)
gen_XHTML_Ins_Miscinline = Generalization(general=Miscinline, specific=XHTML_Ins)
gen_XHTML_Del_Attrs = Generalization(general=Attrs, specific=XHTML_Del)
gen_XHTML_Del_Miscinline = Generalization(general=Miscinline, specific=XHTML_Del)
gen_XHTML_A_Attrs = Generalization(general=Attrs, specific=XHTML_A)
gen_XHTML_A_Focus = Generalization(general=Focus, specific=XHTML_A)
gen_XHTML_A_inline = Generalization(general=inline, specific=XHTML_A)
gen_XHTML_A_PreContent = Generalization(general=PreContent, specific=XHTML_A)
gen_XHTML_Span_Attrs = Generalization(general=Attrs, specific=XHTML_Span)
gen_XHTML_Span_Specialpre = Generalization(general=Specialpre, specific=XHTML_Span)
gen_XHTML_Bdo_CoreAttrs = Generalization(general=CoreAttrs, specific=XHTML_Bdo)
gen_XHTML_Bdo_Events = Generalization(general=Events, specific=XHTML_Bdo)
gen_XHTML_Bdo_Specialpre = Generalization(general=Specialpre, specific=XHTML_Bdo)
gen_XHTML_Br_EMPTY = Generalization(general=EMPTY, specific=XHTML_Br)
gen_XHTML_Br_CoreAttrs = Generalization(general=CoreAttrs, specific=XHTML_Br)
gen_XHTML_Br_Specialpre = Generalization(general=Specialpre, specific=XHTML_Br)
gen_XHTML_Em_Attrs = Generalization(general=Attrs, specific=XHTML_Em)
gen_XHTML_Em_Phrase = Generalization(general=Phrase, specific=XHTML_Em)
gen_XHTML_Strong_Attrs = Generalization(general=Attrs, specific=XHTML_Strong)
gen_XHTML_Strong_Phrase = Generalization(general=Phrase, specific=XHTML_Strong)
gen_XHTML_Dfn_Attrs = Generalization(general=Attrs, specific=XHTML_Dfn)
gen_XHTML_Dfn_Phrase = Generalization(general=Phrase, specific=XHTML_Dfn)
gen_XHTML_Code_Attrs = Generalization(general=Attrs, specific=XHTML_Code)
gen_XHTML_Code_Phrase = Generalization(general=Phrase, specific=XHTML_Code)
gen_XHTML_Samp_Attrs = Generalization(general=Attrs, specific=XHTML_Samp)
gen_XHTML_Samp_Phrase = Generalization(general=Phrase, specific=XHTML_Samp)
gen_XHTML_Kbd_Attrs = Generalization(general=Attrs, specific=XHTML_Kbd)
gen_XHTML_Kbd_Phrase = Generalization(general=Phrase, specific=XHTML_Kbd)
gen_XHTML_Var_Attrs = Generalization(general=Attrs, specific=XHTML_Var)
gen_XHTML_Var_Phrase = Generalization(general=Phrase, specific=XHTML_Var)
gen_XHTML_Cite_Attrs = Generalization(general=Attrs, specific=XHTML_Cite)
gen_XHTML_Cite_Phrase = Generalization(general=Phrase, specific=XHTML_Cite)
gen_XHTML_Abbr_Attrs = Generalization(general=Attrs, specific=XHTML_Abbr)
gen_XHTML_Abbr_Phrase = Generalization(general=Phrase, specific=XHTML_Abbr)
gen_XHTML_Acronym_Attrs = Generalization(general=Attrs, specific=XHTML_Acronym)
gen_XHTML_Acronym_Phrase = Generalization(general=Phrase, specific=XHTML_Acronym)
gen_XHTML_Q_Attrs = Generalization(general=Attrs, specific=XHTML_Q)
gen_XHTML_Q_Phrase = Generalization(general=Phrase, specific=XHTML_Q)
gen_XHTML_Sub_Attrs = Generalization(general=Attrs, specific=XHTML_Sub)
gen_XHTML_Sub_Phrase = Generalization(general=Phrase, specific=XHTML_Sub)
gen_XHTML_Tt_Attrs = Generalization(general=Attrs, specific=XHTML_Tt)
gen_XHTML_Tt_Fontstyle = Generalization(general=Fontstyle, specific=XHTML_Tt)
gen_XHTML_I_Attrs = Generalization(general=Attrs, specific=XHTML_I)
gen_XHTML_I_Fontstyle = Generalization(general=Fontstyle, specific=XHTML_I)
gen_XHTML_B_Attrs = Generalization(general=Attrs, specific=XHTML_B)
gen_XHTML_B_Fontstyle = Generalization(general=Fontstyle, specific=XHTML_B)
gen_XHTML_Big_Attrs = Generalization(general=Attrs, specific=XHTML_Big)
gen_XHTML_Big_Fontstyle = Generalization(general=Fontstyle, specific=XHTML_Big)
gen_XHTML_Small_Attrs = Generalization(general=Attrs, specific=XHTML_Small)
gen_XHTML_Small_Fontstyle = Generalization(general=Fontstyle, specific=XHTML_Small)
gen_XHTML_Object_Attrs = Generalization(general=Attrs, specific=XHTML_Object)
gen_XHTML_Object_Special = Generalization(general=Special, specific=XHTML_Object)
gen_XHTML_Object_HeadMisc = Generalization(general=HeadMisc, specific=XHTML_Object)
gen_XHTML_Sup_Attrs = Generalization(general=Attrs, specific=XHTML_Sup)
gen_XHTML_Sup_Phrase = Generalization(general=Phrase, specific=XHTML_Sup)
gen_XHTML_Param_EMPTY = Generalization(general=EMPTY, specific=XHTML_Param)
gen_XHTML_Param_ObjectElement = Generalization(general=ObjectElement, specific=XHTML_Param)
gen_XHTML_Img_EMPTY = Generalization(general=EMPTY, specific=XHTML_Img)
gen_XHTML_Img_Attrs = Generalization(general=Attrs, specific=XHTML_Img)
gen_XHTML_Img_Special = Generalization(general=Special, specific=XHTML_Img)
gen_XHTML_Map_I18n = Generalization(general=I18n, specific=XHTML_Map)
gen_XHTML_Map_Events = Generalization(general=Events, specific=XHTML_Map)
gen_XHTML_Map_Specialpre = Generalization(general=Specialpre, specific=XHTML_Map)
gen_XHTML_Area_EMPTY = Generalization(general=EMPTY, specific=XHTML_Area)
gen_XHTML_Area_Attrs = Generalization(general=Attrs, specific=XHTML_Area)
gen_XHTML_Area_Focus = Generalization(general=Focus, specific=XHTML_Area)
gen_XHTML_Area_MapElement = Generalization(general=MapElement, specific=XHTML_Area)
gen_XHTML_Form_Attrs = Generalization(general=Attrs, specific=XHTML_Form)
gen_XHTML_Form_Block = Generalization(general=Block, specific=XHTML_Form)
gen_XHTML_Form_ObjectElement = Generalization(general=ObjectElement, specific=XHTML_Form)
gen_XHTML_Form_MapElementContent = Generalization(general=MapElementContent, specific=XHTML_Form)
gen_XHTML_Form_FieldsetElement = Generalization(general=FieldsetElement, specific=XHTML_Form)
gen_XHTML_Label_Attrs = Generalization(general=Attrs, specific=XHTML_Label)
gen_XHTML_Label_Inlineforms = Generalization(general=Inlineforms, specific=XHTML_Label)
gen_XHTML_Input_Inlineforms = Generalization(general=Inlineforms, specific=XHTML_Input)
gen_XHTML_Input_EMPTY = Generalization(general=EMPTY, specific=XHTML_Input)
gen_XHTML_Input_Attrs = Generalization(general=Attrs, specific=XHTML_Input)
gen_XHTML_Input_Focus = Generalization(general=Focus, specific=XHTML_Input)
gen_XHTML_Select_Attrs = Generalization(general=Attrs, specific=XHTML_Select)
gen_XHTML_Select_Inlineforms = Generalization(general=Inlineforms, specific=XHTML_Select)
gen_XHTML_Optgroup_SelectElement = Generalization(general=SelectElement, specific=XHTML_Optgroup)
gen_XHTML_Optgroup_Attrs = Generalization(general=Attrs, specific=XHTML_Optgroup)
gen_XHTML_Option_SelectElement = Generalization(general=SelectElement, specific=XHTML_Option)
gen_XHTML_Option_PCDATA = Generalization(general=PCDATA, specific=XHTML_Option)
gen_XHTML_Option_Attrs = Generalization(general=Attrs, specific=XHTML_Option)
gen_XHTML_Textarea_PCDATA = Generalization(general=PCDATA, specific=XHTML_Textarea)
gen_XHTML_Textarea_Attrs = Generalization(general=Attrs, specific=XHTML_Textarea)
gen_XHTML_Textarea_Focus = Generalization(general=Focus, specific=XHTML_Textarea)
gen_XHTML_Textarea_Inlineforms = Generalization(general=Inlineforms, specific=XHTML_Textarea)
gen_XHTML_Fieldset_Attrs = Generalization(general=Attrs, specific=XHTML_Fieldset)
gen_XHTML_Legend_Attrs = Generalization(general=Attrs, specific=XHTML_Legend)
gen_XHTML_Legend_FieldsetElement = Generalization(general=FieldsetElement, specific=XHTML_Legend)
gen_XHTML_Button_Attrs = Generalization(general=Attrs, specific=XHTML_Button)
gen_XHTML_Button_Focus = Generalization(general=Focus, specific=XHTML_Button)
gen_XHTML_Button_Inlineforms = Generalization(general=Inlineforms, specific=XHTML_Button)
gen_XHTML_Fieldset_block = Generalization(general=block, specific=XHTML_Fieldset)
gen_XHTML_Table_Attrs = Generalization(general=Attrs, specific=XHTML_Table)
gen_XHTML_Table_block = Generalization(general=block, specific=XHTML_Table)
gen_XHTML_Table_ButtonContent = Generalization(general=ButtonContent, specific=XHTML_Table)
gen_XHTML_Thead_Attrs = Generalization(general=Attrs, specific=XHTML_Thead)
gen_XHTML_Thead_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Thead)
gen_XHTML_Thead_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Thead)
gen_XHTML_Tfoot_Attrs = Generalization(general=Attrs, specific=XHTML_Tfoot)
gen_XHTML_Tfoot_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Tfoot)
gen_XHTML_Tfoot_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Tfoot)
gen_XHTML_Tbody_Attrs = Generalization(general=Attrs, specific=XHTML_Tbody)
gen_XHTML_Tbody_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Tbody)
gen_XHTML_Tbody_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Tbody)
gen_XHTML_Colgroup_Attrs = Generalization(general=Attrs, specific=XHTML_Colgroup)
gen_XHTML_Colgroup_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Colgroup)
gen_XHTML_Caption_Attrs = Generalization(general=Attrs, specific=XHTML_Caption)
gen_XHTML_Col_EMPTY = Generalization(general=EMPTY, specific=XHTML_Col)
gen_XHTML_Col_Attrs = Generalization(general=Attrs, specific=XHTML_Col)
gen_XHTML_Col_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Col)
gen_XHTML_Col_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Col)
gen_XHTML_Tr_Attrs = Generalization(general=Attrs, specific=XHTML_Tr)
gen_XHTML_Tr_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Tr)
gen_XHTML_Tr_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Tr)
gen_XHTML_Colgroup_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Colgroup)
gen_XHTML_Th_TrElement = Generalization(general=TrElement, specific=XHTML_Th)
gen_XHTML_Th_Attrs = Generalization(general=Attrs, specific=XHTML_Th)
gen_XHTML_Th_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Th)
gen_XHTML_Th_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Th)
gen_XHTML_Td_TrElement = Generalization(general=TrElement, specific=XHTML_Td)
gen_XHTML_Td_Attrs = Generalization(general=Attrs, specific=XHTML_Td)
gen_XHTML_Td_Cellvalign = Generalization(general=Cellvalign, specific=XHTML_Td)
gen_XHTML_Td_Cellhalign = Generalization(general=Cellhalign, specific=XHTML_Td)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={XHTML_ValuedElement, XHTML_CDATA, ValuedElement, XHTML_PCDATA, XHTML_NMTOKEN, XHTML_IDREF, XHTML_IDREFS, IDREF, XHTML_ID, XHTML_EMPTY, XHTML_ContentType, CDATA, XHTML_ContentTypes, ContentType, XHTML_Charset, XHTML_Charsets, Charset, XHTML_Character, XHTML_Number, XHTML_LinkTypes, XHTML_MediaDesc, XHTML_URI, XHTML_UriList, URI, XHTML_Datetime, XHTML_ScriptExpression, XHTML_StyleSheet, XHTML_Text, XHTML_Length, XHTML_MultiLength, XHTML_Pixels, XHTML_LanguageCode, NMTOKEN, XHTML_Coords, Length, XHTML_CoreAttrs, ID, StyleSheet, Text, XHTML_I18n, LanguageCode, XHTML_Events, ScriptExpression, XHTML_Attrs, CoreAttrs, I18n, Events, XHTML_Focus, Character, Number, XHTML_Specialpre, Special, PreContent, XHTML_Special, inline, ButtonContent, XHTML_Fontstyle, AContent, XHTML_Phrase, XHTML_Inlineforms, XHTML_Miscinline, Misc, Inline, XHTML_Misc, Block, Flow, FormContent, ObjectElement, MapElementContent, FieldsetElement, XHTML_inline, XHTML_Inline, PCDATA, XHTML_Heading, block, XHTML_Lists, XHTML_Blocktext, XHTML_Block, XHTML_Flow, XHTML_AContent, XHTML_PreContent, XHTML_FormContent, XHTML_ButtonContent, XHTML_Html, Head, Body, XHTML_HeadMisc, XHTML_Head, HeadMisc, HeadElement, Html, XHTML_block, XHTML_HeadElement, XHTML_TitleHeadElement, Title, BaseTitleHeadElement, XHTML_BaseTitleHeadElement, Base, XHTML_BaseHeadElement, TitleBaseHeadElement, XHTML_TitleBaseHeadElement, XHTML_Title, XHTML_Base, EMPTY, XHTML_Link, Attrs, LinkTypes, MediaDesc, XHTML_Meta, XHTML_Script, Miscinline, XHTML_Noscript, XHTML_Style, XHTML_Div, XHTML_P, XHTML_H1, Heading, XHTML_H2, XHTML_H3, XHTML_H4, XHTML_H5, XHTML_H6, XHTML_Body, XHTML_Ol, XHTML_Li, XHTML_Dl, DlElement, XHTML_DlElement, XHTML_Dt, XHTML_Dd, XHTML_Address, Blocktext, XHTML_Hr, XHTML_Pre, XHTML_Ul, Lists, Li, XHTML_Blockquote, XHTML_Ins, Datetime, XHTML_Del, XHTML_A, Focus, Coords, XHTML_Span, Specialpre, XHTML_Bdo, XHTML_Br, XHTML_Em, Phrase, XHTML_Strong, XHTML_Dfn, XHTML_Code, XHTML_Samp, XHTML_Kbd, XHTML_Var, XHTML_Cite, XHTML_Abbr, XHTML_Acronym, XHTML_Q, XHTML_Sub, XHTML_Sup, XHTML_Tt, Fontstyle, XHTML_I, XHTML_B, XHTML_Big, XHTML_Small, XHTML_ObjectElement, XHTML_Object, UriList, XHTML_Param, XHTML_Img, XHTML_MapContent, MapElement, XHTML_MapElement, XHTML_MapElementContent, XHTML_Map, MapContent, XHTML_Area, XHTML_Form, ContentTypes, Charsets, XHTML_Label, XHTML_Input, Inlineforms, XHTML_Select, SelectElement, XHTML_SelectElement, XHTML_Optgroup, XHTML_Option, XHTML_Textarea, Option, XHTML_FieldsetElement, XHTML_Fieldset, XHTML_Legend, XHTML_Button, XHTML_Cellhalign, XHTML_Cellvalign, XHTML_Table, Caption, Thead, Tfoot, TableElement, ColElement, XHTML_ColElement, Col, Colgroup, XHTML_TableElement, Tbody, Tr, Pixels, XHTML_Thead, Cellhalign, Cellvalign, XHTML_Tfoot, XHTML_Tbody, XHTML_Colgroup, XHTML_Caption, MultiLength, XHTML_Col, XHTML_Tr, TrElement, IDREFS, XHTML_TrElement, XHTML_Th, XHTML_Td, Shape, Direction, ValueType, FomeMethod, InputType, ButtonType, TFrame, TRules, CellHAlign, CellVAlign, Scope},
    associations={idrefs0, contentTypes1, charsets2, uris3, lengths4, id5, class_6, style8, title10, lang12, xml_lang13, onclick16, ondblclick17, onmouseup23, onmouseover26, onmousemove29, onmouseout32, onkeypress35, onkeydown38, onkeyup41, accesskey44, tabindex45, onfocus47, onblur50, onmousedown20, pcdataInline53, pcdataFlow54, pcdataAContent56, pcdataPreContent58, pcdataButtonContent60, i18n62, id63, xmlns66, head69, body70, i18n72, id74, profile77, headmisc80, headelement82, html84, title85, headmisc86, baseTitleHeadElement89, base91, headmisc92, base95, headmisc97, titleBaseHeadElement100, title102, headmisc104, i18n107, id109, href112, i18n117, id119, httpequiv122, name125, content128, scheme131, charset134, href136, hreflang139, type142, rel145, rev147, id114, i18n152, id154, type157, media160, title163, id166, charset168, type171, src174, block177, media150, onload180, onunload183, html186, divElements188, pElements189, h1Elements190, h2Elements192, h3Elements194, h4Elements196, h5Elements198, h6Elements200, bodyElements178, li203, liElements205, dlElements207, dtElements208, ddElements210, addressElements212, li202, blockquoteElements215, cite217, flowelement220, cite222, datetime225, flowelement227, cite229, datetime232, preElements214, acontent235, charset236, type239, name242, href244, hreflang247, rel250, rev253, coords256, spanElements258, bdoElements260, lang262, xml_lang265, emElements268, strongElements270, dfnElements272, sampElements276, kbdElements278, varElements280, citeElements282, abbrElements284, acronymElements286, qElements288, cite290, subElements293, codeElements274, ttElements297, iElements299, bElements301, bigElements303, smallElements305, objectpcdata307, objectelement309, supElements295, classid310, codebase313, data316, type319, codetype322, archive325, standby327, height330, width333, usemap336, name339, tabindex342, id345, value350, type353, src356, alt358, longdesc361, height364, width367, name347, mapElements373, mapelement374, usemap370, style381, title384, name387, coords390, href392, alt395, id375, class_378, formelement398, action399, enctype402, onsubmit405, onreset408, accept411, accept_charset413, for_417, accesskey420, onfocus423, onblur426, labelelements415, name429, value431, size434, maxlength437, src440, alt443, usemap446, onselect449, onchange452, accept455, selectelement458, size462, tabindex465, onfocus468, onblur471, onchange474, name459, options477, label478, label481, optionvalue483, rows488, cols491, onselect494, onchange497, fieldsetpcdata500, name486, fieldsetelements502, legendelement503, accesskey505, buttoncontent508, value512, name509, char515, charoff517, caption520, colelement521, thead523, tfoot525, tableelement527, summary529, width532, cellspacing537, cellpadding540, cols543, colgroup544, tbody546, tr547, border535, captionelement549, tr551, tr553, tr555, cols557, span559, width562, span564, width566, headers578, rowspan580, thelement570, abbr572, axis575, trelements569, colspan583, tdelement586, headers594, abbr588, rowspan597, axis591, colspan600},
    generalizations={gen_XHTML_CDATA_ValuedElement, gen_XHTML_PCDATA_ValuedElement, gen_XHTML_NMTOKEN_ValuedElement, gen_XHTML_IDREF_ValuedElement, gen_XHTML_ID_ValuedElement, gen_XHTML_ContentType_CDATA, gen_XHTML_Charset_CDATA, gen_XHTML_Character_CDATA, gen_XHTML_Number_CDATA, gen_XHTML_LinkTypes_CDATA, gen_XHTML_MediaDesc_CDATA, gen_XHTML_URI_CDATA, gen_XHTML_Datetime_CDATA, gen_XHTML_ScriptExpression_CDATA, gen_XHTML_StyleSheet_CDATA, gen_XHTML_Text_CDATA, gen_XHTML_Length_CDATA, gen_XHTML_MultiLength_CDATA, gen_XHTML_Pixels_CDATA, gen_XHTML_LanguageCode_NMTOKEN, gen_XHTML_Attrs_CoreAttrs, gen_XHTML_Attrs_I18n, gen_XHTML_Attrs_Events, gen_XHTML_Specialpre_Special, gen_XHTML_Specialpre_PreContent, gen_XHTML_Special_inline, gen_XHTML_Special_ButtonContent, gen_XHTML_Fontstyle_inline, gen_XHTML_Fontstyle_AContent, gen_XHTML_Fontstyle_PreContent, gen_XHTML_Fontstyle_ButtonContent, gen_XHTML_Phrase_inline, gen_XHTML_Phrase_AContent, gen_XHTML_Phrase_PreContent, gen_XHTML_Phrase_ButtonContent, gen_XHTML_Inlineforms_inline, gen_XHTML_Inlineforms_AContent, gen_XHTML_Inlineforms_PreContent, gen_XHTML_Miscinline_Misc, gen_XHTML_Miscinline_Inline, gen_XHTML_Miscinline_AContent, gen_XHTML_Miscinline_PreContent, gen_XHTML_Misc_Block, gen_XHTML_Misc_Flow, gen_XHTML_Misc_FormContent, gen_XHTML_Misc_ButtonContent, gen_XHTML_Misc_ObjectElement, gen_XHTML_Misc_MapElementContent, gen_XHTML_Misc_FieldsetElement, gen_XHTML_inline_Inline, gen_XHTML_Inline_Flow, gen_XHTML_Inline_ObjectElement, gen_XHTML_Inline_FieldsetElement, gen_XHTML_Heading_block, gen_XHTML_Heading_ButtonContent, gen_XHTML_Lists_block, gen_XHTML_Lists_ButtonContent, gen_XHTML_Blocktext_block, gen_XHTML_Blocktext_ButtonContent, gen_XHTML_block_Block, gen_XHTML_block_Flow, gen_XHTML_block_FormContent, gen_XHTML_block_ObjectElement, gen_XHTML_block_MapElementContent, gen_XHTML_block_FieldsetElement, gen_XHTML_TitleHeadElement_HeadElement, gen_XHTML_BaseHeadElement_HeadElement, gen_XHTML_Title_PCDATA, gen_XHTML_Base_EMPTY, gen_XHTML_Link_EMPTY, gen_XHTML_Link_Attrs, gen_XHTML_Link_HeadMisc, gen_XHTML_Meta_EMPTY, gen_XHTML_Meta_HeadMisc, gen_XHTML_Script_PCDATA, gen_XHTML_Script_Miscinline, gen_XHTML_Script_HeadMisc, gen_XHTML_Noscript_Attrs, gen_XHTML_Noscript_Misc, gen_XHTML_Style_PCDATA, gen_XHTML_Style_HeadMisc, gen_XHTML_Div_Attrs, gen_XHTML_Div_block, gen_XHTML_Div_ButtonContent, gen_XHTML_P_Attrs, gen_XHTML_P_block, gen_XHTML_P_ButtonContent, gen_XHTML_H1_Attrs, gen_XHTML_H1_Heading, gen_XHTML_H2_Attrs, gen_XHTML_H2_Heading, gen_XHTML_H3_Attrs, gen_XHTML_H3_Heading, gen_XHTML_H4_Attrs, gen_XHTML_H4_Heading, gen_XHTML_H5_Attrs, gen_XHTML_H5_Heading, gen_XHTML_H6_Attrs, gen_XHTML_H6_Heading, gen_XHTML_Body_Attrs, gen_XHTML_Ol_Attrs, gen_XHTML_Ol_Lists, gen_XHTML_Li_Attrs, gen_XHTML_Dl_Attrs, gen_XHTML_Dl_Lists, gen_XHTML_DlElement_Attrs, gen_XHTML_Dt_DlElement, gen_XHTML_Dd_DlElement, gen_XHTML_Address_Attrs, gen_XHTML_Address_Blocktext, gen_XHTML_Hr_EMPTY, gen_XHTML_Hr_Attrs, gen_XHTML_Hr_Blocktext, gen_XHTML_Pre_Attrs, gen_XHTML_Pre_Blocktext, gen_XHTML_Ul_Attrs, gen_XHTML_Ul_Lists, gen_XHTML_Blockquote_Attrs, gen_XHTML_Blockquote_Blocktext, gen_XHTML_Ins_Attrs, gen_XHTML_Ins_Miscinline, gen_XHTML_Del_Attrs, gen_XHTML_Del_Miscinline, gen_XHTML_A_Attrs, gen_XHTML_A_Focus, gen_XHTML_A_inline, gen_XHTML_A_PreContent, gen_XHTML_Span_Attrs, gen_XHTML_Span_Specialpre, gen_XHTML_Bdo_CoreAttrs, gen_XHTML_Bdo_Events, gen_XHTML_Bdo_Specialpre, gen_XHTML_Br_EMPTY, gen_XHTML_Br_CoreAttrs, gen_XHTML_Br_Specialpre, gen_XHTML_Em_Attrs, gen_XHTML_Em_Phrase, gen_XHTML_Strong_Attrs, gen_XHTML_Strong_Phrase, gen_XHTML_Dfn_Attrs, gen_XHTML_Dfn_Phrase, gen_XHTML_Code_Attrs, gen_XHTML_Code_Phrase, gen_XHTML_Samp_Attrs, gen_XHTML_Samp_Phrase, gen_XHTML_Kbd_Attrs, gen_XHTML_Kbd_Phrase, gen_XHTML_Var_Attrs, gen_XHTML_Var_Phrase, gen_XHTML_Cite_Attrs, gen_XHTML_Cite_Phrase, gen_XHTML_Abbr_Attrs, gen_XHTML_Abbr_Phrase, gen_XHTML_Acronym_Attrs, gen_XHTML_Acronym_Phrase, gen_XHTML_Q_Attrs, gen_XHTML_Q_Phrase, gen_XHTML_Sub_Attrs, gen_XHTML_Sub_Phrase, gen_XHTML_Tt_Attrs, gen_XHTML_Tt_Fontstyle, gen_XHTML_I_Attrs, gen_XHTML_I_Fontstyle, gen_XHTML_B_Attrs, gen_XHTML_B_Fontstyle, gen_XHTML_Big_Attrs, gen_XHTML_Big_Fontstyle, gen_XHTML_Small_Attrs, gen_XHTML_Small_Fontstyle, gen_XHTML_Object_Attrs, gen_XHTML_Object_Special, gen_XHTML_Object_HeadMisc, gen_XHTML_Sup_Attrs, gen_XHTML_Sup_Phrase, gen_XHTML_Param_EMPTY, gen_XHTML_Param_ObjectElement, gen_XHTML_Img_EMPTY, gen_XHTML_Img_Attrs, gen_XHTML_Img_Special, gen_XHTML_Map_I18n, gen_XHTML_Map_Events, gen_XHTML_Map_Specialpre, gen_XHTML_Area_EMPTY, gen_XHTML_Area_Attrs, gen_XHTML_Area_Focus, gen_XHTML_Area_MapElement, gen_XHTML_Form_Attrs, gen_XHTML_Form_Block, gen_XHTML_Form_ObjectElement, gen_XHTML_Form_MapElementContent, gen_XHTML_Form_FieldsetElement, gen_XHTML_Label_Attrs, gen_XHTML_Label_Inlineforms, gen_XHTML_Input_Inlineforms, gen_XHTML_Input_EMPTY, gen_XHTML_Input_Attrs, gen_XHTML_Input_Focus, gen_XHTML_Select_Attrs, gen_XHTML_Select_Inlineforms, gen_XHTML_Optgroup_SelectElement, gen_XHTML_Optgroup_Attrs, gen_XHTML_Option_SelectElement, gen_XHTML_Option_PCDATA, gen_XHTML_Option_Attrs, gen_XHTML_Textarea_PCDATA, gen_XHTML_Textarea_Attrs, gen_XHTML_Textarea_Focus, gen_XHTML_Textarea_Inlineforms, gen_XHTML_Fieldset_Attrs, gen_XHTML_Legend_Attrs, gen_XHTML_Legend_FieldsetElement, gen_XHTML_Button_Attrs, gen_XHTML_Button_Focus, gen_XHTML_Button_Inlineforms, gen_XHTML_Fieldset_block, gen_XHTML_Table_Attrs, gen_XHTML_Table_block, gen_XHTML_Table_ButtonContent, gen_XHTML_Thead_Attrs, gen_XHTML_Thead_Cellhalign, gen_XHTML_Thead_Cellvalign, gen_XHTML_Tfoot_Attrs, gen_XHTML_Tfoot_Cellhalign, gen_XHTML_Tfoot_Cellvalign, gen_XHTML_Tbody_Attrs, gen_XHTML_Tbody_Cellhalign, gen_XHTML_Tbody_Cellvalign, gen_XHTML_Colgroup_Attrs, gen_XHTML_Colgroup_Cellhalign, gen_XHTML_Caption_Attrs, gen_XHTML_Col_EMPTY, gen_XHTML_Col_Attrs, gen_XHTML_Col_Cellhalign, gen_XHTML_Col_Cellvalign, gen_XHTML_Tr_Attrs, gen_XHTML_Tr_Cellhalign, gen_XHTML_Tr_Cellvalign, gen_XHTML_Colgroup_Cellvalign, gen_XHTML_Th_TrElement, gen_XHTML_Th_Attrs, gen_XHTML_Th_Cellvalign, gen_XHTML_Th_Cellhalign, gen_XHTML_Td_TrElement, gen_XHTML_Td_Attrs, gen_XHTML_Td_Cellvalign, gen_XHTML_Td_Cellhalign},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)