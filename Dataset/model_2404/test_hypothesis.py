import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DerivedTable,
    BaseTable,
    SQL2003::Trigger,
    SQL2003::TypedTable,
    SQL2003::View,
    SQL2003::StructuralComponent,
    SQL2003::Restriction,
    TableConstraint,
    SQL2003::UniqueConstraint,
    SQL2003::TableCheckConstraint,
    SQL2003::ReferentialConstraint,
    UniqueConstraint,
    SQL2003::PrimaryKey,
    SQL2003::Parameter,
    Parameter,
    SQL2003::MethodParameter,
    ColumnConstraint,
    SQL2003::NotNull,
    SQL2003::Method,
    SQL2003::Feature,
    UserDefinedType,
    SQL2003::DistinctType,
    BehaviouralComponent,
    SQL2003::Procedure,
    SQL2003::Function,
    DataType,
    SQL2003::PredefinedType,
    SQL2003::UserDefinedType,
    SQL2003::ConstructedType,
    Restriction,
    SQL2003::TableConstraint,
    SQL2003::ColumnConstraint,
    SQL2003::Table,
    SQL2003::DataType,
    ConstructedType,
    SQL2003::ReferenceType,
    SQL2003::ROW,
    SQL2003::CollectionType,
    Feature,
    SQL2003::NumericFeature,
    SQL2003::StringFeature,
    SQL2003::IntervalFeature,
    SQL2003::DatetimeFeature,
    PredefinedType,
    SQL2003::IntervalType,
    SQL2003::NumericType,
    SQL2003::DatetimeType,
    SQL2003::XMLType,
    SQL2003::BinaryStringType,
    SQL2003::ParameterWithMode,
    SQL2003::Schema,
    SQL2003::BehaviouralComponent,
    Table,
    SQL2003::DerivedTable,
    SQL2003::BaseTable,
    SQL2003::StructuredType,
    StructuralComponent,
    SQL2003::Column,
    SQL2003::Field,
    SQL2003::Attribute,
    CollectionType,
    SQL2003::MULTISET,
    SQL2003::ARRAY,
    SQL2003::CharacterStringType,
    SQL2003::BooleanType,
    IntervalTypes,
    ParameterMode,
    DatetimeFeatures,
    NumericTypes,
    XMLTypes,
    BooleanTypes,
    CharacterStringTypes,
    TriggerActionTime,
    DatetimeTypes,
    Unit,
    Multiplier,
    ReferentialAction,
    IntervalFeatures,
    TriggerEvent,
    MatchTypes,
    StringFeatures,
    BinaryStringTypes,
    NumericFeatures,
    NumericRadix,
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



def test_sql2003::trigger_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Trigger)


def test_sql2003::trigger_constructor_exists():
    assert callable(SQL2003::Trigger.__init__)


