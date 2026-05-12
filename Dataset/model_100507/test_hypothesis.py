import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    requirement_NamedElement,
    requirement_EObject,
    NamedElement,
    requirement_Category,
    requirement_Requirement,
    requirement_Repository,
    RequirementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirement_namedelement_is_not_abstract():
    assert not inspect.isabstract(requirement_NamedElement)


def test_requirement_namedelement_constructor_exists():
    assert callable(requirement_NamedElement.__init__)


def test_requirement_namedelement_constructor_args():
    sig = inspect.signature(requirement_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_requirement_namedelement_has_name():
    assert hasattr(requirement_NamedElement, "name")
    descriptor = None
    for klass in requirement_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_requirement_eobject_is_not_abstract():
    assert not inspect.isabstract(requirement_EObject)


def test_requirement_eobject_constructor_exists():
    assert callable(requirement_EObject.__init__)


def test_requirement_eobject_constructor_args():
    sig = inspect.signature(requirement_EObject.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_requirement_category_is_not_abstract():
    assert not inspect.isabstract(requirement_Category)


def test_requirement_category_constructor_exists():
    assert callable(requirement_Category.__init__)


def test_requirement_category_constructor_args():
    sig = inspect.signature(requirement_Category.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_requirement_category_has_id():
    assert hasattr(requirement_Category, "id")
    descriptor = None
    for klass in requirement_Category.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_requirement_requirement_is_not_abstract():
    assert not inspect.isabstract(requirement_Requirement)


def test_requirement_requirement_constructor_exists():
    assert callable(requirement_Requirement.__init__)


def test_requirement_requirement_constructor_args():
    sig = inspect.signature(requirement_Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "rationale" in params, "Missing parameter 'rationale'"
    assert "status" in params, "Missing parameter 'status'"
    assert "subtype" in params, "Missing parameter 'subtype'"
    assert "statement" in params, "Missing parameter 'statement'"
    assert "createdOn" in params, "Missing parameter 'createdOn'"
    assert "version" in params, "Missing parameter 'version'"
    assert "modifiedOn" in params, "Missing parameter 'modifiedOn'"
    assert "acceptanceCriteria" in params, "Missing parameter 'acceptanceCriteria'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_requirement_requirement_has_rationale():
    assert hasattr(requirement_Requirement, "rationale")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_status():
    assert hasattr(requirement_Requirement, "status")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_subtype():
    assert hasattr(requirement_Requirement, "subtype")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "subtype" in klass.__dict__:
            descriptor = klass.__dict__["subtype"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_statement():
    assert hasattr(requirement_Requirement, "statement")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "statement" in klass.__dict__:
            descriptor = klass.__dict__["statement"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_createdOn():
    assert hasattr(requirement_Requirement, "createdOn")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "createdOn" in klass.__dict__:
            descriptor = klass.__dict__["createdOn"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_version():
    assert hasattr(requirement_Requirement, "version")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_modifiedOn():
    assert hasattr(requirement_Requirement, "modifiedOn")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "modifiedOn" in klass.__dict__:
            descriptor = klass.__dict__["modifiedOn"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_acceptanceCriteria():
    assert hasattr(requirement_Requirement, "acceptanceCriteria")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "acceptanceCriteria" in klass.__dict__:
            descriptor = klass.__dict__["acceptanceCriteria"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_type():
    assert hasattr(requirement_Requirement, "type")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_requirement_requirement_has_id():
    assert hasattr(requirement_Requirement, "id")
    descriptor = None
    for klass in requirement_Requirement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_requirement_repository_is_not_abstract():
    assert not inspect.isabstract(requirement_Repository)


def test_requirement_repository_constructor_exists():
    assert callable(requirement_Repository.__init__)


def test_requirement_repository_constructor_args():
    sig = inspect.signature(requirement_Repository.__init__)
    params = list(sig.parameters.keys())

def test_requirementtype_exists():
    # Check that the Enumeration exists
    assert RequirementType is not None

def test_requirementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RequirementType]
    expected_literals = [
        "functional",
        "technical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RequirementType"


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
requirement_NamedElement_strategy = st.builds(
    requirement_NamedElement,
    name=
        safe_text
)
requirement_EObject_strategy = st.builds(
    requirement_EObject,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
requirement_Category_strategy = st.builds(
    requirement_Category,
    id=
        safe_text
)
requirement_Requirement_strategy = st.builds(
    requirement_Requirement,
    rationale=
        safe_text,
    status=
        safe_text,
    subtype=
        safe_text,
    statement=
        safe_text,
    createdOn=
        st.dates(),
    version=
        st.integers(),
    modifiedOn=
        st.dates(),
    acceptanceCriteria=
        safe_text,
    type=
        safe_text,
    id=
        safe_text
)
requirement_Repository_strategy = st.builds(
    requirement_Repository,
)

@given(instance=requirement_NamedElement_strategy)
@settings(max_examples=50)
def test_requirement_namedelement_instantiation(instance):
    assert isinstance(instance, requirement_NamedElement)



@given(instance=requirement_NamedElement_strategy)
def test_requirement_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=requirement_EObject_strategy)
@settings(max_examples=50)
def test_requirement_eobject_instantiation(instance):
    assert isinstance(instance, requirement_EObject)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=requirement_Category_strategy)
@settings(max_examples=50)
def test_requirement_category_instantiation(instance):
    assert isinstance(instance, requirement_Category)



@given(instance=requirement_Category_strategy)
def test_requirement_category_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=requirement_Requirement_strategy)
@settings(max_examples=50)
def test_requirement_requirement_instantiation(instance):
    assert isinstance(instance, requirement_Requirement)



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_subtype_setter(instance):
    original = instance.subtype
    instance.subtype = original
    assert instance.subtype == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_statement_setter(instance):
    original = instance.statement
    instance.statement = original
    assert instance.statement == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_createdOn_setter(instance):
    original = instance.createdOn
    instance.createdOn = original
    assert instance.createdOn == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_modifiedOn_setter(instance):
    original = instance.modifiedOn
    instance.modifiedOn = original
    assert instance.modifiedOn == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_acceptanceCriteria_setter(instance):
    original = instance.acceptanceCriteria
    instance.acceptanceCriteria = original
    assert instance.acceptanceCriteria == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=requirement_Requirement_strategy)
def test_requirement_requirement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=requirement_Repository_strategy)
@settings(max_examples=50)
def test_requirement_repository_instantiation(instance):
    assert isinstance(instance, requirement_Repository)
