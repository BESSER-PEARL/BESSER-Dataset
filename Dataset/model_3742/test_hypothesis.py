import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DerivedTable,
    ORDB4ORA_View,
    Table,
    ORDB4ORA_DerivedTable,
    ORDB4ORA_Trigger,
    ORDB4ORA_TypedTable,
    ORDB4ORA_StoredNestedTable,
    ORDB4ORA_Parameter,
    ORDB4ORA_StructuralComponent,
    ORDB4ORA_Restriction,
    ORDB4ORA_Package,
    ORDB4ORA_Operation,
    ORDB4ORA_Method,
    Operation,
    ORDB4ORA_Procedure,
    ORDB4ORA_Function,
    ORDB4ORA_Feature,
    Parameter,
    ORDB4ORA_OperationParameter,
    ORDB4ORA_MethodParameter,
    ORDB4ORA_Model,
    ORDB4ORA_Datatype,
    ORDB4ORA_Table,
    Restriction,
    ORDB4ORA_ForeignKey,
    ORDB4ORA_NotNull,
    ORDB4ORA_PrimaryKey,
    ORDB4ORA_Unique,
    ORDB4ORA_Check,
    Feature,
    ORDB4ORA_NumberFeature,
    ORDB4ORA_RowFeature,
    ORDB4ORA_DatetimeFeature,
    ORDB4ORA_RawFeature,
    ORDB4ORA_IntervalFeature,
    ORDB4ORA_CharacterFeature,
    BuiltInType,
    ORDB4ORA_BuiltInNumberType,
    ORDB4ORA_LongAndRawType,
    ORDB4ORA_ROWIDType,
    ORDB4ORA_DatetimeType,
    ORDB4ORA_LOBType,
    ORDB4ORA_BuiltInCharacterType,
    Datatype,
    ORDB4ORA_ReferenceType,
    ORDB4ORA_NestedTableType,
    ORDB4ORA_Varray,
    ORDB4ORA_BasicDataType,
    ORDB4ORA_StructuredType,
    StructuralComponent,
    ORDB4ORA_Column,
    ORDB4ORA_Attribute,
    SuppliedType,
    ORDB4ORA_MediaType,
    ORDB4ORA_XMLType,
    ORDB4ORA_SpacialType,
    ORDB4ORA_AnyType,
    BasicDataType,
    ORDB4ORA_SuppliedType,
    ORDB4ORA_BuiltInType,
    ORDB4ORA_ANSIType,
    ANSIType,
    ORDB4ORA_ANSICharacterType,
    ORDB4ORA_ANSINumberType,
    SuppliedXMLTypes,
    BuiltInCharacterSemantics,
    ANSICharacterTypes,
    ParameterMode,
    TriggerActionTime,
    SuppliedMediaTypes,
    SuppliedAnyTypes,
    BuiltInLOBType,
    DatetimeFeatures,
    RawFeatures,
    RowFeatures,
    NumberFeatures,
    BuiltInDatetimeTypes,
    BuiltInROWIDType,
    ANSINumberTypes,
    TriggerEvent,
    ONDELETEActions,
    BuiltInCharacterTypes,
    SuppliedSpacialTypes,
    BuiltNumberTypes,
    BuiltInLongAndRawTypes,
    CharacterFeatures,
    IntervalFeatures,
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



def test_ordb4ora_view_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_View)


def test_ordb4ora_view_constructor_exists():
    assert callable(ORDB4ORA_View.__init__)


def test_ordb4ora_view_constructor_args():
    sig = inspect.signature(ORDB4ORA_View.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_derivedtable_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_DerivedTable)


def test_ordb4ora_derivedtable_constructor_exists():
    assert callable(ORDB4ORA_DerivedTable.__init__)


def test_ordb4ora_derivedtable_constructor_args():
    sig = inspect.signature(ORDB4ORA_DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_ordb4ora_derivedtable_has_query_expression():
    assert hasattr(ORDB4ORA_DerivedTable, "query_expression")
    descriptor = None
    for klass in ORDB4ORA_DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_trigger_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Trigger)


def test_ordb4ora_trigger_constructor_exists():
    assert callable(ORDB4ORA_Trigger.__init__)


