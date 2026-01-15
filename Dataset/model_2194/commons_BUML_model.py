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
ResourceType: Enumeration = Enumeration(
    name="ResourceType",
    literals={
            EnumerationLiteral(name="bundle"),
			EnumerationLiteral(name="file"),
			EnumerationLiteral(name="database"),
			EnumerationLiteral(name="classpath")
    }
)

Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="unknown"),
			EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

EClassStatus: Enumeration = Enumeration(
    name="EClassStatus",
    literals={
            EnumerationLiteral(name="unresolved"),
			EnumerationLiteral(name="resolved")
    }
)

JavaClassStatus: Enumeration = Enumeration(
    name="JavaClassStatus",
    literals={
            EnumerationLiteral(name="unresolved"),
			EnumerationLiteral(name="resolved")
    }
)

ProgressStatus: Enumeration = Enumeration(
    name="ProgressStatus",
    literals={
            EnumerationLiteral(name="ok"),
			EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="deleted"),
			EnumerationLiteral(name="skipped")
    }
)

AccountStatus: Enumeration = Enumeration(
    name="AccountStatus",
    literals={
            EnumerationLiteral(name="draft"),
			EnumerationLiteral(name="validated"),
			EnumerationLiteral(name="active"),
			EnumerationLiteral(name="verified"),
			EnumerationLiteral(name="inactive"),
			EnumerationLiteral(name="void"),
			EnumerationLiteral(name="unregister")
    }
)

ArchivalStatus: Enumeration = Enumeration(
    name="ArchivalStatus",
    literals={
            EnumerationLiteral(name="fresh"),
			EnumerationLiteral(name="archived")
    }
)

PublicationStatus: Enumeration = Enumeration(
    name="PublicationStatus",
    literals={
            EnumerationLiteral(name="draft"),
			EnumerationLiteral(name="published"),
			EnumerationLiteral(name="unpublished")
    }
)

TranslationState: Enumeration = Enumeration(
    name="TranslationState",
    literals={
            EnumerationLiteral(name="original"),
			EnumerationLiteral(name="translated")
    }
)

ExpansionState: Enumeration = Enumeration(
    name="ExpansionState",
    literals={
            EnumerationLiteral(name="expanded"),
			EnumerationLiteral(name="unexpanded")
    }
)

SignupSourceType: Enumeration = Enumeration(
    name="SignupSourceType",
    literals={
            EnumerationLiteral(name="other"),
			EnumerationLiteral(name="google_search"),
			EnumerationLiteral(name="google_ads"),
			EnumerationLiteral(name="facebook_ads"),
			EnumerationLiteral(name="facebook_friend"),
			EnumerationLiteral(name="alia_magazine")
    }
)

TenantSource: Enumeration = Enumeration(
    name="TenantSource",
    literals={
            EnumerationLiteral(name="config"),
			EnumerationLiteral(name="repository"),
			EnumerationLiteral(name="classpath")
    }
)

GenericStatus: Enumeration = Enumeration(
    name="GenericStatus",
    literals={
            EnumerationLiteral(name="booked"),
			EnumerationLiteral(name="draft"),
			EnumerationLiteral(name="inactive"),
			EnumerationLiteral(name="void")
    }
)

CustomerRoleStatus: Enumeration = Enumeration(
    name="CustomerRoleStatus",
    literals={
            EnumerationLiteral(name="active"),
			EnumerationLiteral(name="inactive"),
			EnumerationLiteral(name="void")
    }
)

EntityKind: Enumeration = Enumeration(
    name="EntityKind",
    literals={
            EnumerationLiteral(name="category"),
			EnumerationLiteral(name="product_release"),
			EnumerationLiteral(name="tag"),
			EnumerationLiteral(name="page"),
			EnumerationLiteral(name="person"),
			EnumerationLiteral(name="shop"),
			EnumerationLiteral(name="product"),
			EnumerationLiteral(name="place"),
			EnumerationLiteral(name="task"),
			EnumerationLiteral(name="article"),
			EnumerationLiteral(name="banner_shop")
    }
)

# Classes
commons_Positionable = Class(name="commons::Positionable", is_abstract=True)
commons_AppManifest = Class(name="commons::AppManifest")
Positionable = Class(name="Positionable")
ResourceAware = Class(name="ResourceAware")
BundleAware = Class(name="BundleAware")
Expandable = Class(name="Expandable")
commons_ResourceAware = Class(name="commons::ResourceAware", is_abstract=True)
commons_Timestamped = Class(name="commons::Timestamped", is_abstract=True)
commons_PersonInfo = Class(name="commons::PersonInfo")
Identifiable = Class(name="Identifiable")
PhotoIdContainer = Class(name="PhotoIdContainer")
Sluggable = Class(name="Sluggable")
NameContainer = Class(name="NameContainer")
PersonLike = Class(name="PersonLike")
commons_Nameable = Class(name="commons::Nameable", is_abstract=True)
commons_Imageable = Class(name="commons::Imageable", is_abstract=True)
commons_Identifiable = Class(name="commons::Identifiable", is_abstract=True)
commons_Sluggable = Class(name="commons::Sluggable", is_abstract=True)
commons_JavaClassLinked = Class(name="commons::JavaClassLinked", is_abstract=True)
commons_PhotoIdContainer = Class(name="commons::PhotoIdContainer", is_abstract=True)
Imageable = Class(name="Imageable")
commons_NameContainer = Class(name="commons::NameContainer", is_abstract=True)
Nameable = Class(name="Nameable")
commons_Informer = Class(name="commons::Informer", is_abstract=True)
commons_Describable = Class(name="commons::Describable", is_abstract=True)
commons_BundleAware = Class(name="commons::BundleAware", is_abstract=True)
commons_EClassLinked = Class(name="commons::EClassLinked", is_abstract=True)
commons_EClass = Class(name="commons::EClass")
commons_SchemaVersionable = Class(name="commons::SchemaVersionable", is_abstract=True)
commons_EFactoryLinked = Class(name="commons::EFactoryLinked", is_abstract=True)
commons_NsPrefixable = Class(name="commons::NsPrefixable", is_abstract=True)
commons_WebAddress = Class(name="commons::WebAddress")
commons_AttributeSet = Class(name="commons::AttributeSet")
commons_Added = Class(name="commons::Added")
commons_ModelNotification = Class(name="commons::ModelNotification", is_abstract=True)
commons_EObject = Class(name="commons::EObject")
commons_Parentable = Class(name="commons::Parentable", is_abstract=True)
commons_CategoryLike = Class(name="commons::CategoryLike", is_abstract=True)
NsPrefixable = Class(name="NsPrefixable")
commons_AttributeUnset = Class(name="commons::AttributeUnset")
commons_Removed = Class(name="commons::Removed")
commons_ObjectNotification = Class(name="commons::ObjectNotification", is_abstract=True)
commons_AttributeNotification = Class(name="commons::AttributeNotification")
commons_EAttribute = Class(name="commons::EAttribute")
commons_AddedMany = Class(name="commons::AddedMany")
commons_RemovedMany = Class(name="commons::RemovedMany")
commons_ObjectsNotification = Class(name="commons::ObjectsNotification", is_abstract=True)
commons_EObjectLinked = Class(name="commons::EObjectLinked", is_abstract=True)
commons_CategoryInfo = Class(name="commons::CategoryInfo")
commons_ProgressMonitor = Class(name="commons::ProgressMonitor", is_abstract=True)
commons_ProgressMonitorWrapper = Class(name="commons::ProgressMonitorWrapper")
commons_ShellProgressMonitor = Class(name="commons::ShellProgressMonitor")
ProgressMonitor = Class(name="ProgressMonitor")
commons_EventBusProgressMonitor = Class(name="commons::EventBusProgressMonitor")
commons_Colorable = Class(name="commons::Colorable", is_abstract=True)
commons_TranslationMessageEntry = Class(name="commons::TranslationMessageEntry")
commons_TranslationManager = Class(name="commons::TranslationManager")
commons_Translatable = Class(name="commons::Translatable", is_abstract=True)
commons_TranslationEntry = Class(name="commons::TranslationEntry")
commons_Translation = Class(name="commons::Translation")
commons_PersonLike = Class(name="commons::PersonLike", is_abstract=True)
commons_StyleConfiguration = Class(name="commons::StyleConfiguration", is_abstract=True)
commons_Expandable = Class(name="commons::Expandable", is_abstract=True)
commons_Person = Class(name="commons::Person")
commons_PhoneNumber = Class(name="commons::PhoneNumber")
commons_Email = Class(name="commons::Email")
commons_PostalAddress = Class(name="commons::PostalAddress")
SchemaVersionable = Class(name="SchemaVersionable")
commons_Organization = Class(name="commons::Organization")
commons_PersonCatalog = Class(name="commons::PersonCatalog")
commons_CanonicalSluggable = Class(name="commons::CanonicalSluggable", is_abstract=True)
commons_SysConfig = Class(name="commons::SysConfig", is_abstract=True)
commons_TwitterAccessible = Class(name="commons::TwitterAccessible", is_abstract=True)
commons_TwitterIdentity = Class(name="commons::TwitterIdentity", is_abstract=True)
commons_FacebookIdentity = Class(name="commons::FacebookIdentity")
commons_FacebookAccessible = Class(name="commons::FacebookAccessible")
commons_Revisionable = Class(name="commons::Revisionable", is_abstract=True)
commons_GeneralSysConfig = Class(name="commons::GeneralSysConfig", is_abstract=True)
SysConfig = Class(name="SysConfig")
Timestamped = Class(name="Timestamped")
commons_Geolocation = Class(name="commons::Geolocation")
commons_ThingInfo = Class(name="commons::ThingInfo")
commons_CustomerRole = Class(name="commons::CustomerRole")
Describable = Class(name="Describable")
commons_MongoSysConfig = Class(name="commons::MongoSysConfig", is_abstract=True)

