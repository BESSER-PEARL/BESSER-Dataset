import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    types::TypeReference,
    types::Property,
    types::Operation,
    UserType,
    types::ServiceType,
    types::ClassType,
    types::EObject,
    TypeReference,
    types::ArrayType,
    Type,
    types::UserType,
    types::PrimitiveType,
    types::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types::typereference_is_not_abstract():
    assert not inspect.isabstract(types::TypeReference)


def test_types::typereference_constructor_exists():
    assert callable(types::TypeReference.__init__)


def test_types::typereference_constructor_args():
    sig = inspect.signature(types::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::property_is_not_abstract():
    assert not inspect.isabstract(types::Property)


def test_types::property_constructor_exists():
    assert callable(types::Property.__init__)


def test_types::property_constructor_args():
    sig = inspect.signature(types::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::property_has_name():
    assert hasattr(types::Property, "name")
    descriptor = None
    for klass in types::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::operation_is_not_abstract():
    assert not inspect.isabstract(types::Operation)


def test_types::operation_constructor_exists():
    assert callable(types::Operation.__init__)


def test_types::operation_constructor_args():
    sig = inspect.signature(types::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::operation_has_name():
    assert hasattr(types::Operation, "name")
    descriptor = None
    for klass in types::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usertype_is_not_abstract():
    assert not inspect.isabstract(UserType)


def test_usertype_constructor_exists():
    assert callable(UserType.__init__)


def test_usertype_constructor_args():
    sig = inspect.signature(UserType.__init__)
    params = list(sig.parameters.keys())



def test_types::servicetype_is_not_abstract():
    assert not inspect.isabstract(types::ServiceType)


def test_types::servicetype_constructor_exists():
    assert callable(types::ServiceType.__init__)


def test_types::servicetype_constructor_args():
    sig = inspect.signature(types::ServiceType.__init__)
    params = list(sig.parameters.keys())



def test_types::classtype_is_not_abstract():
    assert not inspect.isabstract(types::ClassType)


def test_types::classtype_constructor_exists():
    assert callable(types::ClassType.__init__)


def test_types::classtype_constructor_args():
    sig = inspect.signature(types::ClassType.__init__)
    params = list(sig.parameters.keys())



def test_types::eobject_is_not_abstract():
    assert not inspect.isabstract(types::EObject)


def test_types::eobject_constructor_exists():
    assert callable(types::EObject.__init__)


def test_types::eobject_constructor_args():
    sig = inspect.signature(types::EObject.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::arraytype_is_not_abstract():
    assert not inspect.isabstract(types::ArrayType)


def test_types::arraytype_constructor_exists():
    assert callable(types::ArrayType.__init__)


def test_types::arraytype_constructor_args():
    sig = inspect.signature(types::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types::arraytype_has_size():
    assert hasattr(types::ArrayType, "size")
    descriptor = None
    for klass in types::ArrayType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types::usertype_is_not_abstract():
    assert not inspect.isabstract(types::UserType)


def test_types::usertype_constructor_exists():
    assert callable(types::UserType.__init__)


def test_types::usertype_constructor_args():
    sig = inspect.signature(types::UserType.__init__)
    params = list(sig.parameters.keys())



def test_types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(types::PrimitiveType)


def test_types::primitivetype_constructor_exists():
    assert callable(types::PrimitiveType.__init__)


def test_types::primitivetype_constructor_args():
    sig = inspect.signature(types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::type_has_name():
    assert hasattr(types::Type, "name")
    descriptor = None
    for klass in types::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
types::TypeReference_strategy = st.builds(
    types::TypeReference,
)
types::Property_strategy = st.builds(
    types::Property,
    name=
        safe_text
)
types::Operation_strategy = st.builds(
    types::Operation,
    name=
        safe_text
)
UserType_strategy = st.builds(
    UserType,
)
types::ServiceType_strategy = st.builds(
    types::ServiceType,
)
types::ClassType_strategy = st.builds(
    types::ClassType,
)
types::EObject_strategy = st.builds(
    types::EObject,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
types::ArrayType_strategy = st.builds(
    types::ArrayType,
    size=
        st.integers()
)
Type_strategy = st.builds(
    Type,
)
types::UserType_strategy = st.builds(
    types::UserType,
)
types::PrimitiveType_strategy = st.builds(
    types::PrimitiveType,
)
types::Type_strategy = st.builds(
    types::Type,
    name=
        safe_text
)

@given(instance=types::TypeReference_strategy)
@settings(max_examples=50)
def test_types::typereference_instantiation(instance):
    assert isinstance(instance, types::TypeReference)

@given(instance=types::Property_strategy)
@settings(max_examples=50)
def test_types::property_instantiation(instance):
    assert isinstance(instance, types::Property)

@given(instance=types::Property_strategy)
def test_types::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::Property_strategy)
def test_types::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::Operation_strategy)
@settings(max_examples=50)
def test_types::operation_instantiation(instance):
    assert isinstance(instance, types::Operation)

@given(instance=types::Operation_strategy)
def test_types::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::Operation_strategy)
def test_types::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UserType_strategy)
@settings(max_examples=50)
def test_usertype_instantiation(instance):
    assert isinstance(instance, UserType)

@given(instance=types::ServiceType_strategy)
@settings(max_examples=50)
def test_types::servicetype_instantiation(instance):
    assert isinstance(instance, types::ServiceType)

@given(instance=types::ClassType_strategy)
@settings(max_examples=50)
def test_types::classtype_instantiation(instance):
    assert isinstance(instance, types::ClassType)

@given(instance=types::EObject_strategy)
@settings(max_examples=50)
def test_types::eobject_instantiation(instance):
    assert isinstance(instance, types::EObject)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=types::ArrayType_strategy)
@settings(max_examples=50)
def test_types::arraytype_instantiation(instance):
    assert isinstance(instance, types::ArrayType)

@given(instance=types::ArrayType_strategy)
def test_types::arraytype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=types::ArrayType_strategy)
def test_types::arraytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types::UserType_strategy)
@settings(max_examples=50)
def test_types::usertype_instantiation(instance):
    assert isinstance(instance, types::UserType)

@given(instance=types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_types::primitivetype_instantiation(instance):
    assert isinstance(instance, types::PrimitiveType)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::Type_strategy)
def test_types::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::Type_strategy)
def test_types::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
