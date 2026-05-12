import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    plSql_NameDeclaration,
    plSql_Name,
    plSql_QualifiedName,
    plSql_IfStatementElseBranch,
    plSql_IfStatementElsifBranch,
    FetchStatementIntoClause,
    plSql_FetchStatementBulkIntoClause,
    plSql_FetchStatementSingleIntoClause,
    LoopStatement,
    plSql_ForLoopStatement,
    plSql_WhileLoopStatement,
    plSql_BasicLoopStatement,
    plSql_CaseStatementElseBranch,
    plSql_CaseStatementWhenBranch,
    plSql_FetchStatementIntoClause,
    plSql_VariableRef,
    Expression,
    plSql_NullLiteralExpression,
    plSql_VariableRefExpression,
    plSql_StringLiteralExpression,
    plSql_BooleanLiteralExpression,
    plSql_IntLiteralExpression,
    plSql_VariableValue,
    ItemDeclaration,
    AssignmentTarget,
    plSql_VariableAssignmentTarget,
    plSql_AssignmentTarget,
    Statement,
    plSql_ContinueStatement,
    plSql_FetchStatement,
    plSql_ExitStatement,
    plSql_ReturnStatement,
    plSql_IfStatement,
    plSql_CaseStatement,
    plSql_LoopStatement,
    plSql_RaiseStatement,
    plSql_CloseStatement,
    plSql_NullStatement,
    plSql_GotoStatement,
    plSql_BlockStatement,
    plSql_AssignmentStatement,
    plSql_Label,
    FunctionContent,
    plSql_FunctionImplementation,
    plSql_StatementBody,
    plSql_DeclareSection,
    ProcedureContent,
    plSql_ExternalProcedureDeclaration,
    plSql_ProcedureImplementation,
    Pragma,
    plSql_PragmaTimestamp,
    plSql_PragmaRestrictReferences,
    FunctionClause,
    plSql_FunctionInvokerRightsClause,
    plSql_Expression,
    plSql_ParameterValue,
    plSql_Statement,
    plSql_PipelinedClause,
    plSql_ResultCacheClause,
    plSql_DeterministicClause,
    Item,
    plSql_Pragma,
    plSql_ItemDeclaration,
    plSql_ProcedureDeclaration,
    plSql_Item,
    plSql_ProcedureContent,
    plSql_ProcedureInvokerRightsClause,
    plSql_ParameterSequence,
    NameDeclaration,
    plSql_VariableDeclaration,
    plSql_ParameterDeclaration,
    plSql_LoopVariableDeclaration,
    plSql_ProcedureDefinition,
    CompilationUnit,
    plSql_Package,
    plSql_Procedure,
    plSql_CompilationUnit,
    plSql_FunctionContent,
    plSql_FunctionClause,
    plSql_Function,
    InvokerRight,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_plsql_namedeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_NameDeclaration)


def test_plsql_namedeclaration_constructor_exists():
    assert callable(plSql_NameDeclaration.__init__)


