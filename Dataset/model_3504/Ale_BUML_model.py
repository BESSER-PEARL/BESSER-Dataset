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
ale_Attribute = Class(name="ale::Attribute")
ale_Unit = Class(name="ale::Unit")
ale_Import = Class(name="ale::Import")
ale_Service = Class(name="ale::Service")
ale_BehavioredClass = Class(name="ale::BehavioredClass")
ale_rOpposite = Class(name="ale::rOpposite")
ale_Operation = Class(name="ale::Operation")
ale_ExtendedClass = Class(name="ale::ExtendedClass")
BehavioredClass = Class(name="BehavioredClass")
ale_RuntimeClass = Class(name="ale::RuntimeClass")
ale_Tag = Class(name="ale::Tag")
ale_rType = Class(name="ale::rType")
ale_Variable = Class(name="ale::Variable")
ale_Block = Class(name="ale::Block")
ale_Remove = Class(name="ale::Remove")
ale_ExpressionStmt = Class(name="ale::ExpressionStmt")
ale_Statement = Class(name="ale::Statement")
ale_VarDecl = Class(name="ale::VarDecl")
Statement = Class(name="Statement")
ale_Assign = Class(name="ale::Assign")
ale_Expression = Class(name="ale::Expression")
ale_Insert = Class(name="ale::Insert")
ale_While = Class(name="ale::While")
ale_ForEach = Class(name="ale::ForEach")
ale_Collection = Class(name="ale::Collection")
ale_If = Class(name="ale::If")
ale_EObject = Class(name="ale::EObject")
ale_binding = Class(name="ale::binding")
ale_rSwitch = Class(name="ale::rSwitch")
ale_rCase = Class(name="ale::rCase")
ale_Mult = Class(name="ale::Mult")
ale_Add = Class(name="ale::Add")
ale_typeLiteral = Class(name="ale::typeLiteral")
ale_literal = Class(name="ale::literal")
literal = Class(name="literal")
rType = Class(name="rType")
ale_classifierTypeRule = Class(name="ale::classifierTypeRule")
typeLiteral = Class(name="typeLiteral")
ale_Call = Class(name="ale::Call")
Expression = Class(name="Expression")
ale_Feature = Class(name="ale::Feature")
ale_Apply = Class(name="ale::Apply")
ale_Implie = Class(name="ale::Implie")
ale_Not = Class(name="ale::Not")
ale_Min = Class(name="ale::Min")
ale_Comp = Class(name="ale::Comp")
ale_And = Class(name="ale::And")
ale_Or = Class(name="ale::Or")
ale_Xor = Class(name="ale::Xor")
ale_False = Class(name="ale::False")
ale_Null = Class(name="ale::Null")
ale_Sequence = Class(name="ale::Sequence")
ale_OrderedSet = Class(name="ale::OrderedSet")
ale_Enum = Class(name="ale::Enum")
ale_VarRef = Class(name="ale::VarRef")
ale_Lit = Class(name="ale::Lit")
ale_Conditional = Class(name="ale::Conditional")
ale_Let = Class(name="ale::Let")
ale_String = Class(name="ale::String")
ale_Int = Class(name="ale::Int")
ale_Real = Class(name="ale::Real")
ale_True = Class(name="ale::True")
ale_StringType = Class(name="ale::StringType")
ale_IntType = Class(name="ale::IntType")
ale_RealType = Class(name="ale::RealType")
ale_BoolType = Class(name="ale::BoolType")
ale_SeqType = Class(name="ale::SeqType")
ale_SetType = Class(name="ale::SetType")
ale_ClassifierSetType = Class(name="ale::ClassifierSetType")
ale_ClassifierType = Class(name="ale::ClassifierType")
classifierTypeRule = Class(name="classifierTypeRule")

# ale_Attribute class attributes and methods
ale_Attribute_modifier: Property = Property(name="modifier", type=StringType)
ale_Attribute_bounds: Property = Property(name="bounds", type=StringType)
ale_Attribute_name: Property = Property(name="name", type=StringType)
ale_Attribute.attributes={ale_Attribute_bounds, ale_Attribute_modifier, ale_Attribute_name}

