import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Section,
    DocBook_Sect2,
    DocBook_Para,
    DocBook_Sect1,
    TitledElement,
    DocBook_Section,
    DocBook_TitledElement,
    DocBook_Article,
    DocBook_Book,
    DocBook_DocBook,
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



def test_docbook_sect2_is_not_abstract():
    assert not inspect.isabstract(DocBook_Sect2)


def test_docbook_sect2_constructor_exists():
    assert callable(DocBook_Sect2.__init__)


def test_docbook_sect2_constructor_args():
    sig = inspect.signature(DocBook_Sect2.__init__)
    params = list(sig.parameters.keys())



def test_docbook_para_is_not_abstract():
    assert not inspect.isabstract(DocBook_Para)


def test_docbook_para_constructor_exists():
    assert callable(DocBook_Para.__init__)


def test_docbook_para_constructor_args():
    sig = inspect.signature(DocBook_Para.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_docbook_para_has_content():
    assert hasattr(DocBook_Para, "content")
    descriptor = None
    for klass in DocBook_Para.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_docbook_sect1_is_not_abstract():
    assert not inspect.isabstract(DocBook_Sect1)


def test_docbook_sect1_constructor_exists():
    assert callable(DocBook_Sect1.__init__)


def test_docbook_sect1_constructor_args():
    sig = inspect.signature(DocBook_Sect1.__init__)
    params = list(sig.parameters.keys())



def test_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook_section_is_not_abstract():
    assert not inspect.isabstract(DocBook_Section)


def test_docbook_section_constructor_exists():
    assert callable(DocBook_Section.__init__)


def test_docbook_section_constructor_args():
    sig = inspect.signature(DocBook_Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook_titledelement_is_not_abstract():
    assert not inspect.isabstract(DocBook_TitledElement)


def test_docbook_titledelement_constructor_exists():
    assert callable(DocBook_TitledElement.__init__)


def test_docbook_titledelement_constructor_args():
    sig = inspect.signature(DocBook_TitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_docbook_titledelement_has_title():
    assert hasattr(DocBook_TitledElement, "title")
    descriptor = None
    for klass in DocBook_TitledElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_docbook_article_is_not_abstract():
    assert not inspect.isabstract(DocBook_Article)


def test_docbook_article_constructor_exists():
    assert callable(DocBook_Article.__init__)


def test_docbook_article_constructor_args():
    sig = inspect.signature(DocBook_Article.__init__)
    params = list(sig.parameters.keys())



def test_docbook_book_is_not_abstract():
    assert not inspect.isabstract(DocBook_Book)


def test_docbook_book_constructor_exists():
    assert callable(DocBook_Book.__init__)


def test_docbook_book_constructor_args():
    sig = inspect.signature(DocBook_Book.__init__)
    params = list(sig.parameters.keys())



def test_docbook_docbook_is_not_abstract():
    assert not inspect.isabstract(DocBook_DocBook)


def test_docbook_docbook_constructor_exists():
    assert callable(DocBook_DocBook.__init__)


def test_docbook_docbook_constructor_args():
    sig = inspect.signature(DocBook_DocBook.__init__)
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
DocBook_Sect2_strategy = st.builds(
    DocBook_Sect2,
)
DocBook_Para_strategy = st.builds(
    DocBook_Para,
    content=
        safe_text
)
DocBook_Sect1_strategy = st.builds(
    DocBook_Sect1,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
DocBook_Section_strategy = st.builds(
    DocBook_Section,
)
DocBook_TitledElement_strategy = st.builds(
    DocBook_TitledElement,
    title=
        safe_text
)
DocBook_Article_strategy = st.builds(
    DocBook_Article,
)
DocBook_Book_strategy = st.builds(
    DocBook_Book,
)
DocBook_DocBook_strategy = st.builds(
    DocBook_DocBook,
)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=DocBook_Sect2_strategy)
@settings(max_examples=50)
def test_docbook_sect2_instantiation(instance):
    assert isinstance(instance, DocBook_Sect2)

@given(instance=DocBook_Para_strategy)
@settings(max_examples=50)
def test_docbook_para_instantiation(instance):
    assert isinstance(instance, DocBook_Para)



@given(instance=DocBook_Para_strategy)
def test_docbook_para_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=DocBook_Sect1_strategy)
@settings(max_examples=50)
def test_docbook_sect1_instantiation(instance):
    assert isinstance(instance, DocBook_Sect1)

@given(instance=TitledElement_strategy)
@settings(max_examples=50)
def test_titledelement_instantiation(instance):
    assert isinstance(instance, TitledElement)

@given(instance=DocBook_Section_strategy)
@settings(max_examples=50)
def test_docbook_section_instantiation(instance):
    assert isinstance(instance, DocBook_Section)

@given(instance=DocBook_TitledElement_strategy)
@settings(max_examples=50)
def test_docbook_titledelement_instantiation(instance):
    assert isinstance(instance, DocBook_TitledElement)



@given(instance=DocBook_TitledElement_strategy)
def test_docbook_titledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=DocBook_Article_strategy)
@settings(max_examples=50)
def test_docbook_article_instantiation(instance):
    assert isinstance(instance, DocBook_Article)

@given(instance=DocBook_Book_strategy)
@settings(max_examples=50)
def test_docbook_book_instantiation(instance):
    assert isinstance(instance, DocBook_Book)

@given(instance=DocBook_DocBook_strategy)
@settings(max_examples=50)
def test_docbook_docbook_instantiation(instance):
    assert isinstance(instance, DocBook_DocBook)
