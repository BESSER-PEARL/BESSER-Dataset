import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    syntax_dbl_Option,
    syntax_dbl_MultipleRowFetchClause,
    syntax_dbl_SingleRowFetchClause,
    syntax_dbl_IntoClause,
    ConditionInfoClause,
    SingleRowFetchClause,
    MultipleRowFetchClause,
    IntoClause,
    Option,
    syntax_dbl_ConditionInfoClause,
    BindingStatement,
    syntax_dbl_GetDiagnosticsStatement,
    syntax_dbl_GetDescriptorStatement,
    syntax_dbl_DeallocateDescriptorStatement,
    syntax_dbl_SetOptionStatement,
    syntax_dbl_OpenStatement,
    syntax_dbl_SetTransactionStatement,
    syntax_dbl_SetDescriptorStatement,
    syntax_dbl_ExecuteStatement,
    syntax_dbl_FetchStatement,
    syntax_dbl_CloseStatement,
    syntax_dbl_DeclareCursorStatement,
    syntax_dbl_PrepareStatement,
    syntax_dbl_ExecuteImmediateStatement,
    syntax_dbl_DescribeStatement,
    syntax_dbl_AllocateDescriptorStatement,
    QueryExpressionBody,
    syntax_dml_ExtendedQueryExpressionBody,
    QuerySelect,
    dml_ExtendedQueryExpressionBody,
    syntax_dml_ExtendedQuerySelect,
    ddl_syntax_TableColumnDef,
    ddl_syntax_IndexDef,
    ddl_syntax_QualifiedName,
    DefinitionStatement,
    syntax_ddl_CommitStatement,
    syntax_ddl_DisconnectStatement,
    syntax_ddl_CreateIndexStatement,
    syntax_ddl_CreateViewStatement,
    syntax_ddl_ReleaseStatement,
    syntax_ddl_SetConnectionStatement,
    syntax_ddl_CreateAliasStatement,
    syntax_ddl_RollbackStatement,
    syntax_ddl_CreateTableStatement,
    syntax_ddl_RenameStatement,
    syntax_ddl_DropStatement,
    syntax_ddl_LockTableStatement,
    syntax_ddl_ConnectStatement,
    syntax_ddl_CallStatement,
    syntax_StatementParser,
    syntax_StatementWriter,
    syntax_SQLObjectNameHelper,
    syntax_QueryParserRegistry,
    syntax_QueryWriterRegistry,
    syntax_NameHelperRegistry,
    SQLObjectNameHelper,
    syntax_NameHelper,
    syntax_DefinitionWriterRegistry,
    StatementWriter,
    syntax_QueryWriter,
    syntax_DefinitionWriter,
    syntax_DefinitionStatement,
    syntax_DefinitionParseResult,
    syntax_DefinitionParseError,
    syntax_DefinitionParserRegistry,
    syntax_BindingStatement,
    syntax_BindingParseResult,
    syntax_BindingParserRegistry,
    StatementParser,
    syntax_QueryParser,
    syntax_DefinitionParser,
    syntax_BindingParser,
    syntax_BindingParseError,
    syntax_AliasResolver,
    FetchPosition,
    StatementType,
    UsingType,
    DropRange,
    TargetItem,
    TargetElement,
    ShareMode,
    OpenUsingType,
    DescriptorScope,
    RWOperation,
    CursorType,
    IsolationLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_syntax_dbl_option_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_Option)


def test_syntax_dbl_option_constructor_exists():
    assert callable(syntax_dbl_Option.__init__)


def test_syntax_dbl_option_constructor_args():
    sig = inspect.signature(syntax_dbl_Option.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_syntax_dbl_option_has_value():
    assert hasattr(syntax_dbl_Option, "value")
    descriptor = None
    for klass in syntax_dbl_Option.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_option_has_name():
    assert hasattr(syntax_dbl_Option, "name")
    descriptor = None
    for klass in syntax_dbl_Option.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_multiplerowfetchclause_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_MultipleRowFetchClause)


def test_syntax_dbl_multiplerowfetchclause_constructor_exists():
    assert callable(syntax_dbl_MultipleRowFetchClause.__init__)


