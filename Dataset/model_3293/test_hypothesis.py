import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Edge,
    edges::PopulationEdge,
    LabelValue,
    edges::MixingEdgeLabelValue,
    edges::MigrationEdgeLabelValue,
    EdgeLabel,
    edges::MixingEdgeLabel,
    edges::MigrationEdgeLabel,
    PopulationEdge,
    edges::MixingEdge,
    edges::MigrationEdge,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_edges::populationedge_is_not_abstract():
    assert not inspect.isabstract(edges::PopulationEdge)


def test_edges::populationedge_constructor_exists():
    assert callable(edges::PopulationEdge.__init__)


def test_edges::populationedge_constructor_args():
    sig = inspect.signature(edges::PopulationEdge.__init__)
    params = list(sig.parameters.keys())
    assert "populationIdentifier" in params, "Missing parameter 'populationIdentifier'"

def test_edges::populationedge_has_populationIdentifier():
    assert hasattr(edges::PopulationEdge, "populationIdentifier")
    descriptor = None
    for klass in edges::PopulationEdge.__mro__:
        if "populationIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["populationIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_labelvalue_is_not_abstract():
    assert not inspect.isabstract(LabelValue)


def test_labelvalue_constructor_exists():
    assert callable(LabelValue.__init__)


def test_labelvalue_constructor_args():
    sig = inspect.signature(LabelValue.__init__)
    params = list(sig.parameters.keys())



def test_edges::mixingedgelabelvalue_is_not_abstract():
    assert not inspect.isabstract(edges::MixingEdgeLabelValue)


def test_edges::mixingedgelabelvalue_constructor_exists():
    assert callable(edges::MixingEdgeLabelValue.__init__)


