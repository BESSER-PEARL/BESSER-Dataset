import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdbms::RdbmsOperationMeta,
    rdbms::RdbmsViewRecordValue,
    RdbmsFieldOperation,
    rdbms::RdbmsDeleteFieldOperation,
    rdbms::RdbmsModifyFieldOperation,
    rdbms::RdbmsCreateFieldOperation,
    RdbmsTableOperation,
    rdbms::RdbmsDeleteTableOperation,
    rdbms::RdbmsCreateTableOperation,
    RdbmsExpression,
    rdbms::RdbmsRelationExpression,
    rdbms::RdbmsLabelExpression,
    rdbms::RdbmsFeature,
    rdbms::RdbmsViewRecord,
    rdbms::RdbmsConfiguration,
    rdbms::RdbmsModel,
    rdbms::RdbmsModifyTableOperation,
    RdbmsViewTableField,
    rdbms::RdbmsViewForeignIdentifierField,
    rdbms::RdbmsViewAliasField,
    RdbmsViewField,
    rdbms::RdbmsViewTableField,
    rdbms::RdbmsViewExpressionField,
    RdbmsViewAliasField,
    rdbms::RdbmsViewValueField,
    rdbms::RdbmsViewIdentifierField,
    rdbms::RdbmsViewRelation,
    RdbmsField,
    rdbms::RdbmsValueField,
    RdbmsTable,
    RdbmsIdentifierField,
    rdbms::RdbmsForeignKey,
    rdbms::RdbmsFieldType,
    rdbms::RdbmsIdentifierField,
    rdbms::RdbmsJunctionTable,
    rdbms::RdbmsElement,
    RdbmsElement,
    rdbms::RdbmsField,
    rdbms::RdbmsIndex,
    rdbms::RdbmsViewField,
    rdbms::RdbmsUniqueConstraint,
    rdbms::RdbmsFieldOperation,
    rdbms::RdbmsTableAlias,
    rdbms::RdbmsTableOperation,
    rdbms::RdbmsExpression,
    rdbms::RdbmsView,
    rdbms::RdbmsTable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms::rdbmsoperationmeta_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsOperationMeta)


def test_rdbms::rdbmsoperationmeta_constructor_exists():
    assert callable(rdbms::RdbmsOperationMeta.__init__)


def test_rdbms::rdbmsoperationmeta_constructor_args():
    sig = inspect.signature(rdbms::RdbmsOperationMeta.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsviewrecordvalue_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewRecordValue)


def test_rdbms::rdbmsviewrecordvalue_constructor_exists():
    assert callable(rdbms::RdbmsViewRecordValue.__init__)


def test_rdbms::rdbmsviewrecordvalue_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewRecordValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rdbms::rdbmsviewrecordvalue_has_value():
    assert hasattr(rdbms::RdbmsViewRecordValue, "value")
    descriptor = None
    for klass in rdbms::RdbmsViewRecordValue.__mro__:
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



def test_rdbms::rdbmsdeletefieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsDeleteFieldOperation)


def test_rdbms::rdbmsdeletefieldoperation_constructor_exists():
    assert callable(rdbms::RdbmsDeleteFieldOperation.__init__)


def test_rdbms::rdbmsdeletefieldoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsDeleteFieldOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsmodifyfieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsModifyFieldOperation)


def test_rdbms::rdbmsmodifyfieldoperation_constructor_exists():
    assert callable(rdbms::RdbmsModifyFieldOperation.__init__)


def test_rdbms::rdbmsmodifyfieldoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsModifyFieldOperation.__init__)
    params = list(sig.parameters.keys())
    assert "nameChanged" in params, "Missing parameter 'nameChanged'"
    assert "mandatoryChanged" in params, "Missing parameter 'mandatoryChanged'"
    assert "typeChanged" in params, "Missing parameter 'typeChanged'"
    assert "changedValueFieldToForeignKey" in params, "Missing parameter 'changedValueFieldToForeignKey'"
    assert "sizeChanged" in params, "Missing parameter 'sizeChanged'"
    assert "changedForeignKeyToValueField" in params, "Missing parameter 'changedForeignKeyToValueField'"

