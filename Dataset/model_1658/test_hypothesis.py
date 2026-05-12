import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ktest400_NamedElement,
    NamedElement,
    ktest400_RelatedTo,
    ktest400_Line,
    ktest400_Article,
    ktest400_Thing,
    ktest400_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ktest400_namedelement_is_not_abstract():
    assert not inspect.isabstract(ktest400_NamedElement)


def test_ktest400_namedelement_constructor_exists():
    assert callable(ktest400_NamedElement.__init__)


def test_ktest400_namedelement_constructor_args():
    sig = inspect.signature(ktest400_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ktest400_namedelement_has_name():
    assert hasattr(ktest400_NamedElement, "name")
    descriptor = None
    for klass in ktest400_NamedElement.__mro__:
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



def test_ktest400_relatedto_is_not_abstract():
    assert not inspect.isabstract(ktest400_RelatedTo)


def test_ktest400_relatedto_constructor_exists():
    assert callable(ktest400_RelatedTo.__init__)


def test_ktest400_relatedto_constructor_args():
    sig = inspect.signature(ktest400_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_ktest400_relatedto_has_since():
    assert hasattr(ktest400_RelatedTo, "since")
    descriptor = None
    for klass in ktest400_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_ktest400_line_is_not_abstract():
    assert not inspect.isabstract(ktest400_Line)


def test_ktest400_line_constructor_exists():
    assert callable(ktest400_Line.__init__)


def test_ktest400_line_constructor_args():
    sig = inspect.signature(ktest400_Line.__init__)
    params = list(sig.parameters.keys())
    assert "articleAid" in params, "Missing parameter 'articleAid'"
    assert "quant" in params, "Missing parameter 'quant'"

def test_ktest400_line_has_articleAid():
    assert hasattr(ktest400_Line, "articleAid")
    descriptor = None
    for klass in ktest400_Line.__mro__:
        if "articleAid" in klass.__dict__:
            descriptor = klass.__dict__["articleAid"]
            break
    assert isinstance(descriptor, property)

def test_ktest400_line_has_quant():
    assert hasattr(ktest400_Line, "quant")
    descriptor = None
    for klass in ktest400_Line.__mro__:
        if "quant" in klass.__dict__:
            descriptor = klass.__dict__["quant"]
            break
    assert isinstance(descriptor, property)



def test_ktest400_article_is_not_abstract():
    assert not inspect.isabstract(ktest400_Article)


def test_ktest400_article_constructor_exists():
    assert callable(ktest400_Article.__init__)


def test_ktest400_article_constructor_args():
    sig = inspect.signature(ktest400_Article.__init__)
    params = list(sig.parameters.keys())
    assert "aid" in params, "Missing parameter 'aid'"

def test_ktest400_article_has_aid():
    assert hasattr(ktest400_Article, "aid")
    descriptor = None
    for klass in ktest400_Article.__mro__:
        if "aid" in klass.__dict__:
            descriptor = klass.__dict__["aid"]
            break
    assert isinstance(descriptor, property)



def test_ktest400_thing_is_not_abstract():
    assert not inspect.isabstract(ktest400_Thing)


def test_ktest400_thing_constructor_exists():
    assert callable(ktest400_Thing.__init__)


def test_ktest400_thing_constructor_args():
    sig = inspect.signature(ktest400_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ktest400_thing_has_id():
    assert hasattr(ktest400_Thing, "id")
    descriptor = None
    for klass in ktest400_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ktest400_world_is_not_abstract():
    assert not inspect.isabstract(ktest400_World)


def test_ktest400_world_constructor_exists():
    assert callable(ktest400_World.__init__)


def test_ktest400_world_constructor_args():
    sig = inspect.signature(ktest400_World.__init__)
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
ktest400_NamedElement_strategy = st.builds(
    ktest400_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ktest400_RelatedTo_strategy = st.builds(
    ktest400_RelatedTo,
    since=
        safe_text
)
ktest400_Line_strategy = st.builds(
    ktest400_Line,
    articleAid=
        safe_text,
    quant=
        st.integers()
)
ktest400_Article_strategy = st.builds(
    ktest400_Article,
    aid=
        safe_text
)
ktest400_Thing_strategy = st.builds(
    ktest400_Thing,
    id=
        st.integers()
)
ktest400_World_strategy = st.builds(
    ktest400_World,
)

@given(instance=ktest400_NamedElement_strategy)
@settings(max_examples=50)
def test_ktest400_namedelement_instantiation(instance):
    assert isinstance(instance, ktest400_NamedElement)



@given(instance=ktest400_NamedElement_strategy)
def test_ktest400_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ktest400_RelatedTo_strategy)
@settings(max_examples=50)
def test_ktest400_relatedto_instantiation(instance):
    assert isinstance(instance, ktest400_RelatedTo)



@given(instance=ktest400_RelatedTo_strategy)
def test_ktest400_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=ktest400_Line_strategy)
@settings(max_examples=50)
def test_ktest400_line_instantiation(instance):
    assert isinstance(instance, ktest400_Line)



@given(instance=ktest400_Line_strategy)
def test_ktest400_line_articleAid_setter(instance):
    original = instance.articleAid
    instance.articleAid = original
    assert instance.articleAid == original



@given(instance=ktest400_Line_strategy)
def test_ktest400_line_quant_setter(instance):
    original = instance.quant
    instance.quant = original
    assert instance.quant == original

@given(instance=ktest400_Article_strategy)
@settings(max_examples=50)
def test_ktest400_article_instantiation(instance):
    assert isinstance(instance, ktest400_Article)



@given(instance=ktest400_Article_strategy)
def test_ktest400_article_aid_setter(instance):
    original = instance.aid
    instance.aid = original
    assert instance.aid == original

@given(instance=ktest400_Thing_strategy)
@settings(max_examples=50)
def test_ktest400_thing_instantiation(instance):
    assert isinstance(instance, ktest400_Thing)



@given(instance=ktest400_Thing_strategy)
def test_ktest400_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ktest400_World_strategy)
@settings(max_examples=50)
def test_ktest400_world_instantiation(instance):
    assert isinstance(instance, ktest400_World)
