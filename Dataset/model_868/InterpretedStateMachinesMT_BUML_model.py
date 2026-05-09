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
PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="entrypoint"),
			EnumerationLiteral(name="exitpoint")
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

# Classes
statemachines_CustomSystem = Class(name="statemachines_CustomSystem")
statemachines_StateMachine = Class(name="statemachines_StateMachine")
statemachines_Signal = Class(name="statemachines_Signal")
statemachines_Operation = Class(name="statemachines_Operation")
NamedElement = Class(name="NamedElement")
statemachines_Attribute = Class(name="statemachines_Attribute", is_abstract=True)
statemachines_EventType = Class(name="statemachines_EventType", is_abstract=True)
statemachines_SignalEventType = Class(name="statemachines_SignalEventType")
EventType = Class(name="EventType")
statemachines_CallEventType = Class(name="statemachines_CallEventType")
statemachines_BooleanAttribute = Class(name="statemachines_BooleanAttribute")
Attribute = Class(name="Attribute")
statemachines_IntegerAttribute = Class(name="statemachines_IntegerAttribute")
statemachines_StringAttribute = Class(name="statemachines_StringAttribute")
statemachines_Constraint = Class(name="statemachines_Constraint", is_abstract=True)
statemachines_BooleanConstraint = Class(name="statemachines_BooleanConstraint")
statemachines_IntegerConstraint = Class(name="statemachines_IntegerConstraint")
statemachines_StringConstraint = Class(name="statemachines_StringConstraint")
statemachines_NamedElement = Class(name="statemachines_NamedElement", is_abstract=True)
statemachines_Region = Class(name="statemachines_Region")
statemachines_Vertex = Class(name="statemachines_Vertex")
statemachines_Transition = Class(name="statemachines_Transition")
statemachines_FinalState = Class(name="statemachines_FinalState")
State = Class(name="State")
statemachines_State = Class(name="statemachines_State")
statemachines_Pseudostate = Class(name="statemachines_Pseudostate")
Vertex = Class(name="Vertex")
statemachines_Behavior = Class(name="statemachines_Behavior")
statemachines_Trigger = Class(name="statemachines_Trigger")
statemachines_SignalEventOccurrence = Class(name="statemachines_SignalEventOccurrence")
statemachines_OperationBehavior = Class(name="statemachines_OperationBehavior")
Behavior = Class(name="Behavior")
statemachines_AttributeValue = Class(name="statemachines_AttributeValue", is_abstract=True)
statemachines_BooleanAttributeValue = Class(name="statemachines_BooleanAttributeValue")
AttributeValue = Class(name="AttributeValue")
statemachines_IntegerAttributeValue = Class(name="statemachines_IntegerAttributeValue")
statemachines_StringAttributeValue = Class(name="statemachines_StringAttributeValue")
statemachines_EventOccurrence = Class(name="statemachines_EventOccurrence")
statemachines_CallEventOccurrence = Class(name="statemachines_CallEventOccurrence")
statemachines_CompletionEventOccurrence = Class(name="statemachines_CompletionEventOccurrence")
EventOccurrence = Class(name="EventOccurrence")

# statemachines_CustomSystem class attributes and methods

# statemachines_StateMachine class attributes and methods
statemachines_StateMachine_m_run: Method = Method(name="run", parameters={})
statemachines_StateMachine_m_eventOccurrenceReceived: Method = Method(name="eventOccurrenceReceived", parameters={Parameter(name='statemachines_event', type=StringType)})
statemachines_StateMachine.methods={statemachines_StateMachine_m_eventOccurrenceReceived, statemachines_StateMachine_m_run}

# statemachines_Signal class attributes and methods

# statemachines_Operation class attributes and methods

# NamedElement class attributes and methods

# statemachines_Attribute class attributes and methods

# statemachines_EventType class attributes and methods

# statemachines_SignalEventType class attributes and methods

# EventType class attributes and methods

