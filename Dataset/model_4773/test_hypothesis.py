import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    types_EObject,
    TypeReference,
    types_ArrayType,
    types_TypeReference,
    types_Property,
    types_Operation,
    UserType,
    types_ServiceType,
    types_ClassType,
    Type,
    types_UserType,
    types_PrimitiveType,
    types_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types_eobject_is_not_abstract():
    assert not inspect.isabstract(types_EObject)


def test_types_eobject_constructor_exists():
    assert callable(types_EObject.__init__)


def test_types_eobject_constructor_args():
    sig = inspect.signature(types_EObject.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types_arraytype_is_not_abstract():
    assert not inspect.isabstract(types_ArrayType)


def test_types_arraytype_constructor_exists():
    assert callable(types_ArrayType.__init__)


def test_types_arraytype_constructor_args():
    sig = inspect.signature(types_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types_arraytype_has_size():
    assert hasattr(types_ArrayType, "size")
    descriptor = None
    for klass in types_ArrayType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types_typereference_is_not_abstract():
    assert not inspect.isabstract(types_TypeReference)


def test_types_typereference_constructor_exists():
    assert callable(types_TypeReference.__init__)


def test_types_typereference_constructor_args():
    sig = inspect.signature(types_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types_property_is_not_abstract():
    assert not inspect.isabstract(types_Property)


def test_types_property_constructor_exists():
    assert callable(types_Property.__init__)


def test_types_property_constructor_args():
    sig = inspect.signature(types_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_property_has_name():
    assert hasattr(types_Property, "name")
    descriptor = None
    for klass in types_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_operation_is_not_abstract():
    assert not inspect.isabstract(types_Operation)


def test_types_operation_constructor_exists():
    assert callable(types_Operation.__init__)


def test_types_operation_constructor_args():
    sig = inspect.signature(types_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_operation_has_name():
    assert hasattr(types_Operation, "name")
    descriptor = None
    for klass in types_Operation.__mro__:
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



def test_types_servicetype_is_not_abstract():
    assert not inspect.isabstract(types_ServiceType)


def test_types_servicetype_constructor_exists():
    assert callable(types_ServiceType.__init__)


def test_types_servicetype_constructor_args():
    sig = inspect.signature(types_ServiceType.__init__)
    params = list(sig.parameters.keys())



def test_types_classtype_is_not_abstract():
    assert not inspect.isabstract(types_ClassType)


def test_types_classtype_constructor_exists():
    assert callable(types_ClassType.__init__)


def test_types_classtype_constructor_args():
    sig = inspect.signature(types_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types_usertype_is_not_abstract():
    assert not inspect.isabstract(types_UserType)


def test_types_usertype_constructor_exists():
    assert callable(types_UserType.__init__)


def test_types_usertype_constructor_args():
    sig = inspect.signature(types_UserType.__init__)
    params = list(sig.parameters.keys())



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_type_has_name():
    assert hasattr(types_Type, "name")
    descriptor = None
    for klass in types_Type.__mro__:
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
types_EObject_strategy = st.builds(
    types_EObject,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
types_ArrayType_strategy = st.builds(
    types_ArrayType,
    size=
        st.integers()
)
types_TypeReference_strategy = st.builds(
    types_TypeReference,
)
types_Property_strategy = st.builds(
    types_Property,
    name=
        safe_text
)
types_Operation_strategy = st.builds(
    types_Operation,
    name=
        safe_text
)
UserType_strategy = st.builds(
    UserType,
)
types_ServiceType_strategy = st.builds(
    types_ServiceType,
)
types_ClassType_strategy = st.builds(
    types_ClassType,
)
Type_strategy = st.builds(
    Type,
)
types_UserType_strategy = st.builds(
    types_UserType,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
types_Type_strategy = st.builds(
    types_Type,
    name=
        safe_text
)

@given(instance=types_EObject_strategy)
@settings(max_examples=50)
def test_types_eobject_instantiation(instance):
    assert isinstance(instance, types_EObject)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=types_ArrayType_strategy)
@settings(max_examples=50)
def test_types_arraytype_instantiation(instance):
    assert isinstance(instance, types_ArrayType)



@given(instance=types_ArrayType_strategy)
def test_types_arraytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types_TypeReference_strategy)
@settings(max_examples=50)
def test_types_typereference_instantiation(instance):
    assert isinstance(instance, types_TypeReference)

@given(instance=types_Property_strategy)
@settings(max_examples=50)
def test_types_property_instantiation(instance):
    assert isinstance(instance, types_Property)



@given(instance=types_Property_strategy)
def test_types_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_Operation_strategy)
@settings(max_examples=50)
def test_types_operation_instantiation(instance):
    assert isinstance(instance, types_Operation)



@given(instance=types_Operation_strategy)
def test_types_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UserType_strategy)
@settings(max_examples=50)
def test_usertype_instantiation(instance):
    assert isinstance(instance, UserType)

@given(instance=types_ServiceType_strategy)
@settings(max_examples=50)
def test_types_servicetype_instantiation(instance):
    assert isinstance(instance, types_ServiceType)

@given(instance=types_ClassType_strategy)
@settings(max_examples=50)
def test_types_classtype_instantiation(instance):
    assert isinstance(instance, types_ClassType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_UserType_strategy)
@settings(max_examples=50)
def test_types_usertype_instantiation(instance):
    assert isinstance(instance, types_UserType)

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)



@given(instance=types_Type_strategy)
def test_types_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
