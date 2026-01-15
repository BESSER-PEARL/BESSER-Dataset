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
ButtonType: Enumeration = Enumeration(
    name="ButtonType",
    literals={
            EnumerationLiteral(name="Submit"),
			EnumerationLiteral(name="Reset"),
			EnumerationLiteral(name="Push")
    }
)

EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="onload"),
			EnumerationLiteral(name="onunload"),
			EnumerationLiteral(name="onclick"),
			EnumerationLiteral(name="ondblclick"),
			EnumerationLiteral(name="onmousedown"),
			EnumerationLiteral(name="onmouseup"),
			EnumerationLiteral(name="onmouseover"),
			EnumerationLiteral(name="onmousemove"),
			EnumerationLiteral(name="onmouseout"),
			EnumerationLiteral(name="onfocus"),
			EnumerationLiteral(name="onblur"),
			EnumerationLiteral(name="onkeypress"),
			EnumerationLiteral(name="onkeydown"),
			EnumerationLiteral(name="onkeyup"),
			EnumerationLiteral(name="onsubmit"),
			EnumerationLiteral(name="onreset"),
			EnumerationLiteral(name="onselect"),
			EnumerationLiteral(name="onchange")
    }
)

ScriptType: Enumeration = Enumeration(
    name="ScriptType",
    literals={
            EnumerationLiteral(name="textJavaScript"),
			EnumerationLiteral(name="textTcl"),
			EnumerationLiteral(name="textVBScript")
    }
)

SubmitFormMethod: Enumeration = Enumeration(
    name="SubmitFormMethod",
    literals={
            EnumerationLiteral(name="post"),
			EnumerationLiteral(name="get")
    }
)

Align: Enumeration = Enumeration(
    name="Align",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="justify")
    }
)

HeadingLevel: Enumeration = Enumeration(
    name="HeadingLevel",
    literals={
            EnumerationLiteral(name="h1"),
			EnumerationLiteral(name="h2"),
			EnumerationLiteral(name="h3"),
			EnumerationLiteral(name="h4"),
			EnumerationLiteral(name="h5"),
			EnumerationLiteral(name="h6")
    }
)

PhraseElementType: Enumeration = Enumeration(
    name="PhraseElementType",
    literals={
            EnumerationLiteral(name="Emphasis"),
			EnumerationLiteral(name="StrongerEmphasis"),
			EnumerationLiteral(name="Citation"),
			EnumerationLiteral(name="Definition"),
			EnumerationLiteral(name="ComputerCode"),
			EnumerationLiteral(name="SampleProgramOutput"),
			EnumerationLiteral(name="EntryFromUser"),
			EnumerationLiteral(name="VariableInstance"),
			EnumerationLiteral(name="Abbreviation"),
			EnumerationLiteral(name="Acronym"),
			EnumerationLiteral(name="None")
    }
)

ObjectAlign: Enumeration = Enumeration(
    name="ObjectAlign",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="baseline"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="textTop"),
			EnumerationLiteral(name="absoluteMiddle"),
			EnumerationLiteral(name="absoluteBottom"),
			EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

DateFormat: Enumeration = Enumeration(
    name="DateFormat",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="ISO8601"),
			EnumerationLiteral(name="Short"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Full")
    }
)

Locale: Enumeration = Enumeration(
    name="Locale",
    literals={
            EnumerationLiteral(name="English_UK"),
			EnumerationLiteral(name="Spanish"),
			EnumerationLiteral(name="German"),
			EnumerationLiteral(name="Portuguese_Brazilian")
    }
)

MatchingOperator: Enumeration = Enumeration(
    name="MatchingOperator",
    literals={
            EnumerationLiteral(name="Equals"),
			EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="LessThan"),
			EnumerationLiteral(name="GreaterOrEqualsThan"),
			EnumerationLiteral(name="LessOrEqualsThan"),
			EnumerationLiteral(name="Different"),
			EnumerationLiteral(name="Contains")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="Vertical"),
			EnumerationLiteral(name="Horizontal")
    }
)

OrderedListType: Enumeration = Enumeration(
    name="OrderedListType",
    literals={
            EnumerationLiteral(name="ArabicNumber"),
			EnumerationLiteral(name="LowerAlpha"),
			EnumerationLiteral(name="UpperAlpha"),
			EnumerationLiteral(name="LowerRoman"),
			EnumerationLiteral(name="UpperRoman"),
			EnumerationLiteral(name="none")
    }
)

UnorderedListType: Enumeration = Enumeration(
    name="UnorderedListType",
    literals={
            EnumerationLiteral(name="disc"),
			EnumerationLiteral(name="circle"),
			EnumerationLiteral(name="square"),
			EnumerationLiteral(name="none")
    }
)

Extension: Enumeration = Enumeration(
    name="Extension",
    literals={
            EnumerationLiteral(name="html"),
			EnumerationLiteral(name="xhtml"),
			EnumerationLiteral(name="jsp"),
			EnumerationLiteral(name="php"),
			EnumerationLiteral(name="asp")
    }
)

FieldSetLegendAlign: Enumeration = Enumeration(
    name="FieldSetLegendAlign",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="top")
    }
)

MessageDialogEvent: Enumeration = Enumeration(
    name="MessageDialogEvent",
    literals={
            EnumerationLiteral(name="closeDialog")
    }
)

