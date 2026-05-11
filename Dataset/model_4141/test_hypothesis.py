import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    arithmetic::Multi,
    arithmetic::Minus,
    arithmetic::Plus,
    arithmetic::SumExpression,
    arithmetic::AbstractDefinition,
    arithmetic::Expression,
    arithmetic::FunctionCall,
    arithmetic::NumberLiteral,
    arithmetic::Div,
    arithmetic::Module,
    AbstractDefinition,
    arithmetic::DeclaredParameter,
    Statement,
    arithmetic::Evaluation,
    arithmetic::Definition,
    arithmetic::Statement,
    arithmetic::Import,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::multi_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Multi)


def test_arithmetic::multi_constructor_exists():
    assert callable(arithmetic::Multi.__init__)


def test_arithmetic::multi_constructor_args():
    sig = inspect.signature(arithmetic::Multi.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::minus_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Minus)


def test_arithmetic::minus_constructor_exists():
    assert callable(arithmetic::Minus.__init__)


def test_arithmetic::minus_constructor_args():
    sig = inspect.signature(arithmetic::Minus.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::plus_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Plus)


def test_arithmetic::plus_constructor_exists():
    assert callable(arithmetic::Plus.__init__)


def test_arithmetic::plus_constructor_args():
    sig = inspect.signature(arithmetic::Plus.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::sumexpression_is_not_abstract():
    assert not inspect.isabstract(arithmetic::SumExpression)


def test_arithmetic::sumexpression_constructor_exists():
    assert callable(arithmetic::SumExpression.__init__)


def test_arithmetic::sumexpression_constructor_args():
    sig = inspect.signature(arithmetic::SumExpression.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_arithmetic::sumexpression_has_upper():
    assert hasattr(arithmetic::SumExpression, "upper")
    descriptor = None
    for klass in arithmetic::SumExpression.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_arithmetic::sumexpression_has_lower():
    assert hasattr(arithmetic::SumExpression, "lower")
    descriptor = None
    for klass in arithmetic::SumExpression.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_arithmetic::abstractdefinition_is_not_abstract():
    assert not inspect.isabstract(arithmetic::AbstractDefinition)


def test_arithmetic::abstractdefinition_constructor_exists():
    assert callable(arithmetic::AbstractDefinition.__init__)


def test_arithmetic::abstractdefinition_constructor_args():
    sig = inspect.signature(arithmetic::AbstractDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arithmetic::abstractdefinition_has_name():
    assert hasattr(arithmetic::AbstractDefinition, "name")
    descriptor = None
    for klass in arithmetic::AbstractDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arithmetic::expression_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Expression)


def test_arithmetic::expression_constructor_exists():
    assert callable(arithmetic::Expression.__init__)


def test_arithmetic::expression_constructor_args():
    sig = inspect.signature(arithmetic::Expression.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::functioncall_is_not_abstract():
    assert not inspect.isabstract(arithmetic::FunctionCall)


def test_arithmetic::functioncall_constructor_exists():
    assert callable(arithmetic::FunctionCall.__init__)


def test_arithmetic::functioncall_constructor_args():
    sig = inspect.signature(arithmetic::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::numberliteral_is_not_abstract():
    assert not inspect.isabstract(arithmetic::NumberLiteral)


def test_arithmetic::numberliteral_constructor_exists():
    assert callable(arithmetic::NumberLiteral.__init__)


def test_arithmetic::numberliteral_constructor_args():
    sig = inspect.signature(arithmetic::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arithmetic::numberliteral_has_value():
    assert hasattr(arithmetic::NumberLiteral, "value")
    descriptor = None
    for klass in arithmetic::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arithmetic::div_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Div)


def test_arithmetic::div_constructor_exists():
    assert callable(arithmetic::Div.__init__)


def test_arithmetic::div_constructor_args():
    sig = inspect.signature(arithmetic::Div.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::module_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Module)


def test_arithmetic::module_constructor_exists():
    assert callable(arithmetic::Module.__init__)


def test_arithmetic::module_constructor_args():
    sig = inspect.signature(arithmetic::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arithmetic::module_has_name():
    assert hasattr(arithmetic::Module, "name")
    descriptor = None
    for klass in arithmetic::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractdefinition_is_not_abstract():
    assert not inspect.isabstract(AbstractDefinition)


def test_abstractdefinition_constructor_exists():
    assert callable(AbstractDefinition.__init__)


def test_abstractdefinition_constructor_args():
    sig = inspect.signature(AbstractDefinition.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::declaredparameter_is_not_abstract():
    assert not inspect.isabstract(arithmetic::DeclaredParameter)


def test_arithmetic::declaredparameter_constructor_exists():
    assert callable(arithmetic::DeclaredParameter.__init__)


def test_arithmetic::declaredparameter_constructor_args():
    sig = inspect.signature(arithmetic::DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::evaluation_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Evaluation)


def test_arithmetic::evaluation_constructor_exists():
    assert callable(arithmetic::Evaluation.__init__)


def test_arithmetic::evaluation_constructor_args():
    sig = inspect.signature(arithmetic::Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::definition_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Definition)


def test_arithmetic::definition_constructor_exists():
    assert callable(arithmetic::Definition.__init__)


def test_arithmetic::definition_constructor_args():
    sig = inspect.signature(arithmetic::Definition.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::statement_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Statement)


def test_arithmetic::statement_constructor_exists():
    assert callable(arithmetic::Statement.__init__)


def test_arithmetic::statement_constructor_args():
    sig = inspect.signature(arithmetic::Statement.__init__)
    params = list(sig.parameters.keys())



def test_arithmetic::import_is_not_abstract():
    assert not inspect.isabstract(arithmetic::Import)


def test_arithmetic::import_constructor_exists():
    assert callable(arithmetic::Import.__init__)


def test_arithmetic::import_constructor_args():
    sig = inspect.signature(arithmetic::Import.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
arithmetic::Multi_strategy = st.builds(
    arithmetic::Multi,
)
arithmetic::Minus_strategy = st.builds(
    arithmetic::Minus,
)
arithmetic::Plus_strategy = st.builds(
    arithmetic::Plus,
)
arithmetic::SumExpression_strategy = st.builds(
    arithmetic::SumExpression,
    upper=
        st.integers(),
    lower=
        st.integers()
)
arithmetic::AbstractDefinition_strategy = st.builds(
    arithmetic::AbstractDefinition,
    name=
        safe_text
)
arithmetic::Expression_strategy = st.builds(
    arithmetic::Expression,
)
arithmetic::FunctionCall_strategy = st.builds(
    arithmetic::FunctionCall,
)
arithmetic::NumberLiteral_strategy = st.builds(
    arithmetic::NumberLiteral,
    value=
        st.integers()
)
arithmetic::Div_strategy = st.builds(
    arithmetic::Div,
)
arithmetic::Module_strategy = st.builds(
    arithmetic::Module,
    name=
        safe_text
)
AbstractDefinition_strategy = st.builds(
    AbstractDefinition,
)
arithmetic::DeclaredParameter_strategy = st.builds(
    arithmetic::DeclaredParameter,
)
Statement_strategy = st.builds(
    Statement,
)
arithmetic::Evaluation_strategy = st.builds(
    arithmetic::Evaluation,
)
arithmetic::Definition_strategy = st.builds(
    arithmetic::Definition,
)
arithmetic::Statement_strategy = st.builds(
    arithmetic::Statement,
)
arithmetic::Import_strategy = st.builds(
    arithmetic::Import,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=arithmetic::Multi_strategy)
@settings(max_examples=50)
def test_arithmetic::multi_instantiation(instance):
    assert isinstance(instance, arithmetic::Multi)

@given(instance=arithmetic::Minus_strategy)
@settings(max_examples=50)
def test_arithmetic::minus_instantiation(instance):
    assert isinstance(instance, arithmetic::Minus)

@given(instance=arithmetic::Plus_strategy)
@settings(max_examples=50)
def test_arithmetic::plus_instantiation(instance):
    assert isinstance(instance, arithmetic::Plus)

@given(instance=arithmetic::SumExpression_strategy)
@settings(max_examples=50)
def test_arithmetic::sumexpression_instantiation(instance):
    assert isinstance(instance, arithmetic::SumExpression)

@given(instance=arithmetic::SumExpression_strategy)
def test_arithmetic::sumexpression_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=arithmetic::SumExpression_strategy)
def test_arithmetic::sumexpression_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=arithmetic::SumExpression_strategy)
def test_arithmetic::sumexpression_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=arithmetic::SumExpression_strategy)
def test_arithmetic::sumexpression_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=arithmetic::AbstractDefinition_strategy)
@settings(max_examples=50)
def test_arithmetic::abstractdefinition_instantiation(instance):
    assert isinstance(instance, arithmetic::AbstractDefinition)

@given(instance=arithmetic::AbstractDefinition_strategy)
def test_arithmetic::abstractdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arithmetic::AbstractDefinition_strategy)
def test_arithmetic::abstractdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arithmetic::Expression_strategy)
@settings(max_examples=50)
def test_arithmetic::expression_instantiation(instance):
    assert isinstance(instance, arithmetic::Expression)

@given(instance=arithmetic::FunctionCall_strategy)
@settings(max_examples=50)
def test_arithmetic::functioncall_instantiation(instance):
    assert isinstance(instance, arithmetic::FunctionCall)

@given(instance=arithmetic::NumberLiteral_strategy)
@settings(max_examples=50)
def test_arithmetic::numberliteral_instantiation(instance):
    assert isinstance(instance, arithmetic::NumberLiteral)

@given(instance=arithmetic::NumberLiteral_strategy)
def test_arithmetic::numberliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arithmetic::NumberLiteral_strategy)
def test_arithmetic::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arithmetic::Div_strategy)
@settings(max_examples=50)
def test_arithmetic::div_instantiation(instance):
    assert isinstance(instance, arithmetic::Div)

