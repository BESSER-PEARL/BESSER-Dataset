import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lendable,
    Item,
    Library::Periodical,
    Library::CirculatingItem,
    Library::Lendable,
    Library::Addressable,
    AudioVisualItem,
    Library::VideoCassette,
    Library::BookOnTape,
    CirculatingItem,
    Library::AudioVisualItem,
    Library::Book,
    Person,
    Library::Item,
    Library::Borrower,
    Library::Employee,
    Addressable,
    Library::Person,
    Library::Library,
    Library::Writer,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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
    assert not inspect.isabstract(Library::Periodical)


def test_library::periodical_constructor_exists():
    assert callable(Library::Periodical.__init__)


def test_library::periodical_constructor_args():
    sig = inspect.signature(Library::Periodical.__init__)
    params = list(sig.parameters.keys())
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::periodical_has_issuesPerYear():
    assert hasattr(Library::Periodical, "issuesPerYear")
    descriptor = None
    for klass in Library::Periodical.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)

def test_library::periodical_has_title():
    assert hasattr(Library::Periodical, "title")
    descriptor = None
    for klass in Library::Periodical.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library::circulatingitem_is_not_abstract():
    assert not inspect.isabstract(Library::CirculatingItem)


def test_library::circulatingitem_constructor_exists():
    assert callable(Library::CirculatingItem.__init__)


def test_library::circulatingitem_constructor_args():
    sig = inspect.signature(Library::CirculatingItem.__init__)
    params = list(sig.parameters.keys())



def test_library::lendable_is_not_abstract():
    assert not inspect.isabstract(Library::Lendable)


def test_library::lendable_constructor_exists():
    assert callable(Library::Lendable.__init__)


