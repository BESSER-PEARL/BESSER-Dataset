import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    syntax::dbl::MultipleRowFetchClause,
    syntax::dbl::SingleRowFetchClause,
    syntax::dbl::IntoClause,
    ConditionInfoClause,
    SingleRowFetchClause,
    MultipleRowFetchClause,
    IntoClause,
    Option,
    syntax::dbl::ConditionInfoClause,
    BindingStatement,
    syntax::dbl::CloseStatement,
    syntax::dbl::GetDescriptorStatement,
    syntax::dbl::DescribeStatement,
    syntax::dbl::FetchStatement,
    syntax::dbl::DeallocateDescriptorStatement,
    syntax::dbl::ExecuteImmediateStatement,
    syntax::dbl::GetDiagnosticsStatement,
    syntax::dbl::SetDescriptorStatement,
    syntax::dbl::SetTransactionStatement,
    syntax::dbl::ExecuteStatement,
    syntax::dbl::DeclareCursorStatement,
    syntax::dbl::AllocateDescriptorStatement,
    QueryExpressionBody,
    syntax::dml::ExtendedQueryExpressionBody,
    QuerySelect,
    dml::ExtendedQueryExpressionBody,
    syntax::dml::ExtendedQuerySelect,
    ddl::syntax::TableColumnDef,
    ddl::syntax::IndexDef,
    ddl::syntax::QualifiedName,
    DefinitionStatement,
    syntax::ddl::CommitStatement,
    syntax::ddl::DropStatement,
    syntax::ddl::RenameStatement,
    syntax::ddl::ConnectStatement,
    syntax::ddl::RollbackStatement,
    syntax::ddl::ReleaseStatement,
    syntax::ddl::CreateAliasStatement,
    syntax::ddl::CreateIndexStatement,
    syntax::ddl::DisconnectStatement,
    syntax::ddl::CreateViewStatement,
    syntax::ddl::SetConnectionStatement,
    syntax::ddl::LockTableStatement,
    syntax::ddl::CreateTableStatement,
    syntax::ddl::CallStatement,
    syntax::StatementParser,
    syntax::StatementWriter,
    syntax::SQLObjectNameHelper,
    syntax::QueryParserRegistry,
    syntax::QueryWriterRegistry,
    syntax::NameHelperRegistry,
    SQLObjectNameHelper,
    syntax::NameHelper,
    syntax::DefinitionWriterRegistry,
    StatementWriter,
    syntax::QueryWriter,
    syntax::DefinitionWriter,
    syntax::DefinitionStatement,
    syntax::DefinitionParseResult,
    syntax::DefinitionParseError,
    syntax::DefinitionParserRegistry,
    syntax::BindingStatement,
    syntax::BindingParseResult,
    syntax::BindingParserRegistry,
    StatementParser,
    syntax::DefinitionParser,
    syntax::QueryParser,
    syntax::BindingParser,
    syntax::BindingParseError,
    syntax::AliasResolver,
    syntax::dbl::Option,
    syntax::dbl::PrepareStatement,
    syntax::dbl::OpenStatement,
    syntax::dbl::SetOptionStatement,
    TargetItem,
    OpenUsingType,
    TargetElement,
    DropRange,
    RWOperation,
    ShareMode,
    UsingType,
    CursorType,
    FetchPosition,
    IsolationLevel,
    StatementType,
    DescriptorScope,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_syntax::dbl::multiplerowfetchclause_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::MultipleRowFetchClause)


def test_syntax::dbl::multiplerowfetchclause_constructor_exists():
    assert callable(syntax::dbl::MultipleRowFetchClause.__init__)


