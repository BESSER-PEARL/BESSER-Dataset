import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tDT4250_asssignment1_2_Semester,
    tDT4250_asssignment1_2_Program_course,
    tDT4250_asssignment1_2_Specialization,
    tDT4250_asssignment1_2_Program,
    tDT4250_asssignment1_2_Course,
    tDT4250_asssignment1_2_Semester_Course,
    Fall_or_spring,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tdt4250_asssignment1_2_semester_is_not_abstract():
    assert not inspect.isabstract(tDT4250_asssignment1_2_Semester)


def test_tdt4250_asssignment1_2_semester_constructor_exists():
    assert callable(tDT4250_asssignment1_2_Semester.__init__)


def test_tdt4250_asssignment1_2_semester_constructor_args():
    sig = inspect.signature(tDT4250_asssignment1_2_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "Number" in params, "Missing parameter 'Number'"

def test_tdt4250_asssignment1_2_semester_has_Credits():
    assert hasattr(tDT4250_asssignment1_2_Semester, "Credits")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Semester.__mro__:
        if "Credits" in klass.__dict__:
            descriptor = klass.__dict__["Credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_semester_has_Number():
    assert hasattr(tDT4250_asssignment1_2_Semester, "Number")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Semester.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_asssignment1_2_program_course_is_not_abstract():
    assert not inspect.isabstract(tDT4250_asssignment1_2_Program_course)


def test_tdt4250_asssignment1_2_program_course_constructor_exists():
    assert callable(tDT4250_asssignment1_2_Program_course.__init__)


def test_tdt4250_asssignment1_2_program_course_constructor_args():
    sig = inspect.signature(tDT4250_asssignment1_2_Program_course.__init__)
    params = list(sig.parameters.keys())
    assert "Fall_or_spring" in params, "Missing parameter 'Fall_or_spring'"
    assert "Mandatory" in params, "Missing parameter 'Mandatory'"

def test_tdt4250_asssignment1_2_program_course_has_Fall_or_spring():
    assert hasattr(tDT4250_asssignment1_2_Program_course, "Fall_or_spring")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Program_course.__mro__:
        if "Fall_or_spring" in klass.__dict__:
            descriptor = klass.__dict__["Fall_or_spring"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_program_course_has_Mandatory():
    assert hasattr(tDT4250_asssignment1_2_Program_course, "Mandatory")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Program_course.__mro__:
        if "Mandatory" in klass.__dict__:
            descriptor = klass.__dict__["Mandatory"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_asssignment1_2_specialization_is_not_abstract():
    assert not inspect.isabstract(tDT4250_asssignment1_2_Specialization)


def test_tdt4250_asssignment1_2_specialization_constructor_exists():
    assert callable(tDT4250_asssignment1_2_Specialization.__init__)


def test_tdt4250_asssignment1_2_specialization_constructor_args():
    sig = inspect.signature(tDT4250_asssignment1_2_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_tdt4250_asssignment1_2_specialization_has_Name():
    assert hasattr(tDT4250_asssignment1_2_Specialization, "Name")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Specialization.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_asssignment1_2_program_is_not_abstract():
    assert not inspect.isabstract(tDT4250_asssignment1_2_Program)


def test_tdt4250_asssignment1_2_program_constructor_exists():
    assert callable(tDT4250_asssignment1_2_Program.__init__)


def test_tdt4250_asssignment1_2_program_constructor_args():
    sig = inspect.signature(tDT4250_asssignment1_2_Program.__init__)
    params = list(sig.parameters.keys())
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_tdt4250_asssignment1_2_program_has_Credits():
    assert hasattr(tDT4250_asssignment1_2_Program, "Credits")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Program.__mro__:
        if "Credits" in klass.__dict__:
            descriptor = klass.__dict__["Credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_program_has_Name():
    assert hasattr(tDT4250_asssignment1_2_Program, "Name")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_asssignment1_2_course_is_not_abstract():
    assert not inspect.isabstract(tDT4250_asssignment1_2_Course)


def test_tdt4250_asssignment1_2_course_constructor_exists():
    assert callable(tDT4250_asssignment1_2_Course.__init__)


def test_tdt4250_asssignment1_2_course_constructor_args():
    sig = inspect.signature(tDT4250_asssignment1_2_Course.__init__)
    params = list(sig.parameters.keys())
    assert "ExamDate" in params, "Missing parameter 'ExamDate'"
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"
    assert "Code" in params, "Missing parameter 'Code'"

def test_tdt4250_asssignment1_2_course_has_ExamDate():
    assert hasattr(tDT4250_asssignment1_2_Course, "ExamDate")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Course.__mro__:
        if "ExamDate" in klass.__dict__:
            descriptor = klass.__dict__["ExamDate"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_course_has_Credits():
    assert hasattr(tDT4250_asssignment1_2_Course, "Credits")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Course.__mro__:
        if "Credits" in klass.__dict__:
            descriptor = klass.__dict__["Credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_course_has_Name():
    assert hasattr(tDT4250_asssignment1_2_Course, "Name")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Course.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_course_has_StartDate():
    assert hasattr(tDT4250_asssignment1_2_Course, "StartDate")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Course.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_course_has_Code():
    assert hasattr(tDT4250_asssignment1_2_Course, "Code")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Course.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250_asssignment1_2_semester_course_is_not_abstract():
    assert not inspect.isabstract(tDT4250_asssignment1_2_Semester_Course)


def test_tdt4250_asssignment1_2_semester_course_constructor_exists():
    assert callable(tDT4250_asssignment1_2_Semester_Course.__init__)


def test_tdt4250_asssignment1_2_semester_course_constructor_args():
    sig = inspect.signature(tDT4250_asssignment1_2_Semester_Course.__init__)
    params = list(sig.parameters.keys())
    assert "Fall_or_spring" in params, "Missing parameter 'Fall_or_spring'"
    assert "Mandatory" in params, "Missing parameter 'Mandatory'"

def test_tdt4250_asssignment1_2_semester_course_has_Fall_or_spring():
    assert hasattr(tDT4250_asssignment1_2_Semester_Course, "Fall_or_spring")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Semester_Course.__mro__:
        if "Fall_or_spring" in klass.__dict__:
            descriptor = klass.__dict__["Fall_or_spring"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250_asssignment1_2_semester_course_has_Mandatory():
    assert hasattr(tDT4250_asssignment1_2_Semester_Course, "Mandatory")
    descriptor = None
    for klass in tDT4250_asssignment1_2_Semester_Course.__mro__:
        if "Mandatory" in klass.__dict__:
            descriptor = klass.__dict__["Mandatory"]
            break
    assert isinstance(descriptor, property)

def test_fall_or_spring_exists():
    # Check that the Enumeration exists
    assert Fall_or_spring is not None

def test_fall_or_spring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Fall_or_spring]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Fall_or_spring"


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
tDT4250_asssignment1_2_Semester_strategy = st.builds(
    tDT4250_asssignment1_2_Semester,
    Credits=
        safe_text,
    Number=
        st.integers()
)
tDT4250_asssignment1_2_Program_course_strategy = st.builds(
    tDT4250_asssignment1_2_Program_course,
    Fall_or_spring=
        safe_text,
    Mandatory=
        st.booleans()
)
tDT4250_asssignment1_2_Specialization_strategy = st.builds(
    tDT4250_asssignment1_2_Specialization,
    Name=
        safe_text
)
tDT4250_asssignment1_2_Program_strategy = st.builds(
    tDT4250_asssignment1_2_Program,
    Credits=
        safe_text,
    Name=
        safe_text
)
tDT4250_asssignment1_2_Course_strategy = st.builds(
    tDT4250_asssignment1_2_Course,
    ExamDate=
        safe_text,
    Credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Name=
        safe_text,
    StartDate=
        safe_text,
    Code=
        safe_text
)
tDT4250_asssignment1_2_Semester_Course_strategy = st.builds(
    tDT4250_asssignment1_2_Semester_Course,
    Fall_or_spring=
        safe_text,
    Mandatory=
        st.booleans()
)

@given(instance=tDT4250_asssignment1_2_Semester_strategy)
@settings(max_examples=50)
def test_tdt4250_asssignment1_2_semester_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Semester)



@given(instance=tDT4250_asssignment1_2_Semester_strategy)
def test_tdt4250_asssignment1_2_semester_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original



@given(instance=tDT4250_asssignment1_2_Semester_strategy)
def test_tdt4250_asssignment1_2_semester_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original

@given(instance=tDT4250_asssignment1_2_Program_course_strategy)
@settings(max_examples=50)
def test_tdt4250_asssignment1_2_program_course_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Program_course)



@given(instance=tDT4250_asssignment1_2_Program_course_strategy)
def test_tdt4250_asssignment1_2_program_course_Fall_or_spring_setter(instance):
    original = instance.Fall_or_spring
    instance.Fall_or_spring = original
    assert instance.Fall_or_spring == original



@given(instance=tDT4250_asssignment1_2_Program_course_strategy)
def test_tdt4250_asssignment1_2_program_course_Mandatory_setter(instance):
    original = instance.Mandatory
    instance.Mandatory = original
    assert instance.Mandatory == original

@given(instance=tDT4250_asssignment1_2_Specialization_strategy)
@settings(max_examples=50)
def test_tdt4250_asssignment1_2_specialization_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Specialization)



@given(instance=tDT4250_asssignment1_2_Specialization_strategy)
def test_tdt4250_asssignment1_2_specialization_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=tDT4250_asssignment1_2_Program_strategy)
@settings(max_examples=50)
def test_tdt4250_asssignment1_2_program_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Program)



@given(instance=tDT4250_asssignment1_2_Program_strategy)
def test_tdt4250_asssignment1_2_program_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original



@given(instance=tDT4250_asssignment1_2_Program_strategy)
def test_tdt4250_asssignment1_2_program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=tDT4250_asssignment1_2_Course_strategy)
@settings(max_examples=50)
def test_tdt4250_asssignment1_2_course_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Course)



@given(instance=tDT4250_asssignment1_2_Course_strategy)
def test_tdt4250_asssignment1_2_course_ExamDate_setter(instance):
    original = instance.ExamDate
    instance.ExamDate = original
    assert instance.ExamDate == original



@given(instance=tDT4250_asssignment1_2_Course_strategy)
def test_tdt4250_asssignment1_2_course_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original



@given(instance=tDT4250_asssignment1_2_Course_strategy)
def test_tdt4250_asssignment1_2_course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=tDT4250_asssignment1_2_Course_strategy)
def test_tdt4250_asssignment1_2_course_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original



@given(instance=tDT4250_asssignment1_2_Course_strategy)
def test_tdt4250_asssignment1_2_course_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original

@given(instance=tDT4250_asssignment1_2_Semester_Course_strategy)
@settings(max_examples=50)
def test_tdt4250_asssignment1_2_semester_course_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Semester_Course)



@given(instance=tDT4250_asssignment1_2_Semester_Course_strategy)
def test_tdt4250_asssignment1_2_semester_course_Fall_or_spring_setter(instance):
    original = instance.Fall_or_spring
    instance.Fall_or_spring = original
    assert instance.Fall_or_spring == original



@given(instance=tDT4250_asssignment1_2_Semester_Course_strategy)
def test_tdt4250_asssignment1_2_semester_course_Mandatory_setter(instance):
    original = instance.Mandatory
    instance.Mandatory = original
    assert instance.Mandatory == original
