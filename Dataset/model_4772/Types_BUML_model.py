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
types_Type = Class(name="types::Type")
types_PrimitiveType = Class(name="types::PrimitiveType")
Type = Class(name="Type")
types_UserType = Class(name="types::UserType")
types_ClassType = Class(name="types::ClassType")
UserType = Class(name="UserType")
types_ServiceType = Class(name="types::ServiceType")
types_Operation = Class(name="types::Operation")
types_EObject = Class(name="types::EObject")
types_Property = Class(name="types::Property")
types_TypeReference = Class(name="types::TypeReference")
types_ArrayType = Class(name="types::ArrayType")
TypeReference = Class(name="TypeReference")

# types_Type class attributes and methods
types_Type_name: Property = Property(name="name", type=StringType)
types_Type.attributes={types_Type_name}

# types_PrimitiveType class attributes and methods

# Type class attributes and methods

# types_UserType class attributes and methods

# types_ClassType class attributes and methods

# UserType class attributes and methods

# types_ServiceType class attributes and methods

# types_Operation class attributes and methods
types_Operation_name: Property = Property(name="name", type=StringType)
types_Operation.attributes={types_Operation_name}

# types_EObject class attributes and methods

# types_Property class attributes and methods
types_Property_name: Property = Property(name="name", type=StringType)
types_Property.attributes={types_Property_name}

# types_TypeReference class attributes and methods

# types_ArrayType class attributes and methods
types_ArrayType_size: Property = Property(name="size", type=IntegerType)
types_ArrayType.attributes={types_ArrayType_size}

# TypeReference class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="types_ClassType", type=types_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ClassType0", type=types_ClassType, multiplicity=Multiplicity(0, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="types_TypeReference7", type=types_Type, multiplicity=Multiplicity(0, 1)),
        Property(name="types_Type", type=types_TypeReference, multiplicity=Multiplicity(1, 1))
    }
)
remainder9: BinaryAssociation = BinaryAssociation(
    name="remainder9",
    ends={
        Property(name="types_TypeReference10", type=types_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeReference8", type=types_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configurations11: BinaryAssociation = BinaryAssociation(
    name="configurations11",
    ends={
        Property(name="types_Property12", type=types_ServiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ServiceType", type=types_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations13: BinaryAssociation = BinaryAssociation(
    name="operations13",
    ends={
        Property(name="types_Operation", type=types_ServiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ServiceType14", type=types_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="types_TypeReference17", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Operation16", type=types_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters18: BinaryAssociation = BinaryAssociation(
    name="parameters18",
    ends={
        Property(name="types_Property20", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Operation19", type=types_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="types_EObject", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Operation22", type=types_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="types_Property", type=types_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ClassType3", type=types_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="types_TypeReference", type=types_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Property5", type=types_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_UserType_Type = Generalization(general=Type, specific=types_UserType)
gen_types_ClassType_UserType = Generalization(general=UserType, specific=types_ClassType)
gen_types_ServiceType_UserType = Generalization(general=UserType, specific=types_ServiceType)
gen_types_ArrayType_TypeReference = Generalization(general=TypeReference, specific=types_ArrayType)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Type, types_PrimitiveType, Type, types_UserType, types_ClassType, UserType, types_ServiceType, types_Operation, types_EObject, types_Property, types_TypeReference, types_ArrayType, TypeReference},
    associations={parent1, type6, remainder9, configurations11, operations13, type15, parameters18, expression21, properties2, type4},
    generalizations={gen_types_PrimitiveType_Type, gen_types_UserType_Type, gen_types_ClassType_UserType, gen_types_ServiceType_UserType, gen_types_ArrayType_TypeReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)