# statemachines_CallEventType class attributes and methods

# statemachines_BooleanAttribute class attributes and methods

# Attribute class attributes and methods

# statemachines_IntegerAttribute class attributes and methods

# statemachines_StringAttribute class attributes and methods

# statemachines_Constraint class attributes and methods
statemachines_Constraint_value: Property = Property(name="value", type=StringType)
statemachines_Constraint.attributes={statemachines_Constraint_value}

# statemachines_BooleanConstraint class attributes and methods

# statemachines_IntegerConstraint class attributes and methods

# statemachines_StringConstraint class attributes and methods

# statemachines_NamedElement class attributes and methods
statemachines_NamedElement_name: Property = Property(name="name", type=StringType)
statemachines_NamedElement.attributes={statemachines_NamedElement_name}

# statemachines_Region class attributes and methods

# statemachines_Vertex class attributes and methods

# statemachines_Transition class attributes and methods
statemachines_Transition_kind: Property = Property(name="kind", type=StringType)
statemachines_Transition_m_fire: Method = Method(name="fire", parameters={Parameter(name='statemachines_eventOccurrence', type=StringType)})
statemachines_Transition.attributes={statemachines_Transition_kind}
statemachines_Transition.methods={statemachines_Transition_m_fire}

# statemachines_FinalState class attributes and methods

# State class attributes and methods

# statemachines_State class attributes and methods
statemachines_State_isEntryCompleted: Property = Property(name="isEntryCompleted", type=BooleanType)
statemachines_State_isDoActivityCompleted: Property = Property(name="isDoActivityCompleted", type=BooleanType)
statemachines_State_isExitCompleted: Property = Property(name="isExitCompleted", type=BooleanType)
statemachines_State.attributes={statemachines_State_isExitCompleted, statemachines_State_isEntryCompleted, statemachines_State_isDoActivityCompleted}

# statemachines_Pseudostate class attributes and methods
statemachines_Pseudostate_kind: Property = Property(name="kind", type=StringType)
statemachines_Pseudostate.attributes={statemachines_Pseudostate_kind}

# Vertex class attributes and methods

# statemachines_Behavior class attributes and methods

# statemachines_Trigger class attributes and methods

# statemachines_SignalEventOccurrence class attributes and methods

# statemachines_OperationBehavior class attributes and methods

# Behavior class attributes and methods

# statemachines_AttributeValue class attributes and methods

# statemachines_BooleanAttributeValue class attributes and methods
statemachines_BooleanAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_BooleanAttributeValue.attributes={statemachines_BooleanAttributeValue_value}

# AttributeValue class attributes and methods

# statemachines_IntegerAttributeValue class attributes and methods
statemachines_IntegerAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_IntegerAttributeValue.attributes={statemachines_IntegerAttributeValue_value}

# statemachines_StringAttributeValue class attributes and methods
statemachines_StringAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_StringAttributeValue.attributes={statemachines_StringAttributeValue_value}

# statemachines_EventOccurrence class attributes and methods

# statemachines_CallEventOccurrence class attributes and methods

# statemachines_CompletionEventOccurrence class attributes and methods

# EventOccurrence class attributes and methods

