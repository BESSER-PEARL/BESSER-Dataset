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
express_Schema = Class(name="express::Schema")
express_Type = Class(name="express::Type")
express_Entity = Class(name="express::Entity")
express_Function = Class(name="express::Function")
express_Rule = Class(name="express::Rule")
express_ExpressConcept = Class(name="express::ExpressConcept")
express_WhereRule = Class(name="express::WhereRule")
ExpressConcept = Class(name="ExpressConcept")
express_DataType = Class(name="express::DataType")
express_Attribute = Class(name="express::Attribute")
express_UniqueRule = Class(name="express::UniqueRule")
express_Reference = Class(name="express::Reference")
express_TypeNameList = Class(name="express::TypeNameList")
express_ConstantVal = Class(name="express::ConstantVal")
express_LocalVar = Class(name="express::LocalVar")
express_Statement = Class(name="express::Statement")
express_Line = Class(name="express::Line")
express_FunctionExpression = Class(name="express::FunctionExpression")
express_ParameterList = Class(name="express::ParameterList")
express_GenericType = Class(name="express::GenericType")
express_CollectionType = Class(name="express::CollectionType")
express_FormalParam = Class(name="express::FormalParam")
express_Intervall = Class(name="express::Intervall")
express_BuiltInType = Class(name="express::BuiltInType")
DataType = Class(name="DataType")
express_ReferenceType = Class(name="express::ReferenceType")
express_RealType = Class(name="express::RealType")
express_NumberType = Class(name="express::NumberType")
express_IntegerType = Class(name="express::IntegerType")
express_StringType = Class(name="express::StringType")
BuiltInType = Class(name="BuiltInType")
express_BinaryType = Class(name="express::BinaryType")
express_LogicalType = Class(name="express::LogicalType")
express_BooleanType = Class(name="express::BooleanType")
express_EnumType = Class(name="express::EnumType")
express_LiteralType = Class(name="express::LiteralType")
express_SelectType = Class(name="express::SelectType")
express_SequenceStatement = Class(name="express::SequenceStatement")
Statement = Class(name="Statement")
express_CaseStatement = Class(name="express::CaseStatement")
express_CaseAction = Class(name="express::CaseAction")
express_IndexTerminal = Class(name="express::IndexTerminal")
Index = Class(name="Index")
express_ReturnStatement = Class(name="express::ReturnStatement")
express_EscapeStatement = Class(name="express::EscapeStatement")
express_Assignment = Class(name="express::Assignment")
express_VarOrAttrib = Class(name="express::VarOrAttrib")
express_SimpleVar = Class(name="express::SimpleVar")
VarOrAttrib = Class(name="VarOrAttrib")
express_IndexedVar = Class(name="express::IndexedVar")
express_Index = Class(name="express::Index")
express_AttributeVar = Class(name="express::AttributeVar")
express_IfStatement = Class(name="express::IfStatement")
express_RepeatStatement = Class(name="express::RepeatStatement")
express_VarLiteral = Class(name="express::VarLiteral")
IndexTerminal = Class(name="IndexTerminal")
express_IntLiteral = Class(name="express::IntLiteral")

# express_Schema class attributes and methods
express_Schema_name: Property = Property(name="name", type=StringType)
express_Schema.attributes={express_Schema_name}

# express_Type class attributes and methods

# express_Entity class attributes and methods
express_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
express_Entity.attributes={express_Entity_abstract}

# express_Function class attributes and methods
express_Function_name: Property = Property(name="name", type=StringType)
express_Function.attributes={express_Function_name}

# express_Rule class attributes and methods
express_Rule_name: Property = Property(name="name", type=StringType)
express_Rule.attributes={express_Rule_name}

# express_ExpressConcept class attributes and methods
express_ExpressConcept_name: Property = Property(name="name", type=StringType)
express_ExpressConcept.attributes={express_ExpressConcept_name}

# express_WhereRule class attributes and methods
express_WhereRule_name: Property = Property(name="name", type=StringType)
express_WhereRule_expression: Property = Property(name="expression", type=StringType)
express_WhereRule.attributes={express_WhereRule_expression, express_WhereRule_name}

# ExpressConcept class attributes and methods

# express_DataType class attributes and methods

