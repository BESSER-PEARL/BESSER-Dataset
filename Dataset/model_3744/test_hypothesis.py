import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DerivedTable,
    Table,
    ORDB4ORA::View,
    ORDB4ORA::Trigger,
    ORDB4ORA::DerivedTable,
    ORDB4ORA::StructuralComponent,
    ORDB4ORA::Restriction,
    ORDB4ORA::TypedTable,
    ORDB4ORA::StoredNestedTable,
    Parameter,
    ORDB4ORA::OperationParameter,
    ORDB4ORA::MethodParameter,
    ORDB4ORA::Parameter,
    Operation,
    ORDB4ORA::Procedure,
    ORDB4ORA::Function,
    ORDB4ORA::Feature,
    ORDB4ORA::Method,
    BuiltInType,
    ORDB4ORA::LOBType,
    ORDB4ORA::DatetimeType,
    ORDB4ORA::ROWIDType,
    ORDB4ORA::LongAndRawType,
    ORDB4ORA::BuiltInNumberType,
    ORDB4ORA::BuiltInCharacterType,
    Restriction,
    ORDB4ORA::NotNull,
    ORDB4ORA::Unique,
    ORDB4ORA::PrimaryKey,
    ORDB4ORA::ForeignKey,
    ORDB4ORA::Check,
    Feature,
    ORDB4ORA::NumberFeature,
    ORDB4ORA::RowFeature,
    ORDB4ORA::IntervalFeature,
    ORDB4ORA::RawFeature,
    ORDB4ORA::DatetimeFeature,
    ORDB4ORA::CharacterFeature,
    ANSIType,
    ORDB4ORA::ANSICharacterType,
    ORDB4ORA::Package,
    ORDB4ORA::Operation,
    ORDB4ORA::Table,
    ORDB4ORA::Datatype,
    ORDB4ORA::Model,
    Datatype,
    ORDB4ORA::Varray,
    ORDB4ORA::NestedTableType,
    ORDB4ORA::ReferenceType,
    ORDB4ORA::BasicDataType,
    ORDB4ORA::StructuredType,
    StructuralComponent,
    ORDB4ORA::Column,
    ORDB4ORA::Attribute,
    SuppliedType,
    ORDB4ORA::MediaType,
    ORDB4ORA::XMLType,
    ORDB4ORA::SpacialType,
    ORDB4ORA::AnyType,
    BasicDataType,
    ORDB4ORA::BuiltInType,
    ORDB4ORA::SuppliedType,
    ORDB4ORA::ANSIType,
    ORDB4ORA::ANSINumberType,
    BuiltInROWIDType,
    BuiltInDatetimeTypes,
    ONDELETEActions,
    BuiltInCharacterTypes,
    SuppliedMediaTypes,
    SuppliedXMLTypes,
    NumberFeatures,
    ANSICharacterTypes,
    IntervalFeatures,
    DatetimeFeatures,
    BuiltInLOBType,
    CharacterFeatures,
    ANSINumberTypes,
    ParameterMode,
    BuiltInCharacterSemantics,
    RowFeatures,
    BuiltInLongAndRawTypes,
    RawFeatures,
    BuiltNumberTypes,
    TriggerEvent,
    SuppliedAnyTypes,
    SuppliedSpacialTypes,
    TriggerActionTime,
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



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::view_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::View)


def test_ordb4ora::view_constructor_exists():
    assert callable(ORDB4ORA::View.__init__)


def test_ordb4ora::view_constructor_args():
    sig = inspect.signature(ORDB4ORA::View.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::trigger_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Trigger)


def test_ordb4ora::trigger_constructor_exists():
    assert callable(ORDB4ORA::Trigger.__init__)


