import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tdt4250::CourseGroup,
    tdt4250::Course,
    tdt4250::Specialisation,
    tdt4250::Student,
    tdt4250::StudyProgram,
    Semester,
    StudyProgramName,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tdt4250::coursegroup_is_not_abstract():
    assert not inspect.isabstract(tdt4250::CourseGroup)


def test_tdt4250::coursegroup_constructor_exists():
    assert callable(tdt4250::CourseGroup.__init__)


def test_tdt4250::coursegroup_constructor_args():
    sig = inspect.signature(tdt4250::CourseGroup.__init__)
    params = list(sig.parameters.keys())



def test_tdt4250::course_is_not_abstract():
    assert not inspect.isabstract(tdt4250::Course)


def test_tdt4250::course_constructor_exists():
    assert callable(tdt4250::Course.__init__)


def test_tdt4250::course_constructor_args():
    sig = inspect.signature(tdt4250::Course.__init__)
    params = list(sig.parameters.keys())
    assert "study_points" in params, "Missing parameter 'study_points'"
    assert "level" in params, "Missing parameter 'level'"
    assert "semester" in params, "Missing parameter 'semester'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_tdt4250::course_has_study_points():
    assert hasattr(tdt4250::Course, "study_points")
    descriptor = None
    for klass in tdt4250::Course.__mro__:
        if "study_points" in klass.__dict__:
            descriptor = klass.__dict__["study_points"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::course_has_level():
    assert hasattr(tdt4250::Course, "level")
    descriptor = None
    for klass in tdt4250::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::course_has_semester():
    assert hasattr(tdt4250::Course, "semester")
    descriptor = None
    for klass in tdt4250::Course.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::course_has_name():
    assert hasattr(tdt4250::Course, "name")
    descriptor = None
    for klass in tdt4250::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::course_has_code():
    assert hasattr(tdt4250::Course, "code")
    descriptor = None
    for klass in tdt4250::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::specialisation_is_not_abstract():
    assert not inspect.isabstract(tdt4250::Specialisation)


def test_tdt4250::specialisation_constructor_exists():
    assert callable(tdt4250::Specialisation.__init__)


def test_tdt4250::specialisation_constructor_args():
    sig = inspect.signature(tdt4250::Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250::specialisation_has_name():
    assert hasattr(tdt4250::Specialisation, "name")
    descriptor = None
    for klass in tdt4250::Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::student_is_not_abstract():
    assert not inspect.isabstract(tdt4250::Student)


def test_tdt4250::student_constructor_exists():
    assert callable(tdt4250::Student.__init__)


def test_tdt4250::student_constructor_args():
    sig = inspect.signature(tdt4250::Student.__init__)
    params = list(sig.parameters.keys())
    assert "current_semester" in params, "Missing parameter 'current_semester'"
    assert "studentID" in params, "Missing parameter 'studentID'"

def test_tdt4250::student_has_current_semester():
    assert hasattr(tdt4250::Student, "current_semester")
    descriptor = None
    for klass in tdt4250::Student.__mro__:
        if "current_semester" in klass.__dict__:
            descriptor = klass.__dict__["current_semester"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::student_has_studentID():
    assert hasattr(tdt4250::Student, "studentID")
    descriptor = None
    for klass in tdt4250::Student.__mro__:
        if "studentID" in klass.__dict__:
            descriptor = klass.__dict__["studentID"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::studyprogram_is_not_abstract():
    assert not inspect.isabstract(tdt4250::StudyProgram)


def test_tdt4250::studyprogram_constructor_exists():
    assert callable(tdt4250::StudyProgram.__init__)


def test_tdt4250::studyprogram_constructor_args():
    sig = inspect.signature(tdt4250::StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "number_of_semesters" in params, "Missing parameter 'number_of_semesters'"
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250::studyprogram_has_number_of_semesters():
    assert hasattr(tdt4250::StudyProgram, "number_of_semesters")
    descriptor = None
    for klass in tdt4250::StudyProgram.__mro__:
        if "number_of_semesters" in klass.__dict__:
            descriptor = klass.__dict__["number_of_semesters"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::studyprogram_has_name():
    assert hasattr(tdt4250::StudyProgram, "name")
    descriptor = None
    for klass in tdt4250::StudyProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_semester_exists():
    # Check that the Enumeration exists
    assert Semester is not None

def test_semester_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Semester]
    expected_literals = [
        "spring",
        "autumn",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Semester"

def test_studyprogramname_exists():
    # Check that the Enumeration exists
    assert StudyProgramName is not None

def test_studyprogramname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyProgramName]
    expected_literals = [
        "informatics",
        "computer_science_5_years",
        "computer_science_2_years",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyProgramName"


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
tdt4250::CourseGroup_strategy = st.builds(
    tdt4250::CourseGroup,
)
tdt4250::Course_strategy = st.builds(
    tdt4250::Course,
    study_points=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    level=
        safe_text,
    semester=
        safe_text,
    name=
        safe_text,
    code=
        safe_text
)
tdt4250::Specialisation_strategy = st.builds(
    tdt4250::Specialisation,
    name=
        safe_text
)
tdt4250::Student_strategy = st.builds(
    tdt4250::Student,
    current_semester=
        st.integers(),
    studentID=
        st.integers()
)
tdt4250::StudyProgram_strategy = st.builds(
    tdt4250::StudyProgram,
    number_of_semesters=
        st.integers(),
    name=
        safe_text
)

@given(instance=tdt4250::CourseGroup_strategy)
@settings(max_examples=50)
def test_tdt4250::coursegroup_instantiation(instance):
    assert isinstance(instance, tdt4250::CourseGroup)

@given(instance=tdt4250::Course_strategy)
@settings(max_examples=50)
def test_tdt4250::course_instantiation(instance):
    assert isinstance(instance, tdt4250::Course)

@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_study_points_type(instance):
    assert isinstance(instance.study_points, float)


@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_study_points_setter(instance):
    original = instance.study_points
    instance.study_points = original
    assert instance.study_points == original

@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_semester_type(instance):
    assert isinstance(instance.semester, str)


@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=tdt4250::Course_strategy)
def test_tdt4250::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=tdt4250::Specialisation_strategy)
@settings(max_examples=50)
def test_tdt4250::specialisation_instantiation(instance):
    assert isinstance(instance, tdt4250::Specialisation)

@given(instance=tdt4250::Specialisation_strategy)
def test_tdt4250::specialisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250::Specialisation_strategy)
def test_tdt4250::specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250::Student_strategy)
@settings(max_examples=50)
def test_tdt4250::student_instantiation(instance):
    assert isinstance(instance, tdt4250::Student)

@given(instance=tdt4250::Student_strategy)
def test_tdt4250::student_current_semester_type(instance):
    assert isinstance(instance.current_semester, int)


@given(instance=tdt4250::Student_strategy)
def test_tdt4250::student_current_semester_setter(instance):
    original = instance.current_semester
    instance.current_semester = original
    assert instance.current_semester == original

@given(instance=tdt4250::Student_strategy)
def test_tdt4250::student_studentID_type(instance):
    assert isinstance(instance.studentID, int)


@given(instance=tdt4250::Student_strategy)
def test_tdt4250::student_studentID_setter(instance):
    original = instance.studentID
    instance.studentID = original
    assert instance.studentID == original

@given(instance=tdt4250::StudyProgram_strategy)
@settings(max_examples=50)
def test_tdt4250::studyprogram_instantiation(instance):
    assert isinstance(instance, tdt4250::StudyProgram)

@given(instance=tdt4250::StudyProgram_strategy)
def test_tdt4250::studyprogram_number_of_semesters_type(instance):
    assert isinstance(instance.number_of_semesters, int)


@given(instance=tdt4250::StudyProgram_strategy)
def test_tdt4250::studyprogram_number_of_semesters_setter(instance):
    original = instance.number_of_semesters
    instance.number_of_semesters = original
    assert instance.number_of_semesters == original

@given(instance=tdt4250::StudyProgram_strategy)
def test_tdt4250::studyprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tdt4250::StudyProgram_strategy)
def test_tdt4250::studyprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
