import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VorkursModel::Address,
    VorkursModel::Qualification,
    VorkursModel::Notebook,
    VorkursModel::Contact,
    VorkursModel::Person,
    VorkursModel::Room,
    Person,
    VorkursModel::TeachingAssistant,
    VorkursModel::Student,
    VorkursModel::RegistrationSystem,
    OperatingSystem,
    Nationality,
    Gender,
    Subject,
    ProgrammingLanguage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vorkursmodel::address_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Address)


def test_vorkursmodel::address_constructor_exists():
    assert callable(VorkursModel::Address.__init__)


def test_vorkursmodel::address_constructor_args():
    sig = inspect.signature(VorkursModel::Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "state" in params, "Missing parameter 'state'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "city" in params, "Missing parameter 'city'"

def test_vorkursmodel::address_has_street():
    assert hasattr(VorkursModel::Address, "street")
    descriptor = None
    for klass in VorkursModel::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::address_has_state():
    assert hasattr(VorkursModel::Address, "state")
    descriptor = None
    for klass in VorkursModel::Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::address_has_zip():
    assert hasattr(VorkursModel::Address, "zip")
    descriptor = None
    for klass in VorkursModel::Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::address_has_city():
    assert hasattr(VorkursModel::Address, "city")
    descriptor = None
    for klass in VorkursModel::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel::qualification_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Qualification)


def test_vorkursmodel::qualification_constructor_exists():
    assert callable(VorkursModel::Qualification.__init__)


def test_vorkursmodel::qualification_constructor_args():
    sig = inspect.signature(VorkursModel::Qualification.__init__)
    params = list(sig.parameters.keys())
    assert "hasProgrammingExperience" in params, "Missing parameter 'hasProgrammingExperience'"
    assert "programminLanguage" in params, "Missing parameter 'programminLanguage'"
    assert "hasPCExperience" in params, "Missing parameter 'hasPCExperience'"
    assert "Language" in params, "Missing parameter 'Language'"

