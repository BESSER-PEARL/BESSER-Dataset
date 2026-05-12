import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ValueExp,
    SQLDML_IntegerValueExp,
    SQLDML_StringValueExp,
    DataType,
    StringValueExp,
    Predicate,
    SQLDML_ValueExp,
    SQLDML_FunctionExp,
    SQLDML_ListExp,
    BinaryExp,
    SQLDML_OperationExp,
    SQLDML_AndExp,
    SQLDML_OrExp,
    WhereClause,
    NamedElement,
    SQLDML_ColumnExp,
    SQLDML_DataType,
    SQLDML_Table,
    Expression,
    SQLDML_InExp,
    SQLDML_LikeExp,
    SQLDML_BinaryExp,
    SQLDML_NotExp,
    SQLDML_Predicate,
    SQLDML_QueryPredicate,
    QueryStmt,
    SQLDML_QueryStmtCol,
    SQLDML_QueryStmtAllCol,
    ColumnExp,
    Table,
    Statement,
    SQLDML_InsertStmt,
    SQLDML_QueryStmt,
    LocatedElement,
    SQLDML_NamedElement,
    SQLDML_Expression,
    SQLDML_WhereClause,
    SQLDML_SQLRoot,
    SQLDML_ViewStatement,
    SQLDML_Statement,
    SQLDML_LocatedElement,
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



def test_sqldml_integervalueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_IntegerValueExp)


def test_sqldml_integervalueexp_constructor_exists():
    assert callable(SQLDML_IntegerValueExp.__init__)


def test_sqldml_integervalueexp_constructor_args():
    sig = inspect.signature(SQLDML_IntegerValueExp.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"

def test_sqldml_integervalueexp_has_aValue():
    assert hasattr(SQLDML_IntegerValueExp, "aValue")
    descriptor = None
    for klass in SQLDML_IntegerValueExp.__mro__:
        if "aValue" in klass.__dict__:
            descriptor = klass.__dict__["aValue"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_stringvalueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_StringValueExp)


def test_sqldml_stringvalueexp_constructor_exists():
    assert callable(SQLDML_StringValueExp.__init__)


def test_sqldml_stringvalueexp_constructor_args():
    sig = inspect.signature(SQLDML_StringValueExp.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"

def test_sqldml_stringvalueexp_has_aValue():
    assert hasattr(SQLDML_StringValueExp, "aValue")
    descriptor = None
    for klass in SQLDML_StringValueExp.__mro__:
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



def test_sqldml_valueexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ValueExp)


def test_sqldml_valueexp_constructor_exists():
    assert callable(SQLDML_ValueExp.__init__)


def test_sqldml_valueexp_constructor_args():
    sig = inspect.signature(SQLDML_ValueExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_functionexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_FunctionExp)


def test_sqldml_functionexp_constructor_exists():
    assert callable(SQLDML_FunctionExp.__init__)


def test_sqldml_functionexp_constructor_args():
    sig = inspect.signature(SQLDML_FunctionExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldml_functionexp_has_name():
    assert hasattr(SQLDML_FunctionExp, "name")
    descriptor = None
    for klass in SQLDML_FunctionExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_listexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ListExp)


def test_sqldml_listexp_constructor_exists():
    assert callable(SQLDML_ListExp.__init__)


def test_sqldml_listexp_constructor_args():
    sig = inspect.signature(SQLDML_ListExp.__init__)
    params = list(sig.parameters.keys())



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_operationexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_OperationExp)


def test_sqldml_operationexp_constructor_exists():
    assert callable(SQLDML_OperationExp.__init__)


def test_sqldml_operationexp_constructor_args():
    sig = inspect.signature(SQLDML_OperationExp.__init__)
    params = list(sig.parameters.keys())
    assert "optName" in params, "Missing parameter 'optName'"

def test_sqldml_operationexp_has_optName():
    assert hasattr(SQLDML_OperationExp, "optName")
    descriptor = None
    for klass in SQLDML_OperationExp.__mro__:
        if "optName" in klass.__dict__:
            descriptor = klass.__dict__["optName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_andexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_AndExp)


def test_sqldml_andexp_constructor_exists():
    assert callable(SQLDML_AndExp.__init__)


def test_sqldml_andexp_constructor_args():
    sig = inspect.signature(SQLDML_AndExp.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_orexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_OrExp)


def test_sqldml_orexp_constructor_exists():
    assert callable(SQLDML_OrExp.__init__)


def test_sqldml_orexp_constructor_args():
    sig = inspect.signature(SQLDML_OrExp.__init__)
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



def test_sqldml_columnexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ColumnExp)


