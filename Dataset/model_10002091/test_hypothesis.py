import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    patient,
    team,
    junior_doctor,
    consultant_doctor,
    ward,
    Hospital,
    doctor,
    Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_patient_is_not_abstract():
    assert not inspect.isabstract(patient)


def test_patient_constructor_exists():
    assert callable(patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(patient.__init__)
    params = list(sig.parameters.keys())



def test_team_is_not_abstract():
    assert not inspect.isabstract(team)


def test_team_constructor_exists():
    assert callable(team.__init__)


def test_team_constructor_args():
    sig = inspect.signature(team.__init__)
    params = list(sig.parameters.keys())



def test_junior_doctor_is_not_abstract():
    assert not inspect.isabstract(junior_doctor)


def test_junior_doctor_constructor_exists():
    assert callable(junior_doctor.__init__)


def test_junior_doctor_constructor_args():
    sig = inspect.signature(junior_doctor.__init__)
    params = list(sig.parameters.keys())



def test_consultant_doctor_is_not_abstract():
    assert not inspect.isabstract(consultant_doctor)


def test_consultant_doctor_constructor_exists():
    assert callable(consultant_doctor.__init__)


def test_consultant_doctor_constructor_args():
    sig = inspect.signature(consultant_doctor.__init__)
    params = list(sig.parameters.keys())



def test_ward_is_not_abstract():
    assert not inspect.isabstract(ward)


def test_ward_constructor_exists():
    assert callable(ward.__init__)


def test_ward_constructor_args():
    sig = inspect.signature(ward.__init__)
    params = list(sig.parameters.keys())
    assert "no_of_patients" in params, "Missing parameter 'no_of_patients'"
    assert "ward_id" in params, "Missing parameter 'ward_id'"

def test_ward_has_no_of_patients():
    assert hasattr(ward, "no_of_patients")
    descriptor = None
    for klass in ward.__mro__:
        if "no_of_patients" in klass.__dict__:
            descriptor = klass.__dict__["no_of_patients"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_ward_id():
    assert hasattr(ward, "ward_id")
    descriptor = None
    for klass in ward.__mro__:
        if "ward_id" in klass.__dict__:
            descriptor = klass.__dict__["ward_id"]
            break
    assert isinstance(descriptor, property)



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "totalwards" in params, "Missing parameter 'totalwards'"
    assert "name" in params, "Missing parameter 'name'"

def test_hospital_has_totalwards():
    assert hasattr(Hospital, "totalwards")
    descriptor = None
    for klass in Hospital.__mro__:
        if "totalwards" in klass.__dict__:
            descriptor = klass.__dict__["totalwards"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_name():
    assert hasattr(Hospital, "name")
    descriptor = None
    for klass in Hospital.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(doctor)


def test_doctor_constructor_exists():
    assert callable(doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(doctor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "grade" in params, "Missing parameter 'grade'"

def test_doctor_has_name():
    assert hasattr(doctor, "name")
    descriptor = None
    for klass in doctor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_address():
    assert hasattr(doctor, "address")
    descriptor = None
    for klass in doctor.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_grade():
    assert hasattr(doctor, "grade")
    descriptor = None
    for klass in doctor.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_class1_is_not_abstract():
    assert not inspect.isabstract(Class1)


def test_class1_constructor_exists():
    assert callable(Class1.__init__)


def test_class1_constructor_args():
    sig = inspect.signature(Class1.__init__)
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
patient_strategy = st.builds(
    patient,
)
team_strategy = st.builds(
    team,
)
junior_doctor_strategy = st.builds(
    junior_doctor,
)
consultant_doctor_strategy = st.builds(
    consultant_doctor,
)
ward_strategy = st.builds(
    ward,
    no_of_patients=
        safe_text,
    ward_id=
        st.integers()
)
Hospital_strategy = st.builds(
    Hospital,
    totalwards=
        st.integers(),
    name=
        safe_text
)
doctor_strategy = st.builds(
    doctor,
    name=
        safe_text,
    address=
        safe_text,
    grade=
        safe_text
)
Class1_strategy = st.builds(
    Class1,
)

@given(instance=patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, patient)

@given(instance=team_strategy)
@settings(max_examples=50)
def test_team_instantiation(instance):
    assert isinstance(instance, team)

@given(instance=junior_doctor_strategy)
@settings(max_examples=50)
def test_junior_doctor_instantiation(instance):
    assert isinstance(instance, junior_doctor)

@given(instance=consultant_doctor_strategy)
@settings(max_examples=50)
def test_consultant_doctor_instantiation(instance):
    assert isinstance(instance, consultant_doctor)

@given(instance=ward_strategy)
@settings(max_examples=50)
def test_ward_instantiation(instance):
    assert isinstance(instance, ward)



@given(instance=ward_strategy)
def test_ward_no_of_patients_setter(instance):
    original = instance.no_of_patients
    instance.no_of_patients = original
    assert instance.no_of_patients == original



@given(instance=ward_strategy)
def test_ward_ward_id_setter(instance):
    original = instance.ward_id
    instance.ward_id = original
    assert instance.ward_id == original

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_totalwards_setter(instance):
    original = instance.totalwards
    instance.totalwards = original
    assert instance.totalwards == original



@given(instance=Hospital_strategy)
def test_hospital_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, doctor)



@given(instance=doctor_strategy)
def test_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=doctor_strategy)
def test_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=doctor_strategy)
def test_doctor_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=Class1_strategy)
@settings(max_examples=50)
def test_class1_instantiation(instance):
    assert isinstance(instance, Class1)
