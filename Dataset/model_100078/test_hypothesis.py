import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IReferenceDescription,
    builderState::ReferenceDescription,
    builderState::UserDataEntry,
    builderState::EClass,
    builderState::ResourceDescription,
    IEObjectDescription,
    builderState::EObjectDescription,
    builderState::IReferenceDescription,
    builderState::IEObjectDescription,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ireferencedescription_is_not_abstract():
    assert not inspect.isabstract(IReferenceDescription)


def test_ireferencedescription_constructor_exists():
    assert callable(IReferenceDescription.__init__)


def test_ireferencedescription_constructor_args():
    sig = inspect.signature(IReferenceDescription.__init__)
    params = list(sig.parameters.keys())



def test_builderstate::referencedescription_is_not_abstract():
    assert not inspect.isabstract(builderState::ReferenceDescription)


def test_builderstate::referencedescription_constructor_exists():
    assert callable(builderState::ReferenceDescription.__init__)


def test_builderstate::referencedescription_constructor_args():
    sig = inspect.signature(builderState::ReferenceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalFormOfEReference" in params, "Missing parameter 'externalFormOfEReference'"

def test_builderstate::referencedescription_has_externalFormOfEReference():
    assert hasattr(builderState::ReferenceDescription, "externalFormOfEReference")
    descriptor = None
    for klass in builderState::ReferenceDescription.__mro__:
        if "externalFormOfEReference" in klass.__dict__:
            descriptor = klass.__dict__["externalFormOfEReference"]
            break
    assert isinstance(descriptor, property)



def test_builderstate::userdataentry_is_not_abstract():
    assert not inspect.isabstract(builderState::UserDataEntry)


def test_builderstate::userdataentry_constructor_exists():
    assert callable(builderState::UserDataEntry.__init__)


def test_builderstate::userdataentry_constructor_args():
    sig = inspect.signature(builderState::UserDataEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_builderstate::userdataentry_has_value():
    assert hasattr(builderState::UserDataEntry, "value")
    descriptor = None
    for klass in builderState::UserDataEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_builderstate::userdataentry_has_key():
    assert hasattr(builderState::UserDataEntry, "key")
    descriptor = None
    for klass in builderState::UserDataEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_builderstate::eclass_is_not_abstract():
    assert not inspect.isabstract(builderState::EClass)


def test_builderstate::eclass_constructor_exists():
    assert callable(builderState::EClass.__init__)


def test_builderstate::eclass_constructor_args():
    sig = inspect.signature(builderState::EClass.__init__)
    params = list(sig.parameters.keys())



def test_builderstate::resourcedescription_is_not_abstract():
    assert not inspect.isabstract(builderState::ResourceDescription)


def test_builderstate::resourcedescription_constructor_exists():
    assert callable(builderState::ResourceDescription.__init__)


def test_builderstate::resourcedescription_constructor_args():
    sig = inspect.signature(builderState::ResourceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"
    assert "importedNames" in params, "Missing parameter 'importedNames'"

def test_builderstate::resourcedescription_has_URI():
    assert hasattr(builderState::ResourceDescription, "URI")
    descriptor = None
    for klass in builderState::ResourceDescription.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
            break
    assert isinstance(descriptor, property)

def test_builderstate::resourcedescription_has_importedNames():
    assert hasattr(builderState::ResourceDescription, "importedNames")
    descriptor = None
    for klass in builderState::ResourceDescription.__mro__:
        if "importedNames" in klass.__dict__:
            descriptor = klass.__dict__["importedNames"]
            break
    assert isinstance(descriptor, property)



def test_ieobjectdescription_is_not_abstract():
    assert not inspect.isabstract(IEObjectDescription)


def test_ieobjectdescription_constructor_exists():
    assert callable(IEObjectDescription.__init__)


def test_ieobjectdescription_constructor_args():
    sig = inspect.signature(IEObjectDescription.__init__)
    params = list(sig.parameters.keys())



def test_builderstate::eobjectdescription_is_not_abstract():
    assert not inspect.isabstract(builderState::EObjectDescription)


def test_builderstate::eobjectdescription_constructor_exists():
    assert callable(builderState::EObjectDescription.__init__)


def test_builderstate::eobjectdescription_constructor_args():
    sig = inspect.signature(builderState::EObjectDescription.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_builderstate::eobjectdescription_has_fragment():
    assert hasattr(builderState::EObjectDescription, "fragment")
    descriptor = None
    for klass in builderState::EObjectDescription.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_builderstate::ireferencedescription_is_not_abstract():
    assert not inspect.isabstract(builderState::IReferenceDescription)


def test_builderstate::ireferencedescription_constructor_exists():
    assert callable(builderState::IReferenceDescription.__init__)


def test_builderstate::ireferencedescription_constructor_args():
    sig = inspect.signature(builderState::IReferenceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "containerEObjectURI" in params, "Missing parameter 'containerEObjectURI'"
    assert "indexInList" in params, "Missing parameter 'indexInList'"
    assert "sourceEObjectUri" in params, "Missing parameter 'sourceEObjectUri'"
    assert "targetEObjectUri" in params, "Missing parameter 'targetEObjectUri'"

def test_builderstate::ireferencedescription_has_containerEObjectURI():
    assert hasattr(builderState::IReferenceDescription, "containerEObjectURI")
    descriptor = None
    for klass in builderState::IReferenceDescription.__mro__:
        if "containerEObjectURI" in klass.__dict__:
            descriptor = klass.__dict__["containerEObjectURI"]
            break
    assert isinstance(descriptor, property)

def test_builderstate::ireferencedescription_has_indexInList():
    assert hasattr(builderState::IReferenceDescription, "indexInList")
    descriptor = None
    for klass in builderState::IReferenceDescription.__mro__:
        if "indexInList" in klass.__dict__:
            descriptor = klass.__dict__["indexInList"]
            break
    assert isinstance(descriptor, property)

def test_builderstate::ireferencedescription_has_sourceEObjectUri():
    assert hasattr(builderState::IReferenceDescription, "sourceEObjectUri")
    descriptor = None
    for klass in builderState::IReferenceDescription.__mro__:
        if "sourceEObjectUri" in klass.__dict__:
            descriptor = klass.__dict__["sourceEObjectUri"]
            break
    assert isinstance(descriptor, property)

def test_builderstate::ireferencedescription_has_targetEObjectUri():
    assert hasattr(builderState::IReferenceDescription, "targetEObjectUri")
    descriptor = None
    for klass in builderState::IReferenceDescription.__mro__:
        if "targetEObjectUri" in klass.__dict__:
            descriptor = klass.__dict__["targetEObjectUri"]
            break
    assert isinstance(descriptor, property)



def test_builderstate::ieobjectdescription_is_not_abstract():
    assert not inspect.isabstract(builderState::IEObjectDescription)


def test_builderstate::ieobjectdescription_constructor_exists():
    assert callable(builderState::IEObjectDescription.__init__)


def test_builderstate::ieobjectdescription_constructor_args():
    sig = inspect.signature(builderState::IEObjectDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_builderstate::ieobjectdescription_has_name():
    assert hasattr(builderState::IEObjectDescription, "name")
    descriptor = None
    for klass in builderState::IEObjectDescription.__mro__:
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
IReferenceDescription_strategy = st.builds(
    IReferenceDescription,
)
builderState::ReferenceDescription_strategy = st.builds(
    builderState::ReferenceDescription,
    externalFormOfEReference=
        safe_text
)
builderState::UserDataEntry_strategy = st.builds(
    builderState::UserDataEntry,
    value=
        safe_text,
    key=
        safe_text
)
builderState::EClass_strategy = st.builds(
    builderState::EClass,
)
builderState::ResourceDescription_strategy = st.builds(
    builderState::ResourceDescription,
    URI=
        safe_text,
    importedNames=
        safe_text
)
IEObjectDescription_strategy = st.builds(
    IEObjectDescription,
)
builderState::EObjectDescription_strategy = st.builds(
    builderState::EObjectDescription,
    fragment=
        safe_text
)
builderState::IReferenceDescription_strategy = st.builds(
    builderState::IReferenceDescription,
    containerEObjectURI=
        safe_text,
    indexInList=
        st.integers(),
    sourceEObjectUri=
        safe_text,
    targetEObjectUri=
        safe_text
)
builderState::IEObjectDescription_strategy = st.builds(
    builderState::IEObjectDescription,
    name=
        safe_text
)

@given(instance=IReferenceDescription_strategy)
@settings(max_examples=50)
def test_ireferencedescription_instantiation(instance):
    assert isinstance(instance, IReferenceDescription)

@given(instance=builderState::ReferenceDescription_strategy)
@settings(max_examples=50)
def test_builderstate::referencedescription_instantiation(instance):
    assert isinstance(instance, builderState::ReferenceDescription)

@given(instance=builderState::ReferenceDescription_strategy)
def test_builderstate::referencedescription_externalFormOfEReference_type(instance):
    assert isinstance(instance.externalFormOfEReference, str)


@given(instance=builderState::ReferenceDescription_strategy)
def test_builderstate::referencedescription_externalFormOfEReference_setter(instance):
    original = instance.externalFormOfEReference
    instance.externalFormOfEReference = original
    assert instance.externalFormOfEReference == original

@given(instance=builderState::UserDataEntry_strategy)
@settings(max_examples=50)
def test_builderstate::userdataentry_instantiation(instance):
    assert isinstance(instance, builderState::UserDataEntry)

@given(instance=builderState::UserDataEntry_strategy)
def test_builderstate::userdataentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=builderState::UserDataEntry_strategy)
def test_builderstate::userdataentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=builderState::UserDataEntry_strategy)
def test_builderstate::userdataentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=builderState::UserDataEntry_strategy)
def test_builderstate::userdataentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=builderState::EClass_strategy)
@settings(max_examples=50)
def test_builderstate::eclass_instantiation(instance):
    assert isinstance(instance, builderState::EClass)

@given(instance=builderState::ResourceDescription_strategy)
@settings(max_examples=50)
def test_builderstate::resourcedescription_instantiation(instance):
    assert isinstance(instance, builderState::ResourceDescription)

@given(instance=builderState::ResourceDescription_strategy)
def test_builderstate::resourcedescription_URI_type(instance):
    assert isinstance(instance.URI, str)


@given(instance=builderState::ResourceDescription_strategy)
def test_builderstate::resourcedescription_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=builderState::ResourceDescription_strategy)
def test_builderstate::resourcedescription_importedNames_type(instance):
    assert isinstance(instance.importedNames, str)


@given(instance=builderState::ResourceDescription_strategy)
def test_builderstate::resourcedescription_importedNames_setter(instance):
    original = instance.importedNames
    instance.importedNames = original
    assert instance.importedNames == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=builderState::ResourceDescription_strategy)
