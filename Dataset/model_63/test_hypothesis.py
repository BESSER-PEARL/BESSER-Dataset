import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AnnotationTypeMemberDeclaration,
    UnresolvedItem,
    Java_UnresolvedAnnotationTypeMemberDeclaration,
    AnnotationTypeDeclaration,
    Java_UnresolvedAnnotationDeclaration,
    AbstractTypeQualifiedExpression,
    Java_ThisExpression,
    Java_SuperFieldAccess,
    PrimitiveType,
    Java_PrimitiveTypeChar,
    Java_PrimitiveTypeShort,
    Java_PrimitiveTypeDouble,
    Java_PrimitiveTypeVoid,
    Java_PrimitiveTypeLong,
    Java_PrimitiveTypeByte,
    Java_PrimitiveTypeInt,
    Java_PrimitiveTypeFloat,
    Java_PrimitiveTypeBoolean,
    NamespaceAccess,
    Java_PackageAccess,
    Java_Model,
    Java_ManifestEntry,
    Java_ManifestAttribute,
    MethodDeclaration,
    Java_UnresolvedMethodDeclaration,
    LabeledStatement,
    Java_UnresolvedLabeledStatement,
    InterfaceDeclaration,
    Java_UnresolvedInterfaceDeclaration,
    EnumDeclaration,
    Java_UnresolvedEnumDeclaration,
    VariableDeclarationFragment,
    Java_UnresolvedVariableDeclarationFragment,
    SingleVariableDeclaration,
    Java_UnresolvedSingleVariableDeclaration,
    ClassDeclaration,
    Java_UnresolvedClassDeclaration,
    VariableDeclaration,
    AbstractVariablesContainer,
    TypeDeclaration,
    Java_InterfaceDeclaration,
    Java_ClassDeclaration,
    AbstractMethodDeclaration,
    Java_MethodDeclaration,
    Java_ConstructorDeclaration,
    AbstractMethodInvocation,
    Java_SuperMethodInvocation,
    Comment,
    Java_LineComment,
    Java_Javadoc,
    Java_BlockComment,
    Java_VariableDeclarationFragment,
    AbstractTypeDeclaration,
    Java_UnresolvedTypeDeclaration,
    Java_TypeDeclaration,
    Java_EnumDeclaration,
    Java_AnnotationTypeDeclaration,
    Java_ASTNode,
    Statement,
    Java_VariableDeclarationStatement,
    Java_ThrowStatement,
    Java_EnhancedForStatement,
    Java_CatchClause,
    Java_TypeDeclarationStatement,
    Java_ExpressionStatement,
    Java_SuperConstructorInvocation,
    Java_SwitchStatement,
    Java_SwitchCase,
    Java_EmptyStatement,
    Java_ReturnStatement,
    Java_SynchronizedStatement,
    Java_ContinueStatement,
    Java_DoStatement,
    Java_ConstructorInvocation,
    Java_ForStatement,
    Java_BreakStatement,
    Java_WhileStatement,
    Java_IfStatement,
    Java_TryStatement,
    Java_AssertStatement,
    Java_Manifest,
    NamedElement,
    Java_UnresolvedItem,
    Java_CompilationUnit,
    Java_ClassFile,
    Java_Type,
    Java_LabeledStatement,
    Java_VariableDeclaration,
    Java_Archive,
    Java_AnnotationMemberValuePair,
    Java_SingleVariableDeclaration,
    Expression,
    Java_CharacterLiteral,
    Java_ClassInstanceCreation,
    Java_VariableDeclarationExpression,
    Java_TypeAccess,
    Java_NumberLiteral,
    Java_BooleanLiteral,
    Java_ArrayLengthAccess,
    Java_ArrayAccess,
    Java_ArrayInitializer,
    Java_ConditionalExpression,
    Java_ArrayCreation,
    Java_Annotation,
    Java_MethodInvocation,
    Java_Assignment,
    Java_NullLiteral,
    Java_InstanceofExpression,
    Java_PostfixExpression,
    Java_CastExpression,
    Java_StringLiteral,
    Java_UnresolvedItemAccess,
    Java_SingleVariableAccess,
    Java_InfixExpression,
    Java_FieldAccess,
    Java_TypeLiteral,
    Java_PrefixExpression,
    Java_ParenthesizedExpression,
    Java_AbstractTypeQualifiedExpression,
    Java_Package,
    Java_BodyDeclaration,
    Type,
    Java_WildCardType,
    Java_ParameterizedType,
    Java_UnresolvedType,
    Java_PrimitiveType,
    Java_TypeParameter,
    Java_ArrayType,
    ASTNode,
    Java_NamedElement,
    Java_ImportDeclaration,
    Java_Comment,
    Java_Statement,
    Java_TagElement,
    Java_TextElement,
    Java_MethodRefParameter,
    Java_MemberRef,
    Java_Modifier,
    Java_AnonymousClassDeclaration,
    Java_MethodRef,
    Java_Expression,
    Java_AbstractVariablesContainer,
    Java_NamespaceAccess,
    Java_AbstractMethodInvocation,
    Java_Block,
    BodyDeclaration,
    Java_EnumConstantDeclaration,
    Java_AnnotationTypeMemberDeclaration,
    Java_FieldDeclaration,
    Java_Initializer,
    Java_AbstractTypeDeclaration,
    Java_AbstractMethodDeclaration,
    PrefixExpressionKind,
    VisibilityKind,
    InheritanceKind,
    PostfixExpressionKind,
    InfixExpressionKind,
    AssignmentKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_java_unresolvedannotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedAnnotationTypeMemberDeclaration)


def test_java_unresolvedannotationtypememberdeclaration_constructor_exists():
    assert callable(Java_UnresolvedAnnotationTypeMemberDeclaration.__init__)


def test_java_unresolvedannotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedAnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AnnotationTypeDeclaration)


def test_annotationtypedeclaration_constructor_exists():
    assert callable(AnnotationTypeDeclaration.__init__)


def test_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedannotationdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedAnnotationDeclaration)


def test_java_unresolvedannotationdeclaration_constructor_exists():
    assert callable(Java_UnresolvedAnnotationDeclaration.__init__)


def test_java_unresolvedannotationdeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedAnnotationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeQualifiedExpression)


def test_abstracttypequalifiedexpression_constructor_exists():
    assert callable(AbstractTypeQualifiedExpression.__init__)


def test_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_thisexpression_is_not_abstract():
    assert not inspect.isabstract(Java_ThisExpression)


def test_java_thisexpression_constructor_exists():
    assert callable(Java_ThisExpression.__init__)


def test_java_thisexpression_constructor_args():
    sig = inspect.signature(Java_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java_SuperFieldAccess)


def test_java_superfieldaccess_constructor_exists():
    assert callable(Java_SuperFieldAccess.__init__)


def test_java_superfieldaccess_constructor_args():
    sig = inspect.signature(Java_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeChar)


def test_java_primitivetypechar_constructor_exists():
    assert callable(Java_PrimitiveTypeChar.__init__)


def test_java_primitivetypechar_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeShort)


def test_java_primitivetypeshort_constructor_exists():
    assert callable(Java_PrimitiveTypeShort.__init__)


def test_java_primitivetypeshort_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeDouble)


def test_java_primitivetypedouble_constructor_exists():
    assert callable(Java_PrimitiveTypeDouble.__init__)


def test_java_primitivetypedouble_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeVoid)


def test_java_primitivetypevoid_constructor_exists():
    assert callable(Java_PrimitiveTypeVoid.__init__)


def test_java_primitivetypevoid_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeLong)


def test_java_primitivetypelong_constructor_exists():
    assert callable(Java_PrimitiveTypeLong.__init__)


def test_java_primitivetypelong_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeByte)


def test_java_primitivetypebyte_constructor_exists():
    assert callable(Java_PrimitiveTypeByte.__init__)


def test_java_primitivetypebyte_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeInt)


def test_java_primitivetypeint_constructor_exists():
    assert callable(Java_PrimitiveTypeInt.__init__)


def test_java_primitivetypeint_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeFloat)


def test_java_primitivetypefloat_constructor_exists():
    assert callable(Java_PrimitiveTypeFloat.__init__)


def test_java_primitivetypefloat_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveTypeBoolean)


def test_java_primitivetypeboolean_constructor_exists():
    assert callable(Java_PrimitiveTypeBoolean.__init__)


