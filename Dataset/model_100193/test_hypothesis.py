import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DerivedTable,
    BaseTable,
    SQL2003::evo::TriggerDescriptor,
    SQL2003::evo::TypedTable,
    SQL2003::evo::View,
    SQL2003::evo::Restriction,
    TableConstraint,
    SQL2003::evo::UniqueConstraint,
    SQL2003::evo::TableCheckConstraint,
    SQL2003::evo::ReferentialConstraint,
    SQL2003::evo::StructuralComponent,
    UniqueConstraint,
    SQL2003::evo::PrimaryKey,
    SQL2003::evo::Parameter,
    ColumnConstraint,
    SQL2003::evo::NotNull,
    Parameter,
    SQL2003::evo::MethodParameter,
    SQL2003::evo::Method,
    SQL2003::evo::Feature,
    UserDefinedType,
    SQL2003::evo::DistinctType,
    BehaviouralComponent,
    SQL2003::evo::Procedure,
    SQL2003::evo::Function,
    Feature,
    SQL2003::evo::StringFeature,
    SQL2003::evo::IntervalFeature,
    SQL2003::evo::NumericFeature,
    SQL2003::evo::DatetimeFeature,
    DataType,
    SQL2003::evo::PredefinedType,
    SQL2003::evo::UserDefinedType,
    SQL2003::evo::ConstructedType,
    Restriction,
    SQL2003::evo::TableConstraint,
    SQL2003::evo::Trigger,
    SQL2003::evo::ColumnConstraint,
    SQL2003::evo::DataType,
    ConstructedType,
    SQL2003::evo::ReferenceType,
    SQL2003::evo::ROW,
    SQL2003::evo::CollectionType,
    SQL2003::evo::Table,
    PredefinedType,
    SQL2003::evo::IntervalType,
    SQL2003::evo::XMLType,
    SQL2003::evo::CharacterStringType,
    SQL2003::evo::DatetimeType,
    SQL2003::evo::NumericType,
    SQL2003::evo::BinaryStringType,
    SQL2003::evo::ParameterWithMode,
    SQL2003::evo::Schema,
    SQL2003::evo::BehaviouralComponent,
    Table,
    SQL2003::evo::DerivedTable,
    SQL2003::evo::BaseTable,
    SQL2003::evo::BooleanType,
    SQL2003::evo::StructuredType,
    StructuralComponent,
    SQL2003::evo::Column,
    SQL2003::evo::Field,
    SQL2003::evo::Attribute,
    CollectionType,
    SQL2003::evo::MULTISET,
    SQL2003::evo::ARRAY,
    TriggerEvent,
    NumericFeatures,
    CharacterStringTypes,
    DatetimeTypes,
    StringFeatures,
    MatchTypes,
    Unit,
    ReferentialAction,
    TriggerActionTime,
    DatetimeFeatures,
    IntervalTypes,
    Multiplier,
    NumericTypes,
    IntervalFeatures,
    NumericRadix,
    XMLTypes,
    BooleanTypes,
    ParameterMode,
    TriggerLevel,
    BinaryStringTypes,
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



def test_sql2003::evo::triggerdescriptor_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::TriggerDescriptor)


def test_sql2003::evo::triggerdescriptor_constructor_exists():
    assert callable(SQL2003::evo::TriggerDescriptor.__init__)


def test_sql2003::evo::triggerdescriptor_constructor_args():
    sig = inspect.signature(SQL2003::evo::TriggerDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "triggeredAction" in params, "Missing parameter 'triggeredAction'"
    assert "level" in params, "Missing parameter 'level'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"

def test_sql2003::evo::triggerdescriptor_has_event():
    assert hasattr(SQL2003::evo::TriggerDescriptor, "event")
    descriptor = None
    for klass in SQL2003::evo::TriggerDescriptor.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::triggerdescriptor_has_triggeredAction():
    assert hasattr(SQL2003::evo::TriggerDescriptor, "triggeredAction")
    descriptor = None
    for klass in SQL2003::evo::TriggerDescriptor.__mro__:
        if "triggeredAction" in klass.__dict__:
            descriptor = klass.__dict__["triggeredAction"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::triggerdescriptor_has_level():
    assert hasattr(SQL2003::evo::TriggerDescriptor, "level")
    descriptor = None
    for klass in SQL2003::evo::TriggerDescriptor.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::triggerdescriptor_has_actionTime():
    assert hasattr(SQL2003::evo::TriggerDescriptor, "actionTime")
    descriptor = None
    for klass in SQL2003::evo::TriggerDescriptor.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::typedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::TypedTable)


def test_sql2003::evo::typedtable_constructor_exists():
    assert callable(SQL2003::evo::TypedTable.__init__)


def test_sql2003::evo::typedtable_constructor_args():
    sig = inspect.signature(SQL2003::evo::TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::view_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::View)


def test_sql2003::evo::view_constructor_exists():
    assert callable(SQL2003::evo::View.__init__)


def test_sql2003::evo::view_constructor_args():
    sig = inspect.signature(SQL2003::evo::View.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::restriction_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Restriction)


def test_sql2003::evo::restriction_constructor_exists():
    assert callable(SQL2003::evo::Restriction.__init__)


def test_sql2003::evo::restriction_constructor_args():
    sig = inspect.signature(SQL2003::evo::Restriction.__init__)
    params = list(sig.parameters.keys())



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::UniqueConstraint)


def test_sql2003::evo::uniqueconstraint_constructor_exists():
    assert callable(SQL2003::evo::UniqueConstraint.__init__)


def test_sql2003::evo::uniqueconstraint_constructor_args():
    sig = inspect.signature(SQL2003::evo::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::tablecheckconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::TableCheckConstraint)


def test_sql2003::evo::tablecheckconstraint_constructor_exists():
    assert callable(SQL2003::evo::TableCheckConstraint.__init__)


def test_sql2003::evo::tablecheckconstraint_constructor_args():
    sig = inspect.signature(SQL2003::evo::TableCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sql2003::evo::tablecheckconstraint_has_expression():
    assert hasattr(SQL2003::evo::TableCheckConstraint, "expression")
    descriptor = None
    for klass in SQL2003::evo::TableCheckConstraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ReferentialConstraint)