def test_edges::mixingedgelabelvalue_constructor_args():
    sig = inspect.signature(edges::MixingEdgeLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "mixingRate" in params, "Missing parameter 'mixingRate'"

def test_edges::mixingedgelabelvalue_has_mixingRate():
    assert hasattr(edges::MixingEdgeLabelValue, "mixingRate")
    descriptor = None
    for klass in edges::MixingEdgeLabelValue.__mro__:
        if "mixingRate" in klass.__dict__:
            descriptor = klass.__dict__["mixingRate"]
            break
    assert isinstance(descriptor, property)



def test_edges::migrationedgelabelvalue_is_not_abstract():
    assert not inspect.isabstract(edges::MigrationEdgeLabelValue)


def test_edges::migrationedgelabelvalue_constructor_exists():
    assert callable(edges::MigrationEdgeLabelValue.__init__)


def test_edges::migrationedgelabelvalue_constructor_args():
    sig = inspect.signature(edges::MigrationEdgeLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "migrationRate" in params, "Missing parameter 'migrationRate'"

def test_edges::migrationedgelabelvalue_has_migrationRate():
    assert hasattr(edges::MigrationEdgeLabelValue, "migrationRate")
    descriptor = None
    for klass in edges::MigrationEdgeLabelValue.__mro__:
        if "migrationRate" in klass.__dict__:
            descriptor = klass.__dict__["migrationRate"]
            break
    assert isinstance(descriptor, property)



def test_edgelabel_is_not_abstract():
    assert not inspect.isabstract(EdgeLabel)


def test_edgelabel_constructor_exists():
    assert callable(EdgeLabel.__init__)


def test_edgelabel_constructor_args():
    sig = inspect.signature(EdgeLabel.__init__)
    params = list(sig.parameters.keys())



def test_edges::mixingedgelabel_is_not_abstract():
    assert not inspect.isabstract(edges::MixingEdgeLabel)


def test_edges::mixingedgelabel_constructor_exists():
    assert callable(edges::MixingEdgeLabel.__init__)


def test_edges::mixingedgelabel_constructor_args():
    sig = inspect.signature(edges::MixingEdgeLabel.__init__)
    params = list(sig.parameters.keys())



def test_edges::migrationedgelabel_is_not_abstract():
    assert not inspect.isabstract(edges::MigrationEdgeLabel)


def test_edges::migrationedgelabel_constructor_exists():
    assert callable(edges::MigrationEdgeLabel.__init__)


def test_edges::migrationedgelabel_constructor_args():
    sig = inspect.signature(edges::MigrationEdgeLabel.__init__)
    params = list(sig.parameters.keys())



def test_populationedge_is_not_abstract():
    assert not inspect.isabstract(PopulationEdge)


def test_populationedge_constructor_exists():
    assert callable(PopulationEdge.__init__)


def test_populationedge_constructor_args():
    sig = inspect.signature(PopulationEdge.__init__)
    params = list(sig.parameters.keys())



def test_edges::mixingedge_is_not_abstract():
    assert not inspect.isabstract(edges::MixingEdge)


def test_edges::mixingedge_constructor_exists():
    assert callable(edges::MixingEdge.__init__)


def test_edges::mixingedge_constructor_args():
    sig = inspect.signature(edges::MixingEdge.__init__)
    params = list(sig.parameters.keys())



def test_edges::migrationedge_is_not_abstract():
    assert not inspect.isabstract(edges::MigrationEdge)


def test_edges::migrationedge_constructor_exists():
    assert callable(edges::MigrationEdge.__init__)


def test_edges::migrationedge_constructor_args():
    sig = inspect.signature(edges::MigrationEdge.__init__)
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
Edge_strategy = st.builds(
    Edge,
)
edges::PopulationEdge_strategy = st.builds(
    edges::PopulationEdge,
    populationIdentifier=
        safe_text
)
LabelValue_strategy = st.builds(
    LabelValue,
)
edges::MixingEdgeLabelValue_strategy = st.builds(
    edges::MixingEdgeLabelValue,
    mixingRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
edges::MigrationEdgeLabelValue_strategy = st.builds(
    edges::MigrationEdgeLabelValue,
    migrationRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
EdgeLabel_strategy = st.builds(
    EdgeLabel,
)
edges::MixingEdgeLabel_strategy = st.builds(
    edges::MixingEdgeLabel,
)
edges::MigrationEdgeLabel_strategy = st.builds(
    edges::MigrationEdgeLabel,
)
PopulationEdge_strategy = st.builds(
    PopulationEdge,
)
edges::MixingEdge_strategy = st.builds(
    edges::MixingEdge,
)
edges::MigrationEdge_strategy = st.builds(
    edges::MigrationEdge,
)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=edges::PopulationEdge_strategy)
@settings(max_examples=50)
def test_edges::populationedge_instantiation(instance):
    assert isinstance(instance, edges::PopulationEdge)

@given(instance=edges::PopulationEdge_strategy)
def test_edges::populationedge_populationIdentifier_type(instance):
    assert isinstance(instance.populationIdentifier, str)


@given(instance=edges::PopulationEdge_strategy)
def test_edges::populationedge_populationIdentifier_setter(instance):
    original = instance.populationIdentifier
    instance.populationIdentifier = original
    assert instance.populationIdentifier == original

@given(instance=LabelValue_strategy)
@settings(max_examples=50)
def test_labelvalue_instantiation(instance):
    assert isinstance(instance, LabelValue)

@given(instance=edges::MixingEdgeLabelValue_strategy)
@settings(max_examples=50)
def test_edges::mixingedgelabelvalue_instantiation(instance):
    assert isinstance(instance, edges::MixingEdgeLabelValue)

@given(instance=edges::MixingEdgeLabelValue_strategy)
def test_edges::mixingedgelabelvalue_mixingRate_type(instance):
    assert isinstance(instance.mixingRate, float)


@given(instance=edges::MixingEdgeLabelValue_strategy)
def test_edges::mixingedgelabelvalue_mixingRate_setter(instance):
    original = instance.mixingRate
    instance.mixingRate = original
    assert instance.mixingRate == original

@given(instance=edges::MigrationEdgeLabelValue_strategy)
@settings(max_examples=50)
def test_edges::migrationedgelabelvalue_instantiation(instance):
    assert isinstance(instance, edges::MigrationEdgeLabelValue)

@given(instance=edges::MigrationEdgeLabelValue_strategy)
def test_edges::migrationedgelabelvalue_migrationRate_type(instance):
    assert isinstance(instance.migrationRate, float)


@given(instance=edges::MigrationEdgeLabelValue_strategy)
def test_edges::migrationedgelabelvalue_migrationRate_setter(instance):
    original = instance.migrationRate
    instance.migrationRate = original
    assert instance.migrationRate == original

@given(instance=EdgeLabel_strategy)
@settings(max_examples=50)
def test_edgelabel_instantiation(instance):
    assert isinstance(instance, EdgeLabel)

@given(instance=edges::MixingEdgeLabel_strategy)
@settings(max_examples=50)
def test_edges::mixingedgelabel_instantiation(instance):
    assert isinstance(instance, edges::MixingEdgeLabel)

@given(instance=edges::MigrationEdgeLabel_strategy)
@settings(max_examples=50)
def test_edges::migrationedgelabel_instantiation(instance):
    assert isinstance(instance, edges::MigrationEdgeLabel)

@given(instance=PopulationEdge_strategy)
@settings(max_examples=50)
def test_populationedge_instantiation(instance):
    assert isinstance(instance, PopulationEdge)

@given(instance=edges::MixingEdge_strategy)
@settings(max_examples=50)
def test_edges::mixingedge_instantiation(instance):
    assert isinstance(instance, edges::MixingEdge)

@given(instance=edges::MigrationEdge_strategy)
@settings(max_examples=50)
def test_edges::migrationedge_instantiation(instance):
    assert isinstance(instance, edges::MigrationEdge)
