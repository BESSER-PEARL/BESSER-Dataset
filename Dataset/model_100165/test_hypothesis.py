import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Item,
    plSql::ProcedureDeclaration,
    plSql::Item,
    plSql::ProcedureContent,
    plSql::ProcedureInvokerRightsClause,
    plSql::ParameterSequence,
    NameDeclaration,
    CompilationUnit,
    plSql::Package,
    plSql::Procedure,
    plSql::CompilationUnit,
    plSql::NameDeclaration,
    plSql::Name,
    plSql::QualifiedName,
    plSql::LoopVariableDeclaration,
    LoopStatement,
    plSql::ForLoopStatement,
    plSql::WhileLoopStatement,
    plSql::BasicLoopStatement,
    plSql::IfStatementElseBranch,
    plSql::IfStatementElsifBranch,
    FetchStatementIntoClause,
    plSql::FetchStatementBulkIntoClause,
    plSql::FetchStatementSingleIntoClause,
    plSql::FetchStatementIntoClause,
    plSql::CaseStatementElseBranch,
    AssignmentTarget,
    plSql::VariableAssignmentTarget,
    plSql::AssignmentTarget,
    Statement,
    plSql::BlockStatement,
    plSql::IfStatement,
    plSql::LoopStatement,
    plSql::GotoStatement,
    plSql::ExitStatement,
    plSql::RaiseStatement,
    plSql::FetchStatement,
    plSql::CloseStatement,
    plSql::NullStatement,
    plSql::ReturnStatement,
    plSql::ContinueStatement,
    plSql::AssignmentStatement,
    plSql::Label,
    plSql::VariableRef,
    Expression,
    plSql::BooleanLiteralExpression,
    plSql::VariableRefExpression,
    plSql::StringLiteralExpression,
    plSql::NullLiteralExpression,
    plSql::IntLiteralExpression,
    plSql::VariableValue,
    plSql::CaseStatementWhenBranch,
    plSql::CaseStatement,
    plSql::Statement,
    FunctionContent,
    plSql::FunctionImplementation,
    plSql::StatementBody,
    plSql::DeclareSection,
    ProcedureContent,
    Pragma,
    plSql::PragmaTimestamp,
    plSql::PragmaRestrictReferences,
    plSql::Pragma,
    FunctionClause,
    plSql::ResultCacheClause,
    plSql::DeterministicClause,
    plSql::PipelinedClause,
    plSql::FunctionInvokerRightsClause,
    ItemDeclaration,
    plSql::VariableDeclaration,
    plSql::ExternalProcedureDeclaration,
    plSql::ItemDeclaration,
    plSql::ParameterDeclaration,
    plSql::FunctionContent,
    plSql::FunctionClause,
    plSql::Function,
    plSql::ProcedureImplementation,
    plSql::Expression,
    plSql::ParameterValue,
    plSql::ProcedureDefinition,
    InvokerRight,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_plsql::proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::ProcedureDeclaration)


def test_plsql::proceduredeclaration_constructor_exists():
    assert callable(plSql::ProcedureDeclaration.__init__)


