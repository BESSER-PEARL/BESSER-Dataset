import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MOFScriptObject,
    MOFScriptModel_MOFScriptStatementOwner,
    MOFScriptModel_MOFScriptParameter,
    MOFScriptModel_MOFScriptTransformation,
    MOFScriptStatementOwner,
    MOFScriptModel_MOFScriptStatement,
    MOFScriptModel_TransformationRule,
    Trace,
    MOFScriptModel_M2MTrace,
    MOFScriptModel_PointCutExpression,
    MOFScriptModel_CreateExpressionParameter,
    MOFScriptModel_PointCut,
    MOFScriptModel_Advice,
    MOFScriptTransformation,
    MOFScriptModel_MOFScriptAspect,
    MOFScriptModel_MOFScriptSpecification,
    SimpleExpression,
    MOFScriptModel_FunctionCall,
    ValueExpression,
    MOFScriptModel_SelectExpression,
    MOFScriptModel_ArithmeticExpression,
    MOFScriptModel_Reference,
    MOFScriptModel_Literal,
    MOFScriptModel_MOFScriptImport,
    MOFScriptModel_SimpleExpression,
    MOFScriptStatement,
    MOFScriptModel_PrintStatement,
    MOFScriptModel_CreateStatement,
    MOFScriptModel_DebugStatement,
    MOFScriptModel_IfStatement,
    MOFScriptModel_VariableDeclarationStatement,
    MOFScriptModel_FileStatement,
    MOFScriptModel_FunctionCallStatement,
    MOFScriptModel_ResultAssignment,
    MOFScriptModel_ReturnStatement,
    MOFScriptModel_GeneralAssignment,
    MOFScriptModel_WhileStatement,
    MOFScriptModel_Trace,
    MOFScriptModel_BreakStatement,
    MOFScriptModel_IteratorStatement,
    MOFScriptModel_MOFScriptObject,
    MOFScriptModel_StatementBlock,
    MOFScriptModel_VariableDeclaration,
    Expression,
    MOFScriptModel_LogicalExpression,
    MOFScriptModel_ComparisonExpression,
    MOFScriptModel_CreateExpression,
    MOFScriptModel_ValueExpression,
    MOFScriptModel_Expression,
    MOFScriptModel_MOFScriptComment,
    ImportSemantics,
    PointCutOperator,
    LogicalOperator,
    LiteralType,
    ParameterDirection,
    AssignmentOperator,
    AccessLevel,
    ComparisonOperator,
    AdviceOperator,
    ImportType,
    PointCutCombinationOperator,
    ArithmeticOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mofscriptobject_is_not_abstract():
    assert not inspect.isabstract(MOFScriptObject)


def test_mofscriptobject_constructor_exists():
    assert callable(MOFScriptObject.__init__)


def test_mofscriptobject_constructor_args():
    sig = inspect.signature(MOFScriptObject.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_mofscriptstatementowner_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptStatementOwner)


def test_mofscriptmodel_mofscriptstatementowner_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptStatementOwner.__init__)


def test_mofscriptmodel_mofscriptstatementowner_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptStatementOwner.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_mofscriptparameter_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptParameter)


def test_mofscriptmodel_mofscriptparameter_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptParameter.__init__)


def test_mofscriptmodel_mofscriptparameter_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptParameter.__init__)
    params = list(sig.parameters.keys())
    assert "typePrefix" in params, "Missing parameter 'typePrefix'"
    assert "name" in params, "Missing parameter 'name'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel_mofscriptparameter_has_typePrefix():
    assert hasattr(MOFScriptModel_MOFScriptParameter, "typePrefix")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptParameter.__mro__:
        if "typePrefix" in klass.__dict__:
            descriptor = klass.__dict__["typePrefix"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptparameter_has_name():
    assert hasattr(MOFScriptModel_MOFScriptParameter, "name")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptparameter_has_direction():
    assert hasattr(MOFScriptModel_MOFScriptParameter, "direction")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptparameter_has_type():
    assert hasattr(MOFScriptModel_MOFScriptParameter, "type")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_mofscripttransformation_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptTransformation)


def test_mofscriptmodel_mofscripttransformation_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptTransformation.__init__)


def test_mofscriptmodel_mofscripttransformation_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "extendsName" in params, "Missing parameter 'extendsName'"

def test_mofscriptmodel_mofscripttransformation_has_name():
    assert hasattr(MOFScriptModel_MOFScriptTransformation, "name")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptTransformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscripttransformation_has_extendsName():
    assert hasattr(MOFScriptModel_MOFScriptTransformation, "extendsName")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptTransformation.__mro__:
        if "extendsName" in klass.__dict__:
            descriptor = klass.__dict__["extendsName"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptstatementowner_is_not_abstract():
    assert not inspect.isabstract(MOFScriptStatementOwner)


def test_mofscriptstatementowner_constructor_exists():
    assert callable(MOFScriptStatementOwner.__init__)


def test_mofscriptstatementowner_constructor_args():
    sig = inspect.signature(MOFScriptStatementOwner.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_mofscriptstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptStatement)


def test_mofscriptmodel_mofscriptstatement_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptStatement.__init__)


def test_mofscriptmodel_mofscriptstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_transformationrule_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_TransformationRule)


def test_mofscriptmodel_transformationrule_constructor_exists():
    assert callable(MOFScriptModel_TransformationRule.__init__)


def test_mofscriptmodel_transformationrule_constructor_args():
    sig = inspect.signature(MOFScriptModel_TransformationRule.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isEntryPoint" in params, "Missing parameter 'isEntryPoint'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"

def test_mofscriptmodel_transformationrule_has_return_():
    assert hasattr(MOFScriptModel_TransformationRule, "return_")
    descriptor = None
    for klass in MOFScriptModel_TransformationRule.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_transformationrule_has_name():
    assert hasattr(MOFScriptModel_TransformationRule, "name")
    descriptor = None
    for klass in MOFScriptModel_TransformationRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_transformationrule_has_isEntryPoint():
    assert hasattr(MOFScriptModel_TransformationRule, "isEntryPoint")
    descriptor = None
    for klass in MOFScriptModel_TransformationRule.__mro__:
        if "isEntryPoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntryPoint"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_transformationrule_has_isAbstract():
    assert hasattr(MOFScriptModel_TransformationRule, "isAbstract")
    descriptor = None
    for klass in MOFScriptModel_TransformationRule.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_transformationrule_has_accessLevel():
    assert hasattr(MOFScriptModel_TransformationRule, "accessLevel")
    descriptor = None
    for klass in MOFScriptModel_TransformationRule.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)