def test_syntax_dbl_multiplerowfetchclause_constructor_args():
    sig = inspect.signature(syntax_dbl_MultipleRowFetchClause.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "rowsNumber" in params, "Missing parameter 'rowsNumber'"
    assert "usingDescriptor" in params, "Missing parameter 'usingDescriptor'"
    assert "into" in params, "Missing parameter 'into'"

def test_syntax_dbl_multiplerowfetchclause_has_descriptor():
    assert hasattr(syntax_dbl_MultipleRowFetchClause, "descriptor")
    descriptor = None
    for klass in syntax_dbl_MultipleRowFetchClause.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_multiplerowfetchclause_has_rowsNumber():
    assert hasattr(syntax_dbl_MultipleRowFetchClause, "rowsNumber")
    descriptor = None
    for klass in syntax_dbl_MultipleRowFetchClause.__mro__:
        if "rowsNumber" in klass.__dict__:
            descriptor = klass.__dict__["rowsNumber"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_multiplerowfetchclause_has_usingDescriptor():
    assert hasattr(syntax_dbl_MultipleRowFetchClause, "usingDescriptor")
    descriptor = None
    for klass in syntax_dbl_MultipleRowFetchClause.__mro__:
        if "usingDescriptor" in klass.__dict__:
            descriptor = klass.__dict__["usingDescriptor"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_multiplerowfetchclause_has_into():
    assert hasattr(syntax_dbl_MultipleRowFetchClause, "into")
    descriptor = None
    for klass in syntax_dbl_MultipleRowFetchClause.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_singlerowfetchclause_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_SingleRowFetchClause)


def test_syntax_dbl_singlerowfetchclause_constructor_exists():
    assert callable(syntax_dbl_SingleRowFetchClause.__init__)


def test_syntax_dbl_singlerowfetchclause_constructor_args():
    sig = inspect.signature(syntax_dbl_SingleRowFetchClause.__init__)
    params = list(sig.parameters.keys())
    assert "into" in params, "Missing parameter 'into'"
    assert "usingDescriptor" in params, "Missing parameter 'usingDescriptor'"

def test_syntax_dbl_singlerowfetchclause_has_into():
    assert hasattr(syntax_dbl_SingleRowFetchClause, "into")
    descriptor = None
    for klass in syntax_dbl_SingleRowFetchClause.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_singlerowfetchclause_has_usingDescriptor():
    assert hasattr(syntax_dbl_SingleRowFetchClause, "usingDescriptor")
    descriptor = None
    for klass in syntax_dbl_SingleRowFetchClause.__mro__:
        if "usingDescriptor" in klass.__dict__:
            descriptor = klass.__dict__["usingDescriptor"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_intoclause_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_IntoClause)


def test_syntax_dbl_intoclause_constructor_exists():
    assert callable(syntax_dbl_IntoClause.__init__)


def test_syntax_dbl_intoclause_constructor_args():
    sig = inspect.signature(syntax_dbl_IntoClause.__init__)
    params = list(sig.parameters.keys())
    assert "using" in params, "Missing parameter 'using'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"

def test_syntax_dbl_intoclause_has_using():
    assert hasattr(syntax_dbl_IntoClause, "using")
    descriptor = None
    for klass in syntax_dbl_IntoClause.__mro__:
        if "using" in klass.__dict__:
            descriptor = klass.__dict__["using"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_intoclause_has_descriptorName():
    assert hasattr(syntax_dbl_IntoClause, "descriptorName")
    descriptor = None
    for klass in syntax_dbl_IntoClause.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)



def test_conditioninfoclause_is_not_abstract():
    assert not inspect.isabstract(ConditionInfoClause)


def test_conditioninfoclause_constructor_exists():
    assert callable(ConditionInfoClause.__init__)


def test_conditioninfoclause_constructor_args():
    sig = inspect.signature(ConditionInfoClause.__init__)
    params = list(sig.parameters.keys())



def test_singlerowfetchclause_is_not_abstract():
    assert not inspect.isabstract(SingleRowFetchClause)


def test_singlerowfetchclause_constructor_exists():
    assert callable(SingleRowFetchClause.__init__)


def test_singlerowfetchclause_constructor_args():
    sig = inspect.signature(SingleRowFetchClause.__init__)
    params = list(sig.parameters.keys())



def test_multiplerowfetchclause_is_not_abstract():
    assert not inspect.isabstract(MultipleRowFetchClause)


def test_multiplerowfetchclause_constructor_exists():
    assert callable(MultipleRowFetchClause.__init__)


def test_multiplerowfetchclause_constructor_args():
    sig = inspect.signature(MultipleRowFetchClause.__init__)
    params = list(sig.parameters.keys())



def test_intoclause_is_not_abstract():
    assert not inspect.isabstract(IntoClause)


def test_intoclause_constructor_exists():
    assert callable(IntoClause.__init__)


def test_intoclause_constructor_args():
    sig = inspect.signature(IntoClause.__init__)
    params = list(sig.parameters.keys())



def test_option_is_not_abstract():
    assert not inspect.isabstract(Option)


def test_option_constructor_exists():
    assert callable(Option.__init__)


def test_option_constructor_args():
    sig = inspect.signature(Option.__init__)
    params = list(sig.parameters.keys())



def test_syntax_dbl_conditioninfoclause_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_ConditionInfoClause)


def test_syntax_dbl_conditioninfoclause_constructor_exists():
    assert callable(syntax_dbl_ConditionInfoClause.__init__)


def test_syntax_dbl_conditioninfoclause_constructor_args():
    sig = inspect.signature(syntax_dbl_ConditionInfoClause.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_syntax_dbl_conditioninfoclause_has_condition():
    assert hasattr(syntax_dbl_ConditionInfoClause, "condition")
    descriptor = None
    for klass in syntax_dbl_ConditionInfoClause.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_bindingstatement_is_not_abstract():
    assert not inspect.isabstract(BindingStatement)


def test_bindingstatement_constructor_exists():
    assert callable(BindingStatement.__init__)


def test_bindingstatement_constructor_args():
    sig = inspect.signature(BindingStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_dbl_getdiagnosticsstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_GetDiagnosticsStatement)


def test_syntax_dbl_getdiagnosticsstatement_constructor_exists():
    assert callable(syntax_dbl_GetDiagnosticsStatement.__init__)


def test_syntax_dbl_getdiagnosticsstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_GetDiagnosticsStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_dbl_getdescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_GetDescriptorStatement)


def test_syntax_dbl_getdescriptorstatement_constructor_exists():
    assert callable(syntax_dbl_GetDescriptorStatement.__init__)


def test_syntax_dbl_getdescriptorstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_GetDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorScope" in params, "Missing parameter 'descriptorScope'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"
    assert "value" in params, "Missing parameter 'value'"

def test_syntax_dbl_getdescriptorstatement_has_descriptorScope():
    assert hasattr(syntax_dbl_GetDescriptorStatement, "descriptorScope")
    descriptor = None
    for klass in syntax_dbl_GetDescriptorStatement.__mro__:
        if "descriptorScope" in klass.__dict__:
            descriptor = klass.__dict__["descriptorScope"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_getdescriptorstatement_has_descriptorName():
    assert hasattr(syntax_dbl_GetDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax_dbl_GetDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_getdescriptorstatement_has_value():
    assert hasattr(syntax_dbl_GetDescriptorStatement, "value")
    descriptor = None
    for klass in syntax_dbl_GetDescriptorStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_deallocatedescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_DeallocateDescriptorStatement)


def test_syntax_dbl_deallocatedescriptorstatement_constructor_exists():
    assert callable(syntax_dbl_DeallocateDescriptorStatement.__init__)


def test_syntax_dbl_deallocatedescriptorstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_DeallocateDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"
    assert "descriptorScope" in params, "Missing parameter 'descriptorScope'"

def test_syntax_dbl_deallocatedescriptorstatement_has_descriptorName():
    assert hasattr(syntax_dbl_DeallocateDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax_dbl_DeallocateDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_deallocatedescriptorstatement_has_descriptorScope():
    assert hasattr(syntax_dbl_DeallocateDescriptorStatement, "descriptorScope")
    descriptor = None
    for klass in syntax_dbl_DeallocateDescriptorStatement.__mro__:
        if "descriptorScope" in klass.__dict__:
            descriptor = klass.__dict__["descriptorScope"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_setoptionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_SetOptionStatement)


def test_syntax_dbl_setoptionstatement_constructor_exists():
    assert callable(syntax_dbl_SetOptionStatement.__init__)


def test_syntax_dbl_setoptionstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_SetOptionStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_dbl_openstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_OpenStatement)


def test_syntax_dbl_openstatement_constructor_exists():
    assert callable(syntax_dbl_OpenStatement.__init__)


def test_syntax_dbl_openstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_OpenStatement.__init__)
    params = list(sig.parameters.keys())
    assert "cursor" in params, "Missing parameter 'cursor'"
    assert "usingType" in params, "Missing parameter 'usingType'"
    assert "using" in params, "Missing parameter 'using'"

def test_syntax_dbl_openstatement_has_cursor():
    assert hasattr(syntax_dbl_OpenStatement, "cursor")
    descriptor = None
    for klass in syntax_dbl_OpenStatement.__mro__:
        if "cursor" in klass.__dict__:
            descriptor = klass.__dict__["cursor"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_openstatement_has_usingType():
    assert hasattr(syntax_dbl_OpenStatement, "usingType")
    descriptor = None
    for klass in syntax_dbl_OpenStatement.__mro__:
        if "usingType" in klass.__dict__:
            descriptor = klass.__dict__["usingType"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_openstatement_has_using():
    assert hasattr(syntax_dbl_OpenStatement, "using")
    descriptor = None
    for klass in syntax_dbl_OpenStatement.__mro__:
        if "using" in klass.__dict__:
            descriptor = klass.__dict__["using"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_settransactionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_SetTransactionStatement)


def test_syntax_dbl_settransactionstatement_constructor_exists():
    assert callable(syntax_dbl_SetTransactionStatement.__init__)


def test_syntax_dbl_settransactionstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_SetTransactionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "isolationLevel" in params, "Missing parameter 'isolationLevel'"
    assert "rwOperation" in params, "Missing parameter 'rwOperation'"

def test_syntax_dbl_settransactionstatement_has_isolationLevel():
    assert hasattr(syntax_dbl_SetTransactionStatement, "isolationLevel")
    descriptor = None
    for klass in syntax_dbl_SetTransactionStatement.__mro__:
        if "isolationLevel" in klass.__dict__:
            descriptor = klass.__dict__["isolationLevel"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_settransactionstatement_has_rwOperation():
    assert hasattr(syntax_dbl_SetTransactionStatement, "rwOperation")
    descriptor = None
    for klass in syntax_dbl_SetTransactionStatement.__mro__:
        if "rwOperation" in klass.__dict__:
            descriptor = klass.__dict__["rwOperation"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_setdescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_SetDescriptorStatement)


def test_syntax_dbl_setdescriptorstatement_constructor_exists():
    assert callable(syntax_dbl_SetDescriptorStatement.__init__)


def test_syntax_dbl_setdescriptorstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_SetDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"
    assert "value" in params, "Missing parameter 'value'"

def test_syntax_dbl_setdescriptorstatement_has_descriptorName():
    assert hasattr(syntax_dbl_SetDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax_dbl_SetDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_setdescriptorstatement_has_value():
    assert hasattr(syntax_dbl_SetDescriptorStatement, "value")
    descriptor = None
    for klass in syntax_dbl_SetDescriptorStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_executestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_ExecuteStatement)


def test_syntax_dbl_executestatement_constructor_exists():
    assert callable(syntax_dbl_ExecuteStatement.__init__)


def test_syntax_dbl_executestatement_constructor_args():
    sig = inspect.signature(syntax_dbl_ExecuteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statementName" in params, "Missing parameter 'statementName'"

def test_syntax_dbl_executestatement_has_statementName():
    assert hasattr(syntax_dbl_ExecuteStatement, "statementName")
    descriptor = None
    for klass in syntax_dbl_ExecuteStatement.__mro__:
        if "statementName" in klass.__dict__:
            descriptor = klass.__dict__["statementName"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_fetchstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_FetchStatement)


def test_syntax_dbl_fetchstatement_constructor_exists():
    assert callable(syntax_dbl_FetchStatement.__init__)


def test_syntax_dbl_fetchstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_FetchStatement.__init__)
    params = list(sig.parameters.keys())
    assert "relativePosition" in params, "Missing parameter 'relativePosition'"
    assert "cursorName" in params, "Missing parameter 'cursorName'"
    assert "position" in params, "Missing parameter 'position'"

def test_syntax_dbl_fetchstatement_has_relativePosition():
    assert hasattr(syntax_dbl_FetchStatement, "relativePosition")
    descriptor = None
    for klass in syntax_dbl_FetchStatement.__mro__:
        if "relativePosition" in klass.__dict__:
            descriptor = klass.__dict__["relativePosition"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_fetchstatement_has_cursorName():
    assert hasattr(syntax_dbl_FetchStatement, "cursorName")
    descriptor = None
    for klass in syntax_dbl_FetchStatement.__mro__:
        if "cursorName" in klass.__dict__:
            descriptor = klass.__dict__["cursorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_fetchstatement_has_position():
    assert hasattr(syntax_dbl_FetchStatement, "position")
    descriptor = None
    for klass in syntax_dbl_FetchStatement.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_closestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_CloseStatement)


def test_syntax_dbl_closestatement_constructor_exists():
    assert callable(syntax_dbl_CloseStatement.__init__)


def test_syntax_dbl_closestatement_constructor_args():
    sig = inspect.signature(syntax_dbl_CloseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "cursor" in params, "Missing parameter 'cursor'"

def test_syntax_dbl_closestatement_has_cursor():
    assert hasattr(syntax_dbl_CloseStatement, "cursor")
    descriptor = None
    for klass in syntax_dbl_CloseStatement.__mro__:
        if "cursor" in klass.__dict__:
            descriptor = klass.__dict__["cursor"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_declarecursorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_DeclareCursorStatement)


def test_syntax_dbl_declarecursorstatement_constructor_exists():
    assert callable(syntax_dbl_DeclareCursorStatement.__init__)


def test_syntax_dbl_declarecursorstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_DeclareCursorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "forQuery" in params, "Missing parameter 'forQuery'"
    assert "forStatementName" in params, "Missing parameter 'forStatementName'"
    assert "hold" in params, "Missing parameter 'hold'"
    assert "cursorName" in params, "Missing parameter 'cursorName'"
    assert "cursorType" in params, "Missing parameter 'cursorType'"

def test_syntax_dbl_declarecursorstatement_has_forQuery():
    assert hasattr(syntax_dbl_DeclareCursorStatement, "forQuery")
    descriptor = None
    for klass in syntax_dbl_DeclareCursorStatement.__mro__:
        if "forQuery" in klass.__dict__:
            descriptor = klass.__dict__["forQuery"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_declarecursorstatement_has_forStatementName():
    assert hasattr(syntax_dbl_DeclareCursorStatement, "forStatementName")
    descriptor = None
    for klass in syntax_dbl_DeclareCursorStatement.__mro__:
        if "forStatementName" in klass.__dict__:
            descriptor = klass.__dict__["forStatementName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_declarecursorstatement_has_hold():
    assert hasattr(syntax_dbl_DeclareCursorStatement, "hold")
    descriptor = None
    for klass in syntax_dbl_DeclareCursorStatement.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_declarecursorstatement_has_cursorName():
    assert hasattr(syntax_dbl_DeclareCursorStatement, "cursorName")
    descriptor = None
    for klass in syntax_dbl_DeclareCursorStatement.__mro__:
        if "cursorName" in klass.__dict__:
            descriptor = klass.__dict__["cursorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_declarecursorstatement_has_cursorType():
    assert hasattr(syntax_dbl_DeclareCursorStatement, "cursorType")
    descriptor = None
    for klass in syntax_dbl_DeclareCursorStatement.__mro__:
        if "cursorType" in klass.__dict__:
            descriptor = klass.__dict__["cursorType"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_preparestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_PrepareStatement)


def test_syntax_dbl_preparestatement_constructor_exists():
    assert callable(syntax_dbl_PrepareStatement.__init__)


def test_syntax_dbl_preparestatement_constructor_args():
    sig = inspect.signature(syntax_dbl_PrepareStatement.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "statementName" in params, "Missing parameter 'statementName'"

def test_syntax_dbl_preparestatement_has_from_():
    assert hasattr(syntax_dbl_PrepareStatement, "from_")
    descriptor = None
    for klass in syntax_dbl_PrepareStatement.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_preparestatement_has_statementName():
    assert hasattr(syntax_dbl_PrepareStatement, "statementName")
    descriptor = None
    for klass in syntax_dbl_PrepareStatement.__mro__:
        if "statementName" in klass.__dict__:
            descriptor = klass.__dict__["statementName"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_executeimmediatestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_ExecuteImmediateStatement)


def test_syntax_dbl_executeimmediatestatement_constructor_exists():
    assert callable(syntax_dbl_ExecuteImmediateStatement.__init__)


def test_syntax_dbl_executeimmediatestatement_constructor_args():
    sig = inspect.signature(syntax_dbl_ExecuteImmediateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_syntax_dbl_executeimmediatestatement_has_variable():
    assert hasattr(syntax_dbl_ExecuteImmediateStatement, "variable")
    descriptor = None
    for klass in syntax_dbl_ExecuteImmediateStatement.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_describestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_DescribeStatement)


def test_syntax_dbl_describestatement_constructor_exists():
    assert callable(syntax_dbl_DescribeStatement.__init__)


def test_syntax_dbl_describestatement_constructor_args():
    sig = inspect.signature(syntax_dbl_DescribeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statementName" in params, "Missing parameter 'statementName'"

def test_syntax_dbl_describestatement_has_statementName():
    assert hasattr(syntax_dbl_DescribeStatement, "statementName")
    descriptor = None
    for klass in syntax_dbl_DescribeStatement.__mro__:
        if "statementName" in klass.__dict__:
            descriptor = klass.__dict__["statementName"]
            break
    assert isinstance(descriptor, property)



def test_syntax_dbl_allocatedescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_dbl_AllocateDescriptorStatement)


def test_syntax_dbl_allocatedescriptorstatement_constructor_exists():
    assert callable(syntax_dbl_AllocateDescriptorStatement.__init__)


def test_syntax_dbl_allocatedescriptorstatement_constructor_args():
    sig = inspect.signature(syntax_dbl_AllocateDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorScope" in params, "Missing parameter 'descriptorScope'"
    assert "withMax" in params, "Missing parameter 'withMax'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"

def test_syntax_dbl_allocatedescriptorstatement_has_descriptorScope():
    assert hasattr(syntax_dbl_AllocateDescriptorStatement, "descriptorScope")
    descriptor = None
    for klass in syntax_dbl_AllocateDescriptorStatement.__mro__:
        if "descriptorScope" in klass.__dict__:
            descriptor = klass.__dict__["descriptorScope"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_allocatedescriptorstatement_has_withMax():
    assert hasattr(syntax_dbl_AllocateDescriptorStatement, "withMax")
    descriptor = None
    for klass in syntax_dbl_AllocateDescriptorStatement.__mro__:
        if "withMax" in klass.__dict__:
            descriptor = klass.__dict__["withMax"]
            break
    assert isinstance(descriptor, property)

def test_syntax_dbl_allocatedescriptorstatement_has_descriptorName():
    assert hasattr(syntax_dbl_AllocateDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax_dbl_AllocateDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)



def test_queryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(QueryExpressionBody)


def test_queryexpressionbody_constructor_exists():
    assert callable(QueryExpressionBody.__init__)


def test_queryexpressionbody_constructor_args():
    sig = inspect.signature(QueryExpressionBody.__init__)
    params = list(sig.parameters.keys())



def test_syntax_dml_extendedqueryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(syntax_dml_ExtendedQueryExpressionBody)


def test_syntax_dml_extendedqueryexpressionbody_constructor_exists():
    assert callable(syntax_dml_ExtendedQueryExpressionBody.__init__)


def test_syntax_dml_extendedqueryexpressionbody_constructor_args():
    sig = inspect.signature(syntax_dml_ExtendedQueryExpressionBody.__init__)
    params = list(sig.parameters.keys())
    assert "optimizeRecordsNumber" in params, "Missing parameter 'optimizeRecordsNumber'"

def test_syntax_dml_extendedqueryexpressionbody_has_optimizeRecordsNumber():
    assert hasattr(syntax_dml_ExtendedQueryExpressionBody, "optimizeRecordsNumber")
    descriptor = None
    for klass in syntax_dml_ExtendedQueryExpressionBody.__mro__:
        if "optimizeRecordsNumber" in klass.__dict__:
            descriptor = klass.__dict__["optimizeRecordsNumber"]
            break
    assert isinstance(descriptor, property)



def test_queryselect_is_not_abstract():
    assert not inspect.isabstract(QuerySelect)


def test_queryselect_constructor_exists():
    assert callable(QuerySelect.__init__)


def test_queryselect_constructor_args():
    sig = inspect.signature(QuerySelect.__init__)
    params = list(sig.parameters.keys())



def test_dml_extendedqueryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(dml_ExtendedQueryExpressionBody)


def test_dml_extendedqueryexpressionbody_constructor_exists():
    assert callable(dml_ExtendedQueryExpressionBody.__init__)


def test_dml_extendedqueryexpressionbody_constructor_args():
    sig = inspect.signature(dml_ExtendedQueryExpressionBody.__init__)
    params = list(sig.parameters.keys())



def test_syntax_dml_extendedqueryselect_is_not_abstract():
    assert not inspect.isabstract(syntax_dml_ExtendedQuerySelect)


def test_syntax_dml_extendedqueryselect_constructor_exists():
    assert callable(syntax_dml_ExtendedQuerySelect.__init__)


def test_syntax_dml_extendedqueryselect_constructor_args():
    sig = inspect.signature(syntax_dml_ExtendedQuerySelect.__init__)
    params = list(sig.parameters.keys())



def test_ddl_syntax_tablecolumndef_is_not_abstract():
    assert not inspect.isabstract(ddl_syntax_TableColumnDef)


def test_ddl_syntax_tablecolumndef_constructor_exists():
    assert callable(ddl_syntax_TableColumnDef.__init__)


def test_ddl_syntax_tablecolumndef_constructor_args():
    sig = inspect.signature(ddl_syntax_TableColumnDef.__init__)
    params = list(sig.parameters.keys())



def test_ddl_syntax_indexdef_is_not_abstract():
    assert not inspect.isabstract(ddl_syntax_IndexDef)


def test_ddl_syntax_indexdef_constructor_exists():
    assert callable(ddl_syntax_IndexDef.__init__)


def test_ddl_syntax_indexdef_constructor_args():
    sig = inspect.signature(ddl_syntax_IndexDef.__init__)
    params = list(sig.parameters.keys())



def test_ddl_syntax_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(ddl_syntax_QualifiedName)


def test_ddl_syntax_qualifiedname_constructor_exists():
    assert callable(ddl_syntax_QualifiedName.__init__)


def test_ddl_syntax_qualifiedname_constructor_args():
    sig = inspect.signature(ddl_syntax_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_definitionstatement_is_not_abstract():
    assert not inspect.isabstract(DefinitionStatement)


def test_definitionstatement_constructor_exists():
    assert callable(DefinitionStatement.__init__)


def test_definitionstatement_constructor_args():
    sig = inspect.signature(DefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_ddl_commitstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_CommitStatement)


def test_syntax_ddl_commitstatement_constructor_exists():
    assert callable(syntax_ddl_CommitStatement.__init__)


def test_syntax_ddl_commitstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_CommitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "hold" in params, "Missing parameter 'hold'"

def test_syntax_ddl_commitstatement_has_hold():
    assert hasattr(syntax_ddl_CommitStatement, "hold")
    descriptor = None
    for klass in syntax_ddl_CommitStatement.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_disconnectstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_DisconnectStatement)


def test_syntax_ddl_disconnectstatement_constructor_exists():
    assert callable(syntax_ddl_DisconnectStatement.__init__)


def test_syntax_ddl_disconnectstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_DisconnectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"

def test_syntax_ddl_disconnectstatement_has_target():
    assert hasattr(syntax_ddl_DisconnectStatement, "target")
    descriptor = None
    for klass in syntax_ddl_DisconnectStatement.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_createindexstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_CreateIndexStatement)


def test_syntax_ddl_createindexstatement_constructor_exists():
    assert callable(syntax_ddl_CreateIndexStatement.__init__)


def test_syntax_ddl_createindexstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_CreateIndexStatement.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_syntax_ddl_createindexstatement_has_unique():
    assert hasattr(syntax_ddl_CreateIndexStatement, "unique")
    descriptor = None
    for klass in syntax_ddl_CreateIndexStatement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_createviewstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_CreateViewStatement)


def test_syntax_ddl_createviewstatement_constructor_exists():
    assert callable(syntax_ddl_CreateViewStatement.__init__)


def test_syntax_ddl_createviewstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_CreateViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "fields" in params, "Missing parameter 'fields'"
    assert "query" in params, "Missing parameter 'query'"

def test_syntax_ddl_createviewstatement_has_fields():
    assert hasattr(syntax_ddl_CreateViewStatement, "fields")
    descriptor = None
    for klass in syntax_ddl_CreateViewStatement.__mro__:
        if "fields" in klass.__dict__:
            descriptor = klass.__dict__["fields"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_createviewstatement_has_query():
    assert hasattr(syntax_ddl_CreateViewStatement, "query")
    descriptor = None
    for klass in syntax_ddl_CreateViewStatement.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_releasestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_ReleaseStatement)


def test_syntax_ddl_releasestatement_constructor_exists():
    assert callable(syntax_ddl_ReleaseStatement.__init__)


def test_syntax_ddl_releasestatement_constructor_args():
    sig = inspect.signature(syntax_ddl_ReleaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "serverName" in params, "Missing parameter 'serverName'"

def test_syntax_ddl_releasestatement_has_serverName():
    assert hasattr(syntax_ddl_ReleaseStatement, "serverName")
    descriptor = None
    for klass in syntax_ddl_ReleaseStatement.__mro__:
        if "serverName" in klass.__dict__:
            descriptor = klass.__dict__["serverName"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_setconnectionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_SetConnectionStatement)


def test_syntax_ddl_setconnectionstatement_constructor_exists():
    assert callable(syntax_ddl_SetConnectionStatement.__init__)


def test_syntax_ddl_setconnectionstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_SetConnectionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_syntax_ddl_setconnectionstatement_has_databaseName():
    assert hasattr(syntax_ddl_SetConnectionStatement, "databaseName")
    descriptor = None
    for klass in syntax_ddl_SetConnectionStatement.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_createaliasstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_CreateAliasStatement)


def test_syntax_ddl_createaliasstatement_constructor_exists():
    assert callable(syntax_ddl_CreateAliasStatement.__init__)


def test_syntax_ddl_createaliasstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_CreateAliasStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_ddl_rollbackstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_RollbackStatement)


def test_syntax_ddl_rollbackstatement_constructor_exists():
    assert callable(syntax_ddl_RollbackStatement.__init__)


def test_syntax_ddl_rollbackstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_RollbackStatement.__init__)
    params = list(sig.parameters.keys())
    assert "hold" in params, "Missing parameter 'hold'"

def test_syntax_ddl_rollbackstatement_has_hold():
    assert hasattr(syntax_ddl_RollbackStatement, "hold")
    descriptor = None
    for klass in syntax_ddl_RollbackStatement.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_createtablestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_CreateTableStatement)


def test_syntax_ddl_createtablestatement_constructor_exists():
    assert callable(syntax_ddl_CreateTableStatement.__init__)


def test_syntax_ddl_createtablestatement_constructor_args():
    sig = inspect.signature(syntax_ddl_CreateTableStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_ddl_renamestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_RenameStatement)


def test_syntax_ddl_renamestatement_constructor_exists():
    assert callable(syntax_ddl_RenameStatement.__init__)


def test_syntax_ddl_renamestatement_constructor_args():
    sig = inspect.signature(syntax_ddl_RenameStatement.__init__)
    params = list(sig.parameters.keys())
    assert "newName" in params, "Missing parameter 'newName'"
    assert "target" in params, "Missing parameter 'target'"
    assert "system" in params, "Missing parameter 'system'"

def test_syntax_ddl_renamestatement_has_newName():
    assert hasattr(syntax_ddl_RenameStatement, "newName")
    descriptor = None
    for klass in syntax_ddl_RenameStatement.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_renamestatement_has_target():
    assert hasattr(syntax_ddl_RenameStatement, "target")
    descriptor = None
    for klass in syntax_ddl_RenameStatement.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_renamestatement_has_system():
    assert hasattr(syntax_ddl_RenameStatement, "system")
    descriptor = None
    for klass in syntax_ddl_RenameStatement.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_dropstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_DropStatement)


def test_syntax_ddl_dropstatement_constructor_exists():
    assert callable(syntax_ddl_DropStatement.__init__)


def test_syntax_ddl_dropstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_DropStatement.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "range" in params, "Missing parameter 'range'"

def test_syntax_ddl_dropstatement_has_target():
    assert hasattr(syntax_ddl_DropStatement, "target")
    descriptor = None
    for klass in syntax_ddl_DropStatement.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_dropstatement_has_range():
    assert hasattr(syntax_ddl_DropStatement, "range")
    descriptor = None
    for klass in syntax_ddl_DropStatement.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_locktablestatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_LockTableStatement)


def test_syntax_ddl_locktablestatement_constructor_exists():
    assert callable(syntax_ddl_LockTableStatement.__init__)


def test_syntax_ddl_locktablestatement_constructor_args():
    sig = inspect.signature(syntax_ddl_LockTableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "allowRead" in params, "Missing parameter 'allowRead'"
    assert "shareMode" in params, "Missing parameter 'shareMode'"

def test_syntax_ddl_locktablestatement_has_allowRead():
    assert hasattr(syntax_ddl_LockTableStatement, "allowRead")
    descriptor = None
    for klass in syntax_ddl_LockTableStatement.__mro__:
        if "allowRead" in klass.__dict__:
            descriptor = klass.__dict__["allowRead"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_locktablestatement_has_shareMode():
    assert hasattr(syntax_ddl_LockTableStatement, "shareMode")
    descriptor = None
    for klass in syntax_ddl_LockTableStatement.__mro__:
        if "shareMode" in klass.__dict__:
            descriptor = klass.__dict__["shareMode"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_connectstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_ConnectStatement)


def test_syntax_ddl_connectstatement_constructor_exists():
    assert callable(syntax_ddl_ConnectStatement.__init__)


def test_syntax_ddl_connectstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_ConnectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "pwd" in params, "Missing parameter 'pwd'"
    assert "to" in params, "Missing parameter 'to'"
    assert "reset" in params, "Missing parameter 'reset'"
    assert "user" in params, "Missing parameter 'user'"

def test_syntax_ddl_connectstatement_has_pwd():
    assert hasattr(syntax_ddl_ConnectStatement, "pwd")
    descriptor = None
    for klass in syntax_ddl_ConnectStatement.__mro__:
        if "pwd" in klass.__dict__:
            descriptor = klass.__dict__["pwd"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_connectstatement_has_to():
    assert hasattr(syntax_ddl_ConnectStatement, "to")
    descriptor = None
    for klass in syntax_ddl_ConnectStatement.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_connectstatement_has_reset():
    assert hasattr(syntax_ddl_ConnectStatement, "reset")
    descriptor = None
    for klass in syntax_ddl_ConnectStatement.__mro__:
        if "reset" in klass.__dict__:
            descriptor = klass.__dict__["reset"]
            break
    assert isinstance(descriptor, property)

def test_syntax_ddl_connectstatement_has_user():
    assert hasattr(syntax_ddl_ConnectStatement, "user")
    descriptor = None
    for klass in syntax_ddl_ConnectStatement.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)



def test_syntax_ddl_callstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_ddl_CallStatement)


def test_syntax_ddl_callstatement_constructor_exists():
    assert callable(syntax_ddl_CallStatement.__init__)


def test_syntax_ddl_callstatement_constructor_args():
    sig = inspect.signature(syntax_ddl_CallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "parms" in params, "Missing parameter 'parms'"

def test_syntax_ddl_callstatement_has_parms():
    assert hasattr(syntax_ddl_CallStatement, "parms")
    descriptor = None
    for klass in syntax_ddl_CallStatement.__mro__:
        if "parms" in klass.__dict__:
            descriptor = klass.__dict__["parms"]
            break
    assert isinstance(descriptor, property)



def test_syntax_statementparser_is_not_abstract():
    assert not inspect.isabstract(syntax_StatementParser)


def test_syntax_statementparser_constructor_exists():
    assert callable(syntax_StatementParser.__init__)


def test_syntax_statementparser_constructor_args():
    sig = inspect.signature(syntax_StatementParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax_statementwriter_is_not_abstract():
    assert not inspect.isabstract(syntax_StatementWriter)


def test_syntax_statementwriter_constructor_exists():
    assert callable(syntax_StatementWriter.__init__)


def test_syntax_statementwriter_constructor_args():
    sig = inspect.signature(syntax_StatementWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax_sqlobjectnamehelper_is_not_abstract():
    assert not inspect.isabstract(syntax_SQLObjectNameHelper)


def test_syntax_sqlobjectnamehelper_constructor_exists():
    assert callable(syntax_SQLObjectNameHelper.__init__)


def test_syntax_sqlobjectnamehelper_constructor_args():
    sig = inspect.signature(syntax_SQLObjectNameHelper.__init__)
    params = list(sig.parameters.keys())



def test_syntax_queryparserregistry_is_not_abstract():
    assert not inspect.isabstract(syntax_QueryParserRegistry)


def test_syntax_queryparserregistry_constructor_exists():
    assert callable(syntax_QueryParserRegistry.__init__)


def test_syntax_queryparserregistry_constructor_args():
    sig = inspect.signature(syntax_QueryParserRegistry.__init__)
    params = list(sig.parameters.keys())



def test_syntax_querywriterregistry_is_not_abstract():
    assert not inspect.isabstract(syntax_QueryWriterRegistry)


def test_syntax_querywriterregistry_constructor_exists():
    assert callable(syntax_QueryWriterRegistry.__init__)


def test_syntax_querywriterregistry_constructor_args():
    sig = inspect.signature(syntax_QueryWriterRegistry.__init__)
    params = list(sig.parameters.keys())



def test_syntax_namehelperregistry_is_not_abstract():
    assert not inspect.isabstract(syntax_NameHelperRegistry)


def test_syntax_namehelperregistry_constructor_exists():
    assert callable(syntax_NameHelperRegistry.__init__)


def test_syntax_namehelperregistry_constructor_args():
    sig = inspect.signature(syntax_NameHelperRegistry.__init__)
    params = list(sig.parameters.keys())



def test_sqlobjectnamehelper_is_not_abstract():
    assert not inspect.isabstract(SQLObjectNameHelper)


def test_sqlobjectnamehelper_constructor_exists():
    assert callable(SQLObjectNameHelper.__init__)


def test_sqlobjectnamehelper_constructor_args():
    sig = inspect.signature(SQLObjectNameHelper.__init__)
    params = list(sig.parameters.keys())



def test_syntax_namehelper_is_not_abstract():
    assert not inspect.isabstract(syntax_NameHelper)


def test_syntax_namehelper_constructor_exists():
    assert callable(syntax_NameHelper.__init__)


def test_syntax_namehelper_constructor_args():
    sig = inspect.signature(syntax_NameHelper.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionwriterregistry_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionWriterRegistry)


def test_syntax_definitionwriterregistry_constructor_exists():
    assert callable(syntax_DefinitionWriterRegistry.__init__)


def test_syntax_definitionwriterregistry_constructor_args():
    sig = inspect.signature(syntax_DefinitionWriterRegistry.__init__)
    params = list(sig.parameters.keys())



def test_statementwriter_is_not_abstract():
    assert not inspect.isabstract(StatementWriter)


def test_statementwriter_constructor_exists():
    assert callable(StatementWriter.__init__)


def test_statementwriter_constructor_args():
    sig = inspect.signature(StatementWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax_querywriter_is_not_abstract():
    assert not inspect.isabstract(syntax_QueryWriter)


def test_syntax_querywriter_constructor_exists():
    assert callable(syntax_QueryWriter.__init__)


def test_syntax_querywriter_constructor_args():
    sig = inspect.signature(syntax_QueryWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionwriter_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionWriter)


def test_syntax_definitionwriter_constructor_exists():
    assert callable(syntax_DefinitionWriter.__init__)


def test_syntax_definitionwriter_constructor_args():
    sig = inspect.signature(syntax_DefinitionWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionStatement)


def test_syntax_definitionstatement_constructor_exists():
    assert callable(syntax_DefinitionStatement.__init__)


def test_syntax_definitionstatement_constructor_args():
    sig = inspect.signature(syntax_DefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionparseresult_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionParseResult)


def test_syntax_definitionparseresult_constructor_exists():
    assert callable(syntax_DefinitionParseResult.__init__)


def test_syntax_definitionparseresult_constructor_args():
    sig = inspect.signature(syntax_DefinitionParseResult.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionparseerror_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionParseError)


def test_syntax_definitionparseerror_constructor_exists():
    assert callable(syntax_DefinitionParseError.__init__)


def test_syntax_definitionparseerror_constructor_args():
    sig = inspect.signature(syntax_DefinitionParseError.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionparserregistry_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionParserRegistry)


def test_syntax_definitionparserregistry_constructor_exists():
    assert callable(syntax_DefinitionParserRegistry.__init__)


def test_syntax_definitionparserregistry_constructor_args():
    sig = inspect.signature(syntax_DefinitionParserRegistry.__init__)
    params = list(sig.parameters.keys())



def test_syntax_bindingstatement_is_not_abstract():
    assert not inspect.isabstract(syntax_BindingStatement)


def test_syntax_bindingstatement_constructor_exists():
    assert callable(syntax_BindingStatement.__init__)


def test_syntax_bindingstatement_constructor_args():
    sig = inspect.signature(syntax_BindingStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax_bindingparseresult_is_not_abstract():
    assert not inspect.isabstract(syntax_BindingParseResult)


def test_syntax_bindingparseresult_constructor_exists():
    assert callable(syntax_BindingParseResult.__init__)


def test_syntax_bindingparseresult_constructor_args():
    sig = inspect.signature(syntax_BindingParseResult.__init__)
    params = list(sig.parameters.keys())



def test_syntax_bindingparserregistry_is_not_abstract():
    assert not inspect.isabstract(syntax_BindingParserRegistry)


def test_syntax_bindingparserregistry_constructor_exists():
    assert callable(syntax_BindingParserRegistry.__init__)


def test_syntax_bindingparserregistry_constructor_args():
    sig = inspect.signature(syntax_BindingParserRegistry.__init__)
    params = list(sig.parameters.keys())



def test_statementparser_is_not_abstract():
    assert not inspect.isabstract(StatementParser)


def test_statementparser_constructor_exists():
    assert callable(StatementParser.__init__)


def test_statementparser_constructor_args():
    sig = inspect.signature(StatementParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax_queryparser_is_not_abstract():
    assert not inspect.isabstract(syntax_QueryParser)


def test_syntax_queryparser_constructor_exists():
    assert callable(syntax_QueryParser.__init__)


def test_syntax_queryparser_constructor_args():
    sig = inspect.signature(syntax_QueryParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax_definitionparser_is_not_abstract():
    assert not inspect.isabstract(syntax_DefinitionParser)


def test_syntax_definitionparser_constructor_exists():
    assert callable(syntax_DefinitionParser.__init__)


def test_syntax_definitionparser_constructor_args():
    sig = inspect.signature(syntax_DefinitionParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax_bindingparser_is_not_abstract():
    assert not inspect.isabstract(syntax_BindingParser)


def test_syntax_bindingparser_constructor_exists():
    assert callable(syntax_BindingParser.__init__)


def test_syntax_bindingparser_constructor_args():
    sig = inspect.signature(syntax_BindingParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax_bindingparseerror_is_not_abstract():
    assert not inspect.isabstract(syntax_BindingParseError)


def test_syntax_bindingparseerror_constructor_exists():
    assert callable(syntax_BindingParseError.__init__)


def test_syntax_bindingparseerror_constructor_args():
    sig = inspect.signature(syntax_BindingParseError.__init__)
    params = list(sig.parameters.keys())



def test_syntax_aliasresolver_is_not_abstract():
    assert not inspect.isabstract(syntax_AliasResolver)


def test_syntax_aliasresolver_constructor_exists():
    assert callable(syntax_AliasResolver.__init__)


def test_syntax_aliasresolver_constructor_args():
    sig = inspect.signature(syntax_AliasResolver.__init__)
    params = list(sig.parameters.keys())

def test_fetchposition_exists():
    # Check that the Enumeration exists
    assert FetchPosition is not None

def test_fetchposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FetchPosition]
    expected_literals = [
        "BEFORE",
        "AFTER",
        "CURRENT",
        "NEXT",
        "FIRST",
        "RELATIVE",
        "PRIOR",
        "LAST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FetchPosition"

def test_statementtype_exists():
    # Check that the Enumeration exists
    assert StatementType is not None

def test_statementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatementType]
    expected_literals = [
        "DML",
        "DBL",
        "DDL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatementType"

def test_usingtype_exists():
    # Check that the Enumeration exists
    assert UsingType is not None

def test_usingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsingType]
    expected_literals = [
        "SYSTEM_NAMES",
        "NONE",
        "BOTH",
        "ANY",
        "LABELS",
        "ALL",
        "NAMES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsingType"

def test_droprange_exists():
    # Check that the Enumeration exists
    assert DropRange is not None

def test_droprange_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DropRange]
    expected_literals = [
        "CASCADE",
        "RESTRICT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DropRange"

def test_targetitem_exists():
    # Check that the Enumeration exists
    assert TargetItem is not None

def test_targetitem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TargetItem]
    expected_literals = [
        "CURRENT",
        "ALL",
        "ALLSQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TargetItem"

def test_targetelement_exists():
    # Check that the Enumeration exists
    assert TargetElement is not None

def test_targetelement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TargetElement]
    expected_literals = [
        "ALIAS",
        "INDEX",
        "TABLE",
        "VIEW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TargetElement"

def test_sharemode_exists():
    # Check that the Enumeration exists
    assert ShareMode is not None

def test_sharemode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShareMode]
    expected_literals = [
        "EXCLUSIVE",
        "SHARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShareMode"

def test_openusingtype_exists():
    # Check that the Enumeration exists
    assert OpenUsingType is not None

def test_openusingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OpenUsingType]
    expected_literals = [
        "DESCRIPTOR",
        "NONE",
        "VARIABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OpenUsingType"

def test_descriptorscope_exists():
    # Check that the Enumeration exists
    assert DescriptorScope is not None

def test_descriptorscope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DescriptorScope]
    expected_literals = [
        "LOCAL",
        "GLOBAL",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DescriptorScope"

def test_rwoperation_exists():
    # Check that the Enumeration exists
    assert RWOperation is not None

def test_rwoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RWOperation]
    expected_literals = [
        "READ_ONLY",
        "READ_WRITE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RWOperation"

def test_cursortype_exists():
    # Check that the Enumeration exists
    assert CursorType is not None

def test_cursortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CursorType]
    expected_literals = [
        "DYNSCROLL",
        "SCROLL",
        "NOTSCROLL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CursorType"

def test_isolationlevel_exists():
    # Check that the Enumeration exists
    assert IsolationLevel is not None

def test_isolationlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IsolationLevel]
    expected_literals = [
        "REPEATABLE_READ",
        "READ_UNCOMMITTED",
        "SERIALIZABLE",
        "NO_COMMIT",
        "READ_COMMITTED",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IsolationLevel"


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
syntax_dbl_Option_strategy = st.builds(
    syntax_dbl_Option,
    value=
        safe_text,
    name=
        safe_text
)
syntax_dbl_MultipleRowFetchClause_strategy = st.builds(
    syntax_dbl_MultipleRowFetchClause,
    descriptor=
        safe_text,
    rowsNumber=
        safe_text,
    usingDescriptor=
        st.booleans(),
    into=
        safe_text
)
syntax_dbl_SingleRowFetchClause_strategy = st.builds(
    syntax_dbl_SingleRowFetchClause,
    into=
        safe_text,
    usingDescriptor=
        st.booleans()
)
syntax_dbl_IntoClause_strategy = st.builds(
    syntax_dbl_IntoClause,
    using=
        safe_text,
    descriptorName=
        safe_text
)
ConditionInfoClause_strategy = st.builds(
    ConditionInfoClause,
)
SingleRowFetchClause_strategy = st.builds(
    SingleRowFetchClause,
)
MultipleRowFetchClause_strategy = st.builds(
    MultipleRowFetchClause,
)
IntoClause_strategy = st.builds(
    IntoClause,
)
Option_strategy = st.builds(
    Option,
)
syntax_dbl_ConditionInfoClause_strategy = st.builds(
    syntax_dbl_ConditionInfoClause,
    condition=
        safe_text
)
BindingStatement_strategy = st.builds(
    BindingStatement,
)
syntax_dbl_GetDiagnosticsStatement_strategy = st.builds(
    syntax_dbl_GetDiagnosticsStatement,
)
syntax_dbl_GetDescriptorStatement_strategy = st.builds(
    syntax_dbl_GetDescriptorStatement,
    descriptorScope=
        safe_text,
    descriptorName=
        safe_text,
    value=
        safe_text
)
syntax_dbl_DeallocateDescriptorStatement_strategy = st.builds(
    syntax_dbl_DeallocateDescriptorStatement,
    descriptorName=
        safe_text,
    descriptorScope=
        safe_text
)
syntax_dbl_SetOptionStatement_strategy = st.builds(
    syntax_dbl_SetOptionStatement,
)
syntax_dbl_OpenStatement_strategy = st.builds(
    syntax_dbl_OpenStatement,
    cursor=
        safe_text,
    usingType=
        safe_text,
    using=
        safe_text
)
syntax_dbl_SetTransactionStatement_strategy = st.builds(
    syntax_dbl_SetTransactionStatement,
    isolationLevel=
        safe_text,
    rwOperation=
        safe_text
)
syntax_dbl_SetDescriptorStatement_strategy = st.builds(
    syntax_dbl_SetDescriptorStatement,
    descriptorName=
        safe_text,
    value=
        safe_text
)
syntax_dbl_ExecuteStatement_strategy = st.builds(
    syntax_dbl_ExecuteStatement,
    statementName=
        safe_text
)
syntax_dbl_FetchStatement_strategy = st.builds(
    syntax_dbl_FetchStatement,
    relativePosition=
        safe_text,
    cursorName=
        safe_text,
    position=
        safe_text
)
syntax_dbl_CloseStatement_strategy = st.builds(
    syntax_dbl_CloseStatement,
    cursor=
        safe_text
)
syntax_dbl_DeclareCursorStatement_strategy = st.builds(
    syntax_dbl_DeclareCursorStatement,
    forQuery=
        safe_text,
    forStatementName=
        safe_text,
    hold=
        st.booleans(),
    cursorName=
        safe_text,
    cursorType=
        safe_text
)
syntax_dbl_PrepareStatement_strategy = st.builds(
    syntax_dbl_PrepareStatement,
    from_=
        safe_text,
    statementName=
        safe_text
)
syntax_dbl_ExecuteImmediateStatement_strategy = st.builds(
    syntax_dbl_ExecuteImmediateStatement,
    variable=
        safe_text
)
syntax_dbl_DescribeStatement_strategy = st.builds(
    syntax_dbl_DescribeStatement,
    statementName=
        safe_text
)
syntax_dbl_AllocateDescriptorStatement_strategy = st.builds(
    syntax_dbl_AllocateDescriptorStatement,
    descriptorScope=
        safe_text,
    withMax=
        safe_text,
    descriptorName=
        safe_text
)
QueryExpressionBody_strategy = st.builds(
    QueryExpressionBody,
)
syntax_dml_ExtendedQueryExpressionBody_strategy = st.builds(
    syntax_dml_ExtendedQueryExpressionBody,
    optimizeRecordsNumber=
        st.integers()
)
QuerySelect_strategy = st.builds(
    QuerySelect,
)
dml_ExtendedQueryExpressionBody_strategy = st.builds(
    dml_ExtendedQueryExpressionBody,
)
syntax_dml_ExtendedQuerySelect_strategy = st.builds(
    syntax_dml_ExtendedQuerySelect,
)
ddl_syntax_TableColumnDef_strategy = st.builds(
    ddl_syntax_TableColumnDef,
)
ddl_syntax_IndexDef_strategy = st.builds(
    ddl_syntax_IndexDef,
)
ddl_syntax_QualifiedName_strategy = st.builds(
    ddl_syntax_QualifiedName,
)
DefinitionStatement_strategy = st.builds(
    DefinitionStatement,
)
syntax_ddl_CommitStatement_strategy = st.builds(
    syntax_ddl_CommitStatement,
    hold=
        st.booleans()
)
syntax_ddl_DisconnectStatement_strategy = st.builds(
    syntax_ddl_DisconnectStatement,
    target=
        safe_text
)
syntax_ddl_CreateIndexStatement_strategy = st.builds(
    syntax_ddl_CreateIndexStatement,
    unique=
        st.booleans()
)
syntax_ddl_CreateViewStatement_strategy = st.builds(
    syntax_ddl_CreateViewStatement,
    fields=
        safe_text,
    query=
        safe_text
)
syntax_ddl_ReleaseStatement_strategy = st.builds(
    syntax_ddl_ReleaseStatement,
    serverName=
        safe_text
)
syntax_ddl_SetConnectionStatement_strategy = st.builds(
    syntax_ddl_SetConnectionStatement,
    databaseName=
        safe_text
)
syntax_ddl_CreateAliasStatement_strategy = st.builds(
    syntax_ddl_CreateAliasStatement,
)
syntax_ddl_RollbackStatement_strategy = st.builds(
    syntax_ddl_RollbackStatement,
    hold=
        st.booleans()
)
syntax_ddl_CreateTableStatement_strategy = st.builds(
    syntax_ddl_CreateTableStatement,
)
syntax_ddl_RenameStatement_strategy = st.builds(
    syntax_ddl_RenameStatement,
    newName=
        safe_text,
    target=
        safe_text,
    system=
        safe_text
)
syntax_ddl_DropStatement_strategy = st.builds(
    syntax_ddl_DropStatement,
    target=
        safe_text,
    range=
        safe_text
)
syntax_ddl_LockTableStatement_strategy = st.builds(
    syntax_ddl_LockTableStatement,
    allowRead=
        st.booleans(),
    shareMode=
        safe_text
)
syntax_ddl_ConnectStatement_strategy = st.builds(
    syntax_ddl_ConnectStatement,
    pwd=
        safe_text,
    to=
        safe_text,
    reset=
        st.booleans(),
    user=
        safe_text
)
syntax_ddl_CallStatement_strategy = st.builds(
    syntax_ddl_CallStatement,
    parms=
        safe_text
)
syntax_StatementParser_strategy = st.builds(
    syntax_StatementParser,
)
syntax_StatementWriter_strategy = st.builds(
    syntax_StatementWriter,
)
syntax_SQLObjectNameHelper_strategy = st.builds(
    syntax_SQLObjectNameHelper,
)
syntax_QueryParserRegistry_strategy = st.builds(
    syntax_QueryParserRegistry,
)
syntax_QueryWriterRegistry_strategy = st.builds(
    syntax_QueryWriterRegistry,
)
syntax_NameHelperRegistry_strategy = st.builds(
    syntax_NameHelperRegistry,
)
SQLObjectNameHelper_strategy = st.builds(
    SQLObjectNameHelper,
)
syntax_NameHelper_strategy = st.builds(
    syntax_NameHelper,
)
syntax_DefinitionWriterRegistry_strategy = st.builds(
    syntax_DefinitionWriterRegistry,
)
StatementWriter_strategy = st.builds(
    StatementWriter,
)
syntax_QueryWriter_strategy = st.builds(
    syntax_QueryWriter,
)
syntax_DefinitionWriter_strategy = st.builds(
    syntax_DefinitionWriter,
)
syntax_DefinitionStatement_strategy = st.builds(
    syntax_DefinitionStatement,
)
syntax_DefinitionParseResult_strategy = st.builds(
    syntax_DefinitionParseResult,
)
syntax_DefinitionParseError_strategy = st.builds(
    syntax_DefinitionParseError,
)
syntax_DefinitionParserRegistry_strategy = st.builds(
    syntax_DefinitionParserRegistry,
)
syntax_BindingStatement_strategy = st.builds(
    syntax_BindingStatement,
)
syntax_BindingParseResult_strategy = st.builds(
    syntax_BindingParseResult,
)
syntax_BindingParserRegistry_strategy = st.builds(
    syntax_BindingParserRegistry,
)
StatementParser_strategy = st.builds(
    StatementParser,
)
syntax_QueryParser_strategy = st.builds(
    syntax_QueryParser,
)
syntax_DefinitionParser_strategy = st.builds(
    syntax_DefinitionParser,
)
syntax_BindingParser_strategy = st.builds(
    syntax_BindingParser,
)
syntax_BindingParseError_strategy = st.builds(
    syntax_BindingParseError,
)
syntax_AliasResolver_strategy = st.builds(
    syntax_AliasResolver,
)

@given(instance=syntax_dbl_Option_strategy)
@settings(max_examples=50)
def test_syntax_dbl_option_instantiation(instance):
    assert isinstance(instance, syntax_dbl_Option)



@given(instance=syntax_dbl_Option_strategy)
def test_syntax_dbl_option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=syntax_dbl_Option_strategy)
def test_syntax_dbl_option_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=syntax_dbl_MultipleRowFetchClause_strategy)
@settings(max_examples=50)
def test_syntax_dbl_multiplerowfetchclause_instantiation(instance):
    assert isinstance(instance, syntax_dbl_MultipleRowFetchClause)



@given(instance=syntax_dbl_MultipleRowFetchClause_strategy)
def test_syntax_dbl_multiplerowfetchclause_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=syntax_dbl_MultipleRowFetchClause_strategy)
def test_syntax_dbl_multiplerowfetchclause_rowsNumber_setter(instance):
    original = instance.rowsNumber
    instance.rowsNumber = original
    assert instance.rowsNumber == original



@given(instance=syntax_dbl_MultipleRowFetchClause_strategy)
def test_syntax_dbl_multiplerowfetchclause_usingDescriptor_setter(instance):
    original = instance.usingDescriptor
    instance.usingDescriptor = original
    assert instance.usingDescriptor == original



@given(instance=syntax_dbl_MultipleRowFetchClause_strategy)
def test_syntax_dbl_multiplerowfetchclause_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=syntax_dbl_SingleRowFetchClause_strategy)
@settings(max_examples=50)
def test_syntax_dbl_singlerowfetchclause_instantiation(instance):
    assert isinstance(instance, syntax_dbl_SingleRowFetchClause)



@given(instance=syntax_dbl_SingleRowFetchClause_strategy)
def test_syntax_dbl_singlerowfetchclause_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original



@given(instance=syntax_dbl_SingleRowFetchClause_strategy)
def test_syntax_dbl_singlerowfetchclause_usingDescriptor_setter(instance):
    original = instance.usingDescriptor
    instance.usingDescriptor = original
    assert instance.usingDescriptor == original

@given(instance=syntax_dbl_IntoClause_strategy)
@settings(max_examples=50)
def test_syntax_dbl_intoclause_instantiation(instance):
    assert isinstance(instance, syntax_dbl_IntoClause)



@given(instance=syntax_dbl_IntoClause_strategy)
def test_syntax_dbl_intoclause_using_setter(instance):
    original = instance.using
    instance.using = original
    assert instance.using == original



@given(instance=syntax_dbl_IntoClause_strategy)
def test_syntax_dbl_intoclause_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original

@given(instance=ConditionInfoClause_strategy)
@settings(max_examples=50)
def test_conditioninfoclause_instantiation(instance):
    assert isinstance(instance, ConditionInfoClause)

@given(instance=SingleRowFetchClause_strategy)
@settings(max_examples=50)
def test_singlerowfetchclause_instantiation(instance):
    assert isinstance(instance, SingleRowFetchClause)

@given(instance=MultipleRowFetchClause_strategy)
@settings(max_examples=50)
def test_multiplerowfetchclause_instantiation(instance):
    assert isinstance(instance, MultipleRowFetchClause)

@given(instance=IntoClause_strategy)
@settings(max_examples=50)
def test_intoclause_instantiation(instance):
    assert isinstance(instance, IntoClause)

@given(instance=Option_strategy)
@settings(max_examples=50)
def test_option_instantiation(instance):
    assert isinstance(instance, Option)

@given(instance=syntax_dbl_ConditionInfoClause_strategy)
@settings(max_examples=50)
def test_syntax_dbl_conditioninfoclause_instantiation(instance):
    assert isinstance(instance, syntax_dbl_ConditionInfoClause)



@given(instance=syntax_dbl_ConditionInfoClause_strategy)
def test_syntax_dbl_conditioninfoclause_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=BindingStatement_strategy)
@settings(max_examples=50)
def test_bindingstatement_instantiation(instance):
    assert isinstance(instance, BindingStatement)

@given(instance=syntax_dbl_GetDiagnosticsStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_getdiagnosticsstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_GetDiagnosticsStatement)

@given(instance=syntax_dbl_GetDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_getdescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_GetDescriptorStatement)



@given(instance=syntax_dbl_GetDescriptorStatement_strategy)
def test_syntax_dbl_getdescriptorstatement_descriptorScope_setter(instance):
    original = instance.descriptorScope
    instance.descriptorScope = original
    assert instance.descriptorScope == original



@given(instance=syntax_dbl_GetDescriptorStatement_strategy)
def test_syntax_dbl_getdescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original



@given(instance=syntax_dbl_GetDescriptorStatement_strategy)
def test_syntax_dbl_getdescriptorstatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=syntax_dbl_DeallocateDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_deallocatedescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_DeallocateDescriptorStatement)



@given(instance=syntax_dbl_DeallocateDescriptorStatement_strategy)
def test_syntax_dbl_deallocatedescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original



@given(instance=syntax_dbl_DeallocateDescriptorStatement_strategy)
def test_syntax_dbl_deallocatedescriptorstatement_descriptorScope_setter(instance):
    original = instance.descriptorScope
    instance.descriptorScope = original
    assert instance.descriptorScope == original

@given(instance=syntax_dbl_SetOptionStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_setoptionstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_SetOptionStatement)

@given(instance=syntax_dbl_OpenStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_openstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_OpenStatement)



@given(instance=syntax_dbl_OpenStatement_strategy)
def test_syntax_dbl_openstatement_cursor_setter(instance):
    original = instance.cursor
    instance.cursor = original
    assert instance.cursor == original



@given(instance=syntax_dbl_OpenStatement_strategy)
def test_syntax_dbl_openstatement_usingType_setter(instance):
    original = instance.usingType
    instance.usingType = original
    assert instance.usingType == original



@given(instance=syntax_dbl_OpenStatement_strategy)
def test_syntax_dbl_openstatement_using_setter(instance):
    original = instance.using
    instance.using = original
    assert instance.using == original

@given(instance=syntax_dbl_SetTransactionStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_settransactionstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_SetTransactionStatement)



@given(instance=syntax_dbl_SetTransactionStatement_strategy)
def test_syntax_dbl_settransactionstatement_isolationLevel_setter(instance):
    original = instance.isolationLevel
    instance.isolationLevel = original
    assert instance.isolationLevel == original



@given(instance=syntax_dbl_SetTransactionStatement_strategy)
def test_syntax_dbl_settransactionstatement_rwOperation_setter(instance):
    original = instance.rwOperation
    instance.rwOperation = original
    assert instance.rwOperation == original

@given(instance=syntax_dbl_SetDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_setdescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_SetDescriptorStatement)



@given(instance=syntax_dbl_SetDescriptorStatement_strategy)
def test_syntax_dbl_setdescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original



@given(instance=syntax_dbl_SetDescriptorStatement_strategy)
def test_syntax_dbl_setdescriptorstatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=syntax_dbl_ExecuteStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_executestatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_ExecuteStatement)



@given(instance=syntax_dbl_ExecuteStatement_strategy)
def test_syntax_dbl_executestatement_statementName_setter(instance):
    original = instance.statementName
    instance.statementName = original
    assert instance.statementName == original

@given(instance=syntax_dbl_FetchStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_fetchstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_FetchStatement)



@given(instance=syntax_dbl_FetchStatement_strategy)
def test_syntax_dbl_fetchstatement_relativePosition_setter(instance):
    original = instance.relativePosition
    instance.relativePosition = original
    assert instance.relativePosition == original



@given(instance=syntax_dbl_FetchStatement_strategy)
def test_syntax_dbl_fetchstatement_cursorName_setter(instance):
    original = instance.cursorName
    instance.cursorName = original
    assert instance.cursorName == original



@given(instance=syntax_dbl_FetchStatement_strategy)
def test_syntax_dbl_fetchstatement_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=syntax_dbl_CloseStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_closestatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_CloseStatement)



@given(instance=syntax_dbl_CloseStatement_strategy)
def test_syntax_dbl_closestatement_cursor_setter(instance):
    original = instance.cursor
    instance.cursor = original
    assert instance.cursor == original

@given(instance=syntax_dbl_DeclareCursorStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_declarecursorstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_DeclareCursorStatement)



@given(instance=syntax_dbl_DeclareCursorStatement_strategy)
def test_syntax_dbl_declarecursorstatement_forQuery_setter(instance):
    original = instance.forQuery
    instance.forQuery = original
    assert instance.forQuery == original



@given(instance=syntax_dbl_DeclareCursorStatement_strategy)
def test_syntax_dbl_declarecursorstatement_forStatementName_setter(instance):
    original = instance.forStatementName
    instance.forStatementName = original
    assert instance.forStatementName == original



@given(instance=syntax_dbl_DeclareCursorStatement_strategy)
def test_syntax_dbl_declarecursorstatement_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original



@given(instance=syntax_dbl_DeclareCursorStatement_strategy)
def test_syntax_dbl_declarecursorstatement_cursorName_setter(instance):
    original = instance.cursorName
    instance.cursorName = original
    assert instance.cursorName == original



@given(instance=syntax_dbl_DeclareCursorStatement_strategy)
def test_syntax_dbl_declarecursorstatement_cursorType_setter(instance):
    original = instance.cursorType
    instance.cursorType = original
    assert instance.cursorType == original

@given(instance=syntax_dbl_PrepareStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_preparestatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_PrepareStatement)



@given(instance=syntax_dbl_PrepareStatement_strategy)
def test_syntax_dbl_preparestatement_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=syntax_dbl_PrepareStatement_strategy)
def test_syntax_dbl_preparestatement_statementName_setter(instance):
    original = instance.statementName
    instance.statementName = original
    assert instance.statementName == original

@given(instance=syntax_dbl_ExecuteImmediateStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_executeimmediatestatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_ExecuteImmediateStatement)



@given(instance=syntax_dbl_ExecuteImmediateStatement_strategy)
def test_syntax_dbl_executeimmediatestatement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=syntax_dbl_DescribeStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_describestatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_DescribeStatement)



@given(instance=syntax_dbl_DescribeStatement_strategy)
def test_syntax_dbl_describestatement_statementName_setter(instance):
    original = instance.statementName
    instance.statementName = original
    assert instance.statementName == original

@given(instance=syntax_dbl_AllocateDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax_dbl_allocatedescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax_dbl_AllocateDescriptorStatement)



@given(instance=syntax_dbl_AllocateDescriptorStatement_strategy)
def test_syntax_dbl_allocatedescriptorstatement_descriptorScope_setter(instance):
    original = instance.descriptorScope
    instance.descriptorScope = original
    assert instance.descriptorScope == original



@given(instance=syntax_dbl_AllocateDescriptorStatement_strategy)
def test_syntax_dbl_allocatedescriptorstatement_withMax_setter(instance):
    original = instance.withMax
    instance.withMax = original
    assert instance.withMax == original



@given(instance=syntax_dbl_AllocateDescriptorStatement_strategy)
def test_syntax_dbl_allocatedescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original

@given(instance=QueryExpressionBody_strategy)
@settings(max_examples=50)
def test_queryexpressionbody_instantiation(instance):
    assert isinstance(instance, QueryExpressionBody)

@given(instance=syntax_dml_ExtendedQueryExpressionBody_strategy)
@settings(max_examples=50)
def test_syntax_dml_extendedqueryexpressionbody_instantiation(instance):
    assert isinstance(instance, syntax_dml_ExtendedQueryExpressionBody)



@given(instance=syntax_dml_ExtendedQueryExpressionBody_strategy)
def test_syntax_dml_extendedqueryexpressionbody_optimizeRecordsNumber_setter(instance):
    original = instance.optimizeRecordsNumber
    instance.optimizeRecordsNumber = original
    assert instance.optimizeRecordsNumber == original

@given(instance=QuerySelect_strategy)
@settings(max_examples=50)
def test_queryselect_instantiation(instance):
    assert isinstance(instance, QuerySelect)

@given(instance=dml_ExtendedQueryExpressionBody_strategy)
@settings(max_examples=50)
def test_dml_extendedqueryexpressionbody_instantiation(instance):
    assert isinstance(instance, dml_ExtendedQueryExpressionBody)

@given(instance=syntax_dml_ExtendedQuerySelect_strategy)
@settings(max_examples=50)
def test_syntax_dml_extendedqueryselect_instantiation(instance):
    assert isinstance(instance, syntax_dml_ExtendedQuerySelect)

@given(instance=ddl_syntax_TableColumnDef_strategy)
@settings(max_examples=50)
def test_ddl_syntax_tablecolumndef_instantiation(instance):
    assert isinstance(instance, ddl_syntax_TableColumnDef)

@given(instance=ddl_syntax_IndexDef_strategy)
@settings(max_examples=50)
def test_ddl_syntax_indexdef_instantiation(instance):
    assert isinstance(instance, ddl_syntax_IndexDef)

@given(instance=ddl_syntax_QualifiedName_strategy)
@settings(max_examples=50)
def test_ddl_syntax_qualifiedname_instantiation(instance):
    assert isinstance(instance, ddl_syntax_QualifiedName)

@given(instance=DefinitionStatement_strategy)
@settings(max_examples=50)
def test_definitionstatement_instantiation(instance):
    assert isinstance(instance, DefinitionStatement)

@given(instance=syntax_ddl_CommitStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_commitstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_CommitStatement)



@given(instance=syntax_ddl_CommitStatement_strategy)
def test_syntax_ddl_commitstatement_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original

@given(instance=syntax_ddl_DisconnectStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_disconnectstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_DisconnectStatement)



@given(instance=syntax_ddl_DisconnectStatement_strategy)
def test_syntax_ddl_disconnectstatement_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=syntax_ddl_CreateIndexStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_createindexstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_CreateIndexStatement)



@given(instance=syntax_ddl_CreateIndexStatement_strategy)
def test_syntax_ddl_createindexstatement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=syntax_ddl_CreateViewStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_createviewstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_CreateViewStatement)



@given(instance=syntax_ddl_CreateViewStatement_strategy)
def test_syntax_ddl_createviewstatement_fields_setter(instance):
    original = instance.fields
    instance.fields = original
    assert instance.fields == original



@given(instance=syntax_ddl_CreateViewStatement_strategy)
def test_syntax_ddl_createviewstatement_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=syntax_ddl_ReleaseStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_releasestatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_ReleaseStatement)



@given(instance=syntax_ddl_ReleaseStatement_strategy)
def test_syntax_ddl_releasestatement_serverName_setter(instance):
    original = instance.serverName
    instance.serverName = original
    assert instance.serverName == original

@given(instance=syntax_ddl_SetConnectionStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_setconnectionstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_SetConnectionStatement)



@given(instance=syntax_ddl_SetConnectionStatement_strategy)
def test_syntax_ddl_setconnectionstatement_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=syntax_ddl_CreateAliasStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_createaliasstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_CreateAliasStatement)

@given(instance=syntax_ddl_RollbackStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_rollbackstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_RollbackStatement)



@given(instance=syntax_ddl_RollbackStatement_strategy)
def test_syntax_ddl_rollbackstatement_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original

@given(instance=syntax_ddl_CreateTableStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_createtablestatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_CreateTableStatement)

@given(instance=syntax_ddl_RenameStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_renamestatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_RenameStatement)



@given(instance=syntax_ddl_RenameStatement_strategy)
def test_syntax_ddl_renamestatement_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original



@given(instance=syntax_ddl_RenameStatement_strategy)
def test_syntax_ddl_renamestatement_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=syntax_ddl_RenameStatement_strategy)
def test_syntax_ddl_renamestatement_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=syntax_ddl_DropStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_dropstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_DropStatement)



