import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    javaDsl::ArrayCreationExpression,
    Primary,
    javaDsl::PrimaryNewArray,
    javaDsl::PrimaryNoNewArray,
    javaDsl::ArrayExpression,
    LeftHandSide,
    javaDsl::ArrayAccess,
    javaDsl::FieldAccess,
    javaDsl::Primary,
    NoArrayExpression,
    javaDsl::NoArrayExpressionWithoutMinus,
    NoArrayExpressionWithoutMinus,
    javaDsl::CastExpression,
    javaDsl::NoArrayExpression,
    javaDsl::MultiplicativeExpression,
    javaDsl::AdditiveExpression,
    javaDsl::ShiftExpression,
    javaDsl::RelationalExpression,
    javaDsl::EqualityExpression,
    javaDsl::AndExpression,
    javaDsl::ExclusiveOrExpression,
    javaDsl::ConditionalAndExpression,
    javaDsl::ConditionalOrExpression,
    javaDsl::LeftHandSide,
    AssignmentExpression,
    javaDsl::ConditionalExpression,
    StatementExpression,
    javaDsl::ClassInstanceCreationExpression,
    javaDsl::MethodInvocation,
    javaDsl::PreDecrementExpression,
    javaDsl::PreIncrementExpression,
    javaDsl::PostfixExpression,
    javaDsl::Assignment,
    Expression,
    javaDsl::AssignmentExpression,
    PrimaryNoNewArray,
    ConstantExpression,
    javaDsl::InclusiveOrExpression,
    javaDsl::ForUpdate,
    javaDsl::ForInit,
    javaDsl::ConstantExpression,
    BlockStatement,
    javaDsl::Statement,
    javaDsl::LocalVariableDeclaration,
    Statement,
    javaDsl::LabeledStatement,
    javaDsl::DoStatement,
    javaDsl::ForStatement,
    javaDsl::BreakStatement,
    javaDsl::IfStatement,
    javaDsl::ReturnStatement,
    javaDsl::TryStatement,
    javaDsl::SwitchStatement,
    javaDsl::SynchronizedStatement,
    javaDsl::ContinueStatement,
    javaDsl::StatementExpression,
    javaDsl::ThrowsStatement,
    javaDsl::WhileStatement,
    VariableInitializer,
    javaDsl::ArrayInitializer,
    InterfaceMemberDeclaration,
    javaDsl::AbstractMethodDeclaration,
    javaDsl::ConstantDeclaration,
    javaDsl::InterfaceMemberDeclaration,
    javaDsl::InterfaceBody,
    javaDsl::ExtendsInterfaces,
    javaDsl::InterfaceDeclaration,
    javaDsl::MethodDeclarator,
    javaDsl::ResultType,
    javaDsl::MethodHeader,
    javaDsl::VariableDeclarator,
    javaDsl::ArgumentList,
    javaDsl::BlockStatement,
    javaDsl::ExplicitConstructorInvocation,
    javaDsl::Type,
    javaDsl::FormalParameter,
    javaDsl::ConstructorBody,
    javaDsl::Exceptions,
    javaDsl::ConstructorDeclarator,
    javaDsl::Block,
    ClassBodyDeclaration,
    javaDsl::ConstructorDeclaration,
    javaDsl::StaticInitializer,
    javaDsl::MethodDeclaration,
    javaDsl::FieldDeclaration,
    javaDsl::ClassMemberDeclaration,
    javaDsl::Expression,
    javaDsl::VariableInitializer,
    javaDsl::ClassBody,
    javaDsl::Interfaces,
    javaDsl::ClassDeclaration,
    javaDsl::EObject,
    javaDsl::TypeDeclaration,
    javaDsl::ImportStatement,
    javaDsl::PackageStatement,
    javaDsl::CompilationUnit,
    javaDsl::Head,
    javaDsl::ClassBodyDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javadsl::arraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ArrayCreationExpression)


def test_javadsl::arraycreationexpression_constructor_exists():
    assert callable(javaDsl::ArrayCreationExpression.__init__)


