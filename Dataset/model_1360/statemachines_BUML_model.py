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
TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

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

# Classes
statemachines_Signal = Class(name="statemachines::Signal")
statemachines_Operation = Class(name="statemachines::Operation")
NamedElement = Class(name="NamedElement")
statemachines_Attribute = Class(name="statemachines::Attribute", is_abstract=True)
statemachines_CustomSystem = Class(name="statemachines::CustomSystem")
statemachines_StateMachine = Class(name="statemachines::StateMachine")
statemachines_BooleanConstraint = Class(name="statemachines::BooleanConstraint")
statemachines_IntegerConstraint = Class(name="statemachines::IntegerConstraint")
statemachines_StringConstraint = Class(name="statemachines::StringConstraint")
statemachines_EventType = Class(name="statemachines::EventType", is_abstract=True)
statemachines_SignalEventType = Class(name="statemachines::SignalEventType")
EventType = Class(name="EventType")
statemachines_CallEventType = Class(name="statemachines::CallEventType")
statemachines_BooleanAttribute = Class(name="statemachines::BooleanAttribute")
Attribute = Class(name="Attribute")
statemachines_IntegerAttribute = Class(name="statemachines::IntegerAttribute")
statemachines_StringAttribute = Class(name="statemachines::StringAttribute")
statemachines_Constraint = Class(name="statemachines::Constraint", is_abstract=True)
statemachines_Pseudostate = Class(name="statemachines::Pseudostate")
Vertex = Class(name="Vertex")
statemachines_NamedElement = Class(name="statemachines::NamedElement", is_abstract=True)
statemachines_Region = Class(name="statemachines::Region")
statemachines_Vertex = Class(name="statemachines::Vertex", is_abstract=True)
statemachines_Transition = Class(name="statemachines::Transition")
statemachines_State = Class(name="statemachines::State")
statemachines_Behavior = Class(name="statemachines::Behavior")
statemachines_Trigger = Class(name="statemachines::Trigger")
statemachines_FinalState = Class(name="statemachines::FinalState")
State = Class(name="State")
statemachines_SignalEventOccurrence = Class(name="statemachines::SignalEventOccurrence")
statemachines_OperationBehavior = Class(name="statemachines::OperationBehavior")
Behavior = Class(name="Behavior")
statemachines_AttributeValue = Class(name="statemachines::AttributeValue", is_abstract=True)
statemachines_StringAttributeValue = Class(name="statemachines::StringAttributeValue")
statemachines_BooleanAttributeValue = Class(name="statemachines::BooleanAttributeValue")
AttributeValue = Class(name="AttributeValue")
statemachines_IntegerAttributeValue = Class(name="statemachines::IntegerAttributeValue")
statemachines_CallEventOccurrence = Class(name="statemachines::CallEventOccurrence")
statemachines_EventOccurrence = Class(name="statemachines::EventOccurrence", is_abstract=True)
statemachines_CompletionEventOccurrence = Class(name="statemachines::CompletionEventOccurrence")
EventOccurrence = Class(name="EventOccurrence")

# statemachines_Signal class attributes and methods

# statemachines_Operation class attributes and methods

# NamedElement class attributes and methods

# statemachines_Attribute class attributes and methods

# statemachines_CustomSystem class attributes and methods

# statemachines_StateMachine class attributes and methods

# statemachines_BooleanConstraint class attributes and methods

# statemachines_IntegerConstraint class attributes and methods

# statemachines_StringConstraint class attributes and methods

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

# statemachines_Pseudostate class attributes and methods
statemachines_Pseudostate_kind: Property = Property(name="kind", type=StringType)
statemachines_Pseudostate.attributes={statemachines_Pseudostate_kind}

# Vertex class attributes and methods

# statemachines_NamedElement class attributes and methods
statemachines_NamedElement_name: Property = Property(name="name", type=StringType)
statemachines_NamedElement.attributes={statemachines_NamedElement_name}

