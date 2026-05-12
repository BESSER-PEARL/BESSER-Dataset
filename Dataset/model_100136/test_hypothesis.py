import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dbdefinition::PrivilegeDefinition,
    dbdefinition::FieldQualifierDefinition,
    dbdefinition::ConstructedDataTypeDefinition,
    dbdefinition::PrivilegedElementDefinition,
    dbdefinition::DebuggerDefinition,
    dbdefinition::ViewDefinition,
    dbdefinition::SchemaDefinition,
    dbdefinition::SequenceDefinition,
    dbdefinition::TableDefinition,
    dbdefinition::IndexDefinition,
    dbdefinition::ExtendedDefinition,
    dbdefinition::ConstraintDefinition,
    dbdefinition::ColumnDefinition,
    dbdefinition::TriggerDefinition,
    dbdefinition::StoredProcedureDefinition,
    dbdefinition::TableSpaceDefinition,
    dbdefinition::NicknameDefinition,
    dbdefinition::SQLSyntaxDefinition,
    dbdefinition::QueryDefinition,
    dbdefinition::UserDefinedTypeDefinition,
    dbdefinition::PredefinedDataTypeDefinition,
    dbdefinition::DatabaseVendorDefinition,
    LengthUnit,
    PercentFreeTerminology,
    ParentDeleteDRIRuleType,
    TableSpaceType,
    ProcedureType,
    CheckOption,
    LanguageType,
    ParameterStyle,
    ParentUpdateDRIRuleType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbdefinition::privilegedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::PrivilegeDefinition)


def test_dbdefinition::privilegedefinition_constructor_exists():
    assert callable(dbdefinition::PrivilegeDefinition.__init__)


def test_dbdefinition::privilegedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::PrivilegeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdefinition::privilegedefinition_has_name():
    assert hasattr(dbdefinition::PrivilegeDefinition, "name")
    descriptor = None
    for klass in dbdefinition::PrivilegeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::fieldqualifierdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::FieldQualifierDefinition)


def test_dbdefinition::fieldqualifierdefinition_constructor_exists():
    assert callable(dbdefinition::FieldQualifierDefinition.__init__)


def test_dbdefinition::fieldqualifierdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::FieldQualifierDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultScale" in params, "Missing parameter 'defaultScale'"
    assert "defaultPrecision" in params, "Missing parameter 'defaultPrecision'"
    assert "precisionSupported" in params, "Missing parameter 'precisionSupported'"
    assert "scaleSupported" in params, "Missing parameter 'scaleSupported'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maximumScale" in params, "Missing parameter 'maximumScale'"
    assert "maximumPrecision" in params, "Missing parameter 'maximumPrecision'"