def test_javadsl::arraycreationexpression_constructor_args():
    sig = inspect.signature(javaDsl::ArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "layers" in params, "Missing parameter 'layers'"

def test_javadsl::arraycreationexpression_has_type():
    assert hasattr(javaDsl::ArrayCreationExpression, "type")
    descriptor = None
    for klass in javaDsl::ArrayCreationExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::arraycreationexpression_has_layers():
    assert hasattr(javaDsl::ArrayCreationExpression, "layers")
    descriptor = None
    for klass in javaDsl::ArrayCreationExpression.__mro__:
        if "layers" in klass.__dict__:
            descriptor = klass.__dict__["layers"]
            break
    assert isinstance(descriptor, property)



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::primarynewarray_is_not_abstract():
    assert not inspect.isabstract(javaDsl::PrimaryNewArray)


def test_javadsl::primarynewarray_constructor_exists():
    assert callable(javaDsl::PrimaryNewArray.__init__)


def test_javadsl::primarynewarray_constructor_args():
    sig = inspect.signature(javaDsl::PrimaryNewArray.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::primarynonewarray_is_not_abstract():
    assert not inspect.isabstract(javaDsl::PrimaryNoNewArray)


def test_javadsl::primarynonewarray_constructor_exists():
    assert callable(javaDsl::PrimaryNoNewArray.__init__)


def test_javadsl::primarynonewarray_constructor_args():
    sig = inspect.signature(javaDsl::PrimaryNoNewArray.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "method" in params, "Missing parameter 'method'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl::primarynonewarray_has_literal():
    assert hasattr(javaDsl::PrimaryNoNewArray, "literal")
    descriptor = None
    for klass in javaDsl::PrimaryNoNewArray.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::primarynonewarray_has_method():
    assert hasattr(javaDsl::PrimaryNoNewArray, "method")
    descriptor = None
    for klass in javaDsl::PrimaryNoNewArray.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::primarynonewarray_has_reference():
    assert hasattr(javaDsl::PrimaryNoNewArray, "reference")
    descriptor = None
    for klass in javaDsl::PrimaryNoNewArray.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::primarynonewarray_has_keyword():
    assert hasattr(javaDsl::PrimaryNoNewArray, "keyword")
    descriptor = None
    for klass in javaDsl::PrimaryNoNewArray.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::arrayexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ArrayExpression)


def test_javadsl::arrayexpression_constructor_exists():
    assert callable(javaDsl::ArrayExpression.__init__)


def test_javadsl::arrayexpression_constructor_args():
    sig = inspect.signature(javaDsl::ArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_lefthandside_is_not_abstract():
    assert not inspect.isabstract(LeftHandSide)


def test_lefthandside_constructor_exists():
    assert callable(LeftHandSide.__init__)


def test_lefthandside_constructor_args():
    sig = inspect.signature(LeftHandSide.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ArrayAccess)


def test_javadsl::arrayaccess_constructor_exists():
    assert callable(javaDsl::ArrayAccess.__init__)


def test_javadsl::arrayaccess_constructor_args():
    sig = inspect.signature(javaDsl::ArrayAccess.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl::arrayaccess_has_reference():
    assert hasattr(javaDsl::ArrayAccess, "reference")
    descriptor = None
    for klass in javaDsl::ArrayAccess.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(javaDsl::FieldAccess)


def test_javadsl::fieldaccess_constructor_exists():
    assert callable(javaDsl::FieldAccess.__init__)


def test_javadsl::fieldaccess_constructor_args():
    sig = inspect.signature(javaDsl::FieldAccess.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl::fieldaccess_has_field():
    assert hasattr(javaDsl::FieldAccess, "field")
    descriptor = None
    for klass in javaDsl::FieldAccess.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::fieldaccess_has_keyword():
    assert hasattr(javaDsl::FieldAccess, "keyword")
    descriptor = None
    for klass in javaDsl::FieldAccess.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::primary_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Primary)


def test_javadsl::primary_constructor_exists():
    assert callable(javaDsl::Primary.__init__)


def test_javadsl::primary_constructor_args():
    sig = inspect.signature(javaDsl::Primary.__init__)
    params = list(sig.parameters.keys())
    assert "fields" in params, "Missing parameter 'fields'"

def test_javadsl::primary_has_fields():
    assert hasattr(javaDsl::Primary, "fields")
    descriptor = None
    for klass in javaDsl::Primary.__mro__:
        if "fields" in klass.__dict__:
            descriptor = klass.__dict__["fields"]
            break
    assert isinstance(descriptor, property)



def test_noarrayexpression_is_not_abstract():
    assert not inspect.isabstract(NoArrayExpression)


def test_noarrayexpression_constructor_exists():
    assert callable(NoArrayExpression.__init__)


def test_noarrayexpression_constructor_args():
    sig = inspect.signature(NoArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::noarrayexpressionwithoutminus_is_not_abstract():
    assert not inspect.isabstract(javaDsl::NoArrayExpressionWithoutMinus)


def test_javadsl::noarrayexpressionwithoutminus_constructor_exists():
    assert callable(javaDsl::NoArrayExpressionWithoutMinus.__init__)


def test_javadsl::noarrayexpressionwithoutminus_constructor_args():
    sig = inspect.signature(javaDsl::NoArrayExpressionWithoutMinus.__init__)
    params = list(sig.parameters.keys())



def test_noarrayexpressionwithoutminus_is_not_abstract():
    assert not inspect.isabstract(NoArrayExpressionWithoutMinus)


def test_noarrayexpressionwithoutminus_constructor_exists():
    assert callable(NoArrayExpressionWithoutMinus.__init__)


def test_noarrayexpressionwithoutminus_constructor_args():
    sig = inspect.signature(NoArrayExpressionWithoutMinus.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::castexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::CastExpression)


def test_javadsl::castexpression_constructor_exists():
    assert callable(javaDsl::CastExpression.__init__)


def test_javadsl::castexpression_constructor_args():
    sig = inspect.signature(javaDsl::CastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javadsl::castexpression_has_type():
    assert hasattr(javaDsl::CastExpression, "type")
    descriptor = None
    for klass in javaDsl::CastExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::noarrayexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::NoArrayExpression)


def test_javadsl::noarrayexpression_constructor_exists():
    assert callable(javaDsl::NoArrayExpression.__init__)


def test_javadsl::noarrayexpression_constructor_args():
    sig = inspect.signature(javaDsl::NoArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javadsl::noarrayexpression_has_operator():
    assert hasattr(javaDsl::NoArrayExpression, "operator")
    descriptor = None
    for klass in javaDsl::NoArrayExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::MultiplicativeExpression)


def test_javadsl::multiplicativeexpression_constructor_exists():
    assert callable(javaDsl::MultiplicativeExpression.__init__)


def test_javadsl::multiplicativeexpression_constructor_args():
    sig = inspect.signature(javaDsl::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::multiplicativeexpression_has_operators():
    assert hasattr(javaDsl::MultiplicativeExpression, "operators")
    descriptor = None
    for klass in javaDsl::MultiplicativeExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::AdditiveExpression)


def test_javadsl::additiveexpression_constructor_exists():
    assert callable(javaDsl::AdditiveExpression.__init__)


def test_javadsl::additiveexpression_constructor_args():
    sig = inspect.signature(javaDsl::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::additiveexpression_has_operators():
    assert hasattr(javaDsl::AdditiveExpression, "operators")
    descriptor = None
    for klass in javaDsl::AdditiveExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ShiftExpression)


def test_javadsl::shiftexpression_constructor_exists():
    assert callable(javaDsl::ShiftExpression.__init__)


def test_javadsl::shiftexpression_constructor_args():
    sig = inspect.signature(javaDsl::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::shiftexpression_has_operators():
    assert hasattr(javaDsl::ShiftExpression, "operators")
    descriptor = None
    for klass in javaDsl::ShiftExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::RelationalExpression)


def test_javadsl::relationalexpression_constructor_exists():
    assert callable(javaDsl::RelationalExpression.__init__)


def test_javadsl::relationalexpression_constructor_args():
    sig = inspect.signature(javaDsl::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"
    assert "classes" in params, "Missing parameter 'classes'"

def test_javadsl::relationalexpression_has_operators():
    assert hasattr(javaDsl::RelationalExpression, "operators")
    descriptor = None
    for klass in javaDsl::RelationalExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::relationalexpression_has_classes():
    assert hasattr(javaDsl::RelationalExpression, "classes")
    descriptor = None
    for klass in javaDsl::RelationalExpression.__mro__:
        if "classes" in klass.__dict__:
            descriptor = klass.__dict__["classes"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::EqualityExpression)


def test_javadsl::equalityexpression_constructor_exists():
    assert callable(javaDsl::EqualityExpression.__init__)


def test_javadsl::equalityexpression_constructor_args():
    sig = inspect.signature(javaDsl::EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::equalityexpression_has_operators():
    assert hasattr(javaDsl::EqualityExpression, "operators")
    descriptor = None
    for klass in javaDsl::EqualityExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::andexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::AndExpression)


def test_javadsl::andexpression_constructor_exists():
    assert callable(javaDsl::AndExpression.__init__)


def test_javadsl::andexpression_constructor_args():
    sig = inspect.signature(javaDsl::AndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::andexpression_has_operators():
    assert hasattr(javaDsl::AndExpression, "operators")
    descriptor = None
    for klass in javaDsl::AndExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ExclusiveOrExpression)


def test_javadsl::exclusiveorexpression_constructor_exists():
    assert callable(javaDsl::ExclusiveOrExpression.__init__)


def test_javadsl::exclusiveorexpression_constructor_args():
    sig = inspect.signature(javaDsl::ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::exclusiveorexpression_has_operators():
    assert hasattr(javaDsl::ExclusiveOrExpression, "operators")
    descriptor = None
    for klass in javaDsl::ExclusiveOrExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConditionalAndExpression)


def test_javadsl::conditionalandexpression_constructor_exists():
    assert callable(javaDsl::ConditionalAndExpression.__init__)


def test_javadsl::conditionalandexpression_constructor_args():
    sig = inspect.signature(javaDsl::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::conditionalandexpression_has_operators():
    assert hasattr(javaDsl::ConditionalAndExpression, "operators")
    descriptor = None
    for klass in javaDsl::ConditionalAndExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConditionalOrExpression)


def test_javadsl::conditionalorexpression_constructor_exists():
    assert callable(javaDsl::ConditionalOrExpression.__init__)


def test_javadsl::conditionalorexpression_constructor_args():
    sig = inspect.signature(javaDsl::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::conditionalorexpression_has_operators():
    assert hasattr(javaDsl::ConditionalOrExpression, "operators")
    descriptor = None
    for klass in javaDsl::ConditionalOrExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::lefthandside_is_not_abstract():
    assert not inspect.isabstract(javaDsl::LeftHandSide)


def test_javadsl::lefthandside_constructor_exists():
    assert callable(javaDsl::LeftHandSide.__init__)


def test_javadsl::lefthandside_constructor_args():
    sig = inspect.signature(javaDsl::LeftHandSide.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpression)


def test_assignmentexpression_constructor_exists():
    assert callable(AssignmentExpression.__init__)


def test_assignmentexpression_constructor_args():
    sig = inspect.signature(AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConditionalExpression)


def test_javadsl::conditionalexpression_constructor_exists():
    assert callable(javaDsl::ConditionalExpression.__init__)


def test_javadsl::conditionalexpression_constructor_args():
    sig = inspect.signature(javaDsl::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::classinstancecreationexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ClassInstanceCreationExpression)


def test_javadsl::classinstancecreationexpression_constructor_exists():
    assert callable(javaDsl::ClassInstanceCreationExpression.__init__)


def test_javadsl::classinstancecreationexpression_constructor_args():
    sig = inspect.signature(javaDsl::ClassInstanceCreationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javadsl::classinstancecreationexpression_has_type():
    assert hasattr(javaDsl::ClassInstanceCreationExpression, "type")
    descriptor = None
    for klass in javaDsl::ClassInstanceCreationExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(javaDsl::MethodInvocation)


def test_javadsl::methodinvocation_constructor_exists():
    assert callable(javaDsl::MethodInvocation.__init__)


def test_javadsl::methodinvocation_constructor_args():
    sig = inspect.signature(javaDsl::MethodInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"
    assert "method" in params, "Missing parameter 'method'"

def test_javadsl::methodinvocation_has_keyword():
    assert hasattr(javaDsl::MethodInvocation, "keyword")
    descriptor = None
    for klass in javaDsl::MethodInvocation.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::methodinvocation_has_method():
    assert hasattr(javaDsl::MethodInvocation, "method")
    descriptor = None
    for klass in javaDsl::MethodInvocation.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::PreDecrementExpression)


def test_javadsl::predecrementexpression_constructor_exists():
    assert callable(javaDsl::PreDecrementExpression.__init__)


def test_javadsl::predecrementexpression_constructor_args():
    sig = inspect.signature(javaDsl::PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::PreIncrementExpression)


def test_javadsl::preincrementexpression_constructor_exists():
    assert callable(javaDsl::PreIncrementExpression.__init__)


def test_javadsl::preincrementexpression_constructor_args():
    sig = inspect.signature(javaDsl::PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::PostfixExpression)


def test_javadsl::postfixexpression_constructor_exists():
    assert callable(javaDsl::PostfixExpression.__init__)


def test_javadsl::postfixexpression_constructor_args():
    sig = inspect.signature(javaDsl::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::postfixexpression_has_reference():
    assert hasattr(javaDsl::PostfixExpression, "reference")
    descriptor = None
    for klass in javaDsl::PostfixExpression.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::postfixexpression_has_operators():
    assert hasattr(javaDsl::PostfixExpression, "operators")
    descriptor = None
    for klass in javaDsl::PostfixExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::assignment_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Assignment)


def test_javadsl::assignment_constructor_exists():
    assert callable(javaDsl::Assignment.__init__)


def test_javadsl::assignment_constructor_args():
    sig = inspect.signature(javaDsl::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javadsl::assignment_has_operator():
    assert hasattr(javaDsl::Assignment, "operator")
    descriptor = None
    for klass in javaDsl::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::AssignmentExpression)


def test_javadsl::assignmentexpression_constructor_exists():
    assert callable(javaDsl::AssignmentExpression.__init__)


def test_javadsl::assignmentexpression_constructor_args():
    sig = inspect.signature(javaDsl::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_primarynonewarray_is_not_abstract():
    assert not inspect.isabstract(PrimaryNoNewArray)


def test_primarynonewarray_constructor_exists():
    assert callable(PrimaryNoNewArray.__init__)


def test_primarynonewarray_constructor_args():
    sig = inspect.signature(PrimaryNoNewArray.__init__)
    params = list(sig.parameters.keys())



def test_constantexpression_is_not_abstract():
    assert not inspect.isabstract(ConstantExpression)


def test_constantexpression_constructor_exists():
    assert callable(ConstantExpression.__init__)


def test_constantexpression_constructor_args():
    sig = inspect.signature(ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::InclusiveOrExpression)


def test_javadsl::inclusiveorexpression_constructor_exists():
    assert callable(javaDsl::InclusiveOrExpression.__init__)


def test_javadsl::inclusiveorexpression_constructor_args():
    sig = inspect.signature(javaDsl::InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl::inclusiveorexpression_has_operators():
    assert hasattr(javaDsl::InclusiveOrExpression, "operators")
    descriptor = None
    for klass in javaDsl::InclusiveOrExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::forupdate_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ForUpdate)


def test_javadsl::forupdate_constructor_exists():
    assert callable(javaDsl::ForUpdate.__init__)


def test_javadsl::forupdate_constructor_args():
    sig = inspect.signature(javaDsl::ForUpdate.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::forinit_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ForInit)


def test_javadsl::forinit_constructor_exists():
    assert callable(javaDsl::ForInit.__init__)


def test_javadsl::forinit_constructor_args():
    sig = inspect.signature(javaDsl::ForInit.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::constantexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConstantExpression)


def test_javadsl::constantexpression_constructor_exists():
    assert callable(javaDsl::ConstantExpression.__init__)


def test_javadsl::constantexpression_constructor_args():
    sig = inspect.signature(javaDsl::ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_blockstatement_is_not_abstract():
    assert not inspect.isabstract(BlockStatement)


def test_blockstatement_constructor_exists():
    assert callable(BlockStatement.__init__)


def test_blockstatement_constructor_args():
    sig = inspect.signature(BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::statement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Statement)


def test_javadsl::statement_constructor_exists():
    assert callable(javaDsl::Statement.__init__)


def test_javadsl::statement_constructor_args():
    sig = inspect.signature(javaDsl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::localvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::LocalVariableDeclaration)


def test_javadsl::localvariabledeclaration_constructor_exists():
    assert callable(javaDsl::LocalVariableDeclaration.__init__)


def test_javadsl::localvariabledeclaration_constructor_args():
    sig = inspect.signature(javaDsl::LocalVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::LabeledStatement)


def test_javadsl::labeledstatement_constructor_exists():
    assert callable(javaDsl::LabeledStatement.__init__)


def test_javadsl::labeledstatement_constructor_args():
    sig = inspect.signature(javaDsl::LabeledStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_javadsl::labeledstatement_has_label():
    assert hasattr(javaDsl::LabeledStatement, "label")
    descriptor = None
    for klass in javaDsl::LabeledStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::dostatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::DoStatement)


def test_javadsl::dostatement_constructor_exists():
    assert callable(javaDsl::DoStatement.__init__)


def test_javadsl::dostatement_constructor_args():
    sig = inspect.signature(javaDsl::DoStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl::dostatement_has_condition():
    assert hasattr(javaDsl::DoStatement, "condition")
    descriptor = None
    for klass in javaDsl::DoStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::forstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ForStatement)


def test_javadsl::forstatement_constructor_exists():
    assert callable(javaDsl::ForStatement.__init__)


def test_javadsl::forstatement_constructor_args():
    sig = inspect.signature(javaDsl::ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl::forstatement_has_condition():
    assert hasattr(javaDsl::ForStatement, "condition")
    descriptor = None
    for klass in javaDsl::ForStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::breakstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::BreakStatement)


def test_javadsl::breakstatement_constructor_exists():
    assert callable(javaDsl::BreakStatement.__init__)


def test_javadsl::breakstatement_constructor_args():
    sig = inspect.signature(javaDsl::BreakStatement.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl::breakstatement_has_reference():
    assert hasattr(javaDsl::BreakStatement, "reference")
    descriptor = None
    for klass in javaDsl::BreakStatement.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::IfStatement)


def test_javadsl::ifstatement_constructor_exists():
    assert callable(javaDsl::IfStatement.__init__)


def test_javadsl::ifstatement_constructor_args():
    sig = inspect.signature(javaDsl::IfStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl::ifstatement_has_condition():
    assert hasattr(javaDsl::IfStatement, "condition")
    descriptor = None
    for klass in javaDsl::IfStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::returnstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ReturnStatement)


def test_javadsl::returnstatement_constructor_exists():
    assert callable(javaDsl::ReturnStatement.__init__)


def test_javadsl::returnstatement_constructor_args():
    sig = inspect.signature(javaDsl::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::trystatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::TryStatement)


def test_javadsl::trystatement_constructor_exists():
    assert callable(javaDsl::TryStatement.__init__)


def test_javadsl::trystatement_constructor_args():
    sig = inspect.signature(javaDsl::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::switchstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::SwitchStatement)


def test_javadsl::switchstatement_constructor_exists():
    assert callable(javaDsl::SwitchStatement.__init__)


def test_javadsl::switchstatement_constructor_args():
    sig = inspect.signature(javaDsl::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::SynchronizedStatement)


def test_javadsl::synchronizedstatement_constructor_exists():
    assert callable(javaDsl::SynchronizedStatement.__init__)


def test_javadsl::synchronizedstatement_constructor_args():
    sig = inspect.signature(javaDsl::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::continuestatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ContinueStatement)


def test_javadsl::continuestatement_constructor_exists():
    assert callable(javaDsl::ContinueStatement.__init__)


def test_javadsl::continuestatement_constructor_args():
    sig = inspect.signature(javaDsl::ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl::continuestatement_has_reference():
    assert hasattr(javaDsl::ContinueStatement, "reference")
    descriptor = None
    for klass in javaDsl::ContinueStatement.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::statementexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::StatementExpression)


def test_javadsl::statementexpression_constructor_exists():
    assert callable(javaDsl::StatementExpression.__init__)


def test_javadsl::statementexpression_constructor_args():
    sig = inspect.signature(javaDsl::StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::throwsstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ThrowsStatement)


def test_javadsl::throwsstatement_constructor_exists():
    assert callable(javaDsl::ThrowsStatement.__init__)


def test_javadsl::throwsstatement_constructor_args():
    sig = inspect.signature(javaDsl::ThrowsStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::whilestatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::WhileStatement)


def test_javadsl::whilestatement_constructor_exists():
    assert callable(javaDsl::WhileStatement.__init__)


def test_javadsl::whilestatement_constructor_args():
    sig = inspect.signature(javaDsl::WhileStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl::whilestatement_has_condition():
    assert hasattr(javaDsl::WhileStatement, "condition")
    descriptor = None
    for klass in javaDsl::WhileStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ArrayInitializer)


def test_javadsl::arrayinitializer_constructor_exists():
    assert callable(javaDsl::ArrayInitializer.__init__)


def test_javadsl::arrayinitializer_constructor_args():
    sig = inspect.signature(javaDsl::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_interfacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(InterfaceMemberDeclaration)


def test_interfacememberdeclaration_constructor_exists():
    assert callable(InterfaceMemberDeclaration.__init__)


def test_interfacememberdeclaration_constructor_args():
    sig = inspect.signature(InterfaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::AbstractMethodDeclaration)


def test_javadsl::abstractmethoddeclaration_constructor_exists():
    assert callable(javaDsl::AbstractMethodDeclaration.__init__)


def test_javadsl::abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(javaDsl::AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConstantDeclaration)


def test_javadsl::constantdeclaration_constructor_exists():
    assert callable(javaDsl::ConstantDeclaration.__init__)


def test_javadsl::constantdeclaration_constructor_args():
    sig = inspect.signature(javaDsl::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::interfacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::InterfaceMemberDeclaration)


def test_javadsl::interfacememberdeclaration_constructor_exists():
    assert callable(javaDsl::InterfaceMemberDeclaration.__init__)


def test_javadsl::interfacememberdeclaration_constructor_args():
    sig = inspect.signature(javaDsl::InterfaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl::interfacememberdeclaration_has_modifiers():
    assert hasattr(javaDsl::InterfaceMemberDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl::InterfaceMemberDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::interfacebody_is_not_abstract():
    assert not inspect.isabstract(javaDsl::InterfaceBody)


def test_javadsl::interfacebody_constructor_exists():
    assert callable(javaDsl::InterfaceBody.__init__)


def test_javadsl::interfacebody_constructor_args():
    sig = inspect.signature(javaDsl::InterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::extendsinterfaces_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ExtendsInterfaces)


def test_javadsl::extendsinterfaces_constructor_exists():
    assert callable(javaDsl::ExtendsInterfaces.__init__)


def test_javadsl::extendsinterfaces_constructor_args():
    sig = inspect.signature(javaDsl::ExtendsInterfaces.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"
    assert "interfaces" in params, "Missing parameter 'interfaces'"

def test_javadsl::extendsinterfaces_has_keyword():
    assert hasattr(javaDsl::ExtendsInterfaces, "keyword")
    descriptor = None
    for klass in javaDsl::ExtendsInterfaces.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::extendsinterfaces_has_interfaces():
    assert hasattr(javaDsl::ExtendsInterfaces, "interfaces")
    descriptor = None
    for klass in javaDsl::ExtendsInterfaces.__mro__:
        if "interfaces" in klass.__dict__:
            descriptor = klass.__dict__["interfaces"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::InterfaceDeclaration)


def test_javadsl::interfacedeclaration_constructor_exists():
    assert callable(javaDsl::InterfaceDeclaration.__init__)


def test_javadsl::interfacedeclaration_constructor_args():
    sig = inspect.signature(javaDsl::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl::interfacedeclaration_has_name():
    assert hasattr(javaDsl::InterfaceDeclaration, "name")
    descriptor = None
    for klass in javaDsl::InterfaceDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::interfacedeclaration_has_modifiers():
    assert hasattr(javaDsl::InterfaceDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl::InterfaceDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::methoddeclarator_is_not_abstract():
    assert not inspect.isabstract(javaDsl::MethodDeclarator)


def test_javadsl::methoddeclarator_constructor_exists():
    assert callable(javaDsl::MethodDeclarator.__init__)


def test_javadsl::methoddeclarator_constructor_args():
    sig = inspect.signature(javaDsl::MethodDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl::methoddeclarator_has_name():
    assert hasattr(javaDsl::MethodDeclarator, "name")
    descriptor = None
    for klass in javaDsl::MethodDeclarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::resulttype_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ResultType)


def test_javadsl::resulttype_constructor_exists():
    assert callable(javaDsl::ResultType.__init__)


def test_javadsl::resulttype_constructor_args():
    sig = inspect.signature(javaDsl::ResultType.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::methodheader_is_not_abstract():
    assert not inspect.isabstract(javaDsl::MethodHeader)


def test_javadsl::methodheader_constructor_exists():
    assert callable(javaDsl::MethodHeader.__init__)


def test_javadsl::methodheader_constructor_args():
    sig = inspect.signature(javaDsl::MethodHeader.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl::methodheader_has_modifiers():
    assert hasattr(javaDsl::MethodHeader, "modifiers")
    descriptor = None
    for klass in javaDsl::MethodHeader.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(javaDsl::VariableDeclarator)


def test_javadsl::variabledeclarator_constructor_exists():
    assert callable(javaDsl::VariableDeclarator.__init__)


def test_javadsl::variabledeclarator_constructor_args():
    sig = inspect.signature(javaDsl::VariableDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl::variabledeclarator_has_name():
    assert hasattr(javaDsl::VariableDeclarator, "name")
    descriptor = None
    for klass in javaDsl::VariableDeclarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::argumentlist_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ArgumentList)


def test_javadsl::argumentlist_constructor_exists():
    assert callable(javaDsl::ArgumentList.__init__)


def test_javadsl::argumentlist_constructor_args():
    sig = inspect.signature(javaDsl::ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::blockstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::BlockStatement)


def test_javadsl::blockstatement_constructor_exists():
    assert callable(javaDsl::BlockStatement.__init__)


def test_javadsl::blockstatement_constructor_args():
    sig = inspect.signature(javaDsl::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::explicitconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ExplicitConstructorInvocation)


def test_javadsl::explicitconstructorinvocation_constructor_exists():
    assert callable(javaDsl::ExplicitConstructorInvocation.__init__)


def test_javadsl::explicitconstructorinvocation_constructor_args():
    sig = inspect.signature(javaDsl::ExplicitConstructorInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl::explicitconstructorinvocation_has_keyword():
    assert hasattr(javaDsl::ExplicitConstructorInvocation, "keyword")
    descriptor = None
    for klass in javaDsl::ExplicitConstructorInvocation.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::type_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Type)


def test_javadsl::type_constructor_exists():
    assert callable(javaDsl::Type.__init__)


def test_javadsl::type_constructor_args():
    sig = inspect.signature(javaDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl::type_has_name():
    assert hasattr(javaDsl::Type, "name")
    descriptor = None
    for klass in javaDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::formalparameter_is_not_abstract():
    assert not inspect.isabstract(javaDsl::FormalParameter)


def test_javadsl::formalparameter_constructor_exists():
    assert callable(javaDsl::FormalParameter.__init__)


def test_javadsl::formalparameter_constructor_args():
    sig = inspect.signature(javaDsl::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_javadsl::formalparameter_has_variable():
    assert hasattr(javaDsl::FormalParameter, "variable")
    descriptor = None
    for klass in javaDsl::FormalParameter.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::constructorbody_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConstructorBody)


def test_javadsl::constructorbody_constructor_exists():
    assert callable(javaDsl::ConstructorBody.__init__)


def test_javadsl::constructorbody_constructor_args():
    sig = inspect.signature(javaDsl::ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::exceptions_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Exceptions)


def test_javadsl::exceptions_constructor_exists():
    assert callable(javaDsl::Exceptions.__init__)


def test_javadsl::exceptions_constructor_args():
    sig = inspect.signature(javaDsl::Exceptions.__init__)
    params = list(sig.parameters.keys())
    assert "exceptions" in params, "Missing parameter 'exceptions'"

def test_javadsl::exceptions_has_exceptions():
    assert hasattr(javaDsl::Exceptions, "exceptions")
    descriptor = None
    for klass in javaDsl::Exceptions.__mro__:
        if "exceptions" in klass.__dict__:
            descriptor = klass.__dict__["exceptions"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::constructordeclarator_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConstructorDeclarator)


def test_javadsl::constructordeclarator_constructor_exists():
    assert callable(javaDsl::ConstructorDeclarator.__init__)


def test_javadsl::constructordeclarator_constructor_args():
    sig = inspect.signature(javaDsl::ConstructorDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl::constructordeclarator_has_name():
    assert hasattr(javaDsl::ConstructorDeclarator, "name")
    descriptor = None
    for klass in javaDsl::ConstructorDeclarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::block_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Block)


def test_javadsl::block_constructor_exists():
    assert callable(javaDsl::Block.__init__)


def test_javadsl::block_constructor_args():
    sig = inspect.signature(javaDsl::Block.__init__)
    params = list(sig.parameters.keys())



def test_classbodydeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassBodyDeclaration)


def test_classbodydeclaration_constructor_exists():
    assert callable(ClassBodyDeclaration.__init__)


def test_classbodydeclaration_constructor_args():
    sig = inspect.signature(ClassBodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ConstructorDeclaration)


def test_javadsl::constructordeclaration_constructor_exists():
    assert callable(javaDsl::ConstructorDeclaration.__init__)


def test_javadsl::constructordeclaration_constructor_args():
    sig = inspect.signature(javaDsl::ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl::constructordeclaration_has_modifiers():
    assert hasattr(javaDsl::ConstructorDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl::ConstructorDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::staticinitializer_is_not_abstract():
    assert not inspect.isabstract(javaDsl::StaticInitializer)


def test_javadsl::staticinitializer_constructor_exists():
    assert callable(javaDsl::StaticInitializer.__init__)


def test_javadsl::staticinitializer_constructor_args():
    sig = inspect.signature(javaDsl::StaticInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::MethodDeclaration)


def test_javadsl::methoddeclaration_constructor_exists():
    assert callable(javaDsl::MethodDeclaration.__init__)


def test_javadsl::methoddeclaration_constructor_args():
    sig = inspect.signature(javaDsl::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::FieldDeclaration)


def test_javadsl::fielddeclaration_constructor_exists():
    assert callable(javaDsl::FieldDeclaration.__init__)


def test_javadsl::fielddeclaration_constructor_args():
    sig = inspect.signature(javaDsl::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl::fielddeclaration_has_modifiers():
    assert hasattr(javaDsl::FieldDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl::FieldDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ClassMemberDeclaration)


def test_javadsl::classmemberdeclaration_constructor_exists():
    assert callable(javaDsl::ClassMemberDeclaration.__init__)


def test_javadsl::classmemberdeclaration_constructor_args():
    sig = inspect.signature(javaDsl::ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::expression_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Expression)


def test_javadsl::expression_constructor_exists():
    assert callable(javaDsl::Expression.__init__)


def test_javadsl::expression_constructor_args():
    sig = inspect.signature(javaDsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::variableinitializer_is_not_abstract():
    assert not inspect.isabstract(javaDsl::VariableInitializer)


def test_javadsl::variableinitializer_constructor_exists():
    assert callable(javaDsl::VariableInitializer.__init__)


def test_javadsl::variableinitializer_constructor_args():
    sig = inspect.signature(javaDsl::VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::classbody_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ClassBody)


def test_javadsl::classbody_constructor_exists():
    assert callable(javaDsl::ClassBody.__init__)


def test_javadsl::classbody_constructor_args():
    sig = inspect.signature(javaDsl::ClassBody.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::interfaces_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Interfaces)


def test_javadsl::interfaces_constructor_exists():
    assert callable(javaDsl::Interfaces.__init__)


def test_javadsl::interfaces_constructor_args():
    sig = inspect.signature(javaDsl::Interfaces.__init__)
    params = list(sig.parameters.keys())
    assert "interfaces" in params, "Missing parameter 'interfaces'"
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl::interfaces_has_interfaces():
    assert hasattr(javaDsl::Interfaces, "interfaces")
    descriptor = None
    for klass in javaDsl::Interfaces.__mro__:
        if "interfaces" in klass.__dict__:
            descriptor = klass.__dict__["interfaces"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::interfaces_has_keyword():
    assert hasattr(javaDsl::Interfaces, "keyword")
    descriptor = None
    for klass in javaDsl::Interfaces.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ClassDeclaration)


def test_javadsl::classdeclaration_constructor_exists():
    assert callable(javaDsl::ClassDeclaration.__init__)


def test_javadsl::classdeclaration_constructor_args():
    sig = inspect.signature(javaDsl::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "extend" in params, "Missing parameter 'extend'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl::classdeclaration_has_className():
    assert hasattr(javaDsl::ClassDeclaration, "className")
    descriptor = None
    for klass in javaDsl::ClassDeclaration.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::classdeclaration_has_extend():
    assert hasattr(javaDsl::ClassDeclaration, "extend")
    descriptor = None
    for klass in javaDsl::ClassDeclaration.__mro__:
        if "extend" in klass.__dict__:
            descriptor = klass.__dict__["extend"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::classdeclaration_has_modifiers():
    assert hasattr(javaDsl::ClassDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl::ClassDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::eobject_is_not_abstract():
    assert not inspect.isabstract(javaDsl::EObject)


def test_javadsl::eobject_constructor_exists():
    assert callable(javaDsl::EObject.__init__)


def test_javadsl::eobject_constructor_args():
    sig = inspect.signature(javaDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::TypeDeclaration)


def test_javadsl::typedeclaration_constructor_exists():
    assert callable(javaDsl::TypeDeclaration.__init__)


def test_javadsl::typedeclaration_constructor_args():
    sig = inspect.signature(javaDsl::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"

def test_javadsl::typedeclaration_has_doc():
    assert hasattr(javaDsl::TypeDeclaration, "doc")
    descriptor = None
    for klass in javaDsl::TypeDeclaration.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::importstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ImportStatement)


def test_javadsl::importstatement_constructor_exists():
    assert callable(javaDsl::ImportStatement.__init__)


def test_javadsl::importstatement_constructor_args():
    sig = inspect.signature(javaDsl::ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "object" in params, "Missing parameter 'object'"

def test_javadsl::importstatement_has_package():
    assert hasattr(javaDsl::ImportStatement, "package")
    descriptor = None
    for klass in javaDsl::ImportStatement.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_javadsl::importstatement_has_object():
    assert hasattr(javaDsl::ImportStatement, "object")
    descriptor = None
    for klass in javaDsl::ImportStatement.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::packagestatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl::PackageStatement)


def test_javadsl::packagestatement_constructor_exists():
    assert callable(javaDsl::PackageStatement.__init__)


def test_javadsl::packagestatement_constructor_args():
    sig = inspect.signature(javaDsl::PackageStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl::packagestatement_has_name():
    assert hasattr(javaDsl::PackageStatement, "name")
    descriptor = None
    for klass in javaDsl::PackageStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl::compilationunit_is_not_abstract():
    assert not inspect.isabstract(javaDsl::CompilationUnit)


def test_javadsl::compilationunit_constructor_exists():
    assert callable(javaDsl::CompilationUnit.__init__)


def test_javadsl::compilationunit_constructor_args():
    sig = inspect.signature(javaDsl::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::head_is_not_abstract():
    assert not inspect.isabstract(javaDsl::Head)


def test_javadsl::head_constructor_exists():
    assert callable(javaDsl::Head.__init__)


def test_javadsl::head_constructor_args():
    sig = inspect.signature(javaDsl::Head.__init__)
    params = list(sig.parameters.keys())



def test_javadsl::classbodydeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl::ClassBodyDeclaration)


def test_javadsl::classbodydeclaration_constructor_exists():
    assert callable(javaDsl::ClassBodyDeclaration.__init__)


def test_javadsl::classbodydeclaration_constructor_args():
    sig = inspect.signature(javaDsl::ClassBodyDeclaration.__init__)
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
javaDsl::ArrayCreationExpression_strategy = st.builds(
    javaDsl::ArrayCreationExpression,
    type=
        safe_text,
    layers=
        safe_text
)
Primary_strategy = st.builds(
    Primary,
)
javaDsl::PrimaryNewArray_strategy = st.builds(
    javaDsl::PrimaryNewArray,
)
javaDsl::PrimaryNoNewArray_strategy = st.builds(
    javaDsl::PrimaryNoNewArray,
    literal=
        safe_text,
    method=
        safe_text,
    reference=
        safe_text,
    keyword=
        safe_text
)
javaDsl::ArrayExpression_strategy = st.builds(
    javaDsl::ArrayExpression,
)
LeftHandSide_strategy = st.builds(
    LeftHandSide,
)
javaDsl::ArrayAccess_strategy = st.builds(
    javaDsl::ArrayAccess,
    reference=
        safe_text
)
javaDsl::FieldAccess_strategy = st.builds(
    javaDsl::FieldAccess,
    field=
        safe_text,
    keyword=
        safe_text
)
javaDsl::Primary_strategy = st.builds(
    javaDsl::Primary,
    fields=
        safe_text
)
NoArrayExpression_strategy = st.builds(
    NoArrayExpression,
)
javaDsl::NoArrayExpressionWithoutMinus_strategy = st.builds(
    javaDsl::NoArrayExpressionWithoutMinus,
)
NoArrayExpressionWithoutMinus_strategy = st.builds(
    NoArrayExpressionWithoutMinus,
)
javaDsl::CastExpression_strategy = st.builds(
    javaDsl::CastExpression,
    type=
        safe_text
)
javaDsl::NoArrayExpression_strategy = st.builds(
    javaDsl::NoArrayExpression,
    operator=
        safe_text
)
javaDsl::MultiplicativeExpression_strategy = st.builds(
    javaDsl::MultiplicativeExpression,
    operators=
        safe_text
)
javaDsl::AdditiveExpression_strategy = st.builds(
    javaDsl::AdditiveExpression,
    operators=
        safe_text
)
javaDsl::ShiftExpression_strategy = st.builds(
    javaDsl::ShiftExpression,
    operators=
        safe_text
)
javaDsl::RelationalExpression_strategy = st.builds(
    javaDsl::RelationalExpression,
    operators=
        safe_text,
    classes=
        safe_text
)
javaDsl::EqualityExpression_strategy = st.builds(
    javaDsl::EqualityExpression,
    operators=
        safe_text
)
javaDsl::AndExpression_strategy = st.builds(
    javaDsl::AndExpression,
    operators=
        safe_text
)
javaDsl::ExclusiveOrExpression_strategy = st.builds(
    javaDsl::ExclusiveOrExpression,
    operators=
        safe_text
)
javaDsl::ConditionalAndExpression_strategy = st.builds(
    javaDsl::ConditionalAndExpression,
    operators=
        safe_text
)
javaDsl::ConditionalOrExpression_strategy = st.builds(
    javaDsl::ConditionalOrExpression,
    operators=
        safe_text
)
javaDsl::LeftHandSide_strategy = st.builds(
    javaDsl::LeftHandSide,
)
AssignmentExpression_strategy = st.builds(
    AssignmentExpression,
)
javaDsl::ConditionalExpression_strategy = st.builds(
    javaDsl::ConditionalExpression,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
javaDsl::ClassInstanceCreationExpression_strategy = st.builds(
    javaDsl::ClassInstanceCreationExpression,
    type=
        safe_text
)
javaDsl::MethodInvocation_strategy = st.builds(
    javaDsl::MethodInvocation,
    keyword=
        safe_text,
    method=
        safe_text
)
javaDsl::PreDecrementExpression_strategy = st.builds(
    javaDsl::PreDecrementExpression,
)
javaDsl::PreIncrementExpression_strategy = st.builds(
    javaDsl::PreIncrementExpression,
)
javaDsl::PostfixExpression_strategy = st.builds(
    javaDsl::PostfixExpression,
    reference=
        safe_text,
    operators=
        safe_text
)
javaDsl::Assignment_strategy = st.builds(
    javaDsl::Assignment,
    operator=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
javaDsl::AssignmentExpression_strategy = st.builds(
    javaDsl::AssignmentExpression,
)
PrimaryNoNewArray_strategy = st.builds(
    PrimaryNoNewArray,
)
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
javaDsl::InclusiveOrExpression_strategy = st.builds(
    javaDsl::InclusiveOrExpression,
    operators=
        safe_text
)
javaDsl::ForUpdate_strategy = st.builds(
    javaDsl::ForUpdate,
)
javaDsl::ForInit_strategy = st.builds(
    javaDsl::ForInit,
)
javaDsl::ConstantExpression_strategy = st.builds(
    javaDsl::ConstantExpression,
)
BlockStatement_strategy = st.builds(
    BlockStatement,
)
javaDsl::Statement_strategy = st.builds(
    javaDsl::Statement,
)
javaDsl::LocalVariableDeclaration_strategy = st.builds(
    javaDsl::LocalVariableDeclaration,
)
Statement_strategy = st.builds(
    Statement,
)
javaDsl::LabeledStatement_strategy = st.builds(
    javaDsl::LabeledStatement,
    label=
        safe_text
)
javaDsl::DoStatement_strategy = st.builds(
    javaDsl::DoStatement,
    condition=
        st.booleans()
)
javaDsl::ForStatement_strategy = st.builds(
    javaDsl::ForStatement,
    condition=
        st.booleans()
)
javaDsl::BreakStatement_strategy = st.builds(
    javaDsl::BreakStatement,
    reference=
        safe_text
)
javaDsl::IfStatement_strategy = st.builds(
    javaDsl::IfStatement,
    condition=
        st.booleans()
)
javaDsl::ReturnStatement_strategy = st.builds(
    javaDsl::ReturnStatement,
)
javaDsl::TryStatement_strategy = st.builds(
    javaDsl::TryStatement,
)
javaDsl::SwitchStatement_strategy = st.builds(
    javaDsl::SwitchStatement,
)
javaDsl::SynchronizedStatement_strategy = st.builds(
    javaDsl::SynchronizedStatement,
)
javaDsl::ContinueStatement_strategy = st.builds(
    javaDsl::ContinueStatement,
    reference=
        safe_text
)
javaDsl::StatementExpression_strategy = st.builds(
    javaDsl::StatementExpression,
)
javaDsl::ThrowsStatement_strategy = st.builds(
    javaDsl::ThrowsStatement,
)
javaDsl::WhileStatement_strategy = st.builds(
    javaDsl::WhileStatement,
    condition=
        st.booleans()
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
javaDsl::ArrayInitializer_strategy = st.builds(
    javaDsl::ArrayInitializer,
)
InterfaceMemberDeclaration_strategy = st.builds(
    InterfaceMemberDeclaration,
)
javaDsl::AbstractMethodDeclaration_strategy = st.builds(
    javaDsl::AbstractMethodDeclaration,
)
javaDsl::ConstantDeclaration_strategy = st.builds(
    javaDsl::ConstantDeclaration,
)
javaDsl::InterfaceMemberDeclaration_strategy = st.builds(
    javaDsl::InterfaceMemberDeclaration,
    modifiers=
        safe_text
)
javaDsl::InterfaceBody_strategy = st.builds(
    javaDsl::InterfaceBody,
)
javaDsl::ExtendsInterfaces_strategy = st.builds(
    javaDsl::ExtendsInterfaces,
    keyword=
        safe_text,
    interfaces=
        safe_text
)
javaDsl::InterfaceDeclaration_strategy = st.builds(
    javaDsl::InterfaceDeclaration,
    name=
        safe_text,
    modifiers=
        safe_text
)
javaDsl::MethodDeclarator_strategy = st.builds(
    javaDsl::MethodDeclarator,
    name=
        safe_text
)
javaDsl::ResultType_strategy = st.builds(
    javaDsl::ResultType,
)
javaDsl::MethodHeader_strategy = st.builds(
    javaDsl::MethodHeader,
    modifiers=
        safe_text
)
javaDsl::VariableDeclarator_strategy = st.builds(
    javaDsl::VariableDeclarator,
    name=
        safe_text
)
javaDsl::ArgumentList_strategy = st.builds(
    javaDsl::ArgumentList,
)
javaDsl::BlockStatement_strategy = st.builds(
    javaDsl::BlockStatement,
)
javaDsl::ExplicitConstructorInvocation_strategy = st.builds(
    javaDsl::ExplicitConstructorInvocation,
    keyword=
        safe_text
)
javaDsl::Type_strategy = st.builds(
    javaDsl::Type,
    name=
        safe_text
)
javaDsl::FormalParameter_strategy = st.builds(
    javaDsl::FormalParameter,
    variable=
        safe_text
)
javaDsl::ConstructorBody_strategy = st.builds(
    javaDsl::ConstructorBody,
)
javaDsl::Exceptions_strategy = st.builds(
    javaDsl::Exceptions,
    exceptions=
        safe_text
)
javaDsl::ConstructorDeclarator_strategy = st.builds(
    javaDsl::ConstructorDeclarator,
    name=
        safe_text
)
javaDsl::Block_strategy = st.builds(
    javaDsl::Block,
)
ClassBodyDeclaration_strategy = st.builds(
    ClassBodyDeclaration,
)
javaDsl::ConstructorDeclaration_strategy = st.builds(
    javaDsl::ConstructorDeclaration,
    modifiers=
        safe_text
)
javaDsl::StaticInitializer_strategy = st.builds(
    javaDsl::StaticInitializer,
)
javaDsl::MethodDeclaration_strategy = st.builds(
    javaDsl::MethodDeclaration,
)
javaDsl::FieldDeclaration_strategy = st.builds(
    javaDsl::FieldDeclaration,
    modifiers=
        safe_text
)
javaDsl::ClassMemberDeclaration_strategy = st.builds(
    javaDsl::ClassMemberDeclaration,
)
javaDsl::Expression_strategy = st.builds(
    javaDsl::Expression,
)
javaDsl::VariableInitializer_strategy = st.builds(
    javaDsl::VariableInitializer,
)
javaDsl::ClassBody_strategy = st.builds(
    javaDsl::ClassBody,
)
javaDsl::Interfaces_strategy = st.builds(
    javaDsl::Interfaces,
    interfaces=
        safe_text,
    keyword=
        safe_text
)
javaDsl::ClassDeclaration_strategy = st.builds(
    javaDsl::ClassDeclaration,
    className=
        safe_text,
    extend=
        safe_text,
    modifiers=
        safe_text
)
javaDsl::EObject_strategy = st.builds(
    javaDsl::EObject,
)
javaDsl::TypeDeclaration_strategy = st.builds(
    javaDsl::TypeDeclaration,
    doc=
        safe_text
)
javaDsl::ImportStatement_strategy = st.builds(
    javaDsl::ImportStatement,
    package=
        safe_text,
    object=
        safe_text
)
javaDsl::PackageStatement_strategy = st.builds(
    javaDsl::PackageStatement,
    name=
        safe_text
)
javaDsl::CompilationUnit_strategy = st.builds(
    javaDsl::CompilationUnit,
)
javaDsl::Head_strategy = st.builds(
    javaDsl::Head,
)
javaDsl::ClassBodyDeclaration_strategy = st.builds(
    javaDsl::ClassBodyDeclaration,
)

@given(instance=javaDsl::ArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_javadsl::arraycreationexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ArrayCreationExpression)

@given(instance=javaDsl::ArrayCreationExpression_strategy)
def test_javadsl::arraycreationexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=javaDsl::ArrayCreationExpression_strategy)
def test_javadsl::arraycreationexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=javaDsl::ArrayCreationExpression_strategy)
def test_javadsl::arraycreationexpression_layers_type(instance):
    assert isinstance(instance.layers, str)


@given(instance=javaDsl::ArrayCreationExpression_strategy)
def test_javadsl::arraycreationexpression_layers_setter(instance):
    original = instance.layers
    instance.layers = original
    assert instance.layers == original

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=javaDsl::PrimaryNewArray_strategy)
@settings(max_examples=50)
def test_javadsl::primarynewarray_instantiation(instance):
    assert isinstance(instance, javaDsl::PrimaryNewArray)

@given(instance=javaDsl::PrimaryNoNewArray_strategy)
@settings(max_examples=50)
def test_javadsl::primarynonewarray_instantiation(instance):
    assert isinstance(instance, javaDsl::PrimaryNoNewArray)

@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=javaDsl::PrimaryNoNewArray_strategy)
def test_javadsl::primarynonewarray_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl::ArrayExpression_strategy)
@settings(max_examples=50)
def test_javadsl::arrayexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ArrayExpression)

@given(instance=LeftHandSide_strategy)
@settings(max_examples=50)
def test_lefthandside_instantiation(instance):
    assert isinstance(instance, LeftHandSide)

@given(instance=javaDsl::ArrayAccess_strategy)
@settings(max_examples=50)
def test_javadsl::arrayaccess_instantiation(instance):
    assert isinstance(instance, javaDsl::ArrayAccess)

@given(instance=javaDsl::ArrayAccess_strategy)
def test_javadsl::arrayaccess_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=javaDsl::ArrayAccess_strategy)
def test_javadsl::arrayaccess_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl::FieldAccess_strategy)
@settings(max_examples=50)
def test_javadsl::fieldaccess_instantiation(instance):
    assert isinstance(instance, javaDsl::FieldAccess)

@given(instance=javaDsl::FieldAccess_strategy)
def test_javadsl::fieldaccess_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=javaDsl::FieldAccess_strategy)
def test_javadsl::fieldaccess_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=javaDsl::FieldAccess_strategy)
def test_javadsl::fieldaccess_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=javaDsl::FieldAccess_strategy)
def test_javadsl::fieldaccess_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl::Primary_strategy)
@settings(max_examples=50)
def test_javadsl::primary_instantiation(instance):
    assert isinstance(instance, javaDsl::Primary)

@given(instance=javaDsl::Primary_strategy)
def test_javadsl::primary_fields_type(instance):
    assert isinstance(instance.fields, str)


@given(instance=javaDsl::Primary_strategy)
def test_javadsl::primary_fields_setter(instance):
    original = instance.fields
    instance.fields = original
    assert instance.fields == original

@given(instance=NoArrayExpression_strategy)
@settings(max_examples=50)
def test_noarrayexpression_instantiation(instance):
    assert isinstance(instance, NoArrayExpression)

@given(instance=javaDsl::NoArrayExpressionWithoutMinus_strategy)
@settings(max_examples=50)
def test_javadsl::noarrayexpressionwithoutminus_instantiation(instance):
    assert isinstance(instance, javaDsl::NoArrayExpressionWithoutMinus)

@given(instance=NoArrayExpressionWithoutMinus_strategy)
@settings(max_examples=50)
def test_noarrayexpressionwithoutminus_instantiation(instance):
    assert isinstance(instance, NoArrayExpressionWithoutMinus)

@given(instance=javaDsl::CastExpression_strategy)
@settings(max_examples=50)
def test_javadsl::castexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::CastExpression)

@given(instance=javaDsl::CastExpression_strategy)
def test_javadsl::castexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=javaDsl::CastExpression_strategy)
def test_javadsl::castexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=javaDsl::NoArrayExpression_strategy)
@settings(max_examples=50)
def test_javadsl::noarrayexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::NoArrayExpression)

@given(instance=javaDsl::NoArrayExpression_strategy)
def test_javadsl::noarrayexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=javaDsl::NoArrayExpression_strategy)
def test_javadsl::noarrayexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=javaDsl::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_javadsl::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::MultiplicativeExpression)

@given(instance=javaDsl::MultiplicativeExpression_strategy)
def test_javadsl::multiplicativeexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::MultiplicativeExpression_strategy)
def test_javadsl::multiplicativeexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_javadsl::additiveexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::AdditiveExpression)

@given(instance=javaDsl::AdditiveExpression_strategy)
def test_javadsl::additiveexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::AdditiveExpression_strategy)
def test_javadsl::additiveexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::ShiftExpression_strategy)
@settings(max_examples=50)
def test_javadsl::shiftexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ShiftExpression)

@given(instance=javaDsl::ShiftExpression_strategy)
def test_javadsl::shiftexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::ShiftExpression_strategy)
def test_javadsl::shiftexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::RelationalExpression_strategy)
@settings(max_examples=50)
def test_javadsl::relationalexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::RelationalExpression)

@given(instance=javaDsl::RelationalExpression_strategy)
def test_javadsl::relationalexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::RelationalExpression_strategy)
def test_javadsl::relationalexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::RelationalExpression_strategy)
def test_javadsl::relationalexpression_classes_type(instance):
    assert isinstance(instance.classes, str)


@given(instance=javaDsl::RelationalExpression_strategy)
def test_javadsl::relationalexpression_classes_setter(instance):
    original = instance.classes
    instance.classes = original
    assert instance.classes == original

@given(instance=javaDsl::EqualityExpression_strategy)
@settings(max_examples=50)
def test_javadsl::equalityexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::EqualityExpression)