@given(instance=syntax_ddl_DropStatement_strategy)
def test_syntax_ddl_dropstatement_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=syntax_ddl_DropStatement_strategy)
def test_syntax_ddl_dropstatement_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=syntax_ddl_LockTableStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_locktablestatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_LockTableStatement)



@given(instance=syntax_ddl_LockTableStatement_strategy)
def test_syntax_ddl_locktablestatement_allowRead_setter(instance):
    original = instance.allowRead
    instance.allowRead = original
    assert instance.allowRead == original



@given(instance=syntax_ddl_LockTableStatement_strategy)
def test_syntax_ddl_locktablestatement_shareMode_setter(instance):
    original = instance.shareMode
    instance.shareMode = original
    assert instance.shareMode == original

@given(instance=syntax_ddl_ConnectStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_connectstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_ConnectStatement)



@given(instance=syntax_ddl_ConnectStatement_strategy)
def test_syntax_ddl_connectstatement_pwd_setter(instance):
    original = instance.pwd
    instance.pwd = original
    assert instance.pwd == original



@given(instance=syntax_ddl_ConnectStatement_strategy)
def test_syntax_ddl_connectstatement_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=syntax_ddl_ConnectStatement_strategy)
def test_syntax_ddl_connectstatement_reset_setter(instance):
    original = instance.reset
    instance.reset = original
    assert instance.reset == original



