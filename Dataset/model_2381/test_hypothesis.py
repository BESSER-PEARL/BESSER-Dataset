import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UserDefinedType,
    relational::DistinctUserDefinedType,
    DistinctUserDefinedType,
    relational::Domain,
    DataType,
    UniqueConstraint,
    relational::PrimaryKey,
    ReferenceConstraint,
    relational::UniqueConstraint,
    Constraint,
    relational::TableConstraint,
    Table,
    relational::BaseTable,
    relational::ForeignKey,
    TypedElement,
    relational::Column,
    TableConstraint,
    relational::CheckConstraint,
    relational::ReferenceConstraint,
    relational::UserDefinedType,
    relational::Assertion,
    SQLObject,
    relational::TypedElement,
    relational::Trigger,
    relational::Table,
    relational::Constraint,
    relational::Schema,
    relational::DataType,
    ENamedElement,
    relational::SQLObject,
    relational::ENamedElement,
    relational::Comment,
    ReferentialActionType,
    ActionTimeType,
    ActionGranularityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_relational::distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(relational::DistinctUserDefinedType)


def test_relational::distinctuserdefinedtype_constructor_exists():
    assert callable(relational::DistinctUserDefinedType.__init__)


def test_relational::distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(relational::DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(DistinctUserDefinedType)


def test_distinctuserdefinedtype_constructor_exists():
    assert callable(DistinctUserDefinedType.__init__)


def test_distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_relational::domain_is_not_abstract():
    assert not inspect.isabstract(relational::Domain)


def test_relational::domain_constructor_exists():
    assert callable(relational::Domain.__init__)


def test_relational::domain_constructor_args():
    sig = inspect.signature(relational::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_relational::domain_has_nullable():
    assert hasattr(relational::Domain, "nullable")
    descriptor = None
    for klass in relational::Domain.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_relational::domain_has_defaultValue():
    assert hasattr(relational::Domain, "defaultValue")
    descriptor = None
    for klass in relational::Domain.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(UniqueConstraint)


def test_uniqueconstraint_constructor_exists():
    assert callable(UniqueConstraint.__init__)


def test_uniqueconstraint_constructor_args():
    sig = inspect.signature(UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational::primarykey_is_not_abstract():
    assert not inspect.isabstract(relational::PrimaryKey)


def test_relational::primarykey_constructor_exists():
    assert callable(relational::PrimaryKey.__init__)


def test_relational::primarykey_constructor_args():
    sig = inspect.signature(relational::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(ReferenceConstraint)


def test_referenceconstraint_constructor_exists():
    assert callable(ReferenceConstraint.__init__)


def test_referenceconstraint_constructor_args():
    sig = inspect.signature(ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(relational::UniqueConstraint)


def test_relational::uniqueconstraint_constructor_exists():
    assert callable(relational::UniqueConstraint.__init__)


def test_relational::uniqueconstraint_constructor_args():
    sig = inspect.signature(relational::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_relational::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(relational::TableConstraint)


def test_relational::tableconstraint_constructor_exists():
    assert callable(relational::TableConstraint.__init__)


def test_relational::tableconstraint_constructor_args():
    sig = inspect.signature(relational::TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_relational::basetable_is_not_abstract():
    assert not inspect.isabstract(relational::BaseTable)


def test_relational::basetable_constructor_exists():
    assert callable(relational::BaseTable.__init__)


def test_relational::basetable_constructor_args():
    sig = inspect.signature(relational::BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_relational::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational::ForeignKey)


def test_relational::foreignkey_constructor_exists():
    assert callable(relational::ForeignKey.__init__)


def test_relational::foreignkey_constructor_args():
    sig = inspect.signature(relational::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"
    assert "onDelete" in params, "Missing parameter 'onDelete'"

def test_relational::foreignkey_has_onUpdate():
    assert hasattr(relational::ForeignKey, "onUpdate")
    descriptor = None
    for klass in relational::ForeignKey.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)

def test_relational::foreignkey_has_onDelete():
    assert hasattr(relational::ForeignKey, "onDelete")
    descriptor = None
    for klass in relational::ForeignKey.__mro__:
        if "onDelete" in klass.__dict__:
            descriptor = klass.__dict__["onDelete"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(relational::Column)


def test_relational::column_constructor_exists():
    assert callable(relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(relational::Column.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "srid" in params, "Missing parameter 'srid'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_relational::column_has_length():
    assert hasattr(relational::Column, "length")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_srid():
    assert hasattr(relational::Column, "srid")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "srid" in klass.__dict__:
            descriptor = klass.__dict__["srid"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_defaultValue():
    assert hasattr(relational::Column, "defaultValue")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_nullable():
    assert hasattr(relational::Column, "nullable")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational::checkconstraint_is_not_abstract():
    assert not inspect.isabstract(relational::CheckConstraint)


def test_relational::checkconstraint_constructor_exists():
    assert callable(relational::CheckConstraint.__init__)


def test_relational::checkconstraint_constructor_args():
    sig = inspect.signature(relational::CheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "searchCondition" in params, "Missing parameter 'searchCondition'"

def test_relational::checkconstraint_has_searchCondition():
    assert hasattr(relational::CheckConstraint, "searchCondition")
    descriptor = None
    for klass in relational::CheckConstraint.__mro__:
        if "searchCondition" in klass.__dict__:
            descriptor = klass.__dict__["searchCondition"]
            break
    assert isinstance(descriptor, property)



def test_relational::referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(relational::ReferenceConstraint)


def test_relational::referenceconstraint_constructor_exists():
    assert callable(relational::ReferenceConstraint.__init__)


def test_relational::referenceconstraint_constructor_args():
    sig = inspect.signature(relational::ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational::userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(relational::UserDefinedType)


def test_relational::userdefinedtype_constructor_exists():
    assert callable(relational::UserDefinedType.__init__)


def test_relational::userdefinedtype_constructor_args():
    sig = inspect.signature(relational::UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_relational::assertion_is_not_abstract():
    assert not inspect.isabstract(relational::Assertion)


def test_relational::assertion_constructor_exists():
    assert callable(relational::Assertion.__init__)


def test_relational::assertion_constructor_args():
    sig = inspect.signature(relational::Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "searchCondition" in params, "Missing parameter 'searchCondition'"

def test_relational::assertion_has_searchCondition():
    assert hasattr(relational::Assertion, "searchCondition")
    descriptor = None
    for klass in relational::Assertion.__mro__:
        if "searchCondition" in klass.__dict__:
            descriptor = klass.__dict__["searchCondition"]
            break
    assert isinstance(descriptor, property)



def test_sqlobject_is_not_abstract():
    assert not inspect.isabstract(SQLObject)


def test_sqlobject_constructor_exists():
    assert callable(SQLObject.__init__)


def test_sqlobject_constructor_args():
    sig = inspect.signature(SQLObject.__init__)
    params = list(sig.parameters.keys())



def test_relational::typedelement_is_not_abstract():
    assert not inspect.isabstract(relational::TypedElement)


def test_relational::typedelement_constructor_exists():
    assert callable(relational::TypedElement.__init__)


def test_relational::typedelement_constructor_args():
    sig = inspect.signature(relational::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_relational::trigger_is_not_abstract():
    assert not inspect.isabstract(relational::Trigger)


def test_relational::trigger_constructor_exists():
    assert callable(relational::Trigger.__init__)


def test_relational::trigger_constructor_args():
    sig = inspect.signature(relational::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "oldTable" in params, "Missing parameter 'oldTable'"
    assert "statementSQL" in params, "Missing parameter 'statementSQL'"
    assert "oldRow" in params, "Missing parameter 'oldRow'"
    assert "insertType" in params, "Missing parameter 'insertType'"
    assert "condition" in params, "Missing parameter 'condition'"
    assert "actionGranularity" in params, "Missing parameter 'actionGranularity'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"
    assert "newTable" in params, "Missing parameter 'newTable'"
    assert "newRow" in params, "Missing parameter 'newRow'"
    assert "updateType" in params, "Missing parameter 'updateType'"
    assert "deleteType" in params, "Missing parameter 'deleteType'"

def test_relational::trigger_has_oldTable():
    assert hasattr(relational::Trigger, "oldTable")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "oldTable" in klass.__dict__:
            descriptor = klass.__dict__["oldTable"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_statementSQL():
    assert hasattr(relational::Trigger, "statementSQL")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "statementSQL" in klass.__dict__:
            descriptor = klass.__dict__["statementSQL"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_oldRow():
    assert hasattr(relational::Trigger, "oldRow")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "oldRow" in klass.__dict__:
            descriptor = klass.__dict__["oldRow"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_insertType():
    assert hasattr(relational::Trigger, "insertType")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "insertType" in klass.__dict__:
            descriptor = klass.__dict__["insertType"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_condition():
    assert hasattr(relational::Trigger, "condition")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_actionGranularity():
    assert hasattr(relational::Trigger, "actionGranularity")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "actionGranularity" in klass.__dict__:
            descriptor = klass.__dict__["actionGranularity"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_actionTime():
    assert hasattr(relational::Trigger, "actionTime")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_newTable():
    assert hasattr(relational::Trigger, "newTable")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "newTable" in klass.__dict__:
            descriptor = klass.__dict__["newTable"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_newRow():
    assert hasattr(relational::Trigger, "newRow")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "newRow" in klass.__dict__:
            descriptor = klass.__dict__["newRow"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_updateType():
    assert hasattr(relational::Trigger, "updateType")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "updateType" in klass.__dict__:
            descriptor = klass.__dict__["updateType"]
            break
    assert isinstance(descriptor, property)

def test_relational::trigger_has_deleteType():
    assert hasattr(relational::Trigger, "deleteType")
    descriptor = None
    for klass in relational::Trigger.__mro__:
        if "deleteType" in klass.__dict__:
            descriptor = klass.__dict__["deleteType"]
            break
    assert isinstance(descriptor, property)



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(relational::Table)


def test_relational::table_constructor_exists():
    assert callable(relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(relational::Table.__init__)
    params = list(sig.parameters.keys())



def test_relational::constraint_is_not_abstract():
    assert not inspect.isabstract(relational::Constraint)


def test_relational::constraint_constructor_exists():
    assert callable(relational::Constraint.__init__)


def test_relational::constraint_constructor_args():
    sig = inspect.signature(relational::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(relational::Schema.__init__)
    params = list(sig.parameters.keys())



def test_relational::datatype_is_not_abstract():
    assert not inspect.isabstract(relational::DataType)


def test_relational::datatype_constructor_exists():
    assert callable(relational::DataType.__init__)


def test_relational::datatype_constructor_args():
    sig = inspect.signature(relational::DataType.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_relational::sqlobject_is_not_abstract():
    assert not inspect.isabstract(relational::SQLObject)


def test_relational::sqlobject_constructor_exists():
    assert callable(relational::SQLObject.__init__)


def test_relational::sqlobject_constructor_args():
    sig = inspect.signature(relational::SQLObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"

def test_relational::sqlobject_has_label():
    assert hasattr(relational::SQLObject, "label")
    descriptor = None
    for klass in relational::SQLObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_relational::sqlobject_has_description():
    assert hasattr(relational::SQLObject, "description")
    descriptor = None
    for klass in relational::SQLObject.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_relational::enamedelement_is_not_abstract():
    assert not inspect.isabstract(relational::ENamedElement)


def test_relational::enamedelement_constructor_exists():
    assert callable(relational::ENamedElement.__init__)


def test_relational::enamedelement_constructor_args():
    sig = inspect.signature(relational::ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::enamedelement_has_name():
    assert hasattr(relational::ENamedElement, "name")
    descriptor = None
    for klass in relational::ENamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::comment_is_not_abstract():
    assert not inspect.isabstract(relational::Comment)


def test_relational::comment_constructor_exists():
    assert callable(relational::Comment.__init__)


def test_relational::comment_constructor_args():
    sig = inspect.signature(relational::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_relational::comment_has_description():
    assert hasattr(relational::Comment, "description")
    descriptor = None
    for klass in relational::Comment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_referentialactiontype_exists():
    # Check that the Enumeration exists
    assert ReferentialActionType is not None

def test_referentialactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialActionType]
    expected_literals = [
        "CASCADE",
        "NO_ACTION",
        "SET_NULL",
        "RESTRICT",
        "SET_DEFAULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialActionType"

def test_actiontimetype_exists():
    # Check that the Enumeration exists
    assert ActionTimeType is not None

def test_actiontimetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionTimeType]
    expected_literals = [
        "INSTEADOF",
        "BEFORE",
        "AFTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionTimeType"

def test_actiongranularitytype_exists():
    # Check that the Enumeration exists
    assert ActionGranularityType is not None

def test_actiongranularitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionGranularityType]
    expected_literals = [
        "ROW",
        "STATEMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionGranularityType"


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
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
relational::DistinctUserDefinedType_strategy = st.builds(
    relational::DistinctUserDefinedType,
)
DistinctUserDefinedType_strategy = st.builds(
    DistinctUserDefinedType,
)
relational::Domain_strategy = st.builds(
    relational::Domain,
    nullable=
        st.booleans(),
    defaultValue=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
UniqueConstraint_strategy = st.builds(
    UniqueConstraint,
)
relational::PrimaryKey_strategy = st.builds(
    relational::PrimaryKey,
)
ReferenceConstraint_strategy = st.builds(
    ReferenceConstraint,
)
relational::UniqueConstraint_strategy = st.builds(
    relational::UniqueConstraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
relational::TableConstraint_strategy = st.builds(
    relational::TableConstraint,
)
Table_strategy = st.builds(
    Table,
)
relational::BaseTable_strategy = st.builds(
    relational::BaseTable,
)
relational::ForeignKey_strategy = st.builds(
    relational::ForeignKey,
    onUpdate=
        safe_text,
    onDelete=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
relational::Column_strategy = st.builds(
    relational::Column,
    length=
        st.integers(),
    srid=
        safe_text,
    defaultValue=
        safe_text,
    nullable=
        st.booleans()
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
relational::CheckConstraint_strategy = st.builds(
    relational::CheckConstraint,
    searchCondition=
        safe_text
)
relational::ReferenceConstraint_strategy = st.builds(
    relational::ReferenceConstraint,
)
relational::UserDefinedType_strategy = st.builds(
    relational::UserDefinedType,
)
relational::Assertion_strategy = st.builds(
    relational::Assertion,
    searchCondition=
        safe_text
)
SQLObject_strategy = st.builds(
    SQLObject,
)
relational::TypedElement_strategy = st.builds(
    relational::TypedElement,
)
relational::Trigger_strategy = st.builds(
    relational::Trigger,
    oldTable=
        safe_text,
    statementSQL=
        safe_text,
    oldRow=
        safe_text,
    insertType=
        st.booleans(),
    condition=
        safe_text,
    actionGranularity=
        safe_text,
    actionTime=
        safe_text,
    newTable=
        safe_text,
    newRow=
        safe_text,
    updateType=
        st.booleans(),
    deleteType=
        st.booleans()
)
relational::Table_strategy = st.builds(
    relational::Table,
)
relational::Constraint_strategy = st.builds(
    relational::Constraint,
)
relational::Schema_strategy = st.builds(
    relational::Schema,
)
relational::DataType_strategy = st.builds(
    relational::DataType,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
relational::SQLObject_strategy = st.builds(
    relational::SQLObject,
    label=
        safe_text,
    description=
        safe_text
)
relational::ENamedElement_strategy = st.builds(
    relational::ENamedElement,
    name=
        safe_text
)
relational::Comment_strategy = st.builds(
    relational::Comment,
    description=
        safe_text
)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=relational::DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_relational::distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, relational::DistinctUserDefinedType)

@given(instance=DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, DistinctUserDefinedType)

@given(instance=relational::Domain_strategy)
@settings(max_examples=50)
def test_relational::domain_instantiation(instance):
    assert isinstance(instance, relational::Domain)

@given(instance=relational::Domain_strategy)
def test_relational::domain_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=relational::Domain_strategy)
def test_relational::domain_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=relational::Domain_strategy)
def test_relational::domain_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=relational::Domain_strategy)
def test_relational::domain_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UniqueConstraint_strategy)
@settings(max_examples=50)
def test_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, UniqueConstraint)

@given(instance=relational::PrimaryKey_strategy)
@settings(max_examples=50)
def test_relational::primarykey_instantiation(instance):
    assert isinstance(instance, relational::PrimaryKey)

@given(instance=ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_referenceconstraint_instantiation(instance):
    assert isinstance(instance, ReferenceConstraint)

@given(instance=relational::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_relational::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, relational::UniqueConstraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=relational::TableConstraint_strategy)
@settings(max_examples=50)
def test_relational::tableconstraint_instantiation(instance):
    assert isinstance(instance, relational::TableConstraint)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=relational::BaseTable_strategy)
@settings(max_examples=50)
def test_relational::basetable_instantiation(instance):
    assert isinstance(instance, relational::BaseTable)

@given(instance=relational::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::foreignkey_instantiation(instance):
    assert isinstance(instance, relational::ForeignKey)

@given(instance=relational::ForeignKey_strategy)
def test_relational::foreignkey_onUpdate_type(instance):
    assert isinstance(instance.onUpdate, str)


@given(instance=relational::ForeignKey_strategy)
def test_relational::foreignkey_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original

@given(instance=relational::ForeignKey_strategy)
def test_relational::foreignkey_onDelete_type(instance):
    assert isinstance(instance.onDelete, str)


@given(instance=relational::ForeignKey_strategy)
def test_relational::foreignkey_onDelete_setter(instance):
    original = instance.onDelete
    instance.onDelete = original
    assert instance.onDelete == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, relational::Column)

@given(instance=relational::Column_strategy)
def test_relational::column_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=relational::Column_strategy)
def test_relational::column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=relational::Column_strategy)
def test_relational::column_srid_type(instance):
    assert isinstance(instance.srid, str)


@given(instance=relational::Column_strategy)
def test_relational::column_srid_setter(instance):
    original = instance.srid
    instance.srid = original
    assert instance.srid == original

@given(instance=relational::Column_strategy)
def test_relational::column_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=relational::Column_strategy)
def test_relational::column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=relational::Column_strategy)
def test_relational::column_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=relational::Column_strategy)
def test_relational::column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=relational::CheckConstraint_strategy)
@settings(max_examples=50)
def test_relational::checkconstraint_instantiation(instance):
    assert isinstance(instance, relational::CheckConstraint)

@given(instance=relational::CheckConstraint_strategy)
def test_relational::checkconstraint_searchCondition_type(instance):
    assert isinstance(instance.searchCondition, str)


@given(instance=relational::CheckConstraint_strategy)
def test_relational::checkconstraint_searchCondition_setter(instance):
    original = instance.searchCondition
    instance.searchCondition = original
    assert instance.searchCondition == original

@given(instance=relational::ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_relational::referenceconstraint_instantiation(instance):
    assert isinstance(instance, relational::ReferenceConstraint)

@given(instance=relational::UserDefinedType_strategy)
@settings(max_examples=50)
def test_relational::userdefinedtype_instantiation(instance):
    assert isinstance(instance, relational::UserDefinedType)

@given(instance=relational::Assertion_strategy)
@settings(max_examples=50)
def test_relational::assertion_instantiation(instance):
    assert isinstance(instance, relational::Assertion)

@given(instance=relational::Assertion_strategy)
def test_relational::assertion_searchCondition_type(instance):
    assert isinstance(instance.searchCondition, str)


@given(instance=relational::Assertion_strategy)
def test_relational::assertion_searchCondition_setter(instance):
    original = instance.searchCondition
    instance.searchCondition = original
    assert instance.searchCondition == original

@given(instance=SQLObject_strategy)
@settings(max_examples=50)
def test_sqlobject_instantiation(instance):
    assert isinstance(instance, SQLObject)

@given(instance=relational::TypedElement_strategy)
@settings(max_examples=50)
def test_relational::typedelement_instantiation(instance):
    assert isinstance(instance, relational::TypedElement)

@given(instance=relational::Trigger_strategy)
@settings(max_examples=50)
def test_relational::trigger_instantiation(instance):
    assert isinstance(instance, relational::Trigger)

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_oldTable_type(instance):
    assert isinstance(instance.oldTable, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_oldTable_setter(instance):
    original = instance.oldTable
    instance.oldTable = original
    assert instance.oldTable == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_statementSQL_type(instance):
    assert isinstance(instance.statementSQL, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_statementSQL_setter(instance):
    original = instance.statementSQL
    instance.statementSQL = original
    assert instance.statementSQL == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_oldRow_type(instance):
    assert isinstance(instance.oldRow, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_oldRow_setter(instance):
    original = instance.oldRow
    instance.oldRow = original
    assert instance.oldRow == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_insertType_type(instance):
    assert isinstance(instance.insertType, bool)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_insertType_setter(instance):
    original = instance.insertType
    instance.insertType = original
    assert instance.insertType == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_actionGranularity_type(instance):
    assert isinstance(instance.actionGranularity, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_actionGranularity_setter(instance):
    original = instance.actionGranularity
    instance.actionGranularity = original
    assert instance.actionGranularity == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_actionTime_type(instance):
    assert isinstance(instance.actionTime, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_newTable_type(instance):
    assert isinstance(instance.newTable, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_newTable_setter(instance):
    original = instance.newTable
    instance.newTable = original
    assert instance.newTable == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_newRow_type(instance):
    assert isinstance(instance.newRow, str)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_newRow_setter(instance):
    original = instance.newRow
    instance.newRow = original
    assert instance.newRow == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_updateType_type(instance):
    assert isinstance(instance.updateType, bool)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_updateType_setter(instance):
    original = instance.updateType
    instance.updateType = original
    assert instance.updateType == original

@given(instance=relational::Trigger_strategy)
def test_relational::trigger_deleteType_type(instance):
    assert isinstance(instance.deleteType, bool)


@given(instance=relational::Trigger_strategy)
def test_relational::trigger_deleteType_setter(instance):
    original = instance.deleteType
    instance.deleteType = original
    assert instance.deleteType == original

@given(instance=relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, relational::Table)

@given(instance=relational::Constraint_strategy)
@settings(max_examples=50)
def test_relational::constraint_instantiation(instance):
    assert isinstance(instance, relational::Constraint)

@given(instance=relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, relational::Schema)

@given(instance=relational::DataType_strategy)
@settings(max_examples=50)
def test_relational::datatype_instantiation(instance):
    assert isinstance(instance, relational::DataType)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=relational::SQLObject_strategy)
@settings(max_examples=50)
def test_relational::sqlobject_instantiation(instance):
    assert isinstance(instance, relational::SQLObject)

@given(instance=relational::SQLObject_strategy)
def test_relational::sqlobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=relational::SQLObject_strategy)
def test_relational::sqlobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=relational::SQLObject_strategy)
def test_relational::sqlobject_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=relational::SQLObject_strategy)
def test_relational::sqlobject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=relational::ENamedElement_strategy)
@settings(max_examples=50)
def test_relational::enamedelement_instantiation(instance):
    assert isinstance(instance, relational::ENamedElement)

@given(instance=relational::ENamedElement_strategy)
def test_relational::enamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::ENamedElement_strategy)
def test_relational::enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Comment_strategy)
@settings(max_examples=50)
def test_relational::comment_instantiation(instance):
    assert isinstance(instance, relational::Comment)

@given(instance=relational::Comment_strategy)
def test_relational::comment_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=relational::Comment_strategy)
def test_relational::comment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
