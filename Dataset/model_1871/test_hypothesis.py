import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    datatypes::Field,
    ComplexType,
    datatypes::IDLReference,
    datatypes::CustomType,
    datatypes::VectorType,
    IDLReference,
    datatypes::RosIDLReference,
    datatypes::DataType,
    datatypes::TypesLibrary,
    DataType,
    datatypes::ComplexType,
    datatypes::SimpleType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datatypes::field_is_not_abstract():
    assert not inspect.isabstract(datatypes::Field)


def test_datatypes::field_constructor_exists():
    assert callable(datatypes::Field.__init__)


def test_datatypes::field_constructor_args():
    sig = inspect.signature(datatypes::Field.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "measureUnit" in params, "Missing parameter 'measureUnit'"
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes::field_has_description():
    assert hasattr(datatypes::Field, "description")
    descriptor = None
    for klass in datatypes::Field.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datatypes::field_has_measureUnit():
    assert hasattr(datatypes::Field, "measureUnit")
    descriptor = None
    for klass in datatypes::Field.__mro__:
        if "measureUnit" in klass.__dict__:
            descriptor = klass.__dict__["measureUnit"]
            break
    assert isinstance(descriptor, property)

def test_datatypes::field_has_name():
    assert hasattr(datatypes::Field, "name")
    descriptor = None
    for klass in datatypes::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::idlreference_is_not_abstract():
    assert not inspect.isabstract(datatypes::IDLReference)


def test_datatypes::idlreference_constructor_exists():
    assert callable(datatypes::IDLReference.__init__)


def test_datatypes::idlreference_constructor_args():
    sig = inspect.signature(datatypes::IDLReference.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::customtype_is_not_abstract():
    assert not inspect.isabstract(datatypes::CustomType)


def test_datatypes::customtype_constructor_exists():
    assert callable(datatypes::CustomType.__init__)


def test_datatypes::customtype_constructor_args():
    sig = inspect.signature(datatypes::CustomType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::vectortype_is_not_abstract():
    assert not inspect.isabstract(datatypes::VectorType)


def test_datatypes::vectortype_constructor_exists():
    assert callable(datatypes::VectorType.__init__)


def test_datatypes::vectortype_constructor_args():
    sig = inspect.signature(datatypes::VectorType.__init__)
    params = list(sig.parameters.keys())



def test_idlreference_is_not_abstract():
    assert not inspect.isabstract(IDLReference)


def test_idlreference_constructor_exists():
    assert callable(IDLReference.__init__)


def test_idlreference_constructor_args():
    sig = inspect.signature(IDLReference.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::rosidlreference_is_not_abstract():
    assert not inspect.isabstract(datatypes::RosIDLReference)


def test_datatypes::rosidlreference_constructor_exists():
    assert callable(datatypes::RosIDLReference.__init__)


def test_datatypes::rosidlreference_constructor_args():
    sig = inspect.signature(datatypes::RosIDLReference.__init__)
    params = list(sig.parameters.keys())
    assert "rosPackage" in params, "Missing parameter 'rosPackage'"
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_datatypes::rosidlreference_has_rosPackage():
    assert hasattr(datatypes::RosIDLReference, "rosPackage")
    descriptor = None
    for klass in datatypes::RosIDLReference.__mro__:
        if "rosPackage" in klass.__dict__:
            descriptor = klass.__dict__["rosPackage"]
            break
    assert isinstance(descriptor, property)

def test_datatypes::rosidlreference_has_namespace():
    assert hasattr(datatypes::RosIDLReference, "namespace")
    descriptor = None
    for klass in datatypes::RosIDLReference.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_datatypes::datatype_is_not_abstract():
    assert not inspect.isabstract(datatypes::DataType)


def test_datatypes::datatype_constructor_exists():
    assert callable(datatypes::DataType.__init__)


def test_datatypes::datatype_constructor_args():
    sig = inspect.signature(datatypes::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes::datatype_has_name():
    assert hasattr(datatypes::DataType, "name")
    descriptor = None
    for klass in datatypes::DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypes::typeslibrary_is_not_abstract():
    assert not inspect.isabstract(datatypes::TypesLibrary)


def test_datatypes::typeslibrary_constructor_exists():
    assert callable(datatypes::TypesLibrary.__init__)


def test_datatypes::typeslibrary_constructor_args():
    sig = inspect.signature(datatypes::TypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes::typeslibrary_has_name():
    assert hasattr(datatypes::TypesLibrary, "name")
    descriptor = None
    for klass in datatypes::TypesLibrary.__mro__:
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



def test_datatypes::complextype_is_not_abstract():
    assert not inspect.isabstract(datatypes::ComplexType)


def test_datatypes::complextype_constructor_exists():
    assert callable(datatypes::ComplexType.__init__)


def test_datatypes::complextype_constructor_args():
    sig = inspect.signature(datatypes::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::simpletype_is_not_abstract():
    assert not inspect.isabstract(datatypes::SimpleType)


def test_datatypes::simpletype_constructor_exists():
    assert callable(datatypes::SimpleType.__init__)


def test_datatypes::simpletype_constructor_args():
    sig = inspect.signature(datatypes::SimpleType.__init__)
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
datatypes::Field_strategy = st.builds(
    datatypes::Field,
    description=
        safe_text,
    measureUnit=
        safe_text,
    name=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
datatypes::IDLReference_strategy = st.builds(
    datatypes::IDLReference,
)
datatypes::CustomType_strategy = st.builds(
    datatypes::CustomType,
)
datatypes::VectorType_strategy = st.builds(
    datatypes::VectorType,
)
IDLReference_strategy = st.builds(
    IDLReference,
)
datatypes::RosIDLReference_strategy = st.builds(
    datatypes::RosIDLReference,
    rosPackage=
        safe_text,
    namespace=
        safe_text
)
datatypes::DataType_strategy = st.builds(
    datatypes::DataType,
    name=
        safe_text
)
datatypes::TypesLibrary_strategy = st.builds(
    datatypes::TypesLibrary,
    name=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
datatypes::ComplexType_strategy = st.builds(
    datatypes::ComplexType,
)
datatypes::SimpleType_strategy = st.builds(
    datatypes::SimpleType,
)

@given(instance=datatypes::Field_strategy)
@settings(max_examples=50)
def test_datatypes::field_instantiation(instance):
    assert isinstance(instance, datatypes::Field)

@given(instance=datatypes::Field_strategy)
def test_datatypes::field_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=datatypes::Field_strategy)
def test_datatypes::field_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=datatypes::Field_strategy)
def test_datatypes::field_measureUnit_type(instance):
    assert isinstance(instance.measureUnit, str)


@given(instance=datatypes::Field_strategy)
def test_datatypes::field_measureUnit_setter(instance):
    original = instance.measureUnit
    instance.measureUnit = original
    assert instance.measureUnit == original

@given(instance=datatypes::Field_strategy)
def test_datatypes::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatypes::Field_strategy)
def test_datatypes::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=datatypes::IDLReference_strategy)
@settings(max_examples=50)
def test_datatypes::idlreference_instantiation(instance):
    assert isinstance(instance, datatypes::IDLReference)

@given(instance=datatypes::CustomType_strategy)
@settings(max_examples=50)
def test_datatypes::customtype_instantiation(instance):
    assert isinstance(instance, datatypes::CustomType)

@given(instance=datatypes::VectorType_strategy)
@settings(max_examples=50)
def test_datatypes::vectortype_instantiation(instance):
    assert isinstance(instance, datatypes::VectorType)

@given(instance=IDLReference_strategy)
@settings(max_examples=50)
def test_idlreference_instantiation(instance):
    assert isinstance(instance, IDLReference)

@given(instance=datatypes::RosIDLReference_strategy)
@settings(max_examples=50)
def test_datatypes::rosidlreference_instantiation(instance):
    assert isinstance(instance, datatypes::RosIDLReference)

@given(instance=datatypes::RosIDLReference_strategy)
def test_datatypes::rosidlreference_rosPackage_type(instance):
    assert isinstance(instance.rosPackage, str)


@given(instance=datatypes::RosIDLReference_strategy)
def test_datatypes::rosidlreference_rosPackage_setter(instance):
    original = instance.rosPackage
    instance.rosPackage = original
    assert instance.rosPackage == original

@given(instance=datatypes::RosIDLReference_strategy)
def test_datatypes::rosidlreference_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=datatypes::RosIDLReference_strategy)
def test_datatypes::rosidlreference_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=datatypes::DataType_strategy)
@settings(max_examples=50)
def test_datatypes::datatype_instantiation(instance):
    assert isinstance(instance, datatypes::DataType)

@given(instance=datatypes::DataType_strategy)
def test_datatypes::datatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatypes::DataType_strategy)
def test_datatypes::datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datatypes::TypesLibrary_strategy)
@settings(max_examples=50)
def test_datatypes::typeslibrary_instantiation(instance):
    assert isinstance(instance, datatypes::TypesLibrary)

@given(instance=datatypes::TypesLibrary_strategy)
def test_datatypes::typeslibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatypes::TypesLibrary_strategy)
def test_datatypes::typeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=datatypes::ComplexType_strategy)
@settings(max_examples=50)
def test_datatypes::complextype_instantiation(instance):
    assert isinstance(instance, datatypes::ComplexType)

@given(instance=datatypes::SimpleType_strategy)
@settings(max_examples=50)
def test_datatypes::simpletype_instantiation(instance):
    assert isinstance(instance, datatypes::SimpleType)
