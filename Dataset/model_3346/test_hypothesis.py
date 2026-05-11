import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Trace,
    MOFScriptModel::M2MTrace,
    MOFScriptModel::PointCutExpression,
    MOFScriptModel::PointCut,
    MOFScriptTransformation,
    MOFScriptModel::MOFScriptAspect,
    SimpleExpression,
    MOFScriptModel::FunctionCall,
    ValueExpression,
    MOFScriptModel::SelectExpression,
    MOFScriptModel::ArithmeticExpression,
    MOFScriptModel::Reference,
    MOFScriptModel::Literal,
    MOFScriptModel::SimpleExpression,
    MOFScriptStatement,
    MOFScriptModel::WhileStatement,
    MOFScriptModel::DebugStatement,
    MOFScriptModel::BreakStatement,
    MOFScriptModel::Trace,
    MOFScriptModel::FunctionCallStatement,
    MOFScriptModel::GeneralAssignment,
    MOFScriptModel::CreateStatement,
    MOFScriptModel::VariableDeclarationStatement,
    MOFScriptModel::ResultAssignment,
    MOFScriptModel::IfStatement,
    MOFScriptModel::PrintStatement,
    MOFScriptModel::FileStatement,
    MOFScriptModel::ReturnStatement,
    MOFScriptModel::IteratorStatement,
    MOFScriptModel::MOFScriptObject,
    MOFScriptModel::StatementBlock,
    Expression,
    MOFScriptModel::ComparisonExpression,
    MOFScriptModel::LogicalExpression,
    MOFScriptModel::CreateExpression,
    MOFScriptModel::ValueExpression,
    MOFScriptObject,
    MOFScriptModel::MOFScriptImport,
    MOFScriptModel::CreateExpressionParameter,
    MOFScriptModel::MOFScriptSpecification,
    MOFScriptModel::Expression,
    MOFScriptModel::MOFScriptComment,
    MOFScriptModel::VariableDeclaration,
    MOFScriptModel::MOFScriptStatementOwner,
    MOFScriptModel::MOFScriptParameter,
    MOFScriptModel::MOFScriptTransformation,
    MOFScriptStatementOwner,
    MOFScriptModel::Advice,
    MOFScriptModel::MOFScriptStatement,
    MOFScriptModel::TransformationRule,
    ParameterDirection,
    ImportSemantics,
    PointCutOperator,
    ImportType,
    AdviceOperator,
    ArithmeticOperator,
    LogicalOperator,
    LiteralType,
    ComparisonOperator,
    AccessLevel,
    AssignmentOperator,
    PointCutCombinationOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_is_not_abstract():
    assert not inspect.isabstract(Trace)


def test_trace_constructor_exists():
    assert callable(Trace.__init__)


def test_trace_constructor_args():
    sig = inspect.signature(Trace.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::m2mtrace_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::M2MTrace)


def test_mofscriptmodel::m2mtrace_constructor_exists():
    assert callable(MOFScriptModel::M2MTrace.__init__)


def test_mofscriptmodel::m2mtrace_constructor_args():
    sig = inspect.signature(MOFScriptModel::M2MTrace.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel::m2mtrace_has_id():
    assert hasattr(MOFScriptModel::M2MTrace, "id")
    descriptor = None
    for klass in MOFScriptModel::M2MTrace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::m2mtrace_has_name():
    assert hasattr(MOFScriptModel::M2MTrace, "name")
    descriptor = None
    for klass in MOFScriptModel::M2MTrace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::pointcutexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::PointCutExpression)


def test_mofscriptmodel::pointcutexpression_constructor_exists():
    assert callable(MOFScriptModel::PointCutExpression.__init__)


def test_mofscriptmodel::pointcutexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::PointCutExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "combinationOperator" in params, "Missing parameter 'combinationOperator'"
    assert "expressionString" in params, "Missing parameter 'expressionString'"

def test_mofscriptmodel::pointcutexpression_has_operator():
    assert hasattr(MOFScriptModel::PointCutExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel::PointCutExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::pointcutexpression_has_combinationOperator():
    assert hasattr(MOFScriptModel::PointCutExpression, "combinationOperator")
    descriptor = None
    for klass in MOFScriptModel::PointCutExpression.__mro__:
        if "combinationOperator" in klass.__dict__:
            descriptor = klass.__dict__["combinationOperator"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::pointcutexpression_has_expressionString():
    assert hasattr(MOFScriptModel::PointCutExpression, "expressionString")
    descriptor = None
    for klass in MOFScriptModel::PointCutExpression.__mro__:
        if "expressionString" in klass.__dict__:
            descriptor = klass.__dict__["expressionString"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::pointcut_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::PointCut)


def test_mofscriptmodel::pointcut_constructor_exists():
    assert callable(MOFScriptModel::PointCut.__init__)


def test_mofscriptmodel::pointcut_constructor_args():
    sig = inspect.signature(MOFScriptModel::PointCut.__init__)
    params = list(sig.parameters.keys())
    assert "typeMatch" in params, "Missing parameter 'typeMatch'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel::pointcut_has_typeMatch():
    assert hasattr(MOFScriptModel::PointCut, "typeMatch")
    descriptor = None
    for klass in MOFScriptModel::PointCut.__mro__:
        if "typeMatch" in klass.__dict__:
            descriptor = klass.__dict__["typeMatch"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::pointcut_has_name():
    assert hasattr(MOFScriptModel::PointCut, "name")
    descriptor = None
    for klass in MOFScriptModel::PointCut.__mro__:
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



def test_mofscriptmodel::mofscriptaspect_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptAspect)


def test_mofscriptmodel::mofscriptaspect_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptAspect.__init__)


def test_mofscriptmodel::mofscriptaspect_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptAspect.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(SimpleExpression)


def test_simpleexpression_constructor_exists():
    assert callable(SimpleExpression.__init__)


def test_simpleexpression_constructor_args():
    sig = inspect.signature(SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::functioncall_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::FunctionCall)


def test_mofscriptmodel::functioncall_constructor_exists():
    assert callable(MOFScriptModel::FunctionCall.__init__)


def test_mofscriptmodel::functioncall_constructor_args():
    sig = inspect.signature(MOFScriptModel::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "transformationContext" in params, "Missing parameter 'transformationContext'"
    assert "isSuperCall" in params, "Missing parameter 'isSuperCall'"

def test_mofscriptmodel::functioncall_has_name():
    assert hasattr(MOFScriptModel::FunctionCall, "name")
    descriptor = None
    for klass in MOFScriptModel::FunctionCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::functioncall_has_transformationContext():
    assert hasattr(MOFScriptModel::FunctionCall, "transformationContext")
    descriptor = None
    for klass in MOFScriptModel::FunctionCall.__mro__:
        if "transformationContext" in klass.__dict__:
            descriptor = klass.__dict__["transformationContext"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::functioncall_has_isSuperCall():
    assert hasattr(MOFScriptModel::FunctionCall, "isSuperCall")
    descriptor = None
    for klass in MOFScriptModel::FunctionCall.__mro__:
        if "isSuperCall" in klass.__dict__:
            descriptor = klass.__dict__["isSuperCall"]
            break
    assert isinstance(descriptor, property)



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::selectexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::SelectExpression)


def test_mofscriptmodel::selectexpression_constructor_exists():
    assert callable(MOFScriptModel::SelectExpression.__init__)


def test_mofscriptmodel::selectexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel::selectexpression_has_variable():
    assert hasattr(MOFScriptModel::SelectExpression, "variable")
    descriptor = None
    for klass in MOFScriptModel::SelectExpression.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::selectexpression_has_type():
    assert hasattr(MOFScriptModel::SelectExpression, "type")
    descriptor = None
    for klass in MOFScriptModel::SelectExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::ArithmeticExpression)


def test_mofscriptmodel::arithmeticexpression_constructor_exists():
    assert callable(MOFScriptModel::ArithmeticExpression.__init__)


def test_mofscriptmodel::arithmeticexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel::arithmeticexpression_has_operator():
    assert hasattr(MOFScriptModel::ArithmeticExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::reference_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::Reference)


def test_mofscriptmodel::reference_constructor_exists():
    assert callable(MOFScriptModel::Reference.__init__)


def test_mofscriptmodel::reference_constructor_args():
    sig = inspect.signature(MOFScriptModel::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel::reference_has_name():
    assert hasattr(MOFScriptModel::Reference, "name")
    descriptor = None
    for klass in MOFScriptModel::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::literal_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::Literal)


def test_mofscriptmodel::literal_constructor_exists():
    assert callable(MOFScriptModel::Literal.__init__)


def test_mofscriptmodel::literal_constructor_args():
    sig = inspect.signature(MOFScriptModel::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel::literal_has_value():
    assert hasattr(MOFScriptModel::Literal, "value")
    descriptor = None
    for klass in MOFScriptModel::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::literal_has_type():
    assert hasattr(MOFScriptModel::Literal, "type")
    descriptor = None
    for klass in MOFScriptModel::Literal.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::simpleexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::SimpleExpression)


def test_mofscriptmodel::simpleexpression_constructor_exists():
    assert callable(MOFScriptModel::SimpleExpression.__init__)


def test_mofscriptmodel::simpleexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptStatement)


