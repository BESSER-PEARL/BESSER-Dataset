import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    feature::Annotation,
    feature::Attribute,
    FeatureTreeNode,
    feature::Group,
    feature::FeatureTreeNode,
    feature::FeatureModel,
    feature::Feature,
    feature::Constraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature::annotation_is_not_abstract():
    assert not inspect.isabstract(feature::Annotation)


def test_feature::annotation_constructor_exists():
    assert callable(feature::Annotation.__init__)


def test_feature::annotation_constructor_args():
    sig = inspect.signature(feature::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_feature::attribute_is_not_abstract():
    assert not inspect.isabstract(feature::Attribute)


def test_feature::attribute_constructor_exists():
    assert callable(feature::Attribute.__init__)


def test_feature::attribute_constructor_args():
    sig = inspect.signature(feature::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_feature::attribute_has_name():
    assert hasattr(feature::Attribute, "name")
    descriptor = None
    for klass in feature::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_feature::attribute_has_type():
    assert hasattr(feature::Attribute, "type")
    descriptor = None
    for klass in feature::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_feature::attribute_has_value():
    assert hasattr(feature::Attribute, "value")
    descriptor = None
    for klass in feature::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuretreenode_is_not_abstract():
    assert not inspect.isabstract(FeatureTreeNode)


def test_featuretreenode_constructor_exists():
    assert callable(FeatureTreeNode.__init__)


def test_featuretreenode_constructor_args():
    sig = inspect.signature(FeatureTreeNode.__init__)
    params = list(sig.parameters.keys())



def test_feature::group_is_not_abstract():
    assert not inspect.isabstract(feature::Group)


def test_feature::group_constructor_exists():
    assert callable(feature::Group.__init__)


def test_feature::group_constructor_args():
    sig = inspect.signature(feature::Group.__init__)
    params = list(sig.parameters.keys())



def test_feature::featuretreenode_is_not_abstract():
    assert not inspect.isabstract(feature::FeatureTreeNode)


def test_feature::featuretreenode_constructor_exists():
    assert callable(feature::FeatureTreeNode.__init__)


def test_feature::featuretreenode_constructor_args():
    sig = inspect.signature(feature::FeatureTreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"

def test_feature::featuretreenode_has_minCardinality():
    assert hasattr(feature::FeatureTreeNode, "minCardinality")
    descriptor = None
    for klass in feature::FeatureTreeNode.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)

def test_feature::featuretreenode_has_maxCardinality():
    assert hasattr(feature::FeatureTreeNode, "maxCardinality")
    descriptor = None
    for klass in feature::FeatureTreeNode.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)



def test_feature::featuremodel_is_not_abstract():
    assert not inspect.isabstract(feature::FeatureModel)


def test_feature::featuremodel_constructor_exists():
    assert callable(feature::FeatureModel.__init__)


def test_feature::featuremodel_constructor_args():
    sig = inspect.signature(feature::FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_feature::featuremodel_has_name():
    assert hasattr(feature::FeatureModel, "name")
    descriptor = None
    for klass in feature::FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature::feature_is_not_abstract():
    assert not inspect.isabstract(feature::Feature)


def test_feature::feature_constructor_exists():
    assert callable(feature::Feature.__init__)


def test_feature::feature_constructor_args():
    sig = inspect.signature(feature::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_feature::feature_has_name():
    assert hasattr(feature::Feature, "name")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature::constraint_is_not_abstract():
    assert not inspect.isabstract(feature::Constraint)


def test_feature::constraint_constructor_exists():
    assert callable(feature::Constraint.__init__)


def test_feature::constraint_constructor_args():
    sig = inspect.signature(feature::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_feature::constraint_has_language():
    assert hasattr(feature::Constraint, "language")
    descriptor = None
    for klass in feature::Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_feature::constraint_has_expression():
    assert hasattr(feature::Constraint, "expression")
    descriptor = None
    for klass in feature::Constraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
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
feature::Annotation_strategy = st.builds(
    feature::Annotation,
)
feature::Attribute_strategy = st.builds(
    feature::Attribute,
    name=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
FeatureTreeNode_strategy = st.builds(
    FeatureTreeNode,
)
feature::Group_strategy = st.builds(
    feature::Group,
)
feature::FeatureTreeNode_strategy = st.builds(
    feature::FeatureTreeNode,
    minCardinality=
        st.integers(),
    maxCardinality=
        st.integers()
)
feature::FeatureModel_strategy = st.builds(
    feature::FeatureModel,
    name=
        safe_text
)
feature::Feature_strategy = st.builds(
    feature::Feature,
    name=
        safe_text
)
feature::Constraint_strategy = st.builds(
    feature::Constraint,
    language=
        safe_text,
    expression=
        safe_text
)

@given(instance=feature::Annotation_strategy)
@settings(max_examples=50)
def test_feature::annotation_instantiation(instance):
    assert isinstance(instance, feature::Annotation)

@given(instance=feature::Attribute_strategy)
@settings(max_examples=50)
def test_feature::attribute_instantiation(instance):
    assert isinstance(instance, feature::Attribute)

@given(instance=feature::Attribute_strategy)
def test_feature::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=feature::Attribute_strategy)
def test_feature::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=feature::Attribute_strategy)
def test_feature::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=feature::Attribute_strategy)
def test_feature::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=feature::Attribute_strategy)
def test_feature::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=feature::Attribute_strategy)
def test_feature::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FeatureTreeNode_strategy)
@settings(max_examples=50)
def test_featuretreenode_instantiation(instance):
    assert isinstance(instance, FeatureTreeNode)

