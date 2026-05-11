import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RegExp,
    cal::RegExpTag,
    cal::RegExpUnary,
    cal::RegExpBinary,
    cal::AnnotationArgument,
    AstType,
    cal::AstTypeFloat,
    cal::AstTypeUint,
    cal::AstTypeInt,
    cal::AstTypeDouble,
    cal::AstTypeString,
    cal::AstTypeHalf,
    cal::AstTypeBool,
    ExpressionLiteral,
    cal::ExpressionInteger,
    cal::ExpressionString,
    cal::ExpressionFloat,
    cal::ExpressionBoolean,
    cal::Generator,
    cal::ExpressionElsif,
    cal::AstTypeList,
    AstExpression,
    cal::ExpressionLiteral,
    cal::ExpressionVariable,
    cal::ExpressionList,
    cal::ExpressionUnary,
    cal::ExpressionBinary,
    cal::ExpressionIndex,
    cal::ExpressionCall,
    cal::StatementElsif,
    cal::ExpressionIf,
    cal::VariableReference,
    Statement,
    cal::StatementIf,
    cal::StatementCall,
    cal::StatementWhile,
    cal::StatementAssign,
    cal::Guard,
    cal::OutputPattern,
    cal::InputPattern,
    cal::StatementForeach,
    cal::ExternalTarget,
    cal::AstTransition,
    cal::Fsm,
    cal::AstState,
    cal::Inequality,
    cal::AstTag,
    cal::Statement,
    cal::Priority,
    cal::RegExp,
    cal::ScheduleFsm,
    cal::LocalFsm,
    cal::AstAction,
    cal::AstPort,
    cal::AstType,
    cal::AstExpression,
    cal::Variable,
    cal::AstProcedure,
    cal::Function,
    cal::AstUnit,
    cal::AstActor,
    cal::AstAnnotation,
    cal::Import,
    cal::AstEntity,
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



def test_cal::regexptag_is_not_abstract():
    assert not inspect.isabstract(cal::RegExpTag)


def test_cal::regexptag_constructor_exists():
    assert callable(cal::RegExpTag.__init__)


def test_cal::regexptag_constructor_args():
    sig = inspect.signature(cal::RegExpTag.__init__)
    params = list(sig.parameters.keys())



def test_cal::regexpunary_is_not_abstract():
    assert not inspect.isabstract(cal::RegExpUnary)


def test_cal::regexpunary_constructor_exists():
    assert callable(cal::RegExpUnary.__init__)