# ale_Unit class attributes and methods
ale_Unit_name: Property = Property(name="name", type=StringType)
ale_Unit.attributes={ale_Unit_name}

# ale_Import class attributes and methods
ale_Import_name: Property = Property(name="name", type=StringType)
ale_Import_alias: Property = Property(name="alias", type=StringType)
ale_Import.attributes={ale_Import_name, ale_Import_alias}

# ale_Service class attributes and methods
ale_Service_name: Property = Property(name="name", type=StringType)
ale_Service.attributes={ale_Service_name}

# ale_BehavioredClass class attributes and methods
ale_BehavioredClass_name: Property = Property(name="name", type=StringType)
ale_BehavioredClass.attributes={ale_BehavioredClass_name}

# ale_rOpposite class attributes and methods
ale_rOpposite_name: Property = Property(name="name", type=StringType)
ale_rOpposite.attributes={ale_rOpposite_name}

# ale_Operation class attributes and methods
ale_Operation_name: Property = Property(name="name", type=StringType)
ale_Operation.attributes={ale_Operation_name}

# ale_ExtendedClass class attributes and methods
ale_ExtendedClass_extends: Property = Property(name="extends", type=StringType)
ale_ExtendedClass.attributes={ale_ExtendedClass_extends}

# BehavioredClass class attributes and methods

# ale_RuntimeClass class attributes and methods

# ale_Tag class attributes and methods
ale_Tag_name: Property = Property(name="name", type=StringType)
ale_Tag.attributes={ale_Tag_name}

# ale_rType class attributes and methods
ale_rType_name: Property = Property(name="name", type=StringType)
ale_rType.attributes={ale_rType_name}

# ale_Variable class attributes and methods
ale_Variable_name: Property = Property(name="name", type=StringType)
ale_Variable.attributes={ale_Variable_name}

# ale_Block class attributes and methods

# ale_Remove class attributes and methods

# ale_ExpressionStmt class attributes and methods

# ale_Statement class attributes and methods

# ale_VarDecl class attributes and methods
ale_VarDecl_name: Property = Property(name="name", type=StringType)
ale_VarDecl.attributes={ale_VarDecl_name}

# Statement class attributes and methods

# ale_Assign class attributes and methods

# ale_Expression class attributes and methods

# ale_Insert class attributes and methods

# ale_While class attributes and methods

# ale_ForEach class attributes and methods
ale_ForEach_iterator: Property = Property(name="iterator", type=StringType)
ale_ForEach.attributes={ale_ForEach_iterator}

# ale_Collection class attributes and methods
ale_Collection_min: Property = Property(name="min", type=IntegerType)
ale_Collection_max: Property = Property(name="max", type=IntegerType)
ale_Collection.attributes={ale_Collection_min, ale_Collection_max}

# ale_If class attributes and methods

# ale_EObject class attributes and methods

# ale_binding class attributes and methods
ale_binding_name: Property = Property(name="name", type=StringType)
ale_binding.attributes={ale_binding_name}

# ale_rSwitch class attributes and methods
ale_rSwitch_paramName: Property = Property(name="paramName", type=StringType)
ale_rSwitch.attributes={ale_rSwitch_paramName}

# ale_rCase class attributes and methods

# ale_Mult class attributes and methods
ale_Mult_op: Property = Property(name="op", type=StringType)
ale_Mult.attributes={ale_Mult_op}

# ale_Add class attributes and methods
ale_Add_op: Property = Property(name="op", type=StringType)
ale_Add.attributes={ale_Add_op}

# ale_typeLiteral class attributes and methods

# ale_literal class attributes and methods

# literal class attributes and methods

# rType class attributes and methods

# ale_classifierTypeRule class attributes and methods

# typeLiteral class attributes and methods

# ale_Call class attributes and methods
ale_Call_name: Property = Property(name="name", type=StringType)
ale_Call.attributes={ale_Call_name}

# Expression class attributes and methods

# ale_Feature class attributes and methods
ale_Feature_feature: Property = Property(name="feature", type=StringType)
ale_Feature.attributes={ale_Feature_feature}

