import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    test::Employee,
    test::Student,
    test::Person,
    test::University,
    EEnum0,
    incomeLevel,
    Grade,
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



def test_test::employee_is_not_abstract():
    assert not inspect.isabstract(test::Employee)


def test_test::employee_constructor_exists():
    assert callable(test::Employee.__init__)


def test_test::employee_constructor_args():
    sig = inspect.signature(test::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "incomeLevel" in params, "Missing parameter 'incomeLevel'"

def test_test::employee_has_incomeLevel():
    assert hasattr(test::Employee, "incomeLevel")
    descriptor = None
    for klass in test::Employee.__mro__:
        if "incomeLevel" in klass.__dict__:
            descriptor = klass.__dict__["incomeLevel"]
            break
    assert isinstance(descriptor, property)



def test_test::student_is_not_abstract():
    assert not inspect.isabstract(test::Student)


def test_test::student_constructor_exists():
    assert callable(test::Student.__init__)


def test_test::student_constructor_args():
    sig = inspect.signature(test::Student.__init__)
    params = list(sig.parameters.keys())
    assert "regNo" in params, "Missing parameter 'regNo'"

def test_test::student_has_regNo():
    assert hasattr(test::Student, "regNo")
    descriptor = None
    for klass in test::Student.__mro__:
        if "regNo" in klass.__dict__:
            descriptor = klass.__dict__["regNo"]
            break
    assert isinstance(descriptor, property)



def test_test::person_is_not_abstract():
    assert not inspect.isabstract(test::Person)


def test_test::person_constructor_exists():
    assert callable(test::Person.__init__)


def test_test::person_constructor_args():
    sig = inspect.signature(test::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstame" in params, "Missing parameter 'firstame'"
    assert "Grade" in params, "Missing parameter 'Grade'"

def test_test::person_has_lastname():
    assert hasattr(test::Person, "lastname")
    descriptor = None
    for klass in test::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_test::person_has_firstame():
    assert hasattr(test::Person, "firstame")
    descriptor = None
    for klass in test::Person.__mro__:
        if "firstame" in klass.__dict__:
            descriptor = klass.__dict__["firstame"]
            break
    assert isinstance(descriptor, property)

def test_test::person_has_Grade():
    assert hasattr(test::Person, "Grade")
    descriptor = None
    for klass in test::Person.__mro__:
        if "Grade" in klass.__dict__:
            descriptor = klass.__dict__["Grade"]
            break
    assert isinstance(descriptor, property)



def test_test::university_is_not_abstract():
    assert not inspect.isabstract(test::University)


def test_test::university_constructor_exists():
    assert callable(test::University.__init__)


def test_test::university_constructor_args():
    sig = inspect.signature(test::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test::university_has_name():
    assert hasattr(test::University, "name")
    descriptor = None
    for klass in test::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_incomelevel_exists():
    # Check that the Enumeration exists
    assert incomeLevel is not None

def test_incomelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in incomeLevel]
    expected_literals = [
        "PostDoc",
        "UnderGrad",
        "Professor",
        "PreDoc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in incomeLevel"

def test_grade_exists():
    # Check that the Enumeration exists
    assert Grade is not None

def test_grade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Grade]
    expected_literals = [
        "Professor",
        "MSC",
        "BSC",
        "PHD",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Grade"


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
test::Employee_strategy = st.builds(
    test::Employee,
    incomeLevel=
        safe_text
)
test::Student_strategy = st.builds(
    test::Student,
    regNo=
        safe_text
)
test::Person_strategy = st.builds(
    test::Person,
    lastname=
        safe_text,
    firstame=
        safe_text,
    Grade=
        safe_text
)
test::University_strategy = st.builds(
    test::University,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=test::Employee_strategy)
@settings(max_examples=50)
def test_test::employee_instantiation(instance):
    assert isinstance(instance, test::Employee)

@given(instance=test::Employee_strategy)
def test_test::employee_incomeLevel_type(instance):
    assert isinstance(instance.incomeLevel, str)


@given(instance=test::Employee_strategy)
def test_test::employee_incomeLevel_setter(instance):
    original = instance.incomeLevel
    instance.incomeLevel = original
    assert instance.incomeLevel == original

@given(instance=test::Student_strategy)
@settings(max_examples=50)
def test_test::student_instantiation(instance):
    assert isinstance(instance, test::Student)

@given(instance=test::Student_strategy)
def test_test::student_regNo_type(instance):
    assert isinstance(instance.regNo, str)


@given(instance=test::Student_strategy)
def test_test::student_regNo_setter(instance):
    original = instance.regNo
    instance.regNo = original
    assert instance.regNo == original

@given(instance=test::Person_strategy)
@settings(max_examples=50)
def test_test::person_instantiation(instance):
    assert isinstance(instance, test::Person)

@given(instance=test::Person_strategy)
def test_test::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=test::Person_strategy)
def test_test::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=test::Person_strategy)
def test_test::person_firstame_type(instance):
    assert isinstance(instance.firstame, str)


@given(instance=test::Person_strategy)
def test_test::person_firstame_setter(instance):
    original = instance.firstame
    instance.firstame = original
    assert instance.firstame == original

@given(instance=test::Person_strategy)
def test_test::person_Grade_type(instance):
    assert isinstance(instance.Grade, str)


@given(instance=test::Person_strategy)
def test_test::person_Grade_setter(instance):
    original = instance.Grade
    instance.Grade = original
    assert instance.Grade == original

@given(instance=test::University_strategy)
@settings(max_examples=50)
def test_test::university_instantiation(instance):
    assert isinstance(instance, test::University)

@given(instance=test::University_strategy)
def test_test::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::University_strategy)
def test_test::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
