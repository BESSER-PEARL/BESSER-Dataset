import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    statemachine::FinalState,
    DataElement,
    statemachine::Event,
    statemachine::Variable,
    statemachine::Statechart,
    statemachine::DataElement,
    statemachine::Transition,
    Node,
    statemachine::Pseudostate,
    statemachine::State,
    statemachine::Node,
    statemachine::Region,
    PseudoTypes,
    IOTypes,
    TriggerTypes,
    DataTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(statemachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(statemachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_dataelement_is_not_abstract():
    assert not inspect.isabstract(DataElement)


def test_dataelement_constructor_exists():
    assert callable(DataElement.__init__)


def test_dataelement_constructor_args():
    sig = inspect.signature(DataElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(statemachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(statemachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statemachine::event_has_trigger():
    assert hasattr(statemachine::Event, "trigger")
    descriptor = None
    for klass in statemachine::Event.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::variable_is_not_abstract():
    assert not inspect.isabstract(statemachine::Variable)


def test_statemachine::variable_constructor_exists():
    assert callable(statemachine::Variable.__init__)


def test_statemachine::variable_constructor_args():
    sig = inspect.signature(statemachine::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_statemachine::variable_has_dataType():
    assert hasattr(statemachine::Variable, "dataType")
    descriptor = None
    for klass in statemachine::Variable.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statechart_is_not_abstract():
    assert not inspect.isabstract(statemachine::Statechart)


def test_statemachine::statechart_constructor_exists():
    assert callable(statemachine::Statechart.__init__)


def test_statemachine::statechart_constructor_args():
    sig = inspect.signature(statemachine::Statechart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "UUID" in params, "Missing parameter 'UUID'"

def test_statemachine::statechart_has_name():
    assert hasattr(statemachine::Statechart, "name")
    descriptor = None
    for klass in statemachine::Statechart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::statechart_has_UUID():
    assert hasattr(statemachine::Statechart, "UUID")
    descriptor = None
    for klass in statemachine::Statechart.__mro__:
        if "UUID" in klass.__dict__:
            descriptor = klass.__dict__["UUID"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::dataelement_is_not_abstract():
    assert not inspect.isabstract(statemachine::DataElement)


def test_statemachine::dataelement_constructor_exists():
    assert callable(statemachine::DataElement.__init__)


def test_statemachine::dataelement_constructor_args():
    sig = inspect.signature(statemachine::DataElement.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "ioType" in params, "Missing parameter 'ioType'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::dataelement_has_port():
    assert hasattr(statemachine::DataElement, "port")
    descriptor = None
    for klass in statemachine::DataElement.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::dataelement_has_ioType():
    assert hasattr(statemachine::DataElement, "ioType")
    descriptor = None
    for klass in statemachine::DataElement.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::dataelement_has_name():
    assert hasattr(statemachine::DataElement, "name")
    descriptor = None
    for klass in statemachine::DataElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine::transition_has_expression():
    assert hasattr(statemachine::Transition, "expression")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_priority():
    assert hasattr(statemachine::Transition, "priority")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_id():
    assert hasattr(statemachine::Transition, "id")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine::Pseudostate)


def test_statemachine::pseudostate_constructor_exists():
    assert callable(statemachine::Pseudostate.__init__)


def test_statemachine::pseudostate_constructor_args():
    sig = inspect.signature(statemachine::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "pseudoType" in params, "Missing parameter 'pseudoType'"

def test_statemachine::pseudostate_has_pseudoType():
    assert hasattr(statemachine::Pseudostate, "pseudoType")
    descriptor = None
    for klass in statemachine::Pseudostate.__mro__:
        if "pseudoType" in klass.__dict__:
            descriptor = klass.__dict__["pseudoType"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "entry" in params, "Missing parameter 'entry'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "do" in params, "Missing parameter 'do'"

def test_statemachine::state_has_entry():
    assert hasattr(statemachine::State, "entry")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_exit():
    assert hasattr(statemachine::State, "exit")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_do():
    assert hasattr(statemachine::State, "do")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "do" in klass.__dict__:
            descriptor = klass.__dict__["do"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::node_is_not_abstract():
    assert not inspect.isabstract(statemachine::Node)


def test_statemachine::node_constructor_exists():
    assert callable(statemachine::Node.__init__)


def test_statemachine::node_constructor_args():
    sig = inspect.signature(statemachine::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine::node_has_name():
    assert hasattr(statemachine::Node, "name")
    descriptor = None
    for klass in statemachine::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::node_has_id():
    assert hasattr(statemachine::Node, "id")
    descriptor = None
    for klass in statemachine::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::region_is_not_abstract():
    assert not inspect.isabstract(statemachine::Region)


def test_statemachine::region_constructor_exists():
    assert callable(statemachine::Region.__init__)


def test_statemachine::region_constructor_args():
    sig = inspect.signature(statemachine::Region.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_statemachine::region_has_priority():
    assert hasattr(statemachine::Region, "priority")
    descriptor = None
    for klass in statemachine::Region.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_pseudotypes_exists():
    # Check that the Enumeration exists
    assert PseudoTypes is not None

def test_pseudotypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoTypes]
    expected_literals = [
        "initial",
        "choice",
        "junction",
        "entryPoint",
        "join",
        "shallowHistory",
        "exitPoint",
        "fork",
        "deepHistory",
        "terminate",
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
        "local",
        "output",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IOTypes"

def test_triggertypes_exists():
    # Check that the Enumeration exists
    assert TriggerTypes is not None

def test_triggertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerTypes]
    expected_literals = [
        "rising",
        "functionCall",
        "falling",
        "either",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerTypes"

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "boolean",
        "double",
        "int",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"


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
State_strategy = st.builds(
    State,
)
statemachine::FinalState_strategy = st.builds(
    statemachine::FinalState,
)
DataElement_strategy = st.builds(
    DataElement,
)
statemachine::Event_strategy = st.builds(
    statemachine::Event,
    trigger=
        safe_text
)
statemachine::Variable_strategy = st.builds(
    statemachine::Variable,
    dataType=
        safe_text
)
statemachine::Statechart_strategy = st.builds(
    statemachine::Statechart,
    name=
        safe_text,
    UUID=
        safe_text
)
statemachine::DataElement_strategy = st.builds(
    statemachine::DataElement,
    port=
        st.integers(),
    ioType=
        safe_text,
    name=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    expression=
        safe_text,
    priority=
        st.integers(),
    id=
        st.integers()
)
Node_strategy = st.builds(
    Node,
)
statemachine::Pseudostate_strategy = st.builds(
    statemachine::Pseudostate,
    pseudoType=
        safe_text
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    entry=
        safe_text,
    exit=
        safe_text,
    do=
        safe_text
)
statemachine::Node_strategy = st.builds(
    statemachine::Node,
    name=
        safe_text,
    id=
        st.integers()
)
statemachine::Region_strategy = st.builds(
    statemachine::Region,
    priority=
        st.integers()
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine::FinalState)

@given(instance=DataElement_strategy)
@settings(max_examples=50)
def test_dataelement_instantiation(instance):
    assert isinstance(instance, DataElement)

@given(instance=statemachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, statemachine::Event)

@given(instance=statemachine::Event_strategy)
def test_statemachine::event_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=statemachine::Event_strategy)
def test_statemachine::event_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=statemachine::Variable_strategy)
@settings(max_examples=50)
def test_statemachine::variable_instantiation(instance):
    assert isinstance(instance, statemachine::Variable)

@given(instance=statemachine::Variable_strategy)
def test_statemachine::variable_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=statemachine::Variable_strategy)
def test_statemachine::variable_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=statemachine::Statechart_strategy)
@settings(max_examples=50)
def test_statemachine::statechart_instantiation(instance):
    assert isinstance(instance, statemachine::Statechart)

@given(instance=statemachine::Statechart_strategy)
def test_statemachine::statechart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Statechart_strategy)
def test_statemachine::statechart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Statechart_strategy)
def test_statemachine::statechart_UUID_type(instance):
    assert isinstance(instance.UUID, str)


@given(instance=statemachine::Statechart_strategy)
def test_statemachine::statechart_UUID_setter(instance):
    original = instance.UUID
    instance.UUID = original
    assert instance.UUID == original

@given(instance=statemachine::DataElement_strategy)
@settings(max_examples=50)
def test_statemachine::dataelement_instantiation(instance):
    assert isinstance(instance, statemachine::DataElement)

@given(instance=statemachine::DataElement_strategy)
def test_statemachine::dataelement_port_type(instance):
    assert isinstance(instance.port, int)


@given(instance=statemachine::DataElement_strategy)
def test_statemachine::dataelement_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=statemachine::DataElement_strategy)
def test_statemachine::dataelement_ioType_type(instance):
    assert isinstance(instance.ioType, str)


@given(instance=statemachine::DataElement_strategy)
def test_statemachine::dataelement_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original

@given(instance=statemachine::DataElement_strategy)
def test_statemachine::dataelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::DataElement_strategy)
def test_statemachine::dataelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=statemachine::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachine::pseudostate_instantiation(instance):
    assert isinstance(instance, statemachine::Pseudostate)

@given(instance=statemachine::Pseudostate_strategy)
def test_statemachine::pseudostate_pseudoType_type(instance):
    assert isinstance(instance.pseudoType, str)


@given(instance=statemachine::Pseudostate_strategy)
def test_statemachine::pseudostate_pseudoType_setter(instance):
    original = instance.pseudoType
    instance.pseudoType = original
    assert instance.pseudoType == original

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_entry_type(instance):
    assert isinstance(instance.entry, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_exit_type(instance):
    assert isinstance(instance.exit, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_do_type(instance):
    assert isinstance(instance.do, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_do_setter(instance):
    original = instance.do
    instance.do = original
    assert instance.do == original

@given(instance=statemachine::Node_strategy)
@settings(max_examples=50)
def test_statemachine::node_instantiation(instance):
    assert isinstance(instance, statemachine::Node)

@given(instance=statemachine::Node_strategy)
def test_statemachine::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Node_strategy)
def test_statemachine::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Node_strategy)
def test_statemachine::node_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=statemachine::Node_strategy)
def test_statemachine::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::Region_strategy)
@settings(max_examples=50)
def test_statemachine::region_instantiation(instance):
    assert isinstance(instance, statemachine::Region)

@given(instance=statemachine::Region_strategy)
def test_statemachine::region_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=statemachine::Region_strategy)
def test_statemachine::region_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original