# statemachines_Region class attributes and methods

# statemachines_Vertex class attributes and methods

# statemachines_Transition class attributes and methods
statemachines_Transition_kind: Property = Property(name="kind", type=StringType)
statemachines_Transition.attributes={statemachines_Transition_kind}

# statemachines_State class attributes and methods

# statemachines_Behavior class attributes and methods

# statemachines_Trigger class attributes and methods

# statemachines_FinalState class attributes and methods

# State class attributes and methods

# statemachines_SignalEventOccurrence class attributes and methods

# statemachines_OperationBehavior class attributes and methods

# Behavior class attributes and methods

# statemachines_AttributeValue class attributes and methods

# statemachines_StringAttributeValue class attributes and methods
statemachines_StringAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_StringAttributeValue.attributes={statemachines_StringAttributeValue_value}

# statemachines_BooleanAttributeValue class attributes and methods
statemachines_BooleanAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_BooleanAttributeValue.attributes={statemachines_BooleanAttributeValue_value}

# AttributeValue class attributes and methods

# statemachines_IntegerAttributeValue class attributes and methods
statemachines_IntegerAttributeValue_value: Property = Property(name="value", type=StringType)
statemachines_IntegerAttributeValue.attributes={statemachines_IntegerAttributeValue_value}

# statemachines_CallEventOccurrence class attributes and methods

# statemachines_EventOccurrence class attributes and methods

# statemachines_CompletionEventOccurrence class attributes and methods

# EventOccurrence class attributes and methods

