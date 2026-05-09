import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    Annotation,
    ast::NormalAnnotation,
    ast::MarkerAnnotation,
    ast::ASTNode,
    ast::MethodReference,
    MethodReference,
    ast::SuperMethodReference,
    ast::ExpressionMethodReference,
    ast::TypeMethodReference,
    ast::CreationReference,
    ast::LambdaExpression,
    ast::InstanceofExpression,
    ast::TypeLiteral,
    AbstractTypeDeclaration,
    ast::EnumDeclaration,
    ast::AnnotationTypeDeclaration,
    ast::TypeDeclaration,
    ast::VariableDeclarationExpression,
    ast::ThisExpression,
    VariableDeclaration,
    ast::SuperMethodInvocation,
    ast::SuperFieldAccess,
    ast::StringLiteral,
    ast::ParenthesizedExpression,
    ast::NumberLiteral,
    ast::NullLiteral,
    Name,
    ast::QualifiedName,
    AnnotatableType,
    ast::WildcardType,
    ast::NameQualifiedType,
    ast::SimpleType,
    ast::QualifiedType,
    ast::PrimitiveType,
    ast::PrefixExpression,
    ast::PostfixExpression,
    Comment,
    ast::BlockComment,
    ast::LineComment,
    ast::MethodInvocation,
    ast::VariableDeclarationFragment,
    ast::Javadoc,
    BodyDeclaration,
    ast::Initializer,
    ast::AnnotationTypeMemberDeclaration,
    ast::MethodDeclaration,
    ast::EnumConstantDeclaration,
    ast::FieldDeclaration,
    ast::FieldAccess,
    ast::InfixExpression,
    ast::ConditionalExpression,
    ast::AbstractTypeDeclaration,
    ast::BooleanLiteral,
    ast::ClassInstanceCreation,
    ast::CharacterLiteral,
    ast::SingleVariableDeclaration,
    ast::CastExpression,
    ast::ArrayAccess,
    ast::Assignment,
    Statement,
    ast::ExpressionStatement,
    ast::TryStatement,
    ast::WhileStatement,
    ast::EnhancedForStatement,
    ast::Block,
    ast::EmptyStatement,
    ast::ForStatement,
    ast::SynchronizedStatement,
    ast::ContinueStatement,
    ast::SwitchCase,
    ast::VariableDeclarationStatement,
    ast::BreakStatement,
    ast::DoStatement,
    ast::LabeledStatement,
    ast::IfStatement,
    ast::ConstructorInvocation,
    ast::SuperConstructorInvocation,
    ast::ThrowStatement,
    ast::ReturnStatement,
    ast::SwitchStatement,
    ast::TypeDeclarationStatement,
    ast::AssertStatement,
    Type,
    ast::UnionType,
    ast::ParameterizedType,
    ast::IntersectionType,
    ast::AnnotatableType,
    ast::ArrayInitializer,
    ast::ArrayType,
    ast::ArrayCreation,
    IExtendedModifier,
    ast::Annotation,
    ASTNode,
    ast::PackageDeclaration,
    ast::Expression,
    ast::ImportDeclaration,
    ast::Dimension,
    ast::CatchClause,
    ast::BodyDeclaration,
    ast::AnonymousClassDeclaration,
    ast::Type,
    ast::Comment,
    ast::Statement,
    ast::TypeParameter,
    ast::CompilationUnit,
    ast::VariableDeclaration,
    ast::Modifier,
    ast::IExtendedModifier,
    ast::MethodRefParameter,
    ast::SimpleName,
    IDocElement,
    ast::Name,
    ast::TagElement,
    ast::MethodRef,
    ast::TextElement,
    ast::MemberRef,
    ast::IDocElement,
    ast::SingleMemberAnnotation,
    ast::MemberValuePair,
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



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ast::normalannotation_is_not_abstract():
    assert not inspect.isabstract(ast::NormalAnnotation)


def test_ast::normalannotation_constructor_exists():
    assert callable(ast::NormalAnnotation.__init__)