# Classes
ric_IdentifiableComponent = Class(name="ric::IdentifiableComponent", is_abstract=True)
ric_ClassifiableComponent = Class(name="ric::ClassifiableComponent", is_abstract=True)
ric_EventComponent = Class(name="ric::EventComponent", is_abstract=True)
ric_Event = Class(name="ric::Event")
ric_FormControl = Class(name="ric::FormControl", is_abstract=True)
IdentifiableComponent = Class(name="IdentifiableComponent")
ClassifiableComponent = Class(name="ClassifiableComponent")
EventComponent = Class(name="EventComponent")
ric_Label = Class(name="ric::Label")
ric_PhraseElement = Class(name="ric::PhraseElement")
ric_ValueConstraint = Class(name="ric::ValueConstraint")
ric_NumberValueConstraint = Class(name="ric::NumberValueConstraint")
ric_RequiredFieldConstraint = Class(name="ric::RequiredFieldConstraint")
ric_ValidDateConstraint = Class(name="ric::ValidDateConstraint")
ric_Button = Class(name="ric::Button")
FormControl = Class(name="FormControl")
ric_TextArea = Class(name="ric::TextArea")
ric_Form = Class(name="ric::Form")
ric_Document = Class(name="ric::Document")
ric_Fieldset = Class(name="ric::Fieldset")
ric_BlockLevelComponent = Class(name="ric::BlockLevelComponent", is_abstract=True)
ric_InlineComponent = Class(name="ric::InlineComponent", is_abstract=True)
ric_TextField = Class(name="ric::TextField")
ric_InputFile = Class(name="ric::InputFile")
ric_Script = Class(name="ric::Script")
ric_Checkbox = Class(name="ric::Checkbox")
ric_Radio = Class(name="ric::Radio")
ric_Select = Class(name="ric::Select")
ric_RichWidget = Class(name="ric::RichWidget", is_abstract=True)
ric_SelectItem = Class(name="ric::SelectItem")
ric_RadioGroup = Class(name="ric::RadioGroup")
ric_CheckGroup = Class(name="ric::CheckGroup")
ric_Div = Class(name="ric::Div")
BlockLevelComponent = Class(name="BlockLevelComponent")
ric_ObjectComponent = Class(name="ric::ObjectComponent", is_abstract=True)
ric_LineBreak = Class(name="ric::LineBreak")
ric_List = Class(name="ric::List", is_abstract=True)
ric_Span = Class(name="ric::Span")
InlineComponent = Class(name="InlineComponent")
ric_Heading = Class(name="ric::Heading")
ric_Paragraph = Class(name="ric::Paragraph")
ric_Link = Class(name="ric::Link")
ric_Image = Class(name="ric::Image")
ObjectComponent = Class(name="ObjectComponent")
ric_TabbedPanel = Class(name="ric::TabbedPanel")
RichWidget = Class(name="RichWidget")
ric_Tab = Class(name="ric::Tab")
ric_AccordionPanel = Class(name="ric::AccordionPanel")
ric_Section = Class(name="ric::Section")
ric_MessageDialog = Class(name="ric::MessageDialog")
ric_MessageDialogButton = Class(name="ric::MessageDialogButton")
ric_Datepicker = Class(name="ric::Datepicker")
TextField = Class(name="TextField")
ric_FormControlConstraint = Class(name="ric::FormControlConstraint", is_abstract=True)
FormControlConstraint = Class(name="FormControlConstraint")
ric_Portal = Class(name="ric::Portal")
ric_HeaderRegion = Class(name="ric::HeaderRegion")
ric_NavigationRegion = Class(name="ric::NavigationRegion")
ric_ContextualNavigationRegion = Class(name="ric::ContextualNavigationRegion")
ric_SearchRegion = Class(name="ric::SearchRegion")
ric_ContentRegion = Class(name="ric::ContentRegion")
ric_FooterRegion = Class(name="ric::FooterRegion")
ric_Logo = Class(name="ric::Logo")
ric_LinkGroup = Class(name="ric::LinkGroup")
ric_OrderedList = Class(name="ric::OrderedList")
List = Class(name="List")
ric_ListItem = Class(name="ric::ListItem")
ric_UnorderedList = Class(name="ric::UnorderedList")

# ric_IdentifiableComponent class attributes and methods
ric_IdentifiableComponent_id: Property = Property(name="id", type=StringType)
ric_IdentifiableComponent.attributes={ric_IdentifiableComponent_id}

# ric_ClassifiableComponent class attributes and methods
ric_ClassifiableComponent_class: Property = Property(name="class", type=StringType)
ric_ClassifiableComponent.attributes={ric_ClassifiableComponent_class}

# ric_EventComponent class attributes and methods

# ric_Event class attributes and methods
ric_Event_type: Property = Property(name="type", type=StringType)
ric_Event.attributes={ric_Event_type}

# ric_FormControl class attributes and methods
ric_FormControl_name: Property = Property(name="name", type=StringType)
ric_FormControl_value: Property = Property(name="value", type=StringType)
ric_FormControl.attributes={ric_FormControl_name, ric_FormControl_value}

# IdentifiableComponent class attributes and methods

# ClassifiableComponent class attributes and methods

# EventComponent class attributes and methods

# ric_Label class attributes and methods
ric_Label_text: Property = Property(name="text", type=StringType)
ric_Label_format: Property = Property(name="format", type=StringType)
ric_Label.attributes={ric_Label_text, ric_Label_format}

# ric_PhraseElement class attributes and methods
ric_PhraseElement_phraseType: Property = Property(name="phraseType", type=StringType)
ric_PhraseElement_title: Property = Property(name="title", type=StringType)
ric_PhraseElement.attributes={ric_PhraseElement_phraseType, ric_PhraseElement_title}

# ric_ValueConstraint class attributes and methods
ric_ValueConstraint_matchingOperator: Property = Property(name="matchingOperator", type=StringType)
ric_ValueConstraint_matchingValue: Property = Property(name="matchingValue", type=StringType)
ric_ValueConstraint_logicalOperator: Property = Property(name="logicalOperator", type=StringType)
ric_ValueConstraint.attributes={ric_ValueConstraint_matchingOperator, ric_ValueConstraint_matchingValue, ric_ValueConstraint_logicalOperator}

# ric_NumberValueConstraint class attributes and methods

# ric_RequiredFieldConstraint class attributes and methods

# ric_ValidDateConstraint class attributes and methods
ric_ValidDateConstraint_dateFormat: Property = Property(name="dateFormat", type=StringType)
ric_ValidDateConstraint.attributes={ric_ValidDateConstraint_dateFormat}

# ric_Button class attributes and methods
ric_Button_type: Property = Property(name="type", type=StringType)
ric_Button_disabled: Property = Property(name="disabled", type=BooleanType)
ric_Button_image: Property = Property(name="image", type=StringType)
ric_Button.attributes={ric_Button_image, ric_Button_type, ric_Button_disabled}

# FormControl class attributes and methods

# ric_TextArea class attributes and methods
ric_TextArea_cols: Property = Property(name="cols", type=IntegerType)
ric_TextArea_rols: Property = Property(name="rols", type=IntegerType)
ric_TextArea_readonly: Property = Property(name="readonly", type=BooleanType)
ric_TextArea.attributes={ric_TextArea_rols, ric_TextArea_readonly, ric_TextArea_cols}

# ric_Form class attributes and methods
ric_Form_name: Property = Property(name="name", type=StringType)
ric_Form_method: Property = Property(name="method", type=StringType)
ric_Form.attributes={ric_Form_method, ric_Form_name}

