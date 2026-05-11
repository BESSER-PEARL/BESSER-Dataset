import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    University::UniversityManagementSystem,
    University::Exam,
    University::Person,
    University::Course,
    Person,
    University::Professor,
    University::Student,
    CourseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::universitymanagementsystem_is_not_abstract():
    assert not inspect.isabstract(University::UniversityManagementSystem)


def test_university::universitymanagementsystem_constructor_exists():
    assert callable(University::UniversityManagementSystem.__init__)


def test_university::universitymanagementsystem_constructor_args():
    sig = inspect.signature(University::UniversityManagementSystem.__init__)
    params = list(sig.parameters.keys())



def test_university::exam_is_not_abstract():
    assert not inspect.isabstract(University::Exam)


def test_university::exam_constructor_exists():
    assert callable(University::Exam.__init__)


def test_university::exam_constructor_args():
    sig = inspect.signature(University::Exam.__init__)
    params = list(sig.parameters.keys())
    assert "examID" in params, "Missing parameter 'examID'"

def test_university::exam_has_examID():
    assert hasattr(University::Exam, "examID")
    descriptor = None
    for klass in University::Exam.__mro__:
        if "examID" in klass.__dict__:
            descriptor = klass.__dict__["examID"]
            break
    assert isinstance(descriptor, property)



def test_university::person_is_not_abstract():
    assert not inspect.isabstract(University::Person)


def test_university::person_constructor_exists():
    assert callable(University::Person.__init__)