def test_mofscriptstatement_constructor_exists():
    assert callable(MOFScriptStatement.__init__)


def test_mofscriptstatement_constructor_args():
    sig = inspect.signature(MOFScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::whilestatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::WhileStatement)


def test_mofscriptmodel::whilestatement_constructor_exists():
    assert callable(MOFScriptModel::WhileStatement.__init__)


def test_mofscriptmodel::whilestatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::debugstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::DebugStatement)


def test_mofscriptmodel::debugstatement_constructor_exists():
    assert callable(MOFScriptModel::DebugStatement.__init__)


def test_mofscriptmodel::debugstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::DebugStatement.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"
    assert "vars" in params, "Missing parameter 'vars'"

def test_mofscriptmodel::debugstatement_has_specification():
    assert hasattr(MOFScriptModel::DebugStatement, "specification")
    descriptor = None
    for klass in MOFScriptModel::DebugStatement.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::debugstatement_has_vars():
    assert hasattr(MOFScriptModel::DebugStatement, "vars")
    descriptor = None
    for klass in MOFScriptModel::DebugStatement.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::breakstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::BreakStatement)


def test_mofscriptmodel::breakstatement_constructor_exists():
    assert callable(MOFScriptModel::BreakStatement.__init__)


def test_mofscriptmodel::breakstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::trace_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::Trace)


def test_mofscriptmodel::trace_constructor_exists():
    assert callable(MOFScriptModel::Trace.__init__)


def test_mofscriptmodel::trace_constructor_args():
    sig = inspect.signature(MOFScriptModel::Trace.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::FunctionCallStatement)


def test_mofscriptmodel::functioncallstatement_constructor_exists():
    assert callable(MOFScriptModel::FunctionCallStatement.__init__)


def test_mofscriptmodel::functioncallstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::generalassignment_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::GeneralAssignment)


def test_mofscriptmodel::generalassignment_constructor_exists():
    assert callable(MOFScriptModel::GeneralAssignment.__init__)


def test_mofscriptmodel::generalassignment_constructor_args():
    sig = inspect.signature(MOFScriptModel::GeneralAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel::generalassignment_has_name():
    assert hasattr(MOFScriptModel::GeneralAssignment, "name")
    descriptor = None
    for klass in MOFScriptModel::GeneralAssignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::generalassignment_has_operator():
    assert hasattr(MOFScriptModel::GeneralAssignment, "operator")
    descriptor = None
    for klass in MOFScriptModel::GeneralAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::createstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::CreateStatement)


def test_mofscriptmodel::createstatement_constructor_exists():
    assert callable(MOFScriptModel::CreateStatement.__init__)


def test_mofscriptmodel::createstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::CreateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel::createstatement_has_name():
    assert hasattr(MOFScriptModel::CreateStatement, "name")
    descriptor = None
    for klass in MOFScriptModel::CreateStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::createstatement_has_type():
    assert hasattr(MOFScriptModel::CreateStatement, "type")
    descriptor = None
    for klass in MOFScriptModel::CreateStatement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::VariableDeclarationStatement)


def test_mofscriptmodel::variabledeclarationstatement_constructor_exists():
    assert callable(MOFScriptModel::VariableDeclarationStatement.__init__)


def test_mofscriptmodel::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::resultassignment_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::ResultAssignment)


def test_mofscriptmodel::resultassignment_constructor_exists():
    assert callable(MOFScriptModel::ResultAssignment.__init__)


def test_mofscriptmodel::resultassignment_constructor_args():
    sig = inspect.signature(MOFScriptModel::ResultAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "resultPart" in params, "Missing parameter 'resultPart'"

def test_mofscriptmodel::resultassignment_has_operator():
    assert hasattr(MOFScriptModel::ResultAssignment, "operator")
    descriptor = None
    for klass in MOFScriptModel::ResultAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::resultassignment_has_resultPart():
    assert hasattr(MOFScriptModel::ResultAssignment, "resultPart")
    descriptor = None
    for klass in MOFScriptModel::ResultAssignment.__mro__:
        if "resultPart" in klass.__dict__:
            descriptor = klass.__dict__["resultPart"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::ifstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::IfStatement)


def test_mofscriptmodel::ifstatement_constructor_exists():
    assert callable(MOFScriptModel::IfStatement.__init__)


def test_mofscriptmodel::ifstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::printstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::PrintStatement)


def test_mofscriptmodel::printstatement_constructor_exists():
    assert callable(MOFScriptModel::PrintStatement.__init__)


def test_mofscriptmodel::printstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::PrintStatement.__init__)
    params = list(sig.parameters.keys())
    assert "printCommand" in params, "Missing parameter 'printCommand'"
    assert "context" in params, "Missing parameter 'context'"