# commons_Positionable class attributes and methods
commons_Positionable_positioner: Property = Property(name="positioner", type=StringType)
commons_Positionable.attributes={commons_Positionable_positioner}

# commons_AppManifest class attributes and methods
commons_AppManifest_defaultTimeZone: Property = Property(name="defaultTimeZone", type=StringType)
commons_AppManifest_defaultCurrencyCode: Property = Property(name="defaultCurrencyCode", type=StringType)
commons_AppManifest_title: Property = Property(name="title", type=StringType)
commons_AppManifest_summary: Property = Property(name="summary", type=StringType)
commons_AppManifest_description: Property = Property(name="description", type=StringType)
commons_AppManifest_domain: Property = Property(name="domain", type=StringType)
commons_AppManifest_domainPrd: Property = Property(name="domainPrd", type=StringType)
commons_AppManifest_domainDev: Property = Property(name="domainDev", type=StringType)
commons_AppManifest_domainStg: Property = Property(name="domainStg", type=StringType)
commons_AppManifest_generalEmail: Property = Property(name="generalEmail", type=StringType)
commons_AppManifest_generalEmailPrd: Property = Property(name="generalEmailPrd", type=StringType)
commons_AppManifest_generalEmailDev: Property = Property(name="generalEmailDev", type=StringType)
commons_AppManifest_generalEmailStg: Property = Property(name="generalEmailStg", type=StringType)
commons_AppManifest_organizationName: Property = Property(name="organizationName", type=StringType)
commons_AppManifest_organizationAddress: Property = Property(name="organizationAddress", type=StringType)
commons_AppManifest_organizationPhoneNumbers: Property = Property(name="organizationPhoneNumbers", type=StringType)
commons_AppManifest_defaultTimeZoneId: Property = Property(name="defaultTimeZoneId", type=StringType)
commons_AppManifest_reminderSchedule: Property = Property(name="reminderSchedule", type=StringType)
commons_AppManifest_reminderPeriodStr: Property = Property(name="reminderPeriodStr", type=StringType)
commons_AppManifest_defaultCurrency: Property = Property(name="defaultCurrency", type=StringType)
commons_AppManifest_defaultLanguageTag: Property = Property(name="defaultLanguageTag", type=StringType)
commons_AppManifest_defaultCountryCode: Property = Property(name="defaultCountryCode", type=StringType)
commons_AppManifest_defaultCategoryUName: Property = Property(name="defaultCategoryUName", type=StringType)
commons_AppManifest_emailLogoUriTemplate: Property = Property(name="emailLogoUriTemplate", type=StringType)
commons_AppManifest_letterSalutation: Property = Property(name="letterSalutation", type=StringType)
commons_AppManifest_letterClosing: Property = Property(name="letterClosing", type=StringType)
commons_AppManifest_footnote: Property = Property(name="footnote", type=StringType)
commons_AppManifest_wwwUsed: Property = Property(name="wwwUsed", type=StringType)
commons_AppManifest_headNote: Property = Property(name="headNote", type=StringType)
commons_AppManifest_headTitle: Property = Property(name="headTitle", type=StringType)
commons_AppManifest_defaultStyle: Property = Property(name="defaultStyle", type=StringType)
commons_AppManifest_defaultVariation: Property = Property(name="defaultVariation", type=StringType)
commons_AppManifest_kursDollarPaypal: Property = Property(name="kursDollarPaypal", type=StringType)
commons_AppManifest_kursDollarDpex: Property = Property(name="kursDollarDpex", type=StringType)
commons_AppManifest_reminderPeriod: Property = Property(name="reminderPeriod", type=StringType)
commons_AppManifest_reminderScheduleStr: Property = Property(name="reminderScheduleStr", type=StringType)
commons_AppManifest_supportEmail: Property = Property(name="supportEmail", type=StringType)
commons_AppManifest_shipmentLogoUriTemplate: Property = Property(name="shipmentLogoUriTemplate", type=StringType)
commons_AppManifest_m_getDefaultLocale: Method = Method(name="getDefaultLocale", parameters={}, type=StringType)
commons_AppManifest_m_getWebHost: Method = Method(name="getWebHost", parameters={}, type=StringType)
commons_AppManifest.attributes={commons_AppManifest_letterClosing, commons_AppManifest_reminderScheduleStr, commons_AppManifest_defaultCurrencyCode, commons_AppManifest_summary, commons_AppManifest_reminderPeriod, commons_AppManifest_defaultTimeZone, commons_AppManifest_defaultCategoryUName, commons_AppManifest_domainDev, commons_AppManifest_headNote, commons_AppManifest_domainStg, commons_AppManifest_organizationPhoneNumbers, commons_AppManifest_generalEmailPrd, commons_AppManifest_generalEmailStg, commons_AppManifest_reminderSchedule, commons_AppManifest_defaultStyle, commons_AppManifest_title, commons_AppManifest_defaultLanguageTag, commons_AppManifest_defaultCountryCode, commons_AppManifest_generalEmail, commons_AppManifest_generalEmailDev, commons_AppManifest_shipmentLogoUriTemplate, commons_AppManifest_defaultTimeZoneId, commons_AppManifest_domainPrd, commons_AppManifest_kursDollarDpex, commons_AppManifest_defaultVariation, commons_AppManifest_letterSalutation, commons_AppManifest_defaultCurrency, commons_AppManifest_organizationName, commons_AppManifest_domain, commons_AppManifest_emailLogoUriTemplate, commons_AppManifest_kursDollarPaypal, commons_AppManifest_reminderPeriodStr, commons_AppManifest_organizationAddress, commons_AppManifest_headTitle, commons_AppManifest_footnote, commons_AppManifest_description, commons_AppManifest_wwwUsed, commons_AppManifest_supportEmail}
commons_AppManifest.methods={commons_AppManifest_m_getDefaultLocale, commons_AppManifest_m_getWebHost}

