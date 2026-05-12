import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    domainDsl_Validator,
    domainDsl_Feature,
    Type,
    domainDsl_Entity,
    domainDsl_DataType,
    domainDsl_EType,
    AbstractElement,
    domainDsl_Type,
    domainDsl_Import,
    domainDsl_PackageDeclaration,
    domainDsl_AbstractElement,
    domainDsl_Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domaindsl_validator_is_not_abstract():
    assert not inspect.isabstract(domainDsl_Validator)


def test_domaindsl_validator_constructor_exists():
    assert callable(domainDsl_Validator.__init__)


def test_domaindsl_validator_constructor_args():
    sig = inspect.signature(domainDsl_Validator.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "svalue" in params, "Missing parameter 'svalue'"

def test_domaindsl_validator_has_value():
    assert hasattr(domainDsl_Validator, "value")
    descriptor = None
    for klass in domainDsl_Validator.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl_validator_has_name():
    assert hasattr(domainDsl_Validator, "name")
    descriptor = None
    for klass in domainDsl_Validator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl_validator_has_svalue():
    assert hasattr(domainDsl_Validator, "svalue")
    descriptor = None
    for klass in domainDsl_Validator.__mro__:
        if "svalue" in klass.__dict__:
            descriptor = klass.__dict__["svalue"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl_feature_is_not_abstract():
    assert not inspect.isabstract(domainDsl_Feature)


def test_domaindsl_feature_constructor_exists():
    assert callable(domainDsl_Feature.__init__)


def test_domaindsl_feature_constructor_args():
    sig = inspect.signature(domainDsl_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"
    assert "defaultVal" in params, "Missing parameter 'defaultVal'"

def test_domaindsl_feature_has_name():
    assert hasattr(domainDsl_Feature, "name")
    descriptor = None
    for klass in domainDsl_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl_feature_has_many():
    assert hasattr(domainDsl_Feature, "many")
    descriptor = None
    for klass in domainDsl_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl_feature_has_defaultVal():
    assert hasattr(domainDsl_Feature, "defaultVal")
    descriptor = None
    for klass in domainDsl_Feature.__mro__:
        if "defaultVal" in klass.__dict__:
            descriptor = klass.__dict__["defaultVal"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl_entity_is_not_abstract():
    assert not inspect.isabstract(domainDsl_Entity)


def test_domaindsl_entity_constructor_exists():
    assert callable(domainDsl_Entity.__init__)


def test_domaindsl_entity_constructor_args():
    sig = inspect.signature(domainDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl_datatype_is_not_abstract():
    assert not inspect.isabstract(domainDsl_DataType)


def test_domaindsl_datatype_constructor_exists():
    assert callable(domainDsl_DataType.__init__)


def test_domaindsl_datatype_constructor_args():
    sig = inspect.signature(domainDsl_DataType.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl_etype_is_not_abstract():
    assert not inspect.isabstract(domainDsl_EType)


def test_domaindsl_etype_constructor_exists():
    assert callable(domainDsl_EType.__init__)


def test_domaindsl_etype_constructor_args():
    sig = inspect.signature(domainDsl_EType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domaindsl_etype_has_name():
    assert hasattr(domainDsl_EType, "name")
    descriptor = None
    for klass in domainDsl_EType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl_type_is_not_abstract():
    assert not inspect.isabstract(domainDsl_Type)


def test_domaindsl_type_constructor_exists():
    assert callable(domainDsl_Type.__init__)


def test_domaindsl_type_constructor_args():
    sig = inspect.signature(domainDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domaindsl_type_has_name():
    assert hasattr(domainDsl_Type, "name")
    descriptor = None
    for klass in domainDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl_import_is_not_abstract():
    assert not inspect.isabstract(domainDsl_Import)


def test_domaindsl_import_constructor_exists():
    assert callable(domainDsl_Import.__init__)


def test_domaindsl_import_constructor_args():
    sig = inspect.signature(domainDsl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_domaindsl_import_has_importedNamespace():
    assert hasattr(domainDsl_Import, "importedNamespace")
    descriptor = None
    for klass in domainDsl_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainDsl_PackageDeclaration)


def test_domaindsl_packagedeclaration_constructor_exists():
    assert callable(domainDsl_PackageDeclaration.__init__)


def test_domaindsl_packagedeclaration_constructor_args():
    sig = inspect.signature(domainDsl_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domaindsl_packagedeclaration_has_name():
    assert hasattr(domainDsl_PackageDeclaration, "name")
    descriptor = None
    for klass in domainDsl_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl_abstractelement_is_not_abstract():
    assert not inspect.isabstract(domainDsl_AbstractElement)


def test_domaindsl_abstractelement_constructor_exists():
    assert callable(domainDsl_AbstractElement.__init__)


def test_domaindsl_abstractelement_constructor_args():
    sig = inspect.signature(domainDsl_AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl_domainmodel_is_not_abstract():
    assert not inspect.isabstract(domainDsl_Domainmodel)


def test_domaindsl_domainmodel_constructor_exists():
    assert callable(domainDsl_Domainmodel.__init__)


def test_domaindsl_domainmodel_constructor_args():
    sig = inspect.signature(domainDsl_Domainmodel.__init__)
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
domainDsl_Validator_strategy = st.builds(
    domainDsl_Validator,
    value=
        st.integers(),
    name=
        safe_text,
    svalue=
        safe_text
)
domainDsl_Feature_strategy = st.builds(
    domainDsl_Feature,
    name=
        safe_text,
    many=
        st.booleans(),
    defaultVal=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
domainDsl_Entity_strategy = st.builds(
    domainDsl_Entity,
)
domainDsl_DataType_strategy = st.builds(
    domainDsl_DataType,
)
domainDsl_EType_strategy = st.builds(
    domainDsl_EType,
    name=
        safe_text
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
domainDsl_Type_strategy = st.builds(
    domainDsl_Type,
    name=
        safe_text
)
domainDsl_Import_strategy = st.builds(
    domainDsl_Import,
    importedNamespace=
        safe_text
)
domainDsl_PackageDeclaration_strategy = st.builds(
    domainDsl_PackageDeclaration,
    name=
        safe_text
)
domainDsl_AbstractElement_strategy = st.builds(
    domainDsl_AbstractElement,
)
domainDsl_Domainmodel_strategy = st.builds(
    domainDsl_Domainmodel,
)

@given(instance=domainDsl_Validator_strategy)
@settings(max_examples=50)
def test_domaindsl_validator_instantiation(instance):
    assert isinstance(instance, domainDsl_Validator)



@given(instance=domainDsl_Validator_strategy)
def test_domaindsl_validator_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=domainDsl_Validator_strategy)
def test_domaindsl_validator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domainDsl_Validator_strategy)
def test_domaindsl_validator_svalue_setter(instance):
    original = instance.svalue
    instance.svalue = original
    assert instance.svalue == original

@given(instance=domainDsl_Feature_strategy)
@settings(max_examples=50)
def test_domaindsl_feature_instantiation(instance):
    assert isinstance(instance, domainDsl_Feature)



@given(instance=domainDsl_Feature_strategy)
def test_domaindsl_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domainDsl_Feature_strategy)
def test_domaindsl_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=domainDsl_Feature_strategy)
def test_domaindsl_feature_defaultVal_setter(instance):
    original = instance.defaultVal
    instance.defaultVal = original
    assert instance.defaultVal == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=domainDsl_Entity_strategy)
@settings(max_examples=50)
def test_domaindsl_entity_instantiation(instance):
    assert isinstance(instance, domainDsl_Entity)

@given(instance=domainDsl_DataType_strategy)
@settings(max_examples=50)
def test_domaindsl_datatype_instantiation(instance):
    assert isinstance(instance, domainDsl_DataType)

@given(instance=domainDsl_EType_strategy)
@settings(max_examples=50)
def test_domaindsl_etype_instantiation(instance):
    assert isinstance(instance, domainDsl_EType)



@given(instance=domainDsl_EType_strategy)
def test_domaindsl_etype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=domainDsl_Type_strategy)
@settings(max_examples=50)
def test_domaindsl_type_instantiation(instance):
    assert isinstance(instance, domainDsl_Type)



@given(instance=domainDsl_Type_strategy)
def test_domaindsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainDsl_Import_strategy)
@settings(max_examples=50)
def test_domaindsl_import_instantiation(instance):
    assert isinstance(instance, domainDsl_Import)



@given(instance=domainDsl_Import_strategy)
def test_domaindsl_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=domainDsl_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_domaindsl_packagedeclaration_instantiation(instance):
    assert isinstance(instance, domainDsl_PackageDeclaration)



@given(instance=domainDsl_PackageDeclaration_strategy)
def test_domaindsl_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainDsl_AbstractElement_strategy)
@settings(max_examples=50)
def test_domaindsl_abstractelement_instantiation(instance):
    assert isinstance(instance, domainDsl_AbstractElement)

@given(instance=domainDsl_Domainmodel_strategy)
@settings(max_examples=50)
def test_domaindsl_domainmodel_instantiation(instance):
    assert isinstance(instance, domainDsl_Domainmodel)