def test_sql2003::evo::referentialconstraint_constructor_exists():
    assert callable(SQL2003::evo::ReferentialConstraint.__init__)


def test_sql2003::evo::referentialconstraint_constructor_args():
    sig = inspect.signature(SQL2003::evo::ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "match" in params, "Missing parameter 'match'"
    assert "delete_action" in params, "Missing parameter 'delete_action'"
    assert "update_action" in params, "Missing parameter 'update_action'"

def test_sql2003::evo::referentialconstraint_has_match():
    assert hasattr(SQL2003::evo::ReferentialConstraint, "match")
    descriptor = None
    for klass in SQL2003::evo::ReferentialConstraint.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::referentialconstraint_has_delete_action():
    assert hasattr(SQL2003::evo::ReferentialConstraint, "delete_action")
    descriptor = None
    for klass in SQL2003::evo::ReferentialConstraint.__mro__:
        if "delete_action" in klass.__dict__:
            descriptor = klass.__dict__["delete_action"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::referentialconstraint_has_update_action():
    assert hasattr(SQL2003::evo::ReferentialConstraint, "update_action")
    descriptor = None
    for klass in SQL2003::evo::ReferentialConstraint.__mro__:
        if "update_action" in klass.__dict__:
            descriptor = klass.__dict__["update_action"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::StructuralComponent)


def test_sql2003::evo::structuralcomponent_constructor_exists():
    assert callable(SQL2003::evo::StructuralComponent.__init__)


def test_sql2003::evo::structuralcomponent_constructor_args():
    sig = inspect.signature(SQL2003::evo::StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::structuralcomponent_has_name():
    assert hasattr(SQL2003::evo::StructuralComponent, "name")
    descriptor = None
    for klass in SQL2003::evo::StructuralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::primarykey_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::PrimaryKey)


def test_sql2003::evo::primarykey_constructor_exists():
    assert callable(SQL2003::evo::PrimaryKey.__init__)


def test_sql2003::evo::primarykey_constructor_args():
    sig = inspect.signature(SQL2003::evo::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::parameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Parameter)


def test_sql2003::evo::parameter_constructor_exists():
    assert callable(SQL2003::evo::Parameter.__init__)


def test_sql2003::evo::parameter_constructor_args():
    sig = inspect.signature(SQL2003::evo::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::parameter_has_name():
    assert hasattr(SQL2003::evo::Parameter, "name")
    descriptor = None
    for klass in SQL2003::evo::Parameter.__mro__:
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



def test_sql2003::evo::notnull_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::NotNull)


def test_sql2003::evo::notnull_constructor_exists():
    assert callable(SQL2003::evo::NotNull.__init__)


def test_sql2003::evo::notnull_constructor_args():
    sig = inspect.signature(SQL2003::evo::NotNull.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::methodparameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::MethodParameter)


def test_sql2003::evo::methodparameter_constructor_exists():
    assert callable(SQL2003::evo::MethodParameter.__init__)


def test_sql2003::evo::methodparameter_constructor_args():
    sig = inspect.signature(SQL2003::evo::MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::method_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Method)


def test_sql2003::evo::method_constructor_exists():
    assert callable(SQL2003::evo::Method.__init__)


def test_sql2003::evo::method_constructor_args():
    sig = inspect.signature(SQL2003::evo::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003::evo::method_has_name():
    assert hasattr(SQL2003::evo::Method, "name")
    descriptor = None
    for klass in SQL2003::evo::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::method_has_body():
    assert hasattr(SQL2003::evo::Method, "body")
    descriptor = None
    for klass in SQL2003::evo::Method.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::feature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Feature)


def test_sql2003::evo::feature_constructor_exists():
    assert callable(SQL2003::evo::Feature.__init__)


def test_sql2003::evo::feature_constructor_args():
    sig = inspect.signature(SQL2003::evo::Feature.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::distincttype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::DistinctType)


def test_sql2003::evo::distincttype_constructor_exists():
    assert callable(SQL2003::evo::DistinctType.__init__)


def test_sql2003::evo::distincttype_constructor_args():
    sig = inspect.signature(SQL2003::evo::DistinctType.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(BehaviouralComponent)


def test_behaviouralcomponent_constructor_exists():
    assert callable(BehaviouralComponent.__init__)


def test_behaviouralcomponent_constructor_args():
    sig = inspect.signature(BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::procedure_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Procedure)


def test_sql2003::evo::procedure_constructor_exists():
    assert callable(SQL2003::evo::Procedure.__init__)


def test_sql2003::evo::procedure_constructor_args():
    sig = inspect.signature(SQL2003::evo::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::function_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Function)


def test_sql2003::evo::function_constructor_exists():
    assert callable(SQL2003::evo::Function.__init__)


def test_sql2003::evo::function_constructor_args():
    sig = inspect.signature(SQL2003::evo::Function.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::stringfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::StringFeature)


def test_sql2003::evo::stringfeature_constructor_exists():
    assert callable(SQL2003::evo::StringFeature.__init__)


def test_sql2003::evo::stringfeature_constructor_args():
    sig = inspect.signature(SQL2003::evo::StringFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003::evo::stringfeature_has_value():
    assert hasattr(SQL2003::evo::StringFeature, "value")
    descriptor = None
    for klass in SQL2003::evo::StringFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::stringfeature_has_key():
    assert hasattr(SQL2003::evo::StringFeature, "key")
    descriptor = None
    for klass in SQL2003::evo::StringFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::intervalfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::IntervalFeature)


def test_sql2003::evo::intervalfeature_constructor_exists():
    assert callable(SQL2003::evo::IntervalFeature.__init__)


def test_sql2003::evo::intervalfeature_constructor_args():
    sig = inspect.signature(SQL2003::evo::IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003::evo::intervalfeature_has_value():
    assert hasattr(SQL2003::evo::IntervalFeature, "value")
    descriptor = None
    for klass in SQL2003::evo::IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::intervalfeature_has_key():
    assert hasattr(SQL2003::evo::IntervalFeature, "key")
    descriptor = None
    for klass in SQL2003::evo::IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::numericfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::NumericFeature)


def test_sql2003::evo::numericfeature_constructor_exists():
    assert callable(SQL2003::evo::NumericFeature.__init__)


def test_sql2003::evo::numericfeature_constructor_args():
    sig = inspect.signature(SQL2003::evo::NumericFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003::evo::numericfeature_has_value():
    assert hasattr(SQL2003::evo::NumericFeature, "value")
    descriptor = None
    for klass in SQL2003::evo::NumericFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::numericfeature_has_key():
    assert hasattr(SQL2003::evo::NumericFeature, "key")
    descriptor = None
    for klass in SQL2003::evo::NumericFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::datetimefeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::DatetimeFeature)


def test_sql2003::evo::datetimefeature_constructor_exists():
    assert callable(SQL2003::evo::DatetimeFeature.__init__)


def test_sql2003::evo::datetimefeature_constructor_args():
    sig = inspect.signature(SQL2003::evo::DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003::evo::datetimefeature_has_key():
    assert hasattr(SQL2003::evo::DatetimeFeature, "key")
    descriptor = None
    for klass in SQL2003::evo::DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::datetimefeature_has_value():
    assert hasattr(SQL2003::evo::DatetimeFeature, "value")
    descriptor = None
    for klass in SQL2003::evo::DatetimeFeature.__mro__:
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



def test_sql2003::evo::predefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::PredefinedType)


def test_sql2003::evo::predefinedtype_constructor_exists():
    assert callable(SQL2003::evo::PredefinedType.__init__)


def test_sql2003::evo::predefinedtype_constructor_args():
    sig = inspect.signature(SQL2003::evo::PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::UserDefinedType)


def test_sql2003::evo::userdefinedtype_constructor_exists():
    assert callable(SQL2003::evo::UserDefinedType.__init__)


def test_sql2003::evo::userdefinedtype_constructor_args():
    sig = inspect.signature(SQL2003::evo::UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::userdefinedtype_has_name():
    assert hasattr(SQL2003::evo::UserDefinedType, "name")
    descriptor = None
    for klass in SQL2003::evo::UserDefinedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::constructedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ConstructedType)


def test_sql2003::evo::constructedtype_constructor_exists():
    assert callable(SQL2003::evo::ConstructedType.__init__)


def test_sql2003::evo::constructedtype_constructor_args():
    sig = inspect.signature(SQL2003::evo::ConstructedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::constructedtype_has_name():
    assert hasattr(SQL2003::evo::ConstructedType, "name")
    descriptor = None
    for klass in SQL2003::evo::ConstructedType.__mro__:
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



def test_sql2003::evo::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::TableConstraint)


def test_sql2003::evo::tableconstraint_constructor_exists():
    assert callable(SQL2003::evo::TableConstraint.__init__)


def test_sql2003::evo::tableconstraint_constructor_args():
    sig = inspect.signature(SQL2003::evo::TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::tableconstraint_has_name():
    assert hasattr(SQL2003::evo::TableConstraint, "name")
    descriptor = None
    for klass in SQL2003::evo::TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::trigger_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Trigger)


def test_sql2003::evo::trigger_constructor_exists():
    assert callable(SQL2003::evo::Trigger.__init__)


def test_sql2003::evo::trigger_constructor_args():
    sig = inspect.signature(SQL2003::evo::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::trigger_has_name():
    assert hasattr(SQL2003::evo::Trigger, "name")
    descriptor = None
    for klass in SQL2003::evo::Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::columnconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ColumnConstraint)


def test_sql2003::evo::columnconstraint_constructor_exists():
    assert callable(SQL2003::evo::ColumnConstraint.__init__)


def test_sql2003::evo::columnconstraint_constructor_args():
    sig = inspect.signature(SQL2003::evo::ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::datatype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::DataType)


def test_sql2003::evo::datatype_constructor_exists():
    assert callable(SQL2003::evo::DataType.__init__)


def test_sql2003::evo::datatype_constructor_args():
    sig = inspect.signature(SQL2003::evo::DataType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::referencetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ReferenceType)


def test_sql2003::evo::referencetype_constructor_exists():
    assert callable(SQL2003::evo::ReferenceType.__init__)


def test_sql2003::evo::referencetype_constructor_args():
    sig = inspect.signature(SQL2003::evo::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::row_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ROW)


def test_sql2003::evo::row_constructor_exists():
    assert callable(SQL2003::evo::ROW.__init__)


def test_sql2003::evo::row_constructor_args():
    sig = inspect.signature(SQL2003::evo::ROW.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::collectiontype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::CollectionType)


def test_sql2003::evo::collectiontype_constructor_exists():
    assert callable(SQL2003::evo::CollectionType.__init__)


def test_sql2003::evo::collectiontype_constructor_args():
    sig = inspect.signature(SQL2003::evo::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::table_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Table)


def test_sql2003::evo::table_constructor_exists():
    assert callable(SQL2003::evo::Table.__init__)


def test_sql2003::evo::table_constructor_args():
    sig = inspect.signature(SQL2003::evo::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::table_has_name():
    assert hasattr(SQL2003::evo::Table, "name")
    descriptor = None
    for klass in SQL2003::evo::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::intervaltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::IntervalType)


def test_sql2003::evo::intervaltype_constructor_exists():
    assert callable(SQL2003::evo::IntervalType.__init__)


def test_sql2003::evo::intervaltype_constructor_args():
    sig = inspect.signature(SQL2003::evo::IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::evo::intervaltype_has_descriptor():
    assert hasattr(SQL2003::evo::IntervalType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::IntervalType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::xmltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::XMLType)


def test_sql2003::evo::xmltype_constructor_exists():
    assert callable(SQL2003::evo::XMLType.__init__)


def test_sql2003::evo::xmltype_constructor_args():
    sig = inspect.signature(SQL2003::evo::XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::evo::xmltype_has_descriptor():
    assert hasattr(SQL2003::evo::XMLType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::XMLType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::characterstringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::CharacterStringType)


def test_sql2003::evo::characterstringtype_constructor_exists():
    assert callable(SQL2003::evo::CharacterStringType.__init__)


def test_sql2003::evo::characterstringtype_constructor_args():
    sig = inspect.signature(SQL2003::evo::CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "length_def" in params, "Missing parameter 'length_def'"

def test_sql2003::evo::characterstringtype_has_descriptor():
    assert hasattr(SQL2003::evo::CharacterStringType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::CharacterStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::characterstringtype_has_length_def():
    assert hasattr(SQL2003::evo::CharacterStringType, "length_def")
    descriptor = None
    for klass in SQL2003::evo::CharacterStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::DatetimeType)


def test_sql2003::evo::datetimetype_constructor_exists():
    assert callable(SQL2003::evo::DatetimeType.__init__)


def test_sql2003::evo::datetimetype_constructor_args():
    sig = inspect.signature(SQL2003::evo::DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::evo::datetimetype_has_descriptor():
    assert hasattr(SQL2003::evo::DatetimeType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::DatetimeType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::numerictype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::NumericType)


def test_sql2003::evo::numerictype_constructor_exists():
    assert callable(SQL2003::evo::NumericType.__init__)


def test_sql2003::evo::numerictype_constructor_args():
    sig = inspect.signature(SQL2003::evo::NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::evo::numerictype_has_descriptor():
    assert hasattr(SQL2003::evo::NumericType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::NumericType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::binarystringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::BinaryStringType)


def test_sql2003::evo::binarystringtype_constructor_exists():
    assert callable(SQL2003::evo::BinaryStringType.__init__)


def test_sql2003::evo::binarystringtype_constructor_args():
    sig = inspect.signature(SQL2003::evo::BinaryStringType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "length_def" in params, "Missing parameter 'length_def'"

def test_sql2003::evo::binarystringtype_has_descriptor():
    assert hasattr(SQL2003::evo::BinaryStringType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::BinaryStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::binarystringtype_has_length_def():
    assert hasattr(SQL2003::evo::BinaryStringType, "length_def")
    descriptor = None
    for klass in SQL2003::evo::BinaryStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::parameterwithmode_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ParameterWithMode)


def test_sql2003::evo::parameterwithmode_constructor_exists():
    assert callable(SQL2003::evo::ParameterWithMode.__init__)


def test_sql2003::evo::parameterwithmode_constructor_args():
    sig = inspect.signature(SQL2003::evo::ParameterWithMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sql2003::evo::parameterwithmode_has_mode():
    assert hasattr(SQL2003::evo::ParameterWithMode, "mode")
    descriptor = None
    for klass in SQL2003::evo::ParameterWithMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::schema_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Schema)


def test_sql2003::evo::schema_constructor_exists():
    assert callable(SQL2003::evo::Schema.__init__)


def test_sql2003::evo::schema_constructor_args():
    sig = inspect.signature(SQL2003::evo::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::evo::schema_has_name():
    assert hasattr(SQL2003::evo::Schema, "name")
    descriptor = None
    for klass in SQL2003::evo::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::BehaviouralComponent)


def test_sql2003::evo::behaviouralcomponent_constructor_exists():
    assert callable(SQL2003::evo::BehaviouralComponent.__init__)


def test_sql2003::evo::behaviouralcomponent_constructor_args():
    sig = inspect.signature(SQL2003::evo::BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003::evo::behaviouralcomponent_has_name():
    assert hasattr(SQL2003::evo::BehaviouralComponent, "name")
    descriptor = None
    for klass in SQL2003::evo::BehaviouralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::behaviouralcomponent_has_body():
    assert hasattr(SQL2003::evo::BehaviouralComponent, "body")
    descriptor = None
    for klass in SQL2003::evo::BehaviouralComponent.__mro__:
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



def test_sql2003::evo::derivedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::DerivedTable)


def test_sql2003::evo::derivedtable_constructor_exists():
    assert callable(SQL2003::evo::DerivedTable.__init__)


def test_sql2003::evo::derivedtable_constructor_args():
    sig = inspect.signature(SQL2003::evo::DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_sql2003::evo::derivedtable_has_query_expression():
    assert hasattr(SQL2003::evo::DerivedTable, "query_expression")
    descriptor = None
    for klass in SQL2003::evo::DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::basetable_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::BaseTable)


def test_sql2003::evo::basetable_constructor_exists():
    assert callable(SQL2003::evo::BaseTable.__init__)


def test_sql2003::evo::basetable_constructor_args():
    sig = inspect.signature(SQL2003::evo::BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::booleantype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::BooleanType)


def test_sql2003::evo::booleantype_constructor_exists():
    assert callable(SQL2003::evo::BooleanType.__init__)


def test_sql2003::evo::booleantype_constructor_args():
    sig = inspect.signature(SQL2003::evo::BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::evo::booleantype_has_descriptor():
    assert hasattr(SQL2003::evo::BooleanType, "descriptor")
    descriptor = None
    for klass in SQL2003::evo::BooleanType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::structuredtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::StructuredType)


def test_sql2003::evo::structuredtype_constructor_exists():
    assert callable(SQL2003::evo::StructuredType.__init__)


def test_sql2003::evo::structuredtype_constructor_args():
    sig = inspect.signature(SQL2003::evo::StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"
    assert "is_final" in params, "Missing parameter 'is_final'"

def test_sql2003::evo::structuredtype_has_is_instantiable():
    assert hasattr(SQL2003::evo::StructuredType, "is_instantiable")
    descriptor = None
    for klass in SQL2003::evo::StructuredType.__mro__:
        if "is_instantiable" in klass.__dict__:
            descriptor = klass.__dict__["is_instantiable"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::evo::structuredtype_has_is_final():
    assert hasattr(SQL2003::evo::StructuredType, "is_final")
    descriptor = None
    for klass in SQL2003::evo::StructuredType.__mro__:
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



def test_sql2003::evo::column_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Column)


def test_sql2003::evo::column_constructor_exists():
    assert callable(SQL2003::evo::Column.__init__)


def test_sql2003::evo::column_constructor_args():
    sig = inspect.signature(SQL2003::evo::Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003::evo::column_has_default():
    assert hasattr(SQL2003::evo::Column, "default")
    descriptor = None
    for klass in SQL2003::evo::Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::evo::field_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Field)


def test_sql2003::evo::field_constructor_exists():
    assert callable(SQL2003::evo::Field.__init__)


def test_sql2003::evo::field_constructor_args():
    sig = inspect.signature(SQL2003::evo::Field.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::attribute_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::Attribute)


def test_sql2003::evo::attribute_constructor_exists():
    assert callable(SQL2003::evo::Attribute.__init__)


def test_sql2003::evo::attribute_constructor_args():
    sig = inspect.signature(SQL2003::evo::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003::evo::attribute_has_default():
    assert hasattr(SQL2003::evo::Attribute, "default")
    descriptor = None
    for klass in SQL2003::evo::Attribute.__mro__:
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



def test_sql2003::evo::multiset_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::MULTISET)


def test_sql2003::evo::multiset_constructor_exists():
    assert callable(SQL2003::evo::MULTISET.__init__)


def test_sql2003::evo::multiset_constructor_args():
    sig = inspect.signature(SQL2003::evo::MULTISET.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::evo::array_is_not_abstract():
    assert not inspect.isabstract(SQL2003::evo::ARRAY)


def test_sql2003::evo::array_constructor_exists():
    assert callable(SQL2003::evo::ARRAY.__init__)


def test_sql2003::evo::array_constructor_args():
    sig = inspect.signature(SQL2003::evo::ARRAY.__init__)
    params = list(sig.parameters.keys())
    assert "num_elements" in params, "Missing parameter 'num_elements'"

def test_sql2003::evo::array_has_num_elements():
    assert hasattr(SQL2003::evo::ARRAY, "num_elements")
    descriptor = None
    for klass in SQL2003::evo::ARRAY.__mro__:
        if "num_elements" in klass.__dict__:
            descriptor = klass.__dict__["num_elements"]
            break
    assert isinstance(descriptor, property)

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

def test_numericfeatures_exists():
    # Check that the Enumeration exists
    assert NumericFeatures is not None

def test_numericfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericFeatures]
    expected_literals = [
        "precision",
        "radix",
        "scale",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericFeatures"

def test_characterstringtypes_exists():
    # Check that the Enumeration exists
    assert CharacterStringTypes is not None

def test_characterstringtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CharacterStringTypes]
    expected_literals = [
        "CHARACTERVARYING",
        "CHARACTERLARGEOBJECT",
        "CHARACTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CharacterStringTypes"

def test_datetimetypes_exists():
    # Check that the Enumeration exists
    assert DatetimeTypes is not None

def test_datetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeTypes]
    expected_literals = [
        "TIMESTAMPWITHOUTTIMEZONE",
        "DATE",
        "TIMEWITHOUTTIMEZONE",
        "TIMESTAMPWITHTIMEZONE",
        "TIMEWITHTIMEZONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeTypes"

def test_stringfeatures_exists():
    # Check that the Enumeration exists
    assert StringFeatures is not None

def test_stringfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringFeatures]
    expected_literals = [
        "multiplier",
        "length",
        "unit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringFeatures"

def test_matchtypes_exists():
    # Check that the Enumeration exists
    assert MatchTypes is not None

def test_matchtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatchTypes]
    expected_literals = [
        "PARTIAL",
        "TOTAL",
        "SIMPLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchTypes"

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

def test_referentialaction_exists():
    # Check that the Enumeration exists
    assert ReferentialAction is not None

def test_referentialaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialAction]
    expected_literals = [
        "NO_ACTION",
        "SET_NULL",
        "SET_DEFAULT",
        "CASCADE",
        "RESTRICT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialAction"

def test_triggeractiontime_exists():
    # Check that the Enumeration exists
    assert TriggerActionTime is not None

def test_triggeractiontime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerActionTime]
    expected_literals = [
        "AFTER",
        "BEFORE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerActionTime"

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

def test_intervaltypes_exists():
    # Check that the Enumeration exists
    assert IntervalTypes is not None

def test_intervaltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalTypes]
    expected_literals = [
        "MINUTE_SECOND",
        "HOUR_SECOND",
        "HOUR",
        "DAY_MINUTE",
        "SECOND",
        "MINUTE",
        "MONTH",
        "DAY_HOUR",
        "YEAR_MONTH",
        "DAY",
        "HOUR_MINUTE",
        "YEAR",
        "DAY_SECOND",
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
        "M",
        "K",
        "T",
        "P",
        "G",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_numerictypes_exists():
    # Check that the Enumeration exists
    assert NumericTypes is not None

def test_numerictypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericTypes]
    expected_literals = [
        "DOUBLEPRECISION",
        "FLOAT",
        "SMALLINT",
        "DECIMAL",
        "BIGINT",
        "INTEGER",
        "NUMERIC",
        "REAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericTypes"

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
SQL2003::evo::TriggerDescriptor_strategy = st.builds(
    SQL2003::evo::TriggerDescriptor,
    event=
        safe_text,
    triggeredAction=
        safe_text,
    level=
        safe_text,
    actionTime=
        safe_text
)
SQL2003::evo::TypedTable_strategy = st.builds(
    SQL2003::evo::TypedTable,
)
SQL2003::evo::View_strategy = st.builds(
    SQL2003::evo::View,
)
SQL2003::evo::Restriction_strategy = st.builds(
    SQL2003::evo::Restriction,
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
SQL2003::evo::UniqueConstraint_strategy = st.builds(
    SQL2003::evo::UniqueConstraint,
)
SQL2003::evo::TableCheckConstraint_strategy = st.builds(
    SQL2003::evo::TableCheckConstraint,
    expression=
        safe_text
)
SQL2003::evo::ReferentialConstraint_strategy = st.builds(
    SQL2003::evo::ReferentialConstraint,
    match=
        safe_text,
    delete_action=
        safe_text,
    update_action=
        safe_text
)
SQL2003::evo::StructuralComponent_strategy = st.builds(
    SQL2003::evo::StructuralComponent,
    name=
        safe_text
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
SQL2003::evo::PrimaryKey_strategy = st.builds(
    SQL2003::evo::PrimaryKey,
)
SQL2003::evo::Parameter_strategy = st.builds(
    SQL2003::evo::Parameter,
    name=
        safe_text
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
SQL2003::evo::NotNull_strategy = st.builds(
    SQL2003::evo::NotNull,
)
Parameter_strategy = st.builds(
    Parameter,
)
SQL2003::evo::MethodParameter_strategy = st.builds(
    SQL2003::evo::MethodParameter,
)
SQL2003::evo::Method_strategy = st.builds(
    SQL2003::evo::Method,
    name=
        safe_text,
    body=
        safe_text
)
SQL2003::evo::Feature_strategy = st.builds(
    SQL2003::evo::Feature,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
SQL2003::evo::DistinctType_strategy = st.builds(
    SQL2003::evo::DistinctType,
)
BehaviouralComponent_strategy = st.builds(
    BehaviouralComponent,
)
SQL2003::evo::Procedure_strategy = st.builds(
    SQL2003::evo::Procedure,
)
SQL2003::evo::Function_strategy = st.builds(
    SQL2003::evo::Function,
)
Feature_strategy = st.builds(
    Feature,
)
SQL2003::evo::StringFeature_strategy = st.builds(
    SQL2003::evo::StringFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003::evo::IntervalFeature_strategy = st.builds(
    SQL2003::evo::IntervalFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003::evo::NumericFeature_strategy = st.builds(
    SQL2003::evo::NumericFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003::evo::DatetimeFeature_strategy = st.builds(
    SQL2003::evo::DatetimeFeature,
    key=
        safe_text,
    value=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
SQL2003::evo::PredefinedType_strategy = st.builds(
    SQL2003::evo::PredefinedType,
)
SQL2003::evo::UserDefinedType_strategy = st.builds(
    SQL2003::evo::UserDefinedType,
    name=
        safe_text
)
SQL2003::evo::ConstructedType_strategy = st.builds(
    SQL2003::evo::ConstructedType,
    name=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
SQL2003::evo::TableConstraint_strategy = st.builds(
    SQL2003::evo::TableConstraint,
    name=
        safe_text
)
SQL2003::evo::Trigger_strategy = st.builds(
    SQL2003::evo::Trigger,
    name=
        safe_text
)
SQL2003::evo::ColumnConstraint_strategy = st.builds(
    SQL2003::evo::ColumnConstraint,
)
SQL2003::evo::DataType_strategy = st.builds(
    SQL2003::evo::DataType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
SQL2003::evo::ReferenceType_strategy = st.builds(
    SQL2003::evo::ReferenceType,
)
SQL2003::evo::ROW_strategy = st.builds(
    SQL2003::evo::ROW,
)
SQL2003::evo::CollectionType_strategy = st.builds(
    SQL2003::evo::CollectionType,
)
SQL2003::evo::Table_strategy = st.builds(
    SQL2003::evo::Table,
    name=
        safe_text
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
SQL2003::evo::IntervalType_strategy = st.builds(
    SQL2003::evo::IntervalType,
    descriptor=
        safe_text
)
SQL2003::evo::XMLType_strategy = st.builds(
    SQL2003::evo::XMLType,
    descriptor=
        safe_text
)
SQL2003::evo::CharacterStringType_strategy = st.builds(
    SQL2003::evo::CharacterStringType,
    descriptor=
        safe_text,
    length_def=
        safe_text
)
SQL2003::evo::DatetimeType_strategy = st.builds(
    SQL2003::evo::DatetimeType,
    descriptor=
        safe_text
)
SQL2003::evo::NumericType_strategy = st.builds(
    SQL2003::evo::NumericType,
    descriptor=
        safe_text
)
SQL2003::evo::BinaryStringType_strategy = st.builds(
    SQL2003::evo::BinaryStringType,
    descriptor=
        safe_text,
    length_def=
        safe_text
)
SQL2003::evo::ParameterWithMode_strategy = st.builds(
    SQL2003::evo::ParameterWithMode,
    mode=
        safe_text
)
SQL2003::evo::Schema_strategy = st.builds(
    SQL2003::evo::Schema,
    name=
        safe_text
)
SQL2003::evo::BehaviouralComponent_strategy = st.builds(
    SQL2003::evo::BehaviouralComponent,
    name=
        safe_text,
    body=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SQL2003::evo::DerivedTable_strategy = st.builds(
    SQL2003::evo::DerivedTable,
    query_expression=
        safe_text
)
SQL2003::evo::BaseTable_strategy = st.builds(
    SQL2003::evo::BaseTable,
)
SQL2003::evo::BooleanType_strategy = st.builds(
    SQL2003::evo::BooleanType,
    descriptor=
        safe_text
)
SQL2003::evo::StructuredType_strategy = st.builds(
    SQL2003::evo::StructuredType,
    is_instantiable=
        st.booleans(),
    is_final=
        st.booleans()
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
SQL2003::evo::Column_strategy = st.builds(
    SQL2003::evo::Column,
    default=
        safe_text
)
SQL2003::evo::Field_strategy = st.builds(
    SQL2003::evo::Field,
)
SQL2003::evo::Attribute_strategy = st.builds(
    SQL2003::evo::Attribute,
    default=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
SQL2003::evo::MULTISET_strategy = st.builds(
    SQL2003::evo::MULTISET,
)
SQL2003::evo::ARRAY_strategy = st.builds(
    SQL2003::evo::ARRAY,
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

@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
@settings(max_examples=50)
def test_sql2003::evo::triggerdescriptor_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::TriggerDescriptor)

@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_triggeredAction_type(instance):
    assert isinstance(instance.triggeredAction, str)


@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_triggeredAction_setter(instance):
    original = instance.triggeredAction
    instance.triggeredAction = original
    assert instance.triggeredAction == original

@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_actionTime_type(instance):
    assert isinstance(instance.actionTime, str)


@given(instance=SQL2003::evo::TriggerDescriptor_strategy)
def test_sql2003::evo::triggerdescriptor_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original

@given(instance=SQL2003::evo::TypedTable_strategy)
@settings(max_examples=50)
def test_sql2003::evo::typedtable_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::TypedTable)

@given(instance=SQL2003::evo::View_strategy)
@settings(max_examples=50)
def test_sql2003::evo::view_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::View)

@given(instance=SQL2003::evo::Restriction_strategy)
@settings(max_examples=50)
def test_sql2003::evo::restriction_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Restriction)

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=SQL2003::evo::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::evo::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::UniqueConstraint)

@given(instance=SQL2003::evo::TableCheckConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::evo::tablecheckconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::TableCheckConstraint)

@given(instance=SQL2003::evo::TableCheckConstraint_strategy)
def test_sql2003::evo::tablecheckconstraint_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=SQL2003::evo::TableCheckConstraint_strategy)
def test_sql2003::evo::tablecheckconstraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::evo::referentialconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ReferentialConstraint)

@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
def test_sql2003::evo::referentialconstraint_match_type(instance):
    assert isinstance(instance.match, str)


@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
def test_sql2003::evo::referentialconstraint_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original

@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
def test_sql2003::evo::referentialconstraint_delete_action_type(instance):
    assert isinstance(instance.delete_action, str)


@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
def test_sql2003::evo::referentialconstraint_delete_action_setter(instance):
    original = instance.delete_action
    instance.delete_action = original
    assert instance.delete_action == original

@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
def test_sql2003::evo::referentialconstraint_update_action_type(instance):
    assert isinstance(instance.update_action, str)


@given(instance=SQL2003::evo::ReferentialConstraint_strategy)
def test_sql2003::evo::referentialconstraint_update_action_setter(instance):
    original = instance.update_action
    instance.update_action = original
    assert instance.update_action == original

@given(instance=SQL2003::evo::StructuralComponent_strategy)
@settings(max_examples=50)
def test_sql2003::evo::structuralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::StructuralComponent)

@given(instance=SQL2003::evo::StructuralComponent_strategy)
def test_sql2003::evo::structuralcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::StructuralComponent_strategy)
def test_sql2003::evo::structuralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=SQL2003::evo::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql2003::evo::primarykey_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::PrimaryKey)

@given(instance=SQL2003::evo::Parameter_strategy)
@settings(max_examples=50)
def test_sql2003::evo::parameter_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Parameter)

@given(instance=SQL2003::evo::Parameter_strategy)
def test_sql2003::evo::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::Parameter_strategy)
def test_sql2003::evo::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=SQL2003::evo::NotNull_strategy)
@settings(max_examples=50)
def test_sql2003::evo::notnull_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::NotNull)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=SQL2003::evo::MethodParameter_strategy)
@settings(max_examples=50)
def test_sql2003::evo::methodparameter_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::MethodParameter)

@given(instance=SQL2003::evo::Method_strategy)
@settings(max_examples=50)
def test_sql2003::evo::method_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Method)

@given(instance=SQL2003::evo::Method_strategy)
def test_sql2003::evo::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::Method_strategy)
def test_sql2003::evo::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::evo::Method_strategy)
def test_sql2003::evo::method_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=SQL2003::evo::Method_strategy)
def test_sql2003::evo::method_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=SQL2003::evo::Feature_strategy)
@settings(max_examples=50)
def test_sql2003::evo::feature_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Feature)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=SQL2003::evo::DistinctType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::distincttype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::DistinctType)

@given(instance=BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, BehaviouralComponent)

@given(instance=SQL2003::evo::Procedure_strategy)
@settings(max_examples=50)
def test_sql2003::evo::procedure_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Procedure)

@given(instance=SQL2003::evo::Function_strategy)
@settings(max_examples=50)
def test_sql2003::evo::function_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Function)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=SQL2003::evo::StringFeature_strategy)
@settings(max_examples=50)
def test_sql2003::evo::stringfeature_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::StringFeature)

