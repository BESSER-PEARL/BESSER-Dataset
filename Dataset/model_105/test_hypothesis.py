import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Annotation,
    DOM_SingleMemberAnnotation,
    DOM_NormalAnnotation,
    DOM_MarkerAnnotation,
    Name,
    DOM_QualifiedName,
    Type,
    DOM_SimpleType,
    DOM_ParameterizedType,
    DOM_PrimitiveType,
    DOM_QualifiedType,
    VariableDeclaration,
    DOM_WildcardType,
    Statement,
    DOM_ForStatement,
    DOM_ExpressionStatement,
    DOM_SwitchStatement,
    DOM_ConstructorInvocation,
    DOM_LabeledStatement,
    DOM_VariableDeclarationStatement,
    DOM_IfStatement,
    DOM_TypeDeclarationStatement,
    DOM_TryStatement,
    DOM_ThrowStatement,
    DOM_BreakStatement,
    DOM_ReturnStatement,
    DOM_EmptyStatement,
    DOM_EnhancedForStatement,
    DOM_SwitchCase,
    DOM_SuperConstructorInvocation,
    DOM_WhileStatement,
    DOM_SynchronizedStatement,
    DOM_AssertStatement,
    DOM_DoStatement,
    DOM_ContinueStatement,
    DOM_ArrayType,
    Expression,
    DOM_ParenthesizedExpression,
    DOM_ConditionalExpression,
    DOM_NumberLiteral,
    DOM_CastExpression,
    DOM_ThisExpression,
    DOM_BooleanLiteral,
    DOM_CharacterLiteral,
    DOM_ArrayInitializer,
    DOM_StringLiteral,
    DOM_InfixExpression,
    DOM_VariableDeclarationExpression,
    DOM_Assignment,
    DOM_SuperFieldAccess,
    DOM_MethodInvocation,
    DOM_SuperMethodInvocation,
    DOM_ArrayCreation,
    DOM_ArrayAccess,
    DOM_FieldAccess,
    DOM_ClassInstanceCreation,
    DOM_PrefixExpression,
    DOM_PostfixExpression,
    DOM_InstanceofExpression,
    DOM_TypeLiteral,
    DOM_NullLiteral,
    Comment,
    DOM_LineComment,
    DOM_BlockComment,
    AbstractTypeDeclaration,
    DOM_AnnotationTypeDeclaration,
    DOM_IMethod,
    DOM_VariableDeclarationFragment,
    DOM_TypeDeclaration,
    DOM_EnumDeclaration,
    BodyDeclaration,
    DOM_MethodDeclaration,
    DOM_Initializer,
    DOM_FieldDeclaration,
    DOM_IPackageFragment,
    DOM_EnumConstantDeclaration,
    DOM_AnnotationTypeMemberDeclaration,
    ExtendedModifier,
    DOM_Annotation,
    DOM_SimpleName,
    DOM_Name,
    DOM_AbstractTypeDeclaration,
    DOM_SingleVariableDeclaration,
    DOM_Block,
    DOM_Javadoc,
    DOM_ExtendedModifier,
    DOM_IType,
    ASTNode,
    DOM_MethodRef,
    DOM_MemberValuePair,
    DOM_TagElement,
    DOM_CompilationUnit,
    DOM_Statement,
    DOM_Expression,
    DOM_CatchClause,
    DOM_Type,
    DOM_MemberRef,
    DOM_Modifier,
    DOM_BodyDeclaration,
    DOM_Comment,
    DOM_TextElement,
    DOM_TypeParameter,
    DOM_VariableDeclaration,
    DOM_MethodRefParameter,
    DOM_PackageDeclaration,
    DOM_ImportDeclaration,
    DOM_AnonymousClassDeclaration,
    DOM_ASTNode,
    DOM_AST,
    InfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
    PostfixExpressionOperatorKind,
    AssignmentOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_SingleMemberAnnotation)


def test_dom_singlememberannotation_constructor_exists():
    assert callable(DOM_SingleMemberAnnotation.__init__)


def test_dom_singlememberannotation_constructor_args():
    sig = inspect.signature(DOM_SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_normalannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_NormalAnnotation)


def test_dom_normalannotation_constructor_exists():
    assert callable(DOM_NormalAnnotation.__init__)


def test_dom_normalannotation_constructor_args():
    sig = inspect.signature(DOM_NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_markerannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_MarkerAnnotation)


def test_dom_markerannotation_constructor_exists():
    assert callable(DOM_MarkerAnnotation.__init__)


