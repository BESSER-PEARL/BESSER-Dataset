import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SQL2003_evo_TriggerDescriptor,
    DerivedTable,
    BaseTable,
    SQL2003_evo_View,
    SQL2003_evo_TypedTable,
    TableConstraint,
    SQL2003_evo_UniqueConstraint,
    SQL2003_evo_TableCheckConstraint,
    SQL2003_evo_ReferentialConstraint,
    SQL2003_evo_StructuralComponent,
    SQL2003_evo_Restriction,
    SQL2003_evo_Parameter,
    ColumnConstraint,
    SQL2003_evo_NotNull,
    UniqueConstraint,
    SQL2003_evo_PrimaryKey,
    Parameter,
    SQL2003_evo_MethodParameter,
    SQL2003_evo_Method,
    BehaviouralComponent,
    SQL2003_evo_Procedure,
    SQL2003_evo_Function,
    SQL2003_evo_Feature,
    UserDefinedType,
    SQL2003_evo_DistinctType,
    Feature,
    SQL2003_evo_NumericFeature,
    SQL2003_evo_IntervalFeature,
    SQL2003_evo_StringFeature,
    SQL2003_evo_DatetimeFeature,
    DataType,
    SQL2003_evo_PredefinedType,
    SQL2003_evo_UserDefinedType,
    SQL2003_evo_ConstructedType,
    Restriction,
    SQL2003_evo_Trigger,
    SQL2003_evo_TableConstraint,
    SQL2003_evo_ColumnConstraint,
    SQL2003_evo_Table,
    SQL2003_evo_DataType,
    ConstructedType,
    SQL2003_evo_ReferenceType,
    SQL2003_evo_ROW,
    SQL2003_evo_CollectionType,
    PredefinedType,
    SQL2003_evo_DatetimeType,
    SQL2003_evo_XMLType,
    SQL2003_evo_IntervalType,
    SQL2003_evo_BooleanType,
    SQL2003_evo_NumericType,
    SQL2003_evo_CharacterStringType,
    SQL2003_evo_BinaryStringType,
    SQL2003_evo_ParameterWithMode,
    SQL2003_evo_Schema,
    SQL2003_evo_BehaviouralComponent,
    Table,
    SQL2003_evo_DerivedTable,
    SQL2003_evo_BaseTable,
    SQL2003_evo_StructuredType,
    StructuralComponent,
    SQL2003_evo_Field,
    SQL2003_evo_Column,
    SQL2003_evo_Attribute,
    CollectionType,
    SQL2003_evo_MULTISET,
    SQL2003_evo_ARRAY,
    MatchTypes,
    StringFeatures,
    DatetimeTypes,
    TriggerActionTime,
    CharacterStringTypes,
    ParameterMode,
    NumericTypes,
    TriggerEvent,
    BooleanTypes,
    Unit,
    IntervalTypes,
    Multiplier,
    NumericRadix,
    BinaryStringTypes,
    ReferentialAction,
    DatetimeFeatures,
    NumericFeatures,
    TriggerLevel,
    XMLTypes,
    IntervalFeatures,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql2003_evo_triggerdescriptor_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_TriggerDescriptor)


def test_sql2003_evo_triggerdescriptor_constructor_exists():
    assert callable(SQL2003_evo_TriggerDescriptor.__init__)