@given(instance=SQL2003::evo::StringFeature_strategy)
def test_sql2003::evo::stringfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::evo::StringFeature_strategy)
def test_sql2003::evo::stringfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::evo::StringFeature_strategy)
def test_sql2003::evo::stringfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::evo::StringFeature_strategy)
def test_sql2003::evo::stringfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::evo::IntervalFeature_strategy)
@settings(max_examples=50)
def test_sql2003::evo::intervalfeature_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::IntervalFeature)

@given(instance=SQL2003::evo::IntervalFeature_strategy)
def test_sql2003::evo::intervalfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::evo::IntervalFeature_strategy)
def test_sql2003::evo::intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::evo::IntervalFeature_strategy)
def test_sql2003::evo::intervalfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::evo::IntervalFeature_strategy)
def test_sql2003::evo::intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::evo::NumericFeature_strategy)
@settings(max_examples=50)
def test_sql2003::evo::numericfeature_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::NumericFeature)

@given(instance=SQL2003::evo::NumericFeature_strategy)
def test_sql2003::evo::numericfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::evo::NumericFeature_strategy)
def test_sql2003::evo::numericfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::evo::NumericFeature_strategy)
def test_sql2003::evo::numericfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::evo::NumericFeature_strategy)
def test_sql2003::evo::numericfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::evo::DatetimeFeature_strategy)
@settings(max_examples=50)
def test_sql2003::evo::datetimefeature_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::DatetimeFeature)