def test_ast::normalannotation_constructor_args():
    sig = inspect.signature(ast::NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ast::markerannotation_is_not_abstract():
    assert not inspect.isabstract(ast::MarkerAnnotation)


def test_ast::markerannotation_constructor_exists():
    assert callable(ast::MarkerAnnotation.__init__)


def test_ast::markerannotation_constructor_args():
    sig = inspect.signature(ast::MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ast::astnode_is_not_abstract():
    assert not inspect.isabstract(ast::ASTNode)


def test_ast::astnode_constructor_exists():
    assert callable(ast::ASTNode.__init__)


def test_ast::astnode_constructor_args():
    sig = inspect.signature(ast::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodreference_is_not_abstract():
    assert not inspect.isabstract(ast::MethodReference)


def test_ast::methodreference_constructor_exists():
    assert callable(ast::MethodReference.__init__)


def test_ast::methodreference_constructor_args():
    sig = inspect.signature(ast::MethodReference.__init__)
    params = list(sig.parameters.keys())



def test_methodreference_is_not_abstract():
    assert not inspect.isabstract(MethodReference)


def test_methodreference_constructor_exists():
    assert callable(MethodReference.__init__)


def test_methodreference_constructor_args():
    sig = inspect.signature(MethodReference.__init__)
    params = list(sig.parameters.keys())



def test_ast::supermethodreference_is_not_abstract():
    assert not inspect.isabstract(ast::SuperMethodReference)


def test_ast::supermethodreference_constructor_exists():
    assert callable(ast::SuperMethodReference.__init__)


def test_ast::supermethodreference_constructor_args():
    sig = inspect.signature(ast::SuperMethodReference.__init__)
    params = list(sig.parameters.keys())



def test_ast::expressionmethodreference_is_not_abstract():
    assert not inspect.isabstract(ast::ExpressionMethodReference)


def test_ast::expressionmethodreference_constructor_exists():
    assert callable(ast::ExpressionMethodReference.__init__)


def test_ast::expressionmethodreference_constructor_args():
    sig = inspect.signature(ast::ExpressionMethodReference.__init__)
    params = list(sig.parameters.keys())



def test_ast::typemethodreference_is_not_abstract():
    assert not inspect.isabstract(ast::TypeMethodReference)


def test_ast::typemethodreference_constructor_exists():
    assert callable(ast::TypeMethodReference.__init__)


def test_ast::typemethodreference_constructor_args():
    sig = inspect.signature(ast::TypeMethodReference.__init__)
    params = list(sig.parameters.keys())



def test_ast::creationreference_is_not_abstract():
    assert not inspect.isabstract(ast::CreationReference)


def test_ast::creationreference_constructor_exists():
    assert callable(ast::CreationReference.__init__)


def test_ast::creationreference_constructor_args():
    sig = inspect.signature(ast::CreationReference.__init__)
    params = list(sig.parameters.keys())



def test_ast::lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(ast::LambdaExpression)


def test_ast::lambdaexpression_constructor_exists():
    assert callable(ast::LambdaExpression.__init__)


def test_ast::lambdaexpression_constructor_args():
    sig = inspect.signature(ast::LambdaExpression.__init__)
    params = list(sig.parameters.keys())
    assert "parentheses" in params, "Missing parameter 'parentheses'"

def test_ast::lambdaexpression_has_parentheses():
    assert hasattr(ast::LambdaExpression, "parentheses")
    descriptor = None
    for klass in ast::LambdaExpression.__mro__:
        if "parentheses" in klass.__dict__:
            descriptor = klass.__dict__["parentheses"]
            break
    assert isinstance(descriptor, property)



def test_ast::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(ast::InstanceofExpression)


def test_ast::instanceofexpression_constructor_exists():
    assert callable(ast::InstanceofExpression.__init__)


def test_ast::instanceofexpression_constructor_args():
    sig = inspect.signature(ast::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::typeliteral_is_not_abstract():
    assert not inspect.isabstract(ast::TypeLiteral)


def test_ast::typeliteral_constructor_exists():
    assert callable(ast::TypeLiteral.__init__)


def test_ast::typeliteral_constructor_args():
    sig = inspect.signature(ast::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::EnumDeclaration)


def test_ast::enumdeclaration_constructor_exists():
    assert callable(ast::EnumDeclaration.__init__)


def test_ast::enumdeclaration_constructor_args():
    sig = inspect.signature(ast::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::AnnotationTypeDeclaration)


def test_ast::annotationtypedeclaration_constructor_exists():
    assert callable(ast::AnnotationTypeDeclaration.__init__)


def test_ast::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(ast::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::TypeDeclaration)


def test_ast::typedeclaration_constructor_exists():
    assert callable(ast::TypeDeclaration.__init__)


def test_ast::typedeclaration_constructor_args():
    sig = inspect.signature(ast::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_ast::typedeclaration_has_interface():
    assert hasattr(ast::TypeDeclaration, "interface")
    descriptor = None
    for klass in ast::TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_ast::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(ast::VariableDeclarationExpression)


def test_ast::variabledeclarationexpression_constructor_exists():
    assert callable(ast::VariableDeclarationExpression.__init__)


def test_ast::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(ast::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::thisexpression_is_not_abstract():
    assert not inspect.isabstract(ast::ThisExpression)


def test_ast::thisexpression_constructor_exists():
    assert callable(ast::ThisExpression.__init__)


def test_ast::thisexpression_constructor_args():
    sig = inspect.signature(ast::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ast::SuperMethodInvocation)


def test_ast::supermethodinvocation_constructor_exists():
    assert callable(ast::SuperMethodInvocation.__init__)


def test_ast::supermethodinvocation_constructor_args():
    sig = inspect.signature(ast::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ast::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(ast::SuperFieldAccess)


def test_ast::superfieldaccess_constructor_exists():
    assert callable(ast::SuperFieldAccess.__init__)


def test_ast::superfieldaccess_constructor_args():
    sig = inspect.signature(ast::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast::stringliteral_is_not_abstract():
    assert not inspect.isabstract(ast::StringLiteral)


def test_ast::stringliteral_constructor_exists():
    assert callable(ast::StringLiteral.__init__)


def test_ast::stringliteral_constructor_args():
    sig = inspect.signature(ast::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_ast::stringliteral_has_escapedValue():
    assert hasattr(ast::StringLiteral, "escapedValue")
    descriptor = None
    for klass in ast::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_ast::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ast::ParenthesizedExpression)


def test_ast::parenthesizedexpression_constructor_exists():
    assert callable(ast::ParenthesizedExpression.__init__)


def test_ast::parenthesizedexpression_constructor_args():
    sig = inspect.signature(ast::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::numberliteral_is_not_abstract():
    assert not inspect.isabstract(ast::NumberLiteral)


def test_ast::numberliteral_constructor_exists():
    assert callable(ast::NumberLiteral.__init__)


def test_ast::numberliteral_constructor_args():
    sig = inspect.signature(ast::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_ast::numberliteral_has_token():
    assert hasattr(ast::NumberLiteral, "token")
    descriptor = None
    for klass in ast::NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_ast::nullliteral_is_not_abstract():
    assert not inspect.isabstract(ast::NullLiteral)


def test_ast::nullliteral_constructor_exists():
    assert callable(ast::NullLiteral.__init__)


def test_ast::nullliteral_constructor_args():
    sig = inspect.signature(ast::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_ast::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(ast::QualifiedName)


def test_ast::qualifiedname_constructor_exists():
    assert callable(ast::QualifiedName.__init__)


def test_ast::qualifiedname_constructor_args():
    sig = inspect.signature(ast::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_annotatabletype_is_not_abstract():
    assert not inspect.isabstract(AnnotatableType)


def test_annotatabletype_constructor_exists():
    assert callable(AnnotatableType.__init__)


def test_annotatabletype_constructor_args():
    sig = inspect.signature(AnnotatableType.__init__)
    params = list(sig.parameters.keys())



def test_ast::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(ast::WildcardType)


def test_ast::wildcardtype_constructor_exists():
    assert callable(ast::WildcardType.__init__)


def test_ast::wildcardtype_constructor_args():
    sig = inspect.signature(ast::WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_ast::wildcardtype_has_upperBound():
    assert hasattr(ast::WildcardType, "upperBound")
    descriptor = None
    for klass in ast::WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_ast::namequalifiedtype_is_not_abstract():
    assert not inspect.isabstract(ast::NameQualifiedType)


def test_ast::namequalifiedtype_constructor_exists():
    assert callable(ast::NameQualifiedType.__init__)


def test_ast::namequalifiedtype_constructor_args():
    sig = inspect.signature(ast::NameQualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_ast::simpletype_is_not_abstract():
    assert not inspect.isabstract(ast::SimpleType)


def test_ast::simpletype_constructor_exists():
    assert callable(ast::SimpleType.__init__)


def test_ast::simpletype_constructor_args():
    sig = inspect.signature(ast::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_ast::qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(ast::QualifiedType)


def test_ast::qualifiedtype_constructor_exists():
    assert callable(ast::QualifiedType.__init__)


def test_ast::qualifiedtype_constructor_args():
    sig = inspect.signature(ast::QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_ast::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ast::PrimitiveType)


def test_ast::primitivetype_constructor_exists():
    assert callable(ast::PrimitiveType.__init__)


def test_ast::primitivetype_constructor_args():
    sig = inspect.signature(ast::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveTypeCode" in params, "Missing parameter 'primitiveTypeCode'"

def test_ast::primitivetype_has_primitiveTypeCode():
    assert hasattr(ast::PrimitiveType, "primitiveTypeCode")
    descriptor = None
    for klass in ast::PrimitiveType.__mro__:
        if "primitiveTypeCode" in klass.__dict__:
            descriptor = klass.__dict__["primitiveTypeCode"]
            break
    assert isinstance(descriptor, property)



def test_ast::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(ast::PrefixExpression)


def test_ast::prefixexpression_constructor_exists():
    assert callable(ast::PrefixExpression.__init__)


def test_ast::prefixexpression_constructor_args():
    sig = inspect.signature(ast::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::prefixexpression_has_operator():
    assert hasattr(ast::PrefixExpression, "operator")
    descriptor = None
    for klass in ast::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(ast::PostfixExpression)


def test_ast::postfixexpression_constructor_exists():
    assert callable(ast::PostfixExpression.__init__)


def test_ast::postfixexpression_constructor_args():
    sig = inspect.signature(ast::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::postfixexpression_has_operator():
    assert hasattr(ast::PostfixExpression, "operator")
    descriptor = None
    for klass in ast::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_ast::blockcomment_is_not_abstract():
    assert not inspect.isabstract(ast::BlockComment)


def test_ast::blockcomment_constructor_exists():
    assert callable(ast::BlockComment.__init__)


def test_ast::blockcomment_constructor_args():
    sig = inspect.signature(ast::BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_ast::linecomment_is_not_abstract():
    assert not inspect.isabstract(ast::LineComment)


def test_ast::linecomment_constructor_exists():
    assert callable(ast::LineComment.__init__)


def test_ast::linecomment_constructor_args():
    sig = inspect.signature(ast::LineComment.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(ast::MethodInvocation)


def test_ast::methodinvocation_constructor_exists():
    assert callable(ast::MethodInvocation.__init__)


def test_ast::methodinvocation_constructor_args():
    sig = inspect.signature(ast::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ast::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(ast::VariableDeclarationFragment)


def test_ast::variabledeclarationfragment_constructor_exists():
    assert callable(ast::VariableDeclarationFragment.__init__)


def test_ast::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(ast::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_ast::javadoc_is_not_abstract():
    assert not inspect.isabstract(ast::Javadoc)


def test_ast::javadoc_constructor_exists():
    assert callable(ast::Javadoc.__init__)


def test_ast::javadoc_constructor_args():
    sig = inspect.signature(ast::Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::initializer_is_not_abstract():
    assert not inspect.isabstract(ast::Initializer)


def test_ast::initializer_constructor_exists():
    assert callable(ast::Initializer.__init__)


def test_ast::initializer_constructor_args():
    sig = inspect.signature(ast::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_ast::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::AnnotationTypeMemberDeclaration)


def test_ast::annotationtypememberdeclaration_constructor_exists():
    assert callable(ast::AnnotationTypeMemberDeclaration.__init__)


def test_ast::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(ast::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::MethodDeclaration)


def test_ast::methoddeclaration_constructor_exists():
    assert callable(ast::MethodDeclaration.__init__)


def test_ast::methoddeclaration_constructor_args():
    sig = inspect.signature(ast::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constructor" in params, "Missing parameter 'constructor'"

def test_ast::methoddeclaration_has_constructor():
    assert hasattr(ast::MethodDeclaration, "constructor")
    descriptor = None
    for klass in ast::MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)



def test_ast::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::EnumConstantDeclaration)


def test_ast::enumconstantdeclaration_constructor_exists():
    assert callable(ast::EnumConstantDeclaration.__init__)


def test_ast::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(ast::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::FieldDeclaration)


def test_ast::fielddeclaration_constructor_exists():
    assert callable(ast::FieldDeclaration.__init__)


def test_ast::fielddeclaration_constructor_args():
    sig = inspect.signature(ast::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(ast::FieldAccess)


def test_ast::fieldaccess_constructor_exists():
    assert callable(ast::FieldAccess.__init__)


def test_ast::fieldaccess_constructor_args():
    sig = inspect.signature(ast::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast::infixexpression_is_not_abstract():
    assert not inspect.isabstract(ast::InfixExpression)


def test_ast::infixexpression_constructor_exists():
    assert callable(ast::InfixExpression.__init__)


def test_ast::infixexpression_constructor_args():
    sig = inspect.signature(ast::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::infixexpression_has_operator():
    assert hasattr(ast::InfixExpression, "operator")
    descriptor = None
    for klass in ast::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(ast::ConditionalExpression)


def test_ast::conditionalexpression_constructor_exists():
    assert callable(ast::ConditionalExpression.__init__)


def test_ast::conditionalexpression_constructor_args():
    sig = inspect.signature(ast::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::AbstractTypeDeclaration)


def test_ast::abstracttypedeclaration_constructor_exists():
    assert callable(ast::AbstractTypeDeclaration.__init__)


def test_ast::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(ast::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ast::BooleanLiteral)


def test_ast::booleanliteral_constructor_exists():
    assert callable(ast::BooleanLiteral.__init__)


def test_ast::booleanliteral_constructor_args():
    sig = inspect.signature(ast::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_ast::booleanliteral_has_booleanValue():
    assert hasattr(ast::BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in ast::BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_ast::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(ast::ClassInstanceCreation)


def test_ast::classinstancecreation_constructor_exists():
    assert callable(ast::ClassInstanceCreation.__init__)


def test_ast::classinstancecreation_constructor_args():
    sig = inspect.signature(ast::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_ast::characterliteral_is_not_abstract():
    assert not inspect.isabstract(ast::CharacterLiteral)


def test_ast::characterliteral_constructor_exists():
    assert callable(ast::CharacterLiteral.__init__)


def test_ast::characterliteral_constructor_args():
    sig = inspect.signature(ast::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_ast::characterliteral_has_escapedValue():
    assert hasattr(ast::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in ast::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_ast::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::SingleVariableDeclaration)


def test_ast::singlevariabledeclaration_constructor_exists():
    assert callable(ast::SingleVariableDeclaration.__init__)


def test_ast::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(ast::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_ast::singlevariabledeclaration_has_varargs():
    assert hasattr(ast::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in ast::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_ast::castexpression_is_not_abstract():
    assert not inspect.isabstract(ast::CastExpression)


def test_ast::castexpression_constructor_exists():
    assert callable(ast::CastExpression.__init__)


def test_ast::castexpression_constructor_args():
    sig = inspect.signature(ast::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayAccess)


def test_ast::arrayaccess_constructor_exists():
    assert callable(ast::ArrayAccess.__init__)


def test_ast::arrayaccess_constructor_args():
    sig = inspect.signature(ast::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast::assignment_is_not_abstract():
    assert not inspect.isabstract(ast::Assignment)


def test_ast::assignment_constructor_exists():
    assert callable(ast::Assignment.__init__)


def test_ast::assignment_constructor_args():
    sig = inspect.signature(ast::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::assignment_has_operator():
    assert hasattr(ast::Assignment, "operator")
    descriptor = None
    for klass in ast::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ast::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ExpressionStatement)


def test_ast::expressionstatement_constructor_exists():
    assert callable(ast::ExpressionStatement.__init__)


def test_ast::expressionstatement_constructor_args():
    sig = inspect.signature(ast::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::trystatement_is_not_abstract():
    assert not inspect.isabstract(ast::TryStatement)


def test_ast::trystatement_constructor_exists():
    assert callable(ast::TryStatement.__init__)


def test_ast::trystatement_constructor_args():
    sig = inspect.signature(ast::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::whilestatement_is_not_abstract():
    assert not inspect.isabstract(ast::WhileStatement)


def test_ast::whilestatement_constructor_exists():
    assert callable(ast::WhileStatement.__init__)


def test_ast::whilestatement_constructor_args():
    sig = inspect.signature(ast::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(ast::EnhancedForStatement)


def test_ast::enhancedforstatement_constructor_exists():
    assert callable(ast::EnhancedForStatement.__init__)


def test_ast::enhancedforstatement_constructor_args():
    sig = inspect.signature(ast::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::block_is_not_abstract():
    assert not inspect.isabstract(ast::Block)


def test_ast::block_constructor_exists():
    assert callable(ast::Block.__init__)


def test_ast::block_constructor_args():
    sig = inspect.signature(ast::Block.__init__)
    params = list(sig.parameters.keys())



def test_ast::emptystatement_is_not_abstract():
    assert not inspect.isabstract(ast::EmptyStatement)


def test_ast::emptystatement_constructor_exists():
    assert callable(ast::EmptyStatement.__init__)


def test_ast::emptystatement_constructor_args():
    sig = inspect.signature(ast::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::forstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ForStatement)


def test_ast::forstatement_constructor_exists():
    assert callable(ast::ForStatement.__init__)


def test_ast::forstatement_constructor_args():
    sig = inspect.signature(ast::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(ast::SynchronizedStatement)


def test_ast::synchronizedstatement_constructor_exists():
    assert callable(ast::SynchronizedStatement.__init__)


def test_ast::synchronizedstatement_constructor_args():
    sig = inspect.signature(ast::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::continuestatement_is_not_abstract():
    assert not inspect.isabstract(ast::ContinueStatement)


def test_ast::continuestatement_constructor_exists():
    assert callable(ast::ContinueStatement.__init__)


def test_ast::continuestatement_constructor_args():
    sig = inspect.signature(ast::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchcase_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchCase)


def test_ast::switchcase_constructor_exists():
    assert callable(ast::SwitchCase.__init__)


def test_ast::switchcase_constructor_args():
    sig = inspect.signature(ast::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_ast::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(ast::VariableDeclarationStatement)


def test_ast::variabledeclarationstatement_constructor_exists():
    assert callable(ast::VariableDeclarationStatement.__init__)


def test_ast::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(ast::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::breakstatement_is_not_abstract():
    assert not inspect.isabstract(ast::BreakStatement)


def test_ast::breakstatement_constructor_exists():
    assert callable(ast::BreakStatement.__init__)


def test_ast::breakstatement_constructor_args():
    sig = inspect.signature(ast::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::dostatement_is_not_abstract():
    assert not inspect.isabstract(ast::DoStatement)


def test_ast::dostatement_constructor_exists():
    assert callable(ast::DoStatement.__init__)


def test_ast::dostatement_constructor_args():
    sig = inspect.signature(ast::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(ast::LabeledStatement)


def test_ast::labeledstatement_constructor_exists():
    assert callable(ast::LabeledStatement.__init__)


def test_ast::labeledstatement_constructor_args():
    sig = inspect.signature(ast::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::ifstatement_is_not_abstract():
    assert not inspect.isabstract(ast::IfStatement)


def test_ast::ifstatement_constructor_exists():
    assert callable(ast::IfStatement.__init__)


def test_ast::ifstatement_constructor_args():
    sig = inspect.signature(ast::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(ast::ConstructorInvocation)


def test_ast::constructorinvocation_constructor_exists():
    assert callable(ast::ConstructorInvocation.__init__)


def test_ast::constructorinvocation_constructor_args():
    sig = inspect.signature(ast::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ast::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(ast::SuperConstructorInvocation)


def test_ast::superconstructorinvocation_constructor_exists():
    assert callable(ast::SuperConstructorInvocation.__init__)


def test_ast::superconstructorinvocation_constructor_args():
    sig = inspect.signature(ast::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ast::throwstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ThrowStatement)


def test_ast::throwstatement_constructor_exists():
    assert callable(ast::ThrowStatement.__init__)


def test_ast::throwstatement_constructor_args():
    sig = inspect.signature(ast::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::returnstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ReturnStatement)


def test_ast::returnstatement_constructor_exists():
    assert callable(ast::ReturnStatement.__init__)


def test_ast::returnstatement_constructor_args():
    sig = inspect.signature(ast::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchstatement_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchStatement)


def test_ast::switchstatement_constructor_exists():
    assert callable(ast::SwitchStatement.__init__)


def test_ast::switchstatement_constructor_args():
    sig = inspect.signature(ast::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(ast::TypeDeclarationStatement)


def test_ast::typedeclarationstatement_constructor_exists():
    assert callable(ast::TypeDeclarationStatement.__init__)


def test_ast::typedeclarationstatement_constructor_args():
    sig = inspect.signature(ast::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::assertstatement_is_not_abstract():
    assert not inspect.isabstract(ast::AssertStatement)


def test_ast::assertstatement_constructor_exists():
    assert callable(ast::AssertStatement.__init__)


def test_ast::assertstatement_constructor_args():
    sig = inspect.signature(ast::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ast::uniontype_is_not_abstract():
    assert not inspect.isabstract(ast::UnionType)


def test_ast::uniontype_constructor_exists():
    assert callable(ast::UnionType.__init__)


def test_ast::uniontype_constructor_args():
    sig = inspect.signature(ast::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_ast::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ast::ParameterizedType)


def test_ast::parameterizedtype_constructor_exists():
    assert callable(ast::ParameterizedType.__init__)


def test_ast::parameterizedtype_constructor_args():
    sig = inspect.signature(ast::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_ast::intersectiontype_is_not_abstract():
    assert not inspect.isabstract(ast::IntersectionType)


def test_ast::intersectiontype_constructor_exists():
    assert callable(ast::IntersectionType.__init__)


def test_ast::intersectiontype_constructor_args():
    sig = inspect.signature(ast::IntersectionType.__init__)
    params = list(sig.parameters.keys())



def test_ast::annotatabletype_is_not_abstract():
    assert not inspect.isabstract(ast::AnnotatableType)


def test_ast::annotatabletype_constructor_exists():
    assert callable(ast::AnnotatableType.__init__)


def test_ast::annotatabletype_constructor_args():
    sig = inspect.signature(ast::AnnotatableType.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayInitializer)


def test_ast::arrayinitializer_constructor_exists():
    assert callable(ast::ArrayInitializer.__init__)


def test_ast::arrayinitializer_constructor_args():
    sig = inspect.signature(ast::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_ast::arraytype_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayType)


def test_ast::arraytype_constructor_exists():
    assert callable(ast::ArrayType.__init__)


def test_ast::arraytype_constructor_args():
    sig = inspect.signature(ast::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_ast::arraycreation_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayCreation)


def test_ast::arraycreation_constructor_exists():
    assert callable(ast::ArrayCreation.__init__)


def test_ast::arraycreation_constructor_args():
    sig = inspect.signature(ast::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_iextendedmodifier_is_not_abstract():
    assert not inspect.isabstract(IExtendedModifier)


def test_iextendedmodifier_constructor_exists():
    assert callable(IExtendedModifier.__init__)


def test_iextendedmodifier_constructor_args():
    sig = inspect.signature(IExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_ast::annotation_is_not_abstract():
    assert not inspect.isabstract(ast::Annotation)


def test_ast::annotation_constructor_exists():
    assert callable(ast::Annotation.__init__)


def test_ast::annotation_constructor_args():
    sig = inspect.signature(ast::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_ast::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::PackageDeclaration)


def test_ast::packagedeclaration_constructor_exists():
    assert callable(ast::PackageDeclaration.__init__)


def test_ast::packagedeclaration_constructor_args():
    sig = inspect.signature(ast::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::expression_is_not_abstract():
    assert not inspect.isabstract(ast::Expression)


def test_ast::expression_constructor_exists():
    assert callable(ast::Expression.__init__)


def test_ast::expression_constructor_args():
    sig = inspect.signature(ast::Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::ImportDeclaration)


def test_ast::importdeclaration_constructor_exists():
    assert callable(ast::ImportDeclaration.__init__)


def test_ast::importdeclaration_constructor_args():
    sig = inspect.signature(ast::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "onDemand" in params, "Missing parameter 'onDemand'"

def test_ast::importdeclaration_has_static():
    assert hasattr(ast::ImportDeclaration, "static")
    descriptor = None
    for klass in ast::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_ast::importdeclaration_has_onDemand():
    assert hasattr(ast::ImportDeclaration, "onDemand")
    descriptor = None
    for klass in ast::ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)



def test_ast::dimension_is_not_abstract():
    assert not inspect.isabstract(ast::Dimension)


def test_ast::dimension_constructor_exists():
    assert callable(ast::Dimension.__init__)


def test_ast::dimension_constructor_args():
    sig = inspect.signature(ast::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_ast::catchclause_is_not_abstract():
    assert not inspect.isabstract(ast::CatchClause)


def test_ast::catchclause_constructor_exists():
    assert callable(ast::CatchClause.__init__)


def test_ast::catchclause_constructor_args():
    sig = inspect.signature(ast::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_ast::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::BodyDeclaration)


def test_ast::bodydeclaration_constructor_exists():
    assert callable(ast::BodyDeclaration.__init__)


def test_ast::bodydeclaration_constructor_args():
    sig = inspect.signature(ast::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::AnonymousClassDeclaration)


def test_ast::anonymousclassdeclaration_constructor_exists():
    assert callable(ast::AnonymousClassDeclaration.__init__)


def test_ast::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(ast::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::type_is_not_abstract():
    assert not inspect.isabstract(ast::Type)


def test_ast::type_constructor_exists():
    assert callable(ast::Type.__init__)


def test_ast::type_constructor_args():
    sig = inspect.signature(ast::Type.__init__)
    params = list(sig.parameters.keys())



def test_ast::comment_is_not_abstract():
    assert not inspect.isabstract(ast::Comment)


def test_ast::comment_constructor_exists():
    assert callable(ast::Comment.__init__)


def test_ast::comment_constructor_args():
    sig = inspect.signature(ast::Comment.__init__)
    params = list(sig.parameters.keys())



def test_ast::statement_is_not_abstract():
    assert not inspect.isabstract(ast::Statement)


def test_ast::statement_constructor_exists():
    assert callable(ast::Statement.__init__)


def test_ast::statement_constructor_args():
    sig = inspect.signature(ast::Statement.__init__)
    params = list(sig.parameters.keys())



def test_ast::typeparameter_is_not_abstract():
    assert not inspect.isabstract(ast::TypeParameter)


def test_ast::typeparameter_constructor_exists():
    assert callable(ast::TypeParameter.__init__)


def test_ast::typeparameter_constructor_args():
    sig = inspect.signature(ast::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_ast::compilationunit_is_not_abstract():
    assert not inspect.isabstract(ast::CompilationUnit)


def test_ast::compilationunit_constructor_exists():
    assert callable(ast::CompilationUnit.__init__)


def test_ast::compilationunit_constructor_args():
    sig = inspect.signature(ast::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_ast::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::VariableDeclaration)


def test_ast::variabledeclaration_constructor_exists():
    assert callable(ast::VariableDeclaration.__init__)


def test_ast::variabledeclaration_constructor_args():
    sig = inspect.signature(ast::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::modifier_is_not_abstract():
    assert not inspect.isabstract(ast::Modifier)


def test_ast::modifier_constructor_exists():
    assert callable(ast::Modifier.__init__)


def test_ast::modifier_constructor_args():
    sig = inspect.signature(ast::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_ast::modifier_has_keyword():
    assert hasattr(ast::Modifier, "keyword")
    descriptor = None
    for klass in ast::Modifier.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_ast::iextendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ast::IExtendedModifier)


def test_ast::iextendedmodifier_constructor_exists():
    assert callable(ast::IExtendedModifier.__init__)


def test_ast::iextendedmodifier_constructor_args():
    sig = inspect.signature(ast::IExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(ast::MethodRefParameter)


def test_ast::methodrefparameter_constructor_exists():
    assert callable(ast::MethodRefParameter.__init__)


def test_ast::methodrefparameter_constructor_args():
    sig = inspect.signature(ast::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_ast::methodrefparameter_has_varargs():
    assert hasattr(ast::MethodRefParameter, "varargs")
    descriptor = None
    for klass in ast::MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_ast::simplename_is_not_abstract():
    assert not inspect.isabstract(ast::SimpleName)


def test_ast::simplename_constructor_exists():
    assert callable(ast::SimpleName.__init__)


def test_ast::simplename_constructor_args():
    sig = inspect.signature(ast::SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ast::simplename_has_identifier():
    assert hasattr(ast::SimpleName, "identifier")
    descriptor = None
    for klass in ast::SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_idocelement_is_not_abstract():
    assert not inspect.isabstract(IDocElement)


def test_idocelement_constructor_exists():
    assert callable(IDocElement.__init__)


def test_idocelement_constructor_args():
    sig = inspect.signature(IDocElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::name_is_not_abstract():
    assert not inspect.isabstract(ast::Name)


def test_ast::name_constructor_exists():
    assert callable(ast::Name.__init__)


def test_ast::name_constructor_args():
    sig = inspect.signature(ast::Name.__init__)
    params = list(sig.parameters.keys())



def test_ast::tagelement_is_not_abstract():
    assert not inspect.isabstract(ast::TagElement)


def test_ast::tagelement_constructor_exists():
    assert callable(ast::TagElement.__init__)


def test_ast::tagelement_constructor_args():
    sig = inspect.signature(ast::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_ast::tagelement_has_tagName():
    assert hasattr(ast::TagElement, "tagName")
    descriptor = None
    for klass in ast::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_ast::methodref_is_not_abstract():
    assert not inspect.isabstract(ast::MethodRef)


def test_ast::methodref_constructor_exists():
    assert callable(ast::MethodRef.__init__)


def test_ast::methodref_constructor_args():
    sig = inspect.signature(ast::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_ast::textelement_is_not_abstract():
    assert not inspect.isabstract(ast::TextElement)


def test_ast::textelement_constructor_exists():
    assert callable(ast::TextElement.__init__)


def test_ast::textelement_constructor_args():
    sig = inspect.signature(ast::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ast::textelement_has_text():
    assert hasattr(ast::TextElement, "text")
    descriptor = None
    for klass in ast::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ast::memberref_is_not_abstract():
    assert not inspect.isabstract(ast::MemberRef)


def test_ast::memberref_constructor_exists():
    assert callable(ast::MemberRef.__init__)


def test_ast::memberref_constructor_args():
    sig = inspect.signature(ast::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_ast::idocelement_is_not_abstract():
    assert not inspect.isabstract(ast::IDocElement)


def test_ast::idocelement_constructor_exists():
    assert callable(ast::IDocElement.__init__)


def test_ast::idocelement_constructor_args():
    sig = inspect.signature(ast::IDocElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(ast::SingleMemberAnnotation)


def test_ast::singlememberannotation_constructor_exists():
    assert callable(ast::SingleMemberAnnotation.__init__)


def test_ast::singlememberannotation_constructor_args():
    sig = inspect.signature(ast::SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_ast::membervaluepair_is_not_abstract():
    assert not inspect.isabstract(ast::MemberValuePair)


def test_ast::membervaluepair_constructor_exists():
    assert callable(ast::MemberValuePair.__init__)


def test_ast::membervaluepair_constructor_args():
    sig = inspect.signature(ast::MemberValuePair.__init__)
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
Annotation_strategy = st.builds(
    Annotation,
)
ast::NormalAnnotation_strategy = st.builds(
    ast::NormalAnnotation,
)
ast::MarkerAnnotation_strategy = st.builds(
    ast::MarkerAnnotation,
)
ast::ASTNode_strategy = st.builds(
    ast::ASTNode,
)
ast::MethodReference_strategy = st.builds(
    ast::MethodReference,
)
MethodReference_strategy = st.builds(
    MethodReference,
)
ast::SuperMethodReference_strategy = st.builds(
    ast::SuperMethodReference,
)
ast::ExpressionMethodReference_strategy = st.builds(
    ast::ExpressionMethodReference,
)
ast::TypeMethodReference_strategy = st.builds(
    ast::TypeMethodReference,
)
ast::CreationReference_strategy = st.builds(
    ast::CreationReference,
)
ast::LambdaExpression_strategy = st.builds(
    ast::LambdaExpression,
    parentheses=
        st.booleans()
)
ast::InstanceofExpression_strategy = st.builds(
    ast::InstanceofExpression,
)
ast::TypeLiteral_strategy = st.builds(
    ast::TypeLiteral,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
ast::EnumDeclaration_strategy = st.builds(
    ast::EnumDeclaration,
)
ast::AnnotationTypeDeclaration_strategy = st.builds(
    ast::AnnotationTypeDeclaration,
)
ast::TypeDeclaration_strategy = st.builds(
    ast::TypeDeclaration,
    interface=
        st.booleans()
)
ast::VariableDeclarationExpression_strategy = st.builds(
    ast::VariableDeclarationExpression,
)
ast::ThisExpression_strategy = st.builds(
    ast::ThisExpression,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
ast::SuperMethodInvocation_strategy = st.builds(
    ast::SuperMethodInvocation,
)
ast::SuperFieldAccess_strategy = st.builds(
    ast::SuperFieldAccess,
)
ast::StringLiteral_strategy = st.builds(
    ast::StringLiteral,
    escapedValue=
        safe_text
)
ast::ParenthesizedExpression_strategy = st.builds(
    ast::ParenthesizedExpression,
)
ast::NumberLiteral_strategy = st.builds(
    ast::NumberLiteral,
    token=
        safe_text
)
ast::NullLiteral_strategy = st.builds(
    ast::NullLiteral,
)
Name_strategy = st.builds(
    Name,
)
ast::QualifiedName_strategy = st.builds(
    ast::QualifiedName,
)
AnnotatableType_strategy = st.builds(
    AnnotatableType,
)
ast::WildcardType_strategy = st.builds(
    ast::WildcardType,
    upperBound=
        st.booleans()
)
ast::NameQualifiedType_strategy = st.builds(
    ast::NameQualifiedType,
)
ast::SimpleType_strategy = st.builds(
    ast::SimpleType,
)
ast::QualifiedType_strategy = st.builds(
    ast::QualifiedType,
)
ast::PrimitiveType_strategy = st.builds(
    ast::PrimitiveType,
    primitiveTypeCode=
        safe_text
)
ast::PrefixExpression_strategy = st.builds(
    ast::PrefixExpression,
    operator=
        safe_text
)
ast::PostfixExpression_strategy = st.builds(
    ast::PostfixExpression,
    operator=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
ast::BlockComment_strategy = st.builds(
    ast::BlockComment,
)
ast::LineComment_strategy = st.builds(
    ast::LineComment,
)
ast::MethodInvocation_strategy = st.builds(
    ast::MethodInvocation,
)
ast::VariableDeclarationFragment_strategy = st.builds(
    ast::VariableDeclarationFragment,
)
ast::Javadoc_strategy = st.builds(
    ast::Javadoc,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
ast::Initializer_strategy = st.builds(
    ast::Initializer,
)
ast::AnnotationTypeMemberDeclaration_strategy = st.builds(
    ast::AnnotationTypeMemberDeclaration,
)
ast::MethodDeclaration_strategy = st.builds(
    ast::MethodDeclaration,
    constructor=
        st.booleans()
)
ast::EnumConstantDeclaration_strategy = st.builds(
    ast::EnumConstantDeclaration,
)
ast::FieldDeclaration_strategy = st.builds(
    ast::FieldDeclaration,
)
ast::FieldAccess_strategy = st.builds(
    ast::FieldAccess,
)
ast::InfixExpression_strategy = st.builds(
    ast::InfixExpression,
    operator=
        safe_text
)
ast::ConditionalExpression_strategy = st.builds(
    ast::ConditionalExpression,
)
ast::AbstractTypeDeclaration_strategy = st.builds(
    ast::AbstractTypeDeclaration,
)
ast::BooleanLiteral_strategy = st.builds(
    ast::BooleanLiteral,
    booleanValue=
        st.booleans()
)
ast::ClassInstanceCreation_strategy = st.builds(
    ast::ClassInstanceCreation,
)
ast::CharacterLiteral_strategy = st.builds(
    ast::CharacterLiteral,
    escapedValue=
        safe_text
)
ast::SingleVariableDeclaration_strategy = st.builds(
    ast::SingleVariableDeclaration,
    varargs=
        st.booleans()
)
ast::CastExpression_strategy = st.builds(
    ast::CastExpression,
)
ast::ArrayAccess_strategy = st.builds(
    ast::ArrayAccess,
)
ast::Assignment_strategy = st.builds(
    ast::Assignment,
    operator=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
ast::ExpressionStatement_strategy = st.builds(
    ast::ExpressionStatement,
)
ast::TryStatement_strategy = st.builds(
    ast::TryStatement,
)
ast::WhileStatement_strategy = st.builds(
    ast::WhileStatement,
)
ast::EnhancedForStatement_strategy = st.builds(
    ast::EnhancedForStatement,
)
ast::Block_strategy = st.builds(
    ast::Block,
)
ast::EmptyStatement_strategy = st.builds(
    ast::EmptyStatement,
)
ast::ForStatement_strategy = st.builds(
    ast::ForStatement,
)
ast::SynchronizedStatement_strategy = st.builds(
    ast::SynchronizedStatement,
)
ast::ContinueStatement_strategy = st.builds(
    ast::ContinueStatement,
)
ast::SwitchCase_strategy = st.builds(
    ast::SwitchCase,
)
ast::VariableDeclarationStatement_strategy = st.builds(
    ast::VariableDeclarationStatement,
)
ast::BreakStatement_strategy = st.builds(
    ast::BreakStatement,
)
ast::DoStatement_strategy = st.builds(
    ast::DoStatement,
)
ast::LabeledStatement_strategy = st.builds(
    ast::LabeledStatement,
)
ast::IfStatement_strategy = st.builds(
    ast::IfStatement,
)
ast::ConstructorInvocation_strategy = st.builds(
    ast::ConstructorInvocation,
)
ast::SuperConstructorInvocation_strategy = st.builds(
    ast::SuperConstructorInvocation,
)
ast::ThrowStatement_strategy = st.builds(
    ast::ThrowStatement,
)
ast::ReturnStatement_strategy = st.builds(
    ast::ReturnStatement,
)
ast::SwitchStatement_strategy = st.builds(
    ast::SwitchStatement,
)
ast::TypeDeclarationStatement_strategy = st.builds(
    ast::TypeDeclarationStatement,
)
ast::AssertStatement_strategy = st.builds(
    ast::AssertStatement,
)
Type_strategy = st.builds(
    Type,
)
ast::UnionType_strategy = st.builds(
    ast::UnionType,
)
ast::ParameterizedType_strategy = st.builds(
    ast::ParameterizedType,
)
ast::IntersectionType_strategy = st.builds(
    ast::IntersectionType,
)
ast::AnnotatableType_strategy = st.builds(
    ast::AnnotatableType,
)
ast::ArrayInitializer_strategy = st.builds(
    ast::ArrayInitializer,
)
ast::ArrayType_strategy = st.builds(
    ast::ArrayType,
)
ast::ArrayCreation_strategy = st.builds(
    ast::ArrayCreation,
)
IExtendedModifier_strategy = st.builds(
    IExtendedModifier,
)
ast::Annotation_strategy = st.builds(
    ast::Annotation,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
ast::PackageDeclaration_strategy = st.builds(
    ast::PackageDeclaration,
)
ast::Expression_strategy = st.builds(
    ast::Expression,
)
ast::ImportDeclaration_strategy = st.builds(
    ast::ImportDeclaration,
    static=
        st.booleans(),
    onDemand=
        st.booleans()
)
ast::Dimension_strategy = st.builds(
    ast::Dimension,
)
ast::CatchClause_strategy = st.builds(
    ast::CatchClause,
)
ast::BodyDeclaration_strategy = st.builds(
    ast::BodyDeclaration,
)
ast::AnonymousClassDeclaration_strategy = st.builds(
    ast::AnonymousClassDeclaration,
)
ast::Type_strategy = st.builds(
    ast::Type,
)
ast::Comment_strategy = st.builds(
    ast::Comment,
)
ast::Statement_strategy = st.builds(
    ast::Statement,
)
ast::TypeParameter_strategy = st.builds(
    ast::TypeParameter,
)
ast::CompilationUnit_strategy = st.builds(
    ast::CompilationUnit,
)
ast::VariableDeclaration_strategy = st.builds(
    ast::VariableDeclaration,
)
ast::Modifier_strategy = st.builds(
    ast::Modifier,
    keyword=
        safe_text
)
ast::IExtendedModifier_strategy = st.builds(
    ast::IExtendedModifier,
)
ast::MethodRefParameter_strategy = st.builds(
    ast::MethodRefParameter,
    varargs=
        st.booleans()
)
ast::SimpleName_strategy = st.builds(
    ast::SimpleName,
    identifier=
        safe_text
)
IDocElement_strategy = st.builds(
    IDocElement,
)
ast::Name_strategy = st.builds(
    ast::Name,
)
ast::TagElement_strategy = st.builds(
    ast::TagElement,
    tagName=
        safe_text
)
ast::MethodRef_strategy = st.builds(
    ast::MethodRef,
)
ast::TextElement_strategy = st.builds(
    ast::TextElement,
    text=
        safe_text
)
ast::MemberRef_strategy = st.builds(
    ast::MemberRef,
)
ast::IDocElement_strategy = st.builds(
    ast::IDocElement,
)
ast::SingleMemberAnnotation_strategy = st.builds(
    ast::SingleMemberAnnotation,
)
ast::MemberValuePair_strategy = st.builds(
    ast::MemberValuePair,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=ast::NormalAnnotation_strategy)
@settings(max_examples=50)
def test_ast::normalannotation_instantiation(instance):
    assert isinstance(instance, ast::NormalAnnotation)

@given(instance=ast::MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_ast::markerannotation_instantiation(instance):
    assert isinstance(instance, ast::MarkerAnnotation)

@given(instance=ast::ASTNode_strategy)
@settings(max_examples=50)
def test_ast::astnode_instantiation(instance):
    assert isinstance(instance, ast::ASTNode)

@given(instance=ast::MethodReference_strategy)
@settings(max_examples=50)
def test_ast::methodreference_instantiation(instance):
    assert isinstance(instance, ast::MethodReference)

@given(instance=MethodReference_strategy)
@settings(max_examples=50)
def test_methodreference_instantiation(instance):
    assert isinstance(instance, MethodReference)

@given(instance=ast::SuperMethodReference_strategy)
@settings(max_examples=50)
def test_ast::supermethodreference_instantiation(instance):
    assert isinstance(instance, ast::SuperMethodReference)

@given(instance=ast::ExpressionMethodReference_strategy)
@settings(max_examples=50)
def test_ast::expressionmethodreference_instantiation(instance):
    assert isinstance(instance, ast::ExpressionMethodReference)

@given(instance=ast::TypeMethodReference_strategy)
@settings(max_examples=50)
def test_ast::typemethodreference_instantiation(instance):
    assert isinstance(instance, ast::TypeMethodReference)

@given(instance=ast::CreationReference_strategy)
@settings(max_examples=50)
def test_ast::creationreference_instantiation(instance):
    assert isinstance(instance, ast::CreationReference)

@given(instance=ast::LambdaExpression_strategy)
@settings(max_examples=50)
def test_ast::lambdaexpression_instantiation(instance):
    assert isinstance(instance, ast::LambdaExpression)

@given(instance=ast::LambdaExpression_strategy)
def test_ast::lambdaexpression_parentheses_type(instance):
    assert isinstance(instance.parentheses, bool)


@given(instance=ast::LambdaExpression_strategy)
def test_ast::lambdaexpression_parentheses_setter(instance):
    original = instance.parentheses
    instance.parentheses = original
    assert instance.parentheses == original

@given(instance=ast::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_ast::instanceofexpression_instantiation(instance):
    assert isinstance(instance, ast::InstanceofExpression)

@given(instance=ast::TypeLiteral_strategy)
@settings(max_examples=50)
def test_ast::typeliteral_instantiation(instance):
    assert isinstance(instance, ast::TypeLiteral)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=ast::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_ast::enumdeclaration_instantiation(instance):
    assert isinstance(instance, ast::EnumDeclaration)

@given(instance=ast::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_ast::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, ast::AnnotationTypeDeclaration)

@given(instance=ast::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_ast::typedeclaration_instantiation(instance):
    assert isinstance(instance, ast::TypeDeclaration)

@given(instance=ast::TypeDeclaration_strategy)
def test_ast::typedeclaration_interface_type(instance):
    assert isinstance(instance.interface, bool)


@given(instance=ast::TypeDeclaration_strategy)
def test_ast::typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=ast::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_ast::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, ast::VariableDeclarationExpression)

@given(instance=ast::ThisExpression_strategy)
@settings(max_examples=50)
def test_ast::thisexpression_instantiation(instance):
    assert isinstance(instance, ast::ThisExpression)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=ast::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_ast::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, ast::SuperMethodInvocation)

@given(instance=ast::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_ast::superfieldaccess_instantiation(instance):
    assert isinstance(instance, ast::SuperFieldAccess)

@given(instance=ast::StringLiteral_strategy)
@settings(max_examples=50)
def test_ast::stringliteral_instantiation(instance):
    assert isinstance(instance, ast::StringLiteral)

@given(instance=ast::StringLiteral_strategy)
def test_ast::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=ast::StringLiteral_strategy)
def test_ast::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=ast::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_ast::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ast::ParenthesizedExpression)

@given(instance=ast::NumberLiteral_strategy)
@settings(max_examples=50)
def test_ast::numberliteral_instantiation(instance):
    assert isinstance(instance, ast::NumberLiteral)

@given(instance=ast::NumberLiteral_strategy)
def test_ast::numberliteral_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=ast::NumberLiteral_strategy)
def test_ast::numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=ast::NullLiteral_strategy)
@settings(max_examples=50)
def test_ast::nullliteral_instantiation(instance):
    assert isinstance(instance, ast::NullLiteral)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=ast::QualifiedName_strategy)
@settings(max_examples=50)
def test_ast::qualifiedname_instantiation(instance):
    assert isinstance(instance, ast::QualifiedName)

@given(instance=AnnotatableType_strategy)
@settings(max_examples=50)
def test_annotatabletype_instantiation(instance):
    assert isinstance(instance, AnnotatableType)

@given(instance=ast::WildcardType_strategy)
@settings(max_examples=50)
def test_ast::wildcardtype_instantiation(instance):
    assert isinstance(instance, ast::WildcardType)

@given(instance=ast::WildcardType_strategy)
def test_ast::wildcardtype_upperBound_type(instance):
    assert isinstance(instance.upperBound, bool)


@given(instance=ast::WildcardType_strategy)
def test_ast::wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=ast::NameQualifiedType_strategy)
@settings(max_examples=50)
def test_ast::namequalifiedtype_instantiation(instance):
    assert isinstance(instance, ast::NameQualifiedType)

@given(instance=ast::SimpleType_strategy)
@settings(max_examples=50)
def test_ast::simpletype_instantiation(instance):
    assert isinstance(instance, ast::SimpleType)

@given(instance=ast::QualifiedType_strategy)
@settings(max_examples=50)
def test_ast::qualifiedtype_instantiation(instance):
    assert isinstance(instance, ast::QualifiedType)

@given(instance=ast::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ast::primitivetype_instantiation(instance):
    assert isinstance(instance, ast::PrimitiveType)

@given(instance=ast::PrimitiveType_strategy)
def test_ast::primitivetype_primitiveTypeCode_type(instance):
    assert isinstance(instance.primitiveTypeCode, str)


@given(instance=ast::PrimitiveType_strategy)
def test_ast::primitivetype_primitiveTypeCode_setter(instance):
    original = instance.primitiveTypeCode
    instance.primitiveTypeCode = original
    assert instance.primitiveTypeCode == original

@given(instance=ast::PrefixExpression_strategy)
@settings(max_examples=50)
def test_ast::prefixexpression_instantiation(instance):
    assert isinstance(instance, ast::PrefixExpression)

@given(instance=ast::PrefixExpression_strategy)
def test_ast::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::PrefixExpression_strategy)
def test_ast::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::PostfixExpression_strategy)
@settings(max_examples=50)
def test_ast::postfixexpression_instantiation(instance):
    assert isinstance(instance, ast::PostfixExpression)

@given(instance=ast::PostfixExpression_strategy)
def test_ast::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::PostfixExpression_strategy)
def test_ast::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=ast::BlockComment_strategy)
@settings(max_examples=50)
def test_ast::blockcomment_instantiation(instance):
    assert isinstance(instance, ast::BlockComment)

@given(instance=ast::LineComment_strategy)
@settings(max_examples=50)
def test_ast::linecomment_instantiation(instance):
    assert isinstance(instance, ast::LineComment)

@given(instance=ast::MethodInvocation_strategy)
@settings(max_examples=50)
def test_ast::methodinvocation_instantiation(instance):
    assert isinstance(instance, ast::MethodInvocation)

@given(instance=ast::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_ast::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, ast::VariableDeclarationFragment)

@given(instance=ast::Javadoc_strategy)
@settings(max_examples=50)
def test_ast::javadoc_instantiation(instance):
    assert isinstance(instance, ast::Javadoc)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=ast::Initializer_strategy)
@settings(max_examples=50)
def test_ast::initializer_instantiation(instance):
    assert isinstance(instance, ast::Initializer)

@given(instance=ast::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_ast::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, ast::AnnotationTypeMemberDeclaration)

@given(instance=ast::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_ast::methoddeclaration_instantiation(instance):
    assert isinstance(instance, ast::MethodDeclaration)

@given(instance=ast::MethodDeclaration_strategy)
def test_ast::methoddeclaration_constructor_type(instance):
    assert isinstance(instance.constructor, bool)


@given(instance=ast::MethodDeclaration_strategy)
def test_ast::methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=ast::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_ast::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, ast::EnumConstantDeclaration)

@given(instance=ast::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_ast::fielddeclaration_instantiation(instance):
    assert isinstance(instance, ast::FieldDeclaration)

@given(instance=ast::FieldAccess_strategy)
@settings(max_examples=50)
def test_ast::fieldaccess_instantiation(instance):
    assert isinstance(instance, ast::FieldAccess)

@given(instance=ast::InfixExpression_strategy)
@settings(max_examples=50)
def test_ast::infixexpression_instantiation(instance):
    assert isinstance(instance, ast::InfixExpression)

@given(instance=ast::InfixExpression_strategy)
def test_ast::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::InfixExpression_strategy)
def test_ast::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_ast::conditionalexpression_instantiation(instance):
    assert isinstance(instance, ast::ConditionalExpression)

@given(instance=ast::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_ast::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, ast::AbstractTypeDeclaration)

@given(instance=ast::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ast::booleanliteral_instantiation(instance):
    assert isinstance(instance, ast::BooleanLiteral)

@given(instance=ast::BooleanLiteral_strategy)
def test_ast::booleanliteral_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, bool)


@given(instance=ast::BooleanLiteral_strategy)
def test_ast::booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=ast::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_ast::classinstancecreation_instantiation(instance):
    assert isinstance(instance, ast::ClassInstanceCreation)

@given(instance=ast::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_ast::characterliteral_instantiation(instance):
    assert isinstance(instance, ast::CharacterLiteral)

@given(instance=ast::CharacterLiteral_strategy)
def test_ast::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=ast::CharacterLiteral_strategy)
def test_ast::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=ast::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, ast::SingleVariableDeclaration)

@given(instance=ast::SingleVariableDeclaration_strategy)
def test_ast::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=ast::SingleVariableDeclaration_strategy)
def test_ast::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=ast::CastExpression_strategy)
@settings(max_examples=50)
def test_ast::castexpression_instantiation(instance):
    assert isinstance(instance, ast::CastExpression)

@given(instance=ast::ArrayAccess_strategy)
@settings(max_examples=50)
def test_ast::arrayaccess_instantiation(instance):
    assert isinstance(instance, ast::ArrayAccess)

@given(instance=ast::Assignment_strategy)
@settings(max_examples=50)
def test_ast::assignment_instantiation(instance):
    assert isinstance(instance, ast::Assignment)

@given(instance=ast::Assignment_strategy)
def test_ast::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::Assignment_strategy)
def test_ast::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ast::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_ast::expressionstatement_instantiation(instance):
    assert isinstance(instance, ast::ExpressionStatement)

@given(instance=ast::TryStatement_strategy)
@settings(max_examples=50)
def test_ast::trystatement_instantiation(instance):
    assert isinstance(instance, ast::TryStatement)

@given(instance=ast::WhileStatement_strategy)
@settings(max_examples=50)
def test_ast::whilestatement_instantiation(instance):
    assert isinstance(instance, ast::WhileStatement)

@given(instance=ast::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_ast::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, ast::EnhancedForStatement)

@given(instance=ast::Block_strategy)
@settings(max_examples=50)
def test_ast::block_instantiation(instance):
    assert isinstance(instance, ast::Block)

@given(instance=ast::EmptyStatement_strategy)
@settings(max_examples=50)
def test_ast::emptystatement_instantiation(instance):
    assert isinstance(instance, ast::EmptyStatement)

@given(instance=ast::ForStatement_strategy)
@settings(max_examples=50)
def test_ast::forstatement_instantiation(instance):
    assert isinstance(instance, ast::ForStatement)

@given(instance=ast::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_ast::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, ast::SynchronizedStatement)

@given(instance=ast::ContinueStatement_strategy)
@settings(max_examples=50)
def test_ast::continuestatement_instantiation(instance):
    assert isinstance(instance, ast::ContinueStatement)

@given(instance=ast::SwitchCase_strategy)
@settings(max_examples=50)
def test_ast::switchcase_instantiation(instance):
    assert isinstance(instance, ast::SwitchCase)

@given(instance=ast::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_ast::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, ast::VariableDeclarationStatement)

@given(instance=ast::BreakStatement_strategy)
@settings(max_examples=50)
def test_ast::breakstatement_instantiation(instance):
    assert isinstance(instance, ast::BreakStatement)

@given(instance=ast::DoStatement_strategy)
@settings(max_examples=50)
def test_ast::dostatement_instantiation(instance):
    assert isinstance(instance, ast::DoStatement)

@given(instance=ast::LabeledStatement_strategy)
@settings(max_examples=50)
def test_ast::labeledstatement_instantiation(instance):
    assert isinstance(instance, ast::LabeledStatement)

@given(instance=ast::IfStatement_strategy)
@settings(max_examples=50)
def test_ast::ifstatement_instantiation(instance):
    assert isinstance(instance, ast::IfStatement)

@given(instance=ast::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_ast::constructorinvocation_instantiation(instance):
    assert isinstance(instance, ast::ConstructorInvocation)

@given(instance=ast::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_ast::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, ast::SuperConstructorInvocation)

@given(instance=ast::ThrowStatement_strategy)
@settings(max_examples=50)
def test_ast::throwstatement_instantiation(instance):
    assert isinstance(instance, ast::ThrowStatement)

@given(instance=ast::ReturnStatement_strategy)
@settings(max_examples=50)
def test_ast::returnstatement_instantiation(instance):
    assert isinstance(instance, ast::ReturnStatement)

@given(instance=ast::SwitchStatement_strategy)
@settings(max_examples=50)
def test_ast::switchstatement_instantiation(instance):
    assert isinstance(instance, ast::SwitchStatement)

@given(instance=ast::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_ast::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, ast::TypeDeclarationStatement)

@given(instance=ast::AssertStatement_strategy)
@settings(max_examples=50)
def test_ast::assertstatement_instantiation(instance):
    assert isinstance(instance, ast::AssertStatement)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ast::UnionType_strategy)
@settings(max_examples=50)
def test_ast::uniontype_instantiation(instance):
    assert isinstance(instance, ast::UnionType)

@given(instance=ast::ParameterizedType_strategy)
@settings(max_examples=50)
def test_ast::parameterizedtype_instantiation(instance):
    assert isinstance(instance, ast::ParameterizedType)

@given(instance=ast::IntersectionType_strategy)
@settings(max_examples=50)
def test_ast::intersectiontype_instantiation(instance):
    assert isinstance(instance, ast::IntersectionType)

@given(instance=ast::AnnotatableType_strategy)
@settings(max_examples=50)
def test_ast::annotatabletype_instantiation(instance):
    assert isinstance(instance, ast::AnnotatableType)

@given(instance=ast::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_ast::arrayinitializer_instantiation(instance):
    assert isinstance(instance, ast::ArrayInitializer)

@given(instance=ast::ArrayType_strategy)
@settings(max_examples=50)
def test_ast::arraytype_instantiation(instance):
    assert isinstance(instance, ast::ArrayType)

@given(instance=ast::ArrayCreation_strategy)
@settings(max_examples=50)
def test_ast::arraycreation_instantiation(instance):
    assert isinstance(instance, ast::ArrayCreation)

@given(instance=IExtendedModifier_strategy)
@settings(max_examples=50)
def test_iextendedmodifier_instantiation(instance):
    assert isinstance(instance, IExtendedModifier)

@given(instance=ast::Annotation_strategy)
@settings(max_examples=50)
def test_ast::annotation_instantiation(instance):
    assert isinstance(instance, ast::Annotation)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=ast::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_ast::packagedeclaration_instantiation(instance):
    assert isinstance(instance, ast::PackageDeclaration)

@given(instance=ast::Expression_strategy)
@settings(max_examples=50)
def test_ast::expression_instantiation(instance):
    assert isinstance(instance, ast::Expression)

@given(instance=ast::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_ast::importdeclaration_instantiation(instance):
    assert isinstance(instance, ast::ImportDeclaration)

@given(instance=ast::ImportDeclaration_strategy)
def test_ast::importdeclaration_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ast::ImportDeclaration_strategy)
def test_ast::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ast::ImportDeclaration_strategy)
def test_ast::importdeclaration_onDemand_type(instance):
    assert isinstance(instance.onDemand, bool)


@given(instance=ast::ImportDeclaration_strategy)
def test_ast::importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original

@given(instance=ast::Dimension_strategy)
@settings(max_examples=50)
def test_ast::dimension_instantiation(instance):
    assert isinstance(instance, ast::Dimension)

@given(instance=ast::CatchClause_strategy)
@settings(max_examples=50)
def test_ast::catchclause_instantiation(instance):
    assert isinstance(instance, ast::CatchClause)

@given(instance=ast::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_ast::bodydeclaration_instantiation(instance):
    assert isinstance(instance, ast::BodyDeclaration)

@given(instance=ast::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_ast::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, ast::AnonymousClassDeclaration)

@given(instance=ast::Type_strategy)
@settings(max_examples=50)
def test_ast::type_instantiation(instance):
    assert isinstance(instance, ast::Type)

@given(instance=ast::Comment_strategy)
@settings(max_examples=50)
def test_ast::comment_instantiation(instance):
    assert isinstance(instance, ast::Comment)

@given(instance=ast::Statement_strategy)
@settings(max_examples=50)
def test_ast::statement_instantiation(instance):
    assert isinstance(instance, ast::Statement)

@given(instance=ast::TypeParameter_strategy)
@settings(max_examples=50)
def test_ast::typeparameter_instantiation(instance):
    assert isinstance(instance, ast::TypeParameter)

@given(instance=ast::CompilationUnit_strategy)
@settings(max_examples=50)
def test_ast::compilationunit_instantiation(instance):
    assert isinstance(instance, ast::CompilationUnit)

@given(instance=ast::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast::variabledeclaration_instantiation(instance):
    assert isinstance(instance, ast::VariableDeclaration)

@given(instance=ast::Modifier_strategy)
@settings(max_examples=50)
def test_ast::modifier_instantiation(instance):
    assert isinstance(instance, ast::Modifier)

@given(instance=ast::Modifier_strategy)
def test_ast::modifier_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=ast::Modifier_strategy)
def test_ast::modifier_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=ast::IExtendedModifier_strategy)
@settings(max_examples=50)
def test_ast::iextendedmodifier_instantiation(instance):
    assert isinstance(instance, ast::IExtendedModifier)

@given(instance=ast::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_ast::methodrefparameter_instantiation(instance):
    assert isinstance(instance, ast::MethodRefParameter)

@given(instance=ast::MethodRefParameter_strategy)
def test_ast::methodrefparameter_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=ast::MethodRefParameter_strategy)
def test_ast::methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=ast::SimpleName_strategy)
@settings(max_examples=50)
def test_ast::simplename_instantiation(instance):
    assert isinstance(instance, ast::SimpleName)

@given(instance=ast::SimpleName_strategy)
def test_ast::simplename_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ast::SimpleName_strategy)
def test_ast::simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=IDocElement_strategy)
@settings(max_examples=50)
def test_idocelement_instantiation(instance):
    assert isinstance(instance, IDocElement)

@given(instance=ast::Name_strategy)
@settings(max_examples=50)
def test_ast::name_instantiation(instance):
    assert isinstance(instance, ast::Name)

@given(instance=ast::TagElement_strategy)
@settings(max_examples=50)
def test_ast::tagelement_instantiation(instance):
    assert isinstance(instance, ast::TagElement)

@given(instance=ast::TagElement_strategy)
def test_ast::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=ast::TagElement_strategy)
def test_ast::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=ast::MethodRef_strategy)
@settings(max_examples=50)
def test_ast::methodref_instantiation(instance):
    assert isinstance(instance, ast::MethodRef)

@given(instance=ast::TextElement_strategy)
@settings(max_examples=50)
def test_ast::textelement_instantiation(instance):
    assert isinstance(instance, ast::TextElement)

@given(instance=ast::TextElement_strategy)
def test_ast::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ast::TextElement_strategy)
def test_ast::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ast::MemberRef_strategy)
@settings(max_examples=50)
def test_ast::memberref_instantiation(instance):
    assert isinstance(instance, ast::MemberRef)

@given(instance=ast::IDocElement_strategy)
@settings(max_examples=50)
def test_ast::idocelement_instantiation(instance):
    assert isinstance(instance, ast::IDocElement)

@given(instance=ast::SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_ast::singlememberannotation_instantiation(instance):
    assert isinstance(instance, ast::SingleMemberAnnotation)

@given(instance=ast::MemberValuePair_strategy)
@settings(max_examples=50)
def test_ast::membervaluepair_instantiation(instance):
    assert isinstance(instance, ast::MemberValuePair)
