import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ReturnTypeExpr,
    b_ReturnOr,
    PropertyExpr,
    b_PropertyTyped,
    ReturnExpr,
    b_Neg,
    b_PropertyRange,
    Return,
    b_ReturnTuple,
    b_ReturnTypeExpr,
    b_ReturnExpr,
    Statement,
    b_BeginBody,
    Type,
    b_PrimitiveType,
    b_SimpleCall,
    b_EObject,
    BeginBody,
    b_FinalExpr,
    b_CaseExpr,
    b_Operation,
    b_PreExpr,
    b_Condition,
    b_IfCond,
    FinalExpr,
    b_Statement,
    Expr,
    b_Return,
    b_Case,
    b_Call,
    b_Assign,
    Body,
    b_Begin,
    b_Seq,
    b_Pre,
    b_Var,
    b_If,
    b_Skip,
    b_Expr,
    b_Body,
    b_PropertyExpr,
    b_Set,
    Arg,
    b_ArgMinus,
    b_StringLiteral,
    Condition,
    b_CondAnd,
    b_CondNeg,
    b_CondLessThan,
    b_CondEq,
    b_BoolLiteral,
    b_CondMinus,
    b_Arg,
    LogicalExpr,
    b_IntLiteral,
    b_ImplyExpr,
    b_TypeConstraint,
    b_AndExpr,
    b_Ref,
    b_BoolTest,
    b_InequalityExpr,
    b_NegExpr,
    b_ConstantExpr,
    b_EqualExpr,
    b_DefinitionCall,
    b_LogicalExpr,
    b_Definition,
    b_AssertionExpr,
    b_Range,
    b_Values,
    b_Imports,
    b_Sets,
    b_InitialisationExpr,
    b_Type,
    b_InvariantExpr,
    b_Variable,
    b_ValueExpr,
    b_LocalOperations,
    b_Assertions,
    b_Initialisation,
    b_Invariant,
    b_ConcreteVariables,
    Abstraction,
    b_Implementation,
    b_Machine,
    b_Operations,
    b_Properties,
    b_Definitions,
    b_ConcreteConstants,
    b_Sees,
    b_Abstraction,
    InequalityOp,
    PrimitiveTypeEnum,
    BoolLiteralEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_returntypeexpr_is_not_abstract():
    assert not inspect.isabstract(ReturnTypeExpr)


def test_returntypeexpr_constructor_exists():
    assert callable(ReturnTypeExpr.__init__)


