import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dmm_Person,
    dmm_UniversityManagementSystem,
    dmm_Exam,
    dmm_Course,
    Person,
    dmm_Professor,
    dmm_Student,
    CourseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dmm_person_is_not_abstract():
    assert not inspect.isabstract(dmm_Person)


def test_dmm_person_constructor_exists():
    assert callable(dmm_Person.__init__)


def test_dmm_person_constructor_args():
    sig = inspect.signature(dmm_Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_dmm_person_has_email():
    assert hasattr(dmm_Person, "email")
    descriptor = None
    for klass in dmm_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_dmm_person_has_name():
    assert hasattr(dmm_Person, "name")
    descriptor = None
    for klass in dmm_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dmm_universitymanagementsystem_is_not_abstract():
    assert not inspect.isabstract(dmm_UniversityManagementSystem)


def test_dmm_universitymanagementsystem_constructor_exists():
    assert callable(dmm_UniversityManagementSystem.__init__)


def test_dmm_universitymanagementsystem_constructor_args():
    sig = inspect.signature(dmm_UniversityManagementSystem.__init__)
    params = list(sig.parameters.keys())



def test_dmm_exam_is_not_abstract():
    assert not inspect.isabstract(dmm_Exam)


def test_dmm_exam_constructor_exists():
    assert callable(dmm_Exam.__init__)


def test_dmm_exam_constructor_args():
    sig = inspect.signature(dmm_Exam.__init__)
    params = list(sig.parameters.keys())
    assert "examID" in params, "Missing parameter 'examID'"

def test_dmm_exam_has_examID():
    assert hasattr(dmm_Exam, "examID")
    descriptor = None
    for klass in dmm_Exam.__mro__:
        if "examID" in klass.__dict__:
            descriptor = klass.__dict__["examID"]
            break
    assert isinstance(descriptor, property)



def test_dmm_course_is_not_abstract():
    assert not inspect.isabstract(dmm_Course)


def test_dmm_course_constructor_exists():
    assert callable(dmm_Course.__init__)


def test_dmm_course_constructor_args():
    sig = inspect.signature(dmm_Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseType" in params, "Missing parameter 'courseType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "courseNumber" in params, "Missing parameter 'courseNumber'"

def test_dmm_course_has_courseType():
    assert hasattr(dmm_Course, "courseType")
    descriptor = None
    for klass in dmm_Course.__mro__:
        if "courseType" in klass.__dict__:
            descriptor = klass.__dict__["courseType"]
            break
    assert isinstance(descriptor, property)

def test_dmm_course_has_name():
    assert hasattr(dmm_Course, "name")
    descriptor = None
    for klass in dmm_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dmm_course_has_courseNumber():
    assert hasattr(dmm_Course, "courseNumber")
    descriptor = None
    for klass in dmm_Course.__mro__:
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



def test_dmm_professor_is_not_abstract():
    assert not inspect.isabstract(dmm_Professor)


def test_dmm_professor_constructor_exists():
    assert callable(dmm_Professor.__init__)


def test_dmm_professor_constructor_args():
    sig = inspect.signature(dmm_Professor.__init__)
    params = list(sig.parameters.keys())
    assert "employeeNumber" in params, "Missing parameter 'employeeNumber'"

def test_dmm_professor_has_employeeNumber():
    assert hasattr(dmm_Professor, "employeeNumber")
    descriptor = None
    for klass in dmm_Professor.__mro__:
        if "employeeNumber" in klass.__dict__:
            descriptor = klass.__dict__["employeeNumber"]
            break
    assert isinstance(descriptor, property)



def test_dmm_student_is_not_abstract():
    assert not inspect.isabstract(dmm_Student)


def test_dmm_student_constructor_exists():
    assert callable(dmm_Student.__init__)


def test_dmm_student_constructor_args():
    sig = inspect.signature(dmm_Student.__init__)
    params = list(sig.parameters.keys())
    assert "matriculationNumber" in params, "Missing parameter 'matriculationNumber'"

def test_dmm_student_has_matriculationNumber():
    assert hasattr(dmm_Student, "matriculationNumber")
    descriptor = None
    for klass in dmm_Student.__mro__:
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
        "UE",
        "SEM",
        "PR",
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
dmm_Person_strategy = st.builds(
    dmm_Person,
    email=
        safe_text,
    name=
        safe_text
)
dmm_UniversityManagementSystem_strategy = st.builds(
    dmm_UniversityManagementSystem,
)
dmm_Exam_strategy = st.builds(
    dmm_Exam,
    examID=
        safe_text
)
dmm_Course_strategy = st.builds(
    dmm_Course,
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
dmm_Professor_strategy = st.builds(
    dmm_Professor,
    employeeNumber=
        st.integers()
)
dmm_Student_strategy = st.builds(
    dmm_Student,
    matriculationNumber=
        st.integers()
)

@given(instance=dmm_Person_strategy)
@settings(max_examples=50)
def test_dmm_person_instantiation(instance):
    assert isinstance(instance, dmm_Person)



@given(instance=dmm_Person_strategy)
def test_dmm_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=dmm_Person_strategy)
def test_dmm_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dmm_UniversityManagementSystem_strategy)
@settings(max_examples=50)
def test_dmm_universitymanagementsystem_instantiation(instance):
    assert isinstance(instance, dmm_UniversityManagementSystem)

@given(instance=dmm_Exam_strategy)
@settings(max_examples=50)
def test_dmm_exam_instantiation(instance):
    assert isinstance(instance, dmm_Exam)



@given(instance=dmm_Exam_strategy)
def test_dmm_exam_examID_setter(instance):
    original = instance.examID
    instance.examID = original
    assert instance.examID == original

@given(instance=dmm_Course_strategy)
@settings(max_examples=50)
def test_dmm_course_instantiation(instance):
    assert isinstance(instance, dmm_Course)



@given(instance=dmm_Course_strategy)
def test_dmm_course_courseType_setter(instance):
    original = instance.courseType
    instance.courseType = original
    assert instance.courseType == original



@given(instance=dmm_Course_strategy)
def test_dmm_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dmm_Course_strategy)
def test_dmm_course_courseNumber_setter(instance):
    original = instance.courseNumber
    instance.courseNumber = original
    assert instance.courseNumber == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=dmm_Professor_strategy)
@settings(max_examples=50)
def test_dmm_professor_instantiation(instance):
    assert isinstance(instance, dmm_Professor)



@given(instance=dmm_Professor_strategy)
def test_dmm_professor_employeeNumber_setter(instance):
    original = instance.employeeNumber
    instance.employeeNumber = original
    assert instance.employeeNumber == original

@given(instance=dmm_Student_strategy)
@settings(max_examples=50)
def test_dmm_student_instantiation(instance):
    assert isinstance(instance, dmm_Student)



@given(instance=dmm_Student_strategy)
def test_dmm_student_matriculationNumber_setter(instance):
    original = instance.matriculationNumber
    instance.matriculationNumber = original
    assert instance.matriculationNumber == original