# express_Attribute class attributes and methods
express_Attribute_self: Property = Property(name="self", type=BooleanType)
express_Attribute_qualifier: Property = Property(name="qualifier", type=StringType)
express_Attribute_name: Property = Property(name="name", type=StringType)
express_Attribute_optional: Property = Property(name="optional", type=BooleanType)
express_Attribute_expression: Property = Property(name="expression", type=StringType)
express_Attribute.attributes={express_Attribute_optional, express_Attribute_self, express_Attribute_expression, express_Attribute_qualifier, express_Attribute_name}

# express_UniqueRule class attributes and methods
express_UniqueRule_name: Property = Property(name="name", type=StringType)
express_UniqueRule_attribute: Property = Property(name="attribute", type=StringType)
express_UniqueRule.attributes={express_UniqueRule_attribute, express_UniqueRule_name}

# express_Reference class attributes and methods
express_Reference_qualifier: Property = Property(name="qualifier", type=StringType)
express_Reference_name: Property = Property(name="name", type=StringType)
express_Reference_optional: Property = Property(name="optional", type=BooleanType)
express_Reference_self: Property = Property(name="self", type=BooleanType)
express_Reference.attributes={express_Reference_qualifier, express_Reference_name, express_Reference_self, express_Reference_optional}

# express_TypeNameList class attributes and methods
express_TypeNameList_type: Property = Property(name="type", type=StringType)
express_TypeNameList.attributes={express_TypeNameList_type}

# express_ConstantVal class attributes and methods
express_ConstantVal_name: Property = Property(name="name", type=StringType)
express_ConstantVal.attributes={express_ConstantVal_name}

# express_LocalVar class attributes and methods
express_LocalVar_varname: Property = Property(name="varname", type=StringType)
express_LocalVar.attributes={express_LocalVar_varname}

# express_Statement class attributes and methods

# express_Line class attributes and methods
express_Line_text: Property = Property(name="text", type=StringType)
express_Line.attributes={express_Line_text}

# express_FunctionExpression class attributes and methods
express_FunctionExpression_name: Property = Property(name="name", type=StringType)
express_FunctionExpression.attributes={express_FunctionExpression_name}

# express_ParameterList class attributes and methods

# express_GenericType class attributes and methods
express_GenericType_typelabel: Property = Property(name="typelabel", type=StringType)
express_GenericType.attributes={express_GenericType_typelabel}

# express_CollectionType class attributes and methods
express_CollectionType_name: Property = Property(name="name", type=StringType)
express_CollectionType_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
express_CollectionType_upperBound: Property = Property(name="upperBound", type=IntegerType)
express_CollectionType_many: Property = Property(name="many", type=BooleanType)
express_CollectionType_opt: Property = Property(name="opt", type=BooleanType)
express_CollectionType_unique: Property = Property(name="unique", type=BooleanType)
express_CollectionType.attributes={express_CollectionType_lowerBound, express_CollectionType_upperBound, express_CollectionType_many, express_CollectionType_unique, express_CollectionType_name, express_CollectionType_opt}

# express_FormalParam class attributes and methods
express_FormalParam_paramName: Property = Property(name="paramName", type=StringType)
express_FormalParam.attributes={express_FormalParam_paramName}

# express_Intervall class attributes and methods
express_Intervall_expression: Property = Property(name="expression", type=StringType)
express_Intervall.attributes={express_Intervall_expression}

# express_BuiltInType class attributes and methods

# DataType class attributes and methods

# express_ReferenceType class attributes and methods

# express_RealType class attributes and methods

# express_NumberType class attributes and methods

# express_IntegerType class attributes and methods

# express_StringType class attributes and methods
express_StringType_size: Property = Property(name="size", type=IntegerType)
express_StringType_fixed: Property = Property(name="fixed", type=BooleanType)
express_StringType.attributes={express_StringType_size, express_StringType_fixed}

# BuiltInType class attributes and methods

# express_BinaryType class attributes and methods
express_BinaryType_size: Property = Property(name="size", type=IntegerType)
express_BinaryType.attributes={express_BinaryType_size}

# express_LogicalType class attributes and methods

# express_BooleanType class attributes and methods

# express_EnumType class attributes and methods

# express_LiteralType class attributes and methods
express_LiteralType_name: Property = Property(name="name", type=StringType)
express_LiteralType.attributes={express_LiteralType_name}

# express_SelectType class attributes and methods

