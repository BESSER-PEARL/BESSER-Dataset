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
EventDependencyType: Enumeration = Enumeration(
    name="EventDependencyType",
    literals={
            EnumerationLiteral(name="onValueChange"),
			EnumerationLiteral(name="onChange"),
			EnumerationLiteral(name="onBlur"),
			EnumerationLiteral(name="onClick")
    }
)

LabelPosition: Enumeration = Enumeration(
    name="LabelPosition",
    literals={
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right"),
			EnumerationLiteral(name="Up"),
			EnumerationLiteral(name="Down")
    }
)

FileWidgetInputType: Enumeration = Enumeration(
    name="FileWidgetInputType",
    literals={
            EnumerationLiteral(name="Document"),
			EnumerationLiteral(name="URL"),
			EnumerationLiteral(name="Resource")
    }
)

FileWidgetDownloadType: Enumeration = Enumeration(
    name="FileWidgetDownloadType",
    literals={
            EnumerationLiteral(name="Both"),
			EnumerationLiteral(name="URL"),
			EnumerationLiteral(name="Browse")
    }
)

# Classes
form_Widget = Class(name="form::Widget", is_abstract=True)
form_Validator = Class(name="form::Validator")
form_WidgetDependency = Class(name="form::WidgetDependency")
form_Operation = Class(name="form::Operation")
form_WidgetLayoutInfo = Class(name="form::WidgetLayoutInfo")
form_Expression = Class(name="form::Expression")
form_Validable = Class(name="form::Validable")
form_Form = Class(name="form::Form")
ConnectableElement = Class(name="ConnectableElement")
Validable = Class(name="Validable")
form_EStringToStringMapEntry = Class(name="form::EStringToStringMapEntry")
form_Column = Class(name="form::Column")
form_Line = Class(name="form::Line")
Element = Class(name="Element")
CSSCustomizable = Class(name="CSSCustomizable")
form_ItemContainer = Class(name="form::ItemContainer", is_abstract=True)
form_Duplicable = Class(name="form::Duplicable", is_abstract=True)
form_ViewForm = Class(name="form::ViewForm")
Form = Class(name="Form")
form_CSSCustomizable = Class(name="form::CSSCustomizable", is_abstract=True)
form_Group = Class(name="form::Group")
Widget = Class(name="Widget")
Duplicable = Class(name="Duplicable")
form_GroupIterator = Class(name="form::GroupIterator")
form_FormField = Class(name="form::FormField", is_abstract=True)
form_TextAreaFormField = Class(name="form::TextAreaFormField")
form_RichTextAreaFormField = Class(name="form::RichTextAreaFormField")
form_FormButton = Class(name="form::FormButton")
form_SubmitFormButton = Class(name="form::SubmitFormButton")
FormButton = Class(name="FormButton")
form_PreviousFormButton = Class(name="form::PreviousFormButton")
form_NextFormButton = Class(name="form::NextFormButton")
form_Info = Class(name="form::Info")
form_MultipleValuatedFormField = Class(name="form::MultipleValuatedFormField", is_abstract=True)
FormField = Class(name="FormField")
form_SingleValuatedFormField = Class(name="form::SingleValuatedFormField", is_abstract=True)
form_CheckBoxMultipleFormField = Class(name="form::CheckBoxMultipleFormField")
MultipleValuatedFormField = Class(name="MultipleValuatedFormField")
ItemContainer = Class(name="ItemContainer")
form_ComboFormField = Class(name="form::ComboFormField")
form_DateFormField = Class(name="form::DateFormField")
SingleValuatedFormField = Class(name="SingleValuatedFormField")
form_ListFormField = Class(name="form::ListFormField")
form_PasswordFormField = Class(name="form::PasswordFormField")
form_RadioFormField = Class(name="form::RadioFormField")
form_SelectFormField = Class(name="form::SelectFormField")
form_TextFormField = Class(name="form::TextFormField")
form_HiddenWidget = Class(name="form::HiddenWidget")
form_DurationFormField = Class(name="form::DurationFormField")
form_AbstractTable = Class(name="form::AbstractTable", is_abstract=True)
form_TextInfo = Class(name="form::TextInfo")
Info = Class(name="Info")
form_MessageInfo = Class(name="form::MessageInfo")
form_CheckBoxSingleFormField = Class(name="form::CheckBoxSingleFormField")
form_FileWidget = Class(name="form::FileWidget")
form_Document = Class(name="form::Document")
form_ImageWidget = Class(name="form::ImageWidget")
form_IFrameWidget = Class(name="form::IFrameWidget")
form_MandatoryFieldsCustomization = Class(name="form::MandatoryFieldsCustomization", is_abstract=True)
form_HtmlWidget = Class(name="form::HtmlWidget")
form_SuggestBox = Class(name="form::SuggestBox")
form_TableExpression = Class(name="form::TableExpression")
form_Table = Class(name="form::Table")
AbstractTable = Class(name="AbstractTable")
form_DynamicTable = Class(name="form::DynamicTable")

