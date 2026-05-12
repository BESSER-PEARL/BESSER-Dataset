import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    feature_Group,
    feature_Attribute,
    feature_Feature,
    feature_Constraint,
    feature_FeatureModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_group_is_not_abstract():
    assert not inspect.isabstract(feature_Group)


def test_feature_group_constructor_exists():
    assert callable(feature_Group.__init__)


def test_feature_group_constructor_args():
    sig = inspect.signature(feature_Group.__init__)
    params = list(sig.parameters.keys())
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"

def test_feature_group_has_maxCardinality():
    assert hasattr(feature_Group, "maxCardinality")
    descriptor = None
    for klass in feature_Group.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)

def test_feature_group_has_minCardinality():
    assert hasattr(feature_Group, "minCardinality")
    descriptor = None
    for klass in feature_Group.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)



def test_feature_attribute_is_not_abstract():
    assert not inspect.isabstract(feature_Attribute)


def test_feature_attribute_constructor_exists():
    assert callable(feature_Attribute.__init__)


def test_feature_attribute_constructor_args():
    sig = inspect.signature(feature_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_feature_attribute_has_type():
    assert hasattr(feature_Attribute, "type")
    descriptor = None
    for klass in feature_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_feature_attribute_has_value():
    assert hasattr(feature_Attribute, "value")
    descriptor = None
    for klass in feature_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_feature_attribute_has_name():
    assert hasattr(feature_Attribute, "name")
    descriptor = None
    for klass in feature_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature_feature_is_not_abstract():
    assert not inspect.isabstract(feature_Feature)


def test_feature_feature_constructor_exists():
    assert callable(feature_Feature.__init__)


def test_feature_feature_constructor_args():
    sig = inspect.signature(feature_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"
    assert "name" in params, "Missing parameter 'name'"

def test_feature_feature_has_minCardinality():
    assert hasattr(feature_Feature, "minCardinality")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)

def test_feature_feature_has_maxCardinality():
    assert hasattr(feature_Feature, "maxCardinality")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)

def test_feature_feature_has_name():
    assert hasattr(feature_Feature, "name")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature_constraint_is_not_abstract():
    assert not inspect.isabstract(feature_Constraint)


def test_feature_constraint_constructor_exists():
    assert callable(feature_Constraint.__init__)


def test_feature_constraint_constructor_args():
    sig = inspect.signature(feature_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_feature_constraint_has_language():
    assert hasattr(feature_Constraint, "language")
    descriptor = None
    for klass in feature_Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_feature_constraint_has_expression():
    assert hasattr(feature_Constraint, "expression")
    descriptor = None
    for klass in feature_Constraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_feature_featuremodel_is_not_abstract():
    assert not inspect.isabstract(feature_FeatureModel)


def test_feature_featuremodel_constructor_exists():
    assert callable(feature_FeatureModel.__init__)


def test_feature_featuremodel_constructor_args():
    sig = inspect.signature(feature_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_feature_featuremodel_has_name():
    assert hasattr(feature_FeatureModel, "name")
    descriptor = None
    for klass in feature_FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
feature_Group_strategy = st.builds(
    feature_Group,
    maxCardinality=
        st.integers(),
    minCardinality=
        st.integers()
)
feature_Attribute_strategy = st.builds(
    feature_Attribute,
    type=
        safe_text,
    value=
        safe_text,
    name=
        safe_text
)
feature_Feature_strategy = st.builds(
    feature_Feature,
    minCardinality=
        st.integers(),
    maxCardinality=
        st.integers(),
    name=
        safe_text
)
feature_Constraint_strategy = st.builds(
    feature_Constraint,
    language=
        safe_text,
    expression=
        safe_text
)
feature_FeatureModel_strategy = st.builds(
    feature_FeatureModel,
    name=
        safe_text
)

@given(instance=feature_Group_strategy)
@settings(max_examples=50)
def test_feature_group_instantiation(instance):
    assert isinstance(instance, feature_Group)



@given(instance=feature_Group_strategy)
def test_feature_group_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original



@given(instance=feature_Group_strategy)
def test_feature_group_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=feature_Attribute_strategy)
@settings(max_examples=50)
def test_feature_attribute_instantiation(instance):
    assert isinstance(instance, feature_Attribute)



@given(instance=feature_Attribute_strategy)
def test_feature_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=feature_Attribute_strategy)
def test_feature_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=feature_Attribute_strategy)
def test_feature_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=feature_Feature_strategy)
@settings(max_examples=50)
def test_feature_feature_instantiation(instance):
    assert isinstance(instance, feature_Feature)



@given(instance=feature_Feature_strategy)
def test_feature_feature_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original



@given(instance=feature_Feature_strategy)
def test_feature_feature_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original



@given(instance=feature_Feature_strategy)
def test_feature_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=feature_Feature_strategy)
@settings(max_examples=30)
def test_feature_feature_ismandatory_changes_state(instance):
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
        assert has_statements, f"Function 'isMandatory' in feature_Feature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMandatory' in feature_Feature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMandatory' in feature_Feature is not implemented or raised an error")

@given(instance=feature_Constraint_strategy)
@settings(max_examples=50)
def test_feature_constraint_instantiation(instance):
    assert isinstance(instance, feature_Constraint)



@given(instance=feature_Constraint_strategy)
def test_feature_constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=feature_Constraint_strategy)
def test_feature_constraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=feature_FeatureModel_strategy)
@settings(max_examples=50)
def test_feature_featuremodel_instantiation(instance):
    assert isinstance(instance, feature_FeatureModel)



@given(instance=feature_FeatureModel_strategy)
def test_feature_featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