def test_mofscriptmodel::printstatement_has_printCommand():
    assert hasattr(MOFScriptModel::PrintStatement, "printCommand")
    descriptor = None
    for klass in MOFScriptModel::PrintStatement.__mro__:
        if "printCommand" in klass.__dict__:
            descriptor = klass.__dict__["printCommand"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::printstatement_has_context():
    assert hasattr(MOFScriptModel::PrintStatement, "context")
    descriptor = None
    for klass in MOFScriptModel::PrintStatement.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::filestatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::FileStatement)


def test_mofscriptmodel::filestatement_constructor_exists():
    assert callable(MOFScriptModel::FileStatement.__init__)


def test_mofscriptmodel::filestatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::FileStatement.__init__)
    params = list(sig.parameters.keys())
    assert "append" in params, "Missing parameter 'append'"
    assert "fileReference" in params, "Missing parameter 'fileReference'"
    assert "use" in params, "Missing parameter 'use'"

def test_mofscriptmodel::filestatement_has_append():
    assert hasattr(MOFScriptModel::FileStatement, "append")
    descriptor = None
    for klass in MOFScriptModel::FileStatement.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::filestatement_has_fileReference():
    assert hasattr(MOFScriptModel::FileStatement, "fileReference")
    descriptor = None
    for klass in MOFScriptModel::FileStatement.__mro__:
        if "fileReference" in klass.__dict__:
            descriptor = klass.__dict__["fileReference"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::filestatement_has_use():
    assert hasattr(MOFScriptModel::FileStatement, "use")
    descriptor = None
    for klass in MOFScriptModel::FileStatement.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::returnstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::ReturnStatement)


def test_mofscriptmodel::returnstatement_constructor_exists():
    assert callable(MOFScriptModel::ReturnStatement.__init__)


def test_mofscriptmodel::returnstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::iteratorstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::IteratorStatement)


def test_mofscriptmodel::iteratorstatement_constructor_exists():
    assert callable(MOFScriptModel::IteratorStatement.__init__)


def test_mofscriptmodel::iteratorstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::IteratorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_mofscriptmodel::iteratorstatement_has_type():
    assert hasattr(MOFScriptModel::IteratorStatement, "type")
    descriptor = None
    for klass in MOFScriptModel::IteratorStatement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::iteratorstatement_has_variable():
    assert hasattr(MOFScriptModel::IteratorStatement, "variable")
    descriptor = None
    for klass in MOFScriptModel::IteratorStatement.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::mofscriptobject_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptObject)


def test_mofscriptmodel::mofscriptobject_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptObject.__init__)


def test_mofscriptmodel::mofscriptobject_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptObject.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"

def test_mofscriptmodel::mofscriptobject_has_column():
    assert hasattr(MOFScriptModel::MOFScriptObject, "column")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptObject.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptobject_has_line():
    assert hasattr(MOFScriptModel::MOFScriptObject, "line")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptObject.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::statementblock_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::StatementBlock)


def test_mofscriptmodel::statementblock_constructor_exists():
    assert callable(MOFScriptModel::StatementBlock.__init__)


def test_mofscriptmodel::statementblock_constructor_args():
    sig = inspect.signature(MOFScriptModel::StatementBlock.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "protected" in params, "Missing parameter 'protected'"

def test_mofscriptmodel::statementblock_has_id():
    assert hasattr(MOFScriptModel::StatementBlock, "id")
    descriptor = None
    for klass in MOFScriptModel::StatementBlock.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::statementblock_has_reference():
    assert hasattr(MOFScriptModel::StatementBlock, "reference")
    descriptor = None
    for klass in MOFScriptModel::StatementBlock.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::statementblock_has_protected():
    assert hasattr(MOFScriptModel::StatementBlock, "protected")
    descriptor = None
    for klass in MOFScriptModel::StatementBlock.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::ComparisonExpression)


def test_mofscriptmodel::comparisonexpression_constructor_exists():
    assert callable(MOFScriptModel::ComparisonExpression.__init__)


def test_mofscriptmodel::comparisonexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel::comparisonexpression_has_operator():
    assert hasattr(MOFScriptModel::ComparisonExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel::ComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::LogicalExpression)


def test_mofscriptmodel::logicalexpression_constructor_exists():
    assert callable(MOFScriptModel::LogicalExpression.__init__)


def test_mofscriptmodel::logicalexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mofscriptmodel::logicalexpression_has_operator():
    assert hasattr(MOFScriptModel::LogicalExpression, "operator")
    descriptor = None
    for klass in MOFScriptModel::LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::createexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::CreateExpression)


def test_mofscriptmodel::createexpression_constructor_exists():
    assert callable(MOFScriptModel::CreateExpression.__init__)


def test_mofscriptmodel::createexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::CreateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mofscriptmodel::createexpression_has_type():
    assert hasattr(MOFScriptModel::CreateExpression, "type")
    descriptor = None
    for klass in MOFScriptModel::CreateExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::valueexpression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::ValueExpression)


def test_mofscriptmodel::valueexpression_constructor_exists():
    assert callable(MOFScriptModel::ValueExpression.__init__)


def test_mofscriptmodel::valueexpression_constructor_args():
    sig = inspect.signature(MOFScriptModel::ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_mofscriptmodel::valueexpression_has_specification():
    assert hasattr(MOFScriptModel::ValueExpression, "specification")
    descriptor = None
    for klass in MOFScriptModel::ValueExpression.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptobject_is_not_abstract():
    assert not inspect.isabstract(MOFScriptObject)


def test_mofscriptobject_constructor_exists():
    assert callable(MOFScriptObject.__init__)


def test_mofscriptobject_constructor_args():
    sig = inspect.signature(MOFScriptObject.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::mofscriptimport_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptImport)


def test_mofscriptmodel::mofscriptimport_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptImport.__init__)


def test_mofscriptmodel::mofscriptimport_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptImport.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "importSemantics" in params, "Missing parameter 'importSemantics'"
    assert "uri" in params, "Missing parameter 'uri'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel::mofscriptimport_has_type():
    assert hasattr(MOFScriptModel::MOFScriptImport, "type")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptImport.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptimport_has_importSemantics():
    assert hasattr(MOFScriptModel::MOFScriptImport, "importSemantics")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptImport.__mro__:
        if "importSemantics" in klass.__dict__:
            descriptor = klass.__dict__["importSemantics"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptimport_has_uri():
    assert hasattr(MOFScriptModel::MOFScriptImport, "uri")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptImport.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptimport_has_name():
    assert hasattr(MOFScriptModel::MOFScriptImport, "name")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptImport.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::createexpressionparameter_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::CreateExpressionParameter)


def test_mofscriptmodel::createexpressionparameter_constructor_exists():
    assert callable(MOFScriptModel::CreateExpressionParameter.__init__)


