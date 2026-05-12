import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RangeLiteral,
    amethyst_CharRangeLiteral,
    amethyst_NumberRangeLiteral,
    Symbol,
    amethyst_ParameterDeclaration,
    amethyst_DefinitionDeclaration,
    amethyst_ForInitializerDeclaration,
    amethyst_TagLoopInitializerDeclaration,
    amethyst_VariableDeclaration,
    amethyst_ClassDeclaration,
    PrimitiveType,
    amethyst_FloatType,
    amethyst_IntType,
    amethyst_StringType,
    amethyst_DefinitionType,
    amethyst_BooleanType,
    amethyst_AnyType,
    amethyst_CharType,
    Type,
    amethyst_PrimitiveType,
    AbstractType,
    amethyst_ArrayType,
    amethyst_Type,
    amethyst_AbstractType,
    Literal,
    amethyst_BooleanLiteral,
    amethyst_NullLiteral,
    amethyst_FloatLiteral,
    amethyst_RangeLiteral,
    amethyst_IntLiteral,
    amethyst_StringLiteral,
    amethyst_CharLiteral,
    Expression,
    amethyst_ShiftExpression,
    amethyst_AndExpression,
    amethyst_CallExpression,
    amethyst_AdditiveExpression,
    amethyst_MatchingExpression,
    amethyst_SuperExpression,
    amethyst_ParenthisedExpression,
    amethyst_SelfExpression,
    amethyst_TypeCastExpression,
    amethyst_IndexAccessExpression,
    amethyst_InExpression,
    amethyst_MultiplicativeExpression,
    amethyst_AssignmentExpression,
    amethyst_MemberAccessExpression,
    amethyst_UnaryMinusExpression,
    amethyst_EqualityExpression,
    amethyst_NotExpression,
    amethyst_RelationalExpression,
    amethyst_Literal,
    amethyst_OrExpression,
    amethyst_NewExpression,
    amethyst_SymbolReference,
    amethyst_TagExpression,
    amethyst_EObject,
    amethyst_TagAttribute,
    amethyst_TagLoopExpression,
    amethyst_ClassType,
    amethyst_TagDeclaration,
    Statement,
    amethyst_ElseIfStatement,
    amethyst_BreakStatement,
    amethyst_ForStatement,
    amethyst_CaseElseStatement,
    amethyst_JsCodeStatement,
    amethyst_Expression,
    amethyst_WhenStatement,
    amethyst_IfStatement,
    amethyst_ElseStatement,
    amethyst_NextStatement,
    amethyst_CaseStatement,
    amethyst_ReturnStatement,
    amethyst_WhileStatement,
    amethyst_Symbol,
    amethyst_Statement,
    amethyst_Import,
    amethyst_Module,
    amethyst_PropertyDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rangeliteral_is_not_abstract():
    assert not inspect.isabstract(RangeLiteral)


def test_rangeliteral_constructor_exists():
    assert callable(RangeLiteral.__init__)


def test_rangeliteral_constructor_args():
    sig = inspect.signature(RangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_charrangeliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_CharRangeLiteral)


def test_amethyst_charrangeliteral_constructor_exists():
    assert callable(amethyst_CharRangeLiteral.__init__)


def test_amethyst_charrangeliteral_constructor_args():
    sig = inspect.signature(amethyst_CharRangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_numberrangeliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_NumberRangeLiteral)


def test_amethyst_numberrangeliteral_constructor_exists():
    assert callable(amethyst_NumberRangeLiteral.__init__)


def test_amethyst_numberrangeliteral_constructor_args():
    sig = inspect.signature(amethyst_NumberRangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_ParameterDeclaration)


def test_amethyst_parameterdeclaration_constructor_exists():
    assert callable(amethyst_ParameterDeclaration.__init__)


def test_amethyst_parameterdeclaration_constructor_args():
    sig = inspect.signature(amethyst_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_definitiondeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_DefinitionDeclaration)


def test_amethyst_definitiondeclaration_constructor_exists():
    assert callable(amethyst_DefinitionDeclaration.__init__)


def test_amethyst_definitiondeclaration_constructor_args():
    sig = inspect.signature(amethyst_DefinitionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_amethyst_definitiondeclaration_has_static():
    assert hasattr(amethyst_DefinitionDeclaration, "static")
    descriptor = None
    for klass in amethyst_DefinitionDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_forinitializerdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_ForInitializerDeclaration)


def test_amethyst_forinitializerdeclaration_constructor_exists():
    assert callable(amethyst_ForInitializerDeclaration.__init__)


def test_amethyst_forinitializerdeclaration_constructor_args():
    sig = inspect.signature(amethyst_ForInitializerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_tagloopinitializerdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagLoopInitializerDeclaration)


def test_amethyst_tagloopinitializerdeclaration_constructor_exists():
    assert callable(amethyst_TagLoopInitializerDeclaration.__init__)


def test_amethyst_tagloopinitializerdeclaration_constructor_args():
    sig = inspect.signature(amethyst_TagLoopInitializerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_VariableDeclaration)


def test_amethyst_variabledeclaration_constructor_exists():
    assert callable(amethyst_VariableDeclaration.__init__)


def test_amethyst_variabledeclaration_constructor_args():
    sig = inspect.signature(amethyst_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_ClassDeclaration)


def test_amethyst_classdeclaration_constructor_exists():
    assert callable(amethyst_ClassDeclaration.__init__)


