import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    comicBookCollection::Publisher,
    comicBookCollection::ComicBookCollection,
    comicBookCollection::Person,
    comicBookCollection::Book,
    comicBookCollection::Series,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comicbookcollection::publisher_is_not_abstract():
    assert not inspect.isabstract(comicBookCollection::Publisher)


def test_comicbookcollection::publisher_constructor_exists():
    assert callable(comicBookCollection::Publisher.__init__)


def test_comicbookcollection::publisher_constructor_args():
    sig = inspect.signature(comicBookCollection::Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "publishingName" in params, "Missing parameter 'publishingName'"

def test_comicbookcollection::publisher_has_publishingName():
    assert hasattr(comicBookCollection::Publisher, "publishingName")
    descriptor = None
    for klass in comicBookCollection::Publisher.__mro__:
        if "publishingName" in klass.__dict__:
            descriptor = klass.__dict__["publishingName"]
            break
    assert isinstance(descriptor, property)



def test_comicbookcollection::comicbookcollection_is_not_abstract():
    assert not inspect.isabstract(comicBookCollection::ComicBookCollection)


def test_comicbookcollection::comicbookcollection_constructor_exists():
    assert callable(comicBookCollection::ComicBookCollection.__init__)


def test_comicbookcollection::comicbookcollection_constructor_args():
    sig = inspect.signature(comicBookCollection::ComicBookCollection.__init__)
    params = list(sig.parameters.keys())



def test_comicbookcollection::person_is_not_abstract():
    assert not inspect.isabstract(comicBookCollection::Person)


def test_comicbookcollection::person_constructor_exists():
    assert callable(comicBookCollection::Person.__init__)


def test_comicbookcollection::person_constructor_args():
    sig = inspect.signature(comicBookCollection::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_comicbookcollection::person_has_name():
    assert hasattr(comicBookCollection::Person, "name")
    descriptor = None
    for klass in comicBookCollection::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_comicbookcollection::book_is_not_abstract():
    assert not inspect.isabstract(comicBookCollection::Book)


def test_comicbookcollection::book_constructor_exists():
    assert callable(comicBookCollection::Book.__init__)


def test_comicbookcollection::book_constructor_args():
    sig = inspect.signature(comicBookCollection::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_comicbookcollection::book_has_title():
    assert hasattr(comicBookCollection::Book, "title")
    descriptor = None
    for klass in comicBookCollection::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_comicbookcollection::book_has_publicationDate():
    assert hasattr(comicBookCollection::Book, "publicationDate")
    descriptor = None
    for klass in comicBookCollection::Book.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_comicbookcollection::series_is_not_abstract():
    assert not inspect.isabstract(comicBookCollection::Series)


def test_comicbookcollection::series_constructor_exists():
    assert callable(comicBookCollection::Series.__init__)


def test_comicbookcollection::series_constructor_args():
    sig = inspect.signature(comicBookCollection::Series.__init__)
    params = list(sig.parameters.keys())
    assert "seriesTitle" in params, "Missing parameter 'seriesTitle'"

def test_comicbookcollection::series_has_seriesTitle():
    assert hasattr(comicBookCollection::Series, "seriesTitle")
    descriptor = None
    for klass in comicBookCollection::Series.__mro__:
        if "seriesTitle" in klass.__dict__:
            descriptor = klass.__dict__["seriesTitle"]
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
comicBookCollection::Publisher_strategy = st.builds(
    comicBookCollection::Publisher,
    publishingName=
        safe_text
)
comicBookCollection::ComicBookCollection_strategy = st.builds(
    comicBookCollection::ComicBookCollection,
)
comicBookCollection::Person_strategy = st.builds(
    comicBookCollection::Person,
    name=
        safe_text
)
comicBookCollection::Book_strategy = st.builds(
    comicBookCollection::Book,
    title=
        safe_text,
    publicationDate=
        safe_text
)
comicBookCollection::Series_strategy = st.builds(
    comicBookCollection::Series,
    seriesTitle=
        safe_text
)

@given(instance=comicBookCollection::Publisher_strategy)
@settings(max_examples=50)
def test_comicbookcollection::publisher_instantiation(instance):
    assert isinstance(instance, comicBookCollection::Publisher)

@given(instance=comicBookCollection::Publisher_strategy)
def test_comicbookcollection::publisher_publishingName_type(instance):
    assert isinstance(instance.publishingName, str)


@given(instance=comicBookCollection::Publisher_strategy)
def test_comicbookcollection::publisher_publishingName_setter(instance):
    original = instance.publishingName
    instance.publishingName = original
    assert instance.publishingName == original

@given(instance=comicBookCollection::ComicBookCollection_strategy)
@settings(max_examples=50)
def test_comicbookcollection::comicbookcollection_instantiation(instance):
    assert isinstance(instance, comicBookCollection::ComicBookCollection)

@given(instance=comicBookCollection::Person_strategy)
@settings(max_examples=50)
def test_comicbookcollection::person_instantiation(instance):
    assert isinstance(instance, comicBookCollection::Person)

@given(instance=comicBookCollection::Person_strategy)
def test_comicbookcollection::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=comicBookCollection::Person_strategy)
def test_comicbookcollection::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=comicBookCollection::Book_strategy)
@settings(max_examples=50)
def test_comicbookcollection::book_instantiation(instance):
    assert isinstance(instance, comicBookCollection::Book)

@given(instance=comicBookCollection::Book_strategy)
def test_comicbookcollection::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=comicBookCollection::Book_strategy)
def test_comicbookcollection::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=comicBookCollection::Book_strategy)
def test_comicbookcollection::book_publicationDate_type(instance):
    assert isinstance(instance.publicationDate, str)


@given(instance=comicBookCollection::Book_strategy)
def test_comicbookcollection::book_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=comicBookCollection::Series_strategy)
@settings(max_examples=50)
def test_comicbookcollection::series_instantiation(instance):
    assert isinstance(instance, comicBookCollection::Series)

@given(instance=comicBookCollection::Series_strategy)
def test_comicbookcollection::series_seriesTitle_type(instance):
    assert isinstance(instance.seriesTitle, str)


@given(instance=comicBookCollection::Series_strategy)
def test_comicbookcollection::series_seriesTitle_setter(instance):
    original = instance.seriesTitle
    instance.seriesTitle = original
    assert instance.seriesTitle == original
