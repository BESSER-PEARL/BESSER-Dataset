import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Name,
    JDTAST_QualifiedName,
    VariableDeclaration,
    Annotation,
    JDTAST_SingleMemberAnnotation,
    JDTAST_NormalAnnotation,
    JDTAST_MarkerAnnotation,
    Type,
    JDTAST_ParameterizedType,
    JDTAST_WildcardType,
    JDTAST_SimpleType,
    JDTAST_QualifiedType,
    JDTAST_PrimitiveType,
    Statement,
    JDTAST_ThrowStatement,
    JDTAST_TryStatement,
    JDTAST_ExpressionStatement,
    JDTAST_LabeledStatement,
    JDTAST_SynchronizedStatement,
    JDTAST_ReturnStatement,
    JDTAST_EnhancedForStatement,
    JDTAST_SwitchCase,
    JDTAST_SwitchStatement,
    JDTAST_TypeDeclarationStatement,
    JDTAST_VariableDeclarationStatement,
    JDTAST_ForStatement,
    JDTAST_IfStatement,
    JDTAST_SuperConstructorInvocation,
    JDTAST_WhileStatement,
    JDTAST_EmptyStatement,
    JDTAST_ConstructorInvocation,
    JDTAST_DoStatement,
    JDTAST_ContinueStatement,
    JDTAST_BreakStatement,
    JDTAST_AssertStatement,
    Expression,
    JDTAST_SuperMethodInvocation,
    JDTAST_NullLiteral,
    JDTAST_VariableDeclarationExpression,
    JDTAST_TypeLiteral,
    JDTAST_BooleanLiteral,
    JDTAST_SuperFieldAccess,
    JDTAST_InstanceofExpression,
    JDTAST_PostfixExpression,
    JDTAST_FieldAccess,
    JDTAST_ThisExpression,
    JDTAST_CastExpression,
    JDTAST_InfixExpression,
    JDTAST_Assignment,
    JDTAST_StringLiteral,
    JDTAST_MethodInvocation,
    JDTAST_ArrayAccess,
    JDTAST_ParenthesizedExpression,
    JDTAST_PrefixExpression,
    JDTAST_ClassInstanceCreation,
    JDTAST_ConditionalExpression,
    JDTAST_NumberLiteral,
    JDTAST_CharacterLiteral,
    Comment,
    JDTAST_LineComment,
    JDTAST_BlockComment,
    AbstractTypeDeclaration,
    JDTAST_EnumDeclaration,
    JDTAST_TypeDeclaration,
    JDTAST_AnnotationTypeDeclaration,
    JDTAST_ArrayType,
    JDTAST_ArrayInitializer,
    JDTAST_ArrayCreation,
    JDTAST_VariableDeclarationFragment,
    BodyDeclaration,
    JDTAST_FieldDeclaration,
    JDTAST_Initializer,
    JDTAST_MethodDeclaration,
    JDTAST_AnnotationTypeMemberDeclaration,
    JDTAST_EnumConstantDeclaration,
    JDTAST_SimpleName,
    ExtendedModifier,
    JDTAST_Annotation,
    JDTAST_Name,
    JDTAST_AbstractTypeDeclaration,
    JDTAST_SingleVariableDeclaration,
    JDTAST_Block,
    JDTAST_ASTNode,
    JDTAST_AST,
    JDTAST_Parameter,
    JDTAST_Javadoc,
    JDTAST_ExtendedModifier,
    ASTNode,
    JDTAST_BodyDeclaration,
    JDTAST_CatchClause,
    JDTAST_Modifier,
    JDTAST_TextElement,
    JDTAST_Comment,
    JDTAST_MethodRefParameter,
    JDTAST_TypeParameter,
    JDTAST_Expression,
    JDTAST_ImportDeclaration,
    JDTAST_MemberRef,
    JDTAST_Type,
    JDTAST_MethodRef,
    JDTAST_VariableDeclaration,
    JDTAST_Statement,
    JDTAST_MemberValuePair,
    JDTAST_TagElement,
    JDTAST_PackageDeclaration,
    JDTAST_AnonymousClassDeclaration,
    IMember,
    JDTAST_IMethod,
    JDTAST_IInitializer,
    JDTAST_IField,
    JDTAST_ISourceRange,
    JDTAST_ISourceReference,
    JDTAST_CompilationUnit,
    IPackageFragmentRoot,
    JDTAST_SourcePackageFragmentRoot,
    JDTAST_BinaryPackageFragmentRoot,
    IJavaElement,
    PhysicalElement,
    JDTAST_IJavaProject,
    JDTAST_IPackageFragment,
    JDTAST_IPackageFragmentRoot,
    JDTAST_IJavaModel,
    JDTAST_PhysicalElement,
    JDTAST_IJavaElement,
    JDTAST_IType,
    ITypeRoot,
    ISourceReference,
    JDTAST_IImportDeclaration,
    JDTAST_IMember,
    JDTAST_ITypeParameter,
    JDTAST_ITypeRoot,
    JDTAST_ICompilationUnit,
    JDTAST_IClassFile,
    Modifiers,
    InfixExpressionOperatorKind,
    AssignmentOperatorKind,
    PostfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
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



def test_jdtast_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(JDTAST_QualifiedName)


def test_jdtast_qualifiedname_constructor_exists():
    assert callable(JDTAST_QualifiedName.__init__)


def test_jdtast_qualifiedname_constructor_args():
    sig = inspect.signature(JDTAST_QualifiedName.__init__)
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



def test_jdtast_singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SingleMemberAnnotation)


def test_jdtast_singlememberannotation_constructor_exists():
    assert callable(JDTAST_SingleMemberAnnotation.__init__)


def test_jdtast_singlememberannotation_constructor_args():
    sig = inspect.signature(JDTAST_SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_normalannotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_NormalAnnotation)


def test_jdtast_normalannotation_constructor_exists():
    assert callable(JDTAST_NormalAnnotation.__init__)


def test_jdtast_normalannotation_constructor_args():
    sig = inspect.signature(JDTAST_NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_markerannotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MarkerAnnotation)


def test_jdtast_markerannotation_constructor_exists():
    assert callable(JDTAST_MarkerAnnotation.__init__)


def test_jdtast_markerannotation_constructor_args():
    sig = inspect.signature(JDTAST_MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ParameterizedType)


def test_jdtast_parameterizedtype_constructor_exists():
    assert callable(JDTAST_ParameterizedType.__init__)


def test_jdtast_parameterizedtype_constructor_args():
    sig = inspect.signature(JDTAST_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_WildcardType)


def test_jdtast_wildcardtype_constructor_exists():
    assert callable(JDTAST_WildcardType.__init__)


def test_jdtast_wildcardtype_constructor_args():
    sig = inspect.signature(JDTAST_WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_jdtast_wildcardtype_has_upperBound():
    assert hasattr(JDTAST_WildcardType, "upperBound")
    descriptor = None
    for klass in JDTAST_WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_simpletype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SimpleType)


def test_jdtast_simpletype_constructor_exists():
    assert callable(JDTAST_SimpleType.__init__)


def test_jdtast_simpletype_constructor_args():
    sig = inspect.signature(JDTAST_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_QualifiedType)


def test_jdtast_qualifiedtype_constructor_exists():
    assert callable(JDTAST_QualifiedType.__init__)


def test_jdtast_qualifiedtype_constructor_args():
    sig = inspect.signature(JDTAST_QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_primitivetype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_PrimitiveType)


def test_jdtast_primitivetype_constructor_exists():
    assert callable(JDTAST_PrimitiveType.__init__)


def test_jdtast_primitivetype_constructor_args():
    sig = inspect.signature(JDTAST_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_jdtast_primitivetype_has_code():
    assert hasattr(JDTAST_PrimitiveType, "code")
    descriptor = None
    for klass in JDTAST_PrimitiveType.__mro__:
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



def test_jdtast_throwstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ThrowStatement)


def test_jdtast_throwstatement_constructor_exists():
    assert callable(JDTAST_ThrowStatement.__init__)


def test_jdtast_throwstatement_constructor_args():
    sig = inspect.signature(JDTAST_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_trystatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TryStatement)


def test_jdtast_trystatement_constructor_exists():
    assert callable(JDTAST_TryStatement.__init__)


def test_jdtast_trystatement_constructor_args():
    sig = inspect.signature(JDTAST_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ExpressionStatement)


def test_jdtast_expressionstatement_constructor_exists():
    assert callable(JDTAST_ExpressionStatement.__init__)


def test_jdtast_expressionstatement_constructor_args():
    sig = inspect.signature(JDTAST_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_LabeledStatement)


def test_jdtast_labeledstatement_constructor_exists():
    assert callable(JDTAST_LabeledStatement.__init__)


def test_jdtast_labeledstatement_constructor_args():
    sig = inspect.signature(JDTAST_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SynchronizedStatement)


def test_jdtast_synchronizedstatement_constructor_exists():
    assert callable(JDTAST_SynchronizedStatement.__init__)


def test_jdtast_synchronizedstatement_constructor_args():
    sig = inspect.signature(JDTAST_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_returnstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ReturnStatement)


def test_jdtast_returnstatement_constructor_exists():
    assert callable(JDTAST_ReturnStatement.__init__)


def test_jdtast_returnstatement_constructor_args():
    sig = inspect.signature(JDTAST_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_EnhancedForStatement)


def test_jdtast_enhancedforstatement_constructor_exists():
    assert callable(JDTAST_EnhancedForStatement.__init__)


def test_jdtast_enhancedforstatement_constructor_args():
    sig = inspect.signature(JDTAST_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_switchcase_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SwitchCase)


def test_jdtast_switchcase_constructor_exists():
    assert callable(JDTAST_SwitchCase.__init__)


def test_jdtast_switchcase_constructor_args():
    sig = inspect.signature(JDTAST_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_jdtast_switchcase_has_default():
    assert hasattr(JDTAST_SwitchCase, "default")
    descriptor = None
    for klass in JDTAST_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_switchstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SwitchStatement)


def test_jdtast_switchstatement_constructor_exists():
    assert callable(JDTAST_SwitchStatement.__init__)


def test_jdtast_switchstatement_constructor_args():
    sig = inspect.signature(JDTAST_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TypeDeclarationStatement)


def test_jdtast_typedeclarationstatement_constructor_exists():
    assert callable(JDTAST_TypeDeclarationStatement.__init__)


def test_jdtast_typedeclarationstatement_constructor_args():
    sig = inspect.signature(JDTAST_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_VariableDeclarationStatement)


def test_jdtast_variabledeclarationstatement_constructor_exists():
    assert callable(JDTAST_VariableDeclarationStatement.__init__)


def test_jdtast_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(JDTAST_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_forstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ForStatement)


def test_jdtast_forstatement_constructor_exists():
    assert callable(JDTAST_ForStatement.__init__)


def test_jdtast_forstatement_constructor_args():
    sig = inspect.signature(JDTAST_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_ifstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IfStatement)


def test_jdtast_ifstatement_constructor_exists():
    assert callable(JDTAST_IfStatement.__init__)


def test_jdtast_ifstatement_constructor_args():
    sig = inspect.signature(JDTAST_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SuperConstructorInvocation)


def test_jdtast_superconstructorinvocation_constructor_exists():
    assert callable(JDTAST_SuperConstructorInvocation.__init__)


def test_jdtast_superconstructorinvocation_constructor_args():
    sig = inspect.signature(JDTAST_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_whilestatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_WhileStatement)


