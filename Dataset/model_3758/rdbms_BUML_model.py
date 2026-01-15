####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
rdbms_RdbmsElement = Class(name="rdbms::RdbmsElement", is_abstract=True)
rdbms_RdbmsTable = Class(name="rdbms::RdbmsTable")
RdbmsElement = Class(name="RdbmsElement")
rdbms_RdbmsFieldType = Class(name="rdbms::RdbmsFieldType")
rdbms_RdbmsField = Class(name="rdbms::RdbmsField", is_abstract=True)
rdbms_RdbmsUniqueConstraint = Class(name="rdbms::RdbmsUniqueConstraint")
rdbms_RdbmsIdentifierField = Class(name="rdbms::RdbmsIdentifierField")
rdbms_RdbmsIndex = Class(name="rdbms::RdbmsIndex")
rdbms_RdbmsJunctionTable = Class(name="rdbms::RdbmsJunctionTable")
RdbmsTable = Class(name="RdbmsTable")
RdbmsField = Class(name="RdbmsField")
rdbms_RdbmsForeignKey = Class(name="rdbms::RdbmsForeignKey")
RdbmsIdentifierField = Class(name="RdbmsIdentifierField")
rdbms_RdbmsViewValueField = Class(name="rdbms::RdbmsViewValueField")
RdbmsViewAliasField = Class(name="RdbmsViewAliasField")
rdbms_RdbmsViewExpressionField = Class(name="rdbms::RdbmsViewExpressionField")
RdbmsViewField = Class(name="RdbmsViewField")
rdbms_RdbmsView = Class(name="rdbms::RdbmsView")
rdbms_RdbmsViewField = Class(name="rdbms::RdbmsViewField", is_abstract=True)
rdbms_RdbmsTableAlias = Class(name="rdbms::RdbmsTableAlias")
rdbms_RdbmsViewRelation = Class(name="rdbms::RdbmsViewRelation")
rdbms_RdbmsViewIdentifierField = Class(name="rdbms::RdbmsViewIdentifierField")
rdbms_RdbmsModel = Class(name="rdbms::RdbmsModel")
rdbms_RdbmsConfiguration = Class(name="rdbms::RdbmsConfiguration")
rdbms_RdbmsExpression = Class(name="rdbms::RdbmsExpression", is_abstract=True)
rdbms_RdbmsFeature = Class(name="rdbms::RdbmsFeature")
rdbms_RdbmsTableOperation = Class(name="rdbms::RdbmsTableOperation", is_abstract=True)
rdbms_RdbmsViewRecord = Class(name="rdbms::RdbmsViewRecord")
rdbms_RdbmsValueField = Class(name="rdbms::RdbmsValueField")
rdbms_RdbmsModifyTableOperation = Class(name="rdbms::RdbmsModifyTableOperation")
RdbmsTableOperation = Class(name="RdbmsTableOperation")
rdbms_RdbmsCreateFieldOperation = Class(name="rdbms::RdbmsCreateFieldOperation")
rdbms_RdbmsModifyFieldOperation = Class(name="rdbms::RdbmsModifyFieldOperation")
rdbms_RdbmsDeleteFieldOperation = Class(name="rdbms::RdbmsDeleteFieldOperation")
rdbms_RdbmsLabelExpression = Class(name="rdbms::RdbmsLabelExpression")
RdbmsExpression = Class(name="RdbmsExpression")
rdbms_RdbmsRelationExpression = Class(name="rdbms::RdbmsRelationExpression")
rdbms_RdbmsViewAliasField = Class(name="rdbms::RdbmsViewAliasField", is_abstract=True)
RdbmsViewTableField = Class(name="RdbmsViewTableField")
rdbms_RdbmsFieldOperation = Class(name="rdbms::RdbmsFieldOperation", is_abstract=True)
RdbmsFieldOperation = Class(name="RdbmsFieldOperation")
rdbms_RdbmsViewTableField = Class(name="rdbms::RdbmsViewTableField", is_abstract=True)
rdbms_RdbmsViewForeignIdentifierField = Class(name="rdbms::RdbmsViewForeignIdentifierField")
rdbms_RdbmsCreateTableOperation = Class(name="rdbms::RdbmsCreateTableOperation")
rdbms_RdbmsDeleteTableOperation = Class(name="rdbms::RdbmsDeleteTableOperation")
rdbms_RdbmsViewRecordValue = Class(name="rdbms::RdbmsViewRecordValue")
rdbms_RdbmsOperationMeta = Class(name="rdbms::RdbmsOperationMeta")

