import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ube::EntityModel,
    Type,
    ube::Entity,
    ube::DataType,
    NamedElement,
    ube::Feature,
    ube::Type,
    ube::NamedElement,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ube::entitymodel_is_not_abstract():
    assert not inspect.isabstract(ube::EntityModel)


def test_ube::entitymodel_constructor_exists():
    assert callable(ube::EntityModel.__init__)


def test_ube::entitymodel_constructor_args():
    sig = inspect.signature(ube::EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ube::entity_is_not_abstract():
    assert not inspect.isabstract(ube::Entity)


def test_ube::entity_constructor_exists():
    assert callable(ube::Entity.__init__)


def test_ube::entity_constructor_args():
    sig = inspect.signature(ube::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ube::entity_has_abstract():
    assert hasattr(ube::Entity, "abstract")
    descriptor = None
    for klass in ube::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_ube::datatype_is_not_abstract():
    assert not inspect.isabstract(ube::DataType)


def test_ube::datatype_constructor_exists():
    assert callable(ube::DataType.__init__)


def test_ube::datatype_constructor_args():
    sig = inspect.signature(ube::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ube::feature_is_not_abstract():
    assert not inspect.isabstract(ube::Feature)


def test_ube::feature_constructor_exists():
    assert callable(ube::Feature.__init__)


def test_ube::feature_constructor_args():
    sig = inspect.signature(ube::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ube::feature_has_kind():
    assert hasattr(ube::Feature, "kind")
    descriptor = None
    for klass in ube::Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ube::type_is_not_abstract():
    assert not inspect.isabstract(ube::Type)


def test_ube::type_constructor_exists():
    assert callable(ube::Type.__init__)


def test_ube::type_constructor_args():
    sig = inspect.signature(ube::Type.__init__)
    params = list(sig.parameters.keys())



def test_ube::namedelement_is_not_abstract():
    assert not inspect.isabstract(ube::NamedElement)


def test_ube::namedelement_constructor_exists():
    assert callable(ube::NamedElement.__init__)


def test_ube::namedelement_constructor_args():
    sig = inspect.signature(ube::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ube::namedelement_has_name():
    assert hasattr(ube::NamedElement, "name")
    descriptor = None
    for klass in ube::NamedElement.__mro__:
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
        "reference",
        "attribute",
        "containment",
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
ube::EntityModel_strategy = st.builds(
    ube::EntityModel,
)
Type_strategy = st.builds(
    Type,
)
ube::Entity_strategy = st.builds(
    ube::Entity,
    abstract=
        st.booleans()
)
ube::DataType_strategy = st.builds(
    ube::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ube::Feature_strategy = st.builds(
    ube::Feature,
    kind=
        safe_text
)
ube::Type_strategy = st.builds(
    ube::Type,
)
ube::NamedElement_strategy = st.builds(
    ube::NamedElement,
    name=
        safe_text
)

@given(instance=ube::EntityModel_strategy)
@settings(max_examples=50)
def test_ube::entitymodel_instantiation(instance):
    assert isinstance(instance, ube::EntityModel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ube::Entity_strategy)
@settings(max_examples=50)
def test_ube::entity_instantiation(instance):
    assert isinstance(instance, ube::Entity)

@given(instance=ube::Entity_strategy)
def test_ube::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=ube::Entity_strategy)
def test_ube::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ube::DataType_strategy)
@settings(max_examples=50)
def test_ube::datatype_instantiation(instance):
    assert isinstance(instance, ube::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ube::Feature_strategy)
@settings(max_examples=50)
def test_ube::feature_instantiation(instance):
    assert isinstance(instance, ube::Feature)

@given(instance=ube::Feature_strategy)
def test_ube::feature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ube::Feature_strategy)
def test_ube::feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ube::Type_strategy)
@settings(max_examples=50)
def test_ube::type_instantiation(instance):
    assert isinstance(instance, ube::Type)

@given(instance=ube::NamedElement_strategy)
@settings(max_examples=50)
def test_ube::namedelement_instantiation(instance):
    assert isinstance(instance, ube::NamedElement)

@given(instance=ube::NamedElement_strategy)
def test_ube::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ube::NamedElement_strategy)
def test_ube::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
