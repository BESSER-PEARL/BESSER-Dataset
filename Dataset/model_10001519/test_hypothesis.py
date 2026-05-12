import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Receptionist,
    Bill,
    Department,
    Ward,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "BillNo" in params, "Missing parameter 'BillNo'"
    assert "patientName" in params, "Missing parameter 'patientName'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_bill_has_BillNo():
    assert hasattr(Bill, "BillNo")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillNo" in klass.__dict__:
            descriptor = klass.__dict__["BillNo"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_patientName():
    assert hasattr(Bill, "patientName")
    descriptor = None
    for klass in Bill.__mro__:
        if "patientName" in klass.__dict__:
            descriptor = klass.__dict__["patientName"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_amount():
    assert hasattr(Bill, "amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "DocID" in params, "Missing parameter 'DocID'"
    assert "deptID" in params, "Missing parameter 'deptID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_department_has_DocID():
    assert hasattr(Department, "DocID")
    descriptor = None
    for klass in Department.__mro__:
        if "DocID" in klass.__dict__:
            descriptor = klass.__dict__["DocID"]
            break
    assert isinstance(descriptor, property)

def test_department_has_deptID():
    assert hasattr(Department, "deptID")
    descriptor = None
    for klass in Department.__mro__:
        if "deptID" in klass.__dict__:
            descriptor = klass.__dict__["deptID"]
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



def test_ward_is_not_abstract():
    assert not inspect.isabstract(Ward)


def test_ward_constructor_exists():
    assert callable(Ward.__init__)


def test_ward_constructor_args():
    sig = inspect.signature(Ward.__init__)
    params = list(sig.parameters.keys())
    assert "Location" in params, "Missing parameter 'Location'"
    assert "wardNo" in params, "Missing parameter 'wardNo'"

def test_ward_has_Location():
    assert hasattr(Ward, "Location")
    descriptor = None
    for klass in Ward.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_wardNo():
    assert hasattr(Ward, "wardNo")
    descriptor = None
    for klass in Ward.__mro__:
        if "wardNo" in klass.__dict__:
            descriptor = klass.__dict__["wardNo"]
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
    assert "WardNo" in params, "Missing parameter 'WardNo'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "PatientID" in params, "Missing parameter 'PatientID'"

def test_patient_has_Name():
    assert hasattr(Patient, "Name")
    descriptor = None
    for klass in Patient.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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

def test_patient_has_Gender():
    assert hasattr(Patient, "Gender")
    descriptor = None
    for klass in Patient.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
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

def test_patient_has_PatientID():
    assert hasattr(Patient, "PatientID")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatientID" in klass.__dict__:
            descriptor = klass.__dict__["PatientID"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Department" in params, "Missing parameter 'Department'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "DocID" in params, "Missing parameter 'DocID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_doctor_has_Department():
    assert hasattr(Doctor, "Department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
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

def test_doctor_has_Specialization():
    assert hasattr(Doctor, "Specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_PhoneNumber():
    assert hasattr(Doctor, "PhoneNumber")
    descriptor = None
    for klass in Doctor.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
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

def test_doctor_has_Name():
    assert hasattr(Doctor, "Name")
    descriptor = None
    for klass in Doctor.__mro__:
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
Receptionist_strategy = st.builds(
    Receptionist,
)
Bill_strategy = st.builds(
    Bill,
    BillNo=
        st.integers(),
    patientName=
        safe_text,
    amount=
        st.integers()
)
Department_strategy = st.builds(
    Department,
    DocID=
        safe_text,
    deptID=
        safe_text,
    Name=
        safe_text
)
Ward_strategy = st.builds(
    Ward,
    Location=
        safe_text,
    wardNo=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    Name=
        safe_text,
    WardNo=
        st.integers(),
    Gender=
        safe_text,
    Age=
        safe_text,
    Address=
        safe_text,
    PatientID=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    Department=
        safe_text,
    Address=
        safe_text,
    Specialization=
        st.integers(),
    PhoneNumber=
        st.integers(),
    DocID=
        safe_text,
    Name=
        safe_text
)

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)

@given(instance=Bill_strategy)
def test_bill_BillNo_type(instance):
    assert isinstance(instance.BillNo, int)


@given(instance=Bill_strategy)
def test_bill_BillNo_setter(instance):
    original = instance.BillNo
    instance.BillNo = original
    assert instance.BillNo == original

@given(instance=Bill_strategy)
def test_bill_patientName_type(instance):
    assert isinstance(instance.patientName, str)


@given(instance=Bill_strategy)
def test_bill_patientName_setter(instance):
    original = instance.patientName
    instance.patientName = original
    assert instance.patientName == original

@given(instance=Bill_strategy)
def test_bill_amount_type(instance):
    assert isinstance(instance.amount, int)


@given(instance=Bill_strategy)
def test_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=Department_strategy)
def test_department_DocID_type(instance):
    assert isinstance(instance.DocID, str)


@given(instance=Department_strategy)
def test_department_DocID_setter(instance):
    original = instance.DocID
    instance.DocID = original
    assert instance.DocID == original

@given(instance=Department_strategy)
def test_department_deptID_type(instance):
    assert isinstance(instance.deptID, str)


@given(instance=Department_strategy)
def test_department_deptID_setter(instance):
    original = instance.deptID
    instance.deptID = original
    assert instance.deptID == original

@given(instance=Department_strategy)
def test_department_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Department_strategy)
def test_department_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Ward_strategy)
@settings(max_examples=50)
def test_ward_instantiation(instance):
    assert isinstance(instance, Ward)

@given(instance=Ward_strategy)
def test_ward_Location_type(instance):
    assert isinstance(instance.Location, str)


@given(instance=Ward_strategy)
def test_ward_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=Ward_strategy)
def test_ward_wardNo_type(instance):
    assert isinstance(instance.wardNo, int)


@given(instance=Ward_strategy)
def test_ward_wardNo_setter(instance):
    original = instance.wardNo
    instance.wardNo = original
    assert instance.wardNo == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)