# rdbms_RdbmsElement class attributes and methods
rdbms_RdbmsElement_name: Property = Property(name="name", type=StringType)
rdbms_RdbmsElement_uuid: Property = Property(name="uuid", type=StringType)
rdbms_RdbmsElement_shortName: Property = Property(name="shortName", type=StringType)
rdbms_RdbmsElement_fullName: Property = Property(name="fullName", type=StringType)
rdbms_RdbmsElement_description: Property = Property(name="description", type=StringType)
rdbms_RdbmsElement_sqlName: Property = Property(name="sqlName", type=StringType)
rdbms_RdbmsElement_originalName: Property = Property(name="originalName", type=StringType)
rdbms_RdbmsElement_originalPackage: Property = Property(name="originalPackage", type=StringType)
rdbms_RdbmsElement.attributes={rdbms_RdbmsElement_sqlName, rdbms_RdbmsElement_description, rdbms_RdbmsElement_name, rdbms_RdbmsElement_originalName, rdbms_RdbmsElement_fullName, rdbms_RdbmsElement_uuid, rdbms_RdbmsElement_originalPackage, rdbms_RdbmsElement_shortName}

# rdbms_RdbmsTable class attributes and methods

# RdbmsElement class attributes and methods

# rdbms_RdbmsFieldType class attributes and methods
rdbms_RdbmsFieldType_scale: Property = Property(name="scale", type=IntegerType)
rdbms_RdbmsFieldType_storageByte: Property = Property(name="storageByte", type=IntegerType)
rdbms_RdbmsFieldType_name: Property = Property(name="name", type=StringType)
rdbms_RdbmsFieldType_rdbmsTypeName: Property = Property(name="rdbmsTypeName", type=StringType)
rdbms_RdbmsFieldType_uuid: Property = Property(name="uuid", type=StringType)
rdbms_RdbmsFieldType_description: Property = Property(name="description", type=StringType)
rdbms_RdbmsFieldType_size: Property = Property(name="size", type=IntegerType)
rdbms_RdbmsFieldType_precision: Property = Property(name="precision", type=IntegerType)
rdbms_RdbmsFieldType.attributes={rdbms_RdbmsFieldType_scale, rdbms_RdbmsFieldType_name, rdbms_RdbmsFieldType_description, rdbms_RdbmsFieldType_precision, rdbms_RdbmsFieldType_size, rdbms_RdbmsFieldType_rdbmsTypeName, rdbms_RdbmsFieldType_uuid, rdbms_RdbmsFieldType_storageByte}

# rdbms_RdbmsField class attributes and methods
rdbms_RdbmsField_mandatory: Property = Property(name="mandatory", type=BooleanType)
rdbms_RdbmsField_rdbmsTypeName: Property = Property(name="rdbmsTypeName", type=StringType)
rdbms_RdbmsField_size: Property = Property(name="size", type=IntegerType)
rdbms_RdbmsField_precision: Property = Property(name="precision", type=IntegerType)
rdbms_RdbmsField_scale: Property = Property(name="scale", type=IntegerType)
rdbms_RdbmsField_storageByte: Property = Property(name="storageByte", type=IntegerType)
rdbms_RdbmsField.attributes={rdbms_RdbmsField_rdbmsTypeName, rdbms_RdbmsField_scale, rdbms_RdbmsField_storageByte, rdbms_RdbmsField_precision, rdbms_RdbmsField_mandatory, rdbms_RdbmsField_size}

# rdbms_RdbmsUniqueConstraint class attributes and methods

# rdbms_RdbmsIdentifierField class attributes and methods

# rdbms_RdbmsIndex class attributes and methods
rdbms_RdbmsIndex_unique: Property = Property(name="unique", type=BooleanType)
rdbms_RdbmsIndex.attributes={rdbms_RdbmsIndex_unique}

# rdbms_RdbmsJunctionTable class attributes and methods

# RdbmsTable class attributes and methods

# RdbmsField class attributes and methods

# rdbms_RdbmsForeignKey class attributes and methods
rdbms_RdbmsForeignKey_inheritenceBased: Property = Property(name="inheritenceBased", type=BooleanType)
rdbms_RdbmsForeignKey_foreignKeySqlName: Property = Property(name="foreignKeySqlName", type=StringType)
rdbms_RdbmsForeignKey_deleteOnCascade: Property = Property(name="deleteOnCascade", type=BooleanType)
rdbms_RdbmsForeignKey_deferred: Property = Property(name="deferred", type=BooleanType)
rdbms_RdbmsForeignKey_readOnly: Property = Property(name="readOnly", type=BooleanType)
rdbms_RdbmsForeignKey.attributes={rdbms_RdbmsForeignKey_readOnly, rdbms_RdbmsForeignKey_foreignKeySqlName, rdbms_RdbmsForeignKey_inheritenceBased, rdbms_RdbmsForeignKey_deferred, rdbms_RdbmsForeignKey_deleteOnCascade}

