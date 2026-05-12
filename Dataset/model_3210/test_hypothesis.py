import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rm_VariableReference,
    rm_MemoryCellReference,
    rm_Memory,
    rm_Device,
    rm_ResourceModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rm_variablereference_is_not_abstract():
    assert not inspect.isabstract(rm_VariableReference)


def test_rm_variablereference_constructor_exists():
    assert callable(rm_VariableReference.__init__)


def test_rm_variablereference_constructor_args():
    sig = inspect.signature(rm_VariableReference.__init__)
    params = list(sig.parameters.keys())
    assert "memoryCellIndex" in params, "Missing parameter 'memoryCellIndex'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_rm_variablereference_has_memoryCellIndex():
    assert hasattr(rm_VariableReference, "memoryCellIndex")
    descriptor = None
    for klass in rm_VariableReference.__mro__:
        if "memoryCellIndex" in klass.__dict__:
            descriptor = klass.__dict__["memoryCellIndex"]
            break
    assert isinstance(descriptor, property)

def test_rm_variablereference_has_variable():
    assert hasattr(rm_VariableReference, "variable")
    descriptor = None
    for klass in rm_VariableReference.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_rm_memorycellreference_is_not_abstract():
    assert not inspect.isabstract(rm_MemoryCellReference)


def test_rm_memorycellreference_constructor_exists():
    assert callable(rm_MemoryCellReference.__init__)


def test_rm_memorycellreference_constructor_args():
    sig = inspect.signature(rm_MemoryCellReference.__init__)
    params = list(sig.parameters.keys())
    assert "endCellIndex" in params, "Missing parameter 'endCellIndex'"
    assert "startCellIndex" in params, "Missing parameter 'startCellIndex'"

def test_rm_memorycellreference_has_endCellIndex():
    assert hasattr(rm_MemoryCellReference, "endCellIndex")
    descriptor = None
    for klass in rm_MemoryCellReference.__mro__:
        if "endCellIndex" in klass.__dict__:
            descriptor = klass.__dict__["endCellIndex"]
            break
    assert isinstance(descriptor, property)

def test_rm_memorycellreference_has_startCellIndex():
    assert hasattr(rm_MemoryCellReference, "startCellIndex")
    descriptor = None
    for klass in rm_MemoryCellReference.__mro__:
        if "startCellIndex" in klass.__dict__:
            descriptor = klass.__dict__["startCellIndex"]
            break
    assert isinstance(descriptor, property)



def test_rm_memory_is_not_abstract():
    assert not inspect.isabstract(rm_Memory)


def test_rm_memory_constructor_exists():
    assert callable(rm_Memory.__init__)


def test_rm_memory_constructor_args():
    sig = inspect.signature(rm_Memory.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_rm_memory_has_size():
    assert hasattr(rm_Memory, "size")
    descriptor = None
    for klass in rm_Memory.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_rm_device_is_not_abstract():
    assert not inspect.isabstract(rm_Device)


def test_rm_device_constructor_exists():
    assert callable(rm_Device.__init__)


def test_rm_device_constructor_args():
    sig = inspect.signature(rm_Device.__init__)
    params = list(sig.parameters.keys())
    assert "cacheSize" in params, "Missing parameter 'cacheSize'"

def test_rm_device_has_cacheSize():
    assert hasattr(rm_Device, "cacheSize")
    descriptor = None
    for klass in rm_Device.__mro__:
        if "cacheSize" in klass.__dict__:
            descriptor = klass.__dict__["cacheSize"]
            break
    assert isinstance(descriptor, property)



def test_rm_resourcemodel_is_not_abstract():
    assert not inspect.isabstract(rm_ResourceModel)


def test_rm_resourcemodel_constructor_exists():
    assert callable(rm_ResourceModel.__init__)


def test_rm_resourcemodel_constructor_args():
    sig = inspect.signature(rm_ResourceModel.__init__)
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
rm_VariableReference_strategy = st.builds(
    rm_VariableReference,
    memoryCellIndex=
        st.integers(),
    variable=
        safe_text
)
rm_MemoryCellReference_strategy = st.builds(
    rm_MemoryCellReference,
    endCellIndex=
        st.integers(),
    startCellIndex=
        st.integers()
)
rm_Memory_strategy = st.builds(
    rm_Memory,
    size=
        st.integers()
)
rm_Device_strategy = st.builds(
    rm_Device,
    cacheSize=
        st.integers()
)
rm_ResourceModel_strategy = st.builds(
    rm_ResourceModel,
)

@given(instance=rm_VariableReference_strategy)
@settings(max_examples=50)
def test_rm_variablereference_instantiation(instance):
    assert isinstance(instance, rm_VariableReference)



@given(instance=rm_VariableReference_strategy)
def test_rm_variablereference_memoryCellIndex_setter(instance):
    original = instance.memoryCellIndex
    instance.memoryCellIndex = original
    assert instance.memoryCellIndex == original



@given(instance=rm_VariableReference_strategy)
def test_rm_variablereference_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=rm_MemoryCellReference_strategy)
@settings(max_examples=50)
def test_rm_memorycellreference_instantiation(instance):
    assert isinstance(instance, rm_MemoryCellReference)



@given(instance=rm_MemoryCellReference_strategy)
def test_rm_memorycellreference_endCellIndex_setter(instance):
    original = instance.endCellIndex
    instance.endCellIndex = original
    assert instance.endCellIndex == original



@given(instance=rm_MemoryCellReference_strategy)
def test_rm_memorycellreference_startCellIndex_setter(instance):
    original = instance.startCellIndex
    instance.startCellIndex = original
    assert instance.startCellIndex == original

@given(instance=rm_Memory_strategy)
@settings(max_examples=50)
def test_rm_memory_instantiation(instance):
    assert isinstance(instance, rm_Memory)



@given(instance=rm_Memory_strategy)
def test_rm_memory_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=rm_Device_strategy)
@settings(max_examples=50)
def test_rm_device_instantiation(instance):
    assert isinstance(instance, rm_Device)



@given(instance=rm_Device_strategy)
def test_rm_device_cacheSize_setter(instance):
    original = instance.cacheSize
    instance.cacheSize = original
    assert instance.cacheSize == original

@given(instance=rm_ResourceModel_strategy)
@settings(max_examples=50)
def test_rm_resourcemodel_instantiation(instance):
    assert isinstance(instance, rm_ResourceModel)
