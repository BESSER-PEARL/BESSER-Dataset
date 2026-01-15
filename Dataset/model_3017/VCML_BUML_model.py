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
OptionType: Enumeration = Enumeration(
    name="OptionType",
    literals={
            EnumerationLiteral(name="ECM"),
			EnumerationLiteral(name="UPS"),
			EnumerationLiteral(name="KeyDate")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="InPreparation"),
			EnumerationLiteral(name="Locked"),
			EnumerationLiteral(name="Released")
    }
)

Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="DE"),
			EnumerationLiteral(name="EL"),
			EnumerationLiteral(name="EN"),
			EnumerationLiteral(name="ES"),
			EnumerationLiteral(name="ET"),
			EnumerationLiteral(name="FI"),
			EnumerationLiteral(name="FR"),
			EnumerationLiteral(name="HE"),
			EnumerationLiteral(name="HR"),
			EnumerationLiteral(name="HU"),
			EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="IS"),
			EnumerationLiteral(name="AF"),
			EnumerationLiteral(name="AR"),
			EnumerationLiteral(name="BG"),
			EnumerationLiteral(name="CA"),
			EnumerationLiteral(name="CS"),
			EnumerationLiteral(name="DA"),
			EnumerationLiteral(name="SV"),
			EnumerationLiteral(name="TH"),
			EnumerationLiteral(name="TR"),
			EnumerationLiteral(name="UK"),
			EnumerationLiteral(name="Z1"),
			EnumerationLiteral(name="ZF"),
			EnumerationLiteral(name="ZH"),
			EnumerationLiteral(name="IT"),
			EnumerationLiteral(name="JA"),
			EnumerationLiteral(name="KO"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LV"),
			EnumerationLiteral(name="MS"),
			EnumerationLiteral(name="NL"),
			EnumerationLiteral(name="NO"),
			EnumerationLiteral(name="PL"),
			EnumerationLiteral(name="PT"),
			EnumerationLiteral(name="RO"),
			EnumerationLiteral(name="RU"),
			EnumerationLiteral(name="SH"),
			EnumerationLiteral(name="SK"),
			EnumerationLiteral(name="SL"),
			EnumerationLiteral(name="SR")
    }
)

UnaryExpressionOperator: Enumeration = Enumeration(
    name="UnaryExpressionOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="LC"),
			EnumerationLiteral(name="UC")
    }
)

ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LE")
    }
)

FunctionName: Enumeration = Enumeration(
    name="FunctionName",
    literals={
            EnumerationLiteral(name="SIN"),
			EnumerationLiteral(name="COS"),
			EnumerationLiteral(name="TAN"),
			EnumerationLiteral(name="EXP"),
			EnumerationLiteral(name="LN"),
			EnumerationLiteral(name="ABS"),
			EnumerationLiteral(name="SQRT"),
			EnumerationLiteral(name="LOG10"),
			EnumerationLiteral(name="ARCSIN"),
			EnumerationLiteral(name="ARCCOS"),
			EnumerationLiteral(name="ARCTAN"),
			EnumerationLiteral(name="SIGN"),
			EnumerationLiteral(name="FRAC"),
			EnumerationLiteral(name="CEIL"),
			EnumerationLiteral(name="TRUNK"),
			EnumerationLiteral(name="FLOOR")
    }
)

ProcedureLocation: Enumeration = Enumeration(
    name="ProcedureLocation",
    literals={
            EnumerationLiteral(name="ROOT"),
			EnumerationLiteral(name="SELF"),
			EnumerationLiteral(name="PARENT")
    }
)

Fixing: Enumeration = Enumeration(
    name="Fixing",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Entry"),
			EnumerationLiteral(name="TopDown"),
			EnumerationLiteral(name="BottomUp")
    }
)

# Classes
vcml_VcmlModel = Class(name="vcml::VcmlModel")
vcml_Import = Class(name="vcml::Import")
vcml_Option = Class(name="vcml::Option")
vcml_VCObject = Class(name="vcml::VCObject")
vcml_BOMItem = Class(name="vcml::BOMItem", is_abstract=True)
vcml_Material = Class(name="vcml::Material")
vcml_SelectionCondition = Class(name="vcml::SelectionCondition")
vcml_ConfigurationProfileEntry = Class(name="vcml::ConfigurationProfileEntry")
vcml_BOMItem_Material = Class(name="vcml::BOMItem::Material")
BOMItem = Class(name="BOMItem")
vcml_BOMItem_Class = Class(name="vcml::BOMItem::Class")
vcml_Class = Class(name="vcml::Class")
vcml_Characteristic = Class(name="vcml::Characteristic")
vcml_Documentation = Class(name="vcml::Documentation")
vcml_CharacteristicType = Class(name="vcml::CharacteristicType")
vcml_CharacteristicOrValueDependencies = Class(name="vcml::CharacteristicOrValueDependencies")
vcml_NumericType = Class(name="vcml::NumericType")
CharacteristicType = Class(name="CharacteristicType")
vcml_Description = Class(name="vcml::Description")
vcml_BillOfMaterial = Class(name="vcml::BillOfMaterial")
VCObject = Class(name="VCObject")
vcml_CharacteristicValue = Class(name="vcml::CharacteristicValue")
vcml_DateType = Class(name="vcml::DateType")
vcml_DateCharacteristicValue = Class(name="vcml::DateCharacteristicValue")
vcml_NumberListEntry = Class(name="vcml::NumberListEntry")
vcml_Dependency = Class(name="vcml::Dependency")
vcml_NumericCharacteristicValue = Class(name="vcml::NumericCharacteristicValue")
vcml_SymbolicType = Class(name="vcml::SymbolicType")
vcml_DependencyNet = Class(name="vcml::DependencyNet")
vcml_Procedure = Class(name="vcml::Procedure")
Dependency = Class(name="Dependency")
vcml_ProcedureSource = Class(name="vcml::ProcedureSource")
vcml_ConditionSource = Class(name="vcml::ConditionSource")
vcml_Precondition = Class(name="vcml::Precondition")
vcml_Condition = Class(name="vcml::Condition")
vcml_ConfigurationProfile = Class(name="vcml::ConfigurationProfile")
vcml_Constraint = Class(name="vcml::Constraint")
vcml_InterfaceDesign = Class(name="vcml::InterfaceDesign")
vcml_ConstraintSource = Class(name="vcml::ConstraintSource")
vcml_CharacteristicGroup = Class(name="vcml::CharacteristicGroup")
vcml_Classification = Class(name="vcml::Classification")
vcml_Literal = Class(name="vcml::Literal")
vcml_VariantFunction = Class(name="vcml::VariantFunction")
vcml_VariantFunctionArgument = Class(name="vcml::VariantFunctionArgument")
vcml_VariantTable = Class(name="vcml::VariantTable")
vcml_VariantTableArgument = Class(name="vcml::VariantTableArgument")
vcml_ValueAssignment = Class(name="vcml::ValueAssignment")
vcml_SimpleDescription = Class(name="vcml::SimpleDescription")
Description = Class(name="Description")
vcml_VariantTableContent = Class(name="vcml::VariantTableContent")
vcml_Row = Class(name="vcml::Row")
vcml_MultiLanguageDescriptions = Class(name="vcml::MultiLanguageDescriptions")
vcml_MultiLanguageDescription = Class(name="vcml::MultiLanguageDescription")
vcml_SimpleDocumentation = Class(name="vcml::SimpleDocumentation")
Documentation = Class(name="Documentation")
vcml_ConstraintRestriction = Class(name="vcml::ConstraintRestriction")
vcml_CharacteristicReference_C = Class(name="vcml::CharacteristicReference::C")
vcml_ShortVarDefinition = Class(name="vcml::ShortVarDefinition")
vcml_MultipleLanguageDocumentation = Class(name="vcml::MultipleLanguageDocumentation")
vcml_MultipleLanguageDocumentation_LanguageBlock = Class(name="vcml::MultipleLanguageDocumentation::LanguageBlock")
vcml_FormattedDocumentationBlock = Class(name="vcml::FormattedDocumentationBlock")
vcml_ConstraintObject = Class(name="vcml::ConstraintObject")
vcml_PartOfCondition = Class(name="vcml::PartOfCondition")
ConstraintRestriction = Class(name="ConstraintRestriction")
Condition = Class(name="Condition")
vcml_ConstraintClass = Class(name="vcml::ConstraintClass")
ConstraintObject = Class(name="ConstraintObject")
vcml_ConstraintMaterial = Class(name="vcml::ConstraintMaterial")
vcml_ObjectType = Class(name="vcml::ObjectType")
vcml_PartialKey = Class(name="vcml::PartialKey")
Literal = Class(name="Literal")
vcml_ObjectCharacteristicReference = Class(name="vcml::ObjectCharacteristicReference")
CharacteristicReference_C = Class(name="CharacteristicReference::C")
vcml_ShortVarReference = Class(name="vcml::ShortVarReference")
vcml_SubpartOfCondition = Class(name="vcml::SubpartOfCondition")
vcml_ConstraintRestrictionFalse = Class(name="vcml::ConstraintRestrictionFalse")
vcml_NegatedConstraintRestrictionLHS = Class(name="vcml::NegatedConstraintRestrictionLHS")
vcml_EObject = Class(name="vcml::EObject")
vcml_FunctionOrTable = Class(name="vcml::FunctionOrTable")
vcml_Function = Class(name="vcml::Function")
FunctionOrTable = Class(name="FunctionOrTable")
vcml_Statement = Class(name="vcml::Statement")
vcml_CompoundStatement = Class(name="vcml::CompoundStatement")
Statement = Class(name="Statement")
vcml_SimpleStatement = Class(name="vcml::SimpleStatement")
vcml_Assignment = Class(name="vcml::Assignment")
SimpleStatement = Class(name="SimpleStatement")
vcml_Expression = Class(name="vcml::Expression")
vcml_SetOrDelDefault = Class(name="vcml::SetOrDelDefault")
vcml_PFunction = Class(name="vcml::PFunction")
vcml_Table = Class(name="vcml::Table")
vcml_CharacteristicReference_P = Class(name="vcml::CharacteristicReference::P")
vcml_SetDefault = Class(name="vcml::SetDefault")
SetOrDelDefault = Class(name="SetOrDelDefault")
vcml_DelDefault = Class(name="vcml::DelDefault")
vcml_IsInvisible = Class(name="vcml::IsInvisible")
vcml_SetPricingFactor = Class(name="vcml::SetPricingFactor")
vcml_CountParts = Class(name="vcml::CountParts")
vcml_MDataCharacteristic_C = Class(name="vcml::MDataCharacteristic::C")
vcml_MDataCharacteristic_P = Class(name="vcml::MDataCharacteristic::P")
vcml_UnaryExpression = Class(name="vcml::UnaryExpression")
Expression = Class(name="Expression")
vcml_FunctionCall = Class(name="vcml::FunctionCall")
vcml_SumParts = Class(name="vcml::SumParts")
vcml_IsSpecified_C = Class(name="vcml::IsSpecified::C")
vcml_NumericLiteral = Class(name="vcml::NumericLiteral")
NumberListEntry = Class(name="NumberListEntry")
vcml_SymbolicLiteral = Class(name="vcml::SymbolicLiteral")
vcml_UnaryCondition = Class(name="vcml::UnaryCondition")
vcml_Comparison = Class(name="vcml::Comparison")
vcml_InCondition_P = Class(name="vcml::InCondition::P")
vcml_NumberList = Class(name="vcml::NumberList")
List = Class(name="List")
vcml_IsSpecified_P = Class(name="vcml::IsSpecified::P")
vcml_TypeOf = Class(name="vcml::TypeOf")
vcml_InCondition_C = Class(name="vcml::InCondition::C")
vcml_List = Class(name="vcml::List")
vcml_NumericInterval = Class(name="vcml::NumericInterval")
vcml_SymbolList = Class(name="vcml::SymbolList")
vcml_ConditionalConstraintRestriction = Class(name="vcml::ConditionalConstraintRestriction")
vcml_ConditionalStatement = Class(name="vcml::ConditionalStatement")
vcml_BinaryExpression = Class(name="vcml::BinaryExpression")
vcml_BinaryCondition = Class(name="vcml::BinaryCondition")

