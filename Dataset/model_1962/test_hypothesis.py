import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sourceanalysator_Library,
    sourceanalysator_Hyperlink,
    sourceanalysator_Article,
    sourceanalysator_Source,
    sourceanalysator_GeneralSource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sourceanalysator_library_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator_Library)


def test_sourceanalysator_library_constructor_exists():
    assert callable(sourceanalysator_Library.__init__)


def test_sourceanalysator_library_constructor_args():
    sig = inspect.signature(sourceanalysator_Library.__init__)
    params = list(sig.parameters.keys())



def test_sourceanalysator_hyperlink_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator_Hyperlink)


def test_sourceanalysator_hyperlink_constructor_exists():
    assert callable(sourceanalysator_Hyperlink.__init__)


def test_sourceanalysator_hyperlink_constructor_args():
    sig = inspect.signature(sourceanalysator_Hyperlink.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_sourceanalysator_hyperlink_has_url():
    assert hasattr(sourceanalysator_Hyperlink, "url")
    descriptor = None
    for klass in sourceanalysator_Hyperlink.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_sourceanalysator_article_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator_Article)


def test_sourceanalysator_article_constructor_exists():
    assert callable(sourceanalysator_Article.__init__)


def test_sourceanalysator_article_constructor_args():
    sig = inspect.signature(sourceanalysator_Article.__init__)
    params = list(sig.parameters.keys())
    assert "localFile" in params, "Missing parameter 'localFile'"
    assert "title" in params, "Missing parameter 'title'"

def test_sourceanalysator_article_has_localFile():
    assert hasattr(sourceanalysator_Article, "localFile")
    descriptor = None
    for klass in sourceanalysator_Article.__mro__:
        if "localFile" in klass.__dict__:
            descriptor = klass.__dict__["localFile"]
            break
    assert isinstance(descriptor, property)

def test_sourceanalysator_article_has_title():
    assert hasattr(sourceanalysator_Article, "title")
    descriptor = None
    for klass in sourceanalysator_Article.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_sourceanalysator_source_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator_Source)


def test_sourceanalysator_source_constructor_exists():
    assert callable(sourceanalysator_Source.__init__)


def test_sourceanalysator_source_constructor_args():
    sig = inspect.signature(sourceanalysator_Source.__init__)
    params = list(sig.parameters.keys())



def test_sourceanalysator_generalsource_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator_GeneralSource)


def test_sourceanalysator_generalsource_constructor_exists():
    assert callable(sourceanalysator_GeneralSource.__init__)


def test_sourceanalysator_generalsource_constructor_args():
    sig = inspect.signature(sourceanalysator_GeneralSource.__init__)
    params = list(sig.parameters.keys())
    assert "dontCount" in params, "Missing parameter 'dontCount'"
    assert "aliases" in params, "Missing parameter 'aliases'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourceanalysator_generalsource_has_dontCount():
    assert hasattr(sourceanalysator_GeneralSource, "dontCount")
    descriptor = None
    for klass in sourceanalysator_GeneralSource.__mro__:
        if "dontCount" in klass.__dict__:
            descriptor = klass.__dict__["dontCount"]
            break
    assert isinstance(descriptor, property)

def test_sourceanalysator_generalsource_has_aliases():
    assert hasattr(sourceanalysator_GeneralSource, "aliases")
    descriptor = None
    for klass in sourceanalysator_GeneralSource.__mro__:
        if "aliases" in klass.__dict__:
            descriptor = klass.__dict__["aliases"]
            break
    assert isinstance(descriptor, property)

def test_sourceanalysator_generalsource_has_name():
    assert hasattr(sourceanalysator_GeneralSource, "name")
    descriptor = None
    for klass in sourceanalysator_GeneralSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
sourceanalysator_Library_strategy = st.builds(
    sourceanalysator_Library,
)
sourceanalysator_Hyperlink_strategy = st.builds(
    sourceanalysator_Hyperlink,
    url=
        safe_text
)
sourceanalysator_Article_strategy = st.builds(
    sourceanalysator_Article,
    localFile=
        safe_text,
    title=
        safe_text
)
sourceanalysator_Source_strategy = st.builds(
    sourceanalysator_Source,
)
sourceanalysator_GeneralSource_strategy = st.builds(
    sourceanalysator_GeneralSource,
    dontCount=
        st.booleans(),
    aliases=
        safe_text,
    name=
        safe_text
)

@given(instance=sourceanalysator_Library_strategy)
@settings(max_examples=50)
def test_sourceanalysator_library_instantiation(instance):
    assert isinstance(instance, sourceanalysator_Library)

@given(instance=sourceanalysator_Hyperlink_strategy)
@settings(max_examples=50)
def test_sourceanalysator_hyperlink_instantiation(instance):
    assert isinstance(instance, sourceanalysator_Hyperlink)



@given(instance=sourceanalysator_Hyperlink_strategy)
def test_sourceanalysator_hyperlink_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=sourceanalysator_Article_strategy)
@settings(max_examples=50)
def test_sourceanalysator_article_instantiation(instance):
    assert isinstance(instance, sourceanalysator_Article)



@given(instance=sourceanalysator_Article_strategy)
def test_sourceanalysator_article_localFile_setter(instance):
    original = instance.localFile
    instance.localFile = original
    assert instance.localFile == original



@given(instance=sourceanalysator_Article_strategy)
def test_sourceanalysator_article_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=sourceanalysator_Source_strategy)
@settings(max_examples=50)
def test_sourceanalysator_source_instantiation(instance):
    assert isinstance(instance, sourceanalysator_Source)

@given(instance=sourceanalysator_GeneralSource_strategy)
@settings(max_examples=50)
def test_sourceanalysator_generalsource_instantiation(instance):
    assert isinstance(instance, sourceanalysator_GeneralSource)



@given(instance=sourceanalysator_GeneralSource_strategy)
def test_sourceanalysator_generalsource_dontCount_setter(instance):
    original = instance.dontCount
    instance.dontCount = original
    assert instance.dontCount == original



@given(instance=sourceanalysator_GeneralSource_strategy)
def test_sourceanalysator_generalsource_aliases_setter(instance):
    original = instance.aliases
    instance.aliases = original
    assert instance.aliases == original



@given(instance=sourceanalysator_GeneralSource_strategy)
def test_sourceanalysator_generalsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
