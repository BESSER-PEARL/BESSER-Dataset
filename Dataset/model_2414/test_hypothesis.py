import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Domain,
    Column,
    CheckConstraint,
    Index,
    ForeignKey,
    NamedElement,
    rdb_Column,
    rdb_Model,
    Element,
    rdb_NamedElement,
    SchemaElement,
    rdb_NamedColumnSet,
    rdb_Element,
    view_rdb_Column,
    rdb_datatypes_DataType,
    datatypes_PrimitiveDataType,
    rdb_datatypes_Domain,
    rdb_constraints_IndexedColumn,
    IndexedColumn,
    rdb_view_ViewColumn,
    view_rdb_NamedColumnSet,
    rdb_view_ViewAlias,
    ViewAlias,
    ViewColumn,
    rdb_view_ViewExpressionColumn,
    rdb_view_ReferencedViewColumn,
    DataType,
    rdb_datatypes_PrimitiveDataType,
    UniqueConstraint,
    rdb_constraints_PrimaryKey,
    PrimaryKey,
    rdb_TableColumn,
    NamedColumnSet,
    rdb_view_View,
    rdb_Table,
    rdb_SchemaElement,
    rdb_Schema,
    ColumnRefConstraint,
    rdb_constraints_ForeignKey,
    rdb_constraints_UniqueConstraint,
    constraints_rdb_TableColumn,
    Constraint,
    rdb_constraints_Index,
    rdb_constraints_ColumnRefConstraint,
    rdb_constraints_CheckConstraint,
    rdb_constraints_Constraint,
    PrimitiveDataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(CheckConstraint)


def test_checkconstraint_constructor_exists():
    assert callable(CheckConstraint.__init__)


def test_checkconstraint_constructor_args():
    sig = inspect.signature(CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ForeignKey)


def test_foreignkey_constructor_exists():
    assert callable(ForeignKey.__init__)


