import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RegExp,
    cal_RegExpTag,
    cal_RegExpUnary,
    cal_RegExpBinary,
    cal_AnnotationArgument,
    AstType,
    cal_AstTypeUint,
    cal_AstTypeDouble,
    cal_AstTypeFloat,
    cal_AstTypeInt,
    cal_AstTypeHalf,
    cal_AstTypeString,
    cal_AstTypeBool,
    ExpressionLiteral,
    cal_ExpressionInteger,
    cal_ExpressionString,
    cal_ExpressionFloat,
    cal_ExpressionBoolean,
    cal_Generator,
    cal_ExpressionElsif,
    cal_AstTypeList,
    AstExpression,
    cal_ExpressionVariable,
    cal_ExpressionBinary,
    cal_ExpressionLiteral,
    cal_ExpressionUnary,
    cal_ExpressionList,
    cal_ExpressionIndex,
    cal_ExpressionCall,
    cal_StatementElsif,
    cal_ExpressionIf,
    cal_VariableReference,
    Statement,
    cal_StatementWhile,
    cal_StatementIf,
    cal_StatementCall,
    cal_StatementAssign,
    cal_Guard,
    cal_OutputPattern,
    cal_InputPattern,
    cal_StatementForeach,
    cal_ExternalTarget,
    cal_AstTransition,
    cal_Fsm,
    cal_AstState,
    cal_Inequality,
    cal_AstTag,
    cal_Statement,
    cal_Priority,
    cal_RegExp,
    cal_ScheduleFsm,
    cal_LocalFsm,
    cal_AstAction,
    cal_AstPort,
    cal_AstType,
    cal_AstExpression,
    cal_Variable,
    cal_AstProcedure,
    cal_Function,
    cal_AstUnit,
    cal_AstActor,
    cal_AstAnnotation,
    cal_Import,
    cal_AstEntity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_regexp_is_not_abstract():
    assert not inspect.isabstract(RegExp)


def test_regexp_constructor_exists():
    assert callable(RegExp.__init__)


def test_regexp_constructor_args():
    sig = inspect.signature(RegExp.__init__)
    params = list(sig.parameters.keys())



def test_cal_regexptag_is_not_abstract():
    assert not inspect.isabstract(cal_RegExpTag)


def test_cal_regexptag_constructor_exists():
    assert callable(cal_RegExpTag.__init__)


def test_cal_regexptag_constructor_args():
    sig = inspect.signature(cal_RegExpTag.__init__)
    params = list(sig.parameters.keys())



def test_cal_regexpunary_is_not_abstract():
    assert not inspect.isabstract(cal_RegExpUnary)


def test_cal_regexpunary_constructor_exists():
    assert callable(cal_RegExpUnary.__init__)