def test_trace_is_not_abstract():
    assert not inspect.isabstract(Trace)


def test_trace_constructor_exists():
    assert callable(Trace.__init__)


def test_trace_constructor_args():
    sig = inspect.signature(Trace.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_m2mtrace_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_M2MTrace)


def test_mofscriptmodel_m2mtrace_constructor_exists():
    assert callable(MOFScriptModel_M2MTrace.__init__)


def test_mofscriptmodel_m2mtrace_constructor_args():
    sig = inspect.signature(MOFScriptModel_M2MTrace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_mofscriptmodel_m2mtrace_has_name():
    assert hasattr(MOFScriptModel_M2MTrace, "name")
    descriptor = None
    for klass in MOFScriptModel_M2MTrace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_m2mtrace_has_id():
    assert hasattr(MOFScriptModel_M2MTrace, "id")
    descriptor = None
    for klass in MOFScriptModel_M2MTrace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_pointcutexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_PointCutExpression)


def test_mofscriptmodel_pointcutexpression_constructor_exists():
    assert callable(MOFScriptModel_PointCutExpression.__init__)


def test_mofscriptmodel_pointcutexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_PointCutExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expressionString" in params, "Missing parameter 'expressionString'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "combinationOperator" in params, "Missing parameter 'combinationOperator'"

def test_mofscriptmodel_pointcutexpression_has_expressionString():
    assert hasattr(MOFScriptModel_PointCutExpression, "expressionString")
    descriptor = None
    for klass in MOFScriptModel_PointCutExpression.__mro__:
        if "expressionString" in klass.__dict__:
            descriptor = klass.__dict__["expressionString"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_pointcutexpression_has_operator():
    assert hasattr(MOFScriptModel_PointCutExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel_PointCutExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_pointcutexpression_has_combinationOperator():
    assert hasattr(MOFScriptModel_PointCutExpression, "combinationOperator")
    descriptor = None
    for klass in MOFScriptModel_PointCutExpression.__mro__:
        if "combinationOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinationOperator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_createexpressionparameter_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_CreateExpressionParameter)


def test_mofscriptmodel_createexpressionparameter_constructor_exists():
    assert callable(MOFScriptModel_CreateExpressionParameter.__init__)


def test_mofscriptmodel_createexpressionparameter_constructor_args():
    sig = inspect.signature(MOFScriptModel_CreateExpressionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel_createexpressionparameter_has_name():
    assert hasattr(MOFScriptModel_CreateExpressionParameter, "name")
    descriptor = None
    for klass in MOFScriptModel_CreateExpressionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_pointcut_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_PointCut)


def test_mofscriptmodel_pointcut_constructor_exists():
    assert callable(MOFScriptModel_PointCut.__init__)


def test_mofscriptmodel_pointcut_constructor_args():
    sig = inspect.signature(MOFScriptModel_PointCut.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "typeMatch" in params, "Missing parameter 'typeMatch'"

def test_mofscriptmodel_pointcut_has_name():
    assert hasattr(MOFScriptModel_PointCut, "name")
    descriptor = None
    for klass in MOFScriptModel_PointCut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_pointcut_has_typeMatch():
    assert hasattr(MOFScriptModel_PointCut, "typeMatch")
    descriptor = None
    for klass in MOFScriptModel_PointCut.__mro__:
        if "typeMatch" in klass.__dict__:
            descriptor = klass.__dict__["typeMatch"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_advice_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_Advice)


def test_mofscriptmodel_advice_constructor_exists():
    assert callable(MOFScriptModel_Advice.__init__)


def test_mofscriptmodel_advice_constructor_args():
    sig = inspect.signature(MOFScriptModel_Advice.__init__)
    params = list(sig.parameters.keys())
    assert "pointCutRef" in params, "Missing parameter 'pointCutRef'"
    assert "code" in params, "Missing parameter 'code'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel_advice_has_pointCutRef():
    assert hasattr(MOFScriptModel_Advice, "pointCutRef")
    descriptor = None
    for klass in MOFScriptModel_Advice.__mro__:
        if "pointCutRef" in klass.__dict__:
            descriptor = klass.__dict__["pointCutRef"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_advice_has_code():
    assert hasattr(MOFScriptModel_Advice, "code")
    descriptor = None
    for klass in MOFScriptModel_Advice.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_advice_has_operator():
    assert hasattr(MOFScriptModel_Advice, "operator")
    descriptor = None
    for klass in MOFScriptModel_Advice.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_advice_has_name():
    assert hasattr(MOFScriptModel_Advice, "name")
    descriptor = None
    for klass in MOFScriptModel_Advice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscripttransformation_is_not_abstract():
    assert not inspect.isabstract(MOFScriptTransformation)


def test_mofscripttransformation_constructor_exists():
    assert callable(MOFScriptTransformation.__init__)


def test_mofscripttransformation_constructor_args():
    sig = inspect.signature(MOFScriptTransformation.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_mofscriptaspect_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptAspect)


def test_mofscriptmodel_mofscriptaspect_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptAspect.__init__)


def test_mofscriptmodel_mofscriptaspect_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptAspect.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_mofscriptspecification_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptSpecification)


def test_mofscriptmodel_mofscriptspecification_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptSpecification.__init__)


def test_mofscriptmodel_mofscriptspecification_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptSpecification.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(SimpleExpression)


def test_simpleexpression_constructor_exists():
    assert callable(SimpleExpression.__init__)


def test_simpleexpression_constructor_args():
    sig = inspect.signature(SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_functioncall_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_FunctionCall)


def test_mofscriptmodel_functioncall_constructor_exists():
    assert callable(MOFScriptModel_FunctionCall.__init__)


def test_mofscriptmodel_functioncall_constructor_args():
    sig = inspect.signature(MOFScriptModel_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "isSuperCall" in params, "Missing parameter 'isSuperCall'"
    assert "transformationContext" in params, "Missing parameter 'transformationContext'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel_functioncall_has_isSuperCall():
    assert hasattr(MOFScriptModel_FunctionCall, "isSuperCall")
    descriptor = None
    for klass in MOFScriptModel_FunctionCall.__mro__:
        if "isSuperCall" in klass.__dict__:
            descriptor = klass.__dict__["isSuperCall"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_functioncall_has_transformationContext():
    assert hasattr(MOFScriptModel_FunctionCall, "transformationContext")
    descriptor = None
    for klass in MOFScriptModel_FunctionCall.__mro__:
        if "transformationContext" in klass.__dict__:
            descriptor = klass.__dict__["transformationContext"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_functioncall_has_name():
    assert hasattr(MOFScriptModel_FunctionCall, "name")
    descriptor = None
    for klass in MOFScriptModel_FunctionCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_selectexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_SelectExpression)


def test_mofscriptmodel_selectexpression_constructor_exists():
    assert callable(MOFScriptModel_SelectExpression.__init__)


def test_mofscriptmodel_selectexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel_selectexpression_has_variable():
    assert hasattr(MOFScriptModel_SelectExpression, "variable")
    descriptor = None
    for klass in MOFScriptModel_SelectExpression.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_selectexpression_has_type():
    assert hasattr(MOFScriptModel_SelectExpression, "type")
    descriptor = None
    for klass in MOFScriptModel_SelectExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_ArithmeticExpression)


def test_mofscriptmodel_arithmeticexpression_constructor_exists():
    assert callable(MOFScriptModel_ArithmeticExpression.__init__)


def test_mofscriptmodel_arithmeticexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel_arithmeticexpression_has_operator():
    assert hasattr(MOFScriptModel_ArithmeticExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel_ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_reference_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_Reference)


def test_mofscriptmodel_reference_constructor_exists():
    assert callable(MOFScriptModel_Reference.__init__)


def test_mofscriptmodel_reference_constructor_args():
    sig = inspect.signature(MOFScriptModel_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel_reference_has_name():
    assert hasattr(MOFScriptModel_Reference, "name")
    descriptor = None
    for klass in MOFScriptModel_Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_literal_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_Literal)


def test_mofscriptmodel_literal_constructor_exists():
    assert callable(MOFScriptModel_Literal.__init__)


def test_mofscriptmodel_literal_constructor_args():
    sig = inspect.signature(MOFScriptModel_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel_literal_has_value():
    assert hasattr(MOFScriptModel_Literal, "value")
    descriptor = None
    for klass in MOFScriptModel_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_literal_has_type():
    assert hasattr(MOFScriptModel_Literal, "type")
    descriptor = None
    for klass in MOFScriptModel_Literal.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_mofscriptimport_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptImport)


def test_mofscriptmodel_mofscriptimport_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptImport.__init__)


def test_mofscriptmodel_mofscriptimport_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptImport.__init__)
    params = list(sig.parameters.keys())
    assert "importSemantics" in params, "Missing parameter 'importSemantics'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_mofscriptmodel_mofscriptimport_has_importSemantics():
    assert hasattr(MOFScriptModel_MOFScriptImport, "importSemantics")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptImport.__mro__:
        if "importSemantics" in klass.__dict__:
            descriptor = klass.__dict__["importSemantics"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptimport_has_name():
    assert hasattr(MOFScriptModel_MOFScriptImport, "name")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptImport.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptimport_has_type():
    assert hasattr(MOFScriptModel_MOFScriptImport, "type")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptImport.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptimport_has_uri():
    assert hasattr(MOFScriptModel_MOFScriptImport, "uri")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptImport.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_SimpleExpression)