# form_Widget class attributes and methods
form_Widget_showDisplayLabel: Property = Property(name="showDisplayLabel", type=StringType)
form_Widget_allowHTMLForDisplayLabel: Property = Property(name="allowHTMLForDisplayLabel", type=BooleanType)
form_Widget_displayDependentWidgetOnlyOnEventTriggered: Property = Property(name="displayDependentWidgetOnlyOnEventTriggered", type=BooleanType)
form_Widget_mandatory: Property = Property(name="mandatory", type=BooleanType)
form_Widget_readOnly: Property = Property(name="readOnly", type=BooleanType)
form_Widget_labelPosition: Property = Property(name="labelPosition", type=StringType)
form_Widget_realHtmlAttributes: Property = Property(name="realHtmlAttributes", type=StringType)
form_Widget_injectWidgetCondition: Property = Property(name="injectWidgetCondition", type=BooleanType)
form_Widget_version: Property = Property(name="version", type=StringType)
form_Widget_returnTypeModifier: Property = Property(name="returnTypeModifier", type=StringType)
form_Widget.attributes={form_Widget_version, form_Widget_allowHTMLForDisplayLabel, form_Widget_showDisplayLabel, form_Widget_mandatory, form_Widget_returnTypeModifier, form_Widget_displayDependentWidgetOnlyOnEventTriggered, form_Widget_readOnly, form_Widget_labelPosition, form_Widget_injectWidgetCondition, form_Widget_realHtmlAttributes}

# form_Validator class attributes and methods
form_Validator_validatorClass: Property = Property(name="validatorClass", type=StringType)
form_Validator_htmlClass: Property = Property(name="htmlClass", type=StringType)
form_Validator_name: Property = Property(name="name", type=StringType)
form_Validator_belowField: Property = Property(name="belowField", type=BooleanType)
form_Validator.attributes={form_Validator_htmlClass, form_Validator_validatorClass, form_Validator_name, form_Validator_belowField}

# form_WidgetDependency class attributes and methods
form_WidgetDependency_triggerRefreshOnModification: Property = Property(name="triggerRefreshOnModification", type=BooleanType)
form_WidgetDependency_eventTypes: Property = Property(name="eventTypes", type=StringType)
form_WidgetDependency.attributes={form_WidgetDependency_triggerRefreshOnModification, form_WidgetDependency_eventTypes}

# form_Operation class attributes and methods

# form_WidgetLayoutInfo class attributes and methods
form_WidgetLayoutInfo_line: Property = Property(name="line", type=IntegerType)
form_WidgetLayoutInfo_column: Property = Property(name="column", type=IntegerType)
form_WidgetLayoutInfo_verticalSpan: Property = Property(name="verticalSpan", type=IntegerType)
form_WidgetLayoutInfo_horizontalSpan: Property = Property(name="horizontalSpan", type=IntegerType)
form_WidgetLayoutInfo.attributes={form_WidgetLayoutInfo_line, form_WidgetLayoutInfo_column, form_WidgetLayoutInfo_horizontalSpan, form_WidgetLayoutInfo_verticalSpan}

# form_Expression class attributes and methods

# form_Validable class attributes and methods
form_Validable_useDefaultValidator: Property = Property(name="useDefaultValidator", type=StringType)
form_Validable_below: Property = Property(name="below", type=BooleanType)
form_Validable.attributes={form_Validable_useDefaultValidator, form_Validable_below}

# form_Form class attributes and methods
form_Form_nColumn: Property = Property(name="nColumn", type=IntegerType)
form_Form_nLine: Property = Property(name="nLine", type=IntegerType)
form_Form_showPageLabel: Property = Property(name="showPageLabel", type=StringType)
form_Form_allowHTMLInPageLabel: Property = Property(name="allowHTMLInPageLabel", type=BooleanType)
form_Form_version: Property = Property(name="version", type=StringType)
form_Form.attributes={form_Form_allowHTMLInPageLabel, form_Form_version, form_Form_showPageLabel, form_Form_nColumn, form_Form_nLine}

# ConnectableElement class attributes and methods

# Validable class attributes and methods

# form_EStringToStringMapEntry class attributes and methods

# form_Column class attributes and methods
form_Column_width: Property = Property(name="width", type=StringType)
form_Column_number: Property = Property(name="number", type=IntegerType)
form_Column.attributes={form_Column_width, form_Column_number}

# form_Line class attributes and methods
form_Line_height: Property = Property(name="height", type=StringType)
form_Line_number: Property = Property(name="number", type=IntegerType)
form_Line.attributes={form_Line_height, form_Line_number}

# Element class attributes and methods

# CSSCustomizable class attributes and methods

# form_ItemContainer class attributes and methods
form_ItemContainer_itemClass: Property = Property(name="itemClass", type=StringType)
form_ItemContainer.attributes={form_ItemContainer_itemClass}

