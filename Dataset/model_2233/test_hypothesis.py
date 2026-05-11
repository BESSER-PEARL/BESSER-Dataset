import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tDT4250::asssignment1::2::Department,
    tDT4250::asssignment1::2::Course,
    tDT4250::asssignment1::2::Semester::Course,
    tDT4250::asssignment1::2::Semester,
    tDT4250::asssignment1::2::Program::course,
    tDT4250::asssignment1::2::Specialization,
    tDT4250::asssignment1::2::Program,
    Fall_or_spring,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tdt4250::asssignment1::2::department_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Department)


def test_tdt4250::asssignment1::2::department_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Department.__init__)


def test_tdt4250::asssignment1::2::department_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Department.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_tdt4250::asssignment1::2::department_has_Name():
    assert hasattr(tDT4250::asssignment1::2::Department, "Name")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Department.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::asssignment1::2::course_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Course)


def test_tdt4250::asssignment1::2::course_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Course.__init__)


def test_tdt4250::asssignment1::2::course_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Course.__init__)
    params = list(sig.parameters.keys())
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Code" in params, "Missing parameter 'Code'"
    assert "ExamDate" in params, "Missing parameter 'ExamDate'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"

def test_tdt4250::asssignment1::2::course_has_Credits():
    assert hasattr(tDT4250::asssignment1::2::Course, "Credits")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Course.__mro__:
        if "Credits" in klass.__dict__:
            descriptor = klass.__dict__["Credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::course_has_Name():
    assert hasattr(tDT4250::asssignment1::2::Course, "Name")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Course.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::course_has_Code():
    assert hasattr(tDT4250::asssignment1::2::Course, "Code")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Course.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::course_has_ExamDate():
    assert hasattr(tDT4250::asssignment1::2::Course, "ExamDate")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Course.__mro__:
        if "ExamDate" in klass.__dict__:
            descriptor = klass.__dict__["ExamDate"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::course_has_StartDate():
    assert hasattr(tDT4250::asssignment1::2::Course, "StartDate")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Course.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::asssignment1::2::semester::course_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Semester::Course)


def test_tdt4250::asssignment1::2::semester::course_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Semester::Course.__init__)


def test_tdt4250::asssignment1::2::semester::course_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Semester::Course.__init__)
    params = list(sig.parameters.keys())
    assert "Fall_or_spring" in params, "Missing parameter 'Fall_or_spring'"
    assert "Mandatory" in params, "Missing parameter 'Mandatory'"

def test_tdt4250::asssignment1::2::semester::course_has_Fall_or_spring():
    assert hasattr(tDT4250::asssignment1::2::Semester::Course, "Fall_or_spring")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Semester::Course.__mro__:
        if "Fall_or_spring" in klass.__dict__:
            descriptor = klass.__dict__["Fall_or_spring"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::semester::course_has_Mandatory():
    assert hasattr(tDT4250::asssignment1::2::Semester::Course, "Mandatory")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Semester::Course.__mro__:
        if "Mandatory" in klass.__dict__:
            descriptor = klass.__dict__["Mandatory"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::asssignment1::2::semester_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Semester)


def test_tdt4250::asssignment1::2::semester_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Semester.__init__)


def test_tdt4250::asssignment1::2::semester_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "Number" in params, "Missing parameter 'Number'"

def test_tdt4250::asssignment1::2::semester_has_Credits():
    assert hasattr(tDT4250::asssignment1::2::Semester, "Credits")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Semester.__mro__:
        if "Credits" in klass.__dict__:
            descriptor = klass.__dict__["Credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::semester_has_Number():
    assert hasattr(tDT4250::asssignment1::2::Semester, "Number")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Semester.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::asssignment1::2::program::course_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Program::course)


def test_tdt4250::asssignment1::2::program::course_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Program::course.__init__)


def test_tdt4250::asssignment1::2::program::course_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Program::course.__init__)
    params = list(sig.parameters.keys())
    assert "Fall_or_spring" in params, "Missing parameter 'Fall_or_spring'"
    assert "Mandatory" in params, "Missing parameter 'Mandatory'"