def test_jdtast_whilestatement_constructor_exists():
    assert callable(JDTAST_WhileStatement.__init__)


def test_jdtast_whilestatement_constructor_args():
    sig = inspect.signature(JDTAST_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_emptystatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_EmptyStatement)


def test_jdtast_emptystatement_constructor_exists():
    assert callable(JDTAST_EmptyStatement.__init__)


def test_jdtast_emptystatement_constructor_args():
    sig = inspect.signature(JDTAST_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ConstructorInvocation)


def test_jdtast_constructorinvocation_constructor_exists():
    assert callable(JDTAST_ConstructorInvocation.__init__)


def test_jdtast_constructorinvocation_constructor_args():
    sig = inspect.signature(JDTAST_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_dostatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_DoStatement)


def test_jdtast_dostatement_constructor_exists():
    assert callable(JDTAST_DoStatement.__init__)


def test_jdtast_dostatement_constructor_args():
    sig = inspect.signature(JDTAST_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_continuestatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ContinueStatement)


def test_jdtast_continuestatement_constructor_exists():
    assert callable(JDTAST_ContinueStatement.__init__)


def test_jdtast_continuestatement_constructor_args():
    sig = inspect.signature(JDTAST_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_breakstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_BreakStatement)


def test_jdtast_breakstatement_constructor_exists():
    assert callable(JDTAST_BreakStatement.__init__)


def test_jdtast_breakstatement_constructor_args():
    sig = inspect.signature(JDTAST_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_assertstatement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_AssertStatement)


def test_jdtast_assertstatement_constructor_exists():
    assert callable(JDTAST_AssertStatement.__init__)


def test_jdtast_assertstatement_constructor_args():
    sig = inspect.signature(JDTAST_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SuperMethodInvocation)


def test_jdtast_supermethodinvocation_constructor_exists():
    assert callable(JDTAST_SuperMethodInvocation.__init__)


def test_jdtast_supermethodinvocation_constructor_args():
    sig = inspect.signature(JDTAST_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_nullliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST_NullLiteral)


def test_jdtast_nullliteral_constructor_exists():
    assert callable(JDTAST_NullLiteral.__init__)


def test_jdtast_nullliteral_constructor_args():
    sig = inspect.signature(JDTAST_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_VariableDeclarationExpression)


def test_jdtast_variabledeclarationexpression_constructor_exists():
    assert callable(JDTAST_VariableDeclarationExpression.__init__)


def test_jdtast_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(JDTAST_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_typeliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TypeLiteral)


def test_jdtast_typeliteral_constructor_exists():
    assert callable(JDTAST_TypeLiteral.__init__)


def test_jdtast_typeliteral_constructor_args():
    sig = inspect.signature(JDTAST_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST_BooleanLiteral)


def test_jdtast_booleanliteral_constructor_exists():
    assert callable(JDTAST_BooleanLiteral.__init__)


