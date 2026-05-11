import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    domainDsl::Validator,
    domainDsl::Feature,
    Type,
    domainDsl::Entity,
    domainDsl::DataType,
    domainDsl::EType,
    AbstractElement,
    domainDsl::Import,
    domainDsl::Type,
    domainDsl::PackageDeclaration,
    domainDsl::AbstractElement,
    domainDsl::Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domaindsl::validator_is_not_abstract():
    assert not inspect.isabstract(domainDsl::Validator)


def test_domaindsl::validator_constructor_exists():
    assert callable(domainDsl::Validator.__init__)


def test_domaindsl::validator_constructor_args():
    sig = inspect.signature(domainDsl::Validator.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "svalue" in params, "Missing parameter 'svalue'"

def test_domaindsl::validator_has_value():
    assert hasattr(domainDsl::Validator, "value")
    descriptor = None
    for klass in domainDsl::Validator.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl::validator_has_name():
    assert hasattr(domainDsl::Validator, "name")
    descriptor = None
    for klass in domainDsl::Validator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl::validator_has_svalue():
    assert hasattr(domainDsl::Validator, "svalue")
    descriptor = None
    for klass in domainDsl::Validator.__mro__:
        if "svalue" in klass.__dict__:
            descriptor = klass.__dict__["svalue"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl::feature_is_not_abstract():
    assert not inspect.isabstract(domainDsl::Feature)


def test_domaindsl::feature_constructor_exists():
    assert callable(domainDsl::Feature.__init__)


def test_domaindsl::feature_constructor_args():
    sig = inspect.signature(domainDsl::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "defaultVal" in params, "Missing parameter 'defaultVal'"
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_domaindsl::feature_has_defaultVal():
    assert hasattr(domainDsl::Feature, "defaultVal")
    descriptor = None
    for klass in domainDsl::Feature.__mro__:
        if "defaultVal" in klass.__dict__:
            descriptor = klass.__dict__["defaultVal"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl::feature_has_name():
    assert hasattr(domainDsl::Feature, "name")
    descriptor = None
    for klass in domainDsl::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domaindsl::feature_has_many():
    assert hasattr(domainDsl::Feature, "many")
    descriptor = None
    for klass in domainDsl::Feature.__mro__:
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



def test_domaindsl::entity_is_not_abstract():
    assert not inspect.isabstract(domainDsl::Entity)


def test_domaindsl::entity_constructor_exists():
    assert callable(domainDsl::Entity.__init__)


def test_domaindsl::entity_constructor_args():
    sig = inspect.signature(domainDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl::datatype_is_not_abstract():
    assert not inspect.isabstract(domainDsl::DataType)


def test_domaindsl::datatype_constructor_exists():
    assert callable(domainDsl::DataType.__init__)


def test_domaindsl::datatype_constructor_args():
    sig = inspect.signature(domainDsl::DataType.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl::etype_is_not_abstract():
    assert not inspect.isabstract(domainDsl::EType)


def test_domaindsl::etype_constructor_exists():
    assert callable(domainDsl::EType.__init__)


def test_domaindsl::etype_constructor_args():
    sig = inspect.signature(domainDsl::EType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domaindsl::etype_has_name():
    assert hasattr(domainDsl::EType, "name")
    descriptor = None
    for klass in domainDsl::EType.__mro__:
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



def test_domaindsl::import_is_not_abstract():
    assert not inspect.isabstract(domainDsl::Import)


def test_domaindsl::import_constructor_exists():
    assert callable(domainDsl::Import.__init__)


def test_domaindsl::import_constructor_args():
    sig = inspect.signature(domainDsl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_domaindsl::import_has_importedNamespace():
    assert hasattr(domainDsl::Import, "importedNamespace")
    descriptor = None
    for klass in domainDsl::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl::type_is_not_abstract():
    assert not inspect.isabstract(domainDsl::Type)


def test_domaindsl::type_constructor_exists():
    assert callable(domainDsl::Type.__init__)


def test_domaindsl::type_constructor_args():
    sig = inspect.signature(domainDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domaindsl::type_has_name():
    assert hasattr(domainDsl::Type, "name")
    descriptor = None
    for klass in domainDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainDsl::PackageDeclaration)


def test_domaindsl::packagedeclaration_constructor_exists():
    assert callable(domainDsl::PackageDeclaration.__init__)


def test_domaindsl::packagedeclaration_constructor_args():
    sig = inspect.signature(domainDsl::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domaindsl::packagedeclaration_has_name():
    assert hasattr(domainDsl::PackageDeclaration, "name")
    descriptor = None
    for klass in domainDsl::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domaindsl::abstractelement_is_not_abstract():
    assert not inspect.isabstract(domainDsl::AbstractElement)


def test_domaindsl::abstractelement_constructor_exists():
    assert callable(domainDsl::AbstractElement.__init__)


def test_domaindsl::abstractelement_constructor_args():
    sig = inspect.signature(domainDsl::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domaindsl::domainmodel_is_not_abstract():
    assert not inspect.isabstract(domainDsl::Domainmodel)


def test_domaindsl::domainmodel_constructor_exists():
    assert callable(domainDsl::Domainmodel.__init__)


def test_domaindsl::domainmodel_constructor_args():
    sig = inspect.signature(domainDsl::Domainmodel.__init__)
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
domainDsl::Validator_strategy = st.builds(
    domainDsl::Validator,
    value=
        st.integers(),
    name=
        safe_text,
    svalue=
        safe_text
)
domainDsl::Feature_strategy = st.builds(
    domainDsl::Feature,
    defaultVal=
        safe_text,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
domainDsl::Entity_strategy = st.builds(
    domainDsl::Entity,
)
domainDsl::DataType_strategy = st.builds(
    domainDsl::DataType,
)
domainDsl::EType_strategy = st.builds(
    domainDsl::EType,
    name=
        safe_text
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
domainDsl::Import_strategy = st.builds(
    domainDsl::Import,
    importedNamespace=
        safe_text
)
domainDsl::Type_strategy = st.builds(
    domainDsl::Type,
    name=
        safe_text
)
domainDsl::PackageDeclaration_strategy = st.builds(
    domainDsl::PackageDeclaration,
    name=
        safe_text
)
domainDsl::AbstractElement_strategy = st.builds(
    domainDsl::AbstractElement,
)
domainDsl::Domainmodel_strategy = st.builds(
    domainDsl::Domainmodel,
)

@given(instance=domainDsl::Validator_strategy)
@settings(max_examples=50)
def test_domaindsl::validator_instantiation(instance):
    assert isinstance(instance, domainDsl::Validator)

@given(instance=domainDsl::Validator_strategy)
def test_domaindsl::validator_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=domainDsl::Validator_strategy)
def test_domaindsl::validator_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domainDsl::Validator_strategy)
def test_domaindsl::validator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainDsl::Validator_strategy)
def test_domaindsl::validator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainDsl::Validator_strategy)
def test_domaindsl::validator_svalue_type(instance):
    assert isinstance(instance.svalue, str)


@given(instance=domainDsl::Validator_strategy)
def test_domaindsl::validator_svalue_setter(instance):
    original = instance.svalue
    instance.svalue = original
    assert instance.svalue == original

@given(instance=domainDsl::Feature_strategy)
@settings(max_examples=50)
def test_domaindsl::feature_instantiation(instance):
    assert isinstance(instance, domainDsl::Feature)

@given(instance=domainDsl::Feature_strategy)
def test_domaindsl::feature_defaultVal_type(instance):
    assert isinstance(instance.defaultVal, str)


@given(instance=domainDsl::Feature_strategy)
def test_domaindsl::feature_defaultVal_setter(instance):
    original = instance.defaultVal
    instance.defaultVal = original
    assert instance.defaultVal == original

@given(instance=domainDsl::Feature_strategy)
def test_domaindsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainDsl::Feature_strategy)
def test_domaindsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainDsl::Feature_strategy)
def test_domaindsl::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=domainDsl::Feature_strategy)
def test_domaindsl::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=domainDsl::Entity_strategy)
@settings(max_examples=50)
def test_domaindsl::entity_instantiation(instance):
    assert isinstance(instance, domainDsl::Entity)

@given(instance=domainDsl::DataType_strategy)
@settings(max_examples=50)
def test_domaindsl::datatype_instantiation(instance):
    assert isinstance(instance, domainDsl::DataType)

@given(instance=domainDsl::EType_strategy)
@settings(max_examples=50)
def test_domaindsl::etype_instantiation(instance):
    assert isinstance(instance, domainDsl::EType)

@given(instance=domainDsl::EType_strategy)
def test_domaindsl::etype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainDsl::EType_strategy)
def test_domaindsl::etype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=domainDsl::Import_strategy)
@settings(max_examples=50)
def test_domaindsl::import_instantiation(instance):
    assert isinstance(instance, domainDsl::Import)

@given(instance=domainDsl::Import_strategy)
def test_domaindsl::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=domainDsl::Import_strategy)
def test_domaindsl::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=domainDsl::Type_strategy)
@settings(max_examples=50)
def test_domaindsl::type_instantiation(instance):
    assert isinstance(instance, domainDsl::Type)

@given(instance=domainDsl::Type_strategy)
def test_domaindsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainDsl::Type_strategy)
def test_domaindsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainDsl::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_domaindsl::packagedeclaration_instantiation(instance):
    assert isinstance(instance, domainDsl::PackageDeclaration)

@given(instance=domainDsl::PackageDeclaration_strategy)
def test_domaindsl::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainDsl::PackageDeclaration_strategy)
def test_domaindsl::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainDsl::AbstractElement_strategy)
@settings(max_examples=50)
def test_domaindsl::abstractelement_instantiation(instance):
    assert isinstance(instance, domainDsl::AbstractElement)

@given(instance=domainDsl::Domainmodel_strategy)
@settings(max_examples=50)
def test_domaindsl::domainmodel_instantiation(instance):
    assert isinstance(instance, domainDsl::Domainmodel)
