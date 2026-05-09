import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gedcoml::Address,
    Source,
    gedcoml::PersonRef,
    gedcoml::Others,
    Person,
    gedcoml::UnbekanntePerson,
    gedcoml::BekanntePerson,
    gedcoml::Person,
    gedcoml::Family,
    gedcoml::Author,
    Address,
    gedcoml::PostAddress,
    gedcoml::FamilyBook,
    gedcoml::Source,
    gedcoml::Note,
    gedcoml::Married,
    gedcoml::FamilyImport,
    gedcoml::Projectdescription,
    Sexus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gedcoml::address_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Address)


def test_gedcoml::address_constructor_exists():
    assert callable(gedcoml::Address.__init__)


def test_gedcoml::address_constructor_args():
    sig = inspect.signature(gedcoml::Address.__init__)
    params = list(sig.parameters.keys())
    assert "exodus" in params, "Missing parameter 'exodus'"
    assert "entry" in params, "Missing parameter 'entry'"

def test_gedcoml::address_has_exodus():
    assert hasattr(gedcoml::Address, "exodus")
    descriptor = None
    for klass in gedcoml::Address.__mro__:
        if "exodus" in klass.__dict__:
            descriptor = klass.__dict__["exodus"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::address_has_entry():
    assert hasattr(gedcoml::Address, "entry")
    descriptor = None
    for klass in gedcoml::Address.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::personref_is_not_abstract():
    assert not inspect.isabstract(gedcoml::PersonRef)


def test_gedcoml::personref_constructor_exists():
    assert callable(gedcoml::PersonRef.__init__)


def test_gedcoml::personref_constructor_args():
    sig = inspect.signature(gedcoml::PersonRef.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::others_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Others)


def test_gedcoml::others_constructor_exists():
    assert callable(gedcoml::Others.__init__)


def test_gedcoml::others_constructor_args():
    sig = inspect.signature(gedcoml::Others.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_gedcoml::others_has_description():
    assert hasattr(gedcoml::Others, "description")
    descriptor = None
    for klass in gedcoml::Others.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::unbekannteperson_is_not_abstract():
    assert not inspect.isabstract(gedcoml::UnbekanntePerson)


def test_gedcoml::unbekannteperson_constructor_exists():
    assert callable(gedcoml::UnbekanntePerson.__init__)


def test_gedcoml::unbekannteperson_constructor_args():
    sig = inspect.signature(gedcoml::UnbekanntePerson.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::bekannteperson_is_not_abstract():
    assert not inspect.isabstract(gedcoml::BekanntePerson)


def test_gedcoml::bekannteperson_constructor_exists():
    assert callable(gedcoml::BekanntePerson.__init__)


def test_gedcoml::bekannteperson_constructor_args():
    sig = inspect.signature(gedcoml::BekanntePerson.__init__)
    params = list(sig.parameters.keys())
    assert "birthDay" in params, "Missing parameter 'birthDay'"
    assert "deathDay" in params, "Missing parameter 'deathDay'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "birthName" in params, "Missing parameter 'birthName'"

def test_gedcoml::bekannteperson_has_birthDay():
    assert hasattr(gedcoml::BekanntePerson, "birthDay")
    descriptor = None
    for klass in gedcoml::BekanntePerson.__mro__:
        if "birthDay" in klass.__dict__:
            descriptor = klass.__dict__["birthDay"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::bekannteperson_has_deathDay():
    assert hasattr(gedcoml::BekanntePerson, "deathDay")
    descriptor = None
    for klass in gedcoml::BekanntePerson.__mro__:
        if "deathDay" in klass.__dict__:
            descriptor = klass.__dict__["deathDay"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::bekannteperson_has_lastName():
    assert hasattr(gedcoml::BekanntePerson, "lastName")
    descriptor = None
    for klass in gedcoml::BekanntePerson.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::bekannteperson_has_middleName():
    assert hasattr(gedcoml::BekanntePerson, "middleName")
    descriptor = None
    for klass in gedcoml::BekanntePerson.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::bekannteperson_has_firstName():
    assert hasattr(gedcoml::BekanntePerson, "firstName")
    descriptor = None
    for klass in gedcoml::BekanntePerson.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::bekannteperson_has_birthName():
    assert hasattr(gedcoml::BekanntePerson, "birthName")
    descriptor = None
    for klass in gedcoml::BekanntePerson.__mro__:
        if "birthName" in klass.__dict__:
            descriptor = klass.__dict__["birthName"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml::person_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Person)


def test_gedcoml::person_constructor_exists():
    assert callable(gedcoml::Person.__init__)


def test_gedcoml::person_constructor_args():
    sig = inspect.signature(gedcoml::Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_gedcoml::person_has_id():
    assert hasattr(gedcoml::Person, "id")
    descriptor = None
    for klass in gedcoml::Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::person_has_sex():
    assert hasattr(gedcoml::Person, "sex")
    descriptor = None
    for klass in gedcoml::Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml::family_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Family)


def test_gedcoml::family_constructor_exists():
    assert callable(gedcoml::Family.__init__)


def test_gedcoml::family_constructor_args():
    sig = inspect.signature(gedcoml::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gedcoml::family_has_name():
    assert hasattr(gedcoml::Family, "name")
    descriptor = None
    for klass in gedcoml::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml::author_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Author)


def test_gedcoml::author_constructor_exists():
    assert callable(gedcoml::Author.__init__)


def test_gedcoml::author_constructor_args():
    sig = inspect.signature(gedcoml::Author.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_gedcoml::author_has_lastName():
    assert hasattr(gedcoml::Author, "lastName")
    descriptor = None
    for klass in gedcoml::Author.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::author_has_firstName():
    assert hasattr(gedcoml::Author, "firstName")
    descriptor = None
    for klass in gedcoml::Author.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::postaddress_is_not_abstract():
    assert not inspect.isabstract(gedcoml::PostAddress)


def test_gedcoml::postaddress_constructor_exists():
    assert callable(gedcoml::PostAddress.__init__)


def test_gedcoml::postaddress_constructor_args():
    sig = inspect.signature(gedcoml::PostAddress.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "postcode" in params, "Missing parameter 'postcode'"
    assert "city" in params, "Missing parameter 'city'"

def test_gedcoml::postaddress_has_street():
    assert hasattr(gedcoml::PostAddress, "street")
    descriptor = None
    for klass in gedcoml::PostAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::postaddress_has_postcode():
    assert hasattr(gedcoml::PostAddress, "postcode")
    descriptor = None
    for klass in gedcoml::PostAddress.__mro__:
        if "postcode" in klass.__dict__:
            descriptor = klass.__dict__["postcode"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::postaddress_has_city():
    assert hasattr(gedcoml::PostAddress, "city")
    descriptor = None
    for klass in gedcoml::PostAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml::familybook_is_not_abstract():
    assert not inspect.isabstract(gedcoml::FamilyBook)


def test_gedcoml::familybook_constructor_exists():
    assert callable(gedcoml::FamilyBook.__init__)


def test_gedcoml::familybook_constructor_args():
    sig = inspect.signature(gedcoml::FamilyBook.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::source_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Source)


def test_gedcoml::source_constructor_exists():
    assert callable(gedcoml::Source.__init__)


def test_gedcoml::source_constructor_args():
    sig = inspect.signature(gedcoml::Source.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::note_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Note)


def test_gedcoml::note_constructor_exists():
    assert callable(gedcoml::Note.__init__)


def test_gedcoml::note_constructor_args():
    sig = inspect.signature(gedcoml::Note.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_gedcoml::note_has_content():
    assert hasattr(gedcoml::Note, "content")
    descriptor = None
    for klass in gedcoml::Note.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml::married_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Married)


def test_gedcoml::married_constructor_exists():
    assert callable(gedcoml::Married.__init__)


def test_gedcoml::married_constructor_args():
    sig = inspect.signature(gedcoml::Married.__init__)
    params = list(sig.parameters.keys())
    assert "separationDay" in params, "Missing parameter 'separationDay'"
    assert "weddingDay" in params, "Missing parameter 'weddingDay'"

def test_gedcoml::married_has_separationDay():
    assert hasattr(gedcoml::Married, "separationDay")
    descriptor = None
    for klass in gedcoml::Married.__mro__:
        if "separationDay" in klass.__dict__:
            descriptor = klass.__dict__["separationDay"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::married_has_weddingDay():
    assert hasattr(gedcoml::Married, "weddingDay")
    descriptor = None
    for klass in gedcoml::Married.__mro__:
        if "weddingDay" in klass.__dict__:
            descriptor = klass.__dict__["weddingDay"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml::familyimport_is_not_abstract():
    assert not inspect.isabstract(gedcoml::FamilyImport)


def test_gedcoml::familyimport_constructor_exists():
    assert callable(gedcoml::FamilyImport.__init__)


def test_gedcoml::familyimport_constructor_args():
    sig = inspect.signature(gedcoml::FamilyImport.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml::projectdescription_is_not_abstract():
    assert not inspect.isabstract(gedcoml::Projectdescription)


def test_gedcoml::projectdescription_constructor_exists():
    assert callable(gedcoml::Projectdescription.__init__)


def test_gedcoml::projectdescription_constructor_args():
    sig = inspect.signature(gedcoml::Projectdescription.__init__)
    params = list(sig.parameters.keys())
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "version" in params, "Missing parameter 'version'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "publishingDate" in params, "Missing parameter 'publishingDate'"

def test_gedcoml::projectdescription_has_groupId():
    assert hasattr(gedcoml::Projectdescription, "groupId")
    descriptor = None
    for klass in gedcoml::Projectdescription.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::projectdescription_has_version():
    assert hasattr(gedcoml::Projectdescription, "version")
    descriptor = None
    for klass in gedcoml::Projectdescription.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::projectdescription_has_artifactId():
    assert hasattr(gedcoml::Projectdescription, "artifactId")
    descriptor = None
    for klass in gedcoml::Projectdescription.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml::projectdescription_has_publishingDate():
    assert hasattr(gedcoml::Projectdescription, "publishingDate")
    descriptor = None
    for klass in gedcoml::Projectdescription.__mro__:
        if "publishingDate" in klass.__dict__:
            descriptor = klass.__dict__["publishingDate"]
            break
    assert isinstance(descriptor, property)

def test_sexus_exists():
    # Check that the Enumeration exists
    assert Sexus is not None

def test_sexus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sexus]
    expected_literals = [
        "female",
        "male",
        "undefined",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sexus"


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
gedcoml::Address_strategy = st.builds(
    gedcoml::Address,
    exodus=
        safe_text,
    entry=
        safe_text
)
Source_strategy = st.builds(
    Source,
)
gedcoml::PersonRef_strategy = st.builds(
    gedcoml::PersonRef,
)
gedcoml::Others_strategy = st.builds(
    gedcoml::Others,
    description=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
gedcoml::UnbekanntePerson_strategy = st.builds(
    gedcoml::UnbekanntePerson,
)
gedcoml::BekanntePerson_strategy = st.builds(
    gedcoml::BekanntePerson,
    birthDay=
        safe_text,
    deathDay=
        safe_text,
    lastName=
        safe_text,
    middleName=
        safe_text,
    firstName=
        safe_text,
    birthName=
        safe_text
)
gedcoml::Person_strategy = st.builds(
    gedcoml::Person,
    id=
        safe_text,
    sex=
        safe_text
)
gedcoml::Family_strategy = st.builds(
    gedcoml::Family,
    name=
        safe_text
)
gedcoml::Author_strategy = st.builds(
    gedcoml::Author,
    lastName=
        safe_text,
    firstName=
        safe_text
)
Address_strategy = st.builds(
    Address,
)
gedcoml::PostAddress_strategy = st.builds(
    gedcoml::PostAddress,
    street=
        safe_text,
    postcode=
        safe_text,
    city=
        safe_text
)
gedcoml::FamilyBook_strategy = st.builds(
    gedcoml::FamilyBook,
)
gedcoml::Source_strategy = st.builds(
    gedcoml::Source,
)
gedcoml::Note_strategy = st.builds(
    gedcoml::Note,
    content=
        safe_text
)
gedcoml::Married_strategy = st.builds(
    gedcoml::Married,
    separationDay=
        safe_text,
    weddingDay=
        safe_text
)
gedcoml::FamilyImport_strategy = st.builds(
    gedcoml::FamilyImport,
)
gedcoml::Projectdescription_strategy = st.builds(
    gedcoml::Projectdescription,
    groupId=
        safe_text,
    version=
        safe_text,
    artifactId=
        safe_text,
    publishingDate=
        safe_text
)

@given(instance=gedcoml::Address_strategy)
@settings(max_examples=50)
def test_gedcoml::address_instantiation(instance):
    assert isinstance(instance, gedcoml::Address)

@given(instance=gedcoml::Address_strategy)
def test_gedcoml::address_exodus_type(instance):
    assert isinstance(instance.exodus, str)


@given(instance=gedcoml::Address_strategy)
def test_gedcoml::address_exodus_setter(instance):
    original = instance.exodus
    instance.exodus = original
    assert instance.exodus == original

@given(instance=gedcoml::Address_strategy)
def test_gedcoml::address_entry_type(instance):
    assert isinstance(instance.entry, str)


@given(instance=gedcoml::Address_strategy)
def test_gedcoml::address_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=gedcoml::PersonRef_strategy)
@settings(max_examples=50)
def test_gedcoml::personref_instantiation(instance):
    assert isinstance(instance, gedcoml::PersonRef)

@given(instance=gedcoml::Others_strategy)
@settings(max_examples=50)
def test_gedcoml::others_instantiation(instance):
    assert isinstance(instance, gedcoml::Others)

@given(instance=gedcoml::Others_strategy)
def test_gedcoml::others_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=gedcoml::Others_strategy)
def test_gedcoml::others_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=gedcoml::UnbekanntePerson_strategy)
@settings(max_examples=50)
def test_gedcoml::unbekannteperson_instantiation(instance):
    assert isinstance(instance, gedcoml::UnbekanntePerson)

@given(instance=gedcoml::BekanntePerson_strategy)
@settings(max_examples=50)
def test_gedcoml::bekannteperson_instantiation(instance):
    assert isinstance(instance, gedcoml::BekanntePerson)

@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_birthDay_type(instance):
    assert isinstance(instance.birthDay, str)


@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_birthDay_setter(instance):
    original = instance.birthDay
    instance.birthDay = original
    assert instance.birthDay == original

@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_deathDay_type(instance):
    assert isinstance(instance.deathDay, str)


@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_deathDay_setter(instance):
    original = instance.deathDay
    instance.deathDay = original
    assert instance.deathDay == original

@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_middleName_type(instance):
    assert isinstance(instance.middleName, str)


@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original

@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_birthName_type(instance):
    assert isinstance(instance.birthName, str)


@given(instance=gedcoml::BekanntePerson_strategy)
def test_gedcoml::bekannteperson_birthName_setter(instance):
    original = instance.birthName
    instance.birthName = original
    assert instance.birthName == original

@given(instance=gedcoml::Person_strategy)
@settings(max_examples=50)
def test_gedcoml::person_instantiation(instance):
    assert isinstance(instance, gedcoml::Person)

@given(instance=gedcoml::Person_strategy)
def test_gedcoml::person_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=gedcoml::Person_strategy)
def test_gedcoml::person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gedcoml::Person_strategy)
def test_gedcoml::person_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=gedcoml::Person_strategy)
def test_gedcoml::person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=gedcoml::Family_strategy)
@settings(max_examples=50)
def test_gedcoml::family_instantiation(instance):
    assert isinstance(instance, gedcoml::Family)

@given(instance=gedcoml::Family_strategy)
def test_gedcoml::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gedcoml::Family_strategy)
def test_gedcoml::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gedcoml::Author_strategy)
@settings(max_examples=50)
def test_gedcoml::author_instantiation(instance):
    assert isinstance(instance, gedcoml::Author)

@given(instance=gedcoml::Author_strategy)
def test_gedcoml::author_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=gedcoml::Author_strategy)
def test_gedcoml::author_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=gedcoml::Author_strategy)
def test_gedcoml::author_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=gedcoml::Author_strategy)
def test_gedcoml::author_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=gedcoml::PostAddress_strategy)
@settings(max_examples=50)
def test_gedcoml::postaddress_instantiation(instance):
    assert isinstance(instance, gedcoml::PostAddress)

