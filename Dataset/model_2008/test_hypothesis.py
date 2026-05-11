import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Value,
    trace::LiteralValue,
    trace::RefValue,
    trace::ParameterValue,
    trace::Value,
    trace::TracedObject,
    trace::ObjectState,
    trace::ModelState,
    trace::Step,
    trace::Trace,
    Step,
    trace::SmallStep,
    trace::BigStep,
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



def test_trace::literalvalue_is_not_abstract():
    assert not inspect.isabstract(trace::LiteralValue)


def test_trace::literalvalue_constructor_exists():
    assert callable(trace::LiteralValue.__init__)


def test_trace::literalvalue_constructor_args():
    sig = inspect.signature(trace::LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_trace::refvalue_is_not_abstract():
    assert not inspect.isabstract(trace::RefValue)


def test_trace::refvalue_constructor_exists():
    assert callable(trace::RefValue.__init__)


def test_trace::refvalue_constructor_args():
    sig = inspect.signature(trace::RefValue.__init__)
    params = list(sig.parameters.keys())



def test_trace::parametervalue_is_not_abstract():
    assert not inspect.isabstract(trace::ParameterValue)


def test_trace::parametervalue_constructor_exists():
    assert callable(trace::ParameterValue.__init__)


def test_trace::parametervalue_constructor_args():
    sig = inspect.signature(trace::ParameterValue.__init__)
    params = list(sig.parameters.keys())
    assert "DirectionKind" in params, "Missing parameter 'DirectionKind'"

def test_trace::parametervalue_has_DirectionKind():
    assert hasattr(trace::ParameterValue, "DirectionKind")
    descriptor = None
    for klass in trace::ParameterValue.__mro__:
        if "DirectionKind" in klass.__dict__:
            descriptor = klass.__dict__["DirectionKind"]
            break
    assert isinstance(descriptor, property)



def test_trace::value_is_not_abstract():
    assert not inspect.isabstract(trace::Value)


def test_trace::value_constructor_exists():
    assert callable(trace::Value.__init__)


def test_trace::value_constructor_args():
    sig = inspect.signature(trace::Value.__init__)
    params = list(sig.parameters.keys())



def test_trace::tracedobject_is_not_abstract():
    assert not inspect.isabstract(trace::TracedObject)


def test_trace::tracedobject_constructor_exists():
    assert callable(trace::TracedObject.__init__)


def test_trace::tracedobject_constructor_args():
    sig = inspect.signature(trace::TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_trace::objectstate_is_not_abstract():
    assert not inspect.isabstract(trace::ObjectState)


def test_trace::objectstate_constructor_exists():
    assert callable(trace::ObjectState.__init__)


def test_trace::objectstate_constructor_args():
    sig = inspect.signature(trace::ObjectState.__init__)
    params = list(sig.parameters.keys())



def test_trace::modelstate_is_not_abstract():
    assert not inspect.isabstract(trace::ModelState)


def test_trace::modelstate_constructor_exists():
    assert callable(trace::ModelState.__init__)


def test_trace::modelstate_constructor_args():
    sig = inspect.signature(trace::ModelState.__init__)
    params = list(sig.parameters.keys())



def test_trace::step_is_not_abstract():
    assert not inspect.isabstract(trace::Step)


def test_trace::step_constructor_exists():
    assert callable(trace::Step.__init__)


def test_trace::step_constructor_args():
    sig = inspect.signature(trace::Step.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_trace::smallstep_is_not_abstract():
    assert not inspect.isabstract(trace::SmallStep)


def test_trace::smallstep_constructor_exists():
    assert callable(trace::SmallStep.__init__)


def test_trace::smallstep_constructor_args():
    sig = inspect.signature(trace::SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_trace::bigstep_is_not_abstract():
    assert not inspect.isabstract(trace::BigStep)


def test_trace::bigstep_constructor_exists():
    assert callable(trace::BigStep.__init__)


def test_trace::bigstep_constructor_args():
    sig = inspect.signature(trace::BigStep.__init__)
    params = list(sig.parameters.keys())

def test_paramterkindenum_exists():
    # Check that the Enumeration exists
    assert ParamterKindEnum is not None

def test_paramterkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParamterKindEnum]
    expected_literals = [
        "RETURN",
        "IN",
        "INOUT",
        "OUT",
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
trace::LiteralValue_strategy = st.builds(
    trace::LiteralValue,
)
trace::RefValue_strategy = st.builds(
    trace::RefValue,
)
trace::ParameterValue_strategy = st.builds(
    trace::ParameterValue,
    DirectionKind=
        safe_text
)
trace::Value_strategy = st.builds(
    trace::Value,
)
trace::TracedObject_strategy = st.builds(
    trace::TracedObject,
)
trace::ObjectState_strategy = st.builds(
    trace::ObjectState,
)
trace::ModelState_strategy = st.builds(
    trace::ModelState,
)
trace::Step_strategy = st.builds(
    trace::Step,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)
Step_strategy = st.builds(
    Step,
)
trace::SmallStep_strategy = st.builds(
    trace::SmallStep,
)
trace::BigStep_strategy = st.builds(
    trace::BigStep,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=trace::LiteralValue_strategy)
@settings(max_examples=50)
def test_trace::literalvalue_instantiation(instance):
    assert isinstance(instance, trace::LiteralValue)

@given(instance=trace::RefValue_strategy)
@settings(max_examples=50)
def test_trace::refvalue_instantiation(instance):
    assert isinstance(instance, trace::RefValue)

@given(instance=trace::ParameterValue_strategy)
@settings(max_examples=50)
def test_trace::parametervalue_instantiation(instance):
    assert isinstance(instance, trace::ParameterValue)

@given(instance=trace::ParameterValue_strategy)
def test_trace::parametervalue_DirectionKind_type(instance):
    assert isinstance(instance.DirectionKind, str)


@given(instance=trace::ParameterValue_strategy)
def test_trace::parametervalue_DirectionKind_setter(instance):
    original = instance.DirectionKind
    instance.DirectionKind = original
    assert instance.DirectionKind == original

@given(instance=trace::Value_strategy)
@settings(max_examples=50)
def test_trace::value_instantiation(instance):
    assert isinstance(instance, trace::Value)

@given(instance=trace::TracedObject_strategy)
@settings(max_examples=50)
def test_trace::tracedobject_instantiation(instance):
    assert isinstance(instance, trace::TracedObject)

@given(instance=trace::ObjectState_strategy)
@settings(max_examples=50)
def test_trace::objectstate_instantiation(instance):
    assert isinstance(instance, trace::ObjectState)

@given(instance=trace::ModelState_strategy)
@settings(max_examples=50)
def test_trace::modelstate_instantiation(instance):
    assert isinstance(instance, trace::ModelState)

@given(instance=trace::Step_strategy)
@settings(max_examples=50)
def test_trace::step_instantiation(instance):
    assert isinstance(instance, trace::Step)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=trace::SmallStep_strategy)
@settings(max_examples=50)
def test_trace::smallstep_instantiation(instance):
    assert isinstance(instance, trace::SmallStep)

@given(instance=trace::BigStep_strategy)
@settings(max_examples=50)
def test_trace::bigstep_instantiation(instance):
    assert isinstance(instance, trace::BigStep)
