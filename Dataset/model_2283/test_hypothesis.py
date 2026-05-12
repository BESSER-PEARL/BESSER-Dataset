import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    University_UniversityManagementSystem,
    University_Exam,
    University_Person,
    University_Course,
    Person,
    University_Professor,
    University_Student,
    CourseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university_universitymanagementsystem_is_not_abstract():
    assert not inspect.isabstract(University_UniversityManagementSystem)


def test_university_universitymanagementsystem_constructor_exists():
    assert callable(University_UniversityManagementSystem.__init__)


def test_university_universitymanagementsystem_constructor_args():
    sig = inspect.signature(University_UniversityManagementSystem.__init__)
    params = list(sig.parameters.keys())



def test_university_exam_is_not_abstract():
    assert not inspect.isabstract(University_Exam)


def test_university_exam_constructor_exists():
    assert callable(University_Exam.__init__)


def test_university_exam_constructor_args():
    sig = inspect.signature(University_Exam.__init__)
    params = list(sig.parameters.keys())
    assert "examID" in params, "Missing parameter 'examID'"

def test_university_exam_has_examID():
    assert hasattr(University_Exam, "examID")
    descriptor = None
    for klass in University_Exam.__mro__:
        if "examID" in klass.__dict__:
            descriptor = klass.__dict__["examID"]
            break
    assert isinstance(descriptor, property)



def test_university_person_is_not_abstract():
    assert not inspect.isabstract(University_Person)


def test_university_person_constructor_exists():
    assert callable(University_Person.__init__)


def test_university_person_constructor_args():
    sig = inspect.signature(University_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"

def test_university_person_has_name():
    assert hasattr(University_Person, "name")
    descriptor = None
    for klass in University_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university_person_has_email():
    assert hasattr(University_Person, "email")
    descriptor = None
    for klass in University_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_university_course_is_not_abstract():
    assert not inspect.isabstract(University_Course)


def test_university_course_constructor_exists():
    assert callable(University_Course.__init__)


def test_university_course_constructor_args():
    sig = inspect.signature(University_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "courseNumber" in params, "Missing parameter 'courseNumber'"
    assert "courseType" in params, "Missing parameter 'courseType'"

def test_university_course_has_name():
    assert hasattr(University_Course, "name")
    descriptor = None
    for klass in University_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_courseNumber():
    assert hasattr(University_Course, "courseNumber")
    descriptor = None
    for klass in University_Course.__mro__:
        if "courseNumber" in klass.__dict__:
            descriptor = klass.__dict__["courseNumber"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_courseType():
    assert hasattr(University_Course, "courseType")
    descriptor = None
    for klass in University_Course.__mro__:
        if "courseType" in klass.__dict__:
            descriptor = klass.__dict__["courseType"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_university_professor_is_not_abstract():
    assert not inspect.isabstract(University_Professor)


def test_university_professor_constructor_exists():
    assert callable(University_Professor.__init__)


def test_university_professor_constructor_args():
    sig = inspect.signature(University_Professor.__init__)
    params = list(sig.parameters.keys())
    assert "employeeNumber" in params, "Missing parameter 'employeeNumber'"

def test_university_professor_has_employeeNumber():
    assert hasattr(University_Professor, "employeeNumber")
    descriptor = None
    for klass in University_Professor.__mro__:
        if "employeeNumber" in klass.__dict__:
            descriptor = klass.__dict__["employeeNumber"]
            break
    assert isinstance(descriptor, property)



def test_university_student_is_not_abstract():
    assert not inspect.isabstract(University_Student)


def test_university_student_constructor_exists():
    assert callable(University_Student.__init__)


def test_university_student_constructor_args():
    sig = inspect.signature(University_Student.__init__)
    params = list(sig.parameters.keys())
    assert "matriculationNumber" in params, "Missing parameter 'matriculationNumber'"

def test_university_student_has_matriculationNumber():
    assert hasattr(University_Student, "matriculationNumber")
    descriptor = None
    for klass in University_Student.__mro__:
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
        "PR",
        "SEM",
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
University_UniversityManagementSystem_strategy = st.builds(
    University_UniversityManagementSystem,
)
University_Exam_strategy = st.builds(
    University_Exam,
    examID=
        safe_text
)
University_Person_strategy = st.builds(
    University_Person,
    name=
        safe_text,
    email=
        safe_text
)
University_Course_strategy = st.builds(
    University_Course,
    name=
        safe_text,
    courseNumber=
        st.integers(),
    courseType=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
University_Professor_strategy = st.builds(
    University_Professor,
    employeeNumber=
        st.integers()
)
University_Student_strategy = st.builds(
    University_Student,
    matriculationNumber=
        st.integers()
)

@given(instance=University_UniversityManagementSystem_strategy)
@settings(max_examples=50)
def test_university_universitymanagementsystem_instantiation(instance):
    assert isinstance(instance, University_UniversityManagementSystem)

@given(instance=University_Exam_strategy)
@settings(max_examples=50)
def test_university_exam_instantiation(instance):
    assert isinstance(instance, University_Exam)



@given(instance=University_Exam_strategy)
def test_university_exam_examID_setter(instance):
    original = instance.examID
    instance.examID = original
    assert instance.examID == original

@given(instance=University_Person_strategy)
@settings(max_examples=50)
def test_university_person_instantiation(instance):
    assert isinstance(instance, University_Person)



@given(instance=University_Person_strategy)
def test_university_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=University_Person_strategy)
def test_university_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=University_Course_strategy)
@settings(max_examples=50)
def test_university_course_instantiation(instance):
    assert isinstance(instance, University_Course)



@given(instance=University_Course_strategy)
def test_university_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=University_Course_strategy)
def test_university_course_courseNumber_setter(instance):
    original = instance.courseNumber
    instance.courseNumber = original
    assert instance.courseNumber == original



@given(instance=University_Course_strategy)
def test_university_course_courseType_setter(instance):
    original = instance.courseType
    instance.courseType = original
    assert instance.courseType == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=University_Professor_strategy)
@settings(max_examples=50)
def test_university_professor_instantiation(instance):
    assert isinstance(instance, University_Professor)



@given(instance=University_Professor_strategy)
def test_university_professor_employeeNumber_setter(instance):
    original = instance.employeeNumber
    instance.employeeNumber = original
    assert instance.employeeNumber == original

@given(instance=University_Student_strategy)
@settings(max_examples=50)
def test_university_student_instantiation(instance):
    assert isinstance(instance, University_Student)



@given(instance=University_Student_strategy)
def test_university_student_matriculationNumber_setter(instance):
    original = instance.matriculationNumber
    instance.matriculationNumber = original
    assert instance.matriculationNumber == original
