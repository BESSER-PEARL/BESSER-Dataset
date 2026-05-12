import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HtmlProfile,
    wikigen::Article,
    wikigen::Document,
    wikigen::HtmlProfile,
    wikigen::GenHtmlDocument,
    wikigen::GenLatexDocument,
    wikigen::Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_htmlprofile_is_not_abstract():
    assert not inspect.isabstract(HtmlProfile)


def test_htmlprofile_constructor_exists():
    assert callable(HtmlProfile.__init__)


def test_htmlprofile_constructor_args():
    sig = inspect.signature(HtmlProfile.__init__)
    params = list(sig.parameters.keys())



def test_wikigen::article_is_not_abstract():
    assert not inspect.isabstract(wikigen::Article)


def test_wikigen::article_constructor_exists():
    assert callable(wikigen::Article.__init__)


def test_wikigen::article_constructor_args():
    sig = inspect.signature(wikigen::Article.__init__)
    params = list(sig.parameters.keys())
    assert "generateTOC" in params, "Missing parameter 'generateTOC'"
    assert "nbColumns" in params, "Missing parameter 'nbColumns'"

def test_wikigen::article_has_generateTOC():
    assert hasattr(wikigen::Article, "generateTOC")
    descriptor = None
    for klass in wikigen::Article.__mro__:
        if "generateTOC" in klass.__dict__:
            descriptor = klass.__dict__["generateTOC"]
            break
    assert isinstance(descriptor, property)

def test_wikigen::article_has_nbColumns():
    assert hasattr(wikigen::Article, "nbColumns")
    descriptor = None
    for klass in wikigen::Article.__mro__:
        if "nbColumns" in klass.__dict__:
            descriptor = klass.__dict__["nbColumns"]
            break
    assert isinstance(descriptor, property)



def test_wikigen::document_is_not_abstract():
    assert not inspect.isabstract(wikigen::Document)


def test_wikigen::document_constructor_exists():
    assert callable(wikigen::Document.__init__)


def test_wikigen::document_constructor_args():
    sig = inspect.signature(wikigen::Document.__init__)
    params = list(sig.parameters.keys())



def test_wikigen::htmlprofile_is_not_abstract():
    assert not inspect.isabstract(wikigen::HtmlProfile)


def test_wikigen::htmlprofile_constructor_exists():
    assert callable(wikigen::HtmlProfile.__init__)


def test_wikigen::htmlprofile_constructor_args():
    sig = inspect.signature(wikigen::HtmlProfile.__init__)
    params = list(sig.parameters.keys())



def test_wikigen::genhtmldocument_is_not_abstract():
    assert not inspect.isabstract(wikigen::GenHtmlDocument)


def test_wikigen::genhtmldocument_constructor_exists():
    assert callable(wikigen::GenHtmlDocument.__init__)


