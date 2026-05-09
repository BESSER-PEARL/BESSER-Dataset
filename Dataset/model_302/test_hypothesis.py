import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Addressable,
    AudioVisualItem,
    library::VideoCassette,
    library::BookOnTape,
    Person,
    library::Item,
    library::Borrower,
    library::Employee,
    Lendable,
    Item,
    library::Periodical,
    library::CirculatingItem,
    library::Lendable,
    Addressable,
    library::Person,
    library::Library,
    library::Writer,
    CirculatingItem,
    library::AudioVisualItem,
    library::Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(AudioVisualItem)


def test_audiovisualitem_constructor_exists():
    assert callable(AudioVisualItem.__init__)


def test_audiovisualitem_constructor_args():
    sig = inspect.signature(AudioVisualItem.__init__)
    params = list(sig.parameters.keys())



def test_library::videocassette_is_not_abstract():
    assert not inspect.isabstract(library::VideoCassette)


def test_library::videocassette_constructor_exists():
    assert callable(library::VideoCassette.__init__)


def test_library::videocassette_constructor_args():
    sig = inspect.signature(library::VideoCassette.__init__)
    params = list(sig.parameters.keys())



def test_library::bookontape_is_not_abstract():
    assert not inspect.isabstract(library::BookOnTape)


def test_library::bookontape_constructor_exists():
    assert callable(library::BookOnTape.__init__)


def test_library::bookontape_constructor_args():
    sig = inspect.signature(library::BookOnTape.__init__)
    params = list(sig.parameters.keys())



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



def test_library::periodical_is_not_abstract():
    assert not inspect.isabstract(library::Periodical)


def test_library::periodical_constructor_exists():
    assert callable(library::Periodical.__init__)


def test_library::periodical_constructor_args():
    sig = inspect.signature(library::Periodical.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"

def test_library::periodical_has_title():
    assert hasattr(library::Periodical, "title")
    descriptor = None
    for klass in library::Periodical.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::periodical_has_issuesPerYear():
    assert hasattr(library::Periodical, "issuesPerYear")
    descriptor = None
    for klass in library::Periodical.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)



def test_library::circulatingitem_is_not_abstract():
    assert not inspect.isabstract(library::CirculatingItem)


def test_library::circulatingitem_constructor_exists():
    assert callable(library::CirculatingItem.__init__)


def test_library::circulatingitem_constructor_args():
    sig = inspect.signature(library::CirculatingItem.__init__)
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
    assert "people" in params, "Missing parameter 'people'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_people():
    assert hasattr(library::Library, "people")
    descriptor = None
    for klass in library::Library.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(library::Writer)


