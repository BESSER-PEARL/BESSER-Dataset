import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    programmes::University,
    Programme,
    programmes::CourseGroup,
    programmes::Semester,
    programmes::Specialization,
    programmes::Programme,
    programmes::Course,
    StudyLevel,
    CourseType,
    SemesterType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_programmes::university_is_not_abstract():
    assert not inspect.isabstract(programmes::University)


def test_programmes::university_constructor_exists():
    assert callable(programmes::University.__init__)


def test_programmes::university_constructor_args():
    sig = inspect.signature(programmes::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_programmes::university_has_name():
    assert hasattr(programmes::University, "name")
    descriptor = None
    for klass in programmes::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_programme_is_not_abstract():
    assert not inspect.isabstract(Programme)


def test_programme_constructor_exists():
    assert callable(Programme.__init__)


def test_programme_constructor_args():
    sig = inspect.signature(Programme.__init__)
    params = list(sig.parameters.keys())



def test_programmes::coursegroup_is_not_abstract():
    assert not inspect.isabstract(programmes::CourseGroup)


def test_programmes::coursegroup_constructor_exists():
    assert callable(programmes::CourseGroup.__init__)


def test_programmes::coursegroup_constructor_args():
    sig = inspect.signature(programmes::CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "coursesType" in params, "Missing parameter 'coursesType'"

def test_programmes::coursegroup_has_name():
    assert hasattr(programmes::CourseGroup, "name")
    descriptor = None
    for klass in programmes::CourseGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programmes::coursegroup_has_coursesType():
    assert hasattr(programmes::CourseGroup, "coursesType")
    descriptor = None
    for klass in programmes::CourseGroup.__mro__:
        if "coursesType" in klass.__dict__:
            descriptor = klass.__dict__["coursesType"]
            break
    assert isinstance(descriptor, property)



def test_programmes::semester_is_not_abstract():
    assert not inspect.isabstract(programmes::Semester)


def test_programmes::semester_constructor_exists():
    assert callable(programmes::Semester.__init__)


def test_programmes::semester_constructor_args():
    sig = inspect.signature(programmes::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterType" in params, "Missing parameter 'semesterType'"
    assert "year" in params, "Missing parameter 'year'"

def test_programmes::semester_has_semesterType():
    assert hasattr(programmes::Semester, "semesterType")
    descriptor = None
    for klass in programmes::Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)

def test_programmes::semester_has_year():
    assert hasattr(programmes::Semester, "year")
    descriptor = None
    for klass in programmes::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_programmes::specialization_is_not_abstract():
    assert not inspect.isabstract(programmes::Specialization)


def test_programmes::specialization_constructor_exists():
    assert callable(programmes::Specialization.__init__)


def test_programmes::specialization_constructor_args():
    sig = inspect.signature(programmes::Specialization.__init__)
    params = list(sig.parameters.keys())



def test_programmes::programme_is_not_abstract():
    assert not inspect.isabstract(programmes::Programme)


def test_programmes::programme_constructor_exists():
    assert callable(programmes::Programme.__init__)


def test_programmes::programme_constructor_args():
    sig = inspect.signature(programmes::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_programmes::programme_has_name():
    assert hasattr(programmes::Programme, "name")
    descriptor = None
    for klass in programmes::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programmes::programme_has_code():
    assert hasattr(programmes::Programme, "code")
    descriptor = None
    for klass in programmes::Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_programmes::course_is_not_abstract():
    assert not inspect.isabstract(programmes::Course)


def test_programmes::course_constructor_exists():
    assert callable(programmes::Course.__init__)


def test_programmes::course_constructor_args():
    sig = inspect.signature(programmes::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"

def test_programmes::course_has_level():
    assert hasattr(programmes::Course, "level")
    descriptor = None
    for klass in programmes::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_programmes::course_has_code():
    assert hasattr(programmes::Course, "code")
    descriptor = None
    for klass in programmes::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_programmes::course_has_name():
    assert hasattr(programmes::Course, "name")
    descriptor = None
    for klass in programmes::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programmes::course_has_credits():
    assert hasattr(programmes::Course, "credits")
    descriptor = None
    for klass in programmes::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studylevel_exists():
    # Check that the Enumeration exists
    assert StudyLevel is not None

def test_studylevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyLevel]
    expected_literals = [
        "THIRD_YEAR",
        "SECOND_YEAR",
        "POST_GRAD",
        "SECOND_DEGREE",
        "FIRST_YEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyLevel"

def test_coursetype_exists():
    # Check that the Enumeration exists
    assert CourseType is not None

def test_coursetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseType]
    expected_literals = [
        "MANDATORY",
        "ELECTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseType"

def test_semestertype_exists():
    # Check that the Enumeration exists
    assert SemesterType is not None

def test_semestertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterType]
    expected_literals = [
        "Spring",
        "Autumn",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterType"


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
programmes::University_strategy = st.builds(
    programmes::University,
    name=
        safe_text
)
Programme_strategy = st.builds(
    Programme,
)
programmes::CourseGroup_strategy = st.builds(
    programmes::CourseGroup,
    name=
        safe_text,
    coursesType=
        safe_text
)
programmes::Semester_strategy = st.builds(
    programmes::Semester,
    semesterType=
        safe_text,
    year=
        st.integers()
)
programmes::Specialization_strategy = st.builds(
    programmes::Specialization,
)
programmes::Programme_strategy = st.builds(
    programmes::Programme,
    name=
        safe_text,
    code=
        safe_text
)
programmes::Course_strategy = st.builds(
    programmes::Course,
    level=
        safe_text,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=programmes::University_strategy)
@settings(max_examples=50)
def test_programmes::university_instantiation(instance):
    assert isinstance(instance, programmes::University)

@given(instance=programmes::University_strategy)
def test_programmes::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programmes::University_strategy)
def test_programmes::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Programme_strategy)
@settings(max_examples=50)
def test_programme_instantiation(instance):
    assert isinstance(instance, Programme)

@given(instance=programmes::CourseGroup_strategy)
@settings(max_examples=50)
def test_programmes::coursegroup_instantiation(instance):
    assert isinstance(instance, programmes::CourseGroup)

@given(instance=programmes::CourseGroup_strategy)
def test_programmes::coursegroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programmes::CourseGroup_strategy)
def test_programmes::coursegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programmes::CourseGroup_strategy)
def test_programmes::coursegroup_coursesType_type(instance):
    assert isinstance(instance.coursesType, str)