def test_mofscriptmodel::createexpressionparameter_constructor_args():
    sig = inspect.signature(MOFScriptModel::CreateExpressionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel::createexpressionparameter_has_name():
    assert hasattr(MOFScriptModel::CreateExpressionParameter, "name")
    descriptor = None
    for klass in MOFScriptModel::CreateExpressionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::mofscriptspecification_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptSpecification)


def test_mofscriptmodel::mofscriptspecification_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptSpecification.__init__)


def test_mofscriptmodel::mofscriptspecification_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptSpecification.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::expression_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::Expression)


def test_mofscriptmodel::expression_constructor_exists():
    assert callable(MOFScriptModel::Expression.__init__)


def test_mofscriptmodel::expression_constructor_args():
    sig = inspect.signature(MOFScriptModel::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::mofscriptcomment_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptComment)


def test_mofscriptmodel::mofscriptcomment_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptComment.__init__)


def test_mofscriptmodel::mofscriptcomment_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptComment.__init__)
    params = list(sig.parameters.keys())
    assert "singleLine" in params, "Missing parameter 'singleLine'"
    assert "commentText" in params, "Missing parameter 'commentText'"
    assert "docStyle" in params, "Missing parameter 'docStyle'"

def test_mofscriptmodel::mofscriptcomment_has_singleLine():
    assert hasattr(MOFScriptModel::MOFScriptComment, "singleLine")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptComment.__mro__:
        if "singleLine" in klass.__dict__:
            descriptor = klass.__dict__["singleLine"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptcomment_has_commentText():
    assert hasattr(MOFScriptModel::MOFScriptComment, "commentText")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptComment.__mro__:
        if "commentText" in klass.__dict__:
            descriptor = klass.__dict__["commentText"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptcomment_has_docStyle():
    assert hasattr(MOFScriptModel::MOFScriptComment, "docStyle")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptComment.__mro__:
        if "docStyle" in klass.__dict__:
            descriptor = klass.__dict__["docStyle"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::VariableDeclaration)


def test_mofscriptmodel::variabledeclaration_constructor_exists():
    assert callable(MOFScriptModel::VariableDeclaration.__init__)


def test_mofscriptmodel::variabledeclaration_constructor_args():
    sig = inspect.signature(MOFScriptModel::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mofscriptmodel::variabledeclaration_has_constant():
    assert hasattr(MOFScriptModel::VariableDeclaration, "constant")
    descriptor = None
    for klass in MOFScriptModel::VariableDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::variabledeclaration_has_type():
    assert hasattr(MOFScriptModel::VariableDeclaration, "type")
    descriptor = None
    for klass in MOFScriptModel::VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::variabledeclaration_has_name():
    assert hasattr(MOFScriptModel::VariableDeclaration, "name")
    descriptor = None
    for klass in MOFScriptModel::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::mofscriptstatementowner_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptStatementOwner)


def test_mofscriptmodel::mofscriptstatementowner_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptStatementOwner.__init__)


def test_mofscriptmodel::mofscriptstatementowner_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptStatementOwner.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::mofscriptparameter_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptParameter)


def test_mofscriptmodel::mofscriptparameter_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptParameter.__init__)


def test_mofscriptmodel::mofscriptparameter_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "typePrefix" in params, "Missing parameter 'typePrefix'"

def test_mofscriptmodel::mofscriptparameter_has_name():
    assert hasattr(MOFScriptModel::MOFScriptParameter, "name")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptparameter_has_type():
    assert hasattr(MOFScriptModel::MOFScriptParameter, "type")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptparameter_has_direction():
    assert hasattr(MOFScriptModel::MOFScriptParameter, "direction")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscriptparameter_has_typePrefix():
    assert hasattr(MOFScriptModel::MOFScriptParameter, "typePrefix")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptParameter.__mro__:
        if "typePrefix" in klass.__dict__:
            descriptor = klass.__dict__["typePrefix"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::mofscripttransformation_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptTransformation)


def test_mofscriptmodel::mofscripttransformation_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptTransformation.__init__)


def test_mofscriptmodel::mofscripttransformation_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "extendsName" in params, "Missing parameter 'extendsName'"

def test_mofscriptmodel::mofscripttransformation_has_name():
    assert hasattr(MOFScriptModel::MOFScriptTransformation, "name")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptTransformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::mofscripttransformation_has_extendsName():
    assert hasattr(MOFScriptModel::MOFScriptTransformation, "extendsName")
    descriptor = None
    for klass in MOFScriptModel::MOFScriptTransformation.__mro__:
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



def test_mofscriptmodel::advice_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::Advice)


def test_mofscriptmodel::advice_constructor_exists():
    assert callable(MOFScriptModel::Advice.__init__)


def test_mofscriptmodel::advice_constructor_args():
    sig = inspect.signature(MOFScriptModel::Advice.__init__)
    params = list(sig.parameters.keys())
    assert "pointCutRef" in params, "Missing parameter 'pointCutRef'"
    assert "name" in params, "Missing parameter 'name'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "code" in params, "Missing parameter 'code'"

def test_mofscriptmodel::advice_has_pointCutRef():
    assert hasattr(MOFScriptModel::Advice, "pointCutRef")
    descriptor = None
    for klass in MOFScriptModel::Advice.__mro__:
        if "pointCutRef" in klass.__dict__:
            descriptor = klass.__dict__["pointCutRef"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::advice_has_name():
    assert hasattr(MOFScriptModel::Advice, "name")
    descriptor = None
    for klass in MOFScriptModel::Advice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::advice_has_operator():
    assert hasattr(MOFScriptModel::Advice, "operator")
    descriptor = None
    for klass in MOFScriptModel::Advice.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::advice_has_code():
    assert hasattr(MOFScriptModel::Advice, "code")
    descriptor = None
    for klass in MOFScriptModel::Advice.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_mofscriptmodel::mofscriptstatement_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::MOFScriptStatement)


def test_mofscriptmodel::mofscriptstatement_constructor_exists():
    assert callable(MOFScriptModel::MOFScriptStatement.__init__)


