import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MemberValuePair,
    VariableDeclaration,
    JavaAbstractSyntax_VariableDeclarationFragment,
    JavaAbstractSyntax_SingleVariableDeclaration,
    CatchClause,
    Statement,
    JavaAbstractSyntax_WhileStatement,
    JavaAbstractSyntax_ForStatement,
    JavaAbstractSyntax_VariableDeclarationStatement,
    JavaAbstractSyntax_ContinueStatement,
    JavaAbstractSyntax_SwitchStatement,
    JavaAbstractSyntax_BreakStatement,
    JavaAbstractSyntax_DoStatement,
    JavaAbstractSyntax_ExpressionStatement,
    JavaAbstractSyntax_EmptyStatement,
    JavaAbstractSyntax_SuperConstructorInvocation,
    JavaAbstractSyntax_ReturnStatement,
    JavaAbstractSyntax_IfStatement,
    JavaAbstractSyntax_EnhancedForStatement,
    JavaAbstractSyntax_Block,
    JavaAbstractSyntax_LabeledStatement,
    JavaAbstractSyntax_TypeDeclarationStatement,
    JavaAbstractSyntax_SwitchCase,
    JavaAbstractSyntax_TryStatement,
    JavaAbstractSyntax_ConstructorInvocation,
    JavaAbstractSyntax_SynchronizedStatement,
    JavaAbstractSyntax_ThrowStatement,
    JavaAbstractSyntax_AssertStatement,
    TypeParameter,
    ArrayType,
    ArrayInitializer,
    TagElement,
    EnumConstantDeclaration,
    VariableDeclarationFragment,
    AnonymousClassDeclaration,
    JavaAbstractSyntax_ExtendedModifier,
    Type,
    JavaAbstractSyntax_ArrayType,
    JavaAbstractSyntax_QualifiedType,
    JavaAbstractSyntax_PrimitiveType,
    JavaAbstractSyntax_ParameterizedType,
    JavaAbstractSyntax_WildcardType,
    JavaAbstractSyntax_SimpleType,
    Annotation,
    JavaAbstractSyntax_NormalAnnotation,
    JavaAbstractSyntax_MarkerAnnotation,
    JavaAbstractSyntax_SingleMemberAnnotation,
    Comment,
    JavaAbstractSyntax_BlockComment,
    JavaAbstractSyntax_Javadoc,
    JavaAbstractSyntax_LineComment,
    SingleVariableDeclaration,
    MethodRefParameter,
    Expression,
    JavaAbstractSyntax_PostfixExpression,
    JavaAbstractSyntax_InstanceofExpression,
    JavaAbstractSyntax_BooleanLiteral,
    JavaAbstractSyntax_CharacterLiteral,
    JavaAbstractSyntax_NumberLiteral,
    JavaAbstractSyntax_SuperFieldAccess,
    JavaAbstractSyntax_InfixExpression,
    JavaAbstractSyntax_ArrayInitializer,
    JavaAbstractSyntax_CastExpression,
    JavaAbstractSyntax_MethodInvocation,
    JavaAbstractSyntax_FieldAccess,
    JavaAbstractSyntax_PrefixExpression,
    JavaAbstractSyntax_ClassInstanceCreation,
    JavaAbstractSyntax_Name,
    JavaAbstractSyntax_NullLiteral,
    JavaAbstractSyntax_ArrayCreation,
    JavaAbstractSyntax_StringLiteral,
    JavaAbstractSyntax_VariableDeclarationExpression,
    JavaAbstractSyntax_TypeLiteral,
    JavaAbstractSyntax_Assignment,
    JavaAbstractSyntax_ArrayAccess,
    JavaAbstractSyntax_ThisExpression,
    JavaAbstractSyntax_ConditionalExpression,
    JavaAbstractSyntax_SuperMethodInvocation,
    JavaAbstractSyntax_ParenthesizedExpression,
    SimpleName,
    Name,
    JavaAbstractSyntax_QualifiedName,
    JavaAbstractSyntax_SimpleName,
    AbstractTypeDeclaration,
    JavaAbstractSyntax_TypeDeclaration,
    JavaAbstractSyntax_AnnotationTypeDeclaration,
    JavaAbstractSyntax_EnumDeclaration,
    ImportDeclaration,
    PackageDeclaration,
    Block,
    Javadoc,
    ExtendedModifier,
    JavaAbstractSyntax_Annotation,
    BodyDeclaration,
    JavaAbstractSyntax_FieldDeclaration,
    JavaAbstractSyntax_EnumConstantDeclaration,
    JavaAbstractSyntax_MethodDeclaration,
    JavaAbstractSyntax_Initializer,
    JavaAbstractSyntax_AnnotationTypeMemberDeclaration,
    JavaAbstractSyntax_AbstractTypeDeclaration,
    JavaAbstractSyntax_ASTNode,
    ASTNode,
    JavaAbstractSyntax_TypeParameter,
    JavaAbstractSyntax_MethodRef,
    JavaAbstractSyntax_Modifier,
    JavaAbstractSyntax_Expression,
    JavaAbstractSyntax_TagElement,
    JavaAbstractSyntax_Type,
    JavaAbstractSyntax_VariableDeclaration,
    JavaAbstractSyntax_CatchClause,
    JavaAbstractSyntax_PackageDeclaration,
    JavaAbstractSyntax_Comment,
    JavaAbstractSyntax_AnonymousClassDeclaration,
    JavaAbstractSyntax_MemberRef,
    JavaAbstractSyntax_CompilationUnit,
    JavaAbstractSyntax_ImportDeclaration,
    JavaAbstractSyntax_MemberValuePair,
    JavaAbstractSyntax_MethodRefParameter,
    JavaAbstractSyntax_TextElement,
    JavaAbstractSyntax_Statement,
    JavaAbstractSyntax_BodyDeclaration,
    JavaAbstractSyntax_AST,
    PrefixExpresssionOperatorKind,
    InfixExpressionOperatorKind,
    PostfixExpresssionOperatorKind,
    AssignementOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(MemberValuePair)


def test_membervaluepair_constructor_exists():
    assert callable(MemberValuePair.__init__)


def test_membervaluepair_constructor_args():
    sig = inspect.signature(MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_VariableDeclarationFragment)


def test_javaabstractsyntax_variabledeclarationfragment_constructor_exists():
    assert callable(JavaAbstractSyntax_VariableDeclarationFragment.__init__)


def test_javaabstractsyntax_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SingleVariableDeclaration)


def test_javaabstractsyntax_singlevariabledeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_SingleVariableDeclaration.__init__)


def test_javaabstractsyntax_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_javaabstractsyntax_singlevariabledeclaration_has_varargs():
    assert hasattr(JavaAbstractSyntax_SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in JavaAbstractSyntax_SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_catchclause_is_not_abstract():
    assert not inspect.isabstract(CatchClause)


def test_catchclause_constructor_exists():
    assert callable(CatchClause.__init__)


def test_catchclause_constructor_args():
    sig = inspect.signature(CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_whilestatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_WhileStatement)


def test_javaabstractsyntax_whilestatement_constructor_exists():
    assert callable(JavaAbstractSyntax_WhileStatement.__init__)


def test_javaabstractsyntax_whilestatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_forstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ForStatement)


def test_javaabstractsyntax_forstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_ForStatement.__init__)


def test_javaabstractsyntax_forstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_VariableDeclarationStatement)


def test_javaabstractsyntax_variabledeclarationstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_VariableDeclarationStatement.__init__)


def test_javaabstractsyntax_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_continuestatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ContinueStatement)


def test_javaabstractsyntax_continuestatement_constructor_exists():
    assert callable(JavaAbstractSyntax_ContinueStatement.__init__)


def test_javaabstractsyntax_continuestatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_switchstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SwitchStatement)


def test_javaabstractsyntax_switchstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_SwitchStatement.__init__)


def test_javaabstractsyntax_switchstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_breakstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_BreakStatement)


def test_javaabstractsyntax_breakstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_BreakStatement.__init__)


def test_javaabstractsyntax_breakstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_dostatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_DoStatement)


def test_javaabstractsyntax_dostatement_constructor_exists():
    assert callable(JavaAbstractSyntax_DoStatement.__init__)


