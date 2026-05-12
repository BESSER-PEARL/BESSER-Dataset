import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    aGES_Feature,
    Type,
    aGES_Entity,
    aGES_DataType,
    AbstractElement,
    aGES_Import,
    aGES_Type,
    aGES_PackageDeclaration,
    aGES_AbstractElement,
    aGES_Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ages_feature_is_not_abstract():
    assert not inspect.isabstract(aGES_Feature)


def test_ages_feature_constructor_exists():
    assert callable(aGES_Feature.__init__)


def test_ages_feature_constructor_args():
    sig = inspect.signature(aGES_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_ages_feature_has_name():
    assert hasattr(aGES_Feature, "name")
    descriptor = None
    for klass in aGES_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ages_feature_has_many():
    assert hasattr(aGES_Feature, "many")
    descriptor = None
    for klass in aGES_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ages_entity_is_not_abstract():
    assert not inspect.isabstract(aGES_Entity)


def test_ages_entity_constructor_exists():
    assert callable(aGES_Entity.__init__)


def test_ages_entity_constructor_args():
    sig = inspect.signature(aGES_Entity.__init__)
    params = list(sig.parameters.keys())



def test_ages_datatype_is_not_abstract():
    assert not inspect.isabstract(aGES_DataType)


def test_ages_datatype_constructor_exists():
    assert callable(aGES_DataType.__init__)


def test_ages_datatype_constructor_args():
    sig = inspect.signature(aGES_DataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ages_import_is_not_abstract():
    assert not inspect.isabstract(aGES_Import)


def test_ages_import_constructor_exists():
    assert callable(aGES_Import.__init__)


def test_ages_import_constructor_args():
    sig = inspect.signature(aGES_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ages_import_has_importedNamespace():
    assert hasattr(aGES_Import, "importedNamespace")
    descriptor = None
    for klass in aGES_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ages_type_is_not_abstract():
    assert not inspect.isabstract(aGES_Type)


def test_ages_type_constructor_exists():
    assert callable(aGES_Type.__init__)


def test_ages_type_constructor_args():
    sig = inspect.signature(aGES_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ages_type_has_name():
    assert hasattr(aGES_Type, "name")
    descriptor = None
    for klass in aGES_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ages_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(aGES_PackageDeclaration)


def test_ages_packagedeclaration_constructor_exists():
    assert callable(aGES_PackageDeclaration.__init__)


def test_ages_packagedeclaration_constructor_args():
    sig = inspect.signature(aGES_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ages_packagedeclaration_has_name():
    assert hasattr(aGES_PackageDeclaration, "name")
    descriptor = None
    for klass in aGES_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ages_abstractelement_is_not_abstract():
    assert not inspect.isabstract(aGES_AbstractElement)


def test_ages_abstractelement_constructor_exists():
    assert callable(aGES_AbstractElement.__init__)


def test_ages_abstractelement_constructor_args():
    sig = inspect.signature(aGES_AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_ages_domainmodel_is_not_abstract():
    assert not inspect.isabstract(aGES_Domainmodel)


def test_ages_domainmodel_constructor_exists():
    assert callable(aGES_Domainmodel.__init__)


def test_ages_domainmodel_constructor_args():
    sig = inspect.signature(aGES_Domainmodel.__init__)
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
aGES_Feature_strategy = st.builds(
    aGES_Feature,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
aGES_Entity_strategy = st.builds(
    aGES_Entity,
)
aGES_DataType_strategy = st.builds(
    aGES_DataType,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
aGES_Import_strategy = st.builds(
    aGES_Import,
    importedNamespace=
        safe_text
)
aGES_Type_strategy = st.builds(
    aGES_Type,
    name=
        safe_text
)
aGES_PackageDeclaration_strategy = st.builds(
    aGES_PackageDeclaration,
    name=
        safe_text
)
aGES_AbstractElement_strategy = st.builds(
    aGES_AbstractElement,
)
aGES_Domainmodel_strategy = st.builds(
    aGES_Domainmodel,
)

@given(instance=aGES_Feature_strategy)
@settings(max_examples=50)
def test_ages_feature_instantiation(instance):
    assert isinstance(instance, aGES_Feature)



@given(instance=aGES_Feature_strategy)
def test_ages_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aGES_Feature_strategy)
def test_ages_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=aGES_Entity_strategy)
@settings(max_examples=50)
def test_ages_entity_instantiation(instance):
    assert isinstance(instance, aGES_Entity)

@given(instance=aGES_DataType_strategy)
@settings(max_examples=50)
def test_ages_datatype_instantiation(instance):
    assert isinstance(instance, aGES_DataType)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=aGES_Import_strategy)
@settings(max_examples=50)
def test_ages_import_instantiation(instance):
    assert isinstance(instance, aGES_Import)



@given(instance=aGES_Import_strategy)
def test_ages_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=aGES_Type_strategy)
@settings(max_examples=50)
def test_ages_type_instantiation(instance):
    assert isinstance(instance, aGES_Type)



@given(instance=aGES_Type_strategy)
def test_ages_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aGES_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_ages_packagedeclaration_instantiation(instance):
    assert isinstance(instance, aGES_PackageDeclaration)



@given(instance=aGES_PackageDeclaration_strategy)
def test_ages_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aGES_AbstractElement_strategy)
@settings(max_examples=50)
def test_ages_abstractelement_instantiation(instance):
    assert isinstance(instance, aGES_AbstractElement)

@given(instance=aGES_Domainmodel_strategy)
@settings(max_examples=50)
def test_ages_domainmodel_instantiation(instance):
    assert isinstance(instance, aGES_Domainmodel)
