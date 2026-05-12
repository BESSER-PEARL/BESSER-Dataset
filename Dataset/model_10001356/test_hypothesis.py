import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    char_Interface,
    Staff,
    Rooms,
    Department,
    Bill,
    Doctor,
    Patient,
    Receptionist,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_char_interface_is_not_abstract():
    assert not inspect.isabstract(char_Interface)


def test_char_interface_constructor_exists():
    assert callable(char_Interface.__init__)


def test_char_interface_constructor_args():
    sig = inspect.signature(char_Interface.__init__)
    params = list(sig.parameters.keys())



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_staff_has_Type():
    assert hasattr(Staff, "Type")
    descriptor = None
    for klass in Staff.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_ID():
    assert hasattr(Staff, "ID")
    descriptor = None
    for klass in Staff.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Name():
    assert hasattr(Staff, "Name")
    descriptor = None
    for klass in Staff.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "Room_No" in params, "Missing parameter 'Room_No'"
    assert "Location" in params, "Missing parameter 'Location'"

def test_rooms_has_Room_No():
    assert hasattr(Rooms, "Room_No")
    descriptor = None
    for klass in Rooms.__mro__:
        if "Room_No" in klass.__dict__:
            descriptor = klass.__dict__["Room_No"]
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



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Doctor_ID" in params, "Missing parameter 'Doctor_ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_department_has_ID():
    assert hasattr(Department, "ID")
    descriptor = None
    for klass in Department.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_department_has_Doctor_ID():
    assert hasattr(Department, "Doctor_ID")
    descriptor = None
    for klass in Department.__mro__:
        if "Doctor_ID" in klass.__dict__:
            descriptor = klass.__dict__["Doctor_ID"]
            break
    assert isinstance(descriptor, property)

def test_department_has_Name():
    assert hasattr(Department, "Name")
    descriptor = None
    for klass in Department.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "Patient_Name" in params, "Missing parameter 'Patient_Name'"
    assert "Bill_No" in params, "Missing parameter 'Bill_No'"
    assert "Amount" in params, "Missing parameter 'Amount'"

def test_bill_has_Patient_Name():
    assert hasattr(Bill, "Patient_Name")
    descriptor = None
    for klass in Bill.__mro__:
        if "Patient_Name" in klass.__dict__:
            descriptor = klass.__dict__["Patient_Name"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_Bill_No():
    assert hasattr(Bill, "Bill_No")
    descriptor = None
    for klass in Bill.__mro__:
        if "Bill_No" in klass.__dict__:
            descriptor = klass.__dict__["Bill_No"]
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
    assert "PhNo" in params, "Missing parameter 'PhNo'"
    assert "DocID" in params, "Missing parameter 'DocID'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Department" in params, "Missing parameter 'Department'"

def test_doctor_has_PhNo():
    assert hasattr(Doctor, "PhNo")
    descriptor = None
    for klass in Doctor.__mro__:
        if "PhNo" in klass.__dict__:
            descriptor = klass.__dict__["PhNo"]
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

def test_doctor_has_Department():
    assert hasattr(Doctor, "Department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Pid" in params, "Missing parameter 'Pid'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "RoomNo_" in params, "Missing parameter 'RoomNo_'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "TelNO" in params, "Missing parameter 'TelNO'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_patient_has_Pid():
    assert hasattr(Patient, "Pid")
    descriptor = None
    for klass in Patient.__mro__:
        if "Pid" in klass.__dict__:
            descriptor = klass.__dict__["Pid"]
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

def test_patient_has_TelNO():
    assert hasattr(Patient, "TelNO")
    descriptor = None
    for klass in Patient.__mro__:
        if "TelNO" in klass.__dict__:
            descriptor = klass.__dict__["TelNO"]
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



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Rname" in params, "Missing parameter 'Rname'"
    assert "Rid" in params, "Missing parameter 'Rid'"

def test_receptionist_has_Rname():
    assert hasattr(Receptionist, "Rname")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Rname" in klass.__dict__:
            descriptor = klass.__dict__["Rname"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_Rid():
    assert hasattr(Receptionist, "Rid")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Rid" in klass.__dict__:
            descriptor = klass.__dict__["Rid"]
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
char_Interface_strategy = st.builds(
    char_Interface,
)
Staff_strategy = st.builds(
    Staff,
    Type=
        safe_text,
    ID=
        st.integers(),
    Name=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    Room_No=
        st.integers(),
    Location=
        safe_text
)
Department_strategy = st.builds(
    Department,
    ID=
        st.integers(),
    Doctor_ID=
        st.integers(),
    Name=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    Patient_Name=
        safe_text,
    Bill_No=
        safe_text,
    Amount=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    PhNo=
        st.integers(),
    DocID=
        st.integers(),
    Address=
        safe_text,
    Name=
        safe_text,
    Specialization=
        safe_text,
    Department=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    Pid=
        st.integers(),
    Age=
        st.integers(),
    Address=
        safe_text,
    RoomNo_=
        st.integers(),
    Sex=
        st.integers(),
    TelNO=
        st.integers(),
    Name=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    Rname=
        safe_text,
    Rid=
        safe_text
)

@given(instance=char_Interface_strategy)
@settings(max_examples=50)
def test_char_interface_instantiation(instance):
    assert isinstance(instance, char_Interface)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Staff_strategy)
def test_staff_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Staff_strategy)
def test_staff_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_Room_No_setter(instance):
    original = instance.Room_No
    instance.Room_No = original
    assert instance.Room_No == original



@given(instance=Rooms_strategy)
def test_rooms_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Department_strategy)
def test_department_Doctor_ID_setter(instance):
    original = instance.Doctor_ID
    instance.Doctor_ID = original
    assert instance.Doctor_ID == original



@given(instance=Department_strategy)
def test_department_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_Patient_Name_setter(instance):
    original = instance.Patient_Name
    instance.Patient_Name = original
    assert instance.Patient_Name == original



@given(instance=Bill_strategy)
def test_bill_Bill_No_setter(instance):
    original = instance.Bill_No
    instance.Bill_No = original
    assert instance.Bill_No == original



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
def test_doctor_PhNo_setter(instance):
    original = instance.PhNo
    instance.PhNo = original
    assert instance.PhNo == original



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
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Pid_setter(instance):
    original = instance.Pid
    instance.Pid = original
    assert instance.Pid == original



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
def test_patient_TelNO_setter(instance):
    original = instance.TelNO
    instance.TelNO = original
    assert instance.TelNO == original



@given(instance=Patient_strategy)
def test_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_Rname_setter(instance):
    original = instance.Rname
    instance.Rname = original
    assert instance.Rname == original



@given(instance=Receptionist_strategy)
def test_receptionist_Rid_setter(instance):
    original = instance.Rid
    instance.Rid = original
    assert instance.Rid == original