# Relationships
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="statemachines_CustomSystem", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="statemachines_StateMachine", type=statemachines_CustomSystem, multiplicity=Multiplicity(1, 1))
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
return13: BinaryAssociation = BinaryAssociation(
    name="return13",
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
incomingTransitions40: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions40",
    ends={
        Property(name="42", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="41", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
state43: BinaryAssociation = BinaryAssociation(
    name="state43",
    ends={
        Property(name="45", type=statemachines_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="44", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
regions20: BinaryAssociation = BinaryAssociation(
    name="regions20",
    ends={
        Property(name="21", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=statemachines_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
vertice22: BinaryAssociation = BinaryAssociation(
    name="vertice22",
    ends={
        Property(name="24", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=statemachines_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions25: BinaryAssociation = BinaryAssociation(
    name="transitions25",
    ends={
        Property(name="27", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="26", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine28: BinaryAssociation = BinaryAssociation(
    name="stateMachine28",
    ends={
        Property(name="30", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="29", type=statemachines_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state31: BinaryAssociation = BinaryAssociation(
    name="state31",
    ends={
        Property(name="33", type=statemachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="32", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
container34: BinaryAssociation = BinaryAssociation(
    name="container34",
    ends={
        Property(name="36", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="35", type=statemachines_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions37: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions37",
    ends={
        Property(name="39", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="38", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container69: BinaryAssociation = BinaryAssociation(
    name="container69",
    ends={
        Property(name="71", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="70", type=statemachines_Region, multiplicity=Multiplicity(1, 1))
    }
)
effect72: BinaryAssociation = BinaryAssociation(
    name="effect72",
    ends={
        Property(name="statemachines_Behavior74", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition73", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
regions46: BinaryAssociation = BinaryAssociation(
    name="regions46",
    ends={
        Property(name="48", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="47", type=statemachines_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry49: BinaryAssociation = BinaryAssociation(
    name="entry49",
    ends={
        Property(name="statemachines_Behavior", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity50: BinaryAssociation = BinaryAssociation(
    name="doActivity50",
    ends={
        Property(name="statemachines_Behavior52", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State51", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit53: BinaryAssociation = BinaryAssociation(
    name="exit53",
    ends={
        Property(name="statemachines_Behavior55", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State54", type=statemachines_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTriggers56: BinaryAssociation = BinaryAssociation(
    name="deferrableTriggers56",
    ends={
        Property(name="statemachines_Trigger", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State57", type=statemachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint58: BinaryAssociation = BinaryAssociation(
    name="connectionPoint58",
    ends={
        Property(name="60", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="59", type=statemachines_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source61: BinaryAssociation = BinaryAssociation(
    name="source61",
    ends={
        Property(name="63", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="62", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target64: BinaryAssociation = BinaryAssociation(
    name="target64",
    ends={
        Property(name="66", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="65", type=statemachines_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
triggers67: BinaryAssociation = BinaryAssociation(
    name="triggers67",
    ends={
        Property(name="statemachines_Trigger68", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition", type=statemachines_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventType75: BinaryAssociation = BinaryAssociation(
    name="eventType75",
    ends={
        Property(name="statemachines_EventType", type=statemachines_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Trigger76", type=statemachines_EventType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
emittedSignals77: BinaryAssociation = BinaryAssociation(
    name="emittedSignals77",
    ends={
        Property(name="statemachines_SignalEventOccurrence", type=statemachines_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Behavior78", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute82: BinaryAssociation = BinaryAssociation(
    name="attribute82",
    ends={
        Property(name="statemachines_StringAttribute", type=statemachines_StringAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StringAttributeValue", type=statemachines_StringAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attributeValues79: BinaryAssociation = BinaryAssociation(
    name="attributeValues79",
    ends={
        Property(name="statemachines_AttributeValue", type=statemachines_OperationBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_OperationBehavior", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute80: BinaryAssociation = BinaryAssociation(
    name="attribute80",
    ends={
        Property(name="statemachines_BooleanAttribute", type=statemachines_BooleanAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_BooleanAttributeValue", type=statemachines_BooleanAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute81: BinaryAssociation = BinaryAssociation(
    name="attribute81",
    ends={
        Property(name="statemachines_IntegerAttribute", type=statemachines_IntegerAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_IntegerAttributeValue", type=statemachines_IntegerAttribute, multiplicity=Multiplicity(0, 1))
    }
)
operation91: BinaryAssociation = BinaryAssociation(
    name="operation91",
    ends={
        Property(name="statemachines_Operation92", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence", type=statemachines_Operation, multiplicity=Multiplicity(1, 1))
    }
)
state83: BinaryAssociation = BinaryAssociation(
    name="state83",
    ends={
        Property(name="statemachines_State84", type=statemachines_CompletionEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CompletionEventOccurrence", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
signal85: BinaryAssociation = BinaryAssociation(
    name="signal85",
    ends={
        Property(name="statemachines_Signal87", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventOccurrence86", type=statemachines_Signal, multiplicity=Multiplicity(1, 1))
    }
)
attributeValues88: BinaryAssociation = BinaryAssociation(
    name="attributeValues88",
    ends={
        Property(name="statemachines_AttributeValue90", type=statemachines_SignalEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_SignalEventOccurrence89", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inParameterValues93: BinaryAssociation = BinaryAssociation(
    name="inParameterValues93",
    ends={
        Property(name="statemachines_AttributeValue95", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence94", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParameterValues96: BinaryAssociation = BinaryAssociation(
    name="outParameterValues96",
    ends={
        Property(name="statemachines_AttributeValue98", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence97", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue99: BinaryAssociation = BinaryAssociation(
    name="returnValue99",
    ends={
        Property(name="statemachines_AttributeValue101", type=statemachines_CallEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_CallEventOccurrence100", type=statemachines_AttributeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
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
gen_statemachines_Pseudostate_Vertex = Generalization(general=Vertex, specific=statemachines_Pseudostate)
gen_statemachines_State_Vertex = Generalization(general=Vertex, specific=statemachines_State)
gen_statemachines_StateMachine_NamedElement = Generalization(general=NamedElement, specific=statemachines_StateMachine)
gen_statemachines_Region_NamedElement = Generalization(general=NamedElement, specific=statemachines_Region)
gen_statemachines_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachines_Vertex)
gen_statemachines_FinalState_State = Generalization(general=State, specific=statemachines_FinalState)
gen_statemachines_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachines_Transition)
gen_statemachines_Behavior_NamedElement = Generalization(general=NamedElement, specific=statemachines_Behavior)
gen_statemachines_OperationBehavior_Behavior = Generalization(general=Behavior, specific=statemachines_OperationBehavior)
gen_statemachines_Trigger_NamedElement = Generalization(general=NamedElement, specific=statemachines_Trigger)
gen_statemachines_StringAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_StringAttributeValue)
gen_statemachines_BooleanAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_BooleanAttributeValue)
gen_statemachines_IntegerAttributeValue_AttributeValue = Generalization(general=AttributeValue, specific=statemachines_IntegerAttributeValue)
gen_statemachines_CallEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=statemachines_CallEventOccurrence)
gen_statemachines_SignalEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=statemachines_SignalEventOccurrence)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_Signal, statemachines_Operation, NamedElement, statemachines_Attribute, statemachines_CustomSystem, statemachines_StateMachine, statemachines_BooleanConstraint, statemachines_IntegerConstraint, statemachines_StringConstraint, statemachines_EventType, statemachines_SignalEventType, EventType, statemachines_CallEventType, statemachines_BooleanAttribute, Attribute, statemachines_IntegerAttribute, statemachines_StringAttribute, statemachines_Constraint, statemachines_Pseudostate, Vertex, statemachines_NamedElement, statemachines_Region, statemachines_Vertex, statemachines_Transition, statemachines_State, statemachines_Behavior, statemachines_Trigger, statemachines_FinalState, State, statemachines_SignalEventOccurrence, statemachines_OperationBehavior, Behavior, statemachines_AttributeValue, statemachines_StringAttributeValue, statemachines_BooleanAttributeValue, AttributeValue, statemachines_IntegerAttributeValue, statemachines_CallEventOccurrence, statemachines_EventOccurrence, statemachines_CompletionEventOccurrence, EventOccurrence, TransitionKind, PseudostateKind},
    associations={statemachine0, signals1, operations3, attributes5, inParameters7, outParameters10, return13, signal16, operation18, incomingTransitions40, state43, regions20, vertice22, transitions25, stateMachine28, state31, container34, outgoingTransitions37, container69, effect72, regions46, entry49, doActivity50, exit53, deferrableTriggers56, connectionPoint58, source61, target64, triggers67, eventType75, emittedSignals77, attribute82, attributeValues79, attribute80, attribute81, operation91, state83, signal85, attributeValues88, inParameterValues93, outParameterValues96, returnValue99},
    generalizations={gen_statemachines_Signal_NamedElement, gen_statemachines_Operation_NamedElement, gen_statemachines_SignalEventType_EventType, gen_statemachines_CallEventType_EventType, gen_statemachines_Attribute_NamedElement, gen_statemachines_BooleanAttribute_Attribute, gen_statemachines_IntegerAttribute_Attribute, gen_statemachines_StringAttribute_Attribute, gen_statemachines_Pseudostate_Vertex, gen_statemachines_State_Vertex, gen_statemachines_StateMachine_NamedElement, gen_statemachines_Region_NamedElement, gen_statemachines_Vertex_NamedElement, gen_statemachines_FinalState_State, gen_statemachines_Transition_NamedElement, gen_statemachines_Behavior_NamedElement, gen_statemachines_OperationBehavior_Behavior, gen_statemachines_Trigger_NamedElement, gen_statemachines_StringAttributeValue_AttributeValue, gen_statemachines_BooleanAttributeValue_AttributeValue, gen_statemachines_IntegerAttributeValue_AttributeValue, gen_statemachines_CallEventOccurrence_EventOccurrence, gen_statemachines_SignalEventOccurrence_EventOccurrence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)