def test_returntypeexpr_constructor_args():
    sig = inspect.signature(ReturnTypeExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_returnor_is_not_abstract():
    assert not inspect.isabstract(b_ReturnOr)


def test_b_returnor_constructor_exists():
    assert callable(b_ReturnOr.__init__)


def test_b_returnor_constructor_args():
    sig = inspect.signature(b_ReturnOr.__init__)
    params = list(sig.parameters.keys())



def test_propertyexpr_is_not_abstract():
    assert not inspect.isabstract(PropertyExpr)


def test_propertyexpr_constructor_exists():
    assert callable(PropertyExpr.__init__)


def test_propertyexpr_constructor_args():
    sig = inspect.signature(PropertyExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_propertytyped_is_not_abstract():
    assert not inspect.isabstract(b_PropertyTyped)


def test_b_propertytyped_constructor_exists():
    assert callable(b_PropertyTyped.__init__)


def test_b_propertytyped_constructor_args():
    sig = inspect.signature(b_PropertyTyped.__init__)
    params = list(sig.parameters.keys())



def test_returnexpr_is_not_abstract():
    assert not inspect.isabstract(ReturnExpr)


def test_returnexpr_constructor_exists():
    assert callable(ReturnExpr.__init__)


def test_returnexpr_constructor_args():
    sig = inspect.signature(ReturnExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_neg_is_not_abstract():
    assert not inspect.isabstract(b_Neg)


def test_b_neg_constructor_exists():
    assert callable(b_Neg.__init__)


def test_b_neg_constructor_args():
    sig = inspect.signature(b_Neg.__init__)
    params = list(sig.parameters.keys())



def test_b_propertyrange_is_not_abstract():
    assert not inspect.isabstract(b_PropertyRange)


def test_b_propertyrange_constructor_exists():
    assert callable(b_PropertyRange.__init__)


def test_b_propertyrange_constructor_args():
    sig = inspect.signature(b_PropertyRange.__init__)
    params = list(sig.parameters.keys())



def test_return_is_not_abstract():
    assert not inspect.isabstract(Return)


def test_return_constructor_exists():
    assert callable(Return.__init__)


def test_return_constructor_args():
    sig = inspect.signature(Return.__init__)
    params = list(sig.parameters.keys())



def test_b_returntuple_is_not_abstract():
    assert not inspect.isabstract(b_ReturnTuple)


def test_b_returntuple_constructor_exists():
    assert callable(b_ReturnTuple.__init__)


def test_b_returntuple_constructor_args():
    sig = inspect.signature(b_ReturnTuple.__init__)
    params = list(sig.parameters.keys())



def test_b_returntypeexpr_is_not_abstract():
    assert not inspect.isabstract(b_ReturnTypeExpr)


def test_b_returntypeexpr_constructor_exists():
    assert callable(b_ReturnTypeExpr.__init__)


def test_b_returntypeexpr_constructor_args():
    sig = inspect.signature(b_ReturnTypeExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_returnexpr_is_not_abstract():
    assert not inspect.isabstract(b_ReturnExpr)


def test_b_returnexpr_constructor_exists():
    assert callable(b_ReturnExpr.__init__)


def test_b_returnexpr_constructor_args():
    sig = inspect.signature(b_ReturnExpr.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_b_beginbody_is_not_abstract():
    assert not inspect.isabstract(b_BeginBody)


def test_b_beginbody_constructor_exists():
    assert callable(b_BeginBody.__init__)


def test_b_beginbody_constructor_args():
    sig = inspect.signature(b_BeginBody.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_b_primitivetype_is_not_abstract():
    assert not inspect.isabstract(b_PrimitiveType)


def test_b_primitivetype_constructor_exists():
    assert callable(b_PrimitiveType.__init__)


def test_b_primitivetype_constructor_args():
    sig = inspect.signature(b_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_b_primitivetype_has_type():
    assert hasattr(b_PrimitiveType, "type")
    descriptor = None
    for klass in b_PrimitiveType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_b_simplecall_is_not_abstract():
    assert not inspect.isabstract(b_SimpleCall)


def test_b_simplecall_constructor_exists():
    assert callable(b_SimpleCall.__init__)


def test_b_simplecall_constructor_args():
    sig = inspect.signature(b_SimpleCall.__init__)
    params = list(sig.parameters.keys())



def test_b_eobject_is_not_abstract():
    assert not inspect.isabstract(b_EObject)


def test_b_eobject_constructor_exists():
    assert callable(b_EObject.__init__)


def test_b_eobject_constructor_args():
    sig = inspect.signature(b_EObject.__init__)
    params = list(sig.parameters.keys())



def test_beginbody_is_not_abstract():
    assert not inspect.isabstract(BeginBody)


def test_beginbody_constructor_exists():
    assert callable(BeginBody.__init__)


def test_beginbody_constructor_args():
    sig = inspect.signature(BeginBody.__init__)
    params = list(sig.parameters.keys())



def test_b_finalexpr_is_not_abstract():
    assert not inspect.isabstract(b_FinalExpr)


def test_b_finalexpr_constructor_exists():
    assert callable(b_FinalExpr.__init__)


def test_b_finalexpr_constructor_args():
    sig = inspect.signature(b_FinalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_caseexpr_is_not_abstract():
    assert not inspect.isabstract(b_CaseExpr)


def test_b_caseexpr_constructor_exists():
    assert callable(b_CaseExpr.__init__)


def test_b_caseexpr_constructor_args():
    sig = inspect.signature(b_CaseExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_operation_is_not_abstract():
    assert not inspect.isabstract(b_Operation)


def test_b_operation_constructor_exists():
    assert callable(b_Operation.__init__)


def test_b_operation_constructor_args():
    sig = inspect.signature(b_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_operation_has_name():
    assert hasattr(b_Operation, "name")
    descriptor = None
    for klass in b_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_preexpr_is_not_abstract():
    assert not inspect.isabstract(b_PreExpr)


def test_b_preexpr_constructor_exists():
    assert callable(b_PreExpr.__init__)


def test_b_preexpr_constructor_args():
    sig = inspect.signature(b_PreExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_condition_is_not_abstract():
    assert not inspect.isabstract(b_Condition)


def test_b_condition_constructor_exists():
    assert callable(b_Condition.__init__)


def test_b_condition_constructor_args():
    sig = inspect.signature(b_Condition.__init__)
    params = list(sig.parameters.keys())



def test_b_ifcond_is_not_abstract():
    assert not inspect.isabstract(b_IfCond)


def test_b_ifcond_constructor_exists():
    assert callable(b_IfCond.__init__)


def test_b_ifcond_constructor_args():
    sig = inspect.signature(b_IfCond.__init__)
    params = list(sig.parameters.keys())



def test_finalexpr_is_not_abstract():
    assert not inspect.isabstract(FinalExpr)


def test_finalexpr_constructor_exists():
    assert callable(FinalExpr.__init__)


def test_finalexpr_constructor_args():
    sig = inspect.signature(FinalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_statement_is_not_abstract():
    assert not inspect.isabstract(b_Statement)


def test_b_statement_constructor_exists():
    assert callable(b_Statement.__init__)


def test_b_statement_constructor_args():
    sig = inspect.signature(b_Statement.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_b_return_is_not_abstract():
    assert not inspect.isabstract(b_Return)


def test_b_return_constructor_exists():
    assert callable(b_Return.__init__)


def test_b_return_constructor_args():
    sig = inspect.signature(b_Return.__init__)
    params = list(sig.parameters.keys())



def test_b_case_is_not_abstract():
    assert not inspect.isabstract(b_Case)


def test_b_case_constructor_exists():
    assert callable(b_Case.__init__)


def test_b_case_constructor_args():
    sig = inspect.signature(b_Case.__init__)
    params = list(sig.parameters.keys())



def test_b_call_is_not_abstract():
    assert not inspect.isabstract(b_Call)


def test_b_call_constructor_exists():
    assert callable(b_Call.__init__)


def test_b_call_constructor_args():
    sig = inspect.signature(b_Call.__init__)
    params = list(sig.parameters.keys())



def test_b_assign_is_not_abstract():
    assert not inspect.isabstract(b_Assign)


def test_b_assign_constructor_exists():
    assert callable(b_Assign.__init__)


def test_b_assign_constructor_args():
    sig = inspect.signature(b_Assign.__init__)
    params = list(sig.parameters.keys())



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_b_begin_is_not_abstract():
    assert not inspect.isabstract(b_Begin)


def test_b_begin_constructor_exists():
    assert callable(b_Begin.__init__)


def test_b_begin_constructor_args():
    sig = inspect.signature(b_Begin.__init__)
    params = list(sig.parameters.keys())



def test_b_seq_is_not_abstract():
    assert not inspect.isabstract(b_Seq)


def test_b_seq_constructor_exists():
    assert callable(b_Seq.__init__)


def test_b_seq_constructor_args():
    sig = inspect.signature(b_Seq.__init__)
    params = list(sig.parameters.keys())



def test_b_pre_is_not_abstract():
    assert not inspect.isabstract(b_Pre)


def test_b_pre_constructor_exists():
    assert callable(b_Pre.__init__)


def test_b_pre_constructor_args():
    sig = inspect.signature(b_Pre.__init__)
    params = list(sig.parameters.keys())



def test_b_var_is_not_abstract():
    assert not inspect.isabstract(b_Var)


def test_b_var_constructor_exists():
    assert callable(b_Var.__init__)


def test_b_var_constructor_args():
    sig = inspect.signature(b_Var.__init__)
    params = list(sig.parameters.keys())



def test_b_if_is_not_abstract():
    assert not inspect.isabstract(b_If)


def test_b_if_constructor_exists():
    assert callable(b_If.__init__)


def test_b_if_constructor_args():
    sig = inspect.signature(b_If.__init__)
    params = list(sig.parameters.keys())



def test_b_skip_is_not_abstract():
    assert not inspect.isabstract(b_Skip)


def test_b_skip_constructor_exists():
    assert callable(b_Skip.__init__)


def test_b_skip_constructor_args():
    sig = inspect.signature(b_Skip.__init__)
    params = list(sig.parameters.keys())



def test_b_expr_is_not_abstract():
    assert not inspect.isabstract(b_Expr)


def test_b_expr_constructor_exists():
    assert callable(b_Expr.__init__)


def test_b_expr_constructor_args():
    sig = inspect.signature(b_Expr.__init__)
    params = list(sig.parameters.keys())



def test_b_body_is_not_abstract():
    assert not inspect.isabstract(b_Body)


def test_b_body_constructor_exists():
    assert callable(b_Body.__init__)


def test_b_body_constructor_args():
    sig = inspect.signature(b_Body.__init__)
    params = list(sig.parameters.keys())



def test_b_propertyexpr_is_not_abstract():
    assert not inspect.isabstract(b_PropertyExpr)


def test_b_propertyexpr_constructor_exists():
    assert callable(b_PropertyExpr.__init__)


def test_b_propertyexpr_constructor_args():
    sig = inspect.signature(b_PropertyExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_set_is_not_abstract():
    assert not inspect.isabstract(b_Set)


def test_b_set_constructor_exists():
    assert callable(b_Set.__init__)


def test_b_set_constructor_args():
    sig = inspect.signature(b_Set.__init__)
    params = list(sig.parameters.keys())



def test_arg_is_not_abstract():
    assert not inspect.isabstract(Arg)


def test_arg_constructor_exists():
    assert callable(Arg.__init__)


def test_arg_constructor_args():
    sig = inspect.signature(Arg.__init__)
    params = list(sig.parameters.keys())



def test_b_argminus_is_not_abstract():
    assert not inspect.isabstract(b_ArgMinus)


def test_b_argminus_constructor_exists():
    assert callable(b_ArgMinus.__init__)


def test_b_argminus_constructor_args():
    sig = inspect.signature(b_ArgMinus.__init__)
    params = list(sig.parameters.keys())



def test_b_stringliteral_is_not_abstract():
    assert not inspect.isabstract(b_StringLiteral)


def test_b_stringliteral_constructor_exists():
    assert callable(b_StringLiteral.__init__)


def test_b_stringliteral_constructor_args():
    sig = inspect.signature(b_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_b_stringliteral_has_value():
    assert hasattr(b_StringLiteral, "value")
    descriptor = None
    for klass in b_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_b_condand_is_not_abstract():
    assert not inspect.isabstract(b_CondAnd)


def test_b_condand_constructor_exists():
    assert callable(b_CondAnd.__init__)


def test_b_condand_constructor_args():
    sig = inspect.signature(b_CondAnd.__init__)
    params = list(sig.parameters.keys())



def test_b_condneg_is_not_abstract():
    assert not inspect.isabstract(b_CondNeg)


def test_b_condneg_constructor_exists():
    assert callable(b_CondNeg.__init__)


def test_b_condneg_constructor_args():
    sig = inspect.signature(b_CondNeg.__init__)
    params = list(sig.parameters.keys())



def test_b_condlessthan_is_not_abstract():
    assert not inspect.isabstract(b_CondLessThan)


def test_b_condlessthan_constructor_exists():
    assert callable(b_CondLessThan.__init__)


def test_b_condlessthan_constructor_args():
    sig = inspect.signature(b_CondLessThan.__init__)
    params = list(sig.parameters.keys())



def test_b_condeq_is_not_abstract():
    assert not inspect.isabstract(b_CondEq)


def test_b_condeq_constructor_exists():
    assert callable(b_CondEq.__init__)


def test_b_condeq_constructor_args():
    sig = inspect.signature(b_CondEq.__init__)
    params = list(sig.parameters.keys())



def test_b_boolliteral_is_not_abstract():
    assert not inspect.isabstract(b_BoolLiteral)


def test_b_boolliteral_constructor_exists():
    assert callable(b_BoolLiteral.__init__)


def test_b_boolliteral_constructor_args():
    sig = inspect.signature(b_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_b_boolliteral_has_value():
    assert hasattr(b_BoolLiteral, "value")
    descriptor = None
    for klass in b_BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_b_boolliteral_has_constant():
    assert hasattr(b_BoolLiteral, "constant")
    descriptor = None
    for klass in b_BoolLiteral.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_b_condminus_is_not_abstract():
    assert not inspect.isabstract(b_CondMinus)


def test_b_condminus_constructor_exists():
    assert callable(b_CondMinus.__init__)


def test_b_condminus_constructor_args():
    sig = inspect.signature(b_CondMinus.__init__)
    params = list(sig.parameters.keys())



def test_b_arg_is_not_abstract():
    assert not inspect.isabstract(b_Arg)


def test_b_arg_constructor_exists():
    assert callable(b_Arg.__init__)


def test_b_arg_constructor_args():
    sig = inspect.signature(b_Arg.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpr_is_not_abstract():
    assert not inspect.isabstract(LogicalExpr)


def test_logicalexpr_constructor_exists():
    assert callable(LogicalExpr.__init__)


def test_logicalexpr_constructor_args():
    sig = inspect.signature(LogicalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_intliteral_is_not_abstract():
    assert not inspect.isabstract(b_IntLiteral)


def test_b_intliteral_constructor_exists():
    assert callable(b_IntLiteral.__init__)


def test_b_intliteral_constructor_args():
    sig = inspect.signature(b_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_b_intliteral_has_value():
    assert hasattr(b_IntLiteral, "value")
    descriptor = None
    for klass in b_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_b_implyexpr_is_not_abstract():
    assert not inspect.isabstract(b_ImplyExpr)


def test_b_implyexpr_constructor_exists():
    assert callable(b_ImplyExpr.__init__)


def test_b_implyexpr_constructor_args():
    sig = inspect.signature(b_ImplyExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_typeconstraint_is_not_abstract():
    assert not inspect.isabstract(b_TypeConstraint)


def test_b_typeconstraint_constructor_exists():
    assert callable(b_TypeConstraint.__init__)


def test_b_typeconstraint_constructor_args():
    sig = inspect.signature(b_TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_b_andexpr_is_not_abstract():
    assert not inspect.isabstract(b_AndExpr)


def test_b_andexpr_constructor_exists():
    assert callable(b_AndExpr.__init__)


def test_b_andexpr_constructor_args():
    sig = inspect.signature(b_AndExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_ref_is_not_abstract():
    assert not inspect.isabstract(b_Ref)


def test_b_ref_constructor_exists():
    assert callable(b_Ref.__init__)


def test_b_ref_constructor_args():
    sig = inspect.signature(b_Ref.__init__)
    params = list(sig.parameters.keys())



def test_b_booltest_is_not_abstract():
    assert not inspect.isabstract(b_BoolTest)


def test_b_booltest_constructor_exists():
    assert callable(b_BoolTest.__init__)


def test_b_booltest_constructor_args():
    sig = inspect.signature(b_BoolTest.__init__)
    params = list(sig.parameters.keys())



def test_b_inequalityexpr_is_not_abstract():
    assert not inspect.isabstract(b_InequalityExpr)


def test_b_inequalityexpr_constructor_exists():
    assert callable(b_InequalityExpr.__init__)


def test_b_inequalityexpr_constructor_args():
    sig = inspect.signature(b_InequalityExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_b_inequalityexpr_has_op():
    assert hasattr(b_InequalityExpr, "op")
    descriptor = None
    for klass in b_InequalityExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_b_negexpr_is_not_abstract():
    assert not inspect.isabstract(b_NegExpr)


def test_b_negexpr_constructor_exists():
    assert callable(b_NegExpr.__init__)


def test_b_negexpr_constructor_args():
    sig = inspect.signature(b_NegExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_constantexpr_is_not_abstract():
    assert not inspect.isabstract(b_ConstantExpr)


def test_b_constantexpr_constructor_exists():
    assert callable(b_ConstantExpr.__init__)


def test_b_constantexpr_constructor_args():
    sig = inspect.signature(b_ConstantExpr.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_b_constantexpr_has_constant():
    assert hasattr(b_ConstantExpr, "constant")
    descriptor = None
    for klass in b_ConstantExpr.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_b_equalexpr_is_not_abstract():
    assert not inspect.isabstract(b_EqualExpr)


def test_b_equalexpr_constructor_exists():
    assert callable(b_EqualExpr.__init__)


def test_b_equalexpr_constructor_args():
    sig = inspect.signature(b_EqualExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_definitioncall_is_not_abstract():
    assert not inspect.isabstract(b_DefinitionCall)


def test_b_definitioncall_constructor_exists():
    assert callable(b_DefinitionCall.__init__)


def test_b_definitioncall_constructor_args():
    sig = inspect.signature(b_DefinitionCall.__init__)
    params = list(sig.parameters.keys())



def test_b_logicalexpr_is_not_abstract():
    assert not inspect.isabstract(b_LogicalExpr)


def test_b_logicalexpr_constructor_exists():
    assert callable(b_LogicalExpr.__init__)


def test_b_logicalexpr_constructor_args():
    sig = inspect.signature(b_LogicalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_definition_is_not_abstract():
    assert not inspect.isabstract(b_Definition)


def test_b_definition_constructor_exists():
    assert callable(b_Definition.__init__)


def test_b_definition_constructor_args():
    sig = inspect.signature(b_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_definition_has_name():
    assert hasattr(b_Definition, "name")
    descriptor = None
    for klass in b_Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_assertionexpr_is_not_abstract():
    assert not inspect.isabstract(b_AssertionExpr)


def test_b_assertionexpr_constructor_exists():
    assert callable(b_AssertionExpr.__init__)


def test_b_assertionexpr_constructor_args():
    sig = inspect.signature(b_AssertionExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_range_is_not_abstract():
    assert not inspect.isabstract(b_Range)


def test_b_range_constructor_exists():
    assert callable(b_Range.__init__)


def test_b_range_constructor_args():
    sig = inspect.signature(b_Range.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_b_range_has_lowerBound():
    assert hasattr(b_Range, "lowerBound")
    descriptor = None
    for klass in b_Range.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_b_values_is_not_abstract():
    assert not inspect.isabstract(b_Values)


def test_b_values_constructor_exists():
    assert callable(b_Values.__init__)


def test_b_values_constructor_args():
    sig = inspect.signature(b_Values.__init__)
    params = list(sig.parameters.keys())



def test_b_imports_is_not_abstract():
    assert not inspect.isabstract(b_Imports)


def test_b_imports_constructor_exists():
    assert callable(b_Imports.__init__)


def test_b_imports_constructor_args():
    sig = inspect.signature(b_Imports.__init__)
    params = list(sig.parameters.keys())



def test_b_sets_is_not_abstract():
    assert not inspect.isabstract(b_Sets)


def test_b_sets_constructor_exists():
    assert callable(b_Sets.__init__)


def test_b_sets_constructor_args():
    sig = inspect.signature(b_Sets.__init__)
    params = list(sig.parameters.keys())



def test_b_initialisationexpr_is_not_abstract():
    assert not inspect.isabstract(b_InitialisationExpr)


def test_b_initialisationexpr_constructor_exists():
    assert callable(b_InitialisationExpr.__init__)


def test_b_initialisationexpr_constructor_args():
    sig = inspect.signature(b_InitialisationExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_type_is_not_abstract():
    assert not inspect.isabstract(b_Type)


def test_b_type_constructor_exists():
    assert callable(b_Type.__init__)


def test_b_type_constructor_args():
    sig = inspect.signature(b_Type.__init__)
    params = list(sig.parameters.keys())



def test_b_invariantexpr_is_not_abstract():
    assert not inspect.isabstract(b_InvariantExpr)


def test_b_invariantexpr_constructor_exists():
    assert callable(b_InvariantExpr.__init__)


def test_b_invariantexpr_constructor_args():
    sig = inspect.signature(b_InvariantExpr.__init__)
    params = list(sig.parameters.keys())



def test_b_variable_is_not_abstract():
    assert not inspect.isabstract(b_Variable)


def test_b_variable_constructor_exists():
    assert callable(b_Variable.__init__)


def test_b_variable_constructor_args():
    sig = inspect.signature(b_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_variable_has_name():
    assert hasattr(b_Variable, "name")
    descriptor = None
    for klass in b_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_valueexpr_is_not_abstract():
    assert not inspect.isabstract(b_ValueExpr)


def test_b_valueexpr_constructor_exists():
    assert callable(b_ValueExpr.__init__)


def test_b_valueexpr_constructor_args():
    sig = inspect.signature(b_ValueExpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_b_valueexpr_has_value():
    assert hasattr(b_ValueExpr, "value")
    descriptor = None
    for klass in b_ValueExpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_b_localoperations_is_not_abstract():
    assert not inspect.isabstract(b_LocalOperations)


def test_b_localoperations_constructor_exists():
    assert callable(b_LocalOperations.__init__)


def test_b_localoperations_constructor_args():
    sig = inspect.signature(b_LocalOperations.__init__)
    params = list(sig.parameters.keys())



def test_b_assertions_is_not_abstract():
    assert not inspect.isabstract(b_Assertions)


def test_b_assertions_constructor_exists():
    assert callable(b_Assertions.__init__)


def test_b_assertions_constructor_args():
    sig = inspect.signature(b_Assertions.__init__)
    params = list(sig.parameters.keys())



def test_b_initialisation_is_not_abstract():
    assert not inspect.isabstract(b_Initialisation)


def test_b_initialisation_constructor_exists():
    assert callable(b_Initialisation.__init__)


def test_b_initialisation_constructor_args():
    sig = inspect.signature(b_Initialisation.__init__)
    params = list(sig.parameters.keys())



def test_b_invariant_is_not_abstract():
    assert not inspect.isabstract(b_Invariant)


def test_b_invariant_constructor_exists():
    assert callable(b_Invariant.__init__)


def test_b_invariant_constructor_args():
    sig = inspect.signature(b_Invariant.__init__)
    params = list(sig.parameters.keys())



def test_b_concretevariables_is_not_abstract():
    assert not inspect.isabstract(b_ConcreteVariables)


def test_b_concretevariables_constructor_exists():
    assert callable(b_ConcreteVariables.__init__)


def test_b_concretevariables_constructor_args():
    sig = inspect.signature(b_ConcreteVariables.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_b_implementation_is_not_abstract():
    assert not inspect.isabstract(b_Implementation)


def test_b_implementation_constructor_exists():
    assert callable(b_Implementation.__init__)


def test_b_implementation_constructor_args():
    sig = inspect.signature(b_Implementation.__init__)
    params = list(sig.parameters.keys())



def test_b_machine_is_not_abstract():
    assert not inspect.isabstract(b_Machine)


def test_b_machine_constructor_exists():
    assert callable(b_Machine.__init__)


def test_b_machine_constructor_args():
    sig = inspect.signature(b_Machine.__init__)
    params = list(sig.parameters.keys())



def test_b_operations_is_not_abstract():
    assert not inspect.isabstract(b_Operations)


def test_b_operations_constructor_exists():
    assert callable(b_Operations.__init__)


def test_b_operations_constructor_args():
    sig = inspect.signature(b_Operations.__init__)
    params = list(sig.parameters.keys())



def test_b_properties_is_not_abstract():
    assert not inspect.isabstract(b_Properties)


def test_b_properties_constructor_exists():
    assert callable(b_Properties.__init__)


def test_b_properties_constructor_args():
    sig = inspect.signature(b_Properties.__init__)
    params = list(sig.parameters.keys())



def test_b_definitions_is_not_abstract():
    assert not inspect.isabstract(b_Definitions)


def test_b_definitions_constructor_exists():
    assert callable(b_Definitions.__init__)


def test_b_definitions_constructor_args():
    sig = inspect.signature(b_Definitions.__init__)
    params = list(sig.parameters.keys())



def test_b_concreteconstants_is_not_abstract():
    assert not inspect.isabstract(b_ConcreteConstants)


def test_b_concreteconstants_constructor_exists():
    assert callable(b_ConcreteConstants.__init__)


def test_b_concreteconstants_constructor_args():
    sig = inspect.signature(b_ConcreteConstants.__init__)
    params = list(sig.parameters.keys())



def test_b_sees_is_not_abstract():
    assert not inspect.isabstract(b_Sees)


def test_b_sees_constructor_exists():
    assert callable(b_Sees.__init__)


def test_b_sees_constructor_args():
    sig = inspect.signature(b_Sees.__init__)
    params = list(sig.parameters.keys())



def test_b_abstraction_is_not_abstract():
    assert not inspect.isabstract(b_Abstraction)


def test_b_abstraction_constructor_exists():
    assert callable(b_Abstraction.__init__)


def test_b_abstraction_constructor_args():
    sig = inspect.signature(b_Abstraction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_abstraction_has_name():
    assert hasattr(b_Abstraction, "name")
    descriptor = None
    for klass in b_Abstraction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_inequalityop_exists():
    # Check that the Enumeration exists
    assert InequalityOp is not None

def test_inequalityop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InequalityOp]
    expected_literals = [
        "LESS_EQ",
        "LESS",
        "GREATER_EQ",
        "GREATER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InequalityOp"

def test_primitivetypeenum_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypeEnum is not None

def test_primitivetypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypeEnum]
    expected_literals = [
        "NAT",
        "STRING",
        "BOOL",
        "NAT1",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypeEnum"

def test_boolliteralenum_exists():
    # Check that the Enumeration exists
    assert BoolLiteralEnum is not None

def test_boolliteralenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoolLiteralEnum]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoolLiteralEnum"


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
ReturnTypeExpr_strategy = st.builds(
    ReturnTypeExpr,
)
b_ReturnOr_strategy = st.builds(
    b_ReturnOr,
)
PropertyExpr_strategy = st.builds(
    PropertyExpr,
)
b_PropertyTyped_strategy = st.builds(
    b_PropertyTyped,
)
ReturnExpr_strategy = st.builds(
    ReturnExpr,
)
b_Neg_strategy = st.builds(
    b_Neg,
)
b_PropertyRange_strategy = st.builds(
    b_PropertyRange,
)
Return_strategy = st.builds(
    Return,
)
b_ReturnTuple_strategy = st.builds(
    b_ReturnTuple,
)
b_ReturnTypeExpr_strategy = st.builds(
    b_ReturnTypeExpr,
)
b_ReturnExpr_strategy = st.builds(
    b_ReturnExpr,
)
Statement_strategy = st.builds(
    Statement,
)
b_BeginBody_strategy = st.builds(
    b_BeginBody,
)
Type_strategy = st.builds(
    Type,
)
b_PrimitiveType_strategy = st.builds(
    b_PrimitiveType,
    type=
        safe_text
)
b_SimpleCall_strategy = st.builds(
    b_SimpleCall,
)
b_EObject_strategy = st.builds(
    b_EObject,
)
BeginBody_strategy = st.builds(
    BeginBody,
)
b_FinalExpr_strategy = st.builds(
    b_FinalExpr,
)
b_CaseExpr_strategy = st.builds(
    b_CaseExpr,
)
b_Operation_strategy = st.builds(
    b_Operation,
    name=
        safe_text
)
b_PreExpr_strategy = st.builds(
    b_PreExpr,
)
b_Condition_strategy = st.builds(
    b_Condition,
)
b_IfCond_strategy = st.builds(
    b_IfCond,
)
FinalExpr_strategy = st.builds(
    FinalExpr,
)
b_Statement_strategy = st.builds(
    b_Statement,
)
Expr_strategy = st.builds(
    Expr,
)
b_Return_strategy = st.builds(
    b_Return,
)
b_Case_strategy = st.builds(
    b_Case,
)
b_Call_strategy = st.builds(
    b_Call,
)
b_Assign_strategy = st.builds(
    b_Assign,
)
Body_strategy = st.builds(
    Body,
)
b_Begin_strategy = st.builds(
    b_Begin,
)
b_Seq_strategy = st.builds(
    b_Seq,
)
b_Pre_strategy = st.builds(
    b_Pre,
)
b_Var_strategy = st.builds(
    b_Var,
)
b_If_strategy = st.builds(
    b_If,
)
b_Skip_strategy = st.builds(
    b_Skip,
)
b_Expr_strategy = st.builds(
    b_Expr,
)
b_Body_strategy = st.builds(
    b_Body,
)
b_PropertyExpr_strategy = st.builds(
    b_PropertyExpr,
)
b_Set_strategy = st.builds(
    b_Set,
)
Arg_strategy = st.builds(
    Arg,
)
b_ArgMinus_strategy = st.builds(
    b_ArgMinus,
)
b_StringLiteral_strategy = st.builds(
    b_StringLiteral,
    value=
        safe_text
)
Condition_strategy = st.builds(
    Condition,
)
b_CondAnd_strategy = st.builds(
    b_CondAnd,
)
b_CondNeg_strategy = st.builds(
    b_CondNeg,
)
b_CondLessThan_strategy = st.builds(
    b_CondLessThan,
)
b_CondEq_strategy = st.builds(
    b_CondEq,
)
b_BoolLiteral_strategy = st.builds(
    b_BoolLiteral,
    value=
        safe_text,
    constant=
        safe_text
)
b_CondMinus_strategy = st.builds(
    b_CondMinus,
)
b_Arg_strategy = st.builds(
    b_Arg,
)
LogicalExpr_strategy = st.builds(
    LogicalExpr,
)
b_IntLiteral_strategy = st.builds(
    b_IntLiteral,
    value=
        st.integers()
)
b_ImplyExpr_strategy = st.builds(
    b_ImplyExpr,
)
b_TypeConstraint_strategy = st.builds(
    b_TypeConstraint,
)
b_AndExpr_strategy = st.builds(
    b_AndExpr,
)
b_Ref_strategy = st.builds(
    b_Ref,
)
b_BoolTest_strategy = st.builds(
    b_BoolTest,
)
b_InequalityExpr_strategy = st.builds(
    b_InequalityExpr,
    op=
        safe_text
)
b_NegExpr_strategy = st.builds(
    b_NegExpr,
)
b_ConstantExpr_strategy = st.builds(
    b_ConstantExpr,
    constant=
        safe_text
)
b_EqualExpr_strategy = st.builds(
    b_EqualExpr,
)
b_DefinitionCall_strategy = st.builds(
    b_DefinitionCall,
)
b_LogicalExpr_strategy = st.builds(
    b_LogicalExpr,
)
b_Definition_strategy = st.builds(
    b_Definition,
    name=
        safe_text
)
b_AssertionExpr_strategy = st.builds(
    b_AssertionExpr,
)
b_Range_strategy = st.builds(
    b_Range,
    lowerBound=
        st.integers()
)
b_Values_strategy = st.builds(
    b_Values,
)
b_Imports_strategy = st.builds(
    b_Imports,
)
b_Sets_strategy = st.builds(
    b_Sets,
)
b_InitialisationExpr_strategy = st.builds(
    b_InitialisationExpr,
)
b_Type_strategy = st.builds(
    b_Type,
)
b_InvariantExpr_strategy = st.builds(
    b_InvariantExpr,
)
b_Variable_strategy = st.builds(
    b_Variable,
    name=
        safe_text
)
b_ValueExpr_strategy = st.builds(
    b_ValueExpr,
    value=
        safe_text
)
b_LocalOperations_strategy = st.builds(
    b_LocalOperations,
)
b_Assertions_strategy = st.builds(
    b_Assertions,
)
b_Initialisation_strategy = st.builds(
    b_Initialisation,
)
b_Invariant_strategy = st.builds(
    b_Invariant,
)
b_ConcreteVariables_strategy = st.builds(
    b_ConcreteVariables,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
b_Implementation_strategy = st.builds(
    b_Implementation,
)
b_Machine_strategy = st.builds(
    b_Machine,
)
b_Operations_strategy = st.builds(
    b_Operations,
)
b_Properties_strategy = st.builds(
    b_Properties,
)
b_Definitions_strategy = st.builds(
    b_Definitions,
)
b_ConcreteConstants_strategy = st.builds(
    b_ConcreteConstants,
)
b_Sees_strategy = st.builds(
    b_Sees,
)
b_Abstraction_strategy = st.builds(
    b_Abstraction,
    name=
        safe_text
)

@given(instance=ReturnTypeExpr_strategy)
@settings(max_examples=50)
def test_returntypeexpr_instantiation(instance):
    assert isinstance(instance, ReturnTypeExpr)

@given(instance=b_ReturnOr_strategy)
@settings(max_examples=50)
def test_b_returnor_instantiation(instance):
    assert isinstance(instance, b_ReturnOr)

@given(instance=PropertyExpr_strategy)
@settings(max_examples=50)
def test_propertyexpr_instantiation(instance):
    assert isinstance(instance, PropertyExpr)

@given(instance=b_PropertyTyped_strategy)
@settings(max_examples=50)
def test_b_propertytyped_instantiation(instance):
    assert isinstance(instance, b_PropertyTyped)

@given(instance=ReturnExpr_strategy)
@settings(max_examples=50)
def test_returnexpr_instantiation(instance):
    assert isinstance(instance, ReturnExpr)

@given(instance=b_Neg_strategy)
@settings(max_examples=50)
def test_b_neg_instantiation(instance):
    assert isinstance(instance, b_Neg)

@given(instance=b_PropertyRange_strategy)
@settings(max_examples=50)
def test_b_propertyrange_instantiation(instance):
    assert isinstance(instance, b_PropertyRange)

@given(instance=Return_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, Return)

@given(instance=b_ReturnTuple_strategy)
@settings(max_examples=50)
def test_b_returntuple_instantiation(instance):
    assert isinstance(instance, b_ReturnTuple)

@given(instance=b_ReturnTypeExpr_strategy)
@settings(max_examples=50)
def test_b_returntypeexpr_instantiation(instance):
    assert isinstance(instance, b_ReturnTypeExpr)

@given(instance=b_ReturnExpr_strategy)
@settings(max_examples=50)
def test_b_returnexpr_instantiation(instance):
    assert isinstance(instance, b_ReturnExpr)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=b_BeginBody_strategy)
@settings(max_examples=50)
def test_b_beginbody_instantiation(instance):
    assert isinstance(instance, b_BeginBody)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=b_PrimitiveType_strategy)
@settings(max_examples=50)
def test_b_primitivetype_instantiation(instance):
    assert isinstance(instance, b_PrimitiveType)



@given(instance=b_PrimitiveType_strategy)
def test_b_primitivetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=b_SimpleCall_strategy)
@settings(max_examples=50)
def test_b_simplecall_instantiation(instance):
    assert isinstance(instance, b_SimpleCall)

@given(instance=b_EObject_strategy)
@settings(max_examples=50)
def test_b_eobject_instantiation(instance):
    assert isinstance(instance, b_EObject)

@given(instance=BeginBody_strategy)
@settings(max_examples=50)
def test_beginbody_instantiation(instance):
    assert isinstance(instance, BeginBody)

@given(instance=b_FinalExpr_strategy)
@settings(max_examples=50)
def test_b_finalexpr_instantiation(instance):
    assert isinstance(instance, b_FinalExpr)

@given(instance=b_CaseExpr_strategy)
@settings(max_examples=50)
def test_b_caseexpr_instantiation(instance):
    assert isinstance(instance, b_CaseExpr)

@given(instance=b_Operation_strategy)
@settings(max_examples=50)
def test_b_operation_instantiation(instance):
    assert isinstance(instance, b_Operation)



@given(instance=b_Operation_strategy)
def test_b_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b_PreExpr_strategy)
@settings(max_examples=50)
def test_b_preexpr_instantiation(instance):
    assert isinstance(instance, b_PreExpr)

@given(instance=b_Condition_strategy)
@settings(max_examples=50)
def test_b_condition_instantiation(instance):
    assert isinstance(instance, b_Condition)

@given(instance=b_IfCond_strategy)
@settings(max_examples=50)
def test_b_ifcond_instantiation(instance):
    assert isinstance(instance, b_IfCond)

@given(instance=FinalExpr_strategy)
@settings(max_examples=50)
def test_finalexpr_instantiation(instance):
    assert isinstance(instance, FinalExpr)

@given(instance=b_Statement_strategy)
@settings(max_examples=50)
def test_b_statement_instantiation(instance):
    assert isinstance(instance, b_Statement)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=b_Return_strategy)
@settings(max_examples=50)
def test_b_return_instantiation(instance):
    assert isinstance(instance, b_Return)

@given(instance=b_Case_strategy)
@settings(max_examples=50)
def test_b_case_instantiation(instance):
    assert isinstance(instance, b_Case)

@given(instance=b_Call_strategy)
@settings(max_examples=50)
def test_b_call_instantiation(instance):
    assert isinstance(instance, b_Call)

@given(instance=b_Assign_strategy)
@settings(max_examples=50)
def test_b_assign_instantiation(instance):
    assert isinstance(instance, b_Assign)

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=b_Begin_strategy)
@settings(max_examples=50)
def test_b_begin_instantiation(instance):
    assert isinstance(instance, b_Begin)

@given(instance=b_Seq_strategy)
@settings(max_examples=50)
def test_b_seq_instantiation(instance):
    assert isinstance(instance, b_Seq)

@given(instance=b_Pre_strategy)
@settings(max_examples=50)
def test_b_pre_instantiation(instance):
    assert isinstance(instance, b_Pre)

@given(instance=b_Var_strategy)
@settings(max_examples=50)
def test_b_var_instantiation(instance):
    assert isinstance(instance, b_Var)

@given(instance=b_If_strategy)
@settings(max_examples=50)
def test_b_if_instantiation(instance):
    assert isinstance(instance, b_If)

@given(instance=b_Skip_strategy)
@settings(max_examples=50)
def test_b_skip_instantiation(instance):
    assert isinstance(instance, b_Skip)

@given(instance=b_Expr_strategy)
@settings(max_examples=50)
def test_b_expr_instantiation(instance):
    assert isinstance(instance, b_Expr)

@given(instance=b_Body_strategy)
@settings(max_examples=50)
def test_b_body_instantiation(instance):
    assert isinstance(instance, b_Body)

@given(instance=b_PropertyExpr_strategy)
@settings(max_examples=50)
def test_b_propertyexpr_instantiation(instance):
    assert isinstance(instance, b_PropertyExpr)

@given(instance=b_Set_strategy)
@settings(max_examples=50)
def test_b_set_instantiation(instance):
    assert isinstance(instance, b_Set)

@given(instance=Arg_strategy)
@settings(max_examples=50)
def test_arg_instantiation(instance):
    assert isinstance(instance, Arg)

@given(instance=b_ArgMinus_strategy)
@settings(max_examples=50)
def test_b_argminus_instantiation(instance):
    assert isinstance(instance, b_ArgMinus)

@given(instance=b_StringLiteral_strategy)
@settings(max_examples=50)
def test_b_stringliteral_instantiation(instance):
    assert isinstance(instance, b_StringLiteral)



@given(instance=b_StringLiteral_strategy)
def test_b_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=b_CondAnd_strategy)
@settings(max_examples=50)
def test_b_condand_instantiation(instance):
    assert isinstance(instance, b_CondAnd)

@given(instance=b_CondNeg_strategy)
@settings(max_examples=50)
def test_b_condneg_instantiation(instance):
    assert isinstance(instance, b_CondNeg)

@given(instance=b_CondLessThan_strategy)
@settings(max_examples=50)
def test_b_condlessthan_instantiation(instance):
    assert isinstance(instance, b_CondLessThan)

@given(instance=b_CondEq_strategy)
@settings(max_examples=50)
def test_b_condeq_instantiation(instance):
    assert isinstance(instance, b_CondEq)

@given(instance=b_BoolLiteral_strategy)
@settings(max_examples=50)
def test_b_boolliteral_instantiation(instance):
    assert isinstance(instance, b_BoolLiteral)



@given(instance=b_BoolLiteral_strategy)
def test_b_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=b_BoolLiteral_strategy)
def test_b_boolliteral_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=b_CondMinus_strategy)
@settings(max_examples=50)
def test_b_condminus_instantiation(instance):
    assert isinstance(instance, b_CondMinus)

@given(instance=b_Arg_strategy)
@settings(max_examples=50)
def test_b_arg_instantiation(instance):
    assert isinstance(instance, b_Arg)

@given(instance=LogicalExpr_strategy)
@settings(max_examples=50)
def test_logicalexpr_instantiation(instance):
    assert isinstance(instance, LogicalExpr)

@given(instance=b_IntLiteral_strategy)
@settings(max_examples=50)
def test_b_intliteral_instantiation(instance):
    assert isinstance(instance, b_IntLiteral)



@given(instance=b_IntLiteral_strategy)
def test_b_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=b_ImplyExpr_strategy)
@settings(max_examples=50)
def test_b_implyexpr_instantiation(instance):
    assert isinstance(instance, b_ImplyExpr)

@given(instance=b_TypeConstraint_strategy)
@settings(max_examples=50)
def test_b_typeconstraint_instantiation(instance):
    assert isinstance(instance, b_TypeConstraint)

@given(instance=b_AndExpr_strategy)
@settings(max_examples=50)
def test_b_andexpr_instantiation(instance):
    assert isinstance(instance, b_AndExpr)

@given(instance=b_Ref_strategy)
@settings(max_examples=50)
def test_b_ref_instantiation(instance):
    assert isinstance(instance, b_Ref)

@given(instance=b_BoolTest_strategy)
@settings(max_examples=50)
def test_b_booltest_instantiation(instance):
    assert isinstance(instance, b_BoolTest)

@given(instance=b_InequalityExpr_strategy)
@settings(max_examples=50)
def test_b_inequalityexpr_instantiation(instance):
    assert isinstance(instance, b_InequalityExpr)



@given(instance=b_InequalityExpr_strategy)
def test_b_inequalityexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=b_NegExpr_strategy)
@settings(max_examples=50)
def test_b_negexpr_instantiation(instance):
    assert isinstance(instance, b_NegExpr)

@given(instance=b_ConstantExpr_strategy)
@settings(max_examples=50)
def test_b_constantexpr_instantiation(instance):
    assert isinstance(instance, b_ConstantExpr)



@given(instance=b_ConstantExpr_strategy)
def test_b_constantexpr_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=b_EqualExpr_strategy)
@settings(max_examples=50)
def test_b_equalexpr_instantiation(instance):
    assert isinstance(instance, b_EqualExpr)

@given(instance=b_DefinitionCall_strategy)
@settings(max_examples=50)
def test_b_definitioncall_instantiation(instance):
    assert isinstance(instance, b_DefinitionCall)

@given(instance=b_LogicalExpr_strategy)
@settings(max_examples=50)
def test_b_logicalexpr_instantiation(instance):
    assert isinstance(instance, b_LogicalExpr)

@given(instance=b_Definition_strategy)
@settings(max_examples=50)
def test_b_definition_instantiation(instance):
    assert isinstance(instance, b_Definition)



@given(instance=b_Definition_strategy)
def test_b_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b_AssertionExpr_strategy)
@settings(max_examples=50)
def test_b_assertionexpr_instantiation(instance):
    assert isinstance(instance, b_AssertionExpr)

@given(instance=b_Range_strategy)
@settings(max_examples=50)
def test_b_range_instantiation(instance):
    assert isinstance(instance, b_Range)



@given(instance=b_Range_strategy)
def test_b_range_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=b_Values_strategy)
@settings(max_examples=50)
def test_b_values_instantiation(instance):
    assert isinstance(instance, b_Values)

@given(instance=b_Imports_strategy)
@settings(max_examples=50)
def test_b_imports_instantiation(instance):
    assert isinstance(instance, b_Imports)

@given(instance=b_Sets_strategy)
@settings(max_examples=50)
def test_b_sets_instantiation(instance):
    assert isinstance(instance, b_Sets)

@given(instance=b_InitialisationExpr_strategy)
@settings(max_examples=50)
def test_b_initialisationexpr_instantiation(instance):
    assert isinstance(instance, b_InitialisationExpr)

@given(instance=b_Type_strategy)
@settings(max_examples=50)
def test_b_type_instantiation(instance):
    assert isinstance(instance, b_Type)

@given(instance=b_InvariantExpr_strategy)
@settings(max_examples=50)
def test_b_invariantexpr_instantiation(instance):
    assert isinstance(instance, b_InvariantExpr)

@given(instance=b_Variable_strategy)
@settings(max_examples=50)
def test_b_variable_instantiation(instance):
    assert isinstance(instance, b_Variable)



@given(instance=b_Variable_strategy)
def test_b_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b_ValueExpr_strategy)
@settings(max_examples=50)
def test_b_valueexpr_instantiation(instance):
    assert isinstance(instance, b_ValueExpr)



@given(instance=b_ValueExpr_strategy)
def test_b_valueexpr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=b_LocalOperations_strategy)
@settings(max_examples=50)
def test_b_localoperations_instantiation(instance):
    assert isinstance(instance, b_LocalOperations)

@given(instance=b_Assertions_strategy)
@settings(max_examples=50)
def test_b_assertions_instantiation(instance):
    assert isinstance(instance, b_Assertions)

@given(instance=b_Initialisation_strategy)
@settings(max_examples=50)
def test_b_initialisation_instantiation(instance):
    assert isinstance(instance, b_Initialisation)

@given(instance=b_Invariant_strategy)
@settings(max_examples=50)
def test_b_invariant_instantiation(instance):
    assert isinstance(instance, b_Invariant)

@given(instance=b_ConcreteVariables_strategy)
@settings(max_examples=50)
def test_b_concretevariables_instantiation(instance):
    assert isinstance(instance, b_ConcreteVariables)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=b_Implementation_strategy)
@settings(max_examples=50)
def test_b_implementation_instantiation(instance):
    assert isinstance(instance, b_Implementation)

@given(instance=b_Machine_strategy)
@settings(max_examples=50)
def test_b_machine_instantiation(instance):
    assert isinstance(instance, b_Machine)

@given(instance=b_Operations_strategy)
@settings(max_examples=50)
def test_b_operations_instantiation(instance):
    assert isinstance(instance, b_Operations)

@given(instance=b_Properties_strategy)
@settings(max_examples=50)
def test_b_properties_instantiation(instance):
    assert isinstance(instance, b_Properties)

@given(instance=b_Definitions_strategy)
@settings(max_examples=50)
def test_b_definitions_instantiation(instance):
    assert isinstance(instance, b_Definitions)

@given(instance=b_ConcreteConstants_strategy)
@settings(max_examples=50)
def test_b_concreteconstants_instantiation(instance):
    assert isinstance(instance, b_ConcreteConstants)

@given(instance=b_Sees_strategy)
@settings(max_examples=50)
def test_b_sees_instantiation(instance):
    assert isinstance(instance, b_Sees)

@given(instance=b_Abstraction_strategy)
@settings(max_examples=50)
def test_b_abstraction_instantiation(instance):
    assert isinstance(instance, b_Abstraction)



@given(instance=b_Abstraction_strategy)
def test_b_abstraction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
