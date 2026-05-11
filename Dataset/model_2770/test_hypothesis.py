import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    links::RootNodeA,
    links::Child::AB::Element::Link,
    links::Root,
    links::ChildNodeB,
    links::ChildNodeA,
    links::Root::BA::Element::Link,
    links::RootNodeB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_links::rootnodea_is_not_abstract():
    assert not inspect.isabstract(links::RootNodeA)


def test_links::rootnodea_constructor_exists():
    assert callable(links::RootNodeA.__init__)


def test_links::rootnodea_constructor_args():
    sig = inspect.signature(links::RootNodeA.__init__)
    params = list(sig.parameters.keys())



def test_links::child::ab::element::link_is_not_abstract():
    assert not inspect.isabstract(links::Child::AB::Element::Link)


def test_links::child::ab::element::link_constructor_exists():
    assert callable(links::Child::AB::Element::Link.__init__)


def test_links::child::ab::element::link_constructor_args():
    sig = inspect.signature(links::Child::AB::Element::Link.__init__)
    params = list(sig.parameters.keys())



def test_links::root_is_not_abstract():
    assert not inspect.isabstract(links::Root)


def test_links::root_constructor_exists():
    assert callable(links::Root.__init__)


def test_links::root_constructor_args():
    sig = inspect.signature(links::Root.__init__)
    params = list(sig.parameters.keys())



def test_links::childnodeb_is_not_abstract():
    assert not inspect.isabstract(links::ChildNodeB)


def test_links::childnodeb_constructor_exists():
    assert callable(links::ChildNodeB.__init__)


def test_links::childnodeb_constructor_args():
    sig = inspect.signature(links::ChildNodeB.__init__)
    params = list(sig.parameters.keys())



def test_links::childnodea_is_not_abstract():
    assert not inspect.isabstract(links::ChildNodeA)


def test_links::childnodea_constructor_exists():
    assert callable(links::ChildNodeA.__init__)


def test_links::childnodea_constructor_args():
    sig = inspect.signature(links::ChildNodeA.__init__)
    params = list(sig.parameters.keys())



def test_links::root::ba::element::link_is_not_abstract():
    assert not inspect.isabstract(links::Root::BA::Element::Link)


def test_links::root::ba::element::link_constructor_exists():
    assert callable(links::Root::BA::Element::Link.__init__)


def test_links::root::ba::element::link_constructor_args():
    sig = inspect.signature(links::Root::BA::Element::Link.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_links::root::ba::element::link_has_name():
    assert hasattr(links::Root::BA::Element::Link, "name")
    descriptor = None
    for klass in links::Root::BA::Element::Link.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_links::rootnodeb_is_not_abstract():
    assert not inspect.isabstract(links::RootNodeB)


def test_links::rootnodeb_constructor_exists():
    assert callable(links::RootNodeB.__init__)


def test_links::rootnodeb_constructor_args():
    sig = inspect.signature(links::RootNodeB.__init__)
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
links::RootNodeA_strategy = st.builds(
    links::RootNodeA,
)
links::Child::AB::Element::Link_strategy = st.builds(
    links::Child::AB::Element::Link,
)
links::Root_strategy = st.builds(
    links::Root,
)
links::ChildNodeB_strategy = st.builds(
    links::ChildNodeB,
)
links::ChildNodeA_strategy = st.builds(
    links::ChildNodeA,
)
links::Root::BA::Element::Link_strategy = st.builds(
    links::Root::BA::Element::Link,
    name=
        safe_text
)
links::RootNodeB_strategy = st.builds(
    links::RootNodeB,
)

@given(instance=links::RootNodeA_strategy)
@settings(max_examples=50)
def test_links::rootnodea_instantiation(instance):
    assert isinstance(instance, links::RootNodeA)

@given(instance=links::Child::AB::Element::Link_strategy)
@settings(max_examples=50)
def test_links::child::ab::element::link_instantiation(instance):
    assert isinstance(instance, links::Child::AB::Element::Link)

@given(instance=links::Root_strategy)
@settings(max_examples=50)
def test_links::root_instantiation(instance):
    assert isinstance(instance, links::Root)

@given(instance=links::ChildNodeB_strategy)
@settings(max_examples=50)
def test_links::childnodeb_instantiation(instance):
    assert isinstance(instance, links::ChildNodeB)

@given(instance=links::ChildNodeA_strategy)
@settings(max_examples=50)
def test_links::childnodea_instantiation(instance):
    assert isinstance(instance, links::ChildNodeA)

@given(instance=links::Root::BA::Element::Link_strategy)
@settings(max_examples=50)
def test_links::root::ba::element::link_instantiation(instance):
    assert isinstance(instance, links::Root::BA::Element::Link)

@given(instance=links::Root::BA::Element::Link_strategy)
def test_links::root::ba::element::link_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=links::Root::BA::Element::Link_strategy)
def test_links::root::ba::element::link_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=links::RootNodeB_strategy)
@settings(max_examples=50)
def test_links::rootnodeb_instantiation(instance):
    assert isinstance(instance, links::RootNodeB)
