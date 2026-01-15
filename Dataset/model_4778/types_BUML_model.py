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
types_Declaration = Class(name="types::Declaration", is_abstract=True)
types_Type = Class(name="types::Type")
types_TypeSpecifier = Class(name="types::TypeSpecifier")
NamedElement = Class(name="NamedElement")
AnnotatableElement = Class(name="AnnotatableElement")
MetaComposite = Class(name="MetaComposite")
types_Operation = Class(name="types::Operation")
TypedDeclaration = Class(name="TypedDeclaration")
GenericElement = Class(name="GenericElement")
types_Parameter = Class(name="types::Parameter")
types_Property = Class(name="types::Property")
types_Expression = Class(name="types::Expression", is_abstract=True)
TypedElement = Class(name="TypedElement")
types_Package = Class(name="types::Package")
Declaration = Class(name="Declaration")
DomainElement = Class(name="DomainElement")
types_Event = Class(name="types::Event")
types_EnumerationType = Class(name="types::EnumerationType")
ComplexType = Class(name="ComplexType")
types_Enumerator = Class(name="types::Enumerator")
types_PrimitiveType = Class(name="types::PrimitiveType")
Type = Class(name="Type")
types_ComplexType = Class(name="types::ComplexType")
types_TypeParameter = Class(name="types::TypeParameter")
types_GenericElement = Class(name="types::GenericElement")
types_Domain = Class(name="types::Domain")
types_TypeAlias = Class(name="types::TypeAlias")
types_TypedElement = Class(name="types::TypedElement", is_abstract=True)
types_ArrayTypeSpecifier = Class(name="types::ArrayTypeSpecifier")
TypeSpecifier = Class(name="TypeSpecifier")
types_EObject = Class(name="types::EObject")
types_TypedDeclaration = Class(name="types::TypedDeclaration")
types_MetaComposite = Class(name="types::MetaComposite")
types_Annotation = Class(name="types::Annotation")
types_AnnotationType = Class(name="types::AnnotationType")
types_AnnotatableElement = Class(name="types::AnnotatableElement")

# types_Declaration class attributes and methods
types_Declaration_static: Property = Property(name="static", type=BooleanType)
types_Declaration_id: Property = Property(name="id", type=StringType)
types_Declaration.attributes={types_Declaration_id, types_Declaration_static}

# types_Type class attributes and methods
types_Type_abstract: Property = Property(name="abstract", type=BooleanType)
types_Type_visible: Property = Property(name="visible", type=BooleanType)
types_Type_m_getOriginType: Method = Method(name="getOriginType", parameters={}, type=StringType)
types_Type.attributes={types_Type_abstract, types_Type_visible}
types_Type.methods={types_Type_m_getOriginType}

# types_TypeSpecifier class attributes and methods

# NamedElement class attributes and methods

# AnnotatableElement class attributes and methods

# MetaComposite class attributes and methods

# types_Operation class attributes and methods
types_Operation_variadic: Property = Property(name="variadic", type=BooleanType)
types_Operation_m_getVarArgIndex: Method = Method(name="getVarArgIndex", parameters={}, type=IntegerType)
types_Operation.attributes={types_Operation_variadic}
types_Operation.methods={types_Operation_m_getVarArgIndex}

# TypedDeclaration class attributes and methods

# GenericElement class attributes and methods

# types_Parameter class attributes and methods
types_Parameter_varArgs: Property = Property(name="varArgs", type=BooleanType)
types_Parameter_optional: Property = Property(name="optional", type=BooleanType)
types_Parameter.attributes={types_Parameter_varArgs, types_Parameter_optional}

# types_Property class attributes and methods
types_Property_const: Property = Property(name="const", type=BooleanType)
types_Property_readonly: Property = Property(name="readonly", type=BooleanType)
types_Property.attributes={types_Property_readonly, types_Property_const}

# types_Expression class attributes and methods

# TypedElement class attributes and methods

# types_Package class attributes and methods

# Declaration class attributes and methods

# DomainElement class attributes and methods

# types_Event class attributes and methods
types_Event_direction: Property = Property(name="direction", type=StringType)
types_Event.attributes={types_Event_direction}

# types_EnumerationType class attributes and methods

# ComplexType class attributes and methods

# types_Enumerator class attributes and methods
types_Enumerator_literalValue: Property = Property(name="literalValue", type=IntegerType)
types_Enumerator.attributes={types_Enumerator_literalValue}

# types_PrimitiveType class attributes and methods

# Type class attributes and methods

# types_ComplexType class attributes and methods
types_ComplexType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={}, type=Declaration)
types_ComplexType.methods={types_ComplexType_m_getAllFeatures}

# types_TypeParameter class attributes and methods

# types_GenericElement class attributes and methods

# types_Domain class attributes and methods
types_Domain_domainID: Property = Property(name="domainID", type=StringType)
types_Domain.attributes={types_Domain_domainID}

