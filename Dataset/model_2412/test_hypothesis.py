import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DerivedTable,
    BaseTable,
    SQL2003_V3_TriggerDescriptor,
    SQL2003_V3_TypedTable,
    SQL2003_V3_View,
    SQL2003_V3_Restriction,
    UniqueConstraint,
    SQL2003_V3_PrimaryKey,
    SQL2003_V3_Parameter,
    ColumnConstraint,
    SQL2003_V3_NotNull,
    Parameter,
    SQL2003_V3_MethodParameter,
    TableConstraint,
    SQL2003_V3_UniqueConstraint,
    SQL2003_V3_ReferentialConstraint,
    SQL2003_V3_TableCheckConstraint,
    SQL2003_V3_DomainConstraint,
    SQL2003_V3_StructuralComponent,
    SQL2003_V3_Method,
    BehaviouralComponent,
    SQL2003_V3_Procedure,
    SQL2003_V3_Function,
    ConstructedType,
    SQL2003_V3_ROW,
    SQL2003_V3_ReferenceType,
    SQL2003_V3_CollectionType,
    SQL2003_V3_Domain,
    SQL2003_V3_Feature,
    UserDefinedType,
    SQL2003_V3_DistinctType,
    Feature,
    SQL2003_V3_NumericFeature,
    SQL2003_V3_IntervalFeature,
    SQL2003_V3_StringFeature,
    SQL2003_V3_DatetimeFeature,
    DataType,
    SQL2003_V3_PredefinedType,
    SQL2003_V3_UserDefinedType,
    SQL2003_V3_ConstructedType,
    Restriction,
    SQL2003_V3_Trigger,
    SQL2003_V3_TableConstraint,
    SQL2003_V3_ColumnConstraint,
    SQL2003_V3_Table,
    SQL2003_V3_DataType,
    PredefinedType,
    SQL2003_V3_IntervalType,
    SQL2003_V3_BooleanType,
    SQL2003_V3_CharacterStringType,
    SQL2003_V3_NumericType,
    SQL2003_V3_DatetimeType,
    SQL2003_V3_XMLType,
    SQL2003_V3_BinaryStringType,
    SQL2003_V3_ParameterWithMode,
    SQL2003_V3_Schema,
    SQL2003_V3_BehaviouralComponent,
    Table,
    SQL2003_V3_DerivedTable,
    SQL2003_V3_BaseTable,
    SQL2003_V3_StructuredType,
    StructuralComponent,
    SQL2003_V3_Field,
    SQL2003_V3_Column,
    SQL2003_V3_Attribute,
    CollectionType,
    SQL2003_V3_MULTISET,
    SQL2003_V3_ARRAY,
    DatetimeTypes,
    BooleanTypes,
    ReferentialAction,
    NumericRadix,
    IntervalTypes,
    NumericTypes,
    StringFeatures,
    TriggerLevel,
    Multiplier,
    CharacterStringTypes,
    IntervalFeatures,
    Unit,
    NumericFeatures,
    MatchTypes,
    BinaryStringTypes,
    ParameterMode,
    TriggerActionTime,
    XMLTypes,
    TriggerEvent,
    DatetimeFeatures,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_sql2003_v3_triggerdescriptor_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_TriggerDescriptor)


def test_sql2003_v3_triggerdescriptor_constructor_exists():
    assert callable(SQL2003_V3_TriggerDescriptor.__init__)


def test_sql2003_v3_triggerdescriptor_constructor_args():
    sig = inspect.signature(SQL2003_V3_TriggerDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "triggeredAction" in params, "Missing parameter 'triggeredAction'"
    assert "level" in params, "Missing parameter 'level'"
    assert "event" in params, "Missing parameter 'event'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"

def test_sql2003_v3_triggerdescriptor_has_triggeredAction():
    assert hasattr(SQL2003_V3_TriggerDescriptor, "triggeredAction")
    descriptor = None
    for klass in SQL2003_V3_TriggerDescriptor.__mro__:
        if "triggeredAction" in klass.__dict__:
            descriptor = klass.__dict__["triggeredAction"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_triggerdescriptor_has_level():
    assert hasattr(SQL2003_V3_TriggerDescriptor, "level")
    descriptor = None
    for klass in SQL2003_V3_TriggerDescriptor.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_triggerdescriptor_has_event():
    assert hasattr(SQL2003_V3_TriggerDescriptor, "event")
    descriptor = None
    for klass in SQL2003_V3_TriggerDescriptor.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_triggerdescriptor_has_actionTime():
    assert hasattr(SQL2003_V3_TriggerDescriptor, "actionTime")
    descriptor = None
    for klass in SQL2003_V3_TriggerDescriptor.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_typedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_TypedTable)


def test_sql2003_v3_typedtable_constructor_exists():
    assert callable(SQL2003_V3_TypedTable.__init__)


def test_sql2003_v3_typedtable_constructor_args():
    sig = inspect.signature(SQL2003_V3_TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_view_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_View)


def test_sql2003_v3_view_constructor_exists():
    assert callable(SQL2003_V3_View.__init__)


def test_sql2003_v3_view_constructor_args():
    sig = inspect.signature(SQL2003_V3_View.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_restriction_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Restriction)


def test_sql2003_v3_restriction_constructor_exists():
    assert callable(SQL2003_V3_Restriction.__init__)


def test_sql2003_v3_restriction_constructor_args():
    sig = inspect.signature(SQL2003_V3_Restriction.__init__)
    params = list(sig.parameters.keys())



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_primarykey_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_PrimaryKey)


def test_sql2003_v3_primarykey_constructor_exists():
    assert callable(SQL2003_V3_PrimaryKey.__init__)


def test_sql2003_v3_primarykey_constructor_args():
    sig = inspect.signature(SQL2003_V3_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_parameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Parameter)


def test_sql2003_v3_parameter_constructor_exists():
    assert callable(SQL2003_V3_Parameter.__init__)


def test_sql2003_v3_parameter_constructor_args():
    sig = inspect.signature(SQL2003_V3_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_parameter_has_name():
    assert hasattr(SQL2003_V3_Parameter, "name")
    descriptor = None
    for klass in SQL2003_V3_Parameter.__mro__:
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



def test_sql2003_v3_notnull_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_NotNull)


