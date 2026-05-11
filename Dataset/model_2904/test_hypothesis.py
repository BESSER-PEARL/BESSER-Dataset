import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    hbmxml::Entity,
    hbmxml::DataType,
    NamedElement,
    hbmxml::Feature,
    hbmxml::Type,
    hbmxml::NamedElement,
    hbmxml::EntityModel,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hbmxml::entity_is_not_abstract():
    assert not inspect.isabstract(hbmxml::Entity)


def test_hbmxml::entity_constructor_exists():
    assert callable(hbmxml::Entity.__init__)


def test_hbmxml::entity_constructor_args():
    sig = inspect.signature(hbmxml::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_hbmxml::entity_has_abstract():
    assert hasattr(hbmxml::Entity, "abstract")
    descriptor = None
    for klass in hbmxml::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_hbmxml::datatype_is_not_abstract():
    assert not inspect.isabstract(hbmxml::DataType)


def test_hbmxml::datatype_constructor_exists():
    assert callable(hbmxml::DataType.__init__)


def test_hbmxml::datatype_constructor_args():
    sig = inspect.signature(hbmxml::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hbmxml::feature_is_not_abstract():
    assert not inspect.isabstract(hbmxml::Feature)


def test_hbmxml::feature_constructor_exists():
    assert callable(hbmxml::Feature.__init__)


def test_hbmxml::feature_constructor_args():
    sig = inspect.signature(hbmxml::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_hbmxml::feature_has_kind():
    assert hasattr(hbmxml::Feature, "kind")
    descriptor = None
    for klass in hbmxml::Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_hbmxml::type_is_not_abstract():
    assert not inspect.isabstract(hbmxml::Type)


def test_hbmxml::type_constructor_exists():
    assert callable(hbmxml::Type.__init__)


def test_hbmxml::type_constructor_args():
    sig = inspect.signature(hbmxml::Type.__init__)
    params = list(sig.parameters.keys())



def test_hbmxml::namedelement_is_not_abstract():
    assert not inspect.isabstract(hbmxml::NamedElement)


def test_hbmxml::namedelement_constructor_exists():
    assert callable(hbmxml::NamedElement.__init__)


def test_hbmxml::namedelement_constructor_args():
    sig = inspect.signature(hbmxml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hbmxml::namedelement_has_name():
    assert hasattr(hbmxml::NamedElement, "name")
    descriptor = None
    for klass in hbmxml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hbmxml::entitymodel_is_not_abstract():
    assert not inspect.isabstract(hbmxml::EntityModel)


def test_hbmxml::entitymodel_constructor_exists():
    assert callable(hbmxml::EntityModel.__init__)


def test_hbmxml::entitymodel_constructor_args():
    sig = inspect.signature(hbmxml::EntityModel.__init__)
    params = list(sig.parameters.keys())

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
Type_strategy = st.builds(
    Type,
)
hbmxml::Entity_strategy = st.builds(
    hbmxml::Entity,
    abstract=
        st.booleans()
)
hbmxml::DataType_strategy = st.builds(
    hbmxml::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hbmxml::Feature_strategy = st.builds(
    hbmxml::Feature,
    kind=
        safe_text
)
hbmxml::Type_strategy = st.builds(
    hbmxml::Type,
)
hbmxml::NamedElement_strategy = st.builds(
    hbmxml::NamedElement,
    name=
        safe_text
)
hbmxml::EntityModel_strategy = st.builds(
    hbmxml::EntityModel,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=hbmxml::Entity_strategy)
@settings(max_examples=50)
def test_hbmxml::entity_instantiation(instance):
    assert isinstance(instance, hbmxml::Entity)

@given(instance=hbmxml::Entity_strategy)
def test_hbmxml::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=hbmxml::Entity_strategy)
def test_hbmxml::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=hbmxml::DataType_strategy)
@settings(max_examples=50)
def test_hbmxml::datatype_instantiation(instance):
    assert isinstance(instance, hbmxml::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hbmxml::Feature_strategy)
@settings(max_examples=50)
def test_hbmxml::feature_instantiation(instance):
    assert isinstance(instance, hbmxml::Feature)

@given(instance=hbmxml::Feature_strategy)
def test_hbmxml::feature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=hbmxml::Feature_strategy)
def test_hbmxml::feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=hbmxml::Type_strategy)
@settings(max_examples=50)
def test_hbmxml::type_instantiation(instance):
    assert isinstance(instance, hbmxml::Type)

@given(instance=hbmxml::NamedElement_strategy)
@settings(max_examples=50)
def test_hbmxml::namedelement_instantiation(instance):
    assert isinstance(instance, hbmxml::NamedElement)

@given(instance=hbmxml::NamedElement_strategy)
def test_hbmxml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hbmxml::NamedElement_strategy)
def test_hbmxml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hbmxml::EntityModel_strategy)
@settings(max_examples=50)
def test_hbmxml::entitymodel_instantiation(instance):
    assert isinstance(instance, hbmxml::EntityModel)
