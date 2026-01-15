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
SourceState: Enumeration = Enumeration(
    name="SourceState",
    literals={
            EnumerationLiteral(name="Active"),
			EnumerationLiteral(name="Paused"),
			EnumerationLiteral(name="Error"),
			EnumerationLiteral(name="Stoped")
    }
)

SourceActiveStates: Enumeration = Enumeration(
    name="SourceActiveStates",
    literals={
            EnumerationLiteral(name="Initializing"),
			EnumerationLiteral(name="Initialized"),
			EnumerationLiteral(name="Filling"),
			EnumerationLiteral(name="Filled"),
			EnumerationLiteral(name="WaitingForUpdate"),
			EnumerationLiteral(name="Updating"),
			EnumerationLiteral(name="Enriching"),
			EnumerationLiteral(name="Unknown")
    }
)

PropertyTypes: Enumeration = Enumeration(
    name="PropertyTypes",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Authorization"),
			EnumerationLiteral(name="UploadZipFile"),
			EnumerationLiteral(name="UploadFile"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
application_Source = Class(name="application::Source")
ConfigurableElement = Class(name="ConfigurableElement")
application_Persistency = Class(name="application::Persistency")
application_DataSet = Class(name="application::DataSet")
application_MappingRule = Class(name="application::MappingRule")
application_Interface = Class(name="application::Interface", is_abstract=True)
application_MashupAdmin = Class(name="application::MashupAdmin")
application_Mashup = Class(name="application::Mashup")
Source = Class(name="Source")
application_Database = Class(name="application::Database")
application_OCLRestrictedProperty = Class(name="application::OCLRestrictedProperty")
Property_ = Class(name="Property")
application_Configuration = Class(name="application::Configuration")
application_Property = Class(name="application::Property")
application_XMLFile = Class(name="application::XMLFile")
Persistency = Class(name="Persistency")
application_MashupContainer = Class(name="application::MashupContainer")
application_FEEDInterface = Class(name="application::FEEDInterface")
application_OAuthConfig = Class(name="application::OAuthConfig")
Security = Class(name="Security")
application_OAuthClientConfig = Class(name="application::OAuthClientConfig")
application_OAuthAdmin = Class(name="application::OAuthAdmin")
application_ApplicationKeyConfig = Class(name="application::ApplicationKeyConfig")
application_Security = Class(name="application::Security", is_abstract=True)
application_RESTInterface = Class(name="application::RESTInterface")
Interface = Class(name="Interface")
application_OAuthClientScope = Class(name="application::OAuthClientScope")
application_ConfigurableElement = Class(name="application::ConfigurableElement", is_abstract=True)

# application_Source class attributes and methods
application_Source_bundleId: Property = Property(name="bundleId", type=StringType)
application_Source_state: Property = Property(name="state", type=StringType)
application_Source_activeState: Property = Property(name="activeState", type=StringType)
application_Source_logLevel: Property = Property(name="logLevel", type=StringType)
application_Source_removeDataOnStop: Property = Property(name="removeDataOnStop", type=StringType)
application_Source_updateRound: Property = Property(name="updateRound", type=StringType)
application_Source_m_getLogLevelIntValue: Method = Method(name="getLogLevelIntValue", parameters={}, type=StringType)
application_Source_m_start: Method = Method(name="start", parameters={})
application_Source_m_stop: Method = Method(name="stop", parameters={})
application_Source_m_pause: Method = Method(name="pause", parameters={})
application_Source.attributes={application_Source_logLevel, application_Source_removeDataOnStop, application_Source_activeState, application_Source_bundleId, application_Source_state, application_Source_updateRound}
application_Source.methods={application_Source_m_stop, application_Source_m_getLogLevelIntValue, application_Source_m_start, application_Source_m_pause}

# ConfigurableElement class attributes and methods

# application_Persistency class attributes and methods

# application_DataSet class attributes and methods

# application_MappingRule class attributes and methods

# application_Interface class attributes and methods
application_Interface_urlSuffix: Property = Property(name="urlSuffix", type=StringType)
application_Interface_frontEndCaching: Property = Property(name="frontEndCaching", type=StringType)
application_Interface.attributes={application_Interface_urlSuffix, application_Interface_frontEndCaching}

# application_MashupAdmin class attributes and methods
application_MashupAdmin_provider: Property = Property(name="provider", type=StringType)
application_MashupAdmin_id: Property = Property(name="id", type=StringType)
application_MashupAdmin_name: Property = Property(name="name", type=StringType)
application_MashupAdmin_localIdent: Property = Property(name="localIdent", type=StringType)
application_MashupAdmin_isConfigurationAdmin: Property = Property(name="isConfigurationAdmin", type=StringType)
application_MashupAdmin_profileImage: Property = Property(name="profileImage", type=StringType)
application_MashupAdmin_email: Property = Property(name="email", type=StringType)
application_MashupAdmin.attributes={application_MashupAdmin_profileImage, application_MashupAdmin_email, application_MashupAdmin_localIdent, application_MashupAdmin_isConfigurationAdmin, application_MashupAdmin_provider, application_MashupAdmin_id, application_MashupAdmin_name}

# application_Mashup class attributes and methods
application_Mashup_workingDirectory: Property = Property(name="workingDirectory", type=StringType)
application_Mashup_cacheAttachments: Property = Property(name="cacheAttachments", type=StringType)
application_Mashup_cacheDataSet: Property = Property(name="cacheDataSet", type=StringType)
application_Mashup_backupDataSet: Property = Property(name="backupDataSet", type=StringType)
application_Mashup_backupIntervall: Property = Property(name="backupIntervall", type=StringType)
application_Mashup_cacheDelay: Property = Property(name="cacheDelay", type=StringType)
application_Mashup_sourceIdentCounter: Property = Property(name="sourceIdentCounter", type=StringType)
application_Mashup_keepDeletedItemsList: Property = Property(name="keepDeletedItemsList", type=StringType)
application_Mashup_m_getSourceWithIdent: Method = Method(name="getSourceWithIdent", parameters={Parameter(name='ident')}, type=Source)
application_Mashup_m_getNewSourceIdent: Method = Method(name="getNewSourceIdent", parameters={}, type=StringType)
application_Mashup.attributes={application_Mashup_cacheDelay, application_Mashup_backupIntervall, application_Mashup_keepDeletedItemsList, application_Mashup_cacheDataSet, application_Mashup_sourceIdentCounter, application_Mashup_workingDirectory, application_Mashup_cacheAttachments, application_Mashup_backupDataSet}
application_Mashup.methods={application_Mashup_m_getSourceWithIdent, application_Mashup_m_getNewSourceIdent}

# Source class attributes and methods

# application_Database class attributes and methods

# application_OCLRestrictedProperty class attributes and methods
application_OCLRestrictedProperty_OCLRestriction: Property = Property(name="OCLRestriction", type=StringType)
application_OCLRestrictedProperty.attributes={application_OCLRestrictedProperty_OCLRestriction}

# Property class attributes and methods

# application_Configuration class attributes and methods

# application_Property class attributes and methods
application_Property_Key: Property = Property(name="Key", type=StringType)
application_Property_Value: Property = Property(name="Value", type=StringType)
application_Property_hidden: Property = Property(name="hidden", type=StringType)
application_Property_changeable: Property = Property(name="changeable", type=StringType)
application_Property_possibleValues: Property = Property(name="possibleValues", type=StringType)
application_Property_helpText: Property = Property(name="helpText", type=StringType)
application_Property_required: Property = Property(name="required", type=StringType)
application_Property_propertyType: Property = Property(name="propertyType", type=StringType)
application_Property_m_isValueList: Method = Method(name="isValueList", parameters={}, type=BooleanType)
application_Property_m_isValueRange: Method = Method(name="isValueRange", parameters={}, type=BooleanType)
application_Property_m_getListOfValues: Method = Method(name="getListOfValues", parameters={}, type=StringType)
application_Property_m_getMinValue: Method = Method(name="getMinValue", parameters={}, type=StringType)
application_Property_m_getMaxValue: Method = Method(name="getMaxValue", parameters={}, type=StringType)
application_Property.attributes={application_Property_hidden, application_Property_Value, application_Property_propertyType, application_Property_possibleValues, application_Property_helpText, application_Property_required, application_Property_changeable, application_Property_Key}
application_Property.methods={application_Property_m_isValueRange, application_Property_m_isValueList, application_Property_m_getMaxValue, application_Property_m_getListOfValues, application_Property_m_getMinValue}

# application_XMLFile class attributes and methods

# Persistency class attributes and methods

# application_MashupContainer class attributes and methods
application_MashupContainer_backupConfiguration: Property = Property(name="backupConfiguration", type=StringType)
application_MashupContainer_backupIntervall: Property = Property(name="backupIntervall", type=StringType)
application_MashupContainer_immediateSave: Property = Property(name="immediateSave", type=StringType)
application_MashupContainer_createAccountsAtLoginTry: Property = Property(name="createAccountsAtLoginTry", type=StringType)
application_MashupContainer_identCounter: Property = Property(name="identCounter", type=StringType)
application_MashupContainer_m_getConfigurationAdmins: Method = Method(name="getConfigurationAdmins", parameters={}, type=StringType)
application_MashupContainer_m_setNewIdentFor: Method = Method(name="setNewIdentFor", parameters={Parameter(name='configurableElement')})
application_MashupContainer_m_getNewIdentNumber: Method = Method(name="getNewIdentNumber", parameters={}, type=StringType)
application_MashupContainer_m_getMashupWithIdent: Method = Method(name="getMashupWithIdent", parameters={Parameter(name='ident')}, type=StringType)
application_MashupContainer_m_getSourceConfigurationWithIdent: Method = Method(name="getSourceConfigurationWithIdent", parameters={Parameter(name='ident')}, type=Source)
application_MashupContainer.attributes={application_MashupContainer_createAccountsAtLoginTry, application_MashupContainer_immediateSave, application_MashupContainer_identCounter, application_MashupContainer_backupIntervall, application_MashupContainer_backupConfiguration}
application_MashupContainer.methods={application_MashupContainer_m_getConfigurationAdmins, application_MashupContainer_m_setNewIdentFor, application_MashupContainer_m_getMashupWithIdent, application_MashupContainer_m_getNewIdentNumber, application_MashupContainer_m_getSourceConfigurationWithIdent}

# application_FEEDInterface class attributes and methods
application_FEEDInterface_allowPersonFiltering: Property = Property(name="allowPersonFiltering", type=StringType)
application_FEEDInterface_allowOrganisationFiltering: Property = Property(name="allowOrganisationFiltering", type=StringType)
application_FEEDInterface_allowTypeFiltering: Property = Property(name="allowTypeFiltering", type=StringType)
application_FEEDInterface_allowTagFiltering: Property = Property(name="allowTagFiltering", type=StringType)
application_FEEDInterface_allowMetaTagFiltering: Property = Property(name="allowMetaTagFiltering", type=StringType)
application_FEEDInterface_allowCategoryFiltering: Property = Property(name="allowCategoryFiltering", type=StringType)
application_FEEDInterface_language: Property = Property(name="language", type=StringType)
application_FEEDInterface_feedType: Property = Property(name="feedType", type=StringType)
application_FEEDInterface_feedTitle: Property = Property(name="feedTitle", type=StringType)
application_FEEDInterface.attributes={application_FEEDInterface_feedType, application_FEEDInterface_allowCategoryFiltering, application_FEEDInterface_allowTypeFiltering, application_FEEDInterface_allowOrganisationFiltering, application_FEEDInterface_language, application_FEEDInterface_feedTitle, application_FEEDInterface_allowMetaTagFiltering, application_FEEDInterface_allowPersonFiltering, application_FEEDInterface_allowTagFiltering}

# application_OAuthConfig class attributes and methods
application_OAuthConfig_useScopeInterfaceOnRedirect: Property = Property(name="useScopeInterfaceOnRedirect", type=StringType)
application_OAuthConfig.attributes={application_OAuthConfig_useScopeInterfaceOnRedirect}

# Security class attributes and methods

# application_OAuthClientConfig class attributes and methods
application_OAuthClientConfig_description: Property = Property(name="description", type=StringType)
application_OAuthClientConfig_clientID: Property = Property(name="clientID", type=StringType)
application_OAuthClientConfig_clientSecret: Property = Property(name="clientSecret", type=StringType)
application_OAuthClientConfig_code: Property = Property(name="code", type=StringType)
application_OAuthClientConfig_grantType: Property = Property(name="grantType", type=StringType)
application_OAuthClientConfig_refreshToken: Property = Property(name="refreshToken", type=StringType)
application_OAuthClientConfig_accessToken: Property = Property(name="accessToken", type=StringType)
application_OAuthClientConfig_accessTokenCreationDate: Property = Property(name="accessTokenCreationDate", type=DateType)
application_OAuthClientConfig_accessTokenExpirationDate: Property = Property(name="accessTokenExpirationDate", type=DateType)
application_OAuthClientConfig_forbiddenMetaTags: Property = Property(name="forbiddenMetaTags", type=StringType)
application_OAuthClientConfig_allowedMetaTags: Property = Property(name="allowedMetaTags", type=StringType)
application_OAuthClientConfig_oAuthScopeLevel: Property = Property(name="oAuthScopeLevel", type=StringType)
application_OAuthClientConfig_type: Property = Property(name="type", type=StringType)
application_OAuthClientConfig_redirectionURL: Property = Property(name="redirectionURL", type=StringType)
application_OAuthClientConfig_name: Property = Property(name="name", type=StringType)
application_OAuthClientConfig.attributes={application_OAuthClientConfig_description, application_OAuthClientConfig_code, application_OAuthClientConfig_forbiddenMetaTags, application_OAuthClientConfig_grantType, application_OAuthClientConfig_accessToken, application_OAuthClientConfig_allowedMetaTags, application_OAuthClientConfig_type, application_OAuthClientConfig_accessTokenCreationDate, application_OAuthClientConfig_clientID, application_OAuthClientConfig_accessTokenExpirationDate, application_OAuthClientConfig_clientSecret, application_OAuthClientConfig_refreshToken, application_OAuthClientConfig_redirectionURL, application_OAuthClientConfig_oAuthScopeLevel, application_OAuthClientConfig_name}

# application_OAuthAdmin class attributes and methods
application_OAuthAdmin_username: Property = Property(name="username", type=StringType)
application_OAuthAdmin_passwordHash: Property = Property(name="passwordHash", type=StringType)
application_OAuthAdmin.attributes={application_OAuthAdmin_username, application_OAuthAdmin_passwordHash}

# application_ApplicationKeyConfig class attributes and methods
application_ApplicationKeyConfig_applicationKeys: Property = Property(name="applicationKeys", type=StringType)
application_ApplicationKeyConfig_m_hasApplicationKey: Method = Method(name="hasApplicationKey", parameters={Parameter(name='applicationKey')}, type=StringType)
application_ApplicationKeyConfig.attributes={application_ApplicationKeyConfig_applicationKeys}
application_ApplicationKeyConfig.methods={application_ApplicationKeyConfig_m_hasApplicationKey}

# application_Security class attributes and methods

# application_RESTInterface class attributes and methods
application_RESTInterface_type: Property = Property(name="type", type=StringType)
application_RESTInterface.attributes={application_RESTInterface_type}

# Interface class attributes and methods

# application_OAuthClientScope class attributes and methods
application_OAuthClientScope_positiveTag: Property = Property(name="positiveTag", type=StringType)
application_OAuthClientScope_negativeTag: Property = Property(name="negativeTag", type=StringType)
application_OAuthClientScope_positiveMetaTag: Property = Property(name="positiveMetaTag", type=StringType)
application_OAuthClientScope_negativeMetaTag: Property = Property(name="negativeMetaTag", type=StringType)
application_OAuthClientScope_positiveCategory: Property = Property(name="positiveCategory", type=StringType)
application_OAuthClientScope_negativeCategory: Property = Property(name="negativeCategory", type=StringType)
application_OAuthClientScope_positivePerson: Property = Property(name="positivePerson", type=StringType)
application_OAuthClientScope_negativePerson: Property = Property(name="negativePerson", type=StringType)
application_OAuthClientScope_positiveOrganisation: Property = Property(name="positiveOrganisation", type=StringType)
application_OAuthClientScope_negativeOrganisation: Property = Property(name="negativeOrganisation", type=StringType)
application_OAuthClientScope_identSpecification: Property = Property(name="identSpecification", type=StringType)
application_OAuthClientScope_allowPersons: Property = Property(name="allowPersons", type=StringType)
application_OAuthClientScope_allowContents: Property = Property(name="allowContents", type=StringType)
application_OAuthClientScope_allowOrganisations: Property = Property(name="allowOrganisations", type=StringType)
application_OAuthClientScope_maximumAge: Property = Property(name="maximumAge", type=StringType)
application_OAuthClientScope.attributes={application_OAuthClientScope_allowOrganisations, application_OAuthClientScope_positiveCategory, application_OAuthClientScope_positiveMetaTag, application_OAuthClientScope_negativeOrganisation, application_OAuthClientScope_allowContents, application_OAuthClientScope_negativeTag, application_OAuthClientScope_positiveOrganisation, application_OAuthClientScope_allowPersons, application_OAuthClientScope_positiveTag, application_OAuthClientScope_negativePerson, application_OAuthClientScope_identSpecification, application_OAuthClientScope_positivePerson, application_OAuthClientScope_maximumAge, application_OAuthClientScope_negativeCategory, application_OAuthClientScope_negativeMetaTag}

# application_ConfigurableElement class attributes and methods
application_ConfigurableElement_name: Property = Property(name="name", type=StringType)
application_ConfigurableElement_configurationImage: Property = Property(name="configurationImage", type=StringType)
application_ConfigurableElement_description: Property = Property(name="description", type=StringType)
application_ConfigurableElement_changeable: Property = Property(name="changeable", type=StringType)
application_ConfigurableElement_hidden: Property = Property(name="hidden", type=StringType)
application_ConfigurableElement_ident: Property = Property(name="ident", type=StringType)
application_ConfigurableElement_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key')}, type=Property_)
application_ConfigurableElement_m_addProperty: Method = Method(name="addProperty", parameters={Parameter(name='value'), Parameter(name='key')})
application_ConfigurableElement_m_addProperty: Method = Method(name="addProperty", parameters={Parameter(name='property')})
application_ConfigurableElement_m_getPropertyValue: Method = Method(name="getPropertyValue", parameters={Parameter(name='key')}, type=StringType)
application_ConfigurableElement_m_isPropertyTrue: Method = Method(name="isPropertyTrue", parameters={Parameter(name='key')}, type=BooleanType)
application_ConfigurableElement_m_getPropertyValueElseDefault: Method = Method(name="getPropertyValueElseDefault", parameters={Parameter(name='key'), Parameter(name='defaultValue')}, type=StringType)
application_ConfigurableElement_m_isPropertyTrueElseDefault: Method = Method(name="isPropertyTrueElseDefault", parameters={Parameter(name='defaultValue'), Parameter(name='key')}, type=BooleanType)
application_ConfigurableElement_m_removeProperty: Method = Method(name="removeProperty", parameters={Parameter(name='key')})
application_ConfigurableElement.attributes={application_ConfigurableElement_ident, application_ConfigurableElement_changeable, application_ConfigurableElement_configurationImage, application_ConfigurableElement_description, application_ConfigurableElement_hidden, application_ConfigurableElement_name}
application_ConfigurableElement.methods={application_ConfigurableElement_m_getProperty, application_ConfigurableElement_m_addProperty, application_ConfigurableElement_m_isPropertyTrue, application_ConfigurableElement_m_getPropertyValue, application_ConfigurableElement_m_isPropertyTrueElseDefault, application_ConfigurableElement_m_removeProperty, application_ConfigurableElement_m_addProperty, application_ConfigurableElement_m_getPropertyValueElseDefault}

# Relationships
persistency0: BinaryAssociation = BinaryAssociation(
    name="persistency0",
    ends={
        Property(name="application_Persistency", type=application_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Source", type=application_Persistency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataSet1: BinaryAssociation = BinaryAssociation(
    name="dataSet1",
    ends={
        Property(name="application_DataSet", type=application_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Source2", type=application_DataSet, multiplicity=Multiplicity(0, 1))
    }
)
mappingRules4: BinaryAssociation = BinaryAssociation(
    name="mappingRules4",
    ends={
        Property(name="application_MappingRule", type=application_Mashup, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Mashup", type=application_MappingRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources5: BinaryAssociation = BinaryAssociation(
    name="sources5",
    ends={
        Property(name="Source", type=application_Mashup, multiplicity=Multiplicity(1, 1)),
        Property(name="mashup", type=application_Source, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces6: BinaryAssociation = BinaryAssociation(
    name="interfaces6",
    ends={
        Property(name="Interface", type=application_Mashup, multiplicity=Multiplicity(1, 1)),
        Property(name="mashup7", type=application_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mashupAdmins8: BinaryAssociation = BinaryAssociation(
    name="mashupAdmins8",
    ends={
        Property(name="MashupAdmin", type=application_Mashup, multiplicity=Multiplicity(1, 1)),
        Property(name="configurableMashups", type=application_MashupAdmin, multiplicity=Multiplicity(0, 9999))
    }
)
mashup3: BinaryAssociation = BinaryAssociation(
    name="mashup3",
    ends={
        Property(name="Mashup", type=application_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=application_Mashup, multiplicity=Multiplicity(0, 1))
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="application_Property", type=application_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="application_Configuration", type=application_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allMashupAdmins12: BinaryAssociation = BinaryAssociation(
    name="allMashupAdmins12",
    ends={
        Property(name="application_MashupAdmin", type=application_MashupContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_MashupContainer13", type=application_MashupAdmin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultMashups14: BinaryAssociation = BinaryAssociation(
    name="defaultMashups14",
    ends={
        Property(name="application_Mashup16", type=application_MashupContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_MashupContainer15", type=application_Mashup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceConfigurations17: BinaryAssociation = BinaryAssociation(
    name="sourceConfigurations17",
    ends={
        Property(name="application_Mashup19", type=application_MashupContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_MashupContainer18", type=application_Mashup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceConfigurations20: BinaryAssociation = BinaryAssociation(
    name="interfaceConfigurations20",
    ends={
        Property(name="application_Interface", type=application_MashupContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_MashupContainer21", type=application_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mashups10: BinaryAssociation = BinaryAssociation(
    name="mashups10",
    ends={
        Property(name="application_Mashup11", type=application_MashupContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="application_MashupContainer", type=application_Mashup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface25: BinaryAssociation = BinaryAssociation(
    name="interface25",
    ends={
        Property(name="Interface26", type=application_Security, multiplicity=Multiplicity(1, 1)),
        Property(name="security", type=application_Interface, multiplicity=Multiplicity(0, 1))
    }
)
clients27: BinaryAssociation = BinaryAssociation(
    name="clients27",
    ends={
        Property(name="application_OAuthClientConfig", type=application_OAuthConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="application_OAuthConfig", type=application_OAuthClientConfig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
admins28: BinaryAssociation = BinaryAssociation(
    name="admins28",
    ends={
        Property(name="application_OAuthAdmin", type=application_OAuthConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="application_OAuthConfig29", type=application_OAuthAdmin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
security22: BinaryAssociation = BinaryAssociation(
    name="security22",
    ends={
        Property(name="Security", type=application_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface", type=application_Security, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mashup23: BinaryAssociation = BinaryAssociation(
    name="mashup23",
    ends={
        Property(name="Mashup24", type=application_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces", type=application_Mashup, multiplicity=Multiplicity(0, 1))
    }
)
clientScope30: BinaryAssociation = BinaryAssociation(
    name="clientScope30",
    ends={
        Property(name="application_OAuthClientScope", type=application_OAuthClientConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="application_OAuthClientConfig31", type=application_OAuthClientScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configuration34: BinaryAssociation = BinaryAssociation(
    name="configuration34",
    ends={
        Property(name="application_Configuration35", type=application_ConfigurableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="application_ConfigurableElement", type=application_Configuration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configurableMashups32: BinaryAssociation = BinaryAssociation(
    name="configurableMashups32",
    ends={
        Property(name="Mashup33", type=application_MashupAdmin, multiplicity=Multiplicity(1, 1)),
        Property(name="mashupAdmins", type=application_Mashup, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_application_Source_ConfigurableElement = Generalization(general=ConfigurableElement, specific=application_Source)
gen_application_Mashup_Source = Generalization(general=Source, specific=application_Mashup)
gen_application_XMLFile_Persistency = Generalization(general=Persistency, specific=application_XMLFile)
gen_application_Database_Persistency = Generalization(general=Persistency, specific=application_Database)
gen_application_OCLRestrictedProperty_Property = Generalization(general=Property_, specific=application_OCLRestrictedProperty)
gen_application_FEEDInterface_Interface = Generalization(general=Interface, specific=application_FEEDInterface)
gen_application_OAuthConfig_Security = Generalization(general=Security, specific=application_OAuthConfig)
gen_application_Interface_ConfigurableElement = Generalization(general=ConfigurableElement, specific=application_Interface)
gen_application_ApplicationKeyConfig_Security = Generalization(general=Security, specific=application_ApplicationKeyConfig)
gen_application_RESTInterface_Interface = Generalization(general=Interface, specific=application_RESTInterface)

# Domain Model
domain_model = DomainModel(
    name="application",
    types={application_Source, ConfigurableElement, application_Persistency, application_DataSet, application_MappingRule, application_Interface, application_MashupAdmin, application_Mashup, Source, application_Database, application_OCLRestrictedProperty, Property_, application_Configuration, application_Property, application_XMLFile, Persistency, application_MashupContainer, application_FEEDInterface, application_OAuthConfig, Security, application_OAuthClientConfig, application_OAuthAdmin, application_ApplicationKeyConfig, application_Security, application_RESTInterface, Interface, application_OAuthClientScope, application_ConfigurableElement, SourceState, SourceActiveStates, PropertyTypes},
    associations={persistency0, dataSet1, mappingRules4, sources5, interfaces6, mashupAdmins8, mashup3, properties9, allMashupAdmins12, defaultMashups14, sourceConfigurations17, interfaceConfigurations20, mashups10, interface25, clients27, admins28, security22, mashup23, clientScope30, configuration34, configurableMashups32},
    generalizations={gen_application_Source_ConfigurableElement, gen_application_Mashup_Source, gen_application_XMLFile_Persistency, gen_application_Database_Persistency, gen_application_OCLRestrictedProperty_Property, gen_application_FEEDInterface_Interface, gen_application_OAuthConfig_Security, gen_application_Interface_ConfigurableElement, gen_application_ApplicationKeyConfig_Security, gen_application_RESTInterface_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)