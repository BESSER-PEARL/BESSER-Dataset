import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StatementVertex,
    cfgraph_CallVertex,
    cfgraph_SimpleStatementVertex,
    ControlFlowVertex,
    cfgraph_ControlFlowVertex,
    cfgraph_BodyVertex,
    cfgraph_ControlFlowEdge,
    cfgraph_StartVertex,
    cfgraph_ControlFlowGraph,
    BodyVertex,
    cfgraph_BranchingVertex,
    cfgraph_StatementVertex,
    cfgraph_EndVertex,
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



def test_cfgraph_callvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_CallVertex)


def test_cfgraph_callvertex_constructor_exists():
    assert callable(cfgraph_CallVertex.__init__)


def test_cfgraph_callvertex_constructor_args():
    sig = inspect.signature(cfgraph_CallVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_simplestatementvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_SimpleStatementVertex)


def test_cfgraph_simplestatementvertex_constructor_exists():
    assert callable(cfgraph_SimpleStatementVertex.__init__)


def test_cfgraph_simplestatementvertex_constructor_args():
    sig = inspect.signature(cfgraph_SimpleStatementVertex.__init__)
    params = list(sig.parameters.keys())



def test_controlflowvertex_is_not_abstract():
    assert not inspect.isabstract(ControlFlowVertex)


def test_controlflowvertex_constructor_exists():
    assert callable(ControlFlowVertex.__init__)


def test_controlflowvertex_constructor_args():
    sig = inspect.signature(ControlFlowVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_controlflowvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_ControlFlowVertex)


def test_cfgraph_controlflowvertex_constructor_exists():
    assert callable(cfgraph_ControlFlowVertex.__init__)


def test_cfgraph_controlflowvertex_constructor_args():
    sig = inspect.signature(cfgraph_ControlFlowVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_bodyvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_BodyVertex)


def test_cfgraph_bodyvertex_constructor_exists():
    assert callable(cfgraph_BodyVertex.__init__)


def test_cfgraph_bodyvertex_constructor_args():
    sig = inspect.signature(cfgraph_BodyVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_controlflowedge_is_not_abstract():
    assert not inspect.isabstract(cfgraph_ControlFlowEdge)


def test_cfgraph_controlflowedge_constructor_exists():
    assert callable(cfgraph_ControlFlowEdge.__init__)


def test_cfgraph_controlflowedge_constructor_args():
    sig = inspect.signature(cfgraph_ControlFlowEdge.__init__)
    params = list(sig.parameters.keys())
    assert "backward" in params, "Missing parameter 'backward'"

def test_cfgraph_controlflowedge_has_backward():
    assert hasattr(cfgraph_ControlFlowEdge, "backward")
    descriptor = None
    for klass in cfgraph_ControlFlowEdge.__mro__:
        if "backward" in klass.__dict__:
            descriptor = klass.__dict__["backward"]
            break
    assert isinstance(descriptor, property)



def test_cfgraph_startvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_StartVertex)


def test_cfgraph_startvertex_constructor_exists():
    assert callable(cfgraph_StartVertex.__init__)


