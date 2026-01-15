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
Behavior = Class(name="Behavior")
CommonBehavior_BasicBehavior_Classifier = Class(name="CommonBehavior::BasicBehavior::Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
CommonBehavior_BasicBehavior_Class = Class(name="CommonBehavior::BasicBehavior::Class", is_abstract=True)
BasicBehavior_Classifier = Class(name="BasicBehavior::Classifier")
BasicBehavior_BehavioredClassifier = Class(name="BasicBehavior::BehavioredClassifier")
CommonBehavior_BasicBehavior_BehavioredClassifier = Class(name="CommonBehavior::BasicBehavior::BehavioredClassifier")
Classifier = Class(name="Classifier")
CommonBehavior_BasicBehavior_Behavior = Class(name="CommonBehavior::BasicBehavior::Behavior", is_abstract=True)
Class_ = Class(name="Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
BehavioralFeature = Class(name="BehavioralFeature")
Parameter_ = Class(name="Parameter")
Reception = Class(name="Reception")
CommonBehavior_BasicBehavior_RedefinableElement = Class(name="CommonBehavior::BasicBehavior::RedefinableElement", is_abstract=True)
CommonBehavior_BasicBehavior_OpaqueBehavior = Class(name="CommonBehavior::BasicBehavior::OpaqueBehavior")
CommonBehavior_BasicBehavior_FunctionBehavior = Class(name="CommonBehavior::BasicBehavior::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
CommonBehavior_BasicBehavior_BehavioralFeature = Class(name="CommonBehavior::BasicBehavior::BehavioralFeature", is_abstract=True)
Constraint = Class(name="Constraint")
CommonBehavior_BasicBehavior_OpaqueExpression = Class(name="CommonBehavior::BasicBehavior::OpaqueExpression")
CommonBehavior_BasicBehavior_Constraint = Class(name="CommonBehavior::BasicBehavior::Constraint")
CommonBehavior_Communications_Signal = Class(name="CommonBehavior::Communications::Signal")
Property_ = Class(name="Property")
CommonBehavior_BasicBehavior_Parameter = Class(name="CommonBehavior::BasicBehavior::Parameter")
CommonBehavior_Communications_Interface = Class(name="CommonBehavior::Communications::Interface")
CommonBehavior_Communications_NamedElement = Class(name="CommonBehavior::Communications::NamedElement", is_abstract=True)
CommonBehavior_Communications_Trigger = Class(name="CommonBehavior::Communications::Trigger")
NamedElement = Class(name="NamedElement")
CommonBehavior_Communications_Property = Class(name="CommonBehavior::Communications::Property")
CommonBehavior_Communications_Reception = Class(name="CommonBehavior::Communications::Reception")
Signal = Class(name="Signal")
CommonBehavior_Communications_Event = Class(name="CommonBehavior::Communications::Event", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
CommonBehavior_Communications_MessageEvent = Class(name="CommonBehavior::Communications::MessageEvent", is_abstract=True)
CommonBehavior_Communications_AnyReceiveEvent = Class(name="CommonBehavior::Communications::AnyReceiveEvent")
MessageEvent = Class(name="MessageEvent")
CommonBehavior_Communications_SignalEvent = Class(name="CommonBehavior::Communications::SignalEvent")
CommonBehavior_Communications_CallEvent = Class(name="CommonBehavior::Communications::CallEvent")
Operation = Class(name="Operation")
Event = Class(name="Event")
CommonBehavior_Communications_PackageableElement = Class(name="CommonBehavior::Communications::PackageableElement", is_abstract=True)
CommonBehavior_Communications_ValueSpecification = Class(name="CommonBehavior::Communications::ValueSpecification", is_abstract=True)
CommonBehavior_SimpleTime_TimeEvent = Class(name="CommonBehavior::SimpleTime::TimeEvent")
TimeExpression = Class(name="TimeExpression")
CommonBehavior_SimpleTime_TimeExpression = Class(name="CommonBehavior::SimpleTime::TimeExpression")
CommonBehavior_Communications_Operation = Class(name="CommonBehavior::Communications::Operation")
CommonBehavior_Communications_ChangeEvent = Class(name="CommonBehavior::Communications::ChangeEvent")
ValueSpecification = Class(name="ValueSpecification")
CommonBehavior_SimpleTime_TimeObservation = Class(name="CommonBehavior::SimpleTime::TimeObservation")
CommonBehavior_SimpleTime_DurationObservation = Class(name="CommonBehavior::SimpleTime::DurationObservation")
Observation = Class(name="Observation")
CommonBehavior_SimpleTime_Observation = Class(name="CommonBehavior::SimpleTime::Observation", is_abstract=True)
CommonBehavior_SimpleTime_Interval = Class(name="CommonBehavior::SimpleTime::Interval")
CommonBehavior_SimpleTime_TimeInterval = Class(name="CommonBehavior::SimpleTime::TimeInterval")
Interval = Class(name="Interval")
CommonBehavior_SimpleTime_Duration = Class(name="CommonBehavior::SimpleTime::Duration")
CommonBehavior_SimpleTime_DurationInterval = Class(name="CommonBehavior::SimpleTime::DurationInterval")
Duration = Class(name="Duration")
CommonBehavior_SimpleTime_IntervalConstraint = Class(name="CommonBehavior::SimpleTime::IntervalConstraint")
CommonBehavior_SimpleTime_TimeConstraint = Class(name="CommonBehavior::SimpleTime::TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
TimeInterval = Class(name="TimeInterval")
CommonBehavior_SimpleTime_DurationConstraint = Class(name="CommonBehavior::SimpleTime::DurationConstraint")
DurationInterval = Class(name="DurationInterval")

# Behavior class attributes and methods

# CommonBehavior_BasicBehavior_Classifier class attributes and methods

# RedefinableElement class attributes and methods

# CommonBehavior_BasicBehavior_Class class attributes and methods

# BasicBehavior_Classifier class attributes and methods

# BasicBehavior_BehavioredClassifier class attributes and methods

# CommonBehavior_BasicBehavior_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# CommonBehavior_BasicBehavior_Behavior class attributes and methods
CommonBehavior_BasicBehavior_Behavior_isReentrant: Property = Property(name="isReentrant", type=BooleanType)
CommonBehavior_BasicBehavior_Behavior.attributes={CommonBehavior_BasicBehavior_Behavior_isReentrant}

# Class class attributes and methods

# BehavioredClassifier class attributes and methods

# BehavioralFeature class attributes and methods

# Parameter class attributes and methods

# Reception class attributes and methods

# CommonBehavior_BasicBehavior_RedefinableElement class attributes and methods

# CommonBehavior_BasicBehavior_OpaqueBehavior class attributes and methods
CommonBehavior_BasicBehavior_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
CommonBehavior_BasicBehavior_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
CommonBehavior_BasicBehavior_OpaqueBehavior.attributes={CommonBehavior_BasicBehavior_OpaqueBehavior_language, CommonBehavior_BasicBehavior_OpaqueBehavior_body}

# CommonBehavior_BasicBehavior_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# CommonBehavior_BasicBehavior_BehavioralFeature class attributes and methods
CommonBehavior_BasicBehavior_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
CommonBehavior_BasicBehavior_BehavioralFeature.attributes={CommonBehavior_BasicBehavior_BehavioralFeature_concurrency}

# Constraint class attributes and methods

# CommonBehavior_BasicBehavior_OpaqueExpression class attributes and methods

# CommonBehavior_BasicBehavior_Constraint class attributes and methods

# CommonBehavior_Communications_Signal class attributes and methods

# Property class attributes and methods

# CommonBehavior_BasicBehavior_Parameter class attributes and methods

# CommonBehavior_Communications_Interface class attributes and methods

# CommonBehavior_Communications_NamedElement class attributes and methods

# CommonBehavior_Communications_Trigger class attributes and methods

# NamedElement class attributes and methods

# CommonBehavior_Communications_Property class attributes and methods

# CommonBehavior_Communications_Reception class attributes and methods

# Signal class attributes and methods

# CommonBehavior_Communications_Event class attributes and methods

# PackageableElement class attributes and methods

# CommonBehavior_Communications_MessageEvent class attributes and methods

# CommonBehavior_Communications_AnyReceiveEvent class attributes and methods

# MessageEvent class attributes and methods

# CommonBehavior_Communications_SignalEvent class attributes and methods

# CommonBehavior_Communications_CallEvent class attributes and methods

# Operation class attributes and methods

# Event class attributes and methods

# CommonBehavior_Communications_PackageableElement class attributes and methods

# CommonBehavior_Communications_ValueSpecification class attributes and methods

# CommonBehavior_SimpleTime_TimeEvent class attributes and methods
CommonBehavior_SimpleTime_TimeEvent_isRelative: Property = Property(name="isRelative", type=BooleanType)
CommonBehavior_SimpleTime_TimeEvent.attributes={CommonBehavior_SimpleTime_TimeEvent_isRelative}

# TimeExpression class attributes and methods

# CommonBehavior_SimpleTime_TimeExpression class attributes and methods

# CommonBehavior_Communications_Operation class attributes and methods

# CommonBehavior_Communications_ChangeEvent class attributes and methods

# ValueSpecification class attributes and methods

# CommonBehavior_SimpleTime_TimeObservation class attributes and methods
CommonBehavior_SimpleTime_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CommonBehavior_SimpleTime_TimeObservation.attributes={CommonBehavior_SimpleTime_TimeObservation_firstEvent}

# CommonBehavior_SimpleTime_DurationObservation class attributes and methods
CommonBehavior_SimpleTime_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CommonBehavior_SimpleTime_DurationObservation.attributes={CommonBehavior_SimpleTime_DurationObservation_firstEvent}

# Observation class attributes and methods

# CommonBehavior_SimpleTime_Observation class attributes and methods

# CommonBehavior_SimpleTime_Interval class attributes and methods

# CommonBehavior_SimpleTime_TimeInterval class attributes and methods

# Interval class attributes and methods

# CommonBehavior_SimpleTime_Duration class attributes and methods

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

# DurationInterval class attributes and methods

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
        Property(name="10", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedReception4: BinaryAssociation = BinaryAssociation(
    name="ownedReception4",
    ends={
        Property(name="Reception", type=CommonBehavior_BasicBehavior_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Class", type=Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition15: BinaryAssociation = BinaryAssociation(
    name="postcondition15",
    ends={
        Property(name="Constraint17", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior16", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter11: BinaryAssociation = BinaryAssociation(
    name="ownedParameter11",
    ends={
        Property(name="Parameter", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior12", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition13: BinaryAssociation = BinaryAssociation(
    name="precondition13",
    ends={
        Property(name="Constraint", type=CommonBehavior_BasicBehavior_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_Behavior14", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result21: BinaryAssociation = BinaryAssociation(
    name="result21",
    ends={
        Property(name="Parameter22", type=CommonBehavior_BasicBehavior_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_OpaqueExpression", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
behavior23: BinaryAssociation = BinaryAssociation(
    name="behavior23",
    ends={
        Property(name="Behavior25", type=CommonBehavior_BasicBehavior_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_BasicBehavior_OpaqueExpression24", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute26: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute26",
    ends={
        Property(name="Property", type=CommonBehavior_Communications_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Signal", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method18: BinaryAssociation = BinaryAssociation(
    name="method18",
    ends={
        Property(name="20", type=CommonBehavior_BasicBehavior_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
signal27: BinaryAssociation = BinaryAssociation(
    name="signal27",
    ends={
        Property(name="CommonBehavior_Communications_Reception", type=Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="Signal", type=CommonBehavior_Communications_Reception, multiplicity=Multiplicity(1, 1))
    }
)
ownedReception28: BinaryAssociation = BinaryAssociation(
    name="ownedReception28",
    ends={
        Property(name="Reception29", type=CommonBehavior_Communications_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Interface", type=Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal31: BinaryAssociation = BinaryAssociation(
    name="signal31",
    ends={
        Property(name="Signal32", type=CommonBehavior_Communications_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_SignalEvent", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation33: BinaryAssociation = BinaryAssociation(
    name="operation33",
    ends={
        Property(name="Operation", type=CommonBehavior_Communications_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_CallEvent", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
event30: BinaryAssociation = BinaryAssociation(
    name="event30",
    ends={
        Property(name="Event", type=CommonBehavior_Communications_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_Communications_Trigger", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression34: BinaryAssociation = BinaryAssociation(
    name="changeExpression34",
    ends={
        Property(name="CommonBehavior_Communications_ChangeEvent", type=ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ValueSpecification", type=CommonBehavior_Communications_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
when35: BinaryAssociation = BinaryAssociation(
    name="when35",
    ends={
        Property(name="TimeExpression", type=CommonBehavior_SimpleTime_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeEvent", type=TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
event40: BinaryAssociation = BinaryAssociation(
    name="event40",
    ends={
        Property(name="NamedElement", type=CommonBehavior_SimpleTime_TimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeObservation", type=NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
event41: BinaryAssociation = BinaryAssociation(
    name="event41",
    ends={
        Property(name="NamedElement42", type=CommonBehavior_SimpleTime_DurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationObservation", type=NamedElement, multiplicity=Multiplicity(1, 2))
    }
)
expr36: BinaryAssociation = BinaryAssociation(
    name="expr36",
    ends={
        Property(name="ValueSpecification37", type=CommonBehavior_SimpleTime_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeExpression", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation38: BinaryAssociation = BinaryAssociation(
    name="observation38",
    ends={
        Property(name="Observation", type=CommonBehavior_SimpleTime_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeExpression39", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
observation45: BinaryAssociation = BinaryAssociation(
    name="observation45",
    ends={
        Property(name="Observation47", type=CommonBehavior_SimpleTime_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Duration46", type=Observation, multiplicity=Multiplicity(0, 9999))
    }
)
max48: BinaryAssociation = BinaryAssociation(
    name="max48",
    ends={
        Property(name="ValueSpecification49", type=CommonBehavior_SimpleTime_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Interval", type=ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
min50: BinaryAssociation = BinaryAssociation(
    name="min50",
    ends={
        Property(name="ValueSpecification52", type=CommonBehavior_SimpleTime_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Interval51", type=ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
expr43: BinaryAssociation = BinaryAssociation(
    name="expr43",
    ends={
        Property(name="ValueSpecification44", type=CommonBehavior_SimpleTime_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_Duration", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
durationMax58: BinaryAssociation = BinaryAssociation(
    name="durationMax58",
    ends={
        Property(name="Duration", type=CommonBehavior_SimpleTime_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationInterval", type=Duration, multiplicity=Multiplicity(1, 1))
    }
)
durationMin59: BinaryAssociation = BinaryAssociation(
    name="durationMin59",
    ends={
        Property(name="Duration61", type=CommonBehavior_SimpleTime_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationInterval60", type=Duration, multiplicity=Multiplicity(1, 1))
    }
)
timeSpecification62: BinaryAssociation = BinaryAssociation(
    name="timeSpecification62",
    ends={
        Property(name="TimeInterval", type=CommonBehavior_SimpleTime_TimeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeConstraint", type=TimeInterval, multiplicity=Multiplicity(1, 1))
    }
)
timeMax53: BinaryAssociation = BinaryAssociation(
    name="timeMax53",
    ends={
        Property(name="TimeExpression54", type=CommonBehavior_SimpleTime_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeInterval", type=TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
timeMin55: BinaryAssociation = BinaryAssociation(
    name="timeMin55",
    ends={
        Property(name="TimeExpression57", type=CommonBehavior_SimpleTime_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_TimeInterval56", type=TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
durationSpecification63: BinaryAssociation = BinaryAssociation(
    name="durationSpecification63",
    ends={
        Property(name="DurationInterval", type=CommonBehavior_SimpleTime_DurationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehavior_SimpleTime_DurationConstraint", type=DurationInterval, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CommonBehavior_BasicBehavior_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=CommonBehavior_BasicBehavior_Classifier)
gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_Classifier = Generalization(general=BasicBehavior_Classifier, specific=CommonBehavior_BasicBehavior_Class)
gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_BehavioredClassifier = Generalization(general=BasicBehavior_BehavioredClassifier, specific=CommonBehavior_BasicBehavior_Class)
gen_CommonBehavior_BasicBehavior_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=CommonBehavior_BasicBehavior_BehavioredClassifier)
gen_CommonBehavior_BasicBehavior_Behavior_Class = Generalization(general=Class_, specific=CommonBehavior_BasicBehavior_Behavior)
gen_CommonBehavior_BasicBehavior_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=CommonBehavior_BasicBehavior_OpaqueBehavior)
gen_CommonBehavior_BasicBehavior_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=CommonBehavior_BasicBehavior_FunctionBehavior)
gen_CommonBehavior_Communications_Signal_Classifier = Generalization(general=Classifier, specific=CommonBehavior_Communications_Signal)
gen_CommonBehavior_Communications_Interface_Classifier = Generalization(general=Classifier, specific=CommonBehavior_Communications_Interface)
gen_CommonBehavior_Communications_Trigger_NamedElement = Generalization(general=NamedElement, specific=CommonBehavior_Communications_Trigger)
gen_CommonBehavior_Communications_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=CommonBehavior_Communications_Reception)
gen_CommonBehavior_Communications_Event_PackageableElement = Generalization(general=PackageableElement, specific=CommonBehavior_Communications_Event)
gen_CommonBehavior_Communications_MessageEvent_Event = Generalization(general=Event, specific=CommonBehavior_Communications_MessageEvent)
gen_CommonBehavior_Communications_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=CommonBehavior_Communications_AnyReceiveEvent)
gen_CommonBehavior_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=CommonBehavior_Communications_SignalEvent)
gen_CommonBehavior_Communications_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=CommonBehavior_Communications_CallEvent)
gen_CommonBehavior_SimpleTime_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=CommonBehavior_SimpleTime_TimeExpression)
gen_CommonBehavior_Communications_ChangeEvent_Event = Generalization(general=Event, specific=CommonBehavior_Communications_ChangeEvent)
gen_CommonBehavior_SimpleTime_TimeObservation_Observation = Generalization(general=Observation, specific=CommonBehavior_SimpleTime_TimeObservation)
gen_CommonBehavior_SimpleTime_DurationObservation_Observation = Generalization(general=Observation, specific=CommonBehavior_SimpleTime_DurationObservation)
gen_CommonBehavior_SimpleTime_Observation_PackageableElement = Generalization(general=PackageableElement, specific=CommonBehavior_SimpleTime_Observation)
gen_CommonBehavior_SimpleTime_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=CommonBehavior_SimpleTime_Interval)
gen_CommonBehavior_SimpleTime_TimeInterval_Interval = Generalization(general=Interval, specific=CommonBehavior_SimpleTime_TimeInterval)
gen_CommonBehavior_SimpleTime_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=CommonBehavior_SimpleTime_Duration)
gen_CommonBehavior_SimpleTime_DurationInterval_Interval = Generalization(general=Interval, specific=CommonBehavior_SimpleTime_DurationInterval)
gen_CommonBehavior_SimpleTime_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=CommonBehavior_SimpleTime_IntervalConstraint)
gen_CommonBehavior_SimpleTime_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CommonBehavior_SimpleTime_TimeConstraint)
gen_CommonBehavior_SimpleTime_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CommonBehavior_SimpleTime_DurationConstraint)

# Domain Model
domain_model = DomainModel(
    name="CommonBehavior",
    types={Behavior, CommonBehavior_BasicBehavior_Classifier, RedefinableElement, CommonBehavior_BasicBehavior_Class, BasicBehavior_Classifier, BasicBehavior_BehavioredClassifier, CommonBehavior_BasicBehavior_BehavioredClassifier, Classifier, CommonBehavior_BasicBehavior_Behavior, Class_, BehavioredClassifier, BehavioralFeature, Parameter_, Reception, CommonBehavior_BasicBehavior_RedefinableElement, CommonBehavior_BasicBehavior_OpaqueBehavior, CommonBehavior_BasicBehavior_FunctionBehavior, OpaqueBehavior, CommonBehavior_BasicBehavior_BehavioralFeature, Constraint, CommonBehavior_BasicBehavior_OpaqueExpression, CommonBehavior_BasicBehavior_Constraint, CommonBehavior_Communications_Signal, Property_, CommonBehavior_BasicBehavior_Parameter, CommonBehavior_Communications_Interface, CommonBehavior_Communications_NamedElement, CommonBehavior_Communications_Trigger, NamedElement, CommonBehavior_Communications_Property, CommonBehavior_Communications_Reception, Signal, CommonBehavior_Communications_Event, PackageableElement, CommonBehavior_Communications_MessageEvent, CommonBehavior_Communications_AnyReceiveEvent, MessageEvent, CommonBehavior_Communications_SignalEvent, CommonBehavior_Communications_CallEvent, Operation, Event, CommonBehavior_Communications_PackageableElement, CommonBehavior_Communications_ValueSpecification, CommonBehavior_SimpleTime_TimeEvent, TimeExpression, CommonBehavior_SimpleTime_TimeExpression, CommonBehavior_Communications_Operation, CommonBehavior_Communications_ChangeEvent, ValueSpecification, CommonBehavior_SimpleTime_TimeObservation, CommonBehavior_SimpleTime_DurationObservation, Observation, CommonBehavior_SimpleTime_Observation, CommonBehavior_SimpleTime_Interval, CommonBehavior_SimpleTime_TimeInterval, Interval, CommonBehavior_SimpleTime_Duration, CommonBehavior_SimpleTime_DurationInterval, Duration, CommonBehavior_SimpleTime_IntervalConstraint, CommonBehavior_SimpleTime_TimeConstraint, IntervalConstraint, TimeInterval, CommonBehavior_SimpleTime_DurationConstraint, DurationInterval, CallConcurrencyFeature},
    associations={ownedBehavior0, classifierBehavior1, context5, redefinedBehavior6, specification9, ownedReception4, postcondition15, ownedParameter11, precondition13, result21, behavior23, ownedAttribute26, method18, signal27, ownedReception28, signal31, operation33, event30, changeExpression34, when35, event40, event41, expr36, observation38, observation45, max48, min50, expr43, durationMax58, durationMin59, timeSpecification62, timeMax53, timeMin55, durationSpecification63},
    generalizations={gen_CommonBehavior_BasicBehavior_Classifier_RedefinableElement, gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_Classifier, gen_CommonBehavior_BasicBehavior_Class_BasicBehavior_BehavioredClassifier, gen_CommonBehavior_BasicBehavior_BehavioredClassifier_Classifier, gen_CommonBehavior_BasicBehavior_Behavior_Class, gen_CommonBehavior_BasicBehavior_OpaqueBehavior_Behavior, gen_CommonBehavior_BasicBehavior_FunctionBehavior_OpaqueBehavior, gen_CommonBehavior_Communications_Signal_Classifier, gen_CommonBehavior_Communications_Interface_Classifier, gen_CommonBehavior_Communications_Trigger_NamedElement, gen_CommonBehavior_Communications_Reception_BehavioralFeature, gen_CommonBehavior_Communications_Event_PackageableElement, gen_CommonBehavior_Communications_MessageEvent_Event, gen_CommonBehavior_Communications_AnyReceiveEvent_MessageEvent, gen_CommonBehavior_Communications_SignalEvent_MessageEvent, gen_CommonBehavior_Communications_CallEvent_MessageEvent, gen_CommonBehavior_SimpleTime_TimeExpression_ValueSpecification, gen_CommonBehavior_Communications_ChangeEvent_Event, gen_CommonBehavior_SimpleTime_TimeObservation_Observation, gen_CommonBehavior_SimpleTime_DurationObservation_Observation, gen_CommonBehavior_SimpleTime_Observation_PackageableElement, gen_CommonBehavior_SimpleTime_Interval_ValueSpecification, gen_CommonBehavior_SimpleTime_TimeInterval_Interval, gen_CommonBehavior_SimpleTime_Duration_ValueSpecification, gen_CommonBehavior_SimpleTime_DurationInterval_Interval, gen_CommonBehavior_SimpleTime_IntervalConstraint_Constraint, gen_CommonBehavior_SimpleTime_TimeConstraint_IntervalConstraint, gen_CommonBehavior_SimpleTime_DurationConstraint_IntervalConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)