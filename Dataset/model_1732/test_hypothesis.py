import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Item,
    library::Book,
    library::Item,
    library::LibraryShelf,
    MultimediaItem,
    library::CD,
    library::BlueRay,
    library::DVD,
    library::MultimediaItem,
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



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "numPages" in params, "Missing parameter 'numPages'"

def test_library::book_has_numPages():
    assert hasattr(library::Book, "numPages")
    descriptor = None
    for klass in library::Book.__mro__:
        if "numPages" in klass.__dict__:
            descriptor = klass.__dict__["numPages"]
            break
    assert isinstance(descriptor, property)



def test_library::item_is_not_abstract():
    assert not inspect.isabstract(library::Item)


def test_library::item_constructor_exists():
    assert callable(library::Item.__init__)


def test_library::item_constructor_args():
    sig = inspect.signature(library::Item.__init__)
    params = list(sig.parameters.keys())
    assert "pubDate" in params, "Missing parameter 'pubDate'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::item_has_pubDate():
    assert hasattr(library::Item, "pubDate")
    descriptor = None
    for klass in library::Item.__mro__:
        if "pubDate" in klass.__dict__:
            descriptor = klass.__dict__["pubDate"]
            break
    assert isinstance(descriptor, property)

def test_library::item_has_title():
    assert hasattr(library::Item, "title")
    descriptor = None
    for klass in library::Item.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library::libraryshelf_is_not_abstract():
    assert not inspect.isabstract(library::LibraryShelf)


def test_library::libraryshelf_constructor_exists():
    assert callable(library::LibraryShelf.__init__)


def test_library::libraryshelf_constructor_args():
    sig = inspect.signature(library::LibraryShelf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::libraryshelf_has_name():
    assert hasattr(library::LibraryShelf, "name")
    descriptor = None
    for klass in library::LibraryShelf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_multimediaitem_is_not_abstract():
    assert not inspect.isabstract(MultimediaItem)


def test_multimediaitem_constructor_exists():
    assert callable(MultimediaItem.__init__)


def test_multimediaitem_constructor_args():
    sig = inspect.signature(MultimediaItem.__init__)
    params = list(sig.parameters.keys())



def test_library::cd_is_not_abstract():
    assert not inspect.isabstract(library::CD)


def test_library::cd_constructor_exists():
    assert callable(library::CD.__init__)


def test_library::cd_constructor_args():
    sig = inspect.signature(library::CD.__init__)
    params = list(sig.parameters.keys())



def test_library::blueray_is_not_abstract():
    assert not inspect.isabstract(library::BlueRay)


def test_library::blueray_constructor_exists():
    assert callable(library::BlueRay.__init__)


def test_library::blueray_constructor_args():
    sig = inspect.signature(library::BlueRay.__init__)
    params = list(sig.parameters.keys())



def test_library::dvd_is_not_abstract():
    assert not inspect.isabstract(library::DVD)


def test_library::dvd_constructor_exists():
    assert callable(library::DVD.__init__)


def test_library::dvd_constructor_args():
    sig = inspect.signature(library::DVD.__init__)
    params = list(sig.parameters.keys())



def test_library::multimediaitem_is_not_abstract():
    assert not inspect.isabstract(library::MultimediaItem)


def test_library::multimediaitem_constructor_exists():
    assert callable(library::MultimediaItem.__init__)


def test_library::multimediaitem_constructor_args():
    sig = inspect.signature(library::MultimediaItem.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_library::multimediaitem_has_length():
    assert hasattr(library::MultimediaItem, "length")
    descriptor = None
    for klass in library::MultimediaItem.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
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
Item_strategy = st.builds(
    Item,
)
library::Book_strategy = st.builds(
    library::Book,
    numPages=
        st.integers()
)
library::Item_strategy = st.builds(
    library::Item,
    pubDate=
        st.dates(),
    title=
        safe_text
)
library::LibraryShelf_strategy = st.builds(
    library::LibraryShelf,
    name=
        safe_text
)
MultimediaItem_strategy = st.builds(
    MultimediaItem,
)
library::CD_strategy = st.builds(
    library::CD,
)
library::BlueRay_strategy = st.builds(
    library::BlueRay,
)
library::DVD_strategy = st.builds(
    library::DVD,
)
library::MultimediaItem_strategy = st.builds(
    library::MultimediaItem,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_numPages_type(instance):
    assert isinstance(instance.numPages, int)


@given(instance=library::Book_strategy)
def test_library::book_numPages_setter(instance):
    original = instance.numPages
    instance.numPages = original
    assert instance.numPages == original

@given(instance=library::Item_strategy)
@settings(max_examples=50)
def test_library::item_instantiation(instance):
    assert isinstance(instance, library::Item)

@given(instance=library::Item_strategy)
def test_library::item_pubDate_type(instance):
    assert isinstance(instance.pubDate, date)


@given(instance=library::Item_strategy)
def test_library::item_pubDate_setter(instance):
    original = instance.pubDate
    instance.pubDate = original
    assert instance.pubDate == original

@given(instance=library::Item_strategy)
def test_library::item_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Item_strategy)
def test_library::item_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::LibraryShelf_strategy)
@settings(max_examples=50)
def test_library::libraryshelf_instantiation(instance):
    assert isinstance(instance, library::LibraryShelf)

@given(instance=library::LibraryShelf_strategy)
def test_library::libraryshelf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::LibraryShelf_strategy)
def test_library::libraryshelf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MultimediaItem_strategy)
@settings(max_examples=50)
def test_multimediaitem_instantiation(instance):
    assert isinstance(instance, MultimediaItem)

@given(instance=library::CD_strategy)
@settings(max_examples=50)
def test_library::cd_instantiation(instance):
    assert isinstance(instance, library::CD)

@given(instance=library::BlueRay_strategy)
@settings(max_examples=50)
def test_library::blueray_instantiation(instance):
    assert isinstance(instance, library::BlueRay)

@given(instance=library::DVD_strategy)
@settings(max_examples=50)
def test_library::dvd_instantiation(instance):
    assert isinstance(instance, library::DVD)

@given(instance=library::MultimediaItem_strategy)
@settings(max_examples=50)
def test_library::multimediaitem_instantiation(instance):
    assert isinstance(instance, library::MultimediaItem)

@given(instance=library::MultimediaItem_strategy)
def test_library::multimediaitem_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=library::MultimediaItem_strategy)
def test_library::multimediaitem_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original