# ale_Apply class attributes and methods
ale_Apply_name: Property = Property(name="name", type=StringType)
ale_Apply_varName: Property = Property(name="varName", type=StringType)
ale_Apply.attributes={ale_Apply_varName, ale_Apply_name}

# ale_Implie class attributes and methods

# ale_Not class attributes and methods

# ale_Min class attributes and methods

# ale_Comp class attributes and methods
ale_Comp_op: Property = Property(name="op", type=StringType)
ale_Comp.attributes={ale_Comp_op}

# ale_And class attributes and methods

# ale_Or class attributes and methods

# ale_Xor class attributes and methods

# ale_False class attributes and methods

# ale_Null class attributes and methods

# ale_Sequence class attributes and methods

# ale_OrderedSet class attributes and methods

# ale_Enum class attributes and methods

# ale_VarRef class attributes and methods
ale_VarRef_ID: Property = Property(name="ID", type=StringType)
ale_VarRef.attributes={ale_VarRef_ID}

# ale_Lit class attributes and methods

# ale_Conditional class attributes and methods

# ale_Let class attributes and methods

# ale_String class attributes and methods
ale_String_value: Property = Property(name="value", type=StringType)
ale_String.attributes={ale_String_value}

# ale_Int class attributes and methods
ale_Int_value: Property = Property(name="value", type=IntegerType)
ale_Int.attributes={ale_Int_value}

# ale_Real class attributes and methods
ale_Real_value: Property = Property(name="value", type=StringType)
ale_Real.attributes={ale_Real_value}

# ale_True class attributes and methods

# ale_StringType class attributes and methods

# ale_IntType class attributes and methods

# ale_RealType class attributes and methods

# ale_BoolType class attributes and methods

# ale_SeqType class attributes and methods

# ale_SetType class attributes and methods

# ale_ClassifierSetType class attributes and methods

# ale_ClassifierType class attributes and methods
ale_ClassifierType_className: Property = Property(name="className", type=StringType)
ale_ClassifierType_packageName: Property = Property(name="packageName", type=StringType)
ale_ClassifierType.attributes={ale_ClassifierType_className, ale_ClassifierType_packageName}

# classifierTypeRule class attributes and methods

