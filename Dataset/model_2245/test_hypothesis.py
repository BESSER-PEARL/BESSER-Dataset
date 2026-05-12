import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    prosjekt_Semester,
    prosjekt_CourseCoordinator,
    prosjekt_Course,
    prosjekt_Institute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prosjekt_semester_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Semester)


def test_prosjekt_semester_constructor_exists():
    assert callable(prosjekt_Semester.__init__)


def test_prosjekt_semester_constructor_args():
    sig = inspect.signature(prosjekt_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt_semester_has_name():
    assert hasattr(prosjekt_Semester, "name")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_coursecoordinator_is_not_abstract():
    assert not inspect.isabstract(prosjekt_CourseCoordinator)


def test_prosjekt_coursecoordinator_constructor_exists():
    assert callable(prosjekt_CourseCoordinator.__init__)


def test_prosjekt_coursecoordinator_constructor_args():
    sig = inspect.signature(prosjekt_CourseCoordinator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt_coursecoordinator_has_name():
    assert hasattr(prosjekt_CourseCoordinator, "name")
    descriptor = None
    for klass in prosjekt_CourseCoordinator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_course_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Course)


def test_prosjekt_course_constructor_exists():
    assert callable(prosjekt_Course.__init__)


def test_prosjekt_course_constructor_args():
    sig = inspect.signature(prosjekt_Course.__init__)
    params = list(sig.parameters.keys())
    assert "avgGrade" in params, "Missing parameter 'avgGrade'"
    assert "studyPoints" in params, "Missing parameter 'studyPoints'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_prosjekt_course_has_avgGrade():
    assert hasattr(prosjekt_Course, "avgGrade")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "avgGrade" in klass.__dict__:
            descriptor = klass.__dict__["avgGrade"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_course_has_studyPoints():
    assert hasattr(prosjekt_Course, "studyPoints")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "studyPoints" in klass.__dict__:
            descriptor = klass.__dict__["studyPoints"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_course_has_name():
    assert hasattr(prosjekt_Course, "name")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_course_has_code():
    assert hasattr(prosjekt_Course, "code")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_institute_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Institute)


def test_prosjekt_institute_constructor_exists():
    assert callable(prosjekt_Institute.__init__)


def test_prosjekt_institute_constructor_args():
    sig = inspect.signature(prosjekt_Institute.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt_institute_has_shortName():
    assert hasattr(prosjekt_Institute, "shortName")
    descriptor = None
    for klass in prosjekt_Institute.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_institute_has_name():
    assert hasattr(prosjekt_Institute, "name")
    descriptor = None
    for klass in prosjekt_Institute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
prosjekt_Semester_strategy = st.builds(
    prosjekt_Semester,
    name=
        safe_text
)
prosjekt_CourseCoordinator_strategy = st.builds(
    prosjekt_CourseCoordinator,
    name=
        safe_text
)
prosjekt_Course_strategy = st.builds(
    prosjekt_Course,
    avgGrade=
        st.integers(),
    studyPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text
)
prosjekt_Institute_strategy = st.builds(
    prosjekt_Institute,
    shortName=
        safe_text,
    name=
        safe_text
)

@given(instance=prosjekt_Semester_strategy)
@settings(max_examples=50)
def test_prosjekt_semester_instantiation(instance):
    assert isinstance(instance, prosjekt_Semester)



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt_CourseCoordinator_strategy)
@settings(max_examples=50)
def test_prosjekt_coursecoordinator_instantiation(instance):
    assert isinstance(instance, prosjekt_CourseCoordinator)



@given(instance=prosjekt_CourseCoordinator_strategy)
def test_prosjekt_coursecoordinator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt_Course_strategy)
@settings(max_examples=50)
def test_prosjekt_course_instantiation(instance):
    assert isinstance(instance, prosjekt_Course)



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_avgGrade_setter(instance):
    original = instance.avgGrade
    instance.avgGrade = original
    assert instance.avgGrade == original



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_studyPoints_setter(instance):
    original = instance.studyPoints
    instance.studyPoints = original
    assert instance.studyPoints == original



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=prosjekt_Institute_strategy)
@settings(max_examples=50)
def test_prosjekt_institute_instantiation(instance):
    assert isinstance(instance, prosjekt_Institute)



@given(instance=prosjekt_Institute_strategy)
def test_prosjekt_institute_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original



@given(instance=prosjekt_Institute_strategy)
def test_prosjekt_institute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
