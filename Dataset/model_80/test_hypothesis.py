import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    java_Annotation,
    java_AbstractTypeQualifiedExpression,
    Type,
    ASTNode,
    java_AbstractVariablesContainer,
    java_Comment,
    java_Expression,
    java_AbstractMethodInvocation,
    java_MethodRef,
    java_TypeParameter,
    BodyDeclaration,
    java_AbstractTypeDeclaration,
    java_AbstractMethodDeclaration,
    java_WildCardType,
    VariableDeclarationFragment,
    SingleVariableDeclaration,
    MethodDeclaration,
    LabeledStatement,
    InterfaceDeclaration,
    EnumDeclaration,
    ClassDeclaration,
    AnnotationTypeMemberDeclaration,
    UnresolvedItem,
    java_UnresolvedType,
    java_UnresolvedInterfaceDeclaration,
    java_UnresolvedClassDeclaration,
    java_UnresolvedAnnotationTypeMemberDeclaration,
    java_UnresolvedSingleVariableDeclaration,
    java_UnresolvedMethodDeclaration,
    java_UnresolvedLabeledStatement,
    java_UnresolvedEnumDeclaration,
    java_UnresolvedVariableDeclarationFragment,
    AnnotationTypeDeclaration,
    java_UnresolvedAnnotationDeclaration,
    java_TypeLiteral,
    java_TextElement,
    AbstractTypeQualifiedExpression,
    java_ThisExpression,
    java_SuperFieldAccess,
    java_StringLiteral,
    PrimitiveType,
    java_PrimitiveTypeByte,
    java_PrimitiveTypeShort,
    java_PrimitiveTypeInt,
    java_PrimitiveTypeChar,
    java_PrimitiveTypeVoid,
    java_PrimitiveTypeDouble,
    java_PrimitiveTypeLong,
    java_PrimitiveTypeFloat,
    java_PrimitiveTypeBoolean,
    java_PrimitiveType,
    java_PrefixExpression,
    java_PostfixExpression,
    java_ParenthesizedExpression,
    java_ParameterizedType,
    NamespaceAccess,
    java_UnresolvedItemAccess,
    java_TypeAccess,
    java_PackageAccess,
    java_NullLiteral,
    java_NumberLiteral,
    java_NamespaceAccess,
    java_Model,
    java_MethodRefParameter,
    java_TagElement,
    java_MemberRef,
    java_ManifestEntry,
    java_ManifestAttribute,
    java_InstanceofExpression,
    java_Initializer,
    java_InfixExpression,
    java_NamedElement,
    AbstractVariablesContainer,
    java_VariableDeclarationExpression,
    java_FieldDeclaration,
    java_SingleVariableAccess,
    java_FieldAccess,
    TypeDeclaration,
    java_InterfaceDeclaration,
    java_ClassDeclaration,
    VariableDeclaration,
    java_SingleVariableDeclaration,
    java_EnumConstantDeclaration,
    java_ImportDeclaration,
    java_Statement,
    Comment,
    java_Javadoc,
    java_LineComment,
    java_BlockComment,
    java_ConditionalExpression,
    AbstractMethodDeclaration,
    java_MethodDeclaration,
    java_ConstructorDeclaration,
    AbstractMethodInvocation,
    java_SuperMethodInvocation,
    java_MethodInvocation,
    java_CharacterLiteral,
    java_CastExpression,
    java_ArrayCreation,
    java_BooleanLiteral,
    java_Modifier,
    java_Assignment,
    java_ArrayType,
    java_ArrayLengthAccess,
    java_ArrayInitializer,
    java_VariableDeclarationFragment,
    java_ArrayAccess,
    java_ClassInstanceCreation,
    java_AnonymousClassDeclaration,
    AbstractTypeDeclaration,
    java_EnumDeclaration,
    java_UnresolvedTypeDeclaration,
    java_TypeDeclaration,
    java_AnnotationTypeDeclaration,
    java_AnnotationTypeMemberDeclaration,
    java_ASTNode,
    Statement,
    java_ExpressionStatement,
    java_SuperConstructorInvocation,
    java_TryStatement,
    java_BreakStatement,
    java_ForStatement,
    java_CatchClause,
    java_ContinueStatement,
    java_WhileStatement,
    java_IfStatement,
    java_ReturnStatement,
    java_SwitchStatement,
    java_ConstructorInvocation,
    java_EmptyStatement,
    java_Block,
    java_SwitchCase,
    java_SynchronizedStatement,
    java_EnhancedForStatement,
    java_VariableDeclarationStatement,
    java_ThrowStatement,
    java_TypeDeclarationStatement,
    java_DoStatement,
    java_AssertStatement,
    java_Manifest,
    NamedElement,
    java_InstanceSpecification,
    java_CompilationUnit,
    java_Package,
    java_VariableDeclaration,
    java_Archive,
    java_ClassFile,
    java_BodyDeclaration,
    java_LabeledStatement,
    java_UnresolvedItem,
    java_AnnotationMemberValuePair,
    java_Type,
    PostfixExpressionKind,
    VisibilityKind,
    InheritanceKind,
    AssignmentKind,
    PrefixExpressionKind,
    InfixExpressionKind,
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



def test_java_annotation_is_not_abstract():
    assert not inspect.isabstract(java_Annotation)


def test_java_annotation_constructor_exists():
    assert callable(java_Annotation.__init__)


def test_java_annotation_constructor_args():
    sig = inspect.signature(java_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(java_AbstractTypeQualifiedExpression)


def test_java_abstracttypequalifiedexpression_constructor_exists():
    assert callable(java_AbstractTypeQualifiedExpression.__init__)


def test_java_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(java_AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(java_AbstractVariablesContainer)


def test_java_abstractvariablescontainer_constructor_exists():
    assert callable(java_AbstractVariablesContainer.__init__)


def test_java_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(java_AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_java_comment_is_not_abstract():
    assert not inspect.isabstract(java_Comment)


def test_java_comment_constructor_exists():
    assert callable(java_Comment.__init__)


def test_java_comment_constructor_args():
    sig = inspect.signature(java_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"

def test_java_comment_has_content():
    assert hasattr(java_Comment, "content")
    descriptor = None
    for klass in java_Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_java_comment_has_prefixOfParent():
    assert hasattr(java_Comment, "prefixOfParent")
    descriptor = None
    for klass in java_Comment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)

def test_java_comment_has_enclosedByParent():
    assert hasattr(java_Comment, "enclosedByParent")
    descriptor = None
    for klass in java_Comment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)



def test_java_expression_is_not_abstract():
    assert not inspect.isabstract(java_Expression)


def test_java_expression_constructor_exists():
    assert callable(java_Expression.__init__)


def test_java_expression_constructor_args():
    sig = inspect.signature(java_Expression.__init__)
    params = list(sig.parameters.keys())



def test_java_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java_AbstractMethodInvocation)


def test_java_abstractmethodinvocation_constructor_exists():
    assert callable(java_AbstractMethodInvocation.__init__)


def test_java_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(java_AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_methodref_is_not_abstract():
    assert not inspect.isabstract(java_MethodRef)


def test_java_methodref_constructor_exists():
    assert callable(java_MethodRef.__init__)


def test_java_methodref_constructor_args():
    sig = inspect.signature(java_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java_typeparameter_is_not_abstract():
    assert not inspect.isabstract(java_TypeParameter)


def test_java_typeparameter_constructor_exists():
    assert callable(java_TypeParameter.__init__)


def test_java_typeparameter_constructor_args():
    sig = inspect.signature(java_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AbstractTypeDeclaration)


def test_java_abstracttypedeclaration_constructor_exists():
    assert callable(java_AbstractTypeDeclaration.__init__)


def test_java_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(java_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AbstractMethodDeclaration)


def test_java_abstractmethoddeclaration_constructor_exists():
    assert callable(java_AbstractMethodDeclaration.__init__)


def test_java_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(java_AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(java_WildCardType)


def test_java_wildcardtype_constructor_exists():
    assert callable(java_WildCardType.__init__)


def test_java_wildcardtype_constructor_args():
    sig = inspect.signature(java_WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_java_wildcardtype_has_upperBound():
    assert hasattr(java_WildCardType, "upperBound")
    descriptor = None
    for klass in java_WildCardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



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



def test_java_unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedType)


def test_java_unresolvedtype_constructor_exists():
    assert callable(java_UnresolvedType.__init__)


def test_java_unresolvedtype_constructor_args():
    sig = inspect.signature(java_UnresolvedType.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedInterfaceDeclaration)


def test_java_unresolvedinterfacedeclaration_constructor_exists():
    assert callable(java_UnresolvedInterfaceDeclaration.__init__)


def test_java_unresolvedinterfacedeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedClassDeclaration)


def test_java_unresolvedclassdeclaration_constructor_exists():
    assert callable(java_UnresolvedClassDeclaration.__init__)


def test_java_unresolvedclassdeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedannotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedAnnotationTypeMemberDeclaration)


def test_java_unresolvedannotationtypememberdeclaration_constructor_exists():
    assert callable(java_UnresolvedAnnotationTypeMemberDeclaration.__init__)


def test_java_unresolvedannotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedAnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedSingleVariableDeclaration)


def test_java_unresolvedsinglevariabledeclaration_constructor_exists():
    assert callable(java_UnresolvedSingleVariableDeclaration.__init__)


def test_java_unresolvedsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedMethodDeclaration)


