import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VariableDeclaration,
    AbstractVariablesContainer,
    TypeDeclaration,
    Java::ClassDeclaration,
    AbstractMethodDeclaration,
    MethodDeclaration,
    LabeledStatement,
    InterfaceDeclaration,
    EnumDeclaration,
    VariableDeclarationFragment,
    SingleVariableDeclaration,
    ClassDeclaration,
    AnnotationTypeMemberDeclaration,
    UnresolvedItem,
    Java::UnresolvedAnnotationTypeMemberDeclaration,
    Java::UnresolvedEnumDeclaration,
    Java::UnresolvedInterfaceDeclaration,
    Java::UnresolvedVariableDeclarationFragment,
    Java::UnresolvedSingleVariableDeclaration,
    Java::UnresolvedLabeledStatement,
    Java::UnresolvedMethodDeclaration,
    Java::UnresolvedClassDeclaration,
    AnnotationTypeDeclaration,
    Java::UnresolvedAnnotationDeclaration,
    AbstractTypeQualifiedExpression,
    Java::ThisExpression,
    Java::SuperFieldAccess,
    PrimitiveType,
    Java::PrimitiveTypeShort,
    Java::PrimitiveTypeVoid,
    Java::PrimitiveTypeInt,
    Java::PrimitiveTypeLong,
    Java::PrimitiveTypeDouble,
    Java::PrimitiveTypeFloat,
    Java::PrimitiveTypeChar,
    Java::PrimitiveTypeByte,
    Java::PrimitiveTypeBoolean,
    NamespaceAccess,
    Java::PackageAccess,
    Java::Model,
    Java::MethodDeclaration,
    Java::ManifestEntry,
    Java::ManifestAttribute,
    Java::InterfaceDeclaration,
    Java::ConstructorDeclaration,
    AbstractMethodInvocation,
    Java::SuperMethodInvocation,
    Comment,
    Java::LineComment,
    Java::Javadoc,
    Java::BlockComment,
    Java::VariableDeclarationFragment,
    AbstractTypeDeclaration,
    Java::UnresolvedTypeDeclaration,
    Java::TypeDeclaration,
    Java::EnumDeclaration,
    Java::AnnotationTypeDeclaration,
    Java::ASTNode,
    Statement,
    Java::CatchClause,
    Java::VariableDeclarationStatement,
    Java::EnhancedForStatement,
    Java::DoStatement,
    Java::ForStatement,
    Java::BreakStatement,
    Java::EmptyStatement,
    Java::ReturnStatement,
    Java::TypeDeclarationStatement,
    Java::ExpressionStatement,
    Java::ConstructorInvocation,
    Java::TryStatement,
    Java::ContinueStatement,
    Java::WhileStatement,
    Java::IfStatement,
    Java::SuperConstructorInvocation,
    Java::SwitchStatement,
    Java::ThrowStatement,
    Java::SynchronizedStatement,
    Java::SwitchCase,
    Java::AssertStatement,
    Java::Manifest,
    NamedElement,
    Java::UnresolvedItem,
    Java::VariableDeclaration,
    Java::Type,
    Java::LabeledStatement,
    Java::ClassFile,
    Java::CompilationUnit,
    Java::Archive,
    Java::AnnotationMemberValuePair,
    Java::SingleVariableDeclaration,
    Expression,
    Java::Assignment,
    Java::CharacterLiteral,
    Java::MethodInvocation,
    Java::VariableDeclarationExpression,
    Java::ClassInstanceCreation,
    Java::ConditionalExpression,
    Java::PostfixExpression,
    Java::PrefixExpression,
    Java::FieldAccess,
    Java::NumberLiteral,
    Java::BooleanLiteral,
    Java::ParenthesizedExpression,
    Java::TypeAccess,
    Java::InfixExpression,
    Java::ArrayLengthAccess,
    Java::TypeLiteral,
    Java::NullLiteral,
    Java::ArrayInitializer,
    Java::InstanceofExpression,
    Java::Annotation,
    Java::ArrayCreation,
    Java::CastExpression,
    Java::UnresolvedItemAccess,
    Java::ArrayAccess,
    Java::SingleVariableAccess,
    Java::StringLiteral,
    Java::AbstractTypeQualifiedExpression,
    Java::Package,
    Java::BodyDeclaration,
    Type,
    Java::ArrayType,
    Java::WildCardType,
    Java::ParameterizedType,
    Java::TypeParameter,
    Java::PrimitiveType,
    Java::UnresolvedType,
    ASTNode,
    Java::MemberRef,
    Java::TagElement,
    Java::AnonymousClassDeclaration,
    Java::ImportDeclaration,
    Java::AbstractVariablesContainer,
    Java::Statement,
    Java::MethodRef,
    Java::Modifier,
    Java::NamedElement,
    Java::MethodRefParameter,
    Java::NamespaceAccess,
    Java::Comment,
    Java::TextElement,
    Java::Expression,
    Java::AbstractMethodInvocation,
    Java::Block,
    BodyDeclaration,
    Java::AnnotationTypeMemberDeclaration,
    Java::AbstractTypeDeclaration,
    Java::EnumConstantDeclaration,
    Java::Initializer,
    Java::FieldDeclaration,
    Java::AbstractMethodDeclaration,
    InheritanceKind,
    AssignmentKind,
    PrefixExpressionKind,
    VisibilityKind,
    InfixExpressionKind,
    PostfixExpressionKind,
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



def test_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractVariablesContainer)


def test_abstractvariablescontainer_constructor_exists():
    assert callable(AbstractVariablesContainer.__init__)


def test_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::ClassDeclaration)


def test_java::classdeclaration_constructor_exists():
    assert callable(Java::ClassDeclaration.__init__)


def test_java::classdeclaration_constructor_args():
    sig = inspect.signature(Java::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(MethodDeclaration)


def test_methoddeclaration_constructor_exists():
    assert callable(MethodDeclaration.__init__)


def test_methoddeclaration_constructor_args():
    sig = inspect.signature(MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(LabeledStatement)


def test_labeledstatement_constructor_exists():
    assert callable(LabeledStatement.__init__)


def test_labeledstatement_constructor_args():
    sig = inspect.signature(LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(InterfaceDeclaration)


def test_interfacedeclaration_constructor_exists():
    assert callable(InterfaceDeclaration.__init__)


def test_interfacedeclaration_constructor_args():
    sig = inspect.signature(InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumDeclaration)


def test_enumdeclaration_constructor_exists():
    assert callable(EnumDeclaration.__init__)


def test_enumdeclaration_constructor_args():
    sig = inspect.signature(EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationFragment)


def test_variabledeclarationfragment_constructor_exists():
    assert callable(VariableDeclarationFragment.__init__)


def test_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassDeclaration)


def test_classdeclaration_constructor_exists():
    assert callable(ClassDeclaration.__init__)


def test_classdeclaration_constructor_args():
    sig = inspect.signature(ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(AnnotationTypeMemberDeclaration)


def test_annotationtypememberdeclaration_constructor_exists():
    assert callable(AnnotationTypeMemberDeclaration.__init__)


def test_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(UnresolvedItem)


def test_unresolveditem_constructor_exists():
    assert callable(UnresolvedItem.__init__)


def test_unresolveditem_constructor_args():
    sig = inspect.signature(UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedannotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedAnnotationTypeMemberDeclaration)


def test_java::unresolvedannotationtypememberdeclaration_constructor_exists():
    assert callable(Java::UnresolvedAnnotationTypeMemberDeclaration.__init__)


def test_java::unresolvedannotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedAnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedenumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedEnumDeclaration)


def test_java::unresolvedenumdeclaration_constructor_exists():
    assert callable(Java::UnresolvedEnumDeclaration.__init__)


def test_java::unresolvedenumdeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedEnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedInterfaceDeclaration)


def test_java::unresolvedinterfacedeclaration_constructor_exists():
    assert callable(Java::UnresolvedInterfaceDeclaration.__init__)


def test_java::unresolvedinterfacedeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedVariableDeclarationFragment)


def test_java::unresolvedvariabledeclarationfragment_constructor_exists():
    assert callable(Java::UnresolvedVariableDeclarationFragment.__init__)


def test_java::unresolvedvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java::UnresolvedVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedSingleVariableDeclaration)


def test_java::unresolvedsinglevariabledeclaration_constructor_exists():
    assert callable(Java::UnresolvedSingleVariableDeclaration.__init__)


def test_java::unresolvedsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedlabeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedLabeledStatement)


def test_java::unresolvedlabeledstatement_constructor_exists():
    assert callable(Java::UnresolvedLabeledStatement.__init__)


def test_java::unresolvedlabeledstatement_constructor_args():
    sig = inspect.signature(Java::UnresolvedLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedMethodDeclaration)


def test_java::unresolvedmethoddeclaration_constructor_exists():
    assert callable(Java::UnresolvedMethodDeclaration.__init__)


def test_java::unresolvedmethoddeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedClassDeclaration)


def test_java::unresolvedclassdeclaration_constructor_exists():
    assert callable(Java::UnresolvedClassDeclaration.__init__)


def test_java::unresolvedclassdeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AnnotationTypeDeclaration)


def test_annotationtypedeclaration_constructor_exists():
    assert callable(AnnotationTypeDeclaration.__init__)


def test_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedannotationdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedAnnotationDeclaration)


def test_java::unresolvedannotationdeclaration_constructor_exists():
    assert callable(Java::UnresolvedAnnotationDeclaration.__init__)


def test_java::unresolvedannotationdeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedAnnotationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeQualifiedExpression)


def test_abstracttypequalifiedexpression_constructor_exists():
    assert callable(AbstractTypeQualifiedExpression.__init__)


def test_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::thisexpression_is_not_abstract():
    assert not inspect.isabstract(Java::ThisExpression)


def test_java::thisexpression_constructor_exists():
    assert callable(Java::ThisExpression.__init__)


def test_java::thisexpression_constructor_args():
    sig = inspect.signature(Java::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java::SuperFieldAccess)


def test_java::superfieldaccess_constructor_exists():
    assert callable(Java::SuperFieldAccess.__init__)


def test_java::superfieldaccess_constructor_args():
    sig = inspect.signature(Java::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeShort)