def test_sql2003::trigger_constructor_args():
    sig = inspect.signature(SQL2003::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"
    assert "name" in params, "Missing parameter 'name'"
    assert "triggeredAction" in params, "Missing parameter 'triggeredAction'"

def test_sql2003::trigger_has_event():
    assert hasattr(SQL2003::Trigger, "event")
    descriptor = None
    for klass in SQL2003::Trigger.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::trigger_has_actionTime():
    assert hasattr(SQL2003::Trigger, "actionTime")
    descriptor = None
    for klass in SQL2003::Trigger.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::trigger_has_name():
    assert hasattr(SQL2003::Trigger, "name")
    descriptor = None
    for klass in SQL2003::Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::trigger_has_triggeredAction():
    assert hasattr(SQL2003::Trigger, "triggeredAction")
    descriptor = None
    for klass in SQL2003::Trigger.__mro__:
        if "triggeredAction" in klass.__dict__:
            descriptor = klass.__dict__["triggeredAction"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::typedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003::TypedTable)


def test_sql2003::typedtable_constructor_exists():
    assert callable(SQL2003::TypedTable.__init__)


def test_sql2003::typedtable_constructor_args():
    sig = inspect.signature(SQL2003::TypedTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::view_is_not_abstract():
    assert not inspect.isabstract(SQL2003::View)


def test_sql2003::view_constructor_exists():
    assert callable(SQL2003::View.__init__)


def test_sql2003::view_constructor_args():
    sig = inspect.signature(SQL2003::View.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::structuralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003::StructuralComponent)


def test_sql2003::structuralcomponent_constructor_exists():
    assert callable(SQL2003::StructuralComponent.__init__)


def test_sql2003::structuralcomponent_constructor_args():
    sig = inspect.signature(SQL2003::StructuralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::structuralcomponent_has_name():
    assert hasattr(SQL2003::StructuralComponent, "name")
    descriptor = None
    for klass in SQL2003::StructuralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::restriction_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Restriction)


def test_sql2003::restriction_constructor_exists():
    assert callable(SQL2003::Restriction.__init__)


def test_sql2003::restriction_constructor_args():
    sig = inspect.signature(SQL2003::Restriction.__init__)
    params = list(sig.parameters.keys())
    assert "NameColumns" in params, "Missing parameter 'NameColumns'"

def test_sql2003::restriction_has_NameColumns():
    assert hasattr(SQL2003::Restriction, "NameColumns")
    descriptor = None
    for klass in SQL2003::Restriction.__mro__:
        if "NameColumns" in klass.__dict__:
            descriptor = klass.__dict__["NameColumns"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::UniqueConstraint)


def test_sql2003::uniqueconstraint_constructor_exists():
    assert callable(SQL2003::UniqueConstraint.__init__)


def test_sql2003::uniqueconstraint_constructor_args():
    sig = inspect.signature(SQL2003::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::tablecheckconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::TableCheckConstraint)


def test_sql2003::tablecheckconstraint_constructor_exists():
    assert callable(SQL2003::TableCheckConstraint.__init__)


def test_sql2003::tablecheckconstraint_constructor_args():
    sig = inspect.signature(SQL2003::TableCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sql2003::tablecheckconstraint_has_expression():
    assert hasattr(SQL2003::TableCheckConstraint, "expression")
    descriptor = None
    for klass in SQL2003::TableCheckConstraint.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::referentialconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ReferentialConstraint)


def test_sql2003::referentialconstraint_constructor_exists():
    assert callable(SQL2003::ReferentialConstraint.__init__)


def test_sql2003::referentialconstraint_constructor_args():
    sig = inspect.signature(SQL2003::ReferentialConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "delete_action" in params, "Missing parameter 'delete_action'"
    assert "match" in params, "Missing parameter 'match'"
    assert "update_action" in params, "Missing parameter 'update_action'"

def test_sql2003::referentialconstraint_has_delete_action():
    assert hasattr(SQL2003::ReferentialConstraint, "delete_action")
    descriptor = None
    for klass in SQL2003::ReferentialConstraint.__mro__:
        if "delete_action" in klass.__dict__:
            descriptor = klass.__dict__["delete_action"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::referentialconstraint_has_match():
    assert hasattr(SQL2003::ReferentialConstraint, "match")
    descriptor = None
    for klass in SQL2003::ReferentialConstraint.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::referentialconstraint_has_update_action():
    assert hasattr(SQL2003::ReferentialConstraint, "update_action")
    descriptor = None
    for klass in SQL2003::ReferentialConstraint.__mro__:
        if "update_action" in klass.__dict__:
            descriptor = klass.__dict__["update_action"]
            break
    assert isinstance(descriptor, property)



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::primarykey_is_not_abstract():
    assert not inspect.isabstract(SQL2003::PrimaryKey)


def test_sql2003::primarykey_constructor_exists():
    assert callable(SQL2003::PrimaryKey.__init__)


def test_sql2003::primarykey_constructor_args():
    sig = inspect.signature(SQL2003::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::parameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Parameter)


def test_sql2003::parameter_constructor_exists():
    assert callable(SQL2003::Parameter.__init__)


def test_sql2003::parameter_constructor_args():
    sig = inspect.signature(SQL2003::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::parameter_has_name():
    assert hasattr(SQL2003::Parameter, "name")
    descriptor = None
    for klass in SQL2003::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::methodparameter_is_not_abstract():
    assert not inspect.isabstract(SQL2003::MethodParameter)


def test_sql2003::methodparameter_constructor_exists():
    assert callable(SQL2003::MethodParameter.__init__)


def test_sql2003::methodparameter_constructor_args():
    sig = inspect.signature(SQL2003::MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::notnull_is_not_abstract():
    assert not inspect.isabstract(SQL2003::NotNull)


def test_sql2003::notnull_constructor_exists():
    assert callable(SQL2003::NotNull.__init__)


def test_sql2003::notnull_constructor_args():
    sig = inspect.signature(SQL2003::NotNull.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::method_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Method)


def test_sql2003::method_constructor_exists():
    assert callable(SQL2003::Method.__init__)


def test_sql2003::method_constructor_args():
    sig = inspect.signature(SQL2003::Method.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::method_has_body():
    assert hasattr(SQL2003::Method, "body")
    descriptor = None
    for klass in SQL2003::Method.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::method_has_name():
    assert hasattr(SQL2003::Method, "name")
    descriptor = None
    for klass in SQL2003::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::feature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Feature)


def test_sql2003::feature_constructor_exists():
    assert callable(SQL2003::Feature.__init__)


def test_sql2003::feature_constructor_args():
    sig = inspect.signature(SQL2003::Feature.__init__)
    params = list(sig.parameters.keys())



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::distincttype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::DistinctType)


def test_sql2003::distincttype_constructor_exists():
    assert callable(SQL2003::DistinctType.__init__)


def test_sql2003::distincttype_constructor_args():
    sig = inspect.signature(SQL2003::DistinctType.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(BehaviouralComponent)


def test_behaviouralcomponent_constructor_exists():
    assert callable(BehaviouralComponent.__init__)


def test_behaviouralcomponent_constructor_args():
    sig = inspect.signature(BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::procedure_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Procedure)


def test_sql2003::procedure_constructor_exists():
    assert callable(SQL2003::Procedure.__init__)


def test_sql2003::procedure_constructor_args():
    sig = inspect.signature(SQL2003::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::function_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Function)


def test_sql2003::function_constructor_exists():
    assert callable(SQL2003::Function.__init__)


def test_sql2003::function_constructor_args():
    sig = inspect.signature(SQL2003::Function.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::predefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::PredefinedType)


def test_sql2003::predefinedtype_constructor_exists():
    assert callable(SQL2003::PredefinedType.__init__)


def test_sql2003::predefinedtype_constructor_args():
    sig = inspect.signature(SQL2003::PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::UserDefinedType)


def test_sql2003::userdefinedtype_constructor_exists():
    assert callable(SQL2003::UserDefinedType.__init__)


def test_sql2003::userdefinedtype_constructor_args():
    sig = inspect.signature(SQL2003::UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::userdefinedtype_has_name():
    assert hasattr(SQL2003::UserDefinedType, "name")
    descriptor = None
    for klass in SQL2003::UserDefinedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::constructedtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ConstructedType)


def test_sql2003::constructedtype_constructor_exists():
    assert callable(SQL2003::ConstructedType.__init__)


def test_sql2003::constructedtype_constructor_args():
    sig = inspect.signature(SQL2003::ConstructedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::constructedtype_has_name():
    assert hasattr(SQL2003::ConstructedType, "name")
    descriptor = None
    for klass in SQL2003::ConstructedType.__mro__:
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



def test_sql2003::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::TableConstraint)


def test_sql2003::tableconstraint_constructor_exists():
    assert callable(SQL2003::TableConstraint.__init__)


def test_sql2003::tableconstraint_constructor_args():
    sig = inspect.signature(SQL2003::TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::tableconstraint_has_name():
    assert hasattr(SQL2003::TableConstraint, "name")
    descriptor = None
    for klass in SQL2003::TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::columnconstraint_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ColumnConstraint)


def test_sql2003::columnconstraint_constructor_exists():
    assert callable(SQL2003::ColumnConstraint.__init__)


def test_sql2003::columnconstraint_constructor_args():
    sig = inspect.signature(SQL2003::ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::table_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Table)


def test_sql2003::table_constructor_exists():
    assert callable(SQL2003::Table.__init__)


def test_sql2003::table_constructor_args():
    sig = inspect.signature(SQL2003::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::table_has_name():
    assert hasattr(SQL2003::Table, "name")
    descriptor = None
    for klass in SQL2003::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::datatype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::DataType)


def test_sql2003::datatype_constructor_exists():
    assert callable(SQL2003::DataType.__init__)


def test_sql2003::datatype_constructor_args():
    sig = inspect.signature(SQL2003::DataType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::referencetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ReferenceType)


def test_sql2003::referencetype_constructor_exists():
    assert callable(SQL2003::ReferenceType.__init__)


def test_sql2003::referencetype_constructor_args():
    sig = inspect.signature(SQL2003::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::row_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ROW)


def test_sql2003::row_constructor_exists():
    assert callable(SQL2003::ROW.__init__)


def test_sql2003::row_constructor_args():
    sig = inspect.signature(SQL2003::ROW.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::collectiontype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::CollectionType)


def test_sql2003::collectiontype_constructor_exists():
    assert callable(SQL2003::CollectionType.__init__)


def test_sql2003::collectiontype_constructor_args():
    sig = inspect.signature(SQL2003::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::numericfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::NumericFeature)


def test_sql2003::numericfeature_constructor_exists():
    assert callable(SQL2003::NumericFeature.__init__)


def test_sql2003::numericfeature_constructor_args():
    sig = inspect.signature(SQL2003::NumericFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003::numericfeature_has_value():
    assert hasattr(SQL2003::NumericFeature, "value")
    descriptor = None
    for klass in SQL2003::NumericFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::numericfeature_has_key():
    assert hasattr(SQL2003::NumericFeature, "key")
    descriptor = None
    for klass in SQL2003::NumericFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::stringfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::StringFeature)


def test_sql2003::stringfeature_constructor_exists():
    assert callable(SQL2003::StringFeature.__init__)


def test_sql2003::stringfeature_constructor_args():
    sig = inspect.signature(SQL2003::StringFeature.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sql2003::stringfeature_has_key():
    assert hasattr(SQL2003::StringFeature, "key")
    descriptor = None
    for klass in SQL2003::StringFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::stringfeature_has_value():
    assert hasattr(SQL2003::StringFeature, "value")
    descriptor = None
    for klass in SQL2003::StringFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::intervalfeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::IntervalFeature)


def test_sql2003::intervalfeature_constructor_exists():
    assert callable(SQL2003::IntervalFeature.__init__)


def test_sql2003::intervalfeature_constructor_args():
    sig = inspect.signature(SQL2003::IntervalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003::intervalfeature_has_value():
    assert hasattr(SQL2003::IntervalFeature, "value")
    descriptor = None
    for klass in SQL2003::IntervalFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::intervalfeature_has_key():
    assert hasattr(SQL2003::IntervalFeature, "key")
    descriptor = None
    for klass in SQL2003::IntervalFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::datetimefeature_is_not_abstract():
    assert not inspect.isabstract(SQL2003::DatetimeFeature)


def test_sql2003::datetimefeature_constructor_exists():
    assert callable(SQL2003::DatetimeFeature.__init__)


def test_sql2003::datetimefeature_constructor_args():
    sig = inspect.signature(SQL2003::DatetimeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sql2003::datetimefeature_has_value():
    assert hasattr(SQL2003::DatetimeFeature, "value")
    descriptor = None
    for klass in SQL2003::DatetimeFeature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::datetimefeature_has_key():
    assert hasattr(SQL2003::DatetimeFeature, "key")
    descriptor = None
    for klass in SQL2003::DatetimeFeature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::intervaltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::IntervalType)


def test_sql2003::intervaltype_constructor_exists():
    assert callable(SQL2003::IntervalType.__init__)


def test_sql2003::intervaltype_constructor_args():
    sig = inspect.signature(SQL2003::IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::intervaltype_has_descriptor():
    assert hasattr(SQL2003::IntervalType, "descriptor")
    descriptor = None
    for klass in SQL2003::IntervalType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::numerictype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::NumericType)


def test_sql2003::numerictype_constructor_exists():
    assert callable(SQL2003::NumericType.__init__)


def test_sql2003::numerictype_constructor_args():
    sig = inspect.signature(SQL2003::NumericType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::numerictype_has_descriptor():
    assert hasattr(SQL2003::NumericType, "descriptor")
    descriptor = None
    for klass in SQL2003::NumericType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::DatetimeType)


def test_sql2003::datetimetype_constructor_exists():
    assert callable(SQL2003::DatetimeType.__init__)


def test_sql2003::datetimetype_constructor_args():
    sig = inspect.signature(SQL2003::DatetimeType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::datetimetype_has_descriptor():
    assert hasattr(SQL2003::DatetimeType, "descriptor")
    descriptor = None
    for klass in SQL2003::DatetimeType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::xmltype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::XMLType)


def test_sql2003::xmltype_constructor_exists():
    assert callable(SQL2003::XMLType.__init__)


def test_sql2003::xmltype_constructor_args():
    sig = inspect.signature(SQL2003::XMLType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::xmltype_has_descriptor():
    assert hasattr(SQL2003::XMLType, "descriptor")
    descriptor = None
    for klass in SQL2003::XMLType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::binarystringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::BinaryStringType)


def test_sql2003::binarystringtype_constructor_exists():
    assert callable(SQL2003::BinaryStringType.__init__)


def test_sql2003::binarystringtype_constructor_args():
    sig = inspect.signature(SQL2003::BinaryStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length_def" in params, "Missing parameter 'length_def'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::binarystringtype_has_length_def():
    assert hasattr(SQL2003::BinaryStringType, "length_def")
    descriptor = None
    for klass in SQL2003::BinaryStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::binarystringtype_has_descriptor():
    assert hasattr(SQL2003::BinaryStringType, "descriptor")
    descriptor = None
    for klass in SQL2003::BinaryStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::parameterwithmode_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ParameterWithMode)


def test_sql2003::parameterwithmode_constructor_exists():
    assert callable(SQL2003::ParameterWithMode.__init__)


def test_sql2003::parameterwithmode_constructor_args():
    sig = inspect.signature(SQL2003::ParameterWithMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sql2003::parameterwithmode_has_mode():
    assert hasattr(SQL2003::ParameterWithMode, "mode")
    descriptor = None
    for klass in SQL2003::ParameterWithMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::schema_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Schema)


def test_sql2003::schema_constructor_exists():
    assert callable(SQL2003::Schema.__init__)


def test_sql2003::schema_constructor_args():
    sig = inspect.signature(SQL2003::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql2003::schema_has_name():
    assert hasattr(SQL2003::Schema, "name")
    descriptor = None
    for klass in SQL2003::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::behaviouralcomponent_is_not_abstract():
    assert not inspect.isabstract(SQL2003::BehaviouralComponent)


def test_sql2003::behaviouralcomponent_constructor_exists():
    assert callable(SQL2003::BehaviouralComponent.__init__)


def test_sql2003::behaviouralcomponent_constructor_args():
    sig = inspect.signature(SQL2003::BehaviouralComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_sql2003::behaviouralcomponent_has_name():
    assert hasattr(SQL2003::BehaviouralComponent, "name")
    descriptor = None
    for klass in SQL2003::BehaviouralComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::behaviouralcomponent_has_body():
    assert hasattr(SQL2003::BehaviouralComponent, "body")
    descriptor = None
    for klass in SQL2003::BehaviouralComponent.__mro__:
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



def test_sql2003::derivedtable_is_not_abstract():
    assert not inspect.isabstract(SQL2003::DerivedTable)


def test_sql2003::derivedtable_constructor_exists():
    assert callable(SQL2003::DerivedTable.__init__)


def test_sql2003::derivedtable_constructor_args():
    sig = inspect.signature(SQL2003::DerivedTable.__init__)
    params = list(sig.parameters.keys())
    assert "query_expression" in params, "Missing parameter 'query_expression'"

def test_sql2003::derivedtable_has_query_expression():
    assert hasattr(SQL2003::DerivedTable, "query_expression")
    descriptor = None
    for klass in SQL2003::DerivedTable.__mro__:
        if "query_expression" in klass.__dict__:
            descriptor = klass.__dict__["query_expression"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::basetable_is_not_abstract():
    assert not inspect.isabstract(SQL2003::BaseTable)


def test_sql2003::basetable_constructor_exists():
    assert callable(SQL2003::BaseTable.__init__)


def test_sql2003::basetable_constructor_args():
    sig = inspect.signature(SQL2003::BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::structuredtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::StructuredType)


def test_sql2003::structuredtype_constructor_exists():
    assert callable(SQL2003::StructuredType.__init__)


def test_sql2003::structuredtype_constructor_args():
    sig = inspect.signature(SQL2003::StructuredType.__init__)
    params = list(sig.parameters.keys())
    assert "is_final" in params, "Missing parameter 'is_final'"
    assert "is_instantiable" in params, "Missing parameter 'is_instantiable'"

def test_sql2003::structuredtype_has_is_final():
    assert hasattr(SQL2003::StructuredType, "is_final")
    descriptor = None
    for klass in SQL2003::StructuredType.__mro__:
        if "is_final" in klass.__dict__:
            descriptor = klass.__dict__["is_final"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::structuredtype_has_is_instantiable():
    assert hasattr(SQL2003::StructuredType, "is_instantiable")
    descriptor = None
    for klass in SQL2003::StructuredType.__mro__:
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



def test_sql2003::column_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Column)


def test_sql2003::column_constructor_exists():
    assert callable(SQL2003::Column.__init__)


def test_sql2003::column_constructor_args():
    sig = inspect.signature(SQL2003::Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003::column_has_default():
    assert hasattr(SQL2003::Column, "default")
    descriptor = None
    for klass in SQL2003::Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::field_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Field)


def test_sql2003::field_constructor_exists():
    assert callable(SQL2003::Field.__init__)


def test_sql2003::field_constructor_args():
    sig = inspect.signature(SQL2003::Field.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::attribute_is_not_abstract():
    assert not inspect.isabstract(SQL2003::Attribute)


def test_sql2003::attribute_constructor_exists():
    assert callable(SQL2003::Attribute.__init__)


def test_sql2003::attribute_constructor_args():
    sig = inspect.signature(SQL2003::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_sql2003::attribute_has_default():
    assert hasattr(SQL2003::Attribute, "default")
    descriptor = None
    for klass in SQL2003::Attribute.__mro__:
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



def test_sql2003::multiset_is_not_abstract():
    assert not inspect.isabstract(SQL2003::MULTISET)


def test_sql2003::multiset_constructor_exists():
    assert callable(SQL2003::MULTISET.__init__)


def test_sql2003::multiset_constructor_args():
    sig = inspect.signature(SQL2003::MULTISET.__init__)
    params = list(sig.parameters.keys())



def test_sql2003::array_is_not_abstract():
    assert not inspect.isabstract(SQL2003::ARRAY)


def test_sql2003::array_constructor_exists():
    assert callable(SQL2003::ARRAY.__init__)


def test_sql2003::array_constructor_args():
    sig = inspect.signature(SQL2003::ARRAY.__init__)
    params = list(sig.parameters.keys())
    assert "num_elements" in params, "Missing parameter 'num_elements'"

def test_sql2003::array_has_num_elements():
    assert hasattr(SQL2003::ARRAY, "num_elements")
    descriptor = None
    for klass in SQL2003::ARRAY.__mro__:
        if "num_elements" in klass.__dict__:
            descriptor = klass.__dict__["num_elements"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::characterstringtype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::CharacterStringType)


def test_sql2003::characterstringtype_constructor_exists():
    assert callable(SQL2003::CharacterStringType.__init__)


def test_sql2003::characterstringtype_constructor_args():
    sig = inspect.signature(SQL2003::CharacterStringType.__init__)
    params = list(sig.parameters.keys())
    assert "length_def" in params, "Missing parameter 'length_def'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::characterstringtype_has_length_def():
    assert hasattr(SQL2003::CharacterStringType, "length_def")
    descriptor = None
    for klass in SQL2003::CharacterStringType.__mro__:
        if "length_def" in klass.__dict__:
            descriptor = klass.__dict__["length_def"]
            break
    assert isinstance(descriptor, property)

def test_sql2003::characterstringtype_has_descriptor():
    assert hasattr(SQL2003::CharacterStringType, "descriptor")
    descriptor = None
    for klass in SQL2003::CharacterStringType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_sql2003::booleantype_is_not_abstract():
    assert not inspect.isabstract(SQL2003::BooleanType)


def test_sql2003::booleantype_constructor_exists():
    assert callable(SQL2003::BooleanType.__init__)


def test_sql2003::booleantype_constructor_args():
    sig = inspect.signature(SQL2003::BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_sql2003::booleantype_has_descriptor():
    assert hasattr(SQL2003::BooleanType, "descriptor")
    descriptor = None
    for klass in SQL2003::BooleanType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_intervaltypes_exists():
    # Check that the Enumeration exists
    assert IntervalTypes is not None

def test_intervaltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalTypes]
    expected_literals = [
        "MINUTE_SECOND",
        "DAY",
        "MINUTE",
        "SECOND",
        "MONTH",
        "YEAR",
        "DAY_SECOND",
        "HOUR_MINUTE",
        "HOUR_SECOND",
        "YEAR_MONTH",
        "DAY_HOUR",
        "DAY_MINUTE",
        "HOUR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalTypes"

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

def test_numerictypes_exists():
    # Check that the Enumeration exists
    assert NumericTypes is not None

def test_numerictypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericTypes]
    expected_literals = [
        "FLOAT",
        "NUMERIC",
        "DOUBLEPRECISION",
        "INTEGER",
        "SMALLINT",
        "BIGINT",
        "REAL",
        "DECIMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericTypes"

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

def test_datetimetypes_exists():
    # Check that the Enumeration exists
    assert DatetimeTypes is not None

def test_datetimetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatetimeTypes]
    expected_literals = [
        "TIMEWITHOUTTIMEZONE",
        "TIMESTAMPWITHTIMEZONE",
        "TIMEWITHTIMEZONE",
        "DATE",
        "TIMESTAMPWITHOUTTIMEZONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatetimeTypes"

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
        "T",
        "M",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Multiplier"

def test_referentialaction_exists():
    # Check that the Enumeration exists
    assert ReferentialAction is not None

def test_referentialaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialAction]
    expected_literals = [
        "SET_DEFAULT",
        "SET_NULL",
        "CASCADE",
        "NO_ACTION",
        "RESTRICT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialAction"

def test_intervalfeatures_exists():
    # Check that the Enumeration exists
    assert IntervalFeatures is not None

def test_intervalfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalFeatures]
    expected_literals = [
        "leading_precision",
        "start_leading_precision",
        "second_precision",
        "end_leading_precision",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalFeatures"

def test_triggerevent_exists():
    # Check that the Enumeration exists
    assert TriggerEvent is not None

def test_triggerevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerEvent]
    expected_literals = [
        "UPDATE",
        "INSERT",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerEvent"

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
        "multiplier",
        "length",
        "unit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringFeatures"

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

def test_numericfeatures_exists():
    # Check that the Enumeration exists
    assert NumericFeatures is not None

def test_numericfeatures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericFeatures]
    expected_literals = [
        "scale",
        "precision",
        "radix",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericFeatures"

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
SQL2003::Trigger_strategy = st.builds(
    SQL2003::Trigger,
    event=
        safe_text,
    actionTime=
        safe_text,
    name=
        safe_text,
    triggeredAction=
        safe_text
)
SQL2003::TypedTable_strategy = st.builds(
    SQL2003::TypedTable,
)
SQL2003::View_strategy = st.builds(
    SQL2003::View,
)
SQL2003::StructuralComponent_strategy = st.builds(
    SQL2003::StructuralComponent,
    name=
        safe_text
)
SQL2003::Restriction_strategy = st.builds(
    SQL2003::Restriction,
    NameColumns=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
SQL2003::UniqueConstraint_strategy = st.builds(
    SQL2003::UniqueConstraint,
)
SQL2003::TableCheckConstraint_strategy = st.builds(
    SQL2003::TableCheckConstraint,
    expression=
        safe_text
)
SQL2003::ReferentialConstraint_strategy = st.builds(
    SQL2003::ReferentialConstraint,
    delete_action=
        safe_text,
    match=
        safe_text,
    update_action=
        safe_text
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
SQL2003::PrimaryKey_strategy = st.builds(
    SQL2003::PrimaryKey,
)
SQL2003::Parameter_strategy = st.builds(
    SQL2003::Parameter,
    name=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
SQL2003::MethodParameter_strategy = st.builds(
    SQL2003::MethodParameter,
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
SQL2003::NotNull_strategy = st.builds(
    SQL2003::NotNull,
)
SQL2003::Method_strategy = st.builds(
    SQL2003::Method,
    body=
        safe_text,
    name=
        safe_text
)
SQL2003::Feature_strategy = st.builds(
    SQL2003::Feature,
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
SQL2003::DistinctType_strategy = st.builds(
    SQL2003::DistinctType,
)
BehaviouralComponent_strategy = st.builds(
    BehaviouralComponent,
)
SQL2003::Procedure_strategy = st.builds(
    SQL2003::Procedure,
)
SQL2003::Function_strategy = st.builds(
    SQL2003::Function,
)
DataType_strategy = st.builds(
    DataType,
)
SQL2003::PredefinedType_strategy = st.builds(
    SQL2003::PredefinedType,
)
SQL2003::UserDefinedType_strategy = st.builds(
    SQL2003::UserDefinedType,
    name=
        safe_text
)
SQL2003::ConstructedType_strategy = st.builds(
    SQL2003::ConstructedType,
    name=
        safe_text
)
Restriction_strategy = st.builds(
    Restriction,
)
SQL2003::TableConstraint_strategy = st.builds(
    SQL2003::TableConstraint,
    name=
        safe_text
)
SQL2003::ColumnConstraint_strategy = st.builds(
    SQL2003::ColumnConstraint,
)
SQL2003::Table_strategy = st.builds(
    SQL2003::Table,
    name=
        safe_text
)
SQL2003::DataType_strategy = st.builds(
    SQL2003::DataType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
SQL2003::ReferenceType_strategy = st.builds(
    SQL2003::ReferenceType,
)
SQL2003::ROW_strategy = st.builds(
    SQL2003::ROW,
)
SQL2003::CollectionType_strategy = st.builds(
    SQL2003::CollectionType,
)
Feature_strategy = st.builds(
    Feature,
)
SQL2003::NumericFeature_strategy = st.builds(
    SQL2003::NumericFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003::StringFeature_strategy = st.builds(
    SQL2003::StringFeature,
    key=
        safe_text,
    value=
        safe_text
)
SQL2003::IntervalFeature_strategy = st.builds(
    SQL2003::IntervalFeature,
    value=
        safe_text,
    key=
        safe_text
)
SQL2003::DatetimeFeature_strategy = st.builds(
    SQL2003::DatetimeFeature,
    value=
        safe_text,
    key=
        safe_text
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
SQL2003::IntervalType_strategy = st.builds(
    SQL2003::IntervalType,
    descriptor=
        safe_text
)
SQL2003::NumericType_strategy = st.builds(
    SQL2003::NumericType,
    descriptor=
        safe_text
)
SQL2003::DatetimeType_strategy = st.builds(
    SQL2003::DatetimeType,
    descriptor=
        safe_text
)
SQL2003::XMLType_strategy = st.builds(
    SQL2003::XMLType,
    descriptor=
        safe_text
)
SQL2003::BinaryStringType_strategy = st.builds(
    SQL2003::BinaryStringType,
    length_def=
        safe_text,
    descriptor=
        safe_text
)
SQL2003::ParameterWithMode_strategy = st.builds(
    SQL2003::ParameterWithMode,
    mode=
        safe_text
)
SQL2003::Schema_strategy = st.builds(
    SQL2003::Schema,
    name=
        safe_text
)
SQL2003::BehaviouralComponent_strategy = st.builds(
    SQL2003::BehaviouralComponent,
    name=
        safe_text,
    body=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SQL2003::DerivedTable_strategy = st.builds(
    SQL2003::DerivedTable,
    query_expression=
        safe_text
)
SQL2003::BaseTable_strategy = st.builds(
    SQL2003::BaseTable,
)
SQL2003::StructuredType_strategy = st.builds(
    SQL2003::StructuredType,
    is_final=
        st.booleans(),
    is_instantiable=
        st.booleans()
)
StructuralComponent_strategy = st.builds(
    StructuralComponent,
)
SQL2003::Column_strategy = st.builds(
    SQL2003::Column,
    default=
        safe_text
)
SQL2003::Field_strategy = st.builds(
    SQL2003::Field,
)
SQL2003::Attribute_strategy = st.builds(
    SQL2003::Attribute,
    default=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
SQL2003::MULTISET_strategy = st.builds(
    SQL2003::MULTISET,
)
SQL2003::ARRAY_strategy = st.builds(
    SQL2003::ARRAY,
    num_elements=
        safe_text
)
SQL2003::CharacterStringType_strategy = st.builds(
    SQL2003::CharacterStringType,
    length_def=
        safe_text,
    descriptor=
        safe_text
)
SQL2003::BooleanType_strategy = st.builds(
    SQL2003::BooleanType,
    descriptor=
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

@given(instance=SQL2003::Trigger_strategy)
@settings(max_examples=50)
def test_sql2003::trigger_instantiation(instance):
    assert isinstance(instance, SQL2003::Trigger)

@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_actionTime_type(instance):
    assert isinstance(instance.actionTime, str)


@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original

@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_triggeredAction_type(instance):
    assert isinstance(instance.triggeredAction, str)


@given(instance=SQL2003::Trigger_strategy)
def test_sql2003::trigger_triggeredAction_setter(instance):
    original = instance.triggeredAction
    instance.triggeredAction = original
    assert instance.triggeredAction == original

@given(instance=SQL2003::TypedTable_strategy)
@settings(max_examples=50)
def test_sql2003::typedtable_instantiation(instance):
    assert isinstance(instance, SQL2003::TypedTable)

@given(instance=SQL2003::View_strategy)
@settings(max_examples=50)
def test_sql2003::view_instantiation(instance):
    assert isinstance(instance, SQL2003::View)

@given(instance=SQL2003::StructuralComponent_strategy)
@settings(max_examples=50)
def test_sql2003::structuralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003::StructuralComponent)

@given(instance=SQL2003::StructuralComponent_strategy)
def test_sql2003::structuralcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::StructuralComponent_strategy)
def test_sql2003::structuralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::Restriction_strategy)
@settings(max_examples=50)
def test_sql2003::restriction_instantiation(instance):
    assert isinstance(instance, SQL2003::Restriction)

@given(instance=SQL2003::Restriction_strategy)
def test_sql2003::restriction_NameColumns_type(instance):
    assert isinstance(instance.NameColumns, str)


@given(instance=SQL2003::Restriction_strategy)
def test_sql2003::restriction_NameColumns_setter(instance):
    original = instance.NameColumns
    instance.NameColumns = original
    assert instance.NameColumns == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=SQL2003::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::UniqueConstraint)

@given(instance=SQL2003::TableCheckConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::tablecheckconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::TableCheckConstraint)

@given(instance=SQL2003::TableCheckConstraint_strategy)
def test_sql2003::tablecheckconstraint_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=SQL2003::TableCheckConstraint_strategy)
def test_sql2003::tablecheckconstraint_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=SQL2003::ReferentialConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::referentialconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::ReferentialConstraint)

@given(instance=SQL2003::ReferentialConstraint_strategy)
def test_sql2003::referentialconstraint_delete_action_type(instance):
    assert isinstance(instance.delete_action, str)


@given(instance=SQL2003::ReferentialConstraint_strategy)
def test_sql2003::referentialconstraint_delete_action_setter(instance):
    original = instance.delete_action
    instance.delete_action = original
    assert instance.delete_action == original

@given(instance=SQL2003::ReferentialConstraint_strategy)
def test_sql2003::referentialconstraint_match_type(instance):
    assert isinstance(instance.match, str)


@given(instance=SQL2003::ReferentialConstraint_strategy)
def test_sql2003::referentialconstraint_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original

@given(instance=SQL2003::ReferentialConstraint_strategy)
def test_sql2003::referentialconstraint_update_action_type(instance):
    assert isinstance(instance.update_action, str)


@given(instance=SQL2003::ReferentialConstraint_strategy)
def test_sql2003::referentialconstraint_update_action_setter(instance):
    original = instance.update_action
    instance.update_action = original
    assert instance.update_action == original

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=SQL2003::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql2003::primarykey_instantiation(instance):
    assert isinstance(instance, SQL2003::PrimaryKey)

@given(instance=SQL2003::Parameter_strategy)
@settings(max_examples=50)
def test_sql2003::parameter_instantiation(instance):
    assert isinstance(instance, SQL2003::Parameter)

@given(instance=SQL2003::Parameter_strategy)
def test_sql2003::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::Parameter_strategy)
def test_sql2003::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=SQL2003::MethodParameter_strategy)
@settings(max_examples=50)
def test_sql2003::methodparameter_instantiation(instance):
    assert isinstance(instance, SQL2003::MethodParameter)

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=SQL2003::NotNull_strategy)
@settings(max_examples=50)
def test_sql2003::notnull_instantiation(instance):
    assert isinstance(instance, SQL2003::NotNull)

@given(instance=SQL2003::Method_strategy)
@settings(max_examples=50)
def test_sql2003::method_instantiation(instance):
    assert isinstance(instance, SQL2003::Method)

@given(instance=SQL2003::Method_strategy)
def test_sql2003::method_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=SQL2003::Method_strategy)
def test_sql2003::method_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=SQL2003::Method_strategy)
def test_sql2003::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::Method_strategy)
def test_sql2003::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::Feature_strategy)
@settings(max_examples=50)
def test_sql2003::feature_instantiation(instance):
    assert isinstance(instance, SQL2003::Feature)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=SQL2003::DistinctType_strategy)
@settings(max_examples=50)
def test_sql2003::distincttype_instantiation(instance):
    assert isinstance(instance, SQL2003::DistinctType)

@given(instance=BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, BehaviouralComponent)

@given(instance=SQL2003::Procedure_strategy)
@settings(max_examples=50)
def test_sql2003::procedure_instantiation(instance):
    assert isinstance(instance, SQL2003::Procedure)

@given(instance=SQL2003::Function_strategy)
@settings(max_examples=50)
def test_sql2003::function_instantiation(instance):
    assert isinstance(instance, SQL2003::Function)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=SQL2003::PredefinedType_strategy)
@settings(max_examples=50)
def test_sql2003::predefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003::PredefinedType)

@given(instance=SQL2003::UserDefinedType_strategy)
@settings(max_examples=50)
def test_sql2003::userdefinedtype_instantiation(instance):
    assert isinstance(instance, SQL2003::UserDefinedType)

@given(instance=SQL2003::UserDefinedType_strategy)
def test_sql2003::userdefinedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::UserDefinedType_strategy)
def test_sql2003::userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::ConstructedType_strategy)
@settings(max_examples=50)
def test_sql2003::constructedtype_instantiation(instance):
    assert isinstance(instance, SQL2003::ConstructedType)

@given(instance=SQL2003::ConstructedType_strategy)
def test_sql2003::constructedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::ConstructedType_strategy)
def test_sql2003::constructedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=SQL2003::TableConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::tableconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::TableConstraint)

@given(instance=SQL2003::TableConstraint_strategy)
def test_sql2003::tableconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::TableConstraint_strategy)
def test_sql2003::tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sql2003::columnconstraint_instantiation(instance):
    assert isinstance(instance, SQL2003::ColumnConstraint)

@given(instance=SQL2003::Table_strategy)
@settings(max_examples=50)
def test_sql2003::table_instantiation(instance):
    assert isinstance(instance, SQL2003::Table)

@given(instance=SQL2003::Table_strategy)
def test_sql2003::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::Table_strategy)
def test_sql2003::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::DataType_strategy)
@settings(max_examples=50)
def test_sql2003::datatype_instantiation(instance):
    assert isinstance(instance, SQL2003::DataType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=SQL2003::ReferenceType_strategy)
@settings(max_examples=50)
def test_sql2003::referencetype_instantiation(instance):
    assert isinstance(instance, SQL2003::ReferenceType)

@given(instance=SQL2003::ROW_strategy)
@settings(max_examples=50)
def test_sql2003::row_instantiation(instance):
    assert isinstance(instance, SQL2003::ROW)

@given(instance=SQL2003::CollectionType_strategy)
@settings(max_examples=50)
def test_sql2003::collectiontype_instantiation(instance):
    assert isinstance(instance, SQL2003::CollectionType)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=SQL2003::NumericFeature_strategy)
