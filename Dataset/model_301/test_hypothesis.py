import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Item,
    Library_Lendable,
    CirculatingItem,
    Library_Book,
    Person,
    Library_Item,
    Library_Borrower,
    Library_Employee,
    Addressable,
    Library_Library,
    Library_Writer,
    Library_Addressable,
    Library_Person,
    AudioVisualItem,
    Library_VideoCassette,
    Library_BookOnTape,
    Library_AudioVisualItem,
    Library_Periodical,
    Lendable,
    Library_CirculatingItem,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_library_lendable_is_not_abstract():
    assert not inspect.isabstract(Library_Lendable)


def test_library_lendable_constructor_exists():
    assert callable(Library_Lendable.__init__)


def test_library_lendable_constructor_args():
    sig = inspect.signature(Library_Lendable.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_library_lendable_has_copies():
    assert hasattr(Library_Lendable, "copies")
    descriptor = None
    for klass in Library_Lendable.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(CirculatingItem)


def test_circulatingitem_constructor_exists():
    assert callable(CirculatingItem.__init__)


def test_circulatingitem_constructor_args():
    sig = inspect.signature(CirculatingItem.__init__)
    params = list(sig.parameters.keys())



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(Library_Book)


def test_library_book_constructor_exists():
    assert callable(Library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(Library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_library_book_has_category():
    assert hasattr(Library_Book, "category")
    descriptor = None
    for klass in Library_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_title():
    assert hasattr(Library_Book, "title")
    descriptor = None
    for klass in Library_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_pages():
    assert hasattr(Library_Book, "pages")
    descriptor = None
    for klass in Library_Book.__mro__:
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



def test_library_item_is_not_abstract():
    assert not inspect.isabstract(Library_Item)


def test_library_item_constructor_exists():
    assert callable(Library_Item.__init__)


def test_library_item_constructor_args():
    sig = inspect.signature(Library_Item.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_library_item_has_publicationDate():
    assert hasattr(Library_Item, "publicationDate")
    descriptor = None
    for klass in Library_Item.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_library_borrower_is_not_abstract():
    assert not inspect.isabstract(Library_Borrower)


def test_library_borrower_constructor_exists():
    assert callable(Library_Borrower.__init__)


def test_library_borrower_constructor_args():
    sig = inspect.signature(Library_Borrower.__init__)
    params = list(sig.parameters.keys())



def test_library_employee_is_not_abstract():
    assert not inspect.isabstract(Library_Employee)


def test_library_employee_constructor_exists():
    assert callable(Library_Employee.__init__)


def test_library_employee_constructor_args():
    sig = inspect.signature(Library_Employee.__init__)
    params = list(sig.parameters.keys())



def test_addressable_is_not_abstract():
    assert not inspect.isabstract(Addressable)


def test_addressable_constructor_exists():
    assert callable(Addressable.__init__)


def test_addressable_constructor_args():
    sig = inspect.signature(Addressable.__init__)
    params = list(sig.parameters.keys())



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(Library_Library)


def test_library_library_constructor_exists():
    assert callable(Library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(Library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "people" in params, "Missing parameter 'people'"

def test_library_library_has_name():
    assert hasattr(Library_Library, "name")
    descriptor = None
    for klass in Library_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library_library_has_people():
    assert hasattr(Library_Library, "people")
    descriptor = None
    for klass in Library_Library.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)



def test_library_writer_is_not_abstract():
    assert not inspect.isabstract(Library_Writer)


def test_library_writer_constructor_exists():
    assert callable(Library_Writer.__init__)


def test_library_writer_constructor_args():
    sig = inspect.signature(Library_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_writer_has_name():
    assert hasattr(Library_Writer, "name")
    descriptor = None
    for klass in Library_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_addressable_is_not_abstract():
    assert not inspect.isabstract(Library_Addressable)


def test_library_addressable_constructor_exists():
    assert callable(Library_Addressable.__init__)


def test_library_addressable_constructor_args():
    sig = inspect.signature(Library_Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library_addressable_has_address():
    assert hasattr(Library_Addressable, "address")
    descriptor = None
    for klass in Library_Addressable.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_library_person_is_not_abstract():
    assert not inspect.isabstract(Library_Person)


def test_library_person_constructor_exists():
    assert callable(Library_Person.__init__)


def test_library_person_constructor_args():
    sig = inspect.signature(Library_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_library_person_has_firstName():
    assert hasattr(Library_Person, "firstName")
    descriptor = None
    for klass in Library_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_library_person_has_lastName():
    assert hasattr(Library_Person, "lastName")
    descriptor = None
    for klass in Library_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(AudioVisualItem)


def test_audiovisualitem_constructor_exists():
    assert callable(AudioVisualItem.__init__)


def test_audiovisualitem_constructor_args():
    sig = inspect.signature(AudioVisualItem.__init__)
    params = list(sig.parameters.keys())



def test_library_videocassette_is_not_abstract():
    assert not inspect.isabstract(Library_VideoCassette)


def test_library_videocassette_constructor_exists():
    assert callable(Library_VideoCassette.__init__)


def test_library_videocassette_constructor_args():
    sig = inspect.signature(Library_VideoCassette.__init__)
    params = list(sig.parameters.keys())



def test_library_bookontape_is_not_abstract():
    assert not inspect.isabstract(Library_BookOnTape)


def test_library_bookontape_constructor_exists():
    assert callable(Library_BookOnTape.__init__)


def test_library_bookontape_constructor_args():
    sig = inspect.signature(Library_BookOnTape.__init__)
    params = list(sig.parameters.keys())



def test_library_audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(Library_AudioVisualItem)


def test_library_audiovisualitem_constructor_exists():
    assert callable(Library_AudioVisualItem.__init__)


def test_library_audiovisualitem_constructor_args():
    sig = inspect.signature(Library_AudioVisualItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_library_audiovisualitem_has_title():
    assert hasattr(Library_AudioVisualItem, "title")
    descriptor = None
    for klass in Library_AudioVisualItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library_audiovisualitem_has_minutesLength():
    assert hasattr(Library_AudioVisualItem, "minutesLength")
    descriptor = None
    for klass in Library_AudioVisualItem.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)

def test_library_audiovisualitem_has_damaged():
    assert hasattr(Library_AudioVisualItem, "damaged")
    descriptor = None
    for klass in Library_AudioVisualItem.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_library_periodical_is_not_abstract():
    assert not inspect.isabstract(Library_Periodical)


def test_library_periodical_constructor_exists():
    assert callable(Library_Periodical.__init__)


def test_library_periodical_constructor_args():
    sig = inspect.signature(Library_Periodical.__init__)
    params = list(sig.parameters.keys())
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"
    assert "title" in params, "Missing parameter 'title'"

def test_library_periodical_has_issuesPerYear():
    assert hasattr(Library_Periodical, "issuesPerYear")
    descriptor = None
    for klass in Library_Periodical.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)

def test_library_periodical_has_title():
    assert hasattr(Library_Periodical, "title")
    descriptor = None
    for klass in Library_Periodical.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lendable_is_not_abstract():
    assert not inspect.isabstract(Lendable)


def test_lendable_constructor_exists():
    assert callable(Lendable.__init__)


def test_lendable_constructor_args():
    sig = inspect.signature(Lendable.__init__)
    params = list(sig.parameters.keys())



def test_library_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(Library_CirculatingItem)


def test_library_circulatingitem_constructor_exists():
    assert callable(Library_CirculatingItem.__init__)


def test_library_circulatingitem_constructor_args():
    sig = inspect.signature(Library_CirculatingItem.__init__)
    params = list(sig.parameters.keys())

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Mystery",
        "Biography",
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
Item_strategy = st.builds(
    Item,
)
Library_Lendable_strategy = st.builds(
    Library_Lendable,
    copies=
        st.integers()
)
CirculatingItem_strategy = st.builds(
    CirculatingItem,
)
Library_Book_strategy = st.builds(
    Library_Book,
    category=
        safe_text,
    title=
        safe_text,
    pages=
        st.integers()
)
Person_strategy = st.builds(
    Person,
)
Library_Item_strategy = st.builds(
    Library_Item,
    publicationDate=
        st.dates()
)
Library_Borrower_strategy = st.builds(
    Library_Borrower,
)
Library_Employee_strategy = st.builds(
    Library_Employee,
)
Addressable_strategy = st.builds(
    Addressable,
)
Library_Library_strategy = st.builds(
    Library_Library,
    name=
        safe_text,
    people=
        safe_text
)
Library_Writer_strategy = st.builds(
    Library_Writer,
    name=
        safe_text
)
Library_Addressable_strategy = st.builds(
    Library_Addressable,
    address=
        safe_text
)
Library_Person_strategy = st.builds(
    Library_Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)
AudioVisualItem_strategy = st.builds(
    AudioVisualItem,
)
Library_VideoCassette_strategy = st.builds(
    Library_VideoCassette,
)
Library_BookOnTape_strategy = st.builds(
    Library_BookOnTape,
)
Library_AudioVisualItem_strategy = st.builds(
    Library_AudioVisualItem,
    title=
        safe_text,
    minutesLength=
        st.integers(),
    damaged=
        st.booleans()
)
Library_Periodical_strategy = st.builds(
    Library_Periodical,
    issuesPerYear=
        st.integers(),
    title=
        safe_text
)
Lendable_strategy = st.builds(
    Lendable,
)
Library_CirculatingItem_strategy = st.builds(
    Library_CirculatingItem,
)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=Library_Lendable_strategy)
@settings(max_examples=50)
def test_library_lendable_instantiation(instance):
    assert isinstance(instance, Library_Lendable)



@given(instance=Library_Lendable_strategy)
def test_library_lendable_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=CirculatingItem_strategy)
@settings(max_examples=50)
def test_circulatingitem_instantiation(instance):
    assert isinstance(instance, CirculatingItem)

@given(instance=Library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, Library_Book)



@given(instance=Library_Book_strategy)
def test_library_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Library_Book_strategy)
def test_library_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Library_Book_strategy)
def test_library_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Library_Item_strategy)
@settings(max_examples=50)
def test_library_item_instantiation(instance):
    assert isinstance(instance, Library_Item)



@given(instance=Library_Item_strategy)
def test_library_item_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=Library_Borrower_strategy)
@settings(max_examples=50)
def test_library_borrower_instantiation(instance):
    assert isinstance(instance, Library_Borrower)

@given(instance=Library_Employee_strategy)
@settings(max_examples=50)
def test_library_employee_instantiation(instance):
    assert isinstance(instance, Library_Employee)

@given(instance=Addressable_strategy)
@settings(max_examples=50)
def test_addressable_instantiation(instance):
    assert isinstance(instance, Addressable)

@given(instance=Library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, Library_Library)



@given(instance=Library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Library_Library_strategy)
def test_library_library_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original

@given(instance=Library_Writer_strategy)
@settings(max_examples=50)
def test_library_writer_instantiation(instance):
    assert isinstance(instance, Library_Writer)



@given(instance=Library_Writer_strategy)
def test_library_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library_Addressable_strategy)
@settings(max_examples=50)
def test_library_addressable_instantiation(instance):
    assert isinstance(instance, Library_Addressable)



