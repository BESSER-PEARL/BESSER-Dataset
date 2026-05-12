import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Source,
    gedcoml_PersonRef,
    gedcoml_Others,
    gedcoml_Address,
    gedcoml_Source,
    gedcoml_Note,
    gedcoml_Married,
    Person,
    gedcoml_UnbekanntePerson,
    gedcoml_BekanntePerson,
    gedcoml_Person,
    gedcoml_Family,
    gedcoml_Author,
    gedcoml_FamilyImport,
    Address,
    gedcoml_PostAddress,
    gedcoml_FamilyBook,
    gedcoml_Projectdescription,
    Sexus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_personref_is_not_abstract():
    assert not inspect.isabstract(gedcoml_PersonRef)


def test_gedcoml_personref_constructor_exists():
    assert callable(gedcoml_PersonRef.__init__)


def test_gedcoml_personref_constructor_args():
    sig = inspect.signature(gedcoml_PersonRef.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_others_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Others)


def test_gedcoml_others_constructor_exists():
    assert callable(gedcoml_Others.__init__)


def test_gedcoml_others_constructor_args():
    sig = inspect.signature(gedcoml_Others.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_gedcoml_others_has_description():
    assert hasattr(gedcoml_Others, "description")
    descriptor = None
    for klass in gedcoml_Others.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_address_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Address)


def test_gedcoml_address_constructor_exists():
    assert callable(gedcoml_Address.__init__)


def test_gedcoml_address_constructor_args():
    sig = inspect.signature(gedcoml_Address.__init__)
    params = list(sig.parameters.keys())
    assert "exodus" in params, "Missing parameter 'exodus'"
    assert "entry" in params, "Missing parameter 'entry'"

def test_gedcoml_address_has_exodus():
    assert hasattr(gedcoml_Address, "exodus")
    descriptor = None
    for klass in gedcoml_Address.__mro__:
        if "exodus" in klass.__dict__:
            descriptor = klass.__dict__["exodus"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_address_has_entry():
    assert hasattr(gedcoml_Address, "entry")
    descriptor = None
    for klass in gedcoml_Address.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_source_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Source)


def test_gedcoml_source_constructor_exists():
    assert callable(gedcoml_Source.__init__)


def test_gedcoml_source_constructor_args():
    sig = inspect.signature(gedcoml_Source.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_note_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Note)


def test_gedcoml_note_constructor_exists():
    assert callable(gedcoml_Note.__init__)


def test_gedcoml_note_constructor_args():
    sig = inspect.signature(gedcoml_Note.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_gedcoml_note_has_content():
    assert hasattr(gedcoml_Note, "content")
    descriptor = None
    for klass in gedcoml_Note.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_married_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Married)


def test_gedcoml_married_constructor_exists():
    assert callable(gedcoml_Married.__init__)


def test_gedcoml_married_constructor_args():
    sig = inspect.signature(gedcoml_Married.__init__)
    params = list(sig.parameters.keys())
    assert "weddingDay" in params, "Missing parameter 'weddingDay'"
    assert "separationDay" in params, "Missing parameter 'separationDay'"

