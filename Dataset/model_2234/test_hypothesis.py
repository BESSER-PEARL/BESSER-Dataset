import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyprogram::Specialisation,
    studyprogram::SemesterCourse,
    studyprogram::Semester,
    studyprogram::Year,
    studyprogram::ObligatoryCourses,
    studyprogram::ElectiveCourses,
    studyprogram::StudyPlan,
    studyprogram::Program,
    studyprogram::Course,
    studyprogram::Department,
    studyprogram::University,
    SemesterType,
    CourseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogram::specialisation_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Specialisation)


def test_studyprogram::specialisation_constructor_exists():
    assert callable(studyprogram::Specialisation.__init__)


def test_studyprogram::specialisation_constructor_args():
    sig = inspect.signature(studyprogram::Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::specialisation_has_name():
    assert hasattr(studyprogram::Specialisation, "name")
    descriptor = None
    for klass in studyprogram::Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::semestercourse_is_not_abstract():
    assert not inspect.isabstract(studyprogram::SemesterCourse)


def test_studyprogram::semestercourse_constructor_exists():
    assert callable(studyprogram::SemesterCourse.__init__)


def test_studyprogram::semestercourse_constructor_args():
    sig = inspect.signature(studyprogram::SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_studyprogram::semestercourse_has_name():
    assert hasattr(studyprogram::SemesterCourse, "name")
    descriptor = None
    for klass in studyprogram::SemesterCourse.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram::semestercourse_has_type():
    assert hasattr(studyprogram::SemesterCourse, "type")
    descriptor = None
    for klass in studyprogram::SemesterCourse.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::semester_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Semester)


def test_studyprogram::semester_constructor_exists():
    assert callable(studyprogram::Semester.__init__)


def test_studyprogram::semester_constructor_args():
    sig = inspect.signature(studyprogram::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_studyprogram::semester_has_type():
    assert hasattr(studyprogram::Semester, "type")
    descriptor = None
    for klass in studyprogram::Semester.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::year_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Year)


def test_studyprogram::year_constructor_exists():
    assert callable(studyprogram::Year.__init__)


def test_studyprogram::year_constructor_args():
    sig = inspect.signature(studyprogram::Year.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_studyprogram::year_has_value():
    assert hasattr(studyprogram::Year, "value")
    descriptor = None
    for klass in studyprogram::Year.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::obligatorycourses_is_not_abstract():
    assert not inspect.isabstract(studyprogram::ObligatoryCourses)


def test_studyprogram::obligatorycourses_constructor_exists():
    assert callable(studyprogram::ObligatoryCourses.__init__)


def test_studyprogram::obligatorycourses_constructor_args():
    sig = inspect.signature(studyprogram::ObligatoryCourses.__init__)
    params = list(sig.parameters.keys())



def test_studyprogram::electivecourses_is_not_abstract():
    assert not inspect.isabstract(studyprogram::ElectiveCourses)


def test_studyprogram::electivecourses_constructor_exists():
    assert callable(studyprogram::ElectiveCourses.__init__)


def test_studyprogram::electivecourses_constructor_args():
    sig = inspect.signature(studyprogram::ElectiveCourses.__init__)
    params = list(sig.parameters.keys())



def test_studyprogram::studyplan_is_not_abstract():
    assert not inspect.isabstract(studyprogram::StudyPlan)


def test_studyprogram::studyplan_constructor_exists():
    assert callable(studyprogram::StudyPlan.__init__)


def test_studyprogram::studyplan_constructor_args():
    sig = inspect.signature(studyprogram::StudyPlan.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::studyplan_has_name():
    assert hasattr(studyprogram::StudyPlan, "name")
    descriptor = None
    for klass in studyprogram::StudyPlan.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::program_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Program)


def test_studyprogram::program_constructor_exists():
    assert callable(studyprogram::Program.__init__)


def test_studyprogram::program_constructor_args():
    sig = inspect.signature(studyprogram::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::program_has_name():
    assert hasattr(studyprogram::Program, "name")
    descriptor = None
    for klass in studyprogram::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::course_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Course)


def test_studyprogram::course_constructor_exists():
    assert callable(studyprogram::Course.__init__)


def test_studyprogram::course_constructor_args():
    sig = inspect.signature(studyprogram::Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "semester" in params, "Missing parameter 'semester'"

def test_studyprogram::course_has_credits():
    assert hasattr(studyprogram::Course, "credits")
    descriptor = None
    for klass in studyprogram::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram::course_has_name():
    assert hasattr(studyprogram::Course, "name")
    descriptor = None
    for klass in studyprogram::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram::course_has_semester():
    assert hasattr(studyprogram::Course, "semester")
    descriptor = None
    for klass in studyprogram::Course.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::department_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Department)


def test_studyprogram::department_constructor_exists():
    assert callable(studyprogram::Department.__init__)


def test_studyprogram::department_constructor_args():
    sig = inspect.signature(studyprogram::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::department_has_name():
    assert hasattr(studyprogram::Department, "name")
    descriptor = None
    for klass in studyprogram::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::university_is_not_abstract():
    assert not inspect.isabstract(studyprogram::University)


def test_studyprogram::university_constructor_exists():
    assert callable(studyprogram::University.__init__)


def test_studyprogram::university_constructor_args():
    sig = inspect.signature(studyprogram::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::university_has_name():
    assert hasattr(studyprogram::University, "name")
    descriptor = None
    for klass in studyprogram::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_semestertype_exists():
    # Check that the Enumeration exists
    assert SemesterType is not None

def test_semestertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterType]
    expected_literals = [
        "Fall",
        "Spring",
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
        "Obligatory",
        "Elective",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseType"


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
studyprogram::Specialisation_strategy = st.builds(
    studyprogram::Specialisation,
    name=
        safe_text
)
studyprogram::SemesterCourse_strategy = st.builds(
    studyprogram::SemesterCourse,
    name=
        safe_text,
    type=
        safe_text
)
studyprogram::Semester_strategy = st.builds(
    studyprogram::Semester,
    type=
        safe_text
)
studyprogram::Year_strategy = st.builds(
    studyprogram::Year,
    value=
        st.integers()
)
studyprogram::ObligatoryCourses_strategy = st.builds(
    studyprogram::ObligatoryCourses,
)
studyprogram::ElectiveCourses_strategy = st.builds(
    studyprogram::ElectiveCourses,
)
studyprogram::StudyPlan_strategy = st.builds(
    studyprogram::StudyPlan,
    name=
        safe_text
)
studyprogram::Program_strategy = st.builds(
    studyprogram::Program,
    name=
        safe_text
)
studyprogram::Course_strategy = st.builds(
    studyprogram::Course,
    credits=
        safe_text,
    name=
        safe_text,
    semester=
        safe_text
)
studyprogram::Department_strategy = st.builds(
    studyprogram::Department,
    name=
        safe_text
)
studyprogram::University_strategy = st.builds(
    studyprogram::University,
    name=
        safe_text
)

@given(instance=studyprogram::Specialisation_strategy)
@settings(max_examples=50)
def test_studyprogram::specialisation_instantiation(instance):
    assert isinstance(instance, studyprogram::Specialisation)

@given(instance=studyprogram::Specialisation_strategy)
def test_studyprogram::specialisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Specialisation_strategy)
def test_studyprogram::specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::SemesterCourse_strategy)
@settings(max_examples=50)
def test_studyprogram::semestercourse_instantiation(instance):
    assert isinstance(instance, studyprogram::SemesterCourse)

@given(instance=studyprogram::SemesterCourse_strategy)
def test_studyprogram::semestercourse_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::SemesterCourse_strategy)
def test_studyprogram::semestercourse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::SemesterCourse_strategy)
def test_studyprogram::semestercourse_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=studyprogram::SemesterCourse_strategy)
def test_studyprogram::semestercourse_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=studyprogram::Semester_strategy)
@settings(max_examples=50)
def test_studyprogram::semester_instantiation(instance):
    assert isinstance(instance, studyprogram::Semester)