# RdbmsIdentifierField class attributes and methods

# rdbms_RdbmsViewValueField class attributes and methods

# RdbmsViewAliasField class attributes and methods

# rdbms_RdbmsViewExpressionField class attributes and methods
rdbms_RdbmsViewExpressionField_expression: Property = Property(name="expression", type=StringType)
rdbms_RdbmsViewExpressionField.attributes={rdbms_RdbmsViewExpressionField_expression}

# RdbmsViewField class attributes and methods

# rdbms_RdbmsView class attributes and methods
rdbms_RdbmsView_originUuid: Property = Property(name="originUuid", type=StringType)
rdbms_RdbmsView.attributes={rdbms_RdbmsView_originUuid}

# rdbms_RdbmsViewField class attributes and methods
rdbms_RdbmsViewField_inherited: Property = Property(name="inherited", type=BooleanType)
rdbms_RdbmsViewField.attributes={rdbms_RdbmsViewField_inherited}

# rdbms_RdbmsTableAlias class attributes and methods

# rdbms_RdbmsViewRelation class attributes and methods
rdbms_RdbmsViewRelation_name: Property = Property(name="name", type=StringType)
rdbms_RdbmsViewRelation.attributes={rdbms_RdbmsViewRelation_name}

# rdbms_RdbmsViewIdentifierField class attributes and methods

# rdbms_RdbmsModel class attributes and methods
rdbms_RdbmsModel_version: Property = Property(name="version", type=StringType)
rdbms_RdbmsModel.attributes={rdbms_RdbmsModel_version}

# rdbms_RdbmsConfiguration class attributes and methods
rdbms_RdbmsConfiguration_dialect: Property = Property(name="dialect", type=StringType)
rdbms_RdbmsConfiguration.attributes={rdbms_RdbmsConfiguration_dialect}

# rdbms_RdbmsExpression class attributes and methods
rdbms_RdbmsExpression_expression: Property = Property(name="expression", type=StringType)
rdbms_RdbmsExpression.attributes={rdbms_RdbmsExpression_expression}

# rdbms_RdbmsFeature class attributes and methods
rdbms_RdbmsFeature_name: Property = Property(name="name", type=StringType)
rdbms_RdbmsFeature.attributes={rdbms_RdbmsFeature_name}

# rdbms_RdbmsTableOperation class attributes and methods

# rdbms_RdbmsViewRecord class attributes and methods

# rdbms_RdbmsValueField class attributes and methods
rdbms_RdbmsValueField_technical: Property = Property(name="technical", type=BooleanType)
rdbms_RdbmsValueField.attributes={rdbms_RdbmsValueField_technical}

# rdbms_RdbmsModifyTableOperation class attributes and methods
rdbms_RdbmsModifyTableOperation_nameChanged: Property = Property(name="nameChanged", type=StringType)
rdbms_RdbmsModifyTableOperation.attributes={rdbms_RdbmsModifyTableOperation_nameChanged}

# RdbmsTableOperation class attributes and methods

# rdbms_RdbmsCreateFieldOperation class attributes and methods

# rdbms_RdbmsModifyFieldOperation class attributes and methods
rdbms_RdbmsModifyFieldOperation_sizeChanged: Property = Property(name="sizeChanged", type=StringType)
rdbms_RdbmsModifyFieldOperation_nameChanged: Property = Property(name="nameChanged", type=StringType)
rdbms_RdbmsModifyFieldOperation_changedValueFieldToForeignKey: Property = Property(name="changedValueFieldToForeignKey", type=StringType)
rdbms_RdbmsModifyFieldOperation_changedForeignKeyToValueField: Property = Property(name="changedForeignKeyToValueField", type=StringType)
rdbms_RdbmsModifyFieldOperation_typeChanged: Property = Property(name="typeChanged", type=BooleanType)
rdbms_RdbmsModifyFieldOperation_mandatoryChanged: Property = Property(name="mandatoryChanged", type=BooleanType)
rdbms_RdbmsModifyFieldOperation.attributes={rdbms_RdbmsModifyFieldOperation_changedForeignKeyToValueField, rdbms_RdbmsModifyFieldOperation_mandatoryChanged, rdbms_RdbmsModifyFieldOperation_changedValueFieldToForeignKey, rdbms_RdbmsModifyFieldOperation_nameChanged, rdbms_RdbmsModifyFieldOperation_sizeChanged, rdbms_RdbmsModifyFieldOperation_typeChanged}