def test_java_primitivetypeboolean_constructor_args():
    sig = inspect.signature(Java_PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_packageaccess_is_not_abstract():
    assert not inspect.isabstract(Java_PackageAccess)


def test_java_packageaccess_constructor_exists():
    assert callable(Java_PackageAccess.__init__)


def test_java_packageaccess_constructor_args():
    sig = inspect.signature(Java_PackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_model_is_not_abstract():
    assert not inspect.isabstract(Java_Model)


def test_java_model_constructor_exists():
    assert callable(Java_Model.__init__)


def test_java_model_constructor_args():
    sig = inspect.signature(Java_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_model_has_name():
    assert hasattr(Java_Model, "name")
    descriptor = None
    for klass in Java_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_manifestentry_is_not_abstract():
    assert not inspect.isabstract(Java_ManifestEntry)


def test_java_manifestentry_constructor_exists():
    assert callable(Java_ManifestEntry.__init__)


def test_java_manifestentry_constructor_args():
    sig = inspect.signature(Java_ManifestEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_manifestentry_has_name():
    assert hasattr(Java_ManifestEntry, "name")
    descriptor = None
    for klass in Java_ManifestEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_manifestattribute_is_not_abstract():
    assert not inspect.isabstract(Java_ManifestAttribute)


def test_java_manifestattribute_constructor_exists():
    assert callable(Java_ManifestAttribute.__init__)


def test_java_manifestattribute_constructor_args():
    sig = inspect.signature(Java_ManifestAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_java_manifestattribute_has_key():
    assert hasattr(Java_ManifestAttribute, "key")
    descriptor = None
    for klass in Java_ManifestAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_java_manifestattribute_has_value():
    assert hasattr(Java_ManifestAttribute, "value")
    descriptor = None
    for klass in Java_ManifestAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(MethodDeclaration)


def test_methoddeclaration_constructor_exists():
    assert callable(MethodDeclaration.__init__)


def test_methoddeclaration_constructor_args():
    sig = inspect.signature(MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedMethodDeclaration)


def test_java_unresolvedmethoddeclaration_constructor_exists():
    assert callable(Java_UnresolvedMethodDeclaration.__init__)


def test_java_unresolvedmethoddeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(LabeledStatement)


def test_labeledstatement_constructor_exists():
    assert callable(LabeledStatement.__init__)


def test_labeledstatement_constructor_args():
    sig = inspect.signature(LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedlabeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedLabeledStatement)


def test_java_unresolvedlabeledstatement_constructor_exists():
    assert callable(Java_UnresolvedLabeledStatement.__init__)


def test_java_unresolvedlabeledstatement_constructor_args():
    sig = inspect.signature(Java_UnresolvedLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(InterfaceDeclaration)


def test_interfacedeclaration_constructor_exists():
    assert callable(InterfaceDeclaration.__init__)


def test_interfacedeclaration_constructor_args():
    sig = inspect.signature(InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedInterfaceDeclaration)


def test_java_unresolvedinterfacedeclaration_constructor_exists():
    assert callable(Java_UnresolvedInterfaceDeclaration.__init__)


def test_java_unresolvedinterfacedeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumDeclaration)


def test_enumdeclaration_constructor_exists():
    assert callable(EnumDeclaration.__init__)


def test_enumdeclaration_constructor_args():
    sig = inspect.signature(EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedenumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedEnumDeclaration)


def test_java_unresolvedenumdeclaration_constructor_exists():
    assert callable(Java_UnresolvedEnumDeclaration.__init__)


def test_java_unresolvedenumdeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedEnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationFragment)


def test_variabledeclarationfragment_constructor_exists():
    assert callable(VariableDeclarationFragment.__init__)


def test_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedVariableDeclarationFragment)


def test_java_unresolvedvariabledeclarationfragment_constructor_exists():
    assert callable(Java_UnresolvedVariableDeclarationFragment.__init__)


def test_java_unresolvedvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java_UnresolvedVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedSingleVariableDeclaration)


def test_java_unresolvedsinglevariabledeclaration_constructor_exists():
    assert callable(Java_UnresolvedSingleVariableDeclaration.__init__)


def test_java_unresolvedsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassDeclaration)


def test_classdeclaration_constructor_exists():
    assert callable(ClassDeclaration.__init__)


def test_classdeclaration_constructor_args():
    sig = inspect.signature(ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedClassDeclaration)


def test_java_unresolvedclassdeclaration_constructor_exists():
    assert callable(Java_UnresolvedClassDeclaration.__init__)


def test_java_unresolvedclassdeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedClassDeclaration.__init__)
    params = list(sig.parameters.keys())



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



def test_java_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_InterfaceDeclaration)


def test_java_interfacedeclaration_constructor_exists():
    assert callable(Java_InterfaceDeclaration.__init__)


def test_java_interfacedeclaration_constructor_args():
    sig = inspect.signature(Java_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_ClassDeclaration)


def test_java_classdeclaration_constructor_exists():
    assert callable(Java_ClassDeclaration.__init__)


def test_java_classdeclaration_constructor_args():
    sig = inspect.signature(Java_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_MethodDeclaration)


def test_java_methoddeclaration_constructor_exists():
    assert callable(Java_MethodDeclaration.__init__)


def test_java_methoddeclaration_constructor_args():
    sig = inspect.signature(Java_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java_methoddeclaration_has_extraArrayDimensions():
    assert hasattr(Java_MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java_MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_ConstructorDeclaration)


def test_java_constructordeclaration_constructor_exists():
    assert callable(Java_ConstructorDeclaration.__init__)


def test_java_constructordeclaration_constructor_args():
    sig = inspect.signature(Java_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodInvocation)


def test_abstractmethodinvocation_constructor_exists():
    assert callable(AbstractMethodInvocation.__init__)


def test_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java_SuperMethodInvocation)


def test_java_supermethodinvocation_constructor_exists():
    assert callable(Java_SuperMethodInvocation.__init__)


