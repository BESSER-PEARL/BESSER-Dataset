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
types_Package = Class(name="types::Package")
NamedElement = Class(name="NamedElement")
types_PackageMember = Class(name="types::PackageMember")
types_Type = Class(name="types::Type", is_abstract=True)
PackageMember = Class(name="PackageMember")
types_TypeConstraint = Class(name="types::TypeConstraint")
types_Feature = Class(name="types::Feature", is_abstract=True)
TypedElement = Class(name="TypedElement")
types_ComplexType = Class(name="types::ComplexType")
types_Operation = Class(name="types::Operation")
Feature = Class(name="Feature")
types_Parameter = Class(name="types::Parameter")
types_Event = Class(name="types::Event")
types_EnumerationType = Class(name="types::EnumerationType")
PrimitiveType = Class(name="PrimitiveType")
types_Enumerator = Class(name="types::Enumerator")
types_PrimitiveType = Class(name="types::PrimitiveType")
Type = Class(name="Type")
ParameterizedType = Class(name="ParameterizedType")
types_TypeParameter = Class(name="types::TypeParameter")
types_ParameterizedType = Class(name="types::ParameterizedType")
types_RangeConstraint = Class(name="types::RangeConstraint")
TypeConstraint = Class(name="TypeConstraint")
types_Property = Class(name="types::Property")
types_TypedElement = Class(name="types::TypedElement", is_abstract=True)
types_Integer = Class(name="types::Integer")
types_Real = Class(name="types::Real")
types_Boolean = Class(name="types::Boolean")
types_String = Class(name="types::String")
types_Void = Class(name="types::Void")

# types_Package class attributes and methods

# NamedElement class attributes and methods

# types_PackageMember class attributes and methods

# types_Type class attributes and methods
types_Type_scheme: Property = Property(name="scheme", type=StringType)
types_Type.attributes={types_Type_scheme}

# PackageMember class attributes and methods

# types_TypeConstraint class attributes and methods
types_TypeConstraint_value: Property = Property(name="value", type=StringType)
types_TypeConstraint.attributes={types_TypeConstraint_value}

# types_Feature class attributes and methods

# TypedElement class attributes and methods

# types_ComplexType class attributes and methods
types_ComplexType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={}, type=Feature)
types_ComplexType.methods={types_ComplexType_m_getAllFeatures}

# types_Operation class attributes and methods

# Feature class attributes and methods

# types_Parameter class attributes and methods

# types_Event class attributes and methods

# types_EnumerationType class attributes and methods

# PrimitiveType class attributes and methods

# types_Enumerator class attributes and methods
types_Enumerator_literalValue: Property = Property(name="literalValue", type=StringType)
types_Enumerator.attributes={types_Enumerator_literalValue}

# types_PrimitiveType class attributes and methods

# Type class attributes and methods

# ParameterizedType class attributes and methods

# types_TypeParameter class attributes and methods

# types_ParameterizedType class attributes and methods

# types_RangeConstraint class attributes and methods
types_RangeConstraint_lowerBound: Property = Property(name="lowerBound", type=StringType)
types_RangeConstraint_upperBound: Property = Property(name="upperBound", type=StringType)
types_RangeConstraint_m_assignableTo: Method = Method(name="assignableTo", parameters={Parameter(name='constraint')}, type=BooleanType)
types_RangeConstraint.attributes={types_RangeConstraint_upperBound, types_RangeConstraint_lowerBound}
types_RangeConstraint.methods={types_RangeConstraint_m_assignableTo}

# TypeConstraint class attributes and methods

# types_Property class attributes and methods

# types_TypedElement class attributes and methods

# types_Integer class attributes and methods

# types_Real class attributes and methods

# types_Boolean class attributes and methods

# types_String class attributes and methods

# types_Void class attributes and methods

