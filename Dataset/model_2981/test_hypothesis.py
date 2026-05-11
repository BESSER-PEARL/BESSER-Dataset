import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    automata::NumberAction,
    automata::BooleanAction,
    automata::StringAction,
    Guard,
    automata::NumberGuard,
    automata::BooleanGuard,
    Variable,
    automata::NumberVariable,
    automata::BooleanVariable,
    automata::StringVariable,
    automata::Action,
    automata::Guard,
    automata::Variable,
    automata::Transition,
    automata::State,
    automata::StringGuard,
    automata::Automaton,
    BooleanOperator,
    StringOperator,
    NumberOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_automata::numberaction_is_not_abstract():
    assert not inspect.isabstract(automata::NumberAction)


def test_automata::numberaction_constructor_exists():
    assert callable(automata::NumberAction.__init__)


def test_automata::numberaction_constructor_args():
    sig = inspect.signature(automata::NumberAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_automata::numberaction_has_value():
    assert hasattr(automata::NumberAction, "value")
    descriptor = None
    for klass in automata::NumberAction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automata::booleanaction_is_not_abstract():
    assert not inspect.isabstract(automata::BooleanAction)


def test_automata::booleanaction_constructor_exists():
    assert callable(automata::BooleanAction.__init__)


def test_automata::booleanaction_constructor_args():
    sig = inspect.signature(automata::BooleanAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_automata::booleanaction_has_value():
    assert hasattr(automata::BooleanAction, "value")
    descriptor = None
    for klass in automata::BooleanAction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automata::stringaction_is_not_abstract():
    assert not inspect.isabstract(automata::StringAction)


def test_automata::stringaction_constructor_exists():
    assert callable(automata::StringAction.__init__)


def test_automata::stringaction_constructor_args():
    sig = inspect.signature(automata::StringAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_automata::stringaction_has_value():
    assert hasattr(automata::StringAction, "value")
    descriptor = None
    for klass in automata::StringAction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_automata::numberguard_is_not_abstract():
    assert not inspect.isabstract(automata::NumberGuard)


def test_automata::numberguard_constructor_exists():
    assert callable(automata::NumberGuard.__init__)


def test_automata::numberguard_constructor_args():
    sig = inspect.signature(automata::NumberGuard.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_automata::numberguard_has_operator():
    assert hasattr(automata::NumberGuard, "operator")
    descriptor = None
    for klass in automata::NumberGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_automata::numberguard_has_value():
    assert hasattr(automata::NumberGuard, "value")
    descriptor = None
    for klass in automata::NumberGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automata::booleanguard_is_not_abstract():
    assert not inspect.isabstract(automata::BooleanGuard)


def test_automata::booleanguard_constructor_exists():
    assert callable(automata::BooleanGuard.__init__)


def test_automata::booleanguard_constructor_args():
    sig = inspect.signature(automata::BooleanGuard.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_automata::booleanguard_has_operator():
    assert hasattr(automata::BooleanGuard, "operator")
    descriptor = None
    for klass in automata::BooleanGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_automata::booleanguard_has_value():
    assert hasattr(automata::BooleanGuard, "value")
    descriptor = None
    for klass in automata::BooleanGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_automata::numbervariable_is_not_abstract():
    assert not inspect.isabstract(automata::NumberVariable)


def test_automata::numbervariable_constructor_exists():
    assert callable(automata::NumberVariable.__init__)


def test_automata::numbervariable_constructor_args():
    sig = inspect.signature(automata::NumberVariable.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_automata::numbervariable_has_initialValue():
    assert hasattr(automata::NumberVariable, "initialValue")
    descriptor = None
    for klass in automata::NumberVariable.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_automata::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(automata::BooleanVariable)


def test_automata::booleanvariable_constructor_exists():
    assert callable(automata::BooleanVariable.__init__)


def test_automata::booleanvariable_constructor_args():
    sig = inspect.signature(automata::BooleanVariable.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_automata::booleanvariable_has_initialValue():
    assert hasattr(automata::BooleanVariable, "initialValue")
    descriptor = None
    for klass in automata::BooleanVariable.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_automata::stringvariable_is_not_abstract():
    assert not inspect.isabstract(automata::StringVariable)


def test_automata::stringvariable_constructor_exists():
    assert callable(automata::StringVariable.__init__)


def test_automata::stringvariable_constructor_args():
    sig = inspect.signature(automata::StringVariable.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_automata::stringvariable_has_initialValue():
    assert hasattr(automata::StringVariable, "initialValue")
    descriptor = None
    for klass in automata::StringVariable.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_automata::action_is_not_abstract():
    assert not inspect.isabstract(automata::Action)


def test_automata::action_constructor_exists():
    assert callable(automata::Action.__init__)


def test_automata::action_constructor_args():
    sig = inspect.signature(automata::Action.__init__)
    params = list(sig.parameters.keys())



def test_automata::guard_is_not_abstract():
    assert not inspect.isabstract(automata::Guard)


def test_automata::guard_constructor_exists():
    assert callable(automata::Guard.__init__)


def test_automata::guard_constructor_args():
    sig = inspect.signature(automata::Guard.__init__)
    params = list(sig.parameters.keys())



def test_automata::variable_is_not_abstract():
    assert not inspect.isabstract(automata::Variable)


def test_automata::variable_constructor_exists():
    assert callable(automata::Variable.__init__)


def test_automata::variable_constructor_args():
    sig = inspect.signature(automata::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata::variable_has_name():
    assert hasattr(automata::Variable, "name")
    descriptor = None
    for klass in automata::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::transition_is_not_abstract():
    assert not inspect.isabstract(automata::Transition)


def test_automata::transition_constructor_exists():
    assert callable(automata::Transition.__init__)


def test_automata::transition_constructor_args():
    sig = inspect.signature(automata::Transition.__init__)
    params = list(sig.parameters.keys())



def test_automata::state_is_not_abstract():
    assert not inspect.isabstract(automata::State)


def test_automata::state_constructor_exists():
    assert callable(automata::State.__init__)


def test_automata::state_constructor_args():
    sig = inspect.signature(automata::State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_automata::state_has_initial():
    assert hasattr(automata::State, "initial")
    descriptor = None
    for klass in automata::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_automata::state_has_name():
    assert hasattr(automata::State, "name")
    descriptor = None
    for klass in automata::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::stringguard_is_not_abstract():
    assert not inspect.isabstract(automata::StringGuard)


def test_automata::stringguard_constructor_exists():
    assert callable(automata::StringGuard.__init__)


def test_automata::stringguard_constructor_args():
    sig = inspect.signature(automata::StringGuard.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_automata::stringguard_has_operator():
    assert hasattr(automata::StringGuard, "operator")
    descriptor = None
    for klass in automata::StringGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_automata::stringguard_has_value():
    assert hasattr(automata::StringGuard, "value")
    descriptor = None
    for klass in automata::StringGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automata::automaton_is_not_abstract():
    assert not inspect.isabstract(automata::Automaton)


def test_automata::automaton_constructor_exists():
    assert callable(automata::Automaton.__init__)


def test_automata::automaton_constructor_args():
    sig = inspect.signature(automata::Automaton.__init__)
    params = list(sig.parameters.keys())

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "Unequal",
        "Equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_stringoperator_exists():
    # Check that the Enumeration exists
    assert StringOperator is not None

def test_stringoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringOperator]
    expected_literals = [
        "Equal",
        "Unequal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringOperator"

def test_numberoperator_exists():
    # Check that the Enumeration exists
    assert NumberOperator is not None

def test_numberoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberOperator]
    expected_literals = [
        "LessOrEqualThan",
        "GreaterThan",
        "Unequal",
        "GreaterOrEqualThan",
        "LessThan",
        "Equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberOperator"


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
Action_strategy = st.builds(
    Action,
)
automata::NumberAction_strategy = st.builds(
    automata::NumberAction,
    value=
        safe_text
)
automata::BooleanAction_strategy = st.builds(
    automata::BooleanAction,
    value=
        st.booleans()
)
automata::StringAction_strategy = st.builds(
    automata::StringAction,
    value=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
automata::NumberGuard_strategy = st.builds(
    automata::NumberGuard,
    operator=
        safe_text,
    value=
        safe_text
)
automata::BooleanGuard_strategy = st.builds(
    automata::BooleanGuard,
    operator=
        safe_text,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
automata::NumberVariable_strategy = st.builds(
    automata::NumberVariable,
    initialValue=
        safe_text
)
automata::BooleanVariable_strategy = st.builds(
    automata::BooleanVariable,
    initialValue=
        st.booleans()
)
automata::StringVariable_strategy = st.builds(
    automata::StringVariable,
    initialValue=
        safe_text
)
automata::Action_strategy = st.builds(
    automata::Action,
)
automata::Guard_strategy = st.builds(
    automata::Guard,
)
automata::Variable_strategy = st.builds(
    automata::Variable,
    name=
        safe_text
)
automata::Transition_strategy = st.builds(
    automata::Transition,
)
automata::State_strategy = st.builds(
    automata::State,
    initial=
        st.booleans(),
    name=
        safe_text
)
automata::StringGuard_strategy = st.builds(
    automata::StringGuard,
    operator=
        safe_text,
    value=
        safe_text
)
automata::Automaton_strategy = st.builds(
    automata::Automaton,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=automata::NumberAction_strategy)
@settings(max_examples=50)
def test_automata::numberaction_instantiation(instance):
    assert isinstance(instance, automata::NumberAction)

@given(instance=automata::NumberAction_strategy)
def test_automata::numberaction_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automata::NumberAction_strategy)
def test_automata::numberaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::BooleanAction_strategy)
@settings(max_examples=50)
def test_automata::booleanaction_instantiation(instance):
    assert isinstance(instance, automata::BooleanAction)

@given(instance=automata::BooleanAction_strategy)
def test_automata::booleanaction_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=automata::BooleanAction_strategy)
def test_automata::booleanaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::StringAction_strategy)
@settings(max_examples=50)
def test_automata::stringaction_instantiation(instance):
    assert isinstance(instance, automata::StringAction)

@given(instance=automata::StringAction_strategy)
def test_automata::stringaction_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automata::StringAction_strategy)
def test_automata::stringaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=automata::NumberGuard_strategy)
@settings(max_examples=50)
def test_automata::numberguard_instantiation(instance):
    assert isinstance(instance, automata::NumberGuard)

@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::BooleanGuard_strategy)
@settings(max_examples=50)
def test_automata::booleanguard_instantiation(instance):
    assert isinstance(instance, automata::BooleanGuard)

@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=automata::NumberVariable_strategy)
@settings(max_examples=50)
def test_automata::numbervariable_instantiation(instance):
    assert isinstance(instance, automata::NumberVariable)

@given(instance=automata::NumberVariable_strategy)
def test_automata::numbervariable_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=automata::NumberVariable_strategy)
def test_automata::numbervariable_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=automata::BooleanVariable_strategy)
@settings(max_examples=50)
def test_automata::booleanvariable_instantiation(instance):
    assert isinstance(instance, automata::BooleanVariable)

@given(instance=automata::BooleanVariable_strategy)
def test_automata::booleanvariable_initialValue_type(instance):
    assert isinstance(instance.initialValue, bool)


@given(instance=automata::BooleanVariable_strategy)
def test_automata::booleanvariable_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=automata::StringVariable_strategy)
@settings(max_examples=50)
def test_automata::stringvariable_instantiation(instance):
    assert isinstance(instance, automata::StringVariable)

@given(instance=automata::StringVariable_strategy)
def test_automata::stringvariable_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=automata::StringVariable_strategy)
def test_automata::stringvariable_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=automata::Action_strategy)
@settings(max_examples=50)
def test_automata::action_instantiation(instance):
    assert isinstance(instance, automata::Action)

@given(instance=automata::Guard_strategy)
@settings(max_examples=50)
def test_automata::guard_instantiation(instance):
    assert isinstance(instance, automata::Guard)

@given(instance=automata::Variable_strategy)
@settings(max_examples=50)
def test_automata::variable_instantiation(instance):
    assert isinstance(instance, automata::Variable)

@given(instance=automata::Variable_strategy)
def test_automata::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::Variable_strategy)
def test_automata::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Transition_strategy)
@settings(max_examples=50)
def test_automata::transition_instantiation(instance):
    assert isinstance(instance, automata::Transition)

@given(instance=automata::State_strategy)
@settings(max_examples=50)
def test_automata::state_instantiation(instance):
    assert isinstance(instance, automata::State)

@given(instance=automata::State_strategy)
def test_automata::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=automata::State_strategy)
def test_automata::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=automata::State_strategy)
def test_automata::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::State_strategy)
def test_automata::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::StringGuard_strategy)
@settings(max_examples=50)
def test_automata::stringguard_instantiation(instance):
    assert isinstance(instance, automata::StringGuard)

@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::Automaton_strategy)
@settings(max_examples=50)
def test_automata::automaton_instantiation(instance):
    assert isinstance(instance, automata::Automaton)
