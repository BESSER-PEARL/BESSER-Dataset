import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Feature,
    SQL2003_V2_DatetimeFeature,
    Restriction,
    SQL2003_V2_ColumnConstraint,
    SQL2003_V2_Table,
    SQL2003_V2_DataType,
    ConstructedType,
    SQL2003_V2_CollectionType,
    PredefinedType,
    SQL2003_V2_DatetimeType,
    SQL2003_V2_BooleanType,
    SQL2003_V2_CharacterStringType,
    SQL2003_V2_BinaryStringType,
    SQL2003_V2_Schema,
    SQL2003_V2_BehaviouralComponent,
    Table,
    SQL2003_V2_BaseTable,
    StructuralComponent,
    SQL2003_V2_Column,
    DerivedTable,
    SQL2003_V2_XMLType,
    BaseTable,
    SQL2003_V2_TriggerDescriptor,
    SQL2003_V2_Trigger,
    SQL2003_V2_TableConstraint,
    SQL2003_V2_TypedTable,
    SQL2003_V2_View,
    SQL2003_V2_StringFeature,
    SQL2003_V2_Domain,
    SQL2003_V2_StructuralComponent,
    SQL2003_V2_Restriction,
    TableConstraint,
    SQL2003_V2_UniqueConstraint,
    SQL2003_V2_TableCheckConstraint,
    SQL2003_V2_ReferentialConstraint,
    SQL2003_V2_ReferenceType,
    UniqueConstraint,
    SQL2003_V2_PrimaryKey,
    SQL2003_V2_Parameter,
    SQL2003_V2_NumericType,
    SQL2003_V2_NumericFeature,
    ColumnConstraint,
    SQL2003_V2_NotNull,
    Parameter,
    SQL2003_V2_ParameterWithMode,
    SQL2003_V2_MethodParameter,
    SQL2003_V2_Method,
    SQL2003_V2_IntervalType,
    SQL2003_V2_IntervalFeature,
    BehaviouralComponent,
    SQL2003_V2_Procedure,
    SQL2003_V2_Function,
    SQL2003_V2_ROW,
    SQL2003_V2_Field,
    SQL2003_V2_Feature,
    UserDefinedType,
    SQL2003_V2_StructuredType,
    SQL2003_V2_DistinctType,
    SQL2003_V2_DerivedTable,
    DataType,
    SQL2003_V2_UserDefinedType,
    SQL2003_V2_PredefinedType,
    SQL2003_V2_ConstructedType,
    SQL2003_V2_Attribute,
    CollectionType,
    SQL2003_V2_MULTISET,
    SQL2003_V2_ARRAY,
    MatchTypes,
    DatetimeTypes,
    NumericFeatures,
    TriggerLevel,
    CharacterStringTypes,
    ReferentialAction,
    IntervalTypes,
    BinaryStringTypes,
    Multiplier,
    NumericRadix,
    IntervalFeatures,
    StringFeatures,
    XMLTypes,
    ParameterMode,
    NumericTypes,
    DatetimeFeatures,
    TriggerActionTime,
    BooleanTypes,
    Unit,
    TriggerEvent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_datetimefeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_DatetimeFeature)


def test_sql2003_v2_datetimefeature_constructor_exists():
    assert callable(SQL2003_V2_DatetimeFeature.__init__)


def test_sql2003_v2_datetimefeature_constructor_args():
    sig = inspect.signature(SQL2003_V2_DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_v2_datetimefeature_has_key():
    assert hasattr(SQL2003_V2_DatetimeFeature, "key")
    descriptor = None
    for klass in SQL2003_V2_DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_datetimefeature_has_value():
    assert hasattr(SQL2003_V2_DatetimeFeature, "value")
    descriptor = None
    for klass in SQL2003_V2_DatetimeFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_restriction_is_not_abstract():
    assert not inspect.isabstract(Restriction)


def test_restriction_constructor_exists():
    assert callable(Restriction.__init__)


def test_restriction_constructor_args():
    sig = inspect.signature(Restriction.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ColumnConstraint)


def test_sql2003_v2_columnconstraint_constructor_exists():
    assert callable(SQL2003_V2_ColumnConstraint.__init__)


def test_sql2003_v2_columnconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V2_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_table_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Table)


def test_sql2003_v2_table_constructor_exists():
    assert callable(SQL2003_V2_Table.__init__)


def test_sql2003_v2_table_constructor_args():
    sig = inspect.signature(SQL2003_V2_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_table_has_name():
    assert hasattr(SQL2003_V2_Table, "name")
    descriptor = None
    for klass in SQL2003_V2_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_datatype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_DataType)


def test_sql2003_v2_datatype_constructor_exists():
    assert callable(SQL2003_V2_DataType.__init__)


def test_sql2003_v2_datatype_constructor_args():
    sig = inspect.signature(SQL2003_V2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_collectiontype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_CollectionType)


def test_sql2003_v2_collectiontype_constructor_exists():
    assert callable(SQL2003_V2_CollectionType.__init__)


def test_sql2003_v2_collectiontype_constructor_args():
    sig = inspect.signature(SQL2003_V2_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_DatetimeType)


def test_sql2003_v2_datetimetype_constructor_exists():
    assert callable(SQL2003_V2_DatetimeType.__init__)