# vcml_VcmlModel class attributes and methods

# vcml_Import class attributes and methods
vcml_Import_importURI: Property = Property(name="importURI", type=StringType)
vcml_Import.attributes={vcml_Import_importURI}

# vcml_Option class attributes and methods
vcml_Option_name: Property = Property(name="name", type=StringType)
vcml_Option_value: Property = Property(name="value", type=StringType)
vcml_Option.attributes={vcml_Option_value, vcml_Option_name}

# vcml_VCObject class attributes and methods
vcml_VCObject_name: Property = Property(name="name", type=StringType)
vcml_VCObject.attributes={vcml_VCObject_name}

# vcml_BOMItem class attributes and methods
vcml_BOMItem_itemnumber: Property = Property(name="itemnumber", type=IntegerType)
vcml_BOMItem.attributes={vcml_BOMItem_itemnumber}

# vcml_Material class attributes and methods
vcml_Material_type: Property = Property(name="type", type=StringType)
vcml_Material.attributes={vcml_Material_type}

# vcml_SelectionCondition class attributes and methods
vcml_SelectionCondition_status: Property = Property(name="status", type=StringType)
vcml_SelectionCondition_group: Property = Property(name="group", type=StringType)
vcml_SelectionCondition.attributes={vcml_SelectionCondition_status, vcml_SelectionCondition_group}

# vcml_ConfigurationProfileEntry class attributes and methods
vcml_ConfigurationProfileEntry_sequence: Property = Property(name="sequence", type=IntegerType)
vcml_ConfigurationProfileEntry.attributes={vcml_ConfigurationProfileEntry_sequence}

# vcml_BOMItem_Material class attributes and methods

# BOMItem class attributes and methods

# vcml_BOMItem_Class class attributes and methods

# vcml_Class class attributes and methods
vcml_Class_status: Property = Property(name="status", type=StringType)
vcml_Class_group: Property = Property(name="group", type=StringType)
vcml_Class.attributes={vcml_Class_status, vcml_Class_group}

# vcml_Characteristic class attributes and methods
vcml_Characteristic_status: Property = Property(name="status", type=StringType)
vcml_Characteristic_group: Property = Property(name="group", type=StringType)
vcml_Characteristic_additionalValues: Property = Property(name="additionalValues", type=BooleanType)
vcml_Characteristic_required: Property = Property(name="required", type=BooleanType)
vcml_Characteristic_restrictable: Property = Property(name="restrictable", type=BooleanType)
vcml_Characteristic_noDisplay: Property = Property(name="noDisplay", type=BooleanType)
vcml_Characteristic_notReadyForInput: Property = Property(name="notReadyForInput", type=BooleanType)
vcml_Characteristic_multiValue: Property = Property(name="multiValue", type=BooleanType)
vcml_Characteristic_displayAllowedValues: Property = Property(name="displayAllowedValues", type=BooleanType)
vcml_Characteristic_table: Property = Property(name="table", type=StringType)
vcml_Characteristic_field: Property = Property(name="field", type=StringType)
vcml_Characteristic.attributes={vcml_Characteristic_status, vcml_Characteristic_group, vcml_Characteristic_required, vcml_Characteristic_additionalValues, vcml_Characteristic_field, vcml_Characteristic_restrictable, vcml_Characteristic_displayAllowedValues, vcml_Characteristic_table, vcml_Characteristic_multiValue, vcml_Characteristic_notReadyForInput, vcml_Characteristic_noDisplay}

# vcml_Documentation class attributes and methods

# vcml_CharacteristicType class attributes and methods
vcml_CharacteristicType_numberOfChars: Property = Property(name="numberOfChars", type=IntegerType)
vcml_CharacteristicType.attributes={vcml_CharacteristicType_numberOfChars}

# vcml_CharacteristicOrValueDependencies class attributes and methods

# vcml_NumericType class attributes and methods
vcml_NumericType_decimalPlaces: Property = Property(name="decimalPlaces", type=IntegerType)
vcml_NumericType_unit: Property = Property(name="unit", type=StringType)
vcml_NumericType_negativeValuesAllowed: Property = Property(name="negativeValuesAllowed", type=BooleanType)
vcml_NumericType_intervalValuesAllowed: Property = Property(name="intervalValuesAllowed", type=BooleanType)
vcml_NumericType.attributes={vcml_NumericType_intervalValuesAllowed, vcml_NumericType_unit, vcml_NumericType_decimalPlaces, vcml_NumericType_negativeValuesAllowed}

# CharacteristicType class attributes and methods

# vcml_Description class attributes and methods

# vcml_BillOfMaterial class attributes and methods

# VCObject class attributes and methods

# vcml_CharacteristicValue class attributes and methods
vcml_CharacteristicValue_name: Property = Property(name="name", type=StringType)
vcml_CharacteristicValue_default: Property = Property(name="default", type=BooleanType)
vcml_CharacteristicValue.attributes={vcml_CharacteristicValue_name, vcml_CharacteristicValue_default}

# vcml_DateType class attributes and methods
vcml_DateType_intervalValuesAllowed: Property = Property(name="intervalValuesAllowed", type=BooleanType)
vcml_DateType.attributes={vcml_DateType_intervalValuesAllowed}

# vcml_DateCharacteristicValue class attributes and methods
vcml_DateCharacteristicValue_from: Property = Property(name="from", type=StringType)
vcml_DateCharacteristicValue_to: Property = Property(name="to", type=StringType)
vcml_DateCharacteristicValue_default: Property = Property(name="default", type=BooleanType)
vcml_DateCharacteristicValue.attributes={vcml_DateCharacteristicValue_from, vcml_DateCharacteristicValue_to, vcml_DateCharacteristicValue_default}

# vcml_NumberListEntry class attributes and methods

# vcml_Dependency class attributes and methods

# vcml_NumericCharacteristicValue class attributes and methods
vcml_NumericCharacteristicValue_default: Property = Property(name="default", type=BooleanType)
vcml_NumericCharacteristicValue.attributes={vcml_NumericCharacteristicValue_default}

# vcml_SymbolicType class attributes and methods
vcml_SymbolicType_caseSensitive: Property = Property(name="caseSensitive", type=BooleanType)
vcml_SymbolicType.attributes={vcml_SymbolicType_caseSensitive}

# vcml_DependencyNet class attributes and methods
vcml_DependencyNet_status: Property = Property(name="status", type=StringType)
vcml_DependencyNet_group: Property = Property(name="group", type=StringType)
vcml_DependencyNet.attributes={vcml_DependencyNet_group, vcml_DependencyNet_status}

# vcml_Procedure class attributes and methods
vcml_Procedure_status: Property = Property(name="status", type=StringType)
vcml_Procedure_group: Property = Property(name="group", type=StringType)
vcml_Procedure.attributes={vcml_Procedure_group, vcml_Procedure_status}

