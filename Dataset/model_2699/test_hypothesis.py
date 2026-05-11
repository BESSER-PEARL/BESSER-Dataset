import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    democea::ConceptC,
    ConceptA,
    democea::ConceptB,
    democea::ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_democea::conceptc_is_not_abstract():
    assert not inspect.isabstract(democea::ConceptC)


def test_democea::conceptc_constructor_exists():
    assert callable(democea::ConceptC.__init__)


def test_democea::conceptc_constructor_args():
    sig = inspect.signature(democea::ConceptC.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_democea::conceptc_has_value():
    assert hasattr(democea::ConceptC, "value")
    descriptor = None
    for klass in democea::ConceptC.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_democea::conceptb_is_not_abstract():
    assert not inspect.isabstract(democea::ConceptB)


def test_democea::conceptb_constructor_exists():
    assert callable(democea::ConceptB.__init__)


def test_democea::conceptb_constructor_args():
    sig = inspect.signature(democea::ConceptB.__init__)
    params = list(sig.parameters.keys())



def test_democea::concepta_is_not_abstract():
    assert not inspect.isabstract(democea::ConceptA)


def test_democea::concepta_constructor_exists():
    assert callable(democea::ConceptA.__init__)


def test_democea::concepta_constructor_args():
    sig = inspect.signature(democea::ConceptA.__init__)
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
democea::ConceptC_strategy = st.builds(
    democea::ConceptC,
    value=
        st.integers()
)
ConceptA_strategy = st.builds(
    ConceptA,
)
democea::ConceptB_strategy = st.builds(
    democea::ConceptB,
)
democea::ConceptA_strategy = st.builds(
    democea::ConceptA,
)

@given(instance=democea::ConceptC_strategy)
@settings(max_examples=50)
def test_democea::conceptc_instantiation(instance):
    assert isinstance(instance, democea::ConceptC)

@given(instance=democea::ConceptC_strategy)
def test_democea::conceptc_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=democea::ConceptC_strategy)
def test_democea::conceptc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=democea::ConceptB_strategy)
@settings(max_examples=50)
def test_democea::conceptb_instantiation(instance):
    assert isinstance(instance, democea::ConceptB)

@given(instance=democea::ConceptA_strategy)
@settings(max_examples=50)
def test_democea::concepta_instantiation(instance):
    assert isinstance(instance, democea::ConceptA)
