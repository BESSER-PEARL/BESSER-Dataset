import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdbms_RdbmsOperationMeta,
    rdbms_RdbmsViewRecordValue,
    RdbmsFieldOperation,
    rdbms_RdbmsDeleteFieldOperation,
    rdbms_RdbmsModifyFieldOperation,
    rdbms_RdbmsCreateFieldOperation,
    RdbmsTableOperation,
    rdbms_RdbmsDeleteTableOperation,
    rdbms_RdbmsCreateTableOperation,
    RdbmsExpression,
    rdbms_RdbmsRelationExpression,
    rdbms_RdbmsLabelExpression,
    rdbms_RdbmsFeature,
    rdbms_RdbmsViewRecord,
    rdbms_RdbmsConfiguration,
    rdbms_RdbmsModel,
    rdbms_RdbmsModifyTableOperation,
    RdbmsViewTableField,
    rdbms_RdbmsViewAliasField,
    rdbms_RdbmsViewForeignIdentifierField,
    RdbmsViewField,
    rdbms_RdbmsViewTableField,
    rdbms_RdbmsViewExpressionField,
    RdbmsViewAliasField,
    rdbms_RdbmsViewValueField,
    rdbms_RdbmsViewIdentifierField,
    rdbms_RdbmsViewRelation,
    RdbmsField,
    rdbms_RdbmsValueField,
    RdbmsTable,
    RdbmsIdentifierField,
    rdbms_RdbmsForeignKey,
    rdbms_RdbmsFieldType,
    rdbms_RdbmsIdentifierField,
    rdbms_RdbmsJunctionTable,
    rdbms_RdbmsElement,
    RdbmsElement,
    rdbms_RdbmsTable,
    rdbms_RdbmsUniqueConstraint,
    rdbms_RdbmsExpression,
    rdbms_RdbmsField,
    rdbms_RdbmsTableAlias,
    rdbms_RdbmsFieldOperation,
    rdbms_RdbmsView,
    rdbms_RdbmsTableOperation,
    rdbms_RdbmsIndex,
    rdbms_RdbmsViewField,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms_rdbmsoperationmeta_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsOperationMeta)


def test_rdbms_rdbmsoperationmeta_constructor_exists():
    assert callable(rdbms_RdbmsOperationMeta.__init__)


def test_rdbms_rdbmsoperationmeta_constructor_args():
    sig = inspect.signature(rdbms_RdbmsOperationMeta.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewrecordvalue_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewRecordValue)


def test_rdbms_rdbmsviewrecordvalue_constructor_exists():
    assert callable(rdbms_RdbmsViewRecordValue.__init__)


def test_rdbms_rdbmsviewrecordvalue_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewRecordValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rdbms_rdbmsviewrecordvalue_has_value():
    assert hasattr(rdbms_RdbmsViewRecordValue, "value")
    descriptor = None
    for klass in rdbms_RdbmsViewRecordValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsfieldoperation_is_not_abstract():
    assert not inspect.isabstract(RdbmsFieldOperation)


def test_rdbmsfieldoperation_constructor_exists():
    assert callable(RdbmsFieldOperation.__init__)


def test_rdbmsfieldoperation_constructor_args():
    sig = inspect.signature(RdbmsFieldOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsdeletefieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsDeleteFieldOperation)


def test_rdbms_rdbmsdeletefieldoperation_constructor_exists():
    assert callable(rdbms_RdbmsDeleteFieldOperation.__init__)


def test_rdbms_rdbmsdeletefieldoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsDeleteFieldOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsmodifyfieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsModifyFieldOperation)


def test_rdbms_rdbmsmodifyfieldoperation_constructor_exists():
    assert callable(rdbms_RdbmsModifyFieldOperation.__init__)


def test_rdbms_rdbmsmodifyfieldoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsModifyFieldOperation.__init__)
    params = list(sig.parameters.keys())
    assert "changedForeignKeyToValueField" in params, "Missing parameter 'changedForeignKeyToValueField'"
    assert "nameChanged" in params, "Missing parameter 'nameChanged'"
    assert "sizeChanged" in params, "Missing parameter 'sizeChanged'"
    assert "changedValueFieldToForeignKey" in params, "Missing parameter 'changedValueFieldToForeignKey'"
    assert "mandatoryChanged" in params, "Missing parameter 'mandatoryChanged'"
    assert "typeChanged" in params, "Missing parameter 'typeChanged'"

