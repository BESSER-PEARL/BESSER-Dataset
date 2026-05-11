import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExpression,
    feature::AndExpression,
    UnaryExpression,
    feature::NotExpression,
    AtomicExpression,
    feature::FeatureReference,
    AttributeOperand,
    feature::AttributeValueLiteral,
    feature::AttributeReference,
    feature::AttributeOperand,
    feature::AttributeComparisonExpression,
    feature::NestedExpression,
    feature::ExcludesExpression,
    feature::ImpliesExpression,
    feature::OrExpression,
    feature::Attribute,
    Expression,
    feature::AtomicExpression,
    feature::BinaryExpression,
    feature::UnaryExpression,
    feature::Expression,
    feature::Identifiable,
    feature::Interval,
    Domain,
    feature::ContinuousDomain,
    feature::DiscreteDomain,
    Identifiable,
    feature::Group,
    feature::Constraint,
    feature::Domain,
    feature::Feature,
    feature::FeatureModel,
    AttributeComparisonOperator,
    SelectedState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::andexpression_is_not_abstract():
    assert not inspect.isabstract(feature::AndExpression)


def test_feature::andexpression_constructor_exists():
    assert callable(feature::AndExpression.__init__)


def test_feature::andexpression_constructor_args():
    sig = inspect.signature(feature::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::notexpression_is_not_abstract():
    assert not inspect.isabstract(feature::NotExpression)


def test_feature::notexpression_constructor_exists():
    assert callable(feature::NotExpression.__init__)


def test_feature::notexpression_constructor_args():
    sig = inspect.signature(feature::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicExpression)


def test_atomicexpression_constructor_exists():
    assert callable(AtomicExpression.__init__)


def test_atomicexpression_constructor_args():
    sig = inspect.signature(AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::featurereference_is_not_abstract():
    assert not inspect.isabstract(feature::FeatureReference)


def test_feature::featurereference_constructor_exists():
    assert callable(feature::FeatureReference.__init__)


def test_feature::featurereference_constructor_args():
    sig = inspect.signature(feature::FeatureReference.__init__)
    params = list(sig.parameters.keys())



def test_attributeoperand_is_not_abstract():
    assert not inspect.isabstract(AttributeOperand)


def test_attributeoperand_constructor_exists():
    assert callable(AttributeOperand.__init__)


def test_attributeoperand_constructor_args():
    sig = inspect.signature(AttributeOperand.__init__)
    params = list(sig.parameters.keys())



def test_feature::attributevalueliteral_is_not_abstract():
    assert not inspect.isabstract(feature::AttributeValueLiteral)


def test_feature::attributevalueliteral_constructor_exists():
    assert callable(feature::AttributeValueLiteral.__init__)


def test_feature::attributevalueliteral_constructor_args():
    sig = inspect.signature(feature::AttributeValueLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_feature::attributevalueliteral_has_value():
    assert hasattr(feature::AttributeValueLiteral, "value")
    descriptor = None
    for klass in feature::AttributeValueLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_feature::attributereference_is_not_abstract():
    assert not inspect.isabstract(feature::AttributeReference)


def test_feature::attributereference_constructor_exists():
    assert callable(feature::AttributeReference.__init__)


def test_feature::attributereference_constructor_args():
    sig = inspect.signature(feature::AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_feature::attributeoperand_is_not_abstract():
    assert not inspect.isabstract(feature::AttributeOperand)


def test_feature::attributeoperand_constructor_exists():
    assert callable(feature::AttributeOperand.__init__)


def test_feature::attributeoperand_constructor_args():
    sig = inspect.signature(feature::AttributeOperand.__init__)
    params = list(sig.parameters.keys())



def test_feature::attributecomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(feature::AttributeComparisonExpression)


def test_feature::attributecomparisonexpression_constructor_exists():
    assert callable(feature::AttributeComparisonExpression.__init__)


def test_feature::attributecomparisonexpression_constructor_args():
    sig = inspect.signature(feature::AttributeComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_feature::attributecomparisonexpression_has_operator():
    assert hasattr(feature::AttributeComparisonExpression, "operator")
    descriptor = None
    for klass in feature::AttributeComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_feature::nestedexpression_is_not_abstract():
    assert not inspect.isabstract(feature::NestedExpression)


def test_feature::nestedexpression_constructor_exists():
    assert callable(feature::NestedExpression.__init__)


def test_feature::nestedexpression_constructor_args():
    sig = inspect.signature(feature::NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::excludesexpression_is_not_abstract():
    assert not inspect.isabstract(feature::ExcludesExpression)


def test_feature::excludesexpression_constructor_exists():
    assert callable(feature::ExcludesExpression.__init__)


def test_feature::excludesexpression_constructor_args():
    sig = inspect.signature(feature::ExcludesExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::impliesexpression_is_not_abstract():
    assert not inspect.isabstract(feature::ImpliesExpression)


def test_feature::impliesexpression_constructor_exists():
    assert callable(feature::ImpliesExpression.__init__)


def test_feature::impliesexpression_constructor_args():
    sig = inspect.signature(feature::ImpliesExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::orexpression_is_not_abstract():
    assert not inspect.isabstract(feature::OrExpression)


def test_feature::orexpression_constructor_exists():
    assert callable(feature::OrExpression.__init__)


def test_feature::orexpression_constructor_args():
    sig = inspect.signature(feature::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::attribute_is_not_abstract():
    assert not inspect.isabstract(feature::Attribute)


def test_feature::attribute_constructor_exists():
    assert callable(feature::Attribute.__init__)


def test_feature::attribute_constructor_args():
    sig = inspect.signature(feature::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_feature::attribute_has_name():
    assert hasattr(feature::Attribute, "name")
    descriptor = None
    for klass in feature::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_feature::atomicexpression_is_not_abstract():
    assert not inspect.isabstract(feature::AtomicExpression)


def test_feature::atomicexpression_constructor_exists():
    assert callable(feature::AtomicExpression.__init__)


def test_feature::atomicexpression_constructor_args():
    sig = inspect.signature(feature::AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(feature::BinaryExpression)


def test_feature::binaryexpression_constructor_exists():
    assert callable(feature::BinaryExpression.__init__)


def test_feature::binaryexpression_constructor_args():
    sig = inspect.signature(feature::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(feature::UnaryExpression)


def test_feature::unaryexpression_constructor_exists():
    assert callable(feature::UnaryExpression.__init__)


def test_feature::unaryexpression_constructor_args():
    sig = inspect.signature(feature::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature::expression_is_not_abstract():
    assert not inspect.isabstract(feature::Expression)


def test_feature::expression_constructor_exists():
    assert callable(feature::Expression.__init__)


def test_feature::expression_constructor_args():
    sig = inspect.signature(feature::Expression.__init__)
    params = list(sig.parameters.keys())



def test_feature::identifiable_is_not_abstract():
    assert not inspect.isabstract(feature::Identifiable)


def test_feature::identifiable_constructor_exists():
    assert callable(feature::Identifiable.__init__)


def test_feature::identifiable_constructor_args():
    sig = inspect.signature(feature::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_feature::identifiable_has_id():
    assert hasattr(feature::Identifiable, "id")
    descriptor = None
    for klass in feature::Identifiable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_feature::interval_is_not_abstract():
    assert not inspect.isabstract(feature::Interval)


def test_feature::interval_constructor_exists():
    assert callable(feature::Interval.__init__)


def test_feature::interval_constructor_args():
    sig = inspect.signature(feature::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_feature::interval_has_lowerBound():
    assert hasattr(feature::Interval, "lowerBound")
    descriptor = None
    for klass in feature::Interval.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_feature::interval_has_upperBound():
    assert hasattr(feature::Interval, "upperBound")
    descriptor = None
    for klass in feature::Interval.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_feature::continuousdomain_is_not_abstract():
    assert not inspect.isabstract(feature::ContinuousDomain)


def test_feature::continuousdomain_constructor_exists():
    assert callable(feature::ContinuousDomain.__init__)


def test_feature::continuousdomain_constructor_args():
    sig = inspect.signature(feature::ContinuousDomain.__init__)
    params = list(sig.parameters.keys())



def test_feature::discretedomain_is_not_abstract():
    assert not inspect.isabstract(feature::DiscreteDomain)


def test_feature::discretedomain_constructor_exists():
    assert callable(feature::DiscreteDomain.__init__)


def test_feature::discretedomain_constructor_args():
    sig = inspect.signature(feature::DiscreteDomain.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_feature::discretedomain_has_values():
    assert hasattr(feature::DiscreteDomain, "values")
    descriptor = None
    for klass in feature::DiscreteDomain.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_feature::group_is_not_abstract():
    assert not inspect.isabstract(feature::Group)


def test_feature::group_constructor_exists():
    assert callable(feature::Group.__init__)


def test_feature::group_constructor_args():
    sig = inspect.signature(feature::Group.__init__)
    params = list(sig.parameters.keys())
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"

def test_feature::group_has_maxCardinality():
    assert hasattr(feature::Group, "maxCardinality")
    descriptor = None
    for klass in feature::Group.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)

def test_feature::group_has_minCardinality():
    assert hasattr(feature::Group, "minCardinality")
    descriptor = None
    for klass in feature::Group.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)



def test_feature::constraint_is_not_abstract():
    assert not inspect.isabstract(feature::Constraint)


def test_feature::constraint_constructor_exists():
    assert callable(feature::Constraint.__init__)


def test_feature::constraint_constructor_args():
    sig = inspect.signature(feature::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_feature::domain_is_not_abstract():
    assert not inspect.isabstract(feature::Domain)


def test_feature::domain_constructor_exists():
    assert callable(feature::Domain.__init__)


def test_feature::domain_constructor_args():
    sig = inspect.signature(feature::Domain.__init__)
    params = list(sig.parameters.keys())



def test_feature::feature_is_not_abstract():
    assert not inspect.isabstract(feature::Feature)


def test_feature::feature_constructor_exists():
    assert callable(feature::Feature.__init__)


def test_feature::feature_constructor_args():
    sig = inspect.signature(feature::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_feature::feature_has_name():
    assert hasattr(feature::Feature, "name")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_feature::feature_has_selected():
    assert hasattr(feature::Feature, "selected")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
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

def test_attributecomparisonoperator_exists():
    # Check that the Enumeration exists
    assert AttributeComparisonOperator is not None

def test_attributecomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeComparisonOperator]
    expected_literals = [
        "lessThan",
        "greaterThan",
        "equal",
        "unequal",
        "lessThanOrEqual",
        "greaterThanOrEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeComparisonOperator"

def test_selectedstate_exists():
    # Check that the Enumeration exists
    assert SelectedState is not None

def test_selectedstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectedState]
    expected_literals = [
        "undetermined",
        "deselected",
        "selected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectedState"


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
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
feature::AndExpression_strategy = st.builds(
    feature::AndExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
feature::NotExpression_strategy = st.builds(
    feature::NotExpression,
)
AtomicExpression_strategy = st.builds(
    AtomicExpression,
)
feature::FeatureReference_strategy = st.builds(
    feature::FeatureReference,
)
AttributeOperand_strategy = st.builds(
    AttributeOperand,
)
feature::AttributeValueLiteral_strategy = st.builds(
    feature::AttributeValueLiteral,
    value=
        safe_text
)
feature::AttributeReference_strategy = st.builds(
    feature::AttributeReference,
)
feature::AttributeOperand_strategy = st.builds(
    feature::AttributeOperand,
)
feature::AttributeComparisonExpression_strategy = st.builds(
    feature::AttributeComparisonExpression,
    operator=
        safe_text
)
feature::NestedExpression_strategy = st.builds(
    feature::NestedExpression,
)
feature::ExcludesExpression_strategy = st.builds(
    feature::ExcludesExpression,
)
feature::ImpliesExpression_strategy = st.builds(
    feature::ImpliesExpression,
)
feature::OrExpression_strategy = st.builds(
    feature::OrExpression,
)
feature::Attribute_strategy = st.builds(
    feature::Attribute,
    name=
        safe_text,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
feature::AtomicExpression_strategy = st.builds(
    feature::AtomicExpression,
)
feature::BinaryExpression_strategy = st.builds(
    feature::BinaryExpression,
)
feature::UnaryExpression_strategy = st.builds(
    feature::UnaryExpression,
)
feature::Expression_strategy = st.builds(
    feature::Expression,
)
feature::Identifiable_strategy = st.builds(
    feature::Identifiable,
    id=
        safe_text
)
feature::Interval_strategy = st.builds(
    feature::Interval,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
Domain_strategy = st.builds(
    Domain,
)
feature::ContinuousDomain_strategy = st.builds(
    feature::ContinuousDomain,
)
feature::DiscreteDomain_strategy = st.builds(
    feature::DiscreteDomain,
    values=
        safe_text
)
Identifiable_strategy = st.builds(
    Identifiable,
)
feature::Group_strategy = st.builds(
    feature::Group,
    maxCardinality=
        st.integers(),
    minCardinality=
        st.integers()
)
feature::Constraint_strategy = st.builds(
    feature::Constraint,
)
feature::Domain_strategy = st.builds(
    feature::Domain,
)
feature::Feature_strategy = st.builds(
    feature::Feature,
    name=
        safe_text,
    selected=
        safe_text
)
feature::FeatureModel_strategy = st.builds(
    feature::FeatureModel,
    name=
        safe_text
)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=feature::AndExpression_strategy)
@settings(max_examples=50)
def test_feature::andexpression_instantiation(instance):
    assert isinstance(instance, feature::AndExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=feature::NotExpression_strategy)
@settings(max_examples=50)
def test_feature::notexpression_instantiation(instance):
    assert isinstance(instance, feature::NotExpression)

@given(instance=AtomicExpression_strategy)
@settings(max_examples=50)
def test_atomicexpression_instantiation(instance):
    assert isinstance(instance, AtomicExpression)

@given(instance=feature::FeatureReference_strategy)
@settings(max_examples=50)
def test_feature::featurereference_instantiation(instance):
    assert isinstance(instance, feature::FeatureReference)

@given(instance=AttributeOperand_strategy)
@settings(max_examples=50)
def test_attributeoperand_instantiation(instance):
    assert isinstance(instance, AttributeOperand)

@given(instance=feature::AttributeValueLiteral_strategy)
@settings(max_examples=50)
def test_feature::attributevalueliteral_instantiation(instance):
    assert isinstance(instance, feature::AttributeValueLiteral)

@given(instance=feature::AttributeValueLiteral_strategy)
def test_feature::attributevalueliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=feature::AttributeValueLiteral_strategy)
def test_feature::attributevalueliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=feature::AttributeReference_strategy)
@settings(max_examples=50)
def test_feature::attributereference_instantiation(instance):
    assert isinstance(instance, feature::AttributeReference)

@given(instance=feature::AttributeOperand_strategy)
@settings(max_examples=50)
def test_feature::attributeoperand_instantiation(instance):
    assert isinstance(instance, feature::AttributeOperand)

@given(instance=feature::AttributeComparisonExpression_strategy)
@settings(max_examples=50)
def test_feature::attributecomparisonexpression_instantiation(instance):
    assert isinstance(instance, feature::AttributeComparisonExpression)

@given(instance=feature::AttributeComparisonExpression_strategy)
def test_feature::attributecomparisonexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=feature::AttributeComparisonExpression_strategy)
def test_feature::attributecomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=feature::NestedExpression_strategy)
@settings(max_examples=50)
def test_feature::nestedexpression_instantiation(instance):
    assert isinstance(instance, feature::NestedExpression)

@given(instance=feature::ExcludesExpression_strategy)
@settings(max_examples=50)
def test_feature::excludesexpression_instantiation(instance):
    assert isinstance(instance, feature::ExcludesExpression)

@given(instance=feature::ImpliesExpression_strategy)
@settings(max_examples=50)
def test_feature::impliesexpression_instantiation(instance):
    assert isinstance(instance, feature::ImpliesExpression)

@given(instance=feature::OrExpression_strategy)
@settings(max_examples=50)
def test_feature::orexpression_instantiation(instance):
    assert isinstance(instance, feature::OrExpression)

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
def test_feature::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=feature::Attribute_strategy)
def test_feature::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=feature::AtomicExpression_strategy)
@settings(max_examples=50)
def test_feature::atomicexpression_instantiation(instance):
    assert isinstance(instance, feature::AtomicExpression)

@given(instance=feature::BinaryExpression_strategy)
@settings(max_examples=50)
def test_feature::binaryexpression_instantiation(instance):
    assert isinstance(instance, feature::BinaryExpression)

@given(instance=feature::UnaryExpression_strategy)
@settings(max_examples=50)
def test_feature::unaryexpression_instantiation(instance):
    assert isinstance(instance, feature::UnaryExpression)

@given(instance=feature::Expression_strategy)
@settings(max_examples=50)
def test_feature::expression_instantiation(instance):
    assert isinstance(instance, feature::Expression)

@given(instance=feature::Identifiable_strategy)
@settings(max_examples=50)
def test_feature::identifiable_instantiation(instance):
    assert isinstance(instance, feature::Identifiable)

@given(instance=feature::Identifiable_strategy)
def test_feature::identifiable_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=feature::Identifiable_strategy)
def test_feature::identifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=feature::Interval_strategy)
@settings(max_examples=50)
def test_feature::interval_instantiation(instance):
    assert isinstance(instance, feature::Interval)

@given(instance=feature::Interval_strategy)
def test_feature::interval_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=feature::Interval_strategy)
def test_feature::interval_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=feature::Interval_strategy)
def test_feature::interval_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=feature::Interval_strategy)
def test_feature::interval_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=feature::ContinuousDomain_strategy)
@settings(max_examples=50)
def test_feature::continuousdomain_instantiation(instance):
    assert isinstance(instance, feature::ContinuousDomain)

@given(instance=feature::DiscreteDomain_strategy)
@settings(max_examples=50)
def test_feature::discretedomain_instantiation(instance):
    assert isinstance(instance, feature::DiscreteDomain)

@given(instance=feature::DiscreteDomain_strategy)
def test_feature::discretedomain_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=feature::DiscreteDomain_strategy)
def test_feature::discretedomain_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=feature::Group_strategy)
@settings(max_examples=50)
def test_feature::group_instantiation(instance):
    assert isinstance(instance, feature::Group)

@given(instance=feature::Group_strategy)
def test_feature::group_maxCardinality_type(instance):
    assert isinstance(instance.maxCardinality, int)


@given(instance=feature::Group_strategy)
def test_feature::group_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original

@given(instance=feature::Group_strategy)
def test_feature::group_minCardinality_type(instance):
    assert isinstance(instance.minCardinality, int)


@given(instance=feature::Group_strategy)
def test_feature::group_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=feature::Constraint_strategy)
@settings(max_examples=50)
def test_feature::constraint_instantiation(instance):
    assert isinstance(instance, feature::Constraint)

@given(instance=feature::Domain_strategy)
@settings(max_examples=50)
def test_feature::domain_instantiation(instance):
    assert isinstance(instance, feature::Domain)

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

@given(instance=feature::Feature_strategy)
def test_feature::feature_selected_type(instance):
    assert isinstance(instance.selected, str)


@given(instance=feature::Feature_strategy)
def test_feature::feature_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

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