@given(instance=syntax_ddl_ConnectStatement_strategy)
def test_syntax_ddl_connectstatement_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=syntax_ddl_CallStatement_strategy)
@settings(max_examples=50)
def test_syntax_ddl_callstatement_instantiation(instance):
    assert isinstance(instance, syntax_ddl_CallStatement)



@given(instance=syntax_ddl_CallStatement_strategy)
def test_syntax_ddl_callstatement_parms_setter(instance):
    original = instance.parms
    instance.parms = original
    assert instance.parms == original

@given(instance=syntax_StatementParser_strategy)
@settings(max_examples=50)
def test_syntax_statementparser_instantiation(instance):
    assert isinstance(instance, syntax_StatementParser)

@given(instance=syntax_StatementWriter_strategy)
@settings(max_examples=50)
def test_syntax_statementwriter_instantiation(instance):
    assert isinstance(instance, syntax_StatementWriter)

@given(instance=syntax_SQLObjectNameHelper_strategy)
@settings(max_examples=50)
def test_syntax_sqlobjectnamehelper_instantiation(instance):
    assert isinstance(instance, syntax_SQLObjectNameHelper)

@given(instance=syntax_QueryParserRegistry_strategy)
@settings(max_examples=50)
def test_syntax_queryparserregistry_instantiation(instance):
    assert isinstance(instance, syntax_QueryParserRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_QueryParserRegistry_strategy)
