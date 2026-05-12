import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TriggerAction,
    sqls_TriggerUpdate,
    sqls_TriggerDelete,
    sqls_TriggerInsert,
    Type,
    sqls_TypeDef,
    sqls_Enum,
    sqls_TriggerAction,
    sqls_UpdateColumnExpression,
    sqls_TableRef,
    sqls_Function,
    SqlExpr,
    sqls_SqlNumberLiteral,
    sqls_ColumnRef,
    sqls_SqlParam,
    sqls_SqlPlaceholder,
    sqls_SqlBinaryExpr,
    sqls_NewColumn,
    sqls_OldColumn,
    sqls_SqlNested,
    sqls_SqlStringLiteral,
    sqls_SqlFunction,
    sqls_SelectList,
    sqls_ResultColumn,
    sqls_OrderingTerm,
    sqls_SqlSentence,
    SqlSentence,
    sqls_Update,
    sqls_Insert,
    sqls_Delete,
    sqls_DeleteTable,
    sqls_InsertStatement,
    sqls_Get,
    sqls_SqlMethodRef,
    sqls_Select,
    TableConstraint,
    sqls_UniqueTableConstraint,
    sqls_TableConstraint,
    sqls_SqlExpr,
    sqls_SqlType,
    sqls_EnumElement,
    sqls_SqlMethod,
    sqls_Trigger,
    sqls_Column,
    sqls_Table,
    sqls_Type,
    sqls_Tag,
    sqls_Import,
    sqls_SqlLibrary,
    TriggerTime,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_triggeraction_is_not_abstract():
    assert not inspect.isabstract(TriggerAction)


def test_triggeraction_constructor_exists():
    assert callable(TriggerAction.__init__)


def test_triggeraction_constructor_args():
    sig = inspect.signature(TriggerAction.__init__)
    params = list(sig.parameters.keys())



def test_sqls_triggerupdate_is_not_abstract():
    assert not inspect.isabstract(sqls_TriggerUpdate)


def test_sqls_triggerupdate_constructor_exists():
    assert callable(sqls_TriggerUpdate.__init__)


def test_sqls_triggerupdate_constructor_args():
    sig = inspect.signature(sqls_TriggerUpdate.__init__)
    params = list(sig.parameters.keys())



def test_sqls_triggerdelete_is_not_abstract():
    assert not inspect.isabstract(sqls_TriggerDelete)


def test_sqls_triggerdelete_constructor_exists():
    assert callable(sqls_TriggerDelete.__init__)


def test_sqls_triggerdelete_constructor_args():
    sig = inspect.signature(sqls_TriggerDelete.__init__)
    params = list(sig.parameters.keys())



def test_sqls_triggerinsert_is_not_abstract():
    assert not inspect.isabstract(sqls_TriggerInsert)


def test_sqls_triggerinsert_constructor_exists():
    assert callable(sqls_TriggerInsert.__init__)