def test_sql2003_evo_triggerdescriptor_constructor_args():
    sig = inspect.signature(SQL2003_evo_TriggerDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "triggeredAction" in params, "Missing parameter 'triggeredAction'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"
    assert "event" in params, "Missing parameter 'event'"

def test_sql2003_evo_triggerdescriptor_has_level():
    assert hasattr(SQL2003_evo_TriggerDescriptor, "level")
    descriptor = None
    for klass in SQL2003_evo_TriggerDescriptor.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_triggerdescriptor_has_triggeredAction():
    assert hasattr(SQL2003_evo_TriggerDescriptor, "triggeredAction")
    descriptor = None
    for klass in SQL2003_evo_TriggerDescriptor.__mro__:
        if "triggeredAction" in klass.__dict__:
            descriptor = klass.__dict__["triggeredAction"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_triggerdescriptor_has_actionTime():
    assert hasattr(SQL2003_evo_TriggerDescriptor, "actionTime")
    descriptor = None
    for klass in SQL2003_evo_TriggerDescriptor.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_triggerdescriptor_has_event():
    assert hasattr(SQL2003_evo_TriggerDescriptor, "event")
    descriptor = None
    for klass in SQL2003_evo_TriggerDescriptor.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_derivedtable_is_not_abstract():
    assert not inspect.isabstract(DerivedTable)


def test_derivedtable_constructor_exists():
    assert callable(DerivedTable.__init__)


def test_derivedtable_constructor_args():
    sig = inspect.signature(DerivedTable.__init__)
    params = list(sig.parameters.keys())



def test_basetable_is_not_abstract():
    assert not inspect.isabstract(BaseTable)


def test_basetable_constructor_exists():
    assert callable(BaseTable.__init__)


def test_basetable_constructor_args():
    sig = inspect.signature(BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_view_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_View)


def test_sql2003_evo_view_constructor_exists():
    assert callable(SQL2003_evo_View.__init__)


def test_sql2003_evo_view_constructor_args():
    sig = inspect.signature(SQL2003_evo_View.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_typedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_TypedTable)


def test_sql2003_evo_typedtable_constructor_exists():
    assert callable(SQL2003_evo_TypedTable.__init__)


def test_sql2003_evo_typedtable_constructor_args():
    sig = inspect.signature(SQL2003_evo_TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_UniqueConstraint)


def test_sql2003_evo_uniqueconstraint_constructor_exists():
    assert callable(SQL2003_evo_UniqueConstraint.__init__)


def test_sql2003_evo_uniqueconstraint_constructor_args():
    sig = inspect.signature(SQL2003_evo_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_tablecheckconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_TableCheckConstraint)


def test_sql2003_evo_tablecheckconstraint_constructor_exists():
    assert callable(SQL2003_evo_TableCheckConstraint.__init__)


def test_sql2003_evo_tablecheckconstraint_constructor_args():
    sig = inspect.signature(SQL2003_evo_TableCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sql2003_evo_tablecheckconstraint_has_expression():
    assert hasattr(SQL2003_evo_TableCheckConstraint, "expression")
    descriptor = None
    for klass in SQL2003_evo_TableCheckConstraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ReferentialConstraint)


def test_sql2003_evo_referentialconstraint_constructor_exists():
    assert callable(SQL2003_evo_ReferentialConstraint.__init__)


def test_sql2003_evo_referentialconstraint_constructor_args():
    sig = inspect.signature(SQL2003_evo_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "match" in params, "Missing parameter 'match'"
    assert "update_action" in params, "Missing parameter 'update_action'"
    assert "delete_action" in params, "Missing parameter 'delete_action'"

def test_sql2003_evo_referentialconstraint_has_match():
    assert hasattr(SQL2003_evo_ReferentialConstraint, "match")
    descriptor = None
    for klass in SQL2003_evo_ReferentialConstraint.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_referentialconstraint_has_update_action():
    assert hasattr(SQL2003_evo_ReferentialConstraint, "update_action")
    descriptor = None
    for klass in SQL2003_evo_ReferentialConstraint.__mro__:
        if "update_action" in klass.__dict__:
            descriptor = klass.__dict__["update_action"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_referentialconstraint_has_delete_action():
    assert hasattr(SQL2003_evo_ReferentialConstraint, "delete_action")
    descriptor = None
    for klass in SQL2003_evo_ReferentialConstraint.__mro__:
        if "delete_action" in klass.__dict__:
            descriptor = klass.__dict__["delete_action"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_StructuralComponent)


def test_sql2003_evo_structuralcomponent_constructor_exists():
    assert callable(SQL2003_evo_StructuralComponent.__init__)


def test_sql2003_evo_structuralcomponent_constructor_args():
    sig = inspect.signature(SQL2003_evo_StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_structuralcomponent_has_name():
    assert hasattr(SQL2003_evo_StructuralComponent, "name")
    descriptor = None
    for klass in SQL2003_evo_StructuralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_restriction_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Restriction)


def test_sql2003_evo_restriction_constructor_exists():
    assert callable(SQL2003_evo_Restriction.__init__)


def test_sql2003_evo_restriction_constructor_args():
    sig = inspect.signature(SQL2003_evo_Restriction.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_parameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Parameter)


def test_sql2003_evo_parameter_constructor_exists():
    assert callable(SQL2003_evo_Parameter.__init__)


def test_sql2003_evo_parameter_constructor_args():
    sig = inspect.signature(SQL2003_evo_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_parameter_has_name():
    assert hasattr(SQL2003_evo_Parameter, "name")
    descriptor = None
    for klass in SQL2003_evo_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_notnull_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_NotNull)


def test_sql2003_evo_notnull_constructor_exists():
    assert callable(SQL2003_evo_NotNull.__init__)


def test_sql2003_evo_notnull_constructor_args():
    sig = inspect.signature(SQL2003_evo_NotNull.__init__)
    params = list(sig.parameters.keys())



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_primarykey_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_PrimaryKey)


def test_sql2003_evo_primarykey_constructor_exists():
    assert callable(SQL2003_evo_PrimaryKey.__init__)


def test_sql2003_evo_primarykey_constructor_args():
    sig = inspect.signature(SQL2003_evo_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_methodparameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_MethodParameter)


def test_sql2003_evo_methodparameter_constructor_exists():
    assert callable(SQL2003_evo_MethodParameter.__init__)


def test_sql2003_evo_methodparameter_constructor_args():
    sig = inspect.signature(SQL2003_evo_MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_method_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Method)


def test_sql2003_evo_method_constructor_exists():
    assert callable(SQL2003_evo_Method.__init__)


def test_sql2003_evo_method_constructor_args():
    sig = inspect.signature(SQL2003_evo_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003_evo_method_has_name():
    assert hasattr(SQL2003_evo_Method, "name")
    descriptor = None
    for klass in SQL2003_evo_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_method_has_body():
    assert hasattr(SQL2003_evo_Method, "body")
    descriptor = None
    for klass in SQL2003_evo_Method.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(BehaviouralComponent)


def test_behaviouralcomponent_constructor_exists():
    assert callable(BehaviouralComponent.__init__)


def test_behaviouralcomponent_constructor_args():
    sig = inspect.signature(BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_procedure_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Procedure)


def test_sql2003_evo_procedure_constructor_exists():
    assert callable(SQL2003_evo_Procedure.__init__)


def test_sql2003_evo_procedure_constructor_args():
    sig = inspect.signature(SQL2003_evo_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_function_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Function)


def test_sql2003_evo_function_constructor_exists():
    assert callable(SQL2003_evo_Function.__init__)


def test_sql2003_evo_function_constructor_args():
    sig = inspect.signature(SQL2003_evo_Function.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_feature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Feature)


def test_sql2003_evo_feature_constructor_exists():
    assert callable(SQL2003_evo_Feature.__init__)


def test_sql2003_evo_feature_constructor_args():
    sig = inspect.signature(SQL2003_evo_Feature.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_distincttype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_DistinctType)


def test_sql2003_evo_distincttype_constructor_exists():
    assert callable(SQL2003_evo_DistinctType.__init__)


def test_sql2003_evo_distincttype_constructor_args():
    sig = inspect.signature(SQL2003_evo_DistinctType.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_numericfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_NumericFeature)


def test_sql2003_evo_numericfeature_constructor_exists():
    assert callable(SQL2003_evo_NumericFeature.__init__)


def test_sql2003_evo_numericfeature_constructor_args():
    sig = inspect.signature(SQL2003_evo_NumericFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_evo_numericfeature_has_key():
    assert hasattr(SQL2003_evo_NumericFeature, "key")
    descriptor = None
    for klass in SQL2003_evo_NumericFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_numericfeature_has_value():
    assert hasattr(SQL2003_evo_NumericFeature, "value")
    descriptor = None
    for klass in SQL2003_evo_NumericFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_intervalfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_IntervalFeature)


def test_sql2003_evo_intervalfeature_constructor_exists():
    assert callable(SQL2003_evo_IntervalFeature.__init__)


def test_sql2003_evo_intervalfeature_constructor_args():
    sig = inspect.signature(SQL2003_evo_IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003_evo_intervalfeature_has_value():
    assert hasattr(SQL2003_evo_IntervalFeature, "value")
    descriptor = None
    for klass in SQL2003_evo_IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_intervalfeature_has_key():
    assert hasattr(SQL2003_evo_IntervalFeature, "key")
    descriptor = None
    for klass in SQL2003_evo_IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_stringfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_StringFeature)


def test_sql2003_evo_stringfeature_constructor_exists():
    assert callable(SQL2003_evo_StringFeature.__init__)


def test_sql2003_evo_stringfeature_constructor_args():
    sig = inspect.signature(SQL2003_evo_StringFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_evo_stringfeature_has_key():
    assert hasattr(SQL2003_evo_StringFeature, "key")
    descriptor = None
    for klass in SQL2003_evo_StringFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_stringfeature_has_value():
    assert hasattr(SQL2003_evo_StringFeature, "value")
    descriptor = None
    for klass in SQL2003_evo_StringFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_datetimefeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_DatetimeFeature)


def test_sql2003_evo_datetimefeature_constructor_exists():
    assert callable(SQL2003_evo_DatetimeFeature.__init__)


def test_sql2003_evo_datetimefeature_constructor_args():
    sig = inspect.signature(SQL2003_evo_DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_evo_datetimefeature_has_key():
    assert hasattr(SQL2003_evo_DatetimeFeature, "key")
    descriptor = None
    for klass in SQL2003_evo_DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_datetimefeature_has_value():
    assert hasattr(SQL2003_evo_DatetimeFeature, "value")
    descriptor = None
    for klass in SQL2003_evo_DatetimeFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_PredefinedType)


def test_sql2003_evo_predefinedtype_constructor_exists():
    assert callable(SQL2003_evo_PredefinedType.__init__)


def test_sql2003_evo_predefinedtype_constructor_args():
    sig = inspect.signature(SQL2003_evo_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_UserDefinedType)


def test_sql2003_evo_userdefinedtype_constructor_exists():
    assert callable(SQL2003_evo_UserDefinedType.__init__)


def test_sql2003_evo_userdefinedtype_constructor_args():
    sig = inspect.signature(SQL2003_evo_UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_userdefinedtype_has_name():
    assert hasattr(SQL2003_evo_UserDefinedType, "name")
    descriptor = None
    for klass in SQL2003_evo_UserDefinedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_constructedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ConstructedType)


def test_sql2003_evo_constructedtype_constructor_exists():
    assert callable(SQL2003_evo_ConstructedType.__init__)


def test_sql2003_evo_constructedtype_constructor_args():
    sig = inspect.signature(SQL2003_evo_ConstructedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_constructedtype_has_name():
    assert hasattr(SQL2003_evo_ConstructedType, "name")
    descriptor = None
    for klass in SQL2003_evo_ConstructedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_restriction_is_not_abstract():
    assert not inspect.isabstract(Restriction)


def test_restriction_constructor_exists():
    assert callable(Restriction.__init__)


def test_restriction_constructor_args():
    sig = inspect.signature(Restriction.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_trigger_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Trigger)


def test_sql2003_evo_trigger_constructor_exists():
    assert callable(SQL2003_evo_Trigger.__init__)


def test_sql2003_evo_trigger_constructor_args():
    sig = inspect.signature(SQL2003_evo_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_trigger_has_name():
    assert hasattr(SQL2003_evo_Trigger, "name")
    descriptor = None
    for klass in SQL2003_evo_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_TableConstraint)


def test_sql2003_evo_tableconstraint_constructor_exists():
    assert callable(SQL2003_evo_TableConstraint.__init__)


def test_sql2003_evo_tableconstraint_constructor_args():
    sig = inspect.signature(SQL2003_evo_TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_tableconstraint_has_name():
    assert hasattr(SQL2003_evo_TableConstraint, "name")
    descriptor = None
    for klass in SQL2003_evo_TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ColumnConstraint)


def test_sql2003_evo_columnconstraint_constructor_exists():
    assert callable(SQL2003_evo_ColumnConstraint.__init__)


def test_sql2003_evo_columnconstraint_constructor_args():
    sig = inspect.signature(SQL2003_evo_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_table_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Table)


def test_sql2003_evo_table_constructor_exists():
    assert callable(SQL2003_evo_Table.__init__)


def test_sql2003_evo_table_constructor_args():
    sig = inspect.signature(SQL2003_evo_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_table_has_name():
    assert hasattr(SQL2003_evo_Table, "name")
    descriptor = None
    for klass in SQL2003_evo_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_datatype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_DataType)


def test_sql2003_evo_datatype_constructor_exists():
    assert callable(SQL2003_evo_DataType.__init__)


def test_sql2003_evo_datatype_constructor_args():
    sig = inspect.signature(SQL2003_evo_DataType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_referencetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ReferenceType)


def test_sql2003_evo_referencetype_constructor_exists():
    assert callable(SQL2003_evo_ReferenceType.__init__)


def test_sql2003_evo_referencetype_constructor_args():
    sig = inspect.signature(SQL2003_evo_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_row_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ROW)


def test_sql2003_evo_row_constructor_exists():
    assert callable(SQL2003_evo_ROW.__init__)


def test_sql2003_evo_row_constructor_args():
    sig = inspect.signature(SQL2003_evo_ROW.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_collectiontype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_CollectionType)


def test_sql2003_evo_collectiontype_constructor_exists():
    assert callable(SQL2003_evo_CollectionType.__init__)


def test_sql2003_evo_collectiontype_constructor_args():
    sig = inspect.signature(SQL2003_evo_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_DatetimeType)


def test_sql2003_evo_datetimetype_constructor_exists():
    assert callable(SQL2003_evo_DatetimeType.__init__)


def test_sql2003_evo_datetimetype_constructor_args():
    sig = inspect.signature(SQL2003_evo_DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_evo_datetimetype_has_descriptor():
    assert hasattr(SQL2003_evo_DatetimeType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_DatetimeType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_xmltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_XMLType)


def test_sql2003_evo_xmltype_constructor_exists():
    assert callable(SQL2003_evo_XMLType.__init__)


def test_sql2003_evo_xmltype_constructor_args():
    sig = inspect.signature(SQL2003_evo_XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_evo_xmltype_has_descriptor():
    assert hasattr(SQL2003_evo_XMLType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_XMLType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_intervaltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_IntervalType)


def test_sql2003_evo_intervaltype_constructor_exists():
    assert callable(SQL2003_evo_IntervalType.__init__)


def test_sql2003_evo_intervaltype_constructor_args():
    sig = inspect.signature(SQL2003_evo_IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_evo_intervaltype_has_descriptor():
    assert hasattr(SQL2003_evo_IntervalType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_IntervalType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_booleantype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_BooleanType)


def test_sql2003_evo_booleantype_constructor_exists():
    assert callable(SQL2003_evo_BooleanType.__init__)


def test_sql2003_evo_booleantype_constructor_args():
    sig = inspect.signature(SQL2003_evo_BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_evo_booleantype_has_descriptor():
    assert hasattr(SQL2003_evo_BooleanType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_BooleanType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_numerictype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_NumericType)


def test_sql2003_evo_numerictype_constructor_exists():
    assert callable(SQL2003_evo_NumericType.__init__)


def test_sql2003_evo_numerictype_constructor_args():
    sig = inspect.signature(SQL2003_evo_NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_evo_numerictype_has_descriptor():
    assert hasattr(SQL2003_evo_NumericType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_NumericType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_CharacterStringType)


def test_sql2003_evo_characterstringtype_constructor_exists():
    assert callable(SQL2003_evo_CharacterStringType.__init__)


def test_sql2003_evo_characterstringtype_constructor_args():
    sig = inspect.signature(SQL2003_evo_CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "length_def" in params, "Missing parameter 'length_def'"

def test_sql2003_evo_characterstringtype_has_descriptor():
    assert hasattr(SQL2003_evo_CharacterStringType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_CharacterStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_characterstringtype_has_length_def():
    assert hasattr(SQL2003_evo_CharacterStringType, "length_def")
    descriptor = None
    for klass in SQL2003_evo_CharacterStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_binarystringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_BinaryStringType)


def test_sql2003_evo_binarystringtype_constructor_exists():
    assert callable(SQL2003_evo_BinaryStringType.__init__)


def test_sql2003_evo_binarystringtype_constructor_args():
    sig = inspect.signature(SQL2003_evo_BinaryStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length_def" in params, "Missing parameter 'length_def'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_evo_binarystringtype_has_length_def():
    assert hasattr(SQL2003_evo_BinaryStringType, "length_def")
    descriptor = None
    for klass in SQL2003_evo_BinaryStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_binarystringtype_has_descriptor():
    assert hasattr(SQL2003_evo_BinaryStringType, "descriptor")
    descriptor = None
    for klass in SQL2003_evo_BinaryStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_parameterwithmode_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ParameterWithMode)


def test_sql2003_evo_parameterwithmode_constructor_exists():
    assert callable(SQL2003_evo_ParameterWithMode.__init__)


def test_sql2003_evo_parameterwithmode_constructor_args():
    sig = inspect.signature(SQL2003_evo_ParameterWithMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sql2003_evo_parameterwithmode_has_mode():
    assert hasattr(SQL2003_evo_ParameterWithMode, "mode")
    descriptor = None
    for klass in SQL2003_evo_ParameterWithMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_schema_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Schema)


def test_sql2003_evo_schema_constructor_exists():
    assert callable(SQL2003_evo_Schema.__init__)


def test_sql2003_evo_schema_constructor_args():
    sig = inspect.signature(SQL2003_evo_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_schema_has_name():
    assert hasattr(SQL2003_evo_Schema, "name")
    descriptor = None
    for klass in SQL2003_evo_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_BehaviouralComponent)


def test_sql2003_evo_behaviouralcomponent_constructor_exists():
    assert callable(SQL2003_evo_BehaviouralComponent.__init__)


def test_sql2003_evo_behaviouralcomponent_constructor_args():
    sig = inspect.signature(SQL2003_evo_BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_evo_behaviouralcomponent_has_body():
    assert hasattr(SQL2003_evo_BehaviouralComponent, "body")
    descriptor = None
    for klass in SQL2003_evo_BehaviouralComponent.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_behaviouralcomponent_has_name():
    assert hasattr(SQL2003_evo_BehaviouralComponent, "name")
    descriptor = None
    for klass in SQL2003_evo_BehaviouralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_derivedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_DerivedTable)


def test_sql2003_evo_derivedtable_constructor_exists():
    assert callable(SQL2003_evo_DerivedTable.__init__)


def test_sql2003_evo_derivedtable_constructor_args():
    sig = inspect.signature(SQL2003_evo_DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_sql2003_evo_derivedtable_has_query_expression():
    assert hasattr(SQL2003_evo_DerivedTable, "query_expression")
    descriptor = None
    for klass in SQL2003_evo_DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_basetable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_BaseTable)


def test_sql2003_evo_basetable_constructor_exists():
    assert callable(SQL2003_evo_BaseTable.__init__)


def test_sql2003_evo_basetable_constructor_args():
    sig = inspect.signature(SQL2003_evo_BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_structuredtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_StructuredType)


def test_sql2003_evo_structuredtype_constructor_exists():
    assert callable(SQL2003_evo_StructuredType.__init__)


def test_sql2003_evo_structuredtype_constructor_args():
    sig = inspect.signature(SQL2003_evo_StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"
    assert "is_final" in params, "Missing parameter 'is_final'"

def test_sql2003_evo_structuredtype_has_is_instantiable():
    assert hasattr(SQL2003_evo_StructuredType, "is_instantiable")
    descriptor = None
    for klass in SQL2003_evo_StructuredType.__mro__:
        if "is_instantiable" in klass.__dict__:
            descriptor = klass.__dict__["is_instantiable"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_evo_structuredtype_has_is_final():
    assert hasattr(SQL2003_evo_StructuredType, "is_final")
    descriptor = None
    for klass in SQL2003_evo_StructuredType.__mro__:
        if "is_final" in klass.__dict__:
            descriptor = klass.__dict__["is_final"]
            break
    assert isinstance(descriptor, property)



def test_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(StructuralComponent)


def test_structuralcomponent_constructor_exists():
    assert callable(StructuralComponent.__init__)


def test_structuralcomponent_constructor_args():
    sig = inspect.signature(StructuralComponent.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_field_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Field)


def test_sql2003_evo_field_constructor_exists():
    assert callable(SQL2003_evo_Field.__init__)


def test_sql2003_evo_field_constructor_args():
    sig = inspect.signature(SQL2003_evo_Field.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_column_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Column)


def test_sql2003_evo_column_constructor_exists():
    assert callable(SQL2003_evo_Column.__init__)


def test_sql2003_evo_column_constructor_args():
    sig = inspect.signature(SQL2003_evo_Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_evo_column_has_default():
    assert hasattr(SQL2003_evo_Column, "default")
    descriptor = None
    for klass in SQL2003_evo_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_evo_attribute_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_Attribute)


def test_sql2003_evo_attribute_constructor_exists():
    assert callable(SQL2003_evo_Attribute.__init__)


def test_sql2003_evo_attribute_constructor_args():
    sig = inspect.signature(SQL2003_evo_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_evo_attribute_has_default():
    assert hasattr(SQL2003_evo_Attribute, "default")
    descriptor = None
    for klass in SQL2003_evo_Attribute.__mro__:
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



def test_sql2003_evo_multiset_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_MULTISET)


def test_sql2003_evo_multiset_constructor_exists():
    assert callable(SQL2003_evo_MULTISET.__init__)


def test_sql2003_evo_multiset_constructor_args():
    sig = inspect.signature(SQL2003_evo_MULTISET.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_evo_array_is_not_abstract():
    assert not inspect.isabstract(SQL2003_evo_ARRAY)


def test_sql2003_evo_array_constructor_exists():
    assert callable(SQL2003_evo_ARRAY.__init__)


def test_sql2003_evo_array_constructor_args():
    sig = inspect.signature(SQL2003_evo_ARRAY.__init__)
    params = list(sig.parameters.keys())
    assert "num_elements" in params, "Missing parameter 'num_elements'"

def test_sql2003_evo_array_has_num_elements():
    assert hasattr(SQL2003_evo_ARRAY, "num_elements")
    descriptor = None
    for klass in SQL2003_evo_ARRAY.__mro__:
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

def test_stringfeatures_exists():
    # Check that the Enumeration exists
    assert StringFeatures is not None

def test_stringfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringFeatures]
    expected_literals = [
        "unit",
        "multiplier",
        "length",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringFeatures"

def test_datetimetypes_exists():
    # Check that the Enumeration exists
    assert DatetimeTypes is not None

def test_datetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeTypes]
    expected_literals = [
        "TIMESTAMPWITHTIMEZONE",
        "TIMEWITHOUTTIMEZONE",
        "TIMESTAMPWITHOUTTIMEZONE",
        "DATE",
        "TIMEWITHTIMEZONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeTypes"

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

def test_characterstringtypes_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypes is not None

def test_characterstringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypes]
    expected_literals = [
        "CHARACTERLARGEOBJECT",
        "CHARACTER",
        "CHARACTERVARYING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypes"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "INOUT",
        "IN",
        "OUT",
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
        "REAL",
        "SMALLINT",
        "DECIMAL",
        "NUMERIC",
        "INTEGER",
        "DOUBLEPRECISION",
        "BIGINT",
        "FLOAT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericTypes"

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
        "CHARACTERS",
        "OCTETS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Unit"

def test_intervaltypes_exists():
    # Check that the Enumeration exists
    assert IntervalTypes is not None

def test_intervaltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalTypes]
    expected_literals = [
        "DAY_MINUTE",
        "HOUR_MINUTE",
        "YEAR_MONTH",
        "DAY_HOUR",
        "MINUTE_SECOND",
        "DAY",
        "MONTH",
        "SECOND",
        "HOUR",
        "HOUR_SECOND",
        "MINUTE",
        "DAY_SECOND",
        "YEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalTypes"

def test_multiplier_exists():
    # Check that the Enumeration exists
    assert Multiplier is not None

def test_multiplier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Multiplier]
    expected_literals = [
        "P",
        "G",
        "K",
        "M",
        "T",
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
        "DECIMAL",
        "BINARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericRadix"

def test_binarystringtypes_exists():
    # Check that the Enumeration exists
    assert BinaryStringTypes is not None

def test_binarystringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryStringTypes]
    expected_literals = [
        "BINARYVARYING",
        "BINARY",
        "BINARYLARGEOBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryStringTypes"

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
        "SET_NULL",
        "NO_ACTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialAction"

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

def test_numericfeatures_exists():
    # Check that the Enumeration exists
    assert NumericFeatures is not None

def test_numericfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericFeatures]
    expected_literals = [
        "precision",
        "scale",
        "radix",
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

def test_intervalfeatures_exists():
    # Check that the Enumeration exists
    assert IntervalFeatures is not None

def test_intervalfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalFeatures]
    expected_literals = [
        "second_precision",
        "end_leading_precision",
        "leading_precision",
        "start_leading_precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalFeatures"


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
SQL2003_evo_TriggerDescriptor_strategy = st.builds(
    SQL2003_evo_TriggerDescriptor,
    level=
        safe_text,
    triggeredAction=
        safe_text,
    actionTime=
        safe_text,
    event=
        safe_text
)
DerivedTable_strategy = st.builds(
    DerivedTable,
)
BaseTable_strategy = st.builds(
    BaseTable,
)
SQL2003_evo_View_strategy = st.builds(
    SQL2003_evo_View,
)
SQL2003_evo_TypedTable_strategy = st.builds(
    SQL2003_evo_TypedTable,
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
SQL2003_evo_UniqueConstraint_strategy = st.builds(
    SQL2003_evo_UniqueConstraint,
)
SQL2003_evo_TableCheckConstraint_strategy = st.builds(
    SQL2003_evo_TableCheckConstraint,
    expression=
        safe_text
)
SQL2003_evo_ReferentialConstraint_strategy = st.builds(
    SQL2003_evo_ReferentialConstraint,
    match=
        safe_text,
    update_action=
        safe_text,
    delete_action=
        safe_text
)
SQL2003_evo_StructuralComponent_strategy = st.builds(
    SQL2003_evo_StructuralComponent,
    name=
        safe_text
)
SQL2003_evo_Restriction_strategy = st.builds(
    SQL2003_evo_Restriction,
)
SQL2003_evo_Parameter_strategy = st.builds(
    SQL2003_evo_Parameter,
    name=
        safe_text
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
SQL2003_evo_NotNull_strategy = st.builds(
    SQL2003_evo_NotNull,
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
SQL2003_evo_PrimaryKey_strategy = st.builds(
    SQL2003_evo_PrimaryKey,
)
Parameter_strategy = st.builds(
    Parameter,
)
SQL2003_evo_MethodParameter_strategy = st.builds(
    SQL2003_evo_MethodParameter,
)
SQL2003_evo_Method_strategy = st.builds(
    SQL2003_evo_Method,
    name=
        safe_text,
    body=
        safe_text
)
BehaviouralComponent_strategy = st.builds(
    BehaviouralComponent,
)
SQL2003_evo_Procedure_strategy = st.builds(
    SQL2003_evo_Procedure,
)
SQL2003_evo_Function_strategy = st.builds(
    SQL2003_evo_Function,
)
SQL2003_evo_Feature_strategy = st.builds(
    SQL2003_evo_Feature,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
SQL2003_evo_DistinctType_strategy = st.builds(
    SQL2003_evo_DistinctType,
)
Feature_strategy = st.builds(
    Feature,
)
SQL2003_evo_NumericFeature_strategy = st.builds(
    SQL2003_evo_NumericFeature,
    key=
        safe_text,
    value=
        safe_text
)
SQL2003_evo_IntervalFeature_strategy = st.builds(
    SQL2003_evo_IntervalFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003_evo_StringFeature_strategy = st.builds(
    SQL2003_evo_StringFeature,
    key=
        safe_text,
    value=
        safe_text
)
SQL2003_evo_DatetimeFeature_strategy = st.builds(
    SQL2003_evo_DatetimeFeature,
    key=
        safe_text,
    value=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
SQL2003_evo_PredefinedType_strategy = st.builds(
    SQL2003_evo_PredefinedType,
)
SQL2003_evo_UserDefinedType_strategy = st.builds(
    SQL2003_evo_UserDefinedType,
    name=
        safe_text
)
SQL2003_evo_ConstructedType_strategy = st.builds(
    SQL2003_evo_ConstructedType,
    name=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
SQL2003_evo_Trigger_strategy = st.builds(
    SQL2003_evo_Trigger,
    name=
        safe_text
)
SQL2003_evo_TableConstraint_strategy = st.builds(
    SQL2003_evo_TableConstraint,
    name=
        safe_text
)
SQL2003_evo_ColumnConstraint_strategy = st.builds(
    SQL2003_evo_ColumnConstraint,
)
SQL2003_evo_Table_strategy = st.builds(
    SQL2003_evo_Table,
    name=
        safe_text
)
SQL2003_evo_DataType_strategy = st.builds(
    SQL2003_evo_DataType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
SQL2003_evo_ReferenceType_strategy = st.builds(
    SQL2003_evo_ReferenceType,
)
SQL2003_evo_ROW_strategy = st.builds(
    SQL2003_evo_ROW,
)
SQL2003_evo_CollectionType_strategy = st.builds(
    SQL2003_evo_CollectionType,
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
SQL2003_evo_DatetimeType_strategy = st.builds(
    SQL2003_evo_DatetimeType,
    descriptor=
        safe_text
)
SQL2003_evo_XMLType_strategy = st.builds(
    SQL2003_evo_XMLType,
    descriptor=
        safe_text
)
SQL2003_evo_IntervalType_strategy = st.builds(
    SQL2003_evo_IntervalType,
    descriptor=
        safe_text
)
SQL2003_evo_BooleanType_strategy = st.builds(
    SQL2003_evo_BooleanType,
    descriptor=
        safe_text
)
SQL2003_evo_NumericType_strategy = st.builds(
    SQL2003_evo_NumericType,
    descriptor=
        safe_text
)
SQL2003_evo_CharacterStringType_strategy = st.builds(
    SQL2003_evo_CharacterStringType,
    descriptor=
        safe_text,
    length_def=
        safe_text
)
SQL2003_evo_BinaryStringType_strategy = st.builds(
    SQL2003_evo_BinaryStringType,
    length_def=
        safe_text,
    descriptor=
        safe_text
)
SQL2003_evo_ParameterWithMode_strategy = st.builds(
    SQL2003_evo_ParameterWithMode,
    mode=
        safe_text
)
SQL2003_evo_Schema_strategy = st.builds(
    SQL2003_evo_Schema,
    name=
        safe_text
)
SQL2003_evo_BehaviouralComponent_strategy = st.builds(
    SQL2003_evo_BehaviouralComponent,
    body=
        safe_text,
    name=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SQL2003_evo_DerivedTable_strategy = st.builds(
    SQL2003_evo_DerivedTable,
    query_expression=
        safe_text
)
SQL2003_evo_BaseTable_strategy = st.builds(
    SQL2003_evo_BaseTable,
)
SQL2003_evo_StructuredType_strategy = st.builds(
    SQL2003_evo_StructuredType,
    is_instantiable=
        st.booleans(),
    is_final=
        st.booleans()
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
SQL2003_evo_Field_strategy = st.builds(
    SQL2003_evo_Field,
)
SQL2003_evo_Column_strategy = st.builds(
    SQL2003_evo_Column,
    default=
        safe_text
)
SQL2003_evo_Attribute_strategy = st.builds(
    SQL2003_evo_Attribute,
    default=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
SQL2003_evo_MULTISET_strategy = st.builds(
    SQL2003_evo_MULTISET,
)
SQL2003_evo_ARRAY_strategy = st.builds(
    SQL2003_evo_ARRAY,
    num_elements=
        safe_text
)

@given(instance=SQL2003_evo_TriggerDescriptor_strategy)
@settings(max_examples=50)
def test_sql2003_evo_triggerdescriptor_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_TriggerDescriptor)



@given(instance=SQL2003_evo_TriggerDescriptor_strategy)
def test_sql2003_evo_triggerdescriptor_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=SQL2003_evo_TriggerDescriptor_strategy)
def test_sql2003_evo_triggerdescriptor_triggeredAction_setter(instance):
    original = instance.triggeredAction
    instance.triggeredAction = original
    assert instance.triggeredAction == original



@given(instance=SQL2003_evo_TriggerDescriptor_strategy)
def test_sql2003_evo_triggerdescriptor_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original



@given(instance=SQL2003_evo_TriggerDescriptor_strategy)
def test_sql2003_evo_triggerdescriptor_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=DerivedTable_strategy)
@settings(max_examples=50)
def test_derivedtable_instantiation(instance):
    assert isinstance(instance, DerivedTable)

@given(instance=BaseTable_strategy)
@settings(max_examples=50)
def test_basetable_instantiation(instance):
    assert isinstance(instance, BaseTable)

@given(instance=SQL2003_evo_View_strategy)
@settings(max_examples=50)
def test_sql2003_evo_view_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_View)

@given(instance=SQL2003_evo_TypedTable_strategy)
@settings(max_examples=50)
def test_sql2003_evo_typedtable_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_TypedTable)

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=SQL2003_evo_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_evo_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_UniqueConstraint)

@given(instance=SQL2003_evo_TableCheckConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_evo_tablecheckconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_TableCheckConstraint)



@given(instance=SQL2003_evo_TableCheckConstraint_strategy)
def test_sql2003_evo_tablecheckconstraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=SQL2003_evo_ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_evo_referentialconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ReferentialConstraint)



@given(instance=SQL2003_evo_ReferentialConstraint_strategy)
def test_sql2003_evo_referentialconstraint_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original



@given(instance=SQL2003_evo_ReferentialConstraint_strategy)
def test_sql2003_evo_referentialconstraint_update_action_setter(instance):
    original = instance.update_action
    instance.update_action = original
    assert instance.update_action == original



@given(instance=SQL2003_evo_ReferentialConstraint_strategy)
def test_sql2003_evo_referentialconstraint_delete_action_setter(instance):
    original = instance.delete_action
    instance.delete_action = original
    assert instance.delete_action == original

@given(instance=SQL2003_evo_StructuralComponent_strategy)
@settings(max_examples=50)
def test_sql2003_evo_structuralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_StructuralComponent)



@given(instance=SQL2003_evo_StructuralComponent_strategy)
def test_sql2003_evo_structuralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_evo_Restriction_strategy)
@settings(max_examples=50)
def test_sql2003_evo_restriction_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Restriction)

@given(instance=SQL2003_evo_Parameter_strategy)
@settings(max_examples=50)
def test_sql2003_evo_parameter_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Parameter)



@given(instance=SQL2003_evo_Parameter_strategy)
def test_sql2003_evo_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=SQL2003_evo_NotNull_strategy)
@settings(max_examples=50)
def test_sql2003_evo_notnull_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_NotNull)

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=SQL2003_evo_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql2003_evo_primarykey_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_PrimaryKey)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=SQL2003_evo_MethodParameter_strategy)
@settings(max_examples=50)
def test_sql2003_evo_methodparameter_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_MethodParameter)

@given(instance=SQL2003_evo_Method_strategy)
@settings(max_examples=50)
def test_sql2003_evo_method_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Method)



@given(instance=SQL2003_evo_Method_strategy)
def test_sql2003_evo_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SQL2003_evo_Method_strategy)
def test_sql2003_evo_method_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, BehaviouralComponent)

@given(instance=SQL2003_evo_Procedure_strategy)
@settings(max_examples=50)
def test_sql2003_evo_procedure_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Procedure)

@given(instance=SQL2003_evo_Function_strategy)
@settings(max_examples=50)
def test_sql2003_evo_function_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Function)

@given(instance=SQL2003_evo_Feature_strategy)
@settings(max_examples=50)
def test_sql2003_evo_feature_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Feature)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=SQL2003_evo_DistinctType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_distincttype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_DistinctType)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=SQL2003_evo_NumericFeature_strategy)
@settings(max_examples=50)
def test_sql2003_evo_numericfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_NumericFeature)



@given(instance=SQL2003_evo_NumericFeature_strategy)
def test_sql2003_evo_numericfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_evo_NumericFeature_strategy)
def test_sql2003_evo_numericfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003_evo_IntervalFeature_strategy)
@settings(max_examples=50)
def test_sql2003_evo_intervalfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_IntervalFeature)