def test_rdbms::rdbmsmodifyfieldoperation_has_nameChanged():
    assert hasattr(rdbms::RdbmsModifyFieldOperation, "nameChanged")
    descriptor = None
    for klass in rdbms::RdbmsModifyFieldOperation.__mro__:
        if "nameChanged" in klass.__dict__:
            descriptor = klass.__dict__["nameChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsmodifyfieldoperation_has_mandatoryChanged():
    assert hasattr(rdbms::RdbmsModifyFieldOperation, "mandatoryChanged")
    descriptor = None
    for klass in rdbms::RdbmsModifyFieldOperation.__mro__:
        if "mandatoryChanged" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsmodifyfieldoperation_has_typeChanged():
    assert hasattr(rdbms::RdbmsModifyFieldOperation, "typeChanged")
    descriptor = None
    for klass in rdbms::RdbmsModifyFieldOperation.__mro__:
        if "typeChanged" in klass.__dict__:
            descriptor = klass.__dict__["typeChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsmodifyfieldoperation_has_changedValueFieldToForeignKey():
    assert hasattr(rdbms::RdbmsModifyFieldOperation, "changedValueFieldToForeignKey")
    descriptor = None
    for klass in rdbms::RdbmsModifyFieldOperation.__mro__:
        if "changedValueFieldToForeignKey" in klass.__dict__:
            descriptor = klass.__dict__["changedValueFieldToForeignKey"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsmodifyfieldoperation_has_sizeChanged():
    assert hasattr(rdbms::RdbmsModifyFieldOperation, "sizeChanged")
    descriptor = None
    for klass in rdbms::RdbmsModifyFieldOperation.__mro__:
        if "sizeChanged" in klass.__dict__:
            descriptor = klass.__dict__["sizeChanged"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsmodifyfieldoperation_has_changedForeignKeyToValueField():
    assert hasattr(rdbms::RdbmsModifyFieldOperation, "changedForeignKeyToValueField")
    descriptor = None
    for klass in rdbms::RdbmsModifyFieldOperation.__mro__:
        if "changedForeignKeyToValueField" in klass.__dict__:
            descriptor = klass.__dict__["changedForeignKeyToValueField"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmscreatefieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsCreateFieldOperation)


def test_rdbms::rdbmscreatefieldoperation_constructor_exists():
    assert callable(rdbms::RdbmsCreateFieldOperation.__init__)


def test_rdbms::rdbmscreatefieldoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsCreateFieldOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbmstableoperation_is_not_abstract():
    assert not inspect.isabstract(RdbmsTableOperation)


def test_rdbmstableoperation_constructor_exists():
    assert callable(RdbmsTableOperation.__init__)


def test_rdbmstableoperation_constructor_args():
    sig = inspect.signature(RdbmsTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsdeletetableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsDeleteTableOperation)


def test_rdbms::rdbmsdeletetableoperation_constructor_exists():
    assert callable(rdbms::RdbmsDeleteTableOperation.__init__)


def test_rdbms::rdbmsdeletetableoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsDeleteTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmscreatetableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsCreateTableOperation)


def test_rdbms::rdbmscreatetableoperation_constructor_exists():
    assert callable(rdbms::RdbmsCreateTableOperation.__init__)


def test_rdbms::rdbmscreatetableoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsCreateTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsexpression_is_not_abstract():
    assert not inspect.isabstract(RdbmsExpression)


def test_rdbmsexpression_constructor_exists():
    assert callable(RdbmsExpression.__init__)


def test_rdbmsexpression_constructor_args():
    sig = inspect.signature(RdbmsExpression.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsrelationexpression_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsRelationExpression)


def test_rdbms::rdbmsrelationexpression_constructor_exists():
    assert callable(rdbms::RdbmsRelationExpression.__init__)


def test_rdbms::rdbmsrelationexpression_constructor_args():
    sig = inspect.signature(rdbms::RdbmsRelationExpression.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmslabelexpression_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsLabelExpression)


def test_rdbms::rdbmslabelexpression_constructor_exists():
    assert callable(rdbms::RdbmsLabelExpression.__init__)


def test_rdbms::rdbmslabelexpression_constructor_args():
    sig = inspect.signature(rdbms::RdbmsLabelExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_rdbms::rdbmslabelexpression_has_text():
    assert hasattr(rdbms::RdbmsLabelExpression, "text")
    descriptor = None
    for klass in rdbms::RdbmsLabelExpression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsfeature_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsFeature)


def test_rdbms::rdbmsfeature_constructor_exists():
    assert callable(rdbms::RdbmsFeature.__init__)


def test_rdbms::rdbmsfeature_constructor_args():
    sig = inspect.signature(rdbms::RdbmsFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::rdbmsfeature_has_name():
    assert hasattr(rdbms::RdbmsFeature, "name")
    descriptor = None
    for klass in rdbms::RdbmsFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsviewrecord_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewRecord)


def test_rdbms::rdbmsviewrecord_constructor_exists():
    assert callable(rdbms::RdbmsViewRecord.__init__)


def test_rdbms::rdbmsviewrecord_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewRecord.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsconfiguration_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsConfiguration)


def test_rdbms::rdbmsconfiguration_constructor_exists():
    assert callable(rdbms::RdbmsConfiguration.__init__)


def test_rdbms::rdbmsconfiguration_constructor_args():
    sig = inspect.signature(rdbms::RdbmsConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "dialect" in params, "Missing parameter 'dialect'"

def test_rdbms::rdbmsconfiguration_has_dialect():
    assert hasattr(rdbms::RdbmsConfiguration, "dialect")
    descriptor = None
    for klass in rdbms::RdbmsConfiguration.__mro__:
        if "dialect" in klass.__dict__:
            descriptor = klass.__dict__["dialect"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsModel)


def test_rdbms::rdbmsmodel_constructor_exists():
    assert callable(rdbms::RdbmsModel.__init__)


def test_rdbms::rdbmsmodel_constructor_args():
    sig = inspect.signature(rdbms::RdbmsModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_rdbms::rdbmsmodel_has_version():
    assert hasattr(rdbms::RdbmsModel, "version")
    descriptor = None
    for klass in rdbms::RdbmsModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsmodifytableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsModifyTableOperation)


def test_rdbms::rdbmsmodifytableoperation_constructor_exists():
    assert callable(rdbms::RdbmsModifyTableOperation.__init__)


def test_rdbms::rdbmsmodifytableoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsModifyTableOperation.__init__)
    params = list(sig.parameters.keys())
    assert "nameChanged" in params, "Missing parameter 'nameChanged'"

def test_rdbms::rdbmsmodifytableoperation_has_nameChanged():
    assert hasattr(rdbms::RdbmsModifyTableOperation, "nameChanged")
    descriptor = None
    for klass in rdbms::RdbmsModifyTableOperation.__mro__:
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



def test_rdbms::rdbmsviewforeignidentifierfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewForeignIdentifierField)


def test_rdbms::rdbmsviewforeignidentifierfield_constructor_exists():
    assert callable(rdbms::RdbmsViewForeignIdentifierField.__init__)


def test_rdbms::rdbmsviewforeignidentifierfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewForeignIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsviewaliasfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewAliasField)


def test_rdbms::rdbmsviewaliasfield_constructor_exists():
    assert callable(rdbms::RdbmsViewAliasField.__init__)


def test_rdbms::rdbmsviewaliasfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewAliasField.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsviewfield_is_not_abstract():
    assert not inspect.isabstract(RdbmsViewField)


def test_rdbmsviewfield_constructor_exists():
    assert callable(RdbmsViewField.__init__)


def test_rdbmsviewfield_constructor_args():
    sig = inspect.signature(RdbmsViewField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsviewtablefield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewTableField)


