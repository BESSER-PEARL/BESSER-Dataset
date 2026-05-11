import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    facademapping::FacadeMappping,
    Mapping,
    facademapping::StereotypedMapping,
    facademapping::EObject,
    facademapping::Mapping,
    ExtensionDefinitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_facademapping::facademappping_is_not_abstract():
    assert not inspect.isabstract(facademapping::FacadeMappping)


def test_facademapping::facademappping_constructor_exists():
    assert callable(facademapping::FacadeMappping.__init__)


def test_facademapping::facademappping_constructor_args():
    sig = inspect.signature(facademapping::FacadeMappping.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_facademapping::stereotypedmapping_is_not_abstract():
    assert not inspect.isabstract(facademapping::StereotypedMapping)


def test_facademapping::stereotypedmapping_constructor_exists():
    assert callable(facademapping::StereotypedMapping.__init__)


def test_facademapping::stereotypedmapping_constructor_args():
    sig = inspect.signature(facademapping::StereotypedMapping.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_facademapping::stereotypedmapping_has_kind():
    assert hasattr(facademapping::StereotypedMapping, "kind")
    descriptor = None
    for klass in facademapping::StereotypedMapping.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_facademapping::eobject_is_not_abstract():
    assert not inspect.isabstract(facademapping::EObject)


def test_facademapping::eobject_constructor_exists():
    assert callable(facademapping::EObject.__init__)


def test_facademapping::eobject_constructor_args():
    sig = inspect.signature(facademapping::EObject.__init__)
    params = list(sig.parameters.keys())



def test_facademapping::mapping_is_not_abstract():
    assert not inspect.isabstract(facademapping::Mapping)


def test_facademapping::mapping_constructor_exists():
    assert callable(facademapping::Mapping.__init__)


def test_facademapping::mapping_constructor_args():
    sig = inspect.signature(facademapping::Mapping.__init__)
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
        "Generalization",
        "MultiGeneralization",
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
facademapping::FacadeMappping_strategy = st.builds(
    facademapping::FacadeMappping,
)
Mapping_strategy = st.builds(
    Mapping,
)
facademapping::StereotypedMapping_strategy = st.builds(
    facademapping::StereotypedMapping,
    kind=
        safe_text
)
facademapping::EObject_strategy = st.builds(
    facademapping::EObject,
)
facademapping::Mapping_strategy = st.builds(
    facademapping::Mapping,
)

@given(instance=facademapping::FacadeMappping_strategy)
@settings(max_examples=50)
def test_facademapping::facademappping_instantiation(instance):
    assert isinstance(instance, facademapping::FacadeMappping)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=facademapping::StereotypedMapping_strategy)
@settings(max_examples=50)
def test_facademapping::stereotypedmapping_instantiation(instance):
    assert isinstance(instance, facademapping::StereotypedMapping)

@given(instance=facademapping::StereotypedMapping_strategy)
def test_facademapping::stereotypedmapping_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=facademapping::StereotypedMapping_strategy)
def test_facademapping::stereotypedmapping_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=facademapping::EObject_strategy)
@settings(max_examples=50)
def test_facademapping::eobject_instantiation(instance):
    assert isinstance(instance, facademapping::EObject)

@given(instance=facademapping::Mapping_strategy)
@settings(max_examples=50)
def test_facademapping::mapping_instantiation(instance):
    assert isinstance(instance, facademapping::Mapping)