def test_java::primitivetypeshort_constructor_exists():
    assert callable(Java::PrimitiveTypeShort.__init__)


def test_java::primitivetypeshort_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeVoid)


def test_java::primitivetypevoid_constructor_exists():
    assert callable(Java::PrimitiveTypeVoid.__init__)


def test_java::primitivetypevoid_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeInt)


def test_java::primitivetypeint_constructor_exists():
    assert callable(Java::PrimitiveTypeInt.__init__)


def test_java::primitivetypeint_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeLong)


def test_java::primitivetypelong_constructor_exists():
    assert callable(Java::PrimitiveTypeLong.__init__)


def test_java::primitivetypelong_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeDouble)


def test_java::primitivetypedouble_constructor_exists():
    assert callable(Java::PrimitiveTypeDouble.__init__)


def test_java::primitivetypedouble_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeFloat)


def test_java::primitivetypefloat_constructor_exists():
    assert callable(Java::PrimitiveTypeFloat.__init__)


def test_java::primitivetypefloat_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeChar)


def test_java::primitivetypechar_constructor_exists():
    assert callable(Java::PrimitiveTypeChar.__init__)


def test_java::primitivetypechar_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeByte)


def test_java::primitivetypebyte_constructor_exists():
    assert callable(Java::PrimitiveTypeByte.__init__)


def test_java::primitivetypebyte_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveTypeBoolean)


def test_java::primitivetypeboolean_constructor_exists():
    assert callable(Java::PrimitiveTypeBoolean.__init__)