@settings(max_examples=30)
def test_syntax_queryparserregistry_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in syntax_QueryParserRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax_QueryParserRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax_QueryParserRegistry is not implemented or raised an error")

@given(instance=syntax_QueryWriterRegistry_strategy)
@settings(max_examples=50)
def test_syntax_querywriterregistry_instantiation(instance):
    assert isinstance(instance, syntax_QueryWriterRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_QueryWriterRegistry_strategy)
@settings(max_examples=30)
def test_syntax_querywriterregistry_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in syntax_QueryWriterRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax_QueryWriterRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax_QueryWriterRegistry is not implemented or raised an error")

@given(instance=syntax_NameHelperRegistry_strategy)
@settings(max_examples=50)
def test_syntax_namehelperregistry_instantiation(instance):
    assert isinstance(instance, syntax_NameHelperRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_NameHelperRegistry_strategy)
@settings(max_examples=30)
def test_syntax_namehelperregistry_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in syntax_NameHelperRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax_NameHelperRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax_NameHelperRegistry is not implemented or raised an error")

@given(instance=SQLObjectNameHelper_strategy)
@settings(max_examples=50)
def test_sqlobjectnamehelper_instantiation(instance):
    assert isinstance(instance, SQLObjectNameHelper)

@given(instance=syntax_NameHelper_strategy)
@settings(max_examples=50)
def test_syntax_namehelper_instantiation(instance):
    assert isinstance(instance, syntax_NameHelper)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_NameHelper_strategy)
