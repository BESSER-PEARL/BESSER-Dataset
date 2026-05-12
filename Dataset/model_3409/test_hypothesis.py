import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VorkursModel_Room,
    Person,
    VorkursModel_Contact,
    VorkursModel_Person,
    VorkursModel_TeachingAssistant,
    VorkursModel_Student,
    VorkursModel_RegistrationSystem,
    VorkursModel_Address,
    VorkursModel_Qualification,
    VorkursModel_Notebook,
    Subject,
    OperatingSystem,
    Nationality,
    ProgrammingLanguage,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vorkursmodel_room_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Room)


def test_vorkursmodel_room_constructor_exists():
    assert callable(VorkursModel_Room.__init__)


def test_vorkursmodel_room_constructor_args():
    sig = inspect.signature(VorkursModel_Room.__init__)
    params = list(sig.parameters.keys())
    assert "hasComputers" in params, "Missing parameter 'hasComputers'"
    assert "seats" in params, "Missing parameter 'seats'"
    assert "roomNr" in params, "Missing parameter 'roomNr'"
    assert "sockets" in params, "Missing parameter 'sockets'"

def test_vorkursmodel_room_has_hasComputers():
    assert hasattr(VorkursModel_Room, "hasComputers")
    descriptor = None
    for klass in VorkursModel_Room.__mro__:
        if "hasComputers" in klass.__dict__:
            descriptor = klass.__dict__["hasComputers"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_room_has_seats():
    assert hasattr(VorkursModel_Room, "seats")
    descriptor = None
    for klass in VorkursModel_Room.__mro__:
        if "seats" in klass.__dict__:
            descriptor = klass.__dict__["seats"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_room_has_roomNr():
    assert hasattr(VorkursModel_Room, "roomNr")
    descriptor = None
    for klass in VorkursModel_Room.__mro__:
        if "roomNr" in klass.__dict__:
            descriptor = klass.__dict__["roomNr"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_room_has_sockets():
    assert hasattr(VorkursModel_Room, "sockets")
    descriptor = None
    for klass in VorkursModel_Room.__mro__:
        if "sockets" in klass.__dict__:
            descriptor = klass.__dict__["sockets"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel_contact_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Contact)


def test_vorkursmodel_contact_constructor_exists():
    assert callable(VorkursModel_Contact.__init__)


def test_vorkursmodel_contact_constructor_args():
    sig = inspect.signature(VorkursModel_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "phonenumber" in params, "Missing parameter 'phonenumber'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_vorkursmodel_contact_has_phonenumber():
    assert hasattr(VorkursModel_Contact, "phonenumber")
    descriptor = None
    for klass in VorkursModel_Contact.__mro__:
        if "phonenumber" in klass.__dict__:
            descriptor = klass.__dict__["phonenumber"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_contact_has_Email():
    assert hasattr(VorkursModel_Contact, "Email")
    descriptor = None
    for klass in VorkursModel_Contact.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel_person_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Person)


def test_vorkursmodel_person_constructor_exists():
    assert callable(VorkursModel_Person.__init__)


def test_vorkursmodel_person_constructor_args():
    sig = inspect.signature(VorkursModel_Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_vorkursmodel_person_has_gender():
    assert hasattr(VorkursModel_Person, "gender")
    descriptor = None
    for klass in VorkursModel_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_person_has_subject():
    assert hasattr(VorkursModel_Person, "subject")
    descriptor = None
    for klass in VorkursModel_Person.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_person_has_lastname():
    assert hasattr(VorkursModel_Person, "lastname")
    descriptor = None
    for klass in VorkursModel_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_person_has_firstname():
    assert hasattr(VorkursModel_Person, "firstname")
    descriptor = None
    for klass in VorkursModel_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel_teachingassistant_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_TeachingAssistant)


def test_vorkursmodel_teachingassistant_constructor_exists():
    assert callable(VorkursModel_TeachingAssistant.__init__)


def test_vorkursmodel_teachingassistant_constructor_args():
    sig = inspect.signature(VorkursModel_TeachingAssistant.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel_student_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Student)


def test_vorkursmodel_student_constructor_exists():
    assert callable(VorkursModel_Student.__init__)


def test_vorkursmodel_student_constructor_args():
    sig = inspect.signature(VorkursModel_Student.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel_registrationsystem_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_RegistrationSystem)


def test_vorkursmodel_registrationsystem_constructor_exists():
    assert callable(VorkursModel_RegistrationSystem.__init__)


def test_vorkursmodel_registrationsystem_constructor_args():
    sig = inspect.signature(VorkursModel_RegistrationSystem.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel_address_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Address)


def test_vorkursmodel_address_constructor_exists():
    assert callable(VorkursModel_Address.__init__)


def test_vorkursmodel_address_constructor_args():
    sig = inspect.signature(VorkursModel_Address.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"

def test_vorkursmodel_address_has_state():
    assert hasattr(VorkursModel_Address, "state")
    descriptor = None
    for klass in VorkursModel_Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_address_has_zip():
    assert hasattr(VorkursModel_Address, "zip")
    descriptor = None
    for klass in VorkursModel_Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_address_has_street():
    assert hasattr(VorkursModel_Address, "street")
    descriptor = None
    for klass in VorkursModel_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_address_has_city():
    assert hasattr(VorkursModel_Address, "city")
    descriptor = None
    for klass in VorkursModel_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel_qualification_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Qualification)


def test_vorkursmodel_qualification_constructor_exists():
    assert callable(VorkursModel_Qualification.__init__)


def test_vorkursmodel_qualification_constructor_args():
    sig = inspect.signature(VorkursModel_Qualification.__init__)
    params = list(sig.parameters.keys())
    assert "hasProgrammingExperience" in params, "Missing parameter 'hasProgrammingExperience'"
    assert "Language" in params, "Missing parameter 'Language'"
    assert "programminLanguage" in params, "Missing parameter 'programminLanguage'"
    assert "hasPCExperience" in params, "Missing parameter 'hasPCExperience'"

def test_vorkursmodel_qualification_has_hasProgrammingExperience():
    assert hasattr(VorkursModel_Qualification, "hasProgrammingExperience")
    descriptor = None
    for klass in VorkursModel_Qualification.__mro__:
        if "hasProgrammingExperience" in klass.__dict__:
            descriptor = klass.__dict__["hasProgrammingExperience"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_qualification_has_Language():
    assert hasattr(VorkursModel_Qualification, "Language")
    descriptor = None
    for klass in VorkursModel_Qualification.__mro__:
        if "Language" in klass.__dict__:
            descriptor = klass.__dict__["Language"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_qualification_has_programminLanguage():
    assert hasattr(VorkursModel_Qualification, "programminLanguage")
    descriptor = None
    for klass in VorkursModel_Qualification.__mro__:
        if "programminLanguage" in klass.__dict__:
            descriptor = klass.__dict__["programminLanguage"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_qualification_has_hasPCExperience():
    assert hasattr(VorkursModel_Qualification, "hasPCExperience")
    descriptor = None
    for klass in VorkursModel_Qualification.__mro__:
        if "hasPCExperience" in klass.__dict__:
            descriptor = klass.__dict__["hasPCExperience"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel_notebook_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Notebook)


def test_vorkursmodel_notebook_constructor_exists():
    assert callable(VorkursModel_Notebook.__init__)


def test_vorkursmodel_notebook_constructor_args():
    sig = inspect.signature(VorkursModel_Notebook.__init__)
    params = list(sig.parameters.keys())
    assert "OperatingSystem" in params, "Missing parameter 'OperatingSystem'"
    assert "hasWLAN" in params, "Missing parameter 'hasWLAN'"

def test_vorkursmodel_notebook_has_OperatingSystem():
    assert hasattr(VorkursModel_Notebook, "OperatingSystem")
    descriptor = None
    for klass in VorkursModel_Notebook.__mro__:
        if "OperatingSystem" in klass.__dict__:
            descriptor = klass.__dict__["OperatingSystem"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel_notebook_has_hasWLAN():
    assert hasattr(VorkursModel_Notebook, "hasWLAN")
    descriptor = None
    for klass in VorkursModel_Notebook.__mro__:
        if "hasWLAN" in klass.__dict__:
            descriptor = klass.__dict__["hasWLAN"]
            break
    assert isinstance(descriptor, property)

def test_subject_exists():
    # Check that the Enumeration exists
    assert Subject is not None

def test_subject_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Subject]
    expected_literals = [
        "ComputerScience",
        "MechanicalEngineering",
        "AppliedGeographics",
        "BusinessEngineering",
        "Physics",
        "Mathematics",
        "CES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Subject"

def test_operatingsystem_exists():
    # Check that the Enumeration exists
    assert OperatingSystem is not None

def test_operatingsystem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatingSystem]
    expected_literals = [
        "other",
        "MacOS",
        "Linux_Unix",
        "Windows",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatingSystem"

def test_nationality_exists():
    # Check that the Enumeration exists
    assert Nationality is not None

def test_nationality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Nationality]
    expected_literals = [
        "Spanish",
        "German",
        "other",
        "French",
        "English",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nationality"

def test_programminglanguage_exists():
    # Check that the Enumeration exists
    assert ProgrammingLanguage is not None

def test_programminglanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammingLanguage]
    expected_literals = [
        "Pascal_Delphi",
        "other",
        "Java",
        "C_CPP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammingLanguage"

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Female",
        "Male",
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
VorkursModel_Room_strategy = st.builds(
    VorkursModel_Room,
    hasComputers=
        st.booleans(),
    seats=
        st.integers(),
    roomNr=
        st.integers(),
    sockets=
        st.booleans()
)
Person_strategy = st.builds(
    Person,
)
VorkursModel_Contact_strategy = st.builds(
    VorkursModel_Contact,
    phonenumber=
        safe_text,
    Email=
        safe_text
)
VorkursModel_Person_strategy = st.builds(
    VorkursModel_Person,
    gender=
        safe_text,
    subject=
        safe_text,
    lastname=
        safe_text,
    firstname=
        safe_text
)
VorkursModel_TeachingAssistant_strategy = st.builds(
    VorkursModel_TeachingAssistant,
)
VorkursModel_Student_strategy = st.builds(
    VorkursModel_Student,
)
VorkursModel_RegistrationSystem_strategy = st.builds(
    VorkursModel_RegistrationSystem,
)
VorkursModel_Address_strategy = st.builds(
    VorkursModel_Address,
    state=
        safe_text,
    zip=
        safe_text,
    street=
        safe_text,
    city=
        safe_text
)
VorkursModel_Qualification_strategy = st.builds(
    VorkursModel_Qualification,
    hasProgrammingExperience=
        st.booleans(),
    Language=
        safe_text,
    programminLanguage=
        safe_text,
    hasPCExperience=
        st.booleans()
)
VorkursModel_Notebook_strategy = st.builds(
    VorkursModel_Notebook,
    OperatingSystem=
        safe_text,
    hasWLAN=
        st.booleans()
)

@given(instance=VorkursModel_Room_strategy)
@settings(max_examples=50)
def test_vorkursmodel_room_instantiation(instance):
    assert isinstance(instance, VorkursModel_Room)



@given(instance=VorkursModel_Room_strategy)
def test_vorkursmodel_room_hasComputers_setter(instance):
    original = instance.hasComputers
    instance.hasComputers = original
    assert instance.hasComputers == original



@given(instance=VorkursModel_Room_strategy)
def test_vorkursmodel_room_seats_setter(instance):
    original = instance.seats
    instance.seats = original
    assert instance.seats == original



@given(instance=VorkursModel_Room_strategy)
def test_vorkursmodel_room_roomNr_setter(instance):
    original = instance.roomNr
    instance.roomNr = original
    assert instance.roomNr == original



@given(instance=VorkursModel_Room_strategy)
def test_vorkursmodel_room_sockets_setter(instance):
    original = instance.sockets
    instance.sockets = original
    assert instance.sockets == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=VorkursModel_Contact_strategy)
@settings(max_examples=50)
def test_vorkursmodel_contact_instantiation(instance):
    assert isinstance(instance, VorkursModel_Contact)



@given(instance=VorkursModel_Contact_strategy)
def test_vorkursmodel_contact_phonenumber_setter(instance):
    original = instance.phonenumber
    instance.phonenumber = original
    assert instance.phonenumber == original



@given(instance=VorkursModel_Contact_strategy)
def test_vorkursmodel_contact_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=VorkursModel_Person_strategy)
@settings(max_examples=50)
def test_vorkursmodel_person_instantiation(instance):
    assert isinstance(instance, VorkursModel_Person)



@given(instance=VorkursModel_Person_strategy)
def test_vorkursmodel_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=VorkursModel_Person_strategy)
def test_vorkursmodel_person_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=VorkursModel_Person_strategy)
def test_vorkursmodel_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=VorkursModel_Person_strategy)
def test_vorkursmodel_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=VorkursModel_TeachingAssistant_strategy)
@settings(max_examples=50)
def test_vorkursmodel_teachingassistant_instantiation(instance):
    assert isinstance(instance, VorkursModel_TeachingAssistant)

@given(instance=VorkursModel_Student_strategy)
@settings(max_examples=50)
def test_vorkursmodel_student_instantiation(instance):
    assert isinstance(instance, VorkursModel_Student)

@given(instance=VorkursModel_RegistrationSystem_strategy)
@settings(max_examples=50)
def test_vorkursmodel_registrationsystem_instantiation(instance):
    assert isinstance(instance, VorkursModel_RegistrationSystem)

@given(instance=VorkursModel_Address_strategy)
@settings(max_examples=50)
def test_vorkursmodel_address_instantiation(instance):
    assert isinstance(instance, VorkursModel_Address)



@given(instance=VorkursModel_Address_strategy)
def test_vorkursmodel_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=VorkursModel_Address_strategy)
def test_vorkursmodel_address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=VorkursModel_Address_strategy)
def test_vorkursmodel_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=VorkursModel_Address_strategy)
def test_vorkursmodel_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=VorkursModel_Qualification_strategy)
@settings(max_examples=50)
def test_vorkursmodel_qualification_instantiation(instance):
    assert isinstance(instance, VorkursModel_Qualification)



