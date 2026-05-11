import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Course,
    school::LimitedCapacityCourse,
    school::SpecialisationCourse,
    school::Student,
    school::SchoolClass,
    school::Teacher,
    school::School,
    school::Course,
    school::Year,
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



def test_school::limitedcapacitycourse_is_not_abstract():
    assert not inspect.isabstract(school::LimitedCapacityCourse)


def test_school::limitedcapacitycourse_constructor_exists():
    assert callable(school::LimitedCapacityCourse.__init__)


def test_school::limitedcapacitycourse_constructor_args():
    sig = inspect.signature(school::LimitedCapacityCourse.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_school::limitedcapacitycourse_has_capacity():
    assert hasattr(school::LimitedCapacityCourse, "capacity")
    descriptor = None
    for klass in school::LimitedCapacityCourse.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_school::specialisationcourse_is_not_abstract():
    assert not inspect.isabstract(school::SpecialisationCourse)


def test_school::specialisationcourse_constructor_exists():
    assert callable(school::SpecialisationCourse.__init__)


def test_school::specialisationcourse_constructor_args():
    sig = inspect.signature(school::SpecialisationCourse.__init__)
    params = list(sig.parameters.keys())
    assert "specialisation" in params, "Missing parameter 'specialisation'"

def test_school::specialisationcourse_has_specialisation():
    assert hasattr(school::SpecialisationCourse, "specialisation")
    descriptor = None
    for klass in school::SpecialisationCourse.__mro__:
        if "specialisation" in klass.__dict__:
            descriptor = klass.__dict__["specialisation"]
            break
    assert isinstance(descriptor, property)



def test_school::student_is_not_abstract():
    assert not inspect.isabstract(school::Student)


def test_school::student_constructor_exists():
    assert callable(school::Student.__init__)


def test_school::student_constructor_args():
    sig = inspect.signature(school::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::student_has_name():
    assert hasattr(school::Student, "name")
    descriptor = None
    for klass in school::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::schoolclass_is_not_abstract():
    assert not inspect.isabstract(school::SchoolClass)


def test_school::schoolclass_constructor_exists():
    assert callable(school::SchoolClass.__init__)


def test_school::schoolclass_constructor_args():
    sig = inspect.signature(school::SchoolClass.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_school::schoolclass_has_code():
    assert hasattr(school::SchoolClass, "code")
    descriptor = None
    for klass in school::SchoolClass.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_school::teacher_is_not_abstract():
    assert not inspect.isabstract(school::Teacher)


def test_school::teacher_constructor_exists():
    assert callable(school::Teacher.__init__)


def test_school::teacher_constructor_args():
    sig = inspect.signature(school::Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::teacher_has_name():
    assert hasattr(school::Teacher, "name")
    descriptor = None
    for klass in school::Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(school::School)


def test_school::school_constructor_exists():
    assert callable(school::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(school::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_school::school_has_name():
    assert hasattr(school::School, "name")
    descriptor = None
    for klass in school::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school::school_has_address():
    assert hasattr(school::School, "address")
    descriptor = None
    for klass in school::School.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_school::course_is_not_abstract():
    assert not inspect.isabstract(school::Course)


def test_school::course_constructor_exists():
    assert callable(school::Course.__init__)


def test_school::course_constructor_args():
    sig = inspect.signature(school::Course.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_school::course_has_weight():
    assert hasattr(school::Course, "weight")
    descriptor = None
    for klass in school::Course.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_school::course_has_subject():
    assert hasattr(school::Course, "subject")
    descriptor = None
    for klass in school::Course.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_school::year_is_not_abstract():
    assert not inspect.isabstract(school::Year)


def test_school::year_constructor_exists():
    assert callable(school::Year.__init__)


def test_school::year_constructor_args():
    sig = inspect.signature(school::Year.__init__)
    params = list(sig.parameters.keys())
    assert "startingDate" in params, "Missing parameter 'startingDate'"

def test_school::year_has_startingDate():
    assert hasattr(school::Year, "startingDate")
    descriptor = None
    for klass in school::Year.__mro__:
        if "startingDate" in klass.__dict__:
            descriptor = klass.__dict__["startingDate"]
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
school::LimitedCapacityCourse_strategy = st.builds(
    school::LimitedCapacityCourse,
    capacity=
        st.integers()
)
school::SpecialisationCourse_strategy = st.builds(
    school::SpecialisationCourse,
    specialisation=
        safe_text
)
school::Student_strategy = st.builds(
    school::Student,
    name=
        safe_text
)
school::SchoolClass_strategy = st.builds(
    school::SchoolClass,
    code=
        safe_text
)
school::Teacher_strategy = st.builds(
    school::Teacher,
    name=
        safe_text
)
school::School_strategy = st.builds(
    school::School,
    name=
        safe_text,
    address=
        safe_text
)
school::Course_strategy = st.builds(
    school::Course,
    weight=
        st.integers(),
    subject=
        safe_text
)
school::Year_strategy = st.builds(
    school::Year,
    startingDate=
        st.integers()
)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)

@given(instance=school::LimitedCapacityCourse_strategy)
@settings(max_examples=50)
def test_school::limitedcapacitycourse_instantiation(instance):
    assert isinstance(instance, school::LimitedCapacityCourse)

@given(instance=school::LimitedCapacityCourse_strategy)
def test_school::limitedcapacitycourse_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=school::LimitedCapacityCourse_strategy)
def test_school::limitedcapacitycourse_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=school::SpecialisationCourse_strategy)
@settings(max_examples=50)
def test_school::specialisationcourse_instantiation(instance):
    assert isinstance(instance, school::SpecialisationCourse)

@given(instance=school::SpecialisationCourse_strategy)
def test_school::specialisationcourse_specialisation_type(instance):
    assert isinstance(instance.specialisation, str)


@given(instance=school::SpecialisationCourse_strategy)
def test_school::specialisationcourse_specialisation_setter(instance):
    original = instance.specialisation
    instance.specialisation = original
    assert instance.specialisation == original

@given(instance=school::Student_strategy)
@settings(max_examples=50)
def test_school::student_instantiation(instance):
    assert isinstance(instance, school::Student)

@given(instance=school::Student_strategy)
def test_school::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Student_strategy)
def test_school::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::SchoolClass_strategy)
@settings(max_examples=50)
def test_school::schoolclass_instantiation(instance):
    assert isinstance(instance, school::SchoolClass)

@given(instance=school::SchoolClass_strategy)
def test_school::schoolclass_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=school::SchoolClass_strategy)
def test_school::schoolclass_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=school::Teacher_strategy)
@settings(max_examples=50)
def test_school::teacher_instantiation(instance):
    assert isinstance(instance, school::Teacher)

@given(instance=school::Teacher_strategy)
def test_school::teacher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Teacher_strategy)
def test_school::teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)

@given(instance=school::School_strategy)
def test_school::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::School_strategy)
def test_school::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::School_strategy)
def test_school::school_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=school::School_strategy)
def test_school::school_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=school::Course_strategy)
@settings(max_examples=50)
def test_school::course_instantiation(instance):
    assert isinstance(instance, school::Course)

@given(instance=school::Course_strategy)
def test_school::course_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=school::Course_strategy)
def test_school::course_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=school::Course_strategy)
def test_school::course_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=school::Course_strategy)
def test_school::course_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=school::Year_strategy)
@settings(max_examples=50)
def test_school::year_instantiation(instance):
    assert isinstance(instance, school::Year)

@given(instance=school::Year_strategy)
def test_school::year_startingDate_type(instance):
    assert isinstance(instance.startingDate, int)


@given(instance=school::Year_strategy)
def test_school::year_startingDate_setter(instance):
    original = instance.startingDate
    instance.startingDate = original
    assert instance.startingDate == original
