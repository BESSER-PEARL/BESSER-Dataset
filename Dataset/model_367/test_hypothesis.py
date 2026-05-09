import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CirculatingItem,
    library::Lendable,
    library::IncBook,
    Person,
    library::Item,
    library::Borrower,
    library::Employee,
    library::Writer,
    library::Addressable,
    Addressable,
    library::Person,
    library::Library,
    Lendable,
    Item,
    library::CirculatingItem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(CirculatingItem)


def test_circulatingitem_constructor_exists():
    assert callable(CirculatingItem.__init__)


def test_circulatingitem_constructor_args():
    sig = inspect.signature(CirculatingItem.__init__)
    params = list(sig.parameters.keys())



def test_library::lendable_is_not_abstract():
    assert not inspect.isabstract(library::Lendable)


def test_library::lendable_constructor_exists():
    assert callable(library::Lendable.__init__)


def test_library::lendable_constructor_args():
    sig = inspect.signature(library::Lendable.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_library::lendable_has_copies():
    assert hasattr(library::Lendable, "copies")
    descriptor = None
    for klass in library::Lendable.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_library::incbook_is_not_abstract():
    assert not inspect.isabstract(library::IncBook)


def test_library::incbook_constructor_exists():
    assert callable(library::IncBook.__init__)


def test_library::incbook_constructor_args():
    sig = inspect.signature(library::IncBook.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library::incbook_has_title():
    assert hasattr(library::IncBook, "title")
    descriptor = None
    for klass in library::IncBook.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::incbook_has_pages():
    assert hasattr(library::IncBook, "pages")
    descriptor = None
    for klass in library::IncBook.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_library::item_is_not_abstract():
    assert not inspect.isabstract(library::Item)


def test_library::item_constructor_exists():
    assert callable(library::Item.__init__)


def test_library::item_constructor_args():
    sig = inspect.signature(library::Item.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_library::item_has_publicationDate():
    assert hasattr(library::Item, "publicationDate")
    descriptor = None
    for klass in library::Item.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_library::borrower_is_not_abstract():
    assert not inspect.isabstract(library::Borrower)


def test_library::borrower_constructor_exists():
    assert callable(library::Borrower.__init__)


def test_library::borrower_constructor_args():
    sig = inspect.signature(library::Borrower.__init__)
    params = list(sig.parameters.keys())



def test_library::employee_is_not_abstract():
    assert not inspect.isabstract(library::Employee)


def test_library::employee_constructor_exists():
    assert callable(library::Employee.__init__)


def test_library::employee_constructor_args():
    sig = inspect.signature(library::Employee.__init__)
    params = list(sig.parameters.keys())



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(library::Writer)


def test_library::writer_constructor_exists():
    assert callable(library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(library::Writer.__init__)
    params = list(sig.parameters.keys())



def test_library::addressable_is_not_abstract():
    assert not inspect.isabstract(library::Addressable)


def test_library::addressable_constructor_exists():
    assert callable(library::Addressable.__init__)


def test_library::addressable_constructor_args():
    sig = inspect.signature(library::Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library::addressable_has_address():
    assert hasattr(library::Addressable, "address")
    descriptor = None
    for klass in library::Addressable.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_addressable_is_not_abstract():
    assert not inspect.isabstract(Addressable)


def test_addressable_constructor_exists():
    assert callable(Addressable.__init__)


def test_addressable_constructor_args():
    sig = inspect.signature(Addressable.__init__)
    params = list(sig.parameters.keys())



def test_library::person_is_not_abstract():
    assert not inspect.isabstract(library::Person)


def test_library::person_constructor_exists():
    assert callable(library::Person.__init__)


def test_library::person_constructor_args():
    sig = inspect.signature(library::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_library::person_has_lastName():
    assert hasattr(library::Person, "lastName")
    descriptor = None
    for klass in library::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_library::person_has_firstName():
    assert hasattr(library::Person, "firstName")
    descriptor = None
    for klass in library::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lendable_is_not_abstract():
    assert not inspect.isabstract(Lendable)


def test_lendable_constructor_exists():
    assert callable(Lendable.__init__)


def test_lendable_constructor_args():
    sig = inspect.signature(Lendable.__init__)
    params = list(sig.parameters.keys())



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_library::circulatingitem_is_not_abstract():
    assert not inspect.isabstract(library::CirculatingItem)


def test_library::circulatingitem_constructor_exists():
    assert callable(library::CirculatingItem.__init__)


def test_library::circulatingitem_constructor_args():
    sig = inspect.signature(library::CirculatingItem.__init__)
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
CirculatingItem_strategy = st.builds(
    CirculatingItem,
)
library::Lendable_strategy = st.builds(
    library::Lendable,
    copies=
        st.integers()
)
library::IncBook_strategy = st.builds(
    library::IncBook,
    title=
        safe_text,
    pages=
        st.integers()
)
Person_strategy = st.builds(
    Person,
)
library::Item_strategy = st.builds(
    library::Item,
    publicationDate=
        st.dates()
)
library::Borrower_strategy = st.builds(
    library::Borrower,
)
library::Employee_strategy = st.builds(
    library::Employee,
)
library::Writer_strategy = st.builds(
    library::Writer,
)
library::Addressable_strategy = st.builds(
    library::Addressable,
    address=
        safe_text
)
Addressable_strategy = st.builds(
    Addressable,
)
library::Person_strategy = st.builds(
    library::Person,
    lastName=
        safe_text,
    firstName=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)
Lendable_strategy = st.builds(
    Lendable,
)
Item_strategy = st.builds(
    Item,
)
library::CirculatingItem_strategy = st.builds(
    library::CirculatingItem,
)

@given(instance=CirculatingItem_strategy)
@settings(max_examples=50)
def test_circulatingitem_instantiation(instance):
    assert isinstance(instance, CirculatingItem)

@given(instance=library::Lendable_strategy)
@settings(max_examples=50)
def test_library::lendable_instantiation(instance):
    assert isinstance(instance, library::Lendable)

@given(instance=library::Lendable_strategy)
def test_library::lendable_copies_type(instance):
    assert isinstance(instance.copies, int)


@given(instance=library::Lendable_strategy)
def test_library::lendable_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=library::IncBook_strategy)
@settings(max_examples=50)
def test_library::incbook_instantiation(instance):
    assert isinstance(instance, library::IncBook)

@given(instance=library::IncBook_strategy)
def test_library::incbook_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::IncBook_strategy)
def test_library::incbook_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::IncBook_strategy)
def test_library::incbook_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library::IncBook_strategy)
def test_library::incbook_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=library::Item_strategy)
@settings(max_examples=50)
def test_library::item_instantiation(instance):
    assert isinstance(instance, library::Item)

@given(instance=library::Item_strategy)
def test_library::item_publicationDate_type(instance):
    assert isinstance(instance.publicationDate, date)


@given(instance=library::Item_strategy)
def test_library::item_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=library::Borrower_strategy)
@settings(max_examples=50)
def test_library::borrower_instantiation(instance):
    assert isinstance(instance, library::Borrower)

