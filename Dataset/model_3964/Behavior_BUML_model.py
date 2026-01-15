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
behavior_BehavioralFeature = Class(name="behavior::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
NamedElement = Class(name="NamedElement")
behavior_Behavior = Class(name="behavior::Behavior", is_abstract=True)
behavior_Operation = Class(name="behavior::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
behavior_NamedElement = Class(name="behavior::NamedElement", is_abstract=True)
Element = Class(name="Element")
behavior_Feature = Class(name="behavior::Feature", is_abstract=True)
behavior_Actor = Class(name="behavior::Actor")
Object = Class(name="Object")
behavior_Class = Class(name="behavior::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
behavior_Namespace = Class(name="behavior::Namespace")
behavior_RedefinableElement = Class(name="behavior::RedefinableElement", is_abstract=True)
behavior_Element = Class(name="behavior::Element", is_abstract=True)
behavior_Comment = Class(name="behavior::Comment")
Class_ = Class(name="Class")
behavior_BehavioredClassifier = Class(name="behavior::BehavioredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
behavior_Lifeline = Class(name="behavior::Lifeline")
behavior_Classifier = Class(name="behavior::Classifier", is_abstract=True)
Namespace = Class(name="Namespace")
behavior_Message = Class(name="behavior::Message")
behavior_Interaction = Class(name="behavior::Interaction")
behavior_MessageEnd = Class(name="behavior::MessageEnd")
behavior_Connector = Class(name="behavior::Connector")
behavior_InteractionFragment = Class(name="behavior::InteractionFragment", is_abstract=True)
behavior_DestructionEvent = Class(name="behavior::DestructionEvent")
behavior_BehaviorExecutionSpecification = Class(name="behavior::BehaviorExecutionSpecification")
Behavior = Class(name="Behavior")
InteractionFragment = Class(name="InteractionFragment")
behavior_Event = Class(name="behavior::Event", is_abstract=True)
behavior_CreatEvent = Class(name="behavior::CreatEvent")
Event = Class(name="Event")
behavior_ExecutionEvent = Class(name="behavior::ExecutionEvent")
behavior_MessageOccurrenceSpecification = Class(name="behavior::MessageOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
MessageEnd = Class(name="MessageEnd")
behavior_GeneralOrdering = Class(name="behavior::GeneralOrdering")
RedefinableElement = Class(name="RedefinableElement")
behavior_OccurrenceSpecification = Class(name="behavior::OccurrenceSpecification")
behavior_ExecutionSpecification = Class(name="behavior::ExecutionSpecification", is_abstract=True)
behavior_ExecutionOccurrenceSpecification = Class(name="behavior::ExecutionOccurrenceSpecification")
ExecutionSpecification = Class(name="ExecutionSpecification")
behavior_Object = Class(name="behavior::Object")

# behavior_BehavioralFeature class attributes and methods

# Feature class attributes and methods

# NamedElement class attributes and methods

# behavior_Behavior class attributes and methods

# behavior_Operation class attributes and methods

# BehavioralFeature class attributes and methods

# behavior_NamedElement class attributes and methods
behavior_NamedElement_name: Property = Property(name="name", type=StringType)
behavior_NamedElement_Archpoint: Property = Property(name="Archpoint", type=BooleanType)
behavior_NamedElement.attributes={behavior_NamedElement_name, behavior_NamedElement_Archpoint}

# Element class attributes and methods

# behavior_Feature class attributes and methods
behavior_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
behavior_Feature.attributes={behavior_Feature_isStatic}

# behavior_Actor class attributes and methods

# Object class attributes and methods

# behavior_Class class attributes and methods

# BehavioredClassifier class attributes and methods

# behavior_Namespace class attributes and methods

# behavior_RedefinableElement class attributes and methods

# behavior_Element class attributes and methods

# behavior_Comment class attributes and methods
behavior_Comment_body: Property = Property(name="body", type=StringType)
behavior_Comment.attributes={behavior_Comment_body}

# Class class attributes and methods

# behavior_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# behavior_Lifeline class attributes and methods

# behavior_Classifier class attributes and methods
behavior_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
behavior_Classifier.attributes={behavior_Classifier_isAbstract}

# Namespace class attributes and methods

# behavior_Message class attributes and methods
behavior_Message_MessageOrder: Property = Property(name="MessageOrder", type=IntegerType)
behavior_Message.attributes={behavior_Message_MessageOrder}

# behavior_Interaction class attributes and methods

# behavior_MessageEnd class attributes and methods

# behavior_Connector class attributes and methods

# behavior_InteractionFragment class attributes and methods

# behavior_DestructionEvent class attributes and methods

# behavior_BehaviorExecutionSpecification class attributes and methods

# Behavior class attributes and methods

# InteractionFragment class attributes and methods

# behavior_Event class attributes and methods

# behavior_CreatEvent class attributes and methods

# Event class attributes and methods

# behavior_ExecutionEvent class attributes and methods

# behavior_MessageOccurrenceSpecification class attributes and methods

# OccurrenceSpecification class attributes and methods

# MessageEnd class attributes and methods

# behavior_GeneralOrdering class attributes and methods

# RedefinableElement class attributes and methods

# behavior_OccurrenceSpecification class attributes and methods

# behavior_ExecutionSpecification class attributes and methods

# behavior_ExecutionOccurrenceSpecification class attributes and methods

# ExecutionSpecification class attributes and methods

# behavior_Object class attributes and methods

# Relationships
method0: BinaryAssociation = BinaryAssociation(
    name="method0",
    ends={
        Property(name="Behavior", type=behavior_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=behavior_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
feature20: BinaryAssociation = BinaryAssociation(
    name="feature20",
    ends={
        Property(name="Feature", type=behavior_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=behavior_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier21: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier21",
    ends={
        Property(name="behavior_Classifier22", type=behavior_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Class", type=behavior_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext23: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext23",
    ends={
        Property(name="behavior_Classifier24", type=behavior_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_RedefinableElement", type=behavior_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinableELement26: BinaryAssociation = BinaryAssociation(
    name="redefinableELement26",
    ends={
        Property(name="behavior_RedefinableElement27", type=behavior_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_RedefinableElement25", type=behavior_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment28: BinaryAssociation = BinaryAssociation(
    name="ownedComment28",
    ends={
        Property(name="behavior_Comment", type=behavior_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Element", type=behavior_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context1: BinaryAssociation = BinaryAssociation(
    name="context1",
    ends={
        Property(name="behavior_BehavioredClassifier", type=behavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Behavior", type=behavior_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
specification2: BinaryAssociation = BinaryAssociation(
    name="specification2",
    ends={
        Property(name="BehavioralFeature", type=behavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=behavior_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
redefinedBehavior4: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior4",
    ends={
        Property(name="behavior_Behavior5", type=behavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Behavior3", type=behavior_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
classifierBehavior6: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior6",
    ends={
        Property(name="behavior_Behavior8", type=behavior_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_BehavioredClassifier7", type=behavior_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
ownedBehavior9: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior9",
    ends={
        Property(name="behavior_Behavior11", type=behavior_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_BehavioredClassifier10", type=behavior_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include12: BinaryAssociation = BinaryAssociation(
    name="include12",
    ends={
        Property(name="Lifeline", type=behavior_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="actor", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1))
    }
)
inheritedMember13: BinaryAssociation = BinaryAssociation(
    name="inheritedMember13",
    ends={
        Property(name="behavior_NamedElement", type=behavior_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Classifier", type=behavior_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier15: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier15",
    ends={
        Property(name="behavior_Classifier16", type=behavior_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Classifier14", type=behavior_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general18: BinaryAssociation = BinaryAssociation(
    name="general18",
    ends={
        Property(name="behavior_Classifier19", type=behavior_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Classifier17", type=behavior_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
fragment48: BinaryAssociation = BinaryAssociation(
    name="fragment48",
    ends={
        Property(name="InteractionFragment49", type=behavior_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingInteraction", type=behavior_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object50: BinaryAssociation = BinaryAssociation(
    name="object50",
    ends={
        Property(name="behavior_BehavioredClassifier51", type=behavior_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Interaction", type=behavior_BehavioredClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destructionevent52: BinaryAssociation = BinaryAssociation(
    name="destructionevent52",
    ends={
        Property(name="DestructionEvent53", type=behavior_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=behavior_DestructionEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifeline54: BinaryAssociation = BinaryAssociation(
    name="lifeline54",
    ends={
        Property(name="Lifeline56", type=behavior_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction55", type=behavior_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message57: BinaryAssociation = BinaryAssociation(
    name="message57",
    ends={
        Property(name="Message", type=behavior_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction58", type=behavior_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
covered59: BinaryAssociation = BinaryAssociation(
    name="covered59",
    ends={
        Property(name="Lifeline60", type=behavior_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=behavior_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
enclosingInteraction61: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction61",
    ends={
        Property(name="Interaction62", type=behavior_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment", type=behavior_Interaction, multiplicity=Multiplicity(0, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="behavior_Element31", type=behavior_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Element29", type=behavior_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement33: BinaryAssociation = BinaryAssociation(
    name="ownedElement33",
    ends={
        Property(name="behavior_Element34", type=behavior_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Element32", type=behavior_Element, multiplicity=Multiplicity(0, 9999))
    }
)
interaction35: BinaryAssociation = BinaryAssociation(
    name="interaction35",
    ends={
        Property(name="Interaction", type=behavior_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=behavior_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
receiveEvent36: BinaryAssociation = BinaryAssociation(
    name="receiveEvent36",
    ends={
        Property(name="behavior_MessageEnd", type=behavior_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Message", type=behavior_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent37: BinaryAssociation = BinaryAssociation(
    name="sendEvent37",
    ends={
        Property(name="behavior_MessageEnd39", type=behavior_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Message38", type=behavior_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
connector40: BinaryAssociation = BinaryAssociation(
    name="connector40",
    ends={
        Property(name="behavior_Connector", type=behavior_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Message41", type=behavior_Connector, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy42: BinaryAssociation = BinaryAssociation(
    name="coveredBy42",
    ends={
        Property(name="InteractionFragment", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=behavior_InteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
interaction43: BinaryAssociation = BinaryAssociation(
    name="interaction43",
    ends={
        Property(name="Interaction44", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="lifeline", type=behavior_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
endby45: BinaryAssociation = BinaryAssociation(
    name="endby45",
    ends={
        Property(name="DestructionEvent", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="end", type=behavior_DestructionEvent, multiplicity=Multiplicity(1, 1))
    }
)
actor46: BinaryAssociation = BinaryAssociation(
    name="actor46",
    ends={
        Property(name="BehavioredClassifier", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=behavior_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
behaviorExecution47: BinaryAssociation = BinaryAssociation(
    name="behaviorExecution47",
    ends={
        Property(name="behavior_BehaviorExecutionSpecification", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Lifeline", type=behavior_BehaviorExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract78: BinaryAssociation = BinaryAssociation(
    name="contract78",
    ends={
        Property(name="behavior_Behavior80", type=behavior_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Connector79", type=behavior_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
end81: BinaryAssociation = BinaryAssociation(
    name="end81",
    ends={
        Property(name="Lifeline82", type=behavior_DestructionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="endby", type=behavior_Lifeline, multiplicity=Multiplicity(1, 1))
    }
)
interaction83: BinaryAssociation = BinaryAssociation(
    name="interaction83",
    ends={
        Property(name="Interaction84", type=behavior_DestructionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="destructionevent", type=behavior_Interaction, multiplicity=Multiplicity(0, 1))
    }
)
generalOrdering63: BinaryAssociation = BinaryAssociation(
    name="generalOrdering63",
    ends={
        Property(name="behavior_GeneralOrdering", type=behavior_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_InteractionFragment", type=behavior_GeneralOrdering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotatedElement64: BinaryAssociation = BinaryAssociation(
    name="annotatedElement64",
    ends={
        Property(name="behavior_Element66", type=behavior_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_Comment65", type=behavior_Element, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier67: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier67",
    ends={
        Property(name="Classifier", type=behavior_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=behavior_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
toAfter68: BinaryAssociation = BinaryAssociation(
    name="toAfter68",
    ends={
        Property(name="GeneralOrdering", type=behavior_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="before", type=behavior_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
toBefore69: BinaryAssociation = BinaryAssociation(
    name="toBefore69",
    ends={
        Property(name="GeneralOrdering70", type=behavior_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="after", type=behavior_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
start71: BinaryAssociation = BinaryAssociation(
    name="start71",
    ends={
        Property(name="behavior_OccurrenceSpecification", type=behavior_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_ExecutionSpecification", type=behavior_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
finish72: BinaryAssociation = BinaryAssociation(
    name="finish72",
    ends={
        Property(name="behavior_OccurrenceSpecification74", type=behavior_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_ExecutionSpecification73", type=behavior_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
message75: BinaryAssociation = BinaryAssociation(
    name="message75",
    ends={
        Property(name="behavior_Message77", type=behavior_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_MessageEnd76", type=behavior_Message, multiplicity=Multiplicity(0, 1))
    }
)
event85: BinaryAssociation = BinaryAssociation(
    name="event85",
    ends={
        Property(name="behavior_Event", type=behavior_MessageOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_MessageOccurrenceSpecification", type=behavior_Event, multiplicity=Multiplicity(1, 1))
    }
)
execution86: BinaryAssociation = BinaryAssociation(
    name="execution86",
    ends={
        Property(name="behavior_ExecutionSpecification87", type=behavior_ExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior_ExecutionOccurrenceSpecification", type=behavior_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
before88: BinaryAssociation = BinaryAssociation(
    name="before88",
    ends={
        Property(name="OccurrenceSpecification", type=behavior_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toAfter", type=behavior_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
after89: BinaryAssociation = BinaryAssociation(
    name="after89",
    ends={
        Property(name="OccurrenceSpecification90", type=behavior_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toBefore", type=behavior_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_behavior_BehavioralFeature_Feature = Generalization(general=Feature, specific=behavior_BehavioralFeature)
gen_behavior_BehavioralFeature_NamedElement = Generalization(general=NamedElement, specific=behavior_BehavioralFeature)
gen_behavior_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=behavior_Operation)
gen_behavior_NamedElement_Element = Generalization(general=Element, specific=behavior_NamedElement)
gen_behavior_Actor_Object = Generalization(general=Object, specific=behavior_Actor)
gen_behavior_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=behavior_Class)
gen_behavior_Namespace_NamedElement = Generalization(general=NamedElement, specific=behavior_Namespace)
gen_behavior_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=behavior_RedefinableElement)
gen_behavior_Behavior_Class = Generalization(general=Class_, specific=behavior_Behavior)
gen_behavior_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=behavior_BehavioredClassifier)
gen_behavior_Classifier_Namespace = Generalization(general=Namespace, specific=behavior_Classifier)
gen_behavior_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=behavior_InteractionFragment)
gen_behavior_Message_NamedElement = Generalization(general=NamedElement, specific=behavior_Message)
gen_behavior_Lifeline_NamedElement = Generalization(general=NamedElement, specific=behavior_Lifeline)
gen_behavior_Interaction_Behavior = Generalization(general=Behavior, specific=behavior_Interaction)
gen_behavior_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=behavior_Interaction)
gen_behavior_Event_NamedElement = Generalization(general=NamedElement, specific=behavior_Event)
gen_behavior_CreatEvent_Event = Generalization(general=Event, specific=behavior_CreatEvent)
gen_behavior_DestructionEvent_Event = Generalization(general=Event, specific=behavior_DestructionEvent)
gen_behavior_ExecutionEvent_Event = Generalization(general=Event, specific=behavior_ExecutionEvent)
gen_behavior_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=behavior_MessageOccurrenceSpecification)
gen_behavior_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=behavior_MessageOccurrenceSpecification)
gen_behavior_Comment_Element = Generalization(general=Element, specific=behavior_Comment)
gen_behavior_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=behavior_Feature)
gen_behavior_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=behavior_OccurrenceSpecification)
gen_behavior_ExecutionSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=behavior_ExecutionSpecification)
gen_behavior_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=behavior_MessageEnd)
gen_behavior_Connector_Feature = Generalization(general=Feature, specific=behavior_Connector)
gen_behavior_ExecutionOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=behavior_ExecutionOccurrenceSpecification)
gen_behavior_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=behavior_GeneralOrdering)
gen_behavior_BehaviorExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=behavior_BehaviorExecutionSpecification)
gen_behavior_Object_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=behavior_Object)

# Domain Model
domain_model = DomainModel(
    name="behavior",
    types={behavior_BehavioralFeature, Feature, NamedElement, behavior_Behavior, behavior_Operation, BehavioralFeature, behavior_NamedElement, Element, behavior_Feature, behavior_Actor, Object, behavior_Class, BehavioredClassifier, behavior_Namespace, behavior_RedefinableElement, behavior_Element, behavior_Comment, Class_, behavior_BehavioredClassifier, Classifier, behavior_Lifeline, behavior_Classifier, Namespace, behavior_Message, behavior_Interaction, behavior_MessageEnd, behavior_Connector, behavior_InteractionFragment, behavior_DestructionEvent, behavior_BehaviorExecutionSpecification, Behavior, InteractionFragment, behavior_Event, behavior_CreatEvent, Event, behavior_ExecutionEvent, behavior_MessageOccurrenceSpecification, OccurrenceSpecification, MessageEnd, behavior_GeneralOrdering, RedefinableElement, behavior_OccurrenceSpecification, behavior_ExecutionSpecification, behavior_ExecutionOccurrenceSpecification, ExecutionSpecification, behavior_Object},
    associations={method0, feature20, nestedClassifier21, redefinitionContext23, redefinableELement26, ownedComment28, context1, specification2, redefinedBehavior4, classifierBehavior6, ownedBehavior9, include12, inheritedMember13, redefinedClassifier15, general18, fragment48, object50, destructionevent52, lifeline54, message57, covered59, enclosingInteraction61, owner30, ownedElement33, interaction35, receiveEvent36, sendEvent37, connector40, coveredBy42, interaction43, endby45, actor46, behaviorExecution47, contract78, end81, interaction83, generalOrdering63, annotatedElement64, featuringClassifier67, toAfter68, toBefore69, start71, finish72, message75, event85, execution86, before88, after89},
    generalizations={gen_behavior_BehavioralFeature_Feature, gen_behavior_BehavioralFeature_NamedElement, gen_behavior_Operation_BehavioralFeature, gen_behavior_NamedElement_Element, gen_behavior_Actor_Object, gen_behavior_Class_BehavioredClassifier, gen_behavior_Namespace_NamedElement, gen_behavior_RedefinableElement_NamedElement, gen_behavior_Behavior_Class, gen_behavior_BehavioredClassifier_Classifier, gen_behavior_Classifier_Namespace, gen_behavior_InteractionFragment_NamedElement, gen_behavior_Message_NamedElement, gen_behavior_Lifeline_NamedElement, gen_behavior_Interaction_Behavior, gen_behavior_Interaction_InteractionFragment, gen_behavior_Event_NamedElement, gen_behavior_CreatEvent_Event, gen_behavior_DestructionEvent_Event, gen_behavior_ExecutionEvent_Event, gen_behavior_MessageOccurrenceSpecification_OccurrenceSpecification, gen_behavior_MessageOccurrenceSpecification_MessageEnd, gen_behavior_Comment_Element, gen_behavior_Feature_RedefinableElement, gen_behavior_OccurrenceSpecification_InteractionFragment, gen_behavior_ExecutionSpecification_InteractionFragment, gen_behavior_MessageEnd_NamedElement, gen_behavior_Connector_Feature, gen_behavior_ExecutionOccurrenceSpecification_OccurrenceSpecification, gen_behavior_GeneralOrdering_NamedElement, gen_behavior_BehaviorExecutionSpecification_ExecutionSpecification, gen_behavior_Object_BehavioredClassifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)