def test_ordb4ora_trigger_constructor_args():
    sig = inspect.signature(ORDB4ORA_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "Event" in params, "Missing parameter 'Event'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Action" in params, "Missing parameter 'Action'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_ordb4ora_trigger_has_Event():
    assert hasattr(ORDB4ORA_Trigger, "Event")
    descriptor = None
    for klass in ORDB4ORA_Trigger.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_trigger_has_Name():
    assert hasattr(ORDB4ORA_Trigger, "Name")
    descriptor = None
    for klass in ORDB4ORA_Trigger.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_trigger_has_Action():
    assert hasattr(ORDB4ORA_Trigger, "Action")
    descriptor = None
    for klass in ORDB4ORA_Trigger.__mro__:
        if "Action" in klass.__dict__:
            descriptor = klass.__dict__["Action"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_trigger_has_Body():
    assert hasattr(ORDB4ORA_Trigger, "Body")
    descriptor = None
    for klass in ORDB4ORA_Trigger.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_typedtable_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_TypedTable)


def test_ordb4ora_typedtable_constructor_exists():
    assert callable(ORDB4ORA_TypedTable.__init__)


def test_ordb4ora_typedtable_constructor_args():
    sig = inspect.signature(ORDB4ORA_TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_storednestedtable_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_StoredNestedTable)


def test_ordb4ora_storednestedtable_constructor_exists():
    assert callable(ORDB4ORA_StoredNestedTable.__init__)


def test_ordb4ora_storednestedtable_constructor_args():
    sig = inspect.signature(ORDB4ORA_StoredNestedTable.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_storednestedtable_has_Name():
    assert hasattr(ORDB4ORA_StoredNestedTable, "Name")
    descriptor = None
    for klass in ORDB4ORA_StoredNestedTable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_parameter_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Parameter)


def test_ordb4ora_parameter_constructor_exists():
    assert callable(ORDB4ORA_Parameter.__init__)


def test_ordb4ora_parameter_constructor_args():
    sig = inspect.signature(ORDB4ORA_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_parameter_has_Name():
    assert hasattr(ORDB4ORA_Parameter, "Name")
    descriptor = None
    for klass in ORDB4ORA_Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_StructuralComponent)


def test_ordb4ora_structuralcomponent_constructor_exists():
    assert callable(ORDB4ORA_StructuralComponent.__init__)


def test_ordb4ora_structuralcomponent_constructor_args():
    sig = inspect.signature(ORDB4ORA_StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_structuralcomponent_has_Name():
    assert hasattr(ORDB4ORA_StructuralComponent, "Name")
    descriptor = None
    for klass in ORDB4ORA_StructuralComponent.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_restriction_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Restriction)


def test_ordb4ora_restriction_constructor_exists():
    assert callable(ORDB4ORA_Restriction.__init__)


def test_ordb4ora_restriction_constructor_args():
    sig = inspect.signature(ORDB4ORA_Restriction.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_package_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Package)


def test_ordb4ora_package_constructor_exists():
    assert callable(ORDB4ORA_Package.__init__)


def test_ordb4ora_package_constructor_args():
    sig = inspect.signature(ORDB4ORA_Package.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_package_has_Name():
    assert hasattr(ORDB4ORA_Package, "Name")
    descriptor = None
    for klass in ORDB4ORA_Package.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_operation_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Operation)


def test_ordb4ora_operation_constructor_exists():
    assert callable(ORDB4ORA_Operation.__init__)


def test_ordb4ora_operation_constructor_args():
    sig = inspect.signature(ORDB4ORA_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_ordb4ora_operation_has_Name():
    assert hasattr(ORDB4ORA_Operation, "Name")
    descriptor = None
    for klass in ORDB4ORA_Operation.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_operation_has_Body():
    assert hasattr(ORDB4ORA_Operation, "Body")
    descriptor = None
    for klass in ORDB4ORA_Operation.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_method_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Method)


def test_ordb4ora_method_constructor_exists():
    assert callable(ORDB4ORA_Method.__init__)


def test_ordb4ora_method_constructor_args():
    sig = inspect.signature(ORDB4ORA_Method.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_method_has_Body():
    assert hasattr(ORDB4ORA_Method, "Body")
    descriptor = None
    for klass in ORDB4ORA_Method.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_method_has_Name():
    assert hasattr(ORDB4ORA_Method, "Name")
    descriptor = None
    for klass in ORDB4ORA_Method.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_procedure_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Procedure)


def test_ordb4ora_procedure_constructor_exists():
    assert callable(ORDB4ORA_Procedure.__init__)


def test_ordb4ora_procedure_constructor_args():
    sig = inspect.signature(ORDB4ORA_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_function_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Function)


def test_ordb4ora_function_constructor_exists():
    assert callable(ORDB4ORA_Function.__init__)


def test_ordb4ora_function_constructor_args():
    sig = inspect.signature(ORDB4ORA_Function.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_feature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Feature)


def test_ordb4ora_feature_constructor_exists():
    assert callable(ORDB4ORA_Feature.__init__)


def test_ordb4ora_feature_constructor_args():
    sig = inspect.signature(ORDB4ORA_Feature.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_operationparameter_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_OperationParameter)


def test_ordb4ora_operationparameter_constructor_exists():
    assert callable(ORDB4ORA_OperationParameter.__init__)


def test_ordb4ora_operationparameter_constructor_args():
    sig = inspect.signature(ORDB4ORA_OperationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "Mode" in params, "Missing parameter 'Mode'"

def test_ordb4ora_operationparameter_has_Mode():
    assert hasattr(ORDB4ORA_OperationParameter, "Mode")
    descriptor = None
    for klass in ORDB4ORA_OperationParameter.__mro__:
        if "Mode" in klass.__dict__:
            descriptor = klass.__dict__["Mode"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_methodparameter_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_MethodParameter)


def test_ordb4ora_methodparameter_constructor_exists():
    assert callable(ORDB4ORA_MethodParameter.__init__)


def test_ordb4ora_methodparameter_constructor_args():
    sig = inspect.signature(ORDB4ORA_MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_model_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Model)


def test_ordb4ora_model_constructor_exists():
    assert callable(ORDB4ORA_Model.__init__)


def test_ordb4ora_model_constructor_args():
    sig = inspect.signature(ORDB4ORA_Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_model_has_Name():
    assert hasattr(ORDB4ORA_Model, "Name")
    descriptor = None
    for klass in ORDB4ORA_Model.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_datatype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Datatype)


def test_ordb4ora_datatype_constructor_exists():
    assert callable(ORDB4ORA_Datatype.__init__)


def test_ordb4ora_datatype_constructor_args():
    sig = inspect.signature(ORDB4ORA_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_table_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Table)


def test_ordb4ora_table_constructor_exists():
    assert callable(ORDB4ORA_Table.__init__)


def test_ordb4ora_table_constructor_args():
    sig = inspect.signature(ORDB4ORA_Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_table_has_Name():
    assert hasattr(ORDB4ORA_Table, "Name")
    descriptor = None
    for klass in ORDB4ORA_Table.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_restriction_is_not_abstract():
    assert not inspect.isabstract(Restriction)


def test_restriction_constructor_exists():
    assert callable(Restriction.__init__)


def test_restriction_constructor_args():
    sig = inspect.signature(Restriction.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_ForeignKey)


def test_ordb4ora_foreignkey_constructor_exists():
    assert callable(ORDB4ORA_ForeignKey.__init__)


def test_ordb4ora_foreignkey_constructor_args():
    sig = inspect.signature(ORDB4ORA_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "OnDelete" in params, "Missing parameter 'OnDelete'"

def test_ordb4ora_foreignkey_has_Name():
    assert hasattr(ORDB4ORA_ForeignKey, "Name")
    descriptor = None
    for klass in ORDB4ORA_ForeignKey.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_foreignkey_has_OnDelete():
    assert hasattr(ORDB4ORA_ForeignKey, "OnDelete")
    descriptor = None
    for klass in ORDB4ORA_ForeignKey.__mro__:
        if "OnDelete" in klass.__dict__:
            descriptor = klass.__dict__["OnDelete"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_notnull_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_NotNull)


def test_ordb4ora_notnull_constructor_exists():
    assert callable(ORDB4ORA_NotNull.__init__)


def test_ordb4ora_notnull_constructor_args():
    sig = inspect.signature(ORDB4ORA_NotNull.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_notnull_has_Name():
    assert hasattr(ORDB4ORA_NotNull, "Name")
    descriptor = None
    for klass in ORDB4ORA_NotNull.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_primarykey_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_PrimaryKey)


def test_ordb4ora_primarykey_constructor_exists():
    assert callable(ORDB4ORA_PrimaryKey.__init__)


def test_ordb4ora_primarykey_constructor_args():
    sig = inspect.signature(ORDB4ORA_PrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_primarykey_has_Name():
    assert hasattr(ORDB4ORA_PrimaryKey, "Name")
    descriptor = None
    for klass in ORDB4ORA_PrimaryKey.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_unique_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Unique)


def test_ordb4ora_unique_constructor_exists():
    assert callable(ORDB4ORA_Unique.__init__)


def test_ordb4ora_unique_constructor_args():
    sig = inspect.signature(ORDB4ORA_Unique.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_unique_has_Name():
    assert hasattr(ORDB4ORA_Unique, "Name")
    descriptor = None
    for klass in ORDB4ORA_Unique.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_check_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Check)


def test_ordb4ora_check_constructor_exists():
    assert callable(ORDB4ORA_Check.__init__)


def test_ordb4ora_check_constructor_args():
    sig = inspect.signature(ORDB4ORA_Check.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Condition" in params, "Missing parameter 'Condition'"

def test_ordb4ora_check_has_Name():
    assert hasattr(ORDB4ORA_Check, "Name")
    descriptor = None
    for klass in ORDB4ORA_Check.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_check_has_Condition():
    assert hasattr(ORDB4ORA_Check, "Condition")
    descriptor = None
    for klass in ORDB4ORA_Check.__mro__:
        if "Condition" in klass.__dict__:
            descriptor = klass.__dict__["Condition"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_numberfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_NumberFeature)


def test_ordb4ora_numberfeature_constructor_exists():
    assert callable(ORDB4ORA_NumberFeature.__init__)


def test_ordb4ora_numberfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA_NumberFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora_numberfeature_has_value():
    assert hasattr(ORDB4ORA_NumberFeature, "value")
    descriptor = None
    for klass in ORDB4ORA_NumberFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_numberfeature_has_key():
    assert hasattr(ORDB4ORA_NumberFeature, "key")
    descriptor = None
    for klass in ORDB4ORA_NumberFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_rowfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_RowFeature)


def test_ordb4ora_rowfeature_constructor_exists():
    assert callable(ORDB4ORA_RowFeature.__init__)


def test_ordb4ora_rowfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA_RowFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora_rowfeature_has_value():
    assert hasattr(ORDB4ORA_RowFeature, "value")
    descriptor = None
    for klass in ORDB4ORA_RowFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_rowfeature_has_key():
    assert hasattr(ORDB4ORA_RowFeature, "key")
    descriptor = None
    for klass in ORDB4ORA_RowFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_datetimefeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_DatetimeFeature)


def test_ordb4ora_datetimefeature_constructor_exists():
    assert callable(ORDB4ORA_DatetimeFeature.__init__)


def test_ordb4ora_datetimefeature_constructor_args():
    sig = inspect.signature(ORDB4ORA_DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora_datetimefeature_has_value():
    assert hasattr(ORDB4ORA_DatetimeFeature, "value")
    descriptor = None
    for klass in ORDB4ORA_DatetimeFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimefeature_has_key():
    assert hasattr(ORDB4ORA_DatetimeFeature, "key")
    descriptor = None
    for klass in ORDB4ORA_DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_rawfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_RawFeature)


def test_ordb4ora_rawfeature_constructor_exists():
    assert callable(ORDB4ORA_RawFeature.__init__)


def test_ordb4ora_rawfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA_RawFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_ordb4ora_rawfeature_has_key():
    assert hasattr(ORDB4ORA_RawFeature, "key")
    descriptor = None
    for klass in ORDB4ORA_RawFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_rawfeature_has_value():
    assert hasattr(ORDB4ORA_RawFeature, "value")
    descriptor = None
    for klass in ORDB4ORA_RawFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_intervalfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_IntervalFeature)


def test_ordb4ora_intervalfeature_constructor_exists():
    assert callable(ORDB4ORA_IntervalFeature.__init__)


def test_ordb4ora_intervalfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA_IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_ordb4ora_intervalfeature_has_key():
    assert hasattr(ORDB4ORA_IntervalFeature, "key")
    descriptor = None
    for klass in ORDB4ORA_IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_intervalfeature_has_value():
    assert hasattr(ORDB4ORA_IntervalFeature, "value")
    descriptor = None
    for klass in ORDB4ORA_IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_characterfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_CharacterFeature)


def test_ordb4ora_characterfeature_constructor_exists():
    assert callable(ORDB4ORA_CharacterFeature.__init__)


def test_ordb4ora_characterfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA_CharacterFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora_characterfeature_has_value():
    assert hasattr(ORDB4ORA_CharacterFeature, "value")
    descriptor = None
    for klass in ORDB4ORA_CharacterFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_characterfeature_has_key():
    assert hasattr(ORDB4ORA_CharacterFeature, "key")
    descriptor = None
    for klass in ORDB4ORA_CharacterFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_builtinnumbertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_BuiltInNumberType)