def test_mofscriptmodel_simpleexpression_constructor_exists():
    assert callable(MOFScriptModel_SimpleExpression.__init__)


def test_mofscriptmodel_simpleexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptStatement)


def test_mofscriptstatement_constructor_exists():
    assert callable(MOFScriptStatement.__init__)


def test_mofscriptstatement_constructor_args():
    sig = inspect.signature(MOFScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_printstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_PrintStatement)


def test_mofscriptmodel_printstatement_constructor_exists():
    assert callable(MOFScriptModel_PrintStatement.__init__)


def test_mofscriptmodel_printstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_PrintStatement.__init__)
    params = list(sig.parameters.keys())
    assert "printCommand" in params, "Missing parameter 'printCommand'"
    assert "context" in params, "Missing parameter 'context'"

def test_mofscriptmodel_printstatement_has_printCommand():
    assert hasattr(MOFScriptModel_PrintStatement, "printCommand")
    descriptor = None
    for klass in MOFScriptModel_PrintStatement.__mro__:
        if "printCommand" in klass.__dict__:
            descriptor = klass.__dict__["printCommand"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_printstatement_has_context():
    assert hasattr(MOFScriptModel_PrintStatement, "context")
    descriptor = None
    for klass in MOFScriptModel_PrintStatement.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_createstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_CreateStatement)


def test_mofscriptmodel_createstatement_constructor_exists():
    assert callable(MOFScriptModel_CreateStatement.__init__)


def test_mofscriptmodel_createstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_CreateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel_createstatement_has_type():
    assert hasattr(MOFScriptModel_CreateStatement, "type")
    descriptor = None
    for klass in MOFScriptModel_CreateStatement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_createstatement_has_name():
    assert hasattr(MOFScriptModel_CreateStatement, "name")
    descriptor = None
    for klass in MOFScriptModel_CreateStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_debugstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_DebugStatement)


def test_mofscriptmodel_debugstatement_constructor_exists():
    assert callable(MOFScriptModel_DebugStatement.__init__)


def test_mofscriptmodel_debugstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_DebugStatement.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"
    assert "vars" in params, "Missing parameter 'vars'"

def test_mofscriptmodel_debugstatement_has_specification():
    assert hasattr(MOFScriptModel_DebugStatement, "specification")
    descriptor = None
    for klass in MOFScriptModel_DebugStatement.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_debugstatement_has_vars():
    assert hasattr(MOFScriptModel_DebugStatement, "vars")
    descriptor = None
    for klass in MOFScriptModel_DebugStatement.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_ifstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_IfStatement)


def test_mofscriptmodel_ifstatement_constructor_exists():
    assert callable(MOFScriptModel_IfStatement.__init__)


def test_mofscriptmodel_ifstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_VariableDeclarationStatement)


def test_mofscriptmodel_variabledeclarationstatement_constructor_exists():
    assert callable(MOFScriptModel_VariableDeclarationStatement.__init__)


def test_mofscriptmodel_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_filestatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_FileStatement)


def test_mofscriptmodel_filestatement_constructor_exists():
    assert callable(MOFScriptModel_FileStatement.__init__)


def test_mofscriptmodel_filestatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_FileStatement.__init__)
    params = list(sig.parameters.keys())
    assert "append" in params, "Missing parameter 'append'"
    assert "fileReference" in params, "Missing parameter 'fileReference'"
    assert "use" in params, "Missing parameter 'use'"