def test_ordb4ora::trigger_constructor_args():
    sig = inspect.signature(ORDB4ORA::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "Event" in params, "Missing parameter 'Event'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Action" in params, "Missing parameter 'Action'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_ordb4ora::trigger_has_Event():
    assert hasattr(ORDB4ORA::Trigger, "Event")
    descriptor = None
    for klass in ORDB4ORA::Trigger.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::trigger_has_Name():
    assert hasattr(ORDB4ORA::Trigger, "Name")
    descriptor = None
    for klass in ORDB4ORA::Trigger.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::trigger_has_Action():
    assert hasattr(ORDB4ORA::Trigger, "Action")
    descriptor = None
    for klass in ORDB4ORA::Trigger.__mro__:
        if "Action" in klass.__dict__:
            descriptor = klass.__dict__["Action"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::trigger_has_Body():
    assert hasattr(ORDB4ORA::Trigger, "Body")
    descriptor = None
    for klass in ORDB4ORA::Trigger.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::derivedtable_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::DerivedTable)


def test_ordb4ora::derivedtable_constructor_exists():
    assert callable(ORDB4ORA::DerivedTable.__init__)


def test_ordb4ora::derivedtable_constructor_args():
    sig = inspect.signature(ORDB4ORA::DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_ordb4ora::derivedtable_has_query_expression():
    assert hasattr(ORDB4ORA::DerivedTable, "query_expression")
    descriptor = None
    for klass in ORDB4ORA::DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::StructuralComponent)


def test_ordb4ora::structuralcomponent_constructor_exists():
    assert callable(ORDB4ORA::StructuralComponent.__init__)


def test_ordb4ora::structuralcomponent_constructor_args():
    sig = inspect.signature(ORDB4ORA::StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::structuralcomponent_has_Name():
    assert hasattr(ORDB4ORA::StructuralComponent, "Name")
    descriptor = None
    for klass in ORDB4ORA::StructuralComponent.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::restriction_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Restriction)


def test_ordb4ora::restriction_constructor_exists():
    assert callable(ORDB4ORA::Restriction.__init__)


def test_ordb4ora::restriction_constructor_args():
    sig = inspect.signature(ORDB4ORA::Restriction.__init__)
    params = list(sig.parameters.keys())
    assert "NameColumns" in params, "Missing parameter 'NameColumns'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::restriction_has_NameColumns():
    assert hasattr(ORDB4ORA::Restriction, "NameColumns")
    descriptor = None
    for klass in ORDB4ORA::Restriction.__mro__:
        if "NameColumns" in klass.__dict__:
            descriptor = klass.__dict__["NameColumns"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::restriction_has_Name():
    assert hasattr(ORDB4ORA::Restriction, "Name")
    descriptor = None
    for klass in ORDB4ORA::Restriction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::typedtable_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::TypedTable)


def test_ordb4ora::typedtable_constructor_exists():
    assert callable(ORDB4ORA::TypedTable.__init__)


def test_ordb4ora::typedtable_constructor_args():
    sig = inspect.signature(ORDB4ORA::TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::storednestedtable_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::StoredNestedTable)


def test_ordb4ora::storednestedtable_constructor_exists():
    assert callable(ORDB4ORA::StoredNestedTable.__init__)


def test_ordb4ora::storednestedtable_constructor_args():
    sig = inspect.signature(ORDB4ORA::StoredNestedTable.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::storednestedtable_has_Name():
    assert hasattr(ORDB4ORA::StoredNestedTable, "Name")
    descriptor = None
    for klass in ORDB4ORA::StoredNestedTable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::operationparameter_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::OperationParameter)


def test_ordb4ora::operationparameter_constructor_exists():
    assert callable(ORDB4ORA::OperationParameter.__init__)


def test_ordb4ora::operationparameter_constructor_args():
    sig = inspect.signature(ORDB4ORA::OperationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "Mode" in params, "Missing parameter 'Mode'"

def test_ordb4ora::operationparameter_has_Mode():
    assert hasattr(ORDB4ORA::OperationParameter, "Mode")
    descriptor = None
    for klass in ORDB4ORA::OperationParameter.__mro__:
        if "Mode" in klass.__dict__:
            descriptor = klass.__dict__["Mode"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::methodparameter_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::MethodParameter)


def test_ordb4ora::methodparameter_constructor_exists():
    assert callable(ORDB4ORA::MethodParameter.__init__)


def test_ordb4ora::methodparameter_constructor_args():
    sig = inspect.signature(ORDB4ORA::MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::parameter_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Parameter)


def test_ordb4ora::parameter_constructor_exists():
    assert callable(ORDB4ORA::Parameter.__init__)


def test_ordb4ora::parameter_constructor_args():
    sig = inspect.signature(ORDB4ORA::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::parameter_has_Name():
    assert hasattr(ORDB4ORA::Parameter, "Name")
    descriptor = None
    for klass in ORDB4ORA::Parameter.__mro__:
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



def test_ordb4ora::procedure_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Procedure)


def test_ordb4ora::procedure_constructor_exists():
    assert callable(ORDB4ORA::Procedure.__init__)


def test_ordb4ora::procedure_constructor_args():
    sig = inspect.signature(ORDB4ORA::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::function_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Function)


def test_ordb4ora::function_constructor_exists():
    assert callable(ORDB4ORA::Function.__init__)


def test_ordb4ora::function_constructor_args():
    sig = inspect.signature(ORDB4ORA::Function.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::feature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Feature)


def test_ordb4ora::feature_constructor_exists():
    assert callable(ORDB4ORA::Feature.__init__)


def test_ordb4ora::feature_constructor_args():
    sig = inspect.signature(ORDB4ORA::Feature.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::method_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Method)


def test_ordb4ora::method_constructor_exists():
    assert callable(ORDB4ORA::Method.__init__)


def test_ordb4ora::method_constructor_args():
    sig = inspect.signature(ORDB4ORA::Method.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::method_has_Body():
    assert hasattr(ORDB4ORA::Method, "Body")
    descriptor = None
    for klass in ORDB4ORA::Method.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::method_has_Name():
    assert hasattr(ORDB4ORA::Method, "Name")
    descriptor = None
    for klass in ORDB4ORA::Method.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::lobtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::LOBType)


def test_ordb4ora::lobtype_constructor_exists():
    assert callable(ORDB4ORA::LOBType.__init__)


def test_ordb4ora::lobtype_constructor_args():
    sig = inspect.signature(ORDB4ORA::LOBType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::lobtype_has_Descriptor():
    assert hasattr(ORDB4ORA::LOBType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::LOBType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::datetimetype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::DatetimeType)


def test_ordb4ora::datetimetype_constructor_exists():
    assert callable(ORDB4ORA::DatetimeType.__init__)


def test_ordb4ora::datetimetype_constructor_args():
    sig = inspect.signature(ORDB4ORA::DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "YearPrecision_Min" in params, "Missing parameter 'YearPrecision_Min'"
    assert "SecondPrecision_Def" in params, "Missing parameter 'SecondPrecision_Def'"
    assert "SecondPrecision_Max" in params, "Missing parameter 'SecondPrecision_Max'"
    assert "YearPrecision_Def" in params, "Missing parameter 'YearPrecision_Def'"
    assert "DayPrecision_Max" in params, "Missing parameter 'DayPrecision_Max'"
    assert "YearPrecision_Max" in params, "Missing parameter 'YearPrecision_Max'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "DayPrecision_Def" in params, "Missing parameter 'DayPrecision_Def'"
    assert "DayPrecision_Min" in params, "Missing parameter 'DayPrecision_Min'"
    assert "SecondPrecision_Min" in params, "Missing parameter 'SecondPrecision_Min'"

def test_ordb4ora::datetimetype_has_YearPrecision_Min():
    assert hasattr(ORDB4ORA::DatetimeType, "YearPrecision_Min")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "YearPrecision_Min" in klass.__dict__:
            descriptor = klass.__dict__["YearPrecision_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_SecondPrecision_Def():
    assert hasattr(ORDB4ORA::DatetimeType, "SecondPrecision_Def")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "SecondPrecision_Def" in klass.__dict__:
            descriptor = klass.__dict__["SecondPrecision_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_SecondPrecision_Max():
    assert hasattr(ORDB4ORA::DatetimeType, "SecondPrecision_Max")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "SecondPrecision_Max" in klass.__dict__:
            descriptor = klass.__dict__["SecondPrecision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_YearPrecision_Def():
    assert hasattr(ORDB4ORA::DatetimeType, "YearPrecision_Def")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "YearPrecision_Def" in klass.__dict__:
            descriptor = klass.__dict__["YearPrecision_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_DayPrecision_Max():
    assert hasattr(ORDB4ORA::DatetimeType, "DayPrecision_Max")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "DayPrecision_Max" in klass.__dict__:
            descriptor = klass.__dict__["DayPrecision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_YearPrecision_Max():
    assert hasattr(ORDB4ORA::DatetimeType, "YearPrecision_Max")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "YearPrecision_Max" in klass.__dict__:
            descriptor = klass.__dict__["YearPrecision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_Descriptor():
    assert hasattr(ORDB4ORA::DatetimeType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_DayPrecision_Def():
    assert hasattr(ORDB4ORA::DatetimeType, "DayPrecision_Def")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "DayPrecision_Def" in klass.__dict__:
            descriptor = klass.__dict__["DayPrecision_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_DayPrecision_Min():
    assert hasattr(ORDB4ORA::DatetimeType, "DayPrecision_Min")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "DayPrecision_Min" in klass.__dict__:
            descriptor = klass.__dict__["DayPrecision_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimetype_has_SecondPrecision_Min():
    assert hasattr(ORDB4ORA::DatetimeType, "SecondPrecision_Min")
    descriptor = None
    for klass in ORDB4ORA::DatetimeType.__mro__:
        if "SecondPrecision_Min" in klass.__dict__:
            descriptor = klass.__dict__["SecondPrecision_Min"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::rowidtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::ROWIDType)


def test_ordb4ora::rowidtype_constructor_exists():
    assert callable(ORDB4ORA::ROWIDType.__init__)


def test_ordb4ora::rowidtype_constructor_args():
    sig = inspect.signature(ORDB4ORA::ROWIDType.__init__)
    params = list(sig.parameters.keys())
    assert "Size_Min" in params, "Missing parameter 'Size_Min'"
    assert "Size_Max" in params, "Missing parameter 'Size_Max'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::rowidtype_has_Size_Min():
    assert hasattr(ORDB4ORA::ROWIDType, "Size_Min")
    descriptor = None
    for klass in ORDB4ORA::ROWIDType.__mro__:
        if "Size_Min" in klass.__dict__:
            descriptor = klass.__dict__["Size_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::rowidtype_has_Size_Max():
    assert hasattr(ORDB4ORA::ROWIDType, "Size_Max")
    descriptor = None
    for klass in ORDB4ORA::ROWIDType.__mro__:
        if "Size_Max" in klass.__dict__:
            descriptor = klass.__dict__["Size_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::rowidtype_has_Descriptor():
    assert hasattr(ORDB4ORA::ROWIDType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::ROWIDType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::longandrawtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::LongAndRawType)


def test_ordb4ora::longandrawtype_constructor_exists():
    assert callable(ORDB4ORA::LongAndRawType.__init__)


def test_ordb4ora::longandrawtype_constructor_args():
    sig = inspect.signature(ORDB4ORA::LongAndRawType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "Size_Min" in params, "Missing parameter 'Size_Min'"
    assert "Size_Max" in params, "Missing parameter 'Size_Max'"

def test_ordb4ora::longandrawtype_has_Descriptor():
    assert hasattr(ORDB4ORA::LongAndRawType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::LongAndRawType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::longandrawtype_has_Size_Min():
    assert hasattr(ORDB4ORA::LongAndRawType, "Size_Min")
    descriptor = None
    for klass in ORDB4ORA::LongAndRawType.__mro__:
        if "Size_Min" in klass.__dict__:
            descriptor = klass.__dict__["Size_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::longandrawtype_has_Size_Max():
    assert hasattr(ORDB4ORA::LongAndRawType, "Size_Max")
    descriptor = None
    for klass in ORDB4ORA::LongAndRawType.__mro__:
        if "Size_Max" in klass.__dict__:
            descriptor = klass.__dict__["Size_Max"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::builtinnumbertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::BuiltInNumberType)


def test_ordb4ora::builtinnumbertype_constructor_exists():
    assert callable(ORDB4ORA::BuiltInNumberType.__init__)


def test_ordb4ora::builtinnumbertype_constructor_args():
    sig = inspect.signature(ORDB4ORA::BuiltInNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "Scale_Min" in params, "Missing parameter 'Scale_Min'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"
    assert "Precision_Max" in params, "Missing parameter 'Precision_Max'"
    assert "Precision_Mn" in params, "Missing parameter 'Precision_Mn'"
    assert "Scale_Max" in params, "Missing parameter 'Scale_Max'"

def test_ordb4ora::builtinnumbertype_has_Scale_Min():
    assert hasattr(ORDB4ORA::BuiltInNumberType, "Scale_Min")
    descriptor = None
    for klass in ORDB4ORA::BuiltInNumberType.__mro__:
        if "Scale_Min" in klass.__dict__:
            descriptor = klass.__dict__["Scale_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtinnumbertype_has_Descriptor():
    assert hasattr(ORDB4ORA::BuiltInNumberType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::BuiltInNumberType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtinnumbertype_has_Precision_Max():
    assert hasattr(ORDB4ORA::BuiltInNumberType, "Precision_Max")
    descriptor = None
    for klass in ORDB4ORA::BuiltInNumberType.__mro__:
        if "Precision_Max" in klass.__dict__:
            descriptor = klass.__dict__["Precision_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtinnumbertype_has_Precision_Mn():
    assert hasattr(ORDB4ORA::BuiltInNumberType, "Precision_Mn")
    descriptor = None
    for klass in ORDB4ORA::BuiltInNumberType.__mro__:
        if "Precision_Mn" in klass.__dict__:
            descriptor = klass.__dict__["Precision_Mn"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtinnumbertype_has_Scale_Max():
    assert hasattr(ORDB4ORA::BuiltInNumberType, "Scale_Max")
    descriptor = None
    for klass in ORDB4ORA::BuiltInNumberType.__mro__:
        if "Scale_Max" in klass.__dict__:
            descriptor = klass.__dict__["Scale_Max"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::builtincharactertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::BuiltInCharacterType)


def test_ordb4ora::builtincharactertype_constructor_exists():
    assert callable(ORDB4ORA::BuiltInCharacterType.__init__)


def test_ordb4ora::builtincharactertype_constructor_args():
    sig = inspect.signature(ORDB4ORA::BuiltInCharacterType.__init__)
    params = list(sig.parameters.keys())
    assert "Size_Def" in params, "Missing parameter 'Size_Def'"
    assert "Semantic" in params, "Missing parameter 'Semantic'"
    assert "Size_Min" in params, "Missing parameter 'Size_Min'"
    assert "Size_Max" in params, "Missing parameter 'Size_Max'"
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::builtincharactertype_has_Size_Def():
    assert hasattr(ORDB4ORA::BuiltInCharacterType, "Size_Def")
    descriptor = None
    for klass in ORDB4ORA::BuiltInCharacterType.__mro__:
        if "Size_Def" in klass.__dict__:
            descriptor = klass.__dict__["Size_Def"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtincharactertype_has_Semantic():
    assert hasattr(ORDB4ORA::BuiltInCharacterType, "Semantic")
    descriptor = None
    for klass in ORDB4ORA::BuiltInCharacterType.__mro__:
        if "Semantic" in klass.__dict__:
            descriptor = klass.__dict__["Semantic"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtincharactertype_has_Size_Min():
    assert hasattr(ORDB4ORA::BuiltInCharacterType, "Size_Min")
    descriptor = None
    for klass in ORDB4ORA::BuiltInCharacterType.__mro__:
        if "Size_Min" in klass.__dict__:
            descriptor = klass.__dict__["Size_Min"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtincharactertype_has_Size_Max():
    assert hasattr(ORDB4ORA::BuiltInCharacterType, "Size_Max")
    descriptor = None
    for klass in ORDB4ORA::BuiltInCharacterType.__mro__:
        if "Size_Max" in klass.__dict__:
            descriptor = klass.__dict__["Size_Max"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::builtincharactertype_has_Descriptor():
    assert hasattr(ORDB4ORA::BuiltInCharacterType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::BuiltInCharacterType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_restriction_is_not_abstract():
    assert not inspect.isabstract(Restriction)


def test_restriction_constructor_exists():
    assert callable(Restriction.__init__)


def test_restriction_constructor_args():
    sig = inspect.signature(Restriction.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::notnull_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::NotNull)


def test_ordb4ora::notnull_constructor_exists():
    assert callable(ORDB4ORA::NotNull.__init__)


def test_ordb4ora::notnull_constructor_args():
    sig = inspect.signature(ORDB4ORA::NotNull.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::unique_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Unique)


def test_ordb4ora::unique_constructor_exists():
    assert callable(ORDB4ORA::Unique.__init__)


def test_ordb4ora::unique_constructor_args():
    sig = inspect.signature(ORDB4ORA::Unique.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::primarykey_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::PrimaryKey)


def test_ordb4ora::primarykey_constructor_exists():
    assert callable(ORDB4ORA::PrimaryKey.__init__)


def test_ordb4ora::primarykey_constructor_args():
    sig = inspect.signature(ORDB4ORA::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::foreignkey_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::ForeignKey)


def test_ordb4ora::foreignkey_constructor_exists():
    assert callable(ORDB4ORA::ForeignKey.__init__)


def test_ordb4ora::foreignkey_constructor_args():
    sig = inspect.signature(ORDB4ORA::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "OnDelete" in params, "Missing parameter 'OnDelete'"

def test_ordb4ora::foreignkey_has_OnDelete():
    assert hasattr(ORDB4ORA::ForeignKey, "OnDelete")
    descriptor = None
    for klass in ORDB4ORA::ForeignKey.__mro__:
        if "OnDelete" in klass.__dict__:
            descriptor = klass.__dict__["OnDelete"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::check_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Check)


def test_ordb4ora::check_constructor_exists():
    assert callable(ORDB4ORA::Check.__init__)


def test_ordb4ora::check_constructor_args():
    sig = inspect.signature(ORDB4ORA::Check.__init__)
    params = list(sig.parameters.keys())
    assert "Condition" in params, "Missing parameter 'Condition'"

def test_ordb4ora::check_has_Condition():
    assert hasattr(ORDB4ORA::Check, "Condition")
    descriptor = None
    for klass in ORDB4ORA::Check.__mro__:
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



def test_ordb4ora::numberfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::NumberFeature)


def test_ordb4ora::numberfeature_constructor_exists():
    assert callable(ORDB4ORA::NumberFeature.__init__)


def test_ordb4ora::numberfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA::NumberFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora::numberfeature_has_value():
    assert hasattr(ORDB4ORA::NumberFeature, "value")
    descriptor = None
    for klass in ORDB4ORA::NumberFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::numberfeature_has_key():
    assert hasattr(ORDB4ORA::NumberFeature, "key")
    descriptor = None
    for klass in ORDB4ORA::NumberFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::rowfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::RowFeature)


def test_ordb4ora::rowfeature_constructor_exists():
    assert callable(ORDB4ORA::RowFeature.__init__)


def test_ordb4ora::rowfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA::RowFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_ordb4ora::rowfeature_has_key():
    assert hasattr(ORDB4ORA::RowFeature, "key")
    descriptor = None
    for klass in ORDB4ORA::RowFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::rowfeature_has_value():
    assert hasattr(ORDB4ORA::RowFeature, "value")
    descriptor = None
    for klass in ORDB4ORA::RowFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::intervalfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::IntervalFeature)


def test_ordb4ora::intervalfeature_constructor_exists():
    assert callable(ORDB4ORA::IntervalFeature.__init__)


def test_ordb4ora::intervalfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA::IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora::intervalfeature_has_value():
    assert hasattr(ORDB4ORA::IntervalFeature, "value")
    descriptor = None
    for klass in ORDB4ORA::IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::intervalfeature_has_key():
    assert hasattr(ORDB4ORA::IntervalFeature, "key")
    descriptor = None
    for klass in ORDB4ORA::IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::rawfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::RawFeature)


def test_ordb4ora::rawfeature_constructor_exists():
    assert callable(ORDB4ORA::RawFeature.__init__)


def test_ordb4ora::rawfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA::RawFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora::rawfeature_has_value():
    assert hasattr(ORDB4ORA::RawFeature, "value")
    descriptor = None
    for klass in ORDB4ORA::RawFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::rawfeature_has_key():
    assert hasattr(ORDB4ORA::RawFeature, "key")
    descriptor = None
    for klass in ORDB4ORA::RawFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::datetimefeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::DatetimeFeature)


def test_ordb4ora::datetimefeature_constructor_exists():
    assert callable(ORDB4ORA::DatetimeFeature.__init__)


def test_ordb4ora::datetimefeature_constructor_args():
    sig = inspect.signature(ORDB4ORA::DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora::datetimefeature_has_value():
    assert hasattr(ORDB4ORA::DatetimeFeature, "value")
    descriptor = None
    for klass in ORDB4ORA::DatetimeFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::datetimefeature_has_key():
    assert hasattr(ORDB4ORA::DatetimeFeature, "key")
    descriptor = None
    for klass in ORDB4ORA::DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::characterfeature_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::CharacterFeature)


def test_ordb4ora::characterfeature_constructor_exists():
    assert callable(ORDB4ORA::CharacterFeature.__init__)


def test_ordb4ora::characterfeature_constructor_args():
    sig = inspect.signature(ORDB4ORA::CharacterFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_ordb4ora::characterfeature_has_value():
    assert hasattr(ORDB4ORA::CharacterFeature, "value")
    descriptor = None
    for klass in ORDB4ORA::CharacterFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::characterfeature_has_key():
    assert hasattr(ORDB4ORA::CharacterFeature, "key")
    descriptor = None
    for klass in ORDB4ORA::CharacterFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_ansitype_is_not_abstract():
    assert not inspect.isabstract(ANSIType)


def test_ansitype_constructor_exists():
    assert callable(ANSIType.__init__)


def test_ansitype_constructor_args():
    sig = inspect.signature(ANSIType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::ansicharactertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::ANSICharacterType)


def test_ordb4ora::ansicharactertype_constructor_exists():
    assert callable(ORDB4ORA::ANSICharacterType.__init__)


def test_ordb4ora::ansicharactertype_constructor_args():
    sig = inspect.signature(ORDB4ORA::ANSICharacterType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::ansicharactertype_has_Descriptor():
    assert hasattr(ORDB4ORA::ANSICharacterType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::ANSICharacterType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::package_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Package)


def test_ordb4ora::package_constructor_exists():
    assert callable(ORDB4ORA::Package.__init__)


def test_ordb4ora::package_constructor_args():
    sig = inspect.signature(ORDB4ORA::Package.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::package_has_Name():
    assert hasattr(ORDB4ORA::Package, "Name")
    descriptor = None
    for klass in ORDB4ORA::Package.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::operation_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Operation)


def test_ordb4ora::operation_constructor_exists():
    assert callable(ORDB4ORA::Operation.__init__)


def test_ordb4ora::operation_constructor_args():
    sig = inspect.signature(ORDB4ORA::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::operation_has_Body():
    assert hasattr(ORDB4ORA::Operation, "Body")
    descriptor = None
    for klass in ORDB4ORA::Operation.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::operation_has_Name():
    assert hasattr(ORDB4ORA::Operation, "Name")
    descriptor = None
    for klass in ORDB4ORA::Operation.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::table_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Table)


def test_ordb4ora::table_constructor_exists():
    assert callable(ORDB4ORA::Table.__init__)


def test_ordb4ora::table_constructor_args():
    sig = inspect.signature(ORDB4ORA::Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::table_has_Name():
    assert hasattr(ORDB4ORA::Table, "Name")
    descriptor = None
    for klass in ORDB4ORA::Table.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::datatype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Datatype)


def test_ordb4ora::datatype_constructor_exists():
    assert callable(ORDB4ORA::Datatype.__init__)


def test_ordb4ora::datatype_constructor_args():
    sig = inspect.signature(ORDB4ORA::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::model_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Model)


def test_ordb4ora::model_constructor_exists():
    assert callable(ORDB4ORA::Model.__init__)


def test_ordb4ora::model_constructor_args():
    sig = inspect.signature(ORDB4ORA::Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::model_has_Name():
    assert hasattr(ORDB4ORA::Model, "Name")
    descriptor = None
    for klass in ORDB4ORA::Model.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(Datatype)


def test_datatype_constructor_exists():
    assert callable(Datatype.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(Datatype.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::varray_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Varray)


def test_ordb4ora::varray_constructor_exists():
    assert callable(ORDB4ORA::Varray.__init__)


def test_ordb4ora::varray_constructor_args():
    sig = inspect.signature(ORDB4ORA::Varray.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "NumElements" in params, "Missing parameter 'NumElements'"

def test_ordb4ora::varray_has_Name():
    assert hasattr(ORDB4ORA::Varray, "Name")
    descriptor = None
    for klass in ORDB4ORA::Varray.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::varray_has_NumElements():
    assert hasattr(ORDB4ORA::Varray, "NumElements")
    descriptor = None
    for klass in ORDB4ORA::Varray.__mro__:
        if "NumElements" in klass.__dict__:
            descriptor = klass.__dict__["NumElements"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::nestedtabletype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::NestedTableType)


def test_ordb4ora::nestedtabletype_constructor_exists():
    assert callable(ORDB4ORA::NestedTableType.__init__)


def test_ordb4ora::nestedtabletype_constructor_args():
    sig = inspect.signature(ORDB4ORA::NestedTableType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::nestedtabletype_has_Name():
    assert hasattr(ORDB4ORA::NestedTableType, "Name")
    descriptor = None
    for klass in ORDB4ORA::NestedTableType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::referencetype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::ReferenceType)


def test_ordb4ora::referencetype_constructor_exists():
    assert callable(ORDB4ORA::ReferenceType.__init__)


def test_ordb4ora::referencetype_constructor_args():
    sig = inspect.signature(ORDB4ORA::ReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::referencetype_has_Name():
    assert hasattr(ORDB4ORA::ReferenceType, "Name")
    descriptor = None
    for klass in ORDB4ORA::ReferenceType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::basicdatatype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::BasicDataType)


def test_ordb4ora::basicdatatype_constructor_exists():
    assert callable(ORDB4ORA::BasicDataType.__init__)


def test_ordb4ora::basicdatatype_constructor_args():
    sig = inspect.signature(ORDB4ORA::BasicDataType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::structuredtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::StructuredType)


def test_ordb4ora::structuredtype_constructor_exists():
    assert callable(ORDB4ORA::StructuredType.__init__)


def test_ordb4ora::structuredtype_constructor_args():
    sig = inspect.signature(ORDB4ORA::StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"
    assert "is_final" in params, "Missing parameter 'is_final'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_ordb4ora::structuredtype_has_is_instantiable():
    assert hasattr(ORDB4ORA::StructuredType, "is_instantiable")
    descriptor = None
    for klass in ORDB4ORA::StructuredType.__mro__:
        if "is_instantiable" in klass.__dict__:
            descriptor = klass.__dict__["is_instantiable"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::structuredtype_has_is_final():
    assert hasattr(ORDB4ORA::StructuredType, "is_final")
    descriptor = None
    for klass in ORDB4ORA::StructuredType.__mro__:
        if "is_final" in klass.__dict__:
            descriptor = klass.__dict__["is_final"]
            break
    assert isinstance(descriptor, property)

def test_ordb4ora::structuredtype_has_Name():
    assert hasattr(ORDB4ORA::StructuredType, "Name")
    descriptor = None
    for klass in ORDB4ORA::StructuredType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(StructuralComponent)


def test_structuralcomponent_constructor_exists():
    assert callable(StructuralComponent.__init__)


def test_structuralcomponent_constructor_args():
    sig = inspect.signature(StructuralComponent.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::column_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Column)


def test_ordb4ora::column_constructor_exists():
    assert callable(ORDB4ORA::Column.__init__)


def test_ordb4ora::column_constructor_args():
    sig = inspect.signature(ORDB4ORA::Column.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::attribute_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::Attribute)


def test_ordb4ora::attribute_constructor_exists():
    assert callable(ORDB4ORA::Attribute.__init__)


def test_ordb4ora::attribute_constructor_args():
    sig = inspect.signature(ORDB4ORA::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_suppliedtype_is_not_abstract():
    assert not inspect.isabstract(SuppliedType)


def test_suppliedtype_constructor_exists():
    assert callable(SuppliedType.__init__)


def test_suppliedtype_constructor_args():
    sig = inspect.signature(SuppliedType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::mediatype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::MediaType)


def test_ordb4ora::mediatype_constructor_exists():
    assert callable(ORDB4ORA::MediaType.__init__)


def test_ordb4ora::mediatype_constructor_args():
    sig = inspect.signature(ORDB4ORA::MediaType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::mediatype_has_Descriptor():
    assert hasattr(ORDB4ORA::MediaType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::MediaType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::xmltype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::XMLType)


def test_ordb4ora::xmltype_constructor_exists():
    assert callable(ORDB4ORA::XMLType.__init__)


def test_ordb4ora::xmltype_constructor_args():
    sig = inspect.signature(ORDB4ORA::XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::xmltype_has_Descriptor():
    assert hasattr(ORDB4ORA::XMLType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::XMLType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::spacialtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::SpacialType)


def test_ordb4ora::spacialtype_constructor_exists():
    assert callable(ORDB4ORA::SpacialType.__init__)


def test_ordb4ora::spacialtype_constructor_args():
    sig = inspect.signature(ORDB4ORA::SpacialType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::spacialtype_has_Descriptor():
    assert hasattr(ORDB4ORA::SpacialType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::SpacialType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)



def test_ordb4ora::anytype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::AnyType)


def test_ordb4ora::anytype_constructor_exists():
    assert callable(ORDB4ORA::AnyType.__init__)


def test_ordb4ora::anytype_constructor_args():
    sig = inspect.signature(ORDB4ORA::AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::anytype_has_Descriptor():
    assert hasattr(ORDB4ORA::AnyType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::AnyType.__mro__:
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



def test_ordb4ora::builtintype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::BuiltInType)


def test_ordb4ora::builtintype_constructor_exists():
    assert callable(ORDB4ORA::BuiltInType.__init__)


def test_ordb4ora::builtintype_constructor_args():
    sig = inspect.signature(ORDB4ORA::BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::suppliedtype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::SuppliedType)


def test_ordb4ora::suppliedtype_constructor_exists():
    assert callable(ORDB4ORA::SuppliedType.__init__)


def test_ordb4ora::suppliedtype_constructor_args():
    sig = inspect.signature(ORDB4ORA::SuppliedType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::ansitype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::ANSIType)


def test_ordb4ora::ansitype_constructor_exists():
    assert callable(ORDB4ORA::ANSIType.__init__)


def test_ordb4ora::ansitype_constructor_args():
    sig = inspect.signature(ORDB4ORA::ANSIType.__init__)
    params = list(sig.parameters.keys())



def test_ordb4ora::ansinumbertype_is_not_abstract():
    assert not inspect.isabstract(ORDB4ORA::ANSINumberType)


def test_ordb4ora::ansinumbertype_constructor_exists():
    assert callable(ORDB4ORA::ANSINumberType.__init__)


def test_ordb4ora::ansinumbertype_constructor_args():
    sig = inspect.signature(ORDB4ORA::ANSINumberType.__init__)
    params = list(sig.parameters.keys())
    assert "Descriptor" in params, "Missing parameter 'Descriptor'"

def test_ordb4ora::ansinumbertype_has_Descriptor():
    assert hasattr(ORDB4ORA::ANSINumberType, "Descriptor")
    descriptor = None
    for klass in ORDB4ORA::ANSINumberType.__mro__:
        if "Descriptor" in klass.__dict__:
            descriptor = klass.__dict__["Descriptor"]
            break
    assert isinstance(descriptor, property)

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

def test_builtindatetimetypes_exists():
    # Check that the Enumeration exists
    assert BuiltInDatetimeTypes is not None

def test_builtindatetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInDatetimeTypes]
    expected_literals = [
        "DATE",
        "TIMESTAMPWITHLOCALTIMEZONE",
        "TIMESTAMP",
        "TIMESTAMPWITHTIMEZONE",
        "INTERVALYEARTOMONTH",
        "INTERVALDAYTOSECOND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInDatetimeTypes"

def test_ondeleteactions_exists():
    # Check that the Enumeration exists
    assert ONDELETEActions is not None

def test_ondeleteactions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ONDELETEActions]
    expected_literals = [
        "SETNULL",
        "CASCADE",
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
        "CHAR",
        "NCHAR",
        "VARCHAR2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInCharacterTypes"

def test_suppliedmediatypes_exists():
    # Check that the Enumeration exists
    assert SuppliedMediaTypes is not None

def test_suppliedmediatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuppliedMediaTypes]
    expected_literals = [
        "ORDImage",
        "SI_FEATURELIST",
        "SI_AVERAGECOLOR",
        "SI_COLORHISTOGRAM",
        "SI_TEXTURE",
        "ORDImageSignature",
        "ORDDoc",
        "SI_POSITIONALCOLOR",
        "SI_COLOR",
        "ORDAudio",
        "ORDVideo",
        "SI_STILLIMAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuppliedMediaTypes"

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

def test_numberfeatures_exists():
    # Check that the Enumeration exists
    assert NumberFeatures is not None

def test_numberfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberFeatures]
    expected_literals = [
        "precision",
        "size",
        "scale",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberFeatures"

def test_ansicharactertypes_exists():
    # Check that the Enumeration exists
    assert ANSICharacterTypes is not None

def test_ansicharactertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ANSICharacterTypes]
    expected_literals = [
        "NATIONALCHARACTERVARYING",
        "CHARACTERVARYING",
        "NATIONALCHARACTER",
        "NATIONALCHARVARYING",
        "NATIONALCHAR",
        "VARCHAR",
        "NCHARVARYING",
        "CHARVARYING",
        "CHARACTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ANSICharacterTypes"

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

def test_builtinlobtype_exists():
    # Check that the Enumeration exists
    assert BuiltInLOBType is not None

def test_builtinlobtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInLOBType]
    expected_literals = [
        "NLOB",
        "CLOB",
        "BLOB",
        "BFILE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInLOBType"

def test_characterfeatures_exists():
    # Check that the Enumeration exists
    assert CharacterFeatures is not None

def test_characterfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterFeatures]
    expected_literals = [
        "size",
        "semantic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterFeatures"

def test_ansinumbertypes_exists():
    # Check that the Enumeration exists
    assert ANSINumberTypes is not None

def test_ansinumbertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ANSINumberTypes]
    expected_literals = [
        "REAL",
        "INT",
        "SMALLINT",
        "NUMERIC",
        "DECIMAL",
        "FLOAT",
        "INTEGER",
        "DOUBLEPRECISION",
        "DEC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ANSINumberTypes"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "OUT",
        "IN",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

def test_builtincharactersemantics_exists():
    # Check that the Enumeration exists
    assert BuiltInCharacterSemantics is not None

def test_builtincharactersemantics_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInCharacterSemantics]
    expected_literals = [
        "CHAR",
        "BYTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInCharacterSemantics"

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

def test_builtinlongandrawtypes_exists():
    # Check that the Enumeration exists
    assert BuiltInLongAndRawTypes is not None

def test_builtinlongandrawtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInLongAndRawTypes]
    expected_literals = [
        "RAW",
        "LONG",
        "LONGRAW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInLongAndRawTypes"

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

def test_builtnumbertypes_exists():
    # Check that the Enumeration exists
    assert BuiltNumberTypes is not None

def test_builtnumbertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltNumberTypes]
    expected_literals = [
        "BINARY_DOUBLE",
        "BINARY_FLOAT",
        "NUMBER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltNumberTypes"

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

def test_suppliedanytypes_exists():
    # Check that the Enumeration exists
    assert SuppliedAnyTypes is not None

def test_suppliedanytypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuppliedAnyTypes]
    expected_literals = [
        "SYSANYDATA",
        "SYSANYDATASET",
        "SYSANYTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuppliedAnyTypes"

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

def test_triggeractiontime_exists():
    # Check that the Enumeration exists
    assert TriggerActionTime is not None

def test_triggeractiontime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerActionTime]
    expected_literals = [
        "AFTER",
        "INSTEADOF",
        "BEFORE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerActionTime"


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
Table_strategy = st.builds(
    Table,
)
ORDB4ORA::View_strategy = st.builds(
    ORDB4ORA::View,
)
ORDB4ORA::Trigger_strategy = st.builds(
    ORDB4ORA::Trigger,
    Event=
        safe_text,
    Name=
        safe_text,
    Action=
        safe_text,
    Body=
        safe_text
)
ORDB4ORA::DerivedTable_strategy = st.builds(
    ORDB4ORA::DerivedTable,
    query_expression=
        safe_text
)
ORDB4ORA::StructuralComponent_strategy = st.builds(
    ORDB4ORA::StructuralComponent,
    Name=
        safe_text
)
ORDB4ORA::Restriction_strategy = st.builds(
    ORDB4ORA::Restriction,
    NameColumns=
        safe_text,
    Name=
        safe_text
)
ORDB4ORA::TypedTable_strategy = st.builds(
    ORDB4ORA::TypedTable,
)
ORDB4ORA::StoredNestedTable_strategy = st.builds(
    ORDB4ORA::StoredNestedTable,
    Name=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
ORDB4ORA::OperationParameter_strategy = st.builds(
    ORDB4ORA::OperationParameter,
    Mode=
        safe_text
)
ORDB4ORA::MethodParameter_strategy = st.builds(
    ORDB4ORA::MethodParameter,
)
ORDB4ORA::Parameter_strategy = st.builds(
    ORDB4ORA::Parameter,
    Name=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
ORDB4ORA::Procedure_strategy = st.builds(
    ORDB4ORA::Procedure,
)
ORDB4ORA::Function_strategy = st.builds(
    ORDB4ORA::Function,
)
ORDB4ORA::Feature_strategy = st.builds(
    ORDB4ORA::Feature,
)
ORDB4ORA::Method_strategy = st.builds(
    ORDB4ORA::Method,
    Body=
        safe_text,
    Name=
        safe_text
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
ORDB4ORA::LOBType_strategy = st.builds(
    ORDB4ORA::LOBType,
    Descriptor=
        safe_text
)
ORDB4ORA::DatetimeType_strategy = st.builds(
    ORDB4ORA::DatetimeType,
    YearPrecision_Min=
        st.integers(),
    SecondPrecision_Def=
        st.integers(),
    SecondPrecision_Max=
        st.integers(),
    YearPrecision_Def=
        st.integers(),
    DayPrecision_Max=
        st.integers(),
    YearPrecision_Max=
        st.integers(),
    Descriptor=
        safe_text,
    DayPrecision_Def=
        st.integers(),
    DayPrecision_Min=
        st.integers(),
    SecondPrecision_Min=
        st.integers()
)
ORDB4ORA::ROWIDType_strategy = st.builds(
    ORDB4ORA::ROWIDType,
    Size_Min=
        st.integers(),
    Size_Max=
        st.integers(),
    Descriptor=
        safe_text
)
ORDB4ORA::LongAndRawType_strategy = st.builds(
    ORDB4ORA::LongAndRawType,
    Descriptor=
        safe_text,
    Size_Min=
        st.integers(),
    Size_Max=
        st.integers()
)
ORDB4ORA::BuiltInNumberType_strategy = st.builds(
    ORDB4ORA::BuiltInNumberType,
    Scale_Min=
        st.integers(),
    Descriptor=
        safe_text,
    Precision_Max=
        st.integers(),
    Precision_Mn=
        st.integers(),
    Scale_Max=
        st.integers()
)
ORDB4ORA::BuiltInCharacterType_strategy = st.builds(
    ORDB4ORA::BuiltInCharacterType,
    Size_Def=
        st.integers(),
    Semantic=
        safe_text,
    Size_Min=
        st.integers(),
    Size_Max=
        st.integers(),
    Descriptor=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
ORDB4ORA::NotNull_strategy = st.builds(
    ORDB4ORA::NotNull,
)
ORDB4ORA::Unique_strategy = st.builds(
    ORDB4ORA::Unique,
)
ORDB4ORA::PrimaryKey_strategy = st.builds(
    ORDB4ORA::PrimaryKey,
)
ORDB4ORA::ForeignKey_strategy = st.builds(
    ORDB4ORA::ForeignKey,
    OnDelete=
        safe_text
)
ORDB4ORA::Check_strategy = st.builds(
    ORDB4ORA::Check,
    Condition=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
ORDB4ORA::NumberFeature_strategy = st.builds(
    ORDB4ORA::NumberFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA::RowFeature_strategy = st.builds(
    ORDB4ORA::RowFeature,
    key=
        safe_text,
    value=
        safe_text
)
ORDB4ORA::IntervalFeature_strategy = st.builds(
    ORDB4ORA::IntervalFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA::RawFeature_strategy = st.builds(
    ORDB4ORA::RawFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA::DatetimeFeature_strategy = st.builds(
    ORDB4ORA::DatetimeFeature,
    value=
        safe_text,
    key=
        safe_text
)
ORDB4ORA::CharacterFeature_strategy = st.builds(
    ORDB4ORA::CharacterFeature,
    value=
        safe_text,
    key=
        safe_text
)
ANSIType_strategy = st.builds(
    ANSIType,
)
ORDB4ORA::ANSICharacterType_strategy = st.builds(
    ORDB4ORA::ANSICharacterType,
    Descriptor=
        safe_text
)
ORDB4ORA::Package_strategy = st.builds(
    ORDB4ORA::Package,
    Name=
        safe_text
)
ORDB4ORA::Operation_strategy = st.builds(
    ORDB4ORA::Operation,
    Body=
        safe_text,
    Name=
        safe_text
)
ORDB4ORA::Table_strategy = st.builds(
    ORDB4ORA::Table,
    Name=
        safe_text
)
ORDB4ORA::Datatype_strategy = st.builds(
    ORDB4ORA::Datatype,
)
ORDB4ORA::Model_strategy = st.builds(
    ORDB4ORA::Model,
    Name=
        safe_text
)
Datatype_strategy = st.builds(
    Datatype,
)
ORDB4ORA::Varray_strategy = st.builds(
    ORDB4ORA::Varray,
    Name=
        safe_text,
    NumElements=
        st.integers()
)
ORDB4ORA::NestedTableType_strategy = st.builds(
    ORDB4ORA::NestedTableType,
    Name=
        safe_text
)
ORDB4ORA::ReferenceType_strategy = st.builds(
    ORDB4ORA::ReferenceType,
    Name=
        safe_text
)
ORDB4ORA::BasicDataType_strategy = st.builds(
    ORDB4ORA::BasicDataType,
)
ORDB4ORA::StructuredType_strategy = st.builds(
    ORDB4ORA::StructuredType,
    is_instantiable=
        st.booleans(),
    is_final=
        st.booleans(),
    Name=
        safe_text
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
ORDB4ORA::Column_strategy = st.builds(
    ORDB4ORA::Column,
)
ORDB4ORA::Attribute_strategy = st.builds(
    ORDB4ORA::Attribute,
)
SuppliedType_strategy = st.builds(
    SuppliedType,
)
ORDB4ORA::MediaType_strategy = st.builds(
    ORDB4ORA::MediaType,
    Descriptor=
        safe_text
)
ORDB4ORA::XMLType_strategy = st.builds(
    ORDB4ORA::XMLType,
    Descriptor=
        safe_text
)
ORDB4ORA::SpacialType_strategy = st.builds(
    ORDB4ORA::SpacialType,
    Descriptor=
        safe_text
)
ORDB4ORA::AnyType_strategy = st.builds(
    ORDB4ORA::AnyType,
    Descriptor=
        safe_text
)
BasicDataType_strategy = st.builds(
    BasicDataType,
)
ORDB4ORA::BuiltInType_strategy = st.builds(
    ORDB4ORA::BuiltInType,
)
ORDB4ORA::SuppliedType_strategy = st.builds(
    ORDB4ORA::SuppliedType,
)
ORDB4ORA::ANSIType_strategy = st.builds(
    ORDB4ORA::ANSIType,
)
ORDB4ORA::ANSINumberType_strategy = st.builds(
    ORDB4ORA::ANSINumberType,
    Descriptor=
        safe_text
)

@given(instance=DerivedTable_strategy)
@settings(max_examples=50)
def test_derivedtable_instantiation(instance):
    assert isinstance(instance, DerivedTable)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=ORDB4ORA::View_strategy)
@settings(max_examples=50)
def test_ordb4ora::view_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::View)

@given(instance=ORDB4ORA::Trigger_strategy)
@settings(max_examples=50)
def test_ordb4ora::trigger_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Trigger)

@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Event_type(instance):
    assert isinstance(instance.Event, str)


@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original

@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Action_type(instance):
    assert isinstance(instance.Action, str)


@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Action_setter(instance):
    original = instance.Action
    instance.Action = original
    assert instance.Action == original

@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=ORDB4ORA::Trigger_strategy)
def test_ordb4ora::trigger_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=ORDB4ORA::DerivedTable_strategy)
@settings(max_examples=50)
def test_ordb4ora::derivedtable_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::DerivedTable)

@given(instance=ORDB4ORA::DerivedTable_strategy)
def test_ordb4ora::derivedtable_query_expression_type(instance):
    assert isinstance(instance.query_expression, str)


@given(instance=ORDB4ORA::DerivedTable_strategy)
def test_ordb4ora::derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=ORDB4ORA::StructuralComponent_strategy)
@settings(max_examples=50)
def test_ordb4ora::structuralcomponent_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::StructuralComponent)

@given(instance=ORDB4ORA::StructuralComponent_strategy)
def test_ordb4ora::structuralcomponent_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::StructuralComponent_strategy)
def test_ordb4ora::structuralcomponent_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::Restriction_strategy)
@settings(max_examples=50)
def test_ordb4ora::restriction_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Restriction)

@given(instance=ORDB4ORA::Restriction_strategy)
def test_ordb4ora::restriction_NameColumns_type(instance):
    assert isinstance(instance.NameColumns, str)


@given(instance=ORDB4ORA::Restriction_strategy)
def test_ordb4ora::restriction_NameColumns_setter(instance):
    original = instance.NameColumns
    instance.NameColumns = original
    assert instance.NameColumns == original

@given(instance=ORDB4ORA::Restriction_strategy)
def test_ordb4ora::restriction_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Restriction_strategy)
def test_ordb4ora::restriction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::TypedTable_strategy)
@settings(max_examples=50)
def test_ordb4ora::typedtable_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::TypedTable)

@given(instance=ORDB4ORA::StoredNestedTable_strategy)
@settings(max_examples=50)
def test_ordb4ora::storednestedtable_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::StoredNestedTable)

@given(instance=ORDB4ORA::StoredNestedTable_strategy)
def test_ordb4ora::storednestedtable_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::StoredNestedTable_strategy)
def test_ordb4ora::storednestedtable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=ORDB4ORA::OperationParameter_strategy)
@settings(max_examples=50)
def test_ordb4ora::operationparameter_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::OperationParameter)

@given(instance=ORDB4ORA::OperationParameter_strategy)
def test_ordb4ora::operationparameter_Mode_type(instance):
    assert isinstance(instance.Mode, str)


@given(instance=ORDB4ORA::OperationParameter_strategy)
def test_ordb4ora::operationparameter_Mode_setter(instance):
    original = instance.Mode
    instance.Mode = original
    assert instance.Mode == original

@given(instance=ORDB4ORA::MethodParameter_strategy)
@settings(max_examples=50)
def test_ordb4ora::methodparameter_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::MethodParameter)

@given(instance=ORDB4ORA::Parameter_strategy)
@settings(max_examples=50)
def test_ordb4ora::parameter_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Parameter)

@given(instance=ORDB4ORA::Parameter_strategy)
def test_ordb4ora::parameter_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Parameter_strategy)
def test_ordb4ora::parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=ORDB4ORA::Procedure_strategy)
@settings(max_examples=50)
def test_ordb4ora::procedure_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Procedure)

@given(instance=ORDB4ORA::Function_strategy)
@settings(max_examples=50)
def test_ordb4ora::function_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Function)

@given(instance=ORDB4ORA::Feature_strategy)
@settings(max_examples=50)
def test_ordb4ora::feature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Feature)

@given(instance=ORDB4ORA::Method_strategy)
@settings(max_examples=50)
def test_ordb4ora::method_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Method)

@given(instance=ORDB4ORA::Method_strategy)
def test_ordb4ora::method_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=ORDB4ORA::Method_strategy)
def test_ordb4ora::method_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=ORDB4ORA::Method_strategy)
def test_ordb4ora::method_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Method_strategy)
def test_ordb4ora::method_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=ORDB4ORA::LOBType_strategy)
@settings(max_examples=50)
def test_ordb4ora::lobtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::LOBType)

@given(instance=ORDB4ORA::LOBType_strategy)
def test_ordb4ora::lobtype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::LOBType_strategy)
def test_ordb4ora::lobtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
@settings(max_examples=50)
def test_ordb4ora::datetimetype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::DatetimeType)

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_YearPrecision_Min_type(instance):
    assert isinstance(instance.YearPrecision_Min, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_YearPrecision_Min_setter(instance):
    original = instance.YearPrecision_Min
    instance.YearPrecision_Min = original
    assert instance.YearPrecision_Min == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_SecondPrecision_Def_type(instance):
    assert isinstance(instance.SecondPrecision_Def, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_SecondPrecision_Def_setter(instance):
    original = instance.SecondPrecision_Def
    instance.SecondPrecision_Def = original
    assert instance.SecondPrecision_Def == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_SecondPrecision_Max_type(instance):
    assert isinstance(instance.SecondPrecision_Max, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_SecondPrecision_Max_setter(instance):
    original = instance.SecondPrecision_Max
    instance.SecondPrecision_Max = original
    assert instance.SecondPrecision_Max == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_YearPrecision_Def_type(instance):
    assert isinstance(instance.YearPrecision_Def, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_YearPrecision_Def_setter(instance):
    original = instance.YearPrecision_Def
    instance.YearPrecision_Def = original
    assert instance.YearPrecision_Def == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_DayPrecision_Max_type(instance):
    assert isinstance(instance.DayPrecision_Max, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_DayPrecision_Max_setter(instance):
    original = instance.DayPrecision_Max
    instance.DayPrecision_Max = original
    assert instance.DayPrecision_Max == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_YearPrecision_Max_type(instance):
    assert isinstance(instance.YearPrecision_Max, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_YearPrecision_Max_setter(instance):
    original = instance.YearPrecision_Max
    instance.YearPrecision_Max = original
    assert instance.YearPrecision_Max == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_DayPrecision_Def_type(instance):
    assert isinstance(instance.DayPrecision_Def, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_DayPrecision_Def_setter(instance):
    original = instance.DayPrecision_Def
    instance.DayPrecision_Def = original
    assert instance.DayPrecision_Def == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_DayPrecision_Min_type(instance):
    assert isinstance(instance.DayPrecision_Min, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_DayPrecision_Min_setter(instance):
    original = instance.DayPrecision_Min
    instance.DayPrecision_Min = original
    assert instance.DayPrecision_Min == original

@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_SecondPrecision_Min_type(instance):
    assert isinstance(instance.SecondPrecision_Min, int)


@given(instance=ORDB4ORA::DatetimeType_strategy)
def test_ordb4ora::datetimetype_SecondPrecision_Min_setter(instance):
    original = instance.SecondPrecision_Min
    instance.SecondPrecision_Min = original
    assert instance.SecondPrecision_Min == original

@given(instance=ORDB4ORA::ROWIDType_strategy)
@settings(max_examples=50)
def test_ordb4ora::rowidtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::ROWIDType)

@given(instance=ORDB4ORA::ROWIDType_strategy)
def test_ordb4ora::rowidtype_Size_Min_type(instance):
    assert isinstance(instance.Size_Min, int)


@given(instance=ORDB4ORA::ROWIDType_strategy)
def test_ordb4ora::rowidtype_Size_Min_setter(instance):
    original = instance.Size_Min
    instance.Size_Min = original
    assert instance.Size_Min == original

@given(instance=ORDB4ORA::ROWIDType_strategy)
def test_ordb4ora::rowidtype_Size_Max_type(instance):
    assert isinstance(instance.Size_Max, int)


@given(instance=ORDB4ORA::ROWIDType_strategy)
def test_ordb4ora::rowidtype_Size_Max_setter(instance):
    original = instance.Size_Max
    instance.Size_Max = original
    assert instance.Size_Max == original

@given(instance=ORDB4ORA::ROWIDType_strategy)
def test_ordb4ora::rowidtype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::ROWIDType_strategy)
def test_ordb4ora::rowidtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::LongAndRawType_strategy)
@settings(max_examples=50)
def test_ordb4ora::longandrawtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::LongAndRawType)

@given(instance=ORDB4ORA::LongAndRawType_strategy)
def test_ordb4ora::longandrawtype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::LongAndRawType_strategy)
def test_ordb4ora::longandrawtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::LongAndRawType_strategy)
def test_ordb4ora::longandrawtype_Size_Min_type(instance):
    assert isinstance(instance.Size_Min, int)


@given(instance=ORDB4ORA::LongAndRawType_strategy)
def test_ordb4ora::longandrawtype_Size_Min_setter(instance):
    original = instance.Size_Min
    instance.Size_Min = original
    assert instance.Size_Min == original

@given(instance=ORDB4ORA::LongAndRawType_strategy)
def test_ordb4ora::longandrawtype_Size_Max_type(instance):
    assert isinstance(instance.Size_Max, int)


@given(instance=ORDB4ORA::LongAndRawType_strategy)
def test_ordb4ora::longandrawtype_Size_Max_setter(instance):
    original = instance.Size_Max
    instance.Size_Max = original
    assert instance.Size_Max == original

@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
@settings(max_examples=50)
def test_ordb4ora::builtinnumbertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::BuiltInNumberType)

@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Scale_Min_type(instance):
    assert isinstance(instance.Scale_Min, int)


@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Scale_Min_setter(instance):
    original = instance.Scale_Min
    instance.Scale_Min = original
    assert instance.Scale_Min == original

@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Precision_Max_type(instance):
    assert isinstance(instance.Precision_Max, int)


@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Precision_Max_setter(instance):
    original = instance.Precision_Max
    instance.Precision_Max = original
    assert instance.Precision_Max == original

@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Precision_Mn_type(instance):
    assert isinstance(instance.Precision_Mn, int)


@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Precision_Mn_setter(instance):
    original = instance.Precision_Mn
    instance.Precision_Mn = original
    assert instance.Precision_Mn == original

@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Scale_Max_type(instance):
    assert isinstance(instance.Scale_Max, int)


@given(instance=ORDB4ORA::BuiltInNumberType_strategy)
def test_ordb4ora::builtinnumbertype_Scale_Max_setter(instance):
    original = instance.Scale_Max
    instance.Scale_Max = original
    assert instance.Scale_Max == original

@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
@settings(max_examples=50)
def test_ordb4ora::builtincharactertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::BuiltInCharacterType)

@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Size_Def_type(instance):
    assert isinstance(instance.Size_Def, int)


@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Size_Def_setter(instance):
    original = instance.Size_Def
    instance.Size_Def = original
    assert instance.Size_Def == original

@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Semantic_type(instance):
    assert isinstance(instance.Semantic, str)


@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Semantic_setter(instance):
    original = instance.Semantic
    instance.Semantic = original
    assert instance.Semantic == original

@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Size_Min_type(instance):
    assert isinstance(instance.Size_Min, int)


@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Size_Min_setter(instance):
    original = instance.Size_Min
    instance.Size_Min = original
    assert instance.Size_Min == original

@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Size_Max_type(instance):
    assert isinstance(instance.Size_Max, int)


@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Size_Max_setter(instance):
    original = instance.Size_Max
    instance.Size_Max = original
    assert instance.Size_Max == original

@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::BuiltInCharacterType_strategy)
def test_ordb4ora::builtincharactertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=ORDB4ORA::NotNull_strategy)
@settings(max_examples=50)
def test_ordb4ora::notnull_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::NotNull)

@given(instance=ORDB4ORA::Unique_strategy)
@settings(max_examples=50)
def test_ordb4ora::unique_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Unique)

@given(instance=ORDB4ORA::PrimaryKey_strategy)
@settings(max_examples=50)
def test_ordb4ora::primarykey_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::PrimaryKey)

@given(instance=ORDB4ORA::ForeignKey_strategy)
@settings(max_examples=50)
def test_ordb4ora::foreignkey_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::ForeignKey)

@given(instance=ORDB4ORA::ForeignKey_strategy)
def test_ordb4ora::foreignkey_OnDelete_type(instance):
    assert isinstance(instance.OnDelete, str)


@given(instance=ORDB4ORA::ForeignKey_strategy)
def test_ordb4ora::foreignkey_OnDelete_setter(instance):
    original = instance.OnDelete
    instance.OnDelete = original
    assert instance.OnDelete == original

@given(instance=ORDB4ORA::Check_strategy)
@settings(max_examples=50)
def test_ordb4ora::check_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Check)

@given(instance=ORDB4ORA::Check_strategy)
def test_ordb4ora::check_Condition_type(instance):
    assert isinstance(instance.Condition, str)


@given(instance=ORDB4ORA::Check_strategy)
def test_ordb4ora::check_Condition_setter(instance):
    original = instance.Condition
    instance.Condition = original
    assert instance.Condition == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ORDB4ORA::NumberFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora::numberfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::NumberFeature)

@given(instance=ORDB4ORA::NumberFeature_strategy)
def test_ordb4ora::numberfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ORDB4ORA::NumberFeature_strategy)
def test_ordb4ora::numberfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA::NumberFeature_strategy)
def test_ordb4ora::numberfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ORDB4ORA::NumberFeature_strategy)
def test_ordb4ora::numberfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA::RowFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora::rowfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::RowFeature)