def test_library::writer_constructor_exists():
    assert callable(library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(library::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::writer_has_name():
    assert hasattr(library::Writer, "name")
    descriptor = None
    for klass in library::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(CirculatingItem)


def test_circulatingitem_constructor_exists():
    assert callable(CirculatingItem.__init__)


def test_circulatingitem_constructor_args():
    sig = inspect.signature(CirculatingItem.__init__)
    params = list(sig.parameters.keys())



def test_library::audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(library::AudioVisualItem)


def test_library::audiovisualitem_constructor_exists():
    assert callable(library::AudioVisualItem.__init__)


def test_library::audiovisualitem_constructor_args():
    sig = inspect.signature(library::AudioVisualItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "damaged" in params, "Missing parameter 'damaged'"
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"

def test_library::audiovisualitem_has_title():
    assert hasattr(library::AudioVisualItem, "title")
    descriptor = None
    for klass in library::AudioVisualItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::audiovisualitem_has_damaged():
    assert hasattr(library::AudioVisualItem, "damaged")
    descriptor = None
    for klass in library::AudioVisualItem.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)

def test_library::audiovisualitem_has_minutesLength():
    assert hasattr(library::AudioVisualItem, "minutesLength")
    descriptor = None
    for klass in library::AudioVisualItem.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"

def test_library::book_has_title():
    assert hasattr(library::Book, "title")
    descriptor = None
    for klass in library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_pages():
    assert hasattr(library::Book, "pages")
    descriptor = None
    for klass in library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_category():
    assert hasattr(library::Book, "category")
    descriptor = None
    for klass in library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Biography",
        "Mystery",
        "ScienceFiction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategory"


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
library::Addressable_strategy = st.builds(
    library::Addressable,
    address=
        safe_text
)
AudioVisualItem_strategy = st.builds(
    AudioVisualItem,
)
library::VideoCassette_strategy = st.builds(
    library::VideoCassette,
)
library::BookOnTape_strategy = st.builds(
    library::BookOnTape,
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
Lendable_strategy = st.builds(
    Lendable,
)
Item_strategy = st.builds(
    Item,
)
library::Periodical_strategy = st.builds(
    library::Periodical,
    title=
        safe_text,
    issuesPerYear=
        st.integers()
)
library::CirculatingItem_strategy = st.builds(
    library::CirculatingItem,
)
library::Lendable_strategy = st.builds(
    library::Lendable,
    copies=
        st.integers()
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
    people=
        safe_text,
    name=
        safe_text
)
library::Writer_strategy = st.builds(
    library::Writer,
    name=
        safe_text
)
CirculatingItem_strategy = st.builds(
    CirculatingItem,
)
library::AudioVisualItem_strategy = st.builds(
    library::AudioVisualItem,
    title=
        safe_text,
    damaged=
        st.booleans(),
    minutesLength=
        st.integers()
)
library::Book_strategy = st.builds(
    library::Book,
    title=
        safe_text,
    pages=
        st.integers(),
    category=
        safe_text
)

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

@given(instance=AudioVisualItem_strategy)
@settings(max_examples=50)
def test_audiovisualitem_instantiation(instance):
    assert isinstance(instance, AudioVisualItem)

@given(instance=library::VideoCassette_strategy)
@settings(max_examples=50)
def test_library::videocassette_instantiation(instance):
    assert isinstance(instance, library::VideoCassette)

@given(instance=library::BookOnTape_strategy)
@settings(max_examples=50)
def test_library::bookontape_instantiation(instance):
    assert isinstance(instance, library::BookOnTape)

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

@given(instance=Lendable_strategy)
@settings(max_examples=50)
def test_lendable_instantiation(instance):
    assert isinstance(instance, Lendable)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=library::Periodical_strategy)
@settings(max_examples=50)
def test_library::periodical_instantiation(instance):
    assert isinstance(instance, library::Periodical)

@given(instance=library::Periodical_strategy)
def test_library::periodical_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Periodical_strategy)
def test_library::periodical_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Periodical_strategy)
def test_library::periodical_issuesPerYear_type(instance):
    assert isinstance(instance.issuesPerYear, int)


@given(instance=library::Periodical_strategy)
def test_library::periodical_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original

@given(instance=library::CirculatingItem_strategy)
@settings(max_examples=50)
def test_library::circulatingitem_instantiation(instance):
    assert isinstance(instance, library::CirculatingItem)

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
def test_library::library_people_type(instance):
    assert isinstance(instance.people, str)


@given(instance=library::Library_strategy)
def test_library::library_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, library::Writer)

@given(instance=library::Writer_strategy)
def test_library::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Writer_strategy)
def test_library::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CirculatingItem_strategy)
@settings(max_examples=50)
def test_circulatingitem_instantiation(instance):
    assert isinstance(instance, CirculatingItem)

@given(instance=library::AudioVisualItem_strategy)
@settings(max_examples=50)
def test_library::audiovisualitem_instantiation(instance):
    assert isinstance(instance, library::AudioVisualItem)

@given(instance=library::AudioVisualItem_strategy)
def test_library::audiovisualitem_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::AudioVisualItem_strategy)
def test_library::audiovisualitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::AudioVisualItem_strategy)
def test_library::audiovisualitem_damaged_type(instance):
    assert isinstance(instance.damaged, bool)


@given(instance=library::AudioVisualItem_strategy)
def test_library::audiovisualitem_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=library::AudioVisualItem_strategy)
def test_library::audiovisualitem_minutesLength_type(instance):
    assert isinstance(instance.minutesLength, int)


@given(instance=library::AudioVisualItem_strategy)
def test_library::audiovisualitem_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library::Book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original
