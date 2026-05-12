import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Staff,
    Patient,
    Bill,
    Dept,
    Doctor,
    Rooms,
    Receptionist,
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
    assert "Staff_name" in params, "Missing parameter 'Staff_name'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_staff_has_Staff_name():
    assert hasattr(Staff, "Staff_name")
    descriptor = None
    for klass in Staff.__mro__:
        if "Staff_name" in klass.__dict__:
            descriptor = klass.__dict__["Staff_name"]
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

def test_staff_has_Id():
    assert hasattr(Staff, "Id")
    descriptor = None
    for klass in Staff.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "RoomNo_" in params, "Missing parameter 'RoomNo_'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "Patient_id" in params, "Missing parameter 'Patient_id'"
    assert "PhoneNo_" in params, "Missing parameter 'PhoneNo_'"

def test_patient_has_Name():
    assert hasattr(Patient, "Name")
    descriptor = None
    for klass in Patient.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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

def test_patient_has_Address():
    assert hasattr(Patient, "Address")
    descriptor = None
    for klass in Patient.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_RoomNo_():
    assert hasattr(Patient, "RoomNo_")
    descriptor = None
    for klass in Patient.__mro__:
        if "RoomNo_" in klass.__dict__:
            descriptor = klass.__dict__["RoomNo_"]
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

