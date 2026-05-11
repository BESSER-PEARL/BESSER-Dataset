import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    JavaSimplified::TypedElement,
    JavaSimplified::StringElement,
    JavaSimplified::JavaModel,
    JavaSimplified::NamedElement,
    JavaSimplified::MethodCall,
    Feature,
    JavaSimplified::Method,
    TypedElement,
    JavaSimplified::Field,
    NamedElement,
    JavaSimplified::Parameter,
    CommentedElement,
    Statement,
    JavaSimplified::ReturnStatement,
    JavaSimplified::VariableDeclarationStatement,
    JavaSimplified::ExpressionStatement,
    JavaSimplified::CommentStatement,
    JavaSimplified::CommentedElement,
    JavaSimplified::JavaClass,
    JavaSimplified::IfStatement,
    Expression,
    JavaSimplified::Literal,
    JavaSimplified::MethodInvocation,
    JavaSimplified::InfixExpression,
    JavaSimplified::Name,
    JavaSimplified::ThisExpression,
    JavaSimplified::FieldAccess,
    JavaSimplified::Assignment,
    StringElement,
    JavaSimplified::Expression,
    JavaSimplified::Feature,
    JavaSimplified::Statement,
    JavaSimplified::Comment,
    JavaSimplified::ClassInstanceCreation,
    JavaSimplified::Type,
    JavaSimplified::CastExpression,
    AssignmentOperatorType,
    LiteralType,
    VisibilityType,
    InfixOperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javasimplified::typedelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::TypedElement)


def test_javasimplified::typedelement_constructor_exists():
    assert callable(JavaSimplified::TypedElement.__init__)


def test_javasimplified::typedelement_constructor_args():
    sig = inspect.signature(JavaSimplified::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::stringelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::StringElement)


def test_javasimplified::stringelement_constructor_exists():
    assert callable(JavaSimplified::StringElement.__init__)


def test_javasimplified::stringelement_constructor_args():
    sig = inspect.signature(JavaSimplified::StringElement.__init__)
    params = list(sig.parameters.keys())
    assert "strValue" in params, "Missing parameter 'strValue'"

def test_javasimplified::stringelement_has_strValue():
    assert hasattr(JavaSimplified::StringElement, "strValue")
    descriptor = None
    for klass in JavaSimplified::StringElement.__mro__:
        if "strValue" in klass.__dict__:
            descriptor = klass.__dict__["strValue"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::javamodel_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::JavaModel)


def test_javasimplified::javamodel_constructor_exists():
    assert callable(JavaSimplified::JavaModel.__init__)


def test_javasimplified::javamodel_constructor_args():
    sig = inspect.signature(JavaSimplified::JavaModel.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::namedelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::NamedElement)


def test_javasimplified::namedelement_constructor_exists():
    assert callable(JavaSimplified::NamedElement.__init__)


def test_javasimplified::namedelement_constructor_args():
    sig = inspect.signature(JavaSimplified::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::methodcall_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::MethodCall)


def test_javasimplified::methodcall_constructor_exists():
    assert callable(JavaSimplified::MethodCall.__init__)


def test_javasimplified::methodcall_constructor_args():
    sig = inspect.signature(JavaSimplified::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::method_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Method)


def test_javasimplified::method_constructor_exists():
    assert callable(JavaSimplified::Method.__init__)


def test_javasimplified::method_constructor_args():
    sig = inspect.signature(JavaSimplified::Method.__init__)
    params = list(sig.parameters.keys())
    assert "exceptions" in params, "Missing parameter 'exceptions'"

def test_javasimplified::method_has_exceptions():
    assert hasattr(JavaSimplified::Method, "exceptions")
    descriptor = None
    for klass in JavaSimplified::Method.__mro__:
        if "exceptions" in klass.__dict__:
            descriptor = klass.__dict__["exceptions"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::field_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Field)


def test_javasimplified::field_constructor_exists():
    assert callable(JavaSimplified::Field.__init__)