def test_plsql::proceduredeclaration_constructor_args():
    sig = inspect.signature(plSql::ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql::proceduredeclaration_has_name():
    assert hasattr(plSql::ProcedureDeclaration, "name")
    descriptor = None
    for klass in plSql::ProcedureDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql::item_is_not_abstract():
    assert not inspect.isabstract(plSql::Item)


def test_plsql::item_constructor_exists():
    assert callable(plSql::Item.__init__)


def test_plsql::item_constructor_args():
    sig = inspect.signature(plSql::Item.__init__)
    params = list(sig.parameters.keys())



def test_plsql::procedurecontent_is_not_abstract():
    assert not inspect.isabstract(plSql::ProcedureContent)


def test_plsql::procedurecontent_constructor_exists():
    assert callable(plSql::ProcedureContent.__init__)


def test_plsql::procedurecontent_constructor_args():
    sig = inspect.signature(plSql::ProcedureContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql::procedureinvokerrightsclause_is_not_abstract():
    assert not inspect.isabstract(plSql::ProcedureInvokerRightsClause)


def test_plsql::procedureinvokerrightsclause_constructor_exists():
    assert callable(plSql::ProcedureInvokerRightsClause.__init__)


def test_plsql::procedureinvokerrightsclause_constructor_args():
    sig = inspect.signature(plSql::ProcedureInvokerRightsClause.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_plsql::procedureinvokerrightsclause_has_right():
    assert hasattr(plSql::ProcedureInvokerRightsClause, "right")
    descriptor = None
    for klass in plSql::ProcedureInvokerRightsClause.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_plsql::parametersequence_is_not_abstract():
    assert not inspect.isabstract(plSql::ParameterSequence)


def test_plsql::parametersequence_constructor_exists():
    assert callable(plSql::ParameterSequence.__init__)


def test_plsql::parametersequence_constructor_args():
    sig = inspect.signature(plSql::ParameterSequence.__init__)
    params = list(sig.parameters.keys())



def test_namedeclaration_is_not_abstract():
    assert not inspect.isabstract(NameDeclaration)


def test_namedeclaration_constructor_exists():
    assert callable(NameDeclaration.__init__)


def test_namedeclaration_constructor_args():
    sig = inspect.signature(NameDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_plsql::package_is_not_abstract():
    assert not inspect.isabstract(plSql::Package)


def test_plsql::package_constructor_exists():
    assert callable(plSql::Package.__init__)


def test_plsql::package_constructor_args():
    sig = inspect.signature(plSql::Package.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "endName" in params, "Missing parameter 'endName'"

def test_plsql::package_has_schemaName():
    assert hasattr(plSql::Package, "schemaName")
    descriptor = None
    for klass in plSql::Package.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)

def test_plsql::package_has_endName():
    assert hasattr(plSql::Package, "endName")
    descriptor = None
    for klass in plSql::Package.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::procedure_is_not_abstract():
    assert not inspect.isabstract(plSql::Procedure)


def test_plsql::procedure_constructor_exists():
    assert callable(plSql::Procedure.__init__)


def test_plsql::procedure_constructor_args():
    sig = inspect.signature(plSql::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"

def test_plsql::procedure_has_schemaName():
    assert hasattr(plSql::Procedure, "schemaName")
    descriptor = None
    for klass in plSql::Procedure.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::compilationunit_is_not_abstract():
    assert not inspect.isabstract(plSql::CompilationUnit)


def test_plsql::compilationunit_constructor_exists():
    assert callable(plSql::CompilationUnit.__init__)


def test_plsql::compilationunit_constructor_args():
    sig = inspect.signature(plSql::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_plsql::namedeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::NameDeclaration)


def test_plsql::namedeclaration_constructor_exists():
    assert callable(plSql::NameDeclaration.__init__)


def test_plsql::namedeclaration_constructor_args():
    sig = inspect.signature(plSql::NameDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql::namedeclaration_has_name():
    assert hasattr(plSql::NameDeclaration, "name")
    descriptor = None
    for klass in plSql::NameDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql::name_is_not_abstract():
    assert not inspect.isabstract(plSql::Name)


def test_plsql::name_constructor_exists():
    assert callable(plSql::Name.__init__)


def test_plsql::name_constructor_args():
    sig = inspect.signature(plSql::Name.__init__)
    params = list(sig.parameters.keys())



def test_plsql::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(plSql::QualifiedName)


def test_plsql::qualifiedname_constructor_exists():
    assert callable(plSql::QualifiedName.__init__)


def test_plsql::qualifiedname_constructor_args():
    sig = inspect.signature(plSql::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_plsql::loopvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::LoopVariableDeclaration)


def test_plsql::loopvariabledeclaration_constructor_exists():
    assert callable(plSql::LoopVariableDeclaration.__init__)


def test_plsql::loopvariabledeclaration_constructor_args():
    sig = inspect.signature(plSql::LoopVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::forloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::ForLoopStatement)


def test_plsql::forloopstatement_constructor_exists():
    assert callable(plSql::ForLoopStatement.__init__)


def test_plsql::forloopstatement_constructor_args():
    sig = inspect.signature(plSql::ForLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::whileloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::WhileLoopStatement)


def test_plsql::whileloopstatement_constructor_exists():
    assert callable(plSql::WhileLoopStatement.__init__)


def test_plsql::whileloopstatement_constructor_args():
    sig = inspect.signature(plSql::WhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::basicloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::BasicLoopStatement)


def test_plsql::basicloopstatement_constructor_exists():
    assert callable(plSql::BasicLoopStatement.__init__)


def test_plsql::basicloopstatement_constructor_args():
    sig = inspect.signature(plSql::BasicLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::ifstatementelsebranch_is_not_abstract():
    assert not inspect.isabstract(plSql::IfStatementElseBranch)


def test_plsql::ifstatementelsebranch_constructor_exists():
    assert callable(plSql::IfStatementElseBranch.__init__)


def test_plsql::ifstatementelsebranch_constructor_args():
    sig = inspect.signature(plSql::IfStatementElseBranch.__init__)
    params = list(sig.parameters.keys())



def test_plsql::ifstatementelsifbranch_is_not_abstract():
    assert not inspect.isabstract(plSql::IfStatementElsifBranch)


def test_plsql::ifstatementelsifbranch_constructor_exists():
    assert callable(plSql::IfStatementElsifBranch.__init__)


def test_plsql::ifstatementelsifbranch_constructor_args():
    sig = inspect.signature(plSql::IfStatementElsifBranch.__init__)
    params = list(sig.parameters.keys())



def test_fetchstatementintoclause_is_not_abstract():
    assert not inspect.isabstract(FetchStatementIntoClause)


def test_fetchstatementintoclause_constructor_exists():
    assert callable(FetchStatementIntoClause.__init__)


def test_fetchstatementintoclause_constructor_args():
    sig = inspect.signature(FetchStatementIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::fetchstatementbulkintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql::FetchStatementBulkIntoClause)


def test_plsql::fetchstatementbulkintoclause_constructor_exists():
    assert callable(plSql::FetchStatementBulkIntoClause.__init__)


def test_plsql::fetchstatementbulkintoclause_constructor_args():
    sig = inspect.signature(plSql::FetchStatementBulkIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::fetchstatementsingleintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql::FetchStatementSingleIntoClause)


def test_plsql::fetchstatementsingleintoclause_constructor_exists():
    assert callable(plSql::FetchStatementSingleIntoClause.__init__)


def test_plsql::fetchstatementsingleintoclause_constructor_args():
    sig = inspect.signature(plSql::FetchStatementSingleIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::fetchstatementintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql::FetchStatementIntoClause)


def test_plsql::fetchstatementintoclause_constructor_exists():
    assert callable(plSql::FetchStatementIntoClause.__init__)


def test_plsql::fetchstatementintoclause_constructor_args():
    sig = inspect.signature(plSql::FetchStatementIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::casestatementelsebranch_is_not_abstract():
    assert not inspect.isabstract(plSql::CaseStatementElseBranch)


def test_plsql::casestatementelsebranch_constructor_exists():
    assert callable(plSql::CaseStatementElseBranch.__init__)


def test_plsql::casestatementelsebranch_constructor_args():
    sig = inspect.signature(plSql::CaseStatementElseBranch.__init__)
    params = list(sig.parameters.keys())



def test_assignmenttarget_is_not_abstract():
    assert not inspect.isabstract(AssignmentTarget)


def test_assignmenttarget_constructor_exists():
    assert callable(AssignmentTarget.__init__)


def test_assignmenttarget_constructor_args():
    sig = inspect.signature(AssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_plsql::variableassignmenttarget_is_not_abstract():
    assert not inspect.isabstract(plSql::VariableAssignmentTarget)


def test_plsql::variableassignmenttarget_constructor_exists():
    assert callable(plSql::VariableAssignmentTarget.__init__)


def test_plsql::variableassignmenttarget_constructor_args():
    sig = inspect.signature(plSql::VariableAssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_plsql::assignmenttarget_is_not_abstract():
    assert not inspect.isabstract(plSql::AssignmentTarget)


def test_plsql::assignmenttarget_constructor_exists():
    assert callable(plSql::AssignmentTarget.__init__)


def test_plsql::assignmenttarget_constructor_args():
    sig = inspect.signature(plSql::AssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::blockstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::BlockStatement)


def test_plsql::blockstatement_constructor_exists():
    assert callable(plSql::BlockStatement.__init__)


def test_plsql::blockstatement_constructor_args():
    sig = inspect.signature(plSql::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::ifstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::IfStatement)


def test_plsql::ifstatement_constructor_exists():
    assert callable(plSql::IfStatement.__init__)


def test_plsql::ifstatement_constructor_args():
    sig = inspect.signature(plSql::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::loopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::LoopStatement)


def test_plsql::loopstatement_constructor_exists():
    assert callable(plSql::LoopStatement.__init__)


def test_plsql::loopstatement_constructor_args():
    sig = inspect.signature(plSql::LoopStatement.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"

def test_plsql::loopstatement_has_endLabel():
    assert hasattr(plSql::LoopStatement, "endLabel")
    descriptor = None
    for klass in plSql::LoopStatement.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)



def test_plsql::gotostatement_is_not_abstract():
    assert not inspect.isabstract(plSql::GotoStatement)


def test_plsql::gotostatement_constructor_exists():
    assert callable(plSql::GotoStatement.__init__)


def test_plsql::gotostatement_constructor_args():
    sig = inspect.signature(plSql::GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::exitstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::ExitStatement)


def test_plsql::exitstatement_constructor_exists():
    assert callable(plSql::ExitStatement.__init__)


def test_plsql::exitstatement_constructor_args():
    sig = inspect.signature(plSql::ExitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelName" in params, "Missing parameter 'labelName'"

def test_plsql::exitstatement_has_labelName():
    assert hasattr(plSql::ExitStatement, "labelName")
    descriptor = None
    for klass in plSql::ExitStatement.__mro__:
        if "labelName" in klass.__dict__:
            descriptor = klass.__dict__["labelName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::raisestatement_is_not_abstract():
    assert not inspect.isabstract(plSql::RaiseStatement)


def test_plsql::raisestatement_constructor_exists():
    assert callable(plSql::RaiseStatement.__init__)


def test_plsql::raisestatement_constructor_args():
    sig = inspect.signature(plSql::RaiseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionName" in params, "Missing parameter 'exceptionName'"

def test_plsql::raisestatement_has_exceptionName():
    assert hasattr(plSql::RaiseStatement, "exceptionName")
    descriptor = None
    for klass in plSql::RaiseStatement.__mro__:
        if "exceptionName" in klass.__dict__:
            descriptor = klass.__dict__["exceptionName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::fetchstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::FetchStatement)


def test_plsql::fetchstatement_constructor_exists():
    assert callable(plSql::FetchStatement.__init__)


def test_plsql::fetchstatement_constructor_args():
    sig = inspect.signature(plSql::FetchStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::closestatement_is_not_abstract():
    assert not inspect.isabstract(plSql::CloseStatement)


def test_plsql::closestatement_constructor_exists():
    assert callable(plSql::CloseStatement.__init__)


def test_plsql::closestatement_constructor_args():
    sig = inspect.signature(plSql::CloseStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::nullstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::NullStatement)


def test_plsql::nullstatement_constructor_exists():
    assert callable(plSql::NullStatement.__init__)


def test_plsql::nullstatement_constructor_args():
    sig = inspect.signature(plSql::NullStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::returnstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::ReturnStatement)


def test_plsql::returnstatement_constructor_exists():
    assert callable(plSql::ReturnStatement.__init__)


def test_plsql::returnstatement_constructor_args():
    sig = inspect.signature(plSql::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::continuestatement_is_not_abstract():
    assert not inspect.isabstract(plSql::ContinueStatement)


def test_plsql::continuestatement_constructor_exists():
    assert callable(plSql::ContinueStatement.__init__)


def test_plsql::continuestatement_constructor_args():
    sig = inspect.signature(plSql::ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelName" in params, "Missing parameter 'labelName'"

def test_plsql::continuestatement_has_labelName():
    assert hasattr(plSql::ContinueStatement, "labelName")
    descriptor = None
    for klass in plSql::ContinueStatement.__mro__:
        if "labelName" in klass.__dict__:
            descriptor = klass.__dict__["labelName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(plSql::AssignmentStatement)


def test_plsql::assignmentstatement_constructor_exists():
    assert callable(plSql::AssignmentStatement.__init__)


def test_plsql::assignmentstatement_constructor_args():
    sig = inspect.signature(plSql::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql::label_is_not_abstract():
    assert not inspect.isabstract(plSql::Label)


def test_plsql::label_constructor_exists():
    assert callable(plSql::Label.__init__)


def test_plsql::label_constructor_args():
    sig = inspect.signature(plSql::Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql::label_has_name():
    assert hasattr(plSql::Label, "name")
    descriptor = None
    for klass in plSql::Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql::variableref_is_not_abstract():
    assert not inspect.isabstract(plSql::VariableRef)


def test_plsql::variableref_constructor_exists():
    assert callable(plSql::VariableRef.__init__)


def test_plsql::variableref_constructor_args():
    sig = inspect.signature(plSql::VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "isHostRef" in params, "Missing parameter 'isHostRef'"

def test_plsql::variableref_has_isHostRef():
    assert hasattr(plSql::VariableRef, "isHostRef")
    descriptor = None
    for klass in plSql::VariableRef.__mro__:
        if "isHostRef" in klass.__dict__:
            descriptor = klass.__dict__["isHostRef"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql::BooleanLiteralExpression)


def test_plsql::booleanliteralexpression_constructor_exists():
    assert callable(plSql::BooleanLiteralExpression.__init__)


def test_plsql::booleanliteralexpression_constructor_args():
    sig = inspect.signature(plSql::BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_plsql::booleanliteralexpression_has_value():
    assert hasattr(plSql::BooleanLiteralExpression, "value")
    descriptor = None
    for klass in plSql::BooleanLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql::variablerefexpression_is_not_abstract():
    assert not inspect.isabstract(plSql::VariableRefExpression)


def test_plsql::variablerefexpression_constructor_exists():
    assert callable(plSql::VariableRefExpression.__init__)


def test_plsql::variablerefexpression_constructor_args():
    sig = inspect.signature(plSql::VariableRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::stringliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql::StringLiteralExpression)


def test_plsql::stringliteralexpression_constructor_exists():
    assert callable(plSql::StringLiteralExpression.__init__)


def test_plsql::stringliteralexpression_constructor_args():
    sig = inspect.signature(plSql::StringLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_plsql::stringliteralexpression_has_value():
    assert hasattr(plSql::StringLiteralExpression, "value")
    descriptor = None
    for klass in plSql::StringLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql::nullliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql::NullLiteralExpression)


def test_plsql::nullliteralexpression_constructor_exists():
    assert callable(plSql::NullLiteralExpression.__init__)


def test_plsql::nullliteralexpression_constructor_args():
    sig = inspect.signature(plSql::NullLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::intliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql::IntLiteralExpression)


def test_plsql::intliteralexpression_constructor_exists():
    assert callable(plSql::IntLiteralExpression.__init__)


def test_plsql::intliteralexpression_constructor_args():
    sig = inspect.signature(plSql::IntLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_plsql::intliteralexpression_has_value():
    assert hasattr(plSql::IntLiteralExpression, "value")
    descriptor = None
    for klass in plSql::IntLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql::variablevalue_is_not_abstract():
    assert not inspect.isabstract(plSql::VariableValue)


def test_plsql::variablevalue_constructor_exists():
    assert callable(plSql::VariableValue.__init__)


def test_plsql::variablevalue_constructor_args():
    sig = inspect.signature(plSql::VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_plsql::casestatementwhenbranch_is_not_abstract():
    assert not inspect.isabstract(plSql::CaseStatementWhenBranch)


def test_plsql::casestatementwhenbranch_constructor_exists():
    assert callable(plSql::CaseStatementWhenBranch.__init__)


def test_plsql::casestatementwhenbranch_constructor_args():
    sig = inspect.signature(plSql::CaseStatementWhenBranch.__init__)
    params = list(sig.parameters.keys())



def test_plsql::casestatement_is_not_abstract():
    assert not inspect.isabstract(plSql::CaseStatement)


def test_plsql::casestatement_constructor_exists():
    assert callable(plSql::CaseStatement.__init__)


def test_plsql::casestatement_constructor_args():
    sig = inspect.signature(plSql::CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"

def test_plsql::casestatement_has_endLabel():
    assert hasattr(plSql::CaseStatement, "endLabel")
    descriptor = None
    for klass in plSql::CaseStatement.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)



def test_plsql::statement_is_not_abstract():
    assert not inspect.isabstract(plSql::Statement)


def test_plsql::statement_constructor_exists():
    assert callable(plSql::Statement.__init__)


def test_plsql::statement_constructor_args():
    sig = inspect.signature(plSql::Statement.__init__)
    params = list(sig.parameters.keys())



def test_functioncontent_is_not_abstract():
    assert not inspect.isabstract(FunctionContent)


def test_functioncontent_constructor_exists():
    assert callable(FunctionContent.__init__)


def test_functioncontent_constructor_args():
    sig = inspect.signature(FunctionContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql::functionimplementation_is_not_abstract():
    assert not inspect.isabstract(plSql::FunctionImplementation)


def test_plsql::functionimplementation_constructor_exists():
    assert callable(plSql::FunctionImplementation.__init__)


def test_plsql::functionimplementation_constructor_args():
    sig = inspect.signature(plSql::FunctionImplementation.__init__)
    params = list(sig.parameters.keys())



def test_plsql::statementbody_is_not_abstract():
    assert not inspect.isabstract(plSql::StatementBody)


def test_plsql::statementbody_constructor_exists():
    assert callable(plSql::StatementBody.__init__)


def test_plsql::statementbody_constructor_args():
    sig = inspect.signature(plSql::StatementBody.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"

def test_plsql::statementbody_has_endName():
    assert hasattr(plSql::StatementBody, "endName")
    descriptor = None
    for klass in plSql::StatementBody.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::declaresection_is_not_abstract():
    assert not inspect.isabstract(plSql::DeclareSection)


def test_plsql::declaresection_constructor_exists():
    assert callable(plSql::DeclareSection.__init__)


def test_plsql::declaresection_constructor_args():
    sig = inspect.signature(plSql::DeclareSection.__init__)
    params = list(sig.parameters.keys())



def test_procedurecontent_is_not_abstract():
    assert not inspect.isabstract(ProcedureContent)


def test_procedurecontent_constructor_exists():
    assert callable(ProcedureContent.__init__)


def test_procedurecontent_constructor_args():
    sig = inspect.signature(ProcedureContent.__init__)
    params = list(sig.parameters.keys())



def test_pragma_is_not_abstract():
    assert not inspect.isabstract(Pragma)


def test_pragma_constructor_exists():
    assert callable(Pragma.__init__)


def test_pragma_constructor_args():
    sig = inspect.signature(Pragma.__init__)
    params = list(sig.parameters.keys())



def test_plsql::pragmatimestamp_is_not_abstract():
    assert not inspect.isabstract(plSql::PragmaTimestamp)


def test_plsql::pragmatimestamp_constructor_exists():
    assert callable(plSql::PragmaTimestamp.__init__)


def test_plsql::pragmatimestamp_constructor_args():
    sig = inspect.signature(plSql::PragmaTimestamp.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_plsql::pragmatimestamp_has_timestamp():
    assert hasattr(plSql::PragmaTimestamp, "timestamp")
    descriptor = None
    for klass in plSql::PragmaTimestamp.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



def test_plsql::pragmarestrictreferences_is_not_abstract():
    assert not inspect.isabstract(plSql::PragmaRestrictReferences)


def test_plsql::pragmarestrictreferences_constructor_exists():
    assert callable(plSql::PragmaRestrictReferences.__init__)


def test_plsql::pragmarestrictreferences_constructor_args():
    sig = inspect.signature(plSql::PragmaRestrictReferences.__init__)
    params = list(sig.parameters.keys())
    assert "restrictions" in params, "Missing parameter 'restrictions'"

def test_plsql::pragmarestrictreferences_has_restrictions():
    assert hasattr(plSql::PragmaRestrictReferences, "restrictions")
    descriptor = None
    for klass in plSql::PragmaRestrictReferences.__mro__:
        if "restrictions" in klass.__dict__:
            descriptor = klass.__dict__["restrictions"]
            break
    assert isinstance(descriptor, property)



def test_plsql::pragma_is_not_abstract():
    assert not inspect.isabstract(plSql::Pragma)


def test_plsql::pragma_constructor_exists():
    assert callable(plSql::Pragma.__init__)


def test_plsql::pragma_constructor_args():
    sig = inspect.signature(plSql::Pragma.__init__)
    params = list(sig.parameters.keys())



def test_functionclause_is_not_abstract():
    assert not inspect.isabstract(FunctionClause)


def test_functionclause_constructor_exists():
    assert callable(FunctionClause.__init__)


def test_functionclause_constructor_args():
    sig = inspect.signature(FunctionClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::resultcacheclause_is_not_abstract():
    assert not inspect.isabstract(plSql::ResultCacheClause)


def test_plsql::resultcacheclause_constructor_exists():
    assert callable(plSql::ResultCacheClause.__init__)


def test_plsql::resultcacheclause_constructor_args():
    sig = inspect.signature(plSql::ResultCacheClause.__init__)
    params = list(sig.parameters.keys())
    assert "dataSources" in params, "Missing parameter 'dataSources'"

def test_plsql::resultcacheclause_has_dataSources():
    assert hasattr(plSql::ResultCacheClause, "dataSources")
    descriptor = None
    for klass in plSql::ResultCacheClause.__mro__:
        if "dataSources" in klass.__dict__:
            descriptor = klass.__dict__["dataSources"]
            break
    assert isinstance(descriptor, property)



def test_plsql::deterministicclause_is_not_abstract():
    assert not inspect.isabstract(plSql::DeterministicClause)


def test_plsql::deterministicclause_constructor_exists():
    assert callable(plSql::DeterministicClause.__init__)


def test_plsql::deterministicclause_constructor_args():
    sig = inspect.signature(plSql::DeterministicClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::pipelinedclause_is_not_abstract():
    assert not inspect.isabstract(plSql::PipelinedClause)


def test_plsql::pipelinedclause_constructor_exists():
    assert callable(plSql::PipelinedClause.__init__)


def test_plsql::pipelinedclause_constructor_args():
    sig = inspect.signature(plSql::PipelinedClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::functioninvokerrightsclause_is_not_abstract():
    assert not inspect.isabstract(plSql::FunctionInvokerRightsClause)


def test_plsql::functioninvokerrightsclause_constructor_exists():
    assert callable(plSql::FunctionInvokerRightsClause.__init__)


def test_plsql::functioninvokerrightsclause_constructor_args():
    sig = inspect.signature(plSql::FunctionInvokerRightsClause.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_plsql::functioninvokerrightsclause_has_right():
    assert hasattr(plSql::FunctionInvokerRightsClause, "right")
    descriptor = None
    for klass in plSql::FunctionInvokerRightsClause.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_itemdeclaration_is_not_abstract():
    assert not inspect.isabstract(ItemDeclaration)


def test_itemdeclaration_constructor_exists():
    assert callable(ItemDeclaration.__init__)


def test_itemdeclaration_constructor_args():
    sig = inspect.signature(ItemDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::VariableDeclaration)


def test_plsql::variabledeclaration_constructor_exists():
    assert callable(plSql::VariableDeclaration.__init__)


def test_plsql::variabledeclaration_constructor_args():
    sig = inspect.signature(plSql::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isConstant" in params, "Missing parameter 'isConstant'"
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_plsql::variabledeclaration_has_isConstant():
    assert hasattr(plSql::VariableDeclaration, "isConstant")
    descriptor = None
    for klass in plSql::VariableDeclaration.__mro__:
        if "isConstant" in klass.__dict__:
            descriptor = klass.__dict__["isConstant"]
            break
    assert isinstance(descriptor, property)

def test_plsql::variabledeclaration_has_isNotNull():
    assert hasattr(plSql::VariableDeclaration, "isNotNull")
    descriptor = None
    for klass in plSql::VariableDeclaration.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)

def test_plsql::variabledeclaration_has_dataType():
    assert hasattr(plSql::VariableDeclaration, "dataType")
    descriptor = None
    for klass in plSql::VariableDeclaration.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_plsql::externalproceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::ExternalProcedureDeclaration)


def test_plsql::externalproceduredeclaration_constructor_exists():
    assert callable(plSql::ExternalProcedureDeclaration.__init__)


def test_plsql::externalproceduredeclaration_constructor_args():
    sig = inspect.signature(plSql::ExternalProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::itemdeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::ItemDeclaration)


def test_plsql::itemdeclaration_constructor_exists():
    assert callable(plSql::ItemDeclaration.__init__)


def test_plsql::itemdeclaration_constructor_args():
    sig = inspect.signature(plSql::ItemDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql::ParameterDeclaration)


def test_plsql::parameterdeclaration_constructor_exists():
    assert callable(plSql::ParameterDeclaration.__init__)


def test_plsql::parameterdeclaration_constructor_args():
    sig = inspect.signature(plSql::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_plsql::parameterdeclaration_has_behavior():
    assert hasattr(plSql::ParameterDeclaration, "behavior")
    descriptor = None
    for klass in plSql::ParameterDeclaration.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)

def test_plsql::parameterdeclaration_has_dataType():
    assert hasattr(plSql::ParameterDeclaration, "dataType")
    descriptor = None
    for klass in plSql::ParameterDeclaration.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_plsql::functioncontent_is_not_abstract():
    assert not inspect.isabstract(plSql::FunctionContent)


def test_plsql::functioncontent_constructor_exists():
    assert callable(plSql::FunctionContent.__init__)


def test_plsql::functioncontent_constructor_args():
    sig = inspect.signature(plSql::FunctionContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql::functionclause_is_not_abstract():
    assert not inspect.isabstract(plSql::FunctionClause)


def test_plsql::functionclause_constructor_exists():
    assert callable(plSql::FunctionClause.__init__)


def test_plsql::functionclause_constructor_args():
    sig = inspect.signature(plSql::FunctionClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql::function_is_not_abstract():
    assert not inspect.isabstract(plSql::Function)


def test_plsql::function_constructor_exists():
    assert callable(plSql::Function.__init__)


def test_plsql::function_constructor_args():
    sig = inspect.signature(plSql::Function.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "schemaName" in params, "Missing parameter 'schemaName'"

def test_plsql::function_has_returnType():
    assert hasattr(plSql::Function, "returnType")
    descriptor = None
    for klass in plSql::Function.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_plsql::function_has_schemaName():
    assert hasattr(plSql::Function, "schemaName")
    descriptor = None
    for klass in plSql::Function.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)



def test_plsql::procedureimplementation_is_not_abstract():
    assert not inspect.isabstract(plSql::ProcedureImplementation)


def test_plsql::procedureimplementation_constructor_exists():
    assert callable(plSql::ProcedureImplementation.__init__)


def test_plsql::procedureimplementation_constructor_args():
    sig = inspect.signature(plSql::ProcedureImplementation.__init__)
    params = list(sig.parameters.keys())



def test_plsql::expression_is_not_abstract():
    assert not inspect.isabstract(plSql::Expression)


def test_plsql::expression_constructor_exists():
    assert callable(plSql::Expression.__init__)


def test_plsql::expression_constructor_args():
    sig = inspect.signature(plSql::Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql::parametervalue_is_not_abstract():
    assert not inspect.isabstract(plSql::ParameterValue)


def test_plsql::parametervalue_constructor_exists():
    assert callable(plSql::ParameterValue.__init__)


def test_plsql::parametervalue_constructor_args():
    sig = inspect.signature(plSql::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_plsql::proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(plSql::ProcedureDefinition)


def test_plsql::proceduredefinition_constructor_exists():
    assert callable(plSql::ProcedureDefinition.__init__)


def test_plsql::proceduredefinition_constructor_args():
    sig = inspect.signature(plSql::ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())

def test_invokerright_exists():
    # Check that the Enumeration exists
    assert InvokerRight is not None

def test_invokerright_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvokerRight]
    expected_literals = [
        "DEFINER",
        "CURRENT_USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvokerRight"


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
Item_strategy = st.builds(
    Item,
)
plSql::ProcedureDeclaration_strategy = st.builds(
    plSql::ProcedureDeclaration,
    name=
        safe_text
)
plSql::Item_strategy = st.builds(
    plSql::Item,
)
plSql::ProcedureContent_strategy = st.builds(
    plSql::ProcedureContent,
)
plSql::ProcedureInvokerRightsClause_strategy = st.builds(
    plSql::ProcedureInvokerRightsClause,
    right=
        safe_text
)
plSql::ParameterSequence_strategy = st.builds(
    plSql::ParameterSequence,
)
NameDeclaration_strategy = st.builds(
    NameDeclaration,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
plSql::Package_strategy = st.builds(
    plSql::Package,
    schemaName=
        safe_text,
    endName=
        safe_text
)
plSql::Procedure_strategy = st.builds(
    plSql::Procedure,
    schemaName=
        safe_text
)
plSql::CompilationUnit_strategy = st.builds(
    plSql::CompilationUnit,
)
plSql::NameDeclaration_strategy = st.builds(
    plSql::NameDeclaration,
    name=
        safe_text
)
plSql::Name_strategy = st.builds(
    plSql::Name,
)
plSql::QualifiedName_strategy = st.builds(
    plSql::QualifiedName,
)
plSql::LoopVariableDeclaration_strategy = st.builds(
    plSql::LoopVariableDeclaration,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
plSql::ForLoopStatement_strategy = st.builds(
    plSql::ForLoopStatement,
)
plSql::WhileLoopStatement_strategy = st.builds(
    plSql::WhileLoopStatement,
)
plSql::BasicLoopStatement_strategy = st.builds(
    plSql::BasicLoopStatement,
)
plSql::IfStatementElseBranch_strategy = st.builds(
    plSql::IfStatementElseBranch,
)
plSql::IfStatementElsifBranch_strategy = st.builds(
    plSql::IfStatementElsifBranch,
)
FetchStatementIntoClause_strategy = st.builds(
    FetchStatementIntoClause,
)
plSql::FetchStatementBulkIntoClause_strategy = st.builds(
    plSql::FetchStatementBulkIntoClause,
)
plSql::FetchStatementSingleIntoClause_strategy = st.builds(
    plSql::FetchStatementSingleIntoClause,
)
plSql::FetchStatementIntoClause_strategy = st.builds(
    plSql::FetchStatementIntoClause,
)
plSql::CaseStatementElseBranch_strategy = st.builds(
    plSql::CaseStatementElseBranch,
)
AssignmentTarget_strategy = st.builds(
    AssignmentTarget,
)
plSql::VariableAssignmentTarget_strategy = st.builds(
    plSql::VariableAssignmentTarget,
)
plSql::AssignmentTarget_strategy = st.builds(
    plSql::AssignmentTarget,
)
Statement_strategy = st.builds(
    Statement,
)
plSql::BlockStatement_strategy = st.builds(
    plSql::BlockStatement,
)
plSql::IfStatement_strategy = st.builds(
    plSql::IfStatement,
)
plSql::LoopStatement_strategy = st.builds(
    plSql::LoopStatement,
    endLabel=
        safe_text
)
plSql::GotoStatement_strategy = st.builds(
    plSql::GotoStatement,
)
plSql::ExitStatement_strategy = st.builds(
    plSql::ExitStatement,
    labelName=
        safe_text
)
plSql::RaiseStatement_strategy = st.builds(
    plSql::RaiseStatement,
    exceptionName=
        safe_text
)
plSql::FetchStatement_strategy = st.builds(
    plSql::FetchStatement,
)
plSql::CloseStatement_strategy = st.builds(
    plSql::CloseStatement,
)
plSql::NullStatement_strategy = st.builds(
    plSql::NullStatement,
)
plSql::ReturnStatement_strategy = st.builds(
    plSql::ReturnStatement,
)
plSql::ContinueStatement_strategy = st.builds(
    plSql::ContinueStatement,
    labelName=
        safe_text
)
plSql::AssignmentStatement_strategy = st.builds(
    plSql::AssignmentStatement,
)
plSql::Label_strategy = st.builds(
    plSql::Label,
    name=
        safe_text
)
plSql::VariableRef_strategy = st.builds(
    plSql::VariableRef,
    isHostRef=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
plSql::BooleanLiteralExpression_strategy = st.builds(
    plSql::BooleanLiteralExpression,
    value=
        safe_text
)
plSql::VariableRefExpression_strategy = st.builds(
    plSql::VariableRefExpression,
)
plSql::StringLiteralExpression_strategy = st.builds(
    plSql::StringLiteralExpression,
    value=
        safe_text
)
plSql::NullLiteralExpression_strategy = st.builds(
    plSql::NullLiteralExpression,
)
plSql::IntLiteralExpression_strategy = st.builds(
    plSql::IntLiteralExpression,
    value=
        st.integers()
)
plSql::VariableValue_strategy = st.builds(
    plSql::VariableValue,
)
plSql::CaseStatementWhenBranch_strategy = st.builds(
    plSql::CaseStatementWhenBranch,
)
plSql::CaseStatement_strategy = st.builds(
    plSql::CaseStatement,
    endLabel=
        safe_text
)
plSql::Statement_strategy = st.builds(
    plSql::Statement,
)
FunctionContent_strategy = st.builds(
    FunctionContent,
)
plSql::FunctionImplementation_strategy = st.builds(
    plSql::FunctionImplementation,
)
plSql::StatementBody_strategy = st.builds(
    plSql::StatementBody,
    endName=
        safe_text
)
plSql::DeclareSection_strategy = st.builds(
    plSql::DeclareSection,
)
ProcedureContent_strategy = st.builds(
    ProcedureContent,
)
Pragma_strategy = st.builds(
    Pragma,
)
plSql::PragmaTimestamp_strategy = st.builds(
    plSql::PragmaTimestamp,
    timestamp=
        safe_text
)
plSql::PragmaRestrictReferences_strategy = st.builds(
    plSql::PragmaRestrictReferences,
    restrictions=
        safe_text
)
plSql::Pragma_strategy = st.builds(
    plSql::Pragma,
)
FunctionClause_strategy = st.builds(
    FunctionClause,
)
plSql::ResultCacheClause_strategy = st.builds(
    plSql::ResultCacheClause,
    dataSources=
        safe_text
)
plSql::DeterministicClause_strategy = st.builds(
    plSql::DeterministicClause,
)
plSql::PipelinedClause_strategy = st.builds(
    plSql::PipelinedClause,
)
plSql::FunctionInvokerRightsClause_strategy = st.builds(
    plSql::FunctionInvokerRightsClause,
    right=
        safe_text
)
ItemDeclaration_strategy = st.builds(
    ItemDeclaration,
)
plSql::VariableDeclaration_strategy = st.builds(
    plSql::VariableDeclaration,
    isConstant=
        st.booleans(),
    isNotNull=
        st.booleans(),
    dataType=
        safe_text
)
plSql::ExternalProcedureDeclaration_strategy = st.builds(
    plSql::ExternalProcedureDeclaration,
)
plSql::ItemDeclaration_strategy = st.builds(
    plSql::ItemDeclaration,
)
plSql::ParameterDeclaration_strategy = st.builds(
    plSql::ParameterDeclaration,
    behavior=
        safe_text,
    dataType=
        safe_text
)
plSql::FunctionContent_strategy = st.builds(
    plSql::FunctionContent,
)
plSql::FunctionClause_strategy = st.builds(
    plSql::FunctionClause,
)
plSql::Function_strategy = st.builds(
    plSql::Function,
    returnType=
        safe_text,
    schemaName=
        safe_text
)
plSql::ProcedureImplementation_strategy = st.builds(
    plSql::ProcedureImplementation,
)
plSql::Expression_strategy = st.builds(
    plSql::Expression,
)
plSql::ParameterValue_strategy = st.builds(
    plSql::ParameterValue,
)
plSql::ProcedureDefinition_strategy = st.builds(
    plSql::ProcedureDefinition,
)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=plSql::ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::proceduredeclaration_instantiation(instance):
    assert isinstance(instance, plSql::ProcedureDeclaration)

@given(instance=plSql::ProcedureDeclaration_strategy)
def test_plsql::proceduredeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=plSql::ProcedureDeclaration_strategy)
def test_plsql::proceduredeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plSql::Item_strategy)
@settings(max_examples=50)
def test_plsql::item_instantiation(instance):
    assert isinstance(instance, plSql::Item)

@given(instance=plSql::ProcedureContent_strategy)
@settings(max_examples=50)
def test_plsql::procedurecontent_instantiation(instance):
    assert isinstance(instance, plSql::ProcedureContent)

@given(instance=plSql::ProcedureInvokerRightsClause_strategy)
@settings(max_examples=50)
def test_plsql::procedureinvokerrightsclause_instantiation(instance):
    assert isinstance(instance, plSql::ProcedureInvokerRightsClause)

@given(instance=plSql::ProcedureInvokerRightsClause_strategy)
def test_plsql::procedureinvokerrightsclause_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=plSql::ProcedureInvokerRightsClause_strategy)
def test_plsql::procedureinvokerrightsclause_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=plSql::ParameterSequence_strategy)
@settings(max_examples=50)
def test_plsql::parametersequence_instantiation(instance):
    assert isinstance(instance, plSql::ParameterSequence)

@given(instance=NameDeclaration_strategy)
@settings(max_examples=50)
def test_namedeclaration_instantiation(instance):
    assert isinstance(instance, NameDeclaration)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=plSql::Package_strategy)
@settings(max_examples=50)
def test_plsql::package_instantiation(instance):
    assert isinstance(instance, plSql::Package)

@given(instance=plSql::Package_strategy)
def test_plsql::package_schemaName_type(instance):
    assert isinstance(instance.schemaName, str)


@given(instance=plSql::Package_strategy)
def test_plsql::package_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=plSql::Package_strategy)
def test_plsql::package_endName_type(instance):
    assert isinstance(instance.endName, str)


@given(instance=plSql::Package_strategy)
def test_plsql::package_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original

@given(instance=plSql::Procedure_strategy)
@settings(max_examples=50)
def test_plsql::procedure_instantiation(instance):
    assert isinstance(instance, plSql::Procedure)

@given(instance=plSql::Procedure_strategy)
def test_plsql::procedure_schemaName_type(instance):
    assert isinstance(instance.schemaName, str)


@given(instance=plSql::Procedure_strategy)
def test_plsql::procedure_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=plSql::CompilationUnit_strategy)
@settings(max_examples=50)
def test_plsql::compilationunit_instantiation(instance):
    assert isinstance(instance, plSql::CompilationUnit)

@given(instance=plSql::NameDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::namedeclaration_instantiation(instance):
    assert isinstance(instance, plSql::NameDeclaration)

@given(instance=plSql::NameDeclaration_strategy)
def test_plsql::namedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=plSql::NameDeclaration_strategy)
def test_plsql::namedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plSql::Name_strategy)
@settings(max_examples=50)
def test_plsql::name_instantiation(instance):
    assert isinstance(instance, plSql::Name)

@given(instance=plSql::QualifiedName_strategy)
@settings(max_examples=50)
def test_plsql::qualifiedname_instantiation(instance):
    assert isinstance(instance, plSql::QualifiedName)

@given(instance=plSql::LoopVariableDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::loopvariabledeclaration_instantiation(instance):
    assert isinstance(instance, plSql::LoopVariableDeclaration)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=plSql::ForLoopStatement_strategy)
@settings(max_examples=50)
def test_plsql::forloopstatement_instantiation(instance):
    assert isinstance(instance, plSql::ForLoopStatement)

@given(instance=plSql::WhileLoopStatement_strategy)
@settings(max_examples=50)
def test_plsql::whileloopstatement_instantiation(instance):
    assert isinstance(instance, plSql::WhileLoopStatement)

@given(instance=plSql::BasicLoopStatement_strategy)
@settings(max_examples=50)
def test_plsql::basicloopstatement_instantiation(instance):
    assert isinstance(instance, plSql::BasicLoopStatement)

@given(instance=plSql::IfStatementElseBranch_strategy)
@settings(max_examples=50)
def test_plsql::ifstatementelsebranch_instantiation(instance):
    assert isinstance(instance, plSql::IfStatementElseBranch)

@given(instance=plSql::IfStatementElsifBranch_strategy)
@settings(max_examples=50)
def test_plsql::ifstatementelsifbranch_instantiation(instance):
    assert isinstance(instance, plSql::IfStatementElsifBranch)

@given(instance=FetchStatementIntoClause_strategy)
@settings(max_examples=50)
def test_fetchstatementintoclause_instantiation(instance):
    assert isinstance(instance, FetchStatementIntoClause)

@given(instance=plSql::FetchStatementBulkIntoClause_strategy)
@settings(max_examples=50)
def test_plsql::fetchstatementbulkintoclause_instantiation(instance):
    assert isinstance(instance, plSql::FetchStatementBulkIntoClause)

@given(instance=plSql::FetchStatementSingleIntoClause_strategy)
@settings(max_examples=50)
def test_plsql::fetchstatementsingleintoclause_instantiation(instance):
    assert isinstance(instance, plSql::FetchStatementSingleIntoClause)

@given(instance=plSql::FetchStatementIntoClause_strategy)
@settings(max_examples=50)
def test_plsql::fetchstatementintoclause_instantiation(instance):
    assert isinstance(instance, plSql::FetchStatementIntoClause)

@given(instance=plSql::CaseStatementElseBranch_strategy)
@settings(max_examples=50)
def test_plsql::casestatementelsebranch_instantiation(instance):
    assert isinstance(instance, plSql::CaseStatementElseBranch)

@given(instance=AssignmentTarget_strategy)
@settings(max_examples=50)
def test_assignmenttarget_instantiation(instance):
    assert isinstance(instance, AssignmentTarget)

@given(instance=plSql::VariableAssignmentTarget_strategy)
@settings(max_examples=50)
def test_plsql::variableassignmenttarget_instantiation(instance):
    assert isinstance(instance, plSql::VariableAssignmentTarget)

@given(instance=plSql::AssignmentTarget_strategy)
@settings(max_examples=50)
def test_plsql::assignmenttarget_instantiation(instance):
    assert isinstance(instance, plSql::AssignmentTarget)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=plSql::BlockStatement_strategy)
@settings(max_examples=50)
def test_plsql::blockstatement_instantiation(instance):
    assert isinstance(instance, plSql::BlockStatement)

@given(instance=plSql::IfStatement_strategy)
@settings(max_examples=50)
def test_plsql::ifstatement_instantiation(instance):
    assert isinstance(instance, plSql::IfStatement)

@given(instance=plSql::LoopStatement_strategy)
@settings(max_examples=50)
def test_plsql::loopstatement_instantiation(instance):
    assert isinstance(instance, plSql::LoopStatement)

@given(instance=plSql::LoopStatement_strategy)
def test_plsql::loopstatement_endLabel_type(instance):
    assert isinstance(instance.endLabel, str)


@given(instance=plSql::LoopStatement_strategy)
def test_plsql::loopstatement_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original

@given(instance=plSql::GotoStatement_strategy)
@settings(max_examples=50)
def test_plsql::gotostatement_instantiation(instance):
    assert isinstance(instance, plSql::GotoStatement)

@given(instance=plSql::ExitStatement_strategy)
@settings(max_examples=50)
def test_plsql::exitstatement_instantiation(instance):
    assert isinstance(instance, plSql::ExitStatement)

@given(instance=plSql::ExitStatement_strategy)
def test_plsql::exitstatement_labelName_type(instance):
    assert isinstance(instance.labelName, str)


@given(instance=plSql::ExitStatement_strategy)
def test_plsql::exitstatement_labelName_setter(instance):
    original = instance.labelName
    instance.labelName = original
    assert instance.labelName == original

@given(instance=plSql::RaiseStatement_strategy)
@settings(max_examples=50)
def test_plsql::raisestatement_instantiation(instance):
    assert isinstance(instance, plSql::RaiseStatement)

@given(instance=plSql::RaiseStatement_strategy)
def test_plsql::raisestatement_exceptionName_type(instance):
    assert isinstance(instance.exceptionName, str)


@given(instance=plSql::RaiseStatement_strategy)
def test_plsql::raisestatement_exceptionName_setter(instance):
    original = instance.exceptionName
    instance.exceptionName = original
    assert instance.exceptionName == original

@given(instance=plSql::FetchStatement_strategy)
@settings(max_examples=50)
def test_plsql::fetchstatement_instantiation(instance):
    assert isinstance(instance, plSql::FetchStatement)

@given(instance=plSql::CloseStatement_strategy)
@settings(max_examples=50)
def test_plsql::closestatement_instantiation(instance):
    assert isinstance(instance, plSql::CloseStatement)

@given(instance=plSql::NullStatement_strategy)
@settings(max_examples=50)
def test_plsql::nullstatement_instantiation(instance):
    assert isinstance(instance, plSql::NullStatement)

@given(instance=plSql::ReturnStatement_strategy)
@settings(max_examples=50)
def test_plsql::returnstatement_instantiation(instance):
    assert isinstance(instance, plSql::ReturnStatement)

@given(instance=plSql::ContinueStatement_strategy)
@settings(max_examples=50)
def test_plsql::continuestatement_instantiation(instance):
    assert isinstance(instance, plSql::ContinueStatement)

@given(instance=plSql::ContinueStatement_strategy)
def test_plsql::continuestatement_labelName_type(instance):
    assert isinstance(instance.labelName, str)


@given(instance=plSql::ContinueStatement_strategy)
def test_plsql::continuestatement_labelName_setter(instance):
    original = instance.labelName
    instance.labelName = original
    assert instance.labelName == original

@given(instance=plSql::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_plsql::assignmentstatement_instantiation(instance):
    assert isinstance(instance, plSql::AssignmentStatement)

@given(instance=plSql::Label_strategy)
@settings(max_examples=50)
def test_plsql::label_instantiation(instance):
    assert isinstance(instance, plSql::Label)

@given(instance=plSql::Label_strategy)
def test_plsql::label_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=plSql::Label_strategy)
def test_plsql::label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plSql::VariableRef_strategy)
@settings(max_examples=50)
def test_plsql::variableref_instantiation(instance):
    assert isinstance(instance, plSql::VariableRef)

@given(instance=plSql::VariableRef_strategy)
def test_plsql::variableref_isHostRef_type(instance):
    assert isinstance(instance.isHostRef, bool)


@given(instance=plSql::VariableRef_strategy)
def test_plsql::variableref_isHostRef_setter(instance):
    original = instance.isHostRef
    instance.isHostRef = original
    assert instance.isHostRef == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=plSql::BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql::booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql::BooleanLiteralExpression)

@given(instance=plSql::BooleanLiteralExpression_strategy)
def test_plsql::booleanliteralexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=plSql::BooleanLiteralExpression_strategy)
def test_plsql::booleanliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plSql::VariableRefExpression_strategy)
@settings(max_examples=50)
def test_plsql::variablerefexpression_instantiation(instance):
    assert isinstance(instance, plSql::VariableRefExpression)

@given(instance=plSql::StringLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql::stringliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql::StringLiteralExpression)

@given(instance=plSql::StringLiteralExpression_strategy)
def test_plsql::stringliteralexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=plSql::StringLiteralExpression_strategy)
def test_plsql::stringliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plSql::NullLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql::nullliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql::NullLiteralExpression)

@given(instance=plSql::IntLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql::intliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql::IntLiteralExpression)

@given(instance=plSql::IntLiteralExpression_strategy)
def test_plsql::intliteralexpression_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=plSql::IntLiteralExpression_strategy)
def test_plsql::intliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plSql::VariableValue_strategy)
@settings(max_examples=50)
def test_plsql::variablevalue_instantiation(instance):
    assert isinstance(instance, plSql::VariableValue)

@given(instance=plSql::CaseStatementWhenBranch_strategy)
@settings(max_examples=50)
def test_plsql::casestatementwhenbranch_instantiation(instance):
    assert isinstance(instance, plSql::CaseStatementWhenBranch)

@given(instance=plSql::CaseStatement_strategy)
@settings(max_examples=50)
def test_plsql::casestatement_instantiation(instance):
    assert isinstance(instance, plSql::CaseStatement)

@given(instance=plSql::CaseStatement_strategy)
def test_plsql::casestatement_endLabel_type(instance):
    assert isinstance(instance.endLabel, str)


@given(instance=plSql::CaseStatement_strategy)
def test_plsql::casestatement_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original

@given(instance=plSql::Statement_strategy)
@settings(max_examples=50)
def test_plsql::statement_instantiation(instance):
    assert isinstance(instance, plSql::Statement)

@given(instance=FunctionContent_strategy)
@settings(max_examples=50)
def test_functioncontent_instantiation(instance):
    assert isinstance(instance, FunctionContent)

@given(instance=plSql::FunctionImplementation_strategy)
@settings(max_examples=50)
def test_plsql::functionimplementation_instantiation(instance):
    assert isinstance(instance, plSql::FunctionImplementation)

@given(instance=plSql::StatementBody_strategy)
@settings(max_examples=50)
def test_plsql::statementbody_instantiation(instance):
    assert isinstance(instance, plSql::StatementBody)

@given(instance=plSql::StatementBody_strategy)
def test_plsql::statementbody_endName_type(instance):
    assert isinstance(instance.endName, str)


@given(instance=plSql::StatementBody_strategy)
def test_plsql::statementbody_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original

@given(instance=plSql::DeclareSection_strategy)
@settings(max_examples=50)
def test_plsql::declaresection_instantiation(instance):
    assert isinstance(instance, plSql::DeclareSection)

@given(instance=ProcedureContent_strategy)
@settings(max_examples=50)
def test_procedurecontent_instantiation(instance):
    assert isinstance(instance, ProcedureContent)

@given(instance=Pragma_strategy)
@settings(max_examples=50)
def test_pragma_instantiation(instance):
    assert isinstance(instance, Pragma)

@given(instance=plSql::PragmaTimestamp_strategy)
@settings(max_examples=50)
def test_plsql::pragmatimestamp_instantiation(instance):
    assert isinstance(instance, plSql::PragmaTimestamp)

@given(instance=plSql::PragmaTimestamp_strategy)
def test_plsql::pragmatimestamp_timestamp_type(instance):
    assert isinstance(instance.timestamp, str)


@given(instance=plSql::PragmaTimestamp_strategy)
def test_plsql::pragmatimestamp_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=plSql::PragmaRestrictReferences_strategy)
@settings(max_examples=50)
def test_plsql::pragmarestrictreferences_instantiation(instance):
    assert isinstance(instance, plSql::PragmaRestrictReferences)

@given(instance=plSql::PragmaRestrictReferences_strategy)
def test_plsql::pragmarestrictreferences_restrictions_type(instance):
    assert isinstance(instance.restrictions, str)


@given(instance=plSql::PragmaRestrictReferences_strategy)
def test_plsql::pragmarestrictreferences_restrictions_setter(instance):
    original = instance.restrictions
    instance.restrictions = original
    assert instance.restrictions == original

@given(instance=plSql::Pragma_strategy)
@settings(max_examples=50)
def test_plsql::pragma_instantiation(instance):
    assert isinstance(instance, plSql::Pragma)

@given(instance=FunctionClause_strategy)
@settings(max_examples=50)
def test_functionclause_instantiation(instance):
    assert isinstance(instance, FunctionClause)

@given(instance=plSql::ResultCacheClause_strategy)
@settings(max_examples=50)
def test_plsql::resultcacheclause_instantiation(instance):
    assert isinstance(instance, plSql::ResultCacheClause)

@given(instance=plSql::ResultCacheClause_strategy)
def test_plsql::resultcacheclause_dataSources_type(instance):
    assert isinstance(instance.dataSources, str)


@given(instance=plSql::ResultCacheClause_strategy)
def test_plsql::resultcacheclause_dataSources_setter(instance):
    original = instance.dataSources
    instance.dataSources = original
    assert instance.dataSources == original

@given(instance=plSql::DeterministicClause_strategy)
@settings(max_examples=50)
def test_plsql::deterministicclause_instantiation(instance):
    assert isinstance(instance, plSql::DeterministicClause)

@given(instance=plSql::PipelinedClause_strategy)
@settings(max_examples=50)
def test_plsql::pipelinedclause_instantiation(instance):
    assert isinstance(instance, plSql::PipelinedClause)

@given(instance=plSql::FunctionInvokerRightsClause_strategy)
@settings(max_examples=50)
def test_plsql::functioninvokerrightsclause_instantiation(instance):
    assert isinstance(instance, plSql::FunctionInvokerRightsClause)

@given(instance=plSql::FunctionInvokerRightsClause_strategy)
def test_plsql::functioninvokerrightsclause_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=plSql::FunctionInvokerRightsClause_strategy)
def test_plsql::functioninvokerrightsclause_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=ItemDeclaration_strategy)
@settings(max_examples=50)
def test_itemdeclaration_instantiation(instance):
    assert isinstance(instance, ItemDeclaration)

@given(instance=plSql::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::variabledeclaration_instantiation(instance):
    assert isinstance(instance, plSql::VariableDeclaration)

@given(instance=plSql::VariableDeclaration_strategy)
def test_plsql::variabledeclaration_isConstant_type(instance):
    assert isinstance(instance.isConstant, bool)


@given(instance=plSql::VariableDeclaration_strategy)
def test_plsql::variabledeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original

@given(instance=plSql::VariableDeclaration_strategy)
def test_plsql::variabledeclaration_isNotNull_type(instance):
    assert isinstance(instance.isNotNull, bool)


@given(instance=plSql::VariableDeclaration_strategy)
def test_plsql::variabledeclaration_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original

@given(instance=plSql::VariableDeclaration_strategy)
def test_plsql::variabledeclaration_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=plSql::VariableDeclaration_strategy)
def test_plsql::variabledeclaration_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=plSql::ExternalProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::externalproceduredeclaration_instantiation(instance):
    assert isinstance(instance, plSql::ExternalProcedureDeclaration)

@given(instance=plSql::ItemDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::itemdeclaration_instantiation(instance):
    assert isinstance(instance, plSql::ItemDeclaration)

@given(instance=plSql::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_plsql::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, plSql::ParameterDeclaration)

@given(instance=plSql::ParameterDeclaration_strategy)
def test_plsql::parameterdeclaration_behavior_type(instance):
    assert isinstance(instance.behavior, str)


@given(instance=plSql::ParameterDeclaration_strategy)
def test_plsql::parameterdeclaration_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=plSql::ParameterDeclaration_strategy)
def test_plsql::parameterdeclaration_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=plSql::ParameterDeclaration_strategy)
def test_plsql::parameterdeclaration_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=plSql::FunctionContent_strategy)
@settings(max_examples=50)
def test_plsql::functioncontent_instantiation(instance):
    assert isinstance(instance, plSql::FunctionContent)

@given(instance=plSql::FunctionClause_strategy)
@settings(max_examples=50)
def test_plsql::functionclause_instantiation(instance):
    assert isinstance(instance, plSql::FunctionClause)

@given(instance=plSql::Function_strategy)
@settings(max_examples=50)
def test_plsql::function_instantiation(instance):
    assert isinstance(instance, plSql::Function)

@given(instance=plSql::Function_strategy)
def test_plsql::function_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=plSql::Function_strategy)
def test_plsql::function_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=plSql::Function_strategy)
def test_plsql::function_schemaName_type(instance):
    assert isinstance(instance.schemaName, str)


@given(instance=plSql::Function_strategy)
def test_plsql::function_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=plSql::ProcedureImplementation_strategy)
@settings(max_examples=50)
def test_plsql::procedureimplementation_instantiation(instance):
    assert isinstance(instance, plSql::ProcedureImplementation)

@given(instance=plSql::Expression_strategy)
@settings(max_examples=50)
def test_plsql::expression_instantiation(instance):
    assert isinstance(instance, plSql::Expression)

@given(instance=plSql::ParameterValue_strategy)
@settings(max_examples=50)
def test_plsql::parametervalue_instantiation(instance):
    assert isinstance(instance, plSql::ParameterValue)

@given(instance=plSql::ProcedureDefinition_strategy)
@settings(max_examples=50)
def test_plsql::proceduredefinition_instantiation(instance):
    assert isinstance(instance, plSql::ProcedureDefinition)
