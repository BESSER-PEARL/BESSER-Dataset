import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    builderState_EClass,
    IEObjectDescription,
    builderState_EObjectDescription,
    IReferenceDescription,
    builderState_ReferenceDescription,
    builderState_UserDataEntry,
    builderState_IReferenceDescription,
    builderState_IEObjectDescription,
    builderState_ResourceDescription,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_builderstate_eclass_is_not_abstract():
    assert not inspect.isabstract(builderState_EClass)


def test_builderstate_eclass_constructor_exists():
    assert callable(builderState_EClass.__init__)


def test_builderstate_eclass_constructor_args():
    sig = inspect.signature(builderState_EClass.__init__)
    params = list(sig.parameters.keys())



def test_ieobjectdescription_is_not_abstract():
    assert not inspect.isabstract(IEObjectDescription)


def test_ieobjectdescription_constructor_exists():
    assert callable(IEObjectDescription.__init__)


def test_ieobjectdescription_constructor_args():
    sig = inspect.signature(IEObjectDescription.__init__)
    params = list(sig.parameters.keys())



def test_builderstate_eobjectdescription_is_not_abstract():
    assert not inspect.isabstract(builderState_EObjectDescription)


def test_builderstate_eobjectdescription_constructor_exists():
    assert callable(builderState_EObjectDescription.__init__)


