import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    grammar_Graph,
    grammar_Node,
    grammar_ConnexionInstruction,
    grammar_Embedding,
    grammar_RHS,
    grammar_LHS,
    grammar_Rule,
    Named,
    grammar_Grammar,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grammar_graph_is_not_abstract():
    assert not inspect.isabstract(grammar_Graph)


def test_grammar_graph_constructor_exists():
    assert callable(grammar_Graph.__init__)


def test_grammar_graph_constructor_args():
    sig = inspect.signature(grammar_Graph.__init__)
    params = list(sig.parameters.keys())



def test_grammar_node_is_not_abstract():
    assert not inspect.isabstract(grammar_Node)


def test_grammar_node_constructor_exists():
    assert callable(grammar_Node.__init__)


def test_grammar_node_constructor_args():
    sig = inspect.signature(grammar_Node.__init__)
    params = list(sig.parameters.keys())



def test_grammar_connexioninstruction_is_not_abstract():
    assert not inspect.isabstract(grammar_ConnexionInstruction)


def test_grammar_connexioninstruction_constructor_exists():
    assert callable(grammar_ConnexionInstruction.__init__)


def test_grammar_connexioninstruction_constructor_args():
    sig = inspect.signature(grammar_ConnexionInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"

def test_grammar_connexioninstruction_has_m():
    assert hasattr(grammar_ConnexionInstruction, "m")
    descriptor = None
    for klass in grammar_ConnexionInstruction.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)



def test_grammar_embedding_is_not_abstract():
    assert not inspect.isabstract(grammar_Embedding)


def test_grammar_embedding_constructor_exists():
    assert callable(grammar_Embedding.__init__)


def test_grammar_embedding_constructor_args():
    sig = inspect.signature(grammar_Embedding.__init__)
    params = list(sig.parameters.keys())



def test_grammar_rhs_is_not_abstract():
    assert not inspect.isabstract(grammar_RHS)


def test_grammar_rhs_constructor_exists():
    assert callable(grammar_RHS.__init__)


def test_grammar_rhs_constructor_args():
    sig = inspect.signature(grammar_RHS.__init__)
    params = list(sig.parameters.keys())



def test_grammar_lhs_is_not_abstract():
    assert not inspect.isabstract(grammar_LHS)


def test_grammar_lhs_constructor_exists():
    assert callable(grammar_LHS.__init__)


def test_grammar_lhs_constructor_args():
    sig = inspect.signature(grammar_LHS.__init__)
    params = list(sig.parameters.keys())



def test_grammar_rule_is_not_abstract():
    assert not inspect.isabstract(grammar_Rule)


def test_grammar_rule_constructor_exists():
    assert callable(grammar_Rule.__init__)


def test_grammar_rule_constructor_args():
    sig = inspect.signature(grammar_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"

def test_grammar_rule_has_priority():
    assert hasattr(grammar_Rule, "priority")
    descriptor = None
    for klass in grammar_Rule.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_grammar_rule_has_name():
    assert hasattr(grammar_Rule, "name")
    descriptor = None
    for klass in grammar_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_grammar_grammar_is_not_abstract():
    assert not inspect.isabstract(grammar_Grammar)


def test_grammar_grammar_constructor_exists():
    assert callable(grammar_Grammar.__init__)


def test_grammar_grammar_constructor_args():
    sig = inspect.signature(grammar_Grammar.__init__)
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
grammar_Graph_strategy = st.builds(
    grammar_Graph,
)
grammar_Node_strategy = st.builds(
    grammar_Node,
)
grammar_ConnexionInstruction_strategy = st.builds(
    grammar_ConnexionInstruction,
    m=
        safe_text
)
grammar_Embedding_strategy = st.builds(
    grammar_Embedding,
)
grammar_RHS_strategy = st.builds(
    grammar_RHS,
)
grammar_LHS_strategy = st.builds(
    grammar_LHS,
)
grammar_Rule_strategy = st.builds(
    grammar_Rule,
    priority=
        st.integers(),
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
grammar_Grammar_strategy = st.builds(
    grammar_Grammar,
)

@given(instance=grammar_Graph_strategy)
@settings(max_examples=50)
def test_grammar_graph_instantiation(instance):
    assert isinstance(instance, grammar_Graph)

@given(instance=grammar_Node_strategy)
@settings(max_examples=50)
def test_grammar_node_instantiation(instance):
    assert isinstance(instance, grammar_Node)

@given(instance=grammar_ConnexionInstruction_strategy)
@settings(max_examples=50)
def test_grammar_connexioninstruction_instantiation(instance):
    assert isinstance(instance, grammar_ConnexionInstruction)



@given(instance=grammar_ConnexionInstruction_strategy)
def test_grammar_connexioninstruction_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

@given(instance=grammar_Embedding_strategy)
@settings(max_examples=50)
def test_grammar_embedding_instantiation(instance):
    assert isinstance(instance, grammar_Embedding)

@given(instance=grammar_RHS_strategy)
@settings(max_examples=50)
def test_grammar_rhs_instantiation(instance):
    assert isinstance(instance, grammar_RHS)

@given(instance=grammar_LHS_strategy)
@settings(max_examples=50)
def test_grammar_lhs_instantiation(instance):
    assert isinstance(instance, grammar_LHS)

@given(instance=grammar_Rule_strategy)
@settings(max_examples=50)
def test_grammar_rule_instantiation(instance):
    assert isinstance(instance, grammar_Rule)



@given(instance=grammar_Rule_strategy)
def test_grammar_rule_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=grammar_Rule_strategy)
def test_grammar_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=grammar_Grammar_strategy)
@settings(max_examples=50)
def test_grammar_grammar_instantiation(instance):
    assert isinstance(instance, grammar_Grammar)
