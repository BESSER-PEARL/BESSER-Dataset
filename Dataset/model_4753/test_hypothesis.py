import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fM::Child,
    fM::Constraints,
    fM::FeatureDiagram,
    fM::FeatureModel,
    Formula,
    fM::Var,
    fM::RuleElement,
    fM::Formula,
    fM::Rule,
    Child,
    fM::Node,
    fM::Leaf,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fm::child_is_not_abstract():
    assert not inspect.isabstract(fM::Child)


def test_fm::child_constructor_exists():
    assert callable(fM::Child.__init__)


def test_fm::child_constructor_args():
    sig = inspect.signature(fM::Child.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_fm::child_has_name():
    assert hasattr(fM::Child, "name")
    descriptor = None
    for klass in fM::Child.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm::child_has_mandatory():
    assert hasattr(fM::Child, "mandatory")
    descriptor = None
    for klass in fM::Child.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_fm::constraints_is_not_abstract():
    assert not inspect.isabstract(fM::Constraints)


def test_fm::constraints_constructor_exists():
    assert callable(fM::Constraints.__init__)


def test_fm::constraints_constructor_args():
    sig = inspect.signature(fM::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_fm::featurediagram_is_not_abstract():
    assert not inspect.isabstract(fM::FeatureDiagram)


def test_fm::featurediagram_constructor_exists():
    assert callable(fM::FeatureDiagram.__init__)


def test_fm::featurediagram_constructor_args():
    sig = inspect.signature(fM::FeatureDiagram.__init__)
    params = list(sig.parameters.keys())



def test_fm::featuremodel_is_not_abstract():
    assert not inspect.isabstract(fM::FeatureModel)


def test_fm::featuremodel_constructor_exists():
    assert callable(fM::FeatureModel.__init__)


def test_fm::featuremodel_constructor_args():
    sig = inspect.signature(fM::FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_formula_is_not_abstract():
    assert not inspect.isabstract(Formula)


def test_formula_constructor_exists():
    assert callable(Formula.__init__)


def test_formula_constructor_args():
    sig = inspect.signature(Formula.__init__)
    params = list(sig.parameters.keys())



def test_fm::var_is_not_abstract():
    assert not inspect.isabstract(fM::Var)


def test_fm::var_constructor_exists():
    assert callable(fM::Var.__init__)


def test_fm::var_constructor_args():
    sig = inspect.signature(fM::Var.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "name" in params, "Missing parameter 'name'"

def test_fm::var_has_not_():
    assert hasattr(fM::Var, "not_")
    descriptor = None
    for klass in fM::Var.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_fm::var_has_name():
    assert hasattr(fM::Var, "name")
    descriptor = None
    for klass in fM::Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fm::ruleelement_is_not_abstract():
    assert not inspect.isabstract(fM::RuleElement)


def test_fm::ruleelement_constructor_exists():
    assert callable(fM::RuleElement.__init__)


def test_fm::ruleelement_constructor_args():
    sig = inspect.signature(fM::RuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "close_operator" in params, "Missing parameter 'close_operator'"
    assert "open_operator" in params, "Missing parameter 'open_operator'"

def test_fm::ruleelement_has_close_operator():
    assert hasattr(fM::RuleElement, "close_operator")
    descriptor = None
    for klass in fM::RuleElement.__mro__:
        if "close_operator" in klass.__dict__:
            descriptor = klass.__dict__["close_operator"]
            break
    assert isinstance(descriptor, property)

def test_fm::ruleelement_has_open_operator():
    assert hasattr(fM::RuleElement, "open_operator")
    descriptor = None
    for klass in fM::RuleElement.__mro__:
        if "open_operator" in klass.__dict__:
            descriptor = klass.__dict__["open_operator"]
            break
    assert isinstance(descriptor, property)



def test_fm::formula_is_not_abstract():
    assert not inspect.isabstract(fM::Formula)


def test_fm::formula_constructor_exists():
    assert callable(fM::Formula.__init__)


def test_fm::formula_constructor_args():
    sig = inspect.signature(fM::Formula.__init__)
    params = list(sig.parameters.keys())



def test_fm::rule_is_not_abstract():
    assert not inspect.isabstract(fM::Rule)


def test_fm::rule_constructor_exists():
    assert callable(fM::Rule.__init__)


def test_fm::rule_constructor_args():
    sig = inspect.signature(fM::Rule.__init__)
    params = list(sig.parameters.keys())



def test_child_is_not_abstract():
    assert not inspect.isabstract(Child)


def test_child_constructor_exists():
    assert callable(Child.__init__)


def test_child_constructor_args():
    sig = inspect.signature(Child.__init__)
    params = list(sig.parameters.keys())



def test_fm::node_is_not_abstract():
    assert not inspect.isabstract(fM::Node)


def test_fm::node_constructor_exists():
    assert callable(fM::Node.__init__)


def test_fm::node_constructor_args():
    sig = inspect.signature(fM::Node.__init__)
    params = list(sig.parameters.keys())
    assert "open_relation" in params, "Missing parameter 'open_relation'"
    assert "close_relation" in params, "Missing parameter 'close_relation'"

def test_fm::node_has_open_relation():
    assert hasattr(fM::Node, "open_relation")
    descriptor = None
    for klass in fM::Node.__mro__:
        if "open_relation" in klass.__dict__:
            descriptor = klass.__dict__["open_relation"]
            break
    assert isinstance(descriptor, property)

def test_fm::node_has_close_relation():
    assert hasattr(fM::Node, "close_relation")
    descriptor = None
    for klass in fM::Node.__mro__:
        if "close_relation" in klass.__dict__:
            descriptor = klass.__dict__["close_relation"]
            break
    assert isinstance(descriptor, property)



def test_fm::leaf_is_not_abstract():
    assert not inspect.isabstract(fM::Leaf)


def test_fm::leaf_constructor_exists():
    assert callable(fM::Leaf.__init__)


def test_fm::leaf_constructor_args():
    sig = inspect.signature(fM::Leaf.__init__)
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
fM::Child_strategy = st.builds(
    fM::Child,
    name=
        safe_text,
    mandatory=
        st.booleans()
)
fM::Constraints_strategy = st.builds(
    fM::Constraints,
)
fM::FeatureDiagram_strategy = st.builds(
    fM::FeatureDiagram,
)
fM::FeatureModel_strategy = st.builds(
    fM::FeatureModel,
)
Formula_strategy = st.builds(
    Formula,
)
fM::Var_strategy = st.builds(
    fM::Var,
    not_=
        st.booleans(),
    name=
        safe_text
)
fM::RuleElement_strategy = st.builds(
    fM::RuleElement,
    close_operator=
        safe_text,
    open_operator=
        safe_text
)
fM::Formula_strategy = st.builds(
    fM::Formula,
)
fM::Rule_strategy = st.builds(
    fM::Rule,
)
Child_strategy = st.builds(
    Child,
)
fM::Node_strategy = st.builds(
    fM::Node,
    open_relation=
        safe_text,
    close_relation=
        safe_text
)
fM::Leaf_strategy = st.builds(
    fM::Leaf,
)

@given(instance=fM::Child_strategy)
@settings(max_examples=50)
def test_fm::child_instantiation(instance):
    assert isinstance(instance, fM::Child)

@given(instance=fM::Child_strategy)
def test_fm::child_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fM::Child_strategy)
def test_fm::child_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fM::Child_strategy)
def test_fm::child_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=fM::Child_strategy)
def test_fm::child_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=fM::Constraints_strategy)
@settings(max_examples=50)
def test_fm::constraints_instantiation(instance):
    assert isinstance(instance, fM::Constraints)

@given(instance=fM::FeatureDiagram_strategy)
@settings(max_examples=50)
def test_fm::featurediagram_instantiation(instance):
    assert isinstance(instance, fM::FeatureDiagram)

@given(instance=fM::FeatureModel_strategy)
@settings(max_examples=50)
def test_fm::featuremodel_instantiation(instance):
    assert isinstance(instance, fM::FeatureModel)

@given(instance=Formula_strategy)
@settings(max_examples=50)
def test_formula_instantiation(instance):
    assert isinstance(instance, Formula)

@given(instance=fM::Var_strategy)
@settings(max_examples=50)
def test_fm::var_instantiation(instance):
    assert isinstance(instance, fM::Var)

@given(instance=fM::Var_strategy)
def test_fm::var_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=fM::Var_strategy)
def test_fm::var_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=fM::Var_strategy)
def test_fm::var_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fM::Var_strategy)
def test_fm::var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fM::RuleElement_strategy)
@settings(max_examples=50)
def test_fm::ruleelement_instantiation(instance):
    assert isinstance(instance, fM::RuleElement)