def test_java_unresolvedmethoddeclaration_constructor_exists():
    assert callable(java_UnresolvedMethodDeclaration.__init__)


def test_java_unresolvedmethoddeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedlabeledstatement_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedLabeledStatement)


def test_java_unresolvedlabeledstatement_constructor_exists():
    assert callable(java_UnresolvedLabeledStatement.__init__)


def test_java_unresolvedlabeledstatement_constructor_args():
    sig = inspect.signature(java_UnresolvedLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedenumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedEnumDeclaration)


def test_java_unresolvedenumdeclaration_constructor_exists():
    assert callable(java_UnresolvedEnumDeclaration.__init__)


def test_java_unresolvedenumdeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedEnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedVariableDeclarationFragment)


def test_java_unresolvedvariabledeclarationfragment_constructor_exists():
    assert callable(java_UnresolvedVariableDeclarationFragment.__init__)


def test_java_unresolvedvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(java_UnresolvedVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AnnotationTypeDeclaration)


def test_annotationtypedeclaration_constructor_exists():
    assert callable(AnnotationTypeDeclaration.__init__)


def test_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedannotationdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedAnnotationDeclaration)


def test_java_unresolvedannotationdeclaration_constructor_exists():
    assert callable(java_UnresolvedAnnotationDeclaration.__init__)


def test_java_unresolvedannotationdeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedAnnotationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_typeliteral_is_not_abstract():
    assert not inspect.isabstract(java_TypeLiteral)


def test_java_typeliteral_constructor_exists():
    assert callable(java_TypeLiteral.__init__)


def test_java_typeliteral_constructor_args():
    sig = inspect.signature(java_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_textelement_is_not_abstract():
    assert not inspect.isabstract(java_TextElement)


def test_java_textelement_constructor_exists():
    assert callable(java_TextElement.__init__)


def test_java_textelement_constructor_args():
    sig = inspect.signature(java_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java_textelement_has_text():
    assert hasattr(java_TextElement, "text")
    descriptor = None
    for klass in java_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeQualifiedExpression)


def test_abstracttypequalifiedexpression_constructor_exists():
    assert callable(AbstractTypeQualifiedExpression.__init__)


def test_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_thisexpression_is_not_abstract():
    assert not inspect.isabstract(java_ThisExpression)


def test_java_thisexpression_constructor_exists():
    assert callable(java_ThisExpression.__init__)


def test_java_thisexpression_constructor_args():
    sig = inspect.signature(java_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(java_SuperFieldAccess)


def test_java_superfieldaccess_constructor_exists():
    assert callable(java_SuperFieldAccess.__init__)


def test_java_superfieldaccess_constructor_args():
    sig = inspect.signature(java_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_stringliteral_is_not_abstract():
    assert not inspect.isabstract(java_StringLiteral)


def test_java_stringliteral_constructor_exists():
    assert callable(java_StringLiteral.__init__)


def test_java_stringliteral_constructor_args():
    sig = inspect.signature(java_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java_stringliteral_has_escapedValue():
    assert hasattr(java_StringLiteral, "escapedValue")
    descriptor = None
    for klass in java_StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeByte)


def test_java_primitivetypebyte_constructor_exists():
    assert callable(java_PrimitiveTypeByte.__init__)


def test_java_primitivetypebyte_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeShort)


def test_java_primitivetypeshort_constructor_exists():
    assert callable(java_PrimitiveTypeShort.__init__)


def test_java_primitivetypeshort_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeInt)


def test_java_primitivetypeint_constructor_exists():
    assert callable(java_PrimitiveTypeInt.__init__)


def test_java_primitivetypeint_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeChar)


def test_java_primitivetypechar_constructor_exists():
    assert callable(java_PrimitiveTypeChar.__init__)


def test_java_primitivetypechar_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeVoid)


def test_java_primitivetypevoid_constructor_exists():
    assert callable(java_PrimitiveTypeVoid.__init__)


def test_java_primitivetypevoid_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeDouble)


def test_java_primitivetypedouble_constructor_exists():
    assert callable(java_PrimitiveTypeDouble.__init__)


def test_java_primitivetypedouble_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeLong)


def test_java_primitivetypelong_constructor_exists():
    assert callable(java_PrimitiveTypeLong.__init__)


def test_java_primitivetypelong_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeFloat)


def test_java_primitivetypefloat_constructor_exists():
    assert callable(java_PrimitiveTypeFloat.__init__)


def test_java_primitivetypefloat_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeBoolean)


def test_java_primitivetypeboolean_constructor_exists():
    assert callable(java_PrimitiveTypeBoolean.__init__)


def test_java_primitivetypeboolean_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_java_primitivetype_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveType)


def test_java_primitivetype_constructor_exists():
    assert callable(java_PrimitiveType.__init__)