def test_java::primitivetypeboolean_constructor_args():
    sig = inspect.signature(Java::PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::packageaccess_is_not_abstract():
    assert not inspect.isabstract(Java::PackageAccess)


def test_java::packageaccess_constructor_exists():
    assert callable(Java::PackageAccess.__init__)


def test_java::packageaccess_constructor_args():
    sig = inspect.signature(Java::PackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::model_is_not_abstract():
    assert not inspect.isabstract(Java::Model)


def test_java::model_constructor_exists():
    assert callable(Java::Model.__init__)


def test_java::model_constructor_args():
    sig = inspect.signature(Java::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::model_has_name():
    assert hasattr(Java::Model, "name")
    descriptor = None
    for klass in Java::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::MethodDeclaration)


def test_java::methoddeclaration_constructor_exists():
    assert callable(Java::MethodDeclaration.__init__)


def test_java::methoddeclaration_constructor_args():
    sig = inspect.signature(Java::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java::methoddeclaration_has_extraArrayDimensions():
    assert hasattr(Java::MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java::MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::manifestentry_is_not_abstract():
    assert not inspect.isabstract(Java::ManifestEntry)


def test_java::manifestentry_constructor_exists():
    assert callable(Java::ManifestEntry.__init__)


def test_java::manifestentry_constructor_args():
    sig = inspect.signature(Java::ManifestEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::manifestentry_has_name():
    assert hasattr(Java::ManifestEntry, "name")
    descriptor = None
    for klass in Java::ManifestEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::manifestattribute_is_not_abstract():
    assert not inspect.isabstract(Java::ManifestAttribute)


def test_java::manifestattribute_constructor_exists():
    assert callable(Java::ManifestAttribute.__init__)


def test_java::manifestattribute_constructor_args():
    sig = inspect.signature(Java::ManifestAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_java::manifestattribute_has_key():
    assert hasattr(Java::ManifestAttribute, "key")
    descriptor = None
    for klass in Java::ManifestAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_java::manifestattribute_has_value():
    assert hasattr(Java::ManifestAttribute, "value")
    descriptor = None
    for klass in Java::ManifestAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::InterfaceDeclaration)


def test_java::interfacedeclaration_constructor_exists():
    assert callable(Java::InterfaceDeclaration.__init__)


def test_java::interfacedeclaration_constructor_args():
    sig = inspect.signature(Java::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::ConstructorDeclaration)


def test_java::constructordeclaration_constructor_exists():
    assert callable(Java::ConstructorDeclaration.__init__)


def test_java::constructordeclaration_constructor_args():
    sig = inspect.signature(Java::ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodInvocation)


def test_abstractmethodinvocation_constructor_exists():
    assert callable(AbstractMethodInvocation.__init__)


def test_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java::SuperMethodInvocation)


def test_java::supermethodinvocation_constructor_exists():
    assert callable(Java::SuperMethodInvocation.__init__)


def test_java::supermethodinvocation_constructor_args():
    sig = inspect.signature(Java::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_java::linecomment_is_not_abstract():
    assert not inspect.isabstract(Java::LineComment)


def test_java::linecomment_constructor_exists():
    assert callable(Java::LineComment.__init__)


def test_java::linecomment_constructor_args():
    sig = inspect.signature(Java::LineComment.__init__)
    params = list(sig.parameters.keys())



def test_java::javadoc_is_not_abstract():
    assert not inspect.isabstract(Java::Javadoc)


def test_java::javadoc_constructor_exists():
    assert callable(Java::Javadoc.__init__)


def test_java::javadoc_constructor_args():
    sig = inspect.signature(Java::Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_java::blockcomment_is_not_abstract():
    assert not inspect.isabstract(Java::BlockComment)


def test_java::blockcomment_constructor_exists():
    assert callable(Java::BlockComment.__init__)


def test_java::blockcomment_constructor_args():
    sig = inspect.signature(Java::BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java::VariableDeclarationFragment)


def test_java::variabledeclarationfragment_constructor_exists():
    assert callable(Java::VariableDeclarationFragment.__init__)


def test_java::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedTypeDeclaration)


def test_java::unresolvedtypedeclaration_constructor_exists():
    assert callable(Java::UnresolvedTypeDeclaration.__init__)


def test_java::unresolvedtypedeclaration_constructor_args():
    sig = inspect.signature(Java::UnresolvedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::TypeDeclaration)


def test_java::typedeclaration_constructor_exists():
    assert callable(Java::TypeDeclaration.__init__)


def test_java::typedeclaration_constructor_args():
    sig = inspect.signature(Java::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::EnumDeclaration)


def test_java::enumdeclaration_constructor_exists():
    assert callable(Java::EnumDeclaration.__init__)


def test_java::enumdeclaration_constructor_args():
    sig = inspect.signature(Java::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::AnnotationTypeDeclaration)


def test_java::annotationtypedeclaration_constructor_exists():
    assert callable(Java::AnnotationTypeDeclaration.__init__)


def test_java::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(Java::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::astnode_is_not_abstract():
    assert not inspect.isabstract(Java::ASTNode)


def test_java::astnode_constructor_exists():
    assert callable(Java::ASTNode.__init__)


def test_java::astnode_constructor_args():
    sig = inspect.signature(Java::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::catchclause_is_not_abstract():
    assert not inspect.isabstract(Java::CatchClause)


def test_java::catchclause_constructor_exists():
    assert callable(Java::CatchClause.__init__)


def test_java::catchclause_constructor_args():
    sig = inspect.signature(Java::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java::VariableDeclarationStatement)


def test_java::variabledeclarationstatement_constructor_exists():
    assert callable(Java::VariableDeclarationStatement.__init__)


def test_java::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(Java::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java::variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(Java::VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in Java::VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(Java::EnhancedForStatement)


def test_java::enhancedforstatement_constructor_exists():
    assert callable(Java::EnhancedForStatement.__init__)


def test_java::enhancedforstatement_constructor_args():
    sig = inspect.signature(Java::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::dostatement_is_not_abstract():
    assert not inspect.isabstract(Java::DoStatement)


def test_java::dostatement_constructor_exists():
    assert callable(Java::DoStatement.__init__)


def test_java::dostatement_constructor_args():
    sig = inspect.signature(Java::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::forstatement_is_not_abstract():
    assert not inspect.isabstract(Java::ForStatement)


def test_java::forstatement_constructor_exists():
    assert callable(Java::ForStatement.__init__)


def test_java::forstatement_constructor_args():
    sig = inspect.signature(Java::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::breakstatement_is_not_abstract():
    assert not inspect.isabstract(Java::BreakStatement)


def test_java::breakstatement_constructor_exists():
    assert callable(Java::BreakStatement.__init__)


def test_java::breakstatement_constructor_args():
    sig = inspect.signature(Java::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::emptystatement_is_not_abstract():
    assert not inspect.isabstract(Java::EmptyStatement)


def test_java::emptystatement_constructor_exists():
    assert callable(Java::EmptyStatement.__init__)


def test_java::emptystatement_constructor_args():
    sig = inspect.signature(Java::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::returnstatement_is_not_abstract():
    assert not inspect.isabstract(Java::ReturnStatement)


def test_java::returnstatement_constructor_exists():
    assert callable(Java::ReturnStatement.__init__)


def test_java::returnstatement_constructor_args():
    sig = inspect.signature(Java::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java::TypeDeclarationStatement)


def test_java::typedeclarationstatement_constructor_exists():
    assert callable(Java::TypeDeclarationStatement.__init__)


def test_java::typedeclarationstatement_constructor_args():
    sig = inspect.signature(Java::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(Java::ExpressionStatement)


def test_java::expressionstatement_constructor_exists():
    assert callable(Java::ExpressionStatement.__init__)


def test_java::expressionstatement_constructor_args():
    sig = inspect.signature(Java::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java::ConstructorInvocation)


def test_java::constructorinvocation_constructor_exists():
    assert callable(Java::ConstructorInvocation.__init__)


def test_java::constructorinvocation_constructor_args():
    sig = inspect.signature(Java::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::trystatement_is_not_abstract():
    assert not inspect.isabstract(Java::TryStatement)


def test_java::trystatement_constructor_exists():
    assert callable(Java::TryStatement.__init__)


def test_java::trystatement_constructor_args():
    sig = inspect.signature(Java::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::continuestatement_is_not_abstract():
    assert not inspect.isabstract(Java::ContinueStatement)


def test_java::continuestatement_constructor_exists():
    assert callable(Java::ContinueStatement.__init__)


def test_java::continuestatement_constructor_args():
    sig = inspect.signature(Java::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::whilestatement_is_not_abstract():
    assert not inspect.isabstract(Java::WhileStatement)


def test_java::whilestatement_constructor_exists():
    assert callable(Java::WhileStatement.__init__)


def test_java::whilestatement_constructor_args():
    sig = inspect.signature(Java::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::ifstatement_is_not_abstract():
    assert not inspect.isabstract(Java::IfStatement)


def test_java::ifstatement_constructor_exists():
    assert callable(Java::IfStatement.__init__)


def test_java::ifstatement_constructor_args():
    sig = inspect.signature(Java::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java::SuperConstructorInvocation)


def test_java::superconstructorinvocation_constructor_exists():
    assert callable(Java::SuperConstructorInvocation.__init__)


def test_java::superconstructorinvocation_constructor_args():
    sig = inspect.signature(Java::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::switchstatement_is_not_abstract():
    assert not inspect.isabstract(Java::SwitchStatement)


def test_java::switchstatement_constructor_exists():
    assert callable(Java::SwitchStatement.__init__)


def test_java::switchstatement_constructor_args():
    sig = inspect.signature(Java::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::throwstatement_is_not_abstract():
    assert not inspect.isabstract(Java::ThrowStatement)


def test_java::throwstatement_constructor_exists():
    assert callable(Java::ThrowStatement.__init__)


def test_java::throwstatement_constructor_args():
    sig = inspect.signature(Java::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(Java::SynchronizedStatement)


def test_java::synchronizedstatement_constructor_exists():
    assert callable(Java::SynchronizedStatement.__init__)


def test_java::synchronizedstatement_constructor_args():
    sig = inspect.signature(Java::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::switchcase_is_not_abstract():
    assert not inspect.isabstract(Java::SwitchCase)


def test_java::switchcase_constructor_exists():
    assert callable(Java::SwitchCase.__init__)


def test_java::switchcase_constructor_args():
    sig = inspect.signature(Java::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java::switchcase_has_default():
    assert hasattr(Java::SwitchCase, "default")
    descriptor = None
    for klass in Java::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java::assertstatement_is_not_abstract():
    assert not inspect.isabstract(Java::AssertStatement)


def test_java::assertstatement_constructor_exists():
    assert callable(Java::AssertStatement.__init__)


def test_java::assertstatement_constructor_args():
    sig = inspect.signature(Java::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::manifest_is_not_abstract():
    assert not inspect.isabstract(Java::Manifest)


def test_java::manifest_constructor_exists():
    assert callable(Java::Manifest.__init__)


def test_java::manifest_constructor_args():
    sig = inspect.signature(Java::Manifest.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolveditem_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedItem)


def test_java::unresolveditem_constructor_exists():
    assert callable(Java::UnresolvedItem.__init__)


def test_java::unresolveditem_constructor_args():
    sig = inspect.signature(Java::UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::VariableDeclaration)


def test_java::variabledeclaration_constructor_exists():
    assert callable(Java::VariableDeclaration.__init__)


def test_java::variabledeclaration_constructor_args():
    sig = inspect.signature(Java::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java::variabledeclaration_has_extraArrayDimensions():
    assert hasattr(Java::VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java::VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::type_is_not_abstract():
    assert not inspect.isabstract(Java::Type)


def test_java::type_constructor_exists():
    assert callable(Java::Type.__init__)


def test_java::type_constructor_args():
    sig = inspect.signature(Java::Type.__init__)
    params = list(sig.parameters.keys())



def test_java::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java::LabeledStatement)


def test_java::labeledstatement_constructor_exists():
    assert callable(Java::LabeledStatement.__init__)


def test_java::labeledstatement_constructor_args():
    sig = inspect.signature(Java::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::classfile_is_not_abstract():
    assert not inspect.isabstract(Java::ClassFile)


def test_java::classfile_constructor_exists():
    assert callable(Java::ClassFile.__init__)


def test_java::classfile_constructor_args():
    sig = inspect.signature(Java::ClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java::classfile_has_originalFilePath():
    assert hasattr(Java::ClassFile, "originalFilePath")
    descriptor = None
    for klass in Java::ClassFile.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java::compilationunit_is_not_abstract():
    assert not inspect.isabstract(Java::CompilationUnit)


def test_java::compilationunit_constructor_exists():
    assert callable(Java::CompilationUnit.__init__)


def test_java::compilationunit_constructor_args():
    sig = inspect.signature(Java::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java::compilationunit_has_originalFilePath():
    assert hasattr(Java::CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in Java::CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java::archive_is_not_abstract():
    assert not inspect.isabstract(Java::Archive)


def test_java::archive_constructor_exists():
    assert callable(Java::Archive.__init__)


def test_java::archive_constructor_args():
    sig = inspect.signature(Java::Archive.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java::archive_has_originalFilePath():
    assert hasattr(Java::Archive, "originalFilePath")
    descriptor = None
    for klass in Java::Archive.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java::annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(Java::AnnotationMemberValuePair)


def test_java::annotationmembervaluepair_constructor_exists():
    assert callable(Java::AnnotationMemberValuePair.__init__)


def test_java::annotationmembervaluepair_constructor_args():
    sig = inspect.signature(Java::AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_java::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::SingleVariableDeclaration)


def test_java::singlevariabledeclaration_constructor_exists():
    assert callable(Java::SingleVariableDeclaration.__init__)


def test_java::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(Java::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java::singlevariabledeclaration_has_varargs():
    assert hasattr(Java::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in Java::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::assignment_is_not_abstract():
    assert not inspect.isabstract(Java::Assignment)


def test_java::assignment_constructor_exists():
    assert callable(Java::Assignment.__init__)


def test_java::assignment_constructor_args():
    sig = inspect.signature(Java::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::assignment_has_operator():
    assert hasattr(Java::Assignment, "operator")
    descriptor = None
    for klass in Java::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::characterliteral_is_not_abstract():
    assert not inspect.isabstract(Java::CharacterLiteral)


def test_java::characterliteral_constructor_exists():
    assert callable(Java::CharacterLiteral.__init__)


def test_java::characterliteral_constructor_args():
    sig = inspect.signature(Java::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java::characterliteral_has_escapedValue():
    assert hasattr(Java::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in Java::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java::MethodInvocation)


def test_java::methodinvocation_constructor_exists():
    assert callable(Java::MethodInvocation.__init__)


def test_java::methodinvocation_constructor_args():
    sig = inspect.signature(Java::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Java::VariableDeclarationExpression)


def test_java::variabledeclarationexpression_constructor_exists():
    assert callable(Java::VariableDeclarationExpression.__init__)


def test_java::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(Java::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(Java::ClassInstanceCreation)


def test_java::classinstancecreation_constructor_exists():
    assert callable(Java::ClassInstanceCreation.__init__)


def test_java::classinstancecreation_constructor_args():
    sig = inspect.signature(Java::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(Java::ConditionalExpression)


def test_java::conditionalexpression_constructor_exists():
    assert callable(Java::ConditionalExpression.__init__)


def test_java::conditionalexpression_constructor_args():
    sig = inspect.signature(Java::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(Java::PostfixExpression)


def test_java::postfixexpression_constructor_exists():
    assert callable(Java::PostfixExpression.__init__)


def test_java::postfixexpression_constructor_args():
    sig = inspect.signature(Java::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::postfixexpression_has_operator():
    assert hasattr(Java::PostfixExpression, "operator")
    descriptor = None
    for klass in Java::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(Java::PrefixExpression)


def test_java::prefixexpression_constructor_exists():
    assert callable(Java::PrefixExpression.__init__)


def test_java::prefixexpression_constructor_args():
    sig = inspect.signature(Java::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::prefixexpression_has_operator():
    assert hasattr(Java::PrefixExpression, "operator")
    descriptor = None
    for klass in Java::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java::FieldAccess)


def test_java::fieldaccess_constructor_exists():
    assert callable(Java::FieldAccess.__init__)


def test_java::fieldaccess_constructor_args():
    sig = inspect.signature(Java::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::numberliteral_is_not_abstract():
    assert not inspect.isabstract(Java::NumberLiteral)


def test_java::numberliteral_constructor_exists():
    assert callable(Java::NumberLiteral.__init__)


def test_java::numberliteral_constructor_args():
    sig = inspect.signature(Java::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java::numberliteral_has_tokenValue():
    assert hasattr(Java::NumberLiteral, "tokenValue")
    descriptor = None
    for klass in Java::NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(Java::BooleanLiteral)


def test_java::booleanliteral_constructor_exists():
    assert callable(Java::BooleanLiteral.__init__)


def test_java::booleanliteral_constructor_args():
    sig = inspect.signature(Java::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java::booleanliteral_has_value():
    assert hasattr(Java::BooleanLiteral, "value")
    descriptor = None
    for klass in Java::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(Java::ParenthesizedExpression)


def test_java::parenthesizedexpression_constructor_exists():
    assert callable(Java::ParenthesizedExpression.__init__)


def test_java::parenthesizedexpression_constructor_args():
    sig = inspect.signature(Java::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::typeaccess_is_not_abstract():
    assert not inspect.isabstract(Java::TypeAccess)


def test_java::typeaccess_constructor_exists():
    assert callable(Java::TypeAccess.__init__)


def test_java::typeaccess_constructor_args():
    sig = inspect.signature(Java::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::infixexpression_is_not_abstract():
    assert not inspect.isabstract(Java::InfixExpression)


def test_java::infixexpression_constructor_exists():
    assert callable(Java::InfixExpression.__init__)


def test_java::infixexpression_constructor_args():
    sig = inspect.signature(Java::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::infixexpression_has_operator():
    assert hasattr(Java::InfixExpression, "operator")
    descriptor = None
    for klass in Java::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(Java::ArrayLengthAccess)


def test_java::arraylengthaccess_constructor_exists():
    assert callable(Java::ArrayLengthAccess.__init__)


def test_java::arraylengthaccess_constructor_args():
    sig = inspect.signature(Java::ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::typeliteral_is_not_abstract():
    assert not inspect.isabstract(Java::TypeLiteral)


def test_java::typeliteral_constructor_exists():
    assert callable(Java::TypeLiteral.__init__)


def test_java::typeliteral_constructor_args():
    sig = inspect.signature(Java::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::nullliteral_is_not_abstract():
    assert not inspect.isabstract(Java::NullLiteral)


def test_java::nullliteral_constructor_exists():
    assert callable(Java::NullLiteral.__init__)


def test_java::nullliteral_constructor_args():
    sig = inspect.signature(Java::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Java::ArrayInitializer)


def test_java::arrayinitializer_constructor_exists():
    assert callable(Java::ArrayInitializer.__init__)


def test_java::arrayinitializer_constructor_args():
    sig = inspect.signature(Java::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(Java::InstanceofExpression)


def test_java::instanceofexpression_constructor_exists():
    assert callable(Java::InstanceofExpression.__init__)


def test_java::instanceofexpression_constructor_args():
    sig = inspect.signature(Java::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::annotation_is_not_abstract():
    assert not inspect.isabstract(Java::Annotation)


def test_java::annotation_constructor_exists():
    assert callable(Java::Annotation.__init__)


def test_java::annotation_constructor_args():
    sig = inspect.signature(Java::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java::arraycreation_is_not_abstract():
    assert not inspect.isabstract(Java::ArrayCreation)


def test_java::arraycreation_constructor_exists():
    assert callable(Java::ArrayCreation.__init__)


def test_java::arraycreation_constructor_args():
    sig = inspect.signature(Java::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java::castexpression_is_not_abstract():
    assert not inspect.isabstract(Java::CastExpression)


def test_java::castexpression_constructor_exists():
    assert callable(Java::CastExpression.__init__)


def test_java::castexpression_constructor_args():
    sig = inspect.signature(Java::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolveditemaccess_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedItemAccess)


def test_java::unresolveditemaccess_constructor_exists():
    assert callable(Java::UnresolvedItemAccess.__init__)


def test_java::unresolveditemaccess_constructor_args():
    sig = inspect.signature(Java::UnresolvedItemAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(Java::ArrayAccess)


def test_java::arrayaccess_constructor_exists():
    assert callable(Java::ArrayAccess.__init__)


def test_java::arrayaccess_constructor_args():
    sig = inspect.signature(Java::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::singlevariableaccess_is_not_abstract():
    assert not inspect.isabstract(Java::SingleVariableAccess)


def test_java::singlevariableaccess_constructor_exists():
    assert callable(Java::SingleVariableAccess.__init__)


def test_java::singlevariableaccess_constructor_args():
    sig = inspect.signature(Java::SingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::stringliteral_is_not_abstract():
    assert not inspect.isabstract(Java::StringLiteral)


def test_java::stringliteral_constructor_exists():
    assert callable(Java::StringLiteral.__init__)


def test_java::stringliteral_constructor_args():
    sig = inspect.signature(Java::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java::stringliteral_has_escapedValue():
    assert hasattr(Java::StringLiteral, "escapedValue")
    descriptor = None
    for klass in Java::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java::abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(Java::AbstractTypeQualifiedExpression)


def test_java::abstracttypequalifiedexpression_constructor_exists():
    assert callable(Java::AbstractTypeQualifiedExpression.__init__)


def test_java::abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(Java::AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::package_is_not_abstract():
    assert not inspect.isabstract(Java::Package)


def test_java::package_constructor_exists():
    assert callable(Java::Package.__init__)


def test_java::package_constructor_args():
    sig = inspect.signature(Java::Package.__init__)
    params = list(sig.parameters.keys())



def test_java::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::BodyDeclaration)


def test_java::bodydeclaration_constructor_exists():
    assert callable(Java::BodyDeclaration.__init__)


def test_java::bodydeclaration_constructor_args():
    sig = inspect.signature(Java::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java::arraytype_is_not_abstract():
    assert not inspect.isabstract(Java::ArrayType)


def test_java::arraytype_constructor_exists():
    assert callable(Java::ArrayType.__init__)


def test_java::arraytype_constructor_args():
    sig = inspect.signature(Java::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_java::arraytype_has_dimensions():
    assert hasattr(Java::ArrayType, "dimensions")
    descriptor = None
    for klass in Java::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(Java::WildCardType)


def test_java::wildcardtype_constructor_exists():
    assert callable(Java::WildCardType.__init__)


def test_java::wildcardtype_constructor_args():
    sig = inspect.signature(Java::WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_java::wildcardtype_has_upperBound():
    assert hasattr(Java::WildCardType, "upperBound")
    descriptor = None
    for klass in Java::WildCardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_java::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(Java::ParameterizedType)


def test_java::parameterizedtype_constructor_exists():
    assert callable(Java::ParameterizedType.__init__)


def test_java::parameterizedtype_constructor_args():
    sig = inspect.signature(Java::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_java::typeparameter_is_not_abstract():
    assert not inspect.isabstract(Java::TypeParameter)


def test_java::typeparameter_constructor_exists():
    assert callable(Java::TypeParameter.__init__)


def test_java::typeparameter_constructor_args():
    sig = inspect.signature(Java::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveType)


def test_java::primitivetype_constructor_exists():
    assert callable(Java::PrimitiveType.__init__)


def test_java::primitivetype_constructor_args():
    sig = inspect.signature(Java::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(Java::UnresolvedType)


def test_java::unresolvedtype_constructor_exists():
    assert callable(Java::UnresolvedType.__init__)


def test_java::unresolvedtype_constructor_args():
    sig = inspect.signature(Java::UnresolvedType.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java::memberref_is_not_abstract():
    assert not inspect.isabstract(Java::MemberRef)


def test_java::memberref_constructor_exists():
    assert callable(Java::MemberRef.__init__)


def test_java::memberref_constructor_args():
    sig = inspect.signature(Java::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java::tagelement_is_not_abstract():
    assert not inspect.isabstract(Java::TagElement)


def test_java::tagelement_constructor_exists():
    assert callable(Java::TagElement.__init__)


def test_java::tagelement_constructor_args():
    sig = inspect.signature(Java::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java::tagelement_has_tagName():
    assert hasattr(Java::TagElement, "tagName")
    descriptor = None
    for klass in Java::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::AnonymousClassDeclaration)


def test_java::anonymousclassdeclaration_constructor_exists():
    assert callable(Java::AnonymousClassDeclaration.__init__)


def test_java::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(Java::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::ImportDeclaration)


def test_java::importdeclaration_constructor_exists():
    assert callable(Java::ImportDeclaration.__init__)


def test_java::importdeclaration_constructor_args():
    sig = inspect.signature(Java::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java::importdeclaration_has_static():
    assert hasattr(Java::ImportDeclaration, "static")
    descriptor = None
    for klass in Java::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java::abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(Java::AbstractVariablesContainer)


def test_java::abstractvariablescontainer_constructor_exists():
    assert callable(Java::AbstractVariablesContainer.__init__)


def test_java::abstractvariablescontainer_constructor_args():
    sig = inspect.signature(Java::AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_java::statement_is_not_abstract():
    assert not inspect.isabstract(Java::Statement)


def test_java::statement_constructor_exists():
    assert callable(Java::Statement.__init__)


def test_java::statement_constructor_args():
    sig = inspect.signature(Java::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::methodref_is_not_abstract():
    assert not inspect.isabstract(Java::MethodRef)


def test_java::methodref_constructor_exists():
    assert callable(Java::MethodRef.__init__)


def test_java::methodref_constructor_args():
    sig = inspect.signature(Java::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java::modifier_is_not_abstract():
    assert not inspect.isabstract(Java::Modifier)


def test_java::modifier_constructor_exists():
    assert callable(Java::Modifier.__init__)


def test_java::modifier_constructor_args():
    sig = inspect.signature(Java::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"
    assert "native" in params, "Missing parameter 'native'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "volatile" in params, "Missing parameter 'volatile'"

def test_java::modifier_has_strictfp():
    assert hasattr(Java::Modifier, "strictfp")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_visibility():
    assert hasattr(Java::Modifier, "visibility")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_static():
    assert hasattr(Java::Modifier, "static")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_native():
    assert hasattr(Java::Modifier, "native")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_synchronized():
    assert hasattr(Java::Modifier, "synchronized")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_transient():
    assert hasattr(Java::Modifier, "transient")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_inheritance():
    assert hasattr(Java::Modifier, "inheritance")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_volatile():
    assert hasattr(Java::Modifier, "volatile")
    descriptor = None
    for klass in Java::Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)



def test_java::namedelement_is_not_abstract():
    assert not inspect.isabstract(Java::NamedElement)


def test_java::namedelement_constructor_exists():
    assert callable(Java::NamedElement.__init__)


def test_java::namedelement_constructor_args():
    sig = inspect.signature(Java::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "proxy" in params, "Missing parameter 'proxy'"
    assert "name" in params, "Missing parameter 'name'"

def test_java::namedelement_has_proxy():
    assert hasattr(Java::NamedElement, "proxy")
    descriptor = None
    for klass in Java::NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)

def test_java::namedelement_has_name():
    assert hasattr(Java::NamedElement, "name")
    descriptor = None
    for klass in Java::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(Java::MethodRefParameter)


def test_java::methodrefparameter_constructor_exists():
    assert callable(Java::MethodRefParameter.__init__)


def test_java::methodrefparameter_constructor_args():
    sig = inspect.signature(Java::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java::methodrefparameter_has_name():
    assert hasattr(Java::MethodRefParameter, "name")
    descriptor = None
    for klass in Java::MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::methodrefparameter_has_varargs():
    assert hasattr(Java::MethodRefParameter, "varargs")
    descriptor = None
    for klass in Java::MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_java::namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(Java::NamespaceAccess)


def test_java::namespaceaccess_constructor_exists():
    assert callable(Java::NamespaceAccess.__init__)


def test_java::namespaceaccess_constructor_args():
    sig = inspect.signature(Java::NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::comment_is_not_abstract():
    assert not inspect.isabstract(Java::Comment)


def test_java::comment_constructor_exists():
    assert callable(Java::Comment.__init__)


def test_java::comment_constructor_args():
    sig = inspect.signature(Java::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"
    assert "content" in params, "Missing parameter 'content'"

def test_java::comment_has_prefixOfParent():
    assert hasattr(Java::Comment, "prefixOfParent")
    descriptor = None
    for klass in Java::Comment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)

def test_java::comment_has_enclosedByParent():
    assert hasattr(Java::Comment, "enclosedByParent")
    descriptor = None
    for klass in Java::Comment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)

def test_java::comment_has_content():
    assert hasattr(Java::Comment, "content")
    descriptor = None
    for klass in Java::Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_java::textelement_is_not_abstract():
    assert not inspect.isabstract(Java::TextElement)


def test_java::textelement_constructor_exists():
    assert callable(Java::TextElement.__init__)


def test_java::textelement_constructor_args():
    sig = inspect.signature(Java::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java::textelement_has_text():
    assert hasattr(Java::TextElement, "text")
    descriptor = None
    for klass in Java::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_java::expression_is_not_abstract():
    assert not inspect.isabstract(Java::Expression)


def test_java::expression_constructor_exists():
    assert callable(Java::Expression.__init__)


def test_java::expression_constructor_args():
    sig = inspect.signature(Java::Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java::AbstractMethodInvocation)


def test_java::abstractmethodinvocation_constructor_exists():
    assert callable(Java::AbstractMethodInvocation.__init__)


def test_java::abstractmethodinvocation_constructor_args():
    sig = inspect.signature(Java::AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::block_is_not_abstract():
    assert not inspect.isabstract(Java::Block)


def test_java::block_constructor_exists():
    assert callable(Java::Block.__init__)


def test_java::block_constructor_args():
    sig = inspect.signature(Java::Block.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::AnnotationTypeMemberDeclaration)


def test_java::annotationtypememberdeclaration_constructor_exists():
    assert callable(Java::AnnotationTypeMemberDeclaration.__init__)


def test_java::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::AbstractTypeDeclaration)


def test_java::abstracttypedeclaration_constructor_exists():
    assert callable(Java::AbstractTypeDeclaration.__init__)


def test_java::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(Java::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::EnumConstantDeclaration)


def test_java::enumconstantdeclaration_constructor_exists():
    assert callable(Java::EnumConstantDeclaration.__init__)


def test_java::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(Java::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::initializer_is_not_abstract():
    assert not inspect.isabstract(Java::Initializer)


def test_java::initializer_constructor_exists():
    assert callable(Java::Initializer.__init__)


def test_java::initializer_constructor_args():
    sig = inspect.signature(Java::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::FieldDeclaration)


def test_java::fielddeclaration_constructor_exists():
    assert callable(Java::FieldDeclaration.__init__)


def test_java::fielddeclaration_constructor_args():
    sig = inspect.signature(Java::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::AbstractMethodDeclaration)


def test_java::abstractmethoddeclaration_constructor_exists():
    assert callable(Java::AbstractMethodDeclaration.__init__)


def test_java::abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(Java::AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "none",
        "abstract",
        "final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "REMAINDER_ASSIGN",
        "LEFT_SHIFT_ASSIGN",
        "ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "DIVIDE_ASSIGN",
        "MINUS_ASSIGN",
        "TIMES_ASSIGN",
        "BIT_XOR_ASSIGN",
        "BIT_OR_ASSIGN",
        "PLUS_ASSIGN",
        "BIT_AND_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentKind"

def test_prefixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionKind is not None

def test_prefixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionKind]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
        "PLUS",
        "NOT",
        "COMPLEMENT",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionKind"

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

def test_infixexpressionkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionKind is not None

def test_infixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionKind]
    expected_literals = [
        "RIGHT_SHIFT_UNSIGNED",
        "LESS_EQUALS",
        "LESS",
        "TIMES",
        "REMAINDER",
        "LEFT_SHIFT",
        "CONDITIONAL_AND",
        "PLUS",
        "XOR",
        "DIVIDE",
        "CONDITIONAL_OR",
        "NOT_EQUALS",
        "OR",
        "GREATER_EQUALS",
        "RIGHT_SHIFT_SIGNED",
        "MINUS",
        "GREATER",
        "AND",
        "EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionKind"

def test_postfixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpressionKind is not None

def test_postfixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpressionKind]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpressionKind"


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
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Java::ClassDeclaration_strategy = st.builds(
    Java::ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
MethodDeclaration_strategy = st.builds(
    MethodDeclaration,
)
LabeledStatement_strategy = st.builds(
    LabeledStatement,
)
InterfaceDeclaration_strategy = st.builds(
    InterfaceDeclaration,
)
EnumDeclaration_strategy = st.builds(
    EnumDeclaration,
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
)
ClassDeclaration_strategy = st.builds(
    ClassDeclaration,
)
AnnotationTypeMemberDeclaration_strategy = st.builds(
    AnnotationTypeMemberDeclaration,
)
UnresolvedItem_strategy = st.builds(
    UnresolvedItem,
)
Java::UnresolvedAnnotationTypeMemberDeclaration_strategy = st.builds(
    Java::UnresolvedAnnotationTypeMemberDeclaration,
)
Java::UnresolvedEnumDeclaration_strategy = st.builds(
    Java::UnresolvedEnumDeclaration,
)
Java::UnresolvedInterfaceDeclaration_strategy = st.builds(
    Java::UnresolvedInterfaceDeclaration,
)
Java::UnresolvedVariableDeclarationFragment_strategy = st.builds(
    Java::UnresolvedVariableDeclarationFragment,
)
Java::UnresolvedSingleVariableDeclaration_strategy = st.builds(
    Java::UnresolvedSingleVariableDeclaration,
)
Java::UnresolvedLabeledStatement_strategy = st.builds(
    Java::UnresolvedLabeledStatement,
)
Java::UnresolvedMethodDeclaration_strategy = st.builds(
    Java::UnresolvedMethodDeclaration,
)
Java::UnresolvedClassDeclaration_strategy = st.builds(
    Java::UnresolvedClassDeclaration,
)
AnnotationTypeDeclaration_strategy = st.builds(
    AnnotationTypeDeclaration,
)
Java::UnresolvedAnnotationDeclaration_strategy = st.builds(
    Java::UnresolvedAnnotationDeclaration,
)
AbstractTypeQualifiedExpression_strategy = st.builds(
    AbstractTypeQualifiedExpression,
)
Java::ThisExpression_strategy = st.builds(
    Java::ThisExpression,
)
Java::SuperFieldAccess_strategy = st.builds(
    Java::SuperFieldAccess,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
Java::PrimitiveTypeShort_strategy = st.builds(
    Java::PrimitiveTypeShort,
)
Java::PrimitiveTypeVoid_strategy = st.builds(
    Java::PrimitiveTypeVoid,
)
Java::PrimitiveTypeInt_strategy = st.builds(
    Java::PrimitiveTypeInt,
)
Java::PrimitiveTypeLong_strategy = st.builds(
    Java::PrimitiveTypeLong,
)
Java::PrimitiveTypeDouble_strategy = st.builds(
    Java::PrimitiveTypeDouble,
)
Java::PrimitiveTypeFloat_strategy = st.builds(
    Java::PrimitiveTypeFloat,
)
Java::PrimitiveTypeChar_strategy = st.builds(
    Java::PrimitiveTypeChar,
)
Java::PrimitiveTypeByte_strategy = st.builds(
    Java::PrimitiveTypeByte,
)
Java::PrimitiveTypeBoolean_strategy = st.builds(
    Java::PrimitiveTypeBoolean,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
Java::PackageAccess_strategy = st.builds(
    Java::PackageAccess,
)
Java::Model_strategy = st.builds(
    Java::Model,
    name=
        safe_text
)
Java::MethodDeclaration_strategy = st.builds(
    Java::MethodDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java::ManifestEntry_strategy = st.builds(
    Java::ManifestEntry,
    name=
        safe_text
)
Java::ManifestAttribute_strategy = st.builds(
    Java::ManifestAttribute,
    key=
        safe_text,
    value=
        safe_text
)
Java::InterfaceDeclaration_strategy = st.builds(
    Java::InterfaceDeclaration,
)
Java::ConstructorDeclaration_strategy = st.builds(
    Java::ConstructorDeclaration,
)
AbstractMethodInvocation_strategy = st.builds(
    AbstractMethodInvocation,
)
Java::SuperMethodInvocation_strategy = st.builds(
    Java::SuperMethodInvocation,
)
Comment_strategy = st.builds(
    Comment,
)
Java::LineComment_strategy = st.builds(
    Java::LineComment,
)
Java::Javadoc_strategy = st.builds(
    Java::Javadoc,
)
Java::BlockComment_strategy = st.builds(
    Java::BlockComment,
)
Java::VariableDeclarationFragment_strategy = st.builds(
    Java::VariableDeclarationFragment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
Java::UnresolvedTypeDeclaration_strategy = st.builds(
    Java::UnresolvedTypeDeclaration,
)
Java::TypeDeclaration_strategy = st.builds(
    Java::TypeDeclaration,
)
Java::EnumDeclaration_strategy = st.builds(
    Java::EnumDeclaration,
)
Java::AnnotationTypeDeclaration_strategy = st.builds(
    Java::AnnotationTypeDeclaration,
)
Java::ASTNode_strategy = st.builds(
    Java::ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
Java::CatchClause_strategy = st.builds(
    Java::CatchClause,
)
Java::VariableDeclarationStatement_strategy = st.builds(
    Java::VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
Java::EnhancedForStatement_strategy = st.builds(
    Java::EnhancedForStatement,
)
Java::DoStatement_strategy = st.builds(
    Java::DoStatement,
)
Java::ForStatement_strategy = st.builds(
    Java::ForStatement,
)
Java::BreakStatement_strategy = st.builds(
    Java::BreakStatement,
)
Java::EmptyStatement_strategy = st.builds(
    Java::EmptyStatement,
)
Java::ReturnStatement_strategy = st.builds(
    Java::ReturnStatement,
)
Java::TypeDeclarationStatement_strategy = st.builds(
    Java::TypeDeclarationStatement,
)
Java::ExpressionStatement_strategy = st.builds(
    Java::ExpressionStatement,
)
Java::ConstructorInvocation_strategy = st.builds(
    Java::ConstructorInvocation,
)
Java::TryStatement_strategy = st.builds(
    Java::TryStatement,
)
Java::ContinueStatement_strategy = st.builds(
    Java::ContinueStatement,
)
Java::WhileStatement_strategy = st.builds(
    Java::WhileStatement,
)
Java::IfStatement_strategy = st.builds(
    Java::IfStatement,
)
Java::SuperConstructorInvocation_strategy = st.builds(
    Java::SuperConstructorInvocation,
)
Java::SwitchStatement_strategy = st.builds(
    Java::SwitchStatement,
)
Java::ThrowStatement_strategy = st.builds(
    Java::ThrowStatement,
)
Java::SynchronizedStatement_strategy = st.builds(
    Java::SynchronizedStatement,
)
Java::SwitchCase_strategy = st.builds(
    Java::SwitchCase,
    default=
        st.booleans()
)
Java::AssertStatement_strategy = st.builds(
    Java::AssertStatement,
)
Java::Manifest_strategy = st.builds(
    Java::Manifest,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Java::UnresolvedItem_strategy = st.builds(
    Java::UnresolvedItem,
)
Java::VariableDeclaration_strategy = st.builds(
    Java::VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java::Type_strategy = st.builds(
    Java::Type,
)
Java::LabeledStatement_strategy = st.builds(
    Java::LabeledStatement,
)
Java::ClassFile_strategy = st.builds(
    Java::ClassFile,
    originalFilePath=
        safe_text
)
Java::CompilationUnit_strategy = st.builds(
    Java::CompilationUnit,
    originalFilePath=
        safe_text
)
Java::Archive_strategy = st.builds(
    Java::Archive,
    originalFilePath=
        safe_text
)
Java::AnnotationMemberValuePair_strategy = st.builds(
    Java::AnnotationMemberValuePair,
)
Java::SingleVariableDeclaration_strategy = st.builds(
    Java::SingleVariableDeclaration,
    varargs=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
Java::Assignment_strategy = st.builds(
    Java::Assignment,
    operator=
        safe_text
)
Java::CharacterLiteral_strategy = st.builds(
    Java::CharacterLiteral,
    escapedValue=
        safe_text
)
Java::MethodInvocation_strategy = st.builds(
    Java::MethodInvocation,
)
Java::VariableDeclarationExpression_strategy = st.builds(
    Java::VariableDeclarationExpression,
)
Java::ClassInstanceCreation_strategy = st.builds(
    Java::ClassInstanceCreation,
)
Java::ConditionalExpression_strategy = st.builds(
    Java::ConditionalExpression,
)
Java::PostfixExpression_strategy = st.builds(
    Java::PostfixExpression,
    operator=
        safe_text
)
Java::PrefixExpression_strategy = st.builds(
    Java::PrefixExpression,
    operator=
        safe_text
)
Java::FieldAccess_strategy = st.builds(
    Java::FieldAccess,
)
Java::NumberLiteral_strategy = st.builds(
    Java::NumberLiteral,
    tokenValue=
        safe_text
)
Java::BooleanLiteral_strategy = st.builds(
    Java::BooleanLiteral,
    value=
        st.booleans()
)
Java::ParenthesizedExpression_strategy = st.builds(
    Java::ParenthesizedExpression,
)
Java::TypeAccess_strategy = st.builds(
    Java::TypeAccess,
)
Java::InfixExpression_strategy = st.builds(
    Java::InfixExpression,
    operator=
        safe_text
)
Java::ArrayLengthAccess_strategy = st.builds(
    Java::ArrayLengthAccess,
)
Java::TypeLiteral_strategy = st.builds(
    Java::TypeLiteral,
)
Java::NullLiteral_strategy = st.builds(
    Java::NullLiteral,
)
Java::ArrayInitializer_strategy = st.builds(
    Java::ArrayInitializer,
)
Java::InstanceofExpression_strategy = st.builds(
    Java::InstanceofExpression,
)
Java::Annotation_strategy = st.builds(
    Java::Annotation,
)
Java::ArrayCreation_strategy = st.builds(
    Java::ArrayCreation,
)
Java::CastExpression_strategy = st.builds(
    Java::CastExpression,
)
Java::UnresolvedItemAccess_strategy = st.builds(
    Java::UnresolvedItemAccess,
)
Java::ArrayAccess_strategy = st.builds(
    Java::ArrayAccess,
)
Java::SingleVariableAccess_strategy = st.builds(
    Java::SingleVariableAccess,
)
Java::StringLiteral_strategy = st.builds(
    Java::StringLiteral,
    escapedValue=
        safe_text
)
Java::AbstractTypeQualifiedExpression_strategy = st.builds(
    Java::AbstractTypeQualifiedExpression,
)
Java::Package_strategy = st.builds(
    Java::Package,
)
Java::BodyDeclaration_strategy = st.builds(
    Java::BodyDeclaration,
)
Type_strategy = st.builds(
    Type,
)
Java::ArrayType_strategy = st.builds(
    Java::ArrayType,
    dimensions=
        st.integers()
)
Java::WildCardType_strategy = st.builds(
    Java::WildCardType,
    upperBound=
        st.booleans()
)
Java::ParameterizedType_strategy = st.builds(
    Java::ParameterizedType,
)
Java::TypeParameter_strategy = st.builds(
    Java::TypeParameter,
)
Java::PrimitiveType_strategy = st.builds(
    Java::PrimitiveType,
)
Java::UnresolvedType_strategy = st.builds(
    Java::UnresolvedType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
Java::MemberRef_strategy = st.builds(
    Java::MemberRef,
)
Java::TagElement_strategy = st.builds(
    Java::TagElement,
    tagName=
        safe_text
)
Java::AnonymousClassDeclaration_strategy = st.builds(
    Java::AnonymousClassDeclaration,
)
Java::ImportDeclaration_strategy = st.builds(
    Java::ImportDeclaration,
    static=
        st.booleans()
)
Java::AbstractVariablesContainer_strategy = st.builds(
    Java::AbstractVariablesContainer,
)
Java::Statement_strategy = st.builds(
    Java::Statement,
)
Java::MethodRef_strategy = st.builds(
    Java::MethodRef,
)
Java::Modifier_strategy = st.builds(
    Java::Modifier,
    strictfp=
        st.booleans(),
    visibility=
        safe_text,
    static=
        st.booleans(),
    native=
        st.booleans(),
    synchronized=
        st.booleans(),
    transient=
        st.booleans(),
    inheritance=
        safe_text,
    volatile=
        st.booleans()
)
Java::NamedElement_strategy = st.builds(
    Java::NamedElement,
    proxy=
        st.booleans(),
    name=
        safe_text
)
Java::MethodRefParameter_strategy = st.builds(
    Java::MethodRefParameter,
    name=
        safe_text,
    varargs=
        st.booleans()
)
Java::NamespaceAccess_strategy = st.builds(
    Java::NamespaceAccess,
)
Java::Comment_strategy = st.builds(
    Java::Comment,
    prefixOfParent=
        st.booleans(),
    enclosedByParent=
        st.booleans(),
    content=
        safe_text
)
Java::TextElement_strategy = st.builds(
    Java::TextElement,
    text=
        safe_text
)
Java::Expression_strategy = st.builds(
    Java::Expression,
)
Java::AbstractMethodInvocation_strategy = st.builds(
    Java::AbstractMethodInvocation,
)
Java::Block_strategy = st.builds(
    Java::Block,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
Java::AnnotationTypeMemberDeclaration_strategy = st.builds(
    Java::AnnotationTypeMemberDeclaration,
)
Java::AbstractTypeDeclaration_strategy = st.builds(
    Java::AbstractTypeDeclaration,
)
Java::EnumConstantDeclaration_strategy = st.builds(
    Java::EnumConstantDeclaration,
)
Java::Initializer_strategy = st.builds(
    Java::Initializer,
)
Java::FieldDeclaration_strategy = st.builds(
    Java::FieldDeclaration,
)
Java::AbstractMethodDeclaration_strategy = st.builds(
    Java::AbstractMethodDeclaration,
)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=Java::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::classdeclaration_instantiation(instance):
    assert isinstance(instance, Java::ClassDeclaration)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=MethodDeclaration_strategy)
@settings(max_examples=50)
def test_methoddeclaration_instantiation(instance):
    assert isinstance(instance, MethodDeclaration)

@given(instance=LabeledStatement_strategy)
@settings(max_examples=50)
def test_labeledstatement_instantiation(instance):
    assert isinstance(instance, LabeledStatement)

@given(instance=InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, InterfaceDeclaration)

@given(instance=EnumDeclaration_strategy)
@settings(max_examples=50)
def test_enumdeclaration_instantiation(instance):
    assert isinstance(instance, EnumDeclaration)

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)

@given(instance=ClassDeclaration_strategy)
@settings(max_examples=50)
def test_classdeclaration_instantiation(instance):
    assert isinstance(instance, ClassDeclaration)

@given(instance=AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeMemberDeclaration)

@given(instance=UnresolvedItem_strategy)
@settings(max_examples=50)
def test_unresolveditem_instantiation(instance):
    assert isinstance(instance, UnresolvedItem)

@given(instance=Java::UnresolvedAnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedannotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedAnnotationTypeMemberDeclaration)

@given(instance=Java::UnresolvedEnumDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedenumdeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedEnumDeclaration)

@given(instance=Java::UnresolvedInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedInterfaceDeclaration)

@given(instance=Java::UnresolvedVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java::unresolvedvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedVariableDeclarationFragment)

@given(instance=Java::UnresolvedSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedSingleVariableDeclaration)

@given(instance=Java::UnresolvedLabeledStatement_strategy)
@settings(max_examples=50)
def test_java::unresolvedlabeledstatement_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedLabeledStatement)

@given(instance=Java::UnresolvedMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedmethoddeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedMethodDeclaration)

@given(instance=Java::UnresolvedClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedclassdeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedClassDeclaration)

@given(instance=AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeDeclaration)

@given(instance=Java::UnresolvedAnnotationDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedannotationdeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedAnnotationDeclaration)

@given(instance=AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, AbstractTypeQualifiedExpression)

@given(instance=Java::ThisExpression_strategy)
@settings(max_examples=50)
def test_java::thisexpression_instantiation(instance):
    assert isinstance(instance, Java::ThisExpression)

@given(instance=Java::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java::superfieldaccess_instantiation(instance):
    assert isinstance(instance, Java::SuperFieldAccess)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=Java::PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java::primitivetypeshort_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeShort)

@given(instance=Java::PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java::primitivetypevoid_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeVoid)

@given(instance=Java::PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java::primitivetypeint_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeInt)

@given(instance=Java::PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java::primitivetypelong_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeLong)

@given(instance=Java::PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java::primitivetypedouble_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeDouble)

@given(instance=Java::PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java::primitivetypefloat_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeFloat)

@given(instance=Java::PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java::primitivetypechar_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeChar)

@given(instance=Java::PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java::primitivetypebyte_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeByte)

@given(instance=Java::PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java::primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveTypeBoolean)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=Java::PackageAccess_strategy)
@settings(max_examples=50)
def test_java::packageaccess_instantiation(instance):
    assert isinstance(instance, Java::PackageAccess)

@given(instance=Java::Model_strategy)
@settings(max_examples=50)
def test_java::model_instantiation(instance):
    assert isinstance(instance, Java::Model)

@given(instance=Java::Model_strategy)
def test_java::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::Model_strategy)
def test_java::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java::methoddeclaration_instantiation(instance):
    assert isinstance(instance, Java::MethodDeclaration)

@given(instance=Java::MethodDeclaration_strategy)
def test_java::methoddeclaration_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=Java::MethodDeclaration_strategy)
def test_java::methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java::ManifestEntry_strategy)
@settings(max_examples=50)
def test_java::manifestentry_instantiation(instance):
    assert isinstance(instance, Java::ManifestEntry)

@given(instance=Java::ManifestEntry_strategy)
def test_java::manifestentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::ManifestEntry_strategy)
def test_java::manifestentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java::ManifestAttribute_strategy)
@settings(max_examples=50)
def test_java::manifestattribute_instantiation(instance):
    assert isinstance(instance, Java::ManifestAttribute)

@given(instance=Java::ManifestAttribute_strategy)
def test_java::manifestattribute_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=Java::ManifestAttribute_strategy)
def test_java::manifestattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=Java::ManifestAttribute_strategy)
def test_java::manifestattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Java::ManifestAttribute_strategy)
def test_java::manifestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, Java::InterfaceDeclaration)

@given(instance=Java::ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_java::constructordeclaration_instantiation(instance):
    assert isinstance(instance, Java::ConstructorDeclaration)

@given(instance=AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, AbstractMethodInvocation)

@given(instance=Java::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, Java::SuperMethodInvocation)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Java::LineComment_strategy)
@settings(max_examples=50)
def test_java::linecomment_instantiation(instance):
    assert isinstance(instance, Java::LineComment)

@given(instance=Java::Javadoc_strategy)
@settings(max_examples=50)
def test_java::javadoc_instantiation(instance):
    assert isinstance(instance, Java::Javadoc)

@given(instance=Java::BlockComment_strategy)
@settings(max_examples=50)
def test_java::blockcomment_instantiation(instance):
    assert isinstance(instance, Java::BlockComment)

@given(instance=Java::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Java::VariableDeclarationFragment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=Java::UnresolvedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedtypedeclaration_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedTypeDeclaration)

@given(instance=Java::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::typedeclaration_instantiation(instance):
    assert isinstance(instance, Java::TypeDeclaration)

@given(instance=Java::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java::enumdeclaration_instantiation(instance):
    assert isinstance(instance, Java::EnumDeclaration)

@given(instance=Java::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, Java::AnnotationTypeDeclaration)

@given(instance=Java::ASTNode_strategy)
@settings(max_examples=50)
def test_java::astnode_instantiation(instance):
    assert isinstance(instance, Java::ASTNode)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Java::CatchClause_strategy)
@settings(max_examples=50)
def test_java::catchclause_instantiation(instance):
    assert isinstance(instance, Java::CatchClause)

@given(instance=Java::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java::VariableDeclarationStatement)

@given(instance=Java::VariableDeclarationStatement_strategy)
def test_java::variabledeclarationstatement_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=Java::VariableDeclarationStatement_strategy)
def test_java::variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, Java::EnhancedForStatement)

@given(instance=Java::DoStatement_strategy)
@settings(max_examples=50)
def test_java::dostatement_instantiation(instance):
    assert isinstance(instance, Java::DoStatement)

@given(instance=Java::ForStatement_strategy)
@settings(max_examples=50)
def test_java::forstatement_instantiation(instance):
    assert isinstance(instance, Java::ForStatement)

@given(instance=Java::BreakStatement_strategy)
@settings(max_examples=50)
def test_java::breakstatement_instantiation(instance):
    assert isinstance(instance, Java::BreakStatement)

@given(instance=Java::EmptyStatement_strategy)
@settings(max_examples=50)
def test_java::emptystatement_instantiation(instance):
    assert isinstance(instance, Java::EmptyStatement)

@given(instance=Java::ReturnStatement_strategy)
@settings(max_examples=50)
def test_java::returnstatement_instantiation(instance):
    assert isinstance(instance, Java::ReturnStatement)

@given(instance=Java::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java::TypeDeclarationStatement)

@given(instance=Java::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java::expressionstatement_instantiation(instance):
    assert isinstance(instance, Java::ExpressionStatement)

@given(instance=Java::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java::constructorinvocation_instantiation(instance):
    assert isinstance(instance, Java::ConstructorInvocation)

@given(instance=Java::TryStatement_strategy)
@settings(max_examples=50)
def test_java::trystatement_instantiation(instance):
    assert isinstance(instance, Java::TryStatement)

@given(instance=Java::ContinueStatement_strategy)
@settings(max_examples=50)
def test_java::continuestatement_instantiation(instance):
    assert isinstance(instance, Java::ContinueStatement)

@given(instance=Java::WhileStatement_strategy)
@settings(max_examples=50)
def test_java::whilestatement_instantiation(instance):
    assert isinstance(instance, Java::WhileStatement)

@given(instance=Java::IfStatement_strategy)
@settings(max_examples=50)
def test_java::ifstatement_instantiation(instance):
    assert isinstance(instance, Java::IfStatement)

@given(instance=Java::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, Java::SuperConstructorInvocation)

@given(instance=Java::SwitchStatement_strategy)
@settings(max_examples=50)
def test_java::switchstatement_instantiation(instance):
    assert isinstance(instance, Java::SwitchStatement)

@given(instance=Java::ThrowStatement_strategy)
@settings(max_examples=50)
def test_java::throwstatement_instantiation(instance):
    assert isinstance(instance, Java::ThrowStatement)

@given(instance=Java::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, Java::SynchronizedStatement)

@given(instance=Java::SwitchCase_strategy)
@settings(max_examples=50)
def test_java::switchcase_instantiation(instance):
    assert isinstance(instance, Java::SwitchCase)

@given(instance=Java::SwitchCase_strategy)
def test_java::switchcase_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=Java::SwitchCase_strategy)
def test_java::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Java::AssertStatement_strategy)
@settings(max_examples=50)
def test_java::assertstatement_instantiation(instance):
    assert isinstance(instance, Java::AssertStatement)

@given(instance=Java::Manifest_strategy)
@settings(max_examples=50)
def test_java::manifest_instantiation(instance):
    assert isinstance(instance, Java::Manifest)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Java::UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java::unresolveditem_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedItem)

@given(instance=Java::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::variabledeclaration_instantiation(instance):
    assert isinstance(instance, Java::VariableDeclaration)

@given(instance=Java::VariableDeclaration_strategy)
def test_java::variabledeclaration_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=Java::VariableDeclaration_strategy)
def test_java::variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java::Type_strategy)
@settings(max_examples=50)
def test_java::type_instantiation(instance):
    assert isinstance(instance, Java::Type)

@given(instance=Java::LabeledStatement_strategy)
@settings(max_examples=50)
def test_java::labeledstatement_instantiation(instance):
    assert isinstance(instance, Java::LabeledStatement)

@given(instance=Java::ClassFile_strategy)
@settings(max_examples=50)
def test_java::classfile_instantiation(instance):
    assert isinstance(instance, Java::ClassFile)

@given(instance=Java::ClassFile_strategy)
def test_java::classfile_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=Java::ClassFile_strategy)
def test_java::classfile_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java::CompilationUnit_strategy)
@settings(max_examples=50)
def test_java::compilationunit_instantiation(instance):
    assert isinstance(instance, Java::CompilationUnit)

@given(instance=Java::CompilationUnit_strategy)
def test_java::compilationunit_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=Java::CompilationUnit_strategy)
def test_java::compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java::Archive_strategy)
@settings(max_examples=50)
def test_java::archive_instantiation(instance):
    assert isinstance(instance, Java::Archive)

@given(instance=Java::Archive_strategy)
def test_java::archive_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=Java::Archive_strategy)
def test_java::archive_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java::AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java::annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, Java::AnnotationMemberValuePair)

@given(instance=Java::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Java::SingleVariableDeclaration)

@given(instance=Java::SingleVariableDeclaration_strategy)
def test_java::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=Java::SingleVariableDeclaration_strategy)
def test_java::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Java::Assignment_strategy)
@settings(max_examples=50)
def test_java::assignment_instantiation(instance):
    assert isinstance(instance, Java::Assignment)

@given(instance=Java::Assignment_strategy)
def test_java::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java::Assignment_strategy)
def test_java::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java::characterliteral_instantiation(instance):
    assert isinstance(instance, Java::CharacterLiteral)

@given(instance=Java::CharacterLiteral_strategy)
def test_java::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=Java::CharacterLiteral_strategy)
def test_java::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java::MethodInvocation_strategy)
@settings(max_examples=50)
def test_java::methodinvocation_instantiation(instance):
    assert isinstance(instance, Java::MethodInvocation)

@given(instance=Java::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, Java::VariableDeclarationExpression)

@given(instance=Java::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java::classinstancecreation_instantiation(instance):
    assert isinstance(instance, Java::ClassInstanceCreation)

@given(instance=Java::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java::conditionalexpression_instantiation(instance):
    assert isinstance(instance, Java::ConditionalExpression)

@given(instance=Java::PostfixExpression_strategy)
@settings(max_examples=50)
def test_java::postfixexpression_instantiation(instance):
    assert isinstance(instance, Java::PostfixExpression)

@given(instance=Java::PostfixExpression_strategy)
def test_java::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java::PostfixExpression_strategy)
def test_java::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java::PrefixExpression_strategy)
@settings(max_examples=50)
def test_java::prefixexpression_instantiation(instance):
    assert isinstance(instance, Java::PrefixExpression)

@given(instance=Java::PrefixExpression_strategy)
def test_java::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java::PrefixExpression_strategy)
def test_java::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java::FieldAccess_strategy)
@settings(max_examples=50)
def test_java::fieldaccess_instantiation(instance):
    assert isinstance(instance, Java::FieldAccess)

@given(instance=Java::NumberLiteral_strategy)
@settings(max_examples=50)
def test_java::numberliteral_instantiation(instance):
    assert isinstance(instance, Java::NumberLiteral)

@given(instance=Java::NumberLiteral_strategy)
def test_java::numberliteral_tokenValue_type(instance):
    assert isinstance(instance.tokenValue, str)


@given(instance=Java::NumberLiteral_strategy)
def test_java::numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=Java::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java::booleanliteral_instantiation(instance):
    assert isinstance(instance, Java::BooleanLiteral)

@given(instance=Java::BooleanLiteral_strategy)
def test_java::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=Java::BooleanLiteral_strategy)
def test_java::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, Java::ParenthesizedExpression)

@given(instance=Java::TypeAccess_strategy)
@settings(max_examples=50)
def test_java::typeaccess_instantiation(instance):
    assert isinstance(instance, Java::TypeAccess)

@given(instance=Java::InfixExpression_strategy)
@settings(max_examples=50)
def test_java::infixexpression_instantiation(instance):
    assert isinstance(instance, Java::InfixExpression)

@given(instance=Java::InfixExpression_strategy)
def test_java::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Java::InfixExpression_strategy)
def test_java::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java::ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java::arraylengthaccess_instantiation(instance):
    assert isinstance(instance, Java::ArrayLengthAccess)

@given(instance=Java::TypeLiteral_strategy)
@settings(max_examples=50)
def test_java::typeliteral_instantiation(instance):
    assert isinstance(instance, Java::TypeLiteral)

@given(instance=Java::NullLiteral_strategy)
@settings(max_examples=50)
def test_java::nullliteral_instantiation(instance):
    assert isinstance(instance, Java::NullLiteral)

@given(instance=Java::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java::arrayinitializer_instantiation(instance):
    assert isinstance(instance, Java::ArrayInitializer)

@given(instance=Java::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java::instanceofexpression_instantiation(instance):
    assert isinstance(instance, Java::InstanceofExpression)

@given(instance=Java::Annotation_strategy)
@settings(max_examples=50)
def test_java::annotation_instantiation(instance):
    assert isinstance(instance, Java::Annotation)

@given(instance=Java::ArrayCreation_strategy)
@settings(max_examples=50)
def test_java::arraycreation_instantiation(instance):
    assert isinstance(instance, Java::ArrayCreation)

@given(instance=Java::CastExpression_strategy)
@settings(max_examples=50)
def test_java::castexpression_instantiation(instance):
    assert isinstance(instance, Java::CastExpression)

@given(instance=Java::UnresolvedItemAccess_strategy)
@settings(max_examples=50)
def test_java::unresolveditemaccess_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedItemAccess)

@given(instance=Java::ArrayAccess_strategy)
@settings(max_examples=50)
def test_java::arrayaccess_instantiation(instance):
    assert isinstance(instance, Java::ArrayAccess)

@given(instance=Java::SingleVariableAccess_strategy)
@settings(max_examples=50)
def test_java::singlevariableaccess_instantiation(instance):
    assert isinstance(instance, Java::SingleVariableAccess)

@given(instance=Java::StringLiteral_strategy)
@settings(max_examples=50)
def test_java::stringliteral_instantiation(instance):
    assert isinstance(instance, Java::StringLiteral)

@given(instance=Java::StringLiteral_strategy)
def test_java::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=Java::StringLiteral_strategy)
def test_java::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java::AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_java::abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, Java::AbstractTypeQualifiedExpression)

@given(instance=Java::Package_strategy)
@settings(max_examples=50)
def test_java::package_instantiation(instance):
    assert isinstance(instance, Java::Package)

@given(instance=Java::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java::bodydeclaration_instantiation(instance):
    assert isinstance(instance, Java::BodyDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Java::ArrayType_strategy)
@settings(max_examples=50)
def test_java::arraytype_instantiation(instance):
    assert isinstance(instance, Java::ArrayType)

@given(instance=Java::ArrayType_strategy)
def test_java::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, int)


@given(instance=Java::ArrayType_strategy)
def test_java::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=Java::WildCardType_strategy)
@settings(max_examples=50)
def test_java::wildcardtype_instantiation(instance):
    assert isinstance(instance, Java::WildCardType)

@given(instance=Java::WildCardType_strategy)
def test_java::wildcardtype_upperBound_type(instance):
    assert isinstance(instance.upperBound, bool)


@given(instance=Java::WildCardType_strategy)
def test_java::wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=Java::ParameterizedType_strategy)
@settings(max_examples=50)
def test_java::parameterizedtype_instantiation(instance):
    assert isinstance(instance, Java::ParameterizedType)

@given(instance=Java::TypeParameter_strategy)
@settings(max_examples=50)
def test_java::typeparameter_instantiation(instance):
    assert isinstance(instance, Java::TypeParameter)

@given(instance=Java::PrimitiveType_strategy)
@settings(max_examples=50)
def test_java::primitivetype_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveType)

@given(instance=Java::UnresolvedType_strategy)
@settings(max_examples=50)
def test_java::unresolvedtype_instantiation(instance):
    assert isinstance(instance, Java::UnresolvedType)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=Java::MemberRef_strategy)
@settings(max_examples=50)
def test_java::memberref_instantiation(instance):
    assert isinstance(instance, Java::MemberRef)

@given(instance=Java::TagElement_strategy)
@settings(max_examples=50)
def test_java::tagelement_instantiation(instance):
    assert isinstance(instance, Java::TagElement)

@given(instance=Java::TagElement_strategy)
def test_java::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=Java::TagElement_strategy)
def test_java::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=Java::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, Java::AnonymousClassDeclaration)

@given(instance=Java::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java::importdeclaration_instantiation(instance):
    assert isinstance(instance, Java::ImportDeclaration)

@given(instance=Java::ImportDeclaration_strategy)
def test_java::importdeclaration_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=Java::ImportDeclaration_strategy)
def test_java::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java::AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_java::abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, Java::AbstractVariablesContainer)

@given(instance=Java::Statement_strategy)
@settings(max_examples=50)
def test_java::statement_instantiation(instance):
    assert isinstance(instance, Java::Statement)

@given(instance=Java::MethodRef_strategy)
@settings(max_examples=50)
def test_java::methodref_instantiation(instance):
    assert isinstance(instance, Java::MethodRef)

@given(instance=Java::Modifier_strategy)
@settings(max_examples=50)
def test_java::modifier_instantiation(instance):
    assert isinstance(instance, Java::Modifier)

@given(instance=Java::Modifier_strategy)
def test_java::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, bool)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_native_type(instance):
    assert isinstance(instance.native, bool)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_inheritance_type(instance):
    assert isinstance(instance.inheritance, str)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=Java::Modifier_strategy)
def test_java::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, bool)


@given(instance=Java::Modifier_strategy)
def test_java::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=Java::NamedElement_strategy)
@settings(max_examples=50)
def test_java::namedelement_instantiation(instance):
    assert isinstance(instance, Java::NamedElement)

@given(instance=Java::NamedElement_strategy)
def test_java::namedelement_proxy_type(instance):
    assert isinstance(instance.proxy, bool)


@given(instance=Java::NamedElement_strategy)
def test_java::namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=Java::NamedElement_strategy)
def test_java::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::NamedElement_strategy)
def test_java::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java::methodrefparameter_instantiation(instance):
    assert isinstance(instance, Java::MethodRefParameter)

@given(instance=Java::MethodRefParameter_strategy)
def test_java::methodrefparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::MethodRefParameter_strategy)
def test_java::methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java::MethodRefParameter_strategy)
def test_java::methodrefparameter_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=Java::MethodRefParameter_strategy)
def test_java::methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=Java::NamespaceAccess_strategy)
@settings(max_examples=50)
def test_java::namespaceaccess_instantiation(instance):
    assert isinstance(instance, Java::NamespaceAccess)

@given(instance=Java::Comment_strategy)
@settings(max_examples=50)
def test_java::comment_instantiation(instance):
    assert isinstance(instance, Java::Comment)

@given(instance=Java::Comment_strategy)
def test_java::comment_prefixOfParent_type(instance):
    assert isinstance(instance.prefixOfParent, bool)


@given(instance=Java::Comment_strategy)
def test_java::comment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original

@given(instance=Java::Comment_strategy)
def test_java::comment_enclosedByParent_type(instance):
    assert isinstance(instance.enclosedByParent, bool)


@given(instance=Java::Comment_strategy)
def test_java::comment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original

@given(instance=Java::Comment_strategy)
def test_java::comment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=Java::Comment_strategy)
def test_java::comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=Java::TextElement_strategy)
@settings(max_examples=50)
def test_java::textelement_instantiation(instance):
    assert isinstance(instance, Java::TextElement)

@given(instance=Java::TextElement_strategy)
def test_java::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=Java::TextElement_strategy)
def test_java::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Java::Expression_strategy)
@settings(max_examples=50)
def test_java::expression_instantiation(instance):
    assert isinstance(instance, Java::Expression)

@given(instance=Java::AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_java::abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, Java::AbstractMethodInvocation)

@given(instance=Java::Block_strategy)
@settings(max_examples=50)
def test_java::block_instantiation(instance):
    assert isinstance(instance, Java::Block)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=Java::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, Java::AnnotationTypeMemberDeclaration)

@given(instance=Java::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, Java::AbstractTypeDeclaration)

@given(instance=Java::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, Java::EnumConstantDeclaration)

@given(instance=Java::Initializer_strategy)
@settings(max_examples=50)
def test_java::initializer_instantiation(instance):
    assert isinstance(instance, Java::Initializer)

@given(instance=Java::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java::fielddeclaration_instantiation(instance):
    assert isinstance(instance, Java::FieldDeclaration)

@given(instance=Java::AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java::abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, Java::AbstractMethodDeclaration)