# Relationships
member0: BinaryAssociation = BinaryAssociation(
    name="member0",
    ends={
        Property(name="types_PackageMember", type=types_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Package", type=types_PackageMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="types_TypeConstraint", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Type", type=types_TypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningType2: BinaryAssociation = BinaryAssociation(
    name="owningType2",
    ends={
        Property(name="ComplexType", type=types_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=types_ComplexType, multiplicity=Multiplicity(0, 1))
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="Parameter", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=types_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerator10: BinaryAssociation = BinaryAssociation(
    name="enumerator10",
    ends={
        Property(name="Enumerator", type=types_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningEnumeration", type=types_Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType12: BinaryAssociation = BinaryAssociation(
    name="baseType12",
    ends={
        Property(name="types_PrimitiveType", type=types_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_PrimitiveType11", type=types_PrimitiveType, multiplicity=Multiplicity(0, 1))
    }
)
features13: BinaryAssociation = BinaryAssociation(
    name="features13",
    ends={
        Property(name="Feature", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=types_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes15: BinaryAssociation = BinaryAssociation(
    name="superTypes15",
    ends={
        Property(name="types_ComplexType", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ComplexType14", type=types_ComplexType, multiplicity=Multiplicity(0, 9999))
    }
)
owningEnumeration16: BinaryAssociation = BinaryAssociation(
    name="owningEnumeration16",
    ends={
        Property(name="EnumerationType", type=types_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="enumerator", type=types_EnumerationType, multiplicity=Multiplicity(0, 1))
    }
)
bound17: BinaryAssociation = BinaryAssociation(
    name="bound17",
    ends={
        Property(name="types_Type18", type=types_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeParameter", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameter19: BinaryAssociation = BinaryAssociation(
    name="parameter19",
    ends={
        Property(name="types_TypeParameter20", type=types_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ParameterizedType", type=types_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningOperation4: BinaryAssociation = BinaryAssociation(
    name="owningOperation4",
    ends={
        Property(name="Operation", type=types_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=types_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="types_Type6", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
typeArguments7: BinaryAssociation = BinaryAssociation(
    name="typeArguments7",
    ends={
        Property(name="types_Type9", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement8", type=types_Type, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_types_Package_NamedElement = Generalization(general=NamedElement, specific=types_Package)
gen_types_Type_PackageMember = Generalization(general=PackageMember, specific=types_Type)
gen_types_Feature_TypedElement = Generalization(general=TypedElement, specific=types_Feature)
gen_types_Feature_NamedElement = Generalization(general=NamedElement, specific=types_Feature)
gen_types_Operation_Feature = Generalization(general=Feature, specific=types_Operation)
gen_types_Event_Feature = Generalization(general=Feature, specific=types_Event)
gen_types_EnumerationType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_EnumerationType)
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_ComplexType_ParameterizedType = Generalization(general=ParameterizedType, specific=types_ComplexType)
gen_types_Enumerator_NamedElement = Generalization(general=NamedElement, specific=types_Enumerator)
gen_types_TypeParameter_Type = Generalization(general=Type, specific=types_TypeParameter)
gen_types_ParameterizedType_Type = Generalization(general=Type, specific=types_ParameterizedType)
gen_types_PackageMember_NamedElement = Generalization(general=NamedElement, specific=types_PackageMember)
gen_types_RangeConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=types_RangeConstraint)
gen_types_Property_Feature = Generalization(general=Feature, specific=types_Property)
gen_types_Parameter_TypedElement = Generalization(general=TypedElement, specific=types_Parameter)
gen_types_Parameter_NamedElement = Generalization(general=NamedElement, specific=types_Parameter)
gen_types_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Integer)
gen_types_Real_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Real)
gen_types_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Boolean)
gen_types_String_PrimitiveType = Generalization(general=PrimitiveType, specific=types_String)
gen_types_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Void)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Package, NamedElement, types_PackageMember, types_Type, PackageMember, types_TypeConstraint, types_Feature, TypedElement, types_ComplexType, types_Operation, Feature, types_Parameter, types_Event, types_EnumerationType, PrimitiveType, types_Enumerator, types_PrimitiveType, Type, ParameterizedType, types_TypeParameter, types_ParameterizedType, types_RangeConstraint, TypeConstraint, types_Property, types_TypedElement, types_Integer, types_Real, types_Boolean, types_String, types_Void},
    associations={member0, constraints1, owningType2, parameters3, enumerator10, baseType12, features13, superTypes15, owningEnumeration16, bound17, parameter19, owningOperation4, type5, typeArguments7},
    generalizations={gen_types_Package_NamedElement, gen_types_Type_PackageMember, gen_types_Feature_TypedElement, gen_types_Feature_NamedElement, gen_types_Operation_Feature, gen_types_Event_Feature, gen_types_EnumerationType_PrimitiveType, gen_types_PrimitiveType_Type, gen_types_ComplexType_ParameterizedType, gen_types_Enumerator_NamedElement, gen_types_TypeParameter_Type, gen_types_ParameterizedType_Type, gen_types_PackageMember_NamedElement, gen_types_RangeConstraint_TypeConstraint, gen_types_Property_Feature, gen_types_Parameter_TypedElement, gen_types_Parameter_NamedElement, gen_types_Integer_PrimitiveType, gen_types_Real_PrimitiveType, gen_types_Boolean_PrimitiveType, gen_types_String_PrimitiveType, gen_types_Void_PrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)