def test_jdtast_booleanliteral_constructor_args():
    sig = inspect.signature(JDTAST_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_jdtast_booleanliteral_has_booleanValue():
    assert hasattr(JDTAST_BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in JDTAST_BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SuperFieldAccess)


def test_jdtast_superfieldaccess_constructor_exists():
    assert callable(JDTAST_SuperFieldAccess.__init__)


def test_jdtast_superfieldaccess_constructor_args():
    sig = inspect.signature(JDTAST_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_InstanceofExpression)


def test_jdtast_instanceofexpression_constructor_exists():
    assert callable(JDTAST_InstanceofExpression.__init__)


def test_jdtast_instanceofexpression_constructor_args():
    sig = inspect.signature(JDTAST_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_PostfixExpression)


def test_jdtast_postfixexpression_constructor_exists():
    assert callable(JDTAST_PostfixExpression.__init__)


def test_jdtast_postfixexpression_constructor_args():
    sig = inspect.signature(JDTAST_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast_postfixexpression_has_operator():
    assert hasattr(JDTAST_PostfixExpression, "operator")
    descriptor = None
    for klass in JDTAST_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(JDTAST_FieldAccess)


def test_jdtast_fieldaccess_constructor_exists():
    assert callable(JDTAST_FieldAccess.__init__)


def test_jdtast_fieldaccess_constructor_args():
    sig = inspect.signature(JDTAST_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_thisexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ThisExpression)


def test_jdtast_thisexpression_constructor_exists():
    assert callable(JDTAST_ThisExpression.__init__)


def test_jdtast_thisexpression_constructor_args():
    sig = inspect.signature(JDTAST_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_castexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_CastExpression)


def test_jdtast_castexpression_constructor_exists():
    assert callable(JDTAST_CastExpression.__init__)


def test_jdtast_castexpression_constructor_args():
    sig = inspect.signature(JDTAST_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_infixexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_InfixExpression)


def test_jdtast_infixexpression_constructor_exists():
    assert callable(JDTAST_InfixExpression.__init__)


def test_jdtast_infixexpression_constructor_args():
    sig = inspect.signature(JDTAST_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast_infixexpression_has_operator():
    assert hasattr(JDTAST_InfixExpression, "operator")
    descriptor = None
    for klass in JDTAST_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_assignment_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Assignment)


def test_jdtast_assignment_constructor_exists():
    assert callable(JDTAST_Assignment.__init__)


def test_jdtast_assignment_constructor_args():
    sig = inspect.signature(JDTAST_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast_assignment_has_operator():
    assert hasattr(JDTAST_Assignment, "operator")
    descriptor = None
    for klass in JDTAST_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_stringliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST_StringLiteral)


def test_jdtast_stringliteral_constructor_exists():
    assert callable(JDTAST_StringLiteral.__init__)


def test_jdtast_stringliteral_constructor_args():
    sig = inspect.signature(JDTAST_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_jdtast_stringliteral_has_escapedValue():
    assert hasattr(JDTAST_StringLiteral, "escapedValue")
    descriptor = None
    for klass in JDTAST_StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_stringliteral_has_literalValue():
    assert hasattr(JDTAST_StringLiteral, "literalValue")
    descriptor = None
    for klass in JDTAST_StringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MethodInvocation)


def test_jdtast_methodinvocation_constructor_exists():
    assert callable(JDTAST_MethodInvocation.__init__)


def test_jdtast_methodinvocation_constructor_args():
    sig = inspect.signature(JDTAST_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ArrayAccess)


def test_jdtast_arrayaccess_constructor_exists():
    assert callable(JDTAST_ArrayAccess.__init__)


def test_jdtast_arrayaccess_constructor_args():
    sig = inspect.signature(JDTAST_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ParenthesizedExpression)


def test_jdtast_parenthesizedexpression_constructor_exists():
    assert callable(JDTAST_ParenthesizedExpression.__init__)


def test_jdtast_parenthesizedexpression_constructor_args():
    sig = inspect.signature(JDTAST_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_PrefixExpression)


def test_jdtast_prefixexpression_constructor_exists():
    assert callable(JDTAST_PrefixExpression.__init__)


def test_jdtast_prefixexpression_constructor_args():
    sig = inspect.signature(JDTAST_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdtast_prefixexpression_has_operator():
    assert hasattr(JDTAST_PrefixExpression, "operator")
    descriptor = None
    for klass in JDTAST_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ClassInstanceCreation)


def test_jdtast_classinstancecreation_constructor_exists():
    assert callable(JDTAST_ClassInstanceCreation.__init__)


def test_jdtast_classinstancecreation_constructor_args():
    sig = inspect.signature(JDTAST_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ConditionalExpression)


def test_jdtast_conditionalexpression_constructor_exists():
    assert callable(JDTAST_ConditionalExpression.__init__)


def test_jdtast_conditionalexpression_constructor_args():
    sig = inspect.signature(JDTAST_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_numberliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST_NumberLiteral)


def test_jdtast_numberliteral_constructor_exists():
    assert callable(JDTAST_NumberLiteral.__init__)


def test_jdtast_numberliteral_constructor_args():
    sig = inspect.signature(JDTAST_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_jdtast_numberliteral_has_token():
    assert hasattr(JDTAST_NumberLiteral, "token")
    descriptor = None
    for klass in JDTAST_NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_characterliteral_is_not_abstract():
    assert not inspect.isabstract(JDTAST_CharacterLiteral)


def test_jdtast_characterliteral_constructor_exists():
    assert callable(JDTAST_CharacterLiteral.__init__)


def test_jdtast_characterliteral_constructor_args():
    sig = inspect.signature(JDTAST_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "charValue" in params, "Missing parameter 'charValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_jdtast_characterliteral_has_charValue():
    assert hasattr(JDTAST_CharacterLiteral, "charValue")
    descriptor = None
    for klass in JDTAST_CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_characterliteral_has_escapedValue():
    assert hasattr(JDTAST_CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in JDTAST_CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_linecomment_is_not_abstract():
    assert not inspect.isabstract(JDTAST_LineComment)


def test_jdtast_linecomment_constructor_exists():
    assert callable(JDTAST_LineComment.__init__)


def test_jdtast_linecomment_constructor_args():
    sig = inspect.signature(JDTAST_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_blockcomment_is_not_abstract():
    assert not inspect.isabstract(JDTAST_BlockComment)


def test_jdtast_blockcomment_constructor_exists():
    assert callable(JDTAST_BlockComment.__init__)


def test_jdtast_blockcomment_constructor_args():
    sig = inspect.signature(JDTAST_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_EnumDeclaration)


def test_jdtast_enumdeclaration_constructor_exists():
    assert callable(JDTAST_EnumDeclaration.__init__)


def test_jdtast_enumdeclaration_constructor_args():
    sig = inspect.signature(JDTAST_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TypeDeclaration)


def test_jdtast_typedeclaration_constructor_exists():
    assert callable(JDTAST_TypeDeclaration.__init__)


def test_jdtast_typedeclaration_constructor_args():
    sig = inspect.signature(JDTAST_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_jdtast_typedeclaration_has_interface():
    assert hasattr(JDTAST_TypeDeclaration, "interface")
    descriptor = None
    for klass in JDTAST_TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_AnnotationTypeDeclaration)


def test_jdtast_annotationtypedeclaration_constructor_exists():
    assert callable(JDTAST_AnnotationTypeDeclaration.__init__)


def test_jdtast_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JDTAST_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_arraytype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ArrayType)


def test_jdtast_arraytype_constructor_exists():
    assert callable(JDTAST_ArrayType.__init__)


def test_jdtast_arraytype_constructor_args():
    sig = inspect.signature(JDTAST_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_jdtast_arraytype_has_dimensions():
    assert hasattr(JDTAST_ArrayType, "dimensions")
    descriptor = None
    for klass in JDTAST_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ArrayInitializer)


def test_jdtast_arrayinitializer_constructor_exists():
    assert callable(JDTAST_ArrayInitializer.__init__)


def test_jdtast_arrayinitializer_constructor_args():
    sig = inspect.signature(JDTAST_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_arraycreation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ArrayCreation)


def test_jdtast_arraycreation_constructor_exists():
    assert callable(JDTAST_ArrayCreation.__init__)


def test_jdtast_arraycreation_constructor_args():
    sig = inspect.signature(JDTAST_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(JDTAST_VariableDeclarationFragment)


def test_jdtast_variabledeclarationfragment_constructor_exists():
    assert callable(JDTAST_VariableDeclarationFragment.__init__)


def test_jdtast_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(JDTAST_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_FieldDeclaration)


def test_jdtast_fielddeclaration_constructor_exists():
    assert callable(JDTAST_FieldDeclaration.__init__)


def test_jdtast_fielddeclaration_constructor_args():
    sig = inspect.signature(JDTAST_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_initializer_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Initializer)


def test_jdtast_initializer_constructor_exists():
    assert callable(JDTAST_Initializer.__init__)


def test_jdtast_initializer_constructor_args():
    sig = inspect.signature(JDTAST_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MethodDeclaration)


def test_jdtast_methoddeclaration_constructor_exists():
    assert callable(JDTAST_MethodDeclaration.__init__)


def test_jdtast_methoddeclaration_constructor_args():
    sig = inspect.signature(JDTAST_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_jdtast_methoddeclaration_has_extraDimensions():
    assert hasattr(JDTAST_MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in JDTAST_MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_methoddeclaration_has_constructor():
    assert hasattr(JDTAST_MethodDeclaration, "constructor")
    descriptor = None
    for klass in JDTAST_MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_methoddeclaration_has_varargs():
    assert hasattr(JDTAST_MethodDeclaration, "varargs")
    descriptor = None
    for klass in JDTAST_MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_AnnotationTypeMemberDeclaration)


def test_jdtast_annotationtypememberdeclaration_constructor_exists():
    assert callable(JDTAST_AnnotationTypeMemberDeclaration.__init__)


def test_jdtast_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(JDTAST_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_EnumConstantDeclaration)


def test_jdtast_enumconstantdeclaration_constructor_exists():
    assert callable(JDTAST_EnumConstantDeclaration.__init__)


def test_jdtast_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(JDTAST_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_simplename_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SimpleName)


def test_jdtast_simplename_constructor_exists():
    assert callable(JDTAST_SimpleName.__init__)


def test_jdtast_simplename_constructor_args():
    sig = inspect.signature(JDTAST_SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_jdtast_simplename_has_declaration():
    assert hasattr(JDTAST_SimpleName, "declaration")
    descriptor = None
    for klass in JDTAST_SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_simplename_has_identifier():
    assert hasattr(JDTAST_SimpleName, "identifier")
    descriptor = None
    for klass in JDTAST_SimpleName.__mro__:
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



def test_jdtast_annotation_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Annotation)


def test_jdtast_annotation_constructor_exists():
    assert callable(JDTAST_Annotation.__init__)


def test_jdtast_annotation_constructor_args():
    sig = inspect.signature(JDTAST_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_name_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Name)


def test_jdtast_name_constructor_exists():
    assert callable(JDTAST_Name.__init__)


def test_jdtast_name_constructor_args():
    sig = inspect.signature(JDTAST_Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_jdtast_name_has_fullyQualifiedName():
    assert hasattr(JDTAST_Name, "fullyQualifiedName")
    descriptor = None
    for klass in JDTAST_Name.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_AbstractTypeDeclaration)


def test_jdtast_abstracttypedeclaration_constructor_exists():
    assert callable(JDTAST_AbstractTypeDeclaration.__init__)


def test_jdtast_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JDTAST_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"

def test_jdtast_abstracttypedeclaration_has_memberTypeDeclaration():
    assert hasattr(JDTAST_AbstractTypeDeclaration, "memberTypeDeclaration")
    descriptor = None
    for klass in JDTAST_AbstractTypeDeclaration.__mro__:
        if "memberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["memberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_abstracttypedeclaration_has_packageMemberTypeDeclaration():
    assert hasattr(JDTAST_AbstractTypeDeclaration, "packageMemberTypeDeclaration")
    descriptor = None
    for klass in JDTAST_AbstractTypeDeclaration.__mro__:
        if "packageMemberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["packageMemberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_abstracttypedeclaration_has_localTypeDeclaration():
    assert hasattr(JDTAST_AbstractTypeDeclaration, "localTypeDeclaration")
    descriptor = None
    for klass in JDTAST_AbstractTypeDeclaration.__mro__:
        if "localTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["localTypeDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SingleVariableDeclaration)


def test_jdtast_singlevariabledeclaration_constructor_exists():
    assert callable(JDTAST_SingleVariableDeclaration.__init__)


def test_jdtast_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(JDTAST_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_jdtast_singlevariabledeclaration_has_varargs():
    assert hasattr(JDTAST_SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in JDTAST_SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_block_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Block)


def test_jdtast_block_constructor_exists():
    assert callable(JDTAST_Block.__init__)


def test_jdtast_block_constructor_args():
    sig = inspect.signature(JDTAST_Block.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_astnode_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ASTNode)


def test_jdtast_astnode_constructor_exists():
    assert callable(JDTAST_ASTNode.__init__)


def test_jdtast_astnode_constructor_args():
    sig = inspect.signature(JDTAST_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_ast_is_not_abstract():
    assert not inspect.isabstract(JDTAST_AST)


def test_jdtast_ast_constructor_exists():
    assert callable(JDTAST_AST.__init__)


def test_jdtast_ast_constructor_args():
    sig = inspect.signature(JDTAST_AST.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_parameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Parameter)


def test_jdtast_parameter_constructor_exists():
    assert callable(JDTAST_Parameter.__init__)


def test_jdtast_parameter_constructor_args():
    sig = inspect.signature(JDTAST_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_jdtast_parameter_has_name():
    assert hasattr(JDTAST_Parameter, "name")
    descriptor = None
    for klass in JDTAST_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_parameter_has_type():
    assert hasattr(JDTAST_Parameter, "type")
    descriptor = None
    for klass in JDTAST_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_javadoc_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Javadoc)


def test_jdtast_javadoc_constructor_exists():
    assert callable(JDTAST_Javadoc.__init__)


def test_jdtast_javadoc_constructor_args():
    sig = inspect.signature(JDTAST_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ExtendedModifier)


def test_jdtast_extendedmodifier_constructor_exists():
    assert callable(JDTAST_ExtendedModifier.__init__)


def test_jdtast_extendedmodifier_constructor_args():
    sig = inspect.signature(JDTAST_ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_BodyDeclaration)


def test_jdtast_bodydeclaration_constructor_exists():
    assert callable(JDTAST_BodyDeclaration.__init__)


def test_jdtast_bodydeclaration_constructor_args():
    sig = inspect.signature(JDTAST_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_catchclause_is_not_abstract():
    assert not inspect.isabstract(JDTAST_CatchClause)


def test_jdtast_catchclause_constructor_exists():
    assert callable(JDTAST_CatchClause.__init__)


def test_jdtast_catchclause_constructor_args():
    sig = inspect.signature(JDTAST_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_modifier_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Modifier)


def test_jdtast_modifier_constructor_exists():
    assert callable(JDTAST_Modifier.__init__)


def test_jdtast_modifier_constructor_args():
    sig = inspect.signature(JDTAST_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "private" in params, "Missing parameter 'private'"
    assert "public" in params, "Missing parameter 'public'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "none" in params, "Missing parameter 'none'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "native" in params, "Missing parameter 'native'"
    assert "final" in params, "Missing parameter 'final'"
    assert "static" in params, "Missing parameter 'static'"
    assert "protected" in params, "Missing parameter 'protected'"

def test_jdtast_modifier_has_private():
    assert hasattr(JDTAST_Modifier, "private")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_public():
    assert hasattr(JDTAST_Modifier, "public")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_volatile():
    assert hasattr(JDTAST_Modifier, "volatile")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_transient():
    assert hasattr(JDTAST_Modifier, "transient")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_synchronized():
    assert hasattr(JDTAST_Modifier, "synchronized")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_strictfp():
    assert hasattr(JDTAST_Modifier, "strictfp")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_none():
    assert hasattr(JDTAST_Modifier, "none")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_abstract():
    assert hasattr(JDTAST_Modifier, "abstract")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_native():
    assert hasattr(JDTAST_Modifier, "native")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_final():
    assert hasattr(JDTAST_Modifier, "final")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_static():
    assert hasattr(JDTAST_Modifier, "static")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_modifier_has_protected():
    assert hasattr(JDTAST_Modifier, "protected")
    descriptor = None
    for klass in JDTAST_Modifier.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_textelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TextElement)


def test_jdtast_textelement_constructor_exists():
    assert callable(JDTAST_TextElement.__init__)


def test_jdtast_textelement_constructor_args():
    sig = inspect.signature(JDTAST_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_jdtast_textelement_has_text():
    assert hasattr(JDTAST_TextElement, "text")
    descriptor = None
    for klass in JDTAST_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_comment_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Comment)


def test_jdtast_comment_constructor_exists():
    assert callable(JDTAST_Comment.__init__)


def test_jdtast_comment_constructor_args():
    sig = inspect.signature(JDTAST_Comment.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MethodRefParameter)


def test_jdtast_methodrefparameter_constructor_exists():
    assert callable(JDTAST_MethodRefParameter.__init__)


def test_jdtast_methodrefparameter_constructor_args():
    sig = inspect.signature(JDTAST_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_jdtast_methodrefparameter_has_varargs():
    assert hasattr(JDTAST_MethodRefParameter, "varargs")
    descriptor = None
    for klass in JDTAST_MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_typeparameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TypeParameter)


def test_jdtast_typeparameter_constructor_exists():
    assert callable(JDTAST_TypeParameter.__init__)


def test_jdtast_typeparameter_constructor_args():
    sig = inspect.signature(JDTAST_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_expression_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Expression)


def test_jdtast_expression_constructor_exists():
    assert callable(JDTAST_Expression.__init__)


def test_jdtast_expression_constructor_args():
    sig = inspect.signature(JDTAST_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"

def test_jdtast_expression_has_resolveBoxing():
    assert hasattr(JDTAST_Expression, "resolveBoxing")
    descriptor = None
    for klass in JDTAST_Expression.__mro__:
        if "resolveBoxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveBoxing"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_expression_has_resolveUnboxing():
    assert hasattr(JDTAST_Expression, "resolveUnboxing")
    descriptor = None
    for klass in JDTAST_Expression.__mro__:
        if "resolveUnboxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveUnboxing"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ImportDeclaration)


def test_jdtast_importdeclaration_constructor_exists():
    assert callable(JDTAST_ImportDeclaration.__init__)


def test_jdtast_importdeclaration_constructor_args():
    sig = inspect.signature(JDTAST_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"

def test_jdtast_importdeclaration_has_onDemand():
    assert hasattr(JDTAST_ImportDeclaration, "onDemand")
    descriptor = None
    for klass in JDTAST_ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_importdeclaration_has_static():
    assert hasattr(JDTAST_ImportDeclaration, "static")
    descriptor = None
    for klass in JDTAST_ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_memberref_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MemberRef)


def test_jdtast_memberref_constructor_exists():
    assert callable(JDTAST_MemberRef.__init__)


def test_jdtast_memberref_constructor_args():
    sig = inspect.signature(JDTAST_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_type_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Type)


def test_jdtast_type_constructor_exists():
    assert callable(JDTAST_Type.__init__)


def test_jdtast_type_constructor_args():
    sig = inspect.signature(JDTAST_Type.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_methodref_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MethodRef)


def test_jdtast_methodref_constructor_exists():
    assert callable(JDTAST_MethodRef.__init__)


def test_jdtast_methodref_constructor_args():
    sig = inspect.signature(JDTAST_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_VariableDeclaration)


def test_jdtast_variabledeclaration_constructor_exists():
    assert callable(JDTAST_VariableDeclaration.__init__)


def test_jdtast_variabledeclaration_constructor_args():
    sig = inspect.signature(JDTAST_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_jdtast_variabledeclaration_has_extraDimensions():
    assert hasattr(JDTAST_VariableDeclaration, "extraDimensions")
    descriptor = None
    for klass in JDTAST_VariableDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_statement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_Statement)


def test_jdtast_statement_constructor_exists():
    assert callable(JDTAST_Statement.__init__)


def test_jdtast_statement_constructor_args():
    sig = inspect.signature(JDTAST_Statement.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(JDTAST_MemberValuePair)


def test_jdtast_membervaluepair_constructor_exists():
    assert callable(JDTAST_MemberValuePair.__init__)


def test_jdtast_membervaluepair_constructor_args():
    sig = inspect.signature(JDTAST_MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_tagelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_TagElement)


def test_jdtast_tagelement_constructor_exists():
    assert callable(JDTAST_TagElement.__init__)


def test_jdtast_tagelement_constructor_args():
    sig = inspect.signature(JDTAST_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "nested" in params, "Missing parameter 'nested'"
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_jdtast_tagelement_has_nested():
    assert hasattr(JDTAST_TagElement, "nested")
    descriptor = None
    for klass in JDTAST_TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_tagelement_has_tagName():
    assert hasattr(JDTAST_TagElement, "tagName")
    descriptor = None
    for klass in JDTAST_TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_PackageDeclaration)


def test_jdtast_packagedeclaration_constructor_exists():
    assert callable(JDTAST_PackageDeclaration.__init__)


def test_jdtast_packagedeclaration_constructor_args():
    sig = inspect.signature(JDTAST_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_AnonymousClassDeclaration)


def test_jdtast_anonymousclassdeclaration_constructor_exists():
    assert callable(JDTAST_AnonymousClassDeclaration.__init__)


def test_jdtast_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(JDTAST_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_imember_is_not_abstract():
    assert not inspect.isabstract(IMember)


def test_imember_constructor_exists():
    assert callable(IMember.__init__)


def test_imember_constructor_args():
    sig = inspect.signature(IMember.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_imethod_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IMethod)


def test_jdtast_imethod_constructor_exists():
    assert callable(JDTAST_IMethod.__init__)


def test_jdtast_imethod_constructor_args():
    sig = inspect.signature(JDTAST_IMethod.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionTypes" in params, "Missing parameter 'exceptionTypes'"
    assert "isMainMethod" in params, "Missing parameter 'isMainMethod'"
    assert "isConstructor" in params, "Missing parameter 'isConstructor'"
    assert "returnType" in params, "Missing parameter 'returnType'"

def test_jdtast_imethod_has_exceptionTypes():
    assert hasattr(JDTAST_IMethod, "exceptionTypes")
    descriptor = None
    for klass in JDTAST_IMethod.__mro__:
        if "exceptionTypes" in klass.__dict__:
            descriptor = klass.__dict__["exceptionTypes"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_imethod_has_isMainMethod():
    assert hasattr(JDTAST_IMethod, "isMainMethod")
    descriptor = None
    for klass in JDTAST_IMethod.__mro__:
        if "isMainMethod" in klass.__dict__:
            descriptor = klass.__dict__["isMainMethod"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_imethod_has_isConstructor():
    assert hasattr(JDTAST_IMethod, "isConstructor")
    descriptor = None
    for klass in JDTAST_IMethod.__mro__:
        if "isConstructor" in klass.__dict__:
            descriptor = klass.__dict__["isConstructor"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_imethod_has_returnType():
    assert hasattr(JDTAST_IMethod, "returnType")
    descriptor = None
    for klass in JDTAST_IMethod.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_iinitializer_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IInitializer)


def test_jdtast_iinitializer_constructor_exists():
    assert callable(JDTAST_IInitializer.__init__)


def test_jdtast_iinitializer_constructor_args():
    sig = inspect.signature(JDTAST_IInitializer.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_ifield_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IField)


def test_jdtast_ifield_constructor_exists():
    assert callable(JDTAST_IField.__init__)


def test_jdtast_ifield_constructor_args():
    sig = inspect.signature(JDTAST_IField.__init__)
    params = list(sig.parameters.keys())
    assert "isEnumConstant" in params, "Missing parameter 'isEnumConstant'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "isTransient" in params, "Missing parameter 'isTransient'"
    assert "typeSignature" in params, "Missing parameter 'typeSignature'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_jdtast_ifield_has_isEnumConstant():
    assert hasattr(JDTAST_IField, "isEnumConstant")
    descriptor = None
    for klass in JDTAST_IField.__mro__:
        if "isEnumConstant" in klass.__dict__:
            descriptor = klass.__dict__["isEnumConstant"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_ifield_has_isVolatile():
    assert hasattr(JDTAST_IField, "isVolatile")
    descriptor = None
    for klass in JDTAST_IField.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_ifield_has_isTransient():
    assert hasattr(JDTAST_IField, "isTransient")
    descriptor = None
    for klass in JDTAST_IField.__mro__:
        if "isTransient" in klass.__dict__:
            descriptor = klass.__dict__["isTransient"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_ifield_has_typeSignature():
    assert hasattr(JDTAST_IField, "typeSignature")
    descriptor = None
    for klass in JDTAST_IField.__mro__:
        if "typeSignature" in klass.__dict__:
            descriptor = klass.__dict__["typeSignature"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_ifield_has_constant():
    assert hasattr(JDTAST_IField, "constant")
    descriptor = None
    for klass in JDTAST_IField.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_isourcerange_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ISourceRange)


def test_jdtast_isourcerange_constructor_exists():
    assert callable(JDTAST_ISourceRange.__init__)


def test_jdtast_isourcerange_constructor_args():
    sig = inspect.signature(JDTAST_ISourceRange.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_jdtast_isourcerange_has_length():
    assert hasattr(JDTAST_ISourceRange, "length")
    descriptor = None
    for klass in JDTAST_ISourceRange.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_isourcerange_has_offset():
    assert hasattr(JDTAST_ISourceRange, "offset")
    descriptor = None
    for klass in JDTAST_ISourceRange.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_isourcereference_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ISourceReference)


def test_jdtast_isourcereference_constructor_exists():
    assert callable(JDTAST_ISourceReference.__init__)


def test_jdtast_isourcereference_constructor_args():
    sig = inspect.signature(JDTAST_ISourceReference.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_jdtast_isourcereference_has_source():
    assert hasattr(JDTAST_ISourceReference, "source")
    descriptor = None
    for klass in JDTAST_ISourceReference.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_compilationunit_is_not_abstract():
    assert not inspect.isabstract(JDTAST_CompilationUnit)


def test_jdtast_compilationunit_constructor_exists():
    assert callable(JDTAST_CompilationUnit.__init__)


def test_jdtast_compilationunit_constructor_args():
    sig = inspect.signature(JDTAST_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(IPackageFragmentRoot)


def test_ipackagefragmentroot_constructor_exists():
    assert callable(IPackageFragmentRoot.__init__)


def test_ipackagefragmentroot_constructor_args():
    sig = inspect.signature(IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_sourcepackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(JDTAST_SourcePackageFragmentRoot)


def test_jdtast_sourcepackagefragmentroot_constructor_exists():
    assert callable(JDTAST_SourcePackageFragmentRoot.__init__)


def test_jdtast_sourcepackagefragmentroot_constructor_args():
    sig = inspect.signature(JDTAST_SourcePackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_binarypackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(JDTAST_BinaryPackageFragmentRoot)


def test_jdtast_binarypackagefragmentroot_constructor_exists():
    assert callable(JDTAST_BinaryPackageFragmentRoot.__init__)


def test_jdtast_binarypackagefragmentroot_constructor_args():
    sig = inspect.signature(JDTAST_BinaryPackageFragmentRoot.__init__)
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



def test_jdtast_ijavaproject_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IJavaProject)


def test_jdtast_ijavaproject_constructor_exists():
    assert callable(JDTAST_IJavaProject.__init__)


def test_jdtast_ijavaproject_constructor_args():
    sig = inspect.signature(JDTAST_IJavaProject.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IPackageFragment)


def test_jdtast_ipackagefragment_constructor_exists():
    assert callable(JDTAST_IPackageFragment.__init__)


def test_jdtast_ipackagefragment_constructor_args():
    sig = inspect.signature(JDTAST_IPackageFragment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefaultPackage" in params, "Missing parameter 'isDefaultPackage'"

def test_jdtast_ipackagefragment_has_isDefaultPackage():
    assert hasattr(JDTAST_IPackageFragment, "isDefaultPackage")
    descriptor = None
    for klass in JDTAST_IPackageFragment.__mro__:
        if "isDefaultPackage" in klass.__dict__:
            descriptor = klass.__dict__["isDefaultPackage"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IPackageFragmentRoot)


def test_jdtast_ipackagefragmentroot_constructor_exists():
    assert callable(JDTAST_IPackageFragmentRoot.__init__)


def test_jdtast_ipackagefragmentroot_constructor_args():
    sig = inspect.signature(JDTAST_IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_ijavamodel_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IJavaModel)


def test_jdtast_ijavamodel_constructor_exists():
    assert callable(JDTAST_IJavaModel.__init__)


def test_jdtast_ijavamodel_constructor_args():
    sig = inspect.signature(JDTAST_IJavaModel.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_physicalelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_PhysicalElement)


def test_jdtast_physicalelement_constructor_exists():
    assert callable(JDTAST_PhysicalElement.__init__)


def test_jdtast_physicalelement_constructor_args():
    sig = inspect.signature(JDTAST_PhysicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "path" in params, "Missing parameter 'path'"

def test_jdtast_physicalelement_has_isReadOnly():
    assert hasattr(JDTAST_PhysicalElement, "isReadOnly")
    descriptor = None
    for klass in JDTAST_PhysicalElement.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_physicalelement_has_path():
    assert hasattr(JDTAST_PhysicalElement, "path")
    descriptor = None
    for klass in JDTAST_PhysicalElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_ijavaelement_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IJavaElement)


def test_jdtast_ijavaelement_constructor_exists():
    assert callable(JDTAST_IJavaElement.__init__)


def test_jdtast_ijavaelement_constructor_args():
    sig = inspect.signature(JDTAST_IJavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"

def test_jdtast_ijavaelement_has_elementName():
    assert hasattr(JDTAST_IJavaElement, "elementName")
    descriptor = None
    for klass in JDTAST_IJavaElement.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_itype_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IType)


def test_jdtast_itype_constructor_exists():
    assert callable(JDTAST_IType.__init__)


def test_jdtast_itype_constructor_args():
    sig = inspect.signature(JDTAST_IType.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"
    assert "fullyQualifiedParametrizedName" in params, "Missing parameter 'fullyQualifiedParametrizedName'"

def test_jdtast_itype_has_fullyQualifiedName():
    assert hasattr(JDTAST_IType, "fullyQualifiedName")
    descriptor = None
    for klass in JDTAST_IType.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_itype_has_fullyQualifiedParametrizedName():
    assert hasattr(JDTAST_IType, "fullyQualifiedParametrizedName")
    descriptor = None
    for klass in JDTAST_IType.__mro__:
        if "fullyQualifiedParametrizedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedParametrizedName"]
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



def test_jdtast_iimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IImportDeclaration)


def test_jdtast_iimportdeclaration_constructor_exists():
    assert callable(JDTAST_IImportDeclaration.__init__)


def test_jdtast_iimportdeclaration_constructor_args():
    sig = inspect.signature(JDTAST_IImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isOnDemand" in params, "Missing parameter 'isOnDemand'"

def test_jdtast_iimportdeclaration_has_isStatic():
    assert hasattr(JDTAST_IImportDeclaration, "isStatic")
    descriptor = None
    for klass in JDTAST_IImportDeclaration.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_iimportdeclaration_has_isOnDemand():
    assert hasattr(JDTAST_IImportDeclaration, "isOnDemand")
    descriptor = None
    for klass in JDTAST_IImportDeclaration.__mro__:
        if "isOnDemand" in klass.__dict__:
            descriptor = klass.__dict__["isOnDemand"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_imember_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IMember)


def test_jdtast_imember_constructor_exists():
    assert callable(JDTAST_IMember.__init__)


def test_jdtast_imember_constructor_args():
    sig = inspect.signature(JDTAST_IMember.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_itypeparameter_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ITypeParameter)


def test_jdtast_itypeparameter_constructor_exists():
    assert callable(JDTAST_ITypeParameter.__init__)


def test_jdtast_itypeparameter_constructor_args():
    sig = inspect.signature(JDTAST_ITypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "bounds" in params, "Missing parameter 'bounds'"

def test_jdtast_itypeparameter_has_bounds():
    assert hasattr(JDTAST_ITypeParameter, "bounds")
    descriptor = None
    for klass in JDTAST_ITypeParameter.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)



def test_jdtast_ityperoot_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ITypeRoot)


def test_jdtast_ityperoot_constructor_exists():
    assert callable(JDTAST_ITypeRoot.__init__)


def test_jdtast_ityperoot_constructor_args():
    sig = inspect.signature(JDTAST_ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_icompilationunit_is_not_abstract():
    assert not inspect.isabstract(JDTAST_ICompilationUnit)


def test_jdtast_icompilationunit_constructor_exists():
    assert callable(JDTAST_ICompilationUnit.__init__)


def test_jdtast_icompilationunit_constructor_args():
    sig = inspect.signature(JDTAST_ICompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_jdtast_iclassfile_is_not_abstract():
    assert not inspect.isabstract(JDTAST_IClassFile)


def test_jdtast_iclassfile_constructor_exists():
    assert callable(JDTAST_IClassFile.__init__)


def test_jdtast_iclassfile_constructor_args():
    sig = inspect.signature(JDTAST_IClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "isInterface" in params, "Missing parameter 'isInterface'"
    assert "isClass" in params, "Missing parameter 'isClass'"

def test_jdtast_iclassfile_has_isInterface():
    assert hasattr(JDTAST_IClassFile, "isInterface")
    descriptor = None
    for klass in JDTAST_IClassFile.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)

def test_jdtast_iclassfile_has_isClass():
    assert hasattr(JDTAST_IClassFile, "isClass")
    descriptor = None
    for klass in JDTAST_IClassFile.__mro__:
        if "isClass" in klass.__dict__:
            descriptor = klass.__dict__["isClass"]
            break
    assert isinstance(descriptor, property)

def test_modifiers_exists():
    # Check that the Enumeration exists
    assert Modifiers is not None

def test_modifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Modifiers]
    expected_literals = [
        "abstract",
        "strictfp",
        "annotation",
        "deprecated",
        "transient",
        "volatile",
        "interface",
        "varargs",
        "enum",
        "native",
        "default",
        "synthetic",
        "final",
        "public",
        "synchronized",
        "private",
        "super",
        "bridge",
        "static",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Modifiers"

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "times",
        "left_shift",
        "greater",
        "conditional_or",
        "remainder",
        "conditional_and",
        "equals",
        "right_shift_unsigned",
        "not_equals",
        "or_",
        "divide",
        "less_equals",
        "right_shift_signed",
        "plus",
        "less",
        "minus",
        "xor",
        "and_",
        "greater_equals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

def test_assignmentoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorKind is not None

def test_assignmentoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorKind]
    expected_literals = [
        "remainder_assign",
        "times_assign",
        "bit_or_assign",
        "plus_assign",
        "divide_assign",
        "bit_and_assign",
        "left_shift_assign",
        "bit_xor_assign",
        "right_shift_signed_assign",
        "right_shift_unsigned_assign",
        "minus_assign",
        "assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"

def test_postfixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpressionOperatorKind is not None

def test_postfixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpressionOperatorKind]
    expected_literals = [
        "increment",
        "decrement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpressionOperatorKind"

def test_prefixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionOperatorKind is not None

def test_prefixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionOperatorKind]
    expected_literals = [
        "decrement",
        "increment",
        "plus",
        "not_",
        "minus",
        "complement",
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
Name_strategy = st.builds(
    Name,
)
JDTAST_QualifiedName_strategy = st.builds(
    JDTAST_QualifiedName,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
Annotation_strategy = st.builds(
    Annotation,
)
JDTAST_SingleMemberAnnotation_strategy = st.builds(
    JDTAST_SingleMemberAnnotation,
)
JDTAST_NormalAnnotation_strategy = st.builds(
    JDTAST_NormalAnnotation,
)
JDTAST_MarkerAnnotation_strategy = st.builds(
    JDTAST_MarkerAnnotation,
)
Type_strategy = st.builds(
    Type,
)
JDTAST_ParameterizedType_strategy = st.builds(
    JDTAST_ParameterizedType,
)
JDTAST_WildcardType_strategy = st.builds(
    JDTAST_WildcardType,
    upperBound=
        safe_text
)
JDTAST_SimpleType_strategy = st.builds(
    JDTAST_SimpleType,
)
JDTAST_QualifiedType_strategy = st.builds(
    JDTAST_QualifiedType,
)
JDTAST_PrimitiveType_strategy = st.builds(
    JDTAST_PrimitiveType,
    code=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
JDTAST_ThrowStatement_strategy = st.builds(
    JDTAST_ThrowStatement,
)
JDTAST_TryStatement_strategy = st.builds(
    JDTAST_TryStatement,
)
JDTAST_ExpressionStatement_strategy = st.builds(
    JDTAST_ExpressionStatement,
)
JDTAST_LabeledStatement_strategy = st.builds(
    JDTAST_LabeledStatement,
)
JDTAST_SynchronizedStatement_strategy = st.builds(
    JDTAST_SynchronizedStatement,
)
JDTAST_ReturnStatement_strategy = st.builds(
    JDTAST_ReturnStatement,
)
JDTAST_EnhancedForStatement_strategy = st.builds(
    JDTAST_EnhancedForStatement,
)
JDTAST_SwitchCase_strategy = st.builds(
    JDTAST_SwitchCase,
    default=
        safe_text
)
JDTAST_SwitchStatement_strategy = st.builds(
    JDTAST_SwitchStatement,
)
JDTAST_TypeDeclarationStatement_strategy = st.builds(
    JDTAST_TypeDeclarationStatement,
)
JDTAST_VariableDeclarationStatement_strategy = st.builds(
    JDTAST_VariableDeclarationStatement,
)
JDTAST_ForStatement_strategy = st.builds(
    JDTAST_ForStatement,
)
JDTAST_IfStatement_strategy = st.builds(
    JDTAST_IfStatement,
)
JDTAST_SuperConstructorInvocation_strategy = st.builds(
    JDTAST_SuperConstructorInvocation,
)
JDTAST_WhileStatement_strategy = st.builds(
    JDTAST_WhileStatement,
)
JDTAST_EmptyStatement_strategy = st.builds(
    JDTAST_EmptyStatement,
)
JDTAST_ConstructorInvocation_strategy = st.builds(
    JDTAST_ConstructorInvocation,
)
JDTAST_DoStatement_strategy = st.builds(
    JDTAST_DoStatement,
)
JDTAST_ContinueStatement_strategy = st.builds(
    JDTAST_ContinueStatement,
)
JDTAST_BreakStatement_strategy = st.builds(
    JDTAST_BreakStatement,
)
JDTAST_AssertStatement_strategy = st.builds(
    JDTAST_AssertStatement,
)
Expression_strategy = st.builds(
    Expression,
)
JDTAST_SuperMethodInvocation_strategy = st.builds(
    JDTAST_SuperMethodInvocation,
)
JDTAST_NullLiteral_strategy = st.builds(
    JDTAST_NullLiteral,
)
JDTAST_VariableDeclarationExpression_strategy = st.builds(
    JDTAST_VariableDeclarationExpression,
)
JDTAST_TypeLiteral_strategy = st.builds(
    JDTAST_TypeLiteral,
)
JDTAST_BooleanLiteral_strategy = st.builds(
    JDTAST_BooleanLiteral,
    booleanValue=
        safe_text
)
JDTAST_SuperFieldAccess_strategy = st.builds(
    JDTAST_SuperFieldAccess,
)
JDTAST_InstanceofExpression_strategy = st.builds(
    JDTAST_InstanceofExpression,
)
JDTAST_PostfixExpression_strategy = st.builds(
    JDTAST_PostfixExpression,
    operator=
        safe_text
)
JDTAST_FieldAccess_strategy = st.builds(
    JDTAST_FieldAccess,
)
JDTAST_ThisExpression_strategy = st.builds(
    JDTAST_ThisExpression,
)
JDTAST_CastExpression_strategy = st.builds(
    JDTAST_CastExpression,
)
JDTAST_InfixExpression_strategy = st.builds(
    JDTAST_InfixExpression,
    operator=
        safe_text
)
JDTAST_Assignment_strategy = st.builds(
    JDTAST_Assignment,
    operator=
        safe_text
)
JDTAST_StringLiteral_strategy = st.builds(
    JDTAST_StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
JDTAST_MethodInvocation_strategy = st.builds(
    JDTAST_MethodInvocation,
)
JDTAST_ArrayAccess_strategy = st.builds(
    JDTAST_ArrayAccess,
)
JDTAST_ParenthesizedExpression_strategy = st.builds(
    JDTAST_ParenthesizedExpression,
)
JDTAST_PrefixExpression_strategy = st.builds(
    JDTAST_PrefixExpression,
    operator=
        safe_text
)
JDTAST_ClassInstanceCreation_strategy = st.builds(
    JDTAST_ClassInstanceCreation,
)
JDTAST_ConditionalExpression_strategy = st.builds(
    JDTAST_ConditionalExpression,
)
JDTAST_NumberLiteral_strategy = st.builds(
    JDTAST_NumberLiteral,
    token=
        safe_text
)
JDTAST_CharacterLiteral_strategy = st.builds(
    JDTAST_CharacterLiteral,
    charValue=
        safe_text,
    escapedValue=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
JDTAST_LineComment_strategy = st.builds(
    JDTAST_LineComment,
)
JDTAST_BlockComment_strategy = st.builds(
    JDTAST_BlockComment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JDTAST_EnumDeclaration_strategy = st.builds(
    JDTAST_EnumDeclaration,
)
JDTAST_TypeDeclaration_strategy = st.builds(
    JDTAST_TypeDeclaration,
    interface=
        safe_text
)
JDTAST_AnnotationTypeDeclaration_strategy = st.builds(
    JDTAST_AnnotationTypeDeclaration,
)
JDTAST_ArrayType_strategy = st.builds(
    JDTAST_ArrayType,
    dimensions=
        safe_text
)
JDTAST_ArrayInitializer_strategy = st.builds(
    JDTAST_ArrayInitializer,
)
JDTAST_ArrayCreation_strategy = st.builds(
    JDTAST_ArrayCreation,
)
JDTAST_VariableDeclarationFragment_strategy = st.builds(
    JDTAST_VariableDeclarationFragment,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JDTAST_FieldDeclaration_strategy = st.builds(
    JDTAST_FieldDeclaration,
)
JDTAST_Initializer_strategy = st.builds(
    JDTAST_Initializer,
)
JDTAST_MethodDeclaration_strategy = st.builds(
    JDTAST_MethodDeclaration,
    extraDimensions=
        safe_text,
    constructor=
        safe_text,
    varargs=
        safe_text
)
JDTAST_AnnotationTypeMemberDeclaration_strategy = st.builds(
    JDTAST_AnnotationTypeMemberDeclaration,
)
JDTAST_EnumConstantDeclaration_strategy = st.builds(
    JDTAST_EnumConstantDeclaration,
)
JDTAST_SimpleName_strategy = st.builds(
    JDTAST_SimpleName,
    declaration=
        safe_text,
    identifier=
        safe_text
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
JDTAST_Annotation_strategy = st.builds(
    JDTAST_Annotation,
)
JDTAST_Name_strategy = st.builds(
    JDTAST_Name,
    fullyQualifiedName=
        safe_text
)
JDTAST_AbstractTypeDeclaration_strategy = st.builds(
    JDTAST_AbstractTypeDeclaration,
    memberTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text,
    localTypeDeclaration=
        safe_text
)
JDTAST_SingleVariableDeclaration_strategy = st.builds(
    JDTAST_SingleVariableDeclaration,
    varargs=
        safe_text
)
JDTAST_Block_strategy = st.builds(
    JDTAST_Block,
)
JDTAST_ASTNode_strategy = st.builds(
    JDTAST_ASTNode,
)
JDTAST_AST_strategy = st.builds(
    JDTAST_AST,
)
JDTAST_Parameter_strategy = st.builds(
    JDTAST_Parameter,
    name=
        safe_text,
    type=
        safe_text
)
JDTAST_Javadoc_strategy = st.builds(
    JDTAST_Javadoc,
)
JDTAST_ExtendedModifier_strategy = st.builds(
    JDTAST_ExtendedModifier,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JDTAST_BodyDeclaration_strategy = st.builds(
    JDTAST_BodyDeclaration,
)
JDTAST_CatchClause_strategy = st.builds(
    JDTAST_CatchClause,
)
JDTAST_Modifier_strategy = st.builds(
    JDTAST_Modifier,
    private=
        safe_text,
    public=
        safe_text,
    volatile=
        safe_text,
    transient=
        safe_text,
    synchronized=
        safe_text,
    strictfp=
        safe_text,
    none=
        safe_text,
    abstract=
        safe_text,
    native=
        safe_text,
    final=
        safe_text,
    static=
        safe_text,
    protected=
        safe_text
)
JDTAST_TextElement_strategy = st.builds(
    JDTAST_TextElement,
    text=
        safe_text
)
JDTAST_Comment_strategy = st.builds(
    JDTAST_Comment,
)
JDTAST_MethodRefParameter_strategy = st.builds(
    JDTAST_MethodRefParameter,
    varargs=
        safe_text
)
JDTAST_TypeParameter_strategy = st.builds(
    JDTAST_TypeParameter,
)
JDTAST_Expression_strategy = st.builds(
    JDTAST_Expression,
    resolveBoxing=
        safe_text,
    resolveUnboxing=
        safe_text
)
JDTAST_ImportDeclaration_strategy = st.builds(
    JDTAST_ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
JDTAST_MemberRef_strategy = st.builds(
    JDTAST_MemberRef,
)
JDTAST_Type_strategy = st.builds(
    JDTAST_Type,
)
JDTAST_MethodRef_strategy = st.builds(
    JDTAST_MethodRef,
)
JDTAST_VariableDeclaration_strategy = st.builds(
    JDTAST_VariableDeclaration,
    extraDimensions=
        safe_text
)
JDTAST_Statement_strategy = st.builds(
    JDTAST_Statement,
)
JDTAST_MemberValuePair_strategy = st.builds(
    JDTAST_MemberValuePair,
)
JDTAST_TagElement_strategy = st.builds(
    JDTAST_TagElement,
    nested=
        safe_text,
    tagName=
        safe_text
)
JDTAST_PackageDeclaration_strategy = st.builds(
    JDTAST_PackageDeclaration,
)
JDTAST_AnonymousClassDeclaration_strategy = st.builds(
    JDTAST_AnonymousClassDeclaration,
)
IMember_strategy = st.builds(
    IMember,
)
JDTAST_IMethod_strategy = st.builds(
    JDTAST_IMethod,
    exceptionTypes=
        safe_text,
    isMainMethod=
        safe_text,
    isConstructor=
        safe_text,
    returnType=
        safe_text
)
JDTAST_IInitializer_strategy = st.builds(
    JDTAST_IInitializer,
)
JDTAST_IField_strategy = st.builds(
    JDTAST_IField,
    isEnumConstant=
        safe_text,
    isVolatile=
        safe_text,
    isTransient=
        safe_text,
    typeSignature=
        safe_text,
    constant=
        safe_text
)
JDTAST_ISourceRange_strategy = st.builds(
    JDTAST_ISourceRange,
    length=
        safe_text,
    offset=
        safe_text
)
JDTAST_ISourceReference_strategy = st.builds(
    JDTAST_ISourceReference,
    source=
        safe_text
)
JDTAST_CompilationUnit_strategy = st.builds(
    JDTAST_CompilationUnit,
)
IPackageFragmentRoot_strategy = st.builds(
    IPackageFragmentRoot,
)
JDTAST_SourcePackageFragmentRoot_strategy = st.builds(
    JDTAST_SourcePackageFragmentRoot,
)
JDTAST_BinaryPackageFragmentRoot_strategy = st.builds(
    JDTAST_BinaryPackageFragmentRoot,
)
IJavaElement_strategy = st.builds(
    IJavaElement,
)
PhysicalElement_strategy = st.builds(
    PhysicalElement,
)
JDTAST_IJavaProject_strategy = st.builds(
    JDTAST_IJavaProject,
)
JDTAST_IPackageFragment_strategy = st.builds(
    JDTAST_IPackageFragment,
    isDefaultPackage=
        safe_text
)
JDTAST_IPackageFragmentRoot_strategy = st.builds(
    JDTAST_IPackageFragmentRoot,
)
JDTAST_IJavaModel_strategy = st.builds(
    JDTAST_IJavaModel,
)
JDTAST_PhysicalElement_strategy = st.builds(
    JDTAST_PhysicalElement,
    isReadOnly=
        safe_text,
    path=
        safe_text
)
JDTAST_IJavaElement_strategy = st.builds(
    JDTAST_IJavaElement,
    elementName=
        safe_text
)
JDTAST_IType_strategy = st.builds(
    JDTAST_IType,
    fullyQualifiedName=
        safe_text,
    fullyQualifiedParametrizedName=
        safe_text
)
ITypeRoot_strategy = st.builds(
    ITypeRoot,
)
ISourceReference_strategy = st.builds(
    ISourceReference,
)
JDTAST_IImportDeclaration_strategy = st.builds(
    JDTAST_IImportDeclaration,
    isStatic=
        safe_text,
    isOnDemand=
        safe_text
)
JDTAST_IMember_strategy = st.builds(
    JDTAST_IMember,
)
JDTAST_ITypeParameter_strategy = st.builds(
    JDTAST_ITypeParameter,
    bounds=
        safe_text
)
JDTAST_ITypeRoot_strategy = st.builds(
    JDTAST_ITypeRoot,
)
JDTAST_ICompilationUnit_strategy = st.builds(
    JDTAST_ICompilationUnit,
)
JDTAST_IClassFile_strategy = st.builds(
    JDTAST_IClassFile,
    isInterface=
        safe_text,
    isClass=
        safe_text
)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=JDTAST_QualifiedName_strategy)
@settings(max_examples=50)
def test_jdtast_qualifiedname_instantiation(instance):
    assert isinstance(instance, JDTAST_QualifiedName)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=JDTAST_SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_jdtast_singlememberannotation_instantiation(instance):
    assert isinstance(instance, JDTAST_SingleMemberAnnotation)

@given(instance=JDTAST_NormalAnnotation_strategy)
@settings(max_examples=50)
def test_jdtast_normalannotation_instantiation(instance):
    assert isinstance(instance, JDTAST_NormalAnnotation)

@given(instance=JDTAST_MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_jdtast_markerannotation_instantiation(instance):
    assert isinstance(instance, JDTAST_MarkerAnnotation)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JDTAST_ParameterizedType_strategy)
@settings(max_examples=50)
def test_jdtast_parameterizedtype_instantiation(instance):
    assert isinstance(instance, JDTAST_ParameterizedType)

@given(instance=JDTAST_WildcardType_strategy)
@settings(max_examples=50)
def test_jdtast_wildcardtype_instantiation(instance):
    assert isinstance(instance, JDTAST_WildcardType)



@given(instance=JDTAST_WildcardType_strategy)
def test_jdtast_wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=JDTAST_SimpleType_strategy)
@settings(max_examples=50)
def test_jdtast_simpletype_instantiation(instance):
    assert isinstance(instance, JDTAST_SimpleType)

@given(instance=JDTAST_QualifiedType_strategy)
@settings(max_examples=50)
def test_jdtast_qualifiedtype_instantiation(instance):
    assert isinstance(instance, JDTAST_QualifiedType)

@given(instance=JDTAST_PrimitiveType_strategy)
@settings(max_examples=50)
def test_jdtast_primitivetype_instantiation(instance):
    assert isinstance(instance, JDTAST_PrimitiveType)



@given(instance=JDTAST_PrimitiveType_strategy)
def test_jdtast_primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=JDTAST_ThrowStatement_strategy)
@settings(max_examples=50)
def test_jdtast_throwstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_ThrowStatement)

@given(instance=JDTAST_TryStatement_strategy)
@settings(max_examples=50)
def test_jdtast_trystatement_instantiation(instance):
    assert isinstance(instance, JDTAST_TryStatement)

@given(instance=JDTAST_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_jdtast_expressionstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_ExpressionStatement)

@given(instance=JDTAST_LabeledStatement_strategy)
@settings(max_examples=50)
def test_jdtast_labeledstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_LabeledStatement)

@given(instance=JDTAST_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_jdtast_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_SynchronizedStatement)

@given(instance=JDTAST_ReturnStatement_strategy)
@settings(max_examples=50)
def test_jdtast_returnstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_ReturnStatement)

@given(instance=JDTAST_EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_jdtast_enhancedforstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_EnhancedForStatement)

@given(instance=JDTAST_SwitchCase_strategy)
@settings(max_examples=50)
def test_jdtast_switchcase_instantiation(instance):
    assert isinstance(instance, JDTAST_SwitchCase)



@given(instance=JDTAST_SwitchCase_strategy)
def test_jdtast_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=JDTAST_SwitchStatement_strategy)
@settings(max_examples=50)
def test_jdtast_switchstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_SwitchStatement)

@given(instance=JDTAST_TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_jdtast_typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_TypeDeclarationStatement)

@given(instance=JDTAST_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_jdtast_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_VariableDeclarationStatement)

@given(instance=JDTAST_ForStatement_strategy)
@settings(max_examples=50)
def test_jdtast_forstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_ForStatement)

@given(instance=JDTAST_IfStatement_strategy)
@settings(max_examples=50)
def test_jdtast_ifstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_IfStatement)

@given(instance=JDTAST_SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_jdtast_superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST_SuperConstructorInvocation)

@given(instance=JDTAST_WhileStatement_strategy)
@settings(max_examples=50)
def test_jdtast_whilestatement_instantiation(instance):
    assert isinstance(instance, JDTAST_WhileStatement)

@given(instance=JDTAST_EmptyStatement_strategy)
@settings(max_examples=50)
def test_jdtast_emptystatement_instantiation(instance):
    assert isinstance(instance, JDTAST_EmptyStatement)

@given(instance=JDTAST_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_jdtast_constructorinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST_ConstructorInvocation)

@given(instance=JDTAST_DoStatement_strategy)
@settings(max_examples=50)
def test_jdtast_dostatement_instantiation(instance):
    assert isinstance(instance, JDTAST_DoStatement)

@given(instance=JDTAST_ContinueStatement_strategy)
@settings(max_examples=50)
def test_jdtast_continuestatement_instantiation(instance):
    assert isinstance(instance, JDTAST_ContinueStatement)

@given(instance=JDTAST_BreakStatement_strategy)
@settings(max_examples=50)
def test_jdtast_breakstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_BreakStatement)

@given(instance=JDTAST_AssertStatement_strategy)
@settings(max_examples=50)
def test_jdtast_assertstatement_instantiation(instance):
    assert isinstance(instance, JDTAST_AssertStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JDTAST_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_jdtast_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST_SuperMethodInvocation)

@given(instance=JDTAST_NullLiteral_strategy)
@settings(max_examples=50)
def test_jdtast_nullliteral_instantiation(instance):
    assert isinstance(instance, JDTAST_NullLiteral)

@given(instance=JDTAST_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_jdtast_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_VariableDeclarationExpression)

@given(instance=JDTAST_TypeLiteral_strategy)
@settings(max_examples=50)
def test_jdtast_typeliteral_instantiation(instance):
    assert isinstance(instance, JDTAST_TypeLiteral)

@given(instance=JDTAST_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_jdtast_booleanliteral_instantiation(instance):
    assert isinstance(instance, JDTAST_BooleanLiteral)



@given(instance=JDTAST_BooleanLiteral_strategy)
def test_jdtast_booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=JDTAST_SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_jdtast_superfieldaccess_instantiation(instance):
    assert isinstance(instance, JDTAST_SuperFieldAccess)

@given(instance=JDTAST_InstanceofExpression_strategy)
@settings(max_examples=50)
def test_jdtast_instanceofexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_InstanceofExpression)

@given(instance=JDTAST_PostfixExpression_strategy)
@settings(max_examples=50)
def test_jdtast_postfixexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_PostfixExpression)



@given(instance=JDTAST_PostfixExpression_strategy)
def test_jdtast_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST_FieldAccess_strategy)
@settings(max_examples=50)
def test_jdtast_fieldaccess_instantiation(instance):
    assert isinstance(instance, JDTAST_FieldAccess)

@given(instance=JDTAST_ThisExpression_strategy)
@settings(max_examples=50)
def test_jdtast_thisexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_ThisExpression)

@given(instance=JDTAST_CastExpression_strategy)
@settings(max_examples=50)
def test_jdtast_castexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_CastExpression)

@given(instance=JDTAST_InfixExpression_strategy)
@settings(max_examples=50)
def test_jdtast_infixexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_InfixExpression)



@given(instance=JDTAST_InfixExpression_strategy)
def test_jdtast_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST_Assignment_strategy)
@settings(max_examples=50)
def test_jdtast_assignment_instantiation(instance):
    assert isinstance(instance, JDTAST_Assignment)



@given(instance=JDTAST_Assignment_strategy)
def test_jdtast_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST_StringLiteral_strategy)
@settings(max_examples=50)
def test_jdtast_stringliteral_instantiation(instance):
    assert isinstance(instance, JDTAST_StringLiteral)



@given(instance=JDTAST_StringLiteral_strategy)
def test_jdtast_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=JDTAST_StringLiteral_strategy)
def test_jdtast_stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=JDTAST_MethodInvocation_strategy)
@settings(max_examples=50)
def test_jdtast_methodinvocation_instantiation(instance):
    assert isinstance(instance, JDTAST_MethodInvocation)

@given(instance=JDTAST_ArrayAccess_strategy)
@settings(max_examples=50)
def test_jdtast_arrayaccess_instantiation(instance):
    assert isinstance(instance, JDTAST_ArrayAccess)

@given(instance=JDTAST_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_jdtast_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_ParenthesizedExpression)

@given(instance=JDTAST_PrefixExpression_strategy)
@settings(max_examples=50)
def test_jdtast_prefixexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_PrefixExpression)



@given(instance=JDTAST_PrefixExpression_strategy)
def test_jdtast_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JDTAST_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_jdtast_classinstancecreation_instantiation(instance):
    assert isinstance(instance, JDTAST_ClassInstanceCreation)

@given(instance=JDTAST_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_jdtast_conditionalexpression_instantiation(instance):
    assert isinstance(instance, JDTAST_ConditionalExpression)

@given(instance=JDTAST_NumberLiteral_strategy)
@settings(max_examples=50)
def test_jdtast_numberliteral_instantiation(instance):
    assert isinstance(instance, JDTAST_NumberLiteral)



@given(instance=JDTAST_NumberLiteral_strategy)
def test_jdtast_numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=JDTAST_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_jdtast_characterliteral_instantiation(instance):
    assert isinstance(instance, JDTAST_CharacterLiteral)



@given(instance=JDTAST_CharacterLiteral_strategy)
def test_jdtast_characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original



@given(instance=JDTAST_CharacterLiteral_strategy)
def test_jdtast_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=JDTAST_LineComment_strategy)
@settings(max_examples=50)
def test_jdtast_linecomment_instantiation(instance):
    assert isinstance(instance, JDTAST_LineComment)

@given(instance=JDTAST_BlockComment_strategy)
@settings(max_examples=50)
def test_jdtast_blockcomment_instantiation(instance):
    assert isinstance(instance, JDTAST_BlockComment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JDTAST_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_enumdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_EnumDeclaration)

@given(instance=JDTAST_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_typedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_TypeDeclaration)



@given(instance=JDTAST_TypeDeclaration_strategy)
def test_jdtast_typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=JDTAST_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_AnnotationTypeDeclaration)

@given(instance=JDTAST_ArrayType_strategy)
@settings(max_examples=50)
def test_jdtast_arraytype_instantiation(instance):
    assert isinstance(instance, JDTAST_ArrayType)



@given(instance=JDTAST_ArrayType_strategy)
def test_jdtast_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=JDTAST_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_jdtast_arrayinitializer_instantiation(instance):
    assert isinstance(instance, JDTAST_ArrayInitializer)

@given(instance=JDTAST_ArrayCreation_strategy)
@settings(max_examples=50)
def test_jdtast_arraycreation_instantiation(instance):
    assert isinstance(instance, JDTAST_ArrayCreation)

@given(instance=JDTAST_VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_jdtast_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, JDTAST_VariableDeclarationFragment)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JDTAST_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_fielddeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_FieldDeclaration)

@given(instance=JDTAST_Initializer_strategy)
@settings(max_examples=50)
def test_jdtast_initializer_instantiation(instance):
    assert isinstance(instance, JDTAST_Initializer)

@given(instance=JDTAST_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_methoddeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_MethodDeclaration)



@given(instance=JDTAST_MethodDeclaration_strategy)
def test_jdtast_methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original



@given(instance=JDTAST_MethodDeclaration_strategy)
def test_jdtast_methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original



@given(instance=JDTAST_MethodDeclaration_strategy)
def test_jdtast_methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JDTAST_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_AnnotationTypeMemberDeclaration)

@given(instance=JDTAST_EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_EnumConstantDeclaration)

@given(instance=JDTAST_SimpleName_strategy)
@settings(max_examples=50)
def test_jdtast_simplename_instantiation(instance):
    assert isinstance(instance, JDTAST_SimpleName)



@given(instance=JDTAST_SimpleName_strategy)
def test_jdtast_simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=JDTAST_SimpleName_strategy)
def test_jdtast_simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=JDTAST_Annotation_strategy)
@settings(max_examples=50)
def test_jdtast_annotation_instantiation(instance):
    assert isinstance(instance, JDTAST_Annotation)

@given(instance=JDTAST_Name_strategy)
@settings(max_examples=50)
def test_jdtast_name_instantiation(instance):
    assert isinstance(instance, JDTAST_Name)



@given(instance=JDTAST_Name_strategy)
def test_jdtast_name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=JDTAST_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_AbstractTypeDeclaration)



@given(instance=JDTAST_AbstractTypeDeclaration_strategy)
def test_jdtast_abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original



@given(instance=JDTAST_AbstractTypeDeclaration_strategy)
def test_jdtast_abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original



@given(instance=JDTAST_AbstractTypeDeclaration_strategy)
def test_jdtast_abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original

@given(instance=JDTAST_SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_SingleVariableDeclaration)



@given(instance=JDTAST_SingleVariableDeclaration_strategy)
def test_jdtast_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JDTAST_Block_strategy)
@settings(max_examples=50)
def test_jdtast_block_instantiation(instance):
    assert isinstance(instance, JDTAST_Block)

@given(instance=JDTAST_ASTNode_strategy)
@settings(max_examples=50)
def test_jdtast_astnode_instantiation(instance):
    assert isinstance(instance, JDTAST_ASTNode)

@given(instance=JDTAST_AST_strategy)
@settings(max_examples=50)
def test_jdtast_ast_instantiation(instance):
    assert isinstance(instance, JDTAST_AST)

@given(instance=JDTAST_Parameter_strategy)
@settings(max_examples=50)
def test_jdtast_parameter_instantiation(instance):
    assert isinstance(instance, JDTAST_Parameter)



@given(instance=JDTAST_Parameter_strategy)
def test_jdtast_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JDTAST_Parameter_strategy)
def test_jdtast_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JDTAST_Javadoc_strategy)
@settings(max_examples=50)
def test_jdtast_javadoc_instantiation(instance):
    assert isinstance(instance, JDTAST_Javadoc)