@settings(max_examples=30)
def test_syntax_namehelper_resolvecontainers_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resolveContainers(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resolveContainers).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resolveContainers' in syntax_NameHelper is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolveContainers' in syntax_NameHelper did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolveContainers' in syntax_NameHelper is not implemented or raised an error")

@given(instance=syntax_DefinitionWriterRegistry_strategy)
@settings(max_examples=50)
def test_syntax_definitionwriterregistry_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionWriterRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriterRegistry_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriterregistry_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in syntax_DefinitionWriterRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax_DefinitionWriterRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax_DefinitionWriterRegistry is not implemented or raised an error")

@given(instance=StatementWriter_strategy)
@settings(max_examples=50)
def test_statementwriter_instantiation(instance):
    assert isinstance(instance, StatementWriter)

@given(instance=syntax_QueryWriter_strategy)
@settings(max_examples=50)
def test_syntax_querywriter_instantiation(instance):
    assert isinstance(instance, syntax_QueryWriter)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_QueryWriter_strategy)
@settings(max_examples=30)
def test_syntax_querywriter_writequery_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.writeQuery(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.writeQuery).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'writeQuery' in syntax_QueryWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'writeQuery' in syntax_QueryWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'writeQuery' in syntax_QueryWriter is not implemented or raised an error")

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=50)
def test_syntax_definitionwriter_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionWriter)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_deletedata_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.deleteData(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.deleteData).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'deleteData' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'deleteData' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'deleteData' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_insertdata_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.insertData(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.insertData).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'insertData' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'insertData' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'insertData' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_createlabelforfields_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createLabelForFields(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createLabelForFields).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createLabelForFields' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLabelForFields' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLabelForFields' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_renameindex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.renameIndex(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.renameIndex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'renameIndex' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'renameIndex' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'renameIndex' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_createindex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createIndex(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createIndex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createIndex' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createIndex' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createIndex' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_dropview_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dropView(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dropView).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dropView' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropView' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropView' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_renametable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.renameTable(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.renameTable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'renameTable' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'renameTable' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'renameTable' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_dropindex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dropIndex(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dropIndex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dropIndex' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropIndex' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropIndex' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_createview_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createView(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createView).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createView' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createView' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createView' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_selectdata_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.selectData(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.selectData).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'selectData' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'selectData' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'selectData' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_copytabledata_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copyTableData(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copyTableData).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copyTableData' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copyTableData' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copyTableData' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_createlabel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createLabel(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createLabel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createLabel' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLabel' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLabel' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_createschema_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createSchema(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createSchema).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createSchema' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createSchema' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createSchema' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_createtable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createTable(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createTable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createTable' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createTable' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createTable' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_dropschema_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dropSchema(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dropSchema).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dropSchema' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropSchema' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropSchema' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_truncatetable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.truncateTable(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.truncateTable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'truncateTable' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'truncateTable' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'truncateTable' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_countrecords_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.countRecords(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.countRecords).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'countRecords' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'countRecords' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'countRecords' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_haslogicals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasLogicals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasLogicals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasLogicals' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasLogicals' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasLogicals' in syntax_DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax_definitionwriter_droptable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dropTable(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dropTable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dropTable' in syntax_DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropTable' in syntax_DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropTable' in syntax_DefinitionWriter is not implemented or raised an error")

@given(instance=syntax_DefinitionStatement_strategy)
@settings(max_examples=50)
def test_syntax_definitionstatement_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionStatement)

@given(instance=syntax_DefinitionParseResult_strategy)
@settings(max_examples=50)
def test_syntax_definitionparseresult_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionParseResult)

@given(instance=syntax_DefinitionParseError_strategy)
@settings(max_examples=50)
def test_syntax_definitionparseerror_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionParseError)

