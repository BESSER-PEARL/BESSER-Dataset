import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML2_Reception,
    UML2_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2_reception_is_not_abstract():
    assert not inspect.isabstract(UML2_Reception)


def test_uml2_reception_constructor_exists():
    assert callable(UML2_Reception.__init__)


def test_uml2_reception_constructor_args():
    sig = inspect.signature(UML2_Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2_class_is_not_abstract():
    assert not inspect.isabstract(UML2_Class)


def test_uml2_class_constructor_exists():
    assert callable(UML2_Class.__init__)


def test_uml2_class_constructor_args():
    sig = inspect.signature(UML2_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml2_class_has_isActive():
    assert hasattr(UML2_Class, "isActive")
    descriptor = None
    for klass in UML2_Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
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
UML2_Reception_strategy = st.builds(
    UML2_Reception,
)
UML2_Class_strategy = st.builds(
    UML2_Class,
    isActive=
        st.booleans()
)

@given(instance=UML2_Reception_strategy)
@settings(max_examples=50)
def test_uml2_reception_instantiation(instance):
    assert isinstance(instance, UML2_Reception)

@given(instance=UML2_Class_strategy)
@settings(max_examples=50)
def test_uml2_class_instantiation(instance):
    assert isinstance(instance, UML2_Class)



@given(instance=UML2_Class_strategy)
def test_uml2_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original
