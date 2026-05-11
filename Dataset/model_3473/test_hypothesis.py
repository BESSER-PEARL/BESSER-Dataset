import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EFM::NodeFeatureElement,
    NodeFeatureElement,
    EFM::IntValue,
    Operation,
    EFM::ValueOperation,
    EFM::RangeOperation,
    EFM::Operation,
    BooleanConstraint,
    EFM::Excludes,
    EFM::Implies,
    Cardinality,
    FMConstraint,
    EFM::Comparison,
    EFM::Requires,
    EFM::Separated,
    EFM::HostedBy,
    EFM::NotHostedBy,
    EFM::Functional,
    EFM::Colocated,
    EFM::ResourceVerification,
    EFM::BooleanConstraint,
    EFM::Value,
    EFM::Cardinality,
    Feature,
    EFM::Alternative,
    Alternative,
    EFM::Exclusive,
    EFM::NodeFeature,
    EFM::FeatCardinality,
    FMElement,
    EFM::Attribute,
    EFM::FMElement,
    EFM::Feature,
    EFM::FMConstraint,
    EFM::FeatureModel,
    LogicalOperator,
    Operator,
    ComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_efm::nodefeatureelement_is_not_abstract():
    assert not inspect.isabstract(EFM::NodeFeatureElement)


def test_efm::nodefeatureelement_constructor_exists():
    assert callable(EFM::NodeFeatureElement.__init__)


def test_efm::nodefeatureelement_constructor_args():
    sig = inspect.signature(EFM::NodeFeatureElement.__init__)
    params = list(sig.parameters.keys())



def test_nodefeatureelement_is_not_abstract():
    assert not inspect.isabstract(NodeFeatureElement)


def test_nodefeatureelement_constructor_exists():
    assert callable(NodeFeatureElement.__init__)


def test_nodefeatureelement_constructor_args():
    sig = inspect.signature(NodeFeatureElement.__init__)
    params = list(sig.parameters.keys())



def test_efm::intvalue_is_not_abstract():
    assert not inspect.isabstract(EFM::IntValue)


def test_efm::intvalue_constructor_exists():
    assert callable(EFM::IntValue.__init__)


