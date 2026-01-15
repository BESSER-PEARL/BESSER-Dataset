from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PropertyTypes(Enum):
    Authorization = "Authorization"
    UploadZipFile = "UploadZipFile"
    UploadFile = "UploadFile"
    Boolean = "Boolean"
    String = "String"
    Integer = "Integer"
    Float = "Float"
    Date = "Date"
class SourceState(Enum):
    Active = "Active"
    Paused = "Paused"
    Error = "Error"
    Stoped = "Stoped"
class SourceActiveStates(Enum):
    Initializing = "Initializing"
    Initialized = "Initialized"
    Filling = "Filling"
    Filled = "Filled"
    WaitingForUpdate = "WaitingForUpdate"
    Updating = "Updating"
    Enriching = "Enriching"
    Unknown = "Unknown"


############################################
# Definition of Classes
############################################

class application_ConfigurableElement(ABC):

    def __init__(self, name: str, configurationImage: str, description: str, changeable: str, hidden: str, ident: str, application_ConfigurableElement: "application_Configuration" = None):
        self.name = name
        self.configurationImage = configurationImage
        self.description = description
        self.changeable = changeable
        self.hidden = hidden
        self.ident = ident
        self.application_ConfigurableElement = application_ConfigurableElement
        
    @property
    def hidden(self) -> str:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden

    @property
    def changeable(self) -> str:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: str):
        self.__changeable = changeable

    @property
    def ident(self) -> str:
        return self.__ident

    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def configurationImage(self) -> str:
        return self.__configurationImage

    @configurationImage.setter
    def configurationImage(self, configurationImage: str):
        self.__configurationImage = configurationImage

    @property
    def application_ConfigurableElement(self):
        return self.__application_ConfigurableElement

    @application_ConfigurableElement.setter
    def application_ConfigurableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ConfigurableElement__application_ConfigurableElement", None)
        self.__application_ConfigurableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Configuration35"):
                opp_val = getattr(old_value, "application_Configuration35", None)
                if opp_val == self:
                    setattr(old_value, "application_Configuration35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Configuration35"):
                opp_val = getattr(value, "application_Configuration35", None)
                setattr(value, "application_Configuration35", self)

    def isPropertyTrue(self, key: str) -> bool:
        # TODO: Implement isPropertyTrue method
        pass

    def isPropertyTrueElseDefault(self, key: str, defaultValue: str) -> bool:
        # TODO: Implement isPropertyTrueElseDefault method
        pass

    def addProperty(self, property: Property):
        # TODO: Implement addProperty method
        pass

    def getPropertyValue(self, key: str) -> str:
        # TODO: Implement getPropertyValue method
        pass

    def addProperty(self, value: str, key: str):
        # TODO: Implement addProperty method
        pass

    def getPropertyValueElseDefault(self, defaultValue: str, key: str) -> str:
        # TODO: Implement getPropertyValueElseDefault method
        pass

    def getProperty(self, key: str) -> Property:
        # TODO: Implement getProperty method
        pass

    def removeProperty(self, key: str):
        # TODO: Implement removeProperty method
        pass

