import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    Edge,
    uppaalSMC::ChanceEdge,
    Location,
    uppaalSMC::ExponentialLocation,
    uppaalSMC::ChanceNode,
    Type,
    uppaalSMC::DoubleType,
    NTA,
    uppaalSMC::NSTA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc::chanceedge_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC::ChanceEdge)


def test_uppaalsmc::chanceedge_constructor_exists():
    assert callable(uppaalSMC::ChanceEdge.__init__)


def test_uppaalsmc::chanceedge_constructor_args():
    sig = inspect.signature(uppaalSMC::ChanceEdge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_uppaalsmc::chanceedge_has_weight():
    assert hasattr(uppaalSMC::ChanceEdge, "weight")
    descriptor = None
    for klass in uppaalSMC::ChanceEdge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc::exponentiallocation_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC::ExponentialLocation)


def test_uppaalsmc::exponentiallocation_constructor_exists():
    assert callable(uppaalSMC::ExponentialLocation.__init__)


def test_uppaalsmc::exponentiallocation_constructor_args():
    sig = inspect.signature(uppaalSMC::ExponentialLocation.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc::chancenode_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC::ChanceNode)


def test_uppaalsmc::chancenode_constructor_exists():
    assert callable(uppaalSMC::ChanceNode.__init__)


def test_uppaalsmc::chancenode_constructor_args():
    sig = inspect.signature(uppaalSMC::ChanceNode.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc::doubletype_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC::DoubleType)


def test_uppaalsmc::doubletype_constructor_exists():
    assert callable(uppaalSMC::DoubleType.__init__)


def test_uppaalsmc::doubletype_constructor_args():
    sig = inspect.signature(uppaalSMC::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_nta_is_not_abstract():
    assert not inspect.isabstract(NTA)


def test_nta_constructor_exists():
    assert callable(NTA.__init__)


def test_nta_constructor_args():
    sig = inspect.signature(NTA.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc::nsta_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC::NSTA)


def test_uppaalsmc::nsta_constructor_exists():
    assert callable(uppaalSMC::NSTA.__init__)


def test_uppaalsmc::nsta_constructor_args():
    sig = inspect.signature(uppaalSMC::NSTA.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
Edge_strategy = st.builds(
    Edge,
)
uppaalSMC::ChanceEdge_strategy = st.builds(
    uppaalSMC::ChanceEdge,
    weight=
        st.integers()
)
Location_strategy = st.builds(
    Location,
)
uppaalSMC::ExponentialLocation_strategy = st.builds(
    uppaalSMC::ExponentialLocation,
)
uppaalSMC::ChanceNode_strategy = st.builds(
    uppaalSMC::ChanceNode,
)
Type_strategy = st.builds(
    Type,
)
uppaalSMC::DoubleType_strategy = st.builds(
    uppaalSMC::DoubleType,
)
NTA_strategy = st.builds(
    NTA,
)
uppaalSMC::NSTA_strategy = st.builds(
    uppaalSMC::NSTA,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=uppaalSMC::ChanceEdge_strategy)
@settings(max_examples=50)
def test_uppaalsmc::chanceedge_instantiation(instance):
    assert isinstance(instance, uppaalSMC::ChanceEdge)

@given(instance=uppaalSMC::ChanceEdge_strategy)
def test_uppaalsmc::chanceedge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=uppaalSMC::ChanceEdge_strategy)
def test_uppaalsmc::chanceedge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=uppaalSMC::ExponentialLocation_strategy)
@settings(max_examples=50)
def test_uppaalsmc::exponentiallocation_instantiation(instance):
    assert isinstance(instance, uppaalSMC::ExponentialLocation)

@given(instance=uppaalSMC::ChanceNode_strategy)
@settings(max_examples=50)
def test_uppaalsmc::chancenode_instantiation(instance):
    assert isinstance(instance, uppaalSMC::ChanceNode)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uppaalSMC::DoubleType_strategy)
@settings(max_examples=50)
def test_uppaalsmc::doubletype_instantiation(instance):
    assert isinstance(instance, uppaalSMC::DoubleType)

@given(instance=NTA_strategy)
@settings(max_examples=50)
def test_nta_instantiation(instance):
    assert isinstance(instance, NTA)

@given(instance=uppaalSMC::NSTA_strategy)
@settings(max_examples=50)
def test_uppaalsmc::nsta_instantiation(instance):
    assert isinstance(instance, uppaalSMC::NSTA)