@given(instance=javaDsl::EqualityExpression_strategy)
def test_javadsl::equalityexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::EqualityExpression_strategy)
def test_javadsl::equalityexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::AndExpression_strategy)
@settings(max_examples=50)
def test_javadsl::andexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::AndExpression)

@given(instance=javaDsl::AndExpression_strategy)
def test_javadsl::andexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::AndExpression_strategy)
def test_javadsl::andexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_javadsl::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ExclusiveOrExpression)

@given(instance=javaDsl::ExclusiveOrExpression_strategy)
def test_javadsl::exclusiveorexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::ExclusiveOrExpression_strategy)
def test_javadsl::exclusiveorexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_javadsl::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ConditionalAndExpression)

@given(instance=javaDsl::ConditionalAndExpression_strategy)
def test_javadsl::conditionalandexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::ConditionalAndExpression_strategy)
def test_javadsl::conditionalandexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_javadsl::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ConditionalOrExpression)

@given(instance=javaDsl::ConditionalOrExpression_strategy)
def test_javadsl::conditionalorexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::ConditionalOrExpression_strategy)
def test_javadsl::conditionalorexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::LeftHandSide_strategy)
@settings(max_examples=50)
def test_javadsl::lefthandside_instantiation(instance):
    assert isinstance(instance, javaDsl::LeftHandSide)