# rdbms_RdbmsDeleteFieldOperation class attributes and methods

# rdbms_RdbmsLabelExpression class attributes and methods
rdbms_RdbmsLabelExpression_text: Property = Property(name="text", type=StringType)
rdbms_RdbmsLabelExpression.attributes={rdbms_RdbmsLabelExpression_text}

# RdbmsExpression class attributes and methods

# rdbms_RdbmsRelationExpression class attributes and methods

# rdbms_RdbmsViewAliasField class attributes and methods

# RdbmsViewTableField class attributes and methods

# rdbms_RdbmsFieldOperation class attributes and methods
rdbms_RdbmsFieldOperation_reviewRequired: Property = Property(name="reviewRequired", type=BooleanType)
rdbms_RdbmsFieldOperation.attributes={rdbms_RdbmsFieldOperation_reviewRequired}

# RdbmsFieldOperation class attributes and methods

# rdbms_RdbmsViewTableField class attributes and methods
rdbms_RdbmsViewTableField_foreign: Property = Property(name="foreign", type=BooleanType)
rdbms_RdbmsViewTableField.attributes={rdbms_RdbmsViewTableField_foreign}

# rdbms_RdbmsViewForeignIdentifierField class attributes and methods

# rdbms_RdbmsCreateTableOperation class attributes and methods

# rdbms_RdbmsDeleteTableOperation class attributes and methods

# rdbms_RdbmsViewRecordValue class attributes and methods
rdbms_RdbmsViewRecordValue_value: Property = Property(name="value", type=StringType)
rdbms_RdbmsViewRecordValue.attributes={rdbms_RdbmsViewRecordValue_value}

# rdbms_RdbmsOperationMeta class attributes and methods