# ric_Document class attributes and methods
ric_Document_title: Property = Property(name="title", type=StringType)
ric_Document_index: Property = Property(name="index", type=BooleanType)
ric_Document_fileName: Property = Property(name="fileName", type=StringType)
ric_Document.attributes={ric_Document_index, ric_Document_fileName, ric_Document_title}

# ric_Fieldset class attributes and methods
ric_Fieldset_legend: Property = Property(name="legend", type=StringType)
ric_Fieldset_legendAlign: Property = Property(name="legendAlign", type=StringType)
ric_Fieldset_legendFormat: Property = Property(name="legendFormat", type=StringType)
ric_Fieldset.attributes={ric_Fieldset_legendAlign, ric_Fieldset_legend, ric_Fieldset_legendFormat}

# ric_BlockLevelComponent class attributes and methods

# ric_InlineComponent class attributes and methods
ric_InlineComponent_text: Property = Property(name="text", type=StringType)
ric_InlineComponent.attributes={ric_InlineComponent_text}

# ric_TextField class attributes and methods
ric_TextField_charWidth: Property = Property(name="charWidth", type=IntegerType)
ric_TextField_maxChars: Property = Property(name="maxChars", type=IntegerType)
ric_TextField_readonly: Property = Property(name="readonly", type=BooleanType)
ric_TextField_password: Property = Property(name="password", type=BooleanType)
ric_TextField.attributes={ric_TextField_maxChars, ric_TextField_readonly, ric_TextField_charWidth, ric_TextField_password}

# ric_InputFile class attributes and methods
ric_InputFile_maxChars: Property = Property(name="maxChars", type=IntegerType)
ric_InputFile_readonly: Property = Property(name="readonly", type=BooleanType)
ric_InputFile_charWidth: Property = Property(name="charWidth", type=IntegerType)
ric_InputFile.attributes={ric_InputFile_readonly, ric_InputFile_maxChars, ric_InputFile_charWidth}

# ric_Script class attributes and methods
ric_Script_name: Property = Property(name="name", type=StringType)
ric_Script_type: Property = Property(name="type", type=StringType)
ric_Script_implementation: Property = Property(name="implementation", type=StringType)
ric_Script.attributes={ric_Script_type, ric_Script_implementation, ric_Script_name}

# ric_Checkbox class attributes and methods
ric_Checkbox_checked: Property = Property(name="checked", type=BooleanType)
ric_Checkbox.attributes={ric_Checkbox_checked}

# ric_Radio class attributes and methods
ric_Radio_checked: Property = Property(name="checked", type=BooleanType)
ric_Radio.attributes={ric_Radio_checked}

# ric_Select class attributes and methods
ric_Select_size: Property = Property(name="size", type=IntegerType)
ric_Select_multiple: Property = Property(name="multiple", type=BooleanType)
ric_Select.attributes={ric_Select_multiple, ric_Select_size}

# ric_RichWidget class attributes and methods

# ric_SelectItem class attributes and methods
ric_SelectItem_itemLabel: Property = Property(name="itemLabel", type=StringType)
ric_SelectItem_value: Property = Property(name="value", type=StringType)
ric_SelectItem_selected: Property = Property(name="selected", type=BooleanType)
ric_SelectItem.attributes={ric_SelectItem_itemLabel, ric_SelectItem_selected, ric_SelectItem_value}

# ric_RadioGroup class attributes and methods
ric_RadioGroup_orientation: Property = Property(name="orientation", type=StringType)
ric_RadioGroup.attributes={ric_RadioGroup_orientation}

# ric_CheckGroup class attributes and methods
ric_CheckGroup_orientation: Property = Property(name="orientation", type=StringType)
ric_CheckGroup.attributes={ric_CheckGroup_orientation}

# ric_Div class attributes and methods
ric_Div_align: Property = Property(name="align", type=StringType)
ric_Div.attributes={ric_Div_align}

# BlockLevelComponent class attributes and methods

# ric_ObjectComponent class attributes and methods
ric_ObjectComponent_align: Property = Property(name="align", type=StringType)
ric_ObjectComponent_width: Property = Property(name="width", type=IntegerType)
ric_ObjectComponent_height: Property = Property(name="height", type=IntegerType)
ric_ObjectComponent_border: Property = Property(name="border", type=IntegerType)
ric_ObjectComponent_hspace: Property = Property(name="hspace", type=IntegerType)
ric_ObjectComponent_vspace: Property = Property(name="vspace", type=IntegerType)
ric_ObjectComponent.attributes={ric_ObjectComponent_height, ric_ObjectComponent_align, ric_ObjectComponent_border, ric_ObjectComponent_width, ric_ObjectComponent_hspace, ric_ObjectComponent_vspace}

# ric_LineBreak class attributes and methods

# ric_List class attributes and methods

# ric_Span class attributes and methods
ric_Span_align: Property = Property(name="align", type=StringType)
ric_Span.attributes={ric_Span_align}

# InlineComponent class attributes and methods

# ric_Heading class attributes and methods
ric_Heading_level: Property = Property(name="level", type=StringType)
ric_Heading.attributes={ric_Heading_level}

# ric_Paragraph class attributes and methods
ric_Paragraph_align: Property = Property(name="align", type=StringType)
ric_Paragraph.attributes={ric_Paragraph_align}

# ric_Link class attributes and methods
ric_Link_title: Property = Property(name="title", type=StringType)
ric_Link.attributes={ric_Link_title}

# ric_Image class attributes and methods
ric_Image_src: Property = Property(name="src", type=StringType)
ric_Image_alt: Property = Property(name="alt", type=StringType)
ric_Image.attributes={ric_Image_alt, ric_Image_src}

# ObjectComponent class attributes and methods

# ric_TabbedPanel class attributes and methods

# RichWidget class attributes and methods

# ric_Tab class attributes and methods
ric_Tab_title: Property = Property(name="title", type=StringType)
ric_Tab.attributes={ric_Tab_title}

# ric_AccordionPanel class attributes and methods

# ric_Section class attributes and methods
ric_Section_title: Property = Property(name="title", type=StringType)
ric_Section.attributes={ric_Section_title}