@given(instance=Library_Addressable_strategy)
def test_library_addressable_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Library_Person_strategy)
@settings(max_examples=50)
def test_library_person_instantiation(instance):
    assert isinstance(instance, Library_Person)



@given(instance=Library_Person_strategy)
def test_library_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Library_Person_strategy)
def test_library_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=AudioVisualItem_strategy)
@settings(max_examples=50)
def test_audiovisualitem_instantiation(instance):
    assert isinstance(instance, AudioVisualItem)

@given(instance=Library_VideoCassette_strategy)
@settings(max_examples=50)
def test_library_videocassette_instantiation(instance):
    assert isinstance(instance, Library_VideoCassette)

@given(instance=Library_BookOnTape_strategy)
@settings(max_examples=50)
def test_library_bookontape_instantiation(instance):
    assert isinstance(instance, Library_BookOnTape)

@given(instance=Library_AudioVisualItem_strategy)
@settings(max_examples=50)
def test_library_audiovisualitem_instantiation(instance):
    assert isinstance(instance, Library_AudioVisualItem)



@given(instance=Library_AudioVisualItem_strategy)
def test_library_audiovisualitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Library_AudioVisualItem_strategy)
def test_library_audiovisualitem_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original



@given(instance=Library_AudioVisualItem_strategy)
def test_library_audiovisualitem_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=Library_Periodical_strategy)
@settings(max_examples=50)
def test_library_periodical_instantiation(instance):
    assert isinstance(instance, Library_Periodical)



@given(instance=Library_Periodical_strategy)
def test_library_periodical_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original



@given(instance=Library_Periodical_strategy)
def test_library_periodical_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Lendable_strategy)
@settings(max_examples=50)
def test_lendable_instantiation(instance):
    assert isinstance(instance, Lendable)

@given(instance=Library_CirculatingItem_strategy)
@settings(max_examples=50)
def test_library_circulatingitem_instantiation(instance):
    assert isinstance(instance, Library_CirculatingItem)
