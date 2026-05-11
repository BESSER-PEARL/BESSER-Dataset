import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDSL::EntityModel,
    myDSL::NamedElement,
    Type,
    myDSL::Entity,
    myDSL::DataType,
    NamedElement,
    myDSL::Feature,
    myDSL::Type,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::entitymodel_is_not_abstract():
    assert not inspect.isabstract(myDSL::EntityModel)


def test_mydsl::entitymodel_constructor_exists():
    assert callable(myDSL::EntityModel.__init__)


def test_mydsl::entitymodel_constructor_args():
    sig = inspect.signature(myDSL::EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::namedelement_is_not_abstract():
    assert not inspect.isabstract(myDSL::NamedElement)


def test_mydsl::namedelement_constructor_exists():
    assert callable(myDSL::NamedElement.__init__)


def test_mydsl::namedelement_constructor_args():
    sig = inspect.signature(myDSL::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::namedelement_has_name():
    assert hasattr(myDSL::NamedElement, "name")
    descriptor = None
    for klass in myDSL::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDSL::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDSL::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDSL::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_mydsl::entity_has_abstract():
    assert hasattr(myDSL::Entity, "abstract")
    descriptor = None
    for klass in myDSL::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::datatype_is_not_abstract():
    assert not inspect.isabstract(myDSL::DataType)


def test_mydsl::datatype_constructor_exists():
    assert callable(myDSL::DataType.__init__)


def test_mydsl::datatype_constructor_args():
    sig = inspect.signature(myDSL::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::feature_is_not_abstract():
    assert not inspect.isabstract(myDSL::Feature)


def test_mydsl::feature_constructor_exists():
    assert callable(myDSL::Feature.__init__)


def test_mydsl::feature_constructor_args():
    sig = inspect.signature(myDSL::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_mydsl::feature_has_kind():
    assert hasattr(myDSL::Feature, "kind")
    descriptor = None
    for klass in myDSL::Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDSL::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDSL::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDSL::Type.__init__)
    params = list(sig.parameters.keys())

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
myDSL::EntityModel_strategy = st.builds(
    myDSL::EntityModel,
)
myDSL::NamedElement_strategy = st.builds(
    myDSL::NamedElement,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDSL::Entity_strategy = st.builds(
    myDSL::Entity,
    abstract=
        st.booleans()
)
myDSL::DataType_strategy = st.builds(
    myDSL::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
myDSL::Feature_strategy = st.builds(
    myDSL::Feature,
    kind=
        safe_text
)
myDSL::Type_strategy = st.builds(
    myDSL::Type,
)

@given(instance=myDSL::EntityModel_strategy)
@settings(max_examples=50)
def test_mydsl::entitymodel_instantiation(instance):
    assert isinstance(instance, myDSL::EntityModel)

@given(instance=myDSL::NamedElement_strategy)
@settings(max_examples=50)
def test_mydsl::namedelement_instantiation(instance):
    assert isinstance(instance, myDSL::NamedElement)

@given(instance=myDSL::NamedElement_strategy)
def test_mydsl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDSL::NamedElement_strategy)
def test_mydsl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDSL::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDSL::Entity)

@given(instance=myDSL::Entity_strategy)
def test_mydsl::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=myDSL::Entity_strategy)
def test_mydsl::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=myDSL::DataType_strategy)
@settings(max_examples=50)
def test_mydsl::datatype_instantiation(instance):
    assert isinstance(instance, myDSL::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=myDSL::Feature_strategy)
@settings(max_examples=50)
def test_mydsl::feature_instantiation(instance):
    assert isinstance(instance, myDSL::Feature)

@given(instance=myDSL::Feature_strategy)
def test_mydsl::feature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=myDSL::Feature_strategy)
def test_mydsl::feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=myDSL::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDSL::Type)
