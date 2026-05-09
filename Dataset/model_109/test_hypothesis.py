import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Name,
    JDTAST::QualifiedName,
    VariableDeclaration,
    Annotation,
    JDTAST::SingleMemberAnnotation,
    JDTAST::NormalAnnotation,
    JDTAST::MarkerAnnotation,
    Type,
    JDTAST::ParameterizedType,
    JDTAST::WildcardType,
    JDTAST::SimpleType,
    JDTAST::QualifiedType,
    JDTAST::PrimitiveType,
    Statement,
    JDTAST::TypeDeclarationStatement,
    JDTAST::ThrowStatement,
    JDTAST::SwitchCase,
    JDTAST::SuperConstructorInvocation,
    JDTAST::EmptyStatement,
    JDTAST::DoStatement,
    JDTAST::ExpressionStatement,
    JDTAST::EnhancedForStatement,
    JDTAST::VariableDeclarationStatement,
    JDTAST::ReturnStatement,
    JDTAST::ForStatement,
    JDTAST::SynchronizedStatement,
    JDTAST::BreakStatement,
    JDTAST::LabeledStatement,
    JDTAST::SwitchStatement,
    JDTAST::WhileStatement,
    JDTAST::ContinueStatement,
    JDTAST::TryStatement,
    JDTAST::IfStatement,
    JDTAST::ConstructorInvocation,
    JDTAST::AssertStatement,
    Expression,
    JDTAST::FieldAccess,
    JDTAST::PostfixExpression,
    JDTAST::ArrayAccess,
    JDTAST::InfixExpression,
    JDTAST::CastExpression,
    JDTAST::SuperMethodInvocation,
    JDTAST::ThisExpression,
    JDTAST::StringLiteral,
    JDTAST::TypeLiteral,
    JDTAST::Assignment,
    JDTAST::MethodInvocation,
    JDTAST::ConditionalExpression,
    JDTAST::ClassInstanceCreation,
    JDTAST::BooleanLiteral,
    JDTAST::NullLiteral,
    JDTAST::InstanceofExpression,
    JDTAST::SuperFieldAccess,
    JDTAST::ParenthesizedExpression,
    JDTAST::NumberLiteral,
    JDTAST::CharacterLiteral,
    JDTAST::VariableDeclarationExpression,
    JDTAST::PrefixExpression,
    Comment,
    JDTAST::LineComment,
    JDTAST::BlockComment,
    AbstractTypeDeclaration,
    JDTAST::EnumDeclaration,
    JDTAST::TypeDeclaration,
    JDTAST::AnnotationTypeDeclaration,
    JDTAST::ArrayType,
    JDTAST::ArrayInitializer,
    JDTAST::ArrayCreation,
    JDTAST::VariableDeclarationFragment,
    BodyDeclaration,
    JDTAST::EnumConstantDeclaration,
    JDTAST::MethodDeclaration,
    JDTAST::FieldDeclaration,
    JDTAST::Initializer,
    JDTAST::AnnotationTypeMemberDeclaration,
    JDTAST::SimpleName,
    ExtendedModifier,
    JDTAST::Annotation,
    JDTAST::Name,
    JDTAST::AbstractTypeDeclaration,
    JDTAST::SingleVariableDeclaration,
    JDTAST::Block,
    JDTAST::ASTNode,
    JDTAST::AST,
    JDTAST::Parameter,
    JDTAST::Javadoc,
    JDTAST::ExtendedModifier,
    ASTNode,
    JDTAST::PackageDeclaration,
    JDTAST::Expression,
    JDTAST::MethodRefParameter,
    JDTAST::Statement,
    JDTAST::MemberRef,
    JDTAST::ImportDeclaration,
    JDTAST::Type,
    JDTAST::VariableDeclaration,
    JDTAST::Modifier,
    JDTAST::MemberValuePair,
    JDTAST::MethodRef,
    JDTAST::Comment,
    JDTAST::TagElement,
    JDTAST::TextElement,
    JDTAST::BodyDeclaration,
    JDTAST::CatchClause,
    JDTAST::TypeParameter,
    JDTAST::AnonymousClassDeclaration,
    IMember,
    JDTAST::IMethod,
    JDTAST::IField,
    JDTAST::IInitializer,
    JDTAST::ISourceRange,
    JDTAST::ISourceReference,
    JDTAST::CompilationUnit,
    IPackageFragmentRoot,
    JDTAST::SourcePackageFragmentRoot,
    JDTAST::BinaryPackageFragmentRoot,
    IJavaElement,
    PhysicalElement,
    JDTAST::IPackageFragment,
    JDTAST::IJavaProject,
    JDTAST::IPackageFragmentRoot,
    JDTAST::IJavaModel,
    JDTAST::PhysicalElement,
    JDTAST::IJavaElement,
    JDTAST::IType,
    ITypeRoot,
    ISourceReference,
    JDTAST::ITypeParameter,
    JDTAST::IImportDeclaration,
    JDTAST::IMember,
    JDTAST::ITypeRoot,
    JDTAST::ICompilationUnit,
    JDTAST::IClassFile,
    AssignmentOperatorKind,
    InfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
    Modifiers,
    PostfixExpressionOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(JDTAST::QualifiedName)


def test_jdtast::qualifiedname_constructor_exists():
    assert callable(JDTAST::QualifiedName.__init__)


def test_jdtast::qualifiedname_constructor_args():
    sig = inspect.signature(JDTAST::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SingleMemberAnnotation)


def test_jdtast::singlememberannotation_constructor_exists():
    assert callable(JDTAST::SingleMemberAnnotation.__init__)


def test_jdtast::singlememberannotation_constructor_args():
    sig = inspect.signature(JDTAST::SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::normalannotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::NormalAnnotation)


def test_jdtast::normalannotation_constructor_exists():
    assert callable(JDTAST::NormalAnnotation.__init__)


def test_jdtast::normalannotation_constructor_args():
    sig = inspect.signature(JDTAST::NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::markerannotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MarkerAnnotation)


def test_jdtast::markerannotation_constructor_exists():
    assert callable(JDTAST::MarkerAnnotation.__init__)


def test_jdtast::markerannotation_constructor_args():
    sig = inspect.signature(JDTAST::MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ParameterizedType)


def test_jdtast::parameterizedtype_constructor_exists():
    assert callable(JDTAST::ParameterizedType.__init__)


def test_jdtast::parameterizedtype_constructor_args():
    sig = inspect.signature(JDTAST::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::WildcardType)


def test_jdtast::wildcardtype_constructor_exists():
    assert callable(JDTAST::WildcardType.__init__)


def test_jdtast::wildcardtype_constructor_args():
    sig = inspect.signature(JDTAST::WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_jdtast::wildcardtype_has_upperBound():
    assert hasattr(JDTAST::WildcardType, "upperBound")
    descriptor = None
    for klass in JDTAST::WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::simpletype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SimpleType)


def test_jdtast::simpletype_constructor_exists():
    assert callable(JDTAST::SimpleType.__init__)


def test_jdtast::simpletype_constructor_args():
    sig = inspect.signature(JDTAST::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::QualifiedType)


def test_jdtast::qualifiedtype_constructor_exists():
    assert callable(JDTAST::QualifiedType.__init__)


def test_jdtast::qualifiedtype_constructor_args():
    sig = inspect.signature(JDTAST::QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::primitivetype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::PrimitiveType)


def test_jdtast::primitivetype_constructor_exists():
    assert callable(JDTAST::PrimitiveType.__init__)


def test_jdtast::primitivetype_constructor_args():
    sig = inspect.signature(JDTAST::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_jdtast::primitivetype_has_code():
    assert hasattr(JDTAST::PrimitiveType, "code")
    descriptor = None
    for klass in JDTAST::PrimitiveType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TypeDeclarationStatement)


def test_jdtast::typedeclarationstatement_constructor_exists():
    assert callable(JDTAST::TypeDeclarationStatement.__init__)


def test_jdtast::typedeclarationstatement_constructor_args():
    sig = inspect.signature(JDTAST::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::throwstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ThrowStatement)


def test_jdtast::throwstatement_constructor_exists():
    assert callable(JDTAST::ThrowStatement.__init__)


def test_jdtast::throwstatement_constructor_args():
    sig = inspect.signature(JDTAST::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::switchcase_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SwitchCase)


def test_jdtast::switchcase_constructor_exists():
    assert callable(JDTAST::SwitchCase.__init__)


def test_jdtast::switchcase_constructor_args():
    sig = inspect.signature(JDTAST::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_jdtast::switchcase_has_default():
    assert hasattr(JDTAST::SwitchCase, "default")
    descriptor = None
    for klass in JDTAST::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SuperConstructorInvocation)


def test_jdtast::superconstructorinvocation_constructor_exists():
    assert callable(JDTAST::SuperConstructorInvocation.__init__)


def test_jdtast::superconstructorinvocation_constructor_args():
    sig = inspect.signature(JDTAST::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::emptystatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::EmptyStatement)


def test_jdtast::emptystatement_constructor_exists():
    assert callable(JDTAST::EmptyStatement.__init__)


def test_jdtast::emptystatement_constructor_args():
    sig = inspect.signature(JDTAST::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::dostatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::DoStatement)


def test_jdtast::dostatement_constructor_exists():
    assert callable(JDTAST::DoStatement.__init__)


def test_jdtast::dostatement_constructor_args():
    sig = inspect.signature(JDTAST::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ExpressionStatement)


def test_jdtast::expressionstatement_constructor_exists():
    assert callable(JDTAST::ExpressionStatement.__init__)


def test_jdtast::expressionstatement_constructor_args():
    sig = inspect.signature(JDTAST::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::EnhancedForStatement)


def test_jdtast::enhancedforstatement_constructor_exists():
    assert callable(JDTAST::EnhancedForStatement.__init__)


def test_jdtast::enhancedforstatement_constructor_args():
    sig = inspect.signature(JDTAST::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::VariableDeclarationStatement)


def test_jdtast::variabledeclarationstatement_constructor_exists():
    assert callable(JDTAST::VariableDeclarationStatement.__init__)


def test_jdtast::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(JDTAST::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::returnstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ReturnStatement)


def test_jdtast::returnstatement_constructor_exists():
    assert callable(JDTAST::ReturnStatement.__init__)


def test_jdtast::returnstatement_constructor_args():
    sig = inspect.signature(JDTAST::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::forstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ForStatement)


def test_jdtast::forstatement_constructor_exists():
    assert callable(JDTAST::ForStatement.__init__)


def test_jdtast::forstatement_constructor_args():
    sig = inspect.signature(JDTAST::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SynchronizedStatement)


def test_jdtast::synchronizedstatement_constructor_exists():
    assert callable(JDTAST::SynchronizedStatement.__init__)


def test_jdtast::synchronizedstatement_constructor_args():
    sig = inspect.signature(JDTAST::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::breakstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::BreakStatement)


def test_jdtast::breakstatement_constructor_exists():
    assert callable(JDTAST::BreakStatement.__init__)


def test_jdtast::breakstatement_constructor_args():
    sig = inspect.signature(JDTAST::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::LabeledStatement)


def test_jdtast::labeledstatement_constructor_exists():
    assert callable(JDTAST::LabeledStatement.__init__)


def test_jdtast::labeledstatement_constructor_args():
    sig = inspect.signature(JDTAST::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::switchstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SwitchStatement)


def test_jdtast::switchstatement_constructor_exists():
    assert callable(JDTAST::SwitchStatement.__init__)


def test_jdtast::switchstatement_constructor_args():
    sig = inspect.signature(JDTAST::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::whilestatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::WhileStatement)


def test_jdtast::whilestatement_constructor_exists():
    assert callable(JDTAST::WhileStatement.__init__)


def test_jdtast::whilestatement_constructor_args():
    sig = inspect.signature(JDTAST::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::continuestatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ContinueStatement)


def test_jdtast::continuestatement_constructor_exists():
    assert callable(JDTAST::ContinueStatement.__init__)


def test_jdtast::continuestatement_constructor_args():
    sig = inspect.signature(JDTAST::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::trystatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TryStatement)


def test_jdtast::trystatement_constructor_exists():
    assert callable(JDTAST::TryStatement.__init__)


