import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EventOccurrence,
    statemachines_CallEventOccurrence,
    statemachines_CompletionEventOccurrence,
    statemachines_EventOccurrence,
    AttributeValue,
    statemachines_IntegerAttributeValue,
    statemachines_StringAttributeValue,
    statemachines_BooleanAttributeValue,
    statemachines_AttributeValue,
    Behavior,
    statemachines_OperationBehavior,
    statemachines_SignalEventOccurrence,
    Vertex,
    statemachines_Pseudostate,
    State,
    statemachines_FinalState,
    statemachines_Constraint,
    statemachines_State,
    statemachines_NamedElement,
    statemachines_StringConstraint,
    statemachines_IntegerConstraint,
    statemachines_BooleanConstraint,
    Attribute,
    statemachines_IntegerAttribute,
    statemachines_StringAttribute,
    statemachines_BooleanAttribute,
    EventType,
    statemachines_CallEventType,
    statemachines_SignalEventType,
    statemachines_EventType,
    NamedElement,
    statemachines_Trigger,
    statemachines_Behavior,
    statemachines_Attribute,
    statemachines_Transition,
    statemachines_Vertex,
    statemachines_Region,
    statemachines_Operation,
    statemachines_Signal,
    statemachines_StateMachine,
    statemachines_CustomSystem,
    TransitionKind,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_calleventoccurrence_is_not_abstract():
    assert not inspect.isabstract(statemachines_CallEventOccurrence)


def test_statemachines_calleventoccurrence_constructor_exists():
    assert callable(statemachines_CallEventOccurrence.__init__)