@given(instance=SQL2003_evo_IntervalFeature_strategy)
def test_sql2003_evo_intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=SQL2003_evo_IntervalFeature_strategy)
def test_sql2003_evo_intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003_evo_StringFeature_strategy)
@settings(max_examples=50)
def test_sql2003_evo_stringfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_StringFeature)



@given(instance=SQL2003_evo_StringFeature_strategy)
def test_sql2003_evo_stringfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_evo_StringFeature_strategy)
def test_sql2003_evo_stringfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003_evo_DatetimeFeature_strategy)
@settings(max_examples=50)
def test_sql2003_evo_datetimefeature_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_DatetimeFeature)



@given(instance=SQL2003_evo_DatetimeFeature_strategy)
def test_sql2003_evo_datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_evo_DatetimeFeature_strategy)
def test_sql2003_evo_datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=SQL2003_evo_PredefinedType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_predefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_PredefinedType)

@given(instance=SQL2003_evo_UserDefinedType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_userdefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_UserDefinedType)



@given(instance=SQL2003_evo_UserDefinedType_strategy)
def test_sql2003_evo_userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_evo_ConstructedType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_constructedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ConstructedType)



@given(instance=SQL2003_evo_ConstructedType_strategy)
def test_sql2003_evo_constructedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=SQL2003_evo_Trigger_strategy)
@settings(max_examples=50)
def test_sql2003_evo_trigger_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Trigger)