@given(instance=JDTAST_ExtendedModifier_strategy)
@settings(max_examples=50)
def test_jdtast_extendedmodifier_instantiation(instance):
    assert isinstance(instance, JDTAST_ExtendedModifier)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JDTAST_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_bodydeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_BodyDeclaration)

@given(instance=JDTAST_CatchClause_strategy)
@settings(max_examples=50)
def test_jdtast_catchclause_instantiation(instance):
    assert isinstance(instance, JDTAST_CatchClause)

@given(instance=JDTAST_Modifier_strategy)
@settings(max_examples=50)
def test_jdtast_modifier_instantiation(instance):
    assert isinstance(instance, JDTAST_Modifier)



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=JDTAST_Modifier_strategy)
def test_jdtast_modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=JDTAST_TextElement_strategy)
@settings(max_examples=50)
def test_jdtast_textelement_instantiation(instance):
    assert isinstance(instance, JDTAST_TextElement)



@given(instance=JDTAST_TextElement_strategy)
def test_jdtast_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=JDTAST_Comment_strategy)
@settings(max_examples=50)
def test_jdtast_comment_instantiation(instance):
    assert isinstance(instance, JDTAST_Comment)

@given(instance=JDTAST_MethodRefParameter_strategy)
@settings(max_examples=50)
def test_jdtast_methodrefparameter_instantiation(instance):
    assert isinstance(instance, JDTAST_MethodRefParameter)



