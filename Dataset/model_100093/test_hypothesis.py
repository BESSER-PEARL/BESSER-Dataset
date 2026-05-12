import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pushbuttonbuild::EStringToStringMapEntry,
    pushbuttonbuild::DocumentRoot,
    pushbuttonbuild::ExtraZIPType,
    pushbuttonbuild::BuildType,
    JreType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pushbuttonbuild::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild::EStringToStringMapEntry)


def test_pushbuttonbuild::estringtostringmapentry_constructor_exists():
    assert callable(pushbuttonbuild::EStringToStringMapEntry.__init__)


def test_pushbuttonbuild::estringtostringmapentry_constructor_args():
    sig = inspect.signature(pushbuttonbuild::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_pushbuttonbuild::documentroot_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild::DocumentRoot)


def test_pushbuttonbuild::documentroot_constructor_exists():
    assert callable(pushbuttonbuild::DocumentRoot.__init__)


def test_pushbuttonbuild::documentroot_constructor_args():
    sig = inspect.signature(pushbuttonbuild::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_pushbuttonbuild::documentroot_has_mixed():
    assert hasattr(pushbuttonbuild::DocumentRoot, "mixed")
    descriptor = None
    for klass in pushbuttonbuild::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_pushbuttonbuild::extraziptype_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild::ExtraZIPType)


def test_pushbuttonbuild::extraziptype_constructor_exists():
    assert callable(pushbuttonbuild::ExtraZIPType.__init__)


def test_pushbuttonbuild::extraziptype_constructor_args():
    sig = inspect.signature(pushbuttonbuild::ExtraZIPType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pushbuttonbuild::extraziptype_has_name():
    assert hasattr(pushbuttonbuild::ExtraZIPType, "name")
    descriptor = None
    for klass in pushbuttonbuild::ExtraZIPType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pushbuttonbuild::buildtype_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild::BuildType)


def test_pushbuttonbuild::buildtype_constructor_exists():
    assert callable(pushbuttonbuild::BuildType.__init__)


def test_pushbuttonbuild::buildtype_constructor_args():
    sig = inspect.signature(pushbuttonbuild::BuildType.__init__)
    params = list(sig.parameters.keys())
    assert "isIncubation" in params, "Missing parameter 'isIncubation'"
    assert "newsgroupPublisherEmail" in params, "Missing parameter 'newsgroupPublisherEmail'"
    assert "jre" in params, "Missing parameter 'jre'"
    assert "newsgroupPublisherName" in params, "Missing parameter 'newsgroupPublisherName'"
    assert "projectNamespace" in params, "Missing parameter 'projectNamespace'"
    assert "testsAreJarred" in params, "Missing parameter 'testsAreJarred'"
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "parentProjectName" in params, "Missing parameter 'parentProjectName'"