def test_sql2003_v3_notnull_constructor_exists():
    assert callable(SQL2003_V3_NotNull.__init__)


def test_sql2003_v3_notnull_constructor_args():
    sig = inspect.signature(SQL2003_V3_NotNull.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_methodparameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_MethodParameter)


def test_sql2003_v3_methodparameter_constructor_exists():
    assert callable(SQL2003_V3_MethodParameter.__init__)


def test_sql2003_v3_methodparameter_constructor_args():
    sig = inspect.signature(SQL2003_V3_MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_UniqueConstraint)


def test_sql2003_v3_uniqueconstraint_constructor_exists():
    assert callable(SQL2003_V3_UniqueConstraint.__init__)


def test_sql2003_v3_uniqueconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V3_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ReferentialConstraint)


def test_sql2003_v3_referentialconstraint_constructor_exists():
    assert callable(SQL2003_V3_ReferentialConstraint.__init__)


def test_sql2003_v3_referentialconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V3_ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "update_action" in params, "Missing parameter 'update_action'"
    assert "match" in params, "Missing parameter 'match'"
    assert "delete_action" in params, "Missing parameter 'delete_action'"

def test_sql2003_v3_referentialconstraint_has_update_action():
    assert hasattr(SQL2003_V3_ReferentialConstraint, "update_action")
    descriptor = None
    for klass in SQL2003_V3_ReferentialConstraint.__mro__:
        if "update_action" in klass.__dict__:
            descriptor = klass.__dict__["update_action"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_referentialconstraint_has_match():
    assert hasattr(SQL2003_V3_ReferentialConstraint, "match")
    descriptor = None
    for klass in SQL2003_V3_ReferentialConstraint.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_referentialconstraint_has_delete_action():
    assert hasattr(SQL2003_V3_ReferentialConstraint, "delete_action")
    descriptor = None
    for klass in SQL2003_V3_ReferentialConstraint.__mro__:
        if "delete_action" in klass.__dict__:
            descriptor = klass.__dict__["delete_action"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_tablecheckconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_TableCheckConstraint)


def test_sql2003_v3_tablecheckconstraint_constructor_exists():
    assert callable(SQL2003_V3_TableCheckConstraint.__init__)


def test_sql2003_v3_tablecheckconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V3_TableCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sql2003_v3_tablecheckconstraint_has_expression():
    assert hasattr(SQL2003_V3_TableCheckConstraint, "expression")
    descriptor = None
    for klass in SQL2003_V3_TableCheckConstraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_domainconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_DomainConstraint)


def test_sql2003_v3_domainconstraint_constructor_exists():
    assert callable(SQL2003_V3_DomainConstraint.__init__)


def test_sql2003_v3_domainconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V3_DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_StructuralComponent)


def test_sql2003_v3_structuralcomponent_constructor_exists():
    assert callable(SQL2003_V3_StructuralComponent.__init__)


def test_sql2003_v3_structuralcomponent_constructor_args():
    sig = inspect.signature(SQL2003_V3_StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_structuralcomponent_has_name():
    assert hasattr(SQL2003_V3_StructuralComponent, "name")
    descriptor = None
    for klass in SQL2003_V3_StructuralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_method_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Method)


def test_sql2003_v3_method_constructor_exists():
    assert callable(SQL2003_V3_Method.__init__)


def test_sql2003_v3_method_constructor_args():
    sig = inspect.signature(SQL2003_V3_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003_v3_method_has_name():
    assert hasattr(SQL2003_V3_Method, "name")
    descriptor = None
    for klass in SQL2003_V3_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_method_has_body():
    assert hasattr(SQL2003_V3_Method, "body")
    descriptor = None
    for klass in SQL2003_V3_Method.__mro__:
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



def test_sql2003_v3_procedure_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Procedure)


def test_sql2003_v3_procedure_constructor_exists():
    assert callable(SQL2003_V3_Procedure.__init__)


def test_sql2003_v3_procedure_constructor_args():
    sig = inspect.signature(SQL2003_V3_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_function_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Function)


def test_sql2003_v3_function_constructor_exists():
    assert callable(SQL2003_V3_Function.__init__)


def test_sql2003_v3_function_constructor_args():
    sig = inspect.signature(SQL2003_V3_Function.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_row_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ROW)


def test_sql2003_v3_row_constructor_exists():
    assert callable(SQL2003_V3_ROW.__init__)


def test_sql2003_v3_row_constructor_args():
    sig = inspect.signature(SQL2003_V3_ROW.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_referencetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ReferenceType)


def test_sql2003_v3_referencetype_constructor_exists():
    assert callable(SQL2003_V3_ReferenceType.__init__)


def test_sql2003_v3_referencetype_constructor_args():
    sig = inspect.signature(SQL2003_V3_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_collectiontype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_CollectionType)


def test_sql2003_v3_collectiontype_constructor_exists():
    assert callable(SQL2003_V3_CollectionType.__init__)


def test_sql2003_v3_collectiontype_constructor_args():
    sig = inspect.signature(SQL2003_V3_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_domain_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Domain)


def test_sql2003_v3_domain_constructor_exists():
    assert callable(SQL2003_V3_Domain.__init__)


def test_sql2003_v3_domain_constructor_args():
    sig = inspect.signature(SQL2003_V3_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_domain_has_default():
    assert hasattr(SQL2003_V3_Domain, "default")
    descriptor = None
    for klass in SQL2003_V3_Domain.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_domain_has_expression():
    assert hasattr(SQL2003_V3_Domain, "expression")
    descriptor = None
    for klass in SQL2003_V3_Domain.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_domain_has_name():
    assert hasattr(SQL2003_V3_Domain, "name")
    descriptor = None
    for klass in SQL2003_V3_Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_feature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Feature)


def test_sql2003_v3_feature_constructor_exists():
    assert callable(SQL2003_V3_Feature.__init__)


def test_sql2003_v3_feature_constructor_args():
    sig = inspect.signature(SQL2003_V3_Feature.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_distincttype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_DistinctType)


def test_sql2003_v3_distincttype_constructor_exists():
    assert callable(SQL2003_V3_DistinctType.__init__)