def test_rdbms_rdbmsmodifyfieldoperation_has_changedForeignKeyToValueField():
    assert hasattr(rdbms_RdbmsModifyFieldOperation, "changedForeignKeyToValueField")
    descriptor = None
    for klass in rdbms_RdbmsModifyFieldOperation.__mro__:
        if "changedForeignKeyToValueField" in klass.__dict__:
            descriptor = klass.__dict__["changedForeignKeyToValueField"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsmodifyfieldoperation_has_nameChanged():
    assert hasattr(rdbms_RdbmsModifyFieldOperation, "nameChanged")
    descriptor = None
    for klass in rdbms_RdbmsModifyFieldOperation.__mro__:
        if "nameChanged" in klass.__dict__:
            descriptor = klass.__dict__["nameChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsmodifyfieldoperation_has_sizeChanged():
    assert hasattr(rdbms_RdbmsModifyFieldOperation, "sizeChanged")
    descriptor = None
    for klass in rdbms_RdbmsModifyFieldOperation.__mro__:
        if "sizeChanged" in klass.__dict__:
            descriptor = klass.__dict__["sizeChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsmodifyfieldoperation_has_changedValueFieldToForeignKey():
    assert hasattr(rdbms_RdbmsModifyFieldOperation, "changedValueFieldToForeignKey")
    descriptor = None
    for klass in rdbms_RdbmsModifyFieldOperation.__mro__:
        if "changedValueFieldToForeignKey" in klass.__dict__:
            descriptor = klass.__dict__["changedValueFieldToForeignKey"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsmodifyfieldoperation_has_mandatoryChanged():
    assert hasattr(rdbms_RdbmsModifyFieldOperation, "mandatoryChanged")
    descriptor = None
    for klass in rdbms_RdbmsModifyFieldOperation.__mro__:
        if "mandatoryChanged" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsmodifyfieldoperation_has_typeChanged():
    assert hasattr(rdbms_RdbmsModifyFieldOperation, "typeChanged")
    descriptor = None
    for klass in rdbms_RdbmsModifyFieldOperation.__mro__:
        if "typeChanged" in klass.__dict__:
            descriptor = klass.__dict__["typeChanged"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmscreatefieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsCreateFieldOperation)


def test_rdbms_rdbmscreatefieldoperation_constructor_exists():
    assert callable(rdbms_RdbmsCreateFieldOperation.__init__)


def test_rdbms_rdbmscreatefieldoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsCreateFieldOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbmstableoperation_is_not_abstract():
    assert not inspect.isabstract(RdbmsTableOperation)


def test_rdbmstableoperation_constructor_exists():
    assert callable(RdbmsTableOperation.__init__)


def test_rdbmstableoperation_constructor_args():
    sig = inspect.signature(RdbmsTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsdeletetableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsDeleteTableOperation)


def test_rdbms_rdbmsdeletetableoperation_constructor_exists():
    assert callable(rdbms_RdbmsDeleteTableOperation.__init__)


def test_rdbms_rdbmsdeletetableoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsDeleteTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmscreatetableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsCreateTableOperation)


def test_rdbms_rdbmscreatetableoperation_constructor_exists():
    assert callable(rdbms_RdbmsCreateTableOperation.__init__)


def test_rdbms_rdbmscreatetableoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsCreateTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsexpression_is_not_abstract():
    assert not inspect.isabstract(RdbmsExpression)


def test_rdbmsexpression_constructor_exists():
    assert callable(RdbmsExpression.__init__)


def test_rdbmsexpression_constructor_args():
    sig = inspect.signature(RdbmsExpression.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsrelationexpression_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsRelationExpression)


def test_rdbms_rdbmsrelationexpression_constructor_exists():
    assert callable(rdbms_RdbmsRelationExpression.__init__)


def test_rdbms_rdbmsrelationexpression_constructor_args():
    sig = inspect.signature(rdbms_RdbmsRelationExpression.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmslabelexpression_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsLabelExpression)


def test_rdbms_rdbmslabelexpression_constructor_exists():
    assert callable(rdbms_RdbmsLabelExpression.__init__)


def test_rdbms_rdbmslabelexpression_constructor_args():
    sig = inspect.signature(rdbms_RdbmsLabelExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_rdbms_rdbmslabelexpression_has_text():
    assert hasattr(rdbms_RdbmsLabelExpression, "text")
    descriptor = None
    for klass in rdbms_RdbmsLabelExpression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsfeature_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsFeature)


def test_rdbms_rdbmsfeature_constructor_exists():
    assert callable(rdbms_RdbmsFeature.__init__)


def test_rdbms_rdbmsfeature_constructor_args():
    sig = inspect.signature(rdbms_RdbmsFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_rdbmsfeature_has_name():
    assert hasattr(rdbms_RdbmsFeature, "name")
    descriptor = None
    for klass in rdbms_RdbmsFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsviewrecord_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewRecord)


def test_rdbms_rdbmsviewrecord_constructor_exists():
    assert callable(rdbms_RdbmsViewRecord.__init__)


def test_rdbms_rdbmsviewrecord_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewRecord.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsconfiguration_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsConfiguration)


def test_rdbms_rdbmsconfiguration_constructor_exists():
    assert callable(rdbms_RdbmsConfiguration.__init__)


def test_rdbms_rdbmsconfiguration_constructor_args():
    sig = inspect.signature(rdbms_RdbmsConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "dialect" in params, "Missing parameter 'dialect'"

def test_rdbms_rdbmsconfiguration_has_dialect():
    assert hasattr(rdbms_RdbmsConfiguration, "dialect")
    descriptor = None
    for klass in rdbms_RdbmsConfiguration.__mro__:
        if "dialect" in klass.__dict__:
            descriptor = klass.__dict__["dialect"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsModel)


def test_rdbms_rdbmsmodel_constructor_exists():
    assert callable(rdbms_RdbmsModel.__init__)


def test_rdbms_rdbmsmodel_constructor_args():
    sig = inspect.signature(rdbms_RdbmsModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_rdbms_rdbmsmodel_has_version():
    assert hasattr(rdbms_RdbmsModel, "version")
    descriptor = None
    for klass in rdbms_RdbmsModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsmodifytableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsModifyTableOperation)


def test_rdbms_rdbmsmodifytableoperation_constructor_exists():
    assert callable(rdbms_RdbmsModifyTableOperation.__init__)


def test_rdbms_rdbmsmodifytableoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsModifyTableOperation.__init__)
    params = list(sig.parameters.keys())
    assert "nameChanged" in params, "Missing parameter 'nameChanged'"

def test_rdbms_rdbmsmodifytableoperation_has_nameChanged():
    assert hasattr(rdbms_RdbmsModifyTableOperation, "nameChanged")
    descriptor = None
    for klass in rdbms_RdbmsModifyTableOperation.__mro__:
        if "nameChanged" in klass.__dict__:
            descriptor = klass.__dict__["nameChanged"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsviewtablefield_is_not_abstract():
    assert not inspect.isabstract(RdbmsViewTableField)


def test_rdbmsviewtablefield_constructor_exists():
    assert callable(RdbmsViewTableField.__init__)


def test_rdbmsviewtablefield_constructor_args():
    sig = inspect.signature(RdbmsViewTableField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewaliasfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewAliasField)


def test_rdbms_rdbmsviewaliasfield_constructor_exists():
    assert callable(rdbms_RdbmsViewAliasField.__init__)


def test_rdbms_rdbmsviewaliasfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewAliasField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewforeignidentifierfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewForeignIdentifierField)


def test_rdbms_rdbmsviewforeignidentifierfield_constructor_exists():
    assert callable(rdbms_RdbmsViewForeignIdentifierField.__init__)


def test_rdbms_rdbmsviewforeignidentifierfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewForeignIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsviewfield_is_not_abstract():
    assert not inspect.isabstract(RdbmsViewField)


def test_rdbmsviewfield_constructor_exists():
    assert callable(RdbmsViewField.__init__)


def test_rdbmsviewfield_constructor_args():
    sig = inspect.signature(RdbmsViewField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewtablefield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewTableField)


def test_rdbms_rdbmsviewtablefield_constructor_exists():
    assert callable(rdbms_RdbmsViewTableField.__init__)


def test_rdbms_rdbmsviewtablefield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewTableField.__init__)
    params = list(sig.parameters.keys())
    assert "foreign" in params, "Missing parameter 'foreign'"

def test_rdbms_rdbmsviewtablefield_has_foreign():
    assert hasattr(rdbms_RdbmsViewTableField, "foreign")
    descriptor = None
    for klass in rdbms_RdbmsViewTableField.__mro__:
        if "foreign" in klass.__dict__:
            descriptor = klass.__dict__["foreign"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsviewexpressionfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewExpressionField)


def test_rdbms_rdbmsviewexpressionfield_constructor_exists():
    assert callable(rdbms_RdbmsViewExpressionField.__init__)


def test_rdbms_rdbmsviewexpressionfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewExpressionField.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_rdbms_rdbmsviewexpressionfield_has_expression():
    assert hasattr(rdbms_RdbmsViewExpressionField, "expression")
    descriptor = None
    for klass in rdbms_RdbmsViewExpressionField.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsviewaliasfield_is_not_abstract():
    assert not inspect.isabstract(RdbmsViewAliasField)


def test_rdbmsviewaliasfield_constructor_exists():
    assert callable(RdbmsViewAliasField.__init__)


def test_rdbmsviewaliasfield_constructor_args():
    sig = inspect.signature(RdbmsViewAliasField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewvaluefield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewValueField)


def test_rdbms_rdbmsviewvaluefield_constructor_exists():
    assert callable(rdbms_RdbmsViewValueField.__init__)


def test_rdbms_rdbmsviewvaluefield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewValueField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewidentifierfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewIdentifierField)


