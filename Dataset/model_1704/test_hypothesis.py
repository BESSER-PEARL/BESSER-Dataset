import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Metadata,
    library::Bookmark,
    Bookmark,
    library::TextAnnotation,
    library::Book,
    library::Library,
    AnnotationColor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::metadata_is_not_abstract():
    assert not inspect.isabstract(library::Metadata)


def test_library::metadata_constructor_exists():
    assert callable(library::Metadata.__init__)


def test_library::metadata_constructor_args():
    sig = inspect.signature(library::Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_library::metadata_has_value():
    assert hasattr(library::Metadata, "value")
    descriptor = None
    for klass in library::Metadata.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_library::metadata_has_key():
    assert hasattr(library::Metadata, "key")
    descriptor = None
    for klass in library::Metadata.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_library::bookmark_is_not_abstract():
    assert not inspect.isabstract(library::Bookmark)


def test_library::bookmark_constructor_exists():
    assert callable(library::Bookmark.__init__)


def test_library::bookmark_constructor_args():
    sig = inspect.signature(library::Bookmark.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "href" in params, "Missing parameter 'href'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "text" in params, "Missing parameter 'text'"
    assert "page" in params, "Missing parameter 'page'"
    assert "id" in params, "Missing parameter 'id'"

def test_library::bookmark_has_location():
    assert hasattr(library::Bookmark, "location")
    descriptor = None
    for klass in library::Bookmark.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_library::bookmark_has_href():
    assert hasattr(library::Bookmark, "href")
    descriptor = None
    for klass in library::Bookmark.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_library::bookmark_has_timestamp():
    assert hasattr(library::Bookmark, "timestamp")
    descriptor = None
    for klass in library::Bookmark.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_library::bookmark_has_text():
    assert hasattr(library::Bookmark, "text")
    descriptor = None
    for klass in library::Bookmark.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_library::bookmark_has_page():
    assert hasattr(library::Bookmark, "page")
    descriptor = None
    for klass in library::Bookmark.__mro__:
        if "page" in klass.__dict__:
            descriptor = klass.__dict__["page"]
            break
    assert isinstance(descriptor, property)

def test_library::bookmark_has_id():
    assert hasattr(library::Bookmark, "id")
    descriptor = None
    for klass in library::Bookmark.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bookmark_is_not_abstract():
    assert not inspect.isabstract(Bookmark)


def test_bookmark_constructor_exists():
    assert callable(Bookmark.__init__)


def test_bookmark_constructor_args():
    sig = inspect.signature(Bookmark.__init__)
    params = list(sig.parameters.keys())



def test_library::textannotation_is_not_abstract():
    assert not inspect.isabstract(library::TextAnnotation)


def test_library::textannotation_constructor_exists():
    assert callable(library::TextAnnotation.__init__)


def test_library::textannotation_constructor_args():
    sig = inspect.signature(library::TextAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_library::textannotation_has_color():
    assert hasattr(library::TextAnnotation, "color")
    descriptor = None
    for klass in library::TextAnnotation.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_library::textannotation_has_comment():
    assert hasattr(library::TextAnnotation, "comment")
    descriptor = None
    for klass in library::TextAnnotation.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "collection" in params, "Missing parameter 'collection'"
    assert "title" in params, "Missing parameter 'title'"
    assert "bookURN" in params, "Missing parameter 'bookURN'"
    assert "bookURL" in params, "Missing parameter 'bookURL'"
    assert "lastOpened" in params, "Missing parameter 'lastOpened'"
    assert "lastHref" in params, "Missing parameter 'lastHref'"
    assert "author" in params, "Missing parameter 'author'"
    assert "lastLocation" in params, "Missing parameter 'lastLocation'"

def test_library::book_has_collection():
    assert hasattr(library::Book, "collection")
    descriptor = None
    for klass in library::Book.__mro__:
        if "collection" in klass.__dict__:
            descriptor = klass.__dict__["collection"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_title():
    assert hasattr(library::Book, "title")
    descriptor = None
    for klass in library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_bookURN():
    assert hasattr(library::Book, "bookURN")
    descriptor = None
    for klass in library::Book.__mro__:
        if "bookURN" in klass.__dict__:
            descriptor = klass.__dict__["bookURN"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_bookURL():
    assert hasattr(library::Book, "bookURL")
    descriptor = None
    for klass in library::Book.__mro__:
        if "bookURL" in klass.__dict__:
            descriptor = klass.__dict__["bookURL"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_lastOpened():
    assert hasattr(library::Book, "lastOpened")
    descriptor = None
    for klass in library::Book.__mro__:
        if "lastOpened" in klass.__dict__:
            descriptor = klass.__dict__["lastOpened"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_lastHref():
    assert hasattr(library::Book, "lastHref")
    descriptor = None
    for klass in library::Book.__mro__:
        if "lastHref" in klass.__dict__:
            descriptor = klass.__dict__["lastHref"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_author():
    assert hasattr(library::Book, "author")
    descriptor = None
    for klass in library::Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_lastLocation():
    assert hasattr(library::Book, "lastLocation")
    descriptor = None
    for klass in library::Book.__mro__:
        if "lastLocation" in klass.__dict__:
            descriptor = klass.__dict__["lastLocation"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_library::library_has_version():
    assert hasattr(library::Library, "version")
    descriptor = None
    for klass in library::Library.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_annotationcolor_exists():
    # Check that the Enumeration exists
    assert AnnotationColor is not None

def test_annotationcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnnotationColor]
    expected_literals = [
        "Red",
        "Green",
        "Purple",
        "Underline",
        "Blue",
        "Yellow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnnotationColor"


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
library::Metadata_strategy = st.builds(
    library::Metadata,
    value=
        safe_text,
    key=
        safe_text
)
library::Bookmark_strategy = st.builds(
    library::Bookmark,
    location=
        safe_text,
    href=
        safe_text,
    timestamp=
        st.dates(),
    text=
        safe_text,
    page=
        st.integers(),
    id=
        safe_text
)
Bookmark_strategy = st.builds(
    Bookmark,
)
library::TextAnnotation_strategy = st.builds(
    library::TextAnnotation,
    color=
        safe_text,
    comment=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    collection=
        safe_text,
    title=
        safe_text,
    bookURN=
        safe_text,
    bookURL=
        safe_text,
    lastOpened=
        safe_text,
    lastHref=
        safe_text,
    author=
        safe_text,
    lastLocation=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    version=
        safe_text
)

@given(instance=library::Metadata_strategy)
@settings(max_examples=50)
def test_library::metadata_instantiation(instance):
    assert isinstance(instance, library::Metadata)

@given(instance=library::Metadata_strategy)
def test_library::metadata_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=library::Metadata_strategy)
def test_library::metadata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=library::Metadata_strategy)
def test_library::metadata_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=library::Metadata_strategy)
def test_library::metadata_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=library::Bookmark_strategy)
@settings(max_examples=50)
def test_library::bookmark_instantiation(instance):
    assert isinstance(instance, library::Bookmark)

@given(instance=library::Bookmark_strategy)
def test_library::bookmark_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=library::Bookmark_strategy)
def test_library::bookmark_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=library::Bookmark_strategy)
def test_library::bookmark_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=library::Bookmark_strategy)
def test_library::bookmark_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=library::Bookmark_strategy)
def test_library::bookmark_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=library::Bookmark_strategy)
def test_library::bookmark_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=library::Bookmark_strategy)
def test_library::bookmark_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=library::Bookmark_strategy)
def test_library::bookmark_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=library::Bookmark_strategy)
def test_library::bookmark_page_type(instance):
    assert isinstance(instance.page, int)


