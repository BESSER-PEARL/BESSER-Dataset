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
fIDL_Declaration = Class(name="fIDL::Declaration")
fIDL_ConstDeclaration = Class(name="fIDL::ConstDeclaration")
Declaration = Class(name="Declaration")
fIDL_File = Class(name="fIDL::File")
fIDL_LibraryHeader = Class(name="fIDL::LibraryHeader")
File = Class(name="File")
fIDL_Using = Class(name="fIDL::Using")
fIDL_AttributedDeclaration = Class(name="fIDL::AttributedDeclaration")
fIDL_Attribute = Class(name="fIDL::Attribute")
fIDL_InterfaceDeclaration = Class(name="fIDL::InterfaceDeclaration")
fIDL_InterfaceMember = Class(name="fIDL::InterfaceMember")
InterfaceMember = Class(name="InterfaceMember")
fIDL_Type = Class(name="fIDL::Type")
fIDL_Constant = Class(name="fIDL::Constant")
fIDL_EnumDeclaration = Class(name="fIDL::EnumDeclaration")
fIDL_IntegerType = Class(name="fIDL::IntegerType")
fIDL_EnumMember = Class(name="fIDL::EnumMember")
fIDL_EnumMemberValue = Class(name="fIDL::EnumMemberValue")
fIDL_StructDeclaration = Class(name="fIDL::StructDeclaration")
fIDL_StructMember = Class(name="fIDL::StructMember")
fIDL_InterfaceMethod = Class(name="fIDL::InterfaceMethod")
fIDL_Expression = Class(name="fIDL::Expression")
fIDL_InterfaceParameters = Class(name="fIDL::InterfaceParameters")
fIDL_ParameterList = Class(name="fIDL::ParameterList")
fIDL_Parameter = Class(name="fIDL::Parameter")
fIDL_UnionMember = Class(name="fIDL::UnionMember")
fIDL_UnionField = Class(name="fIDL::UnionField")
UnionMember = Class(name="UnionMember")
fIDL_StructField = Class(name="fIDL::StructField")
fIDL_IdentifierType = Class(name="fIDL::IdentifierType")
Type = Class(name="Type")
fIDL_ArrayType = Class(name="fIDL::ArrayType")
fIDL_UnionDeclaration = Class(name="fIDL::UnionDeclaration")
fIDL_VectorType = Class(name="fIDL::VectorType")
fIDL_StringType = Class(name="fIDL::StringType")
fIDL_HandleType = Class(name="fIDL::HandleType")
fIDL_RequestType = Class(name="fIDL::RequestType")
fIDL_PrimitiveType = Class(name="fIDL::PrimitiveType")
PrimitiveType = Class(name="PrimitiveType")
fIDL_Literal = Class(name="fIDL::Literal")
Constant = Class(name="Constant")
EnumMemberValue = Class(name="EnumMemberValue")
Literal = Class(name="Literal")
fIDL_StatusType = Class(name="fIDL::StatusType")
fIDL_BooleanType = Class(name="fIDL::BooleanType")
fIDL_Float32Type = Class(name="fIDL::Float32Type")
fIDL_Float64Type = Class(name="fIDL::Float64Type")
fIDL_Int8Type = Class(name="fIDL::Int8Type")
IntegerType = Class(name="IntegerType")
fIDL_Int16Type = Class(name="fIDL::Int16Type")
fIDL_Int32Type = Class(name="fIDL::Int32Type")
fIDL_Int64Type = Class(name="fIDL::Int64Type")
fIDL_Uint8Type = Class(name="fIDL::Uint8Type")
fIDL_Uint16Type = Class(name="fIDL::Uint16Type")
fIDL_Uint32Type = Class(name="fIDL::Uint32Type")
fIDL_Uint64Type = Class(name="fIDL::Uint64Type")
fIDL_BooleanLiteral = Class(name="fIDL::BooleanLiteral")
Expression = Class(name="Expression")
fIDL_NumberLiteral = Class(name="fIDL::NumberLiteral")
fIDL_StringLiteral = Class(name="fIDL::StringLiteral")

# fIDL_Declaration class attributes and methods
fIDL_Declaration_name: Property = Property(name="name", type=StringType)
fIDL_Declaration.attributes={fIDL_Declaration_name}

# fIDL_ConstDeclaration class attributes and methods

# Declaration class attributes and methods

# fIDL_File class attributes and methods

# fIDL_LibraryHeader class attributes and methods
fIDL_LibraryHeader_name: Property = Property(name="name", type=StringType)
fIDL_LibraryHeader.attributes={fIDL_LibraryHeader_name}

