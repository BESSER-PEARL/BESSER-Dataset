import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Ent,
    bookstore::Book,
    bookstore::Cd,
    bookstore::Magazine,
    bookstore::Dvd,
    bookstore::Person,
    bookstore::Ent,
    bookstore::Model,
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



def test_bookstore::book_is_not_abstract():
    assert not inspect.isabstract(bookstore::Book)


def test_bookstore::book_constructor_exists():
    assert callable(bookstore::Book.__init__)


def test_bookstore::book_constructor_args():
    sig = inspect.signature(bookstore::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_bookstore::book_has_title():
    assert hasattr(bookstore::Book, "title")
    descriptor = None
    for klass in bookstore::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bookstore::book_has_pages():
    assert hasattr(bookstore::Book, "pages")
    descriptor = None
    for klass in bookstore::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_bookstore::cd_is_not_abstract():
    assert not inspect.isabstract(bookstore::Cd)


def test_bookstore::cd_constructor_exists():
    assert callable(bookstore::Cd.__init__)


def test_bookstore::cd_constructor_args():
    sig = inspect.signature(bookstore::Cd.__init__)
    params = list(sig.parameters.keys())
    assert "albumName" in params, "Missing parameter 'albumName'"
    assert "bandArtist" in params, "Missing parameter 'bandArtist'"

def test_bookstore::cd_has_albumName():
    assert hasattr(bookstore::Cd, "albumName")
    descriptor = None
    for klass in bookstore::Cd.__mro__:
        if "albumName" in klass.__dict__:
            descriptor = klass.__dict__["albumName"]
            break
    assert isinstance(descriptor, property)

def test_bookstore::cd_has_bandArtist():
    assert hasattr(bookstore::Cd, "bandArtist")
    descriptor = None
    for klass in bookstore::Cd.__mro__:
        if "bandArtist" in klass.__dict__:
            descriptor = klass.__dict__["bandArtist"]
            break
    assert isinstance(descriptor, property)



def test_bookstore::magazine_is_not_abstract():
    assert not inspect.isabstract(bookstore::Magazine)


def test_bookstore::magazine_constructor_exists():
    assert callable(bookstore::Magazine.__init__)


def test_bookstore::magazine_constructor_args():
    sig = inspect.signature(bookstore::Magazine.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "version" in params, "Missing parameter 'version'"
    assert "title" in params, "Missing parameter 'title'"

def test_bookstore::magazine_has_pages():
    assert hasattr(bookstore::Magazine, "pages")
    descriptor = None
    for klass in bookstore::Magazine.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bookstore::magazine_has_version():
    assert hasattr(bookstore::Magazine, "version")
    descriptor = None
    for klass in bookstore::Magazine.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_bookstore::magazine_has_title():
    assert hasattr(bookstore::Magazine, "title")
    descriptor = None
    for klass in bookstore::Magazine.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bookstore::dvd_is_not_abstract():
    assert not inspect.isabstract(bookstore::Dvd)


def test_bookstore::dvd_constructor_exists():
    assert callable(bookstore::Dvd.__init__)


def test_bookstore::dvd_constructor_args():
    sig = inspect.signature(bookstore::Dvd.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_bookstore::dvd_has_title():
    assert hasattr(bookstore::Dvd, "title")
    descriptor = None
    for klass in bookstore::Dvd.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bookstore::person_is_not_abstract():
    assert not inspect.isabstract(bookstore::Person)


def test_bookstore::person_constructor_exists():
    assert callable(bookstore::Person.__init__)


def test_bookstore::person_constructor_args():
    sig = inspect.signature(bookstore::Person.__init__)
    params = list(sig.parameters.keys())
    assert "achternaam" in params, "Missing parameter 'achternaam'"
    assert "voornaam" in params, "Missing parameter 'voornaam'"

def test_bookstore::person_has_achternaam():
    assert hasattr(bookstore::Person, "achternaam")
    descriptor = None
    for klass in bookstore::Person.__mro__:
        if "achternaam" in klass.__dict__:
            descriptor = klass.__dict__["achternaam"]
            break
    assert isinstance(descriptor, property)

def test_bookstore::person_has_voornaam():
    assert hasattr(bookstore::Person, "voornaam")
    descriptor = None
    for klass in bookstore::Person.__mro__:
        if "voornaam" in klass.__dict__:
            descriptor = klass.__dict__["voornaam"]
            break
    assert isinstance(descriptor, property)



def test_bookstore::ent_is_not_abstract():
    assert not inspect.isabstract(bookstore::Ent)


def test_bookstore::ent_constructor_exists():
    assert callable(bookstore::Ent.__init__)


def test_bookstore::ent_constructor_args():
    sig = inspect.signature(bookstore::Ent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bookstore::ent_has_name():
    assert hasattr(bookstore::Ent, "name")
    descriptor = None
    for klass in bookstore::Ent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bookstore::model_is_not_abstract():
    assert not inspect.isabstract(bookstore::Model)


def test_bookstore::model_constructor_exists():
    assert callable(bookstore::Model.__init__)


def test_bookstore::model_constructor_args():
    sig = inspect.signature(bookstore::Model.__init__)
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
bookstore::Book_strategy = st.builds(
    bookstore::Book,
    title=
        safe_text,
    pages=
        st.integers()
)
bookstore::Cd_strategy = st.builds(
    bookstore::Cd,
    albumName=
        safe_text,
    bandArtist=
        safe_text
)
bookstore::Magazine_strategy = st.builds(
    bookstore::Magazine,
    pages=
        st.integers(),
    version=
        safe_text,
    title=
        safe_text
)
bookstore::Dvd_strategy = st.builds(
    bookstore::Dvd,
    title=
        safe_text
)
bookstore::Person_strategy = st.builds(
    bookstore::Person,
    achternaam=
        safe_text,
    voornaam=
        safe_text
)
bookstore::Ent_strategy = st.builds(
    bookstore::Ent,
    name=
        safe_text
)
bookstore::Model_strategy = st.builds(
    bookstore::Model,
)

@given(instance=Ent_strategy)
@settings(max_examples=50)
def test_ent_instantiation(instance):
    assert isinstance(instance, Ent)

@given(instance=bookstore::Book_strategy)
@settings(max_examples=50)
def test_bookstore::book_instantiation(instance):
    assert isinstance(instance, bookstore::Book)

@given(instance=bookstore::Book_strategy)
def test_bookstore::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bookstore::Book_strategy)
def test_bookstore::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bookstore::Book_strategy)
def test_bookstore::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=bookstore::Book_strategy)
def test_bookstore::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bookstore::Cd_strategy)
@settings(max_examples=50)
def test_bookstore::cd_instantiation(instance):
    assert isinstance(instance, bookstore::Cd)