def test_mofscriptmodel_filestatement_has_append():
    assert hasattr(MOFScriptModel_FileStatement, "append")
    descriptor = None
    for klass in MOFScriptModel_FileStatement.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_filestatement_has_fileReference():
    assert hasattr(MOFScriptModel_FileStatement, "fileReference")
    descriptor = None
    for klass in MOFScriptModel_FileStatement.__mro__:
        if "fileReference" in klass.__dict__:
            descriptor = klass.__dict__["fileReference"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_filestatement_has_use():
    assert hasattr(MOFScriptModel_FileStatement, "use")
    descriptor = None
    for klass in MOFScriptModel_FileStatement.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_FunctionCallStatement)


def test_mofscriptmodel_functioncallstatement_constructor_exists():
    assert callable(MOFScriptModel_FunctionCallStatement.__init__)


def test_mofscriptmodel_functioncallstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_resultassignment_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_ResultAssignment)


def test_mofscriptmodel_resultassignment_constructor_exists():
    assert callable(MOFScriptModel_ResultAssignment.__init__)


def test_mofscriptmodel_resultassignment_constructor_args():
    sig = inspect.signature(MOFScriptModel_ResultAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "resultPart" in params, "Missing parameter 'resultPart'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel_resultassignment_has_resultPart():
    assert hasattr(MOFScriptModel_ResultAssignment, "resultPart")
    descriptor = None
    for klass in MOFScriptModel_ResultAssignment.__mro__:
        if "resultPart" in klass.__dict__:
            descriptor = klass.__dict__["resultPart"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_resultassignment_has_operator():
    assert hasattr(MOFScriptModel_ResultAssignment, "operator")
    descriptor = None
    for klass in MOFScriptModel_ResultAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_returnstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_ReturnStatement)


def test_mofscriptmodel_returnstatement_constructor_exists():
    assert callable(MOFScriptModel_ReturnStatement.__init__)


def test_mofscriptmodel_returnstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_generalassignment_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_GeneralAssignment)


def test_mofscriptmodel_generalassignment_constructor_exists():
    assert callable(MOFScriptModel_GeneralAssignment.__init__)


def test_mofscriptmodel_generalassignment_constructor_args():
    sig = inspect.signature(MOFScriptModel_GeneralAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel_generalassignment_has_name():
    assert hasattr(MOFScriptModel_GeneralAssignment, "name")
    descriptor = None
    for klass in MOFScriptModel_GeneralAssignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_generalassignment_has_operator():
    assert hasattr(MOFScriptModel_GeneralAssignment, "operator")
    descriptor = None
    for klass in MOFScriptModel_GeneralAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_whilestatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_WhileStatement)


def test_mofscriptmodel_whilestatement_constructor_exists():
    assert callable(MOFScriptModel_WhileStatement.__init__)


def test_mofscriptmodel_whilestatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_trace_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_Trace)


def test_mofscriptmodel_trace_constructor_exists():
    assert callable(MOFScriptModel_Trace.__init__)


def test_mofscriptmodel_trace_constructor_args():
    sig = inspect.signature(MOFScriptModel_Trace.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_breakstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_BreakStatement)


def test_mofscriptmodel_breakstatement_constructor_exists():
    assert callable(MOFScriptModel_BreakStatement.__init__)


def test_mofscriptmodel_breakstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_iteratorstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_IteratorStatement)


def test_mofscriptmodel_iteratorstatement_constructor_exists():
    assert callable(MOFScriptModel_IteratorStatement.__init__)


def test_mofscriptmodel_iteratorstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel_IteratorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_mofscriptmodel_iteratorstatement_has_type():
    assert hasattr(MOFScriptModel_IteratorStatement, "type")
    descriptor = None
    for klass in MOFScriptModel_IteratorStatement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_iteratorstatement_has_variable():
    assert hasattr(MOFScriptModel_IteratorStatement, "variable")
    descriptor = None
    for klass in MOFScriptModel_IteratorStatement.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_mofscriptobject_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptObject)


def test_mofscriptmodel_mofscriptobject_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptObject.__init__)


def test_mofscriptmodel_mofscriptobject_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptObject.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"

def test_mofscriptmodel_mofscriptobject_has_column():
    assert hasattr(MOFScriptModel_MOFScriptObject, "column")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptObject.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptobject_has_line():
    assert hasattr(MOFScriptModel_MOFScriptObject, "line")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptObject.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_statementblock_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_StatementBlock)


def test_mofscriptmodel_statementblock_constructor_exists():
    assert callable(MOFScriptModel_StatementBlock.__init__)


def test_mofscriptmodel_statementblock_constructor_args():
    sig = inspect.signature(MOFScriptModel_StatementBlock.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "id" in params, "Missing parameter 'id'"

def test_mofscriptmodel_statementblock_has_protected():
    assert hasattr(MOFScriptModel_StatementBlock, "protected")
    descriptor = None
    for klass in MOFScriptModel_StatementBlock.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_statementblock_has_reference():
    assert hasattr(MOFScriptModel_StatementBlock, "reference")
    descriptor = None
    for klass in MOFScriptModel_StatementBlock.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_statementblock_has_id():
    assert hasattr(MOFScriptModel_StatementBlock, "id")
    descriptor = None
    for klass in MOFScriptModel_StatementBlock.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_VariableDeclaration)


def test_mofscriptmodel_variabledeclaration_constructor_exists():
    assert callable(MOFScriptModel_VariableDeclaration.__init__)


def test_mofscriptmodel_variabledeclaration_constructor_args():
    sig = inspect.signature(MOFScriptModel_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_mofscriptmodel_variabledeclaration_has_name():
    assert hasattr(MOFScriptModel_VariableDeclaration, "name")
    descriptor = None
    for klass in MOFScriptModel_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_variabledeclaration_has_type():
    assert hasattr(MOFScriptModel_VariableDeclaration, "type")
    descriptor = None
    for klass in MOFScriptModel_VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_variabledeclaration_has_constant():
    assert hasattr(MOFScriptModel_VariableDeclaration, "constant")
    descriptor = None
    for klass in MOFScriptModel_VariableDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_LogicalExpression)


def test_mofscriptmodel_logicalexpression_constructor_exists():
    assert callable(MOFScriptModel_LogicalExpression.__init__)


def test_mofscriptmodel_logicalexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel_logicalexpression_has_operator():
    assert hasattr(MOFScriptModel_LogicalExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel_LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_ComparisonExpression)