@given(instance=arithmetic::Module_strategy)
@settings(max_examples=50)
def test_arithmetic::module_instantiation(instance):
    assert isinstance(instance, arithmetic::Module)

@given(instance=arithmetic::Module_strategy)
def test_arithmetic::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arithmetic::Module_strategy)
def test_arithmetic::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractDefinition_strategy)
@settings(max_examples=50)
def test_abstractdefinition_instantiation(instance):
    assert isinstance(instance, AbstractDefinition)

@given(instance=arithmetic::DeclaredParameter_strategy)
@settings(max_examples=50)
def test_arithmetic::declaredparameter_instantiation(instance):
    assert isinstance(instance, arithmetic::DeclaredParameter)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=arithmetic::Evaluation_strategy)
@settings(max_examples=50)
def test_arithmetic::evaluation_instantiation(instance):
    assert isinstance(instance, arithmetic::Evaluation)

@given(instance=arithmetic::Definition_strategy)
@settings(max_examples=50)
def test_arithmetic::definition_instantiation(instance):
    assert isinstance(instance, arithmetic::Definition)

@given(instance=arithmetic::Statement_strategy)
@settings(max_examples=50)
def test_arithmetic::statement_instantiation(instance):
    assert isinstance(instance, arithmetic::Statement)

@given(instance=arithmetic::Import_strategy)
@settings(max_examples=50)
def test_arithmetic::import_instantiation(instance):
    assert isinstance(instance, arithmetic::Import)