def test_sql2003_v2_datetimetype_constructor_args():
    sig = inspect.signature(SQL2003_V2_DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v2_datetimetype_has_descriptor():
    assert hasattr(SQL2003_V2_DatetimeType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_DatetimeType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_booleantype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_BooleanType)


def test_sql2003_v2_booleantype_constructor_exists():
    assert callable(SQL2003_V2_BooleanType.__init__)


def test_sql2003_v2_booleantype_constructor_args():
    sig = inspect.signature(SQL2003_V2_BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v2_booleantype_has_descriptor():
    assert hasattr(SQL2003_V2_BooleanType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_BooleanType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_CharacterStringType)


def test_sql2003_v2_characterstringtype_constructor_exists():
    assert callable(SQL2003_V2_CharacterStringType.__init__)


def test_sql2003_v2_characterstringtype_constructor_args():
    sig = inspect.signature(SQL2003_V2_CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "length_def" in params, "Missing parameter 'length_def'"

def test_sql2003_v2_characterstringtype_has_descriptor():
    assert hasattr(SQL2003_V2_CharacterStringType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_CharacterStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_characterstringtype_has_length_def():
    assert hasattr(SQL2003_V2_CharacterStringType, "length_def")
    descriptor = None
    for klass in SQL2003_V2_CharacterStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_binarystringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_BinaryStringType)


def test_sql2003_v2_binarystringtype_constructor_exists():
    assert callable(SQL2003_V2_BinaryStringType.__init__)


def test_sql2003_v2_binarystringtype_constructor_args():
    sig = inspect.signature(SQL2003_V2_BinaryStringType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "length_def" in params, "Missing parameter 'length_def'"

def test_sql2003_v2_binarystringtype_has_descriptor():
    assert hasattr(SQL2003_V2_BinaryStringType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_BinaryStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_binarystringtype_has_length_def():
    assert hasattr(SQL2003_V2_BinaryStringType, "length_def")
    descriptor = None
    for klass in SQL2003_V2_BinaryStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_schema_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Schema)


def test_sql2003_v2_schema_constructor_exists():
    assert callable(SQL2003_V2_Schema.__init__)


def test_sql2003_v2_schema_constructor_args():
    sig = inspect.signature(SQL2003_V2_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_schema_has_name():
    assert hasattr(SQL2003_V2_Schema, "name")
    descriptor = None
    for klass in SQL2003_V2_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_BehaviouralComponent)


def test_sql2003_v2_behaviouralcomponent_constructor_exists():
    assert callable(SQL2003_V2_BehaviouralComponent.__init__)


def test_sql2003_v2_behaviouralcomponent_constructor_args():
    sig = inspect.signature(SQL2003_V2_BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003_v2_behaviouralcomponent_has_name():
    assert hasattr(SQL2003_V2_BehaviouralComponent, "name")
    descriptor = None
    for klass in SQL2003_V2_BehaviouralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_behaviouralcomponent_has_body():
    assert hasattr(SQL2003_V2_BehaviouralComponent, "body")
    descriptor = None
    for klass in SQL2003_V2_BehaviouralComponent.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_basetable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_BaseTable)


def test_sql2003_v2_basetable_constructor_exists():
    assert callable(SQL2003_V2_BaseTable.__init__)


def test_sql2003_v2_basetable_constructor_args():
    sig = inspect.signature(SQL2003_V2_BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(StructuralComponent)


def test_structuralcomponent_constructor_exists():
    assert callable(StructuralComponent.__init__)


def test_structuralcomponent_constructor_args():
    sig = inspect.signature(StructuralComponent.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_column_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Column)


def test_sql2003_v2_column_constructor_exists():
    assert callable(SQL2003_V2_Column.__init__)


def test_sql2003_v2_column_constructor_args():
    sig = inspect.signature(SQL2003_V2_Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_v2_column_has_default():
    assert hasattr(SQL2003_V2_Column, "default")
    descriptor = None
    for klass in SQL2003_V2_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_derivedtable_is_not_abstract():
    assert not inspect.isabstract(DerivedTable)


def test_derivedtable_constructor_exists():
    assert callable(DerivedTable.__init__)


def test_derivedtable_constructor_args():
    sig = inspect.signature(DerivedTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_xmltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_XMLType)


def test_sql2003_v2_xmltype_constructor_exists():
    assert callable(SQL2003_V2_XMLType.__init__)


def test_sql2003_v2_xmltype_constructor_args():
    sig = inspect.signature(SQL2003_V2_XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v2_xmltype_has_descriptor():
    assert hasattr(SQL2003_V2_XMLType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_XMLType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_basetable_is_not_abstract():
    assert not inspect.isabstract(BaseTable)


def test_basetable_constructor_exists():
    assert callable(BaseTable.__init__)


def test_basetable_constructor_args():
    sig = inspect.signature(BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_triggerdescriptor_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_TriggerDescriptor)


def test_sql2003_v2_triggerdescriptor_constructor_exists():
    assert callable(SQL2003_V2_TriggerDescriptor.__init__)


def test_sql2003_v2_triggerdescriptor_constructor_args():
    sig = inspect.signature(SQL2003_V2_TriggerDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "triggeredAction" in params, "Missing parameter 'triggeredAction'"
    assert "event" in params, "Missing parameter 'event'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"

def test_sql2003_v2_triggerdescriptor_has_level():
    assert hasattr(SQL2003_V2_TriggerDescriptor, "level")
    descriptor = None
    for klass in SQL2003_V2_TriggerDescriptor.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_triggerdescriptor_has_triggeredAction():
    assert hasattr(SQL2003_V2_TriggerDescriptor, "triggeredAction")
    descriptor = None
    for klass in SQL2003_V2_TriggerDescriptor.__mro__:
        if "triggeredAction" in klass.__dict__:
            descriptor = klass.__dict__["triggeredAction"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_triggerdescriptor_has_event():
    assert hasattr(SQL2003_V2_TriggerDescriptor, "event")
    descriptor = None
    for klass in SQL2003_V2_TriggerDescriptor.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_triggerdescriptor_has_actionTime():
    assert hasattr(SQL2003_V2_TriggerDescriptor, "actionTime")
    descriptor = None
    for klass in SQL2003_V2_TriggerDescriptor.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_trigger_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Trigger)


def test_sql2003_v2_trigger_constructor_exists():
    assert callable(SQL2003_V2_Trigger.__init__)


def test_sql2003_v2_trigger_constructor_args():
    sig = inspect.signature(SQL2003_V2_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_trigger_has_name():
    assert hasattr(SQL2003_V2_Trigger, "name")
    descriptor = None
    for klass in SQL2003_V2_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_TableConstraint)


def test_sql2003_v2_tableconstraint_constructor_exists():
    assert callable(SQL2003_V2_TableConstraint.__init__)


def test_sql2003_v2_tableconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V2_TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_tableconstraint_has_name():
    assert hasattr(SQL2003_V2_TableConstraint, "name")
    descriptor = None
    for klass in SQL2003_V2_TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_typedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_TypedTable)


def test_sql2003_v2_typedtable_constructor_exists():
    assert callable(SQL2003_V2_TypedTable.__init__)


def test_sql2003_v2_typedtable_constructor_args():
    sig = inspect.signature(SQL2003_V2_TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_view_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_View)


def test_sql2003_v2_view_constructor_exists():
    assert callable(SQL2003_V2_View.__init__)


def test_sql2003_v2_view_constructor_args():
    sig = inspect.signature(SQL2003_V2_View.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_stringfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_StringFeature)


def test_sql2003_v2_stringfeature_constructor_exists():
    assert callable(SQL2003_V2_StringFeature.__init__)


def test_sql2003_v2_stringfeature_constructor_args():
    sig = inspect.signature(SQL2003_V2_StringFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_v2_stringfeature_has_key():
    assert hasattr(SQL2003_V2_StringFeature, "key")
    descriptor = None
    for klass in SQL2003_V2_StringFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_stringfeature_has_value():
    assert hasattr(SQL2003_V2_StringFeature, "value")
    descriptor = None
    for klass in SQL2003_V2_StringFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_domain_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Domain)


def test_sql2003_v2_domain_constructor_exists():
    assert callable(SQL2003_V2_Domain.__init__)


def test_sql2003_v2_domain_constructor_args():
    sig = inspect.signature(SQL2003_V2_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_v2_domain_has_expression():
    assert hasattr(SQL2003_V2_Domain, "expression")
    descriptor = None
    for klass in SQL2003_V2_Domain.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_domain_has_name():
    assert hasattr(SQL2003_V2_Domain, "name")
    descriptor = None
    for klass in SQL2003_V2_Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_domain_has_default():
    assert hasattr(SQL2003_V2_Domain, "default")
    descriptor = None
    for klass in SQL2003_V2_Domain.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_StructuralComponent)


def test_sql2003_v2_structuralcomponent_constructor_exists():
    assert callable(SQL2003_V2_StructuralComponent.__init__)


def test_sql2003_v2_structuralcomponent_constructor_args():
    sig = inspect.signature(SQL2003_V2_StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_structuralcomponent_has_name():
    assert hasattr(SQL2003_V2_StructuralComponent, "name")
    descriptor = None
    for klass in SQL2003_V2_StructuralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_restriction_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Restriction)


def test_sql2003_v2_restriction_constructor_exists():
    assert callable(SQL2003_V2_Restriction.__init__)


def test_sql2003_v2_restriction_constructor_args():
    sig = inspect.signature(SQL2003_V2_Restriction.__init__)
    params = list(sig.parameters.keys())



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_UniqueConstraint)


def test_sql2003_v2_uniqueconstraint_constructor_exists():
    assert callable(SQL2003_V2_UniqueConstraint.__init__)


def test_sql2003_v2_uniqueconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V2_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_tablecheckconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_TableCheckConstraint)


def test_sql2003_v2_tablecheckconstraint_constructor_exists():
    assert callable(SQL2003_V2_TableCheckConstraint.__init__)


def test_sql2003_v2_tablecheckconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V2_TableCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sql2003_v2_tablecheckconstraint_has_expression():
    assert hasattr(SQL2003_V2_TableCheckConstraint, "expression")
    descriptor = None
    for klass in SQL2003_V2_TableCheckConstraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ReferentialConstraint)


def test_sql2003_v2_referentialconstraint_constructor_exists():
    assert callable(SQL2003_V2_ReferentialConstraint.__init__)


def test_sql2003_v2_referentialconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V2_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "match" in params, "Missing parameter 'match'"
    assert "delete_action" in params, "Missing parameter 'delete_action'"
    assert "update_action" in params, "Missing parameter 'update_action'"

def test_sql2003_v2_referentialconstraint_has_match():
    assert hasattr(SQL2003_V2_ReferentialConstraint, "match")
    descriptor = None
    for klass in SQL2003_V2_ReferentialConstraint.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_referentialconstraint_has_delete_action():
    assert hasattr(SQL2003_V2_ReferentialConstraint, "delete_action")
    descriptor = None
    for klass in SQL2003_V2_ReferentialConstraint.__mro__:
        if "delete_action" in klass.__dict__:
            descriptor = klass.__dict__["delete_action"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_referentialconstraint_has_update_action():
    assert hasattr(SQL2003_V2_ReferentialConstraint, "update_action")
    descriptor = None
    for klass in SQL2003_V2_ReferentialConstraint.__mro__:
        if "update_action" in klass.__dict__:
            descriptor = klass.__dict__["update_action"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_referencetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ReferenceType)


def test_sql2003_v2_referencetype_constructor_exists():
    assert callable(SQL2003_V2_ReferenceType.__init__)


def test_sql2003_v2_referencetype_constructor_args():
    sig = inspect.signature(SQL2003_V2_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_primarykey_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_PrimaryKey)


def test_sql2003_v2_primarykey_constructor_exists():
    assert callable(SQL2003_V2_PrimaryKey.__init__)


def test_sql2003_v2_primarykey_constructor_args():
    sig = inspect.signature(SQL2003_V2_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_parameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Parameter)


def test_sql2003_v2_parameter_constructor_exists():
    assert callable(SQL2003_V2_Parameter.__init__)


def test_sql2003_v2_parameter_constructor_args():
    sig = inspect.signature(SQL2003_V2_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_parameter_has_name():
    assert hasattr(SQL2003_V2_Parameter, "name")
    descriptor = None
    for klass in SQL2003_V2_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_numerictype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_NumericType)


def test_sql2003_v2_numerictype_constructor_exists():
    assert callable(SQL2003_V2_NumericType.__init__)


def test_sql2003_v2_numerictype_constructor_args():
    sig = inspect.signature(SQL2003_V2_NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v2_numerictype_has_descriptor():
    assert hasattr(SQL2003_V2_NumericType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_NumericType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_numericfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_NumericFeature)


def test_sql2003_v2_numericfeature_constructor_exists():
    assert callable(SQL2003_V2_NumericFeature.__init__)


def test_sql2003_v2_numericfeature_constructor_args():
    sig = inspect.signature(SQL2003_V2_NumericFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_v2_numericfeature_has_key():
    assert hasattr(SQL2003_V2_NumericFeature, "key")
    descriptor = None
    for klass in SQL2003_V2_NumericFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_numericfeature_has_value():
    assert hasattr(SQL2003_V2_NumericFeature, "value")
    descriptor = None
    for klass in SQL2003_V2_NumericFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_notnull_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_NotNull)


def test_sql2003_v2_notnull_constructor_exists():
    assert callable(SQL2003_V2_NotNull.__init__)


def test_sql2003_v2_notnull_constructor_args():
    sig = inspect.signature(SQL2003_V2_NotNull.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_parameterwithmode_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ParameterWithMode)


def test_sql2003_v2_parameterwithmode_constructor_exists():
    assert callable(SQL2003_V2_ParameterWithMode.__init__)


def test_sql2003_v2_parameterwithmode_constructor_args():
    sig = inspect.signature(SQL2003_V2_ParameterWithMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sql2003_v2_parameterwithmode_has_mode():
    assert hasattr(SQL2003_V2_ParameterWithMode, "mode")
    descriptor = None
    for klass in SQL2003_V2_ParameterWithMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_methodparameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_MethodParameter)


def test_sql2003_v2_methodparameter_constructor_exists():
    assert callable(SQL2003_V2_MethodParameter.__init__)


def test_sql2003_v2_methodparameter_constructor_args():
    sig = inspect.signature(SQL2003_V2_MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_method_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Method)


def test_sql2003_v2_method_constructor_exists():
    assert callable(SQL2003_V2_Method.__init__)


def test_sql2003_v2_method_constructor_args():
    sig = inspect.signature(SQL2003_V2_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003_v2_method_has_name():
    assert hasattr(SQL2003_V2_Method, "name")
    descriptor = None
    for klass in SQL2003_V2_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_method_has_body():
    assert hasattr(SQL2003_V2_Method, "body")
    descriptor = None
    for klass in SQL2003_V2_Method.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_intervaltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_IntervalType)


def test_sql2003_v2_intervaltype_constructor_exists():
    assert callable(SQL2003_V2_IntervalType.__init__)


def test_sql2003_v2_intervaltype_constructor_args():
    sig = inspect.signature(SQL2003_V2_IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v2_intervaltype_has_descriptor():
    assert hasattr(SQL2003_V2_IntervalType, "descriptor")
    descriptor = None
    for klass in SQL2003_V2_IntervalType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_intervalfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_IntervalFeature)


def test_sql2003_v2_intervalfeature_constructor_exists():
    assert callable(SQL2003_V2_IntervalFeature.__init__)


def test_sql2003_v2_intervalfeature_constructor_args():
    sig = inspect.signature(SQL2003_V2_IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_v2_intervalfeature_has_key():
    assert hasattr(SQL2003_V2_IntervalFeature, "key")
    descriptor = None
    for klass in SQL2003_V2_IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_intervalfeature_has_value():
    assert hasattr(SQL2003_V2_IntervalFeature, "value")
    descriptor = None
    for klass in SQL2003_V2_IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(BehaviouralComponent)


def test_behaviouralcomponent_constructor_exists():
    assert callable(BehaviouralComponent.__init__)


def test_behaviouralcomponent_constructor_args():
    sig = inspect.signature(BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_procedure_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Procedure)


def test_sql2003_v2_procedure_constructor_exists():
    assert callable(SQL2003_V2_Procedure.__init__)


def test_sql2003_v2_procedure_constructor_args():
    sig = inspect.signature(SQL2003_V2_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_function_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Function)


def test_sql2003_v2_function_constructor_exists():
    assert callable(SQL2003_V2_Function.__init__)


def test_sql2003_v2_function_constructor_args():
    sig = inspect.signature(SQL2003_V2_Function.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_row_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ROW)


def test_sql2003_v2_row_constructor_exists():
    assert callable(SQL2003_V2_ROW.__init__)


def test_sql2003_v2_row_constructor_args():
    sig = inspect.signature(SQL2003_V2_ROW.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_field_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Field)


def test_sql2003_v2_field_constructor_exists():
    assert callable(SQL2003_V2_Field.__init__)


def test_sql2003_v2_field_constructor_args():
    sig = inspect.signature(SQL2003_V2_Field.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_feature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Feature)


def test_sql2003_v2_feature_constructor_exists():
    assert callable(SQL2003_V2_Feature.__init__)


def test_sql2003_v2_feature_constructor_args():
    sig = inspect.signature(SQL2003_V2_Feature.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_structuredtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_StructuredType)


def test_sql2003_v2_structuredtype_constructor_exists():
    assert callable(SQL2003_V2_StructuredType.__init__)


def test_sql2003_v2_structuredtype_constructor_args():
    sig = inspect.signature(SQL2003_V2_StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_final" in params, "Missing parameter 'is_final'"
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"

def test_sql2003_v2_structuredtype_has_is_final():
    assert hasattr(SQL2003_V2_StructuredType, "is_final")
    descriptor = None
    for klass in SQL2003_V2_StructuredType.__mro__:
        if "is_final" in klass.__dict__:
            descriptor = klass.__dict__["is_final"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v2_structuredtype_has_is_instantiable():
    assert hasattr(SQL2003_V2_StructuredType, "is_instantiable")
    descriptor = None
    for klass in SQL2003_V2_StructuredType.__mro__:
        if "is_instantiable" in klass.__dict__:
            descriptor = klass.__dict__["is_instantiable"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_distincttype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_DistinctType)


def test_sql2003_v2_distincttype_constructor_exists():
    assert callable(SQL2003_V2_DistinctType.__init__)


def test_sql2003_v2_distincttype_constructor_args():
    sig = inspect.signature(SQL2003_V2_DistinctType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_derivedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_DerivedTable)


def test_sql2003_v2_derivedtable_constructor_exists():
    assert callable(SQL2003_V2_DerivedTable.__init__)


def test_sql2003_v2_derivedtable_constructor_args():
    sig = inspect.signature(SQL2003_V2_DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_sql2003_v2_derivedtable_has_query_expression():
    assert hasattr(SQL2003_V2_DerivedTable, "query_expression")
    descriptor = None
    for klass in SQL2003_V2_DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_UserDefinedType)


def test_sql2003_v2_userdefinedtype_constructor_exists():
    assert callable(SQL2003_V2_UserDefinedType.__init__)


def test_sql2003_v2_userdefinedtype_constructor_args():
    sig = inspect.signature(SQL2003_V2_UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_userdefinedtype_has_name():
    assert hasattr(SQL2003_V2_UserDefinedType, "name")
    descriptor = None
    for klass in SQL2003_V2_UserDefinedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_PredefinedType)


def test_sql2003_v2_predefinedtype_constructor_exists():
    assert callable(SQL2003_V2_PredefinedType.__init__)


def test_sql2003_v2_predefinedtype_constructor_args():
    sig = inspect.signature(SQL2003_V2_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_constructedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ConstructedType)


def test_sql2003_v2_constructedtype_constructor_exists():
    assert callable(SQL2003_V2_ConstructedType.__init__)


def test_sql2003_v2_constructedtype_constructor_args():
    sig = inspect.signature(SQL2003_V2_ConstructedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v2_constructedtype_has_name():
    assert hasattr(SQL2003_V2_ConstructedType, "name")
    descriptor = None
    for klass in SQL2003_V2_ConstructedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v2_attribute_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_Attribute)


def test_sql2003_v2_attribute_constructor_exists():
    assert callable(SQL2003_V2_Attribute.__init__)


def test_sql2003_v2_attribute_constructor_args():
    sig = inspect.signature(SQL2003_V2_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_v2_attribute_has_default():
    assert hasattr(SQL2003_V2_Attribute, "default")
    descriptor = None
    for klass in SQL2003_V2_Attribute.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_multiset_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_MULTISET)


def test_sql2003_v2_multiset_constructor_exists():
    assert callable(SQL2003_V2_MULTISET.__init__)


def test_sql2003_v2_multiset_constructor_args():
    sig = inspect.signature(SQL2003_V2_MULTISET.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v2_array_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V2_ARRAY)


def test_sql2003_v2_array_constructor_exists():
    assert callable(SQL2003_V2_ARRAY.__init__)


def test_sql2003_v2_array_constructor_args():
    sig = inspect.signature(SQL2003_V2_ARRAY.__init__)
    params = list(sig.parameters.keys())
    assert "num_elements" in params, "Missing parameter 'num_elements'"

def test_sql2003_v2_array_has_num_elements():
    assert hasattr(SQL2003_V2_ARRAY, "num_elements")
    descriptor = None
    for klass in SQL2003_V2_ARRAY.__mro__:
        if "num_elements" in klass.__dict__:
            descriptor = klass.__dict__["num_elements"]
            break
    assert isinstance(descriptor, property)

def test_matchtypes_exists():
    # Check that the Enumeration exists
    assert MatchTypes is not None

def test_matchtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatchTypes]
    expected_literals = [
        "PARTIAL",
        "SIMPLE",
        "TOTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchTypes"

def test_datetimetypes_exists():
    # Check that the Enumeration exists
    assert DatetimeTypes is not None

def test_datetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeTypes]
    expected_literals = [
        "TIMEWITHOUTTIMEZONE",
        "TIMEWITHTIMEZONE",
        "DATE",
        "TIMESTAMPWITHTIMEZONE",
        "TIMESTAMPWITHOUTTIMEZONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeTypes"

def test_numericfeatures_exists():
    # Check that the Enumeration exists
    assert NumericFeatures is not None

def test_numericfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericFeatures]
    expected_literals = [
        "scale",
        "radix",
        "precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericFeatures"

def test_triggerlevel_exists():
    # Check that the Enumeration exists
    assert TriggerLevel is not None

def test_triggerlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerLevel]
    expected_literals = [
        "ROW_LEVEL",
        "STATEMENT_LEVEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerLevel"

def test_characterstringtypes_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypes is not None

def test_characterstringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypes]
    expected_literals = [
        "CHARACTER",
        "CHARACTERLARGEOBJECT",
        "CHARACTERVARYING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypes"

def test_referentialaction_exists():
    # Check that the Enumeration exists
    assert ReferentialAction is not None

def test_referentialaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialAction]
    expected_literals = [
        "RESTRICT",
        "SET_DEFAULT",
        "CASCADE",
        "NO_ACTION",
        "SET_NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialAction"

def test_intervaltypes_exists():
    # Check that the Enumeration exists
    assert IntervalTypes is not None

def test_intervaltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalTypes]
    expected_literals = [
        "DAY_SECOND",
        "HOUR_SECOND",
        "HOUR_MINUTE",
        "DAY_HOUR",
        "YEAR",
        "DAY",
        "MINUTE_SECOND",
        "DAY_MINUTE",
        "YEAR_MONTH",
        "MONTH",
        "SECOND",
        "HOUR",
        "MINUTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalTypes"

def test_binarystringtypes_exists():
    # Check that the Enumeration exists
    assert BinaryStringTypes is not None

def test_binarystringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryStringTypes]
    expected_literals = [
        "BINARYVARYING",
        "BINARYLARGEOBJECT",
        "BINARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryStringTypes"

def test_multiplier_exists():
    # Check that the Enumeration exists
    assert Multiplier is not None

def test_multiplier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Multiplier]
    expected_literals = [
        "P",
        "M",
        "T",
        "K",
        "G",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_numericradix_exists():
    # Check that the Enumeration exists
    assert NumericRadix is not None

def test_numericradix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericRadix]
    expected_literals = [
        "BINARY",
        "DECIMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericRadix"

def test_intervalfeatures_exists():
    # Check that the Enumeration exists
    assert IntervalFeatures is not None

def test_intervalfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalFeatures]
    expected_literals = [
        "second_precision",
        "end_leading_precision",
        "start_leading_precision",
        "leading_precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalFeatures"

def test_stringfeatures_exists():
    # Check that the Enumeration exists
    assert StringFeatures is not None

def test_stringfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringFeatures]
    expected_literals = [
        "length",
        "unit",
        "multiplier",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringFeatures"

def test_xmltypes_exists():
    # Check that the Enumeration exists
    assert XMLTypes is not None

def test_xmltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XMLTypes]
    expected_literals = [
        "XMLTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XMLTypes"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "OUT",
        "INOUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

def test_numerictypes_exists():
    # Check that the Enumeration exists
    assert NumericTypes is not None

def test_numerictypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericTypes]
    expected_literals = [
        "SMALLINT",
        "INTEGER",
        "DOUBLEPRECISION",
        "NUMERIC",
        "DECIMAL",
        "FLOAT",
        "REAL",
        "BIGINT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericTypes"

def test_datetimefeatures_exists():
    # Check that the Enumeration exists
    assert DatetimeFeatures is not None

def test_datetimefeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeFeatures]
    expected_literals = [
        "precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeFeatures"

def test_triggeractiontime_exists():
    # Check that the Enumeration exists
    assert TriggerActionTime is not None

def test_triggeractiontime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerActionTime]
    expected_literals = [
        "BEFORE",
        "AFTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerActionTime"

def test_booleantypes_exists():
    # Check that the Enumeration exists
    assert BooleanTypes is not None

def test_booleantypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanTypes]
    expected_literals = [
        "BOOLEAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanTypes"

def test_unit_exists():
    # Check that the Enumeration exists
    assert Unit is not None

def test_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Unit]
    expected_literals = [
        "OCTETS",
        "CHARACTERS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Unit"

def test_triggerevent_exists():
    # Check that the Enumeration exists
    assert TriggerEvent is not None

def test_triggerevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerEvent]
    expected_literals = [
        "DELETE",
        "INSERT",
        "UPDATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerEvent"


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
Feature_strategy = st.builds(
    Feature,
)
SQL2003_V2_DatetimeFeature_strategy = st.builds(
    SQL2003_V2_DatetimeFeature,
    key=
        safe_text,
    value=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
SQL2003_V2_ColumnConstraint_strategy = st.builds(
    SQL2003_V2_ColumnConstraint,
)
SQL2003_V2_Table_strategy = st.builds(
    SQL2003_V2_Table,
    name=
        safe_text
)
SQL2003_V2_DataType_strategy = st.builds(
    SQL2003_V2_DataType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
SQL2003_V2_CollectionType_strategy = st.builds(
    SQL2003_V2_CollectionType,
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
SQL2003_V2_DatetimeType_strategy = st.builds(
    SQL2003_V2_DatetimeType,
    descriptor=
        safe_text
)
SQL2003_V2_BooleanType_strategy = st.builds(
    SQL2003_V2_BooleanType,
    descriptor=
        safe_text
)
SQL2003_V2_CharacterStringType_strategy = st.builds(
    SQL2003_V2_CharacterStringType,
    descriptor=
        safe_text,
    length_def=
        safe_text
)
SQL2003_V2_BinaryStringType_strategy = st.builds(
    SQL2003_V2_BinaryStringType,
    descriptor=
        safe_text,
    length_def=
        safe_text
)
SQL2003_V2_Schema_strategy = st.builds(
    SQL2003_V2_Schema,
    name=
        safe_text
)
SQL2003_V2_BehaviouralComponent_strategy = st.builds(
    SQL2003_V2_BehaviouralComponent,
    name=
        safe_text,
    body=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SQL2003_V2_BaseTable_strategy = st.builds(
    SQL2003_V2_BaseTable,
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
SQL2003_V2_Column_strategy = st.builds(
    SQL2003_V2_Column,
    default=
        safe_text
)
DerivedTable_strategy = st.builds(
    DerivedTable,
)
SQL2003_V2_XMLType_strategy = st.builds(
    SQL2003_V2_XMLType,
    descriptor=
        safe_text
)
BaseTable_strategy = st.builds(
    BaseTable,
)
SQL2003_V2_TriggerDescriptor_strategy = st.builds(
    SQL2003_V2_TriggerDescriptor,
    level=
        safe_text,
    triggeredAction=
        safe_text,
    event=
        safe_text,
    actionTime=
        safe_text
)
SQL2003_V2_Trigger_strategy = st.builds(
    SQL2003_V2_Trigger,
    name=
        safe_text
)
SQL2003_V2_TableConstraint_strategy = st.builds(
    SQL2003_V2_TableConstraint,
    name=
        safe_text
)
SQL2003_V2_TypedTable_strategy = st.builds(
    SQL2003_V2_TypedTable,
)
SQL2003_V2_View_strategy = st.builds(
    SQL2003_V2_View,
)
SQL2003_V2_StringFeature_strategy = st.builds(
    SQL2003_V2_StringFeature,
    key=
        safe_text,
    value=
        safe_text
)
SQL2003_V2_Domain_strategy = st.builds(
    SQL2003_V2_Domain,
    expression=
        safe_text,
    name=
        safe_text,
    default=
        safe_text
)
SQL2003_V2_StructuralComponent_strategy = st.builds(
    SQL2003_V2_StructuralComponent,
    name=
        safe_text
)
SQL2003_V2_Restriction_strategy = st.builds(
    SQL2003_V2_Restriction,
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
SQL2003_V2_UniqueConstraint_strategy = st.builds(
    SQL2003_V2_UniqueConstraint,
)
SQL2003_V2_TableCheckConstraint_strategy = st.builds(
    SQL2003_V2_TableCheckConstraint,
    expression=
        safe_text
)
SQL2003_V2_ReferentialConstraint_strategy = st.builds(
    SQL2003_V2_ReferentialConstraint,
    match=
        safe_text,
    delete_action=
        safe_text,
    update_action=
        safe_text
)
SQL2003_V2_ReferenceType_strategy = st.builds(
    SQL2003_V2_ReferenceType,
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
SQL2003_V2_PrimaryKey_strategy = st.builds(
    SQL2003_V2_PrimaryKey,
)
SQL2003_V2_Parameter_strategy = st.builds(
    SQL2003_V2_Parameter,
    name=
        safe_text
)
SQL2003_V2_NumericType_strategy = st.builds(
    SQL2003_V2_NumericType,
    descriptor=
        safe_text
)
SQL2003_V2_NumericFeature_strategy = st.builds(
    SQL2003_V2_NumericFeature,
    key=
        safe_text,
    value=
        safe_text
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
SQL2003_V2_NotNull_strategy = st.builds(
    SQL2003_V2_NotNull,
)
Parameter_strategy = st.builds(
    Parameter,
)
SQL2003_V2_ParameterWithMode_strategy = st.builds(
    SQL2003_V2_ParameterWithMode,
    mode=
        safe_text
)
SQL2003_V2_MethodParameter_strategy = st.builds(
    SQL2003_V2_MethodParameter,
)
SQL2003_V2_Method_strategy = st.builds(
    SQL2003_V2_Method,
    name=
        safe_text,
    body=
        safe_text
)
SQL2003_V2_IntervalType_strategy = st.builds(
    SQL2003_V2_IntervalType,
    descriptor=
        safe_text
)
SQL2003_V2_IntervalFeature_strategy = st.builds(
    SQL2003_V2_IntervalFeature,
    key=
        safe_text,
    value=
        safe_text
)
BehaviouralComponent_strategy = st.builds(
    BehaviouralComponent,
)
SQL2003_V2_Procedure_strategy = st.builds(
    SQL2003_V2_Procedure,
)
SQL2003_V2_Function_strategy = st.builds(
    SQL2003_V2_Function,
)
SQL2003_V2_ROW_strategy = st.builds(
    SQL2003_V2_ROW,
)
SQL2003_V2_Field_strategy = st.builds(
    SQL2003_V2_Field,
)
SQL2003_V2_Feature_strategy = st.builds(
    SQL2003_V2_Feature,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
SQL2003_V2_StructuredType_strategy = st.builds(
    SQL2003_V2_StructuredType,
    is_final=
        st.booleans(),
    is_instantiable=
        st.booleans()
)
SQL2003_V2_DistinctType_strategy = st.builds(
    SQL2003_V2_DistinctType,
)
SQL2003_V2_DerivedTable_strategy = st.builds(
    SQL2003_V2_DerivedTable,
    query_expression=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
SQL2003_V2_UserDefinedType_strategy = st.builds(
    SQL2003_V2_UserDefinedType,
    name=
        safe_text
)
SQL2003_V2_PredefinedType_strategy = st.builds(
    SQL2003_V2_PredefinedType,
)
SQL2003_V2_ConstructedType_strategy = st.builds(
    SQL2003_V2_ConstructedType,
    name=
        safe_text
)
SQL2003_V2_Attribute_strategy = st.builds(
    SQL2003_V2_Attribute,
    default=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
SQL2003_V2_MULTISET_strategy = st.builds(
    SQL2003_V2_MULTISET,
)
SQL2003_V2_ARRAY_strategy = st.builds(
    SQL2003_V2_ARRAY,
    num_elements=
        safe_text
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=SQL2003_V2_DatetimeFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v2_datetimefeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_DatetimeFeature)



@given(instance=SQL2003_V2_DatetimeFeature_strategy)
def test_sql2003_v2_datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_V2_DatetimeFeature_strategy)
def test_sql2003_v2_datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=SQL2003_V2_ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v2_columnconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ColumnConstraint)

@given(instance=SQL2003_V2_Table_strategy)
@settings(max_examples=50)
def test_sql2003_v2_table_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Table)



@given(instance=SQL2003_V2_Table_strategy)
def test_sql2003_v2_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_DataType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_datatype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_DataType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=SQL2003_V2_CollectionType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_collectiontype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_CollectionType)

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=SQL2003_V2_DatetimeType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_datetimetype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_DatetimeType)



@given(instance=SQL2003_V2_DatetimeType_strategy)
def test_sql2003_v2_datetimetype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V2_BooleanType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_booleantype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_BooleanType)



@given(instance=SQL2003_V2_BooleanType_strategy)
def test_sql2003_v2_booleantype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V2_CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_characterstringtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_CharacterStringType)



@given(instance=SQL2003_V2_CharacterStringType_strategy)
def test_sql2003_v2_characterstringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=SQL2003_V2_CharacterStringType_strategy)
def test_sql2003_v2_characterstringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003_V2_BinaryStringType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_binarystringtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_BinaryStringType)



@given(instance=SQL2003_V2_BinaryStringType_strategy)
def test_sql2003_v2_binarystringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=SQL2003_V2_BinaryStringType_strategy)
def test_sql2003_v2_binarystringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003_V2_Schema_strategy)
@settings(max_examples=50)
def test_sql2003_v2_schema_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Schema)



@given(instance=SQL2003_V2_Schema_strategy)
def test_sql2003_v2_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_sql2003_v2_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_BehaviouralComponent)



@given(instance=SQL2003_V2_BehaviouralComponent_strategy)
def test_sql2003_v2_behaviouralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SQL2003_V2_BehaviouralComponent_strategy)
def test_sql2003_v2_behaviouralcomponent_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SQL2003_V2_BaseTable_strategy)
@settings(max_examples=50)
def test_sql2003_v2_basetable_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_BaseTable)

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=SQL2003_V2_Column_strategy)
@settings(max_examples=50)
def test_sql2003_v2_column_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Column)



@given(instance=SQL2003_V2_Column_strategy)
def test_sql2003_v2_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=DerivedTable_strategy)
@settings(max_examples=50)
def test_derivedtable_instantiation(instance):
    assert isinstance(instance, DerivedTable)

@given(instance=SQL2003_V2_XMLType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_xmltype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_XMLType)



@given(instance=SQL2003_V2_XMLType_strategy)
def test_sql2003_v2_xmltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=BaseTable_strategy)
@settings(max_examples=50)
def test_basetable_instantiation(instance):
    assert isinstance(instance, BaseTable)

@given(instance=SQL2003_V2_TriggerDescriptor_strategy)
@settings(max_examples=50)
def test_sql2003_v2_triggerdescriptor_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_TriggerDescriptor)



