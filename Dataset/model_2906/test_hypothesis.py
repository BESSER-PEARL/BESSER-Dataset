import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bombXML::NamedElement,
    bombXML::EntityModel,
    Type,
    bombXML::Entity,
    bombXML::DataType,
    NamedElement,
    bombXML::Type,
    bombXML::Feature,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bombxml::namedelement_is_not_abstract():
    assert not inspect.isabstract(bombXML::NamedElement)


def test_bombxml::namedelement_constructor_exists():
    assert callable(bombXML::NamedElement.__init__)


def test_bombxml::namedelement_constructor_args():
    sig = inspect.signature(bombXML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bombxml::namedelement_has_name():
    assert hasattr(bombXML::NamedElement, "name")
    descriptor = None
    for klass in bombXML::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bombxml::entitymodel_is_not_abstract():
    assert not inspect.isabstract(bombXML::EntityModel)


def test_bombxml::entitymodel_constructor_exists():
    assert callable(bombXML::EntityModel.__init__)


def test_bombxml::entitymodel_constructor_args():
    sig = inspect.signature(bombXML::EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_bombxml::entity_is_not_abstract():
    assert not inspect.isabstract(bombXML::Entity)


def test_bombxml::entity_constructor_exists():
    assert callable(bombXML::Entity.__init__)


def test_bombxml::entity_constructor_args():
    sig = inspect.signature(bombXML::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_bombxml::entity_has_abstract():
    assert hasattr(bombXML::Entity, "abstract")
    descriptor = None
    for klass in bombXML::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_bombxml::datatype_is_not_abstract():
    assert not inspect.isabstract(bombXML::DataType)


def test_bombxml::datatype_constructor_exists():
    assert callable(bombXML::DataType.__init__)


def test_bombxml::datatype_constructor_args():
    sig = inspect.signature(bombXML::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_bombxml::type_is_not_abstract():
    assert not inspect.isabstract(bombXML::Type)


def test_bombxml::type_constructor_exists():
    assert callable(bombXML::Type.__init__)


def test_bombxml::type_constructor_args():
    sig = inspect.signature(bombXML::Type.__init__)
    params = list(sig.parameters.keys())



def test_bombxml::feature_is_not_abstract():
    assert not inspect.isabstract(bombXML::Feature)


def test_bombxml::feature_constructor_exists():
    assert callable(bombXML::Feature.__init__)


def test_bombxml::feature_constructor_args():
    sig = inspect.signature(bombXML::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_bombxml::feature_has_kind():
    assert hasattr(bombXML::Feature, "kind")
    descriptor = None
    for klass in bombXML::Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
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
bombXML::NamedElement_strategy = st.builds(
    bombXML::NamedElement,
    name=
        safe_text
)
bombXML::EntityModel_strategy = st.builds(
    bombXML::EntityModel,
)
Type_strategy = st.builds(
    Type,
)
bombXML::Entity_strategy = st.builds(
    bombXML::Entity,
    abstract=
        st.booleans()
)
bombXML::DataType_strategy = st.builds(
    bombXML::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
bombXML::Type_strategy = st.builds(
    bombXML::Type,
)
bombXML::Feature_strategy = st.builds(
    bombXML::Feature,
    kind=
        safe_text
)

@given(instance=bombXML::NamedElement_strategy)
@settings(max_examples=50)
def test_bombxml::namedelement_instantiation(instance):
    assert isinstance(instance, bombXML::NamedElement)

@given(instance=bombXML::NamedElement_strategy)
def test_bombxml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bombXML::NamedElement_strategy)
def test_bombxml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bombXML::EntityModel_strategy)
@settings(max_examples=50)
def test_bombxml::entitymodel_instantiation(instance):
    assert isinstance(instance, bombXML::EntityModel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=bombXML::Entity_strategy)
@settings(max_examples=50)
def test_bombxml::entity_instantiation(instance):
    assert isinstance(instance, bombXML::Entity)

@given(instance=bombXML::Entity_strategy)
def test_bombxml::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=bombXML::Entity_strategy)
def test_bombxml::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=bombXML::DataType_strategy)
@settings(max_examples=50)
def test_bombxml::datatype_instantiation(instance):
    assert isinstance(instance, bombXML::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=bombXML::Type_strategy)
@settings(max_examples=50)
def test_bombxml::type_instantiation(instance):
    assert isinstance(instance, bombXML::Type)

@given(instance=bombXML::Feature_strategy)
@settings(max_examples=50)
def test_bombxml::feature_instantiation(instance):
    assert isinstance(instance, bombXML::Feature)

@given(instance=bombXML::Feature_strategy)
def test_bombxml::feature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=bombXML::Feature_strategy)
def test_bombxml::feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
