import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    myDsl_Teacher,
    myDsl_Student,
    myDsl_Person,
    myDsl_School,
    myDsl_SchoolModel,
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



def test_mydsl_teacher_is_not_abstract():
    assert not inspect.isabstract(myDsl_Teacher)


def test_mydsl_teacher_constructor_exists():
    assert callable(myDsl_Teacher.__init__)


def test_mydsl_teacher_constructor_args():
    sig = inspect.signature(myDsl_Teacher.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_student_is_not_abstract():
    assert not inspect.isabstract(myDsl_Student)


def test_mydsl_student_constructor_exists():
    assert callable(myDsl_Student.__init__)


def test_mydsl_student_constructor_args():
    sig = inspect.signature(myDsl_Student.__init__)
    params = list(sig.parameters.keys())
    assert "registrationNum" in params, "Missing parameter 'registrationNum'"

def test_mydsl_student_has_registrationNum():
    assert hasattr(myDsl_Student, "registrationNum")
    descriptor = None
    for klass in myDsl_Student.__mro__:
        if "registrationNum" in klass.__dict__:
            descriptor = klass.__dict__["registrationNum"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_person_is_not_abstract():
    assert not inspect.isabstract(myDsl_Person)


def test_mydsl_person_constructor_exists():
    assert callable(myDsl_Person.__init__)


def test_mydsl_person_constructor_args():
    sig = inspect.signature(myDsl_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_person_has_name():
    assert hasattr(myDsl_Person, "name")
    descriptor = None
    for klass in myDsl_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_school_is_not_abstract():
    assert not inspect.isabstract(myDsl_School)


def test_mydsl_school_constructor_exists():
    assert callable(myDsl_School.__init__)


def test_mydsl_school_constructor_args():
    sig = inspect.signature(myDsl_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_school_has_name():
    assert hasattr(myDsl_School, "name")
    descriptor = None
    for klass in myDsl_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_schoolmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl_SchoolModel)


def test_mydsl_schoolmodel_constructor_exists():
    assert callable(myDsl_SchoolModel.__init__)


def test_mydsl_schoolmodel_constructor_args():
    sig = inspect.signature(myDsl_SchoolModel.__init__)
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
myDsl_Teacher_strategy = st.builds(
    myDsl_Teacher,
)
myDsl_Student_strategy = st.builds(
    myDsl_Student,
    registrationNum=
        st.integers()
)
myDsl_Person_strategy = st.builds(
    myDsl_Person,
    name=
        safe_text
)
myDsl_School_strategy = st.builds(
    myDsl_School,
    name=
        safe_text
)
myDsl_SchoolModel_strategy = st.builds(
    myDsl_SchoolModel,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=myDsl_Teacher_strategy)
@settings(max_examples=50)
def test_mydsl_teacher_instantiation(instance):
    assert isinstance(instance, myDsl_Teacher)

@given(instance=myDsl_Student_strategy)
@settings(max_examples=50)
def test_mydsl_student_instantiation(instance):
    assert isinstance(instance, myDsl_Student)



@given(instance=myDsl_Student_strategy)
def test_mydsl_student_registrationNum_setter(instance):
    original = instance.registrationNum
    instance.registrationNum = original
    assert instance.registrationNum == original

@given(instance=myDsl_Person_strategy)
@settings(max_examples=50)
def test_mydsl_person_instantiation(instance):
    assert isinstance(instance, myDsl_Person)



@given(instance=myDsl_Person_strategy)
def test_mydsl_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_School_strategy)
@settings(max_examples=50)
def test_mydsl_school_instantiation(instance):
    assert isinstance(instance, myDsl_School)



@given(instance=myDsl_School_strategy)
def test_mydsl_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_SchoolModel_strategy)
@settings(max_examples=50)
def test_mydsl_schoolmodel_instantiation(instance):
    assert isinstance(instance, myDsl_SchoolModel)