@given(instance=fM::RuleElement_strategy)
def test_fm::ruleelement_close_operator_type(instance):
    assert isinstance(instance.close_operator, str)


@given(instance=fM::RuleElement_strategy)
def test_fm::ruleelement_close_operator_setter(instance):
    original = instance.close_operator
    instance.close_operator = original
    assert instance.close_operator == original

@given(instance=fM::RuleElement_strategy)
def test_fm::ruleelement_open_operator_type(instance):
    assert isinstance(instance.open_operator, str)


@given(instance=fM::RuleElement_strategy)
def test_fm::ruleelement_open_operator_setter(instance):
    original = instance.open_operator
    instance.open_operator = original
    assert instance.open_operator == original

@given(instance=fM::Formula_strategy)
@settings(max_examples=50)
def test_fm::formula_instantiation(instance):
    assert isinstance(instance, fM::Formula)

@given(instance=fM::Rule_strategy)
@settings(max_examples=50)
def test_fm::rule_instantiation(instance):
    assert isinstance(instance, fM::Rule)

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)

@given(instance=fM::Node_strategy)
@settings(max_examples=50)
def test_fm::node_instantiation(instance):
    assert isinstance(instance, fM::Node)

@given(instance=fM::Node_strategy)
def test_fm::node_open_relation_type(instance):
    assert isinstance(instance.open_relation, str)


@given(instance=fM::Node_strategy)
def test_fm::node_open_relation_setter(instance):
    original = instance.open_relation
    instance.open_relation = original
    assert instance.open_relation == original

@given(instance=fM::Node_strategy)
def test_fm::node_close_relation_type(instance):
    assert isinstance(instance.close_relation, str)


@given(instance=fM::Node_strategy)
def test_fm::node_close_relation_setter(instance):
    original = instance.close_relation
    instance.close_relation = original
    assert instance.close_relation == original

@given(instance=fM::Leaf_strategy)
@settings(max_examples=50)
def test_fm::leaf_instantiation(instance):
    assert isinstance(instance, fM::Leaf)