def test_mofscriptmodel_comparisonexpression_constructor_exists():
    assert callable(MOFScriptModel_ComparisonExpression.__init__)


def test_mofscriptmodel_comparisonexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel_comparisonexpression_has_operator():
    assert hasattr(MOFScriptModel_ComparisonExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel_ComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_createexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_CreateExpression)


def test_mofscriptmodel_createexpression_constructor_exists():
    assert callable(MOFScriptModel_CreateExpression.__init__)


def test_mofscriptmodel_createexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_CreateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel_createexpression_has_type():
    assert hasattr(MOFScriptModel_CreateExpression, "type")
    descriptor = None
    for klass in MOFScriptModel_CreateExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_valueexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_ValueExpression)


def test_mofscriptmodel_valueexpression_constructor_exists():
    assert callable(MOFScriptModel_ValueExpression.__init__)


def test_mofscriptmodel_valueexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_mofscriptmodel_valueexpression_has_specification():
    assert hasattr(MOFScriptModel_ValueExpression, "specification")
    descriptor = None
    for klass in MOFScriptModel_ValueExpression.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel_expression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_Expression)


def test_mofscriptmodel_expression_constructor_exists():
    assert callable(MOFScriptModel_Expression.__init__)


def test_mofscriptmodel_expression_constructor_args():
    sig = inspect.signature(MOFScriptModel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel_mofscriptcomment_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel_MOFScriptComment)


def test_mofscriptmodel_mofscriptcomment_constructor_exists():
    assert callable(MOFScriptModel_MOFScriptComment.__init__)


def test_mofscriptmodel_mofscriptcomment_constructor_args():
    sig = inspect.signature(MOFScriptModel_MOFScriptComment.__init__)
    params = list(sig.parameters.keys())
    assert "docStyle" in params, "Missing parameter 'docStyle'"
    assert "commentText" in params, "Missing parameter 'commentText'"
    assert "singleLine" in params, "Missing parameter 'singleLine'"

