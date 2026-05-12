import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractElement,
    wh_PackageDeclaration,
    wh_AbstractElement,
    wh_Wh,
    wh_Feature,
    Type,
    wh_Entity,
    wh_DataType,
    wh_Type,
    wh_Import,
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



def test_wh_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(wh_PackageDeclaration)


def test_wh_packagedeclaration_constructor_exists():
    assert callable(wh_PackageDeclaration.__init__)


def test_wh_packagedeclaration_constructor_args():
    sig = inspect.signature(wh_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh_packagedeclaration_has_name():
    assert hasattr(wh_PackageDeclaration, "name")
    descriptor = None
    for klass in wh_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh_abstractelement_is_not_abstract():
    assert not inspect.isabstract(wh_AbstractElement)


def test_wh_abstractelement_constructor_exists():
    assert callable(wh_AbstractElement.__init__)


def test_wh_abstractelement_constructor_args():
    sig = inspect.signature(wh_AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_wh_wh_is_not_abstract():
    assert not inspect.isabstract(wh_Wh)


def test_wh_wh_constructor_exists():
    assert callable(wh_Wh.__init__)


def test_wh_wh_constructor_args():
    sig = inspect.signature(wh_Wh.__init__)
    params = list(sig.parameters.keys())



def test_wh_feature_is_not_abstract():
    assert not inspect.isabstract(wh_Feature)


def test_wh_feature_constructor_exists():
    assert callable(wh_Feature.__init__)


def test_wh_feature_constructor_args():
    sig = inspect.signature(wh_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_wh_feature_has_many():
    assert hasattr(wh_Feature, "many")
    descriptor = None
    for klass in wh_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_wh_feature_has_name():
    assert hasattr(wh_Feature, "name")
    descriptor = None
    for klass in wh_Feature.__mro__:
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



def test_wh_entity_is_not_abstract():
    assert not inspect.isabstract(wh_Entity)


def test_wh_entity_constructor_exists():
    assert callable(wh_Entity.__init__)


def test_wh_entity_constructor_args():
    sig = inspect.signature(wh_Entity.__init__)
    params = list(sig.parameters.keys())



def test_wh_datatype_is_not_abstract():
    assert not inspect.isabstract(wh_DataType)


def test_wh_datatype_constructor_exists():
    assert callable(wh_DataType.__init__)


def test_wh_datatype_constructor_args():
    sig = inspect.signature(wh_DataType.__init__)
    params = list(sig.parameters.keys())



def test_wh_type_is_not_abstract():
    assert not inspect.isabstract(wh_Type)


def test_wh_type_constructor_exists():
    assert callable(wh_Type.__init__)


def test_wh_type_constructor_args():
    sig = inspect.signature(wh_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh_type_has_name():
    assert hasattr(wh_Type, "name")
    descriptor = None
    for klass in wh_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh_import_is_not_abstract():
    assert not inspect.isabstract(wh_Import)


def test_wh_import_constructor_exists():
    assert callable(wh_Import.__init__)


def test_wh_import_constructor_args():
    sig = inspect.signature(wh_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_wh_import_has_importedNamespace():
    assert hasattr(wh_Import, "importedNamespace")
    descriptor = None
    for klass in wh_Import.__mro__:
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
wh_PackageDeclaration_strategy = st.builds(
    wh_PackageDeclaration,
    name=
        safe_text
)
wh_AbstractElement_strategy = st.builds(
    wh_AbstractElement,
)
wh_Wh_strategy = st.builds(
    wh_Wh,
)
wh_Feature_strategy = st.builds(
    wh_Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
wh_Entity_strategy = st.builds(
    wh_Entity,
)
wh_DataType_strategy = st.builds(
    wh_DataType,
)
wh_Type_strategy = st.builds(
    wh_Type,
    name=
        safe_text
)
wh_Import_strategy = st.builds(
    wh_Import,
    importedNamespace=
        safe_text
)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=wh_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_wh_packagedeclaration_instantiation(instance):
    assert isinstance(instance, wh_PackageDeclaration)



@given(instance=wh_PackageDeclaration_strategy)
def test_wh_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh_AbstractElement_strategy)
@settings(max_examples=50)
def test_wh_abstractelement_instantiation(instance):
    assert isinstance(instance, wh_AbstractElement)

@given(instance=wh_Wh_strategy)
@settings(max_examples=50)
def test_wh_wh_instantiation(instance):
    assert isinstance(instance, wh_Wh)

@given(instance=wh_Feature_strategy)
@settings(max_examples=50)
def test_wh_feature_instantiation(instance):
    assert isinstance(instance, wh_Feature)



@given(instance=wh_Feature_strategy)
def test_wh_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=wh_Feature_strategy)
def test_wh_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=wh_Entity_strategy)
@settings(max_examples=50)
def test_wh_entity_instantiation(instance):
    assert isinstance(instance, wh_Entity)

@given(instance=wh_DataType_strategy)
@settings(max_examples=50)
def test_wh_datatype_instantiation(instance):
    assert isinstance(instance, wh_DataType)

@given(instance=wh_Type_strategy)
@settings(max_examples=50)
def test_wh_type_instantiation(instance):
    assert isinstance(instance, wh_Type)



@given(instance=wh_Type_strategy)
def test_wh_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh_Import_strategy)
@settings(max_examples=50)
def test_wh_import_instantiation(instance):
    assert isinstance(instance, wh_Import)



@given(instance=wh_Import_strategy)
def test_wh_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original