def test_rdbms_rdbmsviewidentifierfield_constructor_exists():
    assert callable(rdbms_RdbmsViewIdentifierField.__init__)


def test_rdbms_rdbmsviewidentifierfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsviewrelation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewRelation)


def test_rdbms_rdbmsviewrelation_constructor_exists():
    assert callable(rdbms_RdbmsViewRelation.__init__)


def test_rdbms_rdbmsviewrelation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewRelation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_rdbmsviewrelation_has_name():
    assert hasattr(rdbms_RdbmsViewRelation, "name")
    descriptor = None
    for klass in rdbms_RdbmsViewRelation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsfield_is_not_abstract():
    assert not inspect.isabstract(RdbmsField)


def test_rdbmsfield_constructor_exists():
    assert callable(RdbmsField.__init__)


def test_rdbmsfield_constructor_args():
    sig = inspect.signature(RdbmsField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsvaluefield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsValueField)


def test_rdbms_rdbmsvaluefield_constructor_exists():
    assert callable(rdbms_RdbmsValueField.__init__)


def test_rdbms_rdbmsvaluefield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsValueField.__init__)
    params = list(sig.parameters.keys())
    assert "technical" in params, "Missing parameter 'technical'"

def test_rdbms_rdbmsvaluefield_has_technical():
    assert hasattr(rdbms_RdbmsValueField, "technical")
    descriptor = None
    for klass in rdbms_RdbmsValueField.__mro__:
        if "technical" in klass.__dict__:
            descriptor = klass.__dict__["technical"]
            break
    assert isinstance(descriptor, property)



def test_rdbmstable_is_not_abstract():
    assert not inspect.isabstract(RdbmsTable)


def test_rdbmstable_constructor_exists():
    assert callable(RdbmsTable.__init__)


