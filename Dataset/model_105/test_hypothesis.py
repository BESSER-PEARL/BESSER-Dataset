import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Annotation,
    DOM::NormalAnnotation,
    DOM::SingleMemberAnnotation,
    DOM::MarkerAnnotation,
    Name,
    DOM::QualifiedName,
    Type,
    DOM::PrimitiveType,
    DOM::ParameterizedType,
    DOM::SimpleType,
    DOM::QualifiedType,
    VariableDeclaration,
    DOM::WildcardType,
    Statement,
    DOM::WhileStatement,
    DOM::BreakStatement,
    DOM::SynchronizedStatement,
    DOM::SwitchStatement,
    DOM::SwitchCase,
    DOM::EnhancedForStatement,
    DOM::TryStatement,
    DOM::ThrowStatement,
    DOM::ForStatement,
    DOM::SuperConstructorInvocation,
    DOM::EmptyStatement,
    DOM::ExpressionStatement,
    DOM::ConstructorInvocation,
    DOM::ReturnStatement,
    DOM::VariableDeclarationStatement,
    DOM::TypeDeclarationStatement,
    DOM::LabeledStatement,
    DOM::IfStatement,
    DOM::AssertStatement,
    DOM::DoStatement,
    DOM::ContinueStatement,
    DOM::ArrayType,
    Expression,
    DOM::InstanceofExpression,
    DOM::ArrayCreation,
    DOM::PrefixExpression,
    DOM::MethodInvocation,
    DOM::PostfixExpression,
    DOM::InfixExpression,
    DOM::ArrayAccess,
    DOM::FieldAccess,
    DOM::VariableDeclarationExpression,
    DOM::NullLiteral,
    DOM::SuperFieldAccess,
    DOM::BooleanLiteral,
    DOM::CharacterLiteral,
    DOM::TypeLiteral,
    DOM::ConditionalExpression,
    DOM::StringLiteral,
    DOM::ClassInstanceCreation,
    DOM::ArrayInitializer,
    DOM::CastExpression,
    DOM::ThisExpression,
    DOM::NumberLiteral,
    DOM::Assignment,
    DOM::SuperMethodInvocation,
    DOM::ParenthesizedExpression,
    Comment,
    DOM::LineComment,
    DOM::BlockComment,
    AbstractTypeDeclaration,
    DOM::AnnotationTypeDeclaration,
    DOM::IMethod,
    DOM::VariableDeclarationFragment,
    DOM::TypeDeclaration,
    DOM::EnumDeclaration,
    BodyDeclaration,
    DOM::MethodDeclaration,
    DOM::Initializer,
    DOM::FieldDeclaration,
    DOM::IPackageFragment,
    DOM::EnumConstantDeclaration,
    DOM::AnnotationTypeMemberDeclaration,
    ExtendedModifier,
    DOM::Annotation,
    DOM::SimpleName,
    DOM::Name,
    DOM::AbstractTypeDeclaration,
    DOM::SingleVariableDeclaration,
    DOM::Block,
    DOM::Javadoc,
    DOM::ExtendedModifier,
    DOM::IType,
    ASTNode,
    DOM::Modifier,
    DOM::CatchClause,
    DOM::CompilationUnit,
    DOM::PackageDeclaration,
    DOM::MemberRef,
    DOM::MethodRef,
    DOM::Statement,
    DOM::VariableDeclaration,
    DOM::TextElement,
    DOM::MemberValuePair,
    DOM::TagElement,
    DOM::Comment,
    DOM::MethodRefParameter,
    DOM::ImportDeclaration,
    DOM::BodyDeclaration,
    DOM::Expression,
    DOM::Type,
    DOM::TypeParameter,
    DOM::AnonymousClassDeclaration,
    DOM::ASTNode,
    DOM::AST,
    PostfixExpressionOperatorKind,
    InfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
    AssignmentOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::normalannotation_is_not_abstract():
    assert not inspect.isabstract(DOM::NormalAnnotation)


def test_dom::normalannotation_constructor_exists():
    assert callable(DOM::NormalAnnotation.__init__)


