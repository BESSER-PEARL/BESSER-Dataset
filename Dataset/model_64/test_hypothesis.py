import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SingleVariableDeclaration,
    MethodDeclaration,
    LabeledStatement,
    InterfaceDeclaration,
    VariableDeclarationFragment,
    EnumDeclaration,
    ClassDeclaration,
    AnnotationTypeMemberDeclaration,
    UnresolvedItem,
    java::UnresolvedClassDeclaration,
    java::UnresolvedVariableDeclarationFragment,
    java::UnresolvedLabeledStatement,
    java::UnresolvedEnumDeclaration,
    java::UnresolvedMethodDeclaration,
    java::UnresolvedAnnotationTypeMemberDeclaration,
    java::UnresolvedInterfaceDeclaration,
    java::UnresolvedSingleVariableDeclaration,
    AnnotationTypeDeclaration,
    java::UnresolvedAnnotationDeclaration,
    AbstractTypeQualifiedExpression,
    java::ThisExpression,
    java::SuperFieldAccess,
    PrimitiveType,
    java::PrimitiveTypeDouble,
    java::PrimitiveTypeFloat,
    java::PrimitiveTypeLong,
    java::PrimitiveTypeInt,
    java::PrimitiveTypeByte,
    java::PrimitiveTypeVoid,
    java::PrimitiveTypeChar,
    java::PrimitiveTypeShort,
    java::PrimitiveTypeBoolean,
    NamespaceAccess,
    java::PackageAccess,
    java::Model,
    java::ManifestEntry,
    java::ManifestAttribute,
    AbstractVariablesContainer,
    VariableDeclaration,
    TypeDeclaration,
    java::InterfaceDeclaration,
    java::ClassDeclaration,
    AbstractMethodDeclaration,
    java::ConstructorDeclaration,
    java::MethodDeclaration,
    AbstractMethodInvocation,
    java::SuperMethodInvocation,
    Comment,
    java::LineComment,
    java::Javadoc,
    java::BlockComment,
    java::ASTNode,
    AbstractTypeDeclaration,
    java::UnresolvedTypeDeclaration,
    java::EnumDeclaration,
    java::TypeDeclaration,
    java::AnnotationTypeDeclaration,
    Statement,
    java::DoStatement,
    java::EnhancedForStatement,
    java::ExpressionStatement,
    java::SynchronizedStatement,
    java::TryStatement,
    java::SuperConstructorInvocation,
    java::BreakStatement,
    java::WhileStatement,
    java::ThrowStatement,
    java::ContinueStatement,
    java::SwitchStatement,
    java::VariableDeclarationStatement,
    java::EmptyStatement,
    java::ForStatement,
    java::SwitchCase,
    java::TypeDeclarationStatement,
    java::IfStatement,
    java::ConstructorInvocation,
    java::ReturnStatement,
    java::CatchClause,
    java::AssertStatement,
    java::Manifest,
    NamedElement,
    java::ClassFile,
    java::CompilationUnit,
    java::VariableDeclaration,
    java::BodyDeclaration,
    java::Type,
    java::UnresolvedItem,
    java::LabeledStatement,
    java::Archive,
    java::AnnotationMemberValuePair,
    java::VariableDeclarationFragment,
    Expression,
    java::CharacterLiteral,
    java::ConditionalExpression,
    java::NumberLiteral,
    java::CastExpression,
    java::Annotation,
    java::ArrayLengthAccess,
    java::PostfixExpression,
    java::PrefixExpression,
    java::ArrayCreation,
    java::ArrayAccess,
    java::StringLiteral,
    java::Assignment,
    java::InstanceofExpression,
    java::NullLiteral,
    java::UnresolvedItemAccess,
    java::SingleVariableAccess,
    java::ParenthesizedExpression,
    java::TypeLiteral,
    java::MethodInvocation,
    java::ClassInstanceCreation,
    java::ArrayInitializer,
    java::InfixExpression,
    java::BooleanLiteral,
    java::FieldAccess,
    java::VariableDeclarationExpression,
    java::AbstractTypeQualifiedExpression,
    java::Package,
    Type,
    java::ArrayType,
    java::ParameterizedType,
    java::PrimitiveType,
    java::WildCardType,
    java::UnresolvedType,
    ASTNode,
    java::Statement,
    java::TagElement,
    java::Modifier,
    java::NamespaceAccess,
    java::Comment,
    java::Expression,
    java::AnonymousClassDeclaration,
    java::TextElement,
    java::MemberRef,
    java::MethodRefParameter,
    java::ImportDeclaration,
    java::AbstractVariablesContainer,
    java::NamedElement,
    java::AbstractMethodInvocation,
    java::MethodRef,
    java::TypeParameter,
    java::TypeAccess,
    java::SingleVariableDeclaration,
    java::Block,
    BodyDeclaration,
    java::AbstractTypeDeclaration,
    java::FieldDeclaration,
    java::Initializer,
    java::EnumConstantDeclaration,
    java::AnnotationTypeMemberDeclaration,
    java::AbstractMethodDeclaration,
    AssignmentKind,
    InfixExpressionKind,
    PostfixExpressionKind,
    PrefixExpressionKind,
    InheritanceKind,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
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



def test_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationFragment)


def test_variabledeclarationfragment_constructor_exists():
    assert callable(VariableDeclarationFragment.__init__)


def test_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumDeclaration)


def test_enumdeclaration_constructor_exists():
    assert callable(EnumDeclaration.__init__)


def test_enumdeclaration_constructor_args():
    sig = inspect.signature(EnumDeclaration.__init__)
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



def test_java::unresolvedclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedClassDeclaration)


def test_java::unresolvedclassdeclaration_constructor_exists():
    assert callable(java::UnresolvedClassDeclaration.__init__)


def test_java::unresolvedclassdeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedVariableDeclarationFragment)


def test_java::unresolvedvariabledeclarationfragment_constructor_exists():
    assert callable(java::UnresolvedVariableDeclarationFragment.__init__)


def test_java::unresolvedvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(java::UnresolvedVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedlabeledstatement_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedLabeledStatement)


def test_java::unresolvedlabeledstatement_constructor_exists():
    assert callable(java::UnresolvedLabeledStatement.__init__)


def test_java::unresolvedlabeledstatement_constructor_args():
    sig = inspect.signature(java::UnresolvedLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedenumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedEnumDeclaration)


def test_java::unresolvedenumdeclaration_constructor_exists():
    assert callable(java::UnresolvedEnumDeclaration.__init__)


def test_java::unresolvedenumdeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedEnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedMethodDeclaration)


def test_java::unresolvedmethoddeclaration_constructor_exists():
    assert callable(java::UnresolvedMethodDeclaration.__init__)


def test_java::unresolvedmethoddeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedannotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedAnnotationTypeMemberDeclaration)


def test_java::unresolvedannotationtypememberdeclaration_constructor_exists():
    assert callable(java::UnresolvedAnnotationTypeMemberDeclaration.__init__)


def test_java::unresolvedannotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedAnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedInterfaceDeclaration)


def test_java::unresolvedinterfacedeclaration_constructor_exists():
    assert callable(java::UnresolvedInterfaceDeclaration.__init__)


def test_java::unresolvedinterfacedeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedSingleVariableDeclaration)


def test_java::unresolvedsinglevariabledeclaration_constructor_exists():
    assert callable(java::UnresolvedSingleVariableDeclaration.__init__)


def test_java::unresolvedsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AnnotationTypeDeclaration)


def test_annotationtypedeclaration_constructor_exists():
    assert callable(AnnotationTypeDeclaration.__init__)


def test_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedannotationdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedAnnotationDeclaration)


def test_java::unresolvedannotationdeclaration_constructor_exists():
    assert callable(java::UnresolvedAnnotationDeclaration.__init__)


def test_java::unresolvedannotationdeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedAnnotationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeQualifiedExpression)


def test_abstracttypequalifiedexpression_constructor_exists():
    assert callable(AbstractTypeQualifiedExpression.__init__)


def test_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::thisexpression_is_not_abstract():
    assert not inspect.isabstract(java::ThisExpression)


def test_java::thisexpression_constructor_exists():
    assert callable(java::ThisExpression.__init__)


def test_java::thisexpression_constructor_args():
    sig = inspect.signature(java::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(java::SuperFieldAccess)


def test_java::superfieldaccess_constructor_exists():
    assert callable(java::SuperFieldAccess.__init__)


def test_java::superfieldaccess_constructor_args():
    sig = inspect.signature(java::SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeDouble)


def test_java::primitivetypedouble_constructor_exists():
    assert callable(java::PrimitiveTypeDouble.__init__)


def test_java::primitivetypedouble_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeFloat)


def test_java::primitivetypefloat_constructor_exists():
    assert callable(java::PrimitiveTypeFloat.__init__)


def test_java::primitivetypefloat_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeLong)


def test_java::primitivetypelong_constructor_exists():
    assert callable(java::PrimitiveTypeLong.__init__)


def test_java::primitivetypelong_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeInt)


def test_java::primitivetypeint_constructor_exists():
    assert callable(java::PrimitiveTypeInt.__init__)


def test_java::primitivetypeint_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeByte)


def test_java::primitivetypebyte_constructor_exists():
    assert callable(java::PrimitiveTypeByte.__init__)


def test_java::primitivetypebyte_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeVoid)


def test_java::primitivetypevoid_constructor_exists():
    assert callable(java::PrimitiveTypeVoid.__init__)


def test_java::primitivetypevoid_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeChar)


def test_java::primitivetypechar_constructor_exists():
    assert callable(java::PrimitiveTypeChar.__init__)


def test_java::primitivetypechar_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeShort)


def test_java::primitivetypeshort_constructor_exists():
    assert callable(java::PrimitiveTypeShort.__init__)


def test_java::primitivetypeshort_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveTypeBoolean)