class application_OAuthClientScope:

    def __init__(self, positiveTag: str, negativeTag: str, positiveMetaTag: str, negativeMetaTag: str, positiveCategory: str, negativeCategory: str, positivePerson: str, negativePerson: str, positiveOrganisation: str, negativeOrganisation: str, identSpecification: str, allowPersons: str, allowContents: str, allowOrganisations: str, maximumAge: str, application_OAuthClientScope: "application_OAuthClientConfig" = None):
        self.positiveTag = positiveTag
        self.negativeTag = negativeTag
        self.positiveMetaTag = positiveMetaTag
        self.negativeMetaTag = negativeMetaTag
        self.positiveCategory = positiveCategory
        self.negativeCategory = negativeCategory
        self.positivePerson = positivePerson
        self.negativePerson = negativePerson
        self.positiveOrganisation = positiveOrganisation
        self.negativeOrganisation = negativeOrganisation
        self.identSpecification = identSpecification
        self.allowPersons = allowPersons
        self.allowContents = allowContents
        self.allowOrganisations = allowOrganisations
        self.maximumAge = maximumAge
        self.application_OAuthClientScope = application_OAuthClientScope
        
    @property
    def allowContents(self) -> str:
        return self.__allowContents

    @allowContents.setter
    def allowContents(self, allowContents: str):
        self.__allowContents = allowContents

    @property
    def positivePerson(self) -> str:
        return self.__positivePerson

    @positivePerson.setter
    def positivePerson(self, positivePerson: str):
        self.__positivePerson = positivePerson

    @property
    def negativeCategory(self) -> str:
        return self.__negativeCategory

    @negativeCategory.setter
    def negativeCategory(self, negativeCategory: str):
        self.__negativeCategory = negativeCategory

    @property
    def negativePerson(self) -> str:
        return self.__negativePerson

    @negativePerson.setter
    def negativePerson(self, negativePerson: str):
        self.__negativePerson = negativePerson

    @property
    def positiveCategory(self) -> str:
        return self.__positiveCategory

    @positiveCategory.setter
    def positiveCategory(self, positiveCategory: str):
        self.__positiveCategory = positiveCategory

    @property
    def allowPersons(self) -> str:
        return self.__allowPersons

    @allowPersons.setter
    def allowPersons(self, allowPersons: str):
        self.__allowPersons = allowPersons

    @property
    def negativeTag(self) -> str:
        return self.__negativeTag

    @negativeTag.setter
    def negativeTag(self, negativeTag: str):
        self.__negativeTag = negativeTag

    @property
    def negativeMetaTag(self) -> str:
        return self.__negativeMetaTag

    @negativeMetaTag.setter
    def negativeMetaTag(self, negativeMetaTag: str):
        self.__negativeMetaTag = negativeMetaTag

    @property
    def positiveOrganisation(self) -> str:
        return self.__positiveOrganisation

    @positiveOrganisation.setter
    def positiveOrganisation(self, positiveOrganisation: str):
        self.__positiveOrganisation = positiveOrganisation

    @property
    def negativeOrganisation(self) -> str:
        return self.__negativeOrganisation

    @negativeOrganisation.setter
    def negativeOrganisation(self, negativeOrganisation: str):
        self.__negativeOrganisation = negativeOrganisation

    @property
    def identSpecification(self) -> str:
        return self.__identSpecification

    @identSpecification.setter
    def identSpecification(self, identSpecification: str):
        self.__identSpecification = identSpecification

    @property
    def positiveTag(self) -> str:
        return self.__positiveTag

    @positiveTag.setter
    def positiveTag(self, positiveTag: str):
        self.__positiveTag = positiveTag

    @property
    def maximumAge(self) -> str:
        return self.__maximumAge

    @maximumAge.setter
    def maximumAge(self, maximumAge: str):
        self.__maximumAge = maximumAge

    @property
    def positiveMetaTag(self) -> str:
        return self.__positiveMetaTag

    @positiveMetaTag.setter
    def positiveMetaTag(self, positiveMetaTag: str):
        self.__positiveMetaTag = positiveMetaTag

    @property
    def allowOrganisations(self) -> str:
        return self.__allowOrganisations

    @allowOrganisations.setter
    def allowOrganisations(self, allowOrganisations: str):
        self.__allowOrganisations = allowOrganisations

    @property
    def application_OAuthClientScope(self):
        return self.__application_OAuthClientScope

    @application_OAuthClientScope.setter
    def application_OAuthClientScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_OAuthClientScope__application_OAuthClientScope", None)
        self.__application_OAuthClientScope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_OAuthClientConfig31"):
                opp_val = getattr(old_value, "application_OAuthClientConfig31", None)
                if opp_val == self:
                    setattr(old_value, "application_OAuthClientConfig31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_OAuthClientConfig31"):
                opp_val = getattr(value, "application_OAuthClientConfig31", None)
                setattr(value, "application_OAuthClientConfig31", self)

