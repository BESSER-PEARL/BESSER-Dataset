import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyPlan_Specialization,
    studyPlan_StudyPlan,
    studyPlan_StudyProgramme,
    studyPlan_Student,
    studyPlan_University,
    studyPlan_Course,
    Semester,
    studyPlan_SemesterProgramme,
    studyPlan_Semester,
    studyPlan_SemesterPlan,
    SeasonEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyplan_specialization_is_not_abstract():
    assert not inspect.isabstract(studyPlan_Specialization)


def test_studyplan_specialization_constructor_exists():
    assert callable(studyPlan_Specialization.__init__)


def test_studyplan_specialization_constructor_args():
    sig = inspect.signature(studyPlan_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan_specialization_has_name():
    assert hasattr(studyPlan_Specialization, "name")
    descriptor = None
    for klass in studyPlan_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_specialization_has_year():
    assert hasattr(studyPlan_Specialization, "year")
    descriptor = None
    for klass in studyPlan_Specialization.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_studyplan_is_not_abstract():
    assert not inspect.isabstract(studyPlan_StudyPlan)


def test_studyplan_studyplan_constructor_exists():
    assert callable(studyPlan_StudyPlan.__init__)


def test_studyplan_studyplan_constructor_args():
    sig = inspect.signature(studyPlan_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_studyplan_studyprogramme_is_not_abstract():
    assert not inspect.isabstract(studyPlan_StudyProgramme)


def test_studyplan_studyprogramme_constructor_exists():
    assert callable(studyPlan_StudyProgramme.__init__)


def test_studyplan_studyprogramme_constructor_args():
    sig = inspect.signature(studyPlan_StudyProgramme.__init__)
    params = list(sig.parameters.keys())
    assert "codename" in params, "Missing parameter 'codename'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lengthInYears" in params, "Missing parameter 'lengthInYears'"

def test_studyplan_studyprogramme_has_codename():
    assert hasattr(studyPlan_StudyProgramme, "codename")
    descriptor = None
    for klass in studyPlan_StudyProgramme.__mro__:
        if "codename" in klass.__dict__:
            descriptor = klass.__dict__["codename"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_studyprogramme_has_name():
    assert hasattr(studyPlan_StudyProgramme, "name")
    descriptor = None
    for klass in studyPlan_StudyProgramme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_studyprogramme_has_lengthInYears():
    assert hasattr(studyPlan_StudyProgramme, "lengthInYears")
    descriptor = None
    for klass in studyPlan_StudyProgramme.__mro__:
        if "lengthInYears" in klass.__dict__:
            descriptor = klass.__dict__["lengthInYears"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_student_is_not_abstract():
    assert not inspect.isabstract(studyPlan_Student)


def test_studyplan_student_constructor_exists():
    assert callable(studyPlan_Student.__init__)


def test_studyplan_student_constructor_args():
    sig = inspect.signature(studyPlan_Student.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan_student_has_username():
    assert hasattr(studyPlan_Student, "username")
    descriptor = None
    for klass in studyPlan_Student.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_student_has_name():
    assert hasattr(studyPlan_Student, "name")
    descriptor = None
    for klass in studyPlan_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_university_is_not_abstract():
    assert not inspect.isabstract(studyPlan_University)


def test_studyplan_university_constructor_exists():
    assert callable(studyPlan_University.__init__)


def test_studyplan_university_constructor_args():
    sig = inspect.signature(studyPlan_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan_university_has_name():
    assert hasattr(studyPlan_University, "name")
    descriptor = None
    for klass in studyPlan_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_course_is_not_abstract():
    assert not inspect.isabstract(studyPlan_Course)


def test_studyplan_course_constructor_exists():
    assert callable(studyPlan_Course.__init__)


def test_studyplan_course_constructor_args():
    sig = inspect.signature(studyPlan_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "codename" in params, "Missing parameter 'codename'"
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan_course_has_credits():
    assert hasattr(studyPlan_Course, "credits")
    descriptor = None
    for klass in studyPlan_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_codename():
    assert hasattr(studyPlan_Course, "codename")
    descriptor = None
    for klass in studyPlan_Course.__mro__:
        if "codename" in klass.__dict__:
            descriptor = klass.__dict__["codename"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_level():
    assert hasattr(studyPlan_Course, "level")
    descriptor = None
    for klass in studyPlan_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_name():
    assert hasattr(studyPlan_Course, "name")
    descriptor = None
    for klass in studyPlan_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_semester_is_not_abstract():
    assert not inspect.isabstract(Semester)


def test_semester_constructor_exists():
    assert callable(Semester.__init__)


def test_semester_constructor_args():
    sig = inspect.signature(Semester.__init__)
    params = list(sig.parameters.keys())



def test_studyplan_semesterprogramme_is_not_abstract():
    assert not inspect.isabstract(studyPlan_SemesterProgramme)


def test_studyplan_semesterprogramme_constructor_exists():
    assert callable(studyPlan_SemesterProgramme.__init__)


def test_studyplan_semesterprogramme_constructor_args():
    sig = inspect.signature(studyPlan_SemesterProgramme.__init__)
    params = list(sig.parameters.keys())



def test_studyplan_semester_is_not_abstract():
    assert not inspect.isabstract(studyPlan_Semester)


def test_studyplan_semester_constructor_exists():
    assert callable(studyPlan_Semester.__init__)


def test_studyplan_semester_constructor_args():
    sig = inspect.signature(studyPlan_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"
    assert "codename" in params, "Missing parameter 'codename'"

def test_studyplan_semester_has_year():
    assert hasattr(studyPlan_Semester, "year")
    descriptor = None
    for klass in studyPlan_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_semester_has_season():
    assert hasattr(studyPlan_Semester, "season")
    descriptor = None
    for klass in studyPlan_Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_semester_has_codename():
    assert hasattr(studyPlan_Semester, "codename")
    descriptor = None
    for klass in studyPlan_Semester.__mro__:
        if "codename" in klass.__dict__:
            descriptor = klass.__dict__["codename"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_semesterplan_is_not_abstract():
    assert not inspect.isabstract(studyPlan_SemesterPlan)


def test_studyplan_semesterplan_constructor_exists():
    assert callable(studyPlan_SemesterPlan.__init__)


def test_studyplan_semesterplan_constructor_args():
    sig = inspect.signature(studyPlan_SemesterPlan.__init__)
    params = list(sig.parameters.keys())

def test_seasonenum_exists():
    # Check that the Enumeration exists
    assert SeasonEnum is not None

def test_seasonenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeasonEnum]
    expected_literals = [
        "Høst",
        "Vår",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeasonEnum"


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
studyPlan_Specialization_strategy = st.builds(
    studyPlan_Specialization,
    name=
        safe_text,
    year=
        st.integers()
)
studyPlan_StudyPlan_strategy = st.builds(
    studyPlan_StudyPlan,
)
studyPlan_StudyProgramme_strategy = st.builds(
    studyPlan_StudyProgramme,
    codename=
        safe_text,
    name=
        safe_text,
    lengthInYears=
        st.integers()
)
studyPlan_Student_strategy = st.builds(
    studyPlan_Student,
    username=
        safe_text,
    name=
        safe_text
)
studyPlan_University_strategy = st.builds(
    studyPlan_University,
    name=
        safe_text
)
studyPlan_Course_strategy = st.builds(
    studyPlan_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    codename=
        safe_text,
    level=
        st.integers(),
    name=
        safe_text
)
Semester_strategy = st.builds(
    Semester,
)
studyPlan_SemesterProgramme_strategy = st.builds(
    studyPlan_SemesterProgramme,
)
studyPlan_Semester_strategy = st.builds(
    studyPlan_Semester,
    year=
        st.integers(),
    season=
        safe_text,
    codename=
        safe_text
)
studyPlan_SemesterPlan_strategy = st.builds(
    studyPlan_SemesterPlan,
)

@given(instance=studyPlan_Specialization_strategy)
@settings(max_examples=50)
def test_studyplan_specialization_instantiation(instance):
    assert isinstance(instance, studyPlan_Specialization)



@given(instance=studyPlan_Specialization_strategy)
def test_studyplan_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyPlan_Specialization_strategy)
def test_studyplan_specialization_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyPlan_StudyPlan_strategy)
@settings(max_examples=50)
def test_studyplan_studyplan_instantiation(instance):
    assert isinstance(instance, studyPlan_StudyPlan)

@given(instance=studyPlan_StudyProgramme_strategy)
@settings(max_examples=50)
def test_studyplan_studyprogramme_instantiation(instance):
    assert isinstance(instance, studyPlan_StudyProgramme)



@given(instance=studyPlan_StudyProgramme_strategy)
def test_studyplan_studyprogramme_codename_setter(instance):
    original = instance.codename
    instance.codename = original
    assert instance.codename == original



@given(instance=studyPlan_StudyProgramme_strategy)
def test_studyplan_studyprogramme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyPlan_StudyProgramme_strategy)
def test_studyplan_studyprogramme_lengthInYears_setter(instance):
    original = instance.lengthInYears
    instance.lengthInYears = original
    assert instance.lengthInYears == original

@given(instance=studyPlan_Student_strategy)
@settings(max_examples=50)
def test_studyplan_student_instantiation(instance):
    assert isinstance(instance, studyPlan_Student)



@given(instance=studyPlan_Student_strategy)
def test_studyplan_student_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=studyPlan_Student_strategy)
def test_studyplan_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan_University_strategy)
@settings(max_examples=50)
def test_studyplan_university_instantiation(instance):
    assert isinstance(instance, studyPlan_University)



@given(instance=studyPlan_University_strategy)
def test_studyplan_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan_Course_strategy)
@settings(max_examples=50)
def test_studyplan_course_instantiation(instance):
    assert isinstance(instance, studyPlan_Course)



@given(instance=studyPlan_Course_strategy)
def test_studyplan_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyPlan_Course_strategy)
def test_studyplan_course_codename_setter(instance):
    original = instance.codename
    instance.codename = original
    assert instance.codename == original



@given(instance=studyPlan_Course_strategy)
def test_studyplan_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=studyPlan_Course_strategy)
def test_studyplan_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Semester_strategy)
@settings(max_examples=50)
def test_semester_instantiation(instance):
    assert isinstance(instance, Semester)

@given(instance=studyPlan_SemesterProgramme_strategy)
@settings(max_examples=50)
def test_studyplan_semesterprogramme_instantiation(instance):
    assert isinstance(instance, studyPlan_SemesterProgramme)

@given(instance=studyPlan_Semester_strategy)
@settings(max_examples=50)
def test_studyplan_semester_instantiation(instance):
    assert isinstance(instance, studyPlan_Semester)



@given(instance=studyPlan_Semester_strategy)
def test_studyplan_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=studyPlan_Semester_strategy)
def test_studyplan_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original



@given(instance=studyPlan_Semester_strategy)
def test_studyplan_semester_codename_setter(instance):
    original = instance.codename
    instance.codename = original
    assert instance.codename == original

@given(instance=studyPlan_SemesterPlan_strategy)
@settings(max_examples=50)
def test_studyplan_semesterplan_instantiation(instance):
    assert isinstance(instance, studyPlan_SemesterPlan)
