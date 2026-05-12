import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VariableDeclarationFragment,
    SingleVariableDeclaration,
    MethodDeclaration,
    LabeledStatement,
    InterfaceDeclaration,
    EnumDeclaration,
    ClassDeclaration,
    AnnotationTypeMemberDeclaration,
    UnresolvedItem,
    java__UnresolvedInterfaceDeclaration,
    java__UnresolvedSingleVariableDeclaration,
    java__UnresolvedMethodDeclaration,
    java__UnresolvedLabeledStatement,
    java__UnresolvedClassDeclaration,
    java__UnresolvedVariableDeclarationFragment,
    java__UnresolvedEnumDeclaration,
    java__UnresolvedAnnotationTypeMemberDeclaration,
    AnnotationTypeDeclaration,
    java__UnresolvedAnnotationDeclaration,
    AbstractTypeQualifiedExpression,
    java__ThisExpression,
    java__SuperFieldAccess,
    PrimitiveType,
    java__PrimitiveTypeInt,
    java__PrimitiveTypeShort,
    java__PrimitiveTypeByte,
    java__PrimitiveTypeLong,
    java__PrimitiveTypeFloat,
    java__PrimitiveTypeDouble,
    java__PrimitiveTypeChar,
    java__PrimitiveTypeBoolean,
    java__PrimitiveTypeVoid,
    NamespaceAccess,
    java__PackageAccess,
    java__Model,
    java__ManifestEntry,
    java__ManifestAttribute,
    AbstractVariablesContainer,
    VariableDeclaration,
    TypeDeclaration,
    java__InterfaceDeclaration,
    java__ClassDeclaration,
    AbstractMethodDeclaration,
    java__MethodDeclaration,
    java__ConstructorDeclaration,
    AbstractMethodInvocation,
    java__SuperMethodInvocation,
    Comment,
    java__Javadoc,
    java__LineComment,
    java__BlockComment,
    AbstractTypeDeclaration,
    java__EnumDeclaration,
    java__TypeDeclaration,
    java__UnresolvedTypeDeclaration,
    java__AnnotationTypeDeclaration,
    Expression,
    java__ConditionalExpression,
    java__BooleanLiteral,
    java__InfixExpression,
    java__VariableDeclarationExpression,
    java__TypeLiteral,
    java__ArrayAccess,
    java__FieldAccess,
    java__MethodInvocation,
    java__PrefixExpression,
    java__ArrayInitializer,
    java__StringLiteral,
    java__Assignment,
    java__CharacterLiteral,
    java__InstanceofExpression,
    java__SingleVariableAccess,
    java__CastExpression,
    java__ArrayCreation,
    java__NullLiteral,
    java__ClassInstanceCreation,
    java__PostfixExpression,
    java__NumberLiteral,
    java__ArrayLengthAccess,
    java__ParenthesizedExpression,
    java__UnresolvedItemAccess,
    java__AbstractTypeQualifiedExpression,
    java__ASTNode,
    Statement,
    java__ConstructorInvocation,
    java__ContinueStatement,
    java__CatchClause,
    java__DoStatement,
    java__EmptyStatement,
    java__ExpressionStatement,
    java__TypeDeclarationStatement,
    java__SwitchStatement,
    java__SynchronizedStatement,
    java__SuperConstructorInvocation,
    java__VariableDeclarationStatement,
    java__BreakStatement,
    java__IfStatement,
    java__ReturnStatement,
    java__ThrowStatement,
    java__WhileStatement,
    java__TryStatement,
    java__EnhancedForStatement,
    java__ForStatement,
    java__SwitchCase,
    java__AssertStatement,
    java__Manifest,
    NamedElement,
    java__Type,
    java__CompilationUnit,
    java__VariableDeclaration,
    java__LabeledStatement,
    java__ClassFile,
    java__UnresolvedItem,
    java__Package,
    java__Archive,
    java__AnnotationMemberValuePair,
    java__Annotation,
    java__VariableDeclarationFragment,
    java__SingleVariableDeclaration,
    java__Block,
    BodyDeclaration,
    java__Initializer,
    java__AnnotationTypeMemberDeclaration,
    java__EnumConstantDeclaration,
    java__FieldDeclaration,
    java__AbstractMethodDeclaration,
    java__BodyDeclaration,
    Type,
    java__WildCardType,
    java__PrimitiveType,
    java__ArrayType,
    java__UnresolvedType,
    java__ParameterizedType,
    java__AbstractTypeDeclaration,
    ASTNode,
    java__TextElement,
    java__NamedElement,
    java__Modifier,
    java__Comment,
    java__TagElement,
    java__NamespaceAccess,
    java__AnonymousClassDeclaration,
    java__Statement,
    java__Expression,
    java__MemberRef,
    java__AbstractVariablesContainer,
    java__ImportDeclaration,
    java__MethodRefParameter,
    java__AbstractMethodInvocation,
    java__MethodRef,
    java__TypeParameter,
    java__TypeAccess,
    PostfixExpressionKind,
    InheritanceKind,
    InfixExpressionKind,
    PrefixExpressionKind,
    VisibilityKind,
    AssignmentKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_java__unresolvedinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedInterfaceDeclaration)


def test_java__unresolvedinterfacedeclaration_constructor_exists():
    assert callable(java__UnresolvedInterfaceDeclaration.__init__)


def test_java__unresolvedinterfacedeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedSingleVariableDeclaration)


def test_java__unresolvedsinglevariabledeclaration_constructor_exists():
    assert callable(java__UnresolvedSingleVariableDeclaration.__init__)


def test_java__unresolvedsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedMethodDeclaration)


def test_java__unresolvedmethoddeclaration_constructor_exists():
    assert callable(java__UnresolvedMethodDeclaration.__init__)


def test_java__unresolvedmethoddeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedlabeledstatement_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedLabeledStatement)


def test_java__unresolvedlabeledstatement_constructor_exists():
    assert callable(java__UnresolvedLabeledStatement.__init__)


def test_java__unresolvedlabeledstatement_constructor_args():
    sig = inspect.signature(java__UnresolvedLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedClassDeclaration)


def test_java__unresolvedclassdeclaration_constructor_exists():
    assert callable(java__UnresolvedClassDeclaration.__init__)


def test_java__unresolvedclassdeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedVariableDeclarationFragment)


def test_java__unresolvedvariabledeclarationfragment_constructor_exists():
    assert callable(java__UnresolvedVariableDeclarationFragment.__init__)


def test_java__unresolvedvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(java__UnresolvedVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedenumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedEnumDeclaration)


def test_java__unresolvedenumdeclaration_constructor_exists():
    assert callable(java__UnresolvedEnumDeclaration.__init__)


def test_java__unresolvedenumdeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedEnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedannotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedAnnotationTypeMemberDeclaration)


def test_java__unresolvedannotationtypememberdeclaration_constructor_exists():
    assert callable(java__UnresolvedAnnotationTypeMemberDeclaration.__init__)


def test_java__unresolvedannotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedAnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AnnotationTypeDeclaration)


def test_annotationtypedeclaration_constructor_exists():
    assert callable(AnnotationTypeDeclaration.__init__)


def test_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedannotationdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedAnnotationDeclaration)


def test_java__unresolvedannotationdeclaration_constructor_exists():
    assert callable(java__UnresolvedAnnotationDeclaration.__init__)


def test_java__unresolvedannotationdeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedAnnotationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeQualifiedExpression)


def test_abstracttypequalifiedexpression_constructor_exists():
    assert callable(AbstractTypeQualifiedExpression.__init__)


def test_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__thisexpression_is_not_abstract():
    assert not inspect.isabstract(java__ThisExpression)


def test_java__thisexpression_constructor_exists():
    assert callable(java__ThisExpression.__init__)


def test_java__thisexpression_constructor_args():
    sig = inspect.signature(java__ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(java__SuperFieldAccess)


def test_java__superfieldaccess_constructor_exists():
    assert callable(java__SuperFieldAccess.__init__)


def test_java__superfieldaccess_constructor_args():
    sig = inspect.signature(java__SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeInt)


def test_java__primitivetypeint_constructor_exists():
    assert callable(java__PrimitiveTypeInt.__init__)


def test_java__primitivetypeint_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeShort)


def test_java__primitivetypeshort_constructor_exists():
    assert callable(java__PrimitiveTypeShort.__init__)


def test_java__primitivetypeshort_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeByte)


def test_java__primitivetypebyte_constructor_exists():
    assert callable(java__PrimitiveTypeByte.__init__)


def test_java__primitivetypebyte_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeLong)


def test_java__primitivetypelong_constructor_exists():
    assert callable(java__PrimitiveTypeLong.__init__)


def test_java__primitivetypelong_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeFloat)


def test_java__primitivetypefloat_constructor_exists():
    assert callable(java__PrimitiveTypeFloat.__init__)


def test_java__primitivetypefloat_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeDouble)


def test_java__primitivetypedouble_constructor_exists():
    assert callable(java__PrimitiveTypeDouble.__init__)


def test_java__primitivetypedouble_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeChar)


def test_java__primitivetypechar_constructor_exists():
    assert callable(java__PrimitiveTypeChar.__init__)


def test_java__primitivetypechar_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeBoolean)


def test_java__primitivetypeboolean_constructor_exists():
    assert callable(java__PrimitiveTypeBoolean.__init__)


def test_java__primitivetypeboolean_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_java__primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveTypeVoid)


def test_java__primitivetypevoid_constructor_exists():
    assert callable(java__PrimitiveTypeVoid.__init__)