def test_sql2003_v3_distincttype_constructor_args():
    sig = inspect.signature(SQL2003_V3_DistinctType.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_numericfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_NumericFeature)


def test_sql2003_v3_numericfeature_constructor_exists():
    assert callable(SQL2003_V3_NumericFeature.__init__)


def test_sql2003_v3_numericfeature_constructor_args():
    sig = inspect.signature(SQL2003_V3_NumericFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_v3_numericfeature_has_key():
    assert hasattr(SQL2003_V3_NumericFeature, "key")
    descriptor = None
    for klass in SQL2003_V3_NumericFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_numericfeature_has_value():
    assert hasattr(SQL2003_V3_NumericFeature, "value")
    descriptor = None
    for klass in SQL2003_V3_NumericFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_intervalfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_IntervalFeature)


def test_sql2003_v3_intervalfeature_constructor_exists():
    assert callable(SQL2003_V3_IntervalFeature.__init__)


def test_sql2003_v3_intervalfeature_constructor_args():
    sig = inspect.signature(SQL2003_V3_IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003_v3_intervalfeature_has_value():
    assert hasattr(SQL2003_V3_IntervalFeature, "value")
    descriptor = None
    for klass in SQL2003_V3_IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_intervalfeature_has_key():
    assert hasattr(SQL2003_V3_IntervalFeature, "key")
    descriptor = None
    for klass in SQL2003_V3_IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_stringfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_StringFeature)


def test_sql2003_v3_stringfeature_constructor_exists():
    assert callable(SQL2003_V3_StringFeature.__init__)


def test_sql2003_v3_stringfeature_constructor_args():
    sig = inspect.signature(SQL2003_V3_StringFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003_v3_stringfeature_has_key():
    assert hasattr(SQL2003_V3_StringFeature, "key")
    descriptor = None
    for klass in SQL2003_V3_StringFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_stringfeature_has_value():
    assert hasattr(SQL2003_V3_StringFeature, "value")
    descriptor = None
    for klass in SQL2003_V3_StringFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_datetimefeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_DatetimeFeature)


def test_sql2003_v3_datetimefeature_constructor_exists():
    assert callable(SQL2003_V3_DatetimeFeature.__init__)


def test_sql2003_v3_datetimefeature_constructor_args():
    sig = inspect.signature(SQL2003_V3_DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003_v3_datetimefeature_has_value():
    assert hasattr(SQL2003_V3_DatetimeFeature, "value")
    descriptor = None
    for klass in SQL2003_V3_DatetimeFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_datetimefeature_has_key():
    assert hasattr(SQL2003_V3_DatetimeFeature, "key")
    descriptor = None
    for klass in SQL2003_V3_DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_PredefinedType)


def test_sql2003_v3_predefinedtype_constructor_exists():
    assert callable(SQL2003_V3_PredefinedType.__init__)


def test_sql2003_v3_predefinedtype_constructor_args():
    sig = inspect.signature(SQL2003_V3_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_UserDefinedType)


def test_sql2003_v3_userdefinedtype_constructor_exists():
    assert callable(SQL2003_V3_UserDefinedType.__init__)


def test_sql2003_v3_userdefinedtype_constructor_args():
    sig = inspect.signature(SQL2003_V3_UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_userdefinedtype_has_name():
    assert hasattr(SQL2003_V3_UserDefinedType, "name")
    descriptor = None
    for klass in SQL2003_V3_UserDefinedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_constructedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ConstructedType)


def test_sql2003_v3_constructedtype_constructor_exists():
    assert callable(SQL2003_V3_ConstructedType.__init__)


def test_sql2003_v3_constructedtype_constructor_args():
    sig = inspect.signature(SQL2003_V3_ConstructedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_constructedtype_has_name():
    assert hasattr(SQL2003_V3_ConstructedType, "name")
    descriptor = None
    for klass in SQL2003_V3_ConstructedType.__mro__:
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



def test_sql2003_v3_trigger_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Trigger)


def test_sql2003_v3_trigger_constructor_exists():
    assert callable(SQL2003_V3_Trigger.__init__)


def test_sql2003_v3_trigger_constructor_args():
    sig = inspect.signature(SQL2003_V3_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_trigger_has_name():
    assert hasattr(SQL2003_V3_Trigger, "name")
    descriptor = None
    for klass in SQL2003_V3_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_TableConstraint)


def test_sql2003_v3_tableconstraint_constructor_exists():
    assert callable(SQL2003_V3_TableConstraint.__init__)


def test_sql2003_v3_tableconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V3_TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_tableconstraint_has_name():
    assert hasattr(SQL2003_V3_TableConstraint, "name")
    descriptor = None
    for klass in SQL2003_V3_TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ColumnConstraint)


def test_sql2003_v3_columnconstraint_constructor_exists():
    assert callable(SQL2003_V3_ColumnConstraint.__init__)


def test_sql2003_v3_columnconstraint_constructor_args():
    sig = inspect.signature(SQL2003_V3_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_table_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Table)


def test_sql2003_v3_table_constructor_exists():
    assert callable(SQL2003_V3_Table.__init__)


def test_sql2003_v3_table_constructor_args():
    sig = inspect.signature(SQL2003_V3_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_table_has_name():
    assert hasattr(SQL2003_V3_Table, "name")
    descriptor = None
    for klass in SQL2003_V3_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_datatype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_DataType)


def test_sql2003_v3_datatype_constructor_exists():
    assert callable(SQL2003_V3_DataType.__init__)


def test_sql2003_v3_datatype_constructor_args():
    sig = inspect.signature(SQL2003_V3_DataType.__init__)
    params = list(sig.parameters.keys())



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_intervaltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_IntervalType)


def test_sql2003_v3_intervaltype_constructor_exists():
    assert callable(SQL2003_V3_IntervalType.__init__)


