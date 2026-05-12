import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Organization,
    project::University,
    Person,
    project::Teenager,
    project::Student,
    project::Adult,
    project::Child,
    project::Organization,
    project::Person,
    project::Enrollment,
    project::Integer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_organization_is_not_abstract():
    assert not inspect.isabstract(Organization)


def test_organization_constructor_exists():
    assert callable(Organization.__init__)


def test_organization_constructor_args():
    sig = inspect.signature(Organization.__init__)
    params = list(sig.parameters.keys())



def test_project::university_is_not_abstract():
    assert not inspect.isabstract(project::University)


def test_project::university_constructor_exists():
    assert callable(project::University.__init__)


def test_project::university_constructor_args():
    sig = inspect.signature(project::University.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_project::teenager_is_not_abstract():
    assert not inspect.isabstract(project::Teenager)


def test_project::teenager_constructor_exists():
    assert callable(project::Teenager.__init__)


def test_project::teenager_constructor_args():
    sig = inspect.signature(project::Teenager.__init__)
    params = list(sig.parameters.keys())



def test_project::student_is_not_abstract():
    assert not inspect.isabstract(project::Student)


def test_project::student_constructor_exists():
    assert callable(project::Student.__init__)


def test_project::student_constructor_args():
    sig = inspect.signature(project::Student.__init__)
    params = list(sig.parameters.keys())



def test_project::adult_is_not_abstract():
    assert not inspect.isabstract(project::Adult)


def test_project::adult_constructor_exists():
    assert callable(project::Adult.__init__)


def test_project::adult_constructor_args():
    sig = inspect.signature(project::Adult.__init__)
    params = list(sig.parameters.keys())



def test_project::child_is_not_abstract():
    assert not inspect.isabstract(project::Child)


def test_project::child_constructor_exists():
    assert callable(project::Child.__init__)


def test_project::child_constructor_args():
    sig = inspect.signature(project::Child.__init__)
    params = list(sig.parameters.keys())



def test_project::organization_is_not_abstract():
    assert not inspect.isabstract(project::Organization)


def test_project::organization_constructor_exists():
    assert callable(project::Organization.__init__)


def test_project::organization_constructor_args():
    sig = inspect.signature(project::Organization.__init__)
    params = list(sig.parameters.keys())



def test_project::person_is_not_abstract():
    assert not inspect.isabstract(project::Person)


def test_project::person_constructor_exists():
    assert callable(project::Person.__init__)


def test_project::person_constructor_args():
    sig = inspect.signature(project::Person.__init__)
    params = list(sig.parameters.keys())



def test_project::enrollment_is_not_abstract():
    assert not inspect.isabstract(project::Enrollment)


def test_project::enrollment_constructor_exists():
    assert callable(project::Enrollment.__init__)


def test_project::enrollment_constructor_args():
    sig = inspect.signature(project::Enrollment.__init__)
    params = list(sig.parameters.keys())



def test_project::integer_is_not_abstract():
    assert not inspect.isabstract(project::Integer)


def test_project::integer_constructor_exists():
    assert callable(project::Integer.__init__)


def test_project::integer_constructor_args():
    sig = inspect.signature(project::Integer.__init__)
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
Organization_strategy = st.builds(
    Organization,
)
project::University_strategy = st.builds(
    project::University,
)
Person_strategy = st.builds(
    Person,
)
project::Teenager_strategy = st.builds(
    project::Teenager,
)
project::Student_strategy = st.builds(
    project::Student,
)
project::Adult_strategy = st.builds(
    project::Adult,
)
project::Child_strategy = st.builds(
    project::Child,
)
project::Organization_strategy = st.builds(
    project::Organization,
)
project::Person_strategy = st.builds(
    project::Person,
)
project::Enrollment_strategy = st.builds(
    project::Enrollment,
)
project::Integer_strategy = st.builds(
    project::Integer,
)

@given(instance=Organization_strategy)
@settings(max_examples=50)
def test_organization_instantiation(instance):
    assert isinstance(instance, Organization)

@given(instance=project::University_strategy)
@settings(max_examples=50)
def test_project::university_instantiation(instance):
    assert isinstance(instance, project::University)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=project::Teenager_strategy)
@settings(max_examples=50)
def test_project::teenager_instantiation(instance):
    assert isinstance(instance, project::Teenager)

@given(instance=project::Student_strategy)
@settings(max_examples=50)
def test_project::student_instantiation(instance):
    assert isinstance(instance, project::Student)

@given(instance=project::Adult_strategy)
@settings(max_examples=50)
def test_project::adult_instantiation(instance):
    assert isinstance(instance, project::Adult)

@given(instance=project::Child_strategy)
@settings(max_examples=50)
def test_project::child_instantiation(instance):
    assert isinstance(instance, project::Child)

@given(instance=project::Organization_strategy)
@settings(max_examples=50)
def test_project::organization_instantiation(instance):
    assert isinstance(instance, project::Organization)

@given(instance=project::Person_strategy)
@settings(max_examples=50)
def test_project::person_instantiation(instance):
    assert isinstance(instance, project::Person)

@given(instance=project::Enrollment_strategy)
@settings(max_examples=50)
def test_project::enrollment_instantiation(instance):
    assert isinstance(instance, project::Enrollment)

@given(instance=project::Integer_strategy)
@settings(max_examples=50)
def test_project::integer_instantiation(instance):
    assert isinstance(instance, project::Integer)
