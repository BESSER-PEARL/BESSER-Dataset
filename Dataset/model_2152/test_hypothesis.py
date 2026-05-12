import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scaffolds_Vertex,
    scaffolds_Edge,
    scaffolds_Contig,
    scaffolds_ScaffoldGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scaffolds_vertex_is_not_abstract():
    assert not inspect.isabstract(scaffolds_Vertex)


def test_scaffolds_vertex_constructor_exists():
    assert callable(scaffolds_Vertex.__init__)


def test_scaffolds_vertex_constructor_args():
    sig = inspect.signature(scaffolds_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"

def test_scaffolds_vertex_has_num():
    assert hasattr(scaffolds_Vertex, "num")
    descriptor = None
    for klass in scaffolds_Vertex.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_scaffolds_edge_is_not_abstract():
    assert not inspect.isabstract(scaffolds_Edge)


def test_scaffolds_edge_constructor_exists():
    assert callable(scaffolds_Edge.__init__)


def test_scaffolds_edge_constructor_args():
    sig = inspect.signature(scaffolds_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_scaffolds_edge_has_distance():
    assert hasattr(scaffolds_Edge, "distance")
    descriptor = None
    for klass in scaffolds_Edge.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_scaffolds_edge_has_weight():
    assert hasattr(scaffolds_Edge, "weight")
    descriptor = None
    for klass in scaffolds_Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_scaffolds_contig_is_not_abstract():
    assert not inspect.isabstract(scaffolds_Contig)


def test_scaffolds_contig_constructor_exists():
    assert callable(scaffolds_Contig.__init__)


def test_scaffolds_contig_constructor_args():
    sig = inspect.signature(scaffolds_Contig.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "length" in params, "Missing parameter 'length'"

def test_scaffolds_contig_has_multiplicity():
    assert hasattr(scaffolds_Contig, "multiplicity")
    descriptor = None
    for klass in scaffolds_Contig.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_scaffolds_contig_has_length():
    assert hasattr(scaffolds_Contig, "length")
    descriptor = None
    for klass in scaffolds_Contig.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_scaffolds_scaffoldgraph_is_not_abstract():
    assert not inspect.isabstract(scaffolds_ScaffoldGraph)


def test_scaffolds_scaffoldgraph_constructor_exists():
    assert callable(scaffolds_ScaffoldGraph.__init__)


def test_scaffolds_scaffoldgraph_constructor_args():
    sig = inspect.signature(scaffolds_ScaffoldGraph.__init__)
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
scaffolds_Vertex_strategy = st.builds(
    scaffolds_Vertex,
    num=
        st.integers()
)
scaffolds_Edge_strategy = st.builds(
    scaffolds_Edge,
    distance=
        st.integers(),
    weight=
        st.integers()
)
scaffolds_Contig_strategy = st.builds(
    scaffolds_Contig,
    multiplicity=
        st.integers(),
    length=
        st.integers()
)
scaffolds_ScaffoldGraph_strategy = st.builds(
    scaffolds_ScaffoldGraph,
)

@given(instance=scaffolds_Vertex_strategy)
@settings(max_examples=50)
def test_scaffolds_vertex_instantiation(instance):
    assert isinstance(instance, scaffolds_Vertex)



@given(instance=scaffolds_Vertex_strategy)
def test_scaffolds_vertex_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=scaffolds_Edge_strategy)
@settings(max_examples=50)
def test_scaffolds_edge_instantiation(instance):
    assert isinstance(instance, scaffolds_Edge)



@given(instance=scaffolds_Edge_strategy)
def test_scaffolds_edge_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=scaffolds_Edge_strategy)
def test_scaffolds_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=scaffolds_Contig_strategy)
@settings(max_examples=50)
def test_scaffolds_contig_instantiation(instance):
    assert isinstance(instance, scaffolds_Contig)



@given(instance=scaffolds_Contig_strategy)
def test_scaffolds_contig_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original



@given(instance=scaffolds_Contig_strategy)
def test_scaffolds_contig_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=scaffolds_ScaffoldGraph_strategy)
@settings(max_examples=50)
def test_scaffolds_scaffoldgraph_instantiation(instance):
    assert isinstance(instance, scaffolds_ScaffoldGraph)