# form_Duplicable class attributes and methods
form_Duplicable_duplicate: Property = Property(name="duplicate", type=BooleanType)
form_Duplicable_limitNumberOfDuplication: Property = Property(name="limitNumberOfDuplication", type=BooleanType)
form_Duplicable_limitMinNumberOfDuplication: Property = Property(name="limitMinNumberOfDuplication", type=BooleanType)
form_Duplicable.attributes={form_Duplicable_limitMinNumberOfDuplication, form_Duplicable_limitNumberOfDuplication, form_Duplicable_duplicate}

# form_ViewForm class attributes and methods

# Form class attributes and methods

# form_CSSCustomizable class attributes and methods

# form_Group class attributes and methods
form_Group_showBorder: Property = Property(name="showBorder", type=BooleanType)
form_Group_useIterator: Property = Property(name="useIterator", type=BooleanType)
form_Group.attributes={form_Group_showBorder, form_Group_useIterator}

# Widget class attributes and methods

# Duplicable class attributes and methods

# form_GroupIterator class attributes and methods
form_GroupIterator_className: Property = Property(name="className", type=StringType)
form_GroupIterator.attributes={form_GroupIterator_className}

# form_FormField class attributes and methods
form_FormField_description: Property = Property(name="description", type=StringType)
form_FormField_exampleMessagePosition: Property = Property(name="exampleMessagePosition", type=StringType)
form_FormField.attributes={form_FormField_description, form_FormField_exampleMessagePosition}

# form_TextAreaFormField class attributes and methods
form_TextAreaFormField_maxLength: Property = Property(name="maxLength", type=IntegerType)
form_TextAreaFormField_maxHeigth: Property = Property(name="maxHeigth", type=IntegerType)
form_TextAreaFormField.attributes={form_TextAreaFormField_maxLength, form_TextAreaFormField_maxHeigth}

# form_RichTextAreaFormField class attributes and methods

# form_FormButton class attributes and methods
form_FormButton_labelBehavior: Property = Property(name="labelBehavior", type=StringType)
form_FormButton.attributes={form_FormButton_labelBehavior}

# form_SubmitFormButton class attributes and methods

# FormButton class attributes and methods

# form_PreviousFormButton class attributes and methods

# form_NextFormButton class attributes and methods

# form_Info class attributes and methods

# form_MultipleValuatedFormField class attributes and methods

# FormField class attributes and methods

# form_SingleValuatedFormField class attributes and methods

# form_CheckBoxMultipleFormField class attributes and methods

# MultipleValuatedFormField class attributes and methods

# ItemContainer class attributes and methods

# form_ComboFormField class attributes and methods

# form_DateFormField class attributes and methods
form_DateFormField_initialFormat: Property = Property(name="initialFormat", type=StringType)
form_DateFormField_displayFormat: Property = Property(name="displayFormat", type=StringType)
form_DateFormField.attributes={form_DateFormField_initialFormat, form_DateFormField_displayFormat}

# SingleValuatedFormField class attributes and methods

# form_ListFormField class attributes and methods
form_ListFormField_maxHeigth: Property = Property(name="maxHeigth", type=IntegerType)
form_ListFormField.attributes={form_ListFormField_maxHeigth}

# form_PasswordFormField class attributes and methods
form_PasswordFormField_maxLength: Property = Property(name="maxLength", type=IntegerType)
form_PasswordFormField.attributes={form_PasswordFormField_maxLength}

# form_RadioFormField class attributes and methods

# form_SelectFormField class attributes and methods

# form_TextFormField class attributes and methods
form_TextFormField_maxLength: Property = Property(name="maxLength", type=IntegerType)
form_TextFormField.attributes={form_TextFormField_maxLength}

# form_HiddenWidget class attributes and methods

# form_DurationFormField class attributes and methods
form_DurationFormField_day: Property = Property(name="day", type=StringType)
form_DurationFormField_hour: Property = Property(name="hour", type=StringType)
form_DurationFormField_min: Property = Property(name="min", type=StringType)
form_DurationFormField_sec: Property = Property(name="sec", type=StringType)
form_DurationFormField.attributes={form_DurationFormField_hour, form_DurationFormField_day, form_DurationFormField_min, form_DurationFormField_sec}

# form_AbstractTable class attributes and methods
form_AbstractTable_leftColumnIsHeader: Property = Property(name="leftColumnIsHeader", type=BooleanType)
form_AbstractTable_rightColumnIsHeader: Property = Property(name="rightColumnIsHeader", type=BooleanType)
form_AbstractTable_firstRowIsHeader: Property = Property(name="firstRowIsHeader", type=BooleanType)
form_AbstractTable_LastRowIsHeader: Property = Property(name="LastRowIsHeader", type=BooleanType)
form_AbstractTable_initializedUsingCells: Property = Property(name="initializedUsingCells", type=BooleanType)
form_AbstractTable_useHorizontalHeader: Property = Property(name="useHorizontalHeader", type=BooleanType)
form_AbstractTable_useVerticalHeader: Property = Property(name="useVerticalHeader", type=BooleanType)
form_AbstractTable.attributes={form_AbstractTable_LastRowIsHeader, form_AbstractTable_rightColumnIsHeader, form_AbstractTable_leftColumnIsHeader, form_AbstractTable_initializedUsingCells, form_AbstractTable_firstRowIsHeader, form_AbstractTable_useVerticalHeader, form_AbstractTable_useHorizontalHeader}

