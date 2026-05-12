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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

ConnectorKind: Enumeration = Enumeration(
    name="ConnectorKind",
    literals={
            EnumerationLiteral(name="assembly"),
			EnumerationLiteral(name="delegation")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint")
    }
)

CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="guarded"),
			EnumerationLiteral(name="concurrent")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return_")
    }
)

ParameterEffectKind: Enumeration = Enumeration(
    name="ParameterEffectKind",
    literals={
            EnumerationLiteral(name="create"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
    }
)

ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered")
    }
)

MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="complete"),
			EnumerationLiteral(name="lost"),
			EnumerationLiteral(name="found"),
			EnumerationLiteral(name="unknown")
    }
)

MessageSort: Enumeration = Enumeration(
    name="MessageSort",
    literals={
            EnumerationLiteral(name="reply"),
			EnumerationLiteral(name="synchCall"),
			EnumerationLiteral(name="asynchCall"),
			EnumerationLiteral(name="asynchSignal"),
			EnumerationLiteral(name="createMessage"),
			EnumerationLiteral(name="deleteMessage")
    }
)

InteractionOperatorKind: Enumeration = Enumeration(
    name="InteractionOperatorKind",
    literals={
            EnumerationLiteral(name="opt"),
			EnumerationLiteral(name="break_"),
			EnumerationLiteral(name="seq"),
			EnumerationLiteral(name="alt"),
			EnumerationLiteral(name="par"),
			EnumerationLiteral(name="strict"),
			EnumerationLiteral(name="loop"),
			EnumerationLiteral(name="critical"),
			EnumerationLiteral(name="neg"),
			EnumerationLiteral(name="assert_"),
			EnumerationLiteral(name="ignore"),
			EnumerationLiteral(name="consider")
    }
)

ExpansionKind: Enumeration = Enumeration(
    name="ExpansionKind",
    literals={
            EnumerationLiteral(name="stream"),
			EnumerationLiteral(name="parallel"),
			EnumerationLiteral(name="iterative")
    }
)

