import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    statemachine_ConstantValue,
    statemachine_GetParameter,
    NumberValue,
    statemachine_LongValue,
    ConstantValue,
    statemachine_NumberValue,
    statemachine_BooleanValue,
    statemachine_StringValue,
    GCompositeState,
    statemachine_GStatemachine,
    statemachine_Call,
    GAbstractAction,
    statemachine_CallAction,
    statemachine_Value,
    GAbstractState,
    statemachine_GStartState,
    statemachine_GStopState,
    Named,
    statemachine_Parameter,
    statemachine_Transition,
    statemachine_GState,
    GState,
    statemachine_GCompositeState,
    statemachine_Named,
    statemachine_GAbstractAction,
    statemachine_GAbstractState,
    ActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_constantvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine_ConstantValue)


def test_statemachine_constantvalue_constructor_exists():
    assert callable(statemachine_ConstantValue.__init__)


def test_statemachine_constantvalue_constructor_args():
    sig = inspect.signature(statemachine_ConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine_constantvalue_has_value():
    assert hasattr(statemachine_ConstantValue, "value")
    descriptor = None
    for klass in statemachine_ConstantValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_getparameter_is_not_abstract():
    assert not inspect.isabstract(statemachine_GetParameter)


def test_statemachine_getparameter_constructor_exists():
    assert callable(statemachine_GetParameter.__init__)


def test_statemachine_getparameter_constructor_args():
    sig = inspect.signature(statemachine_GetParameter.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_longvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine_LongValue)


def test_statemachine_longvalue_constructor_exists():
    assert callable(statemachine_LongValue.__init__)


def test_statemachine_longvalue_constructor_args():
    sig = inspect.signature(statemachine_LongValue.__init__)
    params = list(sig.parameters.keys())



def test_constantvalue_is_not_abstract():
    assert not inspect.isabstract(ConstantValue)


def test_constantvalue_constructor_exists():
    assert callable(ConstantValue.__init__)


def test_constantvalue_constructor_args():
    sig = inspect.signature(ConstantValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_numbervalue_is_not_abstract():
    assert not inspect.isabstract(statemachine_NumberValue)


def test_statemachine_numbervalue_constructor_exists():
    assert callable(statemachine_NumberValue.__init__)


def test_statemachine_numbervalue_constructor_args():
    sig = inspect.signature(statemachine_NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine_BooleanValue)


def test_statemachine_booleanvalue_constructor_exists():
    assert callable(statemachine_BooleanValue.__init__)


def test_statemachine_booleanvalue_constructor_args():
    sig = inspect.signature(statemachine_BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_stringvalue_is_not_abstract():
    assert not inspect.isabstract(statemachine_StringValue)


def test_statemachine_stringvalue_constructor_exists():
    assert callable(statemachine_StringValue.__init__)


def test_statemachine_stringvalue_constructor_args():
    sig = inspect.signature(statemachine_StringValue.__init__)
    params = list(sig.parameters.keys())



def test_gcompositestate_is_not_abstract():
    assert not inspect.isabstract(GCompositeState)


def test_gcompositestate_constructor_exists():
    assert callable(GCompositeState.__init__)


def test_gcompositestate_constructor_args():
    sig = inspect.signature(GCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_gstatemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_GStatemachine)


def test_statemachine_gstatemachine_constructor_exists():
    assert callable(statemachine_GStatemachine.__init__)


def test_statemachine_gstatemachine_constructor_args():
    sig = inspect.signature(statemachine_GStatemachine.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_statemachine_gstatemachine_has_package():
    assert hasattr(statemachine_GStatemachine, "package")
    descriptor = None
    for klass in statemachine_GStatemachine.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_call_is_not_abstract():
    assert not inspect.isabstract(statemachine_Call)


def test_statemachine_call_constructor_exists():
    assert callable(statemachine_Call.__init__)


def test_statemachine_call_constructor_args():
    sig = inspect.signature(statemachine_Call.__init__)
    params = list(sig.parameters.keys())
    assert "actionId" in params, "Missing parameter 'actionId'"

def test_statemachine_call_has_actionId():
    assert hasattr(statemachine_Call, "actionId")
    descriptor = None
    for klass in statemachine_Call.__mro__:
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



def test_statemachine_callaction_is_not_abstract():
    assert not inspect.isabstract(statemachine_CallAction)


def test_statemachine_callaction_constructor_exists():
    assert callable(statemachine_CallAction.__init__)


def test_statemachine_callaction_constructor_args():
    sig = inspect.signature(statemachine_CallAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_value_is_not_abstract():
    assert not inspect.isabstract(statemachine_Value)


def test_statemachine_value_constructor_exists():
    assert callable(statemachine_Value.__init__)


def test_statemachine_value_constructor_args():
    sig = inspect.signature(statemachine_Value.__init__)
    params = list(sig.parameters.keys())



def test_gabstractstate_is_not_abstract():
    assert not inspect.isabstract(GAbstractState)


def test_gabstractstate_constructor_exists():
    assert callable(GAbstractState.__init__)


def test_gabstractstate_constructor_args():
    sig = inspect.signature(GAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_gstartstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_GStartState)


def test_statemachine_gstartstate_constructor_exists():
    assert callable(statemachine_GStartState.__init__)


def test_statemachine_gstartstate_constructor_args():
    sig = inspect.signature(statemachine_GStartState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_gstopstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_GStopState)


def test_statemachine_gstopstate_constructor_exists():
    assert callable(statemachine_GStopState.__init__)


def test_statemachine_gstopstate_constructor_args():
    sig = inspect.signature(statemachine_GStopState.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_parameter_is_not_abstract():
    assert not inspect.isabstract(statemachine_Parameter)


def test_statemachine_parameter_constructor_exists():
    assert callable(statemachine_Parameter.__init__)


def test_statemachine_parameter_constructor_args():
    sig = inspect.signature(statemachine_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "preserveTimers" in params, "Missing parameter 'preserveTimers'"

def test_statemachine_transition_has_preserveTimers():
    assert hasattr(statemachine_Transition, "preserveTimers")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "preserveTimers" in klass.__dict__:
            descriptor = klass.__dict__["preserveTimers"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_gstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_GState)


def test_statemachine_gstate_constructor_exists():
    assert callable(statemachine_GState.__init__)


def test_statemachine_gstate_constructor_args():
    sig = inspect.signature(statemachine_GState.__init__)
    params = list(sig.parameters.keys())



def test_gstate_is_not_abstract():
    assert not inspect.isabstract(GState)


def test_gstate_constructor_exists():
    assert callable(GState.__init__)


def test_gstate_constructor_args():
    sig = inspect.signature(GState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_gcompositestate_is_not_abstract():
    assert not inspect.isabstract(statemachine_GCompositeState)


def test_statemachine_gcompositestate_constructor_exists():
    assert callable(statemachine_GCompositeState.__init__)


def test_statemachine_gcompositestate_constructor_args():
    sig = inspect.signature(statemachine_GCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_named_is_not_abstract():
    assert not inspect.isabstract(statemachine_Named)


def test_statemachine_named_constructor_exists():
    assert callable(statemachine_Named.__init__)


def test_statemachine_named_constructor_args():
    sig = inspect.signature(statemachine_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_statemachine_named_has_name():
    assert hasattr(statemachine_Named, "name")
    descriptor = None
    for klass in statemachine_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_named_has_comment():
    assert hasattr(statemachine_Named, "comment")
    descriptor = None
    for klass in statemachine_Named.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_gabstractaction_is_not_abstract():
    assert not inspect.isabstract(statemachine_GAbstractAction)


def test_statemachine_gabstractaction_constructor_exists():
    assert callable(statemachine_GAbstractAction.__init__)


def test_statemachine_gabstractaction_constructor_args():
    sig = inspect.signature(statemachine_GAbstractAction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine_gabstractaction_has_kind():
    assert hasattr(statemachine_GAbstractAction, "kind")
    descriptor = None
    for klass in statemachine_GAbstractAction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_gabstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_GAbstractState)


def test_statemachine_gabstractstate_constructor_exists():
    assert callable(statemachine_GAbstractState.__init__)


def test_statemachine_gabstractstate_constructor_args():
    sig = inspect.signature(statemachine_GAbstractState.__init__)
    params = list(sig.parameters.keys())

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
Value_strategy = st.builds(
    Value,
)
statemachine_ConstantValue_strategy = st.builds(
    statemachine_ConstantValue,
    value=
        safe_text
)
statemachine_GetParameter_strategy = st.builds(
    statemachine_GetParameter,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
statemachine_LongValue_strategy = st.builds(
    statemachine_LongValue,
)
ConstantValue_strategy = st.builds(
    ConstantValue,
)
statemachine_NumberValue_strategy = st.builds(
    statemachine_NumberValue,
)
statemachine_BooleanValue_strategy = st.builds(
    statemachine_BooleanValue,
)
statemachine_StringValue_strategy = st.builds(
    statemachine_StringValue,
)
GCompositeState_strategy = st.builds(
    GCompositeState,
)
statemachine_GStatemachine_strategy = st.builds(
    statemachine_GStatemachine,
    package=
        safe_text
)
statemachine_Call_strategy = st.builds(
    statemachine_Call,
    actionId=
        safe_text
)
GAbstractAction_strategy = st.builds(
    GAbstractAction,
)
statemachine_CallAction_strategy = st.builds(
    statemachine_CallAction,
)
statemachine_Value_strategy = st.builds(
    statemachine_Value,
)
GAbstractState_strategy = st.builds(
    GAbstractState,
)
statemachine_GStartState_strategy = st.builds(
    statemachine_GStartState,
)
statemachine_GStopState_strategy = st.builds(
    statemachine_GStopState,
)
Named_strategy = st.builds(
    Named,
)
statemachine_Parameter_strategy = st.builds(
    statemachine_Parameter,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    preserveTimers=
        st.booleans()
)
statemachine_GState_strategy = st.builds(
    statemachine_GState,
)
GState_strategy = st.builds(
    GState,
)
statemachine_GCompositeState_strategy = st.builds(
    statemachine_GCompositeState,
)
statemachine_Named_strategy = st.builds(
    statemachine_Named,
    name=
        safe_text,
    comment=
        safe_text
)
statemachine_GAbstractAction_strategy = st.builds(
    statemachine_GAbstractAction,
    kind=
        safe_text
)
statemachine_GAbstractState_strategy = st.builds(
    statemachine_GAbstractState,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=statemachine_ConstantValue_strategy)
@settings(max_examples=50)
def test_statemachine_constantvalue_instantiation(instance):
    assert isinstance(instance, statemachine_ConstantValue)



@given(instance=statemachine_ConstantValue_strategy)
def test_statemachine_constantvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachine_GetParameter_strategy)
@settings(max_examples=50)
def test_statemachine_getparameter_instantiation(instance):
    assert isinstance(instance, statemachine_GetParameter)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=statemachine_LongValue_strategy)
@settings(max_examples=50)
def test_statemachine_longvalue_instantiation(instance):
    assert isinstance(instance, statemachine_LongValue)

@given(instance=ConstantValue_strategy)
@settings(max_examples=50)
def test_constantvalue_instantiation(instance):
    assert isinstance(instance, ConstantValue)

@given(instance=statemachine_NumberValue_strategy)
@settings(max_examples=50)
def test_statemachine_numbervalue_instantiation(instance):
    assert isinstance(instance, statemachine_NumberValue)

@given(instance=statemachine_BooleanValue_strategy)
@settings(max_examples=50)
def test_statemachine_booleanvalue_instantiation(instance):
    assert isinstance(instance, statemachine_BooleanValue)

@given(instance=statemachine_StringValue_strategy)
@settings(max_examples=50)
def test_statemachine_stringvalue_instantiation(instance):
    assert isinstance(instance, statemachine_StringValue)

@given(instance=GCompositeState_strategy)
@settings(max_examples=50)
def test_gcompositestate_instantiation(instance):
    assert isinstance(instance, GCompositeState)

@given(instance=statemachine_GStatemachine_strategy)
@settings(max_examples=50)
def test_statemachine_gstatemachine_instantiation(instance):
    assert isinstance(instance, statemachine_GStatemachine)



@given(instance=statemachine_GStatemachine_strategy)
def test_statemachine_gstatemachine_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=statemachine_Call_strategy)
@settings(max_examples=50)
def test_statemachine_call_instantiation(instance):
    assert isinstance(instance, statemachine_Call)



@given(instance=statemachine_Call_strategy)
def test_statemachine_call_actionId_setter(instance):
    original = instance.actionId
    instance.actionId = original
    assert instance.actionId == original

@given(instance=GAbstractAction_strategy)
@settings(max_examples=50)
def test_gabstractaction_instantiation(instance):
    assert isinstance(instance, GAbstractAction)

@given(instance=statemachine_CallAction_strategy)
@settings(max_examples=50)
def test_statemachine_callaction_instantiation(instance):
    assert isinstance(instance, statemachine_CallAction)

@given(instance=statemachine_Value_strategy)
@settings(max_examples=50)
def test_statemachine_value_instantiation(instance):
    assert isinstance(instance, statemachine_Value)

@given(instance=GAbstractState_strategy)
@settings(max_examples=50)
def test_gabstractstate_instantiation(instance):
    assert isinstance(instance, GAbstractState)

@given(instance=statemachine_GStartState_strategy)
@settings(max_examples=50)
def test_statemachine_gstartstate_instantiation(instance):
    assert isinstance(instance, statemachine_GStartState)

@given(instance=statemachine_GStopState_strategy)
@settings(max_examples=50)
def test_statemachine_gstopstate_instantiation(instance):
    assert isinstance(instance, statemachine_GStopState)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=statemachine_Parameter_strategy)
@settings(max_examples=50)
def test_statemachine_parameter_instantiation(instance):
    assert isinstance(instance, statemachine_Parameter)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_preserveTimers_setter(instance):
    original = instance.preserveTimers
    instance.preserveTimers = original
    assert instance.preserveTimers == original

@given(instance=statemachine_GState_strategy)
@settings(max_examples=50)
def test_statemachine_gstate_instantiation(instance):
    assert isinstance(instance, statemachine_GState)

@given(instance=GState_strategy)
@settings(max_examples=50)
def test_gstate_instantiation(instance):
    assert isinstance(instance, GState)

@given(instance=statemachine_GCompositeState_strategy)
@settings(max_examples=50)
def test_statemachine_gcompositestate_instantiation(instance):
    assert isinstance(instance, statemachine_GCompositeState)

@given(instance=statemachine_Named_strategy)
@settings(max_examples=50)
def test_statemachine_named_instantiation(instance):
    assert isinstance(instance, statemachine_Named)



@given(instance=statemachine_Named_strategy)
def test_statemachine_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachine_Named_strategy)
def test_statemachine_named_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=statemachine_GAbstractAction_strategy)
@settings(max_examples=50)
def test_statemachine_gabstractaction_instantiation(instance):
    assert isinstance(instance, statemachine_GAbstractAction)



@given(instance=statemachine_GAbstractAction_strategy)
def test_statemachine_gabstractaction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=statemachine_GAbstractState_strategy)
@settings(max_examples=50)
def test_statemachine_gabstractstate_instantiation(instance):
    assert isinstance(instance, statemachine_GAbstractState)