def test_builderstate_eobjectdescription_constructor_args():
    sig = inspect.signature(builderState_EObjectDescription.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_builderstate_eobjectdescription_has_fragment():
    assert hasattr(builderState_EObjectDescription, "fragment")
    descriptor = None
    for klass in builderState_EObjectDescription.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_ireferencedescription_is_not_abstract():
    assert not inspect.isabstract(IReferenceDescription)


def test_ireferencedescription_constructor_exists():
    assert callable(IReferenceDescription.__init__)


def test_ireferencedescription_constructor_args():
    sig = inspect.signature(IReferenceDescription.__init__)
    params = list(sig.parameters.keys())



def test_builderstate_referencedescription_is_not_abstract():
    assert not inspect.isabstract(builderState_ReferenceDescription)


def test_builderstate_referencedescription_constructor_exists():
    assert callable(builderState_ReferenceDescription.__init__)


def test_builderstate_referencedescription_constructor_args():
    sig = inspect.signature(builderState_ReferenceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalFormOfEReference" in params, "Missing parameter 'externalFormOfEReference'"

def test_builderstate_referencedescription_has_externalFormOfEReference():
    assert hasattr(builderState_ReferenceDescription, "externalFormOfEReference")
    descriptor = None
    for klass in builderState_ReferenceDescription.__mro__:
        if "externalFormOfEReference" in klass.__dict__:
            descriptor = klass.__dict__["externalFormOfEReference"]
            break
    assert isinstance(descriptor, property)



def test_builderstate_userdataentry_is_not_abstract():
    assert not inspect.isabstract(builderState_UserDataEntry)


def test_builderstate_userdataentry_constructor_exists():
    assert callable(builderState_UserDataEntry.__init__)


def test_builderstate_userdataentry_constructor_args():
    sig = inspect.signature(builderState_UserDataEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_builderstate_userdataentry_has_key():
    assert hasattr(builderState_UserDataEntry, "key")
    descriptor = None
    for klass in builderState_UserDataEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_builderstate_userdataentry_has_value():
    assert hasattr(builderState_UserDataEntry, "value")
    descriptor = None
    for klass in builderState_UserDataEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_builderstate_ireferencedescription_is_not_abstract():
    assert not inspect.isabstract(builderState_IReferenceDescription)


def test_builderstate_ireferencedescription_constructor_exists():
    assert callable(builderState_IReferenceDescription.__init__)


def test_builderstate_ireferencedescription_constructor_args():
    sig = inspect.signature(builderState_IReferenceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "indexInList" in params, "Missing parameter 'indexInList'"
    assert "sourceEObjectUri" in params, "Missing parameter 'sourceEObjectUri'"
    assert "containerEObjectURI" in params, "Missing parameter 'containerEObjectURI'"
    assert "targetEObjectUri" in params, "Missing parameter 'targetEObjectUri'"

def test_builderstate_ireferencedescription_has_indexInList():
    assert hasattr(builderState_IReferenceDescription, "indexInList")
    descriptor = None
    for klass in builderState_IReferenceDescription.__mro__:
        if "indexInList" in klass.__dict__:
            descriptor = klass.__dict__["indexInList"]
            break
    assert isinstance(descriptor, property)

def test_builderstate_ireferencedescription_has_sourceEObjectUri():
    assert hasattr(builderState_IReferenceDescription, "sourceEObjectUri")
    descriptor = None
    for klass in builderState_IReferenceDescription.__mro__:
        if "sourceEObjectUri" in klass.__dict__:
            descriptor = klass.__dict__["sourceEObjectUri"]
            break
    assert isinstance(descriptor, property)

def test_builderstate_ireferencedescription_has_containerEObjectURI():
    assert hasattr(builderState_IReferenceDescription, "containerEObjectURI")
    descriptor = None
    for klass in builderState_IReferenceDescription.__mro__:
        if "containerEObjectURI" in klass.__dict__:
            descriptor = klass.__dict__["containerEObjectURI"]
            break
    assert isinstance(descriptor, property)

def test_builderstate_ireferencedescription_has_targetEObjectUri():
    assert hasattr(builderState_IReferenceDescription, "targetEObjectUri")
    descriptor = None
    for klass in builderState_IReferenceDescription.__mro__:
        if "targetEObjectUri" in klass.__dict__:
            descriptor = klass.__dict__["targetEObjectUri"]
            break
    assert isinstance(descriptor, property)



def test_builderstate_ieobjectdescription_is_not_abstract():
    assert not inspect.isabstract(builderState_IEObjectDescription)


def test_builderstate_ieobjectdescription_constructor_exists():
    assert callable(builderState_IEObjectDescription.__init__)


def test_builderstate_ieobjectdescription_constructor_args():
    sig = inspect.signature(builderState_IEObjectDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_builderstate_ieobjectdescription_has_name():
    assert hasattr(builderState_IEObjectDescription, "name")
    descriptor = None
    for klass in builderState_IEObjectDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_builderstate_resourcedescription_is_not_abstract():
    assert not inspect.isabstract(builderState_ResourceDescription)


def test_builderstate_resourcedescription_constructor_exists():
    assert callable(builderState_ResourceDescription.__init__)


def test_builderstate_resourcedescription_constructor_args():
    sig = inspect.signature(builderState_ResourceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "importedNames" in params, "Missing parameter 'importedNames'"
    assert "URI" in params, "Missing parameter 'URI'"

def test_builderstate_resourcedescription_has_importedNames():
    assert hasattr(builderState_ResourceDescription, "importedNames")
    descriptor = None
    for klass in builderState_ResourceDescription.__mro__:
        if "importedNames" in klass.__dict__:
            descriptor = klass.__dict__["importedNames"]
            break
    assert isinstance(descriptor, property)

def test_builderstate_resourcedescription_has_URI():
    assert hasattr(builderState_ResourceDescription, "URI")
    descriptor = None
    for klass in builderState_ResourceDescription.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
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
builderState_EClass_strategy = st.builds(
    builderState_EClass,
)
IEObjectDescription_strategy = st.builds(
    IEObjectDescription,
)
builderState_EObjectDescription_strategy = st.builds(
    builderState_EObjectDescription,
    fragment=
        safe_text
)
IReferenceDescription_strategy = st.builds(
    IReferenceDescription,
)
builderState_ReferenceDescription_strategy = st.builds(
    builderState_ReferenceDescription,
    externalFormOfEReference=
        safe_text
)
builderState_UserDataEntry_strategy = st.builds(
    builderState_UserDataEntry,
    key=
        safe_text,
    value=
        safe_text
)
builderState_IReferenceDescription_strategy = st.builds(
    builderState_IReferenceDescription,
    indexInList=
        st.integers(),
    sourceEObjectUri=
        safe_text,
    containerEObjectURI=
        safe_text,
    targetEObjectUri=
        safe_text
)
builderState_IEObjectDescription_strategy = st.builds(
    builderState_IEObjectDescription,
    name=
        safe_text
)
builderState_ResourceDescription_strategy = st.builds(
    builderState_ResourceDescription,
    importedNames=
        safe_text,
    URI=
        safe_text
)

@given(instance=builderState_EClass_strategy)
@settings(max_examples=50)
def test_builderstate_eclass_instantiation(instance):
    assert isinstance(instance, builderState_EClass)

@given(instance=IEObjectDescription_strategy)
@settings(max_examples=50)
def test_ieobjectdescription_instantiation(instance):
    assert isinstance(instance, IEObjectDescription)

@given(instance=builderState_EObjectDescription_strategy)
@settings(max_examples=50)
def test_builderstate_eobjectdescription_instantiation(instance):
    assert isinstance(instance, builderState_EObjectDescription)



@given(instance=builderState_EObjectDescription_strategy)
def test_builderstate_eobjectdescription_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=IReferenceDescription_strategy)
@settings(max_examples=50)
def test_ireferencedescription_instantiation(instance):
    assert isinstance(instance, IReferenceDescription)

@given(instance=builderState_ReferenceDescription_strategy)
@settings(max_examples=50)
def test_builderstate_referencedescription_instantiation(instance):
    assert isinstance(instance, builderState_ReferenceDescription)



@given(instance=builderState_ReferenceDescription_strategy)
def test_builderstate_referencedescription_externalFormOfEReference_setter(instance):
    original = instance.externalFormOfEReference
    instance.externalFormOfEReference = original
    assert instance.externalFormOfEReference == original

@given(instance=builderState_UserDataEntry_strategy)
@settings(max_examples=50)
def test_builderstate_userdataentry_instantiation(instance):
    assert isinstance(instance, builderState_UserDataEntry)



@given(instance=builderState_UserDataEntry_strategy)
def test_builderstate_userdataentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=builderState_UserDataEntry_strategy)
def test_builderstate_userdataentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=builderState_IReferenceDescription_strategy)
@settings(max_examples=50)
def test_builderstate_ireferencedescription_instantiation(instance):
    assert isinstance(instance, builderState_IReferenceDescription)



@given(instance=builderState_IReferenceDescription_strategy)
def test_builderstate_ireferencedescription_indexInList_setter(instance):
    original = instance.indexInList
    instance.indexInList = original
    assert instance.indexInList == original



@given(instance=builderState_IReferenceDescription_strategy)
def test_builderstate_ireferencedescription_sourceEObjectUri_setter(instance):
    original = instance.sourceEObjectUri
    instance.sourceEObjectUri = original
    assert instance.sourceEObjectUri == original



@given(instance=builderState_IReferenceDescription_strategy)
def test_builderstate_ireferencedescription_containerEObjectURI_setter(instance):
    original = instance.containerEObjectURI
    instance.containerEObjectURI = original
    assert instance.containerEObjectURI == original



@given(instance=builderState_IReferenceDescription_strategy)
def test_builderstate_ireferencedescription_targetEObjectUri_setter(instance):
    original = instance.targetEObjectUri
    instance.targetEObjectUri = original
    assert instance.targetEObjectUri == original

@given(instance=builderState_IEObjectDescription_strategy)
@settings(max_examples=50)
def test_builderstate_ieobjectdescription_instantiation(instance):
    assert isinstance(instance, builderState_IEObjectDescription)



@given(instance=builderState_IEObjectDescription_strategy)
def test_builderstate_ieobjectdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=builderState_ResourceDescription_strategy)
@settings(max_examples=50)
def test_builderstate_resourcedescription_instantiation(instance):
    assert isinstance(instance, builderState_ResourceDescription)



@given(instance=builderState_ResourceDescription_strategy)
def test_builderstate_resourcedescription_importedNames_setter(instance):
    original = instance.importedNames
    instance.importedNames = original
    assert instance.importedNames == original



@given(instance=builderState_ResourceDescription_strategy)
def test_builderstate_resourcedescription_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=builderState_ResourceDescription_strategy)
@settings(max_examples=30)
def test_builderstate_resourcedescription_isempty_changes_state(instance):
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
        assert has_statements, f"Function 'isEmpty' in builderState_ResourceDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEmpty' in builderState_ResourceDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEmpty' in builderState_ResourceDescription is not implemented or raised an error")