def test_jdtast::trystatement_constructor_args():
    sig = inspect.signature(JDTAST::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::ifstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IfStatement)


def test_jdtast::ifstatement_constructor_exists():
    assert callable(JDTAST::IfStatement.__init__)


def test_jdtast::ifstatement_constructor_args():
    sig = inspect.signature(JDTAST::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ConstructorInvocation)


def test_jdtast::constructorinvocation_constructor_exists():
    assert callable(JDTAST::ConstructorInvocation.__init__)


def test_jdtast::constructorinvocation_constructor_args():
    sig = inspect.signature(JDTAST::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::assertstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::AssertStatement)


def test_jdtast::assertstatement_constructor_exists():
    assert callable(JDTAST::AssertStatement.__init__)


def test_jdtast::assertstatement_constructor_args():
    sig = inspect.signature(JDTAST::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(JDTAST::FieldAccess)


def test_jdtast::fieldaccess_constructor_exists():
    assert callable(JDTAST::FieldAccess.__init__)


def test_jdtast::fieldaccess_constructor_args():
    sig = inspect.signature(JDTAST::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::PostfixExpression)


def test_jdtast::postfixexpression_constructor_exists():
    assert callable(JDTAST::PostfixExpression.__init__)


def test_jdtast::postfixexpression_constructor_args():
    sig = inspect.signature(JDTAST::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast::postfixexpression_has_operator():
    assert hasattr(JDTAST::PostfixExpression, "operator")
    descriptor = None
    for klass in JDTAST::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ArrayAccess)


def test_jdtast::arrayaccess_constructor_exists():
    assert callable(JDTAST::ArrayAccess.__init__)


def test_jdtast::arrayaccess_constructor_args():
    sig = inspect.signature(JDTAST::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::infixexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::InfixExpression)


def test_jdtast::infixexpression_constructor_exists():
    assert callable(JDTAST::InfixExpression.__init__)


def test_jdtast::infixexpression_constructor_args():
    sig = inspect.signature(JDTAST::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast::infixexpression_has_operator():
    assert hasattr(JDTAST::InfixExpression, "operator")
    descriptor = None
    for klass in JDTAST::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::castexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::CastExpression)


def test_jdtast::castexpression_constructor_exists():
    assert callable(JDTAST::CastExpression.__init__)


def test_jdtast::castexpression_constructor_args():
    sig = inspect.signature(JDTAST::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SuperMethodInvocation)


def test_jdtast::supermethodinvocation_constructor_exists():
    assert callable(JDTAST::SuperMethodInvocation.__init__)


def test_jdtast::supermethodinvocation_constructor_args():
    sig = inspect.signature(JDTAST::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::thisexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ThisExpression)


def test_jdtast::thisexpression_constructor_exists():
    assert callable(JDTAST::ThisExpression.__init__)


def test_jdtast::thisexpression_constructor_args():
    sig = inspect.signature(JDTAST::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::stringliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST::StringLiteral)


def test_jdtast::stringliteral_constructor_exists():
    assert callable(JDTAST::StringLiteral.__init__)


def test_jdtast::stringliteral_constructor_args():
    sig = inspect.signature(JDTAST::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_jdtast::stringliteral_has_escapedValue():
    assert hasattr(JDTAST::StringLiteral, "escapedValue")
    descriptor = None
    for klass in JDTAST::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::stringliteral_has_literalValue():
    assert hasattr(JDTAST::StringLiteral, "literalValue")
    descriptor = None
    for klass in JDTAST::StringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::typeliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TypeLiteral)


def test_jdtast::typeliteral_constructor_exists():
    assert callable(JDTAST::TypeLiteral.__init__)


def test_jdtast::typeliteral_constructor_args():
    sig = inspect.signature(JDTAST::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::assignment_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Assignment)


def test_jdtast::assignment_constructor_exists():
    assert callable(JDTAST::Assignment.__init__)


def test_jdtast::assignment_constructor_args():
    sig = inspect.signature(JDTAST::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast::assignment_has_operator():
    assert hasattr(JDTAST::Assignment, "operator")
    descriptor = None
    for klass in JDTAST::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MethodInvocation)


def test_jdtast::methodinvocation_constructor_exists():
    assert callable(JDTAST::MethodInvocation.__init__)


def test_jdtast::methodinvocation_constructor_args():
    sig = inspect.signature(JDTAST::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ConditionalExpression)


def test_jdtast::conditionalexpression_constructor_exists():
    assert callable(JDTAST::ConditionalExpression.__init__)


def test_jdtast::conditionalexpression_constructor_args():
    sig = inspect.signature(JDTAST::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ClassInstanceCreation)


def test_jdtast::classinstancecreation_constructor_exists():
    assert callable(JDTAST::ClassInstanceCreation.__init__)


def test_jdtast::classinstancecreation_constructor_args():
    sig = inspect.signature(JDTAST::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST::BooleanLiteral)


def test_jdtast::booleanliteral_constructor_exists():
    assert callable(JDTAST::BooleanLiteral.__init__)


def test_jdtast::booleanliteral_constructor_args():
    sig = inspect.signature(JDTAST::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_jdtast::booleanliteral_has_booleanValue():
    assert hasattr(JDTAST::BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in JDTAST::BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::nullliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST::NullLiteral)


def test_jdtast::nullliteral_constructor_exists():
    assert callable(JDTAST::NullLiteral.__init__)


def test_jdtast::nullliteral_constructor_args():
    sig = inspect.signature(JDTAST::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::InstanceofExpression)


def test_jdtast::instanceofexpression_constructor_exists():
    assert callable(JDTAST::InstanceofExpression.__init__)


def test_jdtast::instanceofexpression_constructor_args():
    sig = inspect.signature(JDTAST::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SuperFieldAccess)


def test_jdtast::superfieldaccess_constructor_exists():
    assert callable(JDTAST::SuperFieldAccess.__init__)


def test_jdtast::superfieldaccess_constructor_args():
    sig = inspect.signature(JDTAST::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ParenthesizedExpression)


def test_jdtast::parenthesizedexpression_constructor_exists():
    assert callable(JDTAST::ParenthesizedExpression.__init__)


def test_jdtast::parenthesizedexpression_constructor_args():
    sig = inspect.signature(JDTAST::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::numberliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST::NumberLiteral)


def test_jdtast::numberliteral_constructor_exists():
    assert callable(JDTAST::NumberLiteral.__init__)


def test_jdtast::numberliteral_constructor_args():
    sig = inspect.signature(JDTAST::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_jdtast::numberliteral_has_token():
    assert hasattr(JDTAST::NumberLiteral, "token")
    descriptor = None
    for klass in JDTAST::NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::characterliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST::CharacterLiteral)


def test_jdtast::characterliteral_constructor_exists():
    assert callable(JDTAST::CharacterLiteral.__init__)


def test_jdtast::characterliteral_constructor_args():
    sig = inspect.signature(JDTAST::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "charValue" in params, "Missing parameter 'charValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_jdtast::characterliteral_has_charValue():
    assert hasattr(JDTAST::CharacterLiteral, "charValue")
    descriptor = None
    for klass in JDTAST::CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::characterliteral_has_escapedValue():
    assert hasattr(JDTAST::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in JDTAST::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::VariableDeclarationExpression)


def test_jdtast::variabledeclarationexpression_constructor_exists():
    assert callable(JDTAST::VariableDeclarationExpression.__init__)


def test_jdtast::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(JDTAST::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::PrefixExpression)


def test_jdtast::prefixexpression_constructor_exists():
    assert callable(JDTAST::PrefixExpression.__init__)


def test_jdtast::prefixexpression_constructor_args():
    sig = inspect.signature(JDTAST::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast::prefixexpression_has_operator():
    assert hasattr(JDTAST::PrefixExpression, "operator")
    descriptor = None
    for klass in JDTAST::PrefixExpression.__mro__:
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



def test_jdtast::linecomment_is_not_abstract():
    assert not inspect.isabstract(JDTAST::LineComment)


def test_jdtast::linecomment_constructor_exists():
    assert callable(JDTAST::LineComment.__init__)


def test_jdtast::linecomment_constructor_args():
    sig = inspect.signature(JDTAST::LineComment.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::blockcomment_is_not_abstract():
    assert not inspect.isabstract(JDTAST::BlockComment)


def test_jdtast::blockcomment_constructor_exists():
    assert callable(JDTAST::BlockComment.__init__)


def test_jdtast::blockcomment_constructor_args():
    sig = inspect.signature(JDTAST::BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::EnumDeclaration)


def test_jdtast::enumdeclaration_constructor_exists():
    assert callable(JDTAST::EnumDeclaration.__init__)


def test_jdtast::enumdeclaration_constructor_args():
    sig = inspect.signature(JDTAST::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TypeDeclaration)


def test_jdtast::typedeclaration_constructor_exists():
    assert callable(JDTAST::TypeDeclaration.__init__)


def test_jdtast::typedeclaration_constructor_args():
    sig = inspect.signature(JDTAST::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_jdtast::typedeclaration_has_interface():
    assert hasattr(JDTAST::TypeDeclaration, "interface")
    descriptor = None
    for klass in JDTAST::TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::AnnotationTypeDeclaration)


def test_jdtast::annotationtypedeclaration_constructor_exists():
    assert callable(JDTAST::AnnotationTypeDeclaration.__init__)


def test_jdtast::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JDTAST::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::arraytype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ArrayType)


def test_jdtast::arraytype_constructor_exists():
    assert callable(JDTAST::ArrayType.__init__)


def test_jdtast::arraytype_constructor_args():
    sig = inspect.signature(JDTAST::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_jdtast::arraytype_has_dimensions():
    assert hasattr(JDTAST::ArrayType, "dimensions")
    descriptor = None
    for klass in JDTAST::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ArrayInitializer)


def test_jdtast::arrayinitializer_constructor_exists():
    assert callable(JDTAST::ArrayInitializer.__init__)


def test_jdtast::arrayinitializer_constructor_args():
    sig = inspect.signature(JDTAST::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::arraycreation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ArrayCreation)


def test_jdtast::arraycreation_constructor_exists():
    assert callable(JDTAST::ArrayCreation.__init__)


def test_jdtast::arraycreation_constructor_args():
    sig = inspect.signature(JDTAST::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(JDTAST::VariableDeclarationFragment)


def test_jdtast::variabledeclarationfragment_constructor_exists():
    assert callable(JDTAST::VariableDeclarationFragment.__init__)


def test_jdtast::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(JDTAST::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::EnumConstantDeclaration)


def test_jdtast::enumconstantdeclaration_constructor_exists():
    assert callable(JDTAST::EnumConstantDeclaration.__init__)


def test_jdtast::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(JDTAST::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MethodDeclaration)


def test_jdtast::methoddeclaration_constructor_exists():
    assert callable(JDTAST::MethodDeclaration.__init__)


def test_jdtast::methoddeclaration_constructor_args():
    sig = inspect.signature(JDTAST::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"

def test_jdtast::methoddeclaration_has_extraDimensions():
    assert hasattr(JDTAST::MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in JDTAST::MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::methoddeclaration_has_varargs():
    assert hasattr(JDTAST::MethodDeclaration, "varargs")
    descriptor = None
    for klass in JDTAST::MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::methoddeclaration_has_constructor():
    assert hasattr(JDTAST::MethodDeclaration, "constructor")
    descriptor = None
    for klass in JDTAST::MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::FieldDeclaration)


def test_jdtast::fielddeclaration_constructor_exists():
    assert callable(JDTAST::FieldDeclaration.__init__)


def test_jdtast::fielddeclaration_constructor_args():
    sig = inspect.signature(JDTAST::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::initializer_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Initializer)


def test_jdtast::initializer_constructor_exists():
    assert callable(JDTAST::Initializer.__init__)


def test_jdtast::initializer_constructor_args():
    sig = inspect.signature(JDTAST::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::AnnotationTypeMemberDeclaration)


def test_jdtast::annotationtypememberdeclaration_constructor_exists():
    assert callable(JDTAST::AnnotationTypeMemberDeclaration.__init__)


def test_jdtast::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(JDTAST::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::simplename_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SimpleName)


def test_jdtast::simplename_constructor_exists():
    assert callable(JDTAST::SimpleName.__init__)


def test_jdtast::simplename_constructor_args():
    sig = inspect.signature(JDTAST::SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_jdtast::simplename_has_declaration():
    assert hasattr(JDTAST::SimpleName, "declaration")
    descriptor = None
    for klass in JDTAST::SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::simplename_has_identifier():
    assert hasattr(JDTAST::SimpleName, "identifier")
    descriptor = None
    for klass in JDTAST::SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::annotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Annotation)


def test_jdtast::annotation_constructor_exists():
    assert callable(JDTAST::Annotation.__init__)


def test_jdtast::annotation_constructor_args():
    sig = inspect.signature(JDTAST::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::name_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Name)


def test_jdtast::name_constructor_exists():
    assert callable(JDTAST::Name.__init__)


def test_jdtast::name_constructor_args():
    sig = inspect.signature(JDTAST::Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_jdtast::name_has_fullyQualifiedName():
    assert hasattr(JDTAST::Name, "fullyQualifiedName")
    descriptor = None
    for klass in JDTAST::Name.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::AbstractTypeDeclaration)


def test_jdtast::abstracttypedeclaration_constructor_exists():
    assert callable(JDTAST::AbstractTypeDeclaration.__init__)


def test_jdtast::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JDTAST::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"

def test_jdtast::abstracttypedeclaration_has_localTypeDeclaration():
    assert hasattr(JDTAST::AbstractTypeDeclaration, "localTypeDeclaration")
    descriptor = None
    for klass in JDTAST::AbstractTypeDeclaration.__mro__:
        if "localTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["localTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::abstracttypedeclaration_has_packageMemberTypeDeclaration():
    assert hasattr(JDTAST::AbstractTypeDeclaration, "packageMemberTypeDeclaration")
    descriptor = None
    for klass in JDTAST::AbstractTypeDeclaration.__mro__:
        if "packageMemberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["packageMemberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::abstracttypedeclaration_has_memberTypeDeclaration():
    assert hasattr(JDTAST::AbstractTypeDeclaration, "memberTypeDeclaration")
    descriptor = None
    for klass in JDTAST::AbstractTypeDeclaration.__mro__:
        if "memberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["memberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SingleVariableDeclaration)


def test_jdtast::singlevariabledeclaration_constructor_exists():
    assert callable(JDTAST::SingleVariableDeclaration.__init__)


def test_jdtast::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(JDTAST::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_jdtast::singlevariabledeclaration_has_varargs():
    assert hasattr(JDTAST::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in JDTAST::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::block_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Block)


def test_jdtast::block_constructor_exists():
    assert callable(JDTAST::Block.__init__)


def test_jdtast::block_constructor_args():
    sig = inspect.signature(JDTAST::Block.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::astnode_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ASTNode)


def test_jdtast::astnode_constructor_exists():
    assert callable(JDTAST::ASTNode.__init__)


def test_jdtast::astnode_constructor_args():
    sig = inspect.signature(JDTAST::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::ast_is_not_abstract():
    assert not inspect.isabstract(JDTAST::AST)


def test_jdtast::ast_constructor_exists():
    assert callable(JDTAST::AST.__init__)


def test_jdtast::ast_constructor_args():
    sig = inspect.signature(JDTAST::AST.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::parameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Parameter)


def test_jdtast::parameter_constructor_exists():
    assert callable(JDTAST::Parameter.__init__)


def test_jdtast::parameter_constructor_args():
    sig = inspect.signature(JDTAST::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_jdtast::parameter_has_type():
    assert hasattr(JDTAST::Parameter, "type")
    descriptor = None
    for klass in JDTAST::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::parameter_has_name():
    assert hasattr(JDTAST::Parameter, "name")
    descriptor = None
    for klass in JDTAST::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::javadoc_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Javadoc)


def test_jdtast::javadoc_constructor_exists():
    assert callable(JDTAST::Javadoc.__init__)


def test_jdtast::javadoc_constructor_args():
    sig = inspect.signature(JDTAST::Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ExtendedModifier)


def test_jdtast::extendedmodifier_constructor_exists():
    assert callable(JDTAST::ExtendedModifier.__init__)


def test_jdtast::extendedmodifier_constructor_args():
    sig = inspect.signature(JDTAST::ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::PackageDeclaration)


def test_jdtast::packagedeclaration_constructor_exists():
    assert callable(JDTAST::PackageDeclaration.__init__)


def test_jdtast::packagedeclaration_constructor_args():
    sig = inspect.signature(JDTAST::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::expression_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Expression)


def test_jdtast::expression_constructor_exists():
    assert callable(JDTAST::Expression.__init__)


def test_jdtast::expression_constructor_args():
    sig = inspect.signature(JDTAST::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"

def test_jdtast::expression_has_resolveUnboxing():
    assert hasattr(JDTAST::Expression, "resolveUnboxing")
    descriptor = None
    for klass in JDTAST::Expression.__mro__:
        if "resolveUnboxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveUnboxing"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::expression_has_resolveBoxing():
    assert hasattr(JDTAST::Expression, "resolveBoxing")
    descriptor = None
    for klass in JDTAST::Expression.__mro__:
        if "resolveBoxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveBoxing"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MethodRefParameter)


def test_jdtast::methodrefparameter_constructor_exists():
    assert callable(JDTAST::MethodRefParameter.__init__)


def test_jdtast::methodrefparameter_constructor_args():
    sig = inspect.signature(JDTAST::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_jdtast::methodrefparameter_has_varargs():
    assert hasattr(JDTAST::MethodRefParameter, "varargs")
    descriptor = None
    for klass in JDTAST::MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::statement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Statement)


def test_jdtast::statement_constructor_exists():
    assert callable(JDTAST::Statement.__init__)


def test_jdtast::statement_constructor_args():
    sig = inspect.signature(JDTAST::Statement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::memberref_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MemberRef)


def test_jdtast::memberref_constructor_exists():
    assert callable(JDTAST::MemberRef.__init__)


def test_jdtast::memberref_constructor_args():
    sig = inspect.signature(JDTAST::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ImportDeclaration)


def test_jdtast::importdeclaration_constructor_exists():
    assert callable(JDTAST::ImportDeclaration.__init__)


def test_jdtast::importdeclaration_constructor_args():
    sig = inspect.signature(JDTAST::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"

def test_jdtast::importdeclaration_has_onDemand():
    assert hasattr(JDTAST::ImportDeclaration, "onDemand")
    descriptor = None
    for klass in JDTAST::ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::importdeclaration_has_static():
    assert hasattr(JDTAST::ImportDeclaration, "static")
    descriptor = None
    for klass in JDTAST::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::type_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Type)


def test_jdtast::type_constructor_exists():
    assert callable(JDTAST::Type.__init__)


def test_jdtast::type_constructor_args():
    sig = inspect.signature(JDTAST::Type.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::VariableDeclaration)


def test_jdtast::variabledeclaration_constructor_exists():
    assert callable(JDTAST::VariableDeclaration.__init__)


def test_jdtast::variabledeclaration_constructor_args():
    sig = inspect.signature(JDTAST::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_jdtast::variabledeclaration_has_extraDimensions():
    assert hasattr(JDTAST::VariableDeclaration, "extraDimensions")
    descriptor = None
    for klass in JDTAST::VariableDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::modifier_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Modifier)


def test_jdtast::modifier_constructor_exists():
    assert callable(JDTAST::Modifier.__init__)


def test_jdtast::modifier_constructor_args():
    sig = inspect.signature(JDTAST::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"
    assert "native" in params, "Missing parameter 'native'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "final" in params, "Missing parameter 'final'"
    assert "public" in params, "Missing parameter 'public'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "none" in params, "Missing parameter 'none'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "private" in params, "Missing parameter 'private'"

def test_jdtast::modifier_has_strictfp():
    assert hasattr(JDTAST::Modifier, "strictfp")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_abstract():
    assert hasattr(JDTAST::Modifier, "abstract")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_static():
    assert hasattr(JDTAST::Modifier, "static")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_native():
    assert hasattr(JDTAST::Modifier, "native")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_protected():
    assert hasattr(JDTAST::Modifier, "protected")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_transient():
    assert hasattr(JDTAST::Modifier, "transient")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_final():
    assert hasattr(JDTAST::Modifier, "final")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_public():
    assert hasattr(JDTAST::Modifier, "public")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_volatile():
    assert hasattr(JDTAST::Modifier, "volatile")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_none():
    assert hasattr(JDTAST::Modifier, "none")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_synchronized():
    assert hasattr(JDTAST::Modifier, "synchronized")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::modifier_has_private():
    assert hasattr(JDTAST::Modifier, "private")
    descriptor = None
    for klass in JDTAST::Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::membervaluepair_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MemberValuePair)


def test_jdtast::membervaluepair_constructor_exists():
    assert callable(JDTAST::MemberValuePair.__init__)


def test_jdtast::membervaluepair_constructor_args():
    sig = inspect.signature(JDTAST::MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::methodref_is_not_abstract():
    assert not inspect.isabstract(JDTAST::MethodRef)


def test_jdtast::methodref_constructor_exists():
    assert callable(JDTAST::MethodRef.__init__)


def test_jdtast::methodref_constructor_args():
    sig = inspect.signature(JDTAST::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::comment_is_not_abstract():
    assert not inspect.isabstract(JDTAST::Comment)


def test_jdtast::comment_constructor_exists():
    assert callable(JDTAST::Comment.__init__)


def test_jdtast::comment_constructor_args():
    sig = inspect.signature(JDTAST::Comment.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::tagelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TagElement)


def test_jdtast::tagelement_constructor_exists():
    assert callable(JDTAST::TagElement.__init__)


def test_jdtast::tagelement_constructor_args():
    sig = inspect.signature(JDTAST::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "nested" in params, "Missing parameter 'nested'"
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_jdtast::tagelement_has_nested():
    assert hasattr(JDTAST::TagElement, "nested")
    descriptor = None
    for klass in JDTAST::TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::tagelement_has_tagName():
    assert hasattr(JDTAST::TagElement, "tagName")
    descriptor = None
    for klass in JDTAST::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::textelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TextElement)


def test_jdtast::textelement_constructor_exists():
    assert callable(JDTAST::TextElement.__init__)


def test_jdtast::textelement_constructor_args():
    sig = inspect.signature(JDTAST::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_jdtast::textelement_has_text():
    assert hasattr(JDTAST::TextElement, "text")
    descriptor = None
    for klass in JDTAST::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::BodyDeclaration)


def test_jdtast::bodydeclaration_constructor_exists():
    assert callable(JDTAST::BodyDeclaration.__init__)


def test_jdtast::bodydeclaration_constructor_args():
    sig = inspect.signature(JDTAST::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::catchclause_is_not_abstract():
    assert not inspect.isabstract(JDTAST::CatchClause)


def test_jdtast::catchclause_constructor_exists():
    assert callable(JDTAST::CatchClause.__init__)


def test_jdtast::catchclause_constructor_args():
    sig = inspect.signature(JDTAST::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::typeparameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST::TypeParameter)


def test_jdtast::typeparameter_constructor_exists():
    assert callable(JDTAST::TypeParameter.__init__)


def test_jdtast::typeparameter_constructor_args():
    sig = inspect.signature(JDTAST::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::AnonymousClassDeclaration)


def test_jdtast::anonymousclassdeclaration_constructor_exists():
    assert callable(JDTAST::AnonymousClassDeclaration.__init__)


def test_jdtast::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(JDTAST::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_imember_is_not_abstract():
    assert not inspect.isabstract(IMember)


def test_imember_constructor_exists():
    assert callable(IMember.__init__)


def test_imember_constructor_args():
    sig = inspect.signature(IMember.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::imethod_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IMethod)


def test_jdtast::imethod_constructor_exists():
    assert callable(JDTAST::IMethod.__init__)


def test_jdtast::imethod_constructor_args():
    sig = inspect.signature(JDTAST::IMethod.__init__)
    params = list(sig.parameters.keys())
    assert "isMainMethod" in params, "Missing parameter 'isMainMethod'"
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "exceptionTypes" in params, "Missing parameter 'exceptionTypes'"
    assert "isConstructor" in params, "Missing parameter 'isConstructor'"

def test_jdtast::imethod_has_isMainMethod():
    assert hasattr(JDTAST::IMethod, "isMainMethod")
    descriptor = None
    for klass in JDTAST::IMethod.__mro__:
        if "isMainMethod" in klass.__dict__:
            descriptor = klass.__dict__["isMainMethod"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::imethod_has_returnType():
    assert hasattr(JDTAST::IMethod, "returnType")
    descriptor = None
    for klass in JDTAST::IMethod.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::imethod_has_exceptionTypes():
    assert hasattr(JDTAST::IMethod, "exceptionTypes")
    descriptor = None
    for klass in JDTAST::IMethod.__mro__:
        if "exceptionTypes" in klass.__dict__:
            descriptor = klass.__dict__["exceptionTypes"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::imethod_has_isConstructor():
    assert hasattr(JDTAST::IMethod, "isConstructor")
    descriptor = None
    for klass in JDTAST::IMethod.__mro__:
        if "isConstructor" in klass.__dict__:
            descriptor = klass.__dict__["isConstructor"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::ifield_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IField)


def test_jdtast::ifield_constructor_exists():
    assert callable(JDTAST::IField.__init__)


def test_jdtast::ifield_constructor_args():
    sig = inspect.signature(JDTAST::IField.__init__)
    params = list(sig.parameters.keys())
    assert "typeSignature" in params, "Missing parameter 'typeSignature'"
    assert "constant" in params, "Missing parameter 'constant'"
    assert "isEnumConstant" in params, "Missing parameter 'isEnumConstant'"
    assert "isTransient" in params, "Missing parameter 'isTransient'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_jdtast::ifield_has_typeSignature():
    assert hasattr(JDTAST::IField, "typeSignature")
    descriptor = None
    for klass in JDTAST::IField.__mro__:
        if "typeSignature" in klass.__dict__:
            descriptor = klass.__dict__["typeSignature"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::ifield_has_constant():
    assert hasattr(JDTAST::IField, "constant")
    descriptor = None
    for klass in JDTAST::IField.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::ifield_has_isEnumConstant():
    assert hasattr(JDTAST::IField, "isEnumConstant")
    descriptor = None
    for klass in JDTAST::IField.__mro__:
        if "isEnumConstant" in klass.__dict__:
            descriptor = klass.__dict__["isEnumConstant"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::ifield_has_isTransient():
    assert hasattr(JDTAST::IField, "isTransient")
    descriptor = None
    for klass in JDTAST::IField.__mro__:
        if "isTransient" in klass.__dict__:
            descriptor = klass.__dict__["isTransient"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::ifield_has_isVolatile():
    assert hasattr(JDTAST::IField, "isVolatile")
    descriptor = None
    for klass in JDTAST::IField.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::iinitializer_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IInitializer)


def test_jdtast::iinitializer_constructor_exists():
    assert callable(JDTAST::IInitializer.__init__)


def test_jdtast::iinitializer_constructor_args():
    sig = inspect.signature(JDTAST::IInitializer.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::isourcerange_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ISourceRange)


def test_jdtast::isourcerange_constructor_exists():
    assert callable(JDTAST::ISourceRange.__init__)


def test_jdtast::isourcerange_constructor_args():
    sig = inspect.signature(JDTAST::ISourceRange.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "length" in params, "Missing parameter 'length'"

def test_jdtast::isourcerange_has_offset():
    assert hasattr(JDTAST::ISourceRange, "offset")
    descriptor = None
    for klass in JDTAST::ISourceRange.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::isourcerange_has_length():
    assert hasattr(JDTAST::ISourceRange, "length")
    descriptor = None
    for klass in JDTAST::ISourceRange.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::isourcereference_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ISourceReference)


def test_jdtast::isourcereference_constructor_exists():
    assert callable(JDTAST::ISourceReference.__init__)


def test_jdtast::isourcereference_constructor_args():
    sig = inspect.signature(JDTAST::ISourceReference.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_jdtast::isourcereference_has_source():
    assert hasattr(JDTAST::ISourceReference, "source")
    descriptor = None
    for klass in JDTAST::ISourceReference.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::compilationunit_is_not_abstract():
    assert not inspect.isabstract(JDTAST::CompilationUnit)


def test_jdtast::compilationunit_constructor_exists():
    assert callable(JDTAST::CompilationUnit.__init__)


def test_jdtast::compilationunit_constructor_args():
    sig = inspect.signature(JDTAST::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(IPackageFragmentRoot)


def test_ipackagefragmentroot_constructor_exists():
    assert callable(IPackageFragmentRoot.__init__)


def test_ipackagefragmentroot_constructor_args():
    sig = inspect.signature(IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::sourcepackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(JDTAST::SourcePackageFragmentRoot)


def test_jdtast::sourcepackagefragmentroot_constructor_exists():
    assert callable(JDTAST::SourcePackageFragmentRoot.__init__)


def test_jdtast::sourcepackagefragmentroot_constructor_args():
    sig = inspect.signature(JDTAST::SourcePackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::binarypackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(JDTAST::BinaryPackageFragmentRoot)


def test_jdtast::binarypackagefragmentroot_constructor_exists():
    assert callable(JDTAST::BinaryPackageFragmentRoot.__init__)


def test_jdtast::binarypackagefragmentroot_constructor_args():
    sig = inspect.signature(JDTAST::BinaryPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_ijavaelement_is_not_abstract():
    assert not inspect.isabstract(IJavaElement)


def test_ijavaelement_constructor_exists():
    assert callable(IJavaElement.__init__)


def test_ijavaelement_constructor_args():
    sig = inspect.signature(IJavaElement.__init__)
    params = list(sig.parameters.keys())



def test_physicalelement_is_not_abstract():
    assert not inspect.isabstract(PhysicalElement)


def test_physicalelement_constructor_exists():
    assert callable(PhysicalElement.__init__)


def test_physicalelement_constructor_args():
    sig = inspect.signature(PhysicalElement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IPackageFragment)


def test_jdtast::ipackagefragment_constructor_exists():
    assert callable(JDTAST::IPackageFragment.__init__)


def test_jdtast::ipackagefragment_constructor_args():
    sig = inspect.signature(JDTAST::IPackageFragment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefaultPackage" in params, "Missing parameter 'isDefaultPackage'"

def test_jdtast::ipackagefragment_has_isDefaultPackage():
    assert hasattr(JDTAST::IPackageFragment, "isDefaultPackage")
    descriptor = None
    for klass in JDTAST::IPackageFragment.__mro__:
        if "isDefaultPackage" in klass.__dict__:
            descriptor = klass.__dict__["isDefaultPackage"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::ijavaproject_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IJavaProject)


def test_jdtast::ijavaproject_constructor_exists():
    assert callable(JDTAST::IJavaProject.__init__)


def test_jdtast::ijavaproject_constructor_args():
    sig = inspect.signature(JDTAST::IJavaProject.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IPackageFragmentRoot)


def test_jdtast::ipackagefragmentroot_constructor_exists():
    assert callable(JDTAST::IPackageFragmentRoot.__init__)


def test_jdtast::ipackagefragmentroot_constructor_args():
    sig = inspect.signature(JDTAST::IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::ijavamodel_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IJavaModel)


def test_jdtast::ijavamodel_constructor_exists():
    assert callable(JDTAST::IJavaModel.__init__)


def test_jdtast::ijavamodel_constructor_args():
    sig = inspect.signature(JDTAST::IJavaModel.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::physicalelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::PhysicalElement)


def test_jdtast::physicalelement_constructor_exists():
    assert callable(JDTAST::PhysicalElement.__init__)


def test_jdtast::physicalelement_constructor_args():
    sig = inspect.signature(JDTAST::PhysicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_jdtast::physicalelement_has_path():
    assert hasattr(JDTAST::PhysicalElement, "path")
    descriptor = None
    for klass in JDTAST::PhysicalElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::physicalelement_has_isReadOnly():
    assert hasattr(JDTAST::PhysicalElement, "isReadOnly")
    descriptor = None
    for klass in JDTAST::PhysicalElement.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::ijavaelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IJavaElement)


def test_jdtast::ijavaelement_constructor_exists():
    assert callable(JDTAST::IJavaElement.__init__)


def test_jdtast::ijavaelement_constructor_args():
    sig = inspect.signature(JDTAST::IJavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"

def test_jdtast::ijavaelement_has_elementName():
    assert hasattr(JDTAST::IJavaElement, "elementName")
    descriptor = None
    for klass in JDTAST::IJavaElement.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::itype_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IType)


def test_jdtast::itype_constructor_exists():
    assert callable(JDTAST::IType.__init__)


def test_jdtast::itype_constructor_args():
    sig = inspect.signature(JDTAST::IType.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedParametrizedName" in params, "Missing parameter 'fullyQualifiedParametrizedName'"
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_jdtast::itype_has_fullyQualifiedParametrizedName():
    assert hasattr(JDTAST::IType, "fullyQualifiedParametrizedName")
    descriptor = None
    for klass in JDTAST::IType.__mro__:
        if "fullyQualifiedParametrizedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedParametrizedName"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::itype_has_fullyQualifiedName():
    assert hasattr(JDTAST::IType, "fullyQualifiedName")
    descriptor = None
    for klass in JDTAST::IType.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_ityperoot_is_not_abstract():
    assert not inspect.isabstract(ITypeRoot)


def test_ityperoot_constructor_exists():
    assert callable(ITypeRoot.__init__)


def test_ityperoot_constructor_args():
    sig = inspect.signature(ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_isourcereference_is_not_abstract():
    assert not inspect.isabstract(ISourceReference)


def test_isourcereference_constructor_exists():
    assert callable(ISourceReference.__init__)


def test_isourcereference_constructor_args():
    sig = inspect.signature(ISourceReference.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::itypeparameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ITypeParameter)


def test_jdtast::itypeparameter_constructor_exists():
    assert callable(JDTAST::ITypeParameter.__init__)


def test_jdtast::itypeparameter_constructor_args():
    sig = inspect.signature(JDTAST::ITypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "bounds" in params, "Missing parameter 'bounds'"

def test_jdtast::itypeparameter_has_bounds():
    assert hasattr(JDTAST::ITypeParameter, "bounds")
    descriptor = None
    for klass in JDTAST::ITypeParameter.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::iimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IImportDeclaration)


def test_jdtast::iimportdeclaration_constructor_exists():
    assert callable(JDTAST::IImportDeclaration.__init__)


def test_jdtast::iimportdeclaration_constructor_args():
    sig = inspect.signature(JDTAST::IImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isOnDemand" in params, "Missing parameter 'isOnDemand'"

def test_jdtast::iimportdeclaration_has_isStatic():
    assert hasattr(JDTAST::IImportDeclaration, "isStatic")
    descriptor = None
    for klass in JDTAST::IImportDeclaration.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::iimportdeclaration_has_isOnDemand():
    assert hasattr(JDTAST::IImportDeclaration, "isOnDemand")
    descriptor = None
    for klass in JDTAST::IImportDeclaration.__mro__:
        if "isOnDemand" in klass.__dict__:
            descriptor = klass.__dict__["isOnDemand"]
            break
    assert isinstance(descriptor, property)



def test_jdtast::imember_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IMember)


def test_jdtast::imember_constructor_exists():
    assert callable(JDTAST::IMember.__init__)


def test_jdtast::imember_constructor_args():
    sig = inspect.signature(JDTAST::IMember.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::ityperoot_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ITypeRoot)


def test_jdtast::ityperoot_constructor_exists():
    assert callable(JDTAST::ITypeRoot.__init__)


def test_jdtast::ityperoot_constructor_args():
    sig = inspect.signature(JDTAST::ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::icompilationunit_is_not_abstract():
    assert not inspect.isabstract(JDTAST::ICompilationUnit)


def test_jdtast::icompilationunit_constructor_exists():
    assert callable(JDTAST::ICompilationUnit.__init__)


def test_jdtast::icompilationunit_constructor_args():
    sig = inspect.signature(JDTAST::ICompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_jdtast::iclassfile_is_not_abstract():
    assert not inspect.isabstract(JDTAST::IClassFile)


def test_jdtast::iclassfile_constructor_exists():
    assert callable(JDTAST::IClassFile.__init__)


def test_jdtast::iclassfile_constructor_args():
    sig = inspect.signature(JDTAST::IClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "isInterface" in params, "Missing parameter 'isInterface'"
    assert "isClass" in params, "Missing parameter 'isClass'"

def test_jdtast::iclassfile_has_isInterface():
    assert hasattr(JDTAST::IClassFile, "isInterface")
    descriptor = None
    for klass in JDTAST::IClassFile.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)

def test_jdtast::iclassfile_has_isClass():
    assert hasattr(JDTAST::IClassFile, "isClass")
    descriptor = None
    for klass in JDTAST::IClassFile.__mro__:
        if "isClass" in klass.__dict__:
            descriptor = klass.__dict__["isClass"]
            break
    assert isinstance(descriptor, property)

def test_assignmentoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorKind is not None

def test_assignmentoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorKind]
    expected_literals = [
        "assign",
        "minus_assign",
        "plus_assign",
        "right_shift_signed_assign",
        "left_shift_assign",
        "bit_or_assign",
        "divide_assign",
        "bit_xor_assign",
        "right_shift_unsigned_assign",
        "bit_and_assign",
        "remainder_assign",
        "times_assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "and_",
        "conditional_and",
        "right_shift_signed",
        "plus",
        "less_equals",
        "greater_equals",
        "left_shift",
        "times",
        "minus",
        "greater",
        "equals",
        "less",
        "or_",
        "right_shift_unsigned",
        "conditional_or",
        "not_equals",
        "divide",
        "xor",
        "remainder",
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
        "increment",
        "plus",
        "minus",
        "not_",
        "decrement",
        "complement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionOperatorKind"

def test_modifiers_exists():
    # Check that the Enumeration exists
    assert Modifiers is not None

def test_modifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Modifiers]
    expected_literals = [
        "public",
        "synchronized",
        "deprecated",
        "annotation",
        "protected",
        "static",
        "interface",
        "synthetic",
        "super",
        "native",
        "bridge",
        "default",
        "enum",
        "abstract",
        "strictfp",
        "volatile",
        "transient",
        "varargs",
        "private",
        "final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Modifiers"

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
Name_strategy = st.builds(
    Name,
)
JDTAST::QualifiedName_strategy = st.builds(
    JDTAST::QualifiedName,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
Annotation_strategy = st.builds(
    Annotation,
)
JDTAST::SingleMemberAnnotation_strategy = st.builds(
    JDTAST::SingleMemberAnnotation,
)
JDTAST::NormalAnnotation_strategy = st.builds(
    JDTAST::NormalAnnotation,
)
JDTAST::MarkerAnnotation_strategy = st.builds(
    JDTAST::MarkerAnnotation,
)
Type_strategy = st.builds(
    Type,
)
JDTAST::ParameterizedType_strategy = st.builds(
    JDTAST::ParameterizedType,
)
JDTAST::WildcardType_strategy = st.builds(
    JDTAST::WildcardType,
    upperBound=
        safe_text
)
JDTAST::SimpleType_strategy = st.builds(
    JDTAST::SimpleType,
)
JDTAST::QualifiedType_strategy = st.builds(
    JDTAST::QualifiedType,
)
JDTAST::PrimitiveType_strategy = st.builds(
    JDTAST::PrimitiveType,
    code=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
JDTAST::TypeDeclarationStatement_strategy = st.builds(
    JDTAST::TypeDeclarationStatement,
)
JDTAST::ThrowStatement_strategy = st.builds(
    JDTAST::ThrowStatement,
)
JDTAST::SwitchCase_strategy = st.builds(
    JDTAST::SwitchCase,
    default=
        safe_text
)
JDTAST::SuperConstructorInvocation_strategy = st.builds(
    JDTAST::SuperConstructorInvocation,
)
JDTAST::EmptyStatement_strategy = st.builds(
    JDTAST::EmptyStatement,
)
JDTAST::DoStatement_strategy = st.builds(
    JDTAST::DoStatement,
)
JDTAST::ExpressionStatement_strategy = st.builds(
    JDTAST::ExpressionStatement,
)
JDTAST::EnhancedForStatement_strategy = st.builds(
    JDTAST::EnhancedForStatement,
)
JDTAST::VariableDeclarationStatement_strategy = st.builds(
    JDTAST::VariableDeclarationStatement,
)
JDTAST::ReturnStatement_strategy = st.builds(
    JDTAST::ReturnStatement,
)
JDTAST::ForStatement_strategy = st.builds(
    JDTAST::ForStatement,
)
JDTAST::SynchronizedStatement_strategy = st.builds(
    JDTAST::SynchronizedStatement,
)
JDTAST::BreakStatement_strategy = st.builds(
    JDTAST::BreakStatement,
)
JDTAST::LabeledStatement_strategy = st.builds(
    JDTAST::LabeledStatement,
)
JDTAST::SwitchStatement_strategy = st.builds(
    JDTAST::SwitchStatement,
)
JDTAST::WhileStatement_strategy = st.builds(
    JDTAST::WhileStatement,
)
JDTAST::ContinueStatement_strategy = st.builds(
    JDTAST::ContinueStatement,
)
JDTAST::TryStatement_strategy = st.builds(
    JDTAST::TryStatement,
)
JDTAST::IfStatement_strategy = st.builds(
    JDTAST::IfStatement,
)
JDTAST::ConstructorInvocation_strategy = st.builds(
    JDTAST::ConstructorInvocation,
)
JDTAST::AssertStatement_strategy = st.builds(
    JDTAST::AssertStatement,
)
Expression_strategy = st.builds(
    Expression,
)
JDTAST::FieldAccess_strategy = st.builds(
    JDTAST::FieldAccess,
)
JDTAST::PostfixExpression_strategy = st.builds(
    JDTAST::PostfixExpression,
    operator=
        safe_text
)
JDTAST::ArrayAccess_strategy = st.builds(
    JDTAST::ArrayAccess,
)
JDTAST::InfixExpression_strategy = st.builds(
    JDTAST::InfixExpression,
    operator=
        safe_text
)
JDTAST::CastExpression_strategy = st.builds(
    JDTAST::CastExpression,
)
JDTAST::SuperMethodInvocation_strategy = st.builds(
    JDTAST::SuperMethodInvocation,
)
JDTAST::ThisExpression_strategy = st.builds(
    JDTAST::ThisExpression,
)
JDTAST::StringLiteral_strategy = st.builds(
    JDTAST::StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
JDTAST::TypeLiteral_strategy = st.builds(
    JDTAST::TypeLiteral,
)
JDTAST::Assignment_strategy = st.builds(
    JDTAST::Assignment,
    operator=
        safe_text
)
JDTAST::MethodInvocation_strategy = st.builds(
    JDTAST::MethodInvocation,
)
JDTAST::ConditionalExpression_strategy = st.builds(
    JDTAST::ConditionalExpression,
)
JDTAST::ClassInstanceCreation_strategy = st.builds(
    JDTAST::ClassInstanceCreation,
)
JDTAST::BooleanLiteral_strategy = st.builds(
    JDTAST::BooleanLiteral,
    booleanValue=
        safe_text
)
JDTAST::NullLiteral_strategy = st.builds(
    JDTAST::NullLiteral,
)
JDTAST::InstanceofExpression_strategy = st.builds(
    JDTAST::InstanceofExpression,
)
JDTAST::SuperFieldAccess_strategy = st.builds(
    JDTAST::SuperFieldAccess,
)
JDTAST::ParenthesizedExpression_strategy = st.builds(
    JDTAST::ParenthesizedExpression,
)
JDTAST::NumberLiteral_strategy = st.builds(
    JDTAST::NumberLiteral,
    token=
        safe_text
)
JDTAST::CharacterLiteral_strategy = st.builds(
    JDTAST::CharacterLiteral,
    charValue=
        safe_text,
    escapedValue=
        safe_text
)
JDTAST::VariableDeclarationExpression_strategy = st.builds(
    JDTAST::VariableDeclarationExpression,
)
JDTAST::PrefixExpression_strategy = st.builds(
    JDTAST::PrefixExpression,
    operator=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
JDTAST::LineComment_strategy = st.builds(
    JDTAST::LineComment,
)
JDTAST::BlockComment_strategy = st.builds(
    JDTAST::BlockComment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JDTAST::EnumDeclaration_strategy = st.builds(
    JDTAST::EnumDeclaration,
)
JDTAST::TypeDeclaration_strategy = st.builds(
    JDTAST::TypeDeclaration,
    interface=
        safe_text
)
JDTAST::AnnotationTypeDeclaration_strategy = st.builds(
    JDTAST::AnnotationTypeDeclaration,
)
JDTAST::ArrayType_strategy = st.builds(
    JDTAST::ArrayType,
    dimensions=
        safe_text
)
JDTAST::ArrayInitializer_strategy = st.builds(
    JDTAST::ArrayInitializer,
)
JDTAST::ArrayCreation_strategy = st.builds(
    JDTAST::ArrayCreation,
)
JDTAST::VariableDeclarationFragment_strategy = st.builds(
    JDTAST::VariableDeclarationFragment,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JDTAST::EnumConstantDeclaration_strategy = st.builds(
    JDTAST::EnumConstantDeclaration,
)
JDTAST::MethodDeclaration_strategy = st.builds(
    JDTAST::MethodDeclaration,
    extraDimensions=
        safe_text,
    varargs=
        safe_text,
    constructor=
        safe_text
)
JDTAST::FieldDeclaration_strategy = st.builds(
    JDTAST::FieldDeclaration,
)
JDTAST::Initializer_strategy = st.builds(
    JDTAST::Initializer,
)
JDTAST::AnnotationTypeMemberDeclaration_strategy = st.builds(
    JDTAST::AnnotationTypeMemberDeclaration,
)
JDTAST::SimpleName_strategy = st.builds(
    JDTAST::SimpleName,
    declaration=
        safe_text,
    identifier=
        safe_text
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
JDTAST::Annotation_strategy = st.builds(
    JDTAST::Annotation,
)
JDTAST::Name_strategy = st.builds(
    JDTAST::Name,
    fullyQualifiedName=
        safe_text
)
JDTAST::AbstractTypeDeclaration_strategy = st.builds(
    JDTAST::AbstractTypeDeclaration,
    localTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text,
    memberTypeDeclaration=
        safe_text
)
JDTAST::SingleVariableDeclaration_strategy = st.builds(
    JDTAST::SingleVariableDeclaration,
    varargs=
        safe_text
)
JDTAST::Block_strategy = st.builds(
    JDTAST::Block,
)
JDTAST::ASTNode_strategy = st.builds(
    JDTAST::ASTNode,
)
JDTAST::AST_strategy = st.builds(
    JDTAST::AST,
)
JDTAST::Parameter_strategy = st.builds(
    JDTAST::Parameter,
    type=
        safe_text,
    name=
        safe_text
)
JDTAST::Javadoc_strategy = st.builds(
    JDTAST::Javadoc,
)
JDTAST::ExtendedModifier_strategy = st.builds(
    JDTAST::ExtendedModifier,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JDTAST::PackageDeclaration_strategy = st.builds(
    JDTAST::PackageDeclaration,
)
JDTAST::Expression_strategy = st.builds(
    JDTAST::Expression,
    resolveUnboxing=
        safe_text,
    resolveBoxing=
        safe_text
)
JDTAST::MethodRefParameter_strategy = st.builds(
    JDTAST::MethodRefParameter,
    varargs=
        safe_text
)
JDTAST::Statement_strategy = st.builds(
    JDTAST::Statement,
)
JDTAST::MemberRef_strategy = st.builds(
    JDTAST::MemberRef,
)
JDTAST::ImportDeclaration_strategy = st.builds(
    JDTAST::ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
JDTAST::Type_strategy = st.builds(
    JDTAST::Type,
)
JDTAST::VariableDeclaration_strategy = st.builds(
    JDTAST::VariableDeclaration,
    extraDimensions=
        safe_text
)
JDTAST::Modifier_strategy = st.builds(
    JDTAST::Modifier,
    strictfp=
        safe_text,
    abstract=
        safe_text,
    static=
        safe_text,
    native=
        safe_text,
    protected=
        safe_text,
    transient=
        safe_text,
    final=
        safe_text,
    public=
        safe_text,
    volatile=
        safe_text,
    none=
        safe_text,
    synchronized=
        safe_text,
    private=
        safe_text
)
JDTAST::MemberValuePair_strategy = st.builds(
    JDTAST::MemberValuePair,
)
JDTAST::MethodRef_strategy = st.builds(
    JDTAST::MethodRef,
)
JDTAST::Comment_strategy = st.builds(
    JDTAST::Comment,
)
JDTAST::TagElement_strategy = st.builds(
    JDTAST::TagElement,
    nested=
        safe_text,
    tagName=
        safe_text
)
JDTAST::TextElement_strategy = st.builds(
    JDTAST::TextElement,
    text=
        safe_text
)
JDTAST::BodyDeclaration_strategy = st.builds(
    JDTAST::BodyDeclaration,
)
JDTAST::CatchClause_strategy = st.builds(
    JDTAST::CatchClause,
)
JDTAST::TypeParameter_strategy = st.builds(
    JDTAST::TypeParameter,
)
JDTAST::AnonymousClassDeclaration_strategy = st.builds(
    JDTAST::AnonymousClassDeclaration,
)
IMember_strategy = st.builds(
    IMember,
)
JDTAST::IMethod_strategy = st.builds(
    JDTAST::IMethod,
    isMainMethod=
        safe_text,
    returnType=
        safe_text,
    exceptionTypes=
        safe_text,
    isConstructor=
        safe_text
)
JDTAST::IField_strategy = st.builds(
    JDTAST::IField,
    typeSignature=
        safe_text,
    constant=
        safe_text,
    isEnumConstant=
        safe_text,
    isTransient=
        safe_text,
    isVolatile=
        safe_text
)
JDTAST::IInitializer_strategy = st.builds(
    JDTAST::IInitializer,
)
JDTAST::ISourceRange_strategy = st.builds(
    JDTAST::ISourceRange,
    offset=
        safe_text,
    length=
        safe_text
)
JDTAST::ISourceReference_strategy = st.builds(
    JDTAST::ISourceReference,
    source=
        safe_text
)
JDTAST::CompilationUnit_strategy = st.builds(
    JDTAST::CompilationUnit,
)
IPackageFragmentRoot_strategy = st.builds(
    IPackageFragmentRoot,
)
JDTAST::SourcePackageFragmentRoot_strategy = st.builds(
    JDTAST::SourcePackageFragmentRoot,
)
JDTAST::BinaryPackageFragmentRoot_strategy = st.builds(
    JDTAST::BinaryPackageFragmentRoot,
)
IJavaElement_strategy = st.builds(
    IJavaElement,
)
PhysicalElement_strategy = st.builds(
    PhysicalElement,
)
JDTAST::IPackageFragment_strategy = st.builds(
    JDTAST::IPackageFragment,
    isDefaultPackage=
        safe_text
)
JDTAST::IJavaProject_strategy = st.builds(
    JDTAST::IJavaProject,
)
JDTAST::IPackageFragmentRoot_strategy = st.builds(
    JDTAST::IPackageFragmentRoot,
)
JDTAST::IJavaModel_strategy = st.builds(
    JDTAST::IJavaModel,
)
JDTAST::PhysicalElement_strategy = st.builds(
    JDTAST::PhysicalElement,
    path=
        safe_text,
    isReadOnly=
        safe_text
)
JDTAST::IJavaElement_strategy = st.builds(
    JDTAST::IJavaElement,
    elementName=
        safe_text
)
JDTAST::IType_strategy = st.builds(
    JDTAST::IType,
    fullyQualifiedParametrizedName=
        safe_text,
    fullyQualifiedName=
        safe_text
)
ITypeRoot_strategy = st.builds(
    ITypeRoot,
)
ISourceReference_strategy = st.builds(
    ISourceReference,
)
JDTAST::ITypeParameter_strategy = st.builds(
    JDTAST::ITypeParameter,
    bounds=
        safe_text
)
JDTAST::IImportDeclaration_strategy = st.builds(
    JDTAST::IImportDeclaration,
    isStatic=
        safe_text,
    isOnDemand=
        safe_text
)
JDTAST::IMember_strategy = st.builds(
    JDTAST::IMember,
)
JDTAST::ITypeRoot_strategy = st.builds(
    JDTAST::ITypeRoot,
)
JDTAST::ICompilationUnit_strategy = st.builds(
    JDTAST::ICompilationUnit,
)
JDTAST::IClassFile_strategy = st.builds(
    JDTAST::IClassFile,
    isInterface=
        safe_text,
    isClass=
        safe_text
)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=JDTAST::QualifiedName_strategy)
@settings(max_examples=50)
def test_jdtast::qualifiedname_instantiation(instance):
    assert isinstance(instance, JDTAST::QualifiedName)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=JDTAST::SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_jdtast::singlememberannotation_instantiation(instance):
    assert isinstance(instance, JDTAST::SingleMemberAnnotation)

@given(instance=JDTAST::NormalAnnotation_strategy)
@settings(max_examples=50)
def test_jdtast::normalannotation_instantiation(instance):
    assert isinstance(instance, JDTAST::NormalAnnotation)

@given(instance=JDTAST::MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_jdtast::markerannotation_instantiation(instance):
    assert isinstance(instance, JDTAST::MarkerAnnotation)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JDTAST::ParameterizedType_strategy)
@settings(max_examples=50)
def test_jdtast::parameterizedtype_instantiation(instance):
    assert isinstance(instance, JDTAST::ParameterizedType)

@given(instance=JDTAST::WildcardType_strategy)
@settings(max_examples=50)
def test_jdtast::wildcardtype_instantiation(instance):
    assert isinstance(instance, JDTAST::WildcardType)

@given(instance=JDTAST::WildcardType_strategy)
def test_jdtast::wildcardtype_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=JDTAST::WildcardType_strategy)
def test_jdtast::wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=JDTAST::SimpleType_strategy)
@settings(max_examples=50)
def test_jdtast::simpletype_instantiation(instance):
    assert isinstance(instance, JDTAST::SimpleType)

@given(instance=JDTAST::QualifiedType_strategy)
@settings(max_examples=50)
def test_jdtast::qualifiedtype_instantiation(instance):
    assert isinstance(instance, JDTAST::QualifiedType)

@given(instance=JDTAST::PrimitiveType_strategy)
@settings(max_examples=50)
def test_jdtast::primitivetype_instantiation(instance):
    assert isinstance(instance, JDTAST::PrimitiveType)

@given(instance=JDTAST::PrimitiveType_strategy)
def test_jdtast::primitivetype_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=JDTAST::PrimitiveType_strategy)
def test_jdtast::primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=JDTAST::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_jdtast::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::TypeDeclarationStatement)

@given(instance=JDTAST::ThrowStatement_strategy)
@settings(max_examples=50)
def test_jdtast::throwstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::ThrowStatement)

@given(instance=JDTAST::SwitchCase_strategy)
@settings(max_examples=50)
def test_jdtast::switchcase_instantiation(instance):
    assert isinstance(instance, JDTAST::SwitchCase)

@given(instance=JDTAST::SwitchCase_strategy)
def test_jdtast::switchcase_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=JDTAST::SwitchCase_strategy)
def test_jdtast::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=JDTAST::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_jdtast::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST::SuperConstructorInvocation)

@given(instance=JDTAST::EmptyStatement_strategy)
@settings(max_examples=50)
def test_jdtast::emptystatement_instantiation(instance):
    assert isinstance(instance, JDTAST::EmptyStatement)

@given(instance=JDTAST::DoStatement_strategy)
@settings(max_examples=50)
def test_jdtast::dostatement_instantiation(instance):
    assert isinstance(instance, JDTAST::DoStatement)

@given(instance=JDTAST::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_jdtast::expressionstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::ExpressionStatement)

@given(instance=JDTAST::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_jdtast::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::EnhancedForStatement)

@given(instance=JDTAST::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_jdtast::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::VariableDeclarationStatement)

@given(instance=JDTAST::ReturnStatement_strategy)
@settings(max_examples=50)
def test_jdtast::returnstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::ReturnStatement)

@given(instance=JDTAST::ForStatement_strategy)
@settings(max_examples=50)
def test_jdtast::forstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::ForStatement)

@given(instance=JDTAST::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_jdtast::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::SynchronizedStatement)

@given(instance=JDTAST::BreakStatement_strategy)
@settings(max_examples=50)
def test_jdtast::breakstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::BreakStatement)

@given(instance=JDTAST::LabeledStatement_strategy)
@settings(max_examples=50)
def test_jdtast::labeledstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::LabeledStatement)

@given(instance=JDTAST::SwitchStatement_strategy)
@settings(max_examples=50)
def test_jdtast::switchstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::SwitchStatement)

@given(instance=JDTAST::WhileStatement_strategy)
@settings(max_examples=50)
def test_jdtast::whilestatement_instantiation(instance):
    assert isinstance(instance, JDTAST::WhileStatement)

@given(instance=JDTAST::ContinueStatement_strategy)
@settings(max_examples=50)
def test_jdtast::continuestatement_instantiation(instance):
    assert isinstance(instance, JDTAST::ContinueStatement)

@given(instance=JDTAST::TryStatement_strategy)
@settings(max_examples=50)
def test_jdtast::trystatement_instantiation(instance):
    assert isinstance(instance, JDTAST::TryStatement)

@given(instance=JDTAST::IfStatement_strategy)
@settings(max_examples=50)
def test_jdtast::ifstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::IfStatement)

@given(instance=JDTAST::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_jdtast::constructorinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST::ConstructorInvocation)

@given(instance=JDTAST::AssertStatement_strategy)
@settings(max_examples=50)
def test_jdtast::assertstatement_instantiation(instance):
    assert isinstance(instance, JDTAST::AssertStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JDTAST::FieldAccess_strategy)
@settings(max_examples=50)
def test_jdtast::fieldaccess_instantiation(instance):
    assert isinstance(instance, JDTAST::FieldAccess)

@given(instance=JDTAST::PostfixExpression_strategy)
@settings(max_examples=50)
def test_jdtast::postfixexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::PostfixExpression)

@given(instance=JDTAST::PostfixExpression_strategy)
def test_jdtast::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JDTAST::PostfixExpression_strategy)
def test_jdtast::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST::ArrayAccess_strategy)
@settings(max_examples=50)
def test_jdtast::arrayaccess_instantiation(instance):
    assert isinstance(instance, JDTAST::ArrayAccess)

@given(instance=JDTAST::InfixExpression_strategy)
@settings(max_examples=50)
def test_jdtast::infixexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::InfixExpression)

@given(instance=JDTAST::InfixExpression_strategy)
def test_jdtast::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JDTAST::InfixExpression_strategy)
def test_jdtast::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST::CastExpression_strategy)
@settings(max_examples=50)
def test_jdtast::castexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::CastExpression)

@given(instance=JDTAST::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_jdtast::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST::SuperMethodInvocation)

@given(instance=JDTAST::ThisExpression_strategy)
@settings(max_examples=50)
def test_jdtast::thisexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::ThisExpression)

@given(instance=JDTAST::StringLiteral_strategy)
@settings(max_examples=50)
def test_jdtast::stringliteral_instantiation(instance):
    assert isinstance(instance, JDTAST::StringLiteral)

@given(instance=JDTAST::StringLiteral_strategy)
def test_jdtast::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=JDTAST::StringLiteral_strategy)
def test_jdtast::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=JDTAST::StringLiteral_strategy)
def test_jdtast::stringliteral_literalValue_type(instance):
    assert isinstance(instance.literalValue, str)


@given(instance=JDTAST::StringLiteral_strategy)
def test_jdtast::stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=JDTAST::TypeLiteral_strategy)
@settings(max_examples=50)
def test_jdtast::typeliteral_instantiation(instance):
    assert isinstance(instance, JDTAST::TypeLiteral)

@given(instance=JDTAST::Assignment_strategy)
@settings(max_examples=50)
def test_jdtast::assignment_instantiation(instance):
    assert isinstance(instance, JDTAST::Assignment)

@given(instance=JDTAST::Assignment_strategy)
def test_jdtast::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JDTAST::Assignment_strategy)
def test_jdtast::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST::MethodInvocation_strategy)
@settings(max_examples=50)
def test_jdtast::methodinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST::MethodInvocation)

@given(instance=JDTAST::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_jdtast::conditionalexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::ConditionalExpression)

@given(instance=JDTAST::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_jdtast::classinstancecreation_instantiation(instance):
    assert isinstance(instance, JDTAST::ClassInstanceCreation)

@given(instance=JDTAST::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_jdtast::booleanliteral_instantiation(instance):
    assert isinstance(instance, JDTAST::BooleanLiteral)

@given(instance=JDTAST::BooleanLiteral_strategy)
def test_jdtast::booleanliteral_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, str)


@given(instance=JDTAST::BooleanLiteral_strategy)
def test_jdtast::booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=JDTAST::NullLiteral_strategy)
@settings(max_examples=50)
def test_jdtast::nullliteral_instantiation(instance):
    assert isinstance(instance, JDTAST::NullLiteral)

@given(instance=JDTAST::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_jdtast::instanceofexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::InstanceofExpression)

@given(instance=JDTAST::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_jdtast::superfieldaccess_instantiation(instance):
    assert isinstance(instance, JDTAST::SuperFieldAccess)

@given(instance=JDTAST::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_jdtast::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::ParenthesizedExpression)

@given(instance=JDTAST::NumberLiteral_strategy)
@settings(max_examples=50)
def test_jdtast::numberliteral_instantiation(instance):
    assert isinstance(instance, JDTAST::NumberLiteral)

@given(instance=JDTAST::NumberLiteral_strategy)
def test_jdtast::numberliteral_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=JDTAST::NumberLiteral_strategy)
def test_jdtast::numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=JDTAST::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_jdtast::characterliteral_instantiation(instance):
    assert isinstance(instance, JDTAST::CharacterLiteral)

@given(instance=JDTAST::CharacterLiteral_strategy)
def test_jdtast::characterliteral_charValue_type(instance):
    assert isinstance(instance.charValue, str)


@given(instance=JDTAST::CharacterLiteral_strategy)
def test_jdtast::characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=JDTAST::CharacterLiteral_strategy)
def test_jdtast::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=JDTAST::CharacterLiteral_strategy)
def test_jdtast::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=JDTAST::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_jdtast::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::VariableDeclarationExpression)

@given(instance=JDTAST::PrefixExpression_strategy)
@settings(max_examples=50)
def test_jdtast::prefixexpression_instantiation(instance):
    assert isinstance(instance, JDTAST::PrefixExpression)

@given(instance=JDTAST::PrefixExpression_strategy)
def test_jdtast::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=JDTAST::PrefixExpression_strategy)
def test_jdtast::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=JDTAST::LineComment_strategy)
@settings(max_examples=50)
def test_jdtast::linecomment_instantiation(instance):
    assert isinstance(instance, JDTAST::LineComment)

@given(instance=JDTAST::BlockComment_strategy)
@settings(max_examples=50)
def test_jdtast::blockcomment_instantiation(instance):
    assert isinstance(instance, JDTAST::BlockComment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JDTAST::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::enumdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::EnumDeclaration)

@given(instance=JDTAST::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::typedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::TypeDeclaration)

@given(instance=JDTAST::TypeDeclaration_strategy)
def test_jdtast::typedeclaration_interface_type(instance):
    assert isinstance(instance.interface, str)


@given(instance=JDTAST::TypeDeclaration_strategy)
def test_jdtast::typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=JDTAST::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::AnnotationTypeDeclaration)