@given(instance=SQL2003::evo::DatetimeFeature_strategy)
def test_sql2003::evo::datetimefeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::evo::DatetimeFeature_strategy)
def test_sql2003::evo::datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::evo::DatetimeFeature_strategy)
def test_sql2003::evo::datetimefeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::evo::DatetimeFeature_strategy)
def test_sql2003::evo::datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=SQL2003::evo::PredefinedType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::predefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::PredefinedType)

@given(instance=SQL2003::evo::UserDefinedType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::userdefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::UserDefinedType)

@given(instance=SQL2003::evo::UserDefinedType_strategy)
def test_sql2003::evo::userdefinedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::UserDefinedType_strategy)
def test_sql2003::evo::userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::evo::ConstructedType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::constructedtype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ConstructedType)

@given(instance=SQL2003::evo::ConstructedType_strategy)
def test_sql2003::evo::constructedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::ConstructedType_strategy)
def test_sql2003::evo::constructedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=SQL2003::evo::TableConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::evo::tableconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::TableConstraint)

@given(instance=SQL2003::evo::TableConstraint_strategy)
def test_sql2003::evo::tableconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::TableConstraint_strategy)
def test_sql2003::evo::tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::evo::Trigger_strategy)
@settings(max_examples=50)
def test_sql2003::evo::trigger_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Trigger)