def test_wikigen::genhtmldocument_constructor_args():
    sig = inspect.signature(wikigen::GenHtmlDocument.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_wikigen::genhtmldocument_has_filename():
    assert hasattr(wikigen::GenHtmlDocument, "filename")
    descriptor = None
    for klass in wikigen::GenHtmlDocument.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_wikigen::genlatexdocument_is_not_abstract():
    assert not inspect.isabstract(wikigen::GenLatexDocument)


def test_wikigen::genlatexdocument_constructor_exists():
    assert callable(wikigen::GenLatexDocument.__init__)


def test_wikigen::genlatexdocument_constructor_args():
    sig = inspect.signature(wikigen::GenLatexDocument.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"
    assert "title" in params, "Missing parameter 'title'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_wikigen::genlatexdocument_has_authors():
    assert hasattr(wikigen::GenLatexDocument, "authors")
    descriptor = None
    for klass in wikigen::GenLatexDocument.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_wikigen::genlatexdocument_has_title():
    assert hasattr(wikigen::GenLatexDocument, "title")
    descriptor = None
    for klass in wikigen::GenLatexDocument.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_wikigen::genlatexdocument_has_filename():
    assert hasattr(wikigen::GenLatexDocument, "filename")
    descriptor = None
    for klass in wikigen::GenLatexDocument.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_wikigen::container_is_not_abstract():
    assert not inspect.isabstract(wikigen::Container)


def test_wikigen::container_constructor_exists():
    assert callable(wikigen::Container.__init__)


def test_wikigen::container_constructor_args():
    sig = inspect.signature(wikigen::Container.__init__)
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
HtmlProfile_strategy = st.builds(
    HtmlProfile,
)
wikigen::Article_strategy = st.builds(
    wikigen::Article,
    generateTOC=
        st.booleans(),
    nbColumns=
        st.integers()
)
wikigen::Document_strategy = st.builds(
    wikigen::Document,
)
wikigen::HtmlProfile_strategy = st.builds(
    wikigen::HtmlProfile,
)
wikigen::GenHtmlDocument_strategy = st.builds(
    wikigen::GenHtmlDocument,
    filename=
        safe_text
)
wikigen::GenLatexDocument_strategy = st.builds(
    wikigen::GenLatexDocument,
    authors=
        safe_text,
    title=
        safe_text,
    filename=
        safe_text
)
wikigen::Container_strategy = st.builds(
    wikigen::Container,
)

@given(instance=HtmlProfile_strategy)
@settings(max_examples=50)
def test_htmlprofile_instantiation(instance):
    assert isinstance(instance, HtmlProfile)

@given(instance=wikigen::Article_strategy)
@settings(max_examples=50)
def test_wikigen::article_instantiation(instance):
    assert isinstance(instance, wikigen::Article)

@given(instance=wikigen::Article_strategy)
def test_wikigen::article_generateTOC_type(instance):
    assert isinstance(instance.generateTOC, bool)


@given(instance=wikigen::Article_strategy)
def test_wikigen::article_generateTOC_setter(instance):
    original = instance.generateTOC
    instance.generateTOC = original
    assert instance.generateTOC == original

@given(instance=wikigen::Article_strategy)
def test_wikigen::article_nbColumns_type(instance):
    assert isinstance(instance.nbColumns, int)


@given(instance=wikigen::Article_strategy)
def test_wikigen::article_nbColumns_setter(instance):
    original = instance.nbColumns
    instance.nbColumns = original
    assert instance.nbColumns == original

@given(instance=wikigen::Document_strategy)
@settings(max_examples=50)
def test_wikigen::document_instantiation(instance):
    assert isinstance(instance, wikigen::Document)

@given(instance=wikigen::HtmlProfile_strategy)
@settings(max_examples=50)
def test_wikigen::htmlprofile_instantiation(instance):
    assert isinstance(instance, wikigen::HtmlProfile)

@given(instance=wikigen::GenHtmlDocument_strategy)
@settings(max_examples=50)
def test_wikigen::genhtmldocument_instantiation(instance):
    assert isinstance(instance, wikigen::GenHtmlDocument)

@given(instance=wikigen::GenHtmlDocument_strategy)
def test_wikigen::genhtmldocument_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=wikigen::GenHtmlDocument_strategy)
def test_wikigen::genhtmldocument_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=wikigen::GenLatexDocument_strategy)
@settings(max_examples=50)
def test_wikigen::genlatexdocument_instantiation(instance):
    assert isinstance(instance, wikigen::GenLatexDocument)

@given(instance=wikigen::GenLatexDocument_strategy)
def test_wikigen::genlatexdocument_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=wikigen::GenLatexDocument_strategy)
def test_wikigen::genlatexdocument_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=wikigen::GenLatexDocument_strategy)
def test_wikigen::genlatexdocument_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=wikigen::GenLatexDocument_strategy)
def test_wikigen::genlatexdocument_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=wikigen::GenLatexDocument_strategy)
def test_wikigen::genlatexdocument_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=wikigen::GenLatexDocument_strategy)
def test_wikigen::genlatexdocument_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=wikigen::Container_strategy)
@settings(max_examples=50)
def test_wikigen::container_instantiation(instance):
    assert isinstance(instance, wikigen::Container)