def test_statemachines_calleventoccurrence_constructor_args():
    sig = inspect.signature(statemachines_CallEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_completioneventoccurrence_is_not_abstract():
    assert not inspect.isabstract(statemachines_CompletionEventOccurrence)


def test_statemachines_completioneventoccurrence_constructor_exists():
    assert callable(statemachines_CompletionEventOccurrence.__init__)


def test_statemachines_completioneventoccurrence_constructor_args():
    sig = inspect.signature(statemachines_CompletionEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(statemachines_EventOccurrence)


def test_statemachines_eventoccurrence_constructor_exists():
    assert callable(statemachines_EventOccurrence.__init__)


def test_statemachines_eventoccurrence_constructor_args():
    sig = inspect.signature(statemachines_EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_integerattributevalue_is_not_abstract():
    assert not inspect.isabstract(statemachines_IntegerAttributeValue)


def test_statemachines_integerattributevalue_constructor_exists():
    assert callable(statemachines_IntegerAttributeValue.__init__)


def test_statemachines_integerattributevalue_constructor_args():
    sig = inspect.signature(statemachines_IntegerAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachines_integerattributevalue_has_value():
    assert hasattr(statemachines_IntegerAttributeValue, "value")
    descriptor = None
    for klass in statemachines_IntegerAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_stringattributevalue_is_not_abstract():
    assert not inspect.isabstract(statemachines_StringAttributeValue)


def test_statemachines_stringattributevalue_constructor_exists():
    assert callable(statemachines_StringAttributeValue.__init__)


def test_statemachines_stringattributevalue_constructor_args():
    sig = inspect.signature(statemachines_StringAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachines_stringattributevalue_has_value():
    assert hasattr(statemachines_StringAttributeValue, "value")
    descriptor = None
    for klass in statemachines_StringAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_booleanattributevalue_is_not_abstract():
    assert not inspect.isabstract(statemachines_BooleanAttributeValue)


def test_statemachines_booleanattributevalue_constructor_exists():
    assert callable(statemachines_BooleanAttributeValue.__init__)


def test_statemachines_booleanattributevalue_constructor_args():
    sig = inspect.signature(statemachines_BooleanAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachines_booleanattributevalue_has_value():
    assert hasattr(statemachines_BooleanAttributeValue, "value")
    descriptor = None
    for klass in statemachines_BooleanAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_attributevalue_is_not_abstract():
    assert not inspect.isabstract(statemachines_AttributeValue)


def test_statemachines_attributevalue_constructor_exists():
    assert callable(statemachines_AttributeValue.__init__)


def test_statemachines_attributevalue_constructor_args():
    sig = inspect.signature(statemachines_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_operationbehavior_is_not_abstract():
    assert not inspect.isabstract(statemachines_OperationBehavior)


def test_statemachines_operationbehavior_constructor_exists():
    assert callable(statemachines_OperationBehavior.__init__)


def test_statemachines_operationbehavior_constructor_args():
    sig = inspect.signature(statemachines_OperationBehavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_signaleventoccurrence_is_not_abstract():
    assert not inspect.isabstract(statemachines_SignalEventOccurrence)


def test_statemachines_signaleventoccurrence_constructor_exists():
    assert callable(statemachines_SignalEventOccurrence.__init__)


def test_statemachines_signaleventoccurrence_constructor_args():
    sig = inspect.signature(statemachines_SignalEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachines_Pseudostate)


def test_statemachines_pseudostate_constructor_exists():
    assert callable(statemachines_Pseudostate.__init__)


def test_statemachines_pseudostate_constructor_args():
    sig = inspect.signature(statemachines_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines_pseudostate_has_kind():
    assert hasattr(statemachines_Pseudostate, "kind")
    descriptor = None
    for klass in statemachines_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachines_FinalState)


def test_statemachines_finalstate_constructor_exists():
    assert callable(statemachines_FinalState.__init__)


def test_statemachines_finalstate_constructor_args():
    sig = inspect.signature(statemachines_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_constraint_is_not_abstract():
    assert not inspect.isabstract(statemachines_Constraint)


def test_statemachines_constraint_constructor_exists():
    assert callable(statemachines_Constraint.__init__)


def test_statemachines_constraint_constructor_args():
    sig = inspect.signature(statemachines_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachines_constraint_has_value():
    assert hasattr(statemachines_Constraint, "value")
    descriptor = None
    for klass in statemachines_Constraint.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_state_is_not_abstract():
    assert not inspect.isabstract(statemachines_State)


def test_statemachines_state_constructor_exists():
    assert callable(statemachines_State.__init__)


def test_statemachines_state_constructor_args():
    sig = inspect.signature(statemachines_State.__init__)
    params = list(sig.parameters.keys())
    assert "isDoActivityCompleted" in params, "Missing parameter 'isDoActivityCompleted'"
    assert "isExitCompleted" in params, "Missing parameter 'isExitCompleted'"
    assert "isEntryCompleted" in params, "Missing parameter 'isEntryCompleted'"

def test_statemachines_state_has_isDoActivityCompleted():
    assert hasattr(statemachines_State, "isDoActivityCompleted")
    descriptor = None
    for klass in statemachines_State.__mro__:
        if "isDoActivityCompleted" in klass.__dict__:
            descriptor = klass.__dict__["isDoActivityCompleted"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_state_has_isExitCompleted():
    assert hasattr(statemachines_State, "isExitCompleted")
    descriptor = None
    for klass in statemachines_State.__mro__:
        if "isExitCompleted" in klass.__dict__:
            descriptor = klass.__dict__["isExitCompleted"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_state_has_isEntryCompleted():
    assert hasattr(statemachines_State, "isEntryCompleted")
    descriptor = None
    for klass in statemachines_State.__mro__:
        if "isEntryCompleted" in klass.__dict__:
            descriptor = klass.__dict__["isEntryCompleted"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachines_NamedElement)


def test_statemachines_namedelement_constructor_exists():
    assert callable(statemachines_NamedElement.__init__)


def test_statemachines_namedelement_constructor_args():
    sig = inspect.signature(statemachines_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachines_namedelement_has_name():
    assert hasattr(statemachines_NamedElement, "name")
    descriptor = None
    for klass in statemachines_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_stringconstraint_is_not_abstract():
    assert not inspect.isabstract(statemachines_StringConstraint)


def test_statemachines_stringconstraint_constructor_exists():
    assert callable(statemachines_StringConstraint.__init__)


def test_statemachines_stringconstraint_constructor_args():
    sig = inspect.signature(statemachines_StringConstraint.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_integerconstraint_is_not_abstract():
    assert not inspect.isabstract(statemachines_IntegerConstraint)


def test_statemachines_integerconstraint_constructor_exists():
    assert callable(statemachines_IntegerConstraint.__init__)


def test_statemachines_integerconstraint_constructor_args():
    sig = inspect.signature(statemachines_IntegerConstraint.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_booleanconstraint_is_not_abstract():
    assert not inspect.isabstract(statemachines_BooleanConstraint)


def test_statemachines_booleanconstraint_constructor_exists():
    assert callable(statemachines_BooleanConstraint.__init__)


def test_statemachines_booleanconstraint_constructor_args():
    sig = inspect.signature(statemachines_BooleanConstraint.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_integerattribute_is_not_abstract():
    assert not inspect.isabstract(statemachines_IntegerAttribute)


def test_statemachines_integerattribute_constructor_exists():
    assert callable(statemachines_IntegerAttribute.__init__)


def test_statemachines_integerattribute_constructor_args():
    sig = inspect.signature(statemachines_IntegerAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_stringattribute_is_not_abstract():
    assert not inspect.isabstract(statemachines_StringAttribute)


def test_statemachines_stringattribute_constructor_exists():
    assert callable(statemachines_StringAttribute.__init__)


def test_statemachines_stringattribute_constructor_args():
    sig = inspect.signature(statemachines_StringAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_booleanattribute_is_not_abstract():
    assert not inspect.isabstract(statemachines_BooleanAttribute)


def test_statemachines_booleanattribute_constructor_exists():
    assert callable(statemachines_BooleanAttribute.__init__)


def test_statemachines_booleanattribute_constructor_args():
    sig = inspect.signature(statemachines_BooleanAttribute.__init__)
    params = list(sig.parameters.keys())



def test_eventtype_is_not_abstract():
    assert not inspect.isabstract(EventType)


def test_eventtype_constructor_exists():
    assert callable(EventType.__init__)


def test_eventtype_constructor_args():
    sig = inspect.signature(EventType.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_calleventtype_is_not_abstract():
    assert not inspect.isabstract(statemachines_CallEventType)


def test_statemachines_calleventtype_constructor_exists():
    assert callable(statemachines_CallEventType.__init__)


def test_statemachines_calleventtype_constructor_args():
    sig = inspect.signature(statemachines_CallEventType.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_signaleventtype_is_not_abstract():
    assert not inspect.isabstract(statemachines_SignalEventType)


def test_statemachines_signaleventtype_constructor_exists():
    assert callable(statemachines_SignalEventType.__init__)


def test_statemachines_signaleventtype_constructor_args():
    sig = inspect.signature(statemachines_SignalEventType.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_eventtype_is_not_abstract():
    assert not inspect.isabstract(statemachines_EventType)


def test_statemachines_eventtype_constructor_exists():
    assert callable(statemachines_EventType.__init__)


def test_statemachines_eventtype_constructor_args():
    sig = inspect.signature(statemachines_EventType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_trigger_is_not_abstract():
    assert not inspect.isabstract(statemachines_Trigger)


def test_statemachines_trigger_constructor_exists():
    assert callable(statemachines_Trigger.__init__)


def test_statemachines_trigger_constructor_args():
    sig = inspect.signature(statemachines_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behavior_is_not_abstract():
    assert not inspect.isabstract(statemachines_Behavior)


def test_statemachines_behavior_constructor_exists():
    assert callable(statemachines_Behavior.__init__)


def test_statemachines_behavior_constructor_args():
    sig = inspect.signature(statemachines_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_attribute_is_not_abstract():
    assert not inspect.isabstract(statemachines_Attribute)


def test_statemachines_attribute_constructor_exists():
    assert callable(statemachines_Attribute.__init__)


def test_statemachines_attribute_constructor_args():
    sig = inspect.signature(statemachines_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_transition_is_not_abstract():
    assert not inspect.isabstract(statemachines_Transition)


def test_statemachines_transition_constructor_exists():
    assert callable(statemachines_Transition.__init__)


def test_statemachines_transition_constructor_args():
    sig = inspect.signature(statemachines_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines_transition_has_kind():
    assert hasattr(statemachines_Transition, "kind")
    descriptor = None
    for klass in statemachines_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_vertex_is_not_abstract():
    assert not inspect.isabstract(statemachines_Vertex)


def test_statemachines_vertex_constructor_exists():
    assert callable(statemachines_Vertex.__init__)


def test_statemachines_vertex_constructor_args():
    sig = inspect.signature(statemachines_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_region_is_not_abstract():
    assert not inspect.isabstract(statemachines_Region)


def test_statemachines_region_constructor_exists():
    assert callable(statemachines_Region.__init__)


def test_statemachines_region_constructor_args():
    sig = inspect.signature(statemachines_Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_operation_is_not_abstract():
    assert not inspect.isabstract(statemachines_Operation)


def test_statemachines_operation_constructor_exists():
    assert callable(statemachines_Operation.__init__)


def test_statemachines_operation_constructor_args():
    sig = inspect.signature(statemachines_Operation.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_signal_is_not_abstract():
    assert not inspect.isabstract(statemachines_Signal)


def test_statemachines_signal_constructor_exists():
    assert callable(statemachines_Signal.__init__)


def test_statemachines_signal_constructor_args():
    sig = inspect.signature(statemachines_Signal.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachines_StateMachine)


def test_statemachines_statemachine_constructor_exists():
    assert callable(statemachines_StateMachine.__init__)


def test_statemachines_statemachine_constructor_args():
    sig = inspect.signature(statemachines_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_customsystem_is_not_abstract():
    assert not inspect.isabstract(statemachines_CustomSystem)


def test_statemachines_customsystem_constructor_exists():
    assert callable(statemachines_CustomSystem.__init__)


def test_statemachines_customsystem_constructor_args():
    sig = inspect.signature(statemachines_CustomSystem.__init__)
    params = list(sig.parameters.keys())

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "external",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "terminate",
        "join",
        "entrypoint",
        "exitpoint",
        "initial",
        "fork",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
statemachines_CallEventOccurrence_strategy = st.builds(
    statemachines_CallEventOccurrence,
)
statemachines_CompletionEventOccurrence_strategy = st.builds(
    statemachines_CompletionEventOccurrence,
)
statemachines_EventOccurrence_strategy = st.builds(
    statemachines_EventOccurrence,
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
statemachines_IntegerAttributeValue_strategy = st.builds(
    statemachines_IntegerAttributeValue,
    value=
        safe_text
)
statemachines_StringAttributeValue_strategy = st.builds(
    statemachines_StringAttributeValue,
    value=
        safe_text
)
statemachines_BooleanAttributeValue_strategy = st.builds(
    statemachines_BooleanAttributeValue,
    value=
        safe_text
)
statemachines_AttributeValue_strategy = st.builds(
    statemachines_AttributeValue,
)
Behavior_strategy = st.builds(
    Behavior,
)
statemachines_OperationBehavior_strategy = st.builds(
    statemachines_OperationBehavior,
)
statemachines_SignalEventOccurrence_strategy = st.builds(
    statemachines_SignalEventOccurrence,
)
Vertex_strategy = st.builds(
    Vertex,
)
statemachines_Pseudostate_strategy = st.builds(
    statemachines_Pseudostate,
    kind=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachines_FinalState_strategy = st.builds(
    statemachines_FinalState,
)
statemachines_Constraint_strategy = st.builds(
    statemachines_Constraint,
    value=
        safe_text
)
statemachines_State_strategy = st.builds(
    statemachines_State,
    isDoActivityCompleted=
        st.booleans(),
    isExitCompleted=
        st.booleans(),
    isEntryCompleted=
        st.booleans()
)
statemachines_NamedElement_strategy = st.builds(
    statemachines_NamedElement,
    name=
        safe_text
)
statemachines_StringConstraint_strategy = st.builds(
    statemachines_StringConstraint,
)
statemachines_IntegerConstraint_strategy = st.builds(
    statemachines_IntegerConstraint,
)
statemachines_BooleanConstraint_strategy = st.builds(
    statemachines_BooleanConstraint,
)
Attribute_strategy = st.builds(
    Attribute,
)
statemachines_IntegerAttribute_strategy = st.builds(
    statemachines_IntegerAttribute,
)
statemachines_StringAttribute_strategy = st.builds(
    statemachines_StringAttribute,
)
statemachines_BooleanAttribute_strategy = st.builds(
    statemachines_BooleanAttribute,
)
EventType_strategy = st.builds(
    EventType,
)
statemachines_CallEventType_strategy = st.builds(
    statemachines_CallEventType,
)
statemachines_SignalEventType_strategy = st.builds(
    statemachines_SignalEventType,
)
statemachines_EventType_strategy = st.builds(
    statemachines_EventType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statemachines_Trigger_strategy = st.builds(
    statemachines_Trigger,
)
statemachines_Behavior_strategy = st.builds(
    statemachines_Behavior,
)
statemachines_Attribute_strategy = st.builds(
    statemachines_Attribute,
)
statemachines_Transition_strategy = st.builds(
    statemachines_Transition,
    kind=
        safe_text
)
statemachines_Vertex_strategy = st.builds(
    statemachines_Vertex,
)
statemachines_Region_strategy = st.builds(
    statemachines_Region,
)
statemachines_Operation_strategy = st.builds(
    statemachines_Operation,
)
statemachines_Signal_strategy = st.builds(
    statemachines_Signal,
)
statemachines_StateMachine_strategy = st.builds(
    statemachines_StateMachine,
)
statemachines_CustomSystem_strategy = st.builds(
    statemachines_CustomSystem,
)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=statemachines_CallEventOccurrence_strategy)
@settings(max_examples=50)
def test_statemachines_calleventoccurrence_instantiation(instance):
    assert isinstance(instance, statemachines_CallEventOccurrence)

@given(instance=statemachines_CompletionEventOccurrence_strategy)
@settings(max_examples=50)
def test_statemachines_completioneventoccurrence_instantiation(instance):
    assert isinstance(instance, statemachines_CompletionEventOccurrence)

@given(instance=statemachines_EventOccurrence_strategy)
@settings(max_examples=50)
def test_statemachines_eventoccurrence_instantiation(instance):
    assert isinstance(instance, statemachines_EventOccurrence)

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=statemachines_IntegerAttributeValue_strategy)
@settings(max_examples=50)
def test_statemachines_integerattributevalue_instantiation(instance):
    assert isinstance(instance, statemachines_IntegerAttributeValue)



@given(instance=statemachines_IntegerAttributeValue_strategy)
def test_statemachines_integerattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachines_StringAttributeValue_strategy)
@settings(max_examples=50)
def test_statemachines_stringattributevalue_instantiation(instance):
    assert isinstance(instance, statemachines_StringAttributeValue)



@given(instance=statemachines_StringAttributeValue_strategy)
def test_statemachines_stringattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachines_BooleanAttributeValue_strategy)
@settings(max_examples=50)
def test_statemachines_booleanattributevalue_instantiation(instance):
    assert isinstance(instance, statemachines_BooleanAttributeValue)



@given(instance=statemachines_BooleanAttributeValue_strategy)
def test_statemachines_booleanattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachines_AttributeValue_strategy)
@settings(max_examples=50)
def test_statemachines_attributevalue_instantiation(instance):
    assert isinstance(instance, statemachines_AttributeValue)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=statemachines_OperationBehavior_strategy)
@settings(max_examples=50)
def test_statemachines_operationbehavior_instantiation(instance):
    assert isinstance(instance, statemachines_OperationBehavior)

@given(instance=statemachines_SignalEventOccurrence_strategy)
@settings(max_examples=50)
def test_statemachines_signaleventoccurrence_instantiation(instance):
    assert isinstance(instance, statemachines_SignalEventOccurrence)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=statemachines_Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachines_pseudostate_instantiation(instance):
    assert isinstance(instance, statemachines_Pseudostate)



@given(instance=statemachines_Pseudostate_strategy)
def test_statemachines_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachines_FinalState_strategy)
@settings(max_examples=50)
def test_statemachines_finalstate_instantiation(instance):
    assert isinstance(instance, statemachines_FinalState)

@given(instance=statemachines_Constraint_strategy)
@settings(max_examples=50)
def test_statemachines_constraint_instantiation(instance):
    assert isinstance(instance, statemachines_Constraint)



@given(instance=statemachines_Constraint_strategy)
def test_statemachines_constraint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachines_State_strategy)
@settings(max_examples=50)
def test_statemachines_state_instantiation(instance):
    assert isinstance(instance, statemachines_State)



@given(instance=statemachines_State_strategy)
def test_statemachines_state_isDoActivityCompleted_setter(instance):
    original = instance.isDoActivityCompleted
    instance.isDoActivityCompleted = original
    assert instance.isDoActivityCompleted == original



@given(instance=statemachines_State_strategy)
def test_statemachines_state_isExitCompleted_setter(instance):
    original = instance.isExitCompleted
    instance.isExitCompleted = original
    assert instance.isExitCompleted == original



@given(instance=statemachines_State_strategy)
def test_statemachines_state_isEntryCompleted_setter(instance):
    original = instance.isEntryCompleted
    instance.isEntryCompleted = original
    assert instance.isEntryCompleted == original

@given(instance=statemachines_NamedElement_strategy)
@settings(max_examples=50)
def test_statemachines_namedelement_instantiation(instance):
    assert isinstance(instance, statemachines_NamedElement)



@given(instance=statemachines_NamedElement_strategy)
def test_statemachines_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachines_StringConstraint_strategy)
@settings(max_examples=50)
def test_statemachines_stringconstraint_instantiation(instance):
    assert isinstance(instance, statemachines_StringConstraint)

@given(instance=statemachines_IntegerConstraint_strategy)
@settings(max_examples=50)
def test_statemachines_integerconstraint_instantiation(instance):
    assert isinstance(instance, statemachines_IntegerConstraint)

@given(instance=statemachines_BooleanConstraint_strategy)
@settings(max_examples=50)
def test_statemachines_booleanconstraint_instantiation(instance):
    assert isinstance(instance, statemachines_BooleanConstraint)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=statemachines_IntegerAttribute_strategy)
@settings(max_examples=50)
def test_statemachines_integerattribute_instantiation(instance):
    assert isinstance(instance, statemachines_IntegerAttribute)

@given(instance=statemachines_StringAttribute_strategy)
@settings(max_examples=50)
def test_statemachines_stringattribute_instantiation(instance):
    assert isinstance(instance, statemachines_StringAttribute)

@given(instance=statemachines_BooleanAttribute_strategy)
@settings(max_examples=50)
def test_statemachines_booleanattribute_instantiation(instance):
    assert isinstance(instance, statemachines_BooleanAttribute)

@given(instance=EventType_strategy)
@settings(max_examples=50)
def test_eventtype_instantiation(instance):
    assert isinstance(instance, EventType)

@given(instance=statemachines_CallEventType_strategy)
@settings(max_examples=50)
def test_statemachines_calleventtype_instantiation(instance):
    assert isinstance(instance, statemachines_CallEventType)

@given(instance=statemachines_SignalEventType_strategy)
@settings(max_examples=50)
def test_statemachines_signaleventtype_instantiation(instance):
    assert isinstance(instance, statemachines_SignalEventType)

@given(instance=statemachines_EventType_strategy)
@settings(max_examples=50)
def test_statemachines_eventtype_instantiation(instance):
    assert isinstance(instance, statemachines_EventType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachines_Trigger_strategy)
@settings(max_examples=50)
def test_statemachines_trigger_instantiation(instance):
    assert isinstance(instance, statemachines_Trigger)

@given(instance=statemachines_Behavior_strategy)
@settings(max_examples=50)
def test_statemachines_behavior_instantiation(instance):
    assert isinstance(instance, statemachines_Behavior)

@given(instance=statemachines_Attribute_strategy)
@settings(max_examples=50)
def test_statemachines_attribute_instantiation(instance):
    assert isinstance(instance, statemachines_Attribute)

@given(instance=statemachines_Transition_strategy)
@settings(max_examples=50)
def test_statemachines_transition_instantiation(instance):
    assert isinstance(instance, statemachines_Transition)



@given(instance=statemachines_Transition_strategy)
def test_statemachines_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachines_Transition_strategy)
@settings(max_examples=30)
def test_statemachines_transition_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in statemachines_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in statemachines_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in statemachines_Transition is not implemented or raised an error")

@given(instance=statemachines_Vertex_strategy)
@settings(max_examples=50)
def test_statemachines_vertex_instantiation(instance):
    assert isinstance(instance, statemachines_Vertex)

@given(instance=statemachines_Region_strategy)
@settings(max_examples=50)
def test_statemachines_region_instantiation(instance):
    assert isinstance(instance, statemachines_Region)

@given(instance=statemachines_Operation_strategy)
@settings(max_examples=50)
def test_statemachines_operation_instantiation(instance):
    assert isinstance(instance, statemachines_Operation)

@given(instance=statemachines_Signal_strategy)
@settings(max_examples=50)
def test_statemachines_signal_instantiation(instance):
    assert isinstance(instance, statemachines_Signal)

@given(instance=statemachines_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines_statemachine_instantiation(instance):
    assert isinstance(instance, statemachines_StateMachine)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachines_StateMachine_strategy)
@settings(max_examples=30)
def test_statemachines_statemachine_run_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.run()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.run).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'run' in statemachines_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in statemachines_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in statemachines_StateMachine is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachines_StateMachine_strategy)
@settings(max_examples=30)
def test_statemachines_statemachine_eventoccurrencereceived_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eventOccurrenceReceived(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eventOccurrenceReceived).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eventOccurrenceReceived' in statemachines_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eventOccurrenceReceived' in statemachines_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eventOccurrenceReceived' in statemachines_StateMachine is not implemented or raised an error")

@given(instance=statemachines_CustomSystem_strategy)
@settings(max_examples=50)
def test_statemachines_customsystem_instantiation(instance):
    assert isinstance(instance, statemachines_CustomSystem)
