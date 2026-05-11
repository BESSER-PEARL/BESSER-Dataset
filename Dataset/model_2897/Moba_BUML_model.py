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

# Enumerations
MobaConstantValueFunction: Enumeration = Enumeration(
    name="MobaConstantValueFunction",
    literals={
            EnumerationLiteral(name="TO_LOWER_CASE"),
			EnumerationLiteral(name="TO_UPPER_CASE"),
			EnumerationLiteral(name="TO_FIRST_UPPER_CASE"),
			EnumerationLiteral(name="TO_FIRST_LOWER_CASE")
    }
)

MobaRESTMethods: Enumeration = Enumeration(
    name="MobaRESTMethods",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="PUT"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="POST")
    }
)

MobaLowerBound: Enumeration = Enumeration(
    name="MobaLowerBound",
    literals={
            EnumerationLiteral(name="OPTIONAL"),
			EnumerationLiteral(name="MANY"),
			EnumerationLiteral(name="ZERO"),
			EnumerationLiteral(name="ATLEASTONE"),
			EnumerationLiteral(name="ONE")
    }
)

MobaUpperBound: Enumeration = Enumeration(
    name="MobaUpperBound",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="MANY")
    }
)

MobaNFCModuleType: Enumeration = Enumeration(
    name="MobaNFCModuleType",
    literals={
            EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="CUSTOM"),
			EnumerationLiteral(name="TEXT")
    }
)

MobaBlueToothModuleType: Enumeration = Enumeration(
    name="MobaBlueToothModuleType",
    literals={
            EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="SPP"),
			EnumerationLiteral(name="BEACON")
    }
)

MobaGeofenceEvent: Enumeration = Enumeration(
    name="MobaGeofenceEvent",
    literals={
            EnumerationLiteral(name="ENTER"),
			EnumerationLiteral(name="LEAVE")
    }
)

# Classes
moba_MobaModelFeature = Class(name="moba_MobaModelFeature", is_abstract=True)
moba_MobaProject = Class(name="moba_MobaProject")
MobaModelFeature = Class(name="MobaModelFeature")
moba_MobaApplication = Class(name="moba_MobaApplication")
moba_MobaCache = Class(name="moba_MobaCache")
moba_MobaModel = Class(name="moba_MobaModel")
MobaFriendsAble = Class(name="MobaFriendsAble")
moba_MobaGeneratorMixinFeature = Class(name="moba_MobaGeneratorMixinFeature")
MobaGeneratorFeature = Class(name="MobaGeneratorFeature")
moba_MobaGeneratorIDFeature = Class(name="moba_MobaGeneratorIDFeature")
moba_MobaGeneratorSlot = Class(name="moba_MobaGeneratorSlot")
moba_MobaDataType = Class(name="moba_MobaDataType")
MobaConstraintable = Class(name="MobaConstraintable")
moba_MobaApplicationFeature = Class(name="moba_MobaApplicationFeature", is_abstract=True)
moba_MobaTemplate = Class(name="moba_MobaTemplate")
MobaApplicationFeature = Class(name="MobaApplicationFeature")
moba_MobaServer = Class(name="moba_MobaServer")
moba_MobaConstant = Class(name="moba_MobaConstant")
moba_MobaREST = Class(name="moba_MobaREST", is_abstract=True)
moba_MobaAuthorization = Class(name="moba_MobaAuthorization")
moba_MobaTransportSerializationType = Class(name="moba_MobaTransportSerializationType")
moba_MobaPersistenceType = Class(name="moba_MobaPersistenceType")
moba_MobaGenerator = Class(name="moba_MobaGenerator")
moba_MobaGeneratorFeature = Class(name="moba_MobaGeneratorFeature", is_abstract=True)
moba_MobaPropertiesAble = Class(name="moba_MobaPropertiesAble", is_abstract=True)
moba_MobaProperty = Class(name="moba_MobaProperty")
moba_MobaEnum = Class(name="moba_MobaEnum")
moba_MobaConstantValue = Class(name="moba_MobaConstantValue")
moba_MobaEntity = Class(name="moba_MobaEntity")
MobaData = Class(name="MobaData")
moba_MobaData = Class(name="moba_MobaData", is_abstract=True)
moba_MobaSettings = Class(name="moba_MobaSettings")
moba_MobaSettingsFeature = Class(name="moba_MobaSettingsFeature", is_abstract=True)
MobaFeature = Class(name="MobaFeature")
moba_MobaSettingsAttribute = Class(name="moba_MobaSettingsAttribute")
MobaSettingsFeature = Class(name="MobaSettingsFeature")
MobaMultiplicityAble = Class(name="MobaMultiplicityAble")
moba_MobaSettingsEntityReference = Class(name="moba_MobaSettingsEntityReference")
moba_MobaRESTHeader = Class(name="moba_MobaRESTHeader")
moba_MobaEntityFeature = Class(name="moba_MobaEntityFeature", is_abstract=True)
moba_MobaEntityIndex = Class(name="moba_MobaEntityIndex")
moba_MobaEntityAttribute = Class(name="moba_MobaEntityAttribute")
moba_MobaDto = Class(name="moba_MobaDto")
moba_MobaDtoFeature = Class(name="moba_MobaDtoFeature", is_abstract=True)
moba_MobaQueue = Class(name="moba_MobaQueue")
moba_MobaQueueFeature = Class(name="moba_MobaQueueFeature", is_abstract=True)
moba_MobaRESTPayloadDefinition = Class(name="moba_MobaRESTPayloadDefinition")
moba_MobaRESTCustomService = Class(name="moba_MobaRESTCustomService")
MobaREST = Class(name="MobaREST")
moba_MobaRESTWorkflow = Class(name="moba_MobaRESTWorkflow")
moba_MobaRESTAbstractAttribute = Class(name="moba_MobaRESTAbstractAttribute", is_abstract=True)
moba_MobaRESTAttribute = Class(name="moba_MobaRESTAttribute")
MobaRESTAbstractAttribute = Class(name="MobaRESTAbstractAttribute")
moba_MobaRESTDtoAttribute = Class(name="moba_MobaRESTDtoAttribute")
moba_MobaDtoAttribute = Class(name="moba_MobaDtoAttribute")
MobaDtoFeature = Class(name="MobaDtoFeature")
moba_MobaDtoReference = Class(name="moba_MobaDtoReference")
moba_MobaRESTCrud = Class(name="moba_MobaRESTCrud")
moba_MobaFeature = Class(name="moba_MobaFeature", is_abstract=True)
MobaEntityFeature = Class(name="MobaEntityFeature")
moba_MobaMultiplicityAble = Class(name="moba_MobaMultiplicityAble", is_abstract=True)
moba_MobaMuliplicity = Class(name="moba_MobaMuliplicity")
moba_MobaEntityReference = Class(name="moba_MobaEntityReference")
moba_MobaEntityEmbeddable = Class(name="moba_MobaEntityEmbeddable")
moba_MobaMinConstraint = Class(name="moba_MobaMinConstraint")
moba_MobaMaxConstraint = Class(name="moba_MobaMaxConstraint")
moba_MobaFutureConstraint = Class(name="moba_MobaFutureConstraint")
moba_MobaPastConstraint = Class(name="moba_MobaPastConstraint")
moba_MobaNotNullConstraint = Class(name="moba_MobaNotNullConstraint")
moba_MobaNullConstraint = Class(name="moba_MobaNullConstraint")
moba_MobaMinLengthConstraint = Class(name="moba_MobaMinLengthConstraint")
moba_MobaDtoEmbeddable = Class(name="moba_MobaDtoEmbeddable")
moba_MobaQueueReference = Class(name="moba_MobaQueueReference")
MobaQueueFeature = Class(name="MobaQueueFeature")
moba_MobaConstraintable = Class(name="moba_MobaConstraintable", is_abstract=True)
moba_MobaConstraint = Class(name="moba_MobaConstraint", is_abstract=True)
moba_MobaRegexpConstraint = Class(name="moba_MobaRegexpConstraint")
MobaConstraint = Class(name="MobaConstraint")
moba_MobaAppInstallTrigger = Class(name="moba_MobaAppInstallTrigger")
MobaTrigger = Class(name="MobaTrigger")
moba_MobaAppUpdateTrigger = Class(name="moba_MobaAppUpdateTrigger")
moba_MobaSMSTrigger = Class(name="moba_MobaSMSTrigger")
moba_MobaDeviceStartupTrigger = Class(name="moba_MobaDeviceStartupTrigger")
moba_MobaEmailTrigger = Class(name="moba_MobaEmailTrigger")
moba_MobaTimerTrigger = Class(name="moba_MobaTimerTrigger")
moba_MobaPushTrigger = Class(name="moba_MobaPushTrigger")
moba_MobaGeofenceTrigger = Class(name="moba_MobaGeofenceTrigger")
moba_MobaMaxLengthConstraint = Class(name="moba_MobaMaxLengthConstraint")
moba_MobaDigitsConstraint = Class(name="moba_MobaDigitsConstraint")
moba_MobaEnumLiteral = Class(name="moba_MobaEnumLiteral")
moba_MobaTrigger = Class(name="moba_MobaTrigger", is_abstract=True)
moba_index_MobaIndex = Class(name="moba_index_MobaIndex")
moba_MobaFriend = Class(name="moba_MobaFriend")
moba_MobaFriendsAble = Class(name="moba_MobaFriendsAble", is_abstract=True)
MobaPropertiesAble = Class(name="MobaPropertiesAble")
moba_MobaExternalModule = Class(name="moba_MobaExternalModule", is_abstract=True)
moba_MobaBluetoothModule = Class(name="moba_MobaBluetoothModule")
MobaExternalModule = Class(name="MobaExternalModule")
moba_MobaNFCModule = Class(name="moba_MobaNFCModule")
moba_MobaPushModule = Class(name="moba_MobaPushModule")
MobaIndexEntry = Class(name="MobaIndexEntry")
moba_index_MobaIndexEntry = Class(name="moba_index_MobaIndexEntry")
index_moba_MobaApplication = Class(name="index_moba_MobaApplication")

