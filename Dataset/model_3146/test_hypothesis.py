import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Axis,
    XPath::FollowingAxis,
    XPath::NamespaceAxis,
    XPath::FollowingSiblingAxis,
    XPath::DescendantOrSelfAxis,
    XPath::AncestorOrSelfAxis,
    XPath::DescendantAxis,
    XPath::PrecedingSiblingAxis,
    XPath::ChildAxis,
    XPath::ParentAxis,
    XPath::AttributeAxis,
    XPath::SelfAxis,
    XPath::PrecedingAxis,
    XPath::AncestorAxis,
    NodeTest,
    XPath::WildCardTest,
    XPath::IsNodeTest,
    XPath::IsTextTest,
    LiteralExp,
    XPath::StringExp,
    XPath::IntegerExp,
    NamedElement,
    XPath::NameTest,
    Expression,
    XPath::LiteralExp,
    XPath::OperatorCallExp,
    XPath::PathExpression,
    XPath::FunctionCallExp,
    XPath::VariableExp,
    LocatedElement,
    XPath::Axis,
    XPath::Step,
    XPath::Predicate,
    XPath::Expression,
    XPath::NodeTest,
    XPath::NamedElement,
    XPath::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_axis_is_not_abstract():
    assert not inspect.isabstract(Axis)


def test_axis_constructor_exists():
    assert callable(Axis.__init__)


def test_axis_constructor_args():
    sig = inspect.signature(Axis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::followingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::FollowingAxis)


def test_xpath::followingaxis_constructor_exists():
    assert callable(XPath::FollowingAxis.__init__)


def test_xpath::followingaxis_constructor_args():
    sig = inspect.signature(XPath::FollowingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::namespaceaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::NamespaceAxis)


def test_xpath::namespaceaxis_constructor_exists():
    assert callable(XPath::NamespaceAxis.__init__)


def test_xpath::namespaceaxis_constructor_args():
    sig = inspect.signature(XPath::NamespaceAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::followingsiblingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::FollowingSiblingAxis)


def test_xpath::followingsiblingaxis_constructor_exists():
    assert callable(XPath::FollowingSiblingAxis.__init__)


def test_xpath::followingsiblingaxis_constructor_args():
    sig = inspect.signature(XPath::FollowingSiblingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::descendantorselfaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::DescendantOrSelfAxis)


def test_xpath::descendantorselfaxis_constructor_exists():
    assert callable(XPath::DescendantOrSelfAxis.__init__)


def test_xpath::descendantorselfaxis_constructor_args():
    sig = inspect.signature(XPath::DescendantOrSelfAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::ancestororselfaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::AncestorOrSelfAxis)


def test_xpath::ancestororselfaxis_constructor_exists():
    assert callable(XPath::AncestorOrSelfAxis.__init__)


def test_xpath::ancestororselfaxis_constructor_args():
    sig = inspect.signature(XPath::AncestorOrSelfAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::descendantaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::DescendantAxis)


def test_xpath::descendantaxis_constructor_exists():
    assert callable(XPath::DescendantAxis.__init__)


def test_xpath::descendantaxis_constructor_args():
    sig = inspect.signature(XPath::DescendantAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::precedingsiblingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::PrecedingSiblingAxis)


def test_xpath::precedingsiblingaxis_constructor_exists():
    assert callable(XPath::PrecedingSiblingAxis.__init__)


def test_xpath::precedingsiblingaxis_constructor_args():
    sig = inspect.signature(XPath::PrecedingSiblingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::childaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::ChildAxis)


def test_xpath::childaxis_constructor_exists():
    assert callable(XPath::ChildAxis.__init__)


def test_xpath::childaxis_constructor_args():
    sig = inspect.signature(XPath::ChildAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::parentaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::ParentAxis)


def test_xpath::parentaxis_constructor_exists():
    assert callable(XPath::ParentAxis.__init__)


def test_xpath::parentaxis_constructor_args():
    sig = inspect.signature(XPath::ParentAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::attributeaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::AttributeAxis)


def test_xpath::attributeaxis_constructor_exists():
    assert callable(XPath::AttributeAxis.__init__)


def test_xpath::attributeaxis_constructor_args():
    sig = inspect.signature(XPath::AttributeAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::selfaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::SelfAxis)


def test_xpath::selfaxis_constructor_exists():
    assert callable(XPath::SelfAxis.__init__)


def test_xpath::selfaxis_constructor_args():
    sig = inspect.signature(XPath::SelfAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::precedingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath::PrecedingAxis)


