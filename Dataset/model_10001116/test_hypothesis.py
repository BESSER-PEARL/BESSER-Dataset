import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Staff,
    Rooms,
    Bill,
    Deparment,
    Receptionsit,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_staff_has_Name():
    assert hasattr(Staff, "Name")
    descriptor = None
    for klass in Staff.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Id():
    assert hasattr(Staff, "Id")
    descriptor = None
    for klass in Staff.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Type():
    assert hasattr(Staff, "Type")
    descriptor = None
    for klass in Staff.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "WardNo" in params, "Missing parameter 'WardNo'"

def test_rooms_has_RoomNo():
    assert hasattr(Rooms, "RoomNo")
    descriptor = None
    for klass in Rooms.__mro__:
        if "RoomNo" in klass.__dict__:
            descriptor = klass.__dict__["RoomNo"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_WardNo():
    assert hasattr(Rooms, "WardNo")
    descriptor = None
    for klass in Rooms.__mro__:
        if "WardNo" in klass.__dict__:
            descriptor = klass.__dict__["WardNo"]
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
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "BillNo" in params, "Missing parameter 'BillNo'"

def test_bill_has_Amount():
    assert hasattr(Bill, "Amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_PatientName():
    assert hasattr(Bill, "PatientName")
    descriptor = None
    for klass in Bill.__mro__:
        if "PatientName" in klass.__dict__:
            descriptor = klass.__dict__["PatientName"]
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



def test_deparment_is_not_abstract():
    assert not inspect.isabstract(Deparment)


def test_deparment_constructor_exists():
    assert callable(Deparment.__init__)


def test_deparment_constructor_args():
    sig = inspect.signature(Deparment.__init__)
    params = list(sig.parameters.keys())
    assert "PhNo" in params, "Missing parameter 'PhNo'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_deparment_has_PhNo():
    assert hasattr(Deparment, "PhNo")
    descriptor = None
    for klass in Deparment.__mro__:
        if "PhNo" in klass.__dict__:
            descriptor = klass.__dict__["PhNo"]
            break
    assert isinstance(descriptor, property)

def test_deparment_has_Name():
    assert hasattr(Deparment, "Name")
    descriptor = None
    for klass in Deparment.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_deparment_has_Id():
    assert hasattr(Deparment, "Id")
    descriptor = None
    for klass in Deparment.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_receptionsit_is_not_abstract():
    assert not inspect.isabstract(Receptionsit)


def test_receptionsit_constructor_exists():
    assert callable(Receptionsit.__init__)


def test_receptionsit_constructor_args():
    sig = inspect.signature(Receptionsit.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_receptionsit_has_Id():
    assert hasattr(Receptionsit, "Id")
    descriptor = None
    for klass in Receptionsit.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_receptionsit_has_Name():
    assert hasattr(Receptionsit, "Name")
    descriptor = None
    for klass in Receptionsit.__mro__:
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
    assert "Name" in params, "Missing parameter 'Name'"
    assert "PatientId" in params, "Missing parameter 'PatientId'"
    assert "age" in params, "Missing parameter 'age'"

def test_patient_has_Name():
    assert hasattr(Patient, "Name")
    descriptor = None
    for klass in Patient.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PatientId():
    assert hasattr(Patient, "PatientId")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatientId" in klass.__dict__:
            descriptor = klass.__dict__["PatientId"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_age():
    assert hasattr(Patient, "age")
    descriptor = None
    for klass in Patient.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "PhNo" in params, "Missing parameter 'PhNo'"
    assert "DocId" in params, "Missing parameter 'DocId'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"

def test_doctor_has_Name():
    assert hasattr(Doctor, "Name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_PhNo():
    assert hasattr(Doctor, "PhNo")
    descriptor = None
    for klass in Doctor.__mro__:
        if "PhNo" in klass.__dict__:
            descriptor = klass.__dict__["PhNo"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DocId():
    assert hasattr(Doctor, "DocId")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DocId" in klass.__dict__:
            descriptor = klass.__dict__["DocId"]
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
Staff_strategy = st.builds(
    Staff,
    Name=
        safe_text,
    Id=
        st.integers(),
    Type=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    RoomNo=
        st.integers(),
    WardNo=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    Amount=
        safe_text,
    PatientName=
        safe_text,
    BillNo=
        safe_text
)
Deparment_strategy = st.builds(
    Deparment,
    PhNo=
        st.integers(),
    Name=
        safe_text,
    Id=
        st.integers()
)
Receptionsit_strategy = st.builds(
    Receptionsit,
    Id=
        st.integers(),
    Name=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    Name=
        safe_text,
    PatientId=
        st.integers(),
    age=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    Name=
        safe_text,
    PhNo=
        st.integers(),
    DocId=
        st.integers(),
    Department=
        safe_text,
    Specialization=
        safe_text
)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Staff_strategy)
def test_staff_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Staff_strategy)
def test_staff_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_RoomNo_setter(instance):
    original = instance.RoomNo
    instance.RoomNo = original
    assert instance.RoomNo == original



@given(instance=Rooms_strategy)
def test_rooms_WardNo_setter(instance):
    original = instance.WardNo
    instance.WardNo = original
    assert instance.WardNo == original

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
def test_bill_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original



@given(instance=Bill_strategy)
def test_bill_BillNo_setter(instance):
    original = instance.BillNo
    instance.BillNo = original
    assert instance.BillNo == original

@given(instance=Deparment_strategy)
@settings(max_examples=50)
def test_deparment_instantiation(instance):
    assert isinstance(instance, Deparment)



@given(instance=Deparment_strategy)
def test_deparment_PhNo_setter(instance):
    original = instance.PhNo
    instance.PhNo = original
    assert instance.PhNo == original



@given(instance=Deparment_strategy)
def test_deparment_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Deparment_strategy)
def test_deparment_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Receptionsit_strategy)
@settings(max_examples=50)
def test_receptionsit_instantiation(instance):
    assert isinstance(instance, Receptionsit)



@given(instance=Receptionsit_strategy)
def test_receptionsit_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Receptionsit_strategy)
def test_receptionsit_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_strategy)
def test_patient_PatientId_setter(instance):
    original = instance.PatientId
    instance.PatientId = original
    assert instance.PatientId == original



@given(instance=Patient_strategy)
def test_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_PhNo_setter(instance):
    original = instance.PhNo
    instance.PhNo = original
    assert instance.PhNo == original



@given(instance=Doctor_strategy)
def test_doctor_DocId_setter(instance):
    original = instance.DocId
    instance.DocId = original
    assert instance.DocId == original



@given(instance=Doctor_strategy)
def test_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original