def test_vorkursmodel::qualification_has_hasProgrammingExperience():
    assert hasattr(VorkursModel::Qualification, "hasProgrammingExperience")
    descriptor = None
    for klass in VorkursModel::Qualification.__mro__:
        if "hasProgrammingExperience" in klass.__dict__:
            descriptor = klass.__dict__["hasProgrammingExperience"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::qualification_has_programminLanguage():
    assert hasattr(VorkursModel::Qualification, "programminLanguage")
    descriptor = None
    for klass in VorkursModel::Qualification.__mro__:
        if "programminLanguage" in klass.__dict__:
            descriptor = klass.__dict__["programminLanguage"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::qualification_has_hasPCExperience():
    assert hasattr(VorkursModel::Qualification, "hasPCExperience")
    descriptor = None
    for klass in VorkursModel::Qualification.__mro__:
        if "hasPCExperience" in klass.__dict__:
            descriptor = klass.__dict__["hasPCExperience"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::qualification_has_Language():
    assert hasattr(VorkursModel::Qualification, "Language")
    descriptor = None
    for klass in VorkursModel::Qualification.__mro__:
        if "Language" in klass.__dict__:
            descriptor = klass.__dict__["Language"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel::notebook_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Notebook)


def test_vorkursmodel::notebook_constructor_exists():
    assert callable(VorkursModel::Notebook.__init__)


def test_vorkursmodel::notebook_constructor_args():
    sig = inspect.signature(VorkursModel::Notebook.__init__)
    params = list(sig.parameters.keys())
    assert "OperatingSystem" in params, "Missing parameter 'OperatingSystem'"
    assert "hasWLAN" in params, "Missing parameter 'hasWLAN'"

def test_vorkursmodel::notebook_has_OperatingSystem():
    assert hasattr(VorkursModel::Notebook, "OperatingSystem")
    descriptor = None
    for klass in VorkursModel::Notebook.__mro__:
        if "OperatingSystem" in klass.__dict__:
            descriptor = klass.__dict__["OperatingSystem"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::notebook_has_hasWLAN():
    assert hasattr(VorkursModel::Notebook, "hasWLAN")
    descriptor = None
    for klass in VorkursModel::Notebook.__mro__:
        if "hasWLAN" in klass.__dict__:
            descriptor = klass.__dict__["hasWLAN"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel::contact_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Contact)


def test_vorkursmodel::contact_constructor_exists():
    assert callable(VorkursModel::Contact.__init__)


def test_vorkursmodel::contact_constructor_args():
    sig = inspect.signature(VorkursModel::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "phonenumber" in params, "Missing parameter 'phonenumber'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_vorkursmodel::contact_has_phonenumber():
    assert hasattr(VorkursModel::Contact, "phonenumber")
    descriptor = None
    for klass in VorkursModel::Contact.__mro__:
        if "phonenumber" in klass.__dict__:
            descriptor = klass.__dict__["phonenumber"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::contact_has_Email():
    assert hasattr(VorkursModel::Contact, "Email")
    descriptor = None
    for klass in VorkursModel::Contact.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel::person_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Person)


def test_vorkursmodel::person_constructor_exists():
    assert callable(VorkursModel::Person.__init__)


def test_vorkursmodel::person_constructor_args():
    sig = inspect.signature(VorkursModel::Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_vorkursmodel::person_has_gender():
    assert hasattr(VorkursModel::Person, "gender")
    descriptor = None
    for klass in VorkursModel::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::person_has_firstname():
    assert hasattr(VorkursModel::Person, "firstname")
    descriptor = None
    for klass in VorkursModel::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::person_has_subject():
    assert hasattr(VorkursModel::Person, "subject")
    descriptor = None
    for klass in VorkursModel::Person.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::person_has_lastname():
    assert hasattr(VorkursModel::Person, "lastname")
    descriptor = None
    for klass in VorkursModel::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_vorkursmodel::room_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Room)


def test_vorkursmodel::room_constructor_exists():
    assert callable(VorkursModel::Room.__init__)


def test_vorkursmodel::room_constructor_args():
    sig = inspect.signature(VorkursModel::Room.__init__)
    params = list(sig.parameters.keys())
    assert "hasComputers" in params, "Missing parameter 'hasComputers'"
    assert "roomNr" in params, "Missing parameter 'roomNr'"
    assert "sockets" in params, "Missing parameter 'sockets'"
    assert "seats" in params, "Missing parameter 'seats'"

def test_vorkursmodel::room_has_hasComputers():
    assert hasattr(VorkursModel::Room, "hasComputers")
    descriptor = None
    for klass in VorkursModel::Room.__mro__:
        if "hasComputers" in klass.__dict__:
            descriptor = klass.__dict__["hasComputers"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::room_has_roomNr():
    assert hasattr(VorkursModel::Room, "roomNr")
    descriptor = None
    for klass in VorkursModel::Room.__mro__:
        if "roomNr" in klass.__dict__:
            descriptor = klass.__dict__["roomNr"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::room_has_sockets():
    assert hasattr(VorkursModel::Room, "sockets")
    descriptor = None
    for klass in VorkursModel::Room.__mro__:
        if "sockets" in klass.__dict__:
            descriptor = klass.__dict__["sockets"]
            break
    assert isinstance(descriptor, property)

def test_vorkursmodel::room_has_seats():
    assert hasattr(VorkursModel::Room, "seats")
    descriptor = None
    for klass in VorkursModel::Room.__mro__:
        if "seats" in klass.__dict__:
            descriptor = klass.__dict__["seats"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel::teachingassistant_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::TeachingAssistant)


def test_vorkursmodel::teachingassistant_constructor_exists():
    assert callable(VorkursModel::TeachingAssistant.__init__)


def test_vorkursmodel::teachingassistant_constructor_args():
    sig = inspect.signature(VorkursModel::TeachingAssistant.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel::student_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::Student)


def test_vorkursmodel::student_constructor_exists():
    assert callable(VorkursModel::Student.__init__)


def test_vorkursmodel::student_constructor_args():
    sig = inspect.signature(VorkursModel::Student.__init__)
    params = list(sig.parameters.keys())



def test_vorkursmodel::registrationsystem_is_not_abstract():
    assert not inspect.isabstract(VorkursModel::RegistrationSystem)


def test_vorkursmodel::registrationsystem_constructor_exists():
    assert callable(VorkursModel::RegistrationSystem.__init__)


def test_vorkursmodel::registrationsystem_constructor_args():
    sig = inspect.signature(VorkursModel::RegistrationSystem.__init__)
    params = list(sig.parameters.keys())

def test_operatingsystem_exists():
    # Check that the Enumeration exists
    assert OperatingSystem is not None

def test_operatingsystem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatingSystem]
    expected_literals = [
        "other",
        "Linux_Unix",
        "MacOS",
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
        "other",
        "French",
        "German",
        "English",
        "Spanish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nationality"

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Male",
        "Female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"

def test_subject_exists():
    # Check that the Enumeration exists
    assert Subject is not None

def test_subject_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Subject]
    expected_literals = [
        "ComputerScience",
        "Physics",
        "BusinessEngineering",
        "CES",
        "Mathematics",
        "AppliedGeographics",
        "MechanicalEngineering",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Subject"

def test_programminglanguage_exists():
    # Check that the Enumeration exists
    assert ProgrammingLanguage is not None

def test_programminglanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammingLanguage]
    expected_literals = [
        "C_CPP",
        "other",
        "Java",
        "Pascal_Delphi",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammingLanguage"


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
VorkursModel::Address_strategy = st.builds(
    VorkursModel::Address,
    street=
        safe_text,
    state=
        safe_text,
    zip=
        safe_text,
    city=
        safe_text
)
VorkursModel::Qualification_strategy = st.builds(
    VorkursModel::Qualification,
    hasProgrammingExperience=
        st.booleans(),
    programminLanguage=
        safe_text,
    hasPCExperience=
        st.booleans(),
    Language=
        safe_text
)
VorkursModel::Notebook_strategy = st.builds(
    VorkursModel::Notebook,
    OperatingSystem=
        safe_text,
    hasWLAN=
        st.booleans()
)
VorkursModel::Contact_strategy = st.builds(
    VorkursModel::Contact,
    phonenumber=
        safe_text,
    Email=
        safe_text
)
VorkursModel::Person_strategy = st.builds(
    VorkursModel::Person,
    gender=
        safe_text,
    firstname=
        safe_text,
    subject=
        safe_text,
    lastname=
        safe_text
)
VorkursModel::Room_strategy = st.builds(
    VorkursModel::Room,
    hasComputers=
        st.booleans(),
    roomNr=
        st.integers(),
    sockets=
        st.booleans(),
    seats=
        st.integers()
)
Person_strategy = st.builds(
    Person,
)
VorkursModel::TeachingAssistant_strategy = st.builds(
    VorkursModel::TeachingAssistant,
)
VorkursModel::Student_strategy = st.builds(
    VorkursModel::Student,
)
VorkursModel::RegistrationSystem_strategy = st.builds(
    VorkursModel::RegistrationSystem,
)

@given(instance=VorkursModel::Address_strategy)
@settings(max_examples=50)
def test_vorkursmodel::address_instantiation(instance):
    assert isinstance(instance, VorkursModel::Address)

@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_zip_type(instance):
    assert isinstance(instance.zip, str)


@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=VorkursModel::Address_strategy)
def test_vorkursmodel::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=VorkursModel::Qualification_strategy)
@settings(max_examples=50)
def test_vorkursmodel::qualification_instantiation(instance):
    assert isinstance(instance, VorkursModel::Qualification)

@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_hasProgrammingExperience_type(instance):
    assert isinstance(instance.hasProgrammingExperience, bool)


@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_hasProgrammingExperience_setter(instance):
    original = instance.hasProgrammingExperience
    instance.hasProgrammingExperience = original
    assert instance.hasProgrammingExperience == original

@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_programminLanguage_type(instance):
    assert isinstance(instance.programminLanguage, str)


@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_programminLanguage_setter(instance):
    original = instance.programminLanguage
    instance.programminLanguage = original
    assert instance.programminLanguage == original

@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_hasPCExperience_type(instance):
    assert isinstance(instance.hasPCExperience, bool)


@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_hasPCExperience_setter(instance):
    original = instance.hasPCExperience
    instance.hasPCExperience = original
    assert instance.hasPCExperience == original

@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_Language_type(instance):
    assert isinstance(instance.Language, str)


@given(instance=VorkursModel::Qualification_strategy)
def test_vorkursmodel::qualification_Language_setter(instance):
    original = instance.Language
    instance.Language = original
    assert instance.Language == original

@given(instance=VorkursModel::Notebook_strategy)
@settings(max_examples=50)
def test_vorkursmodel::notebook_instantiation(instance):
    assert isinstance(instance, VorkursModel::Notebook)

@given(instance=VorkursModel::Notebook_strategy)
def test_vorkursmodel::notebook_OperatingSystem_type(instance):
    assert isinstance(instance.OperatingSystem, str)


@given(instance=VorkursModel::Notebook_strategy)
def test_vorkursmodel::notebook_OperatingSystem_setter(instance):
    original = instance.OperatingSystem
    instance.OperatingSystem = original
    assert instance.OperatingSystem == original

@given(instance=VorkursModel::Notebook_strategy)
def test_vorkursmodel::notebook_hasWLAN_type(instance):
    assert isinstance(instance.hasWLAN, bool)


@given(instance=VorkursModel::Notebook_strategy)
def test_vorkursmodel::notebook_hasWLAN_setter(instance):
    original = instance.hasWLAN
    instance.hasWLAN = original
    assert instance.hasWLAN == original

@given(instance=VorkursModel::Contact_strategy)
@settings(max_examples=50)
def test_vorkursmodel::contact_instantiation(instance):
    assert isinstance(instance, VorkursModel::Contact)

@given(instance=VorkursModel::Contact_strategy)
def test_vorkursmodel::contact_phonenumber_type(instance):
    assert isinstance(instance.phonenumber, str)


@given(instance=VorkursModel::Contact_strategy)
def test_vorkursmodel::contact_phonenumber_setter(instance):
    original = instance.phonenumber
    instance.phonenumber = original
    assert instance.phonenumber == original

@given(instance=VorkursModel::Contact_strategy)
def test_vorkursmodel::contact_Email_type(instance):
    assert isinstance(instance.Email, str)


@given(instance=VorkursModel::Contact_strategy)
def test_vorkursmodel::contact_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=VorkursModel::Person_strategy)
@settings(max_examples=50)
def test_vorkursmodel::person_instantiation(instance):
    assert isinstance(instance, VorkursModel::Person)

@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=VorkursModel::Person_strategy)
def test_vorkursmodel::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=VorkursModel::Room_strategy)
@settings(max_examples=50)
def test_vorkursmodel::room_instantiation(instance):
    assert isinstance(instance, VorkursModel::Room)

@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_hasComputers_type(instance):
    assert isinstance(instance.hasComputers, bool)


@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_hasComputers_setter(instance):
    original = instance.hasComputers
    instance.hasComputers = original
    assert instance.hasComputers == original

@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_roomNr_type(instance):
    assert isinstance(instance.roomNr, int)


@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_roomNr_setter(instance):
    original = instance.roomNr
    instance.roomNr = original
    assert instance.roomNr == original

@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_sockets_type(instance):
    assert isinstance(instance.sockets, bool)


@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_sockets_setter(instance):
    original = instance.sockets
    instance.sockets = original
    assert instance.sockets == original

@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_seats_type(instance):
    assert isinstance(instance.seats, int)


@given(instance=VorkursModel::Room_strategy)
def test_vorkursmodel::room_seats_setter(instance):
    original = instance.seats
    instance.seats = original
    assert instance.seats == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=VorkursModel::TeachingAssistant_strategy)
@settings(max_examples=50)
def test_vorkursmodel::teachingassistant_instantiation(instance):
    assert isinstance(instance, VorkursModel::TeachingAssistant)

@given(instance=VorkursModel::Student_strategy)
@settings(max_examples=50)
def test_vorkursmodel::student_instantiation(instance):
    assert isinstance(instance, VorkursModel::Student)

@given(instance=VorkursModel::RegistrationSystem_strategy)
@settings(max_examples=50)
def test_vorkursmodel::registrationsystem_instantiation(instance):
    assert isinstance(instance, VorkursModel::RegistrationSystem)