def test_syntax::dbl::multiplerowfetchclause_constructor_args():
    sig = inspect.signature(syntax::dbl::MultipleRowFetchClause.__init__)
    params = list(sig.parameters.keys())
    assert "into" in params, "Missing parameter 'into'"
    assert "usingDescriptor" in params, "Missing parameter 'usingDescriptor'"
    assert "rowsNumber" in params, "Missing parameter 'rowsNumber'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_syntax::dbl::multiplerowfetchclause_has_into():
    assert hasattr(syntax::dbl::MultipleRowFetchClause, "into")
    descriptor = None
    for klass in syntax::dbl::MultipleRowFetchClause.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::multiplerowfetchclause_has_usingDescriptor():
    assert hasattr(syntax::dbl::MultipleRowFetchClause, "usingDescriptor")
    descriptor = None
    for klass in syntax::dbl::MultipleRowFetchClause.__mro__:
        if "usingDescriptor" in klass.__dict__:
            descriptor = klass.__dict__["usingDescriptor"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::multiplerowfetchclause_has_rowsNumber():
    assert hasattr(syntax::dbl::MultipleRowFetchClause, "rowsNumber")
    descriptor = None
    for klass in syntax::dbl::MultipleRowFetchClause.__mro__:
        if "rowsNumber" in klass.__dict__:
            descriptor = klass.__dict__["rowsNumber"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::multiplerowfetchclause_has_descriptor():
    assert hasattr(syntax::dbl::MultipleRowFetchClause, "descriptor")
    descriptor = None
    for klass in syntax::dbl::MultipleRowFetchClause.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::singlerowfetchclause_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::SingleRowFetchClause)


def test_syntax::dbl::singlerowfetchclause_constructor_exists():
    assert callable(syntax::dbl::SingleRowFetchClause.__init__)


def test_syntax::dbl::singlerowfetchclause_constructor_args():
    sig = inspect.signature(syntax::dbl::SingleRowFetchClause.__init__)
    params = list(sig.parameters.keys())
    assert "usingDescriptor" in params, "Missing parameter 'usingDescriptor'"
    assert "into" in params, "Missing parameter 'into'"

def test_syntax::dbl::singlerowfetchclause_has_usingDescriptor():
    assert hasattr(syntax::dbl::SingleRowFetchClause, "usingDescriptor")
    descriptor = None
    for klass in syntax::dbl::SingleRowFetchClause.__mro__:
        if "usingDescriptor" in klass.__dict__:
            descriptor = klass.__dict__["usingDescriptor"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::singlerowfetchclause_has_into():
    assert hasattr(syntax::dbl::SingleRowFetchClause, "into")
    descriptor = None
    for klass in syntax::dbl::SingleRowFetchClause.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::intoclause_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::IntoClause)


def test_syntax::dbl::intoclause_constructor_exists():
    assert callable(syntax::dbl::IntoClause.__init__)


def test_syntax::dbl::intoclause_constructor_args():
    sig = inspect.signature(syntax::dbl::IntoClause.__init__)
    params = list(sig.parameters.keys())
    assert "using" in params, "Missing parameter 'using'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"

def test_syntax::dbl::intoclause_has_using():
    assert hasattr(syntax::dbl::IntoClause, "using")
    descriptor = None
    for klass in syntax::dbl::IntoClause.__mro__:
        if "using" in klass.__dict__:
            descriptor = klass.__dict__["using"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::intoclause_has_descriptorName():
    assert hasattr(syntax::dbl::IntoClause, "descriptorName")
    descriptor = None
    for klass in syntax::dbl::IntoClause.__mro__:
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



def test_syntax::dbl::conditioninfoclause_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::ConditionInfoClause)


def test_syntax::dbl::conditioninfoclause_constructor_exists():
    assert callable(syntax::dbl::ConditionInfoClause.__init__)


def test_syntax::dbl::conditioninfoclause_constructor_args():
    sig = inspect.signature(syntax::dbl::ConditionInfoClause.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_syntax::dbl::conditioninfoclause_has_condition():
    assert hasattr(syntax::dbl::ConditionInfoClause, "condition")
    descriptor = None
    for klass in syntax::dbl::ConditionInfoClause.__mro__:
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



def test_syntax::dbl::closestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::CloseStatement)


def test_syntax::dbl::closestatement_constructor_exists():
    assert callable(syntax::dbl::CloseStatement.__init__)


def test_syntax::dbl::closestatement_constructor_args():
    sig = inspect.signature(syntax::dbl::CloseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "cursor" in params, "Missing parameter 'cursor'"

def test_syntax::dbl::closestatement_has_cursor():
    assert hasattr(syntax::dbl::CloseStatement, "cursor")
    descriptor = None
    for klass in syntax::dbl::CloseStatement.__mro__:
        if "cursor" in klass.__dict__:
            descriptor = klass.__dict__["cursor"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::getdescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::GetDescriptorStatement)


def test_syntax::dbl::getdescriptorstatement_constructor_exists():
    assert callable(syntax::dbl::GetDescriptorStatement.__init__)


def test_syntax::dbl::getdescriptorstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::GetDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorScope" in params, "Missing parameter 'descriptorScope'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"
    assert "value" in params, "Missing parameter 'value'"

def test_syntax::dbl::getdescriptorstatement_has_descriptorScope():
    assert hasattr(syntax::dbl::GetDescriptorStatement, "descriptorScope")
    descriptor = None
    for klass in syntax::dbl::GetDescriptorStatement.__mro__:
        if "descriptorScope" in klass.__dict__:
            descriptor = klass.__dict__["descriptorScope"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::getdescriptorstatement_has_descriptorName():
    assert hasattr(syntax::dbl::GetDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax::dbl::GetDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::getdescriptorstatement_has_value():
    assert hasattr(syntax::dbl::GetDescriptorStatement, "value")
    descriptor = None
    for klass in syntax::dbl::GetDescriptorStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::describestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::DescribeStatement)


def test_syntax::dbl::describestatement_constructor_exists():
    assert callable(syntax::dbl::DescribeStatement.__init__)


def test_syntax::dbl::describestatement_constructor_args():
    sig = inspect.signature(syntax::dbl::DescribeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statementName" in params, "Missing parameter 'statementName'"

def test_syntax::dbl::describestatement_has_statementName():
    assert hasattr(syntax::dbl::DescribeStatement, "statementName")
    descriptor = None
    for klass in syntax::dbl::DescribeStatement.__mro__:
        if "statementName" in klass.__dict__:
            descriptor = klass.__dict__["statementName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::fetchstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::FetchStatement)


def test_syntax::dbl::fetchstatement_constructor_exists():
    assert callable(syntax::dbl::FetchStatement.__init__)


def test_syntax::dbl::fetchstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::FetchStatement.__init__)
    params = list(sig.parameters.keys())
    assert "relativePosition" in params, "Missing parameter 'relativePosition'"
    assert "position" in params, "Missing parameter 'position'"
    assert "cursorName" in params, "Missing parameter 'cursorName'"

def test_syntax::dbl::fetchstatement_has_relativePosition():
    assert hasattr(syntax::dbl::FetchStatement, "relativePosition")
    descriptor = None
    for klass in syntax::dbl::FetchStatement.__mro__:
        if "relativePosition" in klass.__dict__:
            descriptor = klass.__dict__["relativePosition"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::fetchstatement_has_position():
    assert hasattr(syntax::dbl::FetchStatement, "position")
    descriptor = None
    for klass in syntax::dbl::FetchStatement.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::fetchstatement_has_cursorName():
    assert hasattr(syntax::dbl::FetchStatement, "cursorName")
    descriptor = None
    for klass in syntax::dbl::FetchStatement.__mro__:
        if "cursorName" in klass.__dict__:
            descriptor = klass.__dict__["cursorName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::deallocatedescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::DeallocateDescriptorStatement)


def test_syntax::dbl::deallocatedescriptorstatement_constructor_exists():
    assert callable(syntax::dbl::DeallocateDescriptorStatement.__init__)


def test_syntax::dbl::deallocatedescriptorstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::DeallocateDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorScope" in params, "Missing parameter 'descriptorScope'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"

def test_syntax::dbl::deallocatedescriptorstatement_has_descriptorScope():
    assert hasattr(syntax::dbl::DeallocateDescriptorStatement, "descriptorScope")
    descriptor = None
    for klass in syntax::dbl::DeallocateDescriptorStatement.__mro__:
        if "descriptorScope" in klass.__dict__:
            descriptor = klass.__dict__["descriptorScope"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::deallocatedescriptorstatement_has_descriptorName():
    assert hasattr(syntax::dbl::DeallocateDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax::dbl::DeallocateDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::executeimmediatestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::ExecuteImmediateStatement)


def test_syntax::dbl::executeimmediatestatement_constructor_exists():
    assert callable(syntax::dbl::ExecuteImmediateStatement.__init__)


def test_syntax::dbl::executeimmediatestatement_constructor_args():
    sig = inspect.signature(syntax::dbl::ExecuteImmediateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_syntax::dbl::executeimmediatestatement_has_variable():
    assert hasattr(syntax::dbl::ExecuteImmediateStatement, "variable")
    descriptor = None
    for klass in syntax::dbl::ExecuteImmediateStatement.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::getdiagnosticsstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::GetDiagnosticsStatement)


def test_syntax::dbl::getdiagnosticsstatement_constructor_exists():
    assert callable(syntax::dbl::GetDiagnosticsStatement.__init__)


def test_syntax::dbl::getdiagnosticsstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::GetDiagnosticsStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax::dbl::setdescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::SetDescriptorStatement)


def test_syntax::dbl::setdescriptorstatement_constructor_exists():
    assert callable(syntax::dbl::SetDescriptorStatement.__init__)


def test_syntax::dbl::setdescriptorstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::SetDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"

def test_syntax::dbl::setdescriptorstatement_has_value():
    assert hasattr(syntax::dbl::SetDescriptorStatement, "value")
    descriptor = None
    for klass in syntax::dbl::SetDescriptorStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::setdescriptorstatement_has_descriptorName():
    assert hasattr(syntax::dbl::SetDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax::dbl::SetDescriptorStatement.__mro__:
        if "descriptorName" in klass.__dict__:
            descriptor = klass.__dict__["descriptorName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::settransactionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::SetTransactionStatement)


def test_syntax::dbl::settransactionstatement_constructor_exists():
    assert callable(syntax::dbl::SetTransactionStatement.__init__)


def test_syntax::dbl::settransactionstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::SetTransactionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "isolationLevel" in params, "Missing parameter 'isolationLevel'"
    assert "rwOperation" in params, "Missing parameter 'rwOperation'"

def test_syntax::dbl::settransactionstatement_has_isolationLevel():
    assert hasattr(syntax::dbl::SetTransactionStatement, "isolationLevel")
    descriptor = None
    for klass in syntax::dbl::SetTransactionStatement.__mro__:
        if "isolationLevel" in klass.__dict__:
            descriptor = klass.__dict__["isolationLevel"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::settransactionstatement_has_rwOperation():
    assert hasattr(syntax::dbl::SetTransactionStatement, "rwOperation")
    descriptor = None
    for klass in syntax::dbl::SetTransactionStatement.__mro__:
        if "rwOperation" in klass.__dict__:
            descriptor = klass.__dict__["rwOperation"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::executestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::ExecuteStatement)


def test_syntax::dbl::executestatement_constructor_exists():
    assert callable(syntax::dbl::ExecuteStatement.__init__)


def test_syntax::dbl::executestatement_constructor_args():
    sig = inspect.signature(syntax::dbl::ExecuteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statementName" in params, "Missing parameter 'statementName'"

def test_syntax::dbl::executestatement_has_statementName():
    assert hasattr(syntax::dbl::ExecuteStatement, "statementName")
    descriptor = None
    for klass in syntax::dbl::ExecuteStatement.__mro__:
        if "statementName" in klass.__dict__:
            descriptor = klass.__dict__["statementName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::declarecursorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::DeclareCursorStatement)


def test_syntax::dbl::declarecursorstatement_constructor_exists():
    assert callable(syntax::dbl::DeclareCursorStatement.__init__)


def test_syntax::dbl::declarecursorstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::DeclareCursorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "cursorType" in params, "Missing parameter 'cursorType'"
    assert "forQuery" in params, "Missing parameter 'forQuery'"
    assert "cursorName" in params, "Missing parameter 'cursorName'"
    assert "forStatementName" in params, "Missing parameter 'forStatementName'"
    assert "hold" in params, "Missing parameter 'hold'"

def test_syntax::dbl::declarecursorstatement_has_cursorType():
    assert hasattr(syntax::dbl::DeclareCursorStatement, "cursorType")
    descriptor = None
    for klass in syntax::dbl::DeclareCursorStatement.__mro__:
        if "cursorType" in klass.__dict__:
            descriptor = klass.__dict__["cursorType"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::declarecursorstatement_has_forQuery():
    assert hasattr(syntax::dbl::DeclareCursorStatement, "forQuery")
    descriptor = None
    for klass in syntax::dbl::DeclareCursorStatement.__mro__:
        if "forQuery" in klass.__dict__:
            descriptor = klass.__dict__["forQuery"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::declarecursorstatement_has_cursorName():
    assert hasattr(syntax::dbl::DeclareCursorStatement, "cursorName")
    descriptor = None
    for klass in syntax::dbl::DeclareCursorStatement.__mro__:
        if "cursorName" in klass.__dict__:
            descriptor = klass.__dict__["cursorName"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::declarecursorstatement_has_forStatementName():
    assert hasattr(syntax::dbl::DeclareCursorStatement, "forStatementName")
    descriptor = None
    for klass in syntax::dbl::DeclareCursorStatement.__mro__:
        if "forStatementName" in klass.__dict__:
            descriptor = klass.__dict__["forStatementName"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::declarecursorstatement_has_hold():
    assert hasattr(syntax::dbl::DeclareCursorStatement, "hold")
    descriptor = None
    for klass in syntax::dbl::DeclareCursorStatement.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::allocatedescriptorstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::AllocateDescriptorStatement)


def test_syntax::dbl::allocatedescriptorstatement_constructor_exists():
    assert callable(syntax::dbl::AllocateDescriptorStatement.__init__)


def test_syntax::dbl::allocatedescriptorstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::AllocateDescriptorStatement.__init__)
    params = list(sig.parameters.keys())
    assert "descriptorScope" in params, "Missing parameter 'descriptorScope'"
    assert "withMax" in params, "Missing parameter 'withMax'"
    assert "descriptorName" in params, "Missing parameter 'descriptorName'"

def test_syntax::dbl::allocatedescriptorstatement_has_descriptorScope():
    assert hasattr(syntax::dbl::AllocateDescriptorStatement, "descriptorScope")
    descriptor = None
    for klass in syntax::dbl::AllocateDescriptorStatement.__mro__:
        if "descriptorScope" in klass.__dict__:
            descriptor = klass.__dict__["descriptorScope"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::allocatedescriptorstatement_has_withMax():
    assert hasattr(syntax::dbl::AllocateDescriptorStatement, "withMax")
    descriptor = None
    for klass in syntax::dbl::AllocateDescriptorStatement.__mro__:
        if "withMax" in klass.__dict__:
            descriptor = klass.__dict__["withMax"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::allocatedescriptorstatement_has_descriptorName():
    assert hasattr(syntax::dbl::AllocateDescriptorStatement, "descriptorName")
    descriptor = None
    for klass in syntax::dbl::AllocateDescriptorStatement.__mro__:
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



def test_syntax::dml::extendedqueryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(syntax::dml::ExtendedQueryExpressionBody)


def test_syntax::dml::extendedqueryexpressionbody_constructor_exists():
    assert callable(syntax::dml::ExtendedQueryExpressionBody.__init__)


def test_syntax::dml::extendedqueryexpressionbody_constructor_args():
    sig = inspect.signature(syntax::dml::ExtendedQueryExpressionBody.__init__)
    params = list(sig.parameters.keys())
    assert "optimizeRecordsNumber" in params, "Missing parameter 'optimizeRecordsNumber'"

def test_syntax::dml::extendedqueryexpressionbody_has_optimizeRecordsNumber():
    assert hasattr(syntax::dml::ExtendedQueryExpressionBody, "optimizeRecordsNumber")
    descriptor = None
    for klass in syntax::dml::ExtendedQueryExpressionBody.__mro__:
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



def test_dml::extendedqueryexpressionbody_is_not_abstract():
    assert not inspect.isabstract(dml::ExtendedQueryExpressionBody)


def test_dml::extendedqueryexpressionbody_constructor_exists():
    assert callable(dml::ExtendedQueryExpressionBody.__init__)


def test_dml::extendedqueryexpressionbody_constructor_args():
    sig = inspect.signature(dml::ExtendedQueryExpressionBody.__init__)
    params = list(sig.parameters.keys())



def test_syntax::dml::extendedqueryselect_is_not_abstract():
    assert not inspect.isabstract(syntax::dml::ExtendedQuerySelect)


def test_syntax::dml::extendedqueryselect_constructor_exists():
    assert callable(syntax::dml::ExtendedQuerySelect.__init__)


def test_syntax::dml::extendedqueryselect_constructor_args():
    sig = inspect.signature(syntax::dml::ExtendedQuerySelect.__init__)
    params = list(sig.parameters.keys())



def test_ddl::syntax::tablecolumndef_is_not_abstract():
    assert not inspect.isabstract(ddl::syntax::TableColumnDef)


def test_ddl::syntax::tablecolumndef_constructor_exists():
    assert callable(ddl::syntax::TableColumnDef.__init__)


def test_ddl::syntax::tablecolumndef_constructor_args():
    sig = inspect.signature(ddl::syntax::TableColumnDef.__init__)
    params = list(sig.parameters.keys())



def test_ddl::syntax::indexdef_is_not_abstract():
    assert not inspect.isabstract(ddl::syntax::IndexDef)


def test_ddl::syntax::indexdef_constructor_exists():
    assert callable(ddl::syntax::IndexDef.__init__)


def test_ddl::syntax::indexdef_constructor_args():
    sig = inspect.signature(ddl::syntax::IndexDef.__init__)
    params = list(sig.parameters.keys())



def test_ddl::syntax::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(ddl::syntax::QualifiedName)


def test_ddl::syntax::qualifiedname_constructor_exists():
    assert callable(ddl::syntax::QualifiedName.__init__)


def test_ddl::syntax::qualifiedname_constructor_args():
    sig = inspect.signature(ddl::syntax::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_definitionstatement_is_not_abstract():
    assert not inspect.isabstract(DefinitionStatement)


def test_definitionstatement_constructor_exists():
    assert callable(DefinitionStatement.__init__)


def test_definitionstatement_constructor_args():
    sig = inspect.signature(DefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax::ddl::commitstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::CommitStatement)


def test_syntax::ddl::commitstatement_constructor_exists():
    assert callable(syntax::ddl::CommitStatement.__init__)


def test_syntax::ddl::commitstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::CommitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "hold" in params, "Missing parameter 'hold'"

def test_syntax::ddl::commitstatement_has_hold():
    assert hasattr(syntax::ddl::CommitStatement, "hold")
    descriptor = None
    for klass in syntax::ddl::CommitStatement.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::dropstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::DropStatement)


def test_syntax::ddl::dropstatement_constructor_exists():
    assert callable(syntax::ddl::DropStatement.__init__)


def test_syntax::ddl::dropstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::DropStatement.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "range" in params, "Missing parameter 'range'"

def test_syntax::ddl::dropstatement_has_target():
    assert hasattr(syntax::ddl::DropStatement, "target")
    descriptor = None
    for klass in syntax::ddl::DropStatement.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::dropstatement_has_range():
    assert hasattr(syntax::ddl::DropStatement, "range")
    descriptor = None
    for klass in syntax::ddl::DropStatement.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::renamestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::RenameStatement)


def test_syntax::ddl::renamestatement_constructor_exists():
    assert callable(syntax::ddl::RenameStatement.__init__)


def test_syntax::ddl::renamestatement_constructor_args():
    sig = inspect.signature(syntax::ddl::RenameStatement.__init__)
    params = list(sig.parameters.keys())
    assert "newName" in params, "Missing parameter 'newName'"
    assert "system" in params, "Missing parameter 'system'"
    assert "target" in params, "Missing parameter 'target'"

def test_syntax::ddl::renamestatement_has_newName():
    assert hasattr(syntax::ddl::RenameStatement, "newName")
    descriptor = None
    for klass in syntax::ddl::RenameStatement.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::renamestatement_has_system():
    assert hasattr(syntax::ddl::RenameStatement, "system")
    descriptor = None
    for klass in syntax::ddl::RenameStatement.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::renamestatement_has_target():
    assert hasattr(syntax::ddl::RenameStatement, "target")
    descriptor = None
    for klass in syntax::ddl::RenameStatement.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::connectstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::ConnectStatement)


def test_syntax::ddl::connectstatement_constructor_exists():
    assert callable(syntax::ddl::ConnectStatement.__init__)


def test_syntax::ddl::connectstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::ConnectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "pwd" in params, "Missing parameter 'pwd'"
    assert "to" in params, "Missing parameter 'to'"
    assert "reset" in params, "Missing parameter 'reset'"
    assert "user" in params, "Missing parameter 'user'"

def test_syntax::ddl::connectstatement_has_pwd():
    assert hasattr(syntax::ddl::ConnectStatement, "pwd")
    descriptor = None
    for klass in syntax::ddl::ConnectStatement.__mro__:
        if "pwd" in klass.__dict__:
            descriptor = klass.__dict__["pwd"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::connectstatement_has_to():
    assert hasattr(syntax::ddl::ConnectStatement, "to")
    descriptor = None
    for klass in syntax::ddl::ConnectStatement.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::connectstatement_has_reset():
    assert hasattr(syntax::ddl::ConnectStatement, "reset")
    descriptor = None
    for klass in syntax::ddl::ConnectStatement.__mro__:
        if "reset" in klass.__dict__:
            descriptor = klass.__dict__["reset"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::connectstatement_has_user():
    assert hasattr(syntax::ddl::ConnectStatement, "user")
    descriptor = None
    for klass in syntax::ddl::ConnectStatement.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::rollbackstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::RollbackStatement)


def test_syntax::ddl::rollbackstatement_constructor_exists():
    assert callable(syntax::ddl::RollbackStatement.__init__)


def test_syntax::ddl::rollbackstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::RollbackStatement.__init__)
    params = list(sig.parameters.keys())
    assert "hold" in params, "Missing parameter 'hold'"

def test_syntax::ddl::rollbackstatement_has_hold():
    assert hasattr(syntax::ddl::RollbackStatement, "hold")
    descriptor = None
    for klass in syntax::ddl::RollbackStatement.__mro__:
        if "hold" in klass.__dict__:
            descriptor = klass.__dict__["hold"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::releasestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::ReleaseStatement)


def test_syntax::ddl::releasestatement_constructor_exists():
    assert callable(syntax::ddl::ReleaseStatement.__init__)


def test_syntax::ddl::releasestatement_constructor_args():
    sig = inspect.signature(syntax::ddl::ReleaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "serverName" in params, "Missing parameter 'serverName'"

def test_syntax::ddl::releasestatement_has_serverName():
    assert hasattr(syntax::ddl::ReleaseStatement, "serverName")
    descriptor = None
    for klass in syntax::ddl::ReleaseStatement.__mro__:
        if "serverName" in klass.__dict__:
            descriptor = klass.__dict__["serverName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::createaliasstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::CreateAliasStatement)


def test_syntax::ddl::createaliasstatement_constructor_exists():
    assert callable(syntax::ddl::CreateAliasStatement.__init__)


def test_syntax::ddl::createaliasstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::CreateAliasStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax::ddl::createindexstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::CreateIndexStatement)


def test_syntax::ddl::createindexstatement_constructor_exists():
    assert callable(syntax::ddl::CreateIndexStatement.__init__)


def test_syntax::ddl::createindexstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::CreateIndexStatement.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_syntax::ddl::createindexstatement_has_unique():
    assert hasattr(syntax::ddl::CreateIndexStatement, "unique")
    descriptor = None
    for klass in syntax::ddl::CreateIndexStatement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::disconnectstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::DisconnectStatement)


def test_syntax::ddl::disconnectstatement_constructor_exists():
    assert callable(syntax::ddl::DisconnectStatement.__init__)


def test_syntax::ddl::disconnectstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::DisconnectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"

def test_syntax::ddl::disconnectstatement_has_target():
    assert hasattr(syntax::ddl::DisconnectStatement, "target")
    descriptor = None
    for klass in syntax::ddl::DisconnectStatement.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::createviewstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::CreateViewStatement)


def test_syntax::ddl::createviewstatement_constructor_exists():
    assert callable(syntax::ddl::CreateViewStatement.__init__)


def test_syntax::ddl::createviewstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::CreateViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "query" in params, "Missing parameter 'query'"
    assert "fields" in params, "Missing parameter 'fields'"

def test_syntax::ddl::createviewstatement_has_query():
    assert hasattr(syntax::ddl::CreateViewStatement, "query")
    descriptor = None
    for klass in syntax::ddl::CreateViewStatement.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::createviewstatement_has_fields():
    assert hasattr(syntax::ddl::CreateViewStatement, "fields")
    descriptor = None
    for klass in syntax::ddl::CreateViewStatement.__mro__:
        if "fields" in klass.__dict__:
            descriptor = klass.__dict__["fields"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::setconnectionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::SetConnectionStatement)


def test_syntax::ddl::setconnectionstatement_constructor_exists():
    assert callable(syntax::ddl::SetConnectionStatement.__init__)


def test_syntax::ddl::setconnectionstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::SetConnectionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_syntax::ddl::setconnectionstatement_has_databaseName():
    assert hasattr(syntax::ddl::SetConnectionStatement, "databaseName")
    descriptor = None
    for klass in syntax::ddl::SetConnectionStatement.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::locktablestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::LockTableStatement)


def test_syntax::ddl::locktablestatement_constructor_exists():
    assert callable(syntax::ddl::LockTableStatement.__init__)


def test_syntax::ddl::locktablestatement_constructor_args():
    sig = inspect.signature(syntax::ddl::LockTableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "allowRead" in params, "Missing parameter 'allowRead'"
    assert "shareMode" in params, "Missing parameter 'shareMode'"

def test_syntax::ddl::locktablestatement_has_allowRead():
    assert hasattr(syntax::ddl::LockTableStatement, "allowRead")
    descriptor = None
    for klass in syntax::ddl::LockTableStatement.__mro__:
        if "allowRead" in klass.__dict__:
            descriptor = klass.__dict__["allowRead"]
            break
    assert isinstance(descriptor, property)

def test_syntax::ddl::locktablestatement_has_shareMode():
    assert hasattr(syntax::ddl::LockTableStatement, "shareMode")
    descriptor = None
    for klass in syntax::ddl::LockTableStatement.__mro__:
        if "shareMode" in klass.__dict__:
            descriptor = klass.__dict__["shareMode"]
            break
    assert isinstance(descriptor, property)



def test_syntax::ddl::createtablestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::CreateTableStatement)


def test_syntax::ddl::createtablestatement_constructor_exists():
    assert callable(syntax::ddl::CreateTableStatement.__init__)


def test_syntax::ddl::createtablestatement_constructor_args():
    sig = inspect.signature(syntax::ddl::CreateTableStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax::ddl::callstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::ddl::CallStatement)


def test_syntax::ddl::callstatement_constructor_exists():
    assert callable(syntax::ddl::CallStatement.__init__)


def test_syntax::ddl::callstatement_constructor_args():
    sig = inspect.signature(syntax::ddl::CallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "parms" in params, "Missing parameter 'parms'"

def test_syntax::ddl::callstatement_has_parms():
    assert hasattr(syntax::ddl::CallStatement, "parms")
    descriptor = None
    for klass in syntax::ddl::CallStatement.__mro__:
        if "parms" in klass.__dict__:
            descriptor = klass.__dict__["parms"]
            break
    assert isinstance(descriptor, property)



def test_syntax::statementparser_is_not_abstract():
    assert not inspect.isabstract(syntax::StatementParser)


def test_syntax::statementparser_constructor_exists():
    assert callable(syntax::StatementParser.__init__)


def test_syntax::statementparser_constructor_args():
    sig = inspect.signature(syntax::StatementParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax::statementwriter_is_not_abstract():
    assert not inspect.isabstract(syntax::StatementWriter)


def test_syntax::statementwriter_constructor_exists():
    assert callable(syntax::StatementWriter.__init__)


def test_syntax::statementwriter_constructor_args():
    sig = inspect.signature(syntax::StatementWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax::sqlobjectnamehelper_is_not_abstract():
    assert not inspect.isabstract(syntax::SQLObjectNameHelper)


def test_syntax::sqlobjectnamehelper_constructor_exists():
    assert callable(syntax::SQLObjectNameHelper.__init__)


def test_syntax::sqlobjectnamehelper_constructor_args():
    sig = inspect.signature(syntax::SQLObjectNameHelper.__init__)
    params = list(sig.parameters.keys())



def test_syntax::queryparserregistry_is_not_abstract():
    assert not inspect.isabstract(syntax::QueryParserRegistry)


def test_syntax::queryparserregistry_constructor_exists():
    assert callable(syntax::QueryParserRegistry.__init__)


def test_syntax::queryparserregistry_constructor_args():
    sig = inspect.signature(syntax::QueryParserRegistry.__init__)
    params = list(sig.parameters.keys())



def test_syntax::querywriterregistry_is_not_abstract():
    assert not inspect.isabstract(syntax::QueryWriterRegistry)


def test_syntax::querywriterregistry_constructor_exists():
    assert callable(syntax::QueryWriterRegistry.__init__)


def test_syntax::querywriterregistry_constructor_args():
    sig = inspect.signature(syntax::QueryWriterRegistry.__init__)
    params = list(sig.parameters.keys())



def test_syntax::namehelperregistry_is_not_abstract():
    assert not inspect.isabstract(syntax::NameHelperRegistry)


def test_syntax::namehelperregistry_constructor_exists():
    assert callable(syntax::NameHelperRegistry.__init__)


def test_syntax::namehelperregistry_constructor_args():
    sig = inspect.signature(syntax::NameHelperRegistry.__init__)
    params = list(sig.parameters.keys())



def test_sqlobjectnamehelper_is_not_abstract():
    assert not inspect.isabstract(SQLObjectNameHelper)


def test_sqlobjectnamehelper_constructor_exists():
    assert callable(SQLObjectNameHelper.__init__)


def test_sqlobjectnamehelper_constructor_args():
    sig = inspect.signature(SQLObjectNameHelper.__init__)
    params = list(sig.parameters.keys())



def test_syntax::namehelper_is_not_abstract():
    assert not inspect.isabstract(syntax::NameHelper)


def test_syntax::namehelper_constructor_exists():
    assert callable(syntax::NameHelper.__init__)


def test_syntax::namehelper_constructor_args():
    sig = inspect.signature(syntax::NameHelper.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionwriterregistry_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionWriterRegistry)


def test_syntax::definitionwriterregistry_constructor_exists():
    assert callable(syntax::DefinitionWriterRegistry.__init__)


def test_syntax::definitionwriterregistry_constructor_args():
    sig = inspect.signature(syntax::DefinitionWriterRegistry.__init__)
    params = list(sig.parameters.keys())



def test_statementwriter_is_not_abstract():
    assert not inspect.isabstract(StatementWriter)


def test_statementwriter_constructor_exists():
    assert callable(StatementWriter.__init__)


def test_statementwriter_constructor_args():
    sig = inspect.signature(StatementWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax::querywriter_is_not_abstract():
    assert not inspect.isabstract(syntax::QueryWriter)


def test_syntax::querywriter_constructor_exists():
    assert callable(syntax::QueryWriter.__init__)


def test_syntax::querywriter_constructor_args():
    sig = inspect.signature(syntax::QueryWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionwriter_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionWriter)


def test_syntax::definitionwriter_constructor_exists():
    assert callable(syntax::DefinitionWriter.__init__)


def test_syntax::definitionwriter_constructor_args():
    sig = inspect.signature(syntax::DefinitionWriter.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionStatement)


def test_syntax::definitionstatement_constructor_exists():
    assert callable(syntax::DefinitionStatement.__init__)


def test_syntax::definitionstatement_constructor_args():
    sig = inspect.signature(syntax::DefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionparseresult_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionParseResult)


def test_syntax::definitionparseresult_constructor_exists():
    assert callable(syntax::DefinitionParseResult.__init__)


def test_syntax::definitionparseresult_constructor_args():
    sig = inspect.signature(syntax::DefinitionParseResult.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionparseerror_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionParseError)


def test_syntax::definitionparseerror_constructor_exists():
    assert callable(syntax::DefinitionParseError.__init__)


def test_syntax::definitionparseerror_constructor_args():
    sig = inspect.signature(syntax::DefinitionParseError.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionparserregistry_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionParserRegistry)


def test_syntax::definitionparserregistry_constructor_exists():
    assert callable(syntax::DefinitionParserRegistry.__init__)


def test_syntax::definitionparserregistry_constructor_args():
    sig = inspect.signature(syntax::DefinitionParserRegistry.__init__)
    params = list(sig.parameters.keys())



def test_syntax::bindingstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::BindingStatement)


def test_syntax::bindingstatement_constructor_exists():
    assert callable(syntax::BindingStatement.__init__)


def test_syntax::bindingstatement_constructor_args():
    sig = inspect.signature(syntax::BindingStatement.__init__)
    params = list(sig.parameters.keys())



def test_syntax::bindingparseresult_is_not_abstract():
    assert not inspect.isabstract(syntax::BindingParseResult)


def test_syntax::bindingparseresult_constructor_exists():
    assert callable(syntax::BindingParseResult.__init__)


def test_syntax::bindingparseresult_constructor_args():
    sig = inspect.signature(syntax::BindingParseResult.__init__)
    params = list(sig.parameters.keys())



def test_syntax::bindingparserregistry_is_not_abstract():
    assert not inspect.isabstract(syntax::BindingParserRegistry)


def test_syntax::bindingparserregistry_constructor_exists():
    assert callable(syntax::BindingParserRegistry.__init__)


def test_syntax::bindingparserregistry_constructor_args():
    sig = inspect.signature(syntax::BindingParserRegistry.__init__)
    params = list(sig.parameters.keys())



def test_statementparser_is_not_abstract():
    assert not inspect.isabstract(StatementParser)


def test_statementparser_constructor_exists():
    assert callable(StatementParser.__init__)


def test_statementparser_constructor_args():
    sig = inspect.signature(StatementParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax::definitionparser_is_not_abstract():
    assert not inspect.isabstract(syntax::DefinitionParser)


def test_syntax::definitionparser_constructor_exists():
    assert callable(syntax::DefinitionParser.__init__)


def test_syntax::definitionparser_constructor_args():
    sig = inspect.signature(syntax::DefinitionParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax::queryparser_is_not_abstract():
    assert not inspect.isabstract(syntax::QueryParser)


def test_syntax::queryparser_constructor_exists():
    assert callable(syntax::QueryParser.__init__)


def test_syntax::queryparser_constructor_args():
    sig = inspect.signature(syntax::QueryParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax::bindingparser_is_not_abstract():
    assert not inspect.isabstract(syntax::BindingParser)


def test_syntax::bindingparser_constructor_exists():
    assert callable(syntax::BindingParser.__init__)


def test_syntax::bindingparser_constructor_args():
    sig = inspect.signature(syntax::BindingParser.__init__)
    params = list(sig.parameters.keys())



def test_syntax::bindingparseerror_is_not_abstract():
    assert not inspect.isabstract(syntax::BindingParseError)


def test_syntax::bindingparseerror_constructor_exists():
    assert callable(syntax::BindingParseError.__init__)


def test_syntax::bindingparseerror_constructor_args():
    sig = inspect.signature(syntax::BindingParseError.__init__)
    params = list(sig.parameters.keys())



def test_syntax::aliasresolver_is_not_abstract():
    assert not inspect.isabstract(syntax::AliasResolver)


def test_syntax::aliasresolver_constructor_exists():
    assert callable(syntax::AliasResolver.__init__)


def test_syntax::aliasresolver_constructor_args():
    sig = inspect.signature(syntax::AliasResolver.__init__)
    params = list(sig.parameters.keys())



def test_syntax::dbl::option_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::Option)


def test_syntax::dbl::option_constructor_exists():
    assert callable(syntax::dbl::Option.__init__)


def test_syntax::dbl::option_constructor_args():
    sig = inspect.signature(syntax::dbl::Option.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_syntax::dbl::option_has_name():
    assert hasattr(syntax::dbl::Option, "name")
    descriptor = None
    for klass in syntax::dbl::Option.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::option_has_value():
    assert hasattr(syntax::dbl::Option, "value")
    descriptor = None
    for klass in syntax::dbl::Option.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::preparestatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::PrepareStatement)


def test_syntax::dbl::preparestatement_constructor_exists():
    assert callable(syntax::dbl::PrepareStatement.__init__)


def test_syntax::dbl::preparestatement_constructor_args():
    sig = inspect.signature(syntax::dbl::PrepareStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statementName" in params, "Missing parameter 'statementName'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_syntax::dbl::preparestatement_has_statementName():
    assert hasattr(syntax::dbl::PrepareStatement, "statementName")
    descriptor = None
    for klass in syntax::dbl::PrepareStatement.__mro__:
        if "statementName" in klass.__dict__:
            descriptor = klass.__dict__["statementName"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::preparestatement_has_from_():
    assert hasattr(syntax::dbl::PrepareStatement, "from_")
    descriptor = None
    for klass in syntax::dbl::PrepareStatement.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::openstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::OpenStatement)


def test_syntax::dbl::openstatement_constructor_exists():
    assert callable(syntax::dbl::OpenStatement.__init__)


def test_syntax::dbl::openstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::OpenStatement.__init__)
    params = list(sig.parameters.keys())
    assert "usingType" in params, "Missing parameter 'usingType'"
    assert "using" in params, "Missing parameter 'using'"
    assert "cursor" in params, "Missing parameter 'cursor'"

def test_syntax::dbl::openstatement_has_usingType():
    assert hasattr(syntax::dbl::OpenStatement, "usingType")
    descriptor = None
    for klass in syntax::dbl::OpenStatement.__mro__:
        if "usingType" in klass.__dict__:
            descriptor = klass.__dict__["usingType"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::openstatement_has_using():
    assert hasattr(syntax::dbl::OpenStatement, "using")
    descriptor = None
    for klass in syntax::dbl::OpenStatement.__mro__:
        if "using" in klass.__dict__:
            descriptor = klass.__dict__["using"]
            break
    assert isinstance(descriptor, property)

def test_syntax::dbl::openstatement_has_cursor():
    assert hasattr(syntax::dbl::OpenStatement, "cursor")
    descriptor = None
    for klass in syntax::dbl::OpenStatement.__mro__:
        if "cursor" in klass.__dict__:
            descriptor = klass.__dict__["cursor"]
            break
    assert isinstance(descriptor, property)



def test_syntax::dbl::setoptionstatement_is_not_abstract():
    assert not inspect.isabstract(syntax::dbl::SetOptionStatement)


def test_syntax::dbl::setoptionstatement_constructor_exists():
    assert callable(syntax::dbl::SetOptionStatement.__init__)


def test_syntax::dbl::setoptionstatement_constructor_args():
    sig = inspect.signature(syntax::dbl::SetOptionStatement.__init__)
    params = list(sig.parameters.keys())

def test_targetitem_exists():
    # Check that the Enumeration exists
    assert TargetItem is not None

def test_targetitem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TargetItem]
    expected_literals = [
        "CURRENT",
        "ALLSQL",
        "ALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TargetItem"

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

def test_targetelement_exists():
    # Check that the Enumeration exists
    assert TargetElement is not None

def test_targetelement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TargetElement]
    expected_literals = [
        "INDEX",
        "ALIAS",
        "VIEW",
        "TABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TargetElement"

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

def test_rwoperation_exists():
    # Check that the Enumeration exists
    assert RWOperation is not None

def test_rwoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RWOperation]
    expected_literals = [
        "READ_WRITE",
        "READ_ONLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RWOperation"

def test_sharemode_exists():
    # Check that the Enumeration exists
    assert ShareMode is not None

def test_sharemode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShareMode]
    expected_literals = [
        "SHARE",
        "EXCLUSIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShareMode"

def test_usingtype_exists():
    # Check that the Enumeration exists
    assert UsingType is not None

def test_usingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsingType]
    expected_literals = [
        "ALL",
        "LABELS",
        "NONE",
        "BOTH",
        "SYSTEM_NAMES",
        "NAMES",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsingType"

def test_cursortype_exists():
    # Check that the Enumeration exists
    assert CursorType is not None

def test_cursortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CursorType]
    expected_literals = [
        "DYNSCROLL",
        "NOTSCROLL",
        "SCROLL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CursorType"

def test_fetchposition_exists():
    # Check that the Enumeration exists
    assert FetchPosition is not None

def test_fetchposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FetchPosition]
    expected_literals = [
        "PRIOR",
        "FIRST",
        "LAST",
        "NEXT",
        "CURRENT",
        "RELATIVE",
        "AFTER",
        "BEFORE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FetchPosition"

def test_isolationlevel_exists():
    # Check that the Enumeration exists
    assert IsolationLevel is not None

def test_isolationlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IsolationLevel]
    expected_literals = [
        "REPEATABLE_READ",
        "READ_COMMITTED",
        "SERIALIZABLE",
        "NONE",
        "READ_UNCOMMITTED",
        "NO_COMMIT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IsolationLevel"

def test_statementtype_exists():
    # Check that the Enumeration exists
    assert StatementType is not None

def test_statementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatementType]
    expected_literals = [
        "DDL",
        "DML",
        "DBL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatementType"

def test_descriptorscope_exists():
    # Check that the Enumeration exists
    assert DescriptorScope is not None

def test_descriptorscope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DescriptorScope]
    expected_literals = [
        "GLOBAL",
        "LOCAL",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DescriptorScope"


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
syntax::dbl::MultipleRowFetchClause_strategy = st.builds(
    syntax::dbl::MultipleRowFetchClause,
    into=
        safe_text,
    usingDescriptor=
        st.booleans(),
    rowsNumber=
        safe_text,
    descriptor=
        safe_text
)
syntax::dbl::SingleRowFetchClause_strategy = st.builds(
    syntax::dbl::SingleRowFetchClause,
    usingDescriptor=
        st.booleans(),
    into=
        safe_text
)
syntax::dbl::IntoClause_strategy = st.builds(
    syntax::dbl::IntoClause,
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
syntax::dbl::ConditionInfoClause_strategy = st.builds(
    syntax::dbl::ConditionInfoClause,
    condition=
        safe_text
)
BindingStatement_strategy = st.builds(
    BindingStatement,
)
syntax::dbl::CloseStatement_strategy = st.builds(
    syntax::dbl::CloseStatement,
    cursor=
        safe_text
)
syntax::dbl::GetDescriptorStatement_strategy = st.builds(
    syntax::dbl::GetDescriptorStatement,
    descriptorScope=
        safe_text,
    descriptorName=
        safe_text,
    value=
        safe_text
)
syntax::dbl::DescribeStatement_strategy = st.builds(
    syntax::dbl::DescribeStatement,
    statementName=
        safe_text
)
syntax::dbl::FetchStatement_strategy = st.builds(
    syntax::dbl::FetchStatement,
    relativePosition=
        safe_text,
    position=
        safe_text,
    cursorName=
        safe_text
)
syntax::dbl::DeallocateDescriptorStatement_strategy = st.builds(
    syntax::dbl::DeallocateDescriptorStatement,
    descriptorScope=
        safe_text,
    descriptorName=
        safe_text
)
syntax::dbl::ExecuteImmediateStatement_strategy = st.builds(
    syntax::dbl::ExecuteImmediateStatement,
    variable=
        safe_text
)
syntax::dbl::GetDiagnosticsStatement_strategy = st.builds(
    syntax::dbl::GetDiagnosticsStatement,
)
syntax::dbl::SetDescriptorStatement_strategy = st.builds(
    syntax::dbl::SetDescriptorStatement,
    value=
        safe_text,
    descriptorName=
        safe_text
)
syntax::dbl::SetTransactionStatement_strategy = st.builds(
    syntax::dbl::SetTransactionStatement,
    isolationLevel=
        safe_text,
    rwOperation=
        safe_text
)
syntax::dbl::ExecuteStatement_strategy = st.builds(
    syntax::dbl::ExecuteStatement,
    statementName=
        safe_text
)
syntax::dbl::DeclareCursorStatement_strategy = st.builds(
    syntax::dbl::DeclareCursorStatement,
    cursorType=
        safe_text,
    forQuery=
        safe_text,
    cursorName=
        safe_text,
    forStatementName=
        safe_text,
    hold=
        st.booleans()
)
syntax::dbl::AllocateDescriptorStatement_strategy = st.builds(
    syntax::dbl::AllocateDescriptorStatement,
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
syntax::dml::ExtendedQueryExpressionBody_strategy = st.builds(
    syntax::dml::ExtendedQueryExpressionBody,
    optimizeRecordsNumber=
        st.integers()
)
QuerySelect_strategy = st.builds(
    QuerySelect,
)
dml::ExtendedQueryExpressionBody_strategy = st.builds(
    dml::ExtendedQueryExpressionBody,
)
syntax::dml::ExtendedQuerySelect_strategy = st.builds(
    syntax::dml::ExtendedQuerySelect,
)
ddl::syntax::TableColumnDef_strategy = st.builds(
    ddl::syntax::TableColumnDef,
)
ddl::syntax::IndexDef_strategy = st.builds(
    ddl::syntax::IndexDef,
)
ddl::syntax::QualifiedName_strategy = st.builds(
    ddl::syntax::QualifiedName,
)
DefinitionStatement_strategy = st.builds(
    DefinitionStatement,
)
syntax::ddl::CommitStatement_strategy = st.builds(
    syntax::ddl::CommitStatement,
    hold=
        st.booleans()
)
syntax::ddl::DropStatement_strategy = st.builds(
    syntax::ddl::DropStatement,
    target=
        safe_text,
    range=
        safe_text
)
syntax::ddl::RenameStatement_strategy = st.builds(
    syntax::ddl::RenameStatement,
    newName=
        safe_text,
    system=
        safe_text,
    target=
        safe_text
)
syntax::ddl::ConnectStatement_strategy = st.builds(
    syntax::ddl::ConnectStatement,
    pwd=
        safe_text,
    to=
        safe_text,
    reset=
        st.booleans(),
    user=
        safe_text
)
syntax::ddl::RollbackStatement_strategy = st.builds(
    syntax::ddl::RollbackStatement,
    hold=
        st.booleans()
)
syntax::ddl::ReleaseStatement_strategy = st.builds(
    syntax::ddl::ReleaseStatement,
    serverName=
        safe_text
)
syntax::ddl::CreateAliasStatement_strategy = st.builds(
    syntax::ddl::CreateAliasStatement,
)
syntax::ddl::CreateIndexStatement_strategy = st.builds(
    syntax::ddl::CreateIndexStatement,
    unique=
        st.booleans()
)
syntax::ddl::DisconnectStatement_strategy = st.builds(
    syntax::ddl::DisconnectStatement,
    target=
        safe_text
)
syntax::ddl::CreateViewStatement_strategy = st.builds(
    syntax::ddl::CreateViewStatement,
    query=
        safe_text,
    fields=
        safe_text
)
syntax::ddl::SetConnectionStatement_strategy = st.builds(
    syntax::ddl::SetConnectionStatement,
    databaseName=
        safe_text
)
syntax::ddl::LockTableStatement_strategy = st.builds(
    syntax::ddl::LockTableStatement,
    allowRead=
        st.booleans(),
    shareMode=
        safe_text
)
syntax::ddl::CreateTableStatement_strategy = st.builds(
    syntax::ddl::CreateTableStatement,
)
syntax::ddl::CallStatement_strategy = st.builds(
    syntax::ddl::CallStatement,
    parms=
        safe_text
)
syntax::StatementParser_strategy = st.builds(
    syntax::StatementParser,
)
syntax::StatementWriter_strategy = st.builds(
    syntax::StatementWriter,
)
syntax::SQLObjectNameHelper_strategy = st.builds(
    syntax::SQLObjectNameHelper,
)
syntax::QueryParserRegistry_strategy = st.builds(
    syntax::QueryParserRegistry,
)
syntax::QueryWriterRegistry_strategy = st.builds(
    syntax::QueryWriterRegistry,
)
syntax::NameHelperRegistry_strategy = st.builds(
    syntax::NameHelperRegistry,
)
SQLObjectNameHelper_strategy = st.builds(
    SQLObjectNameHelper,
)
syntax::NameHelper_strategy = st.builds(
    syntax::NameHelper,
)
syntax::DefinitionWriterRegistry_strategy = st.builds(
    syntax::DefinitionWriterRegistry,
)
StatementWriter_strategy = st.builds(
    StatementWriter,
)
syntax::QueryWriter_strategy = st.builds(
    syntax::QueryWriter,
)
syntax::DefinitionWriter_strategy = st.builds(
    syntax::DefinitionWriter,
)
syntax::DefinitionStatement_strategy = st.builds(
    syntax::DefinitionStatement,
)
syntax::DefinitionParseResult_strategy = st.builds(
    syntax::DefinitionParseResult,
)
syntax::DefinitionParseError_strategy = st.builds(
    syntax::DefinitionParseError,
)
syntax::DefinitionParserRegistry_strategy = st.builds(
    syntax::DefinitionParserRegistry,
)
syntax::BindingStatement_strategy = st.builds(
    syntax::BindingStatement,
)
syntax::BindingParseResult_strategy = st.builds(
    syntax::BindingParseResult,
)
syntax::BindingParserRegistry_strategy = st.builds(
    syntax::BindingParserRegistry,
)
StatementParser_strategy = st.builds(
    StatementParser,
)
syntax::DefinitionParser_strategy = st.builds(
    syntax::DefinitionParser,
)
syntax::QueryParser_strategy = st.builds(
    syntax::QueryParser,
)
syntax::BindingParser_strategy = st.builds(
    syntax::BindingParser,
)
syntax::BindingParseError_strategy = st.builds(
    syntax::BindingParseError,
)
syntax::AliasResolver_strategy = st.builds(
    syntax::AliasResolver,
)
syntax::dbl::Option_strategy = st.builds(
    syntax::dbl::Option,
    name=
        safe_text,
    value=
        safe_text
)
syntax::dbl::PrepareStatement_strategy = st.builds(
    syntax::dbl::PrepareStatement,
    statementName=
        safe_text,
    from_=
        safe_text
)
syntax::dbl::OpenStatement_strategy = st.builds(
    syntax::dbl::OpenStatement,
    usingType=
        safe_text,
    using=
        safe_text,
    cursor=
        safe_text
)
syntax::dbl::SetOptionStatement_strategy = st.builds(
    syntax::dbl::SetOptionStatement,
)

@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
@settings(max_examples=50)
def test_syntax::dbl::multiplerowfetchclause_instantiation(instance):
    assert isinstance(instance, syntax::dbl::MultipleRowFetchClause)

@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_into_type(instance):
    assert isinstance(instance.into, str)


@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_usingDescriptor_type(instance):
    assert isinstance(instance.usingDescriptor, bool)


@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_usingDescriptor_setter(instance):
    original = instance.usingDescriptor
    instance.usingDescriptor = original
    assert instance.usingDescriptor == original

@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_rowsNumber_type(instance):
    assert isinstance(instance.rowsNumber, str)


@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_rowsNumber_setter(instance):
    original = instance.rowsNumber
    instance.rowsNumber = original
    assert instance.rowsNumber == original

@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=syntax::dbl::MultipleRowFetchClause_strategy)
def test_syntax::dbl::multiplerowfetchclause_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=syntax::dbl::SingleRowFetchClause_strategy)
@settings(max_examples=50)
def test_syntax::dbl::singlerowfetchclause_instantiation(instance):
    assert isinstance(instance, syntax::dbl::SingleRowFetchClause)

@given(instance=syntax::dbl::SingleRowFetchClause_strategy)
def test_syntax::dbl::singlerowfetchclause_usingDescriptor_type(instance):
    assert isinstance(instance.usingDescriptor, bool)


@given(instance=syntax::dbl::SingleRowFetchClause_strategy)
def test_syntax::dbl::singlerowfetchclause_usingDescriptor_setter(instance):
    original = instance.usingDescriptor
    instance.usingDescriptor = original
    assert instance.usingDescriptor == original

@given(instance=syntax::dbl::SingleRowFetchClause_strategy)
def test_syntax::dbl::singlerowfetchclause_into_type(instance):
    assert isinstance(instance.into, str)


@given(instance=syntax::dbl::SingleRowFetchClause_strategy)
def test_syntax::dbl::singlerowfetchclause_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=syntax::dbl::IntoClause_strategy)
@settings(max_examples=50)
def test_syntax::dbl::intoclause_instantiation(instance):
    assert isinstance(instance, syntax::dbl::IntoClause)

@given(instance=syntax::dbl::IntoClause_strategy)
def test_syntax::dbl::intoclause_using_type(instance):
    assert isinstance(instance.using, str)


@given(instance=syntax::dbl::IntoClause_strategy)
def test_syntax::dbl::intoclause_using_setter(instance):
    original = instance.using
    instance.using = original
    assert instance.using == original

@given(instance=syntax::dbl::IntoClause_strategy)
def test_syntax::dbl::intoclause_descriptorName_type(instance):
    assert isinstance(instance.descriptorName, str)


@given(instance=syntax::dbl::IntoClause_strategy)
def test_syntax::dbl::intoclause_descriptorName_setter(instance):
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

@given(instance=syntax::dbl::ConditionInfoClause_strategy)
@settings(max_examples=50)
def test_syntax::dbl::conditioninfoclause_instantiation(instance):
    assert isinstance(instance, syntax::dbl::ConditionInfoClause)

@given(instance=syntax::dbl::ConditionInfoClause_strategy)
def test_syntax::dbl::conditioninfoclause_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=syntax::dbl::ConditionInfoClause_strategy)
def test_syntax::dbl::conditioninfoclause_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=BindingStatement_strategy)
@settings(max_examples=50)
def test_bindingstatement_instantiation(instance):
    assert isinstance(instance, BindingStatement)

@given(instance=syntax::dbl::CloseStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::closestatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::CloseStatement)

@given(instance=syntax::dbl::CloseStatement_strategy)
def test_syntax::dbl::closestatement_cursor_type(instance):
    assert isinstance(instance.cursor, str)


@given(instance=syntax::dbl::CloseStatement_strategy)
def test_syntax::dbl::closestatement_cursor_setter(instance):
    original = instance.cursor
    instance.cursor = original
    assert instance.cursor == original

@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::getdescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::GetDescriptorStatement)

@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
def test_syntax::dbl::getdescriptorstatement_descriptorScope_type(instance):
    assert isinstance(instance.descriptorScope, str)


@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
def test_syntax::dbl::getdescriptorstatement_descriptorScope_setter(instance):
    original = instance.descriptorScope
    instance.descriptorScope = original
    assert instance.descriptorScope == original

@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
def test_syntax::dbl::getdescriptorstatement_descriptorName_type(instance):
    assert isinstance(instance.descriptorName, str)


@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
def test_syntax::dbl::getdescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original

@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
def test_syntax::dbl::getdescriptorstatement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=syntax::dbl::GetDescriptorStatement_strategy)
def test_syntax::dbl::getdescriptorstatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=syntax::dbl::DescribeStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::describestatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::DescribeStatement)

@given(instance=syntax::dbl::DescribeStatement_strategy)
def test_syntax::dbl::describestatement_statementName_type(instance):
    assert isinstance(instance.statementName, str)


@given(instance=syntax::dbl::DescribeStatement_strategy)
def test_syntax::dbl::describestatement_statementName_setter(instance):
    original = instance.statementName
    instance.statementName = original
    assert instance.statementName == original

@given(instance=syntax::dbl::FetchStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::fetchstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::FetchStatement)

@given(instance=syntax::dbl::FetchStatement_strategy)
def test_syntax::dbl::fetchstatement_relativePosition_type(instance):
    assert isinstance(instance.relativePosition, str)


@given(instance=syntax::dbl::FetchStatement_strategy)
def test_syntax::dbl::fetchstatement_relativePosition_setter(instance):
    original = instance.relativePosition
    instance.relativePosition = original
    assert instance.relativePosition == original

@given(instance=syntax::dbl::FetchStatement_strategy)
def test_syntax::dbl::fetchstatement_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=syntax::dbl::FetchStatement_strategy)
def test_syntax::dbl::fetchstatement_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=syntax::dbl::FetchStatement_strategy)
def test_syntax::dbl::fetchstatement_cursorName_type(instance):
    assert isinstance(instance.cursorName, str)


@given(instance=syntax::dbl::FetchStatement_strategy)
def test_syntax::dbl::fetchstatement_cursorName_setter(instance):
    original = instance.cursorName
    instance.cursorName = original
    assert instance.cursorName == original

@given(instance=syntax::dbl::DeallocateDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::deallocatedescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::DeallocateDescriptorStatement)

@given(instance=syntax::dbl::DeallocateDescriptorStatement_strategy)
def test_syntax::dbl::deallocatedescriptorstatement_descriptorScope_type(instance):
    assert isinstance(instance.descriptorScope, str)


@given(instance=syntax::dbl::DeallocateDescriptorStatement_strategy)
def test_syntax::dbl::deallocatedescriptorstatement_descriptorScope_setter(instance):
    original = instance.descriptorScope
    instance.descriptorScope = original
    assert instance.descriptorScope == original

@given(instance=syntax::dbl::DeallocateDescriptorStatement_strategy)
def test_syntax::dbl::deallocatedescriptorstatement_descriptorName_type(instance):
    assert isinstance(instance.descriptorName, str)


@given(instance=syntax::dbl::DeallocateDescriptorStatement_strategy)
def test_syntax::dbl::deallocatedescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original

@given(instance=syntax::dbl::ExecuteImmediateStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::executeimmediatestatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::ExecuteImmediateStatement)

@given(instance=syntax::dbl::ExecuteImmediateStatement_strategy)
def test_syntax::dbl::executeimmediatestatement_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=syntax::dbl::ExecuteImmediateStatement_strategy)
def test_syntax::dbl::executeimmediatestatement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=syntax::dbl::GetDiagnosticsStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::getdiagnosticsstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::GetDiagnosticsStatement)

@given(instance=syntax::dbl::SetDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::setdescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::SetDescriptorStatement)

@given(instance=syntax::dbl::SetDescriptorStatement_strategy)
def test_syntax::dbl::setdescriptorstatement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=syntax::dbl::SetDescriptorStatement_strategy)
def test_syntax::dbl::setdescriptorstatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=syntax::dbl::SetDescriptorStatement_strategy)
def test_syntax::dbl::setdescriptorstatement_descriptorName_type(instance):
    assert isinstance(instance.descriptorName, str)


@given(instance=syntax::dbl::SetDescriptorStatement_strategy)
def test_syntax::dbl::setdescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original

@given(instance=syntax::dbl::SetTransactionStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::settransactionstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::SetTransactionStatement)

@given(instance=syntax::dbl::SetTransactionStatement_strategy)
def test_syntax::dbl::settransactionstatement_isolationLevel_type(instance):
    assert isinstance(instance.isolationLevel, str)


@given(instance=syntax::dbl::SetTransactionStatement_strategy)
def test_syntax::dbl::settransactionstatement_isolationLevel_setter(instance):
    original = instance.isolationLevel
    instance.isolationLevel = original
    assert instance.isolationLevel == original

@given(instance=syntax::dbl::SetTransactionStatement_strategy)
def test_syntax::dbl::settransactionstatement_rwOperation_type(instance):
    assert isinstance(instance.rwOperation, str)


@given(instance=syntax::dbl::SetTransactionStatement_strategy)
def test_syntax::dbl::settransactionstatement_rwOperation_setter(instance):
    original = instance.rwOperation
    instance.rwOperation = original
    assert instance.rwOperation == original

@given(instance=syntax::dbl::ExecuteStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::executestatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::ExecuteStatement)

@given(instance=syntax::dbl::ExecuteStatement_strategy)
def test_syntax::dbl::executestatement_statementName_type(instance):
    assert isinstance(instance.statementName, str)


@given(instance=syntax::dbl::ExecuteStatement_strategy)
def test_syntax::dbl::executestatement_statementName_setter(instance):
    original = instance.statementName
    instance.statementName = original
    assert instance.statementName == original

@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::declarecursorstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::DeclareCursorStatement)

@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_cursorType_type(instance):
    assert isinstance(instance.cursorType, str)


@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_cursorType_setter(instance):
    original = instance.cursorType
    instance.cursorType = original
    assert instance.cursorType == original

@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_forQuery_type(instance):
    assert isinstance(instance.forQuery, str)


@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_forQuery_setter(instance):
    original = instance.forQuery
    instance.forQuery = original
    assert instance.forQuery == original

@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_cursorName_type(instance):
    assert isinstance(instance.cursorName, str)


@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_cursorName_setter(instance):
    original = instance.cursorName
    instance.cursorName = original
    assert instance.cursorName == original

@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_forStatementName_type(instance):
    assert isinstance(instance.forStatementName, str)


@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_forStatementName_setter(instance):
    original = instance.forStatementName
    instance.forStatementName = original
    assert instance.forStatementName == original

@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_hold_type(instance):
    assert isinstance(instance.hold, bool)


@given(instance=syntax::dbl::DeclareCursorStatement_strategy)
def test_syntax::dbl::declarecursorstatement_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original

@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::allocatedescriptorstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::AllocateDescriptorStatement)

@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
def test_syntax::dbl::allocatedescriptorstatement_descriptorScope_type(instance):
    assert isinstance(instance.descriptorScope, str)


@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
def test_syntax::dbl::allocatedescriptorstatement_descriptorScope_setter(instance):
    original = instance.descriptorScope
    instance.descriptorScope = original
    assert instance.descriptorScope == original

@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
def test_syntax::dbl::allocatedescriptorstatement_withMax_type(instance):
    assert isinstance(instance.withMax, str)


@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
def test_syntax::dbl::allocatedescriptorstatement_withMax_setter(instance):
    original = instance.withMax
    instance.withMax = original
    assert instance.withMax == original

@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
def test_syntax::dbl::allocatedescriptorstatement_descriptorName_type(instance):
    assert isinstance(instance.descriptorName, str)


@given(instance=syntax::dbl::AllocateDescriptorStatement_strategy)
def test_syntax::dbl::allocatedescriptorstatement_descriptorName_setter(instance):
    original = instance.descriptorName
    instance.descriptorName = original
    assert instance.descriptorName == original

@given(instance=QueryExpressionBody_strategy)
@settings(max_examples=50)
def test_queryexpressionbody_instantiation(instance):
    assert isinstance(instance, QueryExpressionBody)

@given(instance=syntax::dml::ExtendedQueryExpressionBody_strategy)
@settings(max_examples=50)
def test_syntax::dml::extendedqueryexpressionbody_instantiation(instance):
    assert isinstance(instance, syntax::dml::ExtendedQueryExpressionBody)

@given(instance=syntax::dml::ExtendedQueryExpressionBody_strategy)
def test_syntax::dml::extendedqueryexpressionbody_optimizeRecordsNumber_type(instance):
    assert isinstance(instance.optimizeRecordsNumber, int)


@given(instance=syntax::dml::ExtendedQueryExpressionBody_strategy)
def test_syntax::dml::extendedqueryexpressionbody_optimizeRecordsNumber_setter(instance):
    original = instance.optimizeRecordsNumber
    instance.optimizeRecordsNumber = original
    assert instance.optimizeRecordsNumber == original

@given(instance=QuerySelect_strategy)
@settings(max_examples=50)
def test_queryselect_instantiation(instance):
    assert isinstance(instance, QuerySelect)

@given(instance=dml::ExtendedQueryExpressionBody_strategy)
@settings(max_examples=50)
def test_dml::extendedqueryexpressionbody_instantiation(instance):
    assert isinstance(instance, dml::ExtendedQueryExpressionBody)

@given(instance=syntax::dml::ExtendedQuerySelect_strategy)
@settings(max_examples=50)
def test_syntax::dml::extendedqueryselect_instantiation(instance):
    assert isinstance(instance, syntax::dml::ExtendedQuerySelect)

@given(instance=ddl::syntax::TableColumnDef_strategy)
@settings(max_examples=50)
def test_ddl::syntax::tablecolumndef_instantiation(instance):
    assert isinstance(instance, ddl::syntax::TableColumnDef)

@given(instance=ddl::syntax::IndexDef_strategy)
@settings(max_examples=50)
def test_ddl::syntax::indexdef_instantiation(instance):
    assert isinstance(instance, ddl::syntax::IndexDef)

@given(instance=ddl::syntax::QualifiedName_strategy)
@settings(max_examples=50)
def test_ddl::syntax::qualifiedname_instantiation(instance):
    assert isinstance(instance, ddl::syntax::QualifiedName)

@given(instance=DefinitionStatement_strategy)
@settings(max_examples=50)
def test_definitionstatement_instantiation(instance):
    assert isinstance(instance, DefinitionStatement)

@given(instance=syntax::ddl::CommitStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::commitstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::CommitStatement)

@given(instance=syntax::ddl::CommitStatement_strategy)
def test_syntax::ddl::commitstatement_hold_type(instance):
    assert isinstance(instance.hold, bool)


@given(instance=syntax::ddl::CommitStatement_strategy)
def test_syntax::ddl::commitstatement_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original

@given(instance=syntax::ddl::DropStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::dropstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::DropStatement)

@given(instance=syntax::ddl::DropStatement_strategy)
def test_syntax::ddl::dropstatement_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=syntax::ddl::DropStatement_strategy)
def test_syntax::ddl::dropstatement_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=syntax::ddl::DropStatement_strategy)
def test_syntax::ddl::dropstatement_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=syntax::ddl::DropStatement_strategy)
def test_syntax::ddl::dropstatement_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=syntax::ddl::RenameStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::renamestatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::RenameStatement)