def test_javaabstractsyntax_dostatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ExpressionStatement)


def test_javaabstractsyntax_expressionstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_ExpressionStatement.__init__)


def test_javaabstractsyntax_expressionstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_emptystatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_EmptyStatement)


def test_javaabstractsyntax_emptystatement_constructor_exists():
    assert callable(JavaAbstractSyntax_EmptyStatement.__init__)


def test_javaabstractsyntax_emptystatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SuperConstructorInvocation)


def test_javaabstractsyntax_superconstructorinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax_SuperConstructorInvocation.__init__)


def test_javaabstractsyntax_superconstructorinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_returnstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ReturnStatement)


def test_javaabstractsyntax_returnstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_ReturnStatement.__init__)


def test_javaabstractsyntax_returnstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_ifstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_IfStatement)


def test_javaabstractsyntax_ifstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_IfStatement.__init__)


def test_javaabstractsyntax_ifstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_EnhancedForStatement)


def test_javaabstractsyntax_enhancedforstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_EnhancedForStatement.__init__)


def test_javaabstractsyntax_enhancedforstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_block_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Block)


def test_javaabstractsyntax_block_constructor_exists():
    assert callable(JavaAbstractSyntax_Block.__init__)


def test_javaabstractsyntax_block_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Block.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_LabeledStatement)


def test_javaabstractsyntax_labeledstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_LabeledStatement.__init__)


def test_javaabstractsyntax_labeledstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TypeDeclarationStatement)


def test_javaabstractsyntax_typedeclarationstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_TypeDeclarationStatement.__init__)


def test_javaabstractsyntax_typedeclarationstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_switchcase_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SwitchCase)


def test_javaabstractsyntax_switchcase_constructor_exists():
    assert callable(JavaAbstractSyntax_SwitchCase.__init__)


def test_javaabstractsyntax_switchcase_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_javaabstractsyntax_switchcase_has_default():
    assert hasattr(JavaAbstractSyntax_SwitchCase, "default")
    descriptor = None
    for klass in JavaAbstractSyntax_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_trystatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TryStatement)


def test_javaabstractsyntax_trystatement_constructor_exists():
    assert callable(JavaAbstractSyntax_TryStatement.__init__)


def test_javaabstractsyntax_trystatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ConstructorInvocation)


def test_javaabstractsyntax_constructorinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax_ConstructorInvocation.__init__)


def test_javaabstractsyntax_constructorinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SynchronizedStatement)


def test_javaabstractsyntax_synchronizedstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_SynchronizedStatement.__init__)


def test_javaabstractsyntax_synchronizedstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_throwstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ThrowStatement)


def test_javaabstractsyntax_throwstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_ThrowStatement.__init__)


def test_javaabstractsyntax_throwstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_assertstatement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_AssertStatement)


def test_javaabstractsyntax_assertstatement_constructor_exists():
    assert callable(JavaAbstractSyntax_AssertStatement.__init__)


def test_javaabstractsyntax_assertstatement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_typeparameter_is_not_abstract():
    assert not inspect.isabstract(TypeParameter)


def test_typeparameter_constructor_exists():
    assert callable(TypeParameter.__init__)


def test_typeparameter_constructor_args():
    sig = inspect.signature(TypeParameter.__init__)
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



def test_tagelement_is_not_abstract():
    assert not inspect.isabstract(TagElement)


def test_tagelement_constructor_exists():
    assert callable(TagElement.__init__)


def test_tagelement_constructor_args():
    sig = inspect.signature(TagElement.__init__)
    params = list(sig.parameters.keys())



def test_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumConstantDeclaration)


def test_enumconstantdeclaration_constructor_exists():
    assert callable(EnumConstantDeclaration.__init__)


def test_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(EnumConstantDeclaration.__init__)
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



def test_javaabstractsyntax_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ExtendedModifier)


def test_javaabstractsyntax_extendedmodifier_constructor_exists():
    assert callable(JavaAbstractSyntax_ExtendedModifier.__init__)


def test_javaabstractsyntax_extendedmodifier_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_arraytype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ArrayType)


def test_javaabstractsyntax_arraytype_constructor_exists():
    assert callable(JavaAbstractSyntax_ArrayType.__init__)


def test_javaabstractsyntax_arraytype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_javaabstractsyntax_arraytype_has_dimensions():
    assert hasattr(JavaAbstractSyntax_ArrayType, "dimensions")
    descriptor = None
    for klass in JavaAbstractSyntax_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_QualifiedType)


def test_javaabstractsyntax_qualifiedtype_constructor_exists():
    assert callable(JavaAbstractSyntax_QualifiedType.__init__)


def test_javaabstractsyntax_qualifiedtype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_primitivetype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_PrimitiveType)


def test_javaabstractsyntax_primitivetype_constructor_exists():
    assert callable(JavaAbstractSyntax_PrimitiveType.__init__)


def test_javaabstractsyntax_primitivetype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_javaabstractsyntax_primitivetype_has_code():
    assert hasattr(JavaAbstractSyntax_PrimitiveType, "code")
    descriptor = None
    for klass in JavaAbstractSyntax_PrimitiveType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ParameterizedType)


def test_javaabstractsyntax_parameterizedtype_constructor_exists():
    assert callable(JavaAbstractSyntax_ParameterizedType.__init__)


def test_javaabstractsyntax_parameterizedtype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_WildcardType)


def test_javaabstractsyntax_wildcardtype_constructor_exists():
    assert callable(JavaAbstractSyntax_WildcardType.__init__)


def test_javaabstractsyntax_wildcardtype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_javaabstractsyntax_wildcardtype_has_upperBound():
    assert hasattr(JavaAbstractSyntax_WildcardType, "upperBound")
    descriptor = None
    for klass in JavaAbstractSyntax_WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_simpletype_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SimpleType)


def test_javaabstractsyntax_simpletype_constructor_exists():
    assert callable(JavaAbstractSyntax_SimpleType.__init__)


def test_javaabstractsyntax_simpletype_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_normalannotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_NormalAnnotation)


def test_javaabstractsyntax_normalannotation_constructor_exists():
    assert callable(JavaAbstractSyntax_NormalAnnotation.__init__)


def test_javaabstractsyntax_normalannotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_markerannotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MarkerAnnotation)


def test_javaabstractsyntax_markerannotation_constructor_exists():
    assert callable(JavaAbstractSyntax_MarkerAnnotation.__init__)


def test_javaabstractsyntax_markerannotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SingleMemberAnnotation)


def test_javaabstractsyntax_singlememberannotation_constructor_exists():
    assert callable(JavaAbstractSyntax_SingleMemberAnnotation.__init__)


def test_javaabstractsyntax_singlememberannotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_blockcomment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_BlockComment)


def test_javaabstractsyntax_blockcomment_constructor_exists():
    assert callable(JavaAbstractSyntax_BlockComment.__init__)


def test_javaabstractsyntax_blockcomment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_javadoc_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Javadoc)


def test_javaabstractsyntax_javadoc_constructor_exists():
    assert callable(JavaAbstractSyntax_Javadoc.__init__)


def test_javaabstractsyntax_javadoc_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_linecomment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_LineComment)


def test_javaabstractsyntax_linecomment_constructor_exists():
    assert callable(JavaAbstractSyntax_LineComment.__init__)


def test_javaabstractsyntax_linecomment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
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



def test_javaabstractsyntax_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_PostfixExpression)


def test_javaabstractsyntax_postfixexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_PostfixExpression.__init__)


def test_javaabstractsyntax_postfixexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax_postfixexpression_has_operator():
    assert hasattr(JavaAbstractSyntax_PostfixExpression, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_InstanceofExpression)


def test_javaabstractsyntax_instanceofexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_InstanceofExpression.__init__)


def test_javaabstractsyntax_instanceofexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_BooleanLiteral)


def test_javaabstractsyntax_booleanliteral_constructor_exists():
    assert callable(JavaAbstractSyntax_BooleanLiteral.__init__)


def test_javaabstractsyntax_booleanliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_javaabstractsyntax_booleanliteral_has_booleanValue():
    assert hasattr(JavaAbstractSyntax_BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in JavaAbstractSyntax_BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_characterliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_CharacterLiteral)