def test_sqls_triggerinsert_constructor_args():
    sig = inspect.signature(sqls_TriggerInsert.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_sqls_typedef_is_not_abstract():
    assert not inspect.isabstract(sqls_TypeDef)


def test_sqls_typedef_constructor_exists():
    assert callable(sqls_TypeDef.__init__)


def test_sqls_typedef_constructor_args():
    sig = inspect.signature(sqls_TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_sqls_enum_is_not_abstract():
    assert not inspect.isabstract(sqls_Enum)


def test_sqls_enum_constructor_exists():
    assert callable(sqls_Enum.__init__)


def test_sqls_enum_constructor_args():
    sig = inspect.signature(sqls_Enum.__init__)
    params = list(sig.parameters.keys())



def test_sqls_triggeraction_is_not_abstract():
    assert not inspect.isabstract(sqls_TriggerAction)


def test_sqls_triggeraction_constructor_exists():
    assert callable(sqls_TriggerAction.__init__)


def test_sqls_triggeraction_constructor_args():
    sig = inspect.signature(sqls_TriggerAction.__init__)
    params = list(sig.parameters.keys())



def test_sqls_updatecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sqls_UpdateColumnExpression)


def test_sqls_updatecolumnexpression_constructor_exists():
    assert callable(sqls_UpdateColumnExpression.__init__)


def test_sqls_updatecolumnexpression_constructor_args():
    sig = inspect.signature(sqls_UpdateColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqls_tableref_is_not_abstract():
    assert not inspect.isabstract(sqls_TableRef)


def test_sqls_tableref_constructor_exists():
    assert callable(sqls_TableRef.__init__)


def test_sqls_tableref_constructor_args():
    sig = inspect.signature(sqls_TableRef.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sqls_tableref_has_alias():
    assert hasattr(sqls_TableRef, "alias")
    descriptor = None
    for klass in sqls_TableRef.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sqls_function_is_not_abstract():
    assert not inspect.isabstract(sqls_Function)


def test_sqls_function_constructor_exists():
    assert callable(sqls_Function.__init__)


def test_sqls_function_constructor_args():
    sig = inspect.signature(sqls_Function.__init__)
    params = list(sig.parameters.keys())



def test_sqlexpr_is_not_abstract():
    assert not inspect.isabstract(SqlExpr)


def test_sqlexpr_constructor_exists():
    assert callable(SqlExpr.__init__)


def test_sqlexpr_constructor_args():
    sig = inspect.signature(SqlExpr.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlnumberliteral_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlNumberLiteral)


def test_sqls_sqlnumberliteral_constructor_exists():
    assert callable(sqls_SqlNumberLiteral.__init__)


def test_sqls_sqlnumberliteral_constructor_args():
    sig = inspect.signature(sqls_SqlNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqls_sqlnumberliteral_has_value():
    assert hasattr(sqls_SqlNumberLiteral, "value")
    descriptor = None
    for klass in sqls_SqlNumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqls_columnref_is_not_abstract():
    assert not inspect.isabstract(sqls_ColumnRef)


def test_sqls_columnref_constructor_exists():
    assert callable(sqls_ColumnRef.__init__)


def test_sqls_columnref_constructor_args():
    sig = inspect.signature(sqls_ColumnRef.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlparam_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlParam)


def test_sqls_sqlparam_constructor_exists():
    assert callable(sqls_SqlParam.__init__)


def test_sqls_sqlparam_constructor_args():
    sig = inspect.signature(sqls_SqlParam.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_sqlparam_has_name():
    assert hasattr(sqls_SqlParam, "name")
    descriptor = None
    for klass in sqls_SqlParam.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_sqlplaceholder_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlPlaceholder)


def test_sqls_sqlplaceholder_constructor_exists():
    assert callable(sqls_SqlPlaceholder.__init__)


def test_sqls_sqlplaceholder_constructor_args():
    sig = inspect.signature(sqls_SqlPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlbinaryexpr_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlBinaryExpr)


def test_sqls_sqlbinaryexpr_constructor_exists():
    assert callable(sqls_SqlBinaryExpr.__init__)


def test_sqls_sqlbinaryexpr_constructor_args():
    sig = inspect.signature(sqls_SqlBinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqls_sqlbinaryexpr_has_op():
    assert hasattr(sqls_SqlBinaryExpr, "op")
    descriptor = None
    for klass in sqls_SqlBinaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqls_newcolumn_is_not_abstract():
    assert not inspect.isabstract(sqls_NewColumn)


def test_sqls_newcolumn_constructor_exists():
    assert callable(sqls_NewColumn.__init__)


def test_sqls_newcolumn_constructor_args():
    sig = inspect.signature(sqls_NewColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqls_oldcolumn_is_not_abstract():
    assert not inspect.isabstract(sqls_OldColumn)


def test_sqls_oldcolumn_constructor_exists():
    assert callable(sqls_OldColumn.__init__)


def test_sqls_oldcolumn_constructor_args():
    sig = inspect.signature(sqls_OldColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlnested_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlNested)


def test_sqls_sqlnested_constructor_exists():
    assert callable(sqls_SqlNested.__init__)


def test_sqls_sqlnested_constructor_args():
    sig = inspect.signature(sqls_SqlNested.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlstringliteral_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlStringLiteral)


def test_sqls_sqlstringliteral_constructor_exists():
    assert callable(sqls_SqlStringLiteral.__init__)


def test_sqls_sqlstringliteral_constructor_args():
    sig = inspect.signature(sqls_SqlStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqls_sqlstringliteral_has_value():
    assert hasattr(sqls_SqlStringLiteral, "value")
    descriptor = None
    for klass in sqls_SqlStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqls_sqlfunction_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlFunction)


def test_sqls_sqlfunction_constructor_exists():
    assert callable(sqls_SqlFunction.__init__)


def test_sqls_sqlfunction_constructor_args():
    sig = inspect.signature(sqls_SqlFunction.__init__)
    params = list(sig.parameters.keys())



def test_sqls_selectlist_is_not_abstract():
    assert not inspect.isabstract(sqls_SelectList)


def test_sqls_selectlist_constructor_exists():
    assert callable(sqls_SelectList.__init__)


def test_sqls_selectlist_constructor_args():
    sig = inspect.signature(sqls_SelectList.__init__)
    params = list(sig.parameters.keys())



def test_sqls_resultcolumn_is_not_abstract():
    assert not inspect.isabstract(sqls_ResultColumn)


def test_sqls_resultcolumn_constructor_exists():
    assert callable(sqls_ResultColumn.__init__)


def test_sqls_resultcolumn_constructor_args():
    sig = inspect.signature(sqls_ResultColumn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_resultcolumn_has_name():
    assert hasattr(sqls_ResultColumn, "name")
    descriptor = None
    for klass in sqls_ResultColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_orderingterm_is_not_abstract():
    assert not inspect.isabstract(sqls_OrderingTerm)


def test_sqls_orderingterm_constructor_exists():
    assert callable(sqls_OrderingTerm.__init__)


def test_sqls_orderingterm_constructor_args():
    sig = inspect.signature(sqls_OrderingTerm.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "asc" in params, "Missing parameter 'asc'"

def test_sqls_orderingterm_has_desc():
    assert hasattr(sqls_OrderingTerm, "desc")
    descriptor = None
    for klass in sqls_OrderingTerm.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_sqls_orderingterm_has_asc():
    assert hasattr(sqls_OrderingTerm, "asc")
    descriptor = None
    for klass in sqls_OrderingTerm.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)



def test_sqls_sqlsentence_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlSentence)


def test_sqls_sqlsentence_constructor_exists():
    assert callable(sqls_SqlSentence.__init__)


def test_sqls_sqlsentence_constructor_args():
    sig = inspect.signature(sqls_SqlSentence.__init__)
    params = list(sig.parameters.keys())



def test_sqlsentence_is_not_abstract():
    assert not inspect.isabstract(SqlSentence)


def test_sqlsentence_constructor_exists():
    assert callable(SqlSentence.__init__)


def test_sqlsentence_constructor_args():
    sig = inspect.signature(SqlSentence.__init__)
    params = list(sig.parameters.keys())



def test_sqls_update_is_not_abstract():
    assert not inspect.isabstract(sqls_Update)


def test_sqls_update_constructor_exists():
    assert callable(sqls_Update.__init__)


def test_sqls_update_constructor_args():
    sig = inspect.signature(sqls_Update.__init__)
    params = list(sig.parameters.keys())



def test_sqls_insert_is_not_abstract():
    assert not inspect.isabstract(sqls_Insert)


def test_sqls_insert_constructor_exists():
    assert callable(sqls_Insert.__init__)


def test_sqls_insert_constructor_args():
    sig = inspect.signature(sqls_Insert.__init__)
    params = list(sig.parameters.keys())



def test_sqls_delete_is_not_abstract():
    assert not inspect.isabstract(sqls_Delete)


def test_sqls_delete_constructor_exists():
    assert callable(sqls_Delete.__init__)


def test_sqls_delete_constructor_args():
    sig = inspect.signature(sqls_Delete.__init__)
    params = list(sig.parameters.keys())



def test_sqls_deletetable_is_not_abstract():
    assert not inspect.isabstract(sqls_DeleteTable)


def test_sqls_deletetable_constructor_exists():
    assert callable(sqls_DeleteTable.__init__)


def test_sqls_deletetable_constructor_args():
    sig = inspect.signature(sqls_DeleteTable.__init__)
    params = list(sig.parameters.keys())



def test_sqls_insertstatement_is_not_abstract():
    assert not inspect.isabstract(sqls_InsertStatement)


def test_sqls_insertstatement_constructor_exists():
    assert callable(sqls_InsertStatement.__init__)


def test_sqls_insertstatement_constructor_args():
    sig = inspect.signature(sqls_InsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqls_get_is_not_abstract():
    assert not inspect.isabstract(sqls_Get)


def test_sqls_get_constructor_exists():
    assert callable(sqls_Get.__init__)


def test_sqls_get_constructor_args():
    sig = inspect.signature(sqls_Get.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlmethodref_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlMethodRef)


def test_sqls_sqlmethodref_constructor_exists():
    assert callable(sqls_SqlMethodRef.__init__)


def test_sqls_sqlmethodref_constructor_args():
    sig = inspect.signature(sqls_SqlMethodRef.__init__)
    params = list(sig.parameters.keys())



def test_sqls_select_is_not_abstract():
    assert not inspect.isabstract(sqls_Select)


def test_sqls_select_constructor_exists():
    assert callable(sqls_Select.__init__)


def test_sqls_select_constructor_args():
    sig = inspect.signature(sqls_Select.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_sqls_select_has_all():
    assert hasattr(sqls_Select, "all")
    descriptor = None
    for klass in sqls_Select.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqls_uniquetableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqls_UniqueTableConstraint)


def test_sqls_uniquetableconstraint_constructor_exists():
    assert callable(sqls_UniqueTableConstraint.__init__)


def test_sqls_uniquetableconstraint_constructor_args():
    sig = inspect.signature(sqls_UniqueTableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_uniquetableconstraint_has_name():
    assert hasattr(sqls_UniqueTableConstraint, "name")
    descriptor = None
    for klass in sqls_UniqueTableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqls_TableConstraint)


def test_sqls_tableconstraint_constructor_exists():
    assert callable(sqls_TableConstraint.__init__)


def test_sqls_tableconstraint_constructor_args():
    sig = inspect.signature(sqls_TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqlexpr_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlExpr)


def test_sqls_sqlexpr_constructor_exists():
    assert callable(sqls_SqlExpr.__init__)


def test_sqls_sqlexpr_constructor_args():
    sig = inspect.signature(sqls_SqlExpr.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqltype_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlType)


def test_sqls_sqltype_constructor_exists():
    assert callable(sqls_SqlType.__init__)


def test_sqls_sqltype_constructor_args():
    sig = inspect.signature(sqls_SqlType.__init__)
    params = list(sig.parameters.keys())



def test_sqls_enumelement_is_not_abstract():
    assert not inspect.isabstract(sqls_EnumElement)


def test_sqls_enumelement_constructor_exists():
    assert callable(sqls_EnumElement.__init__)


def test_sqls_enumelement_constructor_args():
    sig = inspect.signature(sqls_EnumElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_enumelement_has_text():
    assert hasattr(sqls_EnumElement, "text")
    descriptor = None
    for klass in sqls_EnumElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_sqls_enumelement_has_name():
    assert hasattr(sqls_EnumElement, "name")
    descriptor = None
    for klass in sqls_EnumElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_sqlmethod_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlMethod)


def test_sqls_sqlmethod_constructor_exists():
    assert callable(sqls_SqlMethod.__init__)


def test_sqls_sqlmethod_constructor_args():
    sig = inspect.signature(sqls_SqlMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "array" in params, "Missing parameter 'array'"

def test_sqls_sqlmethod_has_name():
    assert hasattr(sqls_SqlMethod, "name")
    descriptor = None
    for klass in sqls_SqlMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqls_sqlmethod_has_array():
    assert hasattr(sqls_SqlMethod, "array")
    descriptor = None
    for klass in sqls_SqlMethod.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_sqls_trigger_is_not_abstract():
    assert not inspect.isabstract(sqls_Trigger)


def test_sqls_trigger_constructor_exists():
    assert callable(sqls_Trigger.__init__)


def test_sqls_trigger_constructor_args():
    sig = inspect.signature(sqls_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_trigger_has_time():
    assert hasattr(sqls_Trigger, "time")
    descriptor = None
    for klass in sqls_Trigger.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_sqls_trigger_has_name():
    assert hasattr(sqls_Trigger, "name")
    descriptor = None
    for klass in sqls_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_column_is_not_abstract():
    assert not inspect.isabstract(sqls_Column)


def test_sqls_column_constructor_exists():
    assert callable(sqls_Column.__init__)


def test_sqls_column_constructor_args():
    sig = inspect.signature(sqls_Column.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "name" in params, "Missing parameter 'name'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"

def test_sqls_column_has_null():
    assert hasattr(sqls_Column, "null")
    descriptor = None
    for klass in sqls_Column.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_sqls_column_has_name():
    assert hasattr(sqls_Column, "name")
    descriptor = None
    for klass in sqls_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqls_column_has_primaryKey():
    assert hasattr(sqls_Column, "primaryKey")
    descriptor = None
    for klass in sqls_Column.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)



def test_sqls_table_is_not_abstract():
    assert not inspect.isabstract(sqls_Table)


def test_sqls_table_constructor_exists():
    assert callable(sqls_Table.__init__)


def test_sqls_table_constructor_args():
    sig = inspect.signature(sqls_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_table_has_name():
    assert hasattr(sqls_Table, "name")
    descriptor = None
    for klass in sqls_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_type_is_not_abstract():
    assert not inspect.isabstract(sqls_Type)


def test_sqls_type_constructor_exists():
    assert callable(sqls_Type.__init__)


def test_sqls_type_constructor_args():
    sig = inspect.signature(sqls_Type.__init__)
    params = list(sig.parameters.keys())



def test_sqls_tag_is_not_abstract():
    assert not inspect.isabstract(sqls_Tag)


def test_sqls_tag_constructor_exists():
    assert callable(sqls_Tag.__init__)


def test_sqls_tag_constructor_args():
    sig = inspect.signature(sqls_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqls_tag_has_name():
    assert hasattr(sqls_Tag, "name")
    descriptor = None
    for klass in sqls_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqls_import_is_not_abstract():
    assert not inspect.isabstract(sqls_Import)


def test_sqls_import_constructor_exists():
    assert callable(sqls_Import.__init__)


def test_sqls_import_constructor_args():
    sig = inspect.signature(sqls_Import.__init__)
    params = list(sig.parameters.keys())



def test_sqls_sqllibrary_is_not_abstract():
    assert not inspect.isabstract(sqls_SqlLibrary)


def test_sqls_sqllibrary_constructor_exists():
    assert callable(sqls_SqlLibrary.__init__)


def test_sqls_sqllibrary_constructor_args():
    sig = inspect.signature(sqls_SqlLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "database" in params, "Missing parameter 'database'"
    assert "version" in params, "Missing parameter 'version'"

def test_sqls_sqllibrary_has_database():
    assert hasattr(sqls_SqlLibrary, "database")
    descriptor = None
    for klass in sqls_SqlLibrary.__mro__:
        if "database" in klass.__dict__:
            descriptor = klass.__dict__["database"]
            break
    assert isinstance(descriptor, property)

def test_sqls_sqllibrary_has_version():
    assert hasattr(sqls_SqlLibrary, "version")
    descriptor = None
    for klass in sqls_SqlLibrary.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_triggertime_exists():
    # Check that the Enumeration exists
    assert TriggerTime is not None

def test_triggertime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerTime]
    expected_literals = [
        "BEFORE",
        "AFTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerTime"


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
TriggerAction_strategy = st.builds(
    TriggerAction,
)
sqls_TriggerUpdate_strategy = st.builds(
    sqls_TriggerUpdate,
)
sqls_TriggerDelete_strategy = st.builds(
    sqls_TriggerDelete,
)
sqls_TriggerInsert_strategy = st.builds(
    sqls_TriggerInsert,
)
Type_strategy = st.builds(
    Type,
)
sqls_TypeDef_strategy = st.builds(
    sqls_TypeDef,
)
sqls_Enum_strategy = st.builds(
    sqls_Enum,
)
sqls_TriggerAction_strategy = st.builds(
    sqls_TriggerAction,
)
sqls_UpdateColumnExpression_strategy = st.builds(
    sqls_UpdateColumnExpression,
)
sqls_TableRef_strategy = st.builds(
    sqls_TableRef,
    alias=
        safe_text
)
sqls_Function_strategy = st.builds(
    sqls_Function,
)
SqlExpr_strategy = st.builds(
    SqlExpr,
)
sqls_SqlNumberLiteral_strategy = st.builds(
    sqls_SqlNumberLiteral,
    value=
        st.integers()
)
sqls_ColumnRef_strategy = st.builds(
    sqls_ColumnRef,
)
sqls_SqlParam_strategy = st.builds(
    sqls_SqlParam,
    name=
        safe_text
)
sqls_SqlPlaceholder_strategy = st.builds(
    sqls_SqlPlaceholder,
)
sqls_SqlBinaryExpr_strategy = st.builds(
    sqls_SqlBinaryExpr,
    op=
        safe_text
)
sqls_NewColumn_strategy = st.builds(
    sqls_NewColumn,
)
sqls_OldColumn_strategy = st.builds(
    sqls_OldColumn,
)
sqls_SqlNested_strategy = st.builds(
    sqls_SqlNested,
)
sqls_SqlStringLiteral_strategy = st.builds(
    sqls_SqlStringLiteral,
    value=
        safe_text
)
sqls_SqlFunction_strategy = st.builds(
    sqls_SqlFunction,
)
sqls_SelectList_strategy = st.builds(
    sqls_SelectList,
)
sqls_ResultColumn_strategy = st.builds(
    sqls_ResultColumn,
    name=
        safe_text
)
sqls_OrderingTerm_strategy = st.builds(
    sqls_OrderingTerm,
    desc=
        st.booleans(),
    asc=
        st.booleans()
)
sqls_SqlSentence_strategy = st.builds(
    sqls_SqlSentence,
)
SqlSentence_strategy = st.builds(
    SqlSentence,
)
sqls_Update_strategy = st.builds(
    sqls_Update,
)
sqls_Insert_strategy = st.builds(
    sqls_Insert,
)
sqls_Delete_strategy = st.builds(
    sqls_Delete,
)
sqls_DeleteTable_strategy = st.builds(
    sqls_DeleteTable,
)
sqls_InsertStatement_strategy = st.builds(
    sqls_InsertStatement,
)
sqls_Get_strategy = st.builds(
    sqls_Get,
)
sqls_SqlMethodRef_strategy = st.builds(
    sqls_SqlMethodRef,
)
sqls_Select_strategy = st.builds(
    sqls_Select,
    all=
        st.booleans()
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sqls_UniqueTableConstraint_strategy = st.builds(
    sqls_UniqueTableConstraint,
    name=
        safe_text
)
sqls_TableConstraint_strategy = st.builds(
    sqls_TableConstraint,
)
sqls_SqlExpr_strategy = st.builds(
    sqls_SqlExpr,
)
sqls_SqlType_strategy = st.builds(
    sqls_SqlType,
)
sqls_EnumElement_strategy = st.builds(
    sqls_EnumElement,
    text=
        safe_text,
    name=
        safe_text
)
sqls_SqlMethod_strategy = st.builds(
    sqls_SqlMethod,
    name=
        safe_text,
    array=
        st.booleans()
)
sqls_Trigger_strategy = st.builds(
    sqls_Trigger,
    time=
        safe_text,
    name=
        safe_text
)
sqls_Column_strategy = st.builds(
    sqls_Column,
    null=
        st.booleans(),
    name=
        safe_text,
    primaryKey=
        st.booleans()
)
sqls_Table_strategy = st.builds(
    sqls_Table,
    name=
        safe_text
)
sqls_Type_strategy = st.builds(
    sqls_Type,
)
sqls_Tag_strategy = st.builds(
    sqls_Tag,
    name=
        safe_text
)
sqls_Import_strategy = st.builds(
    sqls_Import,
)
sqls_SqlLibrary_strategy = st.builds(
    sqls_SqlLibrary,
    database=
        safe_text,
    version=
        st.integers()
)

@given(instance=TriggerAction_strategy)
@settings(max_examples=50)
def test_triggeraction_instantiation(instance):
    assert isinstance(instance, TriggerAction)

@given(instance=sqls_TriggerUpdate_strategy)
@settings(max_examples=50)
def test_sqls_triggerupdate_instantiation(instance):
    assert isinstance(instance, sqls_TriggerUpdate)

@given(instance=sqls_TriggerDelete_strategy)
@settings(max_examples=50)
def test_sqls_triggerdelete_instantiation(instance):
    assert isinstance(instance, sqls_TriggerDelete)

@given(instance=sqls_TriggerInsert_strategy)
@settings(max_examples=50)
def test_sqls_triggerinsert_instantiation(instance):
    assert isinstance(instance, sqls_TriggerInsert)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=sqls_TypeDef_strategy)
@settings(max_examples=50)
def test_sqls_typedef_instantiation(instance):
    assert isinstance(instance, sqls_TypeDef)

@given(instance=sqls_Enum_strategy)
@settings(max_examples=50)
def test_sqls_enum_instantiation(instance):
    assert isinstance(instance, sqls_Enum)

@given(instance=sqls_TriggerAction_strategy)
@settings(max_examples=50)
def test_sqls_triggeraction_instantiation(instance):
    assert isinstance(instance, sqls_TriggerAction)

@given(instance=sqls_UpdateColumnExpression_strategy)
@settings(max_examples=50)
def test_sqls_updatecolumnexpression_instantiation(instance):
    assert isinstance(instance, sqls_UpdateColumnExpression)

@given(instance=sqls_TableRef_strategy)
@settings(max_examples=50)
def test_sqls_tableref_instantiation(instance):
    assert isinstance(instance, sqls_TableRef)



@given(instance=sqls_TableRef_strategy)
def test_sqls_tableref_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sqls_Function_strategy)
@settings(max_examples=50)
def test_sqls_function_instantiation(instance):
    assert isinstance(instance, sqls_Function)

@given(instance=SqlExpr_strategy)
@settings(max_examples=50)
def test_sqlexpr_instantiation(instance):
    assert isinstance(instance, SqlExpr)

@given(instance=sqls_SqlNumberLiteral_strategy)
@settings(max_examples=50)
def test_sqls_sqlnumberliteral_instantiation(instance):
    assert isinstance(instance, sqls_SqlNumberLiteral)



@given(instance=sqls_SqlNumberLiteral_strategy)
def test_sqls_sqlnumberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sqls_ColumnRef_strategy)
@settings(max_examples=50)
def test_sqls_columnref_instantiation(instance):
    assert isinstance(instance, sqls_ColumnRef)

@given(instance=sqls_SqlParam_strategy)
@settings(max_examples=50)
def test_sqls_sqlparam_instantiation(instance):
    assert isinstance(instance, sqls_SqlParam)



@given(instance=sqls_SqlParam_strategy)
def test_sqls_sqlparam_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_SqlPlaceholder_strategy)
@settings(max_examples=50)
def test_sqls_sqlplaceholder_instantiation(instance):
    assert isinstance(instance, sqls_SqlPlaceholder)

@given(instance=sqls_SqlBinaryExpr_strategy)
@settings(max_examples=50)
def test_sqls_sqlbinaryexpr_instantiation(instance):
    assert isinstance(instance, sqls_SqlBinaryExpr)



@given(instance=sqls_SqlBinaryExpr_strategy)
def test_sqls_sqlbinaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqls_NewColumn_strategy)
@settings(max_examples=50)
def test_sqls_newcolumn_instantiation(instance):
    assert isinstance(instance, sqls_NewColumn)

@given(instance=sqls_OldColumn_strategy)
@settings(max_examples=50)
def test_sqls_oldcolumn_instantiation(instance):
    assert isinstance(instance, sqls_OldColumn)

@given(instance=sqls_SqlNested_strategy)
@settings(max_examples=50)
def test_sqls_sqlnested_instantiation(instance):
    assert isinstance(instance, sqls_SqlNested)

@given(instance=sqls_SqlStringLiteral_strategy)
@settings(max_examples=50)
def test_sqls_sqlstringliteral_instantiation(instance):
    assert isinstance(instance, sqls_SqlStringLiteral)



@given(instance=sqls_SqlStringLiteral_strategy)
def test_sqls_sqlstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sqls_SqlFunction_strategy)
@settings(max_examples=50)
def test_sqls_sqlfunction_instantiation(instance):
    assert isinstance(instance, sqls_SqlFunction)

@given(instance=sqls_SelectList_strategy)
@settings(max_examples=50)
def test_sqls_selectlist_instantiation(instance):
    assert isinstance(instance, sqls_SelectList)

@given(instance=sqls_ResultColumn_strategy)
@settings(max_examples=50)
def test_sqls_resultcolumn_instantiation(instance):
    assert isinstance(instance, sqls_ResultColumn)



@given(instance=sqls_ResultColumn_strategy)
def test_sqls_resultcolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_OrderingTerm_strategy)
@settings(max_examples=50)
def test_sqls_orderingterm_instantiation(instance):
    assert isinstance(instance, sqls_OrderingTerm)



@given(instance=sqls_OrderingTerm_strategy)
def test_sqls_orderingterm_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=sqls_OrderingTerm_strategy)
def test_sqls_orderingterm_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

@given(instance=sqls_SqlSentence_strategy)
@settings(max_examples=50)
def test_sqls_sqlsentence_instantiation(instance):
    assert isinstance(instance, sqls_SqlSentence)

@given(instance=SqlSentence_strategy)
@settings(max_examples=50)
def test_sqlsentence_instantiation(instance):
    assert isinstance(instance, SqlSentence)

@given(instance=sqls_Update_strategy)
@settings(max_examples=50)
def test_sqls_update_instantiation(instance):
    assert isinstance(instance, sqls_Update)

@given(instance=sqls_Insert_strategy)
@settings(max_examples=50)
def test_sqls_insert_instantiation(instance):
    assert isinstance(instance, sqls_Insert)

@given(instance=sqls_Delete_strategy)
@settings(max_examples=50)
def test_sqls_delete_instantiation(instance):
    assert isinstance(instance, sqls_Delete)

@given(instance=sqls_DeleteTable_strategy)
@settings(max_examples=50)
def test_sqls_deletetable_instantiation(instance):
    assert isinstance(instance, sqls_DeleteTable)

@given(instance=sqls_InsertStatement_strategy)
@settings(max_examples=50)
def test_sqls_insertstatement_instantiation(instance):
    assert isinstance(instance, sqls_InsertStatement)

@given(instance=sqls_Get_strategy)
@settings(max_examples=50)
def test_sqls_get_instantiation(instance):
    assert isinstance(instance, sqls_Get)

@given(instance=sqls_SqlMethodRef_strategy)
@settings(max_examples=50)
def test_sqls_sqlmethodref_instantiation(instance):
    assert isinstance(instance, sqls_SqlMethodRef)

@given(instance=sqls_Select_strategy)
@settings(max_examples=50)
def test_sqls_select_instantiation(instance):
    assert isinstance(instance, sqls_Select)



@given(instance=sqls_Select_strategy)
def test_sqls_select_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=sqls_UniqueTableConstraint_strategy)
@settings(max_examples=50)
def test_sqls_uniquetableconstraint_instantiation(instance):
    assert isinstance(instance, sqls_UniqueTableConstraint)



@given(instance=sqls_UniqueTableConstraint_strategy)
def test_sqls_uniquetableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_TableConstraint_strategy)
@settings(max_examples=50)
def test_sqls_tableconstraint_instantiation(instance):
    assert isinstance(instance, sqls_TableConstraint)

@given(instance=sqls_SqlExpr_strategy)
@settings(max_examples=50)
def test_sqls_sqlexpr_instantiation(instance):
    assert isinstance(instance, sqls_SqlExpr)

@given(instance=sqls_SqlType_strategy)
@settings(max_examples=50)
def test_sqls_sqltype_instantiation(instance):
    assert isinstance(instance, sqls_SqlType)

@given(instance=sqls_EnumElement_strategy)
@settings(max_examples=50)
def test_sqls_enumelement_instantiation(instance):
    assert isinstance(instance, sqls_EnumElement)



@given(instance=sqls_EnumElement_strategy)
def test_sqls_enumelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=sqls_EnumElement_strategy)
def test_sqls_enumelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_SqlMethod_strategy)
@settings(max_examples=50)
def test_sqls_sqlmethod_instantiation(instance):
    assert isinstance(instance, sqls_SqlMethod)



@given(instance=sqls_SqlMethod_strategy)
def test_sqls_sqlmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sqls_SqlMethod_strategy)
def test_sqls_sqlmethod_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=sqls_Trigger_strategy)
@settings(max_examples=50)
def test_sqls_trigger_instantiation(instance):
    assert isinstance(instance, sqls_Trigger)