def test_java__primitivetypevoid_constructor_args():
    sig = inspect.signature(java__PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__packageaccess_is_not_abstract():
    assert not inspect.isabstract(java__PackageAccess)


def test_java__packageaccess_constructor_exists():
    assert callable(java__PackageAccess.__init__)


def test_java__packageaccess_constructor_args():
    sig = inspect.signature(java__PackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__model_is_not_abstract():
    assert not inspect.isabstract(java__Model)


def test_java__model_constructor_exists():
    assert callable(java__Model.__init__)


def test_java__model_constructor_args():
    sig = inspect.signature(java__Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java__model_has_name():
    assert hasattr(java__Model, "name")
    descriptor = None
    for klass in java__Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java__manifestentry_is_not_abstract():
    assert not inspect.isabstract(java__ManifestEntry)


def test_java__manifestentry_constructor_exists():
    assert callable(java__ManifestEntry.__init__)


def test_java__manifestentry_constructor_args():
    sig = inspect.signature(java__ManifestEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java__manifestentry_has_name():
    assert hasattr(java__ManifestEntry, "name")
    descriptor = None
    for klass in java__ManifestEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java__manifestattribute_is_not_abstract():
    assert not inspect.isabstract(java__ManifestAttribute)


def test_java__manifestattribute_constructor_exists():
    assert callable(java__ManifestAttribute.__init__)


def test_java__manifestattribute_constructor_args():
    sig = inspect.signature(java__ManifestAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_java__manifestattribute_has_value():
    assert hasattr(java__ManifestAttribute, "value")
    descriptor = None
    for klass in java__ManifestAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_java__manifestattribute_has_key():
    assert hasattr(java__ManifestAttribute, "key")
    descriptor = None
    for klass in java__ManifestAttribute.__mro__:
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



def test_java__interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java__InterfaceDeclaration)


def test_java__interfacedeclaration_constructor_exists():
    assert callable(java__InterfaceDeclaration.__init__)


def test_java__interfacedeclaration_constructor_args():
    sig = inspect.signature(java__InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__classdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__ClassDeclaration)


def test_java__classdeclaration_constructor_exists():
    assert callable(java__ClassDeclaration.__init__)


def test_java__classdeclaration_constructor_args():
    sig = inspect.signature(java__ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java__MethodDeclaration)


def test_java__methoddeclaration_constructor_exists():
    assert callable(java__MethodDeclaration.__init__)


def test_java__methoddeclaration_constructor_args():
    sig = inspect.signature(java__MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java__methoddeclaration_has_extraArrayDimensions():
    assert hasattr(java__MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in java__MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java__constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(java__ConstructorDeclaration)


def test_java__constructordeclaration_constructor_exists():
    assert callable(java__ConstructorDeclaration.__init__)


def test_java__constructordeclaration_constructor_args():
    sig = inspect.signature(java__ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodInvocation)


def test_abstractmethodinvocation_constructor_exists():
    assert callable(AbstractMethodInvocation.__init__)


def test_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java__supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java__SuperMethodInvocation)


def test_java__supermethodinvocation_constructor_exists():
    assert callable(java__SuperMethodInvocation.__init__)


def test_java__supermethodinvocation_constructor_args():
    sig = inspect.signature(java__SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_java__javadoc_is_not_abstract():
    assert not inspect.isabstract(java__Javadoc)


def test_java__javadoc_constructor_exists():
    assert callable(java__Javadoc.__init__)


def test_java__javadoc_constructor_args():
    sig = inspect.signature(java__Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_java__linecomment_is_not_abstract():
    assert not inspect.isabstract(java__LineComment)


def test_java__linecomment_constructor_exists():
    assert callable(java__LineComment.__init__)


def test_java__linecomment_constructor_args():
    sig = inspect.signature(java__LineComment.__init__)
    params = list(sig.parameters.keys())



def test_java__blockcomment_is_not_abstract():
    assert not inspect.isabstract(java__BlockComment)


def test_java__blockcomment_constructor_exists():
    assert callable(java__BlockComment.__init__)


def test_java__blockcomment_constructor_args():
    sig = inspect.signature(java__BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__EnumDeclaration)


def test_java__enumdeclaration_constructor_exists():
    assert callable(java__EnumDeclaration.__init__)


def test_java__enumdeclaration_constructor_args():
    sig = inspect.signature(java__EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__typedeclaration_is_not_abstract():
    assert not inspect.isabstract(java__TypeDeclaration)


def test_java__typedeclaration_constructor_exists():
    assert callable(java__TypeDeclaration.__init__)


def test_java__typedeclaration_constructor_args():
    sig = inspect.signature(java__TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolvedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedTypeDeclaration)


def test_java__unresolvedtypedeclaration_constructor_exists():
    assert callable(java__UnresolvedTypeDeclaration.__init__)


def test_java__unresolvedtypedeclaration_constructor_args():
    sig = inspect.signature(java__UnresolvedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java__AnnotationTypeDeclaration)


def test_java__annotationtypedeclaration_constructor_exists():
    assert callable(java__AnnotationTypeDeclaration.__init__)


def test_java__annotationtypedeclaration_constructor_args():
    sig = inspect.signature(java__AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java__conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(java__ConditionalExpression)


def test_java__conditionalexpression_constructor_exists():
    assert callable(java__ConditionalExpression.__init__)


def test_java__conditionalexpression_constructor_args():
    sig = inspect.signature(java__ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__booleanliteral_is_not_abstract():
    assert not inspect.isabstract(java__BooleanLiteral)


def test_java__booleanliteral_constructor_exists():
    assert callable(java__BooleanLiteral.__init__)


def test_java__booleanliteral_constructor_args():
    sig = inspect.signature(java__BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java__booleanliteral_has_value():
    assert hasattr(java__BooleanLiteral, "value")
    descriptor = None
    for klass in java__BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java__infixexpression_is_not_abstract():
    assert not inspect.isabstract(java__InfixExpression)


def test_java__infixexpression_constructor_exists():
    assert callable(java__InfixExpression.__init__)


def test_java__infixexpression_constructor_args():
    sig = inspect.signature(java__InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java__infixexpression_has_operator():
    assert hasattr(java__InfixExpression, "operator")
    descriptor = None
    for klass in java__InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java__variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(java__VariableDeclarationExpression)


def test_java__variabledeclarationexpression_constructor_exists():
    assert callable(java__VariableDeclarationExpression.__init__)


def test_java__variabledeclarationexpression_constructor_args():
    sig = inspect.signature(java__VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__typeliteral_is_not_abstract():
    assert not inspect.isabstract(java__TypeLiteral)


def test_java__typeliteral_constructor_exists():
    assert callable(java__TypeLiteral.__init__)


def test_java__typeliteral_constructor_args():
    sig = inspect.signature(java__TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java__arrayaccess_is_not_abstract():
    assert not inspect.isabstract(java__ArrayAccess)


def test_java__arrayaccess_constructor_exists():
    assert callable(java__ArrayAccess.__init__)


def test_java__arrayaccess_constructor_args():
    sig = inspect.signature(java__ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__fieldaccess_is_not_abstract():
    assert not inspect.isabstract(java__FieldAccess)


def test_java__fieldaccess_constructor_exists():
    assert callable(java__FieldAccess.__init__)


def test_java__fieldaccess_constructor_args():
    sig = inspect.signature(java__FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__methodinvocation_is_not_abstract():
    assert not inspect.isabstract(java__MethodInvocation)


def test_java__methodinvocation_constructor_exists():
    assert callable(java__MethodInvocation.__init__)


def test_java__methodinvocation_constructor_args():
    sig = inspect.signature(java__MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java__prefixexpression_is_not_abstract():
    assert not inspect.isabstract(java__PrefixExpression)


def test_java__prefixexpression_constructor_exists():
    assert callable(java__PrefixExpression.__init__)


def test_java__prefixexpression_constructor_args():
    sig = inspect.signature(java__PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java__prefixexpression_has_operator():
    assert hasattr(java__PrefixExpression, "operator")
    descriptor = None
    for klass in java__PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java__arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(java__ArrayInitializer)


def test_java__arrayinitializer_constructor_exists():
    assert callable(java__ArrayInitializer.__init__)


def test_java__arrayinitializer_constructor_args():
    sig = inspect.signature(java__ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java__stringliteral_is_not_abstract():
    assert not inspect.isabstract(java__StringLiteral)


def test_java__stringliteral_constructor_exists():
    assert callable(java__StringLiteral.__init__)


def test_java__stringliteral_constructor_args():
    sig = inspect.signature(java__StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java__stringliteral_has_escapedValue():
    assert hasattr(java__StringLiteral, "escapedValue")
    descriptor = None
    for klass in java__StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java__assignment_is_not_abstract():
    assert not inspect.isabstract(java__Assignment)


def test_java__assignment_constructor_exists():
    assert callable(java__Assignment.__init__)


def test_java__assignment_constructor_args():
    sig = inspect.signature(java__Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java__assignment_has_operator():
    assert hasattr(java__Assignment, "operator")
    descriptor = None
    for klass in java__Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java__characterliteral_is_not_abstract():
    assert not inspect.isabstract(java__CharacterLiteral)


def test_java__characterliteral_constructor_exists():
    assert callable(java__CharacterLiteral.__init__)


def test_java__characterliteral_constructor_args():
    sig = inspect.signature(java__CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java__characterliteral_has_escapedValue():
    assert hasattr(java__CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in java__CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java__instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(java__InstanceofExpression)


def test_java__instanceofexpression_constructor_exists():
    assert callable(java__InstanceofExpression.__init__)


def test_java__instanceofexpression_constructor_args():
    sig = inspect.signature(java__InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__singlevariableaccess_is_not_abstract():
    assert not inspect.isabstract(java__SingleVariableAccess)


def test_java__singlevariableaccess_constructor_exists():
    assert callable(java__SingleVariableAccess.__init__)


def test_java__singlevariableaccess_constructor_args():
    sig = inspect.signature(java__SingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__castexpression_is_not_abstract():
    assert not inspect.isabstract(java__CastExpression)


def test_java__castexpression_constructor_exists():
    assert callable(java__CastExpression.__init__)


def test_java__castexpression_constructor_args():
    sig = inspect.signature(java__CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__arraycreation_is_not_abstract():
    assert not inspect.isabstract(java__ArrayCreation)


def test_java__arraycreation_constructor_exists():
    assert callable(java__ArrayCreation.__init__)


def test_java__arraycreation_constructor_args():
    sig = inspect.signature(java__ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java__nullliteral_is_not_abstract():
    assert not inspect.isabstract(java__NullLiteral)


def test_java__nullliteral_constructor_exists():
    assert callable(java__NullLiteral.__init__)


def test_java__nullliteral_constructor_args():
    sig = inspect.signature(java__NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java__classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(java__ClassInstanceCreation)


def test_java__classinstancecreation_constructor_exists():
    assert callable(java__ClassInstanceCreation.__init__)


def test_java__classinstancecreation_constructor_args():
    sig = inspect.signature(java__ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java__postfixexpression_is_not_abstract():
    assert not inspect.isabstract(java__PostfixExpression)


def test_java__postfixexpression_constructor_exists():
    assert callable(java__PostfixExpression.__init__)


def test_java__postfixexpression_constructor_args():
    sig = inspect.signature(java__PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java__postfixexpression_has_operator():
    assert hasattr(java__PostfixExpression, "operator")
    descriptor = None
    for klass in java__PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java__numberliteral_is_not_abstract():
    assert not inspect.isabstract(java__NumberLiteral)


def test_java__numberliteral_constructor_exists():
    assert callable(java__NumberLiteral.__init__)


def test_java__numberliteral_constructor_args():
    sig = inspect.signature(java__NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java__numberliteral_has_tokenValue():
    assert hasattr(java__NumberLiteral, "tokenValue")
    descriptor = None
    for klass in java__NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java__arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(java__ArrayLengthAccess)


def test_java__arraylengthaccess_constructor_exists():
    assert callable(java__ArrayLengthAccess.__init__)


def test_java__arraylengthaccess_constructor_args():
    sig = inspect.signature(java__ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(java__ParenthesizedExpression)


def test_java__parenthesizedexpression_constructor_exists():
    assert callable(java__ParenthesizedExpression.__init__)


def test_java__parenthesizedexpression_constructor_args():
    sig = inspect.signature(java__ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__unresolveditemaccess_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedItemAccess)


def test_java__unresolveditemaccess_constructor_exists():
    assert callable(java__UnresolvedItemAccess.__init__)


def test_java__unresolveditemaccess_constructor_args():
    sig = inspect.signature(java__UnresolvedItemAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(java__AbstractTypeQualifiedExpression)


def test_java__abstracttypequalifiedexpression_constructor_exists():
    assert callable(java__AbstractTypeQualifiedExpression.__init__)


def test_java__abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(java__AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java__astnode_is_not_abstract():
    assert not inspect.isabstract(java__ASTNode)


def test_java__astnode_constructor_exists():
    assert callable(java__ASTNode.__init__)


def test_java__astnode_constructor_args():
    sig = inspect.signature(java__ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java__constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java__ConstructorInvocation)


def test_java__constructorinvocation_constructor_exists():
    assert callable(java__ConstructorInvocation.__init__)


def test_java__constructorinvocation_constructor_args():
    sig = inspect.signature(java__ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java__continuestatement_is_not_abstract():
    assert not inspect.isabstract(java__ContinueStatement)


def test_java__continuestatement_constructor_exists():
    assert callable(java__ContinueStatement.__init__)


def test_java__continuestatement_constructor_args():
    sig = inspect.signature(java__ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__catchclause_is_not_abstract():
    assert not inspect.isabstract(java__CatchClause)


def test_java__catchclause_constructor_exists():
    assert callable(java__CatchClause.__init__)


def test_java__catchclause_constructor_args():
    sig = inspect.signature(java__CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java__dostatement_is_not_abstract():
    assert not inspect.isabstract(java__DoStatement)


def test_java__dostatement_constructor_exists():
    assert callable(java__DoStatement.__init__)


def test_java__dostatement_constructor_args():
    sig = inspect.signature(java__DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__emptystatement_is_not_abstract():
    assert not inspect.isabstract(java__EmptyStatement)


def test_java__emptystatement_constructor_exists():
    assert callable(java__EmptyStatement.__init__)


def test_java__emptystatement_constructor_args():
    sig = inspect.signature(java__EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__expressionstatement_is_not_abstract():
    assert not inspect.isabstract(java__ExpressionStatement)


def test_java__expressionstatement_constructor_exists():
    assert callable(java__ExpressionStatement.__init__)


def test_java__expressionstatement_constructor_args():
    sig = inspect.signature(java__ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java__TypeDeclarationStatement)


def test_java__typedeclarationstatement_constructor_exists():
    assert callable(java__TypeDeclarationStatement.__init__)


def test_java__typedeclarationstatement_constructor_args():
    sig = inspect.signature(java__TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__switchstatement_is_not_abstract():
    assert not inspect.isabstract(java__SwitchStatement)


def test_java__switchstatement_constructor_exists():
    assert callable(java__SwitchStatement.__init__)


def test_java__switchstatement_constructor_args():
    sig = inspect.signature(java__SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(java__SynchronizedStatement)


def test_java__synchronizedstatement_constructor_exists():
    assert callable(java__SynchronizedStatement.__init__)


def test_java__synchronizedstatement_constructor_args():
    sig = inspect.signature(java__SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java__SuperConstructorInvocation)


def test_java__superconstructorinvocation_constructor_exists():
    assert callable(java__SuperConstructorInvocation.__init__)


def test_java__superconstructorinvocation_constructor_args():
    sig = inspect.signature(java__SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java__variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java__VariableDeclarationStatement)


def test_java__variabledeclarationstatement_constructor_exists():
    assert callable(java__VariableDeclarationStatement.__init__)


def test_java__variabledeclarationstatement_constructor_args():
    sig = inspect.signature(java__VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java__variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(java__VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in java__VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java__breakstatement_is_not_abstract():
    assert not inspect.isabstract(java__BreakStatement)


def test_java__breakstatement_constructor_exists():
    assert callable(java__BreakStatement.__init__)


def test_java__breakstatement_constructor_args():
    sig = inspect.signature(java__BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__ifstatement_is_not_abstract():
    assert not inspect.isabstract(java__IfStatement)


def test_java__ifstatement_constructor_exists():
    assert callable(java__IfStatement.__init__)


def test_java__ifstatement_constructor_args():
    sig = inspect.signature(java__IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__returnstatement_is_not_abstract():
    assert not inspect.isabstract(java__ReturnStatement)


def test_java__returnstatement_constructor_exists():
    assert callable(java__ReturnStatement.__init__)


def test_java__returnstatement_constructor_args():
    sig = inspect.signature(java__ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__throwstatement_is_not_abstract():
    assert not inspect.isabstract(java__ThrowStatement)


def test_java__throwstatement_constructor_exists():
    assert callable(java__ThrowStatement.__init__)


def test_java__throwstatement_constructor_args():
    sig = inspect.signature(java__ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__whilestatement_is_not_abstract():
    assert not inspect.isabstract(java__WhileStatement)


def test_java__whilestatement_constructor_exists():
    assert callable(java__WhileStatement.__init__)


def test_java__whilestatement_constructor_args():
    sig = inspect.signature(java__WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__trystatement_is_not_abstract():
    assert not inspect.isabstract(java__TryStatement)


def test_java__trystatement_constructor_exists():
    assert callable(java__TryStatement.__init__)


def test_java__trystatement_constructor_args():
    sig = inspect.signature(java__TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(java__EnhancedForStatement)


def test_java__enhancedforstatement_constructor_exists():
    assert callable(java__EnhancedForStatement.__init__)


def test_java__enhancedforstatement_constructor_args():
    sig = inspect.signature(java__EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__forstatement_is_not_abstract():
    assert not inspect.isabstract(java__ForStatement)


def test_java__forstatement_constructor_exists():
    assert callable(java__ForStatement.__init__)


def test_java__forstatement_constructor_args():
    sig = inspect.signature(java__ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__switchcase_is_not_abstract():
    assert not inspect.isabstract(java__SwitchCase)


def test_java__switchcase_constructor_exists():
    assert callable(java__SwitchCase.__init__)


def test_java__switchcase_constructor_args():
    sig = inspect.signature(java__SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java__switchcase_has_default():
    assert hasattr(java__SwitchCase, "default")
    descriptor = None
    for klass in java__SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java__assertstatement_is_not_abstract():
    assert not inspect.isabstract(java__AssertStatement)


def test_java__assertstatement_constructor_exists():
    assert callable(java__AssertStatement.__init__)


def test_java__assertstatement_constructor_args():
    sig = inspect.signature(java__AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__manifest_is_not_abstract():
    assert not inspect.isabstract(java__Manifest)


def test_java__manifest_constructor_exists():
    assert callable(java__Manifest.__init__)


def test_java__manifest_constructor_args():
    sig = inspect.signature(java__Manifest.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java__type_is_not_abstract():
    assert not inspect.isabstract(java__Type)


def test_java__type_constructor_exists():
    assert callable(java__Type.__init__)


def test_java__type_constructor_args():
    sig = inspect.signature(java__Type.__init__)
    params = list(sig.parameters.keys())



def test_java__compilationunit_is_not_abstract():
    assert not inspect.isabstract(java__CompilationUnit)


def test_java__compilationunit_constructor_exists():
    assert callable(java__CompilationUnit.__init__)


def test_java__compilationunit_constructor_args():
    sig = inspect.signature(java__CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java__compilationunit_has_originalFilePath():
    assert hasattr(java__CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in java__CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java__variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java__VariableDeclaration)


def test_java__variabledeclaration_constructor_exists():
    assert callable(java__VariableDeclaration.__init__)


def test_java__variabledeclaration_constructor_args():
    sig = inspect.signature(java__VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java__variabledeclaration_has_extraArrayDimensions():
    assert hasattr(java__VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in java__VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java__labeledstatement_is_not_abstract():
    assert not inspect.isabstract(java__LabeledStatement)


def test_java__labeledstatement_constructor_exists():
    assert callable(java__LabeledStatement.__init__)


def test_java__labeledstatement_constructor_args():
    sig = inspect.signature(java__LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java__classfile_is_not_abstract():
    assert not inspect.isabstract(java__ClassFile)


def test_java__classfile_constructor_exists():
    assert callable(java__ClassFile.__init__)


def test_java__classfile_constructor_args():
    sig = inspect.signature(java__ClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java__classfile_has_originalFilePath():
    assert hasattr(java__ClassFile, "originalFilePath")
    descriptor = None
    for klass in java__ClassFile.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java__unresolveditem_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedItem)


def test_java__unresolveditem_constructor_exists():
    assert callable(java__UnresolvedItem.__init__)


def test_java__unresolveditem_constructor_args():
    sig = inspect.signature(java__UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java__package_is_not_abstract():
    assert not inspect.isabstract(java__Package)


def test_java__package_constructor_exists():
    assert callable(java__Package.__init__)


def test_java__package_constructor_args():
    sig = inspect.signature(java__Package.__init__)
    params = list(sig.parameters.keys())



def test_java__archive_is_not_abstract():
    assert not inspect.isabstract(java__Archive)


def test_java__archive_constructor_exists():
    assert callable(java__Archive.__init__)


def test_java__archive_constructor_args():
    sig = inspect.signature(java__Archive.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java__archive_has_originalFilePath():
    assert hasattr(java__Archive, "originalFilePath")
    descriptor = None
    for klass in java__Archive.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java__annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(java__AnnotationMemberValuePair)


def test_java__annotationmembervaluepair_constructor_exists():
    assert callable(java__AnnotationMemberValuePair.__init__)


def test_java__annotationmembervaluepair_constructor_args():
    sig = inspect.signature(java__AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_java__annotation_is_not_abstract():
    assert not inspect.isabstract(java__Annotation)


def test_java__annotation_constructor_exists():
    assert callable(java__Annotation.__init__)


def test_java__annotation_constructor_args():
    sig = inspect.signature(java__Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java__variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java__VariableDeclarationFragment)


def test_java__variabledeclarationfragment_constructor_exists():
    assert callable(java__VariableDeclarationFragment.__init__)


def test_java__variabledeclarationfragment_constructor_args():
    sig = inspect.signature(java__VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java__singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java__SingleVariableDeclaration)


def test_java__singlevariabledeclaration_constructor_exists():
    assert callable(java__SingleVariableDeclaration.__init__)


def test_java__singlevariabledeclaration_constructor_args():
    sig = inspect.signature(java__SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java__singlevariabledeclaration_has_varargs():
    assert hasattr(java__SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in java__SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_java__block_is_not_abstract():
    assert not inspect.isabstract(java__Block)


def test_java__block_constructor_exists():
    assert callable(java__Block.__init__)


def test_java__block_constructor_args():
    sig = inspect.signature(java__Block.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__initializer_is_not_abstract():
    assert not inspect.isabstract(java__Initializer)


def test_java__initializer_constructor_exists():
    assert callable(java__Initializer.__init__)


def test_java__initializer_constructor_args():
    sig = inspect.signature(java__Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java__annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__AnnotationTypeMemberDeclaration)


def test_java__annotationtypememberdeclaration_constructor_exists():
    assert callable(java__AnnotationTypeMemberDeclaration.__init__)


def test_java__annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java__AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__EnumConstantDeclaration)


def test_java__enumconstantdeclaration_constructor_exists():
    assert callable(java__EnumConstantDeclaration.__init__)


def test_java__enumconstantdeclaration_constructor_args():
    sig = inspect.signature(java__EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(java__FieldDeclaration)


def test_java__fielddeclaration_constructor_exists():
    assert callable(java__FieldDeclaration.__init__)


def test_java__fielddeclaration_constructor_args():
    sig = inspect.signature(java__FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java__AbstractMethodDeclaration)


def test_java__abstractmethoddeclaration_constructor_exists():
    assert callable(java__AbstractMethodDeclaration.__init__)


def test_java__abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(java__AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(java__BodyDeclaration)


def test_java__bodydeclaration_constructor_exists():
    assert callable(java__BodyDeclaration.__init__)


def test_java__bodydeclaration_constructor_args():
    sig = inspect.signature(java__BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java__wildcardtype_is_not_abstract():
    assert not inspect.isabstract(java__WildCardType)


def test_java__wildcardtype_constructor_exists():
    assert callable(java__WildCardType.__init__)


def test_java__wildcardtype_constructor_args():
    sig = inspect.signature(java__WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_java__wildcardtype_has_upperBound():
    assert hasattr(java__WildCardType, "upperBound")
    descriptor = None
    for klass in java__WildCardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_java__primitivetype_is_not_abstract():
    assert not inspect.isabstract(java__PrimitiveType)


def test_java__primitivetype_constructor_exists():
    assert callable(java__PrimitiveType.__init__)


def test_java__primitivetype_constructor_args():
    sig = inspect.signature(java__PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java__arraytype_is_not_abstract():
    assert not inspect.isabstract(java__ArrayType)


def test_java__arraytype_constructor_exists():
    assert callable(java__ArrayType.__init__)


def test_java__arraytype_constructor_args():
    sig = inspect.signature(java__ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_java__arraytype_has_dimensions():
    assert hasattr(java__ArrayType, "dimensions")
    descriptor = None
    for klass in java__ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_java__unresolvedtype_is_not_abstract():
    assert not inspect.isabstract(java__UnresolvedType)


def test_java__unresolvedtype_constructor_exists():
    assert callable(java__UnresolvedType.__init__)


def test_java__unresolvedtype_constructor_args():
    sig = inspect.signature(java__UnresolvedType.__init__)
    params = list(sig.parameters.keys())



def test_java__parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(java__ParameterizedType)


def test_java__parameterizedtype_constructor_exists():
    assert callable(java__ParameterizedType.__init__)


def test_java__parameterizedtype_constructor_args():
    sig = inspect.signature(java__ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_java__abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java__AbstractTypeDeclaration)


def test_java__abstracttypedeclaration_constructor_exists():
    assert callable(java__AbstractTypeDeclaration.__init__)


def test_java__abstracttypedeclaration_constructor_args():
    sig = inspect.signature(java__AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java__textelement_is_not_abstract():
    assert not inspect.isabstract(java__TextElement)


def test_java__textelement_constructor_exists():
    assert callable(java__TextElement.__init__)


def test_java__textelement_constructor_args():
    sig = inspect.signature(java__TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java__textelement_has_text():
    assert hasattr(java__TextElement, "text")
    descriptor = None
    for klass in java__TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_java__namedelement_is_not_abstract():
    assert not inspect.isabstract(java__NamedElement)


def test_java__namedelement_constructor_exists():
    assert callable(java__NamedElement.__init__)


def test_java__namedelement_constructor_args():
    sig = inspect.signature(java__NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_java__namedelement_has_name():
    assert hasattr(java__NamedElement, "name")
    descriptor = None
    for klass in java__NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java__namedelement_has_proxy():
    assert hasattr(java__NamedElement, "proxy")
    descriptor = None
    for klass in java__NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_java__modifier_is_not_abstract():
    assert not inspect.isabstract(java__Modifier)


def test_java__modifier_constructor_exists():
    assert callable(java__Modifier.__init__)


def test_java__modifier_constructor_args():
    sig = inspect.signature(java__Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"
    assert "native" in params, "Missing parameter 'native'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_java__modifier_has_transient():
    assert hasattr(java__Modifier, "transient")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_synchronized():
    assert hasattr(java__Modifier, "synchronized")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_strictfp():
    assert hasattr(java__Modifier, "strictfp")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_volatile():
    assert hasattr(java__Modifier, "volatile")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_visibility():
    assert hasattr(java__Modifier, "visibility")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_static():
    assert hasattr(java__Modifier, "static")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_native():
    assert hasattr(java__Modifier, "native")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_java__modifier_has_inheritance():
    assert hasattr(java__Modifier, "inheritance")
    descriptor = None
    for klass in java__Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_java__comment_is_not_abstract():
    assert not inspect.isabstract(java__Comment)


def test_java__comment_constructor_exists():
    assert callable(java__Comment.__init__)


def test_java__comment_constructor_args():
    sig = inspect.signature(java__Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"

def test_java__comment_has_content():
    assert hasattr(java__Comment, "content")
    descriptor = None
    for klass in java__Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_java__comment_has_prefixOfParent():
    assert hasattr(java__Comment, "prefixOfParent")
    descriptor = None
    for klass in java__Comment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)

def test_java__comment_has_enclosedByParent():
    assert hasattr(java__Comment, "enclosedByParent")
    descriptor = None
    for klass in java__Comment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)



def test_java__tagelement_is_not_abstract():
    assert not inspect.isabstract(java__TagElement)


def test_java__tagelement_constructor_exists():
    assert callable(java__TagElement.__init__)


def test_java__tagelement_constructor_args():
    sig = inspect.signature(java__TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java__tagelement_has_tagName():
    assert hasattr(java__TagElement, "tagName")
    descriptor = None
    for klass in java__TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java__namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(java__NamespaceAccess)


def test_java__namespaceaccess_constructor_exists():
    assert callable(java__NamespaceAccess.__init__)


def test_java__namespaceaccess_constructor_args():
    sig = inspect.signature(java__NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_java__anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__AnonymousClassDeclaration)


def test_java__anonymousclassdeclaration_constructor_exists():
    assert callable(java__AnonymousClassDeclaration.__init__)


def test_java__anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(java__AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java__statement_is_not_abstract():
    assert not inspect.isabstract(java__Statement)


def test_java__statement_constructor_exists():
    assert callable(java__Statement.__init__)


def test_java__statement_constructor_args():
    sig = inspect.signature(java__Statement.__init__)
    params = list(sig.parameters.keys())



def test_java__expression_is_not_abstract():
    assert not inspect.isabstract(java__Expression)


def test_java__expression_constructor_exists():
    assert callable(java__Expression.__init__)


def test_java__expression_constructor_args():
    sig = inspect.signature(java__Expression.__init__)
    params = list(sig.parameters.keys())



def test_java__memberref_is_not_abstract():
    assert not inspect.isabstract(java__MemberRef)


def test_java__memberref_constructor_exists():
    assert callable(java__MemberRef.__init__)


def test_java__memberref_constructor_args():
    sig = inspect.signature(java__MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java__abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(java__AbstractVariablesContainer)


def test_java__abstractvariablescontainer_constructor_exists():
    assert callable(java__AbstractVariablesContainer.__init__)


def test_java__abstractvariablescontainer_constructor_args():
    sig = inspect.signature(java__AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_java__importdeclaration_is_not_abstract():
    assert not inspect.isabstract(java__ImportDeclaration)


def test_java__importdeclaration_constructor_exists():
    assert callable(java__ImportDeclaration.__init__)


def test_java__importdeclaration_constructor_args():
    sig = inspect.signature(java__ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java__importdeclaration_has_static():
    assert hasattr(java__ImportDeclaration, "static")
    descriptor = None
    for klass in java__ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java__methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(java__MethodRefParameter)


def test_java__methodrefparameter_constructor_exists():
    assert callable(java__MethodRefParameter.__init__)


def test_java__methodrefparameter_constructor_args():
    sig = inspect.signature(java__MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "name" in params, "Missing parameter 'name'"

def test_java__methodrefparameter_has_varargs():
    assert hasattr(java__MethodRefParameter, "varargs")
    descriptor = None
    for klass in java__MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_java__methodrefparameter_has_name():
    assert hasattr(java__MethodRefParameter, "name")
    descriptor = None
    for klass in java__MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java__abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java__AbstractMethodInvocation)


def test_java__abstractmethodinvocation_constructor_exists():
    assert callable(java__AbstractMethodInvocation.__init__)


def test_java__abstractmethodinvocation_constructor_args():
    sig = inspect.signature(java__AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java__methodref_is_not_abstract():
    assert not inspect.isabstract(java__MethodRef)


def test_java__methodref_constructor_exists():
    assert callable(java__MethodRef.__init__)


def test_java__methodref_constructor_args():
    sig = inspect.signature(java__MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java__typeparameter_is_not_abstract():
    assert not inspect.isabstract(java__TypeParameter)


def test_java__typeparameter_constructor_exists():
    assert callable(java__TypeParameter.__init__)


def test_java__typeparameter_constructor_args():
    sig = inspect.signature(java__TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java__typeaccess_is_not_abstract():
    assert not inspect.isabstract(java__TypeAccess)


def test_java__typeaccess_constructor_exists():
    assert callable(java__TypeAccess.__init__)


def test_java__typeaccess_constructor_args():
    sig = inspect.signature(java__TypeAccess.__init__)
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

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "abstract",
        "none",
        "final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"

def test_infixexpressionkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionKind is not None

def test_infixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionKind]
    expected_literals = [
        "NOT_EQUALS",
        "GREATER",
        "EQUALS",
        "CONDITIONAL_AND",
        "RIGHT_SHIFT_UNSIGNED",
        "LESS",
        "CONDITIONAL_OR",
        "OR",
        "XOR",
        "REMAINDER",
        "TIMES",
        "LEFT_SHIFT",
        "MINUS",
        "PLUS",
        "AND",
        "RIGHT_SHIFT_SIGNED",
        "DIVIDE",
        "GREATER_EQUALS",
        "LESS_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionKind"

def test_prefixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionKind is not None

def test_prefixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionKind]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
        "COMPLEMENT",
        "NOT",
        "PLUS",
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
        "public",
        "none",
        "protected",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "MINUS_ASSIGN",
        "BIT_AND_ASSIGN",
        "DIVIDE_ASSIGN",
        "ASSIGN",
        "TIMES_ASSIGN",
        "PLUS_ASSIGN",
        "REMAINDER_ASSIGN",
        "BIT_XOR_ASSIGN",
        "LEFT_SHIFT_ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "BIT_OR_ASSIGN",
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
java__UnresolvedInterfaceDeclaration_strategy = st.builds(
    java__UnresolvedInterfaceDeclaration,
)
java__UnresolvedSingleVariableDeclaration_strategy = st.builds(
    java__UnresolvedSingleVariableDeclaration,
)
java__UnresolvedMethodDeclaration_strategy = st.builds(
    java__UnresolvedMethodDeclaration,
)
java__UnresolvedLabeledStatement_strategy = st.builds(
    java__UnresolvedLabeledStatement,
)
java__UnresolvedClassDeclaration_strategy = st.builds(
    java__UnresolvedClassDeclaration,
)
java__UnresolvedVariableDeclarationFragment_strategy = st.builds(
    java__UnresolvedVariableDeclarationFragment,
)
java__UnresolvedEnumDeclaration_strategy = st.builds(
    java__UnresolvedEnumDeclaration,
)
java__UnresolvedAnnotationTypeMemberDeclaration_strategy = st.builds(
    java__UnresolvedAnnotationTypeMemberDeclaration,
)
AnnotationTypeDeclaration_strategy = st.builds(
    AnnotationTypeDeclaration,
)
java__UnresolvedAnnotationDeclaration_strategy = st.builds(
    java__UnresolvedAnnotationDeclaration,
)
AbstractTypeQualifiedExpression_strategy = st.builds(
    AbstractTypeQualifiedExpression,
)
java__ThisExpression_strategy = st.builds(
    java__ThisExpression,
)
java__SuperFieldAccess_strategy = st.builds(
    java__SuperFieldAccess,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
java__PrimitiveTypeInt_strategy = st.builds(
    java__PrimitiveTypeInt,
)
java__PrimitiveTypeShort_strategy = st.builds(
    java__PrimitiveTypeShort,
)
java__PrimitiveTypeByte_strategy = st.builds(
    java__PrimitiveTypeByte,
)
java__PrimitiveTypeLong_strategy = st.builds(
    java__PrimitiveTypeLong,
)
java__PrimitiveTypeFloat_strategy = st.builds(
    java__PrimitiveTypeFloat,
)
java__PrimitiveTypeDouble_strategy = st.builds(
    java__PrimitiveTypeDouble,
)
java__PrimitiveTypeChar_strategy = st.builds(
    java__PrimitiveTypeChar,
)
java__PrimitiveTypeBoolean_strategy = st.builds(
    java__PrimitiveTypeBoolean,
)
java__PrimitiveTypeVoid_strategy = st.builds(
    java__PrimitiveTypeVoid,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
java__PackageAccess_strategy = st.builds(
    java__PackageAccess,
)
java__Model_strategy = st.builds(
    java__Model,
    name=
        safe_text
)
java__ManifestEntry_strategy = st.builds(
    java__ManifestEntry,
    name=
        safe_text
)
java__ManifestAttribute_strategy = st.builds(
    java__ManifestAttribute,
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
java__InterfaceDeclaration_strategy = st.builds(
    java__InterfaceDeclaration,
)
java__ClassDeclaration_strategy = st.builds(
    java__ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
java__MethodDeclaration_strategy = st.builds(
    java__MethodDeclaration,
    extraArrayDimensions=
        st.integers()
)
java__ConstructorDeclaration_strategy = st.builds(
    java__ConstructorDeclaration,
)
AbstractMethodInvocation_strategy = st.builds(
    AbstractMethodInvocation,
)
java__SuperMethodInvocation_strategy = st.builds(
    java__SuperMethodInvocation,
)
Comment_strategy = st.builds(
    Comment,
)
java__Javadoc_strategy = st.builds(
    java__Javadoc,
)
java__LineComment_strategy = st.builds(
    java__LineComment,
)
java__BlockComment_strategy = st.builds(
    java__BlockComment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
java__EnumDeclaration_strategy = st.builds(
    java__EnumDeclaration,
)
java__TypeDeclaration_strategy = st.builds(
    java__TypeDeclaration,
)
java__UnresolvedTypeDeclaration_strategy = st.builds(
    java__UnresolvedTypeDeclaration,
)
java__AnnotationTypeDeclaration_strategy = st.builds(
    java__AnnotationTypeDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
java__ConditionalExpression_strategy = st.builds(
    java__ConditionalExpression,
)
java__BooleanLiteral_strategy = st.builds(
    java__BooleanLiteral,
    value=
        st.booleans()
)
java__InfixExpression_strategy = st.builds(
    java__InfixExpression,
    operator=
        safe_text
)
java__VariableDeclarationExpression_strategy = st.builds(
    java__VariableDeclarationExpression,
)
java__TypeLiteral_strategy = st.builds(
    java__TypeLiteral,
)
java__ArrayAccess_strategy = st.builds(
    java__ArrayAccess,
)
java__FieldAccess_strategy = st.builds(
    java__FieldAccess,
)
java__MethodInvocation_strategy = st.builds(
    java__MethodInvocation,
)
java__PrefixExpression_strategy = st.builds(
    java__PrefixExpression,
    operator=
        safe_text
)
java__ArrayInitializer_strategy = st.builds(
    java__ArrayInitializer,
)
java__StringLiteral_strategy = st.builds(
    java__StringLiteral,
    escapedValue=
        safe_text
)
java__Assignment_strategy = st.builds(
    java__Assignment,
    operator=
        safe_text
)
java__CharacterLiteral_strategy = st.builds(
    java__CharacterLiteral,
    escapedValue=
        safe_text
)
java__InstanceofExpression_strategy = st.builds(
    java__InstanceofExpression,
)
java__SingleVariableAccess_strategy = st.builds(
    java__SingleVariableAccess,
)
java__CastExpression_strategy = st.builds(
    java__CastExpression,
)
java__ArrayCreation_strategy = st.builds(
    java__ArrayCreation,
)
java__NullLiteral_strategy = st.builds(
    java__NullLiteral,
)
java__ClassInstanceCreation_strategy = st.builds(
    java__ClassInstanceCreation,
)
java__PostfixExpression_strategy = st.builds(
    java__PostfixExpression,
    operator=
        safe_text
)
java__NumberLiteral_strategy = st.builds(
    java__NumberLiteral,
    tokenValue=
        safe_text
)
java__ArrayLengthAccess_strategy = st.builds(
    java__ArrayLengthAccess,
)
java__ParenthesizedExpression_strategy = st.builds(
    java__ParenthesizedExpression,
)
java__UnresolvedItemAccess_strategy = st.builds(
    java__UnresolvedItemAccess,
)
java__AbstractTypeQualifiedExpression_strategy = st.builds(
    java__AbstractTypeQualifiedExpression,
)
java__ASTNode_strategy = st.builds(
    java__ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
java__ConstructorInvocation_strategy = st.builds(
    java__ConstructorInvocation,
)
java__ContinueStatement_strategy = st.builds(
    java__ContinueStatement,
)
java__CatchClause_strategy = st.builds(
    java__CatchClause,
)
java__DoStatement_strategy = st.builds(
    java__DoStatement,
)
java__EmptyStatement_strategy = st.builds(
    java__EmptyStatement,
)
java__ExpressionStatement_strategy = st.builds(
    java__ExpressionStatement,
)
java__TypeDeclarationStatement_strategy = st.builds(
    java__TypeDeclarationStatement,
)
java__SwitchStatement_strategy = st.builds(
    java__SwitchStatement,
)
java__SynchronizedStatement_strategy = st.builds(
    java__SynchronizedStatement,
)
java__SuperConstructorInvocation_strategy = st.builds(
    java__SuperConstructorInvocation,
)
java__VariableDeclarationStatement_strategy = st.builds(
    java__VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
java__BreakStatement_strategy = st.builds(
    java__BreakStatement,
)
java__IfStatement_strategy = st.builds(
    java__IfStatement,
)
java__ReturnStatement_strategy = st.builds(
    java__ReturnStatement,
)
java__ThrowStatement_strategy = st.builds(
    java__ThrowStatement,
)
java__WhileStatement_strategy = st.builds(
    java__WhileStatement,
)
java__TryStatement_strategy = st.builds(
    java__TryStatement,
)
java__EnhancedForStatement_strategy = st.builds(
    java__EnhancedForStatement,
)
java__ForStatement_strategy = st.builds(
    java__ForStatement,
)
java__SwitchCase_strategy = st.builds(
    java__SwitchCase,
    default=
        st.booleans()
)
java__AssertStatement_strategy = st.builds(
    java__AssertStatement,
)
java__Manifest_strategy = st.builds(
    java__Manifest,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
java__Type_strategy = st.builds(
    java__Type,
)
java__CompilationUnit_strategy = st.builds(
    java__CompilationUnit,
    originalFilePath=
        safe_text
)
java__VariableDeclaration_strategy = st.builds(
    java__VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
java__LabeledStatement_strategy = st.builds(
    java__LabeledStatement,
)
java__ClassFile_strategy = st.builds(
    java__ClassFile,
    originalFilePath=
        safe_text
)
java__UnresolvedItem_strategy = st.builds(
    java__UnresolvedItem,
)
java__Package_strategy = st.builds(
    java__Package,
)
java__Archive_strategy = st.builds(
    java__Archive,
    originalFilePath=
        safe_text
)
java__AnnotationMemberValuePair_strategy = st.builds(
    java__AnnotationMemberValuePair,
)
java__Annotation_strategy = st.builds(
    java__Annotation,
)
java__VariableDeclarationFragment_strategy = st.builds(
    java__VariableDeclarationFragment,
)
java__SingleVariableDeclaration_strategy = st.builds(
    java__SingleVariableDeclaration,
    varargs=
        st.booleans()
)
java__Block_strategy = st.builds(
    java__Block,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
java__Initializer_strategy = st.builds(
    java__Initializer,
)
java__AnnotationTypeMemberDeclaration_strategy = st.builds(
    java__AnnotationTypeMemberDeclaration,
)
java__EnumConstantDeclaration_strategy = st.builds(
    java__EnumConstantDeclaration,
)
java__FieldDeclaration_strategy = st.builds(
    java__FieldDeclaration,
)
java__AbstractMethodDeclaration_strategy = st.builds(
    java__AbstractMethodDeclaration,
)
java__BodyDeclaration_strategy = st.builds(
    java__BodyDeclaration,
)
Type_strategy = st.builds(
    Type,
)
java__WildCardType_strategy = st.builds(
    java__WildCardType,
    upperBound=
        st.booleans()
)
java__PrimitiveType_strategy = st.builds(
    java__PrimitiveType,
)
java__ArrayType_strategy = st.builds(
    java__ArrayType,
    dimensions=
        st.integers()
)
java__UnresolvedType_strategy = st.builds(
    java__UnresolvedType,
)
java__ParameterizedType_strategy = st.builds(
    java__ParameterizedType,
)
java__AbstractTypeDeclaration_strategy = st.builds(
    java__AbstractTypeDeclaration,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
java__TextElement_strategy = st.builds(
    java__TextElement,
    text=
        safe_text
)
java__NamedElement_strategy = st.builds(
    java__NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
java__Modifier_strategy = st.builds(
    java__Modifier,
    transient=
        st.booleans(),
    synchronized=
        st.booleans(),
    strictfp=
        st.booleans(),
    volatile=
        st.booleans(),
    visibility=
        safe_text,
    static=
        st.booleans(),
    native=
        st.booleans(),
    inheritance=
        safe_text
)
java__Comment_strategy = st.builds(
    java__Comment,
    content=
        safe_text,
    prefixOfParent=
        st.booleans(),
    enclosedByParent=
        st.booleans()
)
java__TagElement_strategy = st.builds(
    java__TagElement,
    tagName=
        safe_text
)
java__NamespaceAccess_strategy = st.builds(
    java__NamespaceAccess,
)
java__AnonymousClassDeclaration_strategy = st.builds(
    java__AnonymousClassDeclaration,
)
java__Statement_strategy = st.builds(
    java__Statement,
)
java__Expression_strategy = st.builds(
    java__Expression,
)
java__MemberRef_strategy = st.builds(
    java__MemberRef,
)
java__AbstractVariablesContainer_strategy = st.builds(
    java__AbstractVariablesContainer,
)
java__ImportDeclaration_strategy = st.builds(
    java__ImportDeclaration,
    static=
        st.booleans()
)
java__MethodRefParameter_strategy = st.builds(
    java__MethodRefParameter,
    varargs=
        st.booleans(),
    name=
        safe_text
)
java__AbstractMethodInvocation_strategy = st.builds(
    java__AbstractMethodInvocation,
)
java__MethodRef_strategy = st.builds(
    java__MethodRef,
)
java__TypeParameter_strategy = st.builds(
    java__TypeParameter,
)
java__TypeAccess_strategy = st.builds(
    java__TypeAccess,
)

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

@given(instance=java__UnresolvedInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedInterfaceDeclaration)

@given(instance=java__UnresolvedSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedSingleVariableDeclaration)

@given(instance=java__UnresolvedMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedmethoddeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedMethodDeclaration)

@given(instance=java__UnresolvedLabeledStatement_strategy)
@settings(max_examples=50)
def test_java__unresolvedlabeledstatement_instantiation(instance):
    assert isinstance(instance, java__UnresolvedLabeledStatement)

@given(instance=java__UnresolvedClassDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedclassdeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedClassDeclaration)

@given(instance=java__UnresolvedVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java__unresolvedvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, java__UnresolvedVariableDeclarationFragment)

@given(instance=java__UnresolvedEnumDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedenumdeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedEnumDeclaration)

@given(instance=java__UnresolvedAnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedannotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedAnnotationTypeMemberDeclaration)

@given(instance=AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, AnnotationTypeDeclaration)

@given(instance=java__UnresolvedAnnotationDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedannotationdeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedAnnotationDeclaration)

@given(instance=AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, AbstractTypeQualifiedExpression)

@given(instance=java__ThisExpression_strategy)
@settings(max_examples=50)
def test_java__thisexpression_instantiation(instance):
    assert isinstance(instance, java__ThisExpression)

@given(instance=java__SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java__superfieldaccess_instantiation(instance):
    assert isinstance(instance, java__SuperFieldAccess)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=java__PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java__primitivetypeint_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeInt)

@given(instance=java__PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java__primitivetypeshort_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeShort)

@given(instance=java__PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java__primitivetypebyte_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeByte)

@given(instance=java__PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java__primitivetypelong_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeLong)

@given(instance=java__PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java__primitivetypefloat_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeFloat)

@given(instance=java__PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java__primitivetypedouble_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeDouble)

@given(instance=java__PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java__primitivetypechar_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeChar)

@given(instance=java__PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java__primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeBoolean)

@given(instance=java__PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java__primitivetypevoid_instantiation(instance):
    assert isinstance(instance, java__PrimitiveTypeVoid)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=java__PackageAccess_strategy)
@settings(max_examples=50)
def test_java__packageaccess_instantiation(instance):
    assert isinstance(instance, java__PackageAccess)

@given(instance=java__Model_strategy)
@settings(max_examples=50)
def test_java__model_instantiation(instance):
    assert isinstance(instance, java__Model)



@given(instance=java__Model_strategy)
def test_java__model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java__ManifestEntry_strategy)
@settings(max_examples=50)
def test_java__manifestentry_instantiation(instance):
    assert isinstance(instance, java__ManifestEntry)



@given(instance=java__ManifestEntry_strategy)
def test_java__manifestentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java__ManifestAttribute_strategy)
@settings(max_examples=50)
def test_java__manifestattribute_instantiation(instance):
    assert isinstance(instance, java__ManifestAttribute)



@given(instance=java__ManifestAttribute_strategy)
def test_java__manifestattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=java__ManifestAttribute_strategy)
def test_java__manifestattribute_key_setter(instance):
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

@given(instance=java__InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java__interfacedeclaration_instantiation(instance):
    assert isinstance(instance, java__InterfaceDeclaration)

@given(instance=java__ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java__classdeclaration_instantiation(instance):
    assert isinstance(instance, java__ClassDeclaration)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=java__MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java__methoddeclaration_instantiation(instance):
    assert isinstance(instance, java__MethodDeclaration)



@given(instance=java__MethodDeclaration_strategy)
def test_java__methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java__ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_java__constructordeclaration_instantiation(instance):
    assert isinstance(instance, java__ConstructorDeclaration)

@given(instance=AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, AbstractMethodInvocation)

@given(instance=java__SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java__supermethodinvocation_instantiation(instance):
    assert isinstance(instance, java__SuperMethodInvocation)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=java__Javadoc_strategy)
@settings(max_examples=50)
def test_java__javadoc_instantiation(instance):
    assert isinstance(instance, java__Javadoc)

@given(instance=java__LineComment_strategy)
@settings(max_examples=50)
def test_java__linecomment_instantiation(instance):
    assert isinstance(instance, java__LineComment)

@given(instance=java__BlockComment_strategy)
@settings(max_examples=50)
def test_java__blockcomment_instantiation(instance):
    assert isinstance(instance, java__BlockComment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=java__EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java__enumdeclaration_instantiation(instance):
    assert isinstance(instance, java__EnumDeclaration)

@given(instance=java__TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java__typedeclaration_instantiation(instance):
    assert isinstance(instance, java__TypeDeclaration)

@given(instance=java__UnresolvedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java__unresolvedtypedeclaration_instantiation(instance):
    assert isinstance(instance, java__UnresolvedTypeDeclaration)

@given(instance=java__AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java__annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, java__AnnotationTypeDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=java__ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java__conditionalexpression_instantiation(instance):
    assert isinstance(instance, java__ConditionalExpression)

@given(instance=java__BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java__booleanliteral_instantiation(instance):
    assert isinstance(instance, java__BooleanLiteral)



@given(instance=java__BooleanLiteral_strategy)
def test_java__booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=java__InfixExpression_strategy)
@settings(max_examples=50)
def test_java__infixexpression_instantiation(instance):
    assert isinstance(instance, java__InfixExpression)



@given(instance=java__InfixExpression_strategy)
def test_java__infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java__VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java__variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, java__VariableDeclarationExpression)

@given(instance=java__TypeLiteral_strategy)
@settings(max_examples=50)
def test_java__typeliteral_instantiation(instance):
    assert isinstance(instance, java__TypeLiteral)

@given(instance=java__ArrayAccess_strategy)
@settings(max_examples=50)
def test_java__arrayaccess_instantiation(instance):
    assert isinstance(instance, java__ArrayAccess)

@given(instance=java__FieldAccess_strategy)
@settings(max_examples=50)
def test_java__fieldaccess_instantiation(instance):
    assert isinstance(instance, java__FieldAccess)

@given(instance=java__MethodInvocation_strategy)
@settings(max_examples=50)
def test_java__methodinvocation_instantiation(instance):
    assert isinstance(instance, java__MethodInvocation)

@given(instance=java__PrefixExpression_strategy)
@settings(max_examples=50)
def test_java__prefixexpression_instantiation(instance):
    assert isinstance(instance, java__PrefixExpression)



@given(instance=java__PrefixExpression_strategy)
def test_java__prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java__ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java__arrayinitializer_instantiation(instance):
    assert isinstance(instance, java__ArrayInitializer)

@given(instance=java__StringLiteral_strategy)
@settings(max_examples=50)
def test_java__stringliteral_instantiation(instance):
    assert isinstance(instance, java__StringLiteral)



@given(instance=java__StringLiteral_strategy)
def test_java__stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=java__Assignment_strategy)
@settings(max_examples=50)
def test_java__assignment_instantiation(instance):
    assert isinstance(instance, java__Assignment)



@given(instance=java__Assignment_strategy)
def test_java__assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java__CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java__characterliteral_instantiation(instance):
    assert isinstance(instance, java__CharacterLiteral)



@given(instance=java__CharacterLiteral_strategy)
def test_java__characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=java__InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java__instanceofexpression_instantiation(instance):
    assert isinstance(instance, java__InstanceofExpression)

@given(instance=java__SingleVariableAccess_strategy)
@settings(max_examples=50)
def test_java__singlevariableaccess_instantiation(instance):
    assert isinstance(instance, java__SingleVariableAccess)

@given(instance=java__CastExpression_strategy)
@settings(max_examples=50)
def test_java__castexpression_instantiation(instance):
    assert isinstance(instance, java__CastExpression)

@given(instance=java__ArrayCreation_strategy)
@settings(max_examples=50)
def test_java__arraycreation_instantiation(instance):
    assert isinstance(instance, java__ArrayCreation)

@given(instance=java__NullLiteral_strategy)
@settings(max_examples=50)
def test_java__nullliteral_instantiation(instance):
    assert isinstance(instance, java__NullLiteral)

@given(instance=java__ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java__classinstancecreation_instantiation(instance):
    assert isinstance(instance, java__ClassInstanceCreation)

@given(instance=java__PostfixExpression_strategy)
@settings(max_examples=50)
def test_java__postfixexpression_instantiation(instance):
    assert isinstance(instance, java__PostfixExpression)



@given(instance=java__PostfixExpression_strategy)
def test_java__postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=java__NumberLiteral_strategy)
@settings(max_examples=50)
def test_java__numberliteral_instantiation(instance):
    assert isinstance(instance, java__NumberLiteral)



@given(instance=java__NumberLiteral_strategy)
def test_java__numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=java__ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java__arraylengthaccess_instantiation(instance):
    assert isinstance(instance, java__ArrayLengthAccess)

@given(instance=java__ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java__parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, java__ParenthesizedExpression)

@given(instance=java__UnresolvedItemAccess_strategy)
@settings(max_examples=50)
def test_java__unresolveditemaccess_instantiation(instance):
    assert isinstance(instance, java__UnresolvedItemAccess)

@given(instance=java__AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=50)
def test_java__abstracttypequalifiedexpression_instantiation(instance):
    assert isinstance(instance, java__AbstractTypeQualifiedExpression)

@given(instance=java__ASTNode_strategy)
@settings(max_examples=50)
def test_java__astnode_instantiation(instance):
    assert isinstance(instance, java__ASTNode)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java__ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java__constructorinvocation_instantiation(instance):
    assert isinstance(instance, java__ConstructorInvocation)

@given(instance=java__ContinueStatement_strategy)
@settings(max_examples=50)
def test_java__continuestatement_instantiation(instance):
    assert isinstance(instance, java__ContinueStatement)

@given(instance=java__CatchClause_strategy)
@settings(max_examples=50)
def test_java__catchclause_instantiation(instance):
    assert isinstance(instance, java__CatchClause)

@given(instance=java__DoStatement_strategy)
@settings(max_examples=50)
def test_java__dostatement_instantiation(instance):
    assert isinstance(instance, java__DoStatement)

@given(instance=java__EmptyStatement_strategy)
@settings(max_examples=50)
def test_java__emptystatement_instantiation(instance):
    assert isinstance(instance, java__EmptyStatement)

@given(instance=java__ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java__expressionstatement_instantiation(instance):
    assert isinstance(instance, java__ExpressionStatement)

@given(instance=java__TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java__typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, java__TypeDeclarationStatement)

@given(instance=java__SwitchStatement_strategy)
@settings(max_examples=50)
def test_java__switchstatement_instantiation(instance):
    assert isinstance(instance, java__SwitchStatement)

@given(instance=java__SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java__synchronizedstatement_instantiation(instance):
    assert isinstance(instance, java__SynchronizedStatement)

@given(instance=java__SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java__superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, java__SuperConstructorInvocation)

@given(instance=java__VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java__variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, java__VariableDeclarationStatement)



@given(instance=java__VariableDeclarationStatement_strategy)
def test_java__variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java__BreakStatement_strategy)
@settings(max_examples=50)
def test_java__breakstatement_instantiation(instance):
    assert isinstance(instance, java__BreakStatement)

@given(instance=java__IfStatement_strategy)
@settings(max_examples=50)
def test_java__ifstatement_instantiation(instance):
    assert isinstance(instance, java__IfStatement)

@given(instance=java__ReturnStatement_strategy)
@settings(max_examples=50)
def test_java__returnstatement_instantiation(instance):
    assert isinstance(instance, java__ReturnStatement)

@given(instance=java__ThrowStatement_strategy)
@settings(max_examples=50)
def test_java__throwstatement_instantiation(instance):
    assert isinstance(instance, java__ThrowStatement)

@given(instance=java__WhileStatement_strategy)
@settings(max_examples=50)
def test_java__whilestatement_instantiation(instance):
    assert isinstance(instance, java__WhileStatement)

@given(instance=java__TryStatement_strategy)
@settings(max_examples=50)
def test_java__trystatement_instantiation(instance):
    assert isinstance(instance, java__TryStatement)

@given(instance=java__EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java__enhancedforstatement_instantiation(instance):
    assert isinstance(instance, java__EnhancedForStatement)

@given(instance=java__ForStatement_strategy)
@settings(max_examples=50)
def test_java__forstatement_instantiation(instance):
    assert isinstance(instance, java__ForStatement)

@given(instance=java__SwitchCase_strategy)
@settings(max_examples=50)
def test_java__switchcase_instantiation(instance):
    assert isinstance(instance, java__SwitchCase)



@given(instance=java__SwitchCase_strategy)
def test_java__switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=java__AssertStatement_strategy)
@settings(max_examples=50)
def test_java__assertstatement_instantiation(instance):
    assert isinstance(instance, java__AssertStatement)

@given(instance=java__Manifest_strategy)
@settings(max_examples=50)
def test_java__manifest_instantiation(instance):
    assert isinstance(instance, java__Manifest)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=java__Type_strategy)
@settings(max_examples=50)
def test_java__type_instantiation(instance):
    assert isinstance(instance, java__Type)

@given(instance=java__CompilationUnit_strategy)
@settings(max_examples=50)
def test_java__compilationunit_instantiation(instance):
    assert isinstance(instance, java__CompilationUnit)



@given(instance=java__CompilationUnit_strategy)
def test_java__compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java__VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java__variabledeclaration_instantiation(instance):
    assert isinstance(instance, java__VariableDeclaration)



@given(instance=java__VariableDeclaration_strategy)
def test_java__variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=java__LabeledStatement_strategy)
@settings(max_examples=50)
def test_java__labeledstatement_instantiation(instance):
    assert isinstance(instance, java__LabeledStatement)

@given(instance=java__ClassFile_strategy)
@settings(max_examples=50)
def test_java__classfile_instantiation(instance):
    assert isinstance(instance, java__ClassFile)



@given(instance=java__ClassFile_strategy)
def test_java__classfile_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java__UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java__unresolveditem_instantiation(instance):
    assert isinstance(instance, java__UnresolvedItem)

@given(instance=java__Package_strategy)
@settings(max_examples=50)
def test_java__package_instantiation(instance):
    assert isinstance(instance, java__Package)

@given(instance=java__Archive_strategy)
@settings(max_examples=50)
def test_java__archive_instantiation(instance):
    assert isinstance(instance, java__Archive)



@given(instance=java__Archive_strategy)
def test_java__archive_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=java__AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java__annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, java__AnnotationMemberValuePair)

@given(instance=java__Annotation_strategy)
@settings(max_examples=50)
def test_java__annotation_instantiation(instance):
    assert isinstance(instance, java__Annotation)

@given(instance=java__VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java__variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, java__VariableDeclarationFragment)

@given(instance=java__SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java__singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, java__SingleVariableDeclaration)



@given(instance=java__SingleVariableDeclaration_strategy)
def test_java__singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=java__Block_strategy)
@settings(max_examples=50)
def test_java__block_instantiation(instance):
    assert isinstance(instance, java__Block)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=java__Initializer_strategy)
@settings(max_examples=50)
def test_java__initializer_instantiation(instance):
    assert isinstance(instance, java__Initializer)

@given(instance=java__AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java__annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, java__AnnotationTypeMemberDeclaration)

@given(instance=java__EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java__enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, java__EnumConstantDeclaration)

@given(instance=java__FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java__fielddeclaration_instantiation(instance):
    assert isinstance(instance, java__FieldDeclaration)

@given(instance=java__AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_java__abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, java__AbstractMethodDeclaration)

@given(instance=java__BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java__bodydeclaration_instantiation(instance):
    assert isinstance(instance, java__BodyDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=java__WildCardType_strategy)
@settings(max_examples=50)
def test_java__wildcardtype_instantiation(instance):
    assert isinstance(instance, java__WildCardType)



@given(instance=java__WildCardType_strategy)
def test_java__wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=java__PrimitiveType_strategy)
@settings(max_examples=50)
def test_java__primitivetype_instantiation(instance):
    assert isinstance(instance, java__PrimitiveType)

@given(instance=java__ArrayType_strategy)
@settings(max_examples=50)
def test_java__arraytype_instantiation(instance):
    assert isinstance(instance, java__ArrayType)



@given(instance=java__ArrayType_strategy)
def test_java__arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=java__UnresolvedType_strategy)
@settings(max_examples=50)
def test_java__unresolvedtype_instantiation(instance):
    assert isinstance(instance, java__UnresolvedType)

@given(instance=java__ParameterizedType_strategy)
@settings(max_examples=50)
def test_java__parameterizedtype_instantiation(instance):
    assert isinstance(instance, java__ParameterizedType)

@given(instance=java__AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java__abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, java__AbstractTypeDeclaration)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=java__TextElement_strategy)
@settings(max_examples=50)
def test_java__textelement_instantiation(instance):
    assert isinstance(instance, java__TextElement)



@given(instance=java__TextElement_strategy)
def test_java__textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=java__NamedElement_strategy)
@settings(max_examples=50)
def test_java__namedelement_instantiation(instance):
    assert isinstance(instance, java__NamedElement)



@given(instance=java__NamedElement_strategy)
def test_java__namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java__NamedElement_strategy)
def test_java__namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=java__Modifier_strategy)
@settings(max_examples=50)
def test_java__modifier_instantiation(instance):
    assert isinstance(instance, java__Modifier)



@given(instance=java__Modifier_strategy)
def test_java__modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=java__Modifier_strategy)
def test_java__modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=java__Comment_strategy)
@settings(max_examples=50)
def test_java__comment_instantiation(instance):
    assert isinstance(instance, java__Comment)



@given(instance=java__Comment_strategy)
def test_java__comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=java__Comment_strategy)
def test_java__comment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original



@given(instance=java__Comment_strategy)
def test_java__comment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original

@given(instance=java__TagElement_strategy)
@settings(max_examples=50)
def test_java__tagelement_instantiation(instance):
    assert isinstance(instance, java__TagElement)



@given(instance=java__TagElement_strategy)
def test_java__tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=java__NamespaceAccess_strategy)
@settings(max_examples=50)
def test_java__namespaceaccess_instantiation(instance):
    assert isinstance(instance, java__NamespaceAccess)

@given(instance=java__AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java__anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, java__AnonymousClassDeclaration)

@given(instance=java__Statement_strategy)
@settings(max_examples=50)
def test_java__statement_instantiation(instance):
    assert isinstance(instance, java__Statement)

@given(instance=java__Expression_strategy)
@settings(max_examples=50)
def test_java__expression_instantiation(instance):
    assert isinstance(instance, java__Expression)

@given(instance=java__MemberRef_strategy)
@settings(max_examples=50)
def test_java__memberref_instantiation(instance):
    assert isinstance(instance, java__MemberRef)

@given(instance=java__AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_java__abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, java__AbstractVariablesContainer)

@given(instance=java__ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java__importdeclaration_instantiation(instance):
    assert isinstance(instance, java__ImportDeclaration)



@given(instance=java__ImportDeclaration_strategy)
def test_java__importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=java__MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java__methodrefparameter_instantiation(instance):
    assert isinstance(instance, java__MethodRefParameter)



@given(instance=java__MethodRefParameter_strategy)
def test_java__methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original



@given(instance=java__MethodRefParameter_strategy)
def test_java__methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java__AbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_java__abstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, java__AbstractMethodInvocation)

@given(instance=java__MethodRef_strategy)
@settings(max_examples=50)
def test_java__methodref_instantiation(instance):
    assert isinstance(instance, java__MethodRef)

@given(instance=java__TypeParameter_strategy)
@settings(max_examples=50)
def test_java__typeparameter_instantiation(instance):
    assert isinstance(instance, java__TypeParameter)

@given(instance=java__TypeAccess_strategy)
@settings(max_examples=50)
def test_java__typeaccess_instantiation(instance):
    assert isinstance(instance, java__TypeAccess)