def test_rdbms::rdbmsviewtablefield_constructor_exists():
    assert callable(rdbms::RdbmsViewTableField.__init__)


def test_rdbms::rdbmsviewtablefield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewTableField.__init__)
    params = list(sig.parameters.keys())
    assert "foreign" in params, "Missing parameter 'foreign'"

def test_rdbms::rdbmsviewtablefield_has_foreign():
    assert hasattr(rdbms::RdbmsViewTableField, "foreign")
    descriptor = None
    for klass in rdbms::RdbmsViewTableField.__mro__:
        if "foreign" in klass.__dict__:
            descriptor = klass.__dict__["foreign"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsviewexpressionfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewExpressionField)


def test_rdbms::rdbmsviewexpressionfield_constructor_exists():
    assert callable(rdbms::RdbmsViewExpressionField.__init__)


def test_rdbms::rdbmsviewexpressionfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewExpressionField.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_rdbms::rdbmsviewexpressionfield_has_expression():
    assert hasattr(rdbms::RdbmsViewExpressionField, "expression")
    descriptor = None
    for klass in rdbms::RdbmsViewExpressionField.__mro__:
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



def test_rdbms::rdbmsviewvaluefield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewValueField)


def test_rdbms::rdbmsviewvaluefield_constructor_exists():
    assert callable(rdbms::RdbmsViewValueField.__init__)


def test_rdbms::rdbmsviewvaluefield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewValueField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsviewidentifierfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewIdentifierField)


def test_rdbms::rdbmsviewidentifierfield_constructor_exists():
    assert callable(rdbms::RdbmsViewIdentifierField.__init__)


def test_rdbms::rdbmsviewidentifierfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsviewrelation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewRelation)


def test_rdbms::rdbmsviewrelation_constructor_exists():
    assert callable(rdbms::RdbmsViewRelation.__init__)


def test_rdbms::rdbmsviewrelation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewRelation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::rdbmsviewrelation_has_name():
    assert hasattr(rdbms::RdbmsViewRelation, "name")
    descriptor = None
    for klass in rdbms::RdbmsViewRelation.__mro__:
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



def test_rdbms::rdbmsvaluefield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsValueField)


def test_rdbms::rdbmsvaluefield_constructor_exists():
    assert callable(rdbms::RdbmsValueField.__init__)


def test_rdbms::rdbmsvaluefield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsValueField.__init__)
    params = list(sig.parameters.keys())
    assert "technical" in params, "Missing parameter 'technical'"

def test_rdbms::rdbmsvaluefield_has_technical():
    assert hasattr(rdbms::RdbmsValueField, "technical")
    descriptor = None
    for klass in rdbms::RdbmsValueField.__mro__:
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



def test_rdbms::rdbmsforeignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsForeignKey)


def test_rdbms::rdbmsforeignkey_constructor_exists():
    assert callable(rdbms::RdbmsForeignKey.__init__)


