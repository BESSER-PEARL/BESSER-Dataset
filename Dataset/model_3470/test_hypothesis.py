import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Constant,
    featureModel::Number,
    featureModel::NULL,
    featureModel::Expression,
    featureModel::Group,
    Expression,
    featureModel::UnaryOperation,
    featureModel::Identifier,
    featureModel::Constant,
    featureModel::BinaryOperation,
    featureModel::Model,
    featureModel::Feature,
    Feature,
    featureModel::GroupedFeature,
    featureModel::SolitaryFeature,
    BinaryOperator,
    SimpleType,
    UnaryOperator,
    SolitaryType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::number_is_not_abstract():
    assert not inspect.isabstract(featureModel::Number)


def test_featuremodel::number_constructor_exists():
    assert callable(featureModel::Number.__init__)


def test_featuremodel::number_constructor_args():
    sig = inspect.signature(featureModel::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_featuremodel::number_has_value():
    assert hasattr(featureModel::Number, "value")
    descriptor = None
    for klass in featureModel::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::null_is_not_abstract():
    assert not inspect.isabstract(featureModel::NULL)


def test_featuremodel::null_constructor_exists():
    assert callable(featureModel::NULL.__init__)


def test_featuremodel::null_constructor_args():
    sig = inspect.signature(featureModel::NULL.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::expression_is_not_abstract():
    assert not inspect.isabstract(featureModel::Expression)


def test_featuremodel::expression_constructor_exists():
    assert callable(featureModel::Expression.__init__)


def test_featuremodel::expression_constructor_args():
    sig = inspect.signature(featureModel::Expression.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::group_is_not_abstract():
    assert not inspect.isabstract(featureModel::Group)


def test_featuremodel::group_constructor_exists():
    assert callable(featureModel::Group.__init__)


def test_featuremodel::group_constructor_args():
    sig = inspect.signature(featureModel::Group.__init__)
    params = list(sig.parameters.keys())
    assert "inclusive" in params, "Missing parameter 'inclusive'"

def test_featuremodel::group_has_inclusive():
    assert hasattr(featureModel::Group, "inclusive")
    descriptor = None
    for klass in featureModel::Group.__mro__:
        if "inclusive" in klass.__dict__:
            descriptor = klass.__dict__["inclusive"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::unaryoperation_is_not_abstract():
    assert not inspect.isabstract(featureModel::UnaryOperation)


def test_featuremodel::unaryoperation_constructor_exists():
    assert callable(featureModel::UnaryOperation.__init__)


def test_featuremodel::unaryoperation_constructor_args():
    sig = inspect.signature(featureModel::UnaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_featuremodel::unaryoperation_has_operator():
    assert hasattr(featureModel::UnaryOperation, "operator")
    descriptor = None
    for klass in featureModel::UnaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::identifier_is_not_abstract():
    assert not inspect.isabstract(featureModel::Identifier)


def test_featuremodel::identifier_constructor_exists():
    assert callable(featureModel::Identifier.__init__)


def test_featuremodel::identifier_constructor_args():
    sig = inspect.signature(featureModel::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel::identifier_has_name():
    assert hasattr(featureModel::Identifier, "name")
    descriptor = None
    for klass in featureModel::Identifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::constant_is_not_abstract():
    assert not inspect.isabstract(featureModel::Constant)


def test_featuremodel::constant_constructor_exists():
    assert callable(featureModel::Constant.__init__)


def test_featuremodel::constant_constructor_args():
    sig = inspect.signature(featureModel::Constant.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(featureModel::BinaryOperation)


def test_featuremodel::binaryoperation_constructor_exists():
    assert callable(featureModel::BinaryOperation.__init__)


def test_featuremodel::binaryoperation_constructor_args():
    sig = inspect.signature(featureModel::BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_featuremodel::binaryoperation_has_operator():
    assert hasattr(featureModel::BinaryOperation, "operator")
    descriptor = None
    for klass in featureModel::BinaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::model_is_not_abstract():
    assert not inspect.isabstract(featureModel::Model)


def test_featuremodel::model_constructor_exists():
    assert callable(featureModel::Model.__init__)


def test_featuremodel::model_constructor_args():
    sig = inspect.signature(featureModel::Model.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::feature_is_not_abstract():
    assert not inspect.isabstract(featureModel::Feature)


def test_featuremodel::feature_constructor_exists():
    assert callable(featureModel::Feature.__init__)


def test_featuremodel::feature_constructor_args():
    sig = inspect.signature(featureModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel::feature_has_name():
    assert hasattr(featureModel::Feature, "name")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_type():
    assert hasattr(featureModel::Feature, "type")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::groupedfeature_is_not_abstract():
    assert not inspect.isabstract(featureModel::GroupedFeature)


def test_featuremodel::groupedfeature_constructor_exists():
    assert callable(featureModel::GroupedFeature.__init__)


def test_featuremodel::groupedfeature_constructor_args():
    sig = inspect.signature(featureModel::GroupedFeature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::solitaryfeature_is_not_abstract():
    assert not inspect.isabstract(featureModel::SolitaryFeature)


def test_featuremodel::solitaryfeature_constructor_exists():
    assert callable(featureModel::SolitaryFeature.__init__)


def test_featuremodel::solitaryfeature_constructor_args():
    sig = inspect.signature(featureModel::SolitaryFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_featuremodel::solitaryfeature_has_required():
    assert hasattr(featureModel::SolitaryFeature, "required")
    descriptor = None
    for klass in featureModel::SolitaryFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_binaryoperator_exists():
    # Check that the Enumeration exists
    assert BinaryOperator is not None

def test_binaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperator]
    expected_literals = [
        "And",
        "Divide",
        "Equals",
        "Higher",
        "Or",
        "Subtract",
        "Add",
        "Lower",
        "Multiply",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperator"

def test_simpletype_exists():
    # Check that the Enumeration exists
    assert SimpleType is not None

def test_simpletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleType]
    expected_literals = [
        "boolean",
        "String",
        "nulltype",
        "int",
        "double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleType"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "Minus",
        "Not",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_solitarytype_exists():
    # Check that the Enumeration exists
    assert SolitaryType is not None

def test_solitarytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SolitaryType]
    expected_literals = [
        "Mandatory",
        "Optional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SolitaryType"


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
Constant_strategy = st.builds(
    Constant,
)
featureModel::Number_strategy = st.builds(
    featureModel::Number,
    value=
        st.integers()
)
featureModel::NULL_strategy = st.builds(
    featureModel::NULL,
)
featureModel::Expression_strategy = st.builds(
    featureModel::Expression,
)
featureModel::Group_strategy = st.builds(
    featureModel::Group,
    inclusive=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
featureModel::UnaryOperation_strategy = st.builds(
    featureModel::UnaryOperation,
    operator=
        safe_text
)
featureModel::Identifier_strategy = st.builds(
    featureModel::Identifier,
    name=
        safe_text
)
featureModel::Constant_strategy = st.builds(
    featureModel::Constant,
)
featureModel::BinaryOperation_strategy = st.builds(
    featureModel::BinaryOperation,
    operator=
        safe_text
)
featureModel::Model_strategy = st.builds(
    featureModel::Model,
)
featureModel::Feature_strategy = st.builds(
    featureModel::Feature,
    name=
        safe_text,
    type=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
featureModel::GroupedFeature_strategy = st.builds(
    featureModel::GroupedFeature,
)
featureModel::SolitaryFeature_strategy = st.builds(
    featureModel::SolitaryFeature,
    required=
        safe_text
)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=featureModel::Number_strategy)
@settings(max_examples=50)
def test_featuremodel::number_instantiation(instance):
    assert isinstance(instance, featureModel::Number)

@given(instance=featureModel::Number_strategy)
def test_featuremodel::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=featureModel::Number_strategy)
def test_featuremodel::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featureModel::NULL_strategy)
@settings(max_examples=50)
def test_featuremodel::null_instantiation(instance):
    assert isinstance(instance, featureModel::NULL)

@given(instance=featureModel::Expression_strategy)
@settings(max_examples=50)
def test_featuremodel::expression_instantiation(instance):
    assert isinstance(instance, featureModel::Expression)

@given(instance=featureModel::Group_strategy)
@settings(max_examples=50)
def test_featuremodel::group_instantiation(instance):
    assert isinstance(instance, featureModel::Group)

@given(instance=featureModel::Group_strategy)
def test_featuremodel::group_inclusive_type(instance):
    assert isinstance(instance.inclusive, bool)


@given(instance=featureModel::Group_strategy)
def test_featuremodel::group_inclusive_setter(instance):
    original = instance.inclusive
    instance.inclusive = original
    assert instance.inclusive == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=featureModel::UnaryOperation_strategy)
@settings(max_examples=50)
def test_featuremodel::unaryoperation_instantiation(instance):
    assert isinstance(instance, featureModel::UnaryOperation)

@given(instance=featureModel::UnaryOperation_strategy)
def test_featuremodel::unaryoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=featureModel::UnaryOperation_strategy)
def test_featuremodel::unaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=featureModel::Identifier_strategy)
@settings(max_examples=50)
def test_featuremodel::identifier_instantiation(instance):
    assert isinstance(instance, featureModel::Identifier)

@given(instance=featureModel::Identifier_strategy)
def test_featuremodel::identifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModel::Identifier_strategy)
def test_featuremodel::identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureModel::Constant_strategy)
@settings(max_examples=50)
def test_featuremodel::constant_instantiation(instance):
    assert isinstance(instance, featureModel::Constant)

@given(instance=featureModel::BinaryOperation_strategy)
@settings(max_examples=50)
def test_featuremodel::binaryoperation_instantiation(instance):
    assert isinstance(instance, featureModel::BinaryOperation)

@given(instance=featureModel::BinaryOperation_strategy)
def test_featuremodel::binaryoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=featureModel::BinaryOperation_strategy)
def test_featuremodel::binaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=featureModel::Model_strategy)
@settings(max_examples=50)
def test_featuremodel::model_instantiation(instance):
    assert isinstance(instance, featureModel::Model)

@given(instance=featureModel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodel::feature_instantiation(instance):
    assert isinstance(instance, featureModel::Feature)

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featureModel::GroupedFeature_strategy)
@settings(max_examples=50)
def test_featuremodel::groupedfeature_instantiation(instance):
    assert isinstance(instance, featureModel::GroupedFeature)

@given(instance=featureModel::SolitaryFeature_strategy)
@settings(max_examples=50)
def test_featuremodel::solitaryfeature_instantiation(instance):
    assert isinstance(instance, featureModel::SolitaryFeature)

@given(instance=featureModel::SolitaryFeature_strategy)
def test_featuremodel::solitaryfeature_required_type(instance):
    assert isinstance(instance.required, str)


@given(instance=featureModel::SolitaryFeature_strategy)
def test_featuremodel::solitaryfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original