# moba_MobaModelFeature class attributes and methods
moba_MobaModelFeature_id: Property = Property(name="id", type=StringType)
moba_MobaModelFeature_name: Property = Property(name="name", type=StringType)
moba_MobaModelFeature_version: Property = Property(name="version", type=StringType)
moba_MobaModelFeature.attributes={moba_MobaModelFeature_version, moba_MobaModelFeature_name, moba_MobaModelFeature_id}

# moba_MobaProject class attributes and methods

# MobaModelFeature class attributes and methods

# moba_MobaApplication class attributes and methods
moba_MobaApplication_javaPackage: Property = Property(name="javaPackage", type=StringType)
moba_MobaApplication.attributes={moba_MobaApplication_javaPackage}

# moba_MobaCache class attributes and methods
moba_MobaCache_name: Property = Property(name="name", type=StringType)
moba_MobaCache_cacheTypeString: Property = Property(name="cacheTypeString", type=StringType)
moba_MobaCache_cacheStrategyString: Property = Property(name="cacheStrategyString", type=StringType)
moba_MobaCache_cacheIntervalInt: Property = Property(name="cacheIntervalInt", type=IntegerType)
moba_MobaCache.attributes={moba_MobaCache_cacheIntervalInt, moba_MobaCache_name, moba_MobaCache_cacheTypeString, moba_MobaCache_cacheStrategyString}

# moba_MobaModel class attributes and methods
moba_MobaModel_copyright: Property = Property(name="copyright", type=StringType)
moba_MobaModel.attributes={moba_MobaModel_copyright}

# MobaFriendsAble class attributes and methods

# moba_MobaGeneratorMixinFeature class attributes and methods

# MobaGeneratorFeature class attributes and methods

# moba_MobaGeneratorIDFeature class attributes and methods
moba_MobaGeneratorIDFeature_generatorId: Property = Property(name="generatorId", type=StringType)
moba_MobaGeneratorIDFeature_generatorVersion: Property = Property(name="generatorVersion", type=StringType)
moba_MobaGeneratorIDFeature.attributes={moba_MobaGeneratorIDFeature_generatorVersion, moba_MobaGeneratorIDFeature_generatorId}

# moba_MobaGeneratorSlot class attributes and methods
moba_MobaGeneratorSlot_name: Property = Property(name="name", type=StringType)
moba_MobaGeneratorSlot_type: Property = Property(name="type", type=StringType)
moba_MobaGeneratorSlot.attributes={moba_MobaGeneratorSlot_name, moba_MobaGeneratorSlot_type}

# moba_MobaDataType class attributes and methods
moba_MobaDataType_name: Property = Property(name="name", type=StringType)
moba_MobaDataType_primitive: Property = Property(name="primitive", type=BooleanType)
moba_MobaDataType_string: Property = Property(name="string", type=BooleanType)
moba_MobaDataType_numeric: Property = Property(name="numeric", type=BooleanType)
moba_MobaDataType_decimal: Property = Property(name="decimal", type=BooleanType)
moba_MobaDataType_date: Property = Property(name="date", type=BooleanType)
moba_MobaDataType_time: Property = Property(name="time", type=BooleanType)
moba_MobaDataType_timestamp: Property = Property(name="timestamp", type=BooleanType)
moba_MobaDataType_array: Property = Property(name="array", type=BooleanType)
moba_MobaDataType_dateFormatString: Property = Property(name="dateFormatString", type=StringType)
moba_MobaDataType_bool: Property = Property(name="bool", type=BooleanType)
moba_MobaDataType_predefined: Property = Property(name="predefined", type=BooleanType)
moba_MobaDataType.attributes={moba_MobaDataType_date, moba_MobaDataType_string, moba_MobaDataType_primitive, moba_MobaDataType_predefined, moba_MobaDataType_array, moba_MobaDataType_numeric, moba_MobaDataType_timestamp, moba_MobaDataType_dateFormatString, moba_MobaDataType_decimal, moba_MobaDataType_bool, moba_MobaDataType_time, moba_MobaDataType_name}

# MobaConstraintable class attributes and methods

# moba_MobaApplicationFeature class attributes and methods

# moba_MobaTemplate class attributes and methods
moba_MobaTemplate_downloadTemplate: Property = Property(name="downloadTemplate", type=StringType)
moba_MobaTemplate.attributes={moba_MobaTemplate_downloadTemplate}

# MobaApplicationFeature class attributes and methods

# moba_MobaServer class attributes and methods
moba_MobaServer_name: Property = Property(name="name", type=StringType)
moba_MobaServer_urlString: Property = Property(name="urlString", type=StringType)
moba_MobaServer.attributes={moba_MobaServer_urlString, moba_MobaServer_name}

# moba_MobaConstant class attributes and methods
moba_MobaConstant_name: Property = Property(name="name", type=StringType)
moba_MobaConstant.attributes={moba_MobaConstant_name}

# moba_MobaREST class attributes and methods
moba_MobaREST_path: Property = Property(name="path", type=StringType)
moba_MobaREST_name: Property = Property(name="name", type=StringType)
moba_MobaREST_url: Property = Property(name="url", type=StringType)
moba_MobaREST_bigData: Property = Property(name="bigData", type=BooleanType)
moba_MobaREST.attributes={moba_MobaREST_name, moba_MobaREST_url, moba_MobaREST_bigData, moba_MobaREST_path}

# moba_MobaAuthorization class attributes and methods
moba_MobaAuthorization_name: Property = Property(name="name", type=StringType)
moba_MobaAuthorization.attributes={moba_MobaAuthorization_name}

# moba_MobaTransportSerializationType class attributes and methods
moba_MobaTransportSerializationType_name: Property = Property(name="name", type=StringType)
moba_MobaTransportSerializationType.attributes={moba_MobaTransportSerializationType_name}

# moba_MobaPersistenceType class attributes and methods
moba_MobaPersistenceType_name: Property = Property(name="name", type=StringType)
moba_MobaPersistenceType.attributes={moba_MobaPersistenceType_name}

# moba_MobaGenerator class attributes and methods
moba_MobaGenerator_name: Property = Property(name="name", type=StringType)
moba_MobaGenerator_active: Property = Property(name="active", type=BooleanType)
moba_MobaGenerator.attributes={moba_MobaGenerator_name, moba_MobaGenerator_active}

# moba_MobaGeneratorFeature class attributes and methods

# moba_MobaPropertiesAble class attributes and methods

# moba_MobaProperty class attributes and methods
moba_MobaProperty_keyString: Property = Property(name="keyString", type=StringType)
moba_MobaProperty_valueString: Property = Property(name="valueString", type=StringType)
moba_MobaProperty_key: Property = Property(name="key", type=StringType)
moba_MobaProperty_value: Property = Property(name="value", type=StringType)
moba_MobaProperty.attributes={moba_MobaProperty_valueString, moba_MobaProperty_key, moba_MobaProperty_value, moba_MobaProperty_keyString}

# moba_MobaEnum class attributes and methods

# moba_MobaConstantValue class attributes and methods
moba_MobaConstantValue_valueInt: Property = Property(name="valueInt", type=StringType)
moba_MobaConstantValue_valueDouble: Property = Property(name="valueDouble", type=StringType)
moba_MobaConstantValue_valueString: Property = Property(name="valueString", type=StringType)
moba_MobaConstantValue_valueConstFunctions: Property = Property(name="valueConstFunctions", type=StringType)
moba_MobaConstantValue_valueConstToLowerCase: Property = Property(name="valueConstToLowerCase", type=BooleanType)
moba_MobaConstantValue.attributes={moba_MobaConstantValue_valueConstFunctions, moba_MobaConstantValue_valueInt, moba_MobaConstantValue_valueConstToLowerCase, moba_MobaConstantValue_valueDouble, moba_MobaConstantValue_valueString}

# moba_MobaEntity class attributes and methods
moba_MobaEntity_name: Property = Property(name="name", type=StringType)
moba_MobaEntity.attributes={moba_MobaEntity_name}

# MobaData class attributes and methods

# moba_MobaData class attributes and methods

# moba_MobaSettings class attributes and methods
moba_MobaSettings_name: Property = Property(name="name", type=StringType)
moba_MobaSettings_active: Property = Property(name="active", type=BooleanType)
moba_MobaSettings.attributes={moba_MobaSettings_active, moba_MobaSettings_name}

# moba_MobaSettingsFeature class attributes and methods

# MobaFeature class attributes and methods