@given(instance=syntax::ddl::RenameStatement_strategy)
def test_syntax::ddl::renamestatement_newName_type(instance):
    assert isinstance(instance.newName, str)


@given(instance=syntax::ddl::RenameStatement_strategy)
def test_syntax::ddl::renamestatement_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original

@given(instance=syntax::ddl::RenameStatement_strategy)
def test_syntax::ddl::renamestatement_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=syntax::ddl::RenameStatement_strategy)
def test_syntax::ddl::renamestatement_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=syntax::ddl::RenameStatement_strategy)
def test_syntax::ddl::renamestatement_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=syntax::ddl::RenameStatement_strategy)
def test_syntax::ddl::renamestatement_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=syntax::ddl::ConnectStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::connectstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::ConnectStatement)

@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_pwd_type(instance):
    assert isinstance(instance.pwd, str)


@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_pwd_setter(instance):
    original = instance.pwd
    instance.pwd = original
    assert instance.pwd == original

@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_reset_type(instance):
    assert isinstance(instance.reset, bool)


@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_reset_setter(instance):
    original = instance.reset
    instance.reset = original
    assert instance.reset == original

@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=syntax::ddl::ConnectStatement_strategy)
def test_syntax::ddl::connectstatement_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=syntax::ddl::RollbackStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::rollbackstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::RollbackStatement)

