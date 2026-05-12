import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Section,
    docbook_Sect2,
    docbook_Para,
    docbook_Sect1,
    TitledElement,
    docbook_Section,
    docbook_TitledElement,
    docbook_Book,
    docbook_DocBook,
    docbook_Article,
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
    assert not inspect.isabstract(docbook_Sect2)


def test_docbook_sect2_constructor_exists():
    assert callable(docbook_Sect2.__init__)


def test_docbook_sect2_constructor_args():
    sig = inspect.signature(docbook_Sect2.__init__)
    params = list(sig.parameters.keys())



def test_docbook_para_is_not_abstract():
    assert not inspect.isabstract(docbook_Para)


def test_docbook_para_constructor_exists():
    assert callable(docbook_Para.__init__)


def test_docbook_para_constructor_args():
    sig = inspect.signature(docbook_Para.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_docbook_para_has_content():
    assert hasattr(docbook_Para, "content")
    descriptor = None
    for klass in docbook_Para.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_docbook_sect1_is_not_abstract():
    assert not inspect.isabstract(docbook_Sect1)


def test_docbook_sect1_constructor_exists():
    assert callable(docbook_Sect1.__init__)


def test_docbook_sect1_constructor_args():
    sig = inspect.signature(docbook_Sect1.__init__)
    params = list(sig.parameters.keys())



def test_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook_section_is_not_abstract():
    assert not inspect.isabstract(docbook_Section)


def test_docbook_section_constructor_exists():
    assert callable(docbook_Section.__init__)


def test_docbook_section_constructor_args():
    sig = inspect.signature(docbook_Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook_titledelement_is_not_abstract():
    assert not inspect.isabstract(docbook_TitledElement)


def test_docbook_titledelement_constructor_exists():
    assert callable(docbook_TitledElement.__init__)


def test_docbook_titledelement_constructor_args():
    sig = inspect.signature(docbook_TitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_docbook_titledelement_has_title():
    assert hasattr(docbook_TitledElement, "title")
    descriptor = None
    for klass in docbook_TitledElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_docbook_book_is_not_abstract():
    assert not inspect.isabstract(docbook_Book)


def test_docbook_book_constructor_exists():
    assert callable(docbook_Book.__init__)


def test_docbook_book_constructor_args():
    sig = inspect.signature(docbook_Book.__init__)
    params = list(sig.parameters.keys())



def test_docbook_docbook_is_not_abstract():
    assert not inspect.isabstract(docbook_DocBook)


def test_docbook_docbook_constructor_exists():
    assert callable(docbook_DocBook.__init__)


def test_docbook_docbook_constructor_args():
    sig = inspect.signature(docbook_DocBook.__init__)
    params = list(sig.parameters.keys())



def test_docbook_article_is_not_abstract():
    assert not inspect.isabstract(docbook_Article)


def test_docbook_article_constructor_exists():
    assert callable(docbook_Article.__init__)


def test_docbook_article_constructor_args():
    sig = inspect.signature(docbook_Article.__init__)
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
docbook_Sect2_strategy = st.builds(
    docbook_Sect2,
)
docbook_Para_strategy = st.builds(
    docbook_Para,
    content=
        safe_text
)
docbook_Sect1_strategy = st.builds(
    docbook_Sect1,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
docbook_Section_strategy = st.builds(
    docbook_Section,
)
docbook_TitledElement_strategy = st.builds(
    docbook_TitledElement,
    title=
        safe_text
)
docbook_Book_strategy = st.builds(
    docbook_Book,
)
docbook_DocBook_strategy = st.builds(
    docbook_DocBook,
)
docbook_Article_strategy = st.builds(
    docbook_Article,
)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=docbook_Sect2_strategy)
@settings(max_examples=50)
def test_docbook_sect2_instantiation(instance):
    assert isinstance(instance, docbook_Sect2)

@given(instance=docbook_Para_strategy)
@settings(max_examples=50)
def test_docbook_para_instantiation(instance):
    assert isinstance(instance, docbook_Para)



@given(instance=docbook_Para_strategy)
def test_docbook_para_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=docbook_Sect1_strategy)
@settings(max_examples=50)
def test_docbook_sect1_instantiation(instance):
    assert isinstance(instance, docbook_Sect1)

@given(instance=TitledElement_strategy)
@settings(max_examples=50)
def test_titledelement_instantiation(instance):
    assert isinstance(instance, TitledElement)

@given(instance=docbook_Section_strategy)
@settings(max_examples=50)
def test_docbook_section_instantiation(instance):
    assert isinstance(instance, docbook_Section)

@given(instance=docbook_TitledElement_strategy)
@settings(max_examples=50)
def test_docbook_titledelement_instantiation(instance):
    assert isinstance(instance, docbook_TitledElement)



@given(instance=docbook_TitledElement_strategy)
def test_docbook_titledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=docbook_Book_strategy)
@settings(max_examples=50)
def test_docbook_book_instantiation(instance):
    assert isinstance(instance, docbook_Book)

@given(instance=docbook_DocBook_strategy)
@settings(max_examples=50)
def test_docbook_docbook_instantiation(instance):
    assert isinstance(instance, docbook_DocBook)

@given(instance=docbook_Article_strategy)
@settings(max_examples=50)
def test_docbook_article_instantiation(instance):
    assert isinstance(instance, docbook_Article)