# Relationships
table9: BinaryAssociation = BinaryAssociation(
    name="table9",
    ends={
        Property(name="RdbmsTable", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="rdbms_RdbmsFieldType", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsField", type=rdbms_RdbmsFieldType, multiplicity=Multiplicity(0, 1))
    }
)
fields0: BinaryAssociation = BinaryAssociation(
    name="fields0",
    ends={
        Property(name="RdbmsField", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=rdbms_RdbmsField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uniqueConstraints1: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraints1",
    ends={
        Property(name="RdbmsUniqueConstraint", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table2", type=rdbms_RdbmsUniqueConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey3: BinaryAssociation = BinaryAssociation(
    name="primaryKey3",
    ends={
        Property(name="rdbms_RdbmsIdentifierField", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsTable", type=rdbms_RdbmsIdentifierField, multiplicity=Multiplicity(1, 1))
    }
)
indexes4: BinaryAssociation = BinaryAssociation(
    name="indexes4",
    ends={
        Property(name="RdbmsIndex", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=rdbms_RdbmsIndex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="rdbms_RdbmsTable8", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsTable6", type=rdbms_RdbmsTable, multiplicity=Multiplicity(0, 1))
    }
)
table12: BinaryAssociation = BinaryAssociation(
    name="table12",
    ends={
        Property(name="RdbmsTable13", type=rdbms_RdbmsUniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueConstraints", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
fields14: BinaryAssociation = BinaryAssociation(
    name="fields14",
    ends={
        Property(name="rdbms_RdbmsField15", type=rdbms_RdbmsUniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsUniqueConstraint", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 9999))
    }
)
field116: BinaryAssociation = BinaryAssociation(
    name="field116",
    ends={
        Property(name="rdbms_RdbmsForeignKey", type=rdbms_RdbmsJunctionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsJunctionTable", type=rdbms_RdbmsForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
field217: BinaryAssociation = BinaryAssociation(
    name="field217",
    ends={
        Property(name="rdbms_RdbmsForeignKey19", type=rdbms_RdbmsJunctionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsJunctionTable18", type=rdbms_RdbmsForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
referenceKey11: BinaryAssociation = BinaryAssociation(
    name="referenceKey11",
    ends={
        Property(name="RdbmsIdentifierField", type=rdbms_RdbmsForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=rdbms_RdbmsIdentifierField, multiplicity=Multiplicity(1, 1))
    }
)
primaryIdentifierField25: BinaryAssociation = BinaryAssociation(
    name="primaryIdentifierField25",
    ends={
        Property(name="rdbms_RdbmsViewIdentifierField", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsView26", type=rdbms_RdbmsViewIdentifierField, multiplicity=Multiplicity(1, 1))
    }
)
tables27: BinaryAssociation = BinaryAssociation(
    name="tables27",
    ends={
        Property(name="RdbmsTableAlias", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1)),
        Property(name="view28", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
view29: BinaryAssociation = BinaryAssociation(
    name="view29",
    ends={
        Property(name="RdbmsView", type=rdbms_RdbmsViewField, multiplicity=Multiplicity(1, 1)),
        Property(name="fields30", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys20: BinaryAssociation = BinaryAssociation(
    name="foreignKeys20",
    ends={
        Property(name="RdbmsForeignKey", type=rdbms_RdbmsIdentifierField, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceKey", type=rdbms_RdbmsForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
fields21: BinaryAssociation = BinaryAssociation(
    name="fields21",
    ends={
        Property(name="RdbmsViewField", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1)),
        Property(name="view", type=rdbms_RdbmsViewField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryTable22: BinaryAssociation = BinaryAssociation(
    name="primaryTable22",
    ends={
        Property(name="rdbms_RdbmsTableAlias", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsView", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 1))
    }
)
relations23: BinaryAssociation = BinaryAssociation(
    name="relations23",
    ends={
        Property(name="rdbms_RdbmsViewRelation", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsView24", type=rdbms_RdbmsViewRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rdbmsFieldTypes32: BinaryAssociation = BinaryAssociation(
    name="rdbmsFieldTypes32",
    ends={
        Property(name="rdbms_RdbmsFieldType33", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModel", type=rdbms_RdbmsFieldType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rdbmsTables34: BinaryAssociation = BinaryAssociation(
    name="rdbmsTables34",
    ends={
        Property(name="rdbms_RdbmsTable36", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModel35", type=rdbms_RdbmsTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rdbmsViews37: BinaryAssociation = BinaryAssociation(
    name="rdbmsViews37",
    ends={
        Property(name="rdbms_RdbmsView39", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModel38", type=rdbms_RdbmsView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration40: BinaryAssociation = BinaryAssociation(
    name="configuration40",
    ends={
        Property(name="rdbms_RdbmsConfiguration", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModel41", type=rdbms_RdbmsConfiguration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions31: BinaryAssociation = BinaryAssociation(
    name="expressions31",
    ends={
        Property(name="rdbms_RdbmsExpression", type=rdbms_RdbmsViewExpressionField, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewExpressionField", type=rdbms_RdbmsExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
features46: BinaryAssociation = BinaryAssociation(
    name="features46",
    ends={
        Property(name="rdbms_RdbmsFeature", type=rdbms_RdbmsConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsConfiguration47", type=rdbms_RdbmsFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table48: BinaryAssociation = BinaryAssociation(
    name="table48",
    ends={
        Property(name="rdbms_RdbmsTable50", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsTableAlias49", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
view51: BinaryAssociation = BinaryAssociation(
    name="view51",
    ends={
        Property(name="RdbmsView52", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1))
    }
)
tableOperations42: BinaryAssociation = BinaryAssociation(
    name="tableOperations42",
    ends={
        Property(name="rdbms_RdbmsTableOperation", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModel43", type=rdbms_RdbmsTableOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewRecords44: BinaryAssociation = BinaryAssociation(
    name="viewRecords44",
    ends={
        Property(name="rdbms_RdbmsViewRecord", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModel45", type=rdbms_RdbmsViewRecord, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createFieldOperations57: BinaryAssociation = BinaryAssociation(
    name="createFieldOperations57",
    ends={
        Property(name="rdbms_RdbmsCreateFieldOperation", type=rdbms_RdbmsModifyTableOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModifyTableOperation", type=rdbms_RdbmsCreateFieldOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifyFieldOperations58: BinaryAssociation = BinaryAssociation(
    name="modifyFieldOperations58",
    ends={
        Property(name="rdbms_RdbmsModifyFieldOperation", type=rdbms_RdbmsModifyTableOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModifyTableOperation59", type=rdbms_RdbmsModifyFieldOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deleteFieldOperations60: BinaryAssociation = BinaryAssociation(
    name="deleteFieldOperations60",
    ends={
        Property(name="rdbms_RdbmsDeleteFieldOperation", type=rdbms_RdbmsModifyTableOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModifyTableOperation61", type=rdbms_RdbmsDeleteFieldOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
previousTable62: BinaryAssociation = BinaryAssociation(
    name="previousTable62",
    ends={
        Property(name="rdbms_RdbmsTable64", type=rdbms_RdbmsModifyTableOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModifyTableOperation63", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
field53: BinaryAssociation = BinaryAssociation(
    name="field53",
    ends={
        Property(name="rdbms_RdbmsViewAliasField", type=rdbms_RdbmsRelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsRelationExpression", type=rdbms_RdbmsViewAliasField, multiplicity=Multiplicity(1, 1))
    }
)
alias54: BinaryAssociation = BinaryAssociation(
    name="alias54",
    ends={
        Property(name="rdbms_RdbmsTableAlias56", type=rdbms_RdbmsViewAliasField, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewAliasField55", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 1))
    }
)
field65: BinaryAssociation = BinaryAssociation(
    name="field65",
    ends={
        Property(name="rdbms_RdbmsField66", type=rdbms_RdbmsFieldOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsFieldOperation", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 1))
    }
)
previousField67: BinaryAssociation = BinaryAssociation(
    name="previousField67",
    ends={
        Property(name="rdbms_RdbmsField69", type=rdbms_RdbmsModifyFieldOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsModifyFieldOperation68", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 1))
    }
)
fromField76: BinaryAssociation = BinaryAssociation(
    name="fromField76",
    ends={
        Property(name="rdbms_RdbmsIdentifierField78", type=rdbms_RdbmsViewRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRelation77", type=rdbms_RdbmsIdentifierField, multiplicity=Multiplicity(1, 1))
    }
)
toField79: BinaryAssociation = BinaryAssociation(
    name="toField79",
    ends={
        Property(name="rdbms_RdbmsIdentifierField81", type=rdbms_RdbmsViewRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRelation80", type=rdbms_RdbmsIdentifierField, multiplicity=Multiplicity(1, 1))
    }
)
fromAlias70: BinaryAssociation = BinaryAssociation(
    name="fromAlias70",
    ends={
        Property(name="rdbms_RdbmsTableAlias72", type=rdbms_RdbmsViewRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRelation71", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 1))
    }
)
toAlias73: BinaryAssociation = BinaryAssociation(
    name="toAlias73",
    ends={
        Property(name="rdbms_RdbmsTableAlias75", type=rdbms_RdbmsViewRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRelation74", type=rdbms_RdbmsTableAlias, multiplicity=Multiplicity(1, 1))
    }
)
table86: BinaryAssociation = BinaryAssociation(
    name="table86",
    ends={
        Property(name="RdbmsTable87", type=rdbms_RdbmsIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
tableField82: BinaryAssociation = BinaryAssociation(
    name="tableField82",
    ends={
        Property(name="rdbms_RdbmsField83", type=rdbms_RdbmsViewTableField, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewTableField", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 1))
    }
)
referenceIdentifier84: BinaryAssociation = BinaryAssociation(
    name="referenceIdentifier84",
    ends={
        Property(name="rdbms_RdbmsViewIdentifierField85", type=rdbms_RdbmsViewForeignIdentifierField, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewForeignIdentifierField", type=rdbms_RdbmsViewIdentifierField, multiplicity=Multiplicity(1, 1))
    }
)
identifierField95: BinaryAssociation = BinaryAssociation(
    name="identifierField95",
    ends={
        Property(name="rdbms_RdbmsViewIdentifierField97", type=rdbms_RdbmsViewRecordValue, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRecordValue96", type=rdbms_RdbmsViewIdentifierField, multiplicity=Multiplicity(0, 1))
    }
)
valueField98: BinaryAssociation = BinaryAssociation(
    name="valueField98",
    ends={
        Property(name="rdbms_RdbmsViewValueField", type=rdbms_RdbmsViewRecordValue, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRecordValue99", type=rdbms_RdbmsViewValueField, multiplicity=Multiplicity(0, 1))
    }
)
table100: BinaryAssociation = BinaryAssociation(
    name="table100",
    ends={
        Property(name="rdbms_RdbmsTable102", type=rdbms_RdbmsTableOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsTableOperation101", type=rdbms_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
fields88: BinaryAssociation = BinaryAssociation(
    name="fields88",
    ends={
        Property(name="rdbms_RdbmsField89", type=rdbms_RdbmsIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsIndex", type=rdbms_RdbmsField, multiplicity=Multiplicity(1, 9999))
    }
)
values90: BinaryAssociation = BinaryAssociation(
    name="values90",
    ends={
        Property(name="rdbms_RdbmsViewRecordValue", type=rdbms_RdbmsViewRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRecord91", type=rdbms_RdbmsViewRecordValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view92: BinaryAssociation = BinaryAssociation(
    name="view92",
    ends={
        Property(name="rdbms_RdbmsView94", type=rdbms_RdbmsViewRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsViewRecord93", type=rdbms_RdbmsView, multiplicity=Multiplicity(1, 1))
    }
)
previousModel103: BinaryAssociation = BinaryAssociation(
    name="previousModel103",
    ends={
        Property(name="rdbms_RdbmsModel104", type=rdbms_RdbmsOperationMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsOperationMeta", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1))
    }
)
currentModel105: BinaryAssociation = BinaryAssociation(
    name="currentModel105",
    ends={
        Property(name="rdbms_RdbmsModel107", type=rdbms_RdbmsOperationMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsOperationMeta106", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1))
    }
)
incrementalModel108: BinaryAssociation = BinaryAssociation(
    name="incrementalModel108",
    ends={
        Property(name="rdbms_RdbmsModel110", type=rdbms_RdbmsOperationMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RdbmsOperationMeta109", type=rdbms_RdbmsModel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdbms_RdbmsTable_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsTable)
gen_rdbms_RdbmsField_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsField)
gen_rdbms_RdbmsJunctionTable_RdbmsTable = Generalization(general=RdbmsTable, specific=rdbms_RdbmsJunctionTable)
gen_rdbms_RdbmsIdentifierField_RdbmsField = Generalization(general=RdbmsField, specific=rdbms_RdbmsIdentifierField)
gen_rdbms_RdbmsForeignKey_RdbmsIdentifierField = Generalization(general=RdbmsIdentifierField, specific=rdbms_RdbmsForeignKey)
gen_rdbms_RdbmsUniqueConstraint_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsUniqueConstraint)
gen_rdbms_RdbmsViewField_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsViewField)
gen_rdbms_RdbmsViewValueField_RdbmsViewAliasField = Generalization(general=RdbmsViewAliasField, specific=rdbms_RdbmsViewValueField)
gen_rdbms_RdbmsViewExpressionField_RdbmsViewField = Generalization(general=RdbmsViewField, specific=rdbms_RdbmsViewExpressionField)
gen_rdbms_RdbmsView_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsView)
gen_rdbms_RdbmsExpression_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsExpression)
gen_rdbms_RdbmsViewIdentifierField_RdbmsViewAliasField = Generalization(general=RdbmsViewAliasField, specific=rdbms_RdbmsViewIdentifierField)
gen_rdbms_RdbmsTableAlias_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsTableAlias)
gen_rdbms_RdbmsValueField_RdbmsField = Generalization(general=RdbmsField, specific=rdbms_RdbmsValueField)
gen_rdbms_RdbmsModifyTableOperation_RdbmsTableOperation = Generalization(general=RdbmsTableOperation, specific=rdbms_RdbmsModifyTableOperation)
gen_rdbms_RdbmsLabelExpression_RdbmsExpression = Generalization(general=RdbmsExpression, specific=rdbms_RdbmsLabelExpression)
gen_rdbms_RdbmsRelationExpression_RdbmsExpression = Generalization(general=RdbmsExpression, specific=rdbms_RdbmsRelationExpression)
gen_rdbms_RdbmsViewAliasField_RdbmsViewTableField = Generalization(general=RdbmsViewTableField, specific=rdbms_RdbmsViewAliasField)
gen_rdbms_RdbmsDeleteFieldOperation_RdbmsFieldOperation = Generalization(general=RdbmsFieldOperation, specific=rdbms_RdbmsDeleteFieldOperation)
gen_rdbms_RdbmsFieldOperation_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsFieldOperation)
gen_rdbms_RdbmsCreateFieldOperation_RdbmsFieldOperation = Generalization(general=RdbmsFieldOperation, specific=rdbms_RdbmsCreateFieldOperation)
gen_rdbms_RdbmsModifyFieldOperation_RdbmsFieldOperation = Generalization(general=RdbmsFieldOperation, specific=rdbms_RdbmsModifyFieldOperation)
gen_rdbms_RdbmsViewTableField_RdbmsViewField = Generalization(general=RdbmsViewField, specific=rdbms_RdbmsViewTableField)
gen_rdbms_RdbmsIndex_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsIndex)
gen_rdbms_RdbmsViewForeignIdentifierField_RdbmsViewTableField = Generalization(general=RdbmsViewTableField, specific=rdbms_RdbmsViewForeignIdentifierField)
gen_rdbms_RdbmsTableOperation_RdbmsElement = Generalization(general=RdbmsElement, specific=rdbms_RdbmsTableOperation)
gen_rdbms_RdbmsCreateTableOperation_RdbmsTableOperation = Generalization(general=RdbmsTableOperation, specific=rdbms_RdbmsCreateTableOperation)
gen_rdbms_RdbmsDeleteTableOperation_RdbmsTableOperation = Generalization(general=RdbmsTableOperation, specific=rdbms_RdbmsDeleteTableOperation)

# Domain Model
domain_model = DomainModel(
    name="rdbms",
    types={rdbms_RdbmsElement, rdbms_RdbmsTable, RdbmsElement, rdbms_RdbmsFieldType, rdbms_RdbmsField, rdbms_RdbmsUniqueConstraint, rdbms_RdbmsIdentifierField, rdbms_RdbmsIndex, rdbms_RdbmsJunctionTable, RdbmsTable, RdbmsField, rdbms_RdbmsForeignKey, RdbmsIdentifierField, rdbms_RdbmsViewValueField, RdbmsViewAliasField, rdbms_RdbmsViewExpressionField, RdbmsViewField, rdbms_RdbmsView, rdbms_RdbmsViewField, rdbms_RdbmsTableAlias, rdbms_RdbmsViewRelation, rdbms_RdbmsViewIdentifierField, rdbms_RdbmsModel, rdbms_RdbmsConfiguration, rdbms_RdbmsExpression, rdbms_RdbmsFeature, rdbms_RdbmsTableOperation, rdbms_RdbmsViewRecord, rdbms_RdbmsValueField, rdbms_RdbmsModifyTableOperation, RdbmsTableOperation, rdbms_RdbmsCreateFieldOperation, rdbms_RdbmsModifyFieldOperation, rdbms_RdbmsDeleteFieldOperation, rdbms_RdbmsLabelExpression, RdbmsExpression, rdbms_RdbmsRelationExpression, rdbms_RdbmsViewAliasField, RdbmsViewTableField, rdbms_RdbmsFieldOperation, RdbmsFieldOperation, rdbms_RdbmsViewTableField, rdbms_RdbmsViewForeignIdentifierField, rdbms_RdbmsCreateTableOperation, rdbms_RdbmsDeleteTableOperation, rdbms_RdbmsViewRecordValue, rdbms_RdbmsOperationMeta},
    associations={table9, type10, fields0, uniqueConstraints1, primaryKey3, indexes4, parent7, table12, fields14, field116, field217, referenceKey11, primaryIdentifierField25, tables27, view29, foreignKeys20, fields21, primaryTable22, relations23, rdbmsFieldTypes32, rdbmsTables34, rdbmsViews37, configuration40, expressions31, features46, table48, view51, tableOperations42, viewRecords44, createFieldOperations57, modifyFieldOperations58, deleteFieldOperations60, previousTable62, field53, alias54, field65, previousField67, fromField76, toField79, fromAlias70, toAlias73, table86, tableField82, referenceIdentifier84, identifierField95, valueField98, table100, fields88, values90, view92, previousModel103, currentModel105, incrementalModel108},
    generalizations={gen_rdbms_RdbmsTable_RdbmsElement, gen_rdbms_RdbmsField_RdbmsElement, gen_rdbms_RdbmsJunctionTable_RdbmsTable, gen_rdbms_RdbmsIdentifierField_RdbmsField, gen_rdbms_RdbmsForeignKey_RdbmsIdentifierField, gen_rdbms_RdbmsUniqueConstraint_RdbmsElement, gen_rdbms_RdbmsViewField_RdbmsElement, gen_rdbms_RdbmsViewValueField_RdbmsViewAliasField, gen_rdbms_RdbmsViewExpressionField_RdbmsViewField, gen_rdbms_RdbmsView_RdbmsElement, gen_rdbms_RdbmsExpression_RdbmsElement, gen_rdbms_RdbmsViewIdentifierField_RdbmsViewAliasField, gen_rdbms_RdbmsTableAlias_RdbmsElement, gen_rdbms_RdbmsValueField_RdbmsField, gen_rdbms_RdbmsModifyTableOperation_RdbmsTableOperation, gen_rdbms_RdbmsLabelExpression_RdbmsExpression, gen_rdbms_RdbmsRelationExpression_RdbmsExpression, gen_rdbms_RdbmsViewAliasField_RdbmsViewTableField, gen_rdbms_RdbmsDeleteFieldOperation_RdbmsFieldOperation, gen_rdbms_RdbmsFieldOperation_RdbmsElement, gen_rdbms_RdbmsCreateFieldOperation_RdbmsFieldOperation, gen_rdbms_RdbmsModifyFieldOperation_RdbmsFieldOperation, gen_rdbms_RdbmsViewTableField_RdbmsViewField, gen_rdbms_RdbmsIndex_RdbmsElement, gen_rdbms_RdbmsViewForeignIdentifierField_RdbmsViewTableField, gen_rdbms_RdbmsTableOperation_RdbmsElement, gen_rdbms_RdbmsCreateTableOperation_RdbmsTableOperation, gen_rdbms_RdbmsDeleteTableOperation_RdbmsTableOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)