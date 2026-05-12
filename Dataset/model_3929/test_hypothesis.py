import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Property,
    Type,
    myDsl_Datatype,
    myDsl_Entity,
    Element,
    myDsl_Namespace,
    myDsl_Type,
    myDsl_Import,
    myDsl_Element,
    myDsl_File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_property_is_not_abstract():
    assert not inspect.isabstract(myDsl_Property)


def test_mydsl_property_constructor_exists():
    assert callable(myDsl_Property.__init__)


def test_mydsl_property_constructor_args():
    sig = inspect.signature(myDsl_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_property_has_name():
    assert hasattr(myDsl_Property, "name")
    descriptor = None
    for klass in myDsl_Property.__mro__:
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



def test_mydsl_datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl_Datatype)


def test_mydsl_datatype_constructor_exists():
    assert callable(myDsl_Datatype.__init__)


def test_mydsl_datatype_constructor_args():
    sig = inspect.signature(myDsl_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_entity_is_not_abstract():
    assert not inspect.isabstract(myDsl_Entity)


def test_mydsl_entity_constructor_exists():
    assert callable(myDsl_Entity.__init__)


def test_mydsl_entity_constructor_args():
    sig = inspect.signature(myDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_namespace_is_not_abstract():
    assert not inspect.isabstract(myDsl_Namespace)


def test_mydsl_namespace_constructor_exists():
    assert callable(myDsl_Namespace.__init__)


def test_mydsl_namespace_constructor_args():
    sig = inspect.signature(myDsl_Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_namespace_has_name():
    assert hasattr(myDsl_Namespace, "name")
    descriptor = None
    for klass in myDsl_Namespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_mydsl_element_is_not_abstract():
    assert not inspect.isabstract(myDsl_Element)


def test_mydsl_element_constructor_exists():
    assert callable(myDsl_Element.__init__)


def test_mydsl_element_constructor_args():
    sig = inspect.signature(myDsl_Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_file_is_not_abstract():
    assert not inspect.isabstract(myDsl_File)


def test_mydsl_file_constructor_exists():
    assert callable(myDsl_File.__init__)


def test_mydsl_file_constructor_args():
    sig = inspect.signature(myDsl_File.__init__)
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
myDsl_Property_strategy = st.builds(
    myDsl_Property,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl_Datatype_strategy = st.builds(
    myDsl_Datatype,
)
myDsl_Entity_strategy = st.builds(
    myDsl_Entity,
)
Element_strategy = st.builds(
    Element,
)
myDsl_Namespace_strategy = st.builds(
    myDsl_Namespace,
    name=
        safe_text
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_Import_strategy = st.builds(
    myDsl_Import,
    importedNamespace=
        safe_text
)
myDsl_Element_strategy = st.builds(
    myDsl_Element,
)
myDsl_File_strategy = st.builds(
    myDsl_File,
)

@given(instance=myDsl_Property_strategy)
@settings(max_examples=50)
def test_mydsl_property_instantiation(instance):
    assert isinstance(instance, myDsl_Property)



@given(instance=myDsl_Property_strategy)
def test_mydsl_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl_Datatype_strategy)
@settings(max_examples=50)
def test_mydsl_datatype_instantiation(instance):
    assert isinstance(instance, myDsl_Datatype)

@given(instance=myDsl_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDsl_Entity)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=myDsl_Namespace_strategy)
@settings(max_examples=50)
def test_mydsl_namespace_instantiation(instance):
    assert isinstance(instance, myDsl_Namespace)



@given(instance=myDsl_Namespace_strategy)
def test_mydsl_namespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Import_strategy)
@settings(max_examples=50)
def test_mydsl_import_instantiation(instance):
    assert isinstance(instance, myDsl_Import)



@given(instance=myDsl_Import_strategy)
def test_mydsl_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=myDsl_Element_strategy)
@settings(max_examples=50)
def test_mydsl_element_instantiation(instance):
    assert isinstance(instance, myDsl_Element)

@given(instance=myDsl_File_strategy)
@settings(max_examples=50)
def test_mydsl_file_instantiation(instance):
    assert isinstance(instance, myDsl_File)