@given(instance=AssignmentExpression_strategy)
@settings(max_examples=50)
def test_assignmentexpression_instantiation(instance):
    assert isinstance(instance, AssignmentExpression)

@given(instance=javaDsl::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_javadsl::conditionalexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ConditionalExpression)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=javaDsl::ClassInstanceCreationExpression_strategy)
@settings(max_examples=50)
def test_javadsl::classinstancecreationexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ClassInstanceCreationExpression)

@given(instance=javaDsl::ClassInstanceCreationExpression_strategy)
def test_javadsl::classinstancecreationexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=javaDsl::ClassInstanceCreationExpression_strategy)
def test_javadsl::classinstancecreationexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=javaDsl::MethodInvocation_strategy)
@settings(max_examples=50)
def test_javadsl::methodinvocation_instantiation(instance):
    assert isinstance(instance, javaDsl::MethodInvocation)

@given(instance=javaDsl::MethodInvocation_strategy)
def test_javadsl::methodinvocation_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=javaDsl::MethodInvocation_strategy)
def test_javadsl::methodinvocation_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl::MethodInvocation_strategy)
def test_javadsl::methodinvocation_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=javaDsl::MethodInvocation_strategy)
def test_javadsl::methodinvocation_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=javaDsl::PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_javadsl::predecrementexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::PreDecrementExpression)

