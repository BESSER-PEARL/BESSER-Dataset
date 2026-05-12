import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Receiptionist,
    Room,
    patient,
    Doctor,
    Nurse,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_receiptionist_is_not_abstract():
    assert not inspect.isabstract(Receiptionist)


def test_receiptionist_constructor_exists():
    assert callable(Receiptionist.__init__)


def test_receiptionist_constructor_args():
    sig = inspect.signature(Receiptionist.__init__)
    params = list(sig.parameters.keys())



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "Room_Rent" in params, "Missing parameter 'Room_Rent'"
    assert "Room_TYPE" in params, "Missing parameter 'Room_TYPE'"
    assert "Room_NO" in params, "Missing parameter 'Room_NO'"

def test_room_has_Room_Rent():
    assert hasattr(Room, "Room_Rent")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_Rent" in klass.__dict__:
            descriptor = klass.__dict__["Room_Rent"]
            break
    assert isinstance(descriptor, property)

def test_room_has_Room_TYPE():
    assert hasattr(Room, "Room_TYPE")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_TYPE" in klass.__dict__:
            descriptor = klass.__dict__["Room_TYPE"]
            break
    assert isinstance(descriptor, property)

def test_room_has_Room_NO():
    assert hasattr(Room, "Room_NO")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_NO" in klass.__dict__:
            descriptor = klass.__dict__["Room_NO"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(patient)


def test_patient_constructor_exists():
    assert callable(patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(patient.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Patient_Address" in params, "Missing parameter 'Patient_Address'"
    assert "Patient_ID" in params, "Missing parameter 'Patient_ID'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "Patient_Name" in params, "Missing parameter 'Patient_Name'"
    assert "Patient_Contact_NO" in params, "Missing parameter 'Patient_Contact_NO'"

def test_patient_has_Status():
    assert hasattr(patient, "Status")
    descriptor = None
    for klass in patient.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Patient_Address():
    assert hasattr(patient, "Patient_Address")
    descriptor = None
    for klass in patient.__mro__:
        if "Patient_Address" in klass.__dict__:
            descriptor = klass.__dict__["Patient_Address"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Patient_ID():
    assert hasattr(patient, "Patient_ID")
    descriptor = None
    for klass in patient.__mro__:
        if "Patient_ID" in klass.__dict__:
            descriptor = klass.__dict__["Patient_ID"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Sex():
    assert hasattr(patient, "Sex")
    descriptor = None
    for klass in patient.__mro__:
        if "Sex" in klass.__dict__:
            descriptor = klass.__dict__["Sex"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_DOB():
    assert hasattr(patient, "DOB")
    descriptor = None
    for klass in patient.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Patient_Name():
    assert hasattr(patient, "Patient_Name")
    descriptor = None
    for klass in patient.__mro__:
        if "Patient_Name" in klass.__dict__:
            descriptor = klass.__dict__["Patient_Name"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Patient_Contact_NO():
    assert hasattr(patient, "Patient_Contact_NO")
    descriptor = None
    for klass in patient.__mro__:
        if "Patient_Contact_NO" in klass.__dict__:
            descriptor = klass.__dict__["Patient_Contact_NO"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Emp_ID" in params, "Missing parameter 'Emp_ID'"
    assert "Joindate" in params, "Missing parameter 'Joindate'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Contact_NO" in params, "Missing parameter 'Contact_NO'"
    assert "Designation" in params, "Missing parameter 'Designation'"
    assert "Salary" in params, "Missing parameter 'Salary'"

def test_employee_has_Address():
    assert hasattr(Employee, "Address")
    descriptor = None
    for klass in Employee.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_ID():
    assert hasattr(Employee, "Emp_ID")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_ID" in klass.__dict__:
            descriptor = klass.__dict__["Emp_ID"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Joindate():
    assert hasattr(Employee, "Joindate")
    descriptor = None
    for klass in Employee.__mro__:
        if "Joindate" in klass.__dict__:
            descriptor = klass.__dict__["Joindate"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Name():
    assert hasattr(Employee, "Emp_Name")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Name" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Name"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Contact_NO():
    assert hasattr(Employee, "Contact_NO")
    descriptor = None
    for klass in Employee.__mro__:
        if "Contact_NO" in klass.__dict__:
            descriptor = klass.__dict__["Contact_NO"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Designation():
    assert hasattr(Employee, "Designation")
    descriptor = None
    for klass in Employee.__mro__:
        if "Designation" in klass.__dict__:
            descriptor = klass.__dict__["Designation"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Salary():
    assert hasattr(Employee, "Salary")
    descriptor = None
    for klass in Employee.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
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
Receiptionist_strategy = st.builds(
    Receiptionist,
)
Room_strategy = st.builds(
    Room,
    Room_Rent=
        safe_text,
    Room_TYPE=
        safe_text,
    Room_NO=
        st.integers()
)
patient_strategy = st.builds(
    patient,
    Status=
        safe_text,
    Patient_Address=
        safe_text,
    Patient_ID=
        st.integers(),
    Sex=
        safe_text,
    DOB=
        safe_text,
    Patient_Name=
        safe_text,
    Patient_Contact_NO=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
)
Nurse_strategy = st.builds(
    Nurse,
)
Employee_strategy = st.builds(
    Employee,
    Address=
        safe_text,
    Emp_ID=
        st.integers(),
    Joindate=
        safe_text,
    Emp_Name=
        safe_text,
    Contact_NO=
        st.integers(),
    Designation=
        safe_text,
    Salary=
        safe_text
)

@given(instance=Receiptionist_strategy)
@settings(max_examples=50)
def test_receiptionist_instantiation(instance):
    assert isinstance(instance, Receiptionist)

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_Room_Rent_setter(instance):
    original = instance.Room_Rent
    instance.Room_Rent = original
    assert instance.Room_Rent == original



@given(instance=Room_strategy)
def test_room_Room_TYPE_setter(instance):
    original = instance.Room_TYPE
    instance.Room_TYPE = original
    assert instance.Room_TYPE == original



@given(instance=Room_strategy)
def test_room_Room_NO_setter(instance):
    original = instance.Room_NO
    instance.Room_NO = original
    assert instance.Room_NO == original

@given(instance=patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, patient)



@given(instance=patient_strategy)
def test_patient_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=patient_strategy)
def test_patient_Patient_Address_setter(instance):
    original = instance.Patient_Address
    instance.Patient_Address = original
    assert instance.Patient_Address == original



@given(instance=patient_strategy)
def test_patient_Patient_ID_setter(instance):
    original = instance.Patient_ID
    instance.Patient_ID = original
    assert instance.Patient_ID == original



@given(instance=patient_strategy)
def test_patient_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



@given(instance=patient_strategy)
def test_patient_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=patient_strategy)
def test_patient_Patient_Name_setter(instance):
    original = instance.Patient_Name
    instance.Patient_Name = original
    assert instance.Patient_Name == original



@given(instance=patient_strategy)
def test_patient_Patient_Contact_NO_setter(instance):
    original = instance.Patient_Contact_NO
    instance.Patient_Contact_NO = original
    assert instance.Patient_Contact_NO == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Employee_strategy)
def test_employee_Emp_ID_setter(instance):
    original = instance.Emp_ID
    instance.Emp_ID = original
    assert instance.Emp_ID == original



@given(instance=Employee_strategy)
def test_employee_Joindate_setter(instance):
    original = instance.Joindate
    instance.Joindate = original
    assert instance.Joindate == original



@given(instance=Employee_strategy)
def test_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_employee_Contact_NO_setter(instance):
    original = instance.Contact_NO
    instance.Contact_NO = original
    assert instance.Contact_NO == original



@given(instance=Employee_strategy)
def test_employee_Designation_setter(instance):
    original = instance.Designation
    instance.Designation = original
    assert instance.Designation == original



@given(instance=Employee_strategy)
def test_employee_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original
