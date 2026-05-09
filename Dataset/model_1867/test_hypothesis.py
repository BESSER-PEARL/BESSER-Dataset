import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractElement,
    datatypes::DataTypeLibrary,
    datatypes::AbstractElement,
    datatypes::TypeModel,
    datatypes::Field,
    DataType,
    datatypes::ComplexType,
    datatypes::SimpleType,
    datatypes::DataType,
    datatypes::Import,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::datatypelibrary_is_not_abstract():
    assert not inspect.isabstract(datatypes::DataTypeLibrary)


def test_datatypes::datatypelibrary_constructor_exists():
    assert callable(datatypes::DataTypeLibrary.__init__)


def test_datatypes::datatypelibrary_constructor_args():
    sig = inspect.signature(datatypes::DataTypeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes::datatypelibrary_has_name():
    assert hasattr(datatypes::DataTypeLibrary, "name")
    descriptor = None
    for klass in datatypes::DataTypeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypes::abstractelement_is_not_abstract():
    assert not inspect.isabstract(datatypes::AbstractElement)


def test_datatypes::abstractelement_constructor_exists():
    assert callable(datatypes::AbstractElement.__init__)


def test_datatypes::abstractelement_constructor_args():
    sig = inspect.signature(datatypes::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::typemodel_is_not_abstract():
    assert not inspect.isabstract(datatypes::TypeModel)


def test_datatypes::typemodel_constructor_exists():
    assert callable(datatypes::TypeModel.__init__)


def test_datatypes::typemodel_constructor_args():
    sig = inspect.signature(datatypes::TypeModel.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::field_is_not_abstract():
    assert not inspect.isabstract(datatypes::Field)


def test_datatypes::field_constructor_exists():
    assert callable(datatypes::Field.__init__)


def test_datatypes::field_constructor_args():
    sig = inspect.signature(datatypes::Field.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_datatypes::field_has_many():
    assert hasattr(datatypes::Field, "many")
    descriptor = None
    for klass in datatypes::Field.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
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



def test_datatypes::import_is_not_abstract():
    assert not inspect.isabstract(datatypes::Import)


def test_datatypes::import_constructor_exists():
    assert callable(datatypes::Import.__init__)


def test_datatypes::import_constructor_args():
    sig = inspect.signature(datatypes::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_datatypes::import_has_importedNamespace():
    assert hasattr(datatypes::Import, "importedNamespace")
    descriptor = None
    for klass in datatypes::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
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
AbstractElement_strategy = st.builds(
    AbstractElement,
)
datatypes::DataTypeLibrary_strategy = st.builds(
    datatypes::DataTypeLibrary,
    name=
        safe_text
)
datatypes::AbstractElement_strategy = st.builds(
    datatypes::AbstractElement,
)
datatypes::TypeModel_strategy = st.builds(
    datatypes::TypeModel,
)
datatypes::Field_strategy = st.builds(
    datatypes::Field,
    many=
        st.booleans(),
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
datatypes::DataType_strategy = st.builds(
    datatypes::DataType,
    name=
        safe_text
)
datatypes::Import_strategy = st.builds(
    datatypes::Import,
    importedNamespace=
        safe_text
)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=datatypes::DataTypeLibrary_strategy)
@settings(max_examples=50)
def test_datatypes::datatypelibrary_instantiation(instance):
    assert isinstance(instance, datatypes::DataTypeLibrary)

@given(instance=datatypes::DataTypeLibrary_strategy)
def test_datatypes::datatypelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatypes::DataTypeLibrary_strategy)
def test_datatypes::datatypelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datatypes::AbstractElement_strategy)
@settings(max_examples=50)
def test_datatypes::abstractelement_instantiation(instance):
    assert isinstance(instance, datatypes::AbstractElement)

@given(instance=datatypes::TypeModel_strategy)
@settings(max_examples=50)
def test_datatypes::typemodel_instantiation(instance):
    assert isinstance(instance, datatypes::TypeModel)

@given(instance=datatypes::Field_strategy)
@settings(max_examples=50)
def test_datatypes::field_instantiation(instance):
    assert isinstance(instance, datatypes::Field)

@given(instance=datatypes::Field_strategy)
def test_datatypes::field_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=datatypes::Field_strategy)
def test_datatypes::field_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=datatypes::Field_strategy)
def test_datatypes::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatypes::Field_strategy)
def test_datatypes::field_name_setter(instance):
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

@given(instance=datatypes::Import_strategy)
@settings(max_examples=50)
def test_datatypes::import_instantiation(instance):
    assert isinstance(instance, datatypes::Import)

@given(instance=datatypes::Import_strategy)
def test_datatypes::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=datatypes::Import_strategy)
def test_datatypes::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original
