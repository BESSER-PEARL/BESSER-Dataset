import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UserDefinedType,
    relational_DistinctUserDefinedType,
    DistinctUserDefinedType,
    relational_Domain,
    DataType,
    UniqueConstraint,
    relational_PrimaryKey,
    ReferenceConstraint,
    relational_UniqueConstraint,
    Constraint,
    relational_TableConstraint,
    Table,
    relational_BaseTable,
    relational_ForeignKey,
    TypedElement,
    relational_Column,
    TableConstraint,
    relational_ReferenceConstraint,
    relational_CheckConstraint,
    relational_UserDefinedType,
    relational_Assertion,
    SQLObject,
    relational_Constraint,
    relational_Table,
    relational_Schema,
    relational_Trigger,
    relational_TypedElement,
    relational_DataType,
    ENamedElement,
    relational_SQLObject,
    relational_ENamedElement,
    relational_Comment,
    ActionGranularityType,
    ActionTimeType,
    ReferentialActionType,
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



def test_relational_distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(relational_DistinctUserDefinedType)


def test_relational_distinctuserdefinedtype_constructor_exists():
    assert callable(relational_DistinctUserDefinedType.__init__)


def test_relational_distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(relational_DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_distinctuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(DistinctUserDefinedType)


def test_distinctuserdefinedtype_constructor_exists():
    assert callable(DistinctUserDefinedType.__init__)


def test_distinctuserdefinedtype_constructor_args():
    sig = inspect.signature(DistinctUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_relational_domain_is_not_abstract():
    assert not inspect.isabstract(relational_Domain)


def test_relational_domain_constructor_exists():
    assert callable(relational_Domain.__init__)


def test_relational_domain_constructor_args():
    sig = inspect.signature(relational_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_relational_domain_has_nullable():
    assert hasattr(relational_Domain, "nullable")
    descriptor = None
    for klass in relational_Domain.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_relational_domain_has_defaultValue():
    assert hasattr(relational_Domain, "defaultValue")
    descriptor = None
    for klass in relational_Domain.__mro__:
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



def test_relational_primarykey_is_not_abstract():
    assert not inspect.isabstract(relational_PrimaryKey)


def test_relational_primarykey_constructor_exists():
    assert callable(relational_PrimaryKey.__init__)


def test_relational_primarykey_constructor_args():
    sig = inspect.signature(relational_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(ReferenceConstraint)


def test_referenceconstraint_constructor_exists():
    assert callable(ReferenceConstraint.__init__)


def test_referenceconstraint_constructor_args():
    sig = inspect.signature(ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(relational_UniqueConstraint)


def test_relational_uniqueconstraint_constructor_exists():
    assert callable(relational_UniqueConstraint.__init__)


def test_relational_uniqueconstraint_constructor_args():
    sig = inspect.signature(relational_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_relational_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(relational_TableConstraint)


def test_relational_tableconstraint_constructor_exists():
    assert callable(relational_TableConstraint.__init__)


def test_relational_tableconstraint_constructor_args():
    sig = inspect.signature(relational_TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_relational_basetable_is_not_abstract():
    assert not inspect.isabstract(relational_BaseTable)


def test_relational_basetable_constructor_exists():
    assert callable(relational_BaseTable.__init__)


def test_relational_basetable_constructor_args():
    sig = inspect.signature(relational_BaseTable.__init__)
    params = list(sig.parameters.keys())



def test_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational_ForeignKey)


def test_relational_foreignkey_constructor_exists():
    assert callable(relational_ForeignKey.__init__)


def test_relational_foreignkey_constructor_args():
    sig = inspect.signature(relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "onDelete" in params, "Missing parameter 'onDelete'"
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"

def test_relational_foreignkey_has_onDelete():
    assert hasattr(relational_ForeignKey, "onDelete")
    descriptor = None
    for klass in relational_ForeignKey.__mro__:
        if "onDelete" in klass.__dict__:
            descriptor = klass.__dict__["onDelete"]
            break
    assert isinstance(descriptor, property)

def test_relational_foreignkey_has_onUpdate():
    assert hasattr(relational_ForeignKey, "onUpdate")
    descriptor = None
    for klass in relational_ForeignKey.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(relational_Column)


def test_relational_column_constructor_exists():
    assert callable(relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(relational_Column.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "srid" in params, "Missing parameter 'srid'"

def test_relational_column_has_length():
    assert hasattr(relational_Column, "length")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_nullable():
    assert hasattr(relational_Column, "nullable")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_defaultValue():
    assert hasattr(relational_Column, "defaultValue")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_srid():
    assert hasattr(relational_Column, "srid")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "srid" in klass.__dict__:
            descriptor = klass.__dict__["srid"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational_referenceconstraint_is_not_abstract():
    assert not inspect.isabstract(relational_ReferenceConstraint)


def test_relational_referenceconstraint_constructor_exists():
    assert callable(relational_ReferenceConstraint.__init__)


def test_relational_referenceconstraint_constructor_args():
    sig = inspect.signature(relational_ReferenceConstraint.__init__)
    params = list(sig.parameters.keys())



def test_relational_checkconstraint_is_not_abstract():
    assert not inspect.isabstract(relational_CheckConstraint)


def test_relational_checkconstraint_constructor_exists():
    assert callable(relational_CheckConstraint.__init__)


def test_relational_checkconstraint_constructor_args():
    sig = inspect.signature(relational_CheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "searchCondition" in params, "Missing parameter 'searchCondition'"

def test_relational_checkconstraint_has_searchCondition():
    assert hasattr(relational_CheckConstraint, "searchCondition")
    descriptor = None
    for klass in relational_CheckConstraint.__mro__:
        if "searchCondition" in klass.__dict__:
            descriptor = klass.__dict__["searchCondition"]
            break
    assert isinstance(descriptor, property)



def test_relational_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(relational_UserDefinedType)


def test_relational_userdefinedtype_constructor_exists():
    assert callable(relational_UserDefinedType.__init__)


def test_relational_userdefinedtype_constructor_args():
    sig = inspect.signature(relational_UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_relational_assertion_is_not_abstract():
    assert not inspect.isabstract(relational_Assertion)


def test_relational_assertion_constructor_exists():
    assert callable(relational_Assertion.__init__)


def test_relational_assertion_constructor_args():
    sig = inspect.signature(relational_Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "searchCondition" in params, "Missing parameter 'searchCondition'"

def test_relational_assertion_has_searchCondition():
    assert hasattr(relational_Assertion, "searchCondition")
    descriptor = None
    for klass in relational_Assertion.__mro__:
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



def test_relational_constraint_is_not_abstract():
    assert not inspect.isabstract(relational_Constraint)


def test_relational_constraint_constructor_exists():
    assert callable(relational_Constraint.__init__)


def test_relational_constraint_constructor_args():
    sig = inspect.signature(relational_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(relational_Table)


def test_relational_table_constructor_exists():
    assert callable(relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(relational_Table.__init__)
    params = list(sig.parameters.keys())



def test_relational_schema_is_not_abstract():
    assert not inspect.isabstract(relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(relational_Schema.__init__)
    params = list(sig.parameters.keys())



def test_relational_trigger_is_not_abstract():
    assert not inspect.isabstract(relational_Trigger)


def test_relational_trigger_constructor_exists():
    assert callable(relational_Trigger.__init__)


def test_relational_trigger_constructor_args():
    sig = inspect.signature(relational_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "deleteType" in params, "Missing parameter 'deleteType'"
    assert "actionGranularity" in params, "Missing parameter 'actionGranularity'"
    assert "newRow" in params, "Missing parameter 'newRow'"
    assert "updateType" in params, "Missing parameter 'updateType'"
    assert "condition" in params, "Missing parameter 'condition'"
    assert "actionTime" in params, "Missing parameter 'actionTime'"
    assert "newTable" in params, "Missing parameter 'newTable'"
    assert "insertType" in params, "Missing parameter 'insertType'"
    assert "oldTable" in params, "Missing parameter 'oldTable'"
    assert "statementSQL" in params, "Missing parameter 'statementSQL'"
    assert "oldRow" in params, "Missing parameter 'oldRow'"

def test_relational_trigger_has_deleteType():
    assert hasattr(relational_Trigger, "deleteType")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "deleteType" in klass.__dict__:
            descriptor = klass.__dict__["deleteType"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_actionGranularity():
    assert hasattr(relational_Trigger, "actionGranularity")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "actionGranularity" in klass.__dict__:
            descriptor = klass.__dict__["actionGranularity"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_newRow():
    assert hasattr(relational_Trigger, "newRow")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "newRow" in klass.__dict__:
            descriptor = klass.__dict__["newRow"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_updateType():
    assert hasattr(relational_Trigger, "updateType")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "updateType" in klass.__dict__:
            descriptor = klass.__dict__["updateType"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_condition():
    assert hasattr(relational_Trigger, "condition")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_actionTime():
    assert hasattr(relational_Trigger, "actionTime")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "actionTime" in klass.__dict__:
            descriptor = klass.__dict__["actionTime"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_newTable():
    assert hasattr(relational_Trigger, "newTable")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "newTable" in klass.__dict__:
            descriptor = klass.__dict__["newTable"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_insertType():
    assert hasattr(relational_Trigger, "insertType")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "insertType" in klass.__dict__:
            descriptor = klass.__dict__["insertType"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_oldTable():
    assert hasattr(relational_Trigger, "oldTable")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "oldTable" in klass.__dict__:
            descriptor = klass.__dict__["oldTable"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_statementSQL():
    assert hasattr(relational_Trigger, "statementSQL")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "statementSQL" in klass.__dict__:
            descriptor = klass.__dict__["statementSQL"]
            break
    assert isinstance(descriptor, property)

def test_relational_trigger_has_oldRow():
    assert hasattr(relational_Trigger, "oldRow")
    descriptor = None
    for klass in relational_Trigger.__mro__:
        if "oldRow" in klass.__dict__:
            descriptor = klass.__dict__["oldRow"]
            break
    assert isinstance(descriptor, property)



def test_relational_typedelement_is_not_abstract():
    assert not inspect.isabstract(relational_TypedElement)


def test_relational_typedelement_constructor_exists():
    assert callable(relational_TypedElement.__init__)


def test_relational_typedelement_constructor_args():
    sig = inspect.signature(relational_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_relational_datatype_is_not_abstract():
    assert not inspect.isabstract(relational_DataType)


def test_relational_datatype_constructor_exists():
    assert callable(relational_DataType.__init__)


def test_relational_datatype_constructor_args():
    sig = inspect.signature(relational_DataType.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_relational_sqlobject_is_not_abstract():
    assert not inspect.isabstract(relational_SQLObject)


def test_relational_sqlobject_constructor_exists():
    assert callable(relational_SQLObject.__init__)


def test_relational_sqlobject_constructor_args():
    sig = inspect.signature(relational_SQLObject.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"

def test_relational_sqlobject_has_label():
    assert hasattr(relational_SQLObject, "label")
    descriptor = None
    for klass in relational_SQLObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_relational_sqlobject_has_description():
    assert hasattr(relational_SQLObject, "description")
    descriptor = None
    for klass in relational_SQLObject.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_relational_enamedelement_is_not_abstract():
    assert not inspect.isabstract(relational_ENamedElement)


def test_relational_enamedelement_constructor_exists():
    assert callable(relational_ENamedElement.__init__)


def test_relational_enamedelement_constructor_args():
    sig = inspect.signature(relational_ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_enamedelement_has_name():
    assert hasattr(relational_ENamedElement, "name")
    descriptor = None
    for klass in relational_ENamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_comment_is_not_abstract():
    assert not inspect.isabstract(relational_Comment)


def test_relational_comment_constructor_exists():
    assert callable(relational_Comment.__init__)


def test_relational_comment_constructor_args():
    sig = inspect.signature(relational_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_relational_comment_has_description():
    assert hasattr(relational_Comment, "description")
    descriptor = None
    for klass in relational_Comment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_actiongranularitytype_exists():
    # Check that the Enumeration exists
    assert ActionGranularityType is not None

def test_actiongranularitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionGranularityType]
    expected_literals = [
        "STATEMENT",
        "ROW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionGranularityType"

def test_actiontimetype_exists():
    # Check that the Enumeration exists
    assert ActionTimeType is not None

def test_actiontimetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionTimeType]
    expected_literals = [
        "AFTER",
        "INSTEADOF",
        "BEFORE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionTimeType"

def test_referentialactiontype_exists():
    # Check that the Enumeration exists
    assert ReferentialActionType is not None

def test_referentialactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferentialActionType]
    expected_literals = [
        "SET_DEFAULT",
        "NO_ACTION",
        "SET_NULL",
        "RESTRICT",
        "CASCADE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferentialActionType"


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
relational_DistinctUserDefinedType_strategy = st.builds(
    relational_DistinctUserDefinedType,
)
DistinctUserDefinedType_strategy = st.builds(
    DistinctUserDefinedType,
)
relational_Domain_strategy = st.builds(
    relational_Domain,
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
relational_PrimaryKey_strategy = st.builds(
    relational_PrimaryKey,
)
ReferenceConstraint_strategy = st.builds(
    ReferenceConstraint,
)
relational_UniqueConstraint_strategy = st.builds(
    relational_UniqueConstraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
relational_TableConstraint_strategy = st.builds(
    relational_TableConstraint,
)
Table_strategy = st.builds(
    Table,
)
relational_BaseTable_strategy = st.builds(
    relational_BaseTable,
)
relational_ForeignKey_strategy = st.builds(
    relational_ForeignKey,
    onDelete=
        safe_text,
    onUpdate=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
relational_Column_strategy = st.builds(
    relational_Column,
    length=
        st.integers(),
    nullable=
        st.booleans(),
    defaultValue=
        safe_text,
    srid=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
relational_ReferenceConstraint_strategy = st.builds(
    relational_ReferenceConstraint,
)
relational_CheckConstraint_strategy = st.builds(
    relational_CheckConstraint,
    searchCondition=
        safe_text
)
relational_UserDefinedType_strategy = st.builds(
    relational_UserDefinedType,
)
relational_Assertion_strategy = st.builds(
    relational_Assertion,
    searchCondition=
        safe_text
)
SQLObject_strategy = st.builds(
    SQLObject,
)
relational_Constraint_strategy = st.builds(
    relational_Constraint,
)
relational_Table_strategy = st.builds(
    relational_Table,
)
relational_Schema_strategy = st.builds(
    relational_Schema,
)
relational_Trigger_strategy = st.builds(
    relational_Trigger,
    deleteType=
        st.booleans(),
    actionGranularity=
        safe_text,
    newRow=
        safe_text,
    updateType=
        st.booleans(),
    condition=
        safe_text,
    actionTime=
        safe_text,
    newTable=
        safe_text,
    insertType=
        st.booleans(),
    oldTable=
        safe_text,
    statementSQL=
        safe_text,
    oldRow=
        safe_text
)
relational_TypedElement_strategy = st.builds(
    relational_TypedElement,
)
relational_DataType_strategy = st.builds(
    relational_DataType,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
relational_SQLObject_strategy = st.builds(
    relational_SQLObject,
    label=
        safe_text,
    description=
        safe_text
)
relational_ENamedElement_strategy = st.builds(
    relational_ENamedElement,
    name=
        safe_text
)
relational_Comment_strategy = st.builds(
    relational_Comment,
    description=
        safe_text
)

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=relational_DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_relational_distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, relational_DistinctUserDefinedType)

@given(instance=DistinctUserDefinedType_strategy)
@settings(max_examples=50)
def test_distinctuserdefinedtype_instantiation(instance):
    assert isinstance(instance, DistinctUserDefinedType)

@given(instance=relational_Domain_strategy)
@settings(max_examples=50)
def test_relational_domain_instantiation(instance):
    assert isinstance(instance, relational_Domain)



@given(instance=relational_Domain_strategy)
def test_relational_domain_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=relational_Domain_strategy)
def test_relational_domain_defaultValue_setter(instance):
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

@given(instance=relational_PrimaryKey_strategy)
@settings(max_examples=50)
def test_relational_primarykey_instantiation(instance):
    assert isinstance(instance, relational_PrimaryKey)

@given(instance=ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_referenceconstraint_instantiation(instance):
    assert isinstance(instance, ReferenceConstraint)

@given(instance=relational_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_relational_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, relational_UniqueConstraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=relational_TableConstraint_strategy)
@settings(max_examples=50)
def test_relational_tableconstraint_instantiation(instance):
    assert isinstance(instance, relational_TableConstraint)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=relational_BaseTable_strategy)
@settings(max_examples=50)
def test_relational_basetable_instantiation(instance):
    assert isinstance(instance, relational_BaseTable)

@given(instance=relational_ForeignKey_strategy)
@settings(max_examples=50)
def test_relational_foreignkey_instantiation(instance):
    assert isinstance(instance, relational_ForeignKey)



@given(instance=relational_ForeignKey_strategy)
def test_relational_foreignkey_onDelete_setter(instance):
    original = instance.onDelete
    instance.onDelete = original
    assert instance.onDelete == original



@given(instance=relational_ForeignKey_strategy)
def test_relational_foreignkey_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, relational_Column)



@given(instance=relational_Column_strategy)
def test_relational_column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=relational_Column_strategy)
def test_relational_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=relational_Column_strategy)
def test_relational_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=relational_Column_strategy)
def test_relational_column_srid_setter(instance):
    original = instance.srid
    instance.srid = original
    assert instance.srid == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=relational_ReferenceConstraint_strategy)
@settings(max_examples=50)
def test_relational_referenceconstraint_instantiation(instance):
    assert isinstance(instance, relational_ReferenceConstraint)

@given(instance=relational_CheckConstraint_strategy)
@settings(max_examples=50)
def test_relational_checkconstraint_instantiation(instance):
    assert isinstance(instance, relational_CheckConstraint)



@given(instance=relational_CheckConstraint_strategy)
def test_relational_checkconstraint_searchCondition_setter(instance):
    original = instance.searchCondition
    instance.searchCondition = original
    assert instance.searchCondition == original

@given(instance=relational_UserDefinedType_strategy)
@settings(max_examples=50)
def test_relational_userdefinedtype_instantiation(instance):
    assert isinstance(instance, relational_UserDefinedType)

@given(instance=relational_Assertion_strategy)
@settings(max_examples=50)
def test_relational_assertion_instantiation(instance):
    assert isinstance(instance, relational_Assertion)



@given(instance=relational_Assertion_strategy)
def test_relational_assertion_searchCondition_setter(instance):
    original = instance.searchCondition
    instance.searchCondition = original
    assert instance.searchCondition == original

@given(instance=SQLObject_strategy)
@settings(max_examples=50)
def test_sqlobject_instantiation(instance):
    assert isinstance(instance, SQLObject)

@given(instance=relational_Constraint_strategy)
@settings(max_examples=50)
def test_relational_constraint_instantiation(instance):
    assert isinstance(instance, relational_Constraint)

@given(instance=relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, relational_Table)

@given(instance=relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, relational_Schema)

@given(instance=relational_Trigger_strategy)
@settings(max_examples=50)
def test_relational_trigger_instantiation(instance):
    assert isinstance(instance, relational_Trigger)



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_deleteType_setter(instance):
    original = instance.deleteType
    instance.deleteType = original
    assert instance.deleteType == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_actionGranularity_setter(instance):
    original = instance.actionGranularity
    instance.actionGranularity = original
    assert instance.actionGranularity == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_newRow_setter(instance):
    original = instance.newRow
    instance.newRow = original
    assert instance.newRow == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_updateType_setter(instance):
    original = instance.updateType
    instance.updateType = original
    assert instance.updateType == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_actionTime_setter(instance):
    original = instance.actionTime
    instance.actionTime = original
    assert instance.actionTime == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_newTable_setter(instance):
    original = instance.newTable
    instance.newTable = original
    assert instance.newTable == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_insertType_setter(instance):
    original = instance.insertType
    instance.insertType = original
    assert instance.insertType == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_oldTable_setter(instance):
    original = instance.oldTable
    instance.oldTable = original
    assert instance.oldTable == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_statementSQL_setter(instance):
    original = instance.statementSQL
    instance.statementSQL = original
    assert instance.statementSQL == original



@given(instance=relational_Trigger_strategy)
def test_relational_trigger_oldRow_setter(instance):
    original = instance.oldRow
    instance.oldRow = original
    assert instance.oldRow == original

@given(instance=relational_TypedElement_strategy)
@settings(max_examples=50)
def test_relational_typedelement_instantiation(instance):
    assert isinstance(instance, relational_TypedElement)

@given(instance=relational_DataType_strategy)
@settings(max_examples=50)
def test_relational_datatype_instantiation(instance):
    assert isinstance(instance, relational_DataType)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=relational_SQLObject_strategy)
@settings(max_examples=50)
def test_relational_sqlobject_instantiation(instance):
    assert isinstance(instance, relational_SQLObject)



@given(instance=relational_SQLObject_strategy)
def test_relational_sqlobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=relational_SQLObject_strategy)
def test_relational_sqlobject_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=relational_ENamedElement_strategy)
@settings(max_examples=50)
def test_relational_enamedelement_instantiation(instance):
    assert isinstance(instance, relational_ENamedElement)



@given(instance=relational_ENamedElement_strategy)
def test_relational_enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_Comment_strategy)
@settings(max_examples=50)
def test_relational_comment_instantiation(instance):
    assert isinstance(instance, relational_Comment)



@given(instance=relational_Comment_strategy)
def test_relational_comment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
