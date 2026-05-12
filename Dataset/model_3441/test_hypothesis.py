import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Student,
    SourceModel_BachelorStudent,
    SourceModel_MasterStudent,
    Person,
    SourceModel_Professor,
    SourceModel_Student,
    SourceModel_Person,
    SourceModel_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel_bachelorstudent_is_not_abstract():
    assert not inspect.isabstract(SourceModel_BachelorStudent)


def test_sourcemodel_bachelorstudent_constructor_exists():
    assert callable(SourceModel_BachelorStudent.__init__)


def test_sourcemodel_bachelorstudent_constructor_args():
    sig = inspect.signature(SourceModel_BachelorStudent.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel_masterstudent_is_not_abstract():
    assert not inspect.isabstract(SourceModel_MasterStudent)


def test_sourcemodel_masterstudent_constructor_exists():
    assert callable(SourceModel_MasterStudent.__init__)


def test_sourcemodel_masterstudent_constructor_args():
    sig = inspect.signature(SourceModel_MasterStudent.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel_professor_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Professor)


def test_sourcemodel_professor_constructor_exists():
    assert callable(SourceModel_Professor.__init__)


def test_sourcemodel_professor_constructor_args():
    sig = inspect.signature(SourceModel_Professor.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel_student_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Student)


def test_sourcemodel_student_constructor_exists():
    assert callable(SourceModel_Student.__init__)


def test_sourcemodel_student_constructor_args():
    sig = inspect.signature(SourceModel_Student.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel_person_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Person)


def test_sourcemodel_person_constructor_exists():
    assert callable(SourceModel_Person.__init__)


def test_sourcemodel_person_constructor_args():
    sig = inspect.signature(SourceModel_Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"

def test_sourcemodel_person_has_age():
    assert hasattr(SourceModel_Person, "age")
    descriptor = None
    for klass in SourceModel_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_sourcemodel_container_is_not_abstract():
    assert not inspect.isabstract(SourceModel_Container)


def test_sourcemodel_container_constructor_exists():
    assert callable(SourceModel_Container.__init__)


def test_sourcemodel_container_constructor_args():
    sig = inspect.signature(SourceModel_Container.__init__)
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
Student_strategy = st.builds(
    Student,
)
SourceModel_BachelorStudent_strategy = st.builds(
    SourceModel_BachelorStudent,
)
SourceModel_MasterStudent_strategy = st.builds(
    SourceModel_MasterStudent,
)
Person_strategy = st.builds(
    Person,
)
SourceModel_Professor_strategy = st.builds(
    SourceModel_Professor,
)
SourceModel_Student_strategy = st.builds(
    SourceModel_Student,
)
SourceModel_Person_strategy = st.builds(
    SourceModel_Person,
    age=
        safe_text
)
SourceModel_Container_strategy = st.builds(
    SourceModel_Container,
)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)

@given(instance=SourceModel_BachelorStudent_strategy)
@settings(max_examples=50)
def test_sourcemodel_bachelorstudent_instantiation(instance):
    assert isinstance(instance, SourceModel_BachelorStudent)

@given(instance=SourceModel_MasterStudent_strategy)
@settings(max_examples=50)
def test_sourcemodel_masterstudent_instantiation(instance):
    assert isinstance(instance, SourceModel_MasterStudent)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=SourceModel_Professor_strategy)
@settings(max_examples=50)
def test_sourcemodel_professor_instantiation(instance):
    assert isinstance(instance, SourceModel_Professor)

@given(instance=SourceModel_Student_strategy)
@settings(max_examples=50)
def test_sourcemodel_student_instantiation(instance):
    assert isinstance(instance, SourceModel_Student)

@given(instance=SourceModel_Person_strategy)
@settings(max_examples=50)
def test_sourcemodel_person_instantiation(instance):
    assert isinstance(instance, SourceModel_Person)



@given(instance=SourceModel_Person_strategy)
def test_sourcemodel_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=SourceModel_Container_strategy)
@settings(max_examples=50)
def test_sourcemodel_container_instantiation(instance):
    assert isinstance(instance, SourceModel_Container)
