import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Room,
    Bill,
    Receptionist,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "RoomType" in params, "Missing parameter 'RoomType'"
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"

def test_room_has_RoomType():
    assert hasattr(Room, "RoomType")
    descriptor = None
    for klass in Room.__mro__:
        if "RoomType" in klass.__dict__:
            descriptor = klass.__dict__["RoomType"]
            break
    assert isinstance(descriptor, property)

def test_room_has_RoomNo():
    assert hasattr(Room, "RoomNo")
    descriptor = None
    for klass in Room.__mro__:
        if "RoomNo" in klass.__dict__:
            descriptor = klass.__dict__["RoomNo"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Patient_Id" in params, "Missing parameter 'Patient_Id'"
    assert "BillNo" in params, "Missing parameter 'BillNo'"

def test_bill_has_Amount():
    assert hasattr(Bill, "Amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_Patient_Id():
    assert hasattr(Bill, "Patient_Id")
    descriptor = None
    for klass in Bill.__mro__:
        if "Patient_Id" in klass.__dict__:
            descriptor = klass.__dict__["Patient_Id"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_BillNo():
    assert hasattr(Bill, "BillNo")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillNo" in klass.__dict__:
            descriptor = klass.__dict__["BillNo"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_receptionist_has_Id():
    assert hasattr(Receptionist, "Id")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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

def test_receptionist_has_Email():
    assert hasattr(Receptionist, "Email")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "WardNo" in params, "Missing parameter 'WardNo'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "PhNo_" in params, "Missing parameter 'PhNo_'"

def test_patient_has_Address():
    assert hasattr(Patient, "Address")
    descriptor = None
    for klass in Patient.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
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

def test_patient_has_WardNo():
    assert hasattr(Patient, "WardNo")
    descriptor = None
    for klass in Patient.__mro__:
        if "WardNo" in klass.__dict__:
            descriptor = klass.__dict__["WardNo"]
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

def test_patient_has_Id():
    assert hasattr(Patient, "Id")
    descriptor = None
    for klass in Patient.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PhNo_():
    assert hasattr(Patient, "PhNo_")
    descriptor = None
    for klass in Patient.__mro__:
        if "PhNo_" in klass.__dict__:
            descriptor = klass.__dict__["PhNo_"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "DocId_" in params, "Missing parameter 'DocId_'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Department" in params, "Missing parameter 'Department'"

def test_doctor_has_Email():
    assert hasattr(Doctor, "Email")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DocId_():
    assert hasattr(Doctor, "DocId_")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DocId_" in klass.__dict__:
            descriptor = klass.__dict__["DocId_"]
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

def test_doctor_has_Address():
    assert hasattr(Doctor, "Address")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
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
Room_strategy = st.builds(
    Room,
    RoomType=
        safe_text,
    RoomNo=
        st.integers()
)
Bill_strategy = st.builds(
    Bill,
    Amount=
        safe_text,
    Patient_Id=
        st.integers(),
    BillNo=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    Id=
        st.integers(),
    Name=
        safe_text,
    Email=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    Address=
        safe_text,
    Age=
        st.integers(),
    WardNo=
        st.integers(),
    Name=
        safe_text,
    Id=
        st.integers(),
    PhNo_=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    Email=
        safe_text,
    DocId_=
        st.integers(),
    Name=
        safe_text,
    Address=
        safe_text,
    Department=
        safe_text
)

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_RoomType_setter(instance):
    original = instance.RoomType
    instance.RoomType = original
    assert instance.RoomType == original



@given(instance=Room_strategy)
def test_room_RoomNo_setter(instance):
    original = instance.RoomNo
    instance.RoomNo = original
    assert instance.RoomNo == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Bill_strategy)
def test_bill_Patient_Id_setter(instance):
    original = instance.Patient_Id
    instance.Patient_Id = original
    assert instance.Patient_Id == original



@given(instance=Bill_strategy)
def test_bill_BillNo_setter(instance):
    original = instance.BillNo
    instance.BillNo = original
    assert instance.BillNo == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Receptionist_strategy)
def test_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Receptionist_strategy)
def test_receptionist_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_patient_WardNo_setter(instance):
    original = instance.WardNo
    instance.WardNo = original
    assert instance.WardNo == original



@given(instance=Patient_strategy)
def test_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_strategy)
def test_patient_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Patient_strategy)
def test_patient_PhNo__setter(instance):
    original = instance.PhNo_
    instance.PhNo_ = original
    assert instance.PhNo_ == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Doctor_strategy)
def test_doctor_DocId__setter(instance):
    original = instance.DocId_
    instance.DocId_ = original
    assert instance.DocId_ == original



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Doctor_strategy)
def test_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original
