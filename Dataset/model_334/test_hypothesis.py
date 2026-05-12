import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    extlibrary_Addressable,
    Person,
    AudioVisualItem,
    extlibrary_VideoCassette,
    extlibrary_BookOnTape,
    Lendable,
    Item,
    extlibrary_Periodical,
    extlibrary_CirculatingItem,
    extlibrary_Lendable,
    extlibrary_Item,
    extlibrary_Borrower,
    extlibrary_Employee,
    Addressable,
    extlibrary_Person,
    extlibrary_Library,
    extlibrary_Writer,
    CirculatingItem,
    extlibrary_AudioVisualItem,
    extlibrary_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary_addressable_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Addressable)


def test_extlibrary_addressable_constructor_exists():
    assert callable(extlibrary_Addressable.__init__)


def test_extlibrary_addressable_constructor_args():
    sig = inspect.signature(extlibrary_Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_extlibrary_addressable_has_address():
    assert hasattr(extlibrary_Addressable, "address")
    descriptor = None
    for klass in extlibrary_Addressable.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(AudioVisualItem)


def test_audiovisualitem_constructor_exists():
    assert callable(AudioVisualItem.__init__)


def test_audiovisualitem_constructor_args():
    sig = inspect.signature(AudioVisualItem.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_videocassette_is_not_abstract():
    assert not inspect.isabstract(extlibrary_VideoCassette)


def test_extlibrary_videocassette_constructor_exists():
    assert callable(extlibrary_VideoCassette.__init__)


def test_extlibrary_videocassette_constructor_args():
    sig = inspect.signature(extlibrary_VideoCassette.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_bookontape_is_not_abstract():
    assert not inspect.isabstract(extlibrary_BookOnTape)


def test_extlibrary_bookontape_constructor_exists():
    assert callable(extlibrary_BookOnTape.__init__)


def test_extlibrary_bookontape_constructor_args():
    sig = inspect.signature(extlibrary_BookOnTape.__init__)
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



def test_extlibrary_periodical_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Periodical)


def test_extlibrary_periodical_constructor_exists():
    assert callable(extlibrary_Periodical.__init__)


def test_extlibrary_periodical_constructor_args():
    sig = inspect.signature(extlibrary_Periodical.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"

def test_extlibrary_periodical_has_title():
    assert hasattr(extlibrary_Periodical, "title")
    descriptor = None
    for klass in extlibrary_Periodical.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_periodical_has_issuesPerYear():
    assert hasattr(extlibrary_Periodical, "issuesPerYear")
    descriptor = None
    for klass in extlibrary_Periodical.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(extlibrary_CirculatingItem)


def test_extlibrary_circulatingitem_constructor_exists():
    assert callable(extlibrary_CirculatingItem.__init__)


def test_extlibrary_circulatingitem_constructor_args():
    sig = inspect.signature(extlibrary_CirculatingItem.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_lendable_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Lendable)


def test_extlibrary_lendable_constructor_exists():
    assert callable(extlibrary_Lendable.__init__)


def test_extlibrary_lendable_constructor_args():
    sig = inspect.signature(extlibrary_Lendable.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_extlibrary_lendable_has_copies():
    assert hasattr(extlibrary_Lendable, "copies")
    descriptor = None
    for klass in extlibrary_Lendable.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_item_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Item)


def test_extlibrary_item_constructor_exists():
    assert callable(extlibrary_Item.__init__)


def test_extlibrary_item_constructor_args():
    sig = inspect.signature(extlibrary_Item.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_extlibrary_item_has_publicationDate():
    assert hasattr(extlibrary_Item, "publicationDate")
    descriptor = None
    for klass in extlibrary_Item.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_borrower_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Borrower)


def test_extlibrary_borrower_constructor_exists():
    assert callable(extlibrary_Borrower.__init__)


def test_extlibrary_borrower_constructor_args():
    sig = inspect.signature(extlibrary_Borrower.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_employee_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Employee)


def test_extlibrary_employee_constructor_exists():
    assert callable(extlibrary_Employee.__init__)


def test_extlibrary_employee_constructor_args():
    sig = inspect.signature(extlibrary_Employee.__init__)
    params = list(sig.parameters.keys())



def test_addressable_is_not_abstract():
    assert not inspect.isabstract(Addressable)


def test_addressable_constructor_exists():
    assert callable(Addressable.__init__)


def test_addressable_constructor_args():
    sig = inspect.signature(Addressable.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_person_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Person)


def test_extlibrary_person_constructor_exists():
    assert callable(extlibrary_Person.__init__)


def test_extlibrary_person_constructor_args():
    sig = inspect.signature(extlibrary_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_extlibrary_person_has_firstName():
    assert hasattr(extlibrary_Person, "firstName")
    descriptor = None
    for klass in extlibrary_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_person_has_lastName():
    assert hasattr(extlibrary_Person, "lastName")
    descriptor = None
    for klass in extlibrary_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_library_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Library)


def test_extlibrary_library_constructor_exists():
    assert callable(extlibrary_Library.__init__)


def test_extlibrary_library_constructor_args():
    sig = inspect.signature(extlibrary_Library.__init__)
    params = list(sig.parameters.keys())
    assert "people" in params, "Missing parameter 'people'"
    assert "name" in params, "Missing parameter 'name'"

def test_extlibrary_library_has_people():
    assert hasattr(extlibrary_Library, "people")
    descriptor = None
    for klass in extlibrary_Library.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_library_has_name():
    assert hasattr(extlibrary_Library, "name")
    descriptor = None
    for klass in extlibrary_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_writer_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Writer)


def test_extlibrary_writer_constructor_exists():
    assert callable(extlibrary_Writer.__init__)


def test_extlibrary_writer_constructor_args():
    sig = inspect.signature(extlibrary_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extlibrary_writer_has_name():
    assert hasattr(extlibrary_Writer, "name")
    descriptor = None
    for klass in extlibrary_Writer.__mro__:
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



def test_extlibrary_audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(extlibrary_AudioVisualItem)


def test_extlibrary_audiovisualitem_constructor_exists():
    assert callable(extlibrary_AudioVisualItem.__init__)


def test_extlibrary_audiovisualitem_constructor_args():
    sig = inspect.signature(extlibrary_AudioVisualItem.__init__)
    params = list(sig.parameters.keys())
    assert "damaged" in params, "Missing parameter 'damaged'"
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"
    assert "title" in params, "Missing parameter 'title'"

def test_extlibrary_audiovisualitem_has_damaged():
    assert hasattr(extlibrary_AudioVisualItem, "damaged")
    descriptor = None
    for klass in extlibrary_AudioVisualItem.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_audiovisualitem_has_minutesLength():
    assert hasattr(extlibrary_AudioVisualItem, "minutesLength")
    descriptor = None
    for klass in extlibrary_AudioVisualItem.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_audiovisualitem_has_title():
    assert hasattr(extlibrary_AudioVisualItem, "title")
    descriptor = None
    for klass in extlibrary_AudioVisualItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_book_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Book)


def test_extlibrary_book_constructor_exists():
    assert callable(extlibrary_Book.__init__)


def test_extlibrary_book_constructor_args():
    sig = inspect.signature(extlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"

def test_extlibrary_book_has_pages():
    assert hasattr(extlibrary_Book, "pages")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_book_has_category():
    assert hasattr(extlibrary_Book, "category")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_book_has_title():
    assert hasattr(extlibrary_Book, "title")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
        "Biography",
        "Mystery",
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
extlibrary_Addressable_strategy = st.builds(
    extlibrary_Addressable,
    address=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
AudioVisualItem_strategy = st.builds(
    AudioVisualItem,
)
extlibrary_VideoCassette_strategy = st.builds(
    extlibrary_VideoCassette,
)
extlibrary_BookOnTape_strategy = st.builds(
    extlibrary_BookOnTape,
)
Lendable_strategy = st.builds(
    Lendable,
)
Item_strategy = st.builds(
    Item,
)
extlibrary_Periodical_strategy = st.builds(
    extlibrary_Periodical,
    title=
        safe_text,
    issuesPerYear=
        st.integers()
)
extlibrary_CirculatingItem_strategy = st.builds(
    extlibrary_CirculatingItem,
)
extlibrary_Lendable_strategy = st.builds(
    extlibrary_Lendable,
    copies=
        st.integers()
)
extlibrary_Item_strategy = st.builds(
    extlibrary_Item,
    publicationDate=
        st.dates()
)
extlibrary_Borrower_strategy = st.builds(
    extlibrary_Borrower,
)
extlibrary_Employee_strategy = st.builds(
    extlibrary_Employee,
)
Addressable_strategy = st.builds(
    Addressable,
)
extlibrary_Person_strategy = st.builds(
    extlibrary_Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)
extlibrary_Library_strategy = st.builds(
    extlibrary_Library,
    people=
        safe_text,
    name=
        safe_text
)
extlibrary_Writer_strategy = st.builds(
    extlibrary_Writer,
    name=
        safe_text
)
CirculatingItem_strategy = st.builds(
    CirculatingItem,
)
extlibrary_AudioVisualItem_strategy = st.builds(
    extlibrary_AudioVisualItem,
    damaged=
        st.booleans(),
    minutesLength=
        st.integers(),
    title=
        safe_text
)
extlibrary_Book_strategy = st.builds(
    extlibrary_Book,
    pages=
        st.integers(),
    category=
        safe_text,
    title=
        safe_text
)

@given(instance=extlibrary_Addressable_strategy)
@settings(max_examples=50)
def test_extlibrary_addressable_instantiation(instance):
    assert isinstance(instance, extlibrary_Addressable)



@given(instance=extlibrary_Addressable_strategy)
def test_extlibrary_addressable_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=AudioVisualItem_strategy)
@settings(max_examples=50)
def test_audiovisualitem_instantiation(instance):
    assert isinstance(instance, AudioVisualItem)

@given(instance=extlibrary_VideoCassette_strategy)
@settings(max_examples=50)
def test_extlibrary_videocassette_instantiation(instance):
    assert isinstance(instance, extlibrary_VideoCassette)

@given(instance=extlibrary_BookOnTape_strategy)
@settings(max_examples=50)
def test_extlibrary_bookontape_instantiation(instance):
    assert isinstance(instance, extlibrary_BookOnTape)

@given(instance=Lendable_strategy)
@settings(max_examples=50)
def test_lendable_instantiation(instance):
    assert isinstance(instance, Lendable)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=extlibrary_Periodical_strategy)
@settings(max_examples=50)
def test_extlibrary_periodical_instantiation(instance):
    assert isinstance(instance, extlibrary_Periodical)



@given(instance=extlibrary_Periodical_strategy)
def test_extlibrary_periodical_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=extlibrary_Periodical_strategy)
def test_extlibrary_periodical_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original

@given(instance=extlibrary_CirculatingItem_strategy)
@settings(max_examples=50)
def test_extlibrary_circulatingitem_instantiation(instance):
    assert isinstance(instance, extlibrary_CirculatingItem)

@given(instance=extlibrary_Lendable_strategy)
@settings(max_examples=50)
def test_extlibrary_lendable_instantiation(instance):
    assert isinstance(instance, extlibrary_Lendable)



@given(instance=extlibrary_Lendable_strategy)
def test_extlibrary_lendable_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=extlibrary_Item_strategy)
@settings(max_examples=50)
def test_extlibrary_item_instantiation(instance):
    assert isinstance(instance, extlibrary_Item)



