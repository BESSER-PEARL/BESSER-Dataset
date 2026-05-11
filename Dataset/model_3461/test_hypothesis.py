import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Cardinality,
    fm::Cardinality,
    OrFeature,
    fm::XorFeature,
    fm::GroupCardinality,
    Operator,
    fm::OrOperator,
    fm::AndOperator,
    fm::Operator,
    fm::Operation,
    Constraints,
    fm::BooleanConstraints,
    fm::CardExConstraint,
    Feature,
    fm::OrFeature,
    fm::Attribute,
    fm::FeatureCardinality,
    fm::Constraints,
    fm::Feature,
    fm::FeatureModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cardinality_is_not_abstract():
    assert not inspect.isabstract(Cardinality)


def test_cardinality_constructor_exists():
    assert callable(Cardinality.__init__)


def test_cardinality_constructor_args():
    sig = inspect.signature(Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_fm::cardinality_is_not_abstract():
    assert not inspect.isabstract(fm::Cardinality)


def test_fm::cardinality_constructor_exists():
    assert callable(fm::Cardinality.__init__)


def test_fm::cardinality_constructor_args():
    sig = inspect.signature(fm::Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_fm::cardinality_has_min():
    assert hasattr(fm::Cardinality, "min")
    descriptor = None
    for klass in fm::Cardinality.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_fm::cardinality_has_max():
    assert hasattr(fm::Cardinality, "max")
    descriptor = None
    for klass in fm::Cardinality.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_orfeature_is_not_abstract():
    assert not inspect.isabstract(OrFeature)


def test_orfeature_constructor_exists():
    assert callable(OrFeature.__init__)


def test_orfeature_constructor_args():
    sig = inspect.signature(OrFeature.__init__)
    params = list(sig.parameters.keys())



def test_fm::xorfeature_is_not_abstract():
    assert not inspect.isabstract(fm::XorFeature)


def test_fm::xorfeature_constructor_exists():
    assert callable(fm::XorFeature.__init__)


def test_fm::xorfeature_constructor_args():
    sig = inspect.signature(fm::XorFeature.__init__)
    params = list(sig.parameters.keys())



def test_fm::groupcardinality_is_not_abstract():
    assert not inspect.isabstract(fm::GroupCardinality)


def test_fm::groupcardinality_constructor_exists():
    assert callable(fm::GroupCardinality.__init__)


def test_fm::groupcardinality_constructor_args():
    sig = inspect.signature(fm::GroupCardinality.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_fm::oroperator_is_not_abstract():
    assert not inspect.isabstract(fm::OrOperator)


def test_fm::oroperator_constructor_exists():
    assert callable(fm::OrOperator.__init__)


def test_fm::oroperator_constructor_args():
    sig = inspect.signature(fm::OrOperator.__init__)
    params = list(sig.parameters.keys())



def test_fm::andoperator_is_not_abstract():
    assert not inspect.isabstract(fm::AndOperator)


def test_fm::andoperator_constructor_exists():
    assert callable(fm::AndOperator.__init__)


def test_fm::andoperator_constructor_args():
    sig = inspect.signature(fm::AndOperator.__init__)
    params = list(sig.parameters.keys())



def test_fm::operator_is_not_abstract():
    assert not inspect.isabstract(fm::Operator)


def test_fm::operator_constructor_exists():
    assert callable(fm::Operator.__init__)


def test_fm::operator_constructor_args():
    sig = inspect.signature(fm::Operator.__init__)
    params = list(sig.parameters.keys())



def test_fm::operation_is_not_abstract():
    assert not inspect.isabstract(fm::Operation)


def test_fm::operation_constructor_exists():
    assert callable(fm::Operation.__init__)


def test_fm::operation_constructor_args():
    sig = inspect.signature(fm::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fm::operation_has_value():
    assert hasattr(fm::Operation, "value")
    descriptor = None
    for klass in fm::Operation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_constraints_is_not_abstract():
    assert not inspect.isabstract(Constraints)


def test_constraints_constructor_exists():
    assert callable(Constraints.__init__)


def test_constraints_constructor_args():
    sig = inspect.signature(Constraints.__init__)
    params = list(sig.parameters.keys())



def test_fm::booleanconstraints_is_not_abstract():
    assert not inspect.isabstract(fm::BooleanConstraints)


def test_fm::booleanconstraints_constructor_exists():
    assert callable(fm::BooleanConstraints.__init__)


def test_fm::booleanconstraints_constructor_args():
    sig = inspect.signature(fm::BooleanConstraints.__init__)
    params = list(sig.parameters.keys())



def test_fm::cardexconstraint_is_not_abstract():
    assert not inspect.isabstract(fm::CardExConstraint)


def test_fm::cardexconstraint_constructor_exists():
    assert callable(fm::CardExConstraint.__init__)


def test_fm::cardexconstraint_constructor_args():
    sig = inspect.signature(fm::CardExConstraint.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_fm::orfeature_is_not_abstract():
    assert not inspect.isabstract(fm::OrFeature)


def test_fm::orfeature_constructor_exists():
    assert callable(fm::OrFeature.__init__)


def test_fm::orfeature_constructor_args():
    sig = inspect.signature(fm::OrFeature.__init__)
    params = list(sig.parameters.keys())



def test_fm::attribute_is_not_abstract():
    assert not inspect.isabstract(fm::Attribute)


def test_fm::attribute_constructor_exists():
    assert callable(fm::Attribute.__init__)


def test_fm::attribute_constructor_args():
    sig = inspect.signature(fm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fm::attribute_has_name():
    assert hasattr(fm::Attribute, "name")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fm::attribute_has_value():
    assert hasattr(fm::Attribute, "value")
    descriptor = None
    for klass in fm::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fm::featurecardinality_is_not_abstract():
    assert not inspect.isabstract(fm::FeatureCardinality)


def test_fm::featurecardinality_constructor_exists():
    assert callable(fm::FeatureCardinality.__init__)


def test_fm::featurecardinality_constructor_args():
    sig = inspect.signature(fm::FeatureCardinality.__init__)
    params = list(sig.parameters.keys())



def test_fm::constraints_is_not_abstract():
    assert not inspect.isabstract(fm::Constraints)


def test_fm::constraints_constructor_exists():
    assert callable(fm::Constraints.__init__)


def test_fm::constraints_constructor_args():
    sig = inspect.signature(fm::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_fm::feature_is_not_abstract():
    assert not inspect.isabstract(fm::Feature)


def test_fm::feature_constructor_exists():
    assert callable(fm::Feature.__init__)


def test_fm::feature_constructor_args():
    sig = inspect.signature(fm::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fm::feature_has_name():
    assert hasattr(fm::Feature, "name")
    descriptor = None
    for klass in fm::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fm::featuremodel_is_not_abstract():
    assert not inspect.isabstract(fm::FeatureModel)


def test_fm::featuremodel_constructor_exists():
    assert callable(fm::FeatureModel.__init__)


def test_fm::featuremodel_constructor_args():
    sig = inspect.signature(fm::FeatureModel.__init__)
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
Cardinality_strategy = st.builds(
    Cardinality,
)
fm::Cardinality_strategy = st.builds(
    fm::Cardinality,
    min=
        st.integers(),
    max=
        st.integers()
)
OrFeature_strategy = st.builds(
    OrFeature,
)
fm::XorFeature_strategy = st.builds(
    fm::XorFeature,
)
fm::GroupCardinality_strategy = st.builds(
    fm::GroupCardinality,
)
Operator_strategy = st.builds(
    Operator,
)
fm::OrOperator_strategy = st.builds(
    fm::OrOperator,
)
fm::AndOperator_strategy = st.builds(
    fm::AndOperator,
)
fm::Operator_strategy = st.builds(
    fm::Operator,
)
fm::Operation_strategy = st.builds(
    fm::Operation,
    value=
        st.integers()
)
Constraints_strategy = st.builds(
    Constraints,
)
fm::BooleanConstraints_strategy = st.builds(
    fm::BooleanConstraints,
)
fm::CardExConstraint_strategy = st.builds(
    fm::CardExConstraint,
)
Feature_strategy = st.builds(
    Feature,
)
fm::OrFeature_strategy = st.builds(
    fm::OrFeature,
)
fm::Attribute_strategy = st.builds(
    fm::Attribute,
    name=
        safe_text,
    value=
        safe_text
)
fm::FeatureCardinality_strategy = st.builds(
    fm::FeatureCardinality,
)
fm::Constraints_strategy = st.builds(
    fm::Constraints,
)
fm::Feature_strategy = st.builds(
    fm::Feature,
    name=
        safe_text
)
fm::FeatureModel_strategy = st.builds(
    fm::FeatureModel,
)

@given(instance=Cardinality_strategy)
@settings(max_examples=50)
def test_cardinality_instantiation(instance):
    assert isinstance(instance, Cardinality)

@given(instance=fm::Cardinality_strategy)
@settings(max_examples=50)
def test_fm::cardinality_instantiation(instance):
    assert isinstance(instance, fm::Cardinality)

@given(instance=fm::Cardinality_strategy)
def test_fm::cardinality_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=fm::Cardinality_strategy)
def test_fm::cardinality_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=fm::Cardinality_strategy)
def test_fm::cardinality_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=fm::Cardinality_strategy)
def test_fm::cardinality_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=OrFeature_strategy)
@settings(max_examples=50)
def test_orfeature_instantiation(instance):
    assert isinstance(instance, OrFeature)

@given(instance=fm::XorFeature_strategy)
@settings(max_examples=50)
def test_fm::xorfeature_instantiation(instance):
    assert isinstance(instance, fm::XorFeature)

@given(instance=fm::GroupCardinality_strategy)
@settings(max_examples=50)
def test_fm::groupcardinality_instantiation(instance):
    assert isinstance(instance, fm::GroupCardinality)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=fm::OrOperator_strategy)
@settings(max_examples=50)
def test_fm::oroperator_instantiation(instance):
    assert isinstance(instance, fm::OrOperator)

@given(instance=fm::AndOperator_strategy)
@settings(max_examples=50)
def test_fm::andoperator_instantiation(instance):
    assert isinstance(instance, fm::AndOperator)

@given(instance=fm::Operator_strategy)
@settings(max_examples=50)
def test_fm::operator_instantiation(instance):
    assert isinstance(instance, fm::Operator)

@given(instance=fm::Operation_strategy)
@settings(max_examples=50)
def test_fm::operation_instantiation(instance):
    assert isinstance(instance, fm::Operation)

@given(instance=fm::Operation_strategy)
def test_fm::operation_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fm::Operation_strategy)
def test_fm::operation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Constraints_strategy)
@settings(max_examples=50)
def test_constraints_instantiation(instance):
    assert isinstance(instance, Constraints)

@given(instance=fm::BooleanConstraints_strategy)
@settings(max_examples=50)
def test_fm::booleanconstraints_instantiation(instance):
    assert isinstance(instance, fm::BooleanConstraints)

@given(instance=fm::CardExConstraint_strategy)
@settings(max_examples=50)
def test_fm::cardexconstraint_instantiation(instance):
    assert isinstance(instance, fm::CardExConstraint)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=fm::OrFeature_strategy)
@settings(max_examples=50)
def test_fm::orfeature_instantiation(instance):
    assert isinstance(instance, fm::OrFeature)

@given(instance=fm::Attribute_strategy)
@settings(max_examples=50)
def test_fm::attribute_instantiation(instance):
    assert isinstance(instance, fm::Attribute)

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fm::Attribute_strategy)
def test_fm::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fm::Attribute_strategy)
def test_fm::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fm::FeatureCardinality_strategy)
@settings(max_examples=50)
def test_fm::featurecardinality_instantiation(instance):
    assert isinstance(instance, fm::FeatureCardinality)

@given(instance=fm::Constraints_strategy)
@settings(max_examples=50)
def test_fm::constraints_instantiation(instance):
    assert isinstance(instance, fm::Constraints)

@given(instance=fm::Feature_strategy)
@settings(max_examples=50)
def test_fm::feature_instantiation(instance):
    assert isinstance(instance, fm::Feature)

@given(instance=fm::Feature_strategy)
def test_fm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fm::Feature_strategy)
def test_fm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fm::FeatureModel_strategy)
@settings(max_examples=50)
def test_fm::featuremodel_instantiation(instance):
    assert isinstance(instance, fm::FeatureModel)