def test_cal::regexpunary_constructor_args():
    sig = inspect.signature(cal::RegExpUnary.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_cal::regexpunary_has_unaryOperator():
    assert hasattr(cal::RegExpUnary, "unaryOperator")
    descriptor = None
    for klass in cal::RegExpUnary.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_cal::regexpbinary_is_not_abstract():
    assert not inspect.isabstract(cal::RegExpBinary)


def test_cal::regexpbinary_constructor_exists():
    assert callable(cal::RegExpBinary.__init__)


def test_cal::regexpbinary_constructor_args():
    sig = inspect.signature(cal::RegExpBinary.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_cal::regexpbinary_has_operator():
    assert hasattr(cal::RegExpBinary, "operator")
    descriptor = None
    for klass in cal::RegExpBinary.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cal::annotationargument_is_not_abstract():
    assert not inspect.isabstract(cal::AnnotationArgument)


def test_cal::annotationargument_constructor_exists():
    assert callable(cal::AnnotationArgument.__init__)


def test_cal::annotationargument_constructor_args():
    sig = inspect.signature(cal::AnnotationArgument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_cal::annotationargument_has_name():
    assert hasattr(cal::AnnotationArgument, "name")
    descriptor = None
    for klass in cal::AnnotationArgument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cal::annotationargument_has_value():
    assert hasattr(cal::AnnotationArgument, "value")
    descriptor = None
    for klass in cal::AnnotationArgument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_asttype_is_not_abstract():
    assert not inspect.isabstract(AstType)


def test_asttype_constructor_exists():
    assert callable(AstType.__init__)


def test_asttype_constructor_args():
    sig = inspect.signature(AstType.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypefloat_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeFloat)


def test_cal::asttypefloat_constructor_exists():
    assert callable(cal::AstTypeFloat.__init__)


def test_cal::asttypefloat_constructor_args():
    sig = inspect.signature(cal::AstTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypeuint_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeUint)


def test_cal::asttypeuint_constructor_exists():
    assert callable(cal::AstTypeUint.__init__)


def test_cal::asttypeuint_constructor_args():
    sig = inspect.signature(cal::AstTypeUint.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypeint_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeInt)


def test_cal::asttypeint_constructor_exists():
    assert callable(cal::AstTypeInt.__init__)


def test_cal::asttypeint_constructor_args():
    sig = inspect.signature(cal::AstTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypedouble_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeDouble)


def test_cal::asttypedouble_constructor_exists():
    assert callable(cal::AstTypeDouble.__init__)


def test_cal::asttypedouble_constructor_args():
    sig = inspect.signature(cal::AstTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypestring_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeString)


def test_cal::asttypestring_constructor_exists():
    assert callable(cal::AstTypeString.__init__)


def test_cal::asttypestring_constructor_args():
    sig = inspect.signature(cal::AstTypeString.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypehalf_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeHalf)


def test_cal::asttypehalf_constructor_exists():
    assert callable(cal::AstTypeHalf.__init__)


def test_cal::asttypehalf_constructor_args():
    sig = inspect.signature(cal::AstTypeHalf.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypebool_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeBool)


def test_cal::asttypebool_constructor_exists():
    assert callable(cal::AstTypeBool.__init__)


def test_cal::asttypebool_constructor_args():
    sig = inspect.signature(cal::AstTypeBool.__init__)
    params = list(sig.parameters.keys())



def test_expressionliteral_is_not_abstract():
    assert not inspect.isabstract(ExpressionLiteral)


def test_expressionliteral_constructor_exists():
    assert callable(ExpressionLiteral.__init__)


def test_expressionliteral_constructor_args():
    sig = inspect.signature(ExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressioninteger_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionInteger)


def test_cal::expressioninteger_constructor_exists():
    assert callable(cal::ExpressionInteger.__init__)


def test_cal::expressioninteger_constructor_args():
    sig = inspect.signature(cal::ExpressionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::expressioninteger_has_value():
    assert hasattr(cal::ExpressionInteger, "value")
    descriptor = None
    for klass in cal::ExpressionInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::expressionstring_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionString)


def test_cal::expressionstring_constructor_exists():
    assert callable(cal::ExpressionString.__init__)


def test_cal::expressionstring_constructor_args():
    sig = inspect.signature(cal::ExpressionString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::expressionstring_has_value():
    assert hasattr(cal::ExpressionString, "value")
    descriptor = None
    for klass in cal::ExpressionString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::expressionfloat_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionFloat)


def test_cal::expressionfloat_constructor_exists():
    assert callable(cal::ExpressionFloat.__init__)


def test_cal::expressionfloat_constructor_args():
    sig = inspect.signature(cal::ExpressionFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::expressionfloat_has_value():
    assert hasattr(cal::ExpressionFloat, "value")
    descriptor = None
    for klass in cal::ExpressionFloat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::expressionboolean_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionBoolean)


def test_cal::expressionboolean_constructor_exists():
    assert callable(cal::ExpressionBoolean.__init__)


def test_cal::expressionboolean_constructor_args():
    sig = inspect.signature(cal::ExpressionBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::expressionboolean_has_value():
    assert hasattr(cal::ExpressionBoolean, "value")
    descriptor = None
    for klass in cal::ExpressionBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::generator_is_not_abstract():
    assert not inspect.isabstract(cal::Generator)


def test_cal::generator_constructor_exists():
    assert callable(cal::Generator.__init__)


def test_cal::generator_constructor_args():
    sig = inspect.signature(cal::Generator.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressionelsif_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionElsif)


def test_cal::expressionelsif_constructor_exists():
    assert callable(cal::ExpressionElsif.__init__)


def test_cal::expressionelsif_constructor_args():
    sig = inspect.signature(cal::ExpressionElsif.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypelist_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeList)


def test_cal::asttypelist_constructor_exists():
    assert callable(cal::AstTypeList.__init__)


def test_cal::asttypelist_constructor_args():
    sig = inspect.signature(cal::AstTypeList.__init__)
    params = list(sig.parameters.keys())



def test_astexpression_is_not_abstract():
    assert not inspect.isabstract(AstExpression)


def test_astexpression_constructor_exists():
    assert callable(AstExpression.__init__)


def test_astexpression_constructor_args():
    sig = inspect.signature(AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressionliteral_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionLiteral)


def test_cal::expressionliteral_constructor_exists():
    assert callable(cal::ExpressionLiteral.__init__)


def test_cal::expressionliteral_constructor_args():
    sig = inspect.signature(cal::ExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressionvariable_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionVariable)


def test_cal::expressionvariable_constructor_exists():
    assert callable(cal::ExpressionVariable.__init__)


def test_cal::expressionvariable_constructor_args():
    sig = inspect.signature(cal::ExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressionlist_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionList)


def test_cal::expressionlist_constructor_exists():
    assert callable(cal::ExpressionList.__init__)


def test_cal::expressionlist_constructor_args():
    sig = inspect.signature(cal::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressionunary_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionUnary)


def test_cal::expressionunary_constructor_exists():
    assert callable(cal::ExpressionUnary.__init__)


def test_cal::expressionunary_constructor_args():
    sig = inspect.signature(cal::ExpressionUnary.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_cal::expressionunary_has_unaryOperator():
    assert hasattr(cal::ExpressionUnary, "unaryOperator")
    descriptor = None
    for klass in cal::ExpressionUnary.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_cal::expressionbinary_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionBinary)


def test_cal::expressionbinary_constructor_exists():
    assert callable(cal::ExpressionBinary.__init__)


def test_cal::expressionbinary_constructor_args():
    sig = inspect.signature(cal::ExpressionBinary.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_cal::expressionbinary_has_operator():
    assert hasattr(cal::ExpressionBinary, "operator")
    descriptor = None
    for klass in cal::ExpressionBinary.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cal::expressionindex_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionIndex)


def test_cal::expressionindex_constructor_exists():
    assert callable(cal::ExpressionIndex.__init__)


def test_cal::expressionindex_constructor_args():
    sig = inspect.signature(cal::ExpressionIndex.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressioncall_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionCall)


def test_cal::expressioncall_constructor_exists():
    assert callable(cal::ExpressionCall.__init__)


def test_cal::expressioncall_constructor_args():
    sig = inspect.signature(cal::ExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_cal::statementelsif_is_not_abstract():
    assert not inspect.isabstract(cal::StatementElsif)


def test_cal::statementelsif_constructor_exists():
    assert callable(cal::StatementElsif.__init__)


def test_cal::statementelsif_constructor_args():
    sig = inspect.signature(cal::StatementElsif.__init__)
    params = list(sig.parameters.keys())



def test_cal::expressionif_is_not_abstract():
    assert not inspect.isabstract(cal::ExpressionIf)


def test_cal::expressionif_constructor_exists():
    assert callable(cal::ExpressionIf.__init__)


def test_cal::expressionif_constructor_args():
    sig = inspect.signature(cal::ExpressionIf.__init__)
    params = list(sig.parameters.keys())



def test_cal::variablereference_is_not_abstract():
    assert not inspect.isabstract(cal::VariableReference)


def test_cal::variablereference_constructor_exists():
    assert callable(cal::VariableReference.__init__)


def test_cal::variablereference_constructor_args():
    sig = inspect.signature(cal::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_cal::statementif_is_not_abstract():
    assert not inspect.isabstract(cal::StatementIf)


def test_cal::statementif_constructor_exists():
    assert callable(cal::StatementIf.__init__)


def test_cal::statementif_constructor_args():
    sig = inspect.signature(cal::StatementIf.__init__)
    params = list(sig.parameters.keys())



def test_cal::statementcall_is_not_abstract():
    assert not inspect.isabstract(cal::StatementCall)


def test_cal::statementcall_constructor_exists():
    assert callable(cal::StatementCall.__init__)


def test_cal::statementcall_constructor_args():
    sig = inspect.signature(cal::StatementCall.__init__)
    params = list(sig.parameters.keys())



def test_cal::statementwhile_is_not_abstract():
    assert not inspect.isabstract(cal::StatementWhile)


def test_cal::statementwhile_constructor_exists():
    assert callable(cal::StatementWhile.__init__)


def test_cal::statementwhile_constructor_args():
    sig = inspect.signature(cal::StatementWhile.__init__)
    params = list(sig.parameters.keys())



def test_cal::statementassign_is_not_abstract():
    assert not inspect.isabstract(cal::StatementAssign)


def test_cal::statementassign_constructor_exists():
    assert callable(cal::StatementAssign.__init__)


def test_cal::statementassign_constructor_args():
    sig = inspect.signature(cal::StatementAssign.__init__)
    params = list(sig.parameters.keys())



def test_cal::guard_is_not_abstract():
    assert not inspect.isabstract(cal::Guard)


def test_cal::guard_constructor_exists():
    assert callable(cal::Guard.__init__)


def test_cal::guard_constructor_args():
    sig = inspect.signature(cal::Guard.__init__)
    params = list(sig.parameters.keys())



def test_cal::outputpattern_is_not_abstract():
    assert not inspect.isabstract(cal::OutputPattern)


def test_cal::outputpattern_constructor_exists():
    assert callable(cal::OutputPattern.__init__)


def test_cal::outputpattern_constructor_args():
    sig = inspect.signature(cal::OutputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal::inputpattern_is_not_abstract():
    assert not inspect.isabstract(cal::InputPattern)


def test_cal::inputpattern_constructor_exists():
    assert callable(cal::InputPattern.__init__)


def test_cal::inputpattern_constructor_args():
    sig = inspect.signature(cal::InputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal::statementforeach_is_not_abstract():
    assert not inspect.isabstract(cal::StatementForeach)


def test_cal::statementforeach_constructor_exists():
    assert callable(cal::StatementForeach.__init__)


def test_cal::statementforeach_constructor_args():
    sig = inspect.signature(cal::StatementForeach.__init__)
    params = list(sig.parameters.keys())



def test_cal::externaltarget_is_not_abstract():
    assert not inspect.isabstract(cal::ExternalTarget)


def test_cal::externaltarget_constructor_exists():
    assert callable(cal::ExternalTarget.__init__)


def test_cal::externaltarget_constructor_args():
    sig = inspect.signature(cal::ExternalTarget.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttransition_is_not_abstract():
    assert not inspect.isabstract(cal::AstTransition)


def test_cal::asttransition_constructor_exists():
    assert callable(cal::AstTransition.__init__)


def test_cal::asttransition_constructor_args():
    sig = inspect.signature(cal::AstTransition.__init__)
    params = list(sig.parameters.keys())



def test_cal::fsm_is_not_abstract():
    assert not inspect.isabstract(cal::Fsm)


def test_cal::fsm_constructor_exists():
    assert callable(cal::Fsm.__init__)


def test_cal::fsm_constructor_args():
    sig = inspect.signature(cal::Fsm.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststate_is_not_abstract():
    assert not inspect.isabstract(cal::AstState)


def test_cal::aststate_constructor_exists():
    assert callable(cal::AstState.__init__)


def test_cal::aststate_constructor_args():
    sig = inspect.signature(cal::AstState.__init__)
    params = list(sig.parameters.keys())
    assert "node" in params, "Missing parameter 'node'"
    assert "name" in params, "Missing parameter 'name'"

def test_cal::aststate_has_node():
    assert hasattr(cal::AstState, "node")
    descriptor = None
    for klass in cal::AstState.__mro__:
        if "node" in klass.__dict__:
            descriptor = klass.__dict__["node"]
            break
    assert isinstance(descriptor, property)

def test_cal::aststate_has_name():
    assert hasattr(cal::AstState, "name")
    descriptor = None
    for klass in cal::AstState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::inequality_is_not_abstract():
    assert not inspect.isabstract(cal::Inequality)


def test_cal::inequality_constructor_exists():
    assert callable(cal::Inequality.__init__)


def test_cal::inequality_constructor_args():
    sig = inspect.signature(cal::Inequality.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttag_is_not_abstract():
    assert not inspect.isabstract(cal::AstTag)


def test_cal::asttag_constructor_exists():
    assert callable(cal::AstTag.__init__)


def test_cal::asttag_constructor_args():
    sig = inspect.signature(cal::AstTag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"

def test_cal::asttag_has_identifiers():
    assert hasattr(cal::AstTag, "identifiers")
    descriptor = None
    for klass in cal::AstTag.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)



def test_cal::statement_is_not_abstract():
    assert not inspect.isabstract(cal::Statement)


def test_cal::statement_constructor_exists():
    assert callable(cal::Statement.__init__)


def test_cal::statement_constructor_args():
    sig = inspect.signature(cal::Statement.__init__)
    params = list(sig.parameters.keys())



def test_cal::priority_is_not_abstract():
    assert not inspect.isabstract(cal::Priority)


def test_cal::priority_constructor_exists():
    assert callable(cal::Priority.__init__)


def test_cal::priority_constructor_args():
    sig = inspect.signature(cal::Priority.__init__)
    params = list(sig.parameters.keys())



def test_cal::regexp_is_not_abstract():
    assert not inspect.isabstract(cal::RegExp)


def test_cal::regexp_constructor_exists():
    assert callable(cal::RegExp.__init__)


def test_cal::regexp_constructor_args():
    sig = inspect.signature(cal::RegExp.__init__)
    params = list(sig.parameters.keys())



def test_cal::schedulefsm_is_not_abstract():
    assert not inspect.isabstract(cal::ScheduleFsm)


def test_cal::schedulefsm_constructor_exists():
    assert callable(cal::ScheduleFsm.__init__)


def test_cal::schedulefsm_constructor_args():
    sig = inspect.signature(cal::ScheduleFsm.__init__)
    params = list(sig.parameters.keys())



def test_cal::localfsm_is_not_abstract():
    assert not inspect.isabstract(cal::LocalFsm)


def test_cal::localfsm_constructor_exists():
    assert callable(cal::LocalFsm.__init__)


def test_cal::localfsm_constructor_args():
    sig = inspect.signature(cal::LocalFsm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::localfsm_has_name():
    assert hasattr(cal::LocalFsm, "name")
    descriptor = None
    for klass in cal::LocalFsm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astaction_is_not_abstract():
    assert not inspect.isabstract(cal::AstAction)


def test_cal::astaction_constructor_exists():
    assert callable(cal::AstAction.__init__)


def test_cal::astaction_constructor_args():
    sig = inspect.signature(cal::AstAction.__init__)
    params = list(sig.parameters.keys())



def test_cal::astport_is_not_abstract():
    assert not inspect.isabstract(cal::AstPort)


def test_cal::astport_constructor_exists():
    assert callable(cal::AstPort.__init__)


def test_cal::astport_constructor_args():
    sig = inspect.signature(cal::AstPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astport_has_name():
    assert hasattr(cal::AstPort, "name")
    descriptor = None
    for klass in cal::AstPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::asttype_is_not_abstract():
    assert not inspect.isabstract(cal::AstType)


def test_cal::asttype_constructor_exists():
    assert callable(cal::AstType.__init__)


def test_cal::asttype_constructor_args():
    sig = inspect.signature(cal::AstType.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpression_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpression)


def test_cal::astexpression_constructor_exists():
    assert callable(cal::AstExpression.__init__)


def test_cal::astexpression_constructor_args():
    sig = inspect.signature(cal::AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal::variable_is_not_abstract():
    assert not inspect.isabstract(cal::Variable)


def test_cal::variable_constructor_exists():
    assert callable(cal::Variable.__init__)


def test_cal::variable_constructor_args():
    sig = inspect.signature(cal::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "name" in params, "Missing parameter 'name'"

def test_cal::variable_has_constant():
    assert hasattr(cal::Variable, "constant")
    descriptor = None
    for klass in cal::Variable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_cal::variable_has_name():
    assert hasattr(cal::Variable, "name")
    descriptor = None
    for klass in cal::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astprocedure_is_not_abstract():
    assert not inspect.isabstract(cal::AstProcedure)


def test_cal::astprocedure_constructor_exists():
    assert callable(cal::AstProcedure.__init__)


def test_cal::astprocedure_constructor_args():
    sig = inspect.signature(cal::AstProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astprocedure_has_name():
    assert hasattr(cal::AstProcedure, "name")
    descriptor = None
    for klass in cal::AstProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::function_is_not_abstract():
    assert not inspect.isabstract(cal::Function)


def test_cal::function_constructor_exists():
    assert callable(cal::Function.__init__)


def test_cal::function_constructor_args():
    sig = inspect.signature(cal::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::function_has_name():
    assert hasattr(cal::Function, "name")
    descriptor = None
    for klass in cal::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astunit_is_not_abstract():
    assert not inspect.isabstract(cal::AstUnit)


def test_cal::astunit_constructor_exists():
    assert callable(cal::AstUnit.__init__)


def test_cal::astunit_constructor_args():
    sig = inspect.signature(cal::AstUnit.__init__)
    params = list(sig.parameters.keys())



def test_cal::astactor_is_not_abstract():
    assert not inspect.isabstract(cal::AstActor)


def test_cal::astactor_constructor_exists():
    assert callable(cal::AstActor.__init__)


def test_cal::astactor_constructor_args():
    sig = inspect.signature(cal::AstActor.__init__)
    params = list(sig.parameters.keys())



def test_cal::astannotation_is_not_abstract():
    assert not inspect.isabstract(cal::AstAnnotation)


def test_cal::astannotation_constructor_exists():
    assert callable(cal::AstAnnotation.__init__)


def test_cal::astannotation_constructor_args():
    sig = inspect.signature(cal::AstAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astannotation_has_name():
    assert hasattr(cal::AstAnnotation, "name")
    descriptor = None
    for klass in cal::AstAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::import_is_not_abstract():
    assert not inspect.isabstract(cal::Import)


def test_cal::import_constructor_exists():
    assert callable(cal::Import.__init__)


def test_cal::import_constructor_args():
    sig = inspect.signature(cal::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_cal::import_has_importedNamespace():
    assert hasattr(cal::Import, "importedNamespace")
    descriptor = None
    for klass in cal::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_cal::astentity_is_not_abstract():
    assert not inspect.isabstract(cal::AstEntity)


def test_cal::astentity_constructor_exists():
    assert callable(cal::AstEntity.__init__)


def test_cal::astentity_constructor_args():
    sig = inspect.signature(cal::AstEntity.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astentity_has_package():
    assert hasattr(cal::AstEntity, "package")
    descriptor = None
    for klass in cal::AstEntity.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_cal::astentity_has_name():
    assert hasattr(cal::AstEntity, "name")
    descriptor = None
    for klass in cal::AstEntity.__mro__:
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
cal::RegExpTag_strategy = st.builds(
    cal::RegExpTag,
)
cal::RegExpUnary_strategy = st.builds(
    cal::RegExpUnary,
    unaryOperator=
        safe_text
)
cal::RegExpBinary_strategy = st.builds(
    cal::RegExpBinary,
    operator=
        safe_text
)
cal::AnnotationArgument_strategy = st.builds(
    cal::AnnotationArgument,
    name=
        safe_text,
    value=
        safe_text
)
AstType_strategy = st.builds(
    AstType,
)
cal::AstTypeFloat_strategy = st.builds(
    cal::AstTypeFloat,
)
cal::AstTypeUint_strategy = st.builds(
    cal::AstTypeUint,
)
cal::AstTypeInt_strategy = st.builds(
    cal::AstTypeInt,
)
cal::AstTypeDouble_strategy = st.builds(
    cal::AstTypeDouble,
)
cal::AstTypeString_strategy = st.builds(
    cal::AstTypeString,
)
cal::AstTypeHalf_strategy = st.builds(
    cal::AstTypeHalf,
)
cal::AstTypeBool_strategy = st.builds(
    cal::AstTypeBool,
)
ExpressionLiteral_strategy = st.builds(
    ExpressionLiteral,
)
cal::ExpressionInteger_strategy = st.builds(
    cal::ExpressionInteger,
    value=
        safe_text
)
cal::ExpressionString_strategy = st.builds(
    cal::ExpressionString,
    value=
        safe_text
)
cal::ExpressionFloat_strategy = st.builds(
    cal::ExpressionFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cal::ExpressionBoolean_strategy = st.builds(
    cal::ExpressionBoolean,
    value=
        st.booleans()
)
cal::Generator_strategy = st.builds(
    cal::Generator,
)
cal::ExpressionElsif_strategy = st.builds(
    cal::ExpressionElsif,
)
cal::AstTypeList_strategy = st.builds(
    cal::AstTypeList,
)
AstExpression_strategy = st.builds(
    AstExpression,
)
cal::ExpressionLiteral_strategy = st.builds(
    cal::ExpressionLiteral,
)
cal::ExpressionVariable_strategy = st.builds(
    cal::ExpressionVariable,
)
cal::ExpressionList_strategy = st.builds(
    cal::ExpressionList,
)
cal::ExpressionUnary_strategy = st.builds(
    cal::ExpressionUnary,
    unaryOperator=
        safe_text
)
cal::ExpressionBinary_strategy = st.builds(
    cal::ExpressionBinary,
    operator=
        safe_text
)
cal::ExpressionIndex_strategy = st.builds(
    cal::ExpressionIndex,
)
cal::ExpressionCall_strategy = st.builds(
    cal::ExpressionCall,
)
cal::StatementElsif_strategy = st.builds(
    cal::StatementElsif,
)
cal::ExpressionIf_strategy = st.builds(
    cal::ExpressionIf,
)
cal::VariableReference_strategy = st.builds(
    cal::VariableReference,
)
Statement_strategy = st.builds(
    Statement,
)
cal::StatementIf_strategy = st.builds(
    cal::StatementIf,
)
cal::StatementCall_strategy = st.builds(
    cal::StatementCall,
)
cal::StatementWhile_strategy = st.builds(
    cal::StatementWhile,
)
cal::StatementAssign_strategy = st.builds(
    cal::StatementAssign,
)
cal::Guard_strategy = st.builds(
    cal::Guard,
)
cal::OutputPattern_strategy = st.builds(
    cal::OutputPattern,
)
cal::InputPattern_strategy = st.builds(
    cal::InputPattern,
)
cal::StatementForeach_strategy = st.builds(
    cal::StatementForeach,
)
cal::ExternalTarget_strategy = st.builds(
    cal::ExternalTarget,
)
cal::AstTransition_strategy = st.builds(
    cal::AstTransition,
)
cal::Fsm_strategy = st.builds(
    cal::Fsm,
)
cal::AstState_strategy = st.builds(
    cal::AstState,
    node=
        safe_text,
    name=
        safe_text
)
cal::Inequality_strategy = st.builds(
    cal::Inequality,
)
cal::AstTag_strategy = st.builds(
    cal::AstTag,
    identifiers=
        safe_text
)
cal::Statement_strategy = st.builds(
    cal::Statement,
)
cal::Priority_strategy = st.builds(
    cal::Priority,
)
cal::RegExp_strategy = st.builds(
    cal::RegExp,
)
cal::ScheduleFsm_strategy = st.builds(
    cal::ScheduleFsm,
)
cal::LocalFsm_strategy = st.builds(
    cal::LocalFsm,
    name=
        safe_text
)
cal::AstAction_strategy = st.builds(
    cal::AstAction,
)
cal::AstPort_strategy = st.builds(
    cal::AstPort,
    name=
        safe_text
)
cal::AstType_strategy = st.builds(
    cal::AstType,
)
cal::AstExpression_strategy = st.builds(
    cal::AstExpression,
)
cal::Variable_strategy = st.builds(
    cal::Variable,
    constant=
        st.booleans(),
    name=
        safe_text
)
cal::AstProcedure_strategy = st.builds(
    cal::AstProcedure,
    name=
        safe_text
)
cal::Function_strategy = st.builds(
    cal::Function,
    name=
        safe_text
)
cal::AstUnit_strategy = st.builds(
    cal::AstUnit,
)
cal::AstActor_strategy = st.builds(
    cal::AstActor,
)
cal::AstAnnotation_strategy = st.builds(
    cal::AstAnnotation,
    name=
        safe_text
)
cal::Import_strategy = st.builds(
    cal::Import,
    importedNamespace=
        safe_text
)
cal::AstEntity_strategy = st.builds(
    cal::AstEntity,
    package=
        safe_text,
    name=
        safe_text
)

@given(instance=RegExp_strategy)
@settings(max_examples=50)
def test_regexp_instantiation(instance):
    assert isinstance(instance, RegExp)

@given(instance=cal::RegExpTag_strategy)
@settings(max_examples=50)
def test_cal::regexptag_instantiation(instance):
    assert isinstance(instance, cal::RegExpTag)

@given(instance=cal::RegExpUnary_strategy)
@settings(max_examples=50)
def test_cal::regexpunary_instantiation(instance):
    assert isinstance(instance, cal::RegExpUnary)

@given(instance=cal::RegExpUnary_strategy)
def test_cal::regexpunary_unaryOperator_type(instance):
    assert isinstance(instance.unaryOperator, str)


@given(instance=cal::RegExpUnary_strategy)
def test_cal::regexpunary_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=cal::RegExpBinary_strategy)
@settings(max_examples=50)
def test_cal::regexpbinary_instantiation(instance):
    assert isinstance(instance, cal::RegExpBinary)

@given(instance=cal::RegExpBinary_strategy)
def test_cal::regexpbinary_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=cal::RegExpBinary_strategy)
def test_cal::regexpbinary_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=cal::AnnotationArgument_strategy)
@settings(max_examples=50)
def test_cal::annotationargument_instantiation(instance):
    assert isinstance(instance, cal::AnnotationArgument)

@given(instance=cal::AnnotationArgument_strategy)
def test_cal::annotationargument_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AnnotationArgument_strategy)
def test_cal::annotationargument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AnnotationArgument_strategy)
def test_cal::annotationargument_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cal::AnnotationArgument_strategy)
def test_cal::annotationargument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AstType_strategy)
@settings(max_examples=50)
def test_asttype_instantiation(instance):
    assert isinstance(instance, AstType)

@given(instance=cal::AstTypeFloat_strategy)
@settings(max_examples=50)
def test_cal::asttypefloat_instantiation(instance):
    assert isinstance(instance, cal::AstTypeFloat)

@given(instance=cal::AstTypeUint_strategy)
@settings(max_examples=50)
def test_cal::asttypeuint_instantiation(instance):
    assert isinstance(instance, cal::AstTypeUint)

@given(instance=cal::AstTypeInt_strategy)
@settings(max_examples=50)
def test_cal::asttypeint_instantiation(instance):
    assert isinstance(instance, cal::AstTypeInt)

@given(instance=cal::AstTypeDouble_strategy)
@settings(max_examples=50)
def test_cal::asttypedouble_instantiation(instance):
    assert isinstance(instance, cal::AstTypeDouble)

@given(instance=cal::AstTypeString_strategy)
@settings(max_examples=50)
def test_cal::asttypestring_instantiation(instance):
    assert isinstance(instance, cal::AstTypeString)

@given(instance=cal::AstTypeHalf_strategy)
@settings(max_examples=50)
def test_cal::asttypehalf_instantiation(instance):
    assert isinstance(instance, cal::AstTypeHalf)

@given(instance=cal::AstTypeBool_strategy)
@settings(max_examples=50)
def test_cal::asttypebool_instantiation(instance):
    assert isinstance(instance, cal::AstTypeBool)

@given(instance=ExpressionLiteral_strategy)
@settings(max_examples=50)
def test_expressionliteral_instantiation(instance):
    assert isinstance(instance, ExpressionLiteral)

@given(instance=cal::ExpressionInteger_strategy)
@settings(max_examples=50)
def test_cal::expressioninteger_instantiation(instance):
    assert isinstance(instance, cal::ExpressionInteger)

@given(instance=cal::ExpressionInteger_strategy)
def test_cal::expressioninteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cal::ExpressionInteger_strategy)
def test_cal::expressioninteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::ExpressionString_strategy)
@settings(max_examples=50)
def test_cal::expressionstring_instantiation(instance):
    assert isinstance(instance, cal::ExpressionString)

@given(instance=cal::ExpressionString_strategy)
def test_cal::expressionstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cal::ExpressionString_strategy)
def test_cal::expressionstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::ExpressionFloat_strategy)
@settings(max_examples=50)
def test_cal::expressionfloat_instantiation(instance):
    assert isinstance(instance, cal::ExpressionFloat)

@given(instance=cal::ExpressionFloat_strategy)
def test_cal::expressionfloat_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=cal::ExpressionFloat_strategy)
def test_cal::expressionfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::ExpressionBoolean_strategy)
@settings(max_examples=50)
def test_cal::expressionboolean_instantiation(instance):
    assert isinstance(instance, cal::ExpressionBoolean)

@given(instance=cal::ExpressionBoolean_strategy)
def test_cal::expressionboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=cal::ExpressionBoolean_strategy)
def test_cal::expressionboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::Generator_strategy)
@settings(max_examples=50)
def test_cal::generator_instantiation(instance):
    assert isinstance(instance, cal::Generator)

@given(instance=cal::ExpressionElsif_strategy)
@settings(max_examples=50)
def test_cal::expressionelsif_instantiation(instance):
    assert isinstance(instance, cal::ExpressionElsif)

@given(instance=cal::AstTypeList_strategy)
@settings(max_examples=50)
def test_cal::asttypelist_instantiation(instance):
    assert isinstance(instance, cal::AstTypeList)

@given(instance=AstExpression_strategy)
@settings(max_examples=50)
def test_astexpression_instantiation(instance):
    assert isinstance(instance, AstExpression)

@given(instance=cal::ExpressionLiteral_strategy)
@settings(max_examples=50)
def test_cal::expressionliteral_instantiation(instance):
    assert isinstance(instance, cal::ExpressionLiteral)

@given(instance=cal::ExpressionVariable_strategy)
@settings(max_examples=50)
def test_cal::expressionvariable_instantiation(instance):
    assert isinstance(instance, cal::ExpressionVariable)

@given(instance=cal::ExpressionList_strategy)
@settings(max_examples=50)
def test_cal::expressionlist_instantiation(instance):
    assert isinstance(instance, cal::ExpressionList)

@given(instance=cal::ExpressionUnary_strategy)
@settings(max_examples=50)
def test_cal::expressionunary_instantiation(instance):
    assert isinstance(instance, cal::ExpressionUnary)

@given(instance=cal::ExpressionUnary_strategy)
def test_cal::expressionunary_unaryOperator_type(instance):
    assert isinstance(instance.unaryOperator, str)


@given(instance=cal::ExpressionUnary_strategy)
def test_cal::expressionunary_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=cal::ExpressionBinary_strategy)
@settings(max_examples=50)
def test_cal::expressionbinary_instantiation(instance):
    assert isinstance(instance, cal::ExpressionBinary)

@given(instance=cal::ExpressionBinary_strategy)
def test_cal::expressionbinary_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=cal::ExpressionBinary_strategy)
def test_cal::expressionbinary_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=cal::ExpressionIndex_strategy)
@settings(max_examples=50)
def test_cal::expressionindex_instantiation(instance):
    assert isinstance(instance, cal::ExpressionIndex)

@given(instance=cal::ExpressionCall_strategy)
@settings(max_examples=50)
def test_cal::expressioncall_instantiation(instance):
    assert isinstance(instance, cal::ExpressionCall)

@given(instance=cal::StatementElsif_strategy)
@settings(max_examples=50)
def test_cal::statementelsif_instantiation(instance):
    assert isinstance(instance, cal::StatementElsif)

@given(instance=cal::ExpressionIf_strategy)
@settings(max_examples=50)
def test_cal::expressionif_instantiation(instance):
    assert isinstance(instance, cal::ExpressionIf)

@given(instance=cal::VariableReference_strategy)
@settings(max_examples=50)
def test_cal::variablereference_instantiation(instance):
    assert isinstance(instance, cal::VariableReference)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=cal::StatementIf_strategy)
@settings(max_examples=50)
def test_cal::statementif_instantiation(instance):
    assert isinstance(instance, cal::StatementIf)

@given(instance=cal::StatementCall_strategy)
@settings(max_examples=50)
def test_cal::statementcall_instantiation(instance):
    assert isinstance(instance, cal::StatementCall)

@given(instance=cal::StatementWhile_strategy)
@settings(max_examples=50)
def test_cal::statementwhile_instantiation(instance):
    assert isinstance(instance, cal::StatementWhile)

@given(instance=cal::StatementAssign_strategy)
@settings(max_examples=50)
def test_cal::statementassign_instantiation(instance):
    assert isinstance(instance, cal::StatementAssign)

@given(instance=cal::Guard_strategy)
@settings(max_examples=50)
def test_cal::guard_instantiation(instance):
    assert isinstance(instance, cal::Guard)

@given(instance=cal::OutputPattern_strategy)
@settings(max_examples=50)
def test_cal::outputpattern_instantiation(instance):
    assert isinstance(instance, cal::OutputPattern)

@given(instance=cal::InputPattern_strategy)
@settings(max_examples=50)
def test_cal::inputpattern_instantiation(instance):
    assert isinstance(instance, cal::InputPattern)

@given(instance=cal::StatementForeach_strategy)
@settings(max_examples=50)
def test_cal::statementforeach_instantiation(instance):
    assert isinstance(instance, cal::StatementForeach)

@given(instance=cal::ExternalTarget_strategy)
@settings(max_examples=50)
def test_cal::externaltarget_instantiation(instance):
    assert isinstance(instance, cal::ExternalTarget)

@given(instance=cal::AstTransition_strategy)
@settings(max_examples=50)
def test_cal::asttransition_instantiation(instance):
    assert isinstance(instance, cal::AstTransition)

@given(instance=cal::Fsm_strategy)
@settings(max_examples=50)
def test_cal::fsm_instantiation(instance):
    assert isinstance(instance, cal::Fsm)

@given(instance=cal::AstState_strategy)
@settings(max_examples=50)
def test_cal::aststate_instantiation(instance):
    assert isinstance(instance, cal::AstState)

@given(instance=cal::AstState_strategy)
def test_cal::aststate_node_type(instance):
    assert isinstance(instance.node, str)


@given(instance=cal::AstState_strategy)
def test_cal::aststate_node_setter(instance):
    original = instance.node
    instance.node = original
    assert instance.node == original

@given(instance=cal::AstState_strategy)
def test_cal::aststate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstState_strategy)
def test_cal::aststate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::Inequality_strategy)
@settings(max_examples=50)
def test_cal::inequality_instantiation(instance):
    assert isinstance(instance, cal::Inequality)

