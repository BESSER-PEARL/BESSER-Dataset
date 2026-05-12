import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rules_NodeRelation,
    rules_Node,
    rules_Rule,
    rules_RulesLattice,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rules_noderelation_is_not_abstract():
    assert not inspect.isabstract(rules_NodeRelation)


def test_rules_noderelation_constructor_exists():
    assert callable(rules_NodeRelation.__init__)


def test_rules_noderelation_constructor_args():
    sig = inspect.signature(rules_NodeRelation.__init__)
    params = list(sig.parameters.keys())
    assert "relationTgt" in params, "Missing parameter 'relationTgt'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "relation" in params, "Missing parameter 'relation'"

def test_rules_noderelation_has_relationTgt():
    assert hasattr(rules_NodeRelation, "relationTgt")
    descriptor = None
    for klass in rules_NodeRelation.__mro__:
        if "relationTgt" in klass.__dict__:
            descriptor = klass.__dict__["relationTgt"]
            break
    assert isinstance(descriptor, property)

def test_rules_noderelation_has_upperBound():
    assert hasattr(rules_NodeRelation, "upperBound")
    descriptor = None
    for klass in rules_NodeRelation.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_rules_noderelation_has_lowerBound():
    assert hasattr(rules_NodeRelation, "lowerBound")
    descriptor = None
    for klass in rules_NodeRelation.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_rules_noderelation_has_relation():
    assert hasattr(rules_NodeRelation, "relation")
    descriptor = None
    for klass in rules_NodeRelation.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_rules_node_is_not_abstract():
    assert not inspect.isabstract(rules_Node)


def test_rules_node_constructor_exists():
    assert callable(rules_Node.__init__)


def test_rules_node_constructor_args():
    sig = inspect.signature(rules_Node.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rules_node_has_type():
    assert hasattr(rules_Node, "type")
    descriptor = None
    for klass in rules_Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rules_rule_is_not_abstract():
    assert not inspect.isabstract(rules_Rule)


def test_rules_rule_constructor_exists():
    assert callable(rules_Rule.__init__)


def test_rules_rule_constructor_args():
    sig = inspect.signature(rules_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rules_rule_has_name():
    assert hasattr(rules_Rule, "name")
    descriptor = None
    for klass in rules_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rules_ruleslattice_is_not_abstract():
    assert not inspect.isabstract(rules_RulesLattice)


def test_rules_ruleslattice_constructor_exists():
    assert callable(rules_RulesLattice.__init__)


def test_rules_ruleslattice_constructor_args():
    sig = inspect.signature(rules_RulesLattice.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "source" in params, "Missing parameter 'source'"

def test_rules_ruleslattice_has_target():
    assert hasattr(rules_RulesLattice, "target")
    descriptor = None
    for klass in rules_RulesLattice.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_rules_ruleslattice_has_source():
    assert hasattr(rules_RulesLattice, "source")
    descriptor = None
    for klass in rules_RulesLattice.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)


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
rules_NodeRelation_strategy = st.builds(
    rules_NodeRelation,
    relationTgt=
        safe_text,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers(),
    relation=
        safe_text
)
rules_Node_strategy = st.builds(
    rules_Node,
    type=
        safe_text
)
rules_Rule_strategy = st.builds(
    rules_Rule,
    name=
        safe_text
)
rules_RulesLattice_strategy = st.builds(
    rules_RulesLattice,
    target=
        safe_text,
    source=
        safe_text
)

@given(instance=rules_NodeRelation_strategy)
@settings(max_examples=50)
def test_rules_noderelation_instantiation(instance):
    assert isinstance(instance, rules_NodeRelation)



@given(instance=rules_NodeRelation_strategy)
def test_rules_noderelation_relationTgt_setter(instance):
    original = instance.relationTgt
    instance.relationTgt = original
    assert instance.relationTgt == original



@given(instance=rules_NodeRelation_strategy)
def test_rules_noderelation_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=rules_NodeRelation_strategy)
def test_rules_noderelation_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=rules_NodeRelation_strategy)
def test_rules_noderelation_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=rules_Node_strategy)
@settings(max_examples=50)
def test_rules_node_instantiation(instance):
    assert isinstance(instance, rules_Node)



@given(instance=rules_Node_strategy)
def test_rules_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rules_Rule_strategy)
@settings(max_examples=50)
def test_rules_rule_instantiation(instance):
    assert isinstance(instance, rules_Rule)



@given(instance=rules_Rule_strategy)
def test_rules_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rules_RulesLattice_strategy)
@settings(max_examples=50)
def test_rules_ruleslattice_instantiation(instance):
    assert isinstance(instance, rules_RulesLattice)



@given(instance=rules_RulesLattice_strategy)
def test_rules_ruleslattice_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=rules_RulesLattice_strategy)
def test_rules_ruleslattice_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original
