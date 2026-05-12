import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ValueExp,
    SQLDML::IntegerValueExp,
    SQLDML::StringValueExp,
    DataType,
    StringValueExp,
    Predicate,
    SQLDML::ListExp,
    SQLDML::FunctionExp,
    SQLDML::ValueExp,
    BinaryExp,
    SQLDML::AndExp,
    SQLDML::OperationExp,
    SQLDML::OrExp,
    WhereClause,
    NamedElement,
    SQLDML::DataType,
    SQLDML::ColumnExp,
    SQLDML::Table,
    Expression,
    SQLDML::QueryPredicate,
    SQLDML::InExp,
    SQLDML::Predicate,
    SQLDML::LikeExp,
    SQLDML::NotExp,
    SQLDML::BinaryExp,
    QueryStmt,
    SQLDML::QueryStmtCol,
    SQLDML::QueryStmtAllCol,
    ColumnExp,
    Table,
    Statement,
    SQLDML::InsertStmt,
    SQLDML::QueryStmt,
    LocatedElement,
    SQLDML::Expression,
    SQLDML::WhereClause,
    SQLDML::NamedElement,
    SQLDML::SQLRoot,
    SQLDML::ViewStatement,
    SQLDML::Statement,
    SQLDML::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_valueexp_is_not_abstract():
    assert not inspect.isabstract(ValueExp)


def test_valueexp_constructor_exists():
    assert callable(ValueExp.__init__)


def test_valueexp_constructor_args():
    sig = inspect.signature(ValueExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::integervalueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::IntegerValueExp)


def test_sqldml::integervalueexp_constructor_exists():
    assert callable(SQLDML::IntegerValueExp.__init__)


