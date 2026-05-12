import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Prefix,
    AffectationPrefixStatement,
    leek_PrefixIncrement,
    leek_PrefixDecrement,
    Postfix,
    AffectationPostfixStatement,
    leek_PostfixDecrement,
    leek_PostfixIncrement,
    ForInVariableReference,
    Expression,
    leek_Div,
    leek_Or,
    leek_Multi,
    leek_FalseLiteral,
    leek_TernaryIf,
    leek_Different,
    leek_Plus,
    leek_And,
    leek_Minus,
    leek_Less,
    leek_TypedDifferent,
    leek_Comparison,
    leek_RealLiteral,
    leek_Postfix,
    leek_More,
    leek_Prefix,
    leek_LessOrEquals,
    leek_TrueLiteral,
    leek_Equals,
    leek_NullLiteral,
    leek_UnitaryMinus,
    leek_Not,
    leek_StringLiteral,
    leek_ArrayLiteral,
    leek_MoreOrEquals,
    leek_IntLiteral,
    leek_ForInVariableReference,
    leek_ForAffectation,
    leek_Script,
    leek_ForInitializer,
    Iteration,
    leek_For,
    leek_ForIn,
    leek_While,
    leek_IfCondition,
    leek_VariableReference,
    ForAffectation,
    ForInitializer,
    leek_VariableDeclaration,
    IfCondition,
    leek_Expression,
    AffectationStatement,
    leek_AffectationIncrement,
    leek_AffectationPrefixStatement,
    leek_AffectationDecrement,
    leek_AffectationPostfixStatement,
    leek_Affectation,
    Statement,
    leek_StatementBlock,
    leek_FunctionDeclaration,
    leek_Iteration,
    leek_LocalDeclaration,
    leek_FunctionCall,
    leek_ReturnStatement,
    leek_GlobalDeclaration,
    leek_EmptyStatement,
    leek_AffectationStatement,
    leek_Include,
    leek_If,
    leek_ContinueStatement,
    leek_BreakStatement,
    leek_Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_affectationprefixstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationPrefixStatement)


def test_affectationprefixstatement_constructor_exists():
    assert callable(AffectationPrefixStatement.__init__)


def test_affectationprefixstatement_constructor_args():
    sig = inspect.signature(AffectationPrefixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_prefixincrement_is_not_abstract():
    assert not inspect.isabstract(leek_PrefixIncrement)


def test_leek_prefixincrement_constructor_exists():
    assert callable(leek_PrefixIncrement.__init__)


def test_leek_prefixincrement_constructor_args():
    sig = inspect.signature(leek_PrefixIncrement.__init__)
    params = list(sig.parameters.keys())



def test_leek_prefixdecrement_is_not_abstract():
    assert not inspect.isabstract(leek_PrefixDecrement)


def test_leek_prefixdecrement_constructor_exists():
    assert callable(leek_PrefixDecrement.__init__)


def test_leek_prefixdecrement_constructor_args():
    sig = inspect.signature(leek_PrefixDecrement.__init__)
    params = list(sig.parameters.keys())



def test_postfix_is_not_abstract():
    assert not inspect.isabstract(Postfix)


def test_postfix_constructor_exists():
    assert callable(Postfix.__init__)


def test_postfix_constructor_args():
    sig = inspect.signature(Postfix.__init__)
    params = list(sig.parameters.keys())



def test_affectationpostfixstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationPostfixStatement)


def test_affectationpostfixstatement_constructor_exists():
    assert callable(AffectationPostfixStatement.__init__)


