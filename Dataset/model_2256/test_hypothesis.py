import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Course,
    schoolIncqDerived::SpecialisationCourse,
    schoolIncqDerived::Student,
    schoolIncqDerived::Year,
    schoolIncqDerived::SchoolClass,
    schoolIncqDerived::Teacher,
    schoolIncqDerived::School,
    schoolIncqDerived::Course,
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



def test_schoolincqderived::specialisationcourse_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::SpecialisationCourse)


def test_schoolincqderived::specialisationcourse_constructor_exists():
    assert callable(schoolIncqDerived::SpecialisationCourse.__init__)


def test_schoolincqderived::specialisationcourse_constructor_args():
    sig = inspect.signature(schoolIncqDerived::SpecialisationCourse.__init__)
    params = list(sig.parameters.keys())
    assert "specialisation" in params, "Missing parameter 'specialisation'"

def test_schoolincqderived::specialisationcourse_has_specialisation():
    assert hasattr(schoolIncqDerived::SpecialisationCourse, "specialisation")
    descriptor = None
    for klass in schoolIncqDerived::SpecialisationCourse.__mro__:
        if "specialisation" in klass.__dict__:
            descriptor = klass.__dict__["specialisation"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived::student_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::Student)


def test_schoolincqderived::student_constructor_exists():
    assert callable(schoolIncqDerived::Student.__init__)


def test_schoolincqderived::student_constructor_args():
    sig = inspect.signature(schoolIncqDerived::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schoolincqderived::student_has_name():
    assert hasattr(schoolIncqDerived::Student, "name")
    descriptor = None
    for klass in schoolIncqDerived::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived::year_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::Year)


def test_schoolincqderived::year_constructor_exists():
    assert callable(schoolIncqDerived::Year.__init__)


def test_schoolincqderived::year_constructor_args():
    sig = inspect.signature(schoolIncqDerived::Year.__init__)
    params = list(sig.parameters.keys())
    assert "startingDate" in params, "Missing parameter 'startingDate'"

def test_schoolincqderived::year_has_startingDate():
    assert hasattr(schoolIncqDerived::Year, "startingDate")
    descriptor = None
    for klass in schoolIncqDerived::Year.__mro__:
        if "startingDate" in klass.__dict__:
            descriptor = klass.__dict__["startingDate"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived::schoolclass_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::SchoolClass)


def test_schoolincqderived::schoolclass_constructor_exists():
    assert callable(schoolIncqDerived::SchoolClass.__init__)


def test_schoolincqderived::schoolclass_constructor_args():
    sig = inspect.signature(schoolIncqDerived::SchoolClass.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_schoolincqderived::schoolclass_has_code():
    assert hasattr(schoolIncqDerived::SchoolClass, "code")
    descriptor = None
    for klass in schoolIncqDerived::SchoolClass.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived::teacher_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::Teacher)


def test_schoolincqderived::teacher_constructor_exists():
    assert callable(schoolIncqDerived::Teacher.__init__)


def test_schoolincqderived::teacher_constructor_args():
    sig = inspect.signature(schoolIncqDerived::Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_schoolincqderived::teacher_has_name():
    assert hasattr(schoolIncqDerived::Teacher, "name")
    descriptor = None
    for klass in schoolIncqDerived::Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived::school_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::School)


def test_schoolincqderived::school_constructor_exists():
    assert callable(schoolIncqDerived::School.__init__)