# types_TypeAlias class attributes and methods

# types_TypedElement class attributes and methods

# types_ArrayTypeSpecifier class attributes and methods
types_ArrayTypeSpecifier_size: Property = Property(name="size", type=IntegerType)
types_ArrayTypeSpecifier_m_getElementType: Method = Method(name="getElementType", parameters={}, type=Type)
types_ArrayTypeSpecifier.attributes={types_ArrayTypeSpecifier_size}
types_ArrayTypeSpecifier.methods={types_ArrayTypeSpecifier_m_getElementType}

# TypeSpecifier class attributes and methods

# types_EObject class attributes and methods

# types_TypedDeclaration class attributes and methods

# types_MetaComposite class attributes and methods

# types_Annotation class attributes and methods

# types_AnnotationType class attributes and methods

# types_AnnotatableElement class attributes and methods
types_AnnotatableElement_m_getAnnotationOfType: Method = Method(name="getAnnotationOfType", parameters={Parameter(name='typeName')}, type=StringType)
types_AnnotatableElement.methods={types_AnnotatableElement_m_getAnnotationOfType}

# Relationships
member0: BinaryAssociation = BinaryAssociation(
    name="member0",
    ends={
        Property(name="types_Declaration", type=types_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Package", type=types_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import2: BinaryAssociation = BinaryAssociation(
    name="import2",
    ends={
        Property(name="types_Package3", type=types_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Package1", type=types_Package, multiplicity=Multiplicity(0, 9999))
    }
)
superTypes4: BinaryAssociation = BinaryAssociation(
    name="superTypes4",
    ends={
        Property(name="types_TypeSpecifier", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Type", type=types_TypeSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters5: BinaryAssociation = BinaryAssociation(
    name="parameters5",
    ends={
        Property(name="Parameter", type=types_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=types_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue6: BinaryAssociation = BinaryAssociation(
    name="initialValue6",
    ends={
        Property(name="types_Expression", type=types_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Property", type=types_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningOperation7: BinaryAssociation = BinaryAssociation(
    name="owningOperation7",
    ends={
        Property(name="Operation", type=types_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=types_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="types_TypeSpecifier14", type=types_Type, multiplicity=Multiplicity(0, 1)),
        Property(name="types_Type15", type=types_TypeSpecifier, multiplicity=Multiplicity(1, 1))
    }
)
typeArguments17: BinaryAssociation = BinaryAssociation(
    name="typeArguments17",
    ends={
        Property(name="types_TypeSpecifier18", type=types_TypeSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeSpecifier16", type=types_TypeSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerator19: BinaryAssociation = BinaryAssociation(
    name="enumerator19",
    ends={
        Property(name="Enumerator", type=types_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningEnumeration", type=types_Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features20: BinaryAssociation = BinaryAssociation(
    name="features20",
    ends={
        Property(name="types_Declaration21", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ComplexType", type=types_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningEnumeration22: BinaryAssociation = BinaryAssociation(
    name="owningEnumeration22",
    ends={
        Property(name="EnumerationType", type=types_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="enumerator", type=types_EnumerationType, multiplicity=Multiplicity(0, 1))
    }
)
bound23: BinaryAssociation = BinaryAssociation(
    name="bound23",
    ends={
        Property(name="types_Type24", type=types_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeParameter", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
typeParameters25: BinaryAssociation = BinaryAssociation(
    name="typeParameters25",
    ends={
        Property(name="types_TypeParameter26", type=types_GenericElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_GenericElement", type=types_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="types_Type9", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement", type=types_Type, multiplicity=Multiplicity(0, 1))
    }
)
typeSpecifier10: BinaryAssociation = BinaryAssociation(
    name="typeSpecifier10",
    ends={
        Property(name="types_TypeSpecifier12", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement11", type=types_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations31: BinaryAssociation = BinaryAssociation(
    name="annotations31",
    ends={
        Property(name="types_Annotation32", type=types_AnnotatableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_AnnotatableElement", type=types_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationInfo34: BinaryAssociation = BinaryAssociation(
    name="annotationInfo34",
    ends={
        Property(name="types_AnnotatableElement35", type=types_AnnotatableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_AnnotatableElement33", type=types_AnnotatableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties36: BinaryAssociation = BinaryAssociation(
    name="properties36",
    ends={
        Property(name="types_Property38", type=types_AnnotationType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_AnnotationType37", type=types_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targets39: BinaryAssociation = BinaryAssociation(
    name="targets39",
    ends={
        Property(name="types_EObject", type=types_AnnotationType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_AnnotationType40", type=types_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
metaFeatures41: BinaryAssociation = BinaryAssociation(
    name="metaFeatures41",
    ends={
        Property(name="types_Declaration42", type=types_MetaComposite, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MetaComposite", type=types_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="types_AnnotationType", type=types_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Annotation", type=types_AnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
arguments28: BinaryAssociation = BinaryAssociation(
    name="arguments28",
    ends={
        Property(name="types_Expression30", type=types_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Annotation29", type=types_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_types_Type_Declaration = Generalization(general=Declaration, specific=types_Type)
gen_types_Declaration_NamedElement = Generalization(general=NamedElement, specific=types_Declaration)
gen_types_Declaration_AnnotatableElement = Generalization(general=AnnotatableElement, specific=types_Declaration)
gen_types_Declaration_MetaComposite = Generalization(general=MetaComposite, specific=types_Declaration)
gen_types_Operation_TypedDeclaration = Generalization(general=TypedDeclaration, specific=types_Operation)
gen_types_Operation_GenericElement = Generalization(general=GenericElement, specific=types_Operation)
gen_types_Property_TypedDeclaration = Generalization(general=TypedDeclaration, specific=types_Property)
gen_types_Parameter_TypedElement = Generalization(general=TypedElement, specific=types_Parameter)
gen_types_Parameter_NamedElement = Generalization(general=NamedElement, specific=types_Parameter)
gen_types_Parameter_AnnotatableElement = Generalization(general=AnnotatableElement, specific=types_Parameter)
gen_types_Package_Declaration = Generalization(general=Declaration, specific=types_Package)
gen_types_Package_DomainElement = Generalization(general=DomainElement, specific=types_Package)
gen_types_Event_TypedDeclaration = Generalization(general=TypedDeclaration, specific=types_Event)
gen_types_EnumerationType_ComplexType = Generalization(general=ComplexType, specific=types_EnumerationType)
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_ComplexType_Type = Generalization(general=Type, specific=types_ComplexType)
gen_types_ComplexType_GenericElement = Generalization(general=GenericElement, specific=types_ComplexType)
gen_types_Enumerator_TypedDeclaration = Generalization(general=TypedDeclaration, specific=types_Enumerator)
gen_types_TypeParameter_Type = Generalization(general=Type, specific=types_TypeParameter)
gen_types_GenericElement_NamedElement = Generalization(general=NamedElement, specific=types_GenericElement)
gen_types_TypeAlias_TypedDeclaration = Generalization(general=TypedDeclaration, specific=types_TypeAlias)
gen_types_TypeAlias_Type = Generalization(general=Type, specific=types_TypeAlias)
gen_types_ArrayTypeSpecifier_TypeSpecifier = Generalization(general=TypeSpecifier, specific=types_ArrayTypeSpecifier)
gen_types_AnnotationType_Type = Generalization(general=Type, specific=types_AnnotationType)
gen_types_TypedDeclaration_Declaration = Generalization(general=Declaration, specific=types_TypedDeclaration)
gen_types_TypedDeclaration_TypedElement = Generalization(general=TypedElement, specific=types_TypedDeclaration)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Declaration, types_Type, types_TypeSpecifier, NamedElement, AnnotatableElement, MetaComposite, types_Operation, TypedDeclaration, GenericElement, types_Parameter, types_Property, types_Expression, TypedElement, types_Package, Declaration, DomainElement, types_Event, types_EnumerationType, ComplexType, types_Enumerator, types_PrimitiveType, Type, types_ComplexType, types_TypeParameter, types_GenericElement, types_Domain, types_TypeAlias, types_TypedElement, types_ArrayTypeSpecifier, TypeSpecifier, types_EObject, types_TypedDeclaration, types_MetaComposite, types_Annotation, types_AnnotationType, types_AnnotatableElement, Direction},
    associations={member0, import2, superTypes4, parameters5, initialValue6, owningOperation7, type13, typeArguments17, enumerator19, features20, owningEnumeration22, bound23, typeParameters25, type8, typeSpecifier10, annotations31, annotationInfo34, properties36, targets39, metaFeatures41, type27, arguments28},
    generalizations={gen_types_Type_Declaration, gen_types_Declaration_NamedElement, gen_types_Declaration_AnnotatableElement, gen_types_Declaration_MetaComposite, gen_types_Operation_TypedDeclaration, gen_types_Operation_GenericElement, gen_types_Property_TypedDeclaration, gen_types_Parameter_TypedElement, gen_types_Parameter_NamedElement, gen_types_Parameter_AnnotatableElement, gen_types_Package_Declaration, gen_types_Package_DomainElement, gen_types_Event_TypedDeclaration, gen_types_EnumerationType_ComplexType, gen_types_PrimitiveType_Type, gen_types_ComplexType_Type, gen_types_ComplexType_GenericElement, gen_types_Enumerator_TypedDeclaration, gen_types_TypeParameter_Type, gen_types_GenericElement_NamedElement, gen_types_TypeAlias_TypedDeclaration, gen_types_TypeAlias_Type, gen_types_ArrayTypeSpecifier_TypeSpecifier, gen_types_AnnotationType_Type, gen_types_TypedDeclaration_Declaration, gen_types_TypedDeclaration_TypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)