def test_dom::normalannotation_constructor_args():
    sig = inspect.signature(DOM::NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(DOM::SingleMemberAnnotation)


def test_dom::singlememberannotation_constructor_exists():
    assert callable(DOM::SingleMemberAnnotation.__init__)


def test_dom::singlememberannotation_constructor_args():
    sig = inspect.signature(DOM::SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::markerannotation_is_not_abstract():
    assert not inspect.isabstract(DOM::MarkerAnnotation)


def test_dom::markerannotation_constructor_exists():
    assert callable(DOM::MarkerAnnotation.__init__)


def test_dom::markerannotation_constructor_args():
    sig = inspect.signature(DOM::MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_dom::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(DOM::QualifiedName)


def test_dom::qualifiedname_constructor_exists():
    assert callable(DOM::QualifiedName.__init__)


def test_dom::qualifiedname_constructor_args():
    sig = inspect.signature(DOM::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dom::primitivetype_is_not_abstract():
    assert not inspect.isabstract(DOM::PrimitiveType)


def test_dom::primitivetype_constructor_exists():
    assert callable(DOM::PrimitiveType.__init__)


def test_dom::primitivetype_constructor_args():
    sig = inspect.signature(DOM::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_dom::primitivetype_has_code():
    assert hasattr(DOM::PrimitiveType, "code")
    descriptor = None
    for klass in DOM::PrimitiveType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_dom::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(DOM::ParameterizedType)


def test_dom::parameterizedtype_constructor_exists():
    assert callable(DOM::ParameterizedType.__init__)


def test_dom::parameterizedtype_constructor_args():
    sig = inspect.signature(DOM::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_dom::simpletype_is_not_abstract():
    assert not inspect.isabstract(DOM::SimpleType)


def test_dom::simpletype_constructor_exists():
    assert callable(DOM::SimpleType.__init__)


def test_dom::simpletype_constructor_args():
    sig = inspect.signature(DOM::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_dom::qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(DOM::QualifiedType)


def test_dom::qualifiedtype_constructor_exists():
    assert callable(DOM::QualifiedType.__init__)


def test_dom::qualifiedtype_constructor_args():
    sig = inspect.signature(DOM::QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(DOM::WildcardType)


def test_dom::wildcardtype_constructor_exists():
    assert callable(DOM::WildcardType.__init__)


def test_dom::wildcardtype_constructor_args():
    sig = inspect.signature(DOM::WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_dom::wildcardtype_has_upperBound():
    assert hasattr(DOM::WildcardType, "upperBound")
    descriptor = None
    for klass in DOM::WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom::whilestatement_is_not_abstract():
    assert not inspect.isabstract(DOM::WhileStatement)


def test_dom::whilestatement_constructor_exists():
    assert callable(DOM::WhileStatement.__init__)


def test_dom::whilestatement_constructor_args():
    sig = inspect.signature(DOM::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::breakstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::BreakStatement)


def test_dom::breakstatement_constructor_exists():
    assert callable(DOM::BreakStatement.__init__)


def test_dom::breakstatement_constructor_args():
    sig = inspect.signature(DOM::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::SynchronizedStatement)


def test_dom::synchronizedstatement_constructor_exists():
    assert callable(DOM::SynchronizedStatement.__init__)


def test_dom::synchronizedstatement_constructor_args():
    sig = inspect.signature(DOM::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::switchstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::SwitchStatement)


def test_dom::switchstatement_constructor_exists():
    assert callable(DOM::SwitchStatement.__init__)


def test_dom::switchstatement_constructor_args():
    sig = inspect.signature(DOM::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::switchcase_is_not_abstract():
    assert not inspect.isabstract(DOM::SwitchCase)


def test_dom::switchcase_constructor_exists():
    assert callable(DOM::SwitchCase.__init__)


def test_dom::switchcase_constructor_args():
    sig = inspect.signature(DOM::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_dom::switchcase_has_default():
    assert hasattr(DOM::SwitchCase, "default")
    descriptor = None
    for klass in DOM::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_dom::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::EnhancedForStatement)


def test_dom::enhancedforstatement_constructor_exists():
    assert callable(DOM::EnhancedForStatement.__init__)


def test_dom::enhancedforstatement_constructor_args():
    sig = inspect.signature(DOM::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::trystatement_is_not_abstract():
    assert not inspect.isabstract(DOM::TryStatement)


def test_dom::trystatement_constructor_exists():
    assert callable(DOM::TryStatement.__init__)


def test_dom::trystatement_constructor_args():
    sig = inspect.signature(DOM::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::throwstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ThrowStatement)


def test_dom::throwstatement_constructor_exists():
    assert callable(DOM::ThrowStatement.__init__)


def test_dom::throwstatement_constructor_args():
    sig = inspect.signature(DOM::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::forstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ForStatement)


def test_dom::forstatement_constructor_exists():
    assert callable(DOM::ForStatement.__init__)


def test_dom::forstatement_constructor_args():
    sig = inspect.signature(DOM::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::SuperConstructorInvocation)


def test_dom::superconstructorinvocation_constructor_exists():
    assert callable(DOM::SuperConstructorInvocation.__init__)


def test_dom::superconstructorinvocation_constructor_args():
    sig = inspect.signature(DOM::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::emptystatement_is_not_abstract():
    assert not inspect.isabstract(DOM::EmptyStatement)


def test_dom::emptystatement_constructor_exists():
    assert callable(DOM::EmptyStatement.__init__)


def test_dom::emptystatement_constructor_args():
    sig = inspect.signature(DOM::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ExpressionStatement)


def test_dom::expressionstatement_constructor_exists():
    assert callable(DOM::ExpressionStatement.__init__)


def test_dom::expressionstatement_constructor_args():
    sig = inspect.signature(DOM::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::ConstructorInvocation)


def test_dom::constructorinvocation_constructor_exists():
    assert callable(DOM::ConstructorInvocation.__init__)


def test_dom::constructorinvocation_constructor_args():
    sig = inspect.signature(DOM::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::returnstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ReturnStatement)


def test_dom::returnstatement_constructor_exists():
    assert callable(DOM::ReturnStatement.__init__)


def test_dom::returnstatement_constructor_args():
    sig = inspect.signature(DOM::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclarationStatement)


def test_dom::variabledeclarationstatement_constructor_exists():
    assert callable(DOM::VariableDeclarationStatement.__init__)


def test_dom::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(DOM::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeDeclarationStatement)


def test_dom::typedeclarationstatement_constructor_exists():
    assert callable(DOM::TypeDeclarationStatement.__init__)


def test_dom::typedeclarationstatement_constructor_args():
    sig = inspect.signature(DOM::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::LabeledStatement)


def test_dom::labeledstatement_constructor_exists():
    assert callable(DOM::LabeledStatement.__init__)


def test_dom::labeledstatement_constructor_args():
    sig = inspect.signature(DOM::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::ifstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::IfStatement)


def test_dom::ifstatement_constructor_exists():
    assert callable(DOM::IfStatement.__init__)


def test_dom::ifstatement_constructor_args():
    sig = inspect.signature(DOM::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::assertstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::AssertStatement)


def test_dom::assertstatement_constructor_exists():
    assert callable(DOM::AssertStatement.__init__)


def test_dom::assertstatement_constructor_args():
    sig = inspect.signature(DOM::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::dostatement_is_not_abstract():
    assert not inspect.isabstract(DOM::DoStatement)


def test_dom::dostatement_constructor_exists():
    assert callable(DOM::DoStatement.__init__)


def test_dom::dostatement_constructor_args():
    sig = inspect.signature(DOM::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::continuestatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ContinueStatement)


def test_dom::continuestatement_constructor_exists():
    assert callable(DOM::ContinueStatement.__init__)


def test_dom::continuestatement_constructor_args():
    sig = inspect.signature(DOM::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::arraytype_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayType)


def test_dom::arraytype_constructor_exists():
    assert callable(DOM::ArrayType.__init__)


def test_dom::arraytype_constructor_args():
    sig = inspect.signature(DOM::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_dom::arraytype_has_dimensions():
    assert hasattr(DOM::ArrayType, "dimensions")
    descriptor = None
    for klass in DOM::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::InstanceofExpression)


def test_dom::instanceofexpression_constructor_exists():
    assert callable(DOM::InstanceofExpression.__init__)


def test_dom::instanceofexpression_constructor_args():
    sig = inspect.signature(DOM::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::arraycreation_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayCreation)


def test_dom::arraycreation_constructor_exists():
    assert callable(DOM::ArrayCreation.__init__)


def test_dom::arraycreation_constructor_args():
    sig = inspect.signature(DOM::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_dom::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::PrefixExpression)


def test_dom::prefixexpression_constructor_exists():
    assert callable(DOM::PrefixExpression.__init__)


def test_dom::prefixexpression_constructor_args():
    sig = inspect.signature(DOM::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::prefixexpression_has_operator():
    assert hasattr(DOM::PrefixExpression, "operator")
    descriptor = None
    for klass in DOM::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodInvocation)


def test_dom::methodinvocation_constructor_exists():
    assert callable(DOM::MethodInvocation.__init__)


def test_dom::methodinvocation_constructor_args():
    sig = inspect.signature(DOM::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::PostfixExpression)


def test_dom::postfixexpression_constructor_exists():
    assert callable(DOM::PostfixExpression.__init__)


def test_dom::postfixexpression_constructor_args():
    sig = inspect.signature(DOM::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::postfixexpression_has_operator():
    assert hasattr(DOM::PostfixExpression, "operator")
    descriptor = None
    for klass in DOM::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::infixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::InfixExpression)


def test_dom::infixexpression_constructor_exists():
    assert callable(DOM::InfixExpression.__init__)


def test_dom::infixexpression_constructor_args():
    sig = inspect.signature(DOM::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::infixexpression_has_operator():
    assert hasattr(DOM::InfixExpression, "operator")
    descriptor = None
    for klass in DOM::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayAccess)


def test_dom::arrayaccess_constructor_exists():
    assert callable(DOM::ArrayAccess.__init__)


def test_dom::arrayaccess_constructor_args():
    sig = inspect.signature(DOM::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM::FieldAccess)


def test_dom::fieldaccess_constructor_exists():
    assert callable(DOM::FieldAccess.__init__)


def test_dom::fieldaccess_constructor_args():
    sig = inspect.signature(DOM::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclarationExpression)


def test_dom::variabledeclarationexpression_constructor_exists():
    assert callable(DOM::VariableDeclarationExpression.__init__)


def test_dom::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(DOM::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::nullliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::NullLiteral)


def test_dom::nullliteral_constructor_exists():
    assert callable(DOM::NullLiteral.__init__)


def test_dom::nullliteral_constructor_args():
    sig = inspect.signature(DOM::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dom::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM::SuperFieldAccess)


def test_dom::superfieldaccess_constructor_exists():
    assert callable(DOM::SuperFieldAccess.__init__)


def test_dom::superfieldaccess_constructor_args():
    sig = inspect.signature(DOM::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::BooleanLiteral)


def test_dom::booleanliteral_constructor_exists():
    assert callable(DOM::BooleanLiteral.__init__)


def test_dom::booleanliteral_constructor_args():
    sig = inspect.signature(DOM::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_dom::booleanliteral_has_booleanValue():
    assert hasattr(DOM::BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in DOM::BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_dom::characterliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::CharacterLiteral)


def test_dom::characterliteral_constructor_exists():
    assert callable(DOM::CharacterLiteral.__init__)


def test_dom::characterliteral_constructor_args():
    sig = inspect.signature(DOM::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "charValue" in params, "Missing parameter 'charValue'"

def test_dom::characterliteral_has_escapedValue():
    assert hasattr(DOM::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in DOM::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_dom::characterliteral_has_charValue():
    assert hasattr(DOM::CharacterLiteral, "charValue")
    descriptor = None
    for klass in DOM::CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)



def test_dom::typeliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeLiteral)


def test_dom::typeliteral_constructor_exists():
    assert callable(DOM::TypeLiteral.__init__)


def test_dom::typeliteral_constructor_args():
    sig = inspect.signature(DOM::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dom::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::ConditionalExpression)


def test_dom::conditionalexpression_constructor_exists():
    assert callable(DOM::ConditionalExpression.__init__)


def test_dom::conditionalexpression_constructor_args():
    sig = inspect.signature(DOM::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::stringliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::StringLiteral)


def test_dom::stringliteral_constructor_exists():
    assert callable(DOM::StringLiteral.__init__)


def test_dom::stringliteral_constructor_args():
    sig = inspect.signature(DOM::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_dom::stringliteral_has_escapedValue():
    assert hasattr(DOM::StringLiteral, "escapedValue")
    descriptor = None
    for klass in DOM::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_dom::stringliteral_has_literalValue():
    assert hasattr(DOM::StringLiteral, "literalValue")
    descriptor = None
    for klass in DOM::StringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_dom::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(DOM::ClassInstanceCreation)


def test_dom::classinstancecreation_constructor_exists():
    assert callable(DOM::ClassInstanceCreation.__init__)


def test_dom::classinstancecreation_constructor_args():
    sig = inspect.signature(DOM::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_dom::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayInitializer)


def test_dom::arrayinitializer_constructor_exists():
    assert callable(DOM::ArrayInitializer.__init__)


def test_dom::arrayinitializer_constructor_args():
    sig = inspect.signature(DOM::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dom::castexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::CastExpression)


def test_dom::castexpression_constructor_exists():
    assert callable(DOM::CastExpression.__init__)


def test_dom::castexpression_constructor_args():
    sig = inspect.signature(DOM::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::thisexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::ThisExpression)


def test_dom::thisexpression_constructor_exists():
    assert callable(DOM::ThisExpression.__init__)


def test_dom::thisexpression_constructor_args():
    sig = inspect.signature(DOM::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::numberliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::NumberLiteral)


def test_dom::numberliteral_constructor_exists():
    assert callable(DOM::NumberLiteral.__init__)


def test_dom::numberliteral_constructor_args():
    sig = inspect.signature(DOM::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_dom::numberliteral_has_token():
    assert hasattr(DOM::NumberLiteral, "token")
    descriptor = None
    for klass in DOM::NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_dom::assignment_is_not_abstract():
    assert not inspect.isabstract(DOM::Assignment)


def test_dom::assignment_constructor_exists():
    assert callable(DOM::Assignment.__init__)


def test_dom::assignment_constructor_args():
    sig = inspect.signature(DOM::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::assignment_has_operator():
    assert hasattr(DOM::Assignment, "operator")
    descriptor = None
    for klass in DOM::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::SuperMethodInvocation)


def test_dom::supermethodinvocation_constructor_exists():
    assert callable(DOM::SuperMethodInvocation.__init__)


def test_dom::supermethodinvocation_constructor_args():
    sig = inspect.signature(DOM::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::ParenthesizedExpression)


def test_dom::parenthesizedexpression_constructor_exists():
    assert callable(DOM::ParenthesizedExpression.__init__)


def test_dom::parenthesizedexpression_constructor_args():
    sig = inspect.signature(DOM::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_dom::linecomment_is_not_abstract():
    assert not inspect.isabstract(DOM::LineComment)


def test_dom::linecomment_constructor_exists():
    assert callable(DOM::LineComment.__init__)


def test_dom::linecomment_constructor_args():
    sig = inspect.signature(DOM::LineComment.__init__)
    params = list(sig.parameters.keys())



def test_dom::blockcomment_is_not_abstract():
    assert not inspect.isabstract(DOM::BlockComment)


def test_dom::blockcomment_constructor_exists():
    assert callable(DOM::BlockComment.__init__)


def test_dom::blockcomment_constructor_args():
    sig = inspect.signature(DOM::BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AnnotationTypeDeclaration)


def test_dom::annotationtypedeclaration_constructor_exists():
    assert callable(DOM::AnnotationTypeDeclaration.__init__)


def test_dom::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(DOM::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::imethod_is_not_abstract():
    assert not inspect.isabstract(DOM::IMethod)


def test_dom::imethod_constructor_exists():
    assert callable(DOM::IMethod.__init__)


def test_dom::imethod_constructor_args():
    sig = inspect.signature(DOM::IMethod.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclarationFragment)


def test_dom::variabledeclarationfragment_constructor_exists():
    assert callable(DOM::VariableDeclarationFragment.__init__)


def test_dom::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(DOM::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_dom::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeDeclaration)


def test_dom::typedeclaration_constructor_exists():
    assert callable(DOM::TypeDeclaration.__init__)


def test_dom::typedeclaration_constructor_args():
    sig = inspect.signature(DOM::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_dom::typedeclaration_has_interface():
    assert hasattr(DOM::TypeDeclaration, "interface")
    descriptor = None
    for klass in DOM::TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_dom::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::EnumDeclaration)


def test_dom::enumdeclaration_constructor_exists():
    assert callable(DOM::EnumDeclaration.__init__)


def test_dom::enumdeclaration_constructor_args():
    sig = inspect.signature(DOM::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodDeclaration)


def test_dom::methoddeclaration_constructor_exists():
    assert callable(DOM::MethodDeclaration.__init__)


def test_dom::methoddeclaration_constructor_args():
    sig = inspect.signature(DOM::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_dom::methoddeclaration_has_constructor():
    assert hasattr(DOM::MethodDeclaration, "constructor")
    descriptor = None
    for klass in DOM::MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_dom::methoddeclaration_has_varargs():
    assert hasattr(DOM::MethodDeclaration, "varargs")
    descriptor = None
    for klass in DOM::MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_dom::methoddeclaration_has_extraDimensions():
    assert hasattr(DOM::MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in DOM::MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_dom::initializer_is_not_abstract():
    assert not inspect.isabstract(DOM::Initializer)


def test_dom::initializer_constructor_exists():
    assert callable(DOM::Initializer.__init__)


def test_dom::initializer_constructor_args():
    sig = inspect.signature(DOM::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_dom::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::FieldDeclaration)


def test_dom::fielddeclaration_constructor_exists():
    assert callable(DOM::FieldDeclaration.__init__)


def test_dom::fielddeclaration_constructor_args():
    sig = inspect.signature(DOM::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(DOM::IPackageFragment)


def test_dom::ipackagefragment_constructor_exists():
    assert callable(DOM::IPackageFragment.__init__)


def test_dom::ipackagefragment_constructor_args():
    sig = inspect.signature(DOM::IPackageFragment.__init__)
    params = list(sig.parameters.keys())



def test_dom::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::EnumConstantDeclaration)


def test_dom::enumconstantdeclaration_constructor_exists():
    assert callable(DOM::EnumConstantDeclaration.__init__)


def test_dom::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(DOM::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AnnotationTypeMemberDeclaration)


def test_dom::annotationtypememberdeclaration_constructor_exists():
    assert callable(DOM::AnnotationTypeMemberDeclaration.__init__)


def test_dom::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(DOM::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_dom::annotation_is_not_abstract():
    assert not inspect.isabstract(DOM::Annotation)


def test_dom::annotation_constructor_exists():
    assert callable(DOM::Annotation.__init__)


def test_dom::annotation_constructor_args():
    sig = inspect.signature(DOM::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::simplename_is_not_abstract():
    assert not inspect.isabstract(DOM::SimpleName)


def test_dom::simplename_constructor_exists():
    assert callable(DOM::SimpleName.__init__)


def test_dom::simplename_constructor_args():
    sig = inspect.signature(DOM::SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_dom::simplename_has_identifier():
    assert hasattr(DOM::SimpleName, "identifier")
    descriptor = None
    for klass in DOM::SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_dom::simplename_has_declaration():
    assert hasattr(DOM::SimpleName, "declaration")
    descriptor = None
    for klass in DOM::SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_dom::name_is_not_abstract():
    assert not inspect.isabstract(DOM::Name)


def test_dom::name_constructor_exists():
    assert callable(DOM::Name.__init__)


def test_dom::name_constructor_args():
    sig = inspect.signature(DOM::Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_dom::name_has_fullyQualifiedName():
    assert hasattr(DOM::Name, "fullyQualifiedName")
    descriptor = None
    for klass in DOM::Name.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_dom::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AbstractTypeDeclaration)


def test_dom::abstracttypedeclaration_constructor_exists():
    assert callable(DOM::AbstractTypeDeclaration.__init__)


def test_dom::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(DOM::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"

def test_dom::abstracttypedeclaration_has_localTypeDeclaration():
    assert hasattr(DOM::AbstractTypeDeclaration, "localTypeDeclaration")
    descriptor = None
    for klass in DOM::AbstractTypeDeclaration.__mro__:
        if "localTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["localTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_dom::abstracttypedeclaration_has_packageMemberTypeDeclaration():
    assert hasattr(DOM::AbstractTypeDeclaration, "packageMemberTypeDeclaration")
    descriptor = None
    for klass in DOM::AbstractTypeDeclaration.__mro__:
        if "packageMemberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["packageMemberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_dom::abstracttypedeclaration_has_memberTypeDeclaration():
    assert hasattr(DOM::AbstractTypeDeclaration, "memberTypeDeclaration")
    descriptor = None
    for klass in DOM::AbstractTypeDeclaration.__mro__:
        if "memberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["memberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_dom::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::SingleVariableDeclaration)


def test_dom::singlevariabledeclaration_constructor_exists():
    assert callable(DOM::SingleVariableDeclaration.__init__)


def test_dom::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(DOM::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_dom::singlevariabledeclaration_has_varargs():
    assert hasattr(DOM::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in DOM::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_dom::block_is_not_abstract():
    assert not inspect.isabstract(DOM::Block)


def test_dom::block_constructor_exists():
    assert callable(DOM::Block.__init__)


def test_dom::block_constructor_args():
    sig = inspect.signature(DOM::Block.__init__)
    params = list(sig.parameters.keys())



def test_dom::javadoc_is_not_abstract():
    assert not inspect.isabstract(DOM::Javadoc)


def test_dom::javadoc_constructor_exists():
    assert callable(DOM::Javadoc.__init__)


def test_dom::javadoc_constructor_args():
    sig = inspect.signature(DOM::Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_dom::extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(DOM::ExtendedModifier)


def test_dom::extendedmodifier_constructor_exists():
    assert callable(DOM::ExtendedModifier.__init__)


def test_dom::extendedmodifier_constructor_args():
    sig = inspect.signature(DOM::ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_dom::itype_is_not_abstract():
    assert not inspect.isabstract(DOM::IType)


def test_dom::itype_constructor_exists():
    assert callable(DOM::IType.__init__)


def test_dom::itype_constructor_args():
    sig = inspect.signature(DOM::IType.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_dom::modifier_is_not_abstract():
    assert not inspect.isabstract(DOM::Modifier)


def test_dom::modifier_constructor_exists():
    assert callable(DOM::Modifier.__init__)


def test_dom::modifier_constructor_args():
    sig = inspect.signature(DOM::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "none" in params, "Missing parameter 'none'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "static" in params, "Missing parameter 'static'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "private" in params, "Missing parameter 'private'"
    assert "public" in params, "Missing parameter 'public'"
    assert "final" in params, "Missing parameter 'final'"
    assert "native" in params, "Missing parameter 'native'"

def test_dom::modifier_has_transient():
    assert hasattr(DOM::Modifier, "transient")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_abstract():
    assert hasattr(DOM::Modifier, "abstract")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_none():
    assert hasattr(DOM::Modifier, "none")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_protected():
    assert hasattr(DOM::Modifier, "protected")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_volatile():
    assert hasattr(DOM::Modifier, "volatile")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_static():
    assert hasattr(DOM::Modifier, "static")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_synchronized():
    assert hasattr(DOM::Modifier, "synchronized")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_strictfp():
    assert hasattr(DOM::Modifier, "strictfp")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_private():
    assert hasattr(DOM::Modifier, "private")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_public():
    assert hasattr(DOM::Modifier, "public")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_final():
    assert hasattr(DOM::Modifier, "final")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_dom::modifier_has_native():
    assert hasattr(DOM::Modifier, "native")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)



def test_dom::catchclause_is_not_abstract():
    assert not inspect.isabstract(DOM::CatchClause)


def test_dom::catchclause_constructor_exists():
    assert callable(DOM::CatchClause.__init__)


def test_dom::catchclause_constructor_args():
    sig = inspect.signature(DOM::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_dom::compilationunit_is_not_abstract():
    assert not inspect.isabstract(DOM::CompilationUnit)


def test_dom::compilationunit_constructor_exists():
    assert callable(DOM::CompilationUnit.__init__)


def test_dom::compilationunit_constructor_args():
    sig = inspect.signature(DOM::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_dom::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::PackageDeclaration)


def test_dom::packagedeclaration_constructor_exists():
    assert callable(DOM::PackageDeclaration.__init__)


def test_dom::packagedeclaration_constructor_args():
    sig = inspect.signature(DOM::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::memberref_is_not_abstract():
    assert not inspect.isabstract(DOM::MemberRef)


def test_dom::memberref_constructor_exists():
    assert callable(DOM::MemberRef.__init__)


def test_dom::memberref_constructor_args():
    sig = inspect.signature(DOM::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_dom::methodref_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodRef)


def test_dom::methodref_constructor_exists():
    assert callable(DOM::MethodRef.__init__)


def test_dom::methodref_constructor_args():
    sig = inspect.signature(DOM::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_dom::statement_is_not_abstract():
    assert not inspect.isabstract(DOM::Statement)


def test_dom::statement_constructor_exists():
    assert callable(DOM::Statement.__init__)


def test_dom::statement_constructor_args():
    sig = inspect.signature(DOM::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclaration)


def test_dom::variabledeclaration_constructor_exists():
    assert callable(DOM::VariableDeclaration.__init__)


def test_dom::variabledeclaration_constructor_args():
    sig = inspect.signature(DOM::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_dom::variabledeclaration_has_extraDimensions():
    assert hasattr(DOM::VariableDeclaration, "extraDimensions")
    descriptor = None
    for klass in DOM::VariableDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_dom::textelement_is_not_abstract():
    assert not inspect.isabstract(DOM::TextElement)


def test_dom::textelement_constructor_exists():
    assert callable(DOM::TextElement.__init__)


def test_dom::textelement_constructor_args():
    sig = inspect.signature(DOM::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_dom::textelement_has_text():
    assert hasattr(DOM::TextElement, "text")
    descriptor = None
    for klass in DOM::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_dom::membervaluepair_is_not_abstract():
    assert not inspect.isabstract(DOM::MemberValuePair)


def test_dom::membervaluepair_constructor_exists():
    assert callable(DOM::MemberValuePair.__init__)


def test_dom::membervaluepair_constructor_args():
    sig = inspect.signature(DOM::MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_dom::tagelement_is_not_abstract():
    assert not inspect.isabstract(DOM::TagElement)


def test_dom::tagelement_constructor_exists():
    assert callable(DOM::TagElement.__init__)


def test_dom::tagelement_constructor_args():
    sig = inspect.signature(DOM::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "nested" in params, "Missing parameter 'nested'"

def test_dom::tagelement_has_tagName():
    assert hasattr(DOM::TagElement, "tagName")
    descriptor = None
    for klass in DOM::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_dom::tagelement_has_nested():
    assert hasattr(DOM::TagElement, "nested")
    descriptor = None
    for klass in DOM::TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)



def test_dom::comment_is_not_abstract():
    assert not inspect.isabstract(DOM::Comment)


def test_dom::comment_constructor_exists():
    assert callable(DOM::Comment.__init__)


def test_dom::comment_constructor_args():
    sig = inspect.signature(DOM::Comment.__init__)
    params = list(sig.parameters.keys())



def test_dom::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodRefParameter)


def test_dom::methodrefparameter_constructor_exists():
    assert callable(DOM::MethodRefParameter.__init__)


def test_dom::methodrefparameter_constructor_args():
    sig = inspect.signature(DOM::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_dom::methodrefparameter_has_varargs():
    assert hasattr(DOM::MethodRefParameter, "varargs")
    descriptor = None
    for klass in DOM::MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_dom::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::ImportDeclaration)


def test_dom::importdeclaration_constructor_exists():
    assert callable(DOM::ImportDeclaration.__init__)


def test_dom::importdeclaration_constructor_args():
    sig = inspect.signature(DOM::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"

def test_dom::importdeclaration_has_onDemand():
    assert hasattr(DOM::ImportDeclaration, "onDemand")
    descriptor = None
    for klass in DOM::ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)

def test_dom::importdeclaration_has_static():
    assert hasattr(DOM::ImportDeclaration, "static")
    descriptor = None
    for klass in DOM::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_dom::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::BodyDeclaration)


def test_dom::bodydeclaration_constructor_exists():
    assert callable(DOM::BodyDeclaration.__init__)


def test_dom::bodydeclaration_constructor_args():
    sig = inspect.signature(DOM::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::expression_is_not_abstract():
    assert not inspect.isabstract(DOM::Expression)


def test_dom::expression_constructor_exists():
    assert callable(DOM::Expression.__init__)


def test_dom::expression_constructor_args():
    sig = inspect.signature(DOM::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"

def test_dom::expression_has_resolveBoxing():
    assert hasattr(DOM::Expression, "resolveBoxing")
    descriptor = None
    for klass in DOM::Expression.__mro__:
        if "resolveBoxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveBoxing"]
            break
    assert isinstance(descriptor, property)

def test_dom::expression_has_resolveUnboxing():
    assert hasattr(DOM::Expression, "resolveUnboxing")
    descriptor = None
    for klass in DOM::Expression.__mro__:
        if "resolveUnboxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveUnboxing"]
            break
    assert isinstance(descriptor, property)



def test_dom::type_is_not_abstract():
    assert not inspect.isabstract(DOM::Type)


def test_dom::type_constructor_exists():
    assert callable(DOM::Type.__init__)


def test_dom::type_constructor_args():
    sig = inspect.signature(DOM::Type.__init__)
    params = list(sig.parameters.keys())



def test_dom::typeparameter_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeParameter)


def test_dom::typeparameter_constructor_exists():
    assert callable(DOM::TypeParameter.__init__)


def test_dom::typeparameter_constructor_args():
    sig = inspect.signature(DOM::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AnonymousClassDeclaration)


def test_dom::anonymousclassdeclaration_constructor_exists():
    assert callable(DOM::AnonymousClassDeclaration.__init__)


def test_dom::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(DOM::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::astnode_is_not_abstract():
    assert not inspect.isabstract(DOM::ASTNode)


def test_dom::astnode_constructor_exists():
    assert callable(DOM::ASTNode.__init__)


def test_dom::astnode_constructor_args():
    sig = inspect.signature(DOM::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_dom::ast_is_not_abstract():
    assert not inspect.isabstract(DOM::AST)


def test_dom::ast_constructor_exists():
    assert callable(DOM::AST.__init__)


def test_dom::ast_constructor_args():
    sig = inspect.signature(DOM::AST.__init__)
    params = list(sig.parameters.keys())

def test_postfixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpressionOperatorKind is not None

def test_postfixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpressionOperatorKind]
    expected_literals = [
        "decrement",
        "increment",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpressionOperatorKind"

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "right_shift_signed",
        "conditional_and",
        "greater_equals",
        "conditional_or",
        "and_",
        "right_shift_unsigned",
        "equals",
        "less",
        "divide",
        "left_shift",
        "times",
        "less_equals",
        "not_equals",
        "plus",
        "greater",
        "remainder",
        "xor",
        "minus",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

def test_prefixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionOperatorKind is not None

def test_prefixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionOperatorKind]
    expected_literals = [
        "not_",
        "minus",
        "plus",
        "decrement",
        "increment",
        "complement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionOperatorKind"

def test_assignmentoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorKind is not None

def test_assignmentoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorKind]
    expected_literals = [
        "divide_assign",
        "bit_xor_assign",
        "assign",
        "bit_or_assign",
        "right_shift_signed_assign",
        "times_assign",
        "minus_assign",
        "left_shift_assign",
        "plus_assign",
        "remainder_assign",
        "bit_and_assign",
        "right_shift_unsigned_assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"


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
Annotation_strategy = st.builds(
    Annotation,
)
DOM::NormalAnnotation_strategy = st.builds(
    DOM::NormalAnnotation,
)
DOM::SingleMemberAnnotation_strategy = st.builds(
    DOM::SingleMemberAnnotation,
)
DOM::MarkerAnnotation_strategy = st.builds(
    DOM::MarkerAnnotation,
)
Name_strategy = st.builds(
    Name,
)
DOM::QualifiedName_strategy = st.builds(
    DOM::QualifiedName,
)
Type_strategy = st.builds(
    Type,
)
DOM::PrimitiveType_strategy = st.builds(
    DOM::PrimitiveType,
    code=
        safe_text
)
DOM::ParameterizedType_strategy = st.builds(
    DOM::ParameterizedType,
)
DOM::SimpleType_strategy = st.builds(
    DOM::SimpleType,
)
DOM::QualifiedType_strategy = st.builds(
    DOM::QualifiedType,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
DOM::WildcardType_strategy = st.builds(
    DOM::WildcardType,
    upperBound=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
DOM::WhileStatement_strategy = st.builds(
    DOM::WhileStatement,
)
DOM::BreakStatement_strategy = st.builds(
    DOM::BreakStatement,
)
DOM::SynchronizedStatement_strategy = st.builds(
    DOM::SynchronizedStatement,
)
DOM::SwitchStatement_strategy = st.builds(
    DOM::SwitchStatement,
)
DOM::SwitchCase_strategy = st.builds(
    DOM::SwitchCase,
    default=
        safe_text
)
DOM::EnhancedForStatement_strategy = st.builds(
    DOM::EnhancedForStatement,
)
DOM::TryStatement_strategy = st.builds(
    DOM::TryStatement,
)
DOM::ThrowStatement_strategy = st.builds(
    DOM::ThrowStatement,
)
DOM::ForStatement_strategy = st.builds(
    DOM::ForStatement,
)
DOM::SuperConstructorInvocation_strategy = st.builds(
    DOM::SuperConstructorInvocation,
)
DOM::EmptyStatement_strategy = st.builds(
    DOM::EmptyStatement,
)
DOM::ExpressionStatement_strategy = st.builds(
    DOM::ExpressionStatement,
)
DOM::ConstructorInvocation_strategy = st.builds(
    DOM::ConstructorInvocation,
)
DOM::ReturnStatement_strategy = st.builds(
    DOM::ReturnStatement,
)
DOM::VariableDeclarationStatement_strategy = st.builds(
    DOM::VariableDeclarationStatement,
)
DOM::TypeDeclarationStatement_strategy = st.builds(
    DOM::TypeDeclarationStatement,
)
DOM::LabeledStatement_strategy = st.builds(
    DOM::LabeledStatement,
)
DOM::IfStatement_strategy = st.builds(
    DOM::IfStatement,
)
DOM::AssertStatement_strategy = st.builds(
    DOM::AssertStatement,
)
DOM::DoStatement_strategy = st.builds(
    DOM::DoStatement,
)
DOM::ContinueStatement_strategy = st.builds(
    DOM::ContinueStatement,
)
DOM::ArrayType_strategy = st.builds(
    DOM::ArrayType,
    dimensions=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
DOM::InstanceofExpression_strategy = st.builds(
    DOM::InstanceofExpression,
)
DOM::ArrayCreation_strategy = st.builds(
    DOM::ArrayCreation,
)
DOM::PrefixExpression_strategy = st.builds(
    DOM::PrefixExpression,
    operator=
        safe_text
)
DOM::MethodInvocation_strategy = st.builds(
    DOM::MethodInvocation,
)
DOM::PostfixExpression_strategy = st.builds(
    DOM::PostfixExpression,
    operator=
        safe_text
)
DOM::InfixExpression_strategy = st.builds(
    DOM::InfixExpression,
    operator=
        safe_text
)
DOM::ArrayAccess_strategy = st.builds(
    DOM::ArrayAccess,
)
DOM::FieldAccess_strategy = st.builds(
    DOM::FieldAccess,
)
DOM::VariableDeclarationExpression_strategy = st.builds(
    DOM::VariableDeclarationExpression,
)
DOM::NullLiteral_strategy = st.builds(
    DOM::NullLiteral,
)
DOM::SuperFieldAccess_strategy = st.builds(
    DOM::SuperFieldAccess,
)
DOM::BooleanLiteral_strategy = st.builds(
    DOM::BooleanLiteral,
    booleanValue=
        safe_text
)
DOM::CharacterLiteral_strategy = st.builds(
    DOM::CharacterLiteral,
    escapedValue=
        safe_text,
    charValue=
        safe_text
)
DOM::TypeLiteral_strategy = st.builds(
    DOM::TypeLiteral,
)
DOM::ConditionalExpression_strategy = st.builds(
    DOM::ConditionalExpression,
)
DOM::StringLiteral_strategy = st.builds(
    DOM::StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
DOM::ClassInstanceCreation_strategy = st.builds(
    DOM::ClassInstanceCreation,
)
DOM::ArrayInitializer_strategy = st.builds(
    DOM::ArrayInitializer,
)
DOM::CastExpression_strategy = st.builds(
    DOM::CastExpression,
)
DOM::ThisExpression_strategy = st.builds(
    DOM::ThisExpression,
)
DOM::NumberLiteral_strategy = st.builds(
    DOM::NumberLiteral,
    token=
        safe_text
)
DOM::Assignment_strategy = st.builds(
    DOM::Assignment,
    operator=
        safe_text
)
DOM::SuperMethodInvocation_strategy = st.builds(
    DOM::SuperMethodInvocation,
)
DOM::ParenthesizedExpression_strategy = st.builds(
    DOM::ParenthesizedExpression,
)
Comment_strategy = st.builds(
    Comment,
)
DOM::LineComment_strategy = st.builds(
    DOM::LineComment,
)
DOM::BlockComment_strategy = st.builds(
    DOM::BlockComment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
DOM::AnnotationTypeDeclaration_strategy = st.builds(
    DOM::AnnotationTypeDeclaration,
)
DOM::IMethod_strategy = st.builds(
    DOM::IMethod,
)
DOM::VariableDeclarationFragment_strategy = st.builds(
    DOM::VariableDeclarationFragment,
)
DOM::TypeDeclaration_strategy = st.builds(
    DOM::TypeDeclaration,
    interface=
        safe_text
)
DOM::EnumDeclaration_strategy = st.builds(
    DOM::EnumDeclaration,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
DOM::MethodDeclaration_strategy = st.builds(
    DOM::MethodDeclaration,
    constructor=
        safe_text,
    varargs=
        safe_text,
    extraDimensions=
        safe_text
)
DOM::Initializer_strategy = st.builds(
    DOM::Initializer,
)
DOM::FieldDeclaration_strategy = st.builds(
    DOM::FieldDeclaration,
)
DOM::IPackageFragment_strategy = st.builds(
    DOM::IPackageFragment,
)
DOM::EnumConstantDeclaration_strategy = st.builds(
    DOM::EnumConstantDeclaration,
)
DOM::AnnotationTypeMemberDeclaration_strategy = st.builds(
    DOM::AnnotationTypeMemberDeclaration,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
DOM::Annotation_strategy = st.builds(
    DOM::Annotation,
)
DOM::SimpleName_strategy = st.builds(
    DOM::SimpleName,
    identifier=
        safe_text,
    declaration=
        safe_text
)
DOM::Name_strategy = st.builds(
    DOM::Name,
    fullyQualifiedName=
        safe_text
)
DOM::AbstractTypeDeclaration_strategy = st.builds(
    DOM::AbstractTypeDeclaration,
    localTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text,
    memberTypeDeclaration=
        safe_text
)
DOM::SingleVariableDeclaration_strategy = st.builds(
    DOM::SingleVariableDeclaration,
    varargs=
        safe_text
)
DOM::Block_strategy = st.builds(
    DOM::Block,
)
DOM::Javadoc_strategy = st.builds(
    DOM::Javadoc,
)
DOM::ExtendedModifier_strategy = st.builds(
    DOM::ExtendedModifier,
)
DOM::IType_strategy = st.builds(
    DOM::IType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
DOM::Modifier_strategy = st.builds(
    DOM::Modifier,
    transient=
        safe_text,
    abstract=
        safe_text,
    none=
        safe_text,
    protected=
        safe_text,
    volatile=
        safe_text,
    static=
        safe_text,
    synchronized=
        safe_text,
    strictfp=
        safe_text,
    private=
        safe_text,
    public=
        safe_text,
    final=
        safe_text,
    native=
        safe_text
)
DOM::CatchClause_strategy = st.builds(
    DOM::CatchClause,
)
DOM::CompilationUnit_strategy = st.builds(
    DOM::CompilationUnit,
)
DOM::PackageDeclaration_strategy = st.builds(
    DOM::PackageDeclaration,
)
DOM::MemberRef_strategy = st.builds(
    DOM::MemberRef,
)
DOM::MethodRef_strategy = st.builds(
    DOM::MethodRef,
)
DOM::Statement_strategy = st.builds(
    DOM::Statement,
)
DOM::VariableDeclaration_strategy = st.builds(
    DOM::VariableDeclaration,
    extraDimensions=
        safe_text
)
DOM::TextElement_strategy = st.builds(
    DOM::TextElement,
    text=
        safe_text
)
DOM::MemberValuePair_strategy = st.builds(
    DOM::MemberValuePair,
)
DOM::TagElement_strategy = st.builds(
    DOM::TagElement,
    tagName=
        safe_text,
    nested=
        safe_text
)
DOM::Comment_strategy = st.builds(
    DOM::Comment,
)
DOM::MethodRefParameter_strategy = st.builds(
    DOM::MethodRefParameter,
    varargs=
        safe_text
)
DOM::ImportDeclaration_strategy = st.builds(
    DOM::ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
DOM::BodyDeclaration_strategy = st.builds(
    DOM::BodyDeclaration,
)
DOM::Expression_strategy = st.builds(
    DOM::Expression,
    resolveBoxing=
        safe_text,
    resolveUnboxing=
        safe_text
)
DOM::Type_strategy = st.builds(
    DOM::Type,
)
DOM::TypeParameter_strategy = st.builds(
    DOM::TypeParameter,
)
DOM::AnonymousClassDeclaration_strategy = st.builds(
    DOM::AnonymousClassDeclaration,
)
DOM::ASTNode_strategy = st.builds(
    DOM::ASTNode,
)
DOM::AST_strategy = st.builds(
    DOM::AST,
)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=DOM::NormalAnnotation_strategy)
@settings(max_examples=50)
def test_dom::normalannotation_instantiation(instance):
    assert isinstance(instance, DOM::NormalAnnotation)

@given(instance=DOM::SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_dom::singlememberannotation_instantiation(instance):
    assert isinstance(instance, DOM::SingleMemberAnnotation)

@given(instance=DOM::MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_dom::markerannotation_instantiation(instance):
    assert isinstance(instance, DOM::MarkerAnnotation)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DOM::QualifiedName_strategy)
@settings(max_examples=50)
def test_dom::qualifiedname_instantiation(instance):
    assert isinstance(instance, DOM::QualifiedName)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=DOM::PrimitiveType_strategy)
@settings(max_examples=50)
def test_dom::primitivetype_instantiation(instance):
    assert isinstance(instance, DOM::PrimitiveType)

@given(instance=DOM::PrimitiveType_strategy)
def test_dom::primitivetype_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=DOM::PrimitiveType_strategy)
def test_dom::primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=DOM::ParameterizedType_strategy)
@settings(max_examples=50)
def test_dom::parameterizedtype_instantiation(instance):
    assert isinstance(instance, DOM::ParameterizedType)

@given(instance=DOM::SimpleType_strategy)
@settings(max_examples=50)
def test_dom::simpletype_instantiation(instance):
    assert isinstance(instance, DOM::SimpleType)

@given(instance=DOM::QualifiedType_strategy)
@settings(max_examples=50)
def test_dom::qualifiedtype_instantiation(instance):
    assert isinstance(instance, DOM::QualifiedType)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=DOM::WildcardType_strategy)
@settings(max_examples=50)
def test_dom::wildcardtype_instantiation(instance):
    assert isinstance(instance, DOM::WildcardType)

@given(instance=DOM::WildcardType_strategy)
def test_dom::wildcardtype_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=DOM::WildcardType_strategy)
def test_dom::wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DOM::WhileStatement_strategy)
@settings(max_examples=50)
def test_dom::whilestatement_instantiation(instance):
    assert isinstance(instance, DOM::WhileStatement)

@given(instance=DOM::BreakStatement_strategy)
@settings(max_examples=50)
def test_dom::breakstatement_instantiation(instance):
    assert isinstance(instance, DOM::BreakStatement)

@given(instance=DOM::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_dom::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, DOM::SynchronizedStatement)

@given(instance=DOM::SwitchStatement_strategy)
@settings(max_examples=50)
def test_dom::switchstatement_instantiation(instance):
    assert isinstance(instance, DOM::SwitchStatement)

@given(instance=DOM::SwitchCase_strategy)
@settings(max_examples=50)
def test_dom::switchcase_instantiation(instance):
    assert isinstance(instance, DOM::SwitchCase)

@given(instance=DOM::SwitchCase_strategy)
def test_dom::switchcase_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=DOM::SwitchCase_strategy)
def test_dom::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=DOM::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_dom::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, DOM::EnhancedForStatement)

@given(instance=DOM::TryStatement_strategy)
@settings(max_examples=50)
def test_dom::trystatement_instantiation(instance):
    assert isinstance(instance, DOM::TryStatement)

@given(instance=DOM::ThrowStatement_strategy)
@settings(max_examples=50)
def test_dom::throwstatement_instantiation(instance):
    assert isinstance(instance, DOM::ThrowStatement)

@given(instance=DOM::ForStatement_strategy)
@settings(max_examples=50)
def test_dom::forstatement_instantiation(instance):
    assert isinstance(instance, DOM::ForStatement)

@given(instance=DOM::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dom::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, DOM::SuperConstructorInvocation)

@given(instance=DOM::EmptyStatement_strategy)
@settings(max_examples=50)
def test_dom::emptystatement_instantiation(instance):
    assert isinstance(instance, DOM::EmptyStatement)

@given(instance=DOM::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom::expressionstatement_instantiation(instance):
    assert isinstance(instance, DOM::ExpressionStatement)

@given(instance=DOM::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dom::constructorinvocation_instantiation(instance):
    assert isinstance(instance, DOM::ConstructorInvocation)

@given(instance=DOM::ReturnStatement_strategy)
@settings(max_examples=50)
def test_dom::returnstatement_instantiation(instance):
    assert isinstance(instance, DOM::ReturnStatement)

@given(instance=DOM::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclarationStatement)

@given(instance=DOM::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, DOM::TypeDeclarationStatement)

@given(instance=DOM::LabeledStatement_strategy)
@settings(max_examples=50)
def test_dom::labeledstatement_instantiation(instance):
    assert isinstance(instance, DOM::LabeledStatement)

@given(instance=DOM::IfStatement_strategy)
@settings(max_examples=50)
def test_dom::ifstatement_instantiation(instance):
    assert isinstance(instance, DOM::IfStatement)

@given(instance=DOM::AssertStatement_strategy)
@settings(max_examples=50)
def test_dom::assertstatement_instantiation(instance):
    assert isinstance(instance, DOM::AssertStatement)

@given(instance=DOM::DoStatement_strategy)
@settings(max_examples=50)
def test_dom::dostatement_instantiation(instance):
    assert isinstance(instance, DOM::DoStatement)

@given(instance=DOM::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dom::continuestatement_instantiation(instance):
    assert isinstance(instance, DOM::ContinueStatement)

@given(instance=DOM::ArrayType_strategy)
@settings(max_examples=50)
def test_dom::arraytype_instantiation(instance):
    assert isinstance(instance, DOM::ArrayType)

@given(instance=DOM::ArrayType_strategy)
def test_dom::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=DOM::ArrayType_strategy)
def test_dom::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=DOM::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_dom::instanceofexpression_instantiation(instance):
    assert isinstance(instance, DOM::InstanceofExpression)

@given(instance=DOM::ArrayCreation_strategy)
@settings(max_examples=50)
def test_dom::arraycreation_instantiation(instance):
    assert isinstance(instance, DOM::ArrayCreation)

@given(instance=DOM::PrefixExpression_strategy)
@settings(max_examples=50)
def test_dom::prefixexpression_instantiation(instance):
    assert isinstance(instance, DOM::PrefixExpression)

@given(instance=DOM::PrefixExpression_strategy)
def test_dom::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=DOM::PrefixExpression_strategy)
def test_dom::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM::MethodInvocation_strategy)
@settings(max_examples=50)
def test_dom::methodinvocation_instantiation(instance):
    assert isinstance(instance, DOM::MethodInvocation)

@given(instance=DOM::PostfixExpression_strategy)
@settings(max_examples=50)
def test_dom::postfixexpression_instantiation(instance):
    assert isinstance(instance, DOM::PostfixExpression)

@given(instance=DOM::PostfixExpression_strategy)
def test_dom::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=DOM::PostfixExpression_strategy)
def test_dom::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM::InfixExpression_strategy)
@settings(max_examples=50)
def test_dom::infixexpression_instantiation(instance):
    assert isinstance(instance, DOM::InfixExpression)

@given(instance=DOM::InfixExpression_strategy)
def test_dom::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=DOM::InfixExpression_strategy)
def test_dom::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM::ArrayAccess_strategy)
@settings(max_examples=50)
def test_dom::arrayaccess_instantiation(instance):
    assert isinstance(instance, DOM::ArrayAccess)

@given(instance=DOM::FieldAccess_strategy)
@settings(max_examples=50)
def test_dom::fieldaccess_instantiation(instance):
    assert isinstance(instance, DOM::FieldAccess)

@given(instance=DOM::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclarationExpression)

@given(instance=DOM::NullLiteral_strategy)
@settings(max_examples=50)
def test_dom::nullliteral_instantiation(instance):
    assert isinstance(instance, DOM::NullLiteral)

@given(instance=DOM::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_dom::superfieldaccess_instantiation(instance):
    assert isinstance(instance, DOM::SuperFieldAccess)

@given(instance=DOM::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_dom::booleanliteral_instantiation(instance):
    assert isinstance(instance, DOM::BooleanLiteral)

@given(instance=DOM::BooleanLiteral_strategy)
def test_dom::booleanliteral_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, str)


@given(instance=DOM::BooleanLiteral_strategy)
def test_dom::booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=DOM::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_dom::characterliteral_instantiation(instance):
    assert isinstance(instance, DOM::CharacterLiteral)

@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_charValue_type(instance):
    assert isinstance(instance.charValue, str)


@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=DOM::TypeLiteral_strategy)
@settings(max_examples=50)
def test_dom::typeliteral_instantiation(instance):
    assert isinstance(instance, DOM::TypeLiteral)

@given(instance=DOM::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_dom::conditionalexpression_instantiation(instance):
    assert isinstance(instance, DOM::ConditionalExpression)

@given(instance=DOM::StringLiteral_strategy)
@settings(max_examples=50)
def test_dom::stringliteral_instantiation(instance):
    assert isinstance(instance, DOM::StringLiteral)

@given(instance=DOM::StringLiteral_strategy)
def test_dom::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=DOM::StringLiteral_strategy)
def test_dom::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=DOM::StringLiteral_strategy)
def test_dom::stringliteral_literalValue_type(instance):
    assert isinstance(instance.literalValue, str)


@given(instance=DOM::StringLiteral_strategy)
def test_dom::stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=DOM::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_dom::classinstancecreation_instantiation(instance):
    assert isinstance(instance, DOM::ClassInstanceCreation)

@given(instance=DOM::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_dom::arrayinitializer_instantiation(instance):
    assert isinstance(instance, DOM::ArrayInitializer)

@given(instance=DOM::CastExpression_strategy)
@settings(max_examples=50)
def test_dom::castexpression_instantiation(instance):
    assert isinstance(instance, DOM::CastExpression)

@given(instance=DOM::ThisExpression_strategy)
@settings(max_examples=50)
def test_dom::thisexpression_instantiation(instance):
    assert isinstance(instance, DOM::ThisExpression)

@given(instance=DOM::NumberLiteral_strategy)
@settings(max_examples=50)
def test_dom::numberliteral_instantiation(instance):
    assert isinstance(instance, DOM::NumberLiteral)

@given(instance=DOM::NumberLiteral_strategy)
def test_dom::numberliteral_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=DOM::NumberLiteral_strategy)
def test_dom::numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=DOM::Assignment_strategy)
@settings(max_examples=50)
def test_dom::assignment_instantiation(instance):
    assert isinstance(instance, DOM::Assignment)

@given(instance=DOM::Assignment_strategy)
def test_dom::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=DOM::Assignment_strategy)
def test_dom::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_dom::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, DOM::SuperMethodInvocation)

@given(instance=DOM::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_dom::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, DOM::ParenthesizedExpression)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=DOM::LineComment_strategy)
@settings(max_examples=50)
def test_dom::linecomment_instantiation(instance):
    assert isinstance(instance, DOM::LineComment)

@given(instance=DOM::BlockComment_strategy)
@settings(max_examples=50)
def test_dom::blockcomment_instantiation(instance):
    assert isinstance(instance, DOM::BlockComment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=DOM::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AnnotationTypeDeclaration)

@given(instance=DOM::IMethod_strategy)
@settings(max_examples=50)
def test_dom::imethod_instantiation(instance):
    assert isinstance(instance, DOM::IMethod)

@given(instance=DOM::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclarationFragment)

@given(instance=DOM::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom::typedeclaration_instantiation(instance):
    assert isinstance(instance, DOM::TypeDeclaration)

@given(instance=DOM::TypeDeclaration_strategy)
def test_dom::typedeclaration_interface_type(instance):
    assert isinstance(instance.interface, str)


@given(instance=DOM::TypeDeclaration_strategy)
def test_dom::typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=DOM::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_dom::enumdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::EnumDeclaration)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=DOM::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_dom::methoddeclaration_instantiation(instance):
    assert isinstance(instance, DOM::MethodDeclaration)

@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_constructor_type(instance):
    assert isinstance(instance.constructor, str)


@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=DOM::Initializer_strategy)
@settings(max_examples=50)
def test_dom::initializer_instantiation(instance):
    assert isinstance(instance, DOM::Initializer)

@given(instance=DOM::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_dom::fielddeclaration_instantiation(instance):
    assert isinstance(instance, DOM::FieldDeclaration)

@given(instance=DOM::IPackageFragment_strategy)
@settings(max_examples=50)
def test_dom::ipackagefragment_instantiation(instance):
    assert isinstance(instance, DOM::IPackageFragment)

@given(instance=DOM::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_dom::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::EnumConstantDeclaration)

@given(instance=DOM::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_dom::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AnnotationTypeMemberDeclaration)

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=DOM::Annotation_strategy)
@settings(max_examples=50)
def test_dom::annotation_instantiation(instance):
    assert isinstance(instance, DOM::Annotation)

@given(instance=DOM::SimpleName_strategy)
@settings(max_examples=50)
def test_dom::simplename_instantiation(instance):
    assert isinstance(instance, DOM::SimpleName)

@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=DOM::Name_strategy)
@settings(max_examples=50)
def test_dom::name_instantiation(instance):
    assert isinstance(instance, DOM::Name)

@given(instance=DOM::Name_strategy)
def test_dom::name_fullyQualifiedName_type(instance):
    assert isinstance(instance.fullyQualifiedName, str)


@given(instance=DOM::Name_strategy)
def test_dom::name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=DOM::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AbstractTypeDeclaration)

@given(instance=DOM::AbstractTypeDeclaration_strategy)
def test_dom::abstracttypedeclaration_localTypeDeclaration_type(instance):
    assert isinstance(instance.localTypeDeclaration, str)


@given(instance=DOM::AbstractTypeDeclaration_strategy)
def test_dom::abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original

@given(instance=DOM::AbstractTypeDeclaration_strategy)
def test_dom::abstracttypedeclaration_packageMemberTypeDeclaration_type(instance):
    assert isinstance(instance.packageMemberTypeDeclaration, str)


@given(instance=DOM::AbstractTypeDeclaration_strategy)
def test_dom::abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original

@given(instance=DOM::AbstractTypeDeclaration_strategy)
def test_dom::abstracttypedeclaration_memberTypeDeclaration_type(instance):
    assert isinstance(instance.memberTypeDeclaration, str)


@given(instance=DOM::AbstractTypeDeclaration_strategy)
def test_dom::abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original

@given(instance=DOM::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_dom::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, DOM::SingleVariableDeclaration)

@given(instance=DOM::SingleVariableDeclaration_strategy)
def test_dom::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=DOM::SingleVariableDeclaration_strategy)
def test_dom::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=DOM::Block_strategy)
@settings(max_examples=50)
def test_dom::block_instantiation(instance):
    assert isinstance(instance, DOM::Block)

@given(instance=DOM::Javadoc_strategy)
@settings(max_examples=50)
def test_dom::javadoc_instantiation(instance):
    assert isinstance(instance, DOM::Javadoc)

@given(instance=DOM::ExtendedModifier_strategy)
@settings(max_examples=50)
def test_dom::extendedmodifier_instantiation(instance):
    assert isinstance(instance, DOM::ExtendedModifier)

@given(instance=DOM::IType_strategy)
@settings(max_examples=50)
def test_dom::itype_instantiation(instance):
    assert isinstance(instance, DOM::IType)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=DOM::Modifier_strategy)
@settings(max_examples=50)
def test_dom::modifier_instantiation(instance):
    assert isinstance(instance, DOM::Modifier)

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_transient_type(instance):
    assert isinstance(instance.transient, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_none_type(instance):
    assert isinstance(instance.none, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_private_type(instance):
    assert isinstance(instance.private, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_public_type(instance):
    assert isinstance(instance.public, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_native_type(instance):
    assert isinstance(instance.native, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=DOM::CatchClause_strategy)
@settings(max_examples=50)
def test_dom::catchclause_instantiation(instance):
    assert isinstance(instance, DOM::CatchClause)

@given(instance=DOM::CompilationUnit_strategy)
@settings(max_examples=50)
def test_dom::compilationunit_instantiation(instance):
    assert isinstance(instance, DOM::CompilationUnit)

@given(instance=DOM::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_dom::packagedeclaration_instantiation(instance):
    assert isinstance(instance, DOM::PackageDeclaration)

@given(instance=DOM::MemberRef_strategy)
@settings(max_examples=50)
def test_dom::memberref_instantiation(instance):
    assert isinstance(instance, DOM::MemberRef)

@given(instance=DOM::MethodRef_strategy)
@settings(max_examples=50)
def test_dom::methodref_instantiation(instance):
    assert isinstance(instance, DOM::MethodRef)

@given(instance=DOM::Statement_strategy)
@settings(max_examples=50)
def test_dom::statement_instantiation(instance):
    assert isinstance(instance, DOM::Statement)

@given(instance=DOM::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_dom::variabledeclaration_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclaration)

@given(instance=DOM::VariableDeclaration_strategy)
def test_dom::variabledeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=DOM::VariableDeclaration_strategy)
def test_dom::variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=DOM::TextElement_strategy)
@settings(max_examples=50)
def test_dom::textelement_instantiation(instance):
    assert isinstance(instance, DOM::TextElement)

@given(instance=DOM::TextElement_strategy)
def test_dom::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=DOM::TextElement_strategy)
def test_dom::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=DOM::MemberValuePair_strategy)
@settings(max_examples=50)
def test_dom::membervaluepair_instantiation(instance):
    assert isinstance(instance, DOM::MemberValuePair)

@given(instance=DOM::TagElement_strategy)
@settings(max_examples=50)
def test_dom::tagelement_instantiation(instance):
    assert isinstance(instance, DOM::TagElement)

@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_nested_type(instance):
    assert isinstance(instance.nested, str)


@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original

@given(instance=DOM::Comment_strategy)
@settings(max_examples=50)
def test_dom::comment_instantiation(instance):
    assert isinstance(instance, DOM::Comment)

@given(instance=DOM::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_dom::methodrefparameter_instantiation(instance):
    assert isinstance(instance, DOM::MethodRefParameter)

@given(instance=DOM::MethodRefParameter_strategy)
def test_dom::methodrefparameter_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=DOM::MethodRefParameter_strategy)
def test_dom::methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=DOM::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_dom::importdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::ImportDeclaration)

@given(instance=DOM::ImportDeclaration_strategy)
def test_dom::importdeclaration_onDemand_type(instance):
    assert isinstance(instance.onDemand, str)


@given(instance=DOM::ImportDeclaration_strategy)
def test_dom::importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original

@given(instance=DOM::ImportDeclaration_strategy)
def test_dom::importdeclaration_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=DOM::ImportDeclaration_strategy)
def test_dom::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=DOM::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_dom::bodydeclaration_instantiation(instance):
    assert isinstance(instance, DOM::BodyDeclaration)

@given(instance=DOM::Expression_strategy)
@settings(max_examples=50)
def test_dom::expression_instantiation(instance):
    assert isinstance(instance, DOM::Expression)

@given(instance=DOM::Expression_strategy)
def test_dom::expression_resolveBoxing_type(instance):
    assert isinstance(instance.resolveBoxing, str)


@given(instance=DOM::Expression_strategy)
def test_dom::expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original

@given(instance=DOM::Expression_strategy)
def test_dom::expression_resolveUnboxing_type(instance):
    assert isinstance(instance.resolveUnboxing, str)


@given(instance=DOM::Expression_strategy)
def test_dom::expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original

@given(instance=DOM::Type_strategy)
@settings(max_examples=50)
def test_dom::type_instantiation(instance):
    assert isinstance(instance, DOM::Type)

@given(instance=DOM::TypeParameter_strategy)
@settings(max_examples=50)
def test_dom::typeparameter_instantiation(instance):
    assert isinstance(instance, DOM::TypeParameter)

@given(instance=DOM::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_dom::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AnonymousClassDeclaration)

@given(instance=DOM::ASTNode_strategy)
@settings(max_examples=50)
def test_dom::astnode_instantiation(instance):
    assert isinstance(instance, DOM::ASTNode)

@given(instance=DOM::AST_strategy)
@settings(max_examples=50)
def test_dom::ast_instantiation(instance):
    assert isinstance(instance, DOM::AST)
