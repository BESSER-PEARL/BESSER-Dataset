import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Staff,
    Media,
    Computer,
    Patron,
    Magazine,
    Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_staff_has_name():
    assert hasattr(Staff, "name")
    descriptor = None
    for klass in Staff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_id():
    assert hasattr(Staff, "id")
    descriptor = None
    for klass in Staff.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_media_is_not_abstract():
    assert not inspect.isabstract(Media)


def test_media_constructor_exists():
    assert callable(Media.__init__)


def test_media_constructor_args():
    sig = inspect.signature(Media.__init__)
    params = list(sig.parameters.keys())
    assert "refNum" in params, "Missing parameter 'refNum'"
    assert "type" in params, "Missing parameter 'type'"

def test_media_has_refNum():
    assert hasattr(Media, "refNum")
    descriptor = None
    for klass in Media.__mro__:
        if "refNum" in klass.__dict__:
            descriptor = klass.__dict__["refNum"]
            break
    assert isinstance(descriptor, property)

def test_media_has_type():
    assert hasattr(Media, "type")
    descriptor = None
    for klass in Media.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_computer_is_not_abstract():
    assert not inspect.isabstract(Computer)


def test_computer_constructor_exists():
    assert callable(Computer.__init__)


def test_computer_constructor_args():
    sig = inspect.signature(Computer.__init__)
    params = list(sig.parameters.keys())
    assert "compID" in params, "Missing parameter 'compID'"

def test_computer_has_compID():
    assert hasattr(Computer, "compID")
    descriptor = None
    for klass in Computer.__mro__:
        if "compID" in klass.__dict__:
            descriptor = klass.__dict__["compID"]
            break
    assert isinstance(descriptor, property)



def test_patron_is_not_abstract():
    assert not inspect.isabstract(Patron)


def test_patron_constructor_exists():
    assert callable(Patron.__init__)


def test_patron_constructor_args():
    sig = inspect.signature(Patron.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_patron_has_position():
    assert hasattr(Patron, "position")
    descriptor = None
    for klass in Patron.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_id():
    assert hasattr(Patron, "id")
    descriptor = None
    for klass in Patron.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_name():
    assert hasattr(Patron, "name")
    descriptor = None
    for klass in Patron.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_magazine_is_not_abstract():
    assert not inspect.isabstract(Magazine)


def test_magazine_constructor_exists():
    assert callable(Magazine.__init__)


def test_magazine_constructor_args():
    sig = inspect.signature(Magazine.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "issueNum" in params, "Missing parameter 'issueNum'"

def test_magazine_has_location():
    assert hasattr(Magazine, "location")
    descriptor = None
    for klass in Magazine.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_magazine_has_name():
    assert hasattr(Magazine, "name")
    descriptor = None
    for klass in Magazine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_magazine_has_issueNum():
    assert hasattr(Magazine, "issueNum")
    descriptor = None
    for klass in Magazine.__mro__:
        if "issueNum" in klass.__dict__:
            descriptor = klass.__dict__["issueNum"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "refNum" in params, "Missing parameter 'refNum'"
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"
    assert "dueDate" in params, "Missing parameter 'dueDate'"

def test_book_has_refNum():
    assert hasattr(Book, "refNum")
    descriptor = None
    for klass in Book.__mro__:
        if "refNum" in klass.__dict__:
            descriptor = klass.__dict__["refNum"]
            break
    assert isinstance(descriptor, property)

def test_book_has_author():
    assert hasattr(Book, "author")
    descriptor = None
    for klass in Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_has_title():
    assert hasattr(Book, "title")
    descriptor = None
    for klass in Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book_has_dueDate():
    assert hasattr(Book, "dueDate")
    descriptor = None
    for klass in Book.__mro__:
        if "dueDate" in klass.__dict__:
            descriptor = klass.__dict__["dueDate"]
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
Staff_strategy = st.builds(
    Staff,
    name=
        safe_text,
    id=
        st.integers()
)
Media_strategy = st.builds(
    Media,
    refNum=
        st.integers(),
    type=
        st.integers()
)
Computer_strategy = st.builds(
    Computer,
    compID=
        st.integers()
)
Patron_strategy = st.builds(
    Patron,
    position=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
Magazine_strategy = st.builds(
    Magazine,
    location=
        safe_text,
    name=
        safe_text,
    issueNum=
        st.integers()
)
Book_strategy = st.builds(
    Book,
    refNum=
        st.integers(),
    author=
        safe_text,
    title=
        safe_text,
    dueDate=
        safe_text
)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_strategy)
def test_staff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Media_strategy)
@settings(max_examples=50)
def test_media_instantiation(instance):
    assert isinstance(instance, Media)



@given(instance=Media_strategy)
def test_media_refNum_setter(instance):
    original = instance.refNum
    instance.refNum = original
    assert instance.refNum == original



@given(instance=Media_strategy)
def test_media_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Computer_strategy)
@settings(max_examples=50)
def test_computer_instantiation(instance):
    assert isinstance(instance, Computer)



@given(instance=Computer_strategy)
def test_computer_compID_setter(instance):
    original = instance.compID
    instance.compID = original
    assert instance.compID == original

@given(instance=Patron_strategy)
@settings(max_examples=50)
def test_patron_instantiation(instance):
    assert isinstance(instance, Patron)



@given(instance=Patron_strategy)
def test_patron_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Patron_strategy)
def test_patron_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patron_strategy)
def test_patron_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Magazine_strategy)
@settings(max_examples=50)
def test_magazine_instantiation(instance):
    assert isinstance(instance, Magazine)



@given(instance=Magazine_strategy)
def test_magazine_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Magazine_strategy)
def test_magazine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Magazine_strategy)
def test_magazine_issueNum_setter(instance):
    original = instance.issueNum
    instance.issueNum = original
    assert instance.issueNum == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_refNum_setter(instance):
    original = instance.refNum
    instance.refNum = original
    assert instance.refNum == original



@given(instance=Book_strategy)
def test_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=Book_strategy)
def test_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Book_strategy)
def test_book_dueDate_setter(instance):
    original = instance.dueDate
    instance.dueDate = original
    assert instance.dueDate == original
