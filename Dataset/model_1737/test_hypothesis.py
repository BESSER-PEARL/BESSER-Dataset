import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ent,
    bookstore_Dvd,
    bookstore_Cd,
    bookstore_Magazine,
    bookstore_Book,
    bookstore_Person,
    bookstore_Ent,
    bookstore_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ent_is_not_abstract():
    assert not inspect.isabstract(Ent)


def test_ent_constructor_exists():
    assert callable(Ent.__init__)


def test_ent_constructor_args():
    sig = inspect.signature(Ent.__init__)
    params = list(sig.parameters.keys())



def test_bookstore_dvd_is_not_abstract():
    assert not inspect.isabstract(bookstore_Dvd)


def test_bookstore_dvd_constructor_exists():
    assert callable(bookstore_Dvd.__init__)


def test_bookstore_dvd_constructor_args():
    sig = inspect.signature(bookstore_Dvd.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_bookstore_dvd_has_title():
    assert hasattr(bookstore_Dvd, "title")
    descriptor = None
    for klass in bookstore_Dvd.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_cd_is_not_abstract():
    assert not inspect.isabstract(bookstore_Cd)


def test_bookstore_cd_constructor_exists():
    assert callable(bookstore_Cd.__init__)


def test_bookstore_cd_constructor_args():
    sig = inspect.signature(bookstore_Cd.__init__)
    params = list(sig.parameters.keys())
    assert "albumName" in params, "Missing parameter 'albumName'"
    assert "bandArtist" in params, "Missing parameter 'bandArtist'"

def test_bookstore_cd_has_albumName():
    assert hasattr(bookstore_Cd, "albumName")
    descriptor = None
    for klass in bookstore_Cd.__mro__:
        if "albumName" in klass.__dict__:
            descriptor = klass.__dict__["albumName"]
            break
    assert isinstance(descriptor, property)

def test_bookstore_cd_has_bandArtist():
    assert hasattr(bookstore_Cd, "bandArtist")
    descriptor = None
    for klass in bookstore_Cd.__mro__:
        if "bandArtist" in klass.__dict__:
            descriptor = klass.__dict__["bandArtist"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_magazine_is_not_abstract():
    assert not inspect.isabstract(bookstore_Magazine)


def test_bookstore_magazine_constructor_exists():
    assert callable(bookstore_Magazine.__init__)


def test_bookstore_magazine_constructor_args():
    sig = inspect.signature(bookstore_Magazine.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "version" in params, "Missing parameter 'version'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_bookstore_magazine_has_title():
    assert hasattr(bookstore_Magazine, "title")
    descriptor = None
    for klass in bookstore_Magazine.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bookstore_magazine_has_version():
    assert hasattr(bookstore_Magazine, "version")
    descriptor = None
    for klass in bookstore_Magazine.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_bookstore_magazine_has_pages():
    assert hasattr(bookstore_Magazine, "pages")
    descriptor = None
    for klass in bookstore_Magazine.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_book_is_not_abstract():
    assert not inspect.isabstract(bookstore_Book)


def test_bookstore_book_constructor_exists():
    assert callable(bookstore_Book.__init__)


def test_bookstore_book_constructor_args():
    sig = inspect.signature(bookstore_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_bookstore_book_has_title():
    assert hasattr(bookstore_Book, "title")
    descriptor = None
    for klass in bookstore_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bookstore_book_has_pages():
    assert hasattr(bookstore_Book, "pages")
    descriptor = None
    for klass in bookstore_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_person_is_not_abstract():
    assert not inspect.isabstract(bookstore_Person)


def test_bookstore_person_constructor_exists():
    assert callable(bookstore_Person.__init__)


def test_bookstore_person_constructor_args():
    sig = inspect.signature(bookstore_Person.__init__)
    params = list(sig.parameters.keys())
    assert "voornaam" in params, "Missing parameter 'voornaam'"
    assert "achternaam" in params, "Missing parameter 'achternaam'"

def test_bookstore_person_has_voornaam():
    assert hasattr(bookstore_Person, "voornaam")
    descriptor = None
    for klass in bookstore_Person.__mro__:
        if "voornaam" in klass.__dict__:
            descriptor = klass.__dict__["voornaam"]
            break
    assert isinstance(descriptor, property)

def test_bookstore_person_has_achternaam():
    assert hasattr(bookstore_Person, "achternaam")
    descriptor = None
    for klass in bookstore_Person.__mro__:
        if "achternaam" in klass.__dict__:
            descriptor = klass.__dict__["achternaam"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_ent_is_not_abstract():
    assert not inspect.isabstract(bookstore_Ent)


def test_bookstore_ent_constructor_exists():
    assert callable(bookstore_Ent.__init__)


def test_bookstore_ent_constructor_args():
    sig = inspect.signature(bookstore_Ent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bookstore_ent_has_name():
    assert hasattr(bookstore_Ent, "name")
    descriptor = None
    for klass in bookstore_Ent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_model_is_not_abstract():
    assert not inspect.isabstract(bookstore_Model)


def test_bookstore_model_constructor_exists():
    assert callable(bookstore_Model.__init__)


def test_bookstore_model_constructor_args():
    sig = inspect.signature(bookstore_Model.__init__)
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
Ent_strategy = st.builds(
    Ent,
)
bookstore_Dvd_strategy = st.builds(
    bookstore_Dvd,
    title=
        safe_text
)
bookstore_Cd_strategy = st.builds(
    bookstore_Cd,
    albumName=
        safe_text,
    bandArtist=
        safe_text
)
bookstore_Magazine_strategy = st.builds(
    bookstore_Magazine,
    title=
        safe_text,
    version=
        safe_text,
    pages=
        st.integers()
)
bookstore_Book_strategy = st.builds(
    bookstore_Book,
    title=
        safe_text,
    pages=
        st.integers()
)
bookstore_Person_strategy = st.builds(
    bookstore_Person,
    voornaam=
        safe_text,
    achternaam=
        safe_text
)
bookstore_Ent_strategy = st.builds(
    bookstore_Ent,
    name=
        safe_text
)
bookstore_Model_strategy = st.builds(
    bookstore_Model,
)

@given(instance=Ent_strategy)
@settings(max_examples=50)
def test_ent_instantiation(instance):
    assert isinstance(instance, Ent)

@given(instance=bookstore_Dvd_strategy)
@settings(max_examples=50)
def test_bookstore_dvd_instantiation(instance):
    assert isinstance(instance, bookstore_Dvd)



@given(instance=bookstore_Dvd_strategy)
def test_bookstore_dvd_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bookstore_Cd_strategy)
@settings(max_examples=50)
def test_bookstore_cd_instantiation(instance):
    assert isinstance(instance, bookstore_Cd)



@given(instance=bookstore_Cd_strategy)
def test_bookstore_cd_albumName_setter(instance):
    original = instance.albumName
    instance.albumName = original
    assert instance.albumName == original



@given(instance=bookstore_Cd_strategy)
def test_bookstore_cd_bandArtist_setter(instance):
    original = instance.bandArtist
    instance.bandArtist = original
    assert instance.bandArtist == original

@given(instance=bookstore_Magazine_strategy)
@settings(max_examples=50)
def test_bookstore_magazine_instantiation(instance):
    assert isinstance(instance, bookstore_Magazine)



@given(instance=bookstore_Magazine_strategy)
def test_bookstore_magazine_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=bookstore_Magazine_strategy)
def test_bookstore_magazine_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=bookstore_Magazine_strategy)
def test_bookstore_magazine_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bookstore_Book_strategy)
@settings(max_examples=50)
def test_bookstore_book_instantiation(instance):
    assert isinstance(instance, bookstore_Book)



@given(instance=bookstore_Book_strategy)
def test_bookstore_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=bookstore_Book_strategy)
def test_bookstore_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bookstore_Person_strategy)
@settings(max_examples=50)
def test_bookstore_person_instantiation(instance):
    assert isinstance(instance, bookstore_Person)



@given(instance=bookstore_Person_strategy)
def test_bookstore_person_voornaam_setter(instance):
    original = instance.voornaam
    instance.voornaam = original
    assert instance.voornaam == original



@given(instance=bookstore_Person_strategy)
def test_bookstore_person_achternaam_setter(instance):
    original = instance.achternaam
    instance.achternaam = original
    assert instance.achternaam == original

@given(instance=bookstore_Ent_strategy)
@settings(max_examples=50)
def test_bookstore_ent_instantiation(instance):
    assert isinstance(instance, bookstore_Ent)



@given(instance=bookstore_Ent_strategy)
def test_bookstore_ent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bookstore_Model_strategy)
@settings(max_examples=50)
def test_bookstore_model_instantiation(instance):
    assert isinstance(instance, bookstore_Model)
