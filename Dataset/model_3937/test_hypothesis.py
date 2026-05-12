import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Role,
    myDsl_Attribute,
    Type,
    myDsl_Association,
    myDsl_Entity,
    myDsl_DataType,
    myDsl_Type,
    myDsl_Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_role_is_not_abstract():
    assert not inspect.isabstract(myDsl_Role)


def test_mydsl_role_constructor_exists():
    assert callable(myDsl_Role.__init__)


def test_mydsl_role_constructor_args():
    sig = inspect.signature(myDsl_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl_role_has_name():
    assert hasattr(myDsl_Role, "name")
    descriptor = None
    for klass in myDsl_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_role_has_many():
    assert hasattr(myDsl_Role, "many")
    descriptor = None
    for klass in myDsl_Role.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl_Attribute)


def test_mydsl_attribute_constructor_exists():
    assert callable(myDsl_Attribute.__init__)


def test_mydsl_attribute_constructor_args():
    sig = inspect.signature(myDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl_attribute_has_name():
    assert hasattr(myDsl_Attribute, "name")
    descriptor = None
    for klass in myDsl_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_attribute_has_many():
    assert hasattr(myDsl_Attribute, "many")
    descriptor = None
    for klass in myDsl_Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_association_is_not_abstract():
    assert not inspect.isabstract(myDsl_Association)


def test_mydsl_association_constructor_exists():
    assert callable(myDsl_Association.__init__)


def test_mydsl_association_constructor_args():
    sig = inspect.signature(myDsl_Association.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_entity_is_not_abstract():
    assert not inspect.isabstract(myDsl_Entity)


def test_mydsl_entity_constructor_exists():
    assert callable(myDsl_Entity.__init__)


def test_mydsl_entity_constructor_args():
    sig = inspect.signature(myDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl_DataType)


def test_mydsl_datatype_constructor_exists():
    assert callable(myDsl_DataType.__init__)


def test_mydsl_datatype_constructor_args():
    sig = inspect.signature(myDsl_DataType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_type_has_name():
    assert hasattr(myDsl_Type, "name")
    descriptor = None
    for klass in myDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_domainmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl_Domainmodel)


def test_mydsl_domainmodel_constructor_exists():
    assert callable(myDsl_Domainmodel.__init__)


def test_mydsl_domainmodel_constructor_args():
    sig = inspect.signature(myDsl_Domainmodel.__init__)
    params = list(sig.parameters.keys())


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
myDsl_Role_strategy = st.builds(
    myDsl_Role,
    name=
        safe_text,
    many=
        st.booleans()
)
myDsl_Attribute_strategy = st.builds(
    myDsl_Attribute,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
myDsl_Association_strategy = st.builds(
    myDsl_Association,
)
myDsl_Entity_strategy = st.builds(
    myDsl_Entity,
)
myDsl_DataType_strategy = st.builds(
    myDsl_DataType,
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_Domainmodel_strategy = st.builds(
    myDsl_Domainmodel,
)

@given(instance=myDsl_Role_strategy)
@settings(max_examples=50)
def test_mydsl_role_instantiation(instance):
    assert isinstance(instance, myDsl_Role)



@given(instance=myDsl_Role_strategy)
def test_mydsl_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Role_strategy)
def test_mydsl_role_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl_Attribute_strategy)
@settings(max_examples=50)
def test_mydsl_attribute_instantiation(instance):
    assert isinstance(instance, myDsl_Attribute)



@given(instance=myDsl_Attribute_strategy)
def test_mydsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Attribute_strategy)
def test_mydsl_attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl_Association_strategy)
@settings(max_examples=50)
def test_mydsl_association_instantiation(instance):
    assert isinstance(instance, myDsl_Association)

@given(instance=myDsl_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDsl_Entity)

@given(instance=myDsl_DataType_strategy)
@settings(max_examples=50)
def test_mydsl_datatype_instantiation(instance):
    assert isinstance(instance, myDsl_DataType)

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Domainmodel_strategy)
@settings(max_examples=50)
def test_mydsl_domainmodel_instantiation(instance):
    assert isinstance(instance, myDsl_Domainmodel)
