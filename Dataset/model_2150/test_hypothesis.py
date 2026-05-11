import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StatementVertex,
    cfgraph::CallVertex,
    cfgraph::SimpleStatementVertex,
    ControlFlowVertex,
    cfgraph::ControlFlowVertex,
    cfgraph::BodyVertex,
    cfgraph::ControlFlowEdge,
    cfgraph::StartVertex,
    cfgraph::ControlFlowGraph,
    BodyVertex,
    cfgraph::StatementVertex,
    cfgraph::BranchingVertex,
    cfgraph::EndVertex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statementvertex_is_not_abstract():
    assert not inspect.isabstract(StatementVertex)


def test_statementvertex_constructor_exists():
    assert callable(StatementVertex.__init__)


def test_statementvertex_constructor_args():
    sig = inspect.signature(StatementVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::callvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::CallVertex)


def test_cfgraph::callvertex_constructor_exists():
    assert callable(cfgraph::CallVertex.__init__)


def test_cfgraph::callvertex_constructor_args():
    sig = inspect.signature(cfgraph::CallVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::simplestatementvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::SimpleStatementVertex)


def test_cfgraph::simplestatementvertex_constructor_exists():
    assert callable(cfgraph::SimpleStatementVertex.__init__)


def test_cfgraph::simplestatementvertex_constructor_args():
    sig = inspect.signature(cfgraph::SimpleStatementVertex.__init__)
    params = list(sig.parameters.keys())



def test_controlflowvertex_is_not_abstract():
    assert not inspect.isabstract(ControlFlowVertex)


def test_controlflowvertex_constructor_exists():
    assert callable(ControlFlowVertex.__init__)


def test_controlflowvertex_constructor_args():
    sig = inspect.signature(ControlFlowVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::controlflowvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::ControlFlowVertex)


def test_cfgraph::controlflowvertex_constructor_exists():
    assert callable(cfgraph::ControlFlowVertex.__init__)


def test_cfgraph::controlflowvertex_constructor_args():
    sig = inspect.signature(cfgraph::ControlFlowVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::bodyvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::BodyVertex)


def test_cfgraph::bodyvertex_constructor_exists():
    assert callable(cfgraph::BodyVertex.__init__)


def test_cfgraph::bodyvertex_constructor_args():
    sig = inspect.signature(cfgraph::BodyVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::controlflowedge_is_not_abstract():
    assert not inspect.isabstract(cfgraph::ControlFlowEdge)


def test_cfgraph::controlflowedge_constructor_exists():
    assert callable(cfgraph::ControlFlowEdge.__init__)


def test_cfgraph::controlflowedge_constructor_args():
    sig = inspect.signature(cfgraph::ControlFlowEdge.__init__)
    params = list(sig.parameters.keys())
    assert "backward" in params, "Missing parameter 'backward'"

def test_cfgraph::controlflowedge_has_backward():
    assert hasattr(cfgraph::ControlFlowEdge, "backward")
    descriptor = None
    for klass in cfgraph::ControlFlowEdge.__mro__:
        if "backward" in klass.__dict__:
            descriptor = klass.__dict__["backward"]
            break
    assert isinstance(descriptor, property)



def test_cfgraph::startvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::StartVertex)


def test_cfgraph::startvertex_constructor_exists():
    assert callable(cfgraph::StartVertex.__init__)


