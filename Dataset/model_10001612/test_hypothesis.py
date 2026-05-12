import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Member,
    Book,
    Guest,
    log,
    Admin,
    Librarian,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"
    assert "username" in params, "Missing parameter 'username'"
    assert "id" in params, "Missing parameter 'id'"

def test_member_has_password():
    assert hasattr(Member, "password")
    descriptor = None
    for klass in Member.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_member_has_name():
    assert hasattr(Member, "name")
    descriptor = None
    for klass in Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_member_has_username():
    assert hasattr(Member, "username")
    descriptor = None
    for klass in Member.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_member_has_id():
    assert hasattr(Member, "id")
    descriptor = None
    for klass in Member.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "author" in params, "Missing parameter 'author'"

def test_book_has_name():
    assert hasattr(Book, "name")
    descriptor = None
    for klass in Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())



def test_log_is_not_abstract():
    assert not inspect.isabstract(log)


def test_log_constructor_exists():
    assert callable(log.__init__)


def test_log_constructor_args():
    sig = inspect.signature(log.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

def test_admin_has_username():
    assert hasattr(Admin, "username")
    descriptor = None
    for klass in Admin.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_id():
    assert hasattr(Admin, "id")
    descriptor = None
    for klass in Admin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(Librarian)


def test_librarian_constructor_exists():
    assert callable(Librarian.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(Librarian.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_librarian_has_attribute():
    assert hasattr(Librarian, "attribute")
    descriptor = None
    for klass in Librarian.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_id():
    assert hasattr(Librarian, "id")
    descriptor = None
    for klass in Librarian.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_password():
    assert hasattr(Librarian, "password")
    descriptor = None
    for klass in Librarian.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
Member_strategy = st.builds(
    Member,
    password=
        safe_text,
    name=
        safe_text,
    username=
        safe_text,
    id=
        st.integers()
)
Book_strategy = st.builds(
    Book,
    name=
        safe_text,
    author=
        safe_text
)
Guest_strategy = st.builds(
    Guest,
)
log_strategy = st.builds(
    log,
)
Admin_strategy = st.builds(
    Admin,
    username=
        safe_text,
    password=
        safe_text,
    id=
        st.integers()
)
Librarian_strategy = st.builds(
    Librarian,
    attribute=
        safe_text,
    id=
        st.integers(),
    password=
        safe_text
)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)



@given(instance=Member_strategy)
def test_member_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Member_strategy)
def test_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Member_strategy)
def test_member_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Member_strategy)
def test_member_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Book_strategy)
def test_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)

@given(instance=log_strategy)
@settings(max_examples=50)
def test_log_instantiation(instance):
    assert isinstance(instance, log)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Librarian_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, Librarian)



@given(instance=Librarian_strategy)
def test_librarian_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Librarian_strategy)
def test_librarian_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Librarian_strategy)
def test_librarian_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