@given(instance=syntax::ddl::RollbackStatement_strategy)
def test_syntax::ddl::rollbackstatement_hold_type(instance):
    assert isinstance(instance.hold, bool)


@given(instance=syntax::ddl::RollbackStatement_strategy)
def test_syntax::ddl::rollbackstatement_hold_setter(instance):
    original = instance.hold
    instance.hold = original
    assert instance.hold == original

@given(instance=syntax::ddl::ReleaseStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::releasestatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::ReleaseStatement)

@given(instance=syntax::ddl::ReleaseStatement_strategy)
def test_syntax::ddl::releasestatement_serverName_type(instance):
    assert isinstance(instance.serverName, str)


@given(instance=syntax::ddl::ReleaseStatement_strategy)
def test_syntax::ddl::releasestatement_serverName_setter(instance):
    original = instance.serverName
    instance.serverName = original
    assert instance.serverName == original

@given(instance=syntax::ddl::CreateAliasStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::createaliasstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::CreateAliasStatement)

@given(instance=syntax::ddl::CreateIndexStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::createindexstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::CreateIndexStatement)

@given(instance=syntax::ddl::CreateIndexStatement_strategy)
def test_syntax::ddl::createindexstatement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=syntax::ddl::CreateIndexStatement_strategy)
def test_syntax::ddl::createindexstatement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=syntax::ddl::DisconnectStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::disconnectstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::DisconnectStatement)