@given(instance=gedcoml::PostAddress_strategy)
def test_gedcoml::postaddress_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=gedcoml::PostAddress_strategy)
def test_gedcoml::postaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=gedcoml::PostAddress_strategy)
def test_gedcoml::postaddress_postcode_type(instance):
    assert isinstance(instance.postcode, str)


@given(instance=gedcoml::PostAddress_strategy)
def test_gedcoml::postaddress_postcode_setter(instance):
    original = instance.postcode
    instance.postcode = original
    assert instance.postcode == original

@given(instance=gedcoml::PostAddress_strategy)
def test_gedcoml::postaddress_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=gedcoml::PostAddress_strategy)
def test_gedcoml::postaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=gedcoml::FamilyBook_strategy)
@settings(max_examples=50)
def test_gedcoml::familybook_instantiation(instance):
    assert isinstance(instance, gedcoml::FamilyBook)

@given(instance=gedcoml::Source_strategy)
@settings(max_examples=50)
def test_gedcoml::source_instantiation(instance):
    assert isinstance(instance, gedcoml::Source)

@given(instance=gedcoml::Note_strategy)
@settings(max_examples=50)
def test_gedcoml::note_instantiation(instance):
    assert isinstance(instance, gedcoml::Note)

@given(instance=gedcoml::Note_strategy)
def test_gedcoml::note_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=gedcoml::Note_strategy)
def test_gedcoml::note_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=gedcoml::Married_strategy)
@settings(max_examples=50)
def test_gedcoml::married_instantiation(instance):
    assert isinstance(instance, gedcoml::Married)

