import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Literal,
    execTraces::BoolLiteral,
    execTraces::IntLiteral,
    execTraces::RealLiteral,
    execTraces::Literal,
    execTraces::Variable,
    execTraces::Edge,
    execTraces::Node,
    execTraces::ExecTraces,
    TransStatus,
    StateStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_exectraces::boolliteral_is_not_abstract():
    assert not inspect.isabstract(execTraces::BoolLiteral)


def test_exectraces::boolliteral_constructor_exists():
    assert callable(execTraces::BoolLiteral.__init__)


def test_exectraces::boolliteral_constructor_args():
    sig = inspect.signature(execTraces::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "bool" in params, "Missing parameter 'bool'"

def test_exectraces::boolliteral_has_bool():
    assert hasattr(execTraces::BoolLiteral, "bool")
    descriptor = None
    for klass in execTraces::BoolLiteral.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_exectraces::intliteral_is_not_abstract():
    assert not inspect.isabstract(execTraces::IntLiteral)


def test_exectraces::intliteral_constructor_exists():
    assert callable(execTraces::IntLiteral.__init__)


def test_exectraces::intliteral_constructor_args():
    sig = inspect.signature(execTraces::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"

def test_exectraces::intliteral_has_int():
    assert hasattr(execTraces::IntLiteral, "int")
    descriptor = None
    for klass in execTraces::IntLiteral.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_exectraces::realliteral_is_not_abstract():
    assert not inspect.isabstract(execTraces::RealLiteral)


def test_exectraces::realliteral_constructor_exists():
    assert callable(execTraces::RealLiteral.__init__)


def test_exectraces::realliteral_constructor_args():
    sig = inspect.signature(execTraces::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intPart" in params, "Missing parameter 'intPart'"
    assert "decimalPart" in params, "Missing parameter 'decimalPart'"

def test_exectraces::realliteral_has_intPart():
    assert hasattr(execTraces::RealLiteral, "intPart")
    descriptor = None
    for klass in execTraces::RealLiteral.__mro__:
        if "intPart" in klass.__dict__:
            descriptor = klass.__dict__["intPart"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::realliteral_has_decimalPart():
    assert hasattr(execTraces::RealLiteral, "decimalPart")
    descriptor = None
    for klass in execTraces::RealLiteral.__mro__:
        if "decimalPart" in klass.__dict__:
            descriptor = klass.__dict__["decimalPart"]
            break
    assert isinstance(descriptor, property)



def test_exectraces::literal_is_not_abstract():
    assert not inspect.isabstract(execTraces::Literal)


def test_exectraces::literal_constructor_exists():
    assert callable(execTraces::Literal.__init__)


def test_exectraces::literal_constructor_args():
    sig = inspect.signature(execTraces::Literal.__init__)
    params = list(sig.parameters.keys())



def test_exectraces::variable_is_not_abstract():
    assert not inspect.isabstract(execTraces::Variable)


def test_exectraces::variable_constructor_exists():
    assert callable(execTraces::Variable.__init__)


def test_exectraces::variable_constructor_args():
    sig = inspect.signature(execTraces::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_exectraces::variable_has_name():
    assert hasattr(execTraces::Variable, "name")
    descriptor = None
    for klass in execTraces::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_exectraces::edge_is_not_abstract():
    assert not inspect.isabstract(execTraces::Edge)


def test_exectraces::edge_constructor_exists():
    assert callable(execTraces::Edge.__init__)


def test_exectraces::edge_constructor_args():
    sig = inspect.signature(execTraces::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "status" in params, "Missing parameter 'status'"
    assert "actions" in params, "Missing parameter 'actions'"

def test_exectraces::edge_has_trigger():
    assert hasattr(execTraces::Edge, "trigger")
    descriptor = None
    for klass in execTraces::Edge.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::edge_has_guard():
    assert hasattr(execTraces::Edge, "guard")
    descriptor = None
    for klass in execTraces::Edge.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::edge_has_status():
    assert hasattr(execTraces::Edge, "status")
    descriptor = None
    for klass in execTraces::Edge.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::edge_has_actions():
    assert hasattr(execTraces::Edge, "actions")
    descriptor = None
    for klass in execTraces::Edge.__mro__:
        if "actions" in klass.__dict__:
            descriptor = klass.__dict__["actions"]
            break
    assert isinstance(descriptor, property)



def test_exectraces::node_is_not_abstract():
    assert not inspect.isabstract(execTraces::Node)


def test_exectraces::node_constructor_exists():
    assert callable(execTraces::Node.__init__)


def test_exectraces::node_constructor_args():
    sig = inspect.signature(execTraces::Node.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "id" in params, "Missing parameter 'id'"
    assert "constraints" in params, "Missing parameter 'constraints'"
    assert "name" in params, "Missing parameter 'name'"
    assert "level" in params, "Missing parameter 'level'"

def test_exectraces::node_has_status():
    assert hasattr(execTraces::Node, "status")
    descriptor = None
    for klass in execTraces::Node.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::node_has_id():
    assert hasattr(execTraces::Node, "id")
    descriptor = None
    for klass in execTraces::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::node_has_constraints():
    assert hasattr(execTraces::Node, "constraints")
    descriptor = None
    for klass in execTraces::Node.__mro__:
        if "constraints" in klass.__dict__:
            descriptor = klass.__dict__["constraints"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::node_has_name():
    assert hasattr(execTraces::Node, "name")
    descriptor = None
    for klass in execTraces::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_exectraces::node_has_level():
    assert hasattr(execTraces::Node, "level")
    descriptor = None
    for klass in execTraces::Node.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_exectraces::exectraces_is_not_abstract():
    assert not inspect.isabstract(execTraces::ExecTraces)


def test_exectraces::exectraces_constructor_exists():
    assert callable(execTraces::ExecTraces.__init__)


def test_exectraces::exectraces_constructor_args():
    sig = inspect.signature(execTraces::ExecTraces.__init__)
    params = list(sig.parameters.keys())
    assert "ComponentName" in params, "Missing parameter 'ComponentName'"

def test_exectraces::exectraces_has_ComponentName():
    assert hasattr(execTraces::ExecTraces, "ComponentName")
    descriptor = None
    for klass in execTraces::ExecTraces.__mro__:
        if "ComponentName" in klass.__dict__:
            descriptor = klass.__dict__["ComponentName"]
            break
    assert isinstance(descriptor, property)

def test_transstatus_exists():
    # Check that the Enumeration exists
    assert TransStatus is not None

def test_transstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransStatus]
    expected_literals = [
        "normal",
        "redundantTrans",
        "unsafeTrans",
        "error",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransStatus"

def test_statestatus_exists():
    # Check that the Enumeration exists
    assert StateStatus is not None

def test_statestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateStatus]
    expected_literals = [
        "Repeated",
        "new",
        "unSafeState",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateStatus"


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
Literal_strategy = st.builds(
    Literal,
)
execTraces::BoolLiteral_strategy = st.builds(
    execTraces::BoolLiteral,
    bool=
        safe_text
)
execTraces::IntLiteral_strategy = st.builds(
    execTraces::IntLiteral,
    int=
        st.integers()
)
execTraces::RealLiteral_strategy = st.builds(
    execTraces::RealLiteral,
    intPart=
        st.integers(),
    decimalPart=
        st.integers()
)
execTraces::Literal_strategy = st.builds(
    execTraces::Literal,
)
execTraces::Variable_strategy = st.builds(
    execTraces::Variable,
    name=
        safe_text
)
execTraces::Edge_strategy = st.builds(
    execTraces::Edge,
    trigger=
        safe_text,
    guard=
        safe_text,
    status=
        safe_text,
    actions=
        safe_text
)
execTraces::Node_strategy = st.builds(
    execTraces::Node,
    status=
        safe_text,
    id=
        st.integers(),
    constraints=
        safe_text,
    name=
        safe_text,
    level=
        st.integers()
)
execTraces::ExecTraces_strategy = st.builds(
    execTraces::ExecTraces,
    ComponentName=
        safe_text
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=execTraces::BoolLiteral_strategy)
@settings(max_examples=50)
def test_exectraces::boolliteral_instantiation(instance):
    assert isinstance(instance, execTraces::BoolLiteral)

@given(instance=execTraces::BoolLiteral_strategy)
def test_exectraces::boolliteral_bool_type(instance):
    assert isinstance(instance.bool, str)


@given(instance=execTraces::BoolLiteral_strategy)
def test_exectraces::boolliteral_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=execTraces::IntLiteral_strategy)
@settings(max_examples=50)
def test_exectraces::intliteral_instantiation(instance):
    assert isinstance(instance, execTraces::IntLiteral)

@given(instance=execTraces::IntLiteral_strategy)
def test_exectraces::intliteral_int_type(instance):
    assert isinstance(instance.int, int)


@given(instance=execTraces::IntLiteral_strategy)
def test_exectraces::intliteral_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=execTraces::RealLiteral_strategy)
@settings(max_examples=50)
def test_exectraces::realliteral_instantiation(instance):
    assert isinstance(instance, execTraces::RealLiteral)

@given(instance=execTraces::RealLiteral_strategy)
def test_exectraces::realliteral_intPart_type(instance):
    assert isinstance(instance.intPart, int)


@given(instance=execTraces::RealLiteral_strategy)
def test_exectraces::realliteral_intPart_setter(instance):
    original = instance.intPart
    instance.intPart = original
    assert instance.intPart == original

@given(instance=execTraces::RealLiteral_strategy)
def test_exectraces::realliteral_decimalPart_type(instance):
    assert isinstance(instance.decimalPart, int)


@given(instance=execTraces::RealLiteral_strategy)
def test_exectraces::realliteral_decimalPart_setter(instance):
    original = instance.decimalPart
    instance.decimalPart = original
    assert instance.decimalPart == original

@given(instance=execTraces::Literal_strategy)
@settings(max_examples=50)
def test_exectraces::literal_instantiation(instance):
    assert isinstance(instance, execTraces::Literal)

@given(instance=execTraces::Variable_strategy)
@settings(max_examples=50)
def test_exectraces::variable_instantiation(instance):
    assert isinstance(instance, execTraces::Variable)

@given(instance=execTraces::Variable_strategy)
def test_exectraces::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=execTraces::Variable_strategy)
def test_exectraces::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=execTraces::Edge_strategy)
@settings(max_examples=50)
def test_exectraces::edge_instantiation(instance):
    assert isinstance(instance, execTraces::Edge)

@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_actions_type(instance):
    assert isinstance(instance.actions, str)


@given(instance=execTraces::Edge_strategy)
def test_exectraces::edge_actions_setter(instance):
    original = instance.actions
    instance.actions = original
    assert instance.actions == original

@given(instance=execTraces::Node_strategy)
@settings(max_examples=50)
def test_exectraces::node_instantiation(instance):
    assert isinstance(instance, execTraces::Node)

@given(instance=execTraces::Node_strategy)
def test_exectraces::node_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=execTraces::Node_strategy)
def test_exectraces::node_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=execTraces::Node_strategy)
def test_exectraces::node_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=execTraces::Node_strategy)
def test_exectraces::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=execTraces::Node_strategy)
def test_exectraces::node_constraints_type(instance):
    assert isinstance(instance.constraints, str)


@given(instance=execTraces::Node_strategy)
def test_exectraces::node_constraints_setter(instance):
    original = instance.constraints
    instance.constraints = original
    assert instance.constraints == original

@given(instance=execTraces::Node_strategy)
def test_exectraces::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=execTraces::Node_strategy)
def test_exectraces::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=execTraces::Node_strategy)
def test_exectraces::node_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=execTraces::Node_strategy)
def test_exectraces::node_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=execTraces::ExecTraces_strategy)
@settings(max_examples=50)
def test_exectraces::exectraces_instantiation(instance):
    assert isinstance(instance, execTraces::ExecTraces)

@given(instance=execTraces::ExecTraces_strategy)
def test_exectraces::exectraces_ComponentName_type(instance):
    assert isinstance(instance.ComponentName, str)


@given(instance=execTraces::ExecTraces_strategy)
def test_exectraces::exectraces_ComponentName_setter(instance):
    original = instance.ComponentName
    instance.ComponentName = original
    assert instance.ComponentName == original