@given(instance=JDTAST_MethodRefParameter_strategy)
def test_jdtast_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JDTAST_TypeParameter_strategy)
@settings(max_examples=50)
def test_jdtast_typeparameter_instantiation(instance):
    assert isinstance(instance, JDTAST_TypeParameter)

@given(instance=JDTAST_Expression_strategy)
@settings(max_examples=50)
def test_jdtast_expression_instantiation(instance):
    assert isinstance(instance, JDTAST_Expression)



@given(instance=JDTAST_Expression_strategy)
def test_jdtast_expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original



@given(instance=JDTAST_Expression_strategy)
def test_jdtast_expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original

@given(instance=JDTAST_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_importdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_ImportDeclaration)



@given(instance=JDTAST_ImportDeclaration_strategy)
def test_jdtast_importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original



@given(instance=JDTAST_ImportDeclaration_strategy)
def test_jdtast_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=JDTAST_MemberRef_strategy)
@settings(max_examples=50)
def test_jdtast_memberref_instantiation(instance):
    assert isinstance(instance, JDTAST_MemberRef)

@given(instance=JDTAST_Type_strategy)
@settings(max_examples=50)
def test_jdtast_type_instantiation(instance):
    assert isinstance(instance, JDTAST_Type)

@given(instance=JDTAST_MethodRef_strategy)
@settings(max_examples=50)
def test_jdtast_methodref_instantiation(instance):
    assert isinstance(instance, JDTAST_MethodRef)

