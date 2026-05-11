import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    programme::SemesterCourse,
    programme::Semester,
    programme::StudyYear,
    programme::Specialization,
    programme::Course,
    programme::Programme,
    programme::Department,
    SemesterType,
    CourseType,
    CourseLevel,
    ProgrammeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_programme::semestercourse_is_not_abstract():
    assert not inspect.isabstract(programme::SemesterCourse)


def test_programme::semestercourse_constructor_exists():
    assert callable(programme::SemesterCourse.__init__)


def test_programme::semestercourse_constructor_args():
    sig = inspect.signature(programme::SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "courseType" in params, "Missing parameter 'courseType'"

def test_programme::semestercourse_has_courseType():
    assert hasattr(programme::SemesterCourse, "courseType")
    descriptor = None
    for klass in programme::SemesterCourse.__mro__:
        if "courseType" in klass.__dict__:
            descriptor = klass.__dict__["courseType"]
            break
    assert isinstance(descriptor, property)



def test_programme::semester_is_not_abstract():
    assert not inspect.isabstract(programme::Semester)


def test_programme::semester_constructor_exists():
    assert callable(programme::Semester.__init__)


def test_programme::semester_constructor_args():
    sig = inspect.signature(programme::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterType" in params, "Missing parameter 'semesterType'"

def test_programme::semester_has_semesterType():
    assert hasattr(programme::Semester, "semesterType")
    descriptor = None
    for klass in programme::Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)



def test_programme::studyyear_is_not_abstract():
    assert not inspect.isabstract(programme::StudyYear)


def test_programme::studyyear_constructor_exists():
    assert callable(programme::StudyYear.__init__)


def test_programme::studyyear_constructor_args():
    sig = inspect.signature(programme::StudyYear.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_programme::studyyear_has_year():
    assert hasattr(programme::StudyYear, "year")
    descriptor = None
    for klass in programme::StudyYear.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_programme::specialization_is_not_abstract():
    assert not inspect.isabstract(programme::Specialization)


def test_programme::specialization_constructor_exists():
    assert callable(programme::Specialization.__init__)


def test_programme::specialization_constructor_args():
    sig = inspect.signature(programme::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_programme::specialization_has_name():
    assert hasattr(programme::Specialization, "name")
    descriptor = None
    for klass in programme::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_programme::course_is_not_abstract():
    assert not inspect.isabstract(programme::Course)


def test_programme::course_constructor_exists():
    assert callable(programme::Course.__init__)


def test_programme::course_constructor_args():
    sig = inspect.signature(programme::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "taugtIn" in params, "Missing parameter 'taugtIn'"
    assert "credits" in params, "Missing parameter 'credits'"

def test_programme::course_has_level():
    assert hasattr(programme::Course, "level")
    descriptor = None
    for klass in programme::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_programme::course_has_code():
    assert hasattr(programme::Course, "code")
    descriptor = None
    for klass in programme::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_programme::course_has_name():
    assert hasattr(programme::Course, "name")
    descriptor = None
    for klass in programme::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programme::course_has_taugtIn():
    assert hasattr(programme::Course, "taugtIn")
    descriptor = None
    for klass in programme::Course.__mro__:
        if "taugtIn" in klass.__dict__:
            descriptor = klass.__dict__["taugtIn"]
            break
    assert isinstance(descriptor, property)

def test_programme::course_has_credits():
    assert hasattr(programme::Course, "credits")
    descriptor = None
    for klass in programme::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)



def test_programme::programme_is_not_abstract():
    assert not inspect.isabstract(programme::Programme)


def test_programme::programme_constructor_exists():
    assert callable(programme::Programme.__init__)


def test_programme::programme_constructor_args():
    sig = inspect.signature(programme::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "programmeType" in params, "Missing parameter 'programmeType'"
    assert "code" in params, "Missing parameter 'code'"

def test_programme::programme_has_name():
    assert hasattr(programme::Programme, "name")
    descriptor = None
    for klass in programme::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programme::programme_has_programmeType():
    assert hasattr(programme::Programme, "programmeType")
    descriptor = None
    for klass in programme::Programme.__mro__:
        if "programmeType" in klass.__dict__:
            descriptor = klass.__dict__["programmeType"]
            break
    assert isinstance(descriptor, property)

def test_programme::programme_has_code():
    assert hasattr(programme::Programme, "code")
    descriptor = None
    for klass in programme::Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_programme::department_is_not_abstract():
    assert not inspect.isabstract(programme::Department)


def test_programme::department_constructor_exists():
    assert callable(programme::Department.__init__)


def test_programme::department_constructor_args():
    sig = inspect.signature(programme::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_programme::department_has_name():
    assert hasattr(programme::Department, "name")
    descriptor = None
    for klass in programme::Department.__mro__:
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
        "SPRING",
        "FALL",
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
        "M2A",
        "Elective",
        "Obligatory",
        "M1A",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseType"

def test_courselevel_exists():
    # Check that the Enumeration exists
    assert CourseLevel is not None

def test_courselevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseLevel]
    expected_literals = [
        "PHD",
        "THIRD_YEAR",
        "HIGHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseLevel"

def test_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "MASTER_2_YEARS",
        "YEAR_STUDY",
        "INTEGRATED_MASTER",
        "BACHELOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeType"


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
programme::SemesterCourse_strategy = st.builds(
    programme::SemesterCourse,
    courseType=
        safe_text
)
programme::Semester_strategy = st.builds(
    programme::Semester,
    semesterType=
        safe_text
)
programme::StudyYear_strategy = st.builds(
    programme::StudyYear,
    year=
        st.integers()
)
programme::Specialization_strategy = st.builds(
    programme::Specialization,
    name=
        safe_text
)
programme::Course_strategy = st.builds(
    programme::Course,
    level=
        safe_text,
    code=
        safe_text,
    name=
        safe_text,
    taugtIn=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
programme::Programme_strategy = st.builds(
    programme::Programme,
    name=
        safe_text,
    programmeType=
        safe_text,
    code=
        safe_text
)
programme::Department_strategy = st.builds(
    programme::Department,
    name=
        safe_text
)

@given(instance=programme::SemesterCourse_strategy)
@settings(max_examples=50)
def test_programme::semestercourse_instantiation(instance):
    assert isinstance(instance, programme::SemesterCourse)

@given(instance=programme::SemesterCourse_strategy)
def test_programme::semestercourse_courseType_type(instance):
    assert isinstance(instance.courseType, str)


@given(instance=programme::SemesterCourse_strategy)
def test_programme::semestercourse_courseType_setter(instance):
    original = instance.courseType
    instance.courseType = original
    assert instance.courseType == original

@given(instance=programme::Semester_strategy)
@settings(max_examples=50)
def test_programme::semester_instantiation(instance):
    assert isinstance(instance, programme::Semester)

@given(instance=programme::Semester_strategy)
def test_programme::semester_semesterType_type(instance):
    assert isinstance(instance.semesterType, str)


@given(instance=programme::Semester_strategy)
def test_programme::semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original

@given(instance=programme::StudyYear_strategy)
@settings(max_examples=50)
def test_programme::studyyear_instantiation(instance):
    assert isinstance(instance, programme::StudyYear)

@given(instance=programme::StudyYear_strategy)
def test_programme::studyyear_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=programme::StudyYear_strategy)
def test_programme::studyyear_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=programme::Specialization_strategy)
@settings(max_examples=50)
def test_programme::specialization_instantiation(instance):
    assert isinstance(instance, programme::Specialization)

@given(instance=programme::Specialization_strategy)
def test_programme::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programme::Specialization_strategy)
def test_programme::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programme::Course_strategy)
@settings(max_examples=50)
def test_programme::course_instantiation(instance):
    assert isinstance(instance, programme::Course)

@given(instance=programme::Course_strategy)
def test_programme::course_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=programme::Course_strategy)
def test_programme::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=programme::Course_strategy)
def test_programme::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=programme::Course_strategy)
def test_programme::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=programme::Course_strategy)
def test_programme::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programme::Course_strategy)
def test_programme::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programme::Course_strategy)
def test_programme::course_taugtIn_type(instance):
    assert isinstance(instance.taugtIn, str)


@given(instance=programme::Course_strategy)
def test_programme::course_taugtIn_setter(instance):
    original = instance.taugtIn
    instance.taugtIn = original
    assert instance.taugtIn == original

@given(instance=programme::Course_strategy)
def test_programme::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=programme::Course_strategy)
def test_programme::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=programme::Programme_strategy)
@settings(max_examples=50)
def test_programme::programme_instantiation(instance):
    assert isinstance(instance, programme::Programme)

@given(instance=programme::Programme_strategy)
def test_programme::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programme::Programme_strategy)
def test_programme::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programme::Programme_strategy)
def test_programme::programme_programmeType_type(instance):
    assert isinstance(instance.programmeType, str)


@given(instance=programme::Programme_strategy)
def test_programme::programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original

@given(instance=programme::Programme_strategy)
def test_programme::programme_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=programme::Programme_strategy)
def test_programme::programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=programme::Department_strategy)
@settings(max_examples=50)
def test_programme::department_instantiation(instance):
    assert isinstance(instance, programme::Department)

@given(instance=programme::Department_strategy)
def test_programme::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=programme::Department_strategy)
def test_programme::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