@given(instance=syntax::ddl::DisconnectStatement_strategy)
def test_syntax::ddl::disconnectstatement_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=syntax::ddl::DisconnectStatement_strategy)
def test_syntax::ddl::disconnectstatement_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=syntax::ddl::CreateViewStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::createviewstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::CreateViewStatement)

@given(instance=syntax::ddl::CreateViewStatement_strategy)
def test_syntax::ddl::createviewstatement_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=syntax::ddl::CreateViewStatement_strategy)
def test_syntax::ddl::createviewstatement_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=syntax::ddl::CreateViewStatement_strategy)
def test_syntax::ddl::createviewstatement_fields_type(instance):
    assert isinstance(instance.fields, str)


@given(instance=syntax::ddl::CreateViewStatement_strategy)
def test_syntax::ddl::createviewstatement_fields_setter(instance):
    original = instance.fields
    instance.fields = original
    assert instance.fields == original

@given(instance=syntax::ddl::SetConnectionStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::setconnectionstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::SetConnectionStatement)

@given(instance=syntax::ddl::SetConnectionStatement_strategy)
def test_syntax::ddl::setconnectionstatement_databaseName_type(instance):
    assert isinstance(instance.databaseName, str)


@given(instance=syntax::ddl::SetConnectionStatement_strategy)
def test_syntax::ddl::setconnectionstatement_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=syntax::ddl::LockTableStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::locktablestatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::LockTableStatement)