def test_tdt4250::asssignment1::2::program::course_has_Fall_or_spring():
    assert hasattr(tDT4250::asssignment1::2::Program::course, "Fall_or_spring")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Program::course.__mro__:
        if "Fall_or_spring" in klass.__dict__:
            descriptor = klass.__dict__["Fall_or_spring"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::program::course_has_Mandatory():
    assert hasattr(tDT4250::asssignment1::2::Program::course, "Mandatory")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Program::course.__mro__:
        if "Mandatory" in klass.__dict__:
            descriptor = klass.__dict__["Mandatory"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::asssignment1::2::specialization_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Specialization)


def test_tdt4250::asssignment1::2::specialization_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Specialization.__init__)


def test_tdt4250::asssignment1::2::specialization_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_tdt4250::asssignment1::2::specialization_has_Name():
    assert hasattr(tDT4250::asssignment1::2::Specialization, "Name")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Specialization.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_tdt4250::asssignment1::2::program_is_not_abstract():
    assert not inspect.isabstract(tDT4250::asssignment1::2::Program)


def test_tdt4250::asssignment1::2::program_constructor_exists():
    assert callable(tDT4250::asssignment1::2::Program.__init__)


def test_tdt4250::asssignment1::2::program_constructor_args():
    sig = inspect.signature(tDT4250::asssignment1::2::Program.__init__)
    params = list(sig.parameters.keys())
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_tdt4250::asssignment1::2::program_has_Credits():
    assert hasattr(tDT4250::asssignment1::2::Program, "Credits")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Program.__mro__:
        if "Credits" in klass.__dict__:
            descriptor = klass.__dict__["Credits"]
            break
    assert isinstance(descriptor, property)

def test_tdt4250::asssignment1::2::program_has_Name():
    assert hasattr(tDT4250::asssignment1::2::Program, "Name")
    descriptor = None
    for klass in tDT4250::asssignment1::2::Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
tDT4250::asssignment1::2::Department_strategy = st.builds(
    tDT4250::asssignment1::2::Department,
    Name=
        safe_text
)
tDT4250::asssignment1::2::Course_strategy = st.builds(
    tDT4250::asssignment1::2::Course,
    Credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Name=
        safe_text,
    Code=
        safe_text,
    ExamDate=
        safe_text,
    StartDate=
        safe_text
)
tDT4250::asssignment1::2::Semester::Course_strategy = st.builds(
    tDT4250::asssignment1::2::Semester::Course,
    Fall_or_spring=
        safe_text,
    Mandatory=
        st.booleans()
)
tDT4250::asssignment1::2::Semester_strategy = st.builds(
    tDT4250::asssignment1::2::Semester,
    Credits=
        safe_text,
    Number=
        st.integers()
)
tDT4250::asssignment1::2::Program::course_strategy = st.builds(
    tDT4250::asssignment1::2::Program::course,
    Fall_or_spring=
        safe_text,
    Mandatory=
        st.booleans()
)
tDT4250::asssignment1::2::Specialization_strategy = st.builds(
    tDT4250::asssignment1::2::Specialization,
    Name=
        safe_text
)
tDT4250::asssignment1::2::Program_strategy = st.builds(
    tDT4250::asssignment1::2::Program,
    Credits=
        safe_text,
    Name=
        safe_text
)

@given(instance=tDT4250::asssignment1::2::Department_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::department_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Department)

@given(instance=tDT4250::asssignment1::2::Department_strategy)
def test_tdt4250::asssignment1::2::department_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=tDT4250::asssignment1::2::Department_strategy)
def test_tdt4250::asssignment1::2::department_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=tDT4250::asssignment1::2::Course_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::course_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Course)

@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_Credits_type(instance):
    assert isinstance(instance.Credits, float)


@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original

@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_Code_type(instance):
    assert isinstance(instance.Code, str)


@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original

@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_ExamDate_type(instance):
    assert isinstance(instance.ExamDate, str)


@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_ExamDate_setter(instance):
    original = instance.ExamDate
    instance.ExamDate = original
    assert instance.ExamDate == original

@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_StartDate_type(instance):
    assert isinstance(instance.StartDate, str)