# Positionable class attributes and methods

# ResourceAware class attributes and methods

# BundleAware class attributes and methods

# Expandable class attributes and methods

# commons_ResourceAware class attributes and methods
commons_ResourceAware_resourceType: Property = Property(name="resourceType", type=StringType)
commons_ResourceAware_resourceUri: Property = Property(name="resourceUri", type=StringType)
commons_ResourceAware_resourceName: Property = Property(name="resourceName", type=StringType)
commons_ResourceAware.attributes={commons_ResourceAware_resourceUri, commons_ResourceAware_resourceName, commons_ResourceAware_resourceType}

# commons_Timestamped class attributes and methods
commons_Timestamped_creationTime: Property = Property(name="creationTime", type=StringType)
commons_Timestamped_modificationTime: Property = Property(name="modificationTime", type=StringType)
commons_Timestamped.attributes={commons_Timestamped_creationTime, commons_Timestamped_modificationTime}

# commons_PersonInfo class attributes and methods
commons_PersonInfo_gender: Property = Property(name="gender", type=StringType)
commons_PersonInfo_email: Property = Property(name="email", type=StringType)
commons_PersonInfo_mobileNumber: Property = Property(name="mobileNumber", type=StringType)
commons_PersonInfo.attributes={commons_PersonInfo_email, commons_PersonInfo_gender, commons_PersonInfo_mobileNumber}

# Identifiable class attributes and methods

# PhotoIdContainer class attributes and methods

# Sluggable class attributes and methods

# NameContainer class attributes and methods

# PersonLike class attributes and methods

# commons_Nameable class attributes and methods
commons_Nameable_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
commons_Nameable.methods={commons_Nameable_m_getName}

# commons_Imageable class attributes and methods
commons_Imageable_m_getImageId: Method = Method(name="getImageId", parameters={}, type=StringType)
commons_Imageable.methods={commons_Imageable_m_getImageId}

# commons_Identifiable class attributes and methods
commons_Identifiable_id: Property = Property(name="id", type=StringType)
commons_Identifiable.attributes={commons_Identifiable_id}

# commons_Sluggable class attributes and methods
commons_Sluggable_slug: Property = Property(name="slug", type=StringType)
commons_Sluggable.attributes={commons_Sluggable_slug}

# commons_JavaClassLinked class attributes and methods
commons_JavaClassLinked_javaClassName: Property = Property(name="javaClassName", type=StringType)
commons_JavaClassLinked_javaClass: Property = Property(name="javaClass", type=StringType)
commons_JavaClassLinked_javaClassStatus: Property = Property(name="javaClassStatus", type=StringType)
commons_JavaClassLinked_m_resolveJavaClass: Method = Method(name="resolveJavaClass", parameters={Parameter(name='bundle')})
commons_JavaClassLinked.attributes={commons_JavaClassLinked_javaClassName, commons_JavaClassLinked_javaClass, commons_JavaClassLinked_javaClassStatus}
commons_JavaClassLinked.methods={commons_JavaClassLinked_m_resolveJavaClass}

# commons_PhotoIdContainer class attributes and methods
commons_PhotoIdContainer_photoId: Property = Property(name="photoId", type=StringType)
commons_PhotoIdContainer.attributes={commons_PhotoIdContainer_photoId}

# Imageable class attributes and methods

# commons_NameContainer class attributes and methods
commons_NameContainer_name: Property = Property(name="name", type=StringType)
commons_NameContainer.attributes={commons_NameContainer_name}

# Nameable class attributes and methods

# commons_Informer class attributes and methods
commons_Informer_m_toInfo: Method = Method(name="toInfo", parameters={})
commons_Informer.methods={commons_Informer_m_toInfo}

# commons_Describable class attributes and methods
commons_Describable_description: Property = Property(name="description", type=StringType)
commons_Describable.attributes={commons_Describable_description}

# commons_BundleAware class attributes and methods
commons_BundleAware_bundle: Property = Property(name="bundle", type=StringType)
commons_BundleAware.attributes={commons_BundleAware_bundle}

# commons_EClassLinked class attributes and methods
commons_EClassLinked_eClassName: Property = Property(name="eClassName", type=StringType)
commons_EClassLinked_ePackageName: Property = Property(name="ePackageName", type=StringType)
commons_EClassLinked_eClassStatus: Property = Property(name="eClassStatus", type=StringType)
commons_EClassLinked_ePackageNsPrefix: Property = Property(name="ePackageNsPrefix", type=StringType)
commons_EClassLinked_m_resolveEClass: Method = Method(name="resolveEClass", parameters={Parameter(name='eClassMap')})
commons_EClassLinked.attributes={commons_EClassLinked_eClassStatus, commons_EClassLinked_ePackageNsPrefix, commons_EClassLinked_ePackageName, commons_EClassLinked_eClassName}
commons_EClassLinked.methods={commons_EClassLinked_m_resolveEClass}

# commons_EClass class attributes and methods

# commons_SchemaVersionable class attributes and methods
commons_SchemaVersionable_m_getSchemaVersion: Method = Method(name="getSchemaVersion", parameters={}, type=StringType)
commons_SchemaVersionable.methods={commons_SchemaVersionable_m_getSchemaVersion}

# commons_EFactoryLinked class attributes and methods
commons_EFactoryLinked_eFactory: Property = Property(name="eFactory", type=StringType)
commons_EFactoryLinked.attributes={commons_EFactoryLinked_eFactory}

# commons_NsPrefixable class attributes and methods
commons_NsPrefixable_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
commons_NsPrefixable.attributes={commons_NsPrefixable_nsPrefix}

# commons_WebAddress class attributes and methods
commons_WebAddress_apiPath: Property = Property(name="apiPath", type=StringType)
commons_WebAddress_imagesUri: Property = Property(name="imagesUri", type=StringType)
commons_WebAddress_baseUri: Property = Property(name="baseUri", type=StringType)
commons_WebAddress_basePath: Property = Property(name="basePath", type=StringType)
commons_WebAddress_skinUri: Property = Property(name="skinUri", type=StringType)
commons_WebAddress_jsUri: Property = Property(name="jsUri", type=StringType)
commons_WebAddress_secureBaseUri: Property = Property(name="secureBaseUri", type=StringType)
commons_WebAddress_secureImagesUri: Property = Property(name="secureImagesUri", type=StringType)
commons_WebAddress_secureSkinUri: Property = Property(name="secureSkinUri", type=StringType)
commons_WebAddress_secureJsUri: Property = Property(name="secureJsUri", type=StringType)
commons_WebAddress_m_getApiUri: Method = Method(name="getApiUri", parameters={}, type=StringType)
commons_WebAddress_m_getSecureApiUri: Method = Method(name="getSecureApiUri", parameters={}, type=StringType)
commons_WebAddress.attributes={commons_WebAddress_secureImagesUri, commons_WebAddress_apiPath, commons_WebAddress_skinUri, commons_WebAddress_basePath, commons_WebAddress_imagesUri, commons_WebAddress_secureBaseUri, commons_WebAddress_secureJsUri, commons_WebAddress_secureSkinUri, commons_WebAddress_jsUri, commons_WebAddress_baseUri}
commons_WebAddress.methods={commons_WebAddress_m_getSecureApiUri, commons_WebAddress_m_getApiUri}

