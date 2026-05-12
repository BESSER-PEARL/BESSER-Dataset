import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metamodel_parameter,
    metamodel_Query,
    metamodel_Feature,
    Type,
    metamodel_Entity,
    metamodel_Datatype,
    metamodel_Type,
    metamodel_Model,
    Annotation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodel_parameter_is_not_abstract():
    assert not inspect.isabstract(metamodel_parameter)


def test_metamodel_parameter_constructor_exists():
    assert callable(metamodel_parameter.__init__)


def test_metamodel_parameter_constructor_args():
    sig = inspect.signature(metamodel_parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_parameter_has_name():
    assert hasattr(metamodel_parameter, "name")
    descriptor = None
    for klass in metamodel_parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_query_is_not_abstract():
    assert not inspect.isabstract(metamodel_Query)


def test_metamodel_query_constructor_exists():
    assert callable(metamodel_Query.__init__)


def test_metamodel_query_constructor_args():
    sig = inspect.signature(metamodel_Query.__init__)
    params = list(sig.parameters.keys())
    assert "methodName" in params, "Missing parameter 'methodName'"
    assert "queryString" in params, "Missing parameter 'queryString'"

def test_metamodel_query_has_methodName():
    assert hasattr(metamodel_Query, "methodName")
    descriptor = None
    for klass in metamodel_Query.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_query_has_queryString():
    assert hasattr(metamodel_Query, "queryString")
    descriptor = None
    for klass in metamodel_Query.__mro__:
        if "queryString" in klass.__dict__:
            descriptor = klass.__dict__["queryString"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_feature_is_not_abstract():
    assert not inspect.isabstract(metamodel_Feature)


def test_metamodel_feature_constructor_exists():
    assert callable(metamodel_Feature.__init__)


def test_metamodel_feature_constructor_args():
    sig = inspect.signature(metamodel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "mappedBy" in params, "Missing parameter 'mappedBy'"
    assert "name" in params, "Missing parameter 'name'"
    assert "annotation" in params, "Missing parameter 'annotation'"

def test_metamodel_feature_has_mappedBy():
    assert hasattr(metamodel_Feature, "mappedBy")
    descriptor = None
    for klass in metamodel_Feature.__mro__:
        if "mappedBy" in klass.__dict__:
            descriptor = klass.__dict__["mappedBy"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_feature_has_name():
    assert hasattr(metamodel_Feature, "name")
    descriptor = None
    for klass in metamodel_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_feature_has_annotation():
    assert hasattr(metamodel_Feature, "annotation")
    descriptor = None
    for klass in metamodel_Feature.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_entity_is_not_abstract():
    assert not inspect.isabstract(metamodel_Entity)


def test_metamodel_entity_constructor_exists():
    assert callable(metamodel_Entity.__init__)


def test_metamodel_entity_constructor_args():
    sig = inspect.signature(metamodel_Entity.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_datatype_is_not_abstract():
    assert not inspect.isabstract(metamodel_Datatype)


def test_metamodel_datatype_constructor_exists():
    assert callable(metamodel_Datatype.__init__)


def test_metamodel_datatype_constructor_args():
    sig = inspect.signature(metamodel_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_type_is_not_abstract():
    assert not inspect.isabstract(metamodel_Type)


def test_metamodel_type_constructor_exists():
    assert callable(metamodel_Type.__init__)


def test_metamodel_type_constructor_args():
    sig = inspect.signature(metamodel_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_type_has_name():
    assert hasattr(metamodel_Type, "name")
    descriptor = None
    for klass in metamodel_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_model_is_not_abstract():
    assert not inspect.isabstract(metamodel_Model)


def test_metamodel_model_constructor_exists():
    assert callable(metamodel_Model.__init__)


def test_metamodel_model_constructor_args():
    sig = inspect.signature(metamodel_Model.__init__)
    params = list(sig.parameters.keys())

def test_annotation_exists():
    # Check that the Enumeration exists
    assert Annotation is not None

def test_annotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Annotation]
    expected_literals = [
        "ManyToMany",
        "OneToMany",
        "None_",
        "Id",
        "OneToOne",
        "ManyToManyMapped",
        "ManyToOne",
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
metamodel_parameter_strategy = st.builds(
    metamodel_parameter,
    name=
        safe_text
)
metamodel_Query_strategy = st.builds(
    metamodel_Query,
    methodName=
        safe_text,
    queryString=
        safe_text
)
metamodel_Feature_strategy = st.builds(
    metamodel_Feature,
    mappedBy=
        safe_text,
    name=
        safe_text,
    annotation=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
metamodel_Entity_strategy = st.builds(
    metamodel_Entity,
)
metamodel_Datatype_strategy = st.builds(
    metamodel_Datatype,
)
metamodel_Type_strategy = st.builds(
    metamodel_Type,
    name=
        safe_text
)
metamodel_Model_strategy = st.builds(
    metamodel_Model,
)

@given(instance=metamodel_parameter_strategy)
@settings(max_examples=50)
def test_metamodel_parameter_instantiation(instance):
    assert isinstance(instance, metamodel_parameter)



@given(instance=metamodel_parameter_strategy)
def test_metamodel_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Query_strategy)
@settings(max_examples=50)
def test_metamodel_query_instantiation(instance):
    assert isinstance(instance, metamodel_Query)



@given(instance=metamodel_Query_strategy)
def test_metamodel_query_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original



@given(instance=metamodel_Query_strategy)
def test_metamodel_query_queryString_setter(instance):
    original = instance.queryString
    instance.queryString = original
    assert instance.queryString == original

@given(instance=metamodel_Feature_strategy)
@settings(max_examples=50)
def test_metamodel_feature_instantiation(instance):
    assert isinstance(instance, metamodel_Feature)



@given(instance=metamodel_Feature_strategy)
def test_metamodel_feature_mappedBy_setter(instance):
    original = instance.mappedBy
    instance.mappedBy = original
    assert instance.mappedBy == original



@given(instance=metamodel_Feature_strategy)
def test_metamodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metamodel_Feature_strategy)
def test_metamodel_feature_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=metamodel_Entity_strategy)
@settings(max_examples=50)
def test_metamodel_entity_instantiation(instance):
    assert isinstance(instance, metamodel_Entity)

@given(instance=metamodel_Datatype_strategy)
@settings(max_examples=50)
def test_metamodel_datatype_instantiation(instance):
    assert isinstance(instance, metamodel_Datatype)

@given(instance=metamodel_Type_strategy)
@settings(max_examples=50)
def test_metamodel_type_instantiation(instance):
    assert isinstance(instance, metamodel_Type)



@given(instance=metamodel_Type_strategy)
def test_metamodel_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Model_strategy)
@settings(max_examples=50)
def test_metamodel_model_instantiation(instance):
    assert isinstance(instance, metamodel_Model)