def test_javasimplified::field_constructor_args():
    sig = inspect.signature(JavaSimplified::Field.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::parameter_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Parameter)


def test_javasimplified::parameter_constructor_exists():
    assert callable(JavaSimplified::Parameter.__init__)


def test_javasimplified::parameter_constructor_args():
    sig = inspect.signature(JavaSimplified::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_commentedelement_is_not_abstract():
    assert not inspect.isabstract(CommentedElement)


def test_commentedelement_constructor_exists():
    assert callable(CommentedElement.__init__)


def test_commentedelement_constructor_args():
    sig = inspect.signature(CommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::returnstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::ReturnStatement)


def test_javasimplified::returnstatement_constructor_exists():
    assert callable(JavaSimplified::ReturnStatement.__init__)


def test_javasimplified::returnstatement_constructor_args():
    sig = inspect.signature(JavaSimplified::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::VariableDeclarationStatement)


def test_javasimplified::variabledeclarationstatement_constructor_exists():
    assert callable(JavaSimplified::VariableDeclarationStatement.__init__)


def test_javasimplified::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(JavaSimplified::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::ExpressionStatement)


def test_javasimplified::expressionstatement_constructor_exists():
    assert callable(JavaSimplified::ExpressionStatement.__init__)


def test_javasimplified::expressionstatement_constructor_args():
    sig = inspect.signature(JavaSimplified::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::commentstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::CommentStatement)


def test_javasimplified::commentstatement_constructor_exists():
    assert callable(JavaSimplified::CommentStatement.__init__)


def test_javasimplified::commentstatement_constructor_args():
    sig = inspect.signature(JavaSimplified::CommentStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::commentedelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::CommentedElement)


def test_javasimplified::commentedelement_constructor_exists():
    assert callable(JavaSimplified::CommentedElement.__init__)


def test_javasimplified::commentedelement_constructor_args():
    sig = inspect.signature(JavaSimplified::CommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::javaclass_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::JavaClass)


def test_javasimplified::javaclass_constructor_exists():
    assert callable(JavaSimplified::JavaClass.__init__)


def test_javasimplified::javaclass_constructor_args():
    sig = inspect.signature(JavaSimplified::JavaClass.__init__)
    params = list(sig.parameters.keys())
    assert "imports" in params, "Missing parameter 'imports'"

def test_javasimplified::javaclass_has_imports():
    assert hasattr(JavaSimplified::JavaClass, "imports")
    descriptor = None
    for klass in JavaSimplified::JavaClass.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::ifstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::IfStatement)


def test_javasimplified::ifstatement_constructor_exists():
    assert callable(JavaSimplified::IfStatement.__init__)


def test_javasimplified::ifstatement_constructor_args():
    sig = inspect.signature(JavaSimplified::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::literal_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Literal)


def test_javasimplified::literal_constructor_exists():
    assert callable(JavaSimplified::Literal.__init__)


def test_javasimplified::literal_constructor_args():
    sig = inspect.signature(JavaSimplified::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_javasimplified::literal_has_type():
    assert hasattr(JavaSimplified::Literal, "type")
    descriptor = None
    for klass in JavaSimplified::Literal.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_javasimplified::literal_has_value():
    assert hasattr(JavaSimplified::Literal, "value")
    descriptor = None
    for klass in JavaSimplified::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::MethodInvocation)


def test_javasimplified::methodinvocation_constructor_exists():
    assert callable(JavaSimplified::MethodInvocation.__init__)


def test_javasimplified::methodinvocation_constructor_args():
    sig = inspect.signature(JavaSimplified::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::infixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::InfixExpression)


def test_javasimplified::infixexpression_constructor_exists():
    assert callable(JavaSimplified::InfixExpression.__init__)


def test_javasimplified::infixexpression_constructor_args():
    sig = inspect.signature(JavaSimplified::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javasimplified::infixexpression_has_operator():
    assert hasattr(JavaSimplified::InfixExpression, "operator")
    descriptor = None
    for klass in JavaSimplified::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::name_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Name)


