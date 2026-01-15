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
ConditionalTemplateExpType: Enumeration = Enumeration(
    name="ConditionalTemplateExpType",
    literals={
            EnumerationLiteral(name="isNotEmpty")
    }
)

FormMethodType: Enumeration = Enumeration(
    name="FormMethodType",
    literals={
            EnumerationLiteral(name="get"),
			EnumerationLiteral(name="post")
    }
)

ConditionType: Enumeration = Enumeration(
    name="ConditionType",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="implies"),
			EnumerationLiteral(name="dateLessEqual")
    }
)

OrientationType: Enumeration = Enumeration(
    name="OrientationType",
    literals={
            EnumerationLiteral(name="right"),
			EnumerationLiteral(name="left")
    }
)

ContentStyle: Enumeration = Enumeration(
    name="ContentStyle",
    literals={
            EnumerationLiteral(name="hierarchical"),
			EnumerationLiteral(name="normal")
    }
)

# Classes
becontent_BeContentModel = Class(name="becontent::BeContentModel")
becontent_BeContentElement = Class(name="becontent::BeContentElement", is_abstract=True)
becontent_DefinitionItem = Class(name="becontent::DefinitionItem", is_abstract=True)
BeContentElement = Class(name="BeContentElement")
becontent_Entity = Class(name="becontent::Entity", is_abstract=True)
DefinitionItem = Class(name="DefinitionItem")
becontent_SystemEntityField = Class(name="becontent::SystemEntityField", is_abstract=True)
becontent_Relation = Class(name="becontent::Relation", is_abstract=True)
becontent_CustomRelation = Class(name="becontent::CustomRelation")
Relation = Class(name="Relation")
becontent_SystemRelation = Class(name="becontent::SystemRelation")
becontent_EntityField = Class(name="becontent::EntityField", is_abstract=True)
becontent_Channel = Class(name="becontent::Channel")
becontent_Handler = Class(name="becontent::Handler")
becontent_CustomEntity = Class(name="becontent::CustomEntity")
Entity = Class(name="Entity")
becontent_SystemEntity = Class(name="becontent::SystemEntity")
TypedAttribute = Class(name="TypedAttribute")
becontent_AttributeDate = Class(name="becontent::AttributeDate")
becontent_AttributeLongDate = Class(name="becontent::AttributeLongDate")
becontent_AttributeText = Class(name="becontent::AttributeText")
becontent_AttributePassword = Class(name="becontent::AttributePassword")
becontent_AttributePosition = Class(name="becontent::AttributePosition")
becontent_AttributeImage = Class(name="becontent::AttributeImage")
becontent_AttributeInteger = Class(name="becontent::AttributeInteger")
becontent_AttributeVarchar = Class(name="becontent::AttributeVarchar")
becontent_AttributeFile = Class(name="becontent::AttributeFile")
becontent_AttributeFileToFolder = Class(name="becontent::AttributeFileToFolder")
becontent_FileToFolderExtension = Class(name="becontent::FileToFolderExtension")
becontent_Reference = Class(name="becontent::Reference")
EntityField = Class(name="EntityField")
becontent_TypedAttribute = Class(name="becontent::TypedAttribute", is_abstract=True)
becontent_AttributeColor = Class(name="becontent::AttributeColor")
becontent_SystemAttributePosition = Class(name="becontent::SystemAttributePosition")
becontent_SystemAttributeImage = Class(name="becontent::SystemAttributeImage")
becontent_SystemAttributeInteger = Class(name="becontent::SystemAttributeInteger")
becontent_SystemAttributeVarchar = Class(name="becontent::SystemAttributeVarchar")
becontent_SystemAttributeFile = Class(name="becontent::SystemAttributeFile")
becontent_SystemAttributeFileToFolder = Class(name="becontent::SystemAttributeFileToFolder")
becontent_SystemReference = Class(name="becontent::SystemReference")
SystemEntityField = Class(name="SystemEntityField")
becontent_TypedSystemAttribute = Class(name="becontent::TypedSystemAttribute", is_abstract=True)
becontent_SystemAttributeColor = Class(name="becontent::SystemAttributeColor")
TypedSystemAttribute = Class(name="TypedSystemAttribute")
becontent_SystemAttributeDate = Class(name="becontent::SystemAttributeDate")
becontent_SystemAttributeLongDate = Class(name="becontent::SystemAttributeLongDate")
becontent_SystemAttributeText = Class(name="becontent::SystemAttributeText")
becontent_SystemAttributePassword = Class(name="becontent::SystemAttributePassword")
becontent_Template = Class(name="becontent::Template")
ViewItem = Class(name="ViewItem")
becontent_Skinlet = Class(name="becontent::Skinlet")
becontent_Content = Class(name="becontent::Content")
becontent_JoinEntity = Class(name="becontent::JoinEntity")
becontent_ViewItem = Class(name="becontent::ViewItem", is_abstract=True)
becontent_Skin = Class(name="becontent::Skin")
becontent_Parameter = Class(name="becontent::Parameter")
ContentCommand = Class(name="ContentCommand")
becontent_UnsetParameter = Class(name="becontent::UnsetParameter")
becontent_Copy = Class(name="becontent::Copy")
becontent_Propagate = Class(name="becontent::Propagate")
becontent_Trigger = Class(name="becontent::Trigger")
becontent_ApplyCommand = Class(name="becontent::ApplyCommand", is_abstract=True)
becontent_ContentCommand = Class(name="becontent::ContentCommand", is_abstract=True)
becontent_ConditionalTemplate = Class(name="becontent::ConditionalTemplate")
becontent_CustomPager = Class(name="becontent::CustomPager")
becontent_Validation = Class(name="becontent::Validation")
becontent_FormElement = Class(name="becontent::FormElement", is_abstract=True)
FormElement = Class(name="FormElement")
becontent_Apply = Class(name="becontent::Apply")
ApplyCommand = Class(name="ApplyCommand")
becontent_ApplyItem = Class(name="becontent::ApplyItem")
becontent_ApplyIndexed = Class(name="becontent::ApplyIndexed")
becontent_EntityManagerPage = Class(name="becontent::EntityManagerPage")
becontent_Form = Class(name="becontent::Form")
becontent_Section = Class(name="becontent::Section")
NotStructuredElement = Class(name="NotStructuredElement")
becontent_ExtendedForm = Class(name="becontent::ExtendedForm")
Form = Class(name="Form")
becontent_NotStructuredElement = Class(name="becontent::NotStructuredElement", is_abstract=True)
becontent_Checkbox = Class(name="becontent::Checkbox")
becontent_Select = Class(name="becontent::Select")
becontent_Textarea = Class(name="becontent::Textarea")
becontent_Text = Class(name="becontent::Text")
becontent_RadioButton = Class(name="becontent::RadioButton")
becontent_Link = Class(name="becontent::Link")
becontent_Password = Class(name="becontent::Password")
becontent_Date = Class(name="becontent::Date")
becontent_Editor = Class(name="becontent::Editor")
becontent_FileToFolder = Class(name="becontent::FileToFolder")
becontent_Image = Class(name="becontent::Image")
becontent_Color = Class(name="becontent::Color")
becontent_RelationManager = Class(name="becontent::RelationManager")
becontent_LongDate = Class(name="becontent::LongDate")
becontent_File = Class(name="becontent::File")
becontent_SelectFromReference = Class(name="becontent::SelectFromReference")
becontent_RadioFromReference = Class(name="becontent::RadioFromReference")
becontent_Year = Class(name="becontent::Year")
becontent_Position = Class(name="becontent::Position")
becontent_HierarchicalPosition = Class(name="becontent::HierarchicalPosition")
becontent_Hidden = Class(name="becontent::Hidden")

