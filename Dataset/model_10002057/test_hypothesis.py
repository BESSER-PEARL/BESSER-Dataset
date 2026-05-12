import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hospital,
    Patients,
    Receptionist,
    Docter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "Operation_Theater" in params, "Missing parameter 'Operation_Theater'"
    assert "Cariology" in params, "Missing parameter 'Cariology'"
    assert "HR" in params, "Missing parameter 'HR'"

def test_hospital_has_Operation_Theater():
    assert hasattr(Hospital, "Operation_Theater")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Operation_Theater" in klass.__dict__:
            descriptor = klass.__dict__["Operation_Theater"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_Cariology():
    assert hasattr(Hospital, "Cariology")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Cariology" in klass.__dict__:
            descriptor = klass.__dict__["Cariology"]
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



def test_patients_is_not_abstract():
    assert not inspect.isabstract(Patients)


def test_patients_constructor_exists():
    assert callable(Patients.__init__)


def test_patients_constructor_args():
    sig = inspect.signature(Patients.__init__)
    params = list(sig.parameters.keys())
    assert "Patient_name" in params, "Missing parameter 'Patient_name'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"
    assert "NIC_NO" in params, "Missing parameter 'NIC_NO'"
    assert "Phone_no" in params, "Missing parameter 'Phone_no'"

def test_patients_has_Patient_name():
    assert hasattr(Patients, "Patient_name")
    descriptor = None
    for klass in Patients.__mro__:
        if "Patient_name" in klass.__dict__:
            descriptor = klass.__dict__["Patient_name"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_Sickness():
    assert hasattr(Patients, "Sickness")
    descriptor = None
    for klass in Patients.__mro__:
        if "Sickness" in klass.__dict__:
            descriptor = klass.__dict__["Sickness"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_NIC_NO():
    assert hasattr(Patients, "NIC_NO")
    descriptor = None
    for klass in Patients.__mro__:
        if "NIC_NO" in klass.__dict__:
            descriptor = klass.__dict__["NIC_NO"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_Phone_no():
    assert hasattr(Patients, "Phone_no")
    descriptor = None
    for klass in Patients.__mro__:
        if "Phone_no" in klass.__dict__:
            descriptor = klass.__dict__["Phone_no"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Employee_ID" in params, "Missing parameter 'Employee_ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_receptionist_has_Employee_ID():
    assert hasattr(Receptionist, "Employee_ID")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Employee_ID" in klass.__dict__:
            descriptor = klass.__dict__["Employee_ID"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_Name():
    assert hasattr(Receptionist, "Name")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_docter_is_not_abstract():
    assert not inspect.isabstract(Docter)


def test_docter_constructor_exists():
    assert callable(Docter.__init__)


def test_docter_constructor_args():
    sig = inspect.signature(Docter.__init__)
    params = list(sig.parameters.keys())
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Rank" in params, "Missing parameter 'Rank'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Salary" in params, "Missing parameter 'Salary'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_docter_has_Specialization():
    assert hasattr(Docter, "Specialization")
    descriptor = None
    for klass in Docter.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)

def test_docter_has_Rank():
    assert hasattr(Docter, "Rank")
    descriptor = None
    for klass in Docter.__mro__:
        if "Rank" in klass.__dict__:
            descriptor = klass.__dict__["Rank"]
            break
    assert isinstance(descriptor, property)

def test_docter_has_ID():
    assert hasattr(Docter, "ID")
    descriptor = None
    for klass in Docter.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_docter_has_Salary():
    assert hasattr(Docter, "Salary")
    descriptor = None
    for klass in Docter.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)

def test_docter_has_attribute2():
    assert hasattr(Docter, "attribute2")
    descriptor = None
    for klass in Docter.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_docter_has_Name():
    assert hasattr(Docter, "Name")
    descriptor = None
    for klass in Docter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Hospital_strategy = st.builds(
    Hospital,
    Operation_Theater=
        safe_text,
    Cariology=
        safe_text,
    HR=
        safe_text
)
Patients_strategy = st.builds(
    Patients,
    Patient_name=
        safe_text,
    Sickness=
        safe_text,
    NIC_NO=
        st.integers(),
    Phone_no=
        st.integers()
)
Receptionist_strategy = st.builds(
    Receptionist,
    Employee_ID=
        st.integers(),
    Name=
        safe_text
)
Docter_strategy = st.builds(
    Docter,
    Specialization=
        safe_text,
    Rank=
        safe_text,
    ID=
        st.integers(),
    Salary=
        safe_text,
    attribute2=
        safe_text,
    Name=
        safe_text
)

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_Operation_Theater_setter(instance):
    original = instance.Operation_Theater
    instance.Operation_Theater = original
    assert instance.Operation_Theater == original



@given(instance=Hospital_strategy)
def test_hospital_Cariology_setter(instance):
    original = instance.Cariology
    instance.Cariology = original
    assert instance.Cariology == original



@given(instance=Hospital_strategy)
def test_hospital_HR_setter(instance):
    original = instance.HR
    instance.HR = original
    assert instance.HR == original

@given(instance=Patients_strategy)
@settings(max_examples=50)
def test_patients_instantiation(instance):
    assert isinstance(instance, Patients)



@given(instance=Patients_strategy)
def test_patients_Patient_name_setter(instance):
    original = instance.Patient_name
    instance.Patient_name = original
    assert instance.Patient_name == original



@given(instance=Patients_strategy)
def test_patients_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original



@given(instance=Patients_strategy)
def test_patients_NIC_NO_setter(instance):
    original = instance.NIC_NO
    instance.NIC_NO = original
    assert instance.NIC_NO == original



@given(instance=Patients_strategy)
def test_patients_Phone_no_setter(instance):
    original = instance.Phone_no
    instance.Phone_no = original
    assert instance.Phone_no == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_Employee_ID_setter(instance):
    original = instance.Employee_ID
    instance.Employee_ID = original
    assert instance.Employee_ID == original



@given(instance=Receptionist_strategy)
def test_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Docter_strategy)
@settings(max_examples=50)
def test_docter_instantiation(instance):
    assert isinstance(instance, Docter)



@given(instance=Docter_strategy)
def test_docter_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Docter_strategy)
def test_docter_Rank_setter(instance):
    original = instance.Rank
    instance.Rank = original
    assert instance.Rank == original



@given(instance=Docter_strategy)
def test_docter_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Docter_strategy)
def test_docter_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original



@given(instance=Docter_strategy)
def test_docter_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Docter_strategy)
def test_docter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