def test_rdbms::rdbmsforeignkey_constructor_args():
    sig = inspect.signature(rdbms::RdbmsForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "deleteOnCascade" in params, "Missing parameter 'deleteOnCascade'"
    assert "deferred" in params, "Missing parameter 'deferred'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "foreignKeySqlName" in params, "Missing parameter 'foreignKeySqlName'"
    assert "inheritenceBased" in params, "Missing parameter 'inheritenceBased'"

def test_rdbms::rdbmsforeignkey_has_deleteOnCascade():
    assert hasattr(rdbms::RdbmsForeignKey, "deleteOnCascade")
    descriptor = None
    for klass in rdbms::RdbmsForeignKey.__mro__:
        if "deleteOnCascade" in klass.__dict__:
            descriptor = klass.__dict__["deleteOnCascade"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsforeignkey_has_deferred():
    assert hasattr(rdbms::RdbmsForeignKey, "deferred")
    descriptor = None
    for klass in rdbms::RdbmsForeignKey.__mro__:
        if "deferred" in klass.__dict__:
            descriptor = klass.__dict__["deferred"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsforeignkey_has_readOnly():
    assert hasattr(rdbms::RdbmsForeignKey, "readOnly")
    descriptor = None
    for klass in rdbms::RdbmsForeignKey.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsforeignkey_has_foreignKeySqlName():
    assert hasattr(rdbms::RdbmsForeignKey, "foreignKeySqlName")
    descriptor = None
    for klass in rdbms::RdbmsForeignKey.__mro__:
        if "foreignKeySqlName" in klass.__dict__:
            descriptor = klass.__dict__["foreignKeySqlName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsforeignkey_has_inheritenceBased():
    assert hasattr(rdbms::RdbmsForeignKey, "inheritenceBased")
    descriptor = None
    for klass in rdbms::RdbmsForeignKey.__mro__:
        if "inheritenceBased" in klass.__dict__:
            descriptor = klass.__dict__["inheritenceBased"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsfieldtype_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsFieldType)


def test_rdbms::rdbmsfieldtype_constructor_exists():
    assert callable(rdbms::RdbmsFieldType.__init__)


def test_rdbms::rdbmsfieldtype_constructor_args():
    sig = inspect.signature(rdbms::RdbmsFieldType.__init__)
    params = list(sig.parameters.keys())
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "size" in params, "Missing parameter 'size'"
    assert "description" in params, "Missing parameter 'description'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "rdbmsTypeName" in params, "Missing parameter 'rdbmsTypeName'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "name" in params, "Missing parameter 'name'"
    assert "storageByte" in params, "Missing parameter 'storageByte'"

def test_rdbms::rdbmsfieldtype_has_uuid():
    assert hasattr(rdbms::RdbmsFieldType, "uuid")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_size():
    assert hasattr(rdbms::RdbmsFieldType, "size")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_description():
    assert hasattr(rdbms::RdbmsFieldType, "description")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_precision():
    assert hasattr(rdbms::RdbmsFieldType, "precision")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_rdbmsTypeName():
    assert hasattr(rdbms::RdbmsFieldType, "rdbmsTypeName")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "rdbmsTypeName" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsTypeName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_scale():
    assert hasattr(rdbms::RdbmsFieldType, "scale")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_name():
    assert hasattr(rdbms::RdbmsFieldType, "name")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfieldtype_has_storageByte():
    assert hasattr(rdbms::RdbmsFieldType, "storageByte")
    descriptor = None
    for klass in rdbms::RdbmsFieldType.__mro__:
        if "storageByte" in klass.__dict__:
            descriptor = klass.__dict__["storageByte"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsidentifierfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsIdentifierField)


def test_rdbms::rdbmsidentifierfield_constructor_exists():
    assert callable(rdbms::RdbmsIdentifierField.__init__)


def test_rdbms::rdbmsidentifierfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsIdentifierField.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsjunctiontable_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsJunctionTable)


def test_rdbms::rdbmsjunctiontable_constructor_exists():
    assert callable(rdbms::RdbmsJunctionTable.__init__)


def test_rdbms::rdbmsjunctiontable_constructor_args():
    sig = inspect.signature(rdbms::RdbmsJunctionTable.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmselement_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsElement)


def test_rdbms::rdbmselement_constructor_exists():
    assert callable(rdbms::RdbmsElement.__init__)


def test_rdbms::rdbmselement_constructor_args():
    sig = inspect.signature(rdbms::RdbmsElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "originalName" in params, "Missing parameter 'originalName'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "originalPackage" in params, "Missing parameter 'originalPackage'"
    assert "sqlName" in params, "Missing parameter 'sqlName'"
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "uuid" in params, "Missing parameter 'uuid'"

def test_rdbms::rdbmselement_has_description():
    assert hasattr(rdbms::RdbmsElement, "description")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_originalName():
    assert hasattr(rdbms::RdbmsElement, "originalName")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "originalName" in klass.__dict__:
            descriptor = klass.__dict__["originalName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_fullName():
    assert hasattr(rdbms::RdbmsElement, "fullName")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_originalPackage():
    assert hasattr(rdbms::RdbmsElement, "originalPackage")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "originalPackage" in klass.__dict__:
            descriptor = klass.__dict__["originalPackage"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_sqlName():
    assert hasattr(rdbms::RdbmsElement, "sqlName")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "sqlName" in klass.__dict__:
            descriptor = klass.__dict__["sqlName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_shortName():
    assert hasattr(rdbms::RdbmsElement, "shortName")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_name():
    assert hasattr(rdbms::RdbmsElement, "name")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmselement_has_uuid():
    assert hasattr(rdbms::RdbmsElement, "uuid")
    descriptor = None
    for klass in rdbms::RdbmsElement.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)



def test_rdbmselement_is_not_abstract():
    assert not inspect.isabstract(RdbmsElement)


def test_rdbmselement_constructor_exists():
    assert callable(RdbmsElement.__init__)


def test_rdbmselement_constructor_args():
    sig = inspect.signature(RdbmsElement.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsField)


def test_rdbms::rdbmsfield_constructor_exists():
    assert callable(rdbms::RdbmsField.__init__)


def test_rdbms::rdbmsfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsField.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "storageByte" in params, "Missing parameter 'storageByte'"
    assert "rdbmsTypeName" in params, "Missing parameter 'rdbmsTypeName'"
    assert "size" in params, "Missing parameter 'size'"

def test_rdbms::rdbmsfield_has_mandatory():
    assert hasattr(rdbms::RdbmsField, "mandatory")
    descriptor = None
    for klass in rdbms::RdbmsField.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfield_has_precision():
    assert hasattr(rdbms::RdbmsField, "precision")
    descriptor = None
    for klass in rdbms::RdbmsField.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfield_has_scale():
    assert hasattr(rdbms::RdbmsField, "scale")
    descriptor = None
    for klass in rdbms::RdbmsField.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfield_has_storageByte():
    assert hasattr(rdbms::RdbmsField, "storageByte")
    descriptor = None
    for klass in rdbms::RdbmsField.__mro__:
        if "storageByte" in klass.__dict__:
            descriptor = klass.__dict__["storageByte"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfield_has_rdbmsTypeName():
    assert hasattr(rdbms::RdbmsField, "rdbmsTypeName")
    descriptor = None
    for klass in rdbms::RdbmsField.__mro__:
        if "rdbmsTypeName" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsTypeName"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::rdbmsfield_has_size():
    assert hasattr(rdbms::RdbmsField, "size")
    descriptor = None
    for klass in rdbms::RdbmsField.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsindex_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsIndex)


def test_rdbms::rdbmsindex_constructor_exists():
    assert callable(rdbms::RdbmsIndex.__init__)


def test_rdbms::rdbmsindex_constructor_args():
    sig = inspect.signature(rdbms::RdbmsIndex.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_rdbms::rdbmsindex_has_unique():
    assert hasattr(rdbms::RdbmsIndex, "unique")
    descriptor = None
    for klass in rdbms::RdbmsIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsviewfield_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsViewField)


def test_rdbms::rdbmsviewfield_constructor_exists():
    assert callable(rdbms::RdbmsViewField.__init__)


def test_rdbms::rdbmsviewfield_constructor_args():
    sig = inspect.signature(rdbms::RdbmsViewField.__init__)
    params = list(sig.parameters.keys())
    assert "inherited" in params, "Missing parameter 'inherited'"

def test_rdbms::rdbmsviewfield_has_inherited():
    assert hasattr(rdbms::RdbmsViewField, "inherited")
    descriptor = None
    for klass in rdbms::RdbmsViewField.__mro__:
        if "inherited" in klass.__dict__:
            descriptor = klass.__dict__["inherited"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsuniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsUniqueConstraint)


def test_rdbms::rdbmsuniqueconstraint_constructor_exists():
    assert callable(rdbms::RdbmsUniqueConstraint.__init__)


def test_rdbms::rdbmsuniqueconstraint_constructor_args():
    sig = inspect.signature(rdbms::RdbmsUniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsfieldoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsFieldOperation)


def test_rdbms::rdbmsfieldoperation_constructor_exists():
    assert callable(rdbms::RdbmsFieldOperation.__init__)


def test_rdbms::rdbmsfieldoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsFieldOperation.__init__)
    params = list(sig.parameters.keys())
    assert "reviewRequired" in params, "Missing parameter 'reviewRequired'"

def test_rdbms::rdbmsfieldoperation_has_reviewRequired():
    assert hasattr(rdbms::RdbmsFieldOperation, "reviewRequired")
    descriptor = None
    for klass in rdbms::RdbmsFieldOperation.__mro__:
        if "reviewRequired" in klass.__dict__:
            descriptor = klass.__dict__["reviewRequired"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmstablealias_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsTableAlias)


def test_rdbms::rdbmstablealias_constructor_exists():
    assert callable(rdbms::RdbmsTableAlias.__init__)


def test_rdbms::rdbmstablealias_constructor_args():
    sig = inspect.signature(rdbms::RdbmsTableAlias.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmstableoperation_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsTableOperation)


def test_rdbms::rdbmstableoperation_constructor_exists():
    assert callable(rdbms::RdbmsTableOperation.__init__)


def test_rdbms::rdbmstableoperation_constructor_args():
    sig = inspect.signature(rdbms::RdbmsTableOperation.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::rdbmsexpression_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsExpression)


def test_rdbms::rdbmsexpression_constructor_exists():
    assert callable(rdbms::RdbmsExpression.__init__)


def test_rdbms::rdbmsexpression_constructor_args():
    sig = inspect.signature(rdbms::RdbmsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_rdbms::rdbmsexpression_has_expression():
    assert hasattr(rdbms::RdbmsExpression, "expression")
    descriptor = None
    for klass in rdbms::RdbmsExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsview_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsView)


def test_rdbms::rdbmsview_constructor_exists():
    assert callable(rdbms::RdbmsView.__init__)


def test_rdbms::rdbmsview_constructor_args():
    sig = inspect.signature(rdbms::RdbmsView.__init__)
    params = list(sig.parameters.keys())
    assert "originUuid" in params, "Missing parameter 'originUuid'"

def test_rdbms::rdbmsview_has_originUuid():
    assert hasattr(rdbms::RdbmsView, "originUuid")
    descriptor = None
    for klass in rdbms::RdbmsView.__mro__:
        if "originUuid" in klass.__dict__:
            descriptor = klass.__dict__["originUuid"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmstable_is_not_abstract():
    assert not inspect.isabstract(rdbms::RdbmsTable)


def test_rdbms::rdbmstable_constructor_exists():
    assert callable(rdbms::RdbmsTable.__init__)


def test_rdbms::rdbmstable_constructor_args():
    sig = inspect.signature(rdbms::RdbmsTable.__init__)
    params = list(sig.parameters.keys())


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
rdbms::RdbmsOperationMeta_strategy = st.builds(
    rdbms::RdbmsOperationMeta,
)
rdbms::RdbmsViewRecordValue_strategy = st.builds(
    rdbms::RdbmsViewRecordValue,
    value=
        safe_text
)
RdbmsFieldOperation_strategy = st.builds(
    RdbmsFieldOperation,
)
rdbms::RdbmsDeleteFieldOperation_strategy = st.builds(
    rdbms::RdbmsDeleteFieldOperation,
)
rdbms::RdbmsModifyFieldOperation_strategy = st.builds(
    rdbms::RdbmsModifyFieldOperation,
    nameChanged=
        safe_text,
    mandatoryChanged=
        st.booleans(),
    typeChanged=
        st.booleans(),
    changedValueFieldToForeignKey=
        safe_text,
    sizeChanged=
        safe_text,
    changedForeignKeyToValueField=
        safe_text
)
rdbms::RdbmsCreateFieldOperation_strategy = st.builds(
    rdbms::RdbmsCreateFieldOperation,
)
RdbmsTableOperation_strategy = st.builds(
    RdbmsTableOperation,
)
rdbms::RdbmsDeleteTableOperation_strategy = st.builds(
    rdbms::RdbmsDeleteTableOperation,
)
rdbms::RdbmsCreateTableOperation_strategy = st.builds(
    rdbms::RdbmsCreateTableOperation,
)
RdbmsExpression_strategy = st.builds(
    RdbmsExpression,
)
rdbms::RdbmsRelationExpression_strategy = st.builds(
    rdbms::RdbmsRelationExpression,
)
rdbms::RdbmsLabelExpression_strategy = st.builds(
    rdbms::RdbmsLabelExpression,
    text=
        safe_text
)
rdbms::RdbmsFeature_strategy = st.builds(
    rdbms::RdbmsFeature,
    name=
        safe_text
)
rdbms::RdbmsViewRecord_strategy = st.builds(
    rdbms::RdbmsViewRecord,
)
rdbms::RdbmsConfiguration_strategy = st.builds(
    rdbms::RdbmsConfiguration,
    dialect=
        safe_text
)
rdbms::RdbmsModel_strategy = st.builds(
    rdbms::RdbmsModel,
    version=
        safe_text
)
rdbms::RdbmsModifyTableOperation_strategy = st.builds(
    rdbms::RdbmsModifyTableOperation,
    nameChanged=
        safe_text
)
RdbmsViewTableField_strategy = st.builds(
    RdbmsViewTableField,
)
rdbms::RdbmsViewForeignIdentifierField_strategy = st.builds(
    rdbms::RdbmsViewForeignIdentifierField,
)
rdbms::RdbmsViewAliasField_strategy = st.builds(
    rdbms::RdbmsViewAliasField,
)
RdbmsViewField_strategy = st.builds(
    RdbmsViewField,
)
rdbms::RdbmsViewTableField_strategy = st.builds(
    rdbms::RdbmsViewTableField,
    foreign=
        st.booleans()
)
rdbms::RdbmsViewExpressionField_strategy = st.builds(
    rdbms::RdbmsViewExpressionField,
    expression=
        safe_text
)
RdbmsViewAliasField_strategy = st.builds(
    RdbmsViewAliasField,
)
rdbms::RdbmsViewValueField_strategy = st.builds(
    rdbms::RdbmsViewValueField,
)
rdbms::RdbmsViewIdentifierField_strategy = st.builds(
    rdbms::RdbmsViewIdentifierField,
)
rdbms::RdbmsViewRelation_strategy = st.builds(
    rdbms::RdbmsViewRelation,
    name=
        safe_text
)
RdbmsField_strategy = st.builds(
    RdbmsField,
)
rdbms::RdbmsValueField_strategy = st.builds(
    rdbms::RdbmsValueField,
    technical=
        st.booleans()
)
RdbmsTable_strategy = st.builds(
    RdbmsTable,
)
RdbmsIdentifierField_strategy = st.builds(
    RdbmsIdentifierField,
)
rdbms::RdbmsForeignKey_strategy = st.builds(
    rdbms::RdbmsForeignKey,
    deleteOnCascade=
        st.booleans(),
    deferred=
        st.booleans(),
    readOnly=
        st.booleans(),
    foreignKeySqlName=
        safe_text,
    inheritenceBased=
        st.booleans()
)
rdbms::RdbmsFieldType_strategy = st.builds(
    rdbms::RdbmsFieldType,
    uuid=
        safe_text,
    size=
        st.integers(),
    description=
        safe_text,
    precision=
        st.integers(),
    rdbmsTypeName=
        safe_text,
    scale=
        st.integers(),
    name=
        safe_text,
    storageByte=
        st.integers()
)
rdbms::RdbmsIdentifierField_strategy = st.builds(
    rdbms::RdbmsIdentifierField,
)
rdbms::RdbmsJunctionTable_strategy = st.builds(
    rdbms::RdbmsJunctionTable,
)
rdbms::RdbmsElement_strategy = st.builds(
    rdbms::RdbmsElement,
    description=
        safe_text,
    originalName=
        safe_text,
    fullName=
        safe_text,
    originalPackage=
        safe_text,
    sqlName=
        safe_text,
    shortName=
        safe_text,
    name=
        safe_text,
    uuid=
        safe_text
)
RdbmsElement_strategy = st.builds(
    RdbmsElement,
)
rdbms::RdbmsField_strategy = st.builds(
    rdbms::RdbmsField,
    mandatory=
        st.booleans(),
    precision=
        st.integers(),
    scale=
        st.integers(),
    storageByte=
        st.integers(),
    rdbmsTypeName=
        safe_text,
    size=
        st.integers()
)
rdbms::RdbmsIndex_strategy = st.builds(
    rdbms::RdbmsIndex,
    unique=
        st.booleans()
)
rdbms::RdbmsViewField_strategy = st.builds(
    rdbms::RdbmsViewField,
    inherited=
        st.booleans()
)
rdbms::RdbmsUniqueConstraint_strategy = st.builds(
    rdbms::RdbmsUniqueConstraint,
)
rdbms::RdbmsFieldOperation_strategy = st.builds(
    rdbms::RdbmsFieldOperation,
    reviewRequired=
        st.booleans()
)
rdbms::RdbmsTableAlias_strategy = st.builds(
    rdbms::RdbmsTableAlias,
)
rdbms::RdbmsTableOperation_strategy = st.builds(
    rdbms::RdbmsTableOperation,
)
rdbms::RdbmsExpression_strategy = st.builds(
    rdbms::RdbmsExpression,
    expression=
        safe_text
)
rdbms::RdbmsView_strategy = st.builds(
    rdbms::RdbmsView,
    originUuid=
        safe_text
)
rdbms::RdbmsTable_strategy = st.builds(
    rdbms::RdbmsTable,
)

@given(instance=rdbms::RdbmsOperationMeta_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsoperationmeta_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsOperationMeta)

@given(instance=rdbms::RdbmsViewRecordValue_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewrecordvalue_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewRecordValue)

@given(instance=rdbms::RdbmsViewRecordValue_strategy)
def test_rdbms::rdbmsviewrecordvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=rdbms::RdbmsViewRecordValue_strategy)
def test_rdbms::rdbmsviewrecordvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=RdbmsFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbmsfieldoperation_instantiation(instance):
    assert isinstance(instance, RdbmsFieldOperation)

@given(instance=rdbms::RdbmsDeleteFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsdeletefieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsDeleteFieldOperation)

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsmodifyfieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsModifyFieldOperation)

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_nameChanged_type(instance):
    assert isinstance(instance.nameChanged, str)


@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_nameChanged_setter(instance):
    original = instance.nameChanged
    instance.nameChanged = original
    assert instance.nameChanged == original

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_mandatoryChanged_type(instance):
    assert isinstance(instance.mandatoryChanged, bool)


@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_mandatoryChanged_setter(instance):
    original = instance.mandatoryChanged
    instance.mandatoryChanged = original
    assert instance.mandatoryChanged == original

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_typeChanged_type(instance):
    assert isinstance(instance.typeChanged, bool)


@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_typeChanged_setter(instance):
    original = instance.typeChanged
    instance.typeChanged = original
    assert instance.typeChanged == original

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_changedValueFieldToForeignKey_type(instance):
    assert isinstance(instance.changedValueFieldToForeignKey, str)


@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_changedValueFieldToForeignKey_setter(instance):
    original = instance.changedValueFieldToForeignKey
    instance.changedValueFieldToForeignKey = original
    assert instance.changedValueFieldToForeignKey == original

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_sizeChanged_type(instance):
    assert isinstance(instance.sizeChanged, str)


@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_sizeChanged_setter(instance):
    original = instance.sizeChanged
    instance.sizeChanged = original
    assert instance.sizeChanged == original

@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_changedForeignKeyToValueField_type(instance):
    assert isinstance(instance.changedForeignKeyToValueField, str)


@given(instance=rdbms::RdbmsModifyFieldOperation_strategy)
def test_rdbms::rdbmsmodifyfieldoperation_changedForeignKeyToValueField_setter(instance):
    original = instance.changedForeignKeyToValueField
    instance.changedForeignKeyToValueField = original
    assert instance.changedForeignKeyToValueField == original

@given(instance=rdbms::RdbmsCreateFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmscreatefieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsCreateFieldOperation)

@given(instance=RdbmsTableOperation_strategy)
@settings(max_examples=50)
def test_rdbmstableoperation_instantiation(instance):
    assert isinstance(instance, RdbmsTableOperation)

@given(instance=rdbms::RdbmsDeleteTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsdeletetableoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsDeleteTableOperation)

@given(instance=rdbms::RdbmsCreateTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmscreatetableoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsCreateTableOperation)

@given(instance=RdbmsExpression_strategy)
@settings(max_examples=50)
def test_rdbmsexpression_instantiation(instance):
    assert isinstance(instance, RdbmsExpression)

@given(instance=rdbms::RdbmsRelationExpression_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsrelationexpression_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsRelationExpression)

@given(instance=rdbms::RdbmsLabelExpression_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmslabelexpression_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsLabelExpression)

@given(instance=rdbms::RdbmsLabelExpression_strategy)
def test_rdbms::rdbmslabelexpression_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=rdbms::RdbmsLabelExpression_strategy)
def test_rdbms::rdbmslabelexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=rdbms::RdbmsFeature_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsfeature_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsFeature)

@given(instance=rdbms::RdbmsFeature_strategy)
def test_rdbms::rdbmsfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::RdbmsFeature_strategy)
def test_rdbms::rdbmsfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::RdbmsViewRecord_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewrecord_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewRecord)