@given(instance=JDTAST::ArrayType_strategy)
@settings(max_examples=50)
def test_jdtast::arraytype_instantiation(instance):
    assert isinstance(instance, JDTAST::ArrayType)

@given(instance=JDTAST::ArrayType_strategy)
def test_jdtast::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=JDTAST::ArrayType_strategy)
def test_jdtast::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=JDTAST::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_jdtast::arrayinitializer_instantiation(instance):
    assert isinstance(instance, JDTAST::ArrayInitializer)

@given(instance=JDTAST::ArrayCreation_strategy)
@settings(max_examples=50)
def test_jdtast::arraycreation_instantiation(instance):
    assert isinstance(instance, JDTAST::ArrayCreation)

@given(instance=JDTAST::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_jdtast::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, JDTAST::VariableDeclarationFragment)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JDTAST::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::EnumConstantDeclaration)

@given(instance=JDTAST::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::methoddeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::MethodDeclaration)

@given(instance=JDTAST::MethodDeclaration_strategy)
def test_jdtast::methoddeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=JDTAST::MethodDeclaration_strategy)
def test_jdtast::methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=JDTAST::MethodDeclaration_strategy)
def test_jdtast::methoddeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=JDTAST::MethodDeclaration_strategy)
def test_jdtast::methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JDTAST::MethodDeclaration_strategy)
def test_jdtast::methoddeclaration_constructor_type(instance):
    assert isinstance(instance.constructor, str)