def test_sqldml_columnexp_constructor_exists():
    assert callable(SQLDML_ColumnExp.__init__)


def test_sqldml_columnexp_constructor_args():
    sig = inspect.signature(SQLDML_ColumnExp.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sqldml_columnexp_has_alias():
    assert hasattr(SQLDML_ColumnExp, "alias")
    descriptor = None
    for klass in SQLDML_ColumnExp.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_datatype_is_not_abstract():
    assert not inspect.isabstract(SQLDML_DataType)


def test_sqldml_datatype_constructor_exists():
    assert callable(SQLDML_DataType.__init__)


def test_sqldml_datatype_constructor_args():
    sig = inspect.signature(SQLDML_DataType.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_table_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Table)


def test_sqldml_table_constructor_exists():
    assert callable(SQLDML_Table.__init__)


def test_sqldml_table_constructor_args():
    sig = inspect.signature(SQLDML_Table.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sqldml_table_has_alias():
    assert hasattr(SQLDML_Table, "alias")
    descriptor = None
    for klass in SQLDML_Table.__mro__:
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



def test_sqldml_inexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_InExp)


def test_sqldml_inexp_constructor_exists():
    assert callable(SQLDML_InExp.__init__)


def test_sqldml_inexp_constructor_args():
    sig = inspect.signature(SQLDML_InExp.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_sqldml_inexp_has_columnName():
    assert hasattr(SQLDML_InExp, "columnName")
    descriptor = None
    for klass in SQLDML_InExp.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_likeexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_LikeExp)


def test_sqldml_likeexp_constructor_exists():
    assert callable(SQLDML_LikeExp.__init__)


def test_sqldml_likeexp_constructor_args():
    sig = inspect.signature(SQLDML_LikeExp.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_sqldml_likeexp_has_columnName():
    assert hasattr(SQLDML_LikeExp, "columnName")
    descriptor = None
    for klass in SQLDML_LikeExp.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_binaryexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_BinaryExp)


def test_sqldml_binaryexp_constructor_exists():
    assert callable(SQLDML_BinaryExp.__init__)


def test_sqldml_binaryexp_constructor_args():
    sig = inspect.signature(SQLDML_BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_sqldml_binaryexp_has_opName():
    assert hasattr(SQLDML_BinaryExp, "opName")
    descriptor = None
    for klass in SQLDML_BinaryExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_notexp_is_not_abstract():
    assert not inspect.isabstract(SQLDML_NotExp)


def test_sqldml_notexp_constructor_exists():
    assert callable(SQLDML_NotExp.__init__)


def test_sqldml_notexp_constructor_args():
    sig = inspect.signature(SQLDML_NotExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_sqldml_notexp_has_opName():
    assert hasattr(SQLDML_NotExp, "opName")
    descriptor = None
    for klass in SQLDML_NotExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_predicate_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Predicate)


def test_sqldml_predicate_constructor_exists():
    assert callable(SQLDML_Predicate.__init__)


def test_sqldml_predicate_constructor_args():
    sig = inspect.signature(SQLDML_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_querypredicate_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryPredicate)


def test_sqldml_querypredicate_constructor_exists():
    assert callable(SQLDML_QueryPredicate.__init__)


def test_sqldml_querypredicate_constructor_args():
    sig = inspect.signature(SQLDML_QueryPredicate.__init__)
    params = list(sig.parameters.keys())



def test_querystmt_is_not_abstract():
    assert not inspect.isabstract(QueryStmt)


def test_querystmt_constructor_exists():
    assert callable(QueryStmt.__init__)


def test_querystmt_constructor_args():
    sig = inspect.signature(QueryStmt.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_querystmtcol_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryStmtCol)


def test_sqldml_querystmtcol_constructor_exists():
    assert callable(SQLDML_QueryStmtCol.__init__)


def test_sqldml_querystmtcol_constructor_args():
    sig = inspect.signature(SQLDML_QueryStmtCol.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_querystmtallcol_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryStmtAllCol)


def test_sqldml_querystmtallcol_constructor_exists():
    assert callable(SQLDML_QueryStmtAllCol.__init__)


def test_sqldml_querystmtallcol_constructor_args():
    sig = inspect.signature(SQLDML_QueryStmtAllCol.__init__)
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



def test_sqldml_insertstmt_is_not_abstract():
    assert not inspect.isabstract(SQLDML_InsertStmt)


def test_sqldml_insertstmt_constructor_exists():
    assert callable(SQLDML_InsertStmt.__init__)


def test_sqldml_insertstmt_constructor_args():
    sig = inspect.signature(SQLDML_InsertStmt.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_sqldml_insertstmt_has_tableName():
    assert hasattr(SQLDML_InsertStmt, "tableName")
    descriptor = None
    for klass in SQLDML_InsertStmt.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_querystmt_is_not_abstract():
    assert not inspect.isabstract(SQLDML_QueryStmt)


def test_sqldml_querystmt_constructor_exists():
    assert callable(SQLDML_QueryStmt.__init__)


def test_sqldml_querystmt_constructor_args():
    sig = inspect.signature(SQLDML_QueryStmt.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_namedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_NamedElement)


def test_sqldml_namedelement_constructor_exists():
    assert callable(SQLDML_NamedElement.__init__)


def test_sqldml_namedelement_constructor_args():
    sig = inspect.signature(SQLDML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldml_namedelement_has_name():
    assert hasattr(SQLDML_NamedElement, "name")
    descriptor = None
    for klass in SQLDML_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_expression_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Expression)


def test_sqldml_expression_constructor_exists():
    assert callable(SQLDML_Expression.__init__)


def test_sqldml_expression_constructor_args():
    sig = inspect.signature(SQLDML_Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_whereclause_is_not_abstract():
    assert not inspect.isabstract(SQLDML_WhereClause)


def test_sqldml_whereclause_constructor_exists():
    assert callable(SQLDML_WhereClause.__init__)


def test_sqldml_whereclause_constructor_args():
    sig = inspect.signature(SQLDML_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_sqlroot_is_not_abstract():
    assert not inspect.isabstract(SQLDML_SQLRoot)


def test_sqldml_sqlroot_constructor_exists():
    assert callable(SQLDML_SQLRoot.__init__)


def test_sqldml_sqlroot_constructor_args():
    sig = inspect.signature(SQLDML_SQLRoot.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_viewstatement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_ViewStatement)


def test_sqldml_viewstatement_constructor_exists():
    assert callable(SQLDML_ViewStatement.__init__)


def test_sqldml_viewstatement_constructor_args():
    sig = inspect.signature(SQLDML_ViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldml_viewstatement_has_name():
    assert hasattr(SQLDML_ViewStatement, "name")
    descriptor = None
    for klass in SQLDML_ViewStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldml_statement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_Statement)


def test_sqldml_statement_constructor_exists():
    assert callable(SQLDML_Statement.__init__)


def test_sqldml_statement_constructor_args():
    sig = inspect.signature(SQLDML_Statement.__init__)
    params = list(sig.parameters.keys())



def test_sqldml_locatedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDML_LocatedElement)


def test_sqldml_locatedelement_constructor_exists():
    assert callable(SQLDML_LocatedElement.__init__)


def test_sqldml_locatedelement_constructor_args():
    sig = inspect.signature(SQLDML_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_sqldml_locatedelement_has_commentsAfter():
    assert hasattr(SQLDML_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in SQLDML_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_sqldml_locatedelement_has_commentsBefore():
    assert hasattr(SQLDML_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in SQLDML_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_sqldml_locatedelement_has_location():
    assert hasattr(SQLDML_LocatedElement, "location")
    descriptor = None
    for klass in SQLDML_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
SQLDML_IntegerValueExp_strategy = st.builds(
    SQLDML_IntegerValueExp,
    aValue=
        safe_text
)
SQLDML_StringValueExp_strategy = st.builds(
    SQLDML_StringValueExp,
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
SQLDML_ValueExp_strategy = st.builds(
    SQLDML_ValueExp,
)
SQLDML_FunctionExp_strategy = st.builds(
    SQLDML_FunctionExp,
    name=
        safe_text
)
SQLDML_ListExp_strategy = st.builds(
    SQLDML_ListExp,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
SQLDML_OperationExp_strategy = st.builds(
    SQLDML_OperationExp,
    optName=
        safe_text
)
SQLDML_AndExp_strategy = st.builds(
    SQLDML_AndExp,
)
SQLDML_OrExp_strategy = st.builds(
    SQLDML_OrExp,
)
WhereClause_strategy = st.builds(
    WhereClause,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SQLDML_ColumnExp_strategy = st.builds(
    SQLDML_ColumnExp,
    alias=
        safe_text
)
SQLDML_DataType_strategy = st.builds(
    SQLDML_DataType,
)
SQLDML_Table_strategy = st.builds(
    SQLDML_Table,
    alias=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
SQLDML_InExp_strategy = st.builds(
    SQLDML_InExp,
    columnName=
        safe_text
)
SQLDML_LikeExp_strategy = st.builds(
    SQLDML_LikeExp,
    columnName=
        safe_text
)
SQLDML_BinaryExp_strategy = st.builds(
    SQLDML_BinaryExp,
    opName=
        safe_text
)
SQLDML_NotExp_strategy = st.builds(
    SQLDML_NotExp,
    opName=
        safe_text
)
SQLDML_Predicate_strategy = st.builds(
    SQLDML_Predicate,
)
SQLDML_QueryPredicate_strategy = st.builds(
    SQLDML_QueryPredicate,
)
QueryStmt_strategy = st.builds(
    QueryStmt,
)
SQLDML_QueryStmtCol_strategy = st.builds(
    SQLDML_QueryStmtCol,
)
SQLDML_QueryStmtAllCol_strategy = st.builds(
    SQLDML_QueryStmtAllCol,
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
SQLDML_InsertStmt_strategy = st.builds(
    SQLDML_InsertStmt,
    tableName=
        safe_text
)
SQLDML_QueryStmt_strategy = st.builds(
    SQLDML_QueryStmt,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SQLDML_NamedElement_strategy = st.builds(
    SQLDML_NamedElement,
    name=
        safe_text
)
SQLDML_Expression_strategy = st.builds(
    SQLDML_Expression,
)
SQLDML_WhereClause_strategy = st.builds(
    SQLDML_WhereClause,
)
SQLDML_SQLRoot_strategy = st.builds(
    SQLDML_SQLRoot,
)
SQLDML_ViewStatement_strategy = st.builds(
    SQLDML_ViewStatement,
    name=
        safe_text
)
SQLDML_Statement_strategy = st.builds(
    SQLDML_Statement,
)
SQLDML_LocatedElement_strategy = st.builds(
    SQLDML_LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)

@given(instance=ValueExp_strategy)
@settings(max_examples=50)
def test_valueexp_instantiation(instance):
    assert isinstance(instance, ValueExp)

@given(instance=SQLDML_IntegerValueExp_strategy)
@settings(max_examples=50)
def test_sqldml_integervalueexp_instantiation(instance):
    assert isinstance(instance, SQLDML_IntegerValueExp)



@given(instance=SQLDML_IntegerValueExp_strategy)
def test_sqldml_integervalueexp_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original

@given(instance=SQLDML_StringValueExp_strategy)
@settings(max_examples=50)
def test_sqldml_stringvalueexp_instantiation(instance):
    assert isinstance(instance, SQLDML_StringValueExp)



@given(instance=SQLDML_StringValueExp_strategy)
def test_sqldml_stringvalueexp_aValue_setter(instance):
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

@given(instance=SQLDML_ValueExp_strategy)
@settings(max_examples=50)
def test_sqldml_valueexp_instantiation(instance):
    assert isinstance(instance, SQLDML_ValueExp)

@given(instance=SQLDML_FunctionExp_strategy)
@settings(max_examples=50)
def test_sqldml_functionexp_instantiation(instance):
    assert isinstance(instance, SQLDML_FunctionExp)



@given(instance=SQLDML_FunctionExp_strategy)
def test_sqldml_functionexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDML_ListExp_strategy)
@settings(max_examples=50)
def test_sqldml_listexp_instantiation(instance):
    assert isinstance(instance, SQLDML_ListExp)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=SQLDML_OperationExp_strategy)
@settings(max_examples=50)
def test_sqldml_operationexp_instantiation(instance):
    assert isinstance(instance, SQLDML_OperationExp)



@given(instance=SQLDML_OperationExp_strategy)
def test_sqldml_operationexp_optName_setter(instance):
    original = instance.optName
    instance.optName = original
    assert instance.optName == original

@given(instance=SQLDML_AndExp_strategy)
@settings(max_examples=50)
def test_sqldml_andexp_instantiation(instance):
    assert isinstance(instance, SQLDML_AndExp)

@given(instance=SQLDML_OrExp_strategy)
@settings(max_examples=50)
def test_sqldml_orexp_instantiation(instance):
    assert isinstance(instance, SQLDML_OrExp)

@given(instance=WhereClause_strategy)
@settings(max_examples=50)
def test_whereclause_instantiation(instance):
    assert isinstance(instance, WhereClause)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SQLDML_ColumnExp_strategy)
@settings(max_examples=50)
def test_sqldml_columnexp_instantiation(instance):
    assert isinstance(instance, SQLDML_ColumnExp)



@given(instance=SQLDML_ColumnExp_strategy)
def test_sqldml_columnexp_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=SQLDML_DataType_strategy)
@settings(max_examples=50)
def test_sqldml_datatype_instantiation(instance):
    assert isinstance(instance, SQLDML_DataType)

@given(instance=SQLDML_Table_strategy)
@settings(max_examples=50)
def test_sqldml_table_instantiation(instance):
    assert isinstance(instance, SQLDML_Table)



@given(instance=SQLDML_Table_strategy)
def test_sqldml_table_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=SQLDML_InExp_strategy)
@settings(max_examples=50)
def test_sqldml_inexp_instantiation(instance):
    assert isinstance(instance, SQLDML_InExp)



@given(instance=SQLDML_InExp_strategy)
def test_sqldml_inexp_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=SQLDML_LikeExp_strategy)
@settings(max_examples=50)
def test_sqldml_likeexp_instantiation(instance):
    assert isinstance(instance, SQLDML_LikeExp)



@given(instance=SQLDML_LikeExp_strategy)
def test_sqldml_likeexp_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=SQLDML_BinaryExp_strategy)
@settings(max_examples=50)
def test_sqldml_binaryexp_instantiation(instance):
    assert isinstance(instance, SQLDML_BinaryExp)



@given(instance=SQLDML_BinaryExp_strategy)
def test_sqldml_binaryexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=SQLDML_NotExp_strategy)
@settings(max_examples=50)
def test_sqldml_notexp_instantiation(instance):
    assert isinstance(instance, SQLDML_NotExp)



@given(instance=SQLDML_NotExp_strategy)
def test_sqldml_notexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=SQLDML_Predicate_strategy)
@settings(max_examples=50)
def test_sqldml_predicate_instantiation(instance):
    assert isinstance(instance, SQLDML_Predicate)

@given(instance=SQLDML_QueryPredicate_strategy)
@settings(max_examples=50)
def test_sqldml_querypredicate_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryPredicate)

@given(instance=QueryStmt_strategy)
@settings(max_examples=50)
def test_querystmt_instantiation(instance):
    assert isinstance(instance, QueryStmt)

@given(instance=SQLDML_QueryStmtCol_strategy)
@settings(max_examples=50)
def test_sqldml_querystmtcol_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryStmtCol)

@given(instance=SQLDML_QueryStmtAllCol_strategy)
@settings(max_examples=50)
def test_sqldml_querystmtallcol_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryStmtAllCol)

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

@given(instance=SQLDML_InsertStmt_strategy)
@settings(max_examples=50)
def test_sqldml_insertstmt_instantiation(instance):
    assert isinstance(instance, SQLDML_InsertStmt)



@given(instance=SQLDML_InsertStmt_strategy)
def test_sqldml_insertstmt_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=SQLDML_QueryStmt_strategy)
@settings(max_examples=50)
def test_sqldml_querystmt_instantiation(instance):
    assert isinstance(instance, SQLDML_QueryStmt)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=SQLDML_NamedElement_strategy)