# ric_MessageDialog class attributes and methods
ric_MessageDialog_title: Property = Property(name="title", type=StringType)
ric_MessageDialog_message: Property = Property(name="message", type=StringType)
ric_MessageDialog_modal: Property = Property(name="modal", type=BooleanType)
ric_MessageDialog_autoOpen: Property = Property(name="autoOpen", type=BooleanType)
ric_MessageDialog_resizable: Property = Property(name="resizable", type=BooleanType)
ric_MessageDialog_height: Property = Property(name="height", type=IntegerType)
ric_MessageDialog_minHeightResize: Property = Property(name="minHeightResize", type=IntegerType)
ric_MessageDialog_maxHeightResize: Property = Property(name="maxHeightResize", type=IntegerType)
ric_MessageDialog_width: Property = Property(name="width", type=IntegerType)
ric_MessageDialog_minWidthResize: Property = Property(name="minWidthResize", type=IntegerType)
ric_MessageDialog_maxWidthResize: Property = Property(name="maxWidthResize", type=IntegerType)
ric_MessageDialog.attributes={ric_MessageDialog_minWidthResize, ric_MessageDialog_maxHeightResize, ric_MessageDialog_message, ric_MessageDialog_modal, ric_MessageDialog_height, ric_MessageDialog_autoOpen, ric_MessageDialog_maxWidthResize, ric_MessageDialog_width, ric_MessageDialog_resizable, ric_MessageDialog_minHeightResize, ric_MessageDialog_title}

# ric_MessageDialogButton class attributes and methods
ric_MessageDialogButton_label: Property = Property(name="label", type=StringType)
ric_MessageDialogButton_event: Property = Property(name="event", type=StringType)
ric_MessageDialogButton.attributes={ric_MessageDialogButton_label, ric_MessageDialogButton_event}

# ric_Datepicker class attributes and methods
ric_Datepicker_showMonthMenu: Property = Property(name="showMonthMenu", type=BooleanType)
ric_Datepicker_showYearMenu: Property = Property(name="showYearMenu", type=BooleanType)
ric_Datepicker_showButtonImage: Property = Property(name="showButtonImage", type=BooleanType)
ric_Datepicker_dateFormat: Property = Property(name="dateFormat", type=StringType)
ric_Datepicker_locale: Property = Property(name="locale", type=StringType)
ric_Datepicker_numberMonthsToShow: Property = Property(name="numberMonthsToShow", type=IntegerType)
ric_Datepicker_showWeekOfYear: Property = Property(name="showWeekOfYear", type=BooleanType)
ric_Datepicker_showButtonClosePanel: Property = Property(name="showButtonClosePanel", type=BooleanType)
ric_Datepicker.attributes={ric_Datepicker_showWeekOfYear, ric_Datepicker_dateFormat, ric_Datepicker_showButtonImage, ric_Datepicker_showYearMenu, ric_Datepicker_showButtonClosePanel, ric_Datepicker_numberMonthsToShow, ric_Datepicker_showMonthMenu, ric_Datepicker_locale}

# TextField class attributes and methods

# ric_FormControlConstraint class attributes and methods

# FormControlConstraint class attributes and methods

# ric_Portal class attributes and methods
ric_Portal_name: Property = Property(name="name", type=StringType)
ric_Portal_documentsExtension: Property = Property(name="documentsExtension", type=StringType)
ric_Portal.attributes={ric_Portal_name, ric_Portal_documentsExtension}

# ric_HeaderRegion class attributes and methods

# ric_NavigationRegion class attributes and methods
ric_NavigationRegion_orientation: Property = Property(name="orientation", type=StringType)
ric_NavigationRegion.attributes={ric_NavigationRegion_orientation}

# ric_ContextualNavigationRegion class attributes and methods

# ric_SearchRegion class attributes and methods

# ric_ContentRegion class attributes and methods

# ric_FooterRegion class attributes and methods

# ric_Logo class attributes and methods

# ric_LinkGroup class attributes and methods
ric_LinkGroup_title: Property = Property(name="title", type=StringType)
ric_LinkGroup.attributes={ric_LinkGroup_title}

# ric_OrderedList class attributes and methods
ric_OrderedList_type: Property = Property(name="type", type=StringType)
ric_OrderedList.attributes={ric_OrderedList_type}

# List class attributes and methods

# ric_ListItem class attributes and methods
ric_ListItem_text: Property = Property(name="text", type=StringType)
ric_ListItem_format: Property = Property(name="format", type=StringType)
ric_ListItem.attributes={ric_ListItem_text, ric_ListItem_format}