@given(instance=javaDsl::PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_javadsl::preincrementexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::PreIncrementExpression)

@given(instance=javaDsl::PostfixExpression_strategy)
@settings(max_examples=50)
def test_javadsl::postfixexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::PostfixExpression)

@given(instance=javaDsl::PostfixExpression_strategy)
def test_javadsl::postfixexpression_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=javaDsl::PostfixExpression_strategy)
def test_javadsl::postfixexpression_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl::PostfixExpression_strategy)
def test_javadsl::postfixexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::PostfixExpression_strategy)
def test_javadsl::postfixexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::Assignment_strategy)
@settings(max_examples=50)
def test_javadsl::assignment_instantiation(instance):
    assert isinstance(instance, javaDsl::Assignment)

@given(instance=javaDsl::Assignment_strategy)
def test_javadsl::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=javaDsl::Assignment_strategy)
def test_javadsl::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=javaDsl::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_javadsl::assignmentexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::AssignmentExpression)

@given(instance=PrimaryNoNewArray_strategy)
@settings(max_examples=50)
def test_primarynonewarray_instantiation(instance):
    assert isinstance(instance, PrimaryNoNewArray)

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=javaDsl::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_javadsl::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::InclusiveOrExpression)

@given(instance=javaDsl::InclusiveOrExpression_strategy)
def test_javadsl::inclusiveorexpression_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=javaDsl::InclusiveOrExpression_strategy)
def test_javadsl::inclusiveorexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl::ForUpdate_strategy)
@settings(max_examples=50)
def test_javadsl::forupdate_instantiation(instance):
    assert isinstance(instance, javaDsl::ForUpdate)