def test_java::primitivetypeboolean_constructor_exists():
    assert callable(java::PrimitiveTypeBoolean.__init__)


def test_java::primitivetypeboolean_constructor_args():
    sig = inspect.signature(java::PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::packageaccess_is_not_abstract():
    assert not inspect.isabstract(java::PackageAccess)


def test_java::packageaccess_constructor_exists():
    assert callable(java::PackageAccess.__init__)


def test_java::packageaccess_constructor_args():
    sig = inspect.signature(java::PackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::model_is_not_abstract():
    assert not inspect.isabstract(java::Model)


def test_java::model_constructor_exists():
    assert callable(java::Model.__init__)


def test_java::model_constructor_args():
    sig = inspect.signature(java::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::model_has_name():
    assert hasattr(java::Model, "name")
    descriptor = None
    for klass in java::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::manifestentry_is_not_abstract():
    assert not inspect.isabstract(java::ManifestEntry)


def test_java::manifestentry_constructor_exists():
    assert callable(java::ManifestEntry.__init__)


def test_java::manifestentry_constructor_args():
    sig = inspect.signature(java::ManifestEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::manifestentry_has_name():
    assert hasattr(java::ManifestEntry, "name")
    descriptor = None
    for klass in java::ManifestEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::manifestattribute_is_not_abstract():
    assert not inspect.isabstract(java::ManifestAttribute)


def test_java::manifestattribute_constructor_exists():
    assert callable(java::ManifestAttribute.__init__)


def test_java::manifestattribute_constructor_args():
    sig = inspect.signature(java::ManifestAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_java::manifestattribute_has_value():
    assert hasattr(java::ManifestAttribute, "value")
    descriptor = None
    for klass in java::ManifestAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_java::manifestattribute_has_key():
    assert hasattr(java::ManifestAttribute, "key")
    descriptor = None
    for klass in java::ManifestAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractVariablesContainer)


def test_abstractvariablescontainer_constructor_exists():
    assert callable(AbstractVariablesContainer.__init__)


def test_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java::InterfaceDeclaration)


def test_java::interfacedeclaration_constructor_exists():
    assert callable(java::InterfaceDeclaration.__init__)


def test_java::interfacedeclaration_constructor_args():
    sig = inspect.signature(java::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::ClassDeclaration)


def test_java::classdeclaration_constructor_exists():
    assert callable(java::ClassDeclaration.__init__)


def test_java::classdeclaration_constructor_args():
    sig = inspect.signature(java::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(java::ConstructorDeclaration)


def test_java::constructordeclaration_constructor_exists():
    assert callable(java::ConstructorDeclaration.__init__)


def test_java::constructordeclaration_constructor_args():
    sig = inspect.signature(java::ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java::MethodDeclaration)


def test_java::methoddeclaration_constructor_exists():
    assert callable(java::MethodDeclaration.__init__)


def test_java::methoddeclaration_constructor_args():
    sig = inspect.signature(java::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java::methoddeclaration_has_extraArrayDimensions():
    assert hasattr(java::MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in java::MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodInvocation)


def test_abstractmethodinvocation_constructor_exists():
    assert callable(AbstractMethodInvocation.__init__)


def test_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java::SuperMethodInvocation)


def test_java::supermethodinvocation_constructor_exists():
    assert callable(java::SuperMethodInvocation.__init__)


def test_java::supermethodinvocation_constructor_args():
    sig = inspect.signature(java::SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_java::linecomment_is_not_abstract():
    assert not inspect.isabstract(java::LineComment)


def test_java::linecomment_constructor_exists():
    assert callable(java::LineComment.__init__)


def test_java::linecomment_constructor_args():
    sig = inspect.signature(java::LineComment.__init__)
    params = list(sig.parameters.keys())



def test_java::javadoc_is_not_abstract():
    assert not inspect.isabstract(java::Javadoc)


def test_java::javadoc_constructor_exists():
    assert callable(java::Javadoc.__init__)


def test_java::javadoc_constructor_args():
    sig = inspect.signature(java::Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_java::blockcomment_is_not_abstract():
    assert not inspect.isabstract(java::BlockComment)


def test_java::blockcomment_constructor_exists():
    assert callable(java::BlockComment.__init__)


def test_java::blockcomment_constructor_args():
    sig = inspect.signature(java::BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_java::astnode_is_not_abstract():
    assert not inspect.isabstract(java::ASTNode)


def test_java::astnode_constructor_exists():
    assert callable(java::ASTNode.__init__)


def test_java::astnode_constructor_args():
    sig = inspect.signature(java::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolvedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedTypeDeclaration)


def test_java::unresolvedtypedeclaration_constructor_exists():
    assert callable(java::UnresolvedTypeDeclaration.__init__)


def test_java::unresolvedtypedeclaration_constructor_args():
    sig = inspect.signature(java::UnresolvedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::EnumDeclaration)


def test_java::enumdeclaration_constructor_exists():
    assert callable(java::EnumDeclaration.__init__)


def test_java::enumdeclaration_constructor_args():
    sig = inspect.signature(java::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(java::TypeDeclaration)


def test_java::typedeclaration_constructor_exists():
    assert callable(java::TypeDeclaration.__init__)


def test_java::typedeclaration_constructor_args():
    sig = inspect.signature(java::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationTypeDeclaration)


def test_java::annotationtypedeclaration_constructor_exists():
    assert callable(java::AnnotationTypeDeclaration.__init__)


def test_java::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(java::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::dostatement_is_not_abstract():
    assert not inspect.isabstract(java::DoStatement)


def test_java::dostatement_constructor_exists():
    assert callable(java::DoStatement.__init__)


def test_java::dostatement_constructor_args():
    sig = inspect.signature(java::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(java::EnhancedForStatement)


def test_java::enhancedforstatement_constructor_exists():
    assert callable(java::EnhancedForStatement.__init__)


def test_java::enhancedforstatement_constructor_args():
    sig = inspect.signature(java::EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(java::ExpressionStatement)


def test_java::expressionstatement_constructor_exists():
    assert callable(java::ExpressionStatement.__init__)


def test_java::expressionstatement_constructor_args():
    sig = inspect.signature(java::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(java::SynchronizedStatement)


def test_java::synchronizedstatement_constructor_exists():
    assert callable(java::SynchronizedStatement.__init__)


def test_java::synchronizedstatement_constructor_args():
    sig = inspect.signature(java::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::trystatement_is_not_abstract():
    assert not inspect.isabstract(java::TryStatement)


def test_java::trystatement_constructor_exists():
    assert callable(java::TryStatement.__init__)


def test_java::trystatement_constructor_args():
    sig = inspect.signature(java::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java::SuperConstructorInvocation)


def test_java::superconstructorinvocation_constructor_exists():
    assert callable(java::SuperConstructorInvocation.__init__)


def test_java::superconstructorinvocation_constructor_args():
    sig = inspect.signature(java::SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::breakstatement_is_not_abstract():
    assert not inspect.isabstract(java::BreakStatement)


def test_java::breakstatement_constructor_exists():
    assert callable(java::BreakStatement.__init__)


def test_java::breakstatement_constructor_args():
    sig = inspect.signature(java::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::whilestatement_is_not_abstract():
    assert not inspect.isabstract(java::WhileStatement)


def test_java::whilestatement_constructor_exists():
    assert callable(java::WhileStatement.__init__)


def test_java::whilestatement_constructor_args():
    sig = inspect.signature(java::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::throwstatement_is_not_abstract():
    assert not inspect.isabstract(java::ThrowStatement)


def test_java::throwstatement_constructor_exists():
    assert callable(java::ThrowStatement.__init__)


def test_java::throwstatement_constructor_args():
    sig = inspect.signature(java::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::continuestatement_is_not_abstract():
    assert not inspect.isabstract(java::ContinueStatement)


def test_java::continuestatement_constructor_exists():
    assert callable(java::ContinueStatement.__init__)


def test_java::continuestatement_constructor_args():
    sig = inspect.signature(java::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::switchstatement_is_not_abstract():
    assert not inspect.isabstract(java::SwitchStatement)


def test_java::switchstatement_constructor_exists():
    assert callable(java::SwitchStatement.__init__)


def test_java::switchstatement_constructor_args():
    sig = inspect.signature(java::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java::VariableDeclarationStatement)


def test_java::variabledeclarationstatement_constructor_exists():
    assert callable(java::VariableDeclarationStatement.__init__)


def test_java::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(java::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java::variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(java::VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in java::VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::emptystatement_is_not_abstract():
    assert not inspect.isabstract(java::EmptyStatement)


def test_java::emptystatement_constructor_exists():
    assert callable(java::EmptyStatement.__init__)


def test_java::emptystatement_constructor_args():
    sig = inspect.signature(java::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::forstatement_is_not_abstract():
    assert not inspect.isabstract(java::ForStatement)


def test_java::forstatement_constructor_exists():
    assert callable(java::ForStatement.__init__)


def test_java::forstatement_constructor_args():
    sig = inspect.signature(java::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::switchcase_is_not_abstract():
    assert not inspect.isabstract(java::SwitchCase)


def test_java::switchcase_constructor_exists():
    assert callable(java::SwitchCase.__init__)


def test_java::switchcase_constructor_args():
    sig = inspect.signature(java::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java::switchcase_has_default():
    assert hasattr(java::SwitchCase, "default")
    descriptor = None
    for klass in java::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java::typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java::TypeDeclarationStatement)


def test_java::typedeclarationstatement_constructor_exists():
    assert callable(java::TypeDeclarationStatement.__init__)


def test_java::typedeclarationstatement_constructor_args():
    sig = inspect.signature(java::TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::ifstatement_is_not_abstract():
    assert not inspect.isabstract(java::IfStatement)


def test_java::ifstatement_constructor_exists():
    assert callable(java::IfStatement.__init__)


def test_java::ifstatement_constructor_args():
    sig = inspect.signature(java::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java::ConstructorInvocation)


def test_java::constructorinvocation_constructor_exists():
    assert callable(java::ConstructorInvocation.__init__)


def test_java::constructorinvocation_constructor_args():
    sig = inspect.signature(java::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::returnstatement_is_not_abstract():
    assert not inspect.isabstract(java::ReturnStatement)


def test_java::returnstatement_constructor_exists():
    assert callable(java::ReturnStatement.__init__)


def test_java::returnstatement_constructor_args():
    sig = inspect.signature(java::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::catchclause_is_not_abstract():
    assert not inspect.isabstract(java::CatchClause)


def test_java::catchclause_constructor_exists():
    assert callable(java::CatchClause.__init__)


def test_java::catchclause_constructor_args():
    sig = inspect.signature(java::CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java::assertstatement_is_not_abstract():
    assert not inspect.isabstract(java::AssertStatement)


def test_java::assertstatement_constructor_exists():
    assert callable(java::AssertStatement.__init__)


def test_java::assertstatement_constructor_args():
    sig = inspect.signature(java::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::manifest_is_not_abstract():
    assert not inspect.isabstract(java::Manifest)


def test_java::manifest_constructor_exists():
    assert callable(java::Manifest.__init__)


def test_java::manifest_constructor_args():
    sig = inspect.signature(java::Manifest.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java::classfile_is_not_abstract():
    assert not inspect.isabstract(java::ClassFile)


def test_java::classfile_constructor_exists():
    assert callable(java::ClassFile.__init__)


def test_java::classfile_constructor_args():
    sig = inspect.signature(java::ClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java::classfile_has_originalFilePath():
    assert hasattr(java::ClassFile, "originalFilePath")
    descriptor = None
    for klass in java::ClassFile.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java::compilationunit_is_not_abstract():
    assert not inspect.isabstract(java::CompilationUnit)


def test_java::compilationunit_constructor_exists():
    assert callable(java::CompilationUnit.__init__)


def test_java::compilationunit_constructor_args():
    sig = inspect.signature(java::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java::compilationunit_has_originalFilePath():
    assert hasattr(java::CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in java::CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java::VariableDeclaration)


def test_java::variabledeclaration_constructor_exists():
    assert callable(java::VariableDeclaration.__init__)


def test_java::variabledeclaration_constructor_args():
    sig = inspect.signature(java::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java::variabledeclaration_has_extraArrayDimensions():
    assert hasattr(java::VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in java::VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(java::BodyDeclaration)


def test_java::bodydeclaration_constructor_exists():
    assert callable(java::BodyDeclaration.__init__)


def test_java::bodydeclaration_constructor_args():
    sig = inspect.signature(java::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::type_is_not_abstract():
    assert not inspect.isabstract(java::Type)


def test_java::type_constructor_exists():
    assert callable(java::Type.__init__)


def test_java::type_constructor_args():
    sig = inspect.signature(java::Type.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolveditem_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedItem)


def test_java::unresolveditem_constructor_exists():
    assert callable(java::UnresolvedItem.__init__)


def test_java::unresolveditem_constructor_args():
    sig = inspect.signature(java::UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(java::LabeledStatement)


def test_java::labeledstatement_constructor_exists():
    assert callable(java::LabeledStatement.__init__)


def test_java::labeledstatement_constructor_args():
    sig = inspect.signature(java::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java::archive_is_not_abstract():
    assert not inspect.isabstract(java::Archive)


def test_java::archive_constructor_exists():
    assert callable(java::Archive.__init__)


def test_java::archive_constructor_args():
    sig = inspect.signature(java::Archive.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java::archive_has_originalFilePath():
    assert hasattr(java::Archive, "originalFilePath")
    descriptor = None
    for klass in java::Archive.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java::annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationMemberValuePair)


def test_java::annotationmembervaluepair_constructor_exists():
    assert callable(java::AnnotationMemberValuePair.__init__)


def test_java::annotationmembervaluepair_constructor_args():
    sig = inspect.signature(java::AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java::VariableDeclarationFragment)


def test_java::variabledeclarationfragment_constructor_exists():
    assert callable(java::VariableDeclarationFragment.__init__)


def test_java::variabledeclarationfragment_constructor_args():
    sig = inspect.signature(java::VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::characterliteral_is_not_abstract():
    assert not inspect.isabstract(java::CharacterLiteral)


def test_java::characterliteral_constructor_exists():
    assert callable(java::CharacterLiteral.__init__)


def test_java::characterliteral_constructor_args():
    sig = inspect.signature(java::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java::characterliteral_has_escapedValue():
    assert hasattr(java::CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in java::CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(java::ConditionalExpression)


def test_java::conditionalexpression_constructor_exists():
    assert callable(java::ConditionalExpression.__init__)


def test_java::conditionalexpression_constructor_args():
    sig = inspect.signature(java::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::numberliteral_is_not_abstract():
    assert not inspect.isabstract(java::NumberLiteral)


def test_java::numberliteral_constructor_exists():
    assert callable(java::NumberLiteral.__init__)


def test_java::numberliteral_constructor_args():
    sig = inspect.signature(java::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java::numberliteral_has_tokenValue():
    assert hasattr(java::NumberLiteral, "tokenValue")
    descriptor = None
    for klass in java::NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java::castexpression_is_not_abstract():
    assert not inspect.isabstract(java::CastExpression)


def test_java::castexpression_constructor_exists():
    assert callable(java::CastExpression.__init__)


def test_java::castexpression_constructor_args():
    sig = inspect.signature(java::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::annotation_is_not_abstract():
    assert not inspect.isabstract(java::Annotation)


def test_java::annotation_constructor_exists():
    assert callable(java::Annotation.__init__)


def test_java::annotation_constructor_args():
    sig = inspect.signature(java::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java::arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(java::ArrayLengthAccess)


def test_java::arraylengthaccess_constructor_exists():
    assert callable(java::ArrayLengthAccess.__init__)


def test_java::arraylengthaccess_constructor_args():
    sig = inspect.signature(java::ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(java::PostfixExpression)


def test_java::postfixexpression_constructor_exists():
    assert callable(java::PostfixExpression.__init__)


def test_java::postfixexpression_constructor_args():
    sig = inspect.signature(java::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::postfixexpression_has_operator():
    assert hasattr(java::PostfixExpression, "operator")
    descriptor = None
    for klass in java::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(java::PrefixExpression)


def test_java::prefixexpression_constructor_exists():
    assert callable(java::PrefixExpression.__init__)


def test_java::prefixexpression_constructor_args():
    sig = inspect.signature(java::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::prefixexpression_has_operator():
    assert hasattr(java::PrefixExpression, "operator")
    descriptor = None
    for klass in java::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::arraycreation_is_not_abstract():
    assert not inspect.isabstract(java::ArrayCreation)


def test_java::arraycreation_constructor_exists():
    assert callable(java::ArrayCreation.__init__)


def test_java::arraycreation_constructor_args():
    sig = inspect.signature(java::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(java::ArrayAccess)


def test_java::arrayaccess_constructor_exists():
    assert callable(java::ArrayAccess.__init__)


def test_java::arrayaccess_constructor_args():
    sig = inspect.signature(java::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::stringliteral_is_not_abstract():
    assert not inspect.isabstract(java::StringLiteral)


def test_java::stringliteral_constructor_exists():
    assert callable(java::StringLiteral.__init__)


def test_java::stringliteral_constructor_args():
    sig = inspect.signature(java::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java::stringliteral_has_escapedValue():
    assert hasattr(java::StringLiteral, "escapedValue")
    descriptor = None
    for klass in java::StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java::assignment_is_not_abstract():
    assert not inspect.isabstract(java::Assignment)


def test_java::assignment_constructor_exists():
    assert callable(java::Assignment.__init__)


def test_java::assignment_constructor_args():
    sig = inspect.signature(java::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::assignment_has_operator():
    assert hasattr(java::Assignment, "operator")
    descriptor = None
    for klass in java::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(java::InstanceofExpression)


def test_java::instanceofexpression_constructor_exists():
    assert callable(java::InstanceofExpression.__init__)


def test_java::instanceofexpression_constructor_args():
    sig = inspect.signature(java::InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::nullliteral_is_not_abstract():
    assert not inspect.isabstract(java::NullLiteral)


def test_java::nullliteral_constructor_exists():
    assert callable(java::NullLiteral.__init__)


def test_java::nullliteral_constructor_args():
    sig = inspect.signature(java::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::unresolveditemaccess_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedItemAccess)


def test_java::unresolveditemaccess_constructor_exists():
    assert callable(java::UnresolvedItemAccess.__init__)


def test_java::unresolveditemaccess_constructor_args():
    sig = inspect.signature(java::UnresolvedItemAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::singlevariableaccess_is_not_abstract():
    assert not inspect.isabstract(java::SingleVariableAccess)


def test_java::singlevariableaccess_constructor_exists():
    assert callable(java::SingleVariableAccess.__init__)


def test_java::singlevariableaccess_constructor_args():
    sig = inspect.signature(java::SingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(java::ParenthesizedExpression)


def test_java::parenthesizedexpression_constructor_exists():
    assert callable(java::ParenthesizedExpression.__init__)


def test_java::parenthesizedexpression_constructor_args():
    sig = inspect.signature(java::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::typeliteral_is_not_abstract():
    assert not inspect.isabstract(java::TypeLiteral)


def test_java::typeliteral_constructor_exists():
    assert callable(java::TypeLiteral.__init__)


def test_java::typeliteral_constructor_args():
    sig = inspect.signature(java::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(java::MethodInvocation)


def test_java::methodinvocation_constructor_exists():
    assert callable(java::MethodInvocation.__init__)


def test_java::methodinvocation_constructor_args():
    sig = inspect.signature(java::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(java::ClassInstanceCreation)


def test_java::classinstancecreation_constructor_exists():
    assert callable(java::ClassInstanceCreation.__init__)


def test_java::classinstancecreation_constructor_args():
    sig = inspect.signature(java::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(java::ArrayInitializer)


def test_java::arrayinitializer_constructor_exists():
    assert callable(java::ArrayInitializer.__init__)


def test_java::arrayinitializer_constructor_args():
    sig = inspect.signature(java::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java::infixexpression_is_not_abstract():
    assert not inspect.isabstract(java::InfixExpression)


def test_java::infixexpression_constructor_exists():
    assert callable(java::InfixExpression.__init__)


def test_java::infixexpression_constructor_args():
    sig = inspect.signature(java::InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java::infixexpression_has_operator():
    assert hasattr(java::InfixExpression, "operator")
    descriptor = None
    for klass in java::InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(java::BooleanLiteral)


def test_java::booleanliteral_constructor_exists():
    assert callable(java::BooleanLiteral.__init__)


def test_java::booleanliteral_constructor_args():
    sig = inspect.signature(java::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java::booleanliteral_has_value():
    assert hasattr(java::BooleanLiteral, "value")
    descriptor = None
    for klass in java::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(java::FieldAccess)


def test_java::fieldaccess_constructor_exists():
    assert callable(java::FieldAccess.__init__)


def test_java::fieldaccess_constructor_args():
    sig = inspect.signature(java::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(java::VariableDeclarationExpression)


def test_java::variabledeclarationexpression_constructor_exists():
    assert callable(java::VariableDeclarationExpression.__init__)


def test_java::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(java::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(java::AbstractTypeQualifiedExpression)


def test_java::abstracttypequalifiedexpression_constructor_exists():
    assert callable(java::AbstractTypeQualifiedExpression.__init__)


def test_java::abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(java::AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java::package_is_not_abstract():
    assert not inspect.isabstract(java::Package)


def test_java::package_constructor_exists():
    assert callable(java::Package.__init__)


def test_java::package_constructor_args():
    sig = inspect.signature(java::Package.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java::arraytype_is_not_abstract():
    assert not inspect.isabstract(java::ArrayType)


def test_java::arraytype_constructor_exists():
    assert callable(java::ArrayType.__init__)


def test_java::arraytype_constructor_args():
    sig = inspect.signature(java::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_java::arraytype_has_dimensions():
    assert hasattr(java::ArrayType, "dimensions")
    descriptor = None
    for klass in java::ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_java::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(java::ParameterizedType)


def test_java::parameterizedtype_constructor_exists():
    assert callable(java::ParameterizedType.__init__)


def test_java::parameterizedtype_constructor_args():
    sig = inspect.signature(java::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetype_is_not_abstract():
    assert not inspect.isabstract(java::PrimitiveType)


def test_java::primitivetype_constructor_exists():
    assert callable(java::PrimitiveType.__init__)


def test_java::primitivetype_constructor_args():
    sig = inspect.signature(java::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(java::WildCardType)


def test_java::wildcardtype_constructor_exists():
    assert callable(java::WildCardType.__init__)


def test_java::wildcardtype_constructor_args():
    sig = inspect.signature(java::WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_java::wildcardtype_has_upperBound():
    assert hasattr(java::WildCardType, "upperBound")
    descriptor = None
    for klass in java::WildCardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_java::unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(java::UnresolvedType)


def test_java::unresolvedtype_constructor_exists():
    assert callable(java::UnresolvedType.__init__)


def test_java::unresolvedtype_constructor_args():
    sig = inspect.signature(java::UnresolvedType.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java::statement_is_not_abstract():
    assert not inspect.isabstract(java::Statement)


def test_java::statement_constructor_exists():
    assert callable(java::Statement.__init__)


def test_java::statement_constructor_args():
    sig = inspect.signature(java::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::tagelement_is_not_abstract():
    assert not inspect.isabstract(java::TagElement)


def test_java::tagelement_constructor_exists():
    assert callable(java::TagElement.__init__)


def test_java::tagelement_constructor_args():
    sig = inspect.signature(java::TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java::tagelement_has_tagName():
    assert hasattr(java::TagElement, "tagName")
    descriptor = None
    for klass in java::TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java::modifier_is_not_abstract():
    assert not inspect.isabstract(java::Modifier)


def test_java::modifier_constructor_exists():
    assert callable(java::Modifier.__init__)


def test_java::modifier_constructor_args():
    sig = inspect.signature(java::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "native" in params, "Missing parameter 'native'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "static" in params, "Missing parameter 'static'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_java::modifier_has_native():
    assert hasattr(java::Modifier, "native")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_transient():
    assert hasattr(java::Modifier, "transient")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_static():
    assert hasattr(java::Modifier, "static")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_strictfp():
    assert hasattr(java::Modifier, "strictfp")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_visibility():
    assert hasattr(java::Modifier, "visibility")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_volatile():
    assert hasattr(java::Modifier, "volatile")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_synchronized():
    assert hasattr(java::Modifier, "synchronized")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java::modifier_has_inheritance():
    assert hasattr(java::Modifier, "inheritance")
    descriptor = None
    for klass in java::Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_java::namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(java::NamespaceAccess)


def test_java::namespaceaccess_constructor_exists():
    assert callable(java::NamespaceAccess.__init__)


def test_java::namespaceaccess_constructor_args():
    sig = inspect.signature(java::NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::comment_is_not_abstract():
    assert not inspect.isabstract(java::Comment)


def test_java::comment_constructor_exists():
    assert callable(java::Comment.__init__)


def test_java::comment_constructor_args():
    sig = inspect.signature(java::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"
    assert "content" in params, "Missing parameter 'content'"
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"

def test_java::comment_has_enclosedByParent():
    assert hasattr(java::Comment, "enclosedByParent")
    descriptor = None
    for klass in java::Comment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)

def test_java::comment_has_content():
    assert hasattr(java::Comment, "content")
    descriptor = None
    for klass in java::Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_java::comment_has_prefixOfParent():
    assert hasattr(java::Comment, "prefixOfParent")
    descriptor = None
    for klass in java::Comment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)



def test_java::expression_is_not_abstract():
    assert not inspect.isabstract(java::Expression)


def test_java::expression_constructor_exists():
    assert callable(java::Expression.__init__)


def test_java::expression_constructor_args():
    sig = inspect.signature(java::Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::AnonymousClassDeclaration)


def test_java::anonymousclassdeclaration_constructor_exists():
    assert callable(java::AnonymousClassDeclaration.__init__)


def test_java::anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(java::AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::textelement_is_not_abstract():
    assert not inspect.isabstract(java::TextElement)


def test_java::textelement_constructor_exists():
    assert callable(java::TextElement.__init__)


def test_java::textelement_constructor_args():
    sig = inspect.signature(java::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java::textelement_has_text():
    assert hasattr(java::TextElement, "text")
    descriptor = None
    for klass in java::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_java::memberref_is_not_abstract():
    assert not inspect.isabstract(java::MemberRef)


def test_java::memberref_constructor_exists():
    assert callable(java::MemberRef.__init__)


def test_java::memberref_constructor_args():
    sig = inspect.signature(java::MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java::methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(java::MethodRefParameter)


def test_java::methodrefparameter_constructor_exists():
    assert callable(java::MethodRefParameter.__init__)


def test_java::methodrefparameter_constructor_args():
    sig = inspect.signature(java::MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "name" in params, "Missing parameter 'name'"

def test_java::methodrefparameter_has_varargs():
    assert hasattr(java::MethodRefParameter, "varargs")
    descriptor = None
    for klass in java::MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_java::methodrefparameter_has_name():
    assert hasattr(java::MethodRefParameter, "name")
    descriptor = None
    for klass in java::MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::ImportDeclaration)


def test_java::importdeclaration_constructor_exists():
    assert callable(java::ImportDeclaration.__init__)


def test_java::importdeclaration_constructor_args():
    sig = inspect.signature(java::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java::importdeclaration_has_static():
    assert hasattr(java::ImportDeclaration, "static")
    descriptor = None
    for klass in java::ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java::abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(java::AbstractVariablesContainer)


def test_java::abstractvariablescontainer_constructor_exists():
    assert callable(java::AbstractVariablesContainer.__init__)


def test_java::abstractvariablescontainer_constructor_args():
    sig = inspect.signature(java::AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_java::namedelement_is_not_abstract():
    assert not inspect.isabstract(java::NamedElement)


def test_java::namedelement_constructor_exists():
    assert callable(java::NamedElement.__init__)


def test_java::namedelement_constructor_args():
    sig = inspect.signature(java::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "proxy" in params, "Missing parameter 'proxy'"
    assert "name" in params, "Missing parameter 'name'"

def test_java::namedelement_has_proxy():
    assert hasattr(java::NamedElement, "proxy")
    descriptor = None
    for klass in java::NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)

def test_java::namedelement_has_name():
    assert hasattr(java::NamedElement, "name")
    descriptor = None
    for klass in java::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java::AbstractMethodInvocation)


def test_java::abstractmethodinvocation_constructor_exists():
    assert callable(java::AbstractMethodInvocation.__init__)


def test_java::abstractmethodinvocation_constructor_args():
    sig = inspect.signature(java::AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java::methodref_is_not_abstract():
    assert not inspect.isabstract(java::MethodRef)


def test_java::methodref_constructor_exists():
    assert callable(java::MethodRef.__init__)


def test_java::methodref_constructor_args():
    sig = inspect.signature(java::MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java::typeparameter_is_not_abstract():
    assert not inspect.isabstract(java::TypeParameter)


def test_java::typeparameter_constructor_exists():
    assert callable(java::TypeParameter.__init__)


def test_java::typeparameter_constructor_args():
    sig = inspect.signature(java::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java::typeaccess_is_not_abstract():
    assert not inspect.isabstract(java::TypeAccess)


def test_java::typeaccess_constructor_exists():
    assert callable(java::TypeAccess.__init__)


def test_java::typeaccess_constructor_args():
    sig = inspect.signature(java::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_java::singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java::SingleVariableDeclaration)


def test_java::singlevariabledeclaration_constructor_exists():
    assert callable(java::SingleVariableDeclaration.__init__)


def test_java::singlevariabledeclaration_constructor_args():
    sig = inspect.signature(java::SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java::singlevariabledeclaration_has_varargs():
    assert hasattr(java::SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in java::SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_java::block_is_not_abstract():
    assert not inspect.isabstract(java::Block)


def test_java::block_constructor_exists():
    assert callable(java::Block.__init__)


def test_java::block_constructor_args():
    sig = inspect.signature(java::Block.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java::AbstractTypeDeclaration)


def test_java::abstracttypedeclaration_constructor_exists():
    assert callable(java::AbstractTypeDeclaration.__init__)


def test_java::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(java::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(java::FieldDeclaration)


def test_java::fielddeclaration_constructor_exists():
    assert callable(java::FieldDeclaration.__init__)


def test_java::fielddeclaration_constructor_args():
    sig = inspect.signature(java::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::initializer_is_not_abstract():
    assert not inspect.isabstract(java::Initializer)


def test_java::initializer_constructor_exists():
    assert callable(java::Initializer.__init__)


def test_java::initializer_constructor_args():
    sig = inspect.signature(java::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java::enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::EnumConstantDeclaration)


def test_java::enumconstantdeclaration_constructor_exists():
    assert callable(java::EnumConstantDeclaration.__init__)


def test_java::enumconstantdeclaration_constructor_args():
    sig = inspect.signature(java::EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java::AnnotationTypeMemberDeclaration)


def test_java::annotationtypememberdeclaration_constructor_exists():
    assert callable(java::AnnotationTypeMemberDeclaration.__init__)


def test_java::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java::AbstractMethodDeclaration)


def test_java::abstractmethoddeclaration_constructor_exists():
    assert callable(java::AbstractMethodDeclaration.__init__)


def test_java::abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(java::AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "MINUS_ASSIGN",
        "ASSIGN",
        "BIT_OR_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "PLUS_ASSIGN",
        "BIT_XOR_ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "TIMES_ASSIGN",
        "REMAINDER_ASSIGN",
        "DIVIDE_ASSIGN",
        "BIT_AND_ASSIGN",
        "LEFT_SHIFT_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentKind"

def test_infixexpressionkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionKind is not None

def test_infixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionKind]
    expected_literals = [
        "TIMES",
        "GREATER",
        "PLUS",
        "LEFT_SHIFT",
        "AND",
        "DIVIDE",
        "LESS_EQUALS",
        "XOR",
        "LESS",
        "OR",
        "RIGHT_SHIFT_SIGNED",
        "GREATER_EQUALS",
        "RIGHT_SHIFT_UNSIGNED",
        "CONDITIONAL_AND",
        "MINUS",
        "REMAINDER",
        "CONDITIONAL_OR",
        "NOT_EQUALS",
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
        "INCREMENT",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpressionKind"

def test_prefixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionKind is not None

def test_prefixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionKind]
    expected_literals = [
        "DECREMENT",
        "NOT",
        "COMPLEMENT",
        "MINUS",
        "INCREMENT",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionKind"

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "none",
        "final",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"

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
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
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
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
EnumDeclaration_strategy = st.builds(
    EnumDeclaration,
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
java::UnresolvedClassDeclaration_strategy = st.builds(
    java::UnresolvedClassDeclaration,
)
java::UnresolvedVariableDeclarationFragment_strategy = st.builds(
    java::UnresolvedVariableDeclarationFragment,
)
java::UnresolvedLabeledStatement_strategy = st.builds(
    java::UnresolvedLabeledStatement,
)
java::UnresolvedEnumDeclaration_strategy = st.builds(
    java::UnresolvedEnumDeclaration,
)
java::UnresolvedMethodDeclaration_strategy = st.builds(
    java::UnresolvedMethodDeclaration,
)
java::UnresolvedAnnotationTypeMemberDeclaration_strategy = st.builds(
    java::UnresolvedAnnotationTypeMemberDeclaration,
)
java::UnresolvedInterfaceDeclaration_strategy = st.builds(
    java::UnresolvedInterfaceDeclaration,
)
java::UnresolvedSingleVariableDeclaration_strategy = st.builds(
    java::UnresolvedSingleVariableDeclaration,
)
AnnotationTypeDeclaration_strategy = st.builds(
    AnnotationTypeDeclaration,
)
java::UnresolvedAnnotationDeclaration_strategy = st.builds(
    java::UnresolvedAnnotationDeclaration,
)
AbstractTypeQualifiedExpression_strategy = st.builds(
    AbstractTypeQualifiedExpression,
)
java::ThisExpression_strategy = st.builds(
    java::ThisExpression,
)
java::SuperFieldAccess_strategy = st.builds(
    java::SuperFieldAccess,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
java::PrimitiveTypeDouble_strategy = st.builds(
    java::PrimitiveTypeDouble,
)
java::PrimitiveTypeFloat_strategy = st.builds(
    java::PrimitiveTypeFloat,
)
java::PrimitiveTypeLong_strategy = st.builds(
    java::PrimitiveTypeLong,
)
java::PrimitiveTypeInt_strategy = st.builds(
    java::PrimitiveTypeInt,
)
java::PrimitiveTypeByte_strategy = st.builds(
    java::PrimitiveTypeByte,
)
java::PrimitiveTypeVoid_strategy = st.builds(
    java::PrimitiveTypeVoid,
)
java::PrimitiveTypeChar_strategy = st.builds(
    java::PrimitiveTypeChar,
)
java::PrimitiveTypeShort_strategy = st.builds(
    java::PrimitiveTypeShort,
)
java::PrimitiveTypeBoolean_strategy = st.builds(
    java::PrimitiveTypeBoolean,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
java::PackageAccess_strategy = st.builds(
    java::PackageAccess,
)
java::Model_strategy = st.builds(
    java::Model,
    name=
        safe_text
)
java::ManifestEntry_strategy = st.builds(
    java::ManifestEntry,
    name=
        safe_text
)
java::ManifestAttribute_strategy = st.builds(
    java::ManifestAttribute,
    value=
        safe_text,
    key=
        safe_text
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
java::InterfaceDeclaration_strategy = st.builds(
    java::InterfaceDeclaration,
)
java::ClassDeclaration_strategy = st.builds(
    java::ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
java::ConstructorDeclaration_strategy = st.builds(
    java::ConstructorDeclaration,
)
java::MethodDeclaration_strategy = st.builds(
    java::MethodDeclaration,
    extraArrayDimensions=
        st.integers()
)
AbstractMethodInvocation_strategy = st.builds(
    AbstractMethodInvocation,
)
java::SuperMethodInvocation_strategy = st.builds(
    java::SuperMethodInvocation,
)
Comment_strategy = st.builds(
    Comment,
)
java::LineComment_strategy = st.builds(
    java::LineComment,
)
java::Javadoc_strategy = st.builds(
    java::Javadoc,
)
java::BlockComment_strategy = st.builds(
    java::BlockComment,
)
java::ASTNode_strategy = st.builds(
    java::ASTNode,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
java::UnresolvedTypeDeclaration_strategy = st.builds(
    java::UnresolvedTypeDeclaration,
)
java::EnumDeclaration_strategy = st.builds(
    java::EnumDeclaration,
)
java::TypeDeclaration_strategy = st.builds(
    java::TypeDeclaration,
)
java::AnnotationTypeDeclaration_strategy = st.builds(
    java::AnnotationTypeDeclaration,
)
Statement_strategy = st.builds(
    Statement,
)
java::DoStatement_strategy = st.builds(
    java::DoStatement,
)
java::EnhancedForStatement_strategy = st.builds(
    java::EnhancedForStatement,
)
java::ExpressionStatement_strategy = st.builds(
    java::ExpressionStatement,
)
java::SynchronizedStatement_strategy = st.builds(
    java::SynchronizedStatement,
)
java::TryStatement_strategy = st.builds(
    java::TryStatement,
)
java::SuperConstructorInvocation_strategy = st.builds(
    java::SuperConstructorInvocation,
)
java::BreakStatement_strategy = st.builds(
    java::BreakStatement,
)
java::WhileStatement_strategy = st.builds(
    java::WhileStatement,
)
java::ThrowStatement_strategy = st.builds(
    java::ThrowStatement,
)
java::ContinueStatement_strategy = st.builds(
    java::ContinueStatement,
)
java::SwitchStatement_strategy = st.builds(
    java::SwitchStatement,
)
java::VariableDeclarationStatement_strategy = st.builds(
    java::VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
java::EmptyStatement_strategy = st.builds(
    java::EmptyStatement,
)
java::ForStatement_strategy = st.builds(
    java::ForStatement,
)
java::SwitchCase_strategy = st.builds(
    java::SwitchCase,
    default=
        st.booleans()
)
java::TypeDeclarationStatement_strategy = st.builds(
    java::TypeDeclarationStatement,
)
java::IfStatement_strategy = st.builds(
    java::IfStatement,
)
java::ConstructorInvocation_strategy = st.builds(
    java::ConstructorInvocation,
)
java::ReturnStatement_strategy = st.builds(
    java::ReturnStatement,
)
java::CatchClause_strategy = st.builds(
    java::CatchClause,
)
java::AssertStatement_strategy = st.builds(
    java::AssertStatement,
)
java::Manifest_strategy = st.builds(
    java::Manifest,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
java::ClassFile_strategy = st.builds(
    java::ClassFile,
    originalFilePath=
        safe_text
)
java::CompilationUnit_strategy = st.builds(
    java::CompilationUnit,
    originalFilePath=
        safe_text
)
java::VariableDeclaration_strategy = st.builds(
    java::VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
java::BodyDeclaration_strategy = st.builds(
    java::BodyDeclaration,
)
java::Type_strategy = st.builds(
    java::Type,
)
java::UnresolvedItem_strategy = st.builds(
    java::UnresolvedItem,
)
java::LabeledStatement_strategy = st.builds(
    java::LabeledStatement,
)
java::Archive_strategy = st.builds(
    java::Archive,
    originalFilePath=
        safe_text
)
java::AnnotationMemberValuePair_strategy = st.builds(
    java::AnnotationMemberValuePair,
)
java::VariableDeclarationFragment_strategy = st.builds(
    java::VariableDeclarationFragment,
)
Expression_strategy = st.builds(
    Expression,
)
java::CharacterLiteral_strategy = st.builds(
    java::CharacterLiteral,
    escapedValue=
        safe_text
)
java::ConditionalExpression_strategy = st.builds(
    java::ConditionalExpression,
)
java::NumberLiteral_strategy = st.builds(
    java::NumberLiteral,
    tokenValue=
        safe_text
)
java::CastExpression_strategy = st.builds(
    java::CastExpression,
)
java::Annotation_strategy = st.builds(
    java::Annotation,
)
java::ArrayLengthAccess_strategy = st.builds(
    java::ArrayLengthAccess,
)
java::PostfixExpression_strategy = st.builds(
    java::PostfixExpression,
    operator=
        safe_text
)
java::PrefixExpression_strategy = st.builds(
    java::PrefixExpression,
    operator=
        safe_text
)
java::ArrayCreation_strategy = st.builds(
    java::ArrayCreation,
)
java::ArrayAccess_strategy = st.builds(
    java::ArrayAccess,
)
java::StringLiteral_strategy = st.builds(
    java::StringLiteral,
    escapedValue=
        safe_text
)
java::Assignment_strategy = st.builds(
    java::Assignment,
    operator=
        safe_text
)
java::InstanceofExpression_strategy = st.builds(
    java::InstanceofExpression,
)
java::NullLiteral_strategy = st.builds(
    java::NullLiteral,
)
java::UnresolvedItemAccess_strategy = st.builds(
    java::UnresolvedItemAccess,
)
java::SingleVariableAccess_strategy = st.builds(
    java::SingleVariableAccess,
)
java::ParenthesizedExpression_strategy = st.builds(
    java::ParenthesizedExpression,
)
java::TypeLiteral_strategy = st.builds(
    java::TypeLiteral,
)
java::MethodInvocation_strategy = st.builds(
    java::MethodInvocation,
)
java::ClassInstanceCreation_strategy = st.builds(
    java::ClassInstanceCreation,
)
java::ArrayInitializer_strategy = st.builds(
    java::ArrayInitializer,
)
java::InfixExpression_strategy = st.builds(
    java::InfixExpression,
    operator=
        safe_text
)
java::BooleanLiteral_strategy = st.builds(
    java::BooleanLiteral,
    value=
        st.booleans()
)
java::FieldAccess_strategy = st.builds(
    java::FieldAccess,
)
java::VariableDeclarationExpression_strategy = st.builds(
    java::VariableDeclarationExpression,
)
java::AbstractTypeQualifiedExpression_strategy = st.builds(
    java::AbstractTypeQualifiedExpression,
)
java::Package_strategy = st.builds(
    java::Package,
)
Type_strategy = st.builds(
    Type,
)
java::ArrayType_strategy = st.builds(
    java::ArrayType,
    dimensions=
        st.integers()
)
java::ParameterizedType_strategy = st.builds(
    java::ParameterizedType,
)
java::PrimitiveType_strategy = st.builds(
    java::PrimitiveType,
)
java::WildCardType_strategy = st.builds(
    java::WildCardType,
    upperBound=
        st.booleans()
)
java::UnresolvedType_strategy = st.builds(
    java::UnresolvedType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
java::Statement_strategy = st.builds(
    java::Statement,
)
java::TagElement_strategy = st.builds(
    java::TagElement,
    tagName=
        safe_text
)
java::Modifier_strategy = st.builds(
    java::Modifier,
    native=
        st.booleans(),
    transient=
        st.booleans(),
    static=
        st.booleans(),
    strictfp=
        st.booleans(),
    visibility=
        safe_text,
    volatile=
        st.booleans(),
    synchronized=
        st.booleans(),
    inheritance=
        safe_text
)
java::NamespaceAccess_strategy = st.builds(
    java::NamespaceAccess,
)
java::Comment_strategy = st.builds(
    java::Comment,
    enclosedByParent=
        st.booleans(),
    content=
        safe_text,
    prefixOfParent=
        st.booleans()
)
java::Expression_strategy = st.builds(
    java::Expression,
)
java::AnonymousClassDeclaration_strategy = st.builds(
    java::AnonymousClassDeclaration,
)
java::TextElement_strategy = st.builds(
    java::TextElement,
    text=
        safe_text
)
java::MemberRef_strategy = st.builds(
    java::MemberRef,
)
java::MethodRefParameter_strategy = st.builds(
    java::MethodRefParameter,
    varargs=
        st.booleans(),
    name=
        safe_text
)
java::ImportDeclaration_strategy = st.builds(
    java::ImportDeclaration,
    static=
        st.booleans()
)
java::AbstractVariablesContainer_strategy = st.builds(
    java::AbstractVariablesContainer,
)
java::NamedElement_strategy = st.builds(
    java::NamedElement,
    proxy=
        st.booleans(),
    name=
        safe_text
)
java::AbstractMethodInvocation_strategy = st.builds(
    java::AbstractMethodInvocation,
)
java::MethodRef_strategy = st.builds(
    java::MethodRef,
)
java::TypeParameter_strategy = st.builds(
    java::TypeParameter,
)
java::TypeAccess_strategy = st.builds(
    java::TypeAccess,
)
java::SingleVariableDeclaration_strategy = st.builds(
    java::SingleVariableDeclaration,
    varargs=
        st.booleans()
)
java::Block_strategy = st.builds(
    java::Block,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
java::AbstractTypeDeclaration_strategy = st.builds(
    java::AbstractTypeDeclaration,
)
java::FieldDeclaration_strategy = st.builds(
    java::FieldDeclaration,
)
java::Initializer_strategy = st.builds(
    java::Initializer,
)
java::EnumConstantDeclaration_strategy = st.builds(
    java::EnumConstantDeclaration,
)
java::AnnotationTypeMemberDeclaration_strategy = st.builds(
    java::AnnotationTypeMemberDeclaration,
)
java::AbstractMethodDeclaration_strategy = st.builds(
    java::AbstractMethodDeclaration,
)

@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)

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

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

@given(instance=EnumDeclaration_strategy)
@settings(max_examples=50)
def test_enumdeclaration_instantiation(instance):
    assert isinstance(instance, EnumDeclaration)

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

@given(instance=java::UnresolvedClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedclassdeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedClassDeclaration)

@given(instance=java::UnresolvedVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java::unresolvedvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, java::UnresolvedVariableDeclarationFragment)

@given(instance=java::UnresolvedLabeledStatement_strategy)
@settings(max_examples=50)
def test_java::unresolvedlabeledstatement_instantiation(instance):
    assert isinstance(instance, java::UnresolvedLabeledStatement)

@given(instance=java::UnresolvedEnumDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedenumdeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedEnumDeclaration)

@given(instance=java::UnresolvedMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedmethoddeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedMethodDeclaration)

@given(instance=java::UnresolvedAnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedannotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedAnnotationTypeMemberDeclaration)

@given(instance=java::UnresolvedInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedInterfaceDeclaration)

@given(instance=java::UnresolvedSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedSingleVariableDeclaration)

@given(instance=AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeDeclaration)

@given(instance=java::UnresolvedAnnotationDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedannotationdeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedAnnotationDeclaration)

@given(instance=AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, AbstractTypeQualifiedExpression)

@given(instance=java::ThisExpression_strategy)
@settings(max_examples=50)
def test_java::thisexpression_instantiation(instance):
    assert isinstance(instance, java::ThisExpression)

@given(instance=java::SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java::superfieldaccess_instantiation(instance):
    assert isinstance(instance, java::SuperFieldAccess)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=java::PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java::primitivetypedouble_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeDouble)

@given(instance=java::PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java::primitivetypefloat_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeFloat)

@given(instance=java::PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java::primitivetypelong_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeLong)

@given(instance=java::PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java::primitivetypeint_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeInt)

@given(instance=java::PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java::primitivetypebyte_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeByte)

@given(instance=java::PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java::primitivetypevoid_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeVoid)

@given(instance=java::PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java::primitivetypechar_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeChar)

@given(instance=java::PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java::primitivetypeshort_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeShort)

@given(instance=java::PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java::primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, java::PrimitiveTypeBoolean)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=java::PackageAccess_strategy)
@settings(max_examples=50)
def test_java::packageaccess_instantiation(instance):
    assert isinstance(instance, java::PackageAccess)

@given(instance=java::Model_strategy)
@settings(max_examples=50)
def test_java::model_instantiation(instance):
    assert isinstance(instance, java::Model)

@given(instance=java::Model_strategy)
def test_java::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Model_strategy)
def test_java::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::ManifestEntry_strategy)
@settings(max_examples=50)
def test_java::manifestentry_instantiation(instance):
    assert isinstance(instance, java::ManifestEntry)

@given(instance=java::ManifestEntry_strategy)
def test_java::manifestentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::ManifestEntry_strategy)
def test_java::manifestentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::ManifestAttribute_strategy)
@settings(max_examples=50)
def test_java::manifestattribute_instantiation(instance):
    assert isinstance(instance, java::ManifestAttribute)

@given(instance=java::ManifestAttribute_strategy)
def test_java::manifestattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=java::ManifestAttribute_strategy)
def test_java::manifestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java::ManifestAttribute_strategy)
def test_java::manifestattribute_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=java::ManifestAttribute_strategy)
def test_java::manifestattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=java::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, java::InterfaceDeclaration)

@given(instance=java::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::classdeclaration_instantiation(instance):
    assert isinstance(instance, java::ClassDeclaration)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=java::ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_java::constructordeclaration_instantiation(instance):
    assert isinstance(instance, java::ConstructorDeclaration)

@given(instance=java::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java::methoddeclaration_instantiation(instance):
    assert isinstance(instance, java::MethodDeclaration)

@given(instance=java::MethodDeclaration_strategy)
def test_java::methoddeclaration_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=java::MethodDeclaration_strategy)
def test_java::methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, AbstractMethodInvocation)

@given(instance=java::SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java::supermethodinvocation_instantiation(instance):
    assert isinstance(instance, java::SuperMethodInvocation)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=java::LineComment_strategy)
@settings(max_examples=50)
def test_java::linecomment_instantiation(instance):
    assert isinstance(instance, java::LineComment)

@given(instance=java::Javadoc_strategy)
@settings(max_examples=50)
def test_java::javadoc_instantiation(instance):
    assert isinstance(instance, java::Javadoc)

@given(instance=java::BlockComment_strategy)
@settings(max_examples=50)
def test_java::blockcomment_instantiation(instance):
    assert isinstance(instance, java::BlockComment)

@given(instance=java::ASTNode_strategy)
@settings(max_examples=50)
def test_java::astnode_instantiation(instance):
    assert isinstance(instance, java::ASTNode)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=java::UnresolvedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::unresolvedtypedeclaration_instantiation(instance):
    assert isinstance(instance, java::UnresolvedTypeDeclaration)

@given(instance=java::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java::enumdeclaration_instantiation(instance):
    assert isinstance(instance, java::EnumDeclaration)

@given(instance=java::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::typedeclaration_instantiation(instance):
    assert isinstance(instance, java::TypeDeclaration)

@given(instance=java::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, java::AnnotationTypeDeclaration)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java::DoStatement_strategy)
@settings(max_examples=50)
def test_java::dostatement_instantiation(instance):
    assert isinstance(instance, java::DoStatement)

@given(instance=java::EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java::enhancedforstatement_instantiation(instance):
    assert isinstance(instance, java::EnhancedForStatement)

@given(instance=java::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java::expressionstatement_instantiation(instance):
    assert isinstance(instance, java::ExpressionStatement)

@given(instance=java::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, java::SynchronizedStatement)

@given(instance=java::TryStatement_strategy)
@settings(max_examples=50)
def test_java::trystatement_instantiation(instance):
    assert isinstance(instance, java::TryStatement)

@given(instance=java::SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java::superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, java::SuperConstructorInvocation)

@given(instance=java::BreakStatement_strategy)
@settings(max_examples=50)
def test_java::breakstatement_instantiation(instance):
    assert isinstance(instance, java::BreakStatement)

@given(instance=java::WhileStatement_strategy)
@settings(max_examples=50)
def test_java::whilestatement_instantiation(instance):
    assert isinstance(instance, java::WhileStatement)

@given(instance=java::ThrowStatement_strategy)
@settings(max_examples=50)
def test_java::throwstatement_instantiation(instance):
    assert isinstance(instance, java::ThrowStatement)

@given(instance=java::ContinueStatement_strategy)
@settings(max_examples=50)
def test_java::continuestatement_instantiation(instance):
    assert isinstance(instance, java::ContinueStatement)

@given(instance=java::SwitchStatement_strategy)
@settings(max_examples=50)
def test_java::switchstatement_instantiation(instance):
    assert isinstance(instance, java::SwitchStatement)

@given(instance=java::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, java::VariableDeclarationStatement)

@given(instance=java::VariableDeclarationStatement_strategy)
def test_java::variabledeclarationstatement_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=java::VariableDeclarationStatement_strategy)
def test_java::variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java::EmptyStatement_strategy)
@settings(max_examples=50)
def test_java::emptystatement_instantiation(instance):
    assert isinstance(instance, java::EmptyStatement)

@given(instance=java::ForStatement_strategy)
@settings(max_examples=50)
def test_java::forstatement_instantiation(instance):
    assert isinstance(instance, java::ForStatement)

@given(instance=java::SwitchCase_strategy)
@settings(max_examples=50)
def test_java::switchcase_instantiation(instance):
    assert isinstance(instance, java::SwitchCase)

@given(instance=java::SwitchCase_strategy)
def test_java::switchcase_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=java::SwitchCase_strategy)
def test_java::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=java::TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java::typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, java::TypeDeclarationStatement)

@given(instance=java::IfStatement_strategy)
@settings(max_examples=50)
def test_java::ifstatement_instantiation(instance):
    assert isinstance(instance, java::IfStatement)

@given(instance=java::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java::constructorinvocation_instantiation(instance):
    assert isinstance(instance, java::ConstructorInvocation)

@given(instance=java::ReturnStatement_strategy)
@settings(max_examples=50)
def test_java::returnstatement_instantiation(instance):
    assert isinstance(instance, java::ReturnStatement)

@given(instance=java::CatchClause_strategy)
@settings(max_examples=50)
def test_java::catchclause_instantiation(instance):
    assert isinstance(instance, java::CatchClause)

@given(instance=java::AssertStatement_strategy)
@settings(max_examples=50)
def test_java::assertstatement_instantiation(instance):
    assert isinstance(instance, java::AssertStatement)

@given(instance=java::Manifest_strategy)
@settings(max_examples=50)
def test_java::manifest_instantiation(instance):
    assert isinstance(instance, java::Manifest)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=java::ClassFile_strategy)
@settings(max_examples=50)
def test_java::classfile_instantiation(instance):
    assert isinstance(instance, java::ClassFile)

@given(instance=java::ClassFile_strategy)
def test_java::classfile_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=java::ClassFile_strategy)
def test_java::classfile_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java::CompilationUnit_strategy)
@settings(max_examples=50)
def test_java::compilationunit_instantiation(instance):
    assert isinstance(instance, java::CompilationUnit)

@given(instance=java::CompilationUnit_strategy)
def test_java::compilationunit_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=java::CompilationUnit_strategy)
def test_java::compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::variabledeclaration_instantiation(instance):
    assert isinstance(instance, java::VariableDeclaration)

@given(instance=java::VariableDeclaration_strategy)
def test_java::variabledeclaration_extraArrayDimensions_type(instance):
    assert isinstance(instance.extraArrayDimensions, int)


@given(instance=java::VariableDeclaration_strategy)
def test_java::variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java::bodydeclaration_instantiation(instance):
    assert isinstance(instance, java::BodyDeclaration)

@given(instance=java::Type_strategy)
@settings(max_examples=50)
def test_java::type_instantiation(instance):
    assert isinstance(instance, java::Type)

@given(instance=java::UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java::unresolveditem_instantiation(instance):
    assert isinstance(instance, java::UnresolvedItem)

@given(instance=java::LabeledStatement_strategy)
@settings(max_examples=50)
def test_java::labeledstatement_instantiation(instance):
    assert isinstance(instance, java::LabeledStatement)

@given(instance=java::Archive_strategy)
@settings(max_examples=50)
def test_java::archive_instantiation(instance):
    assert isinstance(instance, java::Archive)

@given(instance=java::Archive_strategy)
def test_java::archive_originalFilePath_type(instance):
    assert isinstance(instance.originalFilePath, str)


@given(instance=java::Archive_strategy)
def test_java::archive_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java::AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java::annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, java::AnnotationMemberValuePair)

@given(instance=java::VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java::variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, java::VariableDeclarationFragment)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=java::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java::characterliteral_instantiation(instance):
    assert isinstance(instance, java::CharacterLiteral)

@given(instance=java::CharacterLiteral_strategy)
def test_java::characterliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=java::CharacterLiteral_strategy)
def test_java::characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=java::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java::conditionalexpression_instantiation(instance):
    assert isinstance(instance, java::ConditionalExpression)

@given(instance=java::NumberLiteral_strategy)
@settings(max_examples=50)
def test_java::numberliteral_instantiation(instance):
    assert isinstance(instance, java::NumberLiteral)

@given(instance=java::NumberLiteral_strategy)
def test_java::numberliteral_tokenValue_type(instance):
    assert isinstance(instance.tokenValue, str)


@given(instance=java::NumberLiteral_strategy)
def test_java::numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=java::CastExpression_strategy)
@settings(max_examples=50)
def test_java::castexpression_instantiation(instance):
    assert isinstance(instance, java::CastExpression)

@given(instance=java::Annotation_strategy)
@settings(max_examples=50)
def test_java::annotation_instantiation(instance):
    assert isinstance(instance, java::Annotation)

@given(instance=java::ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java::arraylengthaccess_instantiation(instance):
    assert isinstance(instance, java::ArrayLengthAccess)

@given(instance=java::PostfixExpression_strategy)
@settings(max_examples=50)
def test_java::postfixexpression_instantiation(instance):
    assert isinstance(instance, java::PostfixExpression)

@given(instance=java::PostfixExpression_strategy)
def test_java::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=java::PostfixExpression_strategy)
def test_java::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java::PrefixExpression_strategy)
@settings(max_examples=50)
def test_java::prefixexpression_instantiation(instance):
    assert isinstance(instance, java::PrefixExpression)

@given(instance=java::PrefixExpression_strategy)
def test_java::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=java::PrefixExpression_strategy)
def test_java::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java::ArrayCreation_strategy)
@settings(max_examples=50)
def test_java::arraycreation_instantiation(instance):
    assert isinstance(instance, java::ArrayCreation)

@given(instance=java::ArrayAccess_strategy)
@settings(max_examples=50)
def test_java::arrayaccess_instantiation(instance):
    assert isinstance(instance, java::ArrayAccess)

@given(instance=java::StringLiteral_strategy)
@settings(max_examples=50)
def test_java::stringliteral_instantiation(instance):
    assert isinstance(instance, java::StringLiteral)

@given(instance=java::StringLiteral_strategy)
def test_java::stringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=java::StringLiteral_strategy)
def test_java::stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=java::Assignment_strategy)
@settings(max_examples=50)
def test_java::assignment_instantiation(instance):
    assert isinstance(instance, java::Assignment)

@given(instance=java::Assignment_strategy)
def test_java::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=java::Assignment_strategy)
def test_java::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java::InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java::instanceofexpression_instantiation(instance):
    assert isinstance(instance, java::InstanceofExpression)

@given(instance=java::NullLiteral_strategy)
@settings(max_examples=50)
def test_java::nullliteral_instantiation(instance):
    assert isinstance(instance, java::NullLiteral)

@given(instance=java::UnresolvedItemAccess_strategy)
@settings(max_examples=50)
def test_java::unresolveditemaccess_instantiation(instance):
    assert isinstance(instance, java::UnresolvedItemAccess)

@given(instance=java::SingleVariableAccess_strategy)
@settings(max_examples=50)
def test_java::singlevariableaccess_instantiation(instance):
    assert isinstance(instance, java::SingleVariableAccess)

@given(instance=java::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, java::ParenthesizedExpression)

@given(instance=java::TypeLiteral_strategy)
@settings(max_examples=50)
def test_java::typeliteral_instantiation(instance):
    assert isinstance(instance, java::TypeLiteral)

@given(instance=java::MethodInvocation_strategy)
@settings(max_examples=50)
def test_java::methodinvocation_instantiation(instance):
    assert isinstance(instance, java::MethodInvocation)

@given(instance=java::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java::classinstancecreation_instantiation(instance):
    assert isinstance(instance, java::ClassInstanceCreation)

@given(instance=java::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java::arrayinitializer_instantiation(instance):
    assert isinstance(instance, java::ArrayInitializer)

@given(instance=java::InfixExpression_strategy)
@settings(max_examples=50)
def test_java::infixexpression_instantiation(instance):
    assert isinstance(instance, java::InfixExpression)

@given(instance=java::InfixExpression_strategy)
def test_java::infixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=java::InfixExpression_strategy)
def test_java::infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java::booleanliteral_instantiation(instance):
    assert isinstance(instance, java::BooleanLiteral)

@given(instance=java::BooleanLiteral_strategy)
def test_java::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=java::BooleanLiteral_strategy)
def test_java::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java::FieldAccess_strategy)
@settings(max_examples=50)
def test_java::fieldaccess_instantiation(instance):
    assert isinstance(instance, java::FieldAccess)

@given(instance=java::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, java::VariableDeclarationExpression)

@given(instance=java::AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_java::abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, java::AbstractTypeQualifiedExpression)

@given(instance=java::Package_strategy)
@settings(max_examples=50)
def test_java::package_instantiation(instance):
    assert isinstance(instance, java::Package)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=java::ArrayType_strategy)
@settings(max_examples=50)
def test_java::arraytype_instantiation(instance):
    assert isinstance(instance, java::ArrayType)

@given(instance=java::ArrayType_strategy)
def test_java::arraytype_dimensions_type(instance):
    assert isinstance(instance.dimensions, int)


@given(instance=java::ArrayType_strategy)
def test_java::arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=java::ParameterizedType_strategy)
@settings(max_examples=50)
def test_java::parameterizedtype_instantiation(instance):
    assert isinstance(instance, java::ParameterizedType)

@given(instance=java::PrimitiveType_strategy)
@settings(max_examples=50)
def test_java::primitivetype_instantiation(instance):
    assert isinstance(instance, java::PrimitiveType)

@given(instance=java::WildCardType_strategy)
@settings(max_examples=50)
def test_java::wildcardtype_instantiation(instance):
    assert isinstance(instance, java::WildCardType)

@given(instance=java::WildCardType_strategy)
def test_java::wildcardtype_upperBound_type(instance):
    assert isinstance(instance.upperBound, bool)


@given(instance=java::WildCardType_strategy)
def test_java::wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=java::UnresolvedType_strategy)
@settings(max_examples=50)
def test_java::unresolvedtype_instantiation(instance):
    assert isinstance(instance, java::UnresolvedType)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=java::Statement_strategy)
@settings(max_examples=50)
def test_java::statement_instantiation(instance):
    assert isinstance(instance, java::Statement)

@given(instance=java::TagElement_strategy)
@settings(max_examples=50)
def test_java::tagelement_instantiation(instance):
    assert isinstance(instance, java::TagElement)

@given(instance=java::TagElement_strategy)
def test_java::tagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=java::TagElement_strategy)
def test_java::tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=java::Modifier_strategy)
@settings(max_examples=50)
def test_java::modifier_instantiation(instance):
    assert isinstance(instance, java::Modifier)

@given(instance=java::Modifier_strategy)
def test_java::modifier_native_type(instance):
    assert isinstance(instance.native, bool)


@given(instance=java::Modifier_strategy)
def test_java::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=java::Modifier_strategy)
def test_java::modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=java::Modifier_strategy)
def test_java::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, bool)


@given(instance=java::Modifier_strategy)
def test_java::modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=java::Modifier_strategy)
def test_java::modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_volatile_type(instance):
    assert isinstance(instance.volatile, bool)


@given(instance=java::Modifier_strategy)
def test_java::modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=java::Modifier_strategy)
def test_java::modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=java::Modifier_strategy)
def test_java::modifier_inheritance_type(instance):
    assert isinstance(instance.inheritance, str)


@given(instance=java::Modifier_strategy)
def test_java::modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=java::NamespaceAccess_strategy)
@settings(max_examples=50)
def test_java::namespaceaccess_instantiation(instance):
    assert isinstance(instance, java::NamespaceAccess)

@given(instance=java::Comment_strategy)
@settings(max_examples=50)
def test_java::comment_instantiation(instance):
    assert isinstance(instance, java::Comment)

@given(instance=java::Comment_strategy)
def test_java::comment_enclosedByParent_type(instance):
    assert isinstance(instance.enclosedByParent, bool)


@given(instance=java::Comment_strategy)
def test_java::comment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original

@given(instance=java::Comment_strategy)
def test_java::comment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=java::Comment_strategy)
def test_java::comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=java::Comment_strategy)
def test_java::comment_prefixOfParent_type(instance):
    assert isinstance(instance.prefixOfParent, bool)


@given(instance=java::Comment_strategy)
def test_java::comment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original

@given(instance=java::Expression_strategy)
@settings(max_examples=50)
def test_java::expression_instantiation(instance):
    assert isinstance(instance, java::Expression)

@given(instance=java::AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, java::AnonymousClassDeclaration)

@given(instance=java::TextElement_strategy)
@settings(max_examples=50)
def test_java::textelement_instantiation(instance):
    assert isinstance(instance, java::TextElement)

@given(instance=java::TextElement_strategy)
def test_java::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=java::TextElement_strategy)
def test_java::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=java::MemberRef_strategy)
@settings(max_examples=50)
def test_java::memberref_instantiation(instance):
    assert isinstance(instance, java::MemberRef)

@given(instance=java::MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java::methodrefparameter_instantiation(instance):
    assert isinstance(instance, java::MethodRefParameter)

@given(instance=java::MethodRefParameter_strategy)
def test_java::methodrefparameter_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=java::MethodRefParameter_strategy)
def test_java::methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=java::MethodRefParameter_strategy)
def test_java::methodrefparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::MethodRefParameter_strategy)
def test_java::methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java::importdeclaration_instantiation(instance):
    assert isinstance(instance, java::ImportDeclaration)

@given(instance=java::ImportDeclaration_strategy)
def test_java::importdeclaration_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=java::ImportDeclaration_strategy)
def test_java::importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=java::AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_java::abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, java::AbstractVariablesContainer)

@given(instance=java::NamedElement_strategy)
@settings(max_examples=50)
def test_java::namedelement_instantiation(instance):
    assert isinstance(instance, java::NamedElement)

@given(instance=java::NamedElement_strategy)
def test_java::namedelement_proxy_type(instance):
    assert isinstance(instance.proxy, bool)


@given(instance=java::NamedElement_strategy)
def test_java::namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=java::NamedElement_strategy)
def test_java::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::NamedElement_strategy)
def test_java::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_java::abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, java::AbstractMethodInvocation)

@given(instance=java::MethodRef_strategy)
@settings(max_examples=50)
def test_java::methodref_instantiation(instance):
    assert isinstance(instance, java::MethodRef)

@given(instance=java::TypeParameter_strategy)
@settings(max_examples=50)
def test_java::typeparameter_instantiation(instance):
    assert isinstance(instance, java::TypeParameter)

@given(instance=java::TypeAccess_strategy)
@settings(max_examples=50)
def test_java::typeaccess_instantiation(instance):
    assert isinstance(instance, java::TypeAccess)

@given(instance=java::SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, java::SingleVariableDeclaration)

@given(instance=java::SingleVariableDeclaration_strategy)
def test_java::singlevariabledeclaration_varargs_type(instance):
    assert isinstance(instance.varargs, bool)


@given(instance=java::SingleVariableDeclaration_strategy)
def test_java::singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=java::Block_strategy)
@settings(max_examples=50)
def test_java::block_instantiation(instance):
    assert isinstance(instance, java::Block)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=java::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, java::AbstractTypeDeclaration)

@given(instance=java::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java::fielddeclaration_instantiation(instance):
    assert isinstance(instance, java::FieldDeclaration)

@given(instance=java::Initializer_strategy)
@settings(max_examples=50)
def test_java::initializer_instantiation(instance):
    assert isinstance(instance, java::Initializer)

@given(instance=java::EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java::enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, java::EnumConstantDeclaration)

@given(instance=java::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, java::AnnotationTypeMemberDeclaration)

@given(instance=java::AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java::abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, java::AbstractMethodDeclaration)