@given(instance=JDTAST_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_variabledeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_VariableDeclaration)



@given(instance=JDTAST_VariableDeclaration_strategy)
def test_jdtast_variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=JDTAST_Statement_strategy)
@settings(max_examples=50)
def test_jdtast_statement_instantiation(instance):
    assert isinstance(instance, JDTAST_Statement)

@given(instance=JDTAST_MemberValuePair_strategy)
@settings(max_examples=50)
def test_jdtast_membervaluepair_instantiation(instance):
    assert isinstance(instance, JDTAST_MemberValuePair)

@given(instance=JDTAST_TagElement_strategy)
@settings(max_examples=50)
def test_jdtast_tagelement_instantiation(instance):
    assert isinstance(instance, JDTAST_TagElement)



@given(instance=JDTAST_TagElement_strategy)
def test_jdtast_tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original



@given(instance=JDTAST_TagElement_strategy)
def test_jdtast_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=JDTAST_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_packagedeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_PackageDeclaration)

@given(instance=JDTAST_AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_AnonymousClassDeclaration)

@given(instance=IMember_strategy)
@settings(max_examples=50)
def test_imember_instantiation(instance):
    assert isinstance(instance, IMember)

@given(instance=JDTAST_IMethod_strategy)
@settings(max_examples=50)
def test_jdtast_imethod_instantiation(instance):
    assert isinstance(instance, JDTAST_IMethod)



