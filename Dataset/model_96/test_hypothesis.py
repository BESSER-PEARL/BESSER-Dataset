import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VariableDeclaration,
    PrimitiveType,
    Java5::PrimitiveTypeLong,
    Java5::PrimitiveTypeDouble,
    Java5::PrimitiveTypeVoid,
    Java5::PrimitiveTypeChar,
    Java5::PrimitiveTypeFloat,
    Java5::PrimitiveTypeShort,
    Java5::PrimitiveTypeInt,
    Java5::PrimitiveTypeByte,
    Java5::PrimitiveTypeBoolean,
    Java5::Model,
    Java5::VariableDeclarationFragment,
    Java5::SingleVariableDeclaration,
    TypeDeclaration,
    Java5::InterfaceDeclaration,
    Java5::ClassDeclaration,
    Java5::ASTNode,
    Statement,
    Java5::VariableDeclarationStatement,
    Java5::EnhancedForStatement,
    Java5::ConstructorInvocation,
    Java5::DoStatement,
    Java5::ReturnStatement,
    Java5::Block,
    Java5::SwitchCase,
    Java5::ContinueStatement,
    Java5::SwitchStatement,
    Java5::ForStatement,
    Java5::CatchClause,
    Java5::SynchronizedStatement,
    Java5::ExpressionStatement,
    Java5::EmptyStatement,
    Java5::IfStatement,
    Java5::BreakStatement,
    Java5::AssertStatement,
    OrphanType,
    Java5::PrimitiveType,
    Java5::ParameterizedType,
    Java5::ArrayType,
    BodyDeclaration,
    Java5::EnumConstantDeclaration,
    Java5::MethodDeclaration,
    Java5::Initializer,
    Java5::FieldDeclaration,
    Java5::AbstractTypeDeclaration,
    ASTNode,
    Java5::Statement,
    Java5::MemberRef,
    Java5::NamedElement,
    Java5::Modifier,
    Java5::MethodRefParameter,
    Java5::MethodRef,
    Java5::AnonymousClassDeclaration,
    Java5::AnnotationTypeMemberDeclaration,
    AbstractTypeDeclaration,
    Java5::EnumDeclaration,
    Java5::AnnotationTypeDeclaration,
    Java5::Expression,
    NamedElement,
    Java5::UnresolvedItem,
    Java5::CompilationUnit,
    Java5::BodyDeclaration,
    Java5::TypeParameter,
    Java5::LabeledStatement,
    Java5::OrphanType,
    Java5::AnnotationMemberValuePair,
    Expression,
    Java5::PostfixExpression,
    Java5::ArrayInitializer,
    Java5::CharacterLiteral,
    Java5::MethodInvocation,
    Java5::BooleanLiteral,
    Java5::VariableDeclarationExpression,
    Java5::ConditionalExpression,
    Java5::ArrayAccess,
    Java5::Assignment,
    Java5::ArrayLengthAccess,
    Java5::InstanceofExpression,
    Java5::InfixExpression,
    Java5::PrefixExpression,
    Java5::ClassInstanceCreation,
    Java5::SuperFieldAccess,
    Java5::CastExpression,
    Java5::FieldAccess,
    Java5::NullLiteral,
    Java5::ParenthesizedExpression,
    Java5::SuperMethodInvocation,
    Java5::NumberLiteral,
    Java5::ArrayCreation,
    Java5::Annotation,
    Java5::NamedElementRef,
    Java5::PackageDeclaration,
    Java5::ImportDeclaration,
    Java5::WildCardType,
    Java5::VariableDeclaration,
    Java5::WhileStatement,
    Java5::ThisExpression,
    Java5::TextElement,
    Java5::TagElement,
    Java5::TryStatement,
    Java5::TypeLiteral,
    Java5::TypeDeclarationStatement,
    Java5::TypeDeclaration,
    Java5::ThrowStatement,
    Java5::SuperConstructorInvocation,
    Java5::StringLiteral,
    VisibilityKind,
    InheritanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeLong)


def test_java5::primitivetypelong_constructor_exists():
    assert callable(Java5::PrimitiveTypeLong.__init__)


def test_java5::primitivetypelong_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeDouble)


def test_java5::primitivetypedouble_constructor_exists():
    assert callable(Java5::PrimitiveTypeDouble.__init__)


def test_java5::primitivetypedouble_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeVoid)


def test_java5::primitivetypevoid_constructor_exists():
    assert callable(Java5::PrimitiveTypeVoid.__init__)


def test_java5::primitivetypevoid_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeChar)


def test_java5::primitivetypechar_constructor_exists():
    assert callable(Java5::PrimitiveTypeChar.__init__)


def test_java5::primitivetypechar_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeFloat)


def test_java5::primitivetypefloat_constructor_exists():
    assert callable(Java5::PrimitiveTypeFloat.__init__)


def test_java5::primitivetypefloat_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeShort)


def test_java5::primitivetypeshort_constructor_exists():
    assert callable(Java5::PrimitiveTypeShort.__init__)


def test_java5::primitivetypeshort_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeInt)


def test_java5::primitivetypeint_constructor_exists():
    assert callable(Java5::PrimitiveTypeInt.__init__)


def test_java5::primitivetypeint_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeByte)


def test_java5::primitivetypebyte_constructor_exists():
    assert callable(Java5::PrimitiveTypeByte.__init__)


def test_java5::primitivetypebyte_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveTypeBoolean)


def test_java5::primitivetypeboolean_constructor_exists():
    assert callable(Java5::PrimitiveTypeBoolean.__init__)


def test_java5::primitivetypeboolean_constructor_args():
    sig = inspect.signature(Java5::PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_java5::model_is_not_abstract():
    assert not inspect.isabstract(Java5::Model)


def test_java5::model_constructor_exists():
    assert callable(Java5::Model.__init__)


def test_java5::model_constructor_args():
    sig = inspect.signature(Java5::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java5::model_has_name():
    assert hasattr(Java5::Model, "name")
    descriptor = None
    for klass in Java5::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java5::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java5::VariableDeclarationFragment)


def test_java5::variabledeclarationfragment_constructor_exists():
    assert callable(Java5::VariableDeclarationFragment.__init__)


def test_java5::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java5::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java5::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::SingleVariableDeclaration)


def test_java5::singlevariabledeclaration_constructor_exists():
    assert callable(Java5::SingleVariableDeclaration.__init__)