def test_sql2003_v3_intervaltype_constructor_args():
    sig = inspect.signature(SQL2003_V3_IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v3_intervaltype_has_descriptor():
    assert hasattr(SQL2003_V3_IntervalType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_IntervalType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_booleantype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_BooleanType)


def test_sql2003_v3_booleantype_constructor_exists():
    assert callable(SQL2003_V3_BooleanType.__init__)


def test_sql2003_v3_booleantype_constructor_args():
    sig = inspect.signature(SQL2003_V3_BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v3_booleantype_has_descriptor():
    assert hasattr(SQL2003_V3_BooleanType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_BooleanType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_characterstringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_CharacterStringType)


def test_sql2003_v3_characterstringtype_constructor_exists():
    assert callable(SQL2003_V3_CharacterStringType.__init__)


def test_sql2003_v3_characterstringtype_constructor_args():
    sig = inspect.signature(SQL2003_V3_CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "length_def" in params, "Missing parameter 'length_def'"

def test_sql2003_v3_characterstringtype_has_descriptor():
    assert hasattr(SQL2003_V3_CharacterStringType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_CharacterStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_characterstringtype_has_length_def():
    assert hasattr(SQL2003_V3_CharacterStringType, "length_def")
    descriptor = None
    for klass in SQL2003_V3_CharacterStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_numerictype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_NumericType)


def test_sql2003_v3_numerictype_constructor_exists():
    assert callable(SQL2003_V3_NumericType.__init__)


def test_sql2003_v3_numerictype_constructor_args():
    sig = inspect.signature(SQL2003_V3_NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v3_numerictype_has_descriptor():
    assert hasattr(SQL2003_V3_NumericType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_NumericType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_DatetimeType)


def test_sql2003_v3_datetimetype_constructor_exists():
    assert callable(SQL2003_V3_DatetimeType.__init__)


def test_sql2003_v3_datetimetype_constructor_args():
    sig = inspect.signature(SQL2003_V3_DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v3_datetimetype_has_descriptor():
    assert hasattr(SQL2003_V3_DatetimeType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_DatetimeType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_xmltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_XMLType)


def test_sql2003_v3_xmltype_constructor_exists():
    assert callable(SQL2003_V3_XMLType.__init__)


def test_sql2003_v3_xmltype_constructor_args():
    sig = inspect.signature(SQL2003_V3_XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v3_xmltype_has_descriptor():
    assert hasattr(SQL2003_V3_XMLType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_XMLType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_binarystringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_BinaryStringType)


def test_sql2003_v3_binarystringtype_constructor_exists():
    assert callable(SQL2003_V3_BinaryStringType.__init__)


def test_sql2003_v3_binarystringtype_constructor_args():
    sig = inspect.signature(SQL2003_V3_BinaryStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length_def" in params, "Missing parameter 'length_def'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003_v3_binarystringtype_has_length_def():
    assert hasattr(SQL2003_V3_BinaryStringType, "length_def")
    descriptor = None
    for klass in SQL2003_V3_BinaryStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_binarystringtype_has_descriptor():
    assert hasattr(SQL2003_V3_BinaryStringType, "descriptor")
    descriptor = None
    for klass in SQL2003_V3_BinaryStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_parameterwithmode_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ParameterWithMode)


def test_sql2003_v3_parameterwithmode_constructor_exists():
    assert callable(SQL2003_V3_ParameterWithMode.__init__)


def test_sql2003_v3_parameterwithmode_constructor_args():
    sig = inspect.signature(SQL2003_V3_ParameterWithMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sql2003_v3_parameterwithmode_has_mode():
    assert hasattr(SQL2003_V3_ParameterWithMode, "mode")
    descriptor = None
    for klass in SQL2003_V3_ParameterWithMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_schema_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Schema)


def test_sql2003_v3_schema_constructor_exists():
    assert callable(SQL2003_V3_Schema.__init__)


def test_sql2003_v3_schema_constructor_args():
    sig = inspect.signature(SQL2003_V3_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_schema_has_name():
    assert hasattr(SQL2003_V3_Schema, "name")
    descriptor = None
    for klass in SQL2003_V3_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_BehaviouralComponent)


def test_sql2003_v3_behaviouralcomponent_constructor_exists():
    assert callable(SQL2003_V3_BehaviouralComponent.__init__)


def test_sql2003_v3_behaviouralcomponent_constructor_args():
    sig = inspect.signature(SQL2003_V3_BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003_v3_behaviouralcomponent_has_body():
    assert hasattr(SQL2003_V3_BehaviouralComponent, "body")
    descriptor = None
    for klass in SQL2003_V3_BehaviouralComponent.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_behaviouralcomponent_has_name():
    assert hasattr(SQL2003_V3_BehaviouralComponent, "name")
    descriptor = None
    for klass in SQL2003_V3_BehaviouralComponent.__mro__:
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



def test_sql2003_v3_derivedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_DerivedTable)


def test_sql2003_v3_derivedtable_constructor_exists():
    assert callable(SQL2003_V3_DerivedTable.__init__)


def test_sql2003_v3_derivedtable_constructor_args():
    sig = inspect.signature(SQL2003_V3_DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_sql2003_v3_derivedtable_has_query_expression():
    assert hasattr(SQL2003_V3_DerivedTable, "query_expression")
    descriptor = None
    for klass in SQL2003_V3_DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_basetable_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_BaseTable)


def test_sql2003_v3_basetable_constructor_exists():
    assert callable(SQL2003_V3_BaseTable.__init__)


def test_sql2003_v3_basetable_constructor_args():
    sig = inspect.signature(SQL2003_V3_BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_structuredtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_StructuredType)


def test_sql2003_v3_structuredtype_constructor_exists():
    assert callable(SQL2003_V3_StructuredType.__init__)


def test_sql2003_v3_structuredtype_constructor_args():
    sig = inspect.signature(SQL2003_V3_StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"
    assert "is_final" in params, "Missing parameter 'is_final'"

def test_sql2003_v3_structuredtype_has_is_instantiable():
    assert hasattr(SQL2003_V3_StructuredType, "is_instantiable")
    descriptor = None
    for klass in SQL2003_V3_StructuredType.__mro__:
        if "is_instantiable" in klass.__dict__:
            descriptor = klass.__dict__["is_instantiable"]
            break
    assert isinstance(descriptor, property)

def test_sql2003_v3_structuredtype_has_is_final():
    assert hasattr(SQL2003_V3_StructuredType, "is_final")
    descriptor = None
    for klass in SQL2003_V3_StructuredType.__mro__:
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



def test_sql2003_v3_field_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Field)


def test_sql2003_v3_field_constructor_exists():
    assert callable(SQL2003_V3_Field.__init__)


def test_sql2003_v3_field_constructor_args():
    sig = inspect.signature(SQL2003_V3_Field.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_column_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Column)


def test_sql2003_v3_column_constructor_exists():
    assert callable(SQL2003_V3_Column.__init__)


def test_sql2003_v3_column_constructor_args():
    sig = inspect.signature(SQL2003_V3_Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_v3_column_has_default():
    assert hasattr(SQL2003_V3_Column, "default")
    descriptor = None
    for klass in SQL2003_V3_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_sql2003_v3_attribute_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_Attribute)


def test_sql2003_v3_attribute_constructor_exists():
    assert callable(SQL2003_V3_Attribute.__init__)


def test_sql2003_v3_attribute_constructor_args():
    sig = inspect.signature(SQL2003_V3_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003_v3_attribute_has_default():
    assert hasattr(SQL2003_V3_Attribute, "default")
    descriptor = None
    for klass in SQL2003_V3_Attribute.__mro__:
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



def test_sql2003_v3_multiset_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_MULTISET)


def test_sql2003_v3_multiset_constructor_exists():
    assert callable(SQL2003_V3_MULTISET.__init__)


def test_sql2003_v3_multiset_constructor_args():
    sig = inspect.signature(SQL2003_V3_MULTISET.__init__)
    params = list(sig.parameters.keys())



def test_sql2003_v3_array_is_not_abstract():
    assert not inspect.isabstract(SQL2003_V3_ARRAY)


def test_sql2003_v3_array_constructor_exists():
    assert callable(SQL2003_V3_ARRAY.__init__)


def test_sql2003_v3_array_constructor_args():
    sig = inspect.signature(SQL2003_V3_ARRAY.__init__)
    params = list(sig.parameters.keys())
    assert "num_elements" in params, "Missing parameter 'num_elements'"

def test_sql2003_v3_array_has_num_elements():
    assert hasattr(SQL2003_V3_ARRAY, "num_elements")
    descriptor = None
    for klass in SQL2003_V3_ARRAY.__mro__:
        if "num_elements" in klass.__dict__:
            descriptor = klass.__dict__["num_elements"]
            break
    assert isinstance(descriptor, property)

def test_datetimetypes_exists():
    # Check that the Enumeration exists
    assert DatetimeTypes is not None

def test_datetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeTypes]
    expected_literals = [
        "DATE",
        "TIMESTAMPWITHTIMEZONE",
        "TIMESTAMPWITHOUTTIMEZONE",
        "TIMEWITHTIMEZONE",
        "TIMEWITHOUTTIMEZONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeTypes"

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

def test_referentialaction_exists():
    # Check that the Enumeration exists
    assert ReferentialAction is not None

def test_referentialaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialAction]
    expected_literals = [
        "CASCADE",
        "NO_ACTION",
        "SET_DEFAULT",
        "RESTRICT",
        "SET_NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialAction"

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

def test_intervaltypes_exists():
    # Check that the Enumeration exists
    assert IntervalTypes is not None

def test_intervaltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalTypes]
    expected_literals = [
        "YEAR_MONTH",
        "HOUR_MINUTE",
        "MINUTE_SECOND",
        "DAY_HOUR",
        "YEAR",
        "DAY",
        "SECOND",
        "HOUR_SECOND",
        "HOUR",
        "MONTH",
        "MINUTE",
        "DAY_SECOND",
        "DAY_MINUTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalTypes"

def test_numerictypes_exists():
    # Check that the Enumeration exists
    assert NumericTypes is not None

def test_numerictypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericTypes]
    expected_literals = [
        "FLOAT",
        "DOUBLEPRECISION",
        "DECIMAL",
        "SMALLINT",
        "INTEGER",
        "NUMERIC",
        "REAL",
        "BIGINT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericTypes"

def test_stringfeatures_exists():
    # Check that the Enumeration exists
    assert StringFeatures is not None

def test_stringfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringFeatures]
    expected_literals = [
        "multiplier",
        "unit",
        "length",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringFeatures"

def test_triggerlevel_exists():
    # Check that the Enumeration exists
    assert TriggerLevel is not None

def test_triggerlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerLevel]
    expected_literals = [
        "STATEMENT_LEVEL",
        "ROW_LEVEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerLevel"

def test_multiplier_exists():
    # Check that the Enumeration exists
    assert Multiplier is not None

def test_multiplier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Multiplier]
    expected_literals = [
        "T",
        "P",
        "M",
        "G",
        "K",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_characterstringtypes_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypes is not None

def test_characterstringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypes]
    expected_literals = [
        "CHARACTERVARYING",
        "CHARACTER",
        "CHARACTERLARGEOBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypes"

def test_intervalfeatures_exists():
    # Check that the Enumeration exists
    assert IntervalFeatures is not None

def test_intervalfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalFeatures]
    expected_literals = [
        "leading_precision",
        "end_leading_precision",
        "second_precision",
        "start_leading_precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalFeatures"

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

def test_matchtypes_exists():
    # Check that the Enumeration exists
    assert MatchTypes is not None

def test_matchtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatchTypes]
    expected_literals = [
        "SIMPLE",
        "TOTAL",
        "PARTIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchTypes"

def test_binarystringtypes_exists():
    # Check that the Enumeration exists
    assert BinaryStringTypes is not None

def test_binarystringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryStringTypes]
    expected_literals = [
        "BINARYLARGEOBJECT",
        "BINARYVARYING",
        "BINARY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryStringTypes"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "IN",
        "OUT",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

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

def test_triggerevent_exists():
    # Check that the Enumeration exists
    assert TriggerEvent is not None

def test_triggerevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerEvent]
    expected_literals = [
        "INSERT",
        "UPDATE",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerEvent"

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
DerivedTable_strategy = st.builds(
    DerivedTable,
)
BaseTable_strategy = st.builds(
    BaseTable,
)
SQL2003_V3_TriggerDescriptor_strategy = st.builds(
    SQL2003_V3_TriggerDescriptor,
    triggeredAction=
        safe_text,
    level=
        safe_text,
    event=
        safe_text,
    actionTime=
        safe_text
)
SQL2003_V3_TypedTable_strategy = st.builds(
    SQL2003_V3_TypedTable,
)
SQL2003_V3_View_strategy = st.builds(
    SQL2003_V3_View,
)
SQL2003_V3_Restriction_strategy = st.builds(
    SQL2003_V3_Restriction,
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
SQL2003_V3_PrimaryKey_strategy = st.builds(
    SQL2003_V3_PrimaryKey,
)
SQL2003_V3_Parameter_strategy = st.builds(
    SQL2003_V3_Parameter,
    name=
        safe_text
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
SQL2003_V3_NotNull_strategy = st.builds(
    SQL2003_V3_NotNull,
)
Parameter_strategy = st.builds(
    Parameter,
)
SQL2003_V3_MethodParameter_strategy = st.builds(
    SQL2003_V3_MethodParameter,
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
SQL2003_V3_UniqueConstraint_strategy = st.builds(
    SQL2003_V3_UniqueConstraint,
)
SQL2003_V3_ReferentialConstraint_strategy = st.builds(
    SQL2003_V3_ReferentialConstraint,
    update_action=
        safe_text,
    match=
        safe_text,
    delete_action=
        safe_text
)
SQL2003_V3_TableCheckConstraint_strategy = st.builds(
    SQL2003_V3_TableCheckConstraint,
    expression=
        safe_text
)
SQL2003_V3_DomainConstraint_strategy = st.builds(
    SQL2003_V3_DomainConstraint,
)
SQL2003_V3_StructuralComponent_strategy = st.builds(
    SQL2003_V3_StructuralComponent,
    name=
        safe_text
)
SQL2003_V3_Method_strategy = st.builds(
    SQL2003_V3_Method,
    name=
        safe_text,
    body=
        safe_text
)
BehaviouralComponent_strategy = st.builds(
    BehaviouralComponent,
)
SQL2003_V3_Procedure_strategy = st.builds(
    SQL2003_V3_Procedure,
)
SQL2003_V3_Function_strategy = st.builds(
    SQL2003_V3_Function,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
SQL2003_V3_ROW_strategy = st.builds(
    SQL2003_V3_ROW,
)
SQL2003_V3_ReferenceType_strategy = st.builds(
    SQL2003_V3_ReferenceType,
)
SQL2003_V3_CollectionType_strategy = st.builds(
    SQL2003_V3_CollectionType,
)
SQL2003_V3_Domain_strategy = st.builds(
    SQL2003_V3_Domain,
    default=
        safe_text,
    expression=
        safe_text,
    name=
        safe_text
)
SQL2003_V3_Feature_strategy = st.builds(
    SQL2003_V3_Feature,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
SQL2003_V3_DistinctType_strategy = st.builds(
    SQL2003_V3_DistinctType,
)
Feature_strategy = st.builds(
    Feature,
)
SQL2003_V3_NumericFeature_strategy = st.builds(
    SQL2003_V3_NumericFeature,
    key=
        safe_text,
    value=
        safe_text
)
SQL2003_V3_IntervalFeature_strategy = st.builds(
    SQL2003_V3_IntervalFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003_V3_StringFeature_strategy = st.builds(
    SQL2003_V3_StringFeature,
    key=
        safe_text,
    value=
        safe_text
)
SQL2003_V3_DatetimeFeature_strategy = st.builds(
    SQL2003_V3_DatetimeFeature,
    value=
        safe_text,
    key=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
SQL2003_V3_PredefinedType_strategy = st.builds(
    SQL2003_V3_PredefinedType,
)
SQL2003_V3_UserDefinedType_strategy = st.builds(
    SQL2003_V3_UserDefinedType,
    name=
        safe_text
)
SQL2003_V3_ConstructedType_strategy = st.builds(
    SQL2003_V3_ConstructedType,
    name=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
SQL2003_V3_Trigger_strategy = st.builds(
    SQL2003_V3_Trigger,
    name=
        safe_text
)
SQL2003_V3_TableConstraint_strategy = st.builds(
    SQL2003_V3_TableConstraint,
    name=
        safe_text
)
SQL2003_V3_ColumnConstraint_strategy = st.builds(
    SQL2003_V3_ColumnConstraint,
)
SQL2003_V3_Table_strategy = st.builds(
    SQL2003_V3_Table,
    name=
        safe_text
)
SQL2003_V3_DataType_strategy = st.builds(
    SQL2003_V3_DataType,
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
SQL2003_V3_IntervalType_strategy = st.builds(
    SQL2003_V3_IntervalType,
    descriptor=
        safe_text
)
SQL2003_V3_BooleanType_strategy = st.builds(
    SQL2003_V3_BooleanType,
    descriptor=
        safe_text
)
SQL2003_V3_CharacterStringType_strategy = st.builds(
    SQL2003_V3_CharacterStringType,
    descriptor=
        safe_text,
    length_def=
        safe_text
)
SQL2003_V3_NumericType_strategy = st.builds(
    SQL2003_V3_NumericType,
    descriptor=
        safe_text
)
SQL2003_V3_DatetimeType_strategy = st.builds(
    SQL2003_V3_DatetimeType,
    descriptor=
        safe_text
)
SQL2003_V3_XMLType_strategy = st.builds(
    SQL2003_V3_XMLType,
    descriptor=
        safe_text
)
SQL2003_V3_BinaryStringType_strategy = st.builds(
    SQL2003_V3_BinaryStringType,
    length_def=
        safe_text,
    descriptor=
        safe_text
)
SQL2003_V3_ParameterWithMode_strategy = st.builds(
    SQL2003_V3_ParameterWithMode,
    mode=
        safe_text
)
SQL2003_V3_Schema_strategy = st.builds(
    SQL2003_V3_Schema,
    name=
        safe_text
)
SQL2003_V3_BehaviouralComponent_strategy = st.builds(
    SQL2003_V3_BehaviouralComponent,
    body=
        safe_text,
    name=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SQL2003_V3_DerivedTable_strategy = st.builds(
    SQL2003_V3_DerivedTable,
    query_expression=
        safe_text
)
SQL2003_V3_BaseTable_strategy = st.builds(
    SQL2003_V3_BaseTable,
)
SQL2003_V3_StructuredType_strategy = st.builds(
    SQL2003_V3_StructuredType,
    is_instantiable=
        st.booleans(),
    is_final=
        st.booleans()
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
SQL2003_V3_Field_strategy = st.builds(
    SQL2003_V3_Field,
)
SQL2003_V3_Column_strategy = st.builds(
    SQL2003_V3_Column,
    default=
        safe_text
)
SQL2003_V3_Attribute_strategy = st.builds(
    SQL2003_V3_Attribute,
    default=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
SQL2003_V3_MULTISET_strategy = st.builds(
    SQL2003_V3_MULTISET,
)
SQL2003_V3_ARRAY_strategy = st.builds(
    SQL2003_V3_ARRAY,
    num_elements=
        safe_text
)

@given(instance=DerivedTable_strategy)
@settings(max_examples=50)
def test_derivedtable_instantiation(instance):
    assert isinstance(instance, DerivedTable)

@given(instance=BaseTable_strategy)
@settings(max_examples=50)
def test_basetable_instantiation(instance):
    assert isinstance(instance, BaseTable)

@given(instance=SQL2003_V3_TriggerDescriptor_strategy)
@settings(max_examples=50)
def test_sql2003_v3_triggerdescriptor_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_TriggerDescriptor)



@given(instance=SQL2003_V3_TriggerDescriptor_strategy)
def test_sql2003_v3_triggerdescriptor_triggeredAction_setter(instance):
    original = instance.triggeredAction
    instance.triggeredAction = original
    assert instance.triggeredAction == original



@given(instance=SQL2003_V3_TriggerDescriptor_strategy)
def test_sql2003_v3_triggerdescriptor_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=SQL2003_V3_TriggerDescriptor_strategy)
def test_sql2003_v3_triggerdescriptor_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=SQL2003_V3_TriggerDescriptor_strategy)
def test_sql2003_v3_triggerdescriptor_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original

@given(instance=SQL2003_V3_TypedTable_strategy)
@settings(max_examples=50)
def test_sql2003_v3_typedtable_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_TypedTable)

@given(instance=SQL2003_V3_View_strategy)
@settings(max_examples=50)
def test_sql2003_v3_view_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_View)

@given(instance=SQL2003_V3_Restriction_strategy)
@settings(max_examples=50)
def test_sql2003_v3_restriction_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Restriction)

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=SQL2003_V3_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql2003_v3_primarykey_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_PrimaryKey)

@given(instance=SQL2003_V3_Parameter_strategy)
@settings(max_examples=50)
def test_sql2003_v3_parameter_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Parameter)



@given(instance=SQL2003_V3_Parameter_strategy)
def test_sql2003_v3_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=SQL2003_V3_NotNull_strategy)
@settings(max_examples=50)
def test_sql2003_v3_notnull_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_NotNull)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=SQL2003_V3_MethodParameter_strategy)
@settings(max_examples=50)
def test_sql2003_v3_methodparameter_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_MethodParameter)

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=SQL2003_V3_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v3_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_UniqueConstraint)

@given(instance=SQL2003_V3_ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v3_referentialconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ReferentialConstraint)



@given(instance=SQL2003_V3_ReferentialConstraint_strategy)
def test_sql2003_v3_referentialconstraint_update_action_setter(instance):
    original = instance.update_action
    instance.update_action = original
    assert instance.update_action == original



@given(instance=SQL2003_V3_ReferentialConstraint_strategy)
def test_sql2003_v3_referentialconstraint_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original



@given(instance=SQL2003_V3_ReferentialConstraint_strategy)
def test_sql2003_v3_referentialconstraint_delete_action_setter(instance):
    original = instance.delete_action
    instance.delete_action = original
    assert instance.delete_action == original

@given(instance=SQL2003_V3_TableCheckConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v3_tablecheckconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_TableCheckConstraint)



@given(instance=SQL2003_V3_TableCheckConstraint_strategy)
def test_sql2003_v3_tablecheckconstraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=SQL2003_V3_DomainConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v3_domainconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_DomainConstraint)

@given(instance=SQL2003_V3_StructuralComponent_strategy)
@settings(max_examples=50)
def test_sql2003_v3_structuralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_StructuralComponent)



@given(instance=SQL2003_V3_StructuralComponent_strategy)
def test_sql2003_v3_structuralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_Method_strategy)
@settings(max_examples=50)
def test_sql2003_v3_method_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Method)



@given(instance=SQL2003_V3_Method_strategy)
def test_sql2003_v3_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SQL2003_V3_Method_strategy)
def test_sql2003_v3_method_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, BehaviouralComponent)

