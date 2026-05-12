import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SQLDistinctType,
    SQLSimpleType,
    CWMRelationalData_SQLDataType,
    CWMRelationalData_Trigger,
    QueryExpression,
    Trigger,
    CWMRelationalData_ColumnSet,
    NamedColumnSet,
    ColumnSet,
    CWMRelationalData_NamedColumnSet,
    CWMRelationalData_QueryColumnSet,
    SQLDataType,
    CWMRelationalData_SQLSimpleType,
    CWMRelationalData_SQLDistinctType,
    CheckConstraint,
    CWMRelationalData_View,
    CWMRelationalData_Table,
    CWMRelationalData_CheckConstraint,
    CWMRelationalData_QueryExpression,
    CWMRelationalData_Column,
    Table,
    Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sqldistincttype_is_not_abstract():
    assert not inspect.isabstract(SQLDistinctType)


def test_sqldistincttype_constructor_exists():
    assert callable(SQLDistinctType.__init__)


def test_sqldistincttype_constructor_args():
    sig = inspect.signature(SQLDistinctType.__init__)
    params = list(sig.parameters.keys())



def test_sqlsimpletype_is_not_abstract():
    assert not inspect.isabstract(SQLSimpleType)


def test_sqlsimpletype_constructor_exists():
    assert callable(SQLSimpleType.__init__)


def test_sqlsimpletype_constructor_args():
    sig = inspect.signature(SQLSimpleType.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_SQLDataType)


def test_cwmrelationaldata_sqldatatype_constructor_exists():
    assert callable(CWMRelationalData_SQLDataType.__init__)


def test_cwmrelationaldata_sqldatatype_constructor_args():
    sig = inspect.signature(CWMRelationalData_SQLDataType.__init__)
    params = list(sig.parameters.keys())
    assert "typeNumber" in params, "Missing parameter 'typeNumber'"

def test_cwmrelationaldata_sqldatatype_has_typeNumber():
    assert hasattr(CWMRelationalData_SQLDataType, "typeNumber")
    descriptor = None
    for klass in CWMRelationalData_SQLDataType.__mro__:
        if "typeNumber" in klass.__dict__:
            descriptor = klass.__dict__["typeNumber"]
            break
    assert isinstance(descriptor, property)



def test_cwmrelationaldata_trigger_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_Trigger)


def test_cwmrelationaldata_trigger_constructor_exists():
    assert callable(CWMRelationalData_Trigger.__init__)