@given(instance=programmes::CourseGroup_strategy)
def test_programmes::coursegroup_coursesType_setter(instance):
    original = instance.coursesType
    instance.coursesType = original
    assert instance.coursesType == original

@given(instance=programmes::Semester_strategy)
@settings(max_examples=50)
def test_programmes::semester_instantiation(instance):
    assert isinstance(instance, programmes::Semester)

@given(instance=programmes::Semester_strategy)
def test_programmes::semester_semesterType_type(instance):
    assert isinstance(instance.semesterType, str)


@given(instance=programmes::Semester_strategy)
def test_programmes::semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original

@given(instance=programmes::Semester_strategy)
def test_programmes::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=programmes::Semester_strategy)
def test_programmes::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=programmes::Specialization_strategy)
@settings(max_examples=50)
def test_programmes::specialization_instantiation(instance):
    assert isinstance(instance, programmes::Specialization)

@given(instance=programmes::Programme_strategy)
@settings(max_examples=50)
def test_programmes::programme_instantiation(instance):
    assert isinstance(instance, programmes::Programme)

@given(instance=programmes::Programme_strategy)
def test_programmes::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programmes::Programme_strategy)
def test_programmes::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programmes::Programme_strategy)
def test_programmes::programme_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=programmes::Programme_strategy)
def test_programmes::programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=programmes::Course_strategy)
@settings(max_examples=50)
def test_programmes::course_instantiation(instance):
    assert isinstance(instance, programmes::Course)

@given(instance=programmes::Course_strategy)
def test_programmes::course_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=programmes::Course_strategy)
def test_programmes::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=programmes::Course_strategy)
def test_programmes::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=programmes::Course_strategy)
def test_programmes::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=programmes::Course_strategy)
def test_programmes::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programmes::Course_strategy)
def test_programmes::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programmes::Course_strategy)
def test_programmes::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=programmes::Course_strategy)
def test_programmes::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original