def test_dbdefinition::fieldqualifierdefinition_has_defaultScale():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "defaultScale")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "defaultScale" in klass.__dict__:
            descriptor = klass.__dict__["defaultScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::fieldqualifierdefinition_has_defaultPrecision():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "defaultPrecision")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "defaultPrecision" in klass.__dict__:
            descriptor = klass.__dict__["defaultPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::fieldqualifierdefinition_has_precisionSupported():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "precisionSupported")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "precisionSupported" in klass.__dict__:
            descriptor = klass.__dict__["precisionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::fieldqualifierdefinition_has_scaleSupported():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "scaleSupported")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "scaleSupported" in klass.__dict__:
            descriptor = klass.__dict__["scaleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::fieldqualifierdefinition_has_name():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "name")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::fieldqualifierdefinition_has_maximumScale():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "maximumScale")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "maximumScale" in klass.__dict__:
            descriptor = klass.__dict__["maximumScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::fieldqualifierdefinition_has_maximumPrecision():
    assert hasattr(dbdefinition::FieldQualifierDefinition, "maximumPrecision")
    descriptor = None
    for klass in dbdefinition::FieldQualifierDefinition.__mro__:
        if "maximumPrecision" in klass.__dict__:
            descriptor = klass.__dict__["maximumPrecision"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::constructeddatatypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::ConstructedDataTypeDefinition)


def test_dbdefinition::constructeddatatypedefinition_constructor_exists():
    assert callable(dbdefinition::ConstructedDataTypeDefinition.__init__)


def test_dbdefinition::constructeddatatypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::ConstructedDataTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "rowDatatypeSupported" in params, "Missing parameter 'rowDatatypeSupported'"
    assert "referenceDatatypeSupported" in params, "Missing parameter 'referenceDatatypeSupported'"
    assert "cursorDatatypeSupported" in params, "Missing parameter 'cursorDatatypeSupported'"
    assert "multisetDatatypeSupported" in params, "Missing parameter 'multisetDatatypeSupported'"
    assert "arrayDatatypeSupported" in params, "Missing parameter 'arrayDatatypeSupported'"

def test_dbdefinition::constructeddatatypedefinition_has_rowDatatypeSupported():
    assert hasattr(dbdefinition::ConstructedDataTypeDefinition, "rowDatatypeSupported")
    descriptor = None
    for klass in dbdefinition::ConstructedDataTypeDefinition.__mro__:
        if "rowDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["rowDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constructeddatatypedefinition_has_referenceDatatypeSupported():
    assert hasattr(dbdefinition::ConstructedDataTypeDefinition, "referenceDatatypeSupported")
    descriptor = None
    for klass in dbdefinition::ConstructedDataTypeDefinition.__mro__:
        if "referenceDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["referenceDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constructeddatatypedefinition_has_cursorDatatypeSupported():
    assert hasattr(dbdefinition::ConstructedDataTypeDefinition, "cursorDatatypeSupported")
    descriptor = None
    for klass in dbdefinition::ConstructedDataTypeDefinition.__mro__:
        if "cursorDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["cursorDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constructeddatatypedefinition_has_multisetDatatypeSupported():
    assert hasattr(dbdefinition::ConstructedDataTypeDefinition, "multisetDatatypeSupported")
    descriptor = None
    for klass in dbdefinition::ConstructedDataTypeDefinition.__mro__:
        if "multisetDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["multisetDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constructeddatatypedefinition_has_arrayDatatypeSupported():
    assert hasattr(dbdefinition::ConstructedDataTypeDefinition, "arrayDatatypeSupported")
    descriptor = None
    for klass in dbdefinition::ConstructedDataTypeDefinition.__mro__:
        if "arrayDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["arrayDatatypeSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::privilegedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::PrivilegedElementDefinition)


def test_dbdefinition::privilegedelementdefinition_constructor_exists():
    assert callable(dbdefinition::PrivilegedElementDefinition.__init__)


def test_dbdefinition::privilegedelementdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::PrivilegedElementDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdefinition::privilegedelementdefinition_has_name():
    assert hasattr(dbdefinition::PrivilegedElementDefinition, "name")
    descriptor = None
    for klass in dbdefinition::PrivilegedElementDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::debuggerdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::DebuggerDefinition)


def test_dbdefinition::debuggerdefinition_constructor_exists():
    assert callable(dbdefinition::DebuggerDefinition.__init__)


def test_dbdefinition::debuggerdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::DebuggerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "conditionSupported" in params, "Missing parameter 'conditionSupported'"

def test_dbdefinition::debuggerdefinition_has_conditionSupported():
    assert hasattr(dbdefinition::DebuggerDefinition, "conditionSupported")
    descriptor = None
    for klass in dbdefinition::DebuggerDefinition.__mro__:
        if "conditionSupported" in klass.__dict__:
            descriptor = klass.__dict__["conditionSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::viewdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::ViewDefinition)


def test_dbdefinition::viewdefinition_constructor_exists():
    assert callable(dbdefinition::ViewDefinition.__init__)


def test_dbdefinition::viewdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::ViewDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "checkOptionSupported" in params, "Missing parameter 'checkOptionSupported'"
    assert "checkOptionLevelsSupported" in params, "Missing parameter 'checkOptionLevelsSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "indexSupported" in params, "Missing parameter 'indexSupported'"

def test_dbdefinition::viewdefinition_has_checkOptionSupported():
    assert hasattr(dbdefinition::ViewDefinition, "checkOptionSupported")
    descriptor = None
    for klass in dbdefinition::ViewDefinition.__mro__:
        if "checkOptionSupported" in klass.__dict__:
            descriptor = klass.__dict__["checkOptionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::viewdefinition_has_checkOptionLevelsSupported():
    assert hasattr(dbdefinition::ViewDefinition, "checkOptionLevelsSupported")
    descriptor = None
    for klass in dbdefinition::ViewDefinition.__mro__:
        if "checkOptionLevelsSupported" in klass.__dict__:
            descriptor = klass.__dict__["checkOptionLevelsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::viewdefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::ViewDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::ViewDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::viewdefinition_has_indexSupported():
    assert hasattr(dbdefinition::ViewDefinition, "indexSupported")
    descriptor = None
    for klass in dbdefinition::ViewDefinition.__mro__:
        if "indexSupported" in klass.__dict__:
            descriptor = klass.__dict__["indexSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::schemadefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::SchemaDefinition)


def test_dbdefinition::schemadefinition_constructor_exists():
    assert callable(dbdefinition::SchemaDefinition.__init__)


def test_dbdefinition::schemadefinition_constructor_args():
    sig = inspect.signature(dbdefinition::SchemaDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"

def test_dbdefinition::schemadefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::SchemaDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::SchemaDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::sequencedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::SequenceDefinition)


def test_dbdefinition::sequencedefinition_constructor_exists():
    assert callable(dbdefinition::SequenceDefinition.__init__)


def test_dbdefinition::sequencedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::SequenceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "noCacheString" in params, "Missing parameter 'noCacheString'"
    assert "noMaximumValueString" in params, "Missing parameter 'noMaximumValueString'"
    assert "cacheSupported" in params, "Missing parameter 'cacheSupported'"
    assert "noMinimumValueString" in params, "Missing parameter 'noMinimumValueString'"
    assert "typeEnumerationSupported" in params, "Missing parameter 'typeEnumerationSupported'"
    assert "orderSupported" in params, "Missing parameter 'orderSupported'"
    assert "cacheDefaultValue" in params, "Missing parameter 'cacheDefaultValue'"

def test_dbdefinition::sequencedefinition_has_noCacheString():
    assert hasattr(dbdefinition::SequenceDefinition, "noCacheString")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "noCacheString" in klass.__dict__:
            descriptor = klass.__dict__["noCacheString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sequencedefinition_has_noMaximumValueString():
    assert hasattr(dbdefinition::SequenceDefinition, "noMaximumValueString")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "noMaximumValueString" in klass.__dict__:
            descriptor = klass.__dict__["noMaximumValueString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sequencedefinition_has_cacheSupported():
    assert hasattr(dbdefinition::SequenceDefinition, "cacheSupported")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "cacheSupported" in klass.__dict__:
            descriptor = klass.__dict__["cacheSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sequencedefinition_has_noMinimumValueString():
    assert hasattr(dbdefinition::SequenceDefinition, "noMinimumValueString")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "noMinimumValueString" in klass.__dict__:
            descriptor = klass.__dict__["noMinimumValueString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sequencedefinition_has_typeEnumerationSupported():
    assert hasattr(dbdefinition::SequenceDefinition, "typeEnumerationSupported")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "typeEnumerationSupported" in klass.__dict__:
            descriptor = klass.__dict__["typeEnumerationSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sequencedefinition_has_orderSupported():
    assert hasattr(dbdefinition::SequenceDefinition, "orderSupported")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "orderSupported" in klass.__dict__:
            descriptor = klass.__dict__["orderSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sequencedefinition_has_cacheDefaultValue():
    assert hasattr(dbdefinition::SequenceDefinition, "cacheDefaultValue")
    descriptor = None
    for klass in dbdefinition::SequenceDefinition.__mro__:
        if "cacheDefaultValue" in klass.__dict__:
            descriptor = klass.__dict__["cacheDefaultValue"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::tabledefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::TableDefinition)


def test_dbdefinition::tabledefinition_constructor_exists():
    assert callable(dbdefinition::TableDefinition.__init__)


def test_dbdefinition::tabledefinition_constructor_args():
    sig = inspect.signature(dbdefinition::TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "auditSupported" in params, "Missing parameter 'auditSupported'"
    assert "dataCaptureSupported" in params, "Missing parameter 'dataCaptureSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "editProcSupported" in params, "Missing parameter 'editProcSupported'"
    assert "encodingSupported" in params, "Missing parameter 'encodingSupported'"
    assert "validProcSupported" in params, "Missing parameter 'validProcSupported'"

def test_dbdefinition::tabledefinition_has_auditSupported():
    assert hasattr(dbdefinition::TableDefinition, "auditSupported")
    descriptor = None
    for klass in dbdefinition::TableDefinition.__mro__:
        if "auditSupported" in klass.__dict__:
            descriptor = klass.__dict__["auditSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tabledefinition_has_dataCaptureSupported():
    assert hasattr(dbdefinition::TableDefinition, "dataCaptureSupported")
    descriptor = None
    for klass in dbdefinition::TableDefinition.__mro__:
        if "dataCaptureSupported" in klass.__dict__:
            descriptor = klass.__dict__["dataCaptureSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tabledefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::TableDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::TableDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tabledefinition_has_editProcSupported():
    assert hasattr(dbdefinition::TableDefinition, "editProcSupported")
    descriptor = None
    for klass in dbdefinition::TableDefinition.__mro__:
        if "editProcSupported" in klass.__dict__:
            descriptor = klass.__dict__["editProcSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tabledefinition_has_encodingSupported():
    assert hasattr(dbdefinition::TableDefinition, "encodingSupported")
    descriptor = None
    for klass in dbdefinition::TableDefinition.__mro__:
        if "encodingSupported" in klass.__dict__:
            descriptor = klass.__dict__["encodingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tabledefinition_has_validProcSupported():
    assert hasattr(dbdefinition::TableDefinition, "validProcSupported")
    descriptor = None
    for klass in dbdefinition::TableDefinition.__mro__:
        if "validProcSupported" in klass.__dict__:
            descriptor = klass.__dict__["validProcSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::indexdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::IndexDefinition)


def test_dbdefinition::indexdefinition_constructor_exists():
    assert callable(dbdefinition::IndexDefinition.__init__)


def test_dbdefinition::indexdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::IndexDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "includedColumnsSupported" in params, "Missing parameter 'includedColumnsSupported'"
    assert "clusterChangeable" in params, "Missing parameter 'clusterChangeable'"
    assert "fillFactorSupported" in params, "Missing parameter 'fillFactorSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "percentFreeTerminology" in params, "Missing parameter 'percentFreeTerminology'"
    assert "clusteringSupported" in params, "Missing parameter 'clusteringSupported'"
    assert "percentFreeChangeable" in params, "Missing parameter 'percentFreeChangeable'"

def test_dbdefinition::indexdefinition_has_includedColumnsSupported():
    assert hasattr(dbdefinition::IndexDefinition, "includedColumnsSupported")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "includedColumnsSupported" in klass.__dict__:
            descriptor = klass.__dict__["includedColumnsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::indexdefinition_has_clusterChangeable():
    assert hasattr(dbdefinition::IndexDefinition, "clusterChangeable")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "clusterChangeable" in klass.__dict__:
            descriptor = klass.__dict__["clusterChangeable"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::indexdefinition_has_fillFactorSupported():
    assert hasattr(dbdefinition::IndexDefinition, "fillFactorSupported")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "fillFactorSupported" in klass.__dict__:
            descriptor = klass.__dict__["fillFactorSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::indexdefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::IndexDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::indexdefinition_has_percentFreeTerminology():
    assert hasattr(dbdefinition::IndexDefinition, "percentFreeTerminology")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "percentFreeTerminology" in klass.__dict__:
            descriptor = klass.__dict__["percentFreeTerminology"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::indexdefinition_has_clusteringSupported():
    assert hasattr(dbdefinition::IndexDefinition, "clusteringSupported")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "clusteringSupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteringSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::indexdefinition_has_percentFreeChangeable():
    assert hasattr(dbdefinition::IndexDefinition, "percentFreeChangeable")
    descriptor = None
    for klass in dbdefinition::IndexDefinition.__mro__:
        if "percentFreeChangeable" in klass.__dict__:
            descriptor = klass.__dict__["percentFreeChangeable"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::extendeddefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::ExtendedDefinition)


def test_dbdefinition::extendeddefinition_constructor_exists():
    assert callable(dbdefinition::ExtendedDefinition.__init__)


def test_dbdefinition::extendeddefinition_constructor_args():
    sig = inspect.signature(dbdefinition::ExtendedDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_dbdefinition::extendeddefinition_has_name():
    assert hasattr(dbdefinition::ExtendedDefinition, "name")
    descriptor = None
    for klass in dbdefinition::ExtendedDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::extendeddefinition_has_value():
    assert hasattr(dbdefinition::ExtendedDefinition, "value")
    descriptor = None
    for klass in dbdefinition::ExtendedDefinition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::ConstraintDefinition)


def test_dbdefinition::constraintdefinition_constructor_exists():
    assert callable(dbdefinition::ConstraintDefinition.__init__)


def test_dbdefinition::constraintdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "deferrableConstraintSupported" in params, "Missing parameter 'deferrableConstraintSupported'"
    assert "maximumCheckExpressionLength" in params, "Missing parameter 'maximumCheckExpressionLength'"
    assert "clusteredUniqueConstraintSupported" in params, "Missing parameter 'clusteredUniqueConstraintSupported'"
    assert "uniqueKeyNullable" in params, "Missing parameter 'uniqueKeyNullable'"
    assert "maximumPrimaryKeyIdentifierLength" in params, "Missing parameter 'maximumPrimaryKeyIdentifierLength'"
    assert "parentUpdateDRIRuleType" in params, "Missing parameter 'parentUpdateDRIRuleType'"
    assert "checkOption" in params, "Missing parameter 'checkOption'"
    assert "parentDeleteDRIRuleType" in params, "Missing parameter 'parentDeleteDRIRuleType'"
    assert "clusteredPrimaryKeySupported" in params, "Missing parameter 'clusteredPrimaryKeySupported'"
    assert "maximumForeignKeyIdentifierLength" in params, "Missing parameter 'maximumForeignKeyIdentifierLength'"
    assert "maximumCheckConstraintIdentifierLength" in params, "Missing parameter 'maximumCheckConstraintIdentifierLength'"
    assert "informationalConstraintSupported" in params, "Missing parameter 'informationalConstraintSupported'"
    assert "primaryKeyNullable" in params, "Missing parameter 'primaryKeyNullable'"

def test_dbdefinition::constraintdefinition_has_deferrableConstraintSupported():
    assert hasattr(dbdefinition::ConstraintDefinition, "deferrableConstraintSupported")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "deferrableConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["deferrableConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_maximumCheckExpressionLength():
    assert hasattr(dbdefinition::ConstraintDefinition, "maximumCheckExpressionLength")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "maximumCheckExpressionLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumCheckExpressionLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_clusteredUniqueConstraintSupported():
    assert hasattr(dbdefinition::ConstraintDefinition, "clusteredUniqueConstraintSupported")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "clusteredUniqueConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteredUniqueConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_uniqueKeyNullable():
    assert hasattr(dbdefinition::ConstraintDefinition, "uniqueKeyNullable")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "uniqueKeyNullable" in klass.__dict__:
            descriptor = klass.__dict__["uniqueKeyNullable"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_maximumPrimaryKeyIdentifierLength():
    assert hasattr(dbdefinition::ConstraintDefinition, "maximumPrimaryKeyIdentifierLength")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "maximumPrimaryKeyIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumPrimaryKeyIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_parentUpdateDRIRuleType():
    assert hasattr(dbdefinition::ConstraintDefinition, "parentUpdateDRIRuleType")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "parentUpdateDRIRuleType" in klass.__dict__:
            descriptor = klass.__dict__["parentUpdateDRIRuleType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_checkOption():
    assert hasattr(dbdefinition::ConstraintDefinition, "checkOption")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "checkOption" in klass.__dict__:
            descriptor = klass.__dict__["checkOption"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_parentDeleteDRIRuleType():
    assert hasattr(dbdefinition::ConstraintDefinition, "parentDeleteDRIRuleType")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "parentDeleteDRIRuleType" in klass.__dict__:
            descriptor = klass.__dict__["parentDeleteDRIRuleType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_clusteredPrimaryKeySupported():
    assert hasattr(dbdefinition::ConstraintDefinition, "clusteredPrimaryKeySupported")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "clusteredPrimaryKeySupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteredPrimaryKeySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_maximumForeignKeyIdentifierLength():
    assert hasattr(dbdefinition::ConstraintDefinition, "maximumForeignKeyIdentifierLength")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "maximumForeignKeyIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumForeignKeyIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_maximumCheckConstraintIdentifierLength():
    assert hasattr(dbdefinition::ConstraintDefinition, "maximumCheckConstraintIdentifierLength")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "maximumCheckConstraintIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumCheckConstraintIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_informationalConstraintSupported():
    assert hasattr(dbdefinition::ConstraintDefinition, "informationalConstraintSupported")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "informationalConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["informationalConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::constraintdefinition_has_primaryKeyNullable():
    assert hasattr(dbdefinition::ConstraintDefinition, "primaryKeyNullable")
    descriptor = None
    for klass in dbdefinition::ConstraintDefinition.__mro__:
        if "primaryKeyNullable" in klass.__dict__:
            descriptor = klass.__dict__["primaryKeyNullable"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::columndefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::ColumnDefinition)


def test_dbdefinition::columndefinition_constructor_exists():
    assert callable(dbdefinition::ColumnDefinition.__init__)


def test_dbdefinition::columndefinition_constructor_args():
    sig = inspect.signature(dbdefinition::ColumnDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "identityIncrementSupported" in params, "Missing parameter 'identityIncrementSupported'"
    assert "identityMinimumSupported" in params, "Missing parameter 'identityMinimumSupported'"
    assert "identitySupported" in params, "Missing parameter 'identitySupported'"
    assert "computedSupported" in params, "Missing parameter 'computedSupported'"
    assert "identityCycleSupported" in params, "Missing parameter 'identityCycleSupported'"
    assert "identityStartValueSupported" in params, "Missing parameter 'identityStartValueSupported'"
    assert "identityMaximumSupported" in params, "Missing parameter 'identityMaximumSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"

def test_dbdefinition::columndefinition_has_identityIncrementSupported():
    assert hasattr(dbdefinition::ColumnDefinition, "identityIncrementSupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "identityIncrementSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityIncrementSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_identityMinimumSupported():
    assert hasattr(dbdefinition::ColumnDefinition, "identityMinimumSupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "identityMinimumSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityMinimumSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_identitySupported():
    assert hasattr(dbdefinition::ColumnDefinition, "identitySupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "identitySupported" in klass.__dict__:
            descriptor = klass.__dict__["identitySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_computedSupported():
    assert hasattr(dbdefinition::ColumnDefinition, "computedSupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "computedSupported" in klass.__dict__:
            descriptor = klass.__dict__["computedSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_identityCycleSupported():
    assert hasattr(dbdefinition::ColumnDefinition, "identityCycleSupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "identityCycleSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityCycleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_identityStartValueSupported():
    assert hasattr(dbdefinition::ColumnDefinition, "identityStartValueSupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "identityStartValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityStartValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_identityMaximumSupported():
    assert hasattr(dbdefinition::ColumnDefinition, "identityMaximumSupported")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "identityMaximumSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityMaximumSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::columndefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::ColumnDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::ColumnDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::triggerdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::TriggerDefinition)


def test_dbdefinition::triggerdefinition_constructor_exists():
    assert callable(dbdefinition::TriggerDefinition.__init__)


def test_dbdefinition::triggerdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::TriggerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "insteadOfTriggerSupported" in params, "Missing parameter 'insteadOfTriggerSupported'"
    assert "rowTriggerReferenceSupported" in params, "Missing parameter 'rowTriggerReferenceSupported'"
    assert "granularitySupported" in params, "Missing parameter 'granularitySupported'"
    assert "maximumActionBodyLength" in params, "Missing parameter 'maximumActionBodyLength'"
    assert "tableTriggerReferenceSupported" in params, "Missing parameter 'tableTriggerReferenceSupported'"
    assert "maximumReferencePartLength" in params, "Missing parameter 'maximumReferencePartLength'"
    assert "referencesClauseSupported" in params, "Missing parameter 'referencesClauseSupported'"
    assert "typeSupported" in params, "Missing parameter 'typeSupported'"
    assert "perColumnUpdateTriggerSupported" in params, "Missing parameter 'perColumnUpdateTriggerSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "whenClauseSupported" in params, "Missing parameter 'whenClauseSupported'"

def test_dbdefinition::triggerdefinition_has_insteadOfTriggerSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "insteadOfTriggerSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "insteadOfTriggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["insteadOfTriggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_rowTriggerReferenceSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "rowTriggerReferenceSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "rowTriggerReferenceSupported" in klass.__dict__:
            descriptor = klass.__dict__["rowTriggerReferenceSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_granularitySupported():
    assert hasattr(dbdefinition::TriggerDefinition, "granularitySupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "granularitySupported" in klass.__dict__:
            descriptor = klass.__dict__["granularitySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_maximumActionBodyLength():
    assert hasattr(dbdefinition::TriggerDefinition, "maximumActionBodyLength")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "maximumActionBodyLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumActionBodyLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_tableTriggerReferenceSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "tableTriggerReferenceSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "tableTriggerReferenceSupported" in klass.__dict__:
            descriptor = klass.__dict__["tableTriggerReferenceSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_maximumReferencePartLength():
    assert hasattr(dbdefinition::TriggerDefinition, "maximumReferencePartLength")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "maximumReferencePartLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumReferencePartLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_referencesClauseSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "referencesClauseSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "referencesClauseSupported" in klass.__dict__:
            descriptor = klass.__dict__["referencesClauseSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_typeSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "typeSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "typeSupported" in klass.__dict__:
            descriptor = klass.__dict__["typeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_perColumnUpdateTriggerSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "perColumnUpdateTriggerSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "perColumnUpdateTriggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["perColumnUpdateTriggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::TriggerDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::triggerdefinition_has_whenClauseSupported():
    assert hasattr(dbdefinition::TriggerDefinition, "whenClauseSupported")
    descriptor = None
    for klass in dbdefinition::TriggerDefinition.__mro__:
        if "whenClauseSupported" in klass.__dict__:
            descriptor = klass.__dict__["whenClauseSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::storedproceduredefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::StoredProcedureDefinition)


def test_dbdefinition::storedproceduredefinition_constructor_exists():
    assert callable(dbdefinition::StoredProcedureDefinition.__init__)


def test_dbdefinition::storedproceduredefinition_constructor_args():
    sig = inspect.signature(dbdefinition::StoredProcedureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "parameterInitValueSupported" in params, "Missing parameter 'parameterInitValueSupported'"
    assert "nullInputActionSupported" in params, "Missing parameter 'nullInputActionSupported'"
    assert "parameterStyle" in params, "Missing parameter 'parameterStyle'"
    assert "determininsticSupported" in params, "Missing parameter 'determininsticSupported'"
    assert "returnTypeSupported" in params, "Missing parameter 'returnTypeSupported'"
    assert "functionLanguageType" in params, "Missing parameter 'functionLanguageType'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "returnedTypeDeclarationConstraintSupported" in params, "Missing parameter 'returnedTypeDeclarationConstraintSupported'"
    assert "parameterStyleSupported" in params, "Missing parameter 'parameterStyleSupported'"
    assert "packageGenerationSupported" in params, "Missing parameter 'packageGenerationSupported'"
    assert "languageType" in params, "Missing parameter 'languageType'"
    assert "maximumActionBodyLength" in params, "Missing parameter 'maximumActionBodyLength'"
    assert "parameterDeclarationConstraintSupported" in params, "Missing parameter 'parameterDeclarationConstraintSupported'"
    assert "returnedNullSupported" in params, "Missing parameter 'returnedNullSupported'"
    assert "procedureType" in params, "Missing parameter 'procedureType'"

def test_dbdefinition::storedproceduredefinition_has_parameterInitValueSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "parameterInitValueSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "parameterInitValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["parameterInitValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_nullInputActionSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "nullInputActionSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "nullInputActionSupported" in klass.__dict__:
            descriptor = klass.__dict__["nullInputActionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_parameterStyle():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "parameterStyle")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "parameterStyle" in klass.__dict__:
            descriptor = klass.__dict__["parameterStyle"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_determininsticSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "determininsticSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "determininsticSupported" in klass.__dict__:
            descriptor = klass.__dict__["determininsticSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_returnTypeSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "returnTypeSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "returnTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["returnTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_functionLanguageType():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "functionLanguageType")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "functionLanguageType" in klass.__dict__:
            descriptor = klass.__dict__["functionLanguageType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_returnedTypeDeclarationConstraintSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "returnedTypeDeclarationConstraintSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "returnedTypeDeclarationConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["returnedTypeDeclarationConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_parameterStyleSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "parameterStyleSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "parameterStyleSupported" in klass.__dict__:
            descriptor = klass.__dict__["parameterStyleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_packageGenerationSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "packageGenerationSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "packageGenerationSupported" in klass.__dict__:
            descriptor = klass.__dict__["packageGenerationSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_languageType():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "languageType")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "languageType" in klass.__dict__:
            descriptor = klass.__dict__["languageType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_maximumActionBodyLength():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "maximumActionBodyLength")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "maximumActionBodyLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumActionBodyLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_parameterDeclarationConstraintSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "parameterDeclarationConstraintSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "parameterDeclarationConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["parameterDeclarationConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_returnedNullSupported():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "returnedNullSupported")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "returnedNullSupported" in klass.__dict__:
            descriptor = klass.__dict__["returnedNullSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::storedproceduredefinition_has_procedureType():
    assert hasattr(dbdefinition::StoredProcedureDefinition, "procedureType")
    descriptor = None
    for klass in dbdefinition::StoredProcedureDefinition.__mro__:
        if "procedureType" in klass.__dict__:
            descriptor = klass.__dict__["procedureType"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::tablespacedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::TableSpaceDefinition)


def test_dbdefinition::tablespacedefinition_constructor_exists():
    assert callable(dbdefinition::TableSpaceDefinition.__init__)


def test_dbdefinition::tablespacedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::TableSpaceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "containerInitialSizeSupported" in params, "Missing parameter 'containerInitialSizeSupported'"
    assert "prefetchSizeSupported" in params, "Missing parameter 'prefetchSizeSupported'"
    assert "typeSupported" in params, "Missing parameter 'typeSupported'"
    assert "containerExtentSizeSupported" in params, "Missing parameter 'containerExtentSizeSupported'"
    assert "bufferPoolSupported" in params, "Missing parameter 'bufferPoolSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "extentSizeSupported" in params, "Missing parameter 'extentSizeSupported'"
    assert "tableSpaceType" in params, "Missing parameter 'tableSpaceType'"
    assert "managedBySupported" in params, "Missing parameter 'managedBySupported'"
    assert "defaultSupported" in params, "Missing parameter 'defaultSupported'"
    assert "pageSizeSupported" in params, "Missing parameter 'pageSizeSupported'"
    assert "containerMaximumSizeSupported" in params, "Missing parameter 'containerMaximumSizeSupported'"

def test_dbdefinition::tablespacedefinition_has_containerInitialSizeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "containerInitialSizeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "containerInitialSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["containerInitialSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_prefetchSizeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "prefetchSizeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "prefetchSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["prefetchSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_typeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "typeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "typeSupported" in klass.__dict__:
            descriptor = klass.__dict__["typeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_containerExtentSizeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "containerExtentSizeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "containerExtentSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["containerExtentSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_bufferPoolSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "bufferPoolSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "bufferPoolSupported" in klass.__dict__:
            descriptor = klass.__dict__["bufferPoolSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::TableSpaceDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_extentSizeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "extentSizeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "extentSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["extentSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_tableSpaceType():
    assert hasattr(dbdefinition::TableSpaceDefinition, "tableSpaceType")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "tableSpaceType" in klass.__dict__:
            descriptor = klass.__dict__["tableSpaceType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_managedBySupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "managedBySupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "managedBySupported" in klass.__dict__:
            descriptor = klass.__dict__["managedBySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_defaultSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "defaultSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "defaultSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_pageSizeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "pageSizeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "pageSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["pageSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::tablespacedefinition_has_containerMaximumSizeSupported():
    assert hasattr(dbdefinition::TableSpaceDefinition, "containerMaximumSizeSupported")
    descriptor = None
    for klass in dbdefinition::TableSpaceDefinition.__mro__:
        if "containerMaximumSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["containerMaximumSizeSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::nicknamedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::NicknameDefinition)


def test_dbdefinition::nicknamedefinition_constructor_exists():
    assert callable(dbdefinition::NicknameDefinition.__init__)


def test_dbdefinition::nicknamedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::NicknameDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "indexSupported" in params, "Missing parameter 'indexSupported'"
    assert "constraintSupported" in params, "Missing parameter 'constraintSupported'"

def test_dbdefinition::nicknamedefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::NicknameDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::NicknameDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::nicknamedefinition_has_indexSupported():
    assert hasattr(dbdefinition::NicknameDefinition, "indexSupported")
    descriptor = None
    for klass in dbdefinition::NicknameDefinition.__mro__:
        if "indexSupported" in klass.__dict__:
            descriptor = klass.__dict__["indexSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::nicknamedefinition_has_constraintSupported():
    assert hasattr(dbdefinition::NicknameDefinition, "constraintSupported")
    descriptor = None
    for klass in dbdefinition::NicknameDefinition.__mro__:
        if "constraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["constraintSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::sqlsyntaxdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::SQLSyntaxDefinition)


def test_dbdefinition::sqlsyntaxdefinition_constructor_exists():
    assert callable(dbdefinition::SQLSyntaxDefinition.__init__)


def test_dbdefinition::sqlsyntaxdefinition_constructor_args():
    sig = inspect.signature(dbdefinition::SQLSyntaxDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"
    assert "terminationCharacter" in params, "Missing parameter 'terminationCharacter'"
    assert "keywords" in params, "Missing parameter 'keywords'"

def test_dbdefinition::sqlsyntaxdefinition_has_operators():
    assert hasattr(dbdefinition::SQLSyntaxDefinition, "operators")
    descriptor = None
    for klass in dbdefinition::SQLSyntaxDefinition.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sqlsyntaxdefinition_has_terminationCharacter():
    assert hasattr(dbdefinition::SQLSyntaxDefinition, "terminationCharacter")
    descriptor = None
    for klass in dbdefinition::SQLSyntaxDefinition.__mro__:
        if "terminationCharacter" in klass.__dict__:
            descriptor = klass.__dict__["terminationCharacter"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::sqlsyntaxdefinition_has_keywords():
    assert hasattr(dbdefinition::SQLSyntaxDefinition, "keywords")
    descriptor = None
    for klass in dbdefinition::SQLSyntaxDefinition.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::querydefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::QueryDefinition)


def test_dbdefinition::querydefinition_constructor_exists():
    assert callable(dbdefinition::QueryDefinition.__init__)


def test_dbdefinition::querydefinition_constructor_args():
    sig = inspect.signature(dbdefinition::QueryDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "extendedGroupingSupported" in params, "Missing parameter 'extendedGroupingSupported'"
    assert "hostVariableMarkerSupported" in params, "Missing parameter 'hostVariableMarkerSupported'"
    assert "defaultKeywordForInsertValueSupported" in params, "Missing parameter 'defaultKeywordForInsertValueSupported'"
    assert "castExpressionSupported" in params, "Missing parameter 'castExpressionSupported'"
    assert "identifierQuoteString" in params, "Missing parameter 'identifierQuoteString'"
    assert "tableAliasInDeleteSupported" in params, "Missing parameter 'tableAliasInDeleteSupported'"
    assert "hostVariableMarker" in params, "Missing parameter 'hostVariableMarker'"

def test_dbdefinition::querydefinition_has_extendedGroupingSupported():
    assert hasattr(dbdefinition::QueryDefinition, "extendedGroupingSupported")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "extendedGroupingSupported" in klass.__dict__:
            descriptor = klass.__dict__["extendedGroupingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::querydefinition_has_hostVariableMarkerSupported():
    assert hasattr(dbdefinition::QueryDefinition, "hostVariableMarkerSupported")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "hostVariableMarkerSupported" in klass.__dict__:
            descriptor = klass.__dict__["hostVariableMarkerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::querydefinition_has_defaultKeywordForInsertValueSupported():
    assert hasattr(dbdefinition::QueryDefinition, "defaultKeywordForInsertValueSupported")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "defaultKeywordForInsertValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultKeywordForInsertValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::querydefinition_has_castExpressionSupported():
    assert hasattr(dbdefinition::QueryDefinition, "castExpressionSupported")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "castExpressionSupported" in klass.__dict__:
            descriptor = klass.__dict__["castExpressionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::querydefinition_has_identifierQuoteString():
    assert hasattr(dbdefinition::QueryDefinition, "identifierQuoteString")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "identifierQuoteString" in klass.__dict__:
            descriptor = klass.__dict__["identifierQuoteString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::querydefinition_has_tableAliasInDeleteSupported():
    assert hasattr(dbdefinition::QueryDefinition, "tableAliasInDeleteSupported")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "tableAliasInDeleteSupported" in klass.__dict__:
            descriptor = klass.__dict__["tableAliasInDeleteSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::querydefinition_has_hostVariableMarker():
    assert hasattr(dbdefinition::QueryDefinition, "hostVariableMarker")
    descriptor = None
    for klass in dbdefinition::QueryDefinition.__mro__:
        if "hostVariableMarker" in klass.__dict__:
            descriptor = klass.__dict__["hostVariableMarker"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::userdefinedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::UserDefinedTypeDefinition)


def test_dbdefinition::userdefinedtypedefinition_constructor_exists():
    assert callable(dbdefinition::UserDefinedTypeDefinition.__init__)


def test_dbdefinition::userdefinedtypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::UserDefinedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "distinctTypeSupported" in params, "Missing parameter 'distinctTypeSupported'"
    assert "structuredTypeSupported" in params, "Missing parameter 'structuredTypeSupported'"
    assert "defaultValueSupported" in params, "Missing parameter 'defaultValueSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"

def test_dbdefinition::userdefinedtypedefinition_has_distinctTypeSupported():
    assert hasattr(dbdefinition::UserDefinedTypeDefinition, "distinctTypeSupported")
    descriptor = None
    for klass in dbdefinition::UserDefinedTypeDefinition.__mro__:
        if "distinctTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["distinctTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::userdefinedtypedefinition_has_structuredTypeSupported():
    assert hasattr(dbdefinition::UserDefinedTypeDefinition, "structuredTypeSupported")
    descriptor = None
    for klass in dbdefinition::UserDefinedTypeDefinition.__mro__:
        if "structuredTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["structuredTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::userdefinedtypedefinition_has_defaultValueSupported():
    assert hasattr(dbdefinition::UserDefinedTypeDefinition, "defaultValueSupported")
    descriptor = None
    for klass in dbdefinition::UserDefinedTypeDefinition.__mro__:
        if "defaultValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::userdefinedtypedefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::UserDefinedTypeDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::UserDefinedTypeDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::predefineddatatypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::PredefinedDataTypeDefinition)


def test_dbdefinition::predefineddatatypedefinition_constructor_exists():
    assert callable(dbdefinition::PredefinedDataTypeDefinition.__init__)


def test_dbdefinition::predefineddatatypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition::PredefinedDataTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "bitDataSupported" in params, "Missing parameter 'bitDataSupported'"
    assert "largeValueSpecifierSupported" in params, "Missing parameter 'largeValueSpecifierSupported'"
    assert "nullableSupported" in params, "Missing parameter 'nullableSupported'"
    assert "minimumValue" in params, "Missing parameter 'minimumValue'"
    assert "defaultLength" in params, "Missing parameter 'defaultLength'"
    assert "multipleColumnsSupported" in params, "Missing parameter 'multipleColumnsSupported'"
    assert "maximumScale" in params, "Missing parameter 'maximumScale'"
    assert "clusteringSupported" in params, "Missing parameter 'clusteringSupported'"
    assert "fillFactorSupported" in params, "Missing parameter 'fillFactorSupported'"
    assert "defaultScale" in params, "Missing parameter 'defaultScale'"
    assert "keyConstraintSupported" in params, "Missing parameter 'keyConstraintSupported'"
    assert "trailingFieldQualifierSupported" in params, "Missing parameter 'trailingFieldQualifierSupported'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "encodingScheme" in params, "Missing parameter 'encodingScheme'"
    assert "jdbcEnumType" in params, "Missing parameter 'jdbcEnumType'"
    assert "defaultPrecision" in params, "Missing parameter 'defaultPrecision'"
    assert "lengthSupported" in params, "Missing parameter 'lengthSupported'"
    assert "lengthUnit" in params, "Missing parameter 'lengthUnit'"
    assert "maximumLength" in params, "Missing parameter 'maximumLength'"
    assert "leadingFieldQualifierSupported" in params, "Missing parameter 'leadingFieldQualifierSupported'"
    assert "scaleSupported" in params, "Missing parameter 'scaleSupported'"
    assert "identitySupported" in params, "Missing parameter 'identitySupported'"
    assert "name" in params, "Missing parameter 'name'"
    assert "displayNameSupported" in params, "Missing parameter 'displayNameSupported'"
    assert "groupingSupported" in params, "Missing parameter 'groupingSupported'"
    assert "precisionSupported" in params, "Missing parameter 'precisionSupported'"
    assert "lengthSemantic" in params, "Missing parameter 'lengthSemantic'"
    assert "largeValueSpecifierName" in params, "Missing parameter 'largeValueSpecifierName'"
    assert "characterSet" in params, "Missing parameter 'characterSet'"
    assert "orderingSupported" in params, "Missing parameter 'orderingSupported'"
    assert "defaultValueTypes" in params, "Missing parameter 'defaultValueTypes'"
    assert "javaClassName" in params, "Missing parameter 'javaClassName'"
    assert "fieldQualifierSeparator" in params, "Missing parameter 'fieldQualifierSeparator'"
    assert "cutoffPrecision" in params, "Missing parameter 'cutoffPrecision'"
    assert "encodingSchemeSuffix" in params, "Missing parameter 'encodingSchemeSuffix'"
    assert "lengthSemanticSupported" in params, "Missing parameter 'lengthSemanticSupported'"
    assert "characterSetSuffix" in params, "Missing parameter 'characterSetSuffix'"
    assert "maximumValue" in params, "Missing parameter 'maximumValue'"
    assert "largeValueSpecifierLength" in params, "Missing parameter 'largeValueSpecifierLength'"
    assert "maximumPrecision" in params, "Missing parameter 'maximumPrecision'"
    assert "defaultSupported" in params, "Missing parameter 'defaultSupported'"
    assert "minimumScale" in params, "Missing parameter 'minimumScale'"
    assert "languageType" in params, "Missing parameter 'languageType'"

def test_dbdefinition::predefineddatatypedefinition_has_primitiveType():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "primitiveType")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_bitDataSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "bitDataSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "bitDataSupported" in klass.__dict__:
            descriptor = klass.__dict__["bitDataSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_largeValueSpecifierSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "largeValueSpecifierSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "largeValueSpecifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["largeValueSpecifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_nullableSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "nullableSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "nullableSupported" in klass.__dict__:
            descriptor = klass.__dict__["nullableSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_minimumValue():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "minimumValue")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "minimumValue" in klass.__dict__:
            descriptor = klass.__dict__["minimumValue"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_defaultLength():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "defaultLength")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "defaultLength" in klass.__dict__:
            descriptor = klass.__dict__["defaultLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_multipleColumnsSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "multipleColumnsSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "multipleColumnsSupported" in klass.__dict__:
            descriptor = klass.__dict__["multipleColumnsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_maximumScale():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "maximumScale")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "maximumScale" in klass.__dict__:
            descriptor = klass.__dict__["maximumScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_clusteringSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "clusteringSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "clusteringSupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteringSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_fillFactorSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "fillFactorSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "fillFactorSupported" in klass.__dict__:
            descriptor = klass.__dict__["fillFactorSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_defaultScale():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "defaultScale")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "defaultScale" in klass.__dict__:
            descriptor = klass.__dict__["defaultScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_keyConstraintSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "keyConstraintSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "keyConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["keyConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_trailingFieldQualifierSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "trailingFieldQualifierSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "trailingFieldQualifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["trailingFieldQualifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_displayName():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "displayName")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_encodingScheme():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "encodingScheme")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "encodingScheme" in klass.__dict__:
            descriptor = klass.__dict__["encodingScheme"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_jdbcEnumType():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "jdbcEnumType")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "jdbcEnumType" in klass.__dict__:
            descriptor = klass.__dict__["jdbcEnumType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_defaultPrecision():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "defaultPrecision")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "defaultPrecision" in klass.__dict__:
            descriptor = klass.__dict__["defaultPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_lengthSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "lengthSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "lengthSupported" in klass.__dict__:
            descriptor = klass.__dict__["lengthSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_lengthUnit():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "lengthUnit")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "lengthUnit" in klass.__dict__:
            descriptor = klass.__dict__["lengthUnit"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_maximumLength():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "maximumLength")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "maximumLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_leadingFieldQualifierSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "leadingFieldQualifierSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "leadingFieldQualifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["leadingFieldQualifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_scaleSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "scaleSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "scaleSupported" in klass.__dict__:
            descriptor = klass.__dict__["scaleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_identitySupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "identitySupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "identitySupported" in klass.__dict__:
            descriptor = klass.__dict__["identitySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_name():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "name")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_displayNameSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "displayNameSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "displayNameSupported" in klass.__dict__:
            descriptor = klass.__dict__["displayNameSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_groupingSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "groupingSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "groupingSupported" in klass.__dict__:
            descriptor = klass.__dict__["groupingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_precisionSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "precisionSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "precisionSupported" in klass.__dict__:
            descriptor = klass.__dict__["precisionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_lengthSemantic():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "lengthSemantic")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "lengthSemantic" in klass.__dict__:
            descriptor = klass.__dict__["lengthSemantic"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_largeValueSpecifierName():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "largeValueSpecifierName")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "largeValueSpecifierName" in klass.__dict__:
            descriptor = klass.__dict__["largeValueSpecifierName"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_characterSet():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "characterSet")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "characterSet" in klass.__dict__:
            descriptor = klass.__dict__["characterSet"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_orderingSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "orderingSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "orderingSupported" in klass.__dict__:
            descriptor = klass.__dict__["orderingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_defaultValueTypes():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "defaultValueTypes")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "defaultValueTypes" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueTypes"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_javaClassName():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "javaClassName")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "javaClassName" in klass.__dict__:
            descriptor = klass.__dict__["javaClassName"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_fieldQualifierSeparator():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "fieldQualifierSeparator")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "fieldQualifierSeparator" in klass.__dict__:
            descriptor = klass.__dict__["fieldQualifierSeparator"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_cutoffPrecision():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "cutoffPrecision")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "cutoffPrecision" in klass.__dict__:
            descriptor = klass.__dict__["cutoffPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_encodingSchemeSuffix():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "encodingSchemeSuffix")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "encodingSchemeSuffix" in klass.__dict__:
            descriptor = klass.__dict__["encodingSchemeSuffix"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_lengthSemanticSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "lengthSemanticSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "lengthSemanticSupported" in klass.__dict__:
            descriptor = klass.__dict__["lengthSemanticSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_characterSetSuffix():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "characterSetSuffix")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "characterSetSuffix" in klass.__dict__:
            descriptor = klass.__dict__["characterSetSuffix"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_maximumValue():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "maximumValue")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "maximumValue" in klass.__dict__:
            descriptor = klass.__dict__["maximumValue"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_largeValueSpecifierLength():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "largeValueSpecifierLength")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "largeValueSpecifierLength" in klass.__dict__:
            descriptor = klass.__dict__["largeValueSpecifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_maximumPrecision():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "maximumPrecision")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "maximumPrecision" in klass.__dict__:
            descriptor = klass.__dict__["maximumPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_defaultSupported():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "defaultSupported")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "defaultSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_minimumScale():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "minimumScale")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "minimumScale" in klass.__dict__:
            descriptor = klass.__dict__["minimumScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::predefineddatatypedefinition_has_languageType():
    assert hasattr(dbdefinition::PredefinedDataTypeDefinition, "languageType")
    descriptor = None
    for klass in dbdefinition::PredefinedDataTypeDefinition.__mro__:
        if "languageType" in klass.__dict__:
            descriptor = klass.__dict__["languageType"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition::databasevendordefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition::DatabaseVendorDefinition)


def test_dbdefinition::databasevendordefinition_constructor_exists():
    assert callable(dbdefinition::DatabaseVendorDefinition.__init__)


def test_dbdefinition::databasevendordefinition_constructor_args():
    sig = inspect.signature(dbdefinition::DatabaseVendorDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "sqlUDFSupported" in params, "Missing parameter 'sqlUDFSupported'"
    assert "joinSupported" in params, "Missing parameter 'joinSupported'"
    assert "mQTSupported" in params, "Missing parameter 'mQTSupported'"
    assert "synonymSupported" in params, "Missing parameter 'synonymSupported'"
    assert "snapshotViewSupported" in params, "Missing parameter 'snapshotViewSupported'"
    assert "roleAuthorizationSupported" in params, "Missing parameter 'roleAuthorizationSupported'"
    assert "triggerSupported" in params, "Missing parameter 'triggerSupported'"
    assert "userSupported" in params, "Missing parameter 'userSupported'"
    assert "sequenceSupported" in params, "Missing parameter 'sequenceSupported'"
    assert "version" in params, "Missing parameter 'version'"
    assert "tablespacesSupported" in params, "Missing parameter 'tablespacesSupported'"
    assert "domainSupported" in params, "Missing parameter 'domainSupported'"
    assert "groupSupported" in params, "Missing parameter 'groupSupported'"
    assert "userDefinedTypeSupported" in params, "Missing parameter 'userDefinedTypeSupported'"
    assert "viewTriggerSupported" in params, "Missing parameter 'viewTriggerSupported'"
    assert "packageSupported" in params, "Missing parameter 'packageSupported'"
    assert "schemaSupported" in params, "Missing parameter 'schemaSupported'"
    assert "eventSupported" in params, "Missing parameter 'eventSupported'"
    assert "constraintsSupported" in params, "Missing parameter 'constraintsSupported'"
    assert "constructedDataTypeSupported" in params, "Missing parameter 'constructedDataTypeSupported'"
    assert "roleSupported" in params, "Missing parameter 'roleSupported'"
    assert "authorizationIdentifierSupported" in params, "Missing parameter 'authorizationIdentifierSupported'"
    assert "aliasSupported" in params, "Missing parameter 'aliasSupported'"
    assert "maximumCommentLength" in params, "Missing parameter 'maximumCommentLength'"
    assert "xmlSupported" in params, "Missing parameter 'xmlSupported'"
    assert "storedProcedureSupported" in params, "Missing parameter 'storedProcedureSupported'"
    assert "SQLStatementSupported" in params, "Missing parameter 'SQLStatementSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "uDFSupported" in params, "Missing parameter 'uDFSupported'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "nicknameSupported" in params, "Missing parameter 'nicknameSupported'"
    assert "quotedDMLSupported" in params, "Missing parameter 'quotedDMLSupported'"
    assert "mQTIndexSupported" in params, "Missing parameter 'mQTIndexSupported'"
    assert "quotedDDLSupported" in params, "Missing parameter 'quotedDDLSupported'"

def test_dbdefinition::databasevendordefinition_has_sqlUDFSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "sqlUDFSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "sqlUDFSupported" in klass.__dict__:
            descriptor = klass.__dict__["sqlUDFSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_joinSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "joinSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "joinSupported" in klass.__dict__:
            descriptor = klass.__dict__["joinSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_mQTSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "mQTSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "mQTSupported" in klass.__dict__:
            descriptor = klass.__dict__["mQTSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_synonymSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "synonymSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "synonymSupported" in klass.__dict__:
            descriptor = klass.__dict__["synonymSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_snapshotViewSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "snapshotViewSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "snapshotViewSupported" in klass.__dict__:
            descriptor = klass.__dict__["snapshotViewSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_roleAuthorizationSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "roleAuthorizationSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "roleAuthorizationSupported" in klass.__dict__:
            descriptor = klass.__dict__["roleAuthorizationSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_triggerSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "triggerSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "triggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["triggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_userSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "userSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "userSupported" in klass.__dict__:
            descriptor = klass.__dict__["userSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_sequenceSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "sequenceSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "sequenceSupported" in klass.__dict__:
            descriptor = klass.__dict__["sequenceSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_version():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "version")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_tablespacesSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "tablespacesSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "tablespacesSupported" in klass.__dict__:
            descriptor = klass.__dict__["tablespacesSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_domainSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "domainSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "domainSupported" in klass.__dict__:
            descriptor = klass.__dict__["domainSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_groupSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "groupSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "groupSupported" in klass.__dict__:
            descriptor = klass.__dict__["groupSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_userDefinedTypeSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "userDefinedTypeSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "userDefinedTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["userDefinedTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_viewTriggerSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "viewTriggerSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "viewTriggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["viewTriggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_packageSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "packageSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "packageSupported" in klass.__dict__:
            descriptor = klass.__dict__["packageSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_schemaSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "schemaSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "schemaSupported" in klass.__dict__:
            descriptor = klass.__dict__["schemaSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_eventSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "eventSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "eventSupported" in klass.__dict__:
            descriptor = klass.__dict__["eventSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_constraintsSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "constraintsSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "constraintsSupported" in klass.__dict__:
            descriptor = klass.__dict__["constraintsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_constructedDataTypeSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "constructedDataTypeSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "constructedDataTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["constructedDataTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_roleSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "roleSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "roleSupported" in klass.__dict__:
            descriptor = klass.__dict__["roleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_authorizationIdentifierSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "authorizationIdentifierSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "authorizationIdentifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["authorizationIdentifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_aliasSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "aliasSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "aliasSupported" in klass.__dict__:
            descriptor = klass.__dict__["aliasSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_maximumCommentLength():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "maximumCommentLength")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "maximumCommentLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumCommentLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_xmlSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "xmlSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "xmlSupported" in klass.__dict__:
            descriptor = klass.__dict__["xmlSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_storedProcedureSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "storedProcedureSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "storedProcedureSupported" in klass.__dict__:
            descriptor = klass.__dict__["storedProcedureSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_SQLStatementSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "SQLStatementSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "SQLStatementSupported" in klass.__dict__:
            descriptor = klass.__dict__["SQLStatementSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_uDFSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "uDFSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "uDFSupported" in klass.__dict__:
            descriptor = klass.__dict__["uDFSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_vendor():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "vendor")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_nicknameSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "nicknameSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "nicknameSupported" in klass.__dict__:
            descriptor = klass.__dict__["nicknameSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_quotedDMLSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "quotedDMLSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "quotedDMLSupported" in klass.__dict__:
            descriptor = klass.__dict__["quotedDMLSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_mQTIndexSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "mQTIndexSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "mQTIndexSupported" in klass.__dict__:
            descriptor = klass.__dict__["mQTIndexSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition::databasevendordefinition_has_quotedDDLSupported():
    assert hasattr(dbdefinition::DatabaseVendorDefinition, "quotedDDLSupported")
    descriptor = None
    for klass in dbdefinition::DatabaseVendorDefinition.__mro__:
        if "quotedDDLSupported" in klass.__dict__:
            descriptor = klass.__dict__["quotedDDLSupported"]
            break
    assert isinstance(descriptor, property)

def test_lengthunit_exists():
    # Check that the Enumeration exists
    assert LengthUnit is not None

def test_lengthunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnit]
    expected_literals = [
        "DOUBLE_BYTE",
        "DECIMAL",
        "BYTE",
        "BIT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnit"

def test_percentfreeterminology_exists():
    # Check that the Enumeration exists
    assert PercentFreeTerminology is not None

def test_percentfreeterminology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PercentFreeTerminology]
    expected_literals = [
        "THRESHOLD",
        "PERCENT_FREE",
        "FILL_FACTOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PercentFreeTerminology"

def test_parentdeletedriruletype_exists():
    # Check that the Enumeration exists
    assert ParentDeleteDRIRuleType is not None

def test_parentdeletedriruletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParentDeleteDRIRuleType]
    expected_literals = [
        "RESTRICT",
        "SET_NULL",
        "NO_ACTION",
        "CASCADE",
        "SET_DEFAULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParentDeleteDRIRuleType"

def test_tablespacetype_exists():
    # Check that the Enumeration exists
    assert TableSpaceType is not None

def test_tablespacetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableSpaceType]
    expected_literals = [
        "REGULAR",
        "LOB",
        "USER_TEMPORARY",
        "LONG",
        "TEMPORARY",
        "LARGE",
        "SYSTEM_TEMPORARY",
        "PERMANENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableSpaceType"

def test_proceduretype_exists():
    # Check that the Enumeration exists
    assert ProcedureType is not None

def test_proceduretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureType]
    expected_literals = [
        "PROCEDURE",
        "FUNCTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureType"

def test_checkoption_exists():
    # Check that the Enumeration exists
    assert CheckOption is not None

def test_checkoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CheckOption]
    expected_literals = [
        "LOCAL",
        "CASCADE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CheckOption"

def test_languagetype_exists():
    # Check that the Enumeration exists
    assert LanguageType is not None

def test_languagetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LanguageType]
    expected_literals = [
        "JAVA",
        "COBOLLE",
        "FORTRAN",
        "CL",
        "COBOL",
        "ASSEMBLY",
        "RPGLE",
        "PLI",
        "REXX",
        "C",
        "RPG",
        "SQL",
        "OLE",
        "CPLUSPLUS",
        "PLSQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LanguageType"

def test_parameterstyle_exists():
    # Check that the Enumeration exists
    assert ParameterStyle is not None

def test_parameterstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterStyle]
    expected_literals = [
        "DB2DARI",
        "GENERAL",
        "DB2SQL",
        "GENERAL_WITH_NULLS",
        "SQL",
        "JAVA",
        "DB2GENRL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterStyle"

def test_parentupdatedriruletype_exists():
    # Check that the Enumeration exists
    assert ParentUpdateDRIRuleType is not None

def test_parentupdatedriruletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParentUpdateDRIRuleType]
    expected_literals = [
        "RESTRICT",
        "SET_DEFAULT",
        "NO_ACTION",
        "SET_NULL",
        "CASCADE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParentUpdateDRIRuleType"


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
dbdefinition::PrivilegeDefinition_strategy = st.builds(
    dbdefinition::PrivilegeDefinition,
    name=
        safe_text
)
dbdefinition::FieldQualifierDefinition_strategy = st.builds(
    dbdefinition::FieldQualifierDefinition,
    defaultScale=
        st.integers(),
    defaultPrecision=
        st.integers(),
    precisionSupported=
        st.booleans(),
    scaleSupported=
        st.booleans(),
    name=
        safe_text,
    maximumScale=
        st.integers(),
    maximumPrecision=
        st.integers()
)
dbdefinition::ConstructedDataTypeDefinition_strategy = st.builds(
    dbdefinition::ConstructedDataTypeDefinition,
    rowDatatypeSupported=
        st.booleans(),
    referenceDatatypeSupported=
        st.booleans(),
    cursorDatatypeSupported=
        st.booleans(),
    multisetDatatypeSupported=
        st.booleans(),
    arrayDatatypeSupported=
        st.booleans()
)
dbdefinition::PrivilegedElementDefinition_strategy = st.builds(
    dbdefinition::PrivilegedElementDefinition,
    name=
        safe_text
)
dbdefinition::DebuggerDefinition_strategy = st.builds(
    dbdefinition::DebuggerDefinition,
    conditionSupported=
        st.booleans()
)
dbdefinition::ViewDefinition_strategy = st.builds(
    dbdefinition::ViewDefinition,
    checkOptionSupported=
        st.booleans(),
    checkOptionLevelsSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    indexSupported=
        st.booleans()
)
dbdefinition::SchemaDefinition_strategy = st.builds(
    dbdefinition::SchemaDefinition,
    maximumIdentifierLength=
        st.integers()
)
dbdefinition::SequenceDefinition_strategy = st.builds(
    dbdefinition::SequenceDefinition,
    noCacheString=
        safe_text,
    noMaximumValueString=
        safe_text,
    cacheSupported=
        st.booleans(),
    noMinimumValueString=
        safe_text,
    typeEnumerationSupported=
        st.booleans(),
    orderSupported=
        st.booleans(),
    cacheDefaultValue=
        st.integers()
)
dbdefinition::TableDefinition_strategy = st.builds(
    dbdefinition::TableDefinition,
    auditSupported=
        st.booleans(),
    dataCaptureSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    editProcSupported=
        st.booleans(),
    encodingSupported=
        st.booleans(),
    validProcSupported=
        st.booleans()
)
dbdefinition::IndexDefinition_strategy = st.builds(
    dbdefinition::IndexDefinition,
    includedColumnsSupported=
        st.booleans(),
    clusterChangeable=
        st.booleans(),
    fillFactorSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    percentFreeTerminology=
        safe_text,
    clusteringSupported=
        st.booleans(),
    percentFreeChangeable=
        st.booleans()
)
dbdefinition::ExtendedDefinition_strategy = st.builds(
    dbdefinition::ExtendedDefinition,
    name=
        safe_text,
    value=
        safe_text
)
dbdefinition::ConstraintDefinition_strategy = st.builds(
    dbdefinition::ConstraintDefinition,
    deferrableConstraintSupported=
        st.booleans(),
    maximumCheckExpressionLength=
        st.integers(),
    clusteredUniqueConstraintSupported=
        st.booleans(),
    uniqueKeyNullable=
        st.booleans(),
    maximumPrimaryKeyIdentifierLength=
        st.integers(),
    parentUpdateDRIRuleType=
        safe_text,
    checkOption=
        safe_text,
    parentDeleteDRIRuleType=
        safe_text,
    clusteredPrimaryKeySupported=
        st.booleans(),
    maximumForeignKeyIdentifierLength=
        st.integers(),
    maximumCheckConstraintIdentifierLength=
        st.integers(),
    informationalConstraintSupported=
        st.booleans(),
    primaryKeyNullable=
        st.booleans()
)
dbdefinition::ColumnDefinition_strategy = st.builds(
    dbdefinition::ColumnDefinition,
    identityIncrementSupported=
        st.booleans(),
    identityMinimumSupported=
        st.booleans(),
    identitySupported=
        st.booleans(),
    computedSupported=
        st.booleans(),
    identityCycleSupported=
        st.booleans(),
    identityStartValueSupported=
        st.booleans(),
    identityMaximumSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers()
)
dbdefinition::TriggerDefinition_strategy = st.builds(
    dbdefinition::TriggerDefinition,
    insteadOfTriggerSupported=
        st.booleans(),
    rowTriggerReferenceSupported=
        st.booleans(),
    granularitySupported=
        st.booleans(),
    maximumActionBodyLength=
        st.integers(),
    tableTriggerReferenceSupported=
        st.booleans(),
    maximumReferencePartLength=
        st.integers(),
    referencesClauseSupported=
        st.booleans(),
    typeSupported=
        st.booleans(),
    perColumnUpdateTriggerSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    whenClauseSupported=
        st.booleans()
)
dbdefinition::StoredProcedureDefinition_strategy = st.builds(
    dbdefinition::StoredProcedureDefinition,
    parameterInitValueSupported=
        st.booleans(),
    nullInputActionSupported=
        st.booleans(),
    parameterStyle=
        safe_text,
    determininsticSupported=
        st.booleans(),
    returnTypeSupported=
        st.booleans(),
    functionLanguageType=
        safe_text,
    maximumIdentifierLength=
        st.integers(),
    returnedTypeDeclarationConstraintSupported=
        st.booleans(),
    parameterStyleSupported=
        st.booleans(),
    packageGenerationSupported=
        st.booleans(),
    languageType=
        safe_text,
    maximumActionBodyLength=
        st.integers(),
    parameterDeclarationConstraintSupported=
        st.booleans(),
    returnedNullSupported=
        st.booleans(),
    procedureType=
        safe_text
)
dbdefinition::TableSpaceDefinition_strategy = st.builds(
    dbdefinition::TableSpaceDefinition,
    containerInitialSizeSupported=
        st.booleans(),
    prefetchSizeSupported=
        st.booleans(),
    typeSupported=
        st.booleans(),
    containerExtentSizeSupported=
        st.booleans(),
    bufferPoolSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    extentSizeSupported=
        st.booleans(),
    tableSpaceType=
        safe_text,
    managedBySupported=
        st.booleans(),
    defaultSupported=
        st.booleans(),
    pageSizeSupported=
        st.booleans(),
    containerMaximumSizeSupported=
        st.booleans()
)
dbdefinition::NicknameDefinition_strategy = st.builds(
    dbdefinition::NicknameDefinition,
    maximumIdentifierLength=
        st.integers(),
    indexSupported=
        st.booleans(),
    constraintSupported=
        st.booleans()
)
dbdefinition::SQLSyntaxDefinition_strategy = st.builds(
    dbdefinition::SQLSyntaxDefinition,
    operators=
        safe_text,
    terminationCharacter=
        safe_text,
    keywords=
        safe_text
)
dbdefinition::QueryDefinition_strategy = st.builds(
    dbdefinition::QueryDefinition,
    extendedGroupingSupported=
        st.booleans(),
    hostVariableMarkerSupported=
        st.booleans(),
    defaultKeywordForInsertValueSupported=
        st.booleans(),
    castExpressionSupported=
        st.booleans(),
    identifierQuoteString=
        safe_text,
    tableAliasInDeleteSupported=
        st.booleans(),
    hostVariableMarker=
        safe_text
)
dbdefinition::UserDefinedTypeDefinition_strategy = st.builds(
    dbdefinition::UserDefinedTypeDefinition,
    distinctTypeSupported=
        st.booleans(),
    structuredTypeSupported=
        st.booleans(),
    defaultValueSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers()
)
dbdefinition::PredefinedDataTypeDefinition_strategy = st.builds(
    dbdefinition::PredefinedDataTypeDefinition,
    primitiveType=
        safe_text,
    bitDataSupported=
        st.booleans(),
    largeValueSpecifierSupported=
        st.booleans(),
    nullableSupported=
        st.booleans(),
    minimumValue=
        safe_text,
    defaultLength=
        st.integers(),
    multipleColumnsSupported=
        st.booleans(),
    maximumScale=
        st.integers(),
    clusteringSupported=
        st.booleans(),
    fillFactorSupported=
        st.booleans(),
    defaultScale=
        st.integers(),
    keyConstraintSupported=
        st.booleans(),
    trailingFieldQualifierSupported=
        st.booleans(),
    displayName=
        safe_text,
    encodingScheme=
        safe_text,
    jdbcEnumType=
        st.integers(),
    defaultPrecision=
        st.integers(),
    lengthSupported=
        st.booleans(),
    lengthUnit=
        safe_text,
    maximumLength=
        st.integers(),
    leadingFieldQualifierSupported=
        st.booleans(),
    scaleSupported=
        st.booleans(),
    identitySupported=
        st.booleans(),
    name=
        safe_text,
    displayNameSupported=
        st.booleans(),
    groupingSupported=
        st.booleans(),
    precisionSupported=
        st.booleans(),
    lengthSemantic=
        safe_text,
    largeValueSpecifierName=
        safe_text,
    characterSet=
        safe_text,
    orderingSupported=
        st.booleans(),
    defaultValueTypes=
        safe_text,
    javaClassName=
        safe_text,
    fieldQualifierSeparator=
        safe_text,
    cutoffPrecision=
        st.integers(),
    encodingSchemeSuffix=
        safe_text,
    lengthSemanticSupported=
        st.booleans(),
    characterSetSuffix=
        safe_text,
    maximumValue=
        safe_text,
    largeValueSpecifierLength=
        st.integers(),
    maximumPrecision=
        st.integers(),
    defaultSupported=
        st.booleans(),
    minimumScale=
        st.integers(),
    languageType=
        safe_text
)
dbdefinition::DatabaseVendorDefinition_strategy = st.builds(
    dbdefinition::DatabaseVendorDefinition,
    sqlUDFSupported=
        st.booleans(),
    joinSupported=
        st.booleans(),
    mQTSupported=
        st.booleans(),
    synonymSupported=
        st.booleans(),
    snapshotViewSupported=
        st.booleans(),
    roleAuthorizationSupported=
        st.booleans(),
    triggerSupported=
        st.booleans(),
    userSupported=
        st.booleans(),
    sequenceSupported=
        st.booleans(),
    version=
        safe_text,
    tablespacesSupported=
        st.booleans(),
    domainSupported=
        st.booleans(),
    groupSupported=
        st.booleans(),
    userDefinedTypeSupported=
        st.booleans(),
    viewTriggerSupported=
        st.booleans(),
    packageSupported=
        st.booleans(),
    schemaSupported=
        st.booleans(),
    eventSupported=
        st.booleans(),
    constraintsSupported=
        st.booleans(),
    constructedDataTypeSupported=
        st.booleans(),
    roleSupported=
        st.booleans(),
    authorizationIdentifierSupported=
        st.booleans(),
    aliasSupported=
        st.booleans(),
    maximumCommentLength=
        st.integers(),
    xmlSupported=
        st.booleans(),
    storedProcedureSupported=
        st.booleans(),
    SQLStatementSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    uDFSupported=
        st.booleans(),
    vendor=
        safe_text,
    nicknameSupported=
        st.booleans(),
    quotedDMLSupported=
        st.booleans(),
    mQTIndexSupported=
        st.booleans(),
    quotedDDLSupported=
        st.booleans()
)

@given(instance=dbdefinition::PrivilegeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::privilegedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::PrivilegeDefinition)

@given(instance=dbdefinition::PrivilegeDefinition_strategy)
def test_dbdefinition::privilegedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbdefinition::PrivilegeDefinition_strategy)
def test_dbdefinition::privilegedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::fieldqualifierdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::FieldQualifierDefinition)

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_defaultScale_type(instance):
    assert isinstance(instance.defaultScale, int)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_defaultScale_setter(instance):
    original = instance.defaultScale
    instance.defaultScale = original
    assert instance.defaultScale == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_defaultPrecision_type(instance):
    assert isinstance(instance.defaultPrecision, int)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_defaultPrecision_setter(instance):
    original = instance.defaultPrecision
    instance.defaultPrecision = original
    assert instance.defaultPrecision == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_precisionSupported_type(instance):
    assert isinstance(instance.precisionSupported, bool)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_precisionSupported_setter(instance):
    original = instance.precisionSupported
    instance.precisionSupported = original
    assert instance.precisionSupported == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_scaleSupported_type(instance):
    assert isinstance(instance.scaleSupported, bool)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_scaleSupported_setter(instance):
    original = instance.scaleSupported
    instance.scaleSupported = original
    assert instance.scaleSupported == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_maximumScale_type(instance):
    assert isinstance(instance.maximumScale, int)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_maximumScale_setter(instance):
    original = instance.maximumScale
    instance.maximumScale = original
    assert instance.maximumScale == original

@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_maximumPrecision_type(instance):
    assert isinstance(instance.maximumPrecision, int)


@given(instance=dbdefinition::FieldQualifierDefinition_strategy)
def test_dbdefinition::fieldqualifierdefinition_maximumPrecision_setter(instance):
    original = instance.maximumPrecision
    instance.maximumPrecision = original
    assert instance.maximumPrecision == original

@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::constructeddatatypedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::ConstructedDataTypeDefinition)

@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_rowDatatypeSupported_type(instance):
    assert isinstance(instance.rowDatatypeSupported, bool)


@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_rowDatatypeSupported_setter(instance):
    original = instance.rowDatatypeSupported
    instance.rowDatatypeSupported = original
    assert instance.rowDatatypeSupported == original

@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_referenceDatatypeSupported_type(instance):
    assert isinstance(instance.referenceDatatypeSupported, bool)


@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_referenceDatatypeSupported_setter(instance):
    original = instance.referenceDatatypeSupported
    instance.referenceDatatypeSupported = original
    assert instance.referenceDatatypeSupported == original

@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_cursorDatatypeSupported_type(instance):
    assert isinstance(instance.cursorDatatypeSupported, bool)


@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_cursorDatatypeSupported_setter(instance):
    original = instance.cursorDatatypeSupported
    instance.cursorDatatypeSupported = original
    assert instance.cursorDatatypeSupported == original

@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_multisetDatatypeSupported_type(instance):
    assert isinstance(instance.multisetDatatypeSupported, bool)


@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_multisetDatatypeSupported_setter(instance):
    original = instance.multisetDatatypeSupported
    instance.multisetDatatypeSupported = original
    assert instance.multisetDatatypeSupported == original

@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_arrayDatatypeSupported_type(instance):
    assert isinstance(instance.arrayDatatypeSupported, bool)


@given(instance=dbdefinition::ConstructedDataTypeDefinition_strategy)
def test_dbdefinition::constructeddatatypedefinition_arrayDatatypeSupported_setter(instance):
    original = instance.arrayDatatypeSupported
    instance.arrayDatatypeSupported = original
    assert instance.arrayDatatypeSupported == original

@given(instance=dbdefinition::PrivilegedElementDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::privilegedelementdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::PrivilegedElementDefinition)

@given(instance=dbdefinition::PrivilegedElementDefinition_strategy)
def test_dbdefinition::privilegedelementdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbdefinition::PrivilegedElementDefinition_strategy)
def test_dbdefinition::privilegedelementdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition::DebuggerDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::debuggerdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::DebuggerDefinition)

@given(instance=dbdefinition::DebuggerDefinition_strategy)
def test_dbdefinition::debuggerdefinition_conditionSupported_type(instance):
    assert isinstance(instance.conditionSupported, bool)


@given(instance=dbdefinition::DebuggerDefinition_strategy)
def test_dbdefinition::debuggerdefinition_conditionSupported_setter(instance):
    original = instance.conditionSupported
    instance.conditionSupported = original
    assert instance.conditionSupported == original

@given(instance=dbdefinition::ViewDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::viewdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::ViewDefinition)

@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_checkOptionSupported_type(instance):
    assert isinstance(instance.checkOptionSupported, bool)


@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_checkOptionSupported_setter(instance):
    original = instance.checkOptionSupported
    instance.checkOptionSupported = original
    assert instance.checkOptionSupported == original

@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_checkOptionLevelsSupported_type(instance):
    assert isinstance(instance.checkOptionLevelsSupported, bool)


@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_checkOptionLevelsSupported_setter(instance):
    original = instance.checkOptionLevelsSupported
    instance.checkOptionLevelsSupported = original
    assert instance.checkOptionLevelsSupported == original

@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_indexSupported_type(instance):
    assert isinstance(instance.indexSupported, bool)


@given(instance=dbdefinition::ViewDefinition_strategy)
def test_dbdefinition::viewdefinition_indexSupported_setter(instance):
    original = instance.indexSupported
    instance.indexSupported = original
    assert instance.indexSupported == original

@given(instance=dbdefinition::SchemaDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::schemadefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::SchemaDefinition)

@given(instance=dbdefinition::SchemaDefinition_strategy)
def test_dbdefinition::schemadefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::SchemaDefinition_strategy)
def test_dbdefinition::schemadefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::sequencedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::SequenceDefinition)

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_noCacheString_type(instance):
    assert isinstance(instance.noCacheString, str)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_noCacheString_setter(instance):
    original = instance.noCacheString
    instance.noCacheString = original
    assert instance.noCacheString == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_noMaximumValueString_type(instance):
    assert isinstance(instance.noMaximumValueString, str)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_noMaximumValueString_setter(instance):
    original = instance.noMaximumValueString
    instance.noMaximumValueString = original
    assert instance.noMaximumValueString == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_cacheSupported_type(instance):
    assert isinstance(instance.cacheSupported, bool)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_cacheSupported_setter(instance):
    original = instance.cacheSupported
    instance.cacheSupported = original
    assert instance.cacheSupported == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_noMinimumValueString_type(instance):
    assert isinstance(instance.noMinimumValueString, str)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_noMinimumValueString_setter(instance):
    original = instance.noMinimumValueString
    instance.noMinimumValueString = original
    assert instance.noMinimumValueString == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_typeEnumerationSupported_type(instance):
    assert isinstance(instance.typeEnumerationSupported, bool)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_typeEnumerationSupported_setter(instance):
    original = instance.typeEnumerationSupported
    instance.typeEnumerationSupported = original
    assert instance.typeEnumerationSupported == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_orderSupported_type(instance):
    assert isinstance(instance.orderSupported, bool)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_orderSupported_setter(instance):
    original = instance.orderSupported
    instance.orderSupported = original
    assert instance.orderSupported == original

@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_cacheDefaultValue_type(instance):
    assert isinstance(instance.cacheDefaultValue, int)


@given(instance=dbdefinition::SequenceDefinition_strategy)
def test_dbdefinition::sequencedefinition_cacheDefaultValue_setter(instance):
    original = instance.cacheDefaultValue
    instance.cacheDefaultValue = original
    assert instance.cacheDefaultValue == original

@given(instance=dbdefinition::TableDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::tabledefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::TableDefinition)

@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_auditSupported_type(instance):
    assert isinstance(instance.auditSupported, bool)


@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_auditSupported_setter(instance):
    original = instance.auditSupported
    instance.auditSupported = original
    assert instance.auditSupported == original

@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_dataCaptureSupported_type(instance):
    assert isinstance(instance.dataCaptureSupported, bool)


@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_dataCaptureSupported_setter(instance):
    original = instance.dataCaptureSupported
    instance.dataCaptureSupported = original
    assert instance.dataCaptureSupported == original

@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_editProcSupported_type(instance):
    assert isinstance(instance.editProcSupported, bool)


@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_editProcSupported_setter(instance):
    original = instance.editProcSupported
    instance.editProcSupported = original
    assert instance.editProcSupported == original

@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_encodingSupported_type(instance):
    assert isinstance(instance.encodingSupported, bool)


@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_encodingSupported_setter(instance):
    original = instance.encodingSupported
    instance.encodingSupported = original
    assert instance.encodingSupported == original

@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_validProcSupported_type(instance):
    assert isinstance(instance.validProcSupported, bool)


@given(instance=dbdefinition::TableDefinition_strategy)
def test_dbdefinition::tabledefinition_validProcSupported_setter(instance):
    original = instance.validProcSupported
    instance.validProcSupported = original
    assert instance.validProcSupported == original

@given(instance=dbdefinition::IndexDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::indexdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::IndexDefinition)

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_includedColumnsSupported_type(instance):
    assert isinstance(instance.includedColumnsSupported, bool)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_includedColumnsSupported_setter(instance):
    original = instance.includedColumnsSupported
    instance.includedColumnsSupported = original
    assert instance.includedColumnsSupported == original

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_clusterChangeable_type(instance):
    assert isinstance(instance.clusterChangeable, bool)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_clusterChangeable_setter(instance):
    original = instance.clusterChangeable
    instance.clusterChangeable = original
    assert instance.clusterChangeable == original

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_fillFactorSupported_type(instance):
    assert isinstance(instance.fillFactorSupported, bool)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_fillFactorSupported_setter(instance):
    original = instance.fillFactorSupported
    instance.fillFactorSupported = original
    assert instance.fillFactorSupported == original

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_percentFreeTerminology_type(instance):
    assert isinstance(instance.percentFreeTerminology, str)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_percentFreeTerminology_setter(instance):
    original = instance.percentFreeTerminology
    instance.percentFreeTerminology = original
    assert instance.percentFreeTerminology == original

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_clusteringSupported_type(instance):
    assert isinstance(instance.clusteringSupported, bool)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_clusteringSupported_setter(instance):
    original = instance.clusteringSupported
    instance.clusteringSupported = original
    assert instance.clusteringSupported == original

@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_percentFreeChangeable_type(instance):
    assert isinstance(instance.percentFreeChangeable, bool)


@given(instance=dbdefinition::IndexDefinition_strategy)
def test_dbdefinition::indexdefinition_percentFreeChangeable_setter(instance):
    original = instance.percentFreeChangeable
    instance.percentFreeChangeable = original
    assert instance.percentFreeChangeable == original

@given(instance=dbdefinition::ExtendedDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::extendeddefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::ExtendedDefinition)

@given(instance=dbdefinition::ExtendedDefinition_strategy)
def test_dbdefinition::extendeddefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbdefinition::ExtendedDefinition_strategy)
def test_dbdefinition::extendeddefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition::ExtendedDefinition_strategy)
def test_dbdefinition::extendeddefinition_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dbdefinition::ExtendedDefinition_strategy)
def test_dbdefinition::extendeddefinition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::constraintdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::ConstraintDefinition)

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_deferrableConstraintSupported_type(instance):
    assert isinstance(instance.deferrableConstraintSupported, bool)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_deferrableConstraintSupported_setter(instance):
    original = instance.deferrableConstraintSupported
    instance.deferrableConstraintSupported = original
    assert instance.deferrableConstraintSupported == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumCheckExpressionLength_type(instance):
    assert isinstance(instance.maximumCheckExpressionLength, int)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumCheckExpressionLength_setter(instance):
    original = instance.maximumCheckExpressionLength
    instance.maximumCheckExpressionLength = original
    assert instance.maximumCheckExpressionLength == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_clusteredUniqueConstraintSupported_type(instance):
    assert isinstance(instance.clusteredUniqueConstraintSupported, bool)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_clusteredUniqueConstraintSupported_setter(instance):
    original = instance.clusteredUniqueConstraintSupported
    instance.clusteredUniqueConstraintSupported = original
    assert instance.clusteredUniqueConstraintSupported == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_uniqueKeyNullable_type(instance):
    assert isinstance(instance.uniqueKeyNullable, bool)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_uniqueKeyNullable_setter(instance):
    original = instance.uniqueKeyNullable
    instance.uniqueKeyNullable = original
    assert instance.uniqueKeyNullable == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumPrimaryKeyIdentifierLength_type(instance):
    assert isinstance(instance.maximumPrimaryKeyIdentifierLength, int)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumPrimaryKeyIdentifierLength_setter(instance):
    original = instance.maximumPrimaryKeyIdentifierLength
    instance.maximumPrimaryKeyIdentifierLength = original
    assert instance.maximumPrimaryKeyIdentifierLength == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_parentUpdateDRIRuleType_type(instance):
    assert isinstance(instance.parentUpdateDRIRuleType, str)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_parentUpdateDRIRuleType_setter(instance):
    original = instance.parentUpdateDRIRuleType
    instance.parentUpdateDRIRuleType = original
    assert instance.parentUpdateDRIRuleType == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_checkOption_type(instance):
    assert isinstance(instance.checkOption, str)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_checkOption_setter(instance):
    original = instance.checkOption
    instance.checkOption = original
    assert instance.checkOption == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_parentDeleteDRIRuleType_type(instance):
    assert isinstance(instance.parentDeleteDRIRuleType, str)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_parentDeleteDRIRuleType_setter(instance):
    original = instance.parentDeleteDRIRuleType
    instance.parentDeleteDRIRuleType = original
    assert instance.parentDeleteDRIRuleType == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_clusteredPrimaryKeySupported_type(instance):
    assert isinstance(instance.clusteredPrimaryKeySupported, bool)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_clusteredPrimaryKeySupported_setter(instance):
    original = instance.clusteredPrimaryKeySupported
    instance.clusteredPrimaryKeySupported = original
    assert instance.clusteredPrimaryKeySupported == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumForeignKeyIdentifierLength_type(instance):
    assert isinstance(instance.maximumForeignKeyIdentifierLength, int)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumForeignKeyIdentifierLength_setter(instance):
    original = instance.maximumForeignKeyIdentifierLength
    instance.maximumForeignKeyIdentifierLength = original
    assert instance.maximumForeignKeyIdentifierLength == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumCheckConstraintIdentifierLength_type(instance):
    assert isinstance(instance.maximumCheckConstraintIdentifierLength, int)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_maximumCheckConstraintIdentifierLength_setter(instance):
    original = instance.maximumCheckConstraintIdentifierLength
    instance.maximumCheckConstraintIdentifierLength = original
    assert instance.maximumCheckConstraintIdentifierLength == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_informationalConstraintSupported_type(instance):
    assert isinstance(instance.informationalConstraintSupported, bool)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_informationalConstraintSupported_setter(instance):
    original = instance.informationalConstraintSupported
    instance.informationalConstraintSupported = original
    assert instance.informationalConstraintSupported == original

@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_primaryKeyNullable_type(instance):
    assert isinstance(instance.primaryKeyNullable, bool)


@given(instance=dbdefinition::ConstraintDefinition_strategy)
def test_dbdefinition::constraintdefinition_primaryKeyNullable_setter(instance):
    original = instance.primaryKeyNullable
    instance.primaryKeyNullable = original
    assert instance.primaryKeyNullable == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::columndefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::ColumnDefinition)

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityIncrementSupported_type(instance):
    assert isinstance(instance.identityIncrementSupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityIncrementSupported_setter(instance):
    original = instance.identityIncrementSupported
    instance.identityIncrementSupported = original
    assert instance.identityIncrementSupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityMinimumSupported_type(instance):
    assert isinstance(instance.identityMinimumSupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityMinimumSupported_setter(instance):
    original = instance.identityMinimumSupported
    instance.identityMinimumSupported = original
    assert instance.identityMinimumSupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identitySupported_type(instance):
    assert isinstance(instance.identitySupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identitySupported_setter(instance):
    original = instance.identitySupported
    instance.identitySupported = original
    assert instance.identitySupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_computedSupported_type(instance):
    assert isinstance(instance.computedSupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_computedSupported_setter(instance):
    original = instance.computedSupported
    instance.computedSupported = original
    assert instance.computedSupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityCycleSupported_type(instance):
    assert isinstance(instance.identityCycleSupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityCycleSupported_setter(instance):
    original = instance.identityCycleSupported
    instance.identityCycleSupported = original
    assert instance.identityCycleSupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityStartValueSupported_type(instance):
    assert isinstance(instance.identityStartValueSupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityStartValueSupported_setter(instance):
    original = instance.identityStartValueSupported
    instance.identityStartValueSupported = original
    assert instance.identityStartValueSupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityMaximumSupported_type(instance):
    assert isinstance(instance.identityMaximumSupported, bool)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_identityMaximumSupported_setter(instance):
    original = instance.identityMaximumSupported
    instance.identityMaximumSupported = original
    assert instance.identityMaximumSupported == original

@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::ColumnDefinition_strategy)
def test_dbdefinition::columndefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::triggerdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::TriggerDefinition)

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_insteadOfTriggerSupported_type(instance):
    assert isinstance(instance.insteadOfTriggerSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_insteadOfTriggerSupported_setter(instance):
    original = instance.insteadOfTriggerSupported
    instance.insteadOfTriggerSupported = original
    assert instance.insteadOfTriggerSupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_rowTriggerReferenceSupported_type(instance):
    assert isinstance(instance.rowTriggerReferenceSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_rowTriggerReferenceSupported_setter(instance):
    original = instance.rowTriggerReferenceSupported
    instance.rowTriggerReferenceSupported = original
    assert instance.rowTriggerReferenceSupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_granularitySupported_type(instance):
    assert isinstance(instance.granularitySupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_granularitySupported_setter(instance):
    original = instance.granularitySupported
    instance.granularitySupported = original
    assert instance.granularitySupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_maximumActionBodyLength_type(instance):
    assert isinstance(instance.maximumActionBodyLength, int)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_maximumActionBodyLength_setter(instance):
    original = instance.maximumActionBodyLength
    instance.maximumActionBodyLength = original
    assert instance.maximumActionBodyLength == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_tableTriggerReferenceSupported_type(instance):
    assert isinstance(instance.tableTriggerReferenceSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_tableTriggerReferenceSupported_setter(instance):
    original = instance.tableTriggerReferenceSupported
    instance.tableTriggerReferenceSupported = original
    assert instance.tableTriggerReferenceSupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_maximumReferencePartLength_type(instance):
    assert isinstance(instance.maximumReferencePartLength, int)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_maximumReferencePartLength_setter(instance):
    original = instance.maximumReferencePartLength
    instance.maximumReferencePartLength = original
    assert instance.maximumReferencePartLength == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_referencesClauseSupported_type(instance):
    assert isinstance(instance.referencesClauseSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_referencesClauseSupported_setter(instance):
    original = instance.referencesClauseSupported
    instance.referencesClauseSupported = original
    assert instance.referencesClauseSupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_typeSupported_type(instance):
    assert isinstance(instance.typeSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_typeSupported_setter(instance):
    original = instance.typeSupported
    instance.typeSupported = original
    assert instance.typeSupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_perColumnUpdateTriggerSupported_type(instance):
    assert isinstance(instance.perColumnUpdateTriggerSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_perColumnUpdateTriggerSupported_setter(instance):
    original = instance.perColumnUpdateTriggerSupported
    instance.perColumnUpdateTriggerSupported = original
    assert instance.perColumnUpdateTriggerSupported == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_whenClauseSupported_type(instance):
    assert isinstance(instance.whenClauseSupported, bool)


@given(instance=dbdefinition::TriggerDefinition_strategy)
def test_dbdefinition::triggerdefinition_whenClauseSupported_setter(instance):
    original = instance.whenClauseSupported
    instance.whenClauseSupported = original
    assert instance.whenClauseSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::storedproceduredefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::StoredProcedureDefinition)

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterInitValueSupported_type(instance):
    assert isinstance(instance.parameterInitValueSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterInitValueSupported_setter(instance):
    original = instance.parameterInitValueSupported
    instance.parameterInitValueSupported = original
    assert instance.parameterInitValueSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_nullInputActionSupported_type(instance):
    assert isinstance(instance.nullInputActionSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_nullInputActionSupported_setter(instance):
    original = instance.nullInputActionSupported
    instance.nullInputActionSupported = original
    assert instance.nullInputActionSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterStyle_type(instance):
    assert isinstance(instance.parameterStyle, str)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterStyle_setter(instance):
    original = instance.parameterStyle
    instance.parameterStyle = original
    assert instance.parameterStyle == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_determininsticSupported_type(instance):
    assert isinstance(instance.determininsticSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_determininsticSupported_setter(instance):
    original = instance.determininsticSupported
    instance.determininsticSupported = original
    assert instance.determininsticSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_returnTypeSupported_type(instance):
    assert isinstance(instance.returnTypeSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_returnTypeSupported_setter(instance):
    original = instance.returnTypeSupported
    instance.returnTypeSupported = original
    assert instance.returnTypeSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_functionLanguageType_type(instance):
    assert isinstance(instance.functionLanguageType, str)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_functionLanguageType_setter(instance):
    original = instance.functionLanguageType
    instance.functionLanguageType = original
    assert instance.functionLanguageType == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_returnedTypeDeclarationConstraintSupported_type(instance):
    assert isinstance(instance.returnedTypeDeclarationConstraintSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_returnedTypeDeclarationConstraintSupported_setter(instance):
    original = instance.returnedTypeDeclarationConstraintSupported
    instance.returnedTypeDeclarationConstraintSupported = original
    assert instance.returnedTypeDeclarationConstraintSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterStyleSupported_type(instance):
    assert isinstance(instance.parameterStyleSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterStyleSupported_setter(instance):
    original = instance.parameterStyleSupported
    instance.parameterStyleSupported = original
    assert instance.parameterStyleSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_packageGenerationSupported_type(instance):
    assert isinstance(instance.packageGenerationSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_packageGenerationSupported_setter(instance):
    original = instance.packageGenerationSupported
    instance.packageGenerationSupported = original
    assert instance.packageGenerationSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_languageType_type(instance):
    assert isinstance(instance.languageType, str)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_languageType_setter(instance):
    original = instance.languageType
    instance.languageType = original
    assert instance.languageType == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_maximumActionBodyLength_type(instance):
    assert isinstance(instance.maximumActionBodyLength, int)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_maximumActionBodyLength_setter(instance):
    original = instance.maximumActionBodyLength
    instance.maximumActionBodyLength = original
    assert instance.maximumActionBodyLength == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterDeclarationConstraintSupported_type(instance):
    assert isinstance(instance.parameterDeclarationConstraintSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_parameterDeclarationConstraintSupported_setter(instance):
    original = instance.parameterDeclarationConstraintSupported
    instance.parameterDeclarationConstraintSupported = original
    assert instance.parameterDeclarationConstraintSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_returnedNullSupported_type(instance):
    assert isinstance(instance.returnedNullSupported, bool)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_returnedNullSupported_setter(instance):
    original = instance.returnedNullSupported
    instance.returnedNullSupported = original
    assert instance.returnedNullSupported == original

@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_procedureType_type(instance):
    assert isinstance(instance.procedureType, str)


@given(instance=dbdefinition::StoredProcedureDefinition_strategy)
def test_dbdefinition::storedproceduredefinition_procedureType_setter(instance):
    original = instance.procedureType
    instance.procedureType = original
    assert instance.procedureType == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::tablespacedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::TableSpaceDefinition)

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_containerInitialSizeSupported_type(instance):
    assert isinstance(instance.containerInitialSizeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_containerInitialSizeSupported_setter(instance):
    original = instance.containerInitialSizeSupported
    instance.containerInitialSizeSupported = original
    assert instance.containerInitialSizeSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_prefetchSizeSupported_type(instance):
    assert isinstance(instance.prefetchSizeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_prefetchSizeSupported_setter(instance):
    original = instance.prefetchSizeSupported
    instance.prefetchSizeSupported = original
    assert instance.prefetchSizeSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_typeSupported_type(instance):
    assert isinstance(instance.typeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_typeSupported_setter(instance):
    original = instance.typeSupported
    instance.typeSupported = original
    assert instance.typeSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_containerExtentSizeSupported_type(instance):
    assert isinstance(instance.containerExtentSizeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_containerExtentSizeSupported_setter(instance):
    original = instance.containerExtentSizeSupported
    instance.containerExtentSizeSupported = original
    assert instance.containerExtentSizeSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_bufferPoolSupported_type(instance):
    assert isinstance(instance.bufferPoolSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_bufferPoolSupported_setter(instance):
    original = instance.bufferPoolSupported
    instance.bufferPoolSupported = original
    assert instance.bufferPoolSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_extentSizeSupported_type(instance):
    assert isinstance(instance.extentSizeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_extentSizeSupported_setter(instance):
    original = instance.extentSizeSupported
    instance.extentSizeSupported = original
    assert instance.extentSizeSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_tableSpaceType_type(instance):
    assert isinstance(instance.tableSpaceType, str)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_tableSpaceType_setter(instance):
    original = instance.tableSpaceType
    instance.tableSpaceType = original
    assert instance.tableSpaceType == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_managedBySupported_type(instance):
    assert isinstance(instance.managedBySupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_managedBySupported_setter(instance):
    original = instance.managedBySupported
    instance.managedBySupported = original
    assert instance.managedBySupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_defaultSupported_type(instance):
    assert isinstance(instance.defaultSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_defaultSupported_setter(instance):
    original = instance.defaultSupported
    instance.defaultSupported = original
    assert instance.defaultSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_pageSizeSupported_type(instance):
    assert isinstance(instance.pageSizeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_pageSizeSupported_setter(instance):
    original = instance.pageSizeSupported
    instance.pageSizeSupported = original
    assert instance.pageSizeSupported == original

@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_containerMaximumSizeSupported_type(instance):
    assert isinstance(instance.containerMaximumSizeSupported, bool)


@given(instance=dbdefinition::TableSpaceDefinition_strategy)
def test_dbdefinition::tablespacedefinition_containerMaximumSizeSupported_setter(instance):
    original = instance.containerMaximumSizeSupported
    instance.containerMaximumSizeSupported = original
    assert instance.containerMaximumSizeSupported == original

@given(instance=dbdefinition::NicknameDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::nicknamedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::NicknameDefinition)

@given(instance=dbdefinition::NicknameDefinition_strategy)
def test_dbdefinition::nicknamedefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::NicknameDefinition_strategy)
def test_dbdefinition::nicknamedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::NicknameDefinition_strategy)
def test_dbdefinition::nicknamedefinition_indexSupported_type(instance):
    assert isinstance(instance.indexSupported, bool)


@given(instance=dbdefinition::NicknameDefinition_strategy)
def test_dbdefinition::nicknamedefinition_indexSupported_setter(instance):
    original = instance.indexSupported
    instance.indexSupported = original
    assert instance.indexSupported == original

@given(instance=dbdefinition::NicknameDefinition_strategy)
def test_dbdefinition::nicknamedefinition_constraintSupported_type(instance):
    assert isinstance(instance.constraintSupported, bool)


@given(instance=dbdefinition::NicknameDefinition_strategy)
def test_dbdefinition::nicknamedefinition_constraintSupported_setter(instance):
    original = instance.constraintSupported
    instance.constraintSupported = original
    assert instance.constraintSupported == original

@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::sqlsyntaxdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::SQLSyntaxDefinition)

@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
def test_dbdefinition::sqlsyntaxdefinition_operators_type(instance):
    assert isinstance(instance.operators, str)


@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
def test_dbdefinition::sqlsyntaxdefinition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
def test_dbdefinition::sqlsyntaxdefinition_terminationCharacter_type(instance):
    assert isinstance(instance.terminationCharacter, str)


@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
def test_dbdefinition::sqlsyntaxdefinition_terminationCharacter_setter(instance):
    original = instance.terminationCharacter
    instance.terminationCharacter = original
    assert instance.terminationCharacter == original

@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
def test_dbdefinition::sqlsyntaxdefinition_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=dbdefinition::SQLSyntaxDefinition_strategy)
def test_dbdefinition::sqlsyntaxdefinition_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=dbdefinition::QueryDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::querydefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::QueryDefinition)

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_extendedGroupingSupported_type(instance):
    assert isinstance(instance.extendedGroupingSupported, bool)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_extendedGroupingSupported_setter(instance):
    original = instance.extendedGroupingSupported
    instance.extendedGroupingSupported = original
    assert instance.extendedGroupingSupported == original

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_hostVariableMarkerSupported_type(instance):
    assert isinstance(instance.hostVariableMarkerSupported, bool)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_hostVariableMarkerSupported_setter(instance):
    original = instance.hostVariableMarkerSupported
    instance.hostVariableMarkerSupported = original
    assert instance.hostVariableMarkerSupported == original

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_defaultKeywordForInsertValueSupported_type(instance):
    assert isinstance(instance.defaultKeywordForInsertValueSupported, bool)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_defaultKeywordForInsertValueSupported_setter(instance):
    original = instance.defaultKeywordForInsertValueSupported
    instance.defaultKeywordForInsertValueSupported = original
    assert instance.defaultKeywordForInsertValueSupported == original

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_castExpressionSupported_type(instance):
    assert isinstance(instance.castExpressionSupported, bool)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_castExpressionSupported_setter(instance):
    original = instance.castExpressionSupported
    instance.castExpressionSupported = original
    assert instance.castExpressionSupported == original

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_identifierQuoteString_type(instance):
    assert isinstance(instance.identifierQuoteString, str)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_identifierQuoteString_setter(instance):
    original = instance.identifierQuoteString
    instance.identifierQuoteString = original
    assert instance.identifierQuoteString == original

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_tableAliasInDeleteSupported_type(instance):
    assert isinstance(instance.tableAliasInDeleteSupported, bool)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_tableAliasInDeleteSupported_setter(instance):
    original = instance.tableAliasInDeleteSupported
    instance.tableAliasInDeleteSupported = original
    assert instance.tableAliasInDeleteSupported == original

@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_hostVariableMarker_type(instance):
    assert isinstance(instance.hostVariableMarker, str)


@given(instance=dbdefinition::QueryDefinition_strategy)
def test_dbdefinition::querydefinition_hostVariableMarker_setter(instance):
    original = instance.hostVariableMarker
    instance.hostVariableMarker = original
    assert instance.hostVariableMarker == original

@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::userdefinedtypedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::UserDefinedTypeDefinition)

@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_distinctTypeSupported_type(instance):
    assert isinstance(instance.distinctTypeSupported, bool)


@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_distinctTypeSupported_setter(instance):
    original = instance.distinctTypeSupported
    instance.distinctTypeSupported = original
    assert instance.distinctTypeSupported == original

@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_structuredTypeSupported_type(instance):
    assert isinstance(instance.structuredTypeSupported, bool)


@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_structuredTypeSupported_setter(instance):
    original = instance.structuredTypeSupported
    instance.structuredTypeSupported = original
    assert instance.structuredTypeSupported == original

@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_defaultValueSupported_type(instance):
    assert isinstance(instance.defaultValueSupported, bool)


@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_defaultValueSupported_setter(instance):
    original = instance.defaultValueSupported
    instance.defaultValueSupported = original
    assert instance.defaultValueSupported == original

@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::UserDefinedTypeDefinition_strategy)
def test_dbdefinition::userdefinedtypedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::predefineddatatypedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::PredefinedDataTypeDefinition)

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_bitDataSupported_type(instance):
    assert isinstance(instance.bitDataSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_bitDataSupported_setter(instance):
    original = instance.bitDataSupported
    instance.bitDataSupported = original
    assert instance.bitDataSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_largeValueSpecifierSupported_type(instance):
    assert isinstance(instance.largeValueSpecifierSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_largeValueSpecifierSupported_setter(instance):
    original = instance.largeValueSpecifierSupported
    instance.largeValueSpecifierSupported = original
    assert instance.largeValueSpecifierSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_nullableSupported_type(instance):
    assert isinstance(instance.nullableSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_nullableSupported_setter(instance):
    original = instance.nullableSupported
    instance.nullableSupported = original
    assert instance.nullableSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_minimumValue_type(instance):
    assert isinstance(instance.minimumValue, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_minimumValue_setter(instance):
    original = instance.minimumValue
    instance.minimumValue = original
    assert instance.minimumValue == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultLength_type(instance):
    assert isinstance(instance.defaultLength, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultLength_setter(instance):
    original = instance.defaultLength
    instance.defaultLength = original
    assert instance.defaultLength == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_multipleColumnsSupported_type(instance):
    assert isinstance(instance.multipleColumnsSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_multipleColumnsSupported_setter(instance):
    original = instance.multipleColumnsSupported
    instance.multipleColumnsSupported = original
    assert instance.multipleColumnsSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumScale_type(instance):
    assert isinstance(instance.maximumScale, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumScale_setter(instance):
    original = instance.maximumScale
    instance.maximumScale = original
    assert instance.maximumScale == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_clusteringSupported_type(instance):
    assert isinstance(instance.clusteringSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_clusteringSupported_setter(instance):
    original = instance.clusteringSupported
    instance.clusteringSupported = original
    assert instance.clusteringSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_fillFactorSupported_type(instance):
    assert isinstance(instance.fillFactorSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_fillFactorSupported_setter(instance):
    original = instance.fillFactorSupported
    instance.fillFactorSupported = original
    assert instance.fillFactorSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultScale_type(instance):
    assert isinstance(instance.defaultScale, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultScale_setter(instance):
    original = instance.defaultScale
    instance.defaultScale = original
    assert instance.defaultScale == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_keyConstraintSupported_type(instance):
    assert isinstance(instance.keyConstraintSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_keyConstraintSupported_setter(instance):
    original = instance.keyConstraintSupported
    instance.keyConstraintSupported = original
    assert instance.keyConstraintSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_trailingFieldQualifierSupported_type(instance):
    assert isinstance(instance.trailingFieldQualifierSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_trailingFieldQualifierSupported_setter(instance):
    original = instance.trailingFieldQualifierSupported
    instance.trailingFieldQualifierSupported = original
    assert instance.trailingFieldQualifierSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_encodingScheme_type(instance):
    assert isinstance(instance.encodingScheme, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_encodingScheme_setter(instance):
    original = instance.encodingScheme
    instance.encodingScheme = original
    assert instance.encodingScheme == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_jdbcEnumType_type(instance):
    assert isinstance(instance.jdbcEnumType, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_jdbcEnumType_setter(instance):
    original = instance.jdbcEnumType
    instance.jdbcEnumType = original
    assert instance.jdbcEnumType == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultPrecision_type(instance):
    assert isinstance(instance.defaultPrecision, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultPrecision_setter(instance):
    original = instance.defaultPrecision
    instance.defaultPrecision = original
    assert instance.defaultPrecision == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthSupported_type(instance):
    assert isinstance(instance.lengthSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthSupported_setter(instance):
    original = instance.lengthSupported
    instance.lengthSupported = original
    assert instance.lengthSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthUnit_type(instance):
    assert isinstance(instance.lengthUnit, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthUnit_setter(instance):
    original = instance.lengthUnit
    instance.lengthUnit = original
    assert instance.lengthUnit == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumLength_type(instance):
    assert isinstance(instance.maximumLength, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumLength_setter(instance):
    original = instance.maximumLength
    instance.maximumLength = original
    assert instance.maximumLength == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_leadingFieldQualifierSupported_type(instance):
    assert isinstance(instance.leadingFieldQualifierSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_leadingFieldQualifierSupported_setter(instance):
    original = instance.leadingFieldQualifierSupported
    instance.leadingFieldQualifierSupported = original
    assert instance.leadingFieldQualifierSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_scaleSupported_type(instance):
    assert isinstance(instance.scaleSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_scaleSupported_setter(instance):
    original = instance.scaleSupported
    instance.scaleSupported = original
    assert instance.scaleSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_identitySupported_type(instance):
    assert isinstance(instance.identitySupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_identitySupported_setter(instance):
    original = instance.identitySupported
    instance.identitySupported = original
    assert instance.identitySupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_displayNameSupported_type(instance):
    assert isinstance(instance.displayNameSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_displayNameSupported_setter(instance):
    original = instance.displayNameSupported
    instance.displayNameSupported = original
    assert instance.displayNameSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_groupingSupported_type(instance):
    assert isinstance(instance.groupingSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_groupingSupported_setter(instance):
    original = instance.groupingSupported
    instance.groupingSupported = original
    assert instance.groupingSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_precisionSupported_type(instance):
    assert isinstance(instance.precisionSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_precisionSupported_setter(instance):
    original = instance.precisionSupported
    instance.precisionSupported = original
    assert instance.precisionSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthSemantic_type(instance):
    assert isinstance(instance.lengthSemantic, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthSemantic_setter(instance):
    original = instance.lengthSemantic
    instance.lengthSemantic = original
    assert instance.lengthSemantic == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_largeValueSpecifierName_type(instance):
    assert isinstance(instance.largeValueSpecifierName, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_largeValueSpecifierName_setter(instance):
    original = instance.largeValueSpecifierName
    instance.largeValueSpecifierName = original
    assert instance.largeValueSpecifierName == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_characterSet_type(instance):
    assert isinstance(instance.characterSet, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_characterSet_setter(instance):
    original = instance.characterSet
    instance.characterSet = original
    assert instance.characterSet == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_orderingSupported_type(instance):
    assert isinstance(instance.orderingSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_orderingSupported_setter(instance):
    original = instance.orderingSupported
    instance.orderingSupported = original
    assert instance.orderingSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultValueTypes_type(instance):
    assert isinstance(instance.defaultValueTypes, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultValueTypes_setter(instance):
    original = instance.defaultValueTypes
    instance.defaultValueTypes = original
    assert instance.defaultValueTypes == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_javaClassName_type(instance):
    assert isinstance(instance.javaClassName, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_javaClassName_setter(instance):
    original = instance.javaClassName
    instance.javaClassName = original
    assert instance.javaClassName == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_fieldQualifierSeparator_type(instance):
    assert isinstance(instance.fieldQualifierSeparator, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_fieldQualifierSeparator_setter(instance):
    original = instance.fieldQualifierSeparator
    instance.fieldQualifierSeparator = original
    assert instance.fieldQualifierSeparator == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_cutoffPrecision_type(instance):
    assert isinstance(instance.cutoffPrecision, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_cutoffPrecision_setter(instance):
    original = instance.cutoffPrecision
    instance.cutoffPrecision = original
    assert instance.cutoffPrecision == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_encodingSchemeSuffix_type(instance):
    assert isinstance(instance.encodingSchemeSuffix, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_encodingSchemeSuffix_setter(instance):
    original = instance.encodingSchemeSuffix
    instance.encodingSchemeSuffix = original
    assert instance.encodingSchemeSuffix == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthSemanticSupported_type(instance):
    assert isinstance(instance.lengthSemanticSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_lengthSemanticSupported_setter(instance):
    original = instance.lengthSemanticSupported
    instance.lengthSemanticSupported = original
    assert instance.lengthSemanticSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_characterSetSuffix_type(instance):
    assert isinstance(instance.characterSetSuffix, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_characterSetSuffix_setter(instance):
    original = instance.characterSetSuffix
    instance.characterSetSuffix = original
    assert instance.characterSetSuffix == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumValue_type(instance):
    assert isinstance(instance.maximumValue, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumValue_setter(instance):
    original = instance.maximumValue
    instance.maximumValue = original
    assert instance.maximumValue == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_largeValueSpecifierLength_type(instance):
    assert isinstance(instance.largeValueSpecifierLength, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_largeValueSpecifierLength_setter(instance):
    original = instance.largeValueSpecifierLength
    instance.largeValueSpecifierLength = original
    assert instance.largeValueSpecifierLength == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumPrecision_type(instance):
    assert isinstance(instance.maximumPrecision, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_maximumPrecision_setter(instance):
    original = instance.maximumPrecision
    instance.maximumPrecision = original
    assert instance.maximumPrecision == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultSupported_type(instance):
    assert isinstance(instance.defaultSupported, bool)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_defaultSupported_setter(instance):
    original = instance.defaultSupported
    instance.defaultSupported = original
    assert instance.defaultSupported == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_minimumScale_type(instance):
    assert isinstance(instance.minimumScale, int)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_minimumScale_setter(instance):
    original = instance.minimumScale
    instance.minimumScale = original
    assert instance.minimumScale == original

@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_languageType_type(instance):
    assert isinstance(instance.languageType, str)


@given(instance=dbdefinition::PredefinedDataTypeDefinition_strategy)
def test_dbdefinition::predefineddatatypedefinition_languageType_setter(instance):
    original = instance.languageType
    instance.languageType = original
    assert instance.languageType == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition::databasevendordefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition::DatabaseVendorDefinition)

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_sqlUDFSupported_type(instance):
    assert isinstance(instance.sqlUDFSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_sqlUDFSupported_setter(instance):
    original = instance.sqlUDFSupported
    instance.sqlUDFSupported = original
    assert instance.sqlUDFSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_joinSupported_type(instance):
    assert isinstance(instance.joinSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_joinSupported_setter(instance):
    original = instance.joinSupported
    instance.joinSupported = original
    assert instance.joinSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_mQTSupported_type(instance):
    assert isinstance(instance.mQTSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_mQTSupported_setter(instance):
    original = instance.mQTSupported
    instance.mQTSupported = original
    assert instance.mQTSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_synonymSupported_type(instance):
    assert isinstance(instance.synonymSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_synonymSupported_setter(instance):
    original = instance.synonymSupported
    instance.synonymSupported = original
    assert instance.synonymSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_snapshotViewSupported_type(instance):
    assert isinstance(instance.snapshotViewSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_snapshotViewSupported_setter(instance):
    original = instance.snapshotViewSupported
    instance.snapshotViewSupported = original
    assert instance.snapshotViewSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_roleAuthorizationSupported_type(instance):
    assert isinstance(instance.roleAuthorizationSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_roleAuthorizationSupported_setter(instance):
    original = instance.roleAuthorizationSupported
    instance.roleAuthorizationSupported = original
    assert instance.roleAuthorizationSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_triggerSupported_type(instance):
    assert isinstance(instance.triggerSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_triggerSupported_setter(instance):
    original = instance.triggerSupported
    instance.triggerSupported = original
    assert instance.triggerSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_userSupported_type(instance):
    assert isinstance(instance.userSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_userSupported_setter(instance):
    original = instance.userSupported
    instance.userSupported = original
    assert instance.userSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_sequenceSupported_type(instance):
    assert isinstance(instance.sequenceSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_sequenceSupported_setter(instance):
    original = instance.sequenceSupported
    instance.sequenceSupported = original
    assert instance.sequenceSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_tablespacesSupported_type(instance):
    assert isinstance(instance.tablespacesSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_tablespacesSupported_setter(instance):
    original = instance.tablespacesSupported
    instance.tablespacesSupported = original
    assert instance.tablespacesSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_domainSupported_type(instance):
    assert isinstance(instance.domainSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_domainSupported_setter(instance):
    original = instance.domainSupported
    instance.domainSupported = original
    assert instance.domainSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_groupSupported_type(instance):
    assert isinstance(instance.groupSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_groupSupported_setter(instance):
    original = instance.groupSupported
    instance.groupSupported = original
    assert instance.groupSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_userDefinedTypeSupported_type(instance):
    assert isinstance(instance.userDefinedTypeSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_userDefinedTypeSupported_setter(instance):
    original = instance.userDefinedTypeSupported
    instance.userDefinedTypeSupported = original
    assert instance.userDefinedTypeSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_viewTriggerSupported_type(instance):
    assert isinstance(instance.viewTriggerSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_viewTriggerSupported_setter(instance):
    original = instance.viewTriggerSupported
    instance.viewTriggerSupported = original
    assert instance.viewTriggerSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_packageSupported_type(instance):
    assert isinstance(instance.packageSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_packageSupported_setter(instance):
    original = instance.packageSupported
    instance.packageSupported = original
    assert instance.packageSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_schemaSupported_type(instance):
    assert isinstance(instance.schemaSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_schemaSupported_setter(instance):
    original = instance.schemaSupported
    instance.schemaSupported = original
    assert instance.schemaSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_eventSupported_type(instance):
    assert isinstance(instance.eventSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_eventSupported_setter(instance):
    original = instance.eventSupported
    instance.eventSupported = original
    assert instance.eventSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_constraintsSupported_type(instance):
    assert isinstance(instance.constraintsSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_constraintsSupported_setter(instance):
    original = instance.constraintsSupported
    instance.constraintsSupported = original
    assert instance.constraintsSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_constructedDataTypeSupported_type(instance):
    assert isinstance(instance.constructedDataTypeSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_constructedDataTypeSupported_setter(instance):
    original = instance.constructedDataTypeSupported
    instance.constructedDataTypeSupported = original
    assert instance.constructedDataTypeSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_roleSupported_type(instance):
    assert isinstance(instance.roleSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_roleSupported_setter(instance):
    original = instance.roleSupported
    instance.roleSupported = original
    assert instance.roleSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_authorizationIdentifierSupported_type(instance):
    assert isinstance(instance.authorizationIdentifierSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_authorizationIdentifierSupported_setter(instance):
    original = instance.authorizationIdentifierSupported
    instance.authorizationIdentifierSupported = original
    assert instance.authorizationIdentifierSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_aliasSupported_type(instance):
    assert isinstance(instance.aliasSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_aliasSupported_setter(instance):
    original = instance.aliasSupported
    instance.aliasSupported = original
    assert instance.aliasSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_maximumCommentLength_type(instance):
    assert isinstance(instance.maximumCommentLength, int)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_maximumCommentLength_setter(instance):
    original = instance.maximumCommentLength
    instance.maximumCommentLength = original
    assert instance.maximumCommentLength == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_xmlSupported_type(instance):
    assert isinstance(instance.xmlSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_xmlSupported_setter(instance):
    original = instance.xmlSupported
    instance.xmlSupported = original
    assert instance.xmlSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_storedProcedureSupported_type(instance):
    assert isinstance(instance.storedProcedureSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_storedProcedureSupported_setter(instance):
    original = instance.storedProcedureSupported
    instance.storedProcedureSupported = original
    assert instance.storedProcedureSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_SQLStatementSupported_type(instance):
    assert isinstance(instance.SQLStatementSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_SQLStatementSupported_setter(instance):
    original = instance.SQLStatementSupported
    instance.SQLStatementSupported = original
    assert instance.SQLStatementSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_maximumIdentifierLength_type(instance):
    assert isinstance(instance.maximumIdentifierLength, int)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_uDFSupported_type(instance):
    assert isinstance(instance.uDFSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_uDFSupported_setter(instance):
    original = instance.uDFSupported
    instance.uDFSupported = original
    assert instance.uDFSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_vendor_type(instance):
    assert isinstance(instance.vendor, str)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_nicknameSupported_type(instance):
    assert isinstance(instance.nicknameSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_nicknameSupported_setter(instance):
    original = instance.nicknameSupported
    instance.nicknameSupported = original
    assert instance.nicknameSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_quotedDMLSupported_type(instance):
    assert isinstance(instance.quotedDMLSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_quotedDMLSupported_setter(instance):
    original = instance.quotedDMLSupported
    instance.quotedDMLSupported = original
    assert instance.quotedDMLSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_mQTIndexSupported_type(instance):
    assert isinstance(instance.mQTIndexSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_mQTIndexSupported_setter(instance):
    original = instance.mQTIndexSupported
    instance.mQTIndexSupported = original
    assert instance.mQTIndexSupported == original

@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_quotedDDLSupported_type(instance):
    assert isinstance(instance.quotedDDLSupported, bool)


@given(instance=dbdefinition::DatabaseVendorDefinition_strategy)
def test_dbdefinition::databasevendordefinition_quotedDDLSupported_setter(instance):
    original = instance.quotedDDLSupported
    instance.quotedDDLSupported = original
    assert instance.quotedDDLSupported == original