def test_ordb4ora_builtinnumbertype_constructor_exists():
    assert callable(ORDB4ORA_BuiltInNumberType.__init__)


def test_ordb4ora_builtinnumbertype_constructor_args():
    sig = inspect.signature(ORDB4ORA_BuiltInNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "Precision_Mn" in params, "Missing parameter 'Precision_Mn'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "Precision_Max" in params, "Missing parameter 'Precision_Max'"
    assert "Scale_Min" in params, "Missing parameter 'Scale_Min'"
    assert "Scale_Max" in params, "Missing parameter 'Scale_Max'"

def test_ordb4ora_builtinnumbertype_has_Precision_Mn():
    assert hasattr(ORDB4ORA_BuiltInNumberType, "Precision_Mn")
    descriptor = None
    for klass in ORDB4ORA_BuiltInNumberType.__mro__:
        if "Precision_Mn" in klass.__dict__:
            descriptor = klass.__dict__["Precision_Mn"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtinnumbertype_has_Descriptor():
    assert hasattr(ORDB4ORA_BuiltInNumberType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_BuiltInNumberType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtinnumbertype_has_Precision_Max():
    assert hasattr(ORDB4ORA_BuiltInNumberType, "Precision_Max")
    descriptor = None
    for klass in ORDB4ORA_BuiltInNumberType.__mro__:
        if "Precision_Max" in klass.__dict__:
            descriptor = klass.__dict__["Precision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtinnumbertype_has_Scale_Min():
    assert hasattr(ORDB4ORA_BuiltInNumberType, "Scale_Min")
    descriptor = None
    for klass in ORDB4ORA_BuiltInNumberType.__mro__:
        if "Scale_Min" in klass.__dict__:
            descriptor = klass.__dict__["Scale_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtinnumbertype_has_Scale_Max():
    assert hasattr(ORDB4ORA_BuiltInNumberType, "Scale_Max")
    descriptor = None
    for klass in ORDB4ORA_BuiltInNumberType.__mro__:
        if "Scale_Max" in klass.__dict__:
            descriptor = klass.__dict__["Scale_Max"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_longandrawtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_LongAndRawType)


def test_ordb4ora_longandrawtype_constructor_exists():
    assert callable(ORDB4ORA_LongAndRawType.__init__)


def test_ordb4ora_longandrawtype_constructor_args():
    sig = inspect.signature(ORDB4ORA_LongAndRawType.__init__)
    params = list(sig.parameters.keys())
    assert "Size_Max" in params, "Missing parameter 'Size_Max'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "Size_Min" in params, "Missing parameter 'Size_Min'"

def test_ordb4ora_longandrawtype_has_Size_Max():
    assert hasattr(ORDB4ORA_LongAndRawType, "Size_Max")
    descriptor = None
    for klass in ORDB4ORA_LongAndRawType.__mro__:
        if "Size_Max" in klass.__dict__:
            descriptor = klass.__dict__["Size_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_longandrawtype_has_Descriptor():
    assert hasattr(ORDB4ORA_LongAndRawType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_LongAndRawType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_longandrawtype_has_Size_Min():
    assert hasattr(ORDB4ORA_LongAndRawType, "Size_Min")
    descriptor = None
    for klass in ORDB4ORA_LongAndRawType.__mro__:
        if "Size_Min" in klass.__dict__:
            descriptor = klass.__dict__["Size_Min"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_rowidtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_ROWIDType)


def test_ordb4ora_rowidtype_constructor_exists():
    assert callable(ORDB4ORA_ROWIDType.__init__)


def test_ordb4ora_rowidtype_constructor_args():
    sig = inspect.signature(ORDB4ORA_ROWIDType.__init__)
    params = list(sig.parameters.keys())
    assert "Size_Max" in params, "Missing parameter 'Size_Max'"
    assert "Size_Min" in params, "Missing parameter 'Size_Min'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_rowidtype_has_Size_Max():
    assert hasattr(ORDB4ORA_ROWIDType, "Size_Max")
    descriptor = None
    for klass in ORDB4ORA_ROWIDType.__mro__:
        if "Size_Max" in klass.__dict__:
            descriptor = klass.__dict__["Size_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_rowidtype_has_Size_Min():
    assert hasattr(ORDB4ORA_ROWIDType, "Size_Min")
    descriptor = None
    for klass in ORDB4ORA_ROWIDType.__mro__:
        if "Size_Min" in klass.__dict__:
            descriptor = klass.__dict__["Size_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_rowidtype_has_Descriptor():
    assert hasattr(ORDB4ORA_ROWIDType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_ROWIDType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_datetimetype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_DatetimeType)


def test_ordb4ora_datetimetype_constructor_exists():
    assert callable(ORDB4ORA_DatetimeType.__init__)


def test_ordb4ora_datetimetype_constructor_args():
    sig = inspect.signature(ORDB4ORA_DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "SecondPrecision_Max" in params, "Missing parameter 'SecondPrecision_Max'"
    assert "DayPrecision_Max" in params, "Missing parameter 'DayPrecision_Max'"
    assert "SecondPrecision_Min" in params, "Missing parameter 'SecondPrecision_Min'"
    assert "DayPrecision_Min" in params, "Missing parameter 'DayPrecision_Min'"
    assert "YearPrecision_Max" in params, "Missing parameter 'YearPrecision_Max'"
    assert "DayPrecision_Def" in params, "Missing parameter 'DayPrecision_Def'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "YearPrecision_Def" in params, "Missing parameter 'YearPrecision_Def'"
    assert "YearPrecision_Min" in params, "Missing parameter 'YearPrecision_Min'"
    assert "SecondPrecision_Def" in params, "Missing parameter 'SecondPrecision_Def'"

def test_ordb4ora_datetimetype_has_SecondPrecision_Max():
    assert hasattr(ORDB4ORA_DatetimeType, "SecondPrecision_Max")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "SecondPrecision_Max" in klass.__dict__:
            descriptor = klass.__dict__["SecondPrecision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_DayPrecision_Max():
    assert hasattr(ORDB4ORA_DatetimeType, "DayPrecision_Max")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "DayPrecision_Max" in klass.__dict__:
            descriptor = klass.__dict__["DayPrecision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_SecondPrecision_Min():
    assert hasattr(ORDB4ORA_DatetimeType, "SecondPrecision_Min")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "SecondPrecision_Min" in klass.__dict__:
            descriptor = klass.__dict__["SecondPrecision_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_DayPrecision_Min():
    assert hasattr(ORDB4ORA_DatetimeType, "DayPrecision_Min")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "DayPrecision_Min" in klass.__dict__:
            descriptor = klass.__dict__["DayPrecision_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_YearPrecision_Max():
    assert hasattr(ORDB4ORA_DatetimeType, "YearPrecision_Max")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "YearPrecision_Max" in klass.__dict__:
            descriptor = klass.__dict__["YearPrecision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_DayPrecision_Def():
    assert hasattr(ORDB4ORA_DatetimeType, "DayPrecision_Def")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "DayPrecision_Def" in klass.__dict__:
            descriptor = klass.__dict__["DayPrecision_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_Descriptor():
    assert hasattr(ORDB4ORA_DatetimeType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_YearPrecision_Def():
    assert hasattr(ORDB4ORA_DatetimeType, "YearPrecision_Def")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "YearPrecision_Def" in klass.__dict__:
            descriptor = klass.__dict__["YearPrecision_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_YearPrecision_Min():
    assert hasattr(ORDB4ORA_DatetimeType, "YearPrecision_Min")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "YearPrecision_Min" in klass.__dict__:
            descriptor = klass.__dict__["YearPrecision_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_datetimetype_has_SecondPrecision_Def():
    assert hasattr(ORDB4ORA_DatetimeType, "SecondPrecision_Def")
    descriptor = None
    for klass in ORDB4ORA_DatetimeType.__mro__:
        if "SecondPrecision_Def" in klass.__dict__:
            descriptor = klass.__dict__["SecondPrecision_Def"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_lobtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_LOBType)


def test_ordb4ora_lobtype_constructor_exists():
    assert callable(ORDB4ORA_LOBType.__init__)


def test_ordb4ora_lobtype_constructor_args():
    sig = inspect.signature(ORDB4ORA_LOBType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_lobtype_has_Descriptor():
    assert hasattr(ORDB4ORA_LOBType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_LOBType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_builtincharactertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_BuiltInCharacterType)


def test_ordb4ora_builtincharactertype_constructor_exists():
    assert callable(ORDB4ORA_BuiltInCharacterType.__init__)


def test_ordb4ora_builtincharactertype_constructor_args():
    sig = inspect.signature(ORDB4ORA_BuiltInCharacterType.__init__)
    params = list(sig.parameters.keys())
    assert "Semantic" in params, "Missing parameter 'Semantic'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "Size_Min" in params, "Missing parameter 'Size_Min'"
    assert "Size_Def" in params, "Missing parameter 'Size_Def'"
    assert "Size_Max" in params, "Missing parameter 'Size_Max'"

def test_ordb4ora_builtincharactertype_has_Semantic():
    assert hasattr(ORDB4ORA_BuiltInCharacterType, "Semantic")
    descriptor = None
    for klass in ORDB4ORA_BuiltInCharacterType.__mro__:
        if "Semantic" in klass.__dict__:
            descriptor = klass.__dict__["Semantic"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtincharactertype_has_Descriptor():
    assert hasattr(ORDB4ORA_BuiltInCharacterType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_BuiltInCharacterType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtincharactertype_has_Size_Min():
    assert hasattr(ORDB4ORA_BuiltInCharacterType, "Size_Min")
    descriptor = None
    for klass in ORDB4ORA_BuiltInCharacterType.__mro__:
        if "Size_Min" in klass.__dict__:
            descriptor = klass.__dict__["Size_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtincharactertype_has_Size_Def():
    assert hasattr(ORDB4ORA_BuiltInCharacterType, "Size_Def")
    descriptor = None
    for klass in ORDB4ORA_BuiltInCharacterType.__mro__:
        if "Size_Def" in klass.__dict__:
            descriptor = klass.__dict__["Size_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_builtincharactertype_has_Size_Max():
    assert hasattr(ORDB4ORA_BuiltInCharacterType, "Size_Max")
    descriptor = None
    for klass in ORDB4ORA_BuiltInCharacterType.__mro__:
        if "Size_Max" in klass.__dict__:
            descriptor = klass.__dict__["Size_Max"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(Datatype)


def test_datatype_constructor_exists():
    assert callable(Datatype.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(Datatype.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_referencetype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_ReferenceType)


def test_ordb4ora_referencetype_constructor_exists():
    assert callable(ORDB4ORA_ReferenceType.__init__)


def test_ordb4ora_referencetype_constructor_args():
    sig = inspect.signature(ORDB4ORA_ReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_referencetype_has_Name():
    assert hasattr(ORDB4ORA_ReferenceType, "Name")
    descriptor = None
    for klass in ORDB4ORA_ReferenceType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_nestedtabletype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_NestedTableType)


def test_ordb4ora_nestedtabletype_constructor_exists():
    assert callable(ORDB4ORA_NestedTableType.__init__)


def test_ordb4ora_nestedtabletype_constructor_args():
    sig = inspect.signature(ORDB4ORA_NestedTableType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_nestedtabletype_has_Name():
    assert hasattr(ORDB4ORA_NestedTableType, "Name")
    descriptor = None
    for klass in ORDB4ORA_NestedTableType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_varray_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Varray)


def test_ordb4ora_varray_constructor_exists():
    assert callable(ORDB4ORA_Varray.__init__)


def test_ordb4ora_varray_constructor_args():
    sig = inspect.signature(ORDB4ORA_Varray.__init__)
    params = list(sig.parameters.keys())
    assert "NumElements" in params, "Missing parameter 'NumElements'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora_varray_has_NumElements():
    assert hasattr(ORDB4ORA_Varray, "NumElements")
    descriptor = None
    for klass in ORDB4ORA_Varray.__mro__:
        if "NumElements" in klass.__dict__:
            descriptor = klass.__dict__["NumElements"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_varray_has_Name():
    assert hasattr(ORDB4ORA_Varray, "Name")
    descriptor = None
    for klass in ORDB4ORA_Varray.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_basicdatatype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_BasicDataType)


def test_ordb4ora_basicdatatype_constructor_exists():
    assert callable(ORDB4ORA_BasicDataType.__init__)


def test_ordb4ora_basicdatatype_constructor_args():
    sig = inspect.signature(ORDB4ORA_BasicDataType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_structuredtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_StructuredType)


def test_ordb4ora_structuredtype_constructor_exists():
    assert callable(ORDB4ORA_StructuredType.__init__)


def test_ordb4ora_structuredtype_constructor_args():
    sig = inspect.signature(ORDB4ORA_StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_final" in params, "Missing parameter 'is_final'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"

def test_ordb4ora_structuredtype_has_is_final():
    assert hasattr(ORDB4ORA_StructuredType, "is_final")
    descriptor = None
    for klass in ORDB4ORA_StructuredType.__mro__:
        if "is_final" in klass.__dict__:
            descriptor = klass.__dict__["is_final"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_structuredtype_has_Name():
    assert hasattr(ORDB4ORA_StructuredType, "Name")
    descriptor = None
    for klass in ORDB4ORA_StructuredType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora_structuredtype_has_is_instantiable():
    assert hasattr(ORDB4ORA_StructuredType, "is_instantiable")
    descriptor = None
    for klass in ORDB4ORA_StructuredType.__mro__:
        if "is_instantiable" in klass.__dict__:
            descriptor = klass.__dict__["is_instantiable"]
            break
    assert isinstance(descriptor, property)



def test_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(StructuralComponent)


def test_structuralcomponent_constructor_exists():
    assert callable(StructuralComponent.__init__)


def test_structuralcomponent_constructor_args():
    sig = inspect.signature(StructuralComponent.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_column_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Column)


def test_ordb4ora_column_constructor_exists():
    assert callable(ORDB4ORA_Column.__init__)


def test_ordb4ora_column_constructor_args():
    sig = inspect.signature(ORDB4ORA_Column.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_attribute_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_Attribute)


def test_ordb4ora_attribute_constructor_exists():
    assert callable(ORDB4ORA_Attribute.__init__)


def test_ordb4ora_attribute_constructor_args():
    sig = inspect.signature(ORDB4ORA_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "Default" in params, "Missing parameter 'Default'"

def test_ordb4ora_attribute_has_Default():
    assert hasattr(ORDB4ORA_Attribute, "Default")
    descriptor = None
    for klass in ORDB4ORA_Attribute.__mro__:
        if "Default" in klass.__dict__:
            descriptor = klass.__dict__["Default"]
            break
    assert isinstance(descriptor, property)



def test_suppliedtype_is_not_abstract():
    assert not inspect.isabstract(SuppliedType)


def test_suppliedtype_constructor_exists():
    assert callable(SuppliedType.__init__)


def test_suppliedtype_constructor_args():
    sig = inspect.signature(SuppliedType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_mediatype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_MediaType)


def test_ordb4ora_mediatype_constructor_exists():
    assert callable(ORDB4ORA_MediaType.__init__)


def test_ordb4ora_mediatype_constructor_args():
    sig = inspect.signature(ORDB4ORA_MediaType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_mediatype_has_Descriptor():
    assert hasattr(ORDB4ORA_MediaType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_MediaType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_xmltype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_XMLType)


def test_ordb4ora_xmltype_constructor_exists():
    assert callable(ORDB4ORA_XMLType.__init__)


def test_ordb4ora_xmltype_constructor_args():
    sig = inspect.signature(ORDB4ORA_XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_xmltype_has_Descriptor():
    assert hasattr(ORDB4ORA_XMLType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_XMLType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_spacialtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_SpacialType)


def test_ordb4ora_spacialtype_constructor_exists():
    assert callable(ORDB4ORA_SpacialType.__init__)


def test_ordb4ora_spacialtype_constructor_args():
    sig = inspect.signature(ORDB4ORA_SpacialType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_spacialtype_has_Descriptor():
    assert hasattr(ORDB4ORA_SpacialType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_SpacialType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_anytype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_AnyType)


def test_ordb4ora_anytype_constructor_exists():
    assert callable(ORDB4ORA_AnyType.__init__)


def test_ordb4ora_anytype_constructor_args():
    sig = inspect.signature(ORDB4ORA_AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_anytype_has_Descriptor():
    assert hasattr(ORDB4ORA_AnyType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_AnyType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_basicdatatype_is_not_abstract():
    assert not inspect.isabstract(BasicDataType)


def test_basicdatatype_constructor_exists():
    assert callable(BasicDataType.__init__)


def test_basicdatatype_constructor_args():
    sig = inspect.signature(BasicDataType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_suppliedtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_SuppliedType)


def test_ordb4ora_suppliedtype_constructor_exists():
    assert callable(ORDB4ORA_SuppliedType.__init__)


def test_ordb4ora_suppliedtype_constructor_args():
    sig = inspect.signature(ORDB4ORA_SuppliedType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_builtintype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_BuiltInType)


def test_ordb4ora_builtintype_constructor_exists():
    assert callable(ORDB4ORA_BuiltInType.__init__)


def test_ordb4ora_builtintype_constructor_args():
    sig = inspect.signature(ORDB4ORA_BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_ansitype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_ANSIType)


def test_ordb4ora_ansitype_constructor_exists():
    assert callable(ORDB4ORA_ANSIType.__init__)


def test_ordb4ora_ansitype_constructor_args():
    sig = inspect.signature(ORDB4ORA_ANSIType.__init__)
    params = list(sig.parameters.keys())



def test_ansitype_is_not_abstract():
    assert not inspect.isabstract(ANSIType)


def test_ansitype_constructor_exists():
    assert callable(ANSIType.__init__)


def test_ansitype_constructor_args():
    sig = inspect.signature(ANSIType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora_ansicharactertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_ANSICharacterType)


def test_ordb4ora_ansicharactertype_constructor_exists():
    assert callable(ORDB4ORA_ANSICharacterType.__init__)


def test_ordb4ora_ansicharactertype_constructor_args():
    sig = inspect.signature(ORDB4ORA_ANSICharacterType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_ansicharactertype_has_Descriptor():
    assert hasattr(ORDB4ORA_ANSICharacterType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_ANSICharacterType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora_ansinumbertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA_ANSINumberType)


def test_ordb4ora_ansinumbertype_constructor_exists():
    assert callable(ORDB4ORA_ANSINumberType.__init__)


def test_ordb4ora_ansinumbertype_constructor_args():
    sig = inspect.signature(ORDB4ORA_ANSINumberType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora_ansinumbertype_has_Descriptor():
    assert hasattr(ORDB4ORA_ANSINumberType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA_ANSINumberType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_suppliedxmltypes_exists():
    # Check that the Enumeration exists
    assert SuppliedXMLTypes is not None

def test_suppliedxmltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuppliedXMLTypes]
    expected_literals = [
        "URITYPE",
        "XMLTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuppliedXMLTypes"

def test_builtincharactersemantics_exists():
    # Check that the Enumeration exists
    assert BuiltInCharacterSemantics is not None

def test_builtincharactersemantics_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInCharacterSemantics]
    expected_literals = [
        "BYTE",
        "CHAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInCharacterSemantics"

def test_ansicharactertypes_exists():
    # Check that the Enumeration exists
    assert ANSICharacterTypes is not None

def test_ansicharactertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ANSICharacterTypes]
    expected_literals = [
        "NCHARVARYING",
        "NATIONALCHARVARYING",
        "NATIONALCHAR",
        "NATIONALCHARACTER",
        "VARCHAR",
        "CHARACTER",
        "NATIONALCHARACTERVARYING",
        "CHARVARYING",
        "CHARACTERVARYING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ANSICharacterTypes"

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

def test_triggeractiontime_exists():
    # Check that the Enumeration exists
    assert TriggerActionTime is not None

def test_triggeractiontime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerActionTime]
    expected_literals = [
        "INSTEADOF",
        "BEFORE",
        "AFTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerActionTime"

def test_suppliedmediatypes_exists():
    # Check that the Enumeration exists
    assert SuppliedMediaTypes is not None

def test_suppliedmediatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuppliedMediaTypes]
    expected_literals = [
        "ORDDoc",
        "SI_COLORHISTOGRAM",
        "ORDAudio",
        "SI_TEXTURE",
        "SI_FEATURELIST",
        "SI_STILLIMAGE",
        "SI_COLOR",
        "ORDImage",
        "SI_POSITIONALCOLOR",
        "ORDVideo",
        "SI_AVERAGECOLOR",
        "ORDImageSignature",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuppliedMediaTypes"

def test_suppliedanytypes_exists():
    # Check that the Enumeration exists
    assert SuppliedAnyTypes is not None

def test_suppliedanytypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuppliedAnyTypes]
    expected_literals = [
        "SYSANYDATASET",
        "SYSANYDATA",
        "SYSANYTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuppliedAnyTypes"

def test_builtinlobtype_exists():
    # Check that the Enumeration exists
    assert BuiltInLOBType is not None

def test_builtinlobtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInLOBType]
    expected_literals = [
        "BFILE",
        "BLOB",
        "CLOB",
        "NLOB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInLOBType"

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

def test_rawfeatures_exists():
    # Check that the Enumeration exists
    assert RawFeatures is not None

def test_rawfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RawFeatures]
    expected_literals = [
        "size",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RawFeatures"

def test_rowfeatures_exists():
    # Check that the Enumeration exists
    assert RowFeatures is not None

def test_rowfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RowFeatures]
    expected_literals = [
        "size",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RowFeatures"

def test_numberfeatures_exists():
    # Check that the Enumeration exists
    assert NumberFeatures is not None

def test_numberfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberFeatures]
    expected_literals = [
        "size",
        "scale",
        "precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberFeatures"

def test_builtindatetimetypes_exists():
    # Check that the Enumeration exists
    assert BuiltInDatetimeTypes is not None

def test_builtindatetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInDatetimeTypes]
    expected_literals = [
        "TIMESTAMPWITHTIMEZONE",
        "DATE",
        "INTERVALDAYTOSECOND",
        "INTERVALYEARTOMONTH",
        "TIMESTAMP",
        "TIMESTAMPWITHLOCALTIMEZONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInDatetimeTypes"

def test_builtinrowidtype_exists():
    # Check that the Enumeration exists
    assert BuiltInROWIDType is not None

def test_builtinrowidtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInROWIDType]
    expected_literals = [
        "UROWID",
        "ROWID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInROWIDType"

def test_ansinumbertypes_exists():
    # Check that the Enumeration exists
    assert ANSINumberTypes is not None

def test_ansinumbertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ANSINumberTypes]
    expected_literals = [
        "REAL",
        "DOUBLEPRECISION",
        "INTEGER",
        "INT",
        "SMALLINT",
        "FLOAT",
        "NUMERIC",
        "DECIMAL",
        "DEC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ANSINumberTypes"

def test_triggerevent_exists():
    # Check that the Enumeration exists
    assert TriggerEvent is not None

def test_triggerevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerEvent]
    expected_literals = [
        "DELETE",
        "UPDATE",
        "INSERT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerEvent"

def test_ondeleteactions_exists():
    # Check that the Enumeration exists
    assert ONDELETEActions is not None

def test_ondeleteactions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ONDELETEActions]
    expected_literals = [
        "CASCADE",
        "SETNULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ONDELETEActions"

def test_builtincharactertypes_exists():
    # Check that the Enumeration exists
    assert BuiltInCharacterTypes is not None

def test_builtincharactertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInCharacterTypes]
    expected_literals = [
        "NVARCHAR2",
        "NCHAR",
        "CHAR",
        "VARCHAR2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInCharacterTypes"

def test_suppliedspacialtypes_exists():
    # Check that the Enumeration exists
    assert SuppliedSpacialTypes is not None

def test_suppliedspacialtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuppliedSpacialTypes]
    expected_literals = [
        "SDO_GEOMETRY",
        "SDO_TOPO_GEOMETRY",
        "SDO_RASTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuppliedSpacialTypes"

def test_builtnumbertypes_exists():
    # Check that the Enumeration exists
    assert BuiltNumberTypes is not None

def test_builtnumbertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltNumberTypes]
    expected_literals = [
        "NUMBER",
        "BINARY_FLOAT",
        "BINARY_DOUBLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltNumberTypes"

def test_builtinlongandrawtypes_exists():
    # Check that the Enumeration exists
    assert BuiltInLongAndRawTypes is not None

def test_builtinlongandrawtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInLongAndRawTypes]
    expected_literals = [
        "LONG",
        "RAW",
        "LONGRAW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInLongAndRawTypes"

def test_characterfeatures_exists():
    # Check that the Enumeration exists
    assert CharacterFeatures is not None

def test_characterfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterFeatures]
    expected_literals = [
        "semantic",
        "size",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterFeatures"

def test_intervalfeatures_exists():
    # Check that the Enumeration exists
    assert IntervalFeatures is not None

def test_intervalfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalFeatures]
    expected_literals = [
        "second_precision",
        "day_precision",
        "year_precision",
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
DerivedTable_strategy = st.builds(
    DerivedTable,
)
ORDB4ORA_View_strategy = st.builds(
    ORDB4ORA_View,
)
Table_strategy = st.builds(
    Table,
)
ORDB4ORA_DerivedTable_strategy = st.builds(
    ORDB4ORA_DerivedTable,
    query_expression=
        safe_text
)
ORDB4ORA_Trigger_strategy = st.builds(
    ORDB4ORA_Trigger,
    Event=
        safe_text,
    Name=
        safe_text,
    Action=
        safe_text,
    Body=
        safe_text
)
ORDB4ORA_TypedTable_strategy = st.builds(
    ORDB4ORA_TypedTable,
)
ORDB4ORA_StoredNestedTable_strategy = st.builds(
    ORDB4ORA_StoredNestedTable,
    Name=
        safe_text
)
ORDB4ORA_Parameter_strategy = st.builds(
    ORDB4ORA_Parameter,
    Name=
        safe_text
)
ORDB4ORA_StructuralComponent_strategy = st.builds(
    ORDB4ORA_StructuralComponent,
    Name=
        safe_text
)
ORDB4ORA_Restriction_strategy = st.builds(
    ORDB4ORA_Restriction,
)
ORDB4ORA_Package_strategy = st.builds(
    ORDB4ORA_Package,
    Name=
        safe_text
)
ORDB4ORA_Operation_strategy = st.builds(
    ORDB4ORA_Operation,
    Name=
        safe_text,
    Body=
        safe_text
)
ORDB4ORA_Method_strategy = st.builds(
    ORDB4ORA_Method,
    Body=
        safe_text,
    Name=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
ORDB4ORA_Procedure_strategy = st.builds(
    ORDB4ORA_Procedure,
)
ORDB4ORA_Function_strategy = st.builds(
    ORDB4ORA_Function,
)
ORDB4ORA_Feature_strategy = st.builds(
    ORDB4ORA_Feature,
)
Parameter_strategy = st.builds(
    Parameter,
)
ORDB4ORA_OperationParameter_strategy = st.builds(
    ORDB4ORA_OperationParameter,
    Mode=
        safe_text
)
ORDB4ORA_MethodParameter_strategy = st.builds(
    ORDB4ORA_MethodParameter,
)
ORDB4ORA_Model_strategy = st.builds(
    ORDB4ORA_Model,
    Name=
        safe_text
)
ORDB4ORA_Datatype_strategy = st.builds(
    ORDB4ORA_Datatype,
)
ORDB4ORA_Table_strategy = st.builds(
    ORDB4ORA_Table,
    Name=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
ORDB4ORA_ForeignKey_strategy = st.builds(
    ORDB4ORA_ForeignKey,
    Name=
        safe_text,
    OnDelete=
        safe_text
)
ORDB4ORA_NotNull_strategy = st.builds(
    ORDB4ORA_NotNull,
    Name=
        safe_text
)
ORDB4ORA_PrimaryKey_strategy = st.builds(
    ORDB4ORA_PrimaryKey,
    Name=
        safe_text
)
ORDB4ORA_Unique_strategy = st.builds(
    ORDB4ORA_Unique,
    Name=
        safe_text
)
ORDB4ORA_Check_strategy = st.builds(
    ORDB4ORA_Check,
    Name=
        safe_text,
    Condition=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
ORDB4ORA_NumberFeature_strategy = st.builds(
    ORDB4ORA_NumberFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA_RowFeature_strategy = st.builds(
    ORDB4ORA_RowFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA_DatetimeFeature_strategy = st.builds(
    ORDB4ORA_DatetimeFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA_RawFeature_strategy = st.builds(
    ORDB4ORA_RawFeature,
    key=
        safe_text,
    value=
        safe_text
)
ORDB4ORA_IntervalFeature_strategy = st.builds(
    ORDB4ORA_IntervalFeature,
    key=
        safe_text,
    value=
        safe_text
)
ORDB4ORA_CharacterFeature_strategy = st.builds(
    ORDB4ORA_CharacterFeature,
    value=
        safe_text,
    key=
        safe_text
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
ORDB4ORA_BuiltInNumberType_strategy = st.builds(
    ORDB4ORA_BuiltInNumberType,
    Precision_Mn=
        st.integers(),
    Descriptor=
        safe_text,
    Precision_Max=
        st.integers(),
    Scale_Min=
        st.integers(),
    Scale_Max=
        st.integers()
)
ORDB4ORA_LongAndRawType_strategy = st.builds(
    ORDB4ORA_LongAndRawType,
    Size_Max=
        st.integers(),
    Descriptor=
        safe_text,
    Size_Min=
        st.integers()
)
ORDB4ORA_ROWIDType_strategy = st.builds(
    ORDB4ORA_ROWIDType,
    Size_Max=
        st.integers(),
    Size_Min=
        st.integers(),
    Descriptor=
        safe_text
)
ORDB4ORA_DatetimeType_strategy = st.builds(
    ORDB4ORA_DatetimeType,
    SecondPrecision_Max=
        st.integers(),
    DayPrecision_Max=
        st.integers(),
    SecondPrecision_Min=
        st.integers(),
    DayPrecision_Min=
        st.integers(),
    YearPrecision_Max=
        st.integers(),
    DayPrecision_Def=
        st.integers(),
    Descriptor=
        safe_text,
    YearPrecision_Def=
        st.integers(),
    YearPrecision_Min=
        st.integers(),
    SecondPrecision_Def=
        st.integers()
)
ORDB4ORA_LOBType_strategy = st.builds(
    ORDB4ORA_LOBType,
    Descriptor=
        safe_text
)
ORDB4ORA_BuiltInCharacterType_strategy = st.builds(
    ORDB4ORA_BuiltInCharacterType,
    Semantic=
        safe_text,
    Descriptor=
        safe_text,
    Size_Min=
        st.integers(),
    Size_Def=
        st.integers(),
    Size_Max=
        st.integers()
)
Datatype_strategy = st.builds(
    Datatype,
)
ORDB4ORA_ReferenceType_strategy = st.builds(
    ORDB4ORA_ReferenceType,
    Name=
        safe_text
)
ORDB4ORA_NestedTableType_strategy = st.builds(
    ORDB4ORA_NestedTableType,
    Name=
        safe_text
)
ORDB4ORA_Varray_strategy = st.builds(
    ORDB4ORA_Varray,
    NumElements=
        st.integers(),
    Name=
        safe_text
)
ORDB4ORA_BasicDataType_strategy = st.builds(
    ORDB4ORA_BasicDataType,
)
ORDB4ORA_StructuredType_strategy = st.builds(
    ORDB4ORA_StructuredType,
    is_final=
        st.booleans(),
    Name=
        safe_text,
    is_instantiable=
        st.booleans()
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
ORDB4ORA_Column_strategy = st.builds(
    ORDB4ORA_Column,
)
ORDB4ORA_Attribute_strategy = st.builds(
    ORDB4ORA_Attribute,
    Default=
        safe_text
)
SuppliedType_strategy = st.builds(
    SuppliedType,
)
ORDB4ORA_MediaType_strategy = st.builds(
    ORDB4ORA_MediaType,
    Descriptor=
        safe_text
)
ORDB4ORA_XMLType_strategy = st.builds(
    ORDB4ORA_XMLType,
    Descriptor=
        safe_text
)
ORDB4ORA_SpacialType_strategy = st.builds(
    ORDB4ORA_SpacialType,
    Descriptor=
        safe_text
)
ORDB4ORA_AnyType_strategy = st.builds(
    ORDB4ORA_AnyType,
    Descriptor=
        safe_text
)
BasicDataType_strategy = st.builds(
    BasicDataType,
)
ORDB4ORA_SuppliedType_strategy = st.builds(
    ORDB4ORA_SuppliedType,
)
ORDB4ORA_BuiltInType_strategy = st.builds(
    ORDB4ORA_BuiltInType,
)
ORDB4ORA_ANSIType_strategy = st.builds(
    ORDB4ORA_ANSIType,
)
ANSIType_strategy = st.builds(
    ANSIType,
)
ORDB4ORA_ANSICharacterType_strategy = st.builds(
    ORDB4ORA_ANSICharacterType,
    Descriptor=
        safe_text
)
ORDB4ORA_ANSINumberType_strategy = st.builds(
    ORDB4ORA_ANSINumberType,
    Descriptor=
        safe_text
)

@given(instance=DerivedTable_strategy)
@settings(max_examples=50)
def test_derivedtable_instantiation(instance):
    assert isinstance(instance, DerivedTable)

@given(instance=ORDB4ORA_View_strategy)
@settings(max_examples=50)
def test_ordb4ora_view_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_View)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=ORDB4ORA_DerivedTable_strategy)
@settings(max_examples=50)
def test_ordb4ora_derivedtable_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_DerivedTable)



@given(instance=ORDB4ORA_DerivedTable_strategy)
def test_ordb4ora_derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=ORDB4ORA_Trigger_strategy)
@settings(max_examples=50)
def test_ordb4ora_trigger_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Trigger)



@given(instance=ORDB4ORA_Trigger_strategy)
def test_ordb4ora_trigger_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original



@given(instance=ORDB4ORA_Trigger_strategy)
def test_ordb4ora_trigger_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=ORDB4ORA_Trigger_strategy)
def test_ordb4ora_trigger_Action_setter(instance):
    original = instance.Action
    instance.Action = original
    assert instance.Action == original



@given(instance=ORDB4ORA_Trigger_strategy)
def test_ordb4ora_trigger_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=ORDB4ORA_TypedTable_strategy)
@settings(max_examples=50)
def test_ordb4ora_typedtable_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_TypedTable)

@given(instance=ORDB4ORA_StoredNestedTable_strategy)
@settings(max_examples=50)
def test_ordb4ora_storednestedtable_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_StoredNestedTable)



@given(instance=ORDB4ORA_StoredNestedTable_strategy)
def test_ordb4ora_storednestedtable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Parameter_strategy)
@settings(max_examples=50)
def test_ordb4ora_parameter_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Parameter)



@given(instance=ORDB4ORA_Parameter_strategy)
def test_ordb4ora_parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_StructuralComponent_strategy)
@settings(max_examples=50)
def test_ordb4ora_structuralcomponent_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_StructuralComponent)



@given(instance=ORDB4ORA_StructuralComponent_strategy)
def test_ordb4ora_structuralcomponent_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Restriction_strategy)
@settings(max_examples=50)
def test_ordb4ora_restriction_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Restriction)

@given(instance=ORDB4ORA_Package_strategy)
@settings(max_examples=50)
def test_ordb4ora_package_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Package)



@given(instance=ORDB4ORA_Package_strategy)
def test_ordb4ora_package_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Operation_strategy)
@settings(max_examples=50)
def test_ordb4ora_operation_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Operation)



@given(instance=ORDB4ORA_Operation_strategy)
def test_ordb4ora_operation_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=ORDB4ORA_Operation_strategy)
def test_ordb4ora_operation_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=ORDB4ORA_Method_strategy)
@settings(max_examples=50)
def test_ordb4ora_method_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Method)



@given(instance=ORDB4ORA_Method_strategy)
def test_ordb4ora_method_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original



@given(instance=ORDB4ORA_Method_strategy)
def test_ordb4ora_method_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=ORDB4ORA_Procedure_strategy)
@settings(max_examples=50)
def test_ordb4ora_procedure_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Procedure)

@given(instance=ORDB4ORA_Function_strategy)
@settings(max_examples=50)
def test_ordb4ora_function_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Function)

@given(instance=ORDB4ORA_Feature_strategy)
@settings(max_examples=50)
def test_ordb4ora_feature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Feature)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=ORDB4ORA_OperationParameter_strategy)
@settings(max_examples=50)
def test_ordb4ora_operationparameter_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_OperationParameter)



@given(instance=ORDB4ORA_OperationParameter_strategy)
def test_ordb4ora_operationparameter_Mode_setter(instance):
    original = instance.Mode
    instance.Mode = original
    assert instance.Mode == original

@given(instance=ORDB4ORA_MethodParameter_strategy)
@settings(max_examples=50)
def test_ordb4ora_methodparameter_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_MethodParameter)

@given(instance=ORDB4ORA_Model_strategy)
@settings(max_examples=50)
def test_ordb4ora_model_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Model)



@given(instance=ORDB4ORA_Model_strategy)
def test_ordb4ora_model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Datatype_strategy)
@settings(max_examples=50)
def test_ordb4ora_datatype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Datatype)

@given(instance=ORDB4ORA_Table_strategy)
@settings(max_examples=50)
def test_ordb4ora_table_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Table)



@given(instance=ORDB4ORA_Table_strategy)
def test_ordb4ora_table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=ORDB4ORA_ForeignKey_strategy)
@settings(max_examples=50)
def test_ordb4ora_foreignkey_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_ForeignKey)



@given(instance=ORDB4ORA_ForeignKey_strategy)
def test_ordb4ora_foreignkey_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=ORDB4ORA_ForeignKey_strategy)
def test_ordb4ora_foreignkey_OnDelete_setter(instance):
    original = instance.OnDelete
    instance.OnDelete = original
    assert instance.OnDelete == original

@given(instance=ORDB4ORA_NotNull_strategy)
@settings(max_examples=50)
def test_ordb4ora_notnull_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_NotNull)



@given(instance=ORDB4ORA_NotNull_strategy)
def test_ordb4ora_notnull_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_PrimaryKey_strategy)
@settings(max_examples=50)
def test_ordb4ora_primarykey_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_PrimaryKey)



@given(instance=ORDB4ORA_PrimaryKey_strategy)
def test_ordb4ora_primarykey_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Unique_strategy)
@settings(max_examples=50)
def test_ordb4ora_unique_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Unique)



@given(instance=ORDB4ORA_Unique_strategy)
def test_ordb4ora_unique_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Check_strategy)
@settings(max_examples=50)
def test_ordb4ora_check_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Check)



@given(instance=ORDB4ORA_Check_strategy)
def test_ordb4ora_check_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=ORDB4ORA_Check_strategy)
def test_ordb4ora_check_Condition_setter(instance):
    original = instance.Condition
    instance.Condition = original
    assert instance.Condition == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ORDB4ORA_NumberFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora_numberfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_NumberFeature)



@given(instance=ORDB4ORA_NumberFeature_strategy)
def test_ordb4ora_numberfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ORDB4ORA_NumberFeature_strategy)
def test_ordb4ora_numberfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA_RowFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora_rowfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_RowFeature)