@settings(max_examples=50)
def test_sql2003::numericfeature_instantiation(instance):
    assert isinstance(instance, SQL2003::NumericFeature)

@given(instance=SQL2003::NumericFeature_strategy)
def test_sql2003::numericfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::NumericFeature_strategy)
def test_sql2003::numericfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::NumericFeature_strategy)
def test_sql2003::numericfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::NumericFeature_strategy)
def test_sql2003::numericfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::StringFeature_strategy)
@settings(max_examples=50)
def test_sql2003::stringfeature_instantiation(instance):
    assert isinstance(instance, SQL2003::StringFeature)

@given(instance=SQL2003::StringFeature_strategy)
def test_sql2003::stringfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::StringFeature_strategy)
def test_sql2003::stringfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::StringFeature_strategy)
def test_sql2003::stringfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::StringFeature_strategy)
def test_sql2003::stringfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::IntervalFeature_strategy)
@settings(max_examples=50)
def test_sql2003::intervalfeature_instantiation(instance):
    assert isinstance(instance, SQL2003::IntervalFeature)

@given(instance=SQL2003::IntervalFeature_strategy)
def test_sql2003::intervalfeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::IntervalFeature_strategy)
def test_sql2003::intervalfeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::IntervalFeature_strategy)
def test_sql2003::intervalfeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::IntervalFeature_strategy)
def test_sql2003::intervalfeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=SQL2003::DatetimeFeature_strategy)
@settings(max_examples=50)
def test_sql2003::datetimefeature_instantiation(instance):
    assert isinstance(instance, SQL2003::DatetimeFeature)

