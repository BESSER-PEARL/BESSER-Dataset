import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Receptionist,
    Surgeon,
    Nurse,
    Doctor,
    Technical_Staff,
    Administrative_Staff,
    Operation_Staff,
    Staff,
    Department,
    Patient,
    Person,
    Hospital,
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



def test_surgeon_is_not_abstract():
    assert not inspect.isabstract(Surgeon)


def test_surgeon_constructor_exists():
    assert callable(Surgeon.__init__)


def test_surgeon_constructor_args():
    sig = inspect.signature(Surgeon.__init__)
    params = list(sig.parameters.keys())



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Speciality" in params, "Missing parameter 'Speciality'"
    assert "Location" in params, "Missing parameter 'Location'"

def test_doctor_has_Speciality():
    assert hasattr(Doctor, "Speciality")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Speciality" in klass.__dict__:
            descriptor = klass.__dict__["Speciality"]
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



def test_technical_staff_is_not_abstract():
    assert not inspect.isabstract(Technical_Staff)


def test_technical_staff_constructor_exists():
    assert callable(Technical_Staff.__init__)


def test_technical_staff_constructor_args():
    sig = inspect.signature(Technical_Staff.__init__)
    params = list(sig.parameters.keys())



def test_administrative_staff_is_not_abstract():
    assert not inspect.isabstract(Administrative_Staff)


def test_administrative_staff_constructor_exists():
    assert callable(Administrative_Staff.__init__)


def test_administrative_staff_constructor_args():
    sig = inspect.signature(Administrative_Staff.__init__)
    params = list(sig.parameters.keys())



def test_operation_staff_is_not_abstract():
    assert not inspect.isabstract(Operation_Staff)


def test_operation_staff_constructor_exists():
    assert callable(Operation_Staff.__init__)


def test_operation_staff_constructor_args():
    sig = inspect.signature(Operation_Staff.__init__)
    params = list(sig.parameters.keys())



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Certification" in params, "Missing parameter 'Certification'"
    assert "Education" in params, "Missing parameter 'Education'"
    assert "Languages" in params, "Missing parameter 'Languages'"

def test_staff_has_Certification():
    assert hasattr(Staff, "Certification")
    descriptor = None
    for klass in Staff.__mro__:
        if "Certification" in klass.__dict__:
            descriptor = klass.__dict__["Certification"]
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

