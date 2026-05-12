import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sqlview::Right,
    sqlview::Left,
    sqlview::Comparison,
    sqlview::EclExpression,
    sqlview::EObject,
    sqlview::Join,
    sqlview::Attribute,
    sqlview::Class,
    sqlview::Relation,
    sqlview::JoinRight,
    sqlview::JoinLeft,
    sqlview::Condition,
    sqlview::From,
    sqlview::Select,
    sqlview::MetamodelName,
    sqlview::SelectAttribute,
    sqlview::Expression,
    sqlview::Metamodel,
    sqlview::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sqlview::right_is_not_abstract():
    assert not inspect.isabstract(sqlview::Right)


def test_sqlview::right_constructor_exists():
    assert callable(sqlview::Right.__init__)


def test_sqlview::right_constructor_args():
    sig = inspect.signature(sqlview::Right.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqlview::right_has_value():
    assert hasattr(sqlview::Right, "value")
    descriptor = None
    for klass in sqlview::Right.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::left_is_not_abstract():
    assert not inspect.isabstract(sqlview::Left)


def test_sqlview::left_constructor_exists():
    assert callable(sqlview::Left.__init__)


def test_sqlview::left_constructor_args():
    sig = inspect.signature(sqlview::Left.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::comparison_is_not_abstract():
    assert not inspect.isabstract(sqlview::Comparison)


def test_sqlview::comparison_constructor_exists():
    assert callable(sqlview::Comparison.__init__)


def test_sqlview::comparison_constructor_args():
    sig = inspect.signature(sqlview::Comparison.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::eclexpression_is_not_abstract():
    assert not inspect.isabstract(sqlview::EclExpression)


def test_sqlview::eclexpression_constructor_exists():
    assert callable(sqlview::EclExpression.__init__)


def test_sqlview::eclexpression_constructor_args():
    sig = inspect.signature(sqlview::EclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqlview::eclexpression_has_value():
    assert hasattr(sqlview::EclExpression, "value")
    descriptor = None
    for klass in sqlview::EclExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::eobject_is_not_abstract():
    assert not inspect.isabstract(sqlview::EObject)


def test_sqlview::eobject_constructor_exists():
    assert callable(sqlview::EObject.__init__)


def test_sqlview::eobject_constructor_args():
    sig = inspect.signature(sqlview::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::join_is_not_abstract():
    assert not inspect.isabstract(sqlview::Join)


def test_sqlview::join_constructor_exists():
    assert callable(sqlview::Join.__init__)


def test_sqlview::join_constructor_args():
    sig = inspect.signature(sqlview::Join.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::attribute_is_not_abstract():
    assert not inspect.isabstract(sqlview::Attribute)


def test_sqlview::attribute_constructor_exists():
    assert callable(sqlview::Attribute.__init__)


def test_sqlview::attribute_constructor_args():
    sig = inspect.signature(sqlview::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlview::attribute_has_name():
    assert hasattr(sqlview::Attribute, "name")
    descriptor = None
    for klass in sqlview::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::class_is_not_abstract():
    assert not inspect.isabstract(sqlview::Class)


def test_sqlview::class_constructor_exists():
    assert callable(sqlview::Class.__init__)


def test_sqlview::class_constructor_args():
    sig = inspect.signature(sqlview::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlview::class_has_name():
    assert hasattr(sqlview::Class, "name")
    descriptor = None
    for klass in sqlview::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::relation_is_not_abstract():
    assert not inspect.isabstract(sqlview::Relation)


def test_sqlview::relation_constructor_exists():
    assert callable(sqlview::Relation.__init__)


def test_sqlview::relation_constructor_args():
    sig = inspect.signature(sqlview::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlview::relation_has_name():
    assert hasattr(sqlview::Relation, "name")
    descriptor = None
    for klass in sqlview::Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::joinright_is_not_abstract():
    assert not inspect.isabstract(sqlview::JoinRight)


def test_sqlview::joinright_constructor_exists():
    assert callable(sqlview::JoinRight.__init__)


def test_sqlview::joinright_constructor_args():
    sig = inspect.signature(sqlview::JoinRight.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::joinleft_is_not_abstract():
    assert not inspect.isabstract(sqlview::JoinLeft)


def test_sqlview::joinleft_constructor_exists():
    assert callable(sqlview::JoinLeft.__init__)


def test_sqlview::joinleft_constructor_args():
    sig = inspect.signature(sqlview::JoinLeft.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::condition_is_not_abstract():
    assert not inspect.isabstract(sqlview::Condition)


def test_sqlview::condition_constructor_exists():
    assert callable(sqlview::Condition.__init__)


def test_sqlview::condition_constructor_args():
    sig = inspect.signature(sqlview::Condition.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::from_is_not_abstract():
    assert not inspect.isabstract(sqlview::From)


def test_sqlview::from_constructor_exists():
    assert callable(sqlview::From.__init__)


def test_sqlview::from_constructor_args():
    sig = inspect.signature(sqlview::From.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::select_is_not_abstract():
    assert not inspect.isabstract(sqlview::Select)


def test_sqlview::select_constructor_exists():
    assert callable(sqlview::Select.__init__)


def test_sqlview::select_constructor_args():
    sig = inspect.signature(sqlview::Select.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_sqlview::select_has_select():
    assert hasattr(sqlview::Select, "select")
    descriptor = None
    for klass in sqlview::Select.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::metamodelname_is_not_abstract():
    assert not inspect.isabstract(sqlview::MetamodelName)


def test_sqlview::metamodelname_constructor_exists():
    assert callable(sqlview::MetamodelName.__init__)


def test_sqlview::metamodelname_constructor_args():
    sig = inspect.signature(sqlview::MetamodelName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlview::metamodelname_has_name():
    assert hasattr(sqlview::MetamodelName, "name")
    descriptor = None
    for klass in sqlview::MetamodelName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::selectattribute_is_not_abstract():
    assert not inspect.isabstract(sqlview::SelectAttribute)


def test_sqlview::selectattribute_constructor_exists():
    assert callable(sqlview::SelectAttribute.__init__)


def test_sqlview::selectattribute_constructor_args():
    sig = inspect.signature(sqlview::SelectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::expression_is_not_abstract():
    assert not inspect.isabstract(sqlview::Expression)


def test_sqlview::expression_constructor_exists():
    assert callable(sqlview::Expression.__init__)


def test_sqlview::expression_constructor_args():
    sig = inspect.signature(sqlview::Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqlview::metamodel_is_not_abstract():
    assert not inspect.isabstract(sqlview::Metamodel)


def test_sqlview::metamodel_constructor_exists():
    assert callable(sqlview::Metamodel.__init__)


def test_sqlview::metamodel_constructor_args():
    sig = inspect.signature(sqlview::Metamodel.__init__)
    params = list(sig.parameters.keys())
    assert "metamodelURL" in params, "Missing parameter 'metamodelURL'"

def test_sqlview::metamodel_has_metamodelURL():
    assert hasattr(sqlview::Metamodel, "metamodelURL")
    descriptor = None
    for klass in sqlview::Metamodel.__mro__:
        if "metamodelURL" in klass.__dict__:
            descriptor = klass.__dict__["metamodelURL"]
            break
    assert isinstance(descriptor, property)



def test_sqlview::model_is_not_abstract():
    assert not inspect.isabstract(sqlview::Model)


def test_sqlview::model_constructor_exists():
    assert callable(sqlview::Model.__init__)


def test_sqlview::model_constructor_args():
    sig = inspect.signature(sqlview::Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewName" in params, "Missing parameter 'viewName'"

def test_sqlview::model_has_viewName():
    assert hasattr(sqlview::Model, "viewName")
    descriptor = None
    for klass in sqlview::Model.__mro__:
        if "viewName" in klass.__dict__:
            descriptor = klass.__dict__["viewName"]
            break
    assert isinstance(descriptor, property)


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
sqlview::Right_strategy = st.builds(
    sqlview::Right,
    value=
        safe_text
)
sqlview::Left_strategy = st.builds(
    sqlview::Left,
)
sqlview::Comparison_strategy = st.builds(
    sqlview::Comparison,
)
sqlview::EclExpression_strategy = st.builds(
    sqlview::EclExpression,
    value=
        safe_text
)
sqlview::EObject_strategy = st.builds(
    sqlview::EObject,
)
sqlview::Join_strategy = st.builds(
    sqlview::Join,
)
sqlview::Attribute_strategy = st.builds(
    sqlview::Attribute,
    name=
        safe_text
)
sqlview::Class_strategy = st.builds(
    sqlview::Class,
    name=
        safe_text
)
sqlview::Relation_strategy = st.builds(
    sqlview::Relation,
    name=
        safe_text
)
sqlview::JoinRight_strategy = st.builds(
    sqlview::JoinRight,
)
sqlview::JoinLeft_strategy = st.builds(
    sqlview::JoinLeft,
)
sqlview::Condition_strategy = st.builds(
    sqlview::Condition,
)
sqlview::From_strategy = st.builds(
    sqlview::From,
)
sqlview::Select_strategy = st.builds(
    sqlview::Select,
    select=
        safe_text
)
sqlview::MetamodelName_strategy = st.builds(
    sqlview::MetamodelName,
    name=
        safe_text
)
sqlview::SelectAttribute_strategy = st.builds(
    sqlview::SelectAttribute,
)
sqlview::Expression_strategy = st.builds(
    sqlview::Expression,
)
sqlview::Metamodel_strategy = st.builds(
    sqlview::Metamodel,
    metamodelURL=
        safe_text
)
sqlview::Model_strategy = st.builds(
    sqlview::Model,
    viewName=
        safe_text
)

@given(instance=sqlview::Right_strategy)
@settings(max_examples=50)
def test_sqlview::right_instantiation(instance):
    assert isinstance(instance, sqlview::Right)

@given(instance=sqlview::Right_strategy)
def test_sqlview::right_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sqlview::Right_strategy)
def test_sqlview::right_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sqlview::Left_strategy)
@settings(max_examples=50)
def test_sqlview::left_instantiation(instance):
    assert isinstance(instance, sqlview::Left)

@given(instance=sqlview::Comparison_strategy)
@settings(max_examples=50)
def test_sqlview::comparison_instantiation(instance):
    assert isinstance(instance, sqlview::Comparison)

@given(instance=sqlview::EclExpression_strategy)
@settings(max_examples=50)
def test_sqlview::eclexpression_instantiation(instance):
    assert isinstance(instance, sqlview::EclExpression)

@given(instance=sqlview::EclExpression_strategy)
def test_sqlview::eclexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sqlview::EclExpression_strategy)
def test_sqlview::eclexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sqlview::EObject_strategy)
@settings(max_examples=50)
def test_sqlview::eobject_instantiation(instance):
    assert isinstance(instance, sqlview::EObject)

@given(instance=sqlview::Join_strategy)
@settings(max_examples=50)
def test_sqlview::join_instantiation(instance):
    assert isinstance(instance, sqlview::Join)

@given(instance=sqlview::Attribute_strategy)
@settings(max_examples=50)
def test_sqlview::attribute_instantiation(instance):
    assert isinstance(instance, sqlview::Attribute)

@given(instance=sqlview::Attribute_strategy)
def test_sqlview::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlview::Attribute_strategy)
def test_sqlview::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlview::Class_strategy)
@settings(max_examples=50)
def test_sqlview::class_instantiation(instance):
    assert isinstance(instance, sqlview::Class)

@given(instance=sqlview::Class_strategy)
def test_sqlview::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlview::Class_strategy)
def test_sqlview::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlview::Relation_strategy)
@settings(max_examples=50)
def test_sqlview::relation_instantiation(instance):
    assert isinstance(instance, sqlview::Relation)

@given(instance=sqlview::Relation_strategy)
def test_sqlview::relation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlview::Relation_strategy)
def test_sqlview::relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlview::JoinRight_strategy)
@settings(max_examples=50)
def test_sqlview::joinright_instantiation(instance):
    assert isinstance(instance, sqlview::JoinRight)

@given(instance=sqlview::JoinLeft_strategy)
@settings(max_examples=50)
def test_sqlview::joinleft_instantiation(instance):
    assert isinstance(instance, sqlview::JoinLeft)

@given(instance=sqlview::Condition_strategy)
@settings(max_examples=50)
def test_sqlview::condition_instantiation(instance):
    assert isinstance(instance, sqlview::Condition)

@given(instance=sqlview::From_strategy)
@settings(max_examples=50)
def test_sqlview::from_instantiation(instance):
    assert isinstance(instance, sqlview::From)

@given(instance=sqlview::Select_strategy)
@settings(max_examples=50)
def test_sqlview::select_instantiation(instance):
    assert isinstance(instance, sqlview::Select)

@given(instance=sqlview::Select_strategy)
def test_sqlview::select_select_type(instance):
    assert isinstance(instance.select, str)


@given(instance=sqlview::Select_strategy)
def test_sqlview::select_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=sqlview::MetamodelName_strategy)
@settings(max_examples=50)
def test_sqlview::metamodelname_instantiation(instance):
    assert isinstance(instance, sqlview::MetamodelName)

@given(instance=sqlview::MetamodelName_strategy)
def test_sqlview::metamodelname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlview::MetamodelName_strategy)
def test_sqlview::metamodelname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlview::SelectAttribute_strategy)
@settings(max_examples=50)
def test_sqlview::selectattribute_instantiation(instance):
    assert isinstance(instance, sqlview::SelectAttribute)

@given(instance=sqlview::Expression_strategy)
@settings(max_examples=50)
def test_sqlview::expression_instantiation(instance):
    assert isinstance(instance, sqlview::Expression)

@given(instance=sqlview::Metamodel_strategy)
@settings(max_examples=50)
def test_sqlview::metamodel_instantiation(instance):
    assert isinstance(instance, sqlview::Metamodel)

@given(instance=sqlview::Metamodel_strategy)
def test_sqlview::metamodel_metamodelURL_type(instance):
    assert isinstance(instance.metamodelURL, str)


@given(instance=sqlview::Metamodel_strategy)
def test_sqlview::metamodel_metamodelURL_setter(instance):
    original = instance.metamodelURL
    instance.metamodelURL = original
    assert instance.metamodelURL == original

@given(instance=sqlview::Model_strategy)
@settings(max_examples=50)
def test_sqlview::model_instantiation(instance):
    assert isinstance(instance, sqlview::Model)

@given(instance=sqlview::Model_strategy)
def test_sqlview::model_viewName_type(instance):
    assert isinstance(instance.viewName, str)


@given(instance=sqlview::Model_strategy)
def test_sqlview::model_viewName_setter(instance):
    original = instance.viewName
    instance.viewName = original
    assert instance.viewName == original