# commons_AttributeSet class attributes and methods
commons_AttributeSet_principals: Property = Property(name="principals", type=StringType)
commons_AttributeSet.attributes={commons_AttributeSet_principals}

# commons_Added class attributes and methods

# commons_ModelNotification class attributes and methods

# commons_EObject class attributes and methods

# commons_Parentable class attributes and methods

# commons_CategoryLike class attributes and methods
commons_CategoryLike_slugPath: Property = Property(name="slugPath", type=StringType)
commons_CategoryLike_color: Property = Property(name="color", type=StringType)
commons_CategoryLike_imageId: Property = Property(name="imageId", type=StringType)
commons_CategoryLike_level: Property = Property(name="level", type=StringType)
commons_CategoryLike_categoryCount: Property = Property(name="categoryCount", type=StringType)
commons_CategoryLike.attributes={commons_CategoryLike_imageId, commons_CategoryLike_slugPath, commons_CategoryLike_level, commons_CategoryLike_categoryCount, commons_CategoryLike_color}

# NsPrefixable class attributes and methods

# commons_AttributeUnset class attributes and methods

# commons_Removed class attributes and methods

# commons_ObjectNotification class attributes and methods
commons_ObjectNotification_object: Property = Property(name="object", type=StringType)
commons_ObjectNotification.attributes={commons_ObjectNotification_object}

# commons_AttributeNotification class attributes and methods
commons_AttributeNotification_object: Property = Property(name="object", type=StringType)
commons_AttributeNotification_oldValue: Property = Property(name="oldValue", type=StringType)
commons_AttributeNotification_newValue: Property = Property(name="newValue", type=StringType)
commons_AttributeNotification.attributes={commons_AttributeNotification_newValue, commons_AttributeNotification_object, commons_AttributeNotification_oldValue}

# commons_EAttribute class attributes and methods

# commons_AddedMany class attributes and methods

# commons_RemovedMany class attributes and methods

# commons_ObjectsNotification class attributes and methods
commons_ObjectsNotification_objects: Property = Property(name="objects", type=StringType)
commons_ObjectsNotification.attributes={commons_ObjectsNotification_objects}

# commons_EObjectLinked class attributes and methods
commons_EObjectLinked_m_getObject: Method = Method(name="getObject", parameters={})
commons_EObjectLinked.methods={commons_EObjectLinked_m_getObject}

# commons_CategoryInfo class attributes and methods
commons_CategoryInfo_primaryUri: Property = Property(name="primaryUri", type=StringType)
commons_CategoryInfo_googleFormalId: Property = Property(name="googleFormalId", type=StringType)
commons_CategoryInfo_m_getEffectiveName: Method = Method(name="getEffectiveName", parameters={Parameter(name='curLanguageTag')}, type=StringType)
commons_CategoryInfo.attributes={commons_CategoryInfo_primaryUri, commons_CategoryInfo_googleFormalId}
commons_CategoryInfo.methods={commons_CategoryInfo_m_getEffectiveName}

# commons_ProgressMonitor class attributes and methods
commons_ProgressMonitor_canceled: Property = Property(name="canceled", type=BooleanType)
commons_ProgressMonitor_taskName: Property = Property(name="taskName", type=StringType)
commons_ProgressMonitor_m_worked: Method = Method(name="worked", parameters={Parameter(name='work')})
commons_ProgressMonitor_m_done: Method = Method(name="done", parameters={Parameter(name='status')})
commons_ProgressMonitor_m_worked: Method = Method(name="worked", parameters={Parameter(name='work'), Parameter(name='status')})
commons_ProgressMonitor_m_beginTask: Method = Method(name="beginTask", parameters={Parameter(name='name'), Parameter(name='totalWork')})
commons_ProgressMonitor_m_done: Method = Method(name="done", parameters={})
commons_ProgressMonitor_m_internalWorked: Method = Method(name="internalWorked", parameters={Parameter(name='work')})
commons_ProgressMonitor_m_subTask: Method = Method(name="subTask", parameters={Parameter(name='name')})
commons_ProgressMonitor.attributes={commons_ProgressMonitor_taskName, commons_ProgressMonitor_canceled}
commons_ProgressMonitor.methods={commons_ProgressMonitor_m_done, commons_ProgressMonitor_m_worked, commons_ProgressMonitor_m_done, commons_ProgressMonitor_m_subTask, commons_ProgressMonitor_m_beginTask, commons_ProgressMonitor_m_internalWorked, commons_ProgressMonitor_m_worked}

# commons_ProgressMonitorWrapper class attributes and methods

# commons_ShellProgressMonitor class attributes and methods

# ProgressMonitor class attributes and methods

# commons_EventBusProgressMonitor class attributes and methods
commons_EventBusProgressMonitor_eventBus: Property = Property(name="eventBus", type=StringType)
commons_EventBusProgressMonitor_trackingId: Property = Property(name="trackingId", type=StringType)
commons_EventBusProgressMonitor.attributes={commons_EventBusProgressMonitor_eventBus, commons_EventBusProgressMonitor_trackingId}

# commons_Colorable class attributes and methods
commons_Colorable_color: Property = Property(name="color", type=StringType)
commons_Colorable.attributes={commons_Colorable_color}

# commons_TranslationMessageEntry class attributes and methods
commons_TranslationMessageEntry_key: Property = Property(name="key", type=StringType)
commons_TranslationMessageEntry_value: Property = Property(name="value", type=StringType)
commons_TranslationMessageEntry.attributes={commons_TranslationMessageEntry_key, commons_TranslationMessageEntry_value}

# commons_TranslationManager class attributes and methods
commons_TranslationManager_m_translate: Method = Method(name="translate", parameters={Parameter(name='entity'), Parameter(name='targetLanguage')})
commons_TranslationManager.methods={commons_TranslationManager_m_translate}

# commons_Translatable class attributes and methods
commons_Translatable_translationState: Property = Property(name="translationState", type=StringType)
commons_Translatable_originalLanguage: Property = Property(name="originalLanguage", type=StringType)
commons_Translatable_language: Property = Property(name="language", type=StringType)
commons_Translatable.attributes={commons_Translatable_language, commons_Translatable_translationState, commons_Translatable_originalLanguage}

# commons_TranslationEntry class attributes and methods
commons_TranslationEntry_key: Property = Property(name="key", type=StringType)
commons_TranslationEntry.attributes={commons_TranslationEntry_key}

# commons_Translation class attributes and methods
commons_Translation_language: Property = Property(name="language", type=StringType)
commons_Translation.attributes={commons_Translation_language}

# commons_PersonLike class attributes and methods
commons_PersonLike_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
commons_PersonLike_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
commons_PersonLike_m_getSlug: Method = Method(name="getSlug", parameters={}, type=StringType)
commons_PersonLike_m_getEmail: Method = Method(name="getEmail", parameters={}, type=StringType)
commons_PersonLike_m_getPhotoId: Method = Method(name="getPhotoId", parameters={}, type=StringType)
commons_PersonLike_m_getGender: Method = Method(name="getGender", parameters={}, type=StringType)
commons_PersonLike.methods={commons_PersonLike_m_getPhotoId, commons_PersonLike_m_getSlug, commons_PersonLike_m_getName, commons_PersonLike_m_getId, commons_PersonLike_m_getEmail, commons_PersonLike_m_getGender}

# commons_StyleConfiguration class attributes and methods
commons_StyleConfiguration_m_getDefaultStyle: Method = Method(name="getDefaultStyle", parameters={}, type=StringType)
commons_StyleConfiguration.methods={commons_StyleConfiguration_m_getDefaultStyle}

