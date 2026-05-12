import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myTuto_Feature,
    Type,
    myTuto_Entity,
    myTuto_DataType,
    AbstractElement,
    myTuto_Import,
    myTuto_Type,
    myTuto_PackageDeclaration,
    myTuto_AbstractElement,
    myTuto_MyTuto,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mytuto_feature_is_not_abstract():
    assert not inspect.isabstract(myTuto_Feature)


def test_mytuto_feature_constructor_exists():
    assert callable(myTuto_Feature.__init__)


def test_mytuto_feature_constructor_args():
    sig = inspect.signature(myTuto_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mytuto_feature_has_many():
    assert hasattr(myTuto_Feature, "many")
    descriptor = None
    for klass in myTuto_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mytuto_feature_has_name():
    assert hasattr(myTuto_Feature, "name")
    descriptor = None
    for klass in myTuto_Feature.__mro__:
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



def test_mytuto_entity_is_not_abstract():
    assert not inspect.isabstract(myTuto_Entity)


def test_mytuto_entity_constructor_exists():
    assert callable(myTuto_Entity.__init__)


def test_mytuto_entity_constructor_args():
    sig = inspect.signature(myTuto_Entity.__init__)
    params = list(sig.parameters.keys())



def test_mytuto_datatype_is_not_abstract():
    assert not inspect.isabstract(myTuto_DataType)


def test_mytuto_datatype_constructor_exists():
    assert callable(myTuto_DataType.__init__)


def test_mytuto_datatype_constructor_args():
    sig = inspect.signature(myTuto_DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mytuto_import_is_not_abstract():
    assert not inspect.isabstract(myTuto_Import)


def test_mytuto_import_constructor_exists():
    assert callable(myTuto_Import.__init__)


def test_mytuto_import_constructor_args():
    sig = inspect.signature(myTuto_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNameSpace" in params, "Missing parameter 'importedNameSpace'"

def test_mytuto_import_has_importedNameSpace():
    assert hasattr(myTuto_Import, "importedNameSpace")
    descriptor = None
    for klass in myTuto_Import.__mro__:
        if "importedNameSpace" in klass.__dict__:
            descriptor = klass.__dict__["importedNameSpace"]
            break
    assert isinstance(descriptor, property)



def test_mytuto_type_is_not_abstract():
    assert not inspect.isabstract(myTuto_Type)


def test_mytuto_type_constructor_exists():
    assert callable(myTuto_Type.__init__)


def test_mytuto_type_constructor_args():
    sig = inspect.signature(myTuto_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytuto_type_has_name():
    assert hasattr(myTuto_Type, "name")
    descriptor = None
    for klass in myTuto_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mytuto_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(myTuto_PackageDeclaration)


def test_mytuto_packagedeclaration_constructor_exists():
    assert callable(myTuto_PackageDeclaration.__init__)


def test_mytuto_packagedeclaration_constructor_args():
    sig = inspect.signature(myTuto_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytuto_packagedeclaration_has_name():
    assert hasattr(myTuto_PackageDeclaration, "name")
    descriptor = None
    for klass in myTuto_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mytuto_abstractelement_is_not_abstract():
    assert not inspect.isabstract(myTuto_AbstractElement)


def test_mytuto_abstractelement_constructor_exists():
    assert callable(myTuto_AbstractElement.__init__)


def test_mytuto_abstractelement_constructor_args():
    sig = inspect.signature(myTuto_AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mytuto_mytuto_is_not_abstract():
    assert not inspect.isabstract(myTuto_MyTuto)


def test_mytuto_mytuto_constructor_exists():
    assert callable(myTuto_MyTuto.__init__)


def test_mytuto_mytuto_constructor_args():
    sig = inspect.signature(myTuto_MyTuto.__init__)
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
myTuto_Feature_strategy = st.builds(
    myTuto_Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myTuto_Entity_strategy = st.builds(
    myTuto_Entity,
)
myTuto_DataType_strategy = st.builds(
    myTuto_DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
myTuto_Import_strategy = st.builds(
    myTuto_Import,
    importedNameSpace=
        safe_text
)
myTuto_Type_strategy = st.builds(
    myTuto_Type,
    name=
        safe_text
)
myTuto_PackageDeclaration_strategy = st.builds(
    myTuto_PackageDeclaration,
    name=
        safe_text
)
myTuto_AbstractElement_strategy = st.builds(
    myTuto_AbstractElement,
)
myTuto_MyTuto_strategy = st.builds(
    myTuto_MyTuto,
)

@given(instance=myTuto_Feature_strategy)
@settings(max_examples=50)
def test_mytuto_feature_instantiation(instance):
    assert isinstance(instance, myTuto_Feature)



@given(instance=myTuto_Feature_strategy)
def test_mytuto_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=myTuto_Feature_strategy)
def test_mytuto_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myTuto_Entity_strategy)
@settings(max_examples=50)
def test_mytuto_entity_instantiation(instance):
    assert isinstance(instance, myTuto_Entity)

@given(instance=myTuto_DataType_strategy)
@settings(max_examples=50)
def test_mytuto_datatype_instantiation(instance):
    assert isinstance(instance, myTuto_DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=myTuto_Import_strategy)
@settings(max_examples=50)
def test_mytuto_import_instantiation(instance):
    assert isinstance(instance, myTuto_Import)



@given(instance=myTuto_Import_strategy)
def test_mytuto_import_importedNameSpace_setter(instance):
    original = instance.importedNameSpace
    instance.importedNameSpace = original
    assert instance.importedNameSpace == original

@given(instance=myTuto_Type_strategy)
@settings(max_examples=50)
def test_mytuto_type_instantiation(instance):
    assert isinstance(instance, myTuto_Type)



@given(instance=myTuto_Type_strategy)
def test_mytuto_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myTuto_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_mytuto_packagedeclaration_instantiation(instance):
    assert isinstance(instance, myTuto_PackageDeclaration)



@given(instance=myTuto_PackageDeclaration_strategy)
def test_mytuto_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myTuto_AbstractElement_strategy)
@settings(max_examples=50)
def test_mytuto_abstractelement_instantiation(instance):
    assert isinstance(instance, myTuto_AbstractElement)

@given(instance=myTuto_MyTuto_strategy)
@settings(max_examples=50)
def test_mytuto_mytuto_instantiation(instance):
    assert isinstance(instance, myTuto_MyTuto)