# form_TextInfo class attributes and methods

# Info class attributes and methods

# form_MessageInfo class attributes and methods

# form_CheckBoxSingleFormField class attributes and methods

# form_FileWidget class attributes and methods
form_FileWidget_downloadOnly: Property = Property(name="downloadOnly", type=BooleanType)
form_FileWidget_usePreview: Property = Property(name="usePreview", type=BooleanType)
form_FileWidget_initialResourcePath: Property = Property(name="initialResourcePath", type=StringType)
form_FileWidget_outputDocumentName: Property = Property(name="outputDocumentName", type=StringType)
form_FileWidget_updateDocument: Property = Property(name="updateDocument", type=BooleanType)
form_FileWidget_intialResourceList: Property = Property(name="intialResourceList", type=StringType)
form_FileWidget_inputType: Property = Property(name="inputType", type=StringType)
form_FileWidget_downloadType: Property = Property(name="downloadType", type=StringType)
form_FileWidget.attributes={form_FileWidget_updateDocument, form_FileWidget_intialResourceList, form_FileWidget_initialResourcePath, form_FileWidget_outputDocumentName, form_FileWidget_downloadOnly, form_FileWidget_downloadType, form_FileWidget_usePreview, form_FileWidget_inputType}

# form_Document class attributes and methods

# form_ImageWidget class attributes and methods
form_ImageWidget_isADocument: Property = Property(name="isADocument", type=BooleanType)
form_ImageWidget.attributes={form_ImageWidget_isADocument}

# form_IFrameWidget class attributes and methods

# form_MandatoryFieldsCustomization class attributes and methods

# form_HtmlWidget class attributes and methods

# form_SuggestBox class attributes and methods
form_SuggestBox_maxItems: Property = Property(name="maxItems", type=IntegerType)
form_SuggestBox_useMaxItems: Property = Property(name="useMaxItems", type=BooleanType)
form_SuggestBox_asynchronous: Property = Property(name="asynchronous", type=BooleanType)
form_SuggestBox_delay: Property = Property(name="delay", type=IntegerType)
form_SuggestBox.attributes={form_SuggestBox_useMaxItems, form_SuggestBox_maxItems, form_SuggestBox_asynchronous, form_SuggestBox_delay}

# form_TableExpression class attributes and methods

# form_Table class attributes and methods
form_Table_usePagination: Property = Property(name="usePagination", type=BooleanType)
form_Table_allowSelection: Property = Property(name="allowSelection", type=BooleanType)
form_Table_selectionModeIsMultiple: Property = Property(name="selectionModeIsMultiple", type=BooleanType)
form_Table.attributes={form_Table_usePagination, form_Table_selectionModeIsMultiple, form_Table_allowSelection}

# AbstractTable class attributes and methods

# form_DynamicTable class attributes and methods
form_DynamicTable_limitMinNumberOfColumn: Property = Property(name="limitMinNumberOfColumn", type=BooleanType)
form_DynamicTable_limitMinNumberOfRow: Property = Property(name="limitMinNumberOfRow", type=BooleanType)
form_DynamicTable_allowAddRemoveRow: Property = Property(name="allowAddRemoveRow", type=BooleanType)
form_DynamicTable_allowAddRemoveColumn: Property = Property(name="allowAddRemoveColumn", type=BooleanType)
form_DynamicTable_limitMaxNumberOfColumn: Property = Property(name="limitMaxNumberOfColumn", type=BooleanType)
form_DynamicTable_limitMaxNumberOfRow: Property = Property(name="limitMaxNumberOfRow", type=BooleanType)
form_DynamicTable.attributes={form_DynamicTable_limitMaxNumberOfColumn, form_DynamicTable_limitMaxNumberOfRow, form_DynamicTable_allowAddRemoveColumn, form_DynamicTable_limitMinNumberOfRow, form_DynamicTable_allowAddRemoveRow, form_DynamicTable_limitMinNumberOfColumn}