@settings(max_examples=50)
def test_sqldml_namedelement_instantiation(instance):
    assert isinstance(instance, SQLDML_NamedElement)



@given(instance=SQLDML_NamedElement_strategy)
def test_sqldml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDML_Expression_strategy)
@settings(max_examples=50)
def test_sqldml_expression_instantiation(instance):
    assert isinstance(instance, SQLDML_Expression)

@given(instance=SQLDML_WhereClause_strategy)
@settings(max_examples=50)
def test_sqldml_whereclause_instantiation(instance):
    assert isinstance(instance, SQLDML_WhereClause)

@given(instance=SQLDML_SQLRoot_strategy)
@settings(max_examples=50)
def test_sqldml_sqlroot_instantiation(instance):
    assert isinstance(instance, SQLDML_SQLRoot)

@given(instance=SQLDML_ViewStatement_strategy)
@settings(max_examples=50)
def test_sqldml_viewstatement_instantiation(instance):
    assert isinstance(instance, SQLDML_ViewStatement)



@given(instance=SQLDML_ViewStatement_strategy)
def test_sqldml_viewstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDML_Statement_strategy)
@settings(max_examples=50)
def test_sqldml_statement_instantiation(instance):
    assert isinstance(instance, SQLDML_Statement)

@given(instance=SQLDML_LocatedElement_strategy)
@settings(max_examples=50)
def test_sqldml_locatedelement_instantiation(instance):
    assert isinstance(instance, SQLDML_LocatedElement)



@given(instance=SQLDML_LocatedElement_strategy)
def test_sqldml_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=SQLDML_LocatedElement_strategy)
def test_sqldml_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=SQLDML_LocatedElement_strategy)
def test_sqldml_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
