import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RAM,
    Cache,
    Memory_Interface,
    Processor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ram_is_not_abstract():
    assert not inspect.isabstract(RAM)


def test_ram_constructor_exists():
    assert callable(RAM.__init__)


def test_ram_constructor_args():
    sig = inspect.signature(RAM.__init__)
    params = list(sig.parameters.keys())



def test_cache_is_not_abstract():
    assert not inspect.isabstract(Cache)


def test_cache_constructor_exists():
    assert callable(Cache.__init__)


def test_cache_constructor_args():
    sig = inspect.signature(Cache.__init__)
    params = list(sig.parameters.keys())
    assert "chunck" in params, "Missing parameter 'chunck'"

def test_cache_has_chunck():
    assert hasattr(Cache, "chunck")
    descriptor = None
    for klass in Cache.__mro__:
        if "chunck" in klass.__dict__:
            descriptor = klass.__dict__["chunck"]
            break
    assert isinstance(descriptor, property)



def test_memory_interface_is_not_abstract():
    assert not inspect.isabstract(Memory_Interface)


def test_memory_interface_constructor_exists():
    assert callable(Memory_Interface.__init__)


def test_memory_interface_constructor_args():
    sig = inspect.signature(Memory_Interface.__init__)
    params = list(sig.parameters.keys())



def test_processor_is_not_abstract():
    assert not inspect.isabstract(Processor)


def test_processor_constructor_exists():
    assert callable(Processor.__init__)


def test_processor_constructor_args():
    sig = inspect.signature(Processor.__init__)
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
RAM_strategy = st.builds(
    RAM,
)
Cache_strategy = st.builds(
    Cache,
    chunck=
        safe_text
)
Memory_Interface_strategy = st.builds(
    Memory_Interface,
)
Processor_strategy = st.builds(
    Processor,
)

@given(instance=RAM_strategy)
@settings(max_examples=50)
def test_ram_instantiation(instance):
    assert isinstance(instance, RAM)

@given(instance=Cache_strategy)
@settings(max_examples=50)
def test_cache_instantiation(instance):
    assert isinstance(instance, Cache)



@given(instance=Cache_strategy)
def test_cache_chunck_setter(instance):
    original = instance.chunck
    instance.chunck = original
    assert instance.chunck == original

@given(instance=Memory_Interface_strategy)
@settings(max_examples=50)
def test_memory_interface_instantiation(instance):
    assert isinstance(instance, Memory_Interface)

@given(instance=Processor_strategy)
@settings(max_examples=50)
def test_processor_instantiation(instance):
    assert isinstance(instance, Processor)
