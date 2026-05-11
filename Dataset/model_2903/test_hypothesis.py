import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    coral::Type,
    coral::EntityModel,
    coral::Feature,
    Type,
    coral::Entity,
    coral::DataType,
    coral::NamedElement,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_coral::type_is_not_abstract():
    assert not inspect.isabstract(coral::Type)


def test_coral::type_constructor_exists():
    assert callable(coral::Type.__init__)


def test_coral::type_constructor_args():
    sig = inspect.signature(coral::Type.__init__)
    params = list(sig.parameters.keys())



def test_coral::entitymodel_is_not_abstract():
    assert not inspect.isabstract(coral::EntityModel)


def test_coral::entitymodel_constructor_exists():
    assert callable(coral::EntityModel.__init__)


def test_coral::entitymodel_constructor_args():
    sig = inspect.signature(coral::EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_coral::feature_is_not_abstract():
    assert not inspect.isabstract(coral::Feature)


def test_coral::feature_constructor_exists():
    assert callable(coral::Feature.__init__)


def test_coral::feature_constructor_args():
    sig = inspect.signature(coral::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_coral::feature_has_kind():
    assert hasattr(coral::Feature, "kind")
    descriptor = None
    for klass in coral::Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_coral::entity_is_not_abstract():
    assert not inspect.isabstract(coral::Entity)


def test_coral::entity_constructor_exists():
    assert callable(coral::Entity.__init__)


def test_coral::entity_constructor_args():
    sig = inspect.signature(coral::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_coral::entity_has_abstract():
    assert hasattr(coral::Entity, "abstract")
    descriptor = None
    for klass in coral::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_coral::datatype_is_not_abstract():
    assert not inspect.isabstract(coral::DataType)


def test_coral::datatype_constructor_exists():
    assert callable(coral::DataType.__init__)


def test_coral::datatype_constructor_args():
    sig = inspect.signature(coral::DataType.__init__)
    params = list(sig.parameters.keys())



def test_coral::namedelement_is_not_abstract():
    assert not inspect.isabstract(coral::NamedElement)


def test_coral::namedelement_constructor_exists():
    assert callable(coral::NamedElement.__init__)


def test_coral::namedelement_constructor_args():
    sig = inspect.signature(coral::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_coral::namedelement_has_name():
    assert hasattr(coral::NamedElement, "name")
    descriptor = None
    for klass in coral::NamedElement.__mro__:
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
        "containment",
        "attribute",
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
NamedElement_strategy = st.builds(
    NamedElement,
)
coral::Type_strategy = st.builds(
    coral::Type,
)
coral::EntityModel_strategy = st.builds(
    coral::EntityModel,
)
coral::Feature_strategy = st.builds(
    coral::Feature,
    kind=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
coral::Entity_strategy = st.builds(
    coral::Entity,
    abstract=
        st.booleans()
)
coral::DataType_strategy = st.builds(
    coral::DataType,
)
coral::NamedElement_strategy = st.builds(
    coral::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=coral::Type_strategy)
@settings(max_examples=50)
def test_coral::type_instantiation(instance):
    assert isinstance(instance, coral::Type)

@given(instance=coral::EntityModel_strategy)
@settings(max_examples=50)
def test_coral::entitymodel_instantiation(instance):
    assert isinstance(instance, coral::EntityModel)

@given(instance=coral::Feature_strategy)
@settings(max_examples=50)
def test_coral::feature_instantiation(instance):
    assert isinstance(instance, coral::Feature)

@given(instance=coral::Feature_strategy)
def test_coral::feature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=coral::Feature_strategy)
def test_coral::feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=coral::Entity_strategy)
@settings(max_examples=50)
def test_coral::entity_instantiation(instance):
    assert isinstance(instance, coral::Entity)

@given(instance=coral::Entity_strategy)
def test_coral::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=coral::Entity_strategy)
def test_coral::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=coral::DataType_strategy)
@settings(max_examples=50)
def test_coral::datatype_instantiation(instance):
    assert isinstance(instance, coral::DataType)

@given(instance=coral::NamedElement_strategy)
@settings(max_examples=50)
def test_coral::namedelement_instantiation(instance):
    assert isinstance(instance, coral::NamedElement)

@given(instance=coral::NamedElement_strategy)
def test_coral::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coral::NamedElement_strategy)
def test_coral::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