def test_patient_has_Patient_id():
    assert hasattr(Patient, "Patient_id")
    descriptor = None
    for klass in Patient.__mro__:
        if "Patient_id" in klass.__dict__:
            descriptor = klass.__dict__["Patient_id"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PhoneNo_():
    assert hasattr(Patient, "PhoneNo_")
    descriptor = None
    for klass in Patient.__mro__:
        if "PhoneNo_" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNo_"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "BillNo_" in params, "Missing parameter 'BillNo_'"
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "Amount" in params, "Missing parameter 'Amount'"

def test_bill_has_BillNo_():
    assert hasattr(Bill, "BillNo_")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillNo_" in klass.__dict__:
            descriptor = klass.__dict__["BillNo_"]
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

def test_bill_has_Amount():
    assert hasattr(Bill, "Amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)



def test_dept_is_not_abstract():
    assert not inspect.isabstract(Dept)


def test_dept_constructor_exists():
    assert callable(Dept.__init__)


def test_dept_constructor_args():
    sig = inspect.signature(Dept.__init__)
    params = list(sig.parameters.keys())
    assert "Doc_id" in params, "Missing parameter 'Doc_id'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_dept_has_Doc_id():
    assert hasattr(Dept, "Doc_id")
    descriptor = None
    for klass in Dept.__mro__:
        if "Doc_id" in klass.__dict__:
            descriptor = klass.__dict__["Doc_id"]
            break
    assert isinstance(descriptor, property)

def test_dept_has_Id():
    assert hasattr(Dept, "Id")
    descriptor = None
    for klass in Dept.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_dept_has_Name():
    assert hasattr(Dept, "Name")
    descriptor = None
    for klass in Dept.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "PhoneNo_" in params, "Missing parameter 'PhoneNo_'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "DocName" in params, "Missing parameter 'DocName'"
    assert "Location" in params, "Missing parameter 'Location'"
    assert "Doct_id" in params, "Missing parameter 'Doct_id'"
    assert "Dept" in params, "Missing parameter 'Dept'"

def test_doctor_has_PhoneNo_():
    assert hasattr(Doctor, "PhoneNo_")
    descriptor = None
    for klass in Doctor.__mro__:
        if "PhoneNo_" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNo_"]
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

def test_doctor_has_DocName():
    assert hasattr(Doctor, "DocName")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DocName" in klass.__dict__:
            descriptor = klass.__dict__["DocName"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Location():
    assert hasattr(Doctor, "Location")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Doct_id():
    assert hasattr(Doctor, "Doct_id")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Doct_id" in klass.__dict__:
            descriptor = klass.__dict__["Doct_id"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Dept():
    assert hasattr(Doctor, "Dept")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Dept" in klass.__dict__:
            descriptor = klass.__dict__["Dept"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "Roomno_" in params, "Missing parameter 'Roomno_'"
    assert "Location" in params, "Missing parameter 'Location'"

def test_rooms_has_Roomno_():
    assert hasattr(Rooms, "Roomno_")
    descriptor = None
    for klass in Rooms.__mro__:
        if "Roomno_" in klass.__dict__:
            descriptor = klass.__dict__["Roomno_"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_Location():
    assert hasattr(Rooms, "Location")
    descriptor = None
    for klass in Rooms.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Receptional_id" in params, "Missing parameter 'Receptional_id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_receptionist_has_Receptional_id():
    assert hasattr(Receptionist, "Receptional_id")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Receptional_id" in klass.__dict__:
            descriptor = klass.__dict__["Receptional_id"]
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
    Staff_name=
        safe_text,
    Type=
        safe_text,
    Id=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    Name=
        safe_text,
    Age=
        st.integers(),
    Address=
        safe_text,
    RoomNo_=
        st.integers(),
    Sex=
        safe_text,
    Patient_id=
        st.integers(),
    PhoneNo_=
        st.integers()
)
Bill_strategy = st.builds(
    Bill,
    BillNo_=
        safe_text,
    PatientName=
        safe_text,
    Amount=
        st.integers()
)
Dept_strategy = st.builds(
    Dept,
    Doc_id=
        st.integers(),
    Id=
        st.integers(),
    Name=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    PhoneNo_=
        st.integers(),
    Specialization=
        safe_text,
    DocName=
        safe_text,
    Location=
        safe_text,
    Doct_id=
        st.integers(),
    Dept=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    Roomno_=
        st.integers(),
    Location=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    Receptional_id=
        st.integers(),
    Name=
        safe_text
)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Staff_name_setter(instance):
    original = instance.Staff_name
    instance.Staff_name = original
    assert instance.Staff_name == original



@given(instance=Staff_strategy)
def test_staff_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Staff_strategy)
def test_staff_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

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
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_patient_RoomNo__setter(instance):
    original = instance.RoomNo_
    instance.RoomNo_ = original
    assert instance.RoomNo_ == original



@given(instance=Patient_strategy)
def test_patient_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



@given(instance=Patient_strategy)
def test_patient_Patient_id_setter(instance):
    original = instance.Patient_id
    instance.Patient_id = original
    assert instance.Patient_id == original



@given(instance=Patient_strategy)
def test_patient_PhoneNo__setter(instance):
    original = instance.PhoneNo_
    instance.PhoneNo_ = original
    assert instance.PhoneNo_ == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_BillNo__setter(instance):
    original = instance.BillNo_
    instance.BillNo_ = original
    assert instance.BillNo_ == original



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

@given(instance=Dept_strategy)
@settings(max_examples=50)
def test_dept_instantiation(instance):
    assert isinstance(instance, Dept)



@given(instance=Dept_strategy)
def test_dept_Doc_id_setter(instance):
    original = instance.Doc_id
    instance.Doc_id = original
    assert instance.Doc_id == original



@given(instance=Dept_strategy)
def test_dept_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Dept_strategy)
def test_dept_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_PhoneNo__setter(instance):
    original = instance.PhoneNo_
    instance.PhoneNo_ = original
    assert instance.PhoneNo_ == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_doctor_DocName_setter(instance):
    original = instance.DocName
    instance.DocName = original
    assert instance.DocName == original



@given(instance=Doctor_strategy)
def test_doctor_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original



@given(instance=Doctor_strategy)
def test_doctor_Doct_id_setter(instance):
    original = instance.Doct_id
    instance.Doct_id = original
    assert instance.Doct_id == original



@given(instance=Doctor_strategy)
def test_doctor_Dept_setter(instance):
    original = instance.Dept
    instance.Dept = original
    assert instance.Dept == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_Roomno__setter(instance):
    original = instance.Roomno_
    instance.Roomno_ = original
    assert instance.Roomno_ == original



@given(instance=Rooms_strategy)
def test_rooms_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_Receptional_id_setter(instance):
    original = instance.Receptional_id
    instance.Receptional_id = original
    assert instance.Receptional_id == original



@given(instance=Receptionist_strategy)
def test_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
