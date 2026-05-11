import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    autocast::ConceptC,
    ConceptA,
    autocast::ConceptB,
    autocast::ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_autocast::conceptc_is_not_abstract():
    assert not inspect.isabstract(autocast::ConceptC)


def test_autocast::conceptc_constructor_exists():
    assert callable(autocast::ConceptC.__init__)


def test_autocast::conceptc_constructor_args():
    sig = inspect.signature(autocast::ConceptC.__init__)
    params = list(sig.parameters.keys())



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_autocast::conceptb_is_not_abstract():
    assert not inspect.isabstract(autocast::ConceptB)


def test_autocast::conceptb_constructor_exists():
    assert callable(autocast::ConceptB.__init__)


def test_autocast::conceptb_constructor_args():
    sig = inspect.signature(autocast::ConceptB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_autocast::conceptb_has_name():
    assert hasattr(autocast::ConceptB, "name")
    descriptor = None
    for klass in autocast::ConceptB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_autocast::concepta_is_not_abstract():
    assert not inspect.isabstract(autocast::ConceptA)


def test_autocast::concepta_constructor_exists():
    assert callable(autocast::ConceptA.__init__)


def test_autocast::concepta_constructor_args():
    sig = inspect.signature(autocast::ConceptA.__init__)
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
autocast::ConceptC_strategy = st.builds(
    autocast::ConceptC,
)
ConceptA_strategy = st.builds(
    ConceptA,
)
autocast::ConceptB_strategy = st.builds(
    autocast::ConceptB,
    name=
        safe_text
)
autocast::ConceptA_strategy = st.builds(
    autocast::ConceptA,
)

@given(instance=autocast::ConceptC_strategy)
@settings(max_examples=50)
def test_autocast::conceptc_instantiation(instance):
    assert isinstance(instance, autocast::ConceptC)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=autocast::ConceptB_strategy)
@settings(max_examples=50)
def test_autocast::conceptb_instantiation(instance):
    assert isinstance(instance, autocast::ConceptB)

@given(instance=autocast::ConceptB_strategy)
def test_autocast::conceptb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=autocast::ConceptB_strategy)
def test_autocast::conceptb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=autocast::ConceptA_strategy)
@settings(max_examples=50)
def test_autocast::concepta_instantiation(instance):
    assert isinstance(instance, autocast::ConceptA)