# becontent_BeContentModel class attributes and methods

# becontent_BeContentElement class attributes and methods

# becontent_DefinitionItem class attributes and methods

# BeContentElement class attributes and methods

# becontent_Entity class attributes and methods
becontent_Entity_name: Property = Property(name="name", type=StringType)
becontent_Entity_variableName: Property = Property(name="variableName", type=StringType)
becontent_Entity_isOwned: Property = Property(name="isOwned", type=BooleanType)
becontent_Entity_presentationString: Property = Property(name="presentationString", type=StringType)
becontent_Entity_rssFilter: Property = Property(name="rssFilter", type=StringType)
becontent_Entity.attributes={becontent_Entity_isOwned, becontent_Entity_rssFilter, becontent_Entity_name, becontent_Entity_variableName, becontent_Entity_presentationString}

# DefinitionItem class attributes and methods

# becontent_SystemEntityField class attributes and methods
becontent_SystemEntityField_isPresented: Property = Property(name="isPresented", type=BooleanType)
becontent_SystemEntityField_isTextSearch: Property = Property(name="isTextSearch", type=BooleanType)
becontent_SystemEntityField_isSearchPresentationHead: Property = Property(name="isSearchPresentationHead", type=BooleanType)
becontent_SystemEntityField_isSearchPresentationBody: Property = Property(name="isSearchPresentationBody", type=BooleanType)
becontent_SystemEntityField.attributes={becontent_SystemEntityField_isPresented, becontent_SystemEntityField_isSearchPresentationHead, becontent_SystemEntityField_isSearchPresentationBody, becontent_SystemEntityField_isTextSearch}

# becontent_Relation class attributes and methods
becontent_Relation_name: Property = Property(name="name", type=StringType)
becontent_Relation_variableName: Property = Property(name="variableName", type=StringType)
becontent_Relation.attributes={becontent_Relation_name, becontent_Relation_variableName}

# becontent_CustomRelation class attributes and methods

# Relation class attributes and methods

# becontent_SystemRelation class attributes and methods

# becontent_EntityField class attributes and methods
becontent_EntityField_isPresented: Property = Property(name="isPresented", type=BooleanType)
becontent_EntityField_isTextSearch: Property = Property(name="isTextSearch", type=BooleanType)
becontent_EntityField_isSearchPresentationHead: Property = Property(name="isSearchPresentationHead", type=BooleanType)
becontent_EntityField_isSearchPresentationBody: Property = Property(name="isSearchPresentationBody", type=BooleanType)
becontent_EntityField.attributes={becontent_EntityField_isSearchPresentationHead, becontent_EntityField_isSearchPresentationBody, becontent_EntityField_isTextSearch, becontent_EntityField_isPresented}

# becontent_Channel class attributes and methods
becontent_Channel_parameters: Property = Property(name="parameters", type=StringType)
becontent_Channel__id_model: Property = Property(name="_id_model", type=StringType)
becontent_Channel.attributes={becontent_Channel_parameters, becontent_Channel__id_model}

# becontent_Handler class attributes and methods
becontent_Handler_fileName: Property = Property(name="fileName", type=StringType)
becontent_Handler_mainSkinWithPager: Property = Property(name="mainSkinWithPager", type=BooleanType)
becontent_Handler_mainSkinPagerLength: Property = Property(name="mainSkinPagerLength", type=IntegerType)
becontent_Handler_mainSkinPlaceholder: Property = Property(name="mainSkinPlaceholder", type=StringType)
becontent_Handler.attributes={becontent_Handler_mainSkinWithPager, becontent_Handler_fileName, becontent_Handler_mainSkinPagerLength, becontent_Handler_mainSkinPlaceholder}

# becontent_CustomEntity class attributes and methods

# Entity class attributes and methods

# becontent_SystemEntity class attributes and methods

# TypedAttribute class attributes and methods

# becontent_AttributeDate class attributes and methods

# becontent_AttributeLongDate class attributes and methods

# becontent_AttributeText class attributes and methods

# becontent_AttributePassword class attributes and methods

# becontent_AttributePosition class attributes and methods

# becontent_AttributeImage class attributes and methods

# becontent_AttributeInteger class attributes and methods
becontent_AttributeInteger_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
becontent_AttributeInteger.attributes={becontent_AttributeInteger_isPrimaryKey}

# becontent_AttributeVarchar class attributes and methods
becontent_AttributeVarchar_length: Property = Property(name="length", type=IntegerType)
becontent_AttributeVarchar_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
becontent_AttributeVarchar.attributes={becontent_AttributeVarchar_length, becontent_AttributeVarchar_isPrimaryKey}

# becontent_AttributeFile class attributes and methods

# becontent_AttributeFileToFolder class attributes and methods

# becontent_FileToFolderExtension class attributes and methods
becontent_FileToFolderExtension_extensionKey: Property = Property(name="extensionKey", type=StringType)
becontent_FileToFolderExtension_extensionValue: Property = Property(name="extensionValue", type=StringType)
becontent_FileToFolderExtension__id_model: Property = Property(name="_id_model", type=StringType)
becontent_FileToFolderExtension.attributes={becontent_FileToFolderExtension_extensionKey, becontent_FileToFolderExtension__id_model, becontent_FileToFolderExtension_extensionValue}

# becontent_Reference class attributes and methods
becontent_Reference_name: Property = Property(name="name", type=StringType)
becontent_Reference.attributes={becontent_Reference_name}

# EntityField class attributes and methods

# becontent_TypedAttribute class attributes and methods
becontent_TypedAttribute_name: Property = Property(name="name", type=StringType)
becontent_TypedAttribute_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_TypedAttribute.attributes={becontent_TypedAttribute_name, becontent_TypedAttribute_isMandatory}

# becontent_AttributeColor class attributes and methods

# becontent_SystemAttributePosition class attributes and methods

# becontent_SystemAttributeImage class attributes and methods

