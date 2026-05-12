import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HospitalSystem,
    SystemAdministrator,
    Doctor,
    Patient,
    Person,
    Staff,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hospitalsystem_is_not_abstract():
    assert not inspect.isabstract(HospitalSystem)


def test_hospitalsystem_constructor_exists():
    assert callable(HospitalSystem.__init__)


def test_hospitalsystem_constructor_args():
    sig = inspect.signature(HospitalSystem.__init__)
    params = list(sig.parameters.keys())
    assert "Doctors" in params, "Missing parameter 'Doctors'"
    assert "admin" in params, "Missing parameter 'admin'"
    assert "Patients" in params, "Missing parameter 'Patients'"

def test_hospitalsystem_has_Doctors():
    assert hasattr(HospitalSystem, "Doctors")
    descriptor = None
    for klass in HospitalSystem.__mro__:
        if "Doctors" in klass.__dict__:
            descriptor = klass.__dict__["Doctors"]
            break
    assert isinstance(descriptor, property)

def test_hospitalsystem_has_admin():
    assert hasattr(HospitalSystem, "admin")
    descriptor = None
    for klass in HospitalSystem.__mro__:
        if "admin" in klass.__dict__:
            descriptor = klass.__dict__["admin"]
            break
    assert isinstance(descriptor, property)

def test_hospitalsystem_has_Patients():
    assert hasattr(HospitalSystem, "Patients")
    descriptor = None
    for klass in HospitalSystem.__mro__:
        if "Patients" in klass.__dict__:
            descriptor = klass.__dict__["Patients"]
            break
    assert isinstance(descriptor, property)



def test_systemadministrator_is_not_abstract():
    assert not inspect.isabstract(SystemAdministrator)


def test_systemadministrator_constructor_exists():
    assert callable(SystemAdministrator.__init__)


def test_systemadministrator_constructor_args():
    sig = inspect.signature(SystemAdministrator.__init__)
    params = list(sig.parameters.keys())
    assert "Doctors" in params, "Missing parameter 'Doctors'"
    assert "Patients" in params, "Missing parameter 'Patients'"

def test_systemadministrator_has_Doctors():
    assert hasattr(SystemAdministrator, "Doctors")
    descriptor = None
    for klass in SystemAdministrator.__mro__:
        if "Doctors" in klass.__dict__:
            descriptor = klass.__dict__["Doctors"]
            break
    assert isinstance(descriptor, property)