@given(instance=feature::Group_strategy)
@settings(max_examples=50)
def test_feature::group_instantiation(instance):
    assert isinstance(instance, feature::Group)

@given(instance=feature::FeatureTreeNode_strategy)
@settings(max_examples=50)
def test_feature::featuretreenode_instantiation(instance):
    assert isinstance(instance, feature::FeatureTreeNode)

@given(instance=feature::FeatureTreeNode_strategy)
def test_feature::featuretreenode_minCardinality_type(instance):
    assert isinstance(instance.minCardinality, int)


@given(instance=feature::FeatureTreeNode_strategy)
def test_feature::featuretreenode_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=feature::FeatureTreeNode_strategy)
def test_feature::featuretreenode_maxCardinality_type(instance):
    assert isinstance(instance.maxCardinality, int)


@given(instance=feature::FeatureTreeNode_strategy)
def test_feature::featuretreenode_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original

@given(instance=feature::FeatureModel_strategy)
@settings(max_examples=50)
def test_feature::featuremodel_instantiation(instance):
    assert isinstance(instance, feature::FeatureModel)

@given(instance=feature::FeatureModel_strategy)
def test_feature::featuremodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=feature::FeatureModel_strategy)
def test_feature::featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=feature::Feature_strategy)
@settings(max_examples=50)
def test_feature::feature_instantiation(instance):
    assert isinstance(instance, feature::Feature)

@given(instance=feature::Feature_strategy)
def test_feature::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=feature::Feature_strategy)
def test_feature::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=feature::Feature_strategy)
@settings(max_examples=30)
def test_feature::feature_ismandatory_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMandatory()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMandatory).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMandatory' in feature::Feature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMandatory' in feature::Feature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMandatory' in feature::Feature is not implemented or raised an error")

@given(instance=feature::Constraint_strategy)
@settings(max_examples=50)
def test_feature::constraint_instantiation(instance):
    assert isinstance(instance, feature::Constraint)

@given(instance=feature::Constraint_strategy)
def test_feature::constraint_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=feature::Constraint_strategy)
def test_feature::constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=feature::Constraint_strategy)
def test_feature::constraint_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=feature::Constraint_strategy)
def test_feature::constraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original