@given(instance=SQL2003_V3_Procedure_strategy)
@settings(max_examples=50)
def test_sql2003_v3_procedure_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Procedure)

@given(instance=SQL2003_V3_Function_strategy)
@settings(max_examples=50)
def test_sql2003_v3_function_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Function)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=SQL2003_V3_ROW_strategy)
@settings(max_examples=50)
def test_sql2003_v3_row_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ROW)

@given(instance=SQL2003_V3_ReferenceType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_referencetype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ReferenceType)

@given(instance=SQL2003_V3_CollectionType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_collectiontype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_CollectionType)

@given(instance=SQL2003_V3_Domain_strategy)
@settings(max_examples=50)
def test_sql2003_v3_domain_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Domain)



@given(instance=SQL2003_V3_Domain_strategy)
def test_sql2003_v3_domain_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=SQL2003_V3_Domain_strategy)
def test_sql2003_v3_domain_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=SQL2003_V3_Domain_strategy)
def test_sql2003_v3_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_Feature_strategy)
@settings(max_examples=50)
def test_sql2003_v3_feature_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Feature)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=SQL2003_V3_DistinctType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_distincttype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_DistinctType)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=SQL2003_V3_NumericFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v3_numericfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_NumericFeature)



@given(instance=SQL2003_V3_NumericFeature_strategy)
def test_sql2003_v3_numericfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_V3_NumericFeature_strategy)
def test_sql2003_v3_numericfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003_V3_IntervalFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v3_intervalfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_IntervalFeature)