def test_pushbuttonbuild::buildtype_has_isIncubation():
    assert hasattr(pushbuttonbuild::BuildType, "isIncubation")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "isIncubation" in klass.__dict__:
            descriptor = klass.__dict__["isIncubation"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_newsgroupPublisherEmail():
    assert hasattr(pushbuttonbuild::BuildType, "newsgroupPublisherEmail")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "newsgroupPublisherEmail" in klass.__dict__:
            descriptor = klass.__dict__["newsgroupPublisherEmail"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_jre():
    assert hasattr(pushbuttonbuild::BuildType, "jre")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "jre" in klass.__dict__:
            descriptor = klass.__dict__["jre"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_newsgroupPublisherName():
    assert hasattr(pushbuttonbuild::BuildType, "newsgroupPublisherName")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "newsgroupPublisherName" in klass.__dict__:
            descriptor = klass.__dict__["newsgroupPublisherName"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_projectNamespace():
    assert hasattr(pushbuttonbuild::BuildType, "projectNamespace")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "projectNamespace" in klass.__dict__:
            descriptor = klass.__dict__["projectNamespace"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_testsAreJarred():
    assert hasattr(pushbuttonbuild::BuildType, "testsAreJarred")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "testsAreJarred" in klass.__dict__:
            descriptor = klass.__dict__["testsAreJarred"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_shortName():
    assert hasattr(pushbuttonbuild::BuildType, "shortName")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild::buildtype_has_parentProjectName():
    assert hasattr(pushbuttonbuild::BuildType, "parentProjectName")
    descriptor = None
    for klass in pushbuttonbuild::BuildType.__mro__:
        if "parentProjectName" in klass.__dict__:
            descriptor = klass.__dict__["parentProjectName"]
            break
    assert isinstance(descriptor, property)

def test_jretype_exists():
    # Check that the Enumeration exists
    assert JreType is not None

def test_jretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JreType]
    expected_literals = [
        "J2SE14",
        "J2SE15",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JreType"


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
pushbuttonbuild::EStringToStringMapEntry_strategy = st.builds(
    pushbuttonbuild::EStringToStringMapEntry,
)
pushbuttonbuild::DocumentRoot_strategy = st.builds(
    pushbuttonbuild::DocumentRoot,
    mixed=
        safe_text
)
pushbuttonbuild::ExtraZIPType_strategy = st.builds(
    pushbuttonbuild::ExtraZIPType,
    name=
        safe_text
)
pushbuttonbuild::BuildType_strategy = st.builds(
    pushbuttonbuild::BuildType,
    isIncubation=
        safe_text,
    newsgroupPublisherEmail=
        safe_text,
    jre=
        safe_text,
    newsgroupPublisherName=
        safe_text,
    projectNamespace=
        safe_text,
    testsAreJarred=
        safe_text,
    shortName=
        safe_text,
    parentProjectName=
        safe_text
)

@given(instance=pushbuttonbuild::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild::EStringToStringMapEntry)

@given(instance=pushbuttonbuild::DocumentRoot_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild::documentroot_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild::DocumentRoot)

@given(instance=pushbuttonbuild::DocumentRoot_strategy)
def test_pushbuttonbuild::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=pushbuttonbuild::DocumentRoot_strategy)
def test_pushbuttonbuild::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=pushbuttonbuild::ExtraZIPType_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild::extraziptype_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild::ExtraZIPType)

@given(instance=pushbuttonbuild::ExtraZIPType_strategy)
def test_pushbuttonbuild::extraziptype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pushbuttonbuild::ExtraZIPType_strategy)
def test_pushbuttonbuild::extraziptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pushbuttonbuild::BuildType_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild::buildtype_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild::BuildType)

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_isIncubation_type(instance):
    assert isinstance(instance.isIncubation, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_isIncubation_setter(instance):
    original = instance.isIncubation
    instance.isIncubation = original
    assert instance.isIncubation == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_newsgroupPublisherEmail_type(instance):
    assert isinstance(instance.newsgroupPublisherEmail, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_newsgroupPublisherEmail_setter(instance):
    original = instance.newsgroupPublisherEmail
    instance.newsgroupPublisherEmail = original
    assert instance.newsgroupPublisherEmail == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_jre_type(instance):
    assert isinstance(instance.jre, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_jre_setter(instance):
    original = instance.jre
    instance.jre = original
    assert instance.jre == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_newsgroupPublisherName_type(instance):
    assert isinstance(instance.newsgroupPublisherName, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_newsgroupPublisherName_setter(instance):
    original = instance.newsgroupPublisherName
    instance.newsgroupPublisherName = original
    assert instance.newsgroupPublisherName == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_projectNamespace_type(instance):
    assert isinstance(instance.projectNamespace, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_projectNamespace_setter(instance):
    original = instance.projectNamespace
    instance.projectNamespace = original
    assert instance.projectNamespace == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_testsAreJarred_type(instance):
    assert isinstance(instance.testsAreJarred, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_testsAreJarred_setter(instance):
    original = instance.testsAreJarred
    instance.testsAreJarred = original
    assert instance.testsAreJarred == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_parentProjectName_type(instance):
    assert isinstance(instance.parentProjectName, str)


@given(instance=pushbuttonbuild::BuildType_strategy)
def test_pushbuttonbuild::buildtype_parentProjectName_setter(instance):
    original = instance.parentProjectName
    instance.parentProjectName = original
    assert instance.parentProjectName == original