@given(instance=studyprogram::Semester_strategy)
def test_studyprogram::semester_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=studyprogram::Semester_strategy)
def test_studyprogram::semester_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=studyprogram::Year_strategy)
@settings(max_examples=50)
def test_studyprogram::year_instantiation(instance):
    assert isinstance(instance, studyprogram::Year)

@given(instance=studyprogram::Year_strategy)
def test_studyprogram::year_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=studyprogram::Year_strategy)
def test_studyprogram::year_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=studyprogram::ObligatoryCourses_strategy)
@settings(max_examples=50)
def test_studyprogram::obligatorycourses_instantiation(instance):
    assert isinstance(instance, studyprogram::ObligatoryCourses)

@given(instance=studyprogram::ElectiveCourses_strategy)
@settings(max_examples=50)
def test_studyprogram::electivecourses_instantiation(instance):
    assert isinstance(instance, studyprogram::ElectiveCourses)

@given(instance=studyprogram::StudyPlan_strategy)
@settings(max_examples=50)
def test_studyprogram::studyplan_instantiation(instance):
    assert isinstance(instance, studyprogram::StudyPlan)

@given(instance=studyprogram::StudyPlan_strategy)
def test_studyprogram::studyplan_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::StudyPlan_strategy)
def test_studyprogram::studyplan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::Program_strategy)
@settings(max_examples=50)
def test_studyprogram::program_instantiation(instance):
    assert isinstance(instance, studyprogram::Program)

@given(instance=studyprogram::Program_strategy)
def test_studyprogram::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Program_strategy)
def test_studyprogram::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::Course_strategy)
@settings(max_examples=50)
def test_studyprogram::course_instantiation(instance):
    assert isinstance(instance, studyprogram::Course)

@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_credits_type(instance):
    assert isinstance(instance.credits, str)


@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_semester_type(instance):
    assert isinstance(instance.semester, str)


@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=studyprogram::Department_strategy)
@settings(max_examples=50)
def test_studyprogram::department_instantiation(instance):
    assert isinstance(instance, studyprogram::Department)

@given(instance=studyprogram::Department_strategy)
def test_studyprogram::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Department_strategy)
def test_studyprogram::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::University_strategy)
@settings(max_examples=50)
def test_studyprogram::university_instantiation(instance):
    assert isinstance(instance, studyprogram::University)

@given(instance=studyprogram::University_strategy)
def test_studyprogram::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::University_strategy)
def test_studyprogram::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