# becontent_SystemAttributeInteger class attributes and methods
becontent_SystemAttributeInteger_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
becontent_SystemAttributeInteger.attributes={becontent_SystemAttributeInteger_isPrimaryKey}

# becontent_SystemAttributeVarchar class attributes and methods
becontent_SystemAttributeVarchar_length: Property = Property(name="length", type=IntegerType)
becontent_SystemAttributeVarchar_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
becontent_SystemAttributeVarchar.attributes={becontent_SystemAttributeVarchar_isPrimaryKey, becontent_SystemAttributeVarchar_length}

# becontent_SystemAttributeFile class attributes and methods

# becontent_SystemAttributeFileToFolder class attributes and methods

# becontent_SystemReference class attributes and methods
becontent_SystemReference_name: Property = Property(name="name", type=StringType)
becontent_SystemReference.attributes={becontent_SystemReference_name}

# SystemEntityField class attributes and methods

# becontent_TypedSystemAttribute class attributes and methods
becontent_TypedSystemAttribute_name: Property = Property(name="name", type=StringType)
becontent_TypedSystemAttribute_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_TypedSystemAttribute.attributes={becontent_TypedSystemAttribute_isMandatory, becontent_TypedSystemAttribute_name}

# becontent_SystemAttributeColor class attributes and methods

# TypedSystemAttribute class attributes and methods

# becontent_SystemAttributeDate class attributes and methods

# becontent_SystemAttributeLongDate class attributes and methods

# becontent_SystemAttributeText class attributes and methods

# becontent_SystemAttributePassword class attributes and methods

# becontent_Template class attributes and methods
becontent_Template_path: Property = Property(name="path", type=StringType)
becontent_Template__id_model: Property = Property(name="_id_model", type=StringType)
becontent_Template.attributes={becontent_Template_path, becontent_Template__id_model}

# ViewItem class attributes and methods

# becontent_Skinlet class attributes and methods
becontent_Skinlet_template: Property = Property(name="template", type=StringType)
becontent_Skinlet__id_model: Property = Property(name="_id_model", type=StringType)
becontent_Skinlet.attributes={becontent_Skinlet_template, becontent_Skinlet__id_model}

# becontent_Content class attributes and methods
becontent_Content_template: Property = Property(name="template", type=StringType)
becontent_Content_presentationFields: Property = Property(name="presentationFields", type=StringType)
becontent_Content_orderFields: Property = Property(name="orderFields", type=StringType)
becontent_Content_joinCondition: Property = Property(name="joinCondition", type=StringType)
becontent_Content_filter: Property = Property(name="filter", type=StringType)
becontent_Content_limit: Property = Property(name="limit", type=IntegerType)
becontent_Content_style: Property = Property(name="style", type=StringType)
becontent_Content__id_model: Property = Property(name="_id_model", type=StringType)
becontent_Content.attributes={becontent_Content_joinCondition, becontent_Content_presentationFields, becontent_Content__id_model, becontent_Content_style, becontent_Content_limit, becontent_Content_template, becontent_Content_orderFields, becontent_Content_filter}

# becontent_JoinEntity class attributes and methods
becontent_JoinEntity__id_model: Property = Property(name="_id_model", type=StringType)
becontent_JoinEntity.attributes={becontent_JoinEntity__id_model}

# becontent_ViewItem class attributes and methods

# becontent_Skin class attributes and methods
becontent_Skin_name: Property = Property(name="name", type=StringType)
becontent_Skin.attributes={becontent_Skin_name}

# becontent_Parameter class attributes and methods
becontent_Parameter_name: Property = Property(name="name", type=StringType)
becontent_Parameter_value: Property = Property(name="value", type=StringType)
becontent_Parameter.attributes={becontent_Parameter_name, becontent_Parameter_value}

# ContentCommand class attributes and methods

# becontent_UnsetParameter class attributes and methods
becontent_UnsetParameter_name: Property = Property(name="name", type=StringType)
becontent_UnsetParameter.attributes={becontent_UnsetParameter_name}

# becontent_Copy class attributes and methods
becontent_Copy_fieldName1: Property = Property(name="fieldName1", type=StringType)
becontent_Copy_fieldName2: Property = Property(name="fieldName2", type=StringType)
becontent_Copy.attributes={becontent_Copy_fieldName1, becontent_Copy_fieldName2}

# becontent_Propagate class attributes and methods
becontent_Propagate_fieldName1: Property = Property(name="fieldName1", type=StringType)
becontent_Propagate_fieldName2: Property = Property(name="fieldName2", type=StringType)
becontent_Propagate.attributes={becontent_Propagate_fieldName1, becontent_Propagate_fieldName2}

# becontent_Trigger class attributes and methods
becontent_Trigger_name: Property = Property(name="name", type=StringType)
becontent_Trigger_value: Property = Property(name="value", type=StringType)
becontent_Trigger.attributes={becontent_Trigger_name, becontent_Trigger_value}

# becontent_ApplyCommand class attributes and methods

# becontent_ContentCommand class attributes and methods
becontent_ContentCommand__id_model: Property = Property(name="_id_model", type=StringType)
becontent_ContentCommand.attributes={becontent_ContentCommand__id_model}

# becontent_ConditionalTemplate class attributes and methods
becontent_ConditionalTemplate__id_model: Property = Property(name="_id_model", type=StringType)
becontent_ConditionalTemplate_trueTemplate: Property = Property(name="trueTemplate", type=StringType)
becontent_ConditionalTemplate_falseTemplate: Property = Property(name="falseTemplate", type=StringType)
becontent_ConditionalTemplate_conditionExp: Property = Property(name="conditionExp", type=StringType)
becontent_ConditionalTemplate_fieldName: Property = Property(name="fieldName", type=StringType)
becontent_ConditionalTemplate.attributes={becontent_ConditionalTemplate_conditionExp, becontent_ConditionalTemplate_falseTemplate, becontent_ConditionalTemplate__id_model, becontent_ConditionalTemplate_fieldName, becontent_ConditionalTemplate_trueTemplate}

# becontent_CustomPager class attributes and methods
becontent_CustomPager__id_model: Property = Property(name="_id_model", type=StringType)
becontent_CustomPager_className: Property = Property(name="className", type=StringType)
becontent_CustomPager_length: Property = Property(name="length", type=IntegerType)
becontent_CustomPager_template: Property = Property(name="template", type=StringType)
becontent_CustomPager_query: Property = Property(name="query", type=StringType)
becontent_CustomPager_filter: Property = Property(name="filter", type=StringType)
becontent_CustomPager_order: Property = Property(name="order", type=StringType)
becontent_CustomPager.attributes={becontent_CustomPager_className, becontent_CustomPager_template, becontent_CustomPager_filter, becontent_CustomPager_query, becontent_CustomPager__id_model, becontent_CustomPager_order, becontent_CustomPager_length}