def test_efm::intvalue_constructor_args():
    sig = inspect.signature(EFM::IntValue.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_efm::valueoperation_is_not_abstract():
    assert not inspect.isabstract(EFM::ValueOperation)


def test_efm::valueoperation_constructor_exists():
    assert callable(EFM::ValueOperation.__init__)


def test_efm::valueoperation_constructor_args():
    sig = inspect.signature(EFM::ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_efm::rangeoperation_is_not_abstract():
    assert not inspect.isabstract(EFM::RangeOperation)


def test_efm::rangeoperation_constructor_exists():
    assert callable(EFM::RangeOperation.__init__)


def test_efm::rangeoperation_constructor_args():
    sig = inspect.signature(EFM::RangeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_efm::rangeoperation_has_min():
    assert hasattr(EFM::RangeOperation, "min")
    descriptor = None
    for klass in EFM::RangeOperation.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_efm::rangeoperation_has_max():
    assert hasattr(EFM::RangeOperation, "max")
    descriptor = None
    for klass in EFM::RangeOperation.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_efm::operation_is_not_abstract():
    assert not inspect.isabstract(EFM::Operation)


def test_efm::operation_constructor_exists():
    assert callable(EFM::Operation.__init__)


def test_efm::operation_constructor_args():
    sig = inspect.signature(EFM::Operation.__init__)
    params = list(sig.parameters.keys())



def test_booleanconstraint_is_not_abstract():
    assert not inspect.isabstract(BooleanConstraint)


def test_booleanconstraint_constructor_exists():
    assert callable(BooleanConstraint.__init__)


def test_booleanconstraint_constructor_args():
    sig = inspect.signature(BooleanConstraint.__init__)
    params = list(sig.parameters.keys())



def test_efm::excludes_is_not_abstract():
    assert not inspect.isabstract(EFM::Excludes)


def test_efm::excludes_constructor_exists():
    assert callable(EFM::Excludes.__init__)


def test_efm::excludes_constructor_args():
    sig = inspect.signature(EFM::Excludes.__init__)
    params = list(sig.parameters.keys())



def test_efm::implies_is_not_abstract():
    assert not inspect.isabstract(EFM::Implies)


def test_efm::implies_constructor_exists():
    assert callable(EFM::Implies.__init__)


def test_efm::implies_constructor_args():
    sig = inspect.signature(EFM::Implies.__init__)
    params = list(sig.parameters.keys())



def test_cardinality_is_not_abstract():
    assert not inspect.isabstract(Cardinality)


def test_cardinality_constructor_exists():
    assert callable(Cardinality.__init__)


def test_cardinality_constructor_args():
    sig = inspect.signature(Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_fmconstraint_is_not_abstract():
    assert not inspect.isabstract(FMConstraint)


def test_fmconstraint_constructor_exists():
    assert callable(FMConstraint.__init__)


def test_fmconstraint_constructor_args():
    sig = inspect.signature(FMConstraint.__init__)
    params = list(sig.parameters.keys())



def test_efm::comparison_is_not_abstract():
    assert not inspect.isabstract(EFM::Comparison)


def test_efm::comparison_constructor_exists():
    assert callable(EFM::Comparison.__init__)


def test_efm::comparison_constructor_args():
    sig = inspect.signature(EFM::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_efm::comparison_has_type():
    assert hasattr(EFM::Comparison, "type")
    descriptor = None
    for klass in EFM::Comparison.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_efm::requires_is_not_abstract():
    assert not inspect.isabstract(EFM::Requires)


def test_efm::requires_constructor_exists():
    assert callable(EFM::Requires.__init__)


def test_efm::requires_constructor_args():
    sig = inspect.signature(EFM::Requires.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_efm::requires_has_operator():
    assert hasattr(EFM::Requires, "operator")
    descriptor = None
    for klass in EFM::Requires.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_efm::separated_is_not_abstract():
    assert not inspect.isabstract(EFM::Separated)


def test_efm::separated_constructor_exists():
    assert callable(EFM::Separated.__init__)


def test_efm::separated_constructor_args():
    sig = inspect.signature(EFM::Separated.__init__)
    params = list(sig.parameters.keys())



def test_efm::hostedby_is_not_abstract():
    assert not inspect.isabstract(EFM::HostedBy)


def test_efm::hostedby_constructor_exists():
    assert callable(EFM::HostedBy.__init__)


def test_efm::hostedby_constructor_args():
    sig = inspect.signature(EFM::HostedBy.__init__)
    params = list(sig.parameters.keys())



def test_efm::nothostedby_is_not_abstract():
    assert not inspect.isabstract(EFM::NotHostedBy)


def test_efm::nothostedby_constructor_exists():
    assert callable(EFM::NotHostedBy.__init__)


def test_efm::nothostedby_constructor_args():
    sig = inspect.signature(EFM::NotHostedBy.__init__)
    params = list(sig.parameters.keys())



def test_efm::functional_is_not_abstract():
    assert not inspect.isabstract(EFM::Functional)


def test_efm::functional_constructor_exists():
    assert callable(EFM::Functional.__init__)


def test_efm::functional_constructor_args():
    sig = inspect.signature(EFM::Functional.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_efm::functional_has_value():
    assert hasattr(EFM::Functional, "value")
    descriptor = None
    for klass in EFM::Functional.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_efm::functional_has_type():
    assert hasattr(EFM::Functional, "type")
    descriptor = None
    for klass in EFM::Functional.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_efm::colocated_is_not_abstract():
    assert not inspect.isabstract(EFM::Colocated)


def test_efm::colocated_constructor_exists():
    assert callable(EFM::Colocated.__init__)


def test_efm::colocated_constructor_args():
    sig = inspect.signature(EFM::Colocated.__init__)
    params = list(sig.parameters.keys())



def test_efm::resourceverification_is_not_abstract():
    assert not inspect.isabstract(EFM::ResourceVerification)


def test_efm::resourceverification_constructor_exists():
    assert callable(EFM::ResourceVerification.__init__)


def test_efm::resourceverification_constructor_args():
    sig = inspect.signature(EFM::ResourceVerification.__init__)
    params = list(sig.parameters.keys())



def test_efm::booleanconstraint_is_not_abstract():
    assert not inspect.isabstract(EFM::BooleanConstraint)


def test_efm::booleanconstraint_constructor_exists():
    assert callable(EFM::BooleanConstraint.__init__)


def test_efm::booleanconstraint_constructor_args():
    sig = inspect.signature(EFM::BooleanConstraint.__init__)
    params = list(sig.parameters.keys())



def test_efm::value_is_not_abstract():
    assert not inspect.isabstract(EFM::Value)


def test_efm::value_constructor_exists():
    assert callable(EFM::Value.__init__)


def test_efm::value_constructor_args():
    sig = inspect.signature(EFM::Value.__init__)
    params = list(sig.parameters.keys())



def test_efm::cardinality_is_not_abstract():
    assert not inspect.isabstract(EFM::Cardinality)


def test_efm::cardinality_constructor_exists():
    assert callable(EFM::Cardinality.__init__)


def test_efm::cardinality_constructor_args():
    sig = inspect.signature(EFM::Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinalityMax" in params, "Missing parameter 'cardinalityMax'"
    assert "cardinalityMin" in params, "Missing parameter 'cardinalityMin'"
    assert "configValue" in params, "Missing parameter 'configValue'"

def test_efm::cardinality_has_cardinalityMax():
    assert hasattr(EFM::Cardinality, "cardinalityMax")
    descriptor = None
    for klass in EFM::Cardinality.__mro__:
        if "cardinalityMax" in klass.__dict__:
            descriptor = klass.__dict__["cardinalityMax"]
            break
    assert isinstance(descriptor, property)

def test_efm::cardinality_has_cardinalityMin():
    assert hasattr(EFM::Cardinality, "cardinalityMin")
    descriptor = None
    for klass in EFM::Cardinality.__mro__:
        if "cardinalityMin" in klass.__dict__:
            descriptor = klass.__dict__["cardinalityMin"]
            break
    assert isinstance(descriptor, property)

def test_efm::cardinality_has_configValue():
    assert hasattr(EFM::Cardinality, "configValue")
    descriptor = None
    for klass in EFM::Cardinality.__mro__:
        if "configValue" in klass.__dict__:
            descriptor = klass.__dict__["configValue"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_efm::alternative_is_not_abstract():
    assert not inspect.isabstract(EFM::Alternative)


def test_efm::alternative_constructor_exists():
    assert callable(EFM::Alternative.__init__)


def test_efm::alternative_constructor_args():
    sig = inspect.signature(EFM::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_alternative_is_not_abstract():
    assert not inspect.isabstract(Alternative)


def test_alternative_constructor_exists():
    assert callable(Alternative.__init__)


def test_alternative_constructor_args():
    sig = inspect.signature(Alternative.__init__)
    params = list(sig.parameters.keys())



def test_efm::exclusive_is_not_abstract():
    assert not inspect.isabstract(EFM::Exclusive)


def test_efm::exclusive_constructor_exists():
    assert callable(EFM::Exclusive.__init__)


def test_efm::exclusive_constructor_args():
    sig = inspect.signature(EFM::Exclusive.__init__)
    params = list(sig.parameters.keys())



def test_efm::nodefeature_is_not_abstract():
    assert not inspect.isabstract(EFM::NodeFeature)


def test_efm::nodefeature_constructor_exists():
    assert callable(EFM::NodeFeature.__init__)


def test_efm::nodefeature_constructor_args():
    sig = inspect.signature(EFM::NodeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efm::nodefeature_has_name():
    assert hasattr(EFM::NodeFeature, "name")
    descriptor = None
    for klass in EFM::NodeFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efm::featcardinality_is_not_abstract():
    assert not inspect.isabstract(EFM::FeatCardinality)


def test_efm::featcardinality_constructor_exists():
    assert callable(EFM::FeatCardinality.__init__)


def test_efm::featcardinality_constructor_args():
    sig = inspect.signature(EFM::FeatCardinality.__init__)
    params = list(sig.parameters.keys())



def test_fmelement_is_not_abstract():
    assert not inspect.isabstract(FMElement)


def test_fmelement_constructor_exists():
    assert callable(FMElement.__init__)


def test_fmelement_constructor_args():
    sig = inspect.signature(FMElement.__init__)
    params = list(sig.parameters.keys())



def test_efm::attribute_is_not_abstract():
    assert not inspect.isabstract(EFM::Attribute)


def test_efm::attribute_constructor_exists():
    assert callable(EFM::Attribute.__init__)


def test_efm::attribute_constructor_args():
    sig = inspect.signature(EFM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efm::attribute_has_name():
    assert hasattr(EFM::Attribute, "name")
    descriptor = None
    for klass in EFM::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efm::fmelement_is_not_abstract():
    assert not inspect.isabstract(EFM::FMElement)


def test_efm::fmelement_constructor_exists():
    assert callable(EFM::FMElement.__init__)


def test_efm::fmelement_constructor_args():
    sig = inspect.signature(EFM::FMElement.__init__)
    params = list(sig.parameters.keys())



def test_efm::feature_is_not_abstract():
    assert not inspect.isabstract(EFM::Feature)


def test_efm::feature_constructor_exists():
    assert callable(EFM::Feature.__init__)


def test_efm::feature_constructor_args():
    sig = inspect.signature(EFM::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efm::feature_has_name():
    assert hasattr(EFM::Feature, "name")
    descriptor = None
    for klass in EFM::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efm::fmconstraint_is_not_abstract():
    assert not inspect.isabstract(EFM::FMConstraint)


def test_efm::fmconstraint_constructor_exists():
    assert callable(EFM::FMConstraint.__init__)


def test_efm::fmconstraint_constructor_args():
    sig = inspect.signature(EFM::FMConstraint.__init__)
    params = list(sig.parameters.keys())



def test_efm::featuremodel_is_not_abstract():
    assert not inspect.isabstract(EFM::FeatureModel)


def test_efm::featuremodel_constructor_exists():
    assert callable(EFM::FeatureModel.__init__)


def test_efm::featuremodel_constructor_args():
    sig = inspect.signature(EFM::FeatureModel.__init__)
    params = list(sig.parameters.keys())

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "or_",
        "and_",
        "void",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "remove",
        "divide",
        "multiply",
        "add",
        "select",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "lt",
        "equal",
        "gt",
        "leq",
        "geq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"


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
EFM::NodeFeatureElement_strategy = st.builds(
    EFM::NodeFeatureElement,
)
NodeFeatureElement_strategy = st.builds(
    NodeFeatureElement,
)
EFM::IntValue_strategy = st.builds(
    EFM::IntValue,
)
Operation_strategy = st.builds(
    Operation,
)
EFM::ValueOperation_strategy = st.builds(
    EFM::ValueOperation,
)
EFM::RangeOperation_strategy = st.builds(
    EFM::RangeOperation,
    min=
        st.integers(),
    max=
        st.integers()
)
EFM::Operation_strategy = st.builds(
    EFM::Operation,
)
BooleanConstraint_strategy = st.builds(
    BooleanConstraint,
)
EFM::Excludes_strategy = st.builds(
    EFM::Excludes,
)
EFM::Implies_strategy = st.builds(
    EFM::Implies,
)
Cardinality_strategy = st.builds(
    Cardinality,
)
FMConstraint_strategy = st.builds(
    FMConstraint,
)
EFM::Comparison_strategy = st.builds(
    EFM::Comparison,
    type=
        safe_text
)
EFM::Requires_strategy = st.builds(
    EFM::Requires,
    operator=
        safe_text
)
EFM::Separated_strategy = st.builds(
    EFM::Separated,
)
EFM::HostedBy_strategy = st.builds(
    EFM::HostedBy,
)
EFM::NotHostedBy_strategy = st.builds(
    EFM::NotHostedBy,
)
EFM::Functional_strategy = st.builds(
    EFM::Functional,
    value=
        st.integers(),
    type=
        safe_text
)
EFM::Colocated_strategy = st.builds(
    EFM::Colocated,
)
EFM::ResourceVerification_strategy = st.builds(
    EFM::ResourceVerification,
)
EFM::BooleanConstraint_strategy = st.builds(
    EFM::BooleanConstraint,
)
EFM::Value_strategy = st.builds(
    EFM::Value,
)
EFM::Cardinality_strategy = st.builds(
    EFM::Cardinality,
    cardinalityMax=
        st.integers(),
    cardinalityMin=
        st.integers(),
    configValue=
        st.integers()
)
Feature_strategy = st.builds(
    Feature,
)
EFM::Alternative_strategy = st.builds(
    EFM::Alternative,
)
Alternative_strategy = st.builds(
    Alternative,
)
EFM::Exclusive_strategy = st.builds(
    EFM::Exclusive,
)
EFM::NodeFeature_strategy = st.builds(
    EFM::NodeFeature,
    name=
        safe_text
)
EFM::FeatCardinality_strategy = st.builds(
    EFM::FeatCardinality,
)
FMElement_strategy = st.builds(
    FMElement,
)
EFM::Attribute_strategy = st.builds(
    EFM::Attribute,
    name=
        safe_text
)
EFM::FMElement_strategy = st.builds(
    EFM::FMElement,
)
EFM::Feature_strategy = st.builds(
    EFM::Feature,
    name=
        safe_text
)
EFM::FMConstraint_strategy = st.builds(
    EFM::FMConstraint,
)
EFM::FeatureModel_strategy = st.builds(
    EFM::FeatureModel,
)

@given(instance=EFM::NodeFeatureElement_strategy)
@settings(max_examples=50)
def test_efm::nodefeatureelement_instantiation(instance):
    assert isinstance(instance, EFM::NodeFeatureElement)

@given(instance=NodeFeatureElement_strategy)
@settings(max_examples=50)
def test_nodefeatureelement_instantiation(instance):
    assert isinstance(instance, NodeFeatureElement)

@given(instance=EFM::IntValue_strategy)
@settings(max_examples=50)
def test_efm::intvalue_instantiation(instance):
    assert isinstance(instance, EFM::IntValue)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=EFM::ValueOperation_strategy)
@settings(max_examples=50)
def test_efm::valueoperation_instantiation(instance):
    assert isinstance(instance, EFM::ValueOperation)

@given(instance=EFM::RangeOperation_strategy)
@settings(max_examples=50)
def test_efm::rangeoperation_instantiation(instance):
    assert isinstance(instance, EFM::RangeOperation)

@given(instance=EFM::RangeOperation_strategy)
def test_efm::rangeoperation_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=EFM::RangeOperation_strategy)
def test_efm::rangeoperation_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=EFM::RangeOperation_strategy)
def test_efm::rangeoperation_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=EFM::RangeOperation_strategy)
def test_efm::rangeoperation_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=EFM::Operation_strategy)
@settings(max_examples=50)
def test_efm::operation_instantiation(instance):
    assert isinstance(instance, EFM::Operation)

@given(instance=BooleanConstraint_strategy)
@settings(max_examples=50)
def test_booleanconstraint_instantiation(instance):
    assert isinstance(instance, BooleanConstraint)

@given(instance=EFM::Excludes_strategy)
@settings(max_examples=50)
def test_efm::excludes_instantiation(instance):
    assert isinstance(instance, EFM::Excludes)

@given(instance=EFM::Implies_strategy)
@settings(max_examples=50)
def test_efm::implies_instantiation(instance):
    assert isinstance(instance, EFM::Implies)

@given(instance=Cardinality_strategy)
@settings(max_examples=50)
def test_cardinality_instantiation(instance):
    assert isinstance(instance, Cardinality)

@given(instance=FMConstraint_strategy)
@settings(max_examples=50)
def test_fmconstraint_instantiation(instance):
    assert isinstance(instance, FMConstraint)

@given(instance=EFM::Comparison_strategy)
@settings(max_examples=50)
def test_efm::comparison_instantiation(instance):
    assert isinstance(instance, EFM::Comparison)

@given(instance=EFM::Comparison_strategy)
def test_efm::comparison_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=EFM::Comparison_strategy)
def test_efm::comparison_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=EFM::Requires_strategy)
@settings(max_examples=50)
def test_efm::requires_instantiation(instance):
    assert isinstance(instance, EFM::Requires)

@given(instance=EFM::Requires_strategy)
def test_efm::requires_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=EFM::Requires_strategy)
def test_efm::requires_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=EFM::Separated_strategy)
@settings(max_examples=50)
def test_efm::separated_instantiation(instance):
    assert isinstance(instance, EFM::Separated)

@given(instance=EFM::HostedBy_strategy)
@settings(max_examples=50)
def test_efm::hostedby_instantiation(instance):
    assert isinstance(instance, EFM::HostedBy)

@given(instance=EFM::NotHostedBy_strategy)
@settings(max_examples=50)
def test_efm::nothostedby_instantiation(instance):
    assert isinstance(instance, EFM::NotHostedBy)

@given(instance=EFM::Functional_strategy)
@settings(max_examples=50)
def test_efm::functional_instantiation(instance):
    assert isinstance(instance, EFM::Functional)

@given(instance=EFM::Functional_strategy)
def test_efm::functional_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=EFM::Functional_strategy)
def test_efm::functional_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EFM::Functional_strategy)
def test_efm::functional_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=EFM::Functional_strategy)
def test_efm::functional_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=EFM::Colocated_strategy)
@settings(max_examples=50)
def test_efm::colocated_instantiation(instance):
    assert isinstance(instance, EFM::Colocated)

