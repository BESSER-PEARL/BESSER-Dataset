import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyPlan::Specialization,
    studyPlan::StudyPlan,
    studyPlan::StudyProgramme,
    studyPlan::Student,
    studyPlan::University,
    studyPlan::Course,
    Semester,
    studyPlan::SemesterProgramme,
    studyPlan::Semester,
    studyPlan::SemesterPlan,
    SeasonEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyplan::specialization_is_not_abstract():
    assert not inspect.isabstract(studyPlan::Specialization)


def test_studyplan::specialization_constructor_exists():
    assert callable(studyPlan::Specialization.__init__)


def test_studyplan::specialization_constructor_args():
    sig = inspect.signature(studyPlan::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan::specialization_has_name():
    assert hasattr(studyPlan::Specialization, "name")
    descriptor = None
    for klass in studyPlan::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::specialization_has_year():
    assert hasattr(studyPlan::Specialization, "year")
    descriptor = None
    for klass in studyPlan::Specialization.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::studyplan_is_not_abstract():
    assert not inspect.isabstract(studyPlan::StudyPlan)


def test_studyplan::studyplan_constructor_exists():
    assert callable(studyPlan::StudyPlan.__init__)


def test_studyplan::studyplan_constructor_args():
    sig = inspect.signature(studyPlan::StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_studyplan::studyprogramme_is_not_abstract():
    assert not inspect.isabstract(studyPlan::StudyProgramme)


def test_studyplan::studyprogramme_constructor_exists():
    assert callable(studyPlan::StudyProgramme.__init__)


def test_studyplan::studyprogramme_constructor_args():
    sig = inspect.signature(studyPlan::StudyProgramme.__init__)
    params = list(sig.parameters.keys())
    assert "lengthInYears" in params, "Missing parameter 'lengthInYears'"
    assert "codename" in params, "Missing parameter 'codename'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan::studyprogramme_has_lengthInYears():
    assert hasattr(studyPlan::StudyProgramme, "lengthInYears")
    descriptor = None
    for klass in studyPlan::StudyProgramme.__mro__:
        if "lengthInYears" in klass.__dict__:
            descriptor = klass.__dict__["lengthInYears"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::studyprogramme_has_codename():
    assert hasattr(studyPlan::StudyProgramme, "codename")
    descriptor = None
    for klass in studyPlan::StudyProgramme.__mro__:
        if "codename" in klass.__dict__:
            descriptor = klass.__dict__["codename"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::studyprogramme_has_name():
    assert hasattr(studyPlan::StudyProgramme, "name")
    descriptor = None
    for klass in studyPlan::StudyProgramme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::student_is_not_abstract():
    assert not inspect.isabstract(studyPlan::Student)


def test_studyplan::student_constructor_exists():
    assert callable(studyPlan::Student.__init__)


def test_studyplan::student_constructor_args():
    sig = inspect.signature(studyPlan::Student.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan::student_has_username():
    assert hasattr(studyPlan::Student, "username")
    descriptor = None
    for klass in studyPlan::Student.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::student_has_name():
    assert hasattr(studyPlan::Student, "name")
    descriptor = None
    for klass in studyPlan::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::university_is_not_abstract():
    assert not inspect.isabstract(studyPlan::University)


def test_studyplan::university_constructor_exists():
    assert callable(studyPlan::University.__init__)


def test_studyplan::university_constructor_args():
    sig = inspect.signature(studyPlan::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan::university_has_name():
    assert hasattr(studyPlan::University, "name")
    descriptor = None
    for klass in studyPlan::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::course_is_not_abstract():
    assert not inspect.isabstract(studyPlan::Course)


def test_studyplan::course_constructor_exists():
    assert callable(studyPlan::Course.__init__)


def test_studyplan::course_constructor_args():
    sig = inspect.signature(studyPlan::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "level" in params, "Missing parameter 'level'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "codename" in params, "Missing parameter 'codename'"

def test_studyplan::course_has_name():
    assert hasattr(studyPlan::Course, "name")
    descriptor = None
    for klass in studyPlan::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_level():
    assert hasattr(studyPlan::Course, "level")
    descriptor = None
    for klass in studyPlan::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_credits():
    assert hasattr(studyPlan::Course, "credits")
    descriptor = None
    for klass in studyPlan::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_codename():
    assert hasattr(studyPlan::Course, "codename")
    descriptor = None
    for klass in studyPlan::Course.__mro__:
        if "codename" in klass.__dict__:
            descriptor = klass.__dict__["codename"]
            break
    assert isinstance(descriptor, property)



def test_semester_is_not_abstract():
    assert not inspect.isabstract(Semester)


def test_semester_constructor_exists():
    assert callable(Semester.__init__)


def test_semester_constructor_args():
    sig = inspect.signature(Semester.__init__)
    params = list(sig.parameters.keys())



def test_studyplan::semesterprogramme_is_not_abstract():
    assert not inspect.isabstract(studyPlan::SemesterProgramme)


def test_studyplan::semesterprogramme_constructor_exists():
    assert callable(studyPlan::SemesterProgramme.__init__)


def test_studyplan::semesterprogramme_constructor_args():
    sig = inspect.signature(studyPlan::SemesterProgramme.__init__)
    params = list(sig.parameters.keys())



def test_studyplan::semester_is_not_abstract():
    assert not inspect.isabstract(studyPlan::Semester)


def test_studyplan::semester_constructor_exists():
    assert callable(studyPlan::Semester.__init__)


def test_studyplan::semester_constructor_args():
    sig = inspect.signature(studyPlan::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "codename" in params, "Missing parameter 'codename'"
    assert "season" in params, "Missing parameter 'season'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan::semester_has_codename():
    assert hasattr(studyPlan::Semester, "codename")
    descriptor = None
    for klass in studyPlan::Semester.__mro__:
        if "codename" in klass.__dict__:
            descriptor = klass.__dict__["codename"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::semester_has_season():
    assert hasattr(studyPlan::Semester, "season")
    descriptor = None
    for klass in studyPlan::Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::semester_has_year():
    assert hasattr(studyPlan::Semester, "year")
    descriptor = None
    for klass in studyPlan::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::semesterplan_is_not_abstract():
    assert not inspect.isabstract(studyPlan::SemesterPlan)


def test_studyplan::semesterplan_constructor_exists():
    assert callable(studyPlan::SemesterPlan.__init__)


def test_studyplan::semesterplan_constructor_args():
    sig = inspect.signature(studyPlan::SemesterPlan.__init__)
    params = list(sig.parameters.keys())

def test_seasonenum_exists():
    # Check that the Enumeration exists
    assert SeasonEnum is not None

def test_seasonenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeasonEnum]
    expected_literals = [
        "Vår",
        "Høst",
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
studyPlan::Specialization_strategy = st.builds(
    studyPlan::Specialization,
    name=
        safe_text,
    year=
        st.integers()
)
studyPlan::StudyPlan_strategy = st.builds(
    studyPlan::StudyPlan,
)
studyPlan::StudyProgramme_strategy = st.builds(
    studyPlan::StudyProgramme,
    lengthInYears=
        st.integers(),
    codename=
        safe_text,
    name=
        safe_text
)
studyPlan::Student_strategy = st.builds(
    studyPlan::Student,
    username=
        safe_text,
    name=
        safe_text
)
studyPlan::University_strategy = st.builds(
    studyPlan::University,
    name=
        safe_text
)
studyPlan::Course_strategy = st.builds(
    studyPlan::Course,
    name=
        safe_text,
    level=
        st.integers(),
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    codename=
        safe_text
)
Semester_strategy = st.builds(
    Semester,
)
studyPlan::SemesterProgramme_strategy = st.builds(
    studyPlan::SemesterProgramme,
)
studyPlan::Semester_strategy = st.builds(
    studyPlan::Semester,
    codename=
        safe_text,
    season=
        safe_text,
    year=
        st.integers()
)
studyPlan::SemesterPlan_strategy = st.builds(
    studyPlan::SemesterPlan,
)

@given(instance=studyPlan::Specialization_strategy)
@settings(max_examples=50)
def test_studyplan::specialization_instantiation(instance):
    assert isinstance(instance, studyPlan::Specialization)

@given(instance=studyPlan::Specialization_strategy)
def test_studyplan::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyPlan::Specialization_strategy)
def test_studyplan::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan::Specialization_strategy)
def test_studyplan::specialization_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyPlan::Specialization_strategy)
def test_studyplan::specialization_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyPlan::StudyPlan_strategy)
@settings(max_examples=50)
def test_studyplan::studyplan_instantiation(instance):
    assert isinstance(instance, studyPlan::StudyPlan)

@given(instance=studyPlan::StudyProgramme_strategy)
@settings(max_examples=50)
def test_studyplan::studyprogramme_instantiation(instance):
    assert isinstance(instance, studyPlan::StudyProgramme)

@given(instance=studyPlan::StudyProgramme_strategy)
def test_studyplan::studyprogramme_lengthInYears_type(instance):
    assert isinstance(instance.lengthInYears, int)


@given(instance=studyPlan::StudyProgramme_strategy)
def test_studyplan::studyprogramme_lengthInYears_setter(instance):
    original = instance.lengthInYears
    instance.lengthInYears = original
    assert instance.lengthInYears == original

@given(instance=studyPlan::StudyProgramme_strategy)
def test_studyplan::studyprogramme_codename_type(instance):
    assert isinstance(instance.codename, str)


@given(instance=studyPlan::StudyProgramme_strategy)
def test_studyplan::studyprogramme_codename_setter(instance):
    original = instance.codename
    instance.codename = original
    assert instance.codename == original

@given(instance=studyPlan::StudyProgramme_strategy)
def test_studyplan::studyprogramme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyPlan::StudyProgramme_strategy)
def test_studyplan::studyprogramme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan::Student_strategy)
@settings(max_examples=50)
def test_studyplan::student_instantiation(instance):
    assert isinstance(instance, studyPlan::Student)

@given(instance=studyPlan::Student_strategy)
def test_studyplan::student_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=studyPlan::Student_strategy)
def test_studyplan::student_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=studyPlan::Student_strategy)
def test_studyplan::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyPlan::Student_strategy)
def test_studyplan::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan::University_strategy)
@settings(max_examples=50)
def test_studyplan::university_instantiation(instance):
    assert isinstance(instance, studyPlan::University)