@given(instance=JDTAST_IMethod_strategy)
def test_jdtast_imethod_exceptionTypes_setter(instance):
    original = instance.exceptionTypes
    instance.exceptionTypes = original
    assert instance.exceptionTypes == original



@given(instance=JDTAST_IMethod_strategy)
def test_jdtast_imethod_isMainMethod_setter(instance):
    original = instance.isMainMethod
    instance.isMainMethod = original
    assert instance.isMainMethod == original



@given(instance=JDTAST_IMethod_strategy)
def test_jdtast_imethod_isConstructor_setter(instance):
    original = instance.isConstructor
    instance.isConstructor = original
    assert instance.isConstructor == original



@given(instance=JDTAST_IMethod_strategy)
def test_jdtast_imethod_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=JDTAST_IInitializer_strategy)
@settings(max_examples=50)
def test_jdtast_iinitializer_instantiation(instance):
    assert isinstance(instance, JDTAST_IInitializer)

@given(instance=JDTAST_IField_strategy)
@settings(max_examples=50)
def test_jdtast_ifield_instantiation(instance):
    assert isinstance(instance, JDTAST_IField)



@given(instance=JDTAST_IField_strategy)
def test_jdtast_ifield_isEnumConstant_setter(instance):
    original = instance.isEnumConstant
    instance.isEnumConstant = original
    assert instance.isEnumConstant == original