def test_javaabstractsyntax_characterliteral_constructor_exists():
    assert callable(JavaAbstractSyntax_CharacterLiteral.__init__)


def test_javaabstractsyntax_characterliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "charValue" in params, "Missing parameter 'charValue'"

def test_javaabstractsyntax_characterliteral_has_escapedValue():
    assert hasattr(JavaAbstractSyntax_CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in JavaAbstractSyntax_CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_characterliteral_has_charValue():
    assert hasattr(JavaAbstractSyntax_CharacterLiteral, "charValue")
    descriptor = None
    for klass in JavaAbstractSyntax_CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_numberliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_NumberLiteral)


def test_javaabstractsyntax_numberliteral_constructor_exists():
    assert callable(JavaAbstractSyntax_NumberLiteral.__init__)


def test_javaabstractsyntax_numberliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_javaabstractsyntax_numberliteral_has_token():
    assert hasattr(JavaAbstractSyntax_NumberLiteral, "token")
    descriptor = None
    for klass in JavaAbstractSyntax_NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SuperFieldAccess)


def test_javaabstractsyntax_superfieldaccess_constructor_exists():
    assert callable(JavaAbstractSyntax_SuperFieldAccess.__init__)


def test_javaabstractsyntax_superfieldaccess_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_infixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_InfixExpression)


def test_javaabstractsyntax_infixexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_InfixExpression.__init__)


def test_javaabstractsyntax_infixexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax_infixexpression_has_operator():
    assert hasattr(JavaAbstractSyntax_InfixExpression, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ArrayInitializer)


def test_javaabstractsyntax_arrayinitializer_constructor_exists():
    assert callable(JavaAbstractSyntax_ArrayInitializer.__init__)


def test_javaabstractsyntax_arrayinitializer_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_castexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_CastExpression)


def test_javaabstractsyntax_castexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_CastExpression.__init__)


def test_javaabstractsyntax_castexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MethodInvocation)


def test_javaabstractsyntax_methodinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax_MethodInvocation.__init__)


def test_javaabstractsyntax_methodinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_FieldAccess)


def test_javaabstractsyntax_fieldaccess_constructor_exists():
    assert callable(JavaAbstractSyntax_FieldAccess.__init__)


def test_javaabstractsyntax_fieldaccess_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_PrefixExpression)


def test_javaabstractsyntax_prefixexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_PrefixExpression.__init__)


def test_javaabstractsyntax_prefixexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax_prefixexpression_has_operator():
    assert hasattr(JavaAbstractSyntax_PrefixExpression, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ClassInstanceCreation)


def test_javaabstractsyntax_classinstancecreation_constructor_exists():
    assert callable(JavaAbstractSyntax_ClassInstanceCreation.__init__)


def test_javaabstractsyntax_classinstancecreation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_name_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Name)


def test_javaabstractsyntax_name_constructor_exists():
    assert callable(JavaAbstractSyntax_Name.__init__)


def test_javaabstractsyntax_name_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_javaabstractsyntax_name_has_fullyQualifiedName():
    assert hasattr(JavaAbstractSyntax_Name, "fullyQualifiedName")
    descriptor = None
    for klass in JavaAbstractSyntax_Name.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_nullliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_NullLiteral)


def test_javaabstractsyntax_nullliteral_constructor_exists():
    assert callable(JavaAbstractSyntax_NullLiteral.__init__)


def test_javaabstractsyntax_nullliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_arraycreation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ArrayCreation)


def test_javaabstractsyntax_arraycreation_constructor_exists():
    assert callable(JavaAbstractSyntax_ArrayCreation.__init__)


def test_javaabstractsyntax_arraycreation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_stringliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_StringLiteral)


def test_javaabstractsyntax_stringliteral_constructor_exists():
    assert callable(JavaAbstractSyntax_StringLiteral.__init__)


def test_javaabstractsyntax_stringliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_javaabstractsyntax_stringliteral_has_escapedValue():
    assert hasattr(JavaAbstractSyntax_StringLiteral, "escapedValue")
    descriptor = None
    for klass in JavaAbstractSyntax_StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_stringliteral_has_literalValue():
    assert hasattr(JavaAbstractSyntax_StringLiteral, "literalValue")
    descriptor = None
    for klass in JavaAbstractSyntax_StringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_VariableDeclarationExpression)


def test_javaabstractsyntax_variabledeclarationexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_VariableDeclarationExpression.__init__)


def test_javaabstractsyntax_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_typeliteral_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TypeLiteral)


def test_javaabstractsyntax_typeliteral_constructor_exists():
    assert callable(JavaAbstractSyntax_TypeLiteral.__init__)


def test_javaabstractsyntax_typeliteral_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_assignment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Assignment)


def test_javaabstractsyntax_assignment_constructor_exists():
    assert callable(JavaAbstractSyntax_Assignment.__init__)


def test_javaabstractsyntax_assignment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javaabstractsyntax_assignment_has_operator():
    assert hasattr(JavaAbstractSyntax_Assignment, "operator")
    descriptor = None
    for klass in JavaAbstractSyntax_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ArrayAccess)


def test_javaabstractsyntax_arrayaccess_constructor_exists():
    assert callable(JavaAbstractSyntax_ArrayAccess.__init__)


def test_javaabstractsyntax_arrayaccess_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_thisexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ThisExpression)


def test_javaabstractsyntax_thisexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_ThisExpression.__init__)


def test_javaabstractsyntax_thisexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ConditionalExpression)


def test_javaabstractsyntax_conditionalexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_ConditionalExpression.__init__)


def test_javaabstractsyntax_conditionalexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SuperMethodInvocation)


def test_javaabstractsyntax_supermethodinvocation_constructor_exists():
    assert callable(JavaAbstractSyntax_SuperMethodInvocation.__init__)


def test_javaabstractsyntax_supermethodinvocation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ParenthesizedExpression)


def test_javaabstractsyntax_parenthesizedexpression_constructor_exists():
    assert callable(JavaAbstractSyntax_ParenthesizedExpression.__init__)


def test_javaabstractsyntax_parenthesizedexpression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ParenthesizedExpression.__init__)
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



def test_javaabstractsyntax_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_QualifiedName)


def test_javaabstractsyntax_qualifiedname_constructor_exists():
    assert callable(JavaAbstractSyntax_QualifiedName.__init__)


def test_javaabstractsyntax_qualifiedname_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_simplename_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_SimpleName)


def test_javaabstractsyntax_simplename_constructor_exists():
    assert callable(JavaAbstractSyntax_SimpleName.__init__)


def test_javaabstractsyntax_simplename_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_javaabstractsyntax_simplename_has_declaration():
    assert hasattr(JavaAbstractSyntax_SimpleName, "declaration")
    descriptor = None
    for klass in JavaAbstractSyntax_SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_simplename_has_identifier():
    assert hasattr(JavaAbstractSyntax_SimpleName, "identifier")
    descriptor = None
    for klass in JavaAbstractSyntax_SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TypeDeclaration)


def test_javaabstractsyntax_typedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_TypeDeclaration.__init__)


def test_javaabstractsyntax_typedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_javaabstractsyntax_typedeclaration_has_interface():
    assert hasattr(JavaAbstractSyntax_TypeDeclaration, "interface")
    descriptor = None
    for klass in JavaAbstractSyntax_TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_AnnotationTypeDeclaration)


def test_javaabstractsyntax_annotationtypedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_AnnotationTypeDeclaration.__init__)


def test_javaabstractsyntax_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_EnumDeclaration)


def test_javaabstractsyntax_enumdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_EnumDeclaration.__init__)


def test_javaabstractsyntax_enumdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_EnumDeclaration.__init__)
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



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
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



def test_javaabstractsyntax_annotation_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Annotation)


def test_javaabstractsyntax_annotation_constructor_exists():
    assert callable(JavaAbstractSyntax_Annotation.__init__)


def test_javaabstractsyntax_annotation_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_FieldDeclaration)


def test_javaabstractsyntax_fielddeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_FieldDeclaration.__init__)


def test_javaabstractsyntax_fielddeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_EnumConstantDeclaration)


def test_javaabstractsyntax_enumconstantdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_EnumConstantDeclaration.__init__)


