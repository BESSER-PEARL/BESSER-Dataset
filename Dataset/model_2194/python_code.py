from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResourceType(Enum):
    bundle = "bundle"
    file = "file"
    database = "database"
    classpath = "classpath"
class TranslationState(Enum):
    original = "original"
    translated = "translated"
class GenericStatus(Enum):
    booked = "booked"
    draft = "draft"
    inactive = "inactive"
    void = "void"
class EntityKind(Enum):
    category = "category"
    product_release = "product_release"
    tag = "tag"
    page = "page"
    person = "person"
    shop = "shop"
    product = "product"
    place = "place"
    task = "task"
    article = "article"
    banner_shop = "banner_shop"
class EClassStatus(Enum):
    unresolved = "unresolved"
    resolved = "resolved"
class ExpansionState(Enum):
    expanded = "expanded"
    unexpanded = "unexpanded"
class CustomerRoleStatus(Enum):
    active = "active"
    inactive = "inactive"
    void = "void"
class SignupSourceType(Enum):
    other = "other"
    google_search = "google_search"
    google_ads = "google_ads"
    facebook_ads = "facebook_ads"
    facebook_friend = "facebook_friend"
    alia_magazine = "alia_magazine"
class TenantSource(Enum):
    config = "config"
    repository = "repository"
    classpath = "classpath"
class JavaClassStatus(Enum):
    unresolved = "unresolved"
    resolved = "resolved"
class ProgressStatus(Enum):
    ok = "ok"
    error = "error"
    warning = "warning"
    deleted = "deleted"
    skipped = "skipped"
class ArchivalStatus(Enum):
    fresh = "fresh"
    archived = "archived"
class PublicationStatus(Enum):
    draft = "draft"
    published = "published"
    unpublished = "unpublished"
class Gender(Enum):
    unknown = "unknown"
    male = "male"
    female = "female"
class AccountStatus(Enum):
    draft = "draft"
    validated = "validated"
    active = "active"
    verified = "verified"
    inactive = "inactive"
    void = "void"
    unregister = "unregister"


############################################
# Definition of Classes
############################################

class commons_MongoSysConfig(ABC):

    def __init__(self, mongoUri: str):
        self.mongoUri = mongoUri
        
    @property
    def mongoUri(self) -> str:
        return self.__mongoUri

    @mongoUri.setter
    def mongoUri(self, mongoUri: str):
        self.__mongoUri = mongoUri

class Describable:

    pass
class commons_Geolocation:

    def __init__(self, latitude: str, longitude: str, elevation: str):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        
    @property
    def elevation(self) -> str:
        return self.__elevation

    @elevation.setter
    def elevation(self, elevation: str):
        self.__elevation = elevation

    @property
    def longitude(self) -> str:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: str):
        self.__longitude = longitude

    @property
    def latitude(self) -> str:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: str):
        self.__latitude = latitude

class Timestamped:

    pass
class SysConfig:

    pass
class commons_Revisionable(ABC):

    def __init__(self, guid: str, revision: str):
        self.guid = guid
        self.revision = revision
        
    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

class commons_FacebookAccessible:

    def __init__(self, facebookAccessToken: str):
        self.facebookAccessToken = facebookAccessToken
        
    @property
    def facebookAccessToken(self) -> str:
        return self.__facebookAccessToken

    @facebookAccessToken.setter
    def facebookAccessToken(self, facebookAccessToken: str):
        self.__facebookAccessToken = facebookAccessToken

class commons_FacebookIdentity:

    def __init__(self, facebookId: str, facebookUsername: str):
        self.facebookId = facebookId
        self.facebookUsername = facebookUsername
        
    @property
    def facebookId(self) -> str:
        return self.__facebookId

    @facebookId.setter
    def facebookId(self, facebookId: str):
        self.__facebookId = facebookId

    @property
    def facebookUsername(self) -> str:
        return self.__facebookUsername

    @facebookUsername.setter
    def facebookUsername(self, facebookUsername: str):
        self.__facebookUsername = facebookUsername

class commons_TwitterIdentity(ABC):

    def __init__(self, twitterId: str, twitterScreenName: str):
        self.twitterId = twitterId
        self.twitterScreenName = twitterScreenName
        
    @property
    def twitterScreenName(self) -> str:
        return self.__twitterScreenName

    @twitterScreenName.setter
    def twitterScreenName(self, twitterScreenName: str):
        self.__twitterScreenName = twitterScreenName

    @property
    def twitterId(self) -> str:
        return self.__twitterId

    @twitterId.setter
    def twitterId(self, twitterId: str):
        self.__twitterId = twitterId

class commons_TwitterAccessible(ABC):

    def __init__(self, twitterAccessToken: str, twitterAccessTokenSecret: str):
        self.twitterAccessToken = twitterAccessToken
        self.twitterAccessTokenSecret = twitterAccessTokenSecret
        
    @property
    def twitterAccessToken(self) -> str:
        return self.__twitterAccessToken

    @twitterAccessToken.setter
    def twitterAccessToken(self, twitterAccessToken: str):
        self.__twitterAccessToken = twitterAccessToken

    @property
    def twitterAccessTokenSecret(self) -> str:
        return self.__twitterAccessTokenSecret

    @twitterAccessTokenSecret.setter
    def twitterAccessTokenSecret(self, twitterAccessTokenSecret: str):
        self.__twitterAccessTokenSecret = twitterAccessTokenSecret

class commons_SysConfig(Timestamped):

    def __init__(self, tenantId: str):
        self.tenantId = tenantId
        
    @property
    def tenantId(self) -> str:
        return self.__tenantId

    @tenantId.setter
    def tenantId(self, tenantId: str):
        self.__tenantId = tenantId

class commons_PersonCatalog:

    pass
class SchemaVersionable:

    pass
