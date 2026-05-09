import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ktest400::NamedElement,
    NamedElement,
    ktest400::RelatedTo,
    ktest400::Line,
    ktest400::Article,
    ktest400::Thing,
    ktest400::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ktest400::namedelement_is_not_abstract():
    assert not inspect.isabstract(ktest400::NamedElement)


def test_ktest400::namedelement_constructor_exists():
    assert callable(ktest400::NamedElement.__init__)


def test_ktest400::namedelement_constructor_args():
    sig = inspect.signature(ktest400::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ktest400::namedelement_has_name():
    assert hasattr(ktest400::NamedElement, "name")
    descriptor = None
    for klass in ktest400::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ktest400::relatedto_is_not_abstract():
    assert not inspect.isabstract(ktest400::RelatedTo)


def test_ktest400::relatedto_constructor_exists():
    assert callable(ktest400::RelatedTo.__init__)


def test_ktest400::relatedto_constructor_args():
    sig = inspect.signature(ktest400::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_ktest400::relatedto_has_since():
    assert hasattr(ktest400::RelatedTo, "since")
    descriptor = None
    for klass in ktest400::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_ktest400::line_is_not_abstract():
    assert not inspect.isabstract(ktest400::Line)


def test_ktest400::line_constructor_exists():
    assert callable(ktest400::Line.__init__)


def test_ktest400::line_constructor_args():
    sig = inspect.signature(ktest400::Line.__init__)
    params = list(sig.parameters.keys())
    assert "quant" in params, "Missing parameter 'quant'"
    assert "articleAid" in params, "Missing parameter 'articleAid'"

def test_ktest400::line_has_quant():
    assert hasattr(ktest400::Line, "quant")
    descriptor = None
    for klass in ktest400::Line.__mro__:
        if "quant" in klass.__dict__:
            descriptor = klass.__dict__["quant"]
            break
    assert isinstance(descriptor, property)

def test_ktest400::line_has_articleAid():
    assert hasattr(ktest400::Line, "articleAid")
    descriptor = None
    for klass in ktest400::Line.__mro__:
        if "articleAid" in klass.__dict__:
            descriptor = klass.__dict__["articleAid"]
            break
    assert isinstance(descriptor, property)



def test_ktest400::article_is_not_abstract():
    assert not inspect.isabstract(ktest400::Article)


def test_ktest400::article_constructor_exists():
    assert callable(ktest400::Article.__init__)


def test_ktest400::article_constructor_args():
    sig = inspect.signature(ktest400::Article.__init__)
    params = list(sig.parameters.keys())
    assert "aid" in params, "Missing parameter 'aid'"

def test_ktest400::article_has_aid():
    assert hasattr(ktest400::Article, "aid")
    descriptor = None
    for klass in ktest400::Article.__mro__:
        if "aid" in klass.__dict__:
            descriptor = klass.__dict__["aid"]
            break
    assert isinstance(descriptor, property)



def test_ktest400::thing_is_not_abstract():
    assert not inspect.isabstract(ktest400::Thing)


def test_ktest400::thing_constructor_exists():
    assert callable(ktest400::Thing.__init__)


def test_ktest400::thing_constructor_args():
    sig = inspect.signature(ktest400::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ktest400::thing_has_id():
    assert hasattr(ktest400::Thing, "id")
    descriptor = None
    for klass in ktest400::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ktest400::world_is_not_abstract():
    assert not inspect.isabstract(ktest400::World)


def test_ktest400::world_constructor_exists():
    assert callable(ktest400::World.__init__)


def test_ktest400::world_constructor_args():
    sig = inspect.signature(ktest400::World.__init__)
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
ktest400::NamedElement_strategy = st.builds(
    ktest400::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ktest400::RelatedTo_strategy = st.builds(
    ktest400::RelatedTo,
    since=
        safe_text
)
ktest400::Line_strategy = st.builds(
    ktest400::Line,
    quant=
        st.integers(),
    articleAid=
        safe_text
)
ktest400::Article_strategy = st.builds(
    ktest400::Article,
    aid=
        safe_text
)
ktest400::Thing_strategy = st.builds(
    ktest400::Thing,
    id=
        st.integers()
)
ktest400::World_strategy = st.builds(
    ktest400::World,
)

@given(instance=ktest400::NamedElement_strategy)
@settings(max_examples=50)
def test_ktest400::namedelement_instantiation(instance):
    assert isinstance(instance, ktest400::NamedElement)

@given(instance=ktest400::NamedElement_strategy)
def test_ktest400::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ktest400::NamedElement_strategy)
def test_ktest400::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ktest400::RelatedTo_strategy)
@settings(max_examples=50)
def test_ktest400::relatedto_instantiation(instance):
    assert isinstance(instance, ktest400::RelatedTo)

@given(instance=ktest400::RelatedTo_strategy)
def test_ktest400::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=ktest400::RelatedTo_strategy)
def test_ktest400::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=ktest400::Line_strategy)
@settings(max_examples=50)
def test_ktest400::line_instantiation(instance):
    assert isinstance(instance, ktest400::Line)

@given(instance=ktest400::Line_strategy)
def test_ktest400::line_quant_type(instance):
    assert isinstance(instance.quant, int)


@given(instance=ktest400::Line_strategy)
def test_ktest400::line_quant_setter(instance):
    original = instance.quant
    instance.quant = original
    assert instance.quant == original

@given(instance=ktest400::Line_strategy)
def test_ktest400::line_articleAid_type(instance):
    assert isinstance(instance.articleAid, str)


@given(instance=ktest400::Line_strategy)
def test_ktest400::line_articleAid_setter(instance):
    original = instance.articleAid
    instance.articleAid = original
    assert instance.articleAid == original

@given(instance=ktest400::Article_strategy)
@settings(max_examples=50)
def test_ktest400::article_instantiation(instance):
    assert isinstance(instance, ktest400::Article)

@given(instance=ktest400::Article_strategy)
def test_ktest400::article_aid_type(instance):
    assert isinstance(instance.aid, str)


@given(instance=ktest400::Article_strategy)
def test_ktest400::article_aid_setter(instance):
    original = instance.aid
    instance.aid = original
    assert instance.aid == original

@given(instance=ktest400::Thing_strategy)
@settings(max_examples=50)
def test_ktest400::thing_instantiation(instance):
    assert isinstance(instance, ktest400::Thing)

@given(instance=ktest400::Thing_strategy)
def test_ktest400::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=ktest400::Thing_strategy)
def test_ktest400::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ktest400::World_strategy)
@settings(max_examples=50)
def test_ktest400::world_instantiation(instance):
    assert isinstance(instance, ktest400::World)