def test_javaabstractsyntax_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MethodDeclaration)


def test_javaabstractsyntax_methoddeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_MethodDeclaration.__init__)


def test_javaabstractsyntax_methoddeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"

def test_javaabstractsyntax_methoddeclaration_has_extraDimensions():
    assert hasattr(JavaAbstractSyntax_MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in JavaAbstractSyntax_MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_methoddeclaration_has_varargs():
    assert hasattr(JavaAbstractSyntax_MethodDeclaration, "varargs")
    descriptor = None
    for klass in JavaAbstractSyntax_MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_methoddeclaration_has_constructor():
    assert hasattr(JavaAbstractSyntax_MethodDeclaration, "constructor")
    descriptor = None
    for klass in JavaAbstractSyntax_MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_initializer_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Initializer)


def test_javaabstractsyntax_initializer_constructor_exists():
    assert callable(JavaAbstractSyntax_Initializer.__init__)


def test_javaabstractsyntax_initializer_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_AnnotationTypeMemberDeclaration)


def test_javaabstractsyntax_annotationtypememberdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_AnnotationTypeMemberDeclaration.__init__)


def test_javaabstractsyntax_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_AbstractTypeDeclaration)


def test_javaabstractsyntax_abstracttypedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_AbstractTypeDeclaration.__init__)


def test_javaabstractsyntax_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"

def test_javaabstractsyntax_abstracttypedeclaration_has_memberTypeDeclaration():
    assert hasattr(JavaAbstractSyntax_AbstractTypeDeclaration, "memberTypeDeclaration")
    descriptor = None
    for klass in JavaAbstractSyntax_AbstractTypeDeclaration.__mro__:
        if "memberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["memberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_abstracttypedeclaration_has_packageMemberTypeDeclaration():
    assert hasattr(JavaAbstractSyntax_AbstractTypeDeclaration, "packageMemberTypeDeclaration")
    descriptor = None
    for klass in JavaAbstractSyntax_AbstractTypeDeclaration.__mro__:
        if "packageMemberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["packageMemberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_abstracttypedeclaration_has_localTypeDeclaration():
    assert hasattr(JavaAbstractSyntax_AbstractTypeDeclaration, "localTypeDeclaration")
    descriptor = None
    for klass in JavaAbstractSyntax_AbstractTypeDeclaration.__mro__:
        if "localTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["localTypeDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_astnode_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ASTNode)


def test_javaabstractsyntax_astnode_constructor_exists():
    assert callable(JavaAbstractSyntax_ASTNode.__init__)


def test_javaabstractsyntax_astnode_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_typeparameter_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TypeParameter)


def test_javaabstractsyntax_typeparameter_constructor_exists():
    assert callable(JavaAbstractSyntax_TypeParameter.__init__)


def test_javaabstractsyntax_typeparameter_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_methodref_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MethodRef)


def test_javaabstractsyntax_methodref_constructor_exists():
    assert callable(JavaAbstractSyntax_MethodRef.__init__)


def test_javaabstractsyntax_methodref_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_modifier_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Modifier)


def test_javaabstractsyntax_modifier_constructor_exists():
    assert callable(JavaAbstractSyntax_Modifier.__init__)


def test_javaabstractsyntax_modifier_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "public" in params, "Missing parameter 'public'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "private" in params, "Missing parameter 'private'"
    assert "native" in params, "Missing parameter 'native'"
    assert "final" in params, "Missing parameter 'final'"
    assert "none" in params, "Missing parameter 'none'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "static" in params, "Missing parameter 'static'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_javaabstractsyntax_modifier_has_protected():
    assert hasattr(JavaAbstractSyntax_Modifier, "protected")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_abstract():
    assert hasattr(JavaAbstractSyntax_Modifier, "abstract")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_transient():
    assert hasattr(JavaAbstractSyntax_Modifier, "transient")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_public():
    assert hasattr(JavaAbstractSyntax_Modifier, "public")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_strictfp():
    assert hasattr(JavaAbstractSyntax_Modifier, "strictfp")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_private():
    assert hasattr(JavaAbstractSyntax_Modifier, "private")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_native():
    assert hasattr(JavaAbstractSyntax_Modifier, "native")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_final():
    assert hasattr(JavaAbstractSyntax_Modifier, "final")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_none():
    assert hasattr(JavaAbstractSyntax_Modifier, "none")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_volatile():
    assert hasattr(JavaAbstractSyntax_Modifier, "volatile")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_static():
    assert hasattr(JavaAbstractSyntax_Modifier, "static")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_modifier_has_synchronized():
    assert hasattr(JavaAbstractSyntax_Modifier, "synchronized")
    descriptor = None
    for klass in JavaAbstractSyntax_Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_expression_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Expression)


def test_javaabstractsyntax_expression_constructor_exists():
    assert callable(JavaAbstractSyntax_Expression.__init__)


def test_javaabstractsyntax_expression_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"

def test_javaabstractsyntax_expression_has_resolveUnboxing():
    assert hasattr(JavaAbstractSyntax_Expression, "resolveUnboxing")
    descriptor = None
    for klass in JavaAbstractSyntax_Expression.__mro__:
        if "resolveUnboxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveUnboxing"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_expression_has_resolveBoxing():
    assert hasattr(JavaAbstractSyntax_Expression, "resolveBoxing")
    descriptor = None
    for klass in JavaAbstractSyntax_Expression.__mro__:
        if "resolveBoxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveBoxing"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_tagelement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TagElement)


def test_javaabstractsyntax_tagelement_constructor_exists():
    assert callable(JavaAbstractSyntax_TagElement.__init__)


def test_javaabstractsyntax_tagelement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "nested" in params, "Missing parameter 'nested'"

def test_javaabstractsyntax_tagelement_has_tagName():
    assert hasattr(JavaAbstractSyntax_TagElement, "tagName")
    descriptor = None
    for klass in JavaAbstractSyntax_TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_tagelement_has_nested():
    assert hasattr(JavaAbstractSyntax_TagElement, "nested")
    descriptor = None
    for klass in JavaAbstractSyntax_TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_type_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Type)


def test_javaabstractsyntax_type_constructor_exists():
    assert callable(JavaAbstractSyntax_Type.__init__)


def test_javaabstractsyntax_type_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Type.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_VariableDeclaration)


def test_javaabstractsyntax_variabledeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_VariableDeclaration.__init__)


def test_javaabstractsyntax_variabledeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_javaabstractsyntax_variabledeclaration_has_extraDimensions():
    assert hasattr(JavaAbstractSyntax_VariableDeclaration, "extraDimensions")
    descriptor = None
    for klass in JavaAbstractSyntax_VariableDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_catchclause_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_CatchClause)


def test_javaabstractsyntax_catchclause_constructor_exists():
    assert callable(JavaAbstractSyntax_CatchClause.__init__)


def test_javaabstractsyntax_catchclause_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_PackageDeclaration)


def test_javaabstractsyntax_packagedeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_PackageDeclaration.__init__)


def test_javaabstractsyntax_packagedeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_comment_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Comment)


def test_javaabstractsyntax_comment_constructor_exists():
    assert callable(JavaAbstractSyntax_Comment.__init__)


def test_javaabstractsyntax_comment_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Comment.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_AnonymousClassDeclaration)


def test_javaabstractsyntax_anonymousclassdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_AnonymousClassDeclaration.__init__)


def test_javaabstractsyntax_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_memberref_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MemberRef)


def test_javaabstractsyntax_memberref_constructor_exists():
    assert callable(JavaAbstractSyntax_MemberRef.__init__)


def test_javaabstractsyntax_memberref_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_compilationunit_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_CompilationUnit)


def test_javaabstractsyntax_compilationunit_constructor_exists():
    assert callable(JavaAbstractSyntax_CompilationUnit.__init__)


def test_javaabstractsyntax_compilationunit_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_ImportDeclaration)


def test_javaabstractsyntax_importdeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_ImportDeclaration.__init__)


def test_javaabstractsyntax_importdeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"

def test_javaabstractsyntax_importdeclaration_has_onDemand():
    assert hasattr(JavaAbstractSyntax_ImportDeclaration, "onDemand")
    descriptor = None
    for klass in JavaAbstractSyntax_ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)