def test_mofscriptmodel_mofscriptcomment_has_docStyle():
    assert hasattr(MOFScriptModel_MOFScriptComment, "docStyle")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptComment.__mro__:
        if "docStyle" in klass.__dict__:
            descriptor = klass.__dict__["docStyle"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptcomment_has_commentText():
    assert hasattr(MOFScriptModel_MOFScriptComment, "commentText")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptComment.__mro__:
        if "commentText" in klass.__dict__:
            descriptor = klass.__dict__["commentText"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel_mofscriptcomment_has_singleLine():
    assert hasattr(MOFScriptModel_MOFScriptComment, "singleLine")
    descriptor = None
    for klass in MOFScriptModel_MOFScriptComment.__mro__:
        if "singleLine" in klass.__dict__:
            descriptor = klass.__dict__["singleLine"]
            break
    assert isinstance(descriptor, property)

def test_importsemantics_exists():
    # Check that the Enumeration exists
    assert ImportSemantics is not None

def test_importsemantics_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportSemantics]
    expected_literals = [
        "ACCESS",
        "IMPORT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportSemantics"

def test_pointcutoperator_exists():
    # Check that the Enumeration exists
    assert PointCutOperator is not None

def test_pointcutoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PointCutOperator]
    expected_literals = [
        "CALL",
        "TARGET",
        "EXECUTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PointCutOperator"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "NOT",
        "OR",
        "AND",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_literaltype_exists():
    # Check that the Enumeration exists
    assert LiteralType is not None

def test_literaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralType]
    expected_literals = [
        "BOOLEAN",
        "INTEGER",
        "STRING",
        "REAL",
        "NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralType"

def test_parameterdirection_exists():
    # Check that the Enumeration exists
    assert ParameterDirection is not None

def test_parameterdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirection]
    expected_literals = [
        "OUT",
        "IN",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirection"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "PLUS_EQ",
        "EQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PUBLIC",
        "NONE",
        "PROTECTED",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevel"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "GT",
        "NE",
        "AND",
        "GE",
        "LT",
        "LE",
        "EQ",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_adviceoperator_exists():
    # Check that the Enumeration exists
    assert AdviceOperator is not None

def test_adviceoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdviceOperator]
    expected_literals = [
        "AROUND",
        "AFTER",
        "BEFORE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdviceOperator"

def test_importtype_exists():
    # Check that the Enumeration exists
    assert ImportType is not None

def test_importtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportType]
    expected_literals = [
        "TRANSFORMATION",
        "LIBRARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportType"

def test_pointcutcombinationoperator_exists():
    # Check that the Enumeration exists
    assert PointCutCombinationOperator is not None

def test_pointcutcombinationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PointCutCombinationOperator]
    expected_literals = [
        "XOR",
        "OR",
        "AND",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PointCutCombinationOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "PLUS",
        "MINUS",
        "MULT",
        "DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"


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
MOFScriptObject_strategy = st.builds(
    MOFScriptObject,
)
MOFScriptModel_MOFScriptStatementOwner_strategy = st.builds(
    MOFScriptModel_MOFScriptStatementOwner,
)
MOFScriptModel_MOFScriptParameter_strategy = st.builds(
    MOFScriptModel_MOFScriptParameter,
    typePrefix=
        safe_text,
    name=
        safe_text,
    direction=
        safe_text,
    type=
        safe_text
)
MOFScriptModel_MOFScriptTransformation_strategy = st.builds(
    MOFScriptModel_MOFScriptTransformation,
    name=
        safe_text,
    extendsName=
        safe_text
)
MOFScriptStatementOwner_strategy = st.builds(
    MOFScriptStatementOwner,
)
MOFScriptModel_MOFScriptStatement_strategy = st.builds(
    MOFScriptModel_MOFScriptStatement,
)
MOFScriptModel_TransformationRule_strategy = st.builds(
    MOFScriptModel_TransformationRule,
    return_=
        safe_text,
    name=
        safe_text,
    isEntryPoint=
        st.booleans(),
    isAbstract=
        st.booleans(),
    accessLevel=
        safe_text
)
Trace_strategy = st.builds(
    Trace,
)
MOFScriptModel_M2MTrace_strategy = st.builds(
    MOFScriptModel_M2MTrace,
    name=
        safe_text,
    id=
        safe_text
)
MOFScriptModel_PointCutExpression_strategy = st.builds(
    MOFScriptModel_PointCutExpression,
    expressionString=
        safe_text,
    operator=
        safe_text,
    combinationOperator=
        safe_text
)
MOFScriptModel_CreateExpressionParameter_strategy = st.builds(
    MOFScriptModel_CreateExpressionParameter,
    name=
        safe_text
)
MOFScriptModel_PointCut_strategy = st.builds(
    MOFScriptModel_PointCut,
    name=
        safe_text,
    typeMatch=
        safe_text
)
MOFScriptModel_Advice_strategy = st.builds(
    MOFScriptModel_Advice,
    pointCutRef=
        safe_text,
    code=
        safe_text,
    operator=
        safe_text,
    name=
        safe_text
)
MOFScriptTransformation_strategy = st.builds(
    MOFScriptTransformation,
)
MOFScriptModel_MOFScriptAspect_strategy = st.builds(
    MOFScriptModel_MOFScriptAspect,
)
MOFScriptModel_MOFScriptSpecification_strategy = st.builds(
    MOFScriptModel_MOFScriptSpecification,
)
SimpleExpression_strategy = st.builds(
    SimpleExpression,
)
MOFScriptModel_FunctionCall_strategy = st.builds(
    MOFScriptModel_FunctionCall,
    isSuperCall=
        st.booleans(),
    transformationContext=
        safe_text,
    name=
        safe_text
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
MOFScriptModel_SelectExpression_strategy = st.builds(
    MOFScriptModel_SelectExpression,
    variable=
        safe_text,
    type=
        safe_text
)
MOFScriptModel_ArithmeticExpression_strategy = st.builds(
    MOFScriptModel_ArithmeticExpression,
    operator=
        safe_text
)
MOFScriptModel_Reference_strategy = st.builds(
    MOFScriptModel_Reference,
    name=
        safe_text
)
MOFScriptModel_Literal_strategy = st.builds(
    MOFScriptModel_Literal,
    value=
        safe_text,
    type=
        safe_text
)
MOFScriptModel_MOFScriptImport_strategy = st.builds(
    MOFScriptModel_MOFScriptImport,
    importSemantics=
        safe_text,
    name=
        safe_text,
    type=
        safe_text,
    uri=
        safe_text
)
MOFScriptModel_SimpleExpression_strategy = st.builds(
    MOFScriptModel_SimpleExpression,
)
MOFScriptStatement_strategy = st.builds(
    MOFScriptStatement,
)
MOFScriptModel_PrintStatement_strategy = st.builds(
    MOFScriptModel_PrintStatement,
    printCommand=
        safe_text,
    context=
        safe_text
)
MOFScriptModel_CreateStatement_strategy = st.builds(
    MOFScriptModel_CreateStatement,
    type=
        safe_text,
    name=
        safe_text
)
MOFScriptModel_DebugStatement_strategy = st.builds(
    MOFScriptModel_DebugStatement,
    specification=
        safe_text,
    vars=
        safe_text
)
MOFScriptModel_IfStatement_strategy = st.builds(
    MOFScriptModel_IfStatement,
)
MOFScriptModel_VariableDeclarationStatement_strategy = st.builds(
    MOFScriptModel_VariableDeclarationStatement,
)
MOFScriptModel_FileStatement_strategy = st.builds(
    MOFScriptModel_FileStatement,
    append=
        st.booleans(),
    fileReference=
        safe_text,
    use=
        st.booleans()
)
MOFScriptModel_FunctionCallStatement_strategy = st.builds(
    MOFScriptModel_FunctionCallStatement,
)
MOFScriptModel_ResultAssignment_strategy = st.builds(
    MOFScriptModel_ResultAssignment,
    resultPart=
        safe_text,
    operator=
        safe_text
)
MOFScriptModel_ReturnStatement_strategy = st.builds(
    MOFScriptModel_ReturnStatement,
)
MOFScriptModel_GeneralAssignment_strategy = st.builds(
    MOFScriptModel_GeneralAssignment,
    name=
        safe_text,
    operator=
        safe_text
)
MOFScriptModel_WhileStatement_strategy = st.builds(
    MOFScriptModel_WhileStatement,
)
MOFScriptModel_Trace_strategy = st.builds(
    MOFScriptModel_Trace,
)
MOFScriptModel_BreakStatement_strategy = st.builds(
    MOFScriptModel_BreakStatement,
)
MOFScriptModel_IteratorStatement_strategy = st.builds(
    MOFScriptModel_IteratorStatement,
    type=
        safe_text,
    variable=
        safe_text
)
MOFScriptModel_MOFScriptObject_strategy = st.builds(
    MOFScriptModel_MOFScriptObject,
    column=
        st.integers(),
    line=
        st.integers()
)
MOFScriptModel_StatementBlock_strategy = st.builds(
    MOFScriptModel_StatementBlock,
    protected=
        st.booleans(),
    reference=
        safe_text,
    id=
        safe_text
)
MOFScriptModel_VariableDeclaration_strategy = st.builds(
    MOFScriptModel_VariableDeclaration,
    name=
        safe_text,
    type=
        safe_text,
    constant=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
MOFScriptModel_LogicalExpression_strategy = st.builds(
    MOFScriptModel_LogicalExpression,
    operator=
        safe_text
)
MOFScriptModel_ComparisonExpression_strategy = st.builds(
    MOFScriptModel_ComparisonExpression,
    operator=
        safe_text
)
MOFScriptModel_CreateExpression_strategy = st.builds(
    MOFScriptModel_CreateExpression,
    type=
        safe_text
)
MOFScriptModel_ValueExpression_strategy = st.builds(
    MOFScriptModel_ValueExpression,
    specification=
        safe_text
)
MOFScriptModel_Expression_strategy = st.builds(
    MOFScriptModel_Expression,
)
MOFScriptModel_MOFScriptComment_strategy = st.builds(
    MOFScriptModel_MOFScriptComment,
    docStyle=
        st.booleans(),
    commentText=
        safe_text,
    singleLine=
        st.booleans()
)

@given(instance=MOFScriptObject_strategy)
@settings(max_examples=50)
def test_mofscriptobject_instantiation(instance):
    assert isinstance(instance, MOFScriptObject)

@given(instance=MOFScriptModel_MOFScriptStatementOwner_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptstatementowner_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptStatementOwner)

@given(instance=MOFScriptModel_MOFScriptParameter_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptparameter_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptParameter)



@given(instance=MOFScriptModel_MOFScriptParameter_strategy)
def test_mofscriptmodel_mofscriptparameter_typePrefix_setter(instance):
    original = instance.typePrefix
    instance.typePrefix = original
    assert instance.typePrefix == original



@given(instance=MOFScriptModel_MOFScriptParameter_strategy)
def test_mofscriptmodel_mofscriptparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_MOFScriptParameter_strategy)
def test_mofscriptmodel_mofscriptparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=MOFScriptModel_MOFScriptParameter_strategy)
def test_mofscriptmodel_mofscriptparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel_MOFScriptTransformation_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscripttransformation_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptTransformation)



@given(instance=MOFScriptModel_MOFScriptTransformation_strategy)
def test_mofscriptmodel_mofscripttransformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_MOFScriptTransformation_strategy)
def test_mofscriptmodel_mofscripttransformation_extendsName_setter(instance):
    original = instance.extendsName
    instance.extendsName = original
    assert instance.extendsName == original

