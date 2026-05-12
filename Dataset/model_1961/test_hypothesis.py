import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    addressbook_AddressBook,
    Contact,
    addressbook_Company,
    addressbook_Person,
    addressbook_Note,
    addressbook_Relationship,
    addressbook_Address,
    addressbook_Contact,
    NoteType,
    RelationshipType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_addressbook_addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook_AddressBook)


def test_addressbook_addressbook_constructor_exists():
    assert callable(addressbook_AddressBook.__init__)


def test_addressbook_addressbook_constructor_args():
    sig = inspect.signature(addressbook_AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())



def test_addressbook_company_is_not_abstract():
    assert not inspect.isabstract(addressbook_Company)


def test_addressbook_company_constructor_exists():
    assert callable(addressbook_Company.__init__)


def test_addressbook_company_constructor_args():
    sig = inspect.signature(addressbook_Company.__init__)
    params = list(sig.parameters.keys())
    assert "Industry" in params, "Missing parameter 'Industry'"

def test_addressbook_company_has_Industry():
    assert hasattr(addressbook_Company, "Industry")
    descriptor = None
    for klass in addressbook_Company.__mro__:
        if "Industry" in klass.__dict__:
            descriptor = klass.__dict__["Industry"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_person_is_not_abstract():
    assert not inspect.isabstract(addressbook_Person)


def test_addressbook_person_constructor_exists():
    assert callable(addressbook_Person.__init__)


def test_addressbook_person_constructor_args():
    sig = inspect.signature(addressbook_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Title" in params, "Missing parameter 'Title'"

def test_addressbook_person_has_Title():
    assert hasattr(addressbook_Person, "Title")
    descriptor = None
    for klass in addressbook_Person.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_note_is_not_abstract():
    assert not inspect.isabstract(addressbook_Note)


def test_addressbook_note_constructor_exists():
    assert callable(addressbook_Note.__init__)


def test_addressbook_note_constructor_args():
    sig = inspect.signature(addressbook_Note.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Comment" in params, "Missing parameter 'Comment'"
    assert "Author" in params, "Missing parameter 'Author'"
    assert "Time" in params, "Missing parameter 'Time'"

def test_addressbook_note_has_Type():
    assert hasattr(addressbook_Note, "Type")
    descriptor = None
    for klass in addressbook_Note.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_note_has_Comment():
    assert hasattr(addressbook_Note, "Comment")
    descriptor = None
    for klass in addressbook_Note.__mro__:
        if "Comment" in klass.__dict__:
            descriptor = klass.__dict__["Comment"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_note_has_Author():
    assert hasattr(addressbook_Note, "Author")
    descriptor = None
    for klass in addressbook_Note.__mro__:
        if "Author" in klass.__dict__:
            descriptor = klass.__dict__["Author"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_note_has_Time():
    assert hasattr(addressbook_Note, "Time")
    descriptor = None
    for klass in addressbook_Note.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_relationship_is_not_abstract():
    assert not inspect.isabstract(addressbook_Relationship)


def test_addressbook_relationship_constructor_exists():
    assert callable(addressbook_Relationship.__init__)


def test_addressbook_relationship_constructor_args():
    sig = inspect.signature(addressbook_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_addressbook_relationship_has_Type():
    assert hasattr(addressbook_Relationship, "Type")
    descriptor = None
    for klass in addressbook_Relationship.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_address_is_not_abstract():
    assert not inspect.isabstract(addressbook_Address)


def test_addressbook_address_constructor_exists():
    assert callable(addressbook_Address.__init__)


def test_addressbook_address_constructor_args():
    sig = inspect.signature(addressbook_Address.__init__)
    params = list(sig.parameters.keys())
    assert "Street" in params, "Missing parameter 'Street'"
    assert "City" in params, "Missing parameter 'City'"
    assert "HouseNr" in params, "Missing parameter 'HouseNr'"

def test_addressbook_address_has_Street():
    assert hasattr(addressbook_Address, "Street")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "Street" in klass.__dict__:
            descriptor = klass.__dict__["Street"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_address_has_City():
    assert hasattr(addressbook_Address, "City")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_address_has_HouseNr():
    assert hasattr(addressbook_Address, "HouseNr")
    descriptor = None
    for klass in addressbook_Address.__mro__:
        if "HouseNr" in klass.__dict__:
            descriptor = klass.__dict__["HouseNr"]
            break
    assert isinstance(descriptor, property)



def test_addressbook_contact_is_not_abstract():
    assert not inspect.isabstract(addressbook_Contact)


def test_addressbook_contact_constructor_exists():
    assert callable(addressbook_Contact.__init__)


def test_addressbook_contact_constructor_args():
    sig = inspect.signature(addressbook_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Website" in params, "Missing parameter 'Website'"
    assert "EMail" in params, "Missing parameter 'EMail'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_addressbook_contact_has_Phone():
    assert hasattr(addressbook_Contact, "Phone")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_contact_has_Website():
    assert hasattr(addressbook_Contact, "Website")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "Website" in klass.__dict__:
            descriptor = klass.__dict__["Website"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_contact_has_EMail():
    assert hasattr(addressbook_Contact, "EMail")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "EMail" in klass.__dict__:
            descriptor = klass.__dict__["EMail"]
            break
    assert isinstance(descriptor, property)

def test_addressbook_contact_has_Name():
    assert hasattr(addressbook_Contact, "Name")
    descriptor = None
    for klass in addressbook_Contact.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_notetype_exists():
    # Check that the Enumeration exists
    assert NoteType is not None

def test_notetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NoteType]
    expected_literals = [
        "CALL",
        "EMAIL",
        "MEETING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoteType"

def test_relationshiptype_exists():
    # Check that the Enumeration exists
    assert RelationshipType is not None

def test_relationshiptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipType]
    expected_literals = [
        "CoWorker",
        "Employee",
        "Boss",
        "Subdivision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationshipType"


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
addressbook_AddressBook_strategy = st.builds(
    addressbook_AddressBook,
)
Contact_strategy = st.builds(
    Contact,
)
addressbook_Company_strategy = st.builds(
    addressbook_Company,
    Industry=
        safe_text
)
addressbook_Person_strategy = st.builds(
    addressbook_Person,
    Title=
        safe_text
)
addressbook_Note_strategy = st.builds(
    addressbook_Note,
    Type=
        safe_text,
    Comment=
        safe_text,
    Author=
        safe_text,
    Time=
        st.dates()
)
addressbook_Relationship_strategy = st.builds(
    addressbook_Relationship,
    Type=
        safe_text
)
addressbook_Address_strategy = st.builds(
    addressbook_Address,
    Street=
        safe_text,
    City=
        safe_text,
    HouseNr=
        safe_text
)
addressbook_Contact_strategy = st.builds(
    addressbook_Contact,
    Phone=
        safe_text,
    Website=
        safe_text,
    EMail=
        safe_text,
    Name=
        safe_text
)

@given(instance=addressbook_AddressBook_strategy)
@settings(max_examples=50)
def test_addressbook_addressbook_instantiation(instance):
    assert isinstance(instance, addressbook_AddressBook)

@given(instance=Contact_strategy)
@settings(max_examples=50)
def test_contact_instantiation(instance):
    assert isinstance(instance, Contact)

@given(instance=addressbook_Company_strategy)
@settings(max_examples=50)
def test_addressbook_company_instantiation(instance):
    assert isinstance(instance, addressbook_Company)



@given(instance=addressbook_Company_strategy)
def test_addressbook_company_Industry_setter(instance):
    original = instance.Industry
    instance.Industry = original
    assert instance.Industry == original

@given(instance=addressbook_Person_strategy)
@settings(max_examples=50)
def test_addressbook_person_instantiation(instance):
    assert isinstance(instance, addressbook_Person)



@given(instance=addressbook_Person_strategy)
def test_addressbook_person_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original

@given(instance=addressbook_Note_strategy)
@settings(max_examples=50)
def test_addressbook_note_instantiation(instance):
    assert isinstance(instance, addressbook_Note)



@given(instance=addressbook_Note_strategy)
def test_addressbook_note_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=addressbook_Note_strategy)
def test_addressbook_note_Comment_setter(instance):
    original = instance.Comment
    instance.Comment = original
    assert instance.Comment == original



@given(instance=addressbook_Note_strategy)
def test_addressbook_note_Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original



@given(instance=addressbook_Note_strategy)
def test_addressbook_note_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original

@given(instance=addressbook_Relationship_strategy)
@settings(max_examples=50)
def test_addressbook_relationship_instantiation(instance):
    assert isinstance(instance, addressbook_Relationship)



@given(instance=addressbook_Relationship_strategy)
def test_addressbook_relationship_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=addressbook_Address_strategy)
@settings(max_examples=50)
def test_addressbook_address_instantiation(instance):
    assert isinstance(instance, addressbook_Address)



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_Street_setter(instance):
    original = instance.Street
    instance.Street = original
    assert instance.Street == original



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=addressbook_Address_strategy)
def test_addressbook_address_HouseNr_setter(instance):
    original = instance.HouseNr
    instance.HouseNr = original
    assert instance.HouseNr == original

@given(instance=addressbook_Contact_strategy)
@settings(max_examples=50)
def test_addressbook_contact_instantiation(instance):
    assert isinstance(instance, addressbook_Contact)



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_Website_setter(instance):
    original = instance.Website
    instance.Website = original
    assert instance.Website == original



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_EMail_setter(instance):
    original = instance.EMail
    instance.EMail = original
    assert instance.EMail == original



@given(instance=addressbook_Contact_strategy)
def test_addressbook_contact_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