# moba_MobaSettingsAttribute class attributes and methods
moba_MobaSettingsAttribute_lazy: Property = Property(name="lazy", type=BooleanType)
moba_MobaSettingsAttribute_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaSettingsAttribute_domainKey: Property = Property(name="domainKey", type=BooleanType)
moba_MobaSettingsAttribute_domainDescription: Property = Property(name="domainDescription", type=BooleanType)
moba_MobaSettingsAttribute_formatString: Property = Property(name="formatString", type=StringType)
moba_MobaSettingsAttribute.attributes={moba_MobaSettingsAttribute_lazy, moba_MobaSettingsAttribute_transient, moba_MobaSettingsAttribute_domainKey, moba_MobaSettingsAttribute_domainDescription, moba_MobaSettingsAttribute_formatString}

# MobaSettingsFeature class attributes and methods

# MobaMultiplicityAble class attributes and methods

# moba_MobaSettingsEntityReference class attributes and methods
moba_MobaSettingsEntityReference_cascading: Property = Property(name="cascading", type=BooleanType)
moba_MobaSettingsEntityReference_lazy: Property = Property(name="lazy", type=BooleanType)
moba_MobaSettingsEntityReference_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaSettingsEntityReference.attributes={moba_MobaSettingsEntityReference_transient, moba_MobaSettingsEntityReference_cascading, moba_MobaSettingsEntityReference_lazy}

# moba_MobaRESTHeader class attributes and methods
moba_MobaRESTHeader_valueString: Property = Property(name="valueString", type=StringType)
moba_MobaRESTHeader_key: Property = Property(name="key", type=StringType)
moba_MobaRESTHeader_value: Property = Property(name="value", type=StringType)
moba_MobaRESTHeader_contentTypeHeader: Property = Property(name="contentTypeHeader", type=BooleanType)
moba_MobaRESTHeader_rawHeader: Property = Property(name="rawHeader", type=BooleanType)
moba_MobaRESTHeader_keyString: Property = Property(name="keyString", type=StringType)
moba_MobaRESTHeader.attributes={moba_MobaRESTHeader_rawHeader, moba_MobaRESTHeader_valueString, moba_MobaRESTHeader_keyString, moba_MobaRESTHeader_value, moba_MobaRESTHeader_contentTypeHeader, moba_MobaRESTHeader_key}

# moba_MobaEntityFeature class attributes and methods

# moba_MobaEntityIndex class attributes and methods
moba_MobaEntityIndex_name: Property = Property(name="name", type=StringType)
moba_MobaEntityIndex_unique: Property = Property(name="unique", type=BooleanType)
moba_MobaEntityIndex.attributes={moba_MobaEntityIndex_unique, moba_MobaEntityIndex_name}

# moba_MobaEntityAttribute class attributes and methods
moba_MobaEntityAttribute_lazy: Property = Property(name="lazy", type=BooleanType)
moba_MobaEntityAttribute_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaEntityAttribute_domainKey: Property = Property(name="domainKey", type=BooleanType)
moba_MobaEntityAttribute_domainDescription: Property = Property(name="domainDescription", type=BooleanType)
moba_MobaEntityAttribute_formatString: Property = Property(name="formatString", type=StringType)
moba_MobaEntityAttribute.attributes={moba_MobaEntityAttribute_formatString, moba_MobaEntityAttribute_domainDescription, moba_MobaEntityAttribute_transient, moba_MobaEntityAttribute_lazy, moba_MobaEntityAttribute_domainKey}

# moba_MobaDto class attributes and methods
moba_MobaDto_name: Property = Property(name="name", type=StringType)
moba_MobaDto.attributes={moba_MobaDto_name}

# moba_MobaDtoFeature class attributes and methods

# moba_MobaQueue class attributes and methods
moba_MobaQueue_name: Property = Property(name="name", type=StringType)
moba_MobaQueue.attributes={moba_MobaQueue_name}

# moba_MobaQueueFeature class attributes and methods

# moba_MobaRESTPayloadDefinition class attributes and methods
moba_MobaRESTPayloadDefinition_array: Property = Property(name="array", type=BooleanType)
moba_MobaRESTPayloadDefinition.attributes={moba_MobaRESTPayloadDefinition_array}

# moba_MobaRESTCustomService class attributes and methods
moba_MobaRESTCustomService_operation: Property = Property(name="operation", type=StringType)
moba_MobaRESTCustomService.attributes={moba_MobaRESTCustomService_operation}

# MobaREST class attributes and methods

# moba_MobaRESTWorkflow class attributes and methods

# moba_MobaRESTAbstractAttribute class attributes and methods
moba_MobaRESTAbstractAttribute_aliasString: Property = Property(name="aliasString", type=StringType)
moba_MobaRESTAbstractAttribute_alias: Property = Property(name="alias", type=StringType)
moba_MobaRESTAbstractAttribute_attachment: Property = Property(name="attachment", type=BooleanType)
moba_MobaRESTAbstractAttribute.attributes={moba_MobaRESTAbstractAttribute_alias, moba_MobaRESTAbstractAttribute_attachment, moba_MobaRESTAbstractAttribute_aliasString}

# moba_MobaRESTAttribute class attributes and methods
moba_MobaRESTAttribute_keyString: Property = Property(name="keyString", type=StringType)
moba_MobaRESTAttribute_key: Property = Property(name="key", type=StringType)
moba_MobaRESTAttribute_valueString: Property = Property(name="valueString", type=StringType)
moba_MobaRESTAttribute_valueDouble: Property = Property(name="valueDouble", type=StringType)
moba_MobaRESTAttribute_valueInt: Property = Property(name="valueInt", type=StringType)
moba_MobaRESTAttribute_value: Property = Property(name="value", type=StringType)
moba_MobaRESTAttribute_formatString: Property = Property(name="formatString", type=StringType)
moba_MobaRESTAttribute.attributes={moba_MobaRESTAttribute_keyString, moba_MobaRESTAttribute_valueDouble, moba_MobaRESTAttribute_value, moba_MobaRESTAttribute_formatString, moba_MobaRESTAttribute_valueString, moba_MobaRESTAttribute_key, moba_MobaRESTAttribute_valueInt}

# MobaRESTAbstractAttribute class attributes and methods

# moba_MobaRESTDtoAttribute class attributes and methods

# moba_MobaDtoAttribute class attributes and methods
moba_MobaDtoAttribute_lazy: Property = Property(name="lazy", type=BooleanType)
moba_MobaDtoAttribute_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaDtoAttribute_domainKey: Property = Property(name="domainKey", type=BooleanType)
moba_MobaDtoAttribute_domainDescription: Property = Property(name="domainDescription", type=BooleanType)
moba_MobaDtoAttribute_alias: Property = Property(name="alias", type=StringType)
moba_MobaDtoAttribute_formatString: Property = Property(name="formatString", type=StringType)
moba_MobaDtoAttribute.attributes={moba_MobaDtoAttribute_domainKey, moba_MobaDtoAttribute_formatString, moba_MobaDtoAttribute_transient, moba_MobaDtoAttribute_lazy, moba_MobaDtoAttribute_alias, moba_MobaDtoAttribute_domainDescription}

# MobaDtoFeature class attributes and methods

# moba_MobaDtoReference class attributes and methods
moba_MobaDtoReference_cascading: Property = Property(name="cascading", type=BooleanType)
moba_MobaDtoReference_lazy: Property = Property(name="lazy", type=BooleanType)
moba_MobaDtoReference_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaDtoReference_alias: Property = Property(name="alias", type=StringType)
moba_MobaDtoReference.attributes={moba_MobaDtoReference_transient, moba_MobaDtoReference_alias, moba_MobaDtoReference_cascading, moba_MobaDtoReference_lazy}

# moba_MobaRESTCrud class attributes and methods
moba_MobaRESTCrud_operations: Property = Property(name="operations", type=StringType)
moba_MobaRESTCrud.attributes={moba_MobaRESTCrud_operations}

# moba_MobaFeature class attributes and methods
moba_MobaFeature_name: Property = Property(name="name", type=StringType)
moba_MobaFeature.attributes={moba_MobaFeature_name}

# MobaEntityFeature class attributes and methods

# moba_MobaMultiplicityAble class attributes and methods

# moba_MobaMuliplicity class attributes and methods
moba_MobaMuliplicity_lower: Property = Property(name="lower", type=StringType)
moba_MobaMuliplicity_upper: Property = Property(name="upper", type=StringType)
moba_MobaMuliplicity.attributes={moba_MobaMuliplicity_lower, moba_MobaMuliplicity_upper}

# moba_MobaEntityReference class attributes and methods
moba_MobaEntityReference_cascading: Property = Property(name="cascading", type=BooleanType)
moba_MobaEntityReference_lazy: Property = Property(name="lazy", type=BooleanType)
moba_MobaEntityReference_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaEntityReference.attributes={moba_MobaEntityReference_cascading, moba_MobaEntityReference_lazy, moba_MobaEntityReference_transient}

# moba_MobaEntityEmbeddable class attributes and methods
moba_MobaEntityEmbeddable_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaEntityEmbeddable.attributes={moba_MobaEntityEmbeddable_transient}

# moba_MobaMinConstraint class attributes and methods
moba_MobaMinConstraint_filterValue: Property = Property(name="filterValue", type=FloatType)
moba_MobaMinConstraint.attributes={moba_MobaMinConstraint_filterValue}

# moba_MobaMaxConstraint class attributes and methods
moba_MobaMaxConstraint_filterValue: Property = Property(name="filterValue", type=FloatType)
moba_MobaMaxConstraint.attributes={moba_MobaMaxConstraint_filterValue}