def test_javaabstractsyntax_importdeclaration_has_static():
    assert hasattr(JavaAbstractSyntax_ImportDeclaration, "static")
    descriptor = None
    for klass in JavaAbstractSyntax_ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MemberValuePair)


def test_javaabstractsyntax_membervaluepair_constructor_exists():
    assert callable(JavaAbstractSyntax_MemberValuePair.__init__)


def test_javaabstractsyntax_membervaluepair_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_MethodRefParameter)


def test_javaabstractsyntax_methodrefparameter_constructor_exists():
    assert callable(JavaAbstractSyntax_MethodRefParameter.__init__)


def test_javaabstractsyntax_methodrefparameter_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_javaabstractsyntax_methodrefparameter_has_varargs():
    assert hasattr(JavaAbstractSyntax_MethodRefParameter, "varargs")
    descriptor = None
    for klass in JavaAbstractSyntax_MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_textelement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_TextElement)


def test_javaabstractsyntax_textelement_constructor_exists():
    assert callable(JavaAbstractSyntax_TextElement.__init__)


def test_javaabstractsyntax_textelement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_javaabstractsyntax_textelement_has_text():
    assert hasattr(JavaAbstractSyntax_TextElement, "text")
    descriptor = None
    for klass in JavaAbstractSyntax_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_javaabstractsyntax_statement_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_Statement)


def test_javaabstractsyntax_statement_constructor_exists():
    assert callable(JavaAbstractSyntax_Statement.__init__)


def test_javaabstractsyntax_statement_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_Statement.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_BodyDeclaration)


def test_javaabstractsyntax_bodydeclaration_constructor_exists():
    assert callable(JavaAbstractSyntax_BodyDeclaration.__init__)


def test_javaabstractsyntax_bodydeclaration_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javaabstractsyntax_ast_is_not_abstract():
    assert not inspect.isabstract(JavaAbstractSyntax_AST)


def test_javaabstractsyntax_ast_constructor_exists():
    assert callable(JavaAbstractSyntax_AST.__init__)


def test_javaabstractsyntax_ast_constructor_args():
    sig = inspect.signature(JavaAbstractSyntax_AST.__init__)
    params = list(sig.parameters.keys())

def test_prefixexpresssionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpresssionOperatorKind is not None

def test_prefixexpresssionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpresssionOperatorKind]
    expected_literals = [
        "NOT",
        "DECREMENT",
        "INCREMENT",
        "MINUS",
        "PLUS",
        "COMPLEMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpresssionOperatorKind"

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "LESS",
        "AND",
        "XOR",
        "OR",
        "PLUS",
        "TIMES",
        "RIGHT_SHIFT_SIGNED",
        "GREATER_EQUALS",
        "EQUALS",
        "CONDITIONAL_AND",
        "REMAINDER",
        "LESS_EQUALS",
        "LEFT_SHIFT",
        "DIVIDE",
        "GREATER",
        "CONDITIONAL_OR",
        "NOT_EQUALS",
        "RIGHT_SHIFT_UNSIGNED",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

def test_postfixexpresssionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpresssionOperatorKind is not None

def test_postfixexpresssionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpresssionOperatorKind]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpresssionOperatorKind"

def test_assignementoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignementOperatorKind is not None

