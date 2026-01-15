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
types_Type = Class(name="types::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
types_TypeConstraint = Class(name="types::TypeConstraint")
types_Feature = Class(name="types::Feature", is_abstract=True)
TypedElement = Class(name="TypedElement")
types_ComplexType = Class(name="types::ComplexType")
types_Operation = Class(name="types::Operation")
Feature = Class(name="Feature")
types_Parameter = Class(name="types::Parameter")
types_Property = Class(name="types::Property")
types_TypedElement = Class(name="types::TypedElement", is_abstract=True)
types_Event = Class(name="types::Event")
types_EnumerationType = Class(name="types::EnumerationType")
PrimitiveType = Class(name="PrimitiveType")
types_Enumerator = Class(name="types::Enumerator")
types_PrimitiveType = Class(name="types::PrimitiveType")
Type = Class(name="Type")

# types_Type class attributes and methods

# NamedElement class attributes and methods

# types_TypeConstraint class attributes and methods
types_TypeConstraint_value: Property = Property(name="value", type=StringType)
types_TypeConstraint.attributes={types_TypeConstraint_value}

# types_Feature class attributes and methods

# TypedElement class attributes and methods

# types_ComplexType class attributes and methods

# types_Operation class attributes and methods

# Feature class attributes and methods

# types_Parameter class attributes and methods

# types_Property class attributes and methods

# types_TypedElement class attributes and methods

# types_Event class attributes and methods

# types_EnumerationType class attributes and methods

# PrimitiveType class attributes and methods

# types_Enumerator class attributes and methods
types_Enumerator_literalValue: Property = Property(name="literalValue", type=StringType)
types_Enumerator.attributes={types_Enumerator_literalValue}

# types_PrimitiveType class attributes and methods

# Type class attributes and methods

# Relationships
constraint0: BinaryAssociation = BinaryAssociation(
    name="constraint0",
    ends={
        Property(name="types_TypeConstraint", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Type", type=types_TypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningType1: BinaryAssociation = BinaryAssociation(
    name="owningType1",
    ends={
        Property(name="ComplexType", type=types_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=types_ComplexType, multiplicity=Multiplicity(0, 1))
    }
)
parameters2: BinaryAssociation = BinaryAssociation(
    name="parameters2",
    ends={
        Property(name="Parameter", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=types_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="types_Type5", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
enumerator6: BinaryAssociation = BinaryAssociation(
    name="enumerator6",
    ends={
        Property(name="Enumerator", type=types_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningEnumeration", type=types_Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType8: BinaryAssociation = BinaryAssociation(
    name="baseType8",
    ends={
        Property(name="types_PrimitiveType", type=types_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_PrimitiveType7", type=types_PrimitiveType, multiplicity=Multiplicity(0, 1))
    }
)
features9: BinaryAssociation = BinaryAssociation(
    name="features9",
    ends={
        Property(name="Feature", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=types_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes11: BinaryAssociation = BinaryAssociation(
    name="superTypes11",
    ends={
        Property(name="types_ComplexType", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ComplexType10", type=types_ComplexType, multiplicity=Multiplicity(0, 9999))
    }
)
owningEnumeration12: BinaryAssociation = BinaryAssociation(
    name="owningEnumeration12",
    ends={
        Property(name="EnumerationType", type=types_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="enumerator", type=types_EnumerationType, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation3: BinaryAssociation = BinaryAssociation(
    name="owningOperation3",
    ends={
        Property(name="Operation", type=types_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=types_Operation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_types_Type_NamedElement = Generalization(general=NamedElement, specific=types_Type)
gen_types_Feature_TypedElement = Generalization(general=TypedElement, specific=types_Feature)
gen_types_Feature_NamedElement = Generalization(general=NamedElement, specific=types_Feature)
gen_types_Operation_Feature = Generalization(general=Feature, specific=types_Operation)
gen_types_Property_Feature = Generalization(general=Feature, specific=types_Property)
gen_types_Parameter_TypedElement = Generalization(general=TypedElement, specific=types_Parameter)
gen_types_Parameter_NamedElement = Generalization(general=NamedElement, specific=types_Parameter)
gen_types_Event_Feature = Generalization(general=Feature, specific=types_Event)
gen_types_EnumerationType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_EnumerationType)
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_ComplexType_Type = Generalization(general=Type, specific=types_ComplexType)
gen_types_Enumerator_NamedElement = Generalization(general=NamedElement, specific=types_Enumerator)
gen_types_TypeConstraint_NamedElement = Generalization(general=NamedElement, specific=types_TypeConstraint)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Type, NamedElement, types_TypeConstraint, types_Feature, TypedElement, types_ComplexType, types_Operation, Feature, types_Parameter, types_Property, types_TypedElement, types_Event, types_EnumerationType, PrimitiveType, types_Enumerator, types_PrimitiveType, Type},
    associations={constraint0, owningType1, parameters2, type4, enumerator6, baseType8, features9, superTypes11, owningEnumeration12, owningOperation3},
    generalizations={gen_types_Type_NamedElement, gen_types_Feature_TypedElement, gen_types_Feature_NamedElement, gen_types_Operation_Feature, gen_types_Property_Feature, gen_types_Parameter_TypedElement, gen_types_Parameter_NamedElement, gen_types_Event_Feature, gen_types_EnumerationType_PrimitiveType, gen_types_PrimitiveType_Type, gen_types_ComplexType_Type, gen_types_Enumerator_NamedElement, gen_types_TypeConstraint_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)