def test_staff_has_Languages():
    assert hasattr(Staff, "Languages")
    descriptor = None
    for klass in Staff.__mro__:
        if "Languages" in klass.__dict__:
            descriptor = klass.__dict__["Languages"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Allergy" in params, "Missing parameter 'Allergy'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"
    assert "Prescription" in params, "Missing parameter 'Prescription'"

def test_patient_has_Allergy():
    assert hasattr(Patient, "Allergy")
    descriptor = None
    for klass in Patient.__mro__:
        if "Allergy" in klass.__dict__:
            descriptor = klass.__dict__["Allergy"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_name():
    assert hasattr(Patient, "name")
    descriptor = None
    for klass in Patient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_patient_has_Prescription():
    assert hasattr(Patient, "Prescription")
    descriptor = None
    for klass in Patient.__mro__:
        if "Prescription" in klass.__dict__:
            descriptor = klass.__dict__["Prescription"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "father_s_name" in params, "Missing parameter 'father_s_name'"
    assert "Birth_date" in params, "Missing parameter 'Birth_date'"

def test_person_has_Gender():
    assert hasattr(Person, "Gender")
    descriptor = None
    for klass in Person.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
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

def test_person_has_Age():
    assert hasattr(Person, "Age")
    descriptor = None
    for klass in Person.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_person_has_father_s_name():
    assert hasattr(Person, "father_s_name")
    descriptor = None
    for klass in Person.__mro__:
        if "father_s_name" in klass.__dict__:
            descriptor = klass.__dict__["father_s_name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Birth_date():
    assert hasattr(Person, "Birth_date")
    descriptor = None
    for klass in Person.__mro__:
        if "Birth_date" in klass.__dict__:
            descriptor = klass.__dict__["Birth_date"]
            break
    assert isinstance(descriptor, property)



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "phone_no" in params, "Missing parameter 'phone_no'"

def test_hospital_has_name():
    assert hasattr(Hospital, "name")
    descriptor = None
    for klass in Hospital.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_hospital_has_phone_no():
    assert hasattr(Hospital, "phone_no")
    descriptor = None
    for klass in Hospital.__mro__:
        if "phone_no" in klass.__dict__:
            descriptor = klass.__dict__["phone_no"]
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
Surgeon_strategy = st.builds(
    Surgeon,
)
Nurse_strategy = st.builds(
    Nurse,
)
Doctor_strategy = st.builds(
    Doctor,
    Speciality=
        safe_text,
    Location=
        safe_text
)
Technical_Staff_strategy = st.builds(
    Technical_Staff,
)
Administrative_Staff_strategy = st.builds(
    Administrative_Staff,
)
Operation_Staff_strategy = st.builds(
    Operation_Staff,
)
Staff_strategy = st.builds(
    Staff,
    Certification=
        safe_text,
    Education=
        safe_text,
    Languages=
        safe_text
)
Department_strategy = st.builds(
    Department,
)
Patient_strategy = st.builds(
    Patient,
    Allergy=
        safe_text,
    name=
        safe_text,
    Sickness=
        safe_text,
    Prescription=
        safe_text
)
Person_strategy = st.builds(
    Person,
    Gender=
        safe_text,
    name=
        safe_text,
    Age=
        st.integers(),
    father_s_name=
        safe_text,
    Birth_date=
        safe_text
)
Hospital_strategy = st.builds(
    Hospital,
    name=
        safe_text,
    Address=
        safe_text,
    phone_no=
        safe_text
)

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)

@given(instance=Surgeon_strategy)
@settings(max_examples=50)
def test_surgeon_instantiation(instance):
    assert isinstance(instance, Surgeon)

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Speciality_setter(instance):
    original = instance.Speciality
    instance.Speciality = original
    assert instance.Speciality == original



@given(instance=Doctor_strategy)
def test_doctor_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=Technical_Staff_strategy)
@settings(max_examples=50)
def test_technical_staff_instantiation(instance):
    assert isinstance(instance, Technical_Staff)

@given(instance=Administrative_Staff_strategy)
@settings(max_examples=50)
def test_administrative_staff_instantiation(instance):
    assert isinstance(instance, Administrative_Staff)

@given(instance=Operation_Staff_strategy)
@settings(max_examples=50)
def test_operation_staff_instantiation(instance):
    assert isinstance(instance, Operation_Staff)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Certification_setter(instance):
    original = instance.Certification
    instance.Certification = original
    assert instance.Certification == original



@given(instance=Staff_strategy)
def test_staff_Education_setter(instance):
    original = instance.Education
    instance.Education = original
    assert instance.Education == original



@given(instance=Staff_strategy)
def test_staff_Languages_setter(instance):
    original = instance.Languages
    instance.Languages = original
    assert instance.Languages == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Allergy_setter(instance):
    original = instance.Allergy
    instance.Allergy = original
    assert instance.Allergy == original



@given(instance=Patient_strategy)
def test_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_patient_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original



@given(instance=Patient_strategy)
def test_patient_Prescription_setter(instance):
    original = instance.Prescription
    instance.Prescription = original
    assert instance.Prescription == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_person_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Person_strategy)
def test_person_father_s_name_setter(instance):
    original = instance.father_s_name
    instance.father_s_name = original
    assert instance.father_s_name == original



@given(instance=Person_strategy)
def test_person_Birth_date_setter(instance):
    original = instance.Birth_date
    instance.Birth_date = original
    assert instance.Birth_date == original

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hospital_strategy)
def test_hospital_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Hospital_strategy)
def test_hospital_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original