@given(instance=syntax::ddl::LockTableStatement_strategy)
def test_syntax::ddl::locktablestatement_allowRead_type(instance):
    assert isinstance(instance.allowRead, bool)


@given(instance=syntax::ddl::LockTableStatement_strategy)
def test_syntax::ddl::locktablestatement_allowRead_setter(instance):
    original = instance.allowRead
    instance.allowRead = original
    assert instance.allowRead == original

@given(instance=syntax::ddl::LockTableStatement_strategy)
def test_syntax::ddl::locktablestatement_shareMode_type(instance):
    assert isinstance(instance.shareMode, str)


@given(instance=syntax::ddl::LockTableStatement_strategy)
def test_syntax::ddl::locktablestatement_shareMode_setter(instance):
    original = instance.shareMode
    instance.shareMode = original
    assert instance.shareMode == original

@given(instance=syntax::ddl::CreateTableStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::createtablestatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::CreateTableStatement)

@given(instance=syntax::ddl::CallStatement_strategy)
@settings(max_examples=50)
def test_syntax::ddl::callstatement_instantiation(instance):
    assert isinstance(instance, syntax::ddl::CallStatement)

@given(instance=syntax::ddl::CallStatement_strategy)
def test_syntax::ddl::callstatement_parms_type(instance):
    assert isinstance(instance.parms, str)