def test_java_supermethodinvocation_constructor_args():
    sig = inspect.signature(Java_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_java_linecomment_is_not_abstract():
    assert not inspect.isabstract(Java_LineComment)


def test_java_linecomment_constructor_exists():
    assert callable(Java_LineComment.__init__)


def test_java_linecomment_constructor_args():
    sig = inspect.signature(Java_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_java_javadoc_is_not_abstract():
    assert not inspect.isabstract(Java_Javadoc)


def test_java_javadoc_constructor_exists():
    assert callable(Java_Javadoc.__init__)


def test_java_javadoc_constructor_args():
    sig = inspect.signature(Java_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_java_blockcomment_is_not_abstract():
    assert not inspect.isabstract(Java_BlockComment)


def test_java_blockcomment_constructor_exists():
    assert callable(Java_BlockComment.__init__)


def test_java_blockcomment_constructor_args():
    sig = inspect.signature(Java_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java_VariableDeclarationFragment)


def test_java_variabledeclarationfragment_constructor_exists():
    assert callable(Java_VariableDeclarationFragment.__init__)


def test_java_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedTypeDeclaration)


def test_java_unresolvedtypedeclaration_constructor_exists():
    assert callable(Java_UnresolvedTypeDeclaration.__init__)


def test_java_unresolvedtypedeclaration_constructor_args():
    sig = inspect.signature(Java_UnresolvedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_TypeDeclaration)


def test_java_typedeclaration_constructor_exists():
    assert callable(Java_TypeDeclaration.__init__)


def test_java_typedeclaration_constructor_args():
    sig = inspect.signature(Java_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_EnumDeclaration)


def test_java_enumdeclaration_constructor_exists():
    assert callable(Java_EnumDeclaration.__init__)


def test_java_enumdeclaration_constructor_args():
    sig = inspect.signature(Java_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_AnnotationTypeDeclaration)


def test_java_annotationtypedeclaration_constructor_exists():
    assert callable(Java_AnnotationTypeDeclaration.__init__)


def test_java_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(Java_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_astnode_is_not_abstract():
    assert not inspect.isabstract(Java_ASTNode)


def test_java_astnode_constructor_exists():
    assert callable(Java_ASTNode.__init__)


def test_java_astnode_constructor_args():
    sig = inspect.signature(Java_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java_VariableDeclarationStatement)


def test_java_variabledeclarationstatement_constructor_exists():
    assert callable(Java_VariableDeclarationStatement.__init__)


def test_java_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(Java_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java_variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(Java_VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in Java_VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_throwstatement_is_not_abstract():
    assert not inspect.isabstract(Java_ThrowStatement)


def test_java_throwstatement_constructor_exists():
    assert callable(Java_ThrowStatement.__init__)


def test_java_throwstatement_constructor_args():
    sig = inspect.signature(Java_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(Java_EnhancedForStatement)


def test_java_enhancedforstatement_constructor_exists():
    assert callable(Java_EnhancedForStatement.__init__)


def test_java_enhancedforstatement_constructor_args():
    sig = inspect.signature(Java_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_catchclause_is_not_abstract():
    assert not inspect.isabstract(Java_CatchClause)


def test_java_catchclause_constructor_exists():
    assert callable(Java_CatchClause.__init__)


def test_java_catchclause_constructor_args():
    sig = inspect.signature(Java_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java_TypeDeclarationStatement)


def test_java_typedeclarationstatement_constructor_exists():
    assert callable(Java_TypeDeclarationStatement.__init__)


def test_java_typedeclarationstatement_constructor_args():
    sig = inspect.signature(Java_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(Java_ExpressionStatement)


def test_java_expressionstatement_constructor_exists():
    assert callable(Java_ExpressionStatement.__init__)


def test_java_expressionstatement_constructor_args():
    sig = inspect.signature(Java_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java_SuperConstructorInvocation)


def test_java_superconstructorinvocation_constructor_exists():
    assert callable(Java_SuperConstructorInvocation.__init__)


def test_java_superconstructorinvocation_constructor_args():
    sig = inspect.signature(Java_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_switchstatement_is_not_abstract():
    assert not inspect.isabstract(Java_SwitchStatement)


def test_java_switchstatement_constructor_exists():
    assert callable(Java_SwitchStatement.__init__)


def test_java_switchstatement_constructor_args():
    sig = inspect.signature(Java_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_switchcase_is_not_abstract():
    assert not inspect.isabstract(Java_SwitchCase)


def test_java_switchcase_constructor_exists():
    assert callable(Java_SwitchCase.__init__)


def test_java_switchcase_constructor_args():
    sig = inspect.signature(Java_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java_switchcase_has_default():
    assert hasattr(Java_SwitchCase, "default")
    descriptor = None
    for klass in Java_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java_emptystatement_is_not_abstract():
    assert not inspect.isabstract(Java_EmptyStatement)


def test_java_emptystatement_constructor_exists():
    assert callable(Java_EmptyStatement.__init__)


def test_java_emptystatement_constructor_args():
    sig = inspect.signature(Java_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_returnstatement_is_not_abstract():
    assert not inspect.isabstract(Java_ReturnStatement)


def test_java_returnstatement_constructor_exists():
    assert callable(Java_ReturnStatement.__init__)


def test_java_returnstatement_constructor_args():
    sig = inspect.signature(Java_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(Java_SynchronizedStatement)


def test_java_synchronizedstatement_constructor_exists():
    assert callable(Java_SynchronizedStatement.__init__)


def test_java_synchronizedstatement_constructor_args():
    sig = inspect.signature(Java_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_continuestatement_is_not_abstract():
    assert not inspect.isabstract(Java_ContinueStatement)


def test_java_continuestatement_constructor_exists():
    assert callable(Java_ContinueStatement.__init__)


def test_java_continuestatement_constructor_args():
    sig = inspect.signature(Java_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_dostatement_is_not_abstract():
    assert not inspect.isabstract(Java_DoStatement)


def test_java_dostatement_constructor_exists():
    assert callable(Java_DoStatement.__init__)


def test_java_dostatement_constructor_args():
    sig = inspect.signature(Java_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java_ConstructorInvocation)


def test_java_constructorinvocation_constructor_exists():
    assert callable(Java_ConstructorInvocation.__init__)


def test_java_constructorinvocation_constructor_args():
    sig = inspect.signature(Java_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_forstatement_is_not_abstract():
    assert not inspect.isabstract(Java_ForStatement)


def test_java_forstatement_constructor_exists():
    assert callable(Java_ForStatement.__init__)


def test_java_forstatement_constructor_args():
    sig = inspect.signature(Java_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_breakstatement_is_not_abstract():
    assert not inspect.isabstract(Java_BreakStatement)


def test_java_breakstatement_constructor_exists():
    assert callable(Java_BreakStatement.__init__)


def test_java_breakstatement_constructor_args():
    sig = inspect.signature(Java_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_whilestatement_is_not_abstract():
    assert not inspect.isabstract(Java_WhileStatement)


def test_java_whilestatement_constructor_exists():
    assert callable(Java_WhileStatement.__init__)


def test_java_whilestatement_constructor_args():
    sig = inspect.signature(Java_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_ifstatement_is_not_abstract():
    assert not inspect.isabstract(Java_IfStatement)


def test_java_ifstatement_constructor_exists():
    assert callable(Java_IfStatement.__init__)


def test_java_ifstatement_constructor_args():
    sig = inspect.signature(Java_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_trystatement_is_not_abstract():
    assert not inspect.isabstract(Java_TryStatement)


def test_java_trystatement_constructor_exists():
    assert callable(Java_TryStatement.__init__)


def test_java_trystatement_constructor_args():
    sig = inspect.signature(Java_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_assertstatement_is_not_abstract():
    assert not inspect.isabstract(Java_AssertStatement)


def test_java_assertstatement_constructor_exists():
    assert callable(Java_AssertStatement.__init__)


def test_java_assertstatement_constructor_args():
    sig = inspect.signature(Java_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_manifest_is_not_abstract():
    assert not inspect.isabstract(Java_Manifest)


def test_java_manifest_constructor_exists():
    assert callable(Java_Manifest.__init__)


def test_java_manifest_constructor_args():
    sig = inspect.signature(Java_Manifest.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedItem)


def test_java_unresolveditem_constructor_exists():
    assert callable(Java_UnresolvedItem.__init__)


def test_java_unresolveditem_constructor_args():
    sig = inspect.signature(Java_UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java_compilationunit_is_not_abstract():
    assert not inspect.isabstract(Java_CompilationUnit)


def test_java_compilationunit_constructor_exists():
    assert callable(Java_CompilationUnit.__init__)


def test_java_compilationunit_constructor_args():
    sig = inspect.signature(Java_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java_compilationunit_has_originalFilePath():
    assert hasattr(Java_CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in Java_CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java_classfile_is_not_abstract():
    assert not inspect.isabstract(Java_ClassFile)


def test_java_classfile_constructor_exists():
    assert callable(Java_ClassFile.__init__)


def test_java_classfile_constructor_args():
    sig = inspect.signature(Java_ClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java_classfile_has_originalFilePath():
    assert hasattr(Java_ClassFile, "originalFilePath")
    descriptor = None
    for klass in Java_ClassFile.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java_type_is_not_abstract():
    assert not inspect.isabstract(Java_Type)


def test_java_type_constructor_exists():
    assert callable(Java_Type.__init__)


def test_java_type_constructor_args():
    sig = inspect.signature(Java_Type.__init__)
    params = list(sig.parameters.keys())



def test_java_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java_LabeledStatement)


def test_java_labeledstatement_constructor_exists():
    assert callable(Java_LabeledStatement.__init__)


def test_java_labeledstatement_constructor_args():
    sig = inspect.signature(Java_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_VariableDeclaration)


def test_java_variabledeclaration_constructor_exists():
    assert callable(Java_VariableDeclaration.__init__)


def test_java_variabledeclaration_constructor_args():
    sig = inspect.signature(Java_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java_variabledeclaration_has_extraArrayDimensions():
    assert hasattr(Java_VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java_VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_archive_is_not_abstract():
    assert not inspect.isabstract(Java_Archive)


def test_java_archive_constructor_exists():
    assert callable(Java_Archive.__init__)


def test_java_archive_constructor_args():
    sig = inspect.signature(Java_Archive.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java_archive_has_originalFilePath():
    assert hasattr(Java_Archive, "originalFilePath")
    descriptor = None
    for klass in Java_Archive.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java_annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(Java_AnnotationMemberValuePair)


def test_java_annotationmembervaluepair_constructor_exists():
    assert callable(Java_AnnotationMemberValuePair.__init__)


def test_java_annotationmembervaluepair_constructor_args():
    sig = inspect.signature(Java_AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_java_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_SingleVariableDeclaration)


def test_java_singlevariabledeclaration_constructor_exists():
    assert callable(Java_SingleVariableDeclaration.__init__)


def test_java_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(Java_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java_singlevariabledeclaration_has_varargs():
    assert hasattr(Java_SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in Java_SingleVariableDeclaration.__mro__:
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



def test_java_characterliteral_is_not_abstract():
    assert not inspect.isabstract(Java_CharacterLiteral)


def test_java_characterliteral_constructor_exists():
    assert callable(Java_CharacterLiteral.__init__)


def test_java_characterliteral_constructor_args():
    sig = inspect.signature(Java_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java_characterliteral_has_escapedValue():
    assert hasattr(Java_CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in Java_CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(Java_ClassInstanceCreation)


def test_java_classinstancecreation_constructor_exists():
    assert callable(Java_ClassInstanceCreation.__init__)


def test_java_classinstancecreation_constructor_args():
    sig = inspect.signature(Java_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Java_VariableDeclarationExpression)


def test_java_variabledeclarationexpression_constructor_exists():
    assert callable(Java_VariableDeclarationExpression.__init__)


def test_java_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(Java_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_typeaccess_is_not_abstract():
    assert not inspect.isabstract(Java_TypeAccess)


def test_java_typeaccess_constructor_exists():
    assert callable(Java_TypeAccess.__init__)


def test_java_typeaccess_constructor_args():
    sig = inspect.signature(Java_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_numberliteral_is_not_abstract():
    assert not inspect.isabstract(Java_NumberLiteral)


def test_java_numberliteral_constructor_exists():
    assert callable(Java_NumberLiteral.__init__)


def test_java_numberliteral_constructor_args():
    sig = inspect.signature(Java_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java_numberliteral_has_tokenValue():
    assert hasattr(Java_NumberLiteral, "tokenValue")
    descriptor = None
    for klass in Java_NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(Java_BooleanLiteral)


def test_java_booleanliteral_constructor_exists():
    assert callable(Java_BooleanLiteral.__init__)


def test_java_booleanliteral_constructor_args():
    sig = inspect.signature(Java_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java_booleanliteral_has_value():
    assert hasattr(Java_BooleanLiteral, "value")
    descriptor = None
    for klass in Java_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java_arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(Java_ArrayLengthAccess)


def test_java_arraylengthaccess_constructor_exists():
    assert callable(Java_ArrayLengthAccess.__init__)


def test_java_arraylengthaccess_constructor_args():
    sig = inspect.signature(Java_ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(Java_ArrayAccess)


def test_java_arrayaccess_constructor_exists():
    assert callable(Java_ArrayAccess.__init__)


def test_java_arrayaccess_constructor_args():
    sig = inspect.signature(Java_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Java_ArrayInitializer)


def test_java_arrayinitializer_constructor_exists():
    assert callable(Java_ArrayInitializer.__init__)


def test_java_arrayinitializer_constructor_args():
    sig = inspect.signature(Java_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(Java_ConditionalExpression)


def test_java_conditionalexpression_constructor_exists():
    assert callable(Java_ConditionalExpression.__init__)


def test_java_conditionalexpression_constructor_args():
    sig = inspect.signature(Java_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_arraycreation_is_not_abstract():
    assert not inspect.isabstract(Java_ArrayCreation)


def test_java_arraycreation_constructor_exists():
    assert callable(Java_ArrayCreation.__init__)


def test_java_arraycreation_constructor_args():
    sig = inspect.signature(Java_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java_annotation_is_not_abstract():
    assert not inspect.isabstract(Java_Annotation)


def test_java_annotation_constructor_exists():
    assert callable(Java_Annotation.__init__)


def test_java_annotation_constructor_args():
    sig = inspect.signature(Java_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java_MethodInvocation)


def test_java_methodinvocation_constructor_exists():
    assert callable(Java_MethodInvocation.__init__)


def test_java_methodinvocation_constructor_args():
    sig = inspect.signature(Java_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_assignment_is_not_abstract():
    assert not inspect.isabstract(Java_Assignment)


def test_java_assignment_constructor_exists():
    assert callable(Java_Assignment.__init__)


def test_java_assignment_constructor_args():
    sig = inspect.signature(Java_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_assignment_has_operator():
    assert hasattr(Java_Assignment, "operator")
    descriptor = None
    for klass in Java_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_nullliteral_is_not_abstract():
    assert not inspect.isabstract(Java_NullLiteral)


def test_java_nullliteral_constructor_exists():
    assert callable(Java_NullLiteral.__init__)


def test_java_nullliteral_constructor_args():
    sig = inspect.signature(Java_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(Java_InstanceofExpression)


def test_java_instanceofexpression_constructor_exists():
    assert callable(Java_InstanceofExpression.__init__)


def test_java_instanceofexpression_constructor_args():
    sig = inspect.signature(Java_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(Java_PostfixExpression)


def test_java_postfixexpression_constructor_exists():
    assert callable(Java_PostfixExpression.__init__)


def test_java_postfixexpression_constructor_args():
    sig = inspect.signature(Java_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_postfixexpression_has_operator():
    assert hasattr(Java_PostfixExpression, "operator")
    descriptor = None
    for klass in Java_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_castexpression_is_not_abstract():
    assert not inspect.isabstract(Java_CastExpression)


def test_java_castexpression_constructor_exists():
    assert callable(Java_CastExpression.__init__)


def test_java_castexpression_constructor_args():
    sig = inspect.signature(Java_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_stringliteral_is_not_abstract():
    assert not inspect.isabstract(Java_StringLiteral)


def test_java_stringliteral_constructor_exists():
    assert callable(Java_StringLiteral.__init__)


def test_java_stringliteral_constructor_args():
    sig = inspect.signature(Java_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java_stringliteral_has_escapedValue():
    assert hasattr(Java_StringLiteral, "escapedValue")
    descriptor = None
    for klass in Java_StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java_unresolveditemaccess_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedItemAccess)


def test_java_unresolveditemaccess_constructor_exists():
    assert callable(Java_UnresolvedItemAccess.__init__)


def test_java_unresolveditemaccess_constructor_args():
    sig = inspect.signature(Java_UnresolvedItemAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_singlevariableaccess_is_not_abstract():
    assert not inspect.isabstract(Java_SingleVariableAccess)


def test_java_singlevariableaccess_constructor_exists():
    assert callable(Java_SingleVariableAccess.__init__)


def test_java_singlevariableaccess_constructor_args():
    sig = inspect.signature(Java_SingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_infixexpression_is_not_abstract():
    assert not inspect.isabstract(Java_InfixExpression)


def test_java_infixexpression_constructor_exists():
    assert callable(Java_InfixExpression.__init__)


def test_java_infixexpression_constructor_args():
    sig = inspect.signature(Java_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_infixexpression_has_operator():
    assert hasattr(Java_InfixExpression, "operator")
    descriptor = None
    for klass in Java_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java_FieldAccess)


def test_java_fieldaccess_constructor_exists():
    assert callable(Java_FieldAccess.__init__)


def test_java_fieldaccess_constructor_args():
    sig = inspect.signature(Java_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_typeliteral_is_not_abstract():
    assert not inspect.isabstract(Java_TypeLiteral)


def test_java_typeliteral_constructor_exists():
    assert callable(Java_TypeLiteral.__init__)


def test_java_typeliteral_constructor_args():
    sig = inspect.signature(Java_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(Java_PrefixExpression)


def test_java_prefixexpression_constructor_exists():
    assert callable(Java_PrefixExpression.__init__)


def test_java_prefixexpression_constructor_args():
    sig = inspect.signature(Java_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_prefixexpression_has_operator():
    assert hasattr(Java_PrefixExpression, "operator")
    descriptor = None
    for klass in Java_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(Java_ParenthesizedExpression)


def test_java_parenthesizedexpression_constructor_exists():
    assert callable(Java_ParenthesizedExpression.__init__)


def test_java_parenthesizedexpression_constructor_args():
    sig = inspect.signature(Java_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(Java_AbstractTypeQualifiedExpression)


def test_java_abstracttypequalifiedexpression_constructor_exists():
    assert callable(Java_AbstractTypeQualifiedExpression.__init__)


def test_java_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(Java_AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_package_is_not_abstract():
    assert not inspect.isabstract(Java_Package)


def test_java_package_constructor_exists():
    assert callable(Java_Package.__init__)


def test_java_package_constructor_args():
    sig = inspect.signature(Java_Package.__init__)
    params = list(sig.parameters.keys())



def test_java_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_BodyDeclaration)


def test_java_bodydeclaration_constructor_exists():
    assert callable(Java_BodyDeclaration.__init__)


def test_java_bodydeclaration_constructor_args():
    sig = inspect.signature(Java_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(Java_WildCardType)


def test_java_wildcardtype_constructor_exists():
    assert callable(Java_WildCardType.__init__)


def test_java_wildcardtype_constructor_args():
    sig = inspect.signature(Java_WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_java_wildcardtype_has_upperBound():
    assert hasattr(Java_WildCardType, "upperBound")
    descriptor = None
    for klass in Java_WildCardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_java_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(Java_ParameterizedType)


def test_java_parameterizedtype_constructor_exists():
    assert callable(Java_ParameterizedType.__init__)


def test_java_parameterizedtype_constructor_args():
    sig = inspect.signature(Java_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(Java_UnresolvedType)


def test_java_unresolvedtype_constructor_exists():
    assert callable(Java_UnresolvedType.__init__)


def test_java_unresolvedtype_constructor_args():
    sig = inspect.signature(Java_UnresolvedType.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveType)


def test_java_primitivetype_constructor_exists():
    assert callable(Java_PrimitiveType.__init__)


def test_java_primitivetype_constructor_args():
    sig = inspect.signature(Java_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java_typeparameter_is_not_abstract():
    assert not inspect.isabstract(Java_TypeParameter)


def test_java_typeparameter_constructor_exists():
    assert callable(Java_TypeParameter.__init__)


def test_java_typeparameter_constructor_args():
    sig = inspect.signature(Java_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java_arraytype_is_not_abstract():
    assert not inspect.isabstract(Java_ArrayType)


def test_java_arraytype_constructor_exists():
    assert callable(Java_ArrayType.__init__)


def test_java_arraytype_constructor_args():
    sig = inspect.signature(Java_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_java_arraytype_has_dimensions():
    assert hasattr(Java_ArrayType, "dimensions")
    descriptor = None
    for klass in Java_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java_namedelement_is_not_abstract():
    assert not inspect.isabstract(Java_NamedElement)


def test_java_namedelement_constructor_exists():
    assert callable(Java_NamedElement.__init__)


def test_java_namedelement_constructor_args():
    sig = inspect.signature(Java_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_java_namedelement_has_name():
    assert hasattr(Java_NamedElement, "name")
    descriptor = None
    for klass in Java_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_namedelement_has_proxy():
    assert hasattr(Java_NamedElement, "proxy")
    descriptor = None
    for klass in Java_NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_java_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_ImportDeclaration)


def test_java_importdeclaration_constructor_exists():
    assert callable(Java_ImportDeclaration.__init__)


def test_java_importdeclaration_constructor_args():
    sig = inspect.signature(Java_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java_importdeclaration_has_static():
    assert hasattr(Java_ImportDeclaration, "static")
    descriptor = None
    for klass in Java_ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java_comment_is_not_abstract():
    assert not inspect.isabstract(Java_Comment)


def test_java_comment_constructor_exists():
    assert callable(Java_Comment.__init__)


def test_java_comment_constructor_args():
    sig = inspect.signature(Java_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"

def test_java_comment_has_content():
    assert hasattr(Java_Comment, "content")
    descriptor = None
    for klass in Java_Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_java_comment_has_prefixOfParent():
    assert hasattr(Java_Comment, "prefixOfParent")
    descriptor = None
    for klass in Java_Comment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)

def test_java_comment_has_enclosedByParent():
    assert hasattr(Java_Comment, "enclosedByParent")
    descriptor = None
    for klass in Java_Comment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)



def test_java_statement_is_not_abstract():
    assert not inspect.isabstract(Java_Statement)


def test_java_statement_constructor_exists():
    assert callable(Java_Statement.__init__)


def test_java_statement_constructor_args():
    sig = inspect.signature(Java_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_tagelement_is_not_abstract():
    assert not inspect.isabstract(Java_TagElement)


def test_java_tagelement_constructor_exists():
    assert callable(Java_TagElement.__init__)


def test_java_tagelement_constructor_args():
    sig = inspect.signature(Java_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java_tagelement_has_tagName():
    assert hasattr(Java_TagElement, "tagName")
    descriptor = None
    for klass in Java_TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java_textelement_is_not_abstract():
    assert not inspect.isabstract(Java_TextElement)


def test_java_textelement_constructor_exists():
    assert callable(Java_TextElement.__init__)


def test_java_textelement_constructor_args():
    sig = inspect.signature(Java_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java_textelement_has_text():
    assert hasattr(Java_TextElement, "text")
    descriptor = None
    for klass in Java_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_java_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(Java_MethodRefParameter)


def test_java_methodrefparameter_constructor_exists():
    assert callable(Java_MethodRefParameter.__init__)


def test_java_methodrefparameter_constructor_args():
    sig = inspect.signature(Java_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java_methodrefparameter_has_name():
    assert hasattr(Java_MethodRefParameter, "name")
    descriptor = None
    for klass in Java_MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_methodrefparameter_has_varargs():
    assert hasattr(Java_MethodRefParameter, "varargs")
    descriptor = None
    for klass in Java_MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_java_memberref_is_not_abstract():
    assert not inspect.isabstract(Java_MemberRef)


def test_java_memberref_constructor_exists():
    assert callable(Java_MemberRef.__init__)


def test_java_memberref_constructor_args():
    sig = inspect.signature(Java_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java_modifier_is_not_abstract():
    assert not inspect.isabstract(Java_Modifier)


def test_java_modifier_constructor_exists():
    assert callable(Java_Modifier.__init__)


def test_java_modifier_constructor_args():
    sig = inspect.signature(Java_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "native" in params, "Missing parameter 'native'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"

def test_java_modifier_has_inheritance():
    assert hasattr(Java_Modifier, "inheritance")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_strictfp():
    assert hasattr(Java_Modifier, "strictfp")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_volatile():
    assert hasattr(Java_Modifier, "volatile")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_transient():
    assert hasattr(Java_Modifier, "transient")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_synchronized():
    assert hasattr(Java_Modifier, "synchronized")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_native():
    assert hasattr(Java_Modifier, "native")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_visibility():
    assert hasattr(Java_Modifier, "visibility")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_static():
    assert hasattr(Java_Modifier, "static")
    descriptor = None
    for klass in Java_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_AnonymousClassDeclaration)


def test_java_anonymousclassdeclaration_constructor_exists():
    assert callable(Java_AnonymousClassDeclaration.__init__)


def test_java_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(Java_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_methodref_is_not_abstract():
    assert not inspect.isabstract(Java_MethodRef)


def test_java_methodref_constructor_exists():
    assert callable(Java_MethodRef.__init__)


def test_java_methodref_constructor_args():
    sig = inspect.signature(Java_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java_expression_is_not_abstract():
    assert not inspect.isabstract(Java_Expression)


def test_java_expression_constructor_exists():
    assert callable(Java_Expression.__init__)


def test_java_expression_constructor_args():
    sig = inspect.signature(Java_Expression.__init__)
    params = list(sig.parameters.keys())



def test_java_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(Java_AbstractVariablesContainer)


def test_java_abstractvariablescontainer_constructor_exists():
    assert callable(Java_AbstractVariablesContainer.__init__)


def test_java_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(Java_AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_java_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(Java_NamespaceAccess)


def test_java_namespaceaccess_constructor_exists():
    assert callable(Java_NamespaceAccess.__init__)


def test_java_namespaceaccess_constructor_args():
    sig = inspect.signature(Java_NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java_AbstractMethodInvocation)


def test_java_abstractmethodinvocation_constructor_exists():
    assert callable(Java_AbstractMethodInvocation.__init__)


def test_java_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(Java_AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_block_is_not_abstract():
    assert not inspect.isabstract(Java_Block)


def test_java_block_constructor_exists():
    assert callable(Java_Block.__init__)


def test_java_block_constructor_args():
    sig = inspect.signature(Java_Block.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_EnumConstantDeclaration)


def test_java_enumconstantdeclaration_constructor_exists():
    assert callable(Java_EnumConstantDeclaration.__init__)


def test_java_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(Java_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_AnnotationTypeMemberDeclaration)


def test_java_annotationtypememberdeclaration_constructor_exists():
    assert callable(Java_AnnotationTypeMemberDeclaration.__init__)


def test_java_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_FieldDeclaration)


def test_java_fielddeclaration_constructor_exists():
    assert callable(Java_FieldDeclaration.__init__)


def test_java_fielddeclaration_constructor_args():
    sig = inspect.signature(Java_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_initializer_is_not_abstract():
    assert not inspect.isabstract(Java_Initializer)


def test_java_initializer_constructor_exists():
    assert callable(Java_Initializer.__init__)


def test_java_initializer_constructor_args():
    sig = inspect.signature(Java_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_AbstractTypeDeclaration)


def test_java_abstracttypedeclaration_constructor_exists():
    assert callable(Java_AbstractTypeDeclaration.__init__)


def test_java_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(Java_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_AbstractMethodDeclaration)


def test_java_abstractmethoddeclaration_constructor_exists():
    assert callable(Java_AbstractMethodDeclaration.__init__)


def test_java_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(Java_AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_prefixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionKind is not None

def test_prefixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionKind]
    expected_literals = [
        "DECREMENT",
        "NOT",
        "INCREMENT",
        "COMPLEMENT",
        "MINUS",
        "PLUS",
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
        "protected",
        "public",
        "private",
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
        "none",
        "final",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"

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

def test_infixexpressionkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionKind is not None

def test_infixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionKind]
    expected_literals = [
        "TIMES",
        "CONDITIONAL_OR",
        "REMAINDER",
        "EQUALS",
        "LEFT_SHIFT",
        "OR",
        "LESS",
        "DIVIDE",
        "GREATER",
        "CONDITIONAL_AND",
        "RIGHT_SHIFT_UNSIGNED",
        "PLUS",
        "LESS_EQUALS",
        "MINUS",
        "AND",
        "RIGHT_SHIFT_SIGNED",
        "NOT_EQUALS",
        "GREATER_EQUALS",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionKind"

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "BIT_XOR_ASSIGN",
        "BIT_AND_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "TIMES_ASSIGN",
        "PLUS_ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "BIT_OR_ASSIGN",
        "MINUS_ASSIGN",
        "LEFT_SHIFT_ASSIGN",
        "REMAINDER_ASSIGN",
        "ASSIGN",
        "DIVIDE_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentKind"


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
AnnotationTypeMemberDeclaration_strategy = st.builds(
    AnnotationTypeMemberDeclaration,
)
UnresolvedItem_strategy = st.builds(
    UnresolvedItem,
)
Java_UnresolvedAnnotationTypeMemberDeclaration_strategy = st.builds(
    Java_UnresolvedAnnotationTypeMemberDeclaration,
)
AnnotationTypeDeclaration_strategy = st.builds(
    AnnotationTypeDeclaration,
)
Java_UnresolvedAnnotationDeclaration_strategy = st.builds(
    Java_UnresolvedAnnotationDeclaration,
)
AbstractTypeQualifiedExpression_strategy = st.builds(
    AbstractTypeQualifiedExpression,
)
Java_ThisExpression_strategy = st.builds(
    Java_ThisExpression,
)
Java_SuperFieldAccess_strategy = st.builds(
    Java_SuperFieldAccess,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
Java_PrimitiveTypeChar_strategy = st.builds(
    Java_PrimitiveTypeChar,
)
Java_PrimitiveTypeShort_strategy = st.builds(
    Java_PrimitiveTypeShort,
)
Java_PrimitiveTypeDouble_strategy = st.builds(
    Java_PrimitiveTypeDouble,
)
Java_PrimitiveTypeVoid_strategy = st.builds(
    Java_PrimitiveTypeVoid,
)
Java_PrimitiveTypeLong_strategy = st.builds(
    Java_PrimitiveTypeLong,
)
Java_PrimitiveTypeByte_strategy = st.builds(
    Java_PrimitiveTypeByte,
)
Java_PrimitiveTypeInt_strategy = st.builds(
    Java_PrimitiveTypeInt,
)
Java_PrimitiveTypeFloat_strategy = st.builds(
    Java_PrimitiveTypeFloat,
)
Java_PrimitiveTypeBoolean_strategy = st.builds(
    Java_PrimitiveTypeBoolean,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
Java_PackageAccess_strategy = st.builds(
    Java_PackageAccess,
)
Java_Model_strategy = st.builds(
    Java_Model,
    name=
        safe_text
)
Java_ManifestEntry_strategy = st.builds(
    Java_ManifestEntry,
    name=
        safe_text
)
Java_ManifestAttribute_strategy = st.builds(
    Java_ManifestAttribute,
    key=
        safe_text,
    value=
        safe_text
)
MethodDeclaration_strategy = st.builds(
    MethodDeclaration,
)
Java_UnresolvedMethodDeclaration_strategy = st.builds(
    Java_UnresolvedMethodDeclaration,
)
LabeledStatement_strategy = st.builds(
    LabeledStatement,
)
Java_UnresolvedLabeledStatement_strategy = st.builds(
    Java_UnresolvedLabeledStatement,
)
InterfaceDeclaration_strategy = st.builds(
    InterfaceDeclaration,
)
Java_UnresolvedInterfaceDeclaration_strategy = st.builds(
    Java_UnresolvedInterfaceDeclaration,
)
EnumDeclaration_strategy = st.builds(
    EnumDeclaration,
)
Java_UnresolvedEnumDeclaration_strategy = st.builds(
    Java_UnresolvedEnumDeclaration,
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
Java_UnresolvedVariableDeclarationFragment_strategy = st.builds(
    Java_UnresolvedVariableDeclarationFragment,
)
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
)
Java_UnresolvedSingleVariableDeclaration_strategy = st.builds(
    Java_UnresolvedSingleVariableDeclaration,
)
ClassDeclaration_strategy = st.builds(
    ClassDeclaration,
)
Java_UnresolvedClassDeclaration_strategy = st.builds(
    Java_UnresolvedClassDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Java_InterfaceDeclaration_strategy = st.builds(
    Java_InterfaceDeclaration,
)
Java_ClassDeclaration_strategy = st.builds(
    Java_ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
Java_MethodDeclaration_strategy = st.builds(
    Java_MethodDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java_ConstructorDeclaration_strategy = st.builds(
    Java_ConstructorDeclaration,
)
AbstractMethodInvocation_strategy = st.builds(
    AbstractMethodInvocation,
)
Java_SuperMethodInvocation_strategy = st.builds(
    Java_SuperMethodInvocation,
)
Comment_strategy = st.builds(
    Comment,
)
Java_LineComment_strategy = st.builds(
    Java_LineComment,
)
Java_Javadoc_strategy = st.builds(
    Java_Javadoc,
)
Java_BlockComment_strategy = st.builds(
    Java_BlockComment,
)
Java_VariableDeclarationFragment_strategy = st.builds(
    Java_VariableDeclarationFragment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
Java_UnresolvedTypeDeclaration_strategy = st.builds(
    Java_UnresolvedTypeDeclaration,
)
Java_TypeDeclaration_strategy = st.builds(
    Java_TypeDeclaration,
)
Java_EnumDeclaration_strategy = st.builds(
    Java_EnumDeclaration,
)
Java_AnnotationTypeDeclaration_strategy = st.builds(
    Java_AnnotationTypeDeclaration,
)
Java_ASTNode_strategy = st.builds(
    Java_ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
Java_VariableDeclarationStatement_strategy = st.builds(
    Java_VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
Java_ThrowStatement_strategy = st.builds(
    Java_ThrowStatement,
)
Java_EnhancedForStatement_strategy = st.builds(
    Java_EnhancedForStatement,
)
Java_CatchClause_strategy = st.builds(
    Java_CatchClause,
)
Java_TypeDeclarationStatement_strategy = st.builds(
    Java_TypeDeclarationStatement,
)
Java_ExpressionStatement_strategy = st.builds(
    Java_ExpressionStatement,
)
Java_SuperConstructorInvocation_strategy = st.builds(
    Java_SuperConstructorInvocation,
)
Java_SwitchStatement_strategy = st.builds(
    Java_SwitchStatement,
)
Java_SwitchCase_strategy = st.builds(
    Java_SwitchCase,
    default=
        st.booleans()
)
Java_EmptyStatement_strategy = st.builds(
    Java_EmptyStatement,
)
Java_ReturnStatement_strategy = st.builds(
    Java_ReturnStatement,
)
Java_SynchronizedStatement_strategy = st.builds(
    Java_SynchronizedStatement,
)
Java_ContinueStatement_strategy = st.builds(
    Java_ContinueStatement,
)
Java_DoStatement_strategy = st.builds(
    Java_DoStatement,
)
Java_ConstructorInvocation_strategy = st.builds(
    Java_ConstructorInvocation,
)
Java_ForStatement_strategy = st.builds(
    Java_ForStatement,
)
Java_BreakStatement_strategy = st.builds(
    Java_BreakStatement,
)
Java_WhileStatement_strategy = st.builds(
    Java_WhileStatement,
)
Java_IfStatement_strategy = st.builds(
    Java_IfStatement,
)
Java_TryStatement_strategy = st.builds(
    Java_TryStatement,
)
Java_AssertStatement_strategy = st.builds(
    Java_AssertStatement,
)
Java_Manifest_strategy = st.builds(
    Java_Manifest,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Java_UnresolvedItem_strategy = st.builds(
    Java_UnresolvedItem,
)
Java_CompilationUnit_strategy = st.builds(
    Java_CompilationUnit,
    originalFilePath=
        safe_text
)
Java_ClassFile_strategy = st.builds(
    Java_ClassFile,
    originalFilePath=
        safe_text
)
Java_Type_strategy = st.builds(
    Java_Type,
)
Java_LabeledStatement_strategy = st.builds(
    Java_LabeledStatement,
)
Java_VariableDeclaration_strategy = st.builds(
    Java_VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java_Archive_strategy = st.builds(
    Java_Archive,
    originalFilePath=
        safe_text
)
Java_AnnotationMemberValuePair_strategy = st.builds(
    Java_AnnotationMemberValuePair,
)
Java_SingleVariableDeclaration_strategy = st.builds(
    Java_SingleVariableDeclaration,
    varargs=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
Java_CharacterLiteral_strategy = st.builds(
    Java_CharacterLiteral,
    escapedValue=
        safe_text
)
Java_ClassInstanceCreation_strategy = st.builds(
    Java_ClassInstanceCreation,
)
Java_VariableDeclarationExpression_strategy = st.builds(
    Java_VariableDeclarationExpression,
)
Java_TypeAccess_strategy = st.builds(
    Java_TypeAccess,
)
Java_NumberLiteral_strategy = st.builds(
    Java_NumberLiteral,
    tokenValue=
        safe_text
)
Java_BooleanLiteral_strategy = st.builds(
    Java_BooleanLiteral,
    value=
        st.booleans()
)
Java_ArrayLengthAccess_strategy = st.builds(
    Java_ArrayLengthAccess,
)
Java_ArrayAccess_strategy = st.builds(
    Java_ArrayAccess,
)
Java_ArrayInitializer_strategy = st.builds(
    Java_ArrayInitializer,
)
Java_ConditionalExpression_strategy = st.builds(
    Java_ConditionalExpression,
)
Java_ArrayCreation_strategy = st.builds(
    Java_ArrayCreation,
)
Java_Annotation_strategy = st.builds(
    Java_Annotation,
)
Java_MethodInvocation_strategy = st.builds(
    Java_MethodInvocation,
)
Java_Assignment_strategy = st.builds(
    Java_Assignment,
    operator=
        safe_text
)
Java_NullLiteral_strategy = st.builds(
    Java_NullLiteral,
)
Java_InstanceofExpression_strategy = st.builds(
    Java_InstanceofExpression,
)
Java_PostfixExpression_strategy = st.builds(
    Java_PostfixExpression,
    operator=
        safe_text
)
Java_CastExpression_strategy = st.builds(
    Java_CastExpression,
)
Java_StringLiteral_strategy = st.builds(
    Java_StringLiteral,
    escapedValue=
        safe_text
)
Java_UnresolvedItemAccess_strategy = st.builds(
    Java_UnresolvedItemAccess,
)
Java_SingleVariableAccess_strategy = st.builds(
    Java_SingleVariableAccess,
)
Java_InfixExpression_strategy = st.builds(
    Java_InfixExpression,
    operator=
        safe_text
)
Java_FieldAccess_strategy = st.builds(
    Java_FieldAccess,
)
Java_TypeLiteral_strategy = st.builds(
    Java_TypeLiteral,
)
Java_PrefixExpression_strategy = st.builds(
    Java_PrefixExpression,
    operator=
        safe_text
)
Java_ParenthesizedExpression_strategy = st.builds(
    Java_ParenthesizedExpression,
)
Java_AbstractTypeQualifiedExpression_strategy = st.builds(
    Java_AbstractTypeQualifiedExpression,
)
Java_Package_strategy = st.builds(
    Java_Package,
)
Java_BodyDeclaration_strategy = st.builds(
    Java_BodyDeclaration,
)
Type_strategy = st.builds(
    Type,
)
Java_WildCardType_strategy = st.builds(
    Java_WildCardType,
    upperBound=
        st.booleans()
)
Java_ParameterizedType_strategy = st.builds(
    Java_ParameterizedType,
)
Java_UnresolvedType_strategy = st.builds(
    Java_UnresolvedType,
)
Java_PrimitiveType_strategy = st.builds(
    Java_PrimitiveType,
)
Java_TypeParameter_strategy = st.builds(
    Java_TypeParameter,
)
Java_ArrayType_strategy = st.builds(
    Java_ArrayType,
    dimensions=
        st.integers()
)
ASTNode_strategy = st.builds(
    ASTNode,
)
Java_NamedElement_strategy = st.builds(
    Java_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
Java_ImportDeclaration_strategy = st.builds(
    Java_ImportDeclaration,
    static=
        st.booleans()
)
Java_Comment_strategy = st.builds(
    Java_Comment,
    content=
        safe_text,
    prefixOfParent=
        st.booleans(),
    enclosedByParent=
        st.booleans()
)
Java_Statement_strategy = st.builds(
    Java_Statement,
)
Java_TagElement_strategy = st.builds(
    Java_TagElement,
    tagName=
        safe_text
)
Java_TextElement_strategy = st.builds(
    Java_TextElement,
    text=
        safe_text
)
Java_MethodRefParameter_strategy = st.builds(
    Java_MethodRefParameter,
    name=
        safe_text,
    varargs=
        st.booleans()
)
Java_MemberRef_strategy = st.builds(
    Java_MemberRef,
)
Java_Modifier_strategy = st.builds(
    Java_Modifier,
    inheritance=
        safe_text,
    strictfp=
        st.booleans(),
    volatile=
        st.booleans(),
    transient=
        st.booleans(),
    synchronized=
        st.booleans(),
    native=
        st.booleans(),
    visibility=
        safe_text,
    static=
        st.booleans()
)
Java_AnonymousClassDeclaration_strategy = st.builds(
    Java_AnonymousClassDeclaration,
)
Java_MethodRef_strategy = st.builds(
    Java_MethodRef,
)
Java_Expression_strategy = st.builds(
    Java_Expression,
)
Java_AbstractVariablesContainer_strategy = st.builds(
    Java_AbstractVariablesContainer,
)
Java_NamespaceAccess_strategy = st.builds(
    Java_NamespaceAccess,
)
Java_AbstractMethodInvocation_strategy = st.builds(
    Java_AbstractMethodInvocation,
)
Java_Block_strategy = st.builds(
    Java_Block,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
Java_EnumConstantDeclaration_strategy = st.builds(
    Java_EnumConstantDeclaration,
)
Java_AnnotationTypeMemberDeclaration_strategy = st.builds(
    Java_AnnotationTypeMemberDeclaration,
)
Java_FieldDeclaration_strategy = st.builds(
    Java_FieldDeclaration,
)
Java_Initializer_strategy = st.builds(
    Java_Initializer,
)
Java_AbstractTypeDeclaration_strategy = st.builds(
    Java_AbstractTypeDeclaration,
)
Java_AbstractMethodDeclaration_strategy = st.builds(
    Java_AbstractMethodDeclaration,
)

@given(instance=AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeMemberDeclaration)

@given(instance=UnresolvedItem_strategy)
@settings(max_examples=50)
def test_unresolveditem_instantiation(instance):
    assert isinstance(instance, UnresolvedItem)

@given(instance=Java_UnresolvedAnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedannotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedAnnotationTypeMemberDeclaration)

@given(instance=AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeDeclaration)

@given(instance=Java_UnresolvedAnnotationDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedannotationdeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedAnnotationDeclaration)

@given(instance=AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, AbstractTypeQualifiedExpression)

@given(instance=Java_ThisExpression_strategy)
@settings(max_examples=50)
def test_java_thisexpression_instantiation(instance):
    assert isinstance(instance, Java_ThisExpression)

@given(instance=Java_SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java_superfieldaccess_instantiation(instance):
    assert isinstance(instance, Java_SuperFieldAccess)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=Java_PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java_primitivetypechar_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeChar)

@given(instance=Java_PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java_primitivetypeshort_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeShort)

@given(instance=Java_PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java_primitivetypedouble_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeDouble)

@given(instance=Java_PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java_primitivetypevoid_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeVoid)

@given(instance=Java_PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java_primitivetypelong_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeLong)

@given(instance=Java_PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java_primitivetypebyte_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeByte)

@given(instance=Java_PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java_primitivetypeint_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeInt)

@given(instance=Java_PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java_primitivetypefloat_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeFloat)

@given(instance=Java_PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java_primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveTypeBoolean)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=Java_PackageAccess_strategy)
@settings(max_examples=50)
def test_java_packageaccess_instantiation(instance):
    assert isinstance(instance, Java_PackageAccess)

@given(instance=Java_Model_strategy)
@settings(max_examples=50)
def test_java_model_instantiation(instance):
    assert isinstance(instance, Java_Model)



@given(instance=Java_Model_strategy)
def test_java_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java_ManifestEntry_strategy)
@settings(max_examples=50)
def test_java_manifestentry_instantiation(instance):
    assert isinstance(instance, Java_ManifestEntry)



@given(instance=Java_ManifestEntry_strategy)
def test_java_manifestentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java_ManifestAttribute_strategy)
@settings(max_examples=50)
def test_java_manifestattribute_instantiation(instance):
    assert isinstance(instance, Java_ManifestAttribute)



@given(instance=Java_ManifestAttribute_strategy)
def test_java_manifestattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=Java_ManifestAttribute_strategy)
def test_java_manifestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MethodDeclaration_strategy)
@settings(max_examples=50)
def test_methoddeclaration_instantiation(instance):
    assert isinstance(instance, MethodDeclaration)

@given(instance=Java_UnresolvedMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedmethoddeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedMethodDeclaration)

@given(instance=LabeledStatement_strategy)
@settings(max_examples=50)
def test_labeledstatement_instantiation(instance):
    assert isinstance(instance, LabeledStatement)

@given(instance=Java_UnresolvedLabeledStatement_strategy)
@settings(max_examples=50)
def test_java_unresolvedlabeledstatement_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedLabeledStatement)

@given(instance=InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, InterfaceDeclaration)

@given(instance=Java_UnresolvedInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedInterfaceDeclaration)

@given(instance=EnumDeclaration_strategy)
@settings(max_examples=50)
def test_enumdeclaration_instantiation(instance):
    assert isinstance(instance, EnumDeclaration)

@given(instance=Java_UnresolvedEnumDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedenumdeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedEnumDeclaration)

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

@given(instance=Java_UnresolvedVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java_unresolvedvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedVariableDeclarationFragment)

@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)

@given(instance=Java_UnresolvedSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedSingleVariableDeclaration)

@given(instance=ClassDeclaration_strategy)
@settings(max_examples=50)
def test_classdeclaration_instantiation(instance):
    assert isinstance(instance, ClassDeclaration)

@given(instance=Java_UnresolvedClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedclassdeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedClassDeclaration)

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

@given(instance=Java_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, Java_InterfaceDeclaration)

@given(instance=Java_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_classdeclaration_instantiation(instance):
    assert isinstance(instance, Java_ClassDeclaration)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=Java_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java_methoddeclaration_instantiation(instance):
    assert isinstance(instance, Java_MethodDeclaration)



@given(instance=Java_MethodDeclaration_strategy)
def test_java_methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java_ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_java_constructordeclaration_instantiation(instance):
    assert isinstance(instance, Java_ConstructorDeclaration)

@given(instance=AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, AbstractMethodInvocation)

@given(instance=Java_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, Java_SuperMethodInvocation)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Java_LineComment_strategy)
@settings(max_examples=50)
def test_java_linecomment_instantiation(instance):
    assert isinstance(instance, Java_LineComment)

@given(instance=Java_Javadoc_strategy)
@settings(max_examples=50)
def test_java_javadoc_instantiation(instance):
    assert isinstance(instance, Java_Javadoc)

@given(instance=Java_BlockComment_strategy)
@settings(max_examples=50)
def test_java_blockcomment_instantiation(instance):
    assert isinstance(instance, Java_BlockComment)

@given(instance=Java_VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Java_VariableDeclarationFragment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=Java_UnresolvedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedtypedeclaration_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedTypeDeclaration)

@given(instance=Java_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_typedeclaration_instantiation(instance):
    assert isinstance(instance, Java_TypeDeclaration)

@given(instance=Java_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java_enumdeclaration_instantiation(instance):
    assert isinstance(instance, Java_EnumDeclaration)

@given(instance=Java_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, Java_AnnotationTypeDeclaration)

@given(instance=Java_ASTNode_strategy)
@settings(max_examples=50)
def test_java_astnode_instantiation(instance):
    assert isinstance(instance, Java_ASTNode)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Java_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java_VariableDeclarationStatement)



@given(instance=Java_VariableDeclarationStatement_strategy)
def test_java_variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java_ThrowStatement_strategy)
@settings(max_examples=50)
def test_java_throwstatement_instantiation(instance):
    assert isinstance(instance, Java_ThrowStatement)

@given(instance=Java_EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java_enhancedforstatement_instantiation(instance):
    assert isinstance(instance, Java_EnhancedForStatement)

@given(instance=Java_CatchClause_strategy)
@settings(max_examples=50)
def test_java_catchclause_instantiation(instance):
    assert isinstance(instance, Java_CatchClause)

@given(instance=Java_TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java_typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java_TypeDeclarationStatement)

@given(instance=Java_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java_expressionstatement_instantiation(instance):
    assert isinstance(instance, Java_ExpressionStatement)

@given(instance=Java_SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java_superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, Java_SuperConstructorInvocation)

@given(instance=Java_SwitchStatement_strategy)
@settings(max_examples=50)
def test_java_switchstatement_instantiation(instance):
    assert isinstance(instance, Java_SwitchStatement)

@given(instance=Java_SwitchCase_strategy)
@settings(max_examples=50)
def test_java_switchcase_instantiation(instance):
    assert isinstance(instance, Java_SwitchCase)



@given(instance=Java_SwitchCase_strategy)
def test_java_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Java_EmptyStatement_strategy)
@settings(max_examples=50)
def test_java_emptystatement_instantiation(instance):
    assert isinstance(instance, Java_EmptyStatement)

@given(instance=Java_ReturnStatement_strategy)
@settings(max_examples=50)
def test_java_returnstatement_instantiation(instance):
    assert isinstance(instance, Java_ReturnStatement)

@given(instance=Java_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, Java_SynchronizedStatement)

@given(instance=Java_ContinueStatement_strategy)
@settings(max_examples=50)
def test_java_continuestatement_instantiation(instance):
    assert isinstance(instance, Java_ContinueStatement)

@given(instance=Java_DoStatement_strategy)
@settings(max_examples=50)
def test_java_dostatement_instantiation(instance):
    assert isinstance(instance, Java_DoStatement)

@given(instance=Java_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java_constructorinvocation_instantiation(instance):
    assert isinstance(instance, Java_ConstructorInvocation)

@given(instance=Java_ForStatement_strategy)
@settings(max_examples=50)
def test_java_forstatement_instantiation(instance):
    assert isinstance(instance, Java_ForStatement)

@given(instance=Java_BreakStatement_strategy)
@settings(max_examples=50)
def test_java_breakstatement_instantiation(instance):
    assert isinstance(instance, Java_BreakStatement)

@given(instance=Java_WhileStatement_strategy)
@settings(max_examples=50)
def test_java_whilestatement_instantiation(instance):
    assert isinstance(instance, Java_WhileStatement)

@given(instance=Java_IfStatement_strategy)
@settings(max_examples=50)
def test_java_ifstatement_instantiation(instance):
    assert isinstance(instance, Java_IfStatement)

@given(instance=Java_TryStatement_strategy)
@settings(max_examples=50)
def test_java_trystatement_instantiation(instance):
    assert isinstance(instance, Java_TryStatement)

@given(instance=Java_AssertStatement_strategy)
@settings(max_examples=50)
def test_java_assertstatement_instantiation(instance):
    assert isinstance(instance, Java_AssertStatement)

@given(instance=Java_Manifest_strategy)
@settings(max_examples=50)
def test_java_manifest_instantiation(instance):
    assert isinstance(instance, Java_Manifest)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Java_UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java_unresolveditem_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedItem)

@given(instance=Java_CompilationUnit_strategy)
@settings(max_examples=50)
def test_java_compilationunit_instantiation(instance):
    assert isinstance(instance, Java_CompilationUnit)



@given(instance=Java_CompilationUnit_strategy)
def test_java_compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java_ClassFile_strategy)
@settings(max_examples=50)
def test_java_classfile_instantiation(instance):
    assert isinstance(instance, Java_ClassFile)



@given(instance=Java_ClassFile_strategy)
def test_java_classfile_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java_Type_strategy)
@settings(max_examples=50)
def test_java_type_instantiation(instance):
    assert isinstance(instance, Java_Type)

@given(instance=Java_LabeledStatement_strategy)
@settings(max_examples=50)
def test_java_labeledstatement_instantiation(instance):
    assert isinstance(instance, Java_LabeledStatement)

@given(instance=Java_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_variabledeclaration_instantiation(instance):
    assert isinstance(instance, Java_VariableDeclaration)



@given(instance=Java_VariableDeclaration_strategy)
def test_java_variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java_Archive_strategy)
@settings(max_examples=50)
def test_java_archive_instantiation(instance):
    assert isinstance(instance, Java_Archive)



@given(instance=Java_Archive_strategy)
def test_java_archive_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java_AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java_annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, Java_AnnotationMemberValuePair)

@given(instance=Java_SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Java_SingleVariableDeclaration)



@given(instance=Java_SingleVariableDeclaration_strategy)
def test_java_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Java_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java_characterliteral_instantiation(instance):
    assert isinstance(instance, Java_CharacterLiteral)



@given(instance=Java_CharacterLiteral_strategy)
def test_java_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java_classinstancecreation_instantiation(instance):
    assert isinstance(instance, Java_ClassInstanceCreation)

@given(instance=Java_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, Java_VariableDeclarationExpression)

@given(instance=Java_TypeAccess_strategy)
@settings(max_examples=50)
def test_java_typeaccess_instantiation(instance):
    assert isinstance(instance, Java_TypeAccess)

@given(instance=Java_NumberLiteral_strategy)
@settings(max_examples=50)
def test_java_numberliteral_instantiation(instance):
    assert isinstance(instance, Java_NumberLiteral)



@given(instance=Java_NumberLiteral_strategy)
def test_java_numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=Java_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java_booleanliteral_instantiation(instance):
    assert isinstance(instance, Java_BooleanLiteral)



@given(instance=Java_BooleanLiteral_strategy)
def test_java_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java_ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java_arraylengthaccess_instantiation(instance):
    assert isinstance(instance, Java_ArrayLengthAccess)

@given(instance=Java_ArrayAccess_strategy)
@settings(max_examples=50)
def test_java_arrayaccess_instantiation(instance):
    assert isinstance(instance, Java_ArrayAccess)

@given(instance=Java_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java_arrayinitializer_instantiation(instance):
    assert isinstance(instance, Java_ArrayInitializer)

@given(instance=Java_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java_conditionalexpression_instantiation(instance):
    assert isinstance(instance, Java_ConditionalExpression)

@given(instance=Java_ArrayCreation_strategy)
@settings(max_examples=50)
def test_java_arraycreation_instantiation(instance):
    assert isinstance(instance, Java_ArrayCreation)

@given(instance=Java_Annotation_strategy)
@settings(max_examples=50)
def test_java_annotation_instantiation(instance):
    assert isinstance(instance, Java_Annotation)

@given(instance=Java_MethodInvocation_strategy)
@settings(max_examples=50)
def test_java_methodinvocation_instantiation(instance):
    assert isinstance(instance, Java_MethodInvocation)

@given(instance=Java_Assignment_strategy)
@settings(max_examples=50)
def test_java_assignment_instantiation(instance):
    assert isinstance(instance, Java_Assignment)



@given(instance=Java_Assignment_strategy)
def test_java_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java_NullLiteral_strategy)
@settings(max_examples=50)
def test_java_nullliteral_instantiation(instance):
    assert isinstance(instance, Java_NullLiteral)

@given(instance=Java_InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java_instanceofexpression_instantiation(instance):
    assert isinstance(instance, Java_InstanceofExpression)

@given(instance=Java_PostfixExpression_strategy)
@settings(max_examples=50)
def test_java_postfixexpression_instantiation(instance):
    assert isinstance(instance, Java_PostfixExpression)



@given(instance=Java_PostfixExpression_strategy)
def test_java_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java_CastExpression_strategy)
@settings(max_examples=50)
def test_java_castexpression_instantiation(instance):
    assert isinstance(instance, Java_CastExpression)

@given(instance=Java_StringLiteral_strategy)
@settings(max_examples=50)
def test_java_stringliteral_instantiation(instance):
    assert isinstance(instance, Java_StringLiteral)



@given(instance=Java_StringLiteral_strategy)
def test_java_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java_UnresolvedItemAccess_strategy)
@settings(max_examples=50)
def test_java_unresolveditemaccess_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedItemAccess)

@given(instance=Java_SingleVariableAccess_strategy)
@settings(max_examples=50)
def test_java_singlevariableaccess_instantiation(instance):
    assert isinstance(instance, Java_SingleVariableAccess)

@given(instance=Java_InfixExpression_strategy)
@settings(max_examples=50)
def test_java_infixexpression_instantiation(instance):
    assert isinstance(instance, Java_InfixExpression)



@given(instance=Java_InfixExpression_strategy)
def test_java_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java_FieldAccess_strategy)
@settings(max_examples=50)
def test_java_fieldaccess_instantiation(instance):
    assert isinstance(instance, Java_FieldAccess)

@given(instance=Java_TypeLiteral_strategy)
@settings(max_examples=50)
def test_java_typeliteral_instantiation(instance):
    assert isinstance(instance, Java_TypeLiteral)

@given(instance=Java_PrefixExpression_strategy)
@settings(max_examples=50)
def test_java_prefixexpression_instantiation(instance):
    assert isinstance(instance, Java_PrefixExpression)



@given(instance=Java_PrefixExpression_strategy)
def test_java_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, Java_ParenthesizedExpression)

@given(instance=Java_AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_java_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, Java_AbstractTypeQualifiedExpression)

@given(instance=Java_Package_strategy)
@settings(max_examples=50)
def test_java_package_instantiation(instance):
    assert isinstance(instance, Java_Package)

@given(instance=Java_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java_bodydeclaration_instantiation(instance):
    assert isinstance(instance, Java_BodyDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Java_WildCardType_strategy)
@settings(max_examples=50)
def test_java_wildcardtype_instantiation(instance):
    assert isinstance(instance, Java_WildCardType)



@given(instance=Java_WildCardType_strategy)
def test_java_wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=Java_ParameterizedType_strategy)
@settings(max_examples=50)
def test_java_parameterizedtype_instantiation(instance):
    assert isinstance(instance, Java_ParameterizedType)

@given(instance=Java_UnresolvedType_strategy)
@settings(max_examples=50)
def test_java_unresolvedtype_instantiation(instance):
    assert isinstance(instance, Java_UnresolvedType)

@given(instance=Java_PrimitiveType_strategy)
@settings(max_examples=50)
def test_java_primitivetype_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveType)

@given(instance=Java_TypeParameter_strategy)
@settings(max_examples=50)
def test_java_typeparameter_instantiation(instance):
    assert isinstance(instance, Java_TypeParameter)

@given(instance=Java_ArrayType_strategy)
@settings(max_examples=50)
def test_java_arraytype_instantiation(instance):
    assert isinstance(instance, Java_ArrayType)



@given(instance=Java_ArrayType_strategy)
def test_java_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=Java_NamedElement_strategy)
@settings(max_examples=50)
def test_java_namedelement_instantiation(instance):
    assert isinstance(instance, Java_NamedElement)



@given(instance=Java_NamedElement_strategy)
def test_java_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Java_NamedElement_strategy)
def test_java_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=Java_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java_importdeclaration_instantiation(instance):
    assert isinstance(instance, Java_ImportDeclaration)



@given(instance=Java_ImportDeclaration_strategy)
def test_java_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java_Comment_strategy)
@settings(max_examples=50)
def test_java_comment_instantiation(instance):
    assert isinstance(instance, Java_Comment)



@given(instance=Java_Comment_strategy)
def test_java_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=Java_Comment_strategy)
def test_java_comment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original



@given(instance=Java_Comment_strategy)
def test_java_comment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original

@given(instance=Java_Statement_strategy)
@settings(max_examples=50)
def test_java_statement_instantiation(instance):
    assert isinstance(instance, Java_Statement)

@given(instance=Java_TagElement_strategy)
@settings(max_examples=50)
def test_java_tagelement_instantiation(instance):
    assert isinstance(instance, Java_TagElement)



@given(instance=Java_TagElement_strategy)
def test_java_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=Java_TextElement_strategy)
@settings(max_examples=50)
def test_java_textelement_instantiation(instance):
    assert isinstance(instance, Java_TextElement)



@given(instance=Java_TextElement_strategy)
def test_java_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Java_MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java_methodrefparameter_instantiation(instance):
    assert isinstance(instance, Java_MethodRefParameter)



@given(instance=Java_MethodRefParameter_strategy)
def test_java_methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Java_MethodRefParameter_strategy)
def test_java_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=Java_MemberRef_strategy)
@settings(max_examples=50)
def test_java_memberref_instantiation(instance):
    assert isinstance(instance, Java_MemberRef)

@given(instance=Java_Modifier_strategy)
@settings(max_examples=50)
def test_java_modifier_instantiation(instance):
    assert isinstance(instance, Java_Modifier)



@given(instance=Java_Modifier_strategy)
def test_java_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=Java_Modifier_strategy)
def test_java_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java_AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, Java_AnonymousClassDeclaration)

@given(instance=Java_MethodRef_strategy)
@settings(max_examples=50)
def test_java_methodref_instantiation(instance):
    assert isinstance(instance, Java_MethodRef)

@given(instance=Java_Expression_strategy)
@settings(max_examples=50)
def test_java_expression_instantiation(instance):
    assert isinstance(instance, Java_Expression)

@given(instance=Java_AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_java_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, Java_AbstractVariablesContainer)

@given(instance=Java_NamespaceAccess_strategy)
@settings(max_examples=50)
def test_java_namespaceaccess_instantiation(instance):
    assert isinstance(instance, Java_NamespaceAccess)

@given(instance=Java_AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_java_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, Java_AbstractMethodInvocation)

@given(instance=Java_Block_strategy)
@settings(max_examples=50)
def test_java_block_instantiation(instance):
    assert isinstance(instance, Java_Block)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=Java_EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, Java_EnumConstantDeclaration)

@given(instance=Java_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, Java_AnnotationTypeMemberDeclaration)

@given(instance=Java_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java_fielddeclaration_instantiation(instance):
    assert isinstance(instance, Java_FieldDeclaration)

@given(instance=Java_Initializer_strategy)
@settings(max_examples=50)
def test_java_initializer_instantiation(instance):
    assert isinstance(instance, Java_Initializer)

@given(instance=Java_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, Java_AbstractTypeDeclaration)

@given(instance=Java_AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, Java_AbstractMethodDeclaration)