@given(instance=SQL2003::DatetimeFeature_strategy)
def test_sql2003::datetimefeature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQL2003::DatetimeFeature_strategy)
def test_sql2003::datetimefeature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQL2003::DatetimeFeature_strategy)
def test_sql2003::datetimefeature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=SQL2003::DatetimeFeature_strategy)
def test_sql2003::datetimefeature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=SQL2003::IntervalType_strategy)
@settings(max_examples=50)
def test_sql2003::intervaltype_instantiation(instance):
    assert isinstance(instance, SQL2003::IntervalType)

@given(instance=SQL2003::IntervalType_strategy)
def test_sql2003::intervaltype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::IntervalType_strategy)
def test_sql2003::intervaltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::NumericType_strategy)
@settings(max_examples=50)
def test_sql2003::numerictype_instantiation(instance):
    assert isinstance(instance, SQL2003::NumericType)

@given(instance=SQL2003::NumericType_strategy)
def test_sql2003::numerictype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::NumericType_strategy)
def test_sql2003::numerictype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::DatetimeType_strategy)
@settings(max_examples=50)
def test_sql2003::datetimetype_instantiation(instance):
    assert isinstance(instance, SQL2003::DatetimeType)

@given(instance=SQL2003::DatetimeType_strategy)
def test_sql2003::datetimetype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::DatetimeType_strategy)
def test_sql2003::datetimetype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::XMLType_strategy)
@settings(max_examples=50)
def test_sql2003::xmltype_instantiation(instance):
    assert isinstance(instance, SQL2003::XMLType)