@given(instance=SQL2003_evo_Trigger_strategy)
def test_sql2003_evo_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_evo_TableConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_evo_tableconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_TableConstraint)



@given(instance=SQL2003_evo_TableConstraint_strategy)
def test_sql2003_evo_tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_evo_ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_evo_columnconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ColumnConstraint)

@given(instance=SQL2003_evo_Table_strategy)
@settings(max_examples=50)
def test_sql2003_evo_table_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Table)



@given(instance=SQL2003_evo_Table_strategy)
def test_sql2003_evo_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_evo_DataType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_datatype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_DataType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=SQL2003_evo_ReferenceType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_referencetype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ReferenceType)

@given(instance=SQL2003_evo_ROW_strategy)
@settings(max_examples=50)
def test_sql2003_evo_row_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ROW)

@given(instance=SQL2003_evo_CollectionType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_collectiontype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_CollectionType)

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=SQL2003_evo_DatetimeType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_datetimetype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_DatetimeType)



@given(instance=SQL2003_evo_DatetimeType_strategy)
def test_sql2003_evo_datetimetype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_evo_XMLType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_xmltype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_XMLType)



@given(instance=SQL2003_evo_XMLType_strategy)
def test_sql2003_evo_xmltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_evo_IntervalType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_intervaltype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_IntervalType)