def test_rdbmstable_constructor_args():
    sig = inspect.signature(RdbmsTable.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsidentifierfield_is_not_abstract():
    assert not inspect.isabstract(RdbmsIdentifierField)


def test_rdbmsidentifierfield_constructor_exists():
    assert callable(RdbmsIdentifierField.__init__)


def test_rdbmsidentifierfield_constructor_args():
    sig = inspect.signature(RdbmsIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsforeignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsForeignKey)


def test_rdbms_rdbmsforeignkey_constructor_exists():
    assert callable(rdbms_RdbmsForeignKey.__init__)


def test_rdbms_rdbmsforeignkey_constructor_args():
    sig = inspect.signature(rdbms_RdbmsForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "inheritenceBased" in params, "Missing parameter 'inheritenceBased'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "foreignKeySqlName" in params, "Missing parameter 'foreignKeySqlName'"
    assert "deleteOnCascade" in params, "Missing parameter 'deleteOnCascade'"
    assert "deferred" in params, "Missing parameter 'deferred'"

def test_rdbms_rdbmsforeignkey_has_inheritenceBased():
    assert hasattr(rdbms_RdbmsForeignKey, "inheritenceBased")
    descriptor = None
    for klass in rdbms_RdbmsForeignKey.__mro__:
        if "inheritenceBased" in klass.__dict__:
            descriptor = klass.__dict__["inheritenceBased"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsforeignkey_has_readOnly():
    assert hasattr(rdbms_RdbmsForeignKey, "readOnly")
    descriptor = None
    for klass in rdbms_RdbmsForeignKey.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsforeignkey_has_foreignKeySqlName():
    assert hasattr(rdbms_RdbmsForeignKey, "foreignKeySqlName")
    descriptor = None
    for klass in rdbms_RdbmsForeignKey.__mro__:
        if "foreignKeySqlName" in klass.__dict__:
            descriptor = klass.__dict__["foreignKeySqlName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsforeignkey_has_deleteOnCascade():
    assert hasattr(rdbms_RdbmsForeignKey, "deleteOnCascade")
    descriptor = None
    for klass in rdbms_RdbmsForeignKey.__mro__:
        if "deleteOnCascade" in klass.__dict__:
            descriptor = klass.__dict__["deleteOnCascade"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsforeignkey_has_deferred():
    assert hasattr(rdbms_RdbmsForeignKey, "deferred")
    descriptor = None
    for klass in rdbms_RdbmsForeignKey.__mro__:
        if "deferred" in klass.__dict__:
            descriptor = klass.__dict__["deferred"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsfieldtype_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsFieldType)


def test_rdbms_rdbmsfieldtype_constructor_exists():
    assert callable(rdbms_RdbmsFieldType.__init__)


def test_rdbms_rdbmsfieldtype_constructor_args():
    sig = inspect.signature(rdbms_RdbmsFieldType.__init__)
    params = list(sig.parameters.keys())
    assert "rdbmsTypeName" in params, "Missing parameter 'rdbmsTypeName'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "storageByte" in params, "Missing parameter 'storageByte'"
    assert "description" in params, "Missing parameter 'description'"

def test_rdbms_rdbmsfieldtype_has_rdbmsTypeName():
    assert hasattr(rdbms_RdbmsFieldType, "rdbmsTypeName")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "rdbmsTypeName" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsTypeName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_uuid():
    assert hasattr(rdbms_RdbmsFieldType, "uuid")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_size():
    assert hasattr(rdbms_RdbmsFieldType, "size")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_name():
    assert hasattr(rdbms_RdbmsFieldType, "name")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_precision():
    assert hasattr(rdbms_RdbmsFieldType, "precision")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_scale():
    assert hasattr(rdbms_RdbmsFieldType, "scale")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_storageByte():
    assert hasattr(rdbms_RdbmsFieldType, "storageByte")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "storageByte" in klass.__dict__:
            descriptor = klass.__dict__["storageByte"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfieldtype_has_description():
    assert hasattr(rdbms_RdbmsFieldType, "description")
    descriptor = None
    for klass in rdbms_RdbmsFieldType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsidentifierfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsIdentifierField)


def test_rdbms_rdbmsidentifierfield_constructor_exists():
    assert callable(rdbms_RdbmsIdentifierField.__init__)


def test_rdbms_rdbmsidentifierfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsjunctiontable_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsJunctionTable)


def test_rdbms_rdbmsjunctiontable_constructor_exists():
    assert callable(rdbms_RdbmsJunctionTable.__init__)


def test_rdbms_rdbmsjunctiontable_constructor_args():
    sig = inspect.signature(rdbms_RdbmsJunctionTable.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmselement_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsElement)


def test_rdbms_rdbmselement_constructor_exists():
    assert callable(rdbms_RdbmsElement.__init__)


def test_rdbms_rdbmselement_constructor_args():
    sig = inspect.signature(rdbms_RdbmsElement.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "sqlName" in params, "Missing parameter 'sqlName'"
    assert "originalPackage" in params, "Missing parameter 'originalPackage'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "originalName" in params, "Missing parameter 'originalName'"

def test_rdbms_rdbmselement_has_shortName():
    assert hasattr(rdbms_RdbmsElement, "shortName")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_name():
    assert hasattr(rdbms_RdbmsElement, "name")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_description():
    assert hasattr(rdbms_RdbmsElement, "description")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_sqlName():
    assert hasattr(rdbms_RdbmsElement, "sqlName")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "sqlName" in klass.__dict__:
            descriptor = klass.__dict__["sqlName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_originalPackage():
    assert hasattr(rdbms_RdbmsElement, "originalPackage")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "originalPackage" in klass.__dict__:
            descriptor = klass.__dict__["originalPackage"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_fullName():
    assert hasattr(rdbms_RdbmsElement, "fullName")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_uuid():
    assert hasattr(rdbms_RdbmsElement, "uuid")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmselement_has_originalName():
    assert hasattr(rdbms_RdbmsElement, "originalName")
    descriptor = None
    for klass in rdbms_RdbmsElement.__mro__:
        if "originalName" in klass.__dict__:
            descriptor = klass.__dict__["originalName"]
            break
    assert isinstance(descriptor, property)



def test_rdbmselement_is_not_abstract():
    assert not inspect.isabstract(RdbmsElement)


def test_rdbmselement_constructor_exists():
    assert callable(RdbmsElement.__init__)


def test_rdbmselement_constructor_args():
    sig = inspect.signature(RdbmsElement.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmstable_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsTable)


def test_rdbms_rdbmstable_constructor_exists():
    assert callable(rdbms_RdbmsTable.__init__)


def test_rdbms_rdbmstable_constructor_args():
    sig = inspect.signature(rdbms_RdbmsTable.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsuniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsUniqueConstraint)


def test_rdbms_rdbmsuniqueconstraint_constructor_exists():
    assert callable(rdbms_RdbmsUniqueConstraint.__init__)


def test_rdbms_rdbmsuniqueconstraint_constructor_args():
    sig = inspect.signature(rdbms_RdbmsUniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsexpression_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsExpression)


def test_rdbms_rdbmsexpression_constructor_exists():
    assert callable(rdbms_RdbmsExpression.__init__)


def test_rdbms_rdbmsexpression_constructor_args():
    sig = inspect.signature(rdbms_RdbmsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_rdbms_rdbmsexpression_has_expression():
    assert hasattr(rdbms_RdbmsExpression, "expression")
    descriptor = None
    for klass in rdbms_RdbmsExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsField)


def test_rdbms_rdbmsfield_constructor_exists():
    assert callable(rdbms_RdbmsField.__init__)


def test_rdbms_rdbmsfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsField.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "rdbmsTypeName" in params, "Missing parameter 'rdbmsTypeName'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "storageByte" in params, "Missing parameter 'storageByte'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_rdbms_rdbmsfield_has_size():
    assert hasattr(rdbms_RdbmsField, "size")
    descriptor = None
    for klass in rdbms_RdbmsField.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfield_has_rdbmsTypeName():
    assert hasattr(rdbms_RdbmsField, "rdbmsTypeName")
    descriptor = None
    for klass in rdbms_RdbmsField.__mro__:
        if "rdbmsTypeName" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsTypeName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfield_has_mandatory():
    assert hasattr(rdbms_RdbmsField, "mandatory")
    descriptor = None
    for klass in rdbms_RdbmsField.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfield_has_precision():
    assert hasattr(rdbms_RdbmsField, "precision")
    descriptor = None
    for klass in rdbms_RdbmsField.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfield_has_storageByte():
    assert hasattr(rdbms_RdbmsField, "storageByte")
    descriptor = None
    for klass in rdbms_RdbmsField.__mro__:
        if "storageByte" in klass.__dict__:
            descriptor = klass.__dict__["storageByte"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rdbmsfield_has_scale():
    assert hasattr(rdbms_RdbmsField, "scale")
    descriptor = None
    for klass in rdbms_RdbmsField.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmstablealias_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsTableAlias)


def test_rdbms_rdbmstablealias_constructor_exists():
    assert callable(rdbms_RdbmsTableAlias.__init__)


def test_rdbms_rdbmstablealias_constructor_args():
    sig = inspect.signature(rdbms_RdbmsTableAlias.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsfieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsFieldOperation)


def test_rdbms_rdbmsfieldoperation_constructor_exists():
    assert callable(rdbms_RdbmsFieldOperation.__init__)


def test_rdbms_rdbmsfieldoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsFieldOperation.__init__)
    params = list(sig.parameters.keys())
    assert "reviewRequired" in params, "Missing parameter 'reviewRequired'"

def test_rdbms_rdbmsfieldoperation_has_reviewRequired():
    assert hasattr(rdbms_RdbmsFieldOperation, "reviewRequired")
    descriptor = None
    for klass in rdbms_RdbmsFieldOperation.__mro__:
        if "reviewRequired" in klass.__dict__:
            descriptor = klass.__dict__["reviewRequired"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsview_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsView)


def test_rdbms_rdbmsview_constructor_exists():
    assert callable(rdbms_RdbmsView.__init__)


def test_rdbms_rdbmsview_constructor_args():
    sig = inspect.signature(rdbms_RdbmsView.__init__)
    params = list(sig.parameters.keys())
    assert "originUuid" in params, "Missing parameter 'originUuid'"

def test_rdbms_rdbmsview_has_originUuid():
    assert hasattr(rdbms_RdbmsView, "originUuid")
    descriptor = None
    for klass in rdbms_RdbmsView.__mro__:
        if "originUuid" in klass.__dict__:
            descriptor = klass.__dict__["originUuid"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmstableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsTableOperation)


def test_rdbms_rdbmstableoperation_constructor_exists():
    assert callable(rdbms_RdbmsTableOperation.__init__)


def test_rdbms_rdbmstableoperation_constructor_args():
    sig = inspect.signature(rdbms_RdbmsTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_rdbmsindex_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsIndex)


def test_rdbms_rdbmsindex_constructor_exists():
    assert callable(rdbms_RdbmsIndex.__init__)


def test_rdbms_rdbmsindex_constructor_args():
    sig = inspect.signature(rdbms_RdbmsIndex.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_rdbms_rdbmsindex_has_unique():
    assert hasattr(rdbms_RdbmsIndex, "unique")
    descriptor = None
    for klass in rdbms_RdbmsIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsviewfield_is_not_abstract():
    assert not inspect.isabstract(rdbms_RdbmsViewField)


def test_rdbms_rdbmsviewfield_constructor_exists():
    assert callable(rdbms_RdbmsViewField.__init__)


def test_rdbms_rdbmsviewfield_constructor_args():
    sig = inspect.signature(rdbms_RdbmsViewField.__init__)
    params = list(sig.parameters.keys())
    assert "inherited" in params, "Missing parameter 'inherited'"

def test_rdbms_rdbmsviewfield_has_inherited():
    assert hasattr(rdbms_RdbmsViewField, "inherited")
    descriptor = None
    for klass in rdbms_RdbmsViewField.__mro__:
        if "inherited" in klass.__dict__:
            descriptor = klass.__dict__["inherited"]
            break
    assert isinstance(descriptor, property)


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
rdbms_RdbmsOperationMeta_strategy = st.builds(
    rdbms_RdbmsOperationMeta,
)
rdbms_RdbmsViewRecordValue_strategy = st.builds(
    rdbms_RdbmsViewRecordValue,
    value=
        safe_text
)
RdbmsFieldOperation_strategy = st.builds(
    RdbmsFieldOperation,
)
rdbms_RdbmsDeleteFieldOperation_strategy = st.builds(
    rdbms_RdbmsDeleteFieldOperation,
)
rdbms_RdbmsModifyFieldOperation_strategy = st.builds(
    rdbms_RdbmsModifyFieldOperation,
    changedForeignKeyToValueField=
        safe_text,
    nameChanged=
        safe_text,
    sizeChanged=
        safe_text,
    changedValueFieldToForeignKey=
        safe_text,
    mandatoryChanged=
        st.booleans(),
    typeChanged=
        st.booleans()
)
rdbms_RdbmsCreateFieldOperation_strategy = st.builds(
    rdbms_RdbmsCreateFieldOperation,
)
RdbmsTableOperation_strategy = st.builds(
    RdbmsTableOperation,
)
rdbms_RdbmsDeleteTableOperation_strategy = st.builds(
    rdbms_RdbmsDeleteTableOperation,
)
rdbms_RdbmsCreateTableOperation_strategy = st.builds(
    rdbms_RdbmsCreateTableOperation,
)
RdbmsExpression_strategy = st.builds(
    RdbmsExpression,
)
rdbms_RdbmsRelationExpression_strategy = st.builds(
    rdbms_RdbmsRelationExpression,
)
rdbms_RdbmsLabelExpression_strategy = st.builds(
    rdbms_RdbmsLabelExpression,
    text=
        safe_text
)
rdbms_RdbmsFeature_strategy = st.builds(
    rdbms_RdbmsFeature,
    name=
        safe_text
)
rdbms_RdbmsViewRecord_strategy = st.builds(
    rdbms_RdbmsViewRecord,
)
rdbms_RdbmsConfiguration_strategy = st.builds(
    rdbms_RdbmsConfiguration,
    dialect=
        safe_text
)
rdbms_RdbmsModel_strategy = st.builds(
    rdbms_RdbmsModel,
    version=
        safe_text
)
rdbms_RdbmsModifyTableOperation_strategy = st.builds(
    rdbms_RdbmsModifyTableOperation,
    nameChanged=
        safe_text
)
RdbmsViewTableField_strategy = st.builds(
    RdbmsViewTableField,
)
rdbms_RdbmsViewAliasField_strategy = st.builds(
    rdbms_RdbmsViewAliasField,
)
rdbms_RdbmsViewForeignIdentifierField_strategy = st.builds(
    rdbms_RdbmsViewForeignIdentifierField,
)
RdbmsViewField_strategy = st.builds(
    RdbmsViewField,
)
rdbms_RdbmsViewTableField_strategy = st.builds(
    rdbms_RdbmsViewTableField,
    foreign=
        st.booleans()
)
rdbms_RdbmsViewExpressionField_strategy = st.builds(
    rdbms_RdbmsViewExpressionField,
    expression=
        safe_text
)
RdbmsViewAliasField_strategy = st.builds(
    RdbmsViewAliasField,
)
rdbms_RdbmsViewValueField_strategy = st.builds(
    rdbms_RdbmsViewValueField,
)
rdbms_RdbmsViewIdentifierField_strategy = st.builds(
    rdbms_RdbmsViewIdentifierField,
)
rdbms_RdbmsViewRelation_strategy = st.builds(
    rdbms_RdbmsViewRelation,
    name=
        safe_text
)
RdbmsField_strategy = st.builds(
    RdbmsField,
)
rdbms_RdbmsValueField_strategy = st.builds(
    rdbms_RdbmsValueField,
    technical=
        st.booleans()
)
RdbmsTable_strategy = st.builds(
    RdbmsTable,
)
RdbmsIdentifierField_strategy = st.builds(
    RdbmsIdentifierField,
)
rdbms_RdbmsForeignKey_strategy = st.builds(
    rdbms_RdbmsForeignKey,
    inheritenceBased=
        st.booleans(),
    readOnly=
        st.booleans(),
    foreignKeySqlName=
        safe_text,
    deleteOnCascade=
        st.booleans(),
    deferred=
        st.booleans()
)
rdbms_RdbmsFieldType_strategy = st.builds(
    rdbms_RdbmsFieldType,
    rdbmsTypeName=
        safe_text,
    uuid=
        safe_text,
    size=
        st.integers(),
    name=
        safe_text,
    precision=
        st.integers(),
    scale=
        st.integers(),
    storageByte=
        st.integers(),
    description=
        safe_text
)
rdbms_RdbmsIdentifierField_strategy = st.builds(
    rdbms_RdbmsIdentifierField,
)
rdbms_RdbmsJunctionTable_strategy = st.builds(
    rdbms_RdbmsJunctionTable,
)
rdbms_RdbmsElement_strategy = st.builds(
    rdbms_RdbmsElement,
    shortName=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    sqlName=
        safe_text,
    originalPackage=
        safe_text,
    fullName=
        safe_text,
    uuid=
        safe_text,
    originalName=
        safe_text
)
RdbmsElement_strategy = st.builds(
    RdbmsElement,
)
rdbms_RdbmsTable_strategy = st.builds(
    rdbms_RdbmsTable,
)
rdbms_RdbmsUniqueConstraint_strategy = st.builds(
    rdbms_RdbmsUniqueConstraint,
)
rdbms_RdbmsExpression_strategy = st.builds(
    rdbms_RdbmsExpression,
    expression=
        safe_text
)
rdbms_RdbmsField_strategy = st.builds(
    rdbms_RdbmsField,
    size=
        st.integers(),
    rdbmsTypeName=
        safe_text,
    mandatory=
        st.booleans(),
    precision=
        st.integers(),
    storageByte=
        st.integers(),
    scale=
        st.integers()
)
rdbms_RdbmsTableAlias_strategy = st.builds(
    rdbms_RdbmsTableAlias,
)
rdbms_RdbmsFieldOperation_strategy = st.builds(
    rdbms_RdbmsFieldOperation,
    reviewRequired=
        st.booleans()
)
rdbms_RdbmsView_strategy = st.builds(
    rdbms_RdbmsView,
    originUuid=
        safe_text
)
rdbms_RdbmsTableOperation_strategy = st.builds(
    rdbms_RdbmsTableOperation,
)
rdbms_RdbmsIndex_strategy = st.builds(
    rdbms_RdbmsIndex,
    unique=
        st.booleans()
)
rdbms_RdbmsViewField_strategy = st.builds(
    rdbms_RdbmsViewField,
    inherited=
        st.booleans()
)

@given(instance=rdbms_RdbmsOperationMeta_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsoperationmeta_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsOperationMeta)

@given(instance=rdbms_RdbmsViewRecordValue_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewrecordvalue_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewRecordValue)



@given(instance=rdbms_RdbmsViewRecordValue_strategy)
def test_rdbms_rdbmsviewrecordvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=RdbmsFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbmsfieldoperation_instantiation(instance):
    assert isinstance(instance, RdbmsFieldOperation)

@given(instance=rdbms_RdbmsDeleteFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsdeletefieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsDeleteFieldOperation)

@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsmodifyfieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsModifyFieldOperation)



@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
def test_rdbms_rdbmsmodifyfieldoperation_changedForeignKeyToValueField_setter(instance):
    original = instance.changedForeignKeyToValueField
    instance.changedForeignKeyToValueField = original
    assert instance.changedForeignKeyToValueField == original



@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
def test_rdbms_rdbmsmodifyfieldoperation_nameChanged_setter(instance):
    original = instance.nameChanged
    instance.nameChanged = original
    assert instance.nameChanged == original



@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
def test_rdbms_rdbmsmodifyfieldoperation_sizeChanged_setter(instance):
    original = instance.sizeChanged
    instance.sizeChanged = original
    assert instance.sizeChanged == original



@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
def test_rdbms_rdbmsmodifyfieldoperation_changedValueFieldToForeignKey_setter(instance):
    original = instance.changedValueFieldToForeignKey
    instance.changedValueFieldToForeignKey = original
    assert instance.changedValueFieldToForeignKey == original



@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
def test_rdbms_rdbmsmodifyfieldoperation_mandatoryChanged_setter(instance):
    original = instance.mandatoryChanged
    instance.mandatoryChanged = original
    assert instance.mandatoryChanged == original



@given(instance=rdbms_RdbmsModifyFieldOperation_strategy)
def test_rdbms_rdbmsmodifyfieldoperation_typeChanged_setter(instance):
    original = instance.typeChanged
    instance.typeChanged = original
    assert instance.typeChanged == original

@given(instance=rdbms_RdbmsCreateFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmscreatefieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsCreateFieldOperation)

@given(instance=RdbmsTableOperation_strategy)
@settings(max_examples=50)
def test_rdbmstableoperation_instantiation(instance):
    assert isinstance(instance, RdbmsTableOperation)

@given(instance=rdbms_RdbmsDeleteTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsdeletetableoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsDeleteTableOperation)

@given(instance=rdbms_RdbmsCreateTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmscreatetableoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsCreateTableOperation)

@given(instance=RdbmsExpression_strategy)
@settings(max_examples=50)
def test_rdbmsexpression_instantiation(instance):
    assert isinstance(instance, RdbmsExpression)

@given(instance=rdbms_RdbmsRelationExpression_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsrelationexpression_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsRelationExpression)

@given(instance=rdbms_RdbmsLabelExpression_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmslabelexpression_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsLabelExpression)



@given(instance=rdbms_RdbmsLabelExpression_strategy)
def test_rdbms_rdbmslabelexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=rdbms_RdbmsFeature_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsfeature_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsFeature)



@given(instance=rdbms_RdbmsFeature_strategy)
def test_rdbms_rdbmsfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms_RdbmsViewRecord_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewrecord_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewRecord)

@given(instance=rdbms_RdbmsConfiguration_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsconfiguration_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsConfiguration)



@given(instance=rdbms_RdbmsConfiguration_strategy)
def test_rdbms_rdbmsconfiguration_dialect_setter(instance):
    original = instance.dialect
    instance.dialect = original
    assert instance.dialect == original

@given(instance=rdbms_RdbmsModel_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsmodel_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsModel)



@given(instance=rdbms_RdbmsModel_strategy)
def test_rdbms_rdbmsmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=rdbms_RdbmsModifyTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsmodifytableoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsModifyTableOperation)



@given(instance=rdbms_RdbmsModifyTableOperation_strategy)
def test_rdbms_rdbmsmodifytableoperation_nameChanged_setter(instance):
    original = instance.nameChanged
    instance.nameChanged = original
    assert instance.nameChanged == original

@given(instance=RdbmsViewTableField_strategy)
@settings(max_examples=50)
def test_rdbmsviewtablefield_instantiation(instance):
    assert isinstance(instance, RdbmsViewTableField)

@given(instance=rdbms_RdbmsViewAliasField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewaliasfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewAliasField)

@given(instance=rdbms_RdbmsViewForeignIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewforeignidentifierfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewForeignIdentifierField)

@given(instance=RdbmsViewField_strategy)
@settings(max_examples=50)
def test_rdbmsviewfield_instantiation(instance):
    assert isinstance(instance, RdbmsViewField)

@given(instance=rdbms_RdbmsViewTableField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewtablefield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewTableField)



@given(instance=rdbms_RdbmsViewTableField_strategy)
def test_rdbms_rdbmsviewtablefield_foreign_setter(instance):
    original = instance.foreign
    instance.foreign = original
    assert instance.foreign == original

@given(instance=rdbms_RdbmsViewExpressionField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewexpressionfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewExpressionField)



@given(instance=rdbms_RdbmsViewExpressionField_strategy)
def test_rdbms_rdbmsviewexpressionfield_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=RdbmsViewAliasField_strategy)
@settings(max_examples=50)
def test_rdbmsviewaliasfield_instantiation(instance):
    assert isinstance(instance, RdbmsViewAliasField)

@given(instance=rdbms_RdbmsViewValueField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewvaluefield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewValueField)

@given(instance=rdbms_RdbmsViewIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewidentifierfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewIdentifierField)

@given(instance=rdbms_RdbmsViewRelation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewrelation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewRelation)



@given(instance=rdbms_RdbmsViewRelation_strategy)
def test_rdbms_rdbmsviewrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RdbmsField_strategy)
@settings(max_examples=50)
def test_rdbmsfield_instantiation(instance):
    assert isinstance(instance, RdbmsField)

@given(instance=rdbms_RdbmsValueField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsvaluefield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsValueField)



@given(instance=rdbms_RdbmsValueField_strategy)
def test_rdbms_rdbmsvaluefield_technical_setter(instance):
    original = instance.technical
    instance.technical = original
    assert instance.technical == original

@given(instance=RdbmsTable_strategy)
@settings(max_examples=50)
def test_rdbmstable_instantiation(instance):
    assert isinstance(instance, RdbmsTable)

@given(instance=RdbmsIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbmsidentifierfield_instantiation(instance):
    assert isinstance(instance, RdbmsIdentifierField)

@given(instance=rdbms_RdbmsForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsforeignkey_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsForeignKey)



@given(instance=rdbms_RdbmsForeignKey_strategy)
def test_rdbms_rdbmsforeignkey_inheritenceBased_setter(instance):
    original = instance.inheritenceBased
    instance.inheritenceBased = original
    assert instance.inheritenceBased == original



@given(instance=rdbms_RdbmsForeignKey_strategy)
def test_rdbms_rdbmsforeignkey_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=rdbms_RdbmsForeignKey_strategy)
def test_rdbms_rdbmsforeignkey_foreignKeySqlName_setter(instance):
    original = instance.foreignKeySqlName
    instance.foreignKeySqlName = original
    assert instance.foreignKeySqlName == original



@given(instance=rdbms_RdbmsForeignKey_strategy)
def test_rdbms_rdbmsforeignkey_deleteOnCascade_setter(instance):
    original = instance.deleteOnCascade
    instance.deleteOnCascade = original
    assert instance.deleteOnCascade == original



@given(instance=rdbms_RdbmsForeignKey_strategy)
def test_rdbms_rdbmsforeignkey_deferred_setter(instance):
    original = instance.deferred
    instance.deferred = original
    assert instance.deferred == original

@given(instance=rdbms_RdbmsFieldType_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsfieldtype_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsFieldType)



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_rdbmsTypeName_setter(instance):
    original = instance.rdbmsTypeName
    instance.rdbmsTypeName = original
    assert instance.rdbmsTypeName == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_storageByte_setter(instance):
    original = instance.storageByte
    instance.storageByte = original
    assert instance.storageByte == original



@given(instance=rdbms_RdbmsFieldType_strategy)
def test_rdbms_rdbmsfieldtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=rdbms_RdbmsIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsidentifierfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsIdentifierField)