# ric_UnorderedList class attributes and methods
ric_UnorderedList_type: Property = Property(name="type", type=StringType)
ric_UnorderedList.attributes={ric_UnorderedList_type}

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="ric_Event", type=ric_EventComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_EventComponent", type=ric_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label1: BinaryAssociation = BinaryAssociation(
    name="label1",
    ends={
        Property(name="ric_Label", type=ric_FormControl, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FormControl", type=ric_Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accompanyingPhrase2: BinaryAssociation = BinaryAssociation(
    name="accompanyingPhrase2",
    ends={
        Property(name="ric_PhraseElement", type=ric_FormControl, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FormControl3", type=ric_PhraseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueConstraints4: BinaryAssociation = BinaryAssociation(
    name="valueConstraints4",
    ends={
        Property(name="ric_ValueConstraint", type=ric_FormControl, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FormControl5", type=ric_ValueConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
numberConstraint6: BinaryAssociation = BinaryAssociation(
    name="numberConstraint6",
    ends={
        Property(name="ric_NumberValueConstraint", type=ric_FormControl, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FormControl7", type=ric_NumberValueConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredFieldConstraint8: BinaryAssociation = BinaryAssociation(
    name="requiredFieldConstraint8",
    ends={
        Property(name="ric_RequiredFieldConstraint", type=ric_FormControl, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FormControl9", type=ric_RequiredFieldConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validDateConstraint10: BinaryAssociation = BinaryAssociation(
    name="validDateConstraint10",
    ends={
        Property(name="ric_ValidDateConstraint", type=ric_FormControl, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FormControl11", type=ric_ValidDateConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggerScript12: BinaryAssociation = BinaryAssociation(
    name="triggerScript12",
    ends={
        Property(name="ric_Script", type=ric_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Event13", type=ric_Script, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action14: BinaryAssociation = BinaryAssociation(
    name="action14",
    ends={
        Property(name="ric_Document", type=ric_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Form", type=ric_Document, multiplicity=Multiplicity(1, 1))
    }
)
fieldsets15: BinaryAssociation = BinaryAssociation(
    name="fieldsets15",
    ends={
        Property(name="ric_Fieldset", type=ric_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Form16", type=ric_Fieldset, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
blockLevelComponents17: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents17",
    ends={
        Property(name="ric_BlockLevelComponent", type=ric_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Form18", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineComponents19: BinaryAssociation = BinaryAssociation(
    name="inlineComponents19",
    ends={
        Property(name="ric_InlineComponent", type=ric_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Form20", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items21: BinaryAssociation = BinaryAssociation(
    name="items21",
    ends={
        Property(name="ric_SelectItem", type=ric_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Select", type=ric_SelectItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
richWidgets35: BinaryAssociation = BinaryAssociation(
    name="richWidgets35",
    ends={
        Property(name="ric_RichWidget", type=ric_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Div36", type=ric_RichWidget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events22: BinaryAssociation = BinaryAssociation(
    name="events22",
    ends={
        Property(name="ric_Event24", type=ric_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Label23", type=ric_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls25: BinaryAssociation = BinaryAssociation(
    name="controls25",
    ends={
        Property(name="ric_FormControl27", type=ric_Fieldset, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Fieldset26", type=ric_FormControl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
radioGroups28: BinaryAssociation = BinaryAssociation(
    name="radioGroups28",
    ends={
        Property(name="ric_RadioGroup", type=ric_Fieldset, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Fieldset29", type=ric_RadioGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkGroups30: BinaryAssociation = BinaryAssociation(
    name="checkGroups30",
    ends={
        Property(name="ric_CheckGroup", type=ric_Fieldset, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Fieldset31", type=ric_CheckGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectComponents32: BinaryAssociation = BinaryAssociation(
    name="objectComponents32",
    ends={
        Property(name="ric_ObjectComponent", type=ric_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Div", type=ric_ObjectComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks33: BinaryAssociation = BinaryAssociation(
    name="lineBreaks33",
    ends={
        Property(name="ric_LineBreak", type=ric_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Div34", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lists37: BinaryAssociation = BinaryAssociation(
    name="lists37",
    ends={
        Property(name="ric_List", type=ric_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Div38", type=ric_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms39: BinaryAssociation = BinaryAssociation(
    name="forms39",
    ends={
        Property(name="ric_Form41", type=ric_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Div40", type=ric_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldsets42: BinaryAssociation = BinaryAssociation(
    name="fieldsets42",
    ends={
        Property(name="ric_Fieldset44", type=ric_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Div43", type=ric_Fieldset, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
blockLevelComponents46: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents46",
    ends={
        Property(name="ric_BlockLevelComponent47", type=ric_BlockLevelComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_BlockLevelComponent45", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineComponents48: BinaryAssociation = BinaryAssociation(
    name="inlineComponents48",
    ends={
        Property(name="ric_InlineComponent50", type=ric_BlockLevelComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_BlockLevelComponent49", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineComponents52: BinaryAssociation = BinaryAssociation(
    name="inlineComponents52",
    ends={
        Property(name="ric_InlineComponent53", type=ric_InlineComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_InlineComponent51", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lists72: BinaryAssociation = BinaryAssociation(
    name="lists72",
    ends={
        Property(name="ric_List74", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab73", type=ric_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target54: BinaryAssociation = BinaryAssociation(
    name="target54",
    ends={
        Property(name="ric_Document55", type=ric_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Link", type=ric_Document, multiplicity=Multiplicity(1, 1))
    }
)
tabs56: BinaryAssociation = BinaryAssociation(
    name="tabs56",
    ends={
        Property(name="ric_Tab", type=ric_TabbedPanel, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_TabbedPanel", type=ric_Tab, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inlineComponents57: BinaryAssociation = BinaryAssociation(
    name="inlineComponents57",
    ends={
        Property(name="ric_InlineComponent59", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab58", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockLevelComponents60: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents60",
    ends={
        Property(name="ric_BlockLevelComponent62", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab61", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectComponents63: BinaryAssociation = BinaryAssociation(
    name="objectComponents63",
    ends={
        Property(name="ric_ObjectComponent65", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab64", type=ric_ObjectComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks66: BinaryAssociation = BinaryAssociation(
    name="lineBreaks66",
    ends={
        Property(name="ric_LineBreak68", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab67", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
richWidgets69: BinaryAssociation = BinaryAssociation(
    name="richWidgets69",
    ends={
        Property(name="ric_RichWidget71", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab70", type=ric_RichWidget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms75: BinaryAssociation = BinaryAssociation(
    name="forms75",
    ends={
        Property(name="ric_Form77", type=ric_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Tab76", type=ric_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections78: BinaryAssociation = BinaryAssociation(
    name="sections78",
    ends={
        Property(name="ric_Section", type=ric_AccordionPanel, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_AccordionPanel", type=ric_Section, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inlineComponents79: BinaryAssociation = BinaryAssociation(
    name="inlineComponents79",
    ends={
        Property(name="ric_InlineComponent81", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section80", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockLevelComponents82: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents82",
    ends={
        Property(name="ric_BlockLevelComponent84", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section83", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectComponents85: BinaryAssociation = BinaryAssociation(
    name="objectComponents85",
    ends={
        Property(name="ric_ObjectComponent87", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section86", type=ric_ObjectComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks88: BinaryAssociation = BinaryAssociation(
    name="lineBreaks88",
    ends={
        Property(name="ric_LineBreak90", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section89", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
richWidgets91: BinaryAssociation = BinaryAssociation(
    name="richWidgets91",
    ends={
        Property(name="ric_RichWidget93", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section92", type=ric_RichWidget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lists94: BinaryAssociation = BinaryAssociation(
    name="lists94",
    ends={
        Property(name="ric_List96", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section95", type=ric_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms97: BinaryAssociation = BinaryAssociation(
    name="forms97",
    ends={
        Property(name="ric_Form99", type=ric_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Section98", type=ric_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buttons100: BinaryAssociation = BinaryAssociation(
    name="buttons100",
    ends={
        Property(name="ric_MessageDialogButton", type=ric_MessageDialog, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_MessageDialog", type=ric_MessageDialogButton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subsiteNavigation114: BinaryAssociation = BinaryAssociation(
    name="subsiteNavigation114",
    ends={
        Property(name="ric_NavigationRegion116", type=ric_HeaderRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_HeaderRegion115", type=ric_NavigationRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headerRegion101: BinaryAssociation = BinaryAssociation(
    name="headerRegion101",
    ends={
        Property(name="ric_HeaderRegion", type=ric_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Portal", type=ric_HeaderRegion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
navigationRegion102: BinaryAssociation = BinaryAssociation(
    name="navigationRegion102",
    ends={
        Property(name="ric_NavigationRegion", type=ric_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Portal103", type=ric_NavigationRegion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextualNavigationRegion104: BinaryAssociation = BinaryAssociation(
    name="contextualNavigationRegion104",
    ends={
        Property(name="ric_ContextualNavigationRegion", type=ric_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Portal105", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
searchRegion106: BinaryAssociation = BinaryAssociation(
    name="searchRegion106",
    ends={
        Property(name="ric_SearchRegion", type=ric_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Portal107", type=ric_SearchRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentRegion108: BinaryAssociation = BinaryAssociation(
    name="contentRegion108",
    ends={
        Property(name="ric_ContentRegion", type=ric_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Portal109", type=ric_ContentRegion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
footerRegion110: BinaryAssociation = BinaryAssociation(
    name="footerRegion110",
    ends={
        Property(name="ric_FooterRegion", type=ric_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Portal111", type=ric_FooterRegion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
logo112: BinaryAssociation = BinaryAssociation(
    name="logo112",
    ends={
        Property(name="ric_Logo", type=ric_HeaderRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_HeaderRegion113", type=ric_Logo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
richWidgets166: BinaryAssociation = BinaryAssociation(
    name="richWidgets166",
    ends={
        Property(name="ric_RichWidget168", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document167", type=ric_RichWidget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineComponents117: BinaryAssociation = BinaryAssociation(
    name="inlineComponents117",
    ends={
        Property(name="ric_InlineComponent119", type=ric_HeaderRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_HeaderRegion118", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks120: BinaryAssociation = BinaryAssociation(
    name="lineBreaks120",
    ends={
        Property(name="ric_LineBreak122", type=ric_HeaderRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_HeaderRegion121", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image123: BinaryAssociation = BinaryAssociation(
    name="image123",
    ends={
        Property(name="ric_Image", type=ric_Logo, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Logo124", type=ric_Image, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
linkGroups125: BinaryAssociation = BinaryAssociation(
    name="linkGroups125",
    ends={
        Property(name="ric_LinkGroup", type=ric_NavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_NavigationRegion126", type=ric_LinkGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inlineComponents127: BinaryAssociation = BinaryAssociation(
    name="inlineComponents127",
    ends={
        Property(name="ric_InlineComponent129", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion128", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockLevelComponents130: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents130",
    ends={
        Property(name="ric_BlockLevelComponent132", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion131", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectComponents133: BinaryAssociation = BinaryAssociation(
    name="objectComponents133",
    ends={
        Property(name="ric_ObjectComponent135", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion134", type=ric_ObjectComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks136: BinaryAssociation = BinaryAssociation(
    name="lineBreaks136",
    ends={
        Property(name="ric_LineBreak138", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion137", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
richWidgets139: BinaryAssociation = BinaryAssociation(
    name="richWidgets139",
    ends={
        Property(name="ric_RichWidget141", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion140", type=ric_RichWidget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lists142: BinaryAssociation = BinaryAssociation(
    name="lists142",
    ends={
        Property(name="ric_List144", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion143", type=ric_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms145: BinaryAssociation = BinaryAssociation(
    name="forms145",
    ends={
        Property(name="ric_Form147", type=ric_ContextualNavigationRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContextualNavigationRegion146", type=ric_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms148: BinaryAssociation = BinaryAssociation(
    name="forms148",
    ends={
        Property(name="ric_Form150", type=ric_SearchRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_SearchRegion149", type=ric_Form, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
documents151: BinaryAssociation = BinaryAssociation(
    name="documents151",
    ends={
        Property(name="ric_Document153", type=ric_ContentRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_ContentRegion152", type=ric_Document, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inlineComponents154: BinaryAssociation = BinaryAssociation(
    name="inlineComponents154",
    ends={
        Property(name="ric_InlineComponent156", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document155", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockLevelComponents157: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents157",
    ends={
        Property(name="ric_BlockLevelComponent159", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document158", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectComponents160: BinaryAssociation = BinaryAssociation(
    name="objectComponents160",
    ends={
        Property(name="ric_ObjectComponent162", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document161", type=ric_ObjectComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks163: BinaryAssociation = BinaryAssociation(
    name="lineBreaks163",
    ends={
        Property(name="ric_LineBreak165", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document164", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checks198: BinaryAssociation = BinaryAssociation(
    name="checks198",
    ends={
        Property(name="ric_Checkbox", type=ric_CheckGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_CheckGroup199", type=ric_Checkbox, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lists169: BinaryAssociation = BinaryAssociation(
    name="lists169",
    ends={
        Property(name="ric_List171", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document170", type=ric_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms172: BinaryAssociation = BinaryAssociation(
    name="forms172",
    ends={
        Property(name="ric_Form174", type=ric_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_Document173", type=ric_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineComponents175: BinaryAssociation = BinaryAssociation(
    name="inlineComponents175",
    ends={
        Property(name="ric_InlineComponent177", type=ric_FooterRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FooterRegion176", type=ric_InlineComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockLevelComponents178: BinaryAssociation = BinaryAssociation(
    name="blockLevelComponents178",
    ends={
        Property(name="ric_BlockLevelComponent180", type=ric_FooterRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FooterRegion179", type=ric_BlockLevelComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectComponents181: BinaryAssociation = BinaryAssociation(
    name="objectComponents181",
    ends={
        Property(name="ric_ObjectComponent183", type=ric_FooterRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FooterRegion182", type=ric_ObjectComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lineBreaks184: BinaryAssociation = BinaryAssociation(
    name="lineBreaks184",
    ends={
        Property(name="ric_LineBreak186", type=ric_FooterRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FooterRegion185", type=ric_LineBreak, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
richWidgets187: BinaryAssociation = BinaryAssociation(
    name="richWidgets187",
    ends={
        Property(name="ric_RichWidget189", type=ric_FooterRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_FooterRegion188", type=ric_RichWidget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listItemns190: BinaryAssociation = BinaryAssociation(
    name="listItemns190",
    ends={
        Property(name="ric_ListItem", type=ric_OrderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_OrderedList", type=ric_ListItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
listItemns191: BinaryAssociation = BinaryAssociation(
    name="listItemns191",
    ends={
        Property(name="ric_ListItem192", type=ric_UnorderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_UnorderedList", type=ric_ListItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
radios193: BinaryAssociation = BinaryAssociation(
    name="radios193",
    ends={
        Property(name="ric_Radio", type=ric_RadioGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_RadioGroup194", type=ric_Radio, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
label195: BinaryAssociation = BinaryAssociation(
    name="label195",
    ends={
        Property(name="ric_Label197", type=ric_RadioGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_RadioGroup196", type=ric_Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label200: BinaryAssociation = BinaryAssociation(
    name="label200",
    ends={
        Property(name="ric_Label202", type=ric_CheckGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_CheckGroup201", type=ric_Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
links203: BinaryAssociation = BinaryAssociation(
    name="links203",
    ends={
        Property(name="ric_Link205", type=ric_LinkGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_LinkGroup204", type=ric_Link, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
linkGroups207: BinaryAssociation = BinaryAssociation(
    name="linkGroups207",
    ends={
        Property(name="ric_LinkGroup208", type=ric_LinkGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ric_LinkGroup206", type=ric_LinkGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ric_FormControl_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_FormControl)
gen_ric_FormControl_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_FormControl)
gen_ric_FormControl_EventComponent = Generalization(general=EventComponent, specific=ric_FormControl)
gen_ric_Button_FormControl = Generalization(general=FormControl, specific=ric_Button)
gen_ric_TextArea_FormControl = Generalization(general=FormControl, specific=ric_TextArea)
gen_ric_Form_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Form)
gen_ric_Form_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Form)
gen_ric_Form_EventComponent = Generalization(general=EventComponent, specific=ric_Form)
gen_ric_TextField_FormControl = Generalization(general=FormControl, specific=ric_TextField)
gen_ric_InputFile_FormControl = Generalization(general=FormControl, specific=ric_InputFile)
gen_ric_Checkbox_FormControl = Generalization(general=FormControl, specific=ric_Checkbox)
gen_ric_Radio_FormControl = Generalization(general=FormControl, specific=ric_Radio)
gen_ric_Select_FormControl = Generalization(general=FormControl, specific=ric_Select)
gen_ric_Label_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Label)
gen_ric_Label_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Label)
gen_ric_Fieldset_EventComponent = Generalization(general=EventComponent, specific=ric_Fieldset)
gen_ric_Fieldset_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Fieldset)
gen_ric_Fieldset_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Fieldset)
gen_ric_Div_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Div)
gen_ric_Div_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Div)
gen_ric_Div_EventComponent = Generalization(general=EventComponent, specific=ric_Div)
gen_ric_Div_BlockLevelComponent = Generalization(general=BlockLevelComponent, specific=ric_Div)
gen_ric_Paragraph_InlineComponent = Generalization(general=InlineComponent, specific=ric_Paragraph)
gen_ric_Paragraph_EventComponent = Generalization(general=EventComponent, specific=ric_Paragraph)
gen_ric_Span_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Span)
gen_ric_Span_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Span)
gen_ric_Span_EventComponent = Generalization(general=EventComponent, specific=ric_Span)
gen_ric_Span_InlineComponent = Generalization(general=InlineComponent, specific=ric_Span)
gen_ric_Heading_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Heading)
gen_ric_Heading_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Heading)
gen_ric_Heading_EventComponent = Generalization(general=EventComponent, specific=ric_Heading)
gen_ric_Heading_InlineComponent = Generalization(general=InlineComponent, specific=ric_Heading)
gen_ric_PhraseElement_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_PhraseElement)
gen_ric_PhraseElement_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_PhraseElement)
gen_ric_PhraseElement_EventComponent = Generalization(general=EventComponent, specific=ric_PhraseElement)
gen_ric_PhraseElement_InlineComponent = Generalization(general=InlineComponent, specific=ric_PhraseElement)
gen_ric_Paragraph_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Paragraph)
gen_ric_Paragraph_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Paragraph)
gen_ric_LineBreak_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_LineBreak)
gen_ric_LineBreak_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_LineBreak)
gen_ric_Link_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Link)
gen_ric_Link_EventComponent = Generalization(general=EventComponent, specific=ric_Link)
gen_ric_Link_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Link)
gen_ric_Link_InlineComponent = Generalization(general=InlineComponent, specific=ric_Link)
gen_ric_Image_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_Image)
gen_ric_Image_EventComponent = Generalization(general=EventComponent, specific=ric_Image)
gen_ric_Image_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_Image)
gen_ric_Image_ObjectComponent = Generalization(general=ObjectComponent, specific=ric_Image)
gen_ric_RichWidget_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_RichWidget)
gen_ric_RichWidget_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_RichWidget)
gen_ric_TabbedPanel_RichWidget = Generalization(general=RichWidget, specific=ric_TabbedPanel)
gen_ric_AccordionPanel_RichWidget = Generalization(general=RichWidget, specific=ric_AccordionPanel)
gen_ric_MessageDialog_RichWidget = Generalization(general=RichWidget, specific=ric_MessageDialog)
gen_ric_Datepicker_RichWidget = Generalization(general=RichWidget, specific=ric_Datepicker)
gen_ric_Datepicker_TextField = Generalization(general=TextField, specific=ric_Datepicker)
gen_ric_ValueConstraint_FormControlConstraint = Generalization(general=FormControlConstraint, specific=ric_ValueConstraint)
gen_ric_NumberValueConstraint_FormControlConstraint = Generalization(general=FormControlConstraint, specific=ric_NumberValueConstraint)
gen_ric_RequiredFieldConstraint_FormControlConstraint = Generalization(general=FormControlConstraint, specific=ric_RequiredFieldConstraint)
gen_ric_ValidDateConstraint_FormControlConstraint = Generalization(general=FormControlConstraint, specific=ric_ValidDateConstraint)
gen_ric_Document_EventComponent = Generalization(general=EventComponent, specific=ric_Document)
gen_ric_List_ClassifiableComponent = Generalization(general=ClassifiableComponent, specific=ric_List)
gen_ric_List_EventComponent = Generalization(general=EventComponent, specific=ric_List)
gen_ric_List_IdentifiableComponent = Generalization(general=IdentifiableComponent, specific=ric_List)
gen_ric_OrderedList_List = Generalization(general=List, specific=ric_OrderedList)
gen_ric_UnorderedList_List = Generalization(general=List, specific=ric_UnorderedList)

# Domain Model
domain_model = DomainModel(
    name="ric",
    types={ric_IdentifiableComponent, ric_ClassifiableComponent, ric_EventComponent, ric_Event, ric_FormControl, IdentifiableComponent, ClassifiableComponent, EventComponent, ric_Label, ric_PhraseElement, ric_ValueConstraint, ric_NumberValueConstraint, ric_RequiredFieldConstraint, ric_ValidDateConstraint, ric_Button, FormControl, ric_TextArea, ric_Form, ric_Document, ric_Fieldset, ric_BlockLevelComponent, ric_InlineComponent, ric_TextField, ric_InputFile, ric_Script, ric_Checkbox, ric_Radio, ric_Select, ric_RichWidget, ric_SelectItem, ric_RadioGroup, ric_CheckGroup, ric_Div, BlockLevelComponent, ric_ObjectComponent, ric_LineBreak, ric_List, ric_Span, InlineComponent, ric_Heading, ric_Paragraph, ric_Link, ric_Image, ObjectComponent, ric_TabbedPanel, RichWidget, ric_Tab, ric_AccordionPanel, ric_Section, ric_MessageDialog, ric_MessageDialogButton, ric_Datepicker, TextField, ric_FormControlConstraint, FormControlConstraint, ric_Portal, ric_HeaderRegion, ric_NavigationRegion, ric_ContextualNavigationRegion, ric_SearchRegion, ric_ContentRegion, ric_FooterRegion, ric_Logo, ric_LinkGroup, ric_OrderedList, List, ric_ListItem, ric_UnorderedList, ButtonType, EventType, ScriptType, SubmitFormMethod, Align, HeadingLevel, PhraseElementType, ObjectAlign, DateFormat, Locale, MatchingOperator, LogicalOperator, Orientation, OrderedListType, UnorderedListType, Extension, FieldSetLegendAlign, MessageDialogEvent},
    associations={events0, label1, accompanyingPhrase2, valueConstraints4, numberConstraint6, requiredFieldConstraint8, validDateConstraint10, triggerScript12, action14, fieldsets15, blockLevelComponents17, inlineComponents19, items21, richWidgets35, events22, controls25, radioGroups28, checkGroups30, objectComponents32, lineBreaks33, lists37, forms39, fieldsets42, blockLevelComponents46, inlineComponents48, inlineComponents52, lists72, target54, tabs56, inlineComponents57, blockLevelComponents60, objectComponents63, lineBreaks66, richWidgets69, forms75, sections78, inlineComponents79, blockLevelComponents82, objectComponents85, lineBreaks88, richWidgets91, lists94, forms97, buttons100, subsiteNavigation114, headerRegion101, navigationRegion102, contextualNavigationRegion104, searchRegion106, contentRegion108, footerRegion110, logo112, richWidgets166, inlineComponents117, lineBreaks120, image123, linkGroups125, inlineComponents127, blockLevelComponents130, objectComponents133, lineBreaks136, richWidgets139, lists142, forms145, forms148, documents151, inlineComponents154, blockLevelComponents157, objectComponents160, lineBreaks163, checks198, lists169, forms172, inlineComponents175, blockLevelComponents178, objectComponents181, lineBreaks184, richWidgets187, listItemns190, listItemns191, radios193, label195, label200, links203, linkGroups207},
    generalizations={gen_ric_FormControl_IdentifiableComponent, gen_ric_FormControl_ClassifiableComponent, gen_ric_FormControl_EventComponent, gen_ric_Button_FormControl, gen_ric_TextArea_FormControl, gen_ric_Form_IdentifiableComponent, gen_ric_Form_ClassifiableComponent, gen_ric_Form_EventComponent, gen_ric_TextField_FormControl, gen_ric_InputFile_FormControl, gen_ric_Checkbox_FormControl, gen_ric_Radio_FormControl, gen_ric_Select_FormControl, gen_ric_Label_IdentifiableComponent, gen_ric_Label_ClassifiableComponent, gen_ric_Fieldset_EventComponent, gen_ric_Fieldset_IdentifiableComponent, gen_ric_Fieldset_ClassifiableComponent, gen_ric_Div_ClassifiableComponent, gen_ric_Div_IdentifiableComponent, gen_ric_Div_EventComponent, gen_ric_Div_BlockLevelComponent, gen_ric_Paragraph_InlineComponent, gen_ric_Paragraph_EventComponent, gen_ric_Span_ClassifiableComponent, gen_ric_Span_IdentifiableComponent, gen_ric_Span_EventComponent, gen_ric_Span_InlineComponent, gen_ric_Heading_ClassifiableComponent, gen_ric_Heading_IdentifiableComponent, gen_ric_Heading_EventComponent, gen_ric_Heading_InlineComponent, gen_ric_PhraseElement_IdentifiableComponent, gen_ric_PhraseElement_ClassifiableComponent, gen_ric_PhraseElement_EventComponent, gen_ric_PhraseElement_InlineComponent, gen_ric_Paragraph_ClassifiableComponent, gen_ric_Paragraph_IdentifiableComponent, gen_ric_LineBreak_ClassifiableComponent, gen_ric_LineBreak_IdentifiableComponent, gen_ric_Link_ClassifiableComponent, gen_ric_Link_EventComponent, gen_ric_Link_IdentifiableComponent, gen_ric_Link_InlineComponent, gen_ric_Image_ClassifiableComponent, gen_ric_Image_EventComponent, gen_ric_Image_IdentifiableComponent, gen_ric_Image_ObjectComponent, gen_ric_RichWidget_ClassifiableComponent, gen_ric_RichWidget_IdentifiableComponent, gen_ric_TabbedPanel_RichWidget, gen_ric_AccordionPanel_RichWidget, gen_ric_MessageDialog_RichWidget, gen_ric_Datepicker_RichWidget, gen_ric_Datepicker_TextField, gen_ric_ValueConstraint_FormControlConstraint, gen_ric_NumberValueConstraint_FormControlConstraint, gen_ric_RequiredFieldConstraint_FormControlConstraint, gen_ric_ValidDateConstraint_FormControlConstraint, gen_ric_Document_EventComponent, gen_ric_List_ClassifiableComponent, gen_ric_List_EventComponent, gen_ric_List_IdentifiableComponent, gen_ric_OrderedList_List, gen_ric_UnorderedList_List},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)