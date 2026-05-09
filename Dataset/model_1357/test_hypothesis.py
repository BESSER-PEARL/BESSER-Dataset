import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NumberValue,
    statemachine::LongValue,
    ConstantValue,
    statemachine::BooleanValue,
    statemachine::NumberValue,
    statemachine::StringValue,
    GState,
    statemachine::GCompositeState,
    statemachine::Value,
    GAbstractState,
    statemachine::GStartState,
    Named,
    statemachine::Transition,
    statemachine::GState,
    statemachine::GAbstractAction,
    statemachine::GAbstractState,
    Value,
    statemachine::ConstantValue,
    statemachine::GetParameter,
    statemachine::Call,
    GAbstractAction,
    statemachine::CallAction,
    statemachine::Parameter,
    GCompositeState,
    statemachine::GStatemachine,
    statemachine::GStopState,
    statemachine::Named,
    ActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::longvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine::LongValue)


def test_statemachine::longvalue_constructor_exists():
    assert callable(statemachine::LongValue.__init__)


def test_statemachine::longvalue_constructor_args():
    sig = inspect.signature(statemachine::LongValue.__init__)
    params = list(sig.parameters.keys())



def test_constantvalue_is_not_abstract():
    assert not inspect.isabstract(ConstantValue)


def test_constantvalue_constructor_exists():
    assert callable(ConstantValue.__init__)


def test_constantvalue_constructor_args():
    sig = inspect.signature(ConstantValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine::BooleanValue)


def test_statemachine::booleanvalue_constructor_exists():
    assert callable(statemachine::BooleanValue.__init__)


