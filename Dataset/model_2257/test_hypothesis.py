import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    school::Grade,
    school::Course,
    school::Pupil,
    school::School,
    Grade,
    school::Grade2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::grade_is_not_abstract():
    assert not inspect.isabstract(school::Grade)


def test_school::grade_constructor_exists():
    assert callable(school::Grade.__init__)


def test_school::grade_constructor_args():
    sig = inspect.signature(school::Grade.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "grade" in params, "Missing parameter 'grade'"

def test_school::grade_has_year():
    assert hasattr(school::Grade, "year")
    descriptor = None
    for klass in school::Grade.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_school::grade_has_grade():
    assert hasattr(school::Grade, "grade")
    descriptor = None
    for klass in school::Grade.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_school::course_is_not_abstract():
    assert not inspect.isabstract(school::Course)


def test_school::course_constructor_exists():
    assert callable(school::Course.__init__)


def test_school::course_constructor_args():
    sig = inspect.signature(school::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::course_has_name():
    assert hasattr(school::Course, "name")
    descriptor = None
    for klass in school::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::pupil_is_not_abstract():
    assert not inspect.isabstract(school::Pupil)


def test_school::pupil_constructor_exists():
    assert callable(school::Pupil.__init__)


def test_school::pupil_constructor_args():
    sig = inspect.signature(school::Pupil.__init__)
    params = list(sig.parameters.keys())
    assert "inclass" in params, "Missing parameter 'inclass'"
    assert "name" in params, "Missing parameter 'name'"

def test_school::pupil_has_inclass():
    assert hasattr(school::Pupil, "inclass")
    descriptor = None
    for klass in school::Pupil.__mro__:
        if "inclass" in klass.__dict__:
            descriptor = klass.__dict__["inclass"]
            break
    assert isinstance(descriptor, property)

def test_school::pupil_has_name():
    assert hasattr(school::Pupil, "name")
    descriptor = None
    for klass in school::Pupil.__mro__:
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



def test_grade_is_not_abstract():
    assert not inspect.isabstract(Grade)


def test_grade_constructor_exists():
    assert callable(Grade.__init__)


def test_grade_constructor_args():
    sig = inspect.signature(Grade.__init__)
    params = list(sig.parameters.keys())



def test_school::grade2_is_not_abstract():
    assert not inspect.isabstract(school::Grade2)


def test_school::grade2_constructor_exists():
    assert callable(school::Grade2.__init__)


def test_school::grade2_constructor_args():
    sig = inspect.signature(school::Grade2.__init__)
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
school::Grade_strategy = st.builds(
    school::Grade,
    year=
        safe_text,
    grade=
        safe_text
)
school::Course_strategy = st.builds(
    school::Course,
    name=
        safe_text
)
school::Pupil_strategy = st.builds(
    school::Pupil,
    inclass=
        safe_text,
    name=
        safe_text
)
school::School_strategy = st.builds(
    school::School,
)
Grade_strategy = st.builds(
    Grade,
)
school::Grade2_strategy = st.builds(
    school::Grade2,
)

@given(instance=school::Grade_strategy)
@settings(max_examples=50)
def test_school::grade_instantiation(instance):
    assert isinstance(instance, school::Grade)

@given(instance=school::Grade_strategy)
def test_school::grade_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=school::Grade_strategy)
def test_school::grade_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=school::Grade_strategy)
def test_school::grade_grade_type(instance):
    assert isinstance(instance.grade, str)


@given(instance=school::Grade_strategy)
def test_school::grade_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=school::Course_strategy)
@settings(max_examples=50)
def test_school::course_instantiation(instance):
    assert isinstance(instance, school::Course)

@given(instance=school::Course_strategy)
def test_school::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Course_strategy)
def test_school::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Pupil_strategy)
@settings(max_examples=50)
def test_school::pupil_instantiation(instance):
    assert isinstance(instance, school::Pupil)

@given(instance=school::Pupil_strategy)
def test_school::pupil_inclass_type(instance):
    assert isinstance(instance.inclass, str)


@given(instance=school::Pupil_strategy)
def test_school::pupil_inclass_setter(instance):
    original = instance.inclass
    instance.inclass = original
    assert instance.inclass == original

@given(instance=school::Pupil_strategy)
def test_school::pupil_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Pupil_strategy)
def test_school::pupil_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)

@given(instance=Grade_strategy)
@settings(max_examples=50)
def test_grade_instantiation(instance):
    assert isinstance(instance, Grade)

@given(instance=school::Grade2_strategy)
@settings(max_examples=50)
def test_school::grade2_instantiation(instance):
    assert isinstance(instance, school::Grade2)