# becontent_Validation class attributes and methods
becontent_Validation_condition: Property = Property(name="condition", type=StringType)
becontent_Validation_message: Property = Property(name="message", type=StringType)
becontent_Validation__id_model: Property = Property(name="_id_model", type=StringType)
becontent_Validation.attributes={becontent_Validation_condition, becontent_Validation__id_model, becontent_Validation_message}

# becontent_FormElement class attributes and methods

# FormElement class attributes and methods

# becontent_Apply class attributes and methods
becontent_Apply_prefix: Property = Property(name="prefix", type=StringType)
becontent_Apply.attributes={becontent_Apply_prefix}

# ApplyCommand class attributes and methods

# becontent_ApplyItem class attributes and methods
becontent_ApplyItem_key: Property = Property(name="key", type=StringType)
becontent_ApplyItem_prefix: Property = Property(name="prefix", type=StringType)
becontent_ApplyItem.attributes={becontent_ApplyItem_key, becontent_ApplyItem_prefix}

# becontent_ApplyIndexed class attributes and methods

# becontent_EntityManagerPage class attributes and methods
becontent_EntityManagerPage_fileName: Property = Property(name="fileName", type=StringType)
becontent_EntityManagerPage_skin: Property = Property(name="skin", type=StringType)
becontent_EntityManagerPage.attributes={becontent_EntityManagerPage_fileName, becontent_EntityManagerPage_skin}

# becontent_Form class attributes and methods
becontent_Form_name: Property = Property(name="name", type=StringType)
becontent_Form_method: Property = Property(name="method", type=StringType)
becontent_Form_description: Property = Property(name="description", type=StringType)
becontent_Form.attributes={becontent_Form_method, becontent_Form_name, becontent_Form_description}

# becontent_Section class attributes and methods
becontent_Section_name: Property = Property(name="name", type=StringType)
becontent_Section_text: Property = Property(name="text", type=StringType)
becontent_Section.attributes={becontent_Section_text, becontent_Section_name}

# NotStructuredElement class attributes and methods

# becontent_ExtendedForm class attributes and methods
becontent_ExtendedForm_className: Property = Property(name="className", type=StringType)
becontent_ExtendedForm.attributes={becontent_ExtendedForm_className}

# Form class attributes and methods

# becontent_NotStructuredElement class attributes and methods
becontent_NotStructuredElement_helper: Property = Property(name="helper", type=StringType)
becontent_NotStructuredElement.attributes={becontent_NotStructuredElement_helper}

# becontent_Checkbox class attributes and methods
becontent_Checkbox_name: Property = Property(name="name", type=StringType)
becontent_Checkbox_label: Property = Property(name="label", type=StringType)
becontent_Checkbox_value: Property = Property(name="value", type=StringType)
becontent_Checkbox_isChecked: Property = Property(name="isChecked", type=BooleanType)
becontent_Checkbox.attributes={becontent_Checkbox_name, becontent_Checkbox_isChecked, becontent_Checkbox_label, becontent_Checkbox_value}

# becontent_Select class attributes and methods
becontent_Select_name: Property = Property(name="name", type=StringType)
becontent_Select_label: Property = Property(name="label", type=StringType)
becontent_Select_values: Property = Property(name="values", type=StringType)
becontent_Select_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Select.attributes={becontent_Select_values, becontent_Select_isMandatory, becontent_Select_name, becontent_Select_label}

# becontent_Textarea class attributes and methods
becontent_Textarea_name: Property = Property(name="name", type=StringType)
becontent_Textarea_label: Property = Property(name="label", type=StringType)
becontent_Textarea_rows: Property = Property(name="rows", type=IntegerType)
becontent_Textarea_columns: Property = Property(name="columns", type=IntegerType)
becontent_Textarea_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Textarea.attributes={becontent_Textarea_label, becontent_Textarea_isMandatory, becontent_Textarea_columns, becontent_Textarea_rows, becontent_Textarea_name}

# becontent_Text class attributes and methods
becontent_Text_name: Property = Property(name="name", type=StringType)
becontent_Text_label: Property = Property(name="label", type=StringType)
becontent_Text_size: Property = Property(name="size", type=IntegerType)
becontent_Text_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Text_maxLength: Property = Property(name="maxLength", type=IntegerType)
becontent_Text.attributes={becontent_Text_isMandatory, becontent_Text_size, becontent_Text_name, becontent_Text_label, becontent_Text_maxLength}

# becontent_RadioButton class attributes and methods
becontent_RadioButton_name: Property = Property(name="name", type=StringType)
becontent_RadioButton_label: Property = Property(name="label", type=StringType)
becontent_RadioButton_values: Property = Property(name="values", type=StringType)
becontent_RadioButton.attributes={becontent_RadioButton_label, becontent_RadioButton_name, becontent_RadioButton_values}

# becontent_Link class attributes and methods
becontent_Link_name: Property = Property(name="name", type=StringType)
becontent_Link_label: Property = Property(name="label", type=StringType)
becontent_Link_size: Property = Property(name="size", type=IntegerType)
becontent_Link_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Link_maxLength: Property = Property(name="maxLength", type=IntegerType)
becontent_Link.attributes={becontent_Link_name, becontent_Link_isMandatory, becontent_Link_size, becontent_Link_label, becontent_Link_maxLength}

# becontent_Password class attributes and methods
becontent_Password_name: Property = Property(name="name", type=StringType)
becontent_Password_label: Property = Property(name="label", type=StringType)
becontent_Password_size: Property = Property(name="size", type=IntegerType)
becontent_Password_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Password_maxLength: Property = Property(name="maxLength", type=IntegerType)
becontent_Password.attributes={becontent_Password_isMandatory, becontent_Password_label, becontent_Password_maxLength, becontent_Password_name, becontent_Password_size}

# becontent_Date class attributes and methods
becontent_Date_name: Property = Property(name="name", type=StringType)
becontent_Date_label: Property = Property(name="label", type=StringType)
becontent_Date_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Date.attributes={becontent_Date_label, becontent_Date_name, becontent_Date_isMandatory}

# becontent_Editor class attributes and methods
becontent_Editor_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Editor_name: Property = Property(name="name", type=StringType)
becontent_Editor_label: Property = Property(name="label", type=StringType)
becontent_Editor_rows: Property = Property(name="rows", type=IntegerType)
becontent_Editor_columns: Property = Property(name="columns", type=IntegerType)
becontent_Editor.attributes={becontent_Editor_isMandatory, becontent_Editor_name, becontent_Editor_columns, becontent_Editor_rows, becontent_Editor_label}

# becontent_FileToFolder class attributes and methods
becontent_FileToFolder_name: Property = Property(name="name", type=StringType)
becontent_FileToFolder_label: Property = Property(name="label", type=StringType)
becontent_FileToFolder_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_FileToFolder_extension: Property = Property(name="extension", type=StringType)
becontent_FileToFolder_extensionMessage: Property = Property(name="extensionMessage", type=StringType)
becontent_FileToFolder.attributes={becontent_FileToFolder_isMandatory, becontent_FileToFolder_extension, becontent_FileToFolder_label, becontent_FileToFolder_name, becontent_FileToFolder_extensionMessage}