@given(instance=MOFScriptStatementOwner_strategy)
@settings(max_examples=50)
def test_mofscriptstatementowner_instantiation(instance):
    assert isinstance(instance, MOFScriptStatementOwner)

@given(instance=MOFScriptModel_MOFScriptStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptStatement)

@given(instance=MOFScriptModel_TransformationRule_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_transformationrule_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_TransformationRule)



@given(instance=MOFScriptModel_TransformationRule_strategy)
def test_mofscriptmodel_transformationrule_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original



@given(instance=MOFScriptModel_TransformationRule_strategy)
def test_mofscriptmodel_transformationrule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_TransformationRule_strategy)
def test_mofscriptmodel_transformationrule_isEntryPoint_setter(instance):
    original = instance.isEntryPoint
    instance.isEntryPoint = original
    assert instance.isEntryPoint == original



@given(instance=MOFScriptModel_TransformationRule_strategy)
def test_mofscriptmodel_transformationrule_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=MOFScriptModel_TransformationRule_strategy)
def test_mofscriptmodel_transformationrule_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=Trace_strategy)
@settings(max_examples=50)
def test_trace_instantiation(instance):
    assert isinstance(instance, Trace)

@given(instance=MOFScriptModel_M2MTrace_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_m2mtrace_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_M2MTrace)



@given(instance=MOFScriptModel_M2MTrace_strategy)
def test_mofscriptmodel_m2mtrace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_M2MTrace_strategy)
def test_mofscriptmodel_m2mtrace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MOFScriptModel_PointCutExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_pointcutexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_PointCutExpression)



@given(instance=MOFScriptModel_PointCutExpression_strategy)
def test_mofscriptmodel_pointcutexpression_expressionString_setter(instance):
    original = instance.expressionString
    instance.expressionString = original
    assert instance.expressionString == original



@given(instance=MOFScriptModel_PointCutExpression_strategy)
def test_mofscriptmodel_pointcutexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=MOFScriptModel_PointCutExpression_strategy)
def test_mofscriptmodel_pointcutexpression_combinationOperator_setter(instance):
    original = instance.combinationOperator
    instance.combinationOperator = original
    assert instance.combinationOperator == original

@given(instance=MOFScriptModel_CreateExpressionParameter_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_createexpressionparameter_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_CreateExpressionParameter)



@given(instance=MOFScriptModel_CreateExpressionParameter_strategy)
def test_mofscriptmodel_createexpressionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel_PointCut_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_pointcut_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_PointCut)



@given(instance=MOFScriptModel_PointCut_strategy)
def test_mofscriptmodel_pointcut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_PointCut_strategy)
def test_mofscriptmodel_pointcut_typeMatch_setter(instance):
    original = instance.typeMatch
    instance.typeMatch = original
    assert instance.typeMatch == original

@given(instance=MOFScriptModel_Advice_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_advice_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_Advice)



@given(instance=MOFScriptModel_Advice_strategy)
def test_mofscriptmodel_advice_pointCutRef_setter(instance):
    original = instance.pointCutRef
    instance.pointCutRef = original
    assert instance.pointCutRef == original



@given(instance=MOFScriptModel_Advice_strategy)
def test_mofscriptmodel_advice_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=MOFScriptModel_Advice_strategy)
def test_mofscriptmodel_advice_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=MOFScriptModel_Advice_strategy)
def test_mofscriptmodel_advice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptTransformation_strategy)
@settings(max_examples=50)
def test_mofscripttransformation_instantiation(instance):
    assert isinstance(instance, MOFScriptTransformation)

@given(instance=MOFScriptModel_MOFScriptAspect_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptaspect_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptAspect)

@given(instance=MOFScriptModel_MOFScriptSpecification_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptspecification_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptSpecification)

@given(instance=SimpleExpression_strategy)
@settings(max_examples=50)
def test_simpleexpression_instantiation(instance):
    assert isinstance(instance, SimpleExpression)

@given(instance=MOFScriptModel_FunctionCall_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_functioncall_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_FunctionCall)



@given(instance=MOFScriptModel_FunctionCall_strategy)
def test_mofscriptmodel_functioncall_isSuperCall_setter(instance):
    original = instance.isSuperCall
    instance.isSuperCall = original
    assert instance.isSuperCall == original



@given(instance=MOFScriptModel_FunctionCall_strategy)
def test_mofscriptmodel_functioncall_transformationContext_setter(instance):
    original = instance.transformationContext
    instance.transformationContext = original
    assert instance.transformationContext == original



@given(instance=MOFScriptModel_FunctionCall_strategy)
def test_mofscriptmodel_functioncall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=MOFScriptModel_SelectExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_selectexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_SelectExpression)



@given(instance=MOFScriptModel_SelectExpression_strategy)
def test_mofscriptmodel_selectexpression_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original



@given(instance=MOFScriptModel_SelectExpression_strategy)
def test_mofscriptmodel_selectexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_ArithmeticExpression)



@given(instance=MOFScriptModel_ArithmeticExpression_strategy)
def test_mofscriptmodel_arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel_Reference_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_reference_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_Reference)



@given(instance=MOFScriptModel_Reference_strategy)
def test_mofscriptmodel_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel_Literal_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_literal_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_Literal)



@given(instance=MOFScriptModel_Literal_strategy)
def test_mofscriptmodel_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=MOFScriptModel_Literal_strategy)
def test_mofscriptmodel_literal_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel_MOFScriptImport_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptimport_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptImport)



@given(instance=MOFScriptModel_MOFScriptImport_strategy)
def test_mofscriptmodel_mofscriptimport_importSemantics_setter(instance):
    original = instance.importSemantics
    instance.importSemantics = original
    assert instance.importSemantics == original