def test_cfgraph_startvertex_constructor_args():
    sig = inspect.signature(cfgraph_StartVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_controlflowgraph_is_not_abstract():
    assert not inspect.isabstract(cfgraph_ControlFlowGraph)


def test_cfgraph_controlflowgraph_constructor_exists():
    assert callable(cfgraph_ControlFlowGraph.__init__)


def test_cfgraph_controlflowgraph_constructor_args():
    sig = inspect.signature(cfgraph_ControlFlowGraph.__init__)
    params = list(sig.parameters.keys())



def test_bodyvertex_is_not_abstract():
    assert not inspect.isabstract(BodyVertex)


def test_bodyvertex_constructor_exists():
    assert callable(BodyVertex.__init__)


def test_bodyvertex_constructor_args():
    sig = inspect.signature(BodyVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_branchingvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_BranchingVertex)


def test_cfgraph_branchingvertex_constructor_exists():
    assert callable(cfgraph_BranchingVertex.__init__)


def test_cfgraph_branchingvertex_constructor_args():
    sig = inspect.signature(cfgraph_BranchingVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_statementvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_StatementVertex)


def test_cfgraph_statementvertex_constructor_exists():
    assert callable(cfgraph_StatementVertex.__init__)


def test_cfgraph_statementvertex_constructor_args():
    sig = inspect.signature(cfgraph_StatementVertex.__init__)
    params = list(sig.parameters.keys())



def test_cfgraph_endvertex_is_not_abstract():
    assert not inspect.isabstract(cfgraph_EndVertex)


def test_cfgraph_endvertex_constructor_exists():
    assert callable(cfgraph_EndVertex.__init__)


def test_cfgraph_endvertex_constructor_args():
    sig = inspect.signature(cfgraph_EndVertex.__init__)
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
cfgraph_CallVertex_strategy = st.builds(
    cfgraph_CallVertex,
)
cfgraph_SimpleStatementVertex_strategy = st.builds(
    cfgraph_SimpleStatementVertex,
)
ControlFlowVertex_strategy = st.builds(
    ControlFlowVertex,
)
cfgraph_ControlFlowVertex_strategy = st.builds(
    cfgraph_ControlFlowVertex,
)
cfgraph_BodyVertex_strategy = st.builds(
    cfgraph_BodyVertex,
)
cfgraph_ControlFlowEdge_strategy = st.builds(
    cfgraph_ControlFlowEdge,
    backward=
        st.booleans()
)
cfgraph_StartVertex_strategy = st.builds(
    cfgraph_StartVertex,
)
cfgraph_ControlFlowGraph_strategy = st.builds(
    cfgraph_ControlFlowGraph,
)
BodyVertex_strategy = st.builds(
    BodyVertex,
)
cfgraph_BranchingVertex_strategy = st.builds(
    cfgraph_BranchingVertex,
)
cfgraph_StatementVertex_strategy = st.builds(
    cfgraph_StatementVertex,
)
cfgraph_EndVertex_strategy = st.builds(
    cfgraph_EndVertex,
)

@given(instance=StatementVertex_strategy)
@settings(max_examples=50)
def test_statementvertex_instantiation(instance):
    assert isinstance(instance, StatementVertex)

@given(instance=cfgraph_CallVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_callvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_CallVertex)

@given(instance=cfgraph_SimpleStatementVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_simplestatementvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_SimpleStatementVertex)

@given(instance=ControlFlowVertex_strategy)
@settings(max_examples=50)
def test_controlflowvertex_instantiation(instance):
    assert isinstance(instance, ControlFlowVertex)

@given(instance=cfgraph_ControlFlowVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_controlflowvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_ControlFlowVertex)

@given(instance=cfgraph_BodyVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_bodyvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_BodyVertex)

@given(instance=cfgraph_ControlFlowEdge_strategy)
@settings(max_examples=50)
def test_cfgraph_controlflowedge_instantiation(instance):
    assert isinstance(instance, cfgraph_ControlFlowEdge)



@given(instance=cfgraph_ControlFlowEdge_strategy)
def test_cfgraph_controlflowedge_backward_setter(instance):
    original = instance.backward
    instance.backward = original
    assert instance.backward == original

@given(instance=cfgraph_StartVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_startvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_StartVertex)

@given(instance=cfgraph_ControlFlowGraph_strategy)
@settings(max_examples=50)
def test_cfgraph_controlflowgraph_instantiation(instance):
    assert isinstance(instance, cfgraph_ControlFlowGraph)

@given(instance=BodyVertex_strategy)
@settings(max_examples=50)
def test_bodyvertex_instantiation(instance):
    assert isinstance(instance, BodyVertex)

@given(instance=cfgraph_BranchingVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_branchingvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_BranchingVertex)

@given(instance=cfgraph_StatementVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_statementvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_StatementVertex)

@given(instance=cfgraph_EndVertex_strategy)
@settings(max_examples=50)
def test_cfgraph_endvertex_instantiation(instance):
    assert isinstance(instance, cfgraph_EndVertex)
