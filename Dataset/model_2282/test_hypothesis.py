import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dmm::Person,
    dmm::UniversityManagementSystem,
    dmm::Exam,
    dmm::Course,
    Person,
    dmm::Professor,
    dmm::Student,
    CourseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dmm::person_is_not_abstract():
    assert not inspect.isabstract(dmm::Person)


def test_dmm::person_constructor_exists():
    assert callable(dmm::Person.__init__)


def test_dmm::person_constructor_args():
    sig = inspect.signature(dmm::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"

def test_dmm::person_has_name():
    assert hasattr(dmm::Person, "name")
    descriptor = None
    for klass in dmm::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dmm::person_has_email():
    assert hasattr(dmm::Person, "email")
    descriptor = None
    for klass in dmm::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_dmm::universitymanagementsystem_is_not_abstract():
    assert not inspect.isabstract(dmm::UniversityManagementSystem)


def test_dmm::universitymanagementsystem_constructor_exists():
    assert callable(dmm::UniversityManagementSystem.__init__)


def test_dmm::universitymanagementsystem_constructor_args():
    sig = inspect.signature(dmm::UniversityManagementSystem.__init__)
    params = list(sig.parameters.keys())



def test_dmm::exam_is_not_abstract():
    assert not inspect.isabstract(dmm::Exam)


def test_dmm::exam_constructor_exists():
    assert callable(dmm::Exam.__init__)


def test_dmm::exam_constructor_args():
    sig = inspect.signature(dmm::Exam.__init__)
    params = list(sig.parameters.keys())
    assert "examID" in params, "Missing parameter 'examID'"

def test_dmm::exam_has_examID():
    assert hasattr(dmm::Exam, "examID")
    descriptor = None
    for klass in dmm::Exam.__mro__:
        if "examID" in klass.__dict__:
            descriptor = klass.__dict__["examID"]
            break
    assert isinstance(descriptor, property)



def test_dmm::course_is_not_abstract():
    assert not inspect.isabstract(dmm::Course)


def test_dmm::course_constructor_exists():
    assert callable(dmm::Course.__init__)


def test_dmm::course_constructor_args():
    sig = inspect.signature(dmm::Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseType" in params, "Missing parameter 'courseType'"
    assert "courseNumber" in params, "Missing parameter 'courseNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_dmm::course_has_courseType():
    assert hasattr(dmm::Course, "courseType")
    descriptor = None
    for klass in dmm::Course.__mro__:
        if "courseType" in klass.__dict__:
            descriptor = klass.__dict__["courseType"]
            break
    assert isinstance(descriptor, property)

def test_dmm::course_has_courseNumber():
    assert hasattr(dmm::Course, "courseNumber")
    descriptor = None
    for klass in dmm::Course.__mro__:
        if "courseNumber" in klass.__dict__:
            descriptor = klass.__dict__["courseNumber"]
            break
    assert isinstance(descriptor, property)

def test_dmm::course_has_name():
    assert hasattr(dmm::Course, "name")
    descriptor = None
    for klass in dmm::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_dmm::professor_is_not_abstract():
    assert not inspect.isabstract(dmm::Professor)


def test_dmm::professor_constructor_exists():
    assert callable(dmm::Professor.__init__)


def test_dmm::professor_constructor_args():
    sig = inspect.signature(dmm::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "employeeNumber" in params, "Missing parameter 'employeeNumber'"

def test_dmm::professor_has_employeeNumber():
    assert hasattr(dmm::Professor, "employeeNumber")
    descriptor = None
    for klass in dmm::Professor.__mro__:
        if "employeeNumber" in klass.__dict__:
            descriptor = klass.__dict__["employeeNumber"]
            break
    assert isinstance(descriptor, property)



def test_dmm::student_is_not_abstract():
    assert not inspect.isabstract(dmm::Student)


def test_dmm::student_constructor_exists():
    assert callable(dmm::Student.__init__)


def test_dmm::student_constructor_args():
    sig = inspect.signature(dmm::Student.__init__)
    params = list(sig.parameters.keys())
    assert "matriculationNumber" in params, "Missing parameter 'matriculationNumber'"

def test_dmm::student_has_matriculationNumber():
    assert hasattr(dmm::Student, "matriculationNumber")
    descriptor = None
    for klass in dmm::Student.__mro__:
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
        "VO",
        "UE",
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
dmm::Person_strategy = st.builds(
    dmm::Person,
    name=
        safe_text,
    email=
        safe_text
)
dmm::UniversityManagementSystem_strategy = st.builds(
    dmm::UniversityManagementSystem,
)
dmm::Exam_strategy = st.builds(
    dmm::Exam,
    examID=
        safe_text
)
dmm::Course_strategy = st.builds(
    dmm::Course,
    courseType=
        safe_text,
    courseNumber=
        st.integers(),
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
dmm::Professor_strategy = st.builds(
    dmm::Professor,
    employeeNumber=
        st.integers()
)
dmm::Student_strategy = st.builds(
    dmm::Student,
    matriculationNumber=
        st.integers()
)

@given(instance=dmm::Person_strategy)
@settings(max_examples=50)
def test_dmm::person_instantiation(instance):
    assert isinstance(instance, dmm::Person)

@given(instance=dmm::Person_strategy)
def test_dmm::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dmm::Person_strategy)
def test_dmm::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dmm::Person_strategy)
def test_dmm::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=dmm::Person_strategy)
def test_dmm::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=dmm::UniversityManagementSystem_strategy)
@settings(max_examples=50)
def test_dmm::universitymanagementsystem_instantiation(instance):
    assert isinstance(instance, dmm::UniversityManagementSystem)