def test_university::person_constructor_args():
    sig = inspect.signature(University::Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_university::person_has_email():
    assert hasattr(University::Person, "email")
    descriptor = None
    for klass in University::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_university::person_has_name():
    assert hasattr(University::Person, "name")
    descriptor = None
    for klass in University::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::course_is_not_abstract():
    assert not inspect.isabstract(University::Course)


def test_university::course_constructor_exists():
    assert callable(University::Course.__init__)


def test_university::course_constructor_args():
    sig = inspect.signature(University::Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseType" in params, "Missing parameter 'courseType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "courseNumber" in params, "Missing parameter 'courseNumber'"

def test_university::course_has_courseType():
    assert hasattr(University::Course, "courseType")
    descriptor = None
    for klass in University::Course.__mro__:
        if "courseType" in klass.__dict__:
            descriptor = klass.__dict__["courseType"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_name():
    assert hasattr(University::Course, "name")
    descriptor = None
    for klass in University::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_courseNumber():
    assert hasattr(University::Course, "courseNumber")
    descriptor = None
    for klass in University::Course.__mro__:
        if "courseNumber" in klass.__dict__:
            descriptor = klass.__dict__["courseNumber"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_university::professor_is_not_abstract():
    assert not inspect.isabstract(University::Professor)


def test_university::professor_constructor_exists():
    assert callable(University::Professor.__init__)


def test_university::professor_constructor_args():
    sig = inspect.signature(University::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "employeeNumber" in params, "Missing parameter 'employeeNumber'"

def test_university::professor_has_employeeNumber():
    assert hasattr(University::Professor, "employeeNumber")
    descriptor = None
    for klass in University::Professor.__mro__:
        if "employeeNumber" in klass.__dict__:
            descriptor = klass.__dict__["employeeNumber"]
            break
    assert isinstance(descriptor, property)



def test_university::student_is_not_abstract():
    assert not inspect.isabstract(University::Student)


def test_university::student_constructor_exists():
    assert callable(University::Student.__init__)


def test_university::student_constructor_args():
    sig = inspect.signature(University::Student.__init__)
    params = list(sig.parameters.keys())
    assert "matriculationNumber" in params, "Missing parameter 'matriculationNumber'"

def test_university::student_has_matriculationNumber():
    assert hasattr(University::Student, "matriculationNumber")
    descriptor = None
    for klass in University::Student.__mro__:
        if "matriculationNumber" in klass.__dict__:
            descriptor = klass.__dict__["matriculationNumber"]
            break
    assert isinstance(descriptor, property)

def test_coursetype_exists():
    # Check that the Enumeration exists
    assert CourseType is not None

def test_coursetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseType]
    expected_literals = [
        "SEM",
        "PR",
        "UE",
        "VO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseType"


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
University::UniversityManagementSystem_strategy = st.builds(
    University::UniversityManagementSystem,
)
University::Exam_strategy = st.builds(
    University::Exam,
    examID=
        safe_text
)
University::Person_strategy = st.builds(
    University::Person,
    email=
        safe_text,
    name=
        safe_text
)
University::Course_strategy = st.builds(
    University::Course,
    courseType=
        safe_text,
    name=
        safe_text,
    courseNumber=
        st.integers()
)
Person_strategy = st.builds(
    Person,
)
University::Professor_strategy = st.builds(
    University::Professor,
    employeeNumber=
        st.integers()
)
University::Student_strategy = st.builds(
    University::Student,
    matriculationNumber=
        st.integers()
)

@given(instance=University::UniversityManagementSystem_strategy)
@settings(max_examples=50)
def test_university::universitymanagementsystem_instantiation(instance):
    assert isinstance(instance, University::UniversityManagementSystem)

@given(instance=University::Exam_strategy)
@settings(max_examples=50)
def test_university::exam_instantiation(instance):
    assert isinstance(instance, University::Exam)

@given(instance=University::Exam_strategy)
def test_university::exam_examID_type(instance):
    assert isinstance(instance.examID, str)


@given(instance=University::Exam_strategy)
def test_university::exam_examID_setter(instance):
    original = instance.examID
    instance.examID = original
    assert instance.examID == original

@given(instance=University::Person_strategy)
@settings(max_examples=50)
def test_university::person_instantiation(instance):
    assert isinstance(instance, University::Person)

@given(instance=University::Person_strategy)
def test_university::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=University::Person_strategy)
def test_university::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=University::Person_strategy)
def test_university::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=University::Person_strategy)
def test_university::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=University::Course_strategy)
@settings(max_examples=50)
def test_university::course_instantiation(instance):
    assert isinstance(instance, University::Course)

@given(instance=University::Course_strategy)
def test_university::course_courseType_type(instance):
    assert isinstance(instance.courseType, str)


@given(instance=University::Course_strategy)
def test_university::course_courseType_setter(instance):
    original = instance.courseType
    instance.courseType = original
    assert instance.courseType == original

@given(instance=University::Course_strategy)
def test_university::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=University::Course_strategy)
def test_university::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=University::Course_strategy)
def test_university::course_courseNumber_type(instance):
    assert isinstance(instance.courseNumber, int)


@given(instance=University::Course_strategy)
def test_university::course_courseNumber_setter(instance):
    original = instance.courseNumber
    instance.courseNumber = original
    assert instance.courseNumber == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=University::Professor_strategy)
@settings(max_examples=50)
def test_university::professor_instantiation(instance):
    assert isinstance(instance, University::Professor)

@given(instance=University::Professor_strategy)
def test_university::professor_employeeNumber_type(instance):
    assert isinstance(instance.employeeNumber, int)


@given(instance=University::Professor_strategy)
def test_university::professor_employeeNumber_setter(instance):
    original = instance.employeeNumber
    instance.employeeNumber = original
    assert instance.employeeNumber == original

@given(instance=University::Student_strategy)
@settings(max_examples=50)
def test_university::student_instantiation(instance):
    assert isinstance(instance, University::Student)

@given(instance=University::Student_strategy)
def test_university::student_matriculationNumber_type(instance):
    assert isinstance(instance.matriculationNumber, int)


@given(instance=University::Student_strategy)
def test_university::student_matriculationNumber_setter(instance):
    original = instance.matriculationNumber
    instance.matriculationNumber = original
    assert instance.matriculationNumber == original
