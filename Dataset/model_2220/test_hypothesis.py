import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    programmes_University,
    Programme,
    programmes_CourseGroup,
    programmes_Semester,
    programmes_Specialization,
    programmes_Programme,
    programmes_Course,
    SemesterType,
    CourseType,
    StudyLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_programmes_university_is_not_abstract():
    assert not inspect.isabstract(programmes_University)


def test_programmes_university_constructor_exists():
    assert callable(programmes_University.__init__)


def test_programmes_university_constructor_args():
    sig = inspect.signature(programmes_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_programmes_university_has_name():
    assert hasattr(programmes_University, "name")
    descriptor = None
    for klass in programmes_University.__mro__:
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



def test_programmes_coursegroup_is_not_abstract():
    assert not inspect.isabstract(programmes_CourseGroup)


def test_programmes_coursegroup_constructor_exists():
    assert callable(programmes_CourseGroup.__init__)


def test_programmes_coursegroup_constructor_args():
    sig = inspect.signature(programmes_CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "coursesType" in params, "Missing parameter 'coursesType'"

def test_programmes_coursegroup_has_name():
    assert hasattr(programmes_CourseGroup, "name")
    descriptor = None
    for klass in programmes_CourseGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programmes_coursegroup_has_coursesType():
    assert hasattr(programmes_CourseGroup, "coursesType")
    descriptor = None
    for klass in programmes_CourseGroup.__mro__:
        if "coursesType" in klass.__dict__:
            descriptor = klass.__dict__["coursesType"]
            break
    assert isinstance(descriptor, property)



def test_programmes_semester_is_not_abstract():
    assert not inspect.isabstract(programmes_Semester)


def test_programmes_semester_constructor_exists():
    assert callable(programmes_Semester.__init__)


def test_programmes_semester_constructor_args():
    sig = inspect.signature(programmes_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterType" in params, "Missing parameter 'semesterType'"
    assert "year" in params, "Missing parameter 'year'"

def test_programmes_semester_has_semesterType():
    assert hasattr(programmes_Semester, "semesterType")
    descriptor = None
    for klass in programmes_Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)

def test_programmes_semester_has_year():
    assert hasattr(programmes_Semester, "year")
    descriptor = None
    for klass in programmes_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_programmes_specialization_is_not_abstract():
    assert not inspect.isabstract(programmes_Specialization)


def test_programmes_specialization_constructor_exists():
    assert callable(programmes_Specialization.__init__)


def test_programmes_specialization_constructor_args():
    sig = inspect.signature(programmes_Specialization.__init__)
    params = list(sig.parameters.keys())



def test_programmes_programme_is_not_abstract():
    assert not inspect.isabstract(programmes_Programme)


def test_programmes_programme_constructor_exists():
    assert callable(programmes_Programme.__init__)


def test_programmes_programme_constructor_args():
    sig = inspect.signature(programmes_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_programmes_programme_has_name():
    assert hasattr(programmes_Programme, "name")
    descriptor = None
    for klass in programmes_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programmes_programme_has_code():
    assert hasattr(programmes_Programme, "code")
    descriptor = None
    for klass in programmes_Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_programmes_course_is_not_abstract():
    assert not inspect.isabstract(programmes_Course)


def test_programmes_course_constructor_exists():
    assert callable(programmes_Course.__init__)


def test_programmes_course_constructor_args():
    sig = inspect.signature(programmes_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "level" in params, "Missing parameter 'level'"

def test_programmes_course_has_credits():
    assert hasattr(programmes_Course, "credits")
    descriptor = None
    for klass in programmes_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_programmes_course_has_name():
    assert hasattr(programmes_Course, "name")
    descriptor = None
    for klass in programmes_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programmes_course_has_code():
    assert hasattr(programmes_Course, "code")
    descriptor = None
    for klass in programmes_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_programmes_course_has_level():
    assert hasattr(programmes_Course, "level")
    descriptor = None
    for klass in programmes_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

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

def test_studylevel_exists():
    # Check that the Enumeration exists
    assert StudyLevel is not None

def test_studylevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyLevel]
    expected_literals = [
        "POST_GRAD",
        "SECOND_DEGREE",
        "FIRST_YEAR",
        "THIRD_YEAR",
        "SECOND_YEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyLevel"


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
programmes_University_strategy = st.builds(
    programmes_University,
    name=
        safe_text
)
Programme_strategy = st.builds(
    Programme,
)
programmes_CourseGroup_strategy = st.builds(
    programmes_CourseGroup,
    name=
        safe_text,
    coursesType=
        safe_text
)
programmes_Semester_strategy = st.builds(
    programmes_Semester,
    semesterType=
        safe_text,
    year=
        st.integers()
)
programmes_Specialization_strategy = st.builds(
    programmes_Specialization,
)
programmes_Programme_strategy = st.builds(
    programmes_Programme,
    name=
        safe_text,
    code=
        safe_text
)
programmes_Course_strategy = st.builds(
    programmes_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text,
    level=
        safe_text
)

@given(instance=programmes_University_strategy)
@settings(max_examples=50)
def test_programmes_university_instantiation(instance):
    assert isinstance(instance, programmes_University)



@given(instance=programmes_University_strategy)
def test_programmes_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Programme_strategy)
@settings(max_examples=50)
def test_programme_instantiation(instance):
    assert isinstance(instance, Programme)

@given(instance=programmes_CourseGroup_strategy)
@settings(max_examples=50)
def test_programmes_coursegroup_instantiation(instance):
    assert isinstance(instance, programmes_CourseGroup)



@given(instance=programmes_CourseGroup_strategy)
def test_programmes_coursegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=programmes_CourseGroup_strategy)
def test_programmes_coursegroup_coursesType_setter(instance):
    original = instance.coursesType
    instance.coursesType = original
    assert instance.coursesType == original

@given(instance=programmes_Semester_strategy)
@settings(max_examples=50)
def test_programmes_semester_instantiation(instance):
    assert isinstance(instance, programmes_Semester)



@given(instance=programmes_Semester_strategy)
def test_programmes_semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original



@given(instance=programmes_Semester_strategy)
def test_programmes_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=programmes_Specialization_strategy)
@settings(max_examples=50)
def test_programmes_specialization_instantiation(instance):
    assert isinstance(instance, programmes_Specialization)

@given(instance=programmes_Programme_strategy)
@settings(max_examples=50)
def test_programmes_programme_instantiation(instance):
    assert isinstance(instance, programmes_Programme)



@given(instance=programmes_Programme_strategy)
def test_programmes_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=programmes_Programme_strategy)
def test_programmes_programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=programmes_Course_strategy)
@settings(max_examples=50)
def test_programmes_course_instantiation(instance):
    assert isinstance(instance, programmes_Course)



@given(instance=programmes_Course_strategy)
def test_programmes_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=programmes_Course_strategy)
def test_programmes_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=programmes_Course_strategy)
def test_programmes_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=programmes_Course_strategy)
def test_programmes_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original
