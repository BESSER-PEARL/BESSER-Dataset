import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hospital_Doctor,
    Hospital__Receptionist,
    Hospital,
    Hospital_Patients,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hospital_doctor_is_not_abstract():
    assert not inspect.isabstract(Hospital_Doctor)


def test_hospital_doctor_constructor_exists():
    assert callable(Hospital_Doctor.__init__)


def test_hospital_doctor_constructor_args():
    sig = inspect.signature(Hospital_Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Rank" in params, "Missing parameter 'Rank'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Salary" in params, "Missing parameter 'Salary'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"

def test_hospital_doctor_has_Name():
    assert hasattr(Hospital_Doctor, "Name")
    descriptor = None
    for klass in Hospital_Doctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hospital_doctor_has_Rank():
    assert hasattr(Hospital_Doctor, "Rank")
    descriptor = None
    for klass in Hospital_Doctor.__mro__:
        if "Rank" in klass.__dict__:
            descriptor = klass.__dict__["Rank"]
            break
    assert isinstance(descriptor, property)

def test_hospital_doctor_has_ID():
    assert hasattr(Hospital_Doctor, "ID")
    descriptor = None
    for klass in Hospital_Doctor.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_hospital_doctor_has_Salary():
    assert hasattr(Hospital_Doctor, "Salary")
    descriptor = None
    for klass in Hospital_Doctor.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)

def test_hospital_doctor_has_Specialization():
    assert hasattr(Hospital_Doctor, "Specialization")
    descriptor = None
    for klass in Hospital_Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)



def test_hospital__receptionist_is_not_abstract():
    assert not inspect.isabstract(Hospital__Receptionist)


def test_hospital__receptionist_constructor_exists():
    assert callable(Hospital__Receptionist.__init__)


