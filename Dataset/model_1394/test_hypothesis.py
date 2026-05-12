import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Statechart,
    DataElement,
    statemachine_Event,
    statemachine_Variable,
    State,
    statemachine_FinalState,
    statemachine_Transition,
    statemachine_Node,
    statemachine_Region,
    statemachine_DataElement,
    Node,
    statemachine_Pseudostate,
    statemachine_State,
    PseudoTypes,
    IOTypes,
    DataTypes,
    TriggerTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_statechart_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statechart)


def test_statemachine_statechart_constructor_exists():
    assert callable(statemachine_Statechart.__init__)


def test_statemachine_statechart_constructor_args():
    sig = inspect.signature(statemachine_Statechart.__init__)
    params = list(sig.parameters.keys())
    assert "UUID" in params, "Missing parameter 'UUID'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statechart_has_UUID():
    assert hasattr(statemachine_Statechart, "UUID")
    descriptor = None
    for klass in statemachine_Statechart.__mro__:
        if "UUID" in klass.__dict__:
            descriptor = klass.__dict__["UUID"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_statechart_has_name():
    assert hasattr(statemachine_Statechart, "name")
    descriptor = None
    for klass in statemachine_Statechart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dataelement_is_not_abstract():
    assert not inspect.isabstract(DataElement)


def test_dataelement_constructor_exists():
    assert callable(DataElement.__init__)


def test_dataelement_constructor_args():
    sig = inspect.signature(DataElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statemachine_event_has_trigger():
    assert hasattr(statemachine_Event, "trigger")
    descriptor = None
    for klass in statemachine_Event.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_variable_is_not_abstract():
    assert not inspect.isabstract(statemachine_Variable)


def test_statemachine_variable_constructor_exists():
    assert callable(statemachine_Variable.__init__)


def test_statemachine_variable_constructor_args():
    sig = inspect.signature(statemachine_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_statemachine_variable_has_dataType():
    assert hasattr(statemachine_Variable, "dataType")
    descriptor = None
    for klass in statemachine_Variable.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_transition_has_priority():
    assert hasattr(statemachine_Transition, "priority")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_expression():
    assert hasattr(statemachine_Transition, "expression")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_id():
    assert hasattr(statemachine_Transition, "id")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_node_is_not_abstract():
    assert not inspect.isabstract(statemachine_Node)


def test_statemachine_node_constructor_exists():
    assert callable(statemachine_Node.__init__)


def test_statemachine_node_constructor_args():
    sig = inspect.signature(statemachine_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_node_has_id():
    assert hasattr(statemachine_Node, "id")
    descriptor = None
    for klass in statemachine_Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_node_has_name():
    assert hasattr(statemachine_Node, "name")
    descriptor = None
    for klass in statemachine_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_region_is_not_abstract():
    assert not inspect.isabstract(statemachine_Region)


def test_statemachine_region_constructor_exists():
    assert callable(statemachine_Region.__init__)


def test_statemachine_region_constructor_args():
    sig = inspect.signature(statemachine_Region.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_statemachine_region_has_priority():
    assert hasattr(statemachine_Region, "priority")
    descriptor = None
    for klass in statemachine_Region.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_dataelement_is_not_abstract():
    assert not inspect.isabstract(statemachine_DataElement)


def test_statemachine_dataelement_constructor_exists():
    assert callable(statemachine_DataElement.__init__)


def test_statemachine_dataelement_constructor_args():
    sig = inspect.signature(statemachine_DataElement.__init__)
    params = list(sig.parameters.keys())
    assert "ioType" in params, "Missing parameter 'ioType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "port" in params, "Missing parameter 'port'"

def test_statemachine_dataelement_has_ioType():
    assert hasattr(statemachine_DataElement, "ioType")
    descriptor = None
    for klass in statemachine_DataElement.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_dataelement_has_name():
    assert hasattr(statemachine_DataElement, "name")
    descriptor = None
    for klass in statemachine_DataElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_dataelement_has_port():
    assert hasattr(statemachine_DataElement, "port")
    descriptor = None
    for klass in statemachine_DataElement.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine_Pseudostate)


def test_statemachine_pseudostate_constructor_exists():
    assert callable(statemachine_Pseudostate.__init__)


def test_statemachine_pseudostate_constructor_args():
    sig = inspect.signature(statemachine_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "pseudoType" in params, "Missing parameter 'pseudoType'"

def test_statemachine_pseudostate_has_pseudoType():
    assert hasattr(statemachine_Pseudostate, "pseudoType")
    descriptor = None
    for klass in statemachine_Pseudostate.__mro__:
        if "pseudoType" in klass.__dict__:
            descriptor = klass.__dict__["pseudoType"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "do" in params, "Missing parameter 'do'"
    assert "entry" in params, "Missing parameter 'entry'"
    assert "exit" in params, "Missing parameter 'exit'"

def test_statemachine_state_has_do():
    assert hasattr(statemachine_State, "do")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "do" in klass.__dict__:
            descriptor = klass.__dict__["do"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_entry():
    assert hasattr(statemachine_State, "entry")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_exit():
    assert hasattr(statemachine_State, "exit")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_pseudotypes_exists():
    # Check that the Enumeration exists
    assert PseudoTypes is not None

def test_pseudotypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoTypes]
    expected_literals = [
        "choice",
        "fork",
        "junction",
        "shallowHistory",
        "terminate",
        "join",
        "initial",
        "deepHistory",
        "entryPoint",
        "exitPoint",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoTypes"

def test_iotypes_exists():
    # Check that the Enumeration exists
    assert IOTypes is not None

def test_iotypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IOTypes]
    expected_literals = [
        "input",
        "output",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IOTypes"

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "double",
        "int",
        "boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"

def test_triggertypes_exists():
    # Check that the Enumeration exists
    assert TriggerTypes is not None

def test_triggertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerTypes]
    expected_literals = [
        "falling",
        "either",
        "functionCall",
        "rising",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerTypes"


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
statemachine_Statechart_strategy = st.builds(
    statemachine_Statechart,
    UUID=
        safe_text,
    name=
        safe_text
)
DataElement_strategy = st.builds(
    DataElement,
)
statemachine_Event_strategy = st.builds(
    statemachine_Event,
    trigger=
        safe_text
)
statemachine_Variable_strategy = st.builds(
    statemachine_Variable,
    dataType=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    priority=
        st.integers(),
    expression=
        safe_text,
    id=
        st.integers()
)
statemachine_Node_strategy = st.builds(
    statemachine_Node,
    id=
        st.integers(),
    name=
        safe_text
)
statemachine_Region_strategy = st.builds(
    statemachine_Region,
    priority=
        st.integers()
)
statemachine_DataElement_strategy = st.builds(
    statemachine_DataElement,
    ioType=
        safe_text,
    name=
        safe_text,
    port=
        st.integers()
)
Node_strategy = st.builds(
    Node,
)
statemachine_Pseudostate_strategy = st.builds(
    statemachine_Pseudostate,
    pseudoType=
        safe_text
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    do=
        safe_text,
    entry=
        safe_text,
    exit=
        safe_text
)

@given(instance=statemachine_Statechart_strategy)
@settings(max_examples=50)
def test_statemachine_statechart_instantiation(instance):
    assert isinstance(instance, statemachine_Statechart)



@given(instance=statemachine_Statechart_strategy)
def test_statemachine_statechart_UUID_setter(instance):
    original = instance.UUID
    instance.UUID = original
    assert instance.UUID == original



@given(instance=statemachine_Statechart_strategy)
def test_statemachine_statechart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataElement_strategy)
@settings(max_examples=50)
def test_dataelement_instantiation(instance):
    assert isinstance(instance, DataElement)

@given(instance=statemachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)



@given(instance=statemachine_Event_strategy)
def test_statemachine_event_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=statemachine_Variable_strategy)
@settings(max_examples=50)
def test_statemachine_variable_instantiation(instance):
    assert isinstance(instance, statemachine_Variable)



@given(instance=statemachine_Variable_strategy)
def test_statemachine_variable_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine_Node_strategy)
@settings(max_examples=50)
def test_statemachine_node_instantiation(instance):
    assert isinstance(instance, statemachine_Node)



@given(instance=statemachine_Node_strategy)
def test_statemachine_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=statemachine_Node_strategy)
def test_statemachine_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Region_strategy)
@settings(max_examples=50)
def test_statemachine_region_instantiation(instance):
    assert isinstance(instance, statemachine_Region)



@given(instance=statemachine_Region_strategy)
def test_statemachine_region_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=statemachine_DataElement_strategy)
@settings(max_examples=50)
def test_statemachine_dataelement_instantiation(instance):
    assert isinstance(instance, statemachine_DataElement)



@given(instance=statemachine_DataElement_strategy)
def test_statemachine_dataelement_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original



@given(instance=statemachine_DataElement_strategy)
def test_statemachine_dataelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachine_DataElement_strategy)
def test_statemachine_dataelement_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=statemachine_Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachine_pseudostate_instantiation(instance):
    assert isinstance(instance, statemachine_Pseudostate)



@given(instance=statemachine_Pseudostate_strategy)
def test_statemachine_pseudostate_pseudoType_setter(instance):
    original = instance.pseudoType
    instance.pseudoType = original
    assert instance.pseudoType == original

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_do_setter(instance):
    original = instance.do
    instance.do = original
    assert instance.do == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original
