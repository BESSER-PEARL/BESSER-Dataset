import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    myDsl::Teacher,
    myDsl::Student,
    myDsl::Person,
    myDsl::School,
    myDsl::SchoolModel,
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



def test_mydsl::teacher_is_not_abstract():
    assert not inspect.isabstract(myDsl::Teacher)


def test_mydsl::teacher_constructor_exists():
    assert callable(myDsl::Teacher.__init__)


def test_mydsl::teacher_constructor_args():
    sig = inspect.signature(myDsl::Teacher.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::student_is_not_abstract():
    assert not inspect.isabstract(myDsl::Student)


def test_mydsl::student_constructor_exists():
    assert callable(myDsl::Student.__init__)


def test_mydsl::student_constructor_args():
    sig = inspect.signature(myDsl::Student.__init__)
    params = list(sig.parameters.keys())
    assert "registrationNum" in params, "Missing parameter 'registrationNum'"

def test_mydsl::student_has_registrationNum():
    assert hasattr(myDsl::Student, "registrationNum")
    descriptor = None
    for klass in myDsl::Student.__mro__:
        if "registrationNum" in klass.__dict__:
            descriptor = klass.__dict__["registrationNum"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::person_is_not_abstract():
    assert not inspect.isabstract(myDsl::Person)


def test_mydsl::person_constructor_exists():
    assert callable(myDsl::Person.__init__)


def test_mydsl::person_constructor_args():
    sig = inspect.signature(myDsl::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::person_has_name():
    assert hasattr(myDsl::Person, "name")
    descriptor = None
    for klass in myDsl::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::school_is_not_abstract():
    assert not inspect.isabstract(myDsl::School)


def test_mydsl::school_constructor_exists():
    assert callable(myDsl::School.__init__)


def test_mydsl::school_constructor_args():
    sig = inspect.signature(myDsl::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::school_has_name():
    assert hasattr(myDsl::School, "name")
    descriptor = None
    for klass in myDsl::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::schoolmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl::SchoolModel)


def test_mydsl::schoolmodel_constructor_exists():
    assert callable(myDsl::SchoolModel.__init__)


def test_mydsl::schoolmodel_constructor_args():
    sig = inspect.signature(myDsl::SchoolModel.__init__)
    params = list(sig.parameters.keys())


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
myDsl::Teacher_strategy = st.builds(
    myDsl::Teacher,
)
myDsl::Student_strategy = st.builds(
    myDsl::Student,
    registrationNum=
        st.integers()
)
myDsl::Person_strategy = st.builds(
    myDsl::Person,
    name=
        safe_text
)
myDsl::School_strategy = st.builds(
    myDsl::School,
    name=
        safe_text
)
myDsl::SchoolModel_strategy = st.builds(
    myDsl::SchoolModel,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=myDsl::Teacher_strategy)
@settings(max_examples=50)
def test_mydsl::teacher_instantiation(instance):
    assert isinstance(instance, myDsl::Teacher)

@given(instance=myDsl::Student_strategy)
@settings(max_examples=50)
def test_mydsl::student_instantiation(instance):
    assert isinstance(instance, myDsl::Student)

@given(instance=myDsl::Student_strategy)
def test_mydsl::student_registrationNum_type(instance):
    assert isinstance(instance.registrationNum, int)


@given(instance=myDsl::Student_strategy)
def test_mydsl::student_registrationNum_setter(instance):
    original = instance.registrationNum
    instance.registrationNum = original
    assert instance.registrationNum == original

@given(instance=myDsl::Person_strategy)
@settings(max_examples=50)
def test_mydsl::person_instantiation(instance):
    assert isinstance(instance, myDsl::Person)

@given(instance=myDsl::Person_strategy)
def test_mydsl::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Person_strategy)
def test_mydsl::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::School_strategy)
@settings(max_examples=50)
def test_mydsl::school_instantiation(instance):
    assert isinstance(instance, myDsl::School)

@given(instance=myDsl::School_strategy)
def test_mydsl::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::School_strategy)
def test_mydsl::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::SchoolModel_strategy)
@settings(max_examples=50)
def test_mydsl::schoolmodel_instantiation(instance):
    assert isinstance(instance, myDsl::SchoolModel)