def test_cal_regexpunary_constructor_args():
    sig = inspect.signature(cal_RegExpUnary.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_cal_regexpunary_has_unaryOperator():
    assert hasattr(cal_RegExpUnary, "unaryOperator")
    descriptor = None
    for klass in cal_RegExpUnary.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_cal_regexpbinary_is_not_abstract():
    assert not inspect.isabstract(cal_RegExpBinary)


def test_cal_regexpbinary_constructor_exists():
    assert callable(cal_RegExpBinary.__init__)


def test_cal_regexpbinary_constructor_args():
    sig = inspect.signature(cal_RegExpBinary.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_cal_regexpbinary_has_operator():
    assert hasattr(cal_RegExpBinary, "operator")
    descriptor = None
    for klass in cal_RegExpBinary.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cal_annotationargument_is_not_abstract():
    assert not inspect.isabstract(cal_AnnotationArgument)


def test_cal_annotationargument_constructor_exists():
    assert callable(cal_AnnotationArgument.__init__)


def test_cal_annotationargument_constructor_args():
    sig = inspect.signature(cal_AnnotationArgument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_cal_annotationargument_has_value():
    assert hasattr(cal_AnnotationArgument, "value")
    descriptor = None
    for klass in cal_AnnotationArgument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cal_annotationargument_has_name():
    assert hasattr(cal_AnnotationArgument, "name")
    descriptor = None
    for klass in cal_AnnotationArgument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asttype_is_not_abstract():
    assert not inspect.isabstract(AstType)


def test_asttype_constructor_exists():
    assert callable(AstType.__init__)


def test_asttype_constructor_args():
    sig = inspect.signature(AstType.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypeuint_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeUint)


def test_cal_asttypeuint_constructor_exists():
    assert callable(cal_AstTypeUint.__init__)


def test_cal_asttypeuint_constructor_args():
    sig = inspect.signature(cal_AstTypeUint.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypedouble_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeDouble)


def test_cal_asttypedouble_constructor_exists():
    assert callable(cal_AstTypeDouble.__init__)


def test_cal_asttypedouble_constructor_args():
    sig = inspect.signature(cal_AstTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypefloat_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeFloat)


def test_cal_asttypefloat_constructor_exists():
    assert callable(cal_AstTypeFloat.__init__)


def test_cal_asttypefloat_constructor_args():
    sig = inspect.signature(cal_AstTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypeint_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeInt)


def test_cal_asttypeint_constructor_exists():
    assert callable(cal_AstTypeInt.__init__)


def test_cal_asttypeint_constructor_args():
    sig = inspect.signature(cal_AstTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypehalf_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeHalf)


def test_cal_asttypehalf_constructor_exists():
    assert callable(cal_AstTypeHalf.__init__)


def test_cal_asttypehalf_constructor_args():
    sig = inspect.signature(cal_AstTypeHalf.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypestring_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeString)


def test_cal_asttypestring_constructor_exists():
    assert callable(cal_AstTypeString.__init__)


def test_cal_asttypestring_constructor_args():
    sig = inspect.signature(cal_AstTypeString.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypebool_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeBool)


def test_cal_asttypebool_constructor_exists():
    assert callable(cal_AstTypeBool.__init__)


def test_cal_asttypebool_constructor_args():
    sig = inspect.signature(cal_AstTypeBool.__init__)
    params = list(sig.parameters.keys())



def test_expressionliteral_is_not_abstract():
    assert not inspect.isabstract(ExpressionLiteral)


def test_expressionliteral_constructor_exists():
    assert callable(ExpressionLiteral.__init__)


def test_expressionliteral_constructor_args():
    sig = inspect.signature(ExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressioninteger_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionInteger)


def test_cal_expressioninteger_constructor_exists():
    assert callable(cal_ExpressionInteger.__init__)


def test_cal_expressioninteger_constructor_args():
    sig = inspect.signature(cal_ExpressionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_expressioninteger_has_value():
    assert hasattr(cal_ExpressionInteger, "value")
    descriptor = None
    for klass in cal_ExpressionInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_expressionstring_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionString)


def test_cal_expressionstring_constructor_exists():
    assert callable(cal_ExpressionString.__init__)


def test_cal_expressionstring_constructor_args():
    sig = inspect.signature(cal_ExpressionString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_expressionstring_has_value():
    assert hasattr(cal_ExpressionString, "value")
    descriptor = None
    for klass in cal_ExpressionString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_expressionfloat_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionFloat)


def test_cal_expressionfloat_constructor_exists():
    assert callable(cal_ExpressionFloat.__init__)


def test_cal_expressionfloat_constructor_args():
    sig = inspect.signature(cal_ExpressionFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_expressionfloat_has_value():
    assert hasattr(cal_ExpressionFloat, "value")
    descriptor = None
    for klass in cal_ExpressionFloat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_expressionboolean_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionBoolean)


def test_cal_expressionboolean_constructor_exists():
    assert callable(cal_ExpressionBoolean.__init__)


def test_cal_expressionboolean_constructor_args():
    sig = inspect.signature(cal_ExpressionBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_expressionboolean_has_value():
    assert hasattr(cal_ExpressionBoolean, "value")
    descriptor = None
    for klass in cal_ExpressionBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_generator_is_not_abstract():
    assert not inspect.isabstract(cal_Generator)


def test_cal_generator_constructor_exists():
    assert callable(cal_Generator.__init__)


def test_cal_generator_constructor_args():
    sig = inspect.signature(cal_Generator.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressionelsif_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionElsif)


def test_cal_expressionelsif_constructor_exists():
    assert callable(cal_ExpressionElsif.__init__)


def test_cal_expressionelsif_constructor_args():
    sig = inspect.signature(cal_ExpressionElsif.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypelist_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeList)


def test_cal_asttypelist_constructor_exists():
    assert callable(cal_AstTypeList.__init__)


def test_cal_asttypelist_constructor_args():
    sig = inspect.signature(cal_AstTypeList.__init__)
    params = list(sig.parameters.keys())



def test_astexpression_is_not_abstract():
    assert not inspect.isabstract(AstExpression)


def test_astexpression_constructor_exists():
    assert callable(AstExpression.__init__)


def test_astexpression_constructor_args():
    sig = inspect.signature(AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressionvariable_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionVariable)


def test_cal_expressionvariable_constructor_exists():
    assert callable(cal_ExpressionVariable.__init__)


def test_cal_expressionvariable_constructor_args():
    sig = inspect.signature(cal_ExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressionbinary_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionBinary)


def test_cal_expressionbinary_constructor_exists():
    assert callable(cal_ExpressionBinary.__init__)


def test_cal_expressionbinary_constructor_args():
    sig = inspect.signature(cal_ExpressionBinary.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_cal_expressionbinary_has_operator():
    assert hasattr(cal_ExpressionBinary, "operator")
    descriptor = None
    for klass in cal_ExpressionBinary.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cal_expressionliteral_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionLiteral)


def test_cal_expressionliteral_constructor_exists():
    assert callable(cal_ExpressionLiteral.__init__)


def test_cal_expressionliteral_constructor_args():
    sig = inspect.signature(cal_ExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressionunary_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionUnary)


def test_cal_expressionunary_constructor_exists():
    assert callable(cal_ExpressionUnary.__init__)


def test_cal_expressionunary_constructor_args():
    sig = inspect.signature(cal_ExpressionUnary.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_cal_expressionunary_has_unaryOperator():
    assert hasattr(cal_ExpressionUnary, "unaryOperator")
    descriptor = None
    for klass in cal_ExpressionUnary.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_cal_expressionlist_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionList)


def test_cal_expressionlist_constructor_exists():
    assert callable(cal_ExpressionList.__init__)


def test_cal_expressionlist_constructor_args():
    sig = inspect.signature(cal_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressionindex_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionIndex)


def test_cal_expressionindex_constructor_exists():
    assert callable(cal_ExpressionIndex.__init__)


def test_cal_expressionindex_constructor_args():
    sig = inspect.signature(cal_ExpressionIndex.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressioncall_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionCall)


def test_cal_expressioncall_constructor_exists():
    assert callable(cal_ExpressionCall.__init__)


def test_cal_expressioncall_constructor_args():
    sig = inspect.signature(cal_ExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_cal_statementelsif_is_not_abstract():
    assert not inspect.isabstract(cal_StatementElsif)


def test_cal_statementelsif_constructor_exists():
    assert callable(cal_StatementElsif.__init__)


def test_cal_statementelsif_constructor_args():
    sig = inspect.signature(cal_StatementElsif.__init__)
    params = list(sig.parameters.keys())



def test_cal_expressionif_is_not_abstract():
    assert not inspect.isabstract(cal_ExpressionIf)


def test_cal_expressionif_constructor_exists():
    assert callable(cal_ExpressionIf.__init__)


def test_cal_expressionif_constructor_args():
    sig = inspect.signature(cal_ExpressionIf.__init__)
    params = list(sig.parameters.keys())



def test_cal_variablereference_is_not_abstract():
    assert not inspect.isabstract(cal_VariableReference)


def test_cal_variablereference_constructor_exists():
    assert callable(cal_VariableReference.__init__)


def test_cal_variablereference_constructor_args():
    sig = inspect.signature(cal_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_cal_statementwhile_is_not_abstract():
    assert not inspect.isabstract(cal_StatementWhile)


def test_cal_statementwhile_constructor_exists():
    assert callable(cal_StatementWhile.__init__)


def test_cal_statementwhile_constructor_args():
    sig = inspect.signature(cal_StatementWhile.__init__)
    params = list(sig.parameters.keys())



def test_cal_statementif_is_not_abstract():
    assert not inspect.isabstract(cal_StatementIf)


def test_cal_statementif_constructor_exists():
    assert callable(cal_StatementIf.__init__)


def test_cal_statementif_constructor_args():
    sig = inspect.signature(cal_StatementIf.__init__)
    params = list(sig.parameters.keys())



def test_cal_statementcall_is_not_abstract():
    assert not inspect.isabstract(cal_StatementCall)


def test_cal_statementcall_constructor_exists():
    assert callable(cal_StatementCall.__init__)


def test_cal_statementcall_constructor_args():
    sig = inspect.signature(cal_StatementCall.__init__)
    params = list(sig.parameters.keys())



def test_cal_statementassign_is_not_abstract():
    assert not inspect.isabstract(cal_StatementAssign)


def test_cal_statementassign_constructor_exists():
    assert callable(cal_StatementAssign.__init__)


def test_cal_statementassign_constructor_args():
    sig = inspect.signature(cal_StatementAssign.__init__)
    params = list(sig.parameters.keys())



def test_cal_guard_is_not_abstract():
    assert not inspect.isabstract(cal_Guard)


def test_cal_guard_constructor_exists():
    assert callable(cal_Guard.__init__)


def test_cal_guard_constructor_args():
    sig = inspect.signature(cal_Guard.__init__)
    params = list(sig.parameters.keys())



def test_cal_outputpattern_is_not_abstract():
    assert not inspect.isabstract(cal_OutputPattern)


def test_cal_outputpattern_constructor_exists():
    assert callable(cal_OutputPattern.__init__)


def test_cal_outputpattern_constructor_args():
    sig = inspect.signature(cal_OutputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal_inputpattern_is_not_abstract():
    assert not inspect.isabstract(cal_InputPattern)


def test_cal_inputpattern_constructor_exists():
    assert callable(cal_InputPattern.__init__)


def test_cal_inputpattern_constructor_args():
    sig = inspect.signature(cal_InputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal_statementforeach_is_not_abstract():
    assert not inspect.isabstract(cal_StatementForeach)


def test_cal_statementforeach_constructor_exists():
    assert callable(cal_StatementForeach.__init__)


def test_cal_statementforeach_constructor_args():
    sig = inspect.signature(cal_StatementForeach.__init__)
    params = list(sig.parameters.keys())



def test_cal_externaltarget_is_not_abstract():
    assert not inspect.isabstract(cal_ExternalTarget)


def test_cal_externaltarget_constructor_exists():
    assert callable(cal_ExternalTarget.__init__)


def test_cal_externaltarget_constructor_args():
    sig = inspect.signature(cal_ExternalTarget.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttransition_is_not_abstract():
    assert not inspect.isabstract(cal_AstTransition)


def test_cal_asttransition_constructor_exists():
    assert callable(cal_AstTransition.__init__)


def test_cal_asttransition_constructor_args():
    sig = inspect.signature(cal_AstTransition.__init__)
    params = list(sig.parameters.keys())



def test_cal_fsm_is_not_abstract():
    assert not inspect.isabstract(cal_Fsm)


def test_cal_fsm_constructor_exists():
    assert callable(cal_Fsm.__init__)


def test_cal_fsm_constructor_args():
    sig = inspect.signature(cal_Fsm.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststate_is_not_abstract():
    assert not inspect.isabstract(cal_AstState)


def test_cal_aststate_constructor_exists():
    assert callable(cal_AstState.__init__)


def test_cal_aststate_constructor_args():
    sig = inspect.signature(cal_AstState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "node" in params, "Missing parameter 'node'"

def test_cal_aststate_has_name():
    assert hasattr(cal_AstState, "name")
    descriptor = None
    for klass in cal_AstState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cal_aststate_has_node():
    assert hasattr(cal_AstState, "node")
    descriptor = None
    for klass in cal_AstState.__mro__:
        if "node" in klass.__dict__:
            descriptor = klass.__dict__["node"]
            break
    assert isinstance(descriptor, property)



def test_cal_inequality_is_not_abstract():
    assert not inspect.isabstract(cal_Inequality)


def test_cal_inequality_constructor_exists():
    assert callable(cal_Inequality.__init__)


def test_cal_inequality_constructor_args():
    sig = inspect.signature(cal_Inequality.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttag_is_not_abstract():
    assert not inspect.isabstract(cal_AstTag)


def test_cal_asttag_constructor_exists():
    assert callable(cal_AstTag.__init__)


def test_cal_asttag_constructor_args():
    sig = inspect.signature(cal_AstTag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"

def test_cal_asttag_has_identifiers():
    assert hasattr(cal_AstTag, "identifiers")
    descriptor = None
    for klass in cal_AstTag.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)



def test_cal_statement_is_not_abstract():
    assert not inspect.isabstract(cal_Statement)


def test_cal_statement_constructor_exists():
    assert callable(cal_Statement.__init__)


def test_cal_statement_constructor_args():
    sig = inspect.signature(cal_Statement.__init__)
    params = list(sig.parameters.keys())



def test_cal_priority_is_not_abstract():
    assert not inspect.isabstract(cal_Priority)


def test_cal_priority_constructor_exists():
    assert callable(cal_Priority.__init__)


def test_cal_priority_constructor_args():
    sig = inspect.signature(cal_Priority.__init__)
    params = list(sig.parameters.keys())



def test_cal_regexp_is_not_abstract():
    assert not inspect.isabstract(cal_RegExp)


def test_cal_regexp_constructor_exists():
    assert callable(cal_RegExp.__init__)


def test_cal_regexp_constructor_args():
    sig = inspect.signature(cal_RegExp.__init__)
    params = list(sig.parameters.keys())



def test_cal_schedulefsm_is_not_abstract():
    assert not inspect.isabstract(cal_ScheduleFsm)


def test_cal_schedulefsm_constructor_exists():
    assert callable(cal_ScheduleFsm.__init__)


def test_cal_schedulefsm_constructor_args():
    sig = inspect.signature(cal_ScheduleFsm.__init__)
    params = list(sig.parameters.keys())



def test_cal_localfsm_is_not_abstract():
    assert not inspect.isabstract(cal_LocalFsm)


def test_cal_localfsm_constructor_exists():
    assert callable(cal_LocalFsm.__init__)


def test_cal_localfsm_constructor_args():
    sig = inspect.signature(cal_LocalFsm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_localfsm_has_name():
    assert hasattr(cal_LocalFsm, "name")
    descriptor = None
    for klass in cal_LocalFsm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astaction_is_not_abstract():
    assert not inspect.isabstract(cal_AstAction)


def test_cal_astaction_constructor_exists():
    assert callable(cal_AstAction.__init__)


def test_cal_astaction_constructor_args():
    sig = inspect.signature(cal_AstAction.__init__)
    params = list(sig.parameters.keys())



def test_cal_astport_is_not_abstract():
    assert not inspect.isabstract(cal_AstPort)


def test_cal_astport_constructor_exists():
    assert callable(cal_AstPort.__init__)


def test_cal_astport_constructor_args():
    sig = inspect.signature(cal_AstPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astport_has_name():
    assert hasattr(cal_AstPort, "name")
    descriptor = None
    for klass in cal_AstPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_asttype_is_not_abstract():
    assert not inspect.isabstract(cal_AstType)


def test_cal_asttype_constructor_exists():
    assert callable(cal_AstType.__init__)


def test_cal_asttype_constructor_args():
    sig = inspect.signature(cal_AstType.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpression_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpression)


def test_cal_astexpression_constructor_exists():
    assert callable(cal_AstExpression.__init__)


def test_cal_astexpression_constructor_args():
    sig = inspect.signature(cal_AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal_variable_is_not_abstract():
    assert not inspect.isabstract(cal_Variable)


def test_cal_variable_constructor_exists():
    assert callable(cal_Variable.__init__)


def test_cal_variable_constructor_args():
    sig = inspect.signature(cal_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_cal_variable_has_name():
    assert hasattr(cal_Variable, "name")
    descriptor = None
    for klass in cal_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cal_variable_has_constant():
    assert hasattr(cal_Variable, "constant")
    descriptor = None
    for klass in cal_Variable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_cal_astprocedure_is_not_abstract():
    assert not inspect.isabstract(cal_AstProcedure)


def test_cal_astprocedure_constructor_exists():
    assert callable(cal_AstProcedure.__init__)


def test_cal_astprocedure_constructor_args():
    sig = inspect.signature(cal_AstProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astprocedure_has_name():
    assert hasattr(cal_AstProcedure, "name")
    descriptor = None
    for klass in cal_AstProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_function_is_not_abstract():
    assert not inspect.isabstract(cal_Function)


def test_cal_function_constructor_exists():
    assert callable(cal_Function.__init__)


def test_cal_function_constructor_args():
    sig = inspect.signature(cal_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_function_has_name():
    assert hasattr(cal_Function, "name")
    descriptor = None
    for klass in cal_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astunit_is_not_abstract():
    assert not inspect.isabstract(cal_AstUnit)


def test_cal_astunit_constructor_exists():
    assert callable(cal_AstUnit.__init__)


def test_cal_astunit_constructor_args():
    sig = inspect.signature(cal_AstUnit.__init__)
    params = list(sig.parameters.keys())



def test_cal_astactor_is_not_abstract():
    assert not inspect.isabstract(cal_AstActor)


def test_cal_astactor_constructor_exists():
    assert callable(cal_AstActor.__init__)


def test_cal_astactor_constructor_args():
    sig = inspect.signature(cal_AstActor.__init__)
    params = list(sig.parameters.keys())



def test_cal_astannotation_is_not_abstract():
    assert not inspect.isabstract(cal_AstAnnotation)


def test_cal_astannotation_constructor_exists():
    assert callable(cal_AstAnnotation.__init__)


def test_cal_astannotation_constructor_args():
    sig = inspect.signature(cal_AstAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astannotation_has_name():
    assert hasattr(cal_AstAnnotation, "name")
    descriptor = None
    for klass in cal_AstAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_import_is_not_abstract():
    assert not inspect.isabstract(cal_Import)


def test_cal_import_constructor_exists():
    assert callable(cal_Import.__init__)


def test_cal_import_constructor_args():
    sig = inspect.signature(cal_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_cal_import_has_importedNamespace():
    assert hasattr(cal_Import, "importedNamespace")
    descriptor = None
    for klass in cal_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_cal_astentity_is_not_abstract():
    assert not inspect.isabstract(cal_AstEntity)


def test_cal_astentity_constructor_exists():
    assert callable(cal_AstEntity.__init__)


def test_cal_astentity_constructor_args():
    sig = inspect.signature(cal_AstEntity.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astentity_has_package():
    assert hasattr(cal_AstEntity, "package")
    descriptor = None
    for klass in cal_AstEntity.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_cal_astentity_has_name():
    assert hasattr(cal_AstEntity, "name")
    descriptor = None
    for klass in cal_AstEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
RegExp_strategy = st.builds(
    RegExp,
)
cal_RegExpTag_strategy = st.builds(
    cal_RegExpTag,
)
cal_RegExpUnary_strategy = st.builds(
    cal_RegExpUnary,
    unaryOperator=
        safe_text
)
cal_RegExpBinary_strategy = st.builds(
    cal_RegExpBinary,
    operator=
        safe_text
)
cal_AnnotationArgument_strategy = st.builds(
    cal_AnnotationArgument,
    value=
        safe_text,
    name=
        safe_text
)
AstType_strategy = st.builds(
    AstType,
)
cal_AstTypeUint_strategy = st.builds(
    cal_AstTypeUint,
)
cal_AstTypeDouble_strategy = st.builds(
    cal_AstTypeDouble,
)
cal_AstTypeFloat_strategy = st.builds(
    cal_AstTypeFloat,
)
cal_AstTypeInt_strategy = st.builds(
    cal_AstTypeInt,
)
cal_AstTypeHalf_strategy = st.builds(
    cal_AstTypeHalf,
)
cal_AstTypeString_strategy = st.builds(
    cal_AstTypeString,
)
cal_AstTypeBool_strategy = st.builds(
    cal_AstTypeBool,
)
ExpressionLiteral_strategy = st.builds(
    ExpressionLiteral,
)
cal_ExpressionInteger_strategy = st.builds(
    cal_ExpressionInteger,
    value=
        safe_text
)
cal_ExpressionString_strategy = st.builds(
    cal_ExpressionString,
    value=
        safe_text
)
cal_ExpressionFloat_strategy = st.builds(
    cal_ExpressionFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cal_ExpressionBoolean_strategy = st.builds(
    cal_ExpressionBoolean,
    value=
        st.booleans()
)
cal_Generator_strategy = st.builds(
    cal_Generator,
)
cal_ExpressionElsif_strategy = st.builds(
    cal_ExpressionElsif,
)
cal_AstTypeList_strategy = st.builds(
    cal_AstTypeList,
)
AstExpression_strategy = st.builds(
    AstExpression,
)
cal_ExpressionVariable_strategy = st.builds(
    cal_ExpressionVariable,
)
cal_ExpressionBinary_strategy = st.builds(
    cal_ExpressionBinary,
    operator=
        safe_text
)
cal_ExpressionLiteral_strategy = st.builds(
    cal_ExpressionLiteral,
)
cal_ExpressionUnary_strategy = st.builds(
    cal_ExpressionUnary,
    unaryOperator=
        safe_text
)
cal_ExpressionList_strategy = st.builds(
    cal_ExpressionList,
)
cal_ExpressionIndex_strategy = st.builds(
    cal_ExpressionIndex,
)
cal_ExpressionCall_strategy = st.builds(
    cal_ExpressionCall,
)
cal_StatementElsif_strategy = st.builds(
    cal_StatementElsif,
)
cal_ExpressionIf_strategy = st.builds(
    cal_ExpressionIf,
)
cal_VariableReference_strategy = st.builds(
    cal_VariableReference,
)
Statement_strategy = st.builds(
    Statement,
)
cal_StatementWhile_strategy = st.builds(
    cal_StatementWhile,
)
cal_StatementIf_strategy = st.builds(
    cal_StatementIf,
)
cal_StatementCall_strategy = st.builds(
    cal_StatementCall,
)
cal_StatementAssign_strategy = st.builds(
    cal_StatementAssign,
)
cal_Guard_strategy = st.builds(
    cal_Guard,
)
cal_OutputPattern_strategy = st.builds(
    cal_OutputPattern,
)
cal_InputPattern_strategy = st.builds(
    cal_InputPattern,
)
cal_StatementForeach_strategy = st.builds(
    cal_StatementForeach,
)
cal_ExternalTarget_strategy = st.builds(
    cal_ExternalTarget,
)
cal_AstTransition_strategy = st.builds(
    cal_AstTransition,
)
cal_Fsm_strategy = st.builds(
    cal_Fsm,
)
cal_AstState_strategy = st.builds(
    cal_AstState,
    name=
        safe_text,
    node=
        safe_text
)
cal_Inequality_strategy = st.builds(
    cal_Inequality,
)
cal_AstTag_strategy = st.builds(
    cal_AstTag,
    identifiers=
        safe_text
)
cal_Statement_strategy = st.builds(
    cal_Statement,
)
cal_Priority_strategy = st.builds(
    cal_Priority,
)
cal_RegExp_strategy = st.builds(
    cal_RegExp,
)
cal_ScheduleFsm_strategy = st.builds(
    cal_ScheduleFsm,
)
cal_LocalFsm_strategy = st.builds(
    cal_LocalFsm,
    name=
        safe_text
)
cal_AstAction_strategy = st.builds(
    cal_AstAction,
)
cal_AstPort_strategy = st.builds(
    cal_AstPort,
    name=
        safe_text
)
cal_AstType_strategy = st.builds(
    cal_AstType,
)
cal_AstExpression_strategy = st.builds(
    cal_AstExpression,
)
cal_Variable_strategy = st.builds(
    cal_Variable,
    name=
        safe_text,
    constant=
        st.booleans()
)
cal_AstProcedure_strategy = st.builds(
    cal_AstProcedure,
    name=
        safe_text
)
cal_Function_strategy = st.builds(
    cal_Function,
    name=
        safe_text
)
cal_AstUnit_strategy = st.builds(
    cal_AstUnit,
)
cal_AstActor_strategy = st.builds(
    cal_AstActor,
)
cal_AstAnnotation_strategy = st.builds(
    cal_AstAnnotation,
    name=
        safe_text
)
cal_Import_strategy = st.builds(
    cal_Import,
    importedNamespace=
        safe_text
)
cal_AstEntity_strategy = st.builds(
    cal_AstEntity,
    package=
        safe_text,
    name=
        safe_text
)

@given(instance=RegExp_strategy)
@settings(max_examples=50)
def test_regexp_instantiation(instance):
    assert isinstance(instance, RegExp)

@given(instance=cal_RegExpTag_strategy)
@settings(max_examples=50)
def test_cal_regexptag_instantiation(instance):
    assert isinstance(instance, cal_RegExpTag)

@given(instance=cal_RegExpUnary_strategy)
@settings(max_examples=50)
def test_cal_regexpunary_instantiation(instance):
    assert isinstance(instance, cal_RegExpUnary)



@given(instance=cal_RegExpUnary_strategy)
def test_cal_regexpunary_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=cal_RegExpBinary_strategy)
@settings(max_examples=50)
def test_cal_regexpbinary_instantiation(instance):
    assert isinstance(instance, cal_RegExpBinary)



@given(instance=cal_RegExpBinary_strategy)
def test_cal_regexpbinary_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=cal_AnnotationArgument_strategy)
@settings(max_examples=50)
def test_cal_annotationargument_instantiation(instance):
    assert isinstance(instance, cal_AnnotationArgument)



@given(instance=cal_AnnotationArgument_strategy)
def test_cal_annotationargument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=cal_AnnotationArgument_strategy)
def test_cal_annotationargument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AstType_strategy)
@settings(max_examples=50)
def test_asttype_instantiation(instance):
    assert isinstance(instance, AstType)

@given(instance=cal_AstTypeUint_strategy)
@settings(max_examples=50)
def test_cal_asttypeuint_instantiation(instance):
    assert isinstance(instance, cal_AstTypeUint)

@given(instance=cal_AstTypeDouble_strategy)
@settings(max_examples=50)
def test_cal_asttypedouble_instantiation(instance):
    assert isinstance(instance, cal_AstTypeDouble)

@given(instance=cal_AstTypeFloat_strategy)
@settings(max_examples=50)
def test_cal_asttypefloat_instantiation(instance):
    assert isinstance(instance, cal_AstTypeFloat)

@given(instance=cal_AstTypeInt_strategy)
@settings(max_examples=50)
def test_cal_asttypeint_instantiation(instance):
    assert isinstance(instance, cal_AstTypeInt)

@given(instance=cal_AstTypeHalf_strategy)
@settings(max_examples=50)
def test_cal_asttypehalf_instantiation(instance):
    assert isinstance(instance, cal_AstTypeHalf)

@given(instance=cal_AstTypeString_strategy)
@settings(max_examples=50)
def test_cal_asttypestring_instantiation(instance):
    assert isinstance(instance, cal_AstTypeString)

@given(instance=cal_AstTypeBool_strategy)
@settings(max_examples=50)
def test_cal_asttypebool_instantiation(instance):
    assert isinstance(instance, cal_AstTypeBool)

@given(instance=ExpressionLiteral_strategy)
@settings(max_examples=50)
def test_expressionliteral_instantiation(instance):
    assert isinstance(instance, ExpressionLiteral)

@given(instance=cal_ExpressionInteger_strategy)
@settings(max_examples=50)
def test_cal_expressioninteger_instantiation(instance):
    assert isinstance(instance, cal_ExpressionInteger)



@given(instance=cal_ExpressionInteger_strategy)
def test_cal_expressioninteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_ExpressionString_strategy)
@settings(max_examples=50)
def test_cal_expressionstring_instantiation(instance):
    assert isinstance(instance, cal_ExpressionString)



@given(instance=cal_ExpressionString_strategy)
def test_cal_expressionstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_ExpressionFloat_strategy)
@settings(max_examples=50)
def test_cal_expressionfloat_instantiation(instance):
    assert isinstance(instance, cal_ExpressionFloat)



@given(instance=cal_ExpressionFloat_strategy)
def test_cal_expressionfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_ExpressionBoolean_strategy)
@settings(max_examples=50)
def test_cal_expressionboolean_instantiation(instance):
    assert isinstance(instance, cal_ExpressionBoolean)



@given(instance=cal_ExpressionBoolean_strategy)
def test_cal_expressionboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_Generator_strategy)
@settings(max_examples=50)
def test_cal_generator_instantiation(instance):
    assert isinstance(instance, cal_Generator)

@given(instance=cal_ExpressionElsif_strategy)
@settings(max_examples=50)
def test_cal_expressionelsif_instantiation(instance):
    assert isinstance(instance, cal_ExpressionElsif)

@given(instance=cal_AstTypeList_strategy)
@settings(max_examples=50)
def test_cal_asttypelist_instantiation(instance):
    assert isinstance(instance, cal_AstTypeList)

@given(instance=AstExpression_strategy)
@settings(max_examples=50)
def test_astexpression_instantiation(instance):
    assert isinstance(instance, AstExpression)

@given(instance=cal_ExpressionVariable_strategy)
@settings(max_examples=50)
def test_cal_expressionvariable_instantiation(instance):
    assert isinstance(instance, cal_ExpressionVariable)

@given(instance=cal_ExpressionBinary_strategy)
@settings(max_examples=50)
def test_cal_expressionbinary_instantiation(instance):
    assert isinstance(instance, cal_ExpressionBinary)



@given(instance=cal_ExpressionBinary_strategy)
def test_cal_expressionbinary_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=cal_ExpressionLiteral_strategy)
@settings(max_examples=50)
def test_cal_expressionliteral_instantiation(instance):
    assert isinstance(instance, cal_ExpressionLiteral)

@given(instance=cal_ExpressionUnary_strategy)
@settings(max_examples=50)
def test_cal_expressionunary_instantiation(instance):
    assert isinstance(instance, cal_ExpressionUnary)



@given(instance=cal_ExpressionUnary_strategy)
def test_cal_expressionunary_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=cal_ExpressionList_strategy)
@settings(max_examples=50)
def test_cal_expressionlist_instantiation(instance):
    assert isinstance(instance, cal_ExpressionList)

@given(instance=cal_ExpressionIndex_strategy)
@settings(max_examples=50)
def test_cal_expressionindex_instantiation(instance):
    assert isinstance(instance, cal_ExpressionIndex)

@given(instance=cal_ExpressionCall_strategy)
@settings(max_examples=50)
def test_cal_expressioncall_instantiation(instance):
    assert isinstance(instance, cal_ExpressionCall)

@given(instance=cal_StatementElsif_strategy)
@settings(max_examples=50)
def test_cal_statementelsif_instantiation(instance):
    assert isinstance(instance, cal_StatementElsif)

@given(instance=cal_ExpressionIf_strategy)
@settings(max_examples=50)
def test_cal_expressionif_instantiation(instance):
    assert isinstance(instance, cal_ExpressionIf)

@given(instance=cal_VariableReference_strategy)
@settings(max_examples=50)
def test_cal_variablereference_instantiation(instance):
    assert isinstance(instance, cal_VariableReference)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=cal_StatementWhile_strategy)
@settings(max_examples=50)
def test_cal_statementwhile_instantiation(instance):
    assert isinstance(instance, cal_StatementWhile)

@given(instance=cal_StatementIf_strategy)
@settings(max_examples=50)
def test_cal_statementif_instantiation(instance):
    assert isinstance(instance, cal_StatementIf)

@given(instance=cal_StatementCall_strategy)
@settings(max_examples=50)
def test_cal_statementcall_instantiation(instance):
    assert isinstance(instance, cal_StatementCall)

@given(instance=cal_StatementAssign_strategy)
@settings(max_examples=50)
def test_cal_statementassign_instantiation(instance):
    assert isinstance(instance, cal_StatementAssign)

@given(instance=cal_Guard_strategy)
@settings(max_examples=50)
def test_cal_guard_instantiation(instance):
    assert isinstance(instance, cal_Guard)

@given(instance=cal_OutputPattern_strategy)
@settings(max_examples=50)
def test_cal_outputpattern_instantiation(instance):
    assert isinstance(instance, cal_OutputPattern)

@given(instance=cal_InputPattern_strategy)
@settings(max_examples=50)
def test_cal_inputpattern_instantiation(instance):
    assert isinstance(instance, cal_InputPattern)

@given(instance=cal_StatementForeach_strategy)
@settings(max_examples=50)
def test_cal_statementforeach_instantiation(instance):
    assert isinstance(instance, cal_StatementForeach)

@given(instance=cal_ExternalTarget_strategy)
@settings(max_examples=50)
def test_cal_externaltarget_instantiation(instance):
    assert isinstance(instance, cal_ExternalTarget)

@given(instance=cal_AstTransition_strategy)
@settings(max_examples=50)
def test_cal_asttransition_instantiation(instance):
    assert isinstance(instance, cal_AstTransition)

@given(instance=cal_Fsm_strategy)
@settings(max_examples=50)
def test_cal_fsm_instantiation(instance):
    assert isinstance(instance, cal_Fsm)

@given(instance=cal_AstState_strategy)
@settings(max_examples=50)
def test_cal_aststate_instantiation(instance):
    assert isinstance(instance, cal_AstState)



@given(instance=cal_AstState_strategy)
def test_cal_aststate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cal_AstState_strategy)
def test_cal_aststate_node_setter(instance):
    original = instance.node
    instance.node = original
    assert instance.node == original

@given(instance=cal_Inequality_strategy)
@settings(max_examples=50)
def test_cal_inequality_instantiation(instance):
    assert isinstance(instance, cal_Inequality)

@given(instance=cal_AstTag_strategy)
@settings(max_examples=50)
def test_cal_asttag_instantiation(instance):
    assert isinstance(instance, cal_AstTag)



@given(instance=cal_AstTag_strategy)
def test_cal_asttag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=cal_Statement_strategy)
@settings(max_examples=50)
def test_cal_statement_instantiation(instance):
    assert isinstance(instance, cal_Statement)

@given(instance=cal_Priority_strategy)
@settings(max_examples=50)
def test_cal_priority_instantiation(instance):
    assert isinstance(instance, cal_Priority)

@given(instance=cal_RegExp_strategy)
@settings(max_examples=50)
def test_cal_regexp_instantiation(instance):
    assert isinstance(instance, cal_RegExp)

@given(instance=cal_ScheduleFsm_strategy)
@settings(max_examples=50)
def test_cal_schedulefsm_instantiation(instance):
    assert isinstance(instance, cal_ScheduleFsm)

@given(instance=cal_LocalFsm_strategy)
@settings(max_examples=50)
def test_cal_localfsm_instantiation(instance):
    assert isinstance(instance, cal_LocalFsm)



@given(instance=cal_LocalFsm_strategy)
def test_cal_localfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstAction_strategy)
@settings(max_examples=50)
def test_cal_astaction_instantiation(instance):
    assert isinstance(instance, cal_AstAction)

@given(instance=cal_AstPort_strategy)
@settings(max_examples=50)
def test_cal_astport_instantiation(instance):
    assert isinstance(instance, cal_AstPort)



@given(instance=cal_AstPort_strategy)
def test_cal_astport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstType_strategy)
@settings(max_examples=50)
def test_cal_asttype_instantiation(instance):
    assert isinstance(instance, cal_AstType)

@given(instance=cal_AstExpression_strategy)
@settings(max_examples=50)
def test_cal_astexpression_instantiation(instance):
    assert isinstance(instance, cal_AstExpression)

@given(instance=cal_Variable_strategy)
@settings(max_examples=50)
def test_cal_variable_instantiation(instance):
    assert isinstance(instance, cal_Variable)



@given(instance=cal_Variable_strategy)
def test_cal_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cal_Variable_strategy)
def test_cal_variable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=cal_AstProcedure_strategy)
@settings(max_examples=50)
def test_cal_astprocedure_instantiation(instance):
    assert isinstance(instance, cal_AstProcedure)



@given(instance=cal_AstProcedure_strategy)
def test_cal_astprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_Function_strategy)
@settings(max_examples=50)
def test_cal_function_instantiation(instance):
    assert isinstance(instance, cal_Function)



@given(instance=cal_Function_strategy)
def test_cal_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstUnit_strategy)
@settings(max_examples=50)
def test_cal_astunit_instantiation(instance):
    assert isinstance(instance, cal_AstUnit)

@given(instance=cal_AstActor_strategy)
@settings(max_examples=50)
def test_cal_astactor_instantiation(instance):
    assert isinstance(instance, cal_AstActor)

@given(instance=cal_AstAnnotation_strategy)
@settings(max_examples=50)
def test_cal_astannotation_instantiation(instance):
    assert isinstance(instance, cal_AstAnnotation)



@given(instance=cal_AstAnnotation_strategy)
def test_cal_astannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_Import_strategy)
@settings(max_examples=50)
def test_cal_import_instantiation(instance):
    assert isinstance(instance, cal_Import)



@given(instance=cal_Import_strategy)
def test_cal_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=cal_AstEntity_strategy)
@settings(max_examples=50)
def test_cal_astentity_instantiation(instance):
    assert isinstance(instance, cal_AstEntity)



@given(instance=cal_AstEntity_strategy)
def test_cal_astentity_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=cal_AstEntity_strategy)
def test_cal_astentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