@given(instance=SQL2003::evo::Trigger_strategy)
def test_sql2003::evo::trigger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::Trigger_strategy)
def test_sql2003::evo::trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::evo::ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::evo::columnconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ColumnConstraint)

@given(instance=SQL2003::evo::DataType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::datatype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::DataType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=SQL2003::evo::ReferenceType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::referencetype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ReferenceType)

@given(instance=SQL2003::evo::ROW_strategy)
@settings(max_examples=50)
def test_sql2003::evo::row_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ROW)

@given(instance=SQL2003::evo::CollectionType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::collectiontype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::CollectionType)

@given(instance=SQL2003::evo::Table_strategy)
@settings(max_examples=50)
def test_sql2003::evo::table_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Table)

@given(instance=SQL2003::evo::Table_strategy)
def test_sql2003::evo::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::Table_strategy)
def test_sql2003::evo::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=SQL2003::evo::IntervalType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::intervaltype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::IntervalType)

@given(instance=SQL2003::evo::IntervalType_strategy)
def test_sql2003::evo::intervaltype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::IntervalType_strategy)
def test_sql2003::evo::intervaltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::XMLType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::xmltype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::XMLType)

@given(instance=SQL2003::evo::XMLType_strategy)
def test_sql2003::evo::xmltype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::XMLType_strategy)
def test_sql2003::evo::xmltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::characterstringtype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::CharacterStringType)