@given(instance=javaDsl::ForInit_strategy)
@settings(max_examples=50)
def test_javadsl::forinit_instantiation(instance):
    assert isinstance(instance, javaDsl::ForInit)

@given(instance=javaDsl::ConstantExpression_strategy)
@settings(max_examples=50)
def test_javadsl::constantexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::ConstantExpression)

@given(instance=BlockStatement_strategy)
@settings(max_examples=50)
def test_blockstatement_instantiation(instance):
    assert isinstance(instance, BlockStatement)

@given(instance=javaDsl::Statement_strategy)
@settings(max_examples=50)
def test_javadsl::statement_instantiation(instance):
    assert isinstance(instance, javaDsl::Statement)

@given(instance=javaDsl::LocalVariableDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::localvariabledeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::LocalVariableDeclaration)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=javaDsl::LabeledStatement_strategy)
@settings(max_examples=50)
def test_javadsl::labeledstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::LabeledStatement)

@given(instance=javaDsl::LabeledStatement_strategy)
def test_javadsl::labeledstatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=javaDsl::LabeledStatement_strategy)
def test_javadsl::labeledstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=javaDsl::DoStatement_strategy)
@settings(max_examples=50)
def test_javadsl::dostatement_instantiation(instance):
    assert isinstance(instance, javaDsl::DoStatement)