def test_assignementoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignementOperatorKind]
    expected_literals = [
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "DIVIDE_ASSIGN",
        "LEFT_SHIFT_ASSIGN",
        "BIT_OR_ASSIGN",
        "MINUS_ASSIGN",
        "BIT_AND_ASSIGN",
        "PLUS_ASSIGN",
        "ASSIGN",
        "TIMES_ASSIGN",
        "BIT_XOR_ASSIGN",
        "REMAINDER_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignementOperatorKind"


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
MemberValuePair_strategy = st.builds(
    MemberValuePair,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
JavaAbstractSyntax_VariableDeclarationFragment_strategy = st.builds(
    JavaAbstractSyntax_VariableDeclarationFragment,
)
JavaAbstractSyntax_SingleVariableDeclaration_strategy = st.builds(
    JavaAbstractSyntax_SingleVariableDeclaration,
    varargs=
        safe_text
)
CatchClause_strategy = st.builds(
    CatchClause,
)
Statement_strategy = st.builds(
    Statement,
)
JavaAbstractSyntax_WhileStatement_strategy = st.builds(
    JavaAbstractSyntax_WhileStatement,
)
JavaAbstractSyntax_ForStatement_strategy = st.builds(
    JavaAbstractSyntax_ForStatement,
)
JavaAbstractSyntax_VariableDeclarationStatement_strategy = st.builds(
    JavaAbstractSyntax_VariableDeclarationStatement,
)
JavaAbstractSyntax_ContinueStatement_strategy = st.builds(
    JavaAbstractSyntax_ContinueStatement,
)
JavaAbstractSyntax_SwitchStatement_strategy = st.builds(
    JavaAbstractSyntax_SwitchStatement,
)
JavaAbstractSyntax_BreakStatement_strategy = st.builds(
    JavaAbstractSyntax_BreakStatement,
)
JavaAbstractSyntax_DoStatement_strategy = st.builds(
    JavaAbstractSyntax_DoStatement,
)
JavaAbstractSyntax_ExpressionStatement_strategy = st.builds(
    JavaAbstractSyntax_ExpressionStatement,
)
JavaAbstractSyntax_EmptyStatement_strategy = st.builds(
    JavaAbstractSyntax_EmptyStatement,
)
JavaAbstractSyntax_SuperConstructorInvocation_strategy = st.builds(
    JavaAbstractSyntax_SuperConstructorInvocation,
)
JavaAbstractSyntax_ReturnStatement_strategy = st.builds(
    JavaAbstractSyntax_ReturnStatement,
)
JavaAbstractSyntax_IfStatement_strategy = st.builds(
    JavaAbstractSyntax_IfStatement,
)
JavaAbstractSyntax_EnhancedForStatement_strategy = st.builds(
    JavaAbstractSyntax_EnhancedForStatement,
)
JavaAbstractSyntax_Block_strategy = st.builds(
    JavaAbstractSyntax_Block,
)
JavaAbstractSyntax_LabeledStatement_strategy = st.builds(
    JavaAbstractSyntax_LabeledStatement,
)
JavaAbstractSyntax_TypeDeclarationStatement_strategy = st.builds(
    JavaAbstractSyntax_TypeDeclarationStatement,
)
JavaAbstractSyntax_SwitchCase_strategy = st.builds(
    JavaAbstractSyntax_SwitchCase,
    default=
        safe_text
)
JavaAbstractSyntax_TryStatement_strategy = st.builds(
    JavaAbstractSyntax_TryStatement,
)
JavaAbstractSyntax_ConstructorInvocation_strategy = st.builds(
    JavaAbstractSyntax_ConstructorInvocation,
)
JavaAbstractSyntax_SynchronizedStatement_strategy = st.builds(
    JavaAbstractSyntax_SynchronizedStatement,
)
JavaAbstractSyntax_ThrowStatement_strategy = st.builds(
    JavaAbstractSyntax_ThrowStatement,
)
JavaAbstractSyntax_AssertStatement_strategy = st.builds(
    JavaAbstractSyntax_AssertStatement,
)
TypeParameter_strategy = st.builds(
    TypeParameter,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
TagElement_strategy = st.builds(
    TagElement,
)
EnumConstantDeclaration_strategy = st.builds(
    EnumConstantDeclaration,
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
AnonymousClassDeclaration_strategy = st.builds(
    AnonymousClassDeclaration,
)
JavaAbstractSyntax_ExtendedModifier_strategy = st.builds(
    JavaAbstractSyntax_ExtendedModifier,
)
Type_strategy = st.builds(
    Type,
)
JavaAbstractSyntax_ArrayType_strategy = st.builds(
    JavaAbstractSyntax_ArrayType,
    dimensions=
        safe_text
)
JavaAbstractSyntax_QualifiedType_strategy = st.builds(
    JavaAbstractSyntax_QualifiedType,
)
JavaAbstractSyntax_PrimitiveType_strategy = st.builds(
    JavaAbstractSyntax_PrimitiveType,
    code=
        safe_text
)
JavaAbstractSyntax_ParameterizedType_strategy = st.builds(
    JavaAbstractSyntax_ParameterizedType,
)
JavaAbstractSyntax_WildcardType_strategy = st.builds(
    JavaAbstractSyntax_WildcardType,
    upperBound=
        safe_text
)
JavaAbstractSyntax_SimpleType_strategy = st.builds(
    JavaAbstractSyntax_SimpleType,
)
Annotation_strategy = st.builds(
    Annotation,
)
JavaAbstractSyntax_NormalAnnotation_strategy = st.builds(
    JavaAbstractSyntax_NormalAnnotation,
)
JavaAbstractSyntax_MarkerAnnotation_strategy = st.builds(
    JavaAbstractSyntax_MarkerAnnotation,
)
JavaAbstractSyntax_SingleMemberAnnotation_strategy = st.builds(
    JavaAbstractSyntax_SingleMemberAnnotation,
)
Comment_strategy = st.builds(
    Comment,
)
JavaAbstractSyntax_BlockComment_strategy = st.builds(
    JavaAbstractSyntax_BlockComment,
)
JavaAbstractSyntax_Javadoc_strategy = st.builds(
    JavaAbstractSyntax_Javadoc,
)
JavaAbstractSyntax_LineComment_strategy = st.builds(
    JavaAbstractSyntax_LineComment,
)
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
)
MethodRefParameter_strategy = st.builds(
    MethodRefParameter,
)
Expression_strategy = st.builds(
    Expression,
)
JavaAbstractSyntax_PostfixExpression_strategy = st.builds(
    JavaAbstractSyntax_PostfixExpression,
    operator=
        safe_text
)
JavaAbstractSyntax_InstanceofExpression_strategy = st.builds(
    JavaAbstractSyntax_InstanceofExpression,
)
JavaAbstractSyntax_BooleanLiteral_strategy = st.builds(
    JavaAbstractSyntax_BooleanLiteral,
    booleanValue=
        safe_text
)
JavaAbstractSyntax_CharacterLiteral_strategy = st.builds(
    JavaAbstractSyntax_CharacterLiteral,
    escapedValue=
        safe_text,
    charValue=
        safe_text
)
JavaAbstractSyntax_NumberLiteral_strategy = st.builds(
    JavaAbstractSyntax_NumberLiteral,
    token=
        safe_text
)
JavaAbstractSyntax_SuperFieldAccess_strategy = st.builds(
    JavaAbstractSyntax_SuperFieldAccess,
)
JavaAbstractSyntax_InfixExpression_strategy = st.builds(
    JavaAbstractSyntax_InfixExpression,
    operator=
        safe_text
)
JavaAbstractSyntax_ArrayInitializer_strategy = st.builds(
    JavaAbstractSyntax_ArrayInitializer,
)
JavaAbstractSyntax_CastExpression_strategy = st.builds(
    JavaAbstractSyntax_CastExpression,
)
JavaAbstractSyntax_MethodInvocation_strategy = st.builds(
    JavaAbstractSyntax_MethodInvocation,
)
JavaAbstractSyntax_FieldAccess_strategy = st.builds(
    JavaAbstractSyntax_FieldAccess,
)
JavaAbstractSyntax_PrefixExpression_strategy = st.builds(
    JavaAbstractSyntax_PrefixExpression,
    operator=
        safe_text
)
JavaAbstractSyntax_ClassInstanceCreation_strategy = st.builds(
    JavaAbstractSyntax_ClassInstanceCreation,
)
JavaAbstractSyntax_Name_strategy = st.builds(
    JavaAbstractSyntax_Name,
    fullyQualifiedName=
        safe_text
)
JavaAbstractSyntax_NullLiteral_strategy = st.builds(
    JavaAbstractSyntax_NullLiteral,
)
JavaAbstractSyntax_ArrayCreation_strategy = st.builds(
    JavaAbstractSyntax_ArrayCreation,
)
JavaAbstractSyntax_StringLiteral_strategy = st.builds(
    JavaAbstractSyntax_StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
JavaAbstractSyntax_VariableDeclarationExpression_strategy = st.builds(
    JavaAbstractSyntax_VariableDeclarationExpression,
)
JavaAbstractSyntax_TypeLiteral_strategy = st.builds(
    JavaAbstractSyntax_TypeLiteral,
)
JavaAbstractSyntax_Assignment_strategy = st.builds(
    JavaAbstractSyntax_Assignment,
    operator=
        safe_text
)
JavaAbstractSyntax_ArrayAccess_strategy = st.builds(
    JavaAbstractSyntax_ArrayAccess,
)
JavaAbstractSyntax_ThisExpression_strategy = st.builds(
    JavaAbstractSyntax_ThisExpression,
)
JavaAbstractSyntax_ConditionalExpression_strategy = st.builds(
    JavaAbstractSyntax_ConditionalExpression,
)
JavaAbstractSyntax_SuperMethodInvocation_strategy = st.builds(
    JavaAbstractSyntax_SuperMethodInvocation,
)
JavaAbstractSyntax_ParenthesizedExpression_strategy = st.builds(
    JavaAbstractSyntax_ParenthesizedExpression,
)
SimpleName_strategy = st.builds(
    SimpleName,
)
Name_strategy = st.builds(
    Name,
)
JavaAbstractSyntax_QualifiedName_strategy = st.builds(
    JavaAbstractSyntax_QualifiedName,
)
JavaAbstractSyntax_SimpleName_strategy = st.builds(
    JavaAbstractSyntax_SimpleName,
    declaration=
        safe_text,
    identifier=
        safe_text
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JavaAbstractSyntax_TypeDeclaration_strategy = st.builds(
    JavaAbstractSyntax_TypeDeclaration,
    interface=
        safe_text
)
JavaAbstractSyntax_AnnotationTypeDeclaration_strategy = st.builds(
    JavaAbstractSyntax_AnnotationTypeDeclaration,
)
JavaAbstractSyntax_EnumDeclaration_strategy = st.builds(
    JavaAbstractSyntax_EnumDeclaration,
)
ImportDeclaration_strategy = st.builds(
    ImportDeclaration,
)
PackageDeclaration_strategy = st.builds(
    PackageDeclaration,
)
Block_strategy = st.builds(
    Block,
)
Javadoc_strategy = st.builds(
    Javadoc,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
JavaAbstractSyntax_Annotation_strategy = st.builds(
    JavaAbstractSyntax_Annotation,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JavaAbstractSyntax_FieldDeclaration_strategy = st.builds(
    JavaAbstractSyntax_FieldDeclaration,
)
JavaAbstractSyntax_EnumConstantDeclaration_strategy = st.builds(
    JavaAbstractSyntax_EnumConstantDeclaration,
)
JavaAbstractSyntax_MethodDeclaration_strategy = st.builds(
    JavaAbstractSyntax_MethodDeclaration,
    extraDimensions=
        safe_text,
    varargs=
        safe_text,
    constructor=
        safe_text
)
JavaAbstractSyntax_Initializer_strategy = st.builds(
    JavaAbstractSyntax_Initializer,
)
JavaAbstractSyntax_AnnotationTypeMemberDeclaration_strategy = st.builds(
    JavaAbstractSyntax_AnnotationTypeMemberDeclaration,
)
JavaAbstractSyntax_AbstractTypeDeclaration_strategy = st.builds(
    JavaAbstractSyntax_AbstractTypeDeclaration,
    memberTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text,
    localTypeDeclaration=
        safe_text
)
JavaAbstractSyntax_ASTNode_strategy = st.builds(
    JavaAbstractSyntax_ASTNode,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JavaAbstractSyntax_TypeParameter_strategy = st.builds(
    JavaAbstractSyntax_TypeParameter,
)
JavaAbstractSyntax_MethodRef_strategy = st.builds(
    JavaAbstractSyntax_MethodRef,
)
JavaAbstractSyntax_Modifier_strategy = st.builds(
    JavaAbstractSyntax_Modifier,
    protected=
        safe_text,
    abstract=
        safe_text,
    transient=
        safe_text,
    public=
        safe_text,
    strictfp=
        safe_text,
    private=
        safe_text,
    native=
        safe_text,
    final=
        safe_text,
    none=
        safe_text,
    volatile=
        safe_text,
    static=
        safe_text,
    synchronized=
        safe_text
)
JavaAbstractSyntax_Expression_strategy = st.builds(
    JavaAbstractSyntax_Expression,
    resolveUnboxing=
        safe_text,
    resolveBoxing=
        safe_text
)
JavaAbstractSyntax_TagElement_strategy = st.builds(
    JavaAbstractSyntax_TagElement,
    tagName=
        safe_text,
    nested=
        safe_text
)
JavaAbstractSyntax_Type_strategy = st.builds(
    JavaAbstractSyntax_Type,
)
JavaAbstractSyntax_VariableDeclaration_strategy = st.builds(
    JavaAbstractSyntax_VariableDeclaration,
    extraDimensions=
        safe_text
)
JavaAbstractSyntax_CatchClause_strategy = st.builds(
    JavaAbstractSyntax_CatchClause,
)
JavaAbstractSyntax_PackageDeclaration_strategy = st.builds(
    JavaAbstractSyntax_PackageDeclaration,
)
JavaAbstractSyntax_Comment_strategy = st.builds(
    JavaAbstractSyntax_Comment,
)
JavaAbstractSyntax_AnonymousClassDeclaration_strategy = st.builds(
    JavaAbstractSyntax_AnonymousClassDeclaration,
)
JavaAbstractSyntax_MemberRef_strategy = st.builds(
    JavaAbstractSyntax_MemberRef,
)
JavaAbstractSyntax_CompilationUnit_strategy = st.builds(
    JavaAbstractSyntax_CompilationUnit,
)
JavaAbstractSyntax_ImportDeclaration_strategy = st.builds(
    JavaAbstractSyntax_ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
JavaAbstractSyntax_MemberValuePair_strategy = st.builds(
    JavaAbstractSyntax_MemberValuePair,
)
JavaAbstractSyntax_MethodRefParameter_strategy = st.builds(
    JavaAbstractSyntax_MethodRefParameter,
    varargs=
        safe_text
)
JavaAbstractSyntax_TextElement_strategy = st.builds(
    JavaAbstractSyntax_TextElement,
    text=
        safe_text
)
JavaAbstractSyntax_Statement_strategy = st.builds(
    JavaAbstractSyntax_Statement,
)
JavaAbstractSyntax_BodyDeclaration_strategy = st.builds(
    JavaAbstractSyntax_BodyDeclaration,
)
JavaAbstractSyntax_AST_strategy = st.builds(
    JavaAbstractSyntax_AST,
)

@given(instance=MemberValuePair_strategy)
@settings(max_examples=50)
def test_membervaluepair_instantiation(instance):
    assert isinstance(instance, MemberValuePair)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=JavaAbstractSyntax_VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_VariableDeclarationFragment)

@given(instance=JavaAbstractSyntax_SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SingleVariableDeclaration)



@given(instance=JavaAbstractSyntax_SingleVariableDeclaration_strategy)
def test_javaabstractsyntax_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=CatchClause_strategy)
@settings(max_examples=50)
def test_catchclause_instantiation(instance):
    assert isinstance(instance, CatchClause)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=JavaAbstractSyntax_WhileStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_whilestatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_WhileStatement)

@given(instance=JavaAbstractSyntax_ForStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_forstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ForStatement)

@given(instance=JavaAbstractSyntax_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_VariableDeclarationStatement)

@given(instance=JavaAbstractSyntax_ContinueStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_continuestatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ContinueStatement)

@given(instance=JavaAbstractSyntax_SwitchStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_switchstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SwitchStatement)

@given(instance=JavaAbstractSyntax_BreakStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_breakstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_BreakStatement)

@given(instance=JavaAbstractSyntax_DoStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_dostatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_DoStatement)

@given(instance=JavaAbstractSyntax_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_expressionstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ExpressionStatement)

@given(instance=JavaAbstractSyntax_EmptyStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_emptystatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_EmptyStatement)

@given(instance=JavaAbstractSyntax_SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SuperConstructorInvocation)

@given(instance=JavaAbstractSyntax_ReturnStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_returnstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ReturnStatement)

@given(instance=JavaAbstractSyntax_IfStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_ifstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_IfStatement)

@given(instance=JavaAbstractSyntax_EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_enhancedforstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_EnhancedForStatement)

@given(instance=JavaAbstractSyntax_Block_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_block_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Block)

@given(instance=JavaAbstractSyntax_LabeledStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_labeledstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_LabeledStatement)

@given(instance=JavaAbstractSyntax_TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TypeDeclarationStatement)

@given(instance=JavaAbstractSyntax_SwitchCase_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_switchcase_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SwitchCase)



@given(instance=JavaAbstractSyntax_SwitchCase_strategy)
def test_javaabstractsyntax_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=JavaAbstractSyntax_TryStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_trystatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TryStatement)

@given(instance=JavaAbstractSyntax_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_constructorinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ConstructorInvocation)

@given(instance=JavaAbstractSyntax_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SynchronizedStatement)

@given(instance=JavaAbstractSyntax_ThrowStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_throwstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ThrowStatement)

@given(instance=JavaAbstractSyntax_AssertStatement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_assertstatement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_AssertStatement)

@given(instance=TypeParameter_strategy)
@settings(max_examples=50)
def test_typeparameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=ArrayInitializer_strategy)
@settings(max_examples=50)
def test_arrayinitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)

@given(instance=TagElement_strategy)
@settings(max_examples=50)
def test_tagelement_instantiation(instance):
    assert isinstance(instance, TagElement)

@given(instance=EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, EnumConstantDeclaration)

@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)

@given(instance=AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, AnonymousClassDeclaration)

@given(instance=JavaAbstractSyntax_ExtendedModifier_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_extendedmodifier_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ExtendedModifier)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JavaAbstractSyntax_ArrayType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_arraytype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ArrayType)



@given(instance=JavaAbstractSyntax_ArrayType_strategy)
def test_javaabstractsyntax_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=JavaAbstractSyntax_QualifiedType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_qualifiedtype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_QualifiedType)

