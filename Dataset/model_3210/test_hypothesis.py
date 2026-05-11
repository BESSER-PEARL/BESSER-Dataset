import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rm::VariableReference,
    rm::MemoryCellReference,
    rm::Memory,
    rm::Device,
    rm::ResourceModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rm::variablereference_is_not_abstract():
    assert not inspect.isabstract(rm::VariableReference)


def test_rm::variablereference_constructor_exists():
    assert callable(rm::VariableReference.__init__)


def test_rm::variablereference_constructor_args():
    sig = inspect.signature(rm::VariableReference.__init__)
    params = list(sig.parameters.keys())
    assert "memoryCellIndex" in params, "Missing parameter 'memoryCellIndex'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_rm::variablereference_has_memoryCellIndex():
    assert hasattr(rm::VariableReference, "memoryCellIndex")
    descriptor = None
    for klass in rm::VariableReference.__mro__:
        if "memoryCellIndex" in klass.__dict__:
            descriptor = klass.__dict__["memoryCellIndex"]
            break
    assert isinstance(descriptor, property)

def test_rm::variablereference_has_variable():
    assert hasattr(rm::VariableReference, "variable")
    descriptor = None
    for klass in rm::VariableReference.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_rm::memorycellreference_is_not_abstract():
    assert not inspect.isabstract(rm::MemoryCellReference)


def test_rm::memorycellreference_constructor_exists():
    assert callable(rm::MemoryCellReference.__init__)


def test_rm::memorycellreference_constructor_args():
    sig = inspect.signature(rm::MemoryCellReference.__init__)
    params = list(sig.parameters.keys())
    assert "endCellIndex" in params, "Missing parameter 'endCellIndex'"
    assert "startCellIndex" in params, "Missing parameter 'startCellIndex'"

def test_rm::memorycellreference_has_endCellIndex():
    assert hasattr(rm::MemoryCellReference, "endCellIndex")
    descriptor = None
    for klass in rm::MemoryCellReference.__mro__:
        if "endCellIndex" in klass.__dict__:
            descriptor = klass.__dict__["endCellIndex"]
            break
    assert isinstance(descriptor, property)

def test_rm::memorycellreference_has_startCellIndex():
    assert hasattr(rm::MemoryCellReference, "startCellIndex")
    descriptor = None
    for klass in rm::MemoryCellReference.__mro__:
        if "startCellIndex" in klass.__dict__:
            descriptor = klass.__dict__["startCellIndex"]
            break
    assert isinstance(descriptor, property)



def test_rm::memory_is_not_abstract():
    assert not inspect.isabstract(rm::Memory)


def test_rm::memory_constructor_exists():
    assert callable(rm::Memory.__init__)


def test_rm::memory_constructor_args():
    sig = inspect.signature(rm::Memory.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_rm::memory_has_size():
    assert hasattr(rm::Memory, "size")
    descriptor = None
    for klass in rm::Memory.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_rm::device_is_not_abstract():
    assert not inspect.isabstract(rm::Device)


def test_rm::device_constructor_exists():
    assert callable(rm::Device.__init__)


def test_rm::device_constructor_args():
    sig = inspect.signature(rm::Device.__init__)
    params = list(sig.parameters.keys())
    assert "cacheSize" in params, "Missing parameter 'cacheSize'"

def test_rm::device_has_cacheSize():
    assert hasattr(rm::Device, "cacheSize")
    descriptor = None
    for klass in rm::Device.__mro__:
        if "cacheSize" in klass.__dict__:
            descriptor = klass.__dict__["cacheSize"]
            break
    assert isinstance(descriptor, property)



def test_rm::resourcemodel_is_not_abstract():
    assert not inspect.isabstract(rm::ResourceModel)


def test_rm::resourcemodel_constructor_exists():
    assert callable(rm::ResourceModel.__init__)


def test_rm::resourcemodel_constructor_args():
    sig = inspect.signature(rm::ResourceModel.__init__)
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
rm::VariableReference_strategy = st.builds(
    rm::VariableReference,
    memoryCellIndex=
        st.integers(),
    variable=
        safe_text
)
rm::MemoryCellReference_strategy = st.builds(
    rm::MemoryCellReference,
    endCellIndex=
        st.integers(),
    startCellIndex=
        st.integers()
)
rm::Memory_strategy = st.builds(
    rm::Memory,
    size=
        st.integers()
)
rm::Device_strategy = st.builds(
    rm::Device,
    cacheSize=
        st.integers()
)
rm::ResourceModel_strategy = st.builds(
    rm::ResourceModel,
)

@given(instance=rm::VariableReference_strategy)
@settings(max_examples=50)
def test_rm::variablereference_instantiation(instance):
    assert isinstance(instance, rm::VariableReference)

@given(instance=rm::VariableReference_strategy)
def test_rm::variablereference_memoryCellIndex_type(instance):
    assert isinstance(instance.memoryCellIndex, int)


@given(instance=rm::VariableReference_strategy)
def test_rm::variablereference_memoryCellIndex_setter(instance):
    original = instance.memoryCellIndex
    instance.memoryCellIndex = original
    assert instance.memoryCellIndex == original

@given(instance=rm::VariableReference_strategy)
def test_rm::variablereference_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=rm::VariableReference_strategy)
def test_rm::variablereference_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=rm::MemoryCellReference_strategy)
@settings(max_examples=50)
def test_rm::memorycellreference_instantiation(instance):
    assert isinstance(instance, rm::MemoryCellReference)

@given(instance=rm::MemoryCellReference_strategy)
def test_rm::memorycellreference_endCellIndex_type(instance):
    assert isinstance(instance.endCellIndex, int)


@given(instance=rm::MemoryCellReference_strategy)
def test_rm::memorycellreference_endCellIndex_setter(instance):
    original = instance.endCellIndex
    instance.endCellIndex = original
    assert instance.endCellIndex == original

@given(instance=rm::MemoryCellReference_strategy)
def test_rm::memorycellreference_startCellIndex_type(instance):
    assert isinstance(instance.startCellIndex, int)


@given(instance=rm::MemoryCellReference_strategy)
def test_rm::memorycellreference_startCellIndex_setter(instance):
    original = instance.startCellIndex
    instance.startCellIndex = original
    assert instance.startCellIndex == original

@given(instance=rm::Memory_strategy)
@settings(max_examples=50)
def test_rm::memory_instantiation(instance):
    assert isinstance(instance, rm::Memory)

@given(instance=rm::Memory_strategy)
def test_rm::memory_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=rm::Memory_strategy)
def test_rm::memory_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=rm::Device_strategy)
@settings(max_examples=50)
def test_rm::device_instantiation(instance):
    assert isinstance(instance, rm::Device)

@given(instance=rm::Device_strategy)
def test_rm::device_cacheSize_type(instance):
    assert isinstance(instance.cacheSize, int)


@given(instance=rm::Device_strategy)
def test_rm::device_cacheSize_setter(instance):
    original = instance.cacheSize
    instance.cacheSize = original
    assert instance.cacheSize == original

@given(instance=rm::ResourceModel_strategy)
@settings(max_examples=50)
def test_rm::resourcemodel_instantiation(instance):
    assert isinstance(instance, rm::ResourceModel)
