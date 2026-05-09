import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sourceanalysator::Library,
    sourceanalysator::Hyperlink,
    sourceanalysator::Article,
    sourceanalysator::Source,
    sourceanalysator::GeneralSource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sourceanalysator::library_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator::Library)


def test_sourceanalysator::library_constructor_exists():
    assert callable(sourceanalysator::Library.__init__)


def test_sourceanalysator::library_constructor_args():
    sig = inspect.signature(sourceanalysator::Library.__init__)
    params = list(sig.parameters.keys())



def test_sourceanalysator::hyperlink_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator::Hyperlink)


def test_sourceanalysator::hyperlink_constructor_exists():
    assert callable(sourceanalysator::Hyperlink.__init__)


def test_sourceanalysator::hyperlink_constructor_args():
    sig = inspect.signature(sourceanalysator::Hyperlink.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_sourceanalysator::hyperlink_has_url():
    assert hasattr(sourceanalysator::Hyperlink, "url")
    descriptor = None
    for klass in sourceanalysator::Hyperlink.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_sourceanalysator::article_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator::Article)


def test_sourceanalysator::article_constructor_exists():
    assert callable(sourceanalysator::Article.__init__)


def test_sourceanalysator::article_constructor_args():
    sig = inspect.signature(sourceanalysator::Article.__init__)
    params = list(sig.parameters.keys())
    assert "localFile" in params, "Missing parameter 'localFile'"
    assert "title" in params, "Missing parameter 'title'"

def test_sourceanalysator::article_has_localFile():
    assert hasattr(sourceanalysator::Article, "localFile")
    descriptor = None
    for klass in sourceanalysator::Article.__mro__:
        if "localFile" in klass.__dict__:
            descriptor = klass.__dict__["localFile"]
            break
    assert isinstance(descriptor, property)

def test_sourceanalysator::article_has_title():
    assert hasattr(sourceanalysator::Article, "title")
    descriptor = None
    for klass in sourceanalysator::Article.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_sourceanalysator::source_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator::Source)


def test_sourceanalysator::source_constructor_exists():
    assert callable(sourceanalysator::Source.__init__)


def test_sourceanalysator::source_constructor_args():
    sig = inspect.signature(sourceanalysator::Source.__init__)
    params = list(sig.parameters.keys())



def test_sourceanalysator::generalsource_is_not_abstract():
    assert not inspect.isabstract(sourceanalysator::GeneralSource)


def test_sourceanalysator::generalsource_constructor_exists():
    assert callable(sourceanalysator::GeneralSource.__init__)


def test_sourceanalysator::generalsource_constructor_args():
    sig = inspect.signature(sourceanalysator::GeneralSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "aliases" in params, "Missing parameter 'aliases'"
    assert "dontCount" in params, "Missing parameter 'dontCount'"

def test_sourceanalysator::generalsource_has_name():
    assert hasattr(sourceanalysator::GeneralSource, "name")
    descriptor = None
    for klass in sourceanalysator::GeneralSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourceanalysator::generalsource_has_aliases():
    assert hasattr(sourceanalysator::GeneralSource, "aliases")
    descriptor = None
    for klass in sourceanalysator::GeneralSource.__mro__:
        if "aliases" in klass.__dict__:
            descriptor = klass.__dict__["aliases"]
            break
    assert isinstance(descriptor, property)

def test_sourceanalysator::generalsource_has_dontCount():
    assert hasattr(sourceanalysator::GeneralSource, "dontCount")
    descriptor = None
    for klass in sourceanalysator::GeneralSource.__mro__:
        if "dontCount" in klass.__dict__:
            descriptor = klass.__dict__["dontCount"]
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
sourceanalysator::Library_strategy = st.builds(
    sourceanalysator::Library,
)
sourceanalysator::Hyperlink_strategy = st.builds(
    sourceanalysator::Hyperlink,
    url=
        safe_text
)
sourceanalysator::Article_strategy = st.builds(
    sourceanalysator::Article,
    localFile=
        safe_text,
    title=
        safe_text
)
sourceanalysator::Source_strategy = st.builds(
    sourceanalysator::Source,
)
sourceanalysator::GeneralSource_strategy = st.builds(
    sourceanalysator::GeneralSource,
    name=
        safe_text,
    aliases=
        safe_text,
    dontCount=
        st.booleans()
)

@given(instance=sourceanalysator::Library_strategy)
@settings(max_examples=50)
def test_sourceanalysator::library_instantiation(instance):
    assert isinstance(instance, sourceanalysator::Library)

@given(instance=sourceanalysator::Hyperlink_strategy)
@settings(max_examples=50)
def test_sourceanalysator::hyperlink_instantiation(instance):
    assert isinstance(instance, sourceanalysator::Hyperlink)

@given(instance=sourceanalysator::Hyperlink_strategy)
def test_sourceanalysator::hyperlink_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=sourceanalysator::Hyperlink_strategy)
def test_sourceanalysator::hyperlink_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=sourceanalysator::Article_strategy)
@settings(max_examples=50)
def test_sourceanalysator::article_instantiation(instance):
    assert isinstance(instance, sourceanalysator::Article)

@given(instance=sourceanalysator::Article_strategy)
def test_sourceanalysator::article_localFile_type(instance):
    assert isinstance(instance.localFile, str)


@given(instance=sourceanalysator::Article_strategy)
def test_sourceanalysator::article_localFile_setter(instance):
    original = instance.localFile
    instance.localFile = original
    assert instance.localFile == original

@given(instance=sourceanalysator::Article_strategy)
def test_sourceanalysator::article_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=sourceanalysator::Article_strategy)
def test_sourceanalysator::article_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=sourceanalysator::Source_strategy)
@settings(max_examples=50)
def test_sourceanalysator::source_instantiation(instance):
    assert isinstance(instance, sourceanalysator::Source)

@given(instance=sourceanalysator::GeneralSource_strategy)
@settings(max_examples=50)
def test_sourceanalysator::generalsource_instantiation(instance):
    assert isinstance(instance, sourceanalysator::GeneralSource)

@given(instance=sourceanalysator::GeneralSource_strategy)
def test_sourceanalysator::generalsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourceanalysator::GeneralSource_strategy)
def test_sourceanalysator::generalsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourceanalysator::GeneralSource_strategy)
def test_sourceanalysator::generalsource_aliases_type(instance):
    assert isinstance(instance.aliases, str)


@given(instance=sourceanalysator::GeneralSource_strategy)
def test_sourceanalysator::generalsource_aliases_setter(instance):
    original = instance.aliases
    instance.aliases = original
    assert instance.aliases == original

@given(instance=sourceanalysator::GeneralSource_strategy)
def test_sourceanalysator::generalsource_dontCount_type(instance):
    assert isinstance(instance.dontCount, bool)


@given(instance=sourceanalysator::GeneralSource_strategy)
def test_sourceanalysator::generalsource_dontCount_setter(instance):
    original = instance.dontCount
    instance.dontCount = original
    assert instance.dontCount == original
