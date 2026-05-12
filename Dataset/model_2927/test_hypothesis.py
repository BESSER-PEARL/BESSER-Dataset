import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ling_Feature,
    Type,
    ling_Entity,
    ling_DataType,
    AbstractElement,
    ling_Import,
    ling_Type,
    ling_PackageDeclaration,
    ling_AbstractElement,
    ling_Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ling_feature_is_not_abstract():
    assert not inspect.isabstract(ling_Feature)


def test_ling_feature_constructor_exists():
    assert callable(ling_Feature.__init__)


def test_ling_feature_constructor_args():
    sig = inspect.signature(ling_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_ling_feature_has_many():
    assert hasattr(ling_Feature, "many")
    descriptor = None
    for klass in ling_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_ling_feature_has_name():
    assert hasattr(ling_Feature, "name")
    descriptor = None
    for klass in ling_Feature.__mro__:
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



def test_ling_entity_is_not_abstract():
    assert not inspect.isabstract(ling_Entity)


def test_ling_entity_constructor_exists():
    assert callable(ling_Entity.__init__)


def test_ling_entity_constructor_args():
    sig = inspect.signature(ling_Entity.__init__)
    params = list(sig.parameters.keys())



def test_ling_datatype_is_not_abstract():
    assert not inspect.isabstract(ling_DataType)


def test_ling_datatype_constructor_exists():
    assert callable(ling_DataType.__init__)


def test_ling_datatype_constructor_args():
    sig = inspect.signature(ling_DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ling_import_is_not_abstract():
    assert not inspect.isabstract(ling_Import)


def test_ling_import_constructor_exists():
    assert callable(ling_Import.__init__)


def test_ling_import_constructor_args():
    sig = inspect.signature(ling_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ling_import_has_importedNamespace():
    assert hasattr(ling_Import, "importedNamespace")
    descriptor = None
    for klass in ling_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ling_type_is_not_abstract():
    assert not inspect.isabstract(ling_Type)


def test_ling_type_constructor_exists():
    assert callable(ling_Type.__init__)


def test_ling_type_constructor_args():
    sig = inspect.signature(ling_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ling_type_has_name():
    assert hasattr(ling_Type, "name")
    descriptor = None
    for klass in ling_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ling_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(ling_PackageDeclaration)


def test_ling_packagedeclaration_constructor_exists():
    assert callable(ling_PackageDeclaration.__init__)


def test_ling_packagedeclaration_constructor_args():
    sig = inspect.signature(ling_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ling_packagedeclaration_has_name():
    assert hasattr(ling_PackageDeclaration, "name")
    descriptor = None
    for klass in ling_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ling_abstractelement_is_not_abstract():
    assert not inspect.isabstract(ling_AbstractElement)


def test_ling_abstractelement_constructor_exists():
    assert callable(ling_AbstractElement.__init__)


def test_ling_abstractelement_constructor_args():
    sig = inspect.signature(ling_AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ling_domainmodel_is_not_abstract():
    assert not inspect.isabstract(ling_Domainmodel)


def test_ling_domainmodel_constructor_exists():
    assert callable(ling_Domainmodel.__init__)


def test_ling_domainmodel_constructor_args():
    sig = inspect.signature(ling_Domainmodel.__init__)
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
ling_Feature_strategy = st.builds(
    ling_Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ling_Entity_strategy = st.builds(
    ling_Entity,
)
ling_DataType_strategy = st.builds(
    ling_DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
ling_Import_strategy = st.builds(
    ling_Import,
    importedNamespace=
        safe_text
)
ling_Type_strategy = st.builds(
    ling_Type,
    name=
        safe_text
)
ling_PackageDeclaration_strategy = st.builds(
    ling_PackageDeclaration,
    name=
        safe_text
)
ling_AbstractElement_strategy = st.builds(
    ling_AbstractElement,
)
ling_Domainmodel_strategy = st.builds(
    ling_Domainmodel,
)

@given(instance=ling_Feature_strategy)
@settings(max_examples=50)
def test_ling_feature_instantiation(instance):
    assert isinstance(instance, ling_Feature)



@given(instance=ling_Feature_strategy)
def test_ling_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=ling_Feature_strategy)
def test_ling_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ling_Entity_strategy)
@settings(max_examples=50)
def test_ling_entity_instantiation(instance):
    assert isinstance(instance, ling_Entity)

@given(instance=ling_DataType_strategy)
@settings(max_examples=50)
def test_ling_datatype_instantiation(instance):
    assert isinstance(instance, ling_DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=ling_Import_strategy)
@settings(max_examples=50)
def test_ling_import_instantiation(instance):
    assert isinstance(instance, ling_Import)



@given(instance=ling_Import_strategy)
def test_ling_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=ling_Type_strategy)
@settings(max_examples=50)
def test_ling_type_instantiation(instance):
    assert isinstance(instance, ling_Type)



@given(instance=ling_Type_strategy)
def test_ling_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ling_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_ling_packagedeclaration_instantiation(instance):
    assert isinstance(instance, ling_PackageDeclaration)



@given(instance=ling_PackageDeclaration_strategy)
def test_ling_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ling_AbstractElement_strategy)
@settings(max_examples=50)
def test_ling_abstractelement_instantiation(instance):
    assert isinstance(instance, ling_AbstractElement)

@given(instance=ling_Domainmodel_strategy)
@settings(max_examples=50)
def test_ling_domainmodel_instantiation(instance):
    assert isinstance(instance, ling_Domainmodel)
