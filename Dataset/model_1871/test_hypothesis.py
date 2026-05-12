import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    datatypes_Field,
    ComplexType,
    datatypes_IDLReference,
    datatypes_CustomType,
    datatypes_VectorType,
    IDLReference,
    datatypes_RosIDLReference,
    datatypes_DataType,
    datatypes_TypesLibrary,
    DataType,
    datatypes_ComplexType,
    datatypes_SimpleType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datatypes_field_is_not_abstract():
    assert not inspect.isabstract(datatypes_Field)


def test_datatypes_field_constructor_exists():
    assert callable(datatypes_Field.__init__)


def test_datatypes_field_constructor_args():
    sig = inspect.signature(datatypes_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "measureUnit" in params, "Missing parameter 'measureUnit'"

def test_datatypes_field_has_name():
    assert hasattr(datatypes_Field, "name")
    descriptor = None
    for klass in datatypes_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatypes_field_has_description():
    assert hasattr(datatypes_Field, "description")
    descriptor = None
    for klass in datatypes_Field.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datatypes_field_has_measureUnit():
    assert hasattr(datatypes_Field, "measureUnit")
    descriptor = None
    for klass in datatypes_Field.__mro__:
        if "measureUnit" in klass.__dict__:
            descriptor = klass.__dict__["measureUnit"]
            break
    assert isinstance(descriptor, property)



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_idlreference_is_not_abstract():
    assert not inspect.isabstract(datatypes_IDLReference)


def test_datatypes_idlreference_constructor_exists():
    assert callable(datatypes_IDLReference.__init__)


def test_datatypes_idlreference_constructor_args():
    sig = inspect.signature(datatypes_IDLReference.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_customtype_is_not_abstract():
    assert not inspect.isabstract(datatypes_CustomType)


def test_datatypes_customtype_constructor_exists():
    assert callable(datatypes_CustomType.__init__)


def test_datatypes_customtype_constructor_args():
    sig = inspect.signature(datatypes_CustomType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_vectortype_is_not_abstract():
    assert not inspect.isabstract(datatypes_VectorType)


def test_datatypes_vectortype_constructor_exists():
    assert callable(datatypes_VectorType.__init__)


def test_datatypes_vectortype_constructor_args():
    sig = inspect.signature(datatypes_VectorType.__init__)
    params = list(sig.parameters.keys())



def test_idlreference_is_not_abstract():
    assert not inspect.isabstract(IDLReference)


def test_idlreference_constructor_exists():
    assert callable(IDLReference.__init__)


def test_idlreference_constructor_args():
    sig = inspect.signature(IDLReference.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_rosidlreference_is_not_abstract():
    assert not inspect.isabstract(datatypes_RosIDLReference)


def test_datatypes_rosidlreference_constructor_exists():
    assert callable(datatypes_RosIDLReference.__init__)


def test_datatypes_rosidlreference_constructor_args():
    sig = inspect.signature(datatypes_RosIDLReference.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "rosPackage" in params, "Missing parameter 'rosPackage'"

def test_datatypes_rosidlreference_has_namespace():
    assert hasattr(datatypes_RosIDLReference, "namespace")
    descriptor = None
    for klass in datatypes_RosIDLReference.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_datatypes_rosidlreference_has_rosPackage():
    assert hasattr(datatypes_RosIDLReference, "rosPackage")
    descriptor = None
    for klass in datatypes_RosIDLReference.__mro__:
        if "rosPackage" in klass.__dict__:
            descriptor = klass.__dict__["rosPackage"]
            break
    assert isinstance(descriptor, property)



def test_datatypes_datatype_is_not_abstract():
    assert not inspect.isabstract(datatypes_DataType)


def test_datatypes_datatype_constructor_exists():
    assert callable(datatypes_DataType.__init__)


def test_datatypes_datatype_constructor_args():
    sig = inspect.signature(datatypes_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes_datatype_has_name():
    assert hasattr(datatypes_DataType, "name")
    descriptor = None
    for klass in datatypes_DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypes_typeslibrary_is_not_abstract():
    assert not inspect.isabstract(datatypes_TypesLibrary)


def test_datatypes_typeslibrary_constructor_exists():
    assert callable(datatypes_TypesLibrary.__init__)


def test_datatypes_typeslibrary_constructor_args():
    sig = inspect.signature(datatypes_TypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes_typeslibrary_has_name():
    assert hasattr(datatypes_TypesLibrary, "name")
    descriptor = None
    for klass in datatypes_TypesLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_complextype_is_not_abstract():
    assert not inspect.isabstract(datatypes_ComplexType)


def test_datatypes_complextype_constructor_exists():
    assert callable(datatypes_ComplexType.__init__)


def test_datatypes_complextype_constructor_args():
    sig = inspect.signature(datatypes_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_simpletype_is_not_abstract():
    assert not inspect.isabstract(datatypes_SimpleType)


def test_datatypes_simpletype_constructor_exists():
    assert callable(datatypes_SimpleType.__init__)


def test_datatypes_simpletype_constructor_args():
    sig = inspect.signature(datatypes_SimpleType.__init__)
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
datatypes_Field_strategy = st.builds(
    datatypes_Field,
    name=
        safe_text,
    description=
        safe_text,
    measureUnit=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
datatypes_IDLReference_strategy = st.builds(
    datatypes_IDLReference,
)
datatypes_CustomType_strategy = st.builds(
    datatypes_CustomType,
)
datatypes_VectorType_strategy = st.builds(
    datatypes_VectorType,
)
IDLReference_strategy = st.builds(
    IDLReference,
)
datatypes_RosIDLReference_strategy = st.builds(
    datatypes_RosIDLReference,
    namespace=
        safe_text,
    rosPackage=
        safe_text
)
datatypes_DataType_strategy = st.builds(
    datatypes_DataType,
    name=
        safe_text
)
datatypes_TypesLibrary_strategy = st.builds(
    datatypes_TypesLibrary,
    name=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
datatypes_ComplexType_strategy = st.builds(
    datatypes_ComplexType,
)
datatypes_SimpleType_strategy = st.builds(
    datatypes_SimpleType,
)

@given(instance=datatypes_Field_strategy)
@settings(max_examples=50)
def test_datatypes_field_instantiation(instance):
    assert isinstance(instance, datatypes_Field)



@given(instance=datatypes_Field_strategy)
def test_datatypes_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=datatypes_Field_strategy)
def test_datatypes_field_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=datatypes_Field_strategy)
def test_datatypes_field_measureUnit_setter(instance):
    original = instance.measureUnit
    instance.measureUnit = original
    assert instance.measureUnit == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=datatypes_IDLReference_strategy)
@settings(max_examples=50)
def test_datatypes_idlreference_instantiation(instance):
    assert isinstance(instance, datatypes_IDLReference)

@given(instance=datatypes_CustomType_strategy)
@settings(max_examples=50)
def test_datatypes_customtype_instantiation(instance):
    assert isinstance(instance, datatypes_CustomType)

@given(instance=datatypes_VectorType_strategy)
@settings(max_examples=50)
def test_datatypes_vectortype_instantiation(instance):
    assert isinstance(instance, datatypes_VectorType)

@given(instance=IDLReference_strategy)
@settings(max_examples=50)
def test_idlreference_instantiation(instance):
    assert isinstance(instance, IDLReference)

@given(instance=datatypes_RosIDLReference_strategy)
@settings(max_examples=50)
def test_datatypes_rosidlreference_instantiation(instance):
    assert isinstance(instance, datatypes_RosIDLReference)



@given(instance=datatypes_RosIDLReference_strategy)
def test_datatypes_rosidlreference_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=datatypes_RosIDLReference_strategy)
def test_datatypes_rosidlreference_rosPackage_setter(instance):
    original = instance.rosPackage
    instance.rosPackage = original
    assert instance.rosPackage == original

@given(instance=datatypes_DataType_strategy)
@settings(max_examples=50)
def test_datatypes_datatype_instantiation(instance):
    assert isinstance(instance, datatypes_DataType)



@given(instance=datatypes_DataType_strategy)
def test_datatypes_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datatypes_TypesLibrary_strategy)
@settings(max_examples=50)
def test_datatypes_typeslibrary_instantiation(instance):
    assert isinstance(instance, datatypes_TypesLibrary)



@given(instance=datatypes_TypesLibrary_strategy)
def test_datatypes_typeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=datatypes_ComplexType_strategy)
@settings(max_examples=50)
def test_datatypes_complextype_instantiation(instance):
    assert isinstance(instance, datatypes_ComplexType)

@given(instance=datatypes_SimpleType_strategy)
@settings(max_examples=50)
def test_datatypes_simpletype_instantiation(instance):
    assert isinstance(instance, datatypes_SimpleType)