@given(instance=gedcoml::Married_strategy)
def test_gedcoml::married_separationDay_type(instance):
    assert isinstance(instance.separationDay, str)


@given(instance=gedcoml::Married_strategy)
def test_gedcoml::married_separationDay_setter(instance):
    original = instance.separationDay
    instance.separationDay = original
    assert instance.separationDay == original

@given(instance=gedcoml::Married_strategy)
def test_gedcoml::married_weddingDay_type(instance):
    assert isinstance(instance.weddingDay, str)


@given(instance=gedcoml::Married_strategy)
def test_gedcoml::married_weddingDay_setter(instance):
    original = instance.weddingDay
    instance.weddingDay = original
    assert instance.weddingDay == original

@given(instance=gedcoml::FamilyImport_strategy)
@settings(max_examples=50)
def test_gedcoml::familyimport_instantiation(instance):
    assert isinstance(instance, gedcoml::FamilyImport)

@given(instance=gedcoml::Projectdescription_strategy)
@settings(max_examples=50)
def test_gedcoml::projectdescription_instantiation(instance):
    assert isinstance(instance, gedcoml::Projectdescription)

@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_groupId_type(instance):
    assert isinstance(instance.groupId, str)


@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original

@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_artifactId_type(instance):
    assert isinstance(instance.artifactId, str)


@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original

@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_publishingDate_type(instance):
    assert isinstance(instance.publishingDate, str)


@given(instance=gedcoml::Projectdescription_strategy)
def test_gedcoml::projectdescription_publishingDate_setter(instance):
    original = instance.publishingDate
    instance.publishingDate = original
    assert instance.publishingDate == original
