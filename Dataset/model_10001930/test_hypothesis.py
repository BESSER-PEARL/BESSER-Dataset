import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ff,
    e,
    Dept,
    Bill,
    Rooms,
    Receptionist,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ff_is_not_abstract():
    assert not inspect.isabstract(ff)


def test_ff_constructor_exists():
    assert callable(ff.__init__)


def test_ff_constructor_args():
    sig = inspect.signature(ff.__init__)
    params = list(sig.parameters.keys())
    assert "fd" in params, "Missing parameter 'fd'"

def test_ff_has_fd():
    assert hasattr(ff, "fd")
    descriptor = None
    for klass in ff.__mro__:
        if "fd" in klass.__dict__:
            descriptor = klass.__dict__["fd"]
            break
    assert isinstance(descriptor, property)



def test_e_is_not_abstract():
    assert not inspect.isabstract(e)


def test_e_constructor_exists():
    assert callable(e.__init__)


def test_e_constructor_args():
    sig = inspect.signature(e.__init__)
    params = list(sig.parameters.keys())
    assert "ee" in params, "Missing parameter 'ee'"

def test_e_has_ee():
    assert hasattr(e, "ee")
    descriptor = None
    for klass in e.__mro__:
        if "ee" in klass.__dict__:
            descriptor = klass.__dict__["ee"]
            break
    assert isinstance(descriptor, property)



def test_dept_is_not_abstract():
    assert not inspect.isabstract(Dept)


def test_dept_constructor_exists():
    assert callable(Dept.__init__)


def test_dept_constructor_args():
    sig = inspect.signature(Dept.__init__)
    params = list(sig.parameters.keys())
    assert "Docid" in params, "Missing parameter 'Docid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "DeptName" in params, "Missing parameter 'DeptName'"

def test_dept_has_Docid():
    assert hasattr(Dept, "Docid")
    descriptor = None
    for klass in Dept.__mro__:
        if "Docid" in klass.__dict__:
            descriptor = klass.__dict__["Docid"]
            break
    assert isinstance(descriptor, property)