@given(instance=JDTAST::MethodDeclaration_strategy)
def test_jdtast::methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=JDTAST::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::fielddeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::FieldDeclaration)

@given(instance=JDTAST::Initializer_strategy)
@settings(max_examples=50)
def test_jdtast::initializer_instantiation(instance):
    assert isinstance(instance, JDTAST::Initializer)

@given(instance=JDTAST::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::AnnotationTypeMemberDeclaration)

@given(instance=JDTAST::SimpleName_strategy)
@settings(max_examples=50)
def test_jdtast::simplename_instantiation(instance):
    assert isinstance(instance, JDTAST::SimpleName)

@given(instance=JDTAST::SimpleName_strategy)
def test_jdtast::simplename_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=JDTAST::SimpleName_strategy)
def test_jdtast::simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=JDTAST::SimpleName_strategy)
def test_jdtast::simplename_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=JDTAST::SimpleName_strategy)
def test_jdtast::simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=JDTAST::Annotation_strategy)
@settings(max_examples=50)
def test_jdtast::annotation_instantiation(instance):
    assert isinstance(instance, JDTAST::Annotation)

@given(instance=JDTAST::Name_strategy)
@settings(max_examples=50)
def test_jdtast::name_instantiation(instance):
    assert isinstance(instance, JDTAST::Name)

