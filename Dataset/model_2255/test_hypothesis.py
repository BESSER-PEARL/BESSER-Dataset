import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Course,
    schoolIncqDerived_SpecialisationCourse,
    schoolIncqDerived_Student,
    schoolIncqDerived_Year,
    schoolIncqDerived_SchoolClass,
    schoolIncqDerived_Teacher,
    schoolIncqDerived_Course,
    schoolIncqDerived_School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())



def test_schoolincqderived_specialisationcourse_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_SpecialisationCourse)


def test_schoolincqderived_specialisationcourse_constructor_exists():
    assert callable(schoolIncqDerived_SpecialisationCourse.__init__)


def test_schoolincqderived_specialisationcourse_constructor_args():
    sig = inspect.signature(schoolIncqDerived_SpecialisationCourse.__init__)
    params = list(sig.parameters.keys())
    assert "specialisation" in params, "Missing parameter 'specialisation'"

def test_schoolincqderived_specialisationcourse_has_specialisation():
    assert hasattr(schoolIncqDerived_SpecialisationCourse, "specialisation")
    descriptor = None
    for klass in schoolIncqDerived_SpecialisationCourse.__mro__:
        if "specialisation" in klass.__dict__:
            descriptor = klass.__dict__["specialisation"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived_student_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_Student)


def test_schoolincqderived_student_constructor_exists():
    assert callable(schoolIncqDerived_Student.__init__)


def test_schoolincqderived_student_constructor_args():
    sig = inspect.signature(schoolIncqDerived_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schoolincqderived_student_has_name():
    assert hasattr(schoolIncqDerived_Student, "name")
    descriptor = None
    for klass in schoolIncqDerived_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived_year_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_Year)


def test_schoolincqderived_year_constructor_exists():
    assert callable(schoolIncqDerived_Year.__init__)


def test_schoolincqderived_year_constructor_args():
    sig = inspect.signature(schoolIncqDerived_Year.__init__)
    params = list(sig.parameters.keys())
    assert "startingDate" in params, "Missing parameter 'startingDate'"

def test_schoolincqderived_year_has_startingDate():
    assert hasattr(schoolIncqDerived_Year, "startingDate")
    descriptor = None
    for klass in schoolIncqDerived_Year.__mro__:
        if "startingDate" in klass.__dict__:
            descriptor = klass.__dict__["startingDate"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived_schoolclass_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_SchoolClass)


def test_schoolincqderived_schoolclass_constructor_exists():
    assert callable(schoolIncqDerived_SchoolClass.__init__)


def test_schoolincqderived_schoolclass_constructor_args():
    sig = inspect.signature(schoolIncqDerived_SchoolClass.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_schoolincqderived_schoolclass_has_code():
    assert hasattr(schoolIncqDerived_SchoolClass, "code")
    descriptor = None
    for klass in schoolIncqDerived_SchoolClass.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived_teacher_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_Teacher)


def test_schoolincqderived_teacher_constructor_exists():
    assert callable(schoolIncqDerived_Teacher.__init__)


def test_schoolincqderived_teacher_constructor_args():
    sig = inspect.signature(schoolIncqDerived_Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schoolincqderived_teacher_has_name():
    assert hasattr(schoolIncqDerived_Teacher, "name")
    descriptor = None
    for klass in schoolIncqDerived_Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived_course_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_Course)


def test_schoolincqderived_course_constructor_exists():
    assert callable(schoolIncqDerived_Course.__init__)


def test_schoolincqderived_course_constructor_args():
    sig = inspect.signature(schoolIncqDerived_Course.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_schoolincqderived_course_has_weight():
    assert hasattr(schoolIncqDerived_Course, "weight")
    descriptor = None
    for klass in schoolIncqDerived_Course.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived_course_has_subject():
    assert hasattr(schoolIncqDerived_Course, "subject")
    descriptor = None
    for klass in schoolIncqDerived_Course.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived_school_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived_School)


def test_schoolincqderived_school_constructor_exists():
    assert callable(schoolIncqDerived_School.__init__)


def test_schoolincqderived_school_constructor_args():
    sig = inspect.signature(schoolIncqDerived_School.__init__)
    params = list(sig.parameters.keys())
    assert "currentYear" in params, "Missing parameter 'currentYear'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "numberOfTeachers" in params, "Missing parameter 'numberOfTeachers'"

