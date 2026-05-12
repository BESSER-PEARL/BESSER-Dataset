import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    facademapping_FacadeMappping,
    Mapping,
    facademapping_StereotypedMapping,
    facademapping_EObject,
    facademapping_Mapping,
    ExtensionDefinitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_facademapping_facademappping_is_not_abstract():
    assert not inspect.isabstract(facademapping_FacadeMappping)


def test_facademapping_facademappping_constructor_exists():
    assert callable(facademapping_FacadeMappping.__init__)


def test_facademapping_facademappping_constructor_args():
    sig = inspect.signature(facademapping_FacadeMappping.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_facademapping_stereotypedmapping_is_not_abstract():
    assert not inspect.isabstract(facademapping_StereotypedMapping)


def test_facademapping_stereotypedmapping_constructor_exists():
    assert callable(facademapping_StereotypedMapping.__init__)


def test_facademapping_stereotypedmapping_constructor_args():
    sig = inspect.signature(facademapping_StereotypedMapping.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_facademapping_stereotypedmapping_has_kind():
    assert hasattr(facademapping_StereotypedMapping, "kind")
    descriptor = None
    for klass in facademapping_StereotypedMapping.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_facademapping_eobject_is_not_abstract():
    assert not inspect.isabstract(facademapping_EObject)


def test_facademapping_eobject_constructor_exists():
    assert callable(facademapping_EObject.__init__)


def test_facademapping_eobject_constructor_args():
    sig = inspect.signature(facademapping_EObject.__init__)
    params = list(sig.parameters.keys())



def test_facademapping_mapping_is_not_abstract():
    assert not inspect.isabstract(facademapping_Mapping)


def test_facademapping_mapping_constructor_exists():
    assert callable(facademapping_Mapping.__init__)


def test_facademapping_mapping_constructor_args():
    sig = inspect.signature(facademapping_Mapping.__init__)
    params = list(sig.parameters.keys())

def test_extensiondefinitionkind_exists():
    # Check that the Enumeration exists
    assert ExtensionDefinitionKind is not None

def test_extensiondefinitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExtensionDefinitionKind]
    expected_literals = [
        "Fusion",
        "Association",
        "MultiGeneralization",
        "Generalization",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExtensionDefinitionKind"


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
facademapping_FacadeMappping_strategy = st.builds(
    facademapping_FacadeMappping,
)
Mapping_strategy = st.builds(
    Mapping,
)
facademapping_StereotypedMapping_strategy = st.builds(
    facademapping_StereotypedMapping,
    kind=
        safe_text
)
facademapping_EObject_strategy = st.builds(
    facademapping_EObject,
)
facademapping_Mapping_strategy = st.builds(
    facademapping_Mapping,
)

@given(instance=facademapping_FacadeMappping_strategy)
@settings(max_examples=50)
def test_facademapping_facademappping_instantiation(instance):
    assert isinstance(instance, facademapping_FacadeMappping)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=facademapping_StereotypedMapping_strategy)
@settings(max_examples=50)
def test_facademapping_stereotypedmapping_instantiation(instance):
    assert isinstance(instance, facademapping_StereotypedMapping)



@given(instance=facademapping_StereotypedMapping_strategy)
def test_facademapping_stereotypedmapping_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=facademapping_EObject_strategy)
@settings(max_examples=50)
def test_facademapping_eobject_instantiation(instance):
    assert isinstance(instance, facademapping_EObject)

@given(instance=facademapping_Mapping_strategy)
@settings(max_examples=50)
def test_facademapping_mapping_instantiation(instance):
    assert isinstance(instance, facademapping_Mapping)
