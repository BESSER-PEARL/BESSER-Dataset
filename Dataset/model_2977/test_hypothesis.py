import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    robochart_NamedExpression,
    BinaryExpression,
    robochart_Plus,
    robochart_Different,
    robochart_Cat,
    robochart_Mult,
    robochart_LessThan,
    robochart_GreaterThan,
    robochart_Modulus,
    robochart_Implies,
    robochart_LessOrEqual,
    robochart_Div,
    robochart_Minus,
    robochart_GreaterOrEqual,
    robochart_Equals,
    robochart_Or,
    robochart_And,
    robochart_Iff,
    LambdaExp,
    robochart_DefiniteDescription,
    QuantifierExpression,
    robochart_Exists,
    robochart_Forall,
    Expression,
    robochart_InExp,
    robochart_IfExpression,
    robochart_VarExp,
    robochart_TupleExp,
    robochart_BooleanExp,
    robochart_IntegerExp,
    robochart_LetExpression,
    robochart_ToExp,
    robochart_IsExp,
    robochart_ArrayExp,
    robochart_LambdaExp,
    robochart_Not,
    robochart_TypeExp,
    robochart_QuantifierExpression,
    robochart_ElseExp,
    robochart_StateClockExp,
    robochart_SetExp,
    robochart_EnumExp,
    robochart_SeqExp,
    robochart_SetComp,
    robochart_IdExp,
    robochart_AsExp,
    robochart_BinaryExpression,
    robochart_FromExp,
    robochart_RangeExp,
    robochart_Neg,
    robochart_StringExp,
    robochart_FloatExp,
    robochart_RefExp,
    robochart_SetRange,
    robochart_ParExp,
    robochart_ClockExp,
    robochart_Selection,
    robochart_ResultExp,
    robochart_Assignable,
    Statement,
    robochart_Skip,
    robochart_Assignment,
    robochart_SendEvent,
    robochart_Wait,
    robochart_Call,
    robochart_ParStmt,
    robochart_IfStmt,
    robochart_SeqStatement,
    robochart_TimedStatement,
    robochart_ClockReset,
    robochart_ConnectionNode,
    robochart_Connection,
    Controller,
    robochart_ControllerRef,
    Action,
    robochart_DuringAction,
    robochart_ExitAction,
    robochart_EntryAction,
    State,
    robochart_Final,
    robochart_Action,
    Junction,
    robochart_Initial,
    Node,
    robochart_Junction,
    robochart_Statement,
    robochart_Trigger,
    robochart_ProbabilisticJunction,
    RoboticPlatform,
    Context,
    robochart_NodeContainer,
    NodeContainer,
    robochart_State,
    robochart_StateMachineBody,
    StateMachine,
    Variable,
    robochart_BasicContext,
    BasicContext,
    robochart_Context,
    Reference,
    robochart_RoboticPlatformRef,
    robochart_StateMachineRef,
    robochart_Reference,
    StateMachineBody,
    OperationSig,
    Operation,
    robochart_OperationRef,
    ConnectionNode,
    robochart_VariableList,
    SetType,
    robochart_SeqType,
    robochart_WaitingConditionRef,
    robochart_CallExp,
    Assignable,
    robochart_ArrayAssignable,
    robochart_VarSelection,
    robochart_VarRef,
    RelationType,
    robochart_FunctionType,
    robochart_Parameter,
    robochart_Expression,
    TypedNamedElement,
    robochart_Member,
    robochart_Type,
    NamedExpression,
    Member,
    robochart_Variable,
    robochart_Field,
    Type,
    robochart_SetType,
    robochart_AnyType,
    robochart_RelationType,
    robochart_VectorType,
    robochart_TypeRef,
    robochart_MatrixType,
    robochart_ProductType,
    robochart_StateMachineDef,
    TypeDecl,
    robochart_Enumeration,
    robochart_Literal,
    robochart_RecordType,
    robochart_NameType,
    robochart_PrimitiveType,
    NamedElement,
    robochart_Event,
    robochart_StateMachine,
    robochart_Controller,
    robochart_OperationSig,
    robochart_Operation,
    robochart_Declaration,
    robochart_Transition,
    robochart_Clock,
    robochart_WaitingCondition,
    robochart_RoboticPlatform,
    robochart_Node,
    robochart_TypedNamedElement,
    robochart_TypeDecl,
    robochart_NamedElement,
    robochart_Function,
    robochart_OperationDef,
    robochart_RCModule,
    robochart_ControllerDef,
    robochart_RoboticPlatformDef,
    robochart_Interface,
    BasicPackage,
    robochart_RCPackage,
    robochart_Import,
    robochart_BasicPackage,
    TriggerType,
    VariableModifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robochart_namedexpression_is_not_abstract():
    assert not inspect.isabstract(robochart_NamedExpression)


def test_robochart_namedexpression_constructor_exists():
    assert callable(robochart_NamedExpression.__init__)