@given(instance=library::Bookmark_strategy)
def test_library::bookmark_page_setter(instance):
    original = instance.page
    instance.page = original
    assert instance.page == original

@given(instance=library::Bookmark_strategy)
def test_library::bookmark_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=library::Bookmark_strategy)
def test_library::bookmark_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Bookmark_strategy)
@settings(max_examples=50)
def test_bookmark_instantiation(instance):
    assert isinstance(instance, Bookmark)

@given(instance=library::TextAnnotation_strategy)
@settings(max_examples=50)
def test_library::textannotation_instantiation(instance):
    assert isinstance(instance, library::TextAnnotation)

@given(instance=library::TextAnnotation_strategy)
def test_library::textannotation_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=library::TextAnnotation_strategy)
def test_library::textannotation_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=library::TextAnnotation_strategy)
def test_library::textannotation_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=library::TextAnnotation_strategy)
def test_library::textannotation_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_collection_type(instance):
    assert isinstance(instance.collection, str)


@given(instance=library::Book_strategy)
def test_library::book_collection_setter(instance):
    original = instance.collection
    instance.collection = original
    assert instance.collection == original

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Book_strategy)
def test_library::book_bookURN_type(instance):
    assert isinstance(instance.bookURN, str)


@given(instance=library::Book_strategy)
def test_library::book_bookURN_setter(instance):
    original = instance.bookURN
    instance.bookURN = original
    assert instance.bookURN == original

@given(instance=library::Book_strategy)
def test_library::book_bookURL_type(instance):
    assert isinstance(instance.bookURL, str)


@given(instance=library::Book_strategy)
def test_library::book_bookURL_setter(instance):
    original = instance.bookURL
    instance.bookURL = original
    assert instance.bookURL == original

@given(instance=library::Book_strategy)
def test_library::book_lastOpened_type(instance):
    assert isinstance(instance.lastOpened, str)


@given(instance=library::Book_strategy)
def test_library::book_lastOpened_setter(instance):
    original = instance.lastOpened
    instance.lastOpened = original
    assert instance.lastOpened == original

@given(instance=library::Book_strategy)
def test_library::book_lastHref_type(instance):
    assert isinstance(instance.lastHref, str)


@given(instance=library::Book_strategy)
def test_library::book_lastHref_setter(instance):
    original = instance.lastHref
    instance.lastHref = original
    assert instance.lastHref == original

@given(instance=library::Book_strategy)
def test_library::book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=library::Book_strategy)
def test_library::book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=library::Book_strategy)
def test_library::book_lastLocation_type(instance):
    assert isinstance(instance.lastLocation, str)


@given(instance=library::Book_strategy)
def test_library::book_lastLocation_setter(instance):
    original = instance.lastLocation
    instance.lastLocation = original
    assert instance.lastLocation == original

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=library::Library_strategy)
def test_library::library_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
