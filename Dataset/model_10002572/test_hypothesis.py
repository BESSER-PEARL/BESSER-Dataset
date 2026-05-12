import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Nurse,
    Technical_Staff,
    Administrative_Staff,
    Operations_Staff,
    Department,
    Doctor,
    Staff,
    Hospital,
    Patient,
    Person,
    Receptionist,
    Technologist,
    Technician,
    Front_Desk_Staff,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())



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



def test_operations_staff_is_not_abstract():
    assert not inspect.isabstract(Operations_Staff)


def test_operations_staff_constructor_exists():
    assert callable(Operations_Staff.__init__)


def test_operations_staff_constructor_args():
    sig = inspect.signature(Operations_Staff.__init__)
    params = list(sig.parameters.keys())



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "specialty" in params, "Missing parameter 'specialty'"
    assert "locations" in params, "Missing parameter 'locations'"

def test_doctor_has_specialty():
    assert hasattr(Doctor, "specialty")
    descriptor = None
    for klass in Doctor.__mro__:
        if "specialty" in klass.__dict__:
            descriptor = klass.__dict__["specialty"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_locations():
    assert hasattr(Doctor, "locations")
    descriptor = None
    for klass in Doctor.__mro__:
        if "locations" in klass.__dict__:
            descriptor = klass.__dict__["locations"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "education" in params, "Missing parameter 'education'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "certification" in params, "Missing parameter 'certification'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "joined" in params, "Missing parameter 'joined'"

def test_staff_has_education():
    assert hasattr(Staff, "education")
    descriptor = None
    for klass in Staff.__mro__:
        if "education" in klass.__dict__:
            descriptor = klass.__dict__["education"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_languages():
    assert hasattr(Staff, "languages")
    descriptor = None
    for klass in Staff.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_UserName():
    assert hasattr(Staff, "UserName")
    descriptor = None
    for klass in Staff.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_certification():
    assert hasattr(Staff, "certification")
    descriptor = None
    for klass in Staff.__mro__:
        if "certification" in klass.__dict__:
            descriptor = klass.__dict__["certification"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Password():
    assert hasattr(Staff, "Password")
    descriptor = None
    for klass in Staff.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_joined():
    assert hasattr(Staff, "joined")
    descriptor = None
    for klass in Staff.__mro__:
        if "joined" in klass.__dict__:
            descriptor = klass.__dict__["joined"]
            break
    assert isinstance(descriptor, property)



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_hospital_has_phone():
    assert hasattr(Hospital, "phone")
    descriptor = None
    for klass in Hospital.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

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



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "sickness" in params, "Missing parameter 'sickness'"
    assert "specialReqs" in params, "Missing parameter 'specialReqs'"
    assert "allergies" in params, "Missing parameter 'allergies'"
    assert "accepted" in params, "Missing parameter 'accepted'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "prescriptions" in params, "Missing parameter 'prescriptions'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "age" in params, "Missing parameter 'age'"
    assert "id" in params, "Missing parameter 'id'"

def test_patient_has_sickness():
    assert hasattr(Patient, "sickness")
    descriptor = None
    for klass in Patient.__mro__:
        if "sickness" in klass.__dict__:
            descriptor = klass.__dict__["sickness"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_specialReqs():
    assert hasattr(Patient, "specialReqs")
    descriptor = None
    for klass in Patient.__mro__:
        if "specialReqs" in klass.__dict__:
            descriptor = klass.__dict__["specialReqs"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_allergies():
    assert hasattr(Patient, "allergies")
    descriptor = None
    for klass in Patient.__mro__:
        if "allergies" in klass.__dict__:
            descriptor = klass.__dict__["allergies"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_accepted():
    assert hasattr(Patient, "accepted")
    descriptor = None
    for klass in Patient.__mro__:
        if "accepted" in klass.__dict__:
            descriptor = klass.__dict__["accepted"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_birthDate():
    assert hasattr(Patient, "birthDate")
    descriptor = None
    for klass in Patient.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_prescriptions():
    assert hasattr(Patient, "prescriptions")
    descriptor = None
    for klass in Patient.__mro__:
        if "prescriptions" in klass.__dict__:
            descriptor = klass.__dict__["prescriptions"]
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

def test_patient_has_gender():
    assert hasattr(Patient, "gender")
    descriptor = None
    for klass in Patient.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_age():
    assert hasattr(Patient, "age")
    descriptor = None
    for klass in Patient.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_id():
    assert hasattr(Patient, "id")
    descriptor = None
    for klass in Patient.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "familyName" in params, "Missing parameter 'familyName'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "title" in params, "Missing parameter 'title'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "givenName" in params, "Missing parameter 'givenName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "homeAddress" in params, "Missing parameter 'homeAddress'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "phone" in params, "Missing parameter 'phone'"

def test_person_has_familyName():
    assert hasattr(Person, "familyName")
    descriptor = None
    for klass in Person.__mro__:
        if "familyName" in klass.__dict__:
            descriptor = klass.__dict__["familyName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_gender():
    assert hasattr(Person, "gender")
    descriptor = None
    for klass in Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
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

def test_person_has_birthDate():
    assert hasattr(Person, "birthDate")
    descriptor = None
    for klass in Person.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_person_has_givenName():
    assert hasattr(Person, "givenName")
    descriptor = None
    for klass in Person.__mro__:
        if "givenName" in klass.__dict__:
            descriptor = klass.__dict__["givenName"]
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

def test_person_has_homeAddress():
    assert hasattr(Person, "homeAddress")
    descriptor = None
    for klass in Person.__mro__:
        if "homeAddress" in klass.__dict__:
            descriptor = klass.__dict__["homeAddress"]
            break
    assert isinstance(descriptor, property)

def test_person_has_middleName():
    assert hasattr(Person, "middleName")
    descriptor = None
    for klass in Person.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_phone():
    assert hasattr(Person, "phone")
    descriptor = None
    for klass in Person.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())



def test_technologist_is_not_abstract():
    assert not inspect.isabstract(Technologist)


def test_technologist_constructor_exists():
    assert callable(Technologist.__init__)


def test_technologist_constructor_args():
    sig = inspect.signature(Technologist.__init__)
    params = list(sig.parameters.keys())



def test_technician_is_not_abstract():
    assert not inspect.isabstract(Technician)


def test_technician_constructor_exists():
    assert callable(Technician.__init__)


def test_technician_constructor_args():
    sig = inspect.signature(Technician.__init__)
    params = list(sig.parameters.keys())



def test_front_desk_staff_is_not_abstract():
    assert not inspect.isabstract(Front_Desk_Staff)


def test_front_desk_staff_constructor_exists():
    assert callable(Front_Desk_Staff.__init__)


def test_front_desk_staff_constructor_args():
    sig = inspect.signature(Front_Desk_Staff.__init__)
    params = list(sig.parameters.keys())


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
Nurse_strategy = st.builds(
    Nurse,
)
Technical_Staff_strategy = st.builds(
    Technical_Staff,
)
Administrative_Staff_strategy = st.builds(
    Administrative_Staff,
)
Operations_Staff_strategy = st.builds(
    Operations_Staff,
)
Department_strategy = st.builds(
    Department,
)
Doctor_strategy = st.builds(
    Doctor,
    specialty=
        safe_text,
    locations=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    education=
        safe_text,
    languages=
        safe_text,
    UserName=
        safe_text,
    certification=
        safe_text,
    Password=
        safe_text,
    joined=
        safe_text
)
Hospital_strategy = st.builds(
    Hospital,
    phone=
        safe_text,
    address=
        safe_text,
    name=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    sickness=
        safe_text,
    specialReqs=
        safe_text,
    allergies=
        safe_text,
    accepted=
        safe_text,
    birthDate=
        safe_text,
    prescriptions=
        safe_text,
    name=
        safe_text,
    gender=
        safe_text,
    age=
        st.integers(),
    id=
        safe_text
)
Person_strategy = st.builds(
    Person,
    familyName=
        safe_text,
    gender=
        safe_text,
    title=
        safe_text,
    birthDate=
        safe_text,
    givenName=
        safe_text,
    name=
        safe_text,
    homeAddress=
        safe_text,
    middleName=
        safe_text,
    phone=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
)
Technologist_strategy = st.builds(
    Technologist,
)
Technician_strategy = st.builds(
    Technician,
)
Front_Desk_Staff_strategy = st.builds(
    Front_Desk_Staff,
)

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)

@given(instance=Technical_Staff_strategy)
@settings(max_examples=50)
def test_technical_staff_instantiation(instance):
    assert isinstance(instance, Technical_Staff)

@given(instance=Administrative_Staff_strategy)
@settings(max_examples=50)
def test_administrative_staff_instantiation(instance):
    assert isinstance(instance, Administrative_Staff)

@given(instance=Operations_Staff_strategy)
@settings(max_examples=50)
def test_operations_staff_instantiation(instance):
    assert isinstance(instance, Operations_Staff)

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_specialty_setter(instance):
    original = instance.specialty
    instance.specialty = original
    assert instance.specialty == original



@given(instance=Doctor_strategy)
def test_doctor_locations_setter(instance):
    original = instance.locations
    instance.locations = original
    assert instance.locations == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_education_setter(instance):
    original = instance.education
    instance.education = original
    assert instance.education == original



@given(instance=Staff_strategy)
def test_staff_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original



@given(instance=Staff_strategy)
def test_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Staff_strategy)
def test_staff_certification_setter(instance):
    original = instance.certification
    instance.certification = original
    assert instance.certification == original



@given(instance=Staff_strategy)
def test_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Staff_strategy)
def test_staff_joined_setter(instance):
    original = instance.joined
    instance.joined = original
    assert instance.joined == original

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



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

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_sickness_setter(instance):
    original = instance.sickness
    instance.sickness = original
    assert instance.sickness == original



@given(instance=Patient_strategy)
def test_patient_specialReqs_setter(instance):
    original = instance.specialReqs
    instance.specialReqs = original
    assert instance.specialReqs == original



@given(instance=Patient_strategy)
def test_patient_allergies_setter(instance):
    original = instance.allergies
    instance.allergies = original
    assert instance.allergies == original



@given(instance=Patient_strategy)
def test_patient_accepted_setter(instance):
    original = instance.accepted
    instance.accepted = original
    assert instance.accepted == original



@given(instance=Patient_strategy)
def test_patient_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=Patient_strategy)
def test_patient_prescriptions_setter(instance):
    original = instance.prescriptions
    instance.prescriptions = original
    assert instance.prescriptions == original



@given(instance=Patient_strategy)
def test_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_patient_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Patient_strategy)
def test_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_familyName_setter(instance):
    original = instance.familyName
    instance.familyName = original
    assert instance.familyName == original



@given(instance=Person_strategy)
def test_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Person_strategy)
def test_person_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Person_strategy)
def test_person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=Person_strategy)
def test_person_givenName_setter(instance):
    original = instance.givenName
    instance.givenName = original
    assert instance.givenName == original



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_person_homeAddress_setter(instance):
    original = instance.homeAddress
    instance.homeAddress = original
    assert instance.homeAddress == original



@given(instance=Person_strategy)
def test_person_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=Person_strategy)
def test_person_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)

@given(instance=Technologist_strategy)
@settings(max_examples=50)
def test_technologist_instantiation(instance):
    assert isinstance(instance, Technologist)

@given(instance=Technician_strategy)
@settings(max_examples=50)
def test_technician_instantiation(instance):
    assert isinstance(instance, Technician)

@given(instance=Front_Desk_Staff_strategy)
@settings(max_examples=50)
def test_front_desk_staff_instantiation(instance):
    assert isinstance(instance, Front_Desk_Staff)