def test_dom_markerannotation_constructor_args():
    sig = inspect.signature(DOM_MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_dom_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(DOM_QualifiedName)


def test_dom_qualifiedname_constructor_exists():
    assert callable(DOM_QualifiedName.__init__)


def test_dom_qualifiedname_constructor_args():
    sig = inspect.signature(DOM_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dom_simpletype_is_not_abstract():
    assert not inspect.isabstract(DOM_SimpleType)


def test_dom_simpletype_constructor_exists():
    assert callable(DOM_SimpleType.__init__)


def test_dom_simpletype_constructor_args():
    sig = inspect.signature(DOM_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_dom_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(DOM_ParameterizedType)


def test_dom_parameterizedtype_constructor_exists():
    assert callable(DOM_ParameterizedType.__init__)


def test_dom_parameterizedtype_constructor_args():
    sig = inspect.signature(DOM_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_dom_primitivetype_is_not_abstract():
    assert not inspect.isabstract(DOM_PrimitiveType)


def test_dom_primitivetype_constructor_exists():
    assert callable(DOM_PrimitiveType.__init__)


def test_dom_primitivetype_constructor_args():
    sig = inspect.signature(DOM_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_dom_primitivetype_has_code():
    assert hasattr(DOM_PrimitiveType, "code")
    descriptor = None
    for klass in DOM_PrimitiveType.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_dom_qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(DOM_QualifiedType)


def test_dom_qualifiedtype_constructor_exists():
    assert callable(DOM_QualifiedType.__init__)


def test_dom_qualifiedtype_constructor_args():
    sig = inspect.signature(DOM_QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(DOM_WildcardType)


def test_dom_wildcardtype_constructor_exists():
    assert callable(DOM_WildcardType.__init__)


def test_dom_wildcardtype_constructor_args():
    sig = inspect.signature(DOM_WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_dom_wildcardtype_has_upperBound():
    assert hasattr(DOM_WildcardType, "upperBound")
    descriptor = None
    for klass in DOM_WildcardType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom_forstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ForStatement)


def test_dom_forstatement_constructor_exists():
    assert callable(DOM_ForStatement.__init__)


def test_dom_forstatement_constructor_args():
    sig = inspect.signature(DOM_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ExpressionStatement)


def test_dom_expressionstatement_constructor_exists():
    assert callable(DOM_ExpressionStatement.__init__)


def test_dom_expressionstatement_constructor_args():
    sig = inspect.signature(DOM_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_switchstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_SwitchStatement)


def test_dom_switchstatement_constructor_exists():
    assert callable(DOM_SwitchStatement.__init__)


def test_dom_switchstatement_constructor_args():
    sig = inspect.signature(DOM_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_ConstructorInvocation)


def test_dom_constructorinvocation_constructor_exists():
    assert callable(DOM_ConstructorInvocation.__init__)


def test_dom_constructorinvocation_constructor_args():
    sig = inspect.signature(DOM_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_LabeledStatement)


def test_dom_labeledstatement_constructor_exists():
    assert callable(DOM_LabeledStatement.__init__)


def test_dom_labeledstatement_constructor_args():
    sig = inspect.signature(DOM_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationStatement)


def test_dom_variabledeclarationstatement_constructor_exists():
    assert callable(DOM_VariableDeclarationStatement.__init__)


def test_dom_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_ifstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_IfStatement)


def test_dom_ifstatement_constructor_exists():
    assert callable(DOM_IfStatement.__init__)


def test_dom_ifstatement_constructor_args():
    sig = inspect.signature(DOM_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeDeclarationStatement)


def test_dom_typedeclarationstatement_constructor_exists():
    assert callable(DOM_TypeDeclarationStatement.__init__)


def test_dom_typedeclarationstatement_constructor_args():
    sig = inspect.signature(DOM_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_trystatement_is_not_abstract():
    assert not inspect.isabstract(DOM_TryStatement)


def test_dom_trystatement_constructor_exists():
    assert callable(DOM_TryStatement.__init__)


def test_dom_trystatement_constructor_args():
    sig = inspect.signature(DOM_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_throwstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ThrowStatement)


def test_dom_throwstatement_constructor_exists():
    assert callable(DOM_ThrowStatement.__init__)


def test_dom_throwstatement_constructor_args():
    sig = inspect.signature(DOM_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_breakstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_BreakStatement)


def test_dom_breakstatement_constructor_exists():
    assert callable(DOM_BreakStatement.__init__)


def test_dom_breakstatement_constructor_args():
    sig = inspect.signature(DOM_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_returnstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ReturnStatement)


def test_dom_returnstatement_constructor_exists():
    assert callable(DOM_ReturnStatement.__init__)


def test_dom_returnstatement_constructor_args():
    sig = inspect.signature(DOM_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_emptystatement_is_not_abstract():
    assert not inspect.isabstract(DOM_EmptyStatement)


def test_dom_emptystatement_constructor_exists():
    assert callable(DOM_EmptyStatement.__init__)


def test_dom_emptystatement_constructor_args():
    sig = inspect.signature(DOM_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_EnhancedForStatement)


def test_dom_enhancedforstatement_constructor_exists():
    assert callable(DOM_EnhancedForStatement.__init__)


def test_dom_enhancedforstatement_constructor_args():
    sig = inspect.signature(DOM_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_switchcase_is_not_abstract():
    assert not inspect.isabstract(DOM_SwitchCase)


def test_dom_switchcase_constructor_exists():
    assert callable(DOM_SwitchCase.__init__)


def test_dom_switchcase_constructor_args():
    sig = inspect.signature(DOM_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_dom_switchcase_has_default():
    assert hasattr(DOM_SwitchCase, "default")
    descriptor = None
    for klass in DOM_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_dom_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperConstructorInvocation)


def test_dom_superconstructorinvocation_constructor_exists():
    assert callable(DOM_SuperConstructorInvocation.__init__)


def test_dom_superconstructorinvocation_constructor_args():
    sig = inspect.signature(DOM_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom_whilestatement_is_not_abstract():
    assert not inspect.isabstract(DOM_WhileStatement)


def test_dom_whilestatement_constructor_exists():
    assert callable(DOM_WhileStatement.__init__)


def test_dom_whilestatement_constructor_args():
    sig = inspect.signature(DOM_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_SynchronizedStatement)


def test_dom_synchronizedstatement_constructor_exists():
    assert callable(DOM_SynchronizedStatement.__init__)


def test_dom_synchronizedstatement_constructor_args():
    sig = inspect.signature(DOM_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_assertstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_AssertStatement)


def test_dom_assertstatement_constructor_exists():
    assert callable(DOM_AssertStatement.__init__)


def test_dom_assertstatement_constructor_args():
    sig = inspect.signature(DOM_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_dostatement_is_not_abstract():
    assert not inspect.isabstract(DOM_DoStatement)


def test_dom_dostatement_constructor_exists():
    assert callable(DOM_DoStatement.__init__)


def test_dom_dostatement_constructor_args():
    sig = inspect.signature(DOM_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_continuestatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ContinueStatement)


def test_dom_continuestatement_constructor_exists():
    assert callable(DOM_ContinueStatement.__init__)


def test_dom_continuestatement_constructor_args():
    sig = inspect.signature(DOM_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_arraytype_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayType)


def test_dom_arraytype_constructor_exists():
    assert callable(DOM_ArrayType.__init__)


def test_dom_arraytype_constructor_args():
    sig = inspect.signature(DOM_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_dom_arraytype_has_dimensions():
    assert hasattr(DOM_ArrayType, "dimensions")
    descriptor = None
    for klass in DOM_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ParenthesizedExpression)


def test_dom_parenthesizedexpression_constructor_exists():
    assert callable(DOM_ParenthesizedExpression.__init__)


def test_dom_parenthesizedexpression_constructor_args():
    sig = inspect.signature(DOM_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ConditionalExpression)


def test_dom_conditionalexpression_constructor_exists():
    assert callable(DOM_ConditionalExpression.__init__)


def test_dom_conditionalexpression_constructor_args():
    sig = inspect.signature(DOM_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_numberliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_NumberLiteral)


def test_dom_numberliteral_constructor_exists():
    assert callable(DOM_NumberLiteral.__init__)


def test_dom_numberliteral_constructor_args():
    sig = inspect.signature(DOM_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_dom_numberliteral_has_token():
    assert hasattr(DOM_NumberLiteral, "token")
    descriptor = None
    for klass in DOM_NumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_dom_castexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_CastExpression)


def test_dom_castexpression_constructor_exists():
    assert callable(DOM_CastExpression.__init__)


def test_dom_castexpression_constructor_args():
    sig = inspect.signature(DOM_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_thisexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ThisExpression)


def test_dom_thisexpression_constructor_exists():
    assert callable(DOM_ThisExpression.__init__)


def test_dom_thisexpression_constructor_args():
    sig = inspect.signature(DOM_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_BooleanLiteral)


def test_dom_booleanliteral_constructor_exists():
    assert callable(DOM_BooleanLiteral.__init__)


def test_dom_booleanliteral_constructor_args():
    sig = inspect.signature(DOM_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_dom_booleanliteral_has_booleanValue():
    assert hasattr(DOM_BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in DOM_BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_dom_characterliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_CharacterLiteral)


def test_dom_characterliteral_constructor_exists():
    assert callable(DOM_CharacterLiteral.__init__)


def test_dom_characterliteral_constructor_args():
    sig = inspect.signature(DOM_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "charValue" in params, "Missing parameter 'charValue'"

def test_dom_characterliteral_has_escapedValue():
    assert hasattr(DOM_CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in DOM_CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_dom_characterliteral_has_charValue():
    assert hasattr(DOM_CharacterLiteral, "charValue")
    descriptor = None
    for klass in DOM_CharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)



def test_dom_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayInitializer)


def test_dom_arrayinitializer_constructor_exists():
    assert callable(DOM_ArrayInitializer.__init__)


def test_dom_arrayinitializer_constructor_args():
    sig = inspect.signature(DOM_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dom_stringliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_StringLiteral)


def test_dom_stringliteral_constructor_exists():
    assert callable(DOM_StringLiteral.__init__)


def test_dom_stringliteral_constructor_args():
    sig = inspect.signature(DOM_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_dom_stringliteral_has_escapedValue():
    assert hasattr(DOM_StringLiteral, "escapedValue")
    descriptor = None
    for klass in DOM_StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_dom_stringliteral_has_literalValue():
    assert hasattr(DOM_StringLiteral, "literalValue")
    descriptor = None
    for klass in DOM_StringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_dom_infixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_InfixExpression)


def test_dom_infixexpression_constructor_exists():
    assert callable(DOM_InfixExpression.__init__)


def test_dom_infixexpression_constructor_args():
    sig = inspect.signature(DOM_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_infixexpression_has_operator():
    assert hasattr(DOM_InfixExpression, "operator")
    descriptor = None
    for klass in DOM_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationExpression)


def test_dom_variabledeclarationexpression_constructor_exists():
    assert callable(DOM_VariableDeclarationExpression.__init__)


def test_dom_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_assignment_is_not_abstract():
    assert not inspect.isabstract(DOM_Assignment)


def test_dom_assignment_constructor_exists():
    assert callable(DOM_Assignment.__init__)


def test_dom_assignment_constructor_args():
    sig = inspect.signature(DOM_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_assignment_has_operator():
    assert hasattr(DOM_Assignment, "operator")
    descriptor = None
    for klass in DOM_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperFieldAccess)


def test_dom_superfieldaccess_constructor_exists():
    assert callable(DOM_SuperFieldAccess.__init__)


def test_dom_superfieldaccess_constructor_args():
    sig = inspect.signature(DOM_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodInvocation)


def test_dom_methodinvocation_constructor_exists():
    assert callable(DOM_MethodInvocation.__init__)


def test_dom_methodinvocation_constructor_args():
    sig = inspect.signature(DOM_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperMethodInvocation)


def test_dom_supermethodinvocation_constructor_exists():
    assert callable(DOM_SuperMethodInvocation.__init__)


def test_dom_supermethodinvocation_constructor_args():
    sig = inspect.signature(DOM_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_dom_arraycreation_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayCreation)


def test_dom_arraycreation_constructor_exists():
    assert callable(DOM_ArrayCreation.__init__)


def test_dom_arraycreation_constructor_args():
    sig = inspect.signature(DOM_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_dom_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayAccess)


def test_dom_arrayaccess_constructor_exists():
    assert callable(DOM_ArrayAccess.__init__)


def test_dom_arrayaccess_constructor_args():
    sig = inspect.signature(DOM_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_FieldAccess)


def test_dom_fieldaccess_constructor_exists():
    assert callable(DOM_FieldAccess.__init__)


def test_dom_fieldaccess_constructor_args():
    sig = inspect.signature(DOM_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_dom_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(DOM_ClassInstanceCreation)


def test_dom_classinstancecreation_constructor_exists():
    assert callable(DOM_ClassInstanceCreation.__init__)


def test_dom_classinstancecreation_constructor_args():
    sig = inspect.signature(DOM_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_dom_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_PrefixExpression)


def test_dom_prefixexpression_constructor_exists():
    assert callable(DOM_PrefixExpression.__init__)


def test_dom_prefixexpression_constructor_args():
    sig = inspect.signature(DOM_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_prefixexpression_has_operator():
    assert hasattr(DOM_PrefixExpression, "operator")
    descriptor = None
    for klass in DOM_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_PostfixExpression)


def test_dom_postfixexpression_constructor_exists():
    assert callable(DOM_PostfixExpression.__init__)


def test_dom_postfixexpression_constructor_args():
    sig = inspect.signature(DOM_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_postfixexpression_has_operator():
    assert hasattr(DOM_PostfixExpression, "operator")
    descriptor = None
    for klass in DOM_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_InstanceofExpression)


def test_dom_instanceofexpression_constructor_exists():
    assert callable(DOM_InstanceofExpression.__init__)


def test_dom_instanceofexpression_constructor_args():
    sig = inspect.signature(DOM_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_typeliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeLiteral)


def test_dom_typeliteral_constructor_exists():
    assert callable(DOM_TypeLiteral.__init__)


def test_dom_typeliteral_constructor_args():
    sig = inspect.signature(DOM_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dom_nullliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_NullLiteral)


def test_dom_nullliteral_constructor_exists():
    assert callable(DOM_NullLiteral.__init__)


def test_dom_nullliteral_constructor_args():
    sig = inspect.signature(DOM_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_dom_linecomment_is_not_abstract():
    assert not inspect.isabstract(DOM_LineComment)


def test_dom_linecomment_constructor_exists():
    assert callable(DOM_LineComment.__init__)


def test_dom_linecomment_constructor_args():
    sig = inspect.signature(DOM_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_dom_blockcomment_is_not_abstract():
    assert not inspect.isabstract(DOM_BlockComment)


def test_dom_blockcomment_constructor_exists():
    assert callable(DOM_BlockComment.__init__)


def test_dom_blockcomment_constructor_args():
    sig = inspect.signature(DOM_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnnotationTypeDeclaration)


def test_dom_annotationtypedeclaration_constructor_exists():
    assert callable(DOM_AnnotationTypeDeclaration.__init__)


def test_dom_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(DOM_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_imethod_is_not_abstract():
    assert not inspect.isabstract(DOM_IMethod)


def test_dom_imethod_constructor_exists():
    assert callable(DOM_IMethod.__init__)


def test_dom_imethod_constructor_args():
    sig = inspect.signature(DOM_IMethod.__init__)
    params = list(sig.parameters.keys())



def test_dom_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationFragment)


def test_dom_variabledeclarationfragment_constructor_exists():
    assert callable(DOM_VariableDeclarationFragment.__init__)


def test_dom_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_dom_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeDeclaration)


def test_dom_typedeclaration_constructor_exists():
    assert callable(DOM_TypeDeclaration.__init__)


def test_dom_typedeclaration_constructor_args():
    sig = inspect.signature(DOM_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_dom_typedeclaration_has_interface():
    assert hasattr(DOM_TypeDeclaration, "interface")
    descriptor = None
    for klass in DOM_TypeDeclaration.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_dom_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_EnumDeclaration)


def test_dom_enumdeclaration_constructor_exists():
    assert callable(DOM_EnumDeclaration.__init__)


def test_dom_enumdeclaration_constructor_args():
    sig = inspect.signature(DOM_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodDeclaration)


def test_dom_methoddeclaration_constructor_exists():
    assert callable(DOM_MethodDeclaration.__init__)


def test_dom_methoddeclaration_constructor_args():
    sig = inspect.signature(DOM_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_dom_methoddeclaration_has_varargs():
    assert hasattr(DOM_MethodDeclaration, "varargs")
    descriptor = None
    for klass in DOM_MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_dom_methoddeclaration_has_constructor():
    assert hasattr(DOM_MethodDeclaration, "constructor")
    descriptor = None
    for klass in DOM_MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_dom_methoddeclaration_has_extraDimensions():
    assert hasattr(DOM_MethodDeclaration, "extraDimensions")
    descriptor = None
    for klass in DOM_MethodDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_dom_initializer_is_not_abstract():
    assert not inspect.isabstract(DOM_Initializer)


def test_dom_initializer_constructor_exists():
    assert callable(DOM_Initializer.__init__)


def test_dom_initializer_constructor_args():
    sig = inspect.signature(DOM_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_dom_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_FieldDeclaration)


def test_dom_fielddeclaration_constructor_exists():
    assert callable(DOM_FieldDeclaration.__init__)


def test_dom_fielddeclaration_constructor_args():
    sig = inspect.signature(DOM_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(DOM_IPackageFragment)


def test_dom_ipackagefragment_constructor_exists():
    assert callable(DOM_IPackageFragment.__init__)


def test_dom_ipackagefragment_constructor_args():
    sig = inspect.signature(DOM_IPackageFragment.__init__)
    params = list(sig.parameters.keys())



def test_dom_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_EnumConstantDeclaration)


def test_dom_enumconstantdeclaration_constructor_exists():
    assert callable(DOM_EnumConstantDeclaration.__init__)


def test_dom_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(DOM_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnnotationTypeMemberDeclaration)


def test_dom_annotationtypememberdeclaration_constructor_exists():
    assert callable(DOM_AnnotationTypeMemberDeclaration.__init__)


def test_dom_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(DOM_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_dom_annotation_is_not_abstract():
    assert not inspect.isabstract(DOM_Annotation)


def test_dom_annotation_constructor_exists():
    assert callable(DOM_Annotation.__init__)


def test_dom_annotation_constructor_args():
    sig = inspect.signature(DOM_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_simplename_is_not_abstract():
    assert not inspect.isabstract(DOM_SimpleName)


def test_dom_simplename_constructor_exists():
    assert callable(DOM_SimpleName.__init__)


def test_dom_simplename_constructor_args():
    sig = inspect.signature(DOM_SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_dom_simplename_has_identifier():
    assert hasattr(DOM_SimpleName, "identifier")
    descriptor = None
    for klass in DOM_SimpleName.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_dom_simplename_has_declaration():
    assert hasattr(DOM_SimpleName, "declaration")
    descriptor = None
    for klass in DOM_SimpleName.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_dom_name_is_not_abstract():
    assert not inspect.isabstract(DOM_Name)


def test_dom_name_constructor_exists():
    assert callable(DOM_Name.__init__)


def test_dom_name_constructor_args():
    sig = inspect.signature(DOM_Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"

def test_dom_name_has_fullyQualifiedName():
    assert hasattr(DOM_Name, "fullyQualifiedName")
    descriptor = None
    for klass in DOM_Name.__mro__:
        if "fullyQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["fullyQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_dom_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AbstractTypeDeclaration)


def test_dom_abstracttypedeclaration_constructor_exists():
    assert callable(DOM_AbstractTypeDeclaration.__init__)


def test_dom_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(DOM_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"

def test_dom_abstracttypedeclaration_has_localTypeDeclaration():
    assert hasattr(DOM_AbstractTypeDeclaration, "localTypeDeclaration")
    descriptor = None
    for klass in DOM_AbstractTypeDeclaration.__mro__:
        if "localTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["localTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_dom_abstracttypedeclaration_has_packageMemberTypeDeclaration():
    assert hasattr(DOM_AbstractTypeDeclaration, "packageMemberTypeDeclaration")
    descriptor = None
    for klass in DOM_AbstractTypeDeclaration.__mro__:
        if "packageMemberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["packageMemberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_dom_abstracttypedeclaration_has_memberTypeDeclaration():
    assert hasattr(DOM_AbstractTypeDeclaration, "memberTypeDeclaration")
    descriptor = None
    for klass in DOM_AbstractTypeDeclaration.__mro__:
        if "memberTypeDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["memberTypeDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_dom_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_SingleVariableDeclaration)


def test_dom_singlevariabledeclaration_constructor_exists():
    assert callable(DOM_SingleVariableDeclaration.__init__)


def test_dom_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(DOM_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_dom_singlevariabledeclaration_has_varargs():
    assert hasattr(DOM_SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in DOM_SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_dom_block_is_not_abstract():
    assert not inspect.isabstract(DOM_Block)


def test_dom_block_constructor_exists():
    assert callable(DOM_Block.__init__)


def test_dom_block_constructor_args():
    sig = inspect.signature(DOM_Block.__init__)
    params = list(sig.parameters.keys())



def test_dom_javadoc_is_not_abstract():
    assert not inspect.isabstract(DOM_Javadoc)


def test_dom_javadoc_constructor_exists():
    assert callable(DOM_Javadoc.__init__)


def test_dom_javadoc_constructor_args():
    sig = inspect.signature(DOM_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_dom_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(DOM_ExtendedModifier)


def test_dom_extendedmodifier_constructor_exists():
    assert callable(DOM_ExtendedModifier.__init__)


def test_dom_extendedmodifier_constructor_args():
    sig = inspect.signature(DOM_ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_dom_itype_is_not_abstract():
    assert not inspect.isabstract(DOM_IType)


def test_dom_itype_constructor_exists():
    assert callable(DOM_IType.__init__)


def test_dom_itype_constructor_args():
    sig = inspect.signature(DOM_IType.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_dom_methodref_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodRef)


def test_dom_methodref_constructor_exists():
    assert callable(DOM_MethodRef.__init__)


def test_dom_methodref_constructor_args():
    sig = inspect.signature(DOM_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_dom_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(DOM_MemberValuePair)


def test_dom_membervaluepair_constructor_exists():
    assert callable(DOM_MemberValuePair.__init__)


def test_dom_membervaluepair_constructor_args():
    sig = inspect.signature(DOM_MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_dom_tagelement_is_not_abstract():
    assert not inspect.isabstract(DOM_TagElement)


def test_dom_tagelement_constructor_exists():
    assert callable(DOM_TagElement.__init__)


def test_dom_tagelement_constructor_args():
    sig = inspect.signature(DOM_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "nested" in params, "Missing parameter 'nested'"

def test_dom_tagelement_has_tagName():
    assert hasattr(DOM_TagElement, "tagName")
    descriptor = None
    for klass in DOM_TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)

def test_dom_tagelement_has_nested():
    assert hasattr(DOM_TagElement, "nested")
    descriptor = None
    for klass in DOM_TagElement.__mro__:
        if "nested" in klass.__dict__:
            descriptor = klass.__dict__["nested"]
            break
    assert isinstance(descriptor, property)



def test_dom_compilationunit_is_not_abstract():
    assert not inspect.isabstract(DOM_CompilationUnit)


def test_dom_compilationunit_constructor_exists():
    assert callable(DOM_CompilationUnit.__init__)


def test_dom_compilationunit_constructor_args():
    sig = inspect.signature(DOM_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_dom_statement_is_not_abstract():
    assert not inspect.isabstract(DOM_Statement)


def test_dom_statement_constructor_exists():
    assert callable(DOM_Statement.__init__)


def test_dom_statement_constructor_args():
    sig = inspect.signature(DOM_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom_expression_is_not_abstract():
    assert not inspect.isabstract(DOM_Expression)


def test_dom_expression_constructor_exists():
    assert callable(DOM_Expression.__init__)


def test_dom_expression_constructor_args():
    sig = inspect.signature(DOM_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"

def test_dom_expression_has_resolveUnboxing():
    assert hasattr(DOM_Expression, "resolveUnboxing")
    descriptor = None
    for klass in DOM_Expression.__mro__:
        if "resolveUnboxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveUnboxing"]
            break
    assert isinstance(descriptor, property)

def test_dom_expression_has_resolveBoxing():
    assert hasattr(DOM_Expression, "resolveBoxing")
    descriptor = None
    for klass in DOM_Expression.__mro__:
        if "resolveBoxing" in klass.__dict__:
            descriptor = klass.__dict__["resolveBoxing"]
            break
    assert isinstance(descriptor, property)



def test_dom_catchclause_is_not_abstract():
    assert not inspect.isabstract(DOM_CatchClause)


def test_dom_catchclause_constructor_exists():
    assert callable(DOM_CatchClause.__init__)


def test_dom_catchclause_constructor_args():
    sig = inspect.signature(DOM_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_dom_type_is_not_abstract():
    assert not inspect.isabstract(DOM_Type)


def test_dom_type_constructor_exists():
    assert callable(DOM_Type.__init__)


def test_dom_type_constructor_args():
    sig = inspect.signature(DOM_Type.__init__)
    params = list(sig.parameters.keys())



def test_dom_memberref_is_not_abstract():
    assert not inspect.isabstract(DOM_MemberRef)


def test_dom_memberref_constructor_exists():
    assert callable(DOM_MemberRef.__init__)


def test_dom_memberref_constructor_args():
    sig = inspect.signature(DOM_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_dom_modifier_is_not_abstract():
    assert not inspect.isabstract(DOM_Modifier)


def test_dom_modifier_constructor_exists():
    assert callable(DOM_Modifier.__init__)


def test_dom_modifier_constructor_args():
    sig = inspect.signature(DOM_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "native" in params, "Missing parameter 'native'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "private" in params, "Missing parameter 'private'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "public" in params, "Missing parameter 'public'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "final" in params, "Missing parameter 'final'"
    assert "static" in params, "Missing parameter 'static'"

def test_dom_modifier_has_none():
    assert hasattr(DOM_Modifier, "none")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_native():
    assert hasattr(DOM_Modifier, "native")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_strictfp():
    assert hasattr(DOM_Modifier, "strictfp")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_protected():
    assert hasattr(DOM_Modifier, "protected")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_abstract():
    assert hasattr(DOM_Modifier, "abstract")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_private():
    assert hasattr(DOM_Modifier, "private")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_synchronized():
    assert hasattr(DOM_Modifier, "synchronized")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_public():
    assert hasattr(DOM_Modifier, "public")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_transient():
    assert hasattr(DOM_Modifier, "transient")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_volatile():
    assert hasattr(DOM_Modifier, "volatile")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_final():
    assert hasattr(DOM_Modifier, "final")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_dom_modifier_has_static():
    assert hasattr(DOM_Modifier, "static")
    descriptor = None
    for klass in DOM_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_dom_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_BodyDeclaration)


def test_dom_bodydeclaration_constructor_exists():
    assert callable(DOM_BodyDeclaration.__init__)


def test_dom_bodydeclaration_constructor_args():
    sig = inspect.signature(DOM_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_comment_is_not_abstract():
    assert not inspect.isabstract(DOM_Comment)


def test_dom_comment_constructor_exists():
    assert callable(DOM_Comment.__init__)


def test_dom_comment_constructor_args():
    sig = inspect.signature(DOM_Comment.__init__)
    params = list(sig.parameters.keys())



def test_dom_textelement_is_not_abstract():
    assert not inspect.isabstract(DOM_TextElement)


def test_dom_textelement_constructor_exists():
    assert callable(DOM_TextElement.__init__)


def test_dom_textelement_constructor_args():
    sig = inspect.signature(DOM_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_dom_textelement_has_text():
    assert hasattr(DOM_TextElement, "text")
    descriptor = None
    for klass in DOM_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_dom_typeparameter_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeParameter)


def test_dom_typeparameter_constructor_exists():
    assert callable(DOM_TypeParameter.__init__)


def test_dom_typeparameter_constructor_args():
    sig = inspect.signature(DOM_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclaration)


def test_dom_variabledeclaration_constructor_exists():
    assert callable(DOM_VariableDeclaration.__init__)


def test_dom_variabledeclaration_constructor_args():
    sig = inspect.signature(DOM_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"

def test_dom_variabledeclaration_has_extraDimensions():
    assert hasattr(DOM_VariableDeclaration, "extraDimensions")
    descriptor = None
    for klass in DOM_VariableDeclaration.__mro__:
        if "extraDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraDimensions"]
            break
    assert isinstance(descriptor, property)



def test_dom_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodRefParameter)


def test_dom_methodrefparameter_constructor_exists():
    assert callable(DOM_MethodRefParameter.__init__)


def test_dom_methodrefparameter_constructor_args():
    sig = inspect.signature(DOM_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_dom_methodrefparameter_has_varargs():
    assert hasattr(DOM_MethodRefParameter, "varargs")
    descriptor = None
    for klass in DOM_MethodRefParameter.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_dom_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_PackageDeclaration)


def test_dom_packagedeclaration_constructor_exists():
    assert callable(DOM_PackageDeclaration.__init__)


def test_dom_packagedeclaration_constructor_args():
    sig = inspect.signature(DOM_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_ImportDeclaration)


def test_dom_importdeclaration_constructor_exists():
    assert callable(DOM_ImportDeclaration.__init__)


def test_dom_importdeclaration_constructor_args():
    sig = inspect.signature(DOM_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"

def test_dom_importdeclaration_has_onDemand():
    assert hasattr(DOM_ImportDeclaration, "onDemand")
    descriptor = None
    for klass in DOM_ImportDeclaration.__mro__:
        if "onDemand" in klass.__dict__:
            descriptor = klass.__dict__["onDemand"]
            break
    assert isinstance(descriptor, property)

def test_dom_importdeclaration_has_static():
    assert hasattr(DOM_ImportDeclaration, "static")
    descriptor = None
    for klass in DOM_ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_dom_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnonymousClassDeclaration)


def test_dom_anonymousclassdeclaration_constructor_exists():
    assert callable(DOM_AnonymousClassDeclaration.__init__)


def test_dom_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(DOM_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dom_astnode_is_not_abstract():
    assert not inspect.isabstract(DOM_ASTNode)


def test_dom_astnode_constructor_exists():
    assert callable(DOM_ASTNode.__init__)


def test_dom_astnode_constructor_args():
    sig = inspect.signature(DOM_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_dom_ast_is_not_abstract():
    assert not inspect.isabstract(DOM_AST)


def test_dom_ast_constructor_exists():
    assert callable(DOM_AST.__init__)


def test_dom_ast_constructor_args():
    sig = inspect.signature(DOM_AST.__init__)
    params = list(sig.parameters.keys())

def test_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "greater_equals",
        "conditional_and",
        "xor",
        "times",
        "remainder",
        "left_shift",
        "conditional_or",
        "plus",
        "right_shift_signed",
        "equals",
        "less_equals",
        "greater",
        "right_shift_unsigned",
        "less",
        "minus",
        "not_equals",
        "divide",
        "or_",
        "and_",
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
        "not_",
        "minus",
        "complement",
        "decrement",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionOperatorKind"

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

def test_assignmentoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorKind is not None

def test_assignmentoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorKind]
    expected_literals = [
        "left_shift_assign",
        "divide_assign",
        "right_shift_unsigned_assign",
        "assign",
        "right_shift_signed_assign",
        "remainder_assign",
        "bit_xor_assign",
        "bit_and_assign",
        "minus_assign",
        "plus_assign",
        "bit_or_assign",
        "times_assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"


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
Annotation_strategy = st.builds(
    Annotation,
)
DOM_SingleMemberAnnotation_strategy = st.builds(
    DOM_SingleMemberAnnotation,
)
DOM_NormalAnnotation_strategy = st.builds(
    DOM_NormalAnnotation,
)
DOM_MarkerAnnotation_strategy = st.builds(
    DOM_MarkerAnnotation,
)
Name_strategy = st.builds(
    Name,
)
DOM_QualifiedName_strategy = st.builds(
    DOM_QualifiedName,
)
Type_strategy = st.builds(
    Type,
)
DOM_SimpleType_strategy = st.builds(
    DOM_SimpleType,
)
DOM_ParameterizedType_strategy = st.builds(
    DOM_ParameterizedType,
)
DOM_PrimitiveType_strategy = st.builds(
    DOM_PrimitiveType,
    code=
        safe_text
)
DOM_QualifiedType_strategy = st.builds(
    DOM_QualifiedType,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
DOM_WildcardType_strategy = st.builds(
    DOM_WildcardType,
    upperBound=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
DOM_ForStatement_strategy = st.builds(
    DOM_ForStatement,
)
DOM_ExpressionStatement_strategy = st.builds(
    DOM_ExpressionStatement,
)
DOM_SwitchStatement_strategy = st.builds(
    DOM_SwitchStatement,
)
DOM_ConstructorInvocation_strategy = st.builds(
    DOM_ConstructorInvocation,
)
DOM_LabeledStatement_strategy = st.builds(
    DOM_LabeledStatement,
)
DOM_VariableDeclarationStatement_strategy = st.builds(
    DOM_VariableDeclarationStatement,
)
DOM_IfStatement_strategy = st.builds(
    DOM_IfStatement,
)
DOM_TypeDeclarationStatement_strategy = st.builds(
    DOM_TypeDeclarationStatement,
)
DOM_TryStatement_strategy = st.builds(
    DOM_TryStatement,
)
DOM_ThrowStatement_strategy = st.builds(
    DOM_ThrowStatement,
)
DOM_BreakStatement_strategy = st.builds(
    DOM_BreakStatement,
)
DOM_ReturnStatement_strategy = st.builds(
    DOM_ReturnStatement,
)
DOM_EmptyStatement_strategy = st.builds(
    DOM_EmptyStatement,
)
DOM_EnhancedForStatement_strategy = st.builds(
    DOM_EnhancedForStatement,
)
DOM_SwitchCase_strategy = st.builds(
    DOM_SwitchCase,
    default=
        safe_text
)
DOM_SuperConstructorInvocation_strategy = st.builds(
    DOM_SuperConstructorInvocation,
)
DOM_WhileStatement_strategy = st.builds(
    DOM_WhileStatement,
)
DOM_SynchronizedStatement_strategy = st.builds(
    DOM_SynchronizedStatement,
)
DOM_AssertStatement_strategy = st.builds(
    DOM_AssertStatement,
)
DOM_DoStatement_strategy = st.builds(
    DOM_DoStatement,
)
DOM_ContinueStatement_strategy = st.builds(
    DOM_ContinueStatement,
)
DOM_ArrayType_strategy = st.builds(
    DOM_ArrayType,
    dimensions=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
DOM_ParenthesizedExpression_strategy = st.builds(
    DOM_ParenthesizedExpression,
)
DOM_ConditionalExpression_strategy = st.builds(
    DOM_ConditionalExpression,
)
DOM_NumberLiteral_strategy = st.builds(
    DOM_NumberLiteral,
    token=
        safe_text
)
DOM_CastExpression_strategy = st.builds(
    DOM_CastExpression,
)
DOM_ThisExpression_strategy = st.builds(
    DOM_ThisExpression,
)
DOM_BooleanLiteral_strategy = st.builds(
    DOM_BooleanLiteral,
    booleanValue=
        safe_text
)
DOM_CharacterLiteral_strategy = st.builds(
    DOM_CharacterLiteral,
    escapedValue=
        safe_text,
    charValue=
        safe_text
)
DOM_ArrayInitializer_strategy = st.builds(
    DOM_ArrayInitializer,
)
DOM_StringLiteral_strategy = st.builds(
    DOM_StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
DOM_InfixExpression_strategy = st.builds(
    DOM_InfixExpression,
    operator=
        safe_text
)
DOM_VariableDeclarationExpression_strategy = st.builds(
    DOM_VariableDeclarationExpression,
)
DOM_Assignment_strategy = st.builds(
    DOM_Assignment,
    operator=
        safe_text
)
DOM_SuperFieldAccess_strategy = st.builds(
    DOM_SuperFieldAccess,
)
DOM_MethodInvocation_strategy = st.builds(
    DOM_MethodInvocation,
)
DOM_SuperMethodInvocation_strategy = st.builds(
    DOM_SuperMethodInvocation,
)
DOM_ArrayCreation_strategy = st.builds(
    DOM_ArrayCreation,
)
DOM_ArrayAccess_strategy = st.builds(
    DOM_ArrayAccess,
)
DOM_FieldAccess_strategy = st.builds(
    DOM_FieldAccess,
)
DOM_ClassInstanceCreation_strategy = st.builds(
    DOM_ClassInstanceCreation,
)
DOM_PrefixExpression_strategy = st.builds(
    DOM_PrefixExpression,
    operator=
        safe_text
)
DOM_PostfixExpression_strategy = st.builds(
    DOM_PostfixExpression,
    operator=
        safe_text
)
DOM_InstanceofExpression_strategy = st.builds(
    DOM_InstanceofExpression,
)
DOM_TypeLiteral_strategy = st.builds(
    DOM_TypeLiteral,
)
DOM_NullLiteral_strategy = st.builds(
    DOM_NullLiteral,
)
Comment_strategy = st.builds(
    Comment,
)
DOM_LineComment_strategy = st.builds(
    DOM_LineComment,
)
DOM_BlockComment_strategy = st.builds(
    DOM_BlockComment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
DOM_AnnotationTypeDeclaration_strategy = st.builds(
    DOM_AnnotationTypeDeclaration,
)
DOM_IMethod_strategy = st.builds(
    DOM_IMethod,
)
DOM_VariableDeclarationFragment_strategy = st.builds(
    DOM_VariableDeclarationFragment,
)
DOM_TypeDeclaration_strategy = st.builds(
    DOM_TypeDeclaration,
    interface=
        safe_text
)
DOM_EnumDeclaration_strategy = st.builds(
    DOM_EnumDeclaration,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
DOM_MethodDeclaration_strategy = st.builds(
    DOM_MethodDeclaration,
    varargs=
        safe_text,
    constructor=
        safe_text,
    extraDimensions=
        safe_text
)
DOM_Initializer_strategy = st.builds(
    DOM_Initializer,
)
DOM_FieldDeclaration_strategy = st.builds(
    DOM_FieldDeclaration,
)
DOM_IPackageFragment_strategy = st.builds(
    DOM_IPackageFragment,
)
DOM_EnumConstantDeclaration_strategy = st.builds(
    DOM_EnumConstantDeclaration,
)
DOM_AnnotationTypeMemberDeclaration_strategy = st.builds(
    DOM_AnnotationTypeMemberDeclaration,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
DOM_Annotation_strategy = st.builds(
    DOM_Annotation,
)
DOM_SimpleName_strategy = st.builds(
    DOM_SimpleName,
    identifier=
        safe_text,
    declaration=
        safe_text
)
DOM_Name_strategy = st.builds(
    DOM_Name,
    fullyQualifiedName=
        safe_text
)
DOM_AbstractTypeDeclaration_strategy = st.builds(
    DOM_AbstractTypeDeclaration,
    localTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text,
    memberTypeDeclaration=
        safe_text
)
DOM_SingleVariableDeclaration_strategy = st.builds(
    DOM_SingleVariableDeclaration,
    varargs=
        safe_text
)
DOM_Block_strategy = st.builds(
    DOM_Block,
)
DOM_Javadoc_strategy = st.builds(
    DOM_Javadoc,
)
DOM_ExtendedModifier_strategy = st.builds(
    DOM_ExtendedModifier,
)
DOM_IType_strategy = st.builds(
    DOM_IType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
DOM_MethodRef_strategy = st.builds(
    DOM_MethodRef,
)
DOM_MemberValuePair_strategy = st.builds(
    DOM_MemberValuePair,
)
DOM_TagElement_strategy = st.builds(
    DOM_TagElement,
    tagName=
        safe_text,
    nested=
        safe_text
)
DOM_CompilationUnit_strategy = st.builds(
    DOM_CompilationUnit,
)
DOM_Statement_strategy = st.builds(
    DOM_Statement,
)
DOM_Expression_strategy = st.builds(
    DOM_Expression,
    resolveUnboxing=
        safe_text,
    resolveBoxing=
        safe_text
)
DOM_CatchClause_strategy = st.builds(
    DOM_CatchClause,
)
DOM_Type_strategy = st.builds(
    DOM_Type,
)
DOM_MemberRef_strategy = st.builds(
    DOM_MemberRef,
)
DOM_Modifier_strategy = st.builds(
    DOM_Modifier,
    none=
        safe_text,
    native=
        safe_text,
    strictfp=
        safe_text,
    protected=
        safe_text,
    abstract=
        safe_text,
    private=
        safe_text,
    synchronized=
        safe_text,
    public=
        safe_text,
    transient=
        safe_text,
    volatile=
        safe_text,
    final=
        safe_text,
    static=
        safe_text
)
DOM_BodyDeclaration_strategy = st.builds(
    DOM_BodyDeclaration,
)
DOM_Comment_strategy = st.builds(
    DOM_Comment,
)
DOM_TextElement_strategy = st.builds(
    DOM_TextElement,
    text=
        safe_text
)
DOM_TypeParameter_strategy = st.builds(
    DOM_TypeParameter,
)
DOM_VariableDeclaration_strategy = st.builds(
    DOM_VariableDeclaration,
    extraDimensions=
        safe_text
)
DOM_MethodRefParameter_strategy = st.builds(
    DOM_MethodRefParameter,
    varargs=
        safe_text
)
DOM_PackageDeclaration_strategy = st.builds(
    DOM_PackageDeclaration,
)
DOM_ImportDeclaration_strategy = st.builds(
    DOM_ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
DOM_AnonymousClassDeclaration_strategy = st.builds(
    DOM_AnonymousClassDeclaration,
)
DOM_ASTNode_strategy = st.builds(
    DOM_ASTNode,
)
DOM_AST_strategy = st.builds(
    DOM_AST,
)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=DOM_SingleMemberAnnotation_strategy)
@settings(max_examples=50)
def test_dom_singlememberannotation_instantiation(instance):
    assert isinstance(instance, DOM_SingleMemberAnnotation)

@given(instance=DOM_NormalAnnotation_strategy)
@settings(max_examples=50)
def test_dom_normalannotation_instantiation(instance):
    assert isinstance(instance, DOM_NormalAnnotation)

@given(instance=DOM_MarkerAnnotation_strategy)
@settings(max_examples=50)
def test_dom_markerannotation_instantiation(instance):
    assert isinstance(instance, DOM_MarkerAnnotation)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DOM_QualifiedName_strategy)
@settings(max_examples=50)
def test_dom_qualifiedname_instantiation(instance):
    assert isinstance(instance, DOM_QualifiedName)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=DOM_SimpleType_strategy)
@settings(max_examples=50)
def test_dom_simpletype_instantiation(instance):
    assert isinstance(instance, DOM_SimpleType)

@given(instance=DOM_ParameterizedType_strategy)
@settings(max_examples=50)
def test_dom_parameterizedtype_instantiation(instance):
    assert isinstance(instance, DOM_ParameterizedType)

@given(instance=DOM_PrimitiveType_strategy)
@settings(max_examples=50)
def test_dom_primitivetype_instantiation(instance):
    assert isinstance(instance, DOM_PrimitiveType)



@given(instance=DOM_PrimitiveType_strategy)
def test_dom_primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=DOM_QualifiedType_strategy)
@settings(max_examples=50)
def test_dom_qualifiedtype_instantiation(instance):
    assert isinstance(instance, DOM_QualifiedType)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=DOM_WildcardType_strategy)
@settings(max_examples=50)
def test_dom_wildcardtype_instantiation(instance):
    assert isinstance(instance, DOM_WildcardType)



@given(instance=DOM_WildcardType_strategy)
def test_dom_wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DOM_ForStatement_strategy)
@settings(max_examples=50)
def test_dom_forstatement_instantiation(instance):
    assert isinstance(instance, DOM_ForStatement)

@given(instance=DOM_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom_expressionstatement_instantiation(instance):
    assert isinstance(instance, DOM_ExpressionStatement)

@given(instance=DOM_SwitchStatement_strategy)
@settings(max_examples=50)
def test_dom_switchstatement_instantiation(instance):
    assert isinstance(instance, DOM_SwitchStatement)

@given(instance=DOM_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dom_constructorinvocation_instantiation(instance):
    assert isinstance(instance, DOM_ConstructorInvocation)

@given(instance=DOM_LabeledStatement_strategy)
@settings(max_examples=50)
def test_dom_labeledstatement_instantiation(instance):
    assert isinstance(instance, DOM_LabeledStatement)

@given(instance=DOM_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclarationStatement)

@given(instance=DOM_IfStatement_strategy)
@settings(max_examples=50)
def test_dom_ifstatement_instantiation(instance):
    assert isinstance(instance, DOM_IfStatement)

@given(instance=DOM_TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom_typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, DOM_TypeDeclarationStatement)

@given(instance=DOM_TryStatement_strategy)
@settings(max_examples=50)
def test_dom_trystatement_instantiation(instance):
    assert isinstance(instance, DOM_TryStatement)

@given(instance=DOM_ThrowStatement_strategy)
@settings(max_examples=50)
def test_dom_throwstatement_instantiation(instance):
    assert isinstance(instance, DOM_ThrowStatement)

@given(instance=DOM_BreakStatement_strategy)
@settings(max_examples=50)
def test_dom_breakstatement_instantiation(instance):
    assert isinstance(instance, DOM_BreakStatement)

@given(instance=DOM_ReturnStatement_strategy)
@settings(max_examples=50)
def test_dom_returnstatement_instantiation(instance):
    assert isinstance(instance, DOM_ReturnStatement)

@given(instance=DOM_EmptyStatement_strategy)
@settings(max_examples=50)
def test_dom_emptystatement_instantiation(instance):
    assert isinstance(instance, DOM_EmptyStatement)

@given(instance=DOM_EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_dom_enhancedforstatement_instantiation(instance):
    assert isinstance(instance, DOM_EnhancedForStatement)

@given(instance=DOM_SwitchCase_strategy)
@settings(max_examples=50)
def test_dom_switchcase_instantiation(instance):
    assert isinstance(instance, DOM_SwitchCase)



@given(instance=DOM_SwitchCase_strategy)
def test_dom_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=DOM_SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dom_superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, DOM_SuperConstructorInvocation)

@given(instance=DOM_WhileStatement_strategy)
@settings(max_examples=50)
def test_dom_whilestatement_instantiation(instance):
    assert isinstance(instance, DOM_WhileStatement)

@given(instance=DOM_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_dom_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, DOM_SynchronizedStatement)

@given(instance=DOM_AssertStatement_strategy)
@settings(max_examples=50)
def test_dom_assertstatement_instantiation(instance):
    assert isinstance(instance, DOM_AssertStatement)

@given(instance=DOM_DoStatement_strategy)
@settings(max_examples=50)
def test_dom_dostatement_instantiation(instance):
    assert isinstance(instance, DOM_DoStatement)

@given(instance=DOM_ContinueStatement_strategy)
@settings(max_examples=50)
def test_dom_continuestatement_instantiation(instance):
    assert isinstance(instance, DOM_ContinueStatement)

@given(instance=DOM_ArrayType_strategy)
@settings(max_examples=50)
def test_dom_arraytype_instantiation(instance):
    assert isinstance(instance, DOM_ArrayType)



@given(instance=DOM_ArrayType_strategy)
def test_dom_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=DOM_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_dom_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, DOM_ParenthesizedExpression)

@given(instance=DOM_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_dom_conditionalexpression_instantiation(instance):
    assert isinstance(instance, DOM_ConditionalExpression)

@given(instance=DOM_NumberLiteral_strategy)
@settings(max_examples=50)
def test_dom_numberliteral_instantiation(instance):
    assert isinstance(instance, DOM_NumberLiteral)



@given(instance=DOM_NumberLiteral_strategy)
def test_dom_numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=DOM_CastExpression_strategy)
@settings(max_examples=50)
def test_dom_castexpression_instantiation(instance):
    assert isinstance(instance, DOM_CastExpression)

@given(instance=DOM_ThisExpression_strategy)
@settings(max_examples=50)
def test_dom_thisexpression_instantiation(instance):
    assert isinstance(instance, DOM_ThisExpression)

@given(instance=DOM_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_dom_booleanliteral_instantiation(instance):
    assert isinstance(instance, DOM_BooleanLiteral)



@given(instance=DOM_BooleanLiteral_strategy)
def test_dom_booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=DOM_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_dom_characterliteral_instantiation(instance):
    assert isinstance(instance, DOM_CharacterLiteral)



@given(instance=DOM_CharacterLiteral_strategy)
def test_dom_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=DOM_CharacterLiteral_strategy)
def test_dom_characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=DOM_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_dom_arrayinitializer_instantiation(instance):
    assert isinstance(instance, DOM_ArrayInitializer)

@given(instance=DOM_StringLiteral_strategy)
@settings(max_examples=50)
def test_dom_stringliteral_instantiation(instance):
    assert isinstance(instance, DOM_StringLiteral)



@given(instance=DOM_StringLiteral_strategy)
def test_dom_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=DOM_StringLiteral_strategy)
def test_dom_stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=DOM_InfixExpression_strategy)
@settings(max_examples=50)
def test_dom_infixexpression_instantiation(instance):
    assert isinstance(instance, DOM_InfixExpression)



@given(instance=DOM_InfixExpression_strategy)
def test_dom_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclarationExpression)

@given(instance=DOM_Assignment_strategy)
@settings(max_examples=50)
def test_dom_assignment_instantiation(instance):
    assert isinstance(instance, DOM_Assignment)



@given(instance=DOM_Assignment_strategy)
def test_dom_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM_SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_dom_superfieldaccess_instantiation(instance):
    assert isinstance(instance, DOM_SuperFieldAccess)

@given(instance=DOM_MethodInvocation_strategy)
@settings(max_examples=50)
def test_dom_methodinvocation_instantiation(instance):
    assert isinstance(instance, DOM_MethodInvocation)

@given(instance=DOM_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_dom_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, DOM_SuperMethodInvocation)

@given(instance=DOM_ArrayCreation_strategy)
@settings(max_examples=50)
def test_dom_arraycreation_instantiation(instance):
    assert isinstance(instance, DOM_ArrayCreation)

@given(instance=DOM_ArrayAccess_strategy)
@settings(max_examples=50)
def test_dom_arrayaccess_instantiation(instance):
    assert isinstance(instance, DOM_ArrayAccess)

@given(instance=DOM_FieldAccess_strategy)
@settings(max_examples=50)
def test_dom_fieldaccess_instantiation(instance):
    assert isinstance(instance, DOM_FieldAccess)

@given(instance=DOM_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_dom_classinstancecreation_instantiation(instance):
    assert isinstance(instance, DOM_ClassInstanceCreation)

@given(instance=DOM_PrefixExpression_strategy)
@settings(max_examples=50)
def test_dom_prefixexpression_instantiation(instance):
    assert isinstance(instance, DOM_PrefixExpression)



@given(instance=DOM_PrefixExpression_strategy)
def test_dom_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM_PostfixExpression_strategy)
@settings(max_examples=50)
def test_dom_postfixexpression_instantiation(instance):
    assert isinstance(instance, DOM_PostfixExpression)



@given(instance=DOM_PostfixExpression_strategy)
def test_dom_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=DOM_InstanceofExpression_strategy)
@settings(max_examples=50)
def test_dom_instanceofexpression_instantiation(instance):
    assert isinstance(instance, DOM_InstanceofExpression)

@given(instance=DOM_TypeLiteral_strategy)
@settings(max_examples=50)
def test_dom_typeliteral_instantiation(instance):
    assert isinstance(instance, DOM_TypeLiteral)

@given(instance=DOM_NullLiteral_strategy)
@settings(max_examples=50)
def test_dom_nullliteral_instantiation(instance):
    assert isinstance(instance, DOM_NullLiteral)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=DOM_LineComment_strategy)
@settings(max_examples=50)
def test_dom_linecomment_instantiation(instance):
    assert isinstance(instance, DOM_LineComment)

@given(instance=DOM_BlockComment_strategy)
@settings(max_examples=50)
def test_dom_blockcomment_instantiation(instance):
    assert isinstance(instance, DOM_BlockComment)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=DOM_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AnnotationTypeDeclaration)

@given(instance=DOM_IMethod_strategy)
@settings(max_examples=50)
def test_dom_imethod_instantiation(instance):
    assert isinstance(instance, DOM_IMethod)

@given(instance=DOM_VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_dom_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclarationFragment)

@given(instance=DOM_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom_typedeclaration_instantiation(instance):
    assert isinstance(instance, DOM_TypeDeclaration)



@given(instance=DOM_TypeDeclaration_strategy)
def test_dom_typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=DOM_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_dom_enumdeclaration_instantiation(instance):
    assert isinstance(instance, DOM_EnumDeclaration)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=DOM_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_dom_methoddeclaration_instantiation(instance):
    assert isinstance(instance, DOM_MethodDeclaration)



@given(instance=DOM_MethodDeclaration_strategy)
def test_dom_methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original



@given(instance=DOM_MethodDeclaration_strategy)
def test_dom_methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original



@given(instance=DOM_MethodDeclaration_strategy)
def test_dom_methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=DOM_Initializer_strategy)
@settings(max_examples=50)
def test_dom_initializer_instantiation(instance):
    assert isinstance(instance, DOM_Initializer)

@given(instance=DOM_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_dom_fielddeclaration_instantiation(instance):
    assert isinstance(instance, DOM_FieldDeclaration)

@given(instance=DOM_IPackageFragment_strategy)
@settings(max_examples=50)
def test_dom_ipackagefragment_instantiation(instance):
    assert isinstance(instance, DOM_IPackageFragment)

@given(instance=DOM_EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_dom_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, DOM_EnumConstantDeclaration)

@given(instance=DOM_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_dom_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AnnotationTypeMemberDeclaration)

@given(instance=ExtendedModifier_strategy)
@settings(max_examples=50)
def test_extendedmodifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)

@given(instance=DOM_Annotation_strategy)
@settings(max_examples=50)
def test_dom_annotation_instantiation(instance):
    assert isinstance(instance, DOM_Annotation)

@given(instance=DOM_SimpleName_strategy)
@settings(max_examples=50)
def test_dom_simplename_instantiation(instance):
    assert isinstance(instance, DOM_SimpleName)



@given(instance=DOM_SimpleName_strategy)
def test_dom_simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=DOM_SimpleName_strategy)
def test_dom_simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=DOM_Name_strategy)
@settings(max_examples=50)
def test_dom_name_instantiation(instance):
    assert isinstance(instance, DOM_Name)



@given(instance=DOM_Name_strategy)
def test_dom_name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original

@given(instance=DOM_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dom_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AbstractTypeDeclaration)



@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_dom_abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original



@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_dom_abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original



@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_dom_abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original

@given(instance=DOM_SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_dom_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, DOM_SingleVariableDeclaration)



@given(instance=DOM_SingleVariableDeclaration_strategy)
def test_dom_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=DOM_Block_strategy)
@settings(max_examples=50)
def test_dom_block_instantiation(instance):
    assert isinstance(instance, DOM_Block)

@given(instance=DOM_Javadoc_strategy)
@settings(max_examples=50)
def test_dom_javadoc_instantiation(instance):
    assert isinstance(instance, DOM_Javadoc)

@given(instance=DOM_ExtendedModifier_strategy)
@settings(max_examples=50)
def test_dom_extendedmodifier_instantiation(instance):
    assert isinstance(instance, DOM_ExtendedModifier)

@given(instance=DOM_IType_strategy)
@settings(max_examples=50)
def test_dom_itype_instantiation(instance):
    assert isinstance(instance, DOM_IType)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=DOM_MethodRef_strategy)
@settings(max_examples=50)
def test_dom_methodref_instantiation(instance):
    assert isinstance(instance, DOM_MethodRef)

@given(instance=DOM_MemberValuePair_strategy)
@settings(max_examples=50)
def test_dom_membervaluepair_instantiation(instance):
    assert isinstance(instance, DOM_MemberValuePair)

@given(instance=DOM_TagElement_strategy)
@settings(max_examples=50)
def test_dom_tagelement_instantiation(instance):
    assert isinstance(instance, DOM_TagElement)



@given(instance=DOM_TagElement_strategy)
def test_dom_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=DOM_TagElement_strategy)
def test_dom_tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original

@given(instance=DOM_CompilationUnit_strategy)
@settings(max_examples=50)
def test_dom_compilationunit_instantiation(instance):
    assert isinstance(instance, DOM_CompilationUnit)

@given(instance=DOM_Statement_strategy)
@settings(max_examples=50)
def test_dom_statement_instantiation(instance):
    assert isinstance(instance, DOM_Statement)

@given(instance=DOM_Expression_strategy)
@settings(max_examples=50)
def test_dom_expression_instantiation(instance):
    assert isinstance(instance, DOM_Expression)



@given(instance=DOM_Expression_strategy)
def test_dom_expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original



@given(instance=DOM_Expression_strategy)
def test_dom_expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original

@given(instance=DOM_CatchClause_strategy)
@settings(max_examples=50)
def test_dom_catchclause_instantiation(instance):
    assert isinstance(instance, DOM_CatchClause)

@given(instance=DOM_Type_strategy)
@settings(max_examples=50)
def test_dom_type_instantiation(instance):
    assert isinstance(instance, DOM_Type)

@given(instance=DOM_MemberRef_strategy)
@settings(max_examples=50)
def test_dom_memberref_instantiation(instance):
    assert isinstance(instance, DOM_MemberRef)

@given(instance=DOM_Modifier_strategy)
@settings(max_examples=50)
def test_dom_modifier_instantiation(instance):
    assert isinstance(instance, DOM_Modifier)



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=DOM_Modifier_strategy)
def test_dom_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=DOM_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_dom_bodydeclaration_instantiation(instance):
    assert isinstance(instance, DOM_BodyDeclaration)

@given(instance=DOM_Comment_strategy)
@settings(max_examples=50)
def test_dom_comment_instantiation(instance):
    assert isinstance(instance, DOM_Comment)

@given(instance=DOM_TextElement_strategy)
@settings(max_examples=50)
def test_dom_textelement_instantiation(instance):
    assert isinstance(instance, DOM_TextElement)



@given(instance=DOM_TextElement_strategy)
def test_dom_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=DOM_TypeParameter_strategy)
@settings(max_examples=50)
def test_dom_typeparameter_instantiation(instance):
    assert isinstance(instance, DOM_TypeParameter)

@given(instance=DOM_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_dom_variabledeclaration_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclaration)



@given(instance=DOM_VariableDeclaration_strategy)
def test_dom_variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original

@given(instance=DOM_MethodRefParameter_strategy)
@settings(max_examples=50)
def test_dom_methodrefparameter_instantiation(instance):
    assert isinstance(instance, DOM_MethodRefParameter)



@given(instance=DOM_MethodRefParameter_strategy)
def test_dom_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=DOM_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_dom_packagedeclaration_instantiation(instance):
    assert isinstance(instance, DOM_PackageDeclaration)

@given(instance=DOM_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_dom_importdeclaration_instantiation(instance):
    assert isinstance(instance, DOM_ImportDeclaration)



@given(instance=DOM_ImportDeclaration_strategy)
def test_dom_importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original



@given(instance=DOM_ImportDeclaration_strategy)
def test_dom_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=DOM_AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_dom_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AnonymousClassDeclaration)

@given(instance=DOM_ASTNode_strategy)
@settings(max_examples=50)
def test_dom_astnode_instantiation(instance):
    assert isinstance(instance, DOM_ASTNode)

@given(instance=DOM_AST_strategy)
@settings(max_examples=50)
def test_dom_ast_instantiation(instance):
    assert isinstance(instance, DOM_AST)
