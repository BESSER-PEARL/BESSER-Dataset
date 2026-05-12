import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pushbuttonbuild_EStringToStringMapEntry,
    pushbuttonbuild_DocumentRoot,
    pushbuttonbuild_ExtraZIPType,
    pushbuttonbuild_BuildType,
    JreType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pushbuttonbuild_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild_EStringToStringMapEntry)


def test_pushbuttonbuild_estringtostringmapentry_constructor_exists():
    assert callable(pushbuttonbuild_EStringToStringMapEntry.__init__)


def test_pushbuttonbuild_estringtostringmapentry_constructor_args():
    sig = inspect.signature(pushbuttonbuild_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_pushbuttonbuild_documentroot_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild_DocumentRoot)


def test_pushbuttonbuild_documentroot_constructor_exists():
    assert callable(pushbuttonbuild_DocumentRoot.__init__)


def test_pushbuttonbuild_documentroot_constructor_args():
    sig = inspect.signature(pushbuttonbuild_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_pushbuttonbuild_documentroot_has_mixed():
    assert hasattr(pushbuttonbuild_DocumentRoot, "mixed")
    descriptor = None
    for klass in pushbuttonbuild_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_pushbuttonbuild_extraziptype_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild_ExtraZIPType)


def test_pushbuttonbuild_extraziptype_constructor_exists():
    assert callable(pushbuttonbuild_ExtraZIPType.__init__)


def test_pushbuttonbuild_extraziptype_constructor_args():
    sig = inspect.signature(pushbuttonbuild_ExtraZIPType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pushbuttonbuild_extraziptype_has_name():
    assert hasattr(pushbuttonbuild_ExtraZIPType, "name")
    descriptor = None
    for klass in pushbuttonbuild_ExtraZIPType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pushbuttonbuild_buildtype_is_not_abstract():
    assert not inspect.isabstract(pushbuttonbuild_BuildType)


def test_pushbuttonbuild_buildtype_constructor_exists():
    assert callable(pushbuttonbuild_BuildType.__init__)


def test_pushbuttonbuild_buildtype_constructor_args():
    sig = inspect.signature(pushbuttonbuild_BuildType.__init__)
    params = list(sig.parameters.keys())
    assert "newsgroupPublisherEmail" in params, "Missing parameter 'newsgroupPublisherEmail'"
    assert "testsAreJarred" in params, "Missing parameter 'testsAreJarred'"
    assert "parentProjectName" in params, "Missing parameter 'parentProjectName'"
    assert "jre" in params, "Missing parameter 'jre'"
    assert "isIncubation" in params, "Missing parameter 'isIncubation'"
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "projectNamespace" in params, "Missing parameter 'projectNamespace'"
    assert "newsgroupPublisherName" in params, "Missing parameter 'newsgroupPublisherName'"

def test_pushbuttonbuild_buildtype_has_newsgroupPublisherEmail():
    assert hasattr(pushbuttonbuild_BuildType, "newsgroupPublisherEmail")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "newsgroupPublisherEmail" in klass.__dict__:
            descriptor = klass.__dict__["newsgroupPublisherEmail"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_testsAreJarred():
    assert hasattr(pushbuttonbuild_BuildType, "testsAreJarred")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "testsAreJarred" in klass.__dict__:
            descriptor = klass.__dict__["testsAreJarred"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_parentProjectName():
    assert hasattr(pushbuttonbuild_BuildType, "parentProjectName")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "parentProjectName" in klass.__dict__:
            descriptor = klass.__dict__["parentProjectName"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_jre():
    assert hasattr(pushbuttonbuild_BuildType, "jre")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "jre" in klass.__dict__:
            descriptor = klass.__dict__["jre"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_isIncubation():
    assert hasattr(pushbuttonbuild_BuildType, "isIncubation")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "isIncubation" in klass.__dict__:
            descriptor = klass.__dict__["isIncubation"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_shortName():
    assert hasattr(pushbuttonbuild_BuildType, "shortName")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_projectNamespace():
    assert hasattr(pushbuttonbuild_BuildType, "projectNamespace")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "projectNamespace" in klass.__dict__:
            descriptor = klass.__dict__["projectNamespace"]
            break
    assert isinstance(descriptor, property)

def test_pushbuttonbuild_buildtype_has_newsgroupPublisherName():
    assert hasattr(pushbuttonbuild_BuildType, "newsgroupPublisherName")
    descriptor = None
    for klass in pushbuttonbuild_BuildType.__mro__:
        if "newsgroupPublisherName" in klass.__dict__:
            descriptor = klass.__dict__["newsgroupPublisherName"]
            break
    assert isinstance(descriptor, property)

def test_jretype_exists():
    # Check that the Enumeration exists
    assert JreType is not None

def test_jretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JreType]
    expected_literals = [
        "J2SE15",
        "J2SE14",
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
pushbuttonbuild_EStringToStringMapEntry_strategy = st.builds(
    pushbuttonbuild_EStringToStringMapEntry,
)
pushbuttonbuild_DocumentRoot_strategy = st.builds(
    pushbuttonbuild_DocumentRoot,
    mixed=
        safe_text
)
pushbuttonbuild_ExtraZIPType_strategy = st.builds(
    pushbuttonbuild_ExtraZIPType,
    name=
        safe_text
)
pushbuttonbuild_BuildType_strategy = st.builds(
    pushbuttonbuild_BuildType,
    newsgroupPublisherEmail=
        safe_text,
    testsAreJarred=
        safe_text,
    parentProjectName=
        safe_text,
    jre=
        safe_text,
    isIncubation=
        safe_text,
    shortName=
        safe_text,
    projectNamespace=
        safe_text,
    newsgroupPublisherName=
        safe_text
)

@given(instance=pushbuttonbuild_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild_EStringToStringMapEntry)

@given(instance=pushbuttonbuild_DocumentRoot_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild_documentroot_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild_DocumentRoot)



@given(instance=pushbuttonbuild_DocumentRoot_strategy)
def test_pushbuttonbuild_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=pushbuttonbuild_ExtraZIPType_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild_extraziptype_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild_ExtraZIPType)



@given(instance=pushbuttonbuild_ExtraZIPType_strategy)
def test_pushbuttonbuild_extraziptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pushbuttonbuild_BuildType_strategy)
@settings(max_examples=50)
def test_pushbuttonbuild_buildtype_instantiation(instance):
    assert isinstance(instance, pushbuttonbuild_BuildType)



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_newsgroupPublisherEmail_setter(instance):
    original = instance.newsgroupPublisherEmail
    instance.newsgroupPublisherEmail = original
    assert instance.newsgroupPublisherEmail == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_testsAreJarred_setter(instance):
    original = instance.testsAreJarred
    instance.testsAreJarred = original
    assert instance.testsAreJarred == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_parentProjectName_setter(instance):
    original = instance.parentProjectName
    instance.parentProjectName = original
    assert instance.parentProjectName == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_jre_setter(instance):
    original = instance.jre
    instance.jre = original
    assert instance.jre == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_isIncubation_setter(instance):
    original = instance.isIncubation
    instance.isIncubation = original
    assert instance.isIncubation == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_projectNamespace_setter(instance):
    original = instance.projectNamespace
    instance.projectNamespace = original
    assert instance.projectNamespace == original



@given(instance=pushbuttonbuild_BuildType_strategy)
def test_pushbuttonbuild_buildtype_newsgroupPublisherName_setter(instance):
    original = instance.newsgroupPublisherName
    instance.newsgroupPublisherName = original
    assert instance.newsgroupPublisherName == original