def test_plsql_namedeclaration_constructor_args():
    sig = inspect.signature(plSql_NameDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql_namedeclaration_has_name():
    assert hasattr(plSql_NameDeclaration, "name")
    descriptor = None
    for klass in plSql_NameDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql_name_is_not_abstract():
    assert not inspect.isabstract(plSql_Name)


def test_plsql_name_constructor_exists():
    assert callable(plSql_Name.__init__)


def test_plsql_name_constructor_args():
    sig = inspect.signature(plSql_Name.__init__)
    params = list(sig.parameters.keys())



def test_plsql_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(plSql_QualifiedName)


def test_plsql_qualifiedname_constructor_exists():
    assert callable(plSql_QualifiedName.__init__)


def test_plsql_qualifiedname_constructor_args():
    sig = inspect.signature(plSql_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_plsql_ifstatementelsebranch_is_not_abstract():
    assert not inspect.isabstract(plSql_IfStatementElseBranch)


def test_plsql_ifstatementelsebranch_constructor_exists():
    assert callable(plSql_IfStatementElseBranch.__init__)


def test_plsql_ifstatementelsebranch_constructor_args():
    sig = inspect.signature(plSql_IfStatementElseBranch.__init__)
    params = list(sig.parameters.keys())



def test_plsql_ifstatementelsifbranch_is_not_abstract():
    assert not inspect.isabstract(plSql_IfStatementElsifBranch)


def test_plsql_ifstatementelsifbranch_constructor_exists():
    assert callable(plSql_IfStatementElsifBranch.__init__)


def test_plsql_ifstatementelsifbranch_constructor_args():
    sig = inspect.signature(plSql_IfStatementElsifBranch.__init__)
    params = list(sig.parameters.keys())



def test_fetchstatementintoclause_is_not_abstract():
    assert not inspect.isabstract(FetchStatementIntoClause)


def test_fetchstatementintoclause_constructor_exists():
    assert callable(FetchStatementIntoClause.__init__)


def test_fetchstatementintoclause_constructor_args():
    sig = inspect.signature(FetchStatementIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql_fetchstatementbulkintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatementBulkIntoClause)


def test_plsql_fetchstatementbulkintoclause_constructor_exists():
    assert callable(plSql_FetchStatementBulkIntoClause.__init__)


def test_plsql_fetchstatementbulkintoclause_constructor_args():
    sig = inspect.signature(plSql_FetchStatementBulkIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql_fetchstatementsingleintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatementSingleIntoClause)


def test_plsql_fetchstatementsingleintoclause_constructor_exists():
    assert callable(plSql_FetchStatementSingleIntoClause.__init__)


def test_plsql_fetchstatementsingleintoclause_constructor_args():
    sig = inspect.signature(plSql_FetchStatementSingleIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_forloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ForLoopStatement)


def test_plsql_forloopstatement_constructor_exists():
    assert callable(plSql_ForLoopStatement.__init__)


def test_plsql_forloopstatement_constructor_args():
    sig = inspect.signature(plSql_ForLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_whileloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_WhileLoopStatement)


def test_plsql_whileloopstatement_constructor_exists():
    assert callable(plSql_WhileLoopStatement.__init__)


def test_plsql_whileloopstatement_constructor_args():
    sig = inspect.signature(plSql_WhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_basicloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_BasicLoopStatement)


def test_plsql_basicloopstatement_constructor_exists():
    assert callable(plSql_BasicLoopStatement.__init__)


def test_plsql_basicloopstatement_constructor_args():
    sig = inspect.signature(plSql_BasicLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_casestatementelsebranch_is_not_abstract():
    assert not inspect.isabstract(plSql_CaseStatementElseBranch)


def test_plsql_casestatementelsebranch_constructor_exists():
    assert callable(plSql_CaseStatementElseBranch.__init__)


def test_plsql_casestatementelsebranch_constructor_args():
    sig = inspect.signature(plSql_CaseStatementElseBranch.__init__)
    params = list(sig.parameters.keys())



def test_plsql_casestatementwhenbranch_is_not_abstract():
    assert not inspect.isabstract(plSql_CaseStatementWhenBranch)


def test_plsql_casestatementwhenbranch_constructor_exists():
    assert callable(plSql_CaseStatementWhenBranch.__init__)


def test_plsql_casestatementwhenbranch_constructor_args():
    sig = inspect.signature(plSql_CaseStatementWhenBranch.__init__)
    params = list(sig.parameters.keys())



def test_plsql_fetchstatementintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatementIntoClause)


def test_plsql_fetchstatementintoclause_constructor_exists():
    assert callable(plSql_FetchStatementIntoClause.__init__)


def test_plsql_fetchstatementintoclause_constructor_args():
    sig = inspect.signature(plSql_FetchStatementIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql_variableref_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableRef)


def test_plsql_variableref_constructor_exists():
    assert callable(plSql_VariableRef.__init__)


def test_plsql_variableref_constructor_args():
    sig = inspect.signature(plSql_VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "isHostRef" in params, "Missing parameter 'isHostRef'"

def test_plsql_variableref_has_isHostRef():
    assert hasattr(plSql_VariableRef, "isHostRef")
    descriptor = None
    for klass in plSql_VariableRef.__mro__:
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



def test_plsql_nullliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_NullLiteralExpression)


def test_plsql_nullliteralexpression_constructor_exists():
    assert callable(plSql_NullLiteralExpression.__init__)


def test_plsql_nullliteralexpression_constructor_args():
    sig = inspect.signature(plSql_NullLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_variablerefexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableRefExpression)


def test_plsql_variablerefexpression_constructor_exists():
    assert callable(plSql_VariableRefExpression.__init__)


def test_plsql_variablerefexpression_constructor_args():
    sig = inspect.signature(plSql_VariableRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_stringliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_StringLiteralExpression)


def test_plsql_stringliteralexpression_constructor_exists():
    assert callable(plSql_StringLiteralExpression.__init__)


def test_plsql_stringliteralexpression_constructor_args():
    sig = inspect.signature(plSql_StringLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_plsql_stringliteralexpression_has_value():
    assert hasattr(plSql_StringLiteralExpression, "value")
    descriptor = None
    for klass in plSql_StringLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_BooleanLiteralExpression)


def test_plsql_booleanliteralexpression_constructor_exists():
    assert callable(plSql_BooleanLiteralExpression.__init__)


def test_plsql_booleanliteralexpression_constructor_args():
    sig = inspect.signature(plSql_BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_plsql_booleanliteralexpression_has_value():
    assert hasattr(plSql_BooleanLiteralExpression, "value")
    descriptor = None
    for klass in plSql_BooleanLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql_intliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_IntLiteralExpression)


def test_plsql_intliteralexpression_constructor_exists():
    assert callable(plSql_IntLiteralExpression.__init__)


def test_plsql_intliteralexpression_constructor_args():
    sig = inspect.signature(plSql_IntLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_plsql_intliteralexpression_has_value():
    assert hasattr(plSql_IntLiteralExpression, "value")
    descriptor = None
    for klass in plSql_IntLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_plsql_variablevalue_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableValue)


def test_plsql_variablevalue_constructor_exists():
    assert callable(plSql_VariableValue.__init__)


def test_plsql_variablevalue_constructor_args():
    sig = inspect.signature(plSql_VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_itemdeclaration_is_not_abstract():
    assert not inspect.isabstract(ItemDeclaration)


def test_itemdeclaration_constructor_exists():
    assert callable(ItemDeclaration.__init__)


def test_itemdeclaration_constructor_args():
    sig = inspect.signature(ItemDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_assignmenttarget_is_not_abstract():
    assert not inspect.isabstract(AssignmentTarget)


def test_assignmenttarget_constructor_exists():
    assert callable(AssignmentTarget.__init__)


def test_assignmenttarget_constructor_args():
    sig = inspect.signature(AssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_plsql_variableassignmenttarget_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableAssignmentTarget)


def test_plsql_variableassignmenttarget_constructor_exists():
    assert callable(plSql_VariableAssignmentTarget.__init__)


def test_plsql_variableassignmenttarget_constructor_args():
    sig = inspect.signature(plSql_VariableAssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_plsql_assignmenttarget_is_not_abstract():
    assert not inspect.isabstract(plSql_AssignmentTarget)


def test_plsql_assignmenttarget_constructor_exists():
    assert callable(plSql_AssignmentTarget.__init__)


def test_plsql_assignmenttarget_constructor_args():
    sig = inspect.signature(plSql_AssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_continuestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ContinueStatement)


def test_plsql_continuestatement_constructor_exists():
    assert callable(plSql_ContinueStatement.__init__)


def test_plsql_continuestatement_constructor_args():
    sig = inspect.signature(plSql_ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelName" in params, "Missing parameter 'labelName'"

def test_plsql_continuestatement_has_labelName():
    assert hasattr(plSql_ContinueStatement, "labelName")
    descriptor = None
    for klass in plSql_ContinueStatement.__mro__:
        if "labelName" in klass.__dict__:
            descriptor = klass.__dict__["labelName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_fetchstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatement)


def test_plsql_fetchstatement_constructor_exists():
    assert callable(plSql_FetchStatement.__init__)


def test_plsql_fetchstatement_constructor_args():
    sig = inspect.signature(plSql_FetchStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_exitstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ExitStatement)


def test_plsql_exitstatement_constructor_exists():
    assert callable(plSql_ExitStatement.__init__)


def test_plsql_exitstatement_constructor_args():
    sig = inspect.signature(plSql_ExitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelName" in params, "Missing parameter 'labelName'"

def test_plsql_exitstatement_has_labelName():
    assert hasattr(plSql_ExitStatement, "labelName")
    descriptor = None
    for klass in plSql_ExitStatement.__mro__:
        if "labelName" in klass.__dict__:
            descriptor = klass.__dict__["labelName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_returnstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ReturnStatement)


def test_plsql_returnstatement_constructor_exists():
    assert callable(plSql_ReturnStatement.__init__)


def test_plsql_returnstatement_constructor_args():
    sig = inspect.signature(plSql_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_ifstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_IfStatement)


def test_plsql_ifstatement_constructor_exists():
    assert callable(plSql_IfStatement.__init__)


def test_plsql_ifstatement_constructor_args():
    sig = inspect.signature(plSql_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_casestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_CaseStatement)


def test_plsql_casestatement_constructor_exists():
    assert callable(plSql_CaseStatement.__init__)


def test_plsql_casestatement_constructor_args():
    sig = inspect.signature(plSql_CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"

def test_plsql_casestatement_has_endLabel():
    assert hasattr(plSql_CaseStatement, "endLabel")
    descriptor = None
    for klass in plSql_CaseStatement.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)



def test_plsql_loopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_LoopStatement)


def test_plsql_loopstatement_constructor_exists():
    assert callable(plSql_LoopStatement.__init__)


def test_plsql_loopstatement_constructor_args():
    sig = inspect.signature(plSql_LoopStatement.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"

def test_plsql_loopstatement_has_endLabel():
    assert hasattr(plSql_LoopStatement, "endLabel")
    descriptor = None
    for klass in plSql_LoopStatement.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)



def test_plsql_raisestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_RaiseStatement)


def test_plsql_raisestatement_constructor_exists():
    assert callable(plSql_RaiseStatement.__init__)


def test_plsql_raisestatement_constructor_args():
    sig = inspect.signature(plSql_RaiseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionName" in params, "Missing parameter 'exceptionName'"

def test_plsql_raisestatement_has_exceptionName():
    assert hasattr(plSql_RaiseStatement, "exceptionName")
    descriptor = None
    for klass in plSql_RaiseStatement.__mro__:
        if "exceptionName" in klass.__dict__:
            descriptor = klass.__dict__["exceptionName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_closestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_CloseStatement)


def test_plsql_closestatement_constructor_exists():
    assert callable(plSql_CloseStatement.__init__)


def test_plsql_closestatement_constructor_args():
    sig = inspect.signature(plSql_CloseStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_nullstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_NullStatement)


def test_plsql_nullstatement_constructor_exists():
    assert callable(plSql_NullStatement.__init__)


def test_plsql_nullstatement_constructor_args():
    sig = inspect.signature(plSql_NullStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_gotostatement_is_not_abstract():
    assert not inspect.isabstract(plSql_GotoStatement)


def test_plsql_gotostatement_constructor_exists():
    assert callable(plSql_GotoStatement.__init__)


def test_plsql_gotostatement_constructor_args():
    sig = inspect.signature(plSql_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_blockstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_BlockStatement)


def test_plsql_blockstatement_constructor_exists():
    assert callable(plSql_BlockStatement.__init__)


def test_plsql_blockstatement_constructor_args():
    sig = inspect.signature(plSql_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_AssignmentStatement)


def test_plsql_assignmentstatement_constructor_exists():
    assert callable(plSql_AssignmentStatement.__init__)


def test_plsql_assignmentstatement_constructor_args():
    sig = inspect.signature(plSql_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_label_is_not_abstract():
    assert not inspect.isabstract(plSql_Label)


def test_plsql_label_constructor_exists():
    assert callable(plSql_Label.__init__)


def test_plsql_label_constructor_args():
    sig = inspect.signature(plSql_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql_label_has_name():
    assert hasattr(plSql_Label, "name")
    descriptor = None
    for klass in plSql_Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_functioncontent_is_not_abstract():
    assert not inspect.isabstract(FunctionContent)


def test_functioncontent_constructor_exists():
    assert callable(FunctionContent.__init__)


def test_functioncontent_constructor_args():
    sig = inspect.signature(FunctionContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql_functionimplementation_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionImplementation)


def test_plsql_functionimplementation_constructor_exists():
    assert callable(plSql_FunctionImplementation.__init__)


def test_plsql_functionimplementation_constructor_args():
    sig = inspect.signature(plSql_FunctionImplementation.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statementbody_is_not_abstract():
    assert not inspect.isabstract(plSql_StatementBody)


def test_plsql_statementbody_constructor_exists():
    assert callable(plSql_StatementBody.__init__)


def test_plsql_statementbody_constructor_args():
    sig = inspect.signature(plSql_StatementBody.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"

def test_plsql_statementbody_has_endName():
    assert hasattr(plSql_StatementBody, "endName")
    descriptor = None
    for klass in plSql_StatementBody.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_declaresection_is_not_abstract():
    assert not inspect.isabstract(plSql_DeclareSection)


def test_plsql_declaresection_constructor_exists():
    assert callable(plSql_DeclareSection.__init__)


def test_plsql_declaresection_constructor_args():
    sig = inspect.signature(plSql_DeclareSection.__init__)
    params = list(sig.parameters.keys())



def test_procedurecontent_is_not_abstract():
    assert not inspect.isabstract(ProcedureContent)


def test_procedurecontent_constructor_exists():
    assert callable(ProcedureContent.__init__)


def test_procedurecontent_constructor_args():
    sig = inspect.signature(ProcedureContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql_externalproceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ExternalProcedureDeclaration)


def test_plsql_externalproceduredeclaration_constructor_exists():
    assert callable(plSql_ExternalProcedureDeclaration.__init__)


def test_plsql_externalproceduredeclaration_constructor_args():
    sig = inspect.signature(plSql_ExternalProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_procedureimplementation_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureImplementation)


def test_plsql_procedureimplementation_constructor_exists():
    assert callable(plSql_ProcedureImplementation.__init__)


def test_plsql_procedureimplementation_constructor_args():
    sig = inspect.signature(plSql_ProcedureImplementation.__init__)
    params = list(sig.parameters.keys())



def test_pragma_is_not_abstract():
    assert not inspect.isabstract(Pragma)


def test_pragma_constructor_exists():
    assert callable(Pragma.__init__)


def test_pragma_constructor_args():
    sig = inspect.signature(Pragma.__init__)
    params = list(sig.parameters.keys())



def test_plsql_pragmatimestamp_is_not_abstract():
    assert not inspect.isabstract(plSql_PragmaTimestamp)


def test_plsql_pragmatimestamp_constructor_exists():
    assert callable(plSql_PragmaTimestamp.__init__)


def test_plsql_pragmatimestamp_constructor_args():
    sig = inspect.signature(plSql_PragmaTimestamp.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_plsql_pragmatimestamp_has_timestamp():
    assert hasattr(plSql_PragmaTimestamp, "timestamp")
    descriptor = None
    for klass in plSql_PragmaTimestamp.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



def test_plsql_pragmarestrictreferences_is_not_abstract():
    assert not inspect.isabstract(plSql_PragmaRestrictReferences)


def test_plsql_pragmarestrictreferences_constructor_exists():
    assert callable(plSql_PragmaRestrictReferences.__init__)


def test_plsql_pragmarestrictreferences_constructor_args():
    sig = inspect.signature(plSql_PragmaRestrictReferences.__init__)
    params = list(sig.parameters.keys())
    assert "restrictions" in params, "Missing parameter 'restrictions'"

def test_plsql_pragmarestrictreferences_has_restrictions():
    assert hasattr(plSql_PragmaRestrictReferences, "restrictions")
    descriptor = None
    for klass in plSql_PragmaRestrictReferences.__mro__:
        if "restrictions" in klass.__dict__:
            descriptor = klass.__dict__["restrictions"]
            break
    assert isinstance(descriptor, property)



def test_functionclause_is_not_abstract():
    assert not inspect.isabstract(FunctionClause)


def test_functionclause_constructor_exists():
    assert callable(FunctionClause.__init__)


def test_functionclause_constructor_args():
    sig = inspect.signature(FunctionClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql_functioninvokerrightsclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionInvokerRightsClause)


def test_plsql_functioninvokerrightsclause_constructor_exists():
    assert callable(plSql_FunctionInvokerRightsClause.__init__)


def test_plsql_functioninvokerrightsclause_constructor_args():
    sig = inspect.signature(plSql_FunctionInvokerRightsClause.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_plsql_functioninvokerrightsclause_has_right():
    assert hasattr(plSql_FunctionInvokerRightsClause, "right")
    descriptor = None
    for klass in plSql_FunctionInvokerRightsClause.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_plsql_expression_is_not_abstract():
    assert not inspect.isabstract(plSql_Expression)


def test_plsql_expression_constructor_exists():
    assert callable(plSql_Expression.__init__)


def test_plsql_expression_constructor_args():
    sig = inspect.signature(plSql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_plsql_parametervalue_is_not_abstract():
    assert not inspect.isabstract(plSql_ParameterValue)


def test_plsql_parametervalue_constructor_exists():
    assert callable(plSql_ParameterValue.__init__)


def test_plsql_parametervalue_constructor_args():
    sig = inspect.signature(plSql_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_plsql_statement_is_not_abstract():
    assert not inspect.isabstract(plSql_Statement)


def test_plsql_statement_constructor_exists():
    assert callable(plSql_Statement.__init__)


def test_plsql_statement_constructor_args():
    sig = inspect.signature(plSql_Statement.__init__)
    params = list(sig.parameters.keys())



def test_plsql_pipelinedclause_is_not_abstract():
    assert not inspect.isabstract(plSql_PipelinedClause)


def test_plsql_pipelinedclause_constructor_exists():
    assert callable(plSql_PipelinedClause.__init__)


def test_plsql_pipelinedclause_constructor_args():
    sig = inspect.signature(plSql_PipelinedClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql_resultcacheclause_is_not_abstract():
    assert not inspect.isabstract(plSql_ResultCacheClause)


def test_plsql_resultcacheclause_constructor_exists():
    assert callable(plSql_ResultCacheClause.__init__)


def test_plsql_resultcacheclause_constructor_args():
    sig = inspect.signature(plSql_ResultCacheClause.__init__)
    params = list(sig.parameters.keys())
    assert "dataSources" in params, "Missing parameter 'dataSources'"

def test_plsql_resultcacheclause_has_dataSources():
    assert hasattr(plSql_ResultCacheClause, "dataSources")
    descriptor = None
    for klass in plSql_ResultCacheClause.__mro__:
        if "dataSources" in klass.__dict__:
            descriptor = klass.__dict__["dataSources"]
            break
    assert isinstance(descriptor, property)



def test_plsql_deterministicclause_is_not_abstract():
    assert not inspect.isabstract(plSql_DeterministicClause)


def test_plsql_deterministicclause_constructor_exists():
    assert callable(plSql_DeterministicClause.__init__)


def test_plsql_deterministicclause_constructor_args():
    sig = inspect.signature(plSql_DeterministicClause.__init__)
    params = list(sig.parameters.keys())



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_plsql_pragma_is_not_abstract():
    assert not inspect.isabstract(plSql_Pragma)


def test_plsql_pragma_constructor_exists():
    assert callable(plSql_Pragma.__init__)


def test_plsql_pragma_constructor_args():
    sig = inspect.signature(plSql_Pragma.__init__)
    params = list(sig.parameters.keys())



def test_plsql_itemdeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ItemDeclaration)


def test_plsql_itemdeclaration_constructor_exists():
    assert callable(plSql_ItemDeclaration.__init__)


def test_plsql_itemdeclaration_constructor_args():
    sig = inspect.signature(plSql_ItemDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureDeclaration)


def test_plsql_proceduredeclaration_constructor_exists():
    assert callable(plSql_ProcedureDeclaration.__init__)


def test_plsql_proceduredeclaration_constructor_args():
    sig = inspect.signature(plSql_ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_plsql_proceduredeclaration_has_name():
    assert hasattr(plSql_ProcedureDeclaration, "name")
    descriptor = None
    for klass in plSql_ProcedureDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_plsql_item_is_not_abstract():
    assert not inspect.isabstract(plSql_Item)


def test_plsql_item_constructor_exists():
    assert callable(plSql_Item.__init__)


def test_plsql_item_constructor_args():
    sig = inspect.signature(plSql_Item.__init__)
    params = list(sig.parameters.keys())



def test_plsql_procedurecontent_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureContent)


def test_plsql_procedurecontent_constructor_exists():
    assert callable(plSql_ProcedureContent.__init__)


def test_plsql_procedurecontent_constructor_args():
    sig = inspect.signature(plSql_ProcedureContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql_procedureinvokerrightsclause_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureInvokerRightsClause)


def test_plsql_procedureinvokerrightsclause_constructor_exists():
    assert callable(plSql_ProcedureInvokerRightsClause.__init__)


def test_plsql_procedureinvokerrightsclause_constructor_args():
    sig = inspect.signature(plSql_ProcedureInvokerRightsClause.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_plsql_procedureinvokerrightsclause_has_right():
    assert hasattr(plSql_ProcedureInvokerRightsClause, "right")
    descriptor = None
    for klass in plSql_ProcedureInvokerRightsClause.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_plsql_parametersequence_is_not_abstract():
    assert not inspect.isabstract(plSql_ParameterSequence)


def test_plsql_parametersequence_constructor_exists():
    assert callable(plSql_ParameterSequence.__init__)


def test_plsql_parametersequence_constructor_args():
    sig = inspect.signature(plSql_ParameterSequence.__init__)
    params = list(sig.parameters.keys())



def test_namedeclaration_is_not_abstract():
    assert not inspect.isabstract(NameDeclaration)


def test_namedeclaration_constructor_exists():
    assert callable(NameDeclaration.__init__)


def test_namedeclaration_constructor_args():
    sig = inspect.signature(NameDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableDeclaration)


def test_plsql_variabledeclaration_constructor_exists():
    assert callable(plSql_VariableDeclaration.__init__)


def test_plsql_variabledeclaration_constructor_args():
    sig = inspect.signature(plSql_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "isConstant" in params, "Missing parameter 'isConstant'"
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"

def test_plsql_variabledeclaration_has_dataType():
    assert hasattr(plSql_VariableDeclaration, "dataType")
    descriptor = None
    for klass in plSql_VariableDeclaration.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_plsql_variabledeclaration_has_isConstant():
    assert hasattr(plSql_VariableDeclaration, "isConstant")
    descriptor = None
    for klass in plSql_VariableDeclaration.__mro__:
        if "isConstant" in klass.__dict__:
            descriptor = klass.__dict__["isConstant"]
            break
    assert isinstance(descriptor, property)

def test_plsql_variabledeclaration_has_isNotNull():
    assert hasattr(plSql_VariableDeclaration, "isNotNull")
    descriptor = None
    for klass in plSql_VariableDeclaration.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)



def test_plsql_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ParameterDeclaration)


def test_plsql_parameterdeclaration_constructor_exists():
    assert callable(plSql_ParameterDeclaration.__init__)


def test_plsql_parameterdeclaration_constructor_args():
    sig = inspect.signature(plSql_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_plsql_parameterdeclaration_has_dataType():
    assert hasattr(plSql_ParameterDeclaration, "dataType")
    descriptor = None
    for klass in plSql_ParameterDeclaration.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_plsql_parameterdeclaration_has_behavior():
    assert hasattr(plSql_ParameterDeclaration, "behavior")
    descriptor = None
    for klass in plSql_ParameterDeclaration.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_plsql_loopvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_LoopVariableDeclaration)


def test_plsql_loopvariabledeclaration_constructor_exists():
    assert callable(plSql_LoopVariableDeclaration.__init__)


def test_plsql_loopvariabledeclaration_constructor_args():
    sig = inspect.signature(plSql_LoopVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_plsql_proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureDefinition)


def test_plsql_proceduredefinition_constructor_exists():
    assert callable(plSql_ProcedureDefinition.__init__)


def test_plsql_proceduredefinition_constructor_args():
    sig = inspect.signature(plSql_ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_plsql_package_is_not_abstract():
    assert not inspect.isabstract(plSql_Package)


def test_plsql_package_constructor_exists():
    assert callable(plSql_Package.__init__)


def test_plsql_package_constructor_args():
    sig = inspect.signature(plSql_Package.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"
    assert "schemaName" in params, "Missing parameter 'schemaName'"

def test_plsql_package_has_endName():
    assert hasattr(plSql_Package, "endName")
    descriptor = None
    for klass in plSql_Package.__mro__:
        if "endName" in klass.__dict__:
            descriptor = klass.__dict__["endName"]
            break
    assert isinstance(descriptor, property)

def test_plsql_package_has_schemaName():
    assert hasattr(plSql_Package, "schemaName")
    descriptor = None
    for klass in plSql_Package.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_procedure_is_not_abstract():
    assert not inspect.isabstract(plSql_Procedure)


def test_plsql_procedure_constructor_exists():
    assert callable(plSql_Procedure.__init__)


def test_plsql_procedure_constructor_args():
    sig = inspect.signature(plSql_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"

def test_plsql_procedure_has_schemaName():
    assert hasattr(plSql_Procedure, "schemaName")
    descriptor = None
    for klass in plSql_Procedure.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)



def test_plsql_compilationunit_is_not_abstract():
    assert not inspect.isabstract(plSql_CompilationUnit)


def test_plsql_compilationunit_constructor_exists():
    assert callable(plSql_CompilationUnit.__init__)


def test_plsql_compilationunit_constructor_args():
    sig = inspect.signature(plSql_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_plsql_functioncontent_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionContent)


def test_plsql_functioncontent_constructor_exists():
    assert callable(plSql_FunctionContent.__init__)


def test_plsql_functioncontent_constructor_args():
    sig = inspect.signature(plSql_FunctionContent.__init__)
    params = list(sig.parameters.keys())



def test_plsql_functionclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionClause)


def test_plsql_functionclause_constructor_exists():
    assert callable(plSql_FunctionClause.__init__)


def test_plsql_functionclause_constructor_args():
    sig = inspect.signature(plSql_FunctionClause.__init__)
    params = list(sig.parameters.keys())



def test_plsql_function_is_not_abstract():
    assert not inspect.isabstract(plSql_Function)


def test_plsql_function_constructor_exists():
    assert callable(plSql_Function.__init__)


def test_plsql_function_constructor_args():
    sig = inspect.signature(plSql_Function.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "returnType" in params, "Missing parameter 'returnType'"

def test_plsql_function_has_schemaName():
    assert hasattr(plSql_Function, "schemaName")
    descriptor = None
    for klass in plSql_Function.__mro__:
        if "schemaName" in klass.__dict__:
            descriptor = klass.__dict__["schemaName"]
            break
    assert isinstance(descriptor, property)

def test_plsql_function_has_returnType():
    assert hasattr(plSql_Function, "returnType")
    descriptor = None
    for klass in plSql_Function.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

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
plSql_NameDeclaration_strategy = st.builds(
    plSql_NameDeclaration,
    name=
        safe_text
)
plSql_Name_strategy = st.builds(
    plSql_Name,
)
plSql_QualifiedName_strategy = st.builds(
    plSql_QualifiedName,
)
plSql_IfStatementElseBranch_strategy = st.builds(
    plSql_IfStatementElseBranch,
)
plSql_IfStatementElsifBranch_strategy = st.builds(
    plSql_IfStatementElsifBranch,
)
FetchStatementIntoClause_strategy = st.builds(
    FetchStatementIntoClause,
)
plSql_FetchStatementBulkIntoClause_strategy = st.builds(
    plSql_FetchStatementBulkIntoClause,
)
plSql_FetchStatementSingleIntoClause_strategy = st.builds(
    plSql_FetchStatementSingleIntoClause,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
plSql_ForLoopStatement_strategy = st.builds(
    plSql_ForLoopStatement,
)
plSql_WhileLoopStatement_strategy = st.builds(
    plSql_WhileLoopStatement,
)
plSql_BasicLoopStatement_strategy = st.builds(
    plSql_BasicLoopStatement,
)
plSql_CaseStatementElseBranch_strategy = st.builds(
    plSql_CaseStatementElseBranch,
)
plSql_CaseStatementWhenBranch_strategy = st.builds(
    plSql_CaseStatementWhenBranch,
)
plSql_FetchStatementIntoClause_strategy = st.builds(
    plSql_FetchStatementIntoClause,
)
plSql_VariableRef_strategy = st.builds(
    plSql_VariableRef,
    isHostRef=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
plSql_NullLiteralExpression_strategy = st.builds(
    plSql_NullLiteralExpression,
)
plSql_VariableRefExpression_strategy = st.builds(
    plSql_VariableRefExpression,
)
plSql_StringLiteralExpression_strategy = st.builds(
    plSql_StringLiteralExpression,
    value=
        safe_text
)
plSql_BooleanLiteralExpression_strategy = st.builds(
    plSql_BooleanLiteralExpression,
    value=
        safe_text
)
plSql_IntLiteralExpression_strategy = st.builds(
    plSql_IntLiteralExpression,
    value=
        st.integers()
)
plSql_VariableValue_strategy = st.builds(
    plSql_VariableValue,
)
ItemDeclaration_strategy = st.builds(
    ItemDeclaration,
)
AssignmentTarget_strategy = st.builds(
    AssignmentTarget,
)
plSql_VariableAssignmentTarget_strategy = st.builds(
    plSql_VariableAssignmentTarget,
)
plSql_AssignmentTarget_strategy = st.builds(
    plSql_AssignmentTarget,
)
Statement_strategy = st.builds(
    Statement,
)
plSql_ContinueStatement_strategy = st.builds(
    plSql_ContinueStatement,
    labelName=
        safe_text
)
plSql_FetchStatement_strategy = st.builds(
    plSql_FetchStatement,
)
plSql_ExitStatement_strategy = st.builds(
    plSql_ExitStatement,
    labelName=
        safe_text
)
plSql_ReturnStatement_strategy = st.builds(
    plSql_ReturnStatement,
)
plSql_IfStatement_strategy = st.builds(
    plSql_IfStatement,
)
plSql_CaseStatement_strategy = st.builds(
    plSql_CaseStatement,
    endLabel=
        safe_text
)
plSql_LoopStatement_strategy = st.builds(
    plSql_LoopStatement,
    endLabel=
        safe_text
)
plSql_RaiseStatement_strategy = st.builds(
    plSql_RaiseStatement,
    exceptionName=
        safe_text
)
plSql_CloseStatement_strategy = st.builds(
    plSql_CloseStatement,
)
plSql_NullStatement_strategy = st.builds(
    plSql_NullStatement,
)
plSql_GotoStatement_strategy = st.builds(
    plSql_GotoStatement,
)
plSql_BlockStatement_strategy = st.builds(
    plSql_BlockStatement,
)
plSql_AssignmentStatement_strategy = st.builds(
    plSql_AssignmentStatement,
)
plSql_Label_strategy = st.builds(
    plSql_Label,
    name=
        safe_text
)
FunctionContent_strategy = st.builds(
    FunctionContent,
)
plSql_FunctionImplementation_strategy = st.builds(
    plSql_FunctionImplementation,
)
plSql_StatementBody_strategy = st.builds(
    plSql_StatementBody,
    endName=
        safe_text
)
plSql_DeclareSection_strategy = st.builds(
    plSql_DeclareSection,
)
ProcedureContent_strategy = st.builds(
    ProcedureContent,
)
plSql_ExternalProcedureDeclaration_strategy = st.builds(
    plSql_ExternalProcedureDeclaration,
)
plSql_ProcedureImplementation_strategy = st.builds(
    plSql_ProcedureImplementation,
)
Pragma_strategy = st.builds(
    Pragma,
)
plSql_PragmaTimestamp_strategy = st.builds(
    plSql_PragmaTimestamp,
    timestamp=
        safe_text
)
plSql_PragmaRestrictReferences_strategy = st.builds(
    plSql_PragmaRestrictReferences,
    restrictions=
        safe_text
)
FunctionClause_strategy = st.builds(
    FunctionClause,
)
plSql_FunctionInvokerRightsClause_strategy = st.builds(
    plSql_FunctionInvokerRightsClause,
    right=
        safe_text
)
plSql_Expression_strategy = st.builds(
    plSql_Expression,
)
plSql_ParameterValue_strategy = st.builds(
    plSql_ParameterValue,
)
plSql_Statement_strategy = st.builds(
    plSql_Statement,
)
plSql_PipelinedClause_strategy = st.builds(
    plSql_PipelinedClause,
)
plSql_ResultCacheClause_strategy = st.builds(
    plSql_ResultCacheClause,
    dataSources=
        safe_text
)
plSql_DeterministicClause_strategy = st.builds(
    plSql_DeterministicClause,
)
Item_strategy = st.builds(
    Item,
)
plSql_Pragma_strategy = st.builds(
    plSql_Pragma,
)
plSql_ItemDeclaration_strategy = st.builds(
    plSql_ItemDeclaration,
)
plSql_ProcedureDeclaration_strategy = st.builds(
    plSql_ProcedureDeclaration,
    name=
        safe_text
)
plSql_Item_strategy = st.builds(
    plSql_Item,
)
plSql_ProcedureContent_strategy = st.builds(
    plSql_ProcedureContent,
)
plSql_ProcedureInvokerRightsClause_strategy = st.builds(
    plSql_ProcedureInvokerRightsClause,
    right=
        safe_text
)
plSql_ParameterSequence_strategy = st.builds(
    plSql_ParameterSequence,
)
NameDeclaration_strategy = st.builds(
    NameDeclaration,
)
plSql_VariableDeclaration_strategy = st.builds(
    plSql_VariableDeclaration,
    dataType=
        safe_text,
    isConstant=
        st.booleans(),
    isNotNull=
        st.booleans()
)
plSql_ParameterDeclaration_strategy = st.builds(
    plSql_ParameterDeclaration,
    dataType=
        safe_text,
    behavior=
        safe_text
)
plSql_LoopVariableDeclaration_strategy = st.builds(
    plSql_LoopVariableDeclaration,
)
plSql_ProcedureDefinition_strategy = st.builds(
    plSql_ProcedureDefinition,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
plSql_Package_strategy = st.builds(
    plSql_Package,
    endName=
        safe_text,
    schemaName=
        safe_text
)
plSql_Procedure_strategy = st.builds(
    plSql_Procedure,
    schemaName=
        safe_text
)
plSql_CompilationUnit_strategy = st.builds(
    plSql_CompilationUnit,
)
plSql_FunctionContent_strategy = st.builds(
    plSql_FunctionContent,
)
plSql_FunctionClause_strategy = st.builds(
    plSql_FunctionClause,
)
plSql_Function_strategy = st.builds(
    plSql_Function,
    schemaName=
        safe_text,
    returnType=
        safe_text
)

@given(instance=plSql_NameDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_namedeclaration_instantiation(instance):
    assert isinstance(instance, plSql_NameDeclaration)



@given(instance=plSql_NameDeclaration_strategy)
def test_plsql_namedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plSql_Name_strategy)
@settings(max_examples=50)
def test_plsql_name_instantiation(instance):
    assert isinstance(instance, plSql_Name)

@given(instance=plSql_QualifiedName_strategy)
@settings(max_examples=50)
def test_plsql_qualifiedname_instantiation(instance):
    assert isinstance(instance, plSql_QualifiedName)

@given(instance=plSql_IfStatementElseBranch_strategy)
@settings(max_examples=50)
def test_plsql_ifstatementelsebranch_instantiation(instance):
    assert isinstance(instance, plSql_IfStatementElseBranch)

@given(instance=plSql_IfStatementElsifBranch_strategy)
@settings(max_examples=50)
def test_plsql_ifstatementelsifbranch_instantiation(instance):
    assert isinstance(instance, plSql_IfStatementElsifBranch)

@given(instance=FetchStatementIntoClause_strategy)
@settings(max_examples=50)
def test_fetchstatementintoclause_instantiation(instance):
    assert isinstance(instance, FetchStatementIntoClause)

@given(instance=plSql_FetchStatementBulkIntoClause_strategy)
@settings(max_examples=50)
def test_plsql_fetchstatementbulkintoclause_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatementBulkIntoClause)

@given(instance=plSql_FetchStatementSingleIntoClause_strategy)
@settings(max_examples=50)
def test_plsql_fetchstatementsingleintoclause_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatementSingleIntoClause)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=plSql_ForLoopStatement_strategy)
@settings(max_examples=50)
def test_plsql_forloopstatement_instantiation(instance):
    assert isinstance(instance, plSql_ForLoopStatement)

@given(instance=plSql_WhileLoopStatement_strategy)
@settings(max_examples=50)
def test_plsql_whileloopstatement_instantiation(instance):
    assert isinstance(instance, plSql_WhileLoopStatement)

@given(instance=plSql_BasicLoopStatement_strategy)
@settings(max_examples=50)
def test_plsql_basicloopstatement_instantiation(instance):
    assert isinstance(instance, plSql_BasicLoopStatement)

@given(instance=plSql_CaseStatementElseBranch_strategy)
@settings(max_examples=50)
def test_plsql_casestatementelsebranch_instantiation(instance):
    assert isinstance(instance, plSql_CaseStatementElseBranch)

@given(instance=plSql_CaseStatementWhenBranch_strategy)
@settings(max_examples=50)
def test_plsql_casestatementwhenbranch_instantiation(instance):
    assert isinstance(instance, plSql_CaseStatementWhenBranch)

@given(instance=plSql_FetchStatementIntoClause_strategy)
@settings(max_examples=50)
def test_plsql_fetchstatementintoclause_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatementIntoClause)

@given(instance=plSql_VariableRef_strategy)
@settings(max_examples=50)
def test_plsql_variableref_instantiation(instance):
    assert isinstance(instance, plSql_VariableRef)



@given(instance=plSql_VariableRef_strategy)
def test_plsql_variableref_isHostRef_setter(instance):
    original = instance.isHostRef
    instance.isHostRef = original
    assert instance.isHostRef == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=plSql_NullLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql_nullliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql_NullLiteralExpression)

@given(instance=plSql_VariableRefExpression_strategy)
@settings(max_examples=50)
def test_plsql_variablerefexpression_instantiation(instance):
    assert isinstance(instance, plSql_VariableRefExpression)

@given(instance=plSql_StringLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql_stringliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql_StringLiteralExpression)



@given(instance=plSql_StringLiteralExpression_strategy)
def test_plsql_stringliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plSql_BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql_BooleanLiteralExpression)



@given(instance=plSql_BooleanLiteralExpression_strategy)
def test_plsql_booleanliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plSql_IntLiteralExpression_strategy)
@settings(max_examples=50)
def test_plsql_intliteralexpression_instantiation(instance):
    assert isinstance(instance, plSql_IntLiteralExpression)



@given(instance=plSql_IntLiteralExpression_strategy)
def test_plsql_intliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=plSql_VariableValue_strategy)
@settings(max_examples=50)
def test_plsql_variablevalue_instantiation(instance):
    assert isinstance(instance, plSql_VariableValue)

@given(instance=ItemDeclaration_strategy)
@settings(max_examples=50)
def test_itemdeclaration_instantiation(instance):
    assert isinstance(instance, ItemDeclaration)

@given(instance=AssignmentTarget_strategy)
@settings(max_examples=50)
def test_assignmenttarget_instantiation(instance):
    assert isinstance(instance, AssignmentTarget)

@given(instance=plSql_VariableAssignmentTarget_strategy)
@settings(max_examples=50)
def test_plsql_variableassignmenttarget_instantiation(instance):
    assert isinstance(instance, plSql_VariableAssignmentTarget)

@given(instance=plSql_AssignmentTarget_strategy)
@settings(max_examples=50)
def test_plsql_assignmenttarget_instantiation(instance):
    assert isinstance(instance, plSql_AssignmentTarget)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=plSql_ContinueStatement_strategy)
@settings(max_examples=50)
def test_plsql_continuestatement_instantiation(instance):
    assert isinstance(instance, plSql_ContinueStatement)



@given(instance=plSql_ContinueStatement_strategy)
def test_plsql_continuestatement_labelName_setter(instance):
    original = instance.labelName
    instance.labelName = original
    assert instance.labelName == original

@given(instance=plSql_FetchStatement_strategy)
@settings(max_examples=50)
def test_plsql_fetchstatement_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatement)

@given(instance=plSql_ExitStatement_strategy)
@settings(max_examples=50)
def test_plsql_exitstatement_instantiation(instance):
    assert isinstance(instance, plSql_ExitStatement)



@given(instance=plSql_ExitStatement_strategy)
def test_plsql_exitstatement_labelName_setter(instance):
    original = instance.labelName
    instance.labelName = original
    assert instance.labelName == original

@given(instance=plSql_ReturnStatement_strategy)
@settings(max_examples=50)
def test_plsql_returnstatement_instantiation(instance):
    assert isinstance(instance, plSql_ReturnStatement)

@given(instance=plSql_IfStatement_strategy)
@settings(max_examples=50)
def test_plsql_ifstatement_instantiation(instance):
    assert isinstance(instance, plSql_IfStatement)

@given(instance=plSql_CaseStatement_strategy)
@settings(max_examples=50)
def test_plsql_casestatement_instantiation(instance):
    assert isinstance(instance, plSql_CaseStatement)



@given(instance=plSql_CaseStatement_strategy)
def test_plsql_casestatement_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original

@given(instance=plSql_LoopStatement_strategy)
@settings(max_examples=50)
def test_plsql_loopstatement_instantiation(instance):
    assert isinstance(instance, plSql_LoopStatement)



@given(instance=plSql_LoopStatement_strategy)
def test_plsql_loopstatement_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original

@given(instance=plSql_RaiseStatement_strategy)
@settings(max_examples=50)
def test_plsql_raisestatement_instantiation(instance):
    assert isinstance(instance, plSql_RaiseStatement)



@given(instance=plSql_RaiseStatement_strategy)
def test_plsql_raisestatement_exceptionName_setter(instance):
    original = instance.exceptionName
    instance.exceptionName = original
    assert instance.exceptionName == original

@given(instance=plSql_CloseStatement_strategy)
@settings(max_examples=50)
def test_plsql_closestatement_instantiation(instance):
    assert isinstance(instance, plSql_CloseStatement)

@given(instance=plSql_NullStatement_strategy)
@settings(max_examples=50)
def test_plsql_nullstatement_instantiation(instance):
    assert isinstance(instance, plSql_NullStatement)

@given(instance=plSql_GotoStatement_strategy)
@settings(max_examples=50)
def test_plsql_gotostatement_instantiation(instance):
    assert isinstance(instance, plSql_GotoStatement)

@given(instance=plSql_BlockStatement_strategy)
@settings(max_examples=50)
def test_plsql_blockstatement_instantiation(instance):
    assert isinstance(instance, plSql_BlockStatement)

@given(instance=plSql_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_plsql_assignmentstatement_instantiation(instance):
    assert isinstance(instance, plSql_AssignmentStatement)

@given(instance=plSql_Label_strategy)
@settings(max_examples=50)
def test_plsql_label_instantiation(instance):
    assert isinstance(instance, plSql_Label)



@given(instance=plSql_Label_strategy)
def test_plsql_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FunctionContent_strategy)
@settings(max_examples=50)
def test_functioncontent_instantiation(instance):
    assert isinstance(instance, FunctionContent)

@given(instance=plSql_FunctionImplementation_strategy)
@settings(max_examples=50)
def test_plsql_functionimplementation_instantiation(instance):
    assert isinstance(instance, plSql_FunctionImplementation)

@given(instance=plSql_StatementBody_strategy)
@settings(max_examples=50)
def test_plsql_statementbody_instantiation(instance):
    assert isinstance(instance, plSql_StatementBody)



@given(instance=plSql_StatementBody_strategy)
def test_plsql_statementbody_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original

@given(instance=plSql_DeclareSection_strategy)
@settings(max_examples=50)
def test_plsql_declaresection_instantiation(instance):
    assert isinstance(instance, plSql_DeclareSection)

@given(instance=ProcedureContent_strategy)
@settings(max_examples=50)
def test_procedurecontent_instantiation(instance):
    assert isinstance(instance, ProcedureContent)

@given(instance=plSql_ExternalProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_externalproceduredeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ExternalProcedureDeclaration)

@given(instance=plSql_ProcedureImplementation_strategy)
@settings(max_examples=50)
def test_plsql_procedureimplementation_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureImplementation)

@given(instance=Pragma_strategy)
@settings(max_examples=50)
def test_pragma_instantiation(instance):
    assert isinstance(instance, Pragma)

@given(instance=plSql_PragmaTimestamp_strategy)
@settings(max_examples=50)
def test_plsql_pragmatimestamp_instantiation(instance):
    assert isinstance(instance, plSql_PragmaTimestamp)



@given(instance=plSql_PragmaTimestamp_strategy)
def test_plsql_pragmatimestamp_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=plSql_PragmaRestrictReferences_strategy)
@settings(max_examples=50)
def test_plsql_pragmarestrictreferences_instantiation(instance):
    assert isinstance(instance, plSql_PragmaRestrictReferences)



@given(instance=plSql_PragmaRestrictReferences_strategy)
def test_plsql_pragmarestrictreferences_restrictions_setter(instance):
    original = instance.restrictions
    instance.restrictions = original
    assert instance.restrictions == original

@given(instance=FunctionClause_strategy)
@settings(max_examples=50)
def test_functionclause_instantiation(instance):
    assert isinstance(instance, FunctionClause)

@given(instance=plSql_FunctionInvokerRightsClause_strategy)
@settings(max_examples=50)
def test_plsql_functioninvokerrightsclause_instantiation(instance):
    assert isinstance(instance, plSql_FunctionInvokerRightsClause)



@given(instance=plSql_FunctionInvokerRightsClause_strategy)
def test_plsql_functioninvokerrightsclause_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=plSql_Expression_strategy)
@settings(max_examples=50)
def test_plsql_expression_instantiation(instance):
    assert isinstance(instance, plSql_Expression)

@given(instance=plSql_ParameterValue_strategy)
@settings(max_examples=50)
def test_plsql_parametervalue_instantiation(instance):
    assert isinstance(instance, plSql_ParameterValue)

@given(instance=plSql_Statement_strategy)
@settings(max_examples=50)
def test_plsql_statement_instantiation(instance):
    assert isinstance(instance, plSql_Statement)

@given(instance=plSql_PipelinedClause_strategy)
@settings(max_examples=50)
def test_plsql_pipelinedclause_instantiation(instance):
    assert isinstance(instance, plSql_PipelinedClause)

@given(instance=plSql_ResultCacheClause_strategy)
@settings(max_examples=50)
def test_plsql_resultcacheclause_instantiation(instance):
    assert isinstance(instance, plSql_ResultCacheClause)



@given(instance=plSql_ResultCacheClause_strategy)
def test_plsql_resultcacheclause_dataSources_setter(instance):
    original = instance.dataSources
    instance.dataSources = original
    assert instance.dataSources == original

@given(instance=plSql_DeterministicClause_strategy)
@settings(max_examples=50)
def test_plsql_deterministicclause_instantiation(instance):
    assert isinstance(instance, plSql_DeterministicClause)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=plSql_Pragma_strategy)
@settings(max_examples=50)
def test_plsql_pragma_instantiation(instance):
    assert isinstance(instance, plSql_Pragma)

@given(instance=plSql_ItemDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_itemdeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ItemDeclaration)

@given(instance=plSql_ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_proceduredeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureDeclaration)



@given(instance=plSql_ProcedureDeclaration_strategy)
def test_plsql_proceduredeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=plSql_Item_strategy)
@settings(max_examples=50)
def test_plsql_item_instantiation(instance):
    assert isinstance(instance, plSql_Item)

@given(instance=plSql_ProcedureContent_strategy)
@settings(max_examples=50)
def test_plsql_procedurecontent_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureContent)

@given(instance=plSql_ProcedureInvokerRightsClause_strategy)
@settings(max_examples=50)
def test_plsql_procedureinvokerrightsclause_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureInvokerRightsClause)



@given(instance=plSql_ProcedureInvokerRightsClause_strategy)
def test_plsql_procedureinvokerrightsclause_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=plSql_ParameterSequence_strategy)
@settings(max_examples=50)
def test_plsql_parametersequence_instantiation(instance):
    assert isinstance(instance, plSql_ParameterSequence)

@given(instance=NameDeclaration_strategy)
@settings(max_examples=50)
def test_namedeclaration_instantiation(instance):
    assert isinstance(instance, NameDeclaration)

@given(instance=plSql_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_variabledeclaration_instantiation(instance):
    assert isinstance(instance, plSql_VariableDeclaration)



@given(instance=plSql_VariableDeclaration_strategy)
def test_plsql_variabledeclaration_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=plSql_VariableDeclaration_strategy)
def test_plsql_variabledeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original



@given(instance=plSql_VariableDeclaration_strategy)
def test_plsql_variabledeclaration_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original

@given(instance=plSql_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ParameterDeclaration)



@given(instance=plSql_ParameterDeclaration_strategy)
def test_plsql_parameterdeclaration_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=plSql_ParameterDeclaration_strategy)
def test_plsql_parameterdeclaration_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=plSql_LoopVariableDeclaration_strategy)
@settings(max_examples=50)
def test_plsql_loopvariabledeclaration_instantiation(instance):
    assert isinstance(instance, plSql_LoopVariableDeclaration)

@given(instance=plSql_ProcedureDefinition_strategy)
@settings(max_examples=50)
def test_plsql_proceduredefinition_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureDefinition)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=plSql_Package_strategy)
@settings(max_examples=50)
def test_plsql_package_instantiation(instance):
    assert isinstance(instance, plSql_Package)



@given(instance=plSql_Package_strategy)
def test_plsql_package_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original



@given(instance=plSql_Package_strategy)
def test_plsql_package_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=plSql_Procedure_strategy)
@settings(max_examples=50)
def test_plsql_procedure_instantiation(instance):
    assert isinstance(instance, plSql_Procedure)



@given(instance=plSql_Procedure_strategy)
def test_plsql_procedure_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original

@given(instance=plSql_CompilationUnit_strategy)
@settings(max_examples=50)
def test_plsql_compilationunit_instantiation(instance):
    assert isinstance(instance, plSql_CompilationUnit)

@given(instance=plSql_FunctionContent_strategy)
@settings(max_examples=50)
def test_plsql_functioncontent_instantiation(instance):
    assert isinstance(instance, plSql_FunctionContent)

@given(instance=plSql_FunctionClause_strategy)
@settings(max_examples=50)
def test_plsql_functionclause_instantiation(instance):
    assert isinstance(instance, plSql_FunctionClause)

@given(instance=plSql_Function_strategy)
@settings(max_examples=50)
def test_plsql_function_instantiation(instance):
    assert isinstance(instance, plSql_Function)



@given(instance=plSql_Function_strategy)
def test_plsql_function_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



@given(instance=plSql_Function_strategy)
def test_plsql_function_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original
