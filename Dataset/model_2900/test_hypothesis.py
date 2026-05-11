import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    forms::EntityModel,
    Type,
    forms::Entity,
    forms::DataType,
    NamedElement,
    forms::Feature,
    forms::Type,
    forms::NamedElement,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_forms::entitymodel_is_not_abstract():
    assert not inspect.isabstract(forms::EntityModel)


def test_forms::entitymodel_constructor_exists():
    assert callable(forms::EntityModel.__init__)


def test_forms::entitymodel_constructor_args():
    sig = inspect.signature(forms::EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_forms::entity_is_not_abstract():
    assert not inspect.isabstract(forms::Entity)


def test_forms::entity_constructor_exists():
    assert callable(forms::Entity.__init__)


def test_forms::entity_constructor_args():
    sig = inspect.signature(forms::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_forms::entity_has_abstract():
    assert hasattr(forms::Entity, "abstract")
    descriptor = None
    for klass in forms::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_forms::datatype_is_not_abstract():
    assert not inspect.isabstract(forms::DataType)


def test_forms::datatype_constructor_exists():
    assert callable(forms::DataType.__init__)


def test_forms::datatype_constructor_args():
    sig = inspect.signature(forms::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_forms::feature_is_not_abstract():
    assert not inspect.isabstract(forms::Feature)


def test_forms::feature_constructor_exists():
    assert callable(forms::Feature.__init__)


def test_forms::feature_constructor_args():
    sig = inspect.signature(forms::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_forms::feature_has_kind():
    assert hasattr(forms::Feature, "kind")
    descriptor = None
    for klass in forms::Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_forms::type_is_not_abstract():
    assert not inspect.isabstract(forms::Type)


def test_forms::type_constructor_exists():
    assert callable(forms::Type.__init__)


def test_forms::type_constructor_args():
    sig = inspect.signature(forms::Type.__init__)
    params = list(sig.parameters.keys())



def test_forms::namedelement_is_not_abstract():
    assert not inspect.isabstract(forms::NamedElement)


def test_forms::namedelement_constructor_exists():
    assert callable(forms::NamedElement.__init__)


def test_forms::namedelement_constructor_args():
    sig = inspect.signature(forms::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_forms::namedelement_has_name():
    assert hasattr(forms::NamedElement, "name")
    descriptor = None
    for klass in forms::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featurekind_exists():
    # Check that the Enumeration exists
    assert FeatureKind is not None

def test_featurekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureKind]
    expected_literals = [
        "attribute",
        "containment",
        "reference",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureKind"


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
forms::EntityModel_strategy = st.builds(
    forms::EntityModel,
)
Type_strategy = st.builds(
    Type,
)
forms::Entity_strategy = st.builds(
    forms::Entity,
    abstract=
        st.booleans()
)
forms::DataType_strategy = st.builds(
    forms::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
forms::Feature_strategy = st.builds(
    forms::Feature,
    kind=
        safe_text
)
forms::Type_strategy = st.builds(
    forms::Type,
)
forms::NamedElement_strategy = st.builds(
    forms::NamedElement,
    name=
        safe_text
)

@given(instance=forms::EntityModel_strategy)
@settings(max_examples=50)
def test_forms::entitymodel_instantiation(instance):
    assert isinstance(instance, forms::EntityModel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=forms::Entity_strategy)
@settings(max_examples=50)
def test_forms::entity_instantiation(instance):
    assert isinstance(instance, forms::Entity)

@given(instance=forms::Entity_strategy)
def test_forms::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=forms::Entity_strategy)
def test_forms::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=forms::DataType_strategy)
@settings(max_examples=50)
def test_forms::datatype_instantiation(instance):
    assert isinstance(instance, forms::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=forms::Feature_strategy)
@settings(max_examples=50)
def test_forms::feature_instantiation(instance):
    assert isinstance(instance, forms::Feature)

@given(instance=forms::Feature_strategy)
def test_forms::feature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=forms::Feature_strategy)
def test_forms::feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=forms::Type_strategy)
@settings(max_examples=50)
def test_forms::type_instantiation(instance):
    assert isinstance(instance, forms::Type)

@given(instance=forms::NamedElement_strategy)
@settings(max_examples=50)
def test_forms::namedelement_instantiation(instance):
    assert isinstance(instance, forms::NamedElement)

@given(instance=forms::NamedElement_strategy)
def test_forms::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=forms::NamedElement_strategy)
def test_forms::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