# moba_MobaFutureConstraint class attributes and methods

# moba_MobaPastConstraint class attributes and methods

# moba_MobaNotNullConstraint class attributes and methods

# moba_MobaNullConstraint class attributes and methods

# moba_MobaMinLengthConstraint class attributes and methods
moba_MobaMinLengthConstraint_filterValue: Property = Property(name="filterValue", type=IntegerType)
moba_MobaMinLengthConstraint.attributes={moba_MobaMinLengthConstraint_filterValue}

# moba_MobaDtoEmbeddable class attributes and methods
moba_MobaDtoEmbeddable_transient: Property = Property(name="transient", type=BooleanType)
moba_MobaDtoEmbeddable_alias: Property = Property(name="alias", type=StringType)
moba_MobaDtoEmbeddable.attributes={moba_MobaDtoEmbeddable_transient, moba_MobaDtoEmbeddable_alias}

# moba_MobaQueueReference class attributes and methods

# MobaQueueFeature class attributes and methods

# moba_MobaConstraintable class attributes and methods

# moba_MobaConstraint class attributes and methods

# moba_MobaRegexpConstraint class attributes and methods
moba_MobaRegexpConstraint_filterString: Property = Property(name="filterString", type=StringType)
moba_MobaRegexpConstraint.attributes={moba_MobaRegexpConstraint_filterString}

# MobaConstraint class attributes and methods

# moba_MobaAppInstallTrigger class attributes and methods

# MobaTrigger class attributes and methods

# moba_MobaAppUpdateTrigger class attributes and methods

# moba_MobaSMSTrigger class attributes and methods

# moba_MobaDeviceStartupTrigger class attributes and methods

# moba_MobaEmailTrigger class attributes and methods

# moba_MobaTimerTrigger class attributes and methods

# moba_MobaPushTrigger class attributes and methods

# moba_MobaGeofenceTrigger class attributes and methods
moba_MobaGeofenceTrigger_eventType: Property = Property(name="eventType", type=StringType)
moba_MobaGeofenceTrigger.attributes={moba_MobaGeofenceTrigger_eventType}

# moba_MobaMaxLengthConstraint class attributes and methods
moba_MobaMaxLengthConstraint_filterValue: Property = Property(name="filterValue", type=IntegerType)
moba_MobaMaxLengthConstraint.attributes={moba_MobaMaxLengthConstraint_filterValue}

# moba_MobaDigitsConstraint class attributes and methods
moba_MobaDigitsConstraint_filterIntegerValue: Property = Property(name="filterIntegerValue", type=IntegerType)
moba_MobaDigitsConstraint_filterFractionValue: Property = Property(name="filterFractionValue", type=IntegerType)
moba_MobaDigitsConstraint.attributes={moba_MobaDigitsConstraint_filterFractionValue, moba_MobaDigitsConstraint_filterIntegerValue}

# moba_MobaEnumLiteral class attributes and methods
moba_MobaEnumLiteral_literal: Property = Property(name="literal", type=StringType)
moba_MobaEnumLiteral_name: Property = Property(name="name", type=StringType)
moba_MobaEnumLiteral_value: Property = Property(name="value", type=IntegerType)
moba_MobaEnumLiteral_default: Property = Property(name="default", type=BooleanType)
moba_MobaEnumLiteral_undefined: Property = Property(name="undefined", type=BooleanType)
moba_MobaEnumLiteral_hidden: Property = Property(name="hidden", type=BooleanType)
moba_MobaEnumLiteral.attributes={moba_MobaEnumLiteral_default, moba_MobaEnumLiteral_hidden, moba_MobaEnumLiteral_name, moba_MobaEnumLiteral_undefined, moba_MobaEnumLiteral_value, moba_MobaEnumLiteral_literal}

# moba_MobaTrigger class attributes and methods
moba_MobaTrigger_name: Property = Property(name="name", type=StringType)
moba_MobaTrigger.attributes={moba_MobaTrigger_name}

# moba_index_MobaIndex class attributes and methods
moba_index_MobaIndex_id: Property = Property(name="id", type=StringType)
moba_index_MobaIndex_name: Property = Property(name="name", type=StringType)
moba_index_MobaIndex_description: Property = Property(name="description", type=StringType)
moba_index_MobaIndex_version: Property = Property(name="version", type=StringType)
moba_index_MobaIndex.attributes={moba_index_MobaIndex_description, moba_index_MobaIndex_id, moba_index_MobaIndex_name, moba_index_MobaIndex_version}

# moba_MobaFriend class attributes and methods
moba_MobaFriend_valueString: Property = Property(name="valueString", type=StringType)
moba_MobaFriend_value: Property = Property(name="value", type=StringType)
moba_MobaFriend.attributes={moba_MobaFriend_value, moba_MobaFriend_valueString}

# moba_MobaFriendsAble class attributes and methods

# MobaPropertiesAble class attributes and methods

# moba_MobaExternalModule class attributes and methods
moba_MobaExternalModule_name: Property = Property(name="name", type=StringType)
moba_MobaExternalModule.attributes={moba_MobaExternalModule_name}

# moba_MobaBluetoothModule class attributes and methods
moba_MobaBluetoothModule_type: Property = Property(name="type", type=StringType)
moba_MobaBluetoothModule.attributes={moba_MobaBluetoothModule_type}

# MobaExternalModule class attributes and methods

# moba_MobaNFCModule class attributes and methods
moba_MobaNFCModule_type: Property = Property(name="type", type=StringType)
moba_MobaNFCModule.attributes={moba_MobaNFCModule_type}

# moba_MobaPushModule class attributes and methods

# MobaIndexEntry class attributes and methods

# moba_index_MobaIndexEntry class attributes and methods
moba_index_MobaIndexEntry_relativePath: Property = Property(name="relativePath", type=StringType)
moba_index_MobaIndexEntry_filename: Property = Property(name="filename", type=StringType)
moba_index_MobaIndexEntry_templateId: Property = Property(name="templateId", type=StringType)
moba_index_MobaIndexEntry_templateName: Property = Property(name="templateName", type=StringType)
moba_index_MobaIndexEntry_templateDescription: Property = Property(name="templateDescription", type=StringType)
moba_index_MobaIndexEntry_templateVersion: Property = Property(name="templateVersion", type=StringType)
moba_index_MobaIndexEntry.attributes={moba_index_MobaIndexEntry_relativePath, moba_index_MobaIndexEntry_templateDescription, moba_index_MobaIndexEntry_templateId, moba_index_MobaIndexEntry_templateVersion, moba_index_MobaIndexEntry_templateName, moba_index_MobaIndexEntry_filename}