@given(instance=rdbms::RdbmsConfiguration_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsconfiguration_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsConfiguration)

@given(instance=rdbms::RdbmsConfiguration_strategy)
def test_rdbms::rdbmsconfiguration_dialect_type(instance):
    assert isinstance(instance.dialect, str)


@given(instance=rdbms::RdbmsConfiguration_strategy)
def test_rdbms::rdbmsconfiguration_dialect_setter(instance):
    original = instance.dialect
    instance.dialect = original
    assert instance.dialect == original

@given(instance=rdbms::RdbmsModel_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsmodel_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsModel)

@given(instance=rdbms::RdbmsModel_strategy)
def test_rdbms::rdbmsmodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=rdbms::RdbmsModel_strategy)
def test_rdbms::rdbmsmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=rdbms::RdbmsModifyTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsmodifytableoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsModifyTableOperation)

@given(instance=rdbms::RdbmsModifyTableOperation_strategy)
def test_rdbms::rdbmsmodifytableoperation_nameChanged_type(instance):
    assert isinstance(instance.nameChanged, str)


@given(instance=rdbms::RdbmsModifyTableOperation_strategy)
def test_rdbms::rdbmsmodifytableoperation_nameChanged_setter(instance):
    original = instance.nameChanged
    instance.nameChanged = original
    assert instance.nameChanged == original

