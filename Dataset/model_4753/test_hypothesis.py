import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fM_Child,
    fM_Constraints,
    fM_FeatureDiagram,
    fM_FeatureModel,
    Formula,
    fM_Var,
    fM_RuleElement,
    fM_Formula,
    fM_Rule,
    Child,
    fM_Node,
    fM_Leaf,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fm_child_is_not_abstract():
    assert not inspect.isabstract(fM_Child)


def test_fm_child_constructor_exists():
    assert callable(fM_Child.__init__)


def test_fm_child_constructor_args():
    sig = inspect.signature(fM_Child.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_fm_child_has_name():
    assert hasattr(fM_Child, "name")
    descriptor = None
    for klass in fM_Child.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm_child_has_mandatory():
    assert hasattr(fM_Child, "mandatory")
    descriptor = None
    for klass in fM_Child.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_fm_constraints_is_not_abstract():
    assert not inspect.isabstract(fM_Constraints)


def test_fm_constraints_constructor_exists():
    assert callable(fM_Constraints.__init__)


def test_fm_constraints_constructor_args():
    sig = inspect.signature(fM_Constraints.__init__)
    params = list(sig.parameters.keys())



def test_fm_featurediagram_is_not_abstract():
    assert not inspect.isabstract(fM_FeatureDiagram)


def test_fm_featurediagram_constructor_exists():
    assert callable(fM_FeatureDiagram.__init__)


def test_fm_featurediagram_constructor_args():
    sig = inspect.signature(fM_FeatureDiagram.__init__)
    params = list(sig.parameters.keys())



def test_fm_featuremodel_is_not_abstract():
    assert not inspect.isabstract(fM_FeatureModel)


def test_fm_featuremodel_constructor_exists():
    assert callable(fM_FeatureModel.__init__)


def test_fm_featuremodel_constructor_args():
    sig = inspect.signature(fM_FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_formula_is_not_abstract():
    assert not inspect.isabstract(Formula)


def test_formula_constructor_exists():
    assert callable(Formula.__init__)


def test_formula_constructor_args():
    sig = inspect.signature(Formula.__init__)
    params = list(sig.parameters.keys())



def test_fm_var_is_not_abstract():
    assert not inspect.isabstract(fM_Var)


def test_fm_var_constructor_exists():
    assert callable(fM_Var.__init__)


def test_fm_var_constructor_args():
    sig = inspect.signature(fM_Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_fm_var_has_name():
    assert hasattr(fM_Var, "name")
    descriptor = None
    for klass in fM_Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm_var_has_not_():
    assert hasattr(fM_Var, "not_")
    descriptor = None
    for klass in fM_Var.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_fm_ruleelement_is_not_abstract():
    assert not inspect.isabstract(fM_RuleElement)


def test_fm_ruleelement_constructor_exists():
    assert callable(fM_RuleElement.__init__)


def test_fm_ruleelement_constructor_args():
    sig = inspect.signature(fM_RuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "open_operator" in params, "Missing parameter 'open_operator'"
    assert "close_operator" in params, "Missing parameter 'close_operator'"

def test_fm_ruleelement_has_open_operator():
    assert hasattr(fM_RuleElement, "open_operator")
    descriptor = None
    for klass in fM_RuleElement.__mro__:
        if "open_operator" in klass.__dict__:
            descriptor = klass.__dict__["open_operator"]
            break
    assert isinstance(descriptor, property)

def test_fm_ruleelement_has_close_operator():
    assert hasattr(fM_RuleElement, "close_operator")
    descriptor = None
    for klass in fM_RuleElement.__mro__:
        if "close_operator" in klass.__dict__:
            descriptor = klass.__dict__["close_operator"]
            break
    assert isinstance(descriptor, property)



def test_fm_formula_is_not_abstract():
    assert not inspect.isabstract(fM_Formula)


def test_fm_formula_constructor_exists():
    assert callable(fM_Formula.__init__)


def test_fm_formula_constructor_args():
    sig = inspect.signature(fM_Formula.__init__)
    params = list(sig.parameters.keys())



def test_fm_rule_is_not_abstract():
    assert not inspect.isabstract(fM_Rule)


def test_fm_rule_constructor_exists():
    assert callable(fM_Rule.__init__)


def test_fm_rule_constructor_args():
    sig = inspect.signature(fM_Rule.__init__)
    params = list(sig.parameters.keys())



def test_child_is_not_abstract():
    assert not inspect.isabstract(Child)


def test_child_constructor_exists():
    assert callable(Child.__init__)


def test_child_constructor_args():
    sig = inspect.signature(Child.__init__)
    params = list(sig.parameters.keys())



def test_fm_node_is_not_abstract():
    assert not inspect.isabstract(fM_Node)


def test_fm_node_constructor_exists():
    assert callable(fM_Node.__init__)


def test_fm_node_constructor_args():
    sig = inspect.signature(fM_Node.__init__)
    params = list(sig.parameters.keys())
    assert "close_relation" in params, "Missing parameter 'close_relation'"
    assert "open_relation" in params, "Missing parameter 'open_relation'"

def test_fm_node_has_close_relation():
    assert hasattr(fM_Node, "close_relation")
    descriptor = None
    for klass in fM_Node.__mro__:
        if "close_relation" in klass.__dict__:
            descriptor = klass.__dict__["close_relation"]
            break
    assert isinstance(descriptor, property)

def test_fm_node_has_open_relation():
    assert hasattr(fM_Node, "open_relation")
    descriptor = None
    for klass in fM_Node.__mro__:
        if "open_relation" in klass.__dict__:
            descriptor = klass.__dict__["open_relation"]
            break
    assert isinstance(descriptor, property)



def test_fm_leaf_is_not_abstract():
    assert not inspect.isabstract(fM_Leaf)


def test_fm_leaf_constructor_exists():
    assert callable(fM_Leaf.__init__)


def test_fm_leaf_constructor_args():
    sig = inspect.signature(fM_Leaf.__init__)
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
fM_Child_strategy = st.builds(
    fM_Child,
    name=
        safe_text,
    mandatory=
        st.booleans()
)
fM_Constraints_strategy = st.builds(
    fM_Constraints,
)
fM_FeatureDiagram_strategy = st.builds(
    fM_FeatureDiagram,
)
fM_FeatureModel_strategy = st.builds(
    fM_FeatureModel,
)
Formula_strategy = st.builds(
    Formula,
)
fM_Var_strategy = st.builds(
    fM_Var,
    name=
        safe_text,
    not_=
        st.booleans()
)
fM_RuleElement_strategy = st.builds(
    fM_RuleElement,
    open_operator=
        safe_text,
    close_operator=
        safe_text
)
fM_Formula_strategy = st.builds(
    fM_Formula,
)
fM_Rule_strategy = st.builds(
    fM_Rule,
)
Child_strategy = st.builds(
    Child,
)
fM_Node_strategy = st.builds(
    fM_Node,
    close_relation=
        safe_text,
    open_relation=
        safe_text
)
fM_Leaf_strategy = st.builds(
    fM_Leaf,
)

@given(instance=fM_Child_strategy)
@settings(max_examples=50)
def test_fm_child_instantiation(instance):
    assert isinstance(instance, fM_Child)



@given(instance=fM_Child_strategy)
def test_fm_child_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fM_Child_strategy)
def test_fm_child_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=fM_Constraints_strategy)
@settings(max_examples=50)
def test_fm_constraints_instantiation(instance):
    assert isinstance(instance, fM_Constraints)

@given(instance=fM_FeatureDiagram_strategy)
@settings(max_examples=50)
def test_fm_featurediagram_instantiation(instance):
    assert isinstance(instance, fM_FeatureDiagram)

@given(instance=fM_FeatureModel_strategy)
@settings(max_examples=50)
def test_fm_featuremodel_instantiation(instance):
    assert isinstance(instance, fM_FeatureModel)

@given(instance=Formula_strategy)
@settings(max_examples=50)
def test_formula_instantiation(instance):
    assert isinstance(instance, Formula)

@given(instance=fM_Var_strategy)
@settings(max_examples=50)
def test_fm_var_instantiation(instance):
    assert isinstance(instance, fM_Var)



@given(instance=fM_Var_strategy)
def test_fm_var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fM_Var_strategy)
def test_fm_var_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=fM_RuleElement_strategy)
@settings(max_examples=50)
def test_fm_ruleelement_instantiation(instance):
    assert isinstance(instance, fM_RuleElement)