def test_sqldml::integervalueexp_constructor_args():
    sig = inspect.signature(SQLDML::IntegerValueExp.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"

def test_sqldml::integervalueexp_has_aValue():
    assert hasattr(SQLDML::IntegerValueExp, "aValue")
    descriptor = None
    for klass in SQLDML::IntegerValueExp.__mro__:
        if "aValue" in klass.__dict__:
            descriptor = klass.__dict__["aValue"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::stringvalueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::StringValueExp)


def test_sqldml::stringvalueexp_constructor_exists():
    assert callable(SQLDML::StringValueExp.__init__)


def test_sqldml::stringvalueexp_constructor_args():
    sig = inspect.signature(SQLDML::StringValueExp.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"

def test_sqldml::stringvalueexp_has_aValue():
    assert hasattr(SQLDML::StringValueExp, "aValue")
    descriptor = None
    for klass in SQLDML::StringValueExp.__mro__:
        if "aValue" in klass.__dict__:
            descriptor = klass.__dict__["aValue"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_stringvalueexp_is_not_abstract():
    assert not inspect.isabstract(StringValueExp)


def test_stringvalueexp_constructor_exists():
    assert callable(StringValueExp.__init__)


def test_stringvalueexp_constructor_args():
    sig = inspect.signature(StringValueExp.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::listexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::ListExp)


def test_sqldml::listexp_constructor_exists():
    assert callable(SQLDML::ListExp.__init__)


def test_sqldml::listexp_constructor_args():
    sig = inspect.signature(SQLDML::ListExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::functionexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::FunctionExp)


def test_sqldml::functionexp_constructor_exists():
    assert callable(SQLDML::FunctionExp.__init__)


def test_sqldml::functionexp_constructor_args():
    sig = inspect.signature(SQLDML::FunctionExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldml::functionexp_has_name():
    assert hasattr(SQLDML::FunctionExp, "name")
    descriptor = None
    for klass in SQLDML::FunctionExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::valueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::ValueExp)


def test_sqldml::valueexp_constructor_exists():
    assert callable(SQLDML::ValueExp.__init__)


def test_sqldml::valueexp_constructor_args():
    sig = inspect.signature(SQLDML::ValueExp.__init__)
    params = list(sig.parameters.keys())



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::andexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::AndExp)


def test_sqldml::andexp_constructor_exists():
    assert callable(SQLDML::AndExp.__init__)


def test_sqldml::andexp_constructor_args():
    sig = inspect.signature(SQLDML::AndExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::operationexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::OperationExp)


def test_sqldml::operationexp_constructor_exists():
    assert callable(SQLDML::OperationExp.__init__)


def test_sqldml::operationexp_constructor_args():
    sig = inspect.signature(SQLDML::OperationExp.__init__)
    params = list(sig.parameters.keys())
    assert "optName" in params, "Missing parameter 'optName'"

def test_sqldml::operationexp_has_optName():
    assert hasattr(SQLDML::OperationExp, "optName")
    descriptor = None
    for klass in SQLDML::OperationExp.__mro__:
        if "optName" in klass.__dict__:
            descriptor = klass.__dict__["optName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::orexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::OrExp)


def test_sqldml::orexp_constructor_exists():
    assert callable(SQLDML::OrExp.__init__)


def test_sqldml::orexp_constructor_args():
    sig = inspect.signature(SQLDML::OrExp.__init__)
    params = list(sig.parameters.keys())



def test_whereclause_is_not_abstract():
    assert not inspect.isabstract(WhereClause)


def test_whereclause_constructor_exists():
    assert callable(WhereClause.__init__)


def test_whereclause_constructor_args():
    sig = inspect.signature(WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::datatype_is_not_abstract():
    assert not inspect.isabstract(SQLDML::DataType)


def test_sqldml::datatype_constructor_exists():
    assert callable(SQLDML::DataType.__init__)


def test_sqldml::datatype_constructor_args():
    sig = inspect.signature(SQLDML::DataType.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::columnexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::ColumnExp)


def test_sqldml::columnexp_constructor_exists():
    assert callable(SQLDML::ColumnExp.__init__)


def test_sqldml::columnexp_constructor_args():
    sig = inspect.signature(SQLDML::ColumnExp.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sqldml::columnexp_has_alias():
    assert hasattr(SQLDML::ColumnExp, "alias")
    descriptor = None
    for klass in SQLDML::ColumnExp.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::table_is_not_abstract():
    assert not inspect.isabstract(SQLDML::Table)


def test_sqldml::table_constructor_exists():
    assert callable(SQLDML::Table.__init__)


def test_sqldml::table_constructor_args():
    sig = inspect.signature(SQLDML::Table.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sqldml::table_has_alias():
    assert hasattr(SQLDML::Table, "alias")
    descriptor = None
    for klass in SQLDML::Table.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::querypredicate_is_not_abstract():
    assert not inspect.isabstract(SQLDML::QueryPredicate)


def test_sqldml::querypredicate_constructor_exists():
    assert callable(SQLDML::QueryPredicate.__init__)


def test_sqldml::querypredicate_constructor_args():
    sig = inspect.signature(SQLDML::QueryPredicate.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::inexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::InExp)


def test_sqldml::inexp_constructor_exists():
    assert callable(SQLDML::InExp.__init__)


def test_sqldml::inexp_constructor_args():
    sig = inspect.signature(SQLDML::InExp.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_sqldml::inexp_has_columnName():
    assert hasattr(SQLDML::InExp, "columnName")
    descriptor = None
    for klass in SQLDML::InExp.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::predicate_is_not_abstract():
    assert not inspect.isabstract(SQLDML::Predicate)


def test_sqldml::predicate_constructor_exists():
    assert callable(SQLDML::Predicate.__init__)


def test_sqldml::predicate_constructor_args():
    sig = inspect.signature(SQLDML::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::likeexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::LikeExp)


def test_sqldml::likeexp_constructor_exists():
    assert callable(SQLDML::LikeExp.__init__)


def test_sqldml::likeexp_constructor_args():
    sig = inspect.signature(SQLDML::LikeExp.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_sqldml::likeexp_has_columnName():
    assert hasattr(SQLDML::LikeExp, "columnName")
    descriptor = None
    for klass in SQLDML::LikeExp.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::notexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::NotExp)


def test_sqldml::notexp_constructor_exists():
    assert callable(SQLDML::NotExp.__init__)


def test_sqldml::notexp_constructor_args():
    sig = inspect.signature(SQLDML::NotExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_sqldml::notexp_has_opName():
    assert hasattr(SQLDML::NotExp, "opName")
    descriptor = None
    for klass in SQLDML::NotExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::binaryexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML::BinaryExp)


def test_sqldml::binaryexp_constructor_exists():
    assert callable(SQLDML::BinaryExp.__init__)


def test_sqldml::binaryexp_constructor_args():
    sig = inspect.signature(SQLDML::BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_sqldml::binaryexp_has_opName():
    assert hasattr(SQLDML::BinaryExp, "opName")
    descriptor = None
    for klass in SQLDML::BinaryExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_querystmt_is_not_abstract():
    assert not inspect.isabstract(QueryStmt)


def test_querystmt_constructor_exists():
    assert callable(QueryStmt.__init__)


def test_querystmt_constructor_args():
    sig = inspect.signature(QueryStmt.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::querystmtcol_is_not_abstract():
    assert not inspect.isabstract(SQLDML::QueryStmtCol)


def test_sqldml::querystmtcol_constructor_exists():
    assert callable(SQLDML::QueryStmtCol.__init__)


def test_sqldml::querystmtcol_constructor_args():
    sig = inspect.signature(SQLDML::QueryStmtCol.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::querystmtallcol_is_not_abstract():
    assert not inspect.isabstract(SQLDML::QueryStmtAllCol)


def test_sqldml::querystmtallcol_constructor_exists():
    assert callable(SQLDML::QueryStmtAllCol.__init__)


def test_sqldml::querystmtallcol_constructor_args():
    sig = inspect.signature(SQLDML::QueryStmtAllCol.__init__)
    params = list(sig.parameters.keys())



def test_columnexp_is_not_abstract():
    assert not inspect.isabstract(ColumnExp)


def test_columnexp_constructor_exists():
    assert callable(ColumnExp.__init__)


def test_columnexp_constructor_args():
    sig = inspect.signature(ColumnExp.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::insertstmt_is_not_abstract():
    assert not inspect.isabstract(SQLDML::InsertStmt)


def test_sqldml::insertstmt_constructor_exists():
    assert callable(SQLDML::InsertStmt.__init__)


def test_sqldml::insertstmt_constructor_args():
    sig = inspect.signature(SQLDML::InsertStmt.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_sqldml::insertstmt_has_tableName():
    assert hasattr(SQLDML::InsertStmt, "tableName")
    descriptor = None
    for klass in SQLDML::InsertStmt.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::querystmt_is_not_abstract():
    assert not inspect.isabstract(SQLDML::QueryStmt)


def test_sqldml::querystmt_constructor_exists():
    assert callable(SQLDML::QueryStmt.__init__)


def test_sqldml::querystmt_constructor_args():
    sig = inspect.signature(SQLDML::QueryStmt.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::expression_is_not_abstract():
    assert not inspect.isabstract(SQLDML::Expression)


def test_sqldml::expression_constructor_exists():
    assert callable(SQLDML::Expression.__init__)


def test_sqldml::expression_constructor_args():
    sig = inspect.signature(SQLDML::Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::whereclause_is_not_abstract():
    assert not inspect.isabstract(SQLDML::WhereClause)


def test_sqldml::whereclause_constructor_exists():
    assert callable(SQLDML::WhereClause.__init__)


def test_sqldml::whereclause_constructor_args():
    sig = inspect.signature(SQLDML::WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::namedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDML::NamedElement)


def test_sqldml::namedelement_constructor_exists():
    assert callable(SQLDML::NamedElement.__init__)


def test_sqldml::namedelement_constructor_args():
    sig = inspect.signature(SQLDML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldml::namedelement_has_name():
    assert hasattr(SQLDML::NamedElement, "name")
    descriptor = None
    for klass in SQLDML::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::sqlroot_is_not_abstract():
    assert not inspect.isabstract(SQLDML::SQLRoot)


def test_sqldml::sqlroot_constructor_exists():
    assert callable(SQLDML::SQLRoot.__init__)


def test_sqldml::sqlroot_constructor_args():
    sig = inspect.signature(SQLDML::SQLRoot.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::viewstatement_is_not_abstract():
    assert not inspect.isabstract(SQLDML::ViewStatement)


def test_sqldml::viewstatement_constructor_exists():
    assert callable(SQLDML::ViewStatement.__init__)


def test_sqldml::viewstatement_constructor_args():
    sig = inspect.signature(SQLDML::ViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldml::viewstatement_has_name():
    assert hasattr(SQLDML::ViewStatement, "name")
    descriptor = None
    for klass in SQLDML::ViewStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldml::statement_is_not_abstract():
    assert not inspect.isabstract(SQLDML::Statement)


def test_sqldml::statement_constructor_exists():
    assert callable(SQLDML::Statement.__init__)


def test_sqldml::statement_constructor_args():
    sig = inspect.signature(SQLDML::Statement.__init__)
    params = list(sig.parameters.keys())



def test_sqldml::locatedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDML::LocatedElement)


def test_sqldml::locatedelement_constructor_exists():
    assert callable(SQLDML::LocatedElement.__init__)


def test_sqldml::locatedelement_constructor_args():
    sig = inspect.signature(SQLDML::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_sqldml::locatedelement_has_commentsAfter():
    assert hasattr(SQLDML::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in SQLDML::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_sqldml::locatedelement_has_location():
    assert hasattr(SQLDML::LocatedElement, "location")
    descriptor = None
    for klass in SQLDML::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sqldml::locatedelement_has_commentsBefore():
    assert hasattr(SQLDML::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in SQLDML::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
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
ValueExp_strategy = st.builds(
    ValueExp,
)
SQLDML::IntegerValueExp_strategy = st.builds(
    SQLDML::IntegerValueExp,
    aValue=
        safe_text
)
SQLDML::StringValueExp_strategy = st.builds(
    SQLDML::StringValueExp,
    aValue=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
StringValueExp_strategy = st.builds(
    StringValueExp,
)
Predicate_strategy = st.builds(
    Predicate,
)
SQLDML::ListExp_strategy = st.builds(
    SQLDML::ListExp,
)
SQLDML::FunctionExp_strategy = st.builds(
    SQLDML::FunctionExp,
    name=
        safe_text
)
SQLDML::ValueExp_strategy = st.builds(
    SQLDML::ValueExp,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
SQLDML::AndExp_strategy = st.builds(
    SQLDML::AndExp,
)
SQLDML::OperationExp_strategy = st.builds(
    SQLDML::OperationExp,
    optName=
        safe_text
)
SQLDML::OrExp_strategy = st.builds(
    SQLDML::OrExp,
)
WhereClause_strategy = st.builds(
    WhereClause,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SQLDML::DataType_strategy = st.builds(
    SQLDML::DataType,
)
SQLDML::ColumnExp_strategy = st.builds(
    SQLDML::ColumnExp,
    alias=
        safe_text
)
SQLDML::Table_strategy = st.builds(
    SQLDML::Table,
    alias=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
SQLDML::QueryPredicate_strategy = st.builds(
    SQLDML::QueryPredicate,
)
SQLDML::InExp_strategy = st.builds(
    SQLDML::InExp,
    columnName=
        safe_text
)
SQLDML::Predicate_strategy = st.builds(
    SQLDML::Predicate,
)
SQLDML::LikeExp_strategy = st.builds(
    SQLDML::LikeExp,
    columnName=
        safe_text
)
SQLDML::NotExp_strategy = st.builds(
    SQLDML::NotExp,
    opName=
        safe_text
)
SQLDML::BinaryExp_strategy = st.builds(
    SQLDML::BinaryExp,
    opName=
        safe_text
)
QueryStmt_strategy = st.builds(
    QueryStmt,
)
SQLDML::QueryStmtCol_strategy = st.builds(
    SQLDML::QueryStmtCol,
)
SQLDML::QueryStmtAllCol_strategy = st.builds(
    SQLDML::QueryStmtAllCol,
)
ColumnExp_strategy = st.builds(
    ColumnExp,
)
Table_strategy = st.builds(
    Table,
)
Statement_strategy = st.builds(
    Statement,
)
SQLDML::InsertStmt_strategy = st.builds(
    SQLDML::InsertStmt,
    tableName=
        safe_text
)
SQLDML::QueryStmt_strategy = st.builds(
    SQLDML::QueryStmt,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SQLDML::Expression_strategy = st.builds(
    SQLDML::Expression,
)
SQLDML::WhereClause_strategy = st.builds(
    SQLDML::WhereClause,
)
SQLDML::NamedElement_strategy = st.builds(
    SQLDML::NamedElement,
    name=
        safe_text
)
SQLDML::SQLRoot_strategy = st.builds(
    SQLDML::SQLRoot,
)
SQLDML::ViewStatement_strategy = st.builds(
    SQLDML::ViewStatement,
    name=
        safe_text
)
SQLDML::Statement_strategy = st.builds(
    SQLDML::Statement,
)
SQLDML::LocatedElement_strategy = st.builds(
    SQLDML::LocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)

@given(instance=ValueExp_strategy)
@settings(max_examples=50)
def test_valueexp_instantiation(instance):
    assert isinstance(instance, ValueExp)

@given(instance=SQLDML::IntegerValueExp_strategy)
@settings(max_examples=50)
def test_sqldml::integervalueexp_instantiation(instance):
    assert isinstance(instance, SQLDML::IntegerValueExp)

@given(instance=SQLDML::IntegerValueExp_strategy)
def test_sqldml::integervalueexp_aValue_type(instance):
    assert isinstance(instance.aValue, str)


@given(instance=SQLDML::IntegerValueExp_strategy)
def test_sqldml::integervalueexp_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original

@given(instance=SQLDML::StringValueExp_strategy)
@settings(max_examples=50)
def test_sqldml::stringvalueexp_instantiation(instance):
    assert isinstance(instance, SQLDML::StringValueExp)

@given(instance=SQLDML::StringValueExp_strategy)
def test_sqldml::stringvalueexp_aValue_type(instance):
    assert isinstance(instance.aValue, str)


@given(instance=SQLDML::StringValueExp_strategy)
def test_sqldml::stringvalueexp_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=StringValueExp_strategy)
@settings(max_examples=50)
def test_stringvalueexp_instantiation(instance):
    assert isinstance(instance, StringValueExp)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=SQLDML::ListExp_strategy)
@settings(max_examples=50)
def test_sqldml::listexp_instantiation(instance):
    assert isinstance(instance, SQLDML::ListExp)

@given(instance=SQLDML::FunctionExp_strategy)
@settings(max_examples=50)
def test_sqldml::functionexp_instantiation(instance):
    assert isinstance(instance, SQLDML::FunctionExp)

@given(instance=SQLDML::FunctionExp_strategy)
def test_sqldml::functionexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQLDML::FunctionExp_strategy)
def test_sqldml::functionexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDML::ValueExp_strategy)
@settings(max_examples=50)
def test_sqldml::valueexp_instantiation(instance):
    assert isinstance(instance, SQLDML::ValueExp)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=SQLDML::AndExp_strategy)
@settings(max_examples=50)
def test_sqldml::andexp_instantiation(instance):
    assert isinstance(instance, SQLDML::AndExp)

@given(instance=SQLDML::OperationExp_strategy)
@settings(max_examples=50)
def test_sqldml::operationexp_instantiation(instance):
    assert isinstance(instance, SQLDML::OperationExp)

@given(instance=SQLDML::OperationExp_strategy)
def test_sqldml::operationexp_optName_type(instance):
    assert isinstance(instance.optName, str)


@given(instance=SQLDML::OperationExp_strategy)
def test_sqldml::operationexp_optName_setter(instance):
    original = instance.optName
    instance.optName = original
    assert instance.optName == original

@given(instance=SQLDML::OrExp_strategy)
@settings(max_examples=50)
def test_sqldml::orexp_instantiation(instance):
    assert isinstance(instance, SQLDML::OrExp)

@given(instance=WhereClause_strategy)
@settings(max_examples=50)
def test_whereclause_instantiation(instance):
    assert isinstance(instance, WhereClause)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SQLDML::DataType_strategy)
@settings(max_examples=50)
def test_sqldml::datatype_instantiation(instance):
    assert isinstance(instance, SQLDML::DataType)

@given(instance=SQLDML::ColumnExp_strategy)
@settings(max_examples=50)
def test_sqldml::columnexp_instantiation(instance):
    assert isinstance(instance, SQLDML::ColumnExp)

@given(instance=SQLDML::ColumnExp_strategy)
def test_sqldml::columnexp_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=SQLDML::ColumnExp_strategy)
def test_sqldml::columnexp_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=SQLDML::Table_strategy)
@settings(max_examples=50)
def test_sqldml::table_instantiation(instance):
    assert isinstance(instance, SQLDML::Table)

@given(instance=SQLDML::Table_strategy)
def test_sqldml::table_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=SQLDML::Table_strategy)
def test_sqldml::table_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=SQLDML::QueryPredicate_strategy)
@settings(max_examples=50)
def test_sqldml::querypredicate_instantiation(instance):
    assert isinstance(instance, SQLDML::QueryPredicate)

@given(instance=SQLDML::InExp_strategy)
@settings(max_examples=50)
def test_sqldml::inexp_instantiation(instance):
    assert isinstance(instance, SQLDML::InExp)

@given(instance=SQLDML::InExp_strategy)
def test_sqldml::inexp_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=SQLDML::InExp_strategy)
def test_sqldml::inexp_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=SQLDML::Predicate_strategy)
@settings(max_examples=50)
def test_sqldml::predicate_instantiation(instance):
    assert isinstance(instance, SQLDML::Predicate)

@given(instance=SQLDML::LikeExp_strategy)
@settings(max_examples=50)
def test_sqldml::likeexp_instantiation(instance):
    assert isinstance(instance, SQLDML::LikeExp)

@given(instance=SQLDML::LikeExp_strategy)
def test_sqldml::likeexp_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=SQLDML::LikeExp_strategy)
def test_sqldml::likeexp_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=SQLDML::NotExp_strategy)
@settings(max_examples=50)
def test_sqldml::notexp_instantiation(instance):
    assert isinstance(instance, SQLDML::NotExp)

@given(instance=SQLDML::NotExp_strategy)
def test_sqldml::notexp_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=SQLDML::NotExp_strategy)
def test_sqldml::notexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=SQLDML::BinaryExp_strategy)
@settings(max_examples=50)
def test_sqldml::binaryexp_instantiation(instance):
    assert isinstance(instance, SQLDML::BinaryExp)

@given(instance=SQLDML::BinaryExp_strategy)
def test_sqldml::binaryexp_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=SQLDML::BinaryExp_strategy)
def test_sqldml::binaryexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=QueryStmt_strategy)
@settings(max_examples=50)
def test_querystmt_instantiation(instance):
    assert isinstance(instance, QueryStmt)

@given(instance=SQLDML::QueryStmtCol_strategy)
@settings(max_examples=50)
def test_sqldml::querystmtcol_instantiation(instance):
    assert isinstance(instance, SQLDML::QueryStmtCol)

@given(instance=SQLDML::QueryStmtAllCol_strategy)
@settings(max_examples=50)
def test_sqldml::querystmtallcol_instantiation(instance):
    assert isinstance(instance, SQLDML::QueryStmtAllCol)

@given(instance=ColumnExp_strategy)
@settings(max_examples=50)
def test_columnexp_instantiation(instance):
    assert isinstance(instance, ColumnExp)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=SQLDML::InsertStmt_strategy)
@settings(max_examples=50)
def test_sqldml::insertstmt_instantiation(instance):
    assert isinstance(instance, SQLDML::InsertStmt)

@given(instance=SQLDML::InsertStmt_strategy)
def test_sqldml::insertstmt_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=SQLDML::InsertStmt_strategy)
def test_sqldml::insertstmt_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=SQLDML::QueryStmt_strategy)
@settings(max_examples=50)
def test_sqldml::querystmt_instantiation(instance):
    assert isinstance(instance, SQLDML::QueryStmt)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=SQLDML::Expression_strategy)
@settings(max_examples=50)
def test_sqldml::expression_instantiation(instance):
    assert isinstance(instance, SQLDML::Expression)

@given(instance=SQLDML::WhereClause_strategy)
@settings(max_examples=50)
def test_sqldml::whereclause_instantiation(instance):
    assert isinstance(instance, SQLDML::WhereClause)

@given(instance=SQLDML::NamedElement_strategy)
@settings(max_examples=50)
def test_sqldml::namedelement_instantiation(instance):
    assert isinstance(instance, SQLDML::NamedElement)

@given(instance=SQLDML::NamedElement_strategy)
def test_sqldml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQLDML::NamedElement_strategy)
def test_sqldml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDML::SQLRoot_strategy)
@settings(max_examples=50)
def test_sqldml::sqlroot_instantiation(instance):
    assert isinstance(instance, SQLDML::SQLRoot)

@given(instance=SQLDML::ViewStatement_strategy)
@settings(max_examples=50)
def test_sqldml::viewstatement_instantiation(instance):
    assert isinstance(instance, SQLDML::ViewStatement)

@given(instance=SQLDML::ViewStatement_strategy)
def test_sqldml::viewstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQLDML::ViewStatement_strategy)
def test_sqldml::viewstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDML::Statement_strategy)
@settings(max_examples=50)
def test_sqldml::statement_instantiation(instance):
    assert isinstance(instance, SQLDML::Statement)

@given(instance=SQLDML::LocatedElement_strategy)
@settings(max_examples=50)
def test_sqldml::locatedelement_instantiation(instance):
    assert isinstance(instance, SQLDML::LocatedElement)

@given(instance=SQLDML::LocatedElement_strategy)
def test_sqldml::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=SQLDML::LocatedElement_strategy)
def test_sqldml::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=SQLDML::LocatedElement_strategy)
def test_sqldml::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=SQLDML::LocatedElement_strategy)
def test_sqldml::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=SQLDML::LocatedElement_strategy)
def test_sqldml::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=SQLDML::LocatedElement_strategy)
def test_sqldml::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original
