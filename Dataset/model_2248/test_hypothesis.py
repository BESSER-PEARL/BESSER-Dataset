import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tdt4250_CourseGroup,
    tdt4250_Course,
    tdt4250_Specialisation,
    tdt4250_Student,
    tdt4250_StudyProgram,
    StudyProgramName,
    Semester,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tdt4250_coursegroup_is_not_abstract():
    assert not inspect.isabstract(tdt4250_CourseGroup)


def test_tdt4250_coursegroup_constructor_exists():
    assert callable(tdt4250_CourseGroup.__init__)


def test_tdt4250_coursegroup_constructor_args():
    sig = inspect.signature(tdt4250_CourseGroup.__init__)
    params = list(sig.parameters.keys())



def test_tdt4250_course_is_not_abstract():
    assert not inspect.isabstract(tdt4250_Course)


def test_tdt4250_course_constructor_exists():
    assert callable(tdt4250_Course.__init__)


def test_tdt4250_course_constructor_args():
    sig = inspect.signature(tdt4250_Course.__init__)
    params = list(sig.parameters.keys())
    assert "study_points" in params, "Missing parameter 'study_points'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "semester" in params, "Missing parameter 'semester'"
    assert "level" in params, "Missing parameter 'level'"

def test_tdt4250_course_has_study_points():
    assert hasattr(tdt4250_Course, "study_points")
    descriptor = None
    for klass in tdt4250_Course.__mro__:
        if "study_points" in klass.__dict__:
            descriptor = klass.__dict__["study_points"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_course_has_name():
    assert hasattr(tdt4250_Course, "name")
    descriptor = None
    for klass in tdt4250_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_course_has_code():
    assert hasattr(tdt4250_Course, "code")
    descriptor = None
    for klass in tdt4250_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_course_has_semester():
    assert hasattr(tdt4250_Course, "semester")
    descriptor = None
    for klass in tdt4250_Course.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_course_has_level():
    assert hasattr(tdt4250_Course, "level")
    descriptor = None
    for klass in tdt4250_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_specialisation_is_not_abstract():
    assert not inspect.isabstract(tdt4250_Specialisation)


def test_tdt4250_specialisation_constructor_exists():
    assert callable(tdt4250_Specialisation.__init__)


def test_tdt4250_specialisation_constructor_args():
    sig = inspect.signature(tdt4250_Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tdt4250_specialisation_has_name():
    assert hasattr(tdt4250_Specialisation, "name")
    descriptor = None
    for klass in tdt4250_Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_student_is_not_abstract():
    assert not inspect.isabstract(tdt4250_Student)


def test_tdt4250_student_constructor_exists():
    assert callable(tdt4250_Student.__init__)


def test_tdt4250_student_constructor_args():
    sig = inspect.signature(tdt4250_Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentID" in params, "Missing parameter 'studentID'"
    assert "current_semester" in params, "Missing parameter 'current_semester'"

def test_tdt4250_student_has_studentID():
    assert hasattr(tdt4250_Student, "studentID")
    descriptor = None
    for klass in tdt4250_Student.__mro__:
        if "studentID" in klass.__dict__:
            descriptor = klass.__dict__["studentID"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_student_has_current_semester():
    assert hasattr(tdt4250_Student, "current_semester")
    descriptor = None
    for klass in tdt4250_Student.__mro__:
        if "current_semester" in klass.__dict__:
            descriptor = klass.__dict__["current_semester"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_studyprogram_is_not_abstract():
    assert not inspect.isabstract(tdt4250_StudyProgram)


def test_tdt4250_studyprogram_constructor_exists():
    assert callable(tdt4250_StudyProgram.__init__)


def test_tdt4250_studyprogram_constructor_args():
    sig = inspect.signature(tdt4250_StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "number_of_semesters" in params, "Missing parameter 'number_of_semesters'"

def test_tdt4250_studyprogram_has_name():
    assert hasattr(tdt4250_StudyProgram, "name")
    descriptor = None
    for klass in tdt4250_StudyProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_studyprogram_has_number_of_semesters():
    assert hasattr(tdt4250_StudyProgram, "number_of_semesters")
    descriptor = None
    for klass in tdt4250_StudyProgram.__mro__:
        if "number_of_semesters" in klass.__dict__:
            descriptor = klass.__dict__["number_of_semesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramname_exists():
    # Check that the Enumeration exists
    assert StudyProgramName is not None

def test_studyprogramname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyProgramName]
    expected_literals = [
        "computer_science_5_years",
        "computer_science_2_years",
        "informatics",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyProgramName"

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
tdt4250_CourseGroup_strategy = st.builds(
    tdt4250_CourseGroup,
)
tdt4250_Course_strategy = st.builds(
    tdt4250_Course,
    study_points=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text,
    semester=
        safe_text,
    level=
        safe_text
)
tdt4250_Specialisation_strategy = st.builds(
    tdt4250_Specialisation,
    name=
        safe_text
)
tdt4250_Student_strategy = st.builds(
    tdt4250_Student,
    studentID=
        st.integers(),
    current_semester=
        st.integers()
)
tdt4250_StudyProgram_strategy = st.builds(
    tdt4250_StudyProgram,
    name=
        safe_text,
    number_of_semesters=
        st.integers()
)

@given(instance=tdt4250_CourseGroup_strategy)
@settings(max_examples=50)
def test_tdt4250_coursegroup_instantiation(instance):
    assert isinstance(instance, tdt4250_CourseGroup)

@given(instance=tdt4250_Course_strategy)
@settings(max_examples=50)
def test_tdt4250_course_instantiation(instance):
    assert isinstance(instance, tdt4250_Course)



@given(instance=tdt4250_Course_strategy)
def test_tdt4250_course_study_points_setter(instance):
    original = instance.study_points
    instance.study_points = original
    assert instance.study_points == original



@given(instance=tdt4250_Course_strategy)
def test_tdt4250_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250_Course_strategy)
def test_tdt4250_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=tdt4250_Course_strategy)
def test_tdt4250_course_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original



@given(instance=tdt4250_Course_strategy)
def test_tdt4250_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=tdt4250_Specialisation_strategy)
@settings(max_examples=50)
def test_tdt4250_specialisation_instantiation(instance):
    assert isinstance(instance, tdt4250_Specialisation)



@given(instance=tdt4250_Specialisation_strategy)
def test_tdt4250_specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tdt4250_Student_strategy)
@settings(max_examples=50)
def test_tdt4250_student_instantiation(instance):
    assert isinstance(instance, tdt4250_Student)



@given(instance=tdt4250_Student_strategy)
def test_tdt4250_student_studentID_setter(instance):
    original = instance.studentID
    instance.studentID = original
    assert instance.studentID == original



@given(instance=tdt4250_Student_strategy)
def test_tdt4250_student_current_semester_setter(instance):
    original = instance.current_semester
    instance.current_semester = original
    assert instance.current_semester == original

@given(instance=tdt4250_StudyProgram_strategy)
@settings(max_examples=50)
def test_tdt4250_studyprogram_instantiation(instance):
    assert isinstance(instance, tdt4250_StudyProgram)



@given(instance=tdt4250_StudyProgram_strategy)
def test_tdt4250_studyprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tdt4250_StudyProgram_strategy)
def test_tdt4250_studyprogram_number_of_semesters_setter(instance):
    original = instance.number_of_semesters
    instance.number_of_semesters = original
    assert instance.number_of_semesters == original
