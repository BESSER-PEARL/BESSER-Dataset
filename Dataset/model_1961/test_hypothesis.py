import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    addressbook::AddressBook,
    Contact,
    addressbook::Company,
    addressbook::Person,
    addressbook::Note,
    addressbook::Relationship,
    addressbook::Address,
    addressbook::Contact,
    RelationshipType,
    NoteType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_addressbook::addressbook_is_not_abstract():
    assert not inspect.isabstract(addressbook::AddressBook)


def test_addressbook::addressbook_constructor_exists():
    assert callable(addressbook::AddressBook.__init__)


def test_addressbook::addressbook_constructor_args():
    sig = inspect.signature(addressbook::AddressBook.__init__)
    params = list(sig.parameters.keys())



def test_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())



def test_addressbook::company_is_not_abstract():
    assert not inspect.isabstract(addressbook::Company)


def test_addressbook::company_constructor_exists():
    assert callable(addressbook::Company.__init__)


def test_addressbook::company_constructor_args():
    sig = inspect.signature(addressbook::Company.__init__)
    params = list(sig.parameters.keys())
    assert "Industry" in params, "Missing parameter 'Industry'"

def test_addressbook::company_has_Industry():
    assert hasattr(addressbook::Company, "Industry")
    descriptor = None
    for klass in addressbook::Company.__mro__:
        if "Industry" in klass.__dict__:
            descriptor = klass.__dict__["Industry"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::person_is_not_abstract():
    assert not inspect.isabstract(addressbook::Person)


def test_addressbook::person_constructor_exists():
    assert callable(addressbook::Person.__init__)


def test_addressbook::person_constructor_args():
    sig = inspect.signature(addressbook::Person.__init__)
    params = list(sig.parameters.keys())
    assert "Title" in params, "Missing parameter 'Title'"

def test_addressbook::person_has_Title():
    assert hasattr(addressbook::Person, "Title")
    descriptor = None
    for klass in addressbook::Person.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::note_is_not_abstract():
    assert not inspect.isabstract(addressbook::Note)


def test_addressbook::note_constructor_exists():
    assert callable(addressbook::Note.__init__)


def test_addressbook::note_constructor_args():
    sig = inspect.signature(addressbook::Note.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Author" in params, "Missing parameter 'Author'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Comment" in params, "Missing parameter 'Comment'"

def test_addressbook::note_has_Type():
    assert hasattr(addressbook::Note, "Type")
    descriptor = None
    for klass in addressbook::Note.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::note_has_Author():
    assert hasattr(addressbook::Note, "Author")
    descriptor = None
    for klass in addressbook::Note.__mro__:
        if "Author" in klass.__dict__:
            descriptor = klass.__dict__["Author"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::note_has_Time():
    assert hasattr(addressbook::Note, "Time")
    descriptor = None
    for klass in addressbook::Note.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::note_has_Comment():
    assert hasattr(addressbook::Note, "Comment")
    descriptor = None
    for klass in addressbook::Note.__mro__:
        if "Comment" in klass.__dict__:
            descriptor = klass.__dict__["Comment"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::relationship_is_not_abstract():
    assert not inspect.isabstract(addressbook::Relationship)


def test_addressbook::relationship_constructor_exists():
    assert callable(addressbook::Relationship.__init__)


def test_addressbook::relationship_constructor_args():
    sig = inspect.signature(addressbook::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_addressbook::relationship_has_Type():
    assert hasattr(addressbook::Relationship, "Type")
    descriptor = None
    for klass in addressbook::Relationship.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::address_is_not_abstract():
    assert not inspect.isabstract(addressbook::Address)


def test_addressbook::address_constructor_exists():
    assert callable(addressbook::Address.__init__)


def test_addressbook::address_constructor_args():
    sig = inspect.signature(addressbook::Address.__init__)
    params = list(sig.parameters.keys())
    assert "City" in params, "Missing parameter 'City'"
    assert "HouseNr" in params, "Missing parameter 'HouseNr'"
    assert "Street" in params, "Missing parameter 'Street'"

def test_addressbook::address_has_City():
    assert hasattr(addressbook::Address, "City")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::address_has_HouseNr():
    assert hasattr(addressbook::Address, "HouseNr")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "HouseNr" in klass.__dict__:
            descriptor = klass.__dict__["HouseNr"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::address_has_Street():
    assert hasattr(addressbook::Address, "Street")
    descriptor = None
    for klass in addressbook::Address.__mro__:
        if "Street" in klass.__dict__:
            descriptor = klass.__dict__["Street"]
            break
    assert isinstance(descriptor, property)



def test_addressbook::contact_is_not_abstract():
    assert not inspect.isabstract(addressbook::Contact)


def test_addressbook::contact_constructor_exists():
    assert callable(addressbook::Contact.__init__)


def test_addressbook::contact_constructor_args():
    sig = inspect.signature(addressbook::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Website" in params, "Missing parameter 'Website'"
    assert "EMail" in params, "Missing parameter 'EMail'"

def test_addressbook::contact_has_Phone():
    assert hasattr(addressbook::Contact, "Phone")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::contact_has_Name():
    assert hasattr(addressbook::Contact, "Name")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::contact_has_Website():
    assert hasattr(addressbook::Contact, "Website")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "Website" in klass.__dict__:
            descriptor = klass.__dict__["Website"]
            break
    assert isinstance(descriptor, property)

def test_addressbook::contact_has_EMail():
    assert hasattr(addressbook::Contact, "EMail")
    descriptor = None
    for klass in addressbook::Contact.__mro__:
        if "EMail" in klass.__dict__:
            descriptor = klass.__dict__["EMail"]
            break
    assert isinstance(descriptor, property)

def test_relationshiptype_exists():
    # Check that the Enumeration exists
    assert RelationshipType is not None

def test_relationshiptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipType]
    expected_literals = [
        "Employee",
        "CoWorker",
        "Boss",
        "Subdivision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationshipType"

def test_notetype_exists():
    # Check that the Enumeration exists
    assert NoteType is not None

def test_notetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NoteType]
    expected_literals = [
        "EMAIL",
        "CALL",
        "MEETING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoteType"


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
addressbook::AddressBook_strategy = st.builds(
    addressbook::AddressBook,
)
Contact_strategy = st.builds(
    Contact,
)
addressbook::Company_strategy = st.builds(
    addressbook::Company,
    Industry=
        safe_text
)
addressbook::Person_strategy = st.builds(
    addressbook::Person,
    Title=
        safe_text
)
addressbook::Note_strategy = st.builds(
    addressbook::Note,
    Type=
        safe_text,
    Author=
        safe_text,
    Time=
        st.dates(),
    Comment=
        safe_text
)
addressbook::Relationship_strategy = st.builds(
    addressbook::Relationship,
    Type=
        safe_text
)
addressbook::Address_strategy = st.builds(
    addressbook::Address,
    City=
        safe_text,
    HouseNr=
        safe_text,
    Street=
        safe_text
)
addressbook::Contact_strategy = st.builds(
    addressbook::Contact,
    Phone=
        safe_text,
    Name=
        safe_text,
    Website=
        safe_text,
    EMail=
        safe_text
)

@given(instance=addressbook::AddressBook_strategy)
@settings(max_examples=50)
def test_addressbook::addressbook_instantiation(instance):
    assert isinstance(instance, addressbook::AddressBook)

@given(instance=Contact_strategy)
@settings(max_examples=50)
def test_contact_instantiation(instance):
    assert isinstance(instance, Contact)

@given(instance=addressbook::Company_strategy)
@settings(max_examples=50)
def test_addressbook::company_instantiation(instance):
    assert isinstance(instance, addressbook::Company)

@given(instance=addressbook::Company_strategy)
def test_addressbook::company_Industry_type(instance):
    assert isinstance(instance.Industry, str)


@given(instance=addressbook::Company_strategy)
def test_addressbook::company_Industry_setter(instance):
    original = instance.Industry
    instance.Industry = original
    assert instance.Industry == original

@given(instance=addressbook::Person_strategy)
@settings(max_examples=50)
def test_addressbook::person_instantiation(instance):
    assert isinstance(instance, addressbook::Person)

@given(instance=addressbook::Person_strategy)
def test_addressbook::person_Title_type(instance):
    assert isinstance(instance.Title, str)


@given(instance=addressbook::Person_strategy)
def test_addressbook::person_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original

@given(instance=addressbook::Note_strategy)
@settings(max_examples=50)
def test_addressbook::note_instantiation(instance):
    assert isinstance(instance, addressbook::Note)

@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Author_type(instance):
    assert isinstance(instance.Author, str)


@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original

@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Time_type(instance):
    assert isinstance(instance.Time, date)


@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original

@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Comment_type(instance):
    assert isinstance(instance.Comment, str)


@given(instance=addressbook::Note_strategy)
def test_addressbook::note_Comment_setter(instance):
    original = instance.Comment
    instance.Comment = original
    assert instance.Comment == original

@given(instance=addressbook::Relationship_strategy)
@settings(max_examples=50)
def test_addressbook::relationship_instantiation(instance):
    assert isinstance(instance, addressbook::Relationship)

@given(instance=addressbook::Relationship_strategy)
def test_addressbook::relationship_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=addressbook::Relationship_strategy)
def test_addressbook::relationship_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=addressbook::Address_strategy)
@settings(max_examples=50)
def test_addressbook::address_instantiation(instance):
    assert isinstance(instance, addressbook::Address)

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_City_type(instance):
    assert isinstance(instance.City, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_HouseNr_type(instance):
    assert isinstance(instance.HouseNr, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_HouseNr_setter(instance):
    original = instance.HouseNr
    instance.HouseNr = original
    assert instance.HouseNr == original

@given(instance=addressbook::Address_strategy)
def test_addressbook::address_Street_type(instance):
    assert isinstance(instance.Street, str)


@given(instance=addressbook::Address_strategy)
def test_addressbook::address_Street_setter(instance):
    original = instance.Street
    instance.Street = original
    assert instance.Street == original

@given(instance=addressbook::Contact_strategy)
@settings(max_examples=50)
def test_addressbook::contact_instantiation(instance):
    assert isinstance(instance, addressbook::Contact)

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_Phone_type(instance):
    assert isinstance(instance.Phone, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_Website_type(instance):
    assert isinstance(instance.Website, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_Website_setter(instance):
    original = instance.Website
    instance.Website = original
    assert instance.Website == original

@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_EMail_type(instance):
    assert isinstance(instance.EMail, str)


@given(instance=addressbook::Contact_strategy)
def test_addressbook::contact_EMail_setter(instance):
    original = instance.EMail
    instance.EMail = original
    assert instance.EMail == original