# Relationships
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="ale_Attribute", type=ale_BehavioredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_BehavioredClass6", type=ale_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="ale_Import", type=ale_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Unit", type=ale_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services1: BinaryAssociation = BinaryAssociation(
    name="services1",
    ends={
        Property(name="ale_Service", type=ale_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Unit2", type=ale_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xtendedClasses3: BinaryAssociation = BinaryAssociation(
    name="xtendedClasses3",
    ends={
        Property(name="ale_BehavioredClass", type=ale_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Unit4", type=ale_BehavioredClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="ale_rType19", type=ale_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Variable18", type=ale_rType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite20: BinaryAssociation = BinaryAssociation(
    name="opposite20",
    ends={
        Property(name="ale_rOpposite", type=ale_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Attribute21", type=ale_rOpposite, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="ale_Operation", type=ale_BehavioredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_BehavioredClass8", type=ale_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag9: BinaryAssociation = BinaryAssociation(
    name="tag9",
    ends={
        Property(name="ale_Tag", type=ale_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Operation10", type=ale_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="ale_rType", type=ale_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Operation12", type=ale_rType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params13: BinaryAssociation = BinaryAssociation(
    name="params13",
    ends={
        Property(name="ale_Variable", type=ale_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Operation14", type=ale_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body15: BinaryAssociation = BinaryAssociation(
    name="body15",
    ends={
        Property(name="ale_Block", type=ale_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Operation16", type=ale_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target36: BinaryAssociation = BinaryAssociation(
    name="target36",
    ends={
        Property(name="ale_Expression37", type=ale_Insert, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Insert", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp38: BinaryAssociation = BinaryAssociation(
    name="exp38",
    ends={
        Property(name="ale_ExpressionStmt40", type=ale_Insert, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Insert39", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target41: BinaryAssociation = BinaryAssociation(
    name="target41",
    ends={
        Property(name="ale_Expression42", type=ale_Remove, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Remove", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp43: BinaryAssociation = BinaryAssociation(
    name="exp43",
    ends={
        Property(name="ale_ExpressionStmt45", type=ale_Remove, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Remove44", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="ale_rType24", type=ale_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Attribute23", type=ale_rType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp25: BinaryAssociation = BinaryAssociation(
    name="exp25",
    ends={
        Property(name="ale_ExpressionStmt", type=ale_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Attribute26", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="ale_rType28", type=ale_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_VarDecl", type=ale_rType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp29: BinaryAssociation = BinaryAssociation(
    name="exp29",
    ends={
        Property(name="ale_ExpressionStmt31", type=ale_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_VarDecl30", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target32: BinaryAssociation = BinaryAssociation(
    name="target32",
    ends={
        Property(name="ale_Expression", type=ale_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Assign", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp33: BinaryAssociation = BinaryAssociation(
    name="exp33",
    ends={
        Property(name="ale_ExpressionStmt35", type=ale_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Assign34", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else60: BinaryAssociation = BinaryAssociation(
    name="else60",
    ends={
        Property(name="ale_Block62", type=ale_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_If61", type=ale_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedIf64: BinaryAssociation = BinaryAssociation(
    name="nestedIf64",
    ends={
        Property(name="ale_If65", type=ale_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_If63", type=ale_If, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond66: BinaryAssociation = BinaryAssociation(
    name="cond66",
    ends={
        Property(name="ale_ExpressionStmt67", type=ale_While, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_While", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection46: BinaryAssociation = BinaryAssociation(
    name="collection46",
    ends={
        Property(name="ale_Collection", type=ale_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_ForEach", type=ale_Collection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block47: BinaryAssociation = BinaryAssociation(
    name="block47",
    ends={
        Property(name="ale_Block49", type=ale_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_ForEach48", type=ale_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp50: BinaryAssociation = BinaryAssociation(
    name="exp50",
    ends={
        Property(name="ale_ExpressionStmt52", type=ale_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Collection51", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements53: BinaryAssociation = BinaryAssociation(
    name="statements53",
    ends={
        Property(name="ale_Statement", type=ale_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Block54", type=ale_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond55: BinaryAssociation = BinaryAssociation(
    name="cond55",
    ends={
        Property(name="ale_ExpressionStmt56", type=ale_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_If", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then57: BinaryAssociation = BinaryAssociation(
    name="then57",
    ends={
        Property(name="ale_Block59", type=ale_If, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_If58", type=ale_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="ale_ExpressionStmt86", type=ale_rCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_rCase85", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp87: BinaryAssociation = BinaryAssociation(
    name="exp87",
    ends={
        Property(name="ale_EObject", type=ale_ExpressionStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_ExpressionStmt88", type=ale_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block68: BinaryAssociation = BinaryAssociation(
    name="block68",
    ends={
        Property(name="ale_Block70", type=ale_While, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_While69", type=ale_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramVal71: BinaryAssociation = BinaryAssociation(
    name="paramVal71",
    ends={
        Property(name="ale_ExpressionStmt72", type=ale_rSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_rSwitch", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases73: BinaryAssociation = BinaryAssociation(
    name="cases73",
    ends={
        Property(name="ale_rCase", type=ale_rSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_rSwitch74", type=ale_rCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
other75: BinaryAssociation = BinaryAssociation(
    name="other75",
    ends={
        Property(name="ale_ExpressionStmt77", type=ale_rSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_rSwitch76", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard78: BinaryAssociation = BinaryAssociation(
    name="guard78",
    ends={
        Property(name="ale_rType80", type=ale_rCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_rCase79", type=ale_rType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
match81: BinaryAssociation = BinaryAssociation(
    name="match81",
    ends={
        Property(name="ale_ExpressionStmt83", type=ale_rCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_rCase82", type=ale_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params108: BinaryAssociation = BinaryAssociation(
    name="params108",
    ends={
        Property(name="ale_Expression110", type=ale_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Apply109", type=ale_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="ale_Expression112", type=ale_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Mult", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right113: BinaryAssociation = BinaryAssociation(
    name="right113",
    ends={
        Property(name="ale_Expression115", type=ale_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Mult114", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type89: BinaryAssociation = BinaryAssociation(
    name="type89",
    ends={
        Property(name="ale_typeLiteral", type=ale_binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_binding", type=ale_typeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp90: BinaryAssociation = BinaryAssociation(
    name="exp90",
    ends={
        Property(name="ale_Expression92", type=ale_binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_binding91", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target93: BinaryAssociation = BinaryAssociation(
    name="target93",
    ends={
        Property(name="ale_Expression94", type=ale_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Call", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params95: BinaryAssociation = BinaryAssociation(
    name="params95",
    ends={
        Property(name="ale_Expression97", type=ale_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Call96", type=ale_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target98: BinaryAssociation = BinaryAssociation(
    name="target98",
    ends={
        Property(name="ale_Expression99", type=ale_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Feature", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target100: BinaryAssociation = BinaryAssociation(
    name="target100",
    ends={
        Property(name="ale_Expression101", type=ale_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Apply", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varType102: BinaryAssociation = BinaryAssociation(
    name="varType102",
    ends={
        Property(name="ale_typeLiteral104", type=ale_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Apply103", type=ale_typeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lambda105: BinaryAssociation = BinaryAssociation(
    name="lambda105",
    ends={
        Property(name="ale_Expression107", type=ale_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Apply106", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="ale_Expression142", type=ale_Implie, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Implie", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="ale_Expression145", type=ale_Implie, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Implie144", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp146: BinaryAssociation = BinaryAssociation(
    name="exp146",
    ends={
        Property(name="ale_Expression147", type=ale_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Not", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="ale_Expression117", type=ale_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Add", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="ale_Expression120", type=ale_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Add119", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="ale_Expression122", type=ale_Comp, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Comp", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="ale_Expression125", type=ale_Comp, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Comp124", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="ale_Expression127", type=ale_And, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_And", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="ale_Expression130", type=ale_And, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_And129", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="ale_Expression132", type=ale_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Or", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="ale_Expression135", type=ale_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Or134", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="ale_Expression137", type=ale_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Xor", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="ale_Expression140", type=ale_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Xor139", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params164: BinaryAssociation = BinaryAssociation(
    name="params164",
    ends={
        Property(name="ale_Expression165", type=ale_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Sequence", type=ale_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params166: BinaryAssociation = BinaryAssociation(
    name="params166",
    ends={
        Property(name="ale_Expression167", type=ale_OrderedSet, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_OrderedSet", type=ale_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp148: BinaryAssociation = BinaryAssociation(
    name="exp148",
    ends={
        Property(name="ale_Expression149", type=ale_Min, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Min", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal150: BinaryAssociation = BinaryAssociation(
    name="literal150",
    ends={
        Property(name="ale_literal", type=ale_Lit, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Lit", type=ale_literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond151: BinaryAssociation = BinaryAssociation(
    name="cond151",
    ends={
        Property(name="ale_Expression152", type=ale_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Conditional", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then153: BinaryAssociation = BinaryAssociation(
    name="then153",
    ends={
        Property(name="ale_Expression155", type=ale_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Conditional154", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else156: BinaryAssociation = BinaryAssociation(
    name="else156",
    ends={
        Property(name="ale_Expression158", type=ale_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Conditional157", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings159: BinaryAssociation = BinaryAssociation(
    name="bindings159",
    ends={
        Property(name="ale_binding160", type=ale_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Let", type=ale_binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp161: BinaryAssociation = BinaryAssociation(
    name="exp161",
    ends={
        Property(name="ale_Expression163", type=ale_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_Let162", type=ale_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type168: BinaryAssociation = BinaryAssociation(
    name="type168",
    ends={
        Property(name="ale_typeLiteral169", type=ale_SeqType, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_SeqType", type=ale_typeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type170: BinaryAssociation = BinaryAssociation(
    name="type170",
    ends={
        Property(name="ale_typeLiteral171", type=ale_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_SetType", type=ale_typeLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types172: BinaryAssociation = BinaryAssociation(
    name="types172",
    ends={
        Property(name="ale_classifierTypeRule", type=ale_ClassifierSetType, multiplicity=Multiplicity(1, 1)),
        Property(name="ale_ClassifierSetType", type=ale_classifierTypeRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ale_ExtendedClass_BehavioredClass = Generalization(general=BehavioredClass, specific=ale_ExtendedClass)
gen_ale_RuntimeClass_BehavioredClass = Generalization(general=BehavioredClass, specific=ale_RuntimeClass)
gen_ale_Remove_Statement = Generalization(general=Statement, specific=ale_Remove)
gen_ale_VarDecl_Statement = Generalization(general=Statement, specific=ale_VarDecl)
gen_ale_Assign_Statement = Generalization(general=Statement, specific=ale_Assign)
gen_ale_Insert_Statement = Generalization(general=Statement, specific=ale_Insert)
gen_ale_While_Statement = Generalization(general=Statement, specific=ale_While)
gen_ale_ForEach_Statement = Generalization(general=Statement, specific=ale_ForEach)
gen_ale_If_Statement = Generalization(general=Statement, specific=ale_If)
gen_ale_ExpressionStmt_Statement = Generalization(general=Statement, specific=ale_ExpressionStmt)
gen_ale_Mult_Expression = Generalization(general=Expression, specific=ale_Mult)
gen_ale_Add_Expression = Generalization(general=Expression, specific=ale_Add)
gen_ale_typeLiteral_literal = Generalization(general=literal, specific=ale_typeLiteral)
gen_ale_typeLiteral_rType = Generalization(general=rType, specific=ale_typeLiteral)
gen_ale_classifierTypeRule_typeLiteral = Generalization(general=typeLiteral, specific=ale_classifierTypeRule)
gen_ale_Call_Expression = Generalization(general=Expression, specific=ale_Call)
gen_ale_Feature_Expression = Generalization(general=Expression, specific=ale_Feature)
gen_ale_Apply_Expression = Generalization(general=Expression, specific=ale_Apply)
gen_ale_Implie_Expression = Generalization(general=Expression, specific=ale_Implie)
gen_ale_Not_Expression = Generalization(general=Expression, specific=ale_Not)
gen_ale_Min_Expression = Generalization(general=Expression, specific=ale_Min)
gen_ale_Comp_Expression = Generalization(general=Expression, specific=ale_Comp)
gen_ale_And_Expression = Generalization(general=Expression, specific=ale_And)
gen_ale_Or_Expression = Generalization(general=Expression, specific=ale_Or)
gen_ale_Xor_Expression = Generalization(general=Expression, specific=ale_Xor)
gen_ale_False_literal = Generalization(general=literal, specific=ale_False)
gen_ale_Null_literal = Generalization(general=literal, specific=ale_Null)
gen_ale_Sequence_literal = Generalization(general=literal, specific=ale_Sequence)
gen_ale_OrderedSet_literal = Generalization(general=literal, specific=ale_OrderedSet)
gen_ale_Enum_literal = Generalization(general=literal, specific=ale_Enum)
gen_ale_VarRef_Expression = Generalization(general=Expression, specific=ale_VarRef)
gen_ale_Lit_Expression = Generalization(general=Expression, specific=ale_Lit)
gen_ale_Conditional_Expression = Generalization(general=Expression, specific=ale_Conditional)
gen_ale_Let_Expression = Generalization(general=Expression, specific=ale_Let)
gen_ale_String_literal = Generalization(general=literal, specific=ale_String)
gen_ale_Int_literal = Generalization(general=literal, specific=ale_Int)
gen_ale_Real_literal = Generalization(general=literal, specific=ale_Real)
gen_ale_True_literal = Generalization(general=literal, specific=ale_True)
gen_ale_StringType_typeLiteral = Generalization(general=typeLiteral, specific=ale_StringType)
gen_ale_IntType_typeLiteral = Generalization(general=typeLiteral, specific=ale_IntType)
gen_ale_RealType_typeLiteral = Generalization(general=typeLiteral, specific=ale_RealType)
gen_ale_BoolType_typeLiteral = Generalization(general=typeLiteral, specific=ale_BoolType)
gen_ale_SeqType_typeLiteral = Generalization(general=typeLiteral, specific=ale_SeqType)
gen_ale_SetType_typeLiteral = Generalization(general=typeLiteral, specific=ale_SetType)
gen_ale_ClassifierSetType_typeLiteral = Generalization(general=typeLiteral, specific=ale_ClassifierSetType)
gen_ale_ClassifierType_classifierTypeRule = Generalization(general=classifierTypeRule, specific=ale_ClassifierType)

# Domain Model
domain_model = DomainModel(
    name="ale",
    types={ale_Attribute, ale_Unit, ale_Import, ale_Service, ale_BehavioredClass, ale_rOpposite, ale_Operation, ale_ExtendedClass, BehavioredClass, ale_RuntimeClass, ale_Tag, ale_rType, ale_Variable, ale_Block, ale_Remove, ale_ExpressionStmt, ale_Statement, ale_VarDecl, Statement, ale_Assign, ale_Expression, ale_Insert, ale_While, ale_ForEach, ale_Collection, ale_If, ale_EObject, ale_binding, ale_rSwitch, ale_rCase, ale_Mult, ale_Add, ale_typeLiteral, ale_literal, literal, rType, ale_classifierTypeRule, typeLiteral, ale_Call, Expression, ale_Feature, ale_Apply, ale_Implie, ale_Not, ale_Min, ale_Comp, ale_And, ale_Or, ale_Xor, ale_False, ale_Null, ale_Sequence, ale_OrderedSet, ale_Enum, ale_VarRef, ale_Lit, ale_Conditional, ale_Let, ale_String, ale_Int, ale_Real, ale_True, ale_StringType, ale_IntType, ale_RealType, ale_BoolType, ale_SeqType, ale_SetType, ale_ClassifierSetType, ale_ClassifierType, classifierTypeRule},
    associations={attributes5, imports0, services1, xtendedClasses3, type17, opposite20, operations7, tag9, type11, params13, body15, target36, exp38, target41, exp43, type22, exp25, type27, exp29, target32, exp33, else60, nestedIf64, cond66, collection46, block47, exp50, statements53, cond55, then57, value84, exp87, block68, paramVal71, cases73, other75, guard78, match81, params108, left111, right113, type89, exp90, target93, params95, target98, target100, varType102, lambda105, left141, right143, exp146, left116, right118, left121, right123, left126, right128, left131, right133, left136, right138, params164, params166, exp148, literal150, cond151, then153, else156, bindings159, exp161, type168, type170, types172},
    generalizations={gen_ale_ExtendedClass_BehavioredClass, gen_ale_RuntimeClass_BehavioredClass, gen_ale_Remove_Statement, gen_ale_VarDecl_Statement, gen_ale_Assign_Statement, gen_ale_Insert_Statement, gen_ale_While_Statement, gen_ale_ForEach_Statement, gen_ale_If_Statement, gen_ale_ExpressionStmt_Statement, gen_ale_Mult_Expression, gen_ale_Add_Expression, gen_ale_typeLiteral_literal, gen_ale_typeLiteral_rType, gen_ale_classifierTypeRule_typeLiteral, gen_ale_Call_Expression, gen_ale_Feature_Expression, gen_ale_Apply_Expression, gen_ale_Implie_Expression, gen_ale_Not_Expression, gen_ale_Min_Expression, gen_ale_Comp_Expression, gen_ale_And_Expression, gen_ale_Or_Expression, gen_ale_Xor_Expression, gen_ale_False_literal, gen_ale_Null_literal, gen_ale_Sequence_literal, gen_ale_OrderedSet_literal, gen_ale_Enum_literal, gen_ale_VarRef_Expression, gen_ale_Lit_Expression, gen_ale_Conditional_Expression, gen_ale_Let_Expression, gen_ale_String_literal, gen_ale_Int_literal, gen_ale_Real_literal, gen_ale_True_literal, gen_ale_StringType_typeLiteral, gen_ale_IntType_typeLiteral, gen_ale_RealType_typeLiteral, gen_ale_BoolType_typeLiteral, gen_ale_SeqType_typeLiteral, gen_ale_SetType_typeLiteral, gen_ale_ClassifierSetType_typeLiteral, gen_ale_ClassifierType_classifierTypeRule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)