def test_hospital__receptionist_constructor_args():
    sig = inspect.signature(Hospital__Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Employee_ID" in params, "Missing parameter 'Employee_ID'"

def test_hospital__receptionist_has_Name():
    assert hasattr(Hospital__Receptionist, "Name")
    descriptor = None
    for klass in Hospital__Receptionist.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hospital__receptionist_has_Employee_ID():
    assert hasattr(Hospital__Receptionist, "Employee_ID")
    descriptor = None
    for klass in Hospital__Receptionist.__mro__:
        if "Employee_ID" in klass.__dict__:
            descriptor = klass.__dict__["Employee_ID"]
            break
    assert isinstance(descriptor, property)



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "Cardiology" in params, "Missing parameter 'Cardiology'"
    assert "HR" in params, "Missing parameter 'HR'"
    assert "Operation_Theater" in params, "Missing parameter 'Operation_Theater'"
    assert "Cancer_Center" in params, "Missing parameter 'Cancer_Center'"

def test_hospital_has_Cardiology():
    assert hasattr(Hospital, "Cardiology")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Cardiology" in klass.__dict__:
            descriptor = klass.__dict__["Cardiology"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_HR():
    assert hasattr(Hospital, "HR")
    descriptor = None
    for klass in Hospital.__mro__:
        if "HR" in klass.__dict__:
            descriptor = klass.__dict__["HR"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_Operation_Theater():
    assert hasattr(Hospital, "Operation_Theater")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Operation_Theater" in klass.__dict__:
            descriptor = klass.__dict__["Operation_Theater"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_Cancer_Center():
    assert hasattr(Hospital, "Cancer_Center")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Cancer_Center" in klass.__dict__:
            descriptor = klass.__dict__["Cancer_Center"]
            break
    assert isinstance(descriptor, property)



def test_hospital_patients_is_not_abstract():
    assert not inspect.isabstract(Hospital_Patients)


def test_hospital_patients_constructor_exists():
    assert callable(Hospital_Patients.__init__)


def test_hospital_patients_constructor_args():
    sig = inspect.signature(Hospital_Patients.__init__)
    params = list(sig.parameters.keys())
    assert "Sickness" in params, "Missing parameter 'Sickness'"
    assert "NIC_Number" in params, "Missing parameter 'NIC_Number'"
    assert "Phone_Number" in params, "Missing parameter 'Phone_Number'"
    assert "Patient_s_Name" in params, "Missing parameter 'Patient_s_Name'"

def test_hospital_patients_has_Sickness():
    assert hasattr(Hospital_Patients, "Sickness")
    descriptor = None
    for klass in Hospital_Patients.__mro__:
        if "Sickness" in klass.__dict__:
            descriptor = klass.__dict__["Sickness"]
            break
    assert isinstance(descriptor, property)

def test_hospital_patients_has_NIC_Number():
    assert hasattr(Hospital_Patients, "NIC_Number")
    descriptor = None
    for klass in Hospital_Patients.__mro__:
        if "NIC_Number" in klass.__dict__:
            descriptor = klass.__dict__["NIC_Number"]
            break
    assert isinstance(descriptor, property)

def test_hospital_patients_has_Phone_Number():
    assert hasattr(Hospital_Patients, "Phone_Number")
    descriptor = None
    for klass in Hospital_Patients.__mro__:
        if "Phone_Number" in klass.__dict__:
            descriptor = klass.__dict__["Phone_Number"]
            break
    assert isinstance(descriptor, property)

def test_hospital_patients_has_Patient_s_Name():
    assert hasattr(Hospital_Patients, "Patient_s_Name")
    descriptor = None
    for klass in Hospital_Patients.__mro__:
        if "Patient_s_Name" in klass.__dict__:
            descriptor = klass.__dict__["Patient_s_Name"]
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
Hospital_Doctor_strategy = st.builds(
    Hospital_Doctor,
    Name=
        safe_text,
    Rank=
        safe_text,
    ID=
        st.integers(),
    Salary=
        st.integers(),
    Specialization=
        safe_text
)
Hospital__Receptionist_strategy = st.builds(
    Hospital__Receptionist,
    Name=
        safe_text,
    Employee_ID=
        st.integers()
)
Hospital_strategy = st.builds(
    Hospital,
    Cardiology=
        safe_text,
    HR=
        safe_text,
    Operation_Theater=
        safe_text,
    Cancer_Center=
        safe_text
)
Hospital_Patients_strategy = st.builds(
    Hospital_Patients,
    Sickness=
        safe_text,
    NIC_Number=
        st.integers(),
    Phone_Number=
        st.integers(),
    Patient_s_Name=
        safe_text
)

@given(instance=Hospital_Doctor_strategy)
@settings(max_examples=50)
def test_hospital_doctor_instantiation(instance):
    assert isinstance(instance, Hospital_Doctor)



@given(instance=Hospital_Doctor_strategy)
def test_hospital_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Hospital_Doctor_strategy)
def test_hospital_doctor_Rank_setter(instance):
    original = instance.Rank
    instance.Rank = original
    assert instance.Rank == original



@given(instance=Hospital_Doctor_strategy)
def test_hospital_doctor_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Hospital_Doctor_strategy)
def test_hospital_doctor_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original



@given(instance=Hospital_Doctor_strategy)
def test_hospital_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original

@given(instance=Hospital__Receptionist_strategy)
@settings(max_examples=50)
def test_hospital__receptionist_instantiation(instance):
    assert isinstance(instance, Hospital__Receptionist)



@given(instance=Hospital__Receptionist_strategy)
def test_hospital__receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Hospital__Receptionist_strategy)
def test_hospital__receptionist_Employee_ID_setter(instance):
    original = instance.Employee_ID
    instance.Employee_ID = original
    assert instance.Employee_ID == original

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_Cardiology_setter(instance):
    original = instance.Cardiology
    instance.Cardiology = original
    assert instance.Cardiology == original



@given(instance=Hospital_strategy)
def test_hospital_HR_setter(instance):
    original = instance.HR
    instance.HR = original
    assert instance.HR == original



@given(instance=Hospital_strategy)
def test_hospital_Operation_Theater_setter(instance):
    original = instance.Operation_Theater
    instance.Operation_Theater = original
    assert instance.Operation_Theater == original



@given(instance=Hospital_strategy)
def test_hospital_Cancer_Center_setter(instance):
    original = instance.Cancer_Center
    instance.Cancer_Center = original
    assert instance.Cancer_Center == original

@given(instance=Hospital_Patients_strategy)
@settings(max_examples=50)
def test_hospital_patients_instantiation(instance):
    assert isinstance(instance, Hospital_Patients)



@given(instance=Hospital_Patients_strategy)
def test_hospital_patients_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original



@given(instance=Hospital_Patients_strategy)
def test_hospital_patients_NIC_Number_setter(instance):
    original = instance.NIC_Number
    instance.NIC_Number = original
    assert instance.NIC_Number == original



@given(instance=Hospital_Patients_strategy)
def test_hospital_patients_Phone_Number_setter(instance):
    original = instance.Phone_Number
    instance.Phone_Number = original
    assert instance.Phone_Number == original



@given(instance=Hospital_Patients_strategy)
def test_hospital_patients_Patient_s_Name_setter(instance):
    original = instance.Patient_s_Name
    instance.Patient_s_Name = original
    assert instance.Patient_s_Name == original