@given(instance=SQL2003_V2_TriggerDescriptor_strategy)
def test_sql2003_v2_triggerdescriptor_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=SQL2003_V2_TriggerDescriptor_strategy)
def test_sql2003_v2_triggerdescriptor_triggeredAction_setter(instance):
    original = instance.triggeredAction
    instance.triggeredAction = original
    assert instance.triggeredAction == original



@given(instance=SQL2003_V2_TriggerDescriptor_strategy)
def test_sql2003_v2_triggerdescriptor_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=SQL2003_V2_TriggerDescriptor_strategy)
def test_sql2003_v2_triggerdescriptor_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original

@given(instance=SQL2003_V2_Trigger_strategy)
@settings(max_examples=50)
def test_sql2003_v2_trigger_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Trigger)



@given(instance=SQL2003_V2_Trigger_strategy)
def test_sql2003_v2_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_TableConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v2_tableconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_TableConstraint)



@given(instance=SQL2003_V2_TableConstraint_strategy)
def test_sql2003_v2_tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_TypedTable_strategy)
@settings(max_examples=50)
def test_sql2003_v2_typedtable_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_TypedTable)

@given(instance=SQL2003_V2_View_strategy)
@settings(max_examples=50)
def test_sql2003_v2_view_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_View)

@given(instance=SQL2003_V2_StringFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v2_stringfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_StringFeature)



