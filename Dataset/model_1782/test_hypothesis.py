import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    docbook_Sect1Type,
    docbook_EStringToStringMapEntry,
    docbook_DocumentRoot,
    docbook_ChapterType,
    docbook_BookType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docbook_sect1type_is_not_abstract():
    assert not inspect.isabstract(docbook_Sect1Type)


def test_docbook_sect1type_constructor_exists():
    assert callable(docbook_Sect1Type.__init__)


def test_docbook_sect1type_constructor_args():
    sig = inspect.signature(docbook_Sect1Type.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "title" in params, "Missing parameter 'title'"
    assert "para" in params, "Missing parameter 'para'"

def test_docbook_sect1type_has_mixed():
    assert hasattr(docbook_Sect1Type, "mixed")
    descriptor = None
    for klass in docbook_Sect1Type.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_sect1type_has_title():
    assert hasattr(docbook_Sect1Type, "title")
    descriptor = None
    for klass in docbook_Sect1Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook_sect1type_has_para():
    assert hasattr(docbook_Sect1Type, "para")
    descriptor = None
    for klass in docbook_Sect1Type.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)



def test_docbook_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(docbook_EStringToStringMapEntry)


def test_docbook_estringtostringmapentry_constructor_exists():
    assert callable(docbook_EStringToStringMapEntry.__init__)


def test_docbook_estringtostringmapentry_constructor_args():
    sig = inspect.signature(docbook_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_docbook_documentroot_is_not_abstract():
    assert not inspect.isabstract(docbook_DocumentRoot)


def test_docbook_documentroot_constructor_exists():
    assert callable(docbook_DocumentRoot.__init__)


def test_docbook_documentroot_constructor_args():
    sig = inspect.signature(docbook_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "para" in params, "Missing parameter 'para'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "info" in params, "Missing parameter 'info'"

def test_docbook_documentroot_has_title():
    assert hasattr(docbook_DocumentRoot, "title")
    descriptor = None
    for klass in docbook_DocumentRoot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_para():
    assert hasattr(docbook_DocumentRoot, "para")
    descriptor = None
    for klass in docbook_DocumentRoot.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_mixed():
    assert hasattr(docbook_DocumentRoot, "mixed")
    descriptor = None
    for klass in docbook_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_info():
    assert hasattr(docbook_DocumentRoot, "info")
    descriptor = None
    for klass in docbook_DocumentRoot.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_docbook_chaptertype_is_not_abstract():
    assert not inspect.isabstract(docbook_ChapterType)


def test_docbook_chaptertype_constructor_exists():
    assert callable(docbook_ChapterType.__init__)


def test_docbook_chaptertype_constructor_args():
    sig = inspect.signature(docbook_ChapterType.__init__)
    params = list(sig.parameters.keys())
    assert "para" in params, "Missing parameter 'para'"
    assert "title" in params, "Missing parameter 'title'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_chaptertype_has_para():
    assert hasattr(docbook_ChapterType, "para")
    descriptor = None
    for klass in docbook_ChapterType.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)

def test_docbook_chaptertype_has_title():
    assert hasattr(docbook_ChapterType, "title")
    descriptor = None
    for klass in docbook_ChapterType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook_chaptertype_has_mixed():
    assert hasattr(docbook_ChapterType, "mixed")
    descriptor = None
    for klass in docbook_ChapterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_booktype_is_not_abstract():
    assert not inspect.isabstract(docbook_BookType)


def test_docbook_booktype_constructor_exists():
    assert callable(docbook_BookType.__init__)


def test_docbook_booktype_constructor_args():
    sig = inspect.signature(docbook_BookType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "info" in params, "Missing parameter 'info'"

def test_docbook_booktype_has_title():
    assert hasattr(docbook_BookType, "title")
    descriptor = None
    for klass in docbook_BookType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_docbook_booktype_has_info():
    assert hasattr(docbook_BookType, "info")
    descriptor = None
    for klass in docbook_BookType.__mro__:
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
docbook_Sect1Type_strategy = st.builds(
    docbook_Sect1Type,
    mixed=
        safe_text,
    title=
        safe_text,
    para=
        safe_text
)
docbook_EStringToStringMapEntry_strategy = st.builds(
    docbook_EStringToStringMapEntry,
)
docbook_DocumentRoot_strategy = st.builds(
    docbook_DocumentRoot,
    title=
        safe_text,
    para=
        safe_text,
    mixed=
        safe_text,
    info=
        safe_text
)
docbook_ChapterType_strategy = st.builds(
    docbook_ChapterType,
    para=
        safe_text,
    title=
        safe_text,
    mixed=
        safe_text
)
docbook_BookType_strategy = st.builds(
    docbook_BookType,
    title=
        safe_text,
    info=
        safe_text
)

@given(instance=docbook_Sect1Type_strategy)
@settings(max_examples=50)
def test_docbook_sect1type_instantiation(instance):
    assert isinstance(instance, docbook_Sect1Type)



@given(instance=docbook_Sect1Type_strategy)
def test_docbook_sect1type_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=docbook_Sect1Type_strategy)
def test_docbook_sect1type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=docbook_Sect1Type_strategy)
def test_docbook_sect1type_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original

@given(instance=docbook_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_docbook_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, docbook_EStringToStringMapEntry)

@given(instance=docbook_DocumentRoot_strategy)
@settings(max_examples=50)
def test_docbook_documentroot_instantiation(instance):
    assert isinstance(instance, docbook_DocumentRoot)



@given(instance=docbook_DocumentRoot_strategy)
def test_docbook_documentroot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=docbook_DocumentRoot_strategy)
def test_docbook_documentroot_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original



@given(instance=docbook_DocumentRoot_strategy)
def test_docbook_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=docbook_DocumentRoot_strategy)
def test_docbook_documentroot_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=docbook_ChapterType_strategy)
@settings(max_examples=50)
def test_docbook_chaptertype_instantiation(instance):
    assert isinstance(instance, docbook_ChapterType)



@given(instance=docbook_ChapterType_strategy)
def test_docbook_chaptertype_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original



@given(instance=docbook_ChapterType_strategy)
def test_docbook_chaptertype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=docbook_ChapterType_strategy)
def test_docbook_chaptertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=docbook_BookType_strategy)
@settings(max_examples=50)
def test_docbook_booktype_instantiation(instance):
    assert isinstance(instance, docbook_BookType)



@given(instance=docbook_BookType_strategy)
def test_docbook_booktype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=docbook_BookType_strategy)
def test_docbook_booktype_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original