@given(instance=SQL2003_evo_IntervalType_strategy)
def test_sql2003_evo_intervaltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_evo_BooleanType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_booleantype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_BooleanType)



@given(instance=SQL2003_evo_BooleanType_strategy)
def test_sql2003_evo_booleantype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_evo_NumericType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_numerictype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_NumericType)



@given(instance=SQL2003_evo_NumericType_strategy)
def test_sql2003_evo_numerictype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_evo_CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_characterstringtype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_CharacterStringType)



@given(instance=SQL2003_evo_CharacterStringType_strategy)
def test_sql2003_evo_characterstringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=SQL2003_evo_CharacterStringType_strategy)
def test_sql2003_evo_characterstringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003_evo_BinaryStringType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_binarystringtype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_BinaryStringType)



@given(instance=SQL2003_evo_BinaryStringType_strategy)
def test_sql2003_evo_binarystringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original



@given(instance=SQL2003_evo_BinaryStringType_strategy)
def test_sql2003_evo_binarystringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_evo_ParameterWithMode_strategy)
@settings(max_examples=50)
def test_sql2003_evo_parameterwithmode_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ParameterWithMode)



@given(instance=SQL2003_evo_ParameterWithMode_strategy)
def test_sql2003_evo_parameterwithmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SQL2003_evo_Schema_strategy)
@settings(max_examples=50)
def test_sql2003_evo_schema_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Schema)



