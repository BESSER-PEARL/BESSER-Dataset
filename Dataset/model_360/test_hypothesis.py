import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    tinylibrary::Person,
    tinylibrary::Writer,
    tinylibrary::Employee,
    tinylibrary::Book,
    tinylibrary::Library,
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



def test_tinylibrary::person_is_not_abstract():
    assert not inspect.isabstract(tinylibrary::Person)


def test_tinylibrary::person_constructor_exists():
    assert callable(tinylibrary::Person.__init__)


def test_tinylibrary::person_constructor_args():
    sig = inspect.signature(tinylibrary::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_tinylibrary::person_has_name():
    assert hasattr(tinylibrary::Person, "name")
    descriptor = None
    for klass in tinylibrary::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::person_has_lastName():
    assert hasattr(tinylibrary::Person, "lastName")
    descriptor = None
    for klass in tinylibrary::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::person_has_firstName():
    assert hasattr(tinylibrary::Person, "firstName")
    descriptor = None
    for klass in tinylibrary::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_tinylibrary::writer_is_not_abstract():
    assert not inspect.isabstract(tinylibrary::Writer)


def test_tinylibrary::writer_constructor_exists():
    assert callable(tinylibrary::Writer.__init__)


def test_tinylibrary::writer_constructor_args():
    sig = inspect.signature(tinylibrary::Writer.__init__)
    params = list(sig.parameters.keys())



def test_tinylibrary::employee_is_not_abstract():
    assert not inspect.isabstract(tinylibrary::Employee)


def test_tinylibrary::employee_constructor_exists():
    assert callable(tinylibrary::Employee.__init__)


def test_tinylibrary::employee_constructor_args():
    sig = inspect.signature(tinylibrary::Employee.__init__)
    params = list(sig.parameters.keys())



def test_tinylibrary::book_is_not_abstract():
    assert not inspect.isabstract(tinylibrary::Book)


def test_tinylibrary::book_constructor_exists():
    assert callable(tinylibrary::Book.__init__)


def test_tinylibrary::book_constructor_args():
    sig = inspect.signature(tinylibrary::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "damaged" in params, "Missing parameter 'damaged'"
    assert "title" in params, "Missing parameter 'title'"
    assert "published" in params, "Missing parameter 'published'"
    assert "category" in params, "Missing parameter 'category'"

def test_tinylibrary::book_has_pages():
    assert hasattr(tinylibrary::Book, "pages")
    descriptor = None
    for klass in tinylibrary::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::book_has_isbn():
    assert hasattr(tinylibrary::Book, "isbn")
    descriptor = None
    for klass in tinylibrary::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::book_has_damaged():
    assert hasattr(tinylibrary::Book, "damaged")
    descriptor = None
    for klass in tinylibrary::Book.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::book_has_title():
    assert hasattr(tinylibrary::Book, "title")
    descriptor = None
    for klass in tinylibrary::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::book_has_published():
    assert hasattr(tinylibrary::Book, "published")
    descriptor = None
    for klass in tinylibrary::Book.__mro__:
        if "published" in klass.__dict__:
            descriptor = klass.__dict__["published"]
            break
    assert isinstance(descriptor, property)

def test_tinylibrary::book_has_category():
    assert hasattr(tinylibrary::Book, "category")
    descriptor = None
    for klass in tinylibrary::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_tinylibrary::library_is_not_abstract():
    assert not inspect.isabstract(tinylibrary::Library)


def test_tinylibrary::library_constructor_exists():
    assert callable(tinylibrary::Library.__init__)


def test_tinylibrary::library_constructor_args():
    sig = inspect.signature(tinylibrary::Library.__init__)
    params = list(sig.parameters.keys())

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Mystery",
        "Computing",
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
Person_strategy = st.builds(
    Person,
)
tinylibrary::Person_strategy = st.builds(
    tinylibrary::Person,
    name=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text
)
tinylibrary::Writer_strategy = st.builds(
    tinylibrary::Writer,
)
tinylibrary::Employee_strategy = st.builds(
    tinylibrary::Employee,
)
tinylibrary::Book_strategy = st.builds(
    tinylibrary::Book,
    pages=
        safe_text,
    isbn=
        safe_text,
    damaged=
        safe_text,
    title=
        safe_text,
    published=
        st.dates(),
    category=
        safe_text
)
tinylibrary::Library_strategy = st.builds(
    tinylibrary::Library,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=tinylibrary::Person_strategy)
@settings(max_examples=50)
def test_tinylibrary::person_instantiation(instance):
    assert isinstance(instance, tinylibrary::Person)

@given(instance=tinylibrary::Person_strategy)
def test_tinylibrary::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tinylibrary::Person_strategy)
def test_tinylibrary::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tinylibrary::Person_strategy)
def test_tinylibrary::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=tinylibrary::Person_strategy)
def test_tinylibrary::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=tinylibrary::Person_strategy)
def test_tinylibrary::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=tinylibrary::Person_strategy)
def test_tinylibrary::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=tinylibrary::Writer_strategy)
@settings(max_examples=50)
def test_tinylibrary::writer_instantiation(instance):
    assert isinstance(instance, tinylibrary::Writer)

@given(instance=tinylibrary::Employee_strategy)
@settings(max_examples=50)
def test_tinylibrary::employee_instantiation(instance):
    assert isinstance(instance, tinylibrary::Employee)

@given(instance=tinylibrary::Book_strategy)
@settings(max_examples=50)
def test_tinylibrary::book_instantiation(instance):
    assert isinstance(instance, tinylibrary::Book)

@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_isbn_type(instance):
    assert isinstance(instance.isbn, str)


@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_damaged_type(instance):
    assert isinstance(instance.damaged, str)


@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_published_type(instance):
    assert isinstance(instance.published, date)


@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original

@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=tinylibrary::Book_strategy)
def test_tinylibrary::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=tinylibrary::Library_strategy)
@settings(max_examples=50)
def test_tinylibrary::library_instantiation(instance):
    assert isinstance(instance, tinylibrary::Library)