@given(instance=SQL2003_V3_IntervalFeature_strategy)
def test_sql2003_v3_intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=SQL2003_V3_IntervalFeature_strategy)
def test_sql2003_v3_intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003_V3_StringFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v3_stringfeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_StringFeature)



@given(instance=SQL2003_V3_StringFeature_strategy)
def test_sql2003_v3_stringfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=SQL2003_V3_StringFeature_strategy)
def test_sql2003_v3_stringfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003_V3_DatetimeFeature_strategy)
@settings(max_examples=50)
def test_sql2003_v3_datetimefeature_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_DatetimeFeature)



@given(instance=SQL2003_V3_DatetimeFeature_strategy)
def test_sql2003_v3_datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=SQL2003_V3_DatetimeFeature_strategy)
def test_sql2003_v3_datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=SQL2003_V3_PredefinedType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_predefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_PredefinedType)

@given(instance=SQL2003_V3_UserDefinedType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_userdefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_UserDefinedType)



@given(instance=SQL2003_V3_UserDefinedType_strategy)
def test_sql2003_v3_userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_ConstructedType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_constructedtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ConstructedType)



@given(instance=SQL2003_V3_ConstructedType_strategy)
def test_sql2003_v3_constructedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=SQL2003_V3_Trigger_strategy)
@settings(max_examples=50)
def test_sql2003_v3_trigger_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Trigger)