def test_java_primitivetype_constructor_args():
    sig = inspect.signature(java_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(java_PrefixExpression)


def test_java_prefixexpression_constructor_exists():
    assert callable(java_PrefixExpression.__init__)


def test_java_prefixexpression_constructor_args():
    sig = inspect.signature(java_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_prefixexpression_has_operator():
    assert hasattr(java_PrefixExpression, "operator")
    descriptor = None
    for klass in java_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(java_PostfixExpression)


def test_java_postfixexpression_constructor_exists():
    assert callable(java_PostfixExpression.__init__)


def test_java_postfixexpression_constructor_args():
    sig = inspect.signature(java_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_postfixexpression_has_operator():
    assert hasattr(java_PostfixExpression, "operator")
    descriptor = None
    for klass in java_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(java_ParenthesizedExpression)


def test_java_parenthesizedexpression_constructor_exists():
    assert callable(java_ParenthesizedExpression.__init__)


def test_java_parenthesizedexpression_constructor_args():
    sig = inspect.signature(java_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(java_ParameterizedType)


def test_java_parameterizedtype_constructor_exists():
    assert callable(java_ParameterizedType.__init__)


def test_java_parameterizedtype_constructor_args():
    sig = inspect.signature(java_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolveditemaccess_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedItemAccess)


def test_java_unresolveditemaccess_constructor_exists():
    assert callable(java_UnresolvedItemAccess.__init__)


def test_java_unresolveditemaccess_constructor_args():
    sig = inspect.signature(java_UnresolvedItemAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_typeaccess_is_not_abstract():
    assert not inspect.isabstract(java_TypeAccess)


def test_java_typeaccess_constructor_exists():
    assert callable(java_TypeAccess.__init__)


def test_java_typeaccess_constructor_args():
    sig = inspect.signature(java_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_packageaccess_is_not_abstract():
    assert not inspect.isabstract(java_PackageAccess)


def test_java_packageaccess_constructor_exists():
    assert callable(java_PackageAccess.__init__)


def test_java_packageaccess_constructor_args():
    sig = inspect.signature(java_PackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_nullliteral_is_not_abstract():
    assert not inspect.isabstract(java_NullLiteral)


def test_java_nullliteral_constructor_exists():
    assert callable(java_NullLiteral.__init__)


def test_java_nullliteral_constructor_args():
    sig = inspect.signature(java_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java_numberliteral_is_not_abstract():
    assert not inspect.isabstract(java_NumberLiteral)


def test_java_numberliteral_constructor_exists():
    assert callable(java_NumberLiteral.__init__)


def test_java_numberliteral_constructor_args():
    sig = inspect.signature(java_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java_numberliteral_has_tokenValue():
    assert hasattr(java_NumberLiteral, "tokenValue")
    descriptor = None
    for klass in java_NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(java_NamespaceAccess)


def test_java_namespaceaccess_constructor_exists():
    assert callable(java_NamespaceAccess.__init__)


def test_java_namespaceaccess_constructor_args():
    sig = inspect.signature(java_NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_model_is_not_abstract():
    assert not inspect.isabstract(java_Model)


def test_java_model_constructor_exists():
    assert callable(java_Model.__init__)


def test_java_model_constructor_args():
    sig = inspect.signature(java_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_model_has_name():
    assert hasattr(java_Model, "name")
    descriptor = None
    for klass in java_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(java_MethodRefParameter)


def test_java_methodrefparameter_constructor_exists():
    assert callable(java_MethodRefParameter.__init__)


def test_java_methodrefparameter_constructor_args():
    sig = inspect.signature(java_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_methodrefparameter_has_varargs():
    assert hasattr(java_MethodRefParameter, "varargs")
    descriptor = None
    for klass in java_MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_java_methodrefparameter_has_name():
    assert hasattr(java_MethodRefParameter, "name")
    descriptor = None
    for klass in java_MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_tagelement_is_not_abstract():
    assert not inspect.isabstract(java_TagElement)


def test_java_tagelement_constructor_exists():
    assert callable(java_TagElement.__init__)


def test_java_tagelement_constructor_args():
    sig = inspect.signature(java_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java_tagelement_has_tagName():
    assert hasattr(java_TagElement, "tagName")
    descriptor = None
    for klass in java_TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java_memberref_is_not_abstract():
    assert not inspect.isabstract(java_MemberRef)


def test_java_memberref_constructor_exists():
    assert callable(java_MemberRef.__init__)


def test_java_memberref_constructor_args():
    sig = inspect.signature(java_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java_manifestentry_is_not_abstract():
    assert not inspect.isabstract(java_ManifestEntry)


def test_java_manifestentry_constructor_exists():
    assert callable(java_ManifestEntry.__init__)


def test_java_manifestentry_constructor_args():
    sig = inspect.signature(java_ManifestEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_manifestentry_has_name():
    assert hasattr(java_ManifestEntry, "name")
    descriptor = None
    for klass in java_ManifestEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_manifestattribute_is_not_abstract():
    assert not inspect.isabstract(java_ManifestAttribute)


def test_java_manifestattribute_constructor_exists():
    assert callable(java_ManifestAttribute.__init__)


def test_java_manifestattribute_constructor_args():
    sig = inspect.signature(java_ManifestAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_java_manifestattribute_has_key():
    assert hasattr(java_ManifestAttribute, "key")
    descriptor = None
    for klass in java_ManifestAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_java_manifestattribute_has_value():
    assert hasattr(java_ManifestAttribute, "value")
    descriptor = None
    for klass in java_ManifestAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(java_InstanceofExpression)


def test_java_instanceofexpression_constructor_exists():
    assert callable(java_InstanceofExpression.__init__)


def test_java_instanceofexpression_constructor_args():
    sig = inspect.signature(java_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_initializer_is_not_abstract():
    assert not inspect.isabstract(java_Initializer)


def test_java_initializer_constructor_exists():
    assert callable(java_Initializer.__init__)


def test_java_initializer_constructor_args():
    sig = inspect.signature(java_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java_infixexpression_is_not_abstract():
    assert not inspect.isabstract(java_InfixExpression)


def test_java_infixexpression_constructor_exists():
    assert callable(java_InfixExpression.__init__)


def test_java_infixexpression_constructor_args():
    sig = inspect.signature(java_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_infixexpression_has_operator():
    assert hasattr(java_InfixExpression, "operator")
    descriptor = None
    for klass in java_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_namedelement_is_not_abstract():
    assert not inspect.isabstract(java_NamedElement)


def test_java_namedelement_constructor_exists():
    assert callable(java_NamedElement.__init__)


def test_java_namedelement_constructor_args():
    sig = inspect.signature(java_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_java_namedelement_has_name():
    assert hasattr(java_NamedElement, "name")
    descriptor = None
    for klass in java_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_namedelement_has_proxy():
    assert hasattr(java_NamedElement, "proxy")
    descriptor = None
    for klass in java_NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractVariablesContainer)


def test_abstractvariablescontainer_constructor_exists():
    assert callable(AbstractVariablesContainer.__init__)


def test_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclarationExpression)


def test_java_variabledeclarationexpression_constructor_exists():
    assert callable(java_VariableDeclarationExpression.__init__)


def test_java_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(java_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_FieldDeclaration)


def test_java_fielddeclaration_constructor_exists():
    assert callable(java_FieldDeclaration.__init__)


def test_java_fielddeclaration_constructor_args():
    sig = inspect.signature(java_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_singlevariableaccess_is_not_abstract():
    assert not inspect.isabstract(java_SingleVariableAccess)


def test_java_singlevariableaccess_constructor_exists():
    assert callable(java_SingleVariableAccess.__init__)


def test_java_singlevariableaccess_constructor_args():
    sig = inspect.signature(java_SingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(java_FieldAccess)


def test_java_fieldaccess_constructor_exists():
    assert callable(java_FieldAccess.__init__)


def test_java_fieldaccess_constructor_args():
    sig = inspect.signature(java_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_InterfaceDeclaration)


def test_java_interfacedeclaration_constructor_exists():
    assert callable(java_InterfaceDeclaration.__init__)


def test_java_interfacedeclaration_constructor_args():
    sig = inspect.signature(java_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_ClassDeclaration)


def test_java_classdeclaration_constructor_exists():
    assert callable(java_ClassDeclaration.__init__)


def test_java_classdeclaration_constructor_args():
    sig = inspect.signature(java_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java_SingleVariableDeclaration)


def test_java_singlevariabledeclaration_constructor_exists():
    assert callable(java_SingleVariableDeclaration.__init__)


def test_java_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(java_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java_singlevariabledeclaration_has_varargs():
    assert hasattr(java_SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in java_SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_java_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_EnumConstantDeclaration)


def test_java_enumconstantdeclaration_constructor_exists():
    assert callable(java_EnumConstantDeclaration.__init__)


def test_java_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(java_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_ImportDeclaration)


def test_java_importdeclaration_constructor_exists():
    assert callable(java_ImportDeclaration.__init__)


def test_java_importdeclaration_constructor_args():
    sig = inspect.signature(java_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java_importdeclaration_has_static():
    assert hasattr(java_ImportDeclaration, "static")
    descriptor = None
    for klass in java_ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java_statement_is_not_abstract():
    assert not inspect.isabstract(java_Statement)


def test_java_statement_constructor_exists():
    assert callable(java_Statement.__init__)


def test_java_statement_constructor_args():
    sig = inspect.signature(java_Statement.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_java_javadoc_is_not_abstract():
    assert not inspect.isabstract(java_Javadoc)


def test_java_javadoc_constructor_exists():
    assert callable(java_Javadoc.__init__)


def test_java_javadoc_constructor_args():
    sig = inspect.signature(java_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_java_linecomment_is_not_abstract():
    assert not inspect.isabstract(java_LineComment)


def test_java_linecomment_constructor_exists():
    assert callable(java_LineComment.__init__)


def test_java_linecomment_constructor_args():
    sig = inspect.signature(java_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_java_blockcomment_is_not_abstract():
    assert not inspect.isabstract(java_BlockComment)


def test_java_blockcomment_constructor_exists():
    assert callable(java_BlockComment.__init__)


def test_java_blockcomment_constructor_args():
    sig = inspect.signature(java_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_java_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalExpression)


def test_java_conditionalexpression_constructor_exists():
    assert callable(java_ConditionalExpression.__init__)


def test_java_conditionalexpression_constructor_args():
    sig = inspect.signature(java_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_MethodDeclaration)


def test_java_methoddeclaration_constructor_exists():
    assert callable(java_MethodDeclaration.__init__)


def test_java_methoddeclaration_constructor_args():
    sig = inspect.signature(java_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java_methoddeclaration_has_extraArrayDimensions():
    assert hasattr(java_MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in java_MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(java_ConstructorDeclaration)


def test_java_constructordeclaration_constructor_exists():
    assert callable(java_ConstructorDeclaration.__init__)


def test_java_constructordeclaration_constructor_args():
    sig = inspect.signature(java_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodInvocation)


def test_abstractmethodinvocation_constructor_exists():
    assert callable(AbstractMethodInvocation.__init__)


def test_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java_SuperMethodInvocation)


def test_java_supermethodinvocation_constructor_exists():
    assert callable(java_SuperMethodInvocation.__init__)


def test_java_supermethodinvocation_constructor_args():
    sig = inspect.signature(java_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(java_MethodInvocation)


def test_java_methodinvocation_constructor_exists():
    assert callable(java_MethodInvocation.__init__)


def test_java_methodinvocation_constructor_args():
    sig = inspect.signature(java_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_characterliteral_is_not_abstract():
    assert not inspect.isabstract(java_CharacterLiteral)


def test_java_characterliteral_constructor_exists():
    assert callable(java_CharacterLiteral.__init__)


def test_java_characterliteral_constructor_args():
    sig = inspect.signature(java_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java_characterliteral_has_escapedValue():
    assert hasattr(java_CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in java_CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java_castexpression_is_not_abstract():
    assert not inspect.isabstract(java_CastExpression)


def test_java_castexpression_constructor_exists():
    assert callable(java_CastExpression.__init__)


def test_java_castexpression_constructor_args():
    sig = inspect.signature(java_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java_arraycreation_is_not_abstract():
    assert not inspect.isabstract(java_ArrayCreation)


def test_java_arraycreation_constructor_exists():
    assert callable(java_ArrayCreation.__init__)


def test_java_arraycreation_constructor_args():
    sig = inspect.signature(java_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(java_BooleanLiteral)


def test_java_booleanliteral_constructor_exists():
    assert callable(java_BooleanLiteral.__init__)


def test_java_booleanliteral_constructor_args():
    sig = inspect.signature(java_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java_booleanliteral_has_value():
    assert hasattr(java_BooleanLiteral, "value")
    descriptor = None
    for klass in java_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java_modifier_is_not_abstract():
    assert not inspect.isabstract(java_Modifier)


def test_java_modifier_constructor_exists():
    assert callable(java_Modifier.__init__)


def test_java_modifier_constructor_args():
    sig = inspect.signature(java_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "static" in params, "Missing parameter 'static'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "native" in params, "Missing parameter 'native'"

def test_java_modifier_has_visibility():
    assert hasattr(java_Modifier, "visibility")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_volatile():
    assert hasattr(java_Modifier, "volatile")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_strictfp():
    assert hasattr(java_Modifier, "strictfp")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_synchronized():
    assert hasattr(java_Modifier, "synchronized")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_inheritance():
    assert hasattr(java_Modifier, "inheritance")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_static():
    assert hasattr(java_Modifier, "static")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_transient():
    assert hasattr(java_Modifier, "transient")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java_modifier_has_native():
    assert hasattr(java_Modifier, "native")
    descriptor = None
    for klass in java_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)



def test_java_assignment_is_not_abstract():
    assert not inspect.isabstract(java_Assignment)


def test_java_assignment_constructor_exists():
    assert callable(java_Assignment.__init__)


def test_java_assignment_constructor_args():
    sig = inspect.signature(java_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java_assignment_has_operator():
    assert hasattr(java_Assignment, "operator")
    descriptor = None
    for klass in java_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java_arraytype_is_not_abstract():
    assert not inspect.isabstract(java_ArrayType)


def test_java_arraytype_constructor_exists():
    assert callable(java_ArrayType.__init__)


def test_java_arraytype_constructor_args():
    sig = inspect.signature(java_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_java_arraytype_has_dimensions():
    assert hasattr(java_ArrayType, "dimensions")
    descriptor = None
    for klass in java_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(java_ArrayLengthAccess)


def test_java_arraylengthaccess_constructor_exists():
    assert callable(java_ArrayLengthAccess.__init__)


def test_java_arraylengthaccess_constructor_args():
    sig = inspect.signature(java_ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInitializer)


def test_java_arrayinitializer_constructor_exists():
    assert callable(java_ArrayInitializer.__init__)


def test_java_arrayinitializer_constructor_args():
    sig = inspect.signature(java_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclarationFragment)


def test_java_variabledeclarationfragment_constructor_exists():
    assert callable(java_VariableDeclarationFragment.__init__)


def test_java_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(java_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(java_ArrayAccess)


def test_java_arrayaccess_constructor_exists():
    assert callable(java_ArrayAccess.__init__)


def test_java_arrayaccess_constructor_args():
    sig = inspect.signature(java_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(java_ClassInstanceCreation)


def test_java_classinstancecreation_constructor_exists():
    assert callable(java_ClassInstanceCreation.__init__)


def test_java_classinstancecreation_constructor_args():
    sig = inspect.signature(java_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AnonymousClassDeclaration)


def test_java_anonymousclassdeclaration_constructor_exists():
    assert callable(java_AnonymousClassDeclaration.__init__)


def test_java_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(java_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_EnumDeclaration)


def test_java_enumdeclaration_constructor_exists():
    assert callable(java_EnumDeclaration.__init__)


def test_java_enumdeclaration_constructor_args():
    sig = inspect.signature(java_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolvedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedTypeDeclaration)


def test_java_unresolvedtypedeclaration_constructor_exists():
    assert callable(java_UnresolvedTypeDeclaration.__init__)


def test_java_unresolvedtypedeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_TypeDeclaration)


def test_java_typedeclaration_constructor_exists():
    assert callable(java_TypeDeclaration.__init__)


def test_java_typedeclaration_constructor_args():
    sig = inspect.signature(java_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationTypeDeclaration)


def test_java_annotationtypedeclaration_constructor_exists():
    assert callable(java_AnnotationTypeDeclaration.__init__)


def test_java_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(java_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationTypeMemberDeclaration)


def test_java_annotationtypememberdeclaration_constructor_exists():
    assert callable(java_AnnotationTypeMemberDeclaration.__init__)


def test_java_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_astnode_is_not_abstract():
    assert not inspect.isabstract(java_ASTNode)


def test_java_astnode_constructor_exists():
    assert callable(java_ASTNode.__init__)


def test_java_astnode_constructor_args():
    sig = inspect.signature(java_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(java_ExpressionStatement)


def test_java_expressionstatement_constructor_exists():
    assert callable(java_ExpressionStatement.__init__)


def test_java_expressionstatement_constructor_args():
    sig = inspect.signature(java_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java_SuperConstructorInvocation)


def test_java_superconstructorinvocation_constructor_exists():
    assert callable(java_SuperConstructorInvocation.__init__)


def test_java_superconstructorinvocation_constructor_args():
    sig = inspect.signature(java_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_trystatement_is_not_abstract():
    assert not inspect.isabstract(java_TryStatement)


def test_java_trystatement_constructor_exists():
    assert callable(java_TryStatement.__init__)


def test_java_trystatement_constructor_args():
    sig = inspect.signature(java_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_breakstatement_is_not_abstract():
    assert not inspect.isabstract(java_BreakStatement)


def test_java_breakstatement_constructor_exists():
    assert callable(java_BreakStatement.__init__)


def test_java_breakstatement_constructor_args():
    sig = inspect.signature(java_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_forstatement_is_not_abstract():
    assert not inspect.isabstract(java_ForStatement)


def test_java_forstatement_constructor_exists():
    assert callable(java_ForStatement.__init__)


def test_java_forstatement_constructor_args():
    sig = inspect.signature(java_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_catchclause_is_not_abstract():
    assert not inspect.isabstract(java_CatchClause)


def test_java_catchclause_constructor_exists():
    assert callable(java_CatchClause.__init__)


def test_java_catchclause_constructor_args():
    sig = inspect.signature(java_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java_continuestatement_is_not_abstract():
    assert not inspect.isabstract(java_ContinueStatement)


def test_java_continuestatement_constructor_exists():
    assert callable(java_ContinueStatement.__init__)


def test_java_continuestatement_constructor_args():
    sig = inspect.signature(java_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_whilestatement_is_not_abstract():
    assert not inspect.isabstract(java_WhileStatement)


def test_java_whilestatement_constructor_exists():
    assert callable(java_WhileStatement.__init__)


def test_java_whilestatement_constructor_args():
    sig = inspect.signature(java_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_ifstatement_is_not_abstract():
    assert not inspect.isabstract(java_IfStatement)


def test_java_ifstatement_constructor_exists():
    assert callable(java_IfStatement.__init__)


def test_java_ifstatement_constructor_args():
    sig = inspect.signature(java_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_returnstatement_is_not_abstract():
    assert not inspect.isabstract(java_ReturnStatement)


def test_java_returnstatement_constructor_exists():
    assert callable(java_ReturnStatement.__init__)


def test_java_returnstatement_constructor_args():
    sig = inspect.signature(java_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_switchstatement_is_not_abstract():
    assert not inspect.isabstract(java_SwitchStatement)


def test_java_switchstatement_constructor_exists():
    assert callable(java_SwitchStatement.__init__)


def test_java_switchstatement_constructor_args():
    sig = inspect.signature(java_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java_ConstructorInvocation)


def test_java_constructorinvocation_constructor_exists():
    assert callable(java_ConstructorInvocation.__init__)


def test_java_constructorinvocation_constructor_args():
    sig = inspect.signature(java_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java_emptystatement_is_not_abstract():
    assert not inspect.isabstract(java_EmptyStatement)


def test_java_emptystatement_constructor_exists():
    assert callable(java_EmptyStatement.__init__)


def test_java_emptystatement_constructor_args():
    sig = inspect.signature(java_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_block_is_not_abstract():
    assert not inspect.isabstract(java_Block)


def test_java_block_constructor_exists():
    assert callable(java_Block.__init__)


def test_java_block_constructor_args():
    sig = inspect.signature(java_Block.__init__)
    params = list(sig.parameters.keys())



def test_java_switchcase_is_not_abstract():
    assert not inspect.isabstract(java_SwitchCase)


def test_java_switchcase_constructor_exists():
    assert callable(java_SwitchCase.__init__)


def test_java_switchcase_constructor_args():
    sig = inspect.signature(java_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java_switchcase_has_default():
    assert hasattr(java_SwitchCase, "default")
    descriptor = None
    for klass in java_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(java_SynchronizedStatement)


def test_java_synchronizedstatement_constructor_exists():
    assert callable(java_SynchronizedStatement.__init__)


def test_java_synchronizedstatement_constructor_args():
    sig = inspect.signature(java_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(java_EnhancedForStatement)


def test_java_enhancedforstatement_constructor_exists():
    assert callable(java_EnhancedForStatement.__init__)


def test_java_enhancedforstatement_constructor_args():
    sig = inspect.signature(java_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclarationStatement)


def test_java_variabledeclarationstatement_constructor_exists():
    assert callable(java_VariableDeclarationStatement.__init__)


def test_java_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(java_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java_variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(java_VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in java_VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_throwstatement_is_not_abstract():
    assert not inspect.isabstract(java_ThrowStatement)


def test_java_throwstatement_constructor_exists():
    assert callable(java_ThrowStatement.__init__)


def test_java_throwstatement_constructor_args():
    sig = inspect.signature(java_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java_TypeDeclarationStatement)


def test_java_typedeclarationstatement_constructor_exists():
    assert callable(java_TypeDeclarationStatement.__init__)


def test_java_typedeclarationstatement_constructor_args():
    sig = inspect.signature(java_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_dostatement_is_not_abstract():
    assert not inspect.isabstract(java_DoStatement)


def test_java_dostatement_constructor_exists():
    assert callable(java_DoStatement.__init__)


def test_java_dostatement_constructor_args():
    sig = inspect.signature(java_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_assertstatement_is_not_abstract():
    assert not inspect.isabstract(java_AssertStatement)


def test_java_assertstatement_constructor_exists():
    assert callable(java_AssertStatement.__init__)


def test_java_assertstatement_constructor_args():
    sig = inspect.signature(java_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_manifest_is_not_abstract():
    assert not inspect.isabstract(java_Manifest)


def test_java_manifest_constructor_exists():
    assert callable(java_Manifest.__init__)


def test_java_manifest_constructor_args():
    sig = inspect.signature(java_Manifest.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java_instancespecification_is_not_abstract():
    assert not inspect.isabstract(java_InstanceSpecification)


def test_java_instancespecification_constructor_exists():
    assert callable(java_InstanceSpecification.__init__)


def test_java_instancespecification_constructor_args():
    sig = inspect.signature(java_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_java_compilationunit_is_not_abstract():
    assert not inspect.isabstract(java_CompilationUnit)


def test_java_compilationunit_constructor_exists():
    assert callable(java_CompilationUnit.__init__)


def test_java_compilationunit_constructor_args():
    sig = inspect.signature(java_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java_compilationunit_has_originalFilePath():
    assert hasattr(java_CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in java_CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java_package_is_not_abstract():
    assert not inspect.isabstract(java_Package)


def test_java_package_constructor_exists():
    assert callable(java_Package.__init__)


def test_java_package_constructor_args():
    sig = inspect.signature(java_Package.__init__)
    params = list(sig.parameters.keys())



def test_java_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclaration)


def test_java_variabledeclaration_constructor_exists():
    assert callable(java_VariableDeclaration.__init__)


def test_java_variabledeclaration_constructor_args():
    sig = inspect.signature(java_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java_variabledeclaration_has_extraArrayDimensions():
    assert hasattr(java_VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in java_VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java_archive_is_not_abstract():
    assert not inspect.isabstract(java_Archive)


def test_java_archive_constructor_exists():
    assert callable(java_Archive.__init__)


def test_java_archive_constructor_args():
    sig = inspect.signature(java_Archive.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java_archive_has_originalFilePath():
    assert hasattr(java_Archive, "originalFilePath")
    descriptor = None
    for klass in java_Archive.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java_classfile_is_not_abstract():
    assert not inspect.isabstract(java_ClassFile)


def test_java_classfile_constructor_exists():
    assert callable(java_ClassFile.__init__)


def test_java_classfile_constructor_args():
    sig = inspect.signature(java_ClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java_classfile_has_originalFilePath():
    assert hasattr(java_ClassFile, "originalFilePath")
    descriptor = None
    for klass in java_ClassFile.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(java_BodyDeclaration)


def test_java_bodydeclaration_constructor_exists():
    assert callable(java_BodyDeclaration.__init__)


def test_java_bodydeclaration_constructor_args():
    sig = inspect.signature(java_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(java_LabeledStatement)


def test_java_labeledstatement_constructor_exists():
    assert callable(java_LabeledStatement.__init__)


def test_java_labeledstatement_constructor_args():
    sig = inspect.signature(java_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedItem)


def test_java_unresolveditem_constructor_exists():
    assert callable(java_UnresolvedItem.__init__)


def test_java_unresolveditem_constructor_args():
    sig = inspect.signature(java_UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java_annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationMemberValuePair)


def test_java_annotationmembervaluepair_constructor_exists():
    assert callable(java_AnnotationMemberValuePair.__init__)


def test_java_annotationmembervaluepair_constructor_args():
    sig = inspect.signature(java_AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_java_type_is_not_abstract():
    assert not inspect.isabstract(java_Type)


def test_java_type_constructor_exists():
    assert callable(java_Type.__init__)


def test_java_type_constructor_args():
    sig = inspect.signature(java_Type.__init__)
    params = list(sig.parameters.keys())

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

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "protected",
        "none",
        "public",
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

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "LEFT_SHIFT_ASSIGN",
        "BIT_AND_ASSIGN",
        "REMAINDER_ASSIGN",
        "ASSIGN",
        "BIT_XOR_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "TIMES_ASSIGN",
        "MINUS_ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "BIT_OR_ASSIGN",
        "PLUS_ASSIGN",
        "DIVIDE_ASSIGN",
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
        "INCREMENT",
        "MINUS",
        "DECREMENT",
        "COMPLEMENT",
        "PLUS",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionKind"

def test_infixexpressionkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionKind is not None

def test_infixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionKind]
    expected_literals = [
        "MINUS",
        "LESS_EQUALS",
        "CONDITIONAL_OR",
        "LEFT_SHIFT",
        "RIGHT_SHIFT_UNSIGNED",
        "OR",
        "PLUS",
        "CONDITIONAL_AND",
        "REMAINDER",
        "LESS",
        "TIMES",
        "RIGHT_SHIFT_SIGNED",
        "AND",
        "DIVIDE",
        "NOT_EQUALS",
        "GREATER_EQUALS",
        "XOR",
        "EQUALS",
        "GREATER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionKind"


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
java_Annotation_strategy = st.builds(
    java_Annotation,
)
java_AbstractTypeQualifiedExpression_strategy = st.builds(
    java_AbstractTypeQualifiedExpression,
)
Type_strategy = st.builds(
    Type,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
java_AbstractVariablesContainer_strategy = st.builds(
    java_AbstractVariablesContainer,
)
java_Comment_strategy = st.builds(
    java_Comment,
    content=
        safe_text,
    prefixOfParent=
        st.booleans(),
    enclosedByParent=
        st.booleans()
)
java_Expression_strategy = st.builds(
    java_Expression,
)
java_AbstractMethodInvocation_strategy = st.builds(
    java_AbstractMethodInvocation,
)
java_MethodRef_strategy = st.builds(
    java_MethodRef,
)
java_TypeParameter_strategy = st.builds(
    java_TypeParameter,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
java_AbstractTypeDeclaration_strategy = st.builds(
    java_AbstractTypeDeclaration,
)
java_AbstractMethodDeclaration_strategy = st.builds(
    java_AbstractMethodDeclaration,
)
java_WildCardType_strategy = st.builds(
    java_WildCardType,
    upperBound=
        st.booleans()
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
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
java_UnresolvedType_strategy = st.builds(
    java_UnresolvedType,
)
java_UnresolvedInterfaceDeclaration_strategy = st.builds(
    java_UnresolvedInterfaceDeclaration,
)
java_UnresolvedClassDeclaration_strategy = st.builds(
    java_UnresolvedClassDeclaration,
)
java_UnresolvedAnnotationTypeMemberDeclaration_strategy = st.builds(
    java_UnresolvedAnnotationTypeMemberDeclaration,
)
java_UnresolvedSingleVariableDeclaration_strategy = st.builds(
    java_UnresolvedSingleVariableDeclaration,
)
java_UnresolvedMethodDeclaration_strategy = st.builds(
    java_UnresolvedMethodDeclaration,
)
java_UnresolvedLabeledStatement_strategy = st.builds(
    java_UnresolvedLabeledStatement,
)
java_UnresolvedEnumDeclaration_strategy = st.builds(
    java_UnresolvedEnumDeclaration,
)
java_UnresolvedVariableDeclarationFragment_strategy = st.builds(
    java_UnresolvedVariableDeclarationFragment,
)
AnnotationTypeDeclaration_strategy = st.builds(
    AnnotationTypeDeclaration,
)
java_UnresolvedAnnotationDeclaration_strategy = st.builds(
    java_UnresolvedAnnotationDeclaration,
)
java_TypeLiteral_strategy = st.builds(
    java_TypeLiteral,
)
java_TextElement_strategy = st.builds(
    java_TextElement,
    text=
        safe_text
)
AbstractTypeQualifiedExpression_strategy = st.builds(
    AbstractTypeQualifiedExpression,
)
java_ThisExpression_strategy = st.builds(
    java_ThisExpression,
)
java_SuperFieldAccess_strategy = st.builds(
    java_SuperFieldAccess,
)
java_StringLiteral_strategy = st.builds(
    java_StringLiteral,
    escapedValue=
        safe_text
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
java_PrimitiveTypeByte_strategy = st.builds(
    java_PrimitiveTypeByte,
)
java_PrimitiveTypeShort_strategy = st.builds(
    java_PrimitiveTypeShort,
)
java_PrimitiveTypeInt_strategy = st.builds(
    java_PrimitiveTypeInt,
)
java_PrimitiveTypeChar_strategy = st.builds(
    java_PrimitiveTypeChar,
)
java_PrimitiveTypeVoid_strategy = st.builds(
    java_PrimitiveTypeVoid,
)
java_PrimitiveTypeDouble_strategy = st.builds(
    java_PrimitiveTypeDouble,
)
java_PrimitiveTypeLong_strategy = st.builds(
    java_PrimitiveTypeLong,
)
java_PrimitiveTypeFloat_strategy = st.builds(
    java_PrimitiveTypeFloat,
)
java_PrimitiveTypeBoolean_strategy = st.builds(
    java_PrimitiveTypeBoolean,
)
java_PrimitiveType_strategy = st.builds(
    java_PrimitiveType,
)
java_PrefixExpression_strategy = st.builds(
    java_PrefixExpression,
    operator=
        safe_text
)
java_PostfixExpression_strategy = st.builds(
    java_PostfixExpression,
    operator=
        safe_text
)
java_ParenthesizedExpression_strategy = st.builds(
    java_ParenthesizedExpression,
)
java_ParameterizedType_strategy = st.builds(
    java_ParameterizedType,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
java_UnresolvedItemAccess_strategy = st.builds(
    java_UnresolvedItemAccess,
)
java_TypeAccess_strategy = st.builds(
    java_TypeAccess,
)
java_PackageAccess_strategy = st.builds(
    java_PackageAccess,
)
java_NullLiteral_strategy = st.builds(
    java_NullLiteral,
)
java_NumberLiteral_strategy = st.builds(
    java_NumberLiteral,
    tokenValue=
        safe_text
)
java_NamespaceAccess_strategy = st.builds(
    java_NamespaceAccess,
)
java_Model_strategy = st.builds(
    java_Model,
    name=
        safe_text
)
java_MethodRefParameter_strategy = st.builds(
    java_MethodRefParameter,
    varargs=
        st.booleans(),
    name=
        safe_text
)
java_TagElement_strategy = st.builds(
    java_TagElement,
    tagName=
        safe_text
)
java_MemberRef_strategy = st.builds(
    java_MemberRef,
)
java_ManifestEntry_strategy = st.builds(
    java_ManifestEntry,
    name=
        safe_text
)
java_ManifestAttribute_strategy = st.builds(
    java_ManifestAttribute,
    key=
        safe_text,
    value=
        safe_text
)
java_InstanceofExpression_strategy = st.builds(
    java_InstanceofExpression,
)
java_Initializer_strategy = st.builds(
    java_Initializer,
)
java_InfixExpression_strategy = st.builds(
    java_InfixExpression,
    operator=
        safe_text
)
java_NamedElement_strategy = st.builds(
    java_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
java_VariableDeclarationExpression_strategy = st.builds(
    java_VariableDeclarationExpression,
)
java_FieldDeclaration_strategy = st.builds(
    java_FieldDeclaration,
)
java_SingleVariableAccess_strategy = st.builds(
    java_SingleVariableAccess,
)
java_FieldAccess_strategy = st.builds(
    java_FieldAccess,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
java_InterfaceDeclaration_strategy = st.builds(
    java_InterfaceDeclaration,
)
java_ClassDeclaration_strategy = st.builds(
    java_ClassDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
java_SingleVariableDeclaration_strategy = st.builds(
    java_SingleVariableDeclaration,
    varargs=
        st.booleans()
)
java_EnumConstantDeclaration_strategy = st.builds(
    java_EnumConstantDeclaration,
)
java_ImportDeclaration_strategy = st.builds(
    java_ImportDeclaration,
    static=
        st.booleans()
)
java_Statement_strategy = st.builds(
    java_Statement,
)
Comment_strategy = st.builds(
    Comment,
)
java_Javadoc_strategy = st.builds(
    java_Javadoc,
)
java_LineComment_strategy = st.builds(
    java_LineComment,
)
java_BlockComment_strategy = st.builds(
    java_BlockComment,
)
java_ConditionalExpression_strategy = st.builds(
    java_ConditionalExpression,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
java_MethodDeclaration_strategy = st.builds(
    java_MethodDeclaration,
    extraArrayDimensions=
        st.integers()
)
java_ConstructorDeclaration_strategy = st.builds(
    java_ConstructorDeclaration,
)
AbstractMethodInvocation_strategy = st.builds(
    AbstractMethodInvocation,
)
java_SuperMethodInvocation_strategy = st.builds(
    java_SuperMethodInvocation,
)
java_MethodInvocation_strategy = st.builds(
    java_MethodInvocation,
)
java_CharacterLiteral_strategy = st.builds(
    java_CharacterLiteral,
    escapedValue=
        safe_text
)
java_CastExpression_strategy = st.builds(
    java_CastExpression,
)
java_ArrayCreation_strategy = st.builds(
    java_ArrayCreation,
)
java_BooleanLiteral_strategy = st.builds(
    java_BooleanLiteral,
    value=
        st.booleans()
)
java_Modifier_strategy = st.builds(
    java_Modifier,
    visibility=
        safe_text,
    volatile=
        st.booleans(),
    strictfp=
        st.booleans(),
    synchronized=
        st.booleans(),
    inheritance=
        safe_text,
    static=
        st.booleans(),
    transient=
        st.booleans(),
    native=
        st.booleans()
)
java_Assignment_strategy = st.builds(
    java_Assignment,
    operator=
        safe_text
)
java_ArrayType_strategy = st.builds(
    java_ArrayType,
    dimensions=
        st.integers()
)
java_ArrayLengthAccess_strategy = st.builds(
    java_ArrayLengthAccess,
)
java_ArrayInitializer_strategy = st.builds(
    java_ArrayInitializer,
)
java_VariableDeclarationFragment_strategy = st.builds(
    java_VariableDeclarationFragment,
)
java_ArrayAccess_strategy = st.builds(
    java_ArrayAccess,
)
java_ClassInstanceCreation_strategy = st.builds(
    java_ClassInstanceCreation,
)
java_AnonymousClassDeclaration_strategy = st.builds(
    java_AnonymousClassDeclaration,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
java_EnumDeclaration_strategy = st.builds(
    java_EnumDeclaration,
)
java_UnresolvedTypeDeclaration_strategy = st.builds(
    java_UnresolvedTypeDeclaration,
)
java_TypeDeclaration_strategy = st.builds(
    java_TypeDeclaration,
)
java_AnnotationTypeDeclaration_strategy = st.builds(
    java_AnnotationTypeDeclaration,
)
java_AnnotationTypeMemberDeclaration_strategy = st.builds(
    java_AnnotationTypeMemberDeclaration,
)
java_ASTNode_strategy = st.builds(
    java_ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
java_ExpressionStatement_strategy = st.builds(
    java_ExpressionStatement,
)
java_SuperConstructorInvocation_strategy = st.builds(
    java_SuperConstructorInvocation,
)
java_TryStatement_strategy = st.builds(
    java_TryStatement,
)
java_BreakStatement_strategy = st.builds(
    java_BreakStatement,
)
java_ForStatement_strategy = st.builds(
    java_ForStatement,
)
java_CatchClause_strategy = st.builds(
    java_CatchClause,
)
java_ContinueStatement_strategy = st.builds(
    java_ContinueStatement,
)
java_WhileStatement_strategy = st.builds(
    java_WhileStatement,
)
java_IfStatement_strategy = st.builds(
    java_IfStatement,
)
java_ReturnStatement_strategy = st.builds(
    java_ReturnStatement,
)
java_SwitchStatement_strategy = st.builds(
    java_SwitchStatement,
)
java_ConstructorInvocation_strategy = st.builds(
    java_ConstructorInvocation,
)
java_EmptyStatement_strategy = st.builds(
    java_EmptyStatement,
)
java_Block_strategy = st.builds(
    java_Block,
)
java_SwitchCase_strategy = st.builds(
    java_SwitchCase,
    default=
        st.booleans()
)
java_SynchronizedStatement_strategy = st.builds(
    java_SynchronizedStatement,
)
java_EnhancedForStatement_strategy = st.builds(
    java_EnhancedForStatement,
)
java_VariableDeclarationStatement_strategy = st.builds(
    java_VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
java_ThrowStatement_strategy = st.builds(
    java_ThrowStatement,
)
java_TypeDeclarationStatement_strategy = st.builds(
    java_TypeDeclarationStatement,
)
java_DoStatement_strategy = st.builds(
    java_DoStatement,
)
java_AssertStatement_strategy = st.builds(
    java_AssertStatement,
)
java_Manifest_strategy = st.builds(
    java_Manifest,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
java_InstanceSpecification_strategy = st.builds(
    java_InstanceSpecification,
)
java_CompilationUnit_strategy = st.builds(
    java_CompilationUnit,
    originalFilePath=
        safe_text
)
java_Package_strategy = st.builds(
    java_Package,
)
java_VariableDeclaration_strategy = st.builds(
    java_VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
java_Archive_strategy = st.builds(
    java_Archive,
    originalFilePath=
        safe_text
)
java_ClassFile_strategy = st.builds(
    java_ClassFile,
    originalFilePath=
        safe_text
)
java_BodyDeclaration_strategy = st.builds(
    java_BodyDeclaration,
)
java_LabeledStatement_strategy = st.builds(
    java_LabeledStatement,
)
java_UnresolvedItem_strategy = st.builds(
    java_UnresolvedItem,
)
java_AnnotationMemberValuePair_strategy = st.builds(
    java_AnnotationMemberValuePair,
)
java_Type_strategy = st.builds(
    java_Type,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=java_Annotation_strategy)
@settings(max_examples=50)
def test_java_annotation_instantiation(instance):
    assert isinstance(instance, java_Annotation)

@given(instance=java_AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_java_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, java_AbstractTypeQualifiedExpression)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=java_AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_java_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, java_AbstractVariablesContainer)

@given(instance=java_Comment_strategy)
@settings(max_examples=50)
def test_java_comment_instantiation(instance):
    assert isinstance(instance, java_Comment)



@given(instance=java_Comment_strategy)
def test_java_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=java_Comment_strategy)
def test_java_comment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original



@given(instance=java_Comment_strategy)
def test_java_comment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original

@given(instance=java_Expression_strategy)
@settings(max_examples=50)
def test_java_expression_instantiation(instance):
    assert isinstance(instance, java_Expression)

@given(instance=java_AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_java_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, java_AbstractMethodInvocation)

@given(instance=java_MethodRef_strategy)
@settings(max_examples=50)
def test_java_methodref_instantiation(instance):
    assert isinstance(instance, java_MethodRef)

@given(instance=java_TypeParameter_strategy)
@settings(max_examples=50)
def test_java_typeparameter_instantiation(instance):
    assert isinstance(instance, java_TypeParameter)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=java_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, java_AbstractTypeDeclaration)

@given(instance=java_AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, java_AbstractMethodDeclaration)

@given(instance=java_WildCardType_strategy)
@settings(max_examples=50)
def test_java_wildcardtype_instantiation(instance):
    assert isinstance(instance, java_WildCardType)



@given(instance=java_WildCardType_strategy)
def test_java_wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

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

@given(instance=java_UnresolvedType_strategy)
@settings(max_examples=50)
def test_java_unresolvedtype_instantiation(instance):
    assert isinstance(instance, java_UnresolvedType)

@given(instance=java_UnresolvedInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedInterfaceDeclaration)

@given(instance=java_UnresolvedClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedclassdeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedClassDeclaration)

@given(instance=java_UnresolvedAnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedannotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedAnnotationTypeMemberDeclaration)

@given(instance=java_UnresolvedSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedSingleVariableDeclaration)

@given(instance=java_UnresolvedMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedmethoddeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedMethodDeclaration)

@given(instance=java_UnresolvedLabeledStatement_strategy)
@settings(max_examples=50)
def test_java_unresolvedlabeledstatement_instantiation(instance):
    assert isinstance(instance, java_UnresolvedLabeledStatement)

@given(instance=java_UnresolvedEnumDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedenumdeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedEnumDeclaration)

@given(instance=java_UnresolvedVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java_unresolvedvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, java_UnresolvedVariableDeclarationFragment)

@given(instance=AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeDeclaration)

@given(instance=java_UnresolvedAnnotationDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedannotationdeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedAnnotationDeclaration)

@given(instance=java_TypeLiteral_strategy)
@settings(max_examples=50)
def test_java_typeliteral_instantiation(instance):
    assert isinstance(instance, java_TypeLiteral)

@given(instance=java_TextElement_strategy)
@settings(max_examples=50)
def test_java_textelement_instantiation(instance):
    assert isinstance(instance, java_TextElement)



@given(instance=java_TextElement_strategy)
def test_java_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, AbstractTypeQualifiedExpression)

@given(instance=java_ThisExpression_strategy)
@settings(max_examples=50)
def test_java_thisexpression_instantiation(instance):
    assert isinstance(instance, java_ThisExpression)

@given(instance=java_SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java_superfieldaccess_instantiation(instance):
    assert isinstance(instance, java_SuperFieldAccess)

@given(instance=java_StringLiteral_strategy)
@settings(max_examples=50)
def test_java_stringliteral_instantiation(instance):
    assert isinstance(instance, java_StringLiteral)



@given(instance=java_StringLiteral_strategy)
def test_java_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=java_PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java_primitivetypebyte_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeByte)

@given(instance=java_PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java_primitivetypeshort_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeShort)

@given(instance=java_PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java_primitivetypeint_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeInt)

@given(instance=java_PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java_primitivetypechar_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeChar)

@given(instance=java_PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java_primitivetypevoid_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeVoid)

@given(instance=java_PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java_primitivetypedouble_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeDouble)

@given(instance=java_PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java_primitivetypelong_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeLong)

@given(instance=java_PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java_primitivetypefloat_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeFloat)

@given(instance=java_PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java_primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeBoolean)

@given(instance=java_PrimitiveType_strategy)
@settings(max_examples=50)
def test_java_primitivetype_instantiation(instance):
    assert isinstance(instance, java_PrimitiveType)

@given(instance=java_PrefixExpression_strategy)
@settings(max_examples=50)
def test_java_prefixexpression_instantiation(instance):
    assert isinstance(instance, java_PrefixExpression)



@given(instance=java_PrefixExpression_strategy)
def test_java_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java_PostfixExpression_strategy)
@settings(max_examples=50)
def test_java_postfixexpression_instantiation(instance):
    assert isinstance(instance, java_PostfixExpression)



@given(instance=java_PostfixExpression_strategy)
def test_java_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, java_ParenthesizedExpression)

@given(instance=java_ParameterizedType_strategy)
@settings(max_examples=50)
def test_java_parameterizedtype_instantiation(instance):
    assert isinstance(instance, java_ParameterizedType)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=java_UnresolvedItemAccess_strategy)
@settings(max_examples=50)
def test_java_unresolveditemaccess_instantiation(instance):
    assert isinstance(instance, java_UnresolvedItemAccess)

@given(instance=java_TypeAccess_strategy)
@settings(max_examples=50)
def test_java_typeaccess_instantiation(instance):
    assert isinstance(instance, java_TypeAccess)

@given(instance=java_PackageAccess_strategy)
@settings(max_examples=50)
def test_java_packageaccess_instantiation(instance):
    assert isinstance(instance, java_PackageAccess)

@given(instance=java_NullLiteral_strategy)
@settings(max_examples=50)
def test_java_nullliteral_instantiation(instance):
    assert isinstance(instance, java_NullLiteral)

@given(instance=java_NumberLiteral_strategy)
@settings(max_examples=50)
def test_java_numberliteral_instantiation(instance):
    assert isinstance(instance, java_NumberLiteral)



@given(instance=java_NumberLiteral_strategy)
def test_java_numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=java_NamespaceAccess_strategy)
@settings(max_examples=50)
def test_java_namespaceaccess_instantiation(instance):
    assert isinstance(instance, java_NamespaceAccess)

@given(instance=java_Model_strategy)
@settings(max_examples=50)
def test_java_model_instantiation(instance):
    assert isinstance(instance, java_Model)



@given(instance=java_Model_strategy)
def test_java_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java_methodrefparameter_instantiation(instance):
    assert isinstance(instance, java_MethodRefParameter)



@given(instance=java_MethodRefParameter_strategy)
def test_java_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original



@given(instance=java_MethodRefParameter_strategy)
def test_java_methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_TagElement_strategy)
@settings(max_examples=50)
def test_java_tagelement_instantiation(instance):
    assert isinstance(instance, java_TagElement)



@given(instance=java_TagElement_strategy)
def test_java_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=java_MemberRef_strategy)
@settings(max_examples=50)
def test_java_memberref_instantiation(instance):
    assert isinstance(instance, java_MemberRef)

@given(instance=java_ManifestEntry_strategy)
@settings(max_examples=50)
def test_java_manifestentry_instantiation(instance):
    assert isinstance(instance, java_ManifestEntry)



@given(instance=java_ManifestEntry_strategy)
def test_java_manifestentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_ManifestAttribute_strategy)
@settings(max_examples=50)
def test_java_manifestattribute_instantiation(instance):
    assert isinstance(instance, java_ManifestAttribute)



@given(instance=java_ManifestAttribute_strategy)
def test_java_manifestattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=java_ManifestAttribute_strategy)
def test_java_manifestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java_InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java_instanceofexpression_instantiation(instance):
    assert isinstance(instance, java_InstanceofExpression)

@given(instance=java_Initializer_strategy)
@settings(max_examples=50)
def test_java_initializer_instantiation(instance):
    assert isinstance(instance, java_Initializer)

@given(instance=java_InfixExpression_strategy)
@settings(max_examples=50)
def test_java_infixexpression_instantiation(instance):
    assert isinstance(instance, java_InfixExpression)



@given(instance=java_InfixExpression_strategy)
def test_java_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java_NamedElement_strategy)
@settings(max_examples=50)
def test_java_namedelement_instantiation(instance):
    assert isinstance(instance, java_NamedElement)



@given(instance=java_NamedElement_strategy)
def test_java_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_NamedElement_strategy)
def test_java_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)

@given(instance=java_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, java_VariableDeclarationExpression)

@given(instance=java_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java_fielddeclaration_instantiation(instance):
    assert isinstance(instance, java_FieldDeclaration)

@given(instance=java_SingleVariableAccess_strategy)
@settings(max_examples=50)
def test_java_singlevariableaccess_instantiation(instance):
    assert isinstance(instance, java_SingleVariableAccess)

@given(instance=java_FieldAccess_strategy)
@settings(max_examples=50)
def test_java_fieldaccess_instantiation(instance):
    assert isinstance(instance, java_FieldAccess)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=java_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, java_InterfaceDeclaration)

@given(instance=java_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_classdeclaration_instantiation(instance):
    assert isinstance(instance, java_ClassDeclaration)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=java_SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, java_SingleVariableDeclaration)



@given(instance=java_SingleVariableDeclaration_strategy)
def test_java_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=java_EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, java_EnumConstantDeclaration)

@given(instance=java_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java_importdeclaration_instantiation(instance):
    assert isinstance(instance, java_ImportDeclaration)



@given(instance=java_ImportDeclaration_strategy)
def test_java_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=java_Statement_strategy)
@settings(max_examples=50)
def test_java_statement_instantiation(instance):
    assert isinstance(instance, java_Statement)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=java_Javadoc_strategy)
@settings(max_examples=50)
def test_java_javadoc_instantiation(instance):
    assert isinstance(instance, java_Javadoc)

@given(instance=java_LineComment_strategy)
@settings(max_examples=50)
def test_java_linecomment_instantiation(instance):
    assert isinstance(instance, java_LineComment)

@given(instance=java_BlockComment_strategy)
@settings(max_examples=50)
def test_java_blockcomment_instantiation(instance):
    assert isinstance(instance, java_BlockComment)

@given(instance=java_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java_conditionalexpression_instantiation(instance):
    assert isinstance(instance, java_ConditionalExpression)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=java_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java_methoddeclaration_instantiation(instance):
    assert isinstance(instance, java_MethodDeclaration)



@given(instance=java_MethodDeclaration_strategy)
def test_java_methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java_ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_java_constructordeclaration_instantiation(instance):
    assert isinstance(instance, java_ConstructorDeclaration)

@given(instance=AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, AbstractMethodInvocation)

@given(instance=java_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, java_SuperMethodInvocation)

@given(instance=java_MethodInvocation_strategy)
@settings(max_examples=50)
def test_java_methodinvocation_instantiation(instance):
    assert isinstance(instance, java_MethodInvocation)

@given(instance=java_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java_characterliteral_instantiation(instance):
    assert isinstance(instance, java_CharacterLiteral)



@given(instance=java_CharacterLiteral_strategy)
def test_java_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=java_CastExpression_strategy)
@settings(max_examples=50)
def test_java_castexpression_instantiation(instance):
    assert isinstance(instance, java_CastExpression)

@given(instance=java_ArrayCreation_strategy)
@settings(max_examples=50)
def test_java_arraycreation_instantiation(instance):
    assert isinstance(instance, java_ArrayCreation)

@given(instance=java_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java_booleanliteral_instantiation(instance):
    assert isinstance(instance, java_BooleanLiteral)



@given(instance=java_BooleanLiteral_strategy)
def test_java_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java_Modifier_strategy)
@settings(max_examples=50)
def test_java_modifier_instantiation(instance):
    assert isinstance(instance, java_Modifier)



@given(instance=java_Modifier_strategy)
def test_java_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=java_Modifier_strategy)
def test_java_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=java_Assignment_strategy)
@settings(max_examples=50)
def test_java_assignment_instantiation(instance):
    assert isinstance(instance, java_Assignment)



@given(instance=java_Assignment_strategy)
def test_java_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java_ArrayType_strategy)
@settings(max_examples=50)
def test_java_arraytype_instantiation(instance):
    assert isinstance(instance, java_ArrayType)



@given(instance=java_ArrayType_strategy)
def test_java_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=java_ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java_arraylengthaccess_instantiation(instance):
    assert isinstance(instance, java_ArrayLengthAccess)

@given(instance=java_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java_arrayinitializer_instantiation(instance):
    assert isinstance(instance, java_ArrayInitializer)

@given(instance=java_VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, java_VariableDeclarationFragment)

@given(instance=java_ArrayAccess_strategy)
@settings(max_examples=50)
def test_java_arrayaccess_instantiation(instance):
    assert isinstance(instance, java_ArrayAccess)

@given(instance=java_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java_classinstancecreation_instantiation(instance):
    assert isinstance(instance, java_ClassInstanceCreation)

@given(instance=java_AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, java_AnonymousClassDeclaration)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=java_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java_enumdeclaration_instantiation(instance):
    assert isinstance(instance, java_EnumDeclaration)

@given(instance=java_UnresolvedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_unresolvedtypedeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedTypeDeclaration)

@given(instance=java_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_typedeclaration_instantiation(instance):
    assert isinstance(instance, java_TypeDeclaration)

@given(instance=java_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, java_AnnotationTypeDeclaration)

@given(instance=java_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, java_AnnotationTypeMemberDeclaration)

@given(instance=java_ASTNode_strategy)
@settings(max_examples=50)
def test_java_astnode_instantiation(instance):
    assert isinstance(instance, java_ASTNode)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java_expressionstatement_instantiation(instance):
    assert isinstance(instance, java_ExpressionStatement)

@given(instance=java_SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java_superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, java_SuperConstructorInvocation)

@given(instance=java_TryStatement_strategy)
@settings(max_examples=50)
def test_java_trystatement_instantiation(instance):
    assert isinstance(instance, java_TryStatement)

@given(instance=java_BreakStatement_strategy)
@settings(max_examples=50)
def test_java_breakstatement_instantiation(instance):
    assert isinstance(instance, java_BreakStatement)

@given(instance=java_ForStatement_strategy)
@settings(max_examples=50)
def test_java_forstatement_instantiation(instance):
    assert isinstance(instance, java_ForStatement)

@given(instance=java_CatchClause_strategy)
@settings(max_examples=50)
def test_java_catchclause_instantiation(instance):
    assert isinstance(instance, java_CatchClause)

@given(instance=java_ContinueStatement_strategy)
@settings(max_examples=50)
def test_java_continuestatement_instantiation(instance):
    assert isinstance(instance, java_ContinueStatement)

@given(instance=java_WhileStatement_strategy)
@settings(max_examples=50)
def test_java_whilestatement_instantiation(instance):
    assert isinstance(instance, java_WhileStatement)

@given(instance=java_IfStatement_strategy)
@settings(max_examples=50)
def test_java_ifstatement_instantiation(instance):
    assert isinstance(instance, java_IfStatement)

@given(instance=java_ReturnStatement_strategy)
@settings(max_examples=50)
def test_java_returnstatement_instantiation(instance):
    assert isinstance(instance, java_ReturnStatement)

@given(instance=java_SwitchStatement_strategy)
@settings(max_examples=50)
def test_java_switchstatement_instantiation(instance):
    assert isinstance(instance, java_SwitchStatement)

@given(instance=java_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java_constructorinvocation_instantiation(instance):
    assert isinstance(instance, java_ConstructorInvocation)

@given(instance=java_EmptyStatement_strategy)
@settings(max_examples=50)
def test_java_emptystatement_instantiation(instance):
    assert isinstance(instance, java_EmptyStatement)

@given(instance=java_Block_strategy)
@settings(max_examples=50)
def test_java_block_instantiation(instance):
    assert isinstance(instance, java_Block)

@given(instance=java_SwitchCase_strategy)
@settings(max_examples=50)
def test_java_switchcase_instantiation(instance):
    assert isinstance(instance, java_SwitchCase)



@given(instance=java_SwitchCase_strategy)
def test_java_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=java_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, java_SynchronizedStatement)

@given(instance=java_EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java_enhancedforstatement_instantiation(instance):
    assert isinstance(instance, java_EnhancedForStatement)

@given(instance=java_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, java_VariableDeclarationStatement)



@given(instance=java_VariableDeclarationStatement_strategy)
def test_java_variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java_ThrowStatement_strategy)
@settings(max_examples=50)
def test_java_throwstatement_instantiation(instance):
    assert isinstance(instance, java_ThrowStatement)

@given(instance=java_TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java_typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, java_TypeDeclarationStatement)

@given(instance=java_DoStatement_strategy)
@settings(max_examples=50)
def test_java_dostatement_instantiation(instance):
    assert isinstance(instance, java_DoStatement)

@given(instance=java_AssertStatement_strategy)
@settings(max_examples=50)
def test_java_assertstatement_instantiation(instance):
    assert isinstance(instance, java_AssertStatement)

@given(instance=java_Manifest_strategy)
@settings(max_examples=50)
def test_java_manifest_instantiation(instance):
    assert isinstance(instance, java_Manifest)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=java_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_java_instancespecification_instantiation(instance):
    assert isinstance(instance, java_InstanceSpecification)

@given(instance=java_CompilationUnit_strategy)
@settings(max_examples=50)
def test_java_compilationunit_instantiation(instance):
    assert isinstance(instance, java_CompilationUnit)



@given(instance=java_CompilationUnit_strategy)
def test_java_compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java_Package_strategy)
@settings(max_examples=50)
def test_java_package_instantiation(instance):
    assert isinstance(instance, java_Package)

@given(instance=java_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_variabledeclaration_instantiation(instance):
    assert isinstance(instance, java_VariableDeclaration)



@given(instance=java_VariableDeclaration_strategy)
def test_java_variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java_Archive_strategy)
@settings(max_examples=50)
def test_java_archive_instantiation(instance):
    assert isinstance(instance, java_Archive)



@given(instance=java_Archive_strategy)
def test_java_archive_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java_ClassFile_strategy)
@settings(max_examples=50)
def test_java_classfile_instantiation(instance):
    assert isinstance(instance, java_ClassFile)



@given(instance=java_ClassFile_strategy)
def test_java_classfile_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java_bodydeclaration_instantiation(instance):
    assert isinstance(instance, java_BodyDeclaration)

@given(instance=java_LabeledStatement_strategy)
@settings(max_examples=50)
def test_java_labeledstatement_instantiation(instance):
    assert isinstance(instance, java_LabeledStatement)

@given(instance=java_UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java_unresolveditem_instantiation(instance):
    assert isinstance(instance, java_UnresolvedItem)

@given(instance=java_AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java_annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, java_AnnotationMemberValuePair)

@given(instance=java_Type_strategy)
@settings(max_examples=50)
def test_java_type_instantiation(instance):
    assert isinstance(instance, java_Type)