@given(instance=ORDB4ORA_RowFeature_strategy)
def test_ordb4ora_rowfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ORDB4ORA_RowFeature_strategy)
def test_ordb4ora_rowfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA_DatetimeFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora_datetimefeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_DatetimeFeature)



@given(instance=ORDB4ORA_DatetimeFeature_strategy)
def test_ordb4ora_datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ORDB4ORA_DatetimeFeature_strategy)
def test_ordb4ora_datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA_RawFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora_rawfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_RawFeature)



@given(instance=ORDB4ORA_RawFeature_strategy)
def test_ordb4ora_rawfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=ORDB4ORA_RawFeature_strategy)
def test_ordb4ora_rawfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA_IntervalFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora_intervalfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_IntervalFeature)



@given(instance=ORDB4ORA_IntervalFeature_strategy)
def test_ordb4ora_intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=ORDB4ORA_IntervalFeature_strategy)
def test_ordb4ora_intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA_CharacterFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora_characterfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_CharacterFeature)



@given(instance=ORDB4ORA_CharacterFeature_strategy)
def test_ordb4ora_characterfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ORDB4ORA_CharacterFeature_strategy)
def test_ordb4ora_characterfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=ORDB4ORA_BuiltInNumberType_strategy)
@settings(max_examples=50)
def test_ordb4ora_builtinnumbertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_BuiltInNumberType)



