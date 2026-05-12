import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    programme_SemesterCourse,
    programme_Semester,
    programme_StudyYear,
    programme_Specialization,
    programme_Course,
    programme_Programme,
    programme_Department,
    SemesterType,
    CourseLevel,
    CourseType,
    ProgrammeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_programme_semestercourse_is_not_abstract():
    assert not inspect.isabstract(programme_SemesterCourse)


def test_programme_semestercourse_constructor_exists():
    assert callable(programme_SemesterCourse.__init__)


def test_programme_semestercourse_constructor_args():
    sig = inspect.signature(programme_SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "courseType" in params, "Missing parameter 'courseType'"

def test_programme_semestercourse_has_courseType():
    assert hasattr(programme_SemesterCourse, "courseType")
    descriptor = None
    for klass in programme_SemesterCourse.__mro__:
        if "courseType" in klass.__dict__:
            descriptor = klass.__dict__["courseType"]
            break
    assert isinstance(descriptor, property)



def test_programme_semester_is_not_abstract():
    assert not inspect.isabstract(programme_Semester)


def test_programme_semester_constructor_exists():
    assert callable(programme_Semester.__init__)


def test_programme_semester_constructor_args():
    sig = inspect.signature(programme_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterType" in params, "Missing parameter 'semesterType'"

def test_programme_semester_has_semesterType():
    assert hasattr(programme_Semester, "semesterType")
    descriptor = None
    for klass in programme_Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)



def test_programme_studyyear_is_not_abstract():
    assert not inspect.isabstract(programme_StudyYear)


def test_programme_studyyear_constructor_exists():
    assert callable(programme_StudyYear.__init__)


def test_programme_studyyear_constructor_args():
    sig = inspect.signature(programme_StudyYear.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_programme_studyyear_has_year():
    assert hasattr(programme_StudyYear, "year")
    descriptor = None
    for klass in programme_StudyYear.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_programme_specialization_is_not_abstract():
    assert not inspect.isabstract(programme_Specialization)


def test_programme_specialization_constructor_exists():
    assert callable(programme_Specialization.__init__)


def test_programme_specialization_constructor_args():
    sig = inspect.signature(programme_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_programme_specialization_has_name():
    assert hasattr(programme_Specialization, "name")
    descriptor = None
    for klass in programme_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_programme_course_is_not_abstract():
    assert not inspect.isabstract(programme_Course)


def test_programme_course_constructor_exists():
    assert callable(programme_Course.__init__)


def test_programme_course_constructor_args():
    sig = inspect.signature(programme_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "taugtIn" in params, "Missing parameter 'taugtIn'"
    assert "level" in params, "Missing parameter 'level'"

def test_programme_course_has_code():
    assert hasattr(programme_Course, "code")
    descriptor = None
    for klass in programme_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_programme_course_has_name():
    assert hasattr(programme_Course, "name")
    descriptor = None
    for klass in programme_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_programme_course_has_credits():
    assert hasattr(programme_Course, "credits")
    descriptor = None
    for klass in programme_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_programme_course_has_taugtIn():
    assert hasattr(programme_Course, "taugtIn")
    descriptor = None
    for klass in programme_Course.__mro__:
        if "taugtIn" in klass.__dict__:
            descriptor = klass.__dict__["taugtIn"]
            break
    assert isinstance(descriptor, property)

def test_programme_course_has_level():
    assert hasattr(programme_Course, "level")
    descriptor = None
    for klass in programme_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_programme_programme_is_not_abstract():
    assert not inspect.isabstract(programme_Programme)


def test_programme_programme_constructor_exists():
    assert callable(programme_Programme.__init__)


def test_programme_programme_constructor_args():
    sig = inspect.signature(programme_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "programmeType" in params, "Missing parameter 'programmeType'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_programme_programme_has_programmeType():
    assert hasattr(programme_Programme, "programmeType")
    descriptor = None
    for klass in programme_Programme.__mro__:
        if "programmeType" in klass.__dict__:
            descriptor = klass.__dict__["programmeType"]
            break
    assert isinstance(descriptor, property)

def test_programme_programme_has_code():
    assert hasattr(programme_Programme, "code")
    descriptor = None
    for klass in programme_Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_programme_programme_has_name():
    assert hasattr(programme_Programme, "name")
    descriptor = None
    for klass in programme_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_programme_department_is_not_abstract():
    assert not inspect.isabstract(programme_Department)


def test_programme_department_constructor_exists():
    assert callable(programme_Department.__init__)


def test_programme_department_constructor_args():
    sig = inspect.signature(programme_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_programme_department_has_name():
    assert hasattr(programme_Department, "name")
    descriptor = None
    for klass in programme_Department.__mro__:
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

def test_courselevel_exists():
    # Check that the Enumeration exists
    assert CourseLevel is not None

def test_courselevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseLevel]
    expected_literals = [
        "THIRD_YEAR",
        "PHD",
        "HIGHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseLevel"

def test_coursetype_exists():
    # Check that the Enumeration exists
    assert CourseType is not None

def test_coursetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseType]
    expected_literals = [
        "M2A",
        "Obligatory",
        "Elective",
        "M1A",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseType"

def test_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "INTEGRATED_MASTER",
        "BACHELOR",
        "MASTER_2_YEARS",
        "YEAR_STUDY",
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
programme_SemesterCourse_strategy = st.builds(
    programme_SemesterCourse,
    courseType=
        safe_text
)
programme_Semester_strategy = st.builds(
    programme_Semester,
    semesterType=
        safe_text
)
programme_StudyYear_strategy = st.builds(
    programme_StudyYear,
    year=
        st.integers()
)
programme_Specialization_strategy = st.builds(
    programme_Specialization,
    name=
        safe_text
)
programme_Course_strategy = st.builds(
    programme_Course,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    taugtIn=
        safe_text,
    level=
        safe_text
)
programme_Programme_strategy = st.builds(
    programme_Programme,
    programmeType=
        safe_text,
    code=
        safe_text,
    name=
        safe_text
)
programme_Department_strategy = st.builds(
    programme_Department,
    name=
        safe_text
)

@given(instance=programme_SemesterCourse_strategy)
@settings(max_examples=50)
def test_programme_semestercourse_instantiation(instance):
    assert isinstance(instance, programme_SemesterCourse)



@given(instance=programme_SemesterCourse_strategy)
def test_programme_semestercourse_courseType_setter(instance):
    original = instance.courseType
    instance.courseType = original
    assert instance.courseType == original

@given(instance=programme_Semester_strategy)
@settings(max_examples=50)
def test_programme_semester_instantiation(instance):
    assert isinstance(instance, programme_Semester)



@given(instance=programme_Semester_strategy)
def test_programme_semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original

@given(instance=programme_StudyYear_strategy)
@settings(max_examples=50)
def test_programme_studyyear_instantiation(instance):
    assert isinstance(instance, programme_StudyYear)



@given(instance=programme_StudyYear_strategy)
def test_programme_studyyear_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=programme_Specialization_strategy)
@settings(max_examples=50)
def test_programme_specialization_instantiation(instance):
    assert isinstance(instance, programme_Specialization)



@given(instance=programme_Specialization_strategy)
def test_programme_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programme_Course_strategy)
@settings(max_examples=50)
def test_programme_course_instantiation(instance):
    assert isinstance(instance, programme_Course)



@given(instance=programme_Course_strategy)
def test_programme_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=programme_Course_strategy)
def test_programme_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=programme_Course_strategy)
def test_programme_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=programme_Course_strategy)
def test_programme_course_taugtIn_setter(instance):
    original = instance.taugtIn
    instance.taugtIn = original
    assert instance.taugtIn == original



@given(instance=programme_Course_strategy)
def test_programme_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=programme_Programme_strategy)
@settings(max_examples=50)
def test_programme_programme_instantiation(instance):
    assert isinstance(instance, programme_Programme)



@given(instance=programme_Programme_strategy)
def test_programme_programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original



@given(instance=programme_Programme_strategy)
def test_programme_programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=programme_Programme_strategy)
def test_programme_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=programme_Department_strategy)
@settings(max_examples=50)
def test_programme_department_instantiation(instance):
    assert isinstance(instance, programme_Department)



@given(instance=programme_Department_strategy)
def test_programme_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