@given(instance=SQL2003::evo::CharacterStringType_strategy)
def test_sql2003::evo::characterstringtype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::CharacterStringType_strategy)
def test_sql2003::evo::characterstringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::CharacterStringType_strategy)
def test_sql2003::evo::characterstringtype_length_def_type(instance):
    assert isinstance(instance.length_def, str)


@given(instance=SQL2003::evo::CharacterStringType_strategy)
def test_sql2003::evo::characterstringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003::evo::DatetimeType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::datetimetype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::DatetimeType)

@given(instance=SQL2003::evo::DatetimeType_strategy)
def test_sql2003::evo::datetimetype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::DatetimeType_strategy)
def test_sql2003::evo::datetimetype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::NumericType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::numerictype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::NumericType)

@given(instance=SQL2003::evo::NumericType_strategy)
def test_sql2003::evo::numerictype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::NumericType_strategy)
def test_sql2003::evo::numerictype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::BinaryStringType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::binarystringtype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::BinaryStringType)

@given(instance=SQL2003::evo::BinaryStringType_strategy)
def test_sql2003::evo::binarystringtype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::BinaryStringType_strategy)
def test_sql2003::evo::binarystringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::BinaryStringType_strategy)
def test_sql2003::evo::binarystringtype_length_def_type(instance):
    assert isinstance(instance.length_def, str)