@given(instance=SQL2003_evo_Schema_strategy)
def test_sql2003_evo_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_evo_BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_sql2003_evo_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_BehaviouralComponent)



@given(instance=SQL2003_evo_BehaviouralComponent_strategy)
def test_sql2003_evo_behaviouralcomponent_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=SQL2003_evo_BehaviouralComponent_strategy)
def test_sql2003_evo_behaviouralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SQL2003_evo_DerivedTable_strategy)
@settings(max_examples=50)
def test_sql2003_evo_derivedtable_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_DerivedTable)



@given(instance=SQL2003_evo_DerivedTable_strategy)
def test_sql2003_evo_derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=SQL2003_evo_BaseTable_strategy)
@settings(max_examples=50)
def test_sql2003_evo_basetable_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_BaseTable)

@given(instance=SQL2003_evo_StructuredType_strategy)
@settings(max_examples=50)
def test_sql2003_evo_structuredtype_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_StructuredType)



@given(instance=SQL2003_evo_StructuredType_strategy)
def test_sql2003_evo_structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original



@given(instance=SQL2003_evo_StructuredType_strategy)
def test_sql2003_evo_structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=SQL2003_evo_Field_strategy)
@settings(max_examples=50)
def test_sql2003_evo_field_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Field)

@given(instance=SQL2003_evo_Column_strategy)
@settings(max_examples=50)
def test_sql2003_evo_column_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Column)



@given(instance=SQL2003_evo_Column_strategy)
def test_sql2003_evo_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=SQL2003_evo_Attribute_strategy)
@settings(max_examples=50)
def test_sql2003_evo_attribute_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_Attribute)



@given(instance=SQL2003_evo_Attribute_strategy)
def test_sql2003_evo_attribute_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=SQL2003_evo_MULTISET_strategy)
@settings(max_examples=50)
def test_sql2003_evo_multiset_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_MULTISET)

@given(instance=SQL2003_evo_ARRAY_strategy)
@settings(max_examples=50)
def test_sql2003_evo_array_instantiation(instance):
    assert isinstance(instance, SQL2003_evo_ARRAY)



@given(instance=SQL2003_evo_ARRAY_strategy)
def test_sql2003_evo_array_num_elements_setter(instance):
    original = instance.num_elements
    instance.num_elements = original
    assert instance.num_elements == original
