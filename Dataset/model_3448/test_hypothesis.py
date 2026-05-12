import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    test_Employee,
    test_Student,
    test_Person,
    test_University,
    Grade,
    incomeLevel,
    EEnum0,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_test_employee_is_not_abstract():
    assert not inspect.isabstract(test_Employee)


def test_test_employee_constructor_exists():
    assert callable(test_Employee.__init__)


def test_test_employee_constructor_args():
    sig = inspect.signature(test_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "incomeLevel" in params, "Missing parameter 'incomeLevel'"

def test_test_employee_has_incomeLevel():
    assert hasattr(test_Employee, "incomeLevel")
    descriptor = None
    for klass in test_Employee.__mro__:
        if "incomeLevel" in klass.__dict__:
            descriptor = klass.__dict__["incomeLevel"]
            break
    assert isinstance(descriptor, property)



def test_test_student_is_not_abstract():
    assert not inspect.isabstract(test_Student)


def test_test_student_constructor_exists():
    assert callable(test_Student.__init__)


def test_test_student_constructor_args():
    sig = inspect.signature(test_Student.__init__)
    params = list(sig.parameters.keys())
    assert "regNo" in params, "Missing parameter 'regNo'"

def test_test_student_has_regNo():
    assert hasattr(test_Student, "regNo")
    descriptor = None
    for klass in test_Student.__mro__:
        if "regNo" in klass.__dict__:
            descriptor = klass.__dict__["regNo"]
            break
    assert isinstance(descriptor, property)



def test_test_person_is_not_abstract():
    assert not inspect.isabstract(test_Person)


def test_test_person_constructor_exists():
    assert callable(test_Person.__init__)


def test_test_person_constructor_args():
    sig = inspect.signature(test_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstame" in params, "Missing parameter 'firstame'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "Grade" in params, "Missing parameter 'Grade'"

def test_test_person_has_firstame():
    assert hasattr(test_Person, "firstame")
    descriptor = None
    for klass in test_Person.__mro__:
        if "firstame" in klass.__dict__:
            descriptor = klass.__dict__["firstame"]
            break
    assert isinstance(descriptor, property)

def test_test_person_has_lastname():
    assert hasattr(test_Person, "lastname")
    descriptor = None
    for klass in test_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_test_person_has_Grade():
    assert hasattr(test_Person, "Grade")
    descriptor = None
    for klass in test_Person.__mro__:
        if "Grade" in klass.__dict__:
            descriptor = klass.__dict__["Grade"]
            break
    assert isinstance(descriptor, property)



def test_test_university_is_not_abstract():
    assert not inspect.isabstract(test_University)


def test_test_university_constructor_exists():
    assert callable(test_University.__init__)


def test_test_university_constructor_args():
    sig = inspect.signature(test_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test_university_has_name():
    assert hasattr(test_University, "name")
    descriptor = None
    for klass in test_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grade_exists():
    # Check that the Enumeration exists
    assert Grade is not None

def test_grade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Grade]
    expected_literals = [
        "PHD",
        "None_",
        "MSC",
        "Professor",
        "BSC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Grade"

def test_incomelevel_exists():
    # Check that the Enumeration exists
    assert incomeLevel is not None

def test_incomelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in incomeLevel]
    expected_literals = [
        "Professor",
        "PostDoc",
        "PreDoc",
        "UnderGrad",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in incomeLevel"

def test_eenum0_exists():
    # Check that the Enumeration exists
    assert EEnum0 is not None

def test_eenum0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnum0]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnum0"


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
Person_strategy = st.builds(
    Person,
)
test_Employee_strategy = st.builds(
    test_Employee,
    incomeLevel=
        safe_text
)
test_Student_strategy = st.builds(
    test_Student,
    regNo=
        safe_text
)
test_Person_strategy = st.builds(
    test_Person,
    firstame=
        safe_text,
    lastname=
        safe_text,
    Grade=
        safe_text
)
test_University_strategy = st.builds(
    test_University,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=test_Employee_strategy)
@settings(max_examples=50)
def test_test_employee_instantiation(instance):
    assert isinstance(instance, test_Employee)



@given(instance=test_Employee_strategy)
def test_test_employee_incomeLevel_setter(instance):
    original = instance.incomeLevel
    instance.incomeLevel = original
    assert instance.incomeLevel == original

@given(instance=test_Student_strategy)
@settings(max_examples=50)
def test_test_student_instantiation(instance):
    assert isinstance(instance, test_Student)



@given(instance=test_Student_strategy)
def test_test_student_regNo_setter(instance):
    original = instance.regNo
    instance.regNo = original
    assert instance.regNo == original

@given(instance=test_Person_strategy)
@settings(max_examples=50)
def test_test_person_instantiation(instance):
    assert isinstance(instance, test_Person)



@given(instance=test_Person_strategy)
def test_test_person_firstame_setter(instance):
    original = instance.firstame
    instance.firstame = original
    assert instance.firstame == original



@given(instance=test_Person_strategy)
def test_test_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=test_Person_strategy)
def test_test_person_Grade_setter(instance):
    original = instance.Grade
    instance.Grade = original
    assert instance.Grade == original

@given(instance=test_University_strategy)
@settings(max_examples=50)
def test_test_university_instantiation(instance):
    assert isinstance(instance, test_University)



@given(instance=test_University_strategy)
def test_test_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