@given(instance=ORDB4ORA::RowFeature_strategy)
def test_ordb4ora::rowfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ORDB4ORA::RowFeature_strategy)
def test_ordb4ora::rowfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA::RowFeature_strategy)
def test_ordb4ora::rowfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ORDB4ORA::RowFeature_strategy)
def test_ordb4ora::rowfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA::IntervalFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora::intervalfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::IntervalFeature)

@given(instance=ORDB4ORA::IntervalFeature_strategy)
def test_ordb4ora::intervalfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ORDB4ORA::IntervalFeature_strategy)
def test_ordb4ora::intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA::IntervalFeature_strategy)
def test_ordb4ora::intervalfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ORDB4ORA::IntervalFeature_strategy)
def test_ordb4ora::intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA::RawFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora::rawfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::RawFeature)

@given(instance=ORDB4ORA::RawFeature_strategy)
def test_ordb4ora::rawfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ORDB4ORA::RawFeature_strategy)
def test_ordb4ora::rawfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA::RawFeature_strategy)
def test_ordb4ora::rawfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ORDB4ORA::RawFeature_strategy)
def test_ordb4ora::rawfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA::DatetimeFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora::datetimefeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::DatetimeFeature)

@given(instance=ORDB4ORA::DatetimeFeature_strategy)
def test_ordb4ora::datetimefeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ORDB4ORA::DatetimeFeature_strategy)
def test_ordb4ora::datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA::DatetimeFeature_strategy)
def test_ordb4ora::datetimefeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ORDB4ORA::DatetimeFeature_strategy)
def test_ordb4ora::datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ORDB4ORA::CharacterFeature_strategy)
@settings(max_examples=50)
def test_ordb4ora::characterfeature_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::CharacterFeature)