# commons_Expandable class attributes and methods
commons_Expandable_expansionState: Property = Property(name="expansionState", type=StringType)
commons_Expandable_m_expand: Method = Method(name="expand", parameters={Parameter(name='scope')})
commons_Expandable.attributes={commons_Expandable_expansionState}
commons_Expandable.methods={commons_Expandable_m_expand}

# commons_Person class attributes and methods
commons_Person_firstName: Property = Property(name="firstName", type=StringType)
commons_Person_lastName: Property = Property(name="lastName", type=StringType)
commons_Person_password: Property = Property(name="password", type=StringType)
commons_Person_schemaVersion: Property = Property(name="schemaVersion", type=StringType)
commons_Person_googlePlusId: Property = Property(name="googlePlusId", type=StringType)
commons_Person_googleUsername: Property = Property(name="googleUsername", type=StringType)
commons_Person_virtualMail: Property = Property(name="virtualMail", type=StringType)
commons_Person_nickname: Property = Property(name="nickname", type=StringType)
commons_Person_customerRole: Property = Property(name="customerRole", type=StringType)
commons_Person_memberRole: Property = Property(name="memberRole", type=StringType)
commons_Person_managerRole: Property = Property(name="managerRole", type=StringType)
commons_Person_timeZoneId: Property = Property(name="timeZoneId", type=StringType)
commons_Person_accountStatus: Property = Property(name="accountStatus", type=StringType)
commons_Person_birthYear: Property = Property(name="birthYear", type=StringType)
commons_Person_birthMonth: Property = Property(name="birthMonth", type=StringType)
commons_Person_birthDay: Property = Property(name="birthDay", type=StringType)
commons_Person_birthDate: Property = Property(name="birthDate", type=StringType)
commons_Person_gender: Property = Property(name="gender", type=StringType)
commons_Person_language: Property = Property(name="language", type=StringType)
commons_Person_currencyCode: Property = Property(name="currencyCode", type=StringType)
commons_Person_currency: Property = Property(name="currency", type=StringType)
commons_Person_folder: Property = Property(name="folder", type=StringType)
commons_Person_religion: Property = Property(name="religion", type=StringType)
commons_Person_passwordResetCode: Property = Property(name="passwordResetCode", type=StringType)
commons_Person_passwordResetExpiryTime: Property = Property(name="passwordResetExpiryTime", type=StringType)
commons_Person_clientAccessToken: Property = Property(name="clientAccessToken", type=StringType)
commons_Person_securityRoleIds: Property = Property(name="securityRoleIds", type=StringType)
commons_Person_timeZone: Property = Property(name="timeZone", type=StringType)
commons_Person_referrerId: Property = Property(name="referrerId", type=StringType)
commons_Person_referrerType: Property = Property(name="referrerType", type=StringType)
commons_Person_signupSource: Property = Property(name="signupSource", type=StringType)
commons_Person_signupSourceType: Property = Property(name="signupSourceType", type=StringType)
commons_Person_ipAddress: Property = Property(name="ipAddress", type=StringType)
commons_Person_lastIpAddress: Property = Property(name="lastIpAddress", type=StringType)
commons_Person_lastLoginTime: Property = Property(name="lastLoginTime", type=StringType)
commons_Person_validationTime: Property = Property(name="validationTime", type=StringType)
commons_Person_activationTime: Property = Property(name="activationTime", type=StringType)
commons_Person_verificationTime: Property = Property(name="verificationTime", type=StringType)
commons_Person_newsletterSubscriptionEnabled: Property = Property(name="newsletterSubscriptionEnabled", type=StringType)
commons_Person_newsletterSubscriptionTime: Property = Property(name="newsletterSubscriptionTime", type=StringType)
commons_Person_socialSharingEnabled: Property = Property(name="socialSharingEnabled", type=StringType)
commons_Person_publicationStatus: Property = Property(name="publicationStatus", type=StringType)
commons_Person_archivalStatus: Property = Property(name="archivalStatus", type=StringType)
commons_Person_debitBalance: Property = Property(name="debitBalance", type=StringType)
commons_Person_debitCurrency: Property = Property(name="debitCurrency", type=StringType)
commons_Person_type: Property = Property(name="type", type=StringType)
commons_Person_verifyCode: Property = Property(name="verifyCode", type=StringType)
commons_Person_zendeskUserId: Property = Property(name="zendeskUserId", type=StringType)
commons_Person_customerRoleEditTime: Property = Property(name="customerRoleEditTime", type=StringType)
commons_Person_lastTimeSynchronizeWithZendesk: Property = Property(name="lastTimeSynchronizeWithZendesk", type=StringType)
commons_Person_zendeskIntegration: Property = Property(name="zendeskIntegration", type=BooleanType)
commons_Person_m_hasEmail: Method = Method(name="hasEmail", parameters={Parameter(name='email')}, type=BooleanType)
commons_Person_m_putEmail: Method = Method(name="putEmail", parameters={Parameter(name='email')}, type=StringType)
commons_Person.attributes={commons_Person_lastName, commons_Person_birthDate, commons_Person_signupSourceType, commons_Person_zendeskIntegration, commons_Person_managerRole, commons_Person_activationTime, commons_Person_timeZone, commons_Person_lastTimeSynchronizeWithZendesk, commons_Person_birthYear, commons_Person_signupSource, commons_Person_securityRoleIds, commons_Person_lastLoginTime, commons_Person_firstName, commons_Person_gender, commons_Person_nickname, commons_Person_accountStatus, commons_Person_language, commons_Person_timeZoneId, commons_Person_password, commons_Person_currency, commons_Person_virtualMail, commons_Person_publicationStatus, commons_Person_passwordResetCode, commons_Person_newsletterSubscriptionTime, commons_Person_customerRoleEditTime, commons_Person_currencyCode, commons_Person_customerRole, commons_Person_schemaVersion, commons_Person_verifyCode, commons_Person_validationTime, commons_Person_birthDay, commons_Person_referrerId, commons_Person_clientAccessToken, commons_Person_googlePlusId, commons_Person_ipAddress, commons_Person_passwordResetExpiryTime, commons_Person_zendeskUserId, commons_Person_verificationTime, commons_Person_debitCurrency, commons_Person_referrerType, commons_Person_newsletterSubscriptionEnabled, commons_Person_religion, commons_Person_birthMonth, commons_Person_socialSharingEnabled, commons_Person_archivalStatus, commons_Person_folder, commons_Person_memberRole, commons_Person_type, commons_Person_lastIpAddress, commons_Person_debitBalance, commons_Person_googleUsername}
commons_Person.methods={commons_Person_m_putEmail, commons_Person_m_hasEmail}

# commons_PhoneNumber class attributes and methods
commons_PhoneNumber_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
commons_PhoneNumber_primary: Property = Property(name="primary", type=BooleanType)
commons_PhoneNumber_validationTime: Property = Property(name="validationTime", type=StringType)
commons_PhoneNumber.attributes={commons_PhoneNumber_phoneNumber, commons_PhoneNumber_primary, commons_PhoneNumber_validationTime}

# commons_Email class attributes and methods
commons_Email_primary: Property = Property(name="primary", type=BooleanType)
commons_Email_validationTime: Property = Property(name="validationTime", type=StringType)
commons_Email_email: Property = Property(name="email", type=StringType)
commons_Email.attributes={commons_Email_validationTime, commons_Email_email, commons_Email_primary}