def test_mofscriptmodel::mofscriptstatement_constructor_args():
    sig = inspect.signature(MOFScriptModel::MOFScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_mofscriptmodel::transformationrule_is_not_abstract():
    assert not inspect.isabstract(MOFScriptModel::TransformationRule)


def test_mofscriptmodel::transformationrule_constructor_exists():
    assert callable(MOFScriptModel::TransformationRule.__init__)


def test_mofscriptmodel::transformationrule_constructor_args():
    sig = inspect.signature(MOFScriptModel::TransformationRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEntryPoint" in params, "Missing parameter 'isEntryPoint'"
    assert "name" in params, "Missing parameter 'name'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "return_" in params, "Missing parameter 'return_'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_mofscriptmodel::transformationrule_has_isEntryPoint():
    assert hasattr(MOFScriptModel::TransformationRule, "isEntryPoint")
    descriptor = None
    for klass in MOFScriptModel::TransformationRule.__mro__:
        if "isEntryPoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntryPoint"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::transformationrule_has_name():
    assert hasattr(MOFScriptModel::TransformationRule, "name")
    descriptor = None
    for klass in MOFScriptModel::TransformationRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::transformationrule_has_accessLevel():
    assert hasattr(MOFScriptModel::TransformationRule, "accessLevel")
    descriptor = None
    for klass in MOFScriptModel::TransformationRule.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::transformationrule_has_return_():
    assert hasattr(MOFScriptModel::TransformationRule, "return_")
    descriptor = None
    for klass in MOFScriptModel::TransformationRule.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_mofscriptmodel::transformationrule_has_isAbstract():
    assert hasattr(MOFScriptModel::TransformationRule, "isAbstract")
    descriptor = None
    for klass in MOFScriptModel::TransformationRule.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_parameterdirection_exists():
    # Check that the Enumeration exists
    assert ParameterDirection is not None

def test_parameterdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirection]
    expected_literals = [
        "OUT",
        "INOUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirection"

def test_importsemantics_exists():
    # Check that the Enumeration exists
    assert ImportSemantics is not None

def test_importsemantics_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportSemantics]
    expected_literals = [
        "IMPORT",
        "ACCESS",
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
        "TARGET",
        "EXECUTE",
        "CALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PointCutOperator"

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

def test_adviceoperator_exists():
    # Check that the Enumeration exists
    assert AdviceOperator is not None

def test_adviceoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdviceOperator]
    expected_literals = [
        "BEFORE",
        "AFTER",
        "AROUND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdviceOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "PLUS",
        "MULT",
        "MINUS",
        "DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "AND",
        "OR",
        "NONE",
        "NOT",
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
        "NULL",
        "BOOLEAN",
        "REAL",
        "STRING",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralType"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "OR",
        "LE",
        "AND",
        "EQ",
        "LT",
        "GT",
        "GE",
        "NE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PRIVATE",
        "PROTECTED",
        "NONE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevel"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "EQ",
        "PLUS_EQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_pointcutcombinationoperator_exists():
    # Check that the Enumeration exists
    assert PointCutCombinationOperator is not None

def test_pointcutcombinationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PointCutCombinationOperator]
    expected_literals = [
        "AND",
        "OR",
        "XOR",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PointCutCombinationOperator"


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
Trace_strategy = st.builds(
    Trace,
)
MOFScriptModel::M2MTrace_strategy = st.builds(
    MOFScriptModel::M2MTrace,
    id=
        safe_text,
    name=
        safe_text
)
MOFScriptModel::PointCutExpression_strategy = st.builds(
    MOFScriptModel::PointCutExpression,
    operator=
        safe_text,
    combinationOperator=
        safe_text,
    expressionString=
        safe_text
)
MOFScriptModel::PointCut_strategy = st.builds(
    MOFScriptModel::PointCut,
    typeMatch=
        safe_text,
    name=
        safe_text
)
MOFScriptTransformation_strategy = st.builds(
    MOFScriptTransformation,
)
MOFScriptModel::MOFScriptAspect_strategy = st.builds(
    MOFScriptModel::MOFScriptAspect,
)
SimpleExpression_strategy = st.builds(
    SimpleExpression,
)
MOFScriptModel::FunctionCall_strategy = st.builds(
    MOFScriptModel::FunctionCall,
    name=
        safe_text,
    transformationContext=
        safe_text,
    isSuperCall=
        st.booleans()
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
MOFScriptModel::SelectExpression_strategy = st.builds(
    MOFScriptModel::SelectExpression,
    variable=
        safe_text,
    type=
        safe_text
)
MOFScriptModel::ArithmeticExpression_strategy = st.builds(
    MOFScriptModel::ArithmeticExpression,
    operator=
        safe_text
)
MOFScriptModel::Reference_strategy = st.builds(
    MOFScriptModel::Reference,
    name=
        safe_text
)
MOFScriptModel::Literal_strategy = st.builds(
    MOFScriptModel::Literal,
    value=
        safe_text,
    type=
        safe_text
)
MOFScriptModel::SimpleExpression_strategy = st.builds(
    MOFScriptModel::SimpleExpression,
)
MOFScriptStatement_strategy = st.builds(
    MOFScriptStatement,
)
MOFScriptModel::WhileStatement_strategy = st.builds(
    MOFScriptModel::WhileStatement,
)
MOFScriptModel::DebugStatement_strategy = st.builds(
    MOFScriptModel::DebugStatement,
    specification=
        safe_text,
    vars=
        safe_text
)
MOFScriptModel::BreakStatement_strategy = st.builds(
    MOFScriptModel::BreakStatement,
)
MOFScriptModel::Trace_strategy = st.builds(
    MOFScriptModel::Trace,
)
MOFScriptModel::FunctionCallStatement_strategy = st.builds(
    MOFScriptModel::FunctionCallStatement,
)
MOFScriptModel::GeneralAssignment_strategy = st.builds(
    MOFScriptModel::GeneralAssignment,
    name=
        safe_text,
    operator=
        safe_text
)
MOFScriptModel::CreateStatement_strategy = st.builds(
    MOFScriptModel::CreateStatement,
    name=
        safe_text,
    type=
        safe_text
)
MOFScriptModel::VariableDeclarationStatement_strategy = st.builds(
    MOFScriptModel::VariableDeclarationStatement,
)
MOFScriptModel::ResultAssignment_strategy = st.builds(
    MOFScriptModel::ResultAssignment,
    operator=
        safe_text,
    resultPart=
        safe_text
)
MOFScriptModel::IfStatement_strategy = st.builds(
    MOFScriptModel::IfStatement,
)
MOFScriptModel::PrintStatement_strategy = st.builds(
    MOFScriptModel::PrintStatement,
    printCommand=
        safe_text,
    context=
        safe_text
)
MOFScriptModel::FileStatement_strategy = st.builds(
    MOFScriptModel::FileStatement,
    append=
        st.booleans(),
    fileReference=
        safe_text,
    use=
        st.booleans()
)
MOFScriptModel::ReturnStatement_strategy = st.builds(
    MOFScriptModel::ReturnStatement,
)
MOFScriptModel::IteratorStatement_strategy = st.builds(
    MOFScriptModel::IteratorStatement,
    type=
        safe_text,
    variable=
        safe_text
)
MOFScriptModel::MOFScriptObject_strategy = st.builds(
    MOFScriptModel::MOFScriptObject,
    column=
        st.integers(),
    line=
        st.integers()
)
MOFScriptModel::StatementBlock_strategy = st.builds(
    MOFScriptModel::StatementBlock,
    id=
        safe_text,
    reference=
        safe_text,
    protected=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
MOFScriptModel::ComparisonExpression_strategy = st.builds(
    MOFScriptModel::ComparisonExpression,
    operator=
        safe_text
)
MOFScriptModel::LogicalExpression_strategy = st.builds(
    MOFScriptModel::LogicalExpression,
    operator=
        safe_text
)
MOFScriptModel::CreateExpression_strategy = st.builds(
    MOFScriptModel::CreateExpression,
    type=
        safe_text
)
MOFScriptModel::ValueExpression_strategy = st.builds(
    MOFScriptModel::ValueExpression,
    specification=
        safe_text
)
MOFScriptObject_strategy = st.builds(
    MOFScriptObject,
)
MOFScriptModel::MOFScriptImport_strategy = st.builds(
    MOFScriptModel::MOFScriptImport,
    type=
        safe_text,
    importSemantics=
        safe_text,
    uri=
        safe_text,
    name=
        safe_text
)
MOFScriptModel::CreateExpressionParameter_strategy = st.builds(
    MOFScriptModel::CreateExpressionParameter,
    name=
        safe_text
)
MOFScriptModel::MOFScriptSpecification_strategy = st.builds(
    MOFScriptModel::MOFScriptSpecification,
)
MOFScriptModel::Expression_strategy = st.builds(
    MOFScriptModel::Expression,
)
MOFScriptModel::MOFScriptComment_strategy = st.builds(
    MOFScriptModel::MOFScriptComment,
    singleLine=
        st.booleans(),
    commentText=
        safe_text,
    docStyle=
        st.booleans()
)
MOFScriptModel::VariableDeclaration_strategy = st.builds(
    MOFScriptModel::VariableDeclaration,
    constant=
        st.booleans(),
    type=
        safe_text,
    name=
        safe_text
)
MOFScriptModel::MOFScriptStatementOwner_strategy = st.builds(
    MOFScriptModel::MOFScriptStatementOwner,
)
MOFScriptModel::MOFScriptParameter_strategy = st.builds(
    MOFScriptModel::MOFScriptParameter,
    name=
        safe_text,
    type=
        safe_text,
    direction=
        safe_text,
    typePrefix=
        safe_text
)
MOFScriptModel::MOFScriptTransformation_strategy = st.builds(
    MOFScriptModel::MOFScriptTransformation,
    name=
        safe_text,
    extendsName=
        safe_text
)
MOFScriptStatementOwner_strategy = st.builds(
    MOFScriptStatementOwner,
)
MOFScriptModel::Advice_strategy = st.builds(
    MOFScriptModel::Advice,
    pointCutRef=
        safe_text,
    name=
        safe_text,
    operator=
        safe_text,
    code=
        safe_text
)
MOFScriptModel::MOFScriptStatement_strategy = st.builds(
    MOFScriptModel::MOFScriptStatement,
)
MOFScriptModel::TransformationRule_strategy = st.builds(
    MOFScriptModel::TransformationRule,
    isEntryPoint=
        st.booleans(),
    name=
        safe_text,
    accessLevel=
        safe_text,
    return_=
        safe_text,
    isAbstract=
        st.booleans()
)

@given(instance=Trace_strategy)
@settings(max_examples=50)
def test_trace_instantiation(instance):
    assert isinstance(instance, Trace)

@given(instance=MOFScriptModel::M2MTrace_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::m2mtrace_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::M2MTrace)

@given(instance=MOFScriptModel::M2MTrace_strategy)
def test_mofscriptmodel::m2mtrace_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MOFScriptModel::M2MTrace_strategy)
def test_mofscriptmodel::m2mtrace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MOFScriptModel::M2MTrace_strategy)
def test_mofscriptmodel::m2mtrace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::M2MTrace_strategy)
def test_mofscriptmodel::m2mtrace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::PointCutExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::pointcutexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::PointCutExpression)