@given(instance=ORDB4ORA::CharacterFeature_strategy)
def test_ordb4ora::characterfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ORDB4ORA::CharacterFeature_strategy)
def test_ordb4ora::characterfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ORDB4ORA::CharacterFeature_strategy)
def test_ordb4ora::characterfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=ORDB4ORA::CharacterFeature_strategy)
def test_ordb4ora::characterfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ANSIType_strategy)
@settings(max_examples=50)
def test_ansitype_instantiation(instance):
    assert isinstance(instance, ANSIType)

@given(instance=ORDB4ORA::ANSICharacterType_strategy)
@settings(max_examples=50)
def test_ordb4ora::ansicharactertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::ANSICharacterType)

@given(instance=ORDB4ORA::ANSICharacterType_strategy)
def test_ordb4ora::ansicharactertype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::ANSICharacterType_strategy)
def test_ordb4ora::ansicharactertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::Package_strategy)
@settings(max_examples=50)
def test_ordb4ora::package_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Package)

@given(instance=ORDB4ORA::Package_strategy)
def test_ordb4ora::package_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Package_strategy)
def test_ordb4ora::package_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::Operation_strategy)
@settings(max_examples=50)
def test_ordb4ora::operation_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Operation)

@given(instance=ORDB4ORA::Operation_strategy)
def test_ordb4ora::operation_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=ORDB4ORA::Operation_strategy)
def test_ordb4ora::operation_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=ORDB4ORA::Operation_strategy)
def test_ordb4ora::operation_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Operation_strategy)
def test_ordb4ora::operation_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::Table_strategy)
@settings(max_examples=50)
def test_ordb4ora::table_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Table)