@given(instance=SQL2003_V2_StringFeature_strategy)
def test_sql2003_v2_stringfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_V2_StringFeature_strategy)
def test_sql2003_v2_stringfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003_V2_Domain_strategy)
@settings(max_examples=50)
def test_sql2003_v2_domain_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Domain)



@given(instance=SQL2003_V2_Domain_strategy)
def test_sql2003_v2_domain_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=SQL2003_V2_Domain_strategy)
def test_sql2003_v2_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SQL2003_V2_Domain_strategy)
def test_sql2003_v2_domain_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=SQL2003_V2_StructuralComponent_strategy)
@settings(max_examples=50)
def test_sql2003_v2_structuralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_StructuralComponent)



@given(instance=SQL2003_V2_StructuralComponent_strategy)
def test_sql2003_v2_structuralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_Restriction_strategy)
@settings(max_examples=50)
def test_sql2003_v2_restriction_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Restriction)

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=SQL2003_V2_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v2_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_UniqueConstraint)

@given(instance=SQL2003_V2_TableCheckConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v2_tablecheckconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_TableCheckConstraint)



@given(instance=SQL2003_V2_TableCheckConstraint_strategy)
def test_sql2003_v2_tablecheckconstraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=SQL2003_V2_ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v2_referentialconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ReferentialConstraint)