@given(instance=SQL2003::XMLType_strategy)
def test_sql2003::xmltype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::XMLType_strategy)
def test_sql2003::xmltype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::BinaryStringType_strategy)
@settings(max_examples=50)
def test_sql2003::binarystringtype_instantiation(instance):
    assert isinstance(instance, SQL2003::BinaryStringType)

@given(instance=SQL2003::BinaryStringType_strategy)
def test_sql2003::binarystringtype_length_def_type(instance):
    assert isinstance(instance.length_def, str)


@given(instance=SQL2003::BinaryStringType_strategy)
def test_sql2003::binarystringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003::BinaryStringType_strategy)
def test_sql2003::binarystringtype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::BinaryStringType_strategy)
def test_sql2003::binarystringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::ParameterWithMode_strategy)
@settings(max_examples=50)
def test_sql2003::parameterwithmode_instantiation(instance):
    assert isinstance(instance, SQL2003::ParameterWithMode)

@given(instance=SQL2003::ParameterWithMode_strategy)
def test_sql2003::parameterwithmode_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=SQL2003::ParameterWithMode_strategy)
def test_sql2003::parameterwithmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SQL2003::Schema_strategy)
@settings(max_examples=50)
def test_sql2003::schema_instantiation(instance):
    assert isinstance(instance, SQL2003::Schema)