# File class attributes and methods

# fIDL_Using class attributes and methods
fIDL_Using_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
fIDL_Using_name: Property = Property(name="name", type=StringType)
fIDL_Using.attributes={fIDL_Using_importedNamespace, fIDL_Using_name}

# fIDL_AttributedDeclaration class attributes and methods

# fIDL_Attribute class attributes and methods
fIDL_Attribute_name: Property = Property(name="name", type=StringType)
fIDL_Attribute_value: Property = Property(name="value", type=StringType)
fIDL_Attribute.attributes={fIDL_Attribute_value, fIDL_Attribute_name}

# fIDL_InterfaceDeclaration class attributes and methods

# fIDL_InterfaceMember class attributes and methods

# InterfaceMember class attributes and methods

# fIDL_Type class attributes and methods

# fIDL_Constant class attributes and methods
fIDL_Constant_ci: Property = Property(name="ci", type=StringType)
fIDL_Constant.attributes={fIDL_Constant_ci}

# fIDL_EnumDeclaration class attributes and methods

# fIDL_IntegerType class attributes and methods

# fIDL_EnumMember class attributes and methods
fIDL_EnumMember_name: Property = Property(name="name", type=StringType)
fIDL_EnumMember.attributes={fIDL_EnumMember_name}

# fIDL_EnumMemberValue class attributes and methods
fIDL_EnumMemberValue_value: Property = Property(name="value", type=StringType)
fIDL_EnumMemberValue.attributes={fIDL_EnumMemberValue_value}

# fIDL_StructDeclaration class attributes and methods

# fIDL_StructMember class attributes and methods

# fIDL_InterfaceMethod class attributes and methods

# fIDL_Expression class attributes and methods

# fIDL_InterfaceParameters class attributes and methods
fIDL_InterfaceParameters_name: Property = Property(name="name", type=StringType)
fIDL_InterfaceParameters_resultName: Property = Property(name="resultName", type=StringType)
fIDL_InterfaceParameters.attributes={fIDL_InterfaceParameters_resultName, fIDL_InterfaceParameters_name}

# fIDL_ParameterList class attributes and methods

# fIDL_Parameter class attributes and methods
fIDL_Parameter_name: Property = Property(name="name", type=StringType)
fIDL_Parameter.attributes={fIDL_Parameter_name}

# fIDL_UnionMember class attributes and methods

# fIDL_UnionField class attributes and methods
fIDL_UnionField_name: Property = Property(name="name", type=StringType)
fIDL_UnionField.attributes={fIDL_UnionField_name}

# UnionMember class attributes and methods

# fIDL_StructField class attributes and methods
fIDL_StructField_name: Property = Property(name="name", type=StringType)
fIDL_StructField.attributes={fIDL_StructField_name}

# fIDL_IdentifierType class attributes and methods
fIDL_IdentifierType_nullable: Property = Property(name="nullable", type=BooleanType)
fIDL_IdentifierType.attributes={fIDL_IdentifierType_nullable}

# Type class attributes and methods

# fIDL_ArrayType class attributes and methods

# fIDL_UnionDeclaration class attributes and methods

# fIDL_VectorType class attributes and methods
fIDL_VectorType_nullable: Property = Property(name="nullable", type=BooleanType)
fIDL_VectorType.attributes={fIDL_VectorType_nullable}

# fIDL_StringType class attributes and methods
fIDL_StringType_nullable: Property = Property(name="nullable", type=BooleanType)
fIDL_StringType.attributes={fIDL_StringType_nullable}

# fIDL_HandleType class attributes and methods
fIDL_HandleType_type: Property = Property(name="type", type=StringType)
fIDL_HandleType_nullable: Property = Property(name="nullable", type=BooleanType)
fIDL_HandleType.attributes={fIDL_HandleType_type, fIDL_HandleType_nullable}

# fIDL_RequestType class attributes and methods
fIDL_RequestType_nullable: Property = Property(name="nullable", type=BooleanType)
fIDL_RequestType.attributes={fIDL_RequestType_nullable}

# fIDL_PrimitiveType class attributes and methods

# PrimitiveType class attributes and methods

# fIDL_Literal class attributes and methods

# Constant class attributes and methods

# EnumMemberValue class attributes and methods

# Literal class attributes and methods

# fIDL_StatusType class attributes and methods

# fIDL_BooleanType class attributes and methods

# fIDL_Float32Type class attributes and methods

# fIDL_Float64Type class attributes and methods

# fIDL_Int8Type class attributes and methods

# IntegerType class attributes and methods

# fIDL_Int16Type class attributes and methods