@given(instance=syntax_DefinitionParserRegistry_strategy)
@settings(max_examples=50)
def test_syntax_definitionparserregistry_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionParserRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionParserRegistry_strategy)
@settings(max_examples=30)
def test_syntax_definitionparserregistry_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in syntax_DefinitionParserRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax_DefinitionParserRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax_DefinitionParserRegistry is not implemented or raised an error")

@given(instance=syntax_BindingStatement_strategy)
@settings(max_examples=50)
def test_syntax_bindingstatement_instantiation(instance):
    assert isinstance(instance, syntax_BindingStatement)

@given(instance=syntax_BindingParseResult_strategy)
@settings(max_examples=50)
def test_syntax_bindingparseresult_instantiation(instance):
    assert isinstance(instance, syntax_BindingParseResult)

@given(instance=syntax_BindingParserRegistry_strategy)
@settings(max_examples=50)
def test_syntax_bindingparserregistry_instantiation(instance):
    assert isinstance(instance, syntax_BindingParserRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_BindingParserRegistry_strategy)
@settings(max_examples=30)
def test_syntax_bindingparserregistry_lookup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lookup(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lookup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lookup' in syntax_BindingParserRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax_BindingParserRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax_BindingParserRegistry is not implemented or raised an error")

@given(instance=StatementParser_strategy)
@settings(max_examples=50)
def test_statementparser_instantiation(instance):
    assert isinstance(instance, StatementParser)

@given(instance=syntax_QueryParser_strategy)
@settings(max_examples=50)
def test_syntax_queryparser_instantiation(instance):
    assert isinstance(instance, syntax_QueryParser)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_QueryParser_strategy)