@given(instance=javaDsl::DoStatement_strategy)
def test_javadsl::dostatement_condition_type(instance):
    assert isinstance(instance.condition, bool)


@given(instance=javaDsl::DoStatement_strategy)
def test_javadsl::dostatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl::ForStatement_strategy)
@settings(max_examples=50)
def test_javadsl::forstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::ForStatement)

@given(instance=javaDsl::ForStatement_strategy)
def test_javadsl::forstatement_condition_type(instance):
    assert isinstance(instance.condition, bool)


@given(instance=javaDsl::ForStatement_strategy)
def test_javadsl::forstatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl::BreakStatement_strategy)
@settings(max_examples=50)
def test_javadsl::breakstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::BreakStatement)

@given(instance=javaDsl::BreakStatement_strategy)
def test_javadsl::breakstatement_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=javaDsl::BreakStatement_strategy)
def test_javadsl::breakstatement_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl::IfStatement_strategy)
@settings(max_examples=50)
def test_javadsl::ifstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::IfStatement)

@given(instance=javaDsl::IfStatement_strategy)
def test_javadsl::ifstatement_condition_type(instance):
    assert isinstance(instance.condition, bool)


@given(instance=javaDsl::IfStatement_strategy)
def test_javadsl::ifstatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl::ReturnStatement_strategy)
@settings(max_examples=50)
def test_javadsl::returnstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::ReturnStatement)

@given(instance=javaDsl::TryStatement_strategy)
@settings(max_examples=50)
def test_javadsl::trystatement_instantiation(instance):
    assert isinstance(instance, javaDsl::TryStatement)

@given(instance=javaDsl::SwitchStatement_strategy)
@settings(max_examples=50)
def test_javadsl::switchstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::SwitchStatement)

@given(instance=javaDsl::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_javadsl::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::SynchronizedStatement)

@given(instance=javaDsl::ContinueStatement_strategy)
@settings(max_examples=50)
def test_javadsl::continuestatement_instantiation(instance):
    assert isinstance(instance, javaDsl::ContinueStatement)

@given(instance=javaDsl::ContinueStatement_strategy)
def test_javadsl::continuestatement_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=javaDsl::ContinueStatement_strategy)
def test_javadsl::continuestatement_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl::StatementExpression_strategy)
@settings(max_examples=50)
def test_javadsl::statementexpression_instantiation(instance):
    assert isinstance(instance, javaDsl::StatementExpression)

@given(instance=javaDsl::ThrowsStatement_strategy)
@settings(max_examples=50)
def test_javadsl::throwsstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::ThrowsStatement)

@given(instance=javaDsl::WhileStatement_strategy)
@settings(max_examples=50)
def test_javadsl::whilestatement_instantiation(instance):
    assert isinstance(instance, javaDsl::WhileStatement)

@given(instance=javaDsl::WhileStatement_strategy)
def test_javadsl::whilestatement_condition_type(instance):
    assert isinstance(instance.condition, bool)


@given(instance=javaDsl::WhileStatement_strategy)
def test_javadsl::whilestatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=VariableInitializer_strategy)
@settings(max_examples=50)
def test_variableinitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)

@given(instance=javaDsl::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_javadsl::arrayinitializer_instantiation(instance):
    assert isinstance(instance, javaDsl::ArrayInitializer)

@given(instance=InterfaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_interfacememberdeclaration_instantiation(instance):
    assert isinstance(instance, InterfaceMemberDeclaration)

@given(instance=javaDsl::AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::AbstractMethodDeclaration)

@given(instance=javaDsl::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::constantdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::ConstantDeclaration)

@given(instance=javaDsl::InterfaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::interfacememberdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::InterfaceMemberDeclaration)

@given(instance=javaDsl::InterfaceMemberDeclaration_strategy)
def test_javadsl::interfacememberdeclaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=javaDsl::InterfaceMemberDeclaration_strategy)
def test_javadsl::interfacememberdeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl::InterfaceBody_strategy)
@settings(max_examples=50)
def test_javadsl::interfacebody_instantiation(instance):
    assert isinstance(instance, javaDsl::InterfaceBody)

@given(instance=javaDsl::ExtendsInterfaces_strategy)
@settings(max_examples=50)
def test_javadsl::extendsinterfaces_instantiation(instance):
    assert isinstance(instance, javaDsl::ExtendsInterfaces)

@given(instance=javaDsl::ExtendsInterfaces_strategy)
def test_javadsl::extendsinterfaces_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=javaDsl::ExtendsInterfaces_strategy)
def test_javadsl::extendsinterfaces_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl::ExtendsInterfaces_strategy)
def test_javadsl::extendsinterfaces_interfaces_type(instance):
    assert isinstance(instance.interfaces, str)


