import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    tinylibrary_Person,
    tinylibrary_Writer,
    tinylibrary_Employee,
    tinylibrary_Book,
    tinylibrary_Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_tinylibrary_person_is_not_abstract():
    assert not inspect.isabstract(tinylibrary_Person)


def test_tinylibrary_person_constructor_exists():
    assert callable(tinylibrary_Person.__init__)


def test_tinylibrary_person_constructor_args():
    sig = inspect.signature(tinylibrary_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_tinylibrary_person_has_lastName():
    assert hasattr(tinylibrary_Person, "lastName")
    descriptor = None
    for klass in tinylibrary_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_person_has_name():
    assert hasattr(tinylibrary_Person, "name")
    descriptor = None
    for klass in tinylibrary_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_person_has_firstName():
    assert hasattr(tinylibrary_Person, "firstName")
    descriptor = None
    for klass in tinylibrary_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_tinylibrary_writer_is_not_abstract():
    assert not inspect.isabstract(tinylibrary_Writer)


def test_tinylibrary_writer_constructor_exists():
    assert callable(tinylibrary_Writer.__init__)


def test_tinylibrary_writer_constructor_args():
    sig = inspect.signature(tinylibrary_Writer.__init__)
    params = list(sig.parameters.keys())



def test_tinylibrary_employee_is_not_abstract():
    assert not inspect.isabstract(tinylibrary_Employee)


def test_tinylibrary_employee_constructor_exists():
    assert callable(tinylibrary_Employee.__init__)


def test_tinylibrary_employee_constructor_args():
    sig = inspect.signature(tinylibrary_Employee.__init__)
    params = list(sig.parameters.keys())



def test_tinylibrary_book_is_not_abstract():
    assert not inspect.isabstract(tinylibrary_Book)


def test_tinylibrary_book_constructor_exists():
    assert callable(tinylibrary_Book.__init__)


def test_tinylibrary_book_constructor_args():
    sig = inspect.signature(tinylibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "published" in params, "Missing parameter 'published'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "damaged" in params, "Missing parameter 'damaged'"
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_tinylibrary_book_has_title():
    assert hasattr(tinylibrary_Book, "title")
    descriptor = None
    for klass in tinylibrary_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_book_has_published():
    assert hasattr(tinylibrary_Book, "published")
    descriptor = None
    for klass in tinylibrary_Book.__mro__:
        if "published" in klass.__dict__:
            descriptor = klass.__dict__["published"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_book_has_pages():
    assert hasattr(tinylibrary_Book, "pages")
    descriptor = None
    for klass in tinylibrary_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_book_has_category():
    assert hasattr(tinylibrary_Book, "category")
    descriptor = None
    for klass in tinylibrary_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_book_has_damaged():
    assert hasattr(tinylibrary_Book, "damaged")
    descriptor = None
    for klass in tinylibrary_Book.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary_book_has_isbn():
    assert hasattr(tinylibrary_Book, "isbn")
    descriptor = None
    for klass in tinylibrary_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_tinylibrary_library_is_not_abstract():
    assert not inspect.isabstract(tinylibrary_Library)


def test_tinylibrary_library_constructor_exists():
    assert callable(tinylibrary_Library.__init__)


def test_tinylibrary_library_constructor_args():
    sig = inspect.signature(tinylibrary_Library.__init__)
    params = list(sig.parameters.keys())

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Biography",
        "Computing",
        "ScienceFiction",
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
Person_strategy = st.builds(
    Person,
)
tinylibrary_Person_strategy = st.builds(
    tinylibrary_Person,
    lastName=
        safe_text,
    name=
        safe_text,
    firstName=
        safe_text
)
tinylibrary_Writer_strategy = st.builds(
    tinylibrary_Writer,
)
tinylibrary_Employee_strategy = st.builds(
    tinylibrary_Employee,
)
tinylibrary_Book_strategy = st.builds(
    tinylibrary_Book,
    title=
        safe_text,
    published=
        st.dates(),
    pages=
        safe_text,
    category=
        safe_text,
    damaged=
        safe_text,
    isbn=
        safe_text
)
tinylibrary_Library_strategy = st.builds(
    tinylibrary_Library,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=tinylibrary_Person_strategy)
@settings(max_examples=50)
def test_tinylibrary_person_instantiation(instance):
    assert isinstance(instance, tinylibrary_Person)



@given(instance=tinylibrary_Person_strategy)
def test_tinylibrary_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=tinylibrary_Person_strategy)
def test_tinylibrary_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tinylibrary_Person_strategy)
def test_tinylibrary_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=tinylibrary_Writer_strategy)
@settings(max_examples=50)
def test_tinylibrary_writer_instantiation(instance):
    assert isinstance(instance, tinylibrary_Writer)

@given(instance=tinylibrary_Employee_strategy)
@settings(max_examples=50)
def test_tinylibrary_employee_instantiation(instance):
    assert isinstance(instance, tinylibrary_Employee)

@given(instance=tinylibrary_Book_strategy)
@settings(max_examples=50)
def test_tinylibrary_book_instantiation(instance):
    assert isinstance(instance, tinylibrary_Book)



@given(instance=tinylibrary_Book_strategy)
def test_tinylibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=tinylibrary_Book_strategy)
def test_tinylibrary_book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original



@given(instance=tinylibrary_Book_strategy)
def test_tinylibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=tinylibrary_Book_strategy)
def test_tinylibrary_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=tinylibrary_Book_strategy)
def test_tinylibrary_book_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original



@given(instance=tinylibrary_Book_strategy)
def test_tinylibrary_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=tinylibrary_Library_strategy)
@settings(max_examples=50)
def test_tinylibrary_library_instantiation(instance):
    assert isinstance(instance, tinylibrary_Library)