@given(instance=JavaAbstractSyntax_PrimitiveType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_primitivetype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_PrimitiveType)



@given(instance=JavaAbstractSyntax_PrimitiveType_strategy)
def test_javaabstractsyntax_primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=JavaAbstractSyntax_ParameterizedType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_parameterizedtype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ParameterizedType)

@given(instance=JavaAbstractSyntax_WildcardType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_wildcardtype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_WildcardType)



@given(instance=JavaAbstractSyntax_WildcardType_strategy)
def test_javaabstractsyntax_wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=JavaAbstractSyntax_SimpleType_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_simpletype_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SimpleType)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=JavaAbstractSyntax_NormalAnnotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_normalannotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_NormalAnnotation)

@given(instance=JavaAbstractSyntax_MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_markerannotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MarkerAnnotation)

@given(instance=JavaAbstractSyntax_SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_singlememberannotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SingleMemberAnnotation)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=JavaAbstractSyntax_BlockComment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_blockcomment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_BlockComment)

@given(instance=JavaAbstractSyntax_Javadoc_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_javadoc_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Javadoc)

@given(instance=JavaAbstractSyntax_LineComment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_linecomment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_LineComment)

@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)

@given(instance=MethodRefParameter_strategy)
@settings(max_examples=50)
def test_methodrefparameter_instantiation(instance):
    assert isinstance(instance, MethodRefParameter)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JavaAbstractSyntax_PostfixExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_postfixexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_PostfixExpression)



@given(instance=JavaAbstractSyntax_PostfixExpression_strategy)
def test_javaabstractsyntax_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax_InstanceofExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_instanceofexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_InstanceofExpression)

@given(instance=JavaAbstractSyntax_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_booleanliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_BooleanLiteral)



@given(instance=JavaAbstractSyntax_BooleanLiteral_strategy)
def test_javaabstractsyntax_booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=JavaAbstractSyntax_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_characterliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_CharacterLiteral)



@given(instance=JavaAbstractSyntax_CharacterLiteral_strategy)
def test_javaabstractsyntax_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=JavaAbstractSyntax_CharacterLiteral_strategy)
def test_javaabstractsyntax_characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=JavaAbstractSyntax_NumberLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_numberliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_NumberLiteral)



