import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    democea_ConceptC,
    ConceptA,
    democea_ConceptB,
    democea_ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_democea_conceptc_is_not_abstract():
    assert not inspect.isabstract(democea_ConceptC)


def test_democea_conceptc_constructor_exists():
    assert callable(democea_ConceptC.__init__)


def test_democea_conceptc_constructor_args():
    sig = inspect.signature(democea_ConceptC.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_democea_conceptc_has_value():
    assert hasattr(democea_ConceptC, "value")
    descriptor = None
    for klass in democea_ConceptC.__mro__:
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



def test_democea_conceptb_is_not_abstract():
    assert not inspect.isabstract(democea_ConceptB)


def test_democea_conceptb_constructor_exists():
    assert callable(democea_ConceptB.__init__)


def test_democea_conceptb_constructor_args():
    sig = inspect.signature(democea_ConceptB.__init__)
    params = list(sig.parameters.keys())



def test_democea_concepta_is_not_abstract():
    assert not inspect.isabstract(democea_ConceptA)


def test_democea_concepta_constructor_exists():
    assert callable(democea_ConceptA.__init__)


def test_democea_concepta_constructor_args():
    sig = inspect.signature(democea_ConceptA.__init__)
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
democea_ConceptC_strategy = st.builds(
    democea_ConceptC,
    value=
        st.integers()
)
ConceptA_strategy = st.builds(
    ConceptA,
)
democea_ConceptB_strategy = st.builds(
    democea_ConceptB,
)
democea_ConceptA_strategy = st.builds(
    democea_ConceptA,
)

@given(instance=democea_ConceptC_strategy)
@settings(max_examples=50)
def test_democea_conceptc_instantiation(instance):
    assert isinstance(instance, democea_ConceptC)



@given(instance=democea_ConceptC_strategy)
def test_democea_conceptc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=democea_ConceptB_strategy)
@settings(max_examples=50)
def test_democea_conceptb_instantiation(instance):
    assert isinstance(instance, democea_ConceptB)

@given(instance=democea_ConceptA_strategy)
@settings(max_examples=50)
def test_democea_concepta_instantiation(instance):
    assert isinstance(instance, democea_ConceptA)