@given(instance=RdbmsViewTableField_strategy)
@settings(max_examples=50)
def test_rdbmsviewtablefield_instantiation(instance):
    assert isinstance(instance, RdbmsViewTableField)

@given(instance=rdbms::RdbmsViewForeignIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewforeignidentifierfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewForeignIdentifierField)

@given(instance=rdbms::RdbmsViewAliasField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewaliasfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewAliasField)

@given(instance=RdbmsViewField_strategy)
@settings(max_examples=50)
def test_rdbmsviewfield_instantiation(instance):
    assert isinstance(instance, RdbmsViewField)

@given(instance=rdbms::RdbmsViewTableField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewtablefield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewTableField)

@given(instance=rdbms::RdbmsViewTableField_strategy)
def test_rdbms::rdbmsviewtablefield_foreign_type(instance):
    assert isinstance(instance.foreign, bool)


@given(instance=rdbms::RdbmsViewTableField_strategy)
def test_rdbms::rdbmsviewtablefield_foreign_setter(instance):
    original = instance.foreign
    instance.foreign = original
    assert instance.foreign == original

@given(instance=rdbms::RdbmsViewExpressionField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewexpressionfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewExpressionField)

@given(instance=rdbms::RdbmsViewExpressionField_strategy)
def test_rdbms::rdbmsviewexpressionfield_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=rdbms::RdbmsViewExpressionField_strategy)
def test_rdbms::rdbmsviewexpressionfield_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=RdbmsViewAliasField_strategy)
@settings(max_examples=50)
def test_rdbmsviewaliasfield_instantiation(instance):
    assert isinstance(instance, RdbmsViewAliasField)