@given(instance=SQL2003::Schema_strategy)
def test_sql2003::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::Schema_strategy)
def test_sql2003::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::BehaviouralComponent_strategy)
@settings(max_examples=50)
def test_sql2003::behaviouralcomponent_instantiation(instance):
    assert isinstance(instance, SQL2003::BehaviouralComponent)

@given(instance=SQL2003::BehaviouralComponent_strategy)
def test_sql2003::behaviouralcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQL2003::BehaviouralComponent_strategy)
def test_sql2003::behaviouralcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQL2003::BehaviouralComponent_strategy)
def test_sql2003::behaviouralcomponent_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=SQL2003::BehaviouralComponent_strategy)
def test_sql2003::behaviouralcomponent_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SQL2003::DerivedTable_strategy)
@settings(max_examples=50)
def test_sql2003::derivedtable_instantiation(instance):
    assert isinstance(instance, SQL2003::DerivedTable)

@given(instance=SQL2003::DerivedTable_strategy)
def test_sql2003::derivedtable_query_expression_type(instance):
    assert isinstance(instance.query_expression, str)


@given(instance=SQL2003::DerivedTable_strategy)
def test_sql2003::derivedtable_query_expression_setter(instance):
    original = instance.query_expression
    instance.query_expression = original
    assert instance.query_expression == original