def test_gedcoml_married_has_weddingDay():
    assert hasattr(gedcoml_Married, "weddingDay")
    descriptor = None
    for klass in gedcoml_Married.__mro__:
        if "weddingDay" in klass.__dict__:
            descriptor = klass.__dict__["weddingDay"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_married_has_separationDay():
    assert hasattr(gedcoml_Married, "separationDay")
    descriptor = None
    for klass in gedcoml_Married.__mro__:
        if "separationDay" in klass.__dict__:
            descriptor = klass.__dict__["separationDay"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_unbekannteperson_is_not_abstract():
    assert not inspect.isabstract(gedcoml_UnbekanntePerson)


def test_gedcoml_unbekannteperson_constructor_exists():
    assert callable(gedcoml_UnbekanntePerson.__init__)


def test_gedcoml_unbekannteperson_constructor_args():
    sig = inspect.signature(gedcoml_UnbekanntePerson.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_bekannteperson_is_not_abstract():
    assert not inspect.isabstract(gedcoml_BekanntePerson)


def test_gedcoml_bekannteperson_constructor_exists():
    assert callable(gedcoml_BekanntePerson.__init__)


def test_gedcoml_bekannteperson_constructor_args():
    sig = inspect.signature(gedcoml_BekanntePerson.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "birthName" in params, "Missing parameter 'birthName'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "birthDay" in params, "Missing parameter 'birthDay'"
    assert "deathDay" in params, "Missing parameter 'deathDay'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_gedcoml_bekannteperson_has_lastName():
    assert hasattr(gedcoml_BekanntePerson, "lastName")
    descriptor = None
    for klass in gedcoml_BekanntePerson.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_bekannteperson_has_birthName():
    assert hasattr(gedcoml_BekanntePerson, "birthName")
    descriptor = None
    for klass in gedcoml_BekanntePerson.__mro__:
        if "birthName" in klass.__dict__:
            descriptor = klass.__dict__["birthName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_bekannteperson_has_middleName():
    assert hasattr(gedcoml_BekanntePerson, "middleName")
    descriptor = None
    for klass in gedcoml_BekanntePerson.__mro__:
        if "middleName" in klass.__dict__:
            descriptor = klass.__dict__["middleName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_bekannteperson_has_birthDay():
    assert hasattr(gedcoml_BekanntePerson, "birthDay")
    descriptor = None
    for klass in gedcoml_BekanntePerson.__mro__:
        if "birthDay" in klass.__dict__:
            descriptor = klass.__dict__["birthDay"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_bekannteperson_has_deathDay():
    assert hasattr(gedcoml_BekanntePerson, "deathDay")
    descriptor = None
    for klass in gedcoml_BekanntePerson.__mro__:
        if "deathDay" in klass.__dict__:
            descriptor = klass.__dict__["deathDay"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_bekannteperson_has_firstName():
    assert hasattr(gedcoml_BekanntePerson, "firstName")
    descriptor = None
    for klass in gedcoml_BekanntePerson.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_person_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Person)


def test_gedcoml_person_constructor_exists():
    assert callable(gedcoml_Person.__init__)


def test_gedcoml_person_constructor_args():
    sig = inspect.signature(gedcoml_Person.__init__)
    params = list(sig.parameters.keys())
    assert "sex" in params, "Missing parameter 'sex'"
    assert "id" in params, "Missing parameter 'id'"

def test_gedcoml_person_has_sex():
    assert hasattr(gedcoml_Person, "sex")
    descriptor = None
    for klass in gedcoml_Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_person_has_id():
    assert hasattr(gedcoml_Person, "id")
    descriptor = None
    for klass in gedcoml_Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_family_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Family)


def test_gedcoml_family_constructor_exists():
    assert callable(gedcoml_Family.__init__)


def test_gedcoml_family_constructor_args():
    sig = inspect.signature(gedcoml_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gedcoml_family_has_name():
    assert hasattr(gedcoml_Family, "name")
    descriptor = None
    for klass in gedcoml_Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_author_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Author)


def test_gedcoml_author_constructor_exists():
    assert callable(gedcoml_Author.__init__)


def test_gedcoml_author_constructor_args():
    sig = inspect.signature(gedcoml_Author.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_gedcoml_author_has_lastName():
    assert hasattr(gedcoml_Author, "lastName")
    descriptor = None
    for klass in gedcoml_Author.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_author_has_firstName():
    assert hasattr(gedcoml_Author, "firstName")
    descriptor = None
    for klass in gedcoml_Author.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_familyimport_is_not_abstract():
    assert not inspect.isabstract(gedcoml_FamilyImport)


def test_gedcoml_familyimport_constructor_exists():
    assert callable(gedcoml_FamilyImport.__init__)


def test_gedcoml_familyimport_constructor_args():
    sig = inspect.signature(gedcoml_FamilyImport.__init__)
    params = list(sig.parameters.keys())



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_postaddress_is_not_abstract():
    assert not inspect.isabstract(gedcoml_PostAddress)


def test_gedcoml_postaddress_constructor_exists():
    assert callable(gedcoml_PostAddress.__init__)


def test_gedcoml_postaddress_constructor_args():
    sig = inspect.signature(gedcoml_PostAddress.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "postcode" in params, "Missing parameter 'postcode'"
    assert "street" in params, "Missing parameter 'street'"

def test_gedcoml_postaddress_has_city():
    assert hasattr(gedcoml_PostAddress, "city")
    descriptor = None
    for klass in gedcoml_PostAddress.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_postaddress_has_postcode():
    assert hasattr(gedcoml_PostAddress, "postcode")
    descriptor = None
    for klass in gedcoml_PostAddress.__mro__:
        if "postcode" in klass.__dict__:
            descriptor = klass.__dict__["postcode"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_postaddress_has_street():
    assert hasattr(gedcoml_PostAddress, "street")
    descriptor = None
    for klass in gedcoml_PostAddress.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)



def test_gedcoml_familybook_is_not_abstract():
    assert not inspect.isabstract(gedcoml_FamilyBook)


def test_gedcoml_familybook_constructor_exists():
    assert callable(gedcoml_FamilyBook.__init__)


def test_gedcoml_familybook_constructor_args():
    sig = inspect.signature(gedcoml_FamilyBook.__init__)
    params = list(sig.parameters.keys())



def test_gedcoml_projectdescription_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Projectdescription)


def test_gedcoml_projectdescription_constructor_exists():
    assert callable(gedcoml_Projectdescription.__init__)


def test_gedcoml_projectdescription_constructor_args():
    sig = inspect.signature(gedcoml_Projectdescription.__init__)
    params = list(sig.parameters.keys())
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "publishingDate" in params, "Missing parameter 'publishingDate'"
    assert "version" in params, "Missing parameter 'version'"

def test_gedcoml_projectdescription_has_artifactId():
    assert hasattr(gedcoml_Projectdescription, "artifactId")
    descriptor = None
    for klass in gedcoml_Projectdescription.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_projectdescription_has_groupId():
    assert hasattr(gedcoml_Projectdescription, "groupId")
    descriptor = None
    for klass in gedcoml_Projectdescription.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_projectdescription_has_publishingDate():
    assert hasattr(gedcoml_Projectdescription, "publishingDate")
    descriptor = None
    for klass in gedcoml_Projectdescription.__mro__:
        if "publishingDate" in klass.__dict__:
            descriptor = klass.__dict__["publishingDate"]
            break
    assert isinstance(descriptor, property)

def test_gedcoml_projectdescription_has_version():
    assert hasattr(gedcoml_Projectdescription, "version")
    descriptor = None
    for klass in gedcoml_Projectdescription.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sexus_exists():
    # Check that the Enumeration exists
    assert Sexus is not None

def test_sexus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sexus]
    expected_literals = [
        "male",
        "undefined",
        "female",
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
Source_strategy = st.builds(
    Source,
)
gedcoml_PersonRef_strategy = st.builds(
    gedcoml_PersonRef,
)
gedcoml_Others_strategy = st.builds(
    gedcoml_Others,
    description=
        safe_text
)
gedcoml_Address_strategy = st.builds(
    gedcoml_Address,
    exodus=
        safe_text,
    entry=
        safe_text
)
gedcoml_Source_strategy = st.builds(
    gedcoml_Source,
)
gedcoml_Note_strategy = st.builds(
    gedcoml_Note,
    content=
        safe_text
)
gedcoml_Married_strategy = st.builds(
    gedcoml_Married,
    weddingDay=
        safe_text,
    separationDay=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
gedcoml_UnbekanntePerson_strategy = st.builds(
    gedcoml_UnbekanntePerson,
)
gedcoml_BekanntePerson_strategy = st.builds(
    gedcoml_BekanntePerson,
    lastName=
        safe_text,
    birthName=
        safe_text,
    middleName=
        safe_text,
    birthDay=
        safe_text,
    deathDay=
        safe_text,
    firstName=
        safe_text
)
gedcoml_Person_strategy = st.builds(
    gedcoml_Person,
    sex=
        safe_text,
    id=
        safe_text
)
gedcoml_Family_strategy = st.builds(
    gedcoml_Family,
    name=
        safe_text
)
gedcoml_Author_strategy = st.builds(
    gedcoml_Author,
    lastName=
        safe_text,
    firstName=
        safe_text
)
gedcoml_FamilyImport_strategy = st.builds(
    gedcoml_FamilyImport,
)
Address_strategy = st.builds(
    Address,
)
gedcoml_PostAddress_strategy = st.builds(
    gedcoml_PostAddress,
    city=
        safe_text,
    postcode=
        safe_text,
    street=
        safe_text
)
gedcoml_FamilyBook_strategy = st.builds(
    gedcoml_FamilyBook,
)
gedcoml_Projectdescription_strategy = st.builds(
    gedcoml_Projectdescription,
    artifactId=
        safe_text,
    groupId=
        safe_text,
    publishingDate=
        safe_text,
    version=
        safe_text
)

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=gedcoml_PersonRef_strategy)
@settings(max_examples=50)
def test_gedcoml_personref_instantiation(instance):
    assert isinstance(instance, gedcoml_PersonRef)

@given(instance=gedcoml_Others_strategy)
@settings(max_examples=50)
def test_gedcoml_others_instantiation(instance):
    assert isinstance(instance, gedcoml_Others)



@given(instance=gedcoml_Others_strategy)
def test_gedcoml_others_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=gedcoml_Address_strategy)
@settings(max_examples=50)
def test_gedcoml_address_instantiation(instance):
    assert isinstance(instance, gedcoml_Address)



@given(instance=gedcoml_Address_strategy)
def test_gedcoml_address_exodus_setter(instance):
    original = instance.exodus
    instance.exodus = original
    assert instance.exodus == original



@given(instance=gedcoml_Address_strategy)
def test_gedcoml_address_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=gedcoml_Source_strategy)
@settings(max_examples=50)
def test_gedcoml_source_instantiation(instance):
    assert isinstance(instance, gedcoml_Source)

@given(instance=gedcoml_Note_strategy)
@settings(max_examples=50)
def test_gedcoml_note_instantiation(instance):
    assert isinstance(instance, gedcoml_Note)



@given(instance=gedcoml_Note_strategy)
def test_gedcoml_note_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=gedcoml_Married_strategy)
@settings(max_examples=50)
def test_gedcoml_married_instantiation(instance):
    assert isinstance(instance, gedcoml_Married)



@given(instance=gedcoml_Married_strategy)
def test_gedcoml_married_weddingDay_setter(instance):
    original = instance.weddingDay
    instance.weddingDay = original
    assert instance.weddingDay == original



@given(instance=gedcoml_Married_strategy)
def test_gedcoml_married_separationDay_setter(instance):
    original = instance.separationDay
    instance.separationDay = original
    assert instance.separationDay == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=gedcoml_UnbekanntePerson_strategy)
@settings(max_examples=50)
def test_gedcoml_unbekannteperson_instantiation(instance):
    assert isinstance(instance, gedcoml_UnbekanntePerson)

@given(instance=gedcoml_BekanntePerson_strategy)
@settings(max_examples=50)
def test_gedcoml_bekannteperson_instantiation(instance):
    assert isinstance(instance, gedcoml_BekanntePerson)



@given(instance=gedcoml_BekanntePerson_strategy)
def test_gedcoml_bekannteperson_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_gedcoml_bekannteperson_birthName_setter(instance):
    original = instance.birthName
    instance.birthName = original
    assert instance.birthName == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_gedcoml_bekannteperson_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_gedcoml_bekannteperson_birthDay_setter(instance):
    original = instance.birthDay
    instance.birthDay = original
    assert instance.birthDay == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_gedcoml_bekannteperson_deathDay_setter(instance):
    original = instance.deathDay
    instance.deathDay = original
    assert instance.deathDay == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_gedcoml_bekannteperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=gedcoml_Person_strategy)
@settings(max_examples=50)
def test_gedcoml_person_instantiation(instance):
    assert isinstance(instance, gedcoml_Person)



@given(instance=gedcoml_Person_strategy)
def test_gedcoml_person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=gedcoml_Person_strategy)
def test_gedcoml_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gedcoml_Family_strategy)
@settings(max_examples=50)
def test_gedcoml_family_instantiation(instance):
    assert isinstance(instance, gedcoml_Family)