@given(instance=JDTAST::Name_strategy)
def test_jdtast::name_fullyQualifiedName_type(instance):
    assert isinstance(instance.fullyQualifiedName, str)


@given(instance=JDTAST::Name_strategy)
def test_jdtast::name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::AbstractTypeDeclaration)

@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
def test_jdtast::abstracttypedeclaration_localTypeDeclaration_type(instance):
    assert isinstance(instance.localTypeDeclaration, str)


@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
def test_jdtast::abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original

@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
def test_jdtast::abstracttypedeclaration_packageMemberTypeDeclaration_type(instance):
    assert isinstance(instance.packageMemberTypeDeclaration, str)


@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
def test_jdtast::abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original

@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
def test_jdtast::abstracttypedeclaration_memberTypeDeclaration_type(instance):
    assert isinstance(instance.memberTypeDeclaration, str)


@given(instance=JDTAST::AbstractTypeDeclaration_strategy)
def test_jdtast::abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original

@given(instance=JDTAST::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::SingleVariableDeclaration)

@given(instance=JDTAST::SingleVariableDeclaration_strategy)
def test_jdtast::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=JDTAST::SingleVariableDeclaration_strategy)
def test_jdtast::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JDTAST::Block_strategy)
@settings(max_examples=50)
def test_jdtast::block_instantiation(instance):
    assert isinstance(instance, JDTAST::Block)

