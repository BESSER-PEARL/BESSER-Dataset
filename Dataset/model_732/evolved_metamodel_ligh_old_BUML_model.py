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
ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO")
    }
)

# Classes
uml_Package = Class(name="uml::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
uml_ActivityGroup = Class(name="uml::ActivityGroup", is_abstract=True)
uml_ActivityPartition = Class(name="uml::ActivityPartition")
NamedElement = Class(name="NamedElement")
ActivityGroup = Class(name="ActivityGroup")
Element = Class(name="Element")
TemplateableElement = Class(name="TemplateableElement")
uml_PackageableElement = Class(name="uml::PackageableElement", is_abstract=True)
uml_Activity = Class(name="uml::Activity")
Behavior = Class(name="Behavior")
uml_ActivityNode = Class(name="uml::ActivityNode", is_abstract=True)
uml_ActivityEdge = Class(name="uml::ActivityEdge", is_abstract=True)
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
uml_Namespace = Class(name="uml::Namespace", is_abstract=True)
uml_BehavioredClassifier = Class(name="uml::BehavioredClassifier", is_abstract=True)
uml_Class = Class(name="uml::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
uml_OpaqueExpression = Class(name="uml::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
uml_Behavior = Class(name="uml::Behavior", is_abstract=True)
Class_ = Class(name="Class")
uml_EncapsulatedClassifier = Class(name="uml::EncapsulatedClassifier", is_abstract=True)
StructuredClassifier = Class(name="StructuredClassifier")
uml_StructuredClassifier = Class(name="uml::StructuredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
uml_Type = Class(name="uml::Type", is_abstract=True)
uml_TemplateableElement = Class(name="uml::TemplateableElement", is_abstract=True)
uml_ParameterableElement = Class(name="uml::ParameterableElement", is_abstract=True)
uml_Element = Class(name="uml::Element", is_abstract=True)
uml_OpaqueAction = Class(name="uml::OpaqueAction")
Action = Class(name="Action")
uml_RedefinableElement = Class(name="uml::RedefinableElement", is_abstract=True)
uml_ValueSpecification = Class(name="uml::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
uml_TypedElement = Class(name="uml::TypedElement", is_abstract=True)
ParameterableElement = Class(name="ParameterableElement")
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)
uml_ActivityParameterNode = Class(name="uml::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
uml_JoinNode = Class(name="uml::JoinNode")
ControlNode = Class(name="ControlNode")
uml_InitialNode = Class(name="uml::InitialNode")
uml_DecisionNode = Class(name="uml::DecisionNode")
uml_ForkNode = Class(name="uml::ForkNode")
uml_FinalNode = Class(name="uml::FinalNode", is_abstract=True)
uml_ActivityFinalNode = Class(name="uml::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
uml_ExecutableNode = Class(name="uml::ExecutableNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
uml_ControlNode = Class(name="uml::ControlNode", is_abstract=True)
uml_Action = Class(name="uml::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
uml_ObjectNode = Class(name="uml::ObjectNode", is_abstract=True)
uml_ControlFlow = Class(name="uml::ControlFlow")
uml_ObjectFlow = Class(name="uml::ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")

# uml_Package class attributes and methods

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# uml_ActivityGroup class attributes and methods

# uml_ActivityPartition class attributes and methods

# NamedElement class attributes and methods

# ActivityGroup class attributes and methods

# Element class attributes and methods

# TemplateableElement class attributes and methods

# uml_PackageableElement class attributes and methods

# uml_Activity class attributes and methods

# Behavior class attributes and methods

# uml_ActivityNode class attributes and methods

# uml_ActivityEdge class attributes and methods

# uml_Classifier class attributes and methods
uml_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_Classifier.attributes={uml_Classifier_isAbstract}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# uml_Namespace class attributes and methods

# uml_BehavioredClassifier class attributes and methods

# uml_Class class attributes and methods
uml_Class_isActive: Property = Property(name="isActive", type=StringType)
uml_Class.attributes={uml_Class_isActive}

# EncapsulatedClassifier class attributes and methods

# BehavioredClassifier class attributes and methods

# uml_OpaqueExpression class attributes and methods
uml_OpaqueExpression_body: Property = Property(name="body", type=StringType)
uml_OpaqueExpression.attributes={uml_OpaqueExpression_body}

# ValueSpecification class attributes and methods

# uml_Behavior class attributes and methods
uml_Behavior_isReentrant: Property = Property(name="isReentrant", type=StringType)
uml_Behavior.attributes={uml_Behavior_isReentrant}

# Class class attributes and methods

# uml_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# uml_StructuredClassifier class attributes and methods

# Classifier class attributes and methods

# uml_Type class attributes and methods

# uml_TemplateableElement class attributes and methods

# uml_ParameterableElement class attributes and methods

# uml_Element class attributes and methods

# uml_OpaqueAction class attributes and methods

# Action class attributes and methods

# uml_RedefinableElement class attributes and methods
uml_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
uml_RedefinableElement.attributes={uml_RedefinableElement_isLeaf}

# uml_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# uml_TypedElement class attributes and methods

# ParameterableElement class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_name}

# uml_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# uml_JoinNode class attributes and methods
uml_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=StringType)
uml_JoinNode.attributes={uml_JoinNode_isCombineDuplicate}

# ControlNode class attributes and methods

# uml_InitialNode class attributes and methods

# uml_DecisionNode class attributes and methods

# uml_ForkNode class attributes and methods

# uml_FinalNode class attributes and methods

# uml_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# uml_ExecutableNode class attributes and methods

# ActivityNode class attributes and methods

# uml_ControlNode class attributes and methods

# uml_Action class attributes and methods

# ExecutableNode class attributes and methods

# uml_ObjectNode class attributes and methods
uml_ObjectNode_isControlType: Property = Property(name="isControlType", type=StringType)
uml_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
uml_ObjectNode.attributes={uml_ObjectNode_isControlType, uml_ObjectNode_ordering}

# uml_ControlFlow class attributes and methods

# uml_ObjectFlow class attributes and methods
uml_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=StringType)
uml_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=StringType)
uml_ObjectFlow.attributes={uml_ObjectFlow_isMultireceive, uml_ObjectFlow_isMulticast}

# ActivityEdge class attributes and methods

# Relationships
edge2: BinaryAssociation = BinaryAssociation(
    name="edge2",
    ends={
        Property(name="uml_ActivityEdge", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Activity3", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group4: BinaryAssociation = BinaryAssociation(
    name="group4",
    ends={
        Property(name="uml_ActivityGroup", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Activity5", type=uml_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node6: BinaryAssociation = BinaryAssociation(
    name="node6",
    ends={
        Property(name="uml_ActivityNode7", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityPartition", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
edge8: BinaryAssociation = BinaryAssociation(
    name="edge8",
    ends={
        Property(name="uml_ActivityEdge10", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityPartition9", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement0: BinaryAssociation = BinaryAssociation(
    name="packagedElement0",
    ends={
        Property(name="uml_PackageableElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Package", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node1: BinaryAssociation = BinaryAssociation(
    name="node1",
    ends={
        Property(name="uml_ActivityNode", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Activity", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="ActivityEdge", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="uml_Type", type=uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TypedElement", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
incoming13: BinaryAssociation = BinaryAssociation(
    name="incoming13",
    ends={
        Property(name="ActivityEdge14", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="ActivityNode", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="ActivityNode17", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard18: BinaryAssociation = BinaryAssociation(
    name="guard18",
    ends={
        Property(name="uml_ValueSpecification", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityEdge19", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_uml_Package_Namespace = Generalization(general=Namespace, specific=uml_Package)
gen_uml_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=uml_ActivityPartition)
gen_uml_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=uml_ActivityPartition)
gen_uml_ActivityGroup_Element = Generalization(general=Element, specific=uml_ActivityGroup)
gen_uml_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml_Package)
gen_uml_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Package)
gen_uml_Activity_Behavior = Generalization(general=Behavior, specific=uml_Activity)
gen_uml_Classifier_Namespace = Generalization(general=Namespace, specific=uml_Classifier)
gen_uml_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Classifier)
gen_uml_Classifier_Type = Generalization(general=Type, specific=uml_Classifier)
gen_uml_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Classifier)
gen_uml_Namespace_NamedElement = Generalization(general=NamedElement, specific=uml_Namespace)
gen_uml_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=uml_BehavioredClassifier)
gen_uml_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=uml_Class)
gen_uml_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml_Class)
gen_uml_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_OpaqueExpression)
gen_uml_Behavior_Class = Generalization(general=Class_, specific=uml_Behavior)
gen_uml_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=uml_EncapsulatedClassifier)
gen_uml_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=uml_StructuredClassifier)
gen_uml_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml_Type)
gen_uml_TemplateableElement_Element = Generalization(general=Element, specific=uml_TemplateableElement)
gen_uml_ParameterableElement_Element = Generalization(general=Element, specific=uml_ParameterableElement)
gen_uml_OpaqueAction_Action = Generalization(general=Action, specific=uml_OpaqueAction)
gen_uml_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=uml_RedefinableElement)
gen_uml_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_ActivityNode)
gen_uml_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml_ValueSpecification)
gen_uml_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=uml_ValueSpecification)
gen_uml_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml_TypedElement)
gen_uml_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml_PackageableElement)
gen_uml_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_PackageableElement)
gen_uml_NamedElement_Element = Generalization(general=Element, specific=uml_NamedElement)
gen_uml_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=uml_ActivityParameterNode)
gen_uml_JoinNode_ControlNode = Generalization(general=ControlNode, specific=uml_JoinNode)
gen_uml_InitialNode_ControlNode = Generalization(general=ControlNode, specific=uml_InitialNode)
gen_uml_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=uml_DecisionNode)
gen_uml_ForkNode_ControlNode = Generalization(general=ControlNode, specific=uml_ForkNode)
gen_uml_FinalNode_ControlNode = Generalization(general=ControlNode, specific=uml_FinalNode)
gen_uml_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=uml_ActivityFinalNode)
gen_uml_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=uml_ExecutableNode)
gen_uml_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=uml_ControlNode)
gen_uml_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=uml_Action)
gen_uml_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=uml_ObjectNode)
gen_uml_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=uml_ObjectNode)
gen_uml_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=uml_ControlFlow)
gen_uml_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_ActivityEdge)
gen_uml_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=uml_ObjectFlow)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Package, Namespace, PackageableElement, uml_ActivityGroup, uml_ActivityPartition, NamedElement, ActivityGroup, Element, TemplateableElement, uml_PackageableElement, uml_Activity, Behavior, uml_ActivityNode, uml_ActivityEdge, uml_Classifier, RedefinableElement, Type, uml_Namespace, uml_BehavioredClassifier, uml_Class, EncapsulatedClassifier, BehavioredClassifier, uml_OpaqueExpression, ValueSpecification, uml_Behavior, Class_, uml_EncapsulatedClassifier, StructuredClassifier, uml_StructuredClassifier, Classifier, uml_Type, uml_TemplateableElement, uml_ParameterableElement, uml_Element, uml_OpaqueAction, Action, uml_RedefinableElement, uml_ValueSpecification, TypedElement, uml_TypedElement, ParameterableElement, uml_NamedElement, uml_ActivityParameterNode, ObjectNode, uml_JoinNode, ControlNode, uml_InitialNode, uml_DecisionNode, uml_ForkNode, uml_FinalNode, uml_ActivityFinalNode, FinalNode, uml_ExecutableNode, ActivityNode, uml_ControlNode, uml_Action, ExecutableNode, uml_ObjectNode, uml_ControlFlow, uml_ObjectFlow, ActivityEdge, ObjectNodeOrderingKind},
    associations={edge2, group4, node6, edge8, packagedElement0, node1, outgoing12, type11, incoming13, source15, target16, guard18},
    generalizations={gen_uml_Package_Namespace, gen_uml_ActivityPartition_NamedElement, gen_uml_ActivityPartition_ActivityGroup, gen_uml_ActivityGroup_Element, gen_uml_Package_PackageableElement, gen_uml_Package_TemplateableElement, gen_uml_Activity_Behavior, gen_uml_Classifier_Namespace, gen_uml_Classifier_RedefinableElement, gen_uml_Classifier_Type, gen_uml_Classifier_TemplateableElement, gen_uml_Namespace_NamedElement, gen_uml_BehavioredClassifier_Classifier, gen_uml_Class_EncapsulatedClassifier, gen_uml_Class_BehavioredClassifier, gen_uml_OpaqueExpression_ValueSpecification, gen_uml_Behavior_Class, gen_uml_EncapsulatedClassifier_StructuredClassifier, gen_uml_StructuredClassifier_Classifier, gen_uml_Type_PackageableElement, gen_uml_TemplateableElement_Element, gen_uml_ParameterableElement_Element, gen_uml_OpaqueAction_Action, gen_uml_RedefinableElement_NamedElement, gen_uml_ActivityNode_RedefinableElement, gen_uml_ValueSpecification_PackageableElement, gen_uml_ValueSpecification_TypedElement, gen_uml_TypedElement_NamedElement, gen_uml_PackageableElement_NamedElement, gen_uml_PackageableElement_ParameterableElement, gen_uml_NamedElement_Element, gen_uml_ActivityParameterNode_ObjectNode, gen_uml_JoinNode_ControlNode, gen_uml_InitialNode_ControlNode, gen_uml_DecisionNode_ControlNode, gen_uml_ForkNode_ControlNode, gen_uml_FinalNode_ControlNode, gen_uml_ActivityFinalNode_FinalNode, gen_uml_ExecutableNode_ActivityNode, gen_uml_ControlNode_ActivityNode, gen_uml_Action_ExecutableNode, gen_uml_ObjectNode_ActivityNode, gen_uml_ObjectNode_TypedElement, gen_uml_ControlFlow_ActivityEdge, gen_uml_ActivityEdge_RedefinableElement, gen_uml_ObjectFlow_ActivityEdge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)