@given(instance=SQL2003_V3_Trigger_strategy)
def test_sql2003_v3_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_TableConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v3_tableconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_TableConstraint)



@given(instance=SQL2003_V3_TableConstraint_strategy)
def test_sql2003_v3_tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql2003_v3_columnconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ColumnConstraint)

@given(instance=SQL2003_V3_Table_strategy)
@settings(max_examples=50)
def test_sql2003_v3_table_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Table)



@given(instance=SQL2003_V3_Table_strategy)
def test_sql2003_v3_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_DataType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_datatype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_DataType)

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=SQL2003_V3_IntervalType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_intervaltype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_IntervalType)



@given(instance=SQL2003_V3_IntervalType_strategy)
def test_sql2003_v3_intervaltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V3_BooleanType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_booleantype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_BooleanType)



@given(instance=SQL2003_V3_BooleanType_strategy)
def test_sql2003_v3_booleantype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V3_CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_characterstringtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_CharacterStringType)



@given(instance=SQL2003_V3_CharacterStringType_strategy)
def test_sql2003_v3_characterstringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=SQL2003_V3_CharacterStringType_strategy)
def test_sql2003_v3_characterstringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003_V3_NumericType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_numerictype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_NumericType)



@given(instance=SQL2003_V3_NumericType_strategy)
def test_sql2003_v3_numerictype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V3_DatetimeType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_datetimetype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_DatetimeType)



