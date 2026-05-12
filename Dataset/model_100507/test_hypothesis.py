import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    requirement::NamedElement,
    requirement::EObject,
    NamedElement,
    requirement::Requirement,
    requirement::Category,
    requirement::Repository,
    RequirementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirement::namedelement_is_not_abstract():
    assert not inspect.isabstract(requirement::NamedElement)


def test_requirement::namedelement_constructor_exists():
    assert callable(requirement::NamedElement.__init__)


def test_requirement::namedelement_constructor_args():
    sig = inspect.signature(requirement::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_requirement::namedelement_has_name():
    assert hasattr(requirement::NamedElement, "name")
    descriptor = None
    for klass in requirement::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_requirement::eobject_is_not_abstract():
    assert not inspect.isabstract(requirement::EObject)


def test_requirement::eobject_constructor_exists():
    assert callable(requirement::EObject.__init__)


def test_requirement::eobject_constructor_args():
    sig = inspect.signature(requirement::EObject.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_requirement::requirement_is_not_abstract():
    assert not inspect.isabstract(requirement::Requirement)


def test_requirement::requirement_constructor_exists():
    assert callable(requirement::Requirement.__init__)


def test_requirement::requirement_constructor_args():
    sig = inspect.signature(requirement::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "modifiedOn" in params, "Missing parameter 'modifiedOn'"
    assert "statement" in params, "Missing parameter 'statement'"
    assert "status" in params, "Missing parameter 'status'"
    assert "subtype" in params, "Missing parameter 'subtype'"
    assert "version" in params, "Missing parameter 'version'"
    assert "acceptanceCriteria" in params, "Missing parameter 'acceptanceCriteria'"
    assert "createdOn" in params, "Missing parameter 'createdOn'"
    assert "rationale" in params, "Missing parameter 'rationale'"
    assert "type" in params, "Missing parameter 'type'"

def test_requirement::requirement_has_id():
    assert hasattr(requirement::Requirement, "id")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_modifiedOn():
    assert hasattr(requirement::Requirement, "modifiedOn")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "modifiedOn" in klass.__dict__:
            descriptor = klass.__dict__["modifiedOn"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_statement():
    assert hasattr(requirement::Requirement, "statement")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "statement" in klass.__dict__:
            descriptor = klass.__dict__["statement"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_status():
    assert hasattr(requirement::Requirement, "status")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_subtype():
    assert hasattr(requirement::Requirement, "subtype")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "subtype" in klass.__dict__:
            descriptor = klass.__dict__["subtype"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_version():
    assert hasattr(requirement::Requirement, "version")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_acceptanceCriteria():
    assert hasattr(requirement::Requirement, "acceptanceCriteria")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "acceptanceCriteria" in klass.__dict__:
            descriptor = klass.__dict__["acceptanceCriteria"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_createdOn():
    assert hasattr(requirement::Requirement, "createdOn")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "createdOn" in klass.__dict__:
            descriptor = klass.__dict__["createdOn"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_rationale():
    assert hasattr(requirement::Requirement, "rationale")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "rationale" in klass.__dict__:
            descriptor = klass.__dict__["rationale"]
            break
    assert isinstance(descriptor, property)

def test_requirement::requirement_has_type():
    assert hasattr(requirement::Requirement, "type")
    descriptor = None
    for klass in requirement::Requirement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_requirement::category_is_not_abstract():
    assert not inspect.isabstract(requirement::Category)


def test_requirement::category_constructor_exists():
    assert callable(requirement::Category.__init__)


def test_requirement::category_constructor_args():
    sig = inspect.signature(requirement::Category.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_requirement::category_has_id():
    assert hasattr(requirement::Category, "id")
    descriptor = None
    for klass in requirement::Category.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_requirement::repository_is_not_abstract():
    assert not inspect.isabstract(requirement::Repository)


def test_requirement::repository_constructor_exists():
    assert callable(requirement::Repository.__init__)


def test_requirement::repository_constructor_args():
    sig = inspect.signature(requirement::Repository.__init__)
    params = list(sig.parameters.keys())

def test_requirementtype_exists():
    # Check that the Enumeration exists
    assert RequirementType is not None

def test_requirementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RequirementType]
    expected_literals = [
        "technical",
        "functional",
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
requirement::NamedElement_strategy = st.builds(
    requirement::NamedElement,
    name=
        safe_text
)
requirement::EObject_strategy = st.builds(
    requirement::EObject,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
requirement::Requirement_strategy = st.builds(
    requirement::Requirement,
    id=
        safe_text,
    modifiedOn=
        st.dates(),
    statement=
        safe_text,
    status=
        safe_text,
    subtype=
        safe_text,
    version=
        st.integers(),
    acceptanceCriteria=
        safe_text,
    createdOn=
        st.dates(),
    rationale=
        safe_text,
    type=
        safe_text
)
requirement::Category_strategy = st.builds(
    requirement::Category,
    id=
        safe_text
)
requirement::Repository_strategy = st.builds(
    requirement::Repository,
)

@given(instance=requirement::NamedElement_strategy)
@settings(max_examples=50)
def test_requirement::namedelement_instantiation(instance):
    assert isinstance(instance, requirement::NamedElement)

@given(instance=requirement::NamedElement_strategy)
def test_requirement::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=requirement::NamedElement_strategy)
def test_requirement::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=requirement::EObject_strategy)
@settings(max_examples=50)
def test_requirement::eobject_instantiation(instance):
    assert isinstance(instance, requirement::EObject)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=requirement::Requirement_strategy)
@settings(max_examples=50)
def test_requirement::requirement_instantiation(instance):
    assert isinstance(instance, requirement::Requirement)

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_modifiedOn_type(instance):
    assert isinstance(instance.modifiedOn, date)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_modifiedOn_setter(instance):
    original = instance.modifiedOn
    instance.modifiedOn = original
    assert instance.modifiedOn == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_statement_type(instance):
    assert isinstance(instance.statement, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_statement_setter(instance):
    original = instance.statement
    instance.statement = original
    assert instance.statement == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_subtype_type(instance):
    assert isinstance(instance.subtype, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_subtype_setter(instance):
    original = instance.subtype
    instance.subtype = original
    assert instance.subtype == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_version_type(instance):
    assert isinstance(instance.version, int)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_acceptanceCriteria_type(instance):
    assert isinstance(instance.acceptanceCriteria, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_acceptanceCriteria_setter(instance):
    original = instance.acceptanceCriteria
    instance.acceptanceCriteria = original
    assert instance.acceptanceCriteria == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_createdOn_type(instance):
    assert isinstance(instance.createdOn, date)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_createdOn_setter(instance):
    original = instance.createdOn
    instance.createdOn = original
    assert instance.createdOn == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_rationale_type(instance):
    assert isinstance(instance.rationale, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_rationale_setter(instance):
    original = instance.rationale
    instance.rationale = original
    assert instance.rationale == original

@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=requirement::Requirement_strategy)
def test_requirement::requirement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=requirement::Category_strategy)
@settings(max_examples=50)
def test_requirement::category_instantiation(instance):
    assert isinstance(instance, requirement::Category)

@given(instance=requirement::Category_strategy)
def test_requirement::category_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=requirement::Category_strategy)
def test_requirement::category_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=requirement::Repository_strategy)
@settings(max_examples=50)
def test_requirement::repository_instantiation(instance):
    assert isinstance(instance, requirement::Repository)
