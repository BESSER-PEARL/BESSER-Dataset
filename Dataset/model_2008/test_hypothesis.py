import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    trace_LiteralValue,
    trace_RefValue,
    trace_ParameterValue,
    trace_Value,
    trace_TracedObject,
    trace_ObjectState,
    trace_ModelState,
    trace_Step,
    trace_Trace,
    Step,
    trace_BigStep,
    trace_SmallStep,
    ParamterKindEnum,
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



def test_trace_literalvalue_is_not_abstract():
    assert not inspect.isabstract(trace_LiteralValue)


def test_trace_literalvalue_constructor_exists():
    assert callable(trace_LiteralValue.__init__)


def test_trace_literalvalue_constructor_args():
    sig = inspect.signature(trace_LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_trace_refvalue_is_not_abstract():
    assert not inspect.isabstract(trace_RefValue)


def test_trace_refvalue_constructor_exists():
    assert callable(trace_RefValue.__init__)


def test_trace_refvalue_constructor_args():
    sig = inspect.signature(trace_RefValue.__init__)
    params = list(sig.parameters.keys())



def test_trace_parametervalue_is_not_abstract():
    assert not inspect.isabstract(trace_ParameterValue)


def test_trace_parametervalue_constructor_exists():
    assert callable(trace_ParameterValue.__init__)


def test_trace_parametervalue_constructor_args():
    sig = inspect.signature(trace_ParameterValue.__init__)
    params = list(sig.parameters.keys())
    assert "DirectionKind" in params, "Missing parameter 'DirectionKind'"

def test_trace_parametervalue_has_DirectionKind():
    assert hasattr(trace_ParameterValue, "DirectionKind")
    descriptor = None
    for klass in trace_ParameterValue.__mro__:
        if "DirectionKind" in klass.__dict__:
            descriptor = klass.__dict__["DirectionKind"]
            break
    assert isinstance(descriptor, property)



def test_trace_value_is_not_abstract():
    assert not inspect.isabstract(trace_Value)


def test_trace_value_constructor_exists():
    assert callable(trace_Value.__init__)


def test_trace_value_constructor_args():
    sig = inspect.signature(trace_Value.__init__)
    params = list(sig.parameters.keys())



def test_trace_tracedobject_is_not_abstract():
    assert not inspect.isabstract(trace_TracedObject)


def test_trace_tracedobject_constructor_exists():
    assert callable(trace_TracedObject.__init__)


def test_trace_tracedobject_constructor_args():
    sig = inspect.signature(trace_TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_trace_objectstate_is_not_abstract():
    assert not inspect.isabstract(trace_ObjectState)


def test_trace_objectstate_constructor_exists():
    assert callable(trace_ObjectState.__init__)


def test_trace_objectstate_constructor_args():
    sig = inspect.signature(trace_ObjectState.__init__)
    params = list(sig.parameters.keys())



def test_trace_modelstate_is_not_abstract():
    assert not inspect.isabstract(trace_ModelState)


def test_trace_modelstate_constructor_exists():
    assert callable(trace_ModelState.__init__)


def test_trace_modelstate_constructor_args():
    sig = inspect.signature(trace_ModelState.__init__)
    params = list(sig.parameters.keys())



def test_trace_step_is_not_abstract():
    assert not inspect.isabstract(trace_Step)


def test_trace_step_constructor_exists():
    assert callable(trace_Step.__init__)


def test_trace_step_constructor_args():
    sig = inspect.signature(trace_Step.__init__)
    params = list(sig.parameters.keys())



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_trace_bigstep_is_not_abstract():
    assert not inspect.isabstract(trace_BigStep)


def test_trace_bigstep_constructor_exists():
    assert callable(trace_BigStep.__init__)


def test_trace_bigstep_constructor_args():
    sig = inspect.signature(trace_BigStep.__init__)
    params = list(sig.parameters.keys())



def test_trace_smallstep_is_not_abstract():
    assert not inspect.isabstract(trace_SmallStep)


def test_trace_smallstep_constructor_exists():
    assert callable(trace_SmallStep.__init__)


def test_trace_smallstep_constructor_args():
    sig = inspect.signature(trace_SmallStep.__init__)
    params = list(sig.parameters.keys())

def test_paramterkindenum_exists():
    # Check that the Enumeration exists
    assert ParamterKindEnum is not None

def test_paramterkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParamterKindEnum]
    expected_literals = [
        "RETURN",
        "OUT",
        "INOUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParamterKindEnum"


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
trace_LiteralValue_strategy = st.builds(
    trace_LiteralValue,
)
trace_RefValue_strategy = st.builds(
    trace_RefValue,
)
trace_ParameterValue_strategy = st.builds(
    trace_ParameterValue,
    DirectionKind=
        safe_text
)
trace_Value_strategy = st.builds(
    trace_Value,
)
trace_TracedObject_strategy = st.builds(
    trace_TracedObject,
)
trace_ObjectState_strategy = st.builds(
    trace_ObjectState,
)
trace_ModelState_strategy = st.builds(
    trace_ModelState,
)
trace_Step_strategy = st.builds(
    trace_Step,
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)
Step_strategy = st.builds(
    Step,
)
trace_BigStep_strategy = st.builds(
    trace_BigStep,
)
trace_SmallStep_strategy = st.builds(
    trace_SmallStep,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=trace_LiteralValue_strategy)
@settings(max_examples=50)
def test_trace_literalvalue_instantiation(instance):
    assert isinstance(instance, trace_LiteralValue)

@given(instance=trace_RefValue_strategy)
@settings(max_examples=50)
def test_trace_refvalue_instantiation(instance):
    assert isinstance(instance, trace_RefValue)

@given(instance=trace_ParameterValue_strategy)
@settings(max_examples=50)
def test_trace_parametervalue_instantiation(instance):
    assert isinstance(instance, trace_ParameterValue)



@given(instance=trace_ParameterValue_strategy)
def test_trace_parametervalue_DirectionKind_setter(instance):
    original = instance.DirectionKind
    instance.DirectionKind = original
    assert instance.DirectionKind == original

@given(instance=trace_Value_strategy)
@settings(max_examples=50)
def test_trace_value_instantiation(instance):
    assert isinstance(instance, trace_Value)

@given(instance=trace_TracedObject_strategy)
@settings(max_examples=50)
def test_trace_tracedobject_instantiation(instance):
    assert isinstance(instance, trace_TracedObject)

@given(instance=trace_ObjectState_strategy)
@settings(max_examples=50)
def test_trace_objectstate_instantiation(instance):
    assert isinstance(instance, trace_ObjectState)

@given(instance=trace_ModelState_strategy)
@settings(max_examples=50)
def test_trace_modelstate_instantiation(instance):
    assert isinstance(instance, trace_ModelState)

@given(instance=trace_Step_strategy)
@settings(max_examples=50)
def test_trace_step_instantiation(instance):
    assert isinstance(instance, trace_Step)

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=trace_BigStep_strategy)
@settings(max_examples=50)
def test_trace_bigstep_instantiation(instance):
    assert isinstance(instance, trace_BigStep)

@given(instance=trace_SmallStep_strategy)
@settings(max_examples=50)
def test_trace_smallstep_instantiation(instance):
    assert isinstance(instance, trace_SmallStep)
