import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    prosjekt::Semester,
    prosjekt::CourseCoordinator,
    prosjekt::Course,
    prosjekt::Institute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prosjekt::semester_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Semester)


def test_prosjekt::semester_constructor_exists():
    assert callable(prosjekt::Semester.__init__)


def test_prosjekt::semester_constructor_args():
    sig = inspect.signature(prosjekt::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt::semester_has_name():
    assert hasattr(prosjekt::Semester, "name")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::coursecoordinator_is_not_abstract():
    assert not inspect.isabstract(prosjekt::CourseCoordinator)


def test_prosjekt::coursecoordinator_constructor_exists():
    assert callable(prosjekt::CourseCoordinator.__init__)


def test_prosjekt::coursecoordinator_constructor_args():
    sig = inspect.signature(prosjekt::CourseCoordinator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt::coursecoordinator_has_name():
    assert hasattr(prosjekt::CourseCoordinator, "name")
    descriptor = None
    for klass in prosjekt::CourseCoordinator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::course_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Course)


def test_prosjekt::course_constructor_exists():
    assert callable(prosjekt::Course.__init__)


def test_prosjekt::course_constructor_args():
    sig = inspect.signature(prosjekt::Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "avgGrade" in params, "Missing parameter 'avgGrade'"
    assert "studyPoints" in params, "Missing parameter 'studyPoints'"

def test_prosjekt::course_has_code():
    assert hasattr(prosjekt::Course, "code")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::course_has_name():
    assert hasattr(prosjekt::Course, "name")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::course_has_avgGrade():
    assert hasattr(prosjekt::Course, "avgGrade")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "avgGrade" in klass.__dict__:
            descriptor = klass.__dict__["avgGrade"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::course_has_studyPoints():
    assert hasattr(prosjekt::Course, "studyPoints")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "studyPoints" in klass.__dict__:
            descriptor = klass.__dict__["studyPoints"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::institute_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Institute)


def test_prosjekt::institute_constructor_exists():
    assert callable(prosjekt::Institute.__init__)


def test_prosjekt::institute_constructor_args():
    sig = inspect.signature(prosjekt::Institute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_prosjekt::institute_has_name():
    assert hasattr(prosjekt::Institute, "name")
    descriptor = None
    for klass in prosjekt::Institute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::institute_has_shortName():
    assert hasattr(prosjekt::Institute, "shortName")
    descriptor = None
    for klass in prosjekt::Institute.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
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
prosjekt::Semester_strategy = st.builds(
    prosjekt::Semester,
    name=
        safe_text
)
prosjekt::CourseCoordinator_strategy = st.builds(
    prosjekt::CourseCoordinator,
    name=
        safe_text
)
prosjekt::Course_strategy = st.builds(
    prosjekt::Course,
    code=
        safe_text,
    name=
        safe_text,
    avgGrade=
        st.integers(),
    studyPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
prosjekt::Institute_strategy = st.builds(
    prosjekt::Institute,
    name=
        safe_text,
    shortName=
        safe_text
)

@given(instance=prosjekt::Semester_strategy)
@settings(max_examples=50)
def test_prosjekt::semester_instantiation(instance):
    assert isinstance(instance, prosjekt::Semester)

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::CourseCoordinator_strategy)
@settings(max_examples=50)
def test_prosjekt::coursecoordinator_instantiation(instance):
    assert isinstance(instance, prosjekt::CourseCoordinator)

@given(instance=prosjekt::CourseCoordinator_strategy)
def test_prosjekt::coursecoordinator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::CourseCoordinator_strategy)
def test_prosjekt::coursecoordinator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Course_strategy)
@settings(max_examples=50)
def test_prosjekt::course_instantiation(instance):
    assert isinstance(instance, prosjekt::Course)

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_avgGrade_type(instance):
    assert isinstance(instance.avgGrade, int)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_avgGrade_setter(instance):
    original = instance.avgGrade
    instance.avgGrade = original
    assert instance.avgGrade == original

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_studyPoints_type(instance):
    assert isinstance(instance.studyPoints, float)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_studyPoints_setter(instance):
    original = instance.studyPoints
    instance.studyPoints = original
    assert instance.studyPoints == original

@given(instance=prosjekt::Institute_strategy)
@settings(max_examples=50)
def test_prosjekt::institute_instantiation(instance):
    assert isinstance(instance, prosjekt::Institute)

@given(instance=prosjekt::Institute_strategy)
def test_prosjekt::institute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Institute_strategy)
def test_prosjekt::institute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Institute_strategy)
def test_prosjekt::institute_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=prosjekt::Institute_strategy)
def test_prosjekt::institute_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original
