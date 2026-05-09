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
statemachines_BooleanConstraint = Class(name="statemachines_BooleanConstraint")
statemachines_IntegerConstraint = Class(name="statemachines_IntegerConstraint")
statemachines_StringConstraint = Class(name="statemachines_StringConstraint")
statemachines_NamedElement = Class(name="statemachines_NamedElement", is_abstract=True)
statemachines_Region = Class(name="statemachines_Region")
statemachines_Vertex = Class(name="statemachines_Vertex", is_abstract=True)
statemachines_Transition = Class(name="statemachines_Transition")
statemachines_State = Class(name="statemachines_State")
statemachines_Pseudostate = Class(name="statemachines_Pseudostate")
Vertex = Class(name="Vertex")
statemachines_BooleanAttribute = Class(name="statemachines_BooleanAttribute")
Attribute = Class(name="Attribute")
statemachines_IntegerAttribute = Class(name="statemachines_IntegerAttribute")
statemachines_StringAttribute = Class(name="statemachines_StringAttribute")
statemachines_Constraint = Class(name="statemachines_Constraint", is_abstract=True)
statemachines_Trigger = Class(name="statemachines_Trigger")
statemachines_FinalState = Class(name="statemachines_FinalState")
State = Class(name="State")
statemachines_SignalEventOccurrence = Class(name="statemachines_SignalEventOccurrence")
statemachines_OperationBehavior = Class(name="statemachines_OperationBehavior")
Behavior = Class(name="Behavior")
statemachines_AttributeValue = Class(name="statemachines_AttributeValue", is_abstract=True)
statemachines_BooleanAttributeValue = Class(name="statemachines_BooleanAttributeValue")
AttributeValue = Class(name="AttributeValue")
statemachines_Behavior = Class(name="statemachines_Behavior")
statemachines_StringAttributeValue = Class(name="statemachines_StringAttributeValue")
statemachines_EventOccurrence = Class(name="statemachines_EventOccurrence", is_abstract=True)
statemachines_CompletionEventOccurrence = Class(name="statemachines_CompletionEventOccurrence")
EventOccurrence = Class(name="EventOccurrence")
statemachines_CallEventOccurrence = Class(name="statemachines_CallEventOccurrence")
statemachines_IntegerAttributeValue = Class(name="statemachines_IntegerAttributeValue")

# statemachines_CustomSystem class attributes and methods

# statemachines_StateMachine class attributes and methods

# statemachines_Signal class attributes and methods

# statemachines_Operation class attributes and methods

# NamedElement class attributes and methods

# statemachines_Attribute class attributes and methods

# statemachines_EventType class attributes and methods

# statemachines_SignalEventType class attributes and methods

# EventType class attributes and methods

# statemachines_CallEventType class attributes and methods

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
statemachines_Transition.attributes={statemachines_Transition_kind}

# statemachines_State class attributes and methods

# statemachines_Pseudostate class attributes and methods
statemachines_Pseudostate_kind: Property = Property(name="kind", type=StringType)
statemachines_Pseudostate.attributes={statemachines_Pseudostate_kind}

# Vertex class attributes and methods

# statemachines_BooleanAttribute class attributes and methods

# Attribute class attributes and methods

# statemachines_IntegerAttribute class attributes and methods

# statemachines_StringAttribute class attributes and methods

# statemachines_Constraint class attributes and methods
statemachines_Constraint_value: Property = Property(name="value", type=StringType)
statemachines_Constraint.attributes={statemachines_Constraint_value}

# statemachines_Trigger class attributes and methods

# statemachines_FinalState class attributes and methods

# State class attributes and methods

# statemachines_SignalEventOccurrence class attributes and methods

# statemachines_OperationBehavior class attributes and methods

# Behavior class attributes and methods

# statemachines_AttributeValue class attributes and methods

# statemachines_BooleanAttributeValue class attributes and methods
statemachines_BooleanAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_BooleanAttributeValue.attributes={statemachines_BooleanAttributeValue_value}

# AttributeValue class attributes and methods

# statemachines_Behavior class attributes and methods

# statemachines_StringAttributeValue class attributes and methods
statemachines_StringAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_StringAttributeValue.attributes={statemachines_StringAttributeValue_value}

# statemachines_EventOccurrence class attributes and methods

# statemachines_CompletionEventOccurrence class attributes and methods

# EventOccurrence class attributes and methods

# statemachines_CallEventOccurrence class attributes and methods