# Dependency class attributes and methods

# vcml_ProcedureSource class attributes and methods

# vcml_ConditionSource class attributes and methods

# vcml_Precondition class attributes and methods
vcml_Precondition_status: Property = Property(name="status", type=StringType)
vcml_Precondition_group: Property = Property(name="group", type=StringType)
vcml_Precondition.attributes={vcml_Precondition_status, vcml_Precondition_group}

# vcml_Condition class attributes and methods

# vcml_ConfigurationProfile class attributes and methods
vcml_ConfigurationProfile_fixing: Property = Property(name="fixing", type=StringType)
vcml_ConfigurationProfile_status: Property = Property(name="status", type=StringType)
vcml_ConfigurationProfile_bomapplication: Property = Property(name="bomapplication", type=StringType)
vcml_ConfigurationProfile.attributes={vcml_ConfigurationProfile_status, vcml_ConfigurationProfile_bomapplication, vcml_ConfigurationProfile_fixing}

# vcml_Constraint class attributes and methods
vcml_Constraint_status: Property = Property(name="status", type=StringType)
vcml_Constraint_group: Property = Property(name="group", type=StringType)
vcml_Constraint.attributes={vcml_Constraint_group, vcml_Constraint_status}

# vcml_InterfaceDesign class attributes and methods

# vcml_ConstraintSource class attributes and methods

# vcml_CharacteristicGroup class attributes and methods
vcml_CharacteristicGroup_name: Property = Property(name="name", type=StringType)
vcml_CharacteristicGroup.attributes={vcml_CharacteristicGroup_name}

# vcml_Classification class attributes and methods

# vcml_Literal class attributes and methods

# vcml_VariantFunction class attributes and methods
vcml_VariantFunction_status: Property = Property(name="status", type=StringType)
vcml_VariantFunction_group: Property = Property(name="group", type=StringType)
vcml_VariantFunction.attributes={vcml_VariantFunction_status, vcml_VariantFunction_group}

# vcml_VariantFunctionArgument class attributes and methods
vcml_VariantFunctionArgument_in: Property = Property(name="in", type=BooleanType)
vcml_VariantFunctionArgument.attributes={vcml_VariantFunctionArgument_in}

# vcml_VariantTable class attributes and methods
vcml_VariantTable_status: Property = Property(name="status", type=StringType)
vcml_VariantTable_group: Property = Property(name="group", type=StringType)
vcml_VariantTable.attributes={vcml_VariantTable_status, vcml_VariantTable_group}

# vcml_VariantTableArgument class attributes and methods
vcml_VariantTableArgument_key: Property = Property(name="key", type=BooleanType)
vcml_VariantTableArgument.attributes={vcml_VariantTableArgument_key}

# vcml_ValueAssignment class attributes and methods

# vcml_SimpleDescription class attributes and methods
vcml_SimpleDescription_value: Property = Property(name="value", type=StringType)
vcml_SimpleDescription.attributes={vcml_SimpleDescription_value}

# Description class attributes and methods

# vcml_VariantTableContent class attributes and methods

# vcml_Row class attributes and methods

# vcml_MultiLanguageDescriptions class attributes and methods

# vcml_MultiLanguageDescription class attributes and methods
vcml_MultiLanguageDescription_language: Property = Property(name="language", type=StringType)
vcml_MultiLanguageDescription_value: Property = Property(name="value", type=StringType)
vcml_MultiLanguageDescription.attributes={vcml_MultiLanguageDescription_language, vcml_MultiLanguageDescription_value}

# vcml_SimpleDocumentation class attributes and methods
vcml_SimpleDocumentation_value: Property = Property(name="value", type=StringType)
vcml_SimpleDocumentation.attributes={vcml_SimpleDocumentation_value}

# Documentation class attributes and methods

# vcml_ConstraintRestriction class attributes and methods

# vcml_CharacteristicReference_C class attributes and methods

# vcml_ShortVarDefinition class attributes and methods
vcml_ShortVarDefinition_name: Property = Property(name="name", type=StringType)
vcml_ShortVarDefinition.attributes={vcml_ShortVarDefinition_name}

# vcml_MultipleLanguageDocumentation class attributes and methods

# vcml_MultipleLanguageDocumentation_LanguageBlock class attributes and methods
vcml_MultipleLanguageDocumentation_LanguageBlock_language: Property = Property(name="language", type=StringType)
vcml_MultipleLanguageDocumentation_LanguageBlock.attributes={vcml_MultipleLanguageDocumentation_LanguageBlock_language}

# vcml_FormattedDocumentationBlock class attributes and methods
vcml_FormattedDocumentationBlock_value: Property = Property(name="value", type=StringType)
vcml_FormattedDocumentationBlock_format: Property = Property(name="format", type=StringType)
vcml_FormattedDocumentationBlock.attributes={vcml_FormattedDocumentationBlock_value, vcml_FormattedDocumentationBlock_format}

# vcml_ConstraintObject class attributes and methods
vcml_ConstraintObject_name: Property = Property(name="name", type=StringType)
vcml_ConstraintObject.attributes={vcml_ConstraintObject_name}

# vcml_PartOfCondition class attributes and methods

# ConstraintRestriction class attributes and methods

# Condition class attributes and methods

# vcml_ConstraintClass class attributes and methods

# ConstraintObject class attributes and methods

# vcml_ConstraintMaterial class attributes and methods

# vcml_ObjectType class attributes and methods
vcml_ObjectType_type: Property = Property(name="type", type=StringType)
vcml_ObjectType_classType: Property = Property(name="classType", type=IntegerType)
vcml_ObjectType.attributes={vcml_ObjectType_classType, vcml_ObjectType_type}

# vcml_PartialKey class attributes and methods
vcml_PartialKey_key: Property = Property(name="key", type=StringType)
vcml_PartialKey.attributes={vcml_PartialKey_key}

# Literal class attributes and methods

# vcml_ObjectCharacteristicReference class attributes and methods

# CharacteristicReference_C class attributes and methods

# vcml_ShortVarReference class attributes and methods

# vcml_SubpartOfCondition class attributes and methods

# vcml_ConstraintRestrictionFalse class attributes and methods

# vcml_NegatedConstraintRestrictionLHS class attributes and methods

# vcml_EObject class attributes and methods

# vcml_FunctionOrTable class attributes and methods

# vcml_Function class attributes and methods

# FunctionOrTable class attributes and methods

# vcml_Statement class attributes and methods

# vcml_CompoundStatement class attributes and methods

# Statement class attributes and methods

# vcml_SimpleStatement class attributes and methods

# vcml_Assignment class attributes and methods

# SimpleStatement class attributes and methods

# vcml_Expression class attributes and methods

# vcml_SetOrDelDefault class attributes and methods

# vcml_PFunction class attributes and methods

# vcml_Table class attributes and methods

# vcml_CharacteristicReference_P class attributes and methods
vcml_CharacteristicReference_P_location: Property = Property(name="location", type=StringType)
vcml_CharacteristicReference_P.attributes={vcml_CharacteristicReference_P_location}

# vcml_SetDefault class attributes and methods

# SetOrDelDefault class attributes and methods

# vcml_DelDefault class attributes and methods

# vcml_IsInvisible class attributes and methods

# vcml_SetPricingFactor class attributes and methods
vcml_SetPricingFactor_location: Property = Property(name="location", type=StringType)
vcml_SetPricingFactor.attributes={vcml_SetPricingFactor_location}

# vcml_CountParts class attributes and methods
vcml_CountParts_location: Property = Property(name="location", type=StringType)
vcml_CountParts.attributes={vcml_CountParts_location}

# vcml_MDataCharacteristic_C class attributes and methods

# vcml_MDataCharacteristic_P class attributes and methods

# vcml_UnaryExpression class attributes and methods
vcml_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
vcml_UnaryExpression.attributes={vcml_UnaryExpression_operator}

# Expression class attributes and methods

# vcml_FunctionCall class attributes and methods
vcml_FunctionCall_function: Property = Property(name="function", type=StringType)
vcml_FunctionCall.attributes={vcml_FunctionCall_function}

# vcml_SumParts class attributes and methods
vcml_SumParts_location: Property = Property(name="location", type=StringType)
vcml_SumParts.attributes={vcml_SumParts_location}

# vcml_IsSpecified_C class attributes and methods

# vcml_NumericLiteral class attributes and methods
vcml_NumericLiteral_value: Property = Property(name="value", type=StringType)
vcml_NumericLiteral.attributes={vcml_NumericLiteral_value}

# NumberListEntry class attributes and methods

# vcml_SymbolicLiteral class attributes and methods
vcml_SymbolicLiteral_value: Property = Property(name="value", type=StringType)
vcml_SymbolicLiteral.attributes={vcml_SymbolicLiteral_value}

# vcml_UnaryCondition class attributes and methods

# vcml_Comparison class attributes and methods
vcml_Comparison_operator: Property = Property(name="operator", type=StringType)
vcml_Comparison.attributes={vcml_Comparison_operator}

# vcml_InCondition_P class attributes and methods

# vcml_NumberList class attributes and methods

# List class attributes and methods

# vcml_IsSpecified_P class attributes and methods

# vcml_TypeOf class attributes and methods
vcml_TypeOf_location: Property = Property(name="location", type=StringType)
vcml_TypeOf.attributes={vcml_TypeOf_location}

# vcml_InCondition_C class attributes and methods

# vcml_List class attributes and methods