@given(instance=ORDB4ORA_BuiltInNumberType_strategy)
def test_ordb4ora_builtinnumbertype_Precision_Mn_setter(instance):
    original = instance.Precision_Mn
    instance.Precision_Mn = original
    assert instance.Precision_Mn == original



@given(instance=ORDB4ORA_BuiltInNumberType_strategy)
def test_ordb4ora_builtinnumbertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original



@given(instance=ORDB4ORA_BuiltInNumberType_strategy)
def test_ordb4ora_builtinnumbertype_Precision_Max_setter(instance):
    original = instance.Precision_Max
    instance.Precision_Max = original
    assert instance.Precision_Max == original



@given(instance=ORDB4ORA_BuiltInNumberType_strategy)
def test_ordb4ora_builtinnumbertype_Scale_Min_setter(instance):
    original = instance.Scale_Min
    instance.Scale_Min = original
    assert instance.Scale_Min == original



@given(instance=ORDB4ORA_BuiltInNumberType_strategy)
def test_ordb4ora_builtinnumbertype_Scale_Max_setter(instance):
    original = instance.Scale_Max
    instance.Scale_Max = original
    assert instance.Scale_Max == original

@given(instance=ORDB4ORA_LongAndRawType_strategy)
@settings(max_examples=50)
def test_ordb4ora_longandrawtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_LongAndRawType)