@given(instance=SQL2003::evo::BinaryStringType_strategy)
def test_sql2003::evo::binarystringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003::evo::ParameterWithMode_strategy)
@settings(max_examples=50)
def test_sql2003::evo::parameterwithmode_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ParameterWithMode)

@given(instance=SQL2003::evo::ParameterWithMode_strategy)
def test_sql2003::evo::parameterwithmode_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=SQL2003::evo::ParameterWithMode_strategy)
def test_sql2003::evo::parameterwithmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SQL2003::evo::Schema_strategy)
@settings(max_examples=50)
def test_sql2003::evo::schema_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Schema)

@given(instance=SQL2003::evo::Schema_strategy)
def test_sql2003::evo::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::Schema_strategy)
def test_sql2003::evo::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::evo::BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_sql2003::evo::behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::BehaviouralComponent)

@given(instance=SQL2003::evo::BehaviouralComponent_strategy)
def test_sql2003::evo::behaviouralcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::evo::BehaviouralComponent_strategy)
def test_sql2003::evo::behaviouralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::evo::BehaviouralComponent_strategy)
def test_sql2003::evo::behaviouralcomponent_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=SQL2003::evo::BehaviouralComponent_strategy)
def test_sql2003::evo::behaviouralcomponent_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SQL2003::evo::DerivedTable_strategy)
@settings(max_examples=50)
def test_sql2003::evo::derivedtable_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::DerivedTable)

