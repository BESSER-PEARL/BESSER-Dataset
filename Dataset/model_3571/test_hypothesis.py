import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Literal,
    expression::RealLiteral,
    expression::StringLiteral,
    expression::NullLiteral,
    expression::IntegerLiteral,
    expression::BooleanLiteral,
    Expression,
    expression::Literal,
    expression::SwitchExpression,
    expression::FeatureCall,
    expression::ChainExpression,
    expression::CastedExpression,
    expression::ConstructorCallExpression,
    expression::GlobalVarExpression,
    expression::ListLiteral,
    expression::IfExpression,
    expression::BooleanOperation,
    expression::LetExpression,
    expression::SyntaxElement,
    SyntaxElement,
    expression::Identifier,
    expression::Case,
    expression::Expression,
    FeatureCall,
    expression::CollectionExpression,
    expression::TypeSelectExpression,
    expression::OperationCall,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression::realliteral_is_not_abstract():
    assert not inspect.isabstract(expression::RealLiteral)


def test_expression::realliteral_constructor_exists():
    assert callable(expression::RealLiteral.__init__)


def test_expression::realliteral_constructor_args():
    sig = inspect.signature(expression::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression::realliteral_has_val():
    assert hasattr(expression::RealLiteral, "val")
    descriptor = None
    for klass in expression::RealLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression::stringliteral_is_not_abstract():
    assert not inspect.isabstract(expression::StringLiteral)


def test_expression::stringliteral_constructor_exists():
    assert callable(expression::StringLiteral.__init__)


def test_expression::stringliteral_constructor_args():
    sig = inspect.signature(expression::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression::stringliteral_has_val():
    assert hasattr(expression::StringLiteral, "val")
    descriptor = None
    for klass in expression::StringLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression::nullliteral_is_not_abstract():
    assert not inspect.isabstract(expression::NullLiteral)


def test_expression::nullliteral_constructor_exists():
    assert callable(expression::NullLiteral.__init__)


def test_expression::nullliteral_constructor_args():
    sig = inspect.signature(expression::NullLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression::nullliteral_has_val():
    assert hasattr(expression::NullLiteral, "val")
    descriptor = None
    for klass in expression::NullLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression::integerliteral_is_not_abstract():
    assert not inspect.isabstract(expression::IntegerLiteral)


def test_expression::integerliteral_constructor_exists():
    assert callable(expression::IntegerLiteral.__init__)


def test_expression::integerliteral_constructor_args():
    sig = inspect.signature(expression::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression::integerliteral_has_val():
    assert hasattr(expression::IntegerLiteral, "val")
    descriptor = None
    for klass in expression::IntegerLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(expression::BooleanLiteral)


def test_expression::booleanliteral_constructor_exists():
    assert callable(expression::BooleanLiteral.__init__)


def test_expression::booleanliteral_constructor_args():
    sig = inspect.signature(expression::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression::booleanliteral_has_val():
    assert hasattr(expression::BooleanLiteral, "val")
    descriptor = None
    for klass in expression::BooleanLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression::literal_is_not_abstract():
    assert not inspect.isabstract(expression::Literal)


def test_expression::literal_constructor_exists():
    assert callable(expression::Literal.__init__)


def test_expression::literal_constructor_args():
    sig = inspect.signature(expression::Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression::switchexpression_is_not_abstract():
    assert not inspect.isabstract(expression::SwitchExpression)


def test_expression::switchexpression_constructor_exists():
    assert callable(expression::SwitchExpression.__init__)


def test_expression::switchexpression_constructor_args():
    sig = inspect.signature(expression::SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::featurecall_is_not_abstract():
    assert not inspect.isabstract(expression::FeatureCall)


def test_expression::featurecall_constructor_exists():
    assert callable(expression::FeatureCall.__init__)


def test_expression::featurecall_constructor_args():
    sig = inspect.signature(expression::FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expression::featurecall_has_name():
    assert hasattr(expression::FeatureCall, "name")
    descriptor = None
    for klass in expression::FeatureCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression::chainexpression_is_not_abstract():
    assert not inspect.isabstract(expression::ChainExpression)


def test_expression::chainexpression_constructor_exists():
    assert callable(expression::ChainExpression.__init__)


def test_expression::chainexpression_constructor_args():
    sig = inspect.signature(expression::ChainExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::castedexpression_is_not_abstract():
    assert not inspect.isabstract(expression::CastedExpression)


def test_expression::castedexpression_constructor_exists():
    assert callable(expression::CastedExpression.__init__)


def test_expression::castedexpression_constructor_args():
    sig = inspect.signature(expression::CastedExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::constructorcallexpression_is_not_abstract():
    assert not inspect.isabstract(expression::ConstructorCallExpression)


def test_expression::constructorcallexpression_constructor_exists():
    assert callable(expression::ConstructorCallExpression.__init__)


def test_expression::constructorcallexpression_constructor_args():
    sig = inspect.signature(expression::ConstructorCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::globalvarexpression_is_not_abstract():
    assert not inspect.isabstract(expression::GlobalVarExpression)


def test_expression::globalvarexpression_constructor_exists():
    assert callable(expression::GlobalVarExpression.__init__)


def test_expression::globalvarexpression_constructor_args():
    sig = inspect.signature(expression::GlobalVarExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expression::globalvarexpression_has_name():
    assert hasattr(expression::GlobalVarExpression, "name")
    descriptor = None
    for klass in expression::GlobalVarExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression::listliteral_is_not_abstract():
    assert not inspect.isabstract(expression::ListLiteral)


def test_expression::listliteral_constructor_exists():
    assert callable(expression::ListLiteral.__init__)


def test_expression::listliteral_constructor_args():
    sig = inspect.signature(expression::ListLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression::ifexpression_is_not_abstract():
    assert not inspect.isabstract(expression::IfExpression)


def test_expression::ifexpression_constructor_exists():
    assert callable(expression::IfExpression.__init__)


def test_expression::ifexpression_constructor_args():
    sig = inspect.signature(expression::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::booleanoperation_is_not_abstract():
    assert not inspect.isabstract(expression::BooleanOperation)


def test_expression::booleanoperation_constructor_exists():
    assert callable(expression::BooleanOperation.__init__)


def test_expression::booleanoperation_constructor_args():
    sig = inspect.signature(expression::BooleanOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expression::booleanoperation_has_operator():
    assert hasattr(expression::BooleanOperation, "operator")
    descriptor = None
    for klass in expression::BooleanOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expression::letexpression_is_not_abstract():
    assert not inspect.isabstract(expression::LetExpression)


def test_expression::letexpression_constructor_exists():
    assert callable(expression::LetExpression.__init__)


def test_expression::letexpression_constructor_args():
    sig = inspect.signature(expression::LetExpression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_expression::letexpression_has_identifier():
    assert hasattr(expression::LetExpression, "identifier")
    descriptor = None
    for klass in expression::LetExpression.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_expression::syntaxelement_is_not_abstract():
    assert not inspect.isabstract(expression::SyntaxElement)


def test_expression::syntaxelement_constructor_exists():
    assert callable(expression::SyntaxElement.__init__)


def test_expression::syntaxelement_constructor_args():
    sig = inspect.signature(expression::SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(SyntaxElement)


def test_syntaxelement_constructor_exists():
    assert callable(SyntaxElement.__init__)


def test_syntaxelement_constructor_args():
    sig = inspect.signature(SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_expression::identifier_is_not_abstract():
    assert not inspect.isabstract(expression::Identifier)


def test_expression::identifier_constructor_exists():
    assert callable(expression::Identifier.__init__)


def test_expression::identifier_constructor_args():
    sig = inspect.signature(expression::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "cl" in params, "Missing parameter 'cl'"
    assert "id" in params, "Missing parameter 'id'"

def test_expression::identifier_has_cl():
    assert hasattr(expression::Identifier, "cl")
    descriptor = None
    for klass in expression::Identifier.__mro__:
        if "cl" in klass.__dict__:
            descriptor = klass.__dict__["cl"]
            break
    assert isinstance(descriptor, property)

def test_expression::identifier_has_id():
    assert hasattr(expression::Identifier, "id")
    descriptor = None
    for klass in expression::Identifier.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_expression::case_is_not_abstract():
    assert not inspect.isabstract(expression::Case)


def test_expression::case_constructor_exists():
    assert callable(expression::Case.__init__)


def test_expression::case_constructor_args():
    sig = inspect.signature(expression::Case.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_expression::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(expression::CollectionExpression)


def test_expression::collectionexpression_constructor_exists():
    assert callable(expression::CollectionExpression.__init__)


def test_expression::collectionexpression_constructor_args():
    sig = inspect.signature(expression::CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_expression::collectionexpression_has_var():
    assert hasattr(expression::CollectionExpression, "var")
    descriptor = None
    for klass in expression::CollectionExpression.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_expression::typeselectexpression_is_not_abstract():
    assert not inspect.isabstract(expression::TypeSelectExpression)


def test_expression::typeselectexpression_constructor_exists():
    assert callable(expression::TypeSelectExpression.__init__)


def test_expression::typeselectexpression_constructor_args():
    sig = inspect.signature(expression::TypeSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::operationcall_is_not_abstract():
    assert not inspect.isabstract(expression::OperationCall)


def test_expression::operationcall_constructor_exists():
    assert callable(expression::OperationCall.__init__)


def test_expression::operationcall_constructor_args():
    sig = inspect.signature(expression::OperationCall.__init__)
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
Literal_strategy = st.builds(
    Literal,
)
expression::RealLiteral_strategy = st.builds(
    expression::RealLiteral,
    val=
        safe_text
)
expression::StringLiteral_strategy = st.builds(
    expression::StringLiteral,
    val=
        safe_text
)
expression::NullLiteral_strategy = st.builds(
    expression::NullLiteral,
    val=
        safe_text
)
expression::IntegerLiteral_strategy = st.builds(
    expression::IntegerLiteral,
    val=
        st.integers()
)
expression::BooleanLiteral_strategy = st.builds(
    expression::BooleanLiteral,
    val=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
expression::Literal_strategy = st.builds(
    expression::Literal,
)
expression::SwitchExpression_strategy = st.builds(
    expression::SwitchExpression,
)
expression::FeatureCall_strategy = st.builds(
    expression::FeatureCall,
    name=
        safe_text
)
expression::ChainExpression_strategy = st.builds(
    expression::ChainExpression,
)
expression::CastedExpression_strategy = st.builds(
    expression::CastedExpression,
)
expression::ConstructorCallExpression_strategy = st.builds(
    expression::ConstructorCallExpression,
)
expression::GlobalVarExpression_strategy = st.builds(
    expression::GlobalVarExpression,
    name=
        safe_text
)
expression::ListLiteral_strategy = st.builds(
    expression::ListLiteral,
)
expression::IfExpression_strategy = st.builds(
    expression::IfExpression,
)
expression::BooleanOperation_strategy = st.builds(
    expression::BooleanOperation,
    operator=
        safe_text
)
expression::LetExpression_strategy = st.builds(
    expression::LetExpression,
    identifier=
        safe_text
)
expression::SyntaxElement_strategy = st.builds(
    expression::SyntaxElement,
)
SyntaxElement_strategy = st.builds(
    SyntaxElement,
)
expression::Identifier_strategy = st.builds(
    expression::Identifier,
    cl=
        safe_text,
    id=
        safe_text
)
expression::Case_strategy = st.builds(
    expression::Case,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
expression::CollectionExpression_strategy = st.builds(
    expression::CollectionExpression,
    var=
        safe_text
)
expression::TypeSelectExpression_strategy = st.builds(
    expression::TypeSelectExpression,
)
expression::OperationCall_strategy = st.builds(
    expression::OperationCall,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=expression::RealLiteral_strategy)
@settings(max_examples=50)
def test_expression::realliteral_instantiation(instance):
    assert isinstance(instance, expression::RealLiteral)

@given(instance=expression::RealLiteral_strategy)
def test_expression::realliteral_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=expression::RealLiteral_strategy)
def test_expression::realliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression::StringLiteral_strategy)
@settings(max_examples=50)
def test_expression::stringliteral_instantiation(instance):
    assert isinstance(instance, expression::StringLiteral)

@given(instance=expression::StringLiteral_strategy)
def test_expression::stringliteral_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=expression::StringLiteral_strategy)
def test_expression::stringliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression::NullLiteral_strategy)
@settings(max_examples=50)
def test_expression::nullliteral_instantiation(instance):
    assert isinstance(instance, expression::NullLiteral)

@given(instance=expression::NullLiteral_strategy)
def test_expression::nullliteral_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=expression::NullLiteral_strategy)
def test_expression::nullliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_expression::integerliteral_instantiation(instance):
    assert isinstance(instance, expression::IntegerLiteral)

@given(instance=expression::IntegerLiteral_strategy)
def test_expression::integerliteral_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=expression::IntegerLiteral_strategy)
def test_expression::integerliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_expression::booleanliteral_instantiation(instance):
    assert isinstance(instance, expression::BooleanLiteral)

@given(instance=expression::BooleanLiteral_strategy)
def test_expression::booleanliteral_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=expression::BooleanLiteral_strategy)
def test_expression::booleanliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression::Literal_strategy)
@settings(max_examples=50)
def test_expression::literal_instantiation(instance):
    assert isinstance(instance, expression::Literal)

@given(instance=expression::SwitchExpression_strategy)
@settings(max_examples=50)
def test_expression::switchexpression_instantiation(instance):
    assert isinstance(instance, expression::SwitchExpression)

@given(instance=expression::FeatureCall_strategy)
@settings(max_examples=50)
def test_expression::featurecall_instantiation(instance):
    assert isinstance(instance, expression::FeatureCall)

@given(instance=expression::FeatureCall_strategy)
def test_expression::featurecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expression::FeatureCall_strategy)
def test_expression::featurecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expression::ChainExpression_strategy)
@settings(max_examples=50)
def test_expression::chainexpression_instantiation(instance):
    assert isinstance(instance, expression::ChainExpression)

@given(instance=expression::CastedExpression_strategy)
@settings(max_examples=50)
def test_expression::castedexpression_instantiation(instance):
    assert isinstance(instance, expression::CastedExpression)

@given(instance=expression::ConstructorCallExpression_strategy)
@settings(max_examples=50)
def test_expression::constructorcallexpression_instantiation(instance):
    assert isinstance(instance, expression::ConstructorCallExpression)

@given(instance=expression::GlobalVarExpression_strategy)
@settings(max_examples=50)
def test_expression::globalvarexpression_instantiation(instance):
    assert isinstance(instance, expression::GlobalVarExpression)

@given(instance=expression::GlobalVarExpression_strategy)
def test_expression::globalvarexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expression::GlobalVarExpression_strategy)
def test_expression::globalvarexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expression::ListLiteral_strategy)
@settings(max_examples=50)
def test_expression::listliteral_instantiation(instance):
    assert isinstance(instance, expression::ListLiteral)

@given(instance=expression::IfExpression_strategy)
@settings(max_examples=50)
def test_expression::ifexpression_instantiation(instance):
    assert isinstance(instance, expression::IfExpression)

@given(instance=expression::BooleanOperation_strategy)
@settings(max_examples=50)
def test_expression::booleanoperation_instantiation(instance):
    assert isinstance(instance, expression::BooleanOperation)

@given(instance=expression::BooleanOperation_strategy)
def test_expression::booleanoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expression::BooleanOperation_strategy)
def test_expression::booleanoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expression::LetExpression_strategy)
@settings(max_examples=50)
def test_expression::letexpression_instantiation(instance):
    assert isinstance(instance, expression::LetExpression)

@given(instance=expression::LetExpression_strategy)
def test_expression::letexpression_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=expression::LetExpression_strategy)
def test_expression::letexpression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=expression::SyntaxElement_strategy)
@settings(max_examples=50)
def test_expression::syntaxelement_instantiation(instance):
    assert isinstance(instance, expression::SyntaxElement)

@given(instance=SyntaxElement_strategy)
@settings(max_examples=50)
def test_syntaxelement_instantiation(instance):
    assert isinstance(instance, SyntaxElement)

@given(instance=expression::Identifier_strategy)
@settings(max_examples=50)
def test_expression::identifier_instantiation(instance):
    assert isinstance(instance, expression::Identifier)

@given(instance=expression::Identifier_strategy)
def test_expression::identifier_cl_type(instance):
    assert isinstance(instance.cl, str)


@given(instance=expression::Identifier_strategy)
def test_expression::identifier_cl_setter(instance):
    original = instance.cl
    instance.cl = original
    assert instance.cl == original

@given(instance=expression::Identifier_strategy)
def test_expression::identifier_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=expression::Identifier_strategy)
def test_expression::identifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=expression::Case_strategy)
@settings(max_examples=50)
def test_expression::case_instantiation(instance):
    assert isinstance(instance, expression::Case)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=FeatureCall_strategy)
@settings(max_examples=50)
def test_featurecall_instantiation(instance):
    assert isinstance(instance, FeatureCall)

@given(instance=expression::CollectionExpression_strategy)
@settings(max_examples=50)
def test_expression::collectionexpression_instantiation(instance):
    assert isinstance(instance, expression::CollectionExpression)

@given(instance=expression::CollectionExpression_strategy)
def test_expression::collectionexpression_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=expression::CollectionExpression_strategy)
def test_expression::collectionexpression_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=expression::TypeSelectExpression_strategy)
@settings(max_examples=50)
def test_expression::typeselectexpression_instantiation(instance):
    assert isinstance(instance, expression::TypeSelectExpression)

@given(instance=expression::OperationCall_strategy)
@settings(max_examples=50)
def test_expression::operationcall_instantiation(instance):
    assert isinstance(instance, expression::OperationCall)
