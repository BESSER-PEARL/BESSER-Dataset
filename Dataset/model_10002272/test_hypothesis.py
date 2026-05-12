import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hospital,
    Nurse,
    Doctor,
    Manager,
    Employee,
    outPatient,
    inPatient,
    Patient,
    Person,
    Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_hospital_has_address():
    assert hasattr(Hospital, "address")
    descriptor = None
    for klass in Hospital.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_name():
    assert hasattr(Hospital, "name")
    descriptor = None
    for klass in Hospital.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"

def test_nurse_has_department():
    assert hasattr(Nurse, "department")
    descriptor = None
    for klass in Nurse.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"

def test_doctor_has_department():
    assert hasattr(Doctor, "department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "employeeList" in params, "Missing parameter 'employeeList'"
    assert "allowance" in params, "Missing parameter 'allowance'"

def test_manager_has_employeeList():
    assert hasattr(Manager, "employeeList")
    descriptor = None
    for klass in Manager.__mro__:
        if "employeeList" in klass.__dict__:
            descriptor = klass.__dict__["employeeList"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_allowance():
    assert hasattr(Manager, "allowance")
    descriptor = None
    for klass in Manager.__mro__:
        if "allowance" in klass.__dict__:
            descriptor = klass.__dict__["allowance"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "employeeID" in params, "Missing parameter 'employeeID'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_employee_has_employeeID():
    assert hasattr(Employee, "employeeID")
    descriptor = None
    for klass in Employee.__mro__:
        if "employeeID" in klass.__dict__:
            descriptor = klass.__dict__["employeeID"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_salary():
    assert hasattr(Employee, "salary")
    descriptor = None
    for klass in Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_outpatient_is_not_abstract():
    assert not inspect.isabstract(outPatient)


def test_outpatient_constructor_exists():
    assert callable(outPatient.__init__)


def test_outpatient_constructor_args():
    sig = inspect.signature(outPatient.__init__)
    params = list(sig.parameters.keys())
    assert "roomNumber" in params, "Missing parameter 'roomNumber'"
    assert "inDate" in params, "Missing parameter 'inDate'"
    assert "outDate" in params, "Missing parameter 'outDate'"

def test_outpatient_has_roomNumber():
    assert hasattr(outPatient, "roomNumber")
    descriptor = None
    for klass in outPatient.__mro__:
        if "roomNumber" in klass.__dict__:
            descriptor = klass.__dict__["roomNumber"]
            break
    assert isinstance(descriptor, property)

def test_outpatient_has_inDate():
    assert hasattr(outPatient, "inDate")
    descriptor = None
    for klass in outPatient.__mro__:
        if "inDate" in klass.__dict__:
            descriptor = klass.__dict__["inDate"]
            break
    assert isinstance(descriptor, property)

def test_outpatient_has_outDate():
    assert hasattr(outPatient, "outDate")
    descriptor = None
    for klass in outPatient.__mro__:
        if "outDate" in klass.__dict__:
            descriptor = klass.__dict__["outDate"]
            break
    assert isinstance(descriptor, property)



def test_inpatient_is_not_abstract():
    assert not inspect.isabstract(inPatient)


def test_inpatient_constructor_exists():
    assert callable(inPatient.__init__)


def test_inpatient_constructor_args():
    sig = inspect.signature(inPatient.__init__)
    params = list(sig.parameters.keys())
    assert "outDate" in params, "Missing parameter 'outDate'"
    assert "inDate" in params, "Missing parameter 'inDate'"
    assert "rooomNumber" in params, "Missing parameter 'rooomNumber'"

def test_inpatient_has_outDate():
    assert hasattr(inPatient, "outDate")
    descriptor = None
    for klass in inPatient.__mro__:
        if "outDate" in klass.__dict__:
            descriptor = klass.__dict__["outDate"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_inDate():
    assert hasattr(inPatient, "inDate")
    descriptor = None
    for klass in inPatient.__mro__:
        if "inDate" in klass.__dict__:
            descriptor = klass.__dict__["inDate"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_rooomNumber():
    assert hasattr(inPatient, "rooomNumber")
    descriptor = None
    for klass in inPatient.__mro__:
        if "rooomNumber" in klass.__dict__:
            descriptor = klass.__dict__["rooomNumber"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "patientID" in params, "Missing parameter 'patientID'"
    assert "treatment" in params, "Missing parameter 'treatment'"

def test_patient_has_patientID():
    assert hasattr(Patient, "patientID")
    descriptor = None
    for klass in Patient.__mro__:
        if "patientID" in klass.__dict__:
            descriptor = klass.__dict__["patientID"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_treatment():
    assert hasattr(Patient, "treatment")
    descriptor = None
    for klass in Patient.__mro__:
        if "treatment" in klass.__dict__:
            descriptor = klass.__dict__["treatment"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "title" in params, "Missing parameter 'title'"

def test_person_has_gender():
    assert hasattr(Person, "gender")
    descriptor = None
    for klass in Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_person_has_address():
    assert hasattr(Person, "address")
    descriptor = None
    for klass in Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_person_has_phoneNumber():
    assert hasattr(Person, "phoneNumber")
    descriptor = None
    for klass in Person.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_person_has_name():
    assert hasattr(Person, "name")
    descriptor = None
    for klass in Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_title():
    assert hasattr(Person, "title")
    descriptor = None
    for klass in Person.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "departmentName" in params, "Missing parameter 'departmentName'"
    assert "departmentID" in params, "Missing parameter 'departmentID'"
    assert "nurseList" in params, "Missing parameter 'nurseList'"
    assert "doctorList" in params, "Missing parameter 'doctorList'"

def test_department_has_departmentName():
    assert hasattr(Department, "departmentName")
    descriptor = None
    for klass in Department.__mro__:
        if "departmentName" in klass.__dict__:
            descriptor = klass.__dict__["departmentName"]
            break
    assert isinstance(descriptor, property)

def test_department_has_departmentID():
    assert hasattr(Department, "departmentID")
    descriptor = None
    for klass in Department.__mro__:
        if "departmentID" in klass.__dict__:
            descriptor = klass.__dict__["departmentID"]
            break
    assert isinstance(descriptor, property)

def test_department_has_nurseList():
    assert hasattr(Department, "nurseList")
    descriptor = None
    for klass in Department.__mro__:
        if "nurseList" in klass.__dict__:
            descriptor = klass.__dict__["nurseList"]
            break
    assert isinstance(descriptor, property)

def test_department_has_doctorList():
    assert hasattr(Department, "doctorList")
    descriptor = None
    for klass in Department.__mro__:
        if "doctorList" in klass.__dict__:
            descriptor = klass.__dict__["doctorList"]
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
Hospital_strategy = st.builds(
    Hospital,
    address=
        safe_text,
    name=
        safe_text
)
Nurse_strategy = st.builds(
    Nurse,
    department=
        st.none()
)
Doctor_strategy = st.builds(
    Doctor,
    department=
        st.none()
)
Manager_strategy = st.builds(
    Manager,
    employeeList=
        safe_text,
    allowance=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    employeeID=
        safe_text,
    salary=
        safe_text
)
outPatient_strategy = st.builds(
    outPatient,
    roomNumber=
        safe_text,
    inDate=
        safe_text,
    outDate=
        safe_text
)
inPatient_strategy = st.builds(
    inPatient,
    outDate=
        safe_text,
    inDate=
        safe_text,
    rooomNumber=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    patientID=
        safe_text,
    treatment=
        safe_text
)
Person_strategy = st.builds(
    Person,
    gender=
        safe_text,
    address=
        safe_text,
    phoneNumber=
        safe_text,
    name=
        safe_text,
    title=
        safe_text
)
Department_strategy = st.builds(
    Department,
    departmentName=
        safe_text,
    departmentID=
        safe_text,
    nurseList=
        safe_text,
    doctorList=
        safe_text
)

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Hospital_strategy)
def test_hospital_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)



@given(instance=Nurse_strategy)
def test_nurse_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_employeeList_setter(instance):
    original = instance.employeeList
    instance.employeeList = original
    assert instance.employeeList == original



@given(instance=Manager_strategy)
def test_manager_allowance_setter(instance):
    original = instance.allowance
    instance.allowance = original
    assert instance.allowance == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_employeeID_setter(instance):
    original = instance.employeeID
    instance.employeeID = original
    assert instance.employeeID == original



@given(instance=Employee_strategy)
def test_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=outPatient_strategy)
@settings(max_examples=50)
def test_outpatient_instantiation(instance):
    assert isinstance(instance, outPatient)



@given(instance=outPatient_strategy)
def test_outpatient_roomNumber_setter(instance):
    original = instance.roomNumber
    instance.roomNumber = original
    assert instance.roomNumber == original



@given(instance=outPatient_strategy)
def test_outpatient_inDate_setter(instance):
    original = instance.inDate
    instance.inDate = original
    assert instance.inDate == original



@given(instance=outPatient_strategy)
def test_outpatient_outDate_setter(instance):
    original = instance.outDate
    instance.outDate = original
    assert instance.outDate == original

@given(instance=inPatient_strategy)
@settings(max_examples=50)
def test_inpatient_instantiation(instance):
    assert isinstance(instance, inPatient)



@given(instance=inPatient_strategy)
def test_inpatient_outDate_setter(instance):
    original = instance.outDate
    instance.outDate = original
    assert instance.outDate == original



@given(instance=inPatient_strategy)
def test_inpatient_inDate_setter(instance):
    original = instance.inDate
    instance.inDate = original
    assert instance.inDate == original



@given(instance=inPatient_strategy)
def test_inpatient_rooomNumber_setter(instance):
    original = instance.rooomNumber
    instance.rooomNumber = original
    assert instance.rooomNumber == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_patientID_setter(instance):
    original = instance.patientID
    instance.patientID = original
    assert instance.patientID == original



@given(instance=Patient_strategy)
def test_patient_treatment_setter(instance):
    original = instance.treatment
    instance.treatment = original
    assert instance.treatment == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Person_strategy)
def test_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_person_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_person_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_departmentName_setter(instance):
    original = instance.departmentName
    instance.departmentName = original
    assert instance.departmentName == original



@given(instance=Department_strategy)
def test_department_departmentID_setter(instance):
    original = instance.departmentID
    instance.departmentID = original
    assert instance.departmentID == original



@given(instance=Department_strategy)
def test_department_nurseList_setter(instance):
    original = instance.nurseList
    instance.nurseList = original
    assert instance.nurseList == original



@given(instance=Department_strategy)
def test_department_doctorList_setter(instance):
    original = instance.doctorList
    instance.doctorList = original
    assert instance.doctorList == original