def test_schoolincqderived::school_constructor_args():
    sig = inspect.signature(schoolIncqDerived::School.__init__)
    params = list(sig.parameters.keys())
    assert "currentYear" in params, "Missing parameter 'currentYear'"
    assert "numberOfTeachers" in params, "Missing parameter 'numberOfTeachers'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_schoolincqderived::school_has_currentYear():
    assert hasattr(schoolIncqDerived::School, "currentYear")
    descriptor = None
    for klass in schoolIncqDerived::School.__mro__:
        if "currentYear" in klass.__dict__:
            descriptor = klass.__dict__["currentYear"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived::school_has_numberOfTeachers():
    assert hasattr(schoolIncqDerived::School, "numberOfTeachers")
    descriptor = None
    for klass in schoolIncqDerived::School.__mro__:
        if "numberOfTeachers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTeachers"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived::school_has_address():
    assert hasattr(schoolIncqDerived::School, "address")
    descriptor = None
    for klass in schoolIncqDerived::School.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived::school_has_name():
    assert hasattr(schoolIncqDerived::School, "name")
    descriptor = None
    for klass in schoolIncqDerived::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schoolincqderived::course_is_not_abstract():
    assert not inspect.isabstract(schoolIncqDerived::Course)


def test_schoolincqderived::course_constructor_exists():
    assert callable(schoolIncqDerived::Course.__init__)


def test_schoolincqderived::course_constructor_args():
    sig = inspect.signature(schoolIncqDerived::Course.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_schoolincqderived::course_has_weight():
    assert hasattr(schoolIncqDerived::Course, "weight")
    descriptor = None
    for klass in schoolIncqDerived::Course.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_schoolincqderived::course_has_subject():
    assert hasattr(schoolIncqDerived::Course, "subject")
    descriptor = None
    for klass in schoolIncqDerived::Course.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
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
schoolIncqDerived::SpecialisationCourse_strategy = st.builds(
    schoolIncqDerived::SpecialisationCourse,
    specialisation=
        safe_text
)
schoolIncqDerived::Student_strategy = st.builds(
    schoolIncqDerived::Student,
    name=
        safe_text
)
schoolIncqDerived::Year_strategy = st.builds(
    schoolIncqDerived::Year,
    startingDate=
        st.integers()
)
schoolIncqDerived::SchoolClass_strategy = st.builds(
    schoolIncqDerived::SchoolClass,
    code=
        safe_text
)
schoolIncqDerived::Teacher_strategy = st.builds(
    schoolIncqDerived::Teacher,
    name=
        safe_text
)
schoolIncqDerived::School_strategy = st.builds(
    schoolIncqDerived::School,
    currentYear=
        st.integers(),
    numberOfTeachers=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)
schoolIncqDerived::Course_strategy = st.builds(
    schoolIncqDerived::Course,
    weight=
        st.integers(),
    subject=
        safe_text
)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)

@given(instance=schoolIncqDerived::SpecialisationCourse_strategy)
@settings(max_examples=50)
def test_schoolincqderived::specialisationcourse_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::SpecialisationCourse)

@given(instance=schoolIncqDerived::SpecialisationCourse_strategy)
def test_schoolincqderived::specialisationcourse_specialisation_type(instance):
    assert isinstance(instance.specialisation, str)


@given(instance=schoolIncqDerived::SpecialisationCourse_strategy)
def test_schoolincqderived::specialisationcourse_specialisation_setter(instance):
    original = instance.specialisation
    instance.specialisation = original
    assert instance.specialisation == original

@given(instance=schoolIncqDerived::Student_strategy)
@settings(max_examples=50)
def test_schoolincqderived::student_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::Student)

@given(instance=schoolIncqDerived::Student_strategy)
def test_schoolincqderived::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schoolIncqDerived::Student_strategy)
def test_schoolincqderived::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schoolIncqDerived::Year_strategy)
@settings(max_examples=50)
def test_schoolincqderived::year_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::Year)

@given(instance=schoolIncqDerived::Year_strategy)
def test_schoolincqderived::year_startingDate_type(instance):
    assert isinstance(instance.startingDate, int)


@given(instance=schoolIncqDerived::Year_strategy)
def test_schoolincqderived::year_startingDate_setter(instance):
    original = instance.startingDate
    instance.startingDate = original
    assert instance.startingDate == original

@given(instance=schoolIncqDerived::SchoolClass_strategy)
@settings(max_examples=50)
def test_schoolincqderived::schoolclass_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::SchoolClass)

@given(instance=schoolIncqDerived::SchoolClass_strategy)
def test_schoolincqderived::schoolclass_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=schoolIncqDerived::SchoolClass_strategy)
def test_schoolincqderived::schoolclass_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=schoolIncqDerived::Teacher_strategy)
@settings(max_examples=50)
def test_schoolincqderived::teacher_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::Teacher)

@given(instance=schoolIncqDerived::Teacher_strategy)
def test_schoolincqderived::teacher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schoolIncqDerived::Teacher_strategy)
def test_schoolincqderived::teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schoolIncqDerived::School_strategy)
@settings(max_examples=50)
def test_schoolincqderived::school_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::School)

@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_currentYear_type(instance):
    assert isinstance(instance.currentYear, int)


@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_currentYear_setter(instance):
    original = instance.currentYear
    instance.currentYear = original
    assert instance.currentYear == original

@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_numberOfTeachers_type(instance):
    assert isinstance(instance.numberOfTeachers, int)


@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_numberOfTeachers_setter(instance):
    original = instance.numberOfTeachers
    instance.numberOfTeachers = original
    assert instance.numberOfTeachers == original

@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=schoolIncqDerived::School_strategy)
def test_schoolincqderived::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=schoolIncqDerived::Course_strategy)
@settings(max_examples=50)
def test_schoolincqderived::course_instantiation(instance):
    assert isinstance(instance, schoolIncqDerived::Course)

@given(instance=schoolIncqDerived::Course_strategy)
def test_schoolincqderived::course_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=schoolIncqDerived::Course_strategy)
def test_schoolincqderived::course_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=schoolIncqDerived::Course_strategy)
def test_schoolincqderived::course_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=schoolIncqDerived::Course_strategy)
def test_schoolincqderived::course_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original