# express_SequenceStatement class attributes and methods
express_SequenceStatement_expression: Property = Property(name="expression", type=StringType)
express_SequenceStatement.attributes={express_SequenceStatement_expression}

# Statement class attributes and methods

# express_CaseStatement class attributes and methods
express_CaseStatement_variable: Property = Property(name="variable", type=StringType)
express_CaseStatement.attributes={express_CaseStatement_variable}

# express_CaseAction class attributes and methods
express_CaseAction_value: Property = Property(name="value", type=StringType)
express_CaseAction.attributes={express_CaseAction_value}

# express_IndexTerminal class attributes and methods

# Index class attributes and methods

# express_ReturnStatement class attributes and methods
express_ReturnStatement_expression: Property = Property(name="expression", type=StringType)
express_ReturnStatement.attributes={express_ReturnStatement_expression}

# express_EscapeStatement class attributes and methods

# express_Assignment class attributes and methods
express_Assignment_expression: Property = Property(name="expression", type=StringType)
express_Assignment.attributes={express_Assignment_expression}

# express_VarOrAttrib class attributes and methods

# express_SimpleVar class attributes and methods
express_SimpleVar_name: Property = Property(name="name", type=StringType)
express_SimpleVar.attributes={express_SimpleVar_name}

# VarOrAttrib class attributes and methods

# express_IndexedVar class attributes and methods

# express_Index class attributes and methods

# express_AttributeVar class attributes and methods

# express_IfStatement class attributes and methods

# express_RepeatStatement class attributes and methods
express_RepeatStatement_idx: Property = Property(name="idx", type=StringType)
express_RepeatStatement_start: Property = Property(name="start", type=StringType)
express_RepeatStatement_end: Property = Property(name="end", type=StringType)
express_RepeatStatement.attributes={express_RepeatStatement_idx, express_RepeatStatement_end, express_RepeatStatement_start}

# express_VarLiteral class attributes and methods
express_VarLiteral_value: Property = Property(name="value", type=StringType)
express_VarLiteral.attributes={express_VarLiteral_value}

# IndexTerminal class attributes and methods

# express_IntLiteral class attributes and methods
express_IntLiteral_value: Property = Property(name="value", type=IntegerType)
express_IntLiteral.attributes={express_IntLiteral_value}