@given(instance=extlibrary_Item_strategy)
def test_extlibrary_item_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=extlibrary_Borrower_strategy)
@settings(max_examples=50)
def test_extlibrary_borrower_instantiation(instance):
    assert isinstance(instance, extlibrary_Borrower)

@given(instance=extlibrary_Employee_strategy)
@settings(max_examples=50)
def test_extlibrary_employee_instantiation(instance):
    assert isinstance(instance, extlibrary_Employee)

@given(instance=Addressable_strategy)
@settings(max_examples=50)
def test_addressable_instantiation(instance):
    assert isinstance(instance, Addressable)

@given(instance=extlibrary_Person_strategy)
@settings(max_examples=50)
def test_extlibrary_person_instantiation(instance):
    assert isinstance(instance, extlibrary_Person)



@given(instance=extlibrary_Person_strategy)
def test_extlibrary_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=extlibrary_Person_strategy)
def test_extlibrary_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=extlibrary_Library_strategy)
@settings(max_examples=50)
def test_extlibrary_library_instantiation(instance):
    assert isinstance(instance, extlibrary_Library)



@given(instance=extlibrary_Library_strategy)
def test_extlibrary_library_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original



@given(instance=extlibrary_Library_strategy)
def test_extlibrary_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extlibrary_Writer_strategy)
@settings(max_examples=50)
def test_extlibrary_writer_instantiation(instance):
    assert isinstance(instance, extlibrary_Writer)



@given(instance=extlibrary_Writer_strategy)
def test_extlibrary_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CirculatingItem_strategy)
@settings(max_examples=50)
def test_circulatingitem_instantiation(instance):
    assert isinstance(instance, CirculatingItem)

@given(instance=extlibrary_AudioVisualItem_strategy)
@settings(max_examples=50)
def test_extlibrary_audiovisualitem_instantiation(instance):
    assert isinstance(instance, extlibrary_AudioVisualItem)



@given(instance=extlibrary_AudioVisualItem_strategy)
def test_extlibrary_audiovisualitem_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original



@given(instance=extlibrary_AudioVisualItem_strategy)
def test_extlibrary_audiovisualitem_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original



@given(instance=extlibrary_AudioVisualItem_strategy)
def test_extlibrary_audiovisualitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary_Book_strategy)
@settings(max_examples=50)
def test_extlibrary_book_instantiation(instance):
    assert isinstance(instance, extlibrary_Book)



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
