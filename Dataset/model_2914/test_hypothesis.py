import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Feature,
    AbstractElement,
    myDsl_PackageDeclaration,
    myDsl_AbstractElement,
    myDsl_Model,
    myDsl_Import,
    Type,
    myDsl_Entity,
    myDsl_DataType,
    myDsl_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_feature_is_not_abstract():
    assert not inspect.isabstract(myDsl_Feature)


def test_mydsl_feature_constructor_exists():
    assert callable(myDsl_Feature.__init__)


def test_mydsl_feature_constructor_args():
    sig = inspect.signature(myDsl_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl_feature_has_name():
    assert hasattr(myDsl_Feature, "name")
    descriptor = None
    for klass in myDsl_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_feature_has_many():
    assert hasattr(myDsl_Feature, "many")
    descriptor = None
    for klass in myDsl_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_PackageDeclaration)


def test_mydsl_packagedeclaration_constructor_exists():
    assert callable(myDsl_PackageDeclaration.__init__)


def test_mydsl_packagedeclaration_constructor_args():
    sig = inspect.signature(myDsl_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_packagedeclaration_has_name():
    assert hasattr(myDsl_PackageDeclaration, "name")
    descriptor = None
    for klass in myDsl_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_abstractelement_is_not_abstract():
    assert not inspect.isabstract(myDsl_AbstractElement)


def test_mydsl_abstractelement_constructor_exists():
    assert callable(myDsl_AbstractElement.__init__)


def test_mydsl_abstractelement_constructor_args():
    sig = inspect.signature(myDsl_AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_import_is_not_abstract():
    assert not inspect.isabstract(myDsl_Import)


def test_mydsl_import_constructor_exists():
    assert callable(myDsl_Import.__init__)


def test_mydsl_import_constructor_args():
    sig = inspect.signature(myDsl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_mydsl_import_has_importedNamespace():
    assert hasattr(myDsl_Import, "importedNamespace")
    descriptor = None
    for klass in myDsl_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
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
myDsl_Feature_strategy = st.builds(
    myDsl_Feature,
    name=
        safe_text,
    many=
        st.booleans()
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
myDsl_PackageDeclaration_strategy = st.builds(
    myDsl_PackageDeclaration,
    name=
        safe_text
)
myDsl_AbstractElement_strategy = st.builds(
    myDsl_AbstractElement,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)
myDsl_Import_strategy = st.builds(
    myDsl_Import,
    importedNamespace=
        safe_text
)
Type_strategy = st.builds(
    Type,
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

@given(instance=myDsl_Feature_strategy)
@settings(max_examples=50)
def test_mydsl_feature_instantiation(instance):
    assert isinstance(instance, myDsl_Feature)



@given(instance=myDsl_Feature_strategy)
def test_mydsl_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Feature_strategy)
def test_mydsl_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=myDsl_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_mydsl_packagedeclaration_instantiation(instance):
    assert isinstance(instance, myDsl_PackageDeclaration)



@given(instance=myDsl_PackageDeclaration_strategy)
def test_mydsl_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_AbstractElement_strategy)
@settings(max_examples=50)
def test_mydsl_abstractelement_instantiation(instance):
    assert isinstance(instance, myDsl_AbstractElement)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

@given(instance=myDsl_Import_strategy)
@settings(max_examples=50)
def test_mydsl_import_instantiation(instance):
    assert isinstance(instance, myDsl_Import)



@given(instance=myDsl_Import_strategy)
def test_mydsl_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

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