def test_foreignkey_constructor_args():
    sig = inspect.signature(ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_rdb_column_is_not_abstract():
    assert not inspect.isabstract(rdb_Column)


def test_rdb_column_constructor_exists():
    assert callable(rdb_Column.__init__)


def test_rdb_column_constructor_args():
    sig = inspect.signature(rdb_Column.__init__)
    params = list(sig.parameters.keys())



def test_rdb_model_is_not_abstract():
    assert not inspect.isabstract(rdb_Model)


def test_rdb_model_constructor_exists():
    assert callable(rdb_Model.__init__)


def test_rdb_model_constructor_args():
    sig = inspect.signature(rdb_Model.__init__)
    params = list(sig.parameters.keys())
    assert "server_id" in params, "Missing parameter 'server_id'"

def test_rdb_model_has_server_id():
    assert hasattr(rdb_Model, "server_id")
    descriptor = None
    for klass in rdb_Model.__mro__:
        if "server_id" in klass.__dict__:
            descriptor = klass.__dict__["server_id"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_rdb_namedelement_is_not_abstract():
    assert not inspect.isabstract(rdb_NamedElement)


def test_rdb_namedelement_constructor_exists():
    assert callable(rdb_NamedElement.__init__)


def test_rdb_namedelement_constructor_args():
    sig = inspect.signature(rdb_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdb_namedelement_has_name():
    assert hasattr(rdb_NamedElement, "name")
    descriptor = None
    for klass in rdb_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schemaelement_is_not_abstract():
    assert not inspect.isabstract(SchemaElement)


def test_schemaelement_constructor_exists():
    assert callable(SchemaElement.__init__)


def test_schemaelement_constructor_args():
    sig = inspect.signature(SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_rdb_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(rdb_NamedColumnSet)


def test_rdb_namedcolumnset_constructor_exists():
    assert callable(rdb_NamedColumnSet.__init__)


def test_rdb_namedcolumnset_constructor_args():
    sig = inspect.signature(rdb_NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_rdb_element_is_not_abstract():
    assert not inspect.isabstract(rdb_Element)


def test_rdb_element_constructor_exists():
    assert callable(rdb_Element.__init__)


def test_rdb_element_constructor_args():
    sig = inspect.signature(rdb_Element.__init__)
    params = list(sig.parameters.keys())



def test_view_rdb_column_is_not_abstract():
    assert not inspect.isabstract(view_rdb_Column)


def test_view_rdb_column_constructor_exists():
    assert callable(view_rdb_Column.__init__)


def test_view_rdb_column_constructor_args():
    sig = inspect.signature(view_rdb_Column.__init__)
    params = list(sig.parameters.keys())



def test_rdb_datatypes_datatype_is_not_abstract():
    assert not inspect.isabstract(rdb_datatypes_DataType)


def test_rdb_datatypes_datatype_constructor_exists():
    assert callable(rdb_datatypes_DataType.__init__)


def test_rdb_datatypes_datatype_constructor_args():
    sig = inspect.signature(rdb_datatypes_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"
    assert "default" in params, "Missing parameter 'default'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "size" in params, "Missing parameter 'size'"
    assert "decimalDigits" in params, "Missing parameter 'decimalDigits'"
    assert "check" in params, "Missing parameter 'check'"

def test_rdb_datatypes_datatype_has_var():
    assert hasattr(rdb_datatypes_DataType, "var")
    descriptor = None
    for klass in rdb_datatypes_DataType.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)

def test_rdb_datatypes_datatype_has_default():
    assert hasattr(rdb_datatypes_DataType, "default")
    descriptor = None
    for klass in rdb_datatypes_DataType.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_rdb_datatypes_datatype_has_nullable():
    assert hasattr(rdb_datatypes_DataType, "nullable")
    descriptor = None
    for klass in rdb_datatypes_DataType.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_rdb_datatypes_datatype_has_size():
    assert hasattr(rdb_datatypes_DataType, "size")
    descriptor = None
    for klass in rdb_datatypes_DataType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_rdb_datatypes_datatype_has_decimalDigits():
    assert hasattr(rdb_datatypes_DataType, "decimalDigits")
    descriptor = None
    for klass in rdb_datatypes_DataType.__mro__:
        if "decimalDigits" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits"]
            break
    assert isinstance(descriptor, property)

def test_rdb_datatypes_datatype_has_check():
    assert hasattr(rdb_datatypes_DataType, "check")
    descriptor = None
    for klass in rdb_datatypes_DataType.__mro__:
        if "check" in klass.__dict__:
            descriptor = klass.__dict__["check"]
            break
    assert isinstance(descriptor, property)



def test_datatypes_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(datatypes_PrimitiveDataType)


def test_datatypes_primitivedatatype_constructor_exists():
    assert callable(datatypes_PrimitiveDataType.__init__)


def test_datatypes_primitivedatatype_constructor_args():
    sig = inspect.signature(datatypes_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_rdb_datatypes_domain_is_not_abstract():
    assert not inspect.isabstract(rdb_datatypes_Domain)


def test_rdb_datatypes_domain_constructor_exists():
    assert callable(rdb_datatypes_Domain.__init__)


def test_rdb_datatypes_domain_constructor_args():
    sig = inspect.signature(rdb_datatypes_Domain.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_indexedcolumn_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_IndexedColumn)


def test_rdb_constraints_indexedcolumn_constructor_exists():
    assert callable(rdb_constraints_IndexedColumn.__init__)


def test_rdb_constraints_indexedcolumn_constructor_args():
    sig = inspect.signature(rdb_constraints_IndexedColumn.__init__)
    params = list(sig.parameters.keys())
    assert "ascending" in params, "Missing parameter 'ascending'"

def test_rdb_constraints_indexedcolumn_has_ascending():
    assert hasattr(rdb_constraints_IndexedColumn, "ascending")
    descriptor = None
    for klass in rdb_constraints_IndexedColumn.__mro__:
        if "ascending" in klass.__dict__:
            descriptor = klass.__dict__["ascending"]
            break
    assert isinstance(descriptor, property)



def test_indexedcolumn_is_not_abstract():
    assert not inspect.isabstract(IndexedColumn)


def test_indexedcolumn_constructor_exists():
    assert callable(IndexedColumn.__init__)


def test_indexedcolumn_constructor_args():
    sig = inspect.signature(IndexedColumn.__init__)
    params = list(sig.parameters.keys())



def test_rdb_view_viewcolumn_is_not_abstract():
    assert not inspect.isabstract(rdb_view_ViewColumn)


def test_rdb_view_viewcolumn_constructor_exists():
    assert callable(rdb_view_ViewColumn.__init__)


def test_rdb_view_viewcolumn_constructor_args():
    sig = inspect.signature(rdb_view_ViewColumn.__init__)
    params = list(sig.parameters.keys())



def test_view_rdb_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(view_rdb_NamedColumnSet)


def test_view_rdb_namedcolumnset_constructor_exists():
    assert callable(view_rdb_NamedColumnSet.__init__)


def test_view_rdb_namedcolumnset_constructor_args():
    sig = inspect.signature(view_rdb_NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_rdb_view_viewalias_is_not_abstract():
    assert not inspect.isabstract(rdb_view_ViewAlias)


def test_rdb_view_viewalias_constructor_exists():
    assert callable(rdb_view_ViewAlias.__init__)


def test_rdb_view_viewalias_constructor_args():
    sig = inspect.signature(rdb_view_ViewAlias.__init__)
    params = list(sig.parameters.keys())



def test_viewalias_is_not_abstract():
    assert not inspect.isabstract(ViewAlias)


def test_viewalias_constructor_exists():
    assert callable(ViewAlias.__init__)


def test_viewalias_constructor_args():
    sig = inspect.signature(ViewAlias.__init__)
    params = list(sig.parameters.keys())



def test_viewcolumn_is_not_abstract():
    assert not inspect.isabstract(ViewColumn)


def test_viewcolumn_constructor_exists():
    assert callable(ViewColumn.__init__)


def test_viewcolumn_constructor_args():
    sig = inspect.signature(ViewColumn.__init__)
    params = list(sig.parameters.keys())



def test_rdb_view_viewexpressioncolumn_is_not_abstract():
    assert not inspect.isabstract(rdb_view_ViewExpressionColumn)


def test_rdb_view_viewexpressioncolumn_constructor_exists():
    assert callable(rdb_view_ViewExpressionColumn.__init__)


def test_rdb_view_viewexpressioncolumn_constructor_args():
    sig = inspect.signature(rdb_view_ViewExpressionColumn.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_rdb_view_viewexpressioncolumn_has_expression():
    assert hasattr(rdb_view_ViewExpressionColumn, "expression")
    descriptor = None
    for klass in rdb_view_ViewExpressionColumn.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_rdb_view_referencedviewcolumn_is_not_abstract():
    assert not inspect.isabstract(rdb_view_ReferencedViewColumn)


def test_rdb_view_referencedviewcolumn_constructor_exists():
    assert callable(rdb_view_ReferencedViewColumn.__init__)


def test_rdb_view_referencedviewcolumn_constructor_args():
    sig = inspect.signature(rdb_view_ReferencedViewColumn.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_rdb_datatypes_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(rdb_datatypes_PrimitiveDataType)


def test_rdb_datatypes_primitivedatatype_constructor_exists():
    assert callable(rdb_datatypes_PrimitiveDataType.__init__)


def test_rdb_datatypes_primitivedatatype_constructor_args():
    sig = inspect.signature(rdb_datatypes_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rdb_datatypes_primitivedatatype_has_type():
    assert hasattr(rdb_datatypes_PrimitiveDataType, "type")
    descriptor = None
    for klass in rdb_datatypes_PrimitiveDataType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_primarykey_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_PrimaryKey)


def test_rdb_constraints_primarykey_constructor_exists():
    assert callable(rdb_constraints_PrimaryKey.__init__)


def test_rdb_constraints_primarykey_constructor_args():
    sig = inspect.signature(rdb_constraints_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_primarykey_is_not_abstract():
    assert not inspect.isabstract(PrimaryKey)


def test_primarykey_constructor_exists():
    assert callable(PrimaryKey.__init__)


def test_primarykey_constructor_args():
    sig = inspect.signature(PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_rdb_tablecolumn_is_not_abstract():
    assert not inspect.isabstract(rdb_TableColumn)


def test_rdb_tablecolumn_constructor_exists():
    assert callable(rdb_TableColumn.__init__)


def test_rdb_tablecolumn_constructor_args():
    sig = inspect.signature(rdb_TableColumn.__init__)
    params = list(sig.parameters.keys())
    assert "isForeignKey" in params, "Missing parameter 'isForeignKey'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_rdb_tablecolumn_has_isForeignKey():
    assert hasattr(rdb_TableColumn, "isForeignKey")
    descriptor = None
    for klass in rdb_TableColumn.__mro__:
        if "isForeignKey" in klass.__dict__:
            descriptor = klass.__dict__["isForeignKey"]
            break
    assert isinstance(descriptor, property)

def test_rdb_tablecolumn_has_isPrimaryKey():
    assert hasattr(rdb_TableColumn, "isPrimaryKey")
    descriptor = None
    for klass in rdb_TableColumn.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(NamedColumnSet)


def test_namedcolumnset_constructor_exists():
    assert callable(NamedColumnSet.__init__)


def test_namedcolumnset_constructor_args():
    sig = inspect.signature(NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_rdb_view_view_is_not_abstract():
    assert not inspect.isabstract(rdb_view_View)


def test_rdb_view_view_constructor_exists():
    assert callable(rdb_view_View.__init__)


def test_rdb_view_view_constructor_args():
    sig = inspect.signature(rdb_view_View.__init__)
    params = list(sig.parameters.keys())
    assert "ddl" in params, "Missing parameter 'ddl'"

def test_rdb_view_view_has_ddl():
    assert hasattr(rdb_view_View, "ddl")
    descriptor = None
    for klass in rdb_view_View.__mro__:
        if "ddl" in klass.__dict__:
            descriptor = klass.__dict__["ddl"]
            break
    assert isinstance(descriptor, property)



def test_rdb_table_is_not_abstract():
    assert not inspect.isabstract(rdb_Table)


def test_rdb_table_constructor_exists():
    assert callable(rdb_Table.__init__)


def test_rdb_table_constructor_args():
    sig = inspect.signature(rdb_Table.__init__)
    params = list(sig.parameters.keys())



def test_rdb_schemaelement_is_not_abstract():
    assert not inspect.isabstract(rdb_SchemaElement)


def test_rdb_schemaelement_constructor_exists():
    assert callable(rdb_SchemaElement.__init__)


def test_rdb_schemaelement_constructor_args():
    sig = inspect.signature(rdb_SchemaElement.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"

def test_rdb_schemaelement_has_owner():
    assert hasattr(rdb_SchemaElement, "owner")
    descriptor = None
    for klass in rdb_SchemaElement.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)



def test_rdb_schema_is_not_abstract():
    assert not inspect.isabstract(rdb_Schema)


def test_rdb_schema_constructor_exists():
    assert callable(rdb_Schema.__init__)


def test_rdb_schema_constructor_args():
    sig = inspect.signature(rdb_Schema.__init__)
    params = list(sig.parameters.keys())



def test_columnrefconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnRefConstraint)


def test_columnrefconstraint_constructor_exists():
    assert callable(ColumnRefConstraint.__init__)


def test_columnrefconstraint_constructor_args():
    sig = inspect.signature(ColumnRefConstraint.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_ForeignKey)


def test_rdb_constraints_foreignkey_constructor_exists():
    assert callable(rdb_constraints_ForeignKey.__init__)


def test_rdb_constraints_foreignkey_constructor_args():
    sig = inspect.signature(rdb_constraints_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_UniqueConstraint)


def test_rdb_constraints_uniqueconstraint_constructor_exists():
    assert callable(rdb_constraints_UniqueConstraint.__init__)


def test_rdb_constraints_uniqueconstraint_constructor_args():
    sig = inspect.signature(rdb_constraints_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_constraints_rdb_tablecolumn_is_not_abstract():
    assert not inspect.isabstract(constraints_rdb_TableColumn)


def test_constraints_rdb_tablecolumn_constructor_exists():
    assert callable(constraints_rdb_TableColumn.__init__)


def test_constraints_rdb_tablecolumn_constructor_args():
    sig = inspect.signature(constraints_rdb_TableColumn.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_index_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_Index)


def test_rdb_constraints_index_constructor_exists():
    assert callable(rdb_constraints_Index.__init__)


def test_rdb_constraints_index_constructor_args():
    sig = inspect.signature(rdb_constraints_Index.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_columnrefconstraint_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_ColumnRefConstraint)


def test_rdb_constraints_columnrefconstraint_constructor_exists():
    assert callable(rdb_constraints_ColumnRefConstraint.__init__)


def test_rdb_constraints_columnrefconstraint_constructor_args():
    sig = inspect.signature(rdb_constraints_ColumnRefConstraint.__init__)
    params = list(sig.parameters.keys())



def test_rdb_constraints_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_CheckConstraint)


def test_rdb_constraints_checkconstraint_constructor_exists():
    assert callable(rdb_constraints_CheckConstraint.__init__)


def test_rdb_constraints_checkconstraint_constructor_args():
    sig = inspect.signature(rdb_constraints_CheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_rdb_constraints_checkconstraint_has_expression():
    assert hasattr(rdb_constraints_CheckConstraint, "expression")
    descriptor = None
    for klass in rdb_constraints_CheckConstraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_rdb_constraints_constraint_is_not_abstract():
    assert not inspect.isabstract(rdb_constraints_Constraint)


def test_rdb_constraints_constraint_constructor_exists():
    assert callable(rdb_constraints_Constraint.__init__)


def test_rdb_constraints_constraint_constructor_args():
    sig = inspect.signature(rdb_constraints_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveDataType)


def test_primitivedatatype_constructor_exists():
    assert callable(PrimitiveDataType.__init__)


def test_primitivedatatype_constructor_args():
    sig = inspect.signature(PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())


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
Domain_strategy = st.builds(
    Domain,
)
Column_strategy = st.builds(
    Column,
)
CheckConstraint_strategy = st.builds(
    CheckConstraint,
)
Index_strategy = st.builds(
    Index,
)
ForeignKey_strategy = st.builds(
    ForeignKey,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
rdb_Column_strategy = st.builds(
    rdb_Column,
)
rdb_Model_strategy = st.builds(
    rdb_Model,
    server_id=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
rdb_NamedElement_strategy = st.builds(
    rdb_NamedElement,
    name=
        safe_text
)
SchemaElement_strategy = st.builds(
    SchemaElement,
)
rdb_NamedColumnSet_strategy = st.builds(
    rdb_NamedColumnSet,
)
rdb_Element_strategy = st.builds(
    rdb_Element,
)
view_rdb_Column_strategy = st.builds(
    view_rdb_Column,
)
rdb_datatypes_DataType_strategy = st.builds(
    rdb_datatypes_DataType,
    var=
        safe_text,
    default=
        safe_text,
    nullable=
        st.booleans(),
    size=
        st.integers(),
    decimalDigits=
        st.integers(),
    check=
        safe_text
)
datatypes_PrimitiveDataType_strategy = st.builds(
    datatypes_PrimitiveDataType,
)
rdb_datatypes_Domain_strategy = st.builds(
    rdb_datatypes_Domain,
)
rdb_constraints_IndexedColumn_strategy = st.builds(
    rdb_constraints_IndexedColumn,
    ascending=
        st.booleans()
)
IndexedColumn_strategy = st.builds(
    IndexedColumn,
)
rdb_view_ViewColumn_strategy = st.builds(
    rdb_view_ViewColumn,
)
view_rdb_NamedColumnSet_strategy = st.builds(
    view_rdb_NamedColumnSet,
)
rdb_view_ViewAlias_strategy = st.builds(
    rdb_view_ViewAlias,
)
ViewAlias_strategy = st.builds(
    ViewAlias,
)
ViewColumn_strategy = st.builds(
    ViewColumn,
)
rdb_view_ViewExpressionColumn_strategy = st.builds(
    rdb_view_ViewExpressionColumn,
    expression=
        safe_text
)
rdb_view_ReferencedViewColumn_strategy = st.builds(
    rdb_view_ReferencedViewColumn,
)
DataType_strategy = st.builds(
    DataType,
)
rdb_datatypes_PrimitiveDataType_strategy = st.builds(
    rdb_datatypes_PrimitiveDataType,
    type=
        safe_text
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
rdb_constraints_PrimaryKey_strategy = st.builds(
    rdb_constraints_PrimaryKey,
)
PrimaryKey_strategy = st.builds(
    PrimaryKey,
)
rdb_TableColumn_strategy = st.builds(
    rdb_TableColumn,
    isForeignKey=
        safe_text,
    isPrimaryKey=
        safe_text
)
NamedColumnSet_strategy = st.builds(
    NamedColumnSet,
)
rdb_view_View_strategy = st.builds(
    rdb_view_View,
    ddl=
        safe_text
)
rdb_Table_strategy = st.builds(
    rdb_Table,
)
rdb_SchemaElement_strategy = st.builds(
    rdb_SchemaElement,
    owner=
        safe_text
)
rdb_Schema_strategy = st.builds(
    rdb_Schema,
)
ColumnRefConstraint_strategy = st.builds(
    ColumnRefConstraint,
)
rdb_constraints_ForeignKey_strategy = st.builds(
    rdb_constraints_ForeignKey,
)
rdb_constraints_UniqueConstraint_strategy = st.builds(
    rdb_constraints_UniqueConstraint,
)
constraints_rdb_TableColumn_strategy = st.builds(
    constraints_rdb_TableColumn,
)
Constraint_strategy = st.builds(
    Constraint,
)
rdb_constraints_Index_strategy = st.builds(
    rdb_constraints_Index,
)
rdb_constraints_ColumnRefConstraint_strategy = st.builds(
    rdb_constraints_ColumnRefConstraint,
)
rdb_constraints_CheckConstraint_strategy = st.builds(
    rdb_constraints_CheckConstraint,
    expression=
        safe_text
)
rdb_constraints_Constraint_strategy = st.builds(
    rdb_constraints_Constraint,
)
PrimitiveDataType_strategy = st.builds(
    PrimitiveDataType,
)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=CheckConstraint_strategy)
@settings(max_examples=50)
def test_checkconstraint_instantiation(instance):
    assert isinstance(instance, CheckConstraint)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=ForeignKey_strategy)
@settings(max_examples=50)
def test_foreignkey_instantiation(instance):
    assert isinstance(instance, ForeignKey)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=rdb_Column_strategy)
@settings(max_examples=50)
def test_rdb_column_instantiation(instance):
    assert isinstance(instance, rdb_Column)

@given(instance=rdb_Model_strategy)
@settings(max_examples=50)
def test_rdb_model_instantiation(instance):
    assert isinstance(instance, rdb_Model)



@given(instance=rdb_Model_strategy)
def test_rdb_model_server_id_setter(instance):
    original = instance.server_id
    instance.server_id = original
    assert instance.server_id == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=rdb_NamedElement_strategy)
@settings(max_examples=50)
def test_rdb_namedelement_instantiation(instance):
    assert isinstance(instance, rdb_NamedElement)



@given(instance=rdb_NamedElement_strategy)
def test_rdb_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SchemaElement_strategy)
@settings(max_examples=50)
def test_schemaelement_instantiation(instance):
    assert isinstance(instance, SchemaElement)

@given(instance=rdb_NamedColumnSet_strategy)
@settings(max_examples=50)
def test_rdb_namedcolumnset_instantiation(instance):
    assert isinstance(instance, rdb_NamedColumnSet)

@given(instance=rdb_Element_strategy)
@settings(max_examples=50)
def test_rdb_element_instantiation(instance):
    assert isinstance(instance, rdb_Element)

@given(instance=view_rdb_Column_strategy)
@settings(max_examples=50)
def test_view_rdb_column_instantiation(instance):
    assert isinstance(instance, view_rdb_Column)

@given(instance=rdb_datatypes_DataType_strategy)
@settings(max_examples=50)
def test_rdb_datatypes_datatype_instantiation(instance):
    assert isinstance(instance, rdb_datatypes_DataType)



@given(instance=rdb_datatypes_DataType_strategy)
def test_rdb_datatypes_datatype_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original



@given(instance=rdb_datatypes_DataType_strategy)
def test_rdb_datatypes_datatype_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=rdb_datatypes_DataType_strategy)
def test_rdb_datatypes_datatype_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=rdb_datatypes_DataType_strategy)
def test_rdb_datatypes_datatype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=rdb_datatypes_DataType_strategy)
def test_rdb_datatypes_datatype_decimalDigits_setter(instance):
    original = instance.decimalDigits
    instance.decimalDigits = original
    assert instance.decimalDigits == original



@given(instance=rdb_datatypes_DataType_strategy)
def test_rdb_datatypes_datatype_check_setter(instance):
    original = instance.check
    instance.check = original
    assert instance.check == original

@given(instance=datatypes_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_datatypes_primitivedatatype_instantiation(instance):
    assert isinstance(instance, datatypes_PrimitiveDataType)

@given(instance=rdb_datatypes_Domain_strategy)
@settings(max_examples=50)
def test_rdb_datatypes_domain_instantiation(instance):
    assert isinstance(instance, rdb_datatypes_Domain)

@given(instance=rdb_constraints_IndexedColumn_strategy)
@settings(max_examples=50)
def test_rdb_constraints_indexedcolumn_instantiation(instance):
    assert isinstance(instance, rdb_constraints_IndexedColumn)



@given(instance=rdb_constraints_IndexedColumn_strategy)
def test_rdb_constraints_indexedcolumn_ascending_setter(instance):
    original = instance.ascending
    instance.ascending = original
    assert instance.ascending == original

@given(instance=IndexedColumn_strategy)
@settings(max_examples=50)
def test_indexedcolumn_instantiation(instance):
    assert isinstance(instance, IndexedColumn)

@given(instance=rdb_view_ViewColumn_strategy)
@settings(max_examples=50)
def test_rdb_view_viewcolumn_instantiation(instance):
    assert isinstance(instance, rdb_view_ViewColumn)

@given(instance=view_rdb_NamedColumnSet_strategy)
@settings(max_examples=50)
def test_view_rdb_namedcolumnset_instantiation(instance):
    assert isinstance(instance, view_rdb_NamedColumnSet)

@given(instance=rdb_view_ViewAlias_strategy)
@settings(max_examples=50)
def test_rdb_view_viewalias_instantiation(instance):
    assert isinstance(instance, rdb_view_ViewAlias)

@given(instance=ViewAlias_strategy)
@settings(max_examples=50)
def test_viewalias_instantiation(instance):
    assert isinstance(instance, ViewAlias)

@given(instance=ViewColumn_strategy)
@settings(max_examples=50)
def test_viewcolumn_instantiation(instance):
    assert isinstance(instance, ViewColumn)

@given(instance=rdb_view_ViewExpressionColumn_strategy)
@settings(max_examples=50)
def test_rdb_view_viewexpressioncolumn_instantiation(instance):
    assert isinstance(instance, rdb_view_ViewExpressionColumn)



@given(instance=rdb_view_ViewExpressionColumn_strategy)
def test_rdb_view_viewexpressioncolumn_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=rdb_view_ReferencedViewColumn_strategy)
@settings(max_examples=50)
def test_rdb_view_referencedviewcolumn_instantiation(instance):
    assert isinstance(instance, rdb_view_ReferencedViewColumn)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=rdb_datatypes_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_rdb_datatypes_primitivedatatype_instantiation(instance):
    assert isinstance(instance, rdb_datatypes_PrimitiveDataType)



@given(instance=rdb_datatypes_PrimitiveDataType_strategy)
def test_rdb_datatypes_primitivedatatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=rdb_constraints_PrimaryKey_strategy)
@settings(max_examples=50)
def test_rdb_constraints_primarykey_instantiation(instance):
    assert isinstance(instance, rdb_constraints_PrimaryKey)

@given(instance=PrimaryKey_strategy)
@settings(max_examples=50)
def test_primarykey_instantiation(instance):
    assert isinstance(instance, PrimaryKey)

@given(instance=rdb_TableColumn_strategy)
@settings(max_examples=50)
def test_rdb_tablecolumn_instantiation(instance):
    assert isinstance(instance, rdb_TableColumn)



@given(instance=rdb_TableColumn_strategy)
def test_rdb_tablecolumn_isForeignKey_setter(instance):
    original = instance.isForeignKey
    instance.isForeignKey = original
    assert instance.isForeignKey == original



@given(instance=rdb_TableColumn_strategy)
def test_rdb_tablecolumn_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=NamedColumnSet_strategy)
@settings(max_examples=50)
def test_namedcolumnset_instantiation(instance):
    assert isinstance(instance, NamedColumnSet)

@given(instance=rdb_view_View_strategy)
@settings(max_examples=50)
def test_rdb_view_view_instantiation(instance):
    assert isinstance(instance, rdb_view_View)



@given(instance=rdb_view_View_strategy)
def test_rdb_view_view_ddl_setter(instance):
    original = instance.ddl
    instance.ddl = original
    assert instance.ddl == original

@given(instance=rdb_Table_strategy)
@settings(max_examples=50)
def test_rdb_table_instantiation(instance):
    assert isinstance(instance, rdb_Table)

@given(instance=rdb_SchemaElement_strategy)
@settings(max_examples=50)
def test_rdb_schemaelement_instantiation(instance):
    assert isinstance(instance, rdb_SchemaElement)



@given(instance=rdb_SchemaElement_strategy)
def test_rdb_schemaelement_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=rdb_Schema_strategy)
@settings(max_examples=50)
def test_rdb_schema_instantiation(instance):
    assert isinstance(instance, rdb_Schema)

@given(instance=ColumnRefConstraint_strategy)
@settings(max_examples=50)
def test_columnrefconstraint_instantiation(instance):
    assert isinstance(instance, ColumnRefConstraint)

@given(instance=rdb_constraints_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdb_constraints_foreignkey_instantiation(instance):
    assert isinstance(instance, rdb_constraints_ForeignKey)

@given(instance=rdb_constraints_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_rdb_constraints_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, rdb_constraints_UniqueConstraint)

@given(instance=constraints_rdb_TableColumn_strategy)
@settings(max_examples=50)
def test_constraints_rdb_tablecolumn_instantiation(instance):
    assert isinstance(instance, constraints_rdb_TableColumn)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=rdb_constraints_Index_strategy)
@settings(max_examples=50)
def test_rdb_constraints_index_instantiation(instance):
    assert isinstance(instance, rdb_constraints_Index)

@given(instance=rdb_constraints_ColumnRefConstraint_strategy)
@settings(max_examples=50)
def test_rdb_constraints_columnrefconstraint_instantiation(instance):
    assert isinstance(instance, rdb_constraints_ColumnRefConstraint)

@given(instance=rdb_constraints_CheckConstraint_strategy)
@settings(max_examples=50)
def test_rdb_constraints_checkconstraint_instantiation(instance):
    assert isinstance(instance, rdb_constraints_CheckConstraint)



@given(instance=rdb_constraints_CheckConstraint_strategy)
def test_rdb_constraints_checkconstraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=rdb_constraints_Constraint_strategy)
@settings(max_examples=50)
def test_rdb_constraints_constraint_instantiation(instance):
    assert isinstance(instance, rdb_constraints_Constraint)

@given(instance=PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_primitivedatatype_instantiation(instance):
    assert isinstance(instance, PrimitiveDataType)