@given(instance=SQL2003::evo::DerivedTable_strategy)
def test_sql2003::evo::derivedtable_query_expression_type(instance):
    assert isinstance(instance.query_expression, str)


@given(instance=SQL2003::evo::DerivedTable_strategy)
def test_sql2003::evo::derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=SQL2003::evo::BaseTable_strategy)
@settings(max_examples=50)
def test_sql2003::evo::basetable_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::BaseTable)

@given(instance=SQL2003::evo::BooleanType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::booleantype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::BooleanType)

@given(instance=SQL2003::evo::BooleanType_strategy)
def test_sql2003::evo::booleantype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::evo::BooleanType_strategy)
def test_sql2003::evo::booleantype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::evo::StructuredType_strategy)
@settings(max_examples=50)
def test_sql2003::evo::structuredtype_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::StructuredType)

@given(instance=SQL2003::evo::StructuredType_strategy)
def test_sql2003::evo::structuredtype_is_instantiable_type(instance):
    assert isinstance(instance.is_instantiable, bool)


@given(instance=SQL2003::evo::StructuredType_strategy)
def test_sql2003::evo::structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original

@given(instance=SQL2003::evo::StructuredType_strategy)
def test_sql2003::evo::structuredtype_is_final_type(instance):
    assert isinstance(instance.is_final, bool)


@given(instance=SQL2003::evo::StructuredType_strategy)
def test_sql2003::evo::structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=SQL2003::evo::Column_strategy)
@settings(max_examples=50)
def test_sql2003::evo::column_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Column)

@given(instance=SQL2003::evo::Column_strategy)
def test_sql2003::evo::column_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=SQL2003::evo::Column_strategy)
def test_sql2003::evo::column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=SQL2003::evo::Field_strategy)
@settings(max_examples=50)
def test_sql2003::evo::field_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Field)

@given(instance=SQL2003::evo::Attribute_strategy)
@settings(max_examples=50)
def test_sql2003::evo::attribute_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::Attribute)

@given(instance=SQL2003::evo::Attribute_strategy)
def test_sql2003::evo::attribute_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=SQL2003::evo::Attribute_strategy)
def test_sql2003::evo::attribute_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=SQL2003::evo::MULTISET_strategy)
@settings(max_examples=50)
def test_sql2003::evo::multiset_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::MULTISET)

@given(instance=SQL2003::evo::ARRAY_strategy)
@settings(max_examples=50)
def test_sql2003::evo::array_instantiation(instance):
    assert isinstance(instance, SQL2003::evo::ARRAY)

@given(instance=SQL2003::evo::ARRAY_strategy)
def test_sql2003::evo::array_num_elements_type(instance):
    assert isinstance(instance.num_elements, str)


@given(instance=SQL2003::evo::ARRAY_strategy)
def test_sql2003::evo::array_num_elements_setter(instance):
    original = instance.num_elements
    instance.num_elements = original
    assert instance.num_elements == original