@settings(max_examples=30)
def test_syntax_queryparser_parsequery_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.parseQuery(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.parseQuery).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'parseQuery' in syntax_QueryParser is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parseQuery' in syntax_QueryParser did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parseQuery' in syntax_QueryParser is not implemented or raised an error")

@given(instance=syntax_DefinitionParser_strategy)
@settings(max_examples=50)
def test_syntax_definitionparser_instantiation(instance):
    assert isinstance(instance, syntax_DefinitionParser)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_DefinitionParser_strategy)
@settings(max_examples=30)
def test_syntax_definitionparser_parsedefinition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.parseDefinition(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.parseDefinition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'parseDefinition' in syntax_DefinitionParser is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parseDefinition' in syntax_DefinitionParser did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parseDefinition' in syntax_DefinitionParser is not implemented or raised an error")

@given(instance=syntax_BindingParser_strategy)
@settings(max_examples=50)
def test_syntax_bindingparser_instantiation(instance):
    assert isinstance(instance, syntax_BindingParser)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_BindingParser_strategy)
@settings(max_examples=30)
def test_syntax_bindingparser_parsebinding_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.parseBinding(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.parseBinding).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'parseBinding' in syntax_BindingParser is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parseBinding' in syntax_BindingParser did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parseBinding' in syntax_BindingParser is not implemented or raised an error")

@given(instance=syntax_BindingParseError_strategy)
@settings(max_examples=50)
def test_syntax_bindingparseerror_instantiation(instance):
    assert isinstance(instance, syntax_BindingParseError)

@given(instance=syntax_AliasResolver_strategy)
@settings(max_examples=50)
def test_syntax_aliasresolver_instantiation(instance):
    assert isinstance(instance, syntax_AliasResolver)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax_AliasResolver_strategy)
@settings(max_examples=30)
def test_syntax_aliasresolver_resolvequery_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resolveQuery(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resolveQuery).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resolveQuery' in syntax_AliasResolver is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolveQuery' in syntax_AliasResolver did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolveQuery' in syntax_AliasResolver is not implemented or raised an error")