# statemachines_IntegerAttributeValue class attributes and methods
statemachines_IntegerAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_IntegerAttributeValue.attributes={statemachines_IntegerAttributeValue_value}

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
return_13: BinaryAssociation = BinaryAssociation(
    name="return_13",
    ends={
        Property(name="statemachines_Attribute15", type=statemachines_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Operation14", type=statemachines_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
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
vertice21: BinaryAssociation = BinaryAssociation(
    name="vertice21",
    ends={
        Property(name="Vertex", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=statemachines_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
container27: BinaryAssociation = BinaryAssociation(
    name="container27",
    ends={
        Property(name="Region28", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertice", type=statemachines_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions29: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions29",
    ends={
        Property(name="Transition30", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions31: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions31",
    ends={
        Property(name="Transition32", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
doActivity38: BinaryAssociation = BinaryAssociation(
    name="doActivity38",
    ends={
        Property(name="statemachines_Behavior40", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State39", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit41: BinaryAssociation = BinaryAssociation(
    name="exit41",
    ends={
        Property(name="statemachines_Behavior43", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State42", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTriggers44: BinaryAssociation = BinaryAssociation(
    name="deferrableTriggers44",
    ends={
        Property(name="statemachines_Trigger", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State45", type=statemachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint46: BinaryAssociation = BinaryAssociation(
    name="connectionPoint46",
    ends={
        Property(name="Pseudostate", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state47", type=statemachines_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source48: BinaryAssociation = BinaryAssociation(
    name="source48",
    ends={
        Property(name="Vertex49", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target50: BinaryAssociation = BinaryAssociation(
    name="target50",
    ends={
        Property(name="Vertex51", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
triggers52: BinaryAssociation = BinaryAssociation(
    name="triggers52",
    ends={
        Property(name="statemachines_Trigger53", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition", type=statemachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container54: BinaryAssociation = BinaryAssociation(
    name="container54",
    ends={
        Property(name="Region55", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=statemachines_Region, multiplicity=Multiplicity(1, 1))
    }
)
effect56: BinaryAssociation = BinaryAssociation(
    name="effect56",
    ends={
        Property(name="statemachines_Behavior58", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition57", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventType59: BinaryAssociation = BinaryAssociation(
    name="eventType59",
    ends={
        Property(name="statemachines_EventType", type=statemachines_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Trigger60", type=statemachines_EventType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
emittedSignals61: BinaryAssociation = BinaryAssociation(
    name="emittedSignals61",
    ends={
        Property(name="statemachines_SignalEventOccurrence", type=statemachines_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Behavior62", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeValues63: BinaryAssociation = BinaryAssociation(
    name="attributeValues63",
    ends={
        Property(name="statemachines_AttributeValue", type=statemachines_OperationBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_OperationBehavior", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state33: BinaryAssociation = BinaryAssociation(
    name="state33",
    ends={
        Property(name="State34", type=statemachines_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
regions35: BinaryAssociation = BinaryAssociation(
    name="regions35",
    ends={
        Property(name="Region36", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=statemachines_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry37: BinaryAssociation = BinaryAssociation(
    name="entry37",
    ends={
        Property(name="statemachines_Behavior", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute66: BinaryAssociation = BinaryAssociation(
    name="attribute66",
    ends={
        Property(name="statemachines_StringAttribute", type=statemachines_StringAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StringAttributeValue", type=statemachines_StringAttribute, multiplicity=Multiplicity(0, 1))
    }
)
state67: BinaryAssociation = BinaryAssociation(
    name="state67",
    ends={
        Property(name="statemachines_State68", type=statemachines_CompletionEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CompletionEventOccurrence", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
signal69: BinaryAssociation = BinaryAssociation(
    name="signal69",
    ends={
        Property(name="statemachines_Signal71", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventOccurrence70", type=statemachines_Signal, multiplicity=Multiplicity(1, 1))
    }
)
attributeValues72: BinaryAssociation = BinaryAssociation(
    name="attributeValues72",
    ends={
        Property(name="statemachines_AttributeValue74", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventOccurrence73", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation75: BinaryAssociation = BinaryAssociation(
    name="operation75",
    ends={
        Property(name="statemachines_Operation76", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence", type=statemachines_Operation, multiplicity=Multiplicity(1, 1))
    }
)
inParameterValues77: BinaryAssociation = BinaryAssociation(
    name="inParameterValues77",
    ends={
        Property(name="statemachines_AttributeValue79", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence78", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParameterValues80: BinaryAssociation = BinaryAssociation(
    name="outParameterValues80",
    ends={
        Property(name="statemachines_AttributeValue82", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence81", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue83: BinaryAssociation = BinaryAssociation(
    name="returnValue83",
    ends={
        Property(name="statemachines_AttributeValue85", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence84", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute64: BinaryAssociation = BinaryAssociation(
    name="attribute64",
    ends={
        Property(name="statemachines_BooleanAttribute", type=statemachines_BooleanAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_BooleanAttributeValue", type=statemachines_BooleanAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute65: BinaryAssociation = BinaryAssociation(
    name="attribute65",
    ends={
        Property(name="statemachines_IntegerAttribute", type=statemachines_IntegerAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_IntegerAttributeValue", type=statemachines_IntegerAttribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statemachines_Signal_NamedElement = Generalization(general=NamedElement, specific=statemachines_Signal)
gen_statemachines_Operation_NamedElement = Generalization(general=NamedElement, specific=statemachines_Operation)
gen_statemachines_SignalEventType_EventType = Generalization(general=EventType, specific=statemachines_SignalEventType)
gen_statemachines_CallEventType_EventType = Generalization(general=EventType, specific=statemachines_CallEventType)
gen_statemachines_StateMachine_NamedElement = Generalization(general=NamedElement, specific=statemachines_StateMachine)
gen_statemachines_Region_NamedElement = Generalization(general=NamedElement, specific=statemachines_Region)
gen_statemachines_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachines_Vertex)
gen_statemachines_Pseudostate_Vertex = Generalization(general=Vertex, specific=statemachines_Pseudostate)
gen_statemachines_Attribute_NamedElement = Generalization(general=NamedElement, specific=statemachines_Attribute)
gen_statemachines_BooleanAttribute_Attribute = Generalization(general=Attribute, specific=statemachines_BooleanAttribute)
gen_statemachines_IntegerAttribute_Attribute = Generalization(general=Attribute, specific=statemachines_IntegerAttribute)
gen_statemachines_StringAttribute_Attribute = Generalization(general=Attribute, specific=statemachines_StringAttribute)
gen_statemachines_FinalState_State = Generalization(general=State, specific=statemachines_FinalState)
gen_statemachines_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachines_Transition)
gen_statemachines_Trigger_NamedElement = Generalization(general=NamedElement, specific=statemachines_Trigger)
gen_statemachines_Behavior_NamedElement = Generalization(general=NamedElement, specific=statemachines_Behavior)
gen_statemachines_OperationBehavior_Behavior = Generalization(general=Behavior, specific=statemachines_OperationBehavior)
gen_statemachines_BooleanAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_BooleanAttributeValue)
gen_statemachines_State_Vertex = Generalization(general=Vertex, specific=statemachines_State)
gen_statemachines_StringAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_StringAttributeValue)
gen_statemachines_SignalEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=statemachines_SignalEventOccurrence)
gen_statemachines_CallEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=statemachines_CallEventOccurrence)
gen_statemachines_IntegerAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_IntegerAttributeValue)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_CustomSystem, statemachines_StateMachine, statemachines_Signal, statemachines_Operation, NamedElement, statemachines_Attribute, statemachines_EventType, statemachines_SignalEventType, EventType, statemachines_CallEventType, statemachines_BooleanConstraint, statemachines_IntegerConstraint, statemachines_StringConstraint, statemachines_NamedElement, statemachines_Region, statemachines_Vertex, statemachines_Transition, statemachines_State, statemachines_Pseudostate, Vertex, statemachines_BooleanAttribute, Attribute, statemachines_IntegerAttribute, statemachines_StringAttribute, statemachines_Constraint, statemachines_Trigger, statemachines_FinalState, State, statemachines_SignalEventOccurrence, statemachines_OperationBehavior, Behavior, statemachines_AttributeValue, statemachines_BooleanAttributeValue, AttributeValue, statemachines_Behavior, statemachines_StringAttributeValue, statemachines_EventOccurrence, statemachines_CompletionEventOccurrence, EventOccurrence, statemachines_CallEventOccurrence, statemachines_IntegerAttributeValue, PseudostateKind, TransitionKind},
    associations={statemachine0, signals1, operations3, attributes5, inParameters7, outParameters10, return_13, signal16, operation18, regions20, vertice21, transitions22, stateMachine24, state25, container27, outgoingTransitions29, incomingTransitions31, doActivity38, exit41, deferrableTriggers44, connectionPoint46, source48, target50, triggers52, container54, effect56, eventType59, emittedSignals61, attributeValues63, state33, regions35, entry37, attribute66, state67, signal69, attributeValues72, operation75, inParameterValues77, outParameterValues80, returnValue83, attribute64, attribute65},
    generalizations={gen_statemachines_Signal_NamedElement, gen_statemachines_Operation_NamedElement, gen_statemachines_SignalEventType_EventType, gen_statemachines_CallEventType_EventType, gen_statemachines_StateMachine_NamedElement, gen_statemachines_Region_NamedElement, gen_statemachines_Vertex_NamedElement, gen_statemachines_Pseudostate_Vertex, gen_statemachines_Attribute_NamedElement, gen_statemachines_BooleanAttribute_Attribute, gen_statemachines_IntegerAttribute_Attribute, gen_statemachines_StringAttribute_Attribute, gen_statemachines_FinalState_State, gen_statemachines_Transition_NamedElement, gen_statemachines_Trigger_NamedElement, gen_statemachines_Behavior_NamedElement, gen_statemachines_OperationBehavior_Behavior, gen_statemachines_BooleanAttributeValue_AttributeValue, gen_statemachines_State_Vertex, gen_statemachines_StringAttributeValue_AttributeValue, gen_statemachines_SignalEventOccurrence_EventOccurrence, gen_statemachines_CallEventOccurrence_EventOccurrence, gen_statemachines_IntegerAttributeValue_AttributeValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)