@given(instance=fM_RuleElement_strategy)
def test_fm_ruleelement_open_operator_setter(instance):
    original = instance.open_operator
    instance.open_operator = original
    assert instance.open_operator == original



@given(instance=fM_RuleElement_strategy)
def test_fm_ruleelement_close_operator_setter(instance):
    original = instance.close_operator
    instance.close_operator = original
    assert instance.close_operator == original

@given(instance=fM_Formula_strategy)
@settings(max_examples=50)
def test_fm_formula_instantiation(instance):
    assert isinstance(instance, fM_Formula)

@given(instance=fM_Rule_strategy)
@settings(max_examples=50)
def test_fm_rule_instantiation(instance):
    assert isinstance(instance, fM_Rule)

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)

@given(instance=fM_Node_strategy)
@settings(max_examples=50)
def test_fm_node_instantiation(instance):
    assert isinstance(instance, fM_Node)



@given(instance=fM_Node_strategy)
def test_fm_node_close_relation_setter(instance):
    original = instance.close_relation
    instance.close_relation = original
    assert instance.close_relation == original



@given(instance=fM_Node_strategy)
def test_fm_node_open_relation_setter(instance):
    original = instance.open_relation
    instance.open_relation = original
    assert instance.open_relation == original

@given(instance=fM_Leaf_strategy)
@settings(max_examples=50)
def test_fm_leaf_instantiation(instance):
    assert isinstance(instance, fM_Leaf)