@given(instance=ORDB4ORA::Table_strategy)
def test_ordb4ora::table_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Table_strategy)
def test_ordb4ora::table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::Datatype_strategy)
@settings(max_examples=50)
def test_ordb4ora::datatype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Datatype)

@given(instance=ORDB4ORA::Model_strategy)
@settings(max_examples=50)
def test_ordb4ora::model_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Model)

@given(instance=ORDB4ORA::Model_strategy)
def test_ordb4ora::model_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Model_strategy)
def test_ordb4ora::model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Datatype_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, Datatype)

@given(instance=ORDB4ORA::Varray_strategy)
@settings(max_examples=50)
def test_ordb4ora::varray_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Varray)

@given(instance=ORDB4ORA::Varray_strategy)
def test_ordb4ora::varray_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::Varray_strategy)
def test_ordb4ora::varray_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::Varray_strategy)
def test_ordb4ora::varray_NumElements_type(instance):
    assert isinstance(instance.NumElements, int)


@given(instance=ORDB4ORA::Varray_strategy)
def test_ordb4ora::varray_NumElements_setter(instance):
    original = instance.NumElements
    instance.NumElements = original
    assert instance.NumElements == original

@given(instance=ORDB4ORA::NestedTableType_strategy)
@settings(max_examples=50)
def test_ordb4ora::nestedtabletype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::NestedTableType)