@given(instance=ORDB4ORA_LongAndRawType_strategy)
def test_ordb4ora_longandrawtype_Size_Max_setter(instance):
    original = instance.Size_Max
    instance.Size_Max = original
    assert instance.Size_Max == original



@given(instance=ORDB4ORA_LongAndRawType_strategy)
def test_ordb4ora_longandrawtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original



@given(instance=ORDB4ORA_LongAndRawType_strategy)
def test_ordb4ora_longandrawtype_Size_Min_setter(instance):
    original = instance.Size_Min
    instance.Size_Min = original
    assert instance.Size_Min == original

@given(instance=ORDB4ORA_ROWIDType_strategy)
@settings(max_examples=50)
def test_ordb4ora_rowidtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_ROWIDType)



@given(instance=ORDB4ORA_ROWIDType_strategy)
def test_ordb4ora_rowidtype_Size_Max_setter(instance):
    original = instance.Size_Max
    instance.Size_Max = original
    assert instance.Size_Max == original



@given(instance=ORDB4ORA_ROWIDType_strategy)
def test_ordb4ora_rowidtype_Size_Min_setter(instance):
    original = instance.Size_Min
    instance.Size_Min = original
    assert instance.Size_Min == original



@given(instance=ORDB4ORA_ROWIDType_strategy)
def test_ordb4ora_rowidtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA_DatetimeType_strategy)
@settings(max_examples=50)
def test_ordb4ora_datetimetype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_DatetimeType)



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_SecondPrecision_Max_setter(instance):
    original = instance.SecondPrecision_Max
    instance.SecondPrecision_Max = original
    assert instance.SecondPrecision_Max == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_DayPrecision_Max_setter(instance):
    original = instance.DayPrecision_Max
    instance.DayPrecision_Max = original
    assert instance.DayPrecision_Max == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_SecondPrecision_Min_setter(instance):
    original = instance.SecondPrecision_Min
    instance.SecondPrecision_Min = original
    assert instance.SecondPrecision_Min == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_DayPrecision_Min_setter(instance):
    original = instance.DayPrecision_Min
    instance.DayPrecision_Min = original
    assert instance.DayPrecision_Min == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_YearPrecision_Max_setter(instance):
    original = instance.YearPrecision_Max
    instance.YearPrecision_Max = original
    assert instance.YearPrecision_Max == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_DayPrecision_Def_setter(instance):
    original = instance.DayPrecision_Def
    instance.DayPrecision_Def = original
    assert instance.DayPrecision_Def == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_YearPrecision_Def_setter(instance):
    original = instance.YearPrecision_Def
    instance.YearPrecision_Def = original
    assert instance.YearPrecision_Def == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_YearPrecision_Min_setter(instance):
    original = instance.YearPrecision_Min
    instance.YearPrecision_Min = original
    assert instance.YearPrecision_Min == original



