import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    docbook::Sect1Type,
    docbook::EStringToStringMapEntry,
    docbook::DocumentRoot,
    docbook::ChapterType,
    docbook::BookType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docbook::sect1type_is_not_abstract():
    assert not inspect.isabstract(docbook::Sect1Type)


def test_docbook::sect1type_constructor_exists():
    assert callable(docbook::Sect1Type.__init__)


def test_docbook::sect1type_constructor_args():
    sig = inspect.signature(docbook::Sect1Type.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "para" in params, "Missing parameter 'para'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::sect1type_has_title():
    assert hasattr(docbook::Sect1Type, "title")
    descriptor = None
    for klass in docbook::Sect1Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook::sect1type_has_para():
    assert hasattr(docbook::Sect1Type, "para")
    descriptor = None
    for klass in docbook::Sect1Type.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)

def test_docbook::sect1type_has_mixed():
    assert hasattr(docbook::Sect1Type, "mixed")
    descriptor = None
    for klass in docbook::Sect1Type.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(docbook::EStringToStringMapEntry)


def test_docbook::estringtostringmapentry_constructor_exists():
    assert callable(docbook::EStringToStringMapEntry.__init__)


def test_docbook::estringtostringmapentry_constructor_args():
    sig = inspect.signature(docbook::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_docbook::documentroot_is_not_abstract():
    assert not inspect.isabstract(docbook::DocumentRoot)


def test_docbook::documentroot_constructor_exists():
    assert callable(docbook::DocumentRoot.__init__)


def test_docbook::documentroot_constructor_args():
    sig = inspect.signature(docbook::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"
    assert "para" in params, "Missing parameter 'para'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "title" in params, "Missing parameter 'title'"

def test_docbook::documentroot_has_info():
    assert hasattr(docbook::DocumentRoot, "info")
    descriptor = None
    for klass in docbook::DocumentRoot.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_para():
    assert hasattr(docbook::DocumentRoot, "para")
    descriptor = None
    for klass in docbook::DocumentRoot.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_mixed():
    assert hasattr(docbook::DocumentRoot, "mixed")
    descriptor = None
    for klass in docbook::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_title():
    assert hasattr(docbook::DocumentRoot, "title")
    descriptor = None
    for klass in docbook::DocumentRoot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_docbook::chaptertype_is_not_abstract():
    assert not inspect.isabstract(docbook::ChapterType)


def test_docbook::chaptertype_constructor_exists():
    assert callable(docbook::ChapterType.__init__)


def test_docbook::chaptertype_constructor_args():
    sig = inspect.signature(docbook::ChapterType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "para" in params, "Missing parameter 'para'"

def test_docbook::chaptertype_has_title():
    assert hasattr(docbook::ChapterType, "title")
    descriptor = None
    for klass in docbook::ChapterType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook::chaptertype_has_mixed():
    assert hasattr(docbook::ChapterType, "mixed")
    descriptor = None
    for klass in docbook::ChapterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::chaptertype_has_para():
    assert hasattr(docbook::ChapterType, "para")
    descriptor = None
    for klass in docbook::ChapterType.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)



def test_docbook::booktype_is_not_abstract():
    assert not inspect.isabstract(docbook::BookType)


def test_docbook::booktype_constructor_exists():
    assert callable(docbook::BookType.__init__)


def test_docbook::booktype_constructor_args():
    sig = inspect.signature(docbook::BookType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "info" in params, "Missing parameter 'info'"

def test_docbook::booktype_has_title():
    assert hasattr(docbook::BookType, "title")
    descriptor = None
    for klass in docbook::BookType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook::booktype_has_info():
    assert hasattr(docbook::BookType, "info")
    descriptor = None
    for klass in docbook::BookType.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
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
docbook::Sect1Type_strategy = st.builds(
    docbook::Sect1Type,
    title=
        safe_text,
    para=
        safe_text,
    mixed=
        safe_text
)
docbook::EStringToStringMapEntry_strategy = st.builds(
    docbook::EStringToStringMapEntry,
)
docbook::DocumentRoot_strategy = st.builds(
    docbook::DocumentRoot,
    info=
        safe_text,
    para=
        safe_text,
    mixed=
        safe_text,
    title=
        safe_text
)
docbook::ChapterType_strategy = st.builds(
    docbook::ChapterType,
    title=
        safe_text,
    mixed=
        safe_text,
    para=
        safe_text
)
docbook::BookType_strategy = st.builds(
    docbook::BookType,
    title=
        safe_text,
    info=
        safe_text
)

@given(instance=docbook::Sect1Type_strategy)
@settings(max_examples=50)
def test_docbook::sect1type_instantiation(instance):
    assert isinstance(instance, docbook::Sect1Type)

@given(instance=docbook::Sect1Type_strategy)
def test_docbook::sect1type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=docbook::Sect1Type_strategy)
def test_docbook::sect1type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=docbook::Sect1Type_strategy)
def test_docbook::sect1type_para_type(instance):
    assert isinstance(instance.para, str)


@given(instance=docbook::Sect1Type_strategy)
def test_docbook::sect1type_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original

@given(instance=docbook::Sect1Type_strategy)
def test_docbook::sect1type_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=docbook::Sect1Type_strategy)
def test_docbook::sect1type_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=docbook::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_docbook::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, docbook::EStringToStringMapEntry)

@given(instance=docbook::DocumentRoot_strategy)
@settings(max_examples=50)
def test_docbook::documentroot_instantiation(instance):
    assert isinstance(instance, docbook::DocumentRoot)

@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_para_type(instance):
    assert isinstance(instance.para, str)


@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original

@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=docbook::DocumentRoot_strategy)
def test_docbook::documentroot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=docbook::ChapterType_strategy)
@settings(max_examples=50)
def test_docbook::chaptertype_instantiation(instance):
    assert isinstance(instance, docbook::ChapterType)

@given(instance=docbook::ChapterType_strategy)
def test_docbook::chaptertype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=docbook::ChapterType_strategy)
def test_docbook::chaptertype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=docbook::ChapterType_strategy)
def test_docbook::chaptertype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=docbook::ChapterType_strategy)
def test_docbook::chaptertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=docbook::ChapterType_strategy)
def test_docbook::chaptertype_para_type(instance):
    assert isinstance(instance.para, str)


@given(instance=docbook::ChapterType_strategy)
def test_docbook::chaptertype_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original

@given(instance=docbook::BookType_strategy)
@settings(max_examples=50)
def test_docbook::booktype_instantiation(instance):
    assert isinstance(instance, docbook::BookType)

@given(instance=docbook::BookType_strategy)
def test_docbook::booktype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=docbook::BookType_strategy)
def test_docbook::booktype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=docbook::BookType_strategy)
def test_docbook::booktype_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=docbook::BookType_strategy)
def test_docbook::booktype_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original