@given(instance=ORDB4ORA::NestedTableType_strategy)
def test_ordb4ora::nestedtabletype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::NestedTableType_strategy)
def test_ordb4ora::nestedtabletype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::ReferenceType_strategy)
@settings(max_examples=50)
def test_ordb4ora::referencetype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::ReferenceType)

@given(instance=ORDB4ORA::ReferenceType_strategy)
def test_ordb4ora::referencetype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::ReferenceType_strategy)
def test_ordb4ora::referencetype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ORDB4ORA::BasicDataType_strategy)
@settings(max_examples=50)
def test_ordb4ora::basicdatatype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::BasicDataType)

@given(instance=ORDB4ORA::StructuredType_strategy)
@settings(max_examples=50)
def test_ordb4ora::structuredtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::StructuredType)

@given(instance=ORDB4ORA::StructuredType_strategy)
def test_ordb4ora::structuredtype_is_instantiable_type(instance):
    assert isinstance(instance.is_instantiable, bool)


@given(instance=ORDB4ORA::StructuredType_strategy)
def test_ordb4ora::structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original

@given(instance=ORDB4ORA::StructuredType_strategy)
def test_ordb4ora::structuredtype_is_final_type(instance):
    assert isinstance(instance.is_final, bool)


@given(instance=ORDB4ORA::StructuredType_strategy)
def test_ordb4ora::structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original