@given(instance=dmm::Exam_strategy)
@settings(max_examples=50)
def test_dmm::exam_instantiation(instance):
    assert isinstance(instance, dmm::Exam)

@given(instance=dmm::Exam_strategy)
def test_dmm::exam_examID_type(instance):
    assert isinstance(instance.examID, str)


@given(instance=dmm::Exam_strategy)
def test_dmm::exam_examID_setter(instance):
    original = instance.examID
    instance.examID = original
    assert instance.examID == original

@given(instance=dmm::Course_strategy)
@settings(max_examples=50)
def test_dmm::course_instantiation(instance):
    assert isinstance(instance, dmm::Course)

@given(instance=dmm::Course_strategy)
def test_dmm::course_courseType_type(instance):
    assert isinstance(instance.courseType, str)


@given(instance=dmm::Course_strategy)
def test_dmm::course_courseType_setter(instance):
    original = instance.courseType
    instance.courseType = original
    assert instance.courseType == original

@given(instance=dmm::Course_strategy)
def test_dmm::course_courseNumber_type(instance):
    assert isinstance(instance.courseNumber, int)


@given(instance=dmm::Course_strategy)
def test_dmm::course_courseNumber_setter(instance):
    original = instance.courseNumber
    instance.courseNumber = original
    assert instance.courseNumber == original

@given(instance=dmm::Course_strategy)
def test_dmm::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dmm::Course_strategy)
def test_dmm::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=dmm::Professor_strategy)
@settings(max_examples=50)
def test_dmm::professor_instantiation(instance):
    assert isinstance(instance, dmm::Professor)

@given(instance=dmm::Professor_strategy)
def test_dmm::professor_employeeNumber_type(instance):
    assert isinstance(instance.employeeNumber, int)


@given(instance=dmm::Professor_strategy)
def test_dmm::professor_employeeNumber_setter(instance):
    original = instance.employeeNumber
    instance.employeeNumber = original
    assert instance.employeeNumber == original

@given(instance=dmm::Student_strategy)
@settings(max_examples=50)
def test_dmm::student_instantiation(instance):
    assert isinstance(instance, dmm::Student)

@given(instance=dmm::Student_strategy)
def test_dmm::student_matriculationNumber_type(instance):
    assert isinstance(instance.matriculationNumber, int)


@given(instance=dmm::Student_strategy)
def test_dmm::student_matriculationNumber_setter(instance):
    original = instance.matriculationNumber
    instance.matriculationNumber = original
    assert instance.matriculationNumber == original
