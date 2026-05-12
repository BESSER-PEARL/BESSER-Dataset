import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    namespace_EStringToStringMapEntry,
    namespace_XMLNamespaceDocumentRoot,
    SpaceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namespace_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(namespace_EStringToStringMapEntry)


def test_namespace_estringtostringmapentry_constructor_exists():
    assert callable(namespace_EStringToStringMapEntry.__init__)


def test_namespace_estringtostringmapentry_constructor_args():
    sig = inspect.signature(namespace_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_namespace_xmlnamespacedocumentroot_is_not_abstract():
    assert not inspect.isabstract(namespace_XMLNamespaceDocumentRoot)


def test_namespace_xmlnamespacedocumentroot_constructor_exists():
    assert callable(namespace_XMLNamespaceDocumentRoot.__init__)


def test_namespace_xmlnamespacedocumentroot_constructor_args():
    sig = inspect.signature(namespace_XMLNamespaceDocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "base" in params, "Missing parameter 'base'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "space" in params, "Missing parameter 'space'"

def test_namespace_xmlnamespacedocumentroot_has_base():
    assert hasattr(namespace_XMLNamespaceDocumentRoot, "base")
    descriptor = None
    for klass in namespace_XMLNamespaceDocumentRoot.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)

def test_namespace_xmlnamespacedocumentroot_has_id():
    assert hasattr(namespace_XMLNamespaceDocumentRoot, "id")
    descriptor = None
    for klass in namespace_XMLNamespaceDocumentRoot.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_namespace_xmlnamespacedocumentroot_has_mixed():
    assert hasattr(namespace_XMLNamespaceDocumentRoot, "mixed")
    descriptor = None
    for klass in namespace_XMLNamespaceDocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_namespace_xmlnamespacedocumentroot_has_lang():
    assert hasattr(namespace_XMLNamespaceDocumentRoot, "lang")
    descriptor = None
    for klass in namespace_XMLNamespaceDocumentRoot.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_namespace_xmlnamespacedocumentroot_has_space():
    assert hasattr(namespace_XMLNamespaceDocumentRoot, "space")
    descriptor = None
    for klass in namespace_XMLNamespaceDocumentRoot.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_spacetype_exists():
    # Check that the Enumeration exists
    assert SpaceType is not None

def test_spacetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpaceType]
    expected_literals = [
        "preserve",
        "default",
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
namespace_EStringToStringMapEntry_strategy = st.builds(
    namespace_EStringToStringMapEntry,
)
namespace_XMLNamespaceDocumentRoot_strategy = st.builds(
    namespace_XMLNamespaceDocumentRoot,
    base=
        safe_text,
    id=
        safe_text,
    mixed=
        safe_text,
    lang=
        safe_text,
    space=
        safe_text
)

@given(instance=namespace_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_namespace_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, namespace_EStringToStringMapEntry)

@given(instance=namespace_XMLNamespaceDocumentRoot_strategy)
@settings(max_examples=50)
def test_namespace_xmlnamespacedocumentroot_instantiation(instance):
    assert isinstance(instance, namespace_XMLNamespaceDocumentRoot)



@given(instance=namespace_XMLNamespaceDocumentRoot_strategy)
def test_namespace_xmlnamespacedocumentroot_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original



@given(instance=namespace_XMLNamespaceDocumentRoot_strategy)
def test_namespace_xmlnamespacedocumentroot_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=namespace_XMLNamespaceDocumentRoot_strategy)
def test_namespace_xmlnamespacedocumentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=namespace_XMLNamespaceDocumentRoot_strategy)
def test_namespace_xmlnamespacedocumentroot_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=namespace_XMLNamespaceDocumentRoot_strategy)
def test_namespace_xmlnamespacedocumentroot_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original