def test_java5::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(Java5::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java5::singlevariabledeclaration_has_varargs():
    assert hasattr(Java5::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in Java5::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::InterfaceDeclaration)


def test_java5::interfacedeclaration_constructor_exists():
    assert callable(Java5::InterfaceDeclaration.__init__)


def test_java5::interfacedeclaration_constructor_args():
    sig = inspect.signature(Java5::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::ClassDeclaration)


def test_java5::classdeclaration_constructor_exists():
    assert callable(Java5::ClassDeclaration.__init__)


def test_java5::classdeclaration_constructor_args():
    sig = inspect.signature(Java5::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::astnode_is_not_abstract():
    assert not inspect.isabstract(Java5::ASTNode)


def test_java5::astnode_constructor_exists():
    assert callable(Java5::ASTNode.__init__)


def test_java5::astnode_constructor_args():
    sig = inspect.signature(Java5::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java5::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::VariableDeclarationStatement)


def test_java5::variabledeclarationstatement_constructor_exists():
    assert callable(Java5::VariableDeclarationStatement.__init__)


def test_java5::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(Java5::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java5::variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(Java5::VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in Java5::VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java5::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::EnhancedForStatement)


def test_java5::enhancedforstatement_constructor_exists():
    assert callable(Java5::EnhancedForStatement.__init__)


def test_java5::enhancedforstatement_constructor_args():
    sig = inspect.signature(Java5::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5::ConstructorInvocation)


def test_java5::constructorinvocation_constructor_exists():
    assert callable(Java5::ConstructorInvocation.__init__)


def test_java5::constructorinvocation_constructor_args():
    sig = inspect.signature(Java5::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5::dostatement_is_not_abstract():
    assert not inspect.isabstract(Java5::DoStatement)


def test_java5::dostatement_constructor_exists():
    assert callable(Java5::DoStatement.__init__)


def test_java5::dostatement_constructor_args():
    sig = inspect.signature(Java5::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::returnstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::ReturnStatement)


def test_java5::returnstatement_constructor_exists():
    assert callable(Java5::ReturnStatement.__init__)


def test_java5::returnstatement_constructor_args():
    sig = inspect.signature(Java5::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::block_is_not_abstract():
    assert not inspect.isabstract(Java5::Block)


def test_java5::block_constructor_exists():
    assert callable(Java5::Block.__init__)


def test_java5::block_constructor_args():
    sig = inspect.signature(Java5::Block.__init__)
    params = list(sig.parameters.keys())



def test_java5::switchcase_is_not_abstract():
    assert not inspect.isabstract(Java5::SwitchCase)


def test_java5::switchcase_constructor_exists():
    assert callable(Java5::SwitchCase.__init__)


def test_java5::switchcase_constructor_args():
    sig = inspect.signature(Java5::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java5::switchcase_has_default():
    assert hasattr(Java5::SwitchCase, "default")
    descriptor = None
    for klass in Java5::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java5::continuestatement_is_not_abstract():
    assert not inspect.isabstract(Java5::ContinueStatement)


def test_java5::continuestatement_constructor_exists():
    assert callable(Java5::ContinueStatement.__init__)


def test_java5::continuestatement_constructor_args():
    sig = inspect.signature(Java5::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::switchstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::SwitchStatement)


def test_java5::switchstatement_constructor_exists():
    assert callable(Java5::SwitchStatement.__init__)


def test_java5::switchstatement_constructor_args():
    sig = inspect.signature(Java5::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::forstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::ForStatement)


def test_java5::forstatement_constructor_exists():
    assert callable(Java5::ForStatement.__init__)


def test_java5::forstatement_constructor_args():
    sig = inspect.signature(Java5::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::catchclause_is_not_abstract():
    assert not inspect.isabstract(Java5::CatchClause)


def test_java5::catchclause_constructor_exists():
    assert callable(Java5::CatchClause.__init__)


def test_java5::catchclause_constructor_args():
    sig = inspect.signature(Java5::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java5::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::SynchronizedStatement)


def test_java5::synchronizedstatement_constructor_exists():
    assert callable(Java5::SynchronizedStatement.__init__)


def test_java5::synchronizedstatement_constructor_args():
    sig = inspect.signature(Java5::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::ExpressionStatement)


def test_java5::expressionstatement_constructor_exists():
    assert callable(Java5::ExpressionStatement.__init__)


def test_java5::expressionstatement_constructor_args():
    sig = inspect.signature(Java5::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::emptystatement_is_not_abstract():
    assert not inspect.isabstract(Java5::EmptyStatement)


def test_java5::emptystatement_constructor_exists():
    assert callable(Java5::EmptyStatement.__init__)


def test_java5::emptystatement_constructor_args():
    sig = inspect.signature(Java5::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::ifstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::IfStatement)


def test_java5::ifstatement_constructor_exists():
    assert callable(Java5::IfStatement.__init__)


def test_java5::ifstatement_constructor_args():
    sig = inspect.signature(Java5::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::breakstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::BreakStatement)


def test_java5::breakstatement_constructor_exists():
    assert callable(Java5::BreakStatement.__init__)


def test_java5::breakstatement_constructor_args():
    sig = inspect.signature(Java5::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::assertstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::AssertStatement)


def test_java5::assertstatement_constructor_exists():
    assert callable(Java5::AssertStatement.__init__)


def test_java5::assertstatement_constructor_args():
    sig = inspect.signature(Java5::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_orphantype_is_not_abstract():
    assert not inspect.isabstract(OrphanType)


def test_orphantype_constructor_exists():
    assert callable(OrphanType.__init__)


def test_orphantype_constructor_args():
    sig = inspect.signature(OrphanType.__init__)
    params = list(sig.parameters.keys())



def test_java5::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java5::PrimitiveType)


def test_java5::primitivetype_constructor_exists():
    assert callable(Java5::PrimitiveType.__init__)


def test_java5::primitivetype_constructor_args():
    sig = inspect.signature(Java5::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java5::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(Java5::ParameterizedType)


def test_java5::parameterizedtype_constructor_exists():
    assert callable(Java5::ParameterizedType.__init__)


def test_java5::parameterizedtype_constructor_args():
    sig = inspect.signature(Java5::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_java5::arraytype_is_not_abstract():
    assert not inspect.isabstract(Java5::ArrayType)


def test_java5::arraytype_constructor_exists():
    assert callable(Java5::ArrayType.__init__)


def test_java5::arraytype_constructor_args():
    sig = inspect.signature(Java5::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "originalName" in params, "Missing parameter 'originalName'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_java5::arraytype_has_originalName():
    assert hasattr(Java5::ArrayType, "originalName")
    descriptor = None
    for klass in Java5::ArrayType.__mro__:
        if "originalName" in klass.__dict__:
            descriptor = klass.__dict__["originalName"]
            break
    assert isinstance(descriptor, property)

def test_java5::arraytype_has_dimensions():
    assert hasattr(Java5::ArrayType, "dimensions")
    descriptor = None
    for klass in Java5::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::EnumConstantDeclaration)


def test_java5::enumconstantdeclaration_constructor_exists():
    assert callable(Java5::EnumConstantDeclaration.__init__)


def test_java5::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(Java5::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::MethodDeclaration)


def test_java5::methoddeclaration_constructor_exists():
    assert callable(Java5::MethodDeclaration.__init__)


def test_java5::methoddeclaration_constructor_args():
    sig = inspect.signature(Java5::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java5::methoddeclaration_has_constructor():
    assert hasattr(Java5::MethodDeclaration, "constructor")
    descriptor = None
    for klass in Java5::MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_java5::methoddeclaration_has_varargs():
    assert hasattr(Java5::MethodDeclaration, "varargs")
    descriptor = None
    for klass in Java5::MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_java5::methoddeclaration_has_extraArrayDimensions():
    assert hasattr(Java5::MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java5::MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java5::initializer_is_not_abstract():
    assert not inspect.isabstract(Java5::Initializer)


def test_java5::initializer_constructor_exists():
    assert callable(Java5::Initializer.__init__)


def test_java5::initializer_constructor_args():
    sig = inspect.signature(Java5::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java5::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::FieldDeclaration)


def test_java5::fielddeclaration_constructor_exists():
    assert callable(Java5::FieldDeclaration.__init__)


def test_java5::fielddeclaration_constructor_args():
    sig = inspect.signature(Java5::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::AbstractTypeDeclaration)


def test_java5::abstracttypedeclaration_constructor_exists():
    assert callable(Java5::AbstractTypeDeclaration.__init__)


def test_java5::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(Java5::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_java5::abstracttypedeclaration_has_qualifiedName():
    assert hasattr(Java5::AbstractTypeDeclaration, "qualifiedName")
    descriptor = None
    for klass in Java5::AbstractTypeDeclaration.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java5::statement_is_not_abstract():
    assert not inspect.isabstract(Java5::Statement)


def test_java5::statement_constructor_exists():
    assert callable(Java5::Statement.__init__)


def test_java5::statement_constructor_args():
    sig = inspect.signature(Java5::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java5::memberref_is_not_abstract():
    assert not inspect.isabstract(Java5::MemberRef)


def test_java5::memberref_constructor_exists():
    assert callable(Java5::MemberRef.__init__)


def test_java5::memberref_constructor_args():
    sig = inspect.signature(Java5::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java5::namedelement_is_not_abstract():
    assert not inspect.isabstract(Java5::NamedElement)


def test_java5::namedelement_constructor_exists():
    assert callable(Java5::NamedElement.__init__)


def test_java5::namedelement_constructor_args():
    sig = inspect.signature(Java5::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_java5::namedelement_has_name():
    assert hasattr(Java5::NamedElement, "name")
    descriptor = None
    for klass in Java5::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java5::namedelement_has_proxy():
    assert hasattr(Java5::NamedElement, "proxy")
    descriptor = None
    for klass in Java5::NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_java5::modifier_is_not_abstract():
    assert not inspect.isabstract(Java5::Modifier)


def test_java5::modifier_constructor_exists():
    assert callable(Java5::Modifier.__init__)


def test_java5::modifier_constructor_args():
    sig = inspect.signature(Java5::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "static" in params, "Missing parameter 'static'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "native" in params, "Missing parameter 'native'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_java5::modifier_has_synchronized():
    assert hasattr(Java5::Modifier, "synchronized")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_visibility():
    assert hasattr(Java5::Modifier, "visibility")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_strictfp():
    assert hasattr(Java5::Modifier, "strictfp")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_static():
    assert hasattr(Java5::Modifier, "static")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_transient():
    assert hasattr(Java5::Modifier, "transient")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_volatile():
    assert hasattr(Java5::Modifier, "volatile")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_native():
    assert hasattr(Java5::Modifier, "native")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_java5::modifier_has_inheritance():
    assert hasattr(Java5::Modifier, "inheritance")
    descriptor = None
    for klass in Java5::Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_java5::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(Java5::MethodRefParameter)


def test_java5::methodrefparameter_constructor_exists():
    assert callable(Java5::MethodRefParameter.__init__)


def test_java5::methodrefparameter_constructor_args():
    sig = inspect.signature(Java5::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isVarargs" in params, "Missing parameter 'isVarargs'"

def test_java5::methodrefparameter_has_name():
    assert hasattr(Java5::MethodRefParameter, "name")
    descriptor = None
    for klass in Java5::MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java5::methodrefparameter_has_isVarargs():
    assert hasattr(Java5::MethodRefParameter, "isVarargs")
    descriptor = None
    for klass in Java5::MethodRefParameter.__mro__:
        if "isVarargs" in klass.__dict__:
            descriptor = klass.__dict__["isVarargs"]
            break
    assert isinstance(descriptor, property)



def test_java5::methodref_is_not_abstract():
    assert not inspect.isabstract(Java5::MethodRef)


def test_java5::methodref_constructor_exists():
    assert callable(Java5::MethodRef.__init__)


def test_java5::methodref_constructor_args():
    sig = inspect.signature(Java5::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java5::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::AnonymousClassDeclaration)


def test_java5::anonymousclassdeclaration_constructor_exists():
    assert callable(Java5::AnonymousClassDeclaration.__init__)


def test_java5::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(Java5::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::AnnotationTypeMemberDeclaration)


def test_java5::annotationtypememberdeclaration_constructor_exists():
    assert callable(Java5::AnnotationTypeMemberDeclaration.__init__)


def test_java5::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java5::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::EnumDeclaration)


def test_java5::enumdeclaration_constructor_exists():
    assert callable(Java5::EnumDeclaration.__init__)


def test_java5::enumdeclaration_constructor_args():
    sig = inspect.signature(Java5::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::AnnotationTypeDeclaration)


def test_java5::annotationtypedeclaration_constructor_exists():
    assert callable(Java5::AnnotationTypeDeclaration.__init__)


def test_java5::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(Java5::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::expression_is_not_abstract():
    assert not inspect.isabstract(Java5::Expression)


def test_java5::expression_constructor_exists():
    assert callable(Java5::Expression.__init__)


def test_java5::expression_constructor_args():
    sig = inspect.signature(Java5::Expression.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java5::unresolveditem_is_not_abstract():
    assert not inspect.isabstract(Java5::UnresolvedItem)


def test_java5::unresolveditem_constructor_exists():
    assert callable(Java5::UnresolvedItem.__init__)


def test_java5::unresolveditem_constructor_args():
    sig = inspect.signature(Java5::UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java5::compilationunit_is_not_abstract():
    assert not inspect.isabstract(Java5::CompilationUnit)


def test_java5::compilationunit_constructor_exists():
    assert callable(Java5::CompilationUnit.__init__)


def test_java5::compilationunit_constructor_args():
    sig = inspect.signature(Java5::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java5::compilationunit_has_originalFilePath():
    assert hasattr(Java5::CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in Java5::CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java5::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::BodyDeclaration)


def test_java5::bodydeclaration_constructor_exists():
    assert callable(Java5::BodyDeclaration.__init__)


def test_java5::bodydeclaration_constructor_args():
    sig = inspect.signature(Java5::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::typeparameter_is_not_abstract():
    assert not inspect.isabstract(Java5::TypeParameter)


def test_java5::typeparameter_constructor_exists():
    assert callable(Java5::TypeParameter.__init__)


def test_java5::typeparameter_constructor_args():
    sig = inspect.signature(Java5::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java5::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::LabeledStatement)


def test_java5::labeledstatement_constructor_exists():
    assert callable(Java5::LabeledStatement.__init__)


def test_java5::labeledstatement_constructor_args():
    sig = inspect.signature(Java5::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::orphantype_is_not_abstract():
    assert not inspect.isabstract(Java5::OrphanType)


def test_java5::orphantype_constructor_exists():
    assert callable(Java5::OrphanType.__init__)


def test_java5::orphantype_constructor_args():
    sig = inspect.signature(Java5::OrphanType.__init__)
    params = list(sig.parameters.keys())



def test_java5::annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(Java5::AnnotationMemberValuePair)


def test_java5::annotationmembervaluepair_constructor_exists():
    assert callable(Java5::AnnotationMemberValuePair.__init__)


def test_java5::annotationmembervaluepair_constructor_args():
    sig = inspect.signature(Java5::AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java5::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::PostfixExpression)


def test_java5::postfixexpression_constructor_exists():
    assert callable(Java5::PostfixExpression.__init__)


def test_java5::postfixexpression_constructor_args():
    sig = inspect.signature(Java5::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5::postfixexpression_has_operator():
    assert hasattr(Java5::PostfixExpression, "operator")
    descriptor = None
    for klass in Java5::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Java5::ArrayInitializer)


def test_java5::arrayinitializer_constructor_exists():
    assert callable(Java5::ArrayInitializer.__init__)


def test_java5::arrayinitializer_constructor_args():
    sig = inspect.signature(Java5::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java5::characterliteral_is_not_abstract():
    assert not inspect.isabstract(Java5::CharacterLiteral)


def test_java5::characterliteral_constructor_exists():
    assert callable(Java5::CharacterLiteral.__init__)


def test_java5::characterliteral_constructor_args():
    sig = inspect.signature(Java5::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java5::characterliteral_has_value():
    assert hasattr(Java5::CharacterLiteral, "value")
    descriptor = None
    for klass in Java5::CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_java5::characterliteral_has_escapedValue():
    assert hasattr(Java5::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in Java5::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java5::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5::MethodInvocation)


def test_java5::methodinvocation_constructor_exists():
    assert callable(Java5::MethodInvocation.__init__)


def test_java5::methodinvocation_constructor_args():
    sig = inspect.signature(Java5::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(Java5::BooleanLiteral)


def test_java5::booleanliteral_constructor_exists():
    assert callable(Java5::BooleanLiteral.__init__)


def test_java5::booleanliteral_constructor_args():
    sig = inspect.signature(Java5::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java5::booleanliteral_has_value():
    assert hasattr(Java5::BooleanLiteral, "value")
    descriptor = None
    for klass in Java5::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java5::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::VariableDeclarationExpression)


def test_java5::variabledeclarationexpression_constructor_exists():
    assert callable(Java5::VariableDeclarationExpression.__init__)


def test_java5::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(Java5::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::ConditionalExpression)


def test_java5::conditionalexpression_constructor_exists():
    assert callable(Java5::ConditionalExpression.__init__)


def test_java5::conditionalexpression_constructor_args():
    sig = inspect.signature(Java5::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(Java5::ArrayAccess)


def test_java5::arrayaccess_constructor_exists():
    assert callable(Java5::ArrayAccess.__init__)


def test_java5::arrayaccess_constructor_args():
    sig = inspect.signature(Java5::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5::assignment_is_not_abstract():
    assert not inspect.isabstract(Java5::Assignment)


def test_java5::assignment_constructor_exists():
    assert callable(Java5::Assignment.__init__)


def test_java5::assignment_constructor_args():
    sig = inspect.signature(Java5::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5::assignment_has_operator():
    assert hasattr(Java5::Assignment, "operator")
    descriptor = None
    for klass in Java5::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5::arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(Java5::ArrayLengthAccess)


def test_java5::arraylengthaccess_constructor_exists():
    assert callable(Java5::ArrayLengthAccess.__init__)


def test_java5::arraylengthaccess_constructor_args():
    sig = inspect.signature(Java5::ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::InstanceofExpression)


def test_java5::instanceofexpression_constructor_exists():
    assert callable(Java5::InstanceofExpression.__init__)


def test_java5::instanceofexpression_constructor_args():
    sig = inspect.signature(Java5::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5::infixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::InfixExpression)


def test_java5::infixexpression_constructor_exists():
    assert callable(Java5::InfixExpression.__init__)


def test_java5::infixexpression_constructor_args():
    sig = inspect.signature(Java5::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5::infixexpression_has_operator():
    assert hasattr(Java5::InfixExpression, "operator")
    descriptor = None
    for klass in Java5::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::PrefixExpression)


def test_java5::prefixexpression_constructor_exists():
    assert callable(Java5::PrefixExpression.__init__)


def test_java5::prefixexpression_constructor_args():
    sig = inspect.signature(Java5::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5::prefixexpression_has_operator():
    assert hasattr(Java5::PrefixExpression, "operator")
    descriptor = None
    for klass in Java5::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(Java5::ClassInstanceCreation)


def test_java5::classinstancecreation_constructor_exists():
    assert callable(Java5::ClassInstanceCreation.__init__)


def test_java5::classinstancecreation_constructor_args():
    sig = inspect.signature(Java5::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java5::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java5::SuperFieldAccess)


def test_java5::superfieldaccess_constructor_exists():
    assert callable(Java5::SuperFieldAccess.__init__)


def test_java5::superfieldaccess_constructor_args():
    sig = inspect.signature(Java5::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5::castexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::CastExpression)


def test_java5::castexpression_constructor_exists():
    assert callable(Java5::CastExpression.__init__)


def test_java5::castexpression_constructor_args():
    sig = inspect.signature(Java5::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java5::FieldAccess)


def test_java5::fieldaccess_constructor_exists():
    assert callable(Java5::FieldAccess.__init__)


def test_java5::fieldaccess_constructor_args():
    sig = inspect.signature(Java5::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5::nullliteral_is_not_abstract():
    assert not inspect.isabstract(Java5::NullLiteral)


def test_java5::nullliteral_constructor_exists():
    assert callable(Java5::NullLiteral.__init__)


def test_java5::nullliteral_constructor_args():
    sig = inspect.signature(Java5::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java5::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::ParenthesizedExpression)


def test_java5::parenthesizedexpression_constructor_exists():
    assert callable(Java5::ParenthesizedExpression.__init__)


def test_java5::parenthesizedexpression_constructor_args():
    sig = inspect.signature(Java5::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5::SuperMethodInvocation)


def test_java5::supermethodinvocation_constructor_exists():
    assert callable(Java5::SuperMethodInvocation.__init__)


def test_java5::supermethodinvocation_constructor_args():
    sig = inspect.signature(Java5::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5::numberliteral_is_not_abstract():
    assert not inspect.isabstract(Java5::NumberLiteral)


def test_java5::numberliteral_constructor_exists():
    assert callable(Java5::NumberLiteral.__init__)


def test_java5::numberliteral_constructor_args():
    sig = inspect.signature(Java5::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java5::numberliteral_has_tokenValue():
    assert hasattr(Java5::NumberLiteral, "tokenValue")
    descriptor = None
    for klass in Java5::NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java5::arraycreation_is_not_abstract():
    assert not inspect.isabstract(Java5::ArrayCreation)


def test_java5::arraycreation_constructor_exists():
    assert callable(Java5::ArrayCreation.__init__)


def test_java5::arraycreation_constructor_args():
    sig = inspect.signature(Java5::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java5::annotation_is_not_abstract():
    assert not inspect.isabstract(Java5::Annotation)


def test_java5::annotation_constructor_exists():
    assert callable(Java5::Annotation.__init__)


def test_java5::annotation_constructor_args():
    sig = inspect.signature(Java5::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java5::namedelementref_is_not_abstract():
    assert not inspect.isabstract(Java5::NamedElementRef)


def test_java5::namedelementref_constructor_exists():
    assert callable(Java5::NamedElementRef.__init__)


def test_java5::namedelementref_constructor_args():
    sig = inspect.signature(Java5::NamedElementRef.__init__)
    params = list(sig.parameters.keys())



def test_java5::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::PackageDeclaration)


def test_java5::packagedeclaration_constructor_exists():
    assert callable(Java5::PackageDeclaration.__init__)


def test_java5::packagedeclaration_constructor_args():
    sig = inspect.signature(Java5::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_java5::packagedeclaration_has_qualifiedName():
    assert hasattr(Java5::PackageDeclaration, "qualifiedName")
    descriptor = None
    for klass in Java5::PackageDeclaration.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_java5::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::ImportDeclaration)


def test_java5::importdeclaration_constructor_exists():
    assert callable(Java5::ImportDeclaration.__init__)


def test_java5::importdeclaration_constructor_args():
    sig = inspect.signature(Java5::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java5::importdeclaration_has_static():
    assert hasattr(Java5::ImportDeclaration, "static")
    descriptor = None
    for klass in Java5::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java5::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(Java5::WildCardType)


def test_java5::wildcardtype_constructor_exists():
    assert callable(Java5::WildCardType.__init__)


def test_java5::wildcardtype_constructor_args():
    sig = inspect.signature(Java5::WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "isUpperBound" in params, "Missing parameter 'isUpperBound'"

def test_java5::wildcardtype_has_isUpperBound():
    assert hasattr(Java5::WildCardType, "isUpperBound")
    descriptor = None
    for klass in Java5::WildCardType.__mro__:
        if "isUpperBound" in klass.__dict__:
            descriptor = klass.__dict__["isUpperBound"]
            break
    assert isinstance(descriptor, property)



def test_java5::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::VariableDeclaration)


def test_java5::variabledeclaration_constructor_exists():
    assert callable(Java5::VariableDeclaration.__init__)


def test_java5::variabledeclaration_constructor_args():
    sig = inspect.signature(Java5::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java5::variabledeclaration_has_extraArrayDimensions():
    assert hasattr(Java5::VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java5::VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java5::whilestatement_is_not_abstract():
    assert not inspect.isabstract(Java5::WhileStatement)


def test_java5::whilestatement_constructor_exists():
    assert callable(Java5::WhileStatement.__init__)


def test_java5::whilestatement_constructor_args():
    sig = inspect.signature(Java5::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::thisexpression_is_not_abstract():
    assert not inspect.isabstract(Java5::ThisExpression)


def test_java5::thisexpression_constructor_exists():
    assert callable(Java5::ThisExpression.__init__)


def test_java5::thisexpression_constructor_args():
    sig = inspect.signature(Java5::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5::textelement_is_not_abstract():
    assert not inspect.isabstract(Java5::TextElement)


def test_java5::textelement_constructor_exists():
    assert callable(Java5::TextElement.__init__)


def test_java5::textelement_constructor_args():
    sig = inspect.signature(Java5::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java5::textelement_has_text():
    assert hasattr(Java5::TextElement, "text")
    descriptor = None
    for klass in Java5::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_java5::tagelement_is_not_abstract():
    assert not inspect.isabstract(Java5::TagElement)


def test_java5::tagelement_constructor_exists():
    assert callable(Java5::TagElement.__init__)


def test_java5::tagelement_constructor_args():
    sig = inspect.signature(Java5::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java5::tagelement_has_tagName():
    assert hasattr(Java5::TagElement, "tagName")
    descriptor = None
    for klass in Java5::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java5::trystatement_is_not_abstract():
    assert not inspect.isabstract(Java5::TryStatement)


def test_java5::trystatement_constructor_exists():
    assert callable(Java5::TryStatement.__init__)


def test_java5::trystatement_constructor_args():
    sig = inspect.signature(Java5::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::typeliteral_is_not_abstract():
    assert not inspect.isabstract(Java5::TypeLiteral)


def test_java5::typeliteral_constructor_exists():
    assert callable(Java5::TypeLiteral.__init__)


def test_java5::typeliteral_constructor_args():
    sig = inspect.signature(Java5::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java5::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::TypeDeclarationStatement)


def test_java5::typedeclarationstatement_constructor_exists():
    assert callable(Java5::TypeDeclarationStatement.__init__)


def test_java5::typedeclarationstatement_constructor_args():
    sig = inspect.signature(Java5::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5::TypeDeclaration)


def test_java5::typedeclaration_constructor_exists():
    assert callable(Java5::TypeDeclaration.__init__)


def test_java5::typedeclaration_constructor_args():
    sig = inspect.signature(Java5::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5::throwstatement_is_not_abstract():
    assert not inspect.isabstract(Java5::ThrowStatement)


def test_java5::throwstatement_constructor_exists():
    assert callable(Java5::ThrowStatement.__init__)


def test_java5::throwstatement_constructor_args():
    sig = inspect.signature(Java5::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5::SuperConstructorInvocation)


def test_java5::superconstructorinvocation_constructor_exists():
    assert callable(Java5::SuperConstructorInvocation.__init__)


def test_java5::superconstructorinvocation_constructor_args():
    sig = inspect.signature(Java5::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5::stringliteral_is_not_abstract():
    assert not inspect.isabstract(Java5::StringLiteral)


def test_java5::stringliteral_constructor_exists():
    assert callable(Java5::StringLiteral.__init__)


def test_java5::stringliteral_constructor_args():
    sig = inspect.signature(Java5::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "value" in params, "Missing parameter 'value'"

def test_java5::stringliteral_has_escapedValue():
    assert hasattr(Java5::StringLiteral, "escapedValue")
    descriptor = None
    for klass in Java5::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_java5::stringliteral_has_value():
    assert hasattr(Java5::StringLiteral, "value")
    descriptor = None
    for klass in Java5::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "none",
        "private",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "final",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"


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
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
Java5::PrimitiveTypeLong_strategy = st.builds(
    Java5::PrimitiveTypeLong,
)
Java5::PrimitiveTypeDouble_strategy = st.builds(
    Java5::PrimitiveTypeDouble,
)
Java5::PrimitiveTypeVoid_strategy = st.builds(
    Java5::PrimitiveTypeVoid,
)
Java5::PrimitiveTypeChar_strategy = st.builds(
    Java5::PrimitiveTypeChar,
)
Java5::PrimitiveTypeFloat_strategy = st.builds(
    Java5::PrimitiveTypeFloat,
)
Java5::PrimitiveTypeShort_strategy = st.builds(
    Java5::PrimitiveTypeShort,
)
Java5::PrimitiveTypeInt_strategy = st.builds(
    Java5::PrimitiveTypeInt,
)
Java5::PrimitiveTypeByte_strategy = st.builds(
    Java5::PrimitiveTypeByte,
)
Java5::PrimitiveTypeBoolean_strategy = st.builds(
    Java5::PrimitiveTypeBoolean,
)
Java5::Model_strategy = st.builds(
    Java5::Model,
    name=
        safe_text
)
Java5::VariableDeclarationFragment_strategy = st.builds(
    Java5::VariableDeclarationFragment,
)
Java5::SingleVariableDeclaration_strategy = st.builds(
    Java5::SingleVariableDeclaration,
    varargs=
        st.booleans()
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Java5::InterfaceDeclaration_strategy = st.builds(
    Java5::InterfaceDeclaration,
)
Java5::ClassDeclaration_strategy = st.builds(
    Java5::ClassDeclaration,
)
Java5::ASTNode_strategy = st.builds(
    Java5::ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
Java5::VariableDeclarationStatement_strategy = st.builds(
    Java5::VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
Java5::EnhancedForStatement_strategy = st.builds(
    Java5::EnhancedForStatement,
)
Java5::ConstructorInvocation_strategy = st.builds(
    Java5::ConstructorInvocation,
)
Java5::DoStatement_strategy = st.builds(
    Java5::DoStatement,
)
Java5::ReturnStatement_strategy = st.builds(
    Java5::ReturnStatement,
)
Java5::Block_strategy = st.builds(
    Java5::Block,
)
Java5::SwitchCase_strategy = st.builds(
    Java5::SwitchCase,
    default=
        st.booleans()
)
Java5::ContinueStatement_strategy = st.builds(
    Java5::ContinueStatement,
)
Java5::SwitchStatement_strategy = st.builds(
    Java5::SwitchStatement,
)
Java5::ForStatement_strategy = st.builds(
    Java5::ForStatement,
)
Java5::CatchClause_strategy = st.builds(
    Java5::CatchClause,
)
Java5::SynchronizedStatement_strategy = st.builds(
    Java5::SynchronizedStatement,
)
Java5::ExpressionStatement_strategy = st.builds(
    Java5::ExpressionStatement,
)
Java5::EmptyStatement_strategy = st.builds(
    Java5::EmptyStatement,
)
Java5::IfStatement_strategy = st.builds(
    Java5::IfStatement,
)
Java5::BreakStatement_strategy = st.builds(
    Java5::BreakStatement,
)
Java5::AssertStatement_strategy = st.builds(
    Java5::AssertStatement,
)
OrphanType_strategy = st.builds(
    OrphanType,
)
Java5::PrimitiveType_strategy = st.builds(
    Java5::PrimitiveType,
)
Java5::ParameterizedType_strategy = st.builds(
    Java5::ParameterizedType,
)
Java5::ArrayType_strategy = st.builds(
    Java5::ArrayType,
    originalName=
        safe_text,
    dimensions=
        st.integers()
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
Java5::EnumConstantDeclaration_strategy = st.builds(
    Java5::EnumConstantDeclaration,
)
Java5::MethodDeclaration_strategy = st.builds(
    Java5::MethodDeclaration,
    constructor=
        st.booleans(),
    varargs=
        st.booleans(),
    extraArrayDimensions=
        st.integers()
)
Java5::Initializer_strategy = st.builds(
    Java5::Initializer,
)
Java5::FieldDeclaration_strategy = st.builds(
    Java5::FieldDeclaration,
)
Java5::AbstractTypeDeclaration_strategy = st.builds(
    Java5::AbstractTypeDeclaration,
    qualifiedName=
        safe_text
)
ASTNode_strategy = st.builds(
    ASTNode,
)
Java5::Statement_strategy = st.builds(
    Java5::Statement,
)
Java5::MemberRef_strategy = st.builds(
    Java5::MemberRef,
)
Java5::NamedElement_strategy = st.builds(
    Java5::NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
Java5::Modifier_strategy = st.builds(
    Java5::Modifier,
    synchronized=
        st.booleans(),
    visibility=
        safe_text,
    strictfp=
        st.booleans(),
    static=
        st.booleans(),
    transient=
        st.booleans(),
    volatile=
        st.booleans(),
    native=
        st.booleans(),
    inheritance=
        safe_text
)
Java5::MethodRefParameter_strategy = st.builds(
    Java5::MethodRefParameter,
    name=
        safe_text,
    isVarargs=
        safe_text
)
Java5::MethodRef_strategy = st.builds(
    Java5::MethodRef,
)
Java5::AnonymousClassDeclaration_strategy = st.builds(
    Java5::AnonymousClassDeclaration,
)
Java5::AnnotationTypeMemberDeclaration_strategy = st.builds(
    Java5::AnnotationTypeMemberDeclaration,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
Java5::EnumDeclaration_strategy = st.builds(
    Java5::EnumDeclaration,
)
Java5::AnnotationTypeDeclaration_strategy = st.builds(
    Java5::AnnotationTypeDeclaration,
)
Java5::Expression_strategy = st.builds(
    Java5::Expression,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Java5::UnresolvedItem_strategy = st.builds(
    Java5::UnresolvedItem,
)
Java5::CompilationUnit_strategy = st.builds(
    Java5::CompilationUnit,
    originalFilePath=
        safe_text
)
Java5::BodyDeclaration_strategy = st.builds(
    Java5::BodyDeclaration,
)
Java5::TypeParameter_strategy = st.builds(
    Java5::TypeParameter,
)
Java5::LabeledStatement_strategy = st.builds(
    Java5::LabeledStatement,
)
Java5::OrphanType_strategy = st.builds(
    Java5::OrphanType,
)
Java5::AnnotationMemberValuePair_strategy = st.builds(
    Java5::AnnotationMemberValuePair,
)
Expression_strategy = st.builds(
    Expression,
)
Java5::PostfixExpression_strategy = st.builds(
    Java5::PostfixExpression,
    operator=
        safe_text
)
Java5::ArrayInitializer_strategy = st.builds(
    Java5::ArrayInitializer,
)
Java5::CharacterLiteral_strategy = st.builds(
    Java5::CharacterLiteral,
    value=
        safe_text,
    escapedValue=
        safe_text
)
Java5::MethodInvocation_strategy = st.builds(
    Java5::MethodInvocation,
)
Java5::BooleanLiteral_strategy = st.builds(
    Java5::BooleanLiteral,
    value=
        st.booleans()
)
Java5::VariableDeclarationExpression_strategy = st.builds(
    Java5::VariableDeclarationExpression,
)
Java5::ConditionalExpression_strategy = st.builds(
    Java5::ConditionalExpression,
)
Java5::ArrayAccess_strategy = st.builds(
    Java5::ArrayAccess,
)
Java5::Assignment_strategy = st.builds(
    Java5::Assignment,
    operator=
        safe_text
)
Java5::ArrayLengthAccess_strategy = st.builds(
    Java5::ArrayLengthAccess,
)
Java5::InstanceofExpression_strategy = st.builds(
    Java5::InstanceofExpression,
)
Java5::InfixExpression_strategy = st.builds(
    Java5::InfixExpression,
    operator=
        safe_text
)
Java5::PrefixExpression_strategy = st.builds(
    Java5::PrefixExpression,
    operator=
        safe_text
)
Java5::ClassInstanceCreation_strategy = st.builds(
    Java5::ClassInstanceCreation,
)
Java5::SuperFieldAccess_strategy = st.builds(
    Java5::SuperFieldAccess,
)
Java5::CastExpression_strategy = st.builds(
    Java5::CastExpression,
)
Java5::FieldAccess_strategy = st.builds(
    Java5::FieldAccess,
)
Java5::NullLiteral_strategy = st.builds(
    Java5::NullLiteral,
)
Java5::ParenthesizedExpression_strategy = st.builds(
    Java5::ParenthesizedExpression,
)
Java5::SuperMethodInvocation_strategy = st.builds(
    Java5::SuperMethodInvocation,
)
Java5::NumberLiteral_strategy = st.builds(
    Java5::NumberLiteral,
    tokenValue=
        safe_text
)
Java5::ArrayCreation_strategy = st.builds(
    Java5::ArrayCreation,
)
Java5::Annotation_strategy = st.builds(
    Java5::Annotation,
)
Java5::NamedElementRef_strategy = st.builds(
    Java5::NamedElementRef,
)
Java5::PackageDeclaration_strategy = st.builds(
    Java5::PackageDeclaration,
    qualifiedName=
        safe_text
)
Java5::ImportDeclaration_strategy = st.builds(
    Java5::ImportDeclaration,
    static=
        st.booleans()
)
Java5::WildCardType_strategy = st.builds(
    Java5::WildCardType,
    isUpperBound=
        safe_text
)
Java5::VariableDeclaration_strategy = st.builds(
    Java5::VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java5::WhileStatement_strategy = st.builds(
    Java5::WhileStatement,
)
Java5::ThisExpression_strategy = st.builds(
    Java5::ThisExpression,
)
Java5::TextElement_strategy = st.builds(
    Java5::TextElement,
    text=
        safe_text
)
Java5::TagElement_strategy = st.builds(
    Java5::TagElement,
    tagName=
        safe_text
)
Java5::TryStatement_strategy = st.builds(
    Java5::TryStatement,
)
Java5::TypeLiteral_strategy = st.builds(
    Java5::TypeLiteral,
)
Java5::TypeDeclarationStatement_strategy = st.builds(
    Java5::TypeDeclarationStatement,
)
Java5::TypeDeclaration_strategy = st.builds(
    Java5::TypeDeclaration,
)
Java5::ThrowStatement_strategy = st.builds(
    Java5::ThrowStatement,
)
Java5::SuperConstructorInvocation_strategy = st.builds(
    Java5::SuperConstructorInvocation,
)
Java5::StringLiteral_strategy = st.builds(
    Java5::StringLiteral,
    escapedValue=
        safe_text,
    value=
        safe_text
)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=Java5::PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java5::primitivetypelong_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeLong)

@given(instance=Java5::PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java5::primitivetypedouble_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeDouble)

@given(instance=Java5::PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java5::primitivetypevoid_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeVoid)

@given(instance=Java5::PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java5::primitivetypechar_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeChar)

@given(instance=Java5::PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java5::primitivetypefloat_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeFloat)

@given(instance=Java5::PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java5::primitivetypeshort_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeShort)

@given(instance=Java5::PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java5::primitivetypeint_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeInt)

@given(instance=Java5::PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java5::primitivetypebyte_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeByte)

@given(instance=Java5::PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java5::primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveTypeBoolean)

@given(instance=Java5::Model_strategy)
@settings(max_examples=50)
def test_java5::model_instantiation(instance):
    assert isinstance(instance, Java5::Model)

@given(instance=Java5::Model_strategy)
def test_java5::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java5::Model_strategy)
def test_java5::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java5::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java5::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Java5::VariableDeclarationFragment)

@given(instance=Java5::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java5::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Java5::SingleVariableDeclaration)

@given(instance=Java5::SingleVariableDeclaration_strategy)
def test_java5::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=Java5::SingleVariableDeclaration_strategy)
def test_java5::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=Java5::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java5::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, Java5::InterfaceDeclaration)

@given(instance=Java5::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java5::classdeclaration_instantiation(instance):
    assert isinstance(instance, Java5::ClassDeclaration)

@given(instance=Java5::ASTNode_strategy)
@settings(max_examples=50)
def test_java5::astnode_instantiation(instance):
    assert isinstance(instance, Java5::ASTNode)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Java5::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java5::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java5::VariableDeclarationStatement)

@given(instance=Java5::VariableDeclarationStatement_strategy)
def test_java5::variabledeclarationstatement_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=Java5::VariableDeclarationStatement_strategy)
def test_java5::variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java5::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java5::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, Java5::EnhancedForStatement)

@given(instance=Java5::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java5::constructorinvocation_instantiation(instance):
    assert isinstance(instance, Java5::ConstructorInvocation)

@given(instance=Java5::DoStatement_strategy)
@settings(max_examples=50)
def test_java5::dostatement_instantiation(instance):
    assert isinstance(instance, Java5::DoStatement)

@given(instance=Java5::ReturnStatement_strategy)
@settings(max_examples=50)
def test_java5::returnstatement_instantiation(instance):
    assert isinstance(instance, Java5::ReturnStatement)

@given(instance=Java5::Block_strategy)
@settings(max_examples=50)
def test_java5::block_instantiation(instance):
    assert isinstance(instance, Java5::Block)

@given(instance=Java5::SwitchCase_strategy)
@settings(max_examples=50)
def test_java5::switchcase_instantiation(instance):
    assert isinstance(instance, Java5::SwitchCase)

@given(instance=Java5::SwitchCase_strategy)
def test_java5::switchcase_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=Java5::SwitchCase_strategy)
def test_java5::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Java5::ContinueStatement_strategy)
@settings(max_examples=50)
def test_java5::continuestatement_instantiation(instance):
    assert isinstance(instance, Java5::ContinueStatement)

@given(instance=Java5::SwitchStatement_strategy)
@settings(max_examples=50)
def test_java5::switchstatement_instantiation(instance):
    assert isinstance(instance, Java5::SwitchStatement)

@given(instance=Java5::ForStatement_strategy)
@settings(max_examples=50)
def test_java5::forstatement_instantiation(instance):
    assert isinstance(instance, Java5::ForStatement)

@given(instance=Java5::CatchClause_strategy)
@settings(max_examples=50)
def test_java5::catchclause_instantiation(instance):
    assert isinstance(instance, Java5::CatchClause)

@given(instance=Java5::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java5::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, Java5::SynchronizedStatement)

@given(instance=Java5::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java5::expressionstatement_instantiation(instance):
    assert isinstance(instance, Java5::ExpressionStatement)

@given(instance=Java5::EmptyStatement_strategy)
@settings(max_examples=50)
def test_java5::emptystatement_instantiation(instance):
    assert isinstance(instance, Java5::EmptyStatement)

@given(instance=Java5::IfStatement_strategy)
@settings(max_examples=50)
def test_java5::ifstatement_instantiation(instance):
    assert isinstance(instance, Java5::IfStatement)

@given(instance=Java5::BreakStatement_strategy)
@settings(max_examples=50)
def test_java5::breakstatement_instantiation(instance):
    assert isinstance(instance, Java5::BreakStatement)

@given(instance=Java5::AssertStatement_strategy)
@settings(max_examples=50)
def test_java5::assertstatement_instantiation(instance):
    assert isinstance(instance, Java5::AssertStatement)

@given(instance=OrphanType_strategy)
@settings(max_examples=50)
def test_orphantype_instantiation(instance):
    assert isinstance(instance, OrphanType)

@given(instance=Java5::PrimitiveType_strategy)
@settings(max_examples=50)
def test_java5::primitivetype_instantiation(instance):
    assert isinstance(instance, Java5::PrimitiveType)

@given(instance=Java5::ParameterizedType_strategy)
@settings(max_examples=50)
def test_java5::parameterizedtype_instantiation(instance):
    assert isinstance(instance, Java5::ParameterizedType)

@given(instance=Java5::ArrayType_strategy)
@settings(max_examples=50)
def test_java5::arraytype_instantiation(instance):
    assert isinstance(instance, Java5::ArrayType)

@given(instance=Java5::ArrayType_strategy)
def test_java5::arraytype_originalName_type(instance):
    assert isinstance(instance.originalName, str)


@given(instance=Java5::ArrayType_strategy)
def test_java5::arraytype_originalName_setter(instance):
    original = instance.originalName
    instance.originalName = original
    assert instance.originalName == original

@given(instance=Java5::ArrayType_strategy)
def test_java5::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, int)


@given(instance=Java5::ArrayType_strategy)
def test_java5::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=Java5::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java5::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, Java5::EnumConstantDeclaration)

@given(instance=Java5::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java5::methoddeclaration_instantiation(instance):
    assert isinstance(instance, Java5::MethodDeclaration)

@given(instance=Java5::MethodDeclaration_strategy)
def test_java5::methoddeclaration_constructor_type(instance):
    assert isinstance(instance.constructor, bool)


@given(instance=Java5::MethodDeclaration_strategy)
def test_java5::methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=Java5::MethodDeclaration_strategy)
def test_java5::methoddeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=Java5::MethodDeclaration_strategy)
def test_java5::methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=Java5::MethodDeclaration_strategy)
def test_java5::methoddeclaration_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=Java5::MethodDeclaration_strategy)
def test_java5::methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java5::Initializer_strategy)
@settings(max_examples=50)
def test_java5::initializer_instantiation(instance):
    assert isinstance(instance, Java5::Initializer)

@given(instance=Java5::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java5::fielddeclaration_instantiation(instance):
    assert isinstance(instance, Java5::FieldDeclaration)

@given(instance=Java5::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java5::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, Java5::AbstractTypeDeclaration)

@given(instance=Java5::AbstractTypeDeclaration_strategy)
def test_java5::abstracttypedeclaration_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=Java5::AbstractTypeDeclaration_strategy)
def test_java5::abstracttypedeclaration_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=Java5::Statement_strategy)
@settings(max_examples=50)
def test_java5::statement_instantiation(instance):
    assert isinstance(instance, Java5::Statement)

@given(instance=Java5::MemberRef_strategy)
@settings(max_examples=50)
def test_java5::memberref_instantiation(instance):
    assert isinstance(instance, Java5::MemberRef)

@given(instance=Java5::NamedElement_strategy)
@settings(max_examples=50)
def test_java5::namedelement_instantiation(instance):
    assert isinstance(instance, Java5::NamedElement)

@given(instance=Java5::NamedElement_strategy)
def test_java5::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java5::NamedElement_strategy)
def test_java5::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java5::NamedElement_strategy)
def test_java5::namedelement_proxy_type(instance):
    assert isinstance(instance.proxy, bool)


@given(instance=Java5::NamedElement_strategy)
def test_java5::namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=Java5::Modifier_strategy)
@settings(max_examples=50)
def test_java5::modifier_instantiation(instance):
    assert isinstance(instance, Java5::Modifier)

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, bool)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, bool)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_native_type(instance):
    assert isinstance(instance.native, bool)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_inheritance_type(instance):
    assert isinstance(instance.inheritance, str)


@given(instance=Java5::Modifier_strategy)
def test_java5::modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=Java5::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java5::methodrefparameter_instantiation(instance):
    assert isinstance(instance, Java5::MethodRefParameter)

@given(instance=Java5::MethodRefParameter_strategy)
def test_java5::methodrefparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java5::MethodRefParameter_strategy)
def test_java5::methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java5::MethodRefParameter_strategy)
def test_java5::methodrefparameter_isVarargs_type(instance):
    assert isinstance(instance.isVarargs, str)


@given(instance=Java5::MethodRefParameter_strategy)
def test_java5::methodrefparameter_isVarargs_setter(instance):
    original = instance.isVarargs
    instance.isVarargs = original
    assert instance.isVarargs == original

@given(instance=Java5::MethodRef_strategy)
@settings(max_examples=50)
def test_java5::methodref_instantiation(instance):
    assert isinstance(instance, Java5::MethodRef)

@given(instance=Java5::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java5::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, Java5::AnonymousClassDeclaration)

@given(instance=Java5::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java5::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, Java5::AnnotationTypeMemberDeclaration)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=Java5::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java5::enumdeclaration_instantiation(instance):
    assert isinstance(instance, Java5::EnumDeclaration)

@given(instance=Java5::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java5::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, Java5::AnnotationTypeDeclaration)

@given(instance=Java5::Expression_strategy)
@settings(max_examples=50)
def test_java5::expression_instantiation(instance):
    assert isinstance(instance, Java5::Expression)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Java5::UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java5::unresolveditem_instantiation(instance):
    assert isinstance(instance, Java5::UnresolvedItem)

@given(instance=Java5::CompilationUnit_strategy)
@settings(max_examples=50)
def test_java5::compilationunit_instantiation(instance):
    assert isinstance(instance, Java5::CompilationUnit)

@given(instance=Java5::CompilationUnit_strategy)
def test_java5::compilationunit_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=Java5::CompilationUnit_strategy)
def test_java5::compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java5::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java5::bodydeclaration_instantiation(instance):
    assert isinstance(instance, Java5::BodyDeclaration)

@given(instance=Java5::TypeParameter_strategy)
@settings(max_examples=50)
def test_java5::typeparameter_instantiation(instance):
    assert isinstance(instance, Java5::TypeParameter)

@given(instance=Java5::LabeledStatement_strategy)
@settings(max_examples=50)
def test_java5::labeledstatement_instantiation(instance):
    assert isinstance(instance, Java5::LabeledStatement)

@given(instance=Java5::OrphanType_strategy)
@settings(max_examples=50)
def test_java5::orphantype_instantiation(instance):
    assert isinstance(instance, Java5::OrphanType)

@given(instance=Java5::AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java5::annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, Java5::AnnotationMemberValuePair)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Java5::PostfixExpression_strategy)
@settings(max_examples=50)
def test_java5::postfixexpression_instantiation(instance):
    assert isinstance(instance, Java5::PostfixExpression)

@given(instance=Java5::PostfixExpression_strategy)
def test_java5::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java5::PostfixExpression_strategy)
def test_java5::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java5::arrayinitializer_instantiation(instance):
    assert isinstance(instance, Java5::ArrayInitializer)

@given(instance=Java5::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java5::characterliteral_instantiation(instance):
    assert isinstance(instance, Java5::CharacterLiteral)

@given(instance=Java5::CharacterLiteral_strategy)
def test_java5::characterliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Java5::CharacterLiteral_strategy)
def test_java5::characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java5::CharacterLiteral_strategy)
def test_java5::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=Java5::CharacterLiteral_strategy)
def test_java5::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java5::MethodInvocation_strategy)
@settings(max_examples=50)
def test_java5::methodinvocation_instantiation(instance):
    assert isinstance(instance, Java5::MethodInvocation)

@given(instance=Java5::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java5::booleanliteral_instantiation(instance):
    assert isinstance(instance, Java5::BooleanLiteral)

@given(instance=Java5::BooleanLiteral_strategy)
def test_java5::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=Java5::BooleanLiteral_strategy)
def test_java5::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java5::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java5::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, Java5::VariableDeclarationExpression)

@given(instance=Java5::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java5::conditionalexpression_instantiation(instance):
    assert isinstance(instance, Java5::ConditionalExpression)

@given(instance=Java5::ArrayAccess_strategy)
@settings(max_examples=50)
def test_java5::arrayaccess_instantiation(instance):
    assert isinstance(instance, Java5::ArrayAccess)

@given(instance=Java5::Assignment_strategy)
@settings(max_examples=50)
def test_java5::assignment_instantiation(instance):
    assert isinstance(instance, Java5::Assignment)

@given(instance=Java5::Assignment_strategy)
def test_java5::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java5::Assignment_strategy)
def test_java5::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5::ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java5::arraylengthaccess_instantiation(instance):
    assert isinstance(instance, Java5::ArrayLengthAccess)

@given(instance=Java5::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java5::instanceofexpression_instantiation(instance):
    assert isinstance(instance, Java5::InstanceofExpression)

@given(instance=Java5::InfixExpression_strategy)
@settings(max_examples=50)
def test_java5::infixexpression_instantiation(instance):
    assert isinstance(instance, Java5::InfixExpression)

@given(instance=Java5::InfixExpression_strategy)
def test_java5::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java5::InfixExpression_strategy)
def test_java5::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5::PrefixExpression_strategy)
@settings(max_examples=50)
def test_java5::prefixexpression_instantiation(instance):
    assert isinstance(instance, Java5::PrefixExpression)

@given(instance=Java5::PrefixExpression_strategy)
def test_java5::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java5::PrefixExpression_strategy)
def test_java5::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java5::classinstancecreation_instantiation(instance):
    assert isinstance(instance, Java5::ClassInstanceCreation)

@given(instance=Java5::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java5::superfieldaccess_instantiation(instance):
    assert isinstance(instance, Java5::SuperFieldAccess)

@given(instance=Java5::CastExpression_strategy)
@settings(max_examples=50)
def test_java5::castexpression_instantiation(instance):
    assert isinstance(instance, Java5::CastExpression)

@given(instance=Java5::FieldAccess_strategy)
@settings(max_examples=50)
def test_java5::fieldaccess_instantiation(instance):
    assert isinstance(instance, Java5::FieldAccess)

@given(instance=Java5::NullLiteral_strategy)
@settings(max_examples=50)
def test_java5::nullliteral_instantiation(instance):
    assert isinstance(instance, Java5::NullLiteral)

@given(instance=Java5::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java5::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, Java5::ParenthesizedExpression)

@given(instance=Java5::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java5::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, Java5::SuperMethodInvocation)

@given(instance=Java5::NumberLiteral_strategy)
@settings(max_examples=50)
def test_java5::numberliteral_instantiation(instance):
    assert isinstance(instance, Java5::NumberLiteral)

@given(instance=Java5::NumberLiteral_strategy)
def test_java5::numberliteral_tokenValue_type(instance):
    assert isinstance(instance.tokenValue, str)


@given(instance=Java5::NumberLiteral_strategy)
def test_java5::numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=Java5::ArrayCreation_strategy)
@settings(max_examples=50)
def test_java5::arraycreation_instantiation(instance):
    assert isinstance(instance, Java5::ArrayCreation)

@given(instance=Java5::Annotation_strategy)
@settings(max_examples=50)
def test_java5::annotation_instantiation(instance):
    assert isinstance(instance, Java5::Annotation)

@given(instance=Java5::NamedElementRef_strategy)
@settings(max_examples=50)
def test_java5::namedelementref_instantiation(instance):
    assert isinstance(instance, Java5::NamedElementRef)

@given(instance=Java5::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_java5::packagedeclaration_instantiation(instance):
    assert isinstance(instance, Java5::PackageDeclaration)

@given(instance=Java5::PackageDeclaration_strategy)
def test_java5::packagedeclaration_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=Java5::PackageDeclaration_strategy)
def test_java5::packagedeclaration_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=Java5::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java5::importdeclaration_instantiation(instance):
    assert isinstance(instance, Java5::ImportDeclaration)

@given(instance=Java5::ImportDeclaration_strategy)
def test_java5::importdeclaration_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=Java5::ImportDeclaration_strategy)
def test_java5::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java5::WildCardType_strategy)
@settings(max_examples=50)
def test_java5::wildcardtype_instantiation(instance):
    assert isinstance(instance, Java5::WildCardType)

@given(instance=Java5::WildCardType_strategy)
def test_java5::wildcardtype_isUpperBound_type(instance):
    assert isinstance(instance.isUpperBound, str)


@given(instance=Java5::WildCardType_strategy)
def test_java5::wildcardtype_isUpperBound_setter(instance):
    original = instance.isUpperBound
    instance.isUpperBound = original
    assert instance.isUpperBound == original

@given(instance=Java5::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java5::variabledeclaration_instantiation(instance):
    assert isinstance(instance, Java5::VariableDeclaration)

@given(instance=Java5::VariableDeclaration_strategy)
def test_java5::variabledeclaration_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=Java5::VariableDeclaration_strategy)
def test_java5::variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java5::WhileStatement_strategy)
@settings(max_examples=50)
def test_java5::whilestatement_instantiation(instance):
    assert isinstance(instance, Java5::WhileStatement)

@given(instance=Java5::ThisExpression_strategy)
@settings(max_examples=50)
def test_java5::thisexpression_instantiation(instance):
    assert isinstance(instance, Java5::ThisExpression)

@given(instance=Java5::TextElement_strategy)
@settings(max_examples=50)
def test_java5::textelement_instantiation(instance):
    assert isinstance(instance, Java5::TextElement)

@given(instance=Java5::TextElement_strategy)
def test_java5::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=Java5::TextElement_strategy)
def test_java5::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Java5::TagElement_strategy)
@settings(max_examples=50)
def test_java5::tagelement_instantiation(instance):
    assert isinstance(instance, Java5::TagElement)

@given(instance=Java5::TagElement_strategy)
def test_java5::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=Java5::TagElement_strategy)
def test_java5::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=Java5::TryStatement_strategy)
@settings(max_examples=50)
def test_java5::trystatement_instantiation(instance):
    assert isinstance(instance, Java5::TryStatement)

@given(instance=Java5::TypeLiteral_strategy)
@settings(max_examples=50)
def test_java5::typeliteral_instantiation(instance):
    assert isinstance(instance, Java5::TypeLiteral)

@given(instance=Java5::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java5::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java5::TypeDeclarationStatement)

@given(instance=Java5::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java5::typedeclaration_instantiation(instance):
    assert isinstance(instance, Java5::TypeDeclaration)

@given(instance=Java5::ThrowStatement_strategy)
@settings(max_examples=50)
def test_java5::throwstatement_instantiation(instance):
    assert isinstance(instance, Java5::ThrowStatement)

@given(instance=Java5::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java5::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, Java5::SuperConstructorInvocation)

@given(instance=Java5::StringLiteral_strategy)
@settings(max_examples=50)
def test_java5::stringliteral_instantiation(instance):
    assert isinstance(instance, Java5::StringLiteral)

@given(instance=Java5::StringLiteral_strategy)
def test_java5::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=Java5::StringLiteral_strategy)
def test_java5::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java5::StringLiteral_strategy)
def test_java5::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Java5::StringLiteral_strategy)
def test_java5::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
