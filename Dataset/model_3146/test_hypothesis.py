import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Axis,
    XPath_PrecedingAxis,
    XPath_DescendantAxis,
    XPath_AttributeAxis,
    XPath_FollowingAxis,
    XPath_AncestorOrSelfAxis,
    XPath_ChildAxis,
    XPath_ParentAxis,
    XPath_NamespaceAxis,
    XPath_FollowingSiblingAxis,
    XPath_DescendantOrSelfAxis,
    XPath_PrecedingSiblingAxis,
    XPath_SelfAxis,
    XPath_AncestorAxis,
    NodeTest,
    XPath_IsNodeTest,
    XPath_IsTextTest,
    XPath_WildCardTest,
    LiteralExp,
    XPath_StringExp,
    XPath_IntegerExp,
    NamedElement,
    XPath_NameTest,
    Expression,
    XPath_OperatorCallExp,
    XPath_PathExpression,
    XPath_LiteralExp,
    XPath_FunctionCallExp,
    XPath_VariableExp,
    LocatedElement,
    XPath_Step,
    XPath_Expression,
    XPath_NodeTest,
    XPath_Predicate,
    XPath_Axis,
    XPath_NamedElement,
    XPath_LocatedElement,
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



def test_xpath_precedingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_PrecedingAxis)


def test_xpath_precedingaxis_constructor_exists():
    assert callable(XPath_PrecedingAxis.__init__)


def test_xpath_precedingaxis_constructor_args():
    sig = inspect.signature(XPath_PrecedingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_descendantaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_DescendantAxis)


def test_xpath_descendantaxis_constructor_exists():
    assert callable(XPath_DescendantAxis.__init__)


def test_xpath_descendantaxis_constructor_args():
    sig = inspect.signature(XPath_DescendantAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_attributeaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_AttributeAxis)


def test_xpath_attributeaxis_constructor_exists():
    assert callable(XPath_AttributeAxis.__init__)


def test_xpath_attributeaxis_constructor_args():
    sig = inspect.signature(XPath_AttributeAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_followingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_FollowingAxis)


def test_xpath_followingaxis_constructor_exists():
    assert callable(XPath_FollowingAxis.__init__)


def test_xpath_followingaxis_constructor_args():
    sig = inspect.signature(XPath_FollowingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_ancestororselfaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_AncestorOrSelfAxis)


def test_xpath_ancestororselfaxis_constructor_exists():
    assert callable(XPath_AncestorOrSelfAxis.__init__)


def test_xpath_ancestororselfaxis_constructor_args():
    sig = inspect.signature(XPath_AncestorOrSelfAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_childaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_ChildAxis)


def test_xpath_childaxis_constructor_exists():
    assert callable(XPath_ChildAxis.__init__)


def test_xpath_childaxis_constructor_args():
    sig = inspect.signature(XPath_ChildAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_parentaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_ParentAxis)


def test_xpath_parentaxis_constructor_exists():
    assert callable(XPath_ParentAxis.__init__)


def test_xpath_parentaxis_constructor_args():
    sig = inspect.signature(XPath_ParentAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_namespaceaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_NamespaceAxis)


def test_xpath_namespaceaxis_constructor_exists():
    assert callable(XPath_NamespaceAxis.__init__)


def test_xpath_namespaceaxis_constructor_args():
    sig = inspect.signature(XPath_NamespaceAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_followingsiblingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_FollowingSiblingAxis)


def test_xpath_followingsiblingaxis_constructor_exists():
    assert callable(XPath_FollowingSiblingAxis.__init__)


def test_xpath_followingsiblingaxis_constructor_args():
    sig = inspect.signature(XPath_FollowingSiblingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_descendantorselfaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_DescendantOrSelfAxis)


def test_xpath_descendantorselfaxis_constructor_exists():
    assert callable(XPath_DescendantOrSelfAxis.__init__)


def test_xpath_descendantorselfaxis_constructor_args():
    sig = inspect.signature(XPath_DescendantOrSelfAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_precedingsiblingaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_PrecedingSiblingAxis)


def test_xpath_precedingsiblingaxis_constructor_exists():
    assert callable(XPath_PrecedingSiblingAxis.__init__)