@given(instance=SQL2003_V3_DatetimeType_strategy)
def test_sql2003_v3_datetimetype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V3_XMLType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_xmltype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_XMLType)



@given(instance=SQL2003_V3_XMLType_strategy)
def test_sql2003_v3_xmltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V3_BinaryStringType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_binarystringtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_BinaryStringType)



@given(instance=SQL2003_V3_BinaryStringType_strategy)
def test_sql2003_v3_binarystringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original



@given(instance=SQL2003_V3_BinaryStringType_strategy)
def test_sql2003_v3_binarystringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003_V3_ParameterWithMode_strategy)
@settings(max_examples=50)
def test_sql2003_v3_parameterwithmode_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ParameterWithMode)



@given(instance=SQL2003_V3_ParameterWithMode_strategy)
def test_sql2003_v3_parameterwithmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SQL2003_V3_Schema_strategy)
@settings(max_examples=50)
def test_sql2003_v3_schema_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Schema)



@given(instance=SQL2003_V3_Schema_strategy)
def test_sql2003_v3_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003_V3_BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_sql2003_v3_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_BehaviouralComponent)



@given(instance=SQL2003_V3_BehaviouralComponent_strategy)
def test_sql2003_v3_behaviouralcomponent_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=SQL2003_V3_BehaviouralComponent_strategy)
def test_sql2003_v3_behaviouralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SQL2003_V3_DerivedTable_strategy)
@settings(max_examples=50)
def test_sql2003_v3_derivedtable_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_DerivedTable)



@given(instance=SQL2003_V3_DerivedTable_strategy)
def test_sql2003_v3_derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=SQL2003_V3_BaseTable_strategy)
@settings(max_examples=50)
def test_sql2003_v3_basetable_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_BaseTable)

@given(instance=SQL2003_V3_StructuredType_strategy)
@settings(max_examples=50)
def test_sql2003_v3_structuredtype_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_StructuredType)



@given(instance=SQL2003_V3_StructuredType_strategy)
def test_sql2003_v3_structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original



@given(instance=SQL2003_V3_StructuredType_strategy)
def test_sql2003_v3_structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=SQL2003_V3_Field_strategy)
@settings(max_examples=50)
def test_sql2003_v3_field_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Field)

@given(instance=SQL2003_V3_Column_strategy)
@settings(max_examples=50)
def test_sql2003_v3_column_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Column)



@given(instance=SQL2003_V3_Column_strategy)
def test_sql2003_v3_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=SQL2003_V3_Attribute_strategy)
@settings(max_examples=50)
def test_sql2003_v3_attribute_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_Attribute)



@given(instance=SQL2003_V3_Attribute_strategy)
def test_sql2003_v3_attribute_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=SQL2003_V3_MULTISET_strategy)
@settings(max_examples=50)
def test_sql2003_v3_multiset_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_MULTISET)

@given(instance=SQL2003_V3_ARRAY_strategy)
@settings(max_examples=50)
def test_sql2003_v3_array_instantiation(instance):
    assert isinstance(instance, SQL2003_V3_ARRAY)



@given(instance=SQL2003_V3_ARRAY_strategy)
def test_sql2003_v3_array_num_elements_setter(instance):
    original = instance.num_elements
    instance.num_elements = original
    assert instance.num_elements == original
