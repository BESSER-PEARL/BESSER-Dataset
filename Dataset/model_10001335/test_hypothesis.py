import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    student_record,
    vendor,
    student,
    books_database,
    librarian,
    library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_student_record_is_not_abstract():
    assert not inspect.isabstract(student_record)


def test_student_record_constructor_exists():
    assert callable(student_record.__init__)


def test_student_record_constructor_args():
    sig = inspect.signature(student_record.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phone_number" in params, "Missing parameter 'phone_number'"
    assert "fines" in params, "Missing parameter 'fines'"
    assert "name" in params, "Missing parameter 'name'"

def test_student_record_has_address():
    assert hasattr(student_record, "address")
    descriptor = None
    for klass in student_record.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_student_record_has_phone_number():
    assert hasattr(student_record, "phone_number")
    descriptor = None
    for klass in student_record.__mro__:
        if "phone_number" in klass.__dict__:
            descriptor = klass.__dict__["phone_number"]
            break
    assert isinstance(descriptor, property)

def test_student_record_has_fines():
    assert hasattr(student_record, "fines")
    descriptor = None
    for klass in student_record.__mro__:
        if "fines" in klass.__dict__:
            descriptor = klass.__dict__["fines"]
            break
    assert isinstance(descriptor, property)

def test_student_record_has_name():
    assert hasattr(student_record, "name")
    descriptor = None
    for klass in student_record.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vendor_is_not_abstract():
    assert not inspect.isabstract(vendor)


def test_vendor_constructor_exists():
    assert callable(vendor.__init__)


def test_vendor_constructor_args():
    sig = inspect.signature(vendor.__init__)
    params = list(sig.parameters.keys())
    assert "book_details" in params, "Missing parameter 'book_details'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_vendor_has_book_details():
    assert hasattr(vendor, "book_details")
    descriptor = None
    for klass in vendor.__mro__:
        if "book_details" in klass.__dict__:
            descriptor = klass.__dict__["book_details"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_attribute():
    assert hasattr(vendor, "attribute")
    descriptor = None
    for klass in vendor.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_student_constructor_exists():
    assert callable(student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"

def test_student_has_details():
    assert hasattr(student, "details")
    descriptor = None
    for klass in student.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_books_database_is_not_abstract():
    assert not inspect.isabstract(books_database)


def test_books_database_constructor_exists():
    assert callable(books_database.__init__)


def test_books_database_constructor_args():
    sig = inspect.signature(books_database.__init__)
    params = list(sig.parameters.keys())
    assert "book_title" in params, "Missing parameter 'book_title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "book_id" in params, "Missing parameter 'book_id'"

def test_books_database_has_book_title():
    assert hasattr(books_database, "book_title")
    descriptor = None
    for klass in books_database.__mro__:
        if "book_title" in klass.__dict__:
            descriptor = klass.__dict__["book_title"]
            break
    assert isinstance(descriptor, property)

def test_books_database_has_author():
    assert hasattr(books_database, "author")
    descriptor = None
    for klass in books_database.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_books_database_has_book_id():
    assert hasattr(books_database, "book_id")
    descriptor = None
    for klass in books_database.__mro__:
        if "book_id" in klass.__dict__:
            descriptor = klass.__dict__["book_id"]
            break
    assert isinstance(descriptor, property)



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(librarian)


def test_librarian_constructor_exists():
    assert callable(librarian.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(librarian.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_librarian_has_name():
    assert hasattr(librarian, "name")
    descriptor = None
    for klass in librarian.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(library)


def test_library_constructor_exists():
    assert callable(library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(library.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_library_has_location():
    assert hasattr(library, "location")
    descriptor = None
    for klass in library.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)


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
student_record_strategy = st.builds(
    student_record,
    address=
        safe_text,
    phone_number=
        safe_text,
    fines=
        safe_text,
    name=
        safe_text
)
vendor_strategy = st.builds(
    vendor,
    book_details=
        safe_text,
    attribute=
        safe_text
)
student_strategy = st.builds(
    student,
    details=
        safe_text
)
books_database_strategy = st.builds(
    books_database,
    book_title=
        safe_text,
    author=
        safe_text,
    book_id=
        safe_text
)
librarian_strategy = st.builds(
    librarian,
    name=
        safe_text
)
library_strategy = st.builds(
    library,
    location=
        safe_text
)

@given(instance=student_record_strategy)
@settings(max_examples=50)
def test_student_record_instantiation(instance):
    assert isinstance(instance, student_record)



@given(instance=student_record_strategy)
def test_student_record_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=student_record_strategy)
def test_student_record_phone_number_setter(instance):
    original = instance.phone_number
    instance.phone_number = original
    assert instance.phone_number == original



@given(instance=student_record_strategy)
def test_student_record_fines_setter(instance):
    original = instance.fines
    instance.fines = original
    assert instance.fines == original



@given(instance=student_record_strategy)
def test_student_record_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vendor_strategy)
@settings(max_examples=50)
def test_vendor_instantiation(instance):
    assert isinstance(instance, vendor)



@given(instance=vendor_strategy)
def test_vendor_book_details_setter(instance):
    original = instance.book_details
    instance.book_details = original
    assert instance.book_details == original



@given(instance=vendor_strategy)
def test_vendor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, student)



@given(instance=student_strategy)
def test_student_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=books_database_strategy)
@settings(max_examples=50)
def test_books_database_instantiation(instance):
    assert isinstance(instance, books_database)



@given(instance=books_database_strategy)
def test_books_database_book_title_setter(instance):
    original = instance.book_title
    instance.book_title = original
    assert instance.book_title == original



@given(instance=books_database_strategy)
def test_books_database_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=books_database_strategy)
def test_books_database_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original

@given(instance=librarian_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, librarian)



@given(instance=librarian_strategy)
def test_librarian_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, library)



@given(instance=library_strategy)
def test_library_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