@given(instance=JDTAST::ASTNode_strategy)
@settings(max_examples=50)
def test_jdtast::astnode_instantiation(instance):
    assert isinstance(instance, JDTAST::ASTNode)

@given(instance=JDTAST::AST_strategy)
@settings(max_examples=50)
def test_jdtast::ast_instantiation(instance):
    assert isinstance(instance, JDTAST::AST)

@given(instance=JDTAST::Parameter_strategy)
@settings(max_examples=50)
def test_jdtast::parameter_instantiation(instance):
    assert isinstance(instance, JDTAST::Parameter)

@given(instance=JDTAST::Parameter_strategy)
def test_jdtast::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JDTAST::Parameter_strategy)
def test_jdtast::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JDTAST::Parameter_strategy)
def test_jdtast::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JDTAST::Parameter_strategy)
def test_jdtast::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JDTAST::Javadoc_strategy)
@settings(max_examples=50)
def test_jdtast::javadoc_instantiation(instance):
    assert isinstance(instance, JDTAST::Javadoc)

@given(instance=JDTAST::ExtendedModifier_strategy)
@settings(max_examples=50)
def test_jdtast::extendedmodifier_instantiation(instance):
    assert isinstance(instance, JDTAST::ExtendedModifier)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JDTAST::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::packagedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::PackageDeclaration)