def test_javasimplified::name_constructor_exists():
    assert callable(JavaSimplified::Name.__init__)


def test_javasimplified::name_constructor_args():
    sig = inspect.signature(JavaSimplified::Name.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_javasimplified::name_has_identifier():
    assert hasattr(JavaSimplified::Name, "identifier")
    descriptor = None
    for klass in JavaSimplified::Name.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::thisexpression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::ThisExpression)


def test_javasimplified::thisexpression_constructor_exists():
    assert callable(JavaSimplified::ThisExpression.__init__)


def test_javasimplified::thisexpression_constructor_args():
    sig = inspect.signature(JavaSimplified::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::FieldAccess)


def test_javasimplified::fieldaccess_constructor_exists():
    assert callable(JavaSimplified::FieldAccess.__init__)


def test_javasimplified::fieldaccess_constructor_args():
    sig = inspect.signature(JavaSimplified::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::assignment_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Assignment)


def test_javasimplified::assignment_constructor_exists():
    assert callable(JavaSimplified::Assignment.__init__)


def test_javasimplified::assignment_constructor_args():
    sig = inspect.signature(JavaSimplified::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javasimplified::assignment_has_operator():
    assert hasattr(JavaSimplified::Assignment, "operator")
    descriptor = None
    for klass in JavaSimplified::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stringelement_is_not_abstract():
    assert not inspect.isabstract(StringElement)


def test_stringelement_constructor_exists():
    assert callable(StringElement.__init__)


def test_stringelement_constructor_args():
    sig = inspect.signature(StringElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::expression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Expression)


def test_javasimplified::expression_constructor_exists():
    assert callable(JavaSimplified::Expression.__init__)


def test_javasimplified::expression_constructor_args():
    sig = inspect.signature(JavaSimplified::Expression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::feature_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Feature)


def test_javasimplified::feature_constructor_exists():
    assert callable(JavaSimplified::Feature.__init__)


def test_javasimplified::feature_constructor_args():
    sig = inspect.signature(JavaSimplified::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javasimplified::feature_has_visibility():
    assert hasattr(JavaSimplified::Feature, "visibility")
    descriptor = None
    for klass in JavaSimplified::Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::statement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Statement)


def test_javasimplified::statement_constructor_exists():
    assert callable(JavaSimplified::Statement.__init__)


def test_javasimplified::statement_constructor_args():
    sig = inspect.signature(JavaSimplified::Statement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::comment_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Comment)


def test_javasimplified::comment_constructor_exists():
    assert callable(JavaSimplified::Comment.__init__)


def test_javasimplified::comment_constructor_args():
    sig = inspect.signature(JavaSimplified::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "isJavadoc" in params, "Missing parameter 'isJavadoc'"

def test_javasimplified::comment_has_isJavadoc():
    assert hasattr(JavaSimplified::Comment, "isJavadoc")
    descriptor = None
    for klass in JavaSimplified::Comment.__mro__:
        if "isJavadoc" in klass.__dict__:
            descriptor = klass.__dict__["isJavadoc"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::ClassInstanceCreation)


def test_javasimplified::classinstancecreation_constructor_exists():
    assert callable(JavaSimplified::ClassInstanceCreation.__init__)


def test_javasimplified::classinstancecreation_constructor_args():
    sig = inspect.signature(JavaSimplified::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::type_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::Type)


def test_javasimplified::type_constructor_exists():
    assert callable(JavaSimplified::Type.__init__)


def test_javasimplified::type_constructor_args():
    sig = inspect.signature(JavaSimplified::Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javasimplified::type_has_type():
    assert hasattr(JavaSimplified::Type, "type")
    descriptor = None
    for klass in JavaSimplified::Type.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::castexpression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified::CastExpression)


def test_javasimplified::castexpression_constructor_exists():
    assert callable(JavaSimplified::CastExpression.__init__)


def test_javasimplified::castexpression_constructor_args():
    sig = inspect.signature(JavaSimplified::CastExpression.__init__)
    params = list(sig.parameters.keys())

def test_assignmentoperatortype_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorType is not None

def test_assignmentoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorType]
    expected_literals = [
        "ASSIGN",
        "PLUS_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorType"

def test_literaltype_exists():
    # Check that the Enumeration exists
    assert LiteralType is not None

def test_literaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralType]
    expected_literals = [
        "NULL",
        "BOOLEAN",
        "INTEGER",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralType"

def test_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "PROTECTED",
        "PRIVATE",
        "PUBLIC",
        "PACKAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"

def test_infixoperatortype_exists():
    # Check that the Enumeration exists
    assert InfixOperatorType is not None

def test_infixoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixOperatorType]
    expected_literals = [
        "CONDITIONAL_OR",
        "EQUALS",
        "CONDITIONAL_AND",
        "NOT_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixOperatorType"


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
JavaSimplified::TypedElement_strategy = st.builds(
    JavaSimplified::TypedElement,
)
JavaSimplified::StringElement_strategy = st.builds(
    JavaSimplified::StringElement,
    strValue=
        safe_text
)
JavaSimplified::JavaModel_strategy = st.builds(
    JavaSimplified::JavaModel,
)
JavaSimplified::NamedElement_strategy = st.builds(
    JavaSimplified::NamedElement,
)
JavaSimplified::MethodCall_strategy = st.builds(
    JavaSimplified::MethodCall,
)
Feature_strategy = st.builds(
    Feature,
)
JavaSimplified::Method_strategy = st.builds(
    JavaSimplified::Method,
    exceptions=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
JavaSimplified::Field_strategy = st.builds(
    JavaSimplified::Field,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JavaSimplified::Parameter_strategy = st.builds(
    JavaSimplified::Parameter,
)
CommentedElement_strategy = st.builds(
    CommentedElement,
)
Statement_strategy = st.builds(
    Statement,
)
JavaSimplified::ReturnStatement_strategy = st.builds(
    JavaSimplified::ReturnStatement,
)
JavaSimplified::VariableDeclarationStatement_strategy = st.builds(
    JavaSimplified::VariableDeclarationStatement,
)
JavaSimplified::ExpressionStatement_strategy = st.builds(
    JavaSimplified::ExpressionStatement,
)
JavaSimplified::CommentStatement_strategy = st.builds(
    JavaSimplified::CommentStatement,
)
JavaSimplified::CommentedElement_strategy = st.builds(
    JavaSimplified::CommentedElement,
)
JavaSimplified::JavaClass_strategy = st.builds(
    JavaSimplified::JavaClass,
    imports=
        safe_text
)
JavaSimplified::IfStatement_strategy = st.builds(
    JavaSimplified::IfStatement,
)
Expression_strategy = st.builds(
    Expression,
)
JavaSimplified::Literal_strategy = st.builds(
    JavaSimplified::Literal,
    type=
        safe_text,
    value=
        safe_text
)
JavaSimplified::MethodInvocation_strategy = st.builds(
    JavaSimplified::MethodInvocation,
)
JavaSimplified::InfixExpression_strategy = st.builds(
    JavaSimplified::InfixExpression,
    operator=
        safe_text
)
JavaSimplified::Name_strategy = st.builds(
    JavaSimplified::Name,
    identifier=
        safe_text
)
JavaSimplified::ThisExpression_strategy = st.builds(
    JavaSimplified::ThisExpression,
)
JavaSimplified::FieldAccess_strategy = st.builds(
    JavaSimplified::FieldAccess,
)
JavaSimplified::Assignment_strategy = st.builds(
    JavaSimplified::Assignment,
    operator=
        safe_text
)
StringElement_strategy = st.builds(
    StringElement,
)
JavaSimplified::Expression_strategy = st.builds(
    JavaSimplified::Expression,
)
JavaSimplified::Feature_strategy = st.builds(
    JavaSimplified::Feature,
    visibility=
        safe_text
)
JavaSimplified::Statement_strategy = st.builds(
    JavaSimplified::Statement,
)
JavaSimplified::Comment_strategy = st.builds(
    JavaSimplified::Comment,
    isJavadoc=
        st.booleans()
)
JavaSimplified::ClassInstanceCreation_strategy = st.builds(
    JavaSimplified::ClassInstanceCreation,
)
JavaSimplified::Type_strategy = st.builds(
    JavaSimplified::Type,
    type=
        safe_text
)
JavaSimplified::CastExpression_strategy = st.builds(
    JavaSimplified::CastExpression,
)

@given(instance=JavaSimplified::TypedElement_strategy)
@settings(max_examples=50)
def test_javasimplified::typedelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::TypedElement)

@given(instance=JavaSimplified::StringElement_strategy)
@settings(max_examples=50)
def test_javasimplified::stringelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::StringElement)

@given(instance=JavaSimplified::StringElement_strategy)
def test_javasimplified::stringelement_strValue_type(instance):
    assert isinstance(instance.strValue, str)


@given(instance=JavaSimplified::StringElement_strategy)
def test_javasimplified::stringelement_strValue_setter(instance):
    original = instance.strValue
    instance.strValue = original
    assert instance.strValue == original

@given(instance=JavaSimplified::JavaModel_strategy)
@settings(max_examples=50)
def test_javasimplified::javamodel_instantiation(instance):
    assert isinstance(instance, JavaSimplified::JavaModel)

@given(instance=JavaSimplified::NamedElement_strategy)
@settings(max_examples=50)
def test_javasimplified::namedelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::NamedElement)

@given(instance=JavaSimplified::MethodCall_strategy)
@settings(max_examples=50)
def test_javasimplified::methodcall_instantiation(instance):
    assert isinstance(instance, JavaSimplified::MethodCall)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=JavaSimplified::Method_strategy)
