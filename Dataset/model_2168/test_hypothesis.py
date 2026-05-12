import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_ResourcePlot,
    graph_ResourceGraph,
    graph_ResourceGraphs,
    FitPolicy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_resourceplot_is_not_abstract():
    assert not inspect.isabstract(graph_ResourcePlot)


def test_graph_resourceplot_constructor_exists():
    assert callable(graph_ResourcePlot.__init__)


def test_graph_resourceplot_constructor_args():
    sig = inspect.signature(graph_ResourcePlot.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "fit" in params, "Missing parameter 'fit'"
    assert "min" in params, "Missing parameter 'min'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rgb" in params, "Missing parameter 'rgb'"

def test_graph_resourceplot_has_max():
    assert hasattr(graph_ResourcePlot, "max")
    descriptor = None
    for klass in graph_ResourcePlot.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_graph_resourceplot_has_fit():
    assert hasattr(graph_ResourcePlot, "fit")
    descriptor = None
    for klass in graph_ResourcePlot.__mro__:
        if "fit" in klass.__dict__:
            descriptor = klass.__dict__["fit"]
            break
    assert isinstance(descriptor, property)

def test_graph_resourceplot_has_min():
    assert hasattr(graph_ResourcePlot, "min")
    descriptor = None
    for klass in graph_ResourcePlot.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_graph_resourceplot_has_name():
    assert hasattr(graph_ResourcePlot, "name")
    descriptor = None
    for klass in graph_ResourcePlot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graph_resourceplot_has_rgb():
    assert hasattr(graph_ResourcePlot, "rgb")
    descriptor = None
    for klass in graph_ResourcePlot.__mro__:
        if "rgb" in klass.__dict__:
            descriptor = klass.__dict__["rgb"]
            break
    assert isinstance(descriptor, property)



def test_graph_resourcegraph_is_not_abstract():
    assert not inspect.isabstract(graph_ResourceGraph)


def test_graph_resourcegraph_constructor_exists():
    assert callable(graph_ResourceGraph.__init__)


def test_graph_resourcegraph_constructor_args():
    sig = inspect.signature(graph_ResourceGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_resourcegraph_has_name():
    assert hasattr(graph_ResourceGraph, "name")
    descriptor = None
    for klass in graph_ResourceGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_resourcegraphs_is_not_abstract():
    assert not inspect.isabstract(graph_ResourceGraphs)


def test_graph_resourcegraphs_constructor_exists():
    assert callable(graph_ResourceGraphs.__init__)


def test_graph_resourcegraphs_constructor_args():
    sig = inspect.signature(graph_ResourceGraphs.__init__)
    params = list(sig.parameters.keys())

def test_fitpolicy_exists():
    # Check that the Enumeration exists
    assert FitPolicy is not None

def test_fitpolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FitPolicy]
    expected_literals = [
        "CUSTOM",
        "AUTO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FitPolicy"


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
graph_ResourcePlot_strategy = st.builds(
    graph_ResourcePlot,
    max=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fit=
        safe_text,
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    rgb=
        safe_text
)
graph_ResourceGraph_strategy = st.builds(
    graph_ResourceGraph,
    name=
        safe_text
)
graph_ResourceGraphs_strategy = st.builds(
    graph_ResourceGraphs,
)

@given(instance=graph_ResourcePlot_strategy)
@settings(max_examples=50)
def test_graph_resourceplot_instantiation(instance):
    assert isinstance(instance, graph_ResourcePlot)



@given(instance=graph_ResourcePlot_strategy)
def test_graph_resourceplot_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=graph_ResourcePlot_strategy)
def test_graph_resourceplot_fit_setter(instance):
    original = instance.fit
    instance.fit = original
    assert instance.fit == original



@given(instance=graph_ResourcePlot_strategy)
def test_graph_resourceplot_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=graph_ResourcePlot_strategy)
def test_graph_resourceplot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graph_ResourcePlot_strategy)
def test_graph_resourceplot_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original

@given(instance=graph_ResourceGraph_strategy)
@settings(max_examples=50)
def test_graph_resourcegraph_instantiation(instance):
    assert isinstance(instance, graph_ResourceGraph)



@given(instance=graph_ResourceGraph_strategy)
def test_graph_resourcegraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_ResourceGraphs_strategy)
@settings(max_examples=50)
def test_graph_resourcegraphs_instantiation(instance):
    assert isinstance(instance, graph_ResourceGraphs)