def test_schoolincqderived_school_has_currentYear():
    assert hasattr(schoolIncqDerived_School, "currentYear")
    descriptor = None
    for klass in schoolIncqDerived_School.__mro__:
        if "currentYear" in klass.__dict__:
            descriptor = klass.__dict__["currentYear"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived_school_has_name():
    assert hasattr(schoolIncqDerived_School, "name")
    descriptor = None
    for klass in schoolIncqDerived_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived_school_has_address():
    assert hasattr(schoolIncqDerived_School, "address")
    descriptor = None
    for klass in schoolIncqDerived_School.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived_school_has_numberOfTeachers():
    assert hasattr(schoolIncqDerived_School, "numberOfTeachers")
    descriptor = None
    for klass in schoolIncqDerived_School.__mro__:
        if "numberOfTeachers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTeachers"]
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
Course_strategy = st.builds(
    Course,
)
schoolIncqDerived_SpecialisationCourse_strategy = st.builds(
    schoolIncqDerived_SpecialisationCourse,
    specialisation=
        safe_text
)
schoolIncqDerived_Student_strategy = st.builds(
    schoolIncqDerived_Student,
    name=
        safe_text
)
schoolIncqDerived_Year_strategy = st.builds(
    schoolIncqDerived_Year,
    startingDate=
        st.integers()
)
schoolIncqDerived_SchoolClass_strategy = st.builds(
    schoolIncqDerived_SchoolClass,
    code=
        safe_text
)
schoolIncqDerived_Teacher_strategy = st.builds(
    schoolIncqDerived_Teacher,
    name=
        safe_text
)
schoolIncqDerived_Course_strategy = st.builds(
    schoolIncqDerived_Course,
    weight=
        st.integers(),
    subject=
        safe_text
)
schoolIncqDerived_School_strategy = st.builds(
    schoolIncqDerived_School,
    currentYear=
        st.integers(),
    name=
        safe_text,
    address=
        safe_text,
    numberOfTeachers=
        st.integers()
)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)

@given(instance=schoolIncqDerived_SpecialisationCourse_strategy)
@settings(max_examples=50)
def test_schoolincqderived_specialisationcourse_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_SpecialisationCourse)



@given(instance=schoolIncqDerived_SpecialisationCourse_strategy)
def test_schoolincqderived_specialisationcourse_specialisation_setter(instance):
    original = instance.specialisation
    instance.specialisation = original
    assert instance.specialisation == original

@given(instance=schoolIncqDerived_Student_strategy)
@settings(max_examples=50)
def test_schoolincqderived_student_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Student)



@given(instance=schoolIncqDerived_Student_strategy)
def test_schoolincqderived_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schoolIncqDerived_Year_strategy)
@settings(max_examples=50)
def test_schoolincqderived_year_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Year)



@given(instance=schoolIncqDerived_Year_strategy)
def test_schoolincqderived_year_startingDate_setter(instance):
    original = instance.startingDate
    instance.startingDate = original
    assert instance.startingDate == original

@given(instance=schoolIncqDerived_SchoolClass_strategy)
@settings(max_examples=50)
def test_schoolincqderived_schoolclass_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_SchoolClass)



@given(instance=schoolIncqDerived_SchoolClass_strategy)
def test_schoolincqderived_schoolclass_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=schoolIncqDerived_Teacher_strategy)
@settings(max_examples=50)
def test_schoolincqderived_teacher_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Teacher)



@given(instance=schoolIncqDerived_Teacher_strategy)
def test_schoolincqderived_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schoolIncqDerived_Course_strategy)
@settings(max_examples=50)
def test_schoolincqderived_course_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_Course)



@given(instance=schoolIncqDerived_Course_strategy)
def test_schoolincqderived_course_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=schoolIncqDerived_Course_strategy)
def test_schoolincqderived_course_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=schoolIncqDerived_School_strategy)
@settings(max_examples=50)
def test_schoolincqderived_school_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived_School)



@given(instance=schoolIncqDerived_School_strategy)
def test_schoolincqderived_school_currentYear_setter(instance):
    original = instance.currentYear
    instance.currentYear = original
    assert instance.currentYear == original



@given(instance=schoolIncqDerived_School_strategy)
def test_schoolincqderived_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=schoolIncqDerived_School_strategy)
def test_schoolincqderived_school_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=schoolIncqDerived_School_strategy)
def test_schoolincqderived_school_numberOfTeachers_setter(instance):
    original = instance.numberOfTeachers
    instance.numberOfTeachers = original
    assert instance.numberOfTeachers == original