# Classes
umluseCases_Element = Class(name="umluseCases_Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
umluseCases_PackageableElement = Class(name="umluseCases_PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
ParameterableElement = Class(name="ParameterableElement")
umluseCases_NamedElement = Class(name="umluseCases_NamedElement", is_abstract=True)
Element = Class(name="Element")
umluseCases_Namespace = Class(name="umluseCases_Namespace", is_abstract=True)
umluseCases_DirectedRelationship = Class(name="umluseCases_DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
umluseCases_Relationship = Class(name="umluseCases_Relationship", is_abstract=True)
umluseCases_Type = Class(name="umluseCases_Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
umluseCases_Classifier = Class(name="umluseCases_Classifier", is_abstract=True)
Namespace = Class(name="Namespace")
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
TemplateableElement = Class(name="TemplateableElement")
umluseCases_UseCase = Class(name="umluseCases_UseCase")
umluseCases_RedefinableElement = Class(name="umluseCases_RedefinableElement", is_abstract=True)
umluseCases_TemplateableElement = Class(name="umluseCases_TemplateableElement", is_abstract=True)
umluseCases_ParameterableElement = Class(name="umluseCases_ParameterableElement", is_abstract=True)
umluseCases_BehavioredClassifier = Class(name="umluseCases_BehavioredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
umluseCases_Include = Class(name="umluseCases_Include")
umluseCases_Extend = Class(name="umluseCases_Extend")
umluseCases_ExtensionPoint = Class(name="umluseCases_ExtensionPoint")
DirectedRelationship = Class(name="DirectedRelationship")
umluseCases_Actor = Class(name="umluseCases_Actor")

# umluseCases_Element class attributes and methods

# EModelElement class attributes and methods

# umluseCases_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# ParameterableElement class attributes and methods

# umluseCases_NamedElement class attributes and methods
umluseCases_NamedElement_name: Property = Property(name="name", type=StringType)
umluseCases_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
umluseCases_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
umluseCases_NamedElement.attributes={umluseCases_NamedElement_qualifiedName, umluseCases_NamedElement_name, umluseCases_NamedElement_visibility}

# Element class attributes and methods

# umluseCases_Namespace class attributes and methods

# umluseCases_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# umluseCases_Relationship class attributes and methods

# umluseCases_Type class attributes and methods

# PackageableElement class attributes and methods

# umluseCases_Classifier class attributes and methods
umluseCases_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
umluseCases_Classifier.attributes={umluseCases_Classifier_isAbstract}

# Namespace class attributes and methods

# RedefinableElement class attributes and methods

# Type class attributes and methods

# TemplateableElement class attributes and methods

# umluseCases_UseCase class attributes and methods
umluseCases_UseCase_m_must_have_name: Method = Method(name="must_have_name", parameters={Parameter(name='umluseCases_diagnostics', type=StringType), Parameter(name='umluseCases_context', type=StringType)}, type=BooleanType)
umluseCases_UseCase_m_allIncludedUseCases: Method = Method(name="allIncludedUseCases", parameters={}, type=StringType)
umluseCases_UseCase_m_binary_associations: Method = Method(name="binary_associations", parameters={Parameter(name='umluseCases_diagnostics', type=StringType), Parameter(name='umluseCases_context', type=StringType)}, type=BooleanType)
umluseCases_UseCase_m_no_association_to_use_case: Method = Method(name="no_association_to_use_case", parameters={Parameter(name='umluseCases_context', type=StringType), Parameter(name='umluseCases_diagnostics', type=StringType)}, type=BooleanType)
umluseCases_UseCase_m_cannot_include_self: Method = Method(name="cannot_include_self", parameters={Parameter(name='umluseCases_diagnostics', type=StringType), Parameter(name='umluseCases_context', type=StringType)}, type=BooleanType)
umluseCases_UseCase.methods={umluseCases_UseCase_m_no_association_to_use_case, umluseCases_UseCase_m_cannot_include_self, umluseCases_UseCase_m_binary_associations, umluseCases_UseCase_m_allIncludedUseCases, umluseCases_UseCase_m_must_have_name}

# umluseCases_RedefinableElement class attributes and methods
umluseCases_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
umluseCases_RedefinableElement.attributes={umluseCases_RedefinableElement_isLeaf}

# umluseCases_TemplateableElement class attributes and methods

# umluseCases_ParameterableElement class attributes and methods

# umluseCases_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# BehavioredClassifier class attributes and methods

# umluseCases_Include class attributes and methods

# umluseCases_Extend class attributes and methods
umluseCases_Extend_m_extension_points: Method = Method(name="extension_points", parameters={Parameter(name='umluseCases_context', type=StringType), Parameter(name='umluseCases_diagnostics', type=StringType)}, type=BooleanType)
umluseCases_Extend.methods={umluseCases_Extend_m_extension_points}

# umluseCases_ExtensionPoint class attributes and methods
umluseCases_ExtensionPoint_m_must_have_name: Method = Method(name="must_have_name", parameters={Parameter(name='umluseCases_context', type=StringType), Parameter(name='umluseCases_diagnostics', type=StringType)}, type=BooleanType)
umluseCases_ExtensionPoint.methods={umluseCases_ExtensionPoint_m_must_have_name}

# DirectedRelationship class attributes and methods

# umluseCases_Actor class attributes and methods
umluseCases_Actor_m_associations: Method = Method(name="associations", parameters={Parameter(name='umluseCases_context', type=StringType), Parameter(name='umluseCases_diagnostics', type=StringType)}, type=BooleanType)
umluseCases_Actor_m_must_have_name: Method = Method(name="must_have_name", parameters={Parameter(name='umluseCases_context', type=StringType), Parameter(name='umluseCases_diagnostics', type=StringType)}, type=BooleanType)
umluseCases_Actor.methods={umluseCases_Actor_m_must_have_name, umluseCases_Actor_m_associations}

# Relationships
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="Element", type=umluseCases_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=umluseCases_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Element4", type=umluseCases_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=umluseCases_Element, multiplicity=Multiplicity(0, 1))
    }
)
namespace5: BinaryAssociation = BinaryAssociation(
    name="namespace5",
    ends={
        Property(name="Namespace", type=umluseCases_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=umluseCases_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="umluseCases_Element", type=umluseCases_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_DirectedRelationship", type=umluseCases_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="umluseCases_Element9", type=umluseCases_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_DirectedRelationship8", type=umluseCases_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement10: BinaryAssociation = BinaryAssociation(
    name="relatedElement10",
    ends={
        Property(name="umluseCases_Element11", type=umluseCases_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Relationship", type=umluseCases_Element, multiplicity=Multiplicity(1, 9999))
    }
)
member12: BinaryAssociation = BinaryAssociation(
    name="member12",
    ends={
        Property(name="umluseCases_NamedElement", type=umluseCases_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Namespace", type=umluseCases_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember15: BinaryAssociation = BinaryAssociation(
    name="ownedMember15",
    ends={
        Property(name="NamedElement", type=umluseCases_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=umluseCases_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember13: BinaryAssociation = BinaryAssociation(
    name="importedMember13",
    ends={
        Property(name="umluseCases_PackageableElement", type=umluseCases_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Namespace14", type=umluseCases_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember16: BinaryAssociation = BinaryAssociation(
    name="inheritedMember16",
    ends={
        Property(name="umluseCases_NamedElement17", type=umluseCases_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Classifier", type=umluseCases_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier19: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier19",
    ends={
        Property(name="umluseCases_Classifier20", type=umluseCases_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Classifier18", type=umluseCases_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general22: BinaryAssociation = BinaryAssociation(
    name="general22",
    ends={
        Property(name="umluseCases_Classifier23", type=umluseCases_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Classifier21", type=umluseCases_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUseCase24: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase24",
    ends={
        Property(name="umluseCases_UseCase", type=umluseCases_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Classifier25", type=umluseCases_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCase26: BinaryAssociation = BinaryAssociation(
    name="useCase26",
    ends={
        Property(name="UseCase", type=umluseCases_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=umluseCases_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext29: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext29",
    ends={
        Property(name="umluseCases_Classifier31", type=umluseCases_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_RedefinableElement30", type=umluseCases_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement28: BinaryAssociation = BinaryAssociation(
    name="redefinedElement28",
    ends={
        Property(name="umluseCases_RedefinableElement", type=umluseCases_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_RedefinableElement27", type=umluseCases_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
include32: BinaryAssociation = BinaryAssociation(
    name="include32",
    ends={
        Property(name="Include", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="includingCase", type=umluseCases_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend33: BinaryAssociation = BinaryAssociation(
    name="extend33",
    ends={
        Property(name="Extend", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=umluseCases_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint34: BinaryAssociation = BinaryAssociation(
    name="extensionPoint34",
    ends={
        Property(name="ExtensionPoint", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=umluseCases_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject35: BinaryAssociation = BinaryAssociation(
    name="subject35",
    ends={
        Property(name="Classifier", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase36", type=umluseCases_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
addition37: BinaryAssociation = BinaryAssociation(
    name="addition37",
    ends={
        Property(name="umluseCases_UseCase38", type=umluseCases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Include", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extension45: BinaryAssociation = BinaryAssociation(
    name="extension45",
    ends={
        Property(name="UseCase46", type=umluseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase39: BinaryAssociation = BinaryAssociation(
    name="includingCase39",
    ends={
        Property(name="UseCase40", type=umluseCases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extendedCase41: BinaryAssociation = BinaryAssociation(
    name="extendedCase41",
    ends={
        Property(name="umluseCases_UseCase42", type=umluseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Extend", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extensionLocation43: BinaryAssociation = BinaryAssociation(
    name="extensionLocation43",
    ends={
        Property(name="umluseCases_ExtensionPoint", type=umluseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="umluseCases_Extend44", type=umluseCases_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
useCase47: BinaryAssociation = BinaryAssociation(
    name="useCase47",
    ends={
        Property(name="UseCase48", type=umluseCases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=umluseCases_UseCase, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umluseCases_Element_EModelElement = Generalization(general=EModelElement, specific=umluseCases_Element)
gen_umluseCases_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=umluseCases_PackageableElement)
gen_umluseCases_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=umluseCases_PackageableElement)
gen_umluseCases_NamedElement_Element = Generalization(general=Element, specific=umluseCases_NamedElement)
gen_umluseCases_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=umluseCases_DirectedRelationship)
gen_umluseCases_Relationship_Element = Generalization(general=Element, specific=umluseCases_Relationship)
gen_umluseCases_Namespace_NamedElement = Generalization(general=NamedElement, specific=umluseCases_Namespace)
gen_umluseCases_Type_PackageableElement = Generalization(general=PackageableElement, specific=umluseCases_Type)
gen_umluseCases_Classifier_Namespace = Generalization(general=Namespace, specific=umluseCases_Classifier)
gen_umluseCases_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=umluseCases_Classifier)
gen_umluseCases_Classifier_Type = Generalization(general=Type, specific=umluseCases_Classifier)
gen_umluseCases_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=umluseCases_Classifier)
gen_umluseCases_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=umluseCases_RedefinableElement)
gen_umluseCases_TemplateableElement_Element = Generalization(general=Element, specific=umluseCases_TemplateableElement)
gen_umluseCases_ParameterableElement_Element = Generalization(general=Element, specific=umluseCases_ParameterableElement)
gen_umluseCases_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=umluseCases_BehavioredClassifier)
gen_umluseCases_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=umluseCases_UseCase)
gen_umluseCases_Include_NamedElement = Generalization(general=NamedElement, specific=umluseCases_Include)
gen_umluseCases_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=umluseCases_Include)
gen_umluseCases_Extend_NamedElement = Generalization(general=NamedElement, specific=umluseCases_Extend)
gen_umluseCases_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=umluseCases_Extend)
gen_umluseCases_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=umluseCases_ExtensionPoint)
gen_umluseCases_Actor_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=umluseCases_Actor)

# Domain Model
domain_model = DomainModel(
    name="umluseCases",
    types={umluseCases_Element, EModelElement, umluseCases_PackageableElement, NamedElement, ParameterableElement, umluseCases_NamedElement, Element, umluseCases_Namespace, umluseCases_DirectedRelationship, Relationship, umluseCases_Relationship, umluseCases_Type, PackageableElement, umluseCases_Classifier, Namespace, RedefinableElement, Type, TemplateableElement, umluseCases_UseCase, umluseCases_RedefinableElement, umluseCases_TemplateableElement, umluseCases_ParameterableElement, umluseCases_BehavioredClassifier, Classifier, BehavioredClassifier, umluseCases_Include, umluseCases_Extend, umluseCases_ExtensionPoint, DirectedRelationship, umluseCases_Actor, VisibilityKind, TransitionKind, ConnectorKind, PseudostateKind, CallConcurrencyKind, AggregationKind, ParameterDirectionKind, ParameterEffectKind, ObjectNodeOrderingKind, MessageKind, MessageSort, InteractionOperatorKind, ExpansionKind},
    associations={ownedElement1, owner3, namespace5, source6, target7, relatedElement10, member12, ownedMember15, importedMember13, inheritedMember16, redefinedClassifier19, general22, ownedUseCase24, useCase26, redefinitionContext29, redefinedElement28, include32, extend33, extensionPoint34, subject35, addition37, extension45, includingCase39, extendedCase41, extensionLocation43, useCase47},
    generalizations={gen_umluseCases_Element_EModelElement, gen_umluseCases_PackageableElement_NamedElement, gen_umluseCases_PackageableElement_ParameterableElement, gen_umluseCases_NamedElement_Element, gen_umluseCases_DirectedRelationship_Relationship, gen_umluseCases_Relationship_Element, gen_umluseCases_Namespace_NamedElement, gen_umluseCases_Type_PackageableElement, gen_umluseCases_Classifier_Namespace, gen_umluseCases_Classifier_RedefinableElement, gen_umluseCases_Classifier_Type, gen_umluseCases_Classifier_TemplateableElement, gen_umluseCases_RedefinableElement_NamedElement, gen_umluseCases_TemplateableElement_Element, gen_umluseCases_ParameterableElement_Element, gen_umluseCases_BehavioredClassifier_Classifier, gen_umluseCases_UseCase_BehavioredClassifier, gen_umluseCases_Include_NamedElement, gen_umluseCases_Include_DirectedRelationship, gen_umluseCases_Extend_NamedElement, gen_umluseCases_Extend_DirectedRelationship, gen_umluseCases_ExtensionPoint_RedefinableElement, gen_umluseCases_Actor_BehavioredClassifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)