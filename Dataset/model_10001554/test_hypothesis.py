import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    system_Component,
    Float,
    Dept,
    Rooms,
    Bill,
    ReceptionList,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_system_component_is_not_abstract():
    assert not inspect.isabstract(system_Component)


def test_system_component_constructor_exists():
    assert callable(system_Component.__init__)


def test_system_component_constructor_args():
    sig = inspect.signature(system_Component.__init__)
    params = list(sig.parameters.keys())



def test_float_is_not_abstract():
    assert not inspect.isabstract(Float)


def test_float_constructor_exists():
    assert callable(Float.__init__)


def test_float_constructor_args():
    sig = inspect.signature(Float.__init__)
    params = list(sig.parameters.keys())



def test_dept_is_not_abstract():
    assert not inspect.isabstract(Dept)


def test_dept_constructor_exists():
    assert callable(Dept.__init__)


def test_dept_constructor_args():
    sig = inspect.signature(Dept.__init__)
    params = list(sig.parameters.keys())
    assert "DocId" in params, "Missing parameter 'DocId'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_dept_has_DocId():
    assert hasattr(Dept, "DocId")
    descriptor = None
    for klass in Dept.__mro__:
        if "DocId" in klass.__dict__:
            descriptor = klass.__dict__["DocId"]
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

def test_dept_has_Id():
    assert hasattr(Dept, "Id")
    descriptor = None
    for klass in Dept.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "BillId" in params, "Missing parameter 'BillId'"

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

def test_bill_has_BillId():
    assert hasattr(Bill, "BillId")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillId" in klass.__dict__:
            descriptor = klass.__dict__["BillId"]
            break
    assert isinstance(descriptor, property)



def test_receptionlist_is_not_abstract():
    assert not inspect.isabstract(ReceptionList)


def test_receptionlist_constructor_exists():
    assert callable(ReceptionList.__init__)


def test_receptionlist_constructor_args():
    sig = inspect.signature(ReceptionList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "RepId" in params, "Missing parameter 'RepId'"

def test_receptionlist_has_name():
    assert hasattr(ReceptionList, "name")
    descriptor = None
    for klass in ReceptionList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_receptionlist_has_RepId():
    assert hasattr(ReceptionList, "RepId")
    descriptor = None
    for klass in ReceptionList.__mro__:
        if "RepId" in klass.__dict__:
            descriptor = klass.__dict__["RepId"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "PhoneNo" in params, "Missing parameter 'PhoneNo'"
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "PatientId" in params, "Missing parameter 'PatientId'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "Age" in params, "Missing parameter 'Age'"

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

def test_patient_has_PatientName():
    assert hasattr(Patient, "PatientName")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatientName" in klass.__dict__:
            descriptor = klass.__dict__["PatientName"]
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



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "docId" in params, "Missing parameter 'docId'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Location" in params, "Missing parameter 'Location'"
    assert "Dept" in params, "Missing parameter 'Dept'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "PhoneNo" in params, "Missing parameter 'PhoneNo'"

def test_doctor_has_docId():
    assert hasattr(Doctor, "docId")
    descriptor = None
    for klass in Doctor.__mro__:
        if "docId" in klass.__dict__:
            descriptor = klass.__dict__["docId"]
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

def test_doctor_has_Location():
    assert hasattr(Doctor, "Location")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
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

def test_doctor_has_Name():
    assert hasattr(Doctor, "Name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
system_Component_strategy = st.builds(
    system_Component,
)
Float_strategy = st.builds(
    Float,
)
Dept_strategy = st.builds(
    Dept,
    DocId=
        st.integers(),
    Name=
        safe_text,
    Id=
        st.integers()
)
Rooms_strategy = st.builds(
    Rooms,
    RoomNo=
        st.integers(),
    Location=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    PatientName=
        safe_text,
    Amount=
        st.none(),
    BillId=
        st.integers()
)
ReceptionList_strategy = st.builds(
    ReceptionList,
    name=
        safe_text,
    RepId=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    Sex=
        safe_text,
    PhoneNo=
        st.integers(),
    PatientName=
        safe_text,
    PatientId=
        st.integers(),
    Address=
        safe_text,
    RoomNo=
        st.integers(),
    Age=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    docId=
        st.integers(),
    Specialization=
        safe_text,
    Location=
        safe_text,
    Dept=
        safe_text,
    Name=
        safe_text,
    PhoneNo=
        st.integers()
)

@given(instance=system_Component_strategy)
@settings(max_examples=50)
def test_system_component_instantiation(instance):
    assert isinstance(instance, system_Component)

@given(instance=Float_strategy)
@settings(max_examples=50)
def test_float_instantiation(instance):
    assert isinstance(instance, Float)

@given(instance=Dept_strategy)
@settings(max_examples=50)
def test_dept_instantiation(instance):
    assert isinstance(instance, Dept)



@given(instance=Dept_strategy)
def test_dept_DocId_setter(instance):
    original = instance.DocId
    instance.DocId = original
    assert instance.DocId == original



@given(instance=Dept_strategy)
def test_dept_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Dept_strategy)
def test_dept_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

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



@given(instance=Bill_strategy)
def test_bill_BillId_setter(instance):
    original = instance.BillId
    instance.BillId = original
    assert instance.BillId == original

@given(instance=ReceptionList_strategy)
@settings(max_examples=50)
def test_receptionlist_instantiation(instance):
    assert isinstance(instance, ReceptionList)



@given(instance=ReceptionList_strategy)
def test_receptionlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ReceptionList_strategy)
def test_receptionlist_RepId_setter(instance):
    original = instance.RepId
    instance.RepId = original
    assert instance.RepId == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



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
def test_patient_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original



@given(instance=Patient_strategy)
def test_patient_PatientId_setter(instance):
    original = instance.PatientId
    instance.PatientId = original
    assert instance.PatientId == original



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

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_docId_setter(instance):
    original = instance.docId
    instance.docId = original
    assert instance.docId == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_doctor_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original



@given(instance=Doctor_strategy)
def test_doctor_Dept_setter(instance):
    original = instance.Dept
    instance.Dept = original
    assert instance.Dept == original



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_PhoneNo_setter(instance):
    original = instance.PhoneNo
    instance.PhoneNo = original
    assert instance.PhoneNo == original