# commons_PostalAddress class attributes and methods
commons_PostalAddress_workPhones: Property = Property(name="workPhones", type=StringType)
commons_PostalAddress_primaryEmail: Property = Property(name="primaryEmail", type=StringType)
commons_PostalAddress_emails: Property = Property(name="emails", type=StringType)
commons_PostalAddress_description: Property = Property(name="description", type=StringType)
commons_PostalAddress_schemaVersion: Property = Property(name="schemaVersion", type=StringType)
commons_PostalAddress_organization: Property = Property(name="organization", type=StringType)
commons_PostalAddress_street: Property = Property(name="street", type=StringType)
commons_PostalAddress_city: Property = Property(name="city", type=StringType)
commons_PostalAddress_postalCode: Property = Property(name="postalCode", type=StringType)
commons_PostalAddress_province: Property = Property(name="province", type=StringType)
commons_PostalAddress_country: Property = Property(name="country", type=StringType)
commons_PostalAddress_countryCode: Property = Property(name="countryCode", type=StringType)
commons_PostalAddress_primaryMobile: Property = Property(name="primaryMobile", type=StringType)
commons_PostalAddress_mobiles: Property = Property(name="mobiles", type=StringType)
commons_PostalAddress_primaryPhone: Property = Property(name="primaryPhone", type=StringType)
commons_PostalAddress_phones: Property = Property(name="phones", type=StringType)
commons_PostalAddress_primaryHomePhone: Property = Property(name="primaryHomePhone", type=StringType)
commons_PostalAddress_homePhones: Property = Property(name="homePhones", type=StringType)
commons_PostalAddress_primaryWorkPhone: Property = Property(name="primaryWorkPhone", type=StringType)
commons_PostalAddress_primary: Property = Property(name="primary", type=BooleanType)
commons_PostalAddress_primaryBilling: Property = Property(name="primaryBilling", type=BooleanType)
commons_PostalAddress_primaryShipping: Property = Property(name="primaryShipping", type=BooleanType)
commons_PostalAddress_validationTime: Property = Property(name="validationTime", type=StringType)
commons_PostalAddress_district: Property = Property(name="district", type=StringType)
commons_PostalAddress_jneAreaCode: Property = Property(name="jneAreaCode", type=StringType)
commons_PostalAddress.attributes={commons_PostalAddress_city, commons_PostalAddress_postalCode, commons_PostalAddress_jneAreaCode, commons_PostalAddress_schemaVersion, commons_PostalAddress_primaryBilling, commons_PostalAddress_primaryMobile, commons_PostalAddress_country, commons_PostalAddress_countryCode, commons_PostalAddress_organization, commons_PostalAddress_primaryEmail, commons_PostalAddress_homePhones, commons_PostalAddress_primaryWorkPhone, commons_PostalAddress_primaryShipping, commons_PostalAddress_workPhones, commons_PostalAddress_phones, commons_PostalAddress_primary, commons_PostalAddress_validationTime, commons_PostalAddress_primaryHomePhone, commons_PostalAddress_street, commons_PostalAddress_district, commons_PostalAddress_primaryPhone, commons_PostalAddress_description, commons_PostalAddress_province, commons_PostalAddress_mobiles, commons_PostalAddress_emails}

# SchemaVersionable class attributes and methods

# commons_Organization class attributes and methods
commons_Organization_schemaVersion: Property = Property(name="schemaVersion", type=StringType)
commons_Organization_blackBerryPin: Property = Property(name="blackBerryPin", type=StringType)
commons_Organization_website: Property = Property(name="website", type=StringType)
commons_Organization_facebookPageUri: Property = Property(name="facebookPageUri", type=StringType)
commons_Organization_facebookAccessToken: Property = Property(name="facebookAccessToken", type=StringType)
commons_Organization_facebookId: Property = Property(name="facebookId", type=StringType)
commons_Organization_facebookUserName: Property = Property(name="facebookUserName", type=StringType)
commons_Organization_twitterScreenName: Property = Property(name="twitterScreenName", type=StringType)
commons_Organization_twitterAccessToken: Property = Property(name="twitterAccessToken", type=StringType)
commons_Organization_twitterAccessTokenSecret: Property = Property(name="twitterAccessTokenSecret", type=StringType)
commons_Organization_twitterId: Property = Property(name="twitterId", type=StringType)
commons_Organization.attributes={commons_Organization_twitterAccessTokenSecret, commons_Organization_website, commons_Organization_facebookId, commons_Organization_facebookAccessToken, commons_Organization_blackBerryPin, commons_Organization_schemaVersion, commons_Organization_twitterScreenName, commons_Organization_twitterId, commons_Organization_facebookUserName, commons_Organization_facebookPageUri, commons_Organization_twitterAccessToken}

# commons_PersonCatalog class attributes and methods

# commons_CanonicalSluggable class attributes and methods
commons_CanonicalSluggable_canonicalSlug: Property = Property(name="canonicalSlug", type=StringType)
commons_CanonicalSluggable.attributes={commons_CanonicalSluggable_canonicalSlug}

# commons_SysConfig class attributes and methods
commons_SysConfig_tenantId: Property = Property(name="tenantId", type=StringType)
commons_SysConfig.attributes={commons_SysConfig_tenantId}

# commons_TwitterAccessible class attributes and methods
commons_TwitterAccessible_twitterAccessToken: Property = Property(name="twitterAccessToken", type=StringType)
commons_TwitterAccessible_twitterAccessTokenSecret: Property = Property(name="twitterAccessTokenSecret", type=StringType)
commons_TwitterAccessible.attributes={commons_TwitterAccessible_twitterAccessToken, commons_TwitterAccessible_twitterAccessTokenSecret}

# commons_TwitterIdentity class attributes and methods
commons_TwitterIdentity_twitterId: Property = Property(name="twitterId", type=StringType)
commons_TwitterIdentity_twitterScreenName: Property = Property(name="twitterScreenName", type=StringType)
commons_TwitterIdentity.attributes={commons_TwitterIdentity_twitterScreenName, commons_TwitterIdentity_twitterId}

# commons_FacebookIdentity class attributes and methods
commons_FacebookIdentity_facebookId: Property = Property(name="facebookId", type=StringType)
commons_FacebookIdentity_facebookUsername: Property = Property(name="facebookUsername", type=StringType)
commons_FacebookIdentity.attributes={commons_FacebookIdentity_facebookId, commons_FacebookIdentity_facebookUsername}

# commons_FacebookAccessible class attributes and methods
commons_FacebookAccessible_facebookAccessToken: Property = Property(name="facebookAccessToken", type=StringType)
commons_FacebookAccessible.attributes={commons_FacebookAccessible_facebookAccessToken}

# commons_Revisionable class attributes and methods
commons_Revisionable_guid: Property = Property(name="guid", type=StringType)
commons_Revisionable_revision: Property = Property(name="revision", type=StringType)
commons_Revisionable.attributes={commons_Revisionable_revision, commons_Revisionable_guid}

# commons_GeneralSysConfig class attributes and methods
commons_GeneralSysConfig_sslSupported: Property = Property(name="sslSupported", type=StringType)
commons_GeneralSysConfig.attributes={commons_GeneralSysConfig_sslSupported}

# SysConfig class attributes and methods

# Timestamped class attributes and methods

# commons_Geolocation class attributes and methods
commons_Geolocation_latitude: Property = Property(name="latitude", type=StringType)
commons_Geolocation_longitude: Property = Property(name="longitude", type=StringType)
commons_Geolocation_elevation: Property = Property(name="elevation", type=StringType)
commons_Geolocation.attributes={commons_Geolocation_elevation, commons_Geolocation_longitude, commons_Geolocation_latitude}

# commons_ThingInfo class attributes and methods
commons_ThingInfo_imageId: Property = Property(name="imageId", type=StringType)
commons_ThingInfo.attributes={commons_ThingInfo_imageId}