def test_affectationpostfixstatement_constructor_args():
    sig = inspect.signature(AffectationPostfixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_postfixdecrement_is_not_abstract():
    assert not inspect.isabstract(leek_PostfixDecrement)


def test_leek_postfixdecrement_constructor_exists():
    assert callable(leek_PostfixDecrement.__init__)


def test_leek_postfixdecrement_constructor_args():
    sig = inspect.signature(leek_PostfixDecrement.__init__)
    params = list(sig.parameters.keys())



def test_leek_postfixincrement_is_not_abstract():
    assert not inspect.isabstract(leek_PostfixIncrement)


def test_leek_postfixincrement_constructor_exists():
    assert callable(leek_PostfixIncrement.__init__)


def test_leek_postfixincrement_constructor_args():
    sig = inspect.signature(leek_PostfixIncrement.__init__)
    params = list(sig.parameters.keys())



def test_forinvariablereference_is_not_abstract():
    assert not inspect.isabstract(ForInVariableReference)


def test_forinvariablereference_constructor_exists():
    assert callable(ForInVariableReference.__init__)


def test_forinvariablereference_constructor_args():
    sig = inspect.signature(ForInVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_leek_div_is_not_abstract():
    assert not inspect.isabstract(leek_Div)


def test_leek_div_constructor_exists():
    assert callable(leek_Div.__init__)


def test_leek_div_constructor_args():
    sig = inspect.signature(leek_Div.__init__)
    params = list(sig.parameters.keys())



def test_leek_or_is_not_abstract():
    assert not inspect.isabstract(leek_Or)


def test_leek_or_constructor_exists():
    assert callable(leek_Or.__init__)


def test_leek_or_constructor_args():
    sig = inspect.signature(leek_Or.__init__)
    params = list(sig.parameters.keys())



def test_leek_multi_is_not_abstract():
    assert not inspect.isabstract(leek_Multi)


def test_leek_multi_constructor_exists():
    assert callable(leek_Multi.__init__)


def test_leek_multi_constructor_args():
    sig = inspect.signature(leek_Multi.__init__)
    params = list(sig.parameters.keys())



def test_leek_falseliteral_is_not_abstract():
    assert not inspect.isabstract(leek_FalseLiteral)


def test_leek_falseliteral_constructor_exists():
    assert callable(leek_FalseLiteral.__init__)


def test_leek_falseliteral_constructor_args():
    sig = inspect.signature(leek_FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek_ternaryif_is_not_abstract():
    assert not inspect.isabstract(leek_TernaryIf)


def test_leek_ternaryif_constructor_exists():
    assert callable(leek_TernaryIf.__init__)


def test_leek_ternaryif_constructor_args():
    sig = inspect.signature(leek_TernaryIf.__init__)
    params = list(sig.parameters.keys())



def test_leek_different_is_not_abstract():
    assert not inspect.isabstract(leek_Different)


def test_leek_different_constructor_exists():
    assert callable(leek_Different.__init__)


def test_leek_different_constructor_args():
    sig = inspect.signature(leek_Different.__init__)
    params = list(sig.parameters.keys())



def test_leek_plus_is_not_abstract():
    assert not inspect.isabstract(leek_Plus)


def test_leek_plus_constructor_exists():
    assert callable(leek_Plus.__init__)


def test_leek_plus_constructor_args():
    sig = inspect.signature(leek_Plus.__init__)
    params = list(sig.parameters.keys())



def test_leek_and_is_not_abstract():
    assert not inspect.isabstract(leek_And)


def test_leek_and_constructor_exists():
    assert callable(leek_And.__init__)


def test_leek_and_constructor_args():
    sig = inspect.signature(leek_And.__init__)
    params = list(sig.parameters.keys())



def test_leek_minus_is_not_abstract():
    assert not inspect.isabstract(leek_Minus)


def test_leek_minus_constructor_exists():
    assert callable(leek_Minus.__init__)


def test_leek_minus_constructor_args():
    sig = inspect.signature(leek_Minus.__init__)
    params = list(sig.parameters.keys())



def test_leek_less_is_not_abstract():
    assert not inspect.isabstract(leek_Less)


def test_leek_less_constructor_exists():
    assert callable(leek_Less.__init__)


def test_leek_less_constructor_args():
    sig = inspect.signature(leek_Less.__init__)
    params = list(sig.parameters.keys())



def test_leek_typeddifferent_is_not_abstract():
    assert not inspect.isabstract(leek_TypedDifferent)


def test_leek_typeddifferent_constructor_exists():
    assert callable(leek_TypedDifferent.__init__)


def test_leek_typeddifferent_constructor_args():
    sig = inspect.signature(leek_TypedDifferent.__init__)
    params = list(sig.parameters.keys())



def test_leek_comparison_is_not_abstract():
    assert not inspect.isabstract(leek_Comparison)


def test_leek_comparison_constructor_exists():
    assert callable(leek_Comparison.__init__)


def test_leek_comparison_constructor_args():
    sig = inspect.signature(leek_Comparison.__init__)
    params = list(sig.parameters.keys())



def test_leek_realliteral_is_not_abstract():
    assert not inspect.isabstract(leek_RealLiteral)


def test_leek_realliteral_constructor_exists():
    assert callable(leek_RealLiteral.__init__)


def test_leek_realliteral_constructor_args():
    sig = inspect.signature(leek_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_leek_realliteral_has_value():
    assert hasattr(leek_RealLiteral, "value")
    descriptor = None
    for klass in leek_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_leek_postfix_is_not_abstract():
    assert not inspect.isabstract(leek_Postfix)


def test_leek_postfix_constructor_exists():
    assert callable(leek_Postfix.__init__)


def test_leek_postfix_constructor_args():
    sig = inspect.signature(leek_Postfix.__init__)
    params = list(sig.parameters.keys())



def test_leek_more_is_not_abstract():
    assert not inspect.isabstract(leek_More)


def test_leek_more_constructor_exists():
    assert callable(leek_More.__init__)


def test_leek_more_constructor_args():
    sig = inspect.signature(leek_More.__init__)
    params = list(sig.parameters.keys())



def test_leek_prefix_is_not_abstract():
    assert not inspect.isabstract(leek_Prefix)


def test_leek_prefix_constructor_exists():
    assert callable(leek_Prefix.__init__)


def test_leek_prefix_constructor_args():
    sig = inspect.signature(leek_Prefix.__init__)
    params = list(sig.parameters.keys())



def test_leek_lessorequals_is_not_abstract():
    assert not inspect.isabstract(leek_LessOrEquals)


def test_leek_lessorequals_constructor_exists():
    assert callable(leek_LessOrEquals.__init__)


def test_leek_lessorequals_constructor_args():
    sig = inspect.signature(leek_LessOrEquals.__init__)
    params = list(sig.parameters.keys())



def test_leek_trueliteral_is_not_abstract():
    assert not inspect.isabstract(leek_TrueLiteral)


def test_leek_trueliteral_constructor_exists():
    assert callable(leek_TrueLiteral.__init__)


def test_leek_trueliteral_constructor_args():
    sig = inspect.signature(leek_TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek_equals_is_not_abstract():
    assert not inspect.isabstract(leek_Equals)


def test_leek_equals_constructor_exists():
    assert callable(leek_Equals.__init__)


def test_leek_equals_constructor_args():
    sig = inspect.signature(leek_Equals.__init__)
    params = list(sig.parameters.keys())



def test_leek_nullliteral_is_not_abstract():
    assert not inspect.isabstract(leek_NullLiteral)


def test_leek_nullliteral_constructor_exists():
    assert callable(leek_NullLiteral.__init__)


def test_leek_nullliteral_constructor_args():
    sig = inspect.signature(leek_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek_unitaryminus_is_not_abstract():
    assert not inspect.isabstract(leek_UnitaryMinus)


def test_leek_unitaryminus_constructor_exists():
    assert callable(leek_UnitaryMinus.__init__)


def test_leek_unitaryminus_constructor_args():
    sig = inspect.signature(leek_UnitaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_leek_not_is_not_abstract():
    assert not inspect.isabstract(leek_Not)


def test_leek_not_constructor_exists():
    assert callable(leek_Not.__init__)


def test_leek_not_constructor_args():
    sig = inspect.signature(leek_Not.__init__)
    params = list(sig.parameters.keys())



def test_leek_stringliteral_is_not_abstract():
    assert not inspect.isabstract(leek_StringLiteral)


def test_leek_stringliteral_constructor_exists():
    assert callable(leek_StringLiteral.__init__)


def test_leek_stringliteral_constructor_args():
    sig = inspect.signature(leek_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_leek_stringliteral_has_value():
    assert hasattr(leek_StringLiteral, "value")
    descriptor = None
    for klass in leek_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_leek_arrayliteral_is_not_abstract():
    assert not inspect.isabstract(leek_ArrayLiteral)


def test_leek_arrayliteral_constructor_exists():
    assert callable(leek_ArrayLiteral.__init__)


def test_leek_arrayliteral_constructor_args():
    sig = inspect.signature(leek_ArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek_moreorequals_is_not_abstract():
    assert not inspect.isabstract(leek_MoreOrEquals)


def test_leek_moreorequals_constructor_exists():
    assert callable(leek_MoreOrEquals.__init__)


def test_leek_moreorequals_constructor_args():
    sig = inspect.signature(leek_MoreOrEquals.__init__)
    params = list(sig.parameters.keys())



def test_leek_intliteral_is_not_abstract():
    assert not inspect.isabstract(leek_IntLiteral)


def test_leek_intliteral_constructor_exists():
    assert callable(leek_IntLiteral.__init__)


def test_leek_intliteral_constructor_args():
    sig = inspect.signature(leek_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_leek_intliteral_has_value():
    assert hasattr(leek_IntLiteral, "value")
    descriptor = None
    for klass in leek_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_leek_forinvariablereference_is_not_abstract():
    assert not inspect.isabstract(leek_ForInVariableReference)


def test_leek_forinvariablereference_constructor_exists():
    assert callable(leek_ForInVariableReference.__init__)


def test_leek_forinvariablereference_constructor_args():
    sig = inspect.signature(leek_ForInVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_leek_foraffectation_is_not_abstract():
    assert not inspect.isabstract(leek_ForAffectation)


def test_leek_foraffectation_constructor_exists():
    assert callable(leek_ForAffectation.__init__)


def test_leek_foraffectation_constructor_args():
    sig = inspect.signature(leek_ForAffectation.__init__)
    params = list(sig.parameters.keys())



def test_leek_script_is_not_abstract():
    assert not inspect.isabstract(leek_Script)


def test_leek_script_constructor_exists():
    assert callable(leek_Script.__init__)


def test_leek_script_constructor_args():
    sig = inspect.signature(leek_Script.__init__)
    params = list(sig.parameters.keys())



def test_leek_forinitializer_is_not_abstract():
    assert not inspect.isabstract(leek_ForInitializer)


def test_leek_forinitializer_constructor_exists():
    assert callable(leek_ForInitializer.__init__)


def test_leek_forinitializer_constructor_args():
    sig = inspect.signature(leek_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_iteration_is_not_abstract():
    assert not inspect.isabstract(Iteration)


def test_iteration_constructor_exists():
    assert callable(Iteration.__init__)


def test_iteration_constructor_args():
    sig = inspect.signature(Iteration.__init__)
    params = list(sig.parameters.keys())



def test_leek_for_is_not_abstract():
    assert not inspect.isabstract(leek_For)


def test_leek_for_constructor_exists():
    assert callable(leek_For.__init__)


def test_leek_for_constructor_args():
    sig = inspect.signature(leek_For.__init__)
    params = list(sig.parameters.keys())



def test_leek_forin_is_not_abstract():
    assert not inspect.isabstract(leek_ForIn)


def test_leek_forin_constructor_exists():
    assert callable(leek_ForIn.__init__)


def test_leek_forin_constructor_args():
    sig = inspect.signature(leek_ForIn.__init__)
    params = list(sig.parameters.keys())



def test_leek_while_is_not_abstract():
    assert not inspect.isabstract(leek_While)


def test_leek_while_constructor_exists():
    assert callable(leek_While.__init__)


def test_leek_while_constructor_args():
    sig = inspect.signature(leek_While.__init__)
    params = list(sig.parameters.keys())



def test_leek_ifcondition_is_not_abstract():
    assert not inspect.isabstract(leek_IfCondition)


def test_leek_ifcondition_constructor_exists():
    assert callable(leek_IfCondition.__init__)


def test_leek_ifcondition_constructor_args():
    sig = inspect.signature(leek_IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_leek_variablereference_is_not_abstract():
    assert not inspect.isabstract(leek_VariableReference)


def test_leek_variablereference_constructor_exists():
    assert callable(leek_VariableReference.__init__)


def test_leek_variablereference_constructor_args():
    sig = inspect.signature(leek_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_foraffectation_is_not_abstract():
    assert not inspect.isabstract(ForAffectation)


def test_foraffectation_constructor_exists():
    assert callable(ForAffectation.__init__)


def test_foraffectation_constructor_args():
    sig = inspect.signature(ForAffectation.__init__)
    params = list(sig.parameters.keys())



def test_forinitializer_is_not_abstract():
    assert not inspect.isabstract(ForInitializer)


def test_forinitializer_constructor_exists():
    assert callable(ForInitializer.__init__)


def test_forinitializer_constructor_args():
    sig = inspect.signature(ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_leek_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_VariableDeclaration)


def test_leek_variabledeclaration_constructor_exists():
    assert callable(leek_VariableDeclaration.__init__)


def test_leek_variabledeclaration_constructor_args():
    sig = inspect.signature(leek_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "byAdress" in params, "Missing parameter 'byAdress'"

def test_leek_variabledeclaration_has_name():
    assert hasattr(leek_VariableDeclaration, "name")
    descriptor = None
    for klass in leek_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_leek_variabledeclaration_has_byAdress():
    assert hasattr(leek_VariableDeclaration, "byAdress")
    descriptor = None
    for klass in leek_VariableDeclaration.__mro__:
        if "byAdress" in klass.__dict__:
            descriptor = klass.__dict__["byAdress"]
            break
    assert isinstance(descriptor, property)



def test_ifcondition_is_not_abstract():
    assert not inspect.isabstract(IfCondition)


def test_ifcondition_constructor_exists():
    assert callable(IfCondition.__init__)


def test_ifcondition_constructor_args():
    sig = inspect.signature(IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_leek_expression_is_not_abstract():
    assert not inspect.isabstract(leek_Expression)


def test_leek_expression_constructor_exists():
    assert callable(leek_Expression.__init__)


def test_leek_expression_constructor_args():
    sig = inspect.signature(leek_Expression.__init__)
    params = list(sig.parameters.keys())



def test_affectationstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationStatement)


def test_affectationstatement_constructor_exists():
    assert callable(AffectationStatement.__init__)


def test_affectationstatement_constructor_args():
    sig = inspect.signature(AffectationStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_affectationincrement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationIncrement)


def test_leek_affectationincrement_constructor_exists():
    assert callable(leek_AffectationIncrement.__init__)


def test_leek_affectationincrement_constructor_args():
    sig = inspect.signature(leek_AffectationIncrement.__init__)
    params = list(sig.parameters.keys())



def test_leek_affectationprefixstatement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationPrefixStatement)


def test_leek_affectationprefixstatement_constructor_exists():
    assert callable(leek_AffectationPrefixStatement.__init__)


def test_leek_affectationprefixstatement_constructor_args():
    sig = inspect.signature(leek_AffectationPrefixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_affectationdecrement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationDecrement)


def test_leek_affectationdecrement_constructor_exists():
    assert callable(leek_AffectationDecrement.__init__)


def test_leek_affectationdecrement_constructor_args():
    sig = inspect.signature(leek_AffectationDecrement.__init__)
    params = list(sig.parameters.keys())



def test_leek_affectationpostfixstatement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationPostfixStatement)


def test_leek_affectationpostfixstatement_constructor_exists():
    assert callable(leek_AffectationPostfixStatement.__init__)


def test_leek_affectationpostfixstatement_constructor_args():
    sig = inspect.signature(leek_AffectationPostfixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_affectation_is_not_abstract():
    assert not inspect.isabstract(leek_Affectation)


def test_leek_affectation_constructor_exists():
    assert callable(leek_Affectation.__init__)


def test_leek_affectation_constructor_args():
    sig = inspect.signature(leek_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_leek_statementblock_is_not_abstract():
    assert not inspect.isabstract(leek_StatementBlock)


def test_leek_statementblock_constructor_exists():
    assert callable(leek_StatementBlock.__init__)


def test_leek_statementblock_constructor_args():
    sig = inspect.signature(leek_StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_leek_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_FunctionDeclaration)


def test_leek_functiondeclaration_constructor_exists():
    assert callable(leek_FunctionDeclaration.__init__)


def test_leek_functiondeclaration_constructor_args():
    sig = inspect.signature(leek_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_leek_functiondeclaration_has_name():
    assert hasattr(leek_FunctionDeclaration, "name")
    descriptor = None
    for klass in leek_FunctionDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_leek_iteration_is_not_abstract():
    assert not inspect.isabstract(leek_Iteration)


def test_leek_iteration_constructor_exists():
    assert callable(leek_Iteration.__init__)


def test_leek_iteration_constructor_args():
    sig = inspect.signature(leek_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_leek_localdeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_LocalDeclaration)


def test_leek_localdeclaration_constructor_exists():
    assert callable(leek_LocalDeclaration.__init__)


def test_leek_localdeclaration_constructor_args():
    sig = inspect.signature(leek_LocalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_leek_functioncall_is_not_abstract():
    assert not inspect.isabstract(leek_FunctionCall)


def test_leek_functioncall_constructor_exists():
    assert callable(leek_FunctionCall.__init__)


def test_leek_functioncall_constructor_args():
    sig = inspect.signature(leek_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_leek_returnstatement_is_not_abstract():
    assert not inspect.isabstract(leek_ReturnStatement)


def test_leek_returnstatement_constructor_exists():
    assert callable(leek_ReturnStatement.__init__)


def test_leek_returnstatement_constructor_args():
    sig = inspect.signature(leek_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_globaldeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_GlobalDeclaration)


def test_leek_globaldeclaration_constructor_exists():
    assert callable(leek_GlobalDeclaration.__init__)


def test_leek_globaldeclaration_constructor_args():
    sig = inspect.signature(leek_GlobalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_leek_emptystatement_is_not_abstract():
    assert not inspect.isabstract(leek_EmptyStatement)


def test_leek_emptystatement_constructor_exists():
    assert callable(leek_EmptyStatement.__init__)


def test_leek_emptystatement_constructor_args():
    sig = inspect.signature(leek_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_affectationstatement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationStatement)


def test_leek_affectationstatement_constructor_exists():
    assert callable(leek_AffectationStatement.__init__)


def test_leek_affectationstatement_constructor_args():
    sig = inspect.signature(leek_AffectationStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_include_is_not_abstract():
    assert not inspect.isabstract(leek_Include)


def test_leek_include_constructor_exists():
    assert callable(leek_Include.__init__)


def test_leek_include_constructor_args():
    sig = inspect.signature(leek_Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_leek_include_has_importURI():
    assert hasattr(leek_Include, "importURI")
    descriptor = None
    for klass in leek_Include.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_leek_if_is_not_abstract():
    assert not inspect.isabstract(leek_If)


def test_leek_if_constructor_exists():
    assert callable(leek_If.__init__)


def test_leek_if_constructor_args():
    sig = inspect.signature(leek_If.__init__)
    params = list(sig.parameters.keys())



def test_leek_continuestatement_is_not_abstract():
    assert not inspect.isabstract(leek_ContinueStatement)


def test_leek_continuestatement_constructor_exists():
    assert callable(leek_ContinueStatement.__init__)


def test_leek_continuestatement_constructor_args():
    sig = inspect.signature(leek_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_breakstatement_is_not_abstract():
    assert not inspect.isabstract(leek_BreakStatement)


def test_leek_breakstatement_constructor_exists():
    assert callable(leek_BreakStatement.__init__)


def test_leek_breakstatement_constructor_args():
    sig = inspect.signature(leek_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek_statement_is_not_abstract():
    assert not inspect.isabstract(leek_Statement)


def test_leek_statement_constructor_exists():
    assert callable(leek_Statement.__init__)


def test_leek_statement_constructor_args():
    sig = inspect.signature(leek_Statement.__init__)
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
Prefix_strategy = st.builds(
    Prefix,
)
AffectationPrefixStatement_strategy = st.builds(
    AffectationPrefixStatement,
)
leek_PrefixIncrement_strategy = st.builds(
    leek_PrefixIncrement,
)
leek_PrefixDecrement_strategy = st.builds(
    leek_PrefixDecrement,
)
Postfix_strategy = st.builds(
    Postfix,
)
AffectationPostfixStatement_strategy = st.builds(
    AffectationPostfixStatement,
)
leek_PostfixDecrement_strategy = st.builds(
    leek_PostfixDecrement,
)
leek_PostfixIncrement_strategy = st.builds(
    leek_PostfixIncrement,
)
ForInVariableReference_strategy = st.builds(
    ForInVariableReference,
)
Expression_strategy = st.builds(
    Expression,
)
leek_Div_strategy = st.builds(
    leek_Div,
)
leek_Or_strategy = st.builds(
    leek_Or,
)
leek_Multi_strategy = st.builds(
    leek_Multi,
)
leek_FalseLiteral_strategy = st.builds(
    leek_FalseLiteral,
)
leek_TernaryIf_strategy = st.builds(
    leek_TernaryIf,
)
leek_Different_strategy = st.builds(
    leek_Different,
)
leek_Plus_strategy = st.builds(
    leek_Plus,
)
leek_And_strategy = st.builds(
    leek_And,
)
leek_Minus_strategy = st.builds(
    leek_Minus,
)
leek_Less_strategy = st.builds(
    leek_Less,
)
leek_TypedDifferent_strategy = st.builds(
    leek_TypedDifferent,
)
leek_Comparison_strategy = st.builds(
    leek_Comparison,
)
leek_RealLiteral_strategy = st.builds(
    leek_RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
leek_Postfix_strategy = st.builds(
    leek_Postfix,
)
leek_More_strategy = st.builds(
    leek_More,
)
leek_Prefix_strategy = st.builds(
    leek_Prefix,
)
leek_LessOrEquals_strategy = st.builds(
    leek_LessOrEquals,
)
leek_TrueLiteral_strategy = st.builds(
    leek_TrueLiteral,
)
leek_Equals_strategy = st.builds(
    leek_Equals,
)
leek_NullLiteral_strategy = st.builds(
    leek_NullLiteral,
)
leek_UnitaryMinus_strategy = st.builds(
    leek_UnitaryMinus,
)
leek_Not_strategy = st.builds(
    leek_Not,
)
leek_StringLiteral_strategy = st.builds(
    leek_StringLiteral,
    value=
        safe_text
)
leek_ArrayLiteral_strategy = st.builds(
    leek_ArrayLiteral,
)
leek_MoreOrEquals_strategy = st.builds(
    leek_MoreOrEquals,
)
leek_IntLiteral_strategy = st.builds(
    leek_IntLiteral,
    value=
        st.integers()
)
leek_ForInVariableReference_strategy = st.builds(
    leek_ForInVariableReference,
)
leek_ForAffectation_strategy = st.builds(
    leek_ForAffectation,
)
leek_Script_strategy = st.builds(
    leek_Script,
)
leek_ForInitializer_strategy = st.builds(
    leek_ForInitializer,
)
Iteration_strategy = st.builds(
    Iteration,
)
leek_For_strategy = st.builds(
    leek_For,
)
leek_ForIn_strategy = st.builds(
    leek_ForIn,
)
leek_While_strategy = st.builds(
    leek_While,
)
leek_IfCondition_strategy = st.builds(
    leek_IfCondition,
)
leek_VariableReference_strategy = st.builds(
    leek_VariableReference,
)
ForAffectation_strategy = st.builds(
    ForAffectation,
)
ForInitializer_strategy = st.builds(
    ForInitializer,
)
leek_VariableDeclaration_strategy = st.builds(
    leek_VariableDeclaration,
    name=
        safe_text,
    byAdress=
        st.booleans()
)
IfCondition_strategy = st.builds(
    IfCondition,
)
leek_Expression_strategy = st.builds(
    leek_Expression,
)
AffectationStatement_strategy = st.builds(
    AffectationStatement,
)
leek_AffectationIncrement_strategy = st.builds(
    leek_AffectationIncrement,
)
leek_AffectationPrefixStatement_strategy = st.builds(
    leek_AffectationPrefixStatement,
)
leek_AffectationDecrement_strategy = st.builds(
    leek_AffectationDecrement,
)
leek_AffectationPostfixStatement_strategy = st.builds(
    leek_AffectationPostfixStatement,
)
leek_Affectation_strategy = st.builds(
    leek_Affectation,
)
Statement_strategy = st.builds(
    Statement,
)
leek_StatementBlock_strategy = st.builds(
    leek_StatementBlock,
)
leek_FunctionDeclaration_strategy = st.builds(
    leek_FunctionDeclaration,
    name=
        safe_text
)
leek_Iteration_strategy = st.builds(
    leek_Iteration,
)
leek_LocalDeclaration_strategy = st.builds(
    leek_LocalDeclaration,
)
leek_FunctionCall_strategy = st.builds(
    leek_FunctionCall,
)
leek_ReturnStatement_strategy = st.builds(
    leek_ReturnStatement,
)
leek_GlobalDeclaration_strategy = st.builds(
    leek_GlobalDeclaration,
)
leek_EmptyStatement_strategy = st.builds(
    leek_EmptyStatement,
)
leek_AffectationStatement_strategy = st.builds(
    leek_AffectationStatement,
)
leek_Include_strategy = st.builds(
    leek_Include,
    importURI=
        safe_text
)
leek_If_strategy = st.builds(
    leek_If,
)
leek_ContinueStatement_strategy = st.builds(
    leek_ContinueStatement,
)
leek_BreakStatement_strategy = st.builds(
    leek_BreakStatement,
)
leek_Statement_strategy = st.builds(
    leek_Statement,
)

@given(instance=Prefix_strategy)
@settings(max_examples=50)
def test_prefix_instantiation(instance):
    assert isinstance(instance, Prefix)

@given(instance=AffectationPrefixStatement_strategy)
@settings(max_examples=50)
def test_affectationprefixstatement_instantiation(instance):
    assert isinstance(instance, AffectationPrefixStatement)

@given(instance=leek_PrefixIncrement_strategy)
@settings(max_examples=50)
def test_leek_prefixincrement_instantiation(instance):
    assert isinstance(instance, leek_PrefixIncrement)

@given(instance=leek_PrefixDecrement_strategy)
@settings(max_examples=50)
def test_leek_prefixdecrement_instantiation(instance):
    assert isinstance(instance, leek_PrefixDecrement)

@given(instance=Postfix_strategy)
@settings(max_examples=50)
def test_postfix_instantiation(instance):
    assert isinstance(instance, Postfix)

@given(instance=AffectationPostfixStatement_strategy)
@settings(max_examples=50)
def test_affectationpostfixstatement_instantiation(instance):
    assert isinstance(instance, AffectationPostfixStatement)

@given(instance=leek_PostfixDecrement_strategy)
@settings(max_examples=50)
def test_leek_postfixdecrement_instantiation(instance):
    assert isinstance(instance, leek_PostfixDecrement)

@given(instance=leek_PostfixIncrement_strategy)
@settings(max_examples=50)
def test_leek_postfixincrement_instantiation(instance):
    assert isinstance(instance, leek_PostfixIncrement)

@given(instance=ForInVariableReference_strategy)
@settings(max_examples=50)
def test_forinvariablereference_instantiation(instance):
    assert isinstance(instance, ForInVariableReference)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=leek_Div_strategy)
@settings(max_examples=50)
def test_leek_div_instantiation(instance):
    assert isinstance(instance, leek_Div)

@given(instance=leek_Or_strategy)
@settings(max_examples=50)
def test_leek_or_instantiation(instance):
    assert isinstance(instance, leek_Or)

@given(instance=leek_Multi_strategy)
@settings(max_examples=50)
def test_leek_multi_instantiation(instance):
    assert isinstance(instance, leek_Multi)

@given(instance=leek_FalseLiteral_strategy)
@settings(max_examples=50)
def test_leek_falseliteral_instantiation(instance):
    assert isinstance(instance, leek_FalseLiteral)

@given(instance=leek_TernaryIf_strategy)
@settings(max_examples=50)
def test_leek_ternaryif_instantiation(instance):
    assert isinstance(instance, leek_TernaryIf)

@given(instance=leek_Different_strategy)
@settings(max_examples=50)
def test_leek_different_instantiation(instance):
    assert isinstance(instance, leek_Different)

@given(instance=leek_Plus_strategy)
@settings(max_examples=50)
def test_leek_plus_instantiation(instance):
    assert isinstance(instance, leek_Plus)

@given(instance=leek_And_strategy)
@settings(max_examples=50)
def test_leek_and_instantiation(instance):
    assert isinstance(instance, leek_And)

@given(instance=leek_Minus_strategy)
@settings(max_examples=50)
def test_leek_minus_instantiation(instance):
    assert isinstance(instance, leek_Minus)

@given(instance=leek_Less_strategy)
@settings(max_examples=50)
def test_leek_less_instantiation(instance):
    assert isinstance(instance, leek_Less)

@given(instance=leek_TypedDifferent_strategy)
@settings(max_examples=50)
def test_leek_typeddifferent_instantiation(instance):
    assert isinstance(instance, leek_TypedDifferent)

@given(instance=leek_Comparison_strategy)
@settings(max_examples=50)
def test_leek_comparison_instantiation(instance):
    assert isinstance(instance, leek_Comparison)

@given(instance=leek_RealLiteral_strategy)
@settings(max_examples=50)
def test_leek_realliteral_instantiation(instance):
    assert isinstance(instance, leek_RealLiteral)



@given(instance=leek_RealLiteral_strategy)
def test_leek_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=leek_Postfix_strategy)
@settings(max_examples=50)
def test_leek_postfix_instantiation(instance):
    assert isinstance(instance, leek_Postfix)

@given(instance=leek_More_strategy)
@settings(max_examples=50)
def test_leek_more_instantiation(instance):
    assert isinstance(instance, leek_More)

@given(instance=leek_Prefix_strategy)
@settings(max_examples=50)
def test_leek_prefix_instantiation(instance):
    assert isinstance(instance, leek_Prefix)

@given(instance=leek_LessOrEquals_strategy)
@settings(max_examples=50)
def test_leek_lessorequals_instantiation(instance):
    assert isinstance(instance, leek_LessOrEquals)

@given(instance=leek_TrueLiteral_strategy)
@settings(max_examples=50)
def test_leek_trueliteral_instantiation(instance):
    assert isinstance(instance, leek_TrueLiteral)

@given(instance=leek_Equals_strategy)
@settings(max_examples=50)
def test_leek_equals_instantiation(instance):
    assert isinstance(instance, leek_Equals)

@given(instance=leek_NullLiteral_strategy)
@settings(max_examples=50)
def test_leek_nullliteral_instantiation(instance):
    assert isinstance(instance, leek_NullLiteral)

@given(instance=leek_UnitaryMinus_strategy)
@settings(max_examples=50)
def test_leek_unitaryminus_instantiation(instance):
    assert isinstance(instance, leek_UnitaryMinus)

@given(instance=leek_Not_strategy)
@settings(max_examples=50)
def test_leek_not_instantiation(instance):
    assert isinstance(instance, leek_Not)

@given(instance=leek_StringLiteral_strategy)
@settings(max_examples=50)
def test_leek_stringliteral_instantiation(instance):
    assert isinstance(instance, leek_StringLiteral)



@given(instance=leek_StringLiteral_strategy)
def test_leek_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=leek_ArrayLiteral_strategy)
@settings(max_examples=50)
def test_leek_arrayliteral_instantiation(instance):
    assert isinstance(instance, leek_ArrayLiteral)

@given(instance=leek_MoreOrEquals_strategy)
@settings(max_examples=50)
def test_leek_moreorequals_instantiation(instance):
    assert isinstance(instance, leek_MoreOrEquals)

@given(instance=leek_IntLiteral_strategy)
@settings(max_examples=50)
def test_leek_intliteral_instantiation(instance):
    assert isinstance(instance, leek_IntLiteral)



@given(instance=leek_IntLiteral_strategy)
def test_leek_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=leek_ForInVariableReference_strategy)
@settings(max_examples=50)
def test_leek_forinvariablereference_instantiation(instance):
    assert isinstance(instance, leek_ForInVariableReference)

@given(instance=leek_ForAffectation_strategy)
@settings(max_examples=50)
def test_leek_foraffectation_instantiation(instance):
    assert isinstance(instance, leek_ForAffectation)

@given(instance=leek_Script_strategy)
@settings(max_examples=50)
def test_leek_script_instantiation(instance):
    assert isinstance(instance, leek_Script)

@given(instance=leek_ForInitializer_strategy)
@settings(max_examples=50)
def test_leek_forinitializer_instantiation(instance):
    assert isinstance(instance, leek_ForInitializer)

@given(instance=Iteration_strategy)
@settings(max_examples=50)
def test_iteration_instantiation(instance):
    assert isinstance(instance, Iteration)

@given(instance=leek_For_strategy)
@settings(max_examples=50)
def test_leek_for_instantiation(instance):
    assert isinstance(instance, leek_For)

@given(instance=leek_ForIn_strategy)
@settings(max_examples=50)
def test_leek_forin_instantiation(instance):
    assert isinstance(instance, leek_ForIn)

@given(instance=leek_While_strategy)
@settings(max_examples=50)
def test_leek_while_instantiation(instance):
    assert isinstance(instance, leek_While)

@given(instance=leek_IfCondition_strategy)
@settings(max_examples=50)
def test_leek_ifcondition_instantiation(instance):
    assert isinstance(instance, leek_IfCondition)

@given(instance=leek_VariableReference_strategy)
@settings(max_examples=50)
def test_leek_variablereference_instantiation(instance):
    assert isinstance(instance, leek_VariableReference)

@given(instance=ForAffectation_strategy)
@settings(max_examples=50)
def test_foraffectation_instantiation(instance):
    assert isinstance(instance, ForAffectation)

@given(instance=ForInitializer_strategy)
@settings(max_examples=50)
def test_forinitializer_instantiation(instance):
    assert isinstance(instance, ForInitializer)

@given(instance=leek_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_leek_variabledeclaration_instantiation(instance):
    assert isinstance(instance, leek_VariableDeclaration)



@given(instance=leek_VariableDeclaration_strategy)
def test_leek_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=leek_VariableDeclaration_strategy)
def test_leek_variabledeclaration_byAdress_setter(instance):
    original = instance.byAdress
    instance.byAdress = original
    assert instance.byAdress == original

@given(instance=IfCondition_strategy)
@settings(max_examples=50)
def test_ifcondition_instantiation(instance):
    assert isinstance(instance, IfCondition)

@given(instance=leek_Expression_strategy)
@settings(max_examples=50)
def test_leek_expression_instantiation(instance):
    assert isinstance(instance, leek_Expression)

@given(instance=AffectationStatement_strategy)
@settings(max_examples=50)
def test_affectationstatement_instantiation(instance):
    assert isinstance(instance, AffectationStatement)

@given(instance=leek_AffectationIncrement_strategy)
@settings(max_examples=50)
def test_leek_affectationincrement_instantiation(instance):
    assert isinstance(instance, leek_AffectationIncrement)

@given(instance=leek_AffectationPrefixStatement_strategy)
@settings(max_examples=50)
def test_leek_affectationprefixstatement_instantiation(instance):
    assert isinstance(instance, leek_AffectationPrefixStatement)

@given(instance=leek_AffectationDecrement_strategy)
@settings(max_examples=50)
def test_leek_affectationdecrement_instantiation(instance):
    assert isinstance(instance, leek_AffectationDecrement)

@given(instance=leek_AffectationPostfixStatement_strategy)
@settings(max_examples=50)
def test_leek_affectationpostfixstatement_instantiation(instance):
    assert isinstance(instance, leek_AffectationPostfixStatement)

@given(instance=leek_Affectation_strategy)
@settings(max_examples=50)
def test_leek_affectation_instantiation(instance):
    assert isinstance(instance, leek_Affectation)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=leek_StatementBlock_strategy)
@settings(max_examples=50)
def test_leek_statementblock_instantiation(instance):
    assert isinstance(instance, leek_StatementBlock)

@given(instance=leek_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_leek_functiondeclaration_instantiation(instance):
    assert isinstance(instance, leek_FunctionDeclaration)



@given(instance=leek_FunctionDeclaration_strategy)
def test_leek_functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=leek_Iteration_strategy)
@settings(max_examples=50)
def test_leek_iteration_instantiation(instance):
    assert isinstance(instance, leek_Iteration)

@given(instance=leek_LocalDeclaration_strategy)
@settings(max_examples=50)
def test_leek_localdeclaration_instantiation(instance):
    assert isinstance(instance, leek_LocalDeclaration)

@given(instance=leek_FunctionCall_strategy)
@settings(max_examples=50)
def test_leek_functioncall_instantiation(instance):
    assert isinstance(instance, leek_FunctionCall)

@given(instance=leek_ReturnStatement_strategy)
@settings(max_examples=50)
def test_leek_returnstatement_instantiation(instance):
    assert isinstance(instance, leek_ReturnStatement)

@given(instance=leek_GlobalDeclaration_strategy)
@settings(max_examples=50)
def test_leek_globaldeclaration_instantiation(instance):
    assert isinstance(instance, leek_GlobalDeclaration)

@given(instance=leek_EmptyStatement_strategy)
@settings(max_examples=50)
def test_leek_emptystatement_instantiation(instance):
    assert isinstance(instance, leek_EmptyStatement)

@given(instance=leek_AffectationStatement_strategy)
@settings(max_examples=50)
def test_leek_affectationstatement_instantiation(instance):
    assert isinstance(instance, leek_AffectationStatement)

@given(instance=leek_Include_strategy)
@settings(max_examples=50)
def test_leek_include_instantiation(instance):
    assert isinstance(instance, leek_Include)



@given(instance=leek_Include_strategy)
def test_leek_include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=leek_If_strategy)
@settings(max_examples=50)
def test_leek_if_instantiation(instance):
    assert isinstance(instance, leek_If)

@given(instance=leek_ContinueStatement_strategy)
@settings(max_examples=50)
def test_leek_continuestatement_instantiation(instance):
    assert isinstance(instance, leek_ContinueStatement)

@given(instance=leek_BreakStatement_strategy)
@settings(max_examples=50)
def test_leek_breakstatement_instantiation(instance):
    assert isinstance(instance, leek_BreakStatement)

@given(instance=leek_Statement_strategy)
@settings(max_examples=50)
def test_leek_statement_instantiation(instance):
    assert isinstance(instance, leek_Statement)