@given(instance=MOFScriptModel::PointCutExpression_strategy)
def test_mofscriptmodel::pointcutexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::PointCutExpression_strategy)
def test_mofscriptmodel::pointcutexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::PointCutExpression_strategy)
def test_mofscriptmodel::pointcutexpression_combinationOperator_type(instance):
    assert isinstance(instance.combinationOperator, str)


@given(instance=MOFScriptModel::PointCutExpression_strategy)
def test_mofscriptmodel::pointcutexpression_combinationOperator_setter(instance):
    original = instance.combinationOperator
    instance.combinationOperator = original
    assert instance.combinationOperator == original

@given(instance=MOFScriptModel::PointCutExpression_strategy)
def test_mofscriptmodel::pointcutexpression_expressionString_type(instance):
    assert isinstance(instance.expressionString, str)


@given(instance=MOFScriptModel::PointCutExpression_strategy)
def test_mofscriptmodel::pointcutexpression_expressionString_setter(instance):
    original = instance.expressionString
    instance.expressionString = original
    assert instance.expressionString == original

@given(instance=MOFScriptModel::PointCut_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::pointcut_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::PointCut)

@given(instance=MOFScriptModel::PointCut_strategy)
def test_mofscriptmodel::pointcut_typeMatch_type(instance):
    assert isinstance(instance.typeMatch, str)


@given(instance=MOFScriptModel::PointCut_strategy)
def test_mofscriptmodel::pointcut_typeMatch_setter(instance):
    original = instance.typeMatch
    instance.typeMatch = original
    assert instance.typeMatch == original

@given(instance=MOFScriptModel::PointCut_strategy)
def test_mofscriptmodel::pointcut_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::PointCut_strategy)
def test_mofscriptmodel::pointcut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptTransformation_strategy)
@settings(max_examples=50)
def test_mofscripttransformation_instantiation(instance):
    assert isinstance(instance, MOFScriptTransformation)

@given(instance=MOFScriptModel::MOFScriptAspect_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptaspect_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptAspect)

@given(instance=SimpleExpression_strategy)
@settings(max_examples=50)
def test_simpleexpression_instantiation(instance):
    assert isinstance(instance, SimpleExpression)

@given(instance=MOFScriptModel::FunctionCall_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::functioncall_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::FunctionCall)

@given(instance=MOFScriptModel::FunctionCall_strategy)
def test_mofscriptmodel::functioncall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::FunctionCall_strategy)
def test_mofscriptmodel::functioncall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::FunctionCall_strategy)
def test_mofscriptmodel::functioncall_transformationContext_type(instance):
    assert isinstance(instance.transformationContext, str)


@given(instance=MOFScriptModel::FunctionCall_strategy)
def test_mofscriptmodel::functioncall_transformationContext_setter(instance):
    original = instance.transformationContext
    instance.transformationContext = original
    assert instance.transformationContext == original

@given(instance=MOFScriptModel::FunctionCall_strategy)
def test_mofscriptmodel::functioncall_isSuperCall_type(instance):
    assert isinstance(instance.isSuperCall, bool)


@given(instance=MOFScriptModel::FunctionCall_strategy)
def test_mofscriptmodel::functioncall_isSuperCall_setter(instance):
    original = instance.isSuperCall
    instance.isSuperCall = original
    assert instance.isSuperCall == original

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=MOFScriptModel::SelectExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::selectexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::SelectExpression)

