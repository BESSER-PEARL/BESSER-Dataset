import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    Edge,
    uppaalSMC_ChanceEdge,
    Location,
    uppaalSMC_ExponentialLocation,
    uppaalSMC_ChanceNode,
    Type,
    uppaalSMC_DoubleType,
    NTA,
    uppaalSMC_NSTA,
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



def test_uppaalsmc_chanceedge_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_ChanceEdge)


def test_uppaalsmc_chanceedge_constructor_exists():
    assert callable(uppaalSMC_ChanceEdge.__init__)


def test_uppaalsmc_chanceedge_constructor_args():
    sig = inspect.signature(uppaalSMC_ChanceEdge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_uppaalsmc_chanceedge_has_weight():
    assert hasattr(uppaalSMC_ChanceEdge, "weight")
    descriptor = None
    for klass in uppaalSMC_ChanceEdge.__mro__:
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



def test_uppaalsmc_exponentiallocation_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_ExponentialLocation)


def test_uppaalsmc_exponentiallocation_constructor_exists():
    assert callable(uppaalSMC_ExponentialLocation.__init__)


def test_uppaalsmc_exponentiallocation_constructor_args():
    sig = inspect.signature(uppaalSMC_ExponentialLocation.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc_chancenode_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_ChanceNode)


def test_uppaalsmc_chancenode_constructor_exists():
    assert callable(uppaalSMC_ChanceNode.__init__)


def test_uppaalsmc_chancenode_constructor_args():
    sig = inspect.signature(uppaalSMC_ChanceNode.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc_doubletype_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_DoubleType)


def test_uppaalsmc_doubletype_constructor_exists():
    assert callable(uppaalSMC_DoubleType.__init__)


def test_uppaalsmc_doubletype_constructor_args():
    sig = inspect.signature(uppaalSMC_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_nta_is_not_abstract():
    assert not inspect.isabstract(NTA)


def test_nta_constructor_exists():
    assert callable(NTA.__init__)


def test_nta_constructor_args():
    sig = inspect.signature(NTA.__init__)
    params = list(sig.parameters.keys())



def test_uppaalsmc_nsta_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_NSTA)


def test_uppaalsmc_nsta_constructor_exists():
    assert callable(uppaalSMC_NSTA.__init__)


def test_uppaalsmc_nsta_constructor_args():
    sig = inspect.signature(uppaalSMC_NSTA.__init__)
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
uppaalSMC_ChanceEdge_strategy = st.builds(
    uppaalSMC_ChanceEdge,
    weight=
        st.integers()
)
Location_strategy = st.builds(
    Location,
)
uppaalSMC_ExponentialLocation_strategy = st.builds(
    uppaalSMC_ExponentialLocation,
)
uppaalSMC_ChanceNode_strategy = st.builds(
    uppaalSMC_ChanceNode,
)
Type_strategy = st.builds(
    Type,
)
uppaalSMC_DoubleType_strategy = st.builds(
    uppaalSMC_DoubleType,
)
NTA_strategy = st.builds(
    NTA,
)
uppaalSMC_NSTA_strategy = st.builds(
    uppaalSMC_NSTA,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=uppaalSMC_ChanceEdge_strategy)
@settings(max_examples=50)
def test_uppaalsmc_chanceedge_instantiation(instance):
    assert isinstance(instance, uppaalSMC_ChanceEdge)



@given(instance=uppaalSMC_ChanceEdge_strategy)
def test_uppaalsmc_chanceedge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=uppaalSMC_ExponentialLocation_strategy)
@settings(max_examples=50)
def test_uppaalsmc_exponentiallocation_instantiation(instance):
    assert isinstance(instance, uppaalSMC_ExponentialLocation)

@given(instance=uppaalSMC_ChanceNode_strategy)
@settings(max_examples=50)
def test_uppaalsmc_chancenode_instantiation(instance):
    assert isinstance(instance, uppaalSMC_ChanceNode)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uppaalSMC_DoubleType_strategy)
@settings(max_examples=50)
def test_uppaalsmc_doubletype_instantiation(instance):
    assert isinstance(instance, uppaalSMC_DoubleType)

@given(instance=NTA_strategy)
@settings(max_examples=50)
def test_nta_instantiation(instance):
    assert isinstance(instance, NTA)

@given(instance=uppaalSMC_NSTA_strategy)
@settings(max_examples=50)
def test_uppaalsmc_nsta_instantiation(instance):
    assert isinstance(instance, uppaalSMC_NSTA)
