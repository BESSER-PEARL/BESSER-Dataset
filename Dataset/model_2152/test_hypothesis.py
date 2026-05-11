import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scaffolds::Vertex,
    scaffolds::Edge,
    scaffolds::Contig,
    scaffolds::ScaffoldGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scaffolds::vertex_is_not_abstract():
    assert not inspect.isabstract(scaffolds::Vertex)


def test_scaffolds::vertex_constructor_exists():
    assert callable(scaffolds::Vertex.__init__)


def test_scaffolds::vertex_constructor_args():
    sig = inspect.signature(scaffolds::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"

def test_scaffolds::vertex_has_num():
    assert hasattr(scaffolds::Vertex, "num")
    descriptor = None
    for klass in scaffolds::Vertex.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_scaffolds::edge_is_not_abstract():
    assert not inspect.isabstract(scaffolds::Edge)


def test_scaffolds::edge_constructor_exists():
    assert callable(scaffolds::Edge.__init__)


def test_scaffolds::edge_constructor_args():
    sig = inspect.signature(scaffolds::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_scaffolds::edge_has_weight():
    assert hasattr(scaffolds::Edge, "weight")
    descriptor = None
    for klass in scaffolds::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_scaffolds::edge_has_distance():
    assert hasattr(scaffolds::Edge, "distance")
    descriptor = None
    for klass in scaffolds::Edge.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_scaffolds::contig_is_not_abstract():
    assert not inspect.isabstract(scaffolds::Contig)


def test_scaffolds::contig_constructor_exists():
    assert callable(scaffolds::Contig.__init__)


def test_scaffolds::contig_constructor_args():
    sig = inspect.signature(scaffolds::Contig.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_scaffolds::contig_has_length():
    assert hasattr(scaffolds::Contig, "length")
    descriptor = None
    for klass in scaffolds::Contig.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_scaffolds::contig_has_multiplicity():
    assert hasattr(scaffolds::Contig, "multiplicity")
    descriptor = None
    for klass in scaffolds::Contig.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_scaffolds::scaffoldgraph_is_not_abstract():
    assert not inspect.isabstract(scaffolds::ScaffoldGraph)


def test_scaffolds::scaffoldgraph_constructor_exists():
    assert callable(scaffolds::ScaffoldGraph.__init__)


def test_scaffolds::scaffoldgraph_constructor_args():
    sig = inspect.signature(scaffolds::ScaffoldGraph.__init__)
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
scaffolds::Vertex_strategy = st.builds(
    scaffolds::Vertex,
    num=
        st.integers()
)
scaffolds::Edge_strategy = st.builds(
    scaffolds::Edge,
    weight=
        st.integers(),
    distance=
        st.integers()
)
scaffolds::Contig_strategy = st.builds(
    scaffolds::Contig,
    length=
        st.integers(),
    multiplicity=
        st.integers()
)
scaffolds::ScaffoldGraph_strategy = st.builds(
    scaffolds::ScaffoldGraph,
)

@given(instance=scaffolds::Vertex_strategy)
@settings(max_examples=50)
def test_scaffolds::vertex_instantiation(instance):
    assert isinstance(instance, scaffolds::Vertex)

@given(instance=scaffolds::Vertex_strategy)
def test_scaffolds::vertex_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=scaffolds::Vertex_strategy)
def test_scaffolds::vertex_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=scaffolds::Edge_strategy)
@settings(max_examples=50)
def test_scaffolds::edge_instantiation(instance):
    assert isinstance(instance, scaffolds::Edge)

@given(instance=scaffolds::Edge_strategy)
def test_scaffolds::edge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=scaffolds::Edge_strategy)
def test_scaffolds::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=scaffolds::Edge_strategy)
def test_scaffolds::edge_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=scaffolds::Edge_strategy)
def test_scaffolds::edge_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=scaffolds::Contig_strategy)
@settings(max_examples=50)
def test_scaffolds::contig_instantiation(instance):
    assert isinstance(instance, scaffolds::Contig)

@given(instance=scaffolds::Contig_strategy)
def test_scaffolds::contig_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=scaffolds::Contig_strategy)
def test_scaffolds::contig_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=scaffolds::Contig_strategy)
def test_scaffolds::contig_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, int)


@given(instance=scaffolds::Contig_strategy)
def test_scaffolds::contig_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=scaffolds::ScaffoldGraph_strategy)
@settings(max_examples=50)
def test_scaffolds::scaffoldgraph_instantiation(instance):
    assert isinstance(instance, scaffolds::ScaffoldGraph)