@given(instance=library::Employee_strategy)
@settings(max_examples=50)
def test_library::employee_instantiation(instance):
    assert isinstance(instance, library::Employee)

@given(instance=library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, library::Writer)

@given(instance=library::Addressable_strategy)
@settings(max_examples=50)
def test_library::addressable_instantiation(instance):
    assert isinstance(instance, library::Addressable)

@given(instance=library::Addressable_strategy)
def test_library::addressable_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=library::Addressable_strategy)
def test_library::addressable_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Addressable_strategy)
@settings(max_examples=50)
def test_addressable_instantiation(instance):
    assert isinstance(instance, Addressable)

@given(instance=library::Person_strategy)
@settings(max_examples=50)
def test_library::person_instantiation(instance):
    assert isinstance(instance, library::Person)

@given(instance=library::Person_strategy)
def test_library::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=library::Person_strategy)
def test_library::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=library::Person_strategy)
def test_library::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=library::Person_strategy)
def test_library::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Lendable_strategy)
@settings(max_examples=50)
def test_lendable_instantiation(instance):
    assert isinstance(instance, Lendable)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=library::CirculatingItem_strategy)
@settings(max_examples=50)
def test_library::circulatingitem_instantiation(instance):
    assert isinstance(instance, library::CirculatingItem)
