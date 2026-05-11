import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Trace::Index,
    Index,
    Trace::Call,
    Call,
    Level,
    Trace::Trace,
    Trace,
    Trace::Level,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::index_is_not_abstract():
    assert not inspect.isabstract(Trace::Index)


def test_trace::index_constructor_exists():
    assert callable(Trace::Index.__init__)


def test_trace::index_constructor_args():
    sig = inspect.signature(Trace::Index.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_trace::index_has_value():
    assert hasattr(Trace::Index, "value")
    descriptor = None
    for klass in Trace::Index.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_trace::call_is_not_abstract():
    assert not inspect.isabstract(Trace::Call)


def test_trace::call_constructor_exists():
    assert callable(Trace::Call.__init__)


def test_trace::call_constructor_args():
    sig = inspect.signature(Trace::Call.__init__)
    params = list(sig.parameters.keys())
    assert "CPUTime" in params, "Missing parameter 'CPUTime'"
    assert "DBRowsNumber" in params, "Missing parameter 'DBRowsNumber'"
    assert "DBAccessesNumber" in params, "Missing parameter 'DBAccessesNumber'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_trace::call_has_CPUTime():
    assert hasattr(Trace::Call, "CPUTime")
    descriptor = None
    for klass in Trace::Call.__mro__:
        if "CPUTime" in klass.__dict__:
            descriptor = klass.__dict__["CPUTime"]
            break
    assert isinstance(descriptor, property)

def test_trace::call_has_DBRowsNumber():
    assert hasattr(Trace::Call, "DBRowsNumber")
    descriptor = None
    for klass in Trace::Call.__mro__:
        if "DBRowsNumber" in klass.__dict__:
            descriptor = klass.__dict__["DBRowsNumber"]
            break
    assert isinstance(descriptor, property)

def test_trace::call_has_DBAccessesNumber():
    assert hasattr(Trace::Call, "DBAccessesNumber")
    descriptor = None
    for klass in Trace::Call.__mro__:
        if "DBAccessesNumber" in klass.__dict__:
            descriptor = klass.__dict__["DBAccessesNumber"]
            break
    assert isinstance(descriptor, property)

def test_trace::call_has_methodName():
    assert hasattr(Trace::Call, "methodName")
    descriptor = None
    for klass in Trace::Call.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_call_is_not_abstract():
    assert not inspect.isabstract(Call)


def test_call_constructor_exists():
    assert callable(Call.__init__)


def test_call_constructor_args():
    sig = inspect.signature(Call.__init__)
    params = list(sig.parameters.keys())



def test_level_is_not_abstract():
    assert not inspect.isabstract(Level)


def test_level_constructor_exists():
    assert callable(Level.__init__)


def test_level_constructor_args():
    sig = inspect.signature(Level.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(Trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(Trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(Trace::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trace::trace_has_name():
    assert hasattr(Trace::Trace, "name")
    descriptor = None
    for klass in Trace::Trace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trace_is_not_abstract():
    assert not inspect.isabstract(Trace)


def test_trace_constructor_exists():
    assert callable(Trace.__init__)


def test_trace_constructor_args():
    sig = inspect.signature(Trace.__init__)
    params = list(sig.parameters.keys())



def test_trace::level_is_not_abstract():
    assert not inspect.isabstract(Trace::Level)


def test_trace::level_constructor_exists():
    assert callable(Trace::Level.__init__)


def test_trace::level_constructor_args():
    sig = inspect.signature(Trace::Level.__init__)
    params = list(sig.parameters.keys())


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
Trace::Index_strategy = st.builds(
    Trace::Index,
    value=
        safe_text
)
Index_strategy = st.builds(
    Index,
)
Trace::Call_strategy = st.builds(
    Trace::Call,
    CPUTime=
        safe_text,
    DBRowsNumber=
        safe_text,
    DBAccessesNumber=
        safe_text,
    methodName=
        safe_text
)
Call_strategy = st.builds(
    Call,
)
Level_strategy = st.builds(
    Level,
)
Trace::Trace_strategy = st.builds(
    Trace::Trace,
    name=
        safe_text
)
Trace_strategy = st.builds(
    Trace,
)
Trace::Level_strategy = st.builds(
    Trace::Level,
)

@given(instance=Trace::Index_strategy)
@settings(max_examples=50)
def test_trace::index_instantiation(instance):
    assert isinstance(instance, Trace::Index)

@given(instance=Trace::Index_strategy)
def test_trace::index_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Trace::Index_strategy)
def test_trace::index_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=Trace::Call_strategy)
@settings(max_examples=50)
def test_trace::call_instantiation(instance):
    assert isinstance(instance, Trace::Call)

@given(instance=Trace::Call_strategy)
def test_trace::call_CPUTime_type(instance):
    assert isinstance(instance.CPUTime, str)


@given(instance=Trace::Call_strategy)
def test_trace::call_CPUTime_setter(instance):
    original = instance.CPUTime
    instance.CPUTime = original
    assert instance.CPUTime == original

@given(instance=Trace::Call_strategy)
def test_trace::call_DBRowsNumber_type(instance):
    assert isinstance(instance.DBRowsNumber, str)


@given(instance=Trace::Call_strategy)
def test_trace::call_DBRowsNumber_setter(instance):
    original = instance.DBRowsNumber
    instance.DBRowsNumber = original
    assert instance.DBRowsNumber == original

@given(instance=Trace::Call_strategy)
def test_trace::call_DBAccessesNumber_type(instance):
    assert isinstance(instance.DBAccessesNumber, str)


@given(instance=Trace::Call_strategy)
def test_trace::call_DBAccessesNumber_setter(instance):
    original = instance.DBAccessesNumber
    instance.DBAccessesNumber = original
    assert instance.DBAccessesNumber == original

@given(instance=Trace::Call_strategy)
def test_trace::call_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=Trace::Call_strategy)
def test_trace::call_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_call_instantiation(instance):
    assert isinstance(instance, Call)

@given(instance=Level_strategy)
@settings(max_examples=50)
def test_level_instantiation(instance):
    assert isinstance(instance, Level)

@given(instance=Trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, Trace::Trace)

@given(instance=Trace::Trace_strategy)
def test_trace::trace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Trace::Trace_strategy)
def test_trace::trace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Trace_strategy)
@settings(max_examples=50)
def test_trace_instantiation(instance):
    assert isinstance(instance, Trace)

@given(instance=Trace::Level_strategy)
@settings(max_examples=50)
def test_trace::level_instantiation(instance):
    assert isinstance(instance, Trace::Level)