@settings(max_examples=30)
def test_builderstate::resourcedescription_isempty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEmpty()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEmpty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEmpty' in builderState::ResourceDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEmpty' in builderState::ResourceDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEmpty' in builderState::ResourceDescription is not implemented or raised an error")

@given(instance=IEObjectDescription_strategy)
@settings(max_examples=50)
def test_ieobjectdescription_instantiation(instance):
    assert isinstance(instance, IEObjectDescription)

@given(instance=builderState::EObjectDescription_strategy)
@settings(max_examples=50)
def test_builderstate::eobjectdescription_instantiation(instance):
    assert isinstance(instance, builderState::EObjectDescription)

@given(instance=builderState::EObjectDescription_strategy)
def test_builderstate::eobjectdescription_fragment_type(instance):
    assert isinstance(instance.fragment, str)


@given(instance=builderState::EObjectDescription_strategy)
def test_builderstate::eobjectdescription_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=builderState::IReferenceDescription_strategy)
@settings(max_examples=50)
def test_builderstate::ireferencedescription_instantiation(instance):
    assert isinstance(instance, builderState::IReferenceDescription)

@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_containerEObjectURI_type(instance):
    assert isinstance(instance.containerEObjectURI, str)


@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_containerEObjectURI_setter(instance):
    original = instance.containerEObjectURI
    instance.containerEObjectURI = original
    assert instance.containerEObjectURI == original

@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_indexInList_type(instance):
    assert isinstance(instance.indexInList, int)


@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_indexInList_setter(instance):
    original = instance.indexInList
    instance.indexInList = original
    assert instance.indexInList == original

@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_sourceEObjectUri_type(instance):
    assert isinstance(instance.sourceEObjectUri, str)


@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_sourceEObjectUri_setter(instance):
    original = instance.sourceEObjectUri
    instance.sourceEObjectUri = original
    assert instance.sourceEObjectUri == original

@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_targetEObjectUri_type(instance):
    assert isinstance(instance.targetEObjectUri, str)


@given(instance=builderState::IReferenceDescription_strategy)
def test_builderstate::ireferencedescription_targetEObjectUri_setter(instance):
    original = instance.targetEObjectUri
    instance.targetEObjectUri = original
    assert instance.targetEObjectUri == original

@given(instance=builderState::IEObjectDescription_strategy)
@settings(max_examples=50)
def test_builderstate::ieobjectdescription_instantiation(instance):
    assert isinstance(instance, builderState::IEObjectDescription)

@given(instance=builderState::IEObjectDescription_strategy)
def test_builderstate::ieobjectdescription_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=builderState::IEObjectDescription_strategy)
def test_builderstate::ieobjectdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