@given(instance=sqls_Trigger_strategy)
def test_sqls_trigger_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=sqls_Trigger_strategy)
def test_sqls_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_Column_strategy)
@settings(max_examples=50)
def test_sqls_column_instantiation(instance):
    assert isinstance(instance, sqls_Column)



@given(instance=sqls_Column_strategy)
def test_sqls_column_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=sqls_Column_strategy)
def test_sqls_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sqls_Column_strategy)
def test_sqls_column_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original

@given(instance=sqls_Table_strategy)
@settings(max_examples=50)
def test_sqls_table_instantiation(instance):
    assert isinstance(instance, sqls_Table)



@given(instance=sqls_Table_strategy)
def test_sqls_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_Type_strategy)
@settings(max_examples=50)
def test_sqls_type_instantiation(instance):
    assert isinstance(instance, sqls_Type)

@given(instance=sqls_Tag_strategy)
@settings(max_examples=50)
def test_sqls_tag_instantiation(instance):
    assert isinstance(instance, sqls_Tag)



@given(instance=sqls_Tag_strategy)
def test_sqls_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqls_Import_strategy)
@settings(max_examples=50)
def test_sqls_import_instantiation(instance):
    assert isinstance(instance, sqls_Import)

@given(instance=sqls_SqlLibrary_strategy)
@settings(max_examples=50)
def test_sqls_sqllibrary_instantiation(instance):
    assert isinstance(instance, sqls_SqlLibrary)



@given(instance=sqls_SqlLibrary_strategy)
def test_sqls_sqllibrary_database_setter(instance):
    original = instance.database
    instance.database = original
    assert instance.database == original



@given(instance=sqls_SqlLibrary_strategy)
def test_sqls_sqllibrary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