@settings(max_examples=50)
def test_javasimplified::method_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Method)

@given(instance=JavaSimplified::Method_strategy)
def test_javasimplified::method_exceptions_type(instance):
    assert isinstance(instance.exceptions, str)


@given(instance=JavaSimplified::Method_strategy)
def test_javasimplified::method_exceptions_setter(instance):
    original = instance.exceptions
    instance.exceptions = original
    assert instance.exceptions == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=JavaSimplified::Field_strategy)
@settings(max_examples=50)
def test_javasimplified::field_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Field)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JavaSimplified::Parameter_strategy)
@settings(max_examples=50)
def test_javasimplified::parameter_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Parameter)

@given(instance=CommentedElement_strategy)
@settings(max_examples=50)
def test_commentedelement_instantiation(instance):
    assert isinstance(instance, CommentedElement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=JavaSimplified::ReturnStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::returnstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::ReturnStatement)

@given(instance=JavaSimplified::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::VariableDeclarationStatement)

@given(instance=JavaSimplified::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::expressionstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::ExpressionStatement)

@given(instance=JavaSimplified::CommentStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::commentstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::CommentStatement)

@given(instance=JavaSimplified::CommentedElement_strategy)
@settings(max_examples=50)
def test_javasimplified::commentedelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::CommentedElement)