@given(instance=rdbms::RdbmsViewValueField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewvaluefield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewValueField)

@given(instance=rdbms::RdbmsViewIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewidentifierfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewIdentifierField)

@given(instance=rdbms::RdbmsViewRelation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewrelation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewRelation)

@given(instance=rdbms::RdbmsViewRelation_strategy)
def test_rdbms::rdbmsviewrelation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::RdbmsViewRelation_strategy)
def test_rdbms::rdbmsviewrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RdbmsField_strategy)
@settings(max_examples=50)
def test_rdbmsfield_instantiation(instance):
    assert isinstance(instance, RdbmsField)

@given(instance=rdbms::RdbmsValueField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsvaluefield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsValueField)

@given(instance=rdbms::RdbmsValueField_strategy)
def test_rdbms::rdbmsvaluefield_technical_type(instance):
    assert isinstance(instance.technical, bool)


@given(instance=rdbms::RdbmsValueField_strategy)
def test_rdbms::rdbmsvaluefield_technical_setter(instance):
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

@given(instance=rdbms::RdbmsForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsforeignkey_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsForeignKey)

@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_deleteOnCascade_type(instance):
    assert isinstance(instance.deleteOnCascade, bool)


@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_deleteOnCascade_setter(instance):
    original = instance.deleteOnCascade
    instance.deleteOnCascade = original
    assert instance.deleteOnCascade == original