def test_xpath::precedingaxis_constructor_exists():
    assert callable(XPath::PrecedingAxis.__init__)


def test_xpath::precedingaxis_constructor_args():
    sig = inspect.signature(XPath::PrecedingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::ancestoraxis_is_not_abstract():
    assert not inspect.isabstract(XPath::AncestorAxis)


def test_xpath::ancestoraxis_constructor_exists():
    assert callable(XPath::AncestorAxis.__init__)


def test_xpath::ancestoraxis_constructor_args():
    sig = inspect.signature(XPath::AncestorAxis.__init__)
    params = list(sig.parameters.keys())



def test_nodetest_is_not_abstract():
    assert not inspect.isabstract(NodeTest)


def test_nodetest_constructor_exists():
    assert callable(NodeTest.__init__)


def test_nodetest_constructor_args():
    sig = inspect.signature(NodeTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath::wildcardtest_is_not_abstract():
    assert not inspect.isabstract(XPath::WildCardTest)


def test_xpath::wildcardtest_constructor_exists():
    assert callable(XPath::WildCardTest.__init__)


def test_xpath::wildcardtest_constructor_args():
    sig = inspect.signature(XPath::WildCardTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath::isnodetest_is_not_abstract():
    assert not inspect.isabstract(XPath::IsNodeTest)


def test_xpath::isnodetest_constructor_exists():
    assert callable(XPath::IsNodeTest.__init__)


def test_xpath::isnodetest_constructor_args():
    sig = inspect.signature(XPath::IsNodeTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath::istexttest_is_not_abstract():
    assert not inspect.isabstract(XPath::IsTextTest)


def test_xpath::istexttest_constructor_exists():
    assert callable(XPath::IsTextTest.__init__)


def test_xpath::istexttest_constructor_args():
    sig = inspect.signature(XPath::IsTextTest.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::stringexp_is_not_abstract():
    assert not inspect.isabstract(XPath::StringExp)


def test_xpath::stringexp_constructor_exists():
    assert callable(XPath::StringExp.__init__)


def test_xpath::stringexp_constructor_args():
    sig = inspect.signature(XPath::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath::stringexp_has_symbol():
    assert hasattr(XPath::StringExp, "symbol")
    descriptor = None
    for klass in XPath::StringExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_xpath::integerexp_is_not_abstract():
    assert not inspect.isabstract(XPath::IntegerExp)


def test_xpath::integerexp_constructor_exists():
    assert callable(XPath::IntegerExp.__init__)


def test_xpath::integerexp_constructor_args():
    sig = inspect.signature(XPath::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath::integerexp_has_symbol():
    assert hasattr(XPath::IntegerExp, "symbol")
    descriptor = None
    for klass in XPath::IntegerExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_xpath::nametest_is_not_abstract():
    assert not inspect.isabstract(XPath::NameTest)


def test_xpath::nametest_constructor_exists():
    assert callable(XPath::NameTest.__init__)


def test_xpath::nametest_constructor_args():
    sig = inspect.signature(XPath::NameTest.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath::literalexp_is_not_abstract():
    assert not inspect.isabstract(XPath::LiteralExp)


def test_xpath::literalexp_constructor_exists():
    assert callable(XPath::LiteralExp.__init__)


def test_xpath::literalexp_constructor_args():
    sig = inspect.signature(XPath::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(XPath::OperatorCallExp)


def test_xpath::operatorcallexp_constructor_exists():
    assert callable(XPath::OperatorCallExp.__init__)


def test_xpath::operatorcallexp_constructor_args():
    sig = inspect.signature(XPath::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::pathexpression_is_not_abstract():
    assert not inspect.isabstract(XPath::PathExpression)


def test_xpath::pathexpression_constructor_exists():
    assert callable(XPath::PathExpression.__init__)


def test_xpath::pathexpression_constructor_args():
    sig = inspect.signature(XPath::PathExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isAbsolute" in params, "Missing parameter 'isAbsolute'"

def test_xpath::pathexpression_has_isAbsolute():
    assert hasattr(XPath::PathExpression, "isAbsolute")
    descriptor = None
    for klass in XPath::PathExpression.__mro__:
        if "isAbsolute" in klass.__dict__:
            descriptor = klass.__dict__["isAbsolute"]
            break
    assert isinstance(descriptor, property)



def test_xpath::functioncallexp_is_not_abstract():
    assert not inspect.isabstract(XPath::FunctionCallExp)


def test_xpath::functioncallexp_constructor_exists():
    assert callable(XPath::FunctionCallExp.__init__)


def test_xpath::functioncallexp_constructor_args():
    sig = inspect.signature(XPath::FunctionCallExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::variableexp_is_not_abstract():
    assert not inspect.isabstract(XPath::VariableExp)


def test_xpath::variableexp_constructor_exists():
    assert callable(XPath::VariableExp.__init__)


def test_xpath::variableexp_constructor_args():
    sig = inspect.signature(XPath::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_xpath::axis_is_not_abstract():
    assert not inspect.isabstract(XPath::Axis)


def test_xpath::axis_constructor_exists():
    assert callable(XPath::Axis.__init__)


def test_xpath::axis_constructor_args():
    sig = inspect.signature(XPath::Axis.__init__)
    params = list(sig.parameters.keys())



def test_xpath::step_is_not_abstract():
    assert not inspect.isabstract(XPath::Step)


def test_xpath::step_constructor_exists():
    assert callable(XPath::Step.__init__)


def test_xpath::step_constructor_args():
    sig = inspect.signature(XPath::Step.__init__)
    params = list(sig.parameters.keys())



def test_xpath::predicate_is_not_abstract():
    assert not inspect.isabstract(XPath::Predicate)


def test_xpath::predicate_constructor_exists():
    assert callable(XPath::Predicate.__init__)


def test_xpath::predicate_constructor_args():
    sig = inspect.signature(XPath::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_xpath::expression_is_not_abstract():
    assert not inspect.isabstract(XPath::Expression)


def test_xpath::expression_constructor_exists():
    assert callable(XPath::Expression.__init__)


def test_xpath::expression_constructor_args():
    sig = inspect.signature(XPath::Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath::nodetest_is_not_abstract():
    assert not inspect.isabstract(XPath::NodeTest)


def test_xpath::nodetest_constructor_exists():
    assert callable(XPath::NodeTest.__init__)


def test_xpath::nodetest_constructor_args():
    sig = inspect.signature(XPath::NodeTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath::namedelement_is_not_abstract():
    assert not inspect.isabstract(XPath::NamedElement)


def test_xpath::namedelement_constructor_exists():
    assert callable(XPath::NamedElement.__init__)


def test_xpath::namedelement_constructor_args():
    sig = inspect.signature(XPath::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xpath::namedelement_has_name():
    assert hasattr(XPath::NamedElement, "name")
    descriptor = None
    for klass in XPath::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpath::locatedelement_is_not_abstract():
    assert not inspect.isabstract(XPath::LocatedElement)


def test_xpath::locatedelement_constructor_exists():
    assert callable(XPath::LocatedElement.__init__)


def test_xpath::locatedelement_constructor_args():
    sig = inspect.signature(XPath::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_xpath::locatedelement_has_commentsAfter():
    assert hasattr(XPath::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in XPath::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_xpath::locatedelement_has_location():
    assert hasattr(XPath::LocatedElement, "location")
    descriptor = None
    for klass in XPath::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_xpath::locatedelement_has_commentsBefore():
    assert hasattr(XPath::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in XPath::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
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
Axis_strategy = st.builds(
    Axis,
)
XPath::FollowingAxis_strategy = st.builds(
    XPath::FollowingAxis,
)
XPath::NamespaceAxis_strategy = st.builds(
    XPath::NamespaceAxis,
)
XPath::FollowingSiblingAxis_strategy = st.builds(
    XPath::FollowingSiblingAxis,
)
XPath::DescendantOrSelfAxis_strategy = st.builds(
    XPath::DescendantOrSelfAxis,
)
XPath::AncestorOrSelfAxis_strategy = st.builds(
    XPath::AncestorOrSelfAxis,
)
XPath::DescendantAxis_strategy = st.builds(
    XPath::DescendantAxis,
)
XPath::PrecedingSiblingAxis_strategy = st.builds(
    XPath::PrecedingSiblingAxis,
)
XPath::ChildAxis_strategy = st.builds(
    XPath::ChildAxis,
)
XPath::ParentAxis_strategy = st.builds(
    XPath::ParentAxis,
)
XPath::AttributeAxis_strategy = st.builds(
    XPath::AttributeAxis,
)
XPath::SelfAxis_strategy = st.builds(
    XPath::SelfAxis,
)
XPath::PrecedingAxis_strategy = st.builds(
    XPath::PrecedingAxis,
)
XPath::AncestorAxis_strategy = st.builds(
    XPath::AncestorAxis,
)
NodeTest_strategy = st.builds(
    NodeTest,
)
XPath::WildCardTest_strategy = st.builds(
    XPath::WildCardTest,
)
XPath::IsNodeTest_strategy = st.builds(
    XPath::IsNodeTest,
)
XPath::IsTextTest_strategy = st.builds(
    XPath::IsTextTest,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
XPath::StringExp_strategy = st.builds(
    XPath::StringExp,
    symbol=
        safe_text
)
XPath::IntegerExp_strategy = st.builds(
    XPath::IntegerExp,
    symbol=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
XPath::NameTest_strategy = st.builds(
    XPath::NameTest,
)
Expression_strategy = st.builds(
    Expression,
)
XPath::LiteralExp_strategy = st.builds(
    XPath::LiteralExp,
)
XPath::OperatorCallExp_strategy = st.builds(
    XPath::OperatorCallExp,
)
XPath::PathExpression_strategy = st.builds(
    XPath::PathExpression,
    isAbsolute=
        safe_text
)
XPath::FunctionCallExp_strategy = st.builds(
    XPath::FunctionCallExp,
)
XPath::VariableExp_strategy = st.builds(
    XPath::VariableExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
XPath::Axis_strategy = st.builds(
    XPath::Axis,
)
XPath::Step_strategy = st.builds(
    XPath::Step,
)
XPath::Predicate_strategy = st.builds(
    XPath::Predicate,
)
XPath::Expression_strategy = st.builds(
    XPath::Expression,
)
XPath::NodeTest_strategy = st.builds(
    XPath::NodeTest,
)
XPath::NamedElement_strategy = st.builds(
    XPath::NamedElement,
    name=
        safe_text
)
XPath::LocatedElement_strategy = st.builds(
    XPath::LocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)

@given(instance=Axis_strategy)
@settings(max_examples=50)
def test_axis_instantiation(instance):
    assert isinstance(instance, Axis)

@given(instance=XPath::FollowingAxis_strategy)
@settings(max_examples=50)
def test_xpath::followingaxis_instantiation(instance):
    assert isinstance(instance, XPath::FollowingAxis)

@given(instance=XPath::NamespaceAxis_strategy)
@settings(max_examples=50)
def test_xpath::namespaceaxis_instantiation(instance):
    assert isinstance(instance, XPath::NamespaceAxis)

@given(instance=XPath::FollowingSiblingAxis_strategy)
@settings(max_examples=50)
def test_xpath::followingsiblingaxis_instantiation(instance):
    assert isinstance(instance, XPath::FollowingSiblingAxis)

@given(instance=XPath::DescendantOrSelfAxis_strategy)
@settings(max_examples=50)
def test_xpath::descendantorselfaxis_instantiation(instance):
    assert isinstance(instance, XPath::DescendantOrSelfAxis)

@given(instance=XPath::AncestorOrSelfAxis_strategy)
@settings(max_examples=50)
def test_xpath::ancestororselfaxis_instantiation(instance):
    assert isinstance(instance, XPath::AncestorOrSelfAxis)

@given(instance=XPath::DescendantAxis_strategy)
@settings(max_examples=50)
def test_xpath::descendantaxis_instantiation(instance):
    assert isinstance(instance, XPath::DescendantAxis)

@given(instance=XPath::PrecedingSiblingAxis_strategy)
@settings(max_examples=50)
def test_xpath::precedingsiblingaxis_instantiation(instance):
    assert isinstance(instance, XPath::PrecedingSiblingAxis)

@given(instance=XPath::ChildAxis_strategy)
@settings(max_examples=50)
def test_xpath::childaxis_instantiation(instance):
    assert isinstance(instance, XPath::ChildAxis)

@given(instance=XPath::ParentAxis_strategy)
@settings(max_examples=50)
def test_xpath::parentaxis_instantiation(instance):
    assert isinstance(instance, XPath::ParentAxis)

@given(instance=XPath::AttributeAxis_strategy)
@settings(max_examples=50)
def test_xpath::attributeaxis_instantiation(instance):
    assert isinstance(instance, XPath::AttributeAxis)

@given(instance=XPath::SelfAxis_strategy)
@settings(max_examples=50)
def test_xpath::selfaxis_instantiation(instance):
    assert isinstance(instance, XPath::SelfAxis)

@given(instance=XPath::PrecedingAxis_strategy)
@settings(max_examples=50)
def test_xpath::precedingaxis_instantiation(instance):
    assert isinstance(instance, XPath::PrecedingAxis)

@given(instance=XPath::AncestorAxis_strategy)
@settings(max_examples=50)
def test_xpath::ancestoraxis_instantiation(instance):
    assert isinstance(instance, XPath::AncestorAxis)

@given(instance=NodeTest_strategy)
@settings(max_examples=50)
def test_nodetest_instantiation(instance):
    assert isinstance(instance, NodeTest)

@given(instance=XPath::WildCardTest_strategy)
@settings(max_examples=50)
def test_xpath::wildcardtest_instantiation(instance):
    assert isinstance(instance, XPath::WildCardTest)

@given(instance=XPath::IsNodeTest_strategy)
@settings(max_examples=50)
def test_xpath::isnodetest_instantiation(instance):
    assert isinstance(instance, XPath::IsNodeTest)

@given(instance=XPath::IsTextTest_strategy)
@settings(max_examples=50)
def test_xpath::istexttest_instantiation(instance):
    assert isinstance(instance, XPath::IsTextTest)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=XPath::StringExp_strategy)
@settings(max_examples=50)
def test_xpath::stringexp_instantiation(instance):
    assert isinstance(instance, XPath::StringExp)

@given(instance=XPath::StringExp_strategy)
def test_xpath::stringexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=XPath::StringExp_strategy)
def test_xpath::stringexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=XPath::IntegerExp_strategy)
@settings(max_examples=50)
def test_xpath::integerexp_instantiation(instance):
    assert isinstance(instance, XPath::IntegerExp)

@given(instance=XPath::IntegerExp_strategy)
def test_xpath::integerexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=XPath::IntegerExp_strategy)
def test_xpath::integerexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=XPath::NameTest_strategy)
@settings(max_examples=50)
def test_xpath::nametest_instantiation(instance):
    assert isinstance(instance, XPath::NameTest)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=XPath::LiteralExp_strategy)
@settings(max_examples=50)
def test_xpath::literalexp_instantiation(instance):
    assert isinstance(instance, XPath::LiteralExp)

@given(instance=XPath::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_xpath::operatorcallexp_instantiation(instance):
    assert isinstance(instance, XPath::OperatorCallExp)

@given(instance=XPath::PathExpression_strategy)
@settings(max_examples=50)
def test_xpath::pathexpression_instantiation(instance):
    assert isinstance(instance, XPath::PathExpression)

@given(instance=XPath::PathExpression_strategy)
def test_xpath::pathexpression_isAbsolute_type(instance):
    assert isinstance(instance.isAbsolute, str)


@given(instance=XPath::PathExpression_strategy)
def test_xpath::pathexpression_isAbsolute_setter(instance):
    original = instance.isAbsolute
    instance.isAbsolute = original
    assert instance.isAbsolute == original

@given(instance=XPath::FunctionCallExp_strategy)
@settings(max_examples=50)
def test_xpath::functioncallexp_instantiation(instance):
    assert isinstance(instance, XPath::FunctionCallExp)

@given(instance=XPath::VariableExp_strategy)
@settings(max_examples=50)
def test_xpath::variableexp_instantiation(instance):
    assert isinstance(instance, XPath::VariableExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=XPath::Axis_strategy)
@settings(max_examples=50)
def test_xpath::axis_instantiation(instance):
    assert isinstance(instance, XPath::Axis)

@given(instance=XPath::Step_strategy)
@settings(max_examples=50)
def test_xpath::step_instantiation(instance):
    assert isinstance(instance, XPath::Step)

@given(instance=XPath::Predicate_strategy)
@settings(max_examples=50)
def test_xpath::predicate_instantiation(instance):
    assert isinstance(instance, XPath::Predicate)

@given(instance=XPath::Expression_strategy)
@settings(max_examples=50)
def test_xpath::expression_instantiation(instance):
    assert isinstance(instance, XPath::Expression)

@given(instance=XPath::NodeTest_strategy)
@settings(max_examples=50)
def test_xpath::nodetest_instantiation(instance):
    assert isinstance(instance, XPath::NodeTest)

@given(instance=XPath::NamedElement_strategy)
@settings(max_examples=50)
def test_xpath::namedelement_instantiation(instance):
    assert isinstance(instance, XPath::NamedElement)

@given(instance=XPath::NamedElement_strategy)
def test_xpath::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=XPath::NamedElement_strategy)
def test_xpath::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=XPath::LocatedElement_strategy)
@settings(max_examples=50)
def test_xpath::locatedelement_instantiation(instance):
    assert isinstance(instance, XPath::LocatedElement)

@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original