# commons_CustomerRole class attributes and methods
commons_CustomerRole_readOnly: Property = Property(name="readOnly", type=BooleanType)
commons_CustomerRole_quickShopEnabled: Property = Property(name="quickShopEnabled", type=BooleanType)
commons_CustomerRole_salesOrderReportEnabled: Property = Property(name="salesOrderReportEnabled", type=BooleanType)
commons_CustomerRole_historySalesOrderEnabled: Property = Property(name="historySalesOrderEnabled", type=BooleanType)
commons_CustomerRole_schemaVersion: Property = Property(name="schemaVersion", type=StringType)
commons_CustomerRole_status: Property = Property(name="status", type=StringType)
commons_CustomerRole_agentSalesReportEnabled: Property = Property(name="agentSalesReportEnabled", type=BooleanType)
commons_CustomerRole_transactionHistoryEnabled: Property = Property(name="transactionHistoryEnabled", type=BooleanType)
commons_CustomerRole_bookingEnabled: Property = Property(name="bookingEnabled", type=BooleanType)
commons_CustomerRole_paymentGatewayEnabled: Property = Property(name="paymentGatewayEnabled", type=BooleanType)
commons_CustomerRole_bookingExpiryTimeInMinutes: Property = Property(name="bookingExpiryTimeInMinutes", type=IntegerType)
commons_CustomerRole_dropshipEnabled: Property = Property(name="dropshipEnabled", type=BooleanType)
commons_CustomerRole_reviewReminderEnabled: Property = Property(name="reviewReminderEnabled", type=BooleanType)
commons_CustomerRole_zendeskIntegration: Property = Property(name="zendeskIntegration", type=BooleanType)
commons_CustomerRole_zendeskOrganizationId: Property = Property(name="zendeskOrganizationId", type=StringType)
commons_CustomerRole.attributes={commons_CustomerRole_bookingEnabled, commons_CustomerRole_transactionHistoryEnabled, commons_CustomerRole_bookingExpiryTimeInMinutes, commons_CustomerRole_paymentGatewayEnabled, commons_CustomerRole_readOnly, commons_CustomerRole_zendeskIntegration, commons_CustomerRole_zendeskOrganizationId, commons_CustomerRole_dropshipEnabled, commons_CustomerRole_schemaVersion, commons_CustomerRole_salesOrderReportEnabled, commons_CustomerRole_status, commons_CustomerRole_agentSalesReportEnabled, commons_CustomerRole_historySalesOrderEnabled, commons_CustomerRole_quickShopEnabled, commons_CustomerRole_reviewReminderEnabled}

# Describable class attributes and methods

# commons_MongoSysConfig class attributes and methods
commons_MongoSysConfig_mongoUri: Property = Property(name="mongoUri", type=StringType)
commons_MongoSysConfig.attributes={commons_MongoSysConfig_mongoUri}

