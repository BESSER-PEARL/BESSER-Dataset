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
types_RealType = Class(name="types::RealType")
NumberType = Class(name="NumberType")
types_StringType = Class(name="types::StringType")
types_ObjectType = Class(name="types::ObjectType")
types_EClass = Class(name="types::EClass")
types_CollectionType = Class(name="types::CollectionType")
types_MapType = Class(name="types::MapType")
types_FunctionType = Class(name="types::FunctionType")
types_Type = Class(name="types::Type")
types_DataType = Class(name="types::DataType")
Type = Class(name="Type")
types_BooleanType = Class(name="types::BooleanType")
DataType = Class(name="DataType")
types_NumberType = Class(name="types::NumberType")
types_IntegerType = Class(name="types::IntegerType")
RealType = Class(name="RealType")
types_MethodType = Class(name="types::MethodType")
FunctionType = Class(name="FunctionType")
types_EnumType = Class(name="types::EnumType")
types_EEnum = Class(name="types::EEnum")

# types_RealType class attributes and methods

# NumberType class attributes and methods

# types_StringType class attributes and methods

# types_ObjectType class attributes and methods

# types_EClass class attributes and methods

# types_CollectionType class attributes and methods

# types_MapType class attributes and methods

# types_FunctionType class attributes and methods
types_FunctionType_optionalParameterCount: Property = Property(name="optionalParameterCount", type=IntegerType)
types_FunctionType.attributes={types_FunctionType_optionalParameterCount}

# types_Type class attributes and methods
types_Type_inExtentDomain: Property = Property(name="inExtentDomain", type=BooleanType)
types_Type.attributes={types_Type_inExtentDomain}

# types_DataType class attributes and methods

# Type class attributes and methods

# types_BooleanType class attributes and methods

# DataType class attributes and methods

# types_NumberType class attributes and methods

# types_IntegerType class attributes and methods

# RealType class attributes and methods

# types_MethodType class attributes and methods

# FunctionType class attributes and methods

# types_EnumType class attributes and methods

# types_EEnum class attributes and methods

# Relationships
objectClass0: BinaryAssociation = BinaryAssociation(
    name="objectClass0",
    ends={
        Property(name="types_EClass", type=types_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ObjectType", type=types_EClass, multiplicity=Multiplicity(1, 1))
    }
)
elementType1: BinaryAssociation = BinaryAssociation(
    name="elementType1",
    ends={
        Property(name="types_Type", type=types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_CollectionType", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
keyType2: BinaryAssociation = BinaryAssociation(
    name="keyType2",
    ends={
        Property(name="types_Type3", type=types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MapType", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
valueType4: BinaryAssociation = BinaryAssociation(
    name="valueType4",
    ends={
        Property(name="types_Type6", type=types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MapType5", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
returnType7: BinaryAssociation = BinaryAssociation(
    name="returnType7",
    ends={
        Property(name="types_Type8", type=types_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_FunctionType", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameterTypes9: BinaryAssociation = BinaryAssociation(
    name="parameterTypes9",
    ends={
        Property(name="types_Type11", type=types_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_FunctionType10", type=types_Type, multiplicity=Multiplicity(0, 9999))
    }
)
objectType12: BinaryAssociation = BinaryAssociation(
    name="objectType12",
    ends={
        Property(name="types_Type13", type=types_MethodType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MethodType", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
enumClass14: BinaryAssociation = BinaryAssociation(
    name="enumClass14",
    ends={
        Property(name="types_EEnum", type=types_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_EnumType", type=types_EEnum, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_types_RealType_NumberType = Generalization(general=NumberType, specific=types_RealType)
gen_types_StringType_DataType = Generalization(general=DataType, specific=types_StringType)
gen_types_ObjectType_Type = Generalization(general=Type, specific=types_ObjectType)
gen_types_CollectionType_Type = Generalization(general=Type, specific=types_CollectionType)
gen_types_MapType_Type = Generalization(general=Type, specific=types_MapType)
gen_types_FunctionType_Type = Generalization(general=Type, specific=types_FunctionType)
gen_types_DataType_Type = Generalization(general=Type, specific=types_DataType)
gen_types_BooleanType_DataType = Generalization(general=DataType, specific=types_BooleanType)
gen_types_NumberType_DataType = Generalization(general=DataType, specific=types_NumberType)
gen_types_IntegerType_RealType = Generalization(general=RealType, specific=types_IntegerType)
gen_types_MethodType_FunctionType = Generalization(general=FunctionType, specific=types_MethodType)
gen_types_EnumType_Type = Generalization(general=Type, specific=types_EnumType)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_RealType, NumberType, types_StringType, types_ObjectType, types_EClass, types_CollectionType, types_MapType, types_FunctionType, types_Type, types_DataType, Type, types_BooleanType, DataType, types_NumberType, types_IntegerType, RealType, types_MethodType, FunctionType, types_EnumType, types_EEnum},
    associations={objectClass0, elementType1, keyType2, valueType4, returnType7, parameterTypes9, objectType12, enumClass14},
    generalizations={gen_types_RealType_NumberType, gen_types_StringType_DataType, gen_types_ObjectType_Type, gen_types_CollectionType_Type, gen_types_MapType_Type, gen_types_FunctionType_Type, gen_types_DataType_Type, gen_types_BooleanType_DataType, gen_types_NumberType_DataType, gen_types_IntegerType_RealType, gen_types_MethodType_FunctionType, gen_types_EnumType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)