@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_deferred_type(instance):
    assert isinstance(instance.deferred, bool)


@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_deferred_setter(instance):
    original = instance.deferred
    instance.deferred = original
    assert instance.deferred == original

@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_foreignKeySqlName_type(instance):
    assert isinstance(instance.foreignKeySqlName, str)


@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_foreignKeySqlName_setter(instance):
    original = instance.foreignKeySqlName
    instance.foreignKeySqlName = original
    assert instance.foreignKeySqlName == original

@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_inheritenceBased_type(instance):
    assert isinstance(instance.inheritenceBased, bool)


@given(instance=rdbms::RdbmsForeignKey_strategy)
def test_rdbms::rdbmsforeignkey_inheritenceBased_setter(instance):
    original = instance.inheritenceBased
    instance.inheritenceBased = original
    assert instance.inheritenceBased == original

@given(instance=rdbms::RdbmsFieldType_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsfieldtype_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsFieldType)

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_rdbmsTypeName_type(instance):
    assert isinstance(instance.rdbmsTypeName, str)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_rdbmsTypeName_setter(instance):
    original = instance.rdbmsTypeName
    instance.rdbmsTypeName = original
    assert instance.rdbmsTypeName == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_storageByte_type(instance):
    assert isinstance(instance.storageByte, int)


@given(instance=rdbms::RdbmsFieldType_strategy)
def test_rdbms::rdbmsfieldtype_storageByte_setter(instance):
    original = instance.storageByte
    instance.storageByte = original
    assert instance.storageByte == original

@given(instance=rdbms::RdbmsIdentifierField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsidentifierfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsIdentifierField)

@given(instance=rdbms::RdbmsJunctionTable_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsjunctiontable_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsJunctionTable)

@given(instance=rdbms::RdbmsElement_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmselement_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsElement)

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_originalName_type(instance):
    assert isinstance(instance.originalName, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_originalName_setter(instance):
    original = instance.originalName
    instance.originalName = original
    assert instance.originalName == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_originalPackage_type(instance):
    assert isinstance(instance.originalPackage, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_originalPackage_setter(instance):
    original = instance.originalPackage
    instance.originalPackage = original
    assert instance.originalPackage == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_sqlName_type(instance):
    assert isinstance(instance.sqlName, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_sqlName_setter(instance):
    original = instance.sqlName
    instance.sqlName = original
    assert instance.sqlName == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=rdbms::RdbmsElement_strategy)
def test_rdbms::rdbmselement_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=RdbmsElement_strategy)
@settings(max_examples=50)
def test_rdbmselement_instantiation(instance):
    assert isinstance(instance, RdbmsElement)

@given(instance=rdbms::RdbmsField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsField)

@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_scale_type(instance):
    assert isinstance(instance.scale, int)


@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_storageByte_type(instance):
    assert isinstance(instance.storageByte, int)


@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_storageByte_setter(instance):
    original = instance.storageByte
    instance.storageByte = original
    assert instance.storageByte == original

@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_rdbmsTypeName_type(instance):
    assert isinstance(instance.rdbmsTypeName, str)


@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_rdbmsTypeName_setter(instance):
    original = instance.rdbmsTypeName
    instance.rdbmsTypeName = original
    assert instance.rdbmsTypeName == original

@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=rdbms::RdbmsField_strategy)
def test_rdbms::rdbmsfield_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=rdbms::RdbmsIndex_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsindex_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsIndex)

@given(instance=rdbms::RdbmsIndex_strategy)
def test_rdbms::rdbmsindex_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=rdbms::RdbmsIndex_strategy)
def test_rdbms::rdbmsindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=rdbms::RdbmsViewField_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsviewfield_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsViewField)

@given(instance=rdbms::RdbmsViewField_strategy)
def test_rdbms::rdbmsviewfield_inherited_type(instance):
    assert isinstance(instance.inherited, bool)


@given(instance=rdbms::RdbmsViewField_strategy)
def test_rdbms::rdbmsviewfield_inherited_setter(instance):
    original = instance.inherited
    instance.inherited = original
    assert instance.inherited == original

@given(instance=rdbms::RdbmsUniqueConstraint_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsuniqueconstraint_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsUniqueConstraint)

@given(instance=rdbms::RdbmsFieldOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsfieldoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsFieldOperation)

@given(instance=rdbms::RdbmsFieldOperation_strategy)
def test_rdbms::rdbmsfieldoperation_reviewRequired_type(instance):
    assert isinstance(instance.reviewRequired, bool)


@given(instance=rdbms::RdbmsFieldOperation_strategy)
def test_rdbms::rdbmsfieldoperation_reviewRequired_setter(instance):
    original = instance.reviewRequired
    instance.reviewRequired = original
    assert instance.reviewRequired == original

@given(instance=rdbms::RdbmsTableAlias_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmstablealias_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsTableAlias)

@given(instance=rdbms::RdbmsTableOperation_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmstableoperation_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsTableOperation)

@given(instance=rdbms::RdbmsExpression_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsexpression_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsExpression)

@given(instance=rdbms::RdbmsExpression_strategy)
def test_rdbms::rdbmsexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=rdbms::RdbmsExpression_strategy)
def test_rdbms::rdbmsexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=rdbms::RdbmsView_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsview_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsView)

@given(instance=rdbms::RdbmsView_strategy)
def test_rdbms::rdbmsview_originUuid_type(instance):
    assert isinstance(instance.originUuid, str)


@given(instance=rdbms::RdbmsView_strategy)
def test_rdbms::rdbmsview_originUuid_setter(instance):
    original = instance.originUuid
    instance.originUuid = original
    assert instance.originUuid == original

@given(instance=rdbms::RdbmsTable_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmstable_instantiation(instance):
    assert isinstance(instance, rdbms::RdbmsTable)