def test_cwmrelationaldata_trigger_constructor_args():
    sig = inspect.signature(CWMRelationalData_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_queryexpression_is_not_abstract():
    assert not inspect.isabstract(QueryExpression)


def test_queryexpression_constructor_exists():
    assert callable(QueryExpression.__init__)


def test_queryexpression_constructor_args():
    sig = inspect.signature(QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_columnset_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_ColumnSet)


def test_cwmrelationaldata_columnset_constructor_exists():
    assert callable(CWMRelationalData_ColumnSet.__init__)


def test_cwmrelationaldata_columnset_constructor_args():
    sig = inspect.signature(CWMRelationalData_ColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(NamedColumnSet)


def test_namedcolumnset_constructor_exists():
    assert callable(NamedColumnSet.__init__)


def test_namedcolumnset_constructor_args():
    sig = inspect.signature(NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_columnset_is_not_abstract():
    assert not inspect.isabstract(ColumnSet)


def test_columnset_constructor_exists():
    assert callable(ColumnSet.__init__)


def test_columnset_constructor_args():
    sig = inspect.signature(ColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_namedcolumnset_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_NamedColumnSet)


def test_cwmrelationaldata_namedcolumnset_constructor_exists():
    assert callable(CWMRelationalData_NamedColumnSet.__init__)


def test_cwmrelationaldata_namedcolumnset_constructor_args():
    sig = inspect.signature(CWMRelationalData_NamedColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_querycolumnset_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_QueryColumnSet)


def test_cwmrelationaldata_querycolumnset_constructor_exists():
    assert callable(CWMRelationalData_QueryColumnSet.__init__)


def test_cwmrelationaldata_querycolumnset_constructor_args():
    sig = inspect.signature(CWMRelationalData_QueryColumnSet.__init__)
    params = list(sig.parameters.keys())



def test_sqldatatype_is_not_abstract():
    assert not inspect.isabstract(SQLDataType)


def test_sqldatatype_constructor_exists():
    assert callable(SQLDataType.__init__)


def test_sqldatatype_constructor_args():
    sig = inspect.signature(SQLDataType.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_sqlsimpletype_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_SQLSimpleType)


def test_cwmrelationaldata_sqlsimpletype_constructor_exists():
    assert callable(CWMRelationalData_SQLSimpleType.__init__)


def test_cwmrelationaldata_sqlsimpletype_constructor_args():
    sig = inspect.signature(CWMRelationalData_SQLSimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "numericScale" in params, "Missing parameter 'numericScale'"
    assert "characterOctetLength" in params, "Missing parameter 'characterOctetLength'"
    assert "characterMaximumLength" in params, "Missing parameter 'characterMaximumLength'"
    assert "numericPrecisionRadix" in params, "Missing parameter 'numericPrecisionRadix'"
    assert "dateTimePrecision" in params, "Missing parameter 'dateTimePrecision'"
    assert "numericPrecision" in params, "Missing parameter 'numericPrecision'"

def test_cwmrelationaldata_sqlsimpletype_has_numericScale():
    assert hasattr(CWMRelationalData_SQLSimpleType, "numericScale")
    descriptor = None
    for klass in CWMRelationalData_SQLSimpleType.__mro__:
        if "numericScale" in klass.__dict__:
            descriptor = klass.__dict__["numericScale"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqlsimpletype_has_characterOctetLength():
    assert hasattr(CWMRelationalData_SQLSimpleType, "characterOctetLength")
    descriptor = None
    for klass in CWMRelationalData_SQLSimpleType.__mro__:
        if "characterOctetLength" in klass.__dict__:
            descriptor = klass.__dict__["characterOctetLength"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqlsimpletype_has_characterMaximumLength():
    assert hasattr(CWMRelationalData_SQLSimpleType, "characterMaximumLength")
    descriptor = None
    for klass in CWMRelationalData_SQLSimpleType.__mro__:
        if "characterMaximumLength" in klass.__dict__:
            descriptor = klass.__dict__["characterMaximumLength"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqlsimpletype_has_numericPrecisionRadix():
    assert hasattr(CWMRelationalData_SQLSimpleType, "numericPrecisionRadix")
    descriptor = None
    for klass in CWMRelationalData_SQLSimpleType.__mro__:
        if "numericPrecisionRadix" in klass.__dict__:
            descriptor = klass.__dict__["numericPrecisionRadix"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqlsimpletype_has_dateTimePrecision():
    assert hasattr(CWMRelationalData_SQLSimpleType, "dateTimePrecision")
    descriptor = None
    for klass in CWMRelationalData_SQLSimpleType.__mro__:
        if "dateTimePrecision" in klass.__dict__:
            descriptor = klass.__dict__["dateTimePrecision"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqlsimpletype_has_numericPrecision():
    assert hasattr(CWMRelationalData_SQLSimpleType, "numericPrecision")
    descriptor = None
    for klass in CWMRelationalData_SQLSimpleType.__mro__:
        if "numericPrecision" in klass.__dict__:
            descriptor = klass.__dict__["numericPrecision"]
            break
    assert isinstance(descriptor, property)



def test_cwmrelationaldata_sqldistincttype_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_SQLDistinctType)


def test_cwmrelationaldata_sqldistincttype_constructor_exists():
    assert callable(CWMRelationalData_SQLDistinctType.__init__)


def test_cwmrelationaldata_sqldistincttype_constructor_args():
    sig = inspect.signature(CWMRelationalData_SQLDistinctType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_cwmrelationaldata_sqldistincttype_has_length():
    assert hasattr(CWMRelationalData_SQLDistinctType, "length")
    descriptor = None
    for klass in CWMRelationalData_SQLDistinctType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqldistincttype_has_precision():
    assert hasattr(CWMRelationalData_SQLDistinctType, "precision")
    descriptor = None
    for klass in CWMRelationalData_SQLDistinctType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_sqldistincttype_has_scale():
    assert hasattr(CWMRelationalData_SQLDistinctType, "scale")
    descriptor = None
    for klass in CWMRelationalData_SQLDistinctType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(CheckConstraint)


def test_checkconstraint_constructor_exists():
    assert callable(CheckConstraint.__init__)


def test_checkconstraint_constructor_args():
    sig = inspect.signature(CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_view_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_View)


def test_cwmrelationaldata_view_constructor_exists():
    assert callable(CWMRelationalData_View.__init__)


def test_cwmrelationaldata_view_constructor_args():
    sig = inspect.signature(CWMRelationalData_View.__init__)
    params = list(sig.parameters.keys())
    assert "checkOption" in params, "Missing parameter 'checkOption'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_cwmrelationaldata_view_has_checkOption():
    assert hasattr(CWMRelationalData_View, "checkOption")
    descriptor = None
    for klass in CWMRelationalData_View.__mro__:
        if "checkOption" in klass.__dict__:
            descriptor = klass.__dict__["checkOption"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_view_has_isReadOnly():
    assert hasattr(CWMRelationalData_View, "isReadOnly")
    descriptor = None
    for klass in CWMRelationalData_View.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_cwmrelationaldata_table_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_Table)


def test_cwmrelationaldata_table_constructor_exists():
    assert callable(CWMRelationalData_Table.__init__)


def test_cwmrelationaldata_table_constructor_args():
    sig = inspect.signature(CWMRelationalData_Table.__init__)
    params = list(sig.parameters.keys())
    assert "isTemporary" in params, "Missing parameter 'isTemporary'"
    assert "temporaryScope" in params, "Missing parameter 'temporaryScope'"
    assert "isSystem" in params, "Missing parameter 'isSystem'"

def test_cwmrelationaldata_table_has_isTemporary():
    assert hasattr(CWMRelationalData_Table, "isTemporary")
    descriptor = None
    for klass in CWMRelationalData_Table.__mro__:
        if "isTemporary" in klass.__dict__:
            descriptor = klass.__dict__["isTemporary"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_table_has_temporaryScope():
    assert hasattr(CWMRelationalData_Table, "temporaryScope")
    descriptor = None
    for klass in CWMRelationalData_Table.__mro__:
        if "temporaryScope" in klass.__dict__:
            descriptor = klass.__dict__["temporaryScope"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_table_has_isSystem():
    assert hasattr(CWMRelationalData_Table, "isSystem")
    descriptor = None
    for klass in CWMRelationalData_Table.__mro__:
        if "isSystem" in klass.__dict__:
            descriptor = klass.__dict__["isSystem"]
            break
    assert isinstance(descriptor, property)



def test_cwmrelationaldata_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_CheckConstraint)


def test_cwmrelationaldata_checkconstraint_constructor_exists():
    assert callable(CWMRelationalData_CheckConstraint.__init__)


def test_cwmrelationaldata_checkconstraint_constructor_args():
    sig = inspect.signature(CWMRelationalData_CheckConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cwmrelationaldata_queryexpression_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_QueryExpression)


def test_cwmrelationaldata_queryexpression_constructor_exists():
    assert callable(CWMRelationalData_QueryExpression.__init__)


def test_cwmrelationaldata_queryexpression_constructor_args():
    sig = inspect.signature(CWMRelationalData_QueryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expresssion" in params, "Missing parameter 'expresssion'"

def test_cwmrelationaldata_queryexpression_has_expresssion():
    assert hasattr(CWMRelationalData_QueryExpression, "expresssion")
    descriptor = None
    for klass in CWMRelationalData_QueryExpression.__mro__:
        if "expresssion" in klass.__dict__:
            descriptor = klass.__dict__["expresssion"]
            break
    assert isinstance(descriptor, property)



def test_cwmrelationaldata_column_is_not_abstract():
    assert not inspect.isabstract(CWMRelationalData_Column)


def test_cwmrelationaldata_column_constructor_exists():
    assert callable(CWMRelationalData_Column.__init__)


def test_cwmrelationaldata_column_constructor_args():
    sig = inspect.signature(CWMRelationalData_Column.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "characterSetName" in params, "Missing parameter 'characterSetName'"
    assert "length" in params, "Missing parameter 'length'"
    assert "isNullable" in params, "Missing parameter 'isNullable'"
    assert "collectionName" in params, "Missing parameter 'collectionName'"

def test_cwmrelationaldata_column_has_precision():
    assert hasattr(CWMRelationalData_Column, "precision")
    descriptor = None
    for klass in CWMRelationalData_Column.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_column_has_scale():
    assert hasattr(CWMRelationalData_Column, "scale")
    descriptor = None
    for klass in CWMRelationalData_Column.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_column_has_characterSetName():
    assert hasattr(CWMRelationalData_Column, "characterSetName")
    descriptor = None
    for klass in CWMRelationalData_Column.__mro__:
        if "characterSetName" in klass.__dict__:
            descriptor = klass.__dict__["characterSetName"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_column_has_length():
    assert hasattr(CWMRelationalData_Column, "length")
    descriptor = None
    for klass in CWMRelationalData_Column.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_column_has_isNullable():
    assert hasattr(CWMRelationalData_Column, "isNullable")
    descriptor = None
    for klass in CWMRelationalData_Column.__mro__:
        if "isNullable" in klass.__dict__:
            descriptor = klass.__dict__["isNullable"]
            break
    assert isinstance(descriptor, property)

def test_cwmrelationaldata_column_has_collectionName():
    assert hasattr(CWMRelationalData_Column, "collectionName")
    descriptor = None
    for klass in CWMRelationalData_Column.__mro__:
        if "collectionName" in klass.__dict__:
            descriptor = klass.__dict__["collectionName"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
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
SQLDistinctType_strategy = st.builds(
    SQLDistinctType,
)
SQLSimpleType_strategy = st.builds(
    SQLSimpleType,
)
CWMRelationalData_SQLDataType_strategy = st.builds(
    CWMRelationalData_SQLDataType,
    typeNumber=
        safe_text
)
CWMRelationalData_Trigger_strategy = st.builds(
    CWMRelationalData_Trigger,
)
QueryExpression_strategy = st.builds(
    QueryExpression,
)
Trigger_strategy = st.builds(
    Trigger,
)
CWMRelationalData_ColumnSet_strategy = st.builds(
    CWMRelationalData_ColumnSet,
)
NamedColumnSet_strategy = st.builds(
    NamedColumnSet,
)
ColumnSet_strategy = st.builds(
    ColumnSet,
)
CWMRelationalData_NamedColumnSet_strategy = st.builds(
    CWMRelationalData_NamedColumnSet,
)
CWMRelationalData_QueryColumnSet_strategy = st.builds(
    CWMRelationalData_QueryColumnSet,
)
SQLDataType_strategy = st.builds(
    SQLDataType,
)
CWMRelationalData_SQLSimpleType_strategy = st.builds(
    CWMRelationalData_SQLSimpleType,
    numericScale=
        safe_text,
    characterOctetLength=
        safe_text,
    characterMaximumLength=
        safe_text,
    numericPrecisionRadix=
        safe_text,
    dateTimePrecision=
        safe_text,
    numericPrecision=
        safe_text
)
CWMRelationalData_SQLDistinctType_strategy = st.builds(
    CWMRelationalData_SQLDistinctType,
    length=
        safe_text,
    precision=
        safe_text,
    scale=
        safe_text
)
CheckConstraint_strategy = st.builds(
    CheckConstraint,
)
CWMRelationalData_View_strategy = st.builds(
    CWMRelationalData_View,
    checkOption=
        safe_text,
    isReadOnly=
        safe_text
)
CWMRelationalData_Table_strategy = st.builds(
    CWMRelationalData_Table,
    isTemporary=
        safe_text,
    temporaryScope=
        safe_text,
    isSystem=
        safe_text
)
CWMRelationalData_CheckConstraint_strategy = st.builds(
    CWMRelationalData_CheckConstraint,
)
CWMRelationalData_QueryExpression_strategy = st.builds(
    CWMRelationalData_QueryExpression,
    expresssion=
        safe_text
)
CWMRelationalData_Column_strategy = st.builds(
    CWMRelationalData_Column,
    precision=
        safe_text,
    scale=
        safe_text,
    characterSetName=
        safe_text,
    length=
        safe_text,
    isNullable=
        safe_text,
    collectionName=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
Column_strategy = st.builds(
    Column,
)

@given(instance=SQLDistinctType_strategy)
@settings(max_examples=50)
def test_sqldistincttype_instantiation(instance):
    assert isinstance(instance, SQLDistinctType)

@given(instance=SQLSimpleType_strategy)
@settings(max_examples=50)
def test_sqlsimpletype_instantiation(instance):
    assert isinstance(instance, SQLSimpleType)

@given(instance=CWMRelationalData_SQLDataType_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_sqldatatype_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_SQLDataType)



@given(instance=CWMRelationalData_SQLDataType_strategy)
def test_cwmrelationaldata_sqldatatype_typeNumber_setter(instance):
    original = instance.typeNumber
    instance.typeNumber = original
    assert instance.typeNumber == original

@given(instance=CWMRelationalData_Trigger_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_trigger_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_Trigger)

@given(instance=QueryExpression_strategy)
@settings(max_examples=50)
def test_queryexpression_instantiation(instance):
    assert isinstance(instance, QueryExpression)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=CWMRelationalData_ColumnSet_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_columnset_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_ColumnSet)

@given(instance=NamedColumnSet_strategy)
@settings(max_examples=50)
def test_namedcolumnset_instantiation(instance):
    assert isinstance(instance, NamedColumnSet)

@given(instance=ColumnSet_strategy)
@settings(max_examples=50)
def test_columnset_instantiation(instance):
    assert isinstance(instance, ColumnSet)

@given(instance=CWMRelationalData_NamedColumnSet_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_namedcolumnset_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_NamedColumnSet)

@given(instance=CWMRelationalData_QueryColumnSet_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_querycolumnset_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_QueryColumnSet)

@given(instance=SQLDataType_strategy)
@settings(max_examples=50)
def test_sqldatatype_instantiation(instance):
    assert isinstance(instance, SQLDataType)

@given(instance=CWMRelationalData_SQLSimpleType_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_sqlsimpletype_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_SQLSimpleType)



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_cwmrelationaldata_sqlsimpletype_numericScale_setter(instance):
    original = instance.numericScale
    instance.numericScale = original
    assert instance.numericScale == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_cwmrelationaldata_sqlsimpletype_characterOctetLength_setter(instance):
    original = instance.characterOctetLength
    instance.characterOctetLength = original
    assert instance.characterOctetLength == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_cwmrelationaldata_sqlsimpletype_characterMaximumLength_setter(instance):
    original = instance.characterMaximumLength
    instance.characterMaximumLength = original
    assert instance.characterMaximumLength == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_cwmrelationaldata_sqlsimpletype_numericPrecisionRadix_setter(instance):
    original = instance.numericPrecisionRadix
    instance.numericPrecisionRadix = original
    assert instance.numericPrecisionRadix == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_cwmrelationaldata_sqlsimpletype_dateTimePrecision_setter(instance):
    original = instance.dateTimePrecision
    instance.dateTimePrecision = original
    assert instance.dateTimePrecision == original



@given(instance=CWMRelationalData_SQLSimpleType_strategy)
def test_cwmrelationaldata_sqlsimpletype_numericPrecision_setter(instance):
    original = instance.numericPrecision
    instance.numericPrecision = original
    assert instance.numericPrecision == original

@given(instance=CWMRelationalData_SQLDistinctType_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_sqldistincttype_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_SQLDistinctType)



@given(instance=CWMRelationalData_SQLDistinctType_strategy)
def test_cwmrelationaldata_sqldistincttype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=CWMRelationalData_SQLDistinctType_strategy)
def test_cwmrelationaldata_sqldistincttype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=CWMRelationalData_SQLDistinctType_strategy)
def test_cwmrelationaldata_sqldistincttype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=CheckConstraint_strategy)
@settings(max_examples=50)
def test_checkconstraint_instantiation(instance):
    assert isinstance(instance, CheckConstraint)

@given(instance=CWMRelationalData_View_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_view_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_View)



@given(instance=CWMRelationalData_View_strategy)
def test_cwmrelationaldata_view_checkOption_setter(instance):
    original = instance.checkOption
    instance.checkOption = original
    assert instance.checkOption == original



@given(instance=CWMRelationalData_View_strategy)
def test_cwmrelationaldata_view_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=CWMRelationalData_Table_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_table_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_Table)



@given(instance=CWMRelationalData_Table_strategy)
def test_cwmrelationaldata_table_isTemporary_setter(instance):
    original = instance.isTemporary
    instance.isTemporary = original
    assert instance.isTemporary == original



@given(instance=CWMRelationalData_Table_strategy)
def test_cwmrelationaldata_table_temporaryScope_setter(instance):
    original = instance.temporaryScope
    instance.temporaryScope = original
    assert instance.temporaryScope == original



@given(instance=CWMRelationalData_Table_strategy)
def test_cwmrelationaldata_table_isSystem_setter(instance):
    original = instance.isSystem
    instance.isSystem = original
    assert instance.isSystem == original

@given(instance=CWMRelationalData_CheckConstraint_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_checkconstraint_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_CheckConstraint)

@given(instance=CWMRelationalData_QueryExpression_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_queryexpression_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_QueryExpression)



@given(instance=CWMRelationalData_QueryExpression_strategy)
def test_cwmrelationaldata_queryexpression_expresssion_setter(instance):
    original = instance.expresssion
    instance.expresssion = original
    assert instance.expresssion == original

@given(instance=CWMRelationalData_Column_strategy)
@settings(max_examples=50)
def test_cwmrelationaldata_column_instantiation(instance):
    assert isinstance(instance, CWMRelationalData_Column)



@given(instance=CWMRelationalData_Column_strategy)
def test_cwmrelationaldata_column_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=CWMRelationalData_Column_strategy)
def test_cwmrelationaldata_column_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=CWMRelationalData_Column_strategy)
def test_cwmrelationaldata_column_characterSetName_setter(instance):
    original = instance.characterSetName
    instance.characterSetName = original
    assert instance.characterSetName == original



@given(instance=CWMRelationalData_Column_strategy)
def test_cwmrelationaldata_column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=CWMRelationalData_Column_strategy)
def test_cwmrelationaldata_column_isNullable_setter(instance):
    original = instance.isNullable
    instance.isNullable = original
    assert instance.isNullable == original



@given(instance=CWMRelationalData_Column_strategy)
def test_cwmrelationaldata_column_collectionName_setter(instance):
    original = instance.collectionName
    instance.collectionName = original
    assert instance.collectionName == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)