@given(instance=JDTAST_IField_strategy)
def test_jdtast_ifield_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original



@given(instance=JDTAST_IField_strategy)
def test_jdtast_ifield_isTransient_setter(instance):
    original = instance.isTransient
    instance.isTransient = original
    assert instance.isTransient == original



@given(instance=JDTAST_IField_strategy)
def test_jdtast_ifield_typeSignature_setter(instance):
    original = instance.typeSignature
    instance.typeSignature = original
    assert instance.typeSignature == original



@given(instance=JDTAST_IField_strategy)
def test_jdtast_ifield_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=JDTAST_ISourceRange_strategy)
@settings(max_examples=50)
def test_jdtast_isourcerange_instantiation(instance):
    assert isinstance(instance, JDTAST_ISourceRange)



@given(instance=JDTAST_ISourceRange_strategy)
def test_jdtast_isourcerange_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=JDTAST_ISourceRange_strategy)
def test_jdtast_isourcerange_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=JDTAST_ISourceReference_strategy)
@settings(max_examples=50)
def test_jdtast_isourcereference_instantiation(instance):
    assert isinstance(instance, JDTAST_ISourceReference)



@given(instance=JDTAST_ISourceReference_strategy)
def test_jdtast_isourcereference_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=JDTAST_CompilationUnit_strategy)
@settings(max_examples=50)
def test_jdtast_compilationunit_instantiation(instance):
    assert isinstance(instance, JDTAST_CompilationUnit)

@given(instance=IPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_ipackagefragmentroot_instantiation(instance):
    assert isinstance(instance, IPackageFragmentRoot)

@given(instance=JDTAST_SourcePackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_jdtast_sourcepackagefragmentroot_instantiation(instance):
    assert isinstance(instance, JDTAST_SourcePackageFragmentRoot)

@given(instance=JDTAST_BinaryPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_jdtast_binarypackagefragmentroot_instantiation(instance):
    assert isinstance(instance, JDTAST_BinaryPackageFragmentRoot)

@given(instance=IJavaElement_strategy)
@settings(max_examples=50)
def test_ijavaelement_instantiation(instance):
    assert isinstance(instance, IJavaElement)

@given(instance=PhysicalElement_strategy)
@settings(max_examples=50)
def test_physicalelement_instantiation(instance):
    assert isinstance(instance, PhysicalElement)

@given(instance=JDTAST_IJavaProject_strategy)
@settings(max_examples=50)
def test_jdtast_ijavaproject_instantiation(instance):
    assert isinstance(instance, JDTAST_IJavaProject)

@given(instance=JDTAST_IPackageFragment_strategy)
@settings(max_examples=50)
def test_jdtast_ipackagefragment_instantiation(instance):
    assert isinstance(instance, JDTAST_IPackageFragment)



@given(instance=JDTAST_IPackageFragment_strategy)
def test_jdtast_ipackagefragment_isDefaultPackage_setter(instance):
    original = instance.isDefaultPackage
    instance.isDefaultPackage = original
    assert instance.isDefaultPackage == original

@given(instance=JDTAST_IPackageFragmentRoot_strategy)
@settings(max_examples=50)
def test_jdtast_ipackagefragmentroot_instantiation(instance):
    assert isinstance(instance, JDTAST_IPackageFragmentRoot)

@given(instance=JDTAST_IJavaModel_strategy)
@settings(max_examples=50)
def test_jdtast_ijavamodel_instantiation(instance):
    assert isinstance(instance, JDTAST_IJavaModel)

@given(instance=JDTAST_PhysicalElement_strategy)
@settings(max_examples=50)
def test_jdtast_physicalelement_instantiation(instance):
    assert isinstance(instance, JDTAST_PhysicalElement)



@given(instance=JDTAST_PhysicalElement_strategy)
def test_jdtast_physicalelement_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=JDTAST_PhysicalElement_strategy)
def test_jdtast_physicalelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=JDTAST_IJavaElement_strategy)
@settings(max_examples=50)
def test_jdtast_ijavaelement_instantiation(instance):
    assert isinstance(instance, JDTAST_IJavaElement)



@given(instance=JDTAST_IJavaElement_strategy)
def test_jdtast_ijavaelement_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=JDTAST_IType_strategy)
@settings(max_examples=50)
def test_jdtast_itype_instantiation(instance):
    assert isinstance(instance, JDTAST_IType)



@given(instance=JDTAST_IType_strategy)
def test_jdtast_itype_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original



@given(instance=JDTAST_IType_strategy)
def test_jdtast_itype_fullyQualifiedParametrizedName_setter(instance):
    original = instance.fullyQualifiedParametrizedName
    instance.fullyQualifiedParametrizedName = original
    assert instance.fullyQualifiedParametrizedName == original

@given(instance=ITypeRoot_strategy)
@settings(max_examples=50)
def test_ityperoot_instantiation(instance):
    assert isinstance(instance, ITypeRoot)

@given(instance=ISourceReference_strategy)
@settings(max_examples=50)
def test_isourcereference_instantiation(instance):
    assert isinstance(instance, ISourceReference)

@given(instance=JDTAST_IImportDeclaration_strategy)
@settings(max_examples=50)
def test_jdtast_iimportdeclaration_instantiation(instance):
    assert isinstance(instance, JDTAST_IImportDeclaration)



@given(instance=JDTAST_IImportDeclaration_strategy)
def test_jdtast_iimportdeclaration_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=JDTAST_IImportDeclaration_strategy)
def test_jdtast_iimportdeclaration_isOnDemand_setter(instance):
    original = instance.isOnDemand
    instance.isOnDemand = original
    assert instance.isOnDemand == original

@given(instance=JDTAST_IMember_strategy)
@settings(max_examples=50)
def test_jdtast_imember_instantiation(instance):
    assert isinstance(instance, JDTAST_IMember)

@given(instance=JDTAST_ITypeParameter_strategy)
@settings(max_examples=50)
def test_jdtast_itypeparameter_instantiation(instance):
    assert isinstance(instance, JDTAST_ITypeParameter)



@given(instance=JDTAST_ITypeParameter_strategy)
def test_jdtast_itypeparameter_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=JDTAST_ITypeRoot_strategy)
@settings(max_examples=50)
def test_jdtast_ityperoot_instantiation(instance):
    assert isinstance(instance, JDTAST_ITypeRoot)

@given(instance=JDTAST_ICompilationUnit_strategy)
@settings(max_examples=50)
def test_jdtast_icompilationunit_instantiation(instance):
    assert isinstance(instance, JDTAST_ICompilationUnit)

@given(instance=JDTAST_IClassFile_strategy)
@settings(max_examples=50)
def test_jdtast_iclassfile_instantiation(instance):
    assert isinstance(instance, JDTAST_IClassFile)



@given(instance=JDTAST_IClassFile_strategy)
def test_jdtast_iclassfile_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original



@given(instance=JDTAST_IClassFile_strategy)
def test_jdtast_iclassfile_isClass_setter(instance):
    original = instance.isClass
    instance.isClass = original
    assert instance.isClass == original