@given(instance=VorkursModel_Qualification_strategy)
def test_vorkursmodel_qualification_hasProgrammingExperience_setter(instance):
    original = instance.hasProgrammingExperience
    instance.hasProgrammingExperience = original
    assert instance.hasProgrammingExperience == original



@given(instance=VorkursModel_Qualification_strategy)
def test_vorkursmodel_qualification_Language_setter(instance):
    original = instance.Language
    instance.Language = original
    assert instance.Language == original



@given(instance=VorkursModel_Qualification_strategy)
def test_vorkursmodel_qualification_programminLanguage_setter(instance):
    original = instance.programminLanguage
    instance.programminLanguage = original
    assert instance.programminLanguage == original



@given(instance=VorkursModel_Qualification_strategy)
def test_vorkursmodel_qualification_hasPCExperience_setter(instance):
    original = instance.hasPCExperience
    instance.hasPCExperience = original
    assert instance.hasPCExperience == original

@given(instance=VorkursModel_Notebook_strategy)
@settings(max_examples=50)
def test_vorkursmodel_notebook_instantiation(instance):
    assert isinstance(instance, VorkursModel_Notebook)



@given(instance=VorkursModel_Notebook_strategy)
def test_vorkursmodel_notebook_OperatingSystem_setter(instance):
    original = instance.OperatingSystem
    instance.OperatingSystem = original
    assert instance.OperatingSystem == original



@given(instance=VorkursModel_Notebook_strategy)
def test_vorkursmodel_notebook_hasWLAN_setter(instance):
    original = instance.hasWLAN
    instance.hasWLAN = original
    assert instance.hasWLAN == original