@given(instance=rdbms_RdbmsJunctionTable_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsjunctiontable_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsJunctionTable)

@given(instance=rdbms_RdbmsElement_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmselement_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsElement)



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_sqlName_setter(instance):
    original = instance.sqlName
    instance.sqlName = original
    assert instance.sqlName == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_originalPackage_setter(instance):
    original = instance.originalPackage
    instance.originalPackage = original
    assert instance.originalPackage == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=rdbms_RdbmsElement_strategy)
def test_rdbms_rdbmselement_originalName_setter(instance):
    original = instance.originalName
    instance.originalName = original
    assert instance.originalName == original

@given(instance=RdbmsElement_strategy)
@settings(max_examples=50)
def test_rdbmselement_instantiation(instance):
    assert isinstance(instance, RdbmsElement)

@given(instance=rdbms_RdbmsTable_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmstable_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsTable)

@given(instance=rdbms_RdbmsUniqueConstraint_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsuniqueconstraint_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsUniqueConstraint)

@given(instance=rdbms_RdbmsExpression_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsexpression_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsExpression)



@given(instance=rdbms_RdbmsExpression_strategy)
def test_rdbms_rdbmsexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=rdbms_RdbmsField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsField)



@given(instance=rdbms_RdbmsField_strategy)
def test_rdbms_rdbmsfield_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=rdbms_RdbmsField_strategy)
def test_rdbms_rdbmsfield_rdbmsTypeName_setter(instance):
    original = instance.rdbmsTypeName
    instance.rdbmsTypeName = original
    assert instance.rdbmsTypeName == original



