import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rules::NodeRelation,
    rules::Node,
    rules::Rule,
    rules::RulesLattice,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rules::noderelation_is_not_abstract():
    assert not inspect.isabstract(rules::NodeRelation)


def test_rules::noderelation_constructor_exists():
    assert callable(rules::NodeRelation.__init__)


def test_rules::noderelation_constructor_args():
    sig = inspect.signature(rules::NodeRelation.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "relationTgt" in params, "Missing parameter 'relationTgt'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_rules::noderelation_has_relation():
    assert hasattr(rules::NodeRelation, "relation")
    descriptor = None
    for klass in rules::NodeRelation.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)

def test_rules::noderelation_has_upperBound():
    assert hasattr(rules::NodeRelation, "upperBound")
    descriptor = None
    for klass in rules::NodeRelation.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_rules::noderelation_has_relationTgt():
    assert hasattr(rules::NodeRelation, "relationTgt")
    descriptor = None
    for klass in rules::NodeRelation.__mro__:
        if "relationTgt" in klass.__dict__:
            descriptor = klass.__dict__["relationTgt"]
            break
    assert isinstance(descriptor, property)

def test_rules::noderelation_has_lowerBound():
    assert hasattr(rules::NodeRelation, "lowerBound")
    descriptor = None
    for klass in rules::NodeRelation.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_rules::node_is_not_abstract():
    assert not inspect.isabstract(rules::Node)


def test_rules::node_constructor_exists():
    assert callable(rules::Node.__init__)


def test_rules::node_constructor_args():
    sig = inspect.signature(rules::Node.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rules::node_has_type():
    assert hasattr(rules::Node, "type")
    descriptor = None
    for klass in rules::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rules::rule_is_not_abstract():
    assert not inspect.isabstract(rules::Rule)


def test_rules::rule_constructor_exists():
    assert callable(rules::Rule.__init__)


def test_rules::rule_constructor_args():
    sig = inspect.signature(rules::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rules::rule_has_name():
    assert hasattr(rules::Rule, "name")
    descriptor = None
    for klass in rules::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rules::ruleslattice_is_not_abstract():
    assert not inspect.isabstract(rules::RulesLattice)


def test_rules::ruleslattice_constructor_exists():
    assert callable(rules::RulesLattice.__init__)


def test_rules::ruleslattice_constructor_args():
    sig = inspect.signature(rules::RulesLattice.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"

def test_rules::ruleslattice_has_source():
    assert hasattr(rules::RulesLattice, "source")
    descriptor = None
    for klass in rules::RulesLattice.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_rules::ruleslattice_has_target():
    assert hasattr(rules::RulesLattice, "target")
    descriptor = None
    for klass in rules::RulesLattice.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
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
rules::NodeRelation_strategy = st.builds(
    rules::NodeRelation,
    relation=
        safe_text,
    upperBound=
        st.integers(),
    relationTgt=
        safe_text,
    lowerBound=
        st.integers()
)
rules::Node_strategy = st.builds(
    rules::Node,
    type=
        safe_text
)
rules::Rule_strategy = st.builds(
    rules::Rule,
    name=
        safe_text
)
rules::RulesLattice_strategy = st.builds(
    rules::RulesLattice,
    source=
        safe_text,
    target=
        safe_text
)

@given(instance=rules::NodeRelation_strategy)
@settings(max_examples=50)
def test_rules::noderelation_instantiation(instance):
    assert isinstance(instance, rules::NodeRelation)

@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_relationTgt_type(instance):
    assert isinstance(instance.relationTgt, str)


@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_relationTgt_setter(instance):
    original = instance.relationTgt
    instance.relationTgt = original
    assert instance.relationTgt == original

@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=rules::NodeRelation_strategy)
def test_rules::noderelation_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=rules::Node_strategy)
@settings(max_examples=50)
def test_rules::node_instantiation(instance):
    assert isinstance(instance, rules::Node)

@given(instance=rules::Node_strategy)
def test_rules::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rules::Node_strategy)
def test_rules::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rules::Rule_strategy)
@settings(max_examples=50)
def test_rules::rule_instantiation(instance):
    assert isinstance(instance, rules::Rule)

@given(instance=rules::Rule_strategy)
def test_rules::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rules::Rule_strategy)
def test_rules::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rules::RulesLattice_strategy)
@settings(max_examples=50)
def test_rules::ruleslattice_instantiation(instance):
    assert isinstance(instance, rules::RulesLattice)

@given(instance=rules::RulesLattice_strategy)
def test_rules::ruleslattice_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=rules::RulesLattice_strategy)
def test_rules::ruleslattice_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=rules::RulesLattice_strategy)
def test_rules::ruleslattice_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=rules::RulesLattice_strategy)
def test_rules::ruleslattice_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original