class application_OAuthAdmin:

    def __init__(self, username: str, passwordHash: str, application_OAuthAdmin: "application_OAuthConfig" = None):
        self.username = username
        self.passwordHash = passwordHash
        self.application_OAuthAdmin = application_OAuthAdmin
        
    @property
    def passwordHash(self) -> str:
        return self.__passwordHash

    @passwordHash.setter
    def passwordHash(self, passwordHash: str):
        self.__passwordHash = passwordHash

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def application_OAuthAdmin(self):
        return self.__application_OAuthAdmin

    @application_OAuthAdmin.setter
    def application_OAuthAdmin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_OAuthAdmin__application_OAuthAdmin", None)
        self.__application_OAuthAdmin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_OAuthConfig29"):
                opp_val = getattr(old_value, "application_OAuthConfig29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_OAuthConfig29"):
                opp_val = getattr(value, "application_OAuthConfig29", None)
                if opp_val is None:
                    setattr(value, "application_OAuthConfig29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class application_OAuthClientConfig:

    def __init__(self, name: str, description: str, clientID: str, type: str, redirectionURL: str, clientSecret: str, code: str, grantType: str, refreshToken: str, accessToken: str, accessTokenCreationDate: date, accessTokenExpirationDate: date, forbiddenMetaTags: str, allowedMetaTags: str, oAuthScopeLevel: str, application_OAuthClientConfig: "application_OAuthConfig" = None, application_OAuthClientConfig31: "application_OAuthClientScope" = None):
        self.name = name
        self.description = description
        self.clientID = clientID
        self.type = type
        self.redirectionURL = redirectionURL
        self.clientSecret = clientSecret
        self.code = code
        self.grantType = grantType
        self.refreshToken = refreshToken
        self.accessToken = accessToken
        self.accessTokenCreationDate = accessTokenCreationDate
        self.accessTokenExpirationDate = accessTokenExpirationDate
        self.forbiddenMetaTags = forbiddenMetaTags
        self.allowedMetaTags = allowedMetaTags
        self.oAuthScopeLevel = oAuthScopeLevel
        self.application_OAuthClientConfig = application_OAuthClientConfig
        self.application_OAuthClientConfig31 = application_OAuthClientConfig31
        
    @property
    def accessTokenExpirationDate(self) -> date:
        return self.__accessTokenExpirationDate

    @accessTokenExpirationDate.setter
    def accessTokenExpirationDate(self, accessTokenExpirationDate: date):
        self.__accessTokenExpirationDate = accessTokenExpirationDate

    @property
    def clientID(self) -> str:
        return self.__clientID

    @clientID.setter
    def clientID(self, clientID: str):
        self.__clientID = clientID

    @property
    def clientSecret(self) -> str:
        return self.__clientSecret

    @clientSecret.setter
    def clientSecret(self, clientSecret: str):
        self.__clientSecret = clientSecret

    @property
    def forbiddenMetaTags(self) -> str:
        return self.__forbiddenMetaTags

    @forbiddenMetaTags.setter
    def forbiddenMetaTags(self, forbiddenMetaTags: str):
        self.__forbiddenMetaTags = forbiddenMetaTags

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def refreshToken(self) -> str:
        return self.__refreshToken

    @refreshToken.setter
    def refreshToken(self, refreshToken: str):
        self.__refreshToken = refreshToken

    @property
    def redirectionURL(self) -> str:
        return self.__redirectionURL

    @redirectionURL.setter
    def redirectionURL(self, redirectionURL: str):
        self.__redirectionURL = redirectionURL

    @property
    def accessToken(self) -> str:
        return self.__accessToken

    @accessToken.setter
    def accessToken(self, accessToken: str):
        self.__accessToken = accessToken

    @property
    def grantType(self) -> str:
        return self.__grantType

    @grantType.setter
    def grantType(self, grantType: str):
        self.__grantType = grantType

    @property
    def oAuthScopeLevel(self) -> str:
        return self.__oAuthScopeLevel

    @oAuthScopeLevel.setter
    def oAuthScopeLevel(self, oAuthScopeLevel: str):
        self.__oAuthScopeLevel = oAuthScopeLevel

    @property
    def accessTokenCreationDate(self) -> date:
        return self.__accessTokenCreationDate

    @accessTokenCreationDate.setter
    def accessTokenCreationDate(self, accessTokenCreationDate: date):
        self.__accessTokenCreationDate = accessTokenCreationDate

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def allowedMetaTags(self) -> str:
        return self.__allowedMetaTags

    @allowedMetaTags.setter
    def allowedMetaTags(self, allowedMetaTags: str):
        self.__allowedMetaTags = allowedMetaTags

    @property
    def application_OAuthClientConfig(self):
        return self.__application_OAuthClientConfig

    @application_OAuthClientConfig.setter
    def application_OAuthClientConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_OAuthClientConfig__application_OAuthClientConfig", None)
        self.__application_OAuthClientConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_OAuthConfig"):
                opp_val = getattr(old_value, "application_OAuthConfig", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_OAuthConfig"):
                opp_val = getattr(value, "application_OAuthConfig", None)
                if opp_val is None:
                    setattr(value, "application_OAuthConfig", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_OAuthClientConfig31(self):
        return self.__application_OAuthClientConfig31

    @application_OAuthClientConfig31.setter
    def application_OAuthClientConfig31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_OAuthClientConfig__application_OAuthClientConfig31", None)
        self.__application_OAuthClientConfig31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_OAuthClientScope"):
                opp_val = getattr(old_value, "application_OAuthClientScope", None)
                if opp_val == self:
                    setattr(old_value, "application_OAuthClientScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_OAuthClientScope"):
                opp_val = getattr(value, "application_OAuthClientScope", None)
                setattr(value, "application_OAuthClientScope", self)

class Security:

    pass
class application_ApplicationKeyConfig(Security):

    def __init__(self, applicationKeys: str):
        self.applicationKeys = applicationKeys
        
    @property
    def applicationKeys(self) -> str:
        return self.__applicationKeys

    @applicationKeys.setter
    def applicationKeys(self, applicationKeys: str):
        self.__applicationKeys = applicationKeys

    def hasApplicationKey(self, applicationKey: str) -> str:
        # TODO: Implement hasApplicationKey method
        pass

class application_OAuthConfig(Security):

    def __init__(self, useScopeInterfaceOnRedirect: str, application_OAuthConfig: set["application_OAuthClientConfig"] = None, application_OAuthConfig29: set["application_OAuthAdmin"] = None):
        self.useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect
        self.application_OAuthConfig = application_OAuthConfig if application_OAuthConfig is not None else set()
        self.application_OAuthConfig29 = application_OAuthConfig29 if application_OAuthConfig29 is not None else set()
        
    @property
    def useScopeInterfaceOnRedirect(self) -> str:
        return self.__useScopeInterfaceOnRedirect

    @useScopeInterfaceOnRedirect.setter
    def useScopeInterfaceOnRedirect(self, useScopeInterfaceOnRedirect: str):
        self.__useScopeInterfaceOnRedirect = useScopeInterfaceOnRedirect

    @property
    def application_OAuthConfig(self):
        return self.__application_OAuthConfig

    @application_OAuthConfig.setter
    def application_OAuthConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_OAuthConfig__application_OAuthConfig", None)
        self.__application_OAuthConfig = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_OAuthClientConfig"):
                    opp_val = getattr(item, "application_OAuthClientConfig", None)
                    
                    if opp_val == self:
                        setattr(item, "application_OAuthClientConfig", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_OAuthClientConfig"):
                    opp_val = getattr(item, "application_OAuthClientConfig", None)
                    
                    setattr(item, "application_OAuthClientConfig", self)
                    

    @property
    def application_OAuthConfig29(self):
        return self.__application_OAuthConfig29

    @application_OAuthConfig29.setter
    def application_OAuthConfig29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_OAuthConfig__application_OAuthConfig29", None)
        self.__application_OAuthConfig29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_OAuthAdmin"):
                    opp_val = getattr(item, "application_OAuthAdmin", None)
                    
                    if opp_val == self:
                        setattr(item, "application_OAuthAdmin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_OAuthAdmin"):
                    opp_val = getattr(item, "application_OAuthAdmin", None)
                    
                    setattr(item, "application_OAuthAdmin", self)
                    

class Interface:

    pass
class application_FEEDInterface(Interface):

    def __init__(self, allowPersonFiltering: str, allowOrganisationFiltering: str, allowTypeFiltering: str, allowTagFiltering: str, allowMetaTagFiltering: str, allowCategoryFiltering: str, language: str, feedType: str, feedTitle: str):
        self.allowPersonFiltering = allowPersonFiltering
        self.allowOrganisationFiltering = allowOrganisationFiltering
        self.allowTypeFiltering = allowTypeFiltering
        self.allowTagFiltering = allowTagFiltering
        self.allowMetaTagFiltering = allowMetaTagFiltering
        self.allowCategoryFiltering = allowCategoryFiltering
        self.language = language
        self.feedType = feedType
        self.feedTitle = feedTitle
        
    @property
    def allowOrganisationFiltering(self) -> str:
        return self.__allowOrganisationFiltering

    @allowOrganisationFiltering.setter
    def allowOrganisationFiltering(self, allowOrganisationFiltering: str):
        self.__allowOrganisationFiltering = allowOrganisationFiltering

    @property
    def allowCategoryFiltering(self) -> str:
        return self.__allowCategoryFiltering

    @allowCategoryFiltering.setter
    def allowCategoryFiltering(self, allowCategoryFiltering: str):
        self.__allowCategoryFiltering = allowCategoryFiltering

    @property
    def allowMetaTagFiltering(self) -> str:
        return self.__allowMetaTagFiltering

    @allowMetaTagFiltering.setter
    def allowMetaTagFiltering(self, allowMetaTagFiltering: str):
        self.__allowMetaTagFiltering = allowMetaTagFiltering

    @property
    def allowPersonFiltering(self) -> str:
        return self.__allowPersonFiltering

    @allowPersonFiltering.setter
    def allowPersonFiltering(self, allowPersonFiltering: str):
        self.__allowPersonFiltering = allowPersonFiltering

    @property
    def feedTitle(self) -> str:
        return self.__feedTitle

    @feedTitle.setter
    def feedTitle(self, feedTitle: str):
        self.__feedTitle = feedTitle

    @property
    def allowTypeFiltering(self) -> str:
        return self.__allowTypeFiltering

    @allowTypeFiltering.setter
    def allowTypeFiltering(self, allowTypeFiltering: str):
        self.__allowTypeFiltering = allowTypeFiltering

    @property
    def allowTagFiltering(self) -> str:
        return self.__allowTagFiltering

    @allowTagFiltering.setter
    def allowTagFiltering(self, allowTagFiltering: str):
        self.__allowTagFiltering = allowTagFiltering

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def feedType(self) -> str:
        return self.__feedType

    @feedType.setter
    def feedType(self, feedType: str):
        self.__feedType = feedType

class application_RESTInterface(Interface):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class application_MashupContainer:

    def __init__(self, immediateSave: str, createAccountsAtLoginTry: str, identCounter: str, backupConfiguration: str, backupIntervall: str, application_MashupContainer18: set["application_Mashup"] = None, application_MashupContainer21: set["application_Interface"] = None, application_MashupContainer: set["application_Mashup"] = None, application_MashupContainer13: set["application_MashupAdmin"] = None, application_MashupContainer15: set["application_Mashup"] = None):
        self.immediateSave = immediateSave
        self.createAccountsAtLoginTry = createAccountsAtLoginTry
        self.identCounter = identCounter
        self.backupConfiguration = backupConfiguration
        self.backupIntervall = backupIntervall
        self.application_MashupContainer18 = application_MashupContainer18 if application_MashupContainer18 is not None else set()
        self.application_MashupContainer21 = application_MashupContainer21 if application_MashupContainer21 is not None else set()
        self.application_MashupContainer = application_MashupContainer if application_MashupContainer is not None else set()
        self.application_MashupContainer13 = application_MashupContainer13 if application_MashupContainer13 is not None else set()
        self.application_MashupContainer15 = application_MashupContainer15 if application_MashupContainer15 is not None else set()
        
    @property
    def backupIntervall(self) -> str:
        return self.__backupIntervall

    @backupIntervall.setter
    def backupIntervall(self, backupIntervall: str):
        self.__backupIntervall = backupIntervall

    @property
    def immediateSave(self) -> str:
        return self.__immediateSave

    @immediateSave.setter
    def immediateSave(self, immediateSave: str):
        self.__immediateSave = immediateSave

    @property
    def createAccountsAtLoginTry(self) -> str:
        return self.__createAccountsAtLoginTry

    @createAccountsAtLoginTry.setter
    def createAccountsAtLoginTry(self, createAccountsAtLoginTry: str):
        self.__createAccountsAtLoginTry = createAccountsAtLoginTry

    @property
    def backupConfiguration(self) -> str:
        return self.__backupConfiguration

    @backupConfiguration.setter
    def backupConfiguration(self, backupConfiguration: str):
        self.__backupConfiguration = backupConfiguration

    @property
    def identCounter(self) -> str:
        return self.__identCounter

    @identCounter.setter
    def identCounter(self, identCounter: str):
        self.__identCounter = identCounter

    @property
    def application_MashupContainer21(self):
        return self.__application_MashupContainer21

    @application_MashupContainer21.setter
    def application_MashupContainer21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupContainer__application_MashupContainer21", None)
        self.__application_MashupContainer21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Interface"):
                    opp_val = getattr(item, "application_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Interface"):
                    opp_val = getattr(item, "application_Interface", None)
                    
                    setattr(item, "application_Interface", self)
                    

    @property
    def application_MashupContainer18(self):
        return self.__application_MashupContainer18

    @application_MashupContainer18.setter
    def application_MashupContainer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupContainer__application_MashupContainer18", None)
        self.__application_MashupContainer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Mashup19"):
                    opp_val = getattr(item, "application_Mashup19", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Mashup19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Mashup19"):
                    opp_val = getattr(item, "application_Mashup19", None)
                    
                    setattr(item, "application_Mashup19", self)
                    

    @property
    def application_MashupContainer15(self):
        return self.__application_MashupContainer15

    @application_MashupContainer15.setter
    def application_MashupContainer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupContainer__application_MashupContainer15", None)
        self.__application_MashupContainer15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Mashup16"):
                    opp_val = getattr(item, "application_Mashup16", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Mashup16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Mashup16"):
                    opp_val = getattr(item, "application_Mashup16", None)
                    
                    setattr(item, "application_Mashup16", self)
                    

    @property
    def application_MashupContainer(self):
        return self.__application_MashupContainer

    @application_MashupContainer.setter
    def application_MashupContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupContainer__application_MashupContainer", None)
        self.__application_MashupContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Mashup11"):
                    opp_val = getattr(item, "application_Mashup11", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Mashup11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Mashup11"):
                    opp_val = getattr(item, "application_Mashup11", None)
                    
                    setattr(item, "application_Mashup11", self)
                    

    @property
    def application_MashupContainer13(self):
        return self.__application_MashupContainer13

    @application_MashupContainer13.setter
    def application_MashupContainer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupContainer__application_MashupContainer13", None)
        self.__application_MashupContainer13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_MashupAdmin"):
                    opp_val = getattr(item, "application_MashupAdmin", None)
                    
                    if opp_val == self:
                        setattr(item, "application_MashupAdmin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_MashupAdmin"):
                    opp_val = getattr(item, "application_MashupAdmin", None)
                    
                    setattr(item, "application_MashupAdmin", self)
                    

    def getSourceConfigurationWithIdent(self, ident: str) -> Source:
        # TODO: Implement getSourceConfigurationWithIdent method
        pass

    def getNewIdentNumber(self) -> str:
        # TODO: Implement getNewIdentNumber method
        pass

    def getMashupWithIdent(self, ident: str) -> str:
        # TODO: Implement getMashupWithIdent method
        pass

    def getConfigurationAdmins(self) -> str:
        # TODO: Implement getConfigurationAdmins method
        pass

    def setNewIdentFor(self, configurableElement: ConfigurableElement):
        # TODO: Implement setNewIdentFor method
        pass

class Property:

    pass
class application_OCLRestrictedProperty(Property):

    def __init__(self, OCLRestriction: str):
        self.OCLRestriction = OCLRestriction
        
    @property
    def OCLRestriction(self) -> str:
        return self.__OCLRestriction

    @OCLRestriction.setter
    def OCLRestriction(self, OCLRestriction: str):
        self.__OCLRestriction = OCLRestriction

class application_Security(ABC):

    pass
class Persistency:

    pass
class application_Database(Persistency):

    pass
class application_XMLFile(Persistency):

    pass
class application_Property:

    def __init__(self, Key: str, Value: str, hidden: str, changeable: str, possibleValues: str, helpText: str, required: str, propertyType: str, application_Property: "application_Configuration" = None):
        self.Key = Key
        self.Value = Value
        self.hidden = hidden
        self.changeable = changeable
        self.possibleValues = possibleValues
        self.helpText = helpText
        self.required = required
        self.propertyType = propertyType
        self.application_Property = application_Property
        
    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def changeable(self) -> str:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: str):
        self.__changeable = changeable

    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def helpText(self) -> str:
        return self.__helpText

    @helpText.setter
    def helpText(self, helpText: str):
        self.__helpText = helpText

    @property
    def hidden(self) -> str:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden

    @property
    def Key(self) -> str:
        return self.__Key

    @Key.setter
    def Key(self, Key: str):
        self.__Key = Key

    @property
    def propertyType(self) -> str:
        return self.__propertyType

    @propertyType.setter
    def propertyType(self, propertyType: str):
        self.__propertyType = propertyType

    @property
    def possibleValues(self) -> str:
        return self.__possibleValues

    @possibleValues.setter
    def possibleValues(self, possibleValues: str):
        self.__possibleValues = possibleValues

    @property
    def application_Property(self):
        return self.__application_Property

    @application_Property.setter
    def application_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Property__application_Property", None)
        self.__application_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Configuration"):
                opp_val = getattr(old_value, "application_Configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Configuration"):
                opp_val = getattr(value, "application_Configuration", None)
                if opp_val is None:
                    setattr(value, "application_Configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getListOfValues(self) -> str:
        # TODO: Implement getListOfValues method
        pass

    def getMinValue(self) -> str:
        # TODO: Implement getMinValue method
        pass

    def isValueRange(self) -> bool:
        # TODO: Implement isValueRange method
        pass

    def getMaxValue(self) -> str:
        # TODO: Implement getMaxValue method
        pass

    def isValueList(self) -> bool:
        # TODO: Implement isValueList method
        pass

class application_Configuration:

    pass
class Source:

    pass
class application_Mashup(Source):

    def __init__(self, workingDirectory: str, cacheAttachments: str, cacheDataSet: str, backupDataSet: str, backupIntervall: str, cacheDelay: str, sourceIdentCounter: str, keepDeletedItemsList: str, application_Mashup: set["application_MappingRule"] = None, mashup: set["application_Source"] = None, mashup7: set["application_Interface"] = None, configurableMashups: set["application_MashupAdmin"] = None, Mashup: "application_Source" = None, application_Mashup19: "application_MashupContainer" = None, application_Mashup11: "application_MashupContainer" = None, application_Mashup16: "application_MashupContainer" = None, Mashup24: "application_Interface" = None, Mashup33: "application_MashupAdmin" = None):
        self.workingDirectory = workingDirectory
        self.cacheAttachments = cacheAttachments
        self.cacheDataSet = cacheDataSet
        self.backupDataSet = backupDataSet
        self.backupIntervall = backupIntervall
        self.cacheDelay = cacheDelay
        self.sourceIdentCounter = sourceIdentCounter
        self.keepDeletedItemsList = keepDeletedItemsList
        self.application_Mashup = application_Mashup if application_Mashup is not None else set()
        self.mashup = mashup if mashup is not None else set()
        self.mashup7 = mashup7 if mashup7 is not None else set()
        self.configurableMashups = configurableMashups if configurableMashups is not None else set()
        self.Mashup = Mashup
        self.application_Mashup19 = application_Mashup19
        self.application_Mashup11 = application_Mashup11
        self.application_Mashup16 = application_Mashup16
        self.Mashup24 = Mashup24
        self.Mashup33 = Mashup33
        
    @property
    def cacheDataSet(self) -> str:
        return self.__cacheDataSet

    @cacheDataSet.setter
    def cacheDataSet(self, cacheDataSet: str):
        self.__cacheDataSet = cacheDataSet

    @property
    def cacheAttachments(self) -> str:
        return self.__cacheAttachments

    @cacheAttachments.setter
    def cacheAttachments(self, cacheAttachments: str):
        self.__cacheAttachments = cacheAttachments

    @property
    def keepDeletedItemsList(self) -> str:
        return self.__keepDeletedItemsList

    @keepDeletedItemsList.setter
    def keepDeletedItemsList(self, keepDeletedItemsList: str):
        self.__keepDeletedItemsList = keepDeletedItemsList

    @property
    def cacheDelay(self) -> str:
        return self.__cacheDelay

    @cacheDelay.setter
    def cacheDelay(self, cacheDelay: str):
        self.__cacheDelay = cacheDelay

    @property
    def sourceIdentCounter(self) -> str:
        return self.__sourceIdentCounter

    @sourceIdentCounter.setter
    def sourceIdentCounter(self, sourceIdentCounter: str):
        self.__sourceIdentCounter = sourceIdentCounter

    @property
    def workingDirectory(self) -> str:
        return self.__workingDirectory

    @workingDirectory.setter
    def workingDirectory(self, workingDirectory: str):
        self.__workingDirectory = workingDirectory

    @property
    def backupIntervall(self) -> str:
        return self.__backupIntervall

    @backupIntervall.setter
    def backupIntervall(self, backupIntervall: str):
        self.__backupIntervall = backupIntervall

    @property
    def backupDataSet(self) -> str:
        return self.__backupDataSet

    @backupDataSet.setter
    def backupDataSet(self, backupDataSet: str):
        self.__backupDataSet = backupDataSet

    @property
    def mashup(self):
        return self.__mashup

    @mashup.setter
    def mashup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__mashup", None)
        self.__mashup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    if opp_val == self:
                        setattr(item, "Source", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    setattr(item, "Source", self)
                    

    @property
    def Mashup(self):
        return self.__Mashup

    @Mashup.setter
    def Mashup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__Mashup", None)
        self.__Mashup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if opp_val == self:
                    setattr(old_value, "sources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                setattr(value, "sources", self)

    @property
    def application_Mashup11(self):
        return self.__application_Mashup11

    @application_Mashup11.setter
    def application_Mashup11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__application_Mashup11", None)
        self.__application_Mashup11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_MashupContainer"):
                opp_val = getattr(old_value, "application_MashupContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_MashupContainer"):
                opp_val = getattr(value, "application_MashupContainer", None)
                if opp_val is None:
                    setattr(value, "application_MashupContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_Mashup(self):
        return self.__application_Mashup

    @application_Mashup.setter
    def application_Mashup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__application_Mashup", None)
        self.__application_Mashup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_MappingRule"):
                    opp_val = getattr(item, "application_MappingRule", None)
                    
                    if opp_val == self:
                        setattr(item, "application_MappingRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_MappingRule"):
                    opp_val = getattr(item, "application_MappingRule", None)
                    
                    setattr(item, "application_MappingRule", self)
                    

    @property
    def application_Mashup19(self):
        return self.__application_Mashup19

    @application_Mashup19.setter
    def application_Mashup19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__application_Mashup19", None)
        self.__application_Mashup19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_MashupContainer18"):
                opp_val = getattr(old_value, "application_MashupContainer18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_MashupContainer18"):
                opp_val = getattr(value, "application_MashupContainer18", None)
                if opp_val is None:
                    setattr(value, "application_MashupContainer18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def configurableMashups(self):
        return self.__configurableMashups

    @configurableMashups.setter
    def configurableMashups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__configurableMashups", None)
        self.__configurableMashups = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MashupAdmin"):
                    opp_val = getattr(item, "MashupAdmin", None)
                    
                    if opp_val == self:
                        setattr(item, "MashupAdmin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MashupAdmin"):
                    opp_val = getattr(item, "MashupAdmin", None)
                    
                    setattr(item, "MashupAdmin", self)
                    

    @property
    def Mashup33(self):
        return self.__Mashup33

    @Mashup33.setter
    def Mashup33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__Mashup33", None)
        self.__Mashup33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mashupAdmins"):
                opp_val = getattr(old_value, "mashupAdmins", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mashupAdmins"):
                opp_val = getattr(value, "mashupAdmins", None)
                if opp_val is None:
                    setattr(value, "mashupAdmins", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Mashup24(self):
        return self.__Mashup24

    @Mashup24.setter
    def Mashup24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__Mashup24", None)
        self.__Mashup24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interfaces"):
                opp_val = getattr(old_value, "interfaces", None)
                if opp_val == self:
                    setattr(old_value, "interfaces", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interfaces"):
                opp_val = getattr(value, "interfaces", None)
                setattr(value, "interfaces", self)

    @property
    def application_Mashup16(self):
        return self.__application_Mashup16

    @application_Mashup16.setter
    def application_Mashup16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__application_Mashup16", None)
        self.__application_Mashup16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_MashupContainer15"):
                opp_val = getattr(old_value, "application_MashupContainer15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_MashupContainer15"):
                opp_val = getattr(value, "application_MashupContainer15", None)
                if opp_val is None:
                    setattr(value, "application_MashupContainer15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mashup7(self):
        return self.__mashup7

    @mashup7.setter
    def mashup7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Mashup__mashup7", None)
        self.__mashup7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    setattr(item, "Interface", self)
                    

    def getSourceWithIdent(self, ident: str) -> Source:
        # TODO: Implement getSourceWithIdent method
        pass

    def getNewSourceIdent(self) -> str:
        # TODO: Implement getNewSourceIdent method
        pass

class application_DataSet:

    pass
class application_Persistency:

    pass
class application_MashupAdmin:

    def __init__(self, provider: str, id: str, name: str, localIdent: str, isConfigurationAdmin: str, profileImage: str, email: str, MashupAdmin: "application_Mashup" = None, application_MashupAdmin: "application_MashupContainer" = None, mashupAdmins: set["application_Mashup"] = None):
        self.provider = provider
        self.id = id
        self.name = name
        self.localIdent = localIdent
        self.isConfigurationAdmin = isConfigurationAdmin
        self.profileImage = profileImage
        self.email = email
        self.MashupAdmin = MashupAdmin
        self.application_MashupAdmin = application_MashupAdmin
        self.mashupAdmins = mashupAdmins if mashupAdmins is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isConfigurationAdmin(self) -> str:
        return self.__isConfigurationAdmin

    @isConfigurationAdmin.setter
    def isConfigurationAdmin(self, isConfigurationAdmin: str):
        self.__isConfigurationAdmin = isConfigurationAdmin

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def profileImage(self) -> str:
        return self.__profileImage

    @profileImage.setter
    def profileImage(self, profileImage: str):
        self.__profileImage = profileImage

    @property
    def localIdent(self) -> str:
        return self.__localIdent

    @localIdent.setter
    def localIdent(self, localIdent: str):
        self.__localIdent = localIdent

    @property
    def application_MashupAdmin(self):
        return self.__application_MashupAdmin

    @application_MashupAdmin.setter
    def application_MashupAdmin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupAdmin__application_MashupAdmin", None)
        self.__application_MashupAdmin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_MashupContainer13"):
                opp_val = getattr(old_value, "application_MashupContainer13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_MashupContainer13"):
                opp_val = getattr(value, "application_MashupContainer13", None)
                if opp_val is None:
                    setattr(value, "application_MashupContainer13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MashupAdmin(self):
        return self.__MashupAdmin

    @MashupAdmin.setter
    def MashupAdmin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupAdmin__MashupAdmin", None)
        self.__MashupAdmin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configurableMashups"):
                opp_val = getattr(old_value, "configurableMashups", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configurableMashups"):
                opp_val = getattr(value, "configurableMashups", None)
                if opp_val is None:
                    setattr(value, "configurableMashups", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mashupAdmins(self):
        return self.__mashupAdmins

    @mashupAdmins.setter
    def mashupAdmins(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_MashupAdmin__mashupAdmins", None)
        self.__mashupAdmins = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Mashup33"):
                    opp_val = getattr(item, "Mashup33", None)
                    
                    if opp_val == self:
                        setattr(item, "Mashup33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Mashup33"):
                    opp_val = getattr(item, "Mashup33", None)
                    
                    setattr(item, "Mashup33", self)
                    

class application_MappingRule:

    pass
class ConfigurableElement:

    pass
class application_Interface(ConfigurableElement):

    def __init__(self, urlSuffix: str, frontEndCaching: str, Interface: "application_Mashup" = None, application_Interface: "application_MashupContainer" = None, interface: "application_Security" = None, Interface26: "application_Security" = None, interfaces: "application_Mashup" = None):
        self.urlSuffix = urlSuffix
        self.frontEndCaching = frontEndCaching
        self.Interface = Interface
        self.application_Interface = application_Interface
        self.interface = interface
        self.Interface26 = Interface26
        self.interfaces = interfaces
        
    @property
    def frontEndCaching(self) -> str:
        return self.__frontEndCaching

    @frontEndCaching.setter
    def frontEndCaching(self, frontEndCaching: str):
        self.__frontEndCaching = frontEndCaching

    @property
    def urlSuffix(self) -> str:
        return self.__urlSuffix

    @urlSuffix.setter
    def urlSuffix(self, urlSuffix: str):
        self.__urlSuffix = urlSuffix

    @property
    def application_Interface(self):
        return self.__application_Interface

    @application_Interface.setter
    def application_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Interface__application_Interface", None)
        self.__application_Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_MashupContainer21"):
                opp_val = getattr(old_value, "application_MashupContainer21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_MashupContainer21"):
                opp_val = getattr(value, "application_MashupContainer21", None)
                if opp_val is None:
                    setattr(value, "application_MashupContainer21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Interface__Interface", None)
        self.__Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mashup7"):
                opp_val = getattr(old_value, "mashup7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mashup7"):
                opp_val = getattr(value, "mashup7", None)
                if opp_val is None:
                    setattr(value, "mashup7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interfaces(self):
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Interface__interfaces", None)
        self.__interfaces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mashup24"):
                opp_val = getattr(old_value, "Mashup24", None)
                if opp_val == self:
                    setattr(old_value, "Mashup24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mashup24"):
                opp_val = getattr(value, "Mashup24", None)
                setattr(value, "Mashup24", self)

    @property
    def Interface26(self):
        return self.__Interface26

    @Interface26.setter
    def Interface26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Interface__Interface26", None)
        self.__Interface26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "security"):
                opp_val = getattr(old_value, "security", None)
                if opp_val == self:
                    setattr(old_value, "security", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "security"):
                opp_val = getattr(value, "security", None)
                setattr(value, "security", self)

    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Interface__interface", None)
        self.__interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Security"):
                opp_val = getattr(old_value, "Security", None)
                if opp_val == self:
                    setattr(old_value, "Security", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Security"):
                opp_val = getattr(value, "Security", None)
                setattr(value, "Security", self)

class application_Source(ConfigurableElement):

    def __init__(self, bundleId: str, state: str, activeState: str, logLevel: str, removeDataOnStop: str, updateRound: str, Source: "application_Mashup" = None, application_Source: "application_Persistency" = None, application_Source2: "application_DataSet" = None, sources: "application_Mashup" = None):
        self.bundleId = bundleId
        self.state = state
        self.activeState = activeState
        self.logLevel = logLevel
        self.removeDataOnStop = removeDataOnStop
        self.updateRound = updateRound
        self.Source = Source
        self.application_Source = application_Source
        self.application_Source2 = application_Source2
        self.sources = sources
        
    @property
    def activeState(self) -> str:
        return self.__activeState

    @activeState.setter
    def activeState(self, activeState: str):
        self.__activeState = activeState

    @property
    def removeDataOnStop(self) -> str:
        return self.__removeDataOnStop

    @removeDataOnStop.setter
    def removeDataOnStop(self, removeDataOnStop: str):
        self.__removeDataOnStop = removeDataOnStop

    @property
    def logLevel(self) -> str:
        return self.__logLevel

    @logLevel.setter
    def logLevel(self, logLevel: str):
        self.__logLevel = logLevel

    @property
    def bundleId(self) -> str:
        return self.__bundleId

    @bundleId.setter
    def bundleId(self, bundleId: str):
        self.__bundleId = bundleId

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def updateRound(self) -> str:
        return self.__updateRound

    @updateRound.setter
    def updateRound(self, updateRound: str):
        self.__updateRound = updateRound

    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Source__sources", None)
        self.__sources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mashup"):
                opp_val = getattr(old_value, "Mashup", None)
                if opp_val == self:
                    setattr(old_value, "Mashup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mashup"):
                opp_val = getattr(value, "Mashup", None)
                setattr(value, "Mashup", self)

    @property
    def Source(self):
        return self.__Source

    @Source.setter
    def Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Source__Source", None)
        self.__Source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mashup"):
                opp_val = getattr(old_value, "mashup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mashup"):
                opp_val = getattr(value, "mashup", None)
                if opp_val is None:
                    setattr(value, "mashup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_Source2(self):
        return self.__application_Source2

    @application_Source2.setter
    def application_Source2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Source__application_Source2", None)
        self.__application_Source2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_DataSet"):
                opp_val = getattr(old_value, "application_DataSet", None)
                if opp_val == self:
                    setattr(old_value, "application_DataSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_DataSet"):
                opp_val = getattr(value, "application_DataSet", None)
                setattr(value, "application_DataSet", self)

    @property
    def application_Source(self):
        return self.__application_Source

    @application_Source.setter
    def application_Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Source__application_Source", None)
        self.__application_Source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Persistency"):
                opp_val = getattr(old_value, "application_Persistency", None)
                if opp_val == self:
                    setattr(old_value, "application_Persistency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Persistency"):
                opp_val = getattr(value, "application_Persistency", None)
                setattr(value, "application_Persistency", self)

    def stop(self):
        # TODO: Implement stop method
        pass

    def pause(self):
        # TODO: Implement pause method
        pass

    def start(self):
        # TODO: Implement start method
        pass

    def getLogLevelIntValue(self) -> str:
        # TODO: Implement getLogLevelIntValue method
        pass
