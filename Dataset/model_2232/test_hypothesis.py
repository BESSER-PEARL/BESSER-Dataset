import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyprogram_SemesterCourse,
    studyprogram_Semester,
    studyprogram_Department,
    studyprogram_University,
    studyprogram_Year,
    studyprogram_ObligatoryCourses,
    studyprogram_ElectiveCourses,
    studyprogram_StudyPlan,
    studyprogram_Program,
    studyprogram_Course,
    SemesterType,
    CourseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogram_semestercourse_is_not_abstract():
    assert not inspect.isabstract(studyprogram_SemesterCourse)


def test_studyprogram_semestercourse_constructor_exists():
    assert callable(studyprogram_SemesterCourse.__init__)


def test_studyprogram_semestercourse_constructor_args():
    sig = inspect.signature(studyprogram_SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_studyprogram_semestercourse_has_name():
    assert hasattr(studyprogram_SemesterCourse, "name")
    descriptor = None
    for klass in studyprogram_SemesterCourse.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram_semestercourse_has_type():
    assert hasattr(studyprogram_SemesterCourse, "type")
    descriptor = None
    for klass in studyprogram_SemesterCourse.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_semester_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Semester)


def test_studyprogram_semester_constructor_exists():
    assert callable(studyprogram_Semester.__init__)


def test_studyprogram_semester_constructor_args():
    sig = inspect.signature(studyprogram_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_studyprogram_semester_has_type():
    assert hasattr(studyprogram_Semester, "type")
    descriptor = None
    for klass in studyprogram_Semester.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_department_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Department)


def test_studyprogram_department_constructor_exists():
    assert callable(studyprogram_Department.__init__)


def test_studyprogram_department_constructor_args():
    sig = inspect.signature(studyprogram_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_department_has_name():
    assert hasattr(studyprogram_Department, "name")
    descriptor = None
    for klass in studyprogram_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_university_is_not_abstract():
    assert not inspect.isabstract(studyprogram_University)


def test_studyprogram_university_constructor_exists():
    assert callable(studyprogram_University.__init__)


def test_studyprogram_university_constructor_args():
    sig = inspect.signature(studyprogram_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_university_has_name():
    assert hasattr(studyprogram_University, "name")
    descriptor = None
    for klass in studyprogram_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_year_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Year)


def test_studyprogram_year_constructor_exists():
    assert callable(studyprogram_Year.__init__)


def test_studyprogram_year_constructor_args():
    sig = inspect.signature(studyprogram_Year.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_studyprogram_year_has_value():
    assert hasattr(studyprogram_Year, "value")
    descriptor = None
    for klass in studyprogram_Year.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_obligatorycourses_is_not_abstract():
    assert not inspect.isabstract(studyprogram_ObligatoryCourses)


def test_studyprogram_obligatorycourses_constructor_exists():
    assert callable(studyprogram_ObligatoryCourses.__init__)


def test_studyprogram_obligatorycourses_constructor_args():
    sig = inspect.signature(studyprogram_ObligatoryCourses.__init__)
    params = list(sig.parameters.keys())



def test_studyprogram_electivecourses_is_not_abstract():
    assert not inspect.isabstract(studyprogram_ElectiveCourses)


def test_studyprogram_electivecourses_constructor_exists():
    assert callable(studyprogram_ElectiveCourses.__init__)


def test_studyprogram_electivecourses_constructor_args():
    sig = inspect.signature(studyprogram_ElectiveCourses.__init__)
    params = list(sig.parameters.keys())



def test_studyprogram_studyplan_is_not_abstract():
    assert not inspect.isabstract(studyprogram_StudyPlan)


def test_studyprogram_studyplan_constructor_exists():
    assert callable(studyprogram_StudyPlan.__init__)


def test_studyprogram_studyplan_constructor_args():
    sig = inspect.signature(studyprogram_StudyPlan.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_studyplan_has_name():
    assert hasattr(studyprogram_StudyPlan, "name")
    descriptor = None
    for klass in studyprogram_StudyPlan.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_program_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Program)


def test_studyprogram_program_constructor_exists():
    assert callable(studyprogram_Program.__init__)


def test_studyprogram_program_constructor_args():
    sig = inspect.signature(studyprogram_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_program_has_name():
    assert hasattr(studyprogram_Program, "name")
    descriptor = None
    for klass in studyprogram_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_course_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Course)


def test_studyprogram_course_constructor_exists():
    assert callable(studyprogram_Course.__init__)


def test_studyprogram_course_constructor_args():
    sig = inspect.signature(studyprogram_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "semester" in params, "Missing parameter 'semester'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_course_has_code():
    assert hasattr(studyprogram_Course, "code")
    descriptor = None
    for klass in studyprogram_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram_course_has_credits():
    assert hasattr(studyprogram_Course, "credits")
    descriptor = None
    for klass in studyprogram_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram_course_has_semester():
    assert hasattr(studyprogram_Course, "semester")
    descriptor = None
    for klass in studyprogram_Course.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram_course_has_name():
    assert hasattr(studyprogram_Course, "name")
    descriptor = None
    for klass in studyprogram_Course.__mro__:
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
studyprogram_SemesterCourse_strategy = st.builds(
    studyprogram_SemesterCourse,
    name=
        safe_text,
    type=
        safe_text
)
studyprogram_Semester_strategy = st.builds(
    studyprogram_Semester,
    type=
        safe_text
)
studyprogram_Department_strategy = st.builds(
    studyprogram_Department,
    name=
        safe_text
)
studyprogram_University_strategy = st.builds(
    studyprogram_University,
    name=
        safe_text
)
studyprogram_Year_strategy = st.builds(
    studyprogram_Year,
    value=
        st.integers()
)
studyprogram_ObligatoryCourses_strategy = st.builds(
    studyprogram_ObligatoryCourses,
)
studyprogram_ElectiveCourses_strategy = st.builds(
    studyprogram_ElectiveCourses,
)
studyprogram_StudyPlan_strategy = st.builds(
    studyprogram_StudyPlan,
    name=
        safe_text
)
studyprogram_Program_strategy = st.builds(
    studyprogram_Program,
    name=
        safe_text
)
studyprogram_Course_strategy = st.builds(
    studyprogram_Course,
    code=
        safe_text,
    credits=
        safe_text,
    semester=
        safe_text,
    name=
        safe_text
)

@given(instance=studyprogram_SemesterCourse_strategy)
@settings(max_examples=50)
def test_studyprogram_semestercourse_instantiation(instance):
    assert isinstance(instance, studyprogram_SemesterCourse)



@given(instance=studyprogram_SemesterCourse_strategy)
def test_studyprogram_semestercourse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyprogram_SemesterCourse_strategy)
def test_studyprogram_semestercourse_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=studyprogram_Semester_strategy)
@settings(max_examples=50)
def test_studyprogram_semester_instantiation(instance):
    assert isinstance(instance, studyprogram_Semester)



@given(instance=studyprogram_Semester_strategy)
def test_studyprogram_semester_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=studyprogram_Department_strategy)
@settings(max_examples=50)
def test_studyprogram_department_instantiation(instance):
    assert isinstance(instance, studyprogram_Department)



