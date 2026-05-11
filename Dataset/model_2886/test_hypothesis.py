import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metamodel::parameter,
    metamodel::Query,
    metamodel::Feature,
    Type,
    metamodel::Entity,
    metamodel::Datatype,
    metamodel::Type,
    metamodel::Model,
    Annotation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodel::parameter_is_not_abstract():
    assert not inspect.isabstract(metamodel::parameter)


def test_metamodel::parameter_constructor_exists():
    assert callable(metamodel::parameter.__init__)


def test_metamodel::parameter_constructor_args():
    sig = inspect.signature(metamodel::parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::parameter_has_name():
    assert hasattr(metamodel::parameter, "name")
    descriptor = None
    for klass in metamodel::parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::query_is_not_abstract():
    assert not inspect.isabstract(metamodel::Query)


def test_metamodel::query_constructor_exists():
    assert callable(metamodel::Query.__init__)


def test_metamodel::query_constructor_args():
    sig = inspect.signature(metamodel::Query.__init__)
    params = list(sig.parameters.keys())
    assert "queryString" in params, "Missing parameter 'queryString'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_metamodel::query_has_queryString():
    assert hasattr(metamodel::Query, "queryString")
    descriptor = None
    for klass in metamodel::Query.__mro__:
        if "queryString" in klass.__dict__:
            descriptor = klass.__dict__["queryString"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::query_has_methodName():
    assert hasattr(metamodel::Query, "methodName")
    descriptor = None
    for klass in metamodel::Query.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::feature_is_not_abstract():
    assert not inspect.isabstract(metamodel::Feature)


def test_metamodel::feature_constructor_exists():
    assert callable(metamodel::Feature.__init__)


def test_metamodel::feature_constructor_args():
    sig = inspect.signature(metamodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "annotation" in params, "Missing parameter 'annotation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mappedBy" in params, "Missing parameter 'mappedBy'"

def test_metamodel::feature_has_annotation():
    assert hasattr(metamodel::Feature, "annotation")
    descriptor = None
    for klass in metamodel::Feature.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::feature_has_name():
    assert hasattr(metamodel::Feature, "name")
    descriptor = None
    for klass in metamodel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::feature_has_mappedBy():
    assert hasattr(metamodel::Feature, "mappedBy")
    descriptor = None
    for klass in metamodel::Feature.__mro__:
        if "mappedBy" in klass.__dict__:
            descriptor = klass.__dict__["mappedBy"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::entity_is_not_abstract():
    assert not inspect.isabstract(metamodel::Entity)


def test_metamodel::entity_constructor_exists():
    assert callable(metamodel::Entity.__init__)


def test_metamodel::entity_constructor_args():
    sig = inspect.signature(metamodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::datatype_is_not_abstract():
    assert not inspect.isabstract(metamodel::Datatype)


def test_metamodel::datatype_constructor_exists():
    assert callable(metamodel::Datatype.__init__)


def test_metamodel::datatype_constructor_args():
    sig = inspect.signature(metamodel::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::type_is_not_abstract():
    assert not inspect.isabstract(metamodel::Type)


def test_metamodel::type_constructor_exists():
    assert callable(metamodel::Type.__init__)


def test_metamodel::type_constructor_args():
    sig = inspect.signature(metamodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::type_has_name():
    assert hasattr(metamodel::Type, "name")
    descriptor = None
    for klass in metamodel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::model_is_not_abstract():
    assert not inspect.isabstract(metamodel::Model)


def test_metamodel::model_constructor_exists():
    assert callable(metamodel::Model.__init__)


def test_metamodel::model_constructor_args():
    sig = inspect.signature(metamodel::Model.__init__)
    params = list(sig.parameters.keys())

def test_annotation_exists():
    # Check that the Enumeration exists
    assert Annotation is not None

def test_annotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Annotation]
    expected_literals = [
        "OneToOne",
        "OneToMany",
        "Id",
        "ManyToManyMapped",
        "None_",
        "ManyToOne",
        "ManyToMany",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Annotation"


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
metamodel::parameter_strategy = st.builds(
    metamodel::parameter,
    name=
        safe_text
)
metamodel::Query_strategy = st.builds(
    metamodel::Query,
    queryString=
        safe_text,
    methodName=
        safe_text
)
metamodel::Feature_strategy = st.builds(
    metamodel::Feature,
    annotation=
        safe_text,
    name=
        safe_text,
    mappedBy=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
metamodel::Entity_strategy = st.builds(
    metamodel::Entity,
)
metamodel::Datatype_strategy = st.builds(
    metamodel::Datatype,
)
metamodel::Type_strategy = st.builds(
    metamodel::Type,
    name=
        safe_text
)
metamodel::Model_strategy = st.builds(
    metamodel::Model,
)

@given(instance=metamodel::parameter_strategy)
@settings(max_examples=50)
def test_metamodel::parameter_instantiation(instance):
    assert isinstance(instance, metamodel::parameter)

@given(instance=metamodel::parameter_strategy)
def test_metamodel::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::parameter_strategy)
def test_metamodel::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Query_strategy)
@settings(max_examples=50)
def test_metamodel::query_instantiation(instance):
    assert isinstance(instance, metamodel::Query)

@given(instance=metamodel::Query_strategy)
def test_metamodel::query_queryString_type(instance):
    assert isinstance(instance.queryString, str)


@given(instance=metamodel::Query_strategy)
def test_metamodel::query_queryString_setter(instance):
    original = instance.queryString
    instance.queryString = original
    assert instance.queryString == original

@given(instance=metamodel::Query_strategy)
def test_metamodel::query_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=metamodel::Query_strategy)
def test_metamodel::query_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=metamodel::Feature_strategy)
@settings(max_examples=50)
def test_metamodel::feature_instantiation(instance):
    assert isinstance(instance, metamodel::Feature)

@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_annotation_type(instance):
    assert isinstance(instance.annotation, str)


@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original

@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_mappedBy_type(instance):
    assert isinstance(instance.mappedBy, str)


@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_mappedBy_setter(instance):
    original = instance.mappedBy
    instance.mappedBy = original
    assert instance.mappedBy == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=metamodel::Entity_strategy)
@settings(max_examples=50)
def test_metamodel::entity_instantiation(instance):
    assert isinstance(instance, metamodel::Entity)

@given(instance=metamodel::Datatype_strategy)
@settings(max_examples=50)
def test_metamodel::datatype_instantiation(instance):
    assert isinstance(instance, metamodel::Datatype)

@given(instance=metamodel::Type_strategy)
@settings(max_examples=50)
def test_metamodel::type_instantiation(instance):
    assert isinstance(instance, metamodel::Type)

@given(instance=metamodel::Type_strategy)
def test_metamodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Type_strategy)
def test_metamodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Model_strategy)
@settings(max_examples=50)
def test_metamodel::model_instantiation(instance):
    assert isinstance(instance, metamodel::Model)