@given(instance=SQL2003_V2_ReferentialConstraint_strategy)
def test_sql2003_v2_referentialconstraint_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original



@given(instance=SQL2003_V2_ReferentialConstraint_strategy)
def test_sql2003_v2_referentialconstraint_delete_action_setter(instance):
    original = instance.delete_action
    instance.delete_action = original
    assert instance.delete_action == original



@given(instance=SQL2003_V2_ReferentialConstraint_strategy)
def test_sql2003_v2_referentialconstraint_update_action_setter(instance):
    original = instance.update_action
    instance.update_action = original
    assert instance.update_action == original

@given(instance=SQL2003_V2_ReferenceType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_referencetype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ReferenceType)

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=SQL2003_V2_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql2003_v2_primarykey_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_PrimaryKey)

@given(instance=SQL2003_V2_Parameter_strategy)
@settings(max_examples=50)
def test_sql2003_v2_parameter_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Parameter)



@given(instance=SQL2003_V2_Parameter_strategy)
def test_sql2003_v2_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_NumericType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_numerictype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_NumericType)



@given(instance=SQL2003_V2_NumericType_strategy)
def test_sql2003_v2_numerictype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V2_NumericFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v2_numericfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_NumericFeature)



@given(instance=SQL2003_V2_NumericFeature_strategy)
def test_sql2003_v2_numericfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_V2_NumericFeature_strategy)
def test_sql2003_v2_numericfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=SQL2003_V2_NotNull_strategy)
@settings(max_examples=50)
def test_sql2003_v2_notnull_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_NotNull)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=SQL2003_V2_ParameterWithMode_strategy)
@settings(max_examples=50)
def test_sql2003_v2_parameterwithmode_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ParameterWithMode)