# Relationships
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="statemachines_StateMachine", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signals1: BinaryAssociation = BinaryAssociation(
    name="signals1",
    ends={
        Property(name="statemachines_Signal", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem2", type=statemachines_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations3: BinaryAssociation = BinaryAssociation(
    name="operations3",
    ends={
        Property(name="statemachines_Operation", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CustomSystem4", type=statemachines_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="statemachines_Attribute", type=statemachines_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Signal6", type=statemachines_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inParameters7: BinaryAssociation = BinaryAssociation(
    name="inParameters7",
    ends={
        Property(name="statemachines_Attribute9", type=statemachines_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Operation8", type=statemachines_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParameters10: BinaryAssociation = BinaryAssociation(
    name="outParameters10",
    ends={
        Property(name="statemachines_Attribute12", type=statemachines_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Operation11", type=statemachines_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal16: BinaryAssociation = BinaryAssociation(
    name="signal16",
    ends={
        Property(name="statemachines_Signal17", type=statemachines_SignalEventType, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventType", type=statemachines_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation18: BinaryAssociation = BinaryAssociation(
    name="operation18",
    ends={
        Property(name="statemachines_Operation19", type=statemachines_CallEventType, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventType", type=statemachines_Operation, multiplicity=Multiplicity(1, 1))
    }
)
regions20: BinaryAssociation = BinaryAssociation(
    name="regions20",
    ends={
        Property(name="Region", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=statemachines_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
return_13: BinaryAssociation = BinaryAssociation(
    name="return_13",
    ends={
        Property(name="statemachines_Attribute15", type=statemachines_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Operation14", type=statemachines_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions22: BinaryAssociation = BinaryAssociation(
    name="transitions22",
    ends={
        Property(name="Transition", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container23", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine24: BinaryAssociation = BinaryAssociation(
    name="stateMachine24",
    ends={
        Property(name="StateMachine", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="regions", type=statemachines_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state25: BinaryAssociation = BinaryAssociation(
    name="state25",
    ends={
        Property(name="State", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="regions26", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
source49: BinaryAssociation = BinaryAssociation(
    name="source49",
    ends={
        Property(name="Vertex50", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
currentVertex27: BinaryAssociation = BinaryAssociation(
    name="currentVertex27",
    ends={
        Property(name="statemachines_Vertex", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Region", type=statemachines_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
target51: BinaryAssociation = BinaryAssociation(
    name="target51",
    ends={
        Property(name="Vertex52", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
container28: BinaryAssociation = BinaryAssociation(
    name="container28",
    ends={
        Property(name="Region29", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertice", type=statemachines_Region, multiplicity=Multiplicity(0, 1))
    }
)
triggers53: BinaryAssociation = BinaryAssociation(
    name="triggers53",
    ends={
        Property(name="statemachines_Trigger54", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition", type=statemachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions30: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions30",
    ends={
        Property(name="Transition31", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions32: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions32",
    ends={
        Property(name="Transition33", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
state34: BinaryAssociation = BinaryAssociation(
    name="state34",
    ends={
        Property(name="State35", type=statemachines_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
regions36: BinaryAssociation = BinaryAssociation(
    name="regions36",
    ends={
        Property(name="Region37", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=statemachines_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry38: BinaryAssociation = BinaryAssociation(
    name="entry38",
    ends={
        Property(name="statemachines_Behavior", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity39: BinaryAssociation = BinaryAssociation(
    name="doActivity39",
    ends={
        Property(name="statemachines_Behavior41", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State40", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit42: BinaryAssociation = BinaryAssociation(
    name="exit42",
    ends={
        Property(name="statemachines_Behavior44", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State43", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTriggers45: BinaryAssociation = BinaryAssociation(
    name="deferrableTriggers45",
    ends={
        Property(name="statemachines_Trigger", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State46", type=statemachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint47: BinaryAssociation = BinaryAssociation(
    name="connectionPoint47",
    ends={
        Property(name="Pseudostate", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state48", type=statemachines_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertice21: BinaryAssociation = BinaryAssociation(
    name="vertice21",
    ends={
        Property(name="Vertex", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=statemachines_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container55: BinaryAssociation = BinaryAssociation(
    name="container55",
    ends={
        Property(name="Region56", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=statemachines_Region, multiplicity=Multiplicity(1, 1))
    }
)
effect57: BinaryAssociation = BinaryAssociation(
    name="effect57",
    ends={
        Property(name="statemachines_Behavior59", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition58", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventType60: BinaryAssociation = BinaryAssociation(
    name="eventType60",
    ends={
        Property(name="statemachines_EventType", type=statemachines_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Trigger61", type=statemachines_EventType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
emittedSignals62: BinaryAssociation = BinaryAssociation(
    name="emittedSignals62",
    ends={
        Property(name="statemachines_SignalEventOccurrence", type=statemachines_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Behavior63", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeValues64: BinaryAssociation = BinaryAssociation(
    name="attributeValues64",
    ends={
        Property(name="statemachines_AttributeValue", type=statemachines_OperationBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_OperationBehavior", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute65: BinaryAssociation = BinaryAssociation(
    name="attribute65",
    ends={
        Property(name="statemachines_BooleanAttribute", type=statemachines_BooleanAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_BooleanAttributeValue", type=statemachines_BooleanAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute66: BinaryAssociation = BinaryAssociation(
    name="attribute66",
    ends={
        Property(name="statemachines_IntegerAttribute", type=statemachines_IntegerAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_IntegerAttributeValue", type=statemachines_IntegerAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute67: BinaryAssociation = BinaryAssociation(
    name="attribute67",
    ends={
        Property(name="statemachines_StringAttribute", type=statemachines_StringAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StringAttributeValue", type=statemachines_StringAttribute, multiplicity=Multiplicity(0, 1))
    }
)
operation76: BinaryAssociation = BinaryAssociation(
    name="operation76",
    ends={
        Property(name="statemachines_Operation77", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence", type=statemachines_Operation, multiplicity=Multiplicity(1, 1))
    }
)
inParameterValues78: BinaryAssociation = BinaryAssociation(
    name="inParameterValues78",
    ends={
        Property(name="statemachines_AttributeValue80", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence79", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParameterValues81: BinaryAssociation = BinaryAssociation(
    name="outParameterValues81",
    ends={
        Property(name="statemachines_AttributeValue83", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence82", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue84: BinaryAssociation = BinaryAssociation(
    name="returnValue84",
    ends={
        Property(name="statemachines_AttributeValue86", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence85", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state68: BinaryAssociation = BinaryAssociation(
    name="state68",
    ends={
        Property(name="statemachines_State69", type=statemachines_CompletionEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CompletionEventOccurrence", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
signal70: BinaryAssociation = BinaryAssociation(
    name="signal70",
    ends={
        Property(name="statemachines_Signal72", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventOccurrence71", type=statemachines_Signal, multiplicity=Multiplicity(1, 1))
    }
)
attributeValues73: BinaryAssociation = BinaryAssociation(
    name="attributeValues73",
    ends={
        Property(name="statemachines_AttributeValue75", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventOccurrence74", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachines_Signal_NamedElement = Generalization(general=NamedElement, specific=statemachines_Signal)
gen_statemachines_Operation_NamedElement = Generalization(general=NamedElement, specific=statemachines_Operation)
gen_statemachines_SignalEventType_EventType = Generalization(general=EventType, specific=statemachines_SignalEventType)
gen_statemachines_CallEventType_EventType = Generalization(general=EventType, specific=statemachines_CallEventType)
gen_statemachines_Attribute_NamedElement = Generalization(general=NamedElement, specific=statemachines_Attribute)
gen_statemachines_BooleanAttribute_Attribute = Generalization(general=Attribute, specific=statemachines_BooleanAttribute)
gen_statemachines_IntegerAttribute_Attribute = Generalization(general=Attribute, specific=statemachines_IntegerAttribute)
gen_statemachines_StringAttribute_Attribute = Generalization(general=Attribute, specific=statemachines_StringAttribute)
gen_statemachines_StateMachine_NamedElement = Generalization(general=NamedElement, specific=statemachines_StateMachine)
gen_statemachines_Region_NamedElement = Generalization(general=NamedElement, specific=statemachines_Region)
gen_statemachines_FinalState_State = Generalization(general=State, specific=statemachines_FinalState)
gen_statemachines_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachines_Transition)
gen_statemachines_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachines_Vertex)
gen_statemachines_Pseudostate_Vertex = Generalization(general=Vertex, specific=statemachines_Pseudostate)
gen_statemachines_State_Vertex = Generalization(general=Vertex, specific=statemachines_State)
gen_statemachines_Trigger_NamedElement = Generalization(general=NamedElement, specific=statemachines_Trigger)
gen_statemachines_Behavior_NamedElement = Generalization(general=NamedElement, specific=statemachines_Behavior)
gen_statemachines_OperationBehavior_Behavior = Generalization(general=Behavior, specific=statemachines_OperationBehavior)
gen_statemachines_BooleanAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_BooleanAttributeValue)
gen_statemachines_IntegerAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_IntegerAttributeValue)
gen_statemachines_StringAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_StringAttributeValue)
gen_statemachines_CallEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=statemachines_CallEventOccurrence)
gen_statemachines_SignalEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=statemachines_SignalEventOccurrence)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_CustomSystem, statemachines_StateMachine, statemachines_Signal, statemachines_Operation, NamedElement, statemachines_Attribute, statemachines_EventType, statemachines_SignalEventType, EventType, statemachines_CallEventType, statemachines_BooleanAttribute, Attribute, statemachines_IntegerAttribute, statemachines_StringAttribute, statemachines_Constraint, statemachines_BooleanConstraint, statemachines_IntegerConstraint, statemachines_StringConstraint, statemachines_NamedElement, statemachines_Region, statemachines_Vertex, statemachines_Transition, statemachines_FinalState, State, statemachines_State, statemachines_Pseudostate, Vertex, statemachines_Behavior, statemachines_Trigger, statemachines_SignalEventOccurrence, statemachines_OperationBehavior, Behavior, statemachines_AttributeValue, statemachines_BooleanAttributeValue, AttributeValue, statemachines_IntegerAttributeValue, statemachines_StringAttributeValue, statemachines_EventOccurrence, statemachines_CallEventOccurrence, statemachines_CompletionEventOccurrence, EventOccurrence, PseudostateKind, TransitionKind},
    associations={statemachine0, signals1, operations3, attributes5, inParameters7, outParameters10, signal16, operation18, regions20, return_13, transitions22, stateMachine24, state25, source49, currentVertex27, target51, container28, triggers53, outgoingTransitions30, incomingTransitions32, state34, regions36, entry38, doActivity39, exit42, deferrableTriggers45, connectionPoint47, vertice21, container55, effect57, eventType60, emittedSignals62, attributeValues64, attribute65, attribute66, attribute67, operation76, inParameterValues78, outParameterValues81, returnValue84, state68, signal70, attributeValues73},
    generalizations={gen_statemachines_Signal_NamedElement, gen_statemachines_Operation_NamedElement, gen_statemachines_SignalEventType_EventType, gen_statemachines_CallEventType_EventType, gen_statemachines_Attribute_NamedElement, gen_statemachines_BooleanAttribute_Attribute, gen_statemachines_IntegerAttribute_Attribute, gen_statemachines_StringAttribute_Attribute, gen_statemachines_StateMachine_NamedElement, gen_statemachines_Region_NamedElement, gen_statemachines_FinalState_State, gen_statemachines_Transition_NamedElement, gen_statemachines_Vertex_NamedElement, gen_statemachines_Pseudostate_Vertex, gen_statemachines_State_Vertex, gen_statemachines_Trigger_NamedElement, gen_statemachines_Behavior_NamedElement, gen_statemachines_OperationBehavior_Behavior, gen_statemachines_BooleanAttributeValue_AttributeValue, gen_statemachines_IntegerAttributeValue_AttributeValue, gen_statemachines_StringAttributeValue_AttributeValue, gen_statemachines_CallEventOccurrence_EventOccurrence, gen_statemachines_SignalEventOccurrence_EventOccurrence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)