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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="LOCAL"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT")
    }
)

# Classes
types_Package = Class(name="types::Package")
NamedElement = Class(name="NamedElement")
types_PackageMember = Class(name="types::PackageMember")
types_Domain = Class(name="types::Domain")
types_Type = Class(name="types::Type", is_abstract=True)
PackageMember = Class(name="PackageMember")
types_TypeConstraint = Class(name="types::TypeConstraint")
types_Declaration = Class(name="types::Declaration", is_abstract=True)
TypedElement = Class(name="TypedElement")
types_Operation = Class(name="types::Operation")
Declaration = Class(name="Declaration")
types_Parameter = Class(name="types::Parameter")
types_TypedElement = Class(name="types::TypedElement", is_abstract=True)
types_Event = Class(name="types::Event")
types_EnumerationType = Class(name="types::EnumerationType")
PrimitiveType = Class(name="PrimitiveType")
types_Enumerator = Class(name="types::Enumerator")
types_PrimitiveType = Class(name="types::PrimitiveType")
Type = Class(name="Type")
types_ComplexType = Class(name="types::ComplexType")
ParameterizedType = Class(name="ParameterizedType")
types_Property = Class(name="types::Property")
types_TypeParameter = Class(name="types::TypeParameter")
types_ParameterizedType = Class(name="types::ParameterizedType")
types_RangeConstraint = Class(name="types::RangeConstraint")
TypeConstraint = Class(name="TypeConstraint")
types_TypeAlias = Class(name="types::TypeAlias")

# types_Package class attributes and methods

# NamedElement class attributes and methods

# types_PackageMember class attributes and methods

# types_Domain class attributes and methods
types_Domain_domainID: Property = Property(name="domainID", type=StringType)
types_Domain.attributes={types_Domain_domainID}

# types_Type class attributes and methods
types_Type_abstract: Property = Property(name="abstract", type=BooleanType)
types_Type_m_getOriginType: Method = Method(name="getOriginType", parameters={}, type=StringType)
types_Type.attributes={types_Type_abstract}
types_Type.methods={types_Type_m_getOriginType}

# PackageMember class attributes and methods

# types_TypeConstraint class attributes and methods
types_TypeConstraint_value: Property = Property(name="value", type=StringType)
types_TypeConstraint.attributes={types_TypeConstraint_value}

# types_Declaration class attributes and methods

# TypedElement class attributes and methods

# types_Operation class attributes and methods

# Declaration class attributes and methods

# types_Parameter class attributes and methods

# types_TypedElement class attributes and methods

# types_Event class attributes and methods
types_Event_direction: Property = Property(name="direction", type=StringType)
types_Event.attributes={types_Event_direction}

# types_EnumerationType class attributes and methods

# PrimitiveType class attributes and methods

# types_Enumerator class attributes and methods
types_Enumerator_literalValue: Property = Property(name="literalValue", type=StringType)
types_Enumerator.attributes={types_Enumerator_literalValue}

# types_PrimitiveType class attributes and methods

# Type class attributes and methods

# types_ComplexType class attributes and methods
types_ComplexType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={}, type=Declaration)
types_ComplexType.methods={types_ComplexType_m_getAllFeatures}

# ParameterizedType class attributes and methods

# types_Property class attributes and methods
types_Property_external: Property = Property(name="external", type=BooleanType)
types_Property_const: Property = Property(name="const", type=BooleanType)
types_Property_readonly: Property = Property(name="readonly", type=BooleanType)
types_Property.attributes={types_Property_readonly, types_Property_external, types_Property_const}

# types_TypeParameter class attributes and methods

# types_ParameterizedType class attributes and methods

# types_RangeConstraint class attributes and methods
types_RangeConstraint_lowerBound: Property = Property(name="lowerBound", type=StringType)
types_RangeConstraint_upperBound: Property = Property(name="upperBound", type=StringType)
types_RangeConstraint.attributes={types_RangeConstraint_upperBound, types_RangeConstraint_lowerBound}

# TypeConstraint class attributes and methods

# types_TypeAlias class attributes and methods