@given(instance=JavaAbstractSyntax_NumberLiteral_strategy)
def test_javaabstractsyntax_numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=JavaAbstractSyntax_SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_superfieldaccess_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SuperFieldAccess)

@given(instance=JavaAbstractSyntax_InfixExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_infixexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_InfixExpression)



@given(instance=JavaAbstractSyntax_InfixExpression_strategy)
def test_javaabstractsyntax_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_arrayinitializer_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ArrayInitializer)

@given(instance=JavaAbstractSyntax_CastExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_castexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_CastExpression)

@given(instance=JavaAbstractSyntax_MethodInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_methodinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MethodInvocation)

@given(instance=JavaAbstractSyntax_FieldAccess_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_fieldaccess_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_FieldAccess)

@given(instance=JavaAbstractSyntax_PrefixExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_prefixexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_PrefixExpression)



@given(instance=JavaAbstractSyntax_PrefixExpression_strategy)
def test_javaabstractsyntax_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_classinstancecreation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ClassInstanceCreation)

@given(instance=JavaAbstractSyntax_Name_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_name_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Name)



@given(instance=JavaAbstractSyntax_Name_strategy)
def test_javaabstractsyntax_name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=JavaAbstractSyntax_NullLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_nullliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_NullLiteral)

@given(instance=JavaAbstractSyntax_ArrayCreation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_arraycreation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ArrayCreation)

@given(instance=JavaAbstractSyntax_StringLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_stringliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_StringLiteral)



@given(instance=JavaAbstractSyntax_StringLiteral_strategy)
def test_javaabstractsyntax_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=JavaAbstractSyntax_StringLiteral_strategy)
def test_javaabstractsyntax_stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=JavaAbstractSyntax_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_VariableDeclarationExpression)

@given(instance=JavaAbstractSyntax_TypeLiteral_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_typeliteral_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TypeLiteral)

@given(instance=JavaAbstractSyntax_Assignment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_assignment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Assignment)



@given(instance=JavaAbstractSyntax_Assignment_strategy)
def test_javaabstractsyntax_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaAbstractSyntax_ArrayAccess_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_arrayaccess_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ArrayAccess)

@given(instance=JavaAbstractSyntax_ThisExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_thisexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ThisExpression)

@given(instance=JavaAbstractSyntax_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_conditionalexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ConditionalExpression)

@given(instance=JavaAbstractSyntax_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SuperMethodInvocation)

@given(instance=JavaAbstractSyntax_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ParenthesizedExpression)

@given(instance=SimpleName_strategy)
@settings(max_examples=50)
def test_simplename_instantiation(instance):
    assert isinstance(instance, SimpleName)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=JavaAbstractSyntax_QualifiedName_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_qualifiedname_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_QualifiedName)

@given(instance=JavaAbstractSyntax_SimpleName_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_simplename_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_SimpleName)



@given(instance=JavaAbstractSyntax_SimpleName_strategy)
def test_javaabstractsyntax_simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=JavaAbstractSyntax_SimpleName_strategy)
def test_javaabstractsyntax_simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JavaAbstractSyntax_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_typedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TypeDeclaration)



@given(instance=JavaAbstractSyntax_TypeDeclaration_strategy)
def test_javaabstractsyntax_typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=JavaAbstractSyntax_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_AnnotationTypeDeclaration)

@given(instance=JavaAbstractSyntax_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_enumdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_EnumDeclaration)

@given(instance=ImportDeclaration_strategy)
@settings(max_examples=50)
def test_importdeclaration_instantiation(instance):
    assert isinstance(instance, ImportDeclaration)

@given(instance=PackageDeclaration_strategy)
@settings(max_examples=50)
def test_packagedeclaration_instantiation(instance):
    assert isinstance(instance, PackageDeclaration)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=Javadoc_strategy)
@settings(max_examples=50)
def test_javadoc_instantiation(instance):
    assert isinstance(instance, Javadoc)

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=JavaAbstractSyntax_Annotation_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_annotation_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Annotation)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JavaAbstractSyntax_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_fielddeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_FieldDeclaration)

@given(instance=JavaAbstractSyntax_EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_EnumConstantDeclaration)

@given(instance=JavaAbstractSyntax_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_methoddeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MethodDeclaration)



@given(instance=JavaAbstractSyntax_MethodDeclaration_strategy)
def test_javaabstractsyntax_methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original



@given(instance=JavaAbstractSyntax_MethodDeclaration_strategy)
def test_javaabstractsyntax_methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original



@given(instance=JavaAbstractSyntax_MethodDeclaration_strategy)
def test_javaabstractsyntax_methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=JavaAbstractSyntax_Initializer_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_initializer_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Initializer)

@given(instance=JavaAbstractSyntax_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_AnnotationTypeMemberDeclaration)

@given(instance=JavaAbstractSyntax_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_AbstractTypeDeclaration)



@given(instance=JavaAbstractSyntax_AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax_abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original



@given(instance=JavaAbstractSyntax_AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax_abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original



@given(instance=JavaAbstractSyntax_AbstractTypeDeclaration_strategy)
def test_javaabstractsyntax_abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original

@given(instance=JavaAbstractSyntax_ASTNode_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_astnode_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ASTNode)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JavaAbstractSyntax_TypeParameter_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_typeparameter_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TypeParameter)

@given(instance=JavaAbstractSyntax_MethodRef_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_methodref_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MethodRef)

@given(instance=JavaAbstractSyntax_Modifier_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_modifier_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Modifier)



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=JavaAbstractSyntax_Modifier_strategy)
def test_javaabstractsyntax_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=JavaAbstractSyntax_Expression_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_expression_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Expression)



@given(instance=JavaAbstractSyntax_Expression_strategy)
def test_javaabstractsyntax_expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original



@given(instance=JavaAbstractSyntax_Expression_strategy)
def test_javaabstractsyntax_expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original

@given(instance=JavaAbstractSyntax_TagElement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_tagelement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TagElement)



@given(instance=JavaAbstractSyntax_TagElement_strategy)
def test_javaabstractsyntax_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=JavaAbstractSyntax_TagElement_strategy)
def test_javaabstractsyntax_tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original

@given(instance=JavaAbstractSyntax_Type_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_type_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Type)

@given(instance=JavaAbstractSyntax_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_variabledeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_VariableDeclaration)



@given(instance=JavaAbstractSyntax_VariableDeclaration_strategy)
def test_javaabstractsyntax_variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=JavaAbstractSyntax_CatchClause_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_catchclause_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_CatchClause)

@given(instance=JavaAbstractSyntax_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_packagedeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_PackageDeclaration)

@given(instance=JavaAbstractSyntax_Comment_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_comment_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Comment)

@given(instance=JavaAbstractSyntax_AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_AnonymousClassDeclaration)

@given(instance=JavaAbstractSyntax_MemberRef_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_memberref_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MemberRef)

@given(instance=JavaAbstractSyntax_CompilationUnit_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_compilationunit_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_CompilationUnit)

@given(instance=JavaAbstractSyntax_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_importdeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_ImportDeclaration)



@given(instance=JavaAbstractSyntax_ImportDeclaration_strategy)
def test_javaabstractsyntax_importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original



@given(instance=JavaAbstractSyntax_ImportDeclaration_strategy)
def test_javaabstractsyntax_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=JavaAbstractSyntax_MemberValuePair_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_membervaluepair_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MemberValuePair)

@given(instance=JavaAbstractSyntax_MethodRefParameter_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_methodrefparameter_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_MethodRefParameter)



@given(instance=JavaAbstractSyntax_MethodRefParameter_strategy)
def test_javaabstractsyntax_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=JavaAbstractSyntax_TextElement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_textelement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_TextElement)



@given(instance=JavaAbstractSyntax_TextElement_strategy)
def test_javaabstractsyntax_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=JavaAbstractSyntax_Statement_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_statement_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_Statement)

@given(instance=JavaAbstractSyntax_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_bodydeclaration_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_BodyDeclaration)

@given(instance=JavaAbstractSyntax_AST_strategy)
@settings(max_examples=50)
def test_javaabstractsyntax_ast_instantiation(instance):
    assert isinstance(instance, JavaAbstractSyntax_AST)
