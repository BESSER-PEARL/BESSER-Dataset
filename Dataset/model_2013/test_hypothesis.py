import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Trace_Index,
    Index,
    Trace_Call,
    Call,
    Level,
    Trace_Trace,
    Trace,
    Trace_Level,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_index_is_not_abstract():
    assert not inspect.isabstract(Trace_Index)


def test_trace_index_constructor_exists():
    assert callable(Trace_Index.__init__)


def test_trace_index_constructor_args():
    sig = inspect.signature(Trace_Index.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_trace_index_has_value():
    assert hasattr(Trace_Index, "value")
    descriptor = None
    for klass in Trace_Index.__mro__:
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



def test_trace_call_is_not_abstract():
    assert not inspect.isabstract(Trace_Call)


def test_trace_call_constructor_exists():
    assert callable(Trace_Call.__init__)


def test_trace_call_constructor_args():
    sig = inspect.signature(Trace_Call.__init__)
    params = list(sig.parameters.keys())
    assert "CPUTime" in params, "Missing parameter 'CPUTime'"
    assert "methodName" in params, "Missing parameter 'methodName'"
    assert "DBRowsNumber" in params, "Missing parameter 'DBRowsNumber'"
    assert "DBAccessesNumber" in params, "Missing parameter 'DBAccessesNumber'"

def test_trace_call_has_CPUTime():
    assert hasattr(Trace_Call, "CPUTime")
    descriptor = None
    for klass in Trace_Call.__mro__:
        if "CPUTime" in klass.__dict__:
            descriptor = klass.__dict__["CPUTime"]
            break
    assert isinstance(descriptor, property)

def test_trace_call_has_methodName():
    assert hasattr(Trace_Call, "methodName")
    descriptor = None
    for klass in Trace_Call.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)

def test_trace_call_has_DBRowsNumber():
    assert hasattr(Trace_Call, "DBRowsNumber")
    descriptor = None
    for klass in Trace_Call.__mro__:
        if "DBRowsNumber" in klass.__dict__:
            descriptor = klass.__dict__["DBRowsNumber"]
            break
    assert isinstance(descriptor, property)

def test_trace_call_has_DBAccessesNumber():
    assert hasattr(Trace_Call, "DBAccessesNumber")
    descriptor = None
    for klass in Trace_Call.__mro__:
        if "DBAccessesNumber" in klass.__dict__:
            descriptor = klass.__dict__["DBAccessesNumber"]
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



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(Trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(Trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(Trace_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trace_trace_has_name():
    assert hasattr(Trace_Trace, "name")
    descriptor = None
    for klass in Trace_Trace.__mro__:
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



def test_trace_level_is_not_abstract():
    assert not inspect.isabstract(Trace_Level)


def test_trace_level_constructor_exists():
    assert callable(Trace_Level.__init__)


def test_trace_level_constructor_args():
    sig = inspect.signature(Trace_Level.__init__)
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
Trace_Index_strategy = st.builds(
    Trace_Index,
    value=
        safe_text
)
Index_strategy = st.builds(
    Index,
)
Trace_Call_strategy = st.builds(
    Trace_Call,
    CPUTime=
        safe_text,
    methodName=
        safe_text,
    DBRowsNumber=
        safe_text,
    DBAccessesNumber=
        safe_text
)
Call_strategy = st.builds(
    Call,
)
Level_strategy = st.builds(
    Level,
)
Trace_Trace_strategy = st.builds(
    Trace_Trace,
    name=
        safe_text
)
Trace_strategy = st.builds(
    Trace,
)
Trace_Level_strategy = st.builds(
    Trace_Level,
)

@given(instance=Trace_Index_strategy)
@settings(max_examples=50)
def test_trace_index_instantiation(instance):
    assert isinstance(instance, Trace_Index)



@given(instance=Trace_Index_strategy)
def test_trace_index_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=Trace_Call_strategy)
@settings(max_examples=50)
def test_trace_call_instantiation(instance):
    assert isinstance(instance, Trace_Call)



@given(instance=Trace_Call_strategy)
def test_trace_call_CPUTime_setter(instance):
    original = instance.CPUTime
    instance.CPUTime = original
    assert instance.CPUTime == original



@given(instance=Trace_Call_strategy)
def test_trace_call_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original



@given(instance=Trace_Call_strategy)
def test_trace_call_DBRowsNumber_setter(instance):
    original = instance.DBRowsNumber
    instance.DBRowsNumber = original
    assert instance.DBRowsNumber == original



@given(instance=Trace_Call_strategy)
def test_trace_call_DBAccessesNumber_setter(instance):
    original = instance.DBAccessesNumber
    instance.DBAccessesNumber = original
    assert instance.DBAccessesNumber == original

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_call_instantiation(instance):
    assert isinstance(instance, Call)

@given(instance=Level_strategy)
@settings(max_examples=50)
def test_level_instantiation(instance):
    assert isinstance(instance, Level)

@given(instance=Trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, Trace_Trace)



@given(instance=Trace_Trace_strategy)
def test_trace_trace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Trace_strategy)
@settings(max_examples=50)
def test_trace_instantiation(instance):
    assert isinstance(instance, Trace)

@given(instance=Trace_Level_strategy)
@settings(max_examples=50)
def test_trace_level_instantiation(instance):
    assert isinstance(instance, Trace_Level)