@given(instance=SQL2003_V2_ParameterWithMode_strategy)
def test_sql2003_v2_parameterwithmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SQL2003_V2_MethodParameter_strategy)
@settings(max_examples=50)
def test_sql2003_v2_methodparameter_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_MethodParameter)

@given(instance=SQL2003_V2_Method_strategy)
@settings(max_examples=50)
def test_sql2003_v2_method_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Method)



@given(instance=SQL2003_V2_Method_strategy)
def test_sql2003_v2_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SQL2003_V2_Method_strategy)
def test_sql2003_v2_method_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=SQL2003_V2_IntervalType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_intervaltype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_IntervalType)



@given(instance=SQL2003_V2_IntervalType_strategy)
def test_sql2003_v2_intervaltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V2_IntervalFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v2_intervalfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_IntervalFeature)



@given(instance=SQL2003_V2_IntervalFeature_strategy)
def test_sql2003_v2_intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_V2_IntervalFeature_strategy)
def test_sql2003_v2_intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, BehaviouralComponent)

@given(instance=SQL2003_V2_Procedure_strategy)
@settings(max_examples=50)
def test_sql2003_v2_procedure_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Procedure)

@given(instance=SQL2003_V2_Function_strategy)
@settings(max_examples=50)
def test_sql2003_v2_function_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Function)

