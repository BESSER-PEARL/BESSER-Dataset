import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::RefArcs,
    petrinet::RefNodes,
    RefPetriNets,
    petrinet::PetriNet,
    RefTokens,
    petrinet::Token,
    petrinet::RefTokens,
    Node,
    petrinet::Place,
    petrinet::Transition,
    RefArcs,
    petrinet::Arc,
    RefNodes,
    petrinet::Node,
    petrinet::RefPetriNets,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::refarcs_is_not_abstract():
    assert not inspect.isabstract(petrinet::RefArcs)


def test_petrinet::refarcs_constructor_exists():
    assert callable(petrinet::RefArcs.__init__)


def test_petrinet::refarcs_constructor_args():
    sig = inspect.signature(petrinet::RefArcs.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::refnodes_is_not_abstract():
    assert not inspect.isabstract(petrinet::RefNodes)


def test_petrinet::refnodes_constructor_exists():
    assert callable(petrinet::RefNodes.__init__)


def test_petrinet::refnodes_constructor_args():
    sig = inspect.signature(petrinet::RefNodes.__init__)
    params = list(sig.parameters.keys())



def test_refpetrinets_is_not_abstract():
    assert not inspect.isabstract(RefPetriNets)


def test_refpetrinets_constructor_exists():
    assert callable(RefPetriNets.__init__)


def test_refpetrinets_constructor_args():
    sig = inspect.signature(RefPetriNets.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petrinet::PetriNet, "name")
    descriptor = None
    for klass in petrinet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_reftokens_is_not_abstract():
    assert not inspect.isabstract(RefTokens)


def test_reftokens_constructor_exists():
    assert callable(RefTokens.__init__)


def test_reftokens_constructor_args():
    sig = inspect.signature(RefTokens.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::token_is_not_abstract():
    assert not inspect.isabstract(petrinet::Token)


def test_petrinet::token_constructor_exists():
    assert callable(petrinet::Token.__init__)


def test_petrinet::token_constructor_args():
    sig = inspect.signature(petrinet::Token.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::token_has_name():
    assert hasattr(petrinet::Token, "name")
    descriptor = None
    for klass in petrinet::Token.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::reftokens_is_not_abstract():
    assert not inspect.isabstract(petrinet::RefTokens)


def test_petrinet::reftokens_constructor_exists():
    assert callable(petrinet::RefTokens.__init__)


def test_petrinet::reftokens_constructor_args():
    sig = inspect.signature(petrinet::RefTokens.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_refarcs_is_not_abstract():
    assert not inspect.isabstract(RefArcs)


def test_refarcs_constructor_exists():
    assert callable(RefArcs.__init__)


def test_refarcs_constructor_args():
    sig = inspect.signature(RefArcs.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::arc_has_name():
    assert hasattr(petrinet::Arc, "name")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refnodes_is_not_abstract():
    assert not inspect.isabstract(RefNodes)


def test_refnodes_constructor_exists():
    assert callable(RefNodes.__init__)


def test_refnodes_constructor_args():
    sig = inspect.signature(RefNodes.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::node_has_name():
    assert hasattr(petrinet::Node, "name")
    descriptor = None
    for klass in petrinet::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::refpetrinets_is_not_abstract():
    assert not inspect.isabstract(petrinet::RefPetriNets)


def test_petrinet::refpetrinets_constructor_exists():
    assert callable(petrinet::RefPetriNets.__init__)


def test_petrinet::refpetrinets_constructor_args():
    sig = inspect.signature(petrinet::RefPetriNets.__init__)
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
petrinet::RefArcs_strategy = st.builds(
    petrinet::RefArcs,
)
petrinet::RefNodes_strategy = st.builds(
    petrinet::RefNodes,
)
RefPetriNets_strategy = st.builds(
    RefPetriNets,
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
    name=
        safe_text
)
RefTokens_strategy = st.builds(
    RefTokens,
)
petrinet::Token_strategy = st.builds(
    petrinet::Token,
    name=
        safe_text
)
petrinet::RefTokens_strategy = st.builds(
    petrinet::RefTokens,
)
Node_strategy = st.builds(
    Node,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
RefArcs_strategy = st.builds(
    RefArcs,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    name=
        safe_text
)
RefNodes_strategy = st.builds(
    RefNodes,
)
petrinet::Node_strategy = st.builds(
    petrinet::Node,
    name=
        safe_text
)
petrinet::RefPetriNets_strategy = st.builds(
    petrinet::RefPetriNets,
)

@given(instance=petrinet::RefArcs_strategy)
@settings(max_examples=50)
def test_petrinet::refarcs_instantiation(instance):
    assert isinstance(instance, petrinet::RefArcs)

@given(instance=petrinet::RefNodes_strategy)
@settings(max_examples=50)
def test_petrinet::refnodes_instantiation(instance):
    assert isinstance(instance, petrinet::RefNodes)

@given(instance=RefPetriNets_strategy)
@settings(max_examples=50)
def test_refpetrinets_instantiation(instance):
    assert isinstance(instance, RefPetriNets)

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RefTokens_strategy)
@settings(max_examples=50)
def test_reftokens_instantiation(instance):
    assert isinstance(instance, RefTokens)

@given(instance=petrinet::Token_strategy)
@settings(max_examples=50)
def test_petrinet::token_instantiation(instance):
    assert isinstance(instance, petrinet::Token)

@given(instance=petrinet::Token_strategy)
def test_petrinet::token_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Token_strategy)
def test_petrinet::token_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::RefTokens_strategy)
@settings(max_examples=50)
def test_petrinet::reftokens_instantiation(instance):
    assert isinstance(instance, petrinet::RefTokens)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=RefArcs_strategy)
@settings(max_examples=50)
def test_refarcs_instantiation(instance):
    assert isinstance(instance, RefArcs)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RefNodes_strategy)
@settings(max_examples=50)
def test_refnodes_instantiation(instance):
    assert isinstance(instance, RefNodes)

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::RefPetriNets_strategy)
@settings(max_examples=50)
def test_petrinet::refpetrinets_instantiation(instance):
    assert isinstance(instance, petrinet::RefPetriNets)