@given(instance=cal::AstTag_strategy)
@settings(max_examples=50)
def test_cal::asttag_instantiation(instance):
    assert isinstance(instance, cal::AstTag)

@given(instance=cal::AstTag_strategy)
def test_cal::asttag_identifiers_type(instance):
    assert isinstance(instance.identifiers, str)


@given(instance=cal::AstTag_strategy)
def test_cal::asttag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=cal::Statement_strategy)
@settings(max_examples=50)
def test_cal::statement_instantiation(instance):
    assert isinstance(instance, cal::Statement)

@given(instance=cal::Priority_strategy)
@settings(max_examples=50)
def test_cal::priority_instantiation(instance):
    assert isinstance(instance, cal::Priority)

@given(instance=cal::RegExp_strategy)
@settings(max_examples=50)
def test_cal::regexp_instantiation(instance):
    assert isinstance(instance, cal::RegExp)

@given(instance=cal::ScheduleFsm_strategy)
@settings(max_examples=50)
def test_cal::schedulefsm_instantiation(instance):
    assert isinstance(instance, cal::ScheduleFsm)

@given(instance=cal::LocalFsm_strategy)
@settings(max_examples=50)
def test_cal::localfsm_instantiation(instance):
    assert isinstance(instance, cal::LocalFsm)