@given(instance=rdbms_RdbmsField_strategy)
def test_rdbms_rdbmsfield_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=rdbms_RdbmsField_strategy)
def test_rdbms_rdbmsfield_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=rdbms_RdbmsField_strategy)
def test_rdbms_rdbmsfield_storageByte_setter(instance):
    original = instance.storageByte
    instance.storageByte = original
    assert instance.storageByte == original



@given(instance=rdbms_RdbmsField_strategy)
def test_rdbms_rdbmsfield_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=rdbms_RdbmsTableAlias_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmstablealias_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsTableAlias)

@given(instance=rdbms_RdbmsFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsfieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsFieldOperation)



@given(instance=rdbms_RdbmsFieldOperation_strategy)
def test_rdbms_rdbmsfieldoperation_reviewRequired_setter(instance):
    original = instance.reviewRequired
    instance.reviewRequired = original
    assert instance.reviewRequired == original

@given(instance=rdbms_RdbmsView_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsview_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsView)



@given(instance=rdbms_RdbmsView_strategy)
def test_rdbms_rdbmsview_originUuid_setter(instance):
    original = instance.originUuid
    instance.originUuid = original
    assert instance.originUuid == original

@given(instance=rdbms_RdbmsTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmstableoperation_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsTableOperation)

@given(instance=rdbms_RdbmsIndex_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsindex_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsIndex)



@given(instance=rdbms_RdbmsIndex_strategy)
def test_rdbms_rdbmsindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=rdbms_RdbmsViewField_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsviewfield_instantiation(instance):
    assert isinstance(instance, rdbms_RdbmsViewField)



@given(instance=rdbms_RdbmsViewField_strategy)
def test_rdbms_rdbmsviewfield_inherited_setter(instance):
    original = instance.inherited
    instance.inherited = original
    assert instance.inherited == original