def test_xpath_precedingsiblingaxis_constructor_args():
    sig = inspect.signature(XPath_PrecedingSiblingAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_selfaxis_is_not_abstract():
    assert not inspect.isabstract(XPath_SelfAxis)


def test_xpath_selfaxis_constructor_exists():
    assert callable(XPath_SelfAxis.__init__)


def test_xpath_selfaxis_constructor_args():
    sig = inspect.signature(XPath_SelfAxis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_ancestoraxis_is_not_abstract():
    assert not inspect.isabstract(XPath_AncestorAxis)


def test_xpath_ancestoraxis_constructor_exists():
    assert callable(XPath_AncestorAxis.__init__)


def test_xpath_ancestoraxis_constructor_args():
    sig = inspect.signature(XPath_AncestorAxis.__init__)
    params = list(sig.parameters.keys())



def test_nodetest_is_not_abstract():
    assert not inspect.isabstract(NodeTest)


def test_nodetest_constructor_exists():
    assert callable(NodeTest.__init__)


def test_nodetest_constructor_args():
    sig = inspect.signature(NodeTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath_isnodetest_is_not_abstract():
    assert not inspect.isabstract(XPath_IsNodeTest)


def test_xpath_isnodetest_constructor_exists():
    assert callable(XPath_IsNodeTest.__init__)


def test_xpath_isnodetest_constructor_args():
    sig = inspect.signature(XPath_IsNodeTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath_istexttest_is_not_abstract():
    assert not inspect.isabstract(XPath_IsTextTest)


def test_xpath_istexttest_constructor_exists():
    assert callable(XPath_IsTextTest.__init__)


def test_xpath_istexttest_constructor_args():
    sig = inspect.signature(XPath_IsTextTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath_wildcardtest_is_not_abstract():
    assert not inspect.isabstract(XPath_WildCardTest)


def test_xpath_wildcardtest_constructor_exists():
    assert callable(XPath_WildCardTest.__init__)


def test_xpath_wildcardtest_constructor_args():
    sig = inspect.signature(XPath_WildCardTest.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath_stringexp_is_not_abstract():
    assert not inspect.isabstract(XPath_StringExp)


def test_xpath_stringexp_constructor_exists():
    assert callable(XPath_StringExp.__init__)


def test_xpath_stringexp_constructor_args():
    sig = inspect.signature(XPath_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath_stringexp_has_symbol():
    assert hasattr(XPath_StringExp, "symbol")
    descriptor = None
    for klass in XPath_StringExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_xpath_integerexp_is_not_abstract():
    assert not inspect.isabstract(XPath_IntegerExp)


def test_xpath_integerexp_constructor_exists():
    assert callable(XPath_IntegerExp.__init__)


def test_xpath_integerexp_constructor_args():
    sig = inspect.signature(XPath_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath_integerexp_has_symbol():
    assert hasattr(XPath_IntegerExp, "symbol")
    descriptor = None
    for klass in XPath_IntegerExp.__mro__:
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



def test_xpath_nametest_is_not_abstract():
    assert not inspect.isabstract(XPath_NameTest)


def test_xpath_nametest_constructor_exists():
    assert callable(XPath_NameTest.__init__)


def test_xpath_nametest_constructor_args():
    sig = inspect.signature(XPath_NameTest.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(XPath_OperatorCallExp)


def test_xpath_operatorcallexp_constructor_exists():
    assert callable(XPath_OperatorCallExp.__init__)


def test_xpath_operatorcallexp_constructor_args():
    sig = inspect.signature(XPath_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath_pathexpression_is_not_abstract():
    assert not inspect.isabstract(XPath_PathExpression)


def test_xpath_pathexpression_constructor_exists():
    assert callable(XPath_PathExpression.__init__)


def test_xpath_pathexpression_constructor_args():
    sig = inspect.signature(XPath_PathExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isAbsolute" in params, "Missing parameter 'isAbsolute'"

def test_xpath_pathexpression_has_isAbsolute():
    assert hasattr(XPath_PathExpression, "isAbsolute")
    descriptor = None
    for klass in XPath_PathExpression.__mro__:
        if "isAbsolute" in klass.__dict__:
            descriptor = klass.__dict__["isAbsolute"]
            break
    assert isinstance(descriptor, property)



def test_xpath_literalexp_is_not_abstract():
    assert not inspect.isabstract(XPath_LiteralExp)


def test_xpath_literalexp_constructor_exists():
    assert callable(XPath_LiteralExp.__init__)


def test_xpath_literalexp_constructor_args():
    sig = inspect.signature(XPath_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath_functioncallexp_is_not_abstract():
    assert not inspect.isabstract(XPath_FunctionCallExp)


def test_xpath_functioncallexp_constructor_exists():
    assert callable(XPath_FunctionCallExp.__init__)


def test_xpath_functioncallexp_constructor_args():
    sig = inspect.signature(XPath_FunctionCallExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath_variableexp_is_not_abstract():
    assert not inspect.isabstract(XPath_VariableExp)


def test_xpath_variableexp_constructor_exists():
    assert callable(XPath_VariableExp.__init__)


def test_xpath_variableexp_constructor_args():
    sig = inspect.signature(XPath_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_xpath_step_is_not_abstract():
    assert not inspect.isabstract(XPath_Step)


def test_xpath_step_constructor_exists():
    assert callable(XPath_Step.__init__)


def test_xpath_step_constructor_args():
    sig = inspect.signature(XPath_Step.__init__)
    params = list(sig.parameters.keys())



def test_xpath_expression_is_not_abstract():
    assert not inspect.isabstract(XPath_Expression)


def test_xpath_expression_constructor_exists():
    assert callable(XPath_Expression.__init__)


def test_xpath_expression_constructor_args():
    sig = inspect.signature(XPath_Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath_nodetest_is_not_abstract():
    assert not inspect.isabstract(XPath_NodeTest)


def test_xpath_nodetest_constructor_exists():
    assert callable(XPath_NodeTest.__init__)


def test_xpath_nodetest_constructor_args():
    sig = inspect.signature(XPath_NodeTest.__init__)
    params = list(sig.parameters.keys())



def test_xpath_predicate_is_not_abstract():
    assert not inspect.isabstract(XPath_Predicate)


def test_xpath_predicate_constructor_exists():
    assert callable(XPath_Predicate.__init__)


def test_xpath_predicate_constructor_args():
    sig = inspect.signature(XPath_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_xpath_axis_is_not_abstract():
    assert not inspect.isabstract(XPath_Axis)


def test_xpath_axis_constructor_exists():
    assert callable(XPath_Axis.__init__)


def test_xpath_axis_constructor_args():
    sig = inspect.signature(XPath_Axis.__init__)
    params = list(sig.parameters.keys())



def test_xpath_namedelement_is_not_abstract():
    assert not inspect.isabstract(XPath_NamedElement)


def test_xpath_namedelement_constructor_exists():
    assert callable(XPath_NamedElement.__init__)


def test_xpath_namedelement_constructor_args():
    sig = inspect.signature(XPath_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xpath_namedelement_has_name():
    assert hasattr(XPath_NamedElement, "name")
    descriptor = None
    for klass in XPath_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpath_locatedelement_is_not_abstract():
    assert not inspect.isabstract(XPath_LocatedElement)


def test_xpath_locatedelement_constructor_exists():
    assert callable(XPath_LocatedElement.__init__)


def test_xpath_locatedelement_constructor_args():
    sig = inspect.signature(XPath_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_xpath_locatedelement_has_location():
    assert hasattr(XPath_LocatedElement, "location")
    descriptor = None
    for klass in XPath_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_xpath_locatedelement_has_commentsBefore():
    assert hasattr(XPath_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in XPath_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_xpath_locatedelement_has_commentsAfter():
    assert hasattr(XPath_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in XPath_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
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
XPath_PrecedingAxis_strategy = st.builds(
    XPath_PrecedingAxis,
)
XPath_DescendantAxis_strategy = st.builds(
    XPath_DescendantAxis,
)
XPath_AttributeAxis_strategy = st.builds(
    XPath_AttributeAxis,
)
XPath_FollowingAxis_strategy = st.builds(
    XPath_FollowingAxis,
)
XPath_AncestorOrSelfAxis_strategy = st.builds(
    XPath_AncestorOrSelfAxis,
)
XPath_ChildAxis_strategy = st.builds(
    XPath_ChildAxis,
)
XPath_ParentAxis_strategy = st.builds(
    XPath_ParentAxis,
)
XPath_NamespaceAxis_strategy = st.builds(
    XPath_NamespaceAxis,
)
XPath_FollowingSiblingAxis_strategy = st.builds(
    XPath_FollowingSiblingAxis,
)
XPath_DescendantOrSelfAxis_strategy = st.builds(
    XPath_DescendantOrSelfAxis,
)
XPath_PrecedingSiblingAxis_strategy = st.builds(
    XPath_PrecedingSiblingAxis,
)
XPath_SelfAxis_strategy = st.builds(
    XPath_SelfAxis,
)
XPath_AncestorAxis_strategy = st.builds(
    XPath_AncestorAxis,
)
NodeTest_strategy = st.builds(
    NodeTest,
)
XPath_IsNodeTest_strategy = st.builds(
    XPath_IsNodeTest,
)
XPath_IsTextTest_strategy = st.builds(
    XPath_IsTextTest,
)
XPath_WildCardTest_strategy = st.builds(
    XPath_WildCardTest,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
XPath_StringExp_strategy = st.builds(
    XPath_StringExp,
    symbol=
        safe_text
)
XPath_IntegerExp_strategy = st.builds(
    XPath_IntegerExp,
    symbol=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
XPath_NameTest_strategy = st.builds(
    XPath_NameTest,
)
Expression_strategy = st.builds(
    Expression,
)
XPath_OperatorCallExp_strategy = st.builds(
    XPath_OperatorCallExp,
)
XPath_PathExpression_strategy = st.builds(
    XPath_PathExpression,
    isAbsolute=
        safe_text
)
XPath_LiteralExp_strategy = st.builds(
    XPath_LiteralExp,
)
XPath_FunctionCallExp_strategy = st.builds(
    XPath_FunctionCallExp,
)
XPath_VariableExp_strategy = st.builds(
    XPath_VariableExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
XPath_Step_strategy = st.builds(
    XPath_Step,
)
XPath_Expression_strategy = st.builds(
    XPath_Expression,
)
XPath_NodeTest_strategy = st.builds(
    XPath_NodeTest,
)
XPath_Predicate_strategy = st.builds(
    XPath_Predicate,
)
XPath_Axis_strategy = st.builds(
    XPath_Axis,
)
XPath_NamedElement_strategy = st.builds(
    XPath_NamedElement,
    name=
        safe_text
)
XPath_LocatedElement_strategy = st.builds(
    XPath_LocatedElement,
    location=
        safe_text,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text
)

@given(instance=Axis_strategy)
@settings(max_examples=50)
def test_axis_instantiation(instance):
    assert isinstance(instance, Axis)

@given(instance=XPath_PrecedingAxis_strategy)
@settings(max_examples=50)
def test_xpath_precedingaxis_instantiation(instance):
    assert isinstance(instance, XPath_PrecedingAxis)

@given(instance=XPath_DescendantAxis_strategy)
@settings(max_examples=50)
def test_xpath_descendantaxis_instantiation(instance):
    assert isinstance(instance, XPath_DescendantAxis)

@given(instance=XPath_AttributeAxis_strategy)
@settings(max_examples=50)
def test_xpath_attributeaxis_instantiation(instance):
    assert isinstance(instance, XPath_AttributeAxis)

@given(instance=XPath_FollowingAxis_strategy)
@settings(max_examples=50)
def test_xpath_followingaxis_instantiation(instance):
    assert isinstance(instance, XPath_FollowingAxis)

@given(instance=XPath_AncestorOrSelfAxis_strategy)
@settings(max_examples=50)
def test_xpath_ancestororselfaxis_instantiation(instance):
    assert isinstance(instance, XPath_AncestorOrSelfAxis)

@given(instance=XPath_ChildAxis_strategy)
@settings(max_examples=50)
def test_xpath_childaxis_instantiation(instance):
    assert isinstance(instance, XPath_ChildAxis)

@given(instance=XPath_ParentAxis_strategy)
@settings(max_examples=50)
def test_xpath_parentaxis_instantiation(instance):
    assert isinstance(instance, XPath_ParentAxis)

@given(instance=XPath_NamespaceAxis_strategy)
@settings(max_examples=50)
def test_xpath_namespaceaxis_instantiation(instance):
    assert isinstance(instance, XPath_NamespaceAxis)

@given(instance=XPath_FollowingSiblingAxis_strategy)
@settings(max_examples=50)
def test_xpath_followingsiblingaxis_instantiation(instance):
    assert isinstance(instance, XPath_FollowingSiblingAxis)

@given(instance=XPath_DescendantOrSelfAxis_strategy)
@settings(max_examples=50)
def test_xpath_descendantorselfaxis_instantiation(instance):
    assert isinstance(instance, XPath_DescendantOrSelfAxis)

@given(instance=XPath_PrecedingSiblingAxis_strategy)
@settings(max_examples=50)
def test_xpath_precedingsiblingaxis_instantiation(instance):
    assert isinstance(instance, XPath_PrecedingSiblingAxis)

@given(instance=XPath_SelfAxis_strategy)
@settings(max_examples=50)
def test_xpath_selfaxis_instantiation(instance):
    assert isinstance(instance, XPath_SelfAxis)

@given(instance=XPath_AncestorAxis_strategy)
@settings(max_examples=50)
def test_xpath_ancestoraxis_instantiation(instance):
    assert isinstance(instance, XPath_AncestorAxis)

@given(instance=NodeTest_strategy)
@settings(max_examples=50)
def test_nodetest_instantiation(instance):
    assert isinstance(instance, NodeTest)

@given(instance=XPath_IsNodeTest_strategy)
@settings(max_examples=50)
def test_xpath_isnodetest_instantiation(instance):
    assert isinstance(instance, XPath_IsNodeTest)

@given(instance=XPath_IsTextTest_strategy)
@settings(max_examples=50)
def test_xpath_istexttest_instantiation(instance):
    assert isinstance(instance, XPath_IsTextTest)

@given(instance=XPath_WildCardTest_strategy)
@settings(max_examples=50)
def test_xpath_wildcardtest_instantiation(instance):
    assert isinstance(instance, XPath_WildCardTest)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=XPath_StringExp_strategy)
@settings(max_examples=50)
def test_xpath_stringexp_instantiation(instance):
    assert isinstance(instance, XPath_StringExp)



@given(instance=XPath_StringExp_strategy)
def test_xpath_stringexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=XPath_IntegerExp_strategy)
@settings(max_examples=50)
def test_xpath_integerexp_instantiation(instance):
    assert isinstance(instance, XPath_IntegerExp)



@given(instance=XPath_IntegerExp_strategy)
def test_xpath_integerexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=XPath_NameTest_strategy)
@settings(max_examples=50)
def test_xpath_nametest_instantiation(instance):
    assert isinstance(instance, XPath_NameTest)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=XPath_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_xpath_operatorcallexp_instantiation(instance):
    assert isinstance(instance, XPath_OperatorCallExp)

@given(instance=XPath_PathExpression_strategy)
@settings(max_examples=50)
def test_xpath_pathexpression_instantiation(instance):
    assert isinstance(instance, XPath_PathExpression)



@given(instance=XPath_PathExpression_strategy)
def test_xpath_pathexpression_isAbsolute_setter(instance):
    original = instance.isAbsolute
    instance.isAbsolute = original
    assert instance.isAbsolute == original

@given(instance=XPath_LiteralExp_strategy)
@settings(max_examples=50)
def test_xpath_literalexp_instantiation(instance):
    assert isinstance(instance, XPath_LiteralExp)

@given(instance=XPath_FunctionCallExp_strategy)
@settings(max_examples=50)
def test_xpath_functioncallexp_instantiation(instance):
    assert isinstance(instance, XPath_FunctionCallExp)

@given(instance=XPath_VariableExp_strategy)
@settings(max_examples=50)
def test_xpath_variableexp_instantiation(instance):
    assert isinstance(instance, XPath_VariableExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=XPath_Step_strategy)
@settings(max_examples=50)
def test_xpath_step_instantiation(instance):
    assert isinstance(instance, XPath_Step)

@given(instance=XPath_Expression_strategy)
@settings(max_examples=50)
def test_xpath_expression_instantiation(instance):
    assert isinstance(instance, XPath_Expression)

@given(instance=XPath_NodeTest_strategy)
@settings(max_examples=50)
def test_xpath_nodetest_instantiation(instance):
    assert isinstance(instance, XPath_NodeTest)

@given(instance=XPath_Predicate_strategy)
@settings(max_examples=50)
def test_xpath_predicate_instantiation(instance):
    assert isinstance(instance, XPath_Predicate)

@given(instance=XPath_Axis_strategy)
@settings(max_examples=50)
def test_xpath_axis_instantiation(instance):
    assert isinstance(instance, XPath_Axis)

@given(instance=XPath_NamedElement_strategy)
@settings(max_examples=50)
def test_xpath_namedelement_instantiation(instance):
    assert isinstance(instance, XPath_NamedElement)



@given(instance=XPath_NamedElement_strategy)
def test_xpath_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=XPath_LocatedElement_strategy)
@settings(max_examples=50)
def test_xpath_locatedelement_instantiation(instance):
    assert isinstance(instance, XPath_LocatedElement)



@given(instance=XPath_LocatedElement_strategy)
def test_xpath_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=XPath_LocatedElement_strategy)
def test_xpath_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=XPath_LocatedElement_strategy)
def test_xpath_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original