@given(instance=cal::LocalFsm_strategy)
def test_cal::localfsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::LocalFsm_strategy)
def test_cal::localfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstAction_strategy)
@settings(max_examples=50)
def test_cal::astaction_instantiation(instance):
    assert isinstance(instance, cal::AstAction)

@given(instance=cal::AstPort_strategy)
@settings(max_examples=50)
def test_cal::astport_instantiation(instance):
    assert isinstance(instance, cal::AstPort)

@given(instance=cal::AstPort_strategy)
def test_cal::astport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstPort_strategy)
def test_cal::astport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstType_strategy)
@settings(max_examples=50)
def test_cal::asttype_instantiation(instance):
    assert isinstance(instance, cal::AstType)

@given(instance=cal::AstExpression_strategy)
@settings(max_examples=50)
def test_cal::astexpression_instantiation(instance):
    assert isinstance(instance, cal::AstExpression)

@given(instance=cal::Variable_strategy)
@settings(max_examples=50)
def test_cal::variable_instantiation(instance):
    assert isinstance(instance, cal::Variable)

@given(instance=cal::Variable_strategy)
def test_cal::variable_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=cal::Variable_strategy)
def test_cal::variable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=cal::Variable_strategy)
def test_cal::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::Variable_strategy)
def test_cal::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstProcedure_strategy)
@settings(max_examples=50)
def test_cal::astprocedure_instantiation(instance):
    assert isinstance(instance, cal::AstProcedure)