# Relationships
eClass0: BinaryAssociation = BinaryAssociation(
    name="eClass0",
    ends={
        Property(name="commons_EClass", type=commons_EClassLinked, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_EClassLinked", type=commons_EClass, multiplicity=Multiplicity(0, 1))
    }
)
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="commons_EObject", type=commons_ModelNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_ModelNotification", type=commons_EObject, multiplicity=Multiplicity(0, 1))
    }
)
attribute2: BinaryAssociation = BinaryAssociation(
    name="attribute2",
    ends={
        Property(name="commons_EAttribute", type=commons_AttributeNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_AttributeNotification", type=commons_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
parents4: BinaryAssociation = BinaryAssociation(
    name="parents4",
    ends={
        Property(name="commons_CategoryInfo", type=commons_CategoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_CategoryInfo3", type=commons_CategoryInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegate5: BinaryAssociation = BinaryAssociation(
    name="delegate5",
    ends={
        Property(name="commons_ProgressMonitor", type=commons_ProgressMonitorWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_ProgressMonitorWrapper", type=commons_ProgressMonitor, multiplicity=Multiplicity(0, 1))
    }
)
messages7: BinaryAssociation = BinaryAssociation(
    name="messages7",
    ends={
        Property(name="commons_TranslationMessageEntry", type=commons_Translation, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Translation", type=commons_TranslationMessageEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translations6: BinaryAssociation = BinaryAssociation(
    name="translations6",
    ends={
        Property(name="commons_TranslationEntry", type=commons_Translatable, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Translatable", type=commons_TranslationEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value8: BinaryAssociation = BinaryAssociation(
    name="value8",
    ends={
        Property(name="commons_Translation10", type=commons_TranslationEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_TranslationEntry9", type=commons_Translation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phoneNumbers11: BinaryAssociation = BinaryAssociation(
    name="phoneNumbers11",
    ends={
        Property(name="commons_PhoneNumber", type=commons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Person", type=commons_PhoneNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emails12: BinaryAssociation = BinaryAssociation(
    name="emails12",
    ends={
        Property(name="commons_Email", type=commons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Person13", type=commons_Email, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mobileNumbers14: BinaryAssociation = BinaryAssociation(
    name="mobileNumbers14",
    ends={
        Property(name="commons_PhoneNumber16", type=commons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Person15", type=commons_PhoneNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addresses17: BinaryAssociation = BinaryAssociation(
    name="addresses17",
    ends={
        Property(name="commons_PostalAddress", type=commons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Person18", type=commons_PostalAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organizations19: BinaryAssociation = BinaryAssociation(
    name="organizations19",
    ends={
        Property(name="commons_Organization", type=commons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_Person20", type=commons_Organization, multiplicity=Multiplicity(0, 9999))
    }
)
people21: BinaryAssociation = BinaryAssociation(
    name="people21",
    ends={
        Property(name="commons_Person22", type=commons_PersonCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="commons_PersonCatalog", type=commons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_commons_AppManifest_Positionable = Generalization(general=Positionable, specific=commons_AppManifest)
gen_commons_AppManifest_ResourceAware = Generalization(general=ResourceAware, specific=commons_AppManifest)
gen_commons_AppManifest_BundleAware = Generalization(general=BundleAware, specific=commons_AppManifest)
gen_commons_AppManifest_Expandable = Generalization(general=Expandable, specific=commons_AppManifest)
gen_commons_PersonInfo_Identifiable = Generalization(general=Identifiable, specific=commons_PersonInfo)
gen_commons_PersonInfo_PhotoIdContainer = Generalization(general=PhotoIdContainer, specific=commons_PersonInfo)
gen_commons_PersonInfo_Sluggable = Generalization(general=Sluggable, specific=commons_PersonInfo)
gen_commons_PersonInfo_NameContainer = Generalization(general=NameContainer, specific=commons_PersonInfo)
gen_commons_PersonInfo_PersonLike = Generalization(general=PersonLike, specific=commons_PersonInfo)
gen_commons_PhotoIdContainer_Imageable = Generalization(general=Imageable, specific=commons_PhotoIdContainer)
gen_commons_NameContainer_Nameable = Generalization(general=Nameable, specific=commons_NameContainer)
gen_commons_WebAddress_Positionable = Generalization(general=Positionable, specific=commons_WebAddress)
gen_commons_WebAddress_BundleAware = Generalization(general=BundleAware, specific=commons_WebAddress)
gen_commons_WebAddress_ResourceAware = Generalization(general=ResourceAware, specific=commons_WebAddress)
gen_commons_WebAddress_Expandable = Generalization(general=Expandable, specific=commons_WebAddress)
gen_commons_CategoryLike_Identifiable = Generalization(general=Identifiable, specific=commons_CategoryLike)
gen_commons_CategoryLike_NsPrefixable = Generalization(general=NsPrefixable, specific=commons_CategoryLike)
gen_commons_CategoryLike_NameContainer = Generalization(general=NameContainer, specific=commons_CategoryLike)
gen_commons_CategoryLike_Positionable = Generalization(general=Positionable, specific=commons_CategoryLike)
gen_commons_CategoryLike_Sluggable = Generalization(general=Sluggable, specific=commons_CategoryLike)
gen_commons_CategoryLike_Imageable = Generalization(general=Imageable, specific=commons_CategoryLike)
gen_commons_ProgressMonitorWrapper_ProgressMonitor = Generalization(general=ProgressMonitor, specific=commons_ProgressMonitorWrapper)
gen_commons_ShellProgressMonitor_ProgressMonitor = Generalization(general=ProgressMonitor, specific=commons_ShellProgressMonitor)
gen_commons_EventBusProgressMonitor_ProgressMonitor = Generalization(general=ProgressMonitor, specific=commons_EventBusProgressMonitor)
gen_commons_PostalAddress_NameContainer = Generalization(general=NameContainer, specific=commons_PostalAddress)
gen_commons_PostalAddress_Identifiable = Generalization(general=Identifiable, specific=commons_PostalAddress)
gen_commons_PostalAddress_SchemaVersionable = Generalization(general=SchemaVersionable, specific=commons_PostalAddress)
gen_commons_CanonicalSluggable_Sluggable = Generalization(general=Sluggable, specific=commons_CanonicalSluggable)
gen_commons_GeneralSysConfig_Expandable = Generalization(general=Expandable, specific=commons_GeneralSysConfig)
gen_commons_GeneralSysConfig_SysConfig = Generalization(general=SysConfig, specific=commons_GeneralSysConfig)
gen_commons_SysConfig_Timestamped = Generalization(general=Timestamped, specific=commons_SysConfig)
gen_commons_ThingInfo_NameContainer = Generalization(general=NameContainer, specific=commons_ThingInfo)
gen_commons_ThingInfo_Identifiable = Generalization(general=Identifiable, specific=commons_ThingInfo)
gen_commons_ThingInfo_Sluggable = Generalization(general=Sluggable, specific=commons_ThingInfo)
gen_commons_ThingInfo_Imageable = Generalization(general=Imageable, specific=commons_ThingInfo)
gen_commons_Organization_Identifiable = Generalization(general=Identifiable, specific=commons_Organization)
gen_commons_Organization_SchemaVersionable = Generalization(general=SchemaVersionable, specific=commons_Organization)
gen_commons_Organization_NameContainer = Generalization(general=NameContainer, specific=commons_Organization)
gen_commons_CustomerRole_Identifiable = Generalization(general=Identifiable, specific=commons_CustomerRole)
gen_commons_CustomerRole_SchemaVersionable = Generalization(general=SchemaVersionable, specific=commons_CustomerRole)
gen_commons_CustomerRole_NameContainer = Generalization(general=NameContainer, specific=commons_CustomerRole)
gen_commons_CustomerRole_Timestamped = Generalization(general=Timestamped, specific=commons_CustomerRole)
gen_commons_CustomerRole_Describable = Generalization(general=Describable, specific=commons_CustomerRole)

# Domain Model
domain_model = DomainModel(
    name="commons",
    types={commons_Positionable, commons_AppManifest, Positionable, ResourceAware, BundleAware, Expandable, commons_ResourceAware, commons_Timestamped, commons_PersonInfo, Identifiable, PhotoIdContainer, Sluggable, NameContainer, PersonLike, commons_Nameable, commons_Imageable, commons_Identifiable, commons_Sluggable, commons_JavaClassLinked, commons_PhotoIdContainer, Imageable, commons_NameContainer, Nameable, commons_Informer, commons_Describable, commons_BundleAware, commons_EClassLinked, commons_EClass, commons_SchemaVersionable, commons_EFactoryLinked, commons_NsPrefixable, commons_WebAddress, commons_AttributeSet, commons_Added, commons_ModelNotification, commons_EObject, commons_Parentable, commons_CategoryLike, NsPrefixable, commons_AttributeUnset, commons_Removed, commons_ObjectNotification, commons_AttributeNotification, commons_EAttribute, commons_AddedMany, commons_RemovedMany, commons_ObjectsNotification, commons_EObjectLinked, commons_CategoryInfo, commons_ProgressMonitor, commons_ProgressMonitorWrapper, commons_ShellProgressMonitor, ProgressMonitor, commons_EventBusProgressMonitor, commons_Colorable, commons_TranslationMessageEntry, commons_TranslationManager, commons_Translatable, commons_TranslationEntry, commons_Translation, commons_PersonLike, commons_StyleConfiguration, commons_Expandable, commons_Person, commons_PhoneNumber, commons_Email, commons_PostalAddress, SchemaVersionable, commons_Organization, commons_PersonCatalog, commons_CanonicalSluggable, commons_SysConfig, commons_TwitterAccessible, commons_TwitterIdentity, commons_FacebookIdentity, commons_FacebookAccessible, commons_Revisionable, commons_GeneralSysConfig, SysConfig, Timestamped, commons_Geolocation, commons_ThingInfo, commons_CustomerRole, Describable, commons_MongoSysConfig, ResourceType, Gender, EClassStatus, JavaClassStatus, ProgressStatus, AccountStatus, ArchivalStatus, PublicationStatus, TranslationState, ExpansionState, SignupSourceType, TenantSource, GenericStatus, CustomerRoleStatus, EntityKind},
    associations={eClass0, container1, attribute2, parents4, delegate5, messages7, translations6, value8, phoneNumbers11, emails12, mobileNumbers14, addresses17, organizations19, people21},
    generalizations={gen_commons_AppManifest_Positionable, gen_commons_AppManifest_ResourceAware, gen_commons_AppManifest_BundleAware, gen_commons_AppManifest_Expandable, gen_commons_PersonInfo_Identifiable, gen_commons_PersonInfo_PhotoIdContainer, gen_commons_PersonInfo_Sluggable, gen_commons_PersonInfo_NameContainer, gen_commons_PersonInfo_PersonLike, gen_commons_PhotoIdContainer_Imageable, gen_commons_NameContainer_Nameable, gen_commons_WebAddress_Positionable, gen_commons_WebAddress_BundleAware, gen_commons_WebAddress_ResourceAware, gen_commons_WebAddress_Expandable, gen_commons_CategoryLike_Identifiable, gen_commons_CategoryLike_NsPrefixable, gen_commons_CategoryLike_NameContainer, gen_commons_CategoryLike_Positionable, gen_commons_CategoryLike_Sluggable, gen_commons_CategoryLike_Imageable, gen_commons_ProgressMonitorWrapper_ProgressMonitor, gen_commons_ShellProgressMonitor_ProgressMonitor, gen_commons_EventBusProgressMonitor_ProgressMonitor, gen_commons_PostalAddress_NameContainer, gen_commons_PostalAddress_Identifiable, gen_commons_PostalAddress_SchemaVersionable, gen_commons_CanonicalSluggable_Sluggable, gen_commons_GeneralSysConfig_Expandable, gen_commons_GeneralSysConfig_SysConfig, gen_commons_SysConfig_Timestamped, gen_commons_ThingInfo_NameContainer, gen_commons_ThingInfo_Identifiable, gen_commons_ThingInfo_Sluggable, gen_commons_ThingInfo_Imageable, gen_commons_Organization_Identifiable, gen_commons_Organization_SchemaVersionable, gen_commons_Organization_NameContainer, gen_commons_CustomerRole_Identifiable, gen_commons_CustomerRole_SchemaVersionable, gen_commons_CustomerRole_NameContainer, gen_commons_CustomerRole_Timestamped, gen_commons_CustomerRole_Describable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)