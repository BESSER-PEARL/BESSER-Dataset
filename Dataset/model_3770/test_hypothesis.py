import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecore::EClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecore::eclass_is_not_abstract():
    assert not inspect.isabstract(ecore::EClass)


def test_ecore::eclass_constructor_exists():
    assert callable(ecore::EClass.__init__)


def test_ecore::eclass_constructor_args():
    sig = inspect.signature(ecore::EClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ecore::eclass_has_abstract():
    assert hasattr(ecore::EClass, "abstract")
    descriptor = None
    for klass in ecore::EClass.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)


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
ecore::EClass_strategy = st.builds(
    ecore::EClass,
    abstract=
        safe_text
)

@given(instance=ecore::EClass_strategy)
@settings(max_examples=50)
def test_ecore::eclass_instantiation(instance):
    assert isinstance(instance, ecore::EClass)

@given(instance=ecore::EClass_strategy)
def test_ecore::eclass_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=ecore::EClass_strategy)
def test_ecore::eclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original