@given(instance=JDTAST::Expression_strategy)
@settings(max_examples=50)
def test_jdtast::expression_instantiation(instance):
    assert isinstance(instance, JDTAST::Expression)

@given(instance=JDTAST::Expression_strategy)
def test_jdtast::expression_resolveUnboxing_type(instance):
    assert isinstance(instance.resolveUnboxing, str)


@given(instance=JDTAST::Expression_strategy)
def test_jdtast::expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original

@given(instance=JDTAST::Expression_strategy)
def test_jdtast::expression_resolveBoxing_type(instance):
    assert isinstance(instance.resolveBoxing, str)


@given(instance=JDTAST::Expression_strategy)
def test_jdtast::expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original

@given(instance=JDTAST::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_jdtast::methodrefparameter_instantiation(instance):
    assert isinstance(instance, JDTAST::MethodRefParameter)

@given(instance=JDTAST::MethodRefParameter_strategy)
def test_jdtast::methodrefparameter_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=JDTAST::MethodRefParameter_strategy)
def test_jdtast::methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JDTAST::Statement_strategy)
@settings(max_examples=50)
def test_jdtast::statement_instantiation(instance):
    assert isinstance(instance, JDTAST::Statement)

@given(instance=JDTAST::MemberRef_strategy)
@settings(max_examples=50)
def test_jdtast::memberref_instantiation(instance):
    assert isinstance(instance, JDTAST::MemberRef)

@given(instance=JDTAST::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::importdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::ImportDeclaration)

@given(instance=JDTAST::ImportDeclaration_strategy)
def test_jdtast::importdeclaration_onDemand_type(instance):
    assert isinstance(instance.onDemand, str)


@given(instance=JDTAST::ImportDeclaration_strategy)
def test_jdtast::importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original

@given(instance=JDTAST::ImportDeclaration_strategy)
def test_jdtast::importdeclaration_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=JDTAST::ImportDeclaration_strategy)
def test_jdtast::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=JDTAST::Type_strategy)
@settings(max_examples=50)
def test_jdtast::type_instantiation(instance):
    assert isinstance(instance, JDTAST::Type)

@given(instance=JDTAST::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::variabledeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::VariableDeclaration)

