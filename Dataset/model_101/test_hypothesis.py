import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    DOM::ConstructorInvocation,
    DOM::ExpressionStatement,
    DOM::Block,
    DOM::EmptyStatement,
    DOM::BreakStatement,
    DOM::EnhancedForStatement,
    DOM::DoStatement,
    DOM::ContinueStatement,
    DOM::AssertStatement,
    ArrayType,
    ArrayInitializer,
    EnumConstantDeclaration,
    TypeParameter,
    TagElement,
    VariableDeclarationFragment,
    AnonymousClassDeclaration,
    Annotation,
    SimpleName,
    Name,
    DOM::ExtendedModifier,
    Type,
    MethodRefParameter,
    Expression,
    DOM::SuperMethodInvocation,
    DOM::ConditionalExpression,
    DOM::BooleanLiteral,
    DOM::VariableDeclarationExpression,
    DOM::ArrayInitializer,
    DOM::TypeLiteral,
    DOM::NullLiteral,
    DOM::CharacterLiteral,
    DOM::ClassInstanceCreation,
    DOM::FieldAccess,
    DOM::Name,
    DOM::SuperFieldAccess,
    DOM::ThisExpression,
    DOM::InstanceofExpression,
    DOM::ParenthesizedExpression,
    DOM::Assignment,
    DOM::StringLiteral,
    DOM::InfixExpression,
    DOM::PrefixExpression,
    DOM::ArrayAccess,
    DOM::ArrayCreation,
    DOM::CastExpression,
    DOM::NumberLiteral,
    DOM::PostfixExpression,
    DOM::MethodInvocation,
    BodyDeclaration,
    DOM::Initializer,
    DOM::MethodDeclaration,
    DOM::AnnotationTypeMemberDeclaration,
    DOM::AbstractTypeDeclaration,
    DOM::EnumConstantDeclaration,
    DOM::FieldDeclaration,
    DOM::ASTNode,
    ASTNode,
    DOM::PackageDeclaration,
    DOM::Statement,
    DOM::VariableDeclaration,
    DOM::MethodRefParameter,
    DOM::TextElement,
    DOM::ImportDeclaration,
    DOM::TagElement,
    DOM::MemberValuePair,
    DOM::MemberRef,
    DOM::AnonymousClassDeclaration,
    DOM::TypeParameter,
    DOM::Type,
    DOM::MethodRef,
    DOM::BodyDeclaration,
    DOM::AST,
    DOM::Expression,
    AbstractTypeDeclaration,
    DOM::TypeDeclaration,
    DOM::EnumDeclaration,
    DOM::AnnotationTypeDeclaration,
    ImportDeclaration,
    PackageDeclaration,
    Comment,
    DOM::Javadoc,
    DOM::LineComment,
    DOM::BlockComment,
    DOM::CompilationUnit,
    DOM::Comment,
    SingleVariableDeclaration,
    Block,
    DOM::CatchClause,
    Javadoc,
    ExtendedModifier,
    DOM::Modifier,
    DOM::Annotation,
    ITypeParameter,
    DOM::SingleMemberAnnotation,
    MemberValuePair,
    DOM::NormalAnnotation,
    DOM::QualifiedType,
    DOM::PrimitiveType,
    DOM::MarkerAnnotation,
    DOM::SimpleName,
    DOM::QualifiedName,
    VariableDeclaration,
    DOM::VariableDeclarationFragment,
    DOM::SingleVariableDeclaration,
    DOM::WildcardType,
    DOM::SimpleType,
    DOM::TypeDeclarationStatement,
    CatchClause,
    DOM::TryStatement,
    DOM::ParameterizedType,
    DOM::ArrayType,
    DOM::WhileStatement,
    DOM::VariableDeclarationStatement,
    DOM::SuperConstructorInvocation,
    DOM::ThrowStatement,
    DOM::SynchronizedStatement,
    DOM::SwitchStatement,
    DOM::SwitchCase,
    DOM::ForStatement,
    DOM::ReturnStatement,
    DOM::LabeledStatement,
    DOM::IfStatement,
    IMethod,
    IField,
    IInitializer,
    IMember,
    Core::IInitializer,
    Core::IField,
    Core::IType,
    Core::Parameter,
    Core::ISourceRange,
    Parameter,
    Core::IMethod,
    CompilationUnit,
    IImportDeclaration,
    IType,
    ITypeRoot,
    Core::IClassFile,
    Core::ICompilationUnit,
    ISourceReference,
    ICompilationUnit,
    IClassFile,
    IPackageFragment,
    ISourceRange,
    Core::ISourceReference,
    PhysicalElement,
    Core::IJavaModel,
    Core::PhysicalElement,
    Core::IJavaElement,
    IJavaElement,
    Core::IImportDeclaration,
    Core::IPackageFragmentRoot,
    Core::IMember,
    Core::IPackageFragment,
    Core::ITypeRoot,
    Core::ITypeParameter,
    Core::IJavaProject,
    IPackageFragmentRoot,
    Core::BinaryPackageFragmentRoot,
    Core::SourcePackageFragmentRoot,
    IJavaProject,
    InfixExpressionOperatorKind,
    PostfixExpressionOperatorKind,
    AssignmentOperatorKind,
    Modifiers,
    PrefixExpressionOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::ConstructorInvocation)


def test_dom::constructorinvocation_constructor_exists():
    assert callable(DOM::ConstructorInvocation.__init__)


def test_dom::constructorinvocation_constructor_args():
    sig = inspect.signature(DOM::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ExpressionStatement)


def test_dom::expressionstatement_constructor_exists():
    assert callable(DOM::ExpressionStatement.__init__)


def test_dom::expressionstatement_constructor_args():
    sig = inspect.signature(DOM::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::block_is_not_abstract():
    assert not inspect.isabstract(DOM::Block)


def test_dom::block_constructor_exists():
    assert callable(DOM::Block.__init__)


def test_dom::block_constructor_args():
    sig = inspect.signature(DOM::Block.__init__)
    params = list(sig.parameters.keys())



def test_dom::emptystatement_is_not_abstract():
    assert not inspect.isabstract(DOM::EmptyStatement)


def test_dom::emptystatement_constructor_exists():
    assert callable(DOM::EmptyStatement.__init__)


def test_dom::emptystatement_constructor_args():
    sig = inspect.signature(DOM::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::breakstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::BreakStatement)


def test_dom::breakstatement_constructor_exists():
    assert callable(DOM::BreakStatement.__init__)


def test_dom::breakstatement_constructor_args():
    sig = inspect.signature(DOM::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::EnhancedForStatement)


def test_dom::enhancedforstatement_constructor_exists():
    assert callable(DOM::EnhancedForStatement.__init__)


def test_dom::enhancedforstatement_constructor_args():
    sig = inspect.signature(DOM::EnhancedForStatement.__init__)
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



def test_dom::assertstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::AssertStatement)


def test_dom::assertstatement_constructor_exists():
    assert callable(DOM::AssertStatement.__init__)


def test_dom::assertstatement_constructor_args():
    sig = inspect.signature(DOM::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumConstantDeclaration)


def test_enumconstantdeclaration_constructor_exists():
    assert callable(EnumConstantDeclaration.__init__)


def test_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typeparameter_is_not_abstract():
    assert not inspect.isabstract(TypeParameter)


def test_typeparameter_constructor_exists():
    assert callable(TypeParameter.__init__)