def test_statemachine::booleanvalue_constructor_args():
    sig = inspect.signature(statemachine::BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::numbervalue_is_not_abstract():
    assert not inspect.isabstract(statemachine::NumberValue)


def test_statemachine::numbervalue_constructor_exists():
    assert callable(statemachine::NumberValue.__init__)


def test_statemachine::numbervalue_constructor_args():
    sig = inspect.signature(statemachine::NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::stringvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine::StringValue)


def test_statemachine::stringvalue_constructor_exists():
    assert callable(statemachine::StringValue.__init__)


def test_statemachine::stringvalue_constructor_args():
    sig = inspect.signature(statemachine::StringValue.__init__)
    params = list(sig.parameters.keys())



def test_gstate_is_not_abstract():
    assert not inspect.isabstract(GState)


def test_gstate_constructor_exists():
    assert callable(GState.__init__)


def test_gstate_constructor_args():
    sig = inspect.signature(GState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::gcompositestate_is_not_abstract():
    assert not inspect.isabstract(statemachine::GCompositeState)


def test_statemachine::gcompositestate_constructor_exists():
    assert callable(statemachine::GCompositeState.__init__)


def test_statemachine::gcompositestate_constructor_args():
    sig = inspect.signature(statemachine::GCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::value_is_not_abstract():
    assert not inspect.isabstract(statemachine::Value)


def test_statemachine::value_constructor_exists():
    assert callable(statemachine::Value.__init__)


def test_statemachine::value_constructor_args():
    sig = inspect.signature(statemachine::Value.__init__)
    params = list(sig.parameters.keys())



def test_gabstractstate_is_not_abstract():
    assert not inspect.isabstract(GAbstractState)


def test_gabstractstate_constructor_exists():
    assert callable(GAbstractState.__init__)


def test_gabstractstate_constructor_args():
    sig = inspect.signature(GAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::gstartstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::GStartState)


def test_statemachine::gstartstate_constructor_exists():
    assert callable(statemachine::GStartState.__init__)


def test_statemachine::gstartstate_constructor_args():
    sig = inspect.signature(statemachine::GStartState.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "preserveTimers" in params, "Missing parameter 'preserveTimers'"

def test_statemachine::transition_has_preserveTimers():
    assert hasattr(statemachine::Transition, "preserveTimers")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "preserveTimers" in klass.__dict__:
            descriptor = klass.__dict__["preserveTimers"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::gstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::GState)


def test_statemachine::gstate_constructor_exists():
    assert callable(statemachine::GState.__init__)


def test_statemachine::gstate_constructor_args():
    sig = inspect.signature(statemachine::GState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::gabstractaction_is_not_abstract():
    assert not inspect.isabstract(statemachine::GAbstractAction)


def test_statemachine::gabstractaction_constructor_exists():
    assert callable(statemachine::GAbstractAction.__init__)


def test_statemachine::gabstractaction_constructor_args():
    sig = inspect.signature(statemachine::GAbstractAction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine::gabstractaction_has_kind():
    assert hasattr(statemachine::GAbstractAction, "kind")
    descriptor = None
    for klass in statemachine::GAbstractAction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::gabstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::GAbstractState)


def test_statemachine::gabstractstate_constructor_exists():
    assert callable(statemachine::GAbstractState.__init__)


def test_statemachine::gabstractstate_constructor_args():
    sig = inspect.signature(statemachine::GAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::constantvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine::ConstantValue)


def test_statemachine::constantvalue_constructor_exists():
    assert callable(statemachine::ConstantValue.__init__)


def test_statemachine::constantvalue_constructor_args():
    sig = inspect.signature(statemachine::ConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine::constantvalue_has_value():
    assert hasattr(statemachine::ConstantValue, "value")
    descriptor = None
    for klass in statemachine::ConstantValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::getparameter_is_not_abstract():
    assert not inspect.isabstract(statemachine::GetParameter)


def test_statemachine::getparameter_constructor_exists():
    assert callable(statemachine::GetParameter.__init__)


def test_statemachine::getparameter_constructor_args():
    sig = inspect.signature(statemachine::GetParameter.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::call_is_not_abstract():
    assert not inspect.isabstract(statemachine::Call)


def test_statemachine::call_constructor_exists():
    assert callable(statemachine::Call.__init__)


def test_statemachine::call_constructor_args():
    sig = inspect.signature(statemachine::Call.__init__)
    params = list(sig.parameters.keys())
    assert "actionId" in params, "Missing parameter 'actionId'"

def test_statemachine::call_has_actionId():
    assert hasattr(statemachine::Call, "actionId")
    descriptor = None
    for klass in statemachine::Call.__mro__:
        if "actionId" in klass.__dict__:
            descriptor = klass.__dict__["actionId"]
            break
    assert isinstance(descriptor, property)



def test_gabstractaction_is_not_abstract():
    assert not inspect.isabstract(GAbstractAction)


def test_gabstractaction_constructor_exists():
    assert callable(GAbstractAction.__init__)


def test_gabstractaction_constructor_args():
    sig = inspect.signature(GAbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::callaction_is_not_abstract():
    assert not inspect.isabstract(statemachine::CallAction)


def test_statemachine::callaction_constructor_exists():
    assert callable(statemachine::CallAction.__init__)


def test_statemachine::callaction_constructor_args():
    sig = inspect.signature(statemachine::CallAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::parameter_is_not_abstract():
    assert not inspect.isabstract(statemachine::Parameter)


def test_statemachine::parameter_constructor_exists():
    assert callable(statemachine::Parameter.__init__)


def test_statemachine::parameter_constructor_args():
    sig = inspect.signature(statemachine::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_gcompositestate_is_not_abstract():
    assert not inspect.isabstract(GCompositeState)


def test_gcompositestate_constructor_exists():
    assert callable(GCompositeState.__init__)


def test_gcompositestate_constructor_args():
    sig = inspect.signature(GCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::gstatemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::GStatemachine)


def test_statemachine::gstatemachine_constructor_exists():
    assert callable(statemachine::GStatemachine.__init__)


def test_statemachine::gstatemachine_constructor_args():
    sig = inspect.signature(statemachine::GStatemachine.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_statemachine::gstatemachine_has_package():
    assert hasattr(statemachine::GStatemachine, "package")
    descriptor = None
    for klass in statemachine::GStatemachine.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::gstopstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::GStopState)


def test_statemachine::gstopstate_constructor_exists():
    assert callable(statemachine::GStopState.__init__)


def test_statemachine::gstopstate_constructor_args():
    sig = inspect.signature(statemachine::GStopState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::named_is_not_abstract():
    assert not inspect.isabstract(statemachine::Named)


def test_statemachine::named_constructor_exists():
    assert callable(statemachine::Named.__init__)


def test_statemachine::named_constructor_args():
    sig = inspect.signature(statemachine::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_statemachine::named_has_name():
    assert hasattr(statemachine::Named, "name")
    descriptor = None
    for klass in statemachine::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::named_has_comment():
    assert hasattr(statemachine::Named, "comment")
    descriptor = None
    for klass in statemachine::Named.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_actionkind_exists():
    # Check that the Enumeration exists
    assert ActionKind is not None

def test_actionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionKind]
    expected_literals = [
        "EXIT",
        "ENTRY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionKind"


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
NumberValue_strategy = st.builds(
    NumberValue,
)
statemachine::LongValue_strategy = st.builds(
    statemachine::LongValue,
)
ConstantValue_strategy = st.builds(
    ConstantValue,
)
statemachine::BooleanValue_strategy = st.builds(
    statemachine::BooleanValue,
)
statemachine::NumberValue_strategy = st.builds(
    statemachine::NumberValue,
)
statemachine::StringValue_strategy = st.builds(
    statemachine::StringValue,
)
GState_strategy = st.builds(
    GState,
)
statemachine::GCompositeState_strategy = st.builds(
    statemachine::GCompositeState,
)
statemachine::Value_strategy = st.builds(
    statemachine::Value,
)
GAbstractState_strategy = st.builds(
    GAbstractState,
)
statemachine::GStartState_strategy = st.builds(
    statemachine::GStartState,
)
Named_strategy = st.builds(
    Named,
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    preserveTimers=
        st.booleans()
)
statemachine::GState_strategy = st.builds(
    statemachine::GState,
)
statemachine::GAbstractAction_strategy = st.builds(
    statemachine::GAbstractAction,
    kind=
        safe_text
)
statemachine::GAbstractState_strategy = st.builds(
    statemachine::GAbstractState,
)
Value_strategy = st.builds(
    Value,
)
statemachine::ConstantValue_strategy = st.builds(
    statemachine::ConstantValue,
    value=
        safe_text
)
statemachine::GetParameter_strategy = st.builds(
    statemachine::GetParameter,
)
statemachine::Call_strategy = st.builds(
    statemachine::Call,
    actionId=
        safe_text
)
GAbstractAction_strategy = st.builds(
    GAbstractAction,
)
statemachine::CallAction_strategy = st.builds(
    statemachine::CallAction,
)
statemachine::Parameter_strategy = st.builds(
    statemachine::Parameter,
)
GCompositeState_strategy = st.builds(
    GCompositeState,
)
statemachine::GStatemachine_strategy = st.builds(
    statemachine::GStatemachine,
    package=
        safe_text
)
statemachine::GStopState_strategy = st.builds(
    statemachine::GStopState,
)
statemachine::Named_strategy = st.builds(
    statemachine::Named,
    name=
        safe_text,
    comment=
        safe_text
)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=statemachine::LongValue_strategy)
@settings(max_examples=50)
def test_statemachine::longvalue_instantiation(instance):
    assert isinstance(instance, statemachine::LongValue)

@given(instance=ConstantValue_strategy)
@settings(max_examples=50)
def test_constantvalue_instantiation(instance):
    assert isinstance(instance, ConstantValue)

@given(instance=statemachine::BooleanValue_strategy)
@settings(max_examples=50)
def test_statemachine::booleanvalue_instantiation(instance):
    assert isinstance(instance, statemachine::BooleanValue)

@given(instance=statemachine::NumberValue_strategy)
@settings(max_examples=50)
def test_statemachine::numbervalue_instantiation(instance):
    assert isinstance(instance, statemachine::NumberValue)

@given(instance=statemachine::StringValue_strategy)
@settings(max_examples=50)
def test_statemachine::stringvalue_instantiation(instance):
    assert isinstance(instance, statemachine::StringValue)

@given(instance=GState_strategy)
@settings(max_examples=50)
def test_gstate_instantiation(instance):
    assert isinstance(instance, GState)

@given(instance=statemachine::GCompositeState_strategy)
@settings(max_examples=50)
def test_statemachine::gcompositestate_instantiation(instance):
    assert isinstance(instance, statemachine::GCompositeState)

@given(instance=statemachine::Value_strategy)
@settings(max_examples=50)
def test_statemachine::value_instantiation(instance):
    assert isinstance(instance, statemachine::Value)

@given(instance=GAbstractState_strategy)
@settings(max_examples=50)
def test_gabstractstate_instantiation(instance):
    assert isinstance(instance, GAbstractState)

@given(instance=statemachine::GStartState_strategy)
@settings(max_examples=50)
def test_statemachine::gstartstate_instantiation(instance):
    assert isinstance(instance, statemachine::GStartState)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_preserveTimers_type(instance):
    assert isinstance(instance.preserveTimers, bool)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_preserveTimers_setter(instance):
    original = instance.preserveTimers
    instance.preserveTimers = original
    assert instance.preserveTimers == original

@given(instance=statemachine::GState_strategy)
@settings(max_examples=50)
def test_statemachine::gstate_instantiation(instance):
    assert isinstance(instance, statemachine::GState)

@given(instance=statemachine::GAbstractAction_strategy)
@settings(max_examples=50)
def test_statemachine::gabstractaction_instantiation(instance):
    assert isinstance(instance, statemachine::GAbstractAction)

@given(instance=statemachine::GAbstractAction_strategy)
def test_statemachine::gabstractaction_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=statemachine::GAbstractAction_strategy)
def test_statemachine::gabstractaction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=statemachine::GAbstractState_strategy)
@settings(max_examples=50)
def test_statemachine::gabstractstate_instantiation(instance):
    assert isinstance(instance, statemachine::GAbstractState)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=statemachine::ConstantValue_strategy)
@settings(max_examples=50)
def test_statemachine::constantvalue_instantiation(instance):
    assert isinstance(instance, statemachine::ConstantValue)

@given(instance=statemachine::ConstantValue_strategy)
def test_statemachine::constantvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=statemachine::ConstantValue_strategy)
def test_statemachine::constantvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachine::GetParameter_strategy)
@settings(max_examples=50)
def test_statemachine::getparameter_instantiation(instance):
    assert isinstance(instance, statemachine::GetParameter)

@given(instance=statemachine::Call_strategy)
@settings(max_examples=50)
def test_statemachine::call_instantiation(instance):
    assert isinstance(instance, statemachine::Call)

@given(instance=statemachine::Call_strategy)
def test_statemachine::call_actionId_type(instance):
    assert isinstance(instance.actionId, str)


@given(instance=statemachine::Call_strategy)
def test_statemachine::call_actionId_setter(instance):
    original = instance.actionId
    instance.actionId = original
    assert instance.actionId == original

@given(instance=GAbstractAction_strategy)
@settings(max_examples=50)
def test_gabstractaction_instantiation(instance):
    assert isinstance(instance, GAbstractAction)

@given(instance=statemachine::CallAction_strategy)
@settings(max_examples=50)
def test_statemachine::callaction_instantiation(instance):
    assert isinstance(instance, statemachine::CallAction)

@given(instance=statemachine::Parameter_strategy)
@settings(max_examples=50)
def test_statemachine::parameter_instantiation(instance):
    assert isinstance(instance, statemachine::Parameter)

@given(instance=GCompositeState_strategy)
@settings(max_examples=50)
def test_gcompositestate_instantiation(instance):
    assert isinstance(instance, GCompositeState)

@given(instance=statemachine::GStatemachine_strategy)
@settings(max_examples=50)
def test_statemachine::gstatemachine_instantiation(instance):
    assert isinstance(instance, statemachine::GStatemachine)

@given(instance=statemachine::GStatemachine_strategy)
def test_statemachine::gstatemachine_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=statemachine::GStatemachine_strategy)
def test_statemachine::gstatemachine_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=statemachine::GStopState_strategy)
@settings(max_examples=50)
def test_statemachine::gstopstate_instantiation(instance):
    assert isinstance(instance, statemachine::GStopState)

@given(instance=statemachine::Named_strategy)
@settings(max_examples=50)
def test_statemachine::named_instantiation(instance):
    assert isinstance(instance, statemachine::Named)

@given(instance=statemachine::Named_strategy)
def test_statemachine::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Named_strategy)
def test_statemachine::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Named_strategy)
def test_statemachine::named_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=statemachine::Named_strategy)
def test_statemachine::named_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original