@given(instance=JDTAST::VariableDeclaration_strategy)
def test_jdtast::variabledeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=JDTAST::VariableDeclaration_strategy)
def test_jdtast::variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=JDTAST::Modifier_strategy)
@settings(max_examples=50)
def test_jdtast::modifier_instantiation(instance):
    assert isinstance(instance, JDTAST::Modifier)

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_native_type(instance):
    assert isinstance(instance.native, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_transient_type(instance):
    assert isinstance(instance.transient, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_public_type(instance):
    assert isinstance(instance.public, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_none_type(instance):
    assert isinstance(instance.none, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_private_type(instance):
    assert isinstance(instance.private, str)


@given(instance=JDTAST::Modifier_strategy)
def test_jdtast::modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=JDTAST::MemberValuePair_strategy)
@settings(max_examples=50)
def test_jdtast::membervaluepair_instantiation(instance):
    assert isinstance(instance, JDTAST::MemberValuePair)

@given(instance=JDTAST::MethodRef_strategy)
@settings(max_examples=50)
def test_jdtast::methodref_instantiation(instance):
    assert isinstance(instance, JDTAST::MethodRef)

@given(instance=JDTAST::Comment_strategy)
@settings(max_examples=50)
def test_jdtast::comment_instantiation(instance):
    assert isinstance(instance, JDTAST::Comment)

@given(instance=JDTAST::TagElement_strategy)
@settings(max_examples=50)
def test_jdtast::tagelement_instantiation(instance):
    assert isinstance(instance, JDTAST::TagElement)

@given(instance=JDTAST::TagElement_strategy)
def test_jdtast::tagelement_nested_type(instance):
    assert isinstance(instance.nested, str)


@given(instance=JDTAST::TagElement_strategy)
def test_jdtast::tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original

@given(instance=JDTAST::TagElement_strategy)
def test_jdtast::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=JDTAST::TagElement_strategy)
def test_jdtast::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=JDTAST::TextElement_strategy)
@settings(max_examples=50)
def test_jdtast::textelement_instantiation(instance):
    assert isinstance(instance, JDTAST::TextElement)

@given(instance=JDTAST::TextElement_strategy)
def test_jdtast::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=JDTAST::TextElement_strategy)
def test_jdtast::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=JDTAST::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::bodydeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::BodyDeclaration)

@given(instance=JDTAST::CatchClause_strategy)
@settings(max_examples=50)
def test_jdtast::catchclause_instantiation(instance):
    assert isinstance(instance, JDTAST::CatchClause)

@given(instance=JDTAST::TypeParameter_strategy)
@settings(max_examples=50)
def test_jdtast::typeparameter_instantiation(instance):
    assert isinstance(instance, JDTAST::TypeParameter)

@given(instance=JDTAST::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::AnonymousClassDeclaration)

@given(instance=IMember_strategy)
@settings(max_examples=50)
def test_imember_instantiation(instance):
    assert isinstance(instance, IMember)

@given(instance=JDTAST::IMethod_strategy)
@settings(max_examples=50)
def test_jdtast::imethod_instantiation(instance):
    assert isinstance(instance, JDTAST::IMethod)

@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_isMainMethod_type(instance):
    assert isinstance(instance.isMainMethod, str)


@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_isMainMethod_setter(instance):
    original = instance.isMainMethod
    instance.isMainMethod = original
    assert instance.isMainMethod == original

@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_exceptionTypes_type(instance):
    assert isinstance(instance.exceptionTypes, str)


@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_exceptionTypes_setter(instance):
    original = instance.exceptionTypes
    instance.exceptionTypes = original
    assert instance.exceptionTypes == original

@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_isConstructor_type(instance):
    assert isinstance(instance.isConstructor, str)


@given(instance=JDTAST::IMethod_strategy)
def test_jdtast::imethod_isConstructor_setter(instance):
    original = instance.isConstructor
    instance.isConstructor = original
    assert instance.isConstructor == original

@given(instance=JDTAST::IField_strategy)
@settings(max_examples=50)
def test_jdtast::ifield_instantiation(instance):
    assert isinstance(instance, JDTAST::IField)

@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_typeSignature_type(instance):
    assert isinstance(instance.typeSignature, str)


@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_typeSignature_setter(instance):
    original = instance.typeSignature
    instance.typeSignature = original
    assert instance.typeSignature == original

@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_isEnumConstant_type(instance):
    assert isinstance(instance.isEnumConstant, str)


@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_isEnumConstant_setter(instance):
    original = instance.isEnumConstant
    instance.isEnumConstant = original
    assert instance.isEnumConstant == original

@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_isTransient_type(instance):
    assert isinstance(instance.isTransient, str)


@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_isTransient_setter(instance):
    original = instance.isTransient
    instance.isTransient = original
    assert instance.isTransient == original

@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, str)


@given(instance=JDTAST::IField_strategy)
def test_jdtast::ifield_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=JDTAST::IInitializer_strategy)
@settings(max_examples=50)
def test_jdtast::iinitializer_instantiation(instance):
    assert isinstance(instance, JDTAST::IInitializer)

@given(instance=JDTAST::ISourceRange_strategy)
@settings(max_examples=50)
def test_jdtast::isourcerange_instantiation(instance):
    assert isinstance(instance, JDTAST::ISourceRange)

@given(instance=JDTAST::ISourceRange_strategy)
def test_jdtast::isourcerange_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=JDTAST::ISourceRange_strategy)
def test_jdtast::isourcerange_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=JDTAST::ISourceRange_strategy)
def test_jdtast::isourcerange_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=JDTAST::ISourceRange_strategy)
def test_jdtast::isourcerange_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=JDTAST::ISourceReference_strategy)
@settings(max_examples=50)
def test_jdtast::isourcereference_instantiation(instance):
    assert isinstance(instance, JDTAST::ISourceReference)

@given(instance=JDTAST::ISourceReference_strategy)
def test_jdtast::isourcereference_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=JDTAST::ISourceReference_strategy)
def test_jdtast::isourcereference_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=JDTAST::CompilationUnit_strategy)
@settings(max_examples=50)
def test_jdtast::compilationunit_instantiation(instance):
    assert isinstance(instance, JDTAST::CompilationUnit)

@given(instance=IPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_ipackagefragmentroot_instantiation(instance):
    assert isinstance(instance, IPackageFragmentRoot)

@given(instance=JDTAST::SourcePackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_jdtast::sourcepackagefragmentroot_instantiation(instance):
    assert isinstance(instance, JDTAST::SourcePackageFragmentRoot)

@given(instance=JDTAST::BinaryPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_jdtast::binarypackagefragmentroot_instantiation(instance):
    assert isinstance(instance, JDTAST::BinaryPackageFragmentRoot)

@given(instance=IJavaElement_strategy)
@settings(max_examples=50)
def test_ijavaelement_instantiation(instance):
    assert isinstance(instance, IJavaElement)

@given(instance=PhysicalElement_strategy)
@settings(max_examples=50)
def test_physicalelement_instantiation(instance):
    assert isinstance(instance, PhysicalElement)

@given(instance=JDTAST::IPackageFragment_strategy)
@settings(max_examples=50)
def test_jdtast::ipackagefragment_instantiation(instance):
    assert isinstance(instance, JDTAST::IPackageFragment)

@given(instance=JDTAST::IPackageFragment_strategy)
def test_jdtast::ipackagefragment_isDefaultPackage_type(instance):
    assert isinstance(instance.isDefaultPackage, str)


@given(instance=JDTAST::IPackageFragment_strategy)
def test_jdtast::ipackagefragment_isDefaultPackage_setter(instance):
    original = instance.isDefaultPackage
    instance.isDefaultPackage = original
    assert instance.isDefaultPackage == original

@given(instance=JDTAST::IJavaProject_strategy)
@settings(max_examples=50)
def test_jdtast::ijavaproject_instantiation(instance):
    assert isinstance(instance, JDTAST::IJavaProject)

@given(instance=JDTAST::IPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_jdtast::ipackagefragmentroot_instantiation(instance):
    assert isinstance(instance, JDTAST::IPackageFragmentRoot)

@given(instance=JDTAST::IJavaModel_strategy)
@settings(max_examples=50)
def test_jdtast::ijavamodel_instantiation(instance):
    assert isinstance(instance, JDTAST::IJavaModel)

@given(instance=JDTAST::PhysicalElement_strategy)
@settings(max_examples=50)
def test_jdtast::physicalelement_instantiation(instance):
    assert isinstance(instance, JDTAST::PhysicalElement)

@given(instance=JDTAST::PhysicalElement_strategy)
def test_jdtast::physicalelement_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=JDTAST::PhysicalElement_strategy)
def test_jdtast::physicalelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=JDTAST::PhysicalElement_strategy)
def test_jdtast::physicalelement_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=JDTAST::PhysicalElement_strategy)
def test_jdtast::physicalelement_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=JDTAST::IJavaElement_strategy)
@settings(max_examples=50)
def test_jdtast::ijavaelement_instantiation(instance):
    assert isinstance(instance, JDTAST::IJavaElement)

@given(instance=JDTAST::IJavaElement_strategy)
def test_jdtast::ijavaelement_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=JDTAST::IJavaElement_strategy)
def test_jdtast::ijavaelement_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=JDTAST::IType_strategy)
@settings(max_examples=50)
def test_jdtast::itype_instantiation(instance):
    assert isinstance(instance, JDTAST::IType)

@given(instance=JDTAST::IType_strategy)
def test_jdtast::itype_fullyQualifiedParametrizedName_type(instance):
    assert isinstance(instance.fullyQualifiedParametrizedName, str)


@given(instance=JDTAST::IType_strategy)
def test_jdtast::itype_fullyQualifiedParametrizedName_setter(instance):
    original = instance.fullyQualifiedParametrizedName
    instance.fullyQualifiedParametrizedName = original
    assert instance.fullyQualifiedParametrizedName == original

@given(instance=JDTAST::IType_strategy)
def test_jdtast::itype_fullyQualifiedName_type(instance):
    assert isinstance(instance.fullyQualifiedName, str)


@given(instance=JDTAST::IType_strategy)
def test_jdtast::itype_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=ITypeRoot_strategy)
@settings(max_examples=50)
def test_ityperoot_instantiation(instance):
    assert isinstance(instance, ITypeRoot)

@given(instance=ISourceReference_strategy)
@settings(max_examples=50)
def test_isourcereference_instantiation(instance):
    assert isinstance(instance, ISourceReference)

@given(instance=JDTAST::ITypeParameter_strategy)
@settings(max_examples=50)
def test_jdtast::itypeparameter_instantiation(instance):
    assert isinstance(instance, JDTAST::ITypeParameter)

@given(instance=JDTAST::ITypeParameter_strategy)
def test_jdtast::itypeparameter_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=JDTAST::ITypeParameter_strategy)
def test_jdtast::itypeparameter_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=JDTAST::IImportDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast::iimportdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST::IImportDeclaration)

@given(instance=JDTAST::IImportDeclaration_strategy)
def test_jdtast::iimportdeclaration_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=JDTAST::IImportDeclaration_strategy)
def test_jdtast::iimportdeclaration_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=JDTAST::IImportDeclaration_strategy)
def test_jdtast::iimportdeclaration_isOnDemand_type(instance):
    assert isinstance(instance.isOnDemand, str)


@given(instance=JDTAST::IImportDeclaration_strategy)
def test_jdtast::iimportdeclaration_isOnDemand_setter(instance):
    original = instance.isOnDemand
    instance.isOnDemand = original
    assert instance.isOnDemand == original

@given(instance=JDTAST::IMember_strategy)
@settings(max_examples=50)
def test_jdtast::imember_instantiation(instance):
    assert isinstance(instance, JDTAST::IMember)

@given(instance=JDTAST::ITypeRoot_strategy)
@settings(max_examples=50)
def test_jdtast::ityperoot_instantiation(instance):
    assert isinstance(instance, JDTAST::ITypeRoot)

@given(instance=JDTAST::ICompilationUnit_strategy)
@settings(max_examples=50)
def test_jdtast::icompilationunit_instantiation(instance):
    assert isinstance(instance, JDTAST::ICompilationUnit)

@given(instance=JDTAST::IClassFile_strategy)
@settings(max_examples=50)
def test_jdtast::iclassfile_instantiation(instance):
    assert isinstance(instance, JDTAST::IClassFile)

@given(instance=JDTAST::IClassFile_strategy)
def test_jdtast::iclassfile_isInterface_type(instance):
    assert isinstance(instance.isInterface, str)


@given(instance=JDTAST::IClassFile_strategy)
def test_jdtast::iclassfile_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original

@given(instance=JDTAST::IClassFile_strategy)
def test_jdtast::iclassfile_isClass_type(instance):
    assert isinstance(instance.isClass, str)


@given(instance=JDTAST::IClassFile_strategy)
def test_jdtast::iclassfile_isClass_setter(instance):
    original = instance.isClass
    instance.isClass = original
    assert instance.isClass == original