@given(instance=ORDB4ORA::StructuredType_strategy)
def test_ordb4ora::structuredtype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ORDB4ORA::StructuredType_strategy)
def test_ordb4ora::structuredtype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=ORDB4ORA::Column_strategy)
@settings(max_examples=50)
def test_ordb4ora::column_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Column)

@given(instance=ORDB4ORA::Attribute_strategy)
@settings(max_examples=50)
def test_ordb4ora::attribute_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::Attribute)

@given(instance=SuppliedType_strategy)
@settings(max_examples=50)
def test_suppliedtype_instantiation(instance):
    assert isinstance(instance, SuppliedType)

@given(instance=ORDB4ORA::MediaType_strategy)
@settings(max_examples=50)
def test_ordb4ora::mediatype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::MediaType)

@given(instance=ORDB4ORA::MediaType_strategy)
def test_ordb4ora::mediatype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::MediaType_strategy)
def test_ordb4ora::mediatype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::XMLType_strategy)
@settings(max_examples=50)
def test_ordb4ora::xmltype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::XMLType)

@given(instance=ORDB4ORA::XMLType_strategy)
def test_ordb4ora::xmltype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::XMLType_strategy)
def test_ordb4ora::xmltype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::SpacialType_strategy)
@settings(max_examples=50)
def test_ordb4ora::spacialtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::SpacialType)