@given(instance=studyPlan::University_strategy)
def test_studyplan::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyPlan::University_strategy)
def test_studyplan::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan::Course_strategy)
@settings(max_examples=50)
def test_studyplan::course_instantiation(instance):
    assert isinstance(instance, studyPlan::Course)

@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_codename_type(instance):
    assert isinstance(instance.codename, str)


@given(instance=studyPlan::Course_strategy)
def test_studyplan::course_codename_setter(instance):
    original = instance.codename
    instance.codename = original
    assert instance.codename == original

@given(instance=Semester_strategy)
@settings(max_examples=50)
def test_semester_instantiation(instance):
    assert isinstance(instance, Semester)

@given(instance=studyPlan::SemesterProgramme_strategy)
@settings(max_examples=50)
def test_studyplan::semesterprogramme_instantiation(instance):
    assert isinstance(instance, studyPlan::SemesterProgramme)

@given(instance=studyPlan::Semester_strategy)
@settings(max_examples=50)
def test_studyplan::semester_instantiation(instance):
    assert isinstance(instance, studyPlan::Semester)

@given(instance=studyPlan::Semester_strategy)
def test_studyplan::semester_codename_type(instance):
    assert isinstance(instance.codename, str)


@given(instance=studyPlan::Semester_strategy)
def test_studyplan::semester_codename_setter(instance):
    original = instance.codename
    instance.codename = original
    assert instance.codename == original

@given(instance=studyPlan::Semester_strategy)
def test_studyplan::semester_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=studyPlan::Semester_strategy)
def test_studyplan::semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=studyPlan::Semester_strategy)
def test_studyplan::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyPlan::Semester_strategy)
def test_studyplan::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyPlan::SemesterPlan_strategy)
@settings(max_examples=50)
def test_studyplan::semesterplan_instantiation(instance):
    assert isinstance(instance, studyPlan::SemesterPlan)