@given(instance=tDT4250::asssignment1::2::Course_strategy)
def test_tdt4250::asssignment1::2::course_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=tDT4250::asssignment1::2::Semester::Course_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::semester::course_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Semester::Course)

@given(instance=tDT4250::asssignment1::2::Semester::Course_strategy)
def test_tdt4250::asssignment1::2::semester::course_Fall_or_spring_type(instance):
    assert isinstance(instance.Fall_or_spring, str)


@given(instance=tDT4250::asssignment1::2::Semester::Course_strategy)
def test_tdt4250::asssignment1::2::semester::course_Fall_or_spring_setter(instance):
    original = instance.Fall_or_spring
    instance.Fall_or_spring = original
    assert instance.Fall_or_spring == original

@given(instance=tDT4250::asssignment1::2::Semester::Course_strategy)
def test_tdt4250::asssignment1::2::semester::course_Mandatory_type(instance):
    assert isinstance(instance.Mandatory, bool)


@given(instance=tDT4250::asssignment1::2::Semester::Course_strategy)
def test_tdt4250::asssignment1::2::semester::course_Mandatory_setter(instance):
    original = instance.Mandatory
    instance.Mandatory = original
    assert instance.Mandatory == original

@given(instance=tDT4250::asssignment1::2::Semester_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::semester_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Semester)

@given(instance=tDT4250::asssignment1::2::Semester_strategy)
def test_tdt4250::asssignment1::2::semester_Credits_type(instance):
    assert isinstance(instance.Credits, str)


@given(instance=tDT4250::asssignment1::2::Semester_strategy)
def test_tdt4250::asssignment1::2::semester_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original

@given(instance=tDT4250::asssignment1::2::Semester_strategy)
def test_tdt4250::asssignment1::2::semester_Number_type(instance):
    assert isinstance(instance.Number, int)


@given(instance=tDT4250::asssignment1::2::Semester_strategy)
def test_tdt4250::asssignment1::2::semester_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original

@given(instance=tDT4250::asssignment1::2::Program::course_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::program::course_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Program::course)

@given(instance=tDT4250::asssignment1::2::Program::course_strategy)
def test_tdt4250::asssignment1::2::program::course_Fall_or_spring_type(instance):
    assert isinstance(instance.Fall_or_spring, str)


@given(instance=tDT4250::asssignment1::2::Program::course_strategy)
def test_tdt4250::asssignment1::2::program::course_Fall_or_spring_setter(instance):
    original = instance.Fall_or_spring
    instance.Fall_or_spring = original
    assert instance.Fall_or_spring == original

@given(instance=tDT4250::asssignment1::2::Program::course_strategy)
def test_tdt4250::asssignment1::2::program::course_Mandatory_type(instance):
    assert isinstance(instance.Mandatory, bool)


@given(instance=tDT4250::asssignment1::2::Program::course_strategy)
def test_tdt4250::asssignment1::2::program::course_Mandatory_setter(instance):
    original = instance.Mandatory
    instance.Mandatory = original
    assert instance.Mandatory == original

@given(instance=tDT4250::asssignment1::2::Specialization_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::specialization_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Specialization)

@given(instance=tDT4250::asssignment1::2::Specialization_strategy)
def test_tdt4250::asssignment1::2::specialization_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=tDT4250::asssignment1::2::Specialization_strategy)
def test_tdt4250::asssignment1::2::specialization_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=tDT4250::asssignment1::2::Program_strategy)
@settings(max_examples=50)
def test_tdt4250::asssignment1::2::program_instantiation(instance):
    assert isinstance(instance, tDT4250::asssignment1::2::Program)

@given(instance=tDT4250::asssignment1::2::Program_strategy)
def test_tdt4250::asssignment1::2::program_Credits_type(instance):
    assert isinstance(instance.Credits, str)


@given(instance=tDT4250::asssignment1::2::Program_strategy)
def test_tdt4250::asssignment1::2::program_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original

@given(instance=tDT4250::asssignment1::2::Program_strategy)
def test_tdt4250::asssignment1::2::program_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=tDT4250::asssignment1::2::Program_strategy)
def test_tdt4250::asssignment1::2::program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