@given(instance=JavaSimplified::JavaClass_strategy)
@settings(max_examples=50)
def test_javasimplified::javaclass_instantiation(instance):
    assert isinstance(instance, JavaSimplified::JavaClass)

@given(instance=JavaSimplified::JavaClass_strategy)
def test_javasimplified::javaclass_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=JavaSimplified::JavaClass_strategy)
def test_javasimplified::javaclass_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=JavaSimplified::IfStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::ifstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::IfStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JavaSimplified::Literal_strategy)
@settings(max_examples=50)
def test_javasimplified::literal_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Literal)

@given(instance=JavaSimplified::Literal_strategy)
def test_javasimplified::literal_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JavaSimplified::Literal_strategy)
def test_javasimplified::literal_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JavaSimplified::Literal_strategy)
def test_javasimplified::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=JavaSimplified::Literal_strategy)
def test_javasimplified::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=JavaSimplified::MethodInvocation_strategy)
@settings(max_examples=50)
def test_javasimplified::methodinvocation_instantiation(instance):
    assert isinstance(instance, JavaSimplified::MethodInvocation)

@given(instance=JavaSimplified::InfixExpression_strategy)
@settings(max_examples=50)
def test_javasimplified::infixexpression_instantiation(instance):
    assert isinstance(instance, JavaSimplified::InfixExpression)