@given(instance=MOFScriptModel::SelectExpression_strategy)
def test_mofscriptmodel::selectexpression_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=MOFScriptModel::SelectExpression_strategy)
def test_mofscriptmodel::selectexpression_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=MOFScriptModel::SelectExpression_strategy)
def test_mofscriptmodel::selectexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::SelectExpression_strategy)
def test_mofscriptmodel::selectexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::ArithmeticExpression)

@given(instance=MOFScriptModel::ArithmeticExpression_strategy)
def test_mofscriptmodel::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::ArithmeticExpression_strategy)
def test_mofscriptmodel::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::Reference_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::reference_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::Reference)

@given(instance=MOFScriptModel::Reference_strategy)
def test_mofscriptmodel::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::Reference_strategy)
def test_mofscriptmodel::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::Literal_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::literal_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::Literal)

@given(instance=MOFScriptModel::Literal_strategy)
def test_mofscriptmodel::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MOFScriptModel::Literal_strategy)
def test_mofscriptmodel::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MOFScriptModel::Literal_strategy)
def test_mofscriptmodel::literal_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::Literal_strategy)
def test_mofscriptmodel::literal_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::SimpleExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::simpleexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::SimpleExpression)

@given(instance=MOFScriptStatement_strategy)
@settings(max_examples=50)
def test_mofscriptstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptStatement)

@given(instance=MOFScriptModel::WhileStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::whilestatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::WhileStatement)

@given(instance=MOFScriptModel::DebugStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::debugstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::DebugStatement)

@given(instance=MOFScriptModel::DebugStatement_strategy)
def test_mofscriptmodel::debugstatement_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=MOFScriptModel::DebugStatement_strategy)
def test_mofscriptmodel::debugstatement_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=MOFScriptModel::DebugStatement_strategy)
def test_mofscriptmodel::debugstatement_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=MOFScriptModel::DebugStatement_strategy)
def test_mofscriptmodel::debugstatement_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=MOFScriptModel::BreakStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::breakstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::BreakStatement)

@given(instance=MOFScriptModel::Trace_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::trace_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::Trace)

@given(instance=MOFScriptModel::FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::functioncallstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::FunctionCallStatement)

@given(instance=MOFScriptModel::GeneralAssignment_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::generalassignment_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::GeneralAssignment)

@given(instance=MOFScriptModel::GeneralAssignment_strategy)
def test_mofscriptmodel::generalassignment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::GeneralAssignment_strategy)
def test_mofscriptmodel::generalassignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::GeneralAssignment_strategy)
def test_mofscriptmodel::generalassignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::GeneralAssignment_strategy)
def test_mofscriptmodel::generalassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::CreateStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::createstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::CreateStatement)

@given(instance=MOFScriptModel::CreateStatement_strategy)
def test_mofscriptmodel::createstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::CreateStatement_strategy)
def test_mofscriptmodel::createstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::CreateStatement_strategy)
def test_mofscriptmodel::createstatement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::CreateStatement_strategy)
def test_mofscriptmodel::createstatement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::VariableDeclarationStatement)

@given(instance=MOFScriptModel::ResultAssignment_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::resultassignment_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::ResultAssignment)

@given(instance=MOFScriptModel::ResultAssignment_strategy)
def test_mofscriptmodel::resultassignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::ResultAssignment_strategy)
def test_mofscriptmodel::resultassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::ResultAssignment_strategy)
def test_mofscriptmodel::resultassignment_resultPart_type(instance):
    assert isinstance(instance.resultPart, str)


@given(instance=MOFScriptModel::ResultAssignment_strategy)
def test_mofscriptmodel::resultassignment_resultPart_setter(instance):
    original = instance.resultPart
    instance.resultPart = original
    assert instance.resultPart == original

@given(instance=MOFScriptModel::IfStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::ifstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::IfStatement)

@given(instance=MOFScriptModel::PrintStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::printstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::PrintStatement)

@given(instance=MOFScriptModel::PrintStatement_strategy)
def test_mofscriptmodel::printstatement_printCommand_type(instance):
    assert isinstance(instance.printCommand, str)


@given(instance=MOFScriptModel::PrintStatement_strategy)
def test_mofscriptmodel::printstatement_printCommand_setter(instance):
    original = instance.printCommand
    instance.printCommand = original
    assert instance.printCommand == original

@given(instance=MOFScriptModel::PrintStatement_strategy)
def test_mofscriptmodel::printstatement_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=MOFScriptModel::PrintStatement_strategy)
def test_mofscriptmodel::printstatement_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=MOFScriptModel::FileStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::filestatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::FileStatement)

@given(instance=MOFScriptModel::FileStatement_strategy)
def test_mofscriptmodel::filestatement_append_type(instance):
    assert isinstance(instance.append, bool)


@given(instance=MOFScriptModel::FileStatement_strategy)
def test_mofscriptmodel::filestatement_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original

@given(instance=MOFScriptModel::FileStatement_strategy)
def test_mofscriptmodel::filestatement_fileReference_type(instance):
    assert isinstance(instance.fileReference, str)


@given(instance=MOFScriptModel::FileStatement_strategy)
def test_mofscriptmodel::filestatement_fileReference_setter(instance):
    original = instance.fileReference
    instance.fileReference = original
    assert instance.fileReference == original

@given(instance=MOFScriptModel::FileStatement_strategy)
def test_mofscriptmodel::filestatement_use_type(instance):
    assert isinstance(instance.use, bool)


@given(instance=MOFScriptModel::FileStatement_strategy)
def test_mofscriptmodel::filestatement_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=MOFScriptModel::ReturnStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::returnstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::ReturnStatement)

@given(instance=MOFScriptModel::IteratorStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::iteratorstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::IteratorStatement)

@given(instance=MOFScriptModel::IteratorStatement_strategy)
def test_mofscriptmodel::iteratorstatement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::IteratorStatement_strategy)
def test_mofscriptmodel::iteratorstatement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::IteratorStatement_strategy)
def test_mofscriptmodel::iteratorstatement_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=MOFScriptModel::IteratorStatement_strategy)
def test_mofscriptmodel::iteratorstatement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=MOFScriptModel::MOFScriptObject_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptobject_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptObject)

@given(instance=MOFScriptModel::MOFScriptObject_strategy)
def test_mofscriptmodel::mofscriptobject_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=MOFScriptModel::MOFScriptObject_strategy)
def test_mofscriptmodel::mofscriptobject_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=MOFScriptModel::MOFScriptObject_strategy)
def test_mofscriptmodel::mofscriptobject_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=MOFScriptModel::MOFScriptObject_strategy)
def test_mofscriptmodel::mofscriptobject_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=MOFScriptModel::StatementBlock_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::statementblock_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::StatementBlock)

@given(instance=MOFScriptModel::StatementBlock_strategy)
def test_mofscriptmodel::statementblock_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MOFScriptModel::StatementBlock_strategy)
def test_mofscriptmodel::statementblock_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MOFScriptModel::StatementBlock_strategy)
def test_mofscriptmodel::statementblock_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=MOFScriptModel::StatementBlock_strategy)
def test_mofscriptmodel::statementblock_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=MOFScriptModel::StatementBlock_strategy)
def test_mofscriptmodel::statementblock_protected_type(instance):
    assert isinstance(instance.protected, bool)