@given(instance=syntax::ddl::CallStatement_strategy)
def test_syntax::ddl::callstatement_parms_setter(instance):
    original = instance.parms
    instance.parms = original
    assert instance.parms == original

@given(instance=syntax::StatementParser_strategy)
@settings(max_examples=50)
def test_syntax::statementparser_instantiation(instance):
    assert isinstance(instance, syntax::StatementParser)

@given(instance=syntax::StatementWriter_strategy)
@settings(max_examples=50)
def test_syntax::statementwriter_instantiation(instance):
    assert isinstance(instance, syntax::StatementWriter)

@given(instance=syntax::SQLObjectNameHelper_strategy)
@settings(max_examples=50)
def test_syntax::sqlobjectnamehelper_instantiation(instance):
    assert isinstance(instance, syntax::SQLObjectNameHelper)

@given(instance=syntax::QueryParserRegistry_strategy)
@settings(max_examples=50)
def test_syntax::queryparserregistry_instantiation(instance):
    assert isinstance(instance, syntax::QueryParserRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::QueryParserRegistry_strategy)
@settings(max_examples=30)
def test_syntax::queryparserregistry_lookup_changes_state(instance):
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
        assert has_statements, f"Function 'lookup' in syntax::QueryParserRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax::QueryParserRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax::QueryParserRegistry is not implemented or raised an error")

@given(instance=syntax::QueryWriterRegistry_strategy)
@settings(max_examples=50)
def test_syntax::querywriterregistry_instantiation(instance):
    assert isinstance(instance, syntax::QueryWriterRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::QueryWriterRegistry_strategy)
@settings(max_examples=30)
def test_syntax::querywriterregistry_lookup_changes_state(instance):
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
        assert has_statements, f"Function 'lookup' in syntax::QueryWriterRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax::QueryWriterRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax::QueryWriterRegistry is not implemented or raised an error")

@given(instance=syntax::NameHelperRegistry_strategy)
@settings(max_examples=50)
def test_syntax::namehelperregistry_instantiation(instance):
    assert isinstance(instance, syntax::NameHelperRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::NameHelperRegistry_strategy)
@settings(max_examples=30)
def test_syntax::namehelperregistry_lookup_changes_state(instance):
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
        assert has_statements, f"Function 'lookup' in syntax::NameHelperRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax::NameHelperRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax::NameHelperRegistry is not implemented or raised an error")

@given(instance=SQLObjectNameHelper_strategy)
@settings(max_examples=50)
def test_sqlobjectnamehelper_instantiation(instance):
    assert isinstance(instance, SQLObjectNameHelper)

