import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    prosjekt_CourseCoordinator,
    prosjekt_Semester,
    prosjekt_Person,
    prosjekt_Course,
    prosjekt_University,
    prosjekt_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prosjekt_coursecoordinator_is_not_abstract():
    assert not inspect.isabstract(prosjekt_CourseCoordinator)


def test_prosjekt_coursecoordinator_constructor_exists():
    assert callable(prosjekt_CourseCoordinator.__init__)


def test_prosjekt_coursecoordinator_constructor_args():
    sig = inspect.signature(prosjekt_CourseCoordinator.__init__)
    params = list(sig.parameters.keys())



def test_prosjekt_semester_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Semester)


def test_prosjekt_semester_constructor_exists():
    assert callable(prosjekt_Semester.__init__)


def test_prosjekt_semester_constructor_args():
    sig = inspect.signature(prosjekt_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "amountA" in params, "Missing parameter 'amountA'"
    assert "averageGrade" in params, "Missing parameter 'averageGrade'"
    assert "name" in params, "Missing parameter 'name'"
    assert "amountD" in params, "Missing parameter 'amountD'"
    assert "amountC" in params, "Missing parameter 'amountC'"
    assert "amountE" in params, "Missing parameter 'amountE'"
    assert "amountF" in params, "Missing parameter 'amountF'"
    assert "amountB" in params, "Missing parameter 'amountB'"

def test_prosjekt_semester_has_amountA():
    assert hasattr(prosjekt_Semester, "amountA")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "amountA" in klass.__dict__:
            descriptor = klass.__dict__["amountA"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_averageGrade():
    assert hasattr(prosjekt_Semester, "averageGrade")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "averageGrade" in klass.__dict__:
            descriptor = klass.__dict__["averageGrade"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_name():
    assert hasattr(prosjekt_Semester, "name")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_amountD():
    assert hasattr(prosjekt_Semester, "amountD")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "amountD" in klass.__dict__:
            descriptor = klass.__dict__["amountD"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_amountC():
    assert hasattr(prosjekt_Semester, "amountC")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "amountC" in klass.__dict__:
            descriptor = klass.__dict__["amountC"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_amountE():
    assert hasattr(prosjekt_Semester, "amountE")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "amountE" in klass.__dict__:
            descriptor = klass.__dict__["amountE"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_amountF():
    assert hasattr(prosjekt_Semester, "amountF")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "amountF" in klass.__dict__:
            descriptor = klass.__dict__["amountF"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_semester_has_amountB():
    assert hasattr(prosjekt_Semester, "amountB")
    descriptor = None
    for klass in prosjekt_Semester.__mro__:
        if "amountB" in klass.__dict__:
            descriptor = klass.__dict__["amountB"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_person_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Person)


def test_prosjekt_person_constructor_exists():
    assert callable(prosjekt_Person.__init__)


def test_prosjekt_person_constructor_args():
    sig = inspect.signature(prosjekt_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt_person_has_name():
    assert hasattr(prosjekt_Person, "name")
    descriptor = None
    for klass in prosjekt_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_course_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Course)


def test_prosjekt_course_constructor_exists():
    assert callable(prosjekt_Course.__init__)


def test_prosjekt_course_constructor_args():
    sig = inspect.signature(prosjekt_Course.__init__)
    params = list(sig.parameters.keys())
    assert "studyPoints" in params, "Missing parameter 'studyPoints'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_prosjekt_course_has_studyPoints():
    assert hasattr(prosjekt_Course, "studyPoints")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "studyPoints" in klass.__dict__:
            descriptor = klass.__dict__["studyPoints"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_course_has_name():
    assert hasattr(prosjekt_Course, "name")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_course_has_code():
    assert hasattr(prosjekt_Course, "code")
    descriptor = None
    for klass in prosjekt_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_university_is_not_abstract():
    assert not inspect.isabstract(prosjekt_University)


def test_prosjekt_university_constructor_exists():
    assert callable(prosjekt_University.__init__)


def test_prosjekt_university_constructor_args():
    sig = inspect.signature(prosjekt_University.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_prosjekt_university_has_shortName():
    assert hasattr(prosjekt_University, "shortName")
    descriptor = None
    for klass in prosjekt_University.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_university_has_name():
    assert hasattr(prosjekt_University, "name")
    descriptor = None
    for klass in prosjekt_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prosjekt_department_is_not_abstract():
    assert not inspect.isabstract(prosjekt_Department)


def test_prosjekt_department_constructor_exists():
    assert callable(prosjekt_Department.__init__)


def test_prosjekt_department_constructor_args():
    sig = inspect.signature(prosjekt_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_prosjekt_department_has_name():
    assert hasattr(prosjekt_Department, "name")
    descriptor = None
    for klass in prosjekt_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prosjekt_department_has_shortName():
    assert hasattr(prosjekt_Department, "shortName")
    descriptor = None
    for klass in prosjekt_Department.__mro__:
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
prosjekt_CourseCoordinator_strategy = st.builds(
    prosjekt_CourseCoordinator,
)
prosjekt_Semester_strategy = st.builds(
    prosjekt_Semester,
    amountA=
        st.integers(),
    averageGrade=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    amountD=
        st.integers(),
    amountC=
        st.integers(),
    amountE=
        st.integers(),
    amountF=
        st.integers(),
    amountB=
        st.integers()
)
prosjekt_Person_strategy = st.builds(
    prosjekt_Person,
    name=
        safe_text
)
prosjekt_Course_strategy = st.builds(
    prosjekt_Course,
    studyPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text
)
prosjekt_University_strategy = st.builds(
    prosjekt_University,
    shortName=
        safe_text,
    name=
        safe_text
)
prosjekt_Department_strategy = st.builds(
    prosjekt_Department,
    name=
        safe_text,
    shortName=
        safe_text
)

@given(instance=prosjekt_CourseCoordinator_strategy)
@settings(max_examples=50)
def test_prosjekt_coursecoordinator_instantiation(instance):
    assert isinstance(instance, prosjekt_CourseCoordinator)

@given(instance=prosjekt_Semester_strategy)
@settings(max_examples=50)
def test_prosjekt_semester_instantiation(instance):
    assert isinstance(instance, prosjekt_Semester)



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_amountA_setter(instance):
    original = instance.amountA
    instance.amountA = original
    assert instance.amountA == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_averageGrade_setter(instance):
    original = instance.averageGrade
    instance.averageGrade = original
    assert instance.averageGrade == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_amountD_setter(instance):
    original = instance.amountD
    instance.amountD = original
    assert instance.amountD == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_amountC_setter(instance):
    original = instance.amountC
    instance.amountC = original
    assert instance.amountC == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_amountE_setter(instance):
    original = instance.amountE
    instance.amountE = original
    assert instance.amountE == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_amountF_setter(instance):
    original = instance.amountF
    instance.amountF = original
    assert instance.amountF == original



@given(instance=prosjekt_Semester_strategy)
def test_prosjekt_semester_amountB_setter(instance):
    original = instance.amountB
    instance.amountB = original
    assert instance.amountB == original

@given(instance=prosjekt_Person_strategy)
@settings(max_examples=50)
def test_prosjekt_person_instantiation(instance):
    assert isinstance(instance, prosjekt_Person)



@given(instance=prosjekt_Person_strategy)
def test_prosjekt_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt_Course_strategy)
@settings(max_examples=50)
def test_prosjekt_course_instantiation(instance):
    assert isinstance(instance, prosjekt_Course)



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_studyPoints_setter(instance):
    original = instance.studyPoints
    instance.studyPoints = original
    assert instance.studyPoints == original



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=prosjekt_Course_strategy)
def test_prosjekt_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=prosjekt_University_strategy)
@settings(max_examples=50)
def test_prosjekt_university_instantiation(instance):
    assert isinstance(instance, prosjekt_University)



@given(instance=prosjekt_University_strategy)
def test_prosjekt_university_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original



@given(instance=prosjekt_University_strategy)
def test_prosjekt_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prosjekt_Department_strategy)
@settings(max_examples=50)
def test_prosjekt_department_instantiation(instance):
    assert isinstance(instance, prosjekt_Department)



@given(instance=prosjekt_Department_strategy)
def test_prosjekt_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=prosjekt_Department_strategy)
def test_prosjekt_department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original