@given(instance=EFM::ResourceVerification_strategy)
@settings(max_examples=50)
def test_efm::resourceverification_instantiation(instance):
    assert isinstance(instance, EFM::ResourceVerification)

@given(instance=EFM::BooleanConstraint_strategy)
@settings(max_examples=50)
def test_efm::booleanconstraint_instantiation(instance):
    assert isinstance(instance, EFM::BooleanConstraint)

@given(instance=EFM::Value_strategy)
@settings(max_examples=50)
def test_efm::value_instantiation(instance):
    assert isinstance(instance, EFM::Value)

@given(instance=EFM::Cardinality_strategy)
@settings(max_examples=50)
def test_efm::cardinality_instantiation(instance):
    assert isinstance(instance, EFM::Cardinality)

@given(instance=EFM::Cardinality_strategy)
def test_efm::cardinality_cardinalityMax_type(instance):
    assert isinstance(instance.cardinalityMax, int)


@given(instance=EFM::Cardinality_strategy)
def test_efm::cardinality_cardinalityMax_setter(instance):
    original = instance.cardinalityMax
    instance.cardinalityMax = original
    assert instance.cardinalityMax == original

@given(instance=EFM::Cardinality_strategy)
def test_efm::cardinality_cardinalityMin_type(instance):
    assert isinstance(instance.cardinalityMin, int)