# Relationships
member0: BinaryAssociation = BinaryAssociation(
    name="member0",
    ends={
        Property(name="types_PackageMember", type=types_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Package", type=types_PackageMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain1: BinaryAssociation = BinaryAssociation(
    name="domain1",
    ends={
        Property(name="types_Domain", type=types_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Package2", type=types_Domain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint3: BinaryAssociation = BinaryAssociation(
    name="constraint3",
    ends={
        Property(name="types_TypeConstraint", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Type", type=types_TypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningOperation5: BinaryAssociation = BinaryAssociation(
    name="owningOperation5",
    ends={
        Property(name="Operation", type=types_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=types_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="types_Type7", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
typeArguments8: BinaryAssociation = BinaryAssociation(
    name="typeArguments8",
    ends={
        Property(name="types_Type10", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement9", type=types_Type, multiplicity=Multiplicity(0, 9999))
    }
)
enumerator11: BinaryAssociation = BinaryAssociation(
    name="enumerator11",
    ends={
        Property(name="Enumerator", type=types_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningEnumeration", type=types_Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType13: BinaryAssociation = BinaryAssociation(
    name="baseType13",
    ends={
        Property(name="types_PrimitiveType", type=types_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_PrimitiveType12", type=types_PrimitiveType, multiplicity=Multiplicity(0, 1))
    }
)
features14: BinaryAssociation = BinaryAssociation(
    name="features14",
    ends={
        Property(name="types_Declaration", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ComplexType", type=types_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes16: BinaryAssociation = BinaryAssociation(
    name="superTypes16",
    ends={
        Property(name="types_ComplexType17", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ComplexType15", type=types_ComplexType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="Parameter", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=types_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound19: BinaryAssociation = BinaryAssociation(
    name="bound19",
    ends={
        Property(name="types_Type20", type=types_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeParameter", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameter21: BinaryAssociation = BinaryAssociation(
    name="parameter21",
    ends={
        Property(name="types_TypeParameter22", type=types_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ParameterizedType", type=types_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningEnumeration18: BinaryAssociation = BinaryAssociation(
    name="owningEnumeration18",
    ends={
        Property(name="EnumerationType", type=types_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="enumerator", type=types_EnumerationType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_types_Package_NamedElement = Generalization(general=NamedElement, specific=types_Package)
gen_types_Type_PackageMember = Generalization(general=PackageMember, specific=types_Type)
gen_types_Declaration_TypedElement = Generalization(general=TypedElement, specific=types_Declaration)
gen_types_Declaration_NamedElement = Generalization(general=NamedElement, specific=types_Declaration)
gen_types_Operation_Declaration = Generalization(general=Declaration, specific=types_Operation)
gen_types_Operation_PackageMember = Generalization(general=PackageMember, specific=types_Operation)
gen_types_Parameter_TypedElement = Generalization(general=TypedElement, specific=types_Parameter)
gen_types_Parameter_NamedElement = Generalization(general=NamedElement, specific=types_Parameter)
gen_types_Event_Declaration = Generalization(general=Declaration, specific=types_Event)
gen_types_EnumerationType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_EnumerationType)
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_ComplexType_ParameterizedType = Generalization(general=ParameterizedType, specific=types_ComplexType)
gen_types_Property_Declaration = Generalization(general=Declaration, specific=types_Property)
gen_types_TypeParameter_Type = Generalization(general=Type, specific=types_TypeParameter)
gen_types_ParameterizedType_Type = Generalization(general=Type, specific=types_ParameterizedType)
gen_types_PackageMember_NamedElement = Generalization(general=NamedElement, specific=types_PackageMember)
gen_types_RangeConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=types_RangeConstraint)
gen_types_TypeAlias_TypedElement = Generalization(general=TypedElement, specific=types_TypeAlias)
gen_types_TypeAlias_Type = Generalization(general=Type, specific=types_TypeAlias)
gen_types_Enumerator_NamedElement = Generalization(general=NamedElement, specific=types_Enumerator)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Package, NamedElement, types_PackageMember, types_Domain, types_Type, PackageMember, types_TypeConstraint, types_Declaration, TypedElement, types_Operation, Declaration, types_Parameter, types_TypedElement, types_Event, types_EnumerationType, PrimitiveType, types_Enumerator, types_PrimitiveType, Type, types_ComplexType, ParameterizedType, types_Property, types_TypeParameter, types_ParameterizedType, types_RangeConstraint, TypeConstraint, types_TypeAlias, Direction},
    associations={member0, domain1, constraint3, owningOperation5, type6, typeArguments8, enumerator11, baseType13, features14, superTypes16, parameters4, bound19, parameter21, owningEnumeration18},
    generalizations={gen_types_Package_NamedElement, gen_types_Type_PackageMember, gen_types_Declaration_TypedElement, gen_types_Declaration_NamedElement, gen_types_Operation_Declaration, gen_types_Operation_PackageMember, gen_types_Parameter_TypedElement, gen_types_Parameter_NamedElement, gen_types_Event_Declaration, gen_types_EnumerationType_PrimitiveType, gen_types_PrimitiveType_Type, gen_types_ComplexType_ParameterizedType, gen_types_Property_Declaration, gen_types_TypeParameter_Type, gen_types_ParameterizedType_Type, gen_types_PackageMember_NamedElement, gen_types_RangeConstraint_TypeConstraint, gen_types_TypeAlias_TypedElement, gen_types_TypeAlias_Type, gen_types_Enumerator_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)