# Relationships
disjointSubtype11: BinaryAssociation = BinaryAssociation(
    name="disjointSubtype11",
    ends={
        Property(name="express_Entity12", type=express_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Entity10", type=express_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="express_Type", type=express_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Schema", type=express_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity1: BinaryAssociation = BinaryAssociation(
    name="entity1",
    ends={
        Property(name="express_Entity", type=express_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Schema2", type=express_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function3: BinaryAssociation = BinaryAssociation(
    name="function3",
    ends={
        Property(name="express_Function", type=express_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Schema4", type=express_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule5: BinaryAssociation = BinaryAssociation(
    name="rule5",
    ends={
        Property(name="express_Rule", type=express_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Schema6", type=express_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereRule7: BinaryAssociation = BinaryAssociation(
    name="whereRule7",
    ends={
        Property(name="express_WhereRule", type=express_ExpressConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="express_ExpressConcept", type=express_WhereRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype8: BinaryAssociation = BinaryAssociation(
    name="datatype8",
    ends={
        Property(name="express_DataType", type=express_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Type9", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtype14: BinaryAssociation = BinaryAssociation(
    name="subtype14",
    ends={
        Property(name="express_Entity15", type=express_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Entity13", type=express_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
supertype17: BinaryAssociation = BinaryAssociation(
    name="supertype17",
    ends={
        Property(name="express_Entity18", type=express_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Entity16", type=express_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
attribute19: BinaryAssociation = BinaryAssociation(
    name="attribute19",
    ends={
        Property(name="express_Attribute", type=express_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Entity20", type=express_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uniqueRule21: BinaryAssociation = BinaryAssociation(
    name="uniqueRule21",
    ends={
        Property(name="express_UniqueRule", type=express_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Entity22", type=express_UniqueRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="express_DataType25", type=express_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Attribute24", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite27: BinaryAssociation = BinaryAssociation(
    name="opposite27",
    ends={
        Property(name="express_Attribute28", type=express_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Attribute26", type=express_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="express_DataType49", type=express_LocalVar, multiplicity=Multiplicity(1, 1)),
        Property(name="express_LocalVar48", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="express_Entity30", type=express_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Reference", type=express_Entity, multiplicity=Multiplicity(0, 1))
    }
)
target31: BinaryAssociation = BinaryAssociation(
    name="target31",
    ends={
        Property(name="express_TypeNameList", type=express_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Rule32", type=express_TypeNameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant33: BinaryAssociation = BinaryAssociation(
    name="constant33",
    ends={
        Property(name="express_ConstantVal", type=express_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Rule34", type=express_ConstantVal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVar35: BinaryAssociation = BinaryAssociation(
    name="localVar35",
    ends={
        Property(name="express_LocalVar", type=express_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Rule36", type=express_LocalVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement37: BinaryAssociation = BinaryAssociation(
    name="statement37",
    ends={
        Property(name="express_Statement", type=express_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Rule38", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereRule39: BinaryAssociation = BinaryAssociation(
    name="whereRule39",
    ends={
        Property(name="express_WhereRule41", type=express_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Rule40", type=express_WhereRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="express_DataType44", type=express_ConstantVal, multiplicity=Multiplicity(1, 1)),
        Property(name="express_ConstantVal43", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression45: BinaryAssociation = BinaryAssociation(
    name="expression45",
    ends={
        Property(name="express_Line", type=express_ConstantVal, multiplicity=Multiplicity(1, 1)),
        Property(name="express_ConstantVal46", type=express_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVar72: BinaryAssociation = BinaryAssociation(
    name="localVar72",
    ends={
        Property(name="express_LocalVar74", type=express_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Function73", type=express_LocalVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement75: BinaryAssociation = BinaryAssociation(
    name="statement75",
    ends={
        Property(name="express_Statement77", type=express_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Function76", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression50: BinaryAssociation = BinaryAssociation(
    name="expression50",
    ends={
        Property(name="express_Line52", type=express_LocalVar, multiplicity=Multiplicity(1, 1)),
        Property(name="express_LocalVar51", type=express_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument53: BinaryAssociation = BinaryAssociation(
    name="argument53",
    ends={
        Property(name="express_ParameterList", type=express_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_FunctionExpression", type=express_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return54: BinaryAssociation = BinaryAssociation(
    name="return54",
    ends={
        Property(name="express_DataType56", type=express_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_FunctionExpression55", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
local57: BinaryAssociation = BinaryAssociation(
    name="local57",
    ends={
        Property(name="express_LocalVar59", type=express_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_FunctionExpression58", type=express_LocalVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement60: BinaryAssociation = BinaryAssociation(
    name="statement60",
    ends={
        Property(name="express_Statement62", type=express_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_FunctionExpression61", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params63: BinaryAssociation = BinaryAssociation(
    name="params63",
    ends={
        Property(name="express_ParameterList65", type=express_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Function64", type=express_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType66: BinaryAssociation = BinaryAssociation(
    name="returnType66",
    ends={
        Property(name="express_DataType68", type=express_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Function67", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant69: BinaryAssociation = BinaryAssociation(
    name="constant69",
    ends={
        Property(name="express_ConstantVal71", type=express_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Function70", type=express_ConstantVal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParam78: BinaryAssociation = BinaryAssociation(
    name="formalParam78",
    ends={
        Property(name="express_FormalParam", type=express_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="express_ParameterList79", type=express_FormalParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="express_DataType82", type=express_FormalParam, multiplicity=Multiplicity(1, 1)),
        Property(name="express_FormalParam81", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interval83: BinaryAssociation = BinaryAssociation(
    name="interval83",
    ends={
        Property(name="express_Intervall", type=express_WhereRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_WhereRule84", type=express_Intervall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance85: BinaryAssociation = BinaryAssociation(
    name="instance85",
    ends={
        Property(name="express_ExpressConcept86", type=express_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_ReferenceType", type=express_ExpressConcept, multiplicity=Multiplicity(0, 1))
    }
)
lowerRef87: BinaryAssociation = BinaryAssociation(
    name="lowerRef87",
    ends={
        Property(name="express_Attribute88", type=express_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_CollectionType", type=express_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
upperRef89: BinaryAssociation = BinaryAssociation(
    name="upperRef89",
    ends={
        Property(name="express_Attribute91", type=express_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_CollectionType90", type=express_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
type92: BinaryAssociation = BinaryAssociation(
    name="type92",
    ends={
        Property(name="express_DataType94", type=express_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_CollectionType93", type=express_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherwise99: BinaryAssociation = BinaryAssociation(
    name="otherwise99",
    ends={
        Property(name="express_CaseStatement100", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="express_Statement101", type=express_CaseStatement, multiplicity=Multiplicity(1, 1))
    }
)
literal95: BinaryAssociation = BinaryAssociation(
    name="literal95",
    ends={
        Property(name="express_LiteralType", type=express_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_EnumType", type=express_LiteralType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
select96: BinaryAssociation = BinaryAssociation(
    name="select96",
    ends={
        Property(name="express_ExpressConcept97", type=express_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_SelectType", type=express_ExpressConcept, multiplicity=Multiplicity(0, 9999))
    }
)
slot98: BinaryAssociation = BinaryAssociation(
    name="slot98",
    ends={
        Property(name="express_CaseAction", type=express_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_CaseStatement", type=express_CaseAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component109: BinaryAssociation = BinaryAssociation(
    name="component109",
    ends={
        Property(name="express_VarOrAttrib110", type=express_AttributeVar, multiplicity=Multiplicity(1, 1)),
        Property(name="express_AttributeVar", type=express_VarOrAttrib, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement102: BinaryAssociation = BinaryAssociation(
    name="statement102",
    ends={
        Property(name="express_Statement104", type=express_CaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="express_CaseAction103", type=express_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignTo105: BinaryAssociation = BinaryAssociation(
    name="assignTo105",
    ends={
        Property(name="express_VarOrAttrib", type=express_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="express_Assignment", type=express_VarOrAttrib, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable106: BinaryAssociation = BinaryAssociation(
    name="variable106",
    ends={
        Property(name="express_SimpleVar", type=express_IndexedVar, multiplicity=Multiplicity(1, 1)),
        Property(name="express_IndexedVar", type=express_SimpleVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index107: BinaryAssociation = BinaryAssociation(
    name="index107",
    ends={
        Property(name="express_Index", type=express_IndexedVar, multiplicity=Multiplicity(1, 1)),
        Property(name="express_IndexedVar108", type=express_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition111: BinaryAssociation = BinaryAssociation(
    name="condition111",
    ends={
        Property(name="express_Line112", type=express_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_IfStatement", type=express_Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement113: BinaryAssociation = BinaryAssociation(
    name="statement113",
    ends={
        Property(name="express_Statement115", type=express_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_IfStatement114", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement116: BinaryAssociation = BinaryAssociation(
    name="elseStatement116",
    ends={
        Property(name="express_Statement118", type=express_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_IfStatement117", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement119: BinaryAssociation = BinaryAssociation(
    name="statement119",
    ends={
        Property(name="express_Statement120", type=express_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_RepeatStatement", type=express_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_express_Type_ExpressConcept = Generalization(general=ExpressConcept, specific=express_Type)
gen_express_Entity_ExpressConcept = Generalization(general=ExpressConcept, specific=express_Entity)
gen_express_GenericType_DataType = Generalization(general=DataType, specific=express_GenericType)
gen_express_CollectionType_DataType = Generalization(general=DataType, specific=express_CollectionType)
gen_express_BuiltInType_DataType = Generalization(general=DataType, specific=express_BuiltInType)
gen_express_ReferenceType_DataType = Generalization(general=DataType, specific=express_ReferenceType)
gen_express_RealType_BuiltInType = Generalization(general=BuiltInType, specific=express_RealType)
gen_express_NumberType_BuiltInType = Generalization(general=BuiltInType, specific=express_NumberType)
gen_express_IntegerType_BuiltInType = Generalization(general=BuiltInType, specific=express_IntegerType)
gen_express_StringType_BuiltInType = Generalization(general=BuiltInType, specific=express_StringType)
gen_express_BinaryType_BuiltInType = Generalization(general=BuiltInType, specific=express_BinaryType)
gen_express_LogicalType_BuiltInType = Generalization(general=BuiltInType, specific=express_LogicalType)
gen_express_BooleanType_BuiltInType = Generalization(general=BuiltInType, specific=express_BooleanType)
gen_express_EnumType_DataType = Generalization(general=DataType, specific=express_EnumType)
gen_express_SelectType_DataType = Generalization(general=DataType, specific=express_SelectType)
gen_express_SequenceStatement_Statement = Generalization(general=Statement, specific=express_SequenceStatement)
gen_express_CaseStatement_Statement = Generalization(general=Statement, specific=express_CaseStatement)
gen_express_IndexTerminal_Index = Generalization(general=Index, specific=express_IndexTerminal)
gen_express_ReturnStatement_Statement = Generalization(general=Statement, specific=express_ReturnStatement)
gen_express_EscapeStatement_Statement = Generalization(general=Statement, specific=express_EscapeStatement)
gen_express_Assignment_Statement = Generalization(general=Statement, specific=express_Assignment)
gen_express_SimpleVar_VarOrAttrib = Generalization(general=VarOrAttrib, specific=express_SimpleVar)
gen_express_IndexedVar_VarOrAttrib = Generalization(general=VarOrAttrib, specific=express_IndexedVar)
gen_express_AttributeVar_VarOrAttrib = Generalization(general=VarOrAttrib, specific=express_AttributeVar)
gen_express_IfStatement_Statement = Generalization(general=Statement, specific=express_IfStatement)
gen_express_RepeatStatement_Statement = Generalization(general=Statement, specific=express_RepeatStatement)
gen_express_VarLiteral_IndexTerminal = Generalization(general=IndexTerminal, specific=express_VarLiteral)
gen_express_IntLiteral_IndexTerminal = Generalization(general=IndexTerminal, specific=express_IntLiteral)

# Domain Model
domain_model = DomainModel(
    name="express",
    types={express_Schema, express_Type, express_Entity, express_Function, express_Rule, express_ExpressConcept, express_WhereRule, ExpressConcept, express_DataType, express_Attribute, express_UniqueRule, express_Reference, express_TypeNameList, express_ConstantVal, express_LocalVar, express_Statement, express_Line, express_FunctionExpression, express_ParameterList, express_GenericType, express_CollectionType, express_FormalParam, express_Intervall, express_BuiltInType, DataType, express_ReferenceType, express_RealType, express_NumberType, express_IntegerType, express_StringType, BuiltInType, express_BinaryType, express_LogicalType, express_BooleanType, express_EnumType, express_LiteralType, express_SelectType, express_SequenceStatement, Statement, express_CaseStatement, express_CaseAction, express_IndexTerminal, Index, express_ReturnStatement, express_EscapeStatement, express_Assignment, express_VarOrAttrib, express_SimpleVar, VarOrAttrib, express_IndexedVar, express_Index, express_AttributeVar, express_IfStatement, express_RepeatStatement, express_VarLiteral, IndexTerminal, express_IntLiteral},
    associations={disjointSubtype11, type0, entity1, function3, rule5, whereRule7, datatype8, subtype14, supertype17, attribute19, uniqueRule21, type23, opposite27, type47, type29, target31, constant33, localVar35, statement37, whereRule39, type42, expression45, localVar72, statement75, expression50, argument53, return54, local57, statement60, params63, returnType66, constant69, formalParam78, type80, interval83, instance85, lowerRef87, upperRef89, type92, otherwise99, literal95, select96, slot98, component109, statement102, assignTo105, variable106, index107, condition111, statement113, elseStatement116, statement119},
    generalizations={gen_express_Type_ExpressConcept, gen_express_Entity_ExpressConcept, gen_express_GenericType_DataType, gen_express_CollectionType_DataType, gen_express_BuiltInType_DataType, gen_express_ReferenceType_DataType, gen_express_RealType_BuiltInType, gen_express_NumberType_BuiltInType, gen_express_IntegerType_BuiltInType, gen_express_StringType_BuiltInType, gen_express_BinaryType_BuiltInType, gen_express_LogicalType_BuiltInType, gen_express_BooleanType_BuiltInType, gen_express_EnumType_DataType, gen_express_SelectType_DataType, gen_express_SequenceStatement_Statement, gen_express_CaseStatement_Statement, gen_express_IndexTerminal_Index, gen_express_ReturnStatement_Statement, gen_express_EscapeStatement_Statement, gen_express_Assignment_Statement, gen_express_SimpleVar_VarOrAttrib, gen_express_IndexedVar_VarOrAttrib, gen_express_AttributeVar_VarOrAttrib, gen_express_IfStatement_Statement, gen_express_RepeatStatement_Statement, gen_express_VarLiteral_IndexTerminal, gen_express_IntLiteral_IndexTerminal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)