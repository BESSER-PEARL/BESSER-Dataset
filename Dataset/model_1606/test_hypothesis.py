import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pn_NamedElement,
    NetElement,
    pn_Transition,
    NamedElement,
    pn_Place,
    pn_NetElement,
    pn_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pn_namedelement_is_not_abstract():
    assert not inspect.isabstract(pn_NamedElement)


def test_pn_namedelement_constructor_exists():
    assert callable(pn_NamedElement.__init__)


def test_pn_namedelement_constructor_args():
    sig = inspect.signature(pn_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn_namedelement_has_name():
    assert hasattr(pn_NamedElement, "name")
    descriptor = None
    for klass in pn_NamedElement.__mro__:
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



def test_pn_transition_is_not_abstract():
    assert not inspect.isabstract(pn_Transition)


def test_pn_transition_constructor_exists():
    assert callable(pn_Transition.__init__)


def test_pn_transition_constructor_args():
    sig = inspect.signature(pn_Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pn_place_is_not_abstract():
    assert not inspect.isabstract(pn_Place)


def test_pn_place_constructor_exists():
    assert callable(pn_Place.__init__)


def test_pn_place_constructor_args():
    sig = inspect.signature(pn_Place.__init__)
    params = list(sig.parameters.keys())
    assert "noOfTokens" in params, "Missing parameter 'noOfTokens'"

def test_pn_place_has_noOfTokens():
    assert hasattr(pn_Place, "noOfTokens")
    descriptor = None
    for klass in pn_Place.__mro__:
        if "noOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["noOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_pn_netelement_is_not_abstract():
    assert not inspect.isabstract(pn_NetElement)


def test_pn_netelement_constructor_exists():
    assert callable(pn_NetElement.__init__)


def test_pn_netelement_constructor_args():
    sig = inspect.signature(pn_NetElement.__init__)
    params = list(sig.parameters.keys())



def test_pn_net_is_not_abstract():
    assert not inspect.isabstract(pn_Net)


def test_pn_net_constructor_exists():
    assert callable(pn_Net.__init__)


def test_pn_net_constructor_args():
    sig = inspect.signature(pn_Net.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"

def test_pn_net_has_incrementalID():
    assert hasattr(pn_Net, "incrementalID")
    descriptor = None
    for klass in pn_Net.__mro__:
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
pn_NamedElement_strategy = st.builds(
    pn_NamedElement,
    name=
        safe_text
)
NetElement_strategy = st.builds(
    NetElement,
)
pn_Transition_strategy = st.builds(
    pn_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pn_Place_strategy = st.builds(
    pn_Place,
    noOfTokens=
        st.integers()
)
pn_NetElement_strategy = st.builds(
    pn_NetElement,
)
pn_Net_strategy = st.builds(
    pn_Net,
    incrementalID=
        safe_text
)

@given(instance=pn_NamedElement_strategy)
@settings(max_examples=50)
def test_pn_namedelement_instantiation(instance):
    assert isinstance(instance, pn_NamedElement)



@given(instance=pn_NamedElement_strategy)
def test_pn_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NetElement_strategy)
@settings(max_examples=50)
def test_netelement_instantiation(instance):
    assert isinstance(instance, NetElement)

@given(instance=pn_Transition_strategy)
@settings(max_examples=50)
def test_pn_transition_instantiation(instance):
    assert isinstance(instance, pn_Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=pn_Place_strategy)
@settings(max_examples=50)
def test_pn_place_instantiation(instance):
    assert isinstance(instance, pn_Place)



@given(instance=pn_Place_strategy)
def test_pn_place_noOfTokens_setter(instance):
    original = instance.noOfTokens
    instance.noOfTokens = original
    assert instance.noOfTokens == original

@given(instance=pn_NetElement_strategy)
@settings(max_examples=50)
def test_pn_netelement_instantiation(instance):
    assert isinstance(instance, pn_NetElement)

@given(instance=pn_Net_strategy)
@settings(max_examples=50)
def test_pn_net_instantiation(instance):
    assert isinstance(instance, pn_Net)



@given(instance=pn_Net_strategy)
def test_pn_net_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original
