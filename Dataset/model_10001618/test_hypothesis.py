import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hospital_Management_System,
    Receptionist,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hospital_management_system_is_not_abstract():
    assert not inspect.isabstract(Hospital_Management_System)


def test_hospital_management_system_constructor_exists():
    assert callable(Hospital_Management_System.__init__)


def test_hospital_management_system_constructor_args():
    sig = inspect.signature(Hospital_Management_System.__init__)
    params = list(sig.parameters.keys())
    assert "Code" in params, "Missing parameter 'Code'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_hospital_management_system_has_Code():
    assert hasattr(Hospital_Management_System, "Code")
    descriptor = None
    for klass in Hospital_Management_System.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
            break
    assert isinstance(descriptor, property)

def test_hospital_management_system_has_Name():
    assert hasattr(Hospital_Management_System, "Name")
    descriptor = None
    for klass in Hospital_Management_System.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hospital_management_system_has_Address():
    assert hasattr(Hospital_Management_System, "Address")
    descriptor = None
    for klass in Hospital_Management_System.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_receptionist_has_Name():
    assert hasattr(Receptionist, "Name")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_ID():
    assert hasattr(Receptionist, "ID")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "PatID" in params, "Missing parameter 'PatID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "TelNo" in params, "Missing parameter 'TelNo'"

def test_patient_has_PatID():
    assert hasattr(Patient, "PatID")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatID" in klass.__dict__:
            descriptor = klass.__dict__["PatID"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Name():
    assert hasattr(Patient, "Name")
    descriptor = None
    for klass in Patient.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Address():
    assert hasattr(Patient, "Address")
    descriptor = None
    for klass in Patient.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_RoomNo():
    assert hasattr(Patient, "RoomNo")
    descriptor = None
    for klass in Patient.__mro__:
        if "RoomNo" in klass.__dict__:
            descriptor = klass.__dict__["RoomNo"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Age():
    assert hasattr(Patient, "Age")
    descriptor = None
    for klass in Patient.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Gender():
    assert hasattr(Patient, "Gender")
    descriptor = None
    for klass in Patient.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_TelNo():
    assert hasattr(Patient, "TelNo")
    descriptor = None
    for klass in Patient.__mro__:
        if "TelNo" in klass.__dict__:
            descriptor = klass.__dict__["TelNo"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "DocID" in params, "Missing parameter 'DocID'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phone" in params, "Missing parameter 'Phone'"

def test_doctor_has_Specialization():
    assert hasattr(Doctor, "Specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Name():
    assert hasattr(Doctor, "Name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Department():
    assert hasattr(Doctor, "Department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DocID():
    assert hasattr(Doctor, "DocID")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DocID" in klass.__dict__:
            descriptor = klass.__dict__["DocID"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Address():
    assert hasattr(Doctor, "Address")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Phone():
    assert hasattr(Doctor, "Phone")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
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
Hospital_Management_System_strategy = st.builds(
    Hospital_Management_System,
    Code=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    Name=
        safe_text,
    ID=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    PatID=
        st.integers(),
    Name=
        safe_text,
    Address=
        safe_text,
    RoomNo=
        st.integers(),
    Age=
        st.integers(),
    Gender=
        safe_text,
    TelNo=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    Specialization=
        safe_text,
    Name=
        safe_text,
    Department=
        safe_text,
    DocID=
        st.integers(),
    Address=
        safe_text,
    Phone=
        st.integers()
)

@given(instance=Hospital_Management_System_strategy)
@settings(max_examples=50)
def test_hospital_management_system_instantiation(instance):
    assert isinstance(instance, Hospital_Management_System)



@given(instance=Hospital_Management_System_strategy)
def test_hospital_management_system_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original



@given(instance=Hospital_Management_System_strategy)
def test_hospital_management_system_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Hospital_Management_System_strategy)
def test_hospital_management_system_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Receptionist_strategy)
def test_receptionist_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_PatID_setter(instance):
    original = instance.PatID
    instance.PatID = original
    assert instance.PatID == original



@given(instance=Patient_strategy)
def test_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_patient_RoomNo_setter(instance):
    original = instance.RoomNo
    instance.RoomNo = original
    assert instance.RoomNo == original



@given(instance=Patient_strategy)
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_patient_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Patient_strategy)
def test_patient_TelNo_setter(instance):
    original = instance.TelNo
    instance.TelNo = original
    assert instance.TelNo == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Doctor_strategy)
def test_doctor_DocID_setter(instance):
    original = instance.DocID
    instance.DocID = original
    assert instance.DocID == original



@given(instance=Doctor_strategy)
def test_doctor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Doctor_strategy)
def test_doctor_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original