@given(instance=SQL2003_V2_ROW_strategy)
@settings(max_examples=50)
def test_sql2003_v2_row_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ROW)

@given(instance=SQL2003_V2_Field_strategy)
@settings(max_examples=50)
def test_sql2003_v2_field_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Field)

@given(instance=SQL2003_V2_Feature_strategy)
@settings(max_examples=50)
def test_sql2003_v2_feature_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Feature)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=SQL2003_V2_StructuredType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_structuredtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_StructuredType)



@given(instance=SQL2003_V2_StructuredType_strategy)
def test_sql2003_v2_structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original



@given(instance=SQL2003_V2_StructuredType_strategy)
def test_sql2003_v2_structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original

@given(instance=SQL2003_V2_DistinctType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_distincttype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_DistinctType)

@given(instance=SQL2003_V2_DerivedTable_strategy)
@settings(max_examples=50)
def test_sql2003_v2_derivedtable_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_DerivedTable)



@given(instance=SQL2003_V2_DerivedTable_strategy)
def test_sql2003_v2_derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=SQL2003_V2_UserDefinedType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_userdefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_UserDefinedType)



@given(instance=SQL2003_V2_UserDefinedType_strategy)
def test_sql2003_v2_userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_PredefinedType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_predefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_PredefinedType)

@given(instance=SQL2003_V2_ConstructedType_strategy)
@settings(max_examples=50)
def test_sql2003_v2_constructedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ConstructedType)



@given(instance=SQL2003_V2_ConstructedType_strategy)
def test_sql2003_v2_constructedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V2_Attribute_strategy)
@settings(max_examples=50)
def test_sql2003_v2_attribute_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_Attribute)



@given(instance=SQL2003_V2_Attribute_strategy)
def test_sql2003_v2_attribute_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=SQL2003_V2_MULTISET_strategy)
@settings(max_examples=50)
def test_sql2003_v2_multiset_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_MULTISET)

@given(instance=SQL2003_V2_ARRAY_strategy)
@settings(max_examples=50)
def test_sql2003_v2_array_instantiation(instance):
    assert isinstance(instance, SQL2003_V2_ARRAY)



@given(instance=SQL2003_V2_ARRAY_strategy)
def test_sql2003_v2_array_num_elements_setter(instance):
    original = instance.num_elements
    instance.num_elements = original
    assert instance.num_elements == original
