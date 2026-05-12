import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    autocast_ConceptC,
    ConceptA,
    autocast_ConceptB,
    autocast_ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_autocast_conceptc_is_not_abstract():
    assert not inspect.isabstract(autocast_ConceptC)


def test_autocast_conceptc_constructor_exists():
    assert callable(autocast_ConceptC.__init__)


def test_autocast_conceptc_constructor_args():
    sig = inspect.signature(autocast_ConceptC.__init__)
    params = list(sig.parameters.keys())



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_autocast_conceptb_is_not_abstract():
    assert not inspect.isabstract(autocast_ConceptB)


def test_autocast_conceptb_constructor_exists():
    assert callable(autocast_ConceptB.__init__)


def test_autocast_conceptb_constructor_args():
    sig = inspect.signature(autocast_ConceptB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_autocast_conceptb_has_name():
    assert hasattr(autocast_ConceptB, "name")
    descriptor = None
    for klass in autocast_ConceptB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_autocast_concepta_is_not_abstract():
    assert not inspect.isabstract(autocast_ConceptA)


def test_autocast_concepta_constructor_exists():
    assert callable(autocast_ConceptA.__init__)


def test_autocast_concepta_constructor_args():
    sig = inspect.signature(autocast_ConceptA.__init__)
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
autocast_ConceptC_strategy = st.builds(
    autocast_ConceptC,
)
ConceptA_strategy = st.builds(
    ConceptA,
)
autocast_ConceptB_strategy = st.builds(
    autocast_ConceptB,
    name=
        safe_text
)
autocast_ConceptA_strategy = st.builds(
    autocast_ConceptA,
)

@given(instance=autocast_ConceptC_strategy)
@settings(max_examples=50)
def test_autocast_conceptc_instantiation(instance):
    assert isinstance(instance, autocast_ConceptC)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=autocast_ConceptB_strategy)
@settings(max_examples=50)
def test_autocast_conceptb_instantiation(instance):
    assert isinstance(instance, autocast_ConceptB)



@given(instance=autocast_ConceptB_strategy)
def test_autocast_conceptb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=autocast_ConceptA_strategy)
@settings(max_examples=50)
def test_autocast_concepta_instantiation(instance):
    assert isinstance(instance, autocast_ConceptA)