@given(instance=cal::AstProcedure_strategy)
def test_cal::astprocedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstProcedure_strategy)
def test_cal::astprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::Function_strategy)
@settings(max_examples=50)
def test_cal::function_instantiation(instance):
    assert isinstance(instance, cal::Function)

@given(instance=cal::Function_strategy)
def test_cal::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::Function_strategy)
def test_cal::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstUnit_strategy)
@settings(max_examples=50)
def test_cal::astunit_instantiation(instance):
    assert isinstance(instance, cal::AstUnit)

@given(instance=cal::AstActor_strategy)
@settings(max_examples=50)
def test_cal::astactor_instantiation(instance):
    assert isinstance(instance, cal::AstActor)

@given(instance=cal::AstAnnotation_strategy)
@settings(max_examples=50)
def test_cal::astannotation_instantiation(instance):
    assert isinstance(instance, cal::AstAnnotation)

@given(instance=cal::AstAnnotation_strategy)
def test_cal::astannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstAnnotation_strategy)
def test_cal::astannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::Import_strategy)
@settings(max_examples=50)
def test_cal::import_instantiation(instance):
    assert isinstance(instance, cal::Import)

@given(instance=cal::Import_strategy)
def test_cal::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=cal::Import_strategy)
def test_cal::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=cal::AstEntity_strategy)
@settings(max_examples=50)
def test_cal::astentity_instantiation(instance):
    assert isinstance(instance, cal::AstEntity)

@given(instance=cal::AstEntity_strategy)
def test_cal::astentity_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=cal::AstEntity_strategy)
def test_cal::astentity_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=cal::AstEntity_strategy)
def test_cal::astentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstEntity_strategy)
def test_cal::astentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