@given(instance=MOFScriptModel_MOFScriptImport_strategy)
def test_mofscriptmodel_mofscriptimport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_MOFScriptImport_strategy)
def test_mofscriptmodel_mofscriptimport_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MOFScriptModel_MOFScriptImport_strategy)
def test_mofscriptmodel_mofscriptimport_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=MOFScriptModel_SimpleExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_simpleexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_SimpleExpression)

@given(instance=MOFScriptStatement_strategy)
@settings(max_examples=50)
def test_mofscriptstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptStatement)

@given(instance=MOFScriptModel_PrintStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_printstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_PrintStatement)



@given(instance=MOFScriptModel_PrintStatement_strategy)
def test_mofscriptmodel_printstatement_printCommand_setter(instance):
    original = instance.printCommand
    instance.printCommand = original
    assert instance.printCommand == original



@given(instance=MOFScriptModel_PrintStatement_strategy)
def test_mofscriptmodel_printstatement_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=MOFScriptModel_CreateStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_createstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_CreateStatement)



@given(instance=MOFScriptModel_CreateStatement_strategy)
def test_mofscriptmodel_createstatement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MOFScriptModel_CreateStatement_strategy)
def test_mofscriptmodel_createstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel_DebugStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_debugstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_DebugStatement)



@given(instance=MOFScriptModel_DebugStatement_strategy)
def test_mofscriptmodel_debugstatement_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original



@given(instance=MOFScriptModel_DebugStatement_strategy)
def test_mofscriptmodel_debugstatement_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=MOFScriptModel_IfStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_ifstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_IfStatement)

@given(instance=MOFScriptModel_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_VariableDeclarationStatement)

@given(instance=MOFScriptModel_FileStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_filestatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_FileStatement)



@given(instance=MOFScriptModel_FileStatement_strategy)
def test_mofscriptmodel_filestatement_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original



@given(instance=MOFScriptModel_FileStatement_strategy)
def test_mofscriptmodel_filestatement_fileReference_setter(instance):
    original = instance.fileReference
    instance.fileReference = original
    assert instance.fileReference == original



@given(instance=MOFScriptModel_FileStatement_strategy)
def test_mofscriptmodel_filestatement_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=MOFScriptModel_FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_functioncallstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_FunctionCallStatement)

@given(instance=MOFScriptModel_ResultAssignment_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_resultassignment_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_ResultAssignment)



@given(instance=MOFScriptModel_ResultAssignment_strategy)
def test_mofscriptmodel_resultassignment_resultPart_setter(instance):
    original = instance.resultPart
    instance.resultPart = original
    assert instance.resultPart == original



@given(instance=MOFScriptModel_ResultAssignment_strategy)
def test_mofscriptmodel_resultassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel_ReturnStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_returnstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_ReturnStatement)

@given(instance=MOFScriptModel_GeneralAssignment_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_generalassignment_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_GeneralAssignment)



@given(instance=MOFScriptModel_GeneralAssignment_strategy)
def test_mofscriptmodel_generalassignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_GeneralAssignment_strategy)
def test_mofscriptmodel_generalassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel_WhileStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_whilestatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_WhileStatement)

@given(instance=MOFScriptModel_Trace_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_trace_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_Trace)

@given(instance=MOFScriptModel_BreakStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_breakstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_BreakStatement)

@given(instance=MOFScriptModel_IteratorStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_iteratorstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_IteratorStatement)



@given(instance=MOFScriptModel_IteratorStatement_strategy)
def test_mofscriptmodel_iteratorstatement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MOFScriptModel_IteratorStatement_strategy)
def test_mofscriptmodel_iteratorstatement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=MOFScriptModel_MOFScriptObject_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptobject_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptObject)



@given(instance=MOFScriptModel_MOFScriptObject_strategy)
def test_mofscriptmodel_mofscriptobject_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=MOFScriptModel_MOFScriptObject_strategy)
def test_mofscriptmodel_mofscriptobject_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=MOFScriptModel_StatementBlock_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_statementblock_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_StatementBlock)



@given(instance=MOFScriptModel_StatementBlock_strategy)
def test_mofscriptmodel_statementblock_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=MOFScriptModel_StatementBlock_strategy)
def test_mofscriptmodel_statementblock_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=MOFScriptModel_StatementBlock_strategy)
def test_mofscriptmodel_statementblock_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MOFScriptModel_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_variabledeclaration_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_VariableDeclaration)



@given(instance=MOFScriptModel_VariableDeclaration_strategy)
def test_mofscriptmodel_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MOFScriptModel_VariableDeclaration_strategy)
def test_mofscriptmodel_variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MOFScriptModel_VariableDeclaration_strategy)
def test_mofscriptmodel_variabledeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=MOFScriptModel_LogicalExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_logicalexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_LogicalExpression)



@given(instance=MOFScriptModel_LogicalExpression_strategy)
def test_mofscriptmodel_logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel_ComparisonExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_comparisonexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_ComparisonExpression)



@given(instance=MOFScriptModel_ComparisonExpression_strategy)
def test_mofscriptmodel_comparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel_CreateExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_createexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_CreateExpression)



@given(instance=MOFScriptModel_CreateExpression_strategy)
def test_mofscriptmodel_createexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel_ValueExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_valueexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_ValueExpression)



@given(instance=MOFScriptModel_ValueExpression_strategy)
def test_mofscriptmodel_valueexpression_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=MOFScriptModel_Expression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_expression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_Expression)

@given(instance=MOFScriptModel_MOFScriptComment_strategy)
@settings(max_examples=50)
def test_mofscriptmodel_mofscriptcomment_instantiation(instance):
    assert isinstance(instance, MOFScriptModel_MOFScriptComment)



@given(instance=MOFScriptModel_MOFScriptComment_strategy)
def test_mofscriptmodel_mofscriptcomment_docStyle_setter(instance):
    original = instance.docStyle
    instance.docStyle = original
    assert instance.docStyle == original



@given(instance=MOFScriptModel_MOFScriptComment_strategy)
def test_mofscriptmodel_mofscriptcomment_commentText_setter(instance):
    original = instance.commentText
    instance.commentText = original
    assert instance.commentText == original



@given(instance=MOFScriptModel_MOFScriptComment_strategy)
def test_mofscriptmodel_mofscriptcomment_singleLine_setter(instance):
    original = instance.singleLine
    instance.singleLine = original
    assert instance.singleLine == original
