import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Organization,
    project_University,
    Person,
    project_Student,
    project_Adult,
    project_Teenager,
    project_Child,
    project_Organization,
    project_Person,
    project_Enrollment,
    project_Integer,
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



def test_project_university_is_not_abstract():
    assert not inspect.isabstract(project_University)


def test_project_university_constructor_exists():
    assert callable(project_University.__init__)


def test_project_university_constructor_args():
    sig = inspect.signature(project_University.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_project_student_is_not_abstract():
    assert not inspect.isabstract(project_Student)


def test_project_student_constructor_exists():
    assert callable(project_Student.__init__)


def test_project_student_constructor_args():
    sig = inspect.signature(project_Student.__init__)
    params = list(sig.parameters.keys())



def test_project_adult_is_not_abstract():
    assert not inspect.isabstract(project_Adult)


def test_project_adult_constructor_exists():
    assert callable(project_Adult.__init__)


def test_project_adult_constructor_args():
    sig = inspect.signature(project_Adult.__init__)
    params = list(sig.parameters.keys())



def test_project_teenager_is_not_abstract():
    assert not inspect.isabstract(project_Teenager)


def test_project_teenager_constructor_exists():
    assert callable(project_Teenager.__init__)


def test_project_teenager_constructor_args():
    sig = inspect.signature(project_Teenager.__init__)
    params = list(sig.parameters.keys())



def test_project_child_is_not_abstract():
    assert not inspect.isabstract(project_Child)


def test_project_child_constructor_exists():
    assert callable(project_Child.__init__)


def test_project_child_constructor_args():
    sig = inspect.signature(project_Child.__init__)
    params = list(sig.parameters.keys())



def test_project_organization_is_not_abstract():
    assert not inspect.isabstract(project_Organization)


def test_project_organization_constructor_exists():
    assert callable(project_Organization.__init__)


def test_project_organization_constructor_args():
    sig = inspect.signature(project_Organization.__init__)
    params = list(sig.parameters.keys())



def test_project_person_is_not_abstract():
    assert not inspect.isabstract(project_Person)


def test_project_person_constructor_exists():
    assert callable(project_Person.__init__)


def test_project_person_constructor_args():
    sig = inspect.signature(project_Person.__init__)
    params = list(sig.parameters.keys())



def test_project_enrollment_is_not_abstract():
    assert not inspect.isabstract(project_Enrollment)


def test_project_enrollment_constructor_exists():
    assert callable(project_Enrollment.__init__)


def test_project_enrollment_constructor_args():
    sig = inspect.signature(project_Enrollment.__init__)
    params = list(sig.parameters.keys())



def test_project_integer_is_not_abstract():
    assert not inspect.isabstract(project_Integer)


def test_project_integer_constructor_exists():
    assert callable(project_Integer.__init__)


def test_project_integer_constructor_args():
    sig = inspect.signature(project_Integer.__init__)
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
project_University_strategy = st.builds(
    project_University,
)
Person_strategy = st.builds(
    Person,
)
project_Student_strategy = st.builds(
    project_Student,
)
project_Adult_strategy = st.builds(
    project_Adult,
)
project_Teenager_strategy = st.builds(
    project_Teenager,
)
project_Child_strategy = st.builds(
    project_Child,
)
project_Organization_strategy = st.builds(
    project_Organization,
)
project_Person_strategy = st.builds(
    project_Person,
)
project_Enrollment_strategy = st.builds(
    project_Enrollment,
)
project_Integer_strategy = st.builds(
    project_Integer,
)

@given(instance=Organization_strategy)
@settings(max_examples=50)
def test_organization_instantiation(instance):
    assert isinstance(instance, Organization)

@given(instance=project_University_strategy)
@settings(max_examples=50)
def test_project_university_instantiation(instance):
    assert isinstance(instance, project_University)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=project_Student_strategy)
@settings(max_examples=50)
def test_project_student_instantiation(instance):
    assert isinstance(instance, project_Student)

@given(instance=project_Adult_strategy)
@settings(max_examples=50)
def test_project_adult_instantiation(instance):
    assert isinstance(instance, project_Adult)

@given(instance=project_Teenager_strategy)
@settings(max_examples=50)
def test_project_teenager_instantiation(instance):
    assert isinstance(instance, project_Teenager)

@given(instance=project_Child_strategy)
@settings(max_examples=50)
def test_project_child_instantiation(instance):
    assert isinstance(instance, project_Child)

@given(instance=project_Organization_strategy)
@settings(max_examples=50)
def test_project_organization_instantiation(instance):
    assert isinstance(instance, project_Organization)

@given(instance=project_Person_strategy)
@settings(max_examples=50)
def test_project_person_instantiation(instance):
    assert isinstance(instance, project_Person)

@given(instance=project_Enrollment_strategy)
@settings(max_examples=50)
def test_project_enrollment_instantiation(instance):
    assert isinstance(instance, project_Enrollment)

@given(instance=project_Integer_strategy)
@settings(max_examples=50)
def test_project_integer_instantiation(instance):
    assert isinstance(instance, project_Integer)
