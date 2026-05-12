import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dbdefinition_PrivilegeDefinition,
    dbdefinition_FieldQualifierDefinition,
    dbdefinition_ConstructedDataTypeDefinition,
    dbdefinition_PrivilegedElementDefinition,
    dbdefinition_DebuggerDefinition,
    dbdefinition_ViewDefinition,
    dbdefinition_SchemaDefinition,
    dbdefinition_SequenceDefinition,
    dbdefinition_TableDefinition,
    dbdefinition_IndexDefinition,
    dbdefinition_ExtendedDefinition,
    dbdefinition_ConstraintDefinition,
    dbdefinition_ColumnDefinition,
    dbdefinition_TriggerDefinition,
    dbdefinition_StoredProcedureDefinition,
    dbdefinition_TableSpaceDefinition,
    dbdefinition_NicknameDefinition,
    dbdefinition_SQLSyntaxDefinition,
    dbdefinition_QueryDefinition,
    dbdefinition_UserDefinedTypeDefinition,
    dbdefinition_PredefinedDataTypeDefinition,
    dbdefinition_DatabaseVendorDefinition,
    ParameterStyle,
    ProcedureType,
    LanguageType,
    CheckOption,
    ParentDeleteDRIRuleType,
    LengthUnit,
    ParentUpdateDRIRuleType,
    TableSpaceType,
    PercentFreeTerminology,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbdefinition_privilegedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_PrivilegeDefinition)


def test_dbdefinition_privilegedefinition_constructor_exists():
    assert callable(dbdefinition_PrivilegeDefinition.__init__)


def test_dbdefinition_privilegedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_PrivilegeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdefinition_privilegedefinition_has_name():
    assert hasattr(dbdefinition_PrivilegeDefinition, "name")
    descriptor = None
    for klass in dbdefinition_PrivilegeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_fieldqualifierdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_FieldQualifierDefinition)


def test_dbdefinition_fieldqualifierdefinition_constructor_exists():
    assert callable(dbdefinition_FieldQualifierDefinition.__init__)


def test_dbdefinition_fieldqualifierdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_FieldQualifierDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maximumScale" in params, "Missing parameter 'maximumScale'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scaleSupported" in params, "Missing parameter 'scaleSupported'"
    assert "defaultPrecision" in params, "Missing parameter 'defaultPrecision'"
    assert "maximumPrecision" in params, "Missing parameter 'maximumPrecision'"
    assert "precisionSupported" in params, "Missing parameter 'precisionSupported'"
    assert "defaultScale" in params, "Missing parameter 'defaultScale'"