def test_dept_has_id():
    assert hasattr(Dept, "id")
    descriptor = None
    for klass in Dept.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dept_has_DeptName():
    assert hasattr(Dept, "DeptName")
    descriptor = None
    for klass in Dept.__mro__:
        if "DeptName" in klass.__dict__:
            descriptor = klass.__dict__["DeptName"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "BillNo" in params, "Missing parameter 'BillNo'"
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "Amt" in params, "Missing parameter 'Amt'"

def test_bill_has_BillNo():
    assert hasattr(Bill, "BillNo")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillNo" in klass.__dict__:
            descriptor = klass.__dict__["BillNo"]
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

def test_bill_has_Amt():
    assert hasattr(Bill, "Amt")
    descriptor = None
    for klass in Bill.__mro__:
        if "Amt" in klass.__dict__:
            descriptor = klass.__dict__["Amt"]
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
    assert "Location" in params, "Missing parameter 'Location'"

def test_rooms_has_RoomNo():
    assert hasattr(Rooms, "RoomNo")
    descriptor = None
    for klass in Rooms.__mro__:
        if "RoomNo" in klass.__dict__:
            descriptor = klass.__dict__["RoomNo"]
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
    assert "RecName" in params, "Missing parameter 'RecName'"
    assert "Receptionid" in params, "Missing parameter 'Receptionid'"

def test_receptionist_has_RecName():
    assert hasattr(Receptionist, "RecName")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "RecName" in klass.__dict__:
            descriptor = klass.__dict__["RecName"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_Receptionid():
    assert hasattr(Receptionist, "Receptionid")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Receptionid" in klass.__dict__:
            descriptor = klass.__dict__["Receptionid"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "PhoneNo" in params, "Missing parameter 'PhoneNo'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Patientid" in params, "Missing parameter 'Patientid'"
    assert "PatientName" in params, "Missing parameter 'PatientName'"

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

def test_patient_has_Sex():
    assert hasattr(Patient, "Sex")
    descriptor = None
    for klass in Patient.__mro__:
        if "Sex" in klass.__dict__:
            descriptor = klass.__dict__["Sex"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PhoneNo():
    assert hasattr(Patient, "PhoneNo")
    descriptor = None
    for klass in Patient.__mro__:
        if "PhoneNo" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNo"]
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

def test_patient_has_Patientid():
    assert hasattr(Patient, "Patientid")
    descriptor = None
    for klass in Patient.__mro__:
        if "Patientid" in klass.__dict__:
            descriptor = klass.__dict__["Patientid"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PatientName():
    assert hasattr(Patient, "PatientName")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatientName" in klass.__dict__:
            descriptor = klass.__dict__["PatientName"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Phoneno" in params, "Missing parameter 'Phoneno'"
    assert "Location" in params, "Missing parameter 'Location'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Docid" in params, "Missing parameter 'Docid'"
    assert "Dept" in params, "Missing parameter 'Dept'"
    assert "DocName" in params, "Missing parameter 'DocName'"

def test_doctor_has_Phoneno():
    assert hasattr(Doctor, "Phoneno")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Phoneno" in klass.__dict__:
            descriptor = klass.__dict__["Phoneno"]
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

def test_doctor_has_Specialization():
    assert hasattr(Doctor, "Specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Docid():
    assert hasattr(Doctor, "Docid")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Docid" in klass.__dict__:
            descriptor = klass.__dict__["Docid"]
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

def test_doctor_has_DocName():
    assert hasattr(Doctor, "DocName")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DocName" in klass.__dict__:
            descriptor = klass.__dict__["DocName"]
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
ff_strategy = st.builds(
    ff,
    fd=
        st.integers()
)
e_strategy = st.builds(
    e,
    ee=
        st.integers()
)
Dept_strategy = st.builds(
    Dept,
    Docid=
        st.integers(),
    id=
        st.integers(),
    DeptName=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    BillNo=
        safe_text,
    PatientName=
        safe_text,
    Amt=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    RoomNo=
        st.integers(),
    Location=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    RecName=
        safe_text,
    Receptionid=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    RoomNo=
        st.integers(),
    Age=
        st.integers(),
    Sex=
        safe_text,
    PhoneNo=
        st.integers(),
    Address=
        safe_text,
    Patientid=
        st.integers(),
    PatientName=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    Phoneno=
        safe_text,
    Location=
        safe_text,
    Specialization=
        safe_text,
    Docid=
        st.integers(),
    Dept=
        safe_text,
    DocName=
        safe_text
)

@given(instance=ff_strategy)
@settings(max_examples=50)
def test_ff_instantiation(instance):
    assert isinstance(instance, ff)



@given(instance=ff_strategy)
def test_ff_fd_setter(instance):
    original = instance.fd
    instance.fd = original
    assert instance.fd == original

@given(instance=e_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, e)



@given(instance=e_strategy)
def test_e_ee_setter(instance):
    original = instance.ee
    instance.ee = original
    assert instance.ee == original

@given(instance=Dept_strategy)
@settings(max_examples=50)
def test_dept_instantiation(instance):
    assert isinstance(instance, Dept)



@given(instance=Dept_strategy)
def test_dept_Docid_setter(instance):
    original = instance.Docid
    instance.Docid = original
    assert instance.Docid == original



@given(instance=Dept_strategy)
def test_dept_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Dept_strategy)
def test_dept_DeptName_setter(instance):
    original = instance.DeptName
    instance.DeptName = original
    assert instance.DeptName == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_BillNo_setter(instance):
    original = instance.BillNo
    instance.BillNo = original
    assert instance.BillNo == original



@given(instance=Bill_strategy)
def test_bill_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original



@given(instance=Bill_strategy)
def test_bill_Amt_setter(instance):
    original = instance.Amt
    instance.Amt = original
    assert instance.Amt == original

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
def test_rooms_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_RecName_setter(instance):
    original = instance.RecName
    instance.RecName = original
    assert instance.RecName == original



@given(instance=Receptionist_strategy)
def test_receptionist_Receptionid_setter(instance):
    original = instance.Receptionid
    instance.Receptionid = original
    assert instance.Receptionid == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



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
def test_patient_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



@given(instance=Patient_strategy)
def test_patient_PhoneNo_setter(instance):
    original = instance.PhoneNo
    instance.PhoneNo = original
    assert instance.PhoneNo == original



@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_patient_Patientid_setter(instance):
    original = instance.Patientid
    instance.Patientid = original
    assert instance.Patientid == original



@given(instance=Patient_strategy)
def test_patient_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Phoneno_setter(instance):
    original = instance.Phoneno
    instance.Phoneno = original
    assert instance.Phoneno == original



@given(instance=Doctor_strategy)
def test_doctor_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_doctor_Docid_setter(instance):
    original = instance.Docid
    instance.Docid = original
    assert instance.Docid == original



@given(instance=Doctor_strategy)
def test_doctor_Dept_setter(instance):
    original = instance.Dept
    instance.Dept = original
    assert instance.Dept == original



@given(instance=Doctor_strategy)
def test_doctor_DocName_setter(instance):
    original = instance.DocName
    instance.DocName = original
    assert instance.DocName == original
