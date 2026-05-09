import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Section,
    docbook::Sect2,
    docbook::Para,
    docbook::Sect1,
    TitledElement,
    docbook::Section,
    docbook::TitledElement,
    docbook::Book,
    docbook::DocBook,
    docbook::Article,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook::sect2_is_not_abstract():
    assert not inspect.isabstract(docbook::Sect2)


def test_docbook::sect2_constructor_exists():
    assert callable(docbook::Sect2.__init__)


def test_docbook::sect2_constructor_args():
    sig = inspect.signature(docbook::Sect2.__init__)
    params = list(sig.parameters.keys())



def test_docbook::para_is_not_abstract():
    assert not inspect.isabstract(docbook::Para)


def test_docbook::para_constructor_exists():
    assert callable(docbook::Para.__init__)


def test_docbook::para_constructor_args():
    sig = inspect.signature(docbook::Para.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_docbook::para_has_content():
    assert hasattr(docbook::Para, "content")
    descriptor = None
    for klass in docbook::Para.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_docbook::sect1_is_not_abstract():
    assert not inspect.isabstract(docbook::Sect1)


def test_docbook::sect1_constructor_exists():
    assert callable(docbook::Sect1.__init__)


def test_docbook::sect1_constructor_args():
    sig = inspect.signature(docbook::Sect1.__init__)
    params = list(sig.parameters.keys())



def test_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook::section_is_not_abstract():
    assert not inspect.isabstract(docbook::Section)


def test_docbook::section_constructor_exists():
    assert callable(docbook::Section.__init__)


def test_docbook::section_constructor_args():
    sig = inspect.signature(docbook::Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook::titledelement_is_not_abstract():
    assert not inspect.isabstract(docbook::TitledElement)


def test_docbook::titledelement_constructor_exists():
    assert callable(docbook::TitledElement.__init__)


def test_docbook::titledelement_constructor_args():
    sig = inspect.signature(docbook::TitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_docbook::titledelement_has_title():
    assert hasattr(docbook::TitledElement, "title")
    descriptor = None
    for klass in docbook::TitledElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_docbook::book_is_not_abstract():
    assert not inspect.isabstract(docbook::Book)


def test_docbook::book_constructor_exists():
    assert callable(docbook::Book.__init__)


def test_docbook::book_constructor_args():
    sig = inspect.signature(docbook::Book.__init__)
    params = list(sig.parameters.keys())



def test_docbook::docbook_is_not_abstract():
    assert not inspect.isabstract(docbook::DocBook)


def test_docbook::docbook_constructor_exists():
    assert callable(docbook::DocBook.__init__)


def test_docbook::docbook_constructor_args():
    sig = inspect.signature(docbook::DocBook.__init__)
    params = list(sig.parameters.keys())



def test_docbook::article_is_not_abstract():
    assert not inspect.isabstract(docbook::Article)


def test_docbook::article_constructor_exists():
    assert callable(docbook::Article.__init__)


def test_docbook::article_constructor_args():
    sig = inspect.signature(docbook::Article.__init__)
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
Section_strategy = st.builds(
    Section,
)
docbook::Sect2_strategy = st.builds(
    docbook::Sect2,
)
docbook::Para_strategy = st.builds(
    docbook::Para,
    content=
        safe_text
)
docbook::Sect1_strategy = st.builds(
    docbook::Sect1,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
docbook::Section_strategy = st.builds(
    docbook::Section,
)
docbook::TitledElement_strategy = st.builds(
    docbook::TitledElement,
    title=
        safe_text
)
docbook::Book_strategy = st.builds(
    docbook::Book,
)
docbook::DocBook_strategy = st.builds(
    docbook::DocBook,
)
docbook::Article_strategy = st.builds(
    docbook::Article,
)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=docbook::Sect2_strategy)
@settings(max_examples=50)
def test_docbook::sect2_instantiation(instance):
    assert isinstance(instance, docbook::Sect2)

@given(instance=docbook::Para_strategy)
@settings(max_examples=50)
def test_docbook::para_instantiation(instance):
    assert isinstance(instance, docbook::Para)

@given(instance=docbook::Para_strategy)
def test_docbook::para_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=docbook::Para_strategy)
def test_docbook::para_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=docbook::Sect1_strategy)
@settings(max_examples=50)
def test_docbook::sect1_instantiation(instance):
    assert isinstance(instance, docbook::Sect1)

@given(instance=TitledElement_strategy)
@settings(max_examples=50)
def test_titledelement_instantiation(instance):
    assert isinstance(instance, TitledElement)

@given(instance=docbook::Section_strategy)
@settings(max_examples=50)
def test_docbook::section_instantiation(instance):
    assert isinstance(instance, docbook::Section)

@given(instance=docbook::TitledElement_strategy)
@settings(max_examples=50)
def test_docbook::titledelement_instantiation(instance):
    assert isinstance(instance, docbook::TitledElement)

@given(instance=docbook::TitledElement_strategy)
def test_docbook::titledelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=docbook::TitledElement_strategy)
def test_docbook::titledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=docbook::Book_strategy)
@settings(max_examples=50)
def test_docbook::book_instantiation(instance):
    assert isinstance(instance, docbook::Book)

@given(instance=docbook::DocBook_strategy)
@settings(max_examples=50)
def test_docbook::docbook_instantiation(instance):
    assert isinstance(instance, docbook::DocBook)

@given(instance=docbook::Article_strategy)
@settings(max_examples=50)
def test_docbook::article_instantiation(instance):
    assert isinstance(instance, docbook::Article)