@given(instance=EFM::Cardinality_strategy)
def test_efm::cardinality_cardinalityMin_setter(instance):
    original = instance.cardinalityMin
    instance.cardinalityMin = original
    assert instance.cardinalityMin == original

@given(instance=EFM::Cardinality_strategy)
def test_efm::cardinality_configValue_type(instance):
    assert isinstance(instance.configValue, int)


@given(instance=EFM::Cardinality_strategy)
def test_efm::cardinality_configValue_setter(instance):
    original = instance.configValue
    instance.configValue = original
    assert instance.configValue == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=EFM::Alternative_strategy)
@settings(max_examples=50)
def test_efm::alternative_instantiation(instance):
    assert isinstance(instance, EFM::Alternative)

@given(instance=Alternative_strategy)
@settings(max_examples=50)
def test_alternative_instantiation(instance):
    assert isinstance(instance, Alternative)

@given(instance=EFM::Exclusive_strategy)
@settings(max_examples=50)
def test_efm::exclusive_instantiation(instance):
    assert isinstance(instance, EFM::Exclusive)

@given(instance=EFM::NodeFeature_strategy)
@settings(max_examples=50)
def test_efm::nodefeature_instantiation(instance):
    assert isinstance(instance, EFM::NodeFeature)

@given(instance=EFM::NodeFeature_strategy)
def test_efm::nodefeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EFM::NodeFeature_strategy)
def test_efm::nodefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EFM::FeatCardinality_strategy)
@settings(max_examples=50)
def test_efm::featcardinality_instantiation(instance):
    assert isinstance(instance, EFM::FeatCardinality)

@given(instance=FMElement_strategy)
@settings(max_examples=50)
def test_fmelement_instantiation(instance):
    assert isinstance(instance, FMElement)

@given(instance=EFM::Attribute_strategy)
@settings(max_examples=50)
def test_efm::attribute_instantiation(instance):
    assert isinstance(instance, EFM::Attribute)

@given(instance=EFM::Attribute_strategy)
def test_efm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EFM::Attribute_strategy)
def test_efm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EFM::FMElement_strategy)
@settings(max_examples=50)
def test_efm::fmelement_instantiation(instance):
    assert isinstance(instance, EFM::FMElement)

@given(instance=EFM::Feature_strategy)
@settings(max_examples=50)
def test_efm::feature_instantiation(instance):
    assert isinstance(instance, EFM::Feature)

@given(instance=EFM::Feature_strategy)
def test_efm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EFM::Feature_strategy)
def test_efm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EFM::FMConstraint_strategy)
@settings(max_examples=50)
def test_efm::fmconstraint_instantiation(instance):
    assert isinstance(instance, EFM::FMConstraint)

@given(instance=EFM::FeatureModel_strategy)
@settings(max_examples=50)
def test_efm::featuremodel_instantiation(instance):
    assert isinstance(instance, EFM::FeatureModel)