@given(instance=ORDB4ORA::SpacialType_strategy)
def test_ordb4ora::spacialtype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::SpacialType_strategy)
def test_ordb4ora::spacialtype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=ORDB4ORA::AnyType_strategy)
@settings(max_examples=50)
def test_ordb4ora::anytype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::AnyType)

@given(instance=ORDB4ORA::AnyType_strategy)
def test_ordb4ora::anytype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::AnyType_strategy)
def test_ordb4ora::anytype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original

@given(instance=BasicDataType_strategy)
@settings(max_examples=50)
def test_basicdatatype_instantiation(instance):
    assert isinstance(instance, BasicDataType)

@given(instance=ORDB4ORA::BuiltInType_strategy)
@settings(max_examples=50)
def test_ordb4ora::builtintype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::BuiltInType)

@given(instance=ORDB4ORA::SuppliedType_strategy)
@settings(max_examples=50)
def test_ordb4ora::suppliedtype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::SuppliedType)

@given(instance=ORDB4ORA::ANSIType_strategy)
@settings(max_examples=50)
def test_ordb4ora::ansitype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::ANSIType)

@given(instance=ORDB4ORA::ANSINumberType_strategy)
@settings(max_examples=50)
def test_ordb4ora::ansinumbertype_instantiation(instance):
    assert isinstance(instance, ORDB4ORA::ANSINumberType)

@given(instance=ORDB4ORA::ANSINumberType_strategy)
def test_ordb4ora::ansinumbertype_Descriptor_type(instance):
    assert isinstance(instance.Descriptor, str)


@given(instance=ORDB4ORA::ANSINumberType_strategy)
def test_ordb4ora::ansinumbertype_Descriptor_setter(instance):
    original = instance.Descriptor
    instance.Descriptor = original
    assert instance.Descriptor == original
