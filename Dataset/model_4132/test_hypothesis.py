import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimaryExpression,
    cool::AssignmentExpression,
    cool::NegationExpression,
    cool::DispatchExpression,
    cool::IntegerCompositeExpression,
    cool::IsvoidExpression,
    cool::LoopExpression,
    cool::BlockExpression,
    cool::LetExpression,
    cool::ConditionalExpression,
    cool::NewExpression,
    cool::SelfTypeLiteral,
    Expression,
    cool::CompareExpression,
    cool::PrimaryExpression,
    cool::Expression,
    Feature::,
    cool::Method,
    cool::Attr,
    cool::Type,
    IdentifiableElement,
    cool::Formal,
    cool::Feature::,
    Type,
    cool::ParenExpression,
    Literal,
    cool::BooleanLiteral,
    cool::StringLiteral,
    cool::NumberLiteral,
    cool::Literal,
    cool::IdentifiableElement,
    cool::IdentifierRefExpression,
    cool::Class::,
    cool::Program,
    cool::Div,
    cool::MultiplicationExpression,
    cool::Minus,
    cool::AdditionExpression,
    cool::Case,
    cool::CaseExpression,
    cool::LetDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(cool::AssignmentExpression)


def test_cool::assignmentexpression_constructor_exists():
    assert callable(cool::AssignmentExpression.__init__)