def test_robochart_namedexpression_constructor_args():
    sig = inspect.signature(robochart_NamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_plus_is_not_abstract():
    assert not inspect.isabstract(robochart_Plus)


def test_robochart_plus_constructor_exists():
    assert callable(robochart_Plus.__init__)


def test_robochart_plus_constructor_args():
    sig = inspect.signature(robochart_Plus.__init__)
    params = list(sig.parameters.keys())



def test_robochart_different_is_not_abstract():
    assert not inspect.isabstract(robochart_Different)


def test_robochart_different_constructor_exists():
    assert callable(robochart_Different.__init__)


def test_robochart_different_constructor_args():
    sig = inspect.signature(robochart_Different.__init__)
    params = list(sig.parameters.keys())



def test_robochart_cat_is_not_abstract():
    assert not inspect.isabstract(robochart_Cat)


def test_robochart_cat_constructor_exists():
    assert callable(robochart_Cat.__init__)


def test_robochart_cat_constructor_args():
    sig = inspect.signature(robochart_Cat.__init__)
    params = list(sig.parameters.keys())



def test_robochart_mult_is_not_abstract():
    assert not inspect.isabstract(robochart_Mult)


def test_robochart_mult_constructor_exists():
    assert callable(robochart_Mult.__init__)


def test_robochart_mult_constructor_args():
    sig = inspect.signature(robochart_Mult.__init__)
    params = list(sig.parameters.keys())



def test_robochart_lessthan_is_not_abstract():
    assert not inspect.isabstract(robochart_LessThan)


def test_robochart_lessthan_constructor_exists():
    assert callable(robochart_LessThan.__init__)


def test_robochart_lessthan_constructor_args():
    sig = inspect.signature(robochart_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_robochart_greaterthan_is_not_abstract():
    assert not inspect.isabstract(robochart_GreaterThan)


def test_robochart_greaterthan_constructor_exists():
    assert callable(robochart_GreaterThan.__init__)


def test_robochart_greaterthan_constructor_args():
    sig = inspect.signature(robochart_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_robochart_modulus_is_not_abstract():
    assert not inspect.isabstract(robochart_Modulus)


def test_robochart_modulus_constructor_exists():
    assert callable(robochart_Modulus.__init__)


def test_robochart_modulus_constructor_args():
    sig = inspect.signature(robochart_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_robochart_implies_is_not_abstract():
    assert not inspect.isabstract(robochart_Implies)


def test_robochart_implies_constructor_exists():
    assert callable(robochart_Implies.__init__)


def test_robochart_implies_constructor_args():
    sig = inspect.signature(robochart_Implies.__init__)
    params = list(sig.parameters.keys())



def test_robochart_lessorequal_is_not_abstract():
    assert not inspect.isabstract(robochart_LessOrEqual)


def test_robochart_lessorequal_constructor_exists():
    assert callable(robochart_LessOrEqual.__init__)


def test_robochart_lessorequal_constructor_args():
    sig = inspect.signature(robochart_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_robochart_div_is_not_abstract():
    assert not inspect.isabstract(robochart_Div)


def test_robochart_div_constructor_exists():
    assert callable(robochart_Div.__init__)


def test_robochart_div_constructor_args():
    sig = inspect.signature(robochart_Div.__init__)
    params = list(sig.parameters.keys())



def test_robochart_minus_is_not_abstract():
    assert not inspect.isabstract(robochart_Minus)


def test_robochart_minus_constructor_exists():
    assert callable(robochart_Minus.__init__)


def test_robochart_minus_constructor_args():
    sig = inspect.signature(robochart_Minus.__init__)
    params = list(sig.parameters.keys())



def test_robochart_greaterorequal_is_not_abstract():
    assert not inspect.isabstract(robochart_GreaterOrEqual)


def test_robochart_greaterorequal_constructor_exists():
    assert callable(robochart_GreaterOrEqual.__init__)


def test_robochart_greaterorequal_constructor_args():
    sig = inspect.signature(robochart_GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_robochart_equals_is_not_abstract():
    assert not inspect.isabstract(robochart_Equals)


def test_robochart_equals_constructor_exists():
    assert callable(robochart_Equals.__init__)


def test_robochart_equals_constructor_args():
    sig = inspect.signature(robochart_Equals.__init__)
    params = list(sig.parameters.keys())



def test_robochart_or_is_not_abstract():
    assert not inspect.isabstract(robochart_Or)


def test_robochart_or_constructor_exists():
    assert callable(robochart_Or.__init__)


def test_robochart_or_constructor_args():
    sig = inspect.signature(robochart_Or.__init__)
    params = list(sig.parameters.keys())



def test_robochart_and_is_not_abstract():
    assert not inspect.isabstract(robochart_And)


def test_robochart_and_constructor_exists():
    assert callable(robochart_And.__init__)


def test_robochart_and_constructor_args():
    sig = inspect.signature(robochart_And.__init__)
    params = list(sig.parameters.keys())



def test_robochart_iff_is_not_abstract():
    assert not inspect.isabstract(robochart_Iff)


def test_robochart_iff_constructor_exists():
    assert callable(robochart_Iff.__init__)


def test_robochart_iff_constructor_args():
    sig = inspect.signature(robochart_Iff.__init__)
    params = list(sig.parameters.keys())



def test_lambdaexp_is_not_abstract():
    assert not inspect.isabstract(LambdaExp)


def test_lambdaexp_constructor_exists():
    assert callable(LambdaExp.__init__)


def test_lambdaexp_constructor_args():
    sig = inspect.signature(LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_definitedescription_is_not_abstract():
    assert not inspect.isabstract(robochart_DefiniteDescription)


def test_robochart_definitedescription_constructor_exists():
    assert callable(robochart_DefiniteDescription.__init__)


def test_robochart_definitedescription_constructor_args():
    sig = inspect.signature(robochart_DefiniteDescription.__init__)
    params = list(sig.parameters.keys())



def test_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifierExpression)


def test_quantifierexpression_constructor_exists():
    assert callable(QuantifierExpression.__init__)


def test_quantifierexpression_constructor_args():
    sig = inspect.signature(QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_exists_is_not_abstract():
    assert not inspect.isabstract(robochart_Exists)


def test_robochart_exists_constructor_exists():
    assert callable(robochart_Exists.__init__)


def test_robochart_exists_constructor_args():
    sig = inspect.signature(robochart_Exists.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_robochart_exists_has_unique():
    assert hasattr(robochart_Exists, "unique")
    descriptor = None
    for klass in robochart_Exists.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_robochart_forall_is_not_abstract():
    assert not inspect.isabstract(robochart_Forall)


def test_robochart_forall_constructor_exists():
    assert callable(robochart_Forall.__init__)


def test_robochart_forall_constructor_args():
    sig = inspect.signature(robochart_Forall.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_inexp_is_not_abstract():
    assert not inspect.isabstract(robochart_InExp)


def test_robochart_inexp_constructor_exists():
    assert callable(robochart_InExp.__init__)


def test_robochart_inexp_constructor_args():
    sig = inspect.signature(robochart_InExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_ifexpression_is_not_abstract():
    assert not inspect.isabstract(robochart_IfExpression)


def test_robochart_ifexpression_constructor_exists():
    assert callable(robochart_IfExpression.__init__)


def test_robochart_ifexpression_constructor_args():
    sig = inspect.signature(robochart_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_varexp_is_not_abstract():
    assert not inspect.isabstract(robochart_VarExp)


def test_robochart_varexp_constructor_exists():
    assert callable(robochart_VarExp.__init__)


def test_robochart_varexp_constructor_args():
    sig = inspect.signature(robochart_VarExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_tupleexp_is_not_abstract():
    assert not inspect.isabstract(robochart_TupleExp)


def test_robochart_tupleexp_constructor_exists():
    assert callable(robochart_TupleExp.__init__)


def test_robochart_tupleexp_constructor_args():
    sig = inspect.signature(robochart_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_booleanexp_is_not_abstract():
    assert not inspect.isabstract(robochart_BooleanExp)


def test_robochart_booleanexp_constructor_exists():
    assert callable(robochart_BooleanExp.__init__)


def test_robochart_booleanexp_constructor_args():
    sig = inspect.signature(robochart_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart_booleanexp_has_value():
    assert hasattr(robochart_BooleanExp, "value")
    descriptor = None
    for klass in robochart_BooleanExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart_integerexp_is_not_abstract():
    assert not inspect.isabstract(robochart_IntegerExp)


def test_robochart_integerexp_constructor_exists():
    assert callable(robochart_IntegerExp.__init__)


def test_robochart_integerexp_constructor_args():
    sig = inspect.signature(robochart_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart_integerexp_has_value():
    assert hasattr(robochart_IntegerExp, "value")
    descriptor = None
    for klass in robochart_IntegerExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart_letexpression_is_not_abstract():
    assert not inspect.isabstract(robochart_LetExpression)


def test_robochart_letexpression_constructor_exists():
    assert callable(robochart_LetExpression.__init__)


def test_robochart_letexpression_constructor_args():
    sig = inspect.signature(robochart_LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_toexp_is_not_abstract():
    assert not inspect.isabstract(robochart_ToExp)


def test_robochart_toexp_constructor_exists():
    assert callable(robochart_ToExp.__init__)


def test_robochart_toexp_constructor_args():
    sig = inspect.signature(robochart_ToExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_isexp_is_not_abstract():
    assert not inspect.isabstract(robochart_IsExp)


def test_robochart_isexp_constructor_exists():
    assert callable(robochart_IsExp.__init__)


def test_robochart_isexp_constructor_args():
    sig = inspect.signature(robochart_IsExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_arrayexp_is_not_abstract():
    assert not inspect.isabstract(robochart_ArrayExp)


def test_robochart_arrayexp_constructor_exists():
    assert callable(robochart_ArrayExp.__init__)


def test_robochart_arrayexp_constructor_args():
    sig = inspect.signature(robochart_ArrayExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_lambdaexp_is_not_abstract():
    assert not inspect.isabstract(robochart_LambdaExp)


def test_robochart_lambdaexp_constructor_exists():
    assert callable(robochart_LambdaExp.__init__)


def test_robochart_lambdaexp_constructor_args():
    sig = inspect.signature(robochart_LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_not_is_not_abstract():
    assert not inspect.isabstract(robochart_Not)


def test_robochart_not_constructor_exists():
    assert callable(robochart_Not.__init__)


def test_robochart_not_constructor_args():
    sig = inspect.signature(robochart_Not.__init__)
    params = list(sig.parameters.keys())



def test_robochart_typeexp_is_not_abstract():
    assert not inspect.isabstract(robochart_TypeExp)


def test_robochart_typeexp_constructor_exists():
    assert callable(robochart_TypeExp.__init__)


def test_robochart_typeexp_constructor_args():
    sig = inspect.signature(robochart_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(robochart_QuantifierExpression)


def test_robochart_quantifierexpression_constructor_exists():
    assert callable(robochart_QuantifierExpression.__init__)


def test_robochart_quantifierexpression_constructor_args():
    sig = inspect.signature(robochart_QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_elseexp_is_not_abstract():
    assert not inspect.isabstract(robochart_ElseExp)


def test_robochart_elseexp_constructor_exists():
    assert callable(robochart_ElseExp.__init__)


def test_robochart_elseexp_constructor_args():
    sig = inspect.signature(robochart_ElseExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_stateclockexp_is_not_abstract():
    assert not inspect.isabstract(robochart_StateClockExp)


def test_robochart_stateclockexp_constructor_exists():
    assert callable(robochart_StateClockExp.__init__)


def test_robochart_stateclockexp_constructor_args():
    sig = inspect.signature(robochart_StateClockExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_setexp_is_not_abstract():
    assert not inspect.isabstract(robochart_SetExp)


def test_robochart_setexp_constructor_exists():
    assert callable(robochart_SetExp.__init__)


def test_robochart_setexp_constructor_args():
    sig = inspect.signature(robochart_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_enumexp_is_not_abstract():
    assert not inspect.isabstract(robochart_EnumExp)


def test_robochart_enumexp_constructor_exists():
    assert callable(robochart_EnumExp.__init__)


def test_robochart_enumexp_constructor_args():
    sig = inspect.signature(robochart_EnumExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_seqexp_is_not_abstract():
    assert not inspect.isabstract(robochart_SeqExp)


def test_robochart_seqexp_constructor_exists():
    assert callable(robochart_SeqExp.__init__)


def test_robochart_seqexp_constructor_args():
    sig = inspect.signature(robochart_SeqExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_setcomp_is_not_abstract():
    assert not inspect.isabstract(robochart_SetComp)


def test_robochart_setcomp_constructor_exists():
    assert callable(robochart_SetComp.__init__)


def test_robochart_setcomp_constructor_args():
    sig = inspect.signature(robochart_SetComp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_idexp_is_not_abstract():
    assert not inspect.isabstract(robochart_IdExp)


def test_robochart_idexp_constructor_exists():
    assert callable(robochart_IdExp.__init__)


def test_robochart_idexp_constructor_args():
    sig = inspect.signature(robochart_IdExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_asexp_is_not_abstract():
    assert not inspect.isabstract(robochart_AsExp)


def test_robochart_asexp_constructor_exists():
    assert callable(robochart_AsExp.__init__)


def test_robochart_asexp_constructor_args():
    sig = inspect.signature(robochart_AsExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(robochart_BinaryExpression)


def test_robochart_binaryexpression_constructor_exists():
    assert callable(robochart_BinaryExpression.__init__)


def test_robochart_binaryexpression_constructor_args():
    sig = inspect.signature(robochart_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_robochart_fromexp_is_not_abstract():
    assert not inspect.isabstract(robochart_FromExp)


def test_robochart_fromexp_constructor_exists():
    assert callable(robochart_FromExp.__init__)


def test_robochart_fromexp_constructor_args():
    sig = inspect.signature(robochart_FromExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_rangeexp_is_not_abstract():
    assert not inspect.isabstract(robochart_RangeExp)


def test_robochart_rangeexp_constructor_exists():
    assert callable(robochart_RangeExp.__init__)


def test_robochart_rangeexp_constructor_args():
    sig = inspect.signature(robochart_RangeExp.__init__)
    params = list(sig.parameters.keys())
    assert "linterval" in params, "Missing parameter 'linterval'"
    assert "rinterval" in params, "Missing parameter 'rinterval'"

def test_robochart_rangeexp_has_linterval():
    assert hasattr(robochart_RangeExp, "linterval")
    descriptor = None
    for klass in robochart_RangeExp.__mro__:
        if "linterval" in klass.__dict__:
            descriptor = klass.__dict__["linterval"]
            break
    assert isinstance(descriptor, property)

def test_robochart_rangeexp_has_rinterval():
    assert hasattr(robochart_RangeExp, "rinterval")
    descriptor = None
    for klass in robochart_RangeExp.__mro__:
        if "rinterval" in klass.__dict__:
            descriptor = klass.__dict__["rinterval"]
            break
    assert isinstance(descriptor, property)



def test_robochart_neg_is_not_abstract():
    assert not inspect.isabstract(robochart_Neg)


def test_robochart_neg_constructor_exists():
    assert callable(robochart_Neg.__init__)


def test_robochart_neg_constructor_args():
    sig = inspect.signature(robochart_Neg.__init__)
    params = list(sig.parameters.keys())



def test_robochart_stringexp_is_not_abstract():
    assert not inspect.isabstract(robochart_StringExp)


def test_robochart_stringexp_constructor_exists():
    assert callable(robochart_StringExp.__init__)


def test_robochart_stringexp_constructor_args():
    sig = inspect.signature(robochart_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart_stringexp_has_value():
    assert hasattr(robochart_StringExp, "value")
    descriptor = None
    for klass in robochart_StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart_floatexp_is_not_abstract():
    assert not inspect.isabstract(robochart_FloatExp)


def test_robochart_floatexp_constructor_exists():
    assert callable(robochart_FloatExp.__init__)


def test_robochart_floatexp_constructor_args():
    sig = inspect.signature(robochart_FloatExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_robochart_floatexp_has_value():
    assert hasattr(robochart_FloatExp, "value")
    descriptor = None
    for klass in robochart_FloatExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_robochart_refexp_is_not_abstract():
    assert not inspect.isabstract(robochart_RefExp)


def test_robochart_refexp_constructor_exists():
    assert callable(robochart_RefExp.__init__)


def test_robochart_refexp_constructor_args():
    sig = inspect.signature(robochart_RefExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_setrange_is_not_abstract():
    assert not inspect.isabstract(robochart_SetRange)


def test_robochart_setrange_constructor_exists():
    assert callable(robochart_SetRange.__init__)


def test_robochart_setrange_constructor_args():
    sig = inspect.signature(robochart_SetRange.__init__)
    params = list(sig.parameters.keys())



def test_robochart_parexp_is_not_abstract():
    assert not inspect.isabstract(robochart_ParExp)


def test_robochart_parexp_constructor_exists():
    assert callable(robochart_ParExp.__init__)


def test_robochart_parexp_constructor_args():
    sig = inspect.signature(robochart_ParExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_clockexp_is_not_abstract():
    assert not inspect.isabstract(robochart_ClockExp)


def test_robochart_clockexp_constructor_exists():
    assert callable(robochart_ClockExp.__init__)


def test_robochart_clockexp_constructor_args():
    sig = inspect.signature(robochart_ClockExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_selection_is_not_abstract():
    assert not inspect.isabstract(robochart_Selection)


def test_robochart_selection_constructor_exists():
    assert callable(robochart_Selection.__init__)


def test_robochart_selection_constructor_args():
    sig = inspect.signature(robochart_Selection.__init__)
    params = list(sig.parameters.keys())



def test_robochart_resultexp_is_not_abstract():
    assert not inspect.isabstract(robochart_ResultExp)


def test_robochart_resultexp_constructor_exists():
    assert callable(robochart_ResultExp.__init__)


def test_robochart_resultexp_constructor_args():
    sig = inspect.signature(robochart_ResultExp.__init__)
    params = list(sig.parameters.keys())



def test_robochart_assignable_is_not_abstract():
    assert not inspect.isabstract(robochart_Assignable)


def test_robochart_assignable_constructor_exists():
    assert callable(robochart_Assignable.__init__)


def test_robochart_assignable_constructor_args():
    sig = inspect.signature(robochart_Assignable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_skip_is_not_abstract():
    assert not inspect.isabstract(robochart_Skip)


def test_robochart_skip_constructor_exists():
    assert callable(robochart_Skip.__init__)


def test_robochart_skip_constructor_args():
    sig = inspect.signature(robochart_Skip.__init__)
    params = list(sig.parameters.keys())



def test_robochart_assignment_is_not_abstract():
    assert not inspect.isabstract(robochart_Assignment)


def test_robochart_assignment_constructor_exists():
    assert callable(robochart_Assignment.__init__)


def test_robochart_assignment_constructor_args():
    sig = inspect.signature(robochart_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_robochart_sendevent_is_not_abstract():
    assert not inspect.isabstract(robochart_SendEvent)


def test_robochart_sendevent_constructor_exists():
    assert callable(robochart_SendEvent.__init__)


def test_robochart_sendevent_constructor_args():
    sig = inspect.signature(robochart_SendEvent.__init__)
    params = list(sig.parameters.keys())



def test_robochart_wait_is_not_abstract():
    assert not inspect.isabstract(robochart_Wait)


def test_robochart_wait_constructor_exists():
    assert callable(robochart_Wait.__init__)


def test_robochart_wait_constructor_args():
    sig = inspect.signature(robochart_Wait.__init__)
    params = list(sig.parameters.keys())



def test_robochart_call_is_not_abstract():
    assert not inspect.isabstract(robochart_Call)


def test_robochart_call_constructor_exists():
    assert callable(robochart_Call.__init__)


def test_robochart_call_constructor_args():
    sig = inspect.signature(robochart_Call.__init__)
    params = list(sig.parameters.keys())



def test_robochart_parstmt_is_not_abstract():
    assert not inspect.isabstract(robochart_ParStmt)


def test_robochart_parstmt_constructor_exists():
    assert callable(robochart_ParStmt.__init__)


def test_robochart_parstmt_constructor_args():
    sig = inspect.signature(robochart_ParStmt.__init__)
    params = list(sig.parameters.keys())



def test_robochart_ifstmt_is_not_abstract():
    assert not inspect.isabstract(robochart_IfStmt)


def test_robochart_ifstmt_constructor_exists():
    assert callable(robochart_IfStmt.__init__)


def test_robochart_ifstmt_constructor_args():
    sig = inspect.signature(robochart_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_robochart_seqstatement_is_not_abstract():
    assert not inspect.isabstract(robochart_SeqStatement)


def test_robochart_seqstatement_constructor_exists():
    assert callable(robochart_SeqStatement.__init__)


def test_robochart_seqstatement_constructor_args():
    sig = inspect.signature(robochart_SeqStatement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_timedstatement_is_not_abstract():
    assert not inspect.isabstract(robochart_TimedStatement)


def test_robochart_timedstatement_constructor_exists():
    assert callable(robochart_TimedStatement.__init__)


def test_robochart_timedstatement_constructor_args():
    sig = inspect.signature(robochart_TimedStatement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_clockreset_is_not_abstract():
    assert not inspect.isabstract(robochart_ClockReset)


def test_robochart_clockreset_constructor_exists():
    assert callable(robochart_ClockReset.__init__)


def test_robochart_clockreset_constructor_args():
    sig = inspect.signature(robochart_ClockReset.__init__)
    params = list(sig.parameters.keys())



def test_robochart_connectionnode_is_not_abstract():
    assert not inspect.isabstract(robochart_ConnectionNode)


def test_robochart_connectionnode_constructor_exists():
    assert callable(robochart_ConnectionNode.__init__)


def test_robochart_connectionnode_constructor_args():
    sig = inspect.signature(robochart_ConnectionNode.__init__)
    params = list(sig.parameters.keys())



def test_robochart_connection_is_not_abstract():
    assert not inspect.isabstract(robochart_Connection)


def test_robochart_connection_constructor_exists():
    assert callable(robochart_Connection.__init__)


def test_robochart_connection_constructor_args():
    sig = inspect.signature(robochart_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "async_" in params, "Missing parameter 'async_'"
    assert "bidirec" in params, "Missing parameter 'bidirec'"

def test_robochart_connection_has_async_():
    assert hasattr(robochart_Connection, "async_")
    descriptor = None
    for klass in robochart_Connection.__mro__:
        if "async_" in klass.__dict__:
            descriptor = klass.__dict__["async_"]
            break
    assert isinstance(descriptor, property)

def test_robochart_connection_has_bidirec():
    assert hasattr(robochart_Connection, "bidirec")
    descriptor = None
    for klass in robochart_Connection.__mro__:
        if "bidirec" in klass.__dict__:
            descriptor = klass.__dict__["bidirec"]
            break
    assert isinstance(descriptor, property)



def test_controller_is_not_abstract():
    assert not inspect.isabstract(Controller)


def test_controller_constructor_exists():
    assert callable(Controller.__init__)


def test_controller_constructor_args():
    sig = inspect.signature(Controller.__init__)
    params = list(sig.parameters.keys())



def test_robochart_controllerref_is_not_abstract():
    assert not inspect.isabstract(robochart_ControllerRef)


def test_robochart_controllerref_constructor_exists():
    assert callable(robochart_ControllerRef.__init__)


def test_robochart_controllerref_constructor_args():
    sig = inspect.signature(robochart_ControllerRef.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_robochart_duringaction_is_not_abstract():
    assert not inspect.isabstract(robochart_DuringAction)


def test_robochart_duringaction_constructor_exists():
    assert callable(robochart_DuringAction.__init__)


def test_robochart_duringaction_constructor_args():
    sig = inspect.signature(robochart_DuringAction.__init__)
    params = list(sig.parameters.keys())



def test_robochart_exitaction_is_not_abstract():
    assert not inspect.isabstract(robochart_ExitAction)


def test_robochart_exitaction_constructor_exists():
    assert callable(robochart_ExitAction.__init__)


def test_robochart_exitaction_constructor_args():
    sig = inspect.signature(robochart_ExitAction.__init__)
    params = list(sig.parameters.keys())



def test_robochart_entryaction_is_not_abstract():
    assert not inspect.isabstract(robochart_EntryAction)


def test_robochart_entryaction_constructor_exists():
    assert callable(robochart_EntryAction.__init__)


def test_robochart_entryaction_constructor_args():
    sig = inspect.signature(robochart_EntryAction.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_robochart_final_is_not_abstract():
    assert not inspect.isabstract(robochart_Final)


def test_robochart_final_constructor_exists():
    assert callable(robochart_Final.__init__)


def test_robochart_final_constructor_args():
    sig = inspect.signature(robochart_Final.__init__)
    params = list(sig.parameters.keys())



def test_robochart_action_is_not_abstract():
    assert not inspect.isabstract(robochart_Action)


def test_robochart_action_constructor_exists():
    assert callable(robochart_Action.__init__)


def test_robochart_action_constructor_args():
    sig = inspect.signature(robochart_Action.__init__)
    params = list(sig.parameters.keys())



def test_junction_is_not_abstract():
    assert not inspect.isabstract(Junction)


def test_junction_constructor_exists():
    assert callable(Junction.__init__)


def test_junction_constructor_args():
    sig = inspect.signature(Junction.__init__)
    params = list(sig.parameters.keys())



def test_robochart_initial_is_not_abstract():
    assert not inspect.isabstract(robochart_Initial)


def test_robochart_initial_constructor_exists():
    assert callable(robochart_Initial.__init__)


def test_robochart_initial_constructor_args():
    sig = inspect.signature(robochart_Initial.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_robochart_junction_is_not_abstract():
    assert not inspect.isabstract(robochart_Junction)


def test_robochart_junction_constructor_exists():
    assert callable(robochart_Junction.__init__)


def test_robochart_junction_constructor_args():
    sig = inspect.signature(robochart_Junction.__init__)
    params = list(sig.parameters.keys())



def test_robochart_statement_is_not_abstract():
    assert not inspect.isabstract(robochart_Statement)


def test_robochart_statement_constructor_exists():
    assert callable(robochart_Statement.__init__)


def test_robochart_statement_constructor_args():
    sig = inspect.signature(robochart_Statement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_trigger_is_not_abstract():
    assert not inspect.isabstract(robochart_Trigger)


def test_robochart_trigger_constructor_exists():
    assert callable(robochart_Trigger.__init__)


def test_robochart_trigger_constructor_args():
    sig = inspect.signature(robochart_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "_type" in params, "Missing parameter '_type'"

def test_robochart_trigger_has__type():
    assert hasattr(robochart_Trigger, "_type")
    descriptor = None
    for klass in robochart_Trigger.__mro__:
        if "_type" in klass.__dict__:
            descriptor = klass.__dict__["_type"]
            break
    assert isinstance(descriptor, property)



def test_robochart_probabilisticjunction_is_not_abstract():
    assert not inspect.isabstract(robochart_ProbabilisticJunction)


def test_robochart_probabilisticjunction_constructor_exists():
    assert callable(robochart_ProbabilisticJunction.__init__)


def test_robochart_probabilisticjunction_constructor_args():
    sig = inspect.signature(robochart_ProbabilisticJunction.__init__)
    params = list(sig.parameters.keys())



def test_roboticplatform_is_not_abstract():
    assert not inspect.isabstract(RoboticPlatform)


def test_roboticplatform_constructor_exists():
    assert callable(RoboticPlatform.__init__)


def test_roboticplatform_constructor_args():
    sig = inspect.signature(RoboticPlatform.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_robochart_nodecontainer_is_not_abstract():
    assert not inspect.isabstract(robochart_NodeContainer)


def test_robochart_nodecontainer_constructor_exists():
    assert callable(robochart_NodeContainer.__init__)


def test_robochart_nodecontainer_constructor_args():
    sig = inspect.signature(robochart_NodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_nodecontainer_is_not_abstract():
    assert not inspect.isabstract(NodeContainer)


def test_nodecontainer_constructor_exists():
    assert callable(NodeContainer.__init__)


def test_nodecontainer_constructor_args():
    sig = inspect.signature(NodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_robochart_state_is_not_abstract():
    assert not inspect.isabstract(robochart_State)


def test_robochart_state_constructor_exists():
    assert callable(robochart_State.__init__)


def test_robochart_state_constructor_args():
    sig = inspect.signature(robochart_State.__init__)
    params = list(sig.parameters.keys())



def test_robochart_statemachinebody_is_not_abstract():
    assert not inspect.isabstract(robochart_StateMachineBody)


def test_robochart_statemachinebody_constructor_exists():
    assert callable(robochart_StateMachineBody.__init__)


def test_robochart_statemachinebody_constructor_args():
    sig = inspect.signature(robochart_StateMachineBody.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_robochart_basiccontext_is_not_abstract():
    assert not inspect.isabstract(robochart_BasicContext)


def test_robochart_basiccontext_constructor_exists():
    assert callable(robochart_BasicContext.__init__)


def test_robochart_basiccontext_constructor_args():
    sig = inspect.signature(robochart_BasicContext.__init__)
    params = list(sig.parameters.keys())



def test_basiccontext_is_not_abstract():
    assert not inspect.isabstract(BasicContext)


def test_basiccontext_constructor_exists():
    assert callable(BasicContext.__init__)


def test_basiccontext_constructor_args():
    sig = inspect.signature(BasicContext.__init__)
    params = list(sig.parameters.keys())



def test_robochart_context_is_not_abstract():
    assert not inspect.isabstract(robochart_Context)


def test_robochart_context_constructor_exists():
    assert callable(robochart_Context.__init__)


def test_robochart_context_constructor_args():
    sig = inspect.signature(robochart_Context.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_robochart_roboticplatformref_is_not_abstract():
    assert not inspect.isabstract(robochart_RoboticPlatformRef)


def test_robochart_roboticplatformref_constructor_exists():
    assert callable(robochart_RoboticPlatformRef.__init__)


def test_robochart_roboticplatformref_constructor_args():
    sig = inspect.signature(robochart_RoboticPlatformRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_statemachineref_is_not_abstract():
    assert not inspect.isabstract(robochart_StateMachineRef)


def test_robochart_statemachineref_constructor_exists():
    assert callable(robochart_StateMachineRef.__init__)


def test_robochart_statemachineref_constructor_args():
    sig = inspect.signature(robochart_StateMachineRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_reference_is_not_abstract():
    assert not inspect.isabstract(robochart_Reference)


def test_robochart_reference_constructor_exists():
    assert callable(robochart_Reference.__init__)


def test_robochart_reference_constructor_args():
    sig = inspect.signature(robochart_Reference.__init__)
    params = list(sig.parameters.keys())



def test_statemachinebody_is_not_abstract():
    assert not inspect.isabstract(StateMachineBody)


def test_statemachinebody_constructor_exists():
    assert callable(StateMachineBody.__init__)


def test_statemachinebody_constructor_args():
    sig = inspect.signature(StateMachineBody.__init__)
    params = list(sig.parameters.keys())



def test_operationsig_is_not_abstract():
    assert not inspect.isabstract(OperationSig)


def test_operationsig_constructor_exists():
    assert callable(OperationSig.__init__)


def test_operationsig_constructor_args():
    sig = inspect.signature(OperationSig.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_robochart_operationref_is_not_abstract():
    assert not inspect.isabstract(robochart_OperationRef)


def test_robochart_operationref_constructor_exists():
    assert callable(robochart_OperationRef.__init__)


def test_robochart_operationref_constructor_args():
    sig = inspect.signature(robochart_OperationRef.__init__)
    params = list(sig.parameters.keys())



def test_connectionnode_is_not_abstract():
    assert not inspect.isabstract(ConnectionNode)


def test_connectionnode_constructor_exists():
    assert callable(ConnectionNode.__init__)


def test_connectionnode_constructor_args():
    sig = inspect.signature(ConnectionNode.__init__)
    params = list(sig.parameters.keys())



def test_robochart_variablelist_is_not_abstract():
    assert not inspect.isabstract(robochart_VariableList)


def test_robochart_variablelist_constructor_exists():
    assert callable(robochart_VariableList.__init__)


def test_robochart_variablelist_constructor_args():
    sig = inspect.signature(robochart_VariableList.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_robochart_variablelist_has_modifier():
    assert hasattr(robochart_VariableList, "modifier")
    descriptor = None
    for klass in robochart_VariableList.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_settype_is_not_abstract():
    assert not inspect.isabstract(SetType)


def test_settype_constructor_exists():
    assert callable(SetType.__init__)


def test_settype_constructor_args():
    sig = inspect.signature(SetType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_seqtype_is_not_abstract():
    assert not inspect.isabstract(robochart_SeqType)


def test_robochart_seqtype_constructor_exists():
    assert callable(robochart_SeqType.__init__)


def test_robochart_seqtype_constructor_args():
    sig = inspect.signature(robochart_SeqType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_waitingconditionref_is_not_abstract():
    assert not inspect.isabstract(robochart_WaitingConditionRef)


def test_robochart_waitingconditionref_constructor_exists():
    assert callable(robochart_WaitingConditionRef.__init__)


def test_robochart_waitingconditionref_constructor_args():
    sig = inspect.signature(robochart_WaitingConditionRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_callexp_is_not_abstract():
    assert not inspect.isabstract(robochart_CallExp)


def test_robochart_callexp_constructor_exists():
    assert callable(robochart_CallExp.__init__)


def test_robochart_callexp_constructor_args():
    sig = inspect.signature(robochart_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_assignable_is_not_abstract():
    assert not inspect.isabstract(Assignable)


def test_assignable_constructor_exists():
    assert callable(Assignable.__init__)


def test_assignable_constructor_args():
    sig = inspect.signature(Assignable.__init__)
    params = list(sig.parameters.keys())



def test_robochart_arrayassignable_is_not_abstract():
    assert not inspect.isabstract(robochart_ArrayAssignable)


def test_robochart_arrayassignable_constructor_exists():
    assert callable(robochart_ArrayAssignable.__init__)


def test_robochart_arrayassignable_constructor_args():
    sig = inspect.signature(robochart_ArrayAssignable.__init__)
    params = list(sig.parameters.keys())



def test_robochart_varselection_is_not_abstract():
    assert not inspect.isabstract(robochart_VarSelection)


def test_robochart_varselection_constructor_exists():
    assert callable(robochart_VarSelection.__init__)


def test_robochart_varselection_constructor_args():
    sig = inspect.signature(robochart_VarSelection.__init__)
    params = list(sig.parameters.keys())



def test_robochart_varref_is_not_abstract():
    assert not inspect.isabstract(robochart_VarRef)


def test_robochart_varref_constructor_exists():
    assert callable(robochart_VarRef.__init__)


def test_robochart_varref_constructor_args():
    sig = inspect.signature(robochart_VarRef.__init__)
    params = list(sig.parameters.keys())



def test_relationtype_is_not_abstract():
    assert not inspect.isabstract(RelationType)


def test_relationtype_constructor_exists():
    assert callable(RelationType.__init__)


def test_relationtype_constructor_args():
    sig = inspect.signature(RelationType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_functiontype_is_not_abstract():
    assert not inspect.isabstract(robochart_FunctionType)


def test_robochart_functiontype_constructor_exists():
    assert callable(robochart_FunctionType.__init__)


def test_robochart_functiontype_constructor_args():
    sig = inspect.signature(robochart_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_parameter_is_not_abstract():
    assert not inspect.isabstract(robochart_Parameter)


def test_robochart_parameter_constructor_exists():
    assert callable(robochart_Parameter.__init__)


def test_robochart_parameter_constructor_args():
    sig = inspect.signature(robochart_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_robochart_expression_is_not_abstract():
    assert not inspect.isabstract(robochart_Expression)


def test_robochart_expression_constructor_exists():
    assert callable(robochart_Expression.__init__)


def test_robochart_expression_constructor_args():
    sig = inspect.signature(robochart_Expression.__init__)
    params = list(sig.parameters.keys())



def test_typednamedelement_is_not_abstract():
    assert not inspect.isabstract(TypedNamedElement)


def test_typednamedelement_constructor_exists():
    assert callable(TypedNamedElement.__init__)


def test_typednamedelement_constructor_args():
    sig = inspect.signature(TypedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_member_is_not_abstract():
    assert not inspect.isabstract(robochart_Member)


def test_robochart_member_constructor_exists():
    assert callable(robochart_Member.__init__)


def test_robochart_member_constructor_args():
    sig = inspect.signature(robochart_Member.__init__)
    params = list(sig.parameters.keys())



def test_robochart_type_is_not_abstract():
    assert not inspect.isabstract(robochart_Type)


def test_robochart_type_constructor_exists():
    assert callable(robochart_Type.__init__)


def test_robochart_type_constructor_args():
    sig = inspect.signature(robochart_Type.__init__)
    params = list(sig.parameters.keys())



def test_namedexpression_is_not_abstract():
    assert not inspect.isabstract(NamedExpression)


def test_namedexpression_constructor_exists():
    assert callable(NamedExpression.__init__)


def test_namedexpression_constructor_args():
    sig = inspect.signature(NamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_robochart_variable_is_not_abstract():
    assert not inspect.isabstract(robochart_Variable)


def test_robochart_variable_constructor_exists():
    assert callable(robochart_Variable.__init__)


def test_robochart_variable_constructor_args():
    sig = inspect.signature(robochart_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_robochart_variable_has_modifier():
    assert hasattr(robochart_Variable, "modifier")
    descriptor = None
    for klass in robochart_Variable.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_robochart_field_is_not_abstract():
    assert not inspect.isabstract(robochart_Field)


def test_robochart_field_constructor_exists():
    assert callable(robochart_Field.__init__)


def test_robochart_field_constructor_args():
    sig = inspect.signature(robochart_Field.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_robochart_settype_is_not_abstract():
    assert not inspect.isabstract(robochart_SetType)


def test_robochart_settype_constructor_exists():
    assert callable(robochart_SetType.__init__)


def test_robochart_settype_constructor_args():
    sig = inspect.signature(robochart_SetType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_anytype_is_not_abstract():
    assert not inspect.isabstract(robochart_AnyType)


def test_robochart_anytype_constructor_exists():
    assert callable(robochart_AnyType.__init__)


def test_robochart_anytype_constructor_args():
    sig = inspect.signature(robochart_AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_robochart_anytype_has_identifier():
    assert hasattr(robochart_AnyType, "identifier")
    descriptor = None
    for klass in robochart_AnyType.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_robochart_relationtype_is_not_abstract():
    assert not inspect.isabstract(robochart_RelationType)


def test_robochart_relationtype_constructor_exists():
    assert callable(robochart_RelationType.__init__)


def test_robochart_relationtype_constructor_args():
    sig = inspect.signature(robochart_RelationType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_vectortype_is_not_abstract():
    assert not inspect.isabstract(robochart_VectorType)


def test_robochart_vectortype_constructor_exists():
    assert callable(robochart_VectorType.__init__)


def test_robochart_vectortype_constructor_args():
    sig = inspect.signature(robochart_VectorType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_robochart_vectortype_has_size():
    assert hasattr(robochart_VectorType, "size")
    descriptor = None
    for klass in robochart_VectorType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_robochart_typeref_is_not_abstract():
    assert not inspect.isabstract(robochart_TypeRef)


def test_robochart_typeref_constructor_exists():
    assert callable(robochart_TypeRef.__init__)


def test_robochart_typeref_constructor_args():
    sig = inspect.signature(robochart_TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_matrixtype_is_not_abstract():
    assert not inspect.isabstract(robochart_MatrixType)


def test_robochart_matrixtype_constructor_exists():
    assert callable(robochart_MatrixType.__init__)


def test_robochart_matrixtype_constructor_args():
    sig = inspect.signature(robochart_MatrixType.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"
    assert "rows" in params, "Missing parameter 'rows'"

def test_robochart_matrixtype_has_columns():
    assert hasattr(robochart_MatrixType, "columns")
    descriptor = None
    for klass in robochart_MatrixType.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_robochart_matrixtype_has_rows():
    assert hasattr(robochart_MatrixType, "rows")
    descriptor = None
    for klass in robochart_MatrixType.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)



def test_robochart_producttype_is_not_abstract():
    assert not inspect.isabstract(robochart_ProductType)


def test_robochart_producttype_constructor_exists():
    assert callable(robochart_ProductType.__init__)


def test_robochart_producttype_constructor_args():
    sig = inspect.signature(robochart_ProductType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_statemachinedef_is_not_abstract():
    assert not inspect.isabstract(robochart_StateMachineDef)


def test_robochart_statemachinedef_constructor_exists():
    assert callable(robochart_StateMachineDef.__init__)


def test_robochart_statemachinedef_constructor_args():
    sig = inspect.signature(robochart_StateMachineDef.__init__)
    params = list(sig.parameters.keys())



def test_typedecl_is_not_abstract():
    assert not inspect.isabstract(TypeDecl)


def test_typedecl_constructor_exists():
    assert callable(TypeDecl.__init__)


def test_typedecl_constructor_args():
    sig = inspect.signature(TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_robochart_enumeration_is_not_abstract():
    assert not inspect.isabstract(robochart_Enumeration)


def test_robochart_enumeration_constructor_exists():
    assert callable(robochart_Enumeration.__init__)


def test_robochart_enumeration_constructor_args():
    sig = inspect.signature(robochart_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_robochart_literal_is_not_abstract():
    assert not inspect.isabstract(robochart_Literal)


def test_robochart_literal_constructor_exists():
    assert callable(robochart_Literal.__init__)


def test_robochart_literal_constructor_args():
    sig = inspect.signature(robochart_Literal.__init__)
    params = list(sig.parameters.keys())



def test_robochart_recordtype_is_not_abstract():
    assert not inspect.isabstract(robochart_RecordType)


def test_robochart_recordtype_constructor_exists():
    assert callable(robochart_RecordType.__init__)


def test_robochart_recordtype_constructor_args():
    sig = inspect.signature(robochart_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_nametype_is_not_abstract():
    assert not inspect.isabstract(robochart_NameType)


def test_robochart_nametype_constructor_exists():
    assert callable(robochart_NameType.__init__)


def test_robochart_nametype_constructor_args():
    sig = inspect.signature(robochart_NameType.__init__)
    params = list(sig.parameters.keys())



def test_robochart_primitivetype_is_not_abstract():
    assert not inspect.isabstract(robochart_PrimitiveType)


def test_robochart_primitivetype_constructor_exists():
    assert callable(robochart_PrimitiveType.__init__)


def test_robochart_primitivetype_constructor_args():
    sig = inspect.signature(robochart_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_event_is_not_abstract():
    assert not inspect.isabstract(robochart_Event)


def test_robochart_event_constructor_exists():
    assert callable(robochart_Event.__init__)


def test_robochart_event_constructor_args():
    sig = inspect.signature(robochart_Event.__init__)
    params = list(sig.parameters.keys())
    assert "broadcast" in params, "Missing parameter 'broadcast'"

def test_robochart_event_has_broadcast():
    assert hasattr(robochart_Event, "broadcast")
    descriptor = None
    for klass in robochart_Event.__mro__:
        if "broadcast" in klass.__dict__:
            descriptor = klass.__dict__["broadcast"]
            break
    assert isinstance(descriptor, property)



def test_robochart_statemachine_is_not_abstract():
    assert not inspect.isabstract(robochart_StateMachine)


def test_robochart_statemachine_constructor_exists():
    assert callable(robochart_StateMachine.__init__)


def test_robochart_statemachine_constructor_args():
    sig = inspect.signature(robochart_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_robochart_controller_is_not_abstract():
    assert not inspect.isabstract(robochart_Controller)


def test_robochart_controller_constructor_exists():
    assert callable(robochart_Controller.__init__)


def test_robochart_controller_constructor_args():
    sig = inspect.signature(robochart_Controller.__init__)
    params = list(sig.parameters.keys())



def test_robochart_operationsig_is_not_abstract():
    assert not inspect.isabstract(robochart_OperationSig)


def test_robochart_operationsig_constructor_exists():
    assert callable(robochart_OperationSig.__init__)


def test_robochart_operationsig_constructor_args():
    sig = inspect.signature(robochart_OperationSig.__init__)
    params = list(sig.parameters.keys())
    assert "terminates" in params, "Missing parameter 'terminates'"

def test_robochart_operationsig_has_terminates():
    assert hasattr(robochart_OperationSig, "terminates")
    descriptor = None
    for klass in robochart_OperationSig.__mro__:
        if "terminates" in klass.__dict__:
            descriptor = klass.__dict__["terminates"]
            break
    assert isinstance(descriptor, property)



def test_robochart_operation_is_not_abstract():
    assert not inspect.isabstract(robochart_Operation)


def test_robochart_operation_constructor_exists():
    assert callable(robochart_Operation.__init__)


def test_robochart_operation_constructor_args():
    sig = inspect.signature(robochart_Operation.__init__)
    params = list(sig.parameters.keys())



def test_robochart_declaration_is_not_abstract():
    assert not inspect.isabstract(robochart_Declaration)


def test_robochart_declaration_constructor_exists():
    assert callable(robochart_Declaration.__init__)


def test_robochart_declaration_constructor_args():
    sig = inspect.signature(robochart_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_robochart_transition_is_not_abstract():
    assert not inspect.isabstract(robochart_Transition)


def test_robochart_transition_constructor_exists():
    assert callable(robochart_Transition.__init__)


def test_robochart_transition_constructor_args():
    sig = inspect.signature(robochart_Transition.__init__)
    params = list(sig.parameters.keys())



def test_robochart_clock_is_not_abstract():
    assert not inspect.isabstract(robochart_Clock)


def test_robochart_clock_constructor_exists():
    assert callable(robochart_Clock.__init__)


def test_robochart_clock_constructor_args():
    sig = inspect.signature(robochart_Clock.__init__)
    params = list(sig.parameters.keys())



def test_robochart_waitingcondition_is_not_abstract():
    assert not inspect.isabstract(robochart_WaitingCondition)


def test_robochart_waitingcondition_constructor_exists():
    assert callable(robochart_WaitingCondition.__init__)


def test_robochart_waitingcondition_constructor_args():
    sig = inspect.signature(robochart_WaitingCondition.__init__)
    params = list(sig.parameters.keys())



def test_robochart_roboticplatform_is_not_abstract():
    assert not inspect.isabstract(robochart_RoboticPlatform)


def test_robochart_roboticplatform_constructor_exists():
    assert callable(robochart_RoboticPlatform.__init__)


def test_robochart_roboticplatform_constructor_args():
    sig = inspect.signature(robochart_RoboticPlatform.__init__)
    params = list(sig.parameters.keys())



def test_robochart_node_is_not_abstract():
    assert not inspect.isabstract(robochart_Node)


def test_robochart_node_constructor_exists():
    assert callable(robochart_Node.__init__)


def test_robochart_node_constructor_args():
    sig = inspect.signature(robochart_Node.__init__)
    params = list(sig.parameters.keys())



def test_robochart_typednamedelement_is_not_abstract():
    assert not inspect.isabstract(robochart_TypedNamedElement)


def test_robochart_typednamedelement_constructor_exists():
    assert callable(robochart_TypedNamedElement.__init__)


def test_robochart_typednamedelement_constructor_args():
    sig = inspect.signature(robochart_TypedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_robochart_typedecl_is_not_abstract():
    assert not inspect.isabstract(robochart_TypeDecl)


def test_robochart_typedecl_constructor_exists():
    assert callable(robochart_TypeDecl.__init__)


def test_robochart_typedecl_constructor_args():
    sig = inspect.signature(robochart_TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_robochart_namedelement_is_not_abstract():
    assert not inspect.isabstract(robochart_NamedElement)


def test_robochart_namedelement_constructor_exists():
    assert callable(robochart_NamedElement.__init__)


def test_robochart_namedelement_constructor_args():
    sig = inspect.signature(robochart_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robochart_namedelement_has_name():
    assert hasattr(robochart_NamedElement, "name")
    descriptor = None
    for klass in robochart_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robochart_function_is_not_abstract():
    assert not inspect.isabstract(robochart_Function)


def test_robochart_function_constructor_exists():
    assert callable(robochart_Function.__init__)


def test_robochart_function_constructor_args():
    sig = inspect.signature(robochart_Function.__init__)
    params = list(sig.parameters.keys())



def test_robochart_operationdef_is_not_abstract():
    assert not inspect.isabstract(robochart_OperationDef)


def test_robochart_operationdef_constructor_exists():
    assert callable(robochart_OperationDef.__init__)


def test_robochart_operationdef_constructor_args():
    sig = inspect.signature(robochart_OperationDef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_rcmodule_is_not_abstract():
    assert not inspect.isabstract(robochart_RCModule)


def test_robochart_rcmodule_constructor_exists():
    assert callable(robochart_RCModule.__init__)


def test_robochart_rcmodule_constructor_args():
    sig = inspect.signature(robochart_RCModule.__init__)
    params = list(sig.parameters.keys())



def test_robochart_controllerdef_is_not_abstract():
    assert not inspect.isabstract(robochart_ControllerDef)


def test_robochart_controllerdef_constructor_exists():
    assert callable(robochart_ControllerDef.__init__)


def test_robochart_controllerdef_constructor_args():
    sig = inspect.signature(robochart_ControllerDef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_roboticplatformdef_is_not_abstract():
    assert not inspect.isabstract(robochart_RoboticPlatformDef)


def test_robochart_roboticplatformdef_constructor_exists():
    assert callable(robochart_RoboticPlatformDef.__init__)


def test_robochart_roboticplatformdef_constructor_args():
    sig = inspect.signature(robochart_RoboticPlatformDef.__init__)
    params = list(sig.parameters.keys())



def test_robochart_interface_is_not_abstract():
    assert not inspect.isabstract(robochart_Interface)


def test_robochart_interface_constructor_exists():
    assert callable(robochart_Interface.__init__)


def test_robochart_interface_constructor_args():
    sig = inspect.signature(robochart_Interface.__init__)
    params = list(sig.parameters.keys())



def test_basicpackage_is_not_abstract():
    assert not inspect.isabstract(BasicPackage)


def test_basicpackage_constructor_exists():
    assert callable(BasicPackage.__init__)


def test_basicpackage_constructor_args():
    sig = inspect.signature(BasicPackage.__init__)
    params = list(sig.parameters.keys())



def test_robochart_rcpackage_is_not_abstract():
    assert not inspect.isabstract(robochart_RCPackage)


def test_robochart_rcpackage_constructor_exists():
    assert callable(robochart_RCPackage.__init__)


def test_robochart_rcpackage_constructor_args():
    sig = inspect.signature(robochart_RCPackage.__init__)
    params = list(sig.parameters.keys())



def test_robochart_import_is_not_abstract():
    assert not inspect.isabstract(robochart_Import)


def test_robochart_import_constructor_exists():
    assert callable(robochart_Import.__init__)


def test_robochart_import_constructor_args():
    sig = inspect.signature(robochart_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_robochart_import_has_importedNamespace():
    assert hasattr(robochart_Import, "importedNamespace")
    descriptor = None
    for klass in robochart_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_robochart_basicpackage_is_not_abstract():
    assert not inspect.isabstract(robochart_BasicPackage)


def test_robochart_basicpackage_constructor_exists():
    assert callable(robochart_BasicPackage.__init__)


def test_robochart_basicpackage_constructor_args():
    sig = inspect.signature(robochart_BasicPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robochart_basicpackage_has_name():
    assert hasattr(robochart_BasicPackage, "name")
    descriptor = None
    for klass in robochart_BasicPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_triggertype_exists():
    # Check that the Enumeration exists
    assert TriggerType is not None

def test_triggertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerType]
    expected_literals = [
        "INPUT",
        "SIMPLE",
        "OUTPUT",
        "EMPTY",
        "SYNC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerType"

def test_variablemodifier_exists():
    # Check that the Enumeration exists
    assert VariableModifier is not None

def test_variablemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableModifier]
    expected_literals = [
        "CONST",
        "VAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableModifier"


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
robochart_NamedExpression_strategy = st.builds(
    robochart_NamedExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
robochart_Plus_strategy = st.builds(
    robochart_Plus,
)
robochart_Different_strategy = st.builds(
    robochart_Different,
)
robochart_Cat_strategy = st.builds(
    robochart_Cat,
)
robochart_Mult_strategy = st.builds(
    robochart_Mult,
)
robochart_LessThan_strategy = st.builds(
    robochart_LessThan,
)
robochart_GreaterThan_strategy = st.builds(
    robochart_GreaterThan,
)
robochart_Modulus_strategy = st.builds(
    robochart_Modulus,
)
robochart_Implies_strategy = st.builds(
    robochart_Implies,
)
robochart_LessOrEqual_strategy = st.builds(
    robochart_LessOrEqual,
)
robochart_Div_strategy = st.builds(
    robochart_Div,
)
robochart_Minus_strategy = st.builds(
    robochart_Minus,
)
robochart_GreaterOrEqual_strategy = st.builds(
    robochart_GreaterOrEqual,
)
robochart_Equals_strategy = st.builds(
    robochart_Equals,
)
robochart_Or_strategy = st.builds(
    robochart_Or,
)
robochart_And_strategy = st.builds(
    robochart_And,
)
robochart_Iff_strategy = st.builds(
    robochart_Iff,
)
LambdaExp_strategy = st.builds(
    LambdaExp,
)
robochart_DefiniteDescription_strategy = st.builds(
    robochart_DefiniteDescription,
)
QuantifierExpression_strategy = st.builds(
    QuantifierExpression,
)
robochart_Exists_strategy = st.builds(
    robochart_Exists,
    unique=
        st.booleans()
)
robochart_Forall_strategy = st.builds(
    robochart_Forall,
)
Expression_strategy = st.builds(
    Expression,
)
robochart_InExp_strategy = st.builds(
    robochart_InExp,
)
robochart_IfExpression_strategy = st.builds(
    robochart_IfExpression,
)
robochart_VarExp_strategy = st.builds(
    robochart_VarExp,
)
robochart_TupleExp_strategy = st.builds(
    robochart_TupleExp,
)
robochart_BooleanExp_strategy = st.builds(
    robochart_BooleanExp,
    value=
        safe_text
)
robochart_IntegerExp_strategy = st.builds(
    robochart_IntegerExp,
    value=
        st.integers()
)
robochart_LetExpression_strategy = st.builds(
    robochart_LetExpression,
)
robochart_ToExp_strategy = st.builds(
    robochart_ToExp,
)
robochart_IsExp_strategy = st.builds(
    robochart_IsExp,
)
robochart_ArrayExp_strategy = st.builds(
    robochart_ArrayExp,
)
robochart_LambdaExp_strategy = st.builds(
    robochart_LambdaExp,
)
robochart_Not_strategy = st.builds(
    robochart_Not,
)
robochart_TypeExp_strategy = st.builds(
    robochart_TypeExp,
)
robochart_QuantifierExpression_strategy = st.builds(
    robochart_QuantifierExpression,
)
robochart_ElseExp_strategy = st.builds(
    robochart_ElseExp,
)
robochart_StateClockExp_strategy = st.builds(
    robochart_StateClockExp,
)
robochart_SetExp_strategy = st.builds(
    robochart_SetExp,
)
robochart_EnumExp_strategy = st.builds(
    robochart_EnumExp,
)
robochart_SeqExp_strategy = st.builds(
    robochart_SeqExp,
)
robochart_SetComp_strategy = st.builds(
    robochart_SetComp,
)
robochart_IdExp_strategy = st.builds(
    robochart_IdExp,
)
robochart_AsExp_strategy = st.builds(
    robochart_AsExp,
)
robochart_BinaryExpression_strategy = st.builds(
    robochart_BinaryExpression,
)
robochart_FromExp_strategy = st.builds(
    robochart_FromExp,
)
robochart_RangeExp_strategy = st.builds(
    robochart_RangeExp,
    linterval=
        safe_text,
    rinterval=
        safe_text
)
robochart_Neg_strategy = st.builds(
    robochart_Neg,
)
robochart_StringExp_strategy = st.builds(
    robochart_StringExp,
    value=
        safe_text
)
robochart_FloatExp_strategy = st.builds(
    robochart_FloatExp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
robochart_RefExp_strategy = st.builds(
    robochart_RefExp,
)
robochart_SetRange_strategy = st.builds(
    robochart_SetRange,
)
robochart_ParExp_strategy = st.builds(
    robochart_ParExp,
)
robochart_ClockExp_strategy = st.builds(
    robochart_ClockExp,
)
robochart_Selection_strategy = st.builds(
    robochart_Selection,
)
robochart_ResultExp_strategy = st.builds(
    robochart_ResultExp,
)
robochart_Assignable_strategy = st.builds(
    robochart_Assignable,
)
Statement_strategy = st.builds(
    Statement,
)
robochart_Skip_strategy = st.builds(
    robochart_Skip,
)
robochart_Assignment_strategy = st.builds(
    robochart_Assignment,
)
robochart_SendEvent_strategy = st.builds(
    robochart_SendEvent,
)
robochart_Wait_strategy = st.builds(
    robochart_Wait,
)
robochart_Call_strategy = st.builds(
    robochart_Call,
)
robochart_ParStmt_strategy = st.builds(
    robochart_ParStmt,
)
robochart_IfStmt_strategy = st.builds(
    robochart_IfStmt,
)
robochart_SeqStatement_strategy = st.builds(
    robochart_SeqStatement,
)
robochart_TimedStatement_strategy = st.builds(
    robochart_TimedStatement,
)
robochart_ClockReset_strategy = st.builds(
    robochart_ClockReset,
)
robochart_ConnectionNode_strategy = st.builds(
    robochart_ConnectionNode,
)
robochart_Connection_strategy = st.builds(
    robochart_Connection,
    async_=
        st.booleans(),
    bidirec=
        st.booleans()
)
Controller_strategy = st.builds(
    Controller,
)
robochart_ControllerRef_strategy = st.builds(
    robochart_ControllerRef,
)
Action_strategy = st.builds(
    Action,
)
robochart_DuringAction_strategy = st.builds(
    robochart_DuringAction,
)
robochart_ExitAction_strategy = st.builds(
    robochart_ExitAction,
)
robochart_EntryAction_strategy = st.builds(
    robochart_EntryAction,
)
State_strategy = st.builds(
    State,
)
robochart_Final_strategy = st.builds(
    robochart_Final,
)
robochart_Action_strategy = st.builds(
    robochart_Action,
)
Junction_strategy = st.builds(
    Junction,
)
robochart_Initial_strategy = st.builds(
    robochart_Initial,
)
Node_strategy = st.builds(
    Node,
)
robochart_Junction_strategy = st.builds(
    robochart_Junction,
)
robochart_Statement_strategy = st.builds(
    robochart_Statement,
)
robochart_Trigger_strategy = st.builds(
    robochart_Trigger,
    _type=
        safe_text
)
robochart_ProbabilisticJunction_strategy = st.builds(
    robochart_ProbabilisticJunction,
)
RoboticPlatform_strategy = st.builds(
    RoboticPlatform,
)
Context_strategy = st.builds(
    Context,
)
robochart_NodeContainer_strategy = st.builds(
    robochart_NodeContainer,
)
NodeContainer_strategy = st.builds(
    NodeContainer,
)
robochart_State_strategy = st.builds(
    robochart_State,
)
robochart_StateMachineBody_strategy = st.builds(
    robochart_StateMachineBody,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
Variable_strategy = st.builds(
    Variable,
)
robochart_BasicContext_strategy = st.builds(
    robochart_BasicContext,
)
BasicContext_strategy = st.builds(
    BasicContext,
)
robochart_Context_strategy = st.builds(
    robochart_Context,
)
Reference_strategy = st.builds(
    Reference,
)
robochart_RoboticPlatformRef_strategy = st.builds(
    robochart_RoboticPlatformRef,
)
robochart_StateMachineRef_strategy = st.builds(
    robochart_StateMachineRef,
)
robochart_Reference_strategy = st.builds(
    robochart_Reference,
)
StateMachineBody_strategy = st.builds(
    StateMachineBody,
)
OperationSig_strategy = st.builds(
    OperationSig,
)
Operation_strategy = st.builds(
    Operation,
)
robochart_OperationRef_strategy = st.builds(
    robochart_OperationRef,
)
ConnectionNode_strategy = st.builds(
    ConnectionNode,
)
robochart_VariableList_strategy = st.builds(
    robochart_VariableList,
    modifier=
        safe_text
)
SetType_strategy = st.builds(
    SetType,
)
robochart_SeqType_strategy = st.builds(
    robochart_SeqType,
)
robochart_WaitingConditionRef_strategy = st.builds(
    robochart_WaitingConditionRef,
)
robochart_CallExp_strategy = st.builds(
    robochart_CallExp,
)
Assignable_strategy = st.builds(
    Assignable,
)
robochart_ArrayAssignable_strategy = st.builds(
    robochart_ArrayAssignable,
)
robochart_VarSelection_strategy = st.builds(
    robochart_VarSelection,
)
robochart_VarRef_strategy = st.builds(
    robochart_VarRef,
)
RelationType_strategy = st.builds(
    RelationType,
)
robochart_FunctionType_strategy = st.builds(
    robochart_FunctionType,
)
robochart_Parameter_strategy = st.builds(
    robochart_Parameter,
)
robochart_Expression_strategy = st.builds(
    robochart_Expression,
)
TypedNamedElement_strategy = st.builds(
    TypedNamedElement,
)
robochart_Member_strategy = st.builds(
    robochart_Member,
)
robochart_Type_strategy = st.builds(
    robochart_Type,
)
NamedExpression_strategy = st.builds(
    NamedExpression,
)
Member_strategy = st.builds(
    Member,
)
robochart_Variable_strategy = st.builds(
    robochart_Variable,
    modifier=
        safe_text
)
robochart_Field_strategy = st.builds(
    robochart_Field,
)
Type_strategy = st.builds(
    Type,
)
robochart_SetType_strategy = st.builds(
    robochart_SetType,
)
robochart_AnyType_strategy = st.builds(
    robochart_AnyType,
    identifier=
        safe_text
)
robochart_RelationType_strategy = st.builds(
    robochart_RelationType,
)
robochart_VectorType_strategy = st.builds(
    robochart_VectorType,
    size=
        st.integers()
)
robochart_TypeRef_strategy = st.builds(
    robochart_TypeRef,
)
robochart_MatrixType_strategy = st.builds(
    robochart_MatrixType,
    columns=
        st.integers(),
    rows=
        st.integers()
)
robochart_ProductType_strategy = st.builds(
    robochart_ProductType,
)
robochart_StateMachineDef_strategy = st.builds(
    robochart_StateMachineDef,
)
TypeDecl_strategy = st.builds(
    TypeDecl,
)
robochart_Enumeration_strategy = st.builds(
    robochart_Enumeration,
)
robochart_Literal_strategy = st.builds(
    robochart_Literal,
)
robochart_RecordType_strategy = st.builds(
    robochart_RecordType,
)
robochart_NameType_strategy = st.builds(
    robochart_NameType,
)
robochart_PrimitiveType_strategy = st.builds(
    robochart_PrimitiveType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
robochart_Event_strategy = st.builds(
    robochart_Event,
    broadcast=
        st.booleans()
)
robochart_StateMachine_strategy = st.builds(
    robochart_StateMachine,
)
robochart_Controller_strategy = st.builds(
    robochart_Controller,
)
robochart_OperationSig_strategy = st.builds(
    robochart_OperationSig,
    terminates=
        st.booleans()
)
robochart_Operation_strategy = st.builds(
    robochart_Operation,
)
robochart_Declaration_strategy = st.builds(
    robochart_Declaration,
)
robochart_Transition_strategy = st.builds(
    robochart_Transition,
)
robochart_Clock_strategy = st.builds(
    robochart_Clock,
)
robochart_WaitingCondition_strategy = st.builds(
    robochart_WaitingCondition,
)
robochart_RoboticPlatform_strategy = st.builds(
    robochart_RoboticPlatform,
)
robochart_Node_strategy = st.builds(
    robochart_Node,
)
robochart_TypedNamedElement_strategy = st.builds(
    robochart_TypedNamedElement,
)
robochart_TypeDecl_strategy = st.builds(
    robochart_TypeDecl,
)
robochart_NamedElement_strategy = st.builds(
    robochart_NamedElement,
    name=
        safe_text
)
robochart_Function_strategy = st.builds(
    robochart_Function,
)
robochart_OperationDef_strategy = st.builds(
    robochart_OperationDef,
)
robochart_RCModule_strategy = st.builds(
    robochart_RCModule,
)
robochart_ControllerDef_strategy = st.builds(
    robochart_ControllerDef,
)
robochart_RoboticPlatformDef_strategy = st.builds(
    robochart_RoboticPlatformDef,
)
robochart_Interface_strategy = st.builds(
    robochart_Interface,
)
BasicPackage_strategy = st.builds(
    BasicPackage,
)
robochart_RCPackage_strategy = st.builds(
    robochart_RCPackage,
)
robochart_Import_strategy = st.builds(
    robochart_Import,
    importedNamespace=
        safe_text
)
robochart_BasicPackage_strategy = st.builds(
    robochart_BasicPackage,
    name=
        safe_text
)

@given(instance=robochart_NamedExpression_strategy)
@settings(max_examples=50)
def test_robochart_namedexpression_instantiation(instance):
    assert isinstance(instance, robochart_NamedExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=robochart_Plus_strategy)
@settings(max_examples=50)
def test_robochart_plus_instantiation(instance):
    assert isinstance(instance, robochart_Plus)

@given(instance=robochart_Different_strategy)
@settings(max_examples=50)
def test_robochart_different_instantiation(instance):
    assert isinstance(instance, robochart_Different)

@given(instance=robochart_Cat_strategy)
@settings(max_examples=50)
def test_robochart_cat_instantiation(instance):
    assert isinstance(instance, robochart_Cat)

@given(instance=robochart_Mult_strategy)
@settings(max_examples=50)
def test_robochart_mult_instantiation(instance):
    assert isinstance(instance, robochart_Mult)

@given(instance=robochart_LessThan_strategy)
@settings(max_examples=50)
def test_robochart_lessthan_instantiation(instance):
    assert isinstance(instance, robochart_LessThan)

@given(instance=robochart_GreaterThan_strategy)
@settings(max_examples=50)
def test_robochart_greaterthan_instantiation(instance):
    assert isinstance(instance, robochart_GreaterThan)

@given(instance=robochart_Modulus_strategy)
@settings(max_examples=50)
def test_robochart_modulus_instantiation(instance):
    assert isinstance(instance, robochart_Modulus)

@given(instance=robochart_Implies_strategy)
@settings(max_examples=50)
def test_robochart_implies_instantiation(instance):
    assert isinstance(instance, robochart_Implies)

@given(instance=robochart_LessOrEqual_strategy)
@settings(max_examples=50)
def test_robochart_lessorequal_instantiation(instance):
    assert isinstance(instance, robochart_LessOrEqual)

@given(instance=robochart_Div_strategy)
@settings(max_examples=50)
def test_robochart_div_instantiation(instance):
    assert isinstance(instance, robochart_Div)

@given(instance=robochart_Minus_strategy)
@settings(max_examples=50)
def test_robochart_minus_instantiation(instance):
    assert isinstance(instance, robochart_Minus)

@given(instance=robochart_GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_robochart_greaterorequal_instantiation(instance):
    assert isinstance(instance, robochart_GreaterOrEqual)

@given(instance=robochart_Equals_strategy)
@settings(max_examples=50)
def test_robochart_equals_instantiation(instance):
    assert isinstance(instance, robochart_Equals)

@given(instance=robochart_Or_strategy)
@settings(max_examples=50)
def test_robochart_or_instantiation(instance):
    assert isinstance(instance, robochart_Or)

@given(instance=robochart_And_strategy)
@settings(max_examples=50)
def test_robochart_and_instantiation(instance):
    assert isinstance(instance, robochart_And)

@given(instance=robochart_Iff_strategy)
@settings(max_examples=50)
def test_robochart_iff_instantiation(instance):
    assert isinstance(instance, robochart_Iff)

@given(instance=LambdaExp_strategy)
@settings(max_examples=50)
def test_lambdaexp_instantiation(instance):
    assert isinstance(instance, LambdaExp)

@given(instance=robochart_DefiniteDescription_strategy)
@settings(max_examples=50)
def test_robochart_definitedescription_instantiation(instance):
    assert isinstance(instance, robochart_DefiniteDescription)

@given(instance=QuantifierExpression_strategy)
@settings(max_examples=50)
def test_quantifierexpression_instantiation(instance):
    assert isinstance(instance, QuantifierExpression)

@given(instance=robochart_Exists_strategy)
@settings(max_examples=50)
def test_robochart_exists_instantiation(instance):
    assert isinstance(instance, robochart_Exists)



@given(instance=robochart_Exists_strategy)
def test_robochart_exists_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=robochart_Forall_strategy)
@settings(max_examples=50)
def test_robochart_forall_instantiation(instance):
    assert isinstance(instance, robochart_Forall)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=robochart_InExp_strategy)
@settings(max_examples=50)
def test_robochart_inexp_instantiation(instance):
    assert isinstance(instance, robochart_InExp)

@given(instance=robochart_IfExpression_strategy)
@settings(max_examples=50)
def test_robochart_ifexpression_instantiation(instance):
    assert isinstance(instance, robochart_IfExpression)

@given(instance=robochart_VarExp_strategy)
@settings(max_examples=50)
def test_robochart_varexp_instantiation(instance):
    assert isinstance(instance, robochart_VarExp)

@given(instance=robochart_TupleExp_strategy)
@settings(max_examples=50)
def test_robochart_tupleexp_instantiation(instance):
    assert isinstance(instance, robochart_TupleExp)

@given(instance=robochart_BooleanExp_strategy)
@settings(max_examples=50)
def test_robochart_booleanexp_instantiation(instance):
    assert isinstance(instance, robochart_BooleanExp)



@given(instance=robochart_BooleanExp_strategy)
def test_robochart_booleanexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart_IntegerExp_strategy)
@settings(max_examples=50)
def test_robochart_integerexp_instantiation(instance):
    assert isinstance(instance, robochart_IntegerExp)



@given(instance=robochart_IntegerExp_strategy)
def test_robochart_integerexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart_LetExpression_strategy)
@settings(max_examples=50)
def test_robochart_letexpression_instantiation(instance):
    assert isinstance(instance, robochart_LetExpression)

@given(instance=robochart_ToExp_strategy)
@settings(max_examples=50)
def test_robochart_toexp_instantiation(instance):
    assert isinstance(instance, robochart_ToExp)

@given(instance=robochart_IsExp_strategy)
@settings(max_examples=50)
def test_robochart_isexp_instantiation(instance):
    assert isinstance(instance, robochart_IsExp)

@given(instance=robochart_ArrayExp_strategy)
@settings(max_examples=50)
def test_robochart_arrayexp_instantiation(instance):
    assert isinstance(instance, robochart_ArrayExp)

@given(instance=robochart_LambdaExp_strategy)
@settings(max_examples=50)
def test_robochart_lambdaexp_instantiation(instance):
    assert isinstance(instance, robochart_LambdaExp)

@given(instance=robochart_Not_strategy)
@settings(max_examples=50)
def test_robochart_not_instantiation(instance):
    assert isinstance(instance, robochart_Not)

@given(instance=robochart_TypeExp_strategy)
@settings(max_examples=50)
def test_robochart_typeexp_instantiation(instance):
    assert isinstance(instance, robochart_TypeExp)

@given(instance=robochart_QuantifierExpression_strategy)
@settings(max_examples=50)
def test_robochart_quantifierexpression_instantiation(instance):
    assert isinstance(instance, robochart_QuantifierExpression)

@given(instance=robochart_ElseExp_strategy)
@settings(max_examples=50)
def test_robochart_elseexp_instantiation(instance):
    assert isinstance(instance, robochart_ElseExp)

@given(instance=robochart_StateClockExp_strategy)
@settings(max_examples=50)
def test_robochart_stateclockexp_instantiation(instance):
    assert isinstance(instance, robochart_StateClockExp)

@given(instance=robochart_SetExp_strategy)
@settings(max_examples=50)
def test_robochart_setexp_instantiation(instance):
    assert isinstance(instance, robochart_SetExp)

@given(instance=robochart_EnumExp_strategy)
@settings(max_examples=50)
def test_robochart_enumexp_instantiation(instance):
    assert isinstance(instance, robochart_EnumExp)

@given(instance=robochart_SeqExp_strategy)
@settings(max_examples=50)
def test_robochart_seqexp_instantiation(instance):
    assert isinstance(instance, robochart_SeqExp)

@given(instance=robochart_SetComp_strategy)
@settings(max_examples=50)
def test_robochart_setcomp_instantiation(instance):
    assert isinstance(instance, robochart_SetComp)

@given(instance=robochart_IdExp_strategy)
@settings(max_examples=50)
def test_robochart_idexp_instantiation(instance):
    assert isinstance(instance, robochart_IdExp)

@given(instance=robochart_AsExp_strategy)
@settings(max_examples=50)
def test_robochart_asexp_instantiation(instance):
    assert isinstance(instance, robochart_AsExp)

@given(instance=robochart_BinaryExpression_strategy)
@settings(max_examples=50)
def test_robochart_binaryexpression_instantiation(instance):
    assert isinstance(instance, robochart_BinaryExpression)

@given(instance=robochart_FromExp_strategy)
@settings(max_examples=50)
def test_robochart_fromexp_instantiation(instance):
    assert isinstance(instance, robochart_FromExp)

@given(instance=robochart_RangeExp_strategy)
@settings(max_examples=50)
def test_robochart_rangeexp_instantiation(instance):
    assert isinstance(instance, robochart_RangeExp)



@given(instance=robochart_RangeExp_strategy)
def test_robochart_rangeexp_linterval_setter(instance):
    original = instance.linterval
    instance.linterval = original
    assert instance.linterval == original



@given(instance=robochart_RangeExp_strategy)
def test_robochart_rangeexp_rinterval_setter(instance):
    original = instance.rinterval
    instance.rinterval = original
    assert instance.rinterval == original

@given(instance=robochart_Neg_strategy)
@settings(max_examples=50)
def test_robochart_neg_instantiation(instance):
    assert isinstance(instance, robochart_Neg)

@given(instance=robochart_StringExp_strategy)
@settings(max_examples=50)
def test_robochart_stringexp_instantiation(instance):
    assert isinstance(instance, robochart_StringExp)



@given(instance=robochart_StringExp_strategy)
def test_robochart_stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart_FloatExp_strategy)
@settings(max_examples=50)
def test_robochart_floatexp_instantiation(instance):
    assert isinstance(instance, robochart_FloatExp)



@given(instance=robochart_FloatExp_strategy)
def test_robochart_floatexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=robochart_RefExp_strategy)
@settings(max_examples=50)
def test_robochart_refexp_instantiation(instance):
    assert isinstance(instance, robochart_RefExp)

@given(instance=robochart_SetRange_strategy)
@settings(max_examples=50)
def test_robochart_setrange_instantiation(instance):
    assert isinstance(instance, robochart_SetRange)

@given(instance=robochart_ParExp_strategy)
@settings(max_examples=50)
def test_robochart_parexp_instantiation(instance):
    assert isinstance(instance, robochart_ParExp)

@given(instance=robochart_ClockExp_strategy)
@settings(max_examples=50)
def test_robochart_clockexp_instantiation(instance):
    assert isinstance(instance, robochart_ClockExp)

@given(instance=robochart_Selection_strategy)
@settings(max_examples=50)
def test_robochart_selection_instantiation(instance):
    assert isinstance(instance, robochart_Selection)

@given(instance=robochart_ResultExp_strategy)
@settings(max_examples=50)
def test_robochart_resultexp_instantiation(instance):
    assert isinstance(instance, robochart_ResultExp)

@given(instance=robochart_Assignable_strategy)
@settings(max_examples=50)
def test_robochart_assignable_instantiation(instance):
    assert isinstance(instance, robochart_Assignable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=robochart_Skip_strategy)
@settings(max_examples=50)
def test_robochart_skip_instantiation(instance):
    assert isinstance(instance, robochart_Skip)

@given(instance=robochart_Assignment_strategy)
@settings(max_examples=50)
def test_robochart_assignment_instantiation(instance):
    assert isinstance(instance, robochart_Assignment)

@given(instance=robochart_SendEvent_strategy)
@settings(max_examples=50)
def test_robochart_sendevent_instantiation(instance):
    assert isinstance(instance, robochart_SendEvent)

@given(instance=robochart_Wait_strategy)
@settings(max_examples=50)
def test_robochart_wait_instantiation(instance):
    assert isinstance(instance, robochart_Wait)

@given(instance=robochart_Call_strategy)
@settings(max_examples=50)
def test_robochart_call_instantiation(instance):
    assert isinstance(instance, robochart_Call)

@given(instance=robochart_ParStmt_strategy)
@settings(max_examples=50)
def test_robochart_parstmt_instantiation(instance):
    assert isinstance(instance, robochart_ParStmt)

@given(instance=robochart_IfStmt_strategy)
@settings(max_examples=50)
def test_robochart_ifstmt_instantiation(instance):
    assert isinstance(instance, robochart_IfStmt)

@given(instance=robochart_SeqStatement_strategy)
@settings(max_examples=50)
def test_robochart_seqstatement_instantiation(instance):
    assert isinstance(instance, robochart_SeqStatement)

@given(instance=robochart_TimedStatement_strategy)
@settings(max_examples=50)
def test_robochart_timedstatement_instantiation(instance):
    assert isinstance(instance, robochart_TimedStatement)

@given(instance=robochart_ClockReset_strategy)
@settings(max_examples=50)
def test_robochart_clockreset_instantiation(instance):
    assert isinstance(instance, robochart_ClockReset)

@given(instance=robochart_ConnectionNode_strategy)
@settings(max_examples=50)
def test_robochart_connectionnode_instantiation(instance):
    assert isinstance(instance, robochart_ConnectionNode)

@given(instance=robochart_Connection_strategy)
@settings(max_examples=50)
def test_robochart_connection_instantiation(instance):
    assert isinstance(instance, robochart_Connection)



@given(instance=robochart_Connection_strategy)
def test_robochart_connection_async__setter(instance):
    original = instance.async_
    instance.async_ = original
    assert instance.async_ == original



@given(instance=robochart_Connection_strategy)
def test_robochart_connection_bidirec_setter(instance):
    original = instance.bidirec
    instance.bidirec = original
    assert instance.bidirec == original

@given(instance=Controller_strategy)
@settings(max_examples=50)
def test_controller_instantiation(instance):
    assert isinstance(instance, Controller)

@given(instance=robochart_ControllerRef_strategy)
@settings(max_examples=50)
def test_robochart_controllerref_instantiation(instance):
    assert isinstance(instance, robochart_ControllerRef)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=robochart_DuringAction_strategy)
@settings(max_examples=50)
def test_robochart_duringaction_instantiation(instance):
    assert isinstance(instance, robochart_DuringAction)

@given(instance=robochart_ExitAction_strategy)
@settings(max_examples=50)
def test_robochart_exitaction_instantiation(instance):
    assert isinstance(instance, robochart_ExitAction)

@given(instance=robochart_EntryAction_strategy)
@settings(max_examples=50)
def test_robochart_entryaction_instantiation(instance):
    assert isinstance(instance, robochart_EntryAction)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=robochart_Final_strategy)
@settings(max_examples=50)
def test_robochart_final_instantiation(instance):
    assert isinstance(instance, robochart_Final)

@given(instance=robochart_Action_strategy)
@settings(max_examples=50)
def test_robochart_action_instantiation(instance):
    assert isinstance(instance, robochart_Action)

@given(instance=Junction_strategy)
@settings(max_examples=50)
def test_junction_instantiation(instance):
    assert isinstance(instance, Junction)

@given(instance=robochart_Initial_strategy)
@settings(max_examples=50)
def test_robochart_initial_instantiation(instance):
    assert isinstance(instance, robochart_Initial)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=robochart_Junction_strategy)
@settings(max_examples=50)
def test_robochart_junction_instantiation(instance):
    assert isinstance(instance, robochart_Junction)

@given(instance=robochart_Statement_strategy)
@settings(max_examples=50)
def test_robochart_statement_instantiation(instance):
    assert isinstance(instance, robochart_Statement)

@given(instance=robochart_Trigger_strategy)
@settings(max_examples=50)
def test_robochart_trigger_instantiation(instance):
    assert isinstance(instance, robochart_Trigger)



@given(instance=robochart_Trigger_strategy)
def test_robochart_trigger__type_setter(instance):
    original = instance._type
    instance._type = original
    assert instance._type == original

@given(instance=robochart_ProbabilisticJunction_strategy)
@settings(max_examples=50)
def test_robochart_probabilisticjunction_instantiation(instance):
    assert isinstance(instance, robochart_ProbabilisticJunction)

@given(instance=RoboticPlatform_strategy)
@settings(max_examples=50)
def test_roboticplatform_instantiation(instance):
    assert isinstance(instance, RoboticPlatform)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=robochart_NodeContainer_strategy)
@settings(max_examples=50)
def test_robochart_nodecontainer_instantiation(instance):
    assert isinstance(instance, robochart_NodeContainer)

@given(instance=NodeContainer_strategy)
@settings(max_examples=50)
def test_nodecontainer_instantiation(instance):
    assert isinstance(instance, NodeContainer)

@given(instance=robochart_State_strategy)
@settings(max_examples=50)
def test_robochart_state_instantiation(instance):
    assert isinstance(instance, robochart_State)

@given(instance=robochart_StateMachineBody_strategy)
@settings(max_examples=50)
def test_robochart_statemachinebody_instantiation(instance):
    assert isinstance(instance, robochart_StateMachineBody)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=robochart_BasicContext_strategy)
@settings(max_examples=50)
def test_robochart_basiccontext_instantiation(instance):
    assert isinstance(instance, robochart_BasicContext)

@given(instance=BasicContext_strategy)
@settings(max_examples=50)
def test_basiccontext_instantiation(instance):
    assert isinstance(instance, BasicContext)

@given(instance=robochart_Context_strategy)
@settings(max_examples=50)
def test_robochart_context_instantiation(instance):
    assert isinstance(instance, robochart_Context)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=robochart_RoboticPlatformRef_strategy)
@settings(max_examples=50)
def test_robochart_roboticplatformref_instantiation(instance):
    assert isinstance(instance, robochart_RoboticPlatformRef)

@given(instance=robochart_StateMachineRef_strategy)
@settings(max_examples=50)
def test_robochart_statemachineref_instantiation(instance):
    assert isinstance(instance, robochart_StateMachineRef)

@given(instance=robochart_Reference_strategy)
@settings(max_examples=50)
def test_robochart_reference_instantiation(instance):
    assert isinstance(instance, robochart_Reference)

@given(instance=StateMachineBody_strategy)
@settings(max_examples=50)
def test_statemachinebody_instantiation(instance):
    assert isinstance(instance, StateMachineBody)

@given(instance=OperationSig_strategy)
@settings(max_examples=50)
def test_operationsig_instantiation(instance):
    assert isinstance(instance, OperationSig)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=robochart_OperationRef_strategy)
@settings(max_examples=50)
def test_robochart_operationref_instantiation(instance):
    assert isinstance(instance, robochart_OperationRef)

@given(instance=ConnectionNode_strategy)
@settings(max_examples=50)
def test_connectionnode_instantiation(instance):
    assert isinstance(instance, ConnectionNode)

@given(instance=robochart_VariableList_strategy)
@settings(max_examples=50)
def test_robochart_variablelist_instantiation(instance):
    assert isinstance(instance, robochart_VariableList)



@given(instance=robochart_VariableList_strategy)
def test_robochart_variablelist_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=SetType_strategy)
@settings(max_examples=50)
def test_settype_instantiation(instance):
    assert isinstance(instance, SetType)

@given(instance=robochart_SeqType_strategy)
@settings(max_examples=50)
def test_robochart_seqtype_instantiation(instance):
    assert isinstance(instance, robochart_SeqType)

@given(instance=robochart_WaitingConditionRef_strategy)
@settings(max_examples=50)
def test_robochart_waitingconditionref_instantiation(instance):
    assert isinstance(instance, robochart_WaitingConditionRef)

@given(instance=robochart_CallExp_strategy)
@settings(max_examples=50)
def test_robochart_callexp_instantiation(instance):
    assert isinstance(instance, robochart_CallExp)

@given(instance=Assignable_strategy)
@settings(max_examples=50)
def test_assignable_instantiation(instance):
    assert isinstance(instance, Assignable)

@given(instance=robochart_ArrayAssignable_strategy)
@settings(max_examples=50)
def test_robochart_arrayassignable_instantiation(instance):
    assert isinstance(instance, robochart_ArrayAssignable)

@given(instance=robochart_VarSelection_strategy)
@settings(max_examples=50)
def test_robochart_varselection_instantiation(instance):
    assert isinstance(instance, robochart_VarSelection)

@given(instance=robochart_VarRef_strategy)
@settings(max_examples=50)
def test_robochart_varref_instantiation(instance):
    assert isinstance(instance, robochart_VarRef)

@given(instance=RelationType_strategy)
@settings(max_examples=50)
def test_relationtype_instantiation(instance):
    assert isinstance(instance, RelationType)

@given(instance=robochart_FunctionType_strategy)
@settings(max_examples=50)
def test_robochart_functiontype_instantiation(instance):
    assert isinstance(instance, robochart_FunctionType)

@given(instance=robochart_Parameter_strategy)
@settings(max_examples=50)
def test_robochart_parameter_instantiation(instance):
    assert isinstance(instance, robochart_Parameter)

@given(instance=robochart_Expression_strategy)
@settings(max_examples=50)
def test_robochart_expression_instantiation(instance):
    assert isinstance(instance, robochart_Expression)

@given(instance=TypedNamedElement_strategy)
@settings(max_examples=50)
def test_typednamedelement_instantiation(instance):
    assert isinstance(instance, TypedNamedElement)

@given(instance=robochart_Member_strategy)
@settings(max_examples=50)
def test_robochart_member_instantiation(instance):
    assert isinstance(instance, robochart_Member)

@given(instance=robochart_Type_strategy)
@settings(max_examples=50)
def test_robochart_type_instantiation(instance):
    assert isinstance(instance, robochart_Type)

@given(instance=NamedExpression_strategy)
@settings(max_examples=50)
def test_namedexpression_instantiation(instance):
    assert isinstance(instance, NamedExpression)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=robochart_Variable_strategy)
@settings(max_examples=50)
def test_robochart_variable_instantiation(instance):
    assert isinstance(instance, robochart_Variable)



@given(instance=robochart_Variable_strategy)
def test_robochart_variable_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=robochart_Field_strategy)
@settings(max_examples=50)
def test_robochart_field_instantiation(instance):
    assert isinstance(instance, robochart_Field)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=robochart_SetType_strategy)
@settings(max_examples=50)
def test_robochart_settype_instantiation(instance):
    assert isinstance(instance, robochart_SetType)

@given(instance=robochart_AnyType_strategy)
@settings(max_examples=50)
def test_robochart_anytype_instantiation(instance):
    assert isinstance(instance, robochart_AnyType)



@given(instance=robochart_AnyType_strategy)
def test_robochart_anytype_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=robochart_RelationType_strategy)
@settings(max_examples=50)
def test_robochart_relationtype_instantiation(instance):
    assert isinstance(instance, robochart_RelationType)

@given(instance=robochart_VectorType_strategy)
@settings(max_examples=50)
def test_robochart_vectortype_instantiation(instance):
    assert isinstance(instance, robochart_VectorType)



@given(instance=robochart_VectorType_strategy)
def test_robochart_vectortype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=robochart_TypeRef_strategy)
@settings(max_examples=50)
def test_robochart_typeref_instantiation(instance):
    assert isinstance(instance, robochart_TypeRef)

@given(instance=robochart_MatrixType_strategy)
@settings(max_examples=50)
def test_robochart_matrixtype_instantiation(instance):
    assert isinstance(instance, robochart_MatrixType)



@given(instance=robochart_MatrixType_strategy)
def test_robochart_matrixtype_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=robochart_MatrixType_strategy)
def test_robochart_matrixtype_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=robochart_ProductType_strategy)
@settings(max_examples=50)
def test_robochart_producttype_instantiation(instance):
    assert isinstance(instance, robochart_ProductType)

@given(instance=robochart_StateMachineDef_strategy)
@settings(max_examples=50)
def test_robochart_statemachinedef_instantiation(instance):
    assert isinstance(instance, robochart_StateMachineDef)

@given(instance=TypeDecl_strategy)
@settings(max_examples=50)
def test_typedecl_instantiation(instance):
    assert isinstance(instance, TypeDecl)

@given(instance=robochart_Enumeration_strategy)
@settings(max_examples=50)
def test_robochart_enumeration_instantiation(instance):
    assert isinstance(instance, robochart_Enumeration)

@given(instance=robochart_Literal_strategy)
@settings(max_examples=50)
def test_robochart_literal_instantiation(instance):
    assert isinstance(instance, robochart_Literal)

@given(instance=robochart_RecordType_strategy)
@settings(max_examples=50)
def test_robochart_recordtype_instantiation(instance):
    assert isinstance(instance, robochart_RecordType)

@given(instance=robochart_NameType_strategy)
@settings(max_examples=50)
def test_robochart_nametype_instantiation(instance):
    assert isinstance(instance, robochart_NameType)

@given(instance=robochart_PrimitiveType_strategy)
@settings(max_examples=50)
def test_robochart_primitivetype_instantiation(instance):
    assert isinstance(instance, robochart_PrimitiveType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=robochart_Event_strategy)
@settings(max_examples=50)
def test_robochart_event_instantiation(instance):
    assert isinstance(instance, robochart_Event)



@given(instance=robochart_Event_strategy)
def test_robochart_event_broadcast_setter(instance):
    original = instance.broadcast
    instance.broadcast = original
    assert instance.broadcast == original

@given(instance=robochart_StateMachine_strategy)
@settings(max_examples=50)
def test_robochart_statemachine_instantiation(instance):
    assert isinstance(instance, robochart_StateMachine)

@given(instance=robochart_Controller_strategy)
@settings(max_examples=50)
def test_robochart_controller_instantiation(instance):
    assert isinstance(instance, robochart_Controller)

@given(instance=robochart_OperationSig_strategy)
@settings(max_examples=50)
def test_robochart_operationsig_instantiation(instance):
    assert isinstance(instance, robochart_OperationSig)



@given(instance=robochart_OperationSig_strategy)
def test_robochart_operationsig_terminates_setter(instance):
    original = instance.terminates
    instance.terminates = original
    assert instance.terminates == original

@given(instance=robochart_Operation_strategy)
@settings(max_examples=50)
def test_robochart_operation_instantiation(instance):
    assert isinstance(instance, robochart_Operation)

@given(instance=robochart_Declaration_strategy)
@settings(max_examples=50)
def test_robochart_declaration_instantiation(instance):
    assert isinstance(instance, robochart_Declaration)

@given(instance=robochart_Transition_strategy)
@settings(max_examples=50)
def test_robochart_transition_instantiation(instance):
    assert isinstance(instance, robochart_Transition)

@given(instance=robochart_Clock_strategy)
@settings(max_examples=50)
def test_robochart_clock_instantiation(instance):
    assert isinstance(instance, robochart_Clock)

@given(instance=robochart_WaitingCondition_strategy)
@settings(max_examples=50)
def test_robochart_waitingcondition_instantiation(instance):
    assert isinstance(instance, robochart_WaitingCondition)

@given(instance=robochart_RoboticPlatform_strategy)
@settings(max_examples=50)
def test_robochart_roboticplatform_instantiation(instance):
    assert isinstance(instance, robochart_RoboticPlatform)

@given(instance=robochart_Node_strategy)
@settings(max_examples=50)
def test_robochart_node_instantiation(instance):
    assert isinstance(instance, robochart_Node)

@given(instance=robochart_TypedNamedElement_strategy)
@settings(max_examples=50)
def test_robochart_typednamedelement_instantiation(instance):
    assert isinstance(instance, robochart_TypedNamedElement)

@given(instance=robochart_TypeDecl_strategy)
@settings(max_examples=50)
def test_robochart_typedecl_instantiation(instance):
    assert isinstance(instance, robochart_TypeDecl)

@given(instance=robochart_NamedElement_strategy)
@settings(max_examples=50)
def test_robochart_namedelement_instantiation(instance):
    assert isinstance(instance, robochart_NamedElement)



@given(instance=robochart_NamedElement_strategy)
def test_robochart_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robochart_Function_strategy)
@settings(max_examples=50)
def test_robochart_function_instantiation(instance):
    assert isinstance(instance, robochart_Function)

@given(instance=robochart_OperationDef_strategy)
@settings(max_examples=50)
def test_robochart_operationdef_instantiation(instance):
    assert isinstance(instance, robochart_OperationDef)

@given(instance=robochart_RCModule_strategy)
@settings(max_examples=50)
def test_robochart_rcmodule_instantiation(instance):
    assert isinstance(instance, robochart_RCModule)

@given(instance=robochart_ControllerDef_strategy)
@settings(max_examples=50)
def test_robochart_controllerdef_instantiation(instance):
    assert isinstance(instance, robochart_ControllerDef)

@given(instance=robochart_RoboticPlatformDef_strategy)
@settings(max_examples=50)
def test_robochart_roboticplatformdef_instantiation(instance):
    assert isinstance(instance, robochart_RoboticPlatformDef)

@given(instance=robochart_Interface_strategy)
@settings(max_examples=50)
def test_robochart_interface_instantiation(instance):
    assert isinstance(instance, robochart_Interface)

@given(instance=BasicPackage_strategy)
@settings(max_examples=50)
def test_basicpackage_instantiation(instance):
    assert isinstance(instance, BasicPackage)

@given(instance=robochart_RCPackage_strategy)
@settings(max_examples=50)
def test_robochart_rcpackage_instantiation(instance):
    assert isinstance(instance, robochart_RCPackage)

@given(instance=robochart_Import_strategy)
@settings(max_examples=50)
def test_robochart_import_instantiation(instance):
    assert isinstance(instance, robochart_Import)



@given(instance=robochart_Import_strategy)
def test_robochart_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=robochart_BasicPackage_strategy)
@settings(max_examples=50)
def test_robochart_basicpackage_instantiation(instance):
    assert isinstance(instance, robochart_BasicPackage)



@given(instance=robochart_BasicPackage_strategy)
def test_robochart_basicpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
