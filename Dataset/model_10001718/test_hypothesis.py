import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    JuniorDoctor,
    ConsultantDoctor,
    Doctor,
    Patient,
    Ward,
    Team,
    Hospital,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "age" in params, "Missing parameter 'age'"
    assert "address" in params, "Missing parameter 'address'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_person_has_phone():
    assert hasattr(Person, "phone")
    descriptor = None
    for klass in Person.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_person_has_age():
    assert hasattr(Person, "age")
    descriptor = None
    for klass in Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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

def test_person_has_gender():
    assert hasattr(Person, "gender")
    descriptor = None
    for klass in Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)



def test_juniordoctor_is_not_abstract():
    assert not inspect.isabstract(JuniorDoctor)


def test_juniordoctor_constructor_exists():
    assert callable(JuniorDoctor.__init__)


def test_juniordoctor_constructor_args():
    sig = inspect.signature(JuniorDoctor.__init__)
    params = list(sig.parameters.keys())



def test_consultantdoctor_is_not_abstract():
    assert not inspect.isabstract(ConsultantDoctor)


def test_consultantdoctor_constructor_exists():
    assert callable(ConsultantDoctor.__init__)


def test_consultantdoctor_constructor_args():
    sig = inspect.signature(ConsultantDoctor.__init__)
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



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "sickness" in params, "Missing parameter 'sickness'"
    assert "allergies" in params, "Missing parameter 'allergies'"
    assert "specialReqs" in params, "Missing parameter 'specialReqs'"
    assert "prescriptions" in params, "Missing parameter 'prescriptions'"
    assert "id" in params, "Missing parameter 'id'"

def test_patient_has_sickness():
    assert hasattr(Patient, "sickness")
    descriptor = None
    for klass in Patient.__mro__:
        if "sickness" in klass.__dict__:
            descriptor = klass.__dict__["sickness"]
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

def test_patient_has_specialReqs():
    assert hasattr(Patient, "specialReqs")
    descriptor = None
    for klass in Patient.__mro__:
        if "specialReqs" in klass.__dict__:
            descriptor = klass.__dict__["specialReqs"]
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

def test_patient_has_id():
    assert hasattr(Patient, "id")
    descriptor = None
    for klass in Patient.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ward_is_not_abstract():
    assert not inspect.isabstract(Ward)


def test_ward_constructor_exists():
    assert callable(Ward.__init__)


def test_ward_constructor_args():
    sig = inspect.signature(Ward.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_ward_has_name():
    assert hasattr(Ward, "name")
    descriptor = None
    for klass in Ward.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_capacity():
    assert hasattr(Ward, "capacity")
    descriptor = None
    for klass in Ward.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_team_is_not_abstract():
    assert not inspect.isabstract(Team)


def test_team_constructor_exists():
    assert callable(Team.__init__)


def test_team_constructor_args():
    sig = inspect.signature(Team.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_team_has_name():
    assert hasattr(Team, "name")
    descriptor = None
    for klass in Team.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"

def test_hospital_has_name():
    assert hasattr(Hospital, "name")
    descriptor = None
    for klass in Hospital.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_hospital_has_phone():
    assert hasattr(Hospital, "phone")
    descriptor = None
    for klass in Hospital.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
Person_strategy = st.builds(
    Person,
    phone=
        safe_text,
    age=
        st.integers(),
    address=
        safe_text,
    gender=
        st.none()
)
JuniorDoctor_strategy = st.builds(
    JuniorDoctor,
)
ConsultantDoctor_strategy = st.builds(
    ConsultantDoctor,
)
Doctor_strategy = st.builds(
    Doctor,
    specialty=
        safe_text,
    locations=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    sickness=
        safe_text,
    allergies=
        safe_text,
    specialReqs=
        safe_text,
    prescriptions=
        safe_text,
    id=
        st.integers()
)
Ward_strategy = st.builds(
    Ward,
    name=
        safe_text,
    capacity=
        st.integers()
)
Team_strategy = st.builds(
    Team,
    name=
        safe_text
)
Hospital_strategy = st.builds(
    Hospital,
    name=
        safe_text,
    address=
        safe_text,
    phone=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Person_strategy)
def test_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Person_strategy)
def test_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=JuniorDoctor_strategy)
@settings(max_examples=50)
def test_juniordoctor_instantiation(instance):
    assert isinstance(instance, JuniorDoctor)

@given(instance=ConsultantDoctor_strategy)
@settings(max_examples=50)
def test_consultantdoctor_instantiation(instance):
    assert isinstance(instance, ConsultantDoctor)

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
def test_patient_allergies_setter(instance):
    original = instance.allergies
    instance.allergies = original
    assert instance.allergies == original



@given(instance=Patient_strategy)
def test_patient_specialReqs_setter(instance):
    original = instance.specialReqs
    instance.specialReqs = original
    assert instance.specialReqs == original



@given(instance=Patient_strategy)
def test_patient_prescriptions_setter(instance):
    original = instance.prescriptions
    instance.prescriptions = original
    assert instance.prescriptions == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Ward_strategy)
@settings(max_examples=50)
def test_ward_instantiation(instance):
    assert isinstance(instance, Ward)



@given(instance=Ward_strategy)
def test_ward_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Ward_strategy)
def test_ward_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=Team_strategy)
@settings(max_examples=50)
def test_team_instantiation(instance):
    assert isinstance(instance, Team)



@given(instance=Team_strategy)
def test_team_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_hospital_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Hospital_strategy)
def test_hospital_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original