def test_amethyst_classdeclaration_constructor_args():
    sig = inspect.signature(amethyst_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_floattype_is_not_abstract():
    assert not inspect.isabstract(amethyst_FloatType)


def test_amethyst_floattype_constructor_exists():
    assert callable(amethyst_FloatType.__init__)


def test_amethyst_floattype_constructor_args():
    sig = inspect.signature(amethyst_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_inttype_is_not_abstract():
    assert not inspect.isabstract(amethyst_IntType)


def test_amethyst_inttype_constructor_exists():
    assert callable(amethyst_IntType.__init__)


def test_amethyst_inttype_constructor_args():
    sig = inspect.signature(amethyst_IntType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_stringtype_is_not_abstract():
    assert not inspect.isabstract(amethyst_StringType)


def test_amethyst_stringtype_constructor_exists():
    assert callable(amethyst_StringType.__init__)


def test_amethyst_stringtype_constructor_args():
    sig = inspect.signature(amethyst_StringType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_definitiontype_is_not_abstract():
    assert not inspect.isabstract(amethyst_DefinitionType)


def test_amethyst_definitiontype_constructor_exists():
    assert callable(amethyst_DefinitionType.__init__)


def test_amethyst_definitiontype_constructor_args():
    sig = inspect.signature(amethyst_DefinitionType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_booleantype_is_not_abstract():
    assert not inspect.isabstract(amethyst_BooleanType)


def test_amethyst_booleantype_constructor_exists():
    assert callable(amethyst_BooleanType.__init__)


def test_amethyst_booleantype_constructor_args():
    sig = inspect.signature(amethyst_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_anytype_is_not_abstract():
    assert not inspect.isabstract(amethyst_AnyType)


def test_amethyst_anytype_constructor_exists():
    assert callable(amethyst_AnyType.__init__)


def test_amethyst_anytype_constructor_args():
    sig = inspect.signature(amethyst_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_chartype_is_not_abstract():
    assert not inspect.isabstract(amethyst_CharType)


def test_amethyst_chartype_constructor_exists():
    assert callable(amethyst_CharType.__init__)


def test_amethyst_chartype_constructor_args():
    sig = inspect.signature(amethyst_CharType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_primitivetype_is_not_abstract():
    assert not inspect.isabstract(amethyst_PrimitiveType)


def test_amethyst_primitivetype_constructor_exists():
    assert callable(amethyst_PrimitiveType.__init__)


def test_amethyst_primitivetype_constructor_args():
    sig = inspect.signature(amethyst_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_arraytype_is_not_abstract():
    assert not inspect.isabstract(amethyst_ArrayType)


def test_amethyst_arraytype_constructor_exists():
    assert callable(amethyst_ArrayType.__init__)


def test_amethyst_arraytype_constructor_args():
    sig = inspect.signature(amethyst_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_type_is_not_abstract():
    assert not inspect.isabstract(amethyst_Type)


def test_amethyst_type_constructor_exists():
    assert callable(amethyst_Type.__init__)


def test_amethyst_type_constructor_args():
    sig = inspect.signature(amethyst_Type.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_abstracttype_is_not_abstract():
    assert not inspect.isabstract(amethyst_AbstractType)


def test_amethyst_abstracttype_constructor_exists():
    assert callable(amethyst_AbstractType.__init__)


def test_amethyst_abstracttype_constructor_args():
    sig = inspect.signature(amethyst_AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_BooleanLiteral)


def test_amethyst_booleanliteral_constructor_exists():
    assert callable(amethyst_BooleanLiteral.__init__)


def test_amethyst_booleanliteral_constructor_args():
    sig = inspect.signature(amethyst_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_amethyst_booleanliteral_has_value():
    assert hasattr(amethyst_BooleanLiteral, "value")
    descriptor = None
    for klass in amethyst_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_nullliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_NullLiteral)


def test_amethyst_nullliteral_constructor_exists():
    assert callable(amethyst_NullLiteral.__init__)


def test_amethyst_nullliteral_constructor_args():
    sig = inspect.signature(amethyst_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_floatliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_FloatLiteral)


def test_amethyst_floatliteral_constructor_exists():
    assert callable(amethyst_FloatLiteral.__init__)


def test_amethyst_floatliteral_constructor_args():
    sig = inspect.signature(amethyst_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_amethyst_floatliteral_has_value():
    assert hasattr(amethyst_FloatLiteral, "value")
    descriptor = None
    for klass in amethyst_FloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_rangeliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_RangeLiteral)


def test_amethyst_rangeliteral_constructor_exists():
    assert callable(amethyst_RangeLiteral.__init__)


def test_amethyst_rangeliteral_constructor_args():
    sig = inspect.signature(amethyst_RangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_intliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_IntLiteral)


def test_amethyst_intliteral_constructor_exists():
    assert callable(amethyst_IntLiteral.__init__)


def test_amethyst_intliteral_constructor_args():
    sig = inspect.signature(amethyst_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_amethyst_intliteral_has_value():
    assert hasattr(amethyst_IntLiteral, "value")
    descriptor = None
    for klass in amethyst_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_stringliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_StringLiteral)


def test_amethyst_stringliteral_constructor_exists():
    assert callable(amethyst_StringLiteral.__init__)


def test_amethyst_stringliteral_constructor_args():
    sig = inspect.signature(amethyst_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_amethyst_stringliteral_has_value():
    assert hasattr(amethyst_StringLiteral, "value")
    descriptor = None
    for klass in amethyst_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_charliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_CharLiteral)


def test_amethyst_charliteral_constructor_exists():
    assert callable(amethyst_CharLiteral.__init__)


def test_amethyst_charliteral_constructor_args():
    sig = inspect.signature(amethyst_CharLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_amethyst_charliteral_has_value():
    assert hasattr(amethyst_CharLiteral, "value")
    descriptor = None
    for klass in amethyst_CharLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_ShiftExpression)


def test_amethyst_shiftexpression_constructor_exists():
    assert callable(amethyst_ShiftExpression.__init__)


def test_amethyst_shiftexpression_constructor_args():
    sig = inspect.signature(amethyst_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_amethyst_shiftexpression_has_operator():
    assert hasattr(amethyst_ShiftExpression, "operator")
    descriptor = None
    for klass in amethyst_ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_andexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_AndExpression)


def test_amethyst_andexpression_constructor_exists():
    assert callable(amethyst_AndExpression.__init__)


def test_amethyst_andexpression_constructor_args():
    sig = inspect.signature(amethyst_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_callexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_CallExpression)


def test_amethyst_callexpression_constructor_exists():
    assert callable(amethyst_CallExpression.__init__)


def test_amethyst_callexpression_constructor_args():
    sig = inspect.signature(amethyst_CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_AdditiveExpression)


def test_amethyst_additiveexpression_constructor_exists():
    assert callable(amethyst_AdditiveExpression.__init__)


def test_amethyst_additiveexpression_constructor_args():
    sig = inspect.signature(amethyst_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_amethyst_additiveexpression_has_operator():
    assert hasattr(amethyst_AdditiveExpression, "operator")
    descriptor = None
    for klass in amethyst_AdditiveExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_matchingexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_MatchingExpression)


def test_amethyst_matchingexpression_constructor_exists():
    assert callable(amethyst_MatchingExpression.__init__)


def test_amethyst_matchingexpression_constructor_args():
    sig = inspect.signature(amethyst_MatchingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_amethyst_matchingexpression_has_operator():
    assert hasattr(amethyst_MatchingExpression, "operator")
    descriptor = None
    for klass in amethyst_MatchingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_superexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_SuperExpression)


def test_amethyst_superexpression_constructor_exists():
    assert callable(amethyst_SuperExpression.__init__)


def test_amethyst_superexpression_constructor_args():
    sig = inspect.signature(amethyst_SuperExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_parenthisedexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_ParenthisedExpression)


def test_amethyst_parenthisedexpression_constructor_exists():
    assert callable(amethyst_ParenthisedExpression.__init__)


def test_amethyst_parenthisedexpression_constructor_args():
    sig = inspect.signature(amethyst_ParenthisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_selfexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_SelfExpression)


def test_amethyst_selfexpression_constructor_exists():
    assert callable(amethyst_SelfExpression.__init__)


def test_amethyst_selfexpression_constructor_args():
    sig = inspect.signature(amethyst_SelfExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_typecastexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_TypeCastExpression)


def test_amethyst_typecastexpression_constructor_exists():
    assert callable(amethyst_TypeCastExpression.__init__)


def test_amethyst_typecastexpression_constructor_args():
    sig = inspect.signature(amethyst_TypeCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_indexaccessexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_IndexAccessExpression)


def test_amethyst_indexaccessexpression_constructor_exists():
    assert callable(amethyst_IndexAccessExpression.__init__)


def test_amethyst_indexaccessexpression_constructor_args():
    sig = inspect.signature(amethyst_IndexAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_inexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_InExpression)


def test_amethyst_inexpression_constructor_exists():
    assert callable(amethyst_InExpression.__init__)


def test_amethyst_inexpression_constructor_args():
    sig = inspect.signature(amethyst_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_MultiplicativeExpression)


def test_amethyst_multiplicativeexpression_constructor_exists():
    assert callable(amethyst_MultiplicativeExpression.__init__)


def test_amethyst_multiplicativeexpression_constructor_args():
    sig = inspect.signature(amethyst_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_amethyst_multiplicativeexpression_has_operator():
    assert hasattr(amethyst_MultiplicativeExpression, "operator")
    descriptor = None
    for klass in amethyst_MultiplicativeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_AssignmentExpression)


def test_amethyst_assignmentexpression_constructor_exists():
    assert callable(amethyst_AssignmentExpression.__init__)


def test_amethyst_assignmentexpression_constructor_args():
    sig = inspect.signature(amethyst_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_memberaccessexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_MemberAccessExpression)


def test_amethyst_memberaccessexpression_constructor_exists():
    assert callable(amethyst_MemberAccessExpression.__init__)


def test_amethyst_memberaccessexpression_constructor_args():
    sig = inspect.signature(amethyst_MemberAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_UnaryMinusExpression)


def test_amethyst_unaryminusexpression_constructor_exists():
    assert callable(amethyst_UnaryMinusExpression.__init__)


def test_amethyst_unaryminusexpression_constructor_args():
    sig = inspect.signature(amethyst_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_EqualityExpression)


def test_amethyst_equalityexpression_constructor_exists():
    assert callable(amethyst_EqualityExpression.__init__)


def test_amethyst_equalityexpression_constructor_args():
    sig = inspect.signature(amethyst_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_amethyst_equalityexpression_has_operator():
    assert hasattr(amethyst_EqualityExpression, "operator")
    descriptor = None
    for klass in amethyst_EqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_notexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_NotExpression)


def test_amethyst_notexpression_constructor_exists():
    assert callable(amethyst_NotExpression.__init__)


def test_amethyst_notexpression_constructor_args():
    sig = inspect.signature(amethyst_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_RelationalExpression)


def test_amethyst_relationalexpression_constructor_exists():
    assert callable(amethyst_RelationalExpression.__init__)


def test_amethyst_relationalexpression_constructor_args():
    sig = inspect.signature(amethyst_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_amethyst_relationalexpression_has_operator():
    assert hasattr(amethyst_RelationalExpression, "operator")
    descriptor = None
    for klass in amethyst_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_literal_is_not_abstract():
    assert not inspect.isabstract(amethyst_Literal)


def test_amethyst_literal_constructor_exists():
    assert callable(amethyst_Literal.__init__)


def test_amethyst_literal_constructor_args():
    sig = inspect.signature(amethyst_Literal.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_orexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_OrExpression)


def test_amethyst_orexpression_constructor_exists():
    assert callable(amethyst_OrExpression.__init__)


def test_amethyst_orexpression_constructor_args():
    sig = inspect.signature(amethyst_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_newexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_NewExpression)


def test_amethyst_newexpression_constructor_exists():
    assert callable(amethyst_NewExpression.__init__)


def test_amethyst_newexpression_constructor_args():
    sig = inspect.signature(amethyst_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_symbolreference_is_not_abstract():
    assert not inspect.isabstract(amethyst_SymbolReference)


def test_amethyst_symbolreference_constructor_exists():
    assert callable(amethyst_SymbolReference.__init__)


def test_amethyst_symbolreference_constructor_args():
    sig = inspect.signature(amethyst_SymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_tagexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagExpression)


def test_amethyst_tagexpression_constructor_exists():
    assert callable(amethyst_TagExpression.__init__)


def test_amethyst_tagexpression_constructor_args():
    sig = inspect.signature(amethyst_TagExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_eobject_is_not_abstract():
    assert not inspect.isabstract(amethyst_EObject)


def test_amethyst_eobject_constructor_exists():
    assert callable(amethyst_EObject.__init__)


def test_amethyst_eobject_constructor_args():
    sig = inspect.signature(amethyst_EObject.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_tagattribute_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagAttribute)


def test_amethyst_tagattribute_constructor_exists():
    assert callable(amethyst_TagAttribute.__init__)


def test_amethyst_tagattribute_constructor_args():
    sig = inspect.signature(amethyst_TagAttribute.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_tagloopexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagLoopExpression)


def test_amethyst_tagloopexpression_constructor_exists():
    assert callable(amethyst_TagLoopExpression.__init__)


def test_amethyst_tagloopexpression_constructor_args():
    sig = inspect.signature(amethyst_TagLoopExpression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_classtype_is_not_abstract():
    assert not inspect.isabstract(amethyst_ClassType)


def test_amethyst_classtype_constructor_exists():
    assert callable(amethyst_ClassType.__init__)


def test_amethyst_classtype_constructor_args():
    sig = inspect.signature(amethyst_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_tagdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagDeclaration)


def test_amethyst_tagdeclaration_constructor_exists():
    assert callable(amethyst_TagDeclaration.__init__)


def test_amethyst_tagdeclaration_constructor_args():
    sig = inspect.signature(amethyst_TagDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_elseifstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ElseIfStatement)


def test_amethyst_elseifstatement_constructor_exists():
    assert callable(amethyst_ElseIfStatement.__init__)


def test_amethyst_elseifstatement_constructor_args():
    sig = inspect.signature(amethyst_ElseIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_breakstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_BreakStatement)


def test_amethyst_breakstatement_constructor_exists():
    assert callable(amethyst_BreakStatement.__init__)


def test_amethyst_breakstatement_constructor_args():
    sig = inspect.signature(amethyst_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_forstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ForStatement)


def test_amethyst_forstatement_constructor_exists():
    assert callable(amethyst_ForStatement.__init__)


def test_amethyst_forstatement_constructor_args():
    sig = inspect.signature(amethyst_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_caseelsestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_CaseElseStatement)


def test_amethyst_caseelsestatement_constructor_exists():
    assert callable(amethyst_CaseElseStatement.__init__)


def test_amethyst_caseelsestatement_constructor_args():
    sig = inspect.signature(amethyst_CaseElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_jscodestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_JsCodeStatement)


def test_amethyst_jscodestatement_constructor_exists():
    assert callable(amethyst_JsCodeStatement.__init__)


def test_amethyst_jscodestatement_constructor_args():
    sig = inspect.signature(amethyst_JsCodeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_amethyst_jscodestatement_has_value():
    assert hasattr(amethyst_JsCodeStatement, "value")
    descriptor = None
    for klass in amethyst_JsCodeStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_expression_is_not_abstract():
    assert not inspect.isabstract(amethyst_Expression)


def test_amethyst_expression_constructor_exists():
    assert callable(amethyst_Expression.__init__)


def test_amethyst_expression_constructor_args():
    sig = inspect.signature(amethyst_Expression.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_whenstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_WhenStatement)


def test_amethyst_whenstatement_constructor_exists():
    assert callable(amethyst_WhenStatement.__init__)


def test_amethyst_whenstatement_constructor_args():
    sig = inspect.signature(amethyst_WhenStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_ifstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_IfStatement)


def test_amethyst_ifstatement_constructor_exists():
    assert callable(amethyst_IfStatement.__init__)


def test_amethyst_ifstatement_constructor_args():
    sig = inspect.signature(amethyst_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_elsestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ElseStatement)


def test_amethyst_elsestatement_constructor_exists():
    assert callable(amethyst_ElseStatement.__init__)


def test_amethyst_elsestatement_constructor_args():
    sig = inspect.signature(amethyst_ElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_nextstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_NextStatement)


def test_amethyst_nextstatement_constructor_exists():
    assert callable(amethyst_NextStatement.__init__)


def test_amethyst_nextstatement_constructor_args():
    sig = inspect.signature(amethyst_NextStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_casestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_CaseStatement)


def test_amethyst_casestatement_constructor_exists():
    assert callable(amethyst_CaseStatement.__init__)


def test_amethyst_casestatement_constructor_args():
    sig = inspect.signature(amethyst_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_returnstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ReturnStatement)


def test_amethyst_returnstatement_constructor_exists():
    assert callable(amethyst_ReturnStatement.__init__)


def test_amethyst_returnstatement_constructor_args():
    sig = inspect.signature(amethyst_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_whilestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_WhileStatement)


def test_amethyst_whilestatement_constructor_exists():
    assert callable(amethyst_WhileStatement.__init__)


def test_amethyst_whilestatement_constructor_args():
    sig = inspect.signature(amethyst_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_symbol_is_not_abstract():
    assert not inspect.isabstract(amethyst_Symbol)


def test_amethyst_symbol_constructor_exists():
    assert callable(amethyst_Symbol.__init__)


def test_amethyst_symbol_constructor_args():
    sig = inspect.signature(amethyst_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amethyst_symbol_has_name():
    assert hasattr(amethyst_Symbol, "name")
    descriptor = None
    for klass in amethyst_Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_statement_is_not_abstract():
    assert not inspect.isabstract(amethyst_Statement)


def test_amethyst_statement_constructor_exists():
    assert callable(amethyst_Statement.__init__)


def test_amethyst_statement_constructor_args():
    sig = inspect.signature(amethyst_Statement.__init__)
    params = list(sig.parameters.keys())



def test_amethyst_import_is_not_abstract():
    assert not inspect.isabstract(amethyst_Import)


def test_amethyst_import_constructor_exists():
    assert callable(amethyst_Import.__init__)


def test_amethyst_import_constructor_args():
    sig = inspect.signature(amethyst_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_amethyst_import_has_importedNamespace():
    assert hasattr(amethyst_Import, "importedNamespace")
    descriptor = None
    for klass in amethyst_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_module_is_not_abstract():
    assert not inspect.isabstract(amethyst_Module)


def test_amethyst_module_constructor_exists():
    assert callable(amethyst_Module.__init__)


def test_amethyst_module_constructor_args():
    sig = inspect.signature(amethyst_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amethyst_module_has_name():
    assert hasattr(amethyst_Module, "name")
    descriptor = None
    for klass in amethyst_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_amethyst_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_PropertyDeclaration)


def test_amethyst_propertydeclaration_constructor_exists():
    assert callable(amethyst_PropertyDeclaration.__init__)


def test_amethyst_propertydeclaration_constructor_args():
    sig = inspect.signature(amethyst_PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())


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
RangeLiteral_strategy = st.builds(
    RangeLiteral,
)
amethyst_CharRangeLiteral_strategy = st.builds(
    amethyst_CharRangeLiteral,
)
amethyst_NumberRangeLiteral_strategy = st.builds(
    amethyst_NumberRangeLiteral,
)
Symbol_strategy = st.builds(
    Symbol,
)
amethyst_ParameterDeclaration_strategy = st.builds(
    amethyst_ParameterDeclaration,
)
amethyst_DefinitionDeclaration_strategy = st.builds(
    amethyst_DefinitionDeclaration,
    static=
        st.booleans()
)
amethyst_ForInitializerDeclaration_strategy = st.builds(
    amethyst_ForInitializerDeclaration,
)
amethyst_TagLoopInitializerDeclaration_strategy = st.builds(
    amethyst_TagLoopInitializerDeclaration,
)
amethyst_VariableDeclaration_strategy = st.builds(
    amethyst_VariableDeclaration,
)
amethyst_ClassDeclaration_strategy = st.builds(
    amethyst_ClassDeclaration,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
amethyst_FloatType_strategy = st.builds(
    amethyst_FloatType,
)
amethyst_IntType_strategy = st.builds(
    amethyst_IntType,
)
amethyst_StringType_strategy = st.builds(
    amethyst_StringType,
)
amethyst_DefinitionType_strategy = st.builds(
    amethyst_DefinitionType,
)
amethyst_BooleanType_strategy = st.builds(
    amethyst_BooleanType,
)
amethyst_AnyType_strategy = st.builds(
    amethyst_AnyType,
)
amethyst_CharType_strategy = st.builds(
    amethyst_CharType,
)
Type_strategy = st.builds(
    Type,
)
amethyst_PrimitiveType_strategy = st.builds(
    amethyst_PrimitiveType,
)
AbstractType_strategy = st.builds(
    AbstractType,
)
amethyst_ArrayType_strategy = st.builds(
    amethyst_ArrayType,
)
amethyst_Type_strategy = st.builds(
    amethyst_Type,
)
amethyst_AbstractType_strategy = st.builds(
    amethyst_AbstractType,
)
Literal_strategy = st.builds(
    Literal,
)
amethyst_BooleanLiteral_strategy = st.builds(
    amethyst_BooleanLiteral,
    value=
        st.booleans()
)
amethyst_NullLiteral_strategy = st.builds(
    amethyst_NullLiteral,
)
amethyst_FloatLiteral_strategy = st.builds(
    amethyst_FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
amethyst_RangeLiteral_strategy = st.builds(
    amethyst_RangeLiteral,
)
amethyst_IntLiteral_strategy = st.builds(
    amethyst_IntLiteral,
    value=
        st.integers()
)
amethyst_StringLiteral_strategy = st.builds(
    amethyst_StringLiteral,
    value=
        safe_text
)
amethyst_CharLiteral_strategy = st.builds(
    amethyst_CharLiteral,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
amethyst_ShiftExpression_strategy = st.builds(
    amethyst_ShiftExpression,
    operator=
        safe_text
)
amethyst_AndExpression_strategy = st.builds(
    amethyst_AndExpression,
)
amethyst_CallExpression_strategy = st.builds(
    amethyst_CallExpression,
)
amethyst_AdditiveExpression_strategy = st.builds(
    amethyst_AdditiveExpression,
    operator=
        safe_text
)
amethyst_MatchingExpression_strategy = st.builds(
    amethyst_MatchingExpression,
    operator=
        safe_text
)
amethyst_SuperExpression_strategy = st.builds(
    amethyst_SuperExpression,
)
amethyst_ParenthisedExpression_strategy = st.builds(
    amethyst_ParenthisedExpression,
)
amethyst_SelfExpression_strategy = st.builds(
    amethyst_SelfExpression,
)
amethyst_TypeCastExpression_strategy = st.builds(
    amethyst_TypeCastExpression,
)
amethyst_IndexAccessExpression_strategy = st.builds(
    amethyst_IndexAccessExpression,
)
amethyst_InExpression_strategy = st.builds(
    amethyst_InExpression,
)
amethyst_MultiplicativeExpression_strategy = st.builds(
    amethyst_MultiplicativeExpression,
    operator=
        safe_text
)
amethyst_AssignmentExpression_strategy = st.builds(
    amethyst_AssignmentExpression,
)
amethyst_MemberAccessExpression_strategy = st.builds(
    amethyst_MemberAccessExpression,
)
amethyst_UnaryMinusExpression_strategy = st.builds(
    amethyst_UnaryMinusExpression,
)
amethyst_EqualityExpression_strategy = st.builds(
    amethyst_EqualityExpression,
    operator=
        safe_text
)
amethyst_NotExpression_strategy = st.builds(
    amethyst_NotExpression,
)
amethyst_RelationalExpression_strategy = st.builds(
    amethyst_RelationalExpression,
    operator=
        safe_text
)
amethyst_Literal_strategy = st.builds(
    amethyst_Literal,
)
amethyst_OrExpression_strategy = st.builds(
    amethyst_OrExpression,
)
amethyst_NewExpression_strategy = st.builds(
    amethyst_NewExpression,
)
amethyst_SymbolReference_strategy = st.builds(
    amethyst_SymbolReference,
)
amethyst_TagExpression_strategy = st.builds(
    amethyst_TagExpression,
)
amethyst_EObject_strategy = st.builds(
    amethyst_EObject,
)
amethyst_TagAttribute_strategy = st.builds(
    amethyst_TagAttribute,
)
amethyst_TagLoopExpression_strategy = st.builds(
    amethyst_TagLoopExpression,
)
amethyst_ClassType_strategy = st.builds(
    amethyst_ClassType,
)
amethyst_TagDeclaration_strategy = st.builds(
    amethyst_TagDeclaration,
)
Statement_strategy = st.builds(
    Statement,
)
amethyst_ElseIfStatement_strategy = st.builds(
    amethyst_ElseIfStatement,
)
amethyst_BreakStatement_strategy = st.builds(
    amethyst_BreakStatement,
)
amethyst_ForStatement_strategy = st.builds(
    amethyst_ForStatement,
)
amethyst_CaseElseStatement_strategy = st.builds(
    amethyst_CaseElseStatement,
)
amethyst_JsCodeStatement_strategy = st.builds(
    amethyst_JsCodeStatement,
    value=
        safe_text
)
amethyst_Expression_strategy = st.builds(
    amethyst_Expression,
)
amethyst_WhenStatement_strategy = st.builds(
    amethyst_WhenStatement,
)
amethyst_IfStatement_strategy = st.builds(
    amethyst_IfStatement,
)
amethyst_ElseStatement_strategy = st.builds(
    amethyst_ElseStatement,
)
amethyst_NextStatement_strategy = st.builds(
    amethyst_NextStatement,
)
amethyst_CaseStatement_strategy = st.builds(
    amethyst_CaseStatement,
)
amethyst_ReturnStatement_strategy = st.builds(
    amethyst_ReturnStatement,
)
amethyst_WhileStatement_strategy = st.builds(
    amethyst_WhileStatement,
)
amethyst_Symbol_strategy = st.builds(
    amethyst_Symbol,
    name=
        safe_text
)
amethyst_Statement_strategy = st.builds(
    amethyst_Statement,
)
amethyst_Import_strategy = st.builds(
    amethyst_Import,
    importedNamespace=
        safe_text
)
amethyst_Module_strategy = st.builds(
    amethyst_Module,
    name=
        safe_text
)
amethyst_PropertyDeclaration_strategy = st.builds(
    amethyst_PropertyDeclaration,
)

@given(instance=RangeLiteral_strategy)
@settings(max_examples=50)
def test_rangeliteral_instantiation(instance):
    assert isinstance(instance, RangeLiteral)

@given(instance=amethyst_CharRangeLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_charrangeliteral_instantiation(instance):
    assert isinstance(instance, amethyst_CharRangeLiteral)

@given(instance=amethyst_NumberRangeLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_numberrangeliteral_instantiation(instance):
    assert isinstance(instance, amethyst_NumberRangeLiteral)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=amethyst_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_ParameterDeclaration)

@given(instance=amethyst_DefinitionDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_definitiondeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_DefinitionDeclaration)



@given(instance=amethyst_DefinitionDeclaration_strategy)
def test_amethyst_definitiondeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=amethyst_ForInitializerDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_forinitializerdeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_ForInitializerDeclaration)

@given(instance=amethyst_TagLoopInitializerDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_tagloopinitializerdeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_TagLoopInitializerDeclaration)

@given(instance=amethyst_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_variabledeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_VariableDeclaration)

@given(instance=amethyst_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_classdeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_ClassDeclaration)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=amethyst_FloatType_strategy)
@settings(max_examples=50)
def test_amethyst_floattype_instantiation(instance):
    assert isinstance(instance, amethyst_FloatType)

@given(instance=amethyst_IntType_strategy)
@settings(max_examples=50)
def test_amethyst_inttype_instantiation(instance):
    assert isinstance(instance, amethyst_IntType)

@given(instance=amethyst_StringType_strategy)
@settings(max_examples=50)
def test_amethyst_stringtype_instantiation(instance):
    assert isinstance(instance, amethyst_StringType)

@given(instance=amethyst_DefinitionType_strategy)
@settings(max_examples=50)
def test_amethyst_definitiontype_instantiation(instance):
    assert isinstance(instance, amethyst_DefinitionType)

@given(instance=amethyst_BooleanType_strategy)
@settings(max_examples=50)
def test_amethyst_booleantype_instantiation(instance):
    assert isinstance(instance, amethyst_BooleanType)

@given(instance=amethyst_AnyType_strategy)
@settings(max_examples=50)
def test_amethyst_anytype_instantiation(instance):
    assert isinstance(instance, amethyst_AnyType)

@given(instance=amethyst_CharType_strategy)
@settings(max_examples=50)
def test_amethyst_chartype_instantiation(instance):
    assert isinstance(instance, amethyst_CharType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=amethyst_PrimitiveType_strategy)
@settings(max_examples=50)
def test_amethyst_primitivetype_instantiation(instance):
    assert isinstance(instance, amethyst_PrimitiveType)

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=amethyst_ArrayType_strategy)
@settings(max_examples=50)
def test_amethyst_arraytype_instantiation(instance):
    assert isinstance(instance, amethyst_ArrayType)

@given(instance=amethyst_Type_strategy)
@settings(max_examples=50)
def test_amethyst_type_instantiation(instance):
    assert isinstance(instance, amethyst_Type)

@given(instance=amethyst_AbstractType_strategy)
@settings(max_examples=50)
def test_amethyst_abstracttype_instantiation(instance):
    assert isinstance(instance, amethyst_AbstractType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=amethyst_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_booleanliteral_instantiation(instance):
    assert isinstance(instance, amethyst_BooleanLiteral)



@given(instance=amethyst_BooleanLiteral_strategy)
def test_amethyst_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=amethyst_NullLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_nullliteral_instantiation(instance):
    assert isinstance(instance, amethyst_NullLiteral)

@given(instance=amethyst_FloatLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_floatliteral_instantiation(instance):
    assert isinstance(instance, amethyst_FloatLiteral)



@given(instance=amethyst_FloatLiteral_strategy)
def test_amethyst_floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=amethyst_RangeLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_rangeliteral_instantiation(instance):
    assert isinstance(instance, amethyst_RangeLiteral)

@given(instance=amethyst_IntLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_intliteral_instantiation(instance):
    assert isinstance(instance, amethyst_IntLiteral)



@given(instance=amethyst_IntLiteral_strategy)
def test_amethyst_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=amethyst_StringLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_stringliteral_instantiation(instance):
    assert isinstance(instance, amethyst_StringLiteral)



@given(instance=amethyst_StringLiteral_strategy)
def test_amethyst_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=amethyst_CharLiteral_strategy)
@settings(max_examples=50)
def test_amethyst_charliteral_instantiation(instance):
    assert isinstance(instance, amethyst_CharLiteral)



@given(instance=amethyst_CharLiteral_strategy)
def test_amethyst_charliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=amethyst_ShiftExpression_strategy)
@settings(max_examples=50)
def test_amethyst_shiftexpression_instantiation(instance):
    assert isinstance(instance, amethyst_ShiftExpression)



@given(instance=amethyst_ShiftExpression_strategy)
def test_amethyst_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=amethyst_AndExpression_strategy)
@settings(max_examples=50)
def test_amethyst_andexpression_instantiation(instance):
    assert isinstance(instance, amethyst_AndExpression)

@given(instance=amethyst_CallExpression_strategy)
@settings(max_examples=50)
def test_amethyst_callexpression_instantiation(instance):
    assert isinstance(instance, amethyst_CallExpression)

@given(instance=amethyst_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_amethyst_additiveexpression_instantiation(instance):
    assert isinstance(instance, amethyst_AdditiveExpression)



@given(instance=amethyst_AdditiveExpression_strategy)
def test_amethyst_additiveexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=amethyst_MatchingExpression_strategy)
@settings(max_examples=50)
def test_amethyst_matchingexpression_instantiation(instance):
    assert isinstance(instance, amethyst_MatchingExpression)



@given(instance=amethyst_MatchingExpression_strategy)
def test_amethyst_matchingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=amethyst_SuperExpression_strategy)
@settings(max_examples=50)
def test_amethyst_superexpression_instantiation(instance):
    assert isinstance(instance, amethyst_SuperExpression)

@given(instance=amethyst_ParenthisedExpression_strategy)
@settings(max_examples=50)
def test_amethyst_parenthisedexpression_instantiation(instance):
    assert isinstance(instance, amethyst_ParenthisedExpression)

@given(instance=amethyst_SelfExpression_strategy)
@settings(max_examples=50)
def test_amethyst_selfexpression_instantiation(instance):
    assert isinstance(instance, amethyst_SelfExpression)

@given(instance=amethyst_TypeCastExpression_strategy)
@settings(max_examples=50)
def test_amethyst_typecastexpression_instantiation(instance):
    assert isinstance(instance, amethyst_TypeCastExpression)

@given(instance=amethyst_IndexAccessExpression_strategy)
@settings(max_examples=50)
def test_amethyst_indexaccessexpression_instantiation(instance):
    assert isinstance(instance, amethyst_IndexAccessExpression)

@given(instance=amethyst_InExpression_strategy)
@settings(max_examples=50)
def test_amethyst_inexpression_instantiation(instance):
    assert isinstance(instance, amethyst_InExpression)

@given(instance=amethyst_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_amethyst_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, amethyst_MultiplicativeExpression)



@given(instance=amethyst_MultiplicativeExpression_strategy)
def test_amethyst_multiplicativeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=amethyst_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_amethyst_assignmentexpression_instantiation(instance):
    assert isinstance(instance, amethyst_AssignmentExpression)

@given(instance=amethyst_MemberAccessExpression_strategy)
@settings(max_examples=50)
def test_amethyst_memberaccessexpression_instantiation(instance):
    assert isinstance(instance, amethyst_MemberAccessExpression)

@given(instance=amethyst_UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_amethyst_unaryminusexpression_instantiation(instance):
    assert isinstance(instance, amethyst_UnaryMinusExpression)

@given(instance=amethyst_EqualityExpression_strategy)
@settings(max_examples=50)
def test_amethyst_equalityexpression_instantiation(instance):
    assert isinstance(instance, amethyst_EqualityExpression)



@given(instance=amethyst_EqualityExpression_strategy)
def test_amethyst_equalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=amethyst_NotExpression_strategy)
@settings(max_examples=50)
def test_amethyst_notexpression_instantiation(instance):
    assert isinstance(instance, amethyst_NotExpression)

@given(instance=amethyst_RelationalExpression_strategy)
@settings(max_examples=50)
def test_amethyst_relationalexpression_instantiation(instance):
    assert isinstance(instance, amethyst_RelationalExpression)



@given(instance=amethyst_RelationalExpression_strategy)
def test_amethyst_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=amethyst_Literal_strategy)
@settings(max_examples=50)
def test_amethyst_literal_instantiation(instance):
    assert isinstance(instance, amethyst_Literal)

@given(instance=amethyst_OrExpression_strategy)
@settings(max_examples=50)
def test_amethyst_orexpression_instantiation(instance):
    assert isinstance(instance, amethyst_OrExpression)

@given(instance=amethyst_NewExpression_strategy)
@settings(max_examples=50)
def test_amethyst_newexpression_instantiation(instance):
    assert isinstance(instance, amethyst_NewExpression)

@given(instance=amethyst_SymbolReference_strategy)
@settings(max_examples=50)
def test_amethyst_symbolreference_instantiation(instance):
    assert isinstance(instance, amethyst_SymbolReference)

@given(instance=amethyst_TagExpression_strategy)
@settings(max_examples=50)
def test_amethyst_tagexpression_instantiation(instance):
    assert isinstance(instance, amethyst_TagExpression)

@given(instance=amethyst_EObject_strategy)
@settings(max_examples=50)
def test_amethyst_eobject_instantiation(instance):
    assert isinstance(instance, amethyst_EObject)

@given(instance=amethyst_TagAttribute_strategy)
@settings(max_examples=50)
def test_amethyst_tagattribute_instantiation(instance):
    assert isinstance(instance, amethyst_TagAttribute)

@given(instance=amethyst_TagLoopExpression_strategy)
@settings(max_examples=50)
def test_amethyst_tagloopexpression_instantiation(instance):
    assert isinstance(instance, amethyst_TagLoopExpression)

@given(instance=amethyst_ClassType_strategy)
@settings(max_examples=50)
def test_amethyst_classtype_instantiation(instance):
    assert isinstance(instance, amethyst_ClassType)

@given(instance=amethyst_TagDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_tagdeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_TagDeclaration)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=amethyst_ElseIfStatement_strategy)
@settings(max_examples=50)
def test_amethyst_elseifstatement_instantiation(instance):
    assert isinstance(instance, amethyst_ElseIfStatement)

@given(instance=amethyst_BreakStatement_strategy)
@settings(max_examples=50)
def test_amethyst_breakstatement_instantiation(instance):
    assert isinstance(instance, amethyst_BreakStatement)

@given(instance=amethyst_ForStatement_strategy)
@settings(max_examples=50)
def test_amethyst_forstatement_instantiation(instance):
    assert isinstance(instance, amethyst_ForStatement)

@given(instance=amethyst_CaseElseStatement_strategy)
@settings(max_examples=50)
def test_amethyst_caseelsestatement_instantiation(instance):
    assert isinstance(instance, amethyst_CaseElseStatement)

@given(instance=amethyst_JsCodeStatement_strategy)
@settings(max_examples=50)
def test_amethyst_jscodestatement_instantiation(instance):
    assert isinstance(instance, amethyst_JsCodeStatement)



@given(instance=amethyst_JsCodeStatement_strategy)
def test_amethyst_jscodestatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=amethyst_Expression_strategy)
@settings(max_examples=50)
def test_amethyst_expression_instantiation(instance):
    assert isinstance(instance, amethyst_Expression)

@given(instance=amethyst_WhenStatement_strategy)
@settings(max_examples=50)
def test_amethyst_whenstatement_instantiation(instance):
    assert isinstance(instance, amethyst_WhenStatement)

@given(instance=amethyst_IfStatement_strategy)
@settings(max_examples=50)
def test_amethyst_ifstatement_instantiation(instance):
    assert isinstance(instance, amethyst_IfStatement)

@given(instance=amethyst_ElseStatement_strategy)
@settings(max_examples=50)
def test_amethyst_elsestatement_instantiation(instance):
    assert isinstance(instance, amethyst_ElseStatement)

@given(instance=amethyst_NextStatement_strategy)
@settings(max_examples=50)
def test_amethyst_nextstatement_instantiation(instance):
    assert isinstance(instance, amethyst_NextStatement)

@given(instance=amethyst_CaseStatement_strategy)
@settings(max_examples=50)
def test_amethyst_casestatement_instantiation(instance):
    assert isinstance(instance, amethyst_CaseStatement)

@given(instance=amethyst_ReturnStatement_strategy)
@settings(max_examples=50)
def test_amethyst_returnstatement_instantiation(instance):
    assert isinstance(instance, amethyst_ReturnStatement)

@given(instance=amethyst_WhileStatement_strategy)
@settings(max_examples=50)
def test_amethyst_whilestatement_instantiation(instance):
    assert isinstance(instance, amethyst_WhileStatement)

@given(instance=amethyst_Symbol_strategy)
@settings(max_examples=50)
def test_amethyst_symbol_instantiation(instance):
    assert isinstance(instance, amethyst_Symbol)



@given(instance=amethyst_Symbol_strategy)
def test_amethyst_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amethyst_Statement_strategy)
@settings(max_examples=50)
def test_amethyst_statement_instantiation(instance):
    assert isinstance(instance, amethyst_Statement)

@given(instance=amethyst_Import_strategy)
@settings(max_examples=50)
def test_amethyst_import_instantiation(instance):
    assert isinstance(instance, amethyst_Import)



@given(instance=amethyst_Import_strategy)
def test_amethyst_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=amethyst_Module_strategy)
@settings(max_examples=50)
def test_amethyst_module_instantiation(instance):
    assert isinstance(instance, amethyst_Module)



@given(instance=amethyst_Module_strategy)
def test_amethyst_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amethyst_PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_amethyst_propertydeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_PropertyDeclaration)
