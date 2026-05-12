import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_Year,
    Course,
    school_SpecialisationCourse,
    school_Student,
    school_SchoolClass,
    school_Teacher,
    school_School,
    school_Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_year_is_not_abstract():
    assert not inspect.isabstract(school_Year)


def test_school_year_constructor_exists():
    assert callable(school_Year.__init__)


def test_school_year_constructor_args():
    sig = inspect.signature(school_Year.__init__)
    params = list(sig.parameters.keys())
    assert "startingDate" in params, "Missing parameter 'startingDate'"

def test_school_year_has_startingDate():
    assert hasattr(school_Year, "startingDate")
    descriptor = None
    for klass in school_Year.__mro__:
        if "startingDate" in klass.__dict__:
            descriptor = klass.__dict__["startingDate"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())



def test_school_specialisationcourse_is_not_abstract():
    assert not inspect.isabstract(school_SpecialisationCourse)


def test_school_specialisationcourse_constructor_exists():
    assert callable(school_SpecialisationCourse.__init__)


def test_school_specialisationcourse_constructor_args():
    sig = inspect.signature(school_SpecialisationCourse.__init__)
    params = list(sig.parameters.keys())
    assert "specialisation" in params, "Missing parameter 'specialisation'"

def test_school_specialisationcourse_has_specialisation():
    assert hasattr(school_SpecialisationCourse, "specialisation")
    descriptor = None
    for klass in school_SpecialisationCourse.__mro__:
        if "specialisation" in klass.__dict__:
            descriptor = klass.__dict__["specialisation"]
            break
    assert isinstance(descriptor, property)



def test_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_student_has_name():
    assert hasattr(school_Student, "name")
    descriptor = None
    for klass in school_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_schoolclass_is_not_abstract():
    assert not inspect.isabstract(school_SchoolClass)


def test_school_schoolclass_constructor_exists():
    assert callable(school_SchoolClass.__init__)


def test_school_schoolclass_constructor_args():
    sig = inspect.signature(school_SchoolClass.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_school_schoolclass_has_code():
    assert hasattr(school_SchoolClass, "code")
    descriptor = None
    for klass in school_SchoolClass.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_school_teacher_is_not_abstract():
    assert not inspect.isabstract(school_Teacher)


def test_school_teacher_constructor_exists():
    assert callable(school_Teacher.__init__)


def test_school_teacher_constructor_args():
    sig = inspect.signature(school_Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_teacher_has_name():
    assert hasattr(school_Teacher, "name")
    descriptor = None
    for klass in school_Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_school_school_has_name():
    assert hasattr(school_School, "name")
    descriptor = None
    for klass in school_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school_school_has_address():
    assert hasattr(school_School, "address")
    descriptor = None
    for klass in school_School.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_school_course_is_not_abstract():
    assert not inspect.isabstract(school_Course)


def test_school_course_constructor_exists():
    assert callable(school_Course.__init__)


def test_school_course_constructor_args():
    sig = inspect.signature(school_Course.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_school_course_has_subject():
    assert hasattr(school_Course, "subject")
    descriptor = None
    for klass in school_Course.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_school_course_has_weight():
    assert hasattr(school_Course, "weight")
    descriptor = None
    for klass in school_Course.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
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
school_Year_strategy = st.builds(
    school_Year,
    startingDate=
        st.integers()
)
Course_strategy = st.builds(
    Course,
)
school_SpecialisationCourse_strategy = st.builds(
    school_SpecialisationCourse,
    specialisation=
        safe_text
)
school_Student_strategy = st.builds(
    school_Student,
    name=
        safe_text
)
school_SchoolClass_strategy = st.builds(
    school_SchoolClass,
    code=
        safe_text
)
school_Teacher_strategy = st.builds(
    school_Teacher,
    name=
        safe_text
)
school_School_strategy = st.builds(
    school_School,
    name=
        safe_text,
    address=
        safe_text
)
school_Course_strategy = st.builds(
    school_Course,
    subject=
        safe_text,
    weight=
        st.integers()
)

@given(instance=school_Year_strategy)
@settings(max_examples=50)
def test_school_year_instantiation(instance):
    assert isinstance(instance, school_Year)



@given(instance=school_Year_strategy)
def test_school_year_startingDate_setter(instance):
    original = instance.startingDate
    instance.startingDate = original
    assert instance.startingDate == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)

@given(instance=school_SpecialisationCourse_strategy)
@settings(max_examples=50)
def test_school_specialisationcourse_instantiation(instance):
    assert isinstance(instance, school_SpecialisationCourse)



@given(instance=school_SpecialisationCourse_strategy)
def test_school_specialisationcourse_specialisation_setter(instance):
    original = instance.specialisation
    instance.specialisation = original
    assert instance.specialisation == original

@given(instance=school_Student_strategy)
@settings(max_examples=50)
def test_school_student_instantiation(instance):
    assert isinstance(instance, school_Student)



@given(instance=school_Student_strategy)
def test_school_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_SchoolClass_strategy)
@settings(max_examples=50)
def test_school_schoolclass_instantiation(instance):
    assert isinstance(instance, school_SchoolClass)



@given(instance=school_SchoolClass_strategy)
def test_school_schoolclass_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=school_Teacher_strategy)
@settings(max_examples=50)
def test_school_teacher_instantiation(instance):
    assert isinstance(instance, school_Teacher)



@given(instance=school_Teacher_strategy)
def test_school_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)



@given(instance=school_School_strategy)
def test_school_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=school_School_strategy)
def test_school_school_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=school_Course_strategy)
@settings(max_examples=50)
def test_school_course_instantiation(instance):
    assert isinstance(instance, school_Course)



@given(instance=school_Course_strategy)
def test_school_course_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=school_Course_strategy)
def test_school_course_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