def test_systemadministrator_has_Patients():
    assert hasattr(SystemAdministrator, "Patients")
    descriptor = None
    for klass in SystemAdministrator.__mro__:
        if "Patients" in klass.__dict__:
            descriptor = klass.__dict__["Patients"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Shedule" in params, "Missing parameter 'Shedule'"

def test_doctor_has_Specialization():
    assert hasattr(Doctor, "Specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Shedule():
    assert hasattr(Doctor, "Shedule")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Shedule" in klass.__dict__:
            descriptor = klass.__dict__["Shedule"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "DiseaseHistory" in params, "Missing parameter 'DiseaseHistory'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Prescriptions" in params, "Missing parameter 'Prescriptions'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phone" in params, "Missing parameter 'Phone'"

def test_patient_has_DiseaseHistory():
    assert hasattr(Patient, "DiseaseHistory")
    descriptor = None
    for klass in Patient.__mro__:
        if "DiseaseHistory" in klass.__dict__:
            descriptor = klass.__dict__["DiseaseHistory"]
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

def test_patient_has_Prescriptions():
    assert hasattr(Patient, "Prescriptions")
    descriptor = None
    for klass in Patient.__mro__:
        if "Prescriptions" in klass.__dict__:
            descriptor = klass.__dict__["Prescriptions"]
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

def test_patient_has_Phone():
    assert hasattr(Patient, "Phone")
    descriptor = None
    for klass in Patient.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "FullName" in params, "Missing parameter 'FullName'"
    assert "BirthDate" in params, "Missing parameter 'BirthDate'"
    assert "AccessLevel" in params, "Missing parameter 'AccessLevel'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Gender" in params, "Missing parameter 'Gender'"

def test_person_has_FullName():
    assert hasattr(Person, "FullName")
    descriptor = None
    for klass in Person.__mro__:
        if "FullName" in klass.__dict__:
            descriptor = klass.__dict__["FullName"]
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

def test_person_has_AccessLevel():
    assert hasattr(Person, "AccessLevel")
    descriptor = None
    for klass in Person.__mro__:
        if "AccessLevel" in klass.__dict__:
            descriptor = klass.__dict__["AccessLevel"]
            break
    assert isinstance(descriptor, property)

def test_person_has_ID():
    assert hasattr(Person, "ID")
    descriptor = None
    for klass in Person.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
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



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Languages" in params, "Missing parameter 'Languages'"
    assert "Certification" in params, "Missing parameter 'Certification'"
    assert "Joined" in params, "Missing parameter 'Joined'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Education" in params, "Missing parameter 'Education'"

def test_staff_has_Languages():
    assert hasattr(Staff, "Languages")
    descriptor = None
    for klass in Staff.__mro__:
        if "Languages" in klass.__dict__:
            descriptor = klass.__dict__["Languages"]
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

def test_staff_has_Joined():
    assert hasattr(Staff, "Joined")
    descriptor = None
    for klass in Staff.__mro__:
        if "Joined" in klass.__dict__:
            descriptor = klass.__dict__["Joined"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Status():
    assert hasattr(Staff, "Status")
    descriptor = None
    for klass in Staff.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
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
HospitalSystem_strategy = st.builds(
    HospitalSystem,
    Doctors=
        safe_text,
    admin=
        st.none(),
    Patients=
        safe_text
)
SystemAdministrator_strategy = st.builds(
    SystemAdministrator,
    Doctors=
        safe_text,
    Patients=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    Specialization=
        safe_text,
    Shedule=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    DiseaseHistory=
        safe_text,
    Age=
        st.integers(),
    Prescriptions=
        safe_text,
    Address=
        safe_text,
    Phone=
        safe_text
)
Person_strategy = st.builds(
    Person,
    FullName=
        safe_text,
    BirthDate=
        safe_text,
    AccessLevel=
        safe_text,
    ID=
        st.integers(),
    Gender=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    Languages=
        safe_text,
    Certification=
        safe_text,
    Joined=
        safe_text,
    Status=
        safe_text,
    Education=
        safe_text
)

@given(instance=HospitalSystem_strategy)
@settings(max_examples=50)
def test_hospitalsystem_instantiation(instance):
    assert isinstance(instance, HospitalSystem)



@given(instance=HospitalSystem_strategy)
def test_hospitalsystem_Doctors_setter(instance):
    original = instance.Doctors
    instance.Doctors = original
    assert instance.Doctors == original



@given(instance=HospitalSystem_strategy)
def test_hospitalsystem_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original



@given(instance=HospitalSystem_strategy)
def test_hospitalsystem_Patients_setter(instance):
    original = instance.Patients
    instance.Patients = original
    assert instance.Patients == original

@given(instance=SystemAdministrator_strategy)
@settings(max_examples=50)
def test_systemadministrator_instantiation(instance):
    assert isinstance(instance, SystemAdministrator)



@given(instance=SystemAdministrator_strategy)
def test_systemadministrator_Doctors_setter(instance):
    original = instance.Doctors
    instance.Doctors = original
    assert instance.Doctors == original



@given(instance=SystemAdministrator_strategy)
def test_systemadministrator_Patients_setter(instance):
    original = instance.Patients
    instance.Patients = original
    assert instance.Patients == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_doctor_Shedule_setter(instance):
    original = instance.Shedule
    instance.Shedule = original
    assert instance.Shedule == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_DiseaseHistory_setter(instance):
    original = instance.DiseaseHistory
    instance.DiseaseHistory = original
    assert instance.DiseaseHistory == original



@given(instance=Patient_strategy)
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_patient_Prescriptions_setter(instance):
    original = instance.Prescriptions
    instance.Prescriptions = original
    assert instance.Prescriptions == original



@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_patient_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_FullName_setter(instance):
    original = instance.FullName
    instance.FullName = original
    assert instance.FullName == original



@given(instance=Person_strategy)
def test_person_BirthDate_setter(instance):
    original = instance.BirthDate
    instance.BirthDate = original
    assert instance.BirthDate == original



@given(instance=Person_strategy)
def test_person_AccessLevel_setter(instance):
    original = instance.AccessLevel
    instance.AccessLevel = original
    assert instance.AccessLevel == original



@given(instance=Person_strategy)
def test_person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Person_strategy)
def test_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Languages_setter(instance):
    original = instance.Languages
    instance.Languages = original
    assert instance.Languages == original



@given(instance=Staff_strategy)
def test_staff_Certification_setter(instance):
    original = instance.Certification
    instance.Certification = original
    assert instance.Certification == original



@given(instance=Staff_strategy)
def test_staff_Joined_setter(instance):
    original = instance.Joined
    instance.Joined = original
    assert instance.Joined == original



@given(instance=Staff_strategy)
def test_staff_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Staff_strategy)
def test_staff_Education_setter(instance):
    original = instance.Education
    instance.Education = original
    assert instance.Education == original