# fIDL_Int32Type class attributes and methods

# fIDL_Int64Type class attributes and methods

# fIDL_Uint8Type class attributes and methods

# fIDL_Uint16Type class attributes and methods

# fIDL_Uint32Type class attributes and methods

# fIDL_Uint64Type class attributes and methods

# fIDL_BooleanLiteral class attributes and methods
fIDL_BooleanLiteral_isTrue: Property = Property(name="isTrue", type=BooleanType)
fIDL_BooleanLiteral.attributes={fIDL_BooleanLiteral_isTrue}

# Expression class attributes and methods

# fIDL_NumberLiteral class attributes and methods

# fIDL_StringLiteral class attributes and methods

# Relationships
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="fIDL_Attribute", type=fIDL_AttributedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_AttributedDeclaration4", type=fIDL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration5: BinaryAssociation = BinaryAssociation(
    name="declaration5",
    ends={
        Property(name="fIDL_Declaration", type=fIDL_AttributedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_AttributedDeclaration6", type=fIDL_Declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usings0: BinaryAssociation = BinaryAssociation(
    name="usings0",
    ends={
        Property(name="fIDL_Using", type=fIDL_LibraryHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_LibraryHeader", type=fIDL_Using, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="fIDL_AttributedDeclaration", type=fIDL_LibraryHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_LibraryHeader2", type=fIDL_AttributedDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces16: BinaryAssociation = BinaryAssociation(
    name="superInterfaces16",
    ends={
        Property(name="fIDL_InterfaceDeclaration", type=fIDL_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_InterfaceDeclaration15", type=fIDL_InterfaceDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
members17: BinaryAssociation = BinaryAssociation(
    name="members17",
    ends={
        Property(name="fIDL_InterfaceMember", type=fIDL_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_InterfaceDeclaration18", type=fIDL_InterfaceMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="fIDL_Type", type=fIDL_ConstDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_ConstDeclaration", type=fIDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value8: BinaryAssociation = BinaryAssociation(
    name="value8",
    ends={
        Property(name="fIDL_Constant", type=fIDL_ConstDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_ConstDeclaration9", type=fIDL_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="fIDL_IntegerType", type=fIDL_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_EnumDeclaration", type=fIDL_IntegerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members11: BinaryAssociation = BinaryAssociation(
    name="members11",
    ends={
        Property(name="fIDL_EnumMember", type=fIDL_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_EnumDeclaration12", type=fIDL_EnumMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="fIDL_EnumMemberValue", type=fIDL_EnumMember, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_EnumMember14", type=fIDL_EnumMemberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters27: BinaryAssociation = BinaryAssociation(
    name="parameters27",
    ends={
        Property(name="fIDL_ParameterList28", type=fIDL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="fIDL_Parameter", type=fIDL_ParameterList, multiplicity=Multiplicity(1, 1))
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="fIDL_Type31", type=fIDL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_Parameter30", type=fIDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members32: BinaryAssociation = BinaryAssociation(
    name="members32",
    ends={
        Property(name="fIDL_StructMember", type=fIDL_StructDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_StructDeclaration", type=fIDL_StructMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ordinal19: BinaryAssociation = BinaryAssociation(
    name="ordinal19",
    ends={
        Property(name="fIDL_Expression", type=fIDL_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_InterfaceMethod", type=fIDL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method20: BinaryAssociation = BinaryAssociation(
    name="method20",
    ends={
        Property(name="fIDL_InterfaceParameters", type=fIDL_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_InterfaceMethod21", type=fIDL_InterfaceParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters22: BinaryAssociation = BinaryAssociation(
    name="parameters22",
    ends={
        Property(name="fIDL_ParameterList", type=fIDL_InterfaceParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_InterfaceParameters23", type=fIDL_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result24: BinaryAssociation = BinaryAssociation(
    name="result24",
    ends={
        Property(name="fIDL_ParameterList26", type=fIDL_InterfaceParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_InterfaceParameters25", type=fIDL_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields46: BinaryAssociation = BinaryAssociation(
    name="fields46",
    ends={
        Property(name="fIDL_UnionMember", type=fIDL_UnionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_UnionDeclaration47", type=fIDL_UnionMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="fIDL_Type49", type=fIDL_UnionField, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_UnionField", type=fIDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field33: BinaryAssociation = BinaryAssociation(
    name="field33",
    ends={
        Property(name="fIDL_StructField", type=fIDL_StructMember, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_StructMember34", type=fIDL_StructField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant35: BinaryAssociation = BinaryAssociation(
    name="constant35",
    ends={
        Property(name="fIDL_ConstDeclaration37", type=fIDL_StructMember, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_StructMember36", type=fIDL_ConstDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref50: BinaryAssociation = BinaryAssociation(
    name="ref50",
    ends={
        Property(name="fIDL_Declaration51", type=fIDL_IdentifierType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_IdentifierType", type=fIDL_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="fIDL_Type40", type=fIDL_StructField, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_StructField39", type=fIDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="fIDL_Type53", type=fIDL_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_ArrayType", type=fIDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value41: BinaryAssociation = BinaryAssociation(
    name="value41",
    ends={
        Property(name="fIDL_Constant43", type=fIDL_StructField, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_StructField42", type=fIDL_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint54: BinaryAssociation = BinaryAssociation(
    name="constraint54",
    ends={
        Property(name="fIDL_Constant56", type=fIDL_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_ArrayType55", type=fIDL_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members44: BinaryAssociation = BinaryAssociation(
    name="members44",
    ends={
        Property(name="fIDL_ConstDeclaration45", type=fIDL_UnionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_UnionDeclaration", type=fIDL_ConstDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint59: BinaryAssociation = BinaryAssociation(
    name="constraint59",
    ends={
        Property(name="fIDL_Constant61", type=fIDL_VectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_VectorType60", type=fIDL_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint62: BinaryAssociation = BinaryAssociation(
    name="constraint62",
    ends={
        Property(name="fIDL_Constant63", type=fIDL_StringType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_StringType", type=fIDL_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref64: BinaryAssociation = BinaryAssociation(
    name="ref64",
    ends={
        Property(name="fIDL_Declaration65", type=fIDL_RequestType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_RequestType", type=fIDL_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
type57: BinaryAssociation = BinaryAssociation(
    name="type57",
    ends={
        Property(name="fIDL_Type58", type=fIDL_VectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="fIDL_VectorType", type=fIDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_fIDL_ConstDeclaration_Declaration = Generalization(general=Declaration, specific=fIDL_ConstDeclaration)
gen_fIDL_LibraryHeader_File = Generalization(general=File, specific=fIDL_LibraryHeader)
gen_fIDL_InterfaceDeclaration_Declaration = Generalization(general=Declaration, specific=fIDL_InterfaceDeclaration)
gen_fIDL_ConstDeclaration_InterfaceMember = Generalization(general=InterfaceMember, specific=fIDL_ConstDeclaration)
gen_fIDL_EnumDeclaration_Declaration = Generalization(general=Declaration, specific=fIDL_EnumDeclaration)
gen_fIDL_StructDeclaration_Declaration = Generalization(general=Declaration, specific=fIDL_StructDeclaration)
gen_fIDL_InterfaceMethod_InterfaceMember = Generalization(general=InterfaceMember, specific=fIDL_InterfaceMethod)
gen_fIDL_UnionField_UnionMember = Generalization(general=UnionMember, specific=fIDL_UnionField)
gen_fIDL_IdentifierType_Type = Generalization(general=Type, specific=fIDL_IdentifierType)
gen_fIDL_ArrayType_Type = Generalization(general=Type, specific=fIDL_ArrayType)
gen_fIDL_UnionDeclaration_Declaration = Generalization(general=Declaration, specific=fIDL_UnionDeclaration)
gen_fIDL_VectorType_Type = Generalization(general=Type, specific=fIDL_VectorType)
gen_fIDL_Expression_Literal = Generalization(general=Literal, specific=fIDL_Expression)
gen_fIDL_StringType_Type = Generalization(general=Type, specific=fIDL_StringType)
gen_fIDL_HandleType_Type = Generalization(general=Type, specific=fIDL_HandleType)
gen_fIDL_RequestType_Type = Generalization(general=Type, specific=fIDL_RequestType)
gen_fIDL_PrimitiveType_Type = Generalization(general=Type, specific=fIDL_PrimitiveType)
gen_fIDL_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=fIDL_IntegerType)
gen_fIDL_Literal_Constant = Generalization(general=Constant, specific=fIDL_Literal)
gen_fIDL_Expression_EnumMemberValue = Generalization(general=EnumMemberValue, specific=fIDL_Expression)
gen_fIDL_StatusType_PrimitiveType = Generalization(general=PrimitiveType, specific=fIDL_StatusType)
gen_fIDL_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=fIDL_BooleanType)
gen_fIDL_Float32Type_PrimitiveType = Generalization(general=PrimitiveType, specific=fIDL_Float32Type)
gen_fIDL_Float64Type_PrimitiveType = Generalization(general=PrimitiveType, specific=fIDL_Float64Type)
gen_fIDL_Int8Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Int8Type)
gen_fIDL_Int16Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Int16Type)
gen_fIDL_Int32Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Int32Type)
gen_fIDL_Int64Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Int64Type)
gen_fIDL_Uint8Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Uint8Type)
gen_fIDL_Uint16Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Uint16Type)
gen_fIDL_Uint32Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Uint32Type)
gen_fIDL_Uint64Type_IntegerType = Generalization(general=IntegerType, specific=fIDL_Uint64Type)
gen_fIDL_BooleanLiteral_Expression = Generalization(general=Expression, specific=fIDL_BooleanLiteral)
gen_fIDL_NumberLiteral_Expression = Generalization(general=Expression, specific=fIDL_NumberLiteral)
gen_fIDL_StringLiteral_Expression = Generalization(general=Expression, specific=fIDL_StringLiteral)

# Domain Model
domain_model = DomainModel(
    name="fIDL",
    types={fIDL_Declaration, fIDL_ConstDeclaration, Declaration, fIDL_File, fIDL_LibraryHeader, File, fIDL_Using, fIDL_AttributedDeclaration, fIDL_Attribute, fIDL_InterfaceDeclaration, fIDL_InterfaceMember, InterfaceMember, fIDL_Type, fIDL_Constant, fIDL_EnumDeclaration, fIDL_IntegerType, fIDL_EnumMember, fIDL_EnumMemberValue, fIDL_StructDeclaration, fIDL_StructMember, fIDL_InterfaceMethod, fIDL_Expression, fIDL_InterfaceParameters, fIDL_ParameterList, fIDL_Parameter, fIDL_UnionMember, fIDL_UnionField, UnionMember, fIDL_StructField, fIDL_IdentifierType, Type, fIDL_ArrayType, fIDL_UnionDeclaration, fIDL_VectorType, fIDL_StringType, fIDL_HandleType, fIDL_RequestType, fIDL_PrimitiveType, PrimitiveType, fIDL_Literal, Constant, EnumMemberValue, Literal, fIDL_StatusType, fIDL_BooleanType, fIDL_Float32Type, fIDL_Float64Type, fIDL_Int8Type, IntegerType, fIDL_Int16Type, fIDL_Int32Type, fIDL_Int64Type, fIDL_Uint8Type, fIDL_Uint16Type, fIDL_Uint32Type, fIDL_Uint64Type, fIDL_BooleanLiteral, Expression, fIDL_NumberLiteral, fIDL_StringLiteral},
    associations={attributes3, declaration5, usings0, declarations1, superInterfaces16, members17, type7, value8, type10, members11, value13, parameters27, type29, members32, ordinal19, method20, parameters22, result24, fields46, type48, field33, constant35, ref50, type38, type52, value41, constraint54, members44, constraint59, constraint62, ref64, type57},
    generalizations={gen_fIDL_ConstDeclaration_Declaration, gen_fIDL_LibraryHeader_File, gen_fIDL_InterfaceDeclaration_Declaration, gen_fIDL_ConstDeclaration_InterfaceMember, gen_fIDL_EnumDeclaration_Declaration, gen_fIDL_StructDeclaration_Declaration, gen_fIDL_InterfaceMethod_InterfaceMember, gen_fIDL_UnionField_UnionMember, gen_fIDL_IdentifierType_Type, gen_fIDL_ArrayType_Type, gen_fIDL_UnionDeclaration_Declaration, gen_fIDL_VectorType_Type, gen_fIDL_Expression_Literal, gen_fIDL_StringType_Type, gen_fIDL_HandleType_Type, gen_fIDL_RequestType_Type, gen_fIDL_PrimitiveType_Type, gen_fIDL_IntegerType_PrimitiveType, gen_fIDL_Literal_Constant, gen_fIDL_Expression_EnumMemberValue, gen_fIDL_StatusType_PrimitiveType, gen_fIDL_BooleanType_PrimitiveType, gen_fIDL_Float32Type_PrimitiveType, gen_fIDL_Float64Type_PrimitiveType, gen_fIDL_Int8Type_IntegerType, gen_fIDL_Int16Type_IntegerType, gen_fIDL_Int32Type_IntegerType, gen_fIDL_Int64Type_IntegerType, gen_fIDL_Uint8Type_IntegerType, gen_fIDL_Uint16Type_IntegerType, gen_fIDL_Uint32Type_IntegerType, gen_fIDL_Uint64Type_IntegerType, gen_fIDL_BooleanLiteral_Expression, gen_fIDL_NumberLiteral_Expression, gen_fIDL_StringLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)