# vcml_NumericInterval class attributes and methods
vcml_NumericInterval_lowerBound: Property = Property(name="lowerBound", type=StringType)
vcml_NumericInterval_upperBound: Property = Property(name="upperBound", type=StringType)
vcml_NumericInterval_lowerBoundOp: Property = Property(name="lowerBoundOp", type=StringType)
vcml_NumericInterval_upperBoundOp: Property = Property(name="upperBoundOp", type=StringType)
vcml_NumericInterval.attributes={vcml_NumericInterval_lowerBoundOp, vcml_NumericInterval_upperBoundOp, vcml_NumericInterval_upperBound, vcml_NumericInterval_lowerBound}

# vcml_SymbolList class attributes and methods

# vcml_ConditionalConstraintRestriction class attributes and methods

# vcml_ConditionalStatement class attributes and methods

# vcml_BinaryExpression class attributes and methods
vcml_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
vcml_BinaryExpression.attributes={vcml_BinaryExpression_operator}

# vcml_BinaryCondition class attributes and methods
vcml_BinaryCondition_operator: Property = Property(name="operator", type=StringType)
vcml_BinaryCondition.attributes={vcml_BinaryCondition_operator}

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="vcml_Import", type=vcml_VcmlModel, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VcmlModel", type=vcml_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options1: BinaryAssociation = BinaryAssociation(
    name="options1",
    ends={
        Property(name="vcml_Option", type=vcml_VcmlModel, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VcmlModel2", type=vcml_Option, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects3: BinaryAssociation = BinaryAssociation(
    name="objects3",
    ends={
        Property(name="vcml_VCObject", type=vcml_VcmlModel, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VcmlModel4", type=vcml_VCObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items10: BinaryAssociation = BinaryAssociation(
    name="items10",
    ends={
        Property(name="vcml_BOMItem", type=vcml_BillOfMaterial, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BillOfMaterial", type=vcml_BOMItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
material11: BinaryAssociation = BinaryAssociation(
    name="material11",
    ends={
        Property(name="Material", type=vcml_BillOfMaterial, multiplicity=Multiplicity(1, 1)),
        Property(name="billofmaterials", type=vcml_Material, multiplicity=Multiplicity(0, 1))
    }
)
selectionCondition12: BinaryAssociation = BinaryAssociation(
    name="selectionCondition12",
    ends={
        Property(name="vcml_SelectionCondition", type=vcml_BOMItem, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BOMItem13", type=vcml_SelectionCondition, multiplicity=Multiplicity(0, 1))
    }
)
entries14: BinaryAssociation = BinaryAssociation(
    name="entries14",
    ends={
        Property(name="vcml_ConfigurationProfileEntry", type=vcml_BOMItem, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BOMItem15", type=vcml_ConfigurationProfileEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
material16: BinaryAssociation = BinaryAssociation(
    name="material16",
    ends={
        Property(name="vcml_Material", type=vcml_BOMItem_Material, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BOMItem_Material", type=vcml_Material, multiplicity=Multiplicity(0, 1))
    }
)
cls17: BinaryAssociation = BinaryAssociation(
    name="cls17",
    ends={
        Property(name="vcml_Class", type=vcml_BOMItem_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BOMItem_Class", type=vcml_Class, multiplicity=Multiplicity(0, 1))
    }
)
documentation18: BinaryAssociation = BinaryAssociation(
    name="documentation18",
    ends={
        Property(name="vcml_Documentation", type=vcml_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Characteristic", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="vcml_CharacteristicType", type=vcml_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Characteristic20", type=vcml_CharacteristicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies21: BinaryAssociation = BinaryAssociation(
    name="dependencies21",
    ends={
        Property(name="vcml_CharacteristicOrValueDependencies", type=vcml_Characteristic, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Characteristic22", type=vcml_CharacteristicOrValueDependencies, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description5: BinaryAssociation = BinaryAssociation(
    name="description5",
    ends={
        Property(name="vcml_Description", type=vcml_VCObject, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VCObject6", type=vcml_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
options7: BinaryAssociation = BinaryAssociation(
    name="options7",
    ends={
        Property(name="vcml_Option9", type=vcml_VCObject, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VCObject8", type=vcml_Option, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values24: BinaryAssociation = BinaryAssociation(
    name="values24",
    ends={
        Property(name="vcml_CharacteristicValue", type=vcml_SymbolicType, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SymbolicType", type=vcml_CharacteristicValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values25: BinaryAssociation = BinaryAssociation(
    name="values25",
    ends={
        Property(name="vcml_DateCharacteristicValue", type=vcml_DateType, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_DateType", type=vcml_DateCharacteristicValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description26: BinaryAssociation = BinaryAssociation(
    name="description26",
    ends={
        Property(name="vcml_Description28", type=vcml_CharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicValue27", type=vcml_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation29: BinaryAssociation = BinaryAssociation(
    name="documentation29",
    ends={
        Property(name="vcml_Documentation31", type=vcml_CharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicValue30", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies32: BinaryAssociation = BinaryAssociation(
    name="dependencies32",
    ends={
        Property(name="vcml_CharacteristicOrValueDependencies34", type=vcml_CharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicValue33", type=vcml_CharacteristicOrValueDependencies, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry35: BinaryAssociation = BinaryAssociation(
    name="entry35",
    ends={
        Property(name="vcml_NumberListEntry", type=vcml_NumericCharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_NumericCharacteristicValue36", type=vcml_NumberListEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation37: BinaryAssociation = BinaryAssociation(
    name="documentation37",
    ends={
        Property(name="vcml_Documentation39", type=vcml_NumericCharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_NumericCharacteristicValue38", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies40: BinaryAssociation = BinaryAssociation(
    name="dependencies40",
    ends={
        Property(name="vcml_CharacteristicOrValueDependencies42", type=vcml_NumericCharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_NumericCharacteristicValue41", type=vcml_CharacteristicOrValueDependencies, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation43: BinaryAssociation = BinaryAssociation(
    name="documentation43",
    ends={
        Property(name="vcml_Documentation45", type=vcml_DateCharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_DateCharacteristicValue44", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies46: BinaryAssociation = BinaryAssociation(
    name="dependencies46",
    ends={
        Property(name="vcml_CharacteristicOrValueDependencies48", type=vcml_DateCharacteristicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_DateCharacteristicValue47", type=vcml_CharacteristicOrValueDependencies, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies49: BinaryAssociation = BinaryAssociation(
    name="dependencies49",
    ends={
        Property(name="vcml_Dependency", type=vcml_CharacteristicOrValueDependencies, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicOrValueDependencies50", type=vcml_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
characteristics51: BinaryAssociation = BinaryAssociation(
    name="characteristics51",
    ends={
        Property(name="vcml_Characteristic53", type=vcml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Class52", type=vcml_Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)
values23: BinaryAssociation = BinaryAssociation(
    name="values23",
    ends={
        Property(name="vcml_NumericCharacteristicValue", type=vcml_NumericType, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_NumericType", type=vcml_NumericCharacteristicValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencyNets58: BinaryAssociation = BinaryAssociation(
    name="dependencyNets58",
    ends={
        Property(name="vcml_DependencyNet", type=vcml_ConfigurationProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConfigurationProfile59", type=vcml_DependencyNet, multiplicity=Multiplicity(0, 9999))
    }
)
entries60: BinaryAssociation = BinaryAssociation(
    name="entries60",
    ends={
        Property(name="vcml_ConfigurationProfileEntry62", type=vcml_ConfigurationProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConfigurationProfile61", type=vcml_ConfigurationProfileEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
material63: BinaryAssociation = BinaryAssociation(
    name="material63",
    ends={
        Property(name="Material64", type=vcml_ConfigurationProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="configurationprofiles", type=vcml_Material, multiplicity=Multiplicity(0, 1))
    }
)
documentation65: BinaryAssociation = BinaryAssociation(
    name="documentation65",
    ends={
        Property(name="vcml_Documentation66", type=vcml_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Procedure", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source67: BinaryAssociation = BinaryAssociation(
    name="source67",
    ends={
        Property(name="vcml_ProcedureSource", type=vcml_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Procedure68", type=vcml_ProcedureSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation69: BinaryAssociation = BinaryAssociation(
    name="documentation69",
    ends={
        Property(name="vcml_Documentation71", type=vcml_SelectionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SelectionCondition70", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source72: BinaryAssociation = BinaryAssociation(
    name="source72",
    ends={
        Property(name="vcml_ConditionSource", type=vcml_SelectionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SelectionCondition73", type=vcml_ConditionSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation74: BinaryAssociation = BinaryAssociation(
    name="documentation74",
    ends={
        Property(name="vcml_Documentation75", type=vcml_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Precondition", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source76: BinaryAssociation = BinaryAssociation(
    name="source76",
    ends={
        Property(name="vcml_ConditionSource78", type=vcml_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Precondition77", type=vcml_ConditionSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition79: BinaryAssociation = BinaryAssociation(
    name="condition79",
    ends={
        Property(name="vcml_Condition", type=vcml_ConditionSource, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConditionSource80", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation81: BinaryAssociation = BinaryAssociation(
    name="documentation81",
    ends={
        Property(name="vcml_Documentation83", type=vcml_DependencyNet, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_DependencyNet82", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superClasses55: BinaryAssociation = BinaryAssociation(
    name="superClasses55",
    ends={
        Property(name="vcml_Class56", type=vcml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Class54", type=vcml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
uidesign57: BinaryAssociation = BinaryAssociation(
    name="uidesign57",
    ends={
        Property(name="vcml_InterfaceDesign", type=vcml_ConfigurationProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConfigurationProfile", type=vcml_InterfaceDesign, multiplicity=Multiplicity(0, 1))
    }
)
documentation86: BinaryAssociation = BinaryAssociation(
    name="documentation86",
    ends={
        Property(name="vcml_Documentation88", type=vcml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Constraint87", type=vcml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source89: BinaryAssociation = BinaryAssociation(
    name="source89",
    ends={
        Property(name="vcml_ConstraintSource", type=vcml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Constraint90", type=vcml_ConstraintSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependency91: BinaryAssociation = BinaryAssociation(
    name="dependency91",
    ends={
        Property(name="vcml_Procedure93", type=vcml_ConfigurationProfileEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConfigurationProfileEntry92", type=vcml_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
characteristicGroups94: BinaryAssociation = BinaryAssociation(
    name="characteristicGroups94",
    ends={
        Property(name="vcml_CharacteristicGroup", type=vcml_InterfaceDesign, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_InterfaceDesign95", type=vcml_CharacteristicGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description96: BinaryAssociation = BinaryAssociation(
    name="description96",
    ends={
        Property(name="vcml_Description98", type=vcml_CharacteristicGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicGroup97", type=vcml_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristics99: BinaryAssociation = BinaryAssociation(
    name="characteristics99",
    ends={
        Property(name="vcml_Characteristic101", type=vcml_CharacteristicGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicGroup100", type=vcml_Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)
billofmaterials102: BinaryAssociation = BinaryAssociation(
    name="billofmaterials102",
    ends={
        Property(name="BillOfMaterial", type=vcml_Material, multiplicity=Multiplicity(1, 1)),
        Property(name="material", type=vcml_BillOfMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
classifications103: BinaryAssociation = BinaryAssociation(
    name="classifications103",
    ends={
        Property(name="vcml_Classification", type=vcml_Material, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Material104", type=vcml_Classification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueAssignments110: BinaryAssociation = BinaryAssociation(
    name="valueAssignments110",
    ends={
        Property(name="vcml_ValueAssignment", type=vcml_Classification, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Classification111", type=vcml_ValueAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints84: BinaryAssociation = BinaryAssociation(
    name="constraints84",
    ends={
        Property(name="vcml_Constraint", type=vcml_DependencyNet, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_DependencyNet85", type=vcml_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
characteristic112: BinaryAssociation = BinaryAssociation(
    name="characteristic112",
    ends={
        Property(name="vcml_Characteristic114", type=vcml_ValueAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ValueAssignment113", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
values115: BinaryAssociation = BinaryAssociation(
    name="values115",
    ends={
        Property(name="vcml_Literal", type=vcml_ValueAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ValueAssignment116", type=vcml_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments117: BinaryAssociation = BinaryAssociation(
    name="arguments117",
    ends={
        Property(name="vcml_VariantFunctionArgument", type=vcml_VariantFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VariantFunction", type=vcml_VariantFunctionArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characteristic118: BinaryAssociation = BinaryAssociation(
    name="characteristic118",
    ends={
        Property(name="vcml_Characteristic120", type=vcml_VariantFunctionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VariantFunctionArgument119", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
arguments121: BinaryAssociation = BinaryAssociation(
    name="arguments121",
    ends={
        Property(name="vcml_VariantTableArgument", type=vcml_VariantTable, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VariantTable", type=vcml_VariantTableArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurationprofiles105: BinaryAssociation = BinaryAssociation(
    name="configurationprofiles105",
    ends={
        Property(name="ConfigurationProfile", type=vcml_Material, multiplicity=Multiplicity(1, 1)),
        Property(name="material106", type=vcml_ConfigurationProfile, multiplicity=Multiplicity(0, 9999))
    }
)
cls107: BinaryAssociation = BinaryAssociation(
    name="cls107",
    ends={
        Property(name="vcml_Class109", type=vcml_Classification, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Classification108", type=vcml_Class, multiplicity=Multiplicity(0, 1))
    }
)
characteristic122: BinaryAssociation = BinaryAssociation(
    name="characteristic122",
    ends={
        Property(name="vcml_Characteristic124", type=vcml_VariantTableArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VariantTableArgument123", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
table125: BinaryAssociation = BinaryAssociation(
    name="table125",
    ends={
        Property(name="vcml_VariantTable126", type=vcml_VariantTableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VariantTableContent", type=vcml_VariantTable, multiplicity=Multiplicity(0, 1))
    }
)
rows127: BinaryAssociation = BinaryAssociation(
    name="rows127",
    ends={
        Property(name="vcml_Row", type=vcml_VariantTableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_VariantTableContent128", type=vcml_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values129: BinaryAssociation = BinaryAssociation(
    name="values129",
    ends={
        Property(name="vcml_Literal131", type=vcml_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Row130", type=vcml_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions132: BinaryAssociation = BinaryAssociation(
    name="descriptions132",
    ends={
        Property(name="vcml_MultiLanguageDescription", type=vcml_MultiLanguageDescriptions, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_MultiLanguageDescriptions", type=vcml_MultiLanguageDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition138: BinaryAssociation = BinaryAssociation(
    name="condition138",
    ends={
        Property(name="vcml_Condition140", type=vcml_ConstraintSource, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintSource139", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restrictions141: BinaryAssociation = BinaryAssociation(
    name="restrictions141",
    ends={
        Property(name="vcml_ConstraintRestriction", type=vcml_ConstraintSource, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintSource142", type=vcml_ConstraintRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inferences143: BinaryAssociation = BinaryAssociation(
    name="inferences143",
    ends={
        Property(name="vcml_CharacteristicReference_C", type=vcml_ConstraintSource, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintSource144", type=vcml_CharacteristicReference_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shortVars145: BinaryAssociation = BinaryAssociation(
    name="shortVars145",
    ends={
        Property(name="vcml_ShortVarDefinition", type=vcml_ConstraintObject, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintObject146", type=vcml_ShortVarDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
languageblocks133: BinaryAssociation = BinaryAssociation(
    name="languageblocks133",
    ends={
        Property(name="vcml_MultipleLanguageDocumentation_LanguageBlock", type=vcml_MultipleLanguageDocumentation, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_MultipleLanguageDocumentation", type=vcml_MultipleLanguageDocumentation_LanguageBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formattedDocumentationBlocks134: BinaryAssociation = BinaryAssociation(
    name="formattedDocumentationBlocks134",
    ends={
        Property(name="vcml_FormattedDocumentationBlock", type=vcml_MultipleLanguageDocumentation_LanguageBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_MultipleLanguageDocumentation_LanguageBlock135", type=vcml_FormattedDocumentationBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects136: BinaryAssociation = BinaryAssociation(
    name="objects136",
    ends={
        Property(name="vcml_ConstraintObject", type=vcml_ConstraintSource, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintSource137", type=vcml_ConstraintObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
material152: BinaryAssociation = BinaryAssociation(
    name="material152",
    ends={
        Property(name="vcml_Material154", type=vcml_PartialKey, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_PartialKey153", type=vcml_Material, multiplicity=Multiplicity(0, 1))
    }
)
characteristic155: BinaryAssociation = BinaryAssociation(
    name="characteristic155",
    ends={
        Property(name="vcml_Characteristic157", type=vcml_ShortVarDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ShortVarDefinition156", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
child158: BinaryAssociation = BinaryAssociation(
    name="child158",
    ends={
        Property(name="vcml_ConstraintObject159", type=vcml_PartOfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_PartOfCondition", type=vcml_ConstraintObject, multiplicity=Multiplicity(0, 1))
    }
)
class147: BinaryAssociation = BinaryAssociation(
    name="class147",
    ends={
        Property(name="vcml_Class148", type=vcml_ConstraintClass, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintClass", type=vcml_Class, multiplicity=Multiplicity(0, 1))
    }
)
objectType149: BinaryAssociation = BinaryAssociation(
    name="objectType149",
    ends={
        Property(name="vcml_ObjectType", type=vcml_ConstraintMaterial, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConstraintMaterial", type=vcml_ObjectType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attrs150: BinaryAssociation = BinaryAssociation(
    name="attrs150",
    ends={
        Property(name="vcml_PartialKey", type=vcml_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ObjectType151", type=vcml_PartialKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location169: BinaryAssociation = BinaryAssociation(
    name="location169",
    ends={
        Property(name="vcml_ConstraintObject170", type=vcml_ObjectCharacteristicReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ObjectCharacteristicReference", type=vcml_ConstraintObject, multiplicity=Multiplicity(0, 1))
    }
)
characteristic171: BinaryAssociation = BinaryAssociation(
    name="characteristic171",
    ends={
        Property(name="vcml_Characteristic173", type=vcml_ObjectCharacteristicReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ObjectCharacteristicReference172", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
ref174: BinaryAssociation = BinaryAssociation(
    name="ref174",
    ends={
        Property(name="vcml_ShortVarDefinition175", type=vcml_ShortVarReference, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ShortVarReference", type=vcml_ShortVarDefinition, multiplicity=Multiplicity(0, 1))
    }
)
parent160: BinaryAssociation = BinaryAssociation(
    name="parent160",
    ends={
        Property(name="vcml_ConstraintObject162", type=vcml_PartOfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_PartOfCondition161", type=vcml_ConstraintObject, multiplicity=Multiplicity(0, 1))
    }
)
child163: BinaryAssociation = BinaryAssociation(
    name="child163",
    ends={
        Property(name="vcml_ConstraintObject164", type=vcml_SubpartOfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SubpartOfCondition", type=vcml_ConstraintObject, multiplicity=Multiplicity(0, 1))
    }
)
parent165: BinaryAssociation = BinaryAssociation(
    name="parent165",
    ends={
        Property(name="vcml_ConstraintObject167", type=vcml_SubpartOfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SubpartOfCondition166", type=vcml_ConstraintObject, multiplicity=Multiplicity(0, 1))
    }
)
restriction168: BinaryAssociation = BinaryAssociation(
    name="restriction168",
    ends={
        Property(name="vcml_EObject", type=vcml_NegatedConstraintRestrictionLHS, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_NegatedConstraintRestrictionLHS", type=vcml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function183: BinaryAssociation = BinaryAssociation(
    name="function183",
    ends={
        Property(name="vcml_VariantFunction184", type=vcml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Function", type=vcml_VariantFunction, multiplicity=Multiplicity(0, 1))
    }
)
characteristics185: BinaryAssociation = BinaryAssociation(
    name="characteristics185",
    ends={
        Property(name="vcml_Characteristic187", type=vcml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Function186", type=vcml_Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)
statements176: BinaryAssociation = BinaryAssociation(
    name="statements176",
    ends={
        Property(name="vcml_Statement", type=vcml_ProcedureSource, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ProcedureSource177", type=vcml_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements178: BinaryAssociation = BinaryAssociation(
    name="statements178",
    ends={
        Property(name="vcml_SimpleStatement", type=vcml_CompoundStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CompoundStatement", type=vcml_SimpleStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characteristic179: BinaryAssociation = BinaryAssociation(
    name="characteristic179",
    ends={
        Property(name="vcml_Characteristic180", type=vcml_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Assignment", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="vcml_Expression", type=vcml_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Assignment182", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table199: BinaryAssociation = BinaryAssociation(
    name="table199",
    ends={
        Property(name="vcml_VariantTable200", type=vcml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Table", type=vcml_VariantTable, multiplicity=Multiplicity(0, 1))
    }
)
characteristics201: BinaryAssociation = BinaryAssociation(
    name="characteristics201",
    ends={
        Property(name="vcml_Characteristic203", type=vcml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Table202", type=vcml_Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)
values204: BinaryAssociation = BinaryAssociation(
    name="values204",
    ends={
        Property(name="vcml_Literal206", type=vcml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Table205", type=vcml_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values188: BinaryAssociation = BinaryAssociation(
    name="values188",
    ends={
        Property(name="vcml_Literal190", type=vcml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Function189", type=vcml_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function191: BinaryAssociation = BinaryAssociation(
    name="function191",
    ends={
        Property(name="vcml_VariantFunction192", type=vcml_PFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_PFunction", type=vcml_VariantFunction, multiplicity=Multiplicity(0, 1))
    }
)
characteristics193: BinaryAssociation = BinaryAssociation(
    name="characteristics193",
    ends={
        Property(name="vcml_Characteristic195", type=vcml_PFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_PFunction194", type=vcml_Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)
values196: BinaryAssociation = BinaryAssociation(
    name="values196",
    ends={
        Property(name="vcml_Literal198", type=vcml_PFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_PFunction197", type=vcml_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characteristic214: BinaryAssociation = BinaryAssociation(
    name="characteristic214",
    ends={
        Property(name="vcml_Characteristic215", type=vcml_SetPricingFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SetPricingFactor", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
arg1216: BinaryAssociation = BinaryAssociation(
    name="arg1216",
    ends={
        Property(name="vcml_Expression218", type=vcml_SetPricingFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SetPricingFactor217", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg2219: BinaryAssociation = BinaryAssociation(
    name="arg2219",
    ends={
        Property(name="vcml_Expression221", type=vcml_SetPricingFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SetPricingFactor220", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristic222: BinaryAssociation = BinaryAssociation(
    name="characteristic222",
    ends={
        Property(name="vcml_Characteristic223", type=vcml_CharacteristicReference_P, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_CharacteristicReference_P", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
characteristic207: BinaryAssociation = BinaryAssociation(
    name="characteristic207",
    ends={
        Property(name="vcml_Characteristic208", type=vcml_SetOrDelDefault, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SetOrDelDefault", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
expression209: BinaryAssociation = BinaryAssociation(
    name="expression209",
    ends={
        Property(name="vcml_Expression211", type=vcml_SetOrDelDefault, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SetOrDelDefault210", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristic212: BinaryAssociation = BinaryAssociation(
    name="characteristic212",
    ends={
        Property(name="vcml_Characteristic213", type=vcml_IsInvisible, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_IsInvisible", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
characteristic228: BinaryAssociation = BinaryAssociation(
    name="characteristic228",
    ends={
        Property(name="vcml_Characteristic229", type=vcml_SumParts, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SumParts", type=vcml_Characteristic, multiplicity=Multiplicity(0, 1))
    }
)
characteristic230: BinaryAssociation = BinaryAssociation(
    name="characteristic230",
    ends={
        Property(name="vcml_CharacteristicReference_C231", type=vcml_MDataCharacteristic_C, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_MDataCharacteristic_C", type=vcml_CharacteristicReference_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression224: BinaryAssociation = BinaryAssociation(
    name="expression224",
    ends={
        Property(name="vcml_Expression225", type=vcml_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_UnaryExpression", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument226: BinaryAssociation = BinaryAssociation(
    name="argument226",
    ends={
        Property(name="vcml_Expression227", type=vcml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_FunctionCall", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left236: BinaryAssociation = BinaryAssociation(
    name="left236",
    ends={
        Property(name="vcml_Expression237", type=vcml_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Comparison", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right238: BinaryAssociation = BinaryAssociation(
    name="right238",
    ends={
        Property(name="vcml_Expression240", type=vcml_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_Comparison239", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristic232: BinaryAssociation = BinaryAssociation(
    name="characteristic232",
    ends={
        Property(name="vcml_CharacteristicReference_P233", type=vcml_MDataCharacteristic_P, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_MDataCharacteristic_P", type=vcml_CharacteristicReference_P, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition234: BinaryAssociation = BinaryAssociation(
    name="condition234",
    ends={
        Property(name="vcml_Condition235", type=vcml_UnaryCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_UnaryCondition", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list249: BinaryAssociation = BinaryAssociation(
    name="list249",
    ends={
        Property(name="vcml_List", type=vcml_InCondition_C, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_InCondition_C250", type=vcml_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristic251: BinaryAssociation = BinaryAssociation(
    name="characteristic251",
    ends={
        Property(name="vcml_CharacteristicReference_P252", type=vcml_InCondition_P, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_InCondition_P", type=vcml_CharacteristicReference_P, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list253: BinaryAssociation = BinaryAssociation(
    name="list253",
    ends={
        Property(name="vcml_List255", type=vcml_InCondition_P, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_InCondition_P254", type=vcml_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristic241: BinaryAssociation = BinaryAssociation(
    name="characteristic241",
    ends={
        Property(name="vcml_CharacteristicReference_C242", type=vcml_IsSpecified_C, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_IsSpecified_C", type=vcml_CharacteristicReference_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries256: BinaryAssociation = BinaryAssociation(
    name="entries256",
    ends={
        Property(name="vcml_NumberListEntry257", type=vcml_NumberList, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_NumberList", type=vcml_NumberListEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characteristic243: BinaryAssociation = BinaryAssociation(
    name="characteristic243",
    ends={
        Property(name="vcml_CharacteristicReference_P244", type=vcml_IsSpecified_P, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_IsSpecified_P", type=vcml_CharacteristicReference_P, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variantclass245: BinaryAssociation = BinaryAssociation(
    name="variantclass245",
    ends={
        Property(name="vcml_ObjectType246", type=vcml_TypeOf, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_TypeOf", type=vcml_ObjectType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characteristic247: BinaryAssociation = BinaryAssociation(
    name="characteristic247",
    ends={
        Property(name="vcml_CharacteristicReference_C248", type=vcml_InCondition_C, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_InCondition_C", type=vcml_CharacteristicReference_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries258: BinaryAssociation = BinaryAssociation(
    name="entries258",
    ends={
        Property(name="vcml_SymbolicLiteral", type=vcml_SymbolList, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_SymbolList", type=vcml_SymbolicLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restriction259: BinaryAssociation = BinaryAssociation(
    name="restriction259",
    ends={
        Property(name="vcml_ConstraintRestriction260", type=vcml_ConditionalConstraintRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConditionalConstraintRestriction", type=vcml_ConstraintRestriction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition261: BinaryAssociation = BinaryAssociation(
    name="condition261",
    ends={
        Property(name="vcml_Condition263", type=vcml_ConditionalConstraintRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConditionalConstraintRestriction262", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement264: BinaryAssociation = BinaryAssociation(
    name="statement264",
    ends={
        Property(name="vcml_Statement265", type=vcml_ConditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConditionalStatement", type=vcml_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition266: BinaryAssociation = BinaryAssociation(
    name="condition266",
    ends={
        Property(name="vcml_Condition268", type=vcml_ConditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_ConditionalStatement267", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right276: BinaryAssociation = BinaryAssociation(
    name="right276",
    ends={
        Property(name="vcml_Condition278", type=vcml_BinaryCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BinaryCondition277", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left269: BinaryAssociation = BinaryAssociation(
    name="left269",
    ends={
        Property(name="vcml_Expression270", type=vcml_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BinaryExpression", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right271: BinaryAssociation = BinaryAssociation(
    name="right271",
    ends={
        Property(name="vcml_Expression273", type=vcml_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BinaryExpression272", type=vcml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left274: BinaryAssociation = BinaryAssociation(
    name="left274",
    ends={
        Property(name="vcml_Condition275", type=vcml_BinaryCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="vcml_BinaryCondition", type=vcml_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_vcml_BOMItem_Material_BOMItem = Generalization(general=BOMItem, specific=vcml_BOMItem_Material)
gen_vcml_BOMItem_Class_BOMItem = Generalization(general=BOMItem, specific=vcml_BOMItem_Class)
gen_vcml_Characteristic_VCObject = Generalization(general=VCObject, specific=vcml_Characteristic)
gen_vcml_NumericType_CharacteristicType = Generalization(general=CharacteristicType, specific=vcml_NumericType)
gen_vcml_BillOfMaterial_VCObject = Generalization(general=VCObject, specific=vcml_BillOfMaterial)
gen_vcml_DateType_CharacteristicType = Generalization(general=CharacteristicType, specific=vcml_DateType)
gen_vcml_Class_VCObject = Generalization(general=VCObject, specific=vcml_Class)
gen_vcml_SymbolicType_CharacteristicType = Generalization(general=CharacteristicType, specific=vcml_SymbolicType)
gen_vcml_Procedure_VCObject = Generalization(general=VCObject, specific=vcml_Procedure)
gen_vcml_Procedure_Dependency = Generalization(general=Dependency, specific=vcml_Procedure)
gen_vcml_SelectionCondition_VCObject = Generalization(general=VCObject, specific=vcml_SelectionCondition)
gen_vcml_SelectionCondition_Dependency = Generalization(general=Dependency, specific=vcml_SelectionCondition)
gen_vcml_Precondition_VCObject = Generalization(general=VCObject, specific=vcml_Precondition)
gen_vcml_Precondition_Dependency = Generalization(general=Dependency, specific=vcml_Precondition)
gen_vcml_DependencyNet_VCObject = Generalization(general=VCObject, specific=vcml_DependencyNet)
gen_vcml_ConfigurationProfile_VCObject = Generalization(general=VCObject, specific=vcml_ConfigurationProfile)
gen_vcml_Constraint_VCObject = Generalization(general=VCObject, specific=vcml_Constraint)
gen_vcml_Constraint_Dependency = Generalization(general=Dependency, specific=vcml_Constraint)
gen_vcml_InterfaceDesign_VCObject = Generalization(general=VCObject, specific=vcml_InterfaceDesign)
gen_vcml_Material_VCObject = Generalization(general=VCObject, specific=vcml_Material)
gen_vcml_VariantFunction_VCObject = Generalization(general=VCObject, specific=vcml_VariantFunction)
gen_vcml_VariantTable_VCObject = Generalization(general=VCObject, specific=vcml_VariantTable)
gen_vcml_SimpleDescription_Description = Generalization(general=Description, specific=vcml_SimpleDescription)
gen_vcml_VariantTableContent_VCObject = Generalization(general=VCObject, specific=vcml_VariantTableContent)
gen_vcml_MultiLanguageDescriptions_Description = Generalization(general=Description, specific=vcml_MultiLanguageDescriptions)
gen_vcml_SimpleDocumentation_Documentation = Generalization(general=Documentation, specific=vcml_SimpleDocumentation)
gen_vcml_MultipleLanguageDocumentation_Documentation = Generalization(general=Documentation, specific=vcml_MultipleLanguageDocumentation)
gen_vcml_PartOfCondition_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_PartOfCondition)
gen_vcml_PartOfCondition_Condition = Generalization(general=Condition, specific=vcml_PartOfCondition)
gen_vcml_ConstraintClass_ConstraintObject = Generalization(general=ConstraintObject, specific=vcml_ConstraintClass)
gen_vcml_ConstraintMaterial_ConstraintObject = Generalization(general=ConstraintObject, specific=vcml_ConstraintMaterial)
gen_vcml_CharacteristicReference_C_Literal = Generalization(general=Literal, specific=vcml_CharacteristicReference_C)
gen_vcml_ObjectCharacteristicReference_CharacteristicReference_C = Generalization(general=CharacteristicReference_C, specific=vcml_ObjectCharacteristicReference)
gen_vcml_ShortVarReference_CharacteristicReference_C = Generalization(general=CharacteristicReference_C, specific=vcml_ShortVarReference)
gen_vcml_SubpartOfCondition_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_SubpartOfCondition)
gen_vcml_SubpartOfCondition_Condition = Generalization(general=Condition, specific=vcml_SubpartOfCondition)
gen_vcml_ConstraintRestrictionFalse_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_ConstraintRestrictionFalse)
gen_vcml_NegatedConstraintRestrictionLHS_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_NegatedConstraintRestrictionLHS)
gen_vcml_Function_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_Function)
gen_vcml_Function_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_Function)
gen_vcml_Function_FunctionOrTable = Generalization(general=FunctionOrTable, specific=vcml_Function)
gen_vcml_Function_Condition = Generalization(general=Condition, specific=vcml_Function)
gen_vcml_CompoundStatement_Statement = Generalization(general=Statement, specific=vcml_CompoundStatement)
gen_vcml_SimpleStatement_Statement = Generalization(general=Statement, specific=vcml_SimpleStatement)
gen_vcml_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_Assignment)
gen_vcml_Table_FunctionOrTable = Generalization(general=FunctionOrTable, specific=vcml_Table)
gen_vcml_Table_Condition = Generalization(general=Condition, specific=vcml_Table)
gen_vcml_SetOrDelDefault_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_SetOrDelDefault)
gen_vcml_PFunction_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_PFunction)
gen_vcml_PFunction_FunctionOrTable = Generalization(general=FunctionOrTable, specific=vcml_PFunction)
gen_vcml_PFunction_Condition = Generalization(general=Condition, specific=vcml_PFunction)
gen_vcml_Table_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_Table)
gen_vcml_Table_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_Table)
gen_vcml_CharacteristicReference_P_Literal = Generalization(general=Literal, specific=vcml_CharacteristicReference_P)
gen_vcml_SetDefault_SetOrDelDefault = Generalization(general=SetOrDelDefault, specific=vcml_SetDefault)
gen_vcml_DelDefault_SetOrDelDefault = Generalization(general=SetOrDelDefault, specific=vcml_DelDefault)
gen_vcml_IsInvisible_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_IsInvisible)
gen_vcml_SetPricingFactor_SimpleStatement = Generalization(general=SimpleStatement, specific=vcml_SetPricingFactor)
gen_vcml_CountParts_Expression = Generalization(general=Expression, specific=vcml_CountParts)
gen_vcml_MDataCharacteristic_C_Literal = Generalization(general=Literal, specific=vcml_MDataCharacteristic_C)
gen_vcml_MDataCharacteristic_P_Literal = Generalization(general=Literal, specific=vcml_MDataCharacteristic_P)
gen_vcml_UnaryExpression_Expression = Generalization(general=Expression, specific=vcml_UnaryExpression)
gen_vcml_Literal_Expression = Generalization(general=Expression, specific=vcml_Literal)
gen_vcml_FunctionCall_Expression = Generalization(general=Expression, specific=vcml_FunctionCall)
gen_vcml_SumParts_Expression = Generalization(general=Expression, specific=vcml_SumParts)
gen_vcml_Comparison_Condition = Generalization(general=Condition, specific=vcml_Comparison)
gen_vcml_IsSpecified_C_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_IsSpecified_C)
gen_vcml_IsSpecified_C_Condition = Generalization(general=Condition, specific=vcml_IsSpecified_C)
gen_vcml_NumericLiteral_Literal = Generalization(general=Literal, specific=vcml_NumericLiteral)
gen_vcml_NumericLiteral_NumberListEntry = Generalization(general=NumberListEntry, specific=vcml_NumericLiteral)
gen_vcml_SymbolicLiteral_Literal = Generalization(general=Literal, specific=vcml_SymbolicLiteral)
gen_vcml_UnaryCondition_Condition = Generalization(general=Condition, specific=vcml_UnaryCondition)
gen_vcml_Comparison_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_Comparison)
gen_vcml_InCondition_P_Condition = Generalization(general=Condition, specific=vcml_InCondition_P)
gen_vcml_NumberList_List = Generalization(general=List, specific=vcml_NumberList)
gen_vcml_IsSpecified_P_Condition = Generalization(general=Condition, specific=vcml_IsSpecified_P)
gen_vcml_TypeOf_Condition = Generalization(general=Condition, specific=vcml_TypeOf)
gen_vcml_InCondition_C_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_InCondition_C)
gen_vcml_InCondition_C_Condition = Generalization(general=Condition, specific=vcml_InCondition_C)
gen_vcml_NumericInterval_NumberListEntry = Generalization(general=NumberListEntry, specific=vcml_NumericInterval)
gen_vcml_SymbolList_List = Generalization(general=List, specific=vcml_SymbolList)
gen_vcml_ConditionalConstraintRestriction_ConstraintRestriction = Generalization(general=ConstraintRestriction, specific=vcml_ConditionalConstraintRestriction)
gen_vcml_ConditionalStatement_Statement = Generalization(general=Statement, specific=vcml_ConditionalStatement)
gen_vcml_BinaryExpression_Expression = Generalization(general=Expression, specific=vcml_BinaryExpression)
gen_vcml_BinaryCondition_Condition = Generalization(general=Condition, specific=vcml_BinaryCondition)

# Domain Model
domain_model = DomainModel(
    name="vcml",
    types={vcml_VcmlModel, vcml_Import, vcml_Option, vcml_VCObject, vcml_BOMItem, vcml_Material, vcml_SelectionCondition, vcml_ConfigurationProfileEntry, vcml_BOMItem_Material, BOMItem, vcml_BOMItem_Class, vcml_Class, vcml_Characteristic, vcml_Documentation, vcml_CharacteristicType, vcml_CharacteristicOrValueDependencies, vcml_NumericType, CharacteristicType, vcml_Description, vcml_BillOfMaterial, VCObject, vcml_CharacteristicValue, vcml_DateType, vcml_DateCharacteristicValue, vcml_NumberListEntry, vcml_Dependency, vcml_NumericCharacteristicValue, vcml_SymbolicType, vcml_DependencyNet, vcml_Procedure, Dependency, vcml_ProcedureSource, vcml_ConditionSource, vcml_Precondition, vcml_Condition, vcml_ConfigurationProfile, vcml_Constraint, vcml_InterfaceDesign, vcml_ConstraintSource, vcml_CharacteristicGroup, vcml_Classification, vcml_Literal, vcml_VariantFunction, vcml_VariantFunctionArgument, vcml_VariantTable, vcml_VariantTableArgument, vcml_ValueAssignment, vcml_SimpleDescription, Description, vcml_VariantTableContent, vcml_Row, vcml_MultiLanguageDescriptions, vcml_MultiLanguageDescription, vcml_SimpleDocumentation, Documentation, vcml_ConstraintRestriction, vcml_CharacteristicReference_C, vcml_ShortVarDefinition, vcml_MultipleLanguageDocumentation, vcml_MultipleLanguageDocumentation_LanguageBlock, vcml_FormattedDocumentationBlock, vcml_ConstraintObject, vcml_PartOfCondition, ConstraintRestriction, Condition, vcml_ConstraintClass, ConstraintObject, vcml_ConstraintMaterial, vcml_ObjectType, vcml_PartialKey, Literal, vcml_ObjectCharacteristicReference, CharacteristicReference_C, vcml_ShortVarReference, vcml_SubpartOfCondition, vcml_ConstraintRestrictionFalse, vcml_NegatedConstraintRestrictionLHS, vcml_EObject, vcml_FunctionOrTable, vcml_Function, FunctionOrTable, vcml_Statement, vcml_CompoundStatement, Statement, vcml_SimpleStatement, vcml_Assignment, SimpleStatement, vcml_Expression, vcml_SetOrDelDefault, vcml_PFunction, vcml_Table, vcml_CharacteristicReference_P, vcml_SetDefault, SetOrDelDefault, vcml_DelDefault, vcml_IsInvisible, vcml_SetPricingFactor, vcml_CountParts, vcml_MDataCharacteristic_C, vcml_MDataCharacteristic_P, vcml_UnaryExpression, Expression, vcml_FunctionCall, vcml_SumParts, vcml_IsSpecified_C, vcml_NumericLiteral, NumberListEntry, vcml_SymbolicLiteral, vcml_UnaryCondition, vcml_Comparison, vcml_InCondition_P, vcml_NumberList, List, vcml_IsSpecified_P, vcml_TypeOf, vcml_InCondition_C, vcml_List, vcml_NumericInterval, vcml_SymbolList, vcml_ConditionalConstraintRestriction, vcml_ConditionalStatement, vcml_BinaryExpression, vcml_BinaryCondition, OptionType, Status, Language, UnaryExpressionOperator, ComparisonOperator, FunctionName, ProcedureLocation, Fixing},
    associations={imports0, options1, objects3, items10, material11, selectionCondition12, entries14, material16, cls17, documentation18, type19, dependencies21, description5, options7, values24, values25, description26, documentation29, dependencies32, entry35, documentation37, dependencies40, documentation43, dependencies46, dependencies49, characteristics51, values23, dependencyNets58, entries60, material63, documentation65, source67, documentation69, source72, documentation74, source76, condition79, documentation81, superClasses55, uidesign57, documentation86, source89, dependency91, characteristicGroups94, description96, characteristics99, billofmaterials102, classifications103, valueAssignments110, constraints84, characteristic112, values115, arguments117, characteristic118, arguments121, configurationprofiles105, cls107, characteristic122, table125, rows127, values129, descriptions132, condition138, restrictions141, inferences143, shortVars145, languageblocks133, formattedDocumentationBlocks134, objects136, material152, characteristic155, child158, class147, objectType149, attrs150, location169, characteristic171, ref174, parent160, child163, parent165, restriction168, function183, characteristics185, statements176, statements178, characteristic179, expression181, table199, characteristics201, values204, values188, function191, characteristics193, values196, characteristic214, arg1216, arg2219, characteristic222, characteristic207, expression209, characteristic212, characteristic228, characteristic230, expression224, argument226, left236, right238, characteristic232, condition234, list249, characteristic251, list253, characteristic241, entries256, characteristic243, variantclass245, characteristic247, entries258, restriction259, condition261, statement264, condition266, right276, left269, right271, left274},
    generalizations={gen_vcml_BOMItem_Material_BOMItem, gen_vcml_BOMItem_Class_BOMItem, gen_vcml_Characteristic_VCObject, gen_vcml_NumericType_CharacteristicType, gen_vcml_BillOfMaterial_VCObject, gen_vcml_DateType_CharacteristicType, gen_vcml_Class_VCObject, gen_vcml_SymbolicType_CharacteristicType, gen_vcml_Procedure_VCObject, gen_vcml_Procedure_Dependency, gen_vcml_SelectionCondition_VCObject, gen_vcml_SelectionCondition_Dependency, gen_vcml_Precondition_VCObject, gen_vcml_Precondition_Dependency, gen_vcml_DependencyNet_VCObject, gen_vcml_ConfigurationProfile_VCObject, gen_vcml_Constraint_VCObject, gen_vcml_Constraint_Dependency, gen_vcml_InterfaceDesign_VCObject, gen_vcml_Material_VCObject, gen_vcml_VariantFunction_VCObject, gen_vcml_VariantTable_VCObject, gen_vcml_SimpleDescription_Description, gen_vcml_VariantTableContent_VCObject, gen_vcml_MultiLanguageDescriptions_Description, gen_vcml_SimpleDocumentation_Documentation, gen_vcml_MultipleLanguageDocumentation_Documentation, gen_vcml_PartOfCondition_ConstraintRestriction, gen_vcml_PartOfCondition_Condition, gen_vcml_ConstraintClass_ConstraintObject, gen_vcml_ConstraintMaterial_ConstraintObject, gen_vcml_CharacteristicReference_C_Literal, gen_vcml_ObjectCharacteristicReference_CharacteristicReference_C, gen_vcml_ShortVarReference_CharacteristicReference_C, gen_vcml_SubpartOfCondition_ConstraintRestriction, gen_vcml_SubpartOfCondition_Condition, gen_vcml_ConstraintRestrictionFalse_ConstraintRestriction, gen_vcml_NegatedConstraintRestrictionLHS_ConstraintRestriction, gen_vcml_Function_ConstraintRestriction, gen_vcml_Function_SimpleStatement, gen_vcml_Function_FunctionOrTable, gen_vcml_Function_Condition, gen_vcml_CompoundStatement_Statement, gen_vcml_SimpleStatement_Statement, gen_vcml_Assignment_SimpleStatement, gen_vcml_Table_FunctionOrTable, gen_vcml_Table_Condition, gen_vcml_SetOrDelDefault_SimpleStatement, gen_vcml_PFunction_SimpleStatement, gen_vcml_PFunction_FunctionOrTable, gen_vcml_PFunction_Condition, gen_vcml_Table_ConstraintRestriction, gen_vcml_Table_SimpleStatement, gen_vcml_CharacteristicReference_P_Literal, gen_vcml_SetDefault_SetOrDelDefault, gen_vcml_DelDefault_SetOrDelDefault, gen_vcml_IsInvisible_SimpleStatement, gen_vcml_SetPricingFactor_SimpleStatement, gen_vcml_CountParts_Expression, gen_vcml_MDataCharacteristic_C_Literal, gen_vcml_MDataCharacteristic_P_Literal, gen_vcml_UnaryExpression_Expression, gen_vcml_Literal_Expression, gen_vcml_FunctionCall_Expression, gen_vcml_SumParts_Expression, gen_vcml_Comparison_Condition, gen_vcml_IsSpecified_C_ConstraintRestriction, gen_vcml_IsSpecified_C_Condition, gen_vcml_NumericLiteral_Literal, gen_vcml_NumericLiteral_NumberListEntry, gen_vcml_SymbolicLiteral_Literal, gen_vcml_UnaryCondition_Condition, gen_vcml_Comparison_ConstraintRestriction, gen_vcml_InCondition_P_Condition, gen_vcml_NumberList_List, gen_vcml_IsSpecified_P_Condition, gen_vcml_TypeOf_Condition, gen_vcml_InCondition_C_ConstraintRestriction, gen_vcml_InCondition_C_Condition, gen_vcml_NumericInterval_NumberListEntry, gen_vcml_SymbolList_List, gen_vcml_ConditionalConstraintRestriction_ConstraintRestriction, gen_vcml_ConditionalStatement_Statement, gen_vcml_BinaryExpression_Expression, gen_vcml_BinaryCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)