# becontent_Image class attributes and methods
becontent_Image_name: Property = Property(name="name", type=StringType)
becontent_Image_label: Property = Property(name="label", type=StringType)
becontent_Image_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Image.attributes={becontent_Image_isMandatory, becontent_Image_name, becontent_Image_label}

# becontent_Color class attributes and methods
becontent_Color_name: Property = Property(name="name", type=StringType)
becontent_Color_label: Property = Property(name="label", type=StringType)
becontent_Color_defaultColor: Property = Property(name="defaultColor", type=StringType)
becontent_Color.attributes={becontent_Color_label, becontent_Color_defaultColor, becontent_Color_name}

# becontent_RelationManager class attributes and methods
becontent_RelationManager_name: Property = Property(name="name", type=StringType)
becontent_RelationManager_label: Property = Property(name="label", type=StringType)
becontent_RelationManager_orientation: Property = Property(name="orientation", type=StringType)
becontent_RelationManager_restrictCondition: Property = Property(name="restrictCondition", type=StringType)
becontent_RelationManager.attributes={becontent_RelationManager_orientation, becontent_RelationManager_restrictCondition, becontent_RelationManager_label, becontent_RelationManager_name}

# becontent_LongDate class attributes and methods
becontent_LongDate_name: Property = Property(name="name", type=StringType)
becontent_LongDate_label: Property = Property(name="label", type=StringType)
becontent_LongDate_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_LongDate.attributes={becontent_LongDate_isMandatory, becontent_LongDate_name, becontent_LongDate_label}

# becontent_File class attributes and methods
becontent_File_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_File_extension: Property = Property(name="extension", type=StringType)
becontent_File_extensionMessage: Property = Property(name="extensionMessage", type=StringType)
becontent_File_name: Property = Property(name="name", type=StringType)
becontent_File_label: Property = Property(name="label", type=StringType)
becontent_File.attributes={becontent_File_extensionMessage, becontent_File_extension, becontent_File_isMandatory, becontent_File_name, becontent_File_label}

# becontent_SelectFromReference class attributes and methods
becontent_SelectFromReference_name: Property = Property(name="name", type=StringType)
becontent_SelectFromReference_label: Property = Property(name="label", type=StringType)
becontent_SelectFromReference_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_SelectFromReference_restrictCondition: Property = Property(name="restrictCondition", type=StringType)
becontent_SelectFromReference.attributes={becontent_SelectFromReference_isMandatory, becontent_SelectFromReference_name, becontent_SelectFromReference_label, becontent_SelectFromReference_restrictCondition}

# becontent_RadioFromReference class attributes and methods
becontent_RadioFromReference_name: Property = Property(name="name", type=StringType)
becontent_RadioFromReference_label: Property = Property(name="label", type=StringType)
becontent_RadioFromReference_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_RadioFromReference_restrictCondition: Property = Property(name="restrictCondition", type=StringType)
becontent_RadioFromReference.attributes={becontent_RadioFromReference_name, becontent_RadioFromReference_label, becontent_RadioFromReference_restrictCondition, becontent_RadioFromReference_isMandatory}

# becontent_Year class attributes and methods
becontent_Year_name: Property = Property(name="name", type=StringType)
becontent_Year_label: Property = Property(name="label", type=StringType)
becontent_Year_start: Property = Property(name="start", type=IntegerType)
becontent_Year_end: Property = Property(name="end", type=IntegerType)
becontent_Year_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Year.attributes={becontent_Year_name, becontent_Year_start, becontent_Year_label, becontent_Year_end, becontent_Year_isMandatory}

# becontent_Position class attributes and methods
becontent_Position_name: Property = Property(name="name", type=StringType)
becontent_Position_label: Property = Property(name="label", type=StringType)
becontent_Position_controlledField: Property = Property(name="controlledField", type=StringType)
becontent_Position_size: Property = Property(name="size", type=IntegerType)
becontent_Position_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
becontent_Position.attributes={becontent_Position_isMandatory, becontent_Position_name, becontent_Position_label, becontent_Position_size, becontent_Position_controlledField}

# becontent_HierarchicalPosition class attributes and methods
becontent_HierarchicalPosition_referenceField: Property = Property(name="referenceField", type=StringType)
becontent_HierarchicalPosition_size: Property = Property(name="size", type=IntegerType)
becontent_HierarchicalPosition_name: Property = Property(name="name", type=StringType)
becontent_HierarchicalPosition_label: Property = Property(name="label", type=StringType)
becontent_HierarchicalPosition_controlledField: Property = Property(name="controlledField", type=StringType)
becontent_HierarchicalPosition.attributes={becontent_HierarchicalPosition_size, becontent_HierarchicalPosition_controlledField, becontent_HierarchicalPosition_label, becontent_HierarchicalPosition_name, becontent_HierarchicalPosition_referenceField}

# becontent_Hidden class attributes and methods
becontent_Hidden_name: Property = Property(name="name", type=StringType)
becontent_Hidden_values: Property = Property(name="values", type=StringType)
becontent_Hidden.attributes={becontent_Hidden_name, becontent_Hidden_values}

