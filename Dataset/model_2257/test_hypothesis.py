import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_Grade,
    school_Course,
    school_Pupil,
    school_School,
    Grade,
    school_Grade2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_grade_is_not_abstract():
    assert not inspect.isabstract(school_Grade)


def test_school_grade_constructor_exists():
    assert callable(school_Grade.__init__)


def test_school_grade_constructor_args():
    sig = inspect.signature(school_Grade.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"
    assert "year" in params, "Missing parameter 'year'"

def test_school_grade_has_grade():
    assert hasattr(school_Grade, "grade")
    descriptor = None
    for klass in school_Grade.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)

def test_school_grade_has_year():
    assert hasattr(school_Grade, "year")
    descriptor = None
    for klass in school_Grade.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_school_course_is_not_abstract():
    assert not inspect.isabstract(school_Course)


def test_school_course_constructor_exists():
    assert callable(school_Course.__init__)


def test_school_course_constructor_args():
    sig = inspect.signature(school_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_course_has_name():
    assert hasattr(school_Course, "name")
    descriptor = None
    for klass in school_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_pupil_is_not_abstract():
    assert not inspect.isabstract(school_Pupil)


def test_school_pupil_constructor_exists():
    assert callable(school_Pupil.__init__)


def test_school_pupil_constructor_args():
    sig = inspect.signature(school_Pupil.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "inclass" in params, "Missing parameter 'inclass'"

def test_school_pupil_has_name():
    assert hasattr(school_Pupil, "name")
    descriptor = None
    for klass in school_Pupil.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_school_pupil_has_inclass():
    assert hasattr(school_Pupil, "inclass")
    descriptor = None
    for klass in school_Pupil.__mro__:
        if "inclass" in klass.__dict__:
            descriptor = klass.__dict__["inclass"]
            break
    assert isinstance(descriptor, property)



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
    params = list(sig.parameters.keys())



def test_grade_is_not_abstract():
    assert not inspect.isabstract(Grade)


def test_grade_constructor_exists():
    assert callable(Grade.__init__)


def test_grade_constructor_args():
    sig = inspect.signature(Grade.__init__)
    params = list(sig.parameters.keys())



def test_school_grade2_is_not_abstract():
    assert not inspect.isabstract(school_Grade2)


def test_school_grade2_constructor_exists():
    assert callable(school_Grade2.__init__)


def test_school_grade2_constructor_args():
    sig = inspect.signature(school_Grade2.__init__)
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
school_Grade_strategy = st.builds(
    school_Grade,
    grade=
        safe_text,
    year=
        safe_text
)
school_Course_strategy = st.builds(
    school_Course,
    name=
        safe_text
)
school_Pupil_strategy = st.builds(
    school_Pupil,
    name=
        safe_text,
    inclass=
        safe_text
)
school_School_strategy = st.builds(
    school_School,
)
Grade_strategy = st.builds(
    Grade,
)
school_Grade2_strategy = st.builds(
    school_Grade2,
)

@given(instance=school_Grade_strategy)
@settings(max_examples=50)
def test_school_grade_instantiation(instance):
    assert isinstance(instance, school_Grade)



@given(instance=school_Grade_strategy)
def test_school_grade_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original



@given(instance=school_Grade_strategy)
def test_school_grade_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=school_Course_strategy)
@settings(max_examples=50)
def test_school_course_instantiation(instance):
    assert isinstance(instance, school_Course)



@given(instance=school_Course_strategy)
def test_school_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Pupil_strategy)
@settings(max_examples=50)
def test_school_pupil_instantiation(instance):
    assert isinstance(instance, school_Pupil)



@given(instance=school_Pupil_strategy)
def test_school_pupil_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=school_Pupil_strategy)
def test_school_pupil_inclass_setter(instance):
    original = instance.inclass
    instance.inclass = original
    assert instance.inclass == original

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)

@given(instance=Grade_strategy)
@settings(max_examples=50)
def test_grade_instantiation(instance):
    assert isinstance(instance, Grade)

@given(instance=school_Grade2_strategy)
@settings(max_examples=50)
def test_school_grade2_instantiation(instance):
    assert isinstance(instance, school_Grade2)
