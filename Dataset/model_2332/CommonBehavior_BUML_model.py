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
CallConcurrencyFeature: Enumeration = Enumeration(
    name="CallConcurrencyFeature",
    literals={
            EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="guarded"),
			EnumerationLiteral(name="concurrent")
    }
)

# Classes
CommonBehavior_BasicBehavior_BehavioredClassifier = Class(name="CommonBehavior_BasicBehavior_BehavioredClassifier")
Classifier = Class(name="Classifier")
CommonBehavior_BasicBehavior_FunctionBehavior = Class(name="CommonBehavior_BasicBehavior_FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
CommonBehavior_BasicBehavior_BehavioralFeature = Class(name="CommonBehavior_BasicBehavior_BehavioralFeature", is_abstract=True)
Behavior = Class(name="Behavior")
CommonBehavior_BasicBehavior_Classifier = Class(name="CommonBehavior_BasicBehavior_Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
CommonBehavior_BasicBehavior_Class = Class(name="CommonBehavior_BasicBehavior_Class", is_abstract=True)
BasicBehavior_Classifier = Class(name="BasicBehavior_Classifier")
BasicBehavior_BehavioredClassifier = Class(name="BasicBehavior_BehavioredClassifier")
Reception = Class(name="Reception")
CommonBehavior_BasicBehavior_Behavior = Class(name="CommonBehavior_BasicBehavior_Behavior", is_abstract=True)
Class_ = Class(name="Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
BehavioralFeature = Class(name="BehavioralFeature")
Parameter_ = Class(name="Parameter")
Constraint = Class(name="Constraint")
CommonBehavior_BasicBehavior_RedefinableElement = Class(name="CommonBehavior_BasicBehavior_RedefinableElement", is_abstract=True)
CommonBehavior_BasicBehavior_OpaqueBehavior = Class(name="CommonBehavior_BasicBehavior_OpaqueBehavior")
Signal = Class(name="Signal")
CommonBehavior_Communications_Interface = Class(name="CommonBehavior_Communications_Interface")
CommonBehavior_BasicBehavior_Parameter = Class(name="CommonBehavior_BasicBehavior_Parameter")
CommonBehavior_BasicBehavior_OpaqueExpression = Class(name="CommonBehavior_BasicBehavior_OpaqueExpression")
CommonBehavior_BasicBehavior_Constraint = Class(name="CommonBehavior_BasicBehavior_Constraint")
CommonBehavior_Communications_Signal = Class(name="CommonBehavior_Communications_Signal")
Property_ = Class(name="Property")
CommonBehavior_Communications_Property = Class(name="CommonBehavior_Communications_Property")
CommonBehavior_Communications_Reception = Class(name="CommonBehavior_Communications_Reception")
Observation = Class(name="Observation")
CommonBehavior_SimpleTime_Observation = Class(name="CommonBehavior_SimpleTime_Observation", is_abstract=True)
CommonBehavior_SimpleTime_TimeObservation = Class(name="CommonBehavior_SimpleTime_TimeObservation")
CommonBehavior_Communications_NamedElement = Class(name="CommonBehavior_Communications_NamedElement", is_abstract=True)
CommonBehavior_Communications_Trigger = Class(name="CommonBehavior_Communications_Trigger")
NamedElement = Class(name="NamedElement")
Event = Class(name="Event")
CommonBehavior_Communications_PackageableElement = Class(name="CommonBehavior_Communications_PackageableElement", is_abstract=True)
CommonBehavior_Communications_Event = Class(name="CommonBehavior_Communications_Event", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
CommonBehavior_Communications_MessageEvent = Class(name="CommonBehavior_Communications_MessageEvent", is_abstract=True)
CommonBehavior_Communications_AnyReceiveEvent = Class(name="CommonBehavior_Communications_AnyReceiveEvent")
MessageEvent = Class(name="MessageEvent")
CommonBehavior_Communications_SignalEvent = Class(name="CommonBehavior_Communications_SignalEvent")
CommonBehavior_Communications_CallEvent = Class(name="CommonBehavior_Communications_CallEvent")
Operation = Class(name="Operation")
CommonBehavior_Communications_Operation = Class(name="CommonBehavior_Communications_Operation")
CommonBehavior_Communications_ChangeEvent = Class(name="CommonBehavior_Communications_ChangeEvent")
ValueSpecification = Class(name="ValueSpecification")
CommonBehavior_Communications_ValueSpecification = Class(name="CommonBehavior_Communications_ValueSpecification", is_abstract=True)
CommonBehavior_SimpleTime_TimeEvent = Class(name="CommonBehavior_SimpleTime_TimeEvent")
TimeExpression = Class(name="TimeExpression")
CommonBehavior_SimpleTime_TimeExpression = Class(name="CommonBehavior_SimpleTime_TimeExpression")
DurationInterval = Class(name="DurationInterval")
CommonBehavior_SimpleTime_DurationObservation = Class(name="CommonBehavior_SimpleTime_DurationObservation")
CommonBehavior_SimpleTime_Duration = Class(name="CommonBehavior_SimpleTime_Duration")
CommonBehavior_SimpleTime_Interval = Class(name="CommonBehavior_SimpleTime_Interval")
CommonBehavior_SimpleTime_TimeInterval = Class(name="CommonBehavior_SimpleTime_TimeInterval")
Interval = Class(name="Interval")
CommonBehavior_SimpleTime_DurationInterval = Class(name="CommonBehavior_SimpleTime_DurationInterval")
Duration = Class(name="Duration")
CommonBehavior_SimpleTime_IntervalConstraint = Class(name="CommonBehavior_SimpleTime_IntervalConstraint")
CommonBehavior_SimpleTime_TimeConstraint = Class(name="CommonBehavior_SimpleTime_TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
TimeInterval = Class(name="TimeInterval")
CommonBehavior_SimpleTime_DurationConstraint = Class(name="CommonBehavior_SimpleTime_DurationConstraint")

# CommonBehavior_BasicBehavior_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# CommonBehavior_BasicBehavior_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# CommonBehavior_BasicBehavior_BehavioralFeature class attributes and methods
CommonBehavior_BasicBehavior_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
CommonBehavior_BasicBehavior_BehavioralFeature.attributes={CommonBehavior_BasicBehavior_BehavioralFeature_concurrency}

# Behavior class attributes and methods

# CommonBehavior_BasicBehavior_Classifier class attributes and methods

# RedefinableElement class attributes and methods

# CommonBehavior_BasicBehavior_Class class attributes and methods

# BasicBehavior_Classifier class attributes and methods

# BasicBehavior_BehavioredClassifier class attributes and methods

# Reception class attributes and methods

# CommonBehavior_BasicBehavior_Behavior class attributes and methods
CommonBehavior_BasicBehavior_Behavior_isReentrant: Property = Property(name="isReentrant", type=BooleanType)
CommonBehavior_BasicBehavior_Behavior.attributes={CommonBehavior_BasicBehavior_Behavior_isReentrant}

# Class class attributes and methods

# BehavioredClassifier class attributes and methods

# BehavioralFeature class attributes and methods

# Parameter class attributes and methods

# Constraint class attributes and methods

# CommonBehavior_BasicBehavior_RedefinableElement class attributes and methods

# CommonBehavior_BasicBehavior_OpaqueBehavior class attributes and methods
CommonBehavior_BasicBehavior_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
CommonBehavior_BasicBehavior_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
CommonBehavior_BasicBehavior_OpaqueBehavior.attributes={CommonBehavior_BasicBehavior_OpaqueBehavior_body, CommonBehavior_BasicBehavior_OpaqueBehavior_language}

# Signal class attributes and methods

# CommonBehavior_Communications_Interface class attributes and methods

# CommonBehavior_BasicBehavior_Parameter class attributes and methods

# CommonBehavior_BasicBehavior_OpaqueExpression class attributes and methods

# CommonBehavior_BasicBehavior_Constraint class attributes and methods

# CommonBehavior_Communications_Signal class attributes and methods

# Property class attributes and methods

# CommonBehavior_Communications_Property class attributes and methods

# CommonBehavior_Communications_Reception class attributes and methods

# Observation class attributes and methods

# CommonBehavior_SimpleTime_Observation class attributes and methods

# CommonBehavior_SimpleTime_TimeObservation class attributes and methods
CommonBehavior_SimpleTime_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CommonBehavior_SimpleTime_TimeObservation.attributes={CommonBehavior_SimpleTime_TimeObservation_firstEvent}

# CommonBehavior_Communications_NamedElement class attributes and methods

# CommonBehavior_Communications_Trigger class attributes and methods

# NamedElement class attributes and methods

# Event class attributes and methods

# CommonBehavior_Communications_PackageableElement class attributes and methods

# CommonBehavior_Communications_Event class attributes and methods

# PackageableElement class attributes and methods

# CommonBehavior_Communications_MessageEvent class attributes and methods

# CommonBehavior_Communications_AnyReceiveEvent class attributes and methods

# MessageEvent class attributes and methods

# CommonBehavior_Communications_SignalEvent class attributes and methods

# CommonBehavior_Communications_CallEvent class attributes and methods

# Operation class attributes and methods

# CommonBehavior_Communications_Operation class attributes and methods

# CommonBehavior_Communications_ChangeEvent class attributes and methods

# ValueSpecification class attributes and methods

# CommonBehavior_Communications_ValueSpecification class attributes and methods

# CommonBehavior_SimpleTime_TimeEvent class attributes and methods
CommonBehavior_SimpleTime_TimeEvent_isRelative: Property = Property(name="isRelative", type=BooleanType)
CommonBehavior_SimpleTime_TimeEvent.attributes={CommonBehavior_SimpleTime_TimeEvent_isRelative}

# TimeExpression class attributes and methods

# CommonBehavior_SimpleTime_TimeExpression class attributes and methods

# DurationInterval class attributes and methods

# CommonBehavior_SimpleTime_DurationObservation class attributes and methods
CommonBehavior_SimpleTime_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CommonBehavior_SimpleTime_DurationObservation.attributes={CommonBehavior_SimpleTime_DurationObservation_firstEvent}

# CommonBehavior_SimpleTime_Duration class attributes and methods

# CommonBehavior_SimpleTime_Interval class attributes and methods

# CommonBehavior_SimpleTime_TimeInterval class attributes and methods

# Interval class attributes and methods

# CommonBehavior_SimpleTime_DurationInterval class attributes and methods

# Duration class attributes and methods

# CommonBehavior_SimpleTime_IntervalConstraint class attributes and methods

# CommonBehavior_SimpleTime_TimeConstraint class attributes and methods
CommonBehavior_SimpleTime_TimeConstraint_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CommonBehavior_SimpleTime_TimeConstraint.attributes={CommonBehavior_SimpleTime_TimeConstraint_firstEvent}

# IntervalConstraint class attributes and methods

# TimeInterval class attributes and methods

# CommonBehavior_SimpleTime_DurationConstraint class attributes and methods
CommonBehavior_SimpleTime_DurationConstraint_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CommonBehavior_SimpleTime_DurationConstraint.attributes={CommonBehavior_SimpleTime_DurationConstraint_firstEvent}

# Relationships
ownedBehavior0: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior0",
    ends={
        Property(name="Behavior", type=CommonBehavior_BasicBehavior_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_BehavioredClassifier", type=Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior1: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior1",
    ends={
        Property(name="Behavior3", type=CommonBehavior_BasicBehavior_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_BehavioredClassifier2", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
ownedReception4: BinaryAssociation = BinaryAssociation(
    name="ownedReception4",
    ends={
        Property(name="Reception", type=CommonBehavior_BasicBehavior_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Class", type=Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context5: BinaryAssociation = BinaryAssociation(
    name="context5",
    ends={
        Property(name="BehavioredClassifier", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior", type=BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
redefinedBehavior6: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior6",
    ends={
        Property(name="Behavior8", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior7", type=Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
specification9: BinaryAssociation = BinaryAssociation(
    name="specification9",
    ends={
        Property(name="BehavioralFeature", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter10: BinaryAssociation = BinaryAssociation(
    name="ownedParameter10",
    ends={
        Property(name="Parameter", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior11", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition12: BinaryAssociation = BinaryAssociation(
    name="precondition12",
    ends={
        Property(name="Constraint", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior13", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition14: BinaryAssociation = BinaryAssociation(
    name="postcondition14",
    ends={
        Property(name="Constraint16", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior15", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal25: BinaryAssociation = BinaryAssociation(
    name="signal25",
    ends={
        Property(name="Signal", type=CommonBehavior_Communications_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Reception", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
method17: BinaryAssociation = BinaryAssociation(
    name="method17",
    ends={
        Property(name="Behavior18", type=CommonBehavior_BasicBehavior_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
result19: BinaryAssociation = BinaryAssociation(
    name="result19",
    ends={
        Property(name="Parameter20", type=CommonBehavior_BasicBehavior_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_OpaqueExpression", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
behavior21: BinaryAssociation = BinaryAssociation(
    name="behavior21",
    ends={
        Property(name="Behavior23", type=CommonBehavior_BasicBehavior_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_OpaqueExpression22", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute24: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute24",
    ends={
        Property(name="Property", type=CommonBehavior_Communications_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Signal", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observation36: BinaryAssociation = BinaryAssociation(
    name="observation36",
    ends={
        Property(name="Observation", type=CommonBehavior_SimpleTime_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeExpression37", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception26: BinaryAssociation = BinaryAssociation(
    name="ownedReception26",
    ends={
        Property(name="Reception27", type=CommonBehavior_Communications_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Interface", type=Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event28: BinaryAssociation = BinaryAssociation(
    name="event28",
    ends={
        Property(name="Event", type=CommonBehavior_Communications_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Trigger", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
signal29: BinaryAssociation = BinaryAssociation(
    name="signal29",
    ends={
        Property(name="Signal30", type=CommonBehavior_Communications_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_SignalEvent", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation31: BinaryAssociation = BinaryAssociation(
    name="operation31",
    ends={
        Property(name="Operation", type=CommonBehavior_Communications_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_CallEvent", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression32: BinaryAssociation = BinaryAssociation(
    name="changeExpression32",
    ends={
        Property(name="ValueSpecification", type=CommonBehavior_Communications_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_ChangeEvent", type=ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
when33: BinaryAssociation = BinaryAssociation(
    name="when33",
    ends={
        Property(name="TimeExpression", type=CommonBehavior_SimpleTime_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeEvent", type=TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr34: BinaryAssociation = BinaryAssociation(
    name="expr34",
    ends={
        Property(name="ValueSpecification35", type=CommonBehavior_SimpleTime_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeExpression", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
durationSpecification61: BinaryAssociation = BinaryAssociation(
    name="durationSpecification61",
    ends={
        Property(name="DurationInterval", type=CommonBehavior_SimpleTime_DurationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationConstraint", type=DurationInterval, multiplicity=Multiplicity(1, 1))
    }
)
event38: BinaryAssociation = BinaryAssociation(
    name="event38",
    ends={
        Property(name="NamedElement", type=CommonBehavior_SimpleTime_TimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeObservation", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
event39: BinaryAssociation = BinaryAssociation(
    name="event39",
    ends={
        Property(name="NamedElement40", type=CommonBehavior_SimpleTime_DurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationObservation", type=NamedElement, multiplicity=Multiplicity(1, 2))
    }
)
expr41: BinaryAssociation = BinaryAssociation(
    name="expr41",
    ends={
        Property(name="ValueSpecification42", type=CommonBehavior_SimpleTime_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Duration", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation43: BinaryAssociation = BinaryAssociation(
    name="observation43",
    ends={
        Property(name="Observation45", type=CommonBehavior_SimpleTime_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Duration44", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
max46: BinaryAssociation = BinaryAssociation(
    name="max46",
    ends={
        Property(name="ValueSpecification47", type=CommonBehavior_SimpleTime_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Interval", type=ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
min48: BinaryAssociation = BinaryAssociation(
    name="min48",
    ends={
        Property(name="ValueSpecification50", type=CommonBehavior_SimpleTime_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Interval49", type=ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
timeMax51: BinaryAssociation = BinaryAssociation(
    name="timeMax51",
    ends={
        Property(name="TimeExpression52", type=CommonBehavior_SimpleTime_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeInterval", type=TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
timeMin53: BinaryAssociation = BinaryAssociation(
    name="timeMin53",
    ends={
        Property(name="TimeExpression55", type=CommonBehavior_SimpleTime_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeInterval54", type=TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
durationMax56: BinaryAssociation = BinaryAssociation(
    name="durationMax56",
    ends={
        Property(name="Duration", type=CommonBehavior_SimpleTime_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationInterval", type=Duration, multiplicity=Multiplicity(1, 1))
    }
)
durationMin57: BinaryAssociation = BinaryAssociation(
    name="durationMin57",
    ends={
        Property(name="Duration59", type=CommonBehavior_SimpleTime_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationInterval58", type=Duration, multiplicity=Multiplicity(1, 1))
    }
)
timeSpecification60: BinaryAssociation = BinaryAssociation(
    name="timeSpecification60",
    ends={
        Property(name="TimeInterval", type=CommonBehavior_SimpleTime_TimeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeConstraint", type=TimeInterval, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CommonBehavior_BasicBehavior_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=CommonBehavior_BasicBehavior_BehavioredClassifier)
gen_CommonBehavior_BasicBehavior_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=CommonBehavior_BasicBehavior_FunctionBehavior)
gen_CommonBehavior_BasicBehavior_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=CommonBehavior_BasicBehavior_Classifier)
gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_Classifier = Generalization(general=BasicBehavior_Classifier, specific=CommonBehavior_BasicBehavior_Class)
gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_BehavioredClassifier = Generalization(general=BasicBehavior_BehavioredClassifier, specific=CommonBehavior_BasicBehavior_Class)
gen_CommonBehavior_BasicBehavior_Behavior_Class = Generalization(general=Class_, specific=CommonBehavior_BasicBehavior_Behavior)
gen_CommonBehavior_BasicBehavior_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=CommonBehavior_BasicBehavior_OpaqueBehavior)
gen_CommonBehavior_Communications_Interface_Classifier = Generalization(general=Classifier, specific=CommonBehavior_Communications_Interface)
gen_CommonBehavior_Communications_Signal_Classifier = Generalization(general=Classifier, specific=CommonBehavior_Communications_Signal)
gen_CommonBehavior_Communications_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=CommonBehavior_Communications_Reception)
gen_CommonBehavior_SimpleTime_Observation_PackageableElement = Generalization(general=PackageableElement, specific=CommonBehavior_SimpleTime_Observation)
gen_CommonBehavior_SimpleTime_TimeObservation_Observation = Generalization(general=Observation, specific=CommonBehavior_SimpleTime_TimeObservation)
gen_CommonBehavior_Communications_Trigger_NamedElement = Generalization(general=NamedElement, specific=CommonBehavior_Communications_Trigger)
gen_CommonBehavior_Communications_Event_PackageableElement = Generalization(general=PackageableElement, specific=CommonBehavior_Communications_Event)
gen_CommonBehavior_Communications_MessageEvent_Event = Generalization(general=Event, specific=CommonBehavior_Communications_MessageEvent)
gen_CommonBehavior_Communications_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=CommonBehavior_Communications_AnyReceiveEvent)
gen_CommonBehavior_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=CommonBehavior_Communications_SignalEvent)
gen_CommonBehavior_Communications_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=CommonBehavior_Communications_CallEvent)
gen_CommonBehavior_Communications_ChangeEvent_Event = Generalization(general=Event, specific=CommonBehavior_Communications_ChangeEvent)
gen_CommonBehavior_SimpleTime_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=CommonBehavior_SimpleTime_TimeExpression)
gen_CommonBehavior_SimpleTime_DurationObservation_Observation = Generalization(general=Observation, specific=CommonBehavior_SimpleTime_DurationObservation)
gen_CommonBehavior_SimpleTime_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=CommonBehavior_SimpleTime_Duration)
gen_CommonBehavior_SimpleTime_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=CommonBehavior_SimpleTime_Interval)
gen_CommonBehavior_SimpleTime_TimeInterval_Interval = Generalization(general=Interval, specific=CommonBehavior_SimpleTime_TimeInterval)
gen_CommonBehavior_SimpleTime_DurationInterval_Interval = Generalization(general=Interval, specific=CommonBehavior_SimpleTime_DurationInterval)
gen_CommonBehavior_SimpleTime_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=CommonBehavior_SimpleTime_IntervalConstraint)
gen_CommonBehavior_SimpleTime_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CommonBehavior_SimpleTime_TimeConstraint)
gen_CommonBehavior_SimpleTime_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CommonBehavior_SimpleTime_DurationConstraint)

# Domain Model
domain_model = DomainModel(
    name="CommonBehavior",
    types={CommonBehavior_BasicBehavior_BehavioredClassifier, Classifier, CommonBehavior_BasicBehavior_FunctionBehavior, OpaqueBehavior, CommonBehavior_BasicBehavior_BehavioralFeature, Behavior, CommonBehavior_BasicBehavior_Classifier, RedefinableElement, CommonBehavior_BasicBehavior_Class, BasicBehavior_Classifier, BasicBehavior_BehavioredClassifier, Reception, CommonBehavior_BasicBehavior_Behavior, Class_, BehavioredClassifier, BehavioralFeature, Parameter_, Constraint, CommonBehavior_BasicBehavior_RedefinableElement, CommonBehavior_BasicBehavior_OpaqueBehavior, Signal, CommonBehavior_Communications_Interface, CommonBehavior_BasicBehavior_Parameter, CommonBehavior_BasicBehavior_OpaqueExpression, CommonBehavior_BasicBehavior_Constraint, CommonBehavior_Communications_Signal, Property_, CommonBehavior_Communications_Property, CommonBehavior_Communications_Reception, Observation, CommonBehavior_SimpleTime_Observation, CommonBehavior_SimpleTime_TimeObservation, CommonBehavior_Communications_NamedElement, CommonBehavior_Communications_Trigger, NamedElement, Event, CommonBehavior_Communications_PackageableElement, CommonBehavior_Communications_Event, PackageableElement, CommonBehavior_Communications_MessageEvent, CommonBehavior_Communications_AnyReceiveEvent, MessageEvent, CommonBehavior_Communications_SignalEvent, CommonBehavior_Communications_CallEvent, Operation, CommonBehavior_Communications_Operation, CommonBehavior_Communications_ChangeEvent, ValueSpecification, CommonBehavior_Communications_ValueSpecification, CommonBehavior_SimpleTime_TimeEvent, TimeExpression, CommonBehavior_SimpleTime_TimeExpression, DurationInterval, CommonBehavior_SimpleTime_DurationObservation, CommonBehavior_SimpleTime_Duration, CommonBehavior_SimpleTime_Interval, CommonBehavior_SimpleTime_TimeInterval, Interval, CommonBehavior_SimpleTime_DurationInterval, Duration, CommonBehavior_SimpleTime_IntervalConstraint, CommonBehavior_SimpleTime_TimeConstraint, IntervalConstraint, TimeInterval, CommonBehavior_SimpleTime_DurationConstraint, CallConcurrencyFeature},
    associations={ownedBehavior0, classifierBehavior1, ownedReception4, context5, redefinedBehavior6, specification9, ownedParameter10, precondition12, postcondition14, signal25, method17, result19, behavior21, ownedAttribute24, observation36, ownedReception26, event28, signal29, operation31, changeExpression32, when33, expr34, durationSpecification61, event38, event39, expr41, observation43, max46, min48, timeMax51, timeMin53, durationMax56, durationMin57, timeSpecification60},
    generalizations={gen_CommonBehavior_BasicBehavior_BehavioredClassifier_Classifier, gen_CommonBehavior_BasicBehavior_FunctionBehavior_OpaqueBehavior, gen_CommonBehavior_BasicBehavior_Classifier_RedefinableElement, gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_Classifier, gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_BehavioredClassifier, gen_CommonBehavior_BasicBehavior_Behavior_Class, gen_CommonBehavior_BasicBehavior_OpaqueBehavior_Behavior, gen_CommonBehavior_Communications_Interface_Classifier, gen_CommonBehavior_Communications_Signal_Classifier, gen_CommonBehavior_Communications_Reception_BehavioralFeature, gen_CommonBehavior_SimpleTime_Observation_PackageableElement, gen_CommonBehavior_SimpleTime_TimeObservation_Observation, gen_CommonBehavior_Communications_Trigger_NamedElement, gen_CommonBehavior_Communications_Event_PackageableElement, gen_CommonBehavior_Communications_MessageEvent_Event, gen_CommonBehavior_Communications_AnyReceiveEvent_MessageEvent, gen_CommonBehavior_Communications_SignalEvent_MessageEvent, gen_CommonBehavior_Communications_CallEvent_MessageEvent, gen_CommonBehavior_Communications_ChangeEvent_Event, gen_CommonBehavior_SimpleTime_TimeExpression_ValueSpecification, gen_CommonBehavior_SimpleTime_DurationObservation_Observation, gen_CommonBehavior_SimpleTime_Duration_ValueSpecification, gen_CommonBehavior_SimpleTime_Interval_ValueSpecification, gen_CommonBehavior_SimpleTime_TimeInterval_Interval, gen_CommonBehavior_SimpleTime_DurationInterval_Interval, gen_CommonBehavior_SimpleTime_IntervalConstraint_Constraint, gen_CommonBehavior_SimpleTime_TimeConstraint_IntervalConstraint, gen_CommonBehavior_SimpleTime_DurationConstraint_IntervalConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)