@given(instance=gedcoml_Family_strategy)
def test_gedcoml_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gedcoml_Author_strategy)
@settings(max_examples=50)
def test_gedcoml_author_instantiation(instance):
    assert isinstance(instance, gedcoml_Author)



@given(instance=gedcoml_Author_strategy)
def test_gedcoml_author_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=gedcoml_Author_strategy)
def test_gedcoml_author_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=gedcoml_FamilyImport_strategy)
@settings(max_examples=50)
def test_gedcoml_familyimport_instantiation(instance):
    assert isinstance(instance, gedcoml_FamilyImport)

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)

@given(instance=gedcoml_PostAddress_strategy)
@settings(max_examples=50)
def test_gedcoml_postaddress_instantiation(instance):
    assert isinstance(instance, gedcoml_PostAddress)



@given(instance=gedcoml_PostAddress_strategy)
def test_gedcoml_postaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=gedcoml_PostAddress_strategy)
def test_gedcoml_postaddress_postcode_setter(instance):
    original = instance.postcode
    instance.postcode = original
    assert instance.postcode == original



@given(instance=gedcoml_PostAddress_strategy)
def test_gedcoml_postaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=gedcoml_FamilyBook_strategy)
@settings(max_examples=50)
def test_gedcoml_familybook_instantiation(instance):
    assert isinstance(instance, gedcoml_FamilyBook)

@given(instance=gedcoml_Projectdescription_strategy)
@settings(max_examples=50)
def test_gedcoml_projectdescription_instantiation(instance):
    assert isinstance(instance, gedcoml_Projectdescription)



@given(instance=gedcoml_Projectdescription_strategy)
def test_gedcoml_projectdescription_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original



@given(instance=gedcoml_Projectdescription_strategy)
def test_gedcoml_projectdescription_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=gedcoml_Projectdescription_strategy)
def test_gedcoml_projectdescription_publishingDate_setter(instance):
    original = instance.publishingDate
    instance.publishingDate = original
    assert instance.publishingDate == original



@given(instance=gedcoml_Projectdescription_strategy)
def test_gedcoml_projectdescription_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
