import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HtmlProfile,
    wikigen_Article,
    wikigen_Document,
    wikigen_HtmlProfile,
    wikigen_GenHtmlDocument,
    wikigen_GenLatexDocument,
    wikigen_Container,
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



def test_wikigen_article_is_not_abstract():
    assert not inspect.isabstract(wikigen_Article)


def test_wikigen_article_constructor_exists():
    assert callable(wikigen_Article.__init__)


def test_wikigen_article_constructor_args():
    sig = inspect.signature(wikigen_Article.__init__)
    params = list(sig.parameters.keys())
    assert "nbColumns" in params, "Missing parameter 'nbColumns'"
    assert "generateTOC" in params, "Missing parameter 'generateTOC'"

def test_wikigen_article_has_nbColumns():
    assert hasattr(wikigen_Article, "nbColumns")
    descriptor = None
    for klass in wikigen_Article.__mro__:
        if "nbColumns" in klass.__dict__:
            descriptor = klass.__dict__["nbColumns"]
            break
    assert isinstance(descriptor, property)

def test_wikigen_article_has_generateTOC():
    assert hasattr(wikigen_Article, "generateTOC")
    descriptor = None
    for klass in wikigen_Article.__mro__:
        if "generateTOC" in klass.__dict__:
            descriptor = klass.__dict__["generateTOC"]
            break
    assert isinstance(descriptor, property)



def test_wikigen_document_is_not_abstract():
    assert not inspect.isabstract(wikigen_Document)


def test_wikigen_document_constructor_exists():
    assert callable(wikigen_Document.__init__)


def test_wikigen_document_constructor_args():
    sig = inspect.signature(wikigen_Document.__init__)
    params = list(sig.parameters.keys())



def test_wikigen_htmlprofile_is_not_abstract():
    assert not inspect.isabstract(wikigen_HtmlProfile)


def test_wikigen_htmlprofile_constructor_exists():
    assert callable(wikigen_HtmlProfile.__init__)


def test_wikigen_htmlprofile_constructor_args():
    sig = inspect.signature(wikigen_HtmlProfile.__init__)
    params = list(sig.parameters.keys())



def test_wikigen_genhtmldocument_is_not_abstract():
    assert not inspect.isabstract(wikigen_GenHtmlDocument)


def test_wikigen_genhtmldocument_constructor_exists():
    assert callable(wikigen_GenHtmlDocument.__init__)


def test_wikigen_genhtmldocument_constructor_args():
    sig = inspect.signature(wikigen_GenHtmlDocument.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_wikigen_genhtmldocument_has_filename():
    assert hasattr(wikigen_GenHtmlDocument, "filename")
    descriptor = None
    for klass in wikigen_GenHtmlDocument.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_wikigen_genlatexdocument_is_not_abstract():
    assert not inspect.isabstract(wikigen_GenLatexDocument)


def test_wikigen_genlatexdocument_constructor_exists():
    assert callable(wikigen_GenLatexDocument.__init__)


def test_wikigen_genlatexdocument_constructor_args():
    sig = inspect.signature(wikigen_GenLatexDocument.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "title" in params, "Missing parameter 'title'"

def test_wikigen_genlatexdocument_has_filename():
    assert hasattr(wikigen_GenLatexDocument, "filename")
    descriptor = None
    for klass in wikigen_GenLatexDocument.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_wikigen_genlatexdocument_has_authors():
    assert hasattr(wikigen_GenLatexDocument, "authors")
    descriptor = None
    for klass in wikigen_GenLatexDocument.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_wikigen_genlatexdocument_has_title():
    assert hasattr(wikigen_GenLatexDocument, "title")
    descriptor = None
    for klass in wikigen_GenLatexDocument.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_wikigen_container_is_not_abstract():
    assert not inspect.isabstract(wikigen_Container)


def test_wikigen_container_constructor_exists():
    assert callable(wikigen_Container.__init__)


def test_wikigen_container_constructor_args():
    sig = inspect.signature(wikigen_Container.__init__)
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
wikigen_Article_strategy = st.builds(
    wikigen_Article,
    nbColumns=
        st.integers(),
    generateTOC=
        st.booleans()
)
wikigen_Document_strategy = st.builds(
    wikigen_Document,
)
wikigen_HtmlProfile_strategy = st.builds(
    wikigen_HtmlProfile,
)
wikigen_GenHtmlDocument_strategy = st.builds(
    wikigen_GenHtmlDocument,
    filename=
        safe_text
)
wikigen_GenLatexDocument_strategy = st.builds(
    wikigen_GenLatexDocument,
    filename=
        safe_text,
    authors=
        safe_text,
    title=
        safe_text
)
wikigen_Container_strategy = st.builds(
    wikigen_Container,
)

@given(instance=HtmlProfile_strategy)
@settings(max_examples=50)
def test_htmlprofile_instantiation(instance):
    assert isinstance(instance, HtmlProfile)

@given(instance=wikigen_Article_strategy)
@settings(max_examples=50)
def test_wikigen_article_instantiation(instance):
    assert isinstance(instance, wikigen_Article)



@given(instance=wikigen_Article_strategy)
def test_wikigen_article_nbColumns_setter(instance):
    original = instance.nbColumns
    instance.nbColumns = original
    assert instance.nbColumns == original



@given(instance=wikigen_Article_strategy)
def test_wikigen_article_generateTOC_setter(instance):
    original = instance.generateTOC
    instance.generateTOC = original
    assert instance.generateTOC == original

@given(instance=wikigen_Document_strategy)
@settings(max_examples=50)
def test_wikigen_document_instantiation(instance):
    assert isinstance(instance, wikigen_Document)

@given(instance=wikigen_HtmlProfile_strategy)
@settings(max_examples=50)
def test_wikigen_htmlprofile_instantiation(instance):
    assert isinstance(instance, wikigen_HtmlProfile)

@given(instance=wikigen_GenHtmlDocument_strategy)
@settings(max_examples=50)
def test_wikigen_genhtmldocument_instantiation(instance):
    assert isinstance(instance, wikigen_GenHtmlDocument)



@given(instance=wikigen_GenHtmlDocument_strategy)
def test_wikigen_genhtmldocument_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=wikigen_GenLatexDocument_strategy)
@settings(max_examples=50)
def test_wikigen_genlatexdocument_instantiation(instance):
    assert isinstance(instance, wikigen_GenLatexDocument)



@given(instance=wikigen_GenLatexDocument_strategy)
def test_wikigen_genlatexdocument_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=wikigen_GenLatexDocument_strategy)
def test_wikigen_genlatexdocument_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=wikigen_GenLatexDocument_strategy)
def test_wikigen_genlatexdocument_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=wikigen_Container_strategy)
@settings(max_examples=50)
def test_wikigen_container_instantiation(instance):
    assert isinstance(instance, wikigen_Container)