@given(instance=JavaSimplified::InfixExpression_strategy)
def test_javasimplified::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JavaSimplified::InfixExpression_strategy)
def test_javasimplified::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaSimplified::Name_strategy)
@settings(max_examples=50)
def test_javasimplified::name_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Name)

@given(instance=JavaSimplified::Name_strategy)
def test_javasimplified::name_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=JavaSimplified::Name_strategy)
def test_javasimplified::name_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=JavaSimplified::ThisExpression_strategy)
@settings(max_examples=50)
def test_javasimplified::thisexpression_instantiation(instance):
    assert isinstance(instance, JavaSimplified::ThisExpression)

@given(instance=JavaSimplified::FieldAccess_strategy)
@settings(max_examples=50)
def test_javasimplified::fieldaccess_instantiation(instance):
    assert isinstance(instance, JavaSimplified::FieldAccess)

@given(instance=JavaSimplified::Assignment_strategy)
@settings(max_examples=50)
def test_javasimplified::assignment_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Assignment)

@given(instance=JavaSimplified::Assignment_strategy)
def test_javasimplified::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JavaSimplified::Assignment_strategy)
def test_javasimplified::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=StringElement_strategy)
@settings(max_examples=50)
def test_stringelement_instantiation(instance):
    assert isinstance(instance, StringElement)

@given(instance=JavaSimplified::Expression_strategy)
@settings(max_examples=50)
def test_javasimplified::expression_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Expression)

@given(instance=JavaSimplified::Feature_strategy)
@settings(max_examples=50)
def test_javasimplified::feature_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Feature)

@given(instance=JavaSimplified::Feature_strategy)
def test_javasimplified::feature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=JavaSimplified::Feature_strategy)
def test_javasimplified::feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=JavaSimplified::Statement_strategy)
@settings(max_examples=50)
def test_javasimplified::statement_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Statement)

@given(instance=JavaSimplified::Comment_strategy)
@settings(max_examples=50)
def test_javasimplified::comment_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Comment)

@given(instance=JavaSimplified::Comment_strategy)
def test_javasimplified::comment_isJavadoc_type(instance):
    assert isinstance(instance.isJavadoc, bool)


@given(instance=JavaSimplified::Comment_strategy)
def test_javasimplified::comment_isJavadoc_setter(instance):
    original = instance.isJavadoc
    instance.isJavadoc = original
    assert instance.isJavadoc == original

@given(instance=JavaSimplified::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_javasimplified::classinstancecreation_instantiation(instance):
    assert isinstance(instance, JavaSimplified::ClassInstanceCreation)

@given(instance=JavaSimplified::Type_strategy)
@settings(max_examples=50)
def test_javasimplified::type_instantiation(instance):
    assert isinstance(instance, JavaSimplified::Type)

@given(instance=JavaSimplified::Type_strategy)
def test_javasimplified::type_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JavaSimplified::Type_strategy)
def test_javasimplified::type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JavaSimplified::CastExpression_strategy)
@settings(max_examples=50)
def test_javasimplified::castexpression_instantiation(instance):
    assert isinstance(instance, JavaSimplified::CastExpression)