def test_cool::assignmentexpression_constructor_args():
    sig = inspect.signature(cool::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cool::assignmentexpression_has_name():
    assert hasattr(cool::AssignmentExpression, "name")
    descriptor = None
    for klass in cool::AssignmentExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cool::negationexpression_is_not_abstract():
    assert not inspect.isabstract(cool::NegationExpression)


def test_cool::negationexpression_constructor_exists():
    assert callable(cool::NegationExpression.__init__)


def test_cool::negationexpression_constructor_args():
    sig = inspect.signature(cool::NegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::dispatchexpression_is_not_abstract():
    assert not inspect.isabstract(cool::DispatchExpression)


def test_cool::dispatchexpression_constructor_exists():
    assert callable(cool::DispatchExpression.__init__)


def test_cool::dispatchexpression_constructor_args():
    sig = inspect.signature(cool::DispatchExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::integercompositeexpression_is_not_abstract():
    assert not inspect.isabstract(cool::IntegerCompositeExpression)


def test_cool::integercompositeexpression_constructor_exists():
    assert callable(cool::IntegerCompositeExpression.__init__)


def test_cool::integercompositeexpression_constructor_args():
    sig = inspect.signature(cool::IntegerCompositeExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::isvoidexpression_is_not_abstract():
    assert not inspect.isabstract(cool::IsvoidExpression)


def test_cool::isvoidexpression_constructor_exists():
    assert callable(cool::IsvoidExpression.__init__)


def test_cool::isvoidexpression_constructor_args():
    sig = inspect.signature(cool::IsvoidExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::loopexpression_is_not_abstract():
    assert not inspect.isabstract(cool::LoopExpression)


def test_cool::loopexpression_constructor_exists():
    assert callable(cool::LoopExpression.__init__)


def test_cool::loopexpression_constructor_args():
    sig = inspect.signature(cool::LoopExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::blockexpression_is_not_abstract():
    assert not inspect.isabstract(cool::BlockExpression)


def test_cool::blockexpression_constructor_exists():
    assert callable(cool::BlockExpression.__init__)


def test_cool::blockexpression_constructor_args():
    sig = inspect.signature(cool::BlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::letexpression_is_not_abstract():
    assert not inspect.isabstract(cool::LetExpression)


def test_cool::letexpression_constructor_exists():
    assert callable(cool::LetExpression.__init__)


def test_cool::letexpression_constructor_args():
    sig = inspect.signature(cool::LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cool::ConditionalExpression)


def test_cool::conditionalexpression_constructor_exists():
    assert callable(cool::ConditionalExpression.__init__)


def test_cool::conditionalexpression_constructor_args():
    sig = inspect.signature(cool::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::newexpression_is_not_abstract():
    assert not inspect.isabstract(cool::NewExpression)


def test_cool::newexpression_constructor_exists():
    assert callable(cool::NewExpression.__init__)


def test_cool::newexpression_constructor_args():
    sig = inspect.signature(cool::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::selftypeliteral_is_not_abstract():
    assert not inspect.isabstract(cool::SelfTypeLiteral)


def test_cool::selftypeliteral_constructor_exists():
    assert callable(cool::SelfTypeLiteral.__init__)


def test_cool::selftypeliteral_constructor_args():
    sig = inspect.signature(cool::SelfTypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_cool::compareexpression_is_not_abstract():
    assert not inspect.isabstract(cool::CompareExpression)


def test_cool::compareexpression_constructor_exists():
    assert callable(cool::CompareExpression.__init__)


def test_cool::compareexpression_constructor_args():
    sig = inspect.signature(cool::CompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_cool::compareexpression_has_op():
    assert hasattr(cool::CompareExpression, "op")
    descriptor = None
    for klass in cool::CompareExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_cool::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(cool::PrimaryExpression)


def test_cool::primaryexpression_constructor_exists():
    assert callable(cool::PrimaryExpression.__init__)


def test_cool::primaryexpression_constructor_args():
    sig = inspect.signature(cool::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::expression_is_not_abstract():
    assert not inspect.isabstract(cool::Expression)


def test_cool::expression_constructor_exists():
    assert callable(cool::Expression.__init__)


def test_cool::expression_constructor_args():
    sig = inspect.signature(cool::Expression.__init__)
    params = list(sig.parameters.keys())



def test_feature::_is_not_abstract():
    assert not inspect.isabstract(Feature::)


def test_feature::_constructor_exists():
    assert callable(Feature::.__init__)


def test_feature::_constructor_args():
    sig = inspect.signature(Feature::.__init__)
    params = list(sig.parameters.keys())



def test_cool::method_is_not_abstract():
    assert not inspect.isabstract(cool::Method)


def test_cool::method_constructor_exists():
    assert callable(cool::Method.__init__)


def test_cool::method_constructor_args():
    sig = inspect.signature(cool::Method.__init__)
    params = list(sig.parameters.keys())



def test_cool::attr_is_not_abstract():
    assert not inspect.isabstract(cool::Attr)


def test_cool::attr_constructor_exists():
    assert callable(cool::Attr.__init__)


def test_cool::attr_constructor_args():
    sig = inspect.signature(cool::Attr.__init__)
    params = list(sig.parameters.keys())



def test_cool::type_is_not_abstract():
    assert not inspect.isabstract(cool::Type)


def test_cool::type_constructor_exists():
    assert callable(cool::Type.__init__)


def test_cool::type_constructor_args():
    sig = inspect.signature(cool::Type.__init__)
    params = list(sig.parameters.keys())



def test_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_cool::formal_is_not_abstract():
    assert not inspect.isabstract(cool::Formal)


def test_cool::formal_constructor_exists():
    assert callable(cool::Formal.__init__)


def test_cool::formal_constructor_args():
    sig = inspect.signature(cool::Formal.__init__)
    params = list(sig.parameters.keys())



def test_cool::feature::_is_not_abstract():
    assert not inspect.isabstract(cool::Feature::)


def test_cool::feature::_constructor_exists():
    assert callable(cool::Feature::.__init__)


def test_cool::feature::_constructor_args():
    sig = inspect.signature(cool::Feature::.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_cool::parenexpression_is_not_abstract():
    assert not inspect.isabstract(cool::ParenExpression)


def test_cool::parenexpression_constructor_exists():
    assert callable(cool::ParenExpression.__init__)


def test_cool::parenexpression_constructor_args():
    sig = inspect.signature(cool::ParenExpression.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_cool::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(cool::BooleanLiteral)


def test_cool::booleanliteral_constructor_exists():
    assert callable(cool::BooleanLiteral.__init__)


def test_cool::booleanliteral_constructor_args():
    sig = inspect.signature(cool::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cool::booleanliteral_has_value():
    assert hasattr(cool::BooleanLiteral, "value")
    descriptor = None
    for klass in cool::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cool::stringliteral_is_not_abstract():
    assert not inspect.isabstract(cool::StringLiteral)


def test_cool::stringliteral_constructor_exists():
    assert callable(cool::StringLiteral.__init__)


def test_cool::stringliteral_constructor_args():
    sig = inspect.signature(cool::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cool::stringliteral_has_value():
    assert hasattr(cool::StringLiteral, "value")
    descriptor = None
    for klass in cool::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cool::numberliteral_is_not_abstract():
    assert not inspect.isabstract(cool::NumberLiteral)


def test_cool::numberliteral_constructor_exists():
    assert callable(cool::NumberLiteral.__init__)


def test_cool::numberliteral_constructor_args():
    sig = inspect.signature(cool::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cool::numberliteral_has_value():
    assert hasattr(cool::NumberLiteral, "value")
    descriptor = None
    for klass in cool::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cool::literal_is_not_abstract():
    assert not inspect.isabstract(cool::Literal)


def test_cool::literal_constructor_exists():
    assert callable(cool::Literal.__init__)


def test_cool::literal_constructor_args():
    sig = inspect.signature(cool::Literal.__init__)
    params = list(sig.parameters.keys())



def test_cool::identifiableelement_is_not_abstract():
    assert not inspect.isabstract(cool::IdentifiableElement)


def test_cool::identifiableelement_constructor_exists():
    assert callable(cool::IdentifiableElement.__init__)


def test_cool::identifiableelement_constructor_args():
    sig = inspect.signature(cool::IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cool::identifiableelement_has_name():
    assert hasattr(cool::IdentifiableElement, "name")
    descriptor = None
    for klass in cool::IdentifiableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cool::identifierrefexpression_is_not_abstract():
    assert not inspect.isabstract(cool::IdentifierRefExpression)


def test_cool::identifierrefexpression_constructor_exists():
    assert callable(cool::IdentifierRefExpression.__init__)


def test_cool::identifierrefexpression_constructor_args():
    sig = inspect.signature(cool::IdentifierRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::class::_is_not_abstract():
    assert not inspect.isabstract(cool::Class::)


def test_cool::class::_constructor_exists():
    assert callable(cool::Class::.__init__)


def test_cool::class::_constructor_args():
    sig = inspect.signature(cool::Class::.__init__)
    params = list(sig.parameters.keys())



def test_cool::program_is_not_abstract():
    assert not inspect.isabstract(cool::Program)


def test_cool::program_constructor_exists():
    assert callable(cool::Program.__init__)


def test_cool::program_constructor_args():
    sig = inspect.signature(cool::Program.__init__)
    params = list(sig.parameters.keys())



def test_cool::div_is_not_abstract():
    assert not inspect.isabstract(cool::Div)


def test_cool::div_constructor_exists():
    assert callable(cool::Div.__init__)


def test_cool::div_constructor_args():
    sig = inspect.signature(cool::Div.__init__)
    params = list(sig.parameters.keys())



def test_cool::multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(cool::MultiplicationExpression)


def test_cool::multiplicationexpression_constructor_exists():
    assert callable(cool::MultiplicationExpression.__init__)


def test_cool::multiplicationexpression_constructor_args():
    sig = inspect.signature(cool::MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::minus_is_not_abstract():
    assert not inspect.isabstract(cool::Minus)


def test_cool::minus_constructor_exists():
    assert callable(cool::Minus.__init__)


def test_cool::minus_constructor_args():
    sig = inspect.signature(cool::Minus.__init__)
    params = list(sig.parameters.keys())



def test_cool::additionexpression_is_not_abstract():
    assert not inspect.isabstract(cool::AdditionExpression)


def test_cool::additionexpression_constructor_exists():
    assert callable(cool::AdditionExpression.__init__)


def test_cool::additionexpression_constructor_args():
    sig = inspect.signature(cool::AdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::case_is_not_abstract():
    assert not inspect.isabstract(cool::Case)


def test_cool::case_constructor_exists():
    assert callable(cool::Case.__init__)


def test_cool::case_constructor_args():
    sig = inspect.signature(cool::Case.__init__)
    params = list(sig.parameters.keys())



def test_cool::caseexpression_is_not_abstract():
    assert not inspect.isabstract(cool::CaseExpression)


def test_cool::caseexpression_constructor_exists():
    assert callable(cool::CaseExpression.__init__)


def test_cool::caseexpression_constructor_args():
    sig = inspect.signature(cool::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool::letdeclaration_is_not_abstract():
    assert not inspect.isabstract(cool::LetDeclaration)


def test_cool::letdeclaration_constructor_exists():
    assert callable(cool::LetDeclaration.__init__)


def test_cool::letdeclaration_constructor_args():
    sig = inspect.signature(cool::LetDeclaration.__init__)
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
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
cool::AssignmentExpression_strategy = st.builds(
    cool::AssignmentExpression,
    name=
        safe_text
)
cool::NegationExpression_strategy = st.builds(
    cool::NegationExpression,
)
cool::DispatchExpression_strategy = st.builds(
    cool::DispatchExpression,
)
cool::IntegerCompositeExpression_strategy = st.builds(
    cool::IntegerCompositeExpression,
)
cool::IsvoidExpression_strategy = st.builds(
    cool::IsvoidExpression,
)
cool::LoopExpression_strategy = st.builds(
    cool::LoopExpression,
)
cool::BlockExpression_strategy = st.builds(
    cool::BlockExpression,
)
cool::LetExpression_strategy = st.builds(
    cool::LetExpression,
)
cool::ConditionalExpression_strategy = st.builds(
    cool::ConditionalExpression,
)
cool::NewExpression_strategy = st.builds(
    cool::NewExpression,
)
cool::SelfTypeLiteral_strategy = st.builds(
    cool::SelfTypeLiteral,
)
Expression_strategy = st.builds(
    Expression,
)
cool::CompareExpression_strategy = st.builds(
    cool::CompareExpression,
    op=
        safe_text
)
cool::PrimaryExpression_strategy = st.builds(
    cool::PrimaryExpression,
)
cool::Expression_strategy = st.builds(
    cool::Expression,
)
Feature::_strategy = st.builds(
    Feature::,
)
cool::Method_strategy = st.builds(
    cool::Method,
)
cool::Attr_strategy = st.builds(
    cool::Attr,
)
cool::Type_strategy = st.builds(
    cool::Type,
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
)
cool::Formal_strategy = st.builds(
    cool::Formal,
)
cool::Feature::_strategy = st.builds(
    cool::Feature::,
)
Type_strategy = st.builds(
    Type,
)
cool::ParenExpression_strategy = st.builds(
    cool::ParenExpression,
)
Literal_strategy = st.builds(
    Literal,
)
cool::BooleanLiteral_strategy = st.builds(
    cool::BooleanLiteral,
    value=
        safe_text
)
cool::StringLiteral_strategy = st.builds(
    cool::StringLiteral,
    value=
        safe_text
)
cool::NumberLiteral_strategy = st.builds(
    cool::NumberLiteral,
    value=
        st.integers()
)
cool::Literal_strategy = st.builds(
    cool::Literal,
)
cool::IdentifiableElement_strategy = st.builds(
    cool::IdentifiableElement,
    name=
        safe_text
)
cool::IdentifierRefExpression_strategy = st.builds(
    cool::IdentifierRefExpression,
)
cool::Class::_strategy = st.builds(
    cool::Class::,
)
cool::Program_strategy = st.builds(
    cool::Program,
)
cool::Div_strategy = st.builds(
    cool::Div,
)
cool::MultiplicationExpression_strategy = st.builds(
    cool::MultiplicationExpression,
)
cool::Minus_strategy = st.builds(
    cool::Minus,
)
cool::AdditionExpression_strategy = st.builds(
    cool::AdditionExpression,
)
cool::Case_strategy = st.builds(
    cool::Case,
)
cool::CaseExpression_strategy = st.builds(
    cool::CaseExpression,
)
cool::LetDeclaration_strategy = st.builds(
    cool::LetDeclaration,
)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=cool::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_cool::assignmentexpression_instantiation(instance):
    assert isinstance(instance, cool::AssignmentExpression)

@given(instance=cool::AssignmentExpression_strategy)
def test_cool::assignmentexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cool::AssignmentExpression_strategy)
def test_cool::assignmentexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cool::NegationExpression_strategy)
@settings(max_examples=50)
def test_cool::negationexpression_instantiation(instance):
    assert isinstance(instance, cool::NegationExpression)

@given(instance=cool::DispatchExpression_strategy)
@settings(max_examples=50)
def test_cool::dispatchexpression_instantiation(instance):
    assert isinstance(instance, cool::DispatchExpression)

@given(instance=cool::IntegerCompositeExpression_strategy)
@settings(max_examples=50)
def test_cool::integercompositeexpression_instantiation(instance):
    assert isinstance(instance, cool::IntegerCompositeExpression)

@given(instance=cool::IsvoidExpression_strategy)
@settings(max_examples=50)
def test_cool::isvoidexpression_instantiation(instance):
    assert isinstance(instance, cool::IsvoidExpression)

@given(instance=cool::LoopExpression_strategy)
@settings(max_examples=50)
def test_cool::loopexpression_instantiation(instance):
    assert isinstance(instance, cool::LoopExpression)

@given(instance=cool::BlockExpression_strategy)
@settings(max_examples=50)
def test_cool::blockexpression_instantiation(instance):
    assert isinstance(instance, cool::BlockExpression)

@given(instance=cool::LetExpression_strategy)
@settings(max_examples=50)
def test_cool::letexpression_instantiation(instance):
    assert isinstance(instance, cool::LetExpression)

@given(instance=cool::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_cool::conditionalexpression_instantiation(instance):
    assert isinstance(instance, cool::ConditionalExpression)

@given(instance=cool::NewExpression_strategy)
@settings(max_examples=50)
def test_cool::newexpression_instantiation(instance):
    assert isinstance(instance, cool::NewExpression)

@given(instance=cool::SelfTypeLiteral_strategy)
@settings(max_examples=50)
def test_cool::selftypeliteral_instantiation(instance):
    assert isinstance(instance, cool::SelfTypeLiteral)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=cool::CompareExpression_strategy)
@settings(max_examples=50)
def test_cool::compareexpression_instantiation(instance):
    assert isinstance(instance, cool::CompareExpression)

@given(instance=cool::CompareExpression_strategy)
def test_cool::compareexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=cool::CompareExpression_strategy)
def test_cool::compareexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=cool::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_cool::primaryexpression_instantiation(instance):
    assert isinstance(instance, cool::PrimaryExpression)

@given(instance=cool::Expression_strategy)
@settings(max_examples=50)
def test_cool::expression_instantiation(instance):
    assert isinstance(instance, cool::Expression)

@given(instance=Feature::_strategy)
@settings(max_examples=50)
def test_feature::_instantiation(instance):
    assert isinstance(instance, Feature::)

@given(instance=cool::Method_strategy)
@settings(max_examples=50)
def test_cool::method_instantiation(instance):
    assert isinstance(instance, cool::Method)

@given(instance=cool::Attr_strategy)
@settings(max_examples=50)
def test_cool::attr_instantiation(instance):
    assert isinstance(instance, cool::Attr)

@given(instance=cool::Type_strategy)
@settings(max_examples=50)
def test_cool::type_instantiation(instance):
    assert isinstance(instance, cool::Type)

@given(instance=IdentifiableElement_strategy)
@settings(max_examples=50)
def test_identifiableelement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)

@given(instance=cool::Formal_strategy)
@settings(max_examples=50)
def test_cool::formal_instantiation(instance):
    assert isinstance(instance, cool::Formal)

@given(instance=cool::Feature::_strategy)
@settings(max_examples=50)
def test_cool::feature::_instantiation(instance):
    assert isinstance(instance, cool::Feature::)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=cool::ParenExpression_strategy)
@settings(max_examples=50)
def test_cool::parenexpression_instantiation(instance):
    assert isinstance(instance, cool::ParenExpression)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=cool::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_cool::booleanliteral_instantiation(instance):
    assert isinstance(instance, cool::BooleanLiteral)

@given(instance=cool::BooleanLiteral_strategy)
def test_cool::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cool::BooleanLiteral_strategy)
def test_cool::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cool::StringLiteral_strategy)
@settings(max_examples=50)
def test_cool::stringliteral_instantiation(instance):
    assert isinstance(instance, cool::StringLiteral)

@given(instance=cool::StringLiteral_strategy)
def test_cool::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cool::StringLiteral_strategy)
def test_cool::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cool::NumberLiteral_strategy)
@settings(max_examples=50)
def test_cool::numberliteral_instantiation(instance):
    assert isinstance(instance, cool::NumberLiteral)

@given(instance=cool::NumberLiteral_strategy)
def test_cool::numberliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=cool::NumberLiteral_strategy)
def test_cool::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cool::Literal_strategy)
@settings(max_examples=50)
def test_cool::literal_instantiation(instance):
    assert isinstance(instance, cool::Literal)

@given(instance=cool::IdentifiableElement_strategy)
@settings(max_examples=50)
def test_cool::identifiableelement_instantiation(instance):
    assert isinstance(instance, cool::IdentifiableElement)

@given(instance=cool::IdentifiableElement_strategy)
def test_cool::identifiableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cool::IdentifiableElement_strategy)
def test_cool::identifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cool::IdentifierRefExpression_strategy)
@settings(max_examples=50)
def test_cool::identifierrefexpression_instantiation(instance):
    assert isinstance(instance, cool::IdentifierRefExpression)

@given(instance=cool::Class::_strategy)
@settings(max_examples=50)
def test_cool::class::_instantiation(instance):
    assert isinstance(instance, cool::Class::)

@given(instance=cool::Program_strategy)
@settings(max_examples=50)
def test_cool::program_instantiation(instance):
    assert isinstance(instance, cool::Program)

@given(instance=cool::Div_strategy)
@settings(max_examples=50)
def test_cool::div_instantiation(instance):
    assert isinstance(instance, cool::Div)

@given(instance=cool::MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_cool::multiplicationexpression_instantiation(instance):
    assert isinstance(instance, cool::MultiplicationExpression)

@given(instance=cool::Minus_strategy)
@settings(max_examples=50)
def test_cool::minus_instantiation(instance):
    assert isinstance(instance, cool::Minus)

@given(instance=cool::AdditionExpression_strategy)
@settings(max_examples=50)
def test_cool::additionexpression_instantiation(instance):
    assert isinstance(instance, cool::AdditionExpression)

@given(instance=cool::Case_strategy)
@settings(max_examples=50)
def test_cool::case_instantiation(instance):
    assert isinstance(instance, cool::Case)

@given(instance=cool::CaseExpression_strategy)
@settings(max_examples=50)
def test_cool::caseexpression_instantiation(instance):
    assert isinstance(instance, cool::CaseExpression)

@given(instance=cool::LetDeclaration_strategy)
@settings(max_examples=50)
def test_cool::letdeclaration_instantiation(instance):
    assert isinstance(instance, cool::LetDeclaration)