class commons_Email:

    def __init__(self, primary: bool, validationTime: str, email: str, commons_Email: "commons_Person" = None):
        self.primary = primary
        self.validationTime = validationTime
        self.email = email
        self.commons_Email = commons_Email
        
    @property
    def validationTime(self) -> str:
        return self.__validationTime

    @validationTime.setter
    def validationTime(self, validationTime: str):
        self.__validationTime = validationTime

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def commons_Email(self):
        return self.__commons_Email

    @commons_Email.setter
    def commons_Email(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Email__commons_Email", None)
        self.__commons_Email = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Person13"):
                opp_val = getattr(old_value, "commons_Person13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Person13"):
                opp_val = getattr(value, "commons_Person13", None)
                if opp_val is None:
                    setattr(value, "commons_Person13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class commons_PhoneNumber:

    def __init__(self, phoneNumber: str, primary: bool, validationTime: str, commons_PhoneNumber: "commons_Person" = None, commons_PhoneNumber16: "commons_Person" = None):
        self.phoneNumber = phoneNumber
        self.primary = primary
        self.validationTime = validationTime
        self.commons_PhoneNumber = commons_PhoneNumber
        self.commons_PhoneNumber16 = commons_PhoneNumber16
        
    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def validationTime(self) -> str:
        return self.__validationTime

    @validationTime.setter
    def validationTime(self, validationTime: str):
        self.__validationTime = validationTime

    @property
    def commons_PhoneNumber(self):
        return self.__commons_PhoneNumber

    @commons_PhoneNumber.setter
    def commons_PhoneNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_PhoneNumber__commons_PhoneNumber", None)
        self.__commons_PhoneNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Person"):
                opp_val = getattr(old_value, "commons_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Person"):
                opp_val = getattr(value, "commons_Person", None)
                if opp_val is None:
                    setattr(value, "commons_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def commons_PhoneNumber16(self):
        return self.__commons_PhoneNumber16

    @commons_PhoneNumber16.setter
    def commons_PhoneNumber16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_PhoneNumber__commons_PhoneNumber16", None)
        self.__commons_PhoneNumber16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Person15"):
                opp_val = getattr(old_value, "commons_Person15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Person15"):
                opp_val = getattr(value, "commons_Person15", None)
                if opp_val is None:
                    setattr(value, "commons_Person15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class commons_Person:

    def __init__(self, firstName: str, lastName: str, password: str, schemaVersion: str, googlePlusId: str, googleUsername: str, virtualMail: str, nickname: str, customerRole: str, memberRole: str, managerRole: str, timeZoneId: str, accountStatus: str, birthYear: str, birthMonth: str, birthDay: str, birthDate: str, gender: str, language: str, currencyCode: str, currency: str, folder: str, religion: str, passwordResetCode: str, passwordResetExpiryTime: str, clientAccessToken: str, securityRoleIds: str, timeZone: str, referrerId: str, referrerType: str, signupSource: str, signupSourceType: str, ipAddress: str, lastIpAddress: str, lastLoginTime: str, validationTime: str, activationTime: str, verificationTime: str, newsletterSubscriptionEnabled: str, newsletterSubscriptionTime: str, socialSharingEnabled: str, publicationStatus: str, archivalStatus: str, debitBalance: str, debitCurrency: str, type: str, verifyCode: str, zendeskUserId: str, customerRoleEditTime: str, lastTimeSynchronizeWithZendesk: str, zendeskIntegration: bool, commons_Person: set["commons_PhoneNumber"] = None, commons_Person13: set["commons_Email"] = None, commons_Person15: set["commons_PhoneNumber"] = None, commons_Person18: set["commons_PostalAddress"] = None, commons_Person20: set["commons_Organization"] = None, commons_Person22: "commons_PersonCatalog" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.schemaVersion = schemaVersion
        self.googlePlusId = googlePlusId
        self.googleUsername = googleUsername
        self.virtualMail = virtualMail
        self.nickname = nickname
        self.customerRole = customerRole
        self.memberRole = memberRole
        self.managerRole = managerRole
        self.timeZoneId = timeZoneId
        self.accountStatus = accountStatus
        self.birthYear = birthYear
        self.birthMonth = birthMonth
        self.birthDay = birthDay
        self.birthDate = birthDate
        self.gender = gender
        self.language = language
        self.currencyCode = currencyCode
        self.currency = currency
        self.folder = folder
        self.religion = religion
        self.passwordResetCode = passwordResetCode
        self.passwordResetExpiryTime = passwordResetExpiryTime
        self.clientAccessToken = clientAccessToken
        self.securityRoleIds = securityRoleIds
        self.timeZone = timeZone
        self.referrerId = referrerId
        self.referrerType = referrerType
        self.signupSource = signupSource
        self.signupSourceType = signupSourceType
        self.ipAddress = ipAddress
        self.lastIpAddress = lastIpAddress
        self.lastLoginTime = lastLoginTime
        self.validationTime = validationTime
        self.activationTime = activationTime
        self.verificationTime = verificationTime
        self.newsletterSubscriptionEnabled = newsletterSubscriptionEnabled
        self.newsletterSubscriptionTime = newsletterSubscriptionTime
        self.socialSharingEnabled = socialSharingEnabled
        self.publicationStatus = publicationStatus
        self.archivalStatus = archivalStatus
        self.debitBalance = debitBalance
        self.debitCurrency = debitCurrency
        self.type = type
        self.verifyCode = verifyCode
        self.zendeskUserId = zendeskUserId
        self.customerRoleEditTime = customerRoleEditTime
        self.lastTimeSynchronizeWithZendesk = lastTimeSynchronizeWithZendesk
        self.zendeskIntegration = zendeskIntegration
        self.commons_Person = commons_Person if commons_Person is not None else set()
        self.commons_Person13 = commons_Person13 if commons_Person13 is not None else set()
        self.commons_Person15 = commons_Person15 if commons_Person15 is not None else set()
        self.commons_Person18 = commons_Person18 if commons_Person18 is not None else set()
        self.commons_Person20 = commons_Person20 if commons_Person20 is not None else set()
        self.commons_Person22 = commons_Person22
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def birthDate(self) -> str:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def signupSourceType(self) -> str:
        return self.__signupSourceType

    @signupSourceType.setter
    def signupSourceType(self, signupSourceType: str):
        self.__signupSourceType = signupSourceType

    @property
    def zendeskIntegration(self) -> bool:
        return self.__zendeskIntegration

    @zendeskIntegration.setter
    def zendeskIntegration(self, zendeskIntegration: bool):
        self.__zendeskIntegration = zendeskIntegration

    @property
    def managerRole(self) -> str:
        return self.__managerRole

    @managerRole.setter
    def managerRole(self, managerRole: str):
        self.__managerRole = managerRole

    @property
    def activationTime(self) -> str:
        return self.__activationTime

    @activationTime.setter
    def activationTime(self, activationTime: str):
        self.__activationTime = activationTime

    @property
    def timeZone(self) -> str:
        return self.__timeZone

    @timeZone.setter
    def timeZone(self, timeZone: str):
        self.__timeZone = timeZone

    @property
    def lastTimeSynchronizeWithZendesk(self) -> str:
        return self.__lastTimeSynchronizeWithZendesk

    @lastTimeSynchronizeWithZendesk.setter
    def lastTimeSynchronizeWithZendesk(self, lastTimeSynchronizeWithZendesk: str):
        self.__lastTimeSynchronizeWithZendesk = lastTimeSynchronizeWithZendesk

    @property
    def birthYear(self) -> str:
        return self.__birthYear

    @birthYear.setter
    def birthYear(self, birthYear: str):
        self.__birthYear = birthYear

    @property
    def signupSource(self) -> str:
        return self.__signupSource

    @signupSource.setter
    def signupSource(self, signupSource: str):
        self.__signupSource = signupSource

    @property
    def securityRoleIds(self) -> str:
        return self.__securityRoleIds

    @securityRoleIds.setter
    def securityRoleIds(self, securityRoleIds: str):
        self.__securityRoleIds = securityRoleIds

    @property
    def lastLoginTime(self) -> str:
        return self.__lastLoginTime

    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: str):
        self.__lastLoginTime = lastLoginTime

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

    @property
    def accountStatus(self) -> str:
        return self.__accountStatus

    @accountStatus.setter
    def accountStatus(self, accountStatus: str):
        self.__accountStatus = accountStatus

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def timeZoneId(self) -> str:
        return self.__timeZoneId

    @timeZoneId.setter
    def timeZoneId(self, timeZoneId: str):
        self.__timeZoneId = timeZoneId

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def currency(self) -> str:
        return self.__currency

    @currency.setter
    def currency(self, currency: str):
        self.__currency = currency

    @property
    def virtualMail(self) -> str:
        return self.__virtualMail

    @virtualMail.setter
    def virtualMail(self, virtualMail: str):
        self.__virtualMail = virtualMail

    @property
    def publicationStatus(self) -> str:
        return self.__publicationStatus

    @publicationStatus.setter
    def publicationStatus(self, publicationStatus: str):
        self.__publicationStatus = publicationStatus

    @property
    def passwordResetCode(self) -> str:
        return self.__passwordResetCode

    @passwordResetCode.setter
    def passwordResetCode(self, passwordResetCode: str):
        self.__passwordResetCode = passwordResetCode

    @property
    def newsletterSubscriptionTime(self) -> str:
        return self.__newsletterSubscriptionTime

    @newsletterSubscriptionTime.setter
    def newsletterSubscriptionTime(self, newsletterSubscriptionTime: str):
        self.__newsletterSubscriptionTime = newsletterSubscriptionTime

    @property
    def customerRoleEditTime(self) -> str:
        return self.__customerRoleEditTime

    @customerRoleEditTime.setter
    def customerRoleEditTime(self, customerRoleEditTime: str):
        self.__customerRoleEditTime = customerRoleEditTime

    @property
    def currencyCode(self) -> str:
        return self.__currencyCode

    @currencyCode.setter
    def currencyCode(self, currencyCode: str):
        self.__currencyCode = currencyCode

    @property
    def customerRole(self) -> str:
        return self.__customerRole

    @customerRole.setter
    def customerRole(self, customerRole: str):
        self.__customerRole = customerRole

    @property
    def schemaVersion(self) -> str:
        return self.__schemaVersion

    @schemaVersion.setter
    def schemaVersion(self, schemaVersion: str):
        self.__schemaVersion = schemaVersion

    @property
    def verifyCode(self) -> str:
        return self.__verifyCode

    @verifyCode.setter
    def verifyCode(self, verifyCode: str):
        self.__verifyCode = verifyCode

    @property
    def validationTime(self) -> str:
        return self.__validationTime

    @validationTime.setter
    def validationTime(self, validationTime: str):
        self.__validationTime = validationTime

    @property
    def birthDay(self) -> str:
        return self.__birthDay

    @birthDay.setter
    def birthDay(self, birthDay: str):
        self.__birthDay = birthDay

    @property
    def referrerId(self) -> str:
        return self.__referrerId

    @referrerId.setter
    def referrerId(self, referrerId: str):
        self.__referrerId = referrerId

    @property
    def clientAccessToken(self) -> str:
        return self.__clientAccessToken

    @clientAccessToken.setter
    def clientAccessToken(self, clientAccessToken: str):
        self.__clientAccessToken = clientAccessToken

    @property
    def googlePlusId(self) -> str:
        return self.__googlePlusId

    @googlePlusId.setter
    def googlePlusId(self, googlePlusId: str):
        self.__googlePlusId = googlePlusId

    @property
    def ipAddress(self) -> str:
        return self.__ipAddress

    @ipAddress.setter
    def ipAddress(self, ipAddress: str):
        self.__ipAddress = ipAddress

    @property
    def passwordResetExpiryTime(self) -> str:
        return self.__passwordResetExpiryTime

    @passwordResetExpiryTime.setter
    def passwordResetExpiryTime(self, passwordResetExpiryTime: str):
        self.__passwordResetExpiryTime = passwordResetExpiryTime

    @property
    def zendeskUserId(self) -> str:
        return self.__zendeskUserId

    @zendeskUserId.setter
    def zendeskUserId(self, zendeskUserId: str):
        self.__zendeskUserId = zendeskUserId

    @property
    def verificationTime(self) -> str:
        return self.__verificationTime

    @verificationTime.setter
    def verificationTime(self, verificationTime: str):
        self.__verificationTime = verificationTime

    @property
    def debitCurrency(self) -> str:
        return self.__debitCurrency

    @debitCurrency.setter
    def debitCurrency(self, debitCurrency: str):
        self.__debitCurrency = debitCurrency

    @property
    def referrerType(self) -> str:
        return self.__referrerType

    @referrerType.setter
    def referrerType(self, referrerType: str):
        self.__referrerType = referrerType

    @property
    def newsletterSubscriptionEnabled(self) -> str:
        return self.__newsletterSubscriptionEnabled

    @newsletterSubscriptionEnabled.setter
    def newsletterSubscriptionEnabled(self, newsletterSubscriptionEnabled: str):
        self.__newsletterSubscriptionEnabled = newsletterSubscriptionEnabled

    @property
    def religion(self) -> str:
        return self.__religion

    @religion.setter
    def religion(self, religion: str):
        self.__religion = religion

    @property
    def birthMonth(self) -> str:
        return self.__birthMonth

    @birthMonth.setter
    def birthMonth(self, birthMonth: str):
        self.__birthMonth = birthMonth

    @property
    def socialSharingEnabled(self) -> str:
        return self.__socialSharingEnabled

    @socialSharingEnabled.setter
    def socialSharingEnabled(self, socialSharingEnabled: str):
        self.__socialSharingEnabled = socialSharingEnabled

    @property
    def archivalStatus(self) -> str:
        return self.__archivalStatus

    @archivalStatus.setter
    def archivalStatus(self, archivalStatus: str):
        self.__archivalStatus = archivalStatus

    @property
    def folder(self) -> str:
        return self.__folder

    @folder.setter
    def folder(self, folder: str):
        self.__folder = folder

    @property
    def memberRole(self) -> str:
        return self.__memberRole

    @memberRole.setter
    def memberRole(self, memberRole: str):
        self.__memberRole = memberRole

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def lastIpAddress(self) -> str:
        return self.__lastIpAddress

    @lastIpAddress.setter
    def lastIpAddress(self, lastIpAddress: str):
        self.__lastIpAddress = lastIpAddress

    @property
    def debitBalance(self) -> str:
        return self.__debitBalance

    @debitBalance.setter
    def debitBalance(self, debitBalance: str):
        self.__debitBalance = debitBalance

    @property
    def googleUsername(self) -> str:
        return self.__googleUsername

    @googleUsername.setter
    def googleUsername(self, googleUsername: str):
        self.__googleUsername = googleUsername

    @property
    def commons_Person18(self):
        return self.__commons_Person18

    @commons_Person18.setter
    def commons_Person18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Person__commons_Person18", None)
        self.__commons_Person18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_PostalAddress"):
                    opp_val = getattr(item, "commons_PostalAddress", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_PostalAddress", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_PostalAddress"):
                    opp_val = getattr(item, "commons_PostalAddress", None)
                    
                    setattr(item, "commons_PostalAddress", self)
                    

    @property
    def commons_Person13(self):
        return self.__commons_Person13

    @commons_Person13.setter
    def commons_Person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Person__commons_Person13", None)
        self.__commons_Person13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_Email"):
                    opp_val = getattr(item, "commons_Email", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_Email", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_Email"):
                    opp_val = getattr(item, "commons_Email", None)
                    
                    setattr(item, "commons_Email", self)
                    

    @property
    def commons_Person20(self):
        return self.__commons_Person20

    @commons_Person20.setter
    def commons_Person20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Person__commons_Person20", None)
        self.__commons_Person20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_Organization"):
                    opp_val = getattr(item, "commons_Organization", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_Organization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_Organization"):
                    opp_val = getattr(item, "commons_Organization", None)
                    
                    setattr(item, "commons_Organization", self)
                    

    @property
    def commons_Person(self):
        return self.__commons_Person

    @commons_Person.setter
    def commons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Person__commons_Person", None)
        self.__commons_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_PhoneNumber"):
                    opp_val = getattr(item, "commons_PhoneNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_PhoneNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_PhoneNumber"):
                    opp_val = getattr(item, "commons_PhoneNumber", None)
                    
                    setattr(item, "commons_PhoneNumber", self)
                    

    @property
    def commons_Person22(self):
        return self.__commons_Person22

    @commons_Person22.setter
    def commons_Person22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Person__commons_Person22", None)
        self.__commons_Person22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_PersonCatalog"):
                opp_val = getattr(old_value, "commons_PersonCatalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_PersonCatalog"):
                opp_val = getattr(value, "commons_PersonCatalog", None)
                if opp_val is None:
                    setattr(value, "commons_PersonCatalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def commons_Person15(self):
        return self.__commons_Person15

    @commons_Person15.setter
    def commons_Person15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Person__commons_Person15", None)
        self.__commons_Person15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_PhoneNumber16"):
                    opp_val = getattr(item, "commons_PhoneNumber16", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_PhoneNumber16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_PhoneNumber16"):
                    opp_val = getattr(item, "commons_PhoneNumber16", None)
                    
                    setattr(item, "commons_PhoneNumber16", self)
                    

    def putEmail(self, email: str) -> str:
        # TODO: Implement putEmail method
        pass

    def hasEmail(self, email: str) -> bool:
        # TODO: Implement hasEmail method
        pass

class commons_Expandable(ABC):

    def __init__(self, expansionState: str):
        self.expansionState = expansionState
        
    @property
    def expansionState(self) -> str:
        return self.__expansionState

    @expansionState.setter
    def expansionState(self, expansionState: str):
        self.__expansionState = expansionState

    def expand(self, scope: str):
        # TODO: Implement expand method
        pass

class commons_StyleConfiguration(ABC):

    def __init__(self):
        
    def getDefaultStyle(self) -> str:
        # TODO: Implement getDefaultStyle method
        pass

class commons_PersonLike(ABC):

    def __init__(self):
        
    def getPhotoId(self) -> str:
        # TODO: Implement getPhotoId method
        pass

    def getSlug(self) -> str:
        # TODO: Implement getSlug method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getId(self) -> str:
        # TODO: Implement getId method
        pass

    def getEmail(self) -> str:
        # TODO: Implement getEmail method
        pass

    def getGender(self) -> str:
        # TODO: Implement getGender method
        pass

class commons_Translation:

    def __init__(self, language: str, commons_Translation: set["commons_TranslationMessageEntry"] = None, commons_Translation10: "commons_TranslationEntry" = None):
        self.language = language
        self.commons_Translation = commons_Translation if commons_Translation is not None else set()
        self.commons_Translation10 = commons_Translation10
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def commons_Translation(self):
        return self.__commons_Translation

    @commons_Translation.setter
    def commons_Translation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Translation__commons_Translation", None)
        self.__commons_Translation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_TranslationMessageEntry"):
                    opp_val = getattr(item, "commons_TranslationMessageEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_TranslationMessageEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_TranslationMessageEntry"):
                    opp_val = getattr(item, "commons_TranslationMessageEntry", None)
                    
                    setattr(item, "commons_TranslationMessageEntry", self)
                    

    @property
    def commons_Translation10(self):
        return self.__commons_Translation10

    @commons_Translation10.setter
    def commons_Translation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Translation__commons_Translation10", None)
        self.__commons_Translation10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_TranslationEntry9"):
                opp_val = getattr(old_value, "commons_TranslationEntry9", None)
                if opp_val == self:
                    setattr(old_value, "commons_TranslationEntry9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_TranslationEntry9"):
                opp_val = getattr(value, "commons_TranslationEntry9", None)
                setattr(value, "commons_TranslationEntry9", self)

class commons_TranslationEntry:

    def __init__(self, key: str, commons_TranslationEntry: "commons_Translatable" = None, commons_TranslationEntry9: "commons_Translation" = None):
        self.key = key
        self.commons_TranslationEntry = commons_TranslationEntry
        self.commons_TranslationEntry9 = commons_TranslationEntry9
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def commons_TranslationEntry9(self):
        return self.__commons_TranslationEntry9

    @commons_TranslationEntry9.setter
    def commons_TranslationEntry9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_TranslationEntry__commons_TranslationEntry9", None)
        self.__commons_TranslationEntry9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Translation10"):
                opp_val = getattr(old_value, "commons_Translation10", None)
                if opp_val == self:
                    setattr(old_value, "commons_Translation10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Translation10"):
                opp_val = getattr(value, "commons_Translation10", None)
                setattr(value, "commons_Translation10", self)

    @property
    def commons_TranslationEntry(self):
        return self.__commons_TranslationEntry

    @commons_TranslationEntry.setter
    def commons_TranslationEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_TranslationEntry__commons_TranslationEntry", None)
        self.__commons_TranslationEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Translatable"):
                opp_val = getattr(old_value, "commons_Translatable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Translatable"):
                opp_val = getattr(value, "commons_Translatable", None)
                if opp_val is None:
                    setattr(value, "commons_Translatable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class commons_Translatable(ABC):

    def __init__(self, translationState: str, originalLanguage: str, language: str, commons_Translatable: set["commons_TranslationEntry"] = None):
        self.translationState = translationState
        self.originalLanguage = originalLanguage
        self.language = language
        self.commons_Translatable = commons_Translatable if commons_Translatable is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def translationState(self) -> str:
        return self.__translationState

    @translationState.setter
    def translationState(self, translationState: str):
        self.__translationState = translationState

    @property
    def originalLanguage(self) -> str:
        return self.__originalLanguage

    @originalLanguage.setter
    def originalLanguage(self, originalLanguage: str):
        self.__originalLanguage = originalLanguage

    @property
    def commons_Translatable(self):
        return self.__commons_Translatable

    @commons_Translatable.setter
    def commons_Translatable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Translatable__commons_Translatable", None)
        self.__commons_Translatable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_TranslationEntry"):
                    opp_val = getattr(item, "commons_TranslationEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_TranslationEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_TranslationEntry"):
                    opp_val = getattr(item, "commons_TranslationEntry", None)
                    
                    setattr(item, "commons_TranslationEntry", self)
                    

class commons_TranslationManager:

    def __init__(self):
        
    def translate(self, entity: str, targetLanguage: str):
        # TODO: Implement translate method
        pass

class commons_TranslationMessageEntry:

    def __init__(self, key: str, value: str, commons_TranslationMessageEntry: "commons_Translation" = None):
        self.key = key
        self.value = value
        self.commons_TranslationMessageEntry = commons_TranslationMessageEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def commons_TranslationMessageEntry(self):
        return self.__commons_TranslationMessageEntry

    @commons_TranslationMessageEntry.setter
    def commons_TranslationMessageEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_TranslationMessageEntry__commons_TranslationMessageEntry", None)
        self.__commons_TranslationMessageEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Translation"):
                opp_val = getattr(old_value, "commons_Translation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Translation"):
                opp_val = getattr(value, "commons_Translation", None)
                if opp_val is None:
                    setattr(value, "commons_Translation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class commons_Colorable(ABC):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class ProgressMonitor:

    pass
class commons_EventBusProgressMonitor(ProgressMonitor):

    def __init__(self, eventBus: str, trackingId: str):
        self.eventBus = eventBus
        self.trackingId = trackingId
        
    @property
    def eventBus(self) -> str:
        return self.__eventBus

    @eventBus.setter
    def eventBus(self, eventBus: str):
        self.__eventBus = eventBus

    @property
    def trackingId(self) -> str:
        return self.__trackingId

    @trackingId.setter
    def trackingId(self, trackingId: str):
        self.__trackingId = trackingId

class commons_ShellProgressMonitor(ProgressMonitor):

    pass
class commons_ProgressMonitorWrapper(ProgressMonitor):

    pass
class commons_ProgressMonitor(ABC):

    def __init__(self, canceled: bool, taskName: str, commons_ProgressMonitor: "commons_ProgressMonitorWrapper" = None):
        self.canceled = canceled
        self.taskName = taskName
        self.commons_ProgressMonitor = commons_ProgressMonitor
        
    @property
    def taskName(self) -> str:
        return self.__taskName

    @taskName.setter
    def taskName(self, taskName: str):
        self.__taskName = taskName

    @property
    def canceled(self) -> bool:
        return self.__canceled

    @canceled.setter
    def canceled(self, canceled: bool):
        self.__canceled = canceled

    @property
    def commons_ProgressMonitor(self):
        return self.__commons_ProgressMonitor

    @commons_ProgressMonitor.setter
    def commons_ProgressMonitor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_ProgressMonitor__commons_ProgressMonitor", None)
        self.__commons_ProgressMonitor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_ProgressMonitorWrapper"):
                opp_val = getattr(old_value, "commons_ProgressMonitorWrapper", None)
                if opp_val == self:
                    setattr(old_value, "commons_ProgressMonitorWrapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_ProgressMonitorWrapper"):
                opp_val = getattr(value, "commons_ProgressMonitorWrapper", None)
                setattr(value, "commons_ProgressMonitorWrapper", self)

    def done(self):
        # TODO: Implement done method
        pass

    def worked(self, work: str, status: str):
        # TODO: Implement worked method
        pass

    def done(self, status: str):
        # TODO: Implement done method
        pass

    def subTask(self, name: str):
        # TODO: Implement subTask method
        pass

    def beginTask(self, name: str, totalWork: str):
        # TODO: Implement beginTask method
        pass

    def internalWorked(self, work: float):
        # TODO: Implement internalWorked method
        pass

    def worked(self, work: str):
        # TODO: Implement worked method
        pass

class commons_CategoryInfo:

    def __init__(self, primaryUri: str, googleFormalId: str, commons_CategoryInfo: "commons_CategoryInfo" = None, commons_CategoryInfo3: set["commons_CategoryInfo"] = None):
        self.primaryUri = primaryUri
        self.googleFormalId = googleFormalId
        self.commons_CategoryInfo = commons_CategoryInfo
        self.commons_CategoryInfo3 = commons_CategoryInfo3 if commons_CategoryInfo3 is not None else set()
        
    @property
    def primaryUri(self) -> str:
        return self.__primaryUri

    @primaryUri.setter
    def primaryUri(self, primaryUri: str):
        self.__primaryUri = primaryUri

    @property
    def googleFormalId(self) -> str:
        return self.__googleFormalId

    @googleFormalId.setter
    def googleFormalId(self, googleFormalId: str):
        self.__googleFormalId = googleFormalId

    @property
    def commons_CategoryInfo(self):
        return self.__commons_CategoryInfo

    @commons_CategoryInfo.setter
    def commons_CategoryInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_CategoryInfo__commons_CategoryInfo", None)
        self.__commons_CategoryInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_CategoryInfo3"):
                opp_val = getattr(old_value, "commons_CategoryInfo3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_CategoryInfo3"):
                opp_val = getattr(value, "commons_CategoryInfo3", None)
                if opp_val is None:
                    setattr(value, "commons_CategoryInfo3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def commons_CategoryInfo3(self):
        return self.__commons_CategoryInfo3

    @commons_CategoryInfo3.setter
    def commons_CategoryInfo3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_CategoryInfo__commons_CategoryInfo3", None)
        self.__commons_CategoryInfo3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commons_CategoryInfo"):
                    opp_val = getattr(item, "commons_CategoryInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "commons_CategoryInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commons_CategoryInfo"):
                    opp_val = getattr(item, "commons_CategoryInfo", None)
                    
                    setattr(item, "commons_CategoryInfo", self)
                    

    def getEffectiveName(self, curLanguageTag: str) -> str:
        # TODO: Implement getEffectiveName method
        pass

class commons_EObjectLinked(ABC):

    def __init__(self):
        
    def getObject(self):
        # TODO: Implement getObject method
        pass

class commons_ObjectsNotification(ABC):

    def __init__(self, objects: str):
        self.objects = objects
        
    @property
    def objects(self) -> str:
        return self.__objects

    @objects.setter
    def objects(self, objects: str):
        self.__objects = objects

class commons_RemovedMany:

    pass
class commons_AddedMany:

    pass
class commons_EAttribute:

    pass
class commons_AttributeNotification:

    def __init__(self, object: str, oldValue: str, newValue: str, commons_AttributeNotification: "commons_EAttribute" = None):
        self.object = object
        self.oldValue = oldValue
        self.newValue = newValue
        self.commons_AttributeNotification = commons_AttributeNotification
        
    @property
    def newValue(self) -> str:
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue

    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

    @property
    def oldValue(self) -> str:
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue

    @property
    def commons_AttributeNotification(self):
        return self.__commons_AttributeNotification

    @commons_AttributeNotification.setter
    def commons_AttributeNotification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_AttributeNotification__commons_AttributeNotification", None)
        self.__commons_AttributeNotification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_EAttribute"):
                opp_val = getattr(old_value, "commons_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "commons_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_EAttribute"):
                opp_val = getattr(value, "commons_EAttribute", None)
                setattr(value, "commons_EAttribute", self)

class commons_ObjectNotification(ABC):

    def __init__(self, object: str):
        self.object = object
        
    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

class commons_Removed:

    pass
class commons_AttributeUnset:

    pass
class NsPrefixable:

    pass
class commons_Parentable(ABC):

    pass
class commons_EObject:

    pass
class commons_ModelNotification(ABC):

    pass
class commons_Added:

    pass
class commons_AttributeSet:

    def __init__(self, principals: str):
        self.principals = principals
        
    @property
    def principals(self) -> str:
        return self.__principals

    @principals.setter
    def principals(self, principals: str):
        self.__principals = principals

class commons_NsPrefixable(ABC):

    def __init__(self, nsPrefix: str):
        self.nsPrefix = nsPrefix
        
    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

class commons_EFactoryLinked(ABC):

    def __init__(self, eFactory: str):
        self.eFactory = eFactory
        
    @property
    def eFactory(self) -> str:
        return self.__eFactory

    @eFactory.setter
    def eFactory(self, eFactory: str):
        self.__eFactory = eFactory

class commons_SchemaVersionable(ABC):

    def __init__(self):
        
    def getSchemaVersion(self) -> str:
        # TODO: Implement getSchemaVersion method
        pass

class commons_EClass:

    pass
class commons_EClassLinked(ABC):

    def __init__(self, eClassName: str, ePackageName: str, eClassStatus: str, ePackageNsPrefix: str, commons_EClassLinked: "commons_EClass" = None):
        self.eClassName = eClassName
        self.ePackageName = ePackageName
        self.eClassStatus = eClassStatus
        self.ePackageNsPrefix = ePackageNsPrefix
        self.commons_EClassLinked = commons_EClassLinked
        
    @property
    def eClassStatus(self) -> str:
        return self.__eClassStatus

    @eClassStatus.setter
    def eClassStatus(self, eClassStatus: str):
        self.__eClassStatus = eClassStatus

    @property
    def ePackageNsPrefix(self) -> str:
        return self.__ePackageNsPrefix

    @ePackageNsPrefix.setter
    def ePackageNsPrefix(self, ePackageNsPrefix: str):
        self.__ePackageNsPrefix = ePackageNsPrefix

    @property
    def ePackageName(self) -> str:
        return self.__ePackageName

    @ePackageName.setter
    def ePackageName(self, ePackageName: str):
        self.__ePackageName = ePackageName

    @property
    def eClassName(self) -> str:
        return self.__eClassName

    @eClassName.setter
    def eClassName(self, eClassName: str):
        self.__eClassName = eClassName

    @property
    def commons_EClassLinked(self):
        return self.__commons_EClassLinked

    @commons_EClassLinked.setter
    def commons_EClassLinked(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_EClassLinked__commons_EClassLinked", None)
        self.__commons_EClassLinked = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_EClass"):
                opp_val = getattr(old_value, "commons_EClass", None)
                if opp_val == self:
                    setattr(old_value, "commons_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_EClass"):
                opp_val = getattr(value, "commons_EClass", None)
                setattr(value, "commons_EClass", self)

    def resolveEClass(self, eClassMap: str):
        # TODO: Implement resolveEClass method
        pass

class commons_BundleAware(ABC):

    def __init__(self, bundle: str):
        self.bundle = bundle
        
    @property
    def bundle(self) -> str:
        return self.__bundle

    @bundle.setter
    def bundle(self, bundle: str):
        self.__bundle = bundle

class commons_Describable(ABC):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class commons_Informer(ABC):

    def __init__(self):
        
    def toInfo(self):
        # TODO: Implement toInfo method
        pass

class Nameable:

    pass
class commons_NameContainer(Nameable):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Imageable:

    pass
class commons_PhotoIdContainer(Imageable):

    def __init__(self, photoId: str):
        self.photoId = photoId
        
    @property
    def photoId(self) -> str:
        return self.__photoId

    @photoId.setter
    def photoId(self, photoId: str):
        self.__photoId = photoId

class commons_JavaClassLinked(ABC):

    def __init__(self, javaClassName: str, javaClass: str, javaClassStatus: str):
        self.javaClassName = javaClassName
        self.javaClass = javaClass
        self.javaClassStatus = javaClassStatus
        
    @property
    def javaClassName(self) -> str:
        return self.__javaClassName

    @javaClassName.setter
    def javaClassName(self, javaClassName: str):
        self.__javaClassName = javaClassName

    @property
    def javaClass(self) -> str:
        return self.__javaClass

    @javaClass.setter
    def javaClass(self, javaClass: str):
        self.__javaClass = javaClass

    @property
    def javaClassStatus(self) -> str:
        return self.__javaClassStatus

    @javaClassStatus.setter
    def javaClassStatus(self, javaClassStatus: str):
        self.__javaClassStatus = javaClassStatus

    def resolveJavaClass(self, bundle: str):
        # TODO: Implement resolveJavaClass method
        pass

class commons_Sluggable(ABC):

    def __init__(self, slug: str):
        self.slug = slug
        
    @property
    def slug(self) -> str:
        return self.__slug

    @slug.setter
    def slug(self, slug: str):
        self.__slug = slug

class commons_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class commons_Imageable(ABC):

    def __init__(self):
        
    def getImageId(self) -> str:
        # TODO: Implement getImageId method
        pass

class commons_Nameable(ABC):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class PersonLike:

    pass
class NameContainer:

    pass
class Sluggable:

    pass
class commons_CanonicalSluggable(Sluggable):

    def __init__(self, canonicalSlug: str):
        self.canonicalSlug = canonicalSlug
        
    @property
    def canonicalSlug(self) -> str:
        return self.__canonicalSlug

    @canonicalSlug.setter
    def canonicalSlug(self, canonicalSlug: str):
        self.__canonicalSlug = canonicalSlug

class PhotoIdContainer:

    pass
class Identifiable:

    pass
class commons_ThingInfo(Sluggable, Identifiable, NameContainer, Imageable):

    def __init__(self, imageId: str):
        self.imageId = imageId
        
    @property
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

class commons_CustomerRole(Identifiable, NameContainer, Describable, SchemaVersionable, Timestamped):

    def __init__(self, readOnly: bool, quickShopEnabled: bool, salesOrderReportEnabled: bool, historySalesOrderEnabled: bool, schemaVersion: str, status: str, agentSalesReportEnabled: bool, transactionHistoryEnabled: bool, bookingEnabled: bool, paymentGatewayEnabled: bool, bookingExpiryTimeInMinutes: int, dropshipEnabled: bool, reviewReminderEnabled: bool, zendeskIntegration: bool, zendeskOrganizationId: str):
        self.readOnly = readOnly
        self.quickShopEnabled = quickShopEnabled
        self.salesOrderReportEnabled = salesOrderReportEnabled
        self.historySalesOrderEnabled = historySalesOrderEnabled
        self.schemaVersion = schemaVersion
        self.status = status
        self.agentSalesReportEnabled = agentSalesReportEnabled
        self.transactionHistoryEnabled = transactionHistoryEnabled
        self.bookingEnabled = bookingEnabled
        self.paymentGatewayEnabled = paymentGatewayEnabled
        self.bookingExpiryTimeInMinutes = bookingExpiryTimeInMinutes
        self.dropshipEnabled = dropshipEnabled
        self.reviewReminderEnabled = reviewReminderEnabled
        self.zendeskIntegration = zendeskIntegration
        self.zendeskOrganizationId = zendeskOrganizationId
        
    @property
    def bookingEnabled(self) -> bool:
        return self.__bookingEnabled

    @bookingEnabled.setter
    def bookingEnabled(self, bookingEnabled: bool):
        self.__bookingEnabled = bookingEnabled

    @property
    def transactionHistoryEnabled(self) -> bool:
        return self.__transactionHistoryEnabled

    @transactionHistoryEnabled.setter
    def transactionHistoryEnabled(self, transactionHistoryEnabled: bool):
        self.__transactionHistoryEnabled = transactionHistoryEnabled

    @property
    def bookingExpiryTimeInMinutes(self) -> int:
        return self.__bookingExpiryTimeInMinutes

    @bookingExpiryTimeInMinutes.setter
    def bookingExpiryTimeInMinutes(self, bookingExpiryTimeInMinutes: int):
        self.__bookingExpiryTimeInMinutes = bookingExpiryTimeInMinutes

    @property
    def paymentGatewayEnabled(self) -> bool:
        return self.__paymentGatewayEnabled

    @paymentGatewayEnabled.setter
    def paymentGatewayEnabled(self, paymentGatewayEnabled: bool):
        self.__paymentGatewayEnabled = paymentGatewayEnabled

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def zendeskIntegration(self) -> bool:
        return self.__zendeskIntegration

    @zendeskIntegration.setter
    def zendeskIntegration(self, zendeskIntegration: bool):
        self.__zendeskIntegration = zendeskIntegration

    @property
    def zendeskOrganizationId(self) -> str:
        return self.__zendeskOrganizationId

    @zendeskOrganizationId.setter
    def zendeskOrganizationId(self, zendeskOrganizationId: str):
        self.__zendeskOrganizationId = zendeskOrganizationId

    @property
    def dropshipEnabled(self) -> bool:
        return self.__dropshipEnabled

    @dropshipEnabled.setter
    def dropshipEnabled(self, dropshipEnabled: bool):
        self.__dropshipEnabled = dropshipEnabled

    @property
    def schemaVersion(self) -> str:
        return self.__schemaVersion

    @schemaVersion.setter
    def schemaVersion(self, schemaVersion: str):
        self.__schemaVersion = schemaVersion

    @property
    def salesOrderReportEnabled(self) -> bool:
        return self.__salesOrderReportEnabled

    @salesOrderReportEnabled.setter
    def salesOrderReportEnabled(self, salesOrderReportEnabled: bool):
        self.__salesOrderReportEnabled = salesOrderReportEnabled

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def agentSalesReportEnabled(self) -> bool:
        return self.__agentSalesReportEnabled

    @agentSalesReportEnabled.setter
    def agentSalesReportEnabled(self, agentSalesReportEnabled: bool):
        self.__agentSalesReportEnabled = agentSalesReportEnabled

    @property
    def historySalesOrderEnabled(self) -> bool:
        return self.__historySalesOrderEnabled

    @historySalesOrderEnabled.setter
    def historySalesOrderEnabled(self, historySalesOrderEnabled: bool):
        self.__historySalesOrderEnabled = historySalesOrderEnabled

    @property
    def quickShopEnabled(self) -> bool:
        return self.__quickShopEnabled

    @quickShopEnabled.setter
    def quickShopEnabled(self, quickShopEnabled: bool):
        self.__quickShopEnabled = quickShopEnabled

    @property
    def reviewReminderEnabled(self) -> bool:
        return self.__reviewReminderEnabled

    @reviewReminderEnabled.setter
    def reviewReminderEnabled(self, reviewReminderEnabled: bool):
        self.__reviewReminderEnabled = reviewReminderEnabled

class commons_Organization(SchemaVersionable, NameContainer, Identifiable):

    def __init__(self, schemaVersion: str, blackBerryPin: str, website: str, facebookPageUri: str, facebookAccessToken: str, facebookId: str, facebookUserName: str, twitterScreenName: str, twitterAccessToken: str, twitterAccessTokenSecret: str, twitterId: str, commons_Organization: "commons_Person" = None):
        self.schemaVersion = schemaVersion
        self.blackBerryPin = blackBerryPin
        self.website = website
        self.facebookPageUri = facebookPageUri
        self.facebookAccessToken = facebookAccessToken
        self.facebookId = facebookId
        self.facebookUserName = facebookUserName
        self.twitterScreenName = twitterScreenName
        self.twitterAccessToken = twitterAccessToken
        self.twitterAccessTokenSecret = twitterAccessTokenSecret
        self.twitterId = twitterId
        self.commons_Organization = commons_Organization
        
    @property
    def twitterAccessTokenSecret(self) -> str:
        return self.__twitterAccessTokenSecret

    @twitterAccessTokenSecret.setter
    def twitterAccessTokenSecret(self, twitterAccessTokenSecret: str):
        self.__twitterAccessTokenSecret = twitterAccessTokenSecret

    @property
    def website(self) -> str:
        return self.__website

    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def facebookId(self) -> str:
        return self.__facebookId

    @facebookId.setter
    def facebookId(self, facebookId: str):
        self.__facebookId = facebookId

    @property
    def facebookAccessToken(self) -> str:
        return self.__facebookAccessToken

    @facebookAccessToken.setter
    def facebookAccessToken(self, facebookAccessToken: str):
        self.__facebookAccessToken = facebookAccessToken

    @property
    def blackBerryPin(self) -> str:
        return self.__blackBerryPin

    @blackBerryPin.setter
    def blackBerryPin(self, blackBerryPin: str):
        self.__blackBerryPin = blackBerryPin

    @property
    def schemaVersion(self) -> str:
        return self.__schemaVersion

    @schemaVersion.setter
    def schemaVersion(self, schemaVersion: str):
        self.__schemaVersion = schemaVersion

    @property
    def twitterScreenName(self) -> str:
        return self.__twitterScreenName

    @twitterScreenName.setter
    def twitterScreenName(self, twitterScreenName: str):
        self.__twitterScreenName = twitterScreenName

    @property
    def twitterId(self) -> str:
        return self.__twitterId

    @twitterId.setter
    def twitterId(self, twitterId: str):
        self.__twitterId = twitterId

    @property
    def facebookUserName(self) -> str:
        return self.__facebookUserName

    @facebookUserName.setter
    def facebookUserName(self, facebookUserName: str):
        self.__facebookUserName = facebookUserName

    @property
    def facebookPageUri(self) -> str:
        return self.__facebookPageUri

    @facebookPageUri.setter
    def facebookPageUri(self, facebookPageUri: str):
        self.__facebookPageUri = facebookPageUri

    @property
    def twitterAccessToken(self) -> str:
        return self.__twitterAccessToken

    @twitterAccessToken.setter
    def twitterAccessToken(self, twitterAccessToken: str):
        self.__twitterAccessToken = twitterAccessToken

    @property
    def commons_Organization(self):
        return self.__commons_Organization

    @commons_Organization.setter
    def commons_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_Organization__commons_Organization", None)
        self.__commons_Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Person20"):
                opp_val = getattr(old_value, "commons_Person20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Person20"):
                opp_val = getattr(value, "commons_Person20", None)
                if opp_val is None:
                    setattr(value, "commons_Person20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class commons_PostalAddress(Identifiable, NameContainer, SchemaVersionable):

    def __init__(self, workPhones: str, primaryEmail: str, emails: str, description: str, schemaVersion: str, organization: str, street: str, city: str, postalCode: str, province: str, country: str, countryCode: str, primaryMobile: str, mobiles: str, primaryPhone: str, phones: str, primaryHomePhone: str, homePhones: str, primaryWorkPhone: str, primary: bool, primaryBilling: bool, primaryShipping: bool, validationTime: str, district: str, jneAreaCode: str, commons_PostalAddress: "commons_Person" = None):
        self.workPhones = workPhones
        self.primaryEmail = primaryEmail
        self.emails = emails
        self.description = description
        self.schemaVersion = schemaVersion
        self.organization = organization
        self.street = street
        self.city = city
        self.postalCode = postalCode
        self.province = province
        self.country = country
        self.countryCode = countryCode
        self.primaryMobile = primaryMobile
        self.mobiles = mobiles
        self.primaryPhone = primaryPhone
        self.phones = phones
        self.primaryHomePhone = primaryHomePhone
        self.homePhones = homePhones
        self.primaryWorkPhone = primaryWorkPhone
        self.primary = primary
        self.primaryBilling = primaryBilling
        self.primaryShipping = primaryShipping
        self.validationTime = validationTime
        self.district = district
        self.jneAreaCode = jneAreaCode
        self.commons_PostalAddress = commons_PostalAddress
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def jneAreaCode(self) -> str:
        return self.__jneAreaCode

    @jneAreaCode.setter
    def jneAreaCode(self, jneAreaCode: str):
        self.__jneAreaCode = jneAreaCode

    @property
    def schemaVersion(self) -> str:
        return self.__schemaVersion

    @schemaVersion.setter
    def schemaVersion(self, schemaVersion: str):
        self.__schemaVersion = schemaVersion

    @property
    def primaryBilling(self) -> bool:
        return self.__primaryBilling

    @primaryBilling.setter
    def primaryBilling(self, primaryBilling: bool):
        self.__primaryBilling = primaryBilling

    @property
    def primaryMobile(self) -> str:
        return self.__primaryMobile

    @primaryMobile.setter
    def primaryMobile(self, primaryMobile: str):
        self.__primaryMobile = primaryMobile

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def countryCode(self) -> str:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: str):
        self.__countryCode = countryCode

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def primaryEmail(self) -> str:
        return self.__primaryEmail

    @primaryEmail.setter
    def primaryEmail(self, primaryEmail: str):
        self.__primaryEmail = primaryEmail

    @property
    def homePhones(self) -> str:
        return self.__homePhones

    @homePhones.setter
    def homePhones(self, homePhones: str):
        self.__homePhones = homePhones

    @property
    def primaryWorkPhone(self) -> str:
        return self.__primaryWorkPhone

    @primaryWorkPhone.setter
    def primaryWorkPhone(self, primaryWorkPhone: str):
        self.__primaryWorkPhone = primaryWorkPhone

    @property
    def primaryShipping(self) -> bool:
        return self.__primaryShipping

    @primaryShipping.setter
    def primaryShipping(self, primaryShipping: bool):
        self.__primaryShipping = primaryShipping

    @property
    def workPhones(self) -> str:
        return self.__workPhones

    @workPhones.setter
    def workPhones(self, workPhones: str):
        self.__workPhones = workPhones

    @property
    def phones(self) -> str:
        return self.__phones

    @phones.setter
    def phones(self, phones: str):
        self.__phones = phones

    @property
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def validationTime(self) -> str:
        return self.__validationTime

    @validationTime.setter
    def validationTime(self, validationTime: str):
        self.__validationTime = validationTime

    @property
    def primaryHomePhone(self) -> str:
        return self.__primaryHomePhone

    @primaryHomePhone.setter
    def primaryHomePhone(self, primaryHomePhone: str):
        self.__primaryHomePhone = primaryHomePhone

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def district(self) -> str:
        return self.__district

    @district.setter
    def district(self, district: str):
        self.__district = district

    @property
    def primaryPhone(self) -> str:
        return self.__primaryPhone

    @primaryPhone.setter
    def primaryPhone(self, primaryPhone: str):
        self.__primaryPhone = primaryPhone

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def province(self) -> str:
        return self.__province

    @province.setter
    def province(self, province: str):
        self.__province = province

    @property
    def mobiles(self) -> str:
        return self.__mobiles

    @mobiles.setter
    def mobiles(self, mobiles: str):
        self.__mobiles = mobiles

    @property
    def emails(self) -> str:
        return self.__emails

    @emails.setter
    def emails(self, emails: str):
        self.__emails = emails

    @property
    def commons_PostalAddress(self):
        return self.__commons_PostalAddress

    @commons_PostalAddress.setter
    def commons_PostalAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_commons_PostalAddress__commons_PostalAddress", None)
        self.__commons_PostalAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commons_Person18"):
                opp_val = getattr(old_value, "commons_Person18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commons_Person18"):
                opp_val = getattr(value, "commons_Person18", None)
                if opp_val is None:
                    setattr(value, "commons_Person18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class commons_PersonInfo(Identifiable, NameContainer, PersonLike, PhotoIdContainer, Sluggable):

    def __init__(self, gender: str, email: str, mobileNumber: str):
        self.gender = gender
        self.email = email
        self.mobileNumber = mobileNumber
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def mobileNumber(self) -> str:
        return self.__mobileNumber

    @mobileNumber.setter
    def mobileNumber(self, mobileNumber: str):
        self.__mobileNumber = mobileNumber

class commons_Timestamped(ABC):

    def __init__(self, creationTime: str, modificationTime: str):
        self.creationTime = creationTime
        self.modificationTime = modificationTime
        
    @property
    def creationTime(self) -> str:
        return self.__creationTime

    @creationTime.setter
    def creationTime(self, creationTime: str):
        self.__creationTime = creationTime

    @property
    def modificationTime(self) -> str:
        return self.__modificationTime

    @modificationTime.setter
    def modificationTime(self, modificationTime: str):
        self.__modificationTime = modificationTime

class commons_ResourceAware(ABC):

    def __init__(self, resourceType: str, resourceUri: str, resourceName: str):
        self.resourceType = resourceType
        self.resourceUri = resourceUri
        self.resourceName = resourceName
        
    @property
    def resourceUri(self) -> str:
        return self.__resourceUri

    @resourceUri.setter
    def resourceUri(self, resourceUri: str):
        self.__resourceUri = resourceUri

    @property
    def resourceName(self) -> str:
        return self.__resourceName

    @resourceName.setter
    def resourceName(self, resourceName: str):
        self.__resourceName = resourceName

    @property
    def resourceType(self) -> str:
        return self.__resourceType

    @resourceType.setter
    def resourceType(self, resourceType: str):
        self.__resourceType = resourceType

class Expandable:

    pass
class commons_GeneralSysConfig(Expandable, SysConfig):

    def __init__(self, sslSupported: str):
        self.sslSupported = sslSupported
        
    @property
    def sslSupported(self) -> str:
        return self.__sslSupported

    @sslSupported.setter
    def sslSupported(self, sslSupported: str):
        self.__sslSupported = sslSupported

class BundleAware:

    pass
class ResourceAware:

    pass
class Positionable:

    pass
class commons_CategoryLike(Identifiable, NameContainer, NsPrefixable, Positionable, Sluggable, Imageable):

    def __init__(self, slugPath: str, color: str, imageId: str, level: str, categoryCount: str):
        self.slugPath = slugPath
        self.color = color
        self.imageId = imageId
        self.level = level
        self.categoryCount = categoryCount
        
    @property
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

    @property
    def slugPath(self) -> str:
        return self.__slugPath

    @slugPath.setter
    def slugPath(self, slugPath: str):
        self.__slugPath = slugPath

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def categoryCount(self) -> str:
        return self.__categoryCount

    @categoryCount.setter
    def categoryCount(self, categoryCount: str):
        self.__categoryCount = categoryCount

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class commons_WebAddress(Expandable, Positionable, BundleAware, ResourceAware):

    def __init__(self, apiPath: str, imagesUri: str, baseUri: str, basePath: str, skinUri: str, jsUri: str, secureBaseUri: str, secureImagesUri: str, secureSkinUri: str, secureJsUri: str):
        self.apiPath = apiPath
        self.imagesUri = imagesUri
        self.baseUri = baseUri
        self.basePath = basePath
        self.skinUri = skinUri
        self.jsUri = jsUri
        self.secureBaseUri = secureBaseUri
        self.secureImagesUri = secureImagesUri
        self.secureSkinUri = secureSkinUri
        self.secureJsUri = secureJsUri
        
    @property
    def secureImagesUri(self) -> str:
        return self.__secureImagesUri

    @secureImagesUri.setter
    def secureImagesUri(self, secureImagesUri: str):
        self.__secureImagesUri = secureImagesUri

    @property
    def apiPath(self) -> str:
        return self.__apiPath

    @apiPath.setter
    def apiPath(self, apiPath: str):
        self.__apiPath = apiPath

    @property
    def skinUri(self) -> str:
        return self.__skinUri

    @skinUri.setter
    def skinUri(self, skinUri: str):
        self.__skinUri = skinUri

    @property
    def basePath(self) -> str:
        return self.__basePath

    @basePath.setter
    def basePath(self, basePath: str):
        self.__basePath = basePath

    @property
    def imagesUri(self) -> str:
        return self.__imagesUri

    @imagesUri.setter
    def imagesUri(self, imagesUri: str):
        self.__imagesUri = imagesUri

    @property
    def secureBaseUri(self) -> str:
        return self.__secureBaseUri

    @secureBaseUri.setter
    def secureBaseUri(self, secureBaseUri: str):
        self.__secureBaseUri = secureBaseUri

    @property
    def secureJsUri(self) -> str:
        return self.__secureJsUri

    @secureJsUri.setter
    def secureJsUri(self, secureJsUri: str):
        self.__secureJsUri = secureJsUri

    @property
    def secureSkinUri(self) -> str:
        return self.__secureSkinUri

    @secureSkinUri.setter
    def secureSkinUri(self, secureSkinUri: str):
        self.__secureSkinUri = secureSkinUri

    @property
    def jsUri(self) -> str:
        return self.__jsUri

    @jsUri.setter
    def jsUri(self, jsUri: str):
        self.__jsUri = jsUri

    @property
    def baseUri(self) -> str:
        return self.__baseUri

    @baseUri.setter
    def baseUri(self, baseUri: str):
        self.__baseUri = baseUri

    def getSecureApiUri(self) -> str:
        # TODO: Implement getSecureApiUri method
        pass

    def getApiUri(self) -> str:
        # TODO: Implement getApiUri method
        pass

class commons_AppManifest(Positionable, BundleAware, Expandable, ResourceAware):

    def __init__(self, defaultTimeZone: str, defaultCurrencyCode: str, title: str, summary: str, description: str, domain: str, domainPrd: str, domainDev: str, domainStg: str, generalEmail: str, generalEmailPrd: str, generalEmailDev: str, generalEmailStg: str, organizationName: str, organizationAddress: str, organizationPhoneNumbers: str, defaultTimeZoneId: str, reminderSchedule: str, reminderPeriodStr: str, defaultCurrency: str, defaultLanguageTag: str, defaultCountryCode: str, defaultCategoryUName: str, emailLogoUriTemplate: str, letterSalutation: str, letterClosing: str, footnote: str, wwwUsed: str, headNote: str, headTitle: str, defaultStyle: str, defaultVariation: str, kursDollarPaypal: str, kursDollarDpex: str, reminderPeriod: str, reminderScheduleStr: str, supportEmail: str, shipmentLogoUriTemplate: str):
        self.defaultTimeZone = defaultTimeZone
        self.defaultCurrencyCode = defaultCurrencyCode
        self.title = title
        self.summary = summary
        self.description = description
        self.domain = domain
        self.domainPrd = domainPrd
        self.domainDev = domainDev
        self.domainStg = domainStg
        self.generalEmail = generalEmail
        self.generalEmailPrd = generalEmailPrd
        self.generalEmailDev = generalEmailDev
        self.generalEmailStg = generalEmailStg
        self.organizationName = organizationName
        self.organizationAddress = organizationAddress
        self.organizationPhoneNumbers = organizationPhoneNumbers
        self.defaultTimeZoneId = defaultTimeZoneId
        self.reminderSchedule = reminderSchedule
        self.reminderPeriodStr = reminderPeriodStr
        self.defaultCurrency = defaultCurrency
        self.defaultLanguageTag = defaultLanguageTag
        self.defaultCountryCode = defaultCountryCode
        self.defaultCategoryUName = defaultCategoryUName
        self.emailLogoUriTemplate = emailLogoUriTemplate
        self.letterSalutation = letterSalutation
        self.letterClosing = letterClosing
        self.footnote = footnote
        self.wwwUsed = wwwUsed
        self.headNote = headNote
        self.headTitle = headTitle
        self.defaultStyle = defaultStyle
        self.defaultVariation = defaultVariation
        self.kursDollarPaypal = kursDollarPaypal
        self.kursDollarDpex = kursDollarDpex
        self.reminderPeriod = reminderPeriod
        self.reminderScheduleStr = reminderScheduleStr
        self.supportEmail = supportEmail
        self.shipmentLogoUriTemplate = shipmentLogoUriTemplate
        
    @property
    def letterClosing(self) -> str:
        return self.__letterClosing

    @letterClosing.setter
    def letterClosing(self, letterClosing: str):
        self.__letterClosing = letterClosing

    @property
    def reminderScheduleStr(self) -> str:
        return self.__reminderScheduleStr

    @reminderScheduleStr.setter
    def reminderScheduleStr(self, reminderScheduleStr: str):
        self.__reminderScheduleStr = reminderScheduleStr

    @property
    def defaultCurrencyCode(self) -> str:
        return self.__defaultCurrencyCode

    @defaultCurrencyCode.setter
    def defaultCurrencyCode(self, defaultCurrencyCode: str):
        self.__defaultCurrencyCode = defaultCurrencyCode

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def reminderPeriod(self) -> str:
        return self.__reminderPeriod

    @reminderPeriod.setter
    def reminderPeriod(self, reminderPeriod: str):
        self.__reminderPeriod = reminderPeriod

    @property
    def defaultTimeZone(self) -> str:
        return self.__defaultTimeZone

    @defaultTimeZone.setter
    def defaultTimeZone(self, defaultTimeZone: str):
        self.__defaultTimeZone = defaultTimeZone

    @property
    def defaultCategoryUName(self) -> str:
        return self.__defaultCategoryUName

    @defaultCategoryUName.setter
    def defaultCategoryUName(self, defaultCategoryUName: str):
        self.__defaultCategoryUName = defaultCategoryUName

    @property
    def domainDev(self) -> str:
        return self.__domainDev

    @domainDev.setter
    def domainDev(self, domainDev: str):
        self.__domainDev = domainDev

    @property
    def headNote(self) -> str:
        return self.__headNote

    @headNote.setter
    def headNote(self, headNote: str):
        self.__headNote = headNote

    @property
    def domainStg(self) -> str:
        return self.__domainStg

    @domainStg.setter
    def domainStg(self, domainStg: str):
        self.__domainStg = domainStg

    @property
    def organizationPhoneNumbers(self) -> str:
        return self.__organizationPhoneNumbers

    @organizationPhoneNumbers.setter
    def organizationPhoneNumbers(self, organizationPhoneNumbers: str):
        self.__organizationPhoneNumbers = organizationPhoneNumbers

    @property
    def generalEmailPrd(self) -> str:
        return self.__generalEmailPrd

    @generalEmailPrd.setter
    def generalEmailPrd(self, generalEmailPrd: str):
        self.__generalEmailPrd = generalEmailPrd

    @property
    def generalEmailStg(self) -> str:
        return self.__generalEmailStg

    @generalEmailStg.setter
    def generalEmailStg(self, generalEmailStg: str):
        self.__generalEmailStg = generalEmailStg

    @property
    def reminderSchedule(self) -> str:
        return self.__reminderSchedule

    @reminderSchedule.setter
    def reminderSchedule(self, reminderSchedule: str):
        self.__reminderSchedule = reminderSchedule

    @property
    def defaultStyle(self) -> str:
        return self.__defaultStyle

    @defaultStyle.setter
    def defaultStyle(self, defaultStyle: str):
        self.__defaultStyle = defaultStyle

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def defaultLanguageTag(self) -> str:
        return self.__defaultLanguageTag

    @defaultLanguageTag.setter
    def defaultLanguageTag(self, defaultLanguageTag: str):
        self.__defaultLanguageTag = defaultLanguageTag

    @property
    def defaultCountryCode(self) -> str:
        return self.__defaultCountryCode

    @defaultCountryCode.setter
    def defaultCountryCode(self, defaultCountryCode: str):
        self.__defaultCountryCode = defaultCountryCode

    @property
    def generalEmail(self) -> str:
        return self.__generalEmail

    @generalEmail.setter
    def generalEmail(self, generalEmail: str):
        self.__generalEmail = generalEmail

    @property
    def generalEmailDev(self) -> str:
        return self.__generalEmailDev

    @generalEmailDev.setter
    def generalEmailDev(self, generalEmailDev: str):
        self.__generalEmailDev = generalEmailDev

    @property
    def shipmentLogoUriTemplate(self) -> str:
        return self.__shipmentLogoUriTemplate

    @shipmentLogoUriTemplate.setter
    def shipmentLogoUriTemplate(self, shipmentLogoUriTemplate: str):
        self.__shipmentLogoUriTemplate = shipmentLogoUriTemplate

    @property
    def defaultTimeZoneId(self) -> str:
        return self.__defaultTimeZoneId

    @defaultTimeZoneId.setter
    def defaultTimeZoneId(self, defaultTimeZoneId: str):
        self.__defaultTimeZoneId = defaultTimeZoneId

    @property
    def domainPrd(self) -> str:
        return self.__domainPrd

    @domainPrd.setter
    def domainPrd(self, domainPrd: str):
        self.__domainPrd = domainPrd

    @property
    def kursDollarDpex(self) -> str:
        return self.__kursDollarDpex

    @kursDollarDpex.setter
    def kursDollarDpex(self, kursDollarDpex: str):
        self.__kursDollarDpex = kursDollarDpex

    @property
    def defaultVariation(self) -> str:
        return self.__defaultVariation

    @defaultVariation.setter
    def defaultVariation(self, defaultVariation: str):
        self.__defaultVariation = defaultVariation

    @property
    def letterSalutation(self) -> str:
        return self.__letterSalutation

    @letterSalutation.setter
    def letterSalutation(self, letterSalutation: str):
        self.__letterSalutation = letterSalutation

    @property
    def defaultCurrency(self) -> str:
        return self.__defaultCurrency

    @defaultCurrency.setter
    def defaultCurrency(self, defaultCurrency: str):
        self.__defaultCurrency = defaultCurrency

    @property
    def organizationName(self) -> str:
        return self.__organizationName

    @organizationName.setter
    def organizationName(self, organizationName: str):
        self.__organizationName = organizationName

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def emailLogoUriTemplate(self) -> str:
        return self.__emailLogoUriTemplate

    @emailLogoUriTemplate.setter
    def emailLogoUriTemplate(self, emailLogoUriTemplate: str):
        self.__emailLogoUriTemplate = emailLogoUriTemplate

    @property
    def kursDollarPaypal(self) -> str:
        return self.__kursDollarPaypal

    @kursDollarPaypal.setter
    def kursDollarPaypal(self, kursDollarPaypal: str):
        self.__kursDollarPaypal = kursDollarPaypal

    @property
    def reminderPeriodStr(self) -> str:
        return self.__reminderPeriodStr

    @reminderPeriodStr.setter
    def reminderPeriodStr(self, reminderPeriodStr: str):
        self.__reminderPeriodStr = reminderPeriodStr

    @property
    def organizationAddress(self) -> str:
        return self.__organizationAddress

    @organizationAddress.setter
    def organizationAddress(self, organizationAddress: str):
        self.__organizationAddress = organizationAddress

    @property
    def headTitle(self) -> str:
        return self.__headTitle

    @headTitle.setter
    def headTitle(self, headTitle: str):
        self.__headTitle = headTitle

    @property
    def footnote(self) -> str:
        return self.__footnote

    @footnote.setter
    def footnote(self, footnote: str):
        self.__footnote = footnote

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def wwwUsed(self) -> str:
        return self.__wwwUsed

    @wwwUsed.setter
    def wwwUsed(self, wwwUsed: str):
        self.__wwwUsed = wwwUsed

    @property
    def supportEmail(self) -> str:
        return self.__supportEmail

    @supportEmail.setter
    def supportEmail(self, supportEmail: str):
        self.__supportEmail = supportEmail

    def getDefaultLocale(self) -> str:
        # TODO: Implement getDefaultLocale method
        pass

    def getWebHost(self) -> str:
        # TODO: Implement getWebHost method
        pass

class commons_Positionable(ABC):

    def __init__(self, positioner: str):
        self.positioner = positioner
        
    @property
    def positioner(self) -> str:
        return self.__positioner

    @positioner.setter
    def positioner(self, positioner: str):
        self.__positioner = positioner