@given(instance=Patient_strategy)
def test_patient_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Patient_strategy)
def test_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Patient_strategy)
def test_patient_WardNo_type(instance):
    assert isinstance(instance.WardNo, int)


@given(instance=Patient_strategy)
def test_patient_WardNo_setter(instance):
    original = instance.WardNo
    instance.WardNo = original
    assert instance.WardNo == original

@given(instance=Patient_strategy)
def test_patient_Gender_type(instance):
    assert isinstance(instance.Gender, str)


@given(instance=Patient_strategy)
def test_patient_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original

@given(instance=Patient_strategy)
def test_patient_Age_type(instance):
    assert isinstance(instance.Age, str)


@given(instance=Patient_strategy)
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=Patient_strategy)
def test_patient_Address_type(instance):
    assert isinstance(instance.Address, str)


@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Patient_strategy)
def test_patient_PatientID_type(instance):
    assert isinstance(instance.PatientID, int)


@given(instance=Patient_strategy)
def test_patient_PatientID_setter(instance):
    original = instance.PatientID
    instance.PatientID = original
    assert instance.PatientID == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)

@given(instance=Doctor_strategy)
def test_doctor_Department_type(instance):
    assert isinstance(instance.Department, str)


@given(instance=Doctor_strategy)
def test_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original

@given(instance=Doctor_strategy)
def test_doctor_Address_type(instance):
    assert isinstance(instance.Address, str)


@given(instance=Doctor_strategy)
def test_doctor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Doctor_strategy)
def test_doctor_Specialization_type(instance):
    assert isinstance(instance.Specialization, int)


@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original

@given(instance=Doctor_strategy)
def test_doctor_PhoneNumber_type(instance):
    assert isinstance(instance.PhoneNumber, int)


@given(instance=Doctor_strategy)
def test_doctor_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original

@given(instance=Doctor_strategy)
def test_doctor_DocID_type(instance):
    assert isinstance(instance.DocID, str)


@given(instance=Doctor_strategy)
def test_doctor_DocID_setter(instance):
    original = instance.DocID
    instance.DocID = original
    assert instance.DocID == original

@given(instance=Doctor_strategy)
def test_doctor_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
