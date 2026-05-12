import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    positionmm_NamedElement,
    NamedElement,
    positionmm_Counter,
    TypeScript,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_positionmm_namedelement_is_not_abstract():
    assert not inspect.isabstract(positionmm_NamedElement)


def test_positionmm_namedelement_constructor_exists():
    assert callable(positionmm_NamedElement.__init__)


def test_positionmm_namedelement_constructor_args():
    sig = inspect.signature(positionmm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_positionmm_namedelement_has_name():
    assert hasattr(positionmm_NamedElement, "name")
    descriptor = None
    for klass in positionmm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_positionmm_counter_is_not_abstract():
    assert not inspect.isabstract(positionmm_Counter)


def test_positionmm_counter_constructor_exists():
    assert callable(positionmm_Counter.__init__)


def test_positionmm_counter_constructor_args():
    sig = inspect.signature(positionmm_Counter.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "script" in params, "Missing parameter 'script'"

def test_positionmm_counter_has_position():
    assert hasattr(positionmm_Counter, "position")
    descriptor = None
    for klass in positionmm_Counter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_positionmm_counter_has_script():
    assert hasattr(positionmm_Counter, "script")
    descriptor = None
    for klass in positionmm_Counter.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)

def test_typescript_exists():
    # Check that the Enumeration exists
    assert TypeScript is not None

def test_typescript_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeScript]
    expected_literals = [
        "PreinstScript",
        "PostrmScript",
        "PostinstScript",
        "PrermScript",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeScript"


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
positionmm_NamedElement_strategy = st.builds(
    positionmm_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
positionmm_Counter_strategy = st.builds(
    positionmm_Counter,
    position=
        st.integers(),
    script=
        safe_text
)

@given(instance=positionmm_NamedElement_strategy)
@settings(max_examples=50)
def test_positionmm_namedelement_instantiation(instance):
    assert isinstance(instance, positionmm_NamedElement)



@given(instance=positionmm_NamedElement_strategy)
def test_positionmm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=positionmm_Counter_strategy)
@settings(max_examples=50)
def test_positionmm_counter_instantiation(instance):
    assert isinstance(instance, positionmm_Counter)



@given(instance=positionmm_Counter_strategy)
def test_positionmm_counter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=positionmm_Counter_strategy)
def test_positionmm_counter_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original