# Relationships
widget0: BinaryAssociation = BinaryAssociation(
    name="widget0",
    ends={
        Property(name="form_Widget", type=form_WidgetDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="form_WidgetDependency", type=form_Widget, multiplicity=Multiplicity(1, 1))
    }
)
widgets12: BinaryAssociation = BinaryAssociation(
    name="widgets12",
    ends={
        Property(name="form_Widget14", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form13", type=form_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageLabel15: BinaryAssociation = BinaryAssociation(
    name="pageLabel15",
    ends={
        Property(name="form_Expression17", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form16", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions18: BinaryAssociation = BinaryAssociation(
    name="actions18",
    ends={
        Property(name="form_Operation", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form19", type=form_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter1: BinaryAssociation = BinaryAssociation(
    name="parameter1",
    ends={
        Property(name="form_Expression", type=form_Validator, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Validator", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayName2: BinaryAssociation = BinaryAssociation(
    name="displayName2",
    ends={
        Property(name="form_Expression4", type=form_Validator, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Validator3", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validators5: BinaryAssociation = BinaryAssociation(
    name="validators5",
    ends={
        Property(name="form_Validator6", type=form_Validable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Validable", type=form_Validator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringAttributes7: BinaryAssociation = BinaryAssociation(
    name="stringAttributes7",
    ends={
        Property(name="form_EStringToStringMapEntry", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form", type=form_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns8: BinaryAssociation = BinaryAssociation(
    name="columns8",
    ends={
        Property(name="form_Column", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form9", type=form_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines10: BinaryAssociation = BinaryAssociation(
    name="lines10",
    ends={
        Property(name="form_Line", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form11", type=form_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
widgetLayoutInfo39: BinaryAssociation = BinaryAssociation(
    name="widgetLayoutInfo39",
    ends={
        Property(name="form_WidgetLayoutInfo", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget40", type=form_WidgetLayoutInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependOn41: BinaryAssociation = BinaryAssociation(
    name="dependOn41",
    ends={
        Property(name="form_WidgetDependency43", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget42", type=form_WidgetDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentOf44: BinaryAssociation = BinaryAssociation(
    name="parentOf44",
    ends={
        Property(name="form_WidgetDependency46", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget45", type=form_WidgetDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxNumberOfDuplication20: BinaryAssociation = BinaryAssociation(
    name="maxNumberOfDuplication20",
    ends={
        Property(name="form_Expression21", type=form_Duplicable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Duplicable", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minNumberOfDuplication22: BinaryAssociation = BinaryAssociation(
    name="minNumberOfDuplication22",
    ends={
        Property(name="form_Expression24", type=form_Duplicable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Duplicable23", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayLabelForAdd25: BinaryAssociation = BinaryAssociation(
    name="displayLabelForAdd25",
    ends={
        Property(name="form_Expression27", type=form_Duplicable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Duplicable26", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tooltipForAdd28: BinaryAssociation = BinaryAssociation(
    name="tooltipForAdd28",
    ends={
        Property(name="form_Expression30", type=form_Duplicable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Duplicable29", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayLabelForRemove31: BinaryAssociation = BinaryAssociation(
    name="displayLabelForRemove31",
    ends={
        Property(name="form_Expression33", type=form_Duplicable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Duplicable32", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tooltipForRemove34: BinaryAssociation = BinaryAssociation(
    name="tooltipForRemove34",
    ends={
        Property(name="form_Expression36", type=form_Duplicable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Duplicable35", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
htmlAttributes37: BinaryAssociation = BinaryAssociation(
    name="htmlAttributes37",
    ends={
        Property(name="form_EStringToStringMapEntry38", type=form_CSSCustomizable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_CSSCustomizable", type=form_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
widgets74: BinaryAssociation = BinaryAssociation(
    name="widgets74",
    ends={
        Property(name="form_Widget75", type=form_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Group", type=form_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns76: BinaryAssociation = BinaryAssociation(
    name="columns76",
    ends={
        Property(name="form_Column78", type=form_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Group77", type=form_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines79: BinaryAssociation = BinaryAssociation(
    name="lines79",
    ends={
        Property(name="form_Line81", type=form_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Group80", type=form_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator82: BinaryAssociation = BinaryAssociation(
    name="iterator82",
    ends={
        Property(name="form_GroupIterator", type=form_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Group83", type=form_GroupIterator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayDependentWidgetOnlyAfterFirstEventTriggeredAndCondition47: BinaryAssociation = BinaryAssociation(
    name="displayDependentWidgetOnlyAfterFirstEventTriggeredAndCondition47",
    ends={
        Property(name="form_Expression49", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget48", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayAfterEventDependsOnConditionScript50: BinaryAssociation = BinaryAssociation(
    name="displayAfterEventDependsOnConditionScript50",
    ends={
        Property(name="form_Expression52", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget51", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputExpression53: BinaryAssociation = BinaryAssociation(
    name="inputExpression53",
    ends={
        Property(name="form_Expression55", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget54", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
afterEventExpression56: BinaryAssociation = BinaryAssociation(
    name="afterEventExpression56",
    ends={
        Property(name="form_Expression58", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget57", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tooltip59: BinaryAssociation = BinaryAssociation(
    name="tooltip59",
    ends={
        Property(name="form_Expression61", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget60", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
helpMessage62: BinaryAssociation = BinaryAssociation(
    name="helpMessage62",
    ends={
        Property(name="form_Expression64", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget63", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
displayLabel65: BinaryAssociation = BinaryAssociation(
    name="displayLabel65",
    ends={
        Property(name="form_Expression67", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget66", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
injectWidgetScript68: BinaryAssociation = BinaryAssociation(
    name="injectWidgetScript68",
    ends={
        Property(name="form_Expression70", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget69", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action71: BinaryAssociation = BinaryAssociation(
    name="action71",
    ends={
        Property(name="form_Operation73", type=form_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Widget72", type=form_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions91: BinaryAssociation = BinaryAssociation(
    name="actions91",
    ends={
        Property(name="form_Operation92", type=form_SubmitFormButton, multiplicity=Multiplicity(1, 1)),
        Property(name="form_SubmitFormButton", type=form_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exampleMessage84: BinaryAssociation = BinaryAssociation(
    name="exampleMessage84",
    ends={
        Property(name="form_Expression85", type=form_FormField, multiplicity=Multiplicity(1, 1)),
        Property(name="form_FormField", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExpression86: BinaryAssociation = BinaryAssociation(
    name="defaultExpression86",
    ends={
        Property(name="form_Expression87", type=form_MultipleValuatedFormField, multiplicity=Multiplicity(1, 1)),
        Property(name="form_MultipleValuatedFormField", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExpressionAfterEvent88: BinaryAssociation = BinaryAssociation(
    name="defaultExpressionAfterEvent88",
    ends={
        Property(name="form_Expression90", type=form_MultipleValuatedFormField, multiplicity=Multiplicity(1, 1)),
        Property(name="form_MultipleValuatedFormField89", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
document93: BinaryAssociation = BinaryAssociation(
    name="document93",
    ends={
        Property(name="form_Document", type=form_FileWidget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_FileWidget", type=form_Document, multiplicity=Multiplicity(0, 1))
    }
)
outputDocumentListExpression94: BinaryAssociation = BinaryAssociation(
    name="outputDocumentListExpression94",
    ends={
        Property(name="form_Expression96", type=form_FileWidget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_FileWidget95", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
document97: BinaryAssociation = BinaryAssociation(
    name="document97",
    ends={
        Property(name="form_Document98", type=form_ImageWidget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_ImageWidget", type=form_Document, multiplicity=Multiplicity(0, 1))
    }
)
imgPath99: BinaryAssociation = BinaryAssociation(
    name="imgPath99",
    ends={
        Property(name="form_Expression101", type=form_ImageWidget, multiplicity=Multiplicity(1, 1)),
        Property(name="form_ImageWidget100", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minNumberOfRow119: BinaryAssociation = BinaryAssociation(
    name="minNumberOfRow119",
    ends={
        Property(name="form_Expression121", type=form_DynamicTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_DynamicTable120", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxNumberOfColumn122: BinaryAssociation = BinaryAssociation(
    name="maxNumberOfColumn122",
    ends={
        Property(name="form_Expression124", type=form_DynamicTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_DynamicTable123", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxNumberOfRow125: BinaryAssociation = BinaryAssociation(
    name="maxNumberOfRow125",
    ends={
        Property(name="form_Expression127", type=form_DynamicTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_DynamicTable126", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mandatorySymbol128: BinaryAssociation = BinaryAssociation(
    name="mandatorySymbol128",
    ends={
        Property(name="form_Expression129", type=form_MandatoryFieldsCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="form_MandatoryFieldsCustomization", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mandatoryLabel130: BinaryAssociation = BinaryAssociation(
    name="mandatoryLabel130",
    ends={
        Property(name="form_Expression132", type=form_MandatoryFieldsCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="form_MandatoryFieldsCustomization131", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
horizontalHeaderExpression102: BinaryAssociation = BinaryAssociation(
    name="horizontalHeaderExpression102",
    ends={
        Property(name="form_Expression103", type=form_AbstractTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_AbstractTable", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
verticalHeaderExpression104: BinaryAssociation = BinaryAssociation(
    name="verticalHeaderExpression104",
    ends={
        Property(name="form_Expression106", type=form_AbstractTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_AbstractTable105", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableExpression107: BinaryAssociation = BinaryAssociation(
    name="tableExpression107",
    ends={
        Property(name="form_TableExpression", type=form_AbstractTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_AbstractTable108", type=form_TableExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxRowForPagination109: BinaryAssociation = BinaryAssociation(
    name="maxRowForPagination109",
    ends={
        Property(name="form_Expression110", type=form_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Table", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnForInitialSelectionIndex111: BinaryAssociation = BinaryAssociation(
    name="columnForInitialSelectionIndex111",
    ends={
        Property(name="form_Expression113", type=form_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Table112", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectedValues114: BinaryAssociation = BinaryAssociation(
    name="selectedValues114",
    ends={
        Property(name="form_Expression116", type=form_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Table115", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minNumberOfColumn117: BinaryAssociation = BinaryAssociation(
    name="minNumberOfColumn117",
    ends={
        Property(name="form_Expression118", type=form_DynamicTable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_DynamicTable", type=form_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_form_Form_ConnectableElement = Generalization(general=ConnectableElement, specific=form_Form)
gen_form_Form_Validable = Generalization(general=Validable, specific=form_Form)
gen_form_Widget_Element = Generalization(general=Element, specific=form_Widget)
gen_form_Widget_CSSCustomizable = Generalization(general=CSSCustomizable, specific=form_Widget)
gen_form_ViewForm_Form = Generalization(general=Form, specific=form_ViewForm)
gen_form_Group_Widget = Generalization(general=Widget, specific=form_Group)
gen_form_Group_Duplicable = Generalization(general=Duplicable, specific=form_Group)
gen_form_FormField_Widget = Generalization(general=Widget, specific=form_FormField)
gen_form_FormField_Validable = Generalization(general=Validable, specific=form_FormField)
gen_form_FormField_Duplicable = Generalization(general=Duplicable, specific=form_FormField)
gen_form_TextFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_TextFormField)
gen_form_TextAreaFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_TextAreaFormField)
gen_form_RichTextAreaFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_RichTextAreaFormField)
gen_form_FormButton_Widget = Generalization(general=Widget, specific=form_FormButton)
gen_form_SubmitFormButton_FormButton = Generalization(general=FormButton, specific=form_SubmitFormButton)
gen_form_SubmitFormButton_ConnectableElement = Generalization(general=ConnectableElement, specific=form_SubmitFormButton)
gen_form_PreviousFormButton_FormButton = Generalization(general=FormButton, specific=form_PreviousFormButton)
gen_form_NextFormButton_FormButton = Generalization(general=FormButton, specific=form_NextFormButton)
gen_form_Info_Widget = Generalization(general=Widget, specific=form_Info)
gen_form_MultipleValuatedFormField_FormField = Generalization(general=FormField, specific=form_MultipleValuatedFormField)
gen_form_SingleValuatedFormField_FormField = Generalization(general=FormField, specific=form_SingleValuatedFormField)
gen_form_CheckBoxMultipleFormField_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_CheckBoxMultipleFormField)
gen_form_CheckBoxMultipleFormField_ItemContainer = Generalization(general=ItemContainer, specific=form_CheckBoxMultipleFormField)
gen_form_ComboFormField_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_ComboFormField)
gen_form_DateFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_DateFormField)
gen_form_ListFormField_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_ListFormField)
gen_form_PasswordFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_PasswordFormField)
gen_form_RadioFormField_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_RadioFormField)
gen_form_RadioFormField_ItemContainer = Generalization(general=ItemContainer, specific=form_RadioFormField)
gen_form_SelectFormField_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_SelectFormField)
gen_form_HiddenWidget_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_HiddenWidget)
gen_form_HiddenWidget_Duplicable = Generalization(general=Duplicable, specific=form_HiddenWidget)
gen_form_DurationFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_DurationFormField)
gen_form_DurationFormField_ItemContainer = Generalization(general=ItemContainer, specific=form_DurationFormField)
gen_form_AbstractTable_Widget = Generalization(general=Widget, specific=form_AbstractTable)
gen_form_AbstractTable_Duplicable = Generalization(general=Duplicable, specific=form_AbstractTable)
gen_form_TextInfo_Info = Generalization(general=Info, specific=form_TextInfo)
gen_form_TextInfo_Duplicable = Generalization(general=Duplicable, specific=form_TextInfo)
gen_form_MessageInfo_Info = Generalization(general=Info, specific=form_MessageInfo)
gen_form_CheckBoxSingleFormField_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_CheckBoxSingleFormField)
gen_form_FileWidget_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_FileWidget)
gen_form_FileWidget_Duplicable = Generalization(general=Duplicable, specific=form_FileWidget)
gen_form_ImageWidget_Widget = Generalization(general=Widget, specific=form_ImageWidget)
gen_form_ImageWidget_Duplicable = Generalization(general=Duplicable, specific=form_ImageWidget)
gen_form_IFrameWidget_Info = Generalization(general=Info, specific=form_IFrameWidget)
gen_form_MandatoryFieldsCustomization_CSSCustomizable = Generalization(general=CSSCustomizable, specific=form_MandatoryFieldsCustomization)
gen_form_HtmlWidget_Info = Generalization(general=Info, specific=form_HtmlWidget)
gen_form_SuggestBox_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_SuggestBox)
gen_form_Table_AbstractTable = Generalization(general=AbstractTable, specific=form_Table)
gen_form_Table_MultipleValuatedFormField = Generalization(general=MultipleValuatedFormField, specific=form_Table)
gen_form_DynamicTable_AbstractTable = Generalization(general=AbstractTable, specific=form_DynamicTable)
gen_form_DynamicTable_SingleValuatedFormField = Generalization(general=SingleValuatedFormField, specific=form_DynamicTable)
gen_form_GroupIterator_Element = Generalization(general=Element, specific=form_GroupIterator)

# Domain Model
domain_model = DomainModel(
    name="form",
    types={form_Widget, form_Validator, form_WidgetDependency, form_Operation, form_WidgetLayoutInfo, form_Expression, form_Validable, form_Form, ConnectableElement, Validable, form_EStringToStringMapEntry, form_Column, form_Line, Element, CSSCustomizable, form_ItemContainer, form_Duplicable, form_ViewForm, Form, form_CSSCustomizable, form_Group, Widget, Duplicable, form_GroupIterator, form_FormField, form_TextAreaFormField, form_RichTextAreaFormField, form_FormButton, form_SubmitFormButton, FormButton, form_PreviousFormButton, form_NextFormButton, form_Info, form_MultipleValuatedFormField, FormField, form_SingleValuatedFormField, form_CheckBoxMultipleFormField, MultipleValuatedFormField, ItemContainer, form_ComboFormField, form_DateFormField, SingleValuatedFormField, form_ListFormField, form_PasswordFormField, form_RadioFormField, form_SelectFormField, form_TextFormField, form_HiddenWidget, form_DurationFormField, form_AbstractTable, form_TextInfo, Info, form_MessageInfo, form_CheckBoxSingleFormField, form_FileWidget, form_Document, form_ImageWidget, form_IFrameWidget, form_MandatoryFieldsCustomization, form_HtmlWidget, form_SuggestBox, form_TableExpression, form_Table, AbstractTable, form_DynamicTable, EventDependencyType, LabelPosition, FileWidgetInputType, FileWidgetDownloadType},
    associations={widget0, widgets12, pageLabel15, actions18, parameter1, displayName2, validators5, stringAttributes7, columns8, lines10, widgetLayoutInfo39, dependOn41, parentOf44, maxNumberOfDuplication20, minNumberOfDuplication22, displayLabelForAdd25, tooltipForAdd28, displayLabelForRemove31, tooltipForRemove34, htmlAttributes37, widgets74, columns76, lines79, iterator82, displayDependentWidgetOnlyAfterFirstEventTriggeredAndCondition47, displayAfterEventDependsOnConditionScript50, inputExpression53, afterEventExpression56, tooltip59, helpMessage62, displayLabel65, injectWidgetScript68, action71, actions91, exampleMessage84, defaultExpression86, defaultExpressionAfterEvent88, document93, outputDocumentListExpression94, document97, imgPath99, minNumberOfRow119, maxNumberOfColumn122, maxNumberOfRow125, mandatorySymbol128, mandatoryLabel130, horizontalHeaderExpression102, verticalHeaderExpression104, tableExpression107, maxRowForPagination109, columnForInitialSelectionIndex111, selectedValues114, minNumberOfColumn117},
    generalizations={gen_form_Form_ConnectableElement, gen_form_Form_Validable, gen_form_Widget_Element, gen_form_Widget_CSSCustomizable, gen_form_ViewForm_Form, gen_form_Group_Widget, gen_form_Group_Duplicable, gen_form_FormField_Widget, gen_form_FormField_Validable, gen_form_FormField_Duplicable, gen_form_TextFormField_SingleValuatedFormField, gen_form_TextAreaFormField_SingleValuatedFormField, gen_form_RichTextAreaFormField_SingleValuatedFormField, gen_form_FormButton_Widget, gen_form_SubmitFormButton_FormButton, gen_form_SubmitFormButton_ConnectableElement, gen_form_PreviousFormButton_FormButton, gen_form_NextFormButton_FormButton, gen_form_Info_Widget, gen_form_MultipleValuatedFormField_FormField, gen_form_SingleValuatedFormField_FormField, gen_form_CheckBoxMultipleFormField_MultipleValuatedFormField, gen_form_CheckBoxMultipleFormField_ItemContainer, gen_form_ComboFormField_MultipleValuatedFormField, gen_form_DateFormField_SingleValuatedFormField, gen_form_ListFormField_MultipleValuatedFormField, gen_form_PasswordFormField_SingleValuatedFormField, gen_form_RadioFormField_MultipleValuatedFormField, gen_form_RadioFormField_ItemContainer, gen_form_SelectFormField_MultipleValuatedFormField, gen_form_HiddenWidget_SingleValuatedFormField, gen_form_HiddenWidget_Duplicable, gen_form_DurationFormField_SingleValuatedFormField, gen_form_DurationFormField_ItemContainer, gen_form_AbstractTable_Widget, gen_form_AbstractTable_Duplicable, gen_form_TextInfo_Info, gen_form_TextInfo_Duplicable, gen_form_MessageInfo_Info, gen_form_CheckBoxSingleFormField_SingleValuatedFormField, gen_form_FileWidget_SingleValuatedFormField, gen_form_FileWidget_Duplicable, gen_form_ImageWidget_Widget, gen_form_ImageWidget_Duplicable, gen_form_IFrameWidget_Info, gen_form_MandatoryFieldsCustomization_CSSCustomizable, gen_form_HtmlWidget_Info, gen_form_SuggestBox_MultipleValuatedFormField, gen_form_Table_AbstractTable, gen_form_Table_MultipleValuatedFormField, gen_form_DynamicTable_AbstractTable, gen_form_DynamicTable_SingleValuatedFormField, gen_form_GroupIterator_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)