@given(instance=SQL2003::BaseTable_strategy)
@settings(max_examples=50)
def test_sql2003::basetable_instantiation(instance):
    assert isinstance(instance, SQL2003::BaseTable)

@given(instance=SQL2003::StructuredType_strategy)
@settings(max_examples=50)
def test_sql2003::structuredtype_instantiation(instance):
    assert isinstance(instance, SQL2003::StructuredType)

@given(instance=SQL2003::StructuredType_strategy)
def test_sql2003::structuredtype_is_final_type(instance):
    assert isinstance(instance.is_final, bool)


@given(instance=SQL2003::StructuredType_strategy)
def test_sql2003::structuredtype_is_final_setter(instance):
    original = instance.is_final
    instance.is_final = original
    assert instance.is_final == original

@given(instance=SQL2003::StructuredType_strategy)
def test_sql2003::structuredtype_is_instantiable_type(instance):
    assert isinstance(instance.is_instantiable, bool)


@given(instance=SQL2003::StructuredType_strategy)
def test_sql2003::structuredtype_is_instantiable_setter(instance):
    original = instance.is_instantiable
    instance.is_instantiable = original
    assert instance.is_instantiable == original

@given(instance=StructuralComponent_strategy)
@settings(max_examples=50)
def test_structuralcomponent_instantiation(instance):
    assert isinstance(instance, StructuralComponent)

