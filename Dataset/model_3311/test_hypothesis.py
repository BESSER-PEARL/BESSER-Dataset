import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    grammar::Graph,
    grammar::Node,
    grammar::ConnexionInstruction,
    grammar::Embedding,
    grammar::RHS,
    grammar::LHS,
    grammar::Rule,
    Named,
    grammar::Grammar,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grammar::graph_is_not_abstract():
    assert not inspect.isabstract(grammar::Graph)


def test_grammar::graph_constructor_exists():
    assert callable(grammar::Graph.__init__)


def test_grammar::graph_constructor_args():
    sig = inspect.signature(grammar::Graph.__init__)
    params = list(sig.parameters.keys())



def test_grammar::node_is_not_abstract():
    assert not inspect.isabstract(grammar::Node)


def test_grammar::node_constructor_exists():
    assert callable(grammar::Node.__init__)


def test_grammar::node_constructor_args():
    sig = inspect.signature(grammar::Node.__init__)
    params = list(sig.parameters.keys())



def test_grammar::connexioninstruction_is_not_abstract():
    assert not inspect.isabstract(grammar::ConnexionInstruction)


def test_grammar::connexioninstruction_constructor_exists():
    assert callable(grammar::ConnexionInstruction.__init__)


def test_grammar::connexioninstruction_constructor_args():
    sig = inspect.signature(grammar::ConnexionInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"

def test_grammar::connexioninstruction_has_m():
    assert hasattr(grammar::ConnexionInstruction, "m")
    descriptor = None
    for klass in grammar::ConnexionInstruction.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)



def test_grammar::embedding_is_not_abstract():
    assert not inspect.isabstract(grammar::Embedding)


def test_grammar::embedding_constructor_exists():
    assert callable(grammar::Embedding.__init__)


def test_grammar::embedding_constructor_args():
    sig = inspect.signature(grammar::Embedding.__init__)
    params = list(sig.parameters.keys())



def test_grammar::rhs_is_not_abstract():
    assert not inspect.isabstract(grammar::RHS)


def test_grammar::rhs_constructor_exists():
    assert callable(grammar::RHS.__init__)


def test_grammar::rhs_constructor_args():
    sig = inspect.signature(grammar::RHS.__init__)
    params = list(sig.parameters.keys())



def test_grammar::lhs_is_not_abstract():
    assert not inspect.isabstract(grammar::LHS)


def test_grammar::lhs_constructor_exists():
    assert callable(grammar::LHS.__init__)


def test_grammar::lhs_constructor_args():
    sig = inspect.signature(grammar::LHS.__init__)
    params = list(sig.parameters.keys())



def test_grammar::rule_is_not_abstract():
    assert not inspect.isabstract(grammar::Rule)


def test_grammar::rule_constructor_exists():
    assert callable(grammar::Rule.__init__)


def test_grammar::rule_constructor_args():
    sig = inspect.signature(grammar::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"

def test_grammar::rule_has_priority():
    assert hasattr(grammar::Rule, "priority")
    descriptor = None
    for klass in grammar::Rule.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_grammar::rule_has_name():
    assert hasattr(grammar::Rule, "name")
    descriptor = None
    for klass in grammar::Rule.__mro__:
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



def test_grammar::grammar_is_not_abstract():
    assert not inspect.isabstract(grammar::Grammar)


def test_grammar::grammar_constructor_exists():
    assert callable(grammar::Grammar.__init__)


def test_grammar::grammar_constructor_args():
    sig = inspect.signature(grammar::Grammar.__init__)
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
grammar::Graph_strategy = st.builds(
    grammar::Graph,
)
grammar::Node_strategy = st.builds(
    grammar::Node,
)
grammar::ConnexionInstruction_strategy = st.builds(
    grammar::ConnexionInstruction,
    m=
        safe_text
)
grammar::Embedding_strategy = st.builds(
    grammar::Embedding,
)
grammar::RHS_strategy = st.builds(
    grammar::RHS,
)
grammar::LHS_strategy = st.builds(
    grammar::LHS,
)
grammar::Rule_strategy = st.builds(
    grammar::Rule,
    priority=
        st.integers(),
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
grammar::Grammar_strategy = st.builds(
    grammar::Grammar,
)

@given(instance=grammar::Graph_strategy)
@settings(max_examples=50)
def test_grammar::graph_instantiation(instance):
    assert isinstance(instance, grammar::Graph)

@given(instance=grammar::Node_strategy)
@settings(max_examples=50)
def test_grammar::node_instantiation(instance):
    assert isinstance(instance, grammar::Node)

@given(instance=grammar::ConnexionInstruction_strategy)
@settings(max_examples=50)
def test_grammar::connexioninstruction_instantiation(instance):
    assert isinstance(instance, grammar::ConnexionInstruction)

@given(instance=grammar::ConnexionInstruction_strategy)
def test_grammar::connexioninstruction_m_type(instance):
    assert isinstance(instance.m, str)


@given(instance=grammar::ConnexionInstruction_strategy)
def test_grammar::connexioninstruction_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

@given(instance=grammar::Embedding_strategy)
@settings(max_examples=50)
def test_grammar::embedding_instantiation(instance):
    assert isinstance(instance, grammar::Embedding)

@given(instance=grammar::RHS_strategy)
@settings(max_examples=50)
def test_grammar::rhs_instantiation(instance):
    assert isinstance(instance, grammar::RHS)

@given(instance=grammar::LHS_strategy)
@settings(max_examples=50)
def test_grammar::lhs_instantiation(instance):
    assert isinstance(instance, grammar::LHS)

@given(instance=grammar::Rule_strategy)
@settings(max_examples=50)
def test_grammar::rule_instantiation(instance):
    assert isinstance(instance, grammar::Rule)

@given(instance=grammar::Rule_strategy)
def test_grammar::rule_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=grammar::Rule_strategy)
def test_grammar::rule_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=grammar::Rule_strategy)
def test_grammar::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=grammar::Rule_strategy)
def test_grammar::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=grammar::Grammar_strategy)
@settings(max_examples=50)
def test_grammar::grammar_instantiation(instance):
    assert isinstance(instance, grammar::Grammar)