# index_moba_MobaApplication class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="moba_MobaModelFeature", type=moba_MobaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaModel", type=moba_MobaModelFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uiApplication1: BinaryAssociation = BinaryAssociation(
    name="uiApplication1",
    ends={
        Property(name="moba_MobaApplication", type=moba_MobaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaProject", type=moba_MobaApplication, multiplicity=Multiplicity(0, 1))
    }
)
backgroundApplication2: BinaryAssociation = BinaryAssociation(
    name="backgroundApplication2",
    ends={
        Property(name="moba_MobaApplication4", type=moba_MobaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaProject3", type=moba_MobaApplication, multiplicity=Multiplicity(0, 1))
    }
)
defaultCache5: BinaryAssociation = BinaryAssociation(
    name="defaultCache5",
    ends={
        Property(name="moba_MobaCache", type=moba_MobaApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaApplication6", type=moba_MobaCache, multiplicity=Multiplicity(0, 1))
    }
)
generatorRef20: BinaryAssociation = BinaryAssociation(
    name="generatorRef20",
    ends={
        Property(name="moba_MobaGenerator21", type=moba_MobaGeneratorMixinFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaGeneratorMixinFeature", type=moba_MobaGenerator, multiplicity=Multiplicity(0, 1))
    }
)
superType23: BinaryAssociation = BinaryAssociation(
    name="superType23",
    ends={
        Property(name="moba_MobaGeneratorSlot", type=moba_MobaGeneratorSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaGeneratorSlot22", type=moba_MobaGeneratorSlot, multiplicity=Multiplicity(0, 1))
    }
)
features7: BinaryAssociation = BinaryAssociation(
    name="features7",
    ends={
        Property(name="moba_MobaApplicationFeature", type=moba_MobaApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaApplication8", type=moba_MobaApplicationFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template9: BinaryAssociation = BinaryAssociation(
    name="template9",
    ends={
        Property(name="moba_MobaApplication10", type=moba_MobaTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaTemplate", type=moba_MobaApplication, multiplicity=Multiplicity(0, 1))
    }
)
urlConst11: BinaryAssociation = BinaryAssociation(
    name="urlConst11",
    ends={
        Property(name="moba_MobaConstant", type=moba_MobaServer, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaServer", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
superType13: BinaryAssociation = BinaryAssociation(
    name="superType13",
    ends={
        Property(name="moba_MobaServer14", type=moba_MobaServer, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaServer12", type=moba_MobaServer, multiplicity=Multiplicity(0, 1))
    }
)
services15: BinaryAssociation = BinaryAssociation(
    name="services15",
    ends={
        Property(name="moba_MobaREST", type=moba_MobaServer, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaServer16", type=moba_MobaREST, multiplicity=Multiplicity(0, 9999))
    }
)
authorization17: BinaryAssociation = BinaryAssociation(
    name="authorization17",
    ends={
        Property(name="moba_MobaAuthorization", type=moba_MobaServer, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaServer18", type=moba_MobaAuthorization, multiplicity=Multiplicity(0, 1))
    }
)
features19: BinaryAssociation = BinaryAssociation(
    name="features19",
    ends={
        Property(name="moba_MobaGeneratorFeature", type=moba_MobaGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaGenerator", type=moba_MobaGeneratorFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties50: BinaryAssociation = BinaryAssociation(
    name="properties50",
    ends={
        Property(name="moba_MobaProperty", type=moba_MobaPropertiesAble, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaPropertiesAble", type=moba_MobaProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumAST24: BinaryAssociation = BinaryAssociation(
    name="enumAST24",
    ends={
        Property(name="moba_MobaEnum", type=moba_MobaDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDataType", type=moba_MobaEnum, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dateFormatConst25: BinaryAssociation = BinaryAssociation(
    name="dateFormatConst25",
    ends={
        Property(name="moba_MobaConstant27", type=moba_MobaDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDataType26", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
superType29: BinaryAssociation = BinaryAssociation(
    name="superType29",
    ends={
        Property(name="moba_MobaDataType30", type=moba_MobaDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDataType28", type=moba_MobaDataType, multiplicity=Multiplicity(0, 1))
    }
)
valueAST31: BinaryAssociation = BinaryAssociation(
    name="valueAST31",
    ends={
        Property(name="moba_MobaConstantValue", type=moba_MobaConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaConstant32", type=moba_MobaConstantValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cacheTypeConst33: BinaryAssociation = BinaryAssociation(
    name="cacheTypeConst33",
    ends={
        Property(name="moba_MobaConstant35", type=moba_MobaCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaCache34", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
cacheStrategyConst36: BinaryAssociation = BinaryAssociation(
    name="cacheStrategyConst36",
    ends={
        Property(name="moba_MobaConstant38", type=moba_MobaCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaCache37", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
cacheIntervalConst39: BinaryAssociation = BinaryAssociation(
    name="cacheIntervalConst39",
    ends={
        Property(name="moba_MobaConstant41", type=moba_MobaCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaCache40", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
cachePersistence42: BinaryAssociation = BinaryAssociation(
    name="cachePersistence42",
    ends={
        Property(name="moba_MobaPersistenceType", type=moba_MobaCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaCache43", type=moba_MobaPersistenceType, multiplicity=Multiplicity(0, 1))
    }
)
valueConst44: BinaryAssociation = BinaryAssociation(
    name="valueConst44",
    ends={
        Property(name="moba_MobaConstant46", type=moba_MobaConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaConstantValue45", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
tail48: BinaryAssociation = BinaryAssociation(
    name="tail48",
    ends={
        Property(name="moba_MobaConstantValue49", type=moba_MobaConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaConstantValue47", type=moba_MobaConstantValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="moba_MobaEntity", type=moba_MobaSettingsEntityReference, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaSettingsEntityReference", type=moba_MobaEntity, multiplicity=Multiplicity(0, 1))
    }
)
superType68: BinaryAssociation = BinaryAssociation(
    name="superType68",
    ends={
        Property(name="moba_MobaEntity69", type=moba_MobaEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntity67", type=moba_MobaEntity, multiplicity=Multiplicity(0, 1))
    }
)
cache70: BinaryAssociation = BinaryAssociation(
    name="cache70",
    ends={
        Property(name="moba_MobaCache72", type=moba_MobaEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntity71", type=moba_MobaCache, multiplicity=Multiplicity(0, 1))
    }
)
keyConst51: BinaryAssociation = BinaryAssociation(
    name="keyConst51",
    ends={
        Property(name="moba_MobaConstant53", type=moba_MobaProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaProperty52", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
valueConst54: BinaryAssociation = BinaryAssociation(
    name="valueConst54",
    ends={
        Property(name="moba_MobaConstant56", type=moba_MobaProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaProperty55", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
superType58: BinaryAssociation = BinaryAssociation(
    name="superType58",
    ends={
        Property(name="moba_MobaSettings", type=moba_MobaSettings, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaSettings57", type=moba_MobaSettings, multiplicity=Multiplicity(0, 1))
    }
)
features59: BinaryAssociation = BinaryAssociation(
    name="features59",
    ends={
        Property(name="moba_MobaSettingsFeature", type=moba_MobaSettings, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaSettings60", type=moba_MobaSettingsFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type61: BinaryAssociation = BinaryAssociation(
    name="type61",
    ends={
        Property(name="moba_MobaDataType62", type=moba_MobaSettingsAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaSettingsAttribute", type=moba_MobaDataType, multiplicity=Multiplicity(0, 1))
    }
)
formatConst63: BinaryAssociation = BinaryAssociation(
    name="formatConst63",
    ends={
        Property(name="moba_MobaConstant65", type=moba_MobaSettingsAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaSettingsAttribute64", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
errorDto100: BinaryAssociation = BinaryAssociation(
    name="errorDto100",
    ends={
        Property(name="moba_MobaRESTPayloadDefinition102", type=moba_MobaREST, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaREST101", type=moba_MobaRESTPayloadDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextDto103: BinaryAssociation = BinaryAssociation(
    name="contextDto103",
    ends={
        Property(name="moba_MobaRESTPayloadDefinition105", type=moba_MobaREST, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaREST104", type=moba_MobaRESTPayloadDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headers106: BinaryAssociation = BinaryAssociation(
    name="headers106",
    ends={
        Property(name="moba_MobaRESTHeader", type=moba_MobaREST, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaREST107", type=moba_MobaRESTHeader, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authorization108: BinaryAssociation = BinaryAssociation(
    name="authorization108",
    ends={
        Property(name="moba_MobaAuthorization110", type=moba_MobaREST, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaREST109", type=moba_MobaAuthorization, multiplicity=Multiplicity(0, 1))
    }
)
dto111: BinaryAssociation = BinaryAssociation(
    name="dto111",
    ends={
        Property(name="moba_MobaDto113", type=moba_MobaRESTPayloadDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTPayloadDefinition112", type=moba_MobaDto, multiplicity=Multiplicity(0, 1))
    }
)
serializationType114: BinaryAssociation = BinaryAssociation(
    name="serializationType114",
    ends={
        Property(name="moba_MobaTransportSerializationType116", type=moba_MobaRESTPayloadDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTPayloadDefinition115", type=moba_MobaTransportSerializationType, multiplicity=Multiplicity(0, 1))
    }
)
features73: BinaryAssociation = BinaryAssociation(
    name="features73",
    ends={
        Property(name="moba_MobaEntityFeature", type=moba_MobaEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntity74", type=moba_MobaEntityFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indizes75: BinaryAssociation = BinaryAssociation(
    name="indizes75",
    ends={
        Property(name="moba_MobaEntityIndex", type=moba_MobaEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntity76", type=moba_MobaEntityIndex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes77: BinaryAssociation = BinaryAssociation(
    name="attributes77",
    ends={
        Property(name="moba_MobaEntityAttribute", type=moba_MobaEntityIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntityIndex78", type=moba_MobaEntityAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
superType80: BinaryAssociation = BinaryAssociation(
    name="superType80",
    ends={
        Property(name="moba_MobaDto", type=moba_MobaDto, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDto79", type=moba_MobaDto, multiplicity=Multiplicity(0, 1))
    }
)
wrappedEntity81: BinaryAssociation = BinaryAssociation(
    name="wrappedEntity81",
    ends={
        Property(name="moba_MobaEntity83", type=moba_MobaDto, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDto82", type=moba_MobaEntity, multiplicity=Multiplicity(0, 1))
    }
)
features84: BinaryAssociation = BinaryAssociation(
    name="features84",
    ends={
        Property(name="moba_MobaDtoFeature", type=moba_MobaDto, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDto85", type=moba_MobaDtoFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serializationType86: BinaryAssociation = BinaryAssociation(
    name="serializationType86",
    ends={
        Property(name="moba_MobaTransportSerializationType", type=moba_MobaDto, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDto87", type=moba_MobaTransportSerializationType, multiplicity=Multiplicity(0, 1))
    }
)
superType89: BinaryAssociation = BinaryAssociation(
    name="superType89",
    ends={
        Property(name="moba_MobaQueue", type=moba_MobaQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaQueue88", type=moba_MobaQueue, multiplicity=Multiplicity(0, 1))
    }
)
cache90: BinaryAssociation = BinaryAssociation(
    name="cache90",
    ends={
        Property(name="moba_MobaCache92", type=moba_MobaQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaQueue91", type=moba_MobaCache, multiplicity=Multiplicity(0, 1))
    }
)
features93: BinaryAssociation = BinaryAssociation(
    name="features93",
    ends={
        Property(name="moba_MobaQueueFeature", type=moba_MobaQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaQueue94", type=moba_MobaQueueFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requestDto95: BinaryAssociation = BinaryAssociation(
    name="requestDto95",
    ends={
        Property(name="moba_MobaRESTPayloadDefinition", type=moba_MobaREST, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaREST96", type=moba_MobaRESTPayloadDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
responseDto97: BinaryAssociation = BinaryAssociation(
    name="responseDto97",
    ends={
        Property(name="moba_MobaRESTPayloadDefinition99", type=moba_MobaREST, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaREST98", type=moba_MobaRESTPayloadDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueConst135: BinaryAssociation = BinaryAssociation(
    name="valueConst135",
    ends={
        Property(name="moba_MobaConstant137", type=moba_MobaRESTHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTHeader136", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
parameters138: BinaryAssociation = BinaryAssociation(
    name="parameters138",
    ends={
        Property(name="moba_MobaRESTAbstractAttribute139", type=moba_MobaRESTCustomService, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTCustomService", type=moba_MobaRESTAbstractAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType141: BinaryAssociation = BinaryAssociation(
    name="superType141",
    ends={
        Property(name="moba_MobaRESTCustomService142", type=moba_MobaRESTCustomService, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTCustomService140", type=moba_MobaRESTCustomService, multiplicity=Multiplicity(0, 1))
    }
)
multipartParameters143: BinaryAssociation = BinaryAssociation(
    name="multipartParameters143",
    ends={
        Property(name="moba_MobaRESTAbstractAttribute145", type=moba_MobaRESTCustomService, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTCustomService144", type=moba_MobaRESTAbstractAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services146: BinaryAssociation = BinaryAssociation(
    name="services146",
    ends={
        Property(name="moba_MobaREST147", type=moba_MobaRESTWorkflow, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTWorkflow", type=moba_MobaREST, multiplicity=Multiplicity(0, 9999))
    }
)
aliasConst117: BinaryAssociation = BinaryAssociation(
    name="aliasConst117",
    ends={
        Property(name="moba_MobaConstant118", type=moba_MobaRESTAbstractAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTAbstractAttribute", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="moba_MobaDataType120", type=moba_MobaRESTAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTAttribute", type=moba_MobaDataType, multiplicity=Multiplicity(0, 1))
    }
)
keyConst121: BinaryAssociation = BinaryAssociation(
    name="keyConst121",
    ends={
        Property(name="moba_MobaConstant123", type=moba_MobaRESTAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTAttribute122", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
valueConst124: BinaryAssociation = BinaryAssociation(
    name="valueConst124",
    ends={
        Property(name="moba_MobaConstant126", type=moba_MobaRESTAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTAttribute125", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
formatConst127: BinaryAssociation = BinaryAssociation(
    name="formatConst127",
    ends={
        Property(name="moba_MobaConstant129", type=moba_MobaRESTAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTAttribute128", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
dtoFeature130: BinaryAssociation = BinaryAssociation(
    name="dtoFeature130",
    ends={
        Property(name="moba_MobaDtoFeature131", type=moba_MobaRESTDtoAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTDtoAttribute", type=moba_MobaDtoFeature, multiplicity=Multiplicity(0, 1))
    }
)
keyConst132: BinaryAssociation = BinaryAssociation(
    name="keyConst132",
    ends={
        Property(name="moba_MobaConstant134", type=moba_MobaRESTHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTHeader133", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
type165: BinaryAssociation = BinaryAssociation(
    name="type165",
    ends={
        Property(name="moba_MobaEntity166", type=moba_MobaEntityEmbeddable, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntityEmbeddable", type=moba_MobaEntity, multiplicity=Multiplicity(0, 1))
    }
)
type167: BinaryAssociation = BinaryAssociation(
    name="type167",
    ends={
        Property(name="moba_MobaDataType168", type=moba_MobaDtoAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDtoAttribute", type=moba_MobaDataType, multiplicity=Multiplicity(0, 1))
    }
)
formatConst169: BinaryAssociation = BinaryAssociation(
    name="formatConst169",
    ends={
        Property(name="moba_MobaConstant171", type=moba_MobaDtoAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDtoAttribute170", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
superType149: BinaryAssociation = BinaryAssociation(
    name="superType149",
    ends={
        Property(name="moba_MobaRESTWorkflow150", type=moba_MobaRESTWorkflow, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTWorkflow148", type=moba_MobaRESTWorkflow, multiplicity=Multiplicity(0, 1))
    }
)
superType152: BinaryAssociation = BinaryAssociation(
    name="superType152",
    ends={
        Property(name="moba_MobaRESTCrud", type=moba_MobaRESTCrud, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRESTCrud151", type=moba_MobaRESTCrud, multiplicity=Multiplicity(0, 1))
    }
)
type153: BinaryAssociation = BinaryAssociation(
    name="type153",
    ends={
        Property(name="moba_MobaDataType155", type=moba_MobaEntityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntityAttribute154", type=moba_MobaDataType, multiplicity=Multiplicity(0, 1))
    }
)
formatConst156: BinaryAssociation = BinaryAssociation(
    name="formatConst156",
    ends={
        Property(name="moba_MobaConstant158", type=moba_MobaEntityAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntityAttribute157", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity159: BinaryAssociation = BinaryAssociation(
    name="multiplicity159",
    ends={
        Property(name="moba_MobaMuliplicity", type=moba_MobaMultiplicityAble, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaMultiplicityAble", type=moba_MobaMuliplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type160: BinaryAssociation = BinaryAssociation(
    name="type160",
    ends={
        Property(name="moba_MobaEntity161", type=moba_MobaEntityReference, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntityReference", type=moba_MobaEntity, multiplicity=Multiplicity(0, 1))
    }
)
opposite163: BinaryAssociation = BinaryAssociation(
    name="opposite163",
    ends={
        Property(name="moba_MobaEntityReference164", type=moba_MobaEntityReference, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEntityReference162", type=moba_MobaEntityReference, multiplicity=Multiplicity(0, 1))
    }
)
filterConst182: BinaryAssociation = BinaryAssociation(
    name="filterConst182",
    ends={
        Property(name="moba_MobaConstant183", type=moba_MobaRegexpConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaRegexpConstraint", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
filterConst184: BinaryAssociation = BinaryAssociation(
    name="filterConst184",
    ends={
        Property(name="moba_MobaConstant185", type=moba_MobaMinConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaMinConstraint", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
filterConst186: BinaryAssociation = BinaryAssociation(
    name="filterConst186",
    ends={
        Property(name="moba_MobaConstant187", type=moba_MobaMaxConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaMaxConstraint", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
filterConst188: BinaryAssociation = BinaryAssociation(
    name="filterConst188",
    ends={
        Property(name="moba_MobaConstant189", type=moba_MobaMinLengthConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaMinLengthConstraint", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
type172: BinaryAssociation = BinaryAssociation(
    name="type172",
    ends={
        Property(name="moba_MobaDto173", type=moba_MobaDtoReference, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDtoReference", type=moba_MobaDto, multiplicity=Multiplicity(0, 1))
    }
)
opposite175: BinaryAssociation = BinaryAssociation(
    name="opposite175",
    ends={
        Property(name="moba_MobaDtoReference176", type=moba_MobaDtoReference, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDtoReference174", type=moba_MobaDtoReference, multiplicity=Multiplicity(0, 1))
    }
)
type177: BinaryAssociation = BinaryAssociation(
    name="type177",
    ends={
        Property(name="moba_MobaDto178", type=moba_MobaDtoEmbeddable, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDtoEmbeddable", type=moba_MobaDto, multiplicity=Multiplicity(0, 1))
    }
)
restService179: BinaryAssociation = BinaryAssociation(
    name="restService179",
    ends={
        Property(name="moba_MobaREST180", type=moba_MobaQueueReference, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaQueueReference", type=moba_MobaREST, multiplicity=Multiplicity(0, 1))
    }
)
constraints181: BinaryAssociation = BinaryAssociation(
    name="constraints181",
    ends={
        Property(name="moba_MobaConstraint", type=moba_MobaConstraintable, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaConstraintable", type=moba_MobaConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filterConst190: BinaryAssociation = BinaryAssociation(
    name="filterConst190",
    ends={
        Property(name="moba_MobaConstant191", type=moba_MobaMaxLengthConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaMaxLengthConstraint", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
filterIntegerConst192: BinaryAssociation = BinaryAssociation(
    name="filterIntegerConst192",
    ends={
        Property(name="moba_MobaConstant193", type=moba_MobaDigitsConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDigitsConstraint", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
filterFractionConst194: BinaryAssociation = BinaryAssociation(
    name="filterFractionConst194",
    ends={
        Property(name="moba_MobaConstant196", type=moba_MobaDigitsConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaDigitsConstraint195", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
literals197: BinaryAssociation = BinaryAssociation(
    name="literals197",
    ends={
        Property(name="moba_MobaEnumLiteral", type=moba_MobaEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaEnum198", type=moba_MobaEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType200: BinaryAssociation = BinaryAssociation(
    name="superType200",
    ends={
        Property(name="moba_MobaTrigger", type=moba_MobaTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaTrigger199", type=moba_MobaTrigger, multiplicity=Multiplicity(0, 1))
    }
)
valueConst201: BinaryAssociation = BinaryAssociation(
    name="valueConst201",
    ends={
        Property(name="moba_MobaConstant202", type=moba_MobaFriend, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaFriend", type=moba_MobaConstant, multiplicity=Multiplicity(0, 1))
    }
)
friends203: BinaryAssociation = BinaryAssociation(
    name="friends203",
    ends={
        Property(name="moba_MobaFriend204", type=moba_MobaFriendsAble, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaFriendsAble", type=moba_MobaFriend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType206: BinaryAssociation = BinaryAssociation(
    name="superType206",
    ends={
        Property(name="moba_MobaExternalModule", type=moba_MobaExternalModule, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_MobaExternalModule205", type=moba_MobaExternalModule, multiplicity=Multiplicity(0, 1))
    }
)
entries207: BinaryAssociation = BinaryAssociation(
    name="entries207",
    ends={
        Property(name="MobaIndexEntry", type=moba_index_MobaIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_index_MobaIndex", type=MobaIndexEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transientTemplate208: BinaryAssociation = BinaryAssociation(
    name="transientTemplate208",
    ends={
        Property(name="index_moba_MobaApplication", type=moba_index_MobaIndexEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="moba_index_MobaIndexEntry", type=index_moba_MobaApplication, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_moba_MobaModelFeature_MobaFriendsAble = Generalization(general=MobaFriendsAble, specific=moba_MobaModelFeature)
gen_moba_MobaProject_MobaModelFeature = Generalization(general=MobaModelFeature, specific=moba_MobaProject)
gen_moba_MobaApplication_MobaModelFeature = Generalization(general=MobaModelFeature, specific=moba_MobaApplication)
gen_moba_MobaModel_MobaFriendsAble = Generalization(general=MobaFriendsAble, specific=moba_MobaModel)
gen_moba_MobaGeneratorMixinFeature_MobaGeneratorFeature = Generalization(general=MobaGeneratorFeature, specific=moba_MobaGeneratorMixinFeature)
gen_moba_MobaGeneratorIDFeature_MobaGeneratorFeature = Generalization(general=MobaGeneratorFeature, specific=moba_MobaGeneratorIDFeature)
gen_moba_MobaGeneratorSlot_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaGeneratorSlot)
gen_moba_MobaDataType_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaDataType)
gen_moba_MobaDataType_MobaConstraintable = Generalization(general=MobaConstraintable, specific=moba_MobaDataType)
gen_moba_MobaApplicationFeature_MobaFriendsAble = Generalization(general=MobaFriendsAble, specific=moba_MobaApplicationFeature)
gen_moba_MobaTemplate_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaTemplate)
gen_moba_MobaServer_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaServer)
gen_moba_MobaAuthorization_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaAuthorization)
gen_moba_MobaTransportSerializationType_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaTransportSerializationType)
gen_moba_MobaPersistenceType_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaPersistenceType)
gen_moba_MobaGenerator_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaGenerator)
gen_moba_MobaConstant_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaConstant)
gen_moba_MobaCache_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaCache)
gen_moba_MobaSettingsEntityReference_MobaSettingsFeature = Generalization(general=MobaSettingsFeature, specific=moba_MobaSettingsEntityReference)
gen_moba_MobaSettingsEntityReference_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaSettingsEntityReference)
gen_moba_MobaSettingsEntityReference_MobaConstraintable = Generalization(general=MobaConstraintable, specific=moba_MobaSettingsEntityReference)
gen_moba_MobaEntity_MobaData = Generalization(general=MobaData, specific=moba_MobaEntity)
gen_moba_MobaData_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaData)
gen_moba_MobaSettings_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaSettings)
gen_moba_MobaSettingsFeature_MobaFeature = Generalization(general=MobaFeature, specific=moba_MobaSettingsFeature)
gen_moba_MobaSettingsAttribute_MobaSettingsFeature = Generalization(general=MobaSettingsFeature, specific=moba_MobaSettingsAttribute)
gen_moba_MobaSettingsAttribute_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaSettingsAttribute)
gen_moba_MobaSettingsAttribute_MobaConstraintable = Generalization(general=MobaConstraintable, specific=moba_MobaSettingsAttribute)
gen_moba_MobaDto_MobaData = Generalization(general=MobaData, specific=moba_MobaDto)
gen_moba_MobaQueue_MobaData = Generalization(general=MobaData, specific=moba_MobaQueue)
gen_moba_MobaREST_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaREST)
gen_moba_MobaRESTCustomService_MobaREST = Generalization(general=MobaREST, specific=moba_MobaRESTCustomService)
gen_moba_MobaRESTWorkflow_MobaREST = Generalization(general=MobaREST, specific=moba_MobaRESTWorkflow)
gen_moba_MobaRESTAttribute_MobaRESTAbstractAttribute = Generalization(general=MobaRESTAbstractAttribute, specific=moba_MobaRESTAttribute)
gen_moba_MobaRESTDtoAttribute_MobaRESTAbstractAttribute = Generalization(general=MobaRESTAbstractAttribute, specific=moba_MobaRESTDtoAttribute)
gen_moba_MobaEntityEmbeddable_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaEntityEmbeddable)
gen_moba_MobaDtoFeature_MobaFeature = Generalization(general=MobaFeature, specific=moba_MobaDtoFeature)
gen_moba_MobaDtoAttribute_MobaDtoFeature = Generalization(general=MobaDtoFeature, specific=moba_MobaDtoAttribute)
gen_moba_MobaDtoAttribute_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaDtoAttribute)
gen_moba_MobaDtoAttribute_MobaConstraintable = Generalization(general=MobaConstraintable, specific=moba_MobaDtoAttribute)
gen_moba_MobaDtoReference_MobaDtoFeature = Generalization(general=MobaDtoFeature, specific=moba_MobaDtoReference)
gen_moba_MobaDtoReference_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaDtoReference)
gen_moba_MobaRESTCrud_MobaREST = Generalization(general=MobaREST, specific=moba_MobaRESTCrud)
gen_moba_MobaFeature_MobaFriendsAble = Generalization(general=MobaFriendsAble, specific=moba_MobaFeature)
gen_moba_MobaEntityFeature_MobaFeature = Generalization(general=MobaFeature, specific=moba_MobaEntityFeature)
gen_moba_MobaEntityAttribute_MobaEntityFeature = Generalization(general=MobaEntityFeature, specific=moba_MobaEntityAttribute)
gen_moba_MobaEntityAttribute_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaEntityAttribute)
gen_moba_MobaEntityAttribute_MobaConstraintable = Generalization(general=MobaConstraintable, specific=moba_MobaEntityAttribute)
gen_moba_MobaEntityReference_MobaEntityFeature = Generalization(general=MobaEntityFeature, specific=moba_MobaEntityReference)
gen_moba_MobaEntityReference_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaEntityReference)
gen_moba_MobaEntityEmbeddable_MobaEntityFeature = Generalization(general=MobaEntityFeature, specific=moba_MobaEntityEmbeddable)
gen_moba_MobaMinConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaMinConstraint)
gen_moba_MobaMaxConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaMaxConstraint)
gen_moba_MobaFutureConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaFutureConstraint)
gen_moba_MobaPastConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaPastConstraint)
gen_moba_MobaNotNullConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaNotNullConstraint)
gen_moba_MobaNullConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaNullConstraint)
gen_moba_MobaMinLengthConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaMinLengthConstraint)
gen_moba_MobaDtoEmbeddable_MobaDtoFeature = Generalization(general=MobaDtoFeature, specific=moba_MobaDtoEmbeddable)
gen_moba_MobaDtoEmbeddable_MobaMultiplicityAble = Generalization(general=MobaMultiplicityAble, specific=moba_MobaDtoEmbeddable)
gen_moba_MobaQueueFeature_MobaFeature = Generalization(general=MobaFeature, specific=moba_MobaQueueFeature)
gen_moba_MobaQueueReference_MobaQueueFeature = Generalization(general=MobaQueueFeature, specific=moba_MobaQueueReference)
gen_moba_MobaRegexpConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaRegexpConstraint)
gen_moba_MobaAppInstallTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaAppInstallTrigger)
gen_moba_MobaAppUpdateTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaAppUpdateTrigger)
gen_moba_MobaSMSTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaSMSTrigger)
gen_moba_MobaDeviceStartupTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaDeviceStartupTrigger)
gen_moba_MobaEmailTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaEmailTrigger)
gen_moba_MobaTimerTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaTimerTrigger)
gen_moba_MobaPushTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaPushTrigger)
gen_moba_MobaGeofenceTrigger_MobaTrigger = Generalization(general=MobaTrigger, specific=moba_MobaGeofenceTrigger)
gen_moba_MobaMaxLengthConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaMaxLengthConstraint)
gen_moba_MobaDigitsConstraint_MobaConstraint = Generalization(general=MobaConstraint, specific=moba_MobaDigitsConstraint)
gen_moba_MobaEnum_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaEnum)
gen_moba_MobaTrigger_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaTrigger)
gen_moba_MobaFriendsAble_MobaPropertiesAble = Generalization(general=MobaPropertiesAble, specific=moba_MobaFriendsAble)
gen_moba_MobaExternalModule_MobaApplicationFeature = Generalization(general=MobaApplicationFeature, specific=moba_MobaExternalModule)
gen_moba_MobaBluetoothModule_MobaExternalModule = Generalization(general=MobaExternalModule, specific=moba_MobaBluetoothModule)
gen_moba_MobaNFCModule_MobaExternalModule = Generalization(general=MobaExternalModule, specific=moba_MobaNFCModule)
gen_moba_MobaPushModule_MobaExternalModule = Generalization(general=MobaExternalModule, specific=moba_MobaPushModule)

# Domain Model
domain_model = DomainModel(
    name="moba",
    types={moba_MobaModelFeature, moba_MobaProject, MobaModelFeature, moba_MobaApplication, moba_MobaCache, moba_MobaModel, MobaFriendsAble, moba_MobaGeneratorMixinFeature, MobaGeneratorFeature, moba_MobaGeneratorIDFeature, moba_MobaGeneratorSlot, moba_MobaDataType, MobaConstraintable, moba_MobaApplicationFeature, moba_MobaTemplate, MobaApplicationFeature, moba_MobaServer, moba_MobaConstant, moba_MobaREST, moba_MobaAuthorization, moba_MobaTransportSerializationType, moba_MobaPersistenceType, moba_MobaGenerator, moba_MobaGeneratorFeature, moba_MobaPropertiesAble, moba_MobaProperty, moba_MobaEnum, moba_MobaConstantValue, moba_MobaEntity, MobaData, moba_MobaData, moba_MobaSettings, moba_MobaSettingsFeature, MobaFeature, moba_MobaSettingsAttribute, MobaSettingsFeature, MobaMultiplicityAble, moba_MobaSettingsEntityReference, moba_MobaRESTHeader, moba_MobaEntityFeature, moba_MobaEntityIndex, moba_MobaEntityAttribute, moba_MobaDto, moba_MobaDtoFeature, moba_MobaQueue, moba_MobaQueueFeature, moba_MobaRESTPayloadDefinition, moba_MobaRESTCustomService, MobaREST, moba_MobaRESTWorkflow, moba_MobaRESTAbstractAttribute, moba_MobaRESTAttribute, MobaRESTAbstractAttribute, moba_MobaRESTDtoAttribute, moba_MobaDtoAttribute, MobaDtoFeature, moba_MobaDtoReference, moba_MobaRESTCrud, moba_MobaFeature, MobaEntityFeature, moba_MobaMultiplicityAble, moba_MobaMuliplicity, moba_MobaEntityReference, moba_MobaEntityEmbeddable, moba_MobaMinConstraint, moba_MobaMaxConstraint, moba_MobaFutureConstraint, moba_MobaPastConstraint, moba_MobaNotNullConstraint, moba_MobaNullConstraint, moba_MobaMinLengthConstraint, moba_MobaDtoEmbeddable, moba_MobaQueueReference, MobaQueueFeature, moba_MobaConstraintable, moba_MobaConstraint, moba_MobaRegexpConstraint, MobaConstraint, moba_MobaAppInstallTrigger, MobaTrigger, moba_MobaAppUpdateTrigger, moba_MobaSMSTrigger, moba_MobaDeviceStartupTrigger, moba_MobaEmailTrigger, moba_MobaTimerTrigger, moba_MobaPushTrigger, moba_MobaGeofenceTrigger, moba_MobaMaxLengthConstraint, moba_MobaDigitsConstraint, moba_MobaEnumLiteral, moba_MobaTrigger, moba_index_MobaIndex, moba_MobaFriend, moba_MobaFriendsAble, MobaPropertiesAble, moba_MobaExternalModule, moba_MobaBluetoothModule, MobaExternalModule, moba_MobaNFCModule, moba_MobaPushModule, MobaIndexEntry, moba_index_MobaIndexEntry, index_moba_MobaApplication, MobaConstantValueFunction, MobaRESTMethods, MobaLowerBound, MobaUpperBound, MobaNFCModuleType, MobaBlueToothModuleType, MobaGeofenceEvent},
    associations={features0, uiApplication1, backgroundApplication2, defaultCache5, generatorRef20, superType23, features7, template9, urlConst11, superType13, services15, authorization17, features19, properties50, enumAST24, dateFormatConst25, superType29, valueAST31, cacheTypeConst33, cacheStrategyConst36, cacheIntervalConst39, cachePersistence42, valueConst44, tail48, type66, superType68, cache70, keyConst51, valueConst54, superType58, features59, type61, formatConst63, errorDto100, contextDto103, headers106, authorization108, dto111, serializationType114, features73, indizes75, attributes77, superType80, wrappedEntity81, features84, serializationType86, superType89, cache90, features93, requestDto95, responseDto97, valueConst135, parameters138, superType141, multipartParameters143, services146, aliasConst117, type119, keyConst121, valueConst124, formatConst127, dtoFeature130, keyConst132, type165, type167, formatConst169, superType149, superType152, type153, formatConst156, multiplicity159, type160, opposite163, filterConst182, filterConst184, filterConst186, filterConst188, type172, opposite175, type177, restService179, constraints181, filterConst190, filterIntegerConst192, filterFractionConst194, literals197, superType200, valueConst201, friends203, superType206, entries207, transientTemplate208},
    generalizations={gen_moba_MobaModelFeature_MobaFriendsAble, gen_moba_MobaProject_MobaModelFeature, gen_moba_MobaApplication_MobaModelFeature, gen_moba_MobaModel_MobaFriendsAble, gen_moba_MobaGeneratorMixinFeature_MobaGeneratorFeature, gen_moba_MobaGeneratorIDFeature_MobaGeneratorFeature, gen_moba_MobaGeneratorSlot_MobaApplicationFeature, gen_moba_MobaDataType_MobaApplicationFeature, gen_moba_MobaDataType_MobaConstraintable, gen_moba_MobaApplicationFeature_MobaFriendsAble, gen_moba_MobaTemplate_MobaApplicationFeature, gen_moba_MobaServer_MobaApplicationFeature, gen_moba_MobaAuthorization_MobaApplicationFeature, gen_moba_MobaTransportSerializationType_MobaApplicationFeature, gen_moba_MobaPersistenceType_MobaApplicationFeature, gen_moba_MobaGenerator_MobaApplicationFeature, gen_moba_MobaConstant_MobaApplicationFeature, gen_moba_MobaCache_MobaApplicationFeature, gen_moba_MobaSettingsEntityReference_MobaSettingsFeature, gen_moba_MobaSettingsEntityReference_MobaMultiplicityAble, gen_moba_MobaSettingsEntityReference_MobaConstraintable, gen_moba_MobaEntity_MobaData, gen_moba_MobaData_MobaApplicationFeature, gen_moba_MobaSettings_MobaApplicationFeature, gen_moba_MobaSettingsFeature_MobaFeature, gen_moba_MobaSettingsAttribute_MobaSettingsFeature, gen_moba_MobaSettingsAttribute_MobaMultiplicityAble, gen_moba_MobaSettingsAttribute_MobaConstraintable, gen_moba_MobaDto_MobaData, gen_moba_MobaQueue_MobaData, gen_moba_MobaREST_MobaApplicationFeature, gen_moba_MobaRESTCustomService_MobaREST, gen_moba_MobaRESTWorkflow_MobaREST, gen_moba_MobaRESTAttribute_MobaRESTAbstractAttribute, gen_moba_MobaRESTDtoAttribute_MobaRESTAbstractAttribute, gen_moba_MobaEntityEmbeddable_MobaMultiplicityAble, gen_moba_MobaDtoFeature_MobaFeature, gen_moba_MobaDtoAttribute_MobaDtoFeature, gen_moba_MobaDtoAttribute_MobaMultiplicityAble, gen_moba_MobaDtoAttribute_MobaConstraintable, gen_moba_MobaDtoReference_MobaDtoFeature, gen_moba_MobaDtoReference_MobaMultiplicityAble, gen_moba_MobaRESTCrud_MobaREST, gen_moba_MobaFeature_MobaFriendsAble, gen_moba_MobaEntityFeature_MobaFeature, gen_moba_MobaEntityAttribute_MobaEntityFeature, gen_moba_MobaEntityAttribute_MobaMultiplicityAble, gen_moba_MobaEntityAttribute_MobaConstraintable, gen_moba_MobaEntityReference_MobaEntityFeature, gen_moba_MobaEntityReference_MobaMultiplicityAble, gen_moba_MobaEntityEmbeddable_MobaEntityFeature, gen_moba_MobaMinConstraint_MobaConstraint, gen_moba_MobaMaxConstraint_MobaConstraint, gen_moba_MobaFutureConstraint_MobaConstraint, gen_moba_MobaPastConstraint_MobaConstraint, gen_moba_MobaNotNullConstraint_MobaConstraint, gen_moba_MobaNullConstraint_MobaConstraint, gen_moba_MobaMinLengthConstraint_MobaConstraint, gen_moba_MobaDtoEmbeddable_MobaDtoFeature, gen_moba_MobaDtoEmbeddable_MobaMultiplicityAble, gen_moba_MobaQueueFeature_MobaFeature, gen_moba_MobaQueueReference_MobaQueueFeature, gen_moba_MobaRegexpConstraint_MobaConstraint, gen_moba_MobaAppInstallTrigger_MobaTrigger, gen_moba_MobaAppUpdateTrigger_MobaTrigger, gen_moba_MobaSMSTrigger_MobaTrigger, gen_moba_MobaDeviceStartupTrigger_MobaTrigger, gen_moba_MobaEmailTrigger_MobaTrigger, gen_moba_MobaTimerTrigger_MobaTrigger, gen_moba_MobaPushTrigger_MobaTrigger, gen_moba_MobaGeofenceTrigger_MobaTrigger, gen_moba_MobaMaxLengthConstraint_MobaConstraint, gen_moba_MobaDigitsConstraint_MobaConstraint, gen_moba_MobaEnum_MobaApplicationFeature, gen_moba_MobaTrigger_MobaApplicationFeature, gen_moba_MobaFriendsAble_MobaPropertiesAble, gen_moba_MobaExternalModule_MobaApplicationFeature, gen_moba_MobaBluetoothModule_MobaExternalModule, gen_moba_MobaNFCModule_MobaExternalModule, gen_moba_MobaPushModule_MobaExternalModule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)