def test_typeparameter_constructor_args():
    sig = inspect.signature(TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_tagelement_is_not_abstract():
    assert not inspect.isabstract(TagElement)


def test_tagelement_constructor_exists():
    assert callable(TagElement.__init__)


def test_tagelement_constructor_args():
    sig = inspect.signature(TagElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationFragment)


def test_variabledeclarationfragment_constructor_exists():
    assert callable(VariableDeclarationFragment.__init__)


def test_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(AnonymousClassDeclaration)


def test_anonymousclassdeclaration_constructor_exists():
    assert callable(AnonymousClassDeclaration.__init__)


def test_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_simplename_is_not_abstract():
    assert not inspect.isabstract(SimpleName)


def test_simplename_constructor_exists():
    assert callable(SimpleName.__init__)


def test_simplename_constructor_args():
    sig = inspect.signature(SimpleName.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_dom::extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(DOM::ExtendedModifier)


def test_dom::extendedmodifier_constructor_exists():
    assert callable(DOM::ExtendedModifier.__init__)


def test_dom::extendedmodifier_constructor_args():
    sig = inspect.signature(DOM::ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(MethodRefParameter)


def test_methodrefparameter_constructor_exists():
    assert callable(MethodRefParameter.__init__)


def test_methodrefparameter_constructor_args():
    sig = inspect.signature(MethodRefParameter.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::SuperMethodInvocation)


def test_dom::supermethodinvocation_constructor_exists():
    assert callable(DOM::SuperMethodInvocation.__init__)


def test_dom::supermethodinvocation_constructor_args():
    sig = inspect.signature(DOM::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::ConditionalExpression)


def test_dom::conditionalexpression_constructor_exists():
    assert callable(DOM::ConditionalExpression.__init__)


def test_dom::conditionalexpression_constructor_args():
    sig = inspect.signature(DOM::ConditionalExpression.__init__)
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



def test_dom::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclarationExpression)


def test_dom::variabledeclarationexpression_constructor_exists():
    assert callable(DOM::VariableDeclarationExpression.__init__)


def test_dom::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(DOM::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayInitializer)


def test_dom::arrayinitializer_constructor_exists():
    assert callable(DOM::ArrayInitializer.__init__)


def test_dom::arrayinitializer_constructor_args():
    sig = inspect.signature(DOM::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dom::typeliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeLiteral)


def test_dom::typeliteral_constructor_exists():
    assert callable(DOM::TypeLiteral.__init__)


def test_dom::typeliteral_constructor_args():
    sig = inspect.signature(DOM::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dom::nullliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::NullLiteral)


def test_dom::nullliteral_constructor_exists():
    assert callable(DOM::NullLiteral.__init__)


def test_dom::nullliteral_constructor_args():
    sig = inspect.signature(DOM::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dom::characterliteral_is_not_abstract():
    assert not inspect.isabstract(DOM::CharacterLiteral)


def test_dom::characterliteral_constructor_exists():
    assert callable(DOM::CharacterLiteral.__init__)


def test_dom::characterliteral_constructor_args():
    sig = inspect.signature(DOM::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "charValue" in params, "Missing parameter 'charValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_dom::characterliteral_has_charValue():
    assert hasattr(DOM::CharacterLiteral, "charValue")
    descriptor = None
    for klass in DOM::CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)

def test_dom::characterliteral_has_escapedValue():
    assert hasattr(DOM::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in DOM::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_dom::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(DOM::ClassInstanceCreation)


def test_dom::classinstancecreation_constructor_exists():
    assert callable(DOM::ClassInstanceCreation.__init__)


def test_dom::classinstancecreation_constructor_args():
    sig = inspect.signature(DOM::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_dom::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM::FieldAccess)


def test_dom::fieldaccess_constructor_exists():
    assert callable(DOM::FieldAccess.__init__)


def test_dom::fieldaccess_constructor_args():
    sig = inspect.signature(DOM::FieldAccess.__init__)
    params = list(sig.parameters.keys())



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



def test_dom::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM::SuperFieldAccess)


def test_dom::superfieldaccess_constructor_exists():
    assert callable(DOM::SuperFieldAccess.__init__)


def test_dom::superfieldaccess_constructor_args():
    sig = inspect.signature(DOM::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom::thisexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::ThisExpression)


def test_dom::thisexpression_constructor_exists():
    assert callable(DOM::ThisExpression.__init__)


def test_dom::thisexpression_constructor_args():
    sig = inspect.signature(DOM::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::InstanceofExpression)


def test_dom::instanceofexpression_constructor_exists():
    assert callable(DOM::InstanceofExpression.__init__)


def test_dom::instanceofexpression_constructor_args():
    sig = inspect.signature(DOM::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::ParenthesizedExpression)


def test_dom::parenthesizedexpression_constructor_exists():
    assert callable(DOM::ParenthesizedExpression.__init__)


def test_dom::parenthesizedexpression_constructor_args():
    sig = inspect.signature(DOM::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



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



def test_dom::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayAccess)


def test_dom::arrayaccess_constructor_exists():
    assert callable(DOM::ArrayAccess.__init__)


def test_dom::arrayaccess_constructor_args():
    sig = inspect.signature(DOM::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom::arraycreation_is_not_abstract():
    assert not inspect.isabstract(DOM::ArrayCreation)


def test_dom::arraycreation_constructor_exists():
    assert callable(DOM::ArrayCreation.__init__)


def test_dom::arraycreation_constructor_args():
    sig = inspect.signature(DOM::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_dom::castexpression_is_not_abstract():
    assert not inspect.isabstract(DOM::CastExpression)


def test_dom::castexpression_constructor_exists():
    assert callable(DOM::CastExpression.__init__)


def test_dom::castexpression_constructor_args():
    sig = inspect.signature(DOM::CastExpression.__init__)
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



def test_dom::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodInvocation)


def test_dom::methodinvocation_constructor_exists():
    assert callable(DOM::MethodInvocation.__init__)


def test_dom::methodinvocation_constructor_args():
    sig = inspect.signature(DOM::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::initializer_is_not_abstract():
    assert not inspect.isabstract(DOM::Initializer)


def test_dom::initializer_constructor_exists():
    assert callable(DOM::Initializer.__init__)


def test_dom::initializer_constructor_args():
    sig = inspect.signature(DOM::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_dom::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodDeclaration)


def test_dom::methoddeclaration_constructor_exists():
    assert callable(DOM::MethodDeclaration.__init__)


def test_dom::methoddeclaration_constructor_args():
    sig = inspect.signature(DOM::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"

def test_dom::methoddeclaration_has_extraDimensions():
    assert hasattr(DOM::MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in DOM::MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
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

def test_dom::methoddeclaration_has_constructor():
    assert hasattr(DOM::MethodDeclaration, "constructor")
    descriptor = None
    for klass in DOM::MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)



def test_dom::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AnnotationTypeMemberDeclaration)


def test_dom::annotationtypememberdeclaration_constructor_exists():
    assert callable(DOM::AnnotationTypeMemberDeclaration.__init__)


def test_dom::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(DOM::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



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



def test_dom::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::EnumConstantDeclaration)


def test_dom::enumconstantdeclaration_constructor_exists():
    assert callable(DOM::EnumConstantDeclaration.__init__)


def test_dom::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(DOM::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::FieldDeclaration)


def test_dom::fielddeclaration_constructor_exists():
    assert callable(DOM::FieldDeclaration.__init__)


def test_dom::fielddeclaration_constructor_args():
    sig = inspect.signature(DOM::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::astnode_is_not_abstract():
    assert not inspect.isabstract(DOM::ASTNode)


def test_dom::astnode_constructor_exists():
    assert callable(DOM::ASTNode.__init__)


def test_dom::astnode_constructor_args():
    sig = inspect.signature(DOM::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_dom::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::PackageDeclaration)


def test_dom::packagedeclaration_constructor_exists():
    assert callable(DOM::PackageDeclaration.__init__)


def test_dom::packagedeclaration_constructor_args():
    sig = inspect.signature(DOM::PackageDeclaration.__init__)
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



def test_dom::tagelement_is_not_abstract():
    assert not inspect.isabstract(DOM::TagElement)


def test_dom::tagelement_constructor_exists():
    assert callable(DOM::TagElement.__init__)


def test_dom::tagelement_constructor_args():
    sig = inspect.signature(DOM::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "nested" in params, "Missing parameter 'nested'"
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_dom::tagelement_has_nested():
    assert hasattr(DOM::TagElement, "nested")
    descriptor = None
    for klass in DOM::TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)

def test_dom::tagelement_has_tagName():
    assert hasattr(DOM::TagElement, "tagName")
    descriptor = None
    for klass in DOM::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_dom::membervaluepair_is_not_abstract():
    assert not inspect.isabstract(DOM::MemberValuePair)


def test_dom::membervaluepair_constructor_exists():
    assert callable(DOM::MemberValuePair.__init__)


def test_dom::membervaluepair_constructor_args():
    sig = inspect.signature(DOM::MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_dom::memberref_is_not_abstract():
    assert not inspect.isabstract(DOM::MemberRef)


def test_dom::memberref_constructor_exists():
    assert callable(DOM::MemberRef.__init__)


def test_dom::memberref_constructor_args():
    sig = inspect.signature(DOM::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_dom::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AnonymousClassDeclaration)


def test_dom::anonymousclassdeclaration_constructor_exists():
    assert callable(DOM::AnonymousClassDeclaration.__init__)


def test_dom::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(DOM::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::typeparameter_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeParameter)


def test_dom::typeparameter_constructor_exists():
    assert callable(DOM::TypeParameter.__init__)


def test_dom::typeparameter_constructor_args():
    sig = inspect.signature(DOM::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::type_is_not_abstract():
    assert not inspect.isabstract(DOM::Type)


def test_dom::type_constructor_exists():
    assert callable(DOM::Type.__init__)


def test_dom::type_constructor_args():
    sig = inspect.signature(DOM::Type.__init__)
    params = list(sig.parameters.keys())



def test_dom::methodref_is_not_abstract():
    assert not inspect.isabstract(DOM::MethodRef)


def test_dom::methodref_constructor_exists():
    assert callable(DOM::MethodRef.__init__)


def test_dom::methodref_constructor_args():
    sig = inspect.signature(DOM::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_dom::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::BodyDeclaration)


def test_dom::bodydeclaration_constructor_exists():
    assert callable(DOM::BodyDeclaration.__init__)


def test_dom::bodydeclaration_constructor_args():
    sig = inspect.signature(DOM::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::ast_is_not_abstract():
    assert not inspect.isabstract(DOM::AST)


def test_dom::ast_constructor_exists():
    assert callable(DOM::AST.__init__)


def test_dom::ast_constructor_args():
    sig = inspect.signature(DOM::AST.__init__)
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



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
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



def test_dom::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM::AnnotationTypeDeclaration)


def test_dom::annotationtypedeclaration_constructor_exists():
    assert callable(DOM::AnnotationTypeDeclaration.__init__)


def test_dom::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(DOM::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(ImportDeclaration)


def test_importdeclaration_constructor_exists():
    assert callable(ImportDeclaration.__init__)


def test_importdeclaration_constructor_args():
    sig = inspect.signature(ImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(PackageDeclaration)


def test_packagedeclaration_constructor_exists():
    assert callable(PackageDeclaration.__init__)


def test_packagedeclaration_constructor_args():
    sig = inspect.signature(PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_dom::javadoc_is_not_abstract():
    assert not inspect.isabstract(DOM::Javadoc)


def test_dom::javadoc_constructor_exists():
    assert callable(DOM::Javadoc.__init__)


def test_dom::javadoc_constructor_args():
    sig = inspect.signature(DOM::Javadoc.__init__)
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



def test_dom::compilationunit_is_not_abstract():
    assert not inspect.isabstract(DOM::CompilationUnit)


def test_dom::compilationunit_constructor_exists():
    assert callable(DOM::CompilationUnit.__init__)


def test_dom::compilationunit_constructor_args():
    sig = inspect.signature(DOM::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_dom::comment_is_not_abstract():
    assert not inspect.isabstract(DOM::Comment)


def test_dom::comment_constructor_exists():
    assert callable(DOM::Comment.__init__)


def test_dom::comment_constructor_args():
    sig = inspect.signature(DOM::Comment.__init__)
    params = list(sig.parameters.keys())



def test_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_dom::catchclause_is_not_abstract():
    assert not inspect.isabstract(DOM::CatchClause)


def test_dom::catchclause_constructor_exists():
    assert callable(DOM::CatchClause.__init__)


def test_dom::catchclause_constructor_args():
    sig = inspect.signature(DOM::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_javadoc_is_not_abstract():
    assert not inspect.isabstract(Javadoc)


def test_javadoc_constructor_exists():
    assert callable(Javadoc.__init__)


def test_javadoc_constructor_args():
    sig = inspect.signature(Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_dom::modifier_is_not_abstract():
    assert not inspect.isabstract(DOM::Modifier)


def test_dom::modifier_constructor_exists():
    assert callable(DOM::Modifier.__init__)


def test_dom::modifier_constructor_args():
    sig = inspect.signature(DOM::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "private" in params, "Missing parameter 'private'"
    assert "native" in params, "Missing parameter 'native'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "static" in params, "Missing parameter 'static'"
    assert "public" in params, "Missing parameter 'public'"
    assert "none" in params, "Missing parameter 'none'"
    assert "final" in params, "Missing parameter 'final'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "volatile" in params, "Missing parameter 'volatile'"

def test_dom::modifier_has_private():
    assert hasattr(DOM::Modifier, "private")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
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

def test_dom::modifier_has_transient():
    assert hasattr(DOM::Modifier, "transient")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
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

def test_dom::modifier_has_synchronized():
    assert hasattr(DOM::Modifier, "synchronized")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
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

def test_dom::modifier_has_static():
    assert hasattr(DOM::Modifier, "static")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
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

def test_dom::modifier_has_none():
    assert hasattr(DOM::Modifier, "none")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
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

def test_dom::modifier_has_abstract():
    assert hasattr(DOM::Modifier, "abstract")
    descriptor = None
    for klass in DOM::Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
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



def test_dom::annotation_is_not_abstract():
    assert not inspect.isabstract(DOM::Annotation)


def test_dom::annotation_constructor_exists():
    assert callable(DOM::Annotation.__init__)


def test_dom::annotation_constructor_args():
    sig = inspect.signature(DOM::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_itypeparameter_is_not_abstract():
    assert not inspect.isabstract(ITypeParameter)


def test_itypeparameter_constructor_exists():
    assert callable(ITypeParameter.__init__)


def test_itypeparameter_constructor_args():
    sig = inspect.signature(ITypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(DOM::SingleMemberAnnotation)


def test_dom::singlememberannotation_constructor_exists():
    assert callable(DOM::SingleMemberAnnotation.__init__)


def test_dom::singlememberannotation_constructor_args():
    sig = inspect.signature(DOM::SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(MemberValuePair)


def test_membervaluepair_constructor_exists():
    assert callable(MemberValuePair.__init__)


def test_membervaluepair_constructor_args():
    sig = inspect.signature(MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_dom::normalannotation_is_not_abstract():
    assert not inspect.isabstract(DOM::NormalAnnotation)


def test_dom::normalannotation_constructor_exists():
    assert callable(DOM::NormalAnnotation.__init__)


def test_dom::normalannotation_constructor_args():
    sig = inspect.signature(DOM::NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(DOM::QualifiedType)


def test_dom::qualifiedtype_constructor_exists():
    assert callable(DOM::QualifiedType.__init__)


def test_dom::qualifiedtype_constructor_args():
    sig = inspect.signature(DOM::QualifiedType.__init__)
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



def test_dom::markerannotation_is_not_abstract():
    assert not inspect.isabstract(DOM::MarkerAnnotation)


def test_dom::markerannotation_constructor_exists():
    assert callable(DOM::MarkerAnnotation.__init__)


def test_dom::markerannotation_constructor_args():
    sig = inspect.signature(DOM::MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::simplename_is_not_abstract():
    assert not inspect.isabstract(DOM::SimpleName)


def test_dom::simplename_constructor_exists():
    assert callable(DOM::SimpleName.__init__)


def test_dom::simplename_constructor_args():
    sig = inspect.signature(DOM::SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_dom::simplename_has_declaration():
    assert hasattr(DOM::SimpleName, "declaration")
    descriptor = None
    for klass in DOM::SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_dom::simplename_has_identifier():
    assert hasattr(DOM::SimpleName, "identifier")
    descriptor = None
    for klass in DOM::SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_dom::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(DOM::QualifiedName)


def test_dom::qualifiedname_constructor_exists():
    assert callable(DOM::QualifiedName.__init__)


def test_dom::qualifiedname_constructor_args():
    sig = inspect.signature(DOM::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclarationFragment)


def test_dom::variabledeclarationfragment_constructor_exists():
    assert callable(DOM::VariableDeclarationFragment.__init__)


def test_dom::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(DOM::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



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



def test_dom::simpletype_is_not_abstract():
    assert not inspect.isabstract(DOM::SimpleType)


def test_dom::simpletype_constructor_exists():
    assert callable(DOM::SimpleType.__init__)


def test_dom::simpletype_constructor_args():
    sig = inspect.signature(DOM::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_dom::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::TypeDeclarationStatement)


def test_dom::typedeclarationstatement_constructor_exists():
    assert callable(DOM::TypeDeclarationStatement.__init__)


def test_dom::typedeclarationstatement_constructor_args():
    sig = inspect.signature(DOM::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_catchclause_is_not_abstract():
    assert not inspect.isabstract(CatchClause)


def test_catchclause_constructor_exists():
    assert callable(CatchClause.__init__)


def test_catchclause_constructor_args():
    sig = inspect.signature(CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_dom::trystatement_is_not_abstract():
    assert not inspect.isabstract(DOM::TryStatement)


def test_dom::trystatement_constructor_exists():
    assert callable(DOM::TryStatement.__init__)


def test_dom::trystatement_constructor_args():
    sig = inspect.signature(DOM::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(DOM::ParameterizedType)


def test_dom::parameterizedtype_constructor_exists():
    assert callable(DOM::ParameterizedType.__init__)


def test_dom::parameterizedtype_constructor_args():
    sig = inspect.signature(DOM::ParameterizedType.__init__)
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



def test_dom::whilestatement_is_not_abstract():
    assert not inspect.isabstract(DOM::WhileStatement)


def test_dom::whilestatement_constructor_exists():
    assert callable(DOM::WhileStatement.__init__)


def test_dom::whilestatement_constructor_args():
    sig = inspect.signature(DOM::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::VariableDeclarationStatement)


def test_dom::variabledeclarationstatement_constructor_exists():
    assert callable(DOM::VariableDeclarationStatement.__init__)


def test_dom::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(DOM::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM::SuperConstructorInvocation)


def test_dom::superconstructorinvocation_constructor_exists():
    assert callable(DOM::SuperConstructorInvocation.__init__)


def test_dom::superconstructorinvocation_constructor_args():
    sig = inspect.signature(DOM::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom::throwstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ThrowStatement)


def test_dom::throwstatement_constructor_exists():
    assert callable(DOM::ThrowStatement.__init__)


def test_dom::throwstatement_constructor_args():
    sig = inspect.signature(DOM::ThrowStatement.__init__)
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



def test_dom::forstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ForStatement)


def test_dom::forstatement_constructor_exists():
    assert callable(DOM::ForStatement.__init__)


def test_dom::forstatement_constructor_args():
    sig = inspect.signature(DOM::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::returnstatement_is_not_abstract():
    assert not inspect.isabstract(DOM::ReturnStatement)


def test_dom::returnstatement_constructor_exists():
    assert callable(DOM::ReturnStatement.__init__)


def test_dom::returnstatement_constructor_args():
    sig = inspect.signature(DOM::ReturnStatement.__init__)
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



def test_imethod_is_not_abstract():
    assert not inspect.isabstract(IMethod)


def test_imethod_constructor_exists():
    assert callable(IMethod.__init__)


def test_imethod_constructor_args():
    sig = inspect.signature(IMethod.__init__)
    params = list(sig.parameters.keys())



def test_ifield_is_not_abstract():
    assert not inspect.isabstract(IField)


def test_ifield_constructor_exists():
    assert callable(IField.__init__)


def test_ifield_constructor_args():
    sig = inspect.signature(IField.__init__)
    params = list(sig.parameters.keys())



def test_iinitializer_is_not_abstract():
    assert not inspect.isabstract(IInitializer)


def test_iinitializer_constructor_exists():
    assert callable(IInitializer.__init__)


def test_iinitializer_constructor_args():
    sig = inspect.signature(IInitializer.__init__)
    params = list(sig.parameters.keys())



def test_imember_is_not_abstract():
    assert not inspect.isabstract(IMember)


def test_imember_constructor_exists():
    assert callable(IMember.__init__)


def test_imember_constructor_args():
    sig = inspect.signature(IMember.__init__)
    params = list(sig.parameters.keys())



def test_core::iinitializer_is_not_abstract():
    assert not inspect.isabstract(Core::IInitializer)


def test_core::iinitializer_constructor_exists():
    assert callable(Core::IInitializer.__init__)


def test_core::iinitializer_constructor_args():
    sig = inspect.signature(Core::IInitializer.__init__)
    params = list(sig.parameters.keys())



def test_core::ifield_is_not_abstract():
    assert not inspect.isabstract(Core::IField)


def test_core::ifield_constructor_exists():
    assert callable(Core::IField.__init__)


def test_core::ifield_constructor_args():
    sig = inspect.signature(Core::IField.__init__)
    params = list(sig.parameters.keys())
    assert "isEnumConstant" in params, "Missing parameter 'isEnumConstant'"
    assert "constant" in params, "Missing parameter 'constant'"
    assert "isTransient" in params, "Missing parameter 'isTransient'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "typeSignature" in params, "Missing parameter 'typeSignature'"

def test_core::ifield_has_isEnumConstant():
    assert hasattr(Core::IField, "isEnumConstant")
    descriptor = None
    for klass in Core::IField.__mro__:
        if "isEnumConstant" in klass.__dict__:
            descriptor = klass.__dict__["isEnumConstant"]
            break
    assert isinstance(descriptor, property)

def test_core::ifield_has_constant():
    assert hasattr(Core::IField, "constant")
    descriptor = None
    for klass in Core::IField.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_core::ifield_has_isTransient():
    assert hasattr(Core::IField, "isTransient")
    descriptor = None
    for klass in Core::IField.__mro__:
        if "isTransient" in klass.__dict__:
            descriptor = klass.__dict__["isTransient"]
            break
    assert isinstance(descriptor, property)

def test_core::ifield_has_isVolatile():
    assert hasattr(Core::IField, "isVolatile")
    descriptor = None
    for klass in Core::IField.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_core::ifield_has_typeSignature():
    assert hasattr(Core::IField, "typeSignature")
    descriptor = None
    for klass in Core::IField.__mro__:
        if "typeSignature" in klass.__dict__:
            descriptor = klass.__dict__["typeSignature"]
            break
    assert isinstance(descriptor, property)



def test_core::itype_is_not_abstract():
    assert not inspect.isabstract(Core::IType)


def test_core::itype_constructor_exists():
    assert callable(Core::IType.__init__)


def test_core::itype_constructor_args():
    sig = inspect.signature(Core::IType.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"
    assert "fullyQualifiedParametrizedName" in params, "Missing parameter 'fullyQualifiedParametrizedName'"

def test_core::itype_has_fullyQualifiedName():
    assert hasattr(Core::IType, "fullyQualifiedName")
    descriptor = None
    for klass in Core::IType.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_core::itype_has_fullyQualifiedParametrizedName():
    assert hasattr(Core::IType, "fullyQualifiedParametrizedName")
    descriptor = None
    for klass in Core::IType.__mro__:
        if "fullyQualifiedParametrizedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedParametrizedName"]
            break
    assert isinstance(descriptor, property)



def test_core::parameter_is_not_abstract():
    assert not inspect.isabstract(Core::Parameter)


def test_core::parameter_constructor_exists():
    assert callable(Core::Parameter.__init__)


def test_core::parameter_constructor_args():
    sig = inspect.signature(Core::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_core::parameter_has_name():
    assert hasattr(Core::Parameter, "name")
    descriptor = None
    for klass in Core::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_core::parameter_has_type():
    assert hasattr(Core::Parameter, "type")
    descriptor = None
    for klass in Core::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_core::isourcerange_is_not_abstract():
    assert not inspect.isabstract(Core::ISourceRange)


def test_core::isourcerange_constructor_exists():
    assert callable(Core::ISourceRange.__init__)


def test_core::isourcerange_constructor_args():
    sig = inspect.signature(Core::ISourceRange.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_core::isourcerange_has_length():
    assert hasattr(Core::ISourceRange, "length")
    descriptor = None
    for klass in Core::ISourceRange.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_core::isourcerange_has_offset():
    assert hasattr(Core::ISourceRange, "offset")
    descriptor = None
    for klass in Core::ISourceRange.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_core::imethod_is_not_abstract():
    assert not inspect.isabstract(Core::IMethod)


def test_core::imethod_constructor_exists():
    assert callable(Core::IMethod.__init__)


def test_core::imethod_constructor_args():
    sig = inspect.signature(Core::IMethod.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "isConstructor" in params, "Missing parameter 'isConstructor'"
    assert "isMainMethod" in params, "Missing parameter 'isMainMethod'"
    assert "exceptionTypes" in params, "Missing parameter 'exceptionTypes'"

def test_core::imethod_has_returnType():
    assert hasattr(Core::IMethod, "returnType")
    descriptor = None
    for klass in Core::IMethod.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_core::imethod_has_isConstructor():
    assert hasattr(Core::IMethod, "isConstructor")
    descriptor = None
    for klass in Core::IMethod.__mro__:
        if "isConstructor" in klass.__dict__:
            descriptor = klass.__dict__["isConstructor"]
            break
    assert isinstance(descriptor, property)

def test_core::imethod_has_isMainMethod():
    assert hasattr(Core::IMethod, "isMainMethod")
    descriptor = None
    for klass in Core::IMethod.__mro__:
        if "isMainMethod" in klass.__dict__:
            descriptor = klass.__dict__["isMainMethod"]
            break
    assert isinstance(descriptor, property)

def test_core::imethod_has_exceptionTypes():
    assert hasattr(Core::IMethod, "exceptionTypes")
    descriptor = None
    for klass in Core::IMethod.__mro__:
        if "exceptionTypes" in klass.__dict__:
            descriptor = klass.__dict__["exceptionTypes"]
            break
    assert isinstance(descriptor, property)



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_iimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(IImportDeclaration)


def test_iimportdeclaration_constructor_exists():
    assert callable(IImportDeclaration.__init__)


def test_iimportdeclaration_constructor_args():
    sig = inspect.signature(IImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_itype_is_not_abstract():
    assert not inspect.isabstract(IType)


def test_itype_constructor_exists():
    assert callable(IType.__init__)


def test_itype_constructor_args():
    sig = inspect.signature(IType.__init__)
    params = list(sig.parameters.keys())



def test_ityperoot_is_not_abstract():
    assert not inspect.isabstract(ITypeRoot)


def test_ityperoot_constructor_exists():
    assert callable(ITypeRoot.__init__)


def test_ityperoot_constructor_args():
    sig = inspect.signature(ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_core::iclassfile_is_not_abstract():
    assert not inspect.isabstract(Core::IClassFile)


def test_core::iclassfile_constructor_exists():
    assert callable(Core::IClassFile.__init__)


def test_core::iclassfile_constructor_args():
    sig = inspect.signature(Core::IClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "isClass" in params, "Missing parameter 'isClass'"
    assert "isInterface" in params, "Missing parameter 'isInterface'"

def test_core::iclassfile_has_isClass():
    assert hasattr(Core::IClassFile, "isClass")
    descriptor = None
    for klass in Core::IClassFile.__mro__:
        if "isClass" in klass.__dict__:
            descriptor = klass.__dict__["isClass"]
            break
    assert isinstance(descriptor, property)

def test_core::iclassfile_has_isInterface():
    assert hasattr(Core::IClassFile, "isInterface")
    descriptor = None
    for klass in Core::IClassFile.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)



def test_core::icompilationunit_is_not_abstract():
    assert not inspect.isabstract(Core::ICompilationUnit)


def test_core::icompilationunit_constructor_exists():
    assert callable(Core::ICompilationUnit.__init__)


def test_core::icompilationunit_constructor_args():
    sig = inspect.signature(Core::ICompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_isourcereference_is_not_abstract():
    assert not inspect.isabstract(ISourceReference)


def test_isourcereference_constructor_exists():
    assert callable(ISourceReference.__init__)


def test_isourcereference_constructor_args():
    sig = inspect.signature(ISourceReference.__init__)
    params = list(sig.parameters.keys())



def test_icompilationunit_is_not_abstract():
    assert not inspect.isabstract(ICompilationUnit)


def test_icompilationunit_constructor_exists():
    assert callable(ICompilationUnit.__init__)


def test_icompilationunit_constructor_args():
    sig = inspect.signature(ICompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_iclassfile_is_not_abstract():
    assert not inspect.isabstract(IClassFile)


def test_iclassfile_constructor_exists():
    assert callable(IClassFile.__init__)


def test_iclassfile_constructor_args():
    sig = inspect.signature(IClassFile.__init__)
    params = list(sig.parameters.keys())



def test_ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(IPackageFragment)


def test_ipackagefragment_constructor_exists():
    assert callable(IPackageFragment.__init__)


def test_ipackagefragment_constructor_args():
    sig = inspect.signature(IPackageFragment.__init__)
    params = list(sig.parameters.keys())



def test_isourcerange_is_not_abstract():
    assert not inspect.isabstract(ISourceRange)


def test_isourcerange_constructor_exists():
    assert callable(ISourceRange.__init__)


def test_isourcerange_constructor_args():
    sig = inspect.signature(ISourceRange.__init__)
    params = list(sig.parameters.keys())



def test_core::isourcereference_is_not_abstract():
    assert not inspect.isabstract(Core::ISourceReference)


def test_core::isourcereference_constructor_exists():
    assert callable(Core::ISourceReference.__init__)


def test_core::isourcereference_constructor_args():
    sig = inspect.signature(Core::ISourceReference.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_core::isourcereference_has_source():
    assert hasattr(Core::ISourceReference, "source")
    descriptor = None
    for klass in Core::ISourceReference.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_physicalelement_is_not_abstract():
    assert not inspect.isabstract(PhysicalElement)


def test_physicalelement_constructor_exists():
    assert callable(PhysicalElement.__init__)


def test_physicalelement_constructor_args():
    sig = inspect.signature(PhysicalElement.__init__)
    params = list(sig.parameters.keys())



def test_core::ijavamodel_is_not_abstract():
    assert not inspect.isabstract(Core::IJavaModel)


def test_core::ijavamodel_constructor_exists():
    assert callable(Core::IJavaModel.__init__)


def test_core::ijavamodel_constructor_args():
    sig = inspect.signature(Core::IJavaModel.__init__)
    params = list(sig.parameters.keys())



def test_core::physicalelement_is_not_abstract():
    assert not inspect.isabstract(Core::PhysicalElement)


def test_core::physicalelement_constructor_exists():
    assert callable(Core::PhysicalElement.__init__)


def test_core::physicalelement_constructor_args():
    sig = inspect.signature(Core::PhysicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_core::physicalelement_has_path():
    assert hasattr(Core::PhysicalElement, "path")
    descriptor = None
    for klass in Core::PhysicalElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_core::physicalelement_has_isReadOnly():
    assert hasattr(Core::PhysicalElement, "isReadOnly")
    descriptor = None
    for klass in Core::PhysicalElement.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_core::ijavaelement_is_not_abstract():
    assert not inspect.isabstract(Core::IJavaElement)


def test_core::ijavaelement_constructor_exists():
    assert callable(Core::IJavaElement.__init__)


def test_core::ijavaelement_constructor_args():
    sig = inspect.signature(Core::IJavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"

def test_core::ijavaelement_has_elementName():
    assert hasattr(Core::IJavaElement, "elementName")
    descriptor = None
    for klass in Core::IJavaElement.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)



def test_ijavaelement_is_not_abstract():
    assert not inspect.isabstract(IJavaElement)


def test_ijavaelement_constructor_exists():
    assert callable(IJavaElement.__init__)


def test_ijavaelement_constructor_args():
    sig = inspect.signature(IJavaElement.__init__)
    params = list(sig.parameters.keys())



def test_core::iimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(Core::IImportDeclaration)


def test_core::iimportdeclaration_constructor_exists():
    assert callable(Core::IImportDeclaration.__init__)


def test_core::iimportdeclaration_constructor_args():
    sig = inspect.signature(Core::IImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isOnDemand" in params, "Missing parameter 'isOnDemand'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_core::iimportdeclaration_has_isOnDemand():
    assert hasattr(Core::IImportDeclaration, "isOnDemand")
    descriptor = None
    for klass in Core::IImportDeclaration.__mro__:
        if "isOnDemand" in klass.__dict__:
            descriptor = klass.__dict__["isOnDemand"]
            break
    assert isinstance(descriptor, property)

def test_core::iimportdeclaration_has_isStatic():
    assert hasattr(Core::IImportDeclaration, "isStatic")
    descriptor = None
    for klass in Core::IImportDeclaration.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_core::ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(Core::IPackageFragmentRoot)


def test_core::ipackagefragmentroot_constructor_exists():
    assert callable(Core::IPackageFragmentRoot.__init__)


def test_core::ipackagefragmentroot_constructor_args():
    sig = inspect.signature(Core::IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_core::imember_is_not_abstract():
    assert not inspect.isabstract(Core::IMember)


def test_core::imember_constructor_exists():
    assert callable(Core::IMember.__init__)


def test_core::imember_constructor_args():
    sig = inspect.signature(Core::IMember.__init__)
    params = list(sig.parameters.keys())



def test_core::ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(Core::IPackageFragment)


def test_core::ipackagefragment_constructor_exists():
    assert callable(Core::IPackageFragment.__init__)


def test_core::ipackagefragment_constructor_args():
    sig = inspect.signature(Core::IPackageFragment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefaultPackage" in params, "Missing parameter 'isDefaultPackage'"

def test_core::ipackagefragment_has_isDefaultPackage():
    assert hasattr(Core::IPackageFragment, "isDefaultPackage")
    descriptor = None
    for klass in Core::IPackageFragment.__mro__:
        if "isDefaultPackage" in klass.__dict__:
            descriptor = klass.__dict__["isDefaultPackage"]
            break
    assert isinstance(descriptor, property)



def test_core::ityperoot_is_not_abstract():
    assert not inspect.isabstract(Core::ITypeRoot)


def test_core::ityperoot_constructor_exists():
    assert callable(Core::ITypeRoot.__init__)


def test_core::ityperoot_constructor_args():
    sig = inspect.signature(Core::ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_core::itypeparameter_is_not_abstract():
    assert not inspect.isabstract(Core::ITypeParameter)


def test_core::itypeparameter_constructor_exists():
    assert callable(Core::ITypeParameter.__init__)


def test_core::itypeparameter_constructor_args():
    sig = inspect.signature(Core::ITypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "bounds" in params, "Missing parameter 'bounds'"

def test_core::itypeparameter_has_bounds():
    assert hasattr(Core::ITypeParameter, "bounds")
    descriptor = None
    for klass in Core::ITypeParameter.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)



def test_core::ijavaproject_is_not_abstract():
    assert not inspect.isabstract(Core::IJavaProject)


def test_core::ijavaproject_constructor_exists():
    assert callable(Core::IJavaProject.__init__)


def test_core::ijavaproject_constructor_args():
    sig = inspect.signature(Core::IJavaProject.__init__)
    params = list(sig.parameters.keys())



def test_ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(IPackageFragmentRoot)


def test_ipackagefragmentroot_constructor_exists():
    assert callable(IPackageFragmentRoot.__init__)


def test_ipackagefragmentroot_constructor_args():
    sig = inspect.signature(IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_core::binarypackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(Core::BinaryPackageFragmentRoot)


def test_core::binarypackagefragmentroot_constructor_exists():
    assert callable(Core::BinaryPackageFragmentRoot.__init__)


def test_core::binarypackagefragmentroot_constructor_args():
    sig = inspect.signature(Core::BinaryPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_core::sourcepackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(Core::SourcePackageFragmentRoot)


def test_core::sourcepackagefragmentroot_constructor_exists():
    assert callable(Core::SourcePackageFragmentRoot.__init__)


def test_core::sourcepackagefragmentroot_constructor_args():
    sig = inspect.signature(Core::SourcePackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_ijavaproject_is_not_abstract():
    assert not inspect.isabstract(IJavaProject)


def test_ijavaproject_constructor_exists():
    assert callable(IJavaProject.__init__)


def test_ijavaproject_constructor_args():
    sig = inspect.signature(IJavaProject.__init__)
    params = list(sig.parameters.keys())

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "minus",
        "right_shift_unsigned",
        "xor",
        "divide",
        "equals",
        "conditional_and",
        "left_shift",
        "or_",
        "plus",
        "times",
        "conditional_or",
        "greater",
        "greater_equals",
        "remainder",
        "right_shift_signed",
        "less",
        "less_equals",
        "not_equals",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

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

def test_assignmentoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorKind is not None

def test_assignmentoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorKind]
    expected_literals = [
        "bit_xor_assign",
        "remainder_assign",
        "plus_assign",
        "right_shift_unsigned_assign",
        "bit_or_assign",
        "bit_and_assign",
        "times_assign",
        "left_shift_assign",
        "minus_assign",
        "assign",
        "right_shift_signed_assign",
        "divide_assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"

def test_modifiers_exists():
    # Check that the Enumeration exists
    assert Modifiers is not None

def test_modifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Modifiers]
    expected_literals = [
        "final",
        "native",
        "deprecated",
        "transient",
        "static",
        "default",
        "volatile",
        "super",
        "varargs",
        "synchronized",
        "annotation",
        "protected",
        "bridge",
        "abstract",
        "interface",
        "strictfp",
        "private",
        "synthetic",
        "public",
        "enum",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Modifiers"

def test_prefixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionOperatorKind is not None

def test_prefixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionOperatorKind]
    expected_literals = [
        "plus",
        "minus",
        "complement",
        "increment",
        "decrement",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionOperatorKind"


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
Statement_strategy = st.builds(
    Statement,
)
DOM::ConstructorInvocation_strategy = st.builds(
    DOM::ConstructorInvocation,
)
DOM::ExpressionStatement_strategy = st.builds(
    DOM::ExpressionStatement,
)
DOM::Block_strategy = st.builds(
    DOM::Block,
)
DOM::EmptyStatement_strategy = st.builds(
    DOM::EmptyStatement,
)
DOM::BreakStatement_strategy = st.builds(
    DOM::BreakStatement,
)
DOM::EnhancedForStatement_strategy = st.builds(
    DOM::EnhancedForStatement,
)
DOM::DoStatement_strategy = st.builds(
    DOM::DoStatement,
)
DOM::ContinueStatement_strategy = st.builds(
    DOM::ContinueStatement,
)
DOM::AssertStatement_strategy = st.builds(
    DOM::AssertStatement,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
EnumConstantDeclaration_strategy = st.builds(
    EnumConstantDeclaration,
)
TypeParameter_strategy = st.builds(
    TypeParameter,
)
TagElement_strategy = st.builds(
    TagElement,
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
AnonymousClassDeclaration_strategy = st.builds(
    AnonymousClassDeclaration,
)
Annotation_strategy = st.builds(
    Annotation,
)
SimpleName_strategy = st.builds(
    SimpleName,
)
Name_strategy = st.builds(
    Name,
)
DOM::ExtendedModifier_strategy = st.builds(
    DOM::ExtendedModifier,
)
Type_strategy = st.builds(
    Type,
)
MethodRefParameter_strategy = st.builds(
    MethodRefParameter,
)
Expression_strategy = st.builds(
    Expression,
)
DOM::SuperMethodInvocation_strategy = st.builds(
    DOM::SuperMethodInvocation,
)
DOM::ConditionalExpression_strategy = st.builds(
    DOM::ConditionalExpression,
)
DOM::BooleanLiteral_strategy = st.builds(
    DOM::BooleanLiteral,
    booleanValue=
        safe_text
)
DOM::VariableDeclarationExpression_strategy = st.builds(
    DOM::VariableDeclarationExpression,
)
DOM::ArrayInitializer_strategy = st.builds(
    DOM::ArrayInitializer,
)
DOM::TypeLiteral_strategy = st.builds(
    DOM::TypeLiteral,
)
DOM::NullLiteral_strategy = st.builds(
    DOM::NullLiteral,
)
DOM::CharacterLiteral_strategy = st.builds(
    DOM::CharacterLiteral,
    charValue=
        safe_text,
    escapedValue=
        safe_text
)
DOM::ClassInstanceCreation_strategy = st.builds(
    DOM::ClassInstanceCreation,
)
DOM::FieldAccess_strategy = st.builds(
    DOM::FieldAccess,
)
DOM::Name_strategy = st.builds(
    DOM::Name,
    fullyQualifiedName=
        safe_text
)
DOM::SuperFieldAccess_strategy = st.builds(
    DOM::SuperFieldAccess,
)
DOM::ThisExpression_strategy = st.builds(
    DOM::ThisExpression,
)
DOM::InstanceofExpression_strategy = st.builds(
    DOM::InstanceofExpression,
)
DOM::ParenthesizedExpression_strategy = st.builds(
    DOM::ParenthesizedExpression,
)
DOM::Assignment_strategy = st.builds(
    DOM::Assignment,
    operator=
        safe_text
)
DOM::StringLiteral_strategy = st.builds(
    DOM::StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
DOM::InfixExpression_strategy = st.builds(
    DOM::InfixExpression,
    operator=
        safe_text
)
DOM::PrefixExpression_strategy = st.builds(
    DOM::PrefixExpression,
    operator=
        safe_text
)
DOM::ArrayAccess_strategy = st.builds(
    DOM::ArrayAccess,
)
DOM::ArrayCreation_strategy = st.builds(
    DOM::ArrayCreation,
)
DOM::CastExpression_strategy = st.builds(
    DOM::CastExpression,
)
DOM::NumberLiteral_strategy = st.builds(
    DOM::NumberLiteral,
    token=
        safe_text
)
DOM::PostfixExpression_strategy = st.builds(
    DOM::PostfixExpression,
    operator=
        safe_text
)
DOM::MethodInvocation_strategy = st.builds(
    DOM::MethodInvocation,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
DOM::Initializer_strategy = st.builds(
    DOM::Initializer,
)
DOM::MethodDeclaration_strategy = st.builds(
    DOM::MethodDeclaration,
    extraDimensions=
        safe_text,
    varargs=
        safe_text,
    constructor=
        safe_text
)
DOM::AnnotationTypeMemberDeclaration_strategy = st.builds(
    DOM::AnnotationTypeMemberDeclaration,
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
DOM::EnumConstantDeclaration_strategy = st.builds(
    DOM::EnumConstantDeclaration,
)
DOM::FieldDeclaration_strategy = st.builds(
    DOM::FieldDeclaration,
)
DOM::ASTNode_strategy = st.builds(
    DOM::ASTNode,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
DOM::PackageDeclaration_strategy = st.builds(
    DOM::PackageDeclaration,
)
DOM::Statement_strategy = st.builds(
    DOM::Statement,
)
DOM::VariableDeclaration_strategy = st.builds(
    DOM::VariableDeclaration,
    extraDimensions=
        safe_text
)
DOM::MethodRefParameter_strategy = st.builds(
    DOM::MethodRefParameter,
    varargs=
        safe_text
)
DOM::TextElement_strategy = st.builds(
    DOM::TextElement,
    text=
        safe_text
)
DOM::ImportDeclaration_strategy = st.builds(
    DOM::ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
DOM::TagElement_strategy = st.builds(
    DOM::TagElement,
    nested=
        safe_text,
    tagName=
        safe_text
)
DOM::MemberValuePair_strategy = st.builds(
    DOM::MemberValuePair,
)
DOM::MemberRef_strategy = st.builds(
    DOM::MemberRef,
)
DOM::AnonymousClassDeclaration_strategy = st.builds(
    DOM::AnonymousClassDeclaration,
)
DOM::TypeParameter_strategy = st.builds(
    DOM::TypeParameter,
)
DOM::Type_strategy = st.builds(
    DOM::Type,
)
DOM::MethodRef_strategy = st.builds(
    DOM::MethodRef,
)
DOM::BodyDeclaration_strategy = st.builds(
    DOM::BodyDeclaration,
)
DOM::AST_strategy = st.builds(
    DOM::AST,
)
DOM::Expression_strategy = st.builds(
    DOM::Expression,
    resolveBoxing=
        safe_text,
    resolveUnboxing=
        safe_text
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
DOM::TypeDeclaration_strategy = st.builds(
    DOM::TypeDeclaration,
    interface=
        safe_text
)
DOM::EnumDeclaration_strategy = st.builds(
    DOM::EnumDeclaration,
)
DOM::AnnotationTypeDeclaration_strategy = st.builds(
    DOM::AnnotationTypeDeclaration,
)
ImportDeclaration_strategy = st.builds(
    ImportDeclaration,
)
PackageDeclaration_strategy = st.builds(
    PackageDeclaration,
)
Comment_strategy = st.builds(
    Comment,
)
DOM::Javadoc_strategy = st.builds(
    DOM::Javadoc,
)
DOM::LineComment_strategy = st.builds(
    DOM::LineComment,
)
DOM::BlockComment_strategy = st.builds(
    DOM::BlockComment,
)
DOM::CompilationUnit_strategy = st.builds(
    DOM::CompilationUnit,
)
DOM::Comment_strategy = st.builds(
    DOM::Comment,
)
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
)
Block_strategy = st.builds(
    Block,
)
DOM::CatchClause_strategy = st.builds(
    DOM::CatchClause,
)
Javadoc_strategy = st.builds(
    Javadoc,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
DOM::Modifier_strategy = st.builds(
    DOM::Modifier,
    private=
        safe_text,
    native=
        safe_text,
    transient=
        safe_text,
    strictfp=
        safe_text,
    synchronized=
        safe_text,
    protected=
        safe_text,
    static=
        safe_text,
    public=
        safe_text,
    none=
        safe_text,
    final=
        safe_text,
    abstract=
        safe_text,
    volatile=
        safe_text
)
DOM::Annotation_strategy = st.builds(
    DOM::Annotation,
)
ITypeParameter_strategy = st.builds(
    ITypeParameter,
)
DOM::SingleMemberAnnotation_strategy = st.builds(
    DOM::SingleMemberAnnotation,
)
MemberValuePair_strategy = st.builds(
    MemberValuePair,
)
DOM::NormalAnnotation_strategy = st.builds(
    DOM::NormalAnnotation,
)
DOM::QualifiedType_strategy = st.builds(
    DOM::QualifiedType,
)
DOM::PrimitiveType_strategy = st.builds(
    DOM::PrimitiveType,
    code=
        safe_text
)
DOM::MarkerAnnotation_strategy = st.builds(
    DOM::MarkerAnnotation,
)
DOM::SimpleName_strategy = st.builds(
    DOM::SimpleName,
    declaration=
        safe_text,
    identifier=
        safe_text
)
DOM::QualifiedName_strategy = st.builds(
    DOM::QualifiedName,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
DOM::VariableDeclarationFragment_strategy = st.builds(
    DOM::VariableDeclarationFragment,
)
DOM::SingleVariableDeclaration_strategy = st.builds(
    DOM::SingleVariableDeclaration,
    varargs=
        safe_text
)
DOM::WildcardType_strategy = st.builds(
    DOM::WildcardType,
    upperBound=
        safe_text
)
DOM::SimpleType_strategy = st.builds(
    DOM::SimpleType,
)
DOM::TypeDeclarationStatement_strategy = st.builds(
    DOM::TypeDeclarationStatement,
)
CatchClause_strategy = st.builds(
    CatchClause,
)
DOM::TryStatement_strategy = st.builds(
    DOM::TryStatement,
)
DOM::ParameterizedType_strategy = st.builds(
    DOM::ParameterizedType,
)
DOM::ArrayType_strategy = st.builds(
    DOM::ArrayType,
    dimensions=
        safe_text
)
DOM::WhileStatement_strategy = st.builds(
    DOM::WhileStatement,
)
DOM::VariableDeclarationStatement_strategy = st.builds(
    DOM::VariableDeclarationStatement,
)
DOM::SuperConstructorInvocation_strategy = st.builds(
    DOM::SuperConstructorInvocation,
)
DOM::ThrowStatement_strategy = st.builds(
    DOM::ThrowStatement,
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
DOM::ForStatement_strategy = st.builds(
    DOM::ForStatement,
)
DOM::ReturnStatement_strategy = st.builds(
    DOM::ReturnStatement,
)
DOM::LabeledStatement_strategy = st.builds(
    DOM::LabeledStatement,
)
DOM::IfStatement_strategy = st.builds(
    DOM::IfStatement,
)
IMethod_strategy = st.builds(
    IMethod,
)
IField_strategy = st.builds(
    IField,
)
IInitializer_strategy = st.builds(
    IInitializer,
)
IMember_strategy = st.builds(
    IMember,
)
Core::IInitializer_strategy = st.builds(
    Core::IInitializer,
)
Core::IField_strategy = st.builds(
    Core::IField,
    isEnumConstant=
        safe_text,
    constant=
        safe_text,
    isTransient=
        safe_text,
    isVolatile=
        safe_text,
    typeSignature=
        safe_text
)
Core::IType_strategy = st.builds(
    Core::IType,
    fullyQualifiedName=
        safe_text,
    fullyQualifiedParametrizedName=
        safe_text
)
Core::Parameter_strategy = st.builds(
    Core::Parameter,
    name=
        safe_text,
    type=
        safe_text
)
Core::ISourceRange_strategy = st.builds(
    Core::ISourceRange,
    length=
        safe_text,
    offset=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Core::IMethod_strategy = st.builds(
    Core::IMethod,
    returnType=
        safe_text,
    isConstructor=
        safe_text,
    isMainMethod=
        safe_text,
    exceptionTypes=
        safe_text
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
IImportDeclaration_strategy = st.builds(
    IImportDeclaration,
)
IType_strategy = st.builds(
    IType,
)
ITypeRoot_strategy = st.builds(
    ITypeRoot,
)
Core::IClassFile_strategy = st.builds(
    Core::IClassFile,
    isClass=
        safe_text,
    isInterface=
        safe_text
)
Core::ICompilationUnit_strategy = st.builds(
    Core::ICompilationUnit,
)
ISourceReference_strategy = st.builds(
    ISourceReference,
)
ICompilationUnit_strategy = st.builds(
    ICompilationUnit,
)
IClassFile_strategy = st.builds(
    IClassFile,
)
IPackageFragment_strategy = st.builds(
    IPackageFragment,
)
ISourceRange_strategy = st.builds(
    ISourceRange,
)
Core::ISourceReference_strategy = st.builds(
    Core::ISourceReference,
    source=
        safe_text
)
PhysicalElement_strategy = st.builds(
    PhysicalElement,
)
Core::IJavaModel_strategy = st.builds(
    Core::IJavaModel,
)
Core::PhysicalElement_strategy = st.builds(
    Core::PhysicalElement,
    path=
        safe_text,
    isReadOnly=
        safe_text
)
Core::IJavaElement_strategy = st.builds(
    Core::IJavaElement,
    elementName=
        safe_text
)
IJavaElement_strategy = st.builds(
    IJavaElement,
)
Core::IImportDeclaration_strategy = st.builds(
    Core::IImportDeclaration,
    isOnDemand=
        safe_text,
    isStatic=
        safe_text
)
Core::IPackageFragmentRoot_strategy = st.builds(
    Core::IPackageFragmentRoot,
)
Core::IMember_strategy = st.builds(
    Core::IMember,
)
Core::IPackageFragment_strategy = st.builds(
    Core::IPackageFragment,
    isDefaultPackage=
        safe_text
)
Core::ITypeRoot_strategy = st.builds(
    Core::ITypeRoot,
)
Core::ITypeParameter_strategy = st.builds(
    Core::ITypeParameter,
    bounds=
        safe_text
)
Core::IJavaProject_strategy = st.builds(
    Core::IJavaProject,
)
IPackageFragmentRoot_strategy = st.builds(
    IPackageFragmentRoot,
)
Core::BinaryPackageFragmentRoot_strategy = st.builds(
    Core::BinaryPackageFragmentRoot,
)
Core::SourcePackageFragmentRoot_strategy = st.builds(
    Core::SourcePackageFragmentRoot,
)
IJavaProject_strategy = st.builds(
    IJavaProject,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DOM::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dom::constructorinvocation_instantiation(instance):
    assert isinstance(instance, DOM::ConstructorInvocation)

@given(instance=DOM::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom::expressionstatement_instantiation(instance):
    assert isinstance(instance, DOM::ExpressionStatement)

@given(instance=DOM::Block_strategy)
@settings(max_examples=50)
def test_dom::block_instantiation(instance):
    assert isinstance(instance, DOM::Block)

@given(instance=DOM::EmptyStatement_strategy)
@settings(max_examples=50)
def test_dom::emptystatement_instantiation(instance):
    assert isinstance(instance, DOM::EmptyStatement)

@given(instance=DOM::BreakStatement_strategy)
@settings(max_examples=50)
def test_dom::breakstatement_instantiation(instance):
    assert isinstance(instance, DOM::BreakStatement)

@given(instance=DOM::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_dom::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, DOM::EnhancedForStatement)

@given(instance=DOM::DoStatement_strategy)
@settings(max_examples=50)
def test_dom::dostatement_instantiation(instance):
    assert isinstance(instance, DOM::DoStatement)

@given(instance=DOM::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dom::continuestatement_instantiation(instance):
    assert isinstance(instance, DOM::ContinueStatement)

@given(instance=DOM::AssertStatement_strategy)
@settings(max_examples=50)
def test_dom::assertstatement_instantiation(instance):
    assert isinstance(instance, DOM::AssertStatement)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, EnumConstantDeclaration)

@given(instance=TypeParameter_strategy)
@settings(max_examples=50)
def test_typeparameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)

@given(instance=TagElement_strategy)
@settings(max_examples=50)
def test_tagelement_instantiation(instance):
    assert isinstance(instance, TagElement)

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

@given(instance=AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, AnonymousClassDeclaration)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=SimpleName_strategy)
@settings(max_examples=50)
def test_simplename_instantiation(instance):
    assert isinstance(instance, SimpleName)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DOM::ExtendedModifier_strategy)
@settings(max_examples=50)
def test_dom::extendedmodifier_instantiation(instance):
    assert isinstance(instance, DOM::ExtendedModifier)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=MethodRefParameter_strategy)
@settings(max_examples=50)
def test_methodrefparameter_instantiation(instance):
    assert isinstance(instance, MethodRefParameter)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=DOM::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_dom::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, DOM::SuperMethodInvocation)

@given(instance=DOM::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_dom::conditionalexpression_instantiation(instance):
    assert isinstance(instance, DOM::ConditionalExpression)

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

@given(instance=DOM::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclarationExpression)

@given(instance=DOM::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_dom::arrayinitializer_instantiation(instance):
    assert isinstance(instance, DOM::ArrayInitializer)

@given(instance=DOM::TypeLiteral_strategy)
@settings(max_examples=50)
def test_dom::typeliteral_instantiation(instance):
    assert isinstance(instance, DOM::TypeLiteral)

@given(instance=DOM::NullLiteral_strategy)
@settings(max_examples=50)
def test_dom::nullliteral_instantiation(instance):
    assert isinstance(instance, DOM::NullLiteral)

@given(instance=DOM::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_dom::characterliteral_instantiation(instance):
    assert isinstance(instance, DOM::CharacterLiteral)

@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_charValue_type(instance):
    assert isinstance(instance.charValue, str)


@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=DOM::CharacterLiteral_strategy)
def test_dom::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=DOM::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_dom::classinstancecreation_instantiation(instance):
    assert isinstance(instance, DOM::ClassInstanceCreation)

@given(instance=DOM::FieldAccess_strategy)
@settings(max_examples=50)
def test_dom::fieldaccess_instantiation(instance):
    assert isinstance(instance, DOM::FieldAccess)

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

@given(instance=DOM::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_dom::superfieldaccess_instantiation(instance):
    assert isinstance(instance, DOM::SuperFieldAccess)

@given(instance=DOM::ThisExpression_strategy)
@settings(max_examples=50)
def test_dom::thisexpression_instantiation(instance):
    assert isinstance(instance, DOM::ThisExpression)

@given(instance=DOM::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_dom::instanceofexpression_instantiation(instance):
    assert isinstance(instance, DOM::InstanceofExpression)

@given(instance=DOM::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_dom::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, DOM::ParenthesizedExpression)

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

@given(instance=DOM::ArrayAccess_strategy)
@settings(max_examples=50)
def test_dom::arrayaccess_instantiation(instance):
    assert isinstance(instance, DOM::ArrayAccess)

@given(instance=DOM::ArrayCreation_strategy)
@settings(max_examples=50)
def test_dom::arraycreation_instantiation(instance):
    assert isinstance(instance, DOM::ArrayCreation)

@given(instance=DOM::CastExpression_strategy)
@settings(max_examples=50)
def test_dom::castexpression_instantiation(instance):
    assert isinstance(instance, DOM::CastExpression)

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

@given(instance=DOM::MethodInvocation_strategy)
@settings(max_examples=50)
def test_dom::methodinvocation_instantiation(instance):
    assert isinstance(instance, DOM::MethodInvocation)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=DOM::Initializer_strategy)
@settings(max_examples=50)
def test_dom::initializer_instantiation(instance):
    assert isinstance(instance, DOM::Initializer)

@given(instance=DOM::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_dom::methoddeclaration_instantiation(instance):
    assert isinstance(instance, DOM::MethodDeclaration)

@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_extraDimensions_type(instance):
    assert isinstance(instance.extraDimensions, str)


@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, str)


@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_constructor_type(instance):
    assert isinstance(instance.constructor, str)


@given(instance=DOM::MethodDeclaration_strategy)
def test_dom::methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=DOM::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_dom::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AnnotationTypeMemberDeclaration)

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

@given(instance=DOM::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_dom::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::EnumConstantDeclaration)

@given(instance=DOM::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_dom::fielddeclaration_instantiation(instance):
    assert isinstance(instance, DOM::FieldDeclaration)

@given(instance=DOM::ASTNode_strategy)
@settings(max_examples=50)
def test_dom::astnode_instantiation(instance):
    assert isinstance(instance, DOM::ASTNode)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=DOM::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_dom::packagedeclaration_instantiation(instance):
    assert isinstance(instance, DOM::PackageDeclaration)

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

@given(instance=DOM::TagElement_strategy)
@settings(max_examples=50)
def test_dom::tagelement_instantiation(instance):
    assert isinstance(instance, DOM::TagElement)

@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_nested_type(instance):
    assert isinstance(instance.nested, str)


@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original

@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=DOM::TagElement_strategy)
def test_dom::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=DOM::MemberValuePair_strategy)
@settings(max_examples=50)
def test_dom::membervaluepair_instantiation(instance):
    assert isinstance(instance, DOM::MemberValuePair)

@given(instance=DOM::MemberRef_strategy)
@settings(max_examples=50)
def test_dom::memberref_instantiation(instance):
    assert isinstance(instance, DOM::MemberRef)

@given(instance=DOM::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_dom::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AnonymousClassDeclaration)

@given(instance=DOM::TypeParameter_strategy)
@settings(max_examples=50)
def test_dom::typeparameter_instantiation(instance):
    assert isinstance(instance, DOM::TypeParameter)

@given(instance=DOM::Type_strategy)
@settings(max_examples=50)
def test_dom::type_instantiation(instance):
    assert isinstance(instance, DOM::Type)

@given(instance=DOM::MethodRef_strategy)
@settings(max_examples=50)
def test_dom::methodref_instantiation(instance):
    assert isinstance(instance, DOM::MethodRef)

@given(instance=DOM::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_dom::bodydeclaration_instantiation(instance):
    assert isinstance(instance, DOM::BodyDeclaration)

@given(instance=DOM::AST_strategy)
@settings(max_examples=50)
def test_dom::ast_instantiation(instance):
    assert isinstance(instance, DOM::AST)

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

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

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

@given(instance=DOM::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, DOM::AnnotationTypeDeclaration)

@given(instance=ImportDeclaration_strategy)
@settings(max_examples=50)
def test_importdeclaration_instantiation(instance):
    assert isinstance(instance, ImportDeclaration)

@given(instance=PackageDeclaration_strategy)
@settings(max_examples=50)
def test_packagedeclaration_instantiation(instance):
    assert isinstance(instance, PackageDeclaration)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=DOM::Javadoc_strategy)
@settings(max_examples=50)
def test_dom::javadoc_instantiation(instance):
    assert isinstance(instance, DOM::Javadoc)

@given(instance=DOM::LineComment_strategy)
@settings(max_examples=50)
def test_dom::linecomment_instantiation(instance):
    assert isinstance(instance, DOM::LineComment)

@given(instance=DOM::BlockComment_strategy)
@settings(max_examples=50)
def test_dom::blockcomment_instantiation(instance):
    assert isinstance(instance, DOM::BlockComment)

@given(instance=DOM::CompilationUnit_strategy)
@settings(max_examples=50)
def test_dom::compilationunit_instantiation(instance):
    assert isinstance(instance, DOM::CompilationUnit)

@given(instance=DOM::Comment_strategy)
@settings(max_examples=50)
def test_dom::comment_instantiation(instance):
    assert isinstance(instance, DOM::Comment)

@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=DOM::CatchClause_strategy)
@settings(max_examples=50)
def test_dom::catchclause_instantiation(instance):
    assert isinstance(instance, DOM::CatchClause)

@given(instance=Javadoc_strategy)
@settings(max_examples=50)
def test_javadoc_instantiation(instance):
    assert isinstance(instance, Javadoc)

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=DOM::Modifier_strategy)
@settings(max_examples=50)
def test_dom::modifier_instantiation(instance):
    assert isinstance(instance, DOM::Modifier)

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_private_type(instance):
    assert isinstance(instance.private, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_native_type(instance):
    assert isinstance(instance.native, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_transient_type(instance):
    assert isinstance(instance.transient, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_public_type(instance):
    assert isinstance(instance.public, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_none_type(instance):
    assert isinstance(instance.none, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_final_type(instance):
    assert isinstance(instance.final, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, str)


@given(instance=DOM::Modifier_strategy)
def test_dom::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=DOM::Annotation_strategy)
@settings(max_examples=50)
def test_dom::annotation_instantiation(instance):
    assert isinstance(instance, DOM::Annotation)

@given(instance=ITypeParameter_strategy)
@settings(max_examples=50)
def test_itypeparameter_instantiation(instance):
    assert isinstance(instance, ITypeParameter)

@given(instance=DOM::SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_dom::singlememberannotation_instantiation(instance):
    assert isinstance(instance, DOM::SingleMemberAnnotation)

@given(instance=MemberValuePair_strategy)
@settings(max_examples=50)
def test_membervaluepair_instantiation(instance):
    assert isinstance(instance, MemberValuePair)

@given(instance=DOM::NormalAnnotation_strategy)
@settings(max_examples=50)
def test_dom::normalannotation_instantiation(instance):
    assert isinstance(instance, DOM::NormalAnnotation)

@given(instance=DOM::QualifiedType_strategy)
@settings(max_examples=50)
def test_dom::qualifiedtype_instantiation(instance):
    assert isinstance(instance, DOM::QualifiedType)

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

@given(instance=DOM::MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_dom::markerannotation_instantiation(instance):
    assert isinstance(instance, DOM::MarkerAnnotation)

@given(instance=DOM::SimpleName_strategy)
@settings(max_examples=50)
def test_dom::simplename_instantiation(instance):
    assert isinstance(instance, DOM::SimpleName)

@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=DOM::SimpleName_strategy)
def test_dom::simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=DOM::QualifiedName_strategy)
@settings(max_examples=50)
def test_dom::qualifiedname_instantiation(instance):
    assert isinstance(instance, DOM::QualifiedName)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=DOM::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclarationFragment)

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

@given(instance=DOM::SimpleType_strategy)
@settings(max_examples=50)
def test_dom::simpletype_instantiation(instance):
    assert isinstance(instance, DOM::SimpleType)

@given(instance=DOM::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, DOM::TypeDeclarationStatement)

@given(instance=CatchClause_strategy)
@settings(max_examples=50)
def test_catchclause_instantiation(instance):
    assert isinstance(instance, CatchClause)

@given(instance=DOM::TryStatement_strategy)
@settings(max_examples=50)
def test_dom::trystatement_instantiation(instance):
    assert isinstance(instance, DOM::TryStatement)

@given(instance=DOM::ParameterizedType_strategy)
@settings(max_examples=50)
def test_dom::parameterizedtype_instantiation(instance):
    assert isinstance(instance, DOM::ParameterizedType)

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

@given(instance=DOM::WhileStatement_strategy)
@settings(max_examples=50)
def test_dom::whilestatement_instantiation(instance):
    assert isinstance(instance, DOM::WhileStatement)

@given(instance=DOM::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, DOM::VariableDeclarationStatement)

@given(instance=DOM::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dom::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, DOM::SuperConstructorInvocation)

@given(instance=DOM::ThrowStatement_strategy)
@settings(max_examples=50)
def test_dom::throwstatement_instantiation(instance):
    assert isinstance(instance, DOM::ThrowStatement)

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

@given(instance=DOM::ForStatement_strategy)
@settings(max_examples=50)
def test_dom::forstatement_instantiation(instance):
    assert isinstance(instance, DOM::ForStatement)

@given(instance=DOM::ReturnStatement_strategy)
@settings(max_examples=50)
def test_dom::returnstatement_instantiation(instance):
    assert isinstance(instance, DOM::ReturnStatement)

@given(instance=DOM::LabeledStatement_strategy)
@settings(max_examples=50)
def test_dom::labeledstatement_instantiation(instance):
    assert isinstance(instance, DOM::LabeledStatement)

@given(instance=DOM::IfStatement_strategy)
@settings(max_examples=50)
def test_dom::ifstatement_instantiation(instance):
    assert isinstance(instance, DOM::IfStatement)

@given(instance=IMethod_strategy)
@settings(max_examples=50)
def test_imethod_instantiation(instance):
    assert isinstance(instance, IMethod)

@given(instance=IField_strategy)
@settings(max_examples=50)
def test_ifield_instantiation(instance):
    assert isinstance(instance, IField)

@given(instance=IInitializer_strategy)
@settings(max_examples=50)
def test_iinitializer_instantiation(instance):
    assert isinstance(instance, IInitializer)

@given(instance=IMember_strategy)
@settings(max_examples=50)
def test_imember_instantiation(instance):
    assert isinstance(instance, IMember)

@given(instance=Core::IInitializer_strategy)
@settings(max_examples=50)
def test_core::iinitializer_instantiation(instance):
    assert isinstance(instance, Core::IInitializer)

@given(instance=Core::IField_strategy)
@settings(max_examples=50)
def test_core::ifield_instantiation(instance):
    assert isinstance(instance, Core::IField)

@given(instance=Core::IField_strategy)
def test_core::ifield_isEnumConstant_type(instance):
    assert isinstance(instance.isEnumConstant, str)


@given(instance=Core::IField_strategy)
def test_core::ifield_isEnumConstant_setter(instance):
    original = instance.isEnumConstant
    instance.isEnumConstant = original
    assert instance.isEnumConstant == original

@given(instance=Core::IField_strategy)
def test_core::ifield_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=Core::IField_strategy)
def test_core::ifield_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=Core::IField_strategy)
def test_core::ifield_isTransient_type(instance):
    assert isinstance(instance.isTransient, str)


@given(instance=Core::IField_strategy)
def test_core::ifield_isTransient_setter(instance):
    original = instance.isTransient
    instance.isTransient = original
    assert instance.isTransient == original

@given(instance=Core::IField_strategy)
def test_core::ifield_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, str)


@given(instance=Core::IField_strategy)
def test_core::ifield_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=Core::IField_strategy)
def test_core::ifield_typeSignature_type(instance):
    assert isinstance(instance.typeSignature, str)


@given(instance=Core::IField_strategy)
def test_core::ifield_typeSignature_setter(instance):
    original = instance.typeSignature
    instance.typeSignature = original
    assert instance.typeSignature == original

@given(instance=Core::IType_strategy)
@settings(max_examples=50)
def test_core::itype_instantiation(instance):
    assert isinstance(instance, Core::IType)

@given(instance=Core::IType_strategy)
def test_core::itype_fullyQualifiedName_type(instance):
    assert isinstance(instance.fullyQualifiedName, str)


@given(instance=Core::IType_strategy)
def test_core::itype_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=Core::IType_strategy)
def test_core::itype_fullyQualifiedParametrizedName_type(instance):
    assert isinstance(instance.fullyQualifiedParametrizedName, str)


@given(instance=Core::IType_strategy)
def test_core::itype_fullyQualifiedParametrizedName_setter(instance):
    original = instance.fullyQualifiedParametrizedName
    instance.fullyQualifiedParametrizedName = original
    assert instance.fullyQualifiedParametrizedName == original

@given(instance=Core::Parameter_strategy)
@settings(max_examples=50)
def test_core::parameter_instantiation(instance):
    assert isinstance(instance, Core::Parameter)

@given(instance=Core::Parameter_strategy)
def test_core::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Core::Parameter_strategy)
def test_core::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Core::Parameter_strategy)
def test_core::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Core::Parameter_strategy)
def test_core::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Core::ISourceRange_strategy)
@settings(max_examples=50)
def test_core::isourcerange_instantiation(instance):
    assert isinstance(instance, Core::ISourceRange)

@given(instance=Core::ISourceRange_strategy)
def test_core::isourcerange_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=Core::ISourceRange_strategy)
def test_core::isourcerange_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=Core::ISourceRange_strategy)
def test_core::isourcerange_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=Core::ISourceRange_strategy)
def test_core::isourcerange_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Core::IMethod_strategy)
@settings(max_examples=50)
def test_core::imethod_instantiation(instance):
    assert isinstance(instance, Core::IMethod)

@given(instance=Core::IMethod_strategy)
def test_core::imethod_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=Core::IMethod_strategy)
def test_core::imethod_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=Core::IMethod_strategy)
def test_core::imethod_isConstructor_type(instance):
    assert isinstance(instance.isConstructor, str)


@given(instance=Core::IMethod_strategy)
def test_core::imethod_isConstructor_setter(instance):
    original = instance.isConstructor
    instance.isConstructor = original
    assert instance.isConstructor == original

@given(instance=Core::IMethod_strategy)
def test_core::imethod_isMainMethod_type(instance):
    assert isinstance(instance.isMainMethod, str)


@given(instance=Core::IMethod_strategy)
def test_core::imethod_isMainMethod_setter(instance):
    original = instance.isMainMethod
    instance.isMainMethod = original
    assert instance.isMainMethod == original

@given(instance=Core::IMethod_strategy)
def test_core::imethod_exceptionTypes_type(instance):
    assert isinstance(instance.exceptionTypes, str)


@given(instance=Core::IMethod_strategy)
def test_core::imethod_exceptionTypes_setter(instance):
    original = instance.exceptionTypes
    instance.exceptionTypes = original
    assert instance.exceptionTypes == original

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=IImportDeclaration_strategy)
@settings(max_examples=50)
def test_iimportdeclaration_instantiation(instance):
    assert isinstance(instance, IImportDeclaration)

@given(instance=IType_strategy)
@settings(max_examples=50)
def test_itype_instantiation(instance):
    assert isinstance(instance, IType)

@given(instance=ITypeRoot_strategy)
@settings(max_examples=50)
def test_ityperoot_instantiation(instance):
    assert isinstance(instance, ITypeRoot)

@given(instance=Core::IClassFile_strategy)
@settings(max_examples=50)
def test_core::iclassfile_instantiation(instance):
    assert isinstance(instance, Core::IClassFile)

@given(instance=Core::IClassFile_strategy)
def test_core::iclassfile_isClass_type(instance):
    assert isinstance(instance.isClass, str)


@given(instance=Core::IClassFile_strategy)
def test_core::iclassfile_isClass_setter(instance):
    original = instance.isClass
    instance.isClass = original
    assert instance.isClass == original

@given(instance=Core::IClassFile_strategy)
def test_core::iclassfile_isInterface_type(instance):
    assert isinstance(instance.isInterface, str)


@given(instance=Core::IClassFile_strategy)
def test_core::iclassfile_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original

@given(instance=Core::ICompilationUnit_strategy)
@settings(max_examples=50)
def test_core::icompilationunit_instantiation(instance):
    assert isinstance(instance, Core::ICompilationUnit)

@given(instance=ISourceReference_strategy)
@settings(max_examples=50)
def test_isourcereference_instantiation(instance):
    assert isinstance(instance, ISourceReference)

@given(instance=ICompilationUnit_strategy)
@settings(max_examples=50)
def test_icompilationunit_instantiation(instance):
    assert isinstance(instance, ICompilationUnit)

@given(instance=IClassFile_strategy)
@settings(max_examples=50)
def test_iclassfile_instantiation(instance):
    assert isinstance(instance, IClassFile)

@given(instance=IPackageFragment_strategy)
@settings(max_examples=50)
def test_ipackagefragment_instantiation(instance):
    assert isinstance(instance, IPackageFragment)

@given(instance=ISourceRange_strategy)
@settings(max_examples=50)
def test_isourcerange_instantiation(instance):
    assert isinstance(instance, ISourceRange)

@given(instance=Core::ISourceReference_strategy)
@settings(max_examples=50)
def test_core::isourcereference_instantiation(instance):
    assert isinstance(instance, Core::ISourceReference)

@given(instance=Core::ISourceReference_strategy)
def test_core::isourcereference_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=Core::ISourceReference_strategy)
def test_core::isourcereference_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=PhysicalElement_strategy)
@settings(max_examples=50)
def test_physicalelement_instantiation(instance):
    assert isinstance(instance, PhysicalElement)

@given(instance=Core::IJavaModel_strategy)
@settings(max_examples=50)
def test_core::ijavamodel_instantiation(instance):
    assert isinstance(instance, Core::IJavaModel)

@given(instance=Core::PhysicalElement_strategy)
@settings(max_examples=50)
def test_core::physicalelement_instantiation(instance):
    assert isinstance(instance, Core::PhysicalElement)

@given(instance=Core::PhysicalElement_strategy)
def test_core::physicalelement_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=Core::PhysicalElement_strategy)
def test_core::physicalelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Core::PhysicalElement_strategy)
def test_core::physicalelement_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=Core::PhysicalElement_strategy)
def test_core::physicalelement_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Core::IJavaElement_strategy)
@settings(max_examples=50)
def test_core::ijavaelement_instantiation(instance):
    assert isinstance(instance, Core::IJavaElement)

@given(instance=Core::IJavaElement_strategy)
def test_core::ijavaelement_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=Core::IJavaElement_strategy)
def test_core::ijavaelement_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=IJavaElement_strategy)
@settings(max_examples=50)
def test_ijavaelement_instantiation(instance):
    assert isinstance(instance, IJavaElement)

@given(instance=Core::IImportDeclaration_strategy)
@settings(max_examples=50)
def test_core::iimportdeclaration_instantiation(instance):
    assert isinstance(instance, Core::IImportDeclaration)

@given(instance=Core::IImportDeclaration_strategy)
def test_core::iimportdeclaration_isOnDemand_type(instance):
    assert isinstance(instance.isOnDemand, str)


@given(instance=Core::IImportDeclaration_strategy)
def test_core::iimportdeclaration_isOnDemand_setter(instance):
    original = instance.isOnDemand
    instance.isOnDemand = original
    assert instance.isOnDemand == original

@given(instance=Core::IImportDeclaration_strategy)
def test_core::iimportdeclaration_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=Core::IImportDeclaration_strategy)
def test_core::iimportdeclaration_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=Core::IPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_core::ipackagefragmentroot_instantiation(instance):
    assert isinstance(instance, Core::IPackageFragmentRoot)

@given(instance=Core::IMember_strategy)
@settings(max_examples=50)
def test_core::imember_instantiation(instance):
    assert isinstance(instance, Core::IMember)

@given(instance=Core::IPackageFragment_strategy)
@settings(max_examples=50)
def test_core::ipackagefragment_instantiation(instance):
    assert isinstance(instance, Core::IPackageFragment)

@given(instance=Core::IPackageFragment_strategy)
def test_core::ipackagefragment_isDefaultPackage_type(instance):
    assert isinstance(instance.isDefaultPackage, str)


@given(instance=Core::IPackageFragment_strategy)
def test_core::ipackagefragment_isDefaultPackage_setter(instance):
    original = instance.isDefaultPackage
    instance.isDefaultPackage = original
    assert instance.isDefaultPackage == original

@given(instance=Core::ITypeRoot_strategy)
@settings(max_examples=50)
def test_core::ityperoot_instantiation(instance):
    assert isinstance(instance, Core::ITypeRoot)

@given(instance=Core::ITypeParameter_strategy)
@settings(max_examples=50)
def test_core::itypeparameter_instantiation(instance):
    assert isinstance(instance, Core::ITypeParameter)

@given(instance=Core::ITypeParameter_strategy)
def test_core::itypeparameter_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=Core::ITypeParameter_strategy)
def test_core::itypeparameter_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=Core::IJavaProject_strategy)
@settings(max_examples=50)
def test_core::ijavaproject_instantiation(instance):
    assert isinstance(instance, Core::IJavaProject)

@given(instance=IPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_ipackagefragmentroot_instantiation(instance):
    assert isinstance(instance, IPackageFragmentRoot)

@given(instance=Core::BinaryPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_core::binarypackagefragmentroot_instantiation(instance):
    assert isinstance(instance, Core::BinaryPackageFragmentRoot)

@given(instance=Core::SourcePackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_core::sourcepackagefragmentroot_instantiation(instance):
    assert isinstance(instance, Core::SourcePackageFragmentRoot)

@given(instance=IJavaProject_strategy)
@settings(max_examples=50)
def test_ijavaproject_instantiation(instance):
    assert isinstance(instance, IJavaProject)