@given(instance=MOFScriptModel::StatementBlock_strategy)
def test_mofscriptmodel::statementblock_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=MOFScriptModel::ComparisonExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::comparisonexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::ComparisonExpression)

@given(instance=MOFScriptModel::ComparisonExpression_strategy)
def test_mofscriptmodel::comparisonexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::ComparisonExpression_strategy)
def test_mofscriptmodel::comparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::LogicalExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::logicalexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::LogicalExpression)

@given(instance=MOFScriptModel::LogicalExpression_strategy)
def test_mofscriptmodel::logicalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::LogicalExpression_strategy)
def test_mofscriptmodel::logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::CreateExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::createexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::CreateExpression)

@given(instance=MOFScriptModel::CreateExpression_strategy)
def test_mofscriptmodel::createexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::CreateExpression_strategy)
def test_mofscriptmodel::createexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::ValueExpression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::valueexpression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::ValueExpression)

@given(instance=MOFScriptModel::ValueExpression_strategy)
def test_mofscriptmodel::valueexpression_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=MOFScriptModel::ValueExpression_strategy)
def test_mofscriptmodel::valueexpression_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=MOFScriptObject_strategy)
@settings(max_examples=50)
def test_mofscriptobject_instantiation(instance):
    assert isinstance(instance, MOFScriptObject)

@given(instance=MOFScriptModel::MOFScriptImport_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptimport_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptImport)

@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_importSemantics_type(instance):
    assert isinstance(instance.importSemantics, str)


@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_importSemantics_setter(instance):
    original = instance.importSemantics
    instance.importSemantics = original
    assert instance.importSemantics == original

@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::MOFScriptImport_strategy)
def test_mofscriptmodel::mofscriptimport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::CreateExpressionParameter_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::createexpressionparameter_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::CreateExpressionParameter)

@given(instance=MOFScriptModel::CreateExpressionParameter_strategy)
def test_mofscriptmodel::createexpressionparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::CreateExpressionParameter_strategy)
def test_mofscriptmodel::createexpressionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::MOFScriptSpecification_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptspecification_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptSpecification)

@given(instance=MOFScriptModel::Expression_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::expression_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::Expression)

@given(instance=MOFScriptModel::MOFScriptComment_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptcomment_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptComment)

@given(instance=MOFScriptModel::MOFScriptComment_strategy)
def test_mofscriptmodel::mofscriptcomment_singleLine_type(instance):
    assert isinstance(instance.singleLine, bool)


@given(instance=MOFScriptModel::MOFScriptComment_strategy)
def test_mofscriptmodel::mofscriptcomment_singleLine_setter(instance):
    original = instance.singleLine
    instance.singleLine = original
    assert instance.singleLine == original

@given(instance=MOFScriptModel::MOFScriptComment_strategy)
def test_mofscriptmodel::mofscriptcomment_commentText_type(instance):
    assert isinstance(instance.commentText, str)


@given(instance=MOFScriptModel::MOFScriptComment_strategy)
def test_mofscriptmodel::mofscriptcomment_commentText_setter(instance):
    original = instance.commentText
    instance.commentText = original
    assert instance.commentText == original

@given(instance=MOFScriptModel::MOFScriptComment_strategy)
def test_mofscriptmodel::mofscriptcomment_docStyle_type(instance):
    assert isinstance(instance.docStyle, bool)


@given(instance=MOFScriptModel::MOFScriptComment_strategy)
def test_mofscriptmodel::mofscriptcomment_docStyle_setter(instance):
    original = instance.docStyle
    instance.docStyle = original
    assert instance.docStyle == original

@given(instance=MOFScriptModel::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::variabledeclaration_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::VariableDeclaration)

@given(instance=MOFScriptModel::VariableDeclaration_strategy)
def test_mofscriptmodel::variabledeclaration_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=MOFScriptModel::VariableDeclaration_strategy)
def test_mofscriptmodel::variabledeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=MOFScriptModel::VariableDeclaration_strategy)
def test_mofscriptmodel::variabledeclaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::VariableDeclaration_strategy)
def test_mofscriptmodel::variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::VariableDeclaration_strategy)
def test_mofscriptmodel::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::VariableDeclaration_strategy)
def test_mofscriptmodel::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::MOFScriptStatementOwner_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptstatementowner_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptStatementOwner)

@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptparameter_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptParameter)

@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_typePrefix_type(instance):
    assert isinstance(instance.typePrefix, str)


@given(instance=MOFScriptModel::MOFScriptParameter_strategy)
def test_mofscriptmodel::mofscriptparameter_typePrefix_setter(instance):
    original = instance.typePrefix
    instance.typePrefix = original
    assert instance.typePrefix == original

@given(instance=MOFScriptModel::MOFScriptTransformation_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscripttransformation_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptTransformation)

@given(instance=MOFScriptModel::MOFScriptTransformation_strategy)
def test_mofscriptmodel::mofscripttransformation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::MOFScriptTransformation_strategy)
def test_mofscriptmodel::mofscripttransformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::MOFScriptTransformation_strategy)
def test_mofscriptmodel::mofscripttransformation_extendsName_type(instance):
    assert isinstance(instance.extendsName, str)


@given(instance=MOFScriptModel::MOFScriptTransformation_strategy)
def test_mofscriptmodel::mofscripttransformation_extendsName_setter(instance):
    original = instance.extendsName
    instance.extendsName = original
    assert instance.extendsName == original

@given(instance=MOFScriptStatementOwner_strategy)
@settings(max_examples=50)
def test_mofscriptstatementowner_instantiation(instance):
    assert isinstance(instance, MOFScriptStatementOwner)

@given(instance=MOFScriptModel::Advice_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::advice_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::Advice)

@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_pointCutRef_type(instance):
    assert isinstance(instance.pointCutRef, str)


@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_pointCutRef_setter(instance):
    original = instance.pointCutRef
    instance.pointCutRef = original
    assert instance.pointCutRef == original

@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=MOFScriptModel::Advice_strategy)
def test_mofscriptmodel::advice_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=MOFScriptModel::MOFScriptStatement_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::mofscriptstatement_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::MOFScriptStatement)

@given(instance=MOFScriptModel::TransformationRule_strategy)
@settings(max_examples=50)
def test_mofscriptmodel::transformationrule_instantiation(instance):
    assert isinstance(instance, MOFScriptModel::TransformationRule)

@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_isEntryPoint_type(instance):
    assert isinstance(instance.isEntryPoint, bool)


@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_isEntryPoint_setter(instance):
    original = instance.isEntryPoint
    instance.isEntryPoint = original
    assert instance.isEntryPoint == original

@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=MOFScriptModel::TransformationRule_strategy)
def test_mofscriptmodel::transformationrule_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original
