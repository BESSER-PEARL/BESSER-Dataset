import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pn::NamedElement,
    NetElement,
    pn::Transition,
    NamedElement,
    pn::NetElement,
    pn::Place,
    pn::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pn::namedelement_is_not_abstract():
    assert not inspect.isabstract(pn::NamedElement)


def test_pn::namedelement_constructor_exists():
    assert callable(pn::NamedElement.__init__)


def test_pn::namedelement_constructor_args():
    sig = inspect.signature(pn::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn::namedelement_has_name():
    assert hasattr(pn::NamedElement, "name")
    descriptor = None
    for klass in pn::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_netelement_is_not_abstract():
    assert not inspect.isabstract(NetElement)


def test_netelement_constructor_exists():
    assert callable(NetElement.__init__)


def test_netelement_constructor_args():
    sig = inspect.signature(NetElement.__init__)
    params = list(sig.parameters.keys())



def test_pn::transition_is_not_abstract():
    assert not inspect.isabstract(pn::Transition)


def test_pn::transition_constructor_exists():
    assert callable(pn::Transition.__init__)


def test_pn::transition_constructor_args():
    sig = inspect.signature(pn::Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pn::netelement_is_not_abstract():
    assert not inspect.isabstract(pn::NetElement)


def test_pn::netelement_constructor_exists():
    assert callable(pn::NetElement.__init__)


def test_pn::netelement_constructor_args():
    sig = inspect.signature(pn::NetElement.__init__)
    params = list(sig.parameters.keys())



def test_pn::place_is_not_abstract():
    assert not inspect.isabstract(pn::Place)


def test_pn::place_constructor_exists():
    assert callable(pn::Place.__init__)


def test_pn::place_constructor_args():
    sig = inspect.signature(pn::Place.__init__)
    params = list(sig.parameters.keys())
    assert "noOfTokens" in params, "Missing parameter 'noOfTokens'"

def test_pn::place_has_noOfTokens():
    assert hasattr(pn::Place, "noOfTokens")
    descriptor = None
    for klass in pn::Place.__mro__:
        if "noOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["noOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_pn::net_is_not_abstract():
    assert not inspect.isabstract(pn::Net)


def test_pn::net_constructor_exists():
    assert callable(pn::Net.__init__)


def test_pn::net_constructor_args():
    sig = inspect.signature(pn::Net.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"

def test_pn::net_has_incrementalID():
    assert hasattr(pn::Net, "incrementalID")
    descriptor = None
    for klass in pn::Net.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
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
pn::NamedElement_strategy = st.builds(
    pn::NamedElement,
    name=
        safe_text
)
NetElement_strategy = st.builds(
    NetElement,
)
pn::Transition_strategy = st.builds(
    pn::Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pn::NetElement_strategy = st.builds(
    pn::NetElement,
)
pn::Place_strategy = st.builds(
    pn::Place,
    noOfTokens=
        st.integers()
)
pn::Net_strategy = st.builds(
    pn::Net,
    incrementalID=
        safe_text
)

@given(instance=pn::NamedElement_strategy)
@settings(max_examples=50)
def test_pn::namedelement_instantiation(instance):
    assert isinstance(instance, pn::NamedElement)

@given(instance=pn::NamedElement_strategy)
def test_pn::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pn::NamedElement_strategy)
def test_pn::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NetElement_strategy)
@settings(max_examples=50)
def test_netelement_instantiation(instance):
    assert isinstance(instance, NetElement)

@given(instance=pn::Transition_strategy)
@settings(max_examples=50)
def test_pn::transition_instantiation(instance):
    assert isinstance(instance, pn::Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=pn::NetElement_strategy)
@settings(max_examples=50)
def test_pn::netelement_instantiation(instance):
    assert isinstance(instance, pn::NetElement)

@given(instance=pn::Place_strategy)
@settings(max_examples=50)
def test_pn::place_instantiation(instance):
    assert isinstance(instance, pn::Place)

@given(instance=pn::Place_strategy)
def test_pn::place_noOfTokens_type(instance):
    assert isinstance(instance.noOfTokens, int)


@given(instance=pn::Place_strategy)
def test_pn::place_noOfTokens_setter(instance):
    original = instance.noOfTokens
    instance.noOfTokens = original
    assert instance.noOfTokens == original

@given(instance=pn::Net_strategy)
@settings(max_examples=50)
def test_pn::net_instantiation(instance):
    assert isinstance(instance, pn::Net)

@given(instance=pn::Net_strategy)
def test_pn::net_incrementalID_type(instance):
    assert isinstance(instance.incrementalID, str)


@given(instance=pn::Net_strategy)
def test_pn::net_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original