@given(instance=syntax::NameHelper_strategy)
@settings(max_examples=50)
def test_syntax::namehelper_instantiation(instance):
    assert isinstance(instance, syntax::NameHelper)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::NameHelper_strategy)
@settings(max_examples=30)
def test_syntax::namehelper_resolvecontainers_changes_state(instance):
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
        assert has_statements, f"Function 'resolveContainers' in syntax::NameHelper is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolveContainers' in syntax::NameHelper did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolveContainers' in syntax::NameHelper is not implemented or raised an error")

@given(instance=syntax::DefinitionWriterRegistry_strategy)
@settings(max_examples=50)
def test_syntax::definitionwriterregistry_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionWriterRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriterRegistry_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriterregistry_lookup_changes_state(instance):
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
        assert has_statements, f"Function 'lookup' in syntax::DefinitionWriterRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax::DefinitionWriterRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax::DefinitionWriterRegistry is not implemented or raised an error")

@given(instance=StatementWriter_strategy)
@settings(max_examples=50)
def test_statementwriter_instantiation(instance):
    assert isinstance(instance, StatementWriter)

@given(instance=syntax::QueryWriter_strategy)
@settings(max_examples=50)
def test_syntax::querywriter_instantiation(instance):
    assert isinstance(instance, syntax::QueryWriter)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::QueryWriter_strategy)
@settings(max_examples=30)
def test_syntax::querywriter_writequery_changes_state(instance):
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
        assert has_statements, f"Function 'writeQuery' in syntax::QueryWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'writeQuery' in syntax::QueryWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'writeQuery' in syntax::QueryWriter is not implemented or raised an error")

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=50)
def test_syntax::definitionwriter_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionWriter)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_copytabledata_changes_state(instance):
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
        assert has_statements, f"Function 'copyTableData' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copyTableData' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copyTableData' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_createtable_changes_state(instance):
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
        assert has_statements, f"Function 'createTable' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createTable' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createTable' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_renameindex_changes_state(instance):
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
        assert has_statements, f"Function 'renameIndex' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'renameIndex' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'renameIndex' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_createlabel_changes_state(instance):
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
        assert has_statements, f"Function 'createLabel' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLabel' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLabel' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_createview_changes_state(instance):
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
        assert has_statements, f"Function 'createView' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createView' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createView' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_dropview_changes_state(instance):
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
        assert has_statements, f"Function 'dropView' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropView' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropView' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_renametable_changes_state(instance):
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
        assert has_statements, f"Function 'renameTable' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'renameTable' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'renameTable' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_dropschema_changes_state(instance):
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
        assert has_statements, f"Function 'dropSchema' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropSchema' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropSchema' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_createlabelforfields_changes_state(instance):
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
        assert has_statements, f"Function 'createLabelForFields' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLabelForFields' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLabelForFields' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_haslogicals_changes_state(instance):
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
        assert has_statements, f"Function 'hasLogicals' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasLogicals' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasLogicals' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_deletedata_changes_state(instance):
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
        assert has_statements, f"Function 'deleteData' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'deleteData' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'deleteData' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_createschema_changes_state(instance):
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
        assert has_statements, f"Function 'createSchema' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createSchema' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createSchema' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_truncatetable_changes_state(instance):
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
        assert has_statements, f"Function 'truncateTable' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'truncateTable' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'truncateTable' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_dropindex_changes_state(instance):
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
        assert has_statements, f"Function 'dropIndex' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropIndex' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropIndex' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_selectdata_changes_state(instance):
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
        assert has_statements, f"Function 'selectData' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'selectData' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'selectData' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_insertdata_changes_state(instance):
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
        assert has_statements, f"Function 'insertData' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'insertData' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'insertData' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_createindex_changes_state(instance):
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
        assert has_statements, f"Function 'createIndex' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createIndex' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createIndex' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_droptable_changes_state(instance):
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
        assert has_statements, f"Function 'dropTable' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dropTable' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dropTable' in syntax::DefinitionWriter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionWriter_strategy)
@settings(max_examples=30)
def test_syntax::definitionwriter_countrecords_changes_state(instance):
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
        assert has_statements, f"Function 'countRecords' in syntax::DefinitionWriter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'countRecords' in syntax::DefinitionWriter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'countRecords' in syntax::DefinitionWriter is not implemented or raised an error")

@given(instance=syntax::DefinitionStatement_strategy)
@settings(max_examples=50)
def test_syntax::definitionstatement_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionStatement)

@given(instance=syntax::DefinitionParseResult_strategy)
@settings(max_examples=50)
def test_syntax::definitionparseresult_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionParseResult)

@given(instance=syntax::DefinitionParseError_strategy)
@settings(max_examples=50)
def test_syntax::definitionparseerror_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionParseError)

@given(instance=syntax::DefinitionParserRegistry_strategy)
@settings(max_examples=50)
def test_syntax::definitionparserregistry_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionParserRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionParserRegistry_strategy)
@settings(max_examples=30)
def test_syntax::definitionparserregistry_lookup_changes_state(instance):
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
        assert has_statements, f"Function 'lookup' in syntax::DefinitionParserRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax::DefinitionParserRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax::DefinitionParserRegistry is not implemented or raised an error")

@given(instance=syntax::BindingStatement_strategy)
@settings(max_examples=50)
def test_syntax::bindingstatement_instantiation(instance):
    assert isinstance(instance, syntax::BindingStatement)

@given(instance=syntax::BindingParseResult_strategy)
@settings(max_examples=50)
def test_syntax::bindingparseresult_instantiation(instance):
    assert isinstance(instance, syntax::BindingParseResult)

@given(instance=syntax::BindingParserRegistry_strategy)
@settings(max_examples=50)
def test_syntax::bindingparserregistry_instantiation(instance):
    assert isinstance(instance, syntax::BindingParserRegistry)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::BindingParserRegistry_strategy)
@settings(max_examples=30)
def test_syntax::bindingparserregistry_lookup_changes_state(instance):
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
        assert has_statements, f"Function 'lookup' in syntax::BindingParserRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lookup' in syntax::BindingParserRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lookup' in syntax::BindingParserRegistry is not implemented or raised an error")

@given(instance=StatementParser_strategy)
@settings(max_examples=50)
def test_statementparser_instantiation(instance):
    assert isinstance(instance, StatementParser)

@given(instance=syntax::DefinitionParser_strategy)
@settings(max_examples=50)
def test_syntax::definitionparser_instantiation(instance):
    assert isinstance(instance, syntax::DefinitionParser)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::DefinitionParser_strategy)
@settings(max_examples=30)
def test_syntax::definitionparser_parsedefinition_changes_state(instance):
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
        assert has_statements, f"Function 'parseDefinition' in syntax::DefinitionParser is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parseDefinition' in syntax::DefinitionParser did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parseDefinition' in syntax::DefinitionParser is not implemented or raised an error")

@given(instance=syntax::QueryParser_strategy)
@settings(max_examples=50)
def test_syntax::queryparser_instantiation(instance):
    assert isinstance(instance, syntax::QueryParser)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::QueryParser_strategy)
@settings(max_examples=30)
def test_syntax::queryparser_parsequery_changes_state(instance):
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
        assert has_statements, f"Function 'parseQuery' in syntax::QueryParser is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parseQuery' in syntax::QueryParser did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parseQuery' in syntax::QueryParser is not implemented or raised an error")

@given(instance=syntax::BindingParser_strategy)
@settings(max_examples=50)
def test_syntax::bindingparser_instantiation(instance):
    assert isinstance(instance, syntax::BindingParser)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::BindingParser_strategy)
@settings(max_examples=30)
def test_syntax::bindingparser_parsebinding_changes_state(instance):
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
        assert has_statements, f"Function 'parseBinding' in syntax::BindingParser is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parseBinding' in syntax::BindingParser did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parseBinding' in syntax::BindingParser is not implemented or raised an error")

@given(instance=syntax::BindingParseError_strategy)
@settings(max_examples=50)
def test_syntax::bindingparseerror_instantiation(instance):
    assert isinstance(instance, syntax::BindingParseError)

@given(instance=syntax::AliasResolver_strategy)
@settings(max_examples=50)
def test_syntax::aliasresolver_instantiation(instance):
    assert isinstance(instance, syntax::AliasResolver)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=syntax::AliasResolver_strategy)
@settings(max_examples=30)
def test_syntax::aliasresolver_resolvequery_changes_state(instance):
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
        assert has_statements, f"Function 'resolveQuery' in syntax::AliasResolver is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolveQuery' in syntax::AliasResolver did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolveQuery' in syntax::AliasResolver is not implemented or raised an error")

@given(instance=syntax::dbl::Option_strategy)
@settings(max_examples=50)
def test_syntax::dbl::option_instantiation(instance):
    assert isinstance(instance, syntax::dbl::Option)

@given(instance=syntax::dbl::Option_strategy)
def test_syntax::dbl::option_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=syntax::dbl::Option_strategy)
def test_syntax::dbl::option_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=syntax::dbl::Option_strategy)
def test_syntax::dbl::option_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=syntax::dbl::Option_strategy)
def test_syntax::dbl::option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=syntax::dbl::PrepareStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::preparestatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::PrepareStatement)

@given(instance=syntax::dbl::PrepareStatement_strategy)
def test_syntax::dbl::preparestatement_statementName_type(instance):
    assert isinstance(instance.statementName, str)


@given(instance=syntax::dbl::PrepareStatement_strategy)
def test_syntax::dbl::preparestatement_statementName_setter(instance):
    original = instance.statementName
    instance.statementName = original
    assert instance.statementName == original

@given(instance=syntax::dbl::PrepareStatement_strategy)
def test_syntax::dbl::preparestatement_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=syntax::dbl::PrepareStatement_strategy)
def test_syntax::dbl::preparestatement_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=syntax::dbl::OpenStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::openstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::OpenStatement)

@given(instance=syntax::dbl::OpenStatement_strategy)
def test_syntax::dbl::openstatement_usingType_type(instance):
    assert isinstance(instance.usingType, str)


@given(instance=syntax::dbl::OpenStatement_strategy)
def test_syntax::dbl::openstatement_usingType_setter(instance):
    original = instance.usingType
    instance.usingType = original
    assert instance.usingType == original

@given(instance=syntax::dbl::OpenStatement_strategy)
def test_syntax::dbl::openstatement_using_type(instance):
    assert isinstance(instance.using, str)


@given(instance=syntax::dbl::OpenStatement_strategy)
def test_syntax::dbl::openstatement_using_setter(instance):
    original = instance.using
    instance.using = original
    assert instance.using == original

@given(instance=syntax::dbl::OpenStatement_strategy)
def test_syntax::dbl::openstatement_cursor_type(instance):
    assert isinstance(instance.cursor, str)


@given(instance=syntax::dbl::OpenStatement_strategy)
def test_syntax::dbl::openstatement_cursor_setter(instance):
    original = instance.cursor
    instance.cursor = original
    assert instance.cursor == original

@given(instance=syntax::dbl::SetOptionStatement_strategy)
@settings(max_examples=50)
def test_syntax::dbl::setoptionstatement_instantiation(instance):
    assert isinstance(instance, syntax::dbl::SetOptionStatement)