@given(instance=javaDsl::ExtendsInterfaces_strategy)
def test_javadsl::extendsinterfaces_interfaces_setter(instance):
    original = instance.interfaces
    instance.interfaces = original
    assert instance.interfaces == original

@given(instance=javaDsl::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::InterfaceDeclaration)

@given(instance=javaDsl::InterfaceDeclaration_strategy)
def test_javadsl::interfacedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaDsl::InterfaceDeclaration_strategy)
def test_javadsl::interfacedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl::InterfaceDeclaration_strategy)
def test_javadsl::interfacedeclaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=javaDsl::InterfaceDeclaration_strategy)
def test_javadsl::interfacedeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl::MethodDeclarator_strategy)
@settings(max_examples=50)
def test_javadsl::methoddeclarator_instantiation(instance):
    assert isinstance(instance, javaDsl::MethodDeclarator)

@given(instance=javaDsl::MethodDeclarator_strategy)
def test_javadsl::methoddeclarator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaDsl::MethodDeclarator_strategy)
def test_javadsl::methoddeclarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl::ResultType_strategy)
@settings(max_examples=50)
def test_javadsl::resulttype_instantiation(instance):
    assert isinstance(instance, javaDsl::ResultType)

@given(instance=javaDsl::MethodHeader_strategy)
@settings(max_examples=50)
def test_javadsl::methodheader_instantiation(instance):
    assert isinstance(instance, javaDsl::MethodHeader)

@given(instance=javaDsl::MethodHeader_strategy)
def test_javadsl::methodheader_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=javaDsl::MethodHeader_strategy)
def test_javadsl::methodheader_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl::VariableDeclarator_strategy)
@settings(max_examples=50)
def test_javadsl::variabledeclarator_instantiation(instance):
    assert isinstance(instance, javaDsl::VariableDeclarator)

@given(instance=javaDsl::VariableDeclarator_strategy)
def test_javadsl::variabledeclarator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaDsl::VariableDeclarator_strategy)
def test_javadsl::variabledeclarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl::ArgumentList_strategy)
@settings(max_examples=50)
def test_javadsl::argumentlist_instantiation(instance):
    assert isinstance(instance, javaDsl::ArgumentList)

@given(instance=javaDsl::BlockStatement_strategy)
@settings(max_examples=50)
def test_javadsl::blockstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::BlockStatement)

@given(instance=javaDsl::ExplicitConstructorInvocation_strategy)
@settings(max_examples=50)
def test_javadsl::explicitconstructorinvocation_instantiation(instance):
    assert isinstance(instance, javaDsl::ExplicitConstructorInvocation)

@given(instance=javaDsl::ExplicitConstructorInvocation_strategy)
def test_javadsl::explicitconstructorinvocation_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=javaDsl::ExplicitConstructorInvocation_strategy)
def test_javadsl::explicitconstructorinvocation_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl::Type_strategy)
@settings(max_examples=50)
def test_javadsl::type_instantiation(instance):
    assert isinstance(instance, javaDsl::Type)

@given(instance=javaDsl::Type_strategy)
def test_javadsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaDsl::Type_strategy)
def test_javadsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl::FormalParameter_strategy)
@settings(max_examples=50)
def test_javadsl::formalparameter_instantiation(instance):
    assert isinstance(instance, javaDsl::FormalParameter)

@given(instance=javaDsl::FormalParameter_strategy)
def test_javadsl::formalparameter_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=javaDsl::FormalParameter_strategy)
def test_javadsl::formalparameter_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=javaDsl::ConstructorBody_strategy)
@settings(max_examples=50)
def test_javadsl::constructorbody_instantiation(instance):
    assert isinstance(instance, javaDsl::ConstructorBody)

@given(instance=javaDsl::Exceptions_strategy)
@settings(max_examples=50)
def test_javadsl::exceptions_instantiation(instance):
    assert isinstance(instance, javaDsl::Exceptions)

@given(instance=javaDsl::Exceptions_strategy)
def test_javadsl::exceptions_exceptions_type(instance):
    assert isinstance(instance.exceptions, str)


@given(instance=javaDsl::Exceptions_strategy)
def test_javadsl::exceptions_exceptions_setter(instance):
    original = instance.exceptions
    instance.exceptions = original
    assert instance.exceptions == original

@given(instance=javaDsl::ConstructorDeclarator_strategy)
@settings(max_examples=50)
def test_javadsl::constructordeclarator_instantiation(instance):
    assert isinstance(instance, javaDsl::ConstructorDeclarator)

@given(instance=javaDsl::ConstructorDeclarator_strategy)
def test_javadsl::constructordeclarator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaDsl::ConstructorDeclarator_strategy)
def test_javadsl::constructordeclarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl::Block_strategy)
@settings(max_examples=50)
def test_javadsl::block_instantiation(instance):
    assert isinstance(instance, javaDsl::Block)

@given(instance=ClassBodyDeclaration_strategy)
@settings(max_examples=50)
def test_classbodydeclaration_instantiation(instance):
    assert isinstance(instance, ClassBodyDeclaration)

@given(instance=javaDsl::ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::constructordeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::ConstructorDeclaration)

@given(instance=javaDsl::ConstructorDeclaration_strategy)
def test_javadsl::constructordeclaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=javaDsl::ConstructorDeclaration_strategy)
def test_javadsl::constructordeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl::StaticInitializer_strategy)
@settings(max_examples=50)
def test_javadsl::staticinitializer_instantiation(instance):
    assert isinstance(instance, javaDsl::StaticInitializer)

@given(instance=javaDsl::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::methoddeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::MethodDeclaration)

@given(instance=javaDsl::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::fielddeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::FieldDeclaration)

@given(instance=javaDsl::FieldDeclaration_strategy)
def test_javadsl::fielddeclaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=javaDsl::FieldDeclaration_strategy)
def test_javadsl::fielddeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl::ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::ClassMemberDeclaration)

@given(instance=javaDsl::Expression_strategy)
@settings(max_examples=50)
def test_javadsl::expression_instantiation(instance):
    assert isinstance(instance, javaDsl::Expression)

@given(instance=javaDsl::VariableInitializer_strategy)
@settings(max_examples=50)
def test_javadsl::variableinitializer_instantiation(instance):
    assert isinstance(instance, javaDsl::VariableInitializer)

@given(instance=javaDsl::ClassBody_strategy)
@settings(max_examples=50)
def test_javadsl::classbody_instantiation(instance):
    assert isinstance(instance, javaDsl::ClassBody)

@given(instance=javaDsl::Interfaces_strategy)
@settings(max_examples=50)
def test_javadsl::interfaces_instantiation(instance):
    assert isinstance(instance, javaDsl::Interfaces)

@given(instance=javaDsl::Interfaces_strategy)
def test_javadsl::interfaces_interfaces_type(instance):
    assert isinstance(instance.interfaces, str)


@given(instance=javaDsl::Interfaces_strategy)
def test_javadsl::interfaces_interfaces_setter(instance):
    original = instance.interfaces
    instance.interfaces = original
    assert instance.interfaces == original

@given(instance=javaDsl::Interfaces_strategy)
def test_javadsl::interfaces_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=javaDsl::Interfaces_strategy)
def test_javadsl::interfaces_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::classdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::ClassDeclaration)

@given(instance=javaDsl::ClassDeclaration_strategy)
def test_javadsl::classdeclaration_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=javaDsl::ClassDeclaration_strategy)
def test_javadsl::classdeclaration_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=javaDsl::ClassDeclaration_strategy)
def test_javadsl::classdeclaration_extend_type(instance):
    assert isinstance(instance.extend, str)


@given(instance=javaDsl::ClassDeclaration_strategy)
def test_javadsl::classdeclaration_extend_setter(instance):
    original = instance.extend
    instance.extend = original
    assert instance.extend == original

@given(instance=javaDsl::ClassDeclaration_strategy)
def test_javadsl::classdeclaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=javaDsl::ClassDeclaration_strategy)
def test_javadsl::classdeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl::EObject_strategy)
@settings(max_examples=50)
def test_javadsl::eobject_instantiation(instance):
    assert isinstance(instance, javaDsl::EObject)

@given(instance=javaDsl::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::typedeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::TypeDeclaration)

@given(instance=javaDsl::TypeDeclaration_strategy)
def test_javadsl::typedeclaration_doc_type(instance):
    assert isinstance(instance.doc, str)


@given(instance=javaDsl::TypeDeclaration_strategy)
def test_javadsl::typedeclaration_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=javaDsl::ImportStatement_strategy)
@settings(max_examples=50)
def test_javadsl::importstatement_instantiation(instance):
    assert isinstance(instance, javaDsl::ImportStatement)

@given(instance=javaDsl::ImportStatement_strategy)
def test_javadsl::importstatement_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=javaDsl::ImportStatement_strategy)
def test_javadsl::importstatement_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=javaDsl::ImportStatement_strategy)
def test_javadsl::importstatement_object_type(instance):
    assert isinstance(instance.object, str)


@given(instance=javaDsl::ImportStatement_strategy)
def test_javadsl::importstatement_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=javaDsl::PackageStatement_strategy)
@settings(max_examples=50)
def test_javadsl::packagestatement_instantiation(instance):
    assert isinstance(instance, javaDsl::PackageStatement)

@given(instance=javaDsl::PackageStatement_strategy)
def test_javadsl::packagestatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaDsl::PackageStatement_strategy)
def test_javadsl::packagestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl::CompilationUnit_strategy)
@settings(max_examples=50)
def test_javadsl::compilationunit_instantiation(instance):
    assert isinstance(instance, javaDsl::CompilationUnit)

@given(instance=javaDsl::Head_strategy)
@settings(max_examples=50)
def test_javadsl::head_instantiation(instance):
    assert isinstance(instance, javaDsl::Head)

@given(instance=javaDsl::ClassBodyDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl::classbodydeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl::ClassBodyDeclaration)