def test_cfgraph::startvertex_constructor_args():
    sig = inspect.signature(cfgraph::StartVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::controlflowgraph_is_not_abstract():
    assert not inspect.isabstract(cfgraph::ControlFlowGraph)


def test_cfgraph::controlflowgraph_constructor_exists():
    assert callable(cfgraph::ControlFlowGraph.__init__)


def test_cfgraph::controlflowgraph_constructor_args():
    sig = inspect.signature(cfgraph::ControlFlowGraph.__init__)
    params = list(sig.parameters.keys())



def test_bodyvertex_is_not_abstract():
    assert not inspect.isabstract(BodyVertex)


def test_bodyvertex_constructor_exists():
    assert callable(BodyVertex.__init__)


def test_bodyvertex_constructor_args():
    sig = inspect.signature(BodyVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::statementvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::StatementVertex)


def test_cfgraph::statementvertex_constructor_exists():
    assert callable(cfgraph::StatementVertex.__init__)


def test_cfgraph::statementvertex_constructor_args():
    sig = inspect.signature(cfgraph::StatementVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::branchingvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::BranchingVertex)


def test_cfgraph::branchingvertex_constructor_exists():
    assert callable(cfgraph::BranchingVertex.__init__)


def test_cfgraph::branchingvertex_constructor_args():
    sig = inspect.signature(cfgraph::BranchingVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph::endvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph::EndVertex)


def test_cfgraph::endvertex_constructor_exists():
    assert callable(cfgraph::EndVertex.__init__)


def test_cfgraph::endvertex_constructor_args():
    sig = inspect.signature(cfgraph::EndVertex.__init__)
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
StatementVertex_strategy = st.builds(
    StatementVertex,
)
cfgraph::CallVertex_strategy = st.builds(
    cfgraph::CallVertex,
)
cfgraph::SimpleStatementVertex_strategy = st.builds(
    cfgraph::SimpleStatementVertex,
)
ControlFlowVertex_strategy = st.builds(
    ControlFlowVertex,
)
cfgraph::ControlFlowVertex_strategy = st.builds(
    cfgraph::ControlFlowVertex,
)
cfgraph::BodyVertex_strategy = st.builds(
    cfgraph::BodyVertex,
)
cfgraph::ControlFlowEdge_strategy = st.builds(
    cfgraph::ControlFlowEdge,
    backward=
        st.booleans()
)
cfgraph::StartVertex_strategy = st.builds(
    cfgraph::StartVertex,
)
cfgraph::ControlFlowGraph_strategy = st.builds(
    cfgraph::ControlFlowGraph,
)
BodyVertex_strategy = st.builds(
    BodyVertex,
)
cfgraph::StatementVertex_strategy = st.builds(
    cfgraph::StatementVertex,
)
cfgraph::BranchingVertex_strategy = st.builds(
    cfgraph::BranchingVertex,
)
cfgraph::EndVertex_strategy = st.builds(
    cfgraph::EndVertex,
)

@given(instance=StatementVertex_strategy)
@settings(max_examples=50)
def test_statementvertex_instantiation(instance):
    assert isinstance(instance, StatementVertex)

@given(instance=cfgraph::CallVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::callvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::CallVertex)

@given(instance=cfgraph::SimpleStatementVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::simplestatementvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::SimpleStatementVertex)

@given(instance=ControlFlowVertex_strategy)
@settings(max_examples=50)
def test_controlflowvertex_instantiation(instance):
    assert isinstance(instance, ControlFlowVertex)

@given(instance=cfgraph::ControlFlowVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::controlflowvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::ControlFlowVertex)

@given(instance=cfgraph::BodyVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::bodyvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::BodyVertex)

@given(instance=cfgraph::ControlFlowEdge_strategy)
@settings(max_examples=50)
def test_cfgraph::controlflowedge_instantiation(instance):
    assert isinstance(instance, cfgraph::ControlFlowEdge)

@given(instance=cfgraph::ControlFlowEdge_strategy)
def test_cfgraph::controlflowedge_backward_type(instance):
    assert isinstance(instance.backward, bool)


@given(instance=cfgraph::ControlFlowEdge_strategy)
def test_cfgraph::controlflowedge_backward_setter(instance):
    original = instance.backward
    instance.backward = original
    assert instance.backward == original

@given(instance=cfgraph::StartVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::startvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::StartVertex)

@given(instance=cfgraph::ControlFlowGraph_strategy)
@settings(max_examples=50)
def test_cfgraph::controlflowgraph_instantiation(instance):
    assert isinstance(instance, cfgraph::ControlFlowGraph)

@given(instance=BodyVertex_strategy)
@settings(max_examples=50)
def test_bodyvertex_instantiation(instance):
    assert isinstance(instance, BodyVertex)

@given(instance=cfgraph::StatementVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::statementvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::StatementVertex)

@given(instance=cfgraph::BranchingVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::branchingvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::BranchingVertex)

@given(instance=cfgraph::EndVertex_strategy)
@settings(max_examples=50)
def test_cfgraph::endvertex_instantiation(instance):
    assert isinstance(instance, cfgraph::EndVertex)
