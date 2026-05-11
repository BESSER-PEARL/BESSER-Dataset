import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2::Class,
    UML2::Reception,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2::class_is_not_abstract():
    assert not inspect.isabstract(UML2::Class)


def test_uml2::class_constructor_exists():
    assert callable(UML2::Class.__init__)


def test_uml2::class_constructor_args():
    sig = inspect.signature(UML2::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml2::class_has_isActive():
    assert hasattr(UML2::Class, "isActive")
    descriptor = None
    for klass in UML2::Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_uml2::reception_is_not_abstract():
    assert not inspect.isabstract(UML2::Reception)


def test_uml2::reception_constructor_exists():
    assert callable(UML2::Reception.__init__)


def test_uml2::reception_constructor_args():
    sig = inspect.signature(UML2::Reception.__init__)
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
UML2::Class_strategy = st.builds(
    UML2::Class,
    isActive=
        st.booleans()
)
UML2::Reception_strategy = st.builds(
    UML2::Reception,
)

@given(instance=UML2::Class_strategy)
@settings(max_examples=50)
def test_uml2::class_instantiation(instance):
    assert isinstance(instance, UML2::Class)

@given(instance=UML2::Class_strategy)
def test_uml2::class_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=UML2::Class_strategy)
def test_uml2::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=UML2::Reception_strategy)
@settings(max_examples=50)
def test_uml2::reception_instantiation(instance):
    assert isinstance(instance, UML2::Reception)