@given(instance=studyprogram_Department_strategy)
def test_studyprogram_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_University_strategy)
@settings(max_examples=50)
def test_studyprogram_university_instantiation(instance):
    assert isinstance(instance, studyprogram_University)



@given(instance=studyprogram_University_strategy)
def test_studyprogram_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_Year_strategy)
@settings(max_examples=50)
def test_studyprogram_year_instantiation(instance):
    assert isinstance(instance, studyprogram_Year)



@given(instance=studyprogram_Year_strategy)
def test_studyprogram_year_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=studyprogram_ObligatoryCourses_strategy)
@settings(max_examples=50)
def test_studyprogram_obligatorycourses_instantiation(instance):
    assert isinstance(instance, studyprogram_ObligatoryCourses)

@given(instance=studyprogram_ElectiveCourses_strategy)
@settings(max_examples=50)
def test_studyprogram_electivecourses_instantiation(instance):
    assert isinstance(instance, studyprogram_ElectiveCourses)

@given(instance=studyprogram_StudyPlan_strategy)
@settings(max_examples=50)
def test_studyprogram_studyplan_instantiation(instance):
    assert isinstance(instance, studyprogram_StudyPlan)



@given(instance=studyprogram_StudyPlan_strategy)
def test_studyprogram_studyplan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_Program_strategy)
@settings(max_examples=50)
def test_studyprogram_program_instantiation(instance):
    assert isinstance(instance, studyprogram_Program)



@given(instance=studyprogram_Program_strategy)
def test_studyprogram_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_Course_strategy)
@settings(max_examples=50)
def test_studyprogram_course_instantiation(instance):
    assert isinstance(instance, studyprogram_Course)



@given(instance=studyprogram_Course_strategy)
def test_studyprogram_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=studyprogram_Course_strategy)
def test_studyprogram_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyprogram_Course_strategy)
def test_studyprogram_course_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original



@given(instance=studyprogram_Course_strategy)
def test_studyprogram_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
