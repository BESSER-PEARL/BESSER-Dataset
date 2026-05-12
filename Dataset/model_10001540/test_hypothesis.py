import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Techinal_Staff,
    Administrative_Staff,
    Operation_Staff,
    Staff,
    Patient,
    Hospital,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_techinal_staff_is_not_abstract():
    assert not inspect.isabstract(Techinal_Staff)


def test_techinal_staff_constructor_exists():
    assert callable(Techinal_Staff.__init__)


def test_techinal_staff_constructor_args():
    sig = inspect.signature(Techinal_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Technician" in params, "Missing parameter 'Technician'"
    assert "Technologist" in params, "Missing parameter 'Technologist'"

def test_techinal_staff_has_Technician():
    assert hasattr(Techinal_Staff, "Technician")
    descriptor = None
    for klass in Techinal_Staff.__mro__:
        if "Technician" in klass.__dict__:
            descriptor = klass.__dict__["Technician"]
            break
    assert isinstance(descriptor, property)

def test_techinal_staff_has_Technologist():
    assert hasattr(Techinal_Staff, "Technologist")
    descriptor = None
    for klass in Techinal_Staff.__mro__:
        if "Technologist" in klass.__dict__:
            descriptor = klass.__dict__["Technologist"]
            break
    assert isinstance(descriptor, property)



def test_administrative_staff_is_not_abstract():
    assert not inspect.isabstract(Administrative_Staff)


def test_administrative_staff_constructor_exists():
    assert callable(Administrative_Staff.__init__)


def test_administrative_staff_constructor_args():
    sig = inspect.signature(Administrative_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "FrontDeskStaffName" in params, "Missing parameter 'FrontDeskStaffName'"
    assert "ReceptionistName" in params, "Missing parameter 'ReceptionistName'"

def test_administrative_staff_has_FrontDeskStaffName():
    assert hasattr(Administrative_Staff, "FrontDeskStaffName")
    descriptor = None
    for klass in Administrative_Staff.__mro__:
        if "FrontDeskStaffName" in klass.__dict__:
            descriptor = klass.__dict__["FrontDeskStaffName"]
            break
    assert isinstance(descriptor, property)

def test_administrative_staff_has_ReceptionistName():
    assert hasattr(Administrative_Staff, "ReceptionistName")
    descriptor = None
    for klass in Administrative_Staff.__mro__:
        if "ReceptionistName" in klass.__dict__:
            descriptor = klass.__dict__["ReceptionistName"]
            break
    assert isinstance(descriptor, property)



def test_operation_staff_is_not_abstract():
    assert not inspect.isabstract(Operation_Staff)


def test_operation_staff_constructor_exists():
    assert callable(Operation_Staff.__init__)


def test_operation_staff_constructor_args():
    sig = inspect.signature(Operation_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "DoctorSpeciality" in params, "Missing parameter 'DoctorSpeciality'"
    assert "DoctorLocation" in params, "Missing parameter 'DoctorLocation'"
    assert "NurseName" in params, "Missing parameter 'NurseName'"

def test_operation_staff_has_DoctorSpeciality():
    assert hasattr(Operation_Staff, "DoctorSpeciality")
    descriptor = None
    for klass in Operation_Staff.__mro__:
        if "DoctorSpeciality" in klass.__dict__:
            descriptor = klass.__dict__["DoctorSpeciality"]
            break
    assert isinstance(descriptor, property)

def test_operation_staff_has_DoctorLocation():
    assert hasattr(Operation_Staff, "DoctorLocation")
    descriptor = None
    for klass in Operation_Staff.__mro__:
        if "DoctorLocation" in klass.__dict__:
            descriptor = klass.__dict__["DoctorLocation"]
            break
    assert isinstance(descriptor, property)

def test_operation_staff_has_NurseName():
    assert hasattr(Operation_Staff, "NurseName")
    descriptor = None
    for klass in Operation_Staff.__mro__:
        if "NurseName" in klass.__dict__:
            descriptor = klass.__dict__["NurseName"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Joined" in params, "Missing parameter 'Joined'"
    assert "Certification" in params, "Missing parameter 'Certification'"
    assert "Languages" in params, "Missing parameter 'Languages'"
    assert "Education" in params, "Missing parameter 'Education'"

def test_staff_has_Joined():
    assert hasattr(Staff, "Joined")
    descriptor = None
    for klass in Staff.__mro__:
        if "Joined" in klass.__dict__:
            descriptor = klass.__dict__["Joined"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Certification():
    assert hasattr(Staff, "Certification")
    descriptor = None
    for klass in Staff.__mro__:
        if "Certification" in klass.__dict__:
            descriptor = klass.__dict__["Certification"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Languages():
    assert hasattr(Staff, "Languages")
    descriptor = None
    for klass in Staff.__mro__:
        if "Languages" in klass.__dict__:
            descriptor = klass.__dict__["Languages"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Education():
    assert hasattr(Staff, "Education")
    descriptor = None
    for klass in Staff.__mro__:
        if "Education" in klass.__dict__:
            descriptor = klass.__dict__["Education"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Birthdate" in params, "Missing parameter 'Birthdate'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"
    assert "PatientId" in params, "Missing parameter 'PatientId'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "DateOfEntry" in params, "Missing parameter 'DateOfEntry'"

def test_patient_has_Birthdate():
    assert hasattr(Patient, "Birthdate")
    descriptor = None
    for klass in Patient.__mro__:
        if "Birthdate" in klass.__dict__:
            descriptor = klass.__dict__["Birthdate"]
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

def test_patient_has_Sickness():
    assert hasattr(Patient, "Sickness")
    descriptor = None
    for klass in Patient.__mro__:
        if "Sickness" in klass.__dict__:
            descriptor = klass.__dict__["Sickness"]
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

def test_patient_has_DateOfEntry():
    assert hasattr(Patient, "DateOfEntry")
    descriptor = None
    for klass in Patient.__mro__:
        if "DateOfEntry" in klass.__dict__:
            descriptor = klass.__dict__["DateOfEntry"]
            break
    assert isinstance(descriptor, property)



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "HospitalId" in params, "Missing parameter 'HospitalId'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_hospital_has_Phone():
    assert hasattr(Hospital, "Phone")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_HospitalId():
    assert hasattr(Hospital, "HospitalId")
    descriptor = None
    for klass in Hospital.__mro__:
        if "HospitalId" in klass.__dict__:
            descriptor = klass.__dict__["HospitalId"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_Address():
    assert hasattr(Hospital, "Address")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_Name():
    assert hasattr(Hospital, "Name")
    descriptor = None
    for klass in Hospital.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "PersonHospitalId" in params, "Missing parameter 'PersonHospitalId'"
    assert "BirthDate" in params, "Missing parameter 'BirthDate'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "MiddleName" in params, "Missing parameter 'MiddleName'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "PersonPatientId" in params, "Missing parameter 'PersonPatientId'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_person_has_PersonHospitalId():
    assert hasattr(Person, "PersonHospitalId")
    descriptor = None
    for klass in Person.__mro__:
        if "PersonHospitalId" in klass.__dict__:
            descriptor = klass.__dict__["PersonHospitalId"]
            break
    assert isinstance(descriptor, property)

def test_person_has_BirthDate():
    assert hasattr(Person, "BirthDate")
    descriptor = None
    for klass in Person.__mro__:
        if "BirthDate" in klass.__dict__:
            descriptor = klass.__dict__["BirthDate"]
            break
    assert isinstance(descriptor, property)

def test_person_has_FirstName():
    assert hasattr(Person, "FirstName")
    descriptor = None
    for klass in Person.__mro__:
        if "FirstName" in klass.__dict__:
            descriptor = klass.__dict__["FirstName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Title():
    assert hasattr(Person, "Title")
    descriptor = None
    for klass in Person.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_person_has_MiddleName():
    assert hasattr(Person, "MiddleName")
    descriptor = None
    for klass in Person.__mro__:
        if "MiddleName" in klass.__dict__:
            descriptor = klass.__dict__["MiddleName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_LastName():
    assert hasattr(Person, "LastName")
    descriptor = None
    for klass in Person.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Gender():
    assert hasattr(Person, "Gender")
    descriptor = None
    for klass in Person.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_person_has_PersonPatientId():
    assert hasattr(Person, "PersonPatientId")
    descriptor = None
    for klass in Person.__mro__:
        if "PersonPatientId" in klass.__dict__:
            descriptor = klass.__dict__["PersonPatientId"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Phone():
    assert hasattr(Person, "Phone")
    descriptor = None
    for klass in Person.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Address():
    assert hasattr(Person, "Address")
    descriptor = None
    for klass in Person.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
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
Techinal_Staff_strategy = st.builds(
    Techinal_Staff,
    Technician=
        safe_text,
    Technologist=
        safe_text
)
Administrative_Staff_strategy = st.builds(
    Administrative_Staff,
    FrontDeskStaffName=
        safe_text,
    ReceptionistName=
        safe_text
)
Operation_Staff_strategy = st.builds(
    Operation_Staff,
    DoctorSpeciality=
        safe_text,
    DoctorLocation=
        safe_text,
    NurseName=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    Joined=
        safe_text,
    Certification=
        safe_text,
    Languages=
        safe_text,
    Education=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    Birthdate=
        safe_text,
    Gender=
        safe_text,
    Sickness=
        safe_text,
    PatientId=
        st.integers(),
    Name=
        safe_text,
    Age=
        st.integers(),
    DateOfEntry=
        safe_text
)
Hospital_strategy = st.builds(
    Hospital,
    Phone=
        st.integers(),
    HospitalId=
        st.integers(),
    Address=
        safe_text,
    Name=
        safe_text
)
Person_strategy = st.builds(
    Person,
    PersonHospitalId=
        st.integers(),
    BirthDate=
        safe_text,
    FirstName=
        safe_text,
    Title=
        safe_text,
    MiddleName=
        safe_text,
    LastName=
        safe_text,
    Gender=
        safe_text,
    PersonPatientId=
        st.integers(),
    Phone=
        st.integers(),
    Address=
        safe_text
)

@given(instance=Techinal_Staff_strategy)
@settings(max_examples=50)
def test_techinal_staff_instantiation(instance):
    assert isinstance(instance, Techinal_Staff)



@given(instance=Techinal_Staff_strategy)
def test_techinal_staff_Technician_setter(instance):
    original = instance.Technician
    instance.Technician = original
    assert instance.Technician == original



@given(instance=Techinal_Staff_strategy)
def test_techinal_staff_Technologist_setter(instance):
    original = instance.Technologist
    instance.Technologist = original
    assert instance.Technologist == original

@given(instance=Administrative_Staff_strategy)
@settings(max_examples=50)
def test_administrative_staff_instantiation(instance):
    assert isinstance(instance, Administrative_Staff)



@given(instance=Administrative_Staff_strategy)
def test_administrative_staff_FrontDeskStaffName_setter(instance):
    original = instance.FrontDeskStaffName
    instance.FrontDeskStaffName = original
    assert instance.FrontDeskStaffName == original



@given(instance=Administrative_Staff_strategy)
def test_administrative_staff_ReceptionistName_setter(instance):
    original = instance.ReceptionistName
    instance.ReceptionistName = original
    assert instance.ReceptionistName == original

@given(instance=Operation_Staff_strategy)
@settings(max_examples=50)
def test_operation_staff_instantiation(instance):
    assert isinstance(instance, Operation_Staff)



@given(instance=Operation_Staff_strategy)
def test_operation_staff_DoctorSpeciality_setter(instance):
    original = instance.DoctorSpeciality
    instance.DoctorSpeciality = original
    assert instance.DoctorSpeciality == original



@given(instance=Operation_Staff_strategy)
def test_operation_staff_DoctorLocation_setter(instance):
    original = instance.DoctorLocation
    instance.DoctorLocation = original
    assert instance.DoctorLocation == original



@given(instance=Operation_Staff_strategy)
def test_operation_staff_NurseName_setter(instance):
    original = instance.NurseName
    instance.NurseName = original
    assert instance.NurseName == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Joined_setter(instance):
    original = instance.Joined
    instance.Joined = original
    assert instance.Joined == original



@given(instance=Staff_strategy)
def test_staff_Certification_setter(instance):
    original = instance.Certification
    instance.Certification = original
    assert instance.Certification == original



@given(instance=Staff_strategy)
def test_staff_Languages_setter(instance):
    original = instance.Languages
    instance.Languages = original
    assert instance.Languages == original



@given(instance=Staff_strategy)
def test_staff_Education_setter(instance):
    original = instance.Education
    instance.Education = original
    assert instance.Education == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Birthdate_setter(instance):
    original = instance.Birthdate
    instance.Birthdate = original
    assert instance.Birthdate == original



@given(instance=Patient_strategy)
def test_patient_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Patient_strategy)
def test_patient_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original



@given(instance=Patient_strategy)
def test_patient_PatientId_setter(instance):
    original = instance.PatientId
    instance.PatientId = original
    assert instance.PatientId == original



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
def test_patient_DateOfEntry_setter(instance):
    original = instance.DateOfEntry
    instance.DateOfEntry = original
    assert instance.DateOfEntry == original

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Hospital_strategy)
def test_hospital_HospitalId_setter(instance):
    original = instance.HospitalId
    instance.HospitalId = original
    assert instance.HospitalId == original



@given(instance=Hospital_strategy)
def test_hospital_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Hospital_strategy)
def test_hospital_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_PersonHospitalId_setter(instance):
    original = instance.PersonHospitalId
    instance.PersonHospitalId = original
    assert instance.PersonHospitalId == original



@given(instance=Person_strategy)
def test_person_BirthDate_setter(instance):
    original = instance.BirthDate
    instance.BirthDate = original
    assert instance.BirthDate == original



@given(instance=Person_strategy)
def test_person_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=Person_strategy)
def test_person_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Person_strategy)
def test_person_MiddleName_setter(instance):
    original = instance.MiddleName
    instance.MiddleName = original
    assert instance.MiddleName == original



@given(instance=Person_strategy)
def test_person_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=Person_strategy)
def test_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Person_strategy)
def test_person_PersonPatientId_setter(instance):
    original = instance.PersonPatientId
    instance.PersonPatientId = original
    assert instance.PersonPatientId == original



@given(instance=Person_strategy)
def test_person_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Person_strategy)
def test_person_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original
