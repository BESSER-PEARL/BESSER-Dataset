import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DocBook::Book,
    DocBook::DocBook,
    Section,
    DocBook::Sect2,
    DocBook::Para,
    DocBook::Sect1,
    TitledElement,
    DocBook::Section,
    DocBook::TitledElement,
    DocBook::Article,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docbook::book_is_not_abstract():
    assert not inspect.isabstract(DocBook::Book)


def test_docbook::book_constructor_exists():
    assert callable(DocBook::Book.__init__)


def test_docbook::book_constructor_args():
    sig = inspect.signature(DocBook::Book.__init__)
    params = list(sig.parameters.keys())



def test_docbook::docbook_is_not_abstract():
    assert not inspect.isabstract(DocBook::DocBook)


def test_docbook::docbook_constructor_exists():
    assert callable(DocBook::DocBook.__init__)


def test_docbook::docbook_constructor_args():
    sig = inspect.signature(DocBook::DocBook.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook::sect2_is_not_abstract():
    assert not inspect.isabstract(DocBook::Sect2)


def test_docbook::sect2_constructor_exists():
    assert callable(DocBook::Sect2.__init__)


def test_docbook::sect2_constructor_args():
    sig = inspect.signature(DocBook::Sect2.__init__)
    params = list(sig.parameters.keys())



def test_docbook::para_is_not_abstract():
    assert not inspect.isabstract(DocBook::Para)


def test_docbook::para_constructor_exists():
    assert callable(DocBook::Para.__init__)


def test_docbook::para_constructor_args():
    sig = inspect.signature(DocBook::Para.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_docbook::para_has_content():
    assert hasattr(DocBook::Para, "content")
    descriptor = None
    for klass in DocBook::Para.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_docbook::sect1_is_not_abstract():
    assert not inspect.isabstract(DocBook::Sect1)


def test_docbook::sect1_constructor_exists():
    assert callable(DocBook::Sect1.__init__)


def test_docbook::sect1_constructor_args():
    sig = inspect.signature(DocBook::Sect1.__init__)
    params = list(sig.parameters.keys())



def test_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook::section_is_not_abstract():
    assert not inspect.isabstract(DocBook::Section)


def test_docbook::section_constructor_exists():
    assert callable(DocBook::Section.__init__)


def test_docbook::section_constructor_args():
    sig = inspect.signature(DocBook::Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook::titledelement_is_not_abstract():
    assert not inspect.isabstract(DocBook::TitledElement)


def test_docbook::titledelement_constructor_exists():
    assert callable(DocBook::TitledElement.__init__)


def test_docbook::titledelement_constructor_args():
    sig = inspect.signature(DocBook::TitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_docbook::titledelement_has_title():
    assert hasattr(DocBook::TitledElement, "title")
    descriptor = None
    for klass in DocBook::TitledElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_docbook::article_is_not_abstract():
    assert not inspect.isabstract(DocBook::Article)


def test_docbook::article_constructor_exists():
    assert callable(DocBook::Article.__init__)


def test_docbook::article_constructor_args():
    sig = inspect.signature(DocBook::Article.__init__)
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
DocBook::Book_strategy = st.builds(
    DocBook::Book,
)
DocBook::DocBook_strategy = st.builds(
    DocBook::DocBook,
)
Section_strategy = st.builds(
    Section,
)
DocBook::Sect2_strategy = st.builds(
    DocBook::Sect2,
)
DocBook::Para_strategy = st.builds(
    DocBook::Para,
    content=
        safe_text
)
DocBook::Sect1_strategy = st.builds(
    DocBook::Sect1,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
DocBook::Section_strategy = st.builds(
    DocBook::Section,
)
DocBook::TitledElement_strategy = st.builds(
    DocBook::TitledElement,
    title=
        safe_text
)
DocBook::Article_strategy = st.builds(
    DocBook::Article,
)

@given(instance=DocBook::Book_strategy)
@settings(max_examples=50)
def test_docbook::book_instantiation(instance):
    assert isinstance(instance, DocBook::Book)

@given(instance=DocBook::DocBook_strategy)
@settings(max_examples=50)
def test_docbook::docbook_instantiation(instance):
    assert isinstance(instance, DocBook::DocBook)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=DocBook::Sect2_strategy)
@settings(max_examples=50)
def test_docbook::sect2_instantiation(instance):
    assert isinstance(instance, DocBook::Sect2)

@given(instance=DocBook::Para_strategy)
@settings(max_examples=50)
def test_docbook::para_instantiation(instance):
    assert isinstance(instance, DocBook::Para)

@given(instance=DocBook::Para_strategy)
def test_docbook::para_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=DocBook::Para_strategy)
def test_docbook::para_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=DocBook::Sect1_strategy)
@settings(max_examples=50)
def test_docbook::sect1_instantiation(instance):
    assert isinstance(instance, DocBook::Sect1)

@given(instance=TitledElement_strategy)
@settings(max_examples=50)
def test_titledelement_instantiation(instance):
    assert isinstance(instance, TitledElement)

@given(instance=DocBook::Section_strategy)
@settings(max_examples=50)
def test_docbook::section_instantiation(instance):
    assert isinstance(instance, DocBook::Section)

@given(instance=DocBook::TitledElement_strategy)
@settings(max_examples=50)
def test_docbook::titledelement_instantiation(instance):
    assert isinstance(instance, DocBook::TitledElement)

@given(instance=DocBook::TitledElement_strategy)
def test_docbook::titledelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=DocBook::TitledElement_strategy)
def test_docbook::titledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=DocBook::Article_strategy)
@settings(max_examples=50)
def test_docbook::article_instantiation(instance):
    assert isinstance(instance, DocBook::Article)
