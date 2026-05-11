import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    namespace::EStringToStringMapEntry,
    namespace::XMLNamespaceDocumentRoot,
    SpaceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namespace::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(namespace::EStringToStringMapEntry)


def test_namespace::estringtostringmapentry_constructor_exists():
    assert callable(namespace::EStringToStringMapEntry.__init__)


def test_namespace::estringtostringmapentry_constructor_args():
    sig = inspect.signature(namespace::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_namespace::xmlnamespacedocumentroot_is_not_abstract():
    assert not inspect.isabstract(namespace::XMLNamespaceDocumentRoot)


def test_namespace::xmlnamespacedocumentroot_constructor_exists():
    assert callable(namespace::XMLNamespaceDocumentRoot.__init__)


def test_namespace::xmlnamespacedocumentroot_constructor_args():
    sig = inspect.signature(namespace::XMLNamespaceDocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "base" in params, "Missing parameter 'base'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "id" in params, "Missing parameter 'id'"

def test_namespace::xmlnamespacedocumentroot_has_space():
    assert hasattr(namespace::XMLNamespaceDocumentRoot, "space")
    descriptor = None
    for klass in namespace::XMLNamespaceDocumentRoot.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_namespace::xmlnamespacedocumentroot_has_mixed():
    assert hasattr(namespace::XMLNamespaceDocumentRoot, "mixed")
    descriptor = None
    for klass in namespace::XMLNamespaceDocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_namespace::xmlnamespacedocumentroot_has_base():
    assert hasattr(namespace::XMLNamespaceDocumentRoot, "base")
    descriptor = None
    for klass in namespace::XMLNamespaceDocumentRoot.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)

def test_namespace::xmlnamespacedocumentroot_has_lang():
    assert hasattr(namespace::XMLNamespaceDocumentRoot, "lang")
    descriptor = None
    for klass in namespace::XMLNamespaceDocumentRoot.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_namespace::xmlnamespacedocumentroot_has_id():
    assert hasattr(namespace::XMLNamespaceDocumentRoot, "id")
    descriptor = None
    for klass in namespace::XMLNamespaceDocumentRoot.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_spacetype_exists():
    # Check that the Enumeration exists
    assert SpaceType is not None

def test_spacetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpaceType]
    expected_literals = [
        "default",
        "preserve",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpaceType"


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
namespace::EStringToStringMapEntry_strategy = st.builds(
    namespace::EStringToStringMapEntry,
)
namespace::XMLNamespaceDocumentRoot_strategy = st.builds(
    namespace::XMLNamespaceDocumentRoot,
    space=
        safe_text,
    mixed=
        safe_text,
    base=
        safe_text,
    lang=
        safe_text,
    id=
        safe_text
)

@given(instance=namespace::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_namespace::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, namespace::EStringToStringMapEntry)

@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
@settings(max_examples=50)
def test_namespace::xmlnamespacedocumentroot_instantiation(instance):
    assert isinstance(instance, namespace::XMLNamespaceDocumentRoot)

@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_base_type(instance):
    assert isinstance(instance.base, str)


@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original

@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=namespace::XMLNamespaceDocumentRoot_strategy)
def test_namespace::xmlnamespacedocumentroot_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