@given(instance=SQL2003::Column_strategy)
@settings(max_examples=50)
def test_sql2003::column_instantiation(instance):
    assert isinstance(instance, SQL2003::Column)

@given(instance=SQL2003::Column_strategy)
def test_sql2003::column_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=SQL2003::Column_strategy)
def test_sql2003::column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=SQL2003::Field_strategy)
@settings(max_examples=50)
def test_sql2003::field_instantiation(instance):
    assert isinstance(instance, SQL2003::Field)

@given(instance=SQL2003::Attribute_strategy)
@settings(max_examples=50)
def test_sql2003::attribute_instantiation(instance):
    assert isinstance(instance, SQL2003::Attribute)

@given(instance=SQL2003::Attribute_strategy)
def test_sql2003::attribute_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=SQL2003::Attribute_strategy)
def test_sql2003::attribute_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=SQL2003::MULTISET_strategy)
@settings(max_examples=50)
def test_sql2003::multiset_instantiation(instance):
    assert isinstance(instance, SQL2003::MULTISET)

@given(instance=SQL2003::ARRAY_strategy)
@settings(max_examples=50)
def test_sql2003::array_instantiation(instance):
    assert isinstance(instance, SQL2003::ARRAY)

@given(instance=SQL2003::ARRAY_strategy)
def test_sql2003::array_num_elements_type(instance):
    assert isinstance(instance.num_elements, str)


@given(instance=SQL2003::ARRAY_strategy)
def test_sql2003::array_num_elements_setter(instance):
    original = instance.num_elements
    instance.num_elements = original
    assert instance.num_elements == original

@given(instance=SQL2003::CharacterStringType_strategy)
@settings(max_examples=50)
def test_sql2003::characterstringtype_instantiation(instance):
    assert isinstance(instance, SQL2003::CharacterStringType)

@given(instance=SQL2003::CharacterStringType_strategy)
def test_sql2003::characterstringtype_length_def_type(instance):
    assert isinstance(instance.length_def, str)


@given(instance=SQL2003::CharacterStringType_strategy)
def test_sql2003::characterstringtype_length_def_setter(instance):
    original = instance.length_def
    instance.length_def = original
    assert instance.length_def == original

@given(instance=SQL2003::CharacterStringType_strategy)
def test_sql2003::characterstringtype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::CharacterStringType_strategy)
def test_sql2003::characterstringtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=SQL2003::BooleanType_strategy)
@settings(max_examples=50)
def test_sql2003::booleantype_instantiation(instance):
    assert isinstance(instance, SQL2003::BooleanType)

@given(instance=SQL2003::BooleanType_strategy)
def test_sql2003::booleantype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=SQL2003::BooleanType_strategy)
def test_sql2003::booleantype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original
