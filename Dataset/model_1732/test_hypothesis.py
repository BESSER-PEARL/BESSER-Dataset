import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Item,
    library_Book,
    library_Item,
    library_LibraryShelf,
    MultimediaItem,
    library_CD,
    library_BlueRay,
    library_DVD,
    library_MultimediaItem,
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



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "numPages" in params, "Missing parameter 'numPages'"

def test_library_book_has_numPages():
    assert hasattr(library_Book, "numPages")
    descriptor = None
    for klass in library_Book.__mro__:
        if "numPages" in klass.__dict__:
            descriptor = klass.__dict__["numPages"]
            break
    assert isinstance(descriptor, property)



def test_library_item_is_not_abstract():
    assert not inspect.isabstract(library_Item)


def test_library_item_constructor_exists():
    assert callable(library_Item.__init__)


def test_library_item_constructor_args():
    sig = inspect.signature(library_Item.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pubDate" in params, "Missing parameter 'pubDate'"

def test_library_item_has_title():
    assert hasattr(library_Item, "title")
    descriptor = None
    for klass in library_Item.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library_item_has_pubDate():
    assert hasattr(library_Item, "pubDate")
    descriptor = None
    for klass in library_Item.__mro__:
        if "pubDate" in klass.__dict__:
            descriptor = klass.__dict__["pubDate"]
            break
    assert isinstance(descriptor, property)



def test_library_libraryshelf_is_not_abstract():
    assert not inspect.isabstract(library_LibraryShelf)


def test_library_libraryshelf_constructor_exists():
    assert callable(library_LibraryShelf.__init__)


def test_library_libraryshelf_constructor_args():
    sig = inspect.signature(library_LibraryShelf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_libraryshelf_has_name():
    assert hasattr(library_LibraryShelf, "name")
    descriptor = None
    for klass in library_LibraryShelf.__mro__:
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



def test_library_cd_is_not_abstract():
    assert not inspect.isabstract(library_CD)


def test_library_cd_constructor_exists():
    assert callable(library_CD.__init__)


def test_library_cd_constructor_args():
    sig = inspect.signature(library_CD.__init__)
    params = list(sig.parameters.keys())



def test_library_blueray_is_not_abstract():
    assert not inspect.isabstract(library_BlueRay)


def test_library_blueray_constructor_exists():
    assert callable(library_BlueRay.__init__)


def test_library_blueray_constructor_args():
    sig = inspect.signature(library_BlueRay.__init__)
    params = list(sig.parameters.keys())



def test_library_dvd_is_not_abstract():
    assert not inspect.isabstract(library_DVD)


def test_library_dvd_constructor_exists():
    assert callable(library_DVD.__init__)


def test_library_dvd_constructor_args():
    sig = inspect.signature(library_DVD.__init__)
    params = list(sig.parameters.keys())



def test_library_multimediaitem_is_not_abstract():
    assert not inspect.isabstract(library_MultimediaItem)


def test_library_multimediaitem_constructor_exists():
    assert callable(library_MultimediaItem.__init__)


def test_library_multimediaitem_constructor_args():
    sig = inspect.signature(library_MultimediaItem.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_library_multimediaitem_has_length():
    assert hasattr(library_MultimediaItem, "length")
    descriptor = None
    for klass in library_MultimediaItem.__mro__:
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
library_Book_strategy = st.builds(
    library_Book,
    numPages=
        st.integers()
)
library_Item_strategy = st.builds(
    library_Item,
    title=
        safe_text,
    pubDate=
        st.dates()
)
library_LibraryShelf_strategy = st.builds(
    library_LibraryShelf,
    name=
        safe_text
)
MultimediaItem_strategy = st.builds(
    MultimediaItem,
)
library_CD_strategy = st.builds(
    library_CD,
)
library_BlueRay_strategy = st.builds(
    library_BlueRay,
)
library_DVD_strategy = st.builds(
    library_DVD,
)
library_MultimediaItem_strategy = st.builds(
    library_MultimediaItem,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_numPages_setter(instance):
    original = instance.numPages
    instance.numPages = original
    assert instance.numPages == original

@given(instance=library_Item_strategy)
@settings(max_examples=50)
def test_library_item_instantiation(instance):
    assert isinstance(instance, library_Item)



@given(instance=library_Item_strategy)
def test_library_item_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_Item_strategy)
def test_library_item_pubDate_setter(instance):
    original = instance.pubDate
    instance.pubDate = original
    assert instance.pubDate == original

@given(instance=library_LibraryShelf_strategy)
@settings(max_examples=50)
def test_library_libraryshelf_instantiation(instance):
    assert isinstance(instance, library_LibraryShelf)



@given(instance=library_LibraryShelf_strategy)
def test_library_libraryshelf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MultimediaItem_strategy)
@settings(max_examples=50)
def test_multimediaitem_instantiation(instance):
    assert isinstance(instance, MultimediaItem)

@given(instance=library_CD_strategy)
@settings(max_examples=50)
def test_library_cd_instantiation(instance):
    assert isinstance(instance, library_CD)

@given(instance=library_BlueRay_strategy)
@settings(max_examples=50)
def test_library_blueray_instantiation(instance):
    assert isinstance(instance, library_BlueRay)

@given(instance=library_DVD_strategy)
@settings(max_examples=50)
def test_library_dvd_instantiation(instance):
    assert isinstance(instance, library_DVD)

@given(instance=library_MultimediaItem_strategy)
@settings(max_examples=50)
def test_library_multimediaitem_instantiation(instance):
    assert isinstance(instance, library_MultimediaItem)



@given(instance=library_MultimediaItem_strategy)
def test_library_multimediaitem_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original