def test_dbdefinition_fieldqualifierdefinition_has_maximumScale():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "maximumScale")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "maximumScale" in klass.__dict__:
            descriptor = klass.__dict__["maximumScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_fieldqualifierdefinition_has_name():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "name")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_fieldqualifierdefinition_has_scaleSupported():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "scaleSupported")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "scaleSupported" in klass.__dict__:
            descriptor = klass.__dict__["scaleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_fieldqualifierdefinition_has_defaultPrecision():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "defaultPrecision")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "defaultPrecision" in klass.__dict__:
            descriptor = klass.__dict__["defaultPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_fieldqualifierdefinition_has_maximumPrecision():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "maximumPrecision")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "maximumPrecision" in klass.__dict__:
            descriptor = klass.__dict__["maximumPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_fieldqualifierdefinition_has_precisionSupported():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "precisionSupported")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "precisionSupported" in klass.__dict__:
            descriptor = klass.__dict__["precisionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_fieldqualifierdefinition_has_defaultScale():
    assert hasattr(dbdefinition_FieldQualifierDefinition, "defaultScale")
    descriptor = None
    for klass in dbdefinition_FieldQualifierDefinition.__mro__:
        if "defaultScale" in klass.__dict__:
            descriptor = klass.__dict__["defaultScale"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_constructeddatatypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ConstructedDataTypeDefinition)


def test_dbdefinition_constructeddatatypedefinition_constructor_exists():
    assert callable(dbdefinition_ConstructedDataTypeDefinition.__init__)


def test_dbdefinition_constructeddatatypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ConstructedDataTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "referenceDatatypeSupported" in params, "Missing parameter 'referenceDatatypeSupported'"
    assert "rowDatatypeSupported" in params, "Missing parameter 'rowDatatypeSupported'"
    assert "cursorDatatypeSupported" in params, "Missing parameter 'cursorDatatypeSupported'"
    assert "arrayDatatypeSupported" in params, "Missing parameter 'arrayDatatypeSupported'"
    assert "multisetDatatypeSupported" in params, "Missing parameter 'multisetDatatypeSupported'"

def test_dbdefinition_constructeddatatypedefinition_has_referenceDatatypeSupported():
    assert hasattr(dbdefinition_ConstructedDataTypeDefinition, "referenceDatatypeSupported")
    descriptor = None
    for klass in dbdefinition_ConstructedDataTypeDefinition.__mro__:
        if "referenceDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["referenceDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constructeddatatypedefinition_has_rowDatatypeSupported():
    assert hasattr(dbdefinition_ConstructedDataTypeDefinition, "rowDatatypeSupported")
    descriptor = None
    for klass in dbdefinition_ConstructedDataTypeDefinition.__mro__:
        if "rowDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["rowDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constructeddatatypedefinition_has_cursorDatatypeSupported():
    assert hasattr(dbdefinition_ConstructedDataTypeDefinition, "cursorDatatypeSupported")
    descriptor = None
    for klass in dbdefinition_ConstructedDataTypeDefinition.__mro__:
        if "cursorDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["cursorDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constructeddatatypedefinition_has_arrayDatatypeSupported():
    assert hasattr(dbdefinition_ConstructedDataTypeDefinition, "arrayDatatypeSupported")
    descriptor = None
    for klass in dbdefinition_ConstructedDataTypeDefinition.__mro__:
        if "arrayDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["arrayDatatypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constructeddatatypedefinition_has_multisetDatatypeSupported():
    assert hasattr(dbdefinition_ConstructedDataTypeDefinition, "multisetDatatypeSupported")
    descriptor = None
    for klass in dbdefinition_ConstructedDataTypeDefinition.__mro__:
        if "multisetDatatypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["multisetDatatypeSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_privilegedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_PrivilegedElementDefinition)


def test_dbdefinition_privilegedelementdefinition_constructor_exists():
    assert callable(dbdefinition_PrivilegedElementDefinition.__init__)


def test_dbdefinition_privilegedelementdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_PrivilegedElementDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdefinition_privilegedelementdefinition_has_name():
    assert hasattr(dbdefinition_PrivilegedElementDefinition, "name")
    descriptor = None
    for klass in dbdefinition_PrivilegedElementDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_debuggerdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_DebuggerDefinition)


def test_dbdefinition_debuggerdefinition_constructor_exists():
    assert callable(dbdefinition_DebuggerDefinition.__init__)


def test_dbdefinition_debuggerdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_DebuggerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "conditionSupported" in params, "Missing parameter 'conditionSupported'"

def test_dbdefinition_debuggerdefinition_has_conditionSupported():
    assert hasattr(dbdefinition_DebuggerDefinition, "conditionSupported")
    descriptor = None
    for klass in dbdefinition_DebuggerDefinition.__mro__:
        if "conditionSupported" in klass.__dict__:
            descriptor = klass.__dict__["conditionSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_viewdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ViewDefinition)


def test_dbdefinition_viewdefinition_constructor_exists():
    assert callable(dbdefinition_ViewDefinition.__init__)


def test_dbdefinition_viewdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ViewDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "checkOptionLevelsSupported" in params, "Missing parameter 'checkOptionLevelsSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "indexSupported" in params, "Missing parameter 'indexSupported'"
    assert "checkOptionSupported" in params, "Missing parameter 'checkOptionSupported'"

def test_dbdefinition_viewdefinition_has_checkOptionLevelsSupported():
    assert hasattr(dbdefinition_ViewDefinition, "checkOptionLevelsSupported")
    descriptor = None
    for klass in dbdefinition_ViewDefinition.__mro__:
        if "checkOptionLevelsSupported" in klass.__dict__:
            descriptor = klass.__dict__["checkOptionLevelsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_viewdefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_ViewDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_ViewDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_viewdefinition_has_indexSupported():
    assert hasattr(dbdefinition_ViewDefinition, "indexSupported")
    descriptor = None
    for klass in dbdefinition_ViewDefinition.__mro__:
        if "indexSupported" in klass.__dict__:
            descriptor = klass.__dict__["indexSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_viewdefinition_has_checkOptionSupported():
    assert hasattr(dbdefinition_ViewDefinition, "checkOptionSupported")
    descriptor = None
    for klass in dbdefinition_ViewDefinition.__mro__:
        if "checkOptionSupported" in klass.__dict__:
            descriptor = klass.__dict__["checkOptionSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_schemadefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_SchemaDefinition)


def test_dbdefinition_schemadefinition_constructor_exists():
    assert callable(dbdefinition_SchemaDefinition.__init__)


def test_dbdefinition_schemadefinition_constructor_args():
    sig = inspect.signature(dbdefinition_SchemaDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"

def test_dbdefinition_schemadefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_SchemaDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_SchemaDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_sequencedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_SequenceDefinition)


def test_dbdefinition_sequencedefinition_constructor_exists():
    assert callable(dbdefinition_SequenceDefinition.__init__)


def test_dbdefinition_sequencedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_SequenceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "cacheDefaultValue" in params, "Missing parameter 'cacheDefaultValue'"
    assert "noMinimumValueString" in params, "Missing parameter 'noMinimumValueString'"
    assert "noMaximumValueString" in params, "Missing parameter 'noMaximumValueString'"
    assert "cacheSupported" in params, "Missing parameter 'cacheSupported'"
    assert "typeEnumerationSupported" in params, "Missing parameter 'typeEnumerationSupported'"
    assert "orderSupported" in params, "Missing parameter 'orderSupported'"
    assert "noCacheString" in params, "Missing parameter 'noCacheString'"

def test_dbdefinition_sequencedefinition_has_cacheDefaultValue():
    assert hasattr(dbdefinition_SequenceDefinition, "cacheDefaultValue")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "cacheDefaultValue" in klass.__dict__:
            descriptor = klass.__dict__["cacheDefaultValue"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sequencedefinition_has_noMinimumValueString():
    assert hasattr(dbdefinition_SequenceDefinition, "noMinimumValueString")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "noMinimumValueString" in klass.__dict__:
            descriptor = klass.__dict__["noMinimumValueString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sequencedefinition_has_noMaximumValueString():
    assert hasattr(dbdefinition_SequenceDefinition, "noMaximumValueString")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "noMaximumValueString" in klass.__dict__:
            descriptor = klass.__dict__["noMaximumValueString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sequencedefinition_has_cacheSupported():
    assert hasattr(dbdefinition_SequenceDefinition, "cacheSupported")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "cacheSupported" in klass.__dict__:
            descriptor = klass.__dict__["cacheSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sequencedefinition_has_typeEnumerationSupported():
    assert hasattr(dbdefinition_SequenceDefinition, "typeEnumerationSupported")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "typeEnumerationSupported" in klass.__dict__:
            descriptor = klass.__dict__["typeEnumerationSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sequencedefinition_has_orderSupported():
    assert hasattr(dbdefinition_SequenceDefinition, "orderSupported")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "orderSupported" in klass.__dict__:
            descriptor = klass.__dict__["orderSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sequencedefinition_has_noCacheString():
    assert hasattr(dbdefinition_SequenceDefinition, "noCacheString")
    descriptor = None
    for klass in dbdefinition_SequenceDefinition.__mro__:
        if "noCacheString" in klass.__dict__:
            descriptor = klass.__dict__["noCacheString"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_TableDefinition)


def test_dbdefinition_tabledefinition_constructor_exists():
    assert callable(dbdefinition_TableDefinition.__init__)


def test_dbdefinition_tabledefinition_constructor_args():
    sig = inspect.signature(dbdefinition_TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "dataCaptureSupported" in params, "Missing parameter 'dataCaptureSupported'"
    assert "encodingSupported" in params, "Missing parameter 'encodingSupported'"
    assert "auditSupported" in params, "Missing parameter 'auditSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "validProcSupported" in params, "Missing parameter 'validProcSupported'"
    assert "editProcSupported" in params, "Missing parameter 'editProcSupported'"

def test_dbdefinition_tabledefinition_has_dataCaptureSupported():
    assert hasattr(dbdefinition_TableDefinition, "dataCaptureSupported")
    descriptor = None
    for klass in dbdefinition_TableDefinition.__mro__:
        if "dataCaptureSupported" in klass.__dict__:
            descriptor = klass.__dict__["dataCaptureSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tabledefinition_has_encodingSupported():
    assert hasattr(dbdefinition_TableDefinition, "encodingSupported")
    descriptor = None
    for klass in dbdefinition_TableDefinition.__mro__:
        if "encodingSupported" in klass.__dict__:
            descriptor = klass.__dict__["encodingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tabledefinition_has_auditSupported():
    assert hasattr(dbdefinition_TableDefinition, "auditSupported")
    descriptor = None
    for klass in dbdefinition_TableDefinition.__mro__:
        if "auditSupported" in klass.__dict__:
            descriptor = klass.__dict__["auditSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tabledefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_TableDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_TableDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tabledefinition_has_validProcSupported():
    assert hasattr(dbdefinition_TableDefinition, "validProcSupported")
    descriptor = None
    for klass in dbdefinition_TableDefinition.__mro__:
        if "validProcSupported" in klass.__dict__:
            descriptor = klass.__dict__["validProcSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tabledefinition_has_editProcSupported():
    assert hasattr(dbdefinition_TableDefinition, "editProcSupported")
    descriptor = None
    for klass in dbdefinition_TableDefinition.__mro__:
        if "editProcSupported" in klass.__dict__:
            descriptor = klass.__dict__["editProcSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_indexdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_IndexDefinition)


def test_dbdefinition_indexdefinition_constructor_exists():
    assert callable(dbdefinition_IndexDefinition.__init__)


def test_dbdefinition_indexdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_IndexDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "percentFreeChangeable" in params, "Missing parameter 'percentFreeChangeable'"
    assert "percentFreeTerminology" in params, "Missing parameter 'percentFreeTerminology'"
    assert "includedColumnsSupported" in params, "Missing parameter 'includedColumnsSupported'"
    assert "clusterChangeable" in params, "Missing parameter 'clusterChangeable'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "clusteringSupported" in params, "Missing parameter 'clusteringSupported'"
    assert "fillFactorSupported" in params, "Missing parameter 'fillFactorSupported'"

def test_dbdefinition_indexdefinition_has_percentFreeChangeable():
    assert hasattr(dbdefinition_IndexDefinition, "percentFreeChangeable")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "percentFreeChangeable" in klass.__dict__:
            descriptor = klass.__dict__["percentFreeChangeable"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_indexdefinition_has_percentFreeTerminology():
    assert hasattr(dbdefinition_IndexDefinition, "percentFreeTerminology")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "percentFreeTerminology" in klass.__dict__:
            descriptor = klass.__dict__["percentFreeTerminology"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_indexdefinition_has_includedColumnsSupported():
    assert hasattr(dbdefinition_IndexDefinition, "includedColumnsSupported")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "includedColumnsSupported" in klass.__dict__:
            descriptor = klass.__dict__["includedColumnsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_indexdefinition_has_clusterChangeable():
    assert hasattr(dbdefinition_IndexDefinition, "clusterChangeable")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "clusterChangeable" in klass.__dict__:
            descriptor = klass.__dict__["clusterChangeable"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_indexdefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_IndexDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_indexdefinition_has_clusteringSupported():
    assert hasattr(dbdefinition_IndexDefinition, "clusteringSupported")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "clusteringSupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteringSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_indexdefinition_has_fillFactorSupported():
    assert hasattr(dbdefinition_IndexDefinition, "fillFactorSupported")
    descriptor = None
    for klass in dbdefinition_IndexDefinition.__mro__:
        if "fillFactorSupported" in klass.__dict__:
            descriptor = klass.__dict__["fillFactorSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_extendeddefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ExtendedDefinition)


def test_dbdefinition_extendeddefinition_constructor_exists():
    assert callable(dbdefinition_ExtendedDefinition.__init__)


def test_dbdefinition_extendeddefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ExtendedDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_dbdefinition_extendeddefinition_has_name():
    assert hasattr(dbdefinition_ExtendedDefinition, "name")
    descriptor = None
    for klass in dbdefinition_ExtendedDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_extendeddefinition_has_value():
    assert hasattr(dbdefinition_ExtendedDefinition, "value")
    descriptor = None
    for klass in dbdefinition_ExtendedDefinition.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ConstraintDefinition)


def test_dbdefinition_constraintdefinition_constructor_exists():
    assert callable(dbdefinition_ConstraintDefinition.__init__)


def test_dbdefinition_constraintdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "parentDeleteDRIRuleType" in params, "Missing parameter 'parentDeleteDRIRuleType'"
    assert "primaryKeyNullable" in params, "Missing parameter 'primaryKeyNullable'"
    assert "parentUpdateDRIRuleType" in params, "Missing parameter 'parentUpdateDRIRuleType'"
    assert "uniqueKeyNullable" in params, "Missing parameter 'uniqueKeyNullable'"
    assert "maximumForeignKeyIdentifierLength" in params, "Missing parameter 'maximumForeignKeyIdentifierLength'"
    assert "clusteredPrimaryKeySupported" in params, "Missing parameter 'clusteredPrimaryKeySupported'"
    assert "informationalConstraintSupported" in params, "Missing parameter 'informationalConstraintSupported'"
    assert "maximumCheckExpressionLength" in params, "Missing parameter 'maximumCheckExpressionLength'"
    assert "clusteredUniqueConstraintSupported" in params, "Missing parameter 'clusteredUniqueConstraintSupported'"
    assert "checkOption" in params, "Missing parameter 'checkOption'"
    assert "maximumPrimaryKeyIdentifierLength" in params, "Missing parameter 'maximumPrimaryKeyIdentifierLength'"
    assert "maximumCheckConstraintIdentifierLength" in params, "Missing parameter 'maximumCheckConstraintIdentifierLength'"
    assert "deferrableConstraintSupported" in params, "Missing parameter 'deferrableConstraintSupported'"

def test_dbdefinition_constraintdefinition_has_parentDeleteDRIRuleType():
    assert hasattr(dbdefinition_ConstraintDefinition, "parentDeleteDRIRuleType")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "parentDeleteDRIRuleType" in klass.__dict__:
            descriptor = klass.__dict__["parentDeleteDRIRuleType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_primaryKeyNullable():
    assert hasattr(dbdefinition_ConstraintDefinition, "primaryKeyNullable")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "primaryKeyNullable" in klass.__dict__:
            descriptor = klass.__dict__["primaryKeyNullable"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_parentUpdateDRIRuleType():
    assert hasattr(dbdefinition_ConstraintDefinition, "parentUpdateDRIRuleType")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "parentUpdateDRIRuleType" in klass.__dict__:
            descriptor = klass.__dict__["parentUpdateDRIRuleType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_uniqueKeyNullable():
    assert hasattr(dbdefinition_ConstraintDefinition, "uniqueKeyNullable")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "uniqueKeyNullable" in klass.__dict__:
            descriptor = klass.__dict__["uniqueKeyNullable"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_maximumForeignKeyIdentifierLength():
    assert hasattr(dbdefinition_ConstraintDefinition, "maximumForeignKeyIdentifierLength")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "maximumForeignKeyIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumForeignKeyIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_clusteredPrimaryKeySupported():
    assert hasattr(dbdefinition_ConstraintDefinition, "clusteredPrimaryKeySupported")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "clusteredPrimaryKeySupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteredPrimaryKeySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_informationalConstraintSupported():
    assert hasattr(dbdefinition_ConstraintDefinition, "informationalConstraintSupported")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "informationalConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["informationalConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_maximumCheckExpressionLength():
    assert hasattr(dbdefinition_ConstraintDefinition, "maximumCheckExpressionLength")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "maximumCheckExpressionLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumCheckExpressionLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_clusteredUniqueConstraintSupported():
    assert hasattr(dbdefinition_ConstraintDefinition, "clusteredUniqueConstraintSupported")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "clusteredUniqueConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteredUniqueConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_checkOption():
    assert hasattr(dbdefinition_ConstraintDefinition, "checkOption")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "checkOption" in klass.__dict__:
            descriptor = klass.__dict__["checkOption"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_maximumPrimaryKeyIdentifierLength():
    assert hasattr(dbdefinition_ConstraintDefinition, "maximumPrimaryKeyIdentifierLength")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "maximumPrimaryKeyIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumPrimaryKeyIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_maximumCheckConstraintIdentifierLength():
    assert hasattr(dbdefinition_ConstraintDefinition, "maximumCheckConstraintIdentifierLength")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "maximumCheckConstraintIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumCheckConstraintIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_constraintdefinition_has_deferrableConstraintSupported():
    assert hasattr(dbdefinition_ConstraintDefinition, "deferrableConstraintSupported")
    descriptor = None
    for klass in dbdefinition_ConstraintDefinition.__mro__:
        if "deferrableConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["deferrableConstraintSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_columndefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_ColumnDefinition)


def test_dbdefinition_columndefinition_constructor_exists():
    assert callable(dbdefinition_ColumnDefinition.__init__)


def test_dbdefinition_columndefinition_constructor_args():
    sig = inspect.signature(dbdefinition_ColumnDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "computedSupported" in params, "Missing parameter 'computedSupported'"
    assert "identityMinimumSupported" in params, "Missing parameter 'identityMinimumSupported'"
    assert "identityIncrementSupported" in params, "Missing parameter 'identityIncrementSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "identityStartValueSupported" in params, "Missing parameter 'identityStartValueSupported'"
    assert "identityCycleSupported" in params, "Missing parameter 'identityCycleSupported'"
    assert "identitySupported" in params, "Missing parameter 'identitySupported'"
    assert "identityMaximumSupported" in params, "Missing parameter 'identityMaximumSupported'"

def test_dbdefinition_columndefinition_has_computedSupported():
    assert hasattr(dbdefinition_ColumnDefinition, "computedSupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "computedSupported" in klass.__dict__:
            descriptor = klass.__dict__["computedSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_identityMinimumSupported():
    assert hasattr(dbdefinition_ColumnDefinition, "identityMinimumSupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "identityMinimumSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityMinimumSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_identityIncrementSupported():
    assert hasattr(dbdefinition_ColumnDefinition, "identityIncrementSupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "identityIncrementSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityIncrementSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_ColumnDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_identityStartValueSupported():
    assert hasattr(dbdefinition_ColumnDefinition, "identityStartValueSupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "identityStartValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityStartValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_identityCycleSupported():
    assert hasattr(dbdefinition_ColumnDefinition, "identityCycleSupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "identityCycleSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityCycleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_identitySupported():
    assert hasattr(dbdefinition_ColumnDefinition, "identitySupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "identitySupported" in klass.__dict__:
            descriptor = klass.__dict__["identitySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_columndefinition_has_identityMaximumSupported():
    assert hasattr(dbdefinition_ColumnDefinition, "identityMaximumSupported")
    descriptor = None
    for klass in dbdefinition_ColumnDefinition.__mro__:
        if "identityMaximumSupported" in klass.__dict__:
            descriptor = klass.__dict__["identityMaximumSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_triggerdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_TriggerDefinition)


def test_dbdefinition_triggerdefinition_constructor_exists():
    assert callable(dbdefinition_TriggerDefinition.__init__)


def test_dbdefinition_triggerdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_TriggerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "insteadOfTriggerSupported" in params, "Missing parameter 'insteadOfTriggerSupported'"
    assert "granularitySupported" in params, "Missing parameter 'granularitySupported'"
    assert "perColumnUpdateTriggerSupported" in params, "Missing parameter 'perColumnUpdateTriggerSupported'"
    assert "maximumActionBodyLength" in params, "Missing parameter 'maximumActionBodyLength'"
    assert "referencesClauseSupported" in params, "Missing parameter 'referencesClauseSupported'"
    assert "tableTriggerReferenceSupported" in params, "Missing parameter 'tableTriggerReferenceSupported'"
    assert "whenClauseSupported" in params, "Missing parameter 'whenClauseSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "rowTriggerReferenceSupported" in params, "Missing parameter 'rowTriggerReferenceSupported'"
    assert "typeSupported" in params, "Missing parameter 'typeSupported'"
    assert "maximumReferencePartLength" in params, "Missing parameter 'maximumReferencePartLength'"

def test_dbdefinition_triggerdefinition_has_insteadOfTriggerSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "insteadOfTriggerSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "insteadOfTriggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["insteadOfTriggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_granularitySupported():
    assert hasattr(dbdefinition_TriggerDefinition, "granularitySupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "granularitySupported" in klass.__dict__:
            descriptor = klass.__dict__["granularitySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_perColumnUpdateTriggerSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "perColumnUpdateTriggerSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "perColumnUpdateTriggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["perColumnUpdateTriggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_maximumActionBodyLength():
    assert hasattr(dbdefinition_TriggerDefinition, "maximumActionBodyLength")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "maximumActionBodyLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumActionBodyLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_referencesClauseSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "referencesClauseSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "referencesClauseSupported" in klass.__dict__:
            descriptor = klass.__dict__["referencesClauseSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_tableTriggerReferenceSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "tableTriggerReferenceSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "tableTriggerReferenceSupported" in klass.__dict__:
            descriptor = klass.__dict__["tableTriggerReferenceSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_whenClauseSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "whenClauseSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "whenClauseSupported" in klass.__dict__:
            descriptor = klass.__dict__["whenClauseSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_TriggerDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_rowTriggerReferenceSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "rowTriggerReferenceSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "rowTriggerReferenceSupported" in klass.__dict__:
            descriptor = klass.__dict__["rowTriggerReferenceSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_typeSupported():
    assert hasattr(dbdefinition_TriggerDefinition, "typeSupported")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "typeSupported" in klass.__dict__:
            descriptor = klass.__dict__["typeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_triggerdefinition_has_maximumReferencePartLength():
    assert hasattr(dbdefinition_TriggerDefinition, "maximumReferencePartLength")
    descriptor = None
    for klass in dbdefinition_TriggerDefinition.__mro__:
        if "maximumReferencePartLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumReferencePartLength"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_storedproceduredefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_StoredProcedureDefinition)


def test_dbdefinition_storedproceduredefinition_constructor_exists():
    assert callable(dbdefinition_StoredProcedureDefinition.__init__)


def test_dbdefinition_storedproceduredefinition_constructor_args():
    sig = inspect.signature(dbdefinition_StoredProcedureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "determininsticSupported" in params, "Missing parameter 'determininsticSupported'"
    assert "parameterStyle" in params, "Missing parameter 'parameterStyle'"
    assert "parameterStyleSupported" in params, "Missing parameter 'parameterStyleSupported'"
    assert "packageGenerationSupported" in params, "Missing parameter 'packageGenerationSupported'"
    assert "maximumActionBodyLength" in params, "Missing parameter 'maximumActionBodyLength'"
    assert "functionLanguageType" in params, "Missing parameter 'functionLanguageType'"
    assert "parameterInitValueSupported" in params, "Missing parameter 'parameterInitValueSupported'"
    assert "nullInputActionSupported" in params, "Missing parameter 'nullInputActionSupported'"
    assert "returnedTypeDeclarationConstraintSupported" in params, "Missing parameter 'returnedTypeDeclarationConstraintSupported'"
    assert "parameterDeclarationConstraintSupported" in params, "Missing parameter 'parameterDeclarationConstraintSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "languageType" in params, "Missing parameter 'languageType'"
    assert "returnedNullSupported" in params, "Missing parameter 'returnedNullSupported'"
    assert "returnTypeSupported" in params, "Missing parameter 'returnTypeSupported'"
    assert "procedureType" in params, "Missing parameter 'procedureType'"

def test_dbdefinition_storedproceduredefinition_has_determininsticSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "determininsticSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "determininsticSupported" in klass.__dict__:
            descriptor = klass.__dict__["determininsticSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_parameterStyle():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "parameterStyle")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "parameterStyle" in klass.__dict__:
            descriptor = klass.__dict__["parameterStyle"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_parameterStyleSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "parameterStyleSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "parameterStyleSupported" in klass.__dict__:
            descriptor = klass.__dict__["parameterStyleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_packageGenerationSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "packageGenerationSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "packageGenerationSupported" in klass.__dict__:
            descriptor = klass.__dict__["packageGenerationSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_maximumActionBodyLength():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "maximumActionBodyLength")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "maximumActionBodyLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumActionBodyLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_functionLanguageType():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "functionLanguageType")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "functionLanguageType" in klass.__dict__:
            descriptor = klass.__dict__["functionLanguageType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_parameterInitValueSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "parameterInitValueSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "parameterInitValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["parameterInitValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_nullInputActionSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "nullInputActionSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "nullInputActionSupported" in klass.__dict__:
            descriptor = klass.__dict__["nullInputActionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_returnedTypeDeclarationConstraintSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "returnedTypeDeclarationConstraintSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "returnedTypeDeclarationConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["returnedTypeDeclarationConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_parameterDeclarationConstraintSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "parameterDeclarationConstraintSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "parameterDeclarationConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["parameterDeclarationConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_languageType():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "languageType")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "languageType" in klass.__dict__:
            descriptor = klass.__dict__["languageType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_returnedNullSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "returnedNullSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "returnedNullSupported" in klass.__dict__:
            descriptor = klass.__dict__["returnedNullSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_returnTypeSupported():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "returnTypeSupported")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "returnTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["returnTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_storedproceduredefinition_has_procedureType():
    assert hasattr(dbdefinition_StoredProcedureDefinition, "procedureType")
    descriptor = None
    for klass in dbdefinition_StoredProcedureDefinition.__mro__:
        if "procedureType" in klass.__dict__:
            descriptor = klass.__dict__["procedureType"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_tablespacedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_TableSpaceDefinition)


def test_dbdefinition_tablespacedefinition_constructor_exists():
    assert callable(dbdefinition_TableSpaceDefinition.__init__)


def test_dbdefinition_tablespacedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_TableSpaceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "prefetchSizeSupported" in params, "Missing parameter 'prefetchSizeSupported'"
    assert "managedBySupported" in params, "Missing parameter 'managedBySupported'"
    assert "containerMaximumSizeSupported" in params, "Missing parameter 'containerMaximumSizeSupported'"
    assert "typeSupported" in params, "Missing parameter 'typeSupported'"
    assert "extentSizeSupported" in params, "Missing parameter 'extentSizeSupported'"
    assert "bufferPoolSupported" in params, "Missing parameter 'bufferPoolSupported'"
    assert "tableSpaceType" in params, "Missing parameter 'tableSpaceType'"
    assert "pageSizeSupported" in params, "Missing parameter 'pageSizeSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "containerExtentSizeSupported" in params, "Missing parameter 'containerExtentSizeSupported'"
    assert "defaultSupported" in params, "Missing parameter 'defaultSupported'"
    assert "containerInitialSizeSupported" in params, "Missing parameter 'containerInitialSizeSupported'"

def test_dbdefinition_tablespacedefinition_has_prefetchSizeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "prefetchSizeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "prefetchSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["prefetchSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_managedBySupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "managedBySupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "managedBySupported" in klass.__dict__:
            descriptor = klass.__dict__["managedBySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_containerMaximumSizeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "containerMaximumSizeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "containerMaximumSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["containerMaximumSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_typeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "typeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "typeSupported" in klass.__dict__:
            descriptor = klass.__dict__["typeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_extentSizeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "extentSizeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "extentSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["extentSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_bufferPoolSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "bufferPoolSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "bufferPoolSupported" in klass.__dict__:
            descriptor = klass.__dict__["bufferPoolSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_tableSpaceType():
    assert hasattr(dbdefinition_TableSpaceDefinition, "tableSpaceType")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "tableSpaceType" in klass.__dict__:
            descriptor = klass.__dict__["tableSpaceType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_pageSizeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "pageSizeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "pageSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["pageSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_TableSpaceDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_containerExtentSizeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "containerExtentSizeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "containerExtentSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["containerExtentSizeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_defaultSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "defaultSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "defaultSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_tablespacedefinition_has_containerInitialSizeSupported():
    assert hasattr(dbdefinition_TableSpaceDefinition, "containerInitialSizeSupported")
    descriptor = None
    for klass in dbdefinition_TableSpaceDefinition.__mro__:
        if "containerInitialSizeSupported" in klass.__dict__:
            descriptor = klass.__dict__["containerInitialSizeSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_nicknamedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_NicknameDefinition)


def test_dbdefinition_nicknamedefinition_constructor_exists():
    assert callable(dbdefinition_NicknameDefinition.__init__)


def test_dbdefinition_nicknamedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_NicknameDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "constraintSupported" in params, "Missing parameter 'constraintSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "indexSupported" in params, "Missing parameter 'indexSupported'"

def test_dbdefinition_nicknamedefinition_has_constraintSupported():
    assert hasattr(dbdefinition_NicknameDefinition, "constraintSupported")
    descriptor = None
    for klass in dbdefinition_NicknameDefinition.__mro__:
        if "constraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["constraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_nicknamedefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_NicknameDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_NicknameDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_nicknamedefinition_has_indexSupported():
    assert hasattr(dbdefinition_NicknameDefinition, "indexSupported")
    descriptor = None
    for klass in dbdefinition_NicknameDefinition.__mro__:
        if "indexSupported" in klass.__dict__:
            descriptor = klass.__dict__["indexSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_sqlsyntaxdefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_SQLSyntaxDefinition)


def test_dbdefinition_sqlsyntaxdefinition_constructor_exists():
    assert callable(dbdefinition_SQLSyntaxDefinition.__init__)


def test_dbdefinition_sqlsyntaxdefinition_constructor_args():
    sig = inspect.signature(dbdefinition_SQLSyntaxDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "operators" in params, "Missing parameter 'operators'"
    assert "terminationCharacter" in params, "Missing parameter 'terminationCharacter'"

def test_dbdefinition_sqlsyntaxdefinition_has_keywords():
    assert hasattr(dbdefinition_SQLSyntaxDefinition, "keywords")
    descriptor = None
    for klass in dbdefinition_SQLSyntaxDefinition.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sqlsyntaxdefinition_has_operators():
    assert hasattr(dbdefinition_SQLSyntaxDefinition, "operators")
    descriptor = None
    for klass in dbdefinition_SQLSyntaxDefinition.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_sqlsyntaxdefinition_has_terminationCharacter():
    assert hasattr(dbdefinition_SQLSyntaxDefinition, "terminationCharacter")
    descriptor = None
    for klass in dbdefinition_SQLSyntaxDefinition.__mro__:
        if "terminationCharacter" in klass.__dict__:
            descriptor = klass.__dict__["terminationCharacter"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_querydefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_QueryDefinition)


def test_dbdefinition_querydefinition_constructor_exists():
    assert callable(dbdefinition_QueryDefinition.__init__)


def test_dbdefinition_querydefinition_constructor_args():
    sig = inspect.signature(dbdefinition_QueryDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "extendedGroupingSupported" in params, "Missing parameter 'extendedGroupingSupported'"
    assert "defaultKeywordForInsertValueSupported" in params, "Missing parameter 'defaultKeywordForInsertValueSupported'"
    assert "hostVariableMarker" in params, "Missing parameter 'hostVariableMarker'"
    assert "tableAliasInDeleteSupported" in params, "Missing parameter 'tableAliasInDeleteSupported'"
    assert "castExpressionSupported" in params, "Missing parameter 'castExpressionSupported'"
    assert "identifierQuoteString" in params, "Missing parameter 'identifierQuoteString'"
    assert "hostVariableMarkerSupported" in params, "Missing parameter 'hostVariableMarkerSupported'"

def test_dbdefinition_querydefinition_has_extendedGroupingSupported():
    assert hasattr(dbdefinition_QueryDefinition, "extendedGroupingSupported")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "extendedGroupingSupported" in klass.__dict__:
            descriptor = klass.__dict__["extendedGroupingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_querydefinition_has_defaultKeywordForInsertValueSupported():
    assert hasattr(dbdefinition_QueryDefinition, "defaultKeywordForInsertValueSupported")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "defaultKeywordForInsertValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultKeywordForInsertValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_querydefinition_has_hostVariableMarker():
    assert hasattr(dbdefinition_QueryDefinition, "hostVariableMarker")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "hostVariableMarker" in klass.__dict__:
            descriptor = klass.__dict__["hostVariableMarker"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_querydefinition_has_tableAliasInDeleteSupported():
    assert hasattr(dbdefinition_QueryDefinition, "tableAliasInDeleteSupported")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "tableAliasInDeleteSupported" in klass.__dict__:
            descriptor = klass.__dict__["tableAliasInDeleteSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_querydefinition_has_castExpressionSupported():
    assert hasattr(dbdefinition_QueryDefinition, "castExpressionSupported")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "castExpressionSupported" in klass.__dict__:
            descriptor = klass.__dict__["castExpressionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_querydefinition_has_identifierQuoteString():
    assert hasattr(dbdefinition_QueryDefinition, "identifierQuoteString")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "identifierQuoteString" in klass.__dict__:
            descriptor = klass.__dict__["identifierQuoteString"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_querydefinition_has_hostVariableMarkerSupported():
    assert hasattr(dbdefinition_QueryDefinition, "hostVariableMarkerSupported")
    descriptor = None
    for klass in dbdefinition_QueryDefinition.__mro__:
        if "hostVariableMarkerSupported" in klass.__dict__:
            descriptor = klass.__dict__["hostVariableMarkerSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_userdefinedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_UserDefinedTypeDefinition)


def test_dbdefinition_userdefinedtypedefinition_constructor_exists():
    assert callable(dbdefinition_UserDefinedTypeDefinition.__init__)


def test_dbdefinition_userdefinedtypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_UserDefinedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueSupported" in params, "Missing parameter 'defaultValueSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "structuredTypeSupported" in params, "Missing parameter 'structuredTypeSupported'"
    assert "distinctTypeSupported" in params, "Missing parameter 'distinctTypeSupported'"

def test_dbdefinition_userdefinedtypedefinition_has_defaultValueSupported():
    assert hasattr(dbdefinition_UserDefinedTypeDefinition, "defaultValueSupported")
    descriptor = None
    for klass in dbdefinition_UserDefinedTypeDefinition.__mro__:
        if "defaultValueSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_userdefinedtypedefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_UserDefinedTypeDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_UserDefinedTypeDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_userdefinedtypedefinition_has_structuredTypeSupported():
    assert hasattr(dbdefinition_UserDefinedTypeDefinition, "structuredTypeSupported")
    descriptor = None
    for klass in dbdefinition_UserDefinedTypeDefinition.__mro__:
        if "structuredTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["structuredTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_userdefinedtypedefinition_has_distinctTypeSupported():
    assert hasattr(dbdefinition_UserDefinedTypeDefinition, "distinctTypeSupported")
    descriptor = None
    for klass in dbdefinition_UserDefinedTypeDefinition.__mro__:
        if "distinctTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["distinctTypeSupported"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_predefineddatatypedefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_PredefinedDataTypeDefinition)


def test_dbdefinition_predefineddatatypedefinition_constructor_exists():
    assert callable(dbdefinition_PredefinedDataTypeDefinition.__init__)


def test_dbdefinition_predefineddatatypedefinition_constructor_args():
    sig = inspect.signature(dbdefinition_PredefinedDataTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueTypes" in params, "Missing parameter 'defaultValueTypes'"
    assert "identitySupported" in params, "Missing parameter 'identitySupported'"
    assert "lengthSemantic" in params, "Missing parameter 'lengthSemantic'"
    assert "minimumScale" in params, "Missing parameter 'minimumScale'"
    assert "languageType" in params, "Missing parameter 'languageType'"
    assert "precisionSupported" in params, "Missing parameter 'precisionSupported'"
    assert "scaleSupported" in params, "Missing parameter 'scaleSupported'"
    assert "largeValueSpecifierLength" in params, "Missing parameter 'largeValueSpecifierLength'"
    assert "jdbcEnumType" in params, "Missing parameter 'jdbcEnumType'"
    assert "characterSetSuffix" in params, "Missing parameter 'characterSetSuffix'"
    assert "defaultPrecision" in params, "Missing parameter 'defaultPrecision'"
    assert "lengthSemanticSupported" in params, "Missing parameter 'lengthSemanticSupported'"
    assert "lengthSupported" in params, "Missing parameter 'lengthSupported'"
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultSupported" in params, "Missing parameter 'defaultSupported'"
    assert "displayNameSupported" in params, "Missing parameter 'displayNameSupported'"
    assert "nullableSupported" in params, "Missing parameter 'nullableSupported'"
    assert "defaultLength" in params, "Missing parameter 'defaultLength'"
    assert "fieldQualifierSeparator" in params, "Missing parameter 'fieldQualifierSeparator'"
    assert "javaClassName" in params, "Missing parameter 'javaClassName'"
    assert "keyConstraintSupported" in params, "Missing parameter 'keyConstraintSupported'"
    assert "trailingFieldQualifierSupported" in params, "Missing parameter 'trailingFieldQualifierSupported'"
    assert "encodingSchemeSuffix" in params, "Missing parameter 'encodingSchemeSuffix'"
    assert "largeValueSpecifierName" in params, "Missing parameter 'largeValueSpecifierName'"
    assert "largeValueSpecifierSupported" in params, "Missing parameter 'largeValueSpecifierSupported'"
    assert "leadingFieldQualifierSupported" in params, "Missing parameter 'leadingFieldQualifierSupported'"
    assert "cutoffPrecision" in params, "Missing parameter 'cutoffPrecision'"
    assert "defaultScale" in params, "Missing parameter 'defaultScale'"
    assert "encodingScheme" in params, "Missing parameter 'encodingScheme'"
    assert "maximumPrecision" in params, "Missing parameter 'maximumPrecision'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "maximumLength" in params, "Missing parameter 'maximumLength'"
    assert "groupingSupported" in params, "Missing parameter 'groupingSupported'"
    assert "clusteringSupported" in params, "Missing parameter 'clusteringSupported'"
    assert "characterSet" in params, "Missing parameter 'characterSet'"
    assert "orderingSupported" in params, "Missing parameter 'orderingSupported'"
    assert "minimumValue" in params, "Missing parameter 'minimumValue'"
    assert "maximumValue" in params, "Missing parameter 'maximumValue'"
    assert "bitDataSupported" in params, "Missing parameter 'bitDataSupported'"
    assert "maximumScale" in params, "Missing parameter 'maximumScale'"
    assert "multipleColumnsSupported" in params, "Missing parameter 'multipleColumnsSupported'"
    assert "fillFactorSupported" in params, "Missing parameter 'fillFactorSupported'"
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "lengthUnit" in params, "Missing parameter 'lengthUnit'"

def test_dbdefinition_predefineddatatypedefinition_has_defaultValueTypes():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "defaultValueTypes")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "defaultValueTypes" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueTypes"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_identitySupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "identitySupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "identitySupported" in klass.__dict__:
            descriptor = klass.__dict__["identitySupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_lengthSemantic():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "lengthSemantic")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "lengthSemantic" in klass.__dict__:
            descriptor = klass.__dict__["lengthSemantic"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_minimumScale():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "minimumScale")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "minimumScale" in klass.__dict__:
            descriptor = klass.__dict__["minimumScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_languageType():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "languageType")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "languageType" in klass.__dict__:
            descriptor = klass.__dict__["languageType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_precisionSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "precisionSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "precisionSupported" in klass.__dict__:
            descriptor = klass.__dict__["precisionSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_scaleSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "scaleSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "scaleSupported" in klass.__dict__:
            descriptor = klass.__dict__["scaleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_largeValueSpecifierLength():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "largeValueSpecifierLength")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "largeValueSpecifierLength" in klass.__dict__:
            descriptor = klass.__dict__["largeValueSpecifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_jdbcEnumType():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "jdbcEnumType")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "jdbcEnumType" in klass.__dict__:
            descriptor = klass.__dict__["jdbcEnumType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_characterSetSuffix():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "characterSetSuffix")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "characterSetSuffix" in klass.__dict__:
            descriptor = klass.__dict__["characterSetSuffix"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_defaultPrecision():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "defaultPrecision")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "defaultPrecision" in klass.__dict__:
            descriptor = klass.__dict__["defaultPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_lengthSemanticSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "lengthSemanticSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "lengthSemanticSupported" in klass.__dict__:
            descriptor = klass.__dict__["lengthSemanticSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_lengthSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "lengthSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "lengthSupported" in klass.__dict__:
            descriptor = klass.__dict__["lengthSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_name():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "name")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_defaultSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "defaultSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "defaultSupported" in klass.__dict__:
            descriptor = klass.__dict__["defaultSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_displayNameSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "displayNameSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "displayNameSupported" in klass.__dict__:
            descriptor = klass.__dict__["displayNameSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_nullableSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "nullableSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "nullableSupported" in klass.__dict__:
            descriptor = klass.__dict__["nullableSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_defaultLength():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "defaultLength")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "defaultLength" in klass.__dict__:
            descriptor = klass.__dict__["defaultLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_fieldQualifierSeparator():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "fieldQualifierSeparator")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "fieldQualifierSeparator" in klass.__dict__:
            descriptor = klass.__dict__["fieldQualifierSeparator"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_javaClassName():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "javaClassName")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "javaClassName" in klass.__dict__:
            descriptor = klass.__dict__["javaClassName"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_keyConstraintSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "keyConstraintSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "keyConstraintSupported" in klass.__dict__:
            descriptor = klass.__dict__["keyConstraintSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_trailingFieldQualifierSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "trailingFieldQualifierSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "trailingFieldQualifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["trailingFieldQualifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_encodingSchemeSuffix():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "encodingSchemeSuffix")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "encodingSchemeSuffix" in klass.__dict__:
            descriptor = klass.__dict__["encodingSchemeSuffix"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_largeValueSpecifierName():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "largeValueSpecifierName")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "largeValueSpecifierName" in klass.__dict__:
            descriptor = klass.__dict__["largeValueSpecifierName"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_largeValueSpecifierSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "largeValueSpecifierSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "largeValueSpecifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["largeValueSpecifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_leadingFieldQualifierSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "leadingFieldQualifierSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "leadingFieldQualifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["leadingFieldQualifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_cutoffPrecision():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "cutoffPrecision")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "cutoffPrecision" in klass.__dict__:
            descriptor = klass.__dict__["cutoffPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_defaultScale():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "defaultScale")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "defaultScale" in klass.__dict__:
            descriptor = klass.__dict__["defaultScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_encodingScheme():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "encodingScheme")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "encodingScheme" in klass.__dict__:
            descriptor = klass.__dict__["encodingScheme"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_maximumPrecision():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "maximumPrecision")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "maximumPrecision" in klass.__dict__:
            descriptor = klass.__dict__["maximumPrecision"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_displayName():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "displayName")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_maximumLength():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "maximumLength")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "maximumLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_groupingSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "groupingSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "groupingSupported" in klass.__dict__:
            descriptor = klass.__dict__["groupingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_clusteringSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "clusteringSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "clusteringSupported" in klass.__dict__:
            descriptor = klass.__dict__["clusteringSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_characterSet():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "characterSet")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "characterSet" in klass.__dict__:
            descriptor = klass.__dict__["characterSet"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_orderingSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "orderingSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "orderingSupported" in klass.__dict__:
            descriptor = klass.__dict__["orderingSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_minimumValue():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "minimumValue")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "minimumValue" in klass.__dict__:
            descriptor = klass.__dict__["minimumValue"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_maximumValue():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "maximumValue")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "maximumValue" in klass.__dict__:
            descriptor = klass.__dict__["maximumValue"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_bitDataSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "bitDataSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "bitDataSupported" in klass.__dict__:
            descriptor = klass.__dict__["bitDataSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_maximumScale():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "maximumScale")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "maximumScale" in klass.__dict__:
            descriptor = klass.__dict__["maximumScale"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_multipleColumnsSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "multipleColumnsSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "multipleColumnsSupported" in klass.__dict__:
            descriptor = klass.__dict__["multipleColumnsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_fillFactorSupported():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "fillFactorSupported")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "fillFactorSupported" in klass.__dict__:
            descriptor = klass.__dict__["fillFactorSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_primitiveType():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "primitiveType")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_predefineddatatypedefinition_has_lengthUnit():
    assert hasattr(dbdefinition_PredefinedDataTypeDefinition, "lengthUnit")
    descriptor = None
    for klass in dbdefinition_PredefinedDataTypeDefinition.__mro__:
        if "lengthUnit" in klass.__dict__:
            descriptor = klass.__dict__["lengthUnit"]
            break
    assert isinstance(descriptor, property)



def test_dbdefinition_databasevendordefinition_is_not_abstract():
    assert not inspect.isabstract(dbdefinition_DatabaseVendorDefinition)


def test_dbdefinition_databasevendordefinition_constructor_exists():
    assert callable(dbdefinition_DatabaseVendorDefinition.__init__)


def test_dbdefinition_databasevendordefinition_constructor_args():
    sig = inspect.signature(dbdefinition_DatabaseVendorDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "quotedDMLSupported" in params, "Missing parameter 'quotedDMLSupported'"
    assert "joinSupported" in params, "Missing parameter 'joinSupported'"
    assert "viewTriggerSupported" in params, "Missing parameter 'viewTriggerSupported'"
    assert "mQTIndexSupported" in params, "Missing parameter 'mQTIndexSupported'"
    assert "quotedDDLSupported" in params, "Missing parameter 'quotedDDLSupported'"
    assert "sqlUDFSupported" in params, "Missing parameter 'sqlUDFSupported'"
    assert "triggerSupported" in params, "Missing parameter 'triggerSupported'"
    assert "constraintsSupported" in params, "Missing parameter 'constraintsSupported'"
    assert "synonymSupported" in params, "Missing parameter 'synonymSupported'"
    assert "packageSupported" in params, "Missing parameter 'packageSupported'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "schemaSupported" in params, "Missing parameter 'schemaSupported'"
    assert "domainSupported" in params, "Missing parameter 'domainSupported'"
    assert "maximumCommentLength" in params, "Missing parameter 'maximumCommentLength'"
    assert "version" in params, "Missing parameter 'version'"
    assert "userDefinedTypeSupported" in params, "Missing parameter 'userDefinedTypeSupported'"
    assert "xmlSupported" in params, "Missing parameter 'xmlSupported'"
    assert "snapshotViewSupported" in params, "Missing parameter 'snapshotViewSupported'"
    assert "groupSupported" in params, "Missing parameter 'groupSupported'"
    assert "mQTSupported" in params, "Missing parameter 'mQTSupported'"
    assert "roleSupported" in params, "Missing parameter 'roleSupported'"
    assert "nicknameSupported" in params, "Missing parameter 'nicknameSupported'"
    assert "userSupported" in params, "Missing parameter 'userSupported'"
    assert "maximumIdentifierLength" in params, "Missing parameter 'maximumIdentifierLength'"
    assert "sequenceSupported" in params, "Missing parameter 'sequenceSupported'"
    assert "authorizationIdentifierSupported" in params, "Missing parameter 'authorizationIdentifierSupported'"
    assert "tablespacesSupported" in params, "Missing parameter 'tablespacesSupported'"
    assert "uDFSupported" in params, "Missing parameter 'uDFSupported'"
    assert "constructedDataTypeSupported" in params, "Missing parameter 'constructedDataTypeSupported'"
    assert "storedProcedureSupported" in params, "Missing parameter 'storedProcedureSupported'"
    assert "roleAuthorizationSupported" in params, "Missing parameter 'roleAuthorizationSupported'"
    assert "SQLStatementSupported" in params, "Missing parameter 'SQLStatementSupported'"
    assert "aliasSupported" in params, "Missing parameter 'aliasSupported'"
    assert "eventSupported" in params, "Missing parameter 'eventSupported'"

def test_dbdefinition_databasevendordefinition_has_quotedDMLSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "quotedDMLSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "quotedDMLSupported" in klass.__dict__:
            descriptor = klass.__dict__["quotedDMLSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_joinSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "joinSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "joinSupported" in klass.__dict__:
            descriptor = klass.__dict__["joinSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_viewTriggerSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "viewTriggerSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "viewTriggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["viewTriggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_mQTIndexSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "mQTIndexSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "mQTIndexSupported" in klass.__dict__:
            descriptor = klass.__dict__["mQTIndexSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_quotedDDLSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "quotedDDLSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "quotedDDLSupported" in klass.__dict__:
            descriptor = klass.__dict__["quotedDDLSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_sqlUDFSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "sqlUDFSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "sqlUDFSupported" in klass.__dict__:
            descriptor = klass.__dict__["sqlUDFSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_triggerSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "triggerSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "triggerSupported" in klass.__dict__:
            descriptor = klass.__dict__["triggerSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_constraintsSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "constraintsSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "constraintsSupported" in klass.__dict__:
            descriptor = klass.__dict__["constraintsSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_synonymSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "synonymSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "synonymSupported" in klass.__dict__:
            descriptor = klass.__dict__["synonymSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_packageSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "packageSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "packageSupported" in klass.__dict__:
            descriptor = klass.__dict__["packageSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_vendor():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "vendor")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_schemaSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "schemaSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "schemaSupported" in klass.__dict__:
            descriptor = klass.__dict__["schemaSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_domainSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "domainSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "domainSupported" in klass.__dict__:
            descriptor = klass.__dict__["domainSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_maximumCommentLength():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "maximumCommentLength")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "maximumCommentLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumCommentLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_version():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "version")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_userDefinedTypeSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "userDefinedTypeSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "userDefinedTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["userDefinedTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_xmlSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "xmlSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "xmlSupported" in klass.__dict__:
            descriptor = klass.__dict__["xmlSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_snapshotViewSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "snapshotViewSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "snapshotViewSupported" in klass.__dict__:
            descriptor = klass.__dict__["snapshotViewSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_groupSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "groupSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "groupSupported" in klass.__dict__:
            descriptor = klass.__dict__["groupSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_mQTSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "mQTSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "mQTSupported" in klass.__dict__:
            descriptor = klass.__dict__["mQTSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_roleSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "roleSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "roleSupported" in klass.__dict__:
            descriptor = klass.__dict__["roleSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_nicknameSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "nicknameSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "nicknameSupported" in klass.__dict__:
            descriptor = klass.__dict__["nicknameSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_userSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "userSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "userSupported" in klass.__dict__:
            descriptor = klass.__dict__["userSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_maximumIdentifierLength():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "maximumIdentifierLength")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "maximumIdentifierLength" in klass.__dict__:
            descriptor = klass.__dict__["maximumIdentifierLength"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_sequenceSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "sequenceSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "sequenceSupported" in klass.__dict__:
            descriptor = klass.__dict__["sequenceSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_authorizationIdentifierSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "authorizationIdentifierSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "authorizationIdentifierSupported" in klass.__dict__:
            descriptor = klass.__dict__["authorizationIdentifierSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_tablespacesSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "tablespacesSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "tablespacesSupported" in klass.__dict__:
            descriptor = klass.__dict__["tablespacesSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_uDFSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "uDFSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "uDFSupported" in klass.__dict__:
            descriptor = klass.__dict__["uDFSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_constructedDataTypeSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "constructedDataTypeSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "constructedDataTypeSupported" in klass.__dict__:
            descriptor = klass.__dict__["constructedDataTypeSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_storedProcedureSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "storedProcedureSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "storedProcedureSupported" in klass.__dict__:
            descriptor = klass.__dict__["storedProcedureSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_roleAuthorizationSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "roleAuthorizationSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "roleAuthorizationSupported" in klass.__dict__:
            descriptor = klass.__dict__["roleAuthorizationSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_SQLStatementSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "SQLStatementSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "SQLStatementSupported" in klass.__dict__:
            descriptor = klass.__dict__["SQLStatementSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_aliasSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "aliasSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "aliasSupported" in klass.__dict__:
            descriptor = klass.__dict__["aliasSupported"]
            break
    assert isinstance(descriptor, property)

def test_dbdefinition_databasevendordefinition_has_eventSupported():
    assert hasattr(dbdefinition_DatabaseVendorDefinition, "eventSupported")
    descriptor = None
    for klass in dbdefinition_DatabaseVendorDefinition.__mro__:
        if "eventSupported" in klass.__dict__:
            descriptor = klass.__dict__["eventSupported"]
            break
    assert isinstance(descriptor, property)

def test_parameterstyle_exists():
    # Check that the Enumeration exists
    assert ParameterStyle is not None

def test_parameterstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterStyle]
    expected_literals = [
        "DB2SQL",
        "JAVA",
        "GENERAL_WITH_NULLS",
        "SQL",
        "GENERAL",
        "DB2DARI",
        "DB2GENRL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterStyle"

def test_proceduretype_exists():
    # Check that the Enumeration exists
    assert ProcedureType is not None

def test_proceduretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureType]
    expected_literals = [
        "FUNCTION",
        "PROCEDURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureType"

def test_languagetype_exists():
    # Check that the Enumeration exists
    assert LanguageType is not None

def test_languagetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LanguageType]
    expected_literals = [
        "COBOLLE",
        "JAVA",
        "ASSEMBLY",
        "OLE",
        "RPGLE",
        "COBOL",
        "RPG",
        "C",
        "CPLUSPLUS",
        "CL",
        "FORTRAN",
        "PLI",
        "REXX",
        "PLSQL",
        "SQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LanguageType"

def test_checkoption_exists():
    # Check that the Enumeration exists
    assert CheckOption is not None

def test_checkoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CheckOption]
    expected_literals = [
        "CASCADE",
        "LOCAL",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CheckOption"

def test_parentdeletedriruletype_exists():
    # Check that the Enumeration exists
    assert ParentDeleteDRIRuleType is not None

def test_parentdeletedriruletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParentDeleteDRIRuleType]
    expected_literals = [
        "NO_ACTION",
        "RESTRICT",
        "SET_DEFAULT",
        "SET_NULL",
        "CASCADE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParentDeleteDRIRuleType"

def test_lengthunit_exists():
    # Check that the Enumeration exists
    assert LengthUnit is not None

def test_lengthunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnit]
    expected_literals = [
        "BIT",
        "DOUBLE_BYTE",
        "BYTE",
        "DECIMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnit"

def test_parentupdatedriruletype_exists():
    # Check that the Enumeration exists
    assert ParentUpdateDRIRuleType is not None

def test_parentupdatedriruletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParentUpdateDRIRuleType]
    expected_literals = [
        "SET_DEFAULT",
        "CASCADE",
        "SET_NULL",
        "NO_ACTION",
        "RESTRICT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParentUpdateDRIRuleType"

def test_tablespacetype_exists():
    # Check that the Enumeration exists
    assert TableSpaceType is not None

def test_tablespacetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TableSpaceType]
    expected_literals = [
        "LARGE",
        "SYSTEM_TEMPORARY",
        "REGULAR",
        "USER_TEMPORARY",
        "TEMPORARY",
        "PERMANENT",
        "LONG",
        "LOB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TableSpaceType"

def test_percentfreeterminology_exists():
    # Check that the Enumeration exists
    assert PercentFreeTerminology is not None

def test_percentfreeterminology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PercentFreeTerminology]
    expected_literals = [
        "PERCENT_FREE",
        "THRESHOLD",
        "FILL_FACTOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PercentFreeTerminology"


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
dbdefinition_PrivilegeDefinition_strategy = st.builds(
    dbdefinition_PrivilegeDefinition,
    name=
        safe_text
)
dbdefinition_FieldQualifierDefinition_strategy = st.builds(
    dbdefinition_FieldQualifierDefinition,
    maximumScale=
        st.integers(),
    name=
        safe_text,
    scaleSupported=
        st.booleans(),
    defaultPrecision=
        st.integers(),
    maximumPrecision=
        st.integers(),
    precisionSupported=
        st.booleans(),
    defaultScale=
        st.integers()
)
dbdefinition_ConstructedDataTypeDefinition_strategy = st.builds(
    dbdefinition_ConstructedDataTypeDefinition,
    referenceDatatypeSupported=
        st.booleans(),
    rowDatatypeSupported=
        st.booleans(),
    cursorDatatypeSupported=
        st.booleans(),
    arrayDatatypeSupported=
        st.booleans(),
    multisetDatatypeSupported=
        st.booleans()
)
dbdefinition_PrivilegedElementDefinition_strategy = st.builds(
    dbdefinition_PrivilegedElementDefinition,
    name=
        safe_text
)
dbdefinition_DebuggerDefinition_strategy = st.builds(
    dbdefinition_DebuggerDefinition,
    conditionSupported=
        st.booleans()
)
dbdefinition_ViewDefinition_strategy = st.builds(
    dbdefinition_ViewDefinition,
    checkOptionLevelsSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    indexSupported=
        st.booleans(),
    checkOptionSupported=
        st.booleans()
)
dbdefinition_SchemaDefinition_strategy = st.builds(
    dbdefinition_SchemaDefinition,
    maximumIdentifierLength=
        st.integers()
)
dbdefinition_SequenceDefinition_strategy = st.builds(
    dbdefinition_SequenceDefinition,
    cacheDefaultValue=
        st.integers(),
    noMinimumValueString=
        safe_text,
    noMaximumValueString=
        safe_text,
    cacheSupported=
        st.booleans(),
    typeEnumerationSupported=
        st.booleans(),
    orderSupported=
        st.booleans(),
    noCacheString=
        safe_text
)
dbdefinition_TableDefinition_strategy = st.builds(
    dbdefinition_TableDefinition,
    dataCaptureSupported=
        st.booleans(),
    encodingSupported=
        st.booleans(),
    auditSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    validProcSupported=
        st.booleans(),
    editProcSupported=
        st.booleans()
)
dbdefinition_IndexDefinition_strategy = st.builds(
    dbdefinition_IndexDefinition,
    percentFreeChangeable=
        st.booleans(),
    percentFreeTerminology=
        safe_text,
    includedColumnsSupported=
        st.booleans(),
    clusterChangeable=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    clusteringSupported=
        st.booleans(),
    fillFactorSupported=
        st.booleans()
)
dbdefinition_ExtendedDefinition_strategy = st.builds(
    dbdefinition_ExtendedDefinition,
    name=
        safe_text,
    value=
        safe_text
)
dbdefinition_ConstraintDefinition_strategy = st.builds(
    dbdefinition_ConstraintDefinition,
    parentDeleteDRIRuleType=
        safe_text,
    primaryKeyNullable=
        st.booleans(),
    parentUpdateDRIRuleType=
        safe_text,
    uniqueKeyNullable=
        st.booleans(),
    maximumForeignKeyIdentifierLength=
        st.integers(),
    clusteredPrimaryKeySupported=
        st.booleans(),
    informationalConstraintSupported=
        st.booleans(),
    maximumCheckExpressionLength=
        st.integers(),
    clusteredUniqueConstraintSupported=
        st.booleans(),
    checkOption=
        safe_text,
    maximumPrimaryKeyIdentifierLength=
        st.integers(),
    maximumCheckConstraintIdentifierLength=
        st.integers(),
    deferrableConstraintSupported=
        st.booleans()
)
dbdefinition_ColumnDefinition_strategy = st.builds(
    dbdefinition_ColumnDefinition,
    computedSupported=
        st.booleans(),
    identityMinimumSupported=
        st.booleans(),
    identityIncrementSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    identityStartValueSupported=
        st.booleans(),
    identityCycleSupported=
        st.booleans(),
    identitySupported=
        st.booleans(),
    identityMaximumSupported=
        st.booleans()
)
dbdefinition_TriggerDefinition_strategy = st.builds(
    dbdefinition_TriggerDefinition,
    insteadOfTriggerSupported=
        st.booleans(),
    granularitySupported=
        st.booleans(),
    perColumnUpdateTriggerSupported=
        st.booleans(),
    maximumActionBodyLength=
        st.integers(),
    referencesClauseSupported=
        st.booleans(),
    tableTriggerReferenceSupported=
        st.booleans(),
    whenClauseSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    rowTriggerReferenceSupported=
        st.booleans(),
    typeSupported=
        st.booleans(),
    maximumReferencePartLength=
        st.integers()
)
dbdefinition_StoredProcedureDefinition_strategy = st.builds(
    dbdefinition_StoredProcedureDefinition,
    determininsticSupported=
        st.booleans(),
    parameterStyle=
        safe_text,
    parameterStyleSupported=
        st.booleans(),
    packageGenerationSupported=
        st.booleans(),
    maximumActionBodyLength=
        st.integers(),
    functionLanguageType=
        safe_text,
    parameterInitValueSupported=
        st.booleans(),
    nullInputActionSupported=
        st.booleans(),
    returnedTypeDeclarationConstraintSupported=
        st.booleans(),
    parameterDeclarationConstraintSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    languageType=
        safe_text,
    returnedNullSupported=
        st.booleans(),
    returnTypeSupported=
        st.booleans(),
    procedureType=
        safe_text
)
dbdefinition_TableSpaceDefinition_strategy = st.builds(
    dbdefinition_TableSpaceDefinition,
    prefetchSizeSupported=
        st.booleans(),
    managedBySupported=
        st.booleans(),
    containerMaximumSizeSupported=
        st.booleans(),
    typeSupported=
        st.booleans(),
    extentSizeSupported=
        st.booleans(),
    bufferPoolSupported=
        st.booleans(),
    tableSpaceType=
        safe_text,
    pageSizeSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    containerExtentSizeSupported=
        st.booleans(),
    defaultSupported=
        st.booleans(),
    containerInitialSizeSupported=
        st.booleans()
)
dbdefinition_NicknameDefinition_strategy = st.builds(
    dbdefinition_NicknameDefinition,
    constraintSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    indexSupported=
        st.booleans()
)
dbdefinition_SQLSyntaxDefinition_strategy = st.builds(
    dbdefinition_SQLSyntaxDefinition,
    keywords=
        safe_text,
    operators=
        safe_text,
    terminationCharacter=
        safe_text
)
dbdefinition_QueryDefinition_strategy = st.builds(
    dbdefinition_QueryDefinition,
    extendedGroupingSupported=
        st.booleans(),
    defaultKeywordForInsertValueSupported=
        st.booleans(),
    hostVariableMarker=
        safe_text,
    tableAliasInDeleteSupported=
        st.booleans(),
    castExpressionSupported=
        st.booleans(),
    identifierQuoteString=
        safe_text,
    hostVariableMarkerSupported=
        st.booleans()
)
dbdefinition_UserDefinedTypeDefinition_strategy = st.builds(
    dbdefinition_UserDefinedTypeDefinition,
    defaultValueSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    structuredTypeSupported=
        st.booleans(),
    distinctTypeSupported=
        st.booleans()
)
dbdefinition_PredefinedDataTypeDefinition_strategy = st.builds(
    dbdefinition_PredefinedDataTypeDefinition,
    defaultValueTypes=
        safe_text,
    identitySupported=
        st.booleans(),
    lengthSemantic=
        safe_text,
    minimumScale=
        st.integers(),
    languageType=
        safe_text,
    precisionSupported=
        st.booleans(),
    scaleSupported=
        st.booleans(),
    largeValueSpecifierLength=
        st.integers(),
    jdbcEnumType=
        st.integers(),
    characterSetSuffix=
        safe_text,
    defaultPrecision=
        st.integers(),
    lengthSemanticSupported=
        st.booleans(),
    lengthSupported=
        st.booleans(),
    name=
        safe_text,
    defaultSupported=
        st.booleans(),
    displayNameSupported=
        st.booleans(),
    nullableSupported=
        st.booleans(),
    defaultLength=
        st.integers(),
    fieldQualifierSeparator=
        safe_text,
    javaClassName=
        safe_text,
    keyConstraintSupported=
        st.booleans(),
    trailingFieldQualifierSupported=
        st.booleans(),
    encodingSchemeSuffix=
        safe_text,
    largeValueSpecifierName=
        safe_text,
    largeValueSpecifierSupported=
        st.booleans(),
    leadingFieldQualifierSupported=
        st.booleans(),
    cutoffPrecision=
        st.integers(),
    defaultScale=
        st.integers(),
    encodingScheme=
        safe_text,
    maximumPrecision=
        st.integers(),
    displayName=
        safe_text,
    maximumLength=
        st.integers(),
    groupingSupported=
        st.booleans(),
    clusteringSupported=
        st.booleans(),
    characterSet=
        safe_text,
    orderingSupported=
        st.booleans(),
    minimumValue=
        safe_text,
    maximumValue=
        safe_text,
    bitDataSupported=
        st.booleans(),
    maximumScale=
        st.integers(),
    multipleColumnsSupported=
        st.booleans(),
    fillFactorSupported=
        st.booleans(),
    primitiveType=
        safe_text,
    lengthUnit=
        safe_text
)
dbdefinition_DatabaseVendorDefinition_strategy = st.builds(
    dbdefinition_DatabaseVendorDefinition,
    quotedDMLSupported=
        st.booleans(),
    joinSupported=
        st.booleans(),
    viewTriggerSupported=
        st.booleans(),
    mQTIndexSupported=
        st.booleans(),
    quotedDDLSupported=
        st.booleans(),
    sqlUDFSupported=
        st.booleans(),
    triggerSupported=
        st.booleans(),
    constraintsSupported=
        st.booleans(),
    synonymSupported=
        st.booleans(),
    packageSupported=
        st.booleans(),
    vendor=
        safe_text,
    schemaSupported=
        st.booleans(),
    domainSupported=
        st.booleans(),
    maximumCommentLength=
        st.integers(),
    version=
        safe_text,
    userDefinedTypeSupported=
        st.booleans(),
    xmlSupported=
        st.booleans(),
    snapshotViewSupported=
        st.booleans(),
    groupSupported=
        st.booleans(),
    mQTSupported=
        st.booleans(),
    roleSupported=
        st.booleans(),
    nicknameSupported=
        st.booleans(),
    userSupported=
        st.booleans(),
    maximumIdentifierLength=
        st.integers(),
    sequenceSupported=
        st.booleans(),
    authorizationIdentifierSupported=
        st.booleans(),
    tablespacesSupported=
        st.booleans(),
    uDFSupported=
        st.booleans(),
    constructedDataTypeSupported=
        st.booleans(),
    storedProcedureSupported=
        st.booleans(),
    roleAuthorizationSupported=
        st.booleans(),
    SQLStatementSupported=
        st.booleans(),
    aliasSupported=
        st.booleans(),
    eventSupported=
        st.booleans()
)

@given(instance=dbdefinition_PrivilegeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_privilegedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_PrivilegeDefinition)



@given(instance=dbdefinition_PrivilegeDefinition_strategy)
def test_dbdefinition_privilegedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_fieldqualifierdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_FieldQualifierDefinition)



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_maximumScale_setter(instance):
    original = instance.maximumScale
    instance.maximumScale = original
    assert instance.maximumScale == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_scaleSupported_setter(instance):
    original = instance.scaleSupported
    instance.scaleSupported = original
    assert instance.scaleSupported == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_defaultPrecision_setter(instance):
    original = instance.defaultPrecision
    instance.defaultPrecision = original
    assert instance.defaultPrecision == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_maximumPrecision_setter(instance):
    original = instance.maximumPrecision
    instance.maximumPrecision = original
    assert instance.maximumPrecision == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_precisionSupported_setter(instance):
    original = instance.precisionSupported
    instance.precisionSupported = original
    assert instance.precisionSupported == original



@given(instance=dbdefinition_FieldQualifierDefinition_strategy)
def test_dbdefinition_fieldqualifierdefinition_defaultScale_setter(instance):
    original = instance.defaultScale
    instance.defaultScale = original
    assert instance.defaultScale == original

@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_constructeddatatypedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ConstructedDataTypeDefinition)



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_dbdefinition_constructeddatatypedefinition_referenceDatatypeSupported_setter(instance):
    original = instance.referenceDatatypeSupported
    instance.referenceDatatypeSupported = original
    assert instance.referenceDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_dbdefinition_constructeddatatypedefinition_rowDatatypeSupported_setter(instance):
    original = instance.rowDatatypeSupported
    instance.rowDatatypeSupported = original
    assert instance.rowDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_dbdefinition_constructeddatatypedefinition_cursorDatatypeSupported_setter(instance):
    original = instance.cursorDatatypeSupported
    instance.cursorDatatypeSupported = original
    assert instance.cursorDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_dbdefinition_constructeddatatypedefinition_arrayDatatypeSupported_setter(instance):
    original = instance.arrayDatatypeSupported
    instance.arrayDatatypeSupported = original
    assert instance.arrayDatatypeSupported == original



@given(instance=dbdefinition_ConstructedDataTypeDefinition_strategy)
def test_dbdefinition_constructeddatatypedefinition_multisetDatatypeSupported_setter(instance):
    original = instance.multisetDatatypeSupported
    instance.multisetDatatypeSupported = original
    assert instance.multisetDatatypeSupported == original

@given(instance=dbdefinition_PrivilegedElementDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_privilegedelementdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_PrivilegedElementDefinition)



@given(instance=dbdefinition_PrivilegedElementDefinition_strategy)
def test_dbdefinition_privilegedelementdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbdefinition_DebuggerDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_debuggerdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_DebuggerDefinition)



@given(instance=dbdefinition_DebuggerDefinition_strategy)
def test_dbdefinition_debuggerdefinition_conditionSupported_setter(instance):
    original = instance.conditionSupported
    instance.conditionSupported = original
    assert instance.conditionSupported == original

@given(instance=dbdefinition_ViewDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_viewdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ViewDefinition)



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_dbdefinition_viewdefinition_checkOptionLevelsSupported_setter(instance):
    original = instance.checkOptionLevelsSupported
    instance.checkOptionLevelsSupported = original
    assert instance.checkOptionLevelsSupported == original



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_dbdefinition_viewdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_dbdefinition_viewdefinition_indexSupported_setter(instance):
    original = instance.indexSupported
    instance.indexSupported = original
    assert instance.indexSupported == original



@given(instance=dbdefinition_ViewDefinition_strategy)
def test_dbdefinition_viewdefinition_checkOptionSupported_setter(instance):
    original = instance.checkOptionSupported
    instance.checkOptionSupported = original
    assert instance.checkOptionSupported == original

@given(instance=dbdefinition_SchemaDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_schemadefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_SchemaDefinition)



@given(instance=dbdefinition_SchemaDefinition_strategy)
def test_dbdefinition_schemadefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original

@given(instance=dbdefinition_SequenceDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_sequencedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_SequenceDefinition)



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_cacheDefaultValue_setter(instance):
    original = instance.cacheDefaultValue
    instance.cacheDefaultValue = original
    assert instance.cacheDefaultValue == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_noMinimumValueString_setter(instance):
    original = instance.noMinimumValueString
    instance.noMinimumValueString = original
    assert instance.noMinimumValueString == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_noMaximumValueString_setter(instance):
    original = instance.noMaximumValueString
    instance.noMaximumValueString = original
    assert instance.noMaximumValueString == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_cacheSupported_setter(instance):
    original = instance.cacheSupported
    instance.cacheSupported = original
    assert instance.cacheSupported == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_typeEnumerationSupported_setter(instance):
    original = instance.typeEnumerationSupported
    instance.typeEnumerationSupported = original
    assert instance.typeEnumerationSupported == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_orderSupported_setter(instance):
    original = instance.orderSupported
    instance.orderSupported = original
    assert instance.orderSupported == original



@given(instance=dbdefinition_SequenceDefinition_strategy)
def test_dbdefinition_sequencedefinition_noCacheString_setter(instance):
    original = instance.noCacheString
    instance.noCacheString = original
    assert instance.noCacheString == original

@given(instance=dbdefinition_TableDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_tabledefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_TableDefinition)



@given(instance=dbdefinition_TableDefinition_strategy)
def test_dbdefinition_tabledefinition_dataCaptureSupported_setter(instance):
    original = instance.dataCaptureSupported
    instance.dataCaptureSupported = original
    assert instance.dataCaptureSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_dbdefinition_tabledefinition_encodingSupported_setter(instance):
    original = instance.encodingSupported
    instance.encodingSupported = original
    assert instance.encodingSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_dbdefinition_tabledefinition_auditSupported_setter(instance):
    original = instance.auditSupported
    instance.auditSupported = original
    assert instance.auditSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_dbdefinition_tabledefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_dbdefinition_tabledefinition_validProcSupported_setter(instance):
    original = instance.validProcSupported
    instance.validProcSupported = original
    assert instance.validProcSupported == original



@given(instance=dbdefinition_TableDefinition_strategy)
def test_dbdefinition_tabledefinition_editProcSupported_setter(instance):
    original = instance.editProcSupported
    instance.editProcSupported = original
    assert instance.editProcSupported == original

@given(instance=dbdefinition_IndexDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_indexdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_IndexDefinition)



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_percentFreeChangeable_setter(instance):
    original = instance.percentFreeChangeable
    instance.percentFreeChangeable = original
    assert instance.percentFreeChangeable == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_percentFreeTerminology_setter(instance):
    original = instance.percentFreeTerminology
    instance.percentFreeTerminology = original
    assert instance.percentFreeTerminology == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_includedColumnsSupported_setter(instance):
    original = instance.includedColumnsSupported
    instance.includedColumnsSupported = original
    assert instance.includedColumnsSupported == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_clusterChangeable_setter(instance):
    original = instance.clusterChangeable
    instance.clusterChangeable = original
    assert instance.clusterChangeable == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_clusteringSupported_setter(instance):
    original = instance.clusteringSupported
    instance.clusteringSupported = original
    assert instance.clusteringSupported == original



@given(instance=dbdefinition_IndexDefinition_strategy)
def test_dbdefinition_indexdefinition_fillFactorSupported_setter(instance):
    original = instance.fillFactorSupported
    instance.fillFactorSupported = original
    assert instance.fillFactorSupported == original

@given(instance=dbdefinition_ExtendedDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_extendeddefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ExtendedDefinition)



@given(instance=dbdefinition_ExtendedDefinition_strategy)
def test_dbdefinition_extendeddefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbdefinition_ExtendedDefinition_strategy)
def test_dbdefinition_extendeddefinition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbdefinition_ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_constraintdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ConstraintDefinition)



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_parentDeleteDRIRuleType_setter(instance):
    original = instance.parentDeleteDRIRuleType
    instance.parentDeleteDRIRuleType = original
    assert instance.parentDeleteDRIRuleType == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_primaryKeyNullable_setter(instance):
    original = instance.primaryKeyNullable
    instance.primaryKeyNullable = original
    assert instance.primaryKeyNullable == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_parentUpdateDRIRuleType_setter(instance):
    original = instance.parentUpdateDRIRuleType
    instance.parentUpdateDRIRuleType = original
    assert instance.parentUpdateDRIRuleType == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_uniqueKeyNullable_setter(instance):
    original = instance.uniqueKeyNullable
    instance.uniqueKeyNullable = original
    assert instance.uniqueKeyNullable == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_maximumForeignKeyIdentifierLength_setter(instance):
    original = instance.maximumForeignKeyIdentifierLength
    instance.maximumForeignKeyIdentifierLength = original
    assert instance.maximumForeignKeyIdentifierLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_clusteredPrimaryKeySupported_setter(instance):
    original = instance.clusteredPrimaryKeySupported
    instance.clusteredPrimaryKeySupported = original
    assert instance.clusteredPrimaryKeySupported == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_informationalConstraintSupported_setter(instance):
    original = instance.informationalConstraintSupported
    instance.informationalConstraintSupported = original
    assert instance.informationalConstraintSupported == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_maximumCheckExpressionLength_setter(instance):
    original = instance.maximumCheckExpressionLength
    instance.maximumCheckExpressionLength = original
    assert instance.maximumCheckExpressionLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_clusteredUniqueConstraintSupported_setter(instance):
    original = instance.clusteredUniqueConstraintSupported
    instance.clusteredUniqueConstraintSupported = original
    assert instance.clusteredUniqueConstraintSupported == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_checkOption_setter(instance):
    original = instance.checkOption
    instance.checkOption = original
    assert instance.checkOption == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_maximumPrimaryKeyIdentifierLength_setter(instance):
    original = instance.maximumPrimaryKeyIdentifierLength
    instance.maximumPrimaryKeyIdentifierLength = original
    assert instance.maximumPrimaryKeyIdentifierLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_maximumCheckConstraintIdentifierLength_setter(instance):
    original = instance.maximumCheckConstraintIdentifierLength
    instance.maximumCheckConstraintIdentifierLength = original
    assert instance.maximumCheckConstraintIdentifierLength == original



@given(instance=dbdefinition_ConstraintDefinition_strategy)
def test_dbdefinition_constraintdefinition_deferrableConstraintSupported_setter(instance):
    original = instance.deferrableConstraintSupported
    instance.deferrableConstraintSupported = original
    assert instance.deferrableConstraintSupported == original

@given(instance=dbdefinition_ColumnDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_columndefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_ColumnDefinition)



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_computedSupported_setter(instance):
    original = instance.computedSupported
    instance.computedSupported = original
    assert instance.computedSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_identityMinimumSupported_setter(instance):
    original = instance.identityMinimumSupported
    instance.identityMinimumSupported = original
    assert instance.identityMinimumSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_identityIncrementSupported_setter(instance):
    original = instance.identityIncrementSupported
    instance.identityIncrementSupported = original
    assert instance.identityIncrementSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_identityStartValueSupported_setter(instance):
    original = instance.identityStartValueSupported
    instance.identityStartValueSupported = original
    assert instance.identityStartValueSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_identityCycleSupported_setter(instance):
    original = instance.identityCycleSupported
    instance.identityCycleSupported = original
    assert instance.identityCycleSupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_identitySupported_setter(instance):
    original = instance.identitySupported
    instance.identitySupported = original
    assert instance.identitySupported == original



@given(instance=dbdefinition_ColumnDefinition_strategy)
def test_dbdefinition_columndefinition_identityMaximumSupported_setter(instance):
    original = instance.identityMaximumSupported
    instance.identityMaximumSupported = original
    assert instance.identityMaximumSupported == original

@given(instance=dbdefinition_TriggerDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_triggerdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_TriggerDefinition)



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_insteadOfTriggerSupported_setter(instance):
    original = instance.insteadOfTriggerSupported
    instance.insteadOfTriggerSupported = original
    assert instance.insteadOfTriggerSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_granularitySupported_setter(instance):
    original = instance.granularitySupported
    instance.granularitySupported = original
    assert instance.granularitySupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_perColumnUpdateTriggerSupported_setter(instance):
    original = instance.perColumnUpdateTriggerSupported
    instance.perColumnUpdateTriggerSupported = original
    assert instance.perColumnUpdateTriggerSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_maximumActionBodyLength_setter(instance):
    original = instance.maximumActionBodyLength
    instance.maximumActionBodyLength = original
    assert instance.maximumActionBodyLength == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_referencesClauseSupported_setter(instance):
    original = instance.referencesClauseSupported
    instance.referencesClauseSupported = original
    assert instance.referencesClauseSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_tableTriggerReferenceSupported_setter(instance):
    original = instance.tableTriggerReferenceSupported
    instance.tableTriggerReferenceSupported = original
    assert instance.tableTriggerReferenceSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_whenClauseSupported_setter(instance):
    original = instance.whenClauseSupported
    instance.whenClauseSupported = original
    assert instance.whenClauseSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_rowTriggerReferenceSupported_setter(instance):
    original = instance.rowTriggerReferenceSupported
    instance.rowTriggerReferenceSupported = original
    assert instance.rowTriggerReferenceSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_typeSupported_setter(instance):
    original = instance.typeSupported
    instance.typeSupported = original
    assert instance.typeSupported == original



@given(instance=dbdefinition_TriggerDefinition_strategy)
def test_dbdefinition_triggerdefinition_maximumReferencePartLength_setter(instance):
    original = instance.maximumReferencePartLength
    instance.maximumReferencePartLength = original
    assert instance.maximumReferencePartLength == original

@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_storedproceduredefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_StoredProcedureDefinition)



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_determininsticSupported_setter(instance):
    original = instance.determininsticSupported
    instance.determininsticSupported = original
    assert instance.determininsticSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_parameterStyle_setter(instance):
    original = instance.parameterStyle
    instance.parameterStyle = original
    assert instance.parameterStyle == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_parameterStyleSupported_setter(instance):
    original = instance.parameterStyleSupported
    instance.parameterStyleSupported = original
    assert instance.parameterStyleSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_packageGenerationSupported_setter(instance):
    original = instance.packageGenerationSupported
    instance.packageGenerationSupported = original
    assert instance.packageGenerationSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_maximumActionBodyLength_setter(instance):
    original = instance.maximumActionBodyLength
    instance.maximumActionBodyLength = original
    assert instance.maximumActionBodyLength == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_functionLanguageType_setter(instance):
    original = instance.functionLanguageType
    instance.functionLanguageType = original
    assert instance.functionLanguageType == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_parameterInitValueSupported_setter(instance):
    original = instance.parameterInitValueSupported
    instance.parameterInitValueSupported = original
    assert instance.parameterInitValueSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_nullInputActionSupported_setter(instance):
    original = instance.nullInputActionSupported
    instance.nullInputActionSupported = original
    assert instance.nullInputActionSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_returnedTypeDeclarationConstraintSupported_setter(instance):
    original = instance.returnedTypeDeclarationConstraintSupported
    instance.returnedTypeDeclarationConstraintSupported = original
    assert instance.returnedTypeDeclarationConstraintSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_parameterDeclarationConstraintSupported_setter(instance):
    original = instance.parameterDeclarationConstraintSupported
    instance.parameterDeclarationConstraintSupported = original
    assert instance.parameterDeclarationConstraintSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_languageType_setter(instance):
    original = instance.languageType
    instance.languageType = original
    assert instance.languageType == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_returnedNullSupported_setter(instance):
    original = instance.returnedNullSupported
    instance.returnedNullSupported = original
    assert instance.returnedNullSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_returnTypeSupported_setter(instance):
    original = instance.returnTypeSupported
    instance.returnTypeSupported = original
    assert instance.returnTypeSupported == original



@given(instance=dbdefinition_StoredProcedureDefinition_strategy)
def test_dbdefinition_storedproceduredefinition_procedureType_setter(instance):
    original = instance.procedureType
    instance.procedureType = original
    assert instance.procedureType == original

@given(instance=dbdefinition_TableSpaceDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_tablespacedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_TableSpaceDefinition)



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_prefetchSizeSupported_setter(instance):
    original = instance.prefetchSizeSupported
    instance.prefetchSizeSupported = original
    assert instance.prefetchSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_managedBySupported_setter(instance):
    original = instance.managedBySupported
    instance.managedBySupported = original
    assert instance.managedBySupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_containerMaximumSizeSupported_setter(instance):
    original = instance.containerMaximumSizeSupported
    instance.containerMaximumSizeSupported = original
    assert instance.containerMaximumSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_typeSupported_setter(instance):
    original = instance.typeSupported
    instance.typeSupported = original
    assert instance.typeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_extentSizeSupported_setter(instance):
    original = instance.extentSizeSupported
    instance.extentSizeSupported = original
    assert instance.extentSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_bufferPoolSupported_setter(instance):
    original = instance.bufferPoolSupported
    instance.bufferPoolSupported = original
    assert instance.bufferPoolSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_tableSpaceType_setter(instance):
    original = instance.tableSpaceType
    instance.tableSpaceType = original
    assert instance.tableSpaceType == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_pageSizeSupported_setter(instance):
    original = instance.pageSizeSupported
    instance.pageSizeSupported = original
    assert instance.pageSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_containerExtentSizeSupported_setter(instance):
    original = instance.containerExtentSizeSupported
    instance.containerExtentSizeSupported = original
    assert instance.containerExtentSizeSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_defaultSupported_setter(instance):
    original = instance.defaultSupported
    instance.defaultSupported = original
    assert instance.defaultSupported == original



@given(instance=dbdefinition_TableSpaceDefinition_strategy)
def test_dbdefinition_tablespacedefinition_containerInitialSizeSupported_setter(instance):
    original = instance.containerInitialSizeSupported
    instance.containerInitialSizeSupported = original
    assert instance.containerInitialSizeSupported == original

@given(instance=dbdefinition_NicknameDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_nicknamedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_NicknameDefinition)



@given(instance=dbdefinition_NicknameDefinition_strategy)
def test_dbdefinition_nicknamedefinition_constraintSupported_setter(instance):
    original = instance.constraintSupported
    instance.constraintSupported = original
    assert instance.constraintSupported == original



@given(instance=dbdefinition_NicknameDefinition_strategy)
def test_dbdefinition_nicknamedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_NicknameDefinition_strategy)
def test_dbdefinition_nicknamedefinition_indexSupported_setter(instance):
    original = instance.indexSupported
    instance.indexSupported = original
    assert instance.indexSupported == original

@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_sqlsyntaxdefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_SQLSyntaxDefinition)



@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
def test_dbdefinition_sqlsyntaxdefinition_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
def test_dbdefinition_sqlsyntaxdefinition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original



@given(instance=dbdefinition_SQLSyntaxDefinition_strategy)
def test_dbdefinition_sqlsyntaxdefinition_terminationCharacter_setter(instance):
    original = instance.terminationCharacter
    instance.terminationCharacter = original
    assert instance.terminationCharacter == original

@given(instance=dbdefinition_QueryDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_querydefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_QueryDefinition)



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_extendedGroupingSupported_setter(instance):
    original = instance.extendedGroupingSupported
    instance.extendedGroupingSupported = original
    assert instance.extendedGroupingSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_defaultKeywordForInsertValueSupported_setter(instance):
    original = instance.defaultKeywordForInsertValueSupported
    instance.defaultKeywordForInsertValueSupported = original
    assert instance.defaultKeywordForInsertValueSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_hostVariableMarker_setter(instance):
    original = instance.hostVariableMarker
    instance.hostVariableMarker = original
    assert instance.hostVariableMarker == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_tableAliasInDeleteSupported_setter(instance):
    original = instance.tableAliasInDeleteSupported
    instance.tableAliasInDeleteSupported = original
    assert instance.tableAliasInDeleteSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_castExpressionSupported_setter(instance):
    original = instance.castExpressionSupported
    instance.castExpressionSupported = original
    assert instance.castExpressionSupported == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_identifierQuoteString_setter(instance):
    original = instance.identifierQuoteString
    instance.identifierQuoteString = original
    assert instance.identifierQuoteString == original



@given(instance=dbdefinition_QueryDefinition_strategy)
def test_dbdefinition_querydefinition_hostVariableMarkerSupported_setter(instance):
    original = instance.hostVariableMarkerSupported
    instance.hostVariableMarkerSupported = original
    assert instance.hostVariableMarkerSupported == original

@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_userdefinedtypedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_UserDefinedTypeDefinition)



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_dbdefinition_userdefinedtypedefinition_defaultValueSupported_setter(instance):
    original = instance.defaultValueSupported
    instance.defaultValueSupported = original
    assert instance.defaultValueSupported == original



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_dbdefinition_userdefinedtypedefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_dbdefinition_userdefinedtypedefinition_structuredTypeSupported_setter(instance):
    original = instance.structuredTypeSupported
    instance.structuredTypeSupported = original
    assert instance.structuredTypeSupported == original



@given(instance=dbdefinition_UserDefinedTypeDefinition_strategy)
def test_dbdefinition_userdefinedtypedefinition_distinctTypeSupported_setter(instance):
    original = instance.distinctTypeSupported
    instance.distinctTypeSupported = original
    assert instance.distinctTypeSupported == original

@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_predefineddatatypedefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_PredefinedDataTypeDefinition)



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_defaultValueTypes_setter(instance):
    original = instance.defaultValueTypes
    instance.defaultValueTypes = original
    assert instance.defaultValueTypes == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_identitySupported_setter(instance):
    original = instance.identitySupported
    instance.identitySupported = original
    assert instance.identitySupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_lengthSemantic_setter(instance):
    original = instance.lengthSemantic
    instance.lengthSemantic = original
    assert instance.lengthSemantic == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_minimumScale_setter(instance):
    original = instance.minimumScale
    instance.minimumScale = original
    assert instance.minimumScale == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_languageType_setter(instance):
    original = instance.languageType
    instance.languageType = original
    assert instance.languageType == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_precisionSupported_setter(instance):
    original = instance.precisionSupported
    instance.precisionSupported = original
    assert instance.precisionSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_scaleSupported_setter(instance):
    original = instance.scaleSupported
    instance.scaleSupported = original
    assert instance.scaleSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_largeValueSpecifierLength_setter(instance):
    original = instance.largeValueSpecifierLength
    instance.largeValueSpecifierLength = original
    assert instance.largeValueSpecifierLength == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_jdbcEnumType_setter(instance):
    original = instance.jdbcEnumType
    instance.jdbcEnumType = original
    assert instance.jdbcEnumType == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_characterSetSuffix_setter(instance):
    original = instance.characterSetSuffix
    instance.characterSetSuffix = original
    assert instance.characterSetSuffix == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_defaultPrecision_setter(instance):
    original = instance.defaultPrecision
    instance.defaultPrecision = original
    assert instance.defaultPrecision == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_lengthSemanticSupported_setter(instance):
    original = instance.lengthSemanticSupported
    instance.lengthSemanticSupported = original
    assert instance.lengthSemanticSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_lengthSupported_setter(instance):
    original = instance.lengthSupported
    instance.lengthSupported = original
    assert instance.lengthSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_defaultSupported_setter(instance):
    original = instance.defaultSupported
    instance.defaultSupported = original
    assert instance.defaultSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_displayNameSupported_setter(instance):
    original = instance.displayNameSupported
    instance.displayNameSupported = original
    assert instance.displayNameSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_nullableSupported_setter(instance):
    original = instance.nullableSupported
    instance.nullableSupported = original
    assert instance.nullableSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_defaultLength_setter(instance):
    original = instance.defaultLength
    instance.defaultLength = original
    assert instance.defaultLength == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_fieldQualifierSeparator_setter(instance):
    original = instance.fieldQualifierSeparator
    instance.fieldQualifierSeparator = original
    assert instance.fieldQualifierSeparator == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_javaClassName_setter(instance):
    original = instance.javaClassName
    instance.javaClassName = original
    assert instance.javaClassName == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_keyConstraintSupported_setter(instance):
    original = instance.keyConstraintSupported
    instance.keyConstraintSupported = original
    assert instance.keyConstraintSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_trailingFieldQualifierSupported_setter(instance):
    original = instance.trailingFieldQualifierSupported
    instance.trailingFieldQualifierSupported = original
    assert instance.trailingFieldQualifierSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_encodingSchemeSuffix_setter(instance):
    original = instance.encodingSchemeSuffix
    instance.encodingSchemeSuffix = original
    assert instance.encodingSchemeSuffix == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_largeValueSpecifierName_setter(instance):
    original = instance.largeValueSpecifierName
    instance.largeValueSpecifierName = original
    assert instance.largeValueSpecifierName == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_largeValueSpecifierSupported_setter(instance):
    original = instance.largeValueSpecifierSupported
    instance.largeValueSpecifierSupported = original
    assert instance.largeValueSpecifierSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_leadingFieldQualifierSupported_setter(instance):
    original = instance.leadingFieldQualifierSupported
    instance.leadingFieldQualifierSupported = original
    assert instance.leadingFieldQualifierSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_cutoffPrecision_setter(instance):
    original = instance.cutoffPrecision
    instance.cutoffPrecision = original
    assert instance.cutoffPrecision == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_defaultScale_setter(instance):
    original = instance.defaultScale
    instance.defaultScale = original
    assert instance.defaultScale == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_encodingScheme_setter(instance):
    original = instance.encodingScheme
    instance.encodingScheme = original
    assert instance.encodingScheme == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_maximumPrecision_setter(instance):
    original = instance.maximumPrecision
    instance.maximumPrecision = original
    assert instance.maximumPrecision == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_maximumLength_setter(instance):
    original = instance.maximumLength
    instance.maximumLength = original
    assert instance.maximumLength == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_groupingSupported_setter(instance):
    original = instance.groupingSupported
    instance.groupingSupported = original
    assert instance.groupingSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_clusteringSupported_setter(instance):
    original = instance.clusteringSupported
    instance.clusteringSupported = original
    assert instance.clusteringSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_characterSet_setter(instance):
    original = instance.characterSet
    instance.characterSet = original
    assert instance.characterSet == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_orderingSupported_setter(instance):
    original = instance.orderingSupported
    instance.orderingSupported = original
    assert instance.orderingSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_minimumValue_setter(instance):
    original = instance.minimumValue
    instance.minimumValue = original
    assert instance.minimumValue == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_maximumValue_setter(instance):
    original = instance.maximumValue
    instance.maximumValue = original
    assert instance.maximumValue == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_bitDataSupported_setter(instance):
    original = instance.bitDataSupported
    instance.bitDataSupported = original
    assert instance.bitDataSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_maximumScale_setter(instance):
    original = instance.maximumScale
    instance.maximumScale = original
    assert instance.maximumScale == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_multipleColumnsSupported_setter(instance):
    original = instance.multipleColumnsSupported
    instance.multipleColumnsSupported = original
    assert instance.multipleColumnsSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_fillFactorSupported_setter(instance):
    original = instance.fillFactorSupported
    instance.fillFactorSupported = original
    assert instance.fillFactorSupported == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original



@given(instance=dbdefinition_PredefinedDataTypeDefinition_strategy)
def test_dbdefinition_predefineddatatypedefinition_lengthUnit_setter(instance):
    original = instance.lengthUnit
    instance.lengthUnit = original
    assert instance.lengthUnit == original

@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
@settings(max_examples=50)
def test_dbdefinition_databasevendordefinition_instantiation(instance):
    assert isinstance(instance, dbdefinition_DatabaseVendorDefinition)



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_quotedDMLSupported_setter(instance):
    original = instance.quotedDMLSupported
    instance.quotedDMLSupported = original
    assert instance.quotedDMLSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_joinSupported_setter(instance):
    original = instance.joinSupported
    instance.joinSupported = original
    assert instance.joinSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_viewTriggerSupported_setter(instance):
    original = instance.viewTriggerSupported
    instance.viewTriggerSupported = original
    assert instance.viewTriggerSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_mQTIndexSupported_setter(instance):
    original = instance.mQTIndexSupported
    instance.mQTIndexSupported = original
    assert instance.mQTIndexSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_quotedDDLSupported_setter(instance):
    original = instance.quotedDDLSupported
    instance.quotedDDLSupported = original
    assert instance.quotedDDLSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_sqlUDFSupported_setter(instance):
    original = instance.sqlUDFSupported
    instance.sqlUDFSupported = original
    assert instance.sqlUDFSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_triggerSupported_setter(instance):
    original = instance.triggerSupported
    instance.triggerSupported = original
    assert instance.triggerSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_constraintsSupported_setter(instance):
    original = instance.constraintsSupported
    instance.constraintsSupported = original
    assert instance.constraintsSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_synonymSupported_setter(instance):
    original = instance.synonymSupported
    instance.synonymSupported = original
    assert instance.synonymSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_packageSupported_setter(instance):
    original = instance.packageSupported
    instance.packageSupported = original
    assert instance.packageSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_schemaSupported_setter(instance):
    original = instance.schemaSupported
    instance.schemaSupported = original
    assert instance.schemaSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_domainSupported_setter(instance):
    original = instance.domainSupported
    instance.domainSupported = original
    assert instance.domainSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_maximumCommentLength_setter(instance):
    original = instance.maximumCommentLength
    instance.maximumCommentLength = original
    assert instance.maximumCommentLength == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_userDefinedTypeSupported_setter(instance):
    original = instance.userDefinedTypeSupported
    instance.userDefinedTypeSupported = original
    assert instance.userDefinedTypeSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_xmlSupported_setter(instance):
    original = instance.xmlSupported
    instance.xmlSupported = original
    assert instance.xmlSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_snapshotViewSupported_setter(instance):
    original = instance.snapshotViewSupported
    instance.snapshotViewSupported = original
    assert instance.snapshotViewSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_groupSupported_setter(instance):
    original = instance.groupSupported
    instance.groupSupported = original
    assert instance.groupSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_mQTSupported_setter(instance):
    original = instance.mQTSupported
    instance.mQTSupported = original
    assert instance.mQTSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_roleSupported_setter(instance):
    original = instance.roleSupported
    instance.roleSupported = original
    assert instance.roleSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_nicknameSupported_setter(instance):
    original = instance.nicknameSupported
    instance.nicknameSupported = original
    assert instance.nicknameSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_userSupported_setter(instance):
    original = instance.userSupported
    instance.userSupported = original
    assert instance.userSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_maximumIdentifierLength_setter(instance):
    original = instance.maximumIdentifierLength
    instance.maximumIdentifierLength = original
    assert instance.maximumIdentifierLength == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_sequenceSupported_setter(instance):
    original = instance.sequenceSupported
    instance.sequenceSupported = original
    assert instance.sequenceSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_authorizationIdentifierSupported_setter(instance):
    original = instance.authorizationIdentifierSupported
    instance.authorizationIdentifierSupported = original
    assert instance.authorizationIdentifierSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_tablespacesSupported_setter(instance):
    original = instance.tablespacesSupported
    instance.tablespacesSupported = original
    assert instance.tablespacesSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_uDFSupported_setter(instance):
    original = instance.uDFSupported
    instance.uDFSupported = original
    assert instance.uDFSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_constructedDataTypeSupported_setter(instance):
    original = instance.constructedDataTypeSupported
    instance.constructedDataTypeSupported = original
    assert instance.constructedDataTypeSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_storedProcedureSupported_setter(instance):
    original = instance.storedProcedureSupported
    instance.storedProcedureSupported = original
    assert instance.storedProcedureSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_roleAuthorizationSupported_setter(instance):
    original = instance.roleAuthorizationSupported
    instance.roleAuthorizationSupported = original
    assert instance.roleAuthorizationSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_SQLStatementSupported_setter(instance):
    original = instance.SQLStatementSupported
    instance.SQLStatementSupported = original
    assert instance.SQLStatementSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_aliasSupported_setter(instance):
    original = instance.aliasSupported
    instance.aliasSupported = original
    assert instance.aliasSupported == original



@given(instance=dbdefinition_DatabaseVendorDefinition_strategy)
def test_dbdefinition_databasevendordefinition_eventSupported_setter(instance):
    original = instance.eventSupported
    instance.eventSupported = original
    assert instance.eventSupported == original
