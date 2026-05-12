import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Nurse,
    Patient,
    Bill,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_nurse_has_ID():
    assert hasattr(Nurse, "ID")
    descriptor = None
    for klass in Nurse.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_nurse_has_Name():
    assert hasattr(Nurse, "Name")
    descriptor = None
    for klass in Nurse.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "TelephoneNo" in params, "Missing parameter 'TelephoneNo'"
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "PatientID" in params, "Missing parameter 'PatientID'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_patient_has_TelephoneNo():
    assert hasattr(Patient, "TelephoneNo")
    descriptor = None
    for klass in Patient.__mro__:
        if "TelephoneNo" in klass.__dict__:
            descriptor = klass.__dict__["TelephoneNo"]
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

def test_patient_has_PatientID():
    assert hasattr(Patient, "PatientID")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatientID" in klass.__dict__:
            descriptor = klass.__dict__["PatientID"]
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

def test_patient_has_Sex():
    assert hasattr(Patient, "Sex")
    descriptor = None
    for klass in Patient.__mro__:
        if "Sex" in klass.__dict__:
            descriptor = klass.__dict__["Sex"]
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



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "Amount" in params, "Missing parameter 'Amount'"

def test_bill_has_PatientName():
    assert hasattr(Bill, "PatientName")
    descriptor = None
    for klass in Bill.__mro__:
        if "PatientName" in klass.__dict__:
            descriptor = klass.__dict__["PatientName"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_Amount():
    assert hasattr(Bill, "Amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "DepartmentID" in params, "Missing parameter 'DepartmentID'"
    assert "DoctorID" in params, "Missing parameter 'DoctorID'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "PhoneNo" in params, "Missing parameter 'PhoneNo'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"

def test_doctor_has_DepartmentID():
    assert hasattr(Doctor, "DepartmentID")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DepartmentID" in klass.__dict__:
            descriptor = klass.__dict__["DepartmentID"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DoctorID():
    assert hasattr(Doctor, "DoctorID")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DoctorID" in klass.__dict__:
            descriptor = klass.__dict__["DoctorID"]
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

def test_doctor_has_attribute():
    assert hasattr(Doctor, "attribute")
    descriptor = None
    for klass in Doctor.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_PhoneNo():
    assert hasattr(Doctor, "PhoneNo")
    descriptor = None
    for klass in Doctor.__mro__:
        if "PhoneNo" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNo"]
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

def test_doctor_has_Specialization():
    assert hasattr(Doctor, "Specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
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
Nurse_strategy = st.builds(
    Nurse,
    ID=
        st.integers(),
    Name=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    TelephoneNo=
        safe_text,
    RoomNo=
        st.integers(),
    PatientID=
        st.integers(),
    Age=
        st.integers(),
    Sex=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    PatientName=
        safe_text,
    Amount=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    DepartmentID=
        st.integers(),
    DoctorID=
        st.integers(),
    Address=
        safe_text,
    attribute=
        safe_text,
    PhoneNo=
        safe_text,
    Name=
        safe_text,
    Specialization=
        safe_text
)

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)



@given(instance=Nurse_strategy)
def test_nurse_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Nurse_strategy)
def test_nurse_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_TelephoneNo_setter(instance):
    original = instance.TelephoneNo
    instance.TelephoneNo = original
    assert instance.TelephoneNo == original



@given(instance=Patient_strategy)
def test_patient_RoomNo_setter(instance):
    original = instance.RoomNo
    instance.RoomNo = original
    assert instance.RoomNo == original



@given(instance=Patient_strategy)
def test_patient_PatientID_setter(instance):
    original = instance.PatientID
    instance.PatientID = original
    assert instance.PatientID == original



@given(instance=Patient_strategy)
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_patient_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



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

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original



@given(instance=Bill_strategy)
def test_bill_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_DepartmentID_setter(instance):
    original = instance.DepartmentID
    instance.DepartmentID = original
    assert instance.DepartmentID == original



@given(instance=Doctor_strategy)
def test_doctor_DoctorID_setter(instance):
    original = instance.DoctorID
    instance.DoctorID = original
    assert instance.DoctorID == original



@given(instance=Doctor_strategy)
def test_doctor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Doctor_strategy)
def test_doctor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Doctor_strategy)
def test_doctor_PhoneNo_setter(instance):
    original = instance.PhoneNo
    instance.PhoneNo = original
    assert instance.PhoneNo == original



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original