# Relationships
modelElements0: BinaryAssociation = BinaryAssociation(
    name="modelElements0",
    ends={
        Property(name="becontent_BeContentElement", type=becontent_BeContentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_BeContentModel", type=becontent_BeContentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemFields6: BinaryAssociation = BinaryAssociation(
    name="systemFields6",
    ends={
        Property(name="becontent_SystemEntityField", type=becontent_SystemEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_SystemEntity", type=becontent_SystemEntityField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftForeignkey7: BinaryAssociation = BinaryAssociation(
    name="leftForeignkey7",
    ends={
        Property(name="becontent_Entity8", type=becontent_CustomRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_CustomRelation", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
rightForeignkey9: BinaryAssociation = BinaryAssociation(
    name="rightForeignkey9",
    ends={
        Property(name="becontent_Entity11", type=becontent_CustomRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_CustomRelation10", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
leftForeignkey12: BinaryAssociation = BinaryAssociation(
    name="leftForeignkey12",
    ends={
        Property(name="becontent_SystemEntity13", type=becontent_SystemRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_SystemRelation", type=becontent_SystemEntity, multiplicity=Multiplicity(1, 1))
    }
)
rightForeignkey14: BinaryAssociation = BinaryAssociation(
    name="rightForeignkey14",
    ends={
        Property(name="becontent_SystemEntity16", type=becontent_SystemRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_SystemRelation15", type=becontent_SystemEntity, multiplicity=Multiplicity(1, 1))
    }
)
fields1: BinaryAssociation = BinaryAssociation(
    name="fields1",
    ends={
        Property(name="becontent_EntityField", type=becontent_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Entity", type=becontent_EntityField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rss2: BinaryAssociation = BinaryAssociation(
    name="rss2",
    ends={
        Property(name="becontent_Channel", type=becontent_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Entity3", type=becontent_Channel, multiplicity=Multiplicity(0, 1))
    }
)
handler4: BinaryAssociation = BinaryAssociation(
    name="handler4",
    ends={
        Property(name="becontent_Handler", type=becontent_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Entity5", type=becontent_Handler, multiplicity=Multiplicity(0, 1))
    }
)
fileExtensions19: BinaryAssociation = BinaryAssociation(
    name="fileExtensions19",
    ends={
        Property(name="becontent_FileToFolderExtension", type=becontent_AttributeFileToFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_AttributeFileToFolder", type=becontent_FileToFolderExtension, multiplicity=Multiplicity(0, 9999))
    }
)
referredEntity17: BinaryAssociation = BinaryAssociation(
    name="referredEntity17",
    ends={
        Property(name="becontent_Entity18", type=becontent_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Reference", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
fileExtensions22: BinaryAssociation = BinaryAssociation(
    name="fileExtensions22",
    ends={
        Property(name="becontent_FileToFolderExtension23", type=becontent_SystemAttributeFileToFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_SystemAttributeFileToFolder", type=becontent_FileToFolderExtension, multiplicity=Multiplicity(0, 9999))
    }
)
channel24: BinaryAssociation = BinaryAssociation(
    name="channel24",
    ends={
        Property(name="becontent_Entity26", type=becontent_Channel, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Channel25", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
referredEntity20: BinaryAssociation = BinaryAssociation(
    name="referredEntity20",
    ends={
        Property(name="becontent_SystemEntity21", type=becontent_SystemReference, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_SystemReference", type=becontent_SystemEntity, multiplicity=Multiplicity(1, 1))
    }
)
mainEntity34: BinaryAssociation = BinaryAssociation(
    name="mainEntity34",
    ends={
        Property(name="becontent_Entity35", type=becontent_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Content", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
joinEntities36: BinaryAssociation = BinaryAssociation(
    name="joinEntities36",
    ends={
        Property(name="becontent_JoinEntity", type=becontent_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Content37", type=becontent_JoinEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewItems27: BinaryAssociation = BinaryAssociation(
    name="viewItems27",
    ends={
        Property(name="becontent_ViewItem", type=becontent_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Handler28", type=becontent_ViewItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mainSkin29: BinaryAssociation = BinaryAssociation(
    name="mainSkin29",
    ends={
        Property(name="becontent_Skin", type=becontent_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Handler30", type=becontent_Skin, multiplicity=Multiplicity(1, 1))
    }
)
mainSkinGetContent31: BinaryAssociation = BinaryAssociation(
    name="mainSkinGetContent31",
    ends={
        Property(name="becontent_ViewItem33", type=becontent_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Handler32", type=becontent_ViewItem, multiplicity=Multiplicity(1, 1))
    }
)
viewItem48: BinaryAssociation = BinaryAssociation(
    name="viewItem48",
    ends={
        Property(name="becontent_ViewItem49", type=becontent_ApplyCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_ApplyCommand", type=becontent_ViewItem, multiplicity=Multiplicity(1, 1))
    }
)
commands38: BinaryAssociation = BinaryAssociation(
    name="commands38",
    ends={
        Property(name="becontent_ContentCommand", type=becontent_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Content39", type=becontent_ContentCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalTemplate40: BinaryAssociation = BinaryAssociation(
    name="conditionalTemplate40",
    ends={
        Property(name="becontent_ConditionalTemplate", type=becontent_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Content41", type=becontent_ConditionalTemplate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinRule43: BinaryAssociation = BinaryAssociation(
    name="joinRule43",
    ends={
        Property(name="becontent_JoinEntity44", type=becontent_JoinEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_JoinEntity42", type=becontent_JoinEntity, multiplicity=Multiplicity(0, 1))
    }
)
referredEntity45: BinaryAssociation = BinaryAssociation(
    name="referredEntity45",
    ends={
        Property(name="becontent_Entity47", type=becontent_JoinEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_JoinEntity46", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
forms50: BinaryAssociation = BinaryAssociation(
    name="forms50",
    ends={
        Property(name="becontent_Form", type=becontent_EntityManagerPage, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_EntityManagerPage", type=becontent_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customPagers51: BinaryAssociation = BinaryAssociation(
    name="customPagers51",
    ends={
        Property(name="becontent_CustomPager", type=becontent_EntityManagerPage, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_EntityManagerPage52", type=becontent_CustomPager, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validations53: BinaryAssociation = BinaryAssociation(
    name="validations53",
    ends={
        Property(name="becontent_Validation", type=becontent_EntityManagerPage, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_EntityManagerPage54", type=becontent_Validation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainEntity55: BinaryAssociation = BinaryAssociation(
    name="mainEntity55",
    ends={
        Property(name="becontent_DefinitionItem", type=becontent_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Form56", type=becontent_DefinitionItem, multiplicity=Multiplicity(1, 1))
    }
)
elements57: BinaryAssociation = BinaryAssociation(
    name="elements57",
    ends={
        Property(name="becontent_FormElement", type=becontent_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Form58", type=becontent_FormElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customPager59: BinaryAssociation = BinaryAssociation(
    name="customPager59",
    ends={
        Property(name="becontent_CustomPager61", type=becontent_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Form60", type=becontent_CustomPager, multiplicity=Multiplicity(0, 1))
    }
)
firstElement65: BinaryAssociation = BinaryAssociation(
    name="firstElement65",
    ends={
        Property(name="becontent_NotStructuredElement", type=becontent_Validation, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Validation66", type=becontent_NotStructuredElement, multiplicity=Multiplicity(1, 1))
    }
)
secondElement67: BinaryAssociation = BinaryAssociation(
    name="secondElement67",
    ends={
        Property(name="becontent_NotStructuredElement69", type=becontent_Validation, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Validation68", type=becontent_NotStructuredElement, multiplicity=Multiplicity(1, 1))
    }
)
validations62: BinaryAssociation = BinaryAssociation(
    name="validations62",
    ends={
        Property(name="becontent_Validation64", type=becontent_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_Form63", type=becontent_Validation, multiplicity=Multiplicity(0, 9999))
    }
)
referredEntity70: BinaryAssociation = BinaryAssociation(
    name="referredEntity70",
    ends={
        Property(name="becontent_Entity71", type=becontent_SelectFromReference, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_SelectFromReference", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)
referredEntity72: BinaryAssociation = BinaryAssociation(
    name="referredEntity72",
    ends={
        Property(name="becontent_Entity73", type=becontent_RadioFromReference, multiplicity=Multiplicity(1, 1)),
        Property(name="becontent_RadioFromReference", type=becontent_Entity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_becontent_DefinitionItem_BeContentElement = Generalization(general=BeContentElement, specific=becontent_DefinitionItem)
gen_becontent_Entity_DefinitionItem = Generalization(general=DefinitionItem, specific=becontent_Entity)
gen_becontent_SystemEntity_Entity = Generalization(general=Entity, specific=becontent_SystemEntity)
gen_becontent_Relation_DefinitionItem = Generalization(general=DefinitionItem, specific=becontent_Relation)
gen_becontent_CustomRelation_Relation = Generalization(general=Relation, specific=becontent_CustomRelation)
gen_becontent_SystemRelation_Relation = Generalization(general=Relation, specific=becontent_SystemRelation)
gen_becontent_CustomEntity_Entity = Generalization(general=Entity, specific=becontent_CustomEntity)
gen_becontent_AttributeColor_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeColor)
gen_becontent_AttributeDate_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeDate)
gen_becontent_AttributeLongDate_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeLongDate)
gen_becontent_AttributeText_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeText)
gen_becontent_AttributePassword_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributePassword)
gen_becontent_AttributePosition_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributePosition)
gen_becontent_AttributeImage_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeImage)
gen_becontent_AttributeInteger_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeInteger)
gen_becontent_AttributeVarchar_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeVarchar)
gen_becontent_AttributeFile_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeFile)
gen_becontent_AttributeFileToFolder_TypedAttribute = Generalization(general=TypedAttribute, specific=becontent_AttributeFileToFolder)
gen_becontent_Reference_EntityField = Generalization(general=EntityField, specific=becontent_Reference)
gen_becontent_TypedAttribute_EntityField = Generalization(general=EntityField, specific=becontent_TypedAttribute)
gen_becontent_SystemAttributePosition_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributePosition)
gen_becontent_SystemAttributeImage_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeImage)
gen_becontent_SystemAttributeInteger_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeInteger)
gen_becontent_SystemAttributeVarchar_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeVarchar)
gen_becontent_SystemAttributeFile_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeFile)
gen_becontent_SystemAttributeFileToFolder_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeFileToFolder)
gen_becontent_FileToFolderExtension_BeContentElement = Generalization(general=BeContentElement, specific=becontent_FileToFolderExtension)
gen_becontent_Channel_BeContentElement = Generalization(general=BeContentElement, specific=becontent_Channel)
gen_becontent_SystemReference_SystemEntityField = Generalization(general=SystemEntityField, specific=becontent_SystemReference)
gen_becontent_TypedSystemAttribute_SystemEntityField = Generalization(general=SystemEntityField, specific=becontent_TypedSystemAttribute)
gen_becontent_SystemAttributeColor_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeColor)
gen_becontent_SystemAttributeDate_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeDate)
gen_becontent_SystemAttributeLongDate_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeLongDate)
gen_becontent_SystemAttributeText_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributeText)
gen_becontent_SystemAttributePassword_TypedSystemAttribute = Generalization(general=TypedSystemAttribute, specific=becontent_SystemAttributePassword)
gen_becontent_Template_ViewItem = Generalization(general=ViewItem, specific=becontent_Template)
gen_becontent_Skinlet_ViewItem = Generalization(general=ViewItem, specific=becontent_Skinlet)
gen_becontent_Skin_ViewItem = Generalization(general=ViewItem, specific=becontent_Skin)
gen_becontent_Content_ViewItem = Generalization(general=ViewItem, specific=becontent_Content)
gen_becontent_Handler_BeContentElement = Generalization(general=BeContentElement, specific=becontent_Handler)
gen_becontent_Parameter_ContentCommand = Generalization(general=ContentCommand, specific=becontent_Parameter)
gen_becontent_UnsetParameter_ContentCommand = Generalization(general=ContentCommand, specific=becontent_UnsetParameter)
gen_becontent_Copy_ContentCommand = Generalization(general=ContentCommand, specific=becontent_Copy)
gen_becontent_Propagate_ContentCommand = Generalization(general=ContentCommand, specific=becontent_Propagate)
gen_becontent_Trigger_ContentCommand = Generalization(general=ContentCommand, specific=becontent_Trigger)
gen_becontent_ApplyCommand_ContentCommand = Generalization(general=ContentCommand, specific=becontent_ApplyCommand)
gen_becontent_Form_FormElement = Generalization(general=FormElement, specific=becontent_Form)
gen_becontent_Apply_ApplyCommand = Generalization(general=ApplyCommand, specific=becontent_Apply)
gen_becontent_ApplyItem_ApplyCommand = Generalization(general=ApplyCommand, specific=becontent_ApplyItem)
gen_becontent_ApplyIndexed_ApplyCommand = Generalization(general=ApplyCommand, specific=becontent_ApplyIndexed)
gen_becontent_EntityManagerPage_BeContentElement = Generalization(general=BeContentElement, specific=becontent_EntityManagerPage)
gen_becontent_Section_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Section)
gen_becontent_ExtendedForm_Form = Generalization(general=Form, specific=becontent_ExtendedForm)
gen_becontent_NotStructuredElement_FormElement = Generalization(general=FormElement, specific=becontent_NotStructuredElement)
gen_becontent_Checkbox_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Checkbox)
gen_becontent_Select_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Select)
gen_becontent_Textarea_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Textarea)
gen_becontent_Text_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Text)
gen_becontent_RadioButton_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_RadioButton)
gen_becontent_Link_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Link)
gen_becontent_Password_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Password)
gen_becontent_Date_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Date)
gen_becontent_Editor_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Editor)
gen_becontent_FileToFolder_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_FileToFolder)
gen_becontent_Image_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Image)
gen_becontent_Color_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Color)
gen_becontent_RelationManager_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_RelationManager)
gen_becontent_LongDate_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_LongDate)
gen_becontent_File_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_File)
gen_becontent_SelectFromReference_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_SelectFromReference)
gen_becontent_RadioFromReference_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_RadioFromReference)
gen_becontent_Position_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Position)
gen_becontent_HierarchicalPosition_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_HierarchicalPosition)
gen_becontent_Year_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Year)
gen_becontent_Hidden_NotStructuredElement = Generalization(general=NotStructuredElement, specific=becontent_Hidden)

# Domain Model
domain_model = DomainModel(
    name="becontent",
    types={becontent_BeContentModel, becontent_BeContentElement, becontent_DefinitionItem, BeContentElement, becontent_Entity, DefinitionItem, becontent_SystemEntityField, becontent_Relation, becontent_CustomRelation, Relation, becontent_SystemRelation, becontent_EntityField, becontent_Channel, becontent_Handler, becontent_CustomEntity, Entity, becontent_SystemEntity, TypedAttribute, becontent_AttributeDate, becontent_AttributeLongDate, becontent_AttributeText, becontent_AttributePassword, becontent_AttributePosition, becontent_AttributeImage, becontent_AttributeInteger, becontent_AttributeVarchar, becontent_AttributeFile, becontent_AttributeFileToFolder, becontent_FileToFolderExtension, becontent_Reference, EntityField, becontent_TypedAttribute, becontent_AttributeColor, becontent_SystemAttributePosition, becontent_SystemAttributeImage, becontent_SystemAttributeInteger, becontent_SystemAttributeVarchar, becontent_SystemAttributeFile, becontent_SystemAttributeFileToFolder, becontent_SystemReference, SystemEntityField, becontent_TypedSystemAttribute, becontent_SystemAttributeColor, TypedSystemAttribute, becontent_SystemAttributeDate, becontent_SystemAttributeLongDate, becontent_SystemAttributeText, becontent_SystemAttributePassword, becontent_Template, ViewItem, becontent_Skinlet, becontent_Content, becontent_JoinEntity, becontent_ViewItem, becontent_Skin, becontent_Parameter, ContentCommand, becontent_UnsetParameter, becontent_Copy, becontent_Propagate, becontent_Trigger, becontent_ApplyCommand, becontent_ContentCommand, becontent_ConditionalTemplate, becontent_CustomPager, becontent_Validation, becontent_FormElement, FormElement, becontent_Apply, ApplyCommand, becontent_ApplyItem, becontent_ApplyIndexed, becontent_EntityManagerPage, becontent_Form, becontent_Section, NotStructuredElement, becontent_ExtendedForm, Form, becontent_NotStructuredElement, becontent_Checkbox, becontent_Select, becontent_Textarea, becontent_Text, becontent_RadioButton, becontent_Link, becontent_Password, becontent_Date, becontent_Editor, becontent_FileToFolder, becontent_Image, becontent_Color, becontent_RelationManager, becontent_LongDate, becontent_File, becontent_SelectFromReference, becontent_RadioFromReference, becontent_Year, becontent_Position, becontent_HierarchicalPosition, becontent_Hidden, ConditionalTemplateExpType, FormMethodType, ConditionType, OrientationType, ContentStyle},
    associations={modelElements0, systemFields6, leftForeignkey7, rightForeignkey9, leftForeignkey12, rightForeignkey14, fields1, rss2, handler4, fileExtensions19, referredEntity17, fileExtensions22, channel24, referredEntity20, mainEntity34, joinEntities36, viewItems27, mainSkin29, mainSkinGetContent31, viewItem48, commands38, conditionalTemplate40, joinRule43, referredEntity45, forms50, customPagers51, validations53, mainEntity55, elements57, customPager59, firstElement65, secondElement67, validations62, referredEntity70, referredEntity72},
    generalizations={gen_becontent_DefinitionItem_BeContentElement, gen_becontent_Entity_DefinitionItem, gen_becontent_SystemEntity_Entity, gen_becontent_Relation_DefinitionItem, gen_becontent_CustomRelation_Relation, gen_becontent_SystemRelation_Relation, gen_becontent_CustomEntity_Entity, gen_becontent_AttributeColor_TypedAttribute, gen_becontent_AttributeDate_TypedAttribute, gen_becontent_AttributeLongDate_TypedAttribute, gen_becontent_AttributeText_TypedAttribute, gen_becontent_AttributePassword_TypedAttribute, gen_becontent_AttributePosition_TypedAttribute, gen_becontent_AttributeImage_TypedAttribute, gen_becontent_AttributeInteger_TypedAttribute, gen_becontent_AttributeVarchar_TypedAttribute, gen_becontent_AttributeFile_TypedAttribute, gen_becontent_AttributeFileToFolder_TypedAttribute, gen_becontent_Reference_EntityField, gen_becontent_TypedAttribute_EntityField, gen_becontent_SystemAttributePosition_TypedSystemAttribute, gen_becontent_SystemAttributeImage_TypedSystemAttribute, gen_becontent_SystemAttributeInteger_TypedSystemAttribute, gen_becontent_SystemAttributeVarchar_TypedSystemAttribute, gen_becontent_SystemAttributeFile_TypedSystemAttribute, gen_becontent_SystemAttributeFileToFolder_TypedSystemAttribute, gen_becontent_FileToFolderExtension_BeContentElement, gen_becontent_Channel_BeContentElement, gen_becontent_SystemReference_SystemEntityField, gen_becontent_TypedSystemAttribute_SystemEntityField, gen_becontent_SystemAttributeColor_TypedSystemAttribute, gen_becontent_SystemAttributeDate_TypedSystemAttribute, gen_becontent_SystemAttributeLongDate_TypedSystemAttribute, gen_becontent_SystemAttributeText_TypedSystemAttribute, gen_becontent_SystemAttributePassword_TypedSystemAttribute, gen_becontent_Template_ViewItem, gen_becontent_Skinlet_ViewItem, gen_becontent_Skin_ViewItem, gen_becontent_Content_ViewItem, gen_becontent_Handler_BeContentElement, gen_becontent_Parameter_ContentCommand, gen_becontent_UnsetParameter_ContentCommand, gen_becontent_Copy_ContentCommand, gen_becontent_Propagate_ContentCommand, gen_becontent_Trigger_ContentCommand, gen_becontent_ApplyCommand_ContentCommand, gen_becontent_Form_FormElement, gen_becontent_Apply_ApplyCommand, gen_becontent_ApplyItem_ApplyCommand, gen_becontent_ApplyIndexed_ApplyCommand, gen_becontent_EntityManagerPage_BeContentElement, gen_becontent_Section_NotStructuredElement, gen_becontent_ExtendedForm_Form, gen_becontent_NotStructuredElement_FormElement, gen_becontent_Checkbox_NotStructuredElement, gen_becontent_Select_NotStructuredElement, gen_becontent_Textarea_NotStructuredElement, gen_becontent_Text_NotStructuredElement, gen_becontent_RadioButton_NotStructuredElement, gen_becontent_Link_NotStructuredElement, gen_becontent_Password_NotStructuredElement, gen_becontent_Date_NotStructuredElement, gen_becontent_Editor_NotStructuredElement, gen_becontent_FileToFolder_NotStructuredElement, gen_becontent_Image_NotStructuredElement, gen_becontent_Color_NotStructuredElement, gen_becontent_RelationManager_NotStructuredElement, gen_becontent_LongDate_NotStructuredElement, gen_becontent_File_NotStructuredElement, gen_becontent_SelectFromReference_NotStructuredElement, gen_becontent_RadioFromReference_NotStructuredElement, gen_becontent_Position_NotStructuredElement, gen_becontent_HierarchicalPosition_NotStructuredElement, gen_becontent_Year_NotStructuredElement, gen_becontent_Hidden_NotStructuredElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)