@given(instance=ORDB4ORA_DatetimeType_strategy)
def test_ordb4ora_datetimetype_SecondPrecision_Def_setter(instance):
    original = instance.SecondPrecision_Def
    instance.SecondPrecision_Def = original
    assert instance.SecondPrecision_Def == original

@given(instance=ORDB4ORA_LOBType_strategy)
@settings(max_examples=50)
def test_ordb4ora_lobtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_LOBType)



@given(instance=ORDB4ORA_LOBType_strategy)
def test_ordb4ora_lobtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA_BuiltInCharacterType_strategy)
@settings(max_examples=50)
def test_ordb4ora_builtincharactertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_BuiltInCharacterType)



@given(instance=ORDB4ORA_BuiltInCharacterType_strategy)
def test_ordb4ora_builtincharactertype_Semantic_setter(instance):
    original = instance.Semantic
    instance.Semantic = original
    assert instance.Semantic == original



@given(instance=ORDB4ORA_BuiltInCharacterType_strategy)
def test_ordb4ora_builtincharactertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original



@given(instance=ORDB4ORA_BuiltInCharacterType_strategy)
def test_ordb4ora_builtincharactertype_Size_Min_setter(instance):
    original = instance.Size_Min
    instance.Size_Min = original
    assert instance.Size_Min == original



@given(instance=ORDB4ORA_BuiltInCharacterType_strategy)
def test_ordb4ora_builtincharactertype_Size_Def_setter(instance):
    original = instance.Size_Def
    instance.Size_Def = original
    assert instance.Size_Def == original



@given(instance=ORDB4ORA_BuiltInCharacterType_strategy)
def test_ordb4ora_builtincharactertype_Size_Max_setter(instance):
    original = instance.Size_Max
    instance.Size_Max = original
    assert instance.Size_Max == original

@given(instance=Datatype_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, Datatype)

@given(instance=ORDB4ORA_ReferenceType_strategy)
@settings(max_examples=50)
def test_ordb4ora_referencetype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_ReferenceType)



@given(instance=ORDB4ORA_ReferenceType_strategy)
def test_ordb4ora_referencetype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_NestedTableType_strategy)
@settings(max_examples=50)
def test_ordb4ora_nestedtabletype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_NestedTableType)



@given(instance=ORDB4ORA_NestedTableType_strategy)
def test_ordb4ora_nestedtabletype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_Varray_strategy)
@settings(max_examples=50)
def test_ordb4ora_varray_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Varray)



@given(instance=ORDB4ORA_Varray_strategy)
def test_ordb4ora_varray_NumElements_setter(instance):
    original = instance.NumElements
    instance.NumElements = original
    assert instance.NumElements == original



@given(instance=ORDB4ORA_Varray_strategy)
def test_ordb4ora_varray_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA_BasicDataType_strategy)
@settings(max_examples=50)
def test_ordb4ora_basicdatatype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_BasicDataType)

@given(instance=ORDB4ORA_StructuredType_strategy)
@settings(max_examples=50)
def test_ordb4ora_structuredtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_StructuredType)



@given(instance=ORDB4ORA_StructuredType_strategy)
def test_ordb4ora_structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original



@given(instance=ORDB4ORA_StructuredType_strategy)
def test_ordb4ora_structuredtype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=ORDB4ORA_StructuredType_strategy)
def test_ordb4ora_structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=ORDB4ORA_Column_strategy)
@settings(max_examples=50)
def test_ordb4ora_column_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Column)

@given(instance=ORDB4ORA_Attribute_strategy)
@settings(max_examples=50)
def test_ordb4ora_attribute_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_Attribute)



@given(instance=ORDB4ORA_Attribute_strategy)
def test_ordb4ora_attribute_Default_setter(instance):
    original = instance.Default
    instance.Default = original
    assert instance.Default == original

@given(instance=SuppliedType_strategy)
@settings(max_examples=50)
def test_suppliedtype_instantiation(instance):
    assert isinstance(instance, SuppliedType)

@given(instance=ORDB4ORA_MediaType_strategy)
@settings(max_examples=50)
def test_ordb4ora_mediatype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_MediaType)



@given(instance=ORDB4ORA_MediaType_strategy)
def test_ordb4ora_mediatype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA_XMLType_strategy)
@settings(max_examples=50)
def test_ordb4ora_xmltype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_XMLType)



@given(instance=ORDB4ORA_XMLType_strategy)
def test_ordb4ora_xmltype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA_SpacialType_strategy)
@settings(max_examples=50)
def test_ordb4ora_spacialtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_SpacialType)



@given(instance=ORDB4ORA_SpacialType_strategy)
def test_ordb4ora_spacialtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA_AnyType_strategy)
@settings(max_examples=50)
def test_ordb4ora_anytype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_AnyType)



@given(instance=ORDB4ORA_AnyType_strategy)
def test_ordb4ora_anytype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=BasicDataType_strategy)
@settings(max_examples=50)
def test_basicdatatype_instantiation(instance):
    assert isinstance(instance, BasicDataType)

@given(instance=ORDB4ORA_SuppliedType_strategy)
@settings(max_examples=50)
def test_ordb4ora_suppliedtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_SuppliedType)

@given(instance=ORDB4ORA_BuiltInType_strategy)
@settings(max_examples=50)
def test_ordb4ora_builtintype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_BuiltInType)

@given(instance=ORDB4ORA_ANSIType_strategy)
@settings(max_examples=50)
def test_ordb4ora_ansitype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_ANSIType)

@given(instance=ANSIType_strategy)
@settings(max_examples=50)
def test_ansitype_instantiation(instance):
    assert isinstance(instance, ANSIType)

@given(instance=ORDB4ORA_ANSICharacterType_strategy)
@settings(max_examples=50)
def test_ordb4ora_ansicharactertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_ANSICharacterType)



@given(instance=ORDB4ORA_ANSICharacterType_strategy)
def test_ordb4ora_ansicharactertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA_ANSINumberType_strategy)
@settings(max_examples=50)
def test_ordb4ora_ansinumbertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA_ANSINumberType)



@given(instance=ORDB4ORA_ANSINumberType_strategy)
def test_ordb4ora_ansinumbertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original
