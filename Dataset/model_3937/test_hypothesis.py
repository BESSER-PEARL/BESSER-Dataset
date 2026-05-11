import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Role,
    myDsl::Attribute,
    Type,
    myDsl::Association,
    myDsl::Entity,
    myDsl::DataType,
    myDsl::Type,
    myDsl::Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::role_is_not_abstract():
    assert not inspect.isabstract(myDsl::Role)


def test_mydsl::role_constructor_exists():
    assert callable(myDsl::Role.__init__)


def test_mydsl::role_constructor_args():
    sig = inspect.signature(myDsl::Role.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::role_has_many():
    assert hasattr(myDsl::Role, "many")
    descriptor = None
    for klass in myDsl::Role.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::role_has_name():
    assert hasattr(myDsl::Role, "name")
    descriptor = None
    for klass in myDsl::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl::Attribute)


def test_mydsl::attribute_constructor_exists():
    assert callable(myDsl::Attribute.__init__)


def test_mydsl::attribute_constructor_args():
    sig = inspect.signature(myDsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::attribute_has_many():
    assert hasattr(myDsl::Attribute, "many")
    descriptor = None
    for klass in myDsl::Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::attribute_has_name():
    assert hasattr(myDsl::Attribute, "name")
    descriptor = None
    for klass in myDsl::Attribute.__mro__:
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



def test_mydsl::association_is_not_abstract():
    assert not inspect.isabstract(myDsl::Association)


def test_mydsl::association_constructor_exists():
    assert callable(myDsl::Association.__init__)


def test_mydsl::association_constructor_args():
    sig = inspect.signature(myDsl::Association.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataType)


def test_mydsl::datatype_constructor_exists():
    assert callable(myDsl::DataType.__init__)


def test_mydsl::datatype_constructor_args():
    sig = inspect.signature(myDsl::DataType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::domainmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl::Domainmodel)


def test_mydsl::domainmodel_constructor_exists():
    assert callable(myDsl::Domainmodel.__init__)


def test_mydsl::domainmodel_constructor_args():
    sig = inspect.signature(myDsl::Domainmodel.__init__)
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
myDsl::Role_strategy = st.builds(
    myDsl::Role,
    many=
        st.booleans(),
    name=
        safe_text
)
myDsl::Attribute_strategy = st.builds(
    myDsl::Attribute,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::Association_strategy = st.builds(
    myDsl::Association,
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
)
myDsl::DataType_strategy = st.builds(
    myDsl::DataType,
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::Domainmodel_strategy = st.builds(
    myDsl::Domainmodel,
)

@given(instance=myDsl::Role_strategy)
@settings(max_examples=50)
def test_mydsl::role_instantiation(instance):
    assert isinstance(instance, myDsl::Role)

@given(instance=myDsl::Role_strategy)
def test_mydsl::role_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myDsl::Role_strategy)
def test_mydsl::role_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl::Role_strategy)
def test_mydsl::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Role_strategy)
def test_mydsl::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Attribute_strategy)
@settings(max_examples=50)
def test_mydsl::attribute_instantiation(instance):
    assert isinstance(instance, myDsl::Attribute)

@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::Association_strategy)
@settings(max_examples=50)
def test_mydsl::association_instantiation(instance):
    assert isinstance(instance, myDsl::Association)

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=myDsl::DataType_strategy)
@settings(max_examples=50)
def test_mydsl::datatype_instantiation(instance):
    assert isinstance(instance, myDsl::DataType)

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Domainmodel_strategy)
@settings(max_examples=50)
def test_mydsl::domainmodel_instantiation(instance):
    assert isinstance(instance, myDsl::Domainmodel)
