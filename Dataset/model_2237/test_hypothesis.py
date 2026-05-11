import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    prosjekt::CourseCoordinator,
    prosjekt::Semester,
    prosjekt::Person,
    prosjekt::Course,
    prosjekt::University,
    prosjekt::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prosjekt::coursecoordinator_is_not_abstract():
    assert not inspect.isabstract(prosjekt::CourseCoordinator)


def test_prosjekt::coursecoordinator_constructor_exists():
    assert callable(prosjekt::CourseCoordinator.__init__)


def test_prosjekt::coursecoordinator_constructor_args():
    sig = inspect.signature(prosjekt::CourseCoordinator.__init__)
    params = list(sig.parameters.keys())



def test_prosjekt::semester_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Semester)


def test_prosjekt::semester_constructor_exists():
    assert callable(prosjekt::Semester.__init__)


def test_prosjekt::semester_constructor_args():
    sig = inspect.signature(prosjekt::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "amountF" in params, "Missing parameter 'amountF'"
    assert "averageGrade" in params, "Missing parameter 'averageGrade'"
    assert "amountC" in params, "Missing parameter 'amountC'"
    assert "amountE" in params, "Missing parameter 'amountE'"
    assert "amountD" in params, "Missing parameter 'amountD'"
    assert "amountB" in params, "Missing parameter 'amountB'"
    assert "amountA" in params, "Missing parameter 'amountA'"
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt::semester_has_amountF():
    assert hasattr(prosjekt::Semester, "amountF")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "amountF" in klass.__dict__:
            descriptor = klass.__dict__["amountF"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_averageGrade():
    assert hasattr(prosjekt::Semester, "averageGrade")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "averageGrade" in klass.__dict__:
            descriptor = klass.__dict__["averageGrade"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_amountC():
    assert hasattr(prosjekt::Semester, "amountC")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "amountC" in klass.__dict__:
            descriptor = klass.__dict__["amountC"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_amountE():
    assert hasattr(prosjekt::Semester, "amountE")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "amountE" in klass.__dict__:
            descriptor = klass.__dict__["amountE"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_amountD():
    assert hasattr(prosjekt::Semester, "amountD")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "amountD" in klass.__dict__:
            descriptor = klass.__dict__["amountD"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_amountB():
    assert hasattr(prosjekt::Semester, "amountB")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "amountB" in klass.__dict__:
            descriptor = klass.__dict__["amountB"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_amountA():
    assert hasattr(prosjekt::Semester, "amountA")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "amountA" in klass.__dict__:
            descriptor = klass.__dict__["amountA"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::semester_has_name():
    assert hasattr(prosjekt::Semester, "name")
    descriptor = None
    for klass in prosjekt::Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::person_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Person)


def test_prosjekt::person_constructor_exists():
    assert callable(prosjekt::Person.__init__)


def test_prosjekt::person_constructor_args():
    sig = inspect.signature(prosjekt::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt::person_has_name():
    assert hasattr(prosjekt::Person, "name")
    descriptor = None
    for klass in prosjekt::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::course_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Course)


def test_prosjekt::course_constructor_exists():
    assert callable(prosjekt::Course.__init__)


def test_prosjekt::course_constructor_args():
    sig = inspect.signature(prosjekt::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "studyPoints" in params, "Missing parameter 'studyPoints'"
    assert "code" in params, "Missing parameter 'code'"

def test_prosjekt::course_has_name():
    assert hasattr(prosjekt::Course, "name")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::course_has_studyPoints():
    assert hasattr(prosjekt::Course, "studyPoints")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "studyPoints" in klass.__dict__:
            descriptor = klass.__dict__["studyPoints"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::course_has_code():
    assert hasattr(prosjekt::Course, "code")
    descriptor = None
    for klass in prosjekt::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::university_is_not_abstract():
    assert not inspect.isabstract(prosjekt::University)


def test_prosjekt::university_constructor_exists():
    assert callable(prosjekt::University.__init__)


def test_prosjekt::university_constructor_args():
    sig = inspect.signature(prosjekt::University.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt::university_has_shortName():
    assert hasattr(prosjekt::University, "shortName")
    descriptor = None
    for klass in prosjekt::University.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::university_has_name():
    assert hasattr(prosjekt::University, "name")
    descriptor = None
    for klass in prosjekt::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt::department_is_not_abstract():
    assert not inspect.isabstract(prosjekt::Department)


def test_prosjekt::department_constructor_exists():
    assert callable(prosjekt::Department.__init__)


def test_prosjekt::department_constructor_args():
    sig = inspect.signature(prosjekt::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_prosjekt::department_has_name():
    assert hasattr(prosjekt::Department, "name")
    descriptor = None
    for klass in prosjekt::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt::department_has_shortName():
    assert hasattr(prosjekt::Department, "shortName")
    descriptor = None
    for klass in prosjekt::Department.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)


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
prosjekt::CourseCoordinator_strategy = st.builds(
    prosjekt::CourseCoordinator,
)
prosjekt::Semester_strategy = st.builds(
    prosjekt::Semester,
    amountF=
        st.integers(),
    averageGrade=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    amountC=
        st.integers(),
    amountE=
        st.integers(),
    amountD=
        st.integers(),
    amountB=
        st.integers(),
    amountA=
        st.integers(),
    name=
        safe_text
)
prosjekt::Person_strategy = st.builds(
    prosjekt::Person,
    name=
        safe_text
)
prosjekt::Course_strategy = st.builds(
    prosjekt::Course,
    name=
        safe_text,
    studyPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text
)
prosjekt::University_strategy = st.builds(
    prosjekt::University,
    shortName=
        safe_text,
    name=
        safe_text
)
prosjekt::Department_strategy = st.builds(
    prosjekt::Department,
    name=
        safe_text,
    shortName=
        safe_text
)

@given(instance=prosjekt::CourseCoordinator_strategy)
@settings(max_examples=50)
def test_prosjekt::coursecoordinator_instantiation(instance):
    assert isinstance(instance, prosjekt::CourseCoordinator)

@given(instance=prosjekt::Semester_strategy)
@settings(max_examples=50)
def test_prosjekt::semester_instantiation(instance):
    assert isinstance(instance, prosjekt::Semester)

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountF_type(instance):
    assert isinstance(instance.amountF, int)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountF_setter(instance):
    original = instance.amountF
    instance.amountF = original
    assert instance.amountF == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_averageGrade_type(instance):
    assert isinstance(instance.averageGrade, float)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_averageGrade_setter(instance):
    original = instance.averageGrade
    instance.averageGrade = original
    assert instance.averageGrade == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountC_type(instance):
    assert isinstance(instance.amountC, int)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountC_setter(instance):
    original = instance.amountC
    instance.amountC = original
    assert instance.amountC == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountE_type(instance):
    assert isinstance(instance.amountE, int)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountE_setter(instance):
    original = instance.amountE
    instance.amountE = original
    assert instance.amountE == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountD_type(instance):
    assert isinstance(instance.amountD, int)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountD_setter(instance):
    original = instance.amountD
    instance.amountD = original
    assert instance.amountD == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountB_type(instance):
    assert isinstance(instance.amountB, int)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountB_setter(instance):
    original = instance.amountB
    instance.amountB = original
    assert instance.amountB == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountA_type(instance):
    assert isinstance(instance.amountA, int)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_amountA_setter(instance):
    original = instance.amountA
    instance.amountA = original
    assert instance.amountA == original

@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Semester_strategy)
def test_prosjekt::semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Person_strategy)
@settings(max_examples=50)
def test_prosjekt::person_instantiation(instance):
    assert isinstance(instance, prosjekt::Person)

@given(instance=prosjekt::Person_strategy)
def test_prosjekt::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Person_strategy)
def test_prosjekt::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Course_strategy)
@settings(max_examples=50)
def test_prosjekt::course_instantiation(instance):
    assert isinstance(instance, prosjekt::Course)

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_studyPoints_type(instance):
    assert isinstance(instance.studyPoints, float)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_studyPoints_setter(instance):
    original = instance.studyPoints
    instance.studyPoints = original
    assert instance.studyPoints == original

@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=prosjekt::Course_strategy)
def test_prosjekt::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=prosjekt::University_strategy)
@settings(max_examples=50)
def test_prosjekt::university_instantiation(instance):
    assert isinstance(instance, prosjekt::University)

@given(instance=prosjekt::University_strategy)
def test_prosjekt::university_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=prosjekt::University_strategy)
def test_prosjekt::university_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=prosjekt::University_strategy)
def test_prosjekt::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::University_strategy)
def test_prosjekt::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Department_strategy)
@settings(max_examples=50)
def test_prosjekt::department_instantiation(instance):
    assert isinstance(instance, prosjekt::Department)

@given(instance=prosjekt::Department_strategy)
def test_prosjekt::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prosjekt::Department_strategy)
def test_prosjekt::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt::Department_strategy)
def test_prosjekt::department_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=prosjekt::Department_strategy)
def test_prosjekt::department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original