def test_library::lendable_constructor_args():
    sig = inspect.signature(Library::Lendable.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_library::lendable_has_copies():
    assert hasattr(Library::Lendable, "copies")
    descriptor = None
    for klass in Library::Lendable.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_library::addressable_is_not_abstract():
    assert not inspect.isabstract(Library::Addressable)


def test_library::addressable_constructor_exists():
    assert callable(Library::Addressable.__init__)


def test_library::addressable_constructor_args():
    sig = inspect.signature(Library::Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library::addressable_has_address():
    assert hasattr(Library::Addressable, "address")
    descriptor = None
    for klass in Library::Addressable.__mro__:
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
    assert not inspect.isabstract(Library::VideoCassette)


def test_library::videocassette_constructor_exists():
    assert callable(Library::VideoCassette.__init__)


def test_library::videocassette_constructor_args():
    sig = inspect.signature(Library::VideoCassette.__init__)
    params = list(sig.parameters.keys())



def test_library::bookontape_is_not_abstract():
    assert not inspect.isabstract(Library::BookOnTape)


def test_library::bookontape_constructor_exists():
    assert callable(Library::BookOnTape.__init__)


def test_library::bookontape_constructor_args():
    sig = inspect.signature(Library::BookOnTape.__init__)
    params = list(sig.parameters.keys())



def test_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(CirculatingItem)


def test_circulatingitem_constructor_exists():
    assert callable(CirculatingItem.__init__)


def test_circulatingitem_constructor_args():
    sig = inspect.signature(CirculatingItem.__init__)
    params = list(sig.parameters.keys())



def test_library::audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(Library::AudioVisualItem)


def test_library::audiovisualitem_constructor_exists():
    assert callable(Library::AudioVisualItem.__init__)


def test_library::audiovisualitem_constructor_args():
    sig = inspect.signature(Library::AudioVisualItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_library::audiovisualitem_has_title():
    assert hasattr(Library::AudioVisualItem, "title")
    descriptor = None
    for klass in Library::AudioVisualItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::audiovisualitem_has_minutesLength():
    assert hasattr(Library::AudioVisualItem, "minutesLength")
    descriptor = None
    for klass in Library::AudioVisualItem.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)

def test_library::audiovisualitem_has_damaged():
    assert hasattr(Library::AudioVisualItem, "damaged")
    descriptor = None
    for klass in Library::AudioVisualItem.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(Library::Book)


def test_library::book_constructor_exists():
    assert callable(Library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(Library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"

def test_library::book_has_title():
    assert hasattr(Library::Book, "title")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_pages():
    assert hasattr(Library::Book, "pages")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_category():
    assert hasattr(Library::Book, "category")
    descriptor = None
    for klass in Library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
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
    assert not inspect.isabstract(Library::Item)


def test_library::item_constructor_exists():
    assert callable(Library::Item.__init__)


def test_library::item_constructor_args():
    sig = inspect.signature(Library::Item.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_library::item_has_publicationDate():
    assert hasattr(Library::Item, "publicationDate")
    descriptor = None
    for klass in Library::Item.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_library::borrower_is_not_abstract():
    assert not inspect.isabstract(Library::Borrower)


def test_library::borrower_constructor_exists():
    assert callable(Library::Borrower.__init__)


def test_library::borrower_constructor_args():
    sig = inspect.signature(Library::Borrower.__init__)
    params = list(sig.parameters.keys())



def test_library::employee_is_not_abstract():
    assert not inspect.isabstract(Library::Employee)


def test_library::employee_constructor_exists():
    assert callable(Library::Employee.__init__)


def test_library::employee_constructor_args():
    sig = inspect.signature(Library::Employee.__init__)
    params = list(sig.parameters.keys())



def test_addressable_is_not_abstract():
    assert not inspect.isabstract(Addressable)


def test_addressable_constructor_exists():
    assert callable(Addressable.__init__)


def test_addressable_constructor_args():
    sig = inspect.signature(Addressable.__init__)
    params = list(sig.parameters.keys())



def test_library::person_is_not_abstract():
    assert not inspect.isabstract(Library::Person)


def test_library::person_constructor_exists():
    assert callable(Library::Person.__init__)


def test_library::person_constructor_args():
    sig = inspect.signature(Library::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_library::person_has_lastName():
    assert hasattr(Library::Person, "lastName")
    descriptor = None
    for klass in Library::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_library::person_has_firstName():
    assert hasattr(Library::Person, "firstName")
    descriptor = None
    for klass in Library::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(Library::Library)


def test_library::library_constructor_exists():
    assert callable(Library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(Library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "people" in params, "Missing parameter 'people'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_people():
    assert hasattr(Library::Library, "people")
    descriptor = None
    for klass in Library::Library.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_name():
    assert hasattr(Library::Library, "name")
    descriptor = None
    for klass in Library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(Library::Writer)


def test_library::writer_constructor_exists():
    assert callable(Library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(Library::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::writer_has_name():
    assert hasattr(Library::Writer, "name")
    descriptor = None
    for klass in Library::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "ScienceFiction",
        "Mystery",
        "Biography",
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
Lendable_strategy = st.builds(
    Lendable,
)
Item_strategy = st.builds(
    Item,
)
Library::Periodical_strategy = st.builds(
    Library::Periodical,
    issuesPerYear=
        st.integers(),
    title=
        safe_text
)
Library::CirculatingItem_strategy = st.builds(
    Library::CirculatingItem,
)
Library::Lendable_strategy = st.builds(
    Library::Lendable,
    copies=
        st.integers()
)
Library::Addressable_strategy = st.builds(
    Library::Addressable,
    address=
        safe_text
)
AudioVisualItem_strategy = st.builds(
    AudioVisualItem,
)
Library::VideoCassette_strategy = st.builds(
    Library::VideoCassette,
)
Library::BookOnTape_strategy = st.builds(
    Library::BookOnTape,
)
CirculatingItem_strategy = st.builds(
    CirculatingItem,
)
Library::AudioVisualItem_strategy = st.builds(
    Library::AudioVisualItem,
    title=
        safe_text,
    minutesLength=
        st.integers(),
    damaged=
        st.booleans()
)
Library::Book_strategy = st.builds(
    Library::Book,
    title=
        safe_text,
    pages=
        st.integers(),
    category=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
Library::Item_strategy = st.builds(
    Library::Item,
    publicationDate=
        st.dates()
)
Library::Borrower_strategy = st.builds(
    Library::Borrower,
)
Library::Employee_strategy = st.builds(
    Library::Employee,
)
Addressable_strategy = st.builds(
    Addressable,
)
Library::Person_strategy = st.builds(
    Library::Person,
    lastName=
        safe_text,
    firstName=
        safe_text
)
Library::Library_strategy = st.builds(
    Library::Library,
    people=
        safe_text,
    name=
        safe_text
)
Library::Writer_strategy = st.builds(
    Library::Writer,
    name=
        safe_text
)

@given(instance=Lendable_strategy)
@settings(max_examples=50)
def test_lendable_instantiation(instance):
    assert isinstance(instance, Lendable)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=Library::Periodical_strategy)
@settings(max_examples=50)
def test_library::periodical_instantiation(instance):
    assert isinstance(instance, Library::Periodical)

@given(instance=Library::Periodical_strategy)
def test_library::periodical_issuesPerYear_type(instance):
    assert isinstance(instance.issuesPerYear, int)


@given(instance=Library::Periodical_strategy)
def test_library::periodical_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original

@given(instance=Library::Periodical_strategy)
def test_library::periodical_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Library::Periodical_strategy)
def test_library::periodical_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Library::CirculatingItem_strategy)
@settings(max_examples=50)
def test_library::circulatingitem_instantiation(instance):
    assert isinstance(instance, Library::CirculatingItem)

@given(instance=Library::Lendable_strategy)
@settings(max_examples=50)
def test_library::lendable_instantiation(instance):
    assert isinstance(instance, Library::Lendable)

@given(instance=Library::Lendable_strategy)
def test_library::lendable_copies_type(instance):
    assert isinstance(instance.copies, int)


@given(instance=Library::Lendable_strategy)
def test_library::lendable_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=Library::Addressable_strategy)
@settings(max_examples=50)
def test_library::addressable_instantiation(instance):
    assert isinstance(instance, Library::Addressable)

@given(instance=Library::Addressable_strategy)
def test_library::addressable_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=Library::Addressable_strategy)
def test_library::addressable_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=AudioVisualItem_strategy)
@settings(max_examples=50)
def test_audiovisualitem_instantiation(instance):
    assert isinstance(instance, AudioVisualItem)

@given(instance=Library::VideoCassette_strategy)
@settings(max_examples=50)
def test_library::videocassette_instantiation(instance):
    assert isinstance(instance, Library::VideoCassette)

@given(instance=Library::BookOnTape_strategy)
@settings(max_examples=50)
def test_library::bookontape_instantiation(instance):
    assert isinstance(instance, Library::BookOnTape)

@given(instance=CirculatingItem_strategy)
@settings(max_examples=50)
def test_circulatingitem_instantiation(instance):
    assert isinstance(instance, CirculatingItem)

@given(instance=Library::AudioVisualItem_strategy)
@settings(max_examples=50)
def test_library::audiovisualitem_instantiation(instance):
    assert isinstance(instance, Library::AudioVisualItem)

@given(instance=Library::AudioVisualItem_strategy)
def test_library::audiovisualitem_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Library::AudioVisualItem_strategy)
def test_library::audiovisualitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Library::AudioVisualItem_strategy)
def test_library::audiovisualitem_minutesLength_type(instance):
    assert isinstance(instance.minutesLength, int)


@given(instance=Library::AudioVisualItem_strategy)
def test_library::audiovisualitem_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original

@given(instance=Library::AudioVisualItem_strategy)
def test_library::audiovisualitem_damaged_type(instance):
    assert isinstance(instance.damaged, bool)


@given(instance=Library::AudioVisualItem_strategy)
def test_library::audiovisualitem_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=Library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, Library::Book)

@given(instance=Library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Library::Book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=Library::Book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=Library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=Library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Library::Item_strategy)
@settings(max_examples=50)
def test_library::item_instantiation(instance):
    assert isinstance(instance, Library::Item)

@given(instance=Library::Item_strategy)
def test_library::item_publicationDate_type(instance):
    assert isinstance(instance.publicationDate, date)


@given(instance=Library::Item_strategy)
def test_library::item_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=Library::Borrower_strategy)
@settings(max_examples=50)
def test_library::borrower_instantiation(instance):
    assert isinstance(instance, Library::Borrower)

@given(instance=Library::Employee_strategy)
@settings(max_examples=50)
def test_library::employee_instantiation(instance):
    assert isinstance(instance, Library::Employee)

@given(instance=Addressable_strategy)
@settings(max_examples=50)
def test_addressable_instantiation(instance):
    assert isinstance(instance, Addressable)

@given(instance=Library::Person_strategy)
@settings(max_examples=50)
def test_library::person_instantiation(instance):
    assert isinstance(instance, Library::Person)

@given(instance=Library::Person_strategy)
def test_library::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Library::Person_strategy)
def test_library::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Library::Person_strategy)
def test_library::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Library::Person_strategy)
def test_library::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, Library::Library)

@given(instance=Library::Library_strategy)
def test_library::library_people_type(instance):
    assert isinstance(instance.people, str)


@given(instance=Library::Library_strategy)
def test_library::library_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original

@given(instance=Library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, Library::Writer)

@given(instance=Library::Writer_strategy)
def test_library::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Library::Writer_strategy)
def test_library::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