@given(instance=bookstore::Cd_strategy)
def test_bookstore::cd_albumName_type(instance):
    assert isinstance(instance.albumName, str)


@given(instance=bookstore::Cd_strategy)
def test_bookstore::cd_albumName_setter(instance):
    original = instance.albumName
    instance.albumName = original
    assert instance.albumName == original

@given(instance=bookstore::Cd_strategy)
def test_bookstore::cd_bandArtist_type(instance):
    assert isinstance(instance.bandArtist, str)


@given(instance=bookstore::Cd_strategy)
def test_bookstore::cd_bandArtist_setter(instance):
    original = instance.bandArtist
    instance.bandArtist = original
    assert instance.bandArtist == original

@given(instance=bookstore::Magazine_strategy)
@settings(max_examples=50)
def test_bookstore::magazine_instantiation(instance):
    assert isinstance(instance, bookstore::Magazine)

@given(instance=bookstore::Magazine_strategy)
def test_bookstore::magazine_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=bookstore::Magazine_strategy)
def test_bookstore::magazine_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bookstore::Magazine_strategy)
def test_bookstore::magazine_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=bookstore::Magazine_strategy)
def test_bookstore::magazine_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=bookstore::Magazine_strategy)
def test_bookstore::magazine_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bookstore::Magazine_strategy)
def test_bookstore::magazine_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bookstore::Dvd_strategy)
@settings(max_examples=50)
def test_bookstore::dvd_instantiation(instance):
    assert isinstance(instance, bookstore::Dvd)

@given(instance=bookstore::Dvd_strategy)
def test_bookstore::dvd_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bookstore::Dvd_strategy)
def test_bookstore::dvd_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bookstore::Person_strategy)
@settings(max_examples=50)
def test_bookstore::person_instantiation(instance):
    assert isinstance(instance, bookstore::Person)

@given(instance=bookstore::Person_strategy)
def test_bookstore::person_achternaam_type(instance):
    assert isinstance(instance.achternaam, str)


@given(instance=bookstore::Person_strategy)
def test_bookstore::person_achternaam_setter(instance):
    original = instance.achternaam
    instance.achternaam = original
    assert instance.achternaam == original

@given(instance=bookstore::Person_strategy)
def test_bookstore::person_voornaam_type(instance):
    assert isinstance(instance.voornaam, str)


@given(instance=bookstore::Person_strategy)
def test_bookstore::person_voornaam_setter(instance):
    original = instance.voornaam
    instance.voornaam = original
    assert instance.voornaam == original

@given(instance=bookstore::Ent_strategy)
@settings(max_examples=50)
def test_bookstore::ent_instantiation(instance):
    assert isinstance(instance, bookstore::Ent)

@given(instance=bookstore::Ent_strategy)
def test_bookstore::ent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bookstore::Ent_strategy)
def test_bookstore::ent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bookstore::Model_strategy)
@settings(max_examples=50)
def test_bookstore::model_instantiation(instance):
    assert